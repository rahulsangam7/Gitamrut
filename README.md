# Bhagavad Gita — Multimodal Pipeline

An end-to-end pipeline that takes the 701 verses of the Bhagavad Gita and
produces:

- Clean Sanskrit + English JSON data
- Image-generation prompts per verse (for Nano Banana / Flux / SDXL)
- TTS scripts with per-character voice casting (for Gemini TTS)
- Reel-sized audio scripts (~60–120s) grouped into **108 reels**, a sacred number
- A Next.js storybook web app for reading verse-by-verse

## Text data

| File | Contents |
|---|---|
| `bhagavad_gita_sanskrit.json` | Devanagari source (public domain, from the `gita/gita` GitHub repo) |
| `bhagavad_gita_english.json` | Scholarly English translation (mine, verse-by-verse) |
| `bhagavad_gita_english_plain.json` | Plain-modern English translation (mine) |

## Image-gen prompts

| File | Contents |
|---|---|
| `bhagavad_gita_prompts.json` | 701 image prompts, nested by chapter |
| `bhagavad_gita_prompts_flat.json` | Same 701, flat array |
| `bhagavad_gita_prompts.csv` | Same 701, spreadsheet-friendly |
| `build_prompts.py` | Source — character sheets (Krishna, Arjuna, Sanjaya, Bhishma, Drona, Duryodhana, Karna, Bhima, Yudhishthira, Dhritarashtra, Vishwarupa), Neo-Ancient art style, per-verse scene data, Kurukshetra battlefield context (18 akshauhinis / ~3.94M combatants) |
| `generate_images.py` | Batch downloader (uses Pollinations.ai free tier) |

## TTS

| File | Contents |
|---|---|
| `bhagavad_gita_tts.json` | 701 verse entries with speaker + voice + tone instructions for `gemini-3.1-flash-tts-preview` |
| `build_tts.py` | Source |
| `bhagavad_gita_reels.json` | 108 reel groupings (60–120s chunks with natural-break endings) |
| `build_reels.py` | Reel grouping with auto-tune to land on exactly 108 |
| `generate_reel.py` | Per-reel audio generator with silence-trim + multi-segment stitching |
| `mix_reel.py` | Voice + mood-matched BG music mixer (sidechain ducking) |
| `moods.py` | 9-mood taxonomy + reel-to-mood mapping |
| `make_mood_beds.py` | Downloads 9 distinct public-domain Indian instrument recordings from archive.org (santoor / sarod / sarangi / bansuri × 2 / sitar × 2 / veena / dilruba) and clips each to a 90-second bed |
| `batch_random_reels.py` | Picks N reels per mood at random, generates + mixes |

## Web app

`gita-app/` — Next.js 14 + TypeScript + Tailwind. Storybook-style UI for
reading verse-by-verse, with language toggle (English ↔ Sanskrit),
keyboard navigation, and a deterministic placeholder image per verse
(swap point for Nano Banana generated art).

## Voice casting (Gemini TTS)

| Speaker | Voice | Notes |
|---|---|---|
| Krishna | Orus (Firm) | Deep, confident, divine |
| Arjuna | Alnilam (Firm) | Warrior-prince in his prime |
| Sanjaya | Schedar (Even) | Mature royal minister (not elderly) |
| Dhritarashtra | Algenib (Gravelly) | Aged blind king (his only verse: 1.1) |

## Mood taxonomy (9 beds)

| # | Mood | Instrument |
|---|---|---|
| 1 | opening_setup | Santoor (Shiv Kumar Sharma) |
| 2 | martial_tension | Sarod (Ali Akbar Khan) |
| 3 | grief_struggle | Sarangi |
| 4 | teaching_calm | Bansuri (Rupak Kulkarni) |
| 5 | heroic_duty | Sitar (Ravi Shankar) |
| 6 | flowing_action | Bansuri (Hariprasad Chaurasia) |
| 7 | divine_warmth | Veena (Raja Rao, 1930s) |
| 8 | majesty_glory | Sitar (Abdul Halim Jaffar Khan, Arabhi raga) |
| 9 | cosmic_terror | Dilruba (Baluji Shrivastav) |

All 9 BG tracks are **Public Domain Mark 1.0** from archive.org — legitimately
free to use.

## Regenerate the audio

```bash
# 1. 9 mood beds (downloads ~400 MB of source MP3s once, clips to 90s WAVs)
python3 make_mood_beds.py

# 2. Per-reel TTS voice (needs Gemini API key)
export GEMINI_API_KEY=your_key_here
python3 generate_reel.py reel_001

# 3. Mix voice + mood bed
python3 mix_reel.py reel_001

# Or batch N-per-mood:
python3 batch_random_reels.py --per-mood 2   # 18 reels
```

## Credits

- Sanskrit source: [`gita/gita`](https://github.com/gita/gita) (Unlicense / public domain)
- English translations: written verse-by-verse by Claude Opus 4.7 from the
  Sanskrit, not adapted from any existing English translation
- Background music: 9 public-domain Indian classical recordings via
  [archive.org](https://archive.org) (CC0 / Public Domain Mark 1.0)
- TTS: Google Gemini 3.1 Flash TTS Preview
