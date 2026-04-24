"""
Picks 18 reels at random from the 108 — distributed so all 9 moods appear
twice — generates the TTS voice track for each (if not already cached) and
mixes each with its mood-appropriate background bed.

Usage:
    GEMINI_API_KEY=... python3 batch_random_reels.py
    GEMINI_API_KEY=... python3 batch_random_reels.py --per-mood 3   # 27 reels
    GEMINI_API_KEY=... python3 batch_random_reels.py --seed 42

Output:
    reel_audio/<reel_id>.wav         (voice only, 24kHz mono PCM wav)
    reel_audio_mixed/<reel_id>.wav   (voice + mood bed, mixed)
"""
import argparse
import json
import os
import pathlib
import random
import subprocess
import sys

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT))
import moods  # noqa: E402

REELS_PATH = ROOT / "bhagavad_gita_reels.json"
VOICE_DIR = ROOT / "reel_audio"
MIXED_DIR = ROOT / "reel_audio_mixed"


def pick_reels(per_mood: int, seed: int) -> list[dict]:
    """Pick `per_mood` random reels for each of the 9 moods. If a mood has
    fewer reels than requested, take all of them."""
    rng = random.Random(seed)
    reels = json.loads(REELS_PATH.read_text())["reels"]
    by_mood: dict[str, list[dict]] = {m["name"]: [] for m in moods.MOODS}
    for r in reels:
        by_mood[moods.mood_for(r)].append(r)

    picked: list[dict] = []
    for m in moods.MOODS:
        pool = by_mood[m["name"]]
        n = min(per_mood, len(pool))
        picked.extend(rng.sample(pool, n))
    rng.shuffle(picked)
    return picked


def run(cmd: list[str], env: dict | None = None) -> int:
    proc = subprocess.run(cmd, env=env)
    return proc.returncode


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-mood", type=int, default=2,
                    help="How many random reels per mood (default 2 → 18 total)")
    ap.add_argument("--seed", type=int, default=108,
                    help="RNG seed for reproducible picks")
    args = ap.parse_args()

    if not os.environ.get("GEMINI_API_KEY"):
        sys.exit("Set GEMINI_API_KEY in your environment before running.")

    picked = pick_reels(args.per_mood, args.seed)
    print(f"Picked {len(picked)} reels (~{args.per_mood} per mood):\n")
    for r in picked:
        mood = moods.mood_for(r)
        print(f"  {r['id']}  verses {r['verse_range']:>12}  "
              f"({r['estimated_duration_seconds']:>5.1f}s)  mood={mood}")
    print()

    for i, r in enumerate(picked, start=1):
        rid = r["id"]
        voice_path = VOICE_DIR / f"{rid}.wav"
        if voice_path.exists():
            print(f"[{i}/{len(picked)}] {rid}  voice cached, skipping TTS")
        else:
            print(f"[{i}/{len(picked)}] {rid}  generating voice …")
            rc = run([sys.executable, str(ROOT / "generate_reel.py"), rid])
            if rc != 0:
                print(f"  ⚠ TTS failed for {rid}, skipping mix")
                continue
        print(f"         → mixing with mood bed …")
        run([sys.executable, str(ROOT / "mix_reel.py"), rid])

    print(f"\nOutputs:")
    print(f"  Voice only: {VOICE_DIR}")
    print(f"  Mixed:      {MIXED_DIR}")


if __name__ == "__main__":
    main()
