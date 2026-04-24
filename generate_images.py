"""
Generates images for every verse of the Bhagavad Gita using Pollinations.ai
(free, no API key required — https://pollinations.ai).

- Reads bhagavad_gita_prompts_flat.json
- For each verse, requests a 1024×1024 image with its prompt
- Saves to gita_images/ch{NN}/ch{NN}_v{NNN}.jpg
- Resumable: skips any file that already exists and is non-trivial in size
- Concurrent but gentle (4 parallel workers, retries with backoff) to stay
  on the right side of Pollinations' free-tier rate limits
"""
import concurrent.futures
import hashlib
import json
import pathlib
import sys
import time
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).parent
IMAGES_DIR = ROOT / "gita_images"
IMAGES_DIR.mkdir(exist_ok=True)

BASE = "https://image.pollinations.ai/prompt/"
# flux is the highest-quality free model on Pollinations; 1024x1024 square.
QUERY = "width=1024&height=1024&nologo=true&model=flux"
TIMEOUT = 180
MIN_BYTES = 5_000  # anything smaller is an error page, not an image
MAX_WORKERS = 1    # Pollinations free tier rate-limits aggressively
RETRIES = 6
# Pollinations' free tier allows ~1 request per 5–10s. Throttle in-process.
REQUEST_INTERVAL = 6.0


def path_for(item: dict) -> pathlib.Path:
    chap = item["chapter"]
    verse = item["verse"]
    d = IMAGES_DIR / f"ch{chap:02d}"
    d.mkdir(exist_ok=True)
    return d / f"ch{chap:02d}_v{verse:03d}.jpg"


def seed_for(item: dict) -> int:
    # Deterministic seed per verse so regenerating gives the same image.
    h = hashlib.sha256(item["id"].encode()).digest()
    return int.from_bytes(h[:4], "big")


def build_url(item: dict) -> str:
    encoded = urllib.parse.quote(item["prompt"], safe="")
    return f"{BASE}{encoded}?{QUERY}&seed={seed_for(item)}"


def fetch(item: dict) -> tuple[str, str]:
    path = path_for(item)
    if path.exists() and path.stat().st_size >= MIN_BYTES:
        return (item["id"], "skipped")

    url = build_url(item)
    last_err = None
    for attempt in range(RETRIES):
        try:
            req = urllib.request.Request(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0 (gita-image-generator)",
                    "Accept": "image/*",
                },
            )
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                data = r.read()
            if len(data) < MIN_BYTES:
                raise RuntimeError(f"response too small ({len(data)} bytes)")
            path.write_bytes(data)
            return (item["id"], f"ok ({len(data):,} bytes)")
        except urllib.error.HTTPError as e:
            last_err = e
            # 429 = rate-limited. Back off exponentially.
            if e.code == 429:
                time.sleep(10 * (attempt + 1))
            elif attempt < RETRIES - 1:
                time.sleep(5 * (attempt + 1))
        except Exception as e:
            last_err = e
            if attempt < RETRIES - 1:
                time.sleep(5 * (attempt + 1))
    return (item["id"], f"FAIL: {last_err}")


def main() -> None:
    prompts = json.loads((ROOT / "bhagavad_gita_prompts_flat.json").read_text())
    total = len(prompts)
    print(f"Generating {total} images → {IMAGES_DIR}")
    t0 = time.time()

    done = 0
    ok = 0
    failed: list[str] = []
    last_request = 0.0

    # Serial loop, throttled — Pollinations' free tier can't handle parallelism.
    for item in prompts:
        # Throttle to REQUEST_INTERVAL seconds between requests (only when
        # we'd actually hit the network — skipped files don't count).
        path = path_for(item)
        if not (path.exists() and path.stat().st_size >= MIN_BYTES):
            wait = REQUEST_INTERVAL - (time.time() - last_request)
            if wait > 0:
                time.sleep(wait)
            last_request = time.time()

        id_, status = fetch(item)
        done += 1
        if status.startswith("FAIL"):
            failed.append(f"{id_}: {status}")
        else:
            ok += 1
        elapsed = time.time() - t0
        rate = done / elapsed if elapsed > 0 else 0
        eta = (total - done) / rate if rate > 0 else 0
        sys.stdout.write(
            f"[{done:3}/{total}] {id_} — {status} "
            f"| {rate:.2f}/s | ETA {eta/60:.1f} min\n"
        )
        sys.stdout.flush()

    print(f"\nDone in {(time.time()-t0)/60:.1f} min. "
          f"ok={ok}, failed={len(failed)}")
    if failed:
        (ROOT / "generate_images.failures.log").write_text("\n".join(failed))
        print(f"Failures logged to generate_images.failures.log")


if __name__ == "__main__":
    main()
