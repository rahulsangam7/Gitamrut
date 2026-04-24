"""
Groups the 701 verses into reel-sized chunks (~30-40s of spoken audio) so
each reel is short enough to post to Instagram/YouTube Shorts/TikTok without
scrolling fatigue.

How reels are grouped:
- Greedy fill: keep adding verses until a reel reaches a word-count sweet spot.
- Hard rule: never cross a chapter boundary.
- Preference: end a reel at a natural speaker transition or thought break when
  the running word count is already in-range. Avoid cutting mid-teaching.

Each reel carries one or more SEGMENTS. A segment is a single-speaker block
you hand to Gemini TTS. A reel with only one speaker = one segment; a reel
where speakers change mid-way = multiple segments. The consumer either:
  (a) generates each segment separately and concatenates the PCM output, or
  (b) uses Gemini's multi-speaker TTS mode (up to 2 speakers per call).

Pacing model:
- Gemini Flash TTS with our tone instructions delivers roughly 2.3 words/sec
  (slightly slower than natural speech, because the instructions ask for
  weighted, unhurried delivery). So 30-40 seconds ≈ 70-92 words.
- Target window:   70–95 words  (ideal 80)
- Hard max:       115 words      (anything more = scroll-too-long for reels)
- Hard min:        45 words      (anything less = reel too short to matter)
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).parent

# Pull the per-verse TTS data (has speaker, voice, instructions, text already).
tts = json.loads((ROOT / "bhagavad_gita_tts.json").read_text())
verses = tts["verses"]
speakers_meta = tts["meta"]["speakers"]

# Pacing targets (words).
# Natural conversational delivery ≈ 2.0 words/sec in Gemini TTS.
WORDS_PER_SECOND = 2.0
DESIRED_REEL_COUNT = 108

# Starting defaults; overwritten by the auto-tune pass below.
TARGET_MIN = 90
TARGET_MAX = 150
HARD_MAX   = 180


def count_words(text: str) -> int:
    return len(re.findall(r"\S+", text))


# Words that, when a verse STARTS with them, signal a new thought is beginning.
# The previous verse is therefore a natural topical stopping point.
NEW_THOUGHT_STARTS = (
    "Therefore", "Thus", "So", "Now", "Again", "Then", "But", "And now",
    "Hence", "Hear", "Listen", "Know", "Behold", "I will", "I shall",
    "Let", "Consider", "O ", "Arjuna,", "Krishna,",
)


def starts_a_new_thought(text: str) -> bool:
    head = text.lstrip().split("\n", 1)[0].lstrip()
    return any(head.startswith(w) for w in NEW_THOUGHT_STARTS)


def build_reels(target_min: int = None, target_max: int = None, hard_max: int = None) -> list[dict]:
    tmin = target_min if target_min is not None else TARGET_MIN
    tmax = target_max if target_max is not None else TARGET_MAX
    hmax = hard_max   if hard_max   is not None else HARD_MAX

    reels: list[dict] = []
    buf: list[dict] = []       # verses accumulating into the current reel
    buf_words = 0

    def flush() -> None:
        nonlocal buf, buf_words
        if not buf:
            return
        reels.append(assemble_reel(buf))
        buf = []
        buf_words = 0

    prev_chapter = None
    for v in verses:
        vw = count_words(v["text"])

        # Decide whether to flush BEFORE adding this verse.
        # The idea: a reel should end at a point where the thought has
        # completed. That happens at:
        #   (a) chapter boundaries,
        #   (b) speaker changes (the current turn has ended — a new speaker
        #       begins), which is by far the strongest "good context" cue,
        #   (c) hard word-count ceilings when (a) and (b) aren't nearby.
        if buf:
            prev = buf[-1]
            chapter_break = v["chapter"] != prev_chapter
            speaker_break = v["speaker"] != prev["speaker"]
            new_thought = starts_a_new_thought(v["text"])
            would_overflow = buf_words + vw > hmax
            past_min = buf_words >= tmin

            if chapter_break:
                # Always close at chapter boundaries.
                flush()
            elif would_overflow:
                # Hard ceiling — close even if the break isn't graceful.
                flush()
            elif past_min and speaker_break:
                # In range AND a new turn is starting. Strongest natural break.
                flush()
            elif past_min and new_thought:
                # In range AND the next verse starts a new line of thought
                # (Therefore, Thus, Now, Hear, Listen, Know, O Arjuna, ...).
                # Weaker signal than a speaker change but usually still a
                # clean paragraph-like boundary in the Gita.
                flush()

        buf.append(v)
        buf_words += vw
        prev_chapter = v["chapter"]

    flush()
    return reels


def assemble_reel(vbuf: list[dict]) -> dict:
    """Collapse consecutive same-speaker verses into segments."""
    segments: list[dict] = []
    current: dict | None = None

    for v in vbuf:
        if current and current["speaker"] == v["speaker"]:
            current["verses"].append(v["id"])
            current["text"] = (current["text"] + "\n\n" + v["text"]).strip()
        else:
            if current:
                segments.append(current)
            current = {
                "speaker": v["speaker"],
                "voice": v["voice"],
                "instructions": v["instructions"],
                "text": v["text"],
                "verses": [v["id"]],
            }
    if current:
        segments.append(current)

    # Pre-combine per-segment prompt (instructions + blank line + text) so
    # the caller can feed it straight to Gemini generateContent.
    for s in segments:
        s["prompt"] = f"{s['instructions']}\n\n{s['text']}"

    total_words = sum(count_words(s["text"]) for s in segments)
    chapters = sorted({int(vid.split(".")[0]) for s in segments for vid in s["verses"]})
    verse_range = f"{vbuf[0]['id']}-{vbuf[-1]['id']}" if len(vbuf) > 1 else vbuf[0]["id"]

    return {
        "chapter": chapters[0] if len(chapters) == 1 else chapters,
        "verse_range": verse_range,
        "verses": [v["id"] for v in vbuf],
        "word_count": total_words,
        "estimated_duration_seconds": round(total_words / WORDS_PER_SECOND, 1),
        "speakers": sorted({s["speaker"] for s in segments}),
        "segments": segments,
    }


def auto_tune_for_count(target_count: int) -> tuple[int, int, int, list[dict]]:
    """Sweep (target_max, hard_max) to find a setting that yields exactly the
    target reel count. Prefer graceful-ending ratio as the tiebreaker among
    settings that all hit target_count."""
    best = None
    # Grid: target_max ∈ [90..220], hard_max = target_max + 25..40.
    # target_min held at 0.6 * target_max so small reels still happen at
    # chapter/speaker boundaries.
    for tmax in range(90, 225):
        for slack in (25, 30, 35, 40):
            hmax = tmax + slack
            tmin = int(tmax * 0.6)
            reels = build_reels(tmin, tmax, hmax)
            if len(reels) != target_count:
                continue
            # Score this setting by ending quality — fewer forced hard-max
            # flushes is better.
            forced = 0
            for i, r in enumerate(reels[:-1]):
                last = next(x for x in verses if x["id"] == r["verses"][-1])
                nxt = next(x for x in verses if x["id"] == reels[i + 1]["verses"][0])
                if (
                    last["chapter"] == nxt["chapter"]
                    and last["speaker"] == nxt["speaker"]
                    and not starts_a_new_thought(nxt["text"])
                ):
                    forced += 1
            score = -forced  # higher is better
            if best is None or score > best[0]:
                best = (score, tmin, tmax, hmax, reels)
    if best is None:
        raise RuntimeError(f"No settings produced exactly {target_count} reels")
    _, tmin, tmax, hmax, reels = best
    return tmin, tmax, hmax, reels


def main() -> None:
    tmin, tmax, hmax, reels = auto_tune_for_count(DESIRED_REEL_COUNT)
    print(f"Auto-tuned: target_min={tmin}, target_max={tmax}, hard_max={hmax} → {len(reels)} reels")
    print()
    # Store the chosen settings back onto the module globals so the later
    # summary stats (which still read TARGET_MIN etc.) stay consistent.
    globals()["TARGET_MIN"] = tmin
    globals()["TARGET_MAX"] = tmax
    globals()["HARD_MAX"] = hmax

    for i, r in enumerate(reels, start=1):
        r["id"] = f"reel_{i:03d}"

    out = {
        "meta": {
            "source": "bhagavad_gita_tts.json",
            "purpose": "Reel-sized audio scripts (~30-40s) for social media posting.",
            "pacing_model": {
                "words_per_second": WORDS_PER_SECOND,
                "target_word_range": [TARGET_MIN, TARGET_MAX],
                "hard_max_words": HARD_MAX,
            },
            "grouping_rules": (
                "Chapter boundaries always break a reel. Verses greedily fill "
                "up to ~95 words (ideal ~80). Consecutive verses by the same "
                "speaker collapse into a single segment; speaker changes "
                "start a new segment within the same reel."
            ),
            "tts_model": "gemini-3.1-flash-tts-preview",
            "tts_usage": (
                "For each reel, generate each segment separately (one Gemini "
                "call per segment with its own voice), then concatenate the "
                "PCM output client-side. Alternatively, for reels with <=2 "
                "speakers, use Gemini's multi-speaker TTS mode in a single "
                "call."
            ),
            "total_reels": len(reels),
            "total_verses": sum(len(r["verses"]) for r in reels),
        },
        "reels": reels,
    }

    (ROOT / "bhagavad_gita_reels.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2)
    )

    # Summary + distribution.
    import statistics
    durations = [r["estimated_duration_seconds"] for r in reels]
    word_counts = [r["word_count"] for r in reels]
    speaker_counts = [len(r["speakers"]) for r in reels]

    print(f"Wrote {len(reels)} reels → bhagavad_gita_reels.json")
    print(f"Covering {sum(len(r['verses']) for r in reels)} verses")
    print()
    print(f"Word count    — min {min(word_counts)}, median {int(statistics.median(word_counts))}, max {max(word_counts)}")
    print(f"Duration (s)  — min {min(durations):.1f}, median {statistics.median(durations):.1f}, max {max(durations):.1f}")
    print(f"Speakers/reel — 1: {speaker_counts.count(1)}, 2: {speaker_counts.count(2)}, 3+: {sum(1 for c in speaker_counts if c >= 3)}")
    print()
    b_short = sum(1 for d in durations if d < 60)
    b_mid = sum(1 for d in durations if 60 <= d <= 120)
    b_long = sum(1 for d in durations if d > 120)
    print(f"Duration buckets:")
    print(f"  < 60s   : {b_short:3} reels ({100*b_short/len(reels):.1f}%)")
    print(f"  60-120s : {b_mid:3} reels ({100*b_mid/len(reels):.1f}%)")
    print(f"  > 120s  : {b_long:3} reels ({100*b_long/len(reels):.1f}%)")
    # A reel ends "naturally" if the NEXT reel starts at: a chapter boundary,
    # a speaker change, or a "new thought" keyword. Anything else is a
    # hard-max force-flush (still fine, but less graceful).
    verse_by_id = {v["id"]: v for v in verses}
    kinds = {"chapter": 0, "speaker": 0, "new_thought": 0, "forced": 0}
    for i, r in enumerate(reels[:-1]):
        last_id = r["verses"][-1]
        next_id = reels[i + 1]["verses"][0]
        last_v = verse_by_id[last_id]
        next_v = verse_by_id[next_id]
        if last_v["chapter"] != next_v["chapter"]:
            kinds["chapter"] += 1
        elif last_v["speaker"] != next_v["speaker"]:
            kinds["speaker"] += 1
        elif starts_a_new_thought(next_v["text"]):
            kinds["new_thought"] += 1
        else:
            kinds["forced"] += 1
    graceful = kinds["chapter"] + kinds["speaker"] + kinds["new_thought"]
    total_transitions = sum(kinds.values())
    print()
    print(f"Ending quality (of {total_transitions} inter-reel transitions):")
    print(f"  chapter boundary  : {kinds['chapter']:3}")
    print(f"  speaker change    : {kinds['speaker']:3}")
    print(f"  new-thought start : {kinds['new_thought']:3}")
    print(f"  forced (hard max) : {kinds['forced']:3}")
    print(f"  → graceful endings: {graceful}/{total_transitions} "
          f"({100*graceful/total_transitions:.1f}%)")


if __name__ == "__main__":
    main()
