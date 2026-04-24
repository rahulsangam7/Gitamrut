"""
Nine mood categories for the Bhagavad Gita reels, plus the mapping from
each reel to its mood. Collapsed from an earlier 30-mood design; this
9-mood split is coarse enough that a single BG bed per mood is enough to
score the whole reel series.

Each mood has:
- `name`          short slug used as filename / key
- `description`   the feel we're going for
"""

MOODS = [
    dict(
        name="1_opening_setup",
        description="Dim palace, anxious inquiry, armies gathering at dawn — quiet pre-battle weight",
    ),
    dict(
        name="2_martial_tension",
        description="Conches and drums, rising tension, martial pride — the eve of war",
    ),
    dict(
        name="3_grief_struggle",
        description="Arjuna's collapse, the restless mind, demonic nature — dark emotional struggle",
    ),
    dict(
        name="4_teaching_calm",
        description="The eternal Self, meditation, steady wisdom — still contemplative teaching",
    ),
    dict(
        name="5_heroic_duty",
        description="Kshatriya dharma, act for the world, duty by one's own nature — resolute action",
    ),
    dict(
        name="6_flowing_action",
        description="Karma yoga, fire of wisdom burning karma — action without attachment",
    ),
    dict(
        name="7_divine_warmth",
        description="Bhakti, beloved devotee, tender surrender — warm personal devotion",
    ),
    dict(
        name="8_majesty_glory",
        description="Divine glories, Supreme Person, royal secret — grand transcendent majesty",
    ),
    dict(
        name="9_cosmic_terror",
        description="Cosmic form, Time the destroyer, three gunas — vast dark awe",
    ),
]

assert len(MOODS) == 9, f"Expected 9 moods, got {len(MOODS)}"

# ---------------------------------------------------------------------------
# Reel-to-mood mapping. Rules by (chapter, verse-start-range) — the first
# matching rule wins. Uses the reel's MIDPOINT verse as the anchor so a reel
# that straddles two mood regions picks up the bulk-content mood.
# ---------------------------------------------------------------------------

def in_range(chapter: int, first: int, last: int):
    def pred(reel):
        ids = reel["verses"]
        mid_id = ids[len(ids) // 2]
        v_ch, v_num = [int(x) for x in mid_id.split(".")]
        return v_ch == chapter and first <= v_num <= last
    return pred


RULES = [
    # Ch 1 — setup → martial → despair
    (in_range(1,  1, 11), "1_opening_setup"),
    (in_range(1, 12, 27), "2_martial_tension"),
    (in_range(1, 28, 47), "3_grief_struggle"),

    # Ch 2 — teaching begins → immortality → duty → karma-yoga → sthitaprajna
    (in_range(2,  1, 10), "4_teaching_calm"),
    (in_range(2, 11, 30), "4_teaching_calm"),
    (in_range(2, 31, 38), "5_heroic_duty"),
    (in_range(2, 39, 53), "6_flowing_action"),
    (in_range(2, 54, 72), "4_teaching_calm"),

    # Ch 3 — duty for the world's welfare
    (in_range(3,  1, 43), "5_heroic_duty"),

    # Ch 4 — divine tradition & fire of wisdom
    (in_range(4,  1, 15), "8_majesty_glory"),
    (in_range(4, 16, 33), "4_teaching_calm"),
    (in_range(4, 34, 42), "6_flowing_action"),

    # Ch 5 — inner renunciation
    (in_range(5,  1, 29), "4_teaching_calm"),

    # Ch 6 — meditation + restless mind
    (in_range(6,  1, 32), "4_teaching_calm"),
    (in_range(6, 33, 47), "3_grief_struggle"),

    # Ch 7-8 — divine presence
    (in_range(7,  1, 30), "8_majesty_glory"),
    (in_range(8,  1, 28), "8_majesty_glory"),

    # Ch 9 — royal secret + devotion
    (in_range(9,  1, 22), "8_majesty_glory"),
    (in_range(9, 23, 34), "7_divine_warmth"),

    # Ch 10 — divine glories
    (in_range(10, 1, 42), "8_majesty_glory"),

    # Ch 11 — cosmic form
    (in_range(11, 1, 14), "8_majesty_glory"),
    (in_range(11, 15, 31), "9_cosmic_terror"),
    (in_range(11, 32, 34), "9_cosmic_terror"),
    (in_range(11, 35, 55), "7_divine_warmth"),

    # Ch 12 — bhakti, the beloved devotee
    (in_range(12, 1, 20),  "7_divine_warmth"),

    # Ch 13-17 — field/knower, gunas, Purushottama, divine/demonic, faiths
    (in_range(13, 1, 35),  "4_teaching_calm"),
    (in_range(14, 1, 27),  "9_cosmic_terror"),
    (in_range(15, 1, 20),  "8_majesty_glory"),
    (in_range(16, 1, 24),  "3_grief_struggle"),
    (in_range(17, 1, 28),  "4_teaching_calm"),

    # Ch 18 — renunciation → own dharma → surrender → benediction
    (in_range(18,  1, 40), "4_teaching_calm"),
    (in_range(18, 41, 62), "5_heroic_duty"),
    (in_range(18, 63, 66), "7_divine_warmth"),
    (in_range(18, 67, 78), "7_divine_warmth"),
]


def mood_for(reel) -> str:
    for pred, name in RULES:
        if pred(reel):
            return name
    return "4_teaching_calm"   # gentle fallback


if __name__ == "__main__":
    import json
    import pathlib
    from collections import Counter

    reels_path = pathlib.Path(__file__).parent / "bhagavad_gita_reels.json"
    reels = json.loads(reels_path.read_text())["reels"]
    counts = Counter(mood_for(r) for r in reels)

    print(f"{len(MOODS)} moods, {len(reels)} reels.\n")
    print(f"{'Mood':30} {'Reels':>6}")
    print(f"{'-'*30} {'-'*6}")
    for m in MOODS:
        print(f"{m['name']:30} {counts.get(m['name'], 0):>6}")
