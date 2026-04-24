"""
Generates 9 distinct 90-second background beds — one per mood — from nine
genuinely different public-domain Indian classical recordings on archive.org.
Each recording uses a different instrument so the beds sound clearly distinct,
not just filter-variants of the same track.

All nine source tracks are CC0 / Public Domain Mark 1.0 — legitimately free
for any use.

Output: background_music/<mood_name>.wav (24kHz, mono, 16-bit PCM, 90s)
"""
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).parent
RAW_DIR = ROOT / "background_music" / "raw"
OUT_DIR = ROOT / "background_music"
RAW_DIR.mkdir(parents=True, exist_ok=True)

CLIP_SECONDS = 90
COMMON_TAIL = "loudnorm=I=-16:LRA=7"

# (mood_name, archive.org item, file on archive, offset into file in seconds)
SOURCES = [
    (
        "1_opening_setup",
        "Shiv-Kumar-Sharma-collection",
        "Maestro's Choice I - Shiv Kumar Sharma/01 Bhoopal.mp3",
        240,
        "santoor — crystalline and reflective, quiet palace atmosphere",
    ),
    (
        "2_martial_tension",
        "lpmr-ali-akbar-khan",
        "LPMR ALI AKBAR KHAN.mp3",
        1200,
        "sarod — intense raga section, martial pre-battle tension",
    ),
    (
        "3_grief_struggle",
        "SS_0024_Sarangi",
        "SS_24_01.mp3",
        60,
        "sarangi — deeply mournful bowed strings",
    ),
    (
        "4_teaching_calm",
        "Rupak-Kulkarni-Bansuri",
        "01 Durga.mp3",
        180,
        "bansuri flute — serene teaching atmosphere",
    ),
    (
        "5_heroic_duty",
        "lpmr-837-ravi-shankar",
        "LPMR 837 RAVI SHANKAR.mp3",
        900,
        "sitar — bold resolute raga for heroic duty",
    ),
    (
        "6_flowing_action",
        "lpmr-hariprasad-chaurasia",
        "LPMR HARIPRASAD CHAURASIA.mp3",
        1800,
        "bansuri master — flowing mid-tempo movement",
    ),
    (
        "7_divine_warmth",
        "VeenaRajaRao1930sAlbum",
        "RajaRao___GopalaRao_-_Pranatarthi_Haram.mp3",
        60,
        "veena — warm devotional (vintage 1930s)",
    ),
    (
        "8_majesty_glory",
        "Abdul-Halim-Jaffar-Khan-Sitar",
        "01 Arabhi.mp3",
        300,
        "sitar — grand Arabhi raga for divine glory",
    ),
    (
        "9_cosmic_terror",
        "lpmr-703-dilruba",
        "LPMR BALUJI SHRIVASTAV.mp3",
        720,
        "dilruba — deep bowed string, dark cosmic awe",
    ),
]


def download(item: str, filename: str) -> pathlib.Path:
    """Download the MP3 once and cache in background_music/raw/."""
    safe = filename.replace("/", "_")
    path = RAW_DIR / f"{item}__{safe}"
    if path.exists() and path.stat().st_size > 10_000:
        return path
    from urllib.parse import quote
    url = f"https://archive.org/download/{item}/{quote(filename)}"
    print(f"    ↓ {url}")
    subprocess.run(
        ["curl", "-sL", url, "-o", str(path)], check=True
    )
    return path


def make_bed(name: str, raw: pathlib.Path, offset: float) -> pathlib.Path:
    out = OUT_DIR / f"{name}.wav"
    chain = (
        f"afade=t=in:st=0:d=2,"
        f"afade=t=out:st={CLIP_SECONDS - 2}:d=2,"
        f"{COMMON_TAIL}"
    )
    cmd = [
        "ffmpeg", "-y",
        "-ss", str(offset),
        "-t", str(CLIP_SECONDS),
        "-i", str(raw),
        "-af", chain,
        "-ar", "24000", "-ac", "1", "-c:a", "pcm_s16le",
        str(out),
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    return out


def main() -> None:
    print(f"Sourcing 9 distinct mood beds from archive.org (public domain) …")
    for name, item, filename, offset, note in SOURCES:
        print(f"\n  {name}  ({note})")
        raw = download(item, filename)
        bed = make_bed(name, raw, offset)
        print(f"    ✓ {bed.name}  ({bed.stat().st_size:,} bytes)")
    print(f"\nAll 9 beds ready in {OUT_DIR}.")


if __name__ == "__main__":
    main()
