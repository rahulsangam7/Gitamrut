"""
Builds bhagavad_gita_tts.json — one entry per verse, ready for Google Gemini
Flash TTS (`gemini-2.5-flash-preview-tts`, or whichever current Gemini TTS
model the caller prefers — structure is model-agnostic).

Each entry carries:
- `text`         the exact words to speak (speaker cue stripped; the voice
                 itself announces the speaker)
- `speaker`      metadata for filing / review
- `voice`        a Gemini prebuilt voice name (Orus / Puck / Charon / Enceladus)
- `instructions` a natural-language style directive tuned to the VERSE context
- `prompt`       `instructions` + blank line + `text`, pre-combined so you can
                 send it directly as the Gemini generateContent request — Gemini
                 has no separate instructions field, tone is steered by
                 prepending style directions to the prompt text

Speaker tracking:
- Verses that start with "X said:" set the current speaker.
- Subsequent verses inherit that speaker until a new cue appears.
- Nested quoted dialogue is left with the narrator's voice (standard
  audiobook pattern).

Tone overrides:
- Base tone per speaker covers the default case.
- `TONE_OVERRIDE[(chapter, verse)]` replaces the base tone for emotionally
  distinctive moments (Arjuna's despair, the cosmic-form terror, the final
  surrender, Sanjaya's triumphant closing benediction, etc.).
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
src = json.loads((ROOT / "bhagavad_gita_english_plain.json").read_text())


# ---------------------------------------------------------------------------
# VOICE CASTING — one Gemini prebuilt voice per speaker.
#
# Picked from the 30 voices documented for `gemini-3.1-flash-tts-preview`.
# Each voice has an official short descriptor (Firm / Upbeat / Excitable / etc.)
# The picks below were chosen to match each character's arc:
#
# - Krishna → `Orus` (Firm): deep, firm, commanding masculine — the best
#   single-word match for "supreme divine being" in Gemini's voice lineup.
# - Arjuna → `Alnilam` (Firm): Arjuna is an elite warrior-prince, so his
#   voice must read as a deep masculine fighter's voice — not an excitable
#   younger-sounding one (`Fenrir`/`Puck` skew too high/reactive). Alnilam's
#   "Firm" descriptor delivers chest-resonant warrior gravitas; the per-verse
#   tone instructions shape the emotional colouring on top.
# - Sanjaya → `Schedar` (Even): Sanjaya is Dhritarashtra's royal suta —
#   advisor, charioteer, and narrator, granted divya-drishti by Vyasa. He
#   is a distinguished MATURE courtier, not an elderly sage; Mahabharata
#   does not depict him as frail or aged. `Schedar`'s "Even" descriptor
#   gives a measured, balanced narrator voice that contrasts cleanly with
#   Krishna's firm divine Orus — distinct without implying old age.
# - Dhritarashtra → `Algenib` (Gravelly): aged, weathered, heavy. Perfect
#   for the blind careworn king. `Enceladus` (Breathy) is a softer
#   alternative.
#
# Other voices worth testing: Puck, Kore, Rasalgethi, Gacrux, Achernar,
# Alnilam, Umbriel.
# ---------------------------------------------------------------------------
SPEAKERS = {
    "Krishna": {
        "voice": "Orus",  # Firm
        "base_tone": (
            "Read this clearly and naturally, at a normal conversational pace. "
            "Calm, confident, warm. Don't emphasize words dramatically; just "
            "deliver the line plainly like a teacher speaking to a student."
        ),
    },
    "Arjuna": {
        "voice": "Alnilam",  # Firm
        "base_tone": (
            "Read this clearly and naturally, at a normal conversational pace. "
            "Plain masculine voice, matter-of-fact. No performance or heightened "
            "emotion — just speak the words straightforwardly."
        ),
    },
    "Sanjaya": {
        "voice": "Schedar",  # Even
        "base_tone": (
            "Read this in an even, straightforward narrator's voice, at a "
            "normal conversational pace. Plainly stated, no dramatic emphasis."
        ),
    },
    "Dhritarashtra": {
        "voice": "Algenib",  # Gravelly
        "base_tone": (
            "Read this plainly and calmly, at a normal pace. A slightly older "
            "voice, but not theatrical — just a king asking a question."
        ),
    },
}


# ---------------------------------------------------------------------------
# AUDIO TAGS — Gemini 3.1 Flash TTS supports bracketed tags like [trembling],
# [excited] etc. embedded in the text. These are VERY powerful — even a
# small tag dramatically changes delivery. Intentionally empty here so
# every verse reads plain. Add back sparingly only if you want a specific
# high-stakes moment to lean dramatic.
# ---------------------------------------------------------------------------
AUDIO_TAG: dict[tuple[int, int], str] = {}


# ---------------------------------------------------------------------------
# TONE OVERRIDES — per-verse context tone. Deliberately kept MINIMAL. Too
# many overrides turn the whole script into a performance; we want the
# default plain-read tone to carry most of the text, and only nudge a
# handful of genuinely pivotal verses gently. Each override still asks for
# "natural pace, no drama" — the goal is mood shading, not performance.
# ---------------------------------------------------------------------------
TONE_OVERRIDE: dict[tuple[int, int], str] = {}

# Arjuna's despair in Ch 1 — slightly softer, natural pace.
for v in range(28, 48):
    TONE_OVERRIDE[(1, v)] = (
        "Read this slightly softer than normal, at natural pace. Plain "
        "honest delivery, no performance."
    )

# Arjuna asks to be taught (Ch 2.4-8) — slightly subdued.
for v in range(4, 9):
    TONE_OVERRIDE[(2, v)] = (
        "Read this slightly more subdued than default, natural pace. "
        "Plain, thinking aloud."
    )

# Krishna's one genuinely weighted line — "I am Time" — a touch firmer.
for v in (32, 33, 34):
    TONE_OVERRIDE[(11, v)] = (
        "Read this a touch firmer than the surrounding text. Steady and "
        "plain, natural pace."
    )

# Final surrender verse — warmer.
TONE_OVERRIDE[(18, 66)] = (
    "Read this warmly at natural pace. Plain delivery."
)


# ---------------------------------------------------------------------------
# Build.
# ---------------------------------------------------------------------------
CUE_RE = re.compile(r"^([A-Z][a-zA-Z]+) said:\s*\n?", re.MULTILINE)


def split_cue(text: str, current_speaker: str | None) -> tuple[str, str]:
    """If the text starts with a speaker cue, return (speaker, rest_of_text).
    Otherwise return (current_speaker, text)."""
    m = CUE_RE.match(text)
    if m:
        speaker = m.group(1)
        # Normalize to canonical key (only Krishna/Arjuna/Sanjaya/Dhritarashtra
        # are explicit speakers in the Gita).
        if speaker in SPEAKERS:
            rest = text[m.end():].lstrip()
            return speaker, rest
    return current_speaker or "Sanjaya", text


def main() -> None:
    entries = []
    current_speaker: str | None = None

    for ch in src["chapters"]:
        cn = ch["chapter_number"]
        for v in ch["verses"]:
            vn = v["verse_number"]
            text = (v.get("translation") or "").strip()
            if not text:
                continue

            speaker, spoken = split_cue(text, current_speaker)
            current_speaker = speaker

            base = SPEAKERS[speaker]
            tone = TONE_OVERRIDE.get((cn, vn), base["base_tone"])

            # Gemini TTS has no separate instructions field — tone is steered
            # by (a) prepending natural-language directions AND (b) optional
            # bracketed audio tags embedded in the spoken text. We build both
            # and pre-combine them into `prompt` so the consumer can send
            # straight through.
            tag = AUDIO_TAG.get((cn, vn), "")
            tagged_text = f"{tag} {spoken}".strip() if tag else spoken
            prompt = f"{tone}\n\n{tagged_text}"

            entries.append({
                "id": f"{cn}.{vn}",
                "chapter": cn,
                "verse": vn,
                "speaker": speaker,
                "voice": base["voice"],
                "instructions": tone,
                "audio_tag": tag or None,
                "text": spoken,
                "prompt": prompt,
            })

    out = {
        "meta": {
            "source": "bhagavad_gita_english_plain.json",
            "tts_provider": "Google Gemini",
            "tts_model": "gemini-3.1-flash-tts-preview",
            "tts_model_fallback": "gemini-2.5-flash-preview-tts",
            "output_audio": {
                "format": "PCM 16-bit signed little-endian",
                "sample_rate_hz": 24000,
                "channels": 1,
                "wrap_to_wav_via": "ffmpeg or wave.open(..., 'wb')",
            },
            "api_usage": {
                "endpoint": "models.generateContent",
                "required_config": {
                    "responseModalities": ["AUDIO"],
                    "speechConfig.voiceConfig.prebuiltVoiceConfig.voiceName":
                        "<see `voice` field on each verse>",
                },
                "how_to_send": (
                    "For each verse, POST the `prompt` field as the text "
                    "content of a user turn. `prompt` is already "
                    "`instructions` + blank line + (optional audio tag) + "
                    "`text`, pre-combined. Gemini has no separate instructions "
                    "parameter — tone is steered inline in the prompt and via "
                    "optional bracketed audio tags (e.g. [trembling], [serious])."
                ),
                "python_example": (
                    "response = client.models.generate_content(\n"
                    "    model='gemini-3.1-flash-tts-preview',\n"
                    "    contents=verse['prompt'],\n"
                    "    config=types.GenerateContentConfig(\n"
                    "        response_modalities=['AUDIO'],\n"
                    "        speech_config=types.SpeechConfig(\n"
                    "            voice_config=types.VoiceConfig(\n"
                    "                prebuilt_voice_config=types."
                    "PrebuiltVoiceConfig(voice_name=verse['voice'])\n"
                    "            )\n"
                    "        ),\n"
                    "    ),\n"
                    ")"
                ),
            },
            "audio_tags_used": sorted(set(AUDIO_TAG.values())),
            "audio_tags_documented": [
                "[amazed]", "[crying]", "[curious]", "[excited]", "[sighs]",
                "[gasp]", "[giggles]", "[laughs]", "[mischievously]",
                "[panicked]", "[sarcastic]", "[serious]", "[shouting]",
                "[tired]", "[trembling]", "[whispers]", "[cough]", "[bored]",
                "[reluctantly]", "[very fast]", "[very slow]",
            ],
            "notes": (
                "Speaker cues like 'Krishna said:' have been stripped from "
                "`text` — the assigned voice already signals the speaker. The "
                "cue is preserved in the `speaker` field."
            ),
            "speakers": {
                name: {"voice": s["voice"], "base_tone": s["base_tone"]}
                for name, s in SPEAKERS.items()
            },
            "total_verses": len(entries),
        },
        "verses": entries,
    }

    (ROOT / "bhagavad_gita_tts.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2)
    )

    # Summary
    from collections import Counter
    speaker_counts = Counter(e["speaker"] for e in entries)
    print(f"Wrote {len(entries)} TTS entries → bhagavad_gita_tts.json")
    print()
    print("Speaker distribution:")
    for sp, n in speaker_counts.most_common():
        print(f"  {sp:15} {n:4} verses   → voice={SPEAKERS[sp]['voice']}")
    print()
    print(f"Verses with context-specific tone overrides: {len(TONE_OVERRIDE)}")


if __name__ == "__main__":
    main()
