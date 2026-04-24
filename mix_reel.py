"""
Mix a reel's voice WAV with a mood-appropriate background-music bed, ducking
the music so the voice stays clear.

By default the BG bed is chosen by looking up the reel's mood in moods.py
and loading background_music/<mood_name>.wav. You can override with --bg.

Usage:
    python3 mix_reel.py reel_001                       # auto mood bed
    python3 mix_reel.py reel_001 --bg some/track.wav   # explicit bed
"""
import argparse
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).parent
BG_DIR = ROOT / "background_music"
DEFAULT_OUT_DIR = ROOT / "reel_audio_mixed"
REELS_PATH = ROOT / "bhagavad_gita_reels.json"


def bg_for_reel(reel_id: str) -> pathlib.Path:
    """Look up the mood for this reel and return its BG bed path."""
    # Local import so `--bg` overrides work even if moods.py has issues.
    import moods

    reels = json.loads(REELS_PATH.read_text())["reels"]
    reel = next((r for r in reels if r["id"] == reel_id), None)
    if reel is None:
        raise SystemExit(f"Reel not found: {reel_id}")

    mood = moods.mood_for(reel)
    path = BG_DIR / f"{mood}.wav"
    if not path.exists():
        raise SystemExit(
            f"Mood bed not found: {path}\n"
            f"  → run `python3 make_mood_beds.py` to generate all 9 beds."
        )
    return path


def mix(voice_path: pathlib.Path, bg_path: pathlib.Path, out_path: pathlib.Path,
        music_gain_db: float = -18.0, duck_db: float = -6.0) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Filtergraph:
    # 1. Loop the music indefinitely and cut it to the base music level.
    # 2. Side-chain compressor keyed off the voice — music dips under speech
    #    (ratio 4, fast attack, slower release for smooth ducking).
    # 3. Fade the music in at the start and out at the end.
    # 4. Mix voice + ducked music, voice driving the total duration.
    filtergraph = (
        f"[1:a]aloop=loop=-1:size=2e+9,volume={music_gain_db}dB[bg_base];"
        f"[0:a]asplit=2[voice][voice_key];"
        f"[bg_base][voice_key]sidechaincompress="
        f"threshold=0.05:ratio=4:attack=20:release=350:makeup=1[bg_ducked];"
        f"[bg_ducked]volume={duck_db}dB,afade=t=in:st=0:d=1.5[bg_final];"
        f"[voice][bg_final]amix=inputs=2:duration=first:normalize=0[out]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-i", str(voice_path),
        "-i", str(bg_path),
        "-filter_complex", filtergraph,
        "-map", "[out]",
        "-ar", "24000", "-ac", "1", "-c:a", "pcm_s16le",
        str(out_path),
    ]
    proc = subprocess.run(cmd, capture_output=True)
    if proc.returncode != 0:
        sys.stderr.write(proc.stderr.decode() + "\n")
        raise SystemExit(proc.returncode)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("reel_id")
    ap.add_argument("--bg", default=None,
                    help="Explicit bed path. If omitted, use the mood bed "
                         "chosen by moods.mood_for().")
    ap.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    ap.add_argument("--music-gain-db", type=float, default=-18.0,
                    help="Base music gain (default -18 dB — audible but under voice)")
    ap.add_argument("--duck-db", type=float, default=-6.0,
                    help="Extra duck under active speech (default -6 dB)")
    args = ap.parse_args()

    voice = ROOT / "reel_audio" / f"{args.reel_id}.wav"
    bg = pathlib.Path(args.bg) if args.bg else bg_for_reel(args.reel_id)
    out = pathlib.Path(args.out_dir) / f"{args.reel_id}.wav"
    if not voice.exists():
        sys.exit(f"Voice file not found: {voice}")
    if not bg.exists():
        sys.exit(f"Background file not found: {bg}")

    mix(voice, bg, out, args.music_gain_db, args.duck_db)
    print(f"Mixed → {out}   [bed: {bg.name}]")


if __name__ == "__main__":
    main()
