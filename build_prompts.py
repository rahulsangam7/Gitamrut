"""
Builds bhagavad_gita_prompts.json — a unique image-generation prompt for each
of the 701 verses, designed for models like Google's Gemini (Nano Banana) or
Flux/SDXL.

Design:
- CHARACTERS: canonical, identical descriptions every time a figure appears,
  so the same face/outfit recurs across every image they are in.
- STYLE: one art-direction sentence prepended to every prompt so the whole
  series reads as a single illustrated manuscript.
- CONSTRAINTS: hard rules enforced on every prompt — square aspect, no text,
  no letters, no captions.
- SCENES: per-verse dict with location, cast, action, mood. Kept deliberately
  compact; the composer expands it into the full prompt.

Output structure mirrors the translation files so the web app can merge it in
by chapter/verse key.
"""
import csv
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
src = json.loads((ROOT / "bhagavad_gita_sanskrit.json").read_text())

# ---------------------------------------------------------------------------
# ART STYLE — applied to every single prompt. Do not vary per verse.
# ---------------------------------------------------------------------------
STYLE = (
    "A single square 1:1 illustration in a Neo-Ancient style: classical Indian "
    "miniature painting fused with cinematic painterly realism. Warm parchment "
    "and sepia palette with saffron, deep indigo, gold leaf accents, and soft "
    "natural volumetric lighting. Delicate ornamental borders and fine ink "
    "linework evoke an illuminated manuscript. Composition is centered, "
    "balanced, and clear."
)

# ---------------------------------------------------------------------------
# HARD CONSTRAINTS — appended to every prompt. Image-gen models respond better
# to explicit negatives than to polite omission.
# ---------------------------------------------------------------------------
CONSTRAINTS = (
    "Strict: square 1:1 aspect ratio, exactly equal width and height. "
    "Absolutely NO text, NO letters, NO numerals, NO captions, NO writing, "
    "NO calligraphy, NO signs, NO inscriptions anywhere in the image. "
    "No watermarks, no logos, no borders with writing."
)

# ---------------------------------------------------------------------------
# CHARACTER SHEETS — canonical physical descriptions. Include every time a
# character appears so the same figure recurs across the series. Keep each
# description tight but complete (face, hair, clothing, identifying props).
# ---------------------------------------------------------------------------
CHARACTERS = {
    # The supreme being. Must always read as the most powerful, most radiant,
    # most commanding figure in any scene he appears in — stronger than every
    # mortal warrior, taller, more divinely adorned, with a clearly visible
    # aura no other character shares.
    "Krishna": (
        "Lord Krishna, THE supreme divine being and the most powerful figure in "
        "any scene — taller, stronger, and more radiant than every other "
        "character present. A towering, majestically muscular god-king with a "
        "sculpted heroic physique — broad chest, powerful shoulders, a warrior's "
        "chiseled arms and torso, posture upright and utterly self-possessed. "
        "Luminous deep blue skin like a monsoon rain cloud; a serene, "
        "all-knowing face with the gentlest knowing smile and piercing deep "
        "dark eyes full of cosmic wisdom and infinite compassion. Long flowing "
        "dark curly hair crowned with a single peacock feather set in an ornate "
        "jewelled gold crown (mukuta) studded with rubies and emeralds. Rich "
        "yellow silk pitambara dhoti embroidered with intricate gold patterns, "
        "a brilliant yajnopavita sacred thread across his bare chest, the "
        "Kaustubha gem glowing at his throat, heavy gold armlets (keyura) on "
        "powerful biceps, gold bangles at the wrists, ornate kundala earrings, "
        "multiple layered necklaces including a long vaijayanti garland of "
        "fresh forest flowers down to his waist, a golden flute tucked in his "
        "sash. A soft radiant halo of golden divine light around his head and "
        "a faint shimmering aura along his whole body that no other figure "
        "has. The viewer must immediately sense a supreme God"
    ),
    # Elite warrior-prince, left-handed archer (Savyasachi). Athletic rather
    # than massive — built like a champion archer/wrestler.
    "Arjuna": (
        "Arjuna, an elite warrior-prince of the Pandavas — a tall, strikingly "
        "handsome young hero with a lean, powerfully athletic warrior's build, "
        "sculpted broad shoulders and a chiseled chest, bronzed olive skin. "
        "Sharp aquiline features, dark intense thoughtful eyes, a clean-shaven "
        "noble face, long jet-black silken hair tied back in a tight warrior's "
        "topknot with a jewelled clasp. Polished silver mail armor with "
        "exquisite gold filigree and lion-motif shoulder plates worn over a "
        "deep saffron silk undertunic, a crimson sash at the waist, a royal "
        "blue cape. Gold armlets carved with tiger heads, heavy gold vambraces, "
        "a gold torque around the neck, ornate kundala earrings, a jewelled "
        "diadem with a single peacock plume. In his hand the great divine bow "
        "Gandiva, a full quiver of gold-fletched arrows on his back. Bearing "
        "proud, focused, and disciplined — unmistakably the foremost champion "
        "among mortal warriors"
    ),
    # Royal minister-bard with divine sight — a distinguished mature courtier,
    # NOT an elderly sage. In Dwapara Yuga characters keep a youthful vigorous
    # look into great age; Sanjaya is depicted here as a senior statesman in
    # his prime, sharp and composed.
    "Sanjaya": (
        "Sanjaya, Dhritarashtra's royal suta (advisor, charioteer, and bard) "
        "blessed with divya-drishti (divine sight) — a distinguished mature "
        "courtier in his prime, NOT elderly or frail. Tall, lean athletic "
        "build, sharp intelligent clean-shaven or neatly short-bearded face "
        "with dark hair (perhaps a few grey strands at the temples). Eyes "
        "gently closed, as if seeing distant events through inner vision. "
        "Fine saffron-and-cream silk courtier's robes with subtle gold "
        "embroidery, a slim gold-threaded sash, a small gold royal-minister's "
        "medallion on a fine chain, modest gold armlets, a single string of "
        "rudraksha beads, a small tripundra mark of sacred ash on his "
        "forehead. No weapons. Poised, composed, unmistakably a senior "
        "statesman of the Kuru court"
    ),
    # Elder blind king — old, yes, but still a massively imposing patriarch,
    # not a shrunken feeble figure. Dwapara Yuga kings in their 80s+ retain
    # power and bearing; only the blindness and the burden of worry diminish
    # him.
    "Dhritarashtra": (
        "Dhritarashtra, elder blind king of the Kurus — a massively built, "
        "broad-shouldered imposing patriarch-monarch, still powerful in "
        "frame though visibly senior. Long white beard and long white hair "
        "neatly bound, lined dignified face with permanently closed "
        "sightless eyes. A huge jewelled royal turban set with a great "
        "central ruby and tall peacock plumes. Heavy crimson-and-gold "
        "brocade royal robes, a long pearl-and-ruby necklace, thick gold "
        "rings, jewelled armlets carved with lions. Seated on an ornate "
        "lion-carved throne with weight and presence — a king who still "
        "commands a hall, not a frail old man"
    ),
    # Grand-elder warrior. Tallest and broadest of the mortal warriors except
    # Krishna. Ancient, immovable, calm and majestic.
    "Bhishma": (
        "Bhishma the Grandsire of the Kurus — chronologically ancient yet, "
        "per Dwapara Yuga lifespan, still at the full vigor of a great "
        "warrior. Extraordinarily tall, broad-chested, powerfully muscular "
        "like an ageless mountain — no stoop, no frailty. A well-kept "
        "silver-white beard and long silver hair bound with a gold fillet; "
        "a strong lined face with piercing clear noble eyes and a calm "
        "majestic expression. Antique heavy silver-and-gold scale armor over "
        "a deep indigo warrior's tunic, a long midnight-blue cloak clasped "
        "with a carved silver lion, a jewelled sword-belt. Ornate gold "
        "vambraces, heavy armlets set with sapphires, a ceremonial gold "
        "torque, a great spiral conch at his hip. Bow and quiver slung "
        "behind. An elder in years, a warrior still in his full power"
    ),
    # Senior brahmin warrior-teacher — seasoned, NOT feeble. Hair may show
    # silver strands but his body is lean, corded, and ready for battle.
    "Drona": (
        "Drona, the brahmin warrior-teacher — a tall, lean, wiry master "
        "archer at full martial vigor despite his seniority. Hard corded "
        "warrior's physique, sharp intelligent features, piercing eyes, "
        "shaved temples with a scholarly topknot (shikha) bound with red "
        "thread, dark hair showing silver streaks, a neatly trimmed short "
        "salt-and-pepper beard. Ash tripundra marks across the forehead. "
        "White-and-saffron ascetic robes under a light silver chain-mail "
        "chest-piece, a visible yajnopavita sacred thread across his bare "
        "chest, a simple bone-bead necklace, carved bronze armlets, a "
        "single ornate ruby ring. A tall compound bow at his side, a "
        "quiver at his back. Bearing stern, precise, authoritative — a "
        "seasoned warrior-guru, not an old man"
    ),
    # Villain-king. Muscular, arrogant, gaudily adorned — wealth without grace.
    "Duryodhana": (
        "Duryodhana, the eldest Kaurava prince-king and antagonist — a tall, "
        "heavily muscled warrior in his arrogant prime, thick bull neck, "
        "barrel chest, powerful arms. Coarse handsome face with a sharp "
        "goateed beard, slicked-back long dark hair, a cruel ambitious "
        "half-smile, proud haughty eyes. A massive ornate gold crown "
        "encrusted with rubies and black onyx, thick gold collars, layered "
        "jewelled necklaces, heavy gold upper-arm bands carved with serpents, "
        "rings on every finger. Deep crimson and black royal robes under "
        "heavy burnished-gold lamellar armor with eagle-motif shoulder "
        "guards. A huge ornate iron mace inlaid with gold resting against "
        "his shoulder. Bearing proud, domineering, dangerous"
    ),
    # Tragic warrior-hero. Handsome and sun-blessed, fused divine armor and
    # earrings — his signature. Noble solitary bearing.
    "Karna": (
        "Karna, the tragic warrior-hero of the sun — a tall, powerfully built "
        "warrior with sun-bronzed copper-toned skin that seems to glow "
        "faintly, a strong chiseled chest and broad shoulders, a striking "
        "handsome face with a straight strong nose and deep brooding eyes, "
        "shoulder-length wavy dark hair. His distinguishing mark: a luminous "
        "gold divine breastplate (kavacha) fused seamlessly to his chest and "
        "two glowing golden earrings (kundala) fused to his ears — these "
        "gleam with a faint inner light. A deep amber and saffron warrior's "
        "tunic beneath, a crimson sash, a gold sun-emblem medallion, gold "
        "armlets carved with sun rays. A mighty bow Vijaya in hand, an "
        "ornate quiver slung across his back. Bearing noble, solitary, "
        "tinged with dignified sorrow"
    ),
    # Mountain-sized warrior — the physically strongest Pandava. All raw power.
    "Bhima": (
        "Bhima the second Pandava — a true giant among men, mountainously "
        "tall and immensely muscular with the build of a great wrestler: a "
        "colossal chest, tree-trunk arms, a massive bull neck. Thick wild "
        "black beard and long wild dark hair tied back roughly. Intense "
        "fierce dark eyes, a permanent wolfish snarl of confidence. Heavy "
        "black-iron scale armor over a blood-red warrior tunic, a lion-skin "
        "cape thrown across one shoulder. Coarse iron-and-gold armbands, a "
        "single heavy gold torque, a large carved-bone necklace. In his "
        "hand his legendary enormous iron mace (gada), spiked and nearly as "
        "tall as a man. Bearing thunderous, fearsome, primal"
    ),
    # Eldest Pandava, dharma-king. Quietly strong, refined rather than flashy.
    "Yudhishthira": (
        "Yudhishthira, the eldest Pandava and dharma-king — a tall, upright "
        "warrior-sage of a king with a balanced athletic build (strong but "
        "without bulk), calm serene face, a neatly trimmed short dark beard, "
        "contemplative gentle eyes, long dark hair tied back simply. A "
        "modest but finely-crafted gold crown set with a single white pearl, "
        "refined cream-and-gold silken robes under lustrous silver mail "
        "armor, an ivory-and-gold belt, simple gold armlets, a single "
        "sacred-thread line across the chest. A long-handled sword at his "
        "hip but rarely drawn. Bearing tranquil, wise, unwavering"
    ),
    # Cosmic revelation — not a normal character. The entire universe as a body.
    "VishwaRupa": (
        "Vishwarupa, the Universal Cosmic Form of Krishna revealed: a vast "
        "awe-inspiring luminous cosmic being spanning the entire sky, with "
        "countless arms, countless mouths, and countless eyes across an "
        "enormous body of swirling galaxies, nebulae, and stars. The sun and "
        "moon are his eyes, blazing fire his many mouths; each hand wields a "
        "different divine weapon (discus, club, bow, trident, sword, conch, "
        "lotus); thousands of divine ornaments — golden crowns, garlands, "
        "jewelled necklaces — glitter across his limitless form. Gods, "
        "sages, demons, kings, and whole worlds are visible entering and "
        "emerging from his being. The form is simultaneously infinitely "
        "terrifying and overwhelmingly radiant, so vast that horizon and "
        "sky disappear into him"
    ),
}


def cast(*names: str) -> str:
    """Expand character names into their full canonical descriptions."""
    return ". ".join(CHARACTERS[n] for n in names)


# ---------------------------------------------------------------------------
# BATTLEFIELD CONTEXT — inherited by every scene set at the chariot. Per the
# Mahabharata, 18 akshauhinis (about 3.94 million combatants, nearly 394,000
# chariots, 394,000 armored war elephants, 1.18 million cavalry, and 1.97
# million infantry) fought on this plain across 18 catastrophic days. Only
# 11 major warriors survived. Any battlefield scene must read as ENORMOUS.
# ---------------------------------------------------------------------------
KURUKSHETRA = (
    "the vast, dust-swept plain of Kurukshetra — one of the largest battlefields "
    "ever imagined. On either side two colossal opposing armies of nearly four "
    "million combatants in total are drawn up in endless ranks stretching to "
    "the horizon: the Pandava host of 7 akshauhinis on one side, the Kaurava "
    "host of 11 akshauhinis on the other. Tens of thousands of gleaming war "
    "chariots with coloured banners; massive war elephants in painted scale "
    "armor with howdahs bristling with archers; vast squadrons of armored "
    "cavalry in disciplined rows; seas of foot-soldiers with spears, swords, "
    "bows, shields, and maces, helms glinting under a dawn sun. Thousands of "
    "tall regimental standards, pennants, and family banners snap in the wind. "
    "Enormous rolling dust-clouds churn behind each army; conches, war-drums, "
    "tabors and trumpets echo across the plain; the ground trembles underfoot. "
    "The atmosphere is epic, ominous, weighted — the hush of the most "
    "devastating war in legend"
)

CHARIOT = (
    "Arjuna's magnificent royal war-chariot — drawn by four pure-white "
    "stallions, built of carved wood inlaid with gold, the tall flagstaff "
    "bearing the banner of Hanuman flying high above — halted at the very "
    "midpoint of " + KURUKSHETRA
)

# ---------------------------------------------------------------------------
# SCENES — per-verse short scene data. Composed into full prompts at build time.
# ---------------------------------------------------------------------------
# Shape: S[(chapter, verse)] = dict(loc=..., cast=[...], action=..., mood=..., extra="")
S: dict[tuple[int, int], dict] = {}


# ============================================================================
# CHAPTER 1 — Arjuna's Despair (47 verses)
# ============================================================================

S[(1, 1)] = dict(
    loc="a dim opulent Hastinapura palace chamber at dawn",
    cast=["Dhritarashtra", "Sanjaya"],
    action=(
        "the blind king leans forward anxiously from an ornate lion-carved "
        "throne; the sage sits cross-legged nearby in deep inner vision, "
        "eyes closed, one hand raised as if listening"
    ),
    mood="solemn anxious inquiry",
    extra="marble pillars, hanging oil lamps, a distant battlefield glimpsed through an archway",
)
S[(1, 2)] = dict(
    loc=KURUKSHETRA + ", viewed from the Kaurava side at dawn",
    cast=["Duryodhana", "Drona"],
    action=(
        "the ambitious young king strides toward his aged teacher in front of "
        "the immense Kaurava host of 11 akshauhinis, gesturing urgently across "
        "the plain at the Pandava army arrayed on the far side"
    ),
    mood="tense strategizing before apocalyptic war",
    extra="countless banners snapping in the wind, war elephants, chariots, and infantry stretching to the horizon",
)
S[(1, 3)] = dict(
    loc="a slight rise overlooking the Pandava army on Kurukshetra",
    cast=["Duryodhana", "Drona"],
    action=(
        "Duryodhana sweeps his arm across the horizon toward the enemy's "
        "vast formation; Drona follows his gaze with a measured expression"
    ),
    mood="martial appraisal",
    extra="distant figure of a commander (Dhrishtadyumna) arranging troops in a fish-shaped vyuha",
)
S[(1, 4)] = dict(
    loc="the Pandava front lines",
    cast=["Arjuna", "Bhima"],
    action=(
        "Arjuna and Bhima stand flanked by four other mighty archers "
        "(Yuyudhana, Virata, Drupada, and their charioteers), bows raised in readiness"
    ),
    mood="heroic gathering of champions",
    extra="row of war chariots with bright banners, morning light catching on polished armor",
)
S[(1, 5)] = dict(
    loc="among the Pandava ranks",
    cast=[],
    action=(
        "a line of noble warrior-kings in varied royal armor — Dhrishtaketu, "
        "Chekitana, the valiant king of Kashi, Purujit, Kuntibhoja, Shaibya "
        "— stand shoulder to shoulder holding spears, bows, and maces"
    ),
    mood="stately muster of allies",
    extra="each warrior's banner distinct: tiger, elephant, bull, lotus",
)
S[(1, 6)] = dict(
    loc="behind the first rank of the Pandavas",
    cast=[],
    action=(
        "the valiant Yudhamanyu and mighty Uttamaujas, the young son of "
        "Subhadra (Abhimanyu) in light armor, and Draupadi's five sons "
        "gathered together, bows in hand"
    ),
    mood="proud kinship and youth in arms",
    extra="family crest on shared banners",
)
S[(1, 7)] = dict(
    loc="a Kaurava command tent, half-open to the field",
    cast=["Duryodhana", "Drona"],
    action=(
        "Duryodhana leans over a map of the battlefield beside Drona, pointing out "
        "positions of his own commanders, voice low and urgent"
    ),
    mood="tactical intensity",
    extra="scroll maps, oil lamp, weapons stacked against the tent pole",
)
S[(1, 8)] = dict(
    loc="the Kaurava line",
    cast=["Bhishma", "Drona", "Karna"],
    action=(
        "Bhishma, Drona, Karna and an older warrior-teacher Kripa stand in a "
        "row; behind them stand Ashvatthama, Vikarna, and Somadatta's son, "
        "all mighty and armored"
    ),
    mood="formidable assembly",
    extra="rising sun behind them, long shadows on the dust",
)
S[(1, 9)] = dict(
    loc="the massed Kaurava army of 11 akshauhinis on the Kurukshetra plain",
    cast=[],
    action=(
        "endless rows of armored warriors — thousands upon thousands with "
        "swords, bows, spears, maces — chariots and war elephants bristling "
        "between them, the host stretching beyond sight, standing resolute, "
        "ready to die for their king"
    ),
    mood="grim collective resolve of a world-scale host",
    extra="rolling dust, countless banners, chariots, war elephants, and infantry vanishing to the horizon",
)
S[(1, 10)] = dict(
    loc="a sweeping high-angle aerial view of the entire Kurukshetra battlefield",
    cast=["Bhishma", "Bhima"],
    action=(
        "an epic bird's-eye composition showing both armies in full: Bhishma "
        "shining at the head of the enormous Kaurava host of 11 akshauhinis "
        "(about 2.4 million troops) on one side; Bhima at the head of the "
        "smaller but fiercer Pandava host of 7 akshauhinis (about 1.5 million "
        "troops) on the other; each host a geometric sea of chariots, "
        "elephants, cavalry, and infantry arranged in battle formations"
    ),
    mood="staggering comparison of force",
    extra="the rising sun splitting the image between the two hosts, dust-clouds on both flanks",
)
S[(1, 11)] = dict(
    loc="the Kaurava formation at the entrances of its military array",
    cast=["Duryodhana", "Bhishma"],
    action=(
        "Duryodhana strides along the line instructing captains to close "
        "ranks and protect Bhishma, who stands tall at the center"
    ),
    mood="hardening defense",
    extra="warriors closing inward toward Bhishma's position",
)
S[(1, 12)] = dict(
    loc="the Kaurava front, under a dawn sky",
    cast=["Bhishma"],
    action=(
        "the elder grandsire, Bhishma, raises a great white conch to his lips "
        "and blows; his mouth open in a lion's roar expression"
    ),
    mood="thunderous war-cry of an elder",
    extra="shockwaves rippling visually through the air, flags trembling",
)
S[(1, 13)] = dict(
    loc="the immense Kaurava host of 11 akshauhinis on Kurukshetra",
    cast=[],
    action=(
        "a world-shaking cacophony of war: thousands of conches blown in unison, "
        "tens of thousands of kettle-drums struck, tabors, trumpets, war-horns, "
        "and a million soldiers roaring their battle calls; elephants trumpeting, "
        "horses rearing; the sound visibly shaking the air across the vast plain"
    ),
    mood="tumultuous deafening roar of millions",
    extra="sound waves drawn as gold-leaf arcs rippling across the battlefield, dust shaking loose from banners",
)
S[(1, 14)] = dict(
    loc="between the two armies on Kurukshetra",
    cast=["Krishna", "Arjuna"],
    action=(
        "Krishna as charioteer and Arjuna as archer stand in a magnificent "
        "chariot drawn by four white horses; both raise conches high to their "
        "lips"
    ),
    mood="divine answering call",
    extra="the sacred white horses rearing slightly, banner of Hanuman flying above",
)
S[(1, 15)] = dict(
    loc="the Pandava chariot line",
    cast=["Krishna", "Arjuna", "Bhima"],
    action=(
        "Krishna blows the conch Panchajanya, Arjuna blows Devadatta, and a "
        "fierce-looking Bhima blows his great conch Paundra"
    ),
    mood="thunderous counter-declaration",
    extra="three distinctive conches rendered in detail, sound radiating outward",
)
S[(1, 16)] = dict(
    loc="the Pandava rank",
    cast=["Yudhishthira"],
    action=(
        "the calm king Yudhishthira blows a gleaming conch; his twin brothers "
        "Nakula and Sahadeva stand nearby blowing theirs, all three conches differing subtly"
    ),
    mood="stately resolve",
    extra="royal banners of the Pandavas behind them",
)
S[(1, 17)] = dict(
    loc="among the Pandava allies",
    cast=[],
    action=(
        "the king of Kashi with a great bow, Shikhandi in armor, Dhrishtadyumna, "
        "Virata, and Satyaki stand together, each blowing his own war-conch"
    ),
    mood="united war-cry of allies",
    extra="different banners clearly distinct for each",
)
S[(1, 18)] = dict(
    loc="the Pandava line",
    cast=[],
    action=(
        "King Drupada, the five sons of Draupadi, and the young mighty "
        "Abhimanyu — each blowing his own conch in unison"
    ),
    mood="multi-generational war-declaration",
    extra="a father-figure Drupada and youths side by side",
)
S[(1, 19)] = dict(
    loc="looking across the vast Kurukshetra plain toward the immense Kaurava host",
    cast=[],
    action=(
        "a great shockwave of sound rolls across the battlefield from the "
        "Pandava conches; thousands upon thousands of Kaurava warriors visibly "
        "recoil, clutch their chests, stagger back; elephants falter, horses "
        "shy, banners bend in the blast"
    ),
    mood="dread striking millions at once",
    extra="tremor lines through sky and earth, dust rising, a collective wave of recoil across endless ranks",
)
S[(1, 20)] = dict(
    loc="on the great chariot between the two armies",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna raises his bow Gandiva toward the Kaurava host, about to "
        "speak to Krishna the charioteer; the Hanuman banner flies high above"
    ),
    mood="the moment before decision",
    extra="weapons clashing in distant background, monkey-figure banner distinct",
)
S[(1, 21)] = dict(
    loc="in the chariot",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna leans toward Krishna and gestures to a spot between the two "
        "armies, asking him to drive the chariot there"
    ),
    mood="quiet urgent request",
    extra="the two of them alone in the frame, armies blurred behind",
)
S[(1, 22)] = dict(
    loc="the chariot rolling forward",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna stands in the chariot looking across at the massed enemy, "
        "readying himself to see them face to face"
    ),
    mood="gathering his nerve",
    extra="wind in his hair, hand resting on his bow",
)
S[(1, 23)] = dict(
    loc="still on the chariot approaching the center",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna narrows his eyes at the distant Duryodhana figure at the "
        "head of the Kaurava line, searching faces"
    ),
    mood="focused scanning",
    extra="Duryodhana distantly visible, ominous on a gold-clad chariot",
)
S[(1, 24)] = dict(
    loc="the precise midpoint of the Kurukshetra plain, between two armies totaling nearly four million troops",
    cast=["Krishna", "Arjuna"],
    action=(
        "Krishna reins in the four white stallions; Arjuna's chariot halts "
        "between the two vast facing hosts; the churned dust settles around "
        "its wheels; a sudden hush across millions of soldiers"
    ),
    mood="hush before the storm of the greatest war",
    extra="two colossal armies symmetrically flanking the tiny chariot, stretching to the horizon on both sides",
)
S[(1, 25)] = dict(
    loc="midfield between the armies",
    cast=["Krishna", "Arjuna", "Bhishma", "Drona"],
    action=(
        "Krishna, standing in the chariot, raises a hand toward Bhishma and "
        "Drona and the assembled kings: 'Behold the Kurus gathered here.' "
        "Arjuna looks"
    ),
    mood="revelatory introduction",
    extra="Bhishma, Drona, and kings in stately half-circle ahead of the chariot",
)
S[(1, 26)] = dict(
    loc="Arjuna's point of view from the chariot",
    cast=["Arjuna"],
    action=(
        "Arjuna's face falls as he recognizes, in the massed ranks on both sides, "
        "fathers and grandfathers, teachers, uncles, brothers, cousins, sons, grandsons, friends"
    ),
    mood="dawning horror of recognition",
    extra="montage of familiar faces subtly echoed in the warrior ranks",
)
S[(1, 27)] = dict(
    loc="on the chariot, Arjuna center frame",
    cast=["Arjuna"],
    action=(
        "Arjuna's bow begins to lower; his eyes fill with grief as the weight "
        "of what he is about to do settles on him"
    ),
    mood="swell of sorrow and pity",
    extra="soft light on his face, dust drifting",
)
S[(1, 28)] = dict(
    loc="the chariot, close on Arjuna",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna, trembling, turns to Krishna; his limbs weaken visibly, his "
        "lips parted, mouth gone dry"
    ),
    mood="physical collapse of resolve",
    extra="beads of sweat, hands unsteady on the bow",
)
S[(1, 29)] = dict(
    loc="the chariot",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna's great bow Gandiva slips from his grip and begins to fall; "
        "his skin flushes, hair seeming to stand on end"
    ),
    mood="body betraying the warrior",
    extra="the bow mid-fall rendered with detail, Krishna watching steadily",
)
S[(1, 30)] = dict(
    loc="the chariot",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna staggers, bracing one hand on the rail; he cannot stand "
        "steady, mind reeling — he sees dark omens in the sky"
    ),
    mood="vertigo and foreboding",
    extra="distant ominous birds, dimming light",
)
S[(1, 31)] = dict(
    loc="between the armies",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna gestures outward at the armies with pained dismissal — "
        "rejecting the prospect of kingdom, victory, pleasures"
    ),
    mood="repudiation of earthly gain",
    extra="a royal crown and scattered gold coins lightly visible as symbolic elements in the foreground",
)
S[(1, 32)] = dict(
    loc="the chariot",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna lists off names with a broken voice, gesturing toward the "
        "Kaurava lines; his other hand over his heart"
    ),
    mood="grief for those for whose sake the kingdom was sought",
    extra="figures of family faintly superimposed over the enemy host",
)
S[(1, 33)] = dict(
    loc="midfield",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna points to the front rank: teachers, fathers, sons, grandfathers "
        "in the enemy line, giving up life and wealth"
    ),
    mood="bitter recognition",
    extra="elders at the front of the opposing ranks",
)
S[(1, 34)] = dict(
    loc="the chariot",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna gestures more broadly — uncles, fathers-in-law, grandsons, "
        "brothers-in-law in the enemy host; his arm falls to his side"
    ),
    mood="overwhelmed by kin on both sides",
    extra="three-generation family faintly glimpsed in opposing ranks",
)
S[(1, 35)] = dict(
    loc="between the armies",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna shakes his head slowly: 'What joy could we get from killing "
        "these?' His bow is lowered to the floor of the chariot"
    ),
    mood="moral refusal",
    extra="a dark stain like ink spreading subtly at the chariot floor as symbol of sin",
)
S[(1, 36)] = dict(
    loc="the chariot",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna turns his face away from the army of Dhritarashtra's sons; "
        "an expression of deep aversion and sorrow"
    ),
    mood="ethical revulsion",
    extra="Krishna quietly attentive",
)
S[(1, 37)] = dict(
    loc="on the chariot, close view",
    cast=["Arjuna"],
    action=(
        "Arjuna imagines the Kauravas' blind greed as a shadow passing "
        "over their faces — symbolically rendered as dim veils across the Kaurava line"
    ),
    mood="contemplating their moral blindness",
    extra="literal shadow veils drifting across the enemy faces in the middle distance",
)
S[(1, 38)] = dict(
    loc="the chariot",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna, voice rising, appeals to moral reason — we who see clearly must turn away"
    ),
    mood="ethical plea",
    extra="subtle halo of inner clarity around Arjuna in contrast to the Kaurava shadow",
)
S[(1, 39)] = dict(
    loc="the chariot, symbolic overlay",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna foresees the collapse of family dharma — depicted as a great "
        "ancestral tree faintly cracking in the sky above the battlefield"
    ),
    mood="lament for tradition's collapse",
    extra="ghostly ancestral tree breaking in clouds, roots fraying",
)
S[(1, 40)] = dict(
    loc="the chariot",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna speaks of the corruption of family and social order; "
        "symbolic imagery of toppling pillars behind him"
    ),
    mood="social foreboding",
    extra="stone pillars in the distance visibly leaning",
)
S[(1, 41)] = dict(
    loc="the chariot, heavy with symbolism",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna imagines the family and its destroyers descending into hell; "
        "ancestors depicted as faded ghostly figures deprived of offerings"
    ),
    mood="ancestral dread",
    extra="ghost-figures of ancestors in the sky, an unlit sacrificial vessel in the foreground",
)
S[(1, 42)] = dict(
    loc="the chariot",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna describes the uprooting of the eternal customs of caste and family; "
        "a stone lineage-pillar depicted cracking"
    ),
    mood="institutional unraveling",
    extra="cracks running through a carved ancestral pillar",
)
S[(1, 43)] = dict(
    loc="the chariot",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna looks down, voice heavy with dread; he speaks of long suffering "
        "for those who destroy family tradition"
    ),
    mood="prophetic sorrow",
    extra="deep shadow pooling around his feet",
)
S[(1, 44)] = dict(
    loc="the chariot",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna presses his palms to his forehead: 'We are ready to commit a great sin'"
    ),
    mood="moral self-indictment",
    extra="a faint golden coin image by his feet as symbol of the greed he renounces",
)
S[(1, 45)] = dict(
    loc="midfield",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna opens his arms wide, unarmed, offering himself to the enemy: "
        "'Better that they kill me than I kill them'"
    ),
    mood="surrender of the warrior",
    extra="bow and arrows set down in the chariot",
)
S[(1, 46)] = dict(
    loc="the chariot, wide composition",
    cast=["Krishna", "Arjuna"],
    action=(
        "Arjuna sinks down onto the seat of the chariot, bow and arrows "
        "cast aside; Krishna stands steady at the reins watching him"
    ),
    mood="collapse of resolve",
    extra="the setting itself seems to hush, dust settling",
)
S[(1, 47)] = dict(
    loc="the chariot at midfield, quiet after the collapse",
    cast=["Krishna", "Arjuna"],
    action=(
        "a still, melancholy frame: Arjuna seated, head bowed over his knees, "
        "bow and arrows beside him; Krishna calm, watchful, not yet speaking"
    ),
    mood="the stillness before revelation",
    extra="long slanted light of early morning",
)


# ============================================================================
# CHAPTER 2 — The Way of Knowledge (72 verses)
# Mostly Krishna–Arjuna dialog on the chariot. Distinguished by the teaching
# in each verse, shown as symbolic elements behind or around the pair.
# ============================================================================

S[(2, 1)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna sunk on the chariot seat, eyes downcast and brimming with tears; Krishna turning toward him with a gentle, knowing look",
    mood="compassion meeting despair",
    extra="soft dawn light, dust at rest",
)
S[(2, 2)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna gently raises a palm, speaking with a measured, firm expression; Arjuna's posture begins to straighten as he listens",
    mood="firm but kind rebuke",
    extra="early sun finding Arjuna's face",
)
S[(2, 3)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna bends to pick up Arjuna's fallen bow Gandiva and offers it back to him",
    mood="calling the warrior back to himself",
    extra="bow detailed with gold wrappings, arrows gleaming in a quiver",
)
S[(2, 4)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna", "Bhishma", "Drona"],
    action="Arjuna turns his face toward the distant figures of Bhishma and Drona in the Kaurava line, bow in hand but hanging low",
    mood="reverence at war with duty",
    extra="two venerable figures glowing faintly with respect-halos in the opposing line",
)
S[(2, 5)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna imagines himself as a humble beggar with a simple bowl instead of a warrior; the image superimposed in soft ghost-lines beside him",
    mood="the pull of renunciation",
    extra="a translucent beggar-silhouette of Arjuna hovering beside the armored Arjuna",
)
S[(2, 6)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna's eyes cloud with doubt; a set of scales tips uneasily in the sky behind him",
    mood="unresolved indecision",
    extra="a subtle pair of balance-scales faintly sketched among the clouds",
)
S[(2, 7)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna kneels within the chariot, hands folded, offering himself as a student to Krishna",
    mood="formal surrender to teaching",
    extra="Krishna's hand raised in a gesture of acceptance",
)
S[(2, 8)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna gestures toward a faint ghost-image of a prosperous kingdom and a throne behind him, shaking his head — none of it can remove this grief",
    mood="nothing external can console him",
    extra="faint ghostly kingdom dissolving into smoke",
)
S[(2, 9)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna closes his eyes, mouth set: 'I will not fight' — his hand falls from the bow",
    mood="the refusal stated",
    extra="silence implied by stilled dust",
)
S[(2, 10)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna, as if smiling ever so faintly, begins to speak; the light on his face gentle and clear",
    mood="the beginning of the teaching",
    extra="first gold shaft of sunrise on Krishna",
)
S[(2, 11)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna gestures across the battlefield — the living and the dead — his expression calm: wise do not grieve for either",
    mood="unsentimental clarity",
    extra="one living figure and one fallen figure in the distance, treated with equal compositional weight",
)
S[(2, 12)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="symbolic composition: Krishna gestures up at a long line of luminous soul-figures stretching back through time, all existing eternally",
    mood="the eternal soul-lineage",
    extra="a glowing ribbon of ancestral soul-figures in the sky",
)
S[(2, 13)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="symbolic: one translucent soul-figure passes through a child, a youth, and an elder — then seamlessly into a new body",
    mood="effortless passage of the soul",
    extra="four stages of one figure in soft progression",
)
S[(2, 14)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="around the chariot, a cycle of elements — cold wind, warm sun, pleasure-blossoms, thorns — flowing past and away",
    mood="impermanence of sense experience",
    extra="transient seasonal symbols circling the scene",
)
S[(2, 15)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna stands still and steady while pleasure and pain drift past as golden and gray streams — untouched",
    mood="the sage's immunity",
    extra="two streams of light passing through without effect",
)
S[(2, 16)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna holds one translucent illusion-flame that flickers and one solid bright flame that does not — the unreal and the real",
    mood="metaphysical distinction",
    extra="two flames side by side in Krishna's open palms",
)
S[(2, 17)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="an invisible luminous field pervades the whole battlefield — rendered as soft golden light permeating every figure equally",
    mood="pervading indestructible presence",
    extra="subtle gold mist throughout the scene",
)
S[(2, 18)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="bodies shown as temporary clay vessels around a single steady inner flame — Krishna directs Arjuna's attention to this",
    mood="the eternal within the transient",
    extra="vessel-and-flame motif floating near the two",
)
S[(2, 19)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="symbolic: a sword passes through a luminous soul-figure leaving it untouched; Arjuna watches",
    mood="the soul cannot be slain",
    extra="one sword frozen mid-strike, passing harmlessly through light",
)
S[(2, 20)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna indicates a luminous soul-figure floating free, beyond a cycle of birth-and-death depicted as a faint wheel",
    mood="eternal, unborn, undying",
    extra="large faint wheel of birth/death in the sky, soul-figure outside it",
)
S[(2, 21)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="close on Arjuna: Krishna places a hand on Arjuna's shoulder — how can you kill anyone knowing this?",
    mood="gentle logical pressure",
    extra="Arjuna's grip softening on the bow",
)
S[(2, 22)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="symbolic: a figure discards a worn, ragged robe and puts on a new radiant one — the soul changing bodies",
    mood="natural passage to a new form",
    extra="soul-figure mid-change, two robes clearly contrasted",
)
S[(2, 23)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="four symbolic attacks — a blade, a flame, a splash of water, a gust of wind — all halted around a luminous soul-figure at center",
    mood="invulnerability of the Self",
    extra="four elements frozen at the edges of a radiant sphere",
)
S[(2, 24)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the luminous soul-figure stands serenely steady against wind, water, fire, and blades — untouched, eternal",
    mood="radiant immovability",
    extra="concentric light rings emphasizing unchanging center",
)
S[(2, 25)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna gestures to a faint shimmering outline — something beyond thought, beyond the senses",
    mood="pointing to the unmanifest",
    extra="a near-invisible luminous outline in Krishna's gesture",
)
S[(2, 26)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna shrugs gently — even if you take the other view, grief is still out of place; his tone is patient",
    mood="argument-agnostic compassion",
    extra="the two hand-postures of two views shown in symmetrical gestures",
)
S[(2, 27)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a wheel of birth-and-death, with figures being born on one side and dying on the other — inevitable, cyclical",
    mood="the inescapable cycle",
    extra="large decorative wheel behind the chariot",
)
S[(2, 28)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="three successive silhouettes: unseen → visible → unseen again — faint to solid to faint",
    mood="the middle visibility of beings",
    extra="three-phase silhouette diagram in soft gold",
)
S[(2, 29)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a wondrous mandala of the Self quietly hovering above — some look at it, some speak of it, most don't truly see it",
    mood="the rarity of true knowing",
    extra="jeweled mandala above the chariot, subtle not garish",
)
S[(2, 30)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna sweeps a hand across the battlefield — the eternal One seated in every body depicted as tiny inner flames",
    mood="one Self in all",
    extra="tiny gentle flames at each distant figure's heart",
)
S[(2, 31)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna reminds Arjuna of his kshatriya dharma — a symbolic sword and scale appear in Arjuna's shadow behind him",
    mood="the call of duty",
    extra="shadow-sword and shadow-scale",
)
S[(2, 32)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a gate of heaven opens faintly in the sky before Arjuna — a just war, offered freely, is an open door",
    mood="fortunate opportunity",
    extra="distant gate-of-light in the clouds",
)
S[(2, 33)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="shadow-twin of Arjuna seen turning away from battle — Krishna points to it: lost dharma, lost honor, sin",
    mood="warning of the path not to take",
    extra="dark shadow-twin in negative space",
)
S[(2, 34)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="in the middle distance, whispering groups of warriors imagined — word of dishonor traveling",
    mood="the weight of disgrace",
    extra="silhouettes turning their heads away",
)
S[(2, 35)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a circle of imagined great warriors looking away from Arjuna with contempt — a projected future",
    mood="the pain of lost regard",
    extra="phantom audience of peer warriors",
)
S[(2, 36)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="imagined enemies laughing and jeering at a faint shadow of Arjuna — Krishna counterpoints with a steady presence",
    mood="the bite of mockery",
    extra="phantom jeering silhouettes, far off",
)
S[(2, 37)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna stands taller, bow in hand once more; Krishna's hand on his shoulder — 'Arise, resolved to fight'",
    mood="recovering resolve",
    extra="bow raised from the chariot floor",
)
S[(2, 38)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="symbolic balance: pleasure/pain, gain/loss, victory/defeat — three symmetric scales behind Arjuna, all perfectly level",
    mood="equanimity before battle",
    extra="three balanced scales in gold",
)
S[(2, 39)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna introduces a new teaching — the word 'yoga' suggested by a subtle lotus unfolding between his hands (no text)",
    mood="a pivot to the yoga of action",
    extra="a small lotus between Krishna's palms",
)
S[(2, 40)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a tiny flame at Arjuna's heart grows steadily — even a little of this protects from great fear",
    mood="the small spark of practice",
    extra="a modest but unwavering heart-flame",
)
S[(2, 41)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="symbolic: a single unbranched arrow of light rising from Arjuna's chest, versus many scattered branching arrows",
    mood="focus vs. scattered mind",
    extra="one bright arrow up, many faded arrows fanning out",
)
S[(2, 42)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="in the distance, ritualists perform flowery fire-rituals absorbed only in visible reward; the chariot stands apart",
    mood="critique of showy ritualism",
    extra="distant ritual fire and garlands, contrasted with the quiet chariot",
)
S[(2, 43)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the ritualists chase heaven and power — rendered as figures reaching for a floating distant golden palace",
    mood="chasing limited rewards",
    extra="distant levitating palace and ritualists grasping toward it",
)
S[(2, 44)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="those bound to pleasure and power drift further from the still, lotus-meditative center; Arjuna steady at center",
    mood="the pull of distractions",
    extra="drifting figures radiating outward",
)
S[(2, 45)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="three colored threads — white (sattva), red (rajas), black (tamas) — weave around a figure; Krishna points Arjuna beyond them",
    mood="transcending the three qualities",
    extra="woven three-color motif",
)
S[(2, 46)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a small well half-full beside a great flooding ocean — the Vedas compared to true knowledge",
    mood="a little vs. a lot",
    extra="tiny stone well, vast ocean behind",
)
S[(2, 47)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the most famous verse: Krishna touches Arjuna's hands (action) while turning his face gently away from a luminous golden fruit (results)",
    mood="the keystone teaching",
    extra="luminous symbolic fruit floating separate from the hands",
)
S[(2, 48)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a perfectly level scale balances between Arjuna's hands — success and failure held equal",
    mood="evenness as yoga",
    extra="golden scale between them",
)
S[(2, 49)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="wisdom depicted as a radiant eye opening above Arjuna; action-for-results depicted as a strained figure below reaching for fruit",
    mood="wisdom above grasping",
    extra="symbolic open eye above, grasping silhouette below",
)
S[(2, 50)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="both good and bad deeds, rendered as symbolic threads, drop away from Arjuna as wisdom takes hold",
    mood="freedom from the moral ledger",
    extra="threads of pale gold and pale shadow falling",
)
S[(2, 51)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a wheel of rebirth behind Arjuna cracks and breaks open, releasing him; Krishna at his side",
    mood="release from the cycle",
    extra="large decorative wheel visibly cracked",
)
S[(2, 52)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna steps out of a thick thorny undergrowth of delusion into clear light",
    mood="emerging from confusion",
    extra="thorny thicket behind, open field ahead",
)
S[(2, 53)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna seated in deep steady meditation within the chariot, face serene, posture upright",
    mood="stillness in samadhi",
    extra="faint halo around his head",
)
S[(2, 54)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna leans forward inquiringly — 'what is a person of steady wisdom like?' — hands folded in question",
    mood="earnest question",
    extra="close composition on the two faces",
)
S[(2, 55)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna sets down a simple bowl representing desires; a sage figure near them sits serene without reaching for anything",
    mood="contentment in the Self",
    extra="unadorned wooden bowl, untouched",
)
S[(2, 56)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a sage-figure sits unmoved while storm-clouds (pain), golden rain (pleasure), and sparks (fear, anger) pass around without disturbing him",
    mood="unshaken amid weather",
    extra="weather motifs swirling but missing the center",
)
S[(2, 57)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a sage-figure with arms relaxed to his sides — neither drawn toward good things nor repelled by bad things floating past",
    mood="equanimity in flux",
    extra="symbolic positive and negative tokens drifting past",
)
S[(2, 58)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a tortoise drawing its limbs in — depicted near the chariot as an emblem; the sage beside it mirrors the posture of withdrawn senses",
    mood="elegant self-withdrawal",
    extra="tortoise rendered in careful detail",
)
S[(2, 59)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sense objects depicted as drifting away, but faint ghostly traces of desire linger until a higher light ahead dissolves them",
    mood="abstinence vs. true freedom",
    extra="fading object-shapes, a bright horizon",
)
S[(2, 60)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="restless winds shown as red-gold swirls trying to tug at a wise figure's robes, nearly pulling him off balance",
    mood="the turbulence of the senses",
    extra="wind-ribbons in warm colors",
)
S[(2, 61)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the sage figure seated firmly, reins of the senses held in both hands, gaze fixed on Krishna",
    mood="senses under rein, devotion fixed",
    extra="small reins in the sage's hands — metaphoric, not literal horses",
)
S[(2, 62)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a small chain links object → attachment → desire — dark links growing from a pretty fruit",
    mood="the mechanism of attachment",
    extra="three symbolic links rendered in chain form",
)
S[(2, 63)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the chain continues and darkens: desire → anger → delusion → loss of memory → collapse of reason, ending in a broken figure",
    mood="the cascade into ruin",
    extra="chain continuing from previous motif, ending at a slumped silhouette",
)
S[(2, 64)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a disciplined figure walks among sense-objects unaffected, inner flame steady at his heart",
    mood="peace through discipline",
    extra="calm walk-through composition",
)
S[(2, 65)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sorrows shown as shadows evaporating under clear peaceful light; Arjuna's face softens",
    mood="dissolving of pain",
    extra="shadows visibly lifting from Arjuna",
)
S[(2, 66)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="without discipline, a figure in a turbulent broken landscape; contrasted with the serene chariot center",
    mood="the absence of peace",
    extra="fractured ground around a distant restless figure",
)
S[(2, 67)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a small boat on wind-tossed waters, drifting where the gale blows — symbolic of the mind pulled by senses",
    mood="the unsteered mind",
    extra="small boat on stylized waves beside the chariot",
)
S[(2, 68)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the sage with senses gathered inward like folded petals — a lotus motif at his chest",
    mood="wisdom fully established",
    extra="closed-lotus emblem over the heart",
)
S[(2, 69)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="split composition: in night (for others), the sage figure is awake with a lamp; in day (for others), he rests while they labor",
    mood="inverted wakefulness",
    extra="clear day/night split in the backdrop",
)
S[(2, 70)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a vast ocean receives many rivers but remains undisturbed; the sage beside it at peace",
    mood="the ocean-like mind",
    extra="stylized rivers pouring into still ocean",
)
S[(2, 71)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the sage walks lightly with empty open hands — free of 'mine', free of 'I', untouched by desire",
    mood="simple freedom",
    extra="light footprints fading behind him",
)
S[(2, 72)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna bathed in the soft glow of Brahman-realization; a halo of pure light behind both figures",
    mood="arrival at the state of Brahman",
    extra="gentle gold aura enveloping both",
)


# ============================================================================
# CHAPTER 3 — The Way of Action (43 verses)
# ============================================================================

S[(3, 1)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna, arms spread in confusion, looks from one palm (wisdom) to the other (action) — 'which is it?'",
    mood="honest puzzlement",
    extra="two symbolic icons in the two palms",
)
S[(3, 2)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna folds his hands and asks for one clear answer — the highest good",
    mood="respectful appeal for clarity",
    extra="close framing, direct eye contact",
)
S[(3, 3)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna holds out two symbolic paths — a lotus of contemplation and a wheel of action — side by side",
    mood="two valid paths",
    extra="lotus in left palm, wheel in right palm",
)
S[(3, 4)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a figure tries to sit perfectly still but the very dust settles on him — inaction alone doesn't free one",
    mood="stillness is not enough",
    extra="still ascetic with dust gathering",
)
S[(3, 5)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the three colored threads of the gunas winding around a figure — he is moved whether he likes it or not",
    mood="nature compels action",
    extra="three-thread motif pulling gently",
)
S[(3, 6)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a seated meditator with a serene outer face but his imagined sense-indulgences billow out as colorful smoke from his mind",
    mood="hypocrisy exposed",
    extra="colorful thought-smoke from the head",
)
S[(3, 7)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a disciplined figure acts with clear-eyed ease — senses reined by the mind, body engaged without strain",
    mood="the excellent way",
    extra="calm confident posture",
)
S[(3, 8)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="ordinary daily action — fetching water, tending fire, weaving — depicted as a quiet friezes around the chariot",
    mood="the necessity of doing",
    extra="soft frieze of daily actions around the frame",
)
S[(3, 9)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a ritual fire glowing peacefully — action offered as sacred, not chasing reward",
    mood="action as offering",
    extra="clean modest fire in a bronze vessel",
)
S[(3, 10)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Prajapati (Lord of beings) depicted dimly in the sky creating humans with yajna (offering) side by side — a wish-fulfilling cow (Kamadhenu) motif",
    mood="primordial pact",
    extra="luminous cow-figure beside humans",
)
S[(3, 11)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="humans below, gods above, sharing a beam of mutual nourishment",
    mood="reciprocal sustaining",
    extra="two-way light beam",
)
S[(3, 12)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a figure hoards offerings privately — his silhouette darkens; contrasted with a giver whose image brightens",
    mood="the thief of gifts",
    extra="two contrasted silhouettes",
)
S[(3, 13)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="two meals side by side: one a plate with offering first, then eaten — leaving the diner bright; another where a figure cooks only for himself and is dim",
    mood="offering vs. hoarding",
    extra="two contrasted meal-scenes",
)
S[(3, 14)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="chain of creation: beings ← food ← rain ← sacrifice ← action, rendered as five linked gold rings",
    mood="the ecological chain",
    extra="five symbolic rings in a ring-chain",
)
S[(3, 15)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="an imperishable seed at the top of the chain glowing softly, from which action flows",
    mood="origin of action",
    extra="a luminous seed above the chain",
)
S[(3, 16)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a figure standing alone in a stalled wheel — disconnected from the great cycle, sad and diminished",
    mood="lives in vain",
    extra="halted decorative wheel beside a small dim figure",
)
S[(3, 17)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a serene sage content in the Self — seated under a tree, nothing left to do, the great wheel still turning around him",
    mood="arrival at inner completeness",
    extra="sage beneath a simple tree",
)
S[(3, 18)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the same sage with open empty hands — nothing to gain from doing or not doing, depending on no being",
    mood="freedom from need",
    extra="open peaceful hands",
)
S[(3, 19)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna lifts his bow again — action without attachment, the way to the supreme",
    mood="right action resumed",
    extra="bow raised lightly, no strain",
)
S[(3, 20)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the ancient king Janaka depicted in royal robes among his people, ruling and serving — a model of action-through-perfection",
    mood="the royal sage-king",
    extra="King Janaka figure in gentle middle ground with his subjects",
)
S[(3, 21)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a revered figure at the head of a line of followers; whatever he does, they imitate — depicted as echoing gestures",
    mood="leadership by example",
    extra="a leader with three mirrored figures behind",
)
S[(3, 22)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna himself, with nothing to gain and nothing unattained, still acts — hands visibly engaged though his face is at peace",
    mood="divine ever-active",
    extra="Krishna's hands mid-motion",
)
S[(3, 23)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna in quiet action; distant people mirror his posture — the world follows",
    mood="setting the pattern",
    extra="mirrored distant figures",
)
S[(3, 24)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="symbolic: if the divine ceased acting, the universe-wheel would fall apart — cracks running through a great background mandala",
    mood="cosmic consequence",
    extra="cracking mandala motif",
)
S[(3, 25)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the ignorant work with grit and attachment; the wise work with the same effort but with serene face, for the world's welfare",
    mood="same work, different spirit",
    extra="two figures in parallel poses, different expressions",
)
S[(3, 26)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a wise figure working alongside ordinary workers, inspiring by participation rather than criticism",
    mood="leading by doing",
    extra="communal labor scene in the middle ground",
)
S[(3, 27)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a figure puffed with ego, labeled by a visible sense of 'I' (shown as a swollen illusory ego-bubble); the gunas are actually doing the work around him",
    mood="the ego's illusion",
    extra="exaggerated ego-bubble around a prideful figure",
)
S[(3, 28)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a wise figure watches the three gunas work upon each other — he stands calmly apart",
    mood="seeing through the machinery",
    extra="three gunas as interacting currents",
)
S[(3, 29)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a wise figure refrains from unsettling ignorant workers at their tasks — a gentle 'leave them be' gesture",
    mood="patience with the unawakened",
    extra="gentle halt of the raised hand",
)
S[(3, 30)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna lifts his bow and dedicates it upward — actions offered to Krishna, free of 'mine' and feverish hope",
    mood="action as offering",
    extra="bow raised in offering gesture",
)
S[(3, 31)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="faithful followers of the teaching depicted as a quiet line behind the chariot, unbound by actions",
    mood="practice freeing practitioners",
    extra="small line of serene followers",
)
S[(3, 32)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="contemptuous critics depicted as dim figures wandering into a fog — lost",
    mood="the fate of dismissers",
    extra="fog swallowing critical figures",
)
S[(3, 33)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a wise figure still acting along the lines of his own nature — symbolic: a tree growing in its own shape, not forced into another",
    mood="nature expresses itself",
    extra="tree motif fitting its own form",
)
S[(3, 34)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a figure walking a narrow path between two beasts — one labeled attachment, one aversion — warned to pass between them, not be ruled",
    mood="the twin enemies",
    extra="two symbolic beast silhouettes flanking the path",
)
S[(3, 35)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna's own warrior-path lit in clear gold; a neighboring foreign path lit dimly with danger — his own dharma first",
    mood="the rightness of one's own way",
    extra="two paths parallel in different tones",
)
S[(3, 36)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna asks urgently, palm raised: 'what force pushes us into sin?'",
    mood="the deeper question",
    extra="close on the raised palm",
)
S[(3, 37)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna names the enemy: desire-anger — depicted as a single figure with two heads of flame, rajas-red",
    mood="identifying the enemy",
    extra="twin-flame figure, red and intense",
)
S[(3, 38)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="three images side by side: fire wrapped in smoke, mirror under dust, womb around embryo — all wisdom-under-desire",
    mood="wisdom hidden",
    extra="three emblems arranged in a row",
)
S[(3, 39)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="insatiable fire-like desire burning behind a wise figure's clear face — the eternal enemy",
    mood="a fire that never quenches",
    extra="restless flames rising behind",
)
S[(3, 40)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="desire's hiding places illuminated: senses, mind, intellect — three small lamps labelled only by position, not text",
    mood="knowing where the enemy lives",
    extra="three small lamp-motifs at three levels of the body",
)
S[(3, 41)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna's eyes steady; he places a hand on his chest: first, master the senses",
    mood="the first step",
    extra="quiet decisive gesture",
)
S[(3, 42)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="symbolic ladder: senses → mind → intellect → Self, rendered as a rising column of soft gold light",
    mood="ascending hierarchy",
    extra="four graded levels of light",
)
S[(3, 43)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna stands tall with his sword of knowledge raised — ready to cut down desire; Krishna's hand approvingly on his shoulder",
    mood="resolved to slay the inner enemy",
    extra="symbolic sword of light in Arjuna's hand",
)


# ============================================================================
# CHAPTER 4 — Knowledge, Action, and Letting Go (42 verses)
# ============================================================================

S[(4, 1)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna, framed by a radiant sun behind him, speaks of teaching the eternal yoga first to Vivasvan the sun god (briefly depicted in the sky)",
    mood="ancient transmission",
    extra="faint solar-deity figure in the rising sun",
)
S[(4, 2)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a long lineage of royal sages faintly visible in the clouds, passing a flame one to the next, until the flame dims — the yoga was lost",
    mood="lineage fading",
    extra="cloud-line of sages with a flickering torch",
)
S[(4, 3)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna presents a small bright flame to Arjuna — the same ancient yoga, given now",
    mood="revival of the teaching",
    extra="small flame transferred from Krishna's palm",
)
S[(4, 4)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna looks puzzled — Krishna stands young, Vivasvan was long ago; question drawn in a gentle furrow of the brow",
    mood="sincere confusion",
    extra="subtle age-contrast imagery in the background",
)
S[(4, 5)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="around them, many lifetimes rendered as nested luminous circles receding into depth — Krishna remembers them all",
    mood="memory across lives",
    extra="nested luminous rings in the sky",
)
S[(4, 6)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna, unborn and imperishable, subtly rendered with a faint multi-armed cosmic silhouette behind his human form — the divine within",
    mood="divine behind the human",
    extra="ghost-silhouette of cosmic self beyond the visible form",
)
S[(4, 7)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="when dharma decays, a crack runs through a large stone wheel in the sky; Krishna appears beneath it to restore it",
    mood="the reason for incarnation",
    extra="cracked cosmic wheel, Krishna radiant below",
)
S[(4, 8)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a protector's hand over good people, a purifying fire over the wicked, and a rebuilding pillar of dharma beside — three symbolic panels",
    mood="the three purposes",
    extra="triptych of symbolic actions",
)
S[(4, 9)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a figure who truly knows Krishna's divine deeds depicted passing through a soft luminous gate into Krishna's aura — not born again",
    mood="liberation",
    extra="gate of light receiving the figure",
)
S[(4, 10)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="many ancient seekers (briefly depicted as sages) purified by the austerity of knowledge, merging into soft gold light",
    mood="many have walked this path",
    extra="small row of merging sages",
)
S[(4, 11)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="people approaching Krishna from many directions; Krishna's four arms gently welcoming each in the way they come",
    mood="responding to each",
    extra="soft multi-directional composition",
)
S[(4, 12)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="people in the middle distance offering ritual fires to various devas for quick success — small shrines dotting the landscape",
    mood="the marketplace of results",
    extra="small ritual fires in middle ground",
)
S[(4, 13)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the four varnas depicted as four complementary figures — teacher, warrior, merchant, servant — in a quiet harmonious ring; Krishna stands apart, unbound",
    mood="fourfold order, divine non-doer",
    extra="circle of four figures",
)
S[(4, 14)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="actions attempt to cling to Krishna but slide off like water from polished stone",
    mood="unbound by actions",
    extra="streams of action-threads not sticking",
)
S[(4, 15)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="ancient liberation-seekers at work — depicted in a soft frieze acting with inner calm; Krishna points to their example",
    mood="follow the ancients",
    extra="frieze of working sages",
)
S[(4, 16)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna's brow furrows at the three words: action, inaction, wrong action — three small labelled glyph-icons (not text) hover before him",
    mood="subtle distinctions",
    extra="three simple non-textual symbols",
)
S[(4, 17)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna wading thigh-deep into a mist-covered pool — the deep way of action is hard to see",
    mood="depth and difficulty",
    extra="misted water around Arjuna",
)
S[(4, 18)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a sage sees inaction in action and action in inaction — depicted as a paradoxical double-image, a figure simultaneously still and moving",
    mood="paradox resolved in wisdom",
    extra="overlayed still/moving silhouette",
)
S[(4, 19)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a figure's undertakings burn away in a small bright fire at their heart — the fire of wisdom",
    mood="actions consumed by wisdom",
    extra="small heart-fire",
)
S[(4, 20)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a figure at work who looks still, relaxed, depending on nothing — a glow of contentment around him",
    mood="content in action",
    extra="halo of contentment",
)
S[(4, 21)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a minimalist figure with only the body acting — few possessions laid in simple order beside him",
    mood="bare-bones action",
    extra="a handful of simple objects",
)
S[(4, 22)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the same figure receives food, wealth, or nothing with the same faint smile — beyond the pairs of opposites",
    mood="content with what comes",
    extra="three symmetric offerings, one smile",
)
S[(4, 23)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a liberated worker: his actions are offered upward and dissolve into pure light; all karma dissolves",
    mood="karma dissolving",
    extra="actions rising as luminous smoke",
)
S[(4, 24)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a single great fire of Brahman at the center, in which offering, sacrificer, and act are all one — rendered as a unified luminous medallion",
    mood="all is Brahman",
    extra="central medallion of unified fire",
)
S[(4, 25)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="two kinds of yogis depicted in the middle distance: some offering material sacrifice to gods, others offering sacrifice itself into the fire of Brahman",
    mood="two approaches to offering",
    extra="two contrasting altars",
)
S[(4, 26)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="some offer the senses into fires of self-restraint; others offer sense-objects into fires of the senses — shown as two symbolic pairs of fire-altars",
    mood="disciplining the senses",
    extra="two pairs of small altars",
)
S[(4, 27)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="all sense-activity and breath offered into a central fire of self-mastery, kindled by wisdom",
    mood="total offering",
    extra="central flame brighter than the rest",
)
S[(4, 28)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="four small scenes in a diamond: giving wealth, austerity, yoga-posture, study — all as forms of sacrifice",
    mood="many forms of sacrifice",
    extra="four mini vignettes in a diamond layout",
)
S[(4, 29)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a meditator regulates breath — visual arcs of prana (inbreath) and apana (outbreath) interchanging",
    mood="breath offered to breath",
    extra="two curling breath-arcs",
)
S[(4, 30)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a disciplined figure restricting food, sins burning away as pale smoke from his shoulders",
    mood="purification through restraint",
    extra="small plume of dissolving smoke",
)
S[(4, 31)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a sage eats the nectar-remnants of offering from a simple bowl; Brahman's soft light around him",
    mood="nourished by sacred remnants",
    extra="a glowing bowl of sacred food",
)
S[(4, 32)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="many types of sacrifices spread out on a broad altar at the mouth of a luminous Brahman-face/portal",
    mood="variety arising from the One",
    extra="wide altar, wide portal of light",
)
S[(4, 33)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a sacrifice of wealth (coins on an altar) and a sacrifice of wisdom (open book of light) — the latter glows brighter",
    mood="wisdom's superiority",
    extra="two altars, one clearly brighter",
)
S[(4, 34)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a student bows humbly before a seated realized teacher — asks, serves; the teacher's hand rests gently on his head",
    mood="humility before the knower",
    extra="classical teacher-student bow",
)
S[(4, 35)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna's eyes open wide — he begins to see every being inside himself and himself in Krishna, rendered as gentle translucent overlays",
    mood="unity glimpsed",
    extra="faint overlayed reflections of beings",
)
S[(4, 36)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a small dark boat of wisdom crosses an ocean of evil — a figure formerly burdened now standing steady at the prow",
    mood="deliverance by wisdom",
    extra="simple boat on a dark stylized ocean",
)
S[(4, 37)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a blazing fire turning firewood to ashes — the fire of wisdom reducing all actions",
    mood="total consumption of karma",
    extra="bright fire central in composition",
)
S[(4, 38)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="nothing purifies like wisdom — a figure stands cleansed by an inner light, not outer water",
    mood="inner purity",
    extra="cleansing inner glow",
)
S[(4, 39)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a faithful, committed seeker receives wisdom like a clear stream poured into cupped hands; immediately peace around him",
    mood="faith bearing fruit",
    extra="bright stream into cupped palms",
)
S[(4, 40)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a doubting figure stands in a fog with no ground — neither this world nor the next nor happiness",
    mood="the cost of doubt",
    extra="fog without horizon",
)
S[(4, 41)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a yogi at ease — actions no longer bind, doubts cut away by wisdom, rendered as a figure with two symbolic broken chains",
    mood="released by wisdom",
    extra="two snapped chains at his feet",
)
S[(4, 42)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna raises the symbolic sword of knowledge and cuts a dark thread of doubt at his chest — then stands up",
    mood="take up yoga, stand up",
    extra="thread visibly parted",
)


# ============================================================================
# CHAPTER 5 — The Way of Renunciation (29 verses)
# ============================================================================

S[(5, 1)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna gestures back and forth — renunciation in one hand, action in the other — asking which is better",
    mood="honest reconciliation asked",
    extra="two-handed weighing gesture",
)
S[(5, 2)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna places the two hands together — both paths lead to the highest, but the way of action is slightly preferred",
    mood="both paths, one goal",
    extra="two hands joining",
)
S[(5, 3)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a serene figure neither grasping nor pushing away — hands open and relaxed, freed from opposites",
    mood="the lifelong renouncer within action",
    extra="balanced open-handed posture",
)
S[(5, 4)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="children play dividing two puzzle pieces; two adult sages behind them see the pieces already fit together",
    mood="children divide, wise unite",
    extra="gentle allegorical backdrop of children and sages",
)
S[(5, 5)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="two paths converging into a single luminous goal above; one figure on each path arriving together",
    mood="unity of the two ways",
    extra="two paths meeting at a shining goal",
)
S[(5, 6)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a renouncer struggles alone on a steep path; a yogi of action ascends smoothly — arrives quickly at Brahman",
    mood="yoga eases the climb",
    extra="two contrasted climbing figures",
)
S[(5, 7)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a yoked yogi working in the world, his self expanded as a soft light encompassing every being in the scene",
    mood="one Self in all beings",
    extra="soft aura enveloping surrounding figures",
)
S[(5, 8)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a wise figure at work — seeing, hearing, touching, eating — yet an inner stillness depicted as a motionless center",
    mood="acting yet not acting",
    extra="still radiant core within an active body",
)
S[(5, 9)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="senses as small figures reaching out to sense-objects around a central still figure — 'senses moving among objects'",
    mood="witnessing the machinery",
    extra="small sense-figures around a calm center",
)
S[(5, 10)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a lotus leaf with a drop of water rolling off — actions roll off the unattached",
    mood="untouched by action",
    extra="detailed lotus leaf with water drop",
)
S[(5, 11)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a figure acts with body, mind, intellect, and senses — purifying the self; a small inner flame brightening with each act",
    mood="purifying through offered action",
    extra="brightening heart-flame",
)
S[(5, 12)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="one figure letting go of fruits and stepping into peace; another gripping fruits and caught in a thorny net",
    mood="two fates",
    extra="contrast of peaceful figure and entangled figure",
)
S[(5, 13)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a sage seated serenely inside a nine-gated dwelling (the body) depicted as an elegant nine-arched pavilion",
    mood="at rest in the city of nine gates",
    extra="elegant pavilion with nine soft-lit arches",
)
S[(5, 14)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the indwelling Self seated calmly; nature (prakriti) depicted as a flowing current doing the acting around it",
    mood="nature acts, Self rests",
    extra="flowing current encircling a still center",
)
S[(5, 15)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the all-pervading One surrounded by beings covered by clouds (ignorance); no sin or merit sticks to the One",
    mood="untouched Lord",
    extra="clouds around beings, clear space at center",
)
S[(5, 16)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="knowledge destroys ignorance — a sun rising over a landscape at dawn, illumining the Supreme",
    mood="sun of wisdom",
    extra="fresh sunrise composition",
)
S[(5, 17)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a seeker's self rooted in That — symbolic: a tree whose root is a brilliant star above and whose branches reach below",
    mood="rooted in the Supreme",
    extra="inverted luminous tree motif",
)
S[(5, 18)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a learned brahmin, a cow, an elephant, a dog, and a humble outcast all depicted in a single row, viewed by a wise sage with equal gaze",
    mood="equal vision",
    extra="row of five figures in equal light",
)
S[(5, 19)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a figure whose mind is steady in sameness, framed by a soft balanced mandala — established in Brahman",
    mood="unshaken sameness",
    extra="small balanced mandala around the figure",
)
S[(5, 20)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a sage calmly receiving both a garland (pleasant) and a thorn (unpleasant) with the same gentle expression",
    mood="steady in both",
    extra="two offerings, one expression",
)
S[(5, 21)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the sage's joy depicted as coming from within — a glowing inner well, not from the outer scene",
    mood="inner imperishable joy",
    extra="small glowing inner well",
)
S[(5, 22)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="pleasures from sense-contact shown as flowers that quickly turn to thorns — the wise do not delight in them",
    mood="impermanent sensory pleasures",
    extra="flowers-to-thorns motif",
)
S[(5, 23)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a yoked figure withstands surges of desire (red gold) and anger (scarlet) as waves breaking against a calm shore",
    mood="withstanding the surges",
    extra="waves meeting a steady shoreline",
)
S[(5, 24)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a yogi whose happiness and light come from within — Brahman's peace surrounding him in soft gold",
    mood="becoming Brahman",
    extra="soft gold aura",
)
S[(5, 25)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a group of sages working for the welfare of all beings — the peace of Brahman touching them as gentle descending light",
    mood="peace to the benefactor-sages",
    extra="soft light above a working group",
)
S[(5, 26)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="disciplined ascetics, freed from desire and anger, with the peace of Brahman all around them like a surrounding aura",
    mood="near-at-hand freedom",
    extra="continuous aura field",
)
S[(5, 27)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a yogi in perfect seated meditation, gaze gently fixed between the eyebrows, inbreath and outbreath balanced as arcs",
    mood="meditation's outer form",
    extra="two small breath-arcs at the nose",
)
S[(5, 28)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the yogi freed from desire, fear, and anger — truly always free; three faded chains lie broken at his feet",
    mood="always free",
    extra="three broken chain-motifs",
)
S[(5, 29)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna receives offerings from all directions — known as the receiver, the great Lord, the friend of all beings; peace settles on Arjuna",
    mood="resting in divine friendship",
    extra="subtle multi-directional offerings",
)


# ============================================================================
# CHAPTER 6 — The Way of Meditation (47 verses)
# Meditation postures, discipline, the lamp-in-windless-place, falling and
# rising yogis, the highest yogi absorbed in Me.
# ============================================================================

S[(6, 1)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna rests a hand on a plough and a lamp side by side — the true renouncer is the one who works without depending on results",
    mood="integrating work and renunciation",
    extra="plough and lamp side by side",
)
S[(6, 2)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a scroll-ribbon over the two: what is called renunciation and yoga are one — two names wrapping into one",
    mood="unity of terms",
    extra="two ribbons merging into one",
)
S[(6, 3)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a figure climbing a ladder of action; at the top, the same figure seated in deep stillness — two stages depicted",
    mood="action, then stillness",
    extra="ladder and seated figure",
)
S[(6, 4)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a figure freed from sense-objects and actions, empty-handed and calm — arrived at yoga",
    mood="renouncing intentions",
    extra="open empty hands",
)
S[(6, 5)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a person lifts his own silhouette upward out of a pit with his own rope; self raised by the Self",
    mood="self-elevation",
    extra="rope-and-pit allegory",
)
S[(6, 6)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="mirror-split composition: one side Self as friend (a warm hand); the other Self as enemy (a closed fist) — depending on self-mastery",
    mood="the friend or the enemy",
    extra="mirror-split of two hand gestures",
)
S[(6, 7)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a peaceful figure steady through cold snow, warm sun, honor-garlands, and scorn-thorns depicted in a four-quadrant composition",
    mood="steady through the opposites",
    extra="four symbolic quadrants",
)
S[(6, 8)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a yogi beside a clod, a stone, and a gold ingot — looks at all three equally",
    mood="equal to clod, stone, gold",
    extra="three materials in a row",
)
S[(6, 9)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a wise figure seated among a circle of friends, foes, neutrals, the righteous, even the sinful — viewing each with equal calm",
    mood="equal mind in all relations",
    extra="symmetrical circle of varied figures",
)
S[(6, 10)] = dict(
    loc="a quiet forest clearing at early dawn",
    cast=["Arjuna"],
    action="a lone meditator sits in a hidden glade, body still, mind composed, a small stream nearby",
    mood="solitary recollection",
    extra="deer and birds in the middle distance, undisturbed",
)
S[(6, 11)] = dict(
    loc="the same forest clearing",
    cast=[],
    action="a low seat being prepared: a clean flat stone layered with kusha grass, a deer-skin, and a plain cloth",
    mood="preparing the seat",
    extra="close-up of the layered seat",
)
S[(6, 12)] = dict(
    loc="the clearing",
    cast=[],
    action="the meditator seated, mind one-pointed; a soft gold halo at the heart",
    mood="one-pointed mind",
    extra="subtle heart-glow",
)
S[(6, 13)] = dict(
    loc="the clearing",
    cast=[],
    action="the meditator sits very upright — body, head, neck in line — gaze soft at the tip of the nose",
    mood="upright steady posture",
    extra="straight line through body",
)
S[(6, 14)] = dict(
    loc="the clearing",
    cast=[],
    action="a meditator with a serene face, faint aura, fearless; mind fixed — a tiny luminous Krishna-figure at the center of meditation",
    mood="devotion-centered meditation",
    extra="tiny Krishna-silhouette at the heart",
)
S[(6, 15)] = dict(
    loc="the clearing, soft dawn",
    cast=[],
    action="the yogi deep in practice; waves of peace visibly radiating outward; a subtle suggestion of nirvana as vast calm light",
    mood="peace ending in nirvana",
    extra="expanding calm light",
)
S[(6, 16)] = dict(
    loc="the clearing",
    cast=[],
    action="a table of moderation: neither an overfull plate nor an empty one; neither long sleep nor sleepless — balanced icons",
    mood="moderation",
    extra="balanced pairs of icons",
)
S[(6, 17)] = dict(
    loc="the clearing",
    cast=[],
    action="a balanced figure whose food, recreation, effort, sleep are rendered as four small balanced scales around him",
    mood="measured life",
    extra="four small scales in balance",
)
S[(6, 18)] = dict(
    loc="the clearing",
    cast=[],
    action="the disciplined mind settling in the Self — rendered as a dove settling calmly onto a lotus",
    mood="mind at rest in the Self",
    extra="dove and lotus motif",
)
S[(6, 19)] = dict(
    loc="the clearing",
    cast=[],
    action="a lamp in a windless place burning perfectly upright, unflickering — the classical Gita simile",
    mood="unwavering mind",
    extra="detailed still-flame lamp",
)
S[(6, 20)] = dict(
    loc="the clearing",
    cast=[],
    action="the meditator seeing the Self by the Self — reflected inner mirror image inside his chest, serene",
    mood="Self seeing Self",
    extra="inner mirror motif",
)
S[(6, 21)] = dict(
    loc="the clearing",
    cast=[],
    action="a soft infinite radiance opens above the yogi — happiness grasped by the intellect, beyond the senses",
    mood="bliss beyond senses",
    extra="soft opening of light above",
)
S[(6, 22)] = dict(
    loc="the clearing",
    cast=[],
    action="a mountain-steady figure unshaken by heavy sorrow, rendered as dark clouds breaking harmlessly against him",
    mood="unshakable",
    extra="clouds around a rock-still figure",
)
S[(6, 23)] = dict(
    loc="the clearing",
    cast=[],
    action="a thread of pain visibly cut — yoga as severance from pain; resolute eyes",
    mood="severance of suffering",
    extra="cleanly cut thread",
)
S[(6, 24)] = dict(
    loc="the clearing",
    cast=[],
    action="many small desires released as small birds flying away; senses restrained by gentle steady hands",
    mood="releasing desires",
    extra="released birds, quiet hands",
)
S[(6, 25)] = dict(
    loc="the clearing",
    cast=[],
    action="the meditator's mind settles step by step — depicted as a series of descending soft ripples on a pond",
    mood="gradual stilling",
    extra="ripples fading to flat water",
)
S[(6, 26)] = dict(
    loc="the clearing",
    cast=[],
    action="a wandering small spark of mind being gently led back to a central flame — bringing the mind back again and again",
    mood="patient return",
    extra="small spark returning to center",
)
S[(6, 27)] = dict(
    loc="the clearing",
    cast=[],
    action="supreme happiness arrives as the meditator — rendered with calm face, free from stain, becoming Brahman; very soft aura",
    mood="supreme bliss",
    extra="expansive soft aura",
)
S[(6, 28)] = dict(
    loc="the clearing",
    cast=[],
    action="the yogi easily at infinite contact with Brahman — depicted as a calm ocean meeting the sky, the yogi a small figure at peace in the scene",
    mood="easy infinite contact",
    extra="ocean-sky horizon",
)
S[(6, 29)] = dict(
    loc="the clearing",
    cast=[],
    action="the yogi sees the Self everywhere — all surrounding beings have tiny inner flames identical to his own",
    mood="same Self in all",
    extra="identical flames in all beings",
)
S[(6, 30)] = dict(
    loc="the clearing",
    cast=[],
    action="Krishna depicted as luminous presence pervading everything; the yogi and all around held within it, nothing lost",
    mood="not lost to the divine",
    extra="pervading golden light",
)
S[(6, 31)] = dict(
    loc="the clearing",
    cast=[],
    action="the yogi worships Krishna as present in every being — small Krishna-suggestions in each nearby figure",
    mood="dwelling in Krishna",
    extra="small Krishna-echoes throughout",
)
S[(6, 32)] = dict(
    loc="the clearing",
    cast=[],
    action="the yogi feels another's pleasure and pain as his own — depicted as a mirrored heart-flame shared between two figures",
    mood="the highest yogi's empathy",
    extra="shared heart-flame motif",
)
S[(6, 33)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna shakes his head — the mind is too restless for such evenness",
    mood="honest resistance",
    extra="gesture of frustration, not anger",
)
S[(6, 34)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="stylized depiction of a wild wind tugging at a restless figure — 'like trying to tame the wind'",
    mood="the mind's wildness",
    extra="wind-ribbons",
)
S[(6, 35)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna gently names two tools — abhyasa (practice) and vairagya (detachment) — shown as two small keys in his hand",
    mood="the two keys",
    extra="two symbolic keys, no text",
)
S[(6, 36)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a striving figure with disciplined eyes makes steady progress up a hill; Krishna points him onward",
    mood="effort is the way",
    extra="hill-path with a determined figure",
)
S[(6, 37)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna asks: what happens to the faithful striver whose mind wanders and who does not reach perfection?",
    mood="worry for the honest seeker",
    extra="sincere questioning posture",
)
S[(6, 38)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a broken cloud drifts across a calm sky — the question of the fallen yogi visualized",
    mood="the image of the broken cloud",
    extra="single wispy torn cloud",
)
S[(6, 39)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna folds his hands and asks Krishna to dispel this doubt completely",
    mood="earnest request",
    extra="folded-hand gesture",
)
S[(6, 40)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna smiles gently — no one who does good is ever lost; a warm reassuring hand",
    mood="reassurance",
    extra="warm hand-gesture",
)
S[(6, 41)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the fallen yogi depicted reborn into a pure, prosperous household; gentle sunlit domestic scene in the middle distance",
    mood="rebirth among the good",
    extra="peaceful home in middle ground",
)
S[(6, 42)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="or even born into a family of wise yogis — a small hut of sages welcoming a new-born soul depicted softly",
    mood="rare birth among sages",
    extra="sage-family scene",
)
S[(6, 43)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a young seeker recalls his past life's understanding — a faint ribbon of memory flowing into his head from the sky",
    mood="recovered realization",
    extra="memory-ribbon from above",
)
S[(6, 44)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the young seeker is carried forward almost automatically by prior practice — a gentle current lifting his steps",
    mood="carried by past effort",
    extra="soft current under the feet",
)
S[(6, 45)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="perfected across many lives, the yogi arrives at the supreme — a figure reaching a luminous summit",
    mood="final arrival",
    extra="summit in glow",
)
S[(6, 46)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a hierarchy: ascetics, the learned, ritualists, and above them all, the yogi; Krishna points upward",
    mood="the yogi the greatest",
    extra="stacked small figures in order",
)
S[(6, 47)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the highest yogi: a devotee with inner self absorbed in Krishna — Krishna's figure faintly luminous within the devotee's chest",
    mood="absorbed in the beloved",
    extra="Krishna-within motif at the heart",
)


# ============================================================================
# CHAPTER 7 — Knowledge and Realization (30 verses)
# ============================================================================

S[(7, 1)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna invites Arjuna to listen closely — mind fixed on him, refuge in him, practicing yoga",
    mood="intimate invitation",
    extra="close composition, soft light",
)
S[(7, 2)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna begins to reveal knowledge together with realization — hands opening like a book of light (no text)",
    mood="the full teaching",
    extra="open-palmed gesture with soft light",
)
S[(7, 3)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a vast crowd in the distance — only one or two figures emit inner light, the true knowers",
    mood="the rarity of the knower",
    extra="crowd with sparse lights",
)
S[(7, 4)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="eight symbolic tokens arranged in a ring — earth, water, fire, air, space, mind, intellect, ego — Krishna's lower nature",
    mood="the eightfold lower nature",
    extra="eight non-textual glyphs in a ring",
)
S[(7, 5)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="within the ring, a radiant inner sphere of life-principle — the higher nature sustaining all",
    mood="the higher nature within",
    extra="inner radiant sphere",
)
S[(7, 6)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna as origin and dissolution — the two hands forming a circle, within which all beings arise and set",
    mood="Alpha and Omega",
    extra="circling hands motif",
)
S[(7, 7)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="all of creation strung on a single thread like jewels on a string — Krishna holding the thread in his hand",
    mood="the thread of all",
    extra="thread-of-jewels motif",
)
S[(7, 8)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna pointing to the taste-shimmer in water, the light in sun and moon, and a halo of sacred 'Om' energy (depicted as concentric circles, not text)",
    mood="divine presence in ordinary",
    extra="concentric sound-rings, shimmering water",
)
S[(7, 9)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="fragrance of earth visualized as scented mist rising from the ground; brilliance in flame behind him",
    mood="divine in scent and flame",
    extra="rising scented mist",
)
S[(7, 10)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna as the eternal seed — a luminous seed in his palm, sprouting gently into all beings of the field",
    mood="origin of beings",
    extra="luminous sprouting seed",
)
S[(7, 11)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna as the strength of the strong — his free right arm glowing; desire-that-aligns-with-dharma shown as a calm golden thread",
    mood="strength without greed",
    extra="single calm gold thread",
)
S[(7, 12)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="three colored streams (sattva white, rajas red, tamas indigo-black) issuing from Krishna but not containing him — he stands beyond",
    mood="the three come from Him, not vice versa",
    extra="three-stream motif around Krishna",
)
S[(7, 13)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a crowd in the three colored currents, confused, not seeing Krishna standing clearly behind them",
    mood="the world's confusion",
    extra="people absorbed in colored currents",
)
S[(7, 14)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="divine maya depicted as a shimmering veil; those taking refuge in Krishna step through it into clear space",
    mood="crossing maya",
    extra="shimmering veil with a doorway of light",
)
S[(7, 15)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a dim crowd turning away from Krishna, clinging to a shadowy demonic-looking form — they do not take refuge",
    mood="those who refuse",
    extra="shadow-form opposite Krishna",
)
S[(7, 16)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="four kinds of devotees approaching Krishna: a distressed person, a seeker of knowledge, a seeker of success, and a wise sage",
    mood="four kinds of virtuous seekers",
    extra="four figures kneeling at Krishna's side",
)
S[(7, 17)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="of the four, the wise sage's figure glows most; Krishna places a hand on his shoulder",
    mood="the wise most beloved",
    extra="single glow on the sage",
)
S[(7, 18)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="all four depicted as noble; but the wise sage's form visibly merges into Krishna's aura",
    mood="the wise as Krishna's own Self",
    extra="merging auras",
)
S[(7, 19)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="at the end of many lifetimes, a seeker realizes 'all this is Krishna' — depicted as Krishna reflected softly in every object of the scene",
    mood="Vasudeva is all this",
    extra="Krishna's gentle reflection everywhere",
)
S[(7, 20)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="others, carried by specific desires, turn to lesser deities — depicted as small shrines far in the background",
    mood="many deities for many desires",
    extra="far-off small shrines",
)
S[(7, 21)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna steadies the faith of each devotee in the form they chose — his hand held protectively over a distant small shrine",
    mood="steadying faith",
    extra="protective gesture",
)
S[(7, 22)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the devotee receives results from the chosen deity — a modest gift in hand — but the gift ultimately comes from Krishna's larger light",
    mood="the source behind gifts",
    extra="gift and larger background light",
)
S[(7, 23)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="limited fruits fade quickly; devotees of lesser deities reach those deities, devotees of Krishna come to Krishna — two distinct paths rendered",
    mood="different destinations",
    extra="two paths with distinct ends",
)
S[(7, 24)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="foolish people think Krishna is merely human — depicted as a reduced small silhouette; the true vast Krishna stands behind, transcending",
    mood="the mistake of reduction",
    extra="small silhouette in front of true vast form",
)
S[(7, 25)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="yoga-maya as a luminous veil around Krishna; many in the world cannot see past it",
    mood="veiled by yoga-maya",
    extra="luminous veil motif",
)
S[(7, 26)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna's gaze sees all beings past, present, future — three faint concentric time-circles behind him",
    mood="all-knowing seer",
    extra="three nested time-circles",
)
S[(7, 27)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="pairs of opposites (like/dislike) depicted as twin tugging ribbons pulling people about in the middle distance",
    mood="confused by opposites",
    extra="twin ribbon motif",
)
S[(7, 28)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the virtuous, sins ended, step past the opposites — two broken ribbons at their feet, firm vows in hand",
    mood="freed by virtue",
    extra="broken ribbons",
)
S[(7, 29)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="seekers striving for freedom from old age and death, taking refuge in Krishna — symbolic old age and death figures melt behind them",
    mood="striving for liberation",
    extra="melting symbolic figures",
)
S[(7, 30)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna named as the principle behind beings, gods, sacrifices — three soft symbols around his head, simple non-textual glyphs",
    mood="threefold principle",
    extra="three simple glyph-motifs",
)


# ============================================================================
# CHAPTER 8 — The Imperishable Reality (28 verses)
# ============================================================================

S[(8, 1)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna, hands folded, asks a series of questions — rendered as small question-glyphs (gentle swirls, no text) around him",
    mood="probing terminology",
    extra="question-swirls",
)
S[(8, 2)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna specifically asks about the hour of death — a soft twilight light behind him",
    mood="the final question",
    extra="twilight backlight",
)
S[(8, 3)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna, with calm authority, defines terms — soft light rising around him as each term is named",
    mood="definitive teaching",
    extra="rising light motif",
)
S[(8, 4)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna points to himself — the principle behind sacrifice here in the body — a gentle heart-flame lit within his own chest",
    mood="'I am within you'",
    extra="heart-flame motif",
)
S[(8, 5)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="at the hour of death a soul-figure leaves its body remembering Krishna — reaches Krishna's aura above",
    mood="remembrance at death",
    extra="soul-figure rising to a luminous Krishna-presence",
)
S[(8, 6)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a last thought rendered as a small glowing token held by a dying figure — to that token he goes",
    mood="what one dwells on becomes one's next state",
    extra="glowing token in hand",
)
S[(8, 7)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna with bow at ready in one hand and Krishna's name at his heart (depicted as a Krishna-silhouette glow) in the other — 'remember and fight'",
    mood="action plus remembrance",
    extra="two-sided composition",
)
S[(8, 8)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a yogi, mind unwavering, reaching the supreme divine Person — a luminous Purusha figure above",
    mood="meditating on the supreme",
    extra="luminous cosmic Purusha above",
)
S[(8, 9)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the supreme depicted as omniscient ancient ruler, sun-colored, beyond darkness — vast cosmic figure in the sky",
    mood="attributes of the Supreme",
    extra="cosmic ruler in glowing mist",
)
S[(8, 10)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a dying yogi draws breath fully between the eyebrows — a visible upward light-arrow from breath to crown",
    mood="the yogic departure",
    extra="upward light-arrow between brows",
)
S[(8, 11)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="ascetics practicing celibacy and self-control move toward a single luminous imperishable goal at the horizon",
    mood="the Imperishable",
    extra="horizon-goal in soft gold",
)
S[(8, 12)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="gates of the body symbolically closed; mind drawn into the heart; life-breath gathered in the head — soft diagram over a meditator",
    mood="internal consolidation",
    extra="soft posture-diagram",
)
S[(8, 13)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the sacred syllable 'Om' depicted as three nested circular sound-rings radiating from a meditator's mouth (no text)",
    mood="Om at the moment of departure",
    extra="triple sound-rings",
)
S[(8, 14)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a yogi always remembering Krishna; Krishna depicted near at hand, easy to reach",
    mood="easy access by remembrance",
    extra="Krishna as near companion",
)
S[(8, 15)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="great souls arrived at Krishna — small circle of realized sages gathered in his aura, freed from rebirth",
    mood="no return",
    extra="circle of sages in Krishna's aura",
)
S[(8, 16)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the creator Brahma's world at top of a descending ladder of realms, all still returning to rebirth; Krishna above them all, beyond",
    mood="beyond all return",
    extra="ladder of realms with Krishna above",
)
S[(8, 17)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Brahma's day and night — vast golden dawn and deep indigo night rendered as two halves of a great clock face",
    mood="day and night of Brahma",
    extra="split golden/indigo clock-face",
)
S[(8, 18)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="at dawn, manifestations stream out of a soft unmanifest source; at dusk they are drawn back — two arcs",
    mood="emergence and return",
    extra="two symmetrical arcs of manifestation",
)
S[(8, 19)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="multitudes of beings helplessly cycling into and out of the unmanifest — small figures riding a great breath-like current",
    mood="helpless cycle",
    extra="current carrying small figures",
)
S[(8, 20)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="beyond the unmanifest, another eternal unmanifest depicted as a still point of light untouched by the cycle",
    mood="beyond the cycle",
    extra="single still point above the current",
)
S[(8, 21)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the supreme abode — a distant luminous city from which none return; a figure approaching its gates",
    mood="the supreme abode",
    extra="distant luminous city",
)
S[(8, 22)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna at the center of all beings — they rest in him, he pervades them — rendered as concentric rings around Krishna",
    mood="all beings resting in Him",
    extra="concentric ring composition",
)
S[(8, 23)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna begins to describe the two paths of departure — two faint roads ahead, one bright, one shadowed",
    mood="two paths introduced",
    extra="bright path and shadow path",
)
S[(8, 24)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the bright path: fire, light, day, bright fortnight, northern course — ascending sun-symbols along a climbing road",
    mood="path of no return",
    extra="sun-symbols climbing",
)
S[(8, 25)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the dark path: smoke, night, dark fortnight, southern course — moon and mist along a lower road leading back",
    mood="path of return",
    extra="moon-mist road",
)
S[(8, 26)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the two eternal paths side by side; one leading to non-return, one to return — a yogi contemplating both",
    mood="the eternal two",
    extra="parallel paths with a contemplator",
)
S[(8, 27)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the yogi, knowing these two, is not confused; Krishna encourages Arjuna to remain ever yoked",
    mood="clarity through knowing",
    extra="calm confident composition",
)
S[(8, 28)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the yogi goes beyond all merit of Vedas, sacrifices, austerities, gifts — arrives at the primal abode as a calm figure reaching a shining doorway",
    mood="transcending all merit",
    extra="shining doorway reached",
)


# ============================================================================
# CHAPTER 9 — The Royal Secret (34 verses)
# ============================================================================

S[(9, 1)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna leans in close — the most profound secret is about to be shared with one who does not cavil",
    mood="the secret shared",
    extra="very close framing",
)
S[(9, 2)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the king-of-sciences depicted as a small golden crown on an open page of light — pure purifier",
    mood="royal knowledge",
    extra="crown on a radiant surface",
)
S[(9, 3)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="those without faith drift in a faint spiraling current of rebirth behind Krishna — they do not reach him",
    mood="the fate of the faithless",
    extra="drifting spiral figures",
)
S[(9, 4)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna unmanifest pervading all; beings subtly drawn inside a luminous body-outline of Krishna",
    mood="all beings within the unmanifest",
    extra="translucent Krishna-outline holding everything",
)
S[(9, 5)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="paradox rendered: beings inside Krishna's outline but also separate dots floating — 'they are not in Me' — divine yoga",
    mood="divine paradox",
    extra="dual composition",
)
S[(9, 6)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the mighty wind moving everywhere rests in space — depicted as stylized wind-ribbons always held in a clear still sky",
    mood="wind-in-space metaphor",
    extra="wind-ribbon detail",
)
S[(9, 7)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="at the end of a cosmic cycle, all beings drawn back into Krishna's nature — depicted as a slow inward spiral of small lights",
    mood="dissolution at cycle's end",
    extra="inward light-spiral",
)
S[(9, 8)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="at the start of the next cycle, the spiral reverses and beings stream out again — Krishna serene, both hands gently releasing",
    mood="re-emanation",
    extra="outward light-spiral",
)
S[(9, 9)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna sits as if indifferent, actions passing by without binding him — symbolic loops flowing around without attaching",
    mood="unattached yet active",
    extra="loops flowing around Krishna",
)
S[(9, 10)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="nature depicted as a weaver producing moving and unmoving things; Krishna overseeing from behind as calm presence",
    mood="Krishna as overseer",
    extra="weaver of nature in the middle distance",
)
S[(9, 11)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="fools depicted dismissing the human Krishna; the vast Lord-form within him hinted at in luminous outline",
    mood="dismissing the human form",
    extra="small dismissive figures vs. vast hidden form",
)
S[(9, 12)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="those with demonic nature, their hopes and actions falling into futility — hands full of dust",
    mood="futility",
    extra="dust slipping from hands",
)
S[(9, 13)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="great souls with undistracted minds bowing to Krishna, knowing him as the imperishable source — devoted circle",
    mood="the great souls",
    extra="circle of undistracted devotees",
)
S[(9, 14)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="devotees always praising, firm in vows, bowing with devotion — small group in steady rhythm of worship",
    mood="constant devotion",
    extra="rhythmic devotion composition",
)
S[(9, 15)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="others worship Krishna as the One, as distinct, as the many, facing everywhere — a mandala of forms around him",
    mood="many ways of worship",
    extra="mandala of forms",
)
S[(9, 16)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna as ritual, sacrifice, ancestral offering, herb, mantra (as sound-rings), butter, fire, offering-act — composite emblem",
    mood="the many roles of the divine in ritual",
    extra="composite ritual emblem",
)
S[(9, 17)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna as father, mother, sustainer, grandfather — depicted as four gentle emanating silhouettes around his form",
    mood="the universal parent",
    extra="four emanations",
)
S[(9, 18)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna as goal, shelter, witness, friend, seed — a composite emblem with small symbols around his heart",
    mood="the refuge of all",
    extra="composite refuge emblem",
)
S[(9, 19)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna gives heat and holds back rain — depicted as a sun above and rain-clouds gathered in his hand",
    mood="regulator of seasons",
    extra="sun and cloud motif",
)
S[(9, 20)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="knowers of three Vedas drinking ritual soma, attaining a heavenly palace briefly — ornate but ephemeral",
    mood="the heavenly reward",
    extra="ornate ephemeral heaven",
)
S[(9, 21)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the same figures falling back to the mortal world when merit runs out — falling-figures motif from a disappearing palace",
    mood="the limit of heaven",
    extra="falling figures beneath fading palace",
)
S[(9, 22)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="for single-minded devotees, Krishna personally supplies what they lack — a gentle hand carrying a cloth-bundle to a sincere devotee",
    mood="personal care",
    extra="hand offering provision",
)
S[(9, 23)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="worshippers of other deities still approach Krishna indirectly — their offerings subtly flowing toward him from distant shrines",
    mood="indirect worship",
    extra="flowing light to Krishna from far shrines",
)
S[(9, 24)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna alone is the receiver and Lord of all sacrifices — many altars converging to a single radiant figure",
    mood="sole receiver",
    extra="many altars, single receiver",
)
S[(9, 25)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="worshippers of gods reach gods, of ancestors reach ancestors, of spirits reach spirits, of Krishna reach Krishna — four distinct destinations",
    mood="you reach what you worship",
    extra="four panels of destination",
)
S[(9, 26)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a simple devotee offers a leaf, a flower, a fruit, water — Krishna accepts with a gentle welcoming hand",
    mood="simplest offering accepted",
    extra="four humble offerings and gentle hand",
)
S[(9, 27)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="everything depicted as offered — a figure's actions, meals, studies all rising as gentle light toward Krishna",
    mood="all as offering",
    extra="rising light of daily life",
)
S[(9, 28)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="chains of karma falling away as actions are offered; the devotee freed, coming to Krishna",
    mood="freed by offering",
    extra="falling chain links",
)
S[(9, 29)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna the same in all beings; devotees inside his aura, him inside theirs — mutual indwelling motif",
    mood="mutual indwelling",
    extra="interlocking aura motif",
)
S[(9, 30)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="even the worst sinner, turning with undivided devotion, becomes righteous — a once-shadowed figure now bright in Krishna's light",
    mood="redemption",
    extra="before-and-after figure",
)
S[(9, 31)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the same figure now at lasting peace; Krishna vows: my devotee never perishes",
    mood="the promise",
    extra="peaceful figure, Krishna's steady gaze",
)
S[(9, 32)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a widow, a merchant, a laborer, and humble folk — all taking refuge, reaching the supreme goal; Krishna welcoming all",
    mood="the path open to all",
    extra="varied figures welcomed",
)
S[(9, 33)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="even brahmins and royal sages welcomed into this worship — two elders stepping forward to join",
    mood="all the more for the learned",
    extra="two dignified elders approaching",
)
S[(9, 34)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna's four instructions depicted as four small emblems around Arjuna: mind fixed, devotion, offering, bowing down",
    mood="the fourfold practice",
    extra="four simple emblems",
)


# ============================================================================
# CHAPTER 10 — Divine Glories (42 verses)
# Each vibhuti is a specific manifestation — a chance for unique imagery.
# ============================================================================

S[(10, 1)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna speaks again, warmth in his voice — a gentle, private tone for a beloved",
    mood="loving address",
    extra="close composition",
)
S[(10, 2)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="gods and great sages depicted in the clouds, unable to fully know Krishna — they turn toward his light",
    mood="beyond the knowledge of the high",
    extra="gods and sages in upper clouds",
)
S[(10, 3)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a serene devotee free from sins, recognizing Krishna as unborn, without beginning — a small broken chain at his feet",
    mood="freed by recognition",
    extra="broken chain-motif",
)
S[(10, 4)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a composite emblem: small symbols of discernment, knowledge, patience, truth, self-control, calm around Krishna",
    mood="virtues arising from Him",
    extra="symbolic virtue-emblems",
)
S[(10, 5)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="additional virtues — non-violence, contentment, austerity, charity, fame — as further emblems completing the ring",
    mood="completing the virtues",
    extra="second ring of emblems",
)
S[(10, 6)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="seven great sages and four ancient Manus depicted in a high cloud council, born of Krishna's mind",
    mood="ancestors of humanity",
    extra="cloud council",
)
S[(10, 7)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a devotee grasping both glory and yoga — depicted with a bright steady flame in each hand, unified",
    mood="anchored in unshakable yoga",
    extra="two-flamed figure",
)
S[(10, 8)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="wise figures clustered around Krishna, offering devotion, recognizing him as the source of all",
    mood="the wise worship",
    extra="cluster of devotees",
)
S[(10, 9)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="devotees enlightening one another with soft beams of mutual light, always speaking of Krishna",
    mood="fellowship of devotees",
    extra="mutual beams",
)
S[(10, 10)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna gives inner discernment — a small lamp placed gently in a devotee's chest",
    mood="the gift of discernment",
    extra="heart-lamp being placed",
)
S[(10, 11)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="darkness of ignorance dispelled by a bright lamp kindled in the heart — figure transformed",
    mood="darkness lifted",
    extra="heart-lamp dispelling dark",
)
S[(10, 12)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna speaks reverently, hands folded — 'you are the supreme Brahman, supreme abode, supreme purifier'",
    mood="devotee's acknowledgment",
    extra="folded hands and soft awe",
)
S[(10, 13)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sages named — Narada, Asita, Devala, Vyasa — as faint figures affirming in the clouds",
    mood="tradition's witness",
    extra="small affirming sages",
)
S[(10, 14)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna accepts Krishna's words as true; gods and demons depicted distantly unable to fully know him",
    mood="accepting the truth",
    extra="distant gods and asuras",
)
S[(10, 15)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna as source of beings, Lord of beings, God of gods, Lord of the world — cosmic light rings behind him",
    mood="knower of Himself by Himself",
    extra="cosmic light rings",
)
S[(10, 16)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna asks Krishna to detail his divine glories — a small mandala unfolding between them",
    mood="request for the vibhutis",
    extra="unfolding mandala",
)
S[(10, 17)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="how to meditate on Krishna? — a contemplation-stance, soft light centered between them",
    mood="the question of meditation",
    extra="centered light",
)
S[(10, 18)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna drinks in nectar-like words — his face lit with thirst, hands cupped as if catching rain",
    mood="unquenchable thirst for the teaching",
    extra="cupped-hand motif",
)
S[(10, 19)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna prepares to name the principal glories — small gallery of faint symbols about to be named",
    mood="gallery opening",
    extra="faint gallery of emblems",
)
S[(10, 20)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna as the Self in the hearts of all beings — tiny heart-Krishna's in every nearby figure",
    mood="the indwelling Self",
    extra="tiny heart-Krishna motif in each figure",
)
S[(10, 21)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="vibhuti: Vishnu among the Adityas (sun-gods); the radiant sun; Marichi among the Maruts; the moon of the stars — four celestial icons",
    mood="celestial manifestations",
    extra="sun, moon, storm-wind, luminary glyphs",
)
S[(10, 22)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="vibhuti: the Sama Veda among Vedas; Indra among gods; mind among senses; consciousness in beings — paired symbols",
    mood="scripture and mind",
    extra="four emblems",
)
S[(10, 23)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="vibhuti: Shiva (Shankara) among Rudras; Kubera among yakshas; Fire among Vasus; Mount Meru among mountains — four emblems",
    mood="divine principals",
    extra="four emblems with a central Meru outline",
)
S[(10, 24)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="vibhuti: Brihaspati as chief priest; Skanda the warrior-general; the ocean among waters — three emblems",
    mood="leaders of their kinds",
    extra="three emblems",
)
S[(10, 25)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="vibhuti: Bhrigu among sages; Om among sounds (sound-rings, no text); silent japa among sacrifices; the Himalayas among immovables",
    mood="quiet supremes",
    extra="sage, sound-rings, beads, Himalayas outline",
)
S[(10, 26)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="vibhuti: the ashvattha tree; Narada among divine sages; Chitraratha among gandharvas; sage Kapila — four emblems",
    mood="wise choices",
    extra="four emblems including a tree",
)
S[(10, 27)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="vibhuti: Ucchaishravas among horses; Airavata among elephants; king among humans — three regal icons",
    mood="royal manifestations",
    extra="three regal symbols",
)
S[(10, 28)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="vibhuti: thunderbolt among weapons; Kamadhenu among cows; Kandarpa among those who beget; Vasuki among serpents — four emblems",
    mood="generative forces",
    extra="four emblems",
)
S[(10, 29)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="vibhuti: Ananta among nagas; Varuna among water beings; Aryaman among ancestors; Yama among rulers — four emblems",
    mood="subtle domains",
    extra="four emblems",
)
S[(10, 30)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="vibhuti: Prahlada among demons; Time among counters; the lion among beasts; Garuda among birds — four emblems",
    mood="moral leaders and swift ones",
    extra="four emblems",
)
S[(10, 31)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="vibhuti: wind among purifiers; Rama among warriors; makara among fish; Ganga among rivers — four emblems",
    mood="moving forces",
    extra="four emblems with a river motif",
)
S[(10, 32)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="vibhuti: the beginning, end, and middle of creations; the self-knowledge among sciences; the debate among disputants",
    mood="structure and culmination",
    extra="three-phase diagram plus a small symposium",
)
S[(10, 33)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="vibhuti: the letter A among letters (a single luminous glyph — not text); the dvandva compound; imperishable Time; the many-faced Creator",
    mood="structural primacy",
    extra="single radiant vowel-glyph, decorative",
)
S[(10, 34)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="vibhuti: all-devouring death; origin of the yet-to-come; feminine virtues fame, fortune, speech, memory, intelligence, steadiness, forgiveness — emblems",
    mood="death and virtues",
    extra="emblem ring",
)
S[(10, 35)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="vibhuti: Brihat-saman among hymns (sound-rings); Gayatri among meters; Margashirsha month; flowering spring — seasonal motif",
    mood="the flowering of time",
    extra="flowering spring backdrop",
)
S[(10, 36)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="vibhuti: gambling of cheats; splendor of the splendid; victory; determination; goodness of the good — a mix of light and dark",
    mood="inside the mixture of life",
    extra="symbolic mixed emblems",
)
S[(10, 37)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="vibhuti: Vasudeva (Krishna himself) among the Vrishnis; Arjuna among the Pandavas; Vyasa among sages; Ushanas among poets",
    mood="meta-reference",
    extra="subtle self-reference motif",
)
S[(10, 38)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="vibhuti: rod among chastisers; statecraft among victory-seekers; silence among secrets; wisdom of the wise — four emblems",
    mood="sovereignty and silence",
    extra="four emblems",
)
S[(10, 39)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="whatever is the seed of any being — that is Krishna; a universal seed motif at the center of the composition",
    mood="seed of all",
    extra="radiant universal seed",
)
S[(10, 40)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna indicates the list is a small sample of vast magnificence — a soft gallery of emblems fading off into infinity",
    mood="endless glory",
    extra="emblems receding in perspective",
)
S[(10, 41)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="anything glorious, prosperous, or mighty depicted as a small spark rising from Krishna's larger flame",
    mood="sparks of His splendor",
    extra="many small sparks rising",
)
S[(10, 42)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna holds the universe on a single fingertip of light — a whole cosmos in miniature balanced there",
    mood="the universe on a fragment",
    extra="miniature cosmos on fingertip",
)


# ============================================================================
# CHAPTER 11 — The Vision of the Cosmic Form (55 verses)
# The theophany. Vishwarupa character sheet is used throughout.
# ============================================================================

S[(11, 1)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna's face clear, no more confusion — he acknowledges the supreme secret has dispelled his delusion",
    mood="confusion lifted",
    extra="soft gold clarity",
)
S[(11, 2)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna addresses Krishna by the epithet 'lotus-eyed' — faint lotus motif reflected in Krishna's eyes",
    mood="reverent address",
    extra="lotus reflection motif",
)
S[(11, 3)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna requests to see the lordly form — his face eager, hands folded",
    mood="the request",
    extra="eager yet reverent",
)
S[(11, 4)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna, hands folded, softly: if you think I can see it, show me the imperishable Self",
    mood="humble request for grace",
    extra="soft humble posture",
)
S[(11, 5)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna begins to reveal — early outlines of many forms appearing as faint multiple silhouettes around him",
    mood="the unveiling begins",
    extra="multiple emerging silhouettes",
)
S[(11, 6)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="in the sky, Adityas, Vasus, Rudras, Ashvins, Maruts begin to appear as distinct radiant figures",
    mood="divine hosts emerging",
    extra="radiant divine hosts emerging",
)
S[(11, 7)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the whole universe gathered into Krishna's body — moving and unmoving — beings and stars arranged within his outline",
    mood="universe within",
    extra="universe within outline",
)
S[(11, 8)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna gives Arjuna a divine eye — a new subtle eye of light rendered opening between Arjuna's brows",
    mood="the granting of divine sight",
    extra="divine-eye motif",
)
S[(11, 9)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna", "VishwaRupa"],
    action="the cosmic form of Krishna begins to fully manifest before Arjuna",
    mood="full theophany begins",
    extra="expanding cosmic presence",
)
S[(11, 10)] = dict(
    loc=CHARIOT,
    cast=["VishwaRupa"],
    action="the cosmic form with many mouths and eyes, divine ornaments, weapons uplifted in many hands",
    mood="vast armed divinity",
    extra="many-armed array",
)
S[(11, 11)] = dict(
    loc=CHARIOT,
    cast=["VishwaRupa"],
    action="garlanded and anointed with divine perfumes, faces on every side, infinitely radiant",
    mood="all-wonderful form",
    extra="radiant faces everywhere",
)
S[(11, 12)] = dict(
    loc=CHARIOT,
    cast=["VishwaRupa"],
    action="a splendor like a thousand suns bursting forth at once in the sky",
    mood="thousand-sun splendor",
    extra="blinding radiant burst",
)
S[(11, 13)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="Arjuna beholds the universe in all its divisions gathered in the body of the God of gods",
    mood="universe in the God",
    extra="universe-in-body motif",
)
S[(11, 14)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="Arjuna, astonished, hair on end, bowing with folded hands",
    mood="awestruck reverence",
    extra="trembling folded hands",
)
S[(11, 15)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="Arjuna sees all gods and beings, Brahma on a lotus, all sages, divine serpents — within the cosmic body",
    mood="all beings in Him",
    extra="cosmic congregation within",
)
S[(11, 16)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="Arjuna sees countless arms, bellies, mouths, eyes — no beginning or end — universal form",
    mood="endless form",
    extra="endless multiplicity",
)
S[(11, 17)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="crown, club, discus, blazing mass of brilliance on every side",
    mood="unbearable brilliance",
    extra="crown, club, discus prominent",
)
S[(11, 18)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="the cosmic form recognized as the Imperishable — the supreme resting place of the universe",
    mood="recognized as Imperishable",
    extra="universe at rest within Him",
)
S[(11, 19)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="no beginning, middle, or end; infinite power; countless arms; sun and moon as eyes; blazing fire mouth",
    mood="beyond measure",
    extra="sun/moon eyes, fire mouth",
)
S[(11, 20)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="the space between heaven and earth and all directions filled by Him alone; three worlds tremble",
    mood="three worlds trembling",
    extra="trembling worlds motif",
)
S[(11, 21)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="hosts of gods entering Him, some in fear, others praising with folded hands; sages crying 'may it be well'",
    mood="gods entering Him",
    extra="gods entering His form",
)
S[(11, 22)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="Rudras, Adityas, Vasus, Sadhyas, Vishvedevas, Ashvins, Maruts, ancestors, gandharvas, yakshas, asuras, siddhas — all gazing in wonder",
    mood="all classes of beings in wonder",
    extra="distinct classes represented as small figures",
)
S[(11, 23)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="the worlds tremble seeing His great form with many mouths, eyes, arms, thighs, bellies, tusks — Arjuna too trembles",
    mood="collective trembling",
    extra="visible tremor in the frame",
)
S[(11, 24)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="Arjuna, peering up at Him touching the sky, cannot find firmness — trembling, many colors blazing",
    mood="cannot find steadiness",
    extra="Arjuna unsteady",
)
S[(11, 25)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="the mouths fearsome with tusks, like the fires of cosmic dissolution; Arjuna losing his bearings",
    mood="devouring mouths",
    extra="fearsome tusked mouths",
)
S[(11, 26)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa", "Bhishma", "Drona", "Karna"],
    action=(
        "entire rivers of warriors — millions of soldiers, thousands of "
        "chariots, elephants and horses — all of the sons of Dhritarashtra, "
        "hosts of kings, Bhishma, Drona, Karna, and chief warriors streaming "
        "in endless currents into the flaming mouths of the cosmic form"
    ),
    mood="millions rushing to their fate",
    extra="streams of tiny warriors flowing upward into the mouths",
)
S[(11, 27)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action=(
        "waves of armored warriors hurrying into vast mouths fearsome with "
        "tusks; countless caught between them, helmets and chariots "
        "shattered to dust — the annihilation of whole armies"
    ),
    mood="annihilation of armies",
    extra="shattered helms, broken chariots, dust of hosts",
)
S[(11, 28)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action=(
        "many torrents of mighty rivers rushing into the ocean — so the "
        "heroes of the world of men rush in their millions into the flaming "
        "mouths of Time"
    ),
    mood="river-torrent simile on epic scale",
    extra="rivers of warriors flowing into a vast ocean of mouths",
)
S[(11, 29)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action=(
        "countless moths rushing headlong into a cosmic blazing fire — "
        "creatures in their millions into the mouths — their own destruction"
    ),
    mood="moth-flame simile at cosmic scale",
    extra="vast swarms of figures consumed by cosmic fire",
)
S[(11, 30)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action=(
        "whole worlds — entire armies, kingdoms, planets — swallowed and "
        "licked up by the flaming mouths; fierce cosmic rays scorch the "
        "universe itself"
    ),
    mood="cosmic devouring of worlds",
    extra="planets and armies being consumed, universe-scale flames",
)
S[(11, 31)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="Arjuna, pleading: 'tell me who you are' — the primal one; bows in reverence, hands folded",
    mood="seeking identity",
    extra="bowed supplication",
)
S[(11, 32)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="Krishna's answer through the cosmic form: 'I am Time, destroyer of worlds' — sand-glass imagery subtly in the background",
    mood="I am Time",
    extra="vast cosmic hourglass motif",
)
S[(11, 33)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="Arjuna called to be the outward cause — warriors already slain by Time depicted as faint outlines fallen already",
    mood="already slain by Time",
    extra="fallen outlines on the field",
)
S[(11, 34)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa", "Bhishma", "Drona", "Karna"],
    action="Drona, Bhishma, Jayadratha, Karna, others — already slain by the divine; Arjuna to fight without hesitation",
    mood="do not tremble — fight",
    extra="faint already-fallen heroes",
)
S[(11, 35)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="Arjuna, trembling, folds his hands, prostrates himself, stammers in fear",
    mood="reverent fear",
    extra="full prostration",
)
S[(11, 36)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="the world rejoices in His praise; demons flee in all directions; perfected beings bow in reverence",
    mood="universal praise",
    extra="fleeing demons, bowing siddhas",
)
S[(11, 37)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="why would they not bow? — greater than Brahma, infinite Lord of gods, refuge of worlds — supreme awe",
    mood="supreme awe",
    extra="Brahma small beneath Him",
)
S[(11, 38)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="the primal God, ancient Person, supreme resting place, knower and known — acknowledged as the all",
    mood="the all-pervading",
    extra="cosmic ring composition",
)
S[(11, 39)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="Vayu, Yama, Agni, Varuna, Moon, Prajapati, great ancestor — all as facets of His form, salutations in many directions",
    mood="facets saluted",
    extra="multi-directional salutation arcs",
)
S[(11, 40)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="salutations from front, back, and every side — four-direction bowing silhouettes around the cosmic form",
    mood="salutation from all directions",
    extra="four-direction bowing figures",
)
S[(11, 41)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="Arjuna confesses past familiarity — 'O Krishna,' 'O friend' — depicted as a small regretful gesture",
    mood="remorse for familiarity",
    extra="small regretful hand",
)
S[(11, 42)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="remorse for past jest — memories of friendly meals and play depicted as faint bright vignettes",
    mood="asking forgiveness",
    extra="faint friendly vignettes",
)
S[(11, 43)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="Krishna as father of the world, revered teacher — no one equal or greater; Arjuna bowed",
    mood="no equal, no greater",
    extra="father-teacher emblem",
)
S[(11, 44)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="Arjuna prostrating, begging grace — 'as father to son, friend to friend, lover to beloved — bear with me'",
    mood="intimate plea",
    extra="full prostration with folded hands",
)
S[(11, 45)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="Arjuna filled with joy and shaken with fear at once — asks to see the gentler form",
    mood="joy and fear together",
    extra="divided expression",
)
S[(11, 46)] = dict(
    loc=CHARIOT,
    cast=["Arjuna", "VishwaRupa"],
    action="asking to see the familiar four-armed form with crown, club, discus — soft transition beginning",
    mood="request to return",
    extra="four-armed form emerging from the cosmic",
)
S[(11, 47)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna's grace — the supreme form shown through yogic power; luminous, universal, primal — Arjuna alone has seen",
    mood="unique grace",
    extra="luminous afterglow",
)
S[(11, 48)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="no Veda, no sacrifice, no gift, no ritual, no austerity grants this sight — only grace",
    mood="grace alone grants",
    extra="small set of offerings faded, grace brighter",
)
S[(11, 49)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna gently calms Arjuna — 'don't be afraid' — returning to the beloved form",
    mood="comforting return",
    extra="calming hand gesture",
)
S[(11, 50)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna resumes his own gentle form; Arjuna's breath returns; the scene settles into familiar light",
    mood="restoration of the gentle form",
    extra="scene softening",
)
S[(11, 51)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna's thoughts calm, back to natural self — the two in quiet companionship once more",
    mood="the calm after",
    extra="natural composed framing",
)
S[(11, 52)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna: 'this form is very hard to see — even gods are eager to behold it'; faint gods gathered in the sky",
    mood="rarity of the vision",
    extra="faint gods in clouds",
)
S[(11, 53)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="no Veda, no austerity, no gift, no sacrifice can reveal this form — the four means depicted faintly crossed out by light",
    mood="beyond usual means",
    extra="four fading means",
)
S[(11, 54)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="by undivided devotion alone — a single steady flame depicted at Arjuna's heart",
    mood="devotion the only means",
    extra="single flame motif",
)
S[(11, 55)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="one who works for Krishna, holds him supreme, is devoted, unattached, without hostility — comes to him; Arjuna stands firm",
    mood="the summary of Bhakti Yoga",
    extra="composed devoted posture",
)


# ============================================================================
# CHAPTER 12 — The Way of Devotion (20 verses)
# ============================================================================

S[(12, 1)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna asks which is better — devotee of personal form or devotee of the unmanifest — hands holding two symbols in either palm",
    mood="which devotion is better?",
    extra="two-hand symbol comparison",
)
S[(12, 2)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna indicates devotees always yoked to him as the most deeply joined — a tight heart-to-heart thread between them",
    mood="deeply joined",
    extra="heart-thread motif",
)
S[(12, 3)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="worshippers of the Imperishable — indefinable, unmanifest, unchanging — shown meditating before an abstract radiant geometry",
    mood="worship of the abstract",
    extra="abstract radiant geometry",
)
S[(12, 4)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="those worshippers: senses controlled, even-minded, delighting in all beings' welfare — reach Him too",
    mood="also reach Him",
    extra="serene meditators",
)
S[(12, 5)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="but their path is harder — depicted as a steeper climb toward an indistinct summit",
    mood="the harder climb",
    extra="steep fog-climb",
)
S[(12, 6)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="those who surrender all actions to Krishna and worship with undivided yoga — Krishna rescues them from the ocean of samsara",
    mood="the rescuer",
    extra="hand reaching to pull a figure from a dark sea",
)
S[(12, 7)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a rescued figure lifted fully into Krishna's light — safely out of the ocean of death and rebirth",
    mood="safely rescued",
    extra="figure lifted into light",
)
S[(12, 8)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna's mind fixed on Krishna alone — two minds depicted as one flame merging into Krishna",
    mood="mind resting in Him",
    extra="two flames merging",
)
S[(12, 9)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="if not fixed, reach by practice — a figure practicing small repeated movements (gestures, breaths)",
    mood="reach by practice",
    extra="practice-motif sequence",
)
S[(12, 10)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="if not practice, work for Krishna — a figure engaged in everyday labor offering it upward",
    mood="work as devotion",
    extra="offered-labor motif",
)
S[(12, 11)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="if not even that, give up the fruits of action — a figure releasing a symbolic fruit upward",
    mood="release of fruits",
    extra="fruit floating upward",
)
S[(12, 12)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a gradient: knowledge > practice > meditation > renunciation-of-fruit > peace — a rising staircase",
    mood="ascending hierarchy",
    extra="rising staircase motif",
)
S[(12, 13)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a devotee who hates no creature — gently surrounded by small animals and people who aren't afraid to approach",
    mood="friendly and compassionate",
    extra="small creatures comfortably near",
)
S[(12, 14)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="always content, yoked, self-controlled, firm, with mind and intellect offered to Krishna — offered-flame motif to Krishna",
    mood="offering of mind and intellect",
    extra="twin offered flames",
)
S[(12, 15)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a figure who neither disturbs nor is disturbed — standing steady as a calm crowd passes around without disturbance",
    mood="non-disturbing presence",
    extra="calm crowd passing",
)
S[(12, 16)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a simple, skilled, detached figure with open empty hands — content, renouncing all undertakings",
    mood="simple, skilled, untroubled",
    extra="open empty hands",
)
S[(12, 17)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="one who neither rejoices nor hates, neither grieves nor desires — renounces both good and evil — soft balanced face",
    mood="beyond good and evil",
    extra="balanced face",
)
S[(12, 18)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the same toward enemy and friend, honor and dishonor, cold and heat, pleasure and pain — four balanced pairs",
    mood="same in opposites",
    extra="four balanced pairs",
)
S[(12, 19)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the same in blame and praise, silent, content, homeless, steady — a traveler with a walking stick and a gentle smile",
    mood="the wandering devotee",
    extra="traveler with stick",
)
S[(12, 20)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="devotees following this nectar-of-dharma with faith — dearly beloved by Krishna; heart-to-heart light shared",
    mood="the dearest devotees",
    extra="shared heart-light",
)


# ============================================================================
# CHAPTER 13 — The Body and the One Who Knows It (35 verses)
# ============================================================================

S[(13, 1)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna asks about prakriti, purusha, field and knower — rendered as four small glyphs floating between them",
    mood="inquiry into distinctions",
    extra="four glyph motifs",
)
S[(13, 2)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna outlines the body as 'the field' — body outline with a small witness-flame inside it",
    mood="defining the field",
    extra="body-outline with inner flame",
)
S[(13, 3)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna points to himself and to every being — same knower in every field; small light in each figure",
    mood="same knower everywhere",
    extra="light in each figure",
)
S[(13, 4)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna indicates the field's components, changes, and origin — a diagram-like composition behind them",
    mood="brief overview",
    extra="faint diagrammatic backdrop",
)
S[(13, 5)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sages of old depicted as a cloud-row singing this in hymns; a book of light between the figures",
    mood="the sages' testimony",
    extra="cloud-row of sages",
)
S[(13, 6)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="diagram of the field's components — five elements, ego, intellect, unmanifest, ten senses + mind, five sense-fields — as a mandala",
    mood="constituents of the field",
    extra="mandala of components",
)
S[(13, 7)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="changes of the field: desire, aversion, pleasure, pain, body, intelligence, steadiness — as small emblems",
    mood="changes and modifications",
    extra="small emblem-row",
)
S[(13, 8)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="marks of knowledge begin: humility, honesty, non-violence, patience, uprightness — quiet symbolic emblems",
    mood="the marks of wisdom",
    extra="row of simple virtue emblems",
)
S[(13, 9)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="lack of interest in sense objects; absence of ego; insight into suffering — faded objects, shrinking ego-bubble",
    mood="detachment and insight",
    extra="shrinking ego-bubble",
)
S[(13, 10)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="non-attachment to home and family — a figure walking forward, hands open; home faintly behind, without a tether",
    mood="non-identification",
    extra="home in soft background",
)
S[(13, 11)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="unswerving devotion to Krishna; solitude preferred — a still small hermitage far off",
    mood="devotion and solitude",
    extra="small hermitage",
)
S[(13, 12)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="steadiness in self-knowledge; insight into the goal — a luminous upward arrow",
    mood="the whole of knowledge",
    extra="upward luminous arrow",
)
S[(13, 13)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the supreme to be known — beginningless Brahman depicted as a soft shimmering halo with no edges",
    mood="pointing to Brahman",
    extra="edgeless halo",
)
S[(13, 14)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Brahman with hands, feet, eyes, heads, ears on all sides — depicted as a radiant mandala of many small limbs and eyes",
    mood="everywhere-presence",
    extra="many-limbed mandala (abstract not monstrous)",
)
S[(13, 15)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Brahman appears to have qualities but is free of them — experiencer of the gunas yet beyond them",
    mood="paradox of Brahman",
    extra="halo around three quiet colored currents",
)
S[(13, 16)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="inside and outside all beings, moving and unmoving — rendered as soft light permeating every figure",
    mood="permeating presence",
    extra="soft permeating light",
)
S[(13, 17)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="undivided yet seeming divided — many figures each holding a piece of the same golden mirror",
    mood="one appearing many",
    extra="shared golden mirror motif",
)
S[(13, 18)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="light of lights beyond darkness — a lantern held high illuminating a dark landscape",
    mood="illumination",
    extra="high lantern motif",
)
S[(13, 19)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna summarizes — field, knowledge, knowable — three small medallions between them",
    mood="brief summary",
    extra="three medallions",
)
S[(13, 20)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="prakriti and purusha without beginning — two paired circles, one active one still, depicted side by side",
    mood="the pair beginningless",
    extra="two concentric circles",
)
S[(13, 21)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="prakriti the cause in bodily action; purusha the cause of experience — two arrows meeting at a figure",
    mood="division of causation",
    extra="meeting arrows",
)
S[(13, 22)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="purusha seated in prakriti experiences the gunas — small figure inside a three-colored swirl",
    mood="attachment to gunas",
    extra="figure within swirl",
)
S[(13, 23)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="supreme Purusha as spectator, permitter, sustainer — a vast serene face above the small inner figure",
    mood="the witness Lord",
    extra="serene above, small below",
)
S[(13, 24)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="one who understands is not reborn — a figure stepping outside a fading wheel",
    mood="not born again",
    extra="fading wheel behind",
)
S[(13, 25)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="three paths to the Self: meditation, analytic knowledge, and action — three small emblems",
    mood="three paths",
    extra="three emblems",
)
S[(13, 26)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="others, not knowing, worship as they have heard — still cross beyond death; humble line of listeners",
    mood="the power of hearing",
    extra="line of listeners",
)
S[(13, 27)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="whatever is born arises from the union of field and knower — two lines meeting at a figure",
    mood="birth from the union",
    extra="meeting-lines composition",
)
S[(13, 28)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the supreme Lord dwells equally in all — same small inner flame in every figure nearby",
    mood="imperishable within perishing",
    extra="same inner flame motif",
)
S[(13, 29)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="seeing the same Lord everywhere, one does not destroy oneself — a protective inner arc",
    mood="protected by equal vision",
    extra="protective arc motif",
)
S[(13, 30)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="all action done by nature alone; the Self is not the doer — a figure still in the middle of a busy landscape",
    mood="still amid busyness",
    extra="still center in activity",
)
S[(13, 31)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="all beings resting in the One and expanding from It — a central sun with beings as rays",
    mood="one expanding into many",
    extra="sun with rays as beings",
)
S[(13, 32)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the imperishable Self without beginning, without qualities — neither acts nor is stained — in a body of clay",
    mood="unstained Self",
    extra="clay body with still light inside",
)
S[(13, 33)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="space not stained by what it contains — a clear sky with clouds, lightning, and rain; the sky remains",
    mood="space-unstained analogy",
    extra="clear sky analogy",
)
S[(13, 34)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="as one sun lights the world, the knower lights the whole field — a sun rising over a varied landscape",
    mood="sun-knower metaphor",
    extra="rising sun over landscape",
)
S[(13, 35)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="those with the eye of knowledge see the distinction and reach the Supreme — a luminous gate opening",
    mood="arrival at the Supreme",
    extra="luminous gate",
)


# ============================================================================
# CHAPTER 14 — The Three Qualities of Nature (27 verses)
# ============================================================================

S[(14, 1)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna introduces the supreme knowledge again — a scroll of light unfurled between them",
    mood="supreme knowledge revisited",
    extra="scroll of light",
)
S[(14, 2)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sages of old reached this knowledge and became like Krishna — small row of sages merging into Krishna's aura",
    mood="union with the divine",
    extra="sages merging into aura",
)
S[(14, 3)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Brahman depicted as a great womb; Krishna plants a seed of light; all beings are born of the union",
    mood="cosmic conception",
    extra="womb-and-seed motif, symbolic",
)
S[(14, 4)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="whatever forms come from any womb, Brahman is the womb and Krishna is the seed-giving father — emblematic diagram",
    mood="universal parentage",
    extra="emblem of womb-and-seed",
)
S[(14, 5)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="three-colored threads — white (sattva), red (rajas), black (tamas) — tying a figure to a body",
    mood="the binding gunas",
    extra="three-thread binding",
)
S[(14, 6)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sattva: pure illuminating, binding by attachment to happiness and knowledge — a figure bathed in white light, gently held by white thread",
    mood="pure binding",
    extra="white-thread and halo",
)
S[(14, 7)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="rajas: thirst and attachment; binds by attachment to action — a figure busy in red-tinted motion",
    mood="restless binding",
    extra="red-threaded motion",
)
S[(14, 8)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="tamas: ignorance; binds by carelessness, laziness, sleep — a drowsy figure in dim indigo light",
    mood="dim binding",
    extra="indigo dim light",
)
S[(14, 9)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="three figures side by side: happiness (white), action (red), heedlessness (indigo) — the three gunas in effect",
    mood="three effects",
    extra="three contrasted figures",
)
S[(14, 10)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the three gunas take turns rising — depicted as a three-phase cycle around a single figure",
    mood="alternation",
    extra="three-phase cycle",
)
S[(14, 11)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="when sattva dominates, light streams out through all the gates of the body — body-outline with soft light at every gate",
    mood="sattva dominant",
    extra="light-at-gates motif",
)
S[(14, 12)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="when rajas dominates: greed, activity, undertakings, restlessness, craving — a figure in feverish motion",
    mood="rajas dominant",
    extra="motion-lines",
)
S[(14, 13)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="when tamas dominates: darkness, inactivity, heedlessness, confusion — a slumped dim figure",
    mood="tamas dominant",
    extra="slumped dim figure",
)
S[(14, 14)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="dying in sattva: reaches pure worlds of knowers — ascending bright path",
    mood="death in sattva",
    extra="ascending path",
)
S[(14, 15)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="dying in rajas: reborn among the active; in tamas: in dull wombs — two contrasting paths",
    mood="divergent rebirths",
    extra="two paths",
)
S[(14, 16)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="fruits of good action: pure (white); rajas → pain; tamas → ignorance — three small fruits shown in three colors",
    mood="fruits colored",
    extra="three colored fruits",
)
S[(14, 17)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="from sattva → knowledge; rajas → greed; tamas → heedlessness — three branching arrows",
    mood="what each produces",
    extra="branching arrows",
)
S[(14, 18)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sattva rises upward; rajas stays in middle; tamas sinks down — three figures in three vertical positions",
    mood="three levels",
    extra="vertical-stack composition",
)
S[(14, 19)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="seeing no agent beyond the gunas, one steps out of their sway — a figure stepping past a three-colored swirl",
    mood="beyond the gunas",
    extra="stepping-past motif",
)
S[(14, 20)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="transcending the gunas, freed from birth, death, old age, pain — arrives at immortality; a radiant upward figure",
    mood="immortality",
    extra="radiant upward figure",
)
S[(14, 21)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna asks: what are the marks of such a person? — hands raised in question",
    mood="the question of marks",
    extra="question gesture",
)
S[(14, 22)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a gunatita figure watching illumination, activity, and confusion arise and pass — three ripples around a still face",
    mood="neither hates nor longs",
    extra="three ripples, still face",
)
S[(14, 23)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sitting as if indifferent, unmoved by the gunas — a still meditator watching currents pass",
    mood="unmoved witness",
    extra="still meditator over currents",
)
S[(14, 24)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="equal in pleasure and pain, treats clod-stone-gold the same; same to liked and disliked; same in praise and blame",
    mood="fully equal",
    extra="rows of balanced opposites",
)
S[(14, 25)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="same in honor and dishonor; same to friend and foe; giving up all undertakings — a calm centered figure",
    mood="fully centered",
    extra="centered calm figure",
)
S[(14, 26)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the devotee's unswerving yoga of devotion — a bright thread from heart to Krishna, transcending the gunas",
    mood="unswerving devotion",
    extra="heart-to-Krishna thread",
)
S[(14, 27)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna as the foundation of Brahman — immortal, imperishable, eternal dharma, absolute happiness — soft cosmic aura",
    mood="ground of Brahman",
    extra="cosmic aura",
)


# ============================================================================
# CHAPTER 15 — The Supreme Person (20 verses)
# ============================================================================

S[(15, 1)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the inverted sacred fig tree: roots above (rooted in Brahman), branches below (extending into the world) — symbolic tree",
    mood="the inverted cosmic tree",
    extra="inverted tree with leaves as hymn-leaves",
)
S[(15, 2)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="branches fed by the three colored gunas; twigs as sense-objects — a detailed diagram of the tree",
    mood="tree-as-world diagram",
    extra="branches with sense-objects as leaves",
)
S[(15, 3)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a figure raising the axe of non-attachment to cut the ashvattha — decisive stroke about to fall",
    mood="cutting the tree",
    extra="axe of non-attachment",
)
S[(15, 4)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="having cut the tree, the figure seeks the primal Person beyond — a path opening upward into light",
    mood="seeking the primal Person",
    extra="opening path upward",
)
S[(15, 5)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="free from pride, delusion, attachment — desires withdrawn; the unconfused reaching the imperishable abode",
    mood="arrival at imperishable",
    extra="imperishable abode motif",
)
S[(15, 6)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="neither sun, moon, nor fire lights that place — self-luminous realm, soft interior glow without source",
    mood="self-luminous abode",
    extra="soft sourceless glow",
)
S[(15, 7)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a part of Krishna becomes a jiva in the living world, drawing mind and senses from nature — subtle emergence",
    mood="the jiva born",
    extra="small soul-figure drawing in senses",
)
S[(15, 8)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the Lord of the body takes up and leaves a body, carrying mind and senses — like wind carrying fragrance from flowers",
    mood="wind-and-fragrance metaphor",
    extra="wind-and-fragrance motif",
)
S[(15, 9)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="presiding over ear, eye, touch, taste, smell and the mind — small emblems of six senses around a central figure",
    mood="presiding over senses",
    extra="six-sense emblem ring",
)
S[(15, 10)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="confused see nothing, wise with the eye of knowledge see Him — two figures, one blind, one with a radiant inner eye",
    mood="two ways of seeing",
    extra="two contrasted figures",
)
S[(15, 11)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="striving yogis see Him within themselves — heart-Krishna motif in a meditator",
    mood="the yogi sees within",
    extra="heart-Krishna",
)
S[(15, 12)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the sun's radiance, moon's light, fire's brilliance — all Krishna's; the three emblems together",
    mood="light is His",
    extra="sun/moon/fire emblems",
)
S[(15, 13)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="entering the earth He sustains all; becoming the moon He nourishes plants — earth and moon emblem",
    mood="sustainer",
    extra="earth and moon emblem",
)
S[(15, 14)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="as the digestive fire in beings, joined with in- and out-breaths — a figure with a soft heart-fire digesting fourfold food",
    mood="the fire of digestion",
    extra="inner heart-fire",
)
S[(15, 15)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="seated in every heart; from Him come memory, knowledge, their loss — tiny heart-Krishna in each nearby figure",
    mood="the heart's seated Lord",
    extra="heart-Krishna motif",
)
S[(15, 16)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="two Persons: perishable (all beings) and imperishable (unchanging) — two distinct silhouettes side by side",
    mood="the two Persons",
    extra="two silhouettes",
)
S[(15, 17)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the supreme Person, higher still — a third figure above, entering the three worlds to sustain them",
    mood="the supreme Person",
    extra="third-figure-above motif",
)
S[(15, 18)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna as Purushottama — transcending perishable, above imperishable; a luminous crown of light above his head",
    mood="the Supreme Person",
    extra="crown of light",
)
S[(15, 19)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the undeluded devotee who knows Him — whole-being devotion; a figure glowing with offered totality",
    mood="total devotion",
    extra="whole-being offering",
)
S[(15, 20)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna concludes: the secret teaching revealed, one becomes wise, all duties done — Arjuna steady and awake",
    mood="the secret revealed",
    extra="steady awake composition",
)


# ============================================================================
# CHAPTER 16 — Divine and Demonic Natures (24 verses)
# ============================================================================

S[(16, 1)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="divine qualities enumerated: fearlessness, purity, steadfastness, generosity, self-control — small virtue emblems rising from the ground",
    mood="divine qualities",
    extra="rising virtue emblems",
)
S[(16, 2)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="more virtues: non-violence, truth, absence of anger, renunciation, calm, compassion, freedom from greed — more emblems",
    mood="further virtues",
    extra="virtue-emblem continuation",
)
S[(16, 3)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="vigor, forgiveness, strength, purity, absence of arrogance — marks of one born with divine qualities",
    mood="marks of the divine",
    extra="final virtue emblems",
)
S[(16, 4)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="demonic qualities: showiness, arrogance, self-importance, anger, harshness, ignorance — dark emblems",
    mood="marks of the demonic",
    extra="dark emblems",
)
S[(16, 5)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="divine qualities lead to liberation (bright upward path); demonic to bondage (dark chain) — two paths",
    mood="two outcomes",
    extra="two contrasting paths",
)
S[(16, 6)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="two kinds of beings — bright divine and dark demonic — as two distant hosts on either side",
    mood="two kinds of beings",
    extra="two hosts",
)
S[(16, 7)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="demonic people confused about what to do — a figure reaching both for a virtuous act and a harmful one, unable to decide",
    mood="moral disorder",
    extra="ambivalent reaching hands",
)
S[(16, 8)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="nihilists declaring no truth, no God — a world depicted as collapsing puzzle pieces behind them",
    mood="nihilism",
    extra="collapsing puzzle pieces",
)
S[(16, 9)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="lost souls of cruel deeds arising as enemies of the world — dark silhouettes destroying a small village model",
    mood="destroyers arising",
    extra="destructive silhouettes",
)
S[(16, 10)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="demonic people clinging to insatiable lust, hypocrisy, pride — a hoarding figure on a pile of gold, crown askew",
    mood="hoarding pride",
    extra="hoarding figure",
)
S[(16, 11)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="consumed by endless worries to the last breath — a figure at death still calculating on his fingers",
    mood="dying calculating",
    extra="calculating-at-death motif",
)
S[(16, 12)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="bound by hundreds of expectations; given to lust and anger; amassing wealth unjustly — chains of expectation visible",
    mood="chains of expectation",
    extra="many faint chains",
)
S[(16, 13)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="'this I've got; this desire I'll fulfill' — a figure gripping a handful of coins, imagining more",
    mood="greedy fantasizing",
    extra="gripping coins, imagining more",
)
S[(16, 14)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="'that enemy I've killed' — a haughty figure standing on a fallen silhouette",
    mood="triumphal arrogance",
    extra="haughty stance",
)
S[(16, 15)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="'I am rich and well-born' — a figure holding a crown above his own head, imagined audience behind",
    mood="self-elevation",
    extra="self-crowning motif",
)
S[(16, 16)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="scattered by anxieties, caught in a net of delusion, falling into a foul hell — a net and a dark pit",
    mood="falling into hell",
    extra="net and pit motif",
)
S[(16, 17)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="performing sacrifices in name only, for show — an ornate empty altar, a performing priest with a showy gesture",
    mood="hollow ritual",
    extra="empty ornate altar",
)
S[(16, 18)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="spiteful egotistic figures hating Krishna within others and themselves — dark figures with cracks of light they reject",
    mood="hating the light within",
    extra="inner light rejected",
)
S[(16, 19)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="hateful, cruel evildoers cast into demonic wombs — a descending dark spiral",
    mood="descent into darkness",
    extra="descending dark spiral",
)
S[(16, 20)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="confused through births, falling further — a figure sinking further with each loop of a descending chain",
    mood="successive falls",
    extra="descending chain of rebirth",
)
S[(16, 21)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="three gates of hell: lust, anger, greed — three dark doorways visibly marked with symbols",
    mood="three gates identified",
    extra="three dark doorways",
)
S[(16, 22)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="one freed from these three gates — a figure turning away from the doors toward the supreme goal",
    mood="turning away, moving toward",
    extra="turning toward light",
)
S[(16, 23)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="one acting on desire without scripture's guidance reaches neither perfection nor happiness — a figure lost in a featureless waste",
    mood="without guidance",
    extra="featureless waste",
)
S[(16, 24)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="scripture as guide — an open palm with a single radiant symbol for authority (no text), guiding action",
    mood="scripture as guide",
    extra="radiant authority symbol, non-textual",
)


# ============================================================================
# CHAPTER 17 — Three Kinds of Faith (28 verses)
# ============================================================================

S[(17, 1)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna asks about those who worship with faith but without scripture — a seeker with folded hands beside an unshaped altar",
    mood="what of such worshippers?",
    extra="unshaped altar",
)
S[(17, 2)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="three kinds of faith depicted as three small flames in white, red, and indigo",
    mood="three faiths",
    extra="three colored flames",
)
S[(17, 3)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="each person's faith matches their nature — a figure shaped by the flame beside them",
    mood="faith and nature",
    extra="figure-and-flame pairing",
)
S[(17, 4)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sattvic worship gods; rajasic worship yakshas/demons; tamasic worship ghosts — three distinct shrines",
    mood="targets of worship",
    extra="three contrasted shrines",
)
S[(17, 5)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="severe austerity not prescribed by scripture — a bound ascetic with forced hypocritical expression",
    mood="hypocritical austerity",
    extra="bound ascetic motif",
)
S[(17, 6)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="torturing the elements in the body and Krishna within — the same figure with inner light visibly pained",
    mood="tortured inner light",
    extra="inner pained flame",
)
S[(17, 7)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="food, sacrifice, austerity, gifts — four categories in three qualities each — composite frieze",
    mood="fourfold × threefold",
    extra="frieze layout",
)
S[(17, 8)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sattvic food: savory, nourishing — a plate of wholesome simple foods, warmly lit",
    mood="wholesome meal",
    extra="wholesome plate",
)
S[(17, 9)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="rajasic food: bitter, sour, hot, pungent, causing suffering — a fiery plate",
    mood="harsh meal",
    extra="fiery plate",
)
S[(17, 10)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="tamasic food: stale, decayed, leftover — a dimly lit cluttered plate, not appetizing",
    mood="spoiled meal",
    extra="dim cluttered plate",
)
S[(17, 11)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sattvic sacrifice: by the rule, no desire for fruit — a simple clean altar, quiet flame",
    mood="sincere offering",
    extra="simple clean altar",
)
S[(17, 12)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="rajasic sacrifice: for results or show — a flashy altar with spectators",
    mood="performative",
    extra="flashy altar",
)
S[(17, 13)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="tamasic sacrifice: rule-less, no food distributed, no faith — a broken disorderly altar",
    mood="broken rite",
    extra="disorderly altar",
)
S[(17, 14)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="austerity of the body: worship, purity, uprightness, celibacy, non-violence — composite body-frieze",
    mood="bodily austerity",
    extra="body-frieze",
)
S[(17, 15)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="austerity of speech: truthful, pleasant, beneficial; recitation of scriptures — a figure gently speaking",
    mood="austerity of speech",
    extra="open mouth in gentle speech",
)
S[(17, 16)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="austerity of the mind: serenity, gentleness, silence, self-control, purity — a centered serene figure",
    mood="austerity of mind",
    extra="centered serene figure",
)
S[(17, 17)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="threefold austerity practiced with supreme faith — a radiant yogi crowned with a soft halo",
    mood="sattvic austerity",
    extra="softly radiant yogi",
)
S[(17, 18)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="austerity for respect and honor — fleeting and unstable — a figure showing off for applause, applause fading",
    mood="rajasic austerity",
    extra="showing-off motif",
)
S[(17, 19)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="austerity out of foolishness or to harm others — a self-harming figure with a dark intent",
    mood="tamasic austerity",
    extra="self-harming motif",
)
S[(17, 20)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sattvic gift: given because it ought to be given; to the worthy, at the right place and time — a simple respectful gift",
    mood="sincere giving",
    extra="respectful gift",
)
S[(17, 21)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="rajasic gift: grudging, expecting return — a hand extending a gift with a string attached",
    mood="conditional giving",
    extra="string-attached gift",
)
S[(17, 22)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="tamasic gift: wrong place, wrong time, unworthy, without respect — a tossed gift to a retreating figure",
    mood="contemptuous giving",
    extra="tossed gift",
)
S[(17, 23)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="'Om Tat Sat' depicted as three concentric sound-mandalas (no text), framing the scene",
    mood="threefold designation",
    extra="three concentric sound-mandalas",
)
S[(17, 24)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sacrifice, gift, austerity begun with 'Om' — the first sound-mandala pulsing brightly at the beginning",
    mood="begun with Om",
    extra="pulsing first mandala",
)
S[(17, 25)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="with 'Tat' — acts performed without aim at fruit — a middle mandala steady and clear",
    mood="dedicated to That",
    extra="middle mandala clear",
)
S[(17, 26)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="with 'Sat' — in reality and goodness — the third mandala strong and bright; a wholesome gesture",
    mood="real and good",
    extra="third mandala bright",
)
S[(17, 27)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="steadiness in sacrifice, austerity, gift — also 'Sat' — three steady pillars depicted",
    mood="steady = Sat",
    extra="three pillars",
)
S[(17, 28)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="anything done without faith is called asat — nothing here, nothing hereafter — an offering dissolving into empty air",
    mood="the no-value of no-faith",
    extra="dissolving offering",
)


# ============================================================================
# CHAPTER 18 — Freedom Through Letting Go (78 verses)
# The summation. Ends with the final surrender verse (18.66), Arjuna's
# restored clarity, and Sanjaya's closing benediction.
# ============================================================================

S[(18, 1)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna asks about sannyasa (renunciation) and tyaga (letting go) — two glyphs floating side by side",
    mood="final distinctions sought",
    extra="two distinct glyphs",
)
S[(18, 2)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna separates the terms — one hand indicating giving up desire-driven action, the other indicating giving up fruits",
    mood="two definitions",
    extra="two distinct hand gestures",
)
S[(18, 3)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="some thinkers say abandon action; others say don't abandon sacrifice, gift, austerity — two debating groups faintly shown",
    mood="a debate among thinkers",
    extra="two debating groups",
)
S[(18, 4)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna announces his conclusion — tyaga is of three kinds — three small branches splitting",
    mood="Krishna's conclusion",
    extra="three branches motif",
)
S[(18, 5)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sacrifice, gift, austerity should be done — they purify — three bright emblems to keep",
    mood="to keep and do",
    extra="three bright emblems",
)
S[(18, 6)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="but done while letting go of attachment and fruits — Krishna's final opinion — a luminous upward gesture",
    mood="the final opinion",
    extra="upward gesture of release",
)
S[(18, 7)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="tamasic renunciation: giving up obligatory action from confusion — a figure shirking in a dim corner",
    mood="dull abandonment",
    extra="shirking figure in dim corner",
)
S[(18, 8)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="rajasic renunciation: abandoning action out of fear of bodily trouble — a figure turning away because it is hard",
    mood="fear-based abandonment",
    extra="turning-away from difficulty",
)
S[(18, 9)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sattvic renunciation: doing obligatory action while letting go of attachment and fruit — a calm figure doing the work",
    mood="the pure way",
    extra="calm worker",
)
S[(18, 10)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the sattvic renunciate doesn't hate unpleasant action nor cling to pleasant — equal hands on both kinds of tasks",
    mood="steady of intellect",
    extra="equal-handed posture",
)
S[(18, 11)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="an embodied being cannot fully give up action — but whoever releases the fruits is the true renouncer",
    mood="the true renouncer",
    extra="releasing-fruit gesture",
)
S[(18, 12)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="threefold fruit — undesired, desired, mixed — three small colored fruits; the true sannyasin has none of them clinging",
    mood="no fruit clinging",
    extra="three fruits drifting away",
)
S[(18, 13)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="five causes of action introduced — five small emblems appearing around the figure",
    mood="five causes",
    extra="five emblems appearing",
)
S[(18, 14)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="body, agent, instruments, activities, divine providence — five clearly distinct emblems labelled only by position",
    mood="the five components",
    extra="five distinct emblems",
)
S[(18, 15)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="any action of body, speech, or mind — all have these five — a small action-scene with five threads attached",
    mood="all actions have five causes",
    extra="five threads motif",
)
S[(18, 16)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="one who thinks only the Self is the agent, with untrained understanding, doesn't see — a confused figure",
    mood="incomplete sight",
    extra="confused figure",
)
S[(18, 17)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="one free from ego, intellect unstained — even if the outward act happens, they aren't really the doer",
    mood="unstained acting",
    extra="unbound peaceful figure",
)
S[(18, 18)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="three movers of action (knower, knowledge, known) and three components (instrument, action, agent) — two triangles",
    mood="structure of action",
    extra="two interlocking triangles",
)
S[(18, 19)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="knowledge, action, agent each of three kinds — a 3×3 small grid of tiny emblems",
    mood="3 × 3 taxonomy",
    extra="tiny 3×3 grid",
)
S[(18, 20)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sattvic knowledge: one imperishable Being in all — a field of many small identical flames",
    mood="one in all",
    extra="identical-flame field",
)
S[(18, 21)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="rajasic knowledge: many distinct entities — a field of many different colored flames",
    mood="many distinct",
    extra="many-colored flames",
)
S[(18, 22)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="tamasic knowledge: clinging to one trivial thing as the whole — a figure hugging a single small object",
    mood="clinging triviality",
    extra="hugging small object",
)
S[(18, 23)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sattvic action: obligatory, without attachment, without desire or hatred — a steady calm doer",
    mood="pure doing",
    extra="steady calm doer",
)
S[(18, 24)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="rajasic action: great effort, seeking fruits, impelled by ego — a straining over-muscled figure",
    mood="straining for results",
    extra="straining figure",
)
S[(18, 25)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="tamasic action: careless, disregarding consequences, loss, injury, ability — a reckless figure",
    mood="reckless action",
    extra="reckless figure",
)
S[(18, 26)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sattvic agent: free from attachment, firm, vigorous, unmoved by success or failure — a composed figure",
    mood="composed agent",
    extra="composed figure",
)
S[(18, 27)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="rajasic agent: passionate, result-seeking, greedy, impure, full of joy and sorrow — a turbulent figure",
    mood="turbulent agent",
    extra="turbulent figure",
)
S[(18, 28)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="tamasic agent: undisciplined, stubborn, deceitful, malicious, lazy, despondent, procrastinating — a slumped figure",
    mood="dull agent",
    extra="slumped figure",
)
S[(18, 29)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna introduces the threefold division of intellect and steadiness — two small emblems lighting up",
    mood="intellect and steadiness",
    extra="two emblems lighting",
)
S[(18, 30)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sattvic intellect: knows action and restraint, dharma and not-dharma, fear and fearlessness, bondage and liberation — a clear balanced set",
    mood="clear intellect",
    extra="balanced set of emblems",
)
S[(18, 31)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="rajasic intellect: mistakes dharma — a figure reading a mirrored or smudged emblem",
    mood="mistaken intellect",
    extra="smudged emblem",
)
S[(18, 32)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="tamasic intellect: takes adharma for dharma — an inverted emblem in darkness",
    mood="inverted intellect",
    extra="inverted emblem",
)
S[(18, 33)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sattvic steadiness: unswerving, through yoga, controls mind and senses — a firm standing figure",
    mood="firm steadiness",
    extra="firm figure",
)
S[(18, 34)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="rajasic steadiness: holds dharma, pleasure, wealth with attachment — a grasping figure",
    mood="attached steadiness",
    extra="grasping figure",
)
S[(18, 35)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="tamasic steadiness: holds on to sleep, fear, grief, depression, conceit — a drooping figure",
    mood="dull steadiness",
    extra="drooping figure",
)
S[(18, 36)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna introduces three kinds of happiness — three small flames side by side",
    mood="three kinds of happiness",
    extra="three flames",
)
S[(18, 37)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="sattvic happiness: poison at first, nectar at the end — a figure pushing through bitter to reach a sweet light",
    mood="delayed gratification of wisdom",
    extra="pass-through motif",
)
S[(18, 38)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="rajasic happiness: nectar first, poison in the end — a tempting fruit turning bitter in the figure's mouth",
    mood="turning to poison",
    extra="bitter-fruit motif",
)
S[(18, 39)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="tamasic happiness: confusing from start to end — a drowsy figure lost in fog",
    mood="fog of confusion",
    extra="drowsy in fog",
)
S[(18, 40)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="no being on earth or in heaven is free from the three qualities — gods and humans all touched by the three colors",
    mood="everywhere the three",
    extra="three-colored influence everywhere",
)
S[(18, 41)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the four varnas' natural duties distributed according to their nature — four figures by emblems: teacher, warrior, merchant, servant",
    mood="four natural duties",
    extra="four contrasted figures",
)
S[(18, 42)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="brahmin's duties: calm, self-control, austerity, purity, patience, uprightness, knowledge, realization, faith — emblems around a brahmin figure",
    mood="brahmin duties",
    extra="brahmin-emblem ring",
)
S[(18, 43)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="warrior's duties: valor, vigor, firmness, skill, not fleeing, generosity, leader's nature — emblems around Arjuna himself",
    mood="warrior duties",
    extra="warrior-emblem ring around Arjuna",
)
S[(18, 44)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="merchant's duties: farming, cattle-rearing, trade; servant's duty: service — two small working scenes in middle distance",
    mood="merchant and servant duties",
    extra="two working scenes",
)
S[(18, 45)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="a person reaches perfection through their own duty — a figure climbing a staircase of their own shape",
    mood="perfection through one's duty",
    extra="shaped-stair motif",
)
S[(18, 46)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="by worshipping through one's own work the One from whom all activity flows — a worker offering his work upward",
    mood="work as worship",
    extra="offered-work motif",
)
S[(18, 47)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="better one's own imperfect duty than another's perfect — two paths, one native (bright), one foreign (dim)",
    mood="own dharma first",
    extra="two paths motif",
)
S[(18, 48)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="every undertaking wrapped in some flaw — a fire wrapped in smoke, constant partial defilement accepted",
    mood="no perfect action",
    extra="fire-and-smoke motif",
)
S[(18, 49)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="with intellect unattached, self controlled, desire gone — attains supreme perfection of freedom from action",
    mood="final perfection",
    extra="serene figure, empty hands",
)
S[(18, 50)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna begins to describe the climb to Brahman — a small luminous staircase",
    mood="staircase to Brahman",
    extra="small luminous staircase",
)
S[(18, 51)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="pure intellect, firm self, letting go of sense objects, casting off attraction and aversion — four emblems dropped from the hand",
    mood="prerequisites",
    extra="four dropped emblems",
)
S[(18, 52)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="solitude, light eating, control of body, speech, mind, meditation, dispassion — a simple hermit-scene",
    mood="the hermit's way",
    extra="simple hermit-scene",
)
S[(18, 53)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="giving up ego, force, arrogance, desire, anger, possession — six symbols discarded; a peaceful figure emerges",
    mood="fit to become Brahman",
    extra="six discarded symbols",
)
S[(18, 54)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="having become Brahman, serene, neither grieving nor desiring — the same toward all — supreme devotion to Krishna",
    mood="supreme devotion",
    extra="serene figure, light reaching toward Krishna",
)
S[(18, 55)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="by devotion knowing Krishna truly, entering him — devotee's figure gently dissolving into Krishna's light",
    mood="entering into Him",
    extra="gentle dissolve into Krishna",
)
S[(18, 56)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="performing all actions, taking refuge in Krishna, reaching the eternal abode by his grace",
    mood="by His grace",
    extra="grace-arc over the devotee",
)
S[(18, 57)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="mentally surrendering all actions to Krishna, with him as highest goal — a figure offering actions as floating lights upward",
    mood="mental surrender",
    extra="floating offered lights",
)
S[(18, 58)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="with mind on Krishna, crossing all difficulties — a figure stepping lightly over symbolic obstacles",
    mood="crossing obstacles",
    extra="stepping-over motif",
)
S[(18, 59)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="clinging to ego 'I will not fight' — a small stubborn figure with arms crossed, nature still pulling at him",
    mood="ego's refusal",
    extra="arms-crossed stubborn figure",
)
S[(18, 60)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="bound by karma of his own nature, helplessly doing — his own nature as a gentle but inevitable hand on his back",
    mood="nature's gentle force",
    extra="hand-on-back motif",
)
S[(18, 61)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the Lord in the hearts of all beings, turning them as if on a machine — small figures mounted on a great gentle wheel",
    mood="the cosmic wheel",
    extra="small figures on a soft cosmic wheel",
)
S[(18, 62)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="take refuge in him with your whole being — Arjuna bowing with folded hands, light streaming into him",
    mood="wholehearted refuge",
    extra="light streaming into bowed figure",
)
S[(18, 63)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="'reflect on this fully, then do as you wish' — Krishna open-palmed, respecting Arjuna's freedom",
    mood="freedom honored",
    extra="open-palm gesture",
)
S[(18, 64)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="the supreme word, most secret of all — a small bright flame passed from Krishna's hand to Arjuna's",
    mood="the final secret",
    extra="flame passed hand to hand",
)
S[(18, 65)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="four essentials: fix mind, be devoted, offer, bow — four small emblems around Arjuna as Krishna promises he will come to him",
    mood="the promise",
    extra="four emblems, promise gesture",
)
S[(18, 66)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="THE culminating verse: Krishna with open arms — 'let go of all dharmas, take refuge in me alone; I will free you from all sins'",
    mood="the ultimate surrender",
    extra="open arms of welcome, soft cascading light",
)
S[(18, 67)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="don't share with the undisciplined or hostile — Krishna lifts a hand as if guarding the secret",
    mood="guarding the teaching",
    extra="guarding-hand gesture",
)
S[(18, 68)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="whoever teaches this to devotees performs supreme devotion — a teacher-figure passing the flame to a student",
    mood="passing the flame",
    extra="teacher-student flame passing",
)
S[(18, 69)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="no one does more precious service — no one will be more beloved — the teacher held especially close in Krishna's light",
    mood="most beloved",
    extra="closely held in light",
)
S[(18, 70)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="whoever studies this dialogue — worships Krishna by the sacrifice of knowledge — two readers side by side (no text visible on their scroll)",
    mood="study as sacrifice",
    extra="two readers with plain glowing scroll",
)
S[(18, 71)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="even the one who listens with faith attains the auspicious worlds of the meritorious — a listening pilgrim",
    mood="even listening avails",
    extra="listening pilgrim at a small gathering",
)
S[(18, 72)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Krishna asks: has your delusion been destroyed? — Arjuna raising his head, clear-eyed",
    mood="the question of resolution",
    extra="clear-eyed Arjuna",
)
S[(18, 73)] = dict(
    loc=CHARIOT,
    cast=["Krishna", "Arjuna"],
    action="Arjuna: 'my delusion is destroyed; I will do as you say' — bow and arrows taken up again with steady hands",
    mood="resolve restored",
    extra="bow taken up firmly",
)
S[(18, 74)] = dict(
    loc="the palace chamber of Hastinapura, mirroring Ch 1.1",
    cast=["Dhritarashtra", "Sanjaya"],
    action="Sanjaya, eyes closed, recounts to the king the wondrous dialogue he has heard — hair subtly standing on end",
    mood="reverential recounting",
    extra="back to the framing scene",
)
S[(18, 75)] = dict(
    loc="the palace chamber",
    cast=["Sanjaya"],
    action="Sanjaya, grateful for sage Vyasa's grace, holding his hand to his heart — having heard the supreme yoga directly",
    mood="gratitude",
    extra="hand to heart",
)
S[(18, 76)] = dict(
    loc="the palace chamber",
    cast=["Dhritarashtra", "Sanjaya"],
    action="Sanjaya rejoicing again and again as he recalls the dialogue between Krishna and Arjuna — soft radiant memory",
    mood="rejoicing in memory",
    extra="soft radiant memory-image of Krishna and Arjuna",
)
S[(18, 77)] = dict(
    loc="the palace chamber",
    cast=["Sanjaya"],
    action="Sanjaya recalls the wondrous cosmic form of Hari — a faint echo of the vishvarupa above him",
    mood="wonder at the cosmic form",
    extra="faint cosmic form echo",
)
S[(18, 78)] = dict(
    loc="the palace chamber opening into a sweeping vision of the chariot on the colossal Kurukshetra battlefield",
    cast=["Krishna", "Arjuna"],
    action=(
        "closing benediction: wherever Krishna — supreme Lord of yoga — and "
        "Arjuna — wielder of the Gandiva bow — stand together, there is "
        "fortune, victory, prosperity, sound policy; both in luminous golden "
        "silhouette on the chariot at the center of the vast battlefield, the "
        "millions of the two armies spread out behind them to the horizon as "
        "a distant golden memory"
    ),
    mood="final benediction over the greatest of wars",
    extra="golden silhouette of chariot centered on a vast horizon of massed armies, framed in gentle gold ornament",
)


def compose(cv: tuple[int, int], scene: dict) -> str:
    """Expand a compact scene into a full image-generation prompt."""
    parts = [STYLE]
    parts.append(f"Scene: {scene['loc']}.")
    if scene.get("cast"):
        parts.append(f"Characters present (render them consistently): {cast(*scene['cast'])}.")
    parts.append(f"Action: {scene['action']}.")
    if scene.get("extra"):
        parts.append(f"Details: {scene['extra']}.")
    parts.append(f"Mood: {scene['mood']}.")
    parts.append(CONSTRAINTS)
    return " ".join(parts)


def build():
    out = {
        "source_sanskrit": "bhagavad_gita_sanskrit.json",
        "notes": (
            "One image-generation prompt per verse of the Bhagavad Gita. "
            "Designed for character consistency across the series (each prompt "
            "inlines canonical descriptions of the figures it mentions) and a "
            "unified Neo-Ancient illustrated-manuscript style. Every prompt is "
            "constrained to square 1:1 aspect ratio and explicitly forbids any "
            "text, letters, or captions within the image."
        ),
        "style": STYLE,
        "constraints": CONSTRAINTS,
        "chapters": [],
    }

    for ch in src["chapters"]:
        cn = ch["chapter_number"]
        ch_out = {
            "chapter_number": cn,
            "chapter_title_sanskrit": ch["chapter_title_sanskrit"],
            "verses": [],
        }
        for v in ch["verses"]:
            vn = v["verse_number"]
            scene = S.get((cn, vn))
            prompt = compose((cn, vn), scene) if scene else None
            ch_out["verses"].append({
                "verse_number": vn,
                "prompt": prompt,
            })
        out["chapters"].append(ch_out)

    (ROOT / "bhagavad_gita_prompts.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2)
    )

    # Also write a FLAT list — one array of 701 objects, easier to browse and
    # to iterate when batch-generating images.
    flat = []
    for ch in out["chapters"]:
        for v in ch["verses"]:
            flat.append({
                "id": f"{ch['chapter_number']}.{v['verse_number']}",
                "chapter": ch["chapter_number"],
                "verse": v["verse_number"],
                "prompt": v["prompt"],
            })
    (ROOT / "bhagavad_gita_prompts_flat.json").write_text(
        json.dumps(flat, ensure_ascii=False, indent=2)
    )

    # CSV export — one row per verse. csv.writer handles quoting and newlines
    # automatically (QUOTE_ALL ensures spreadsheets parse multi-line prompts
    # cleanly). UTF-8 with BOM so Excel opens it correctly.
    with open(ROOT / "bhagavad_gita_prompts.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(["id", "chapter", "verse", "prompt"])
        for row in flat:
            w.writerow([row["id"], row["chapter"], row["verse"], row["prompt"] or ""])

    total = sum(len(c["verses"]) for c in out["chapters"])
    written = sum(
        1 for c in out["chapters"] for v in c["verses"]
        if v["prompt"] is not None
    )
    print(f"Total verses:     {total}")
    print(f"Prompts written:  {written}")
    print(f"Remaining:        {total - written}")
    print(f"Flat list length: {len(flat)}")


if __name__ == "__main__":
    build()
