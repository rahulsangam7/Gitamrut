"""
Generate audio for a single reel from bhagavad_gita_reels.json using
Google Gemini TTS.

For each segment in the reel, makes one generateContent call with the
segment's voice. Concatenates raw PCM across segments, then wraps the
final buffer into a single WAV file.

Usage:
    GEMINI_API_KEY=xxxx python3 generate_reel.py reel_001
    GEMINI_API_KEY=xxxx python3 generate_reel.py reel_001 --model gemini-2.5-flash-preview-tts

Output:
    reel_audio/reel_001.wav
"""
import argparse
import base64
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request
import wave

import numpy as np

ROOT = pathlib.Path(__file__).parent
OUT_DIR = ROOT / "reel_audio"
OUT_DIR.mkdir(exist_ok=True)

# Gemini TTS audio format (per docs).
SAMPLE_RATE_HZ = 24_000
SAMPLE_WIDTH_BYTES = 2       # 16-bit
CHANNELS = 1


def synthesize(prompt: str, voice: str, model: str, api_key: str,
               max_retries: int = 5) -> bytes:
    """Call Gemini generateContent in AUDIO mode, return raw PCM bytes.
    Retries on 429 (rate limit) and 5xx with exponential backoff."""
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent?key={api_key}"
    )
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {
                "voiceConfig": {
                    "prebuiltVoiceConfig": {"voiceName": voice}
                }
            },
        },
    }
    data = json.dumps(body).encode("utf-8")

    for attempt in range(max_retries):
        req = urllib.request.Request(
            url, data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                payload = json.loads(r.read())
            break
        except urllib.error.HTTPError as e:
            # 429 = rate limit, 5xx = transient; back off and retry.
            if e.code == 429 or 500 <= e.code < 600:
                wait = 30 * (2 ** attempt)  # 30, 60, 120, 240, 480s
                sys.stderr.write(
                    f"  ⚠ HTTP {e.code}; retrying in {wait}s "
                    f"(attempt {attempt+1}/{max_retries})\n"
                )
                time.sleep(wait)
                continue
            sys.stderr.write(f"HTTP {e.code}: {e.read().decode()[:300]}\n")
            raise
    else:
        raise RuntimeError(f"Gemini retried {max_retries} times, still failing.")

    # Extract the audio inlineData part from the response.
    for candidate in payload.get("candidates", []):
        for part in candidate.get("content", {}).get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                return base64.b64decode(inline["data"])
    raise RuntimeError(f"No audio in response: {json.dumps(payload)[:400]}")


def write_wav(path: pathlib.Path, pcm_bytes: bytes) -> None:
    with wave.open(str(path), "wb") as w:
        w.setnchannels(CHANNELS)
        w.setsampwidth(SAMPLE_WIDTH_BYTES)
        w.setframerate(SAMPLE_RATE_HZ)
        w.writeframes(pcm_bytes)


def trim_silence(pcm: bytes, threshold: int = 400, keep_ms: int = 40) -> bytes:
    """Trim near-silence from the start and end of a mono 16-bit PCM buffer.
    `threshold` is the absolute amplitude below which a sample counts as
    silence (out of 32767). `keep_ms` of near-silence is left at each end
    so consonants don't get clipped."""
    arr = np.frombuffer(pcm, dtype=np.int16)
    if arr.size == 0:
        return pcm
    loud = np.abs(arr) > threshold
    if not loud.any():
        return pcm
    first = int(np.argmax(loud))
    last = int(arr.size - np.argmax(loud[::-1]))
    pad = (keep_ms * SAMPLE_RATE_HZ) // 1000
    first = max(0, first - pad)
    last = min(arr.size, last + pad)
    return arr[first:last].tobytes()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("reel_id", help="e.g. reel_001")
    ap.add_argument("--model", default="gemini-3.1-flash-tts-preview")
    args = ap.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("Set GEMINI_API_KEY in your environment.")

    reels = json.loads((ROOT / "bhagavad_gita_reels.json").read_text())["reels"]
    reel = next((r for r in reels if r["id"] == args.reel_id), None)
    if not reel:
        sys.exit(f"Reel not found: {args.reel_id}")

    print(f"Reel {reel['id']}: {reel['verse_range']} "
          f"({reel['word_count']} words ≈ {reel['estimated_duration_seconds']}s, "
          f"{len(reel['segments'])} segment(s))")

    all_pcm = bytearray()
    for i, seg in enumerate(reel["segments"], start=1):
        print(f"  [{i}/{len(reel['segments'])}] {seg['speaker']} → {seg['voice']} "
              f"({len(seg['text'].split())} words)")
        pcm = synthesize(seg["prompt"], seg["voice"], args.model, api_key)
        # Trim near-silence from both ends of each segment — Gemini TTS
        # tends to pad with 500–800ms of silence before and after the
        # speech, which makes stitched reels feel sluggish.
        pcm = trim_silence(pcm)
        all_pcm.extend(pcm)
        # Short 80ms gap between speaker turns — enough to feel like a
        # breath, not enough to feel like a pause.
        if i < len(reel["segments"]):
            silence_samples = (80 * SAMPLE_RATE_HZ) // 1000
            all_pcm.extend(b"\x00\x00" * silence_samples)

    out_path = OUT_DIR / f"{reel['id']}.wav"
    write_wav(out_path, bytes(all_pcm))
    seconds = len(all_pcm) / (SAMPLE_RATE_HZ * SAMPLE_WIDTH_BYTES * CHANNELS)
    print(f"\nWrote {out_path}  ({seconds:.1f}s, {len(all_pcm):,} bytes PCM)")


if __name__ == "__main__":
    main()
