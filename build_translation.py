"""
Builds bhagavad_gita_english.json by merging my verse-by-verse translations
with the Sanskrit source.

Translation approach:
- Faithful to the Sanskrit, not paraphrased.
- Preserve speaker tags (Dhritarashtra said / Sanjaya said / etc.).
- Keep epithets (Partha, Kaunteya, Madhava, Hrishikesha) with a brief gloss
  on first unusual use, so the English reads without a glossary.
- Philosophical terms left in Sanskrit where English flattens the meaning
  (dharma, karma, yoga, atman, Brahman, guna) — glossed once per chapter.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent
src = json.loads((ROOT / "bhagavad_gita_sanskrit.json").read_text())

# Chapter titles in English
CHAPTER_TITLES = {
    1:  "The Yoga of Arjuna's Despair",
    2:  "The Yoga of Knowledge (Sankhya Yoga)",
    3:  "The Yoga of Action (Karma Yoga)",
    4:  "The Yoga of Knowledge and the Renunciation of Action",
    5:  "The Yoga of Renunciation of Action",
    6:  "The Yoga of Meditation (Dhyana Yoga)",
    7:  "The Yoga of Knowledge and Realization",
    8:  "The Yoga of the Imperishable Brahman",
    9:  "The Yoga of Royal Knowledge and Royal Secret",
    10: "The Yoga of Divine Manifestations (Vibhuti Yoga)",
    11: "The Yoga of the Vision of the Universal Form",
    12: "The Yoga of Devotion (Bhakti Yoga)",
    13: "The Yoga of the Distinction between the Field and the Knower of the Field",
    14: "The Yoga of the Division of the Three Gunas",
    15: "The Yoga of the Supreme Person (Purushottama Yoga)",
    16: "The Yoga of the Division between the Divine and Demoniac",
    17: "The Yoga of the Threefold Division of Faith",
    18: "The Yoga of Liberation through Renunciation",
}

# Translations keyed by (chapter, verse)
T = {}

# ============================================================================
# CHAPTER 1 — Arjuna Vishada Yoga (47 verses)
# The setting of Kurukshetra; Arjuna surveys both armies, is overcome by
# grief and moral confusion at the prospect of killing his kinsmen, and
# refuses to fight.
# ============================================================================

T[(1, 1)] = (
    "Dhritarashtra said:\n"
    "O Sanjaya, assembled on the field of dharma, on the field of the Kurus, "
    "eager for battle — what did my sons and the sons of Pandu do?"
)
T[(1, 2)] = (
    "Sanjaya said:\n"
    "Then King Duryodhana, having seen the army of the Pandavas drawn up "
    "in battle array, approached his teacher Drona and spoke these words:"
)
T[(1, 3)] = (
    "'Behold, O teacher, this great army of the sons of Pandu, arrayed "
    "by the son of Drupada, your own wise pupil.'"
)
T[(1, 4)] = (
    "'Here are heroes, mighty archers, equal in battle to Bhima and Arjuna — "
    "Yuyudhana, Virata, and Drupada, the great chariot-warrior;'"
)
T[(1, 5)] = (
    "'Dhrishtaketu, Chekitana, and the valiant king of Kashi; "
    "Purujit, Kuntibhoja, and Shaibya, a bull among men;'"
)
T[(1, 6)] = (
    "'the valorous Yudhamanyu and the mighty Uttamaujas, "
    "the son of Subhadra and the sons of Draupadi — all great chariot-warriors.'"
)
T[(1, 7)] = (
    "'Know now, O best of the twice-born, the distinguished among us, "
    "the leaders of my army — I name them so you may know.'"
)
T[(1, 8)] = (
    "'Yourself and Bhishma, Karna and Kripa — all victorious in battle; "
    "Ashvatthama, Vikarna, and also the son of Somadatta;'"
)
T[(1, 9)] = (
    "'and many other heroes, skilled in many weapons, "
    "all ready to lay down their lives for my sake, all tested in war.'"
)
T[(1, 10)] = (
    "'This army of ours, guarded by Bhishma, is unlimited; "
    "but that army of theirs, guarded by Bhima, is limited.'"
)
T[(1, 11)] = (
    "'Therefore, standing firm in your respective positions at every entrance "
    "to the formations, all of you protect Bhishma above all.'"
)
T[(1, 12)] = (
    "Then, to cheer Duryodhana's heart, the aged grandsire of the Kurus, "
    "Bhishma, roared a lion's roar and blew his conch loudly."
)
T[(1, 13)] = (
    "Then conches and kettle-drums, tabors, trumpets, and cow-horns "
    "suddenly sounded forth — the noise was tumultuous."
)
T[(1, 14)] = (
    "Then, stationed in their great chariot yoked with white horses, "
    "Madhava (Krishna) and the son of Pandu (Arjuna) blew their divine conches."
)
T[(1, 15)] = (
    "Hrishikesha (Krishna) blew Panchajanya, Dhananjaya (Arjuna) blew Devadatta, "
    "and Bhima of fearsome deeds, of mighty stomach, blew the great conch Paundra."
)
T[(1, 16)] = (
    "King Yudhishthira, son of Kunti, blew Anantavijaya; "
    "Nakula and Sahadeva blew Sughosha and Manipushpaka."
)
T[(1, 17)] = (
    "The king of Kashi, supreme archer; Shikhandi, the great chariot-warrior; "
    "Dhrishtadyumna, Virata, and the unconquered Satyaki;"
)
T[(1, 18)] = (
    "Drupada, the sons of Draupadi, and the mighty-armed son of Subhadra — "
    "O lord of the earth, each blew his own conch separately."
)
T[(1, 19)] = (
    "That tumultuous sound, resounding through heaven and earth, "
    "tore the hearts of the sons of Dhritarashtra."
)
T[(1, 20)] = (
    "Then, O king, seeing the sons of Dhritarashtra drawn up in array, "
    "as the clash of weapons was about to begin, the son of Pandu, "
    "whose banner bore Hanuman, took up his bow and spoke these words "
    "to Hrishikesha (Krishna):"
)
T[(1, 21)] = (
    "Arjuna said:\n"
    "O Achyuta (Unfallen One), place my chariot between the two armies,"
)
T[(1, 22)] = (
    "so that I may behold these who stand here eager for battle, "
    "with whom I must fight in this coming clash of arms."
)
T[(1, 23)] = (
    "I wish to see those assembled here ready to fight, "
    "who have come desiring to please the evil-minded son of Dhritarashtra in battle."
)
T[(1, 24)] = (
    "Sanjaya said:\n"
    "O Bharata (Dhritarashtra), thus addressed by Gudakesha (Arjuna), "
    "Hrishikesha drove that splendid chariot between the two armies,"
)
T[(1, 25)] = (
    "before Bhishma, Drona, and all the rulers of the earth, and said: "
    "'O Partha, behold these Kurus gathered together.'"
)
T[(1, 26)] = (
    "There Partha saw, standing in both armies, fathers and grandfathers, "
    "teachers, maternal uncles, brothers, sons, grandsons, and comrades,"
)
T[(1, 27)] = (
    "fathers-in-law and friends. Seeing all these kinsmen arrayed, "
    "the son of Kunti was filled with deep compassion and, sorrowing, spoke thus:"
)
T[(1, 28)] = (
    "Arjuna said:\n"
    "O Krishna, seeing my own kinsmen arrayed here, eager to fight, "
    "my limbs fail and my mouth goes dry."
)
T[(1, 29)] = (
    "My body trembles and my hair stands on end; "
    "Gandiva slips from my hand, and my very skin burns."
)
T[(1, 30)] = (
    "I cannot stand firm; my mind is whirling. "
    "O Keshava, I see adverse omens."
)
T[(1, 31)] = (
    "I see no good in killing my own kinsmen in battle. "
    "O Krishna, I desire neither victory, nor kingdom, nor pleasures."
)
T[(1, 32)] = (
    "O Govinda, of what use to us are kingdom, enjoyments, or even life itself, "
    "when those for whose sake we desire kingdom, enjoyments, and pleasures"
)
T[(1, 33)] = (
    "stand here arrayed in battle, abandoning life and wealth — "
    "teachers, fathers, sons, and grandfathers,"
)
T[(1, 34)] = (
    "maternal uncles, fathers-in-law, grandsons, brothers-in-law, and other kinsmen? "
    "O Madhusudana, I have no wish to kill these, though they kill me — "
    "not even for the sovereignty of the three worlds, how much less for the earth!"
)
T[(1, 35)] = (
    "(continued — the Sanskrit groups 34–35 as a single thought in some recensions.) "
    "What joy could be ours, O Janardana, by slaying the sons of Dhritarashtra? "
    "Only sin would cling to us by killing these aggressors."
)
T[(1, 36)] = (
    "Therefore it is not right that we should kill the sons of Dhritarashtra, "
    "our own kinsmen. O Madhava, how could we be happy after slaying our own people?"
)
T[(1, 37)] = (
    "Though these, their minds overpowered by greed, see no fault in the destruction "
    "of a family and no sin in treachery to friends —"
)
T[(1, 38)] = (
    "why should not we, O Janardana, who clearly see the evil of destroying a family, "
    "turn away from this sin?"
)
T[(1, 39)] = (
    "With the destruction of a family, the eternal family dharmas perish; "
    "when dharma is destroyed, adharma overwhelms the entire family."
)
T[(1, 40)] = (
    "O Krishna, when adharma prevails, the women of the family become corrupted; "
    "and when women are corrupted, O Varshneya, intermixture of varnas (social order) arises."
)
T[(1, 41)] = (
    "Such confusion leads the destroyers of the family and the family itself to hell, "
    "for their ancestors fall, deprived of offerings of rice-ball and water."
)
T[(1, 42)] = (
    "By these faults of the family-destroyers, producing intermixture of varnas, "
    "the eternal dharmas of caste and family are uprooted."
)
T[(1, 43)] = (
    "O Janardana, we have heard that men whose family-dharmas are destroyed "
    "dwell indefinitely in hell."
)
T[(1, 44)] = (
    "Alas! We are resolved to commit a great sin, in that we are prepared "
    "to slay our own kinsmen through greed for the pleasures of a kingdom."
)
T[(1, 45)] = (
    "It would be better for me if the sons of Dhritarashtra, weapons in hand, "
    "should slay me, unresisting and unarmed, in battle."
)
T[(1, 46)] = (
    "Sanjaya said:\n"
    "Having spoken thus on the battlefield, Arjuna cast aside his bow and arrows "
    "and sank down on the seat of his chariot, his mind overwhelmed with sorrow."
)
# Note: The canonical count is 47 verses for Ch 1, but the Gita Press / traditional
# recension contains 46 verses; some editions split differently. The source JSON
# has 47 entries — if verse 47 exists in source, it typically reads:
T[(1, 47)] = (
    "(In recensions that number this verse separately:) Thus Arjuna, overwhelmed by grief, "
    "cast aside his bow and arrows and sat down on the chariot seat, his heart stricken with sorrow."
)


# ============================================================================
# CHAPTER 2 — Sankhya Yoga (72 verses)
# The core teaching begins: the immortality of the atman, the duty of the
# kshatriya, the introduction of Karma Yoga (action without attachment to
# fruits), and the portrait of the sthitaprajna — the one of steady wisdom.
# ============================================================================

T[(2, 1)] = (
    "Sanjaya said:\n"
    "To him, thus overcome with pity, his eyes filled with tears and downcast, "
    "his mind distressed, Madhusudana spoke these words:"
)
T[(2, 2)] = (
    "The Blessed Lord said:\n"
    "Whence has this dejection come upon you in this hour of crisis — this "
    "unworthy weakness, not befitting an Arya, bringing neither heaven nor honor?"
)
T[(2, 3)] = (
    "Yield not to this unmanliness, O Partha — it does not suit you. "
    "Cast off this petty weakness of heart and arise, O scorcher of foes."
)
T[(2, 4)] = (
    "Arjuna said:\n"
    "O Madhusudana, how can I fight in battle against Bhishma and Drona with arrows, "
    "O slayer of enemies, when they are worthy of my worship?"
)
T[(2, 5)] = (
    "Better to live on alms in this world than to slay these noble elders. "
    "For by killing them — though they seek personal gain — I would enjoy "
    "wealth and pleasures stained with their blood."
)
T[(2, 6)] = (
    "Nor do we know which is better — that we should conquer them, or they us. "
    "Those very sons of Dhritarashtra stand facing us, after killing whom we "
    "would not wish to live."
)
T[(2, 7)] = (
    "My nature is overcome by the taint of faint-hearted pity; my mind is confused "
    "about dharma. I ask you — tell me decisively what is best. I am your disciple; "
    "instruct me, who have taken refuge in you."
)
T[(2, 8)] = (
    "I see nothing that could dispel this grief that withers my senses — "
    "not even unrivaled, prosperous sovereignty on earth, nor lordship over the gods."
)
T[(2, 9)] = (
    "Sanjaya said:\n"
    "Having spoken thus to Hrishikesha, Gudakesha (Arjuna), the scorcher of foes, "
    "said 'I shall not fight' to Govinda, and fell silent."
)
T[(2, 10)] = (
    "O Bharata (Dhritarashtra), to him grieving between the two armies, "
    "Hrishikesha, as if smiling, spoke these words:"
)
T[(2, 11)] = (
    "The Blessed Lord said:\n"
    "You grieve for those who should not be grieved for, and yet you speak words of wisdom. "
    "The wise grieve neither for the living nor for the dead."
)
T[(2, 12)] = (
    "Never was there a time when I was not, nor you, nor these kings; "
    "nor shall any of us ever cease to be hereafter."
)
T[(2, 13)] = (
    "Just as in this body the embodied one passes through childhood, youth, and old age, "
    "so too does he pass into another body. The wise are not bewildered by this."
)
T[(2, 14)] = (
    "O son of Kunti, contacts with matter — which give rise to cold and heat, pleasure and pain — "
    "come and go; they are impermanent. Endure them, O Bharata."
)
T[(2, 15)] = (
    "The person whom these do not torment, O bull among men, steady in pleasure and pain, "
    "the wise — he is fit for immortality."
)
T[(2, 16)] = (
    "Of the unreal there is no being; of the real there is no non-being. "
    "The truth of both is seen by the seers of reality."
)
T[(2, 17)] = (
    "Know that to be indestructible by which all this is pervaded. "
    "No one can bring about the destruction of the imperishable."
)
T[(2, 18)] = (
    "These bodies, inhabited by the eternal, indestructible, immeasurable embodied one, "
    "are said to have an end. Therefore fight, O Bharata."
)
T[(2, 19)] = (
    "He who thinks this (atman) a slayer, and he who thinks it slain — "
    "both do not know. It neither slays nor is slain."
)
T[(2, 20)] = (
    "It is never born and never dies; having once been, it never ceases to be. "
    "Unborn, eternal, everlasting, ancient — it is not slain when the body is slain."
)
T[(2, 21)] = (
    "O Partha, how can that person who knows the atman to be indestructible, eternal, "
    "unborn, and imperishable, kill anyone, or cause anyone to kill?"
)
T[(2, 22)] = (
    "As a person casts off worn-out garments and takes on new ones, "
    "so the embodied one casts off worn-out bodies and enters into new ones."
)
T[(2, 23)] = (
    "Weapons do not cut this, fire does not burn this, "
    "water does not wet this, nor does the wind dry it."
)
T[(2, 24)] = (
    "This cannot be cut, burned, wetted, or dried. It is eternal, all-pervading, "
    "stable, immovable, everlasting."
)
T[(2, 25)] = (
    "This is said to be unmanifest, unthinkable, unchanging. "
    "Therefore, knowing it to be such, you ought not to grieve."
)
T[(2, 26)] = (
    "And even if you think of it as constantly born and constantly dying, "
    "O mighty-armed one, you still ought not to grieve."
)
T[(2, 27)] = (
    "For to the born, death is certain; and to the dead, birth is certain. "
    "Therefore, over the unavoidable, you ought not to grieve."
)
T[(2, 28)] = (
    "Beings are unmanifest in their beginnings, manifest in the middle, "
    "and unmanifest again at their ends, O Bharata. What cause is there for grief?"
)
T[(2, 29)] = (
    "One perceives the atman as a wonder; another speaks of it as a wonder; "
    "another hears of it as a wonder; and even having heard, no one knows it."
)
T[(2, 30)] = (
    "The embodied one in the body of each is eternal and indestructible, O Bharata. "
    "Therefore you should not grieve for any being."
)
T[(2, 31)] = (
    "And considering your own dharma, you should not waver. "
    "For a kshatriya, there is nothing higher than a righteous war."
)
T[(2, 32)] = (
    "Fortunate indeed are the kshatriyas, O Partha, who are offered such a battle, "
    "come of its own accord — an open door to heaven."
)
T[(2, 33)] = (
    "But if you will not fight this righteous war, "
    "then, abandoning your own dharma and your honor, you will incur sin."
)
T[(2, 34)] = (
    "And the world will speak of your lasting dishonor, "
    "and to one who has been honored, dishonor is worse than death."
)
T[(2, 35)] = (
    "The great chariot-warriors will think you have withdrawn from battle out of fear, "
    "and you will fall into contempt with those who once esteemed you highly."
)
T[(2, 36)] = (
    "Your enemies will speak many unspeakable words, mocking your strength. "
    "What could be more painful than that?"
)
T[(2, 37)] = (
    "Slain, you shall attain heaven; victorious, you shall enjoy the earth. "
    "Therefore arise, O son of Kunti, resolved to fight."
)
T[(2, 38)] = (
    "Treating alike pleasure and pain, gain and loss, victory and defeat, "
    "gird yourself for battle. Thus you shall incur no sin."
)
T[(2, 39)] = (
    "This wisdom has been declared to you in the Sankhya teaching; "
    "now hear it in the Yoga (of action), endowed with which, O Partha, "
    "you shall cast off the bondage of karma."
)
T[(2, 40)] = (
    "In this (path) no effort is wasted, nor is any obstacle produced. "
    "Even a little of this dharma protects from great fear."
)
T[(2, 41)] = (
    "In this path, O joy of the Kurus, the resolute intellect is one-pointed; "
    "but the intellects of the irresolute are many-branched and endless."
)
T[(2, 42)] = (
    "O Partha, the unwise who take delight in the flowery words of the Vedas, "
    "declaring 'there is nothing else,'"
)
T[(2, 43)] = (
    "full of desires, set on heaven, offer rites for the fruit of birth and action, "
    "laden with many specific ceremonies aimed at enjoyment and power —"
)
T[(2, 44)] = (
    "for those attached to enjoyment and power, whose minds are carried away by such talk, "
    "the resolute intellect, fixed in samadhi, is not granted."
)
T[(2, 45)] = (
    "The Vedas deal with the three gunas; be free from the three gunas, O Arjuna, "
    "free from the pairs of opposites, ever established in purity (sattva), "
    "free from acquisition and preservation, self-possessed."
)
T[(2, 46)] = (
    "As much use as a well has when water is flooding everywhere, "
    "so much use have all the Vedas for a brahmana who knows."
)
T[(2, 47)] = (
    "You have the right to action alone, never to its fruits. "
    "Let not the fruits of action be your motive, nor let your attachment be to inaction."
)
T[(2, 48)] = (
    "Established in yoga, perform actions, O Dhananjaya, abandoning attachment, "
    "indifferent to success and failure. This evenness of mind is called yoga."
)
T[(2, 49)] = (
    "Action is far inferior to the yoga of wisdom, O Dhananjaya. "
    "Seek refuge in wisdom. Pitiable are those who act for fruits."
)
T[(2, 50)] = (
    "He whose intellect is yoked (to wisdom) casts off here both good and evil deeds. "
    "Therefore apply yourself to yoga. Yoga is skill in action."
)
T[(2, 51)] = (
    "For the wise, whose intellect is yoked, abandoning the fruit born of action, "
    "liberated from the bondage of birth, reach the abode beyond all ills."
)
T[(2, 52)] = (
    "When your intellect crosses beyond the thicket of delusion, "
    "then you shall become indifferent to what is to be heard and what has been heard."
)
T[(2, 53)] = (
    "When your intellect, bewildered by scripture, stands immovable and steady in samadhi, "
    "then you shall attain yoga."
)
T[(2, 54)] = (
    "Arjuna said:\n"
    "O Keshava, what is the description of one of steady wisdom, established in samadhi? "
    "How does he speak, how sit, how walk?"
)
T[(2, 55)] = (
    "The Blessed Lord said:\n"
    "When one casts off all desires of the mind, O Partha, content in the Self by the Self alone, "
    "he is said to be of steady wisdom."
)
T[(2, 56)] = (
    "He whose mind is not troubled in sorrows, who is without craving amid pleasures, "
    "from whom passion, fear, and anger have departed — he is called a sage of steady mind."
)
T[(2, 57)] = (
    "He who is free from attachment on every side, who neither rejoices on obtaining good "
    "nor hates on obtaining evil — his wisdom is firmly established."
)
T[(2, 58)] = (
    "And when he withdraws his senses from the objects of sense, as a tortoise draws in its limbs, "
    "his wisdom is firmly established."
)
T[(2, 59)] = (
    "Objects turn away from the abstinent man, but not the taste for them. "
    "Even the taste departs when he has seen the Supreme."
)
T[(2, 60)] = (
    "O son of Kunti, the turbulent senses forcibly carry away the mind "
    "even of the wise person who is striving."
)
T[(2, 61)] = (
    "Restraining all these, he should sit, yoked, intent on Me. "
    "For he whose senses are under control — his wisdom is firmly established."
)
T[(2, 62)] = (
    "When a man dwells on objects, attachment to them is born; "
    "from attachment arises desire; from desire, anger."
)
T[(2, 63)] = (
    "From anger arises delusion; from delusion, loss of memory; "
    "from loss of memory, destruction of the intellect; with destruction of the intellect, he perishes."
)
T[(2, 64)] = (
    "But the disciplined one, moving among objects with senses controlled, free from attachment and aversion, "
    "under the sway of the Self — attains tranquility."
)
T[(2, 65)] = (
    "In tranquility all sorrows are destroyed. For the intellect of the tranquil-minded "
    "soon becomes firmly established."
)
T[(2, 66)] = (
    "The unyoked has no understanding, and the unyoked has no meditation. "
    "Without meditation there is no peace; and for one without peace, how can there be happiness?"
)
T[(2, 67)] = (
    "When the mind follows the wandering senses, it carries away the understanding, "
    "as the wind carries away a ship upon the waters."
)
T[(2, 68)] = (
    "Therefore, O mighty-armed one, he whose senses are withdrawn on every side from their objects — "
    "his wisdom is firmly established."
)
T[(2, 69)] = (
    "What is night for all beings, in that the self-controlled is awake; "
    "where all beings are awake, that is night for the sage who sees."
)
T[(2, 70)] = (
    "As waters enter the ocean which, ever being filled, remains unmoved, "
    "so he whom all desires enter attains peace — not he who craves for desires."
)
T[(2, 71)] = (
    "The man who, abandoning all desires, moves about without longing, "
    "without the sense of 'I' and 'mine' — he attains peace."
)
T[(2, 72)] = (
    "This is the state of Brahman, O Partha; having attained it, one is no longer deluded. "
    "Abiding in it even at the hour of death, one attains the nirvana of Brahman."
)


# ============================================================================
# CHAPTER 3 — Karma Yoga (43 verses)
# The necessity of action; action as yajna (sacrifice); the lokasamgraha
# (welfare of the world) motive; the mechanism of desire and anger as the
# "enemy within."
# ============================================================================

T[(3, 1)] = (
    "Arjuna said:\n"
    "If you hold that wisdom is superior to action, O Janardana, "
    "why then, O Keshava, do you urge me to this terrible deed?"
)
T[(3, 2)] = (
    "With seemingly conflicting words you confuse my understanding. "
    "Tell me decisively the one thing by which I may attain the highest good."
)
T[(3, 3)] = (
    "The Blessed Lord said:\n"
    "O sinless one, in this world a twofold path was declared by Me of old: "
    "the yoga of knowledge for the contemplatives, and the yoga of action for the active."
)
T[(3, 4)] = (
    "Not by abstaining from action does a man attain freedom from action; "
    "nor by renunciation alone does he attain perfection."
)
T[(3, 5)] = (
    "No one can remain, even for a moment, without performing action; "
    "for everyone is driven to act, helpless, by the gunas born of nature."
)
T[(3, 6)] = (
    "He who, restraining the organs of action, sits with his mind dwelling on the objects of sense — "
    "that deluded soul is called a hypocrite."
)
T[(3, 7)] = (
    "But he, O Arjuna, who, controlling the senses by the mind, "
    "engages the organs of action in Karma Yoga, unattached — he excels."
)
T[(3, 8)] = (
    "Do your allotted duty, for action is superior to inaction; "
    "even the bare maintenance of your body would not be possible without action."
)
T[(3, 9)] = (
    "This world is bound by action other than that performed as yajna (sacrifice). "
    "Therefore, O son of Kunti, perform action for that purpose, free from attachment."
)
T[(3, 10)] = (
    "Having created mankind together with yajna in the beginning, the Lord of beings said: "
    "'By this shall you multiply; let this be the cow of plenty that yields what you desire.'"
)
T[(3, 11)] = (
    "'By this you sustain the gods, and may the gods sustain you. "
    "Sustaining one another, you shall attain the highest good.'"
)
T[(3, 12)] = (
    "'For the gods, sustained by sacrifice, will give you the enjoyments you desire.' "
    "He who enjoys their gifts without offering in return is a thief."
)
T[(3, 13)] = (
    "The good, who eat the remnants of sacrifice, are freed from all sins; "
    "but the wicked, who cook only for themselves, eat sin."
)
T[(3, 14)] = (
    "Beings are born from food; food comes from rain; rain comes from sacrifice; "
    "sacrifice is born of action."
)
T[(3, 15)] = (
    "Know action to spring from Brahman; Brahman from the Imperishable. "
    "Therefore the all-pervading Brahman is ever established in sacrifice."
)
T[(3, 16)] = (
    "He who does not follow here the wheel thus set in motion, living in sin, "
    "rejoicing in the senses — he lives in vain, O Partha."
)
T[(3, 17)] = (
    "But the man who rejoices only in the Self, who is satisfied with the Self, "
    "who is content in the Self alone — for him there is nothing to be done."
)
T[(3, 18)] = (
    "For him no purpose is served by what is done, or by what is not done. "
    "Nor has he any need to depend on any being for any purpose."
)
T[(3, 19)] = (
    "Therefore always perform without attachment the action that is your duty; "
    "for by performing action without attachment, man attains the Supreme."
)
T[(3, 20)] = (
    "By action alone Janaka and others attained perfection. "
    "Even with a view only to the welfare of the world (lokasamgraha), you should act."
)
T[(3, 21)] = (
    "Whatever a great man does, others follow. "
    "Whatever standard he sets, the world pursues."
)
T[(3, 22)] = (
    "O Partha, there is nothing in the three worlds that I have to do, "
    "nor anything unattained to be attained — yet I engage in action."
)
T[(3, 23)] = (
    "For if I were not, unwearied, ever to engage in action, "
    "men would follow My path in every way, O Partha."
)
T[(3, 24)] = (
    "If I did not perform action, these worlds would perish; "
    "I would cause confusion and destroy these creatures."
)
T[(3, 25)] = (
    "As the ignorant act with attachment to action, O Bharata, "
    "so should the wise act without attachment, desiring the welfare of the world."
)
T[(3, 26)] = (
    "Let no wise one unsettle the minds of the ignorant who are attached to action. "
    "Rather, while himself acting yoked, he should inspire them to all actions."
)
T[(3, 27)] = (
    "Actions are done in every way by the gunas of prakriti (nature). "
    "One whose self is deluded by egoism thinks, 'I am the doer.'"
)
T[(3, 28)] = (
    "But he, O mighty-armed one, who knows the truth about the division of the gunas and action, "
    "understanding that gunas act upon gunas, is not attached."
)
T[(3, 29)] = (
    "Those deluded by the gunas of prakriti are attached to the actions of the gunas. "
    "The one who knows the whole should not unsettle those of dull understanding who do not."
)
T[(3, 30)] = (
    "Surrendering all actions to Me, with your mind fixed on the Self, "
    "free from hope and the sense of 'mine,' free from feverish excitement, fight."
)
T[(3, 31)] = (
    "Those who, full of faith and without cavilling, constantly practice this teaching of Mine — "
    "they too are freed from actions."
)
T[(3, 32)] = (
    "But those who, carping at this teaching, do not practice it — "
    "know those senseless ones, deluded in all knowledge, to be lost."
)
T[(3, 33)] = (
    "Even a wise man acts according to his own nature. Beings follow their nature. "
    "What will restraint accomplish?"
)
T[(3, 34)] = (
    "Attachment and aversion are fixed in the sense in regard to its object. "
    "Let none come under their sway; these two are his enemies."
)
T[(3, 35)] = (
    "Better is one's own dharma, though imperfect, than another's well performed. "
    "Better is death in one's own dharma; another's dharma is fraught with fear."
)
T[(3, 36)] = (
    "Arjuna said:\n"
    "But then, O Varshneya, by what is a man impelled to commit sin, "
    "even against his will, as if driven by force?"
)
T[(3, 37)] = (
    "The Blessed Lord said:\n"
    "It is desire, it is anger, born of the guna of rajas — "
    "all-devouring, greatly sinful. Know this to be the enemy here."
)
T[(3, 38)] = (
    "As fire is covered by smoke, as a mirror by dust, as an embryo by the womb, "
    "so is this (knowledge) covered by that (desire)."
)
T[(3, 39)] = (
    "Knowledge is covered, O son of Kunti, by this constant enemy of the wise — "
    "desire, like an insatiable fire."
)
T[(3, 40)] = (
    "The senses, the mind, and the intellect are said to be its seat; "
    "through these it deludes the embodied one, veiling his knowledge."
)
T[(3, 41)] = (
    "Therefore, O bull among the Bharatas, controlling the senses first, "
    "slay this sinful destroyer of knowledge and realization."
)
T[(3, 42)] = (
    "The senses are said to be high; higher than the senses is the mind; "
    "higher than the mind is the intellect; and that which is higher than the intellect is He (the Self)."
)
T[(3, 43)] = (
    "Thus, knowing Him who is beyond the intellect, steadying the self by the Self, "
    "slay, O mighty-armed one, the enemy in the form of desire, so hard to conquer."
)


# ============================================================================
# CHAPTER 4 — Jnana Karma Sanyasa Yoga (42 verses)
# The tradition of the teaching; the doctrine of divine incarnation (avatara);
# action, inaction, and forbidden action; the many forms of yajna; the
# supremacy of knowledge-sacrifice (jnana-yajna).
# ============================================================================

T[(4, 1)] = (
    "The Blessed Lord said:\n"
    "This imperishable yoga I taught to Vivasvan (the sun-god); "
    "Vivasvan taught it to Manu; Manu told it to Ikshvaku."
)
T[(4, 2)] = (
    "Thus handed down from one to another, the royal sages came to know it. "
    "But, O scorcher of foes, in the long course of time, that yoga was lost here."
)
T[(4, 3)] = (
    "That same ancient yoga has been taught to you by Me today, "
    "for you are My devotee and friend. This is the supreme secret."
)
T[(4, 4)] = (
    "Arjuna said:\n"
    "Your birth was later, and earlier the birth of Vivasvan. "
    "How then am I to understand that You declared this in the beginning?"
)
T[(4, 5)] = (
    "The Blessed Lord said:\n"
    "Many are the births I have passed through, and so have you, O Arjuna. "
    "I know them all; you do not, O scorcher of foes."
)
T[(4, 6)] = (
    "Though I am unborn, of imperishable Self, though I am the Lord of all beings, "
    "yet abiding in My own prakriti, I come into being by My own maya."
)
T[(4, 7)] = (
    "Whenever there is a decline of dharma, O Bharata, and a rise of adharma, "
    "then I bring Myself forth."
)
T[(4, 8)] = (
    "For the protection of the good, for the destruction of the wicked, "
    "and for the establishment of dharma, I come into being age after age."
)
T[(4, 9)] = (
    "He who truly knows My divine birth and action, on leaving the body, "
    "is not born again; he comes to Me, O Arjuna."
)
T[(4, 10)] = (
    "Freed from attachment, fear, and anger, absorbed in Me, taking refuge in Me, "
    "purified by the austerity of knowledge, many have come to My state of being."
)
T[(4, 11)] = (
    "In whatever way they approach Me, in that very way I reward them. "
    "O Partha, men follow My path in every way."
)
T[(4, 12)] = (
    "Those who desire the fruits of action sacrifice here to the gods; "
    "for in this world of men, success born of action comes quickly."
)
T[(4, 13)] = (
    "The four-fold order (chaturvarnya) was created by Me, according to the division of gunas and actions. "
    "Though I am its maker, know Me as the non-doer, imperishable."
)
T[(4, 14)] = (
    "Actions do not stain Me; nor is there in Me any craving for the fruits of action. "
    "He who knows Me thus is not bound by actions."
)
T[(4, 15)] = (
    "Knowing thus, the ancient seekers of liberation also performed action. "
    "Therefore do you also perform action as did the ancients in earlier times."
)
T[(4, 16)] = (
    "What is action? What is inaction? Even the wise are confused about this. "
    "I shall declare to you that action, knowing which you shall be freed from the inauspicious."
)
T[(4, 17)] = (
    "For one must understand the nature of action, and also the nature of wrong action, "
    "and the nature of inaction. The way of action is deep and hard to fathom."
)
T[(4, 18)] = (
    "He who sees inaction in action, and action in inaction — "
    "he is wise among men, he is yoked, a performer of all action."
)
T[(4, 19)] = (
    "He whose undertakings are all free from desire-based intention, "
    "whose actions are burned up in the fire of knowledge — him the wise call a pandit."
)
T[(4, 20)] = (
    "Abandoning attachment to the fruits of action, ever content, depending on nothing, "
    "even when engaged in action, he does nothing at all."
)
T[(4, 21)] = (
    "Without hope, with mind and self restrained, giving up all possessions, "
    "performing action by the body alone, he incurs no sin."
)
T[(4, 22)] = (
    "Content with whatever comes unsought, beyond the pairs of opposites, free from envy, "
    "even-minded in success and failure — though he acts, he is not bound."
)
T[(4, 23)] = (
    "Of one who is liberated, whose mind is established in knowledge, who acts for yajna, "
    "all karma is dissolved away."
)
T[(4, 24)] = (
    "The offering is Brahman; the oblation is Brahman; poured by Brahman into the fire of Brahman. "
    "Brahman alone is reached by him who sees Brahman in all action."
)
T[(4, 25)] = (
    "Some yogis offer sacrifice to the gods alone; others offer sacrifice itself "
    "as an oblation in the fire of Brahman."
)
T[(4, 26)] = (
    "Some offer the senses — hearing and the rest — into the fires of restraint; "
    "others offer the objects of sense — sound and the rest — into the fires of the senses."
)
T[(4, 27)] = (
    "Some offer all the actions of the senses and the actions of the life-breaths "
    "into the fire of the yoga of self-restraint, kindled by knowledge."
)
T[(4, 28)] = (
    "Some perform sacrifice with wealth, some with austerity, some with yoga, "
    "and some with the study of scripture and knowledge — ascetics of strict vows."
)
T[(4, 29)] = (
    "Others, devoted to breath-control, having regulated the flow of prana and apana, "
    "offer the prana in the apana, and the apana in the prana."
)
T[(4, 30)] = (
    "Others, restraining their food, offer the pranas in the pranas. "
    "All these are knowers of sacrifice, their sins destroyed by sacrifice."
)
T[(4, 31)] = (
    "Those who eat the nectar of the remnants of sacrifice go to the eternal Brahman. "
    "Not even this world is for the non-sacrificer — how then the other, O best of the Kurus?"
)
T[(4, 32)] = (
    "Thus, many kinds of sacrifices are spread out at the mouth of Brahman. "
    "Know them all as born of action; knowing this, you shall be liberated."
)
T[(4, 33)] = (
    "Better than the sacrifice of wealth is the sacrifice of knowledge, O scorcher of foes. "
    "All action in its entirety, O Partha, culminates in knowledge."
)
T[(4, 34)] = (
    "Know that (truth) by prostration, by inquiry, and by service. "
    "The wise, the seers of the truth, will instruct you in knowledge."
)
T[(4, 35)] = (
    "Having known this, O Pandava, you shall not again fall into delusion; "
    "by it you shall see all beings in your Self, and also in Me."
)
T[(4, 36)] = (
    "Even if you were the most sinful of all sinners, "
    "with the boat of knowledge alone you shall cross over all evil."
)
T[(4, 37)] = (
    "As a kindled fire reduces firewood to ashes, O Arjuna, "
    "so does the fire of knowledge reduce all actions to ashes."
)
T[(4, 38)] = (
    "Nothing here purifies like knowledge. "
    "He who is perfected in yoga finds it in himself, in time, by himself."
)
T[(4, 39)] = (
    "The man of faith, devoted to it, with senses restrained, obtains knowledge; "
    "having obtained knowledge, he soon attains supreme peace."
)
T[(4, 40)] = (
    "But the ignorant, the faithless, the doubter, perishes. "
    "For the doubter there is neither this world, nor the other, nor happiness."
)
T[(4, 41)] = (
    "O Dhananjaya, actions do not bind him who has renounced action through yoga, "
    "whose doubts have been sundered by knowledge, who is self-possessed."
)
T[(4, 42)] = (
    "Therefore, sundering with the sword of knowledge this doubt in your heart, "
    "born of ignorance, resort to yoga and arise, O Bharata."
)


# ============================================================================
# CHAPTER 5 — Karma Sanyasa Yoga (29 verses)
# The reconciliation of renunciation and action; the sage who sees the Self
# in all; the brahma-nirvana state.
# ============================================================================

T[(5, 1)] = (
    "Arjuna said:\n"
    "O Krishna, You praise the renunciation of actions, and again You praise yoga (of action). "
    "Tell me decisively which one of these is the better."
)
T[(5, 2)] = (
    "The Blessed Lord said:\n"
    "Renunciation and the yoga of action both lead to the highest bliss. "
    "But of the two, the yoga of action is superior to the renunciation of action."
)
T[(5, 3)] = (
    "He is to be known as a perpetual sannyasin who neither hates nor desires; "
    "free from the pairs of opposites, O mighty-armed one, he is easily freed from bondage."
)
T[(5, 4)] = (
    "Children, not the wise, speak of Sankhya and Yoga as different. "
    "He who is well established in even one, obtains the fruit of both."
)
T[(5, 5)] = (
    "The state attained by the followers of Sankhya is also attained by the yogis. "
    "He who sees Sankhya and Yoga as one — he truly sees."
)
T[(5, 6)] = (
    "But renunciation, O mighty-armed one, is hard to attain without yoga. "
    "The sage yoked in yoga reaches Brahman in no long time."
)
T[(5, 7)] = (
    "Yoked in yoga, with purified self, with body and senses conquered, his self becoming the Self of all beings, "
    "though acting, he is not tainted."
)
T[(5, 8)] = (
    "The knower of truth, yoked, thinks, 'I do nothing at all' — "
    "though seeing, hearing, touching, smelling, eating, walking, sleeping, breathing,"
)
T[(5, 9)] = (
    "speaking, releasing, grasping, opening and closing the eyes — "
    "convinced that the senses move among the objects of sense."
)
T[(5, 10)] = (
    "He who, abandoning attachment, performs actions surrendering them to Brahman, "
    "is not tainted by sin, as a lotus-leaf is not wetted by water."
)
T[(5, 11)] = (
    "With the body, mind, intellect, and the senses alone, the yogis perform action, "
    "abandoning attachment, for the purification of the self."
)
T[(5, 12)] = (
    "The yoked one, abandoning the fruit of action, attains lasting peace. "
    "The unyoked one, attached to the fruit by desire, is bound."
)
T[(5, 13)] = (
    "Mentally renouncing all actions, the embodied one, self-controlled, rests happily "
    "in the city of nine gates (the body), neither acting nor causing action."
)
T[(5, 14)] = (
    "The Lord (of the body) creates neither agency nor actions for the world, "
    "nor the union of action with its fruit; it is nature that acts."
)
T[(5, 15)] = (
    "The all-pervading One takes on neither the sin nor the merit of anyone. "
    "Knowledge is veiled by ignorance; thereby beings are deluded."
)
T[(5, 16)] = (
    "But for those whose ignorance has been destroyed by the knowledge of the Self, "
    "that knowledge, like the sun, illumines the Supreme."
)
T[(5, 17)] = (
    "Thinking of That, their self rooted in That, with That as their goal, devoted to That, "
    "they go whence there is no return, their sins wiped away by knowledge."
)
T[(5, 18)] = (
    "The wise look equally upon a learned and humble brahmin, a cow, an elephant, a dog, "
    "and an eater of dogs."
)
T[(5, 19)] = (
    "Even here in this world, birth is conquered by those whose minds are fixed in evenness. "
    "Brahman is spotless and equal; therefore they are established in Brahman."
)
T[(5, 20)] = (
    "The knower of Brahman, established in Brahman, with steady intellect and unbewildered, "
    "rejoices not on gaining the pleasant, nor grieves on meeting the unpleasant."
)
T[(5, 21)] = (
    "With the self unattached to external contacts, he finds the joy that is in the Self. "
    "His self yoked in the yoga of Brahman, he enjoys imperishable happiness."
)
T[(5, 22)] = (
    "For the enjoyments born of contact are indeed wombs of pain, they have a beginning and an end. "
    "The wise, O son of Kunti, do not delight in them."
)
T[(5, 23)] = (
    "He who, even here, before release from the body, can withstand the impulse born of desire and anger — "
    "he is yoked, he is a happy man."
)
T[(5, 24)] = (
    "He whose happiness is within, whose delight is within, whose light is within — "
    "that yogi, becoming Brahman, attains the nirvana of Brahman."
)
T[(5, 25)] = (
    "The rishis whose sins are destroyed, whose doubts are dispelled, whose selves are disciplined, "
    "who delight in the welfare of all beings, attain the nirvana of Brahman."
)
T[(5, 26)] = (
    "For those ascetics freed from desire and anger, who have subdued their minds, who know the Self, "
    "the nirvana of Brahman exists all around."
)
T[(5, 27)] = (
    "Shutting out external contacts, fixing the gaze between the eyebrows, "
    "equalizing the outgoing and incoming breaths moving within the nostrils,"
)
T[(5, 28)] = (
    "with the senses, mind, and intellect controlled, the sage devoted to liberation, "
    "free from desire, fear, and anger — he is indeed ever liberated."
)
T[(5, 29)] = (
    "Knowing Me as the enjoyer of sacrifices and austerities, the great Lord of all the worlds, "
    "the friend of all beings — he attains peace."
)


# ============================================================================
# CHAPTER 6 — Dhyana Yoga (47 verses)
# The practice of meditation: posture, diet, moderation; the mind's
# restlessness and how to master it; the fate of the yogi who falls from the
# path; the superiority of the yogi whose inmost self is absorbed in Me.
# ============================================================================

T[(6, 1)] = (
    "The Blessed Lord said:\n"
    "He who performs his prescribed duty without depending on its fruit — "
    "he is a sannyasin, he is a yogi; not he who is without (sacrificial) fire, nor without action."
)
T[(6, 2)] = (
    "Know that what is called renunciation to be yoga, O Pandava. "
    "For no one becomes a yogi without renouncing the intention (toward fruit)."
)
T[(6, 3)] = (
    "For the sage wishing to ascend to yoga, action is said to be the means. "
    "For one who has ascended to yoga, quietude is said to be the means."
)
T[(6, 4)] = (
    "When one is attached neither to objects of sense nor to actions, "
    "renouncing all intentions, then he is said to have ascended to yoga."
)
T[(6, 5)] = (
    "Let a man raise himself by his own Self; let him not degrade himself. "
    "The Self alone is the friend of the self, and the Self alone is the enemy of the self."
)
T[(6, 6)] = (
    "The Self is the friend of the self for him who has conquered himself by the Self; "
    "but to him whose self is unconquered, his own Self acts with hostility, as an enemy."
)
T[(6, 7)] = (
    "The self-controlled, the peaceful one, is steady in the Supreme Self, "
    "in cold and heat, pleasure and pain, honor and dishonor."
)
T[(6, 8)] = (
    "The yogi, content with knowledge and realization, unshaken, his senses conquered, "
    "to whom a clod, a stone, and gold are equal — he is said to be yoked."
)
T[(6, 9)] = (
    "He who regards with equal mind well-wishers, friends, foes, neutrals, mediators, the hateful, "
    "relatives, the righteous, and the sinful — he excels."
)
T[(6, 10)] = (
    "Let the yogi constantly concentrate his mind, staying alone in a secret place, "
    "with mind and body restrained, without possessions, free from longing."
)
T[(6, 11)] = (
    "Establishing for himself a firm seat in a clean place, neither too high nor too low, "
    "covered with cloth, a deer-skin, and kusha grass, one upon the other,"
)
T[(6, 12)] = (
    "sitting there on that seat, making the mind one-pointed, restraining the actions of the senses and the mind, "
    "let him practice yoga for the purification of the self."
)
T[(6, 13)] = (
    "Holding the body, head, and neck erect and still, "
    "gazing at the tip of his own nose, not looking in any direction,"
)
T[(6, 14)] = (
    "with serene self, fearless, firm in the vow of celibacy, mind restrained, "
    "his thoughts fixed on Me, let him sit, yoked, intent on Me as the supreme."
)
T[(6, 15)] = (
    "Ever yoking himself thus, the yogi of disciplined mind attains the peace "
    "abiding in Me, which ends in nirvana."
)
T[(6, 16)] = (
    "Yoga is not for him who eats too much, nor for him who eats nothing at all; "
    "not for him who sleeps too much, nor for him who keeps awake, O Arjuna."
)
T[(6, 17)] = (
    "For him whose food and recreation are measured, whose effort in actions is measured, "
    "whose sleep and waking are measured — yoga is the destroyer of sorrow."
)
T[(6, 18)] = (
    "When the disciplined mind is established in the Self alone, free from longing for any desire — "
    "then is one said to be yoked."
)
T[(6, 19)] = (
    "As a lamp in a windless place does not flicker — "
    "this simile is used for the yoked mind of the yogi practicing concentration on the Self."
)
T[(6, 20)] = (
    "That state in which the mind ceases, restrained by the practice of yoga, "
    "in which, seeing the Self by the Self, one is satisfied in the Self;"
)
T[(6, 21)] = (
    "that in which he knows that infinite bliss, grasped by the intellect, beyond the senses, "
    "and wherein, established, he never wanders from the truth;"
)
T[(6, 22)] = (
    "that, which having gained, he thinks there is no greater gain; "
    "established in which, he is not shaken even by heavy sorrow;"
)
T[(6, 23)] = (
    "that severance from the union with pain should be known as yoga. "
    "This yoga is to be practiced with resolute heart and without despondency."
)
T[(6, 24)] = (
    "Abandoning, without reserve, all desires born of intention, "
    "restraining the whole host of senses with the mind on every side,"
)
T[(6, 25)] = (
    "let him gradually become quiet by the intellect held firm. "
    "With the mind fixed on the Self, let him not think of anything."
)
T[(6, 26)] = (
    "Whatever makes the wavering and unsteady mind wander away — "
    "from that let him restrain it, bring it back under the control of the Self alone."
)
T[(6, 27)] = (
    "Supreme bliss indeed comes to the yogi whose mind is perfectly peaceful, "
    "whose passion is stilled, who has become Brahman, free from stain."
)
T[(6, 28)] = (
    "Thus constantly yoking the self, the yogi, his sins cast off, "
    "easily attains the infinite bliss of contact with Brahman."
)
T[(6, 29)] = (
    "He whose self is yoked in yoga, who sees the same everywhere, "
    "sees the Self abiding in all beings, and all beings in the Self."
)
T[(6, 30)] = (
    "He who sees Me everywhere and sees all in Me — "
    "for him I am not lost, and he is not lost to Me."
)
T[(6, 31)] = (
    "He who, established in oneness, worships Me as abiding in all beings — "
    "that yogi, however he dwells, dwells in Me."
)
T[(6, 32)] = (
    "He who, by the analogy with his own self, O Arjuna, sees equality everywhere, "
    "whether in pleasure or in pain — he is regarded as the highest yogi."
)
T[(6, 33)] = (
    "Arjuna said:\n"
    "O Madhusudana, this yoga of evenness which You have declared — "
    "I do not see its firm abiding, because of the restlessness of the mind."
)
T[(6, 34)] = (
    "The mind is indeed restless, O Krishna, turbulent, strong, and obstinate. "
    "To control it, I think, is as hard as to control the wind."
)
T[(6, 35)] = (
    "The Blessed Lord said:\n"
    "Undoubtedly, O mighty-armed one, the mind is hard to restrain and restless. "
    "But by practice (abhyasa), O son of Kunti, and by dispassion (vairagya), it is brought under control."
)
T[(6, 36)] = (
    "Yoga is hard to attain, I agree, for one whose self is unsubdued. "
    "But by him who strives, his self subdued, it can be attained by means."
)
T[(6, 37)] = (
    "Arjuna said:\n"
    "He who strives with faith, but whose mind wanders away from yoga, "
    "and who does not attain perfection in yoga — what path, O Krishna, does he tread?"
)
T[(6, 38)] = (
    "Fallen from both, does he not perish like a rent cloud, O mighty-armed one, "
    "without support, deluded on the path of Brahman?"
)
T[(6, 39)] = (
    "O Krishna, please dispel completely this doubt of mine. "
    "None other than You can be found to dispel this doubt."
)
T[(6, 40)] = (
    "The Blessed Lord said:\n"
    "O Partha, neither in this world nor in the next does he perish. "
    "None who does good, My son, ever comes to grief."
)
T[(6, 41)] = (
    "Having reached the worlds of the righteous and dwelt there for countless years, "
    "he who has fallen from yoga is born in the home of the pure and the prosperous."
)
T[(6, 42)] = (
    "Or he may even be born into a family of wise yogis. "
    "Such a birth as this is very hard to attain in the world."
)
T[(6, 43)] = (
    "There he regains the understanding acquired in his former body "
    "and strives once again, O joy of the Kurus, for perfection."
)
T[(6, 44)] = (
    "By that very former practice he is carried on, even against his will. "
    "One who merely inquires about yoga surpasses the one who follows only the Word of the Vedas."
)
T[(6, 45)] = (
    "But the yogi, striving with diligence, purified of his sins, "
    "perfected through many births, then attains the supreme goal."
)
T[(6, 46)] = (
    "The yogi is greater than the ascetics, greater even than those of knowledge, "
    "greater than the ritualists. Therefore be a yogi, O Arjuna."
)
T[(6, 47)] = (
    "And of all yogis, he who, full of faith, worships Me with his inmost self absorbed in Me — "
    "him I consider most deeply yoked."
)


# ============================================================================
# CHAPTER 7 — Jnana Vijnana Yoga (30 verses)
# Krishna's two prakritis (lower material, higher living); He as the thread
# on which all this is strung; His maya and those who cross it; the four
# types of devotees.
# ============================================================================

T[(7, 1)] = (
    "The Blessed Lord said:\n"
    "O Partha, with mind fixed on Me, taking refuge in Me, practicing yoga, "
    "hear how you shall know Me fully, without doubt."
)
T[(7, 2)] = (
    "I shall declare to you in full this knowledge together with realization, "
    "knowing which nothing further remains to be known here."
)
T[(7, 3)] = (
    "Among thousands of men, scarcely one strives for perfection; "
    "even among those who strive and are perfected, scarcely one knows Me in truth."
)
T[(7, 4)] = (
    "Earth, water, fire, air, ether, mind, intellect, and the sense of 'I' — "
    "thus is My prakriti divided eightfold."
)
T[(7, 5)] = (
    "This is the lower. But know, O mighty-armed one, My other, higher prakriti — "
    "the life-principle (jiva) by which this universe is upheld."
)
T[(7, 6)] = (
    "Know that all beings have these two as their source. "
    "I am the origin of the entire universe, and also its dissolution."
)
T[(7, 7)] = (
    "There is nothing whatever higher than Me, O Dhananjaya. "
    "All this is strung on Me like rows of jewels on a thread."
)
T[(7, 8)] = (
    "O son of Kunti, I am the taste in water, the light in the moon and the sun, "
    "the sacred syllable Om in all the Vedas, the sound in space, manliness in men."
)
T[(7, 9)] = (
    "I am the sweet fragrance of the earth, the brilliance in fire; "
    "the life in all beings, the austerity in ascetics."
)
T[(7, 10)] = (
    "Know Me, O Partha, as the eternal seed of all beings. "
    "I am the intelligence of the intelligent, the splendor of the splendid."
)
T[(7, 11)] = (
    "I am the strength of the strong, devoid of desire and passion. "
    "In beings, O bull of the Bharatas, I am desire that is not contrary to dharma."
)
T[(7, 12)] = (
    "Whatever states of being there are, of sattva, rajas, and tamas — "
    "know them to come from Me alone. But I am not in them; they are in Me."
)
T[(7, 13)] = (
    "Deluded by these three states of the gunas, this whole world does not recognize Me, "
    "who am beyond them, imperishable."
)
T[(7, 14)] = (
    "This divine maya of Mine, consisting of the gunas, is hard to cross over. "
    "They who take refuge in Me alone cross over this maya."
)
T[(7, 15)] = (
    "The evildoers, the deluded, the lowest of men, do not take refuge in Me; "
    "their knowledge is carried away by maya; they cling to demonic nature."
)
T[(7, 16)] = (
    "Four kinds of virtuous men worship Me, O Arjuna: "
    "the distressed, the seeker of knowledge, the seeker of wealth, and the wise, O bull of the Bharatas."
)
T[(7, 17)] = (
    "Of them, the wise man, ever yoked, devoted to the One, excels. "
    "To the wise I am exceedingly dear, and he is dear to Me."
)
T[(7, 18)] = (
    "All these are noble; but the wise I hold to be My very Self. "
    "For he, with steady mind, is established in Me alone, the supreme goal."
)
T[(7, 19)] = (
    "At the end of many births, the man of knowledge takes refuge in Me, "
    "seeing 'Vasudeva is all this.' Such a great soul is very hard to find."
)
T[(7, 20)] = (
    "Those whose knowledge is carried away by this and that desire resort to other deities, "
    "adopting various practices, constrained by their own nature."
)
T[(7, 21)] = (
    "Whatever form any devotee with faith desires to worship — "
    "that same faith I make steady in him."
)
T[(7, 22)] = (
    "Endowed with that faith, he strives for the grace of that deity; "
    "and from that he obtains those desired fruits — ordained by Me alone."
)
T[(7, 23)] = (
    "But the fruit that accrues to them, men of small understanding, is finite. "
    "Worshippers of the gods go to the gods; My devotees come to Me."
)
T[(7, 24)] = (
    "The foolish regard Me, the unmanifest, as having come into manifestation, "
    "not knowing My higher, imperishable, and supreme nature."
)
T[(7, 25)] = (
    "I am not manifest to all, veiled as I am by My yoga-maya. "
    "This deluded world does not know Me, the unborn, the imperishable."
)
T[(7, 26)] = (
    "O Arjuna, I know the beings of the past, present, and future; "
    "but no one knows Me."
)
T[(7, 27)] = (
    "Deluded by the pairs of opposites that arise from desire and aversion, O Bharata, "
    "all beings in creation are bewildered, O scorcher of foes."
)
T[(7, 28)] = (
    "But those of virtuous action, whose sin has come to an end, "
    "freed from the delusion of the pairs of opposites, worship Me with firm vows."
)
T[(7, 29)] = (
    "Those who strive for liberation from old age and death, taking refuge in Me — "
    "they know Brahman entire, the Adhyatma (the Self), and all action."
)
T[(7, 30)] = (
    "Those who know Me as the Adhibhuta (principle of beings), the Adhidaiva (of gods), "
    "and the Adhiyajna (of sacrifices), with yoked mind, know Me even at the hour of death."
)


# ============================================================================
# CHAPTER 8 — Akshara Brahma Yoga (28 verses)
# Definitions of Brahman, Adhyatma, Karma, Adhibhuta, Adhidaiva, Adhiyajna;
# the final thought at death; the path of light and the path of smoke;
# the day and night of Brahma.
# ============================================================================

T[(8, 1)] = (
    "Arjuna said:\n"
    "What is that Brahman? What is the Adhyatma? What is action, O best of men? "
    "What is said to be the Adhibhuta? And what is called the Adhidaiva?"
)
T[(8, 2)] = (
    "What is the Adhiyajna here, and how, in this body, O Madhusudana? "
    "And how, at the hour of death, are You to be known by the self-controlled?"
)
T[(8, 3)] = (
    "The Blessed Lord said:\n"
    "The Imperishable is the supreme Brahman; its nature is called Adhyatma; "
    "the offering that causes the origination of beings is called karma."
)
T[(8, 4)] = (
    "The Adhibhuta is the perishable nature; the Adhidaiva is the Purusha (cosmic Person); "
    "the Adhiyajna here in the body is I Myself, O best of the embodied."
)
T[(8, 5)] = (
    "He who, at the hour of death, remembering Me alone, leaves the body and departs, "
    "attains My state of being — of this there is no doubt."
)
T[(8, 6)] = (
    "Whatever state of being one remembers at the last moment when leaving the body — "
    "to that very one he goes, O son of Kunti, ever reflected upon."
)
T[(8, 7)] = (
    "Therefore at all times remember Me and fight. "
    "With mind and intellect fixed on Me, you shall surely come to Me."
)
T[(8, 8)] = (
    "He whose mind, yoked by the practice of yoga, does not wander to anything else, "
    "reaches the supreme Divine Purusha, O Partha, meditating upon Him."
)
T[(8, 9)] = (
    "He who meditates on the omniscient, the ancient, the ruler, smaller than the smallest, "
    "the sustainer of all, of inconceivable form, sun-colored, beyond darkness,"
)
T[(8, 10)] = (
    "at the hour of death, with a steady mind, yoked by devotion and by the power of yoga, "
    "drawing the life-breath fully between the eyebrows — he reaches the Supreme Divine Purusha."
)
T[(8, 11)] = (
    "That which the knowers of the Vedas call the Imperishable, that which the self-controlled ascetics, "
    "free from passion, enter; desiring which they practice celibacy — that goal I shall briefly declare."
)
T[(8, 12)] = (
    "Closing all the gates of the body, confining the mind in the heart, "
    "fixing the life-breath in the head, established in yogic concentration,"
)
T[(8, 13)] = (
    "uttering the one-syllabled Om, which is Brahman, remembering Me, "
    "he who departs, giving up the body, attains the supreme goal."
)
T[(8, 14)] = (
    "He who always remembers Me without thinking of anything else — "
    "for that ever-yoked yogi, I am easy to reach, O Partha."
)
T[(8, 15)] = (
    "The great souls who have come to Me, having attained the highest perfection, "
    "are not reborn in this impermanent abode of suffering."
)
T[(8, 16)] = (
    "From the world of Brahma (the creator) downwards, all worlds are subject to return, O Arjuna. "
    "But on attaining Me, O son of Kunti, there is no rebirth."
)
T[(8, 17)] = (
    "Those who know that the day of Brahma lasts a thousand yugas, "
    "and that his night also extends to a thousand yugas — they are the knowers of day and night."
)
T[(8, 18)] = (
    "At the coming of day, all manifestations issue forth from the unmanifest; "
    "at the coming of night, they dissolve into that very same unmanifest."
)
T[(8, 19)] = (
    "This same multitude of beings, coming forth again and again, "
    "helplessly dissolves at the coming of night, O Partha, and comes forth at the coming of day."
)
T[(8, 20)] = (
    "But beyond this unmanifest is another unmanifest, eternal Being, "
    "which does not perish when all beings perish."
)
T[(8, 21)] = (
    "That unmanifest, called the Imperishable, is declared to be the supreme goal. "
    "Attaining which they do not return — that is My supreme abode."
)
T[(8, 22)] = (
    "O Partha, that Supreme Purusha, in whom all beings abide and by whom all this is pervaded, "
    "is attainable by undivided devotion alone."
)
T[(8, 23)] = (
    "Now I shall declare the times at which yogis depart, O bull of the Bharatas, "
    "to return or not to return."
)
T[(8, 24)] = (
    "Fire, light, the day, the bright fortnight, the six months of the northern course — "
    "departing then, the knowers of Brahman go to Brahman."
)
T[(8, 25)] = (
    "Smoke, night, the dark fortnight, the six months of the southern course — "
    "the yogi attaining by these the moon's light returns."
)
T[(8, 26)] = (
    "These two paths of the world — the bright and the dark — are considered eternal. "
    "By one, one goes to non-return; by the other, one returns again."
)
T[(8, 27)] = (
    "Knowing these two paths, O Partha, no yogi is deluded. "
    "Therefore, at all times, be yoked in yoga, O Arjuna."
)
T[(8, 28)] = (
    "Whatever fruit of merit is declared for the study of the Vedas, for sacrifices, austerities, and gifts — "
    "the yogi, knowing this, transcends all these and attains the supreme, primal abode."
)


# ============================================================================
# CHAPTER 9 — Raja Vidya Yoga (34 verses)
# The "king of sciences, king of secrets": Krishna pervades all without being
# contained; He treats all devotees equally; even the worst sinner, turning
# to Him with single-minded devotion, is quickly redeemed.
# ============================================================================

T[(9, 1)] = (
    "The Blessed Lord said:\n"
    "To you, who do not cavil, I shall declare this most profound secret — "
    "knowledge combined with realization — knowing which you shall be freed from evil."
)
T[(9, 2)] = (
    "This is the king of sciences, the king of secrets, the supreme purifier; "
    "it is realizable by direct experience, accords with dharma, easy to practice, imperishable."
)
T[(9, 3)] = (
    "Men who have no faith in this dharma, O scorcher of foes, "
    "fail to reach Me, and return to the path of the cycle of death."
)
T[(9, 4)] = (
    "By Me, in My unmanifest form, all this world is pervaded. "
    "All beings abide in Me, but I do not abide in them."
)
T[(9, 5)] = (
    "And yet beings do not abide in Me — behold My divine yoga! "
    "Sustaining beings and not abiding in them, My Self is the cause of beings."
)
T[(9, 6)] = (
    "As the mighty wind, moving everywhere, ever abides in the ether, "
    "so all beings abide in Me — know this."
)
T[(9, 7)] = (
    "All beings, O son of Kunti, enter into My prakriti at the end of a kalpa; "
    "at the beginning of the next kalpa, I send them forth again."
)
T[(9, 8)] = (
    "Taking hold of My own prakriti, I send forth again and again "
    "this entire multitude of beings, helpless under the sway of nature."
)
T[(9, 9)] = (
    "But these actions do not bind Me, O Dhananjaya, "
    "seated as if indifferent, unattached to those actions."
)
T[(9, 10)] = (
    "With Me as overseer, prakriti produces the moving and the unmoving. "
    "For this reason, O son of Kunti, the world revolves."
)
T[(9, 11)] = (
    "Fools disregard Me when I have taken a human body, "
    "not knowing My higher state as the great Lord of beings."
)
T[(9, 12)] = (
    "Of futile hopes, futile actions, futile knowledge, without discernment, "
    "they are filled with the deluding nature of rakshasas and asuras."
)
T[(9, 13)] = (
    "But the great souls, O Partha, partaking of the divine nature, "
    "worship Me with undistracted mind, knowing Me as the imperishable source of beings."
)
T[(9, 14)] = (
    "Always glorifying Me, striving, firm in vows, "
    "bowing down to Me with devotion, ever-yoked, they worship Me."
)
T[(9, 15)] = (
    "Others, sacrificing by the yajna of knowledge, worship Me as the One, "
    "as distinct, as in many forms, facing everywhere."
)
T[(9, 16)] = (
    "I am the ritual, I am the sacrifice, I am the ancestral offering, I am the herb; "
    "I am the mantra, I am the clarified butter, I am the fire, I am the oblation."
)
T[(9, 17)] = (
    "I am the father of this world, the mother, the sustainer, the grandsire, "
    "the knowable, the purifier, the sacred syllable Om, and also the Rik, the Sama, and the Yajus."
)
T[(9, 18)] = (
    "I am the goal, the sustainer, the master, the witness, the abode, the shelter, the friend; "
    "the origin, the dissolution, the ground, the treasure-house, the imperishable seed."
)
T[(9, 19)] = (
    "I give heat; I hold back and pour forth the rain. "
    "I am immortality as well as death; I am both being and non-being, O Arjuna."
)
T[(9, 20)] = (
    "The knowers of the three Vedas, the soma-drinkers, their sins cleansed, "
    "worshipping Me by sacrifices, pray for the way to heaven; "
    "reaching the pure world of the lord of gods, they taste in heaven the divine pleasures of the gods."
)
T[(9, 21)] = (
    "Having enjoyed that vast heavenly world, on the exhaustion of their merit, "
    "they enter the mortal world. Thus, following the dharma of the three Vedas, "
    "desiring enjoyments, they obtain only what goes and returns."
)
T[(9, 22)] = (
    "For those who, thinking of no other, worship Me as ever-united, "
    "I provide what they lack and preserve what they have."
)
T[(9, 23)] = (
    "Even those devotees of other gods who worship them with faith — "
    "they too, O son of Kunti, worship Me alone, though not according to the rule."
)
T[(9, 24)] = (
    "For I alone am the enjoyer and Lord of all sacrifices. "
    "But they do not recognize Me in truth, and so they fall."
)
T[(9, 25)] = (
    "Worshippers of the gods go to the gods; to the ancestors go the ancestor-worshippers; "
    "to the bhutas go the worshippers of bhutas; and My worshippers come to Me."
)
T[(9, 26)] = (
    "Whoever offers Me with devotion a leaf, a flower, a fruit, water — "
    "that, offered with devotion by the pure-minded, I accept."
)
T[(9, 27)] = (
    "Whatever you do, whatever you eat, whatever you offer in sacrifice, whatever you give, "
    "whatever austerity you practice — do that, O son of Kunti, as an offering to Me."
)
T[(9, 28)] = (
    "Thus you shall be freed from the bonds of action, from its good and evil fruits. "
    "With your self yoked in the yoga of renunciation, liberated, you shall come to Me."
)
T[(9, 29)] = (
    "I am the same in all beings; none is hateful nor dear to Me. "
    "But those who worship Me with devotion — they are in Me, and I am in them."
)
T[(9, 30)] = (
    "Even if the most evildoer worships Me with undivided devotion, "
    "he is to be regarded as righteous, for he has resolved rightly."
)
T[(9, 31)] = (
    "Quickly he becomes righteous in soul and attains lasting peace. "
    "O son of Kunti, know for certain that My devotee never perishes."
)
T[(9, 32)] = (
    "Even those who are of sinful birth, O Partha — women, vaishyas, and shudras — "
    "taking refuge in Me, attain the supreme goal."
)
T[(9, 33)] = (
    "How much more, then, holy brahmanas and devoted royal sages! "
    "Having come to this impermanent and sorrowful world, worship Me."
)
T[(9, 34)] = (
    "Fix your mind on Me, be devoted to Me, sacrifice to Me, bow down to Me. "
    "Yoking yourself thus, with Me as your supreme goal, to Me you shall come."
)


# ============================================================================
# CHAPTER 10 — Vibhuti Yoga (42 verses)
# Krishna as the origin of all; His divine manifestations (vibhutis) in
# nature, scripture, and human life; of any class, He is its most excellent
# instance.
# ============================================================================

T[(10, 1)] = (
    "The Blessed Lord said:\n"
    "Again, O mighty-armed one, hear My supreme word, "
    "which I shall speak to you, who are dear to Me, desiring your welfare."
)
T[(10, 2)] = (
    "Neither the hosts of gods nor the great sages know My origin; "
    "for I am the source, in every way, of the gods and the great rishis."
)
T[(10, 3)] = (
    "He who knows Me, unborn, without beginning, the great Lord of the worlds — "
    "he, undeluded among men, is freed from all sins."
)
T[(10, 4)] = (
    "Discrimination, knowledge, freedom from delusion, patience, truthfulness, self-control, calmness, "
    "pleasure, pain, existence, non-existence, fear, and also fearlessness;"
)
T[(10, 5)] = (
    "non-injury, equanimity, contentment, austerity, charity, fame, infamy — "
    "these various dispositions of beings arise from Me alone."
)
T[(10, 6)] = (
    "The seven great sages and the four ancient (Manus), partaking of My nature, "
    "were born of My mind. From them have come these creatures in the world."
)
T[(10, 7)] = (
    "He who knows in truth this glory and yoga of Mine — "
    "he is yoked in unshakable yoga. Of this there is no doubt."
)
T[(10, 8)] = (
    "I am the source of all; from Me everything proceeds. "
    "Knowing this, the wise, full of devotion, worship Me."
)
T[(10, 9)] = (
    "With their thoughts fixed on Me, with their life surrendered to Me, "
    "enlightening one another, ever speaking of Me, they are satisfied and rejoice."
)
T[(10, 10)] = (
    "To them, ever yoked, worshipping Me with love, "
    "I give the yoga of discrimination by which they come to Me."
)
T[(10, 11)] = (
    "Out of compassion for them, I, dwelling in their own self, "
    "destroy the darkness born of ignorance with the shining lamp of knowledge."
)
T[(10, 12)] = (
    "Arjuna said:\n"
    "You are the supreme Brahman, the supreme abode, the supreme purifier — "
    "the eternal divine Person, the primal God, unborn, all-pervading."
)
T[(10, 13)] = (
    "All the sages say this of You, and so too the divine sage Narada, "
    "Asita, Devala, and Vyasa; and You Yourself tell me so."
)
T[(10, 14)] = (
    "I hold all this that You have told me to be true, O Keshava. "
    "Neither the gods nor the demons, O Lord, know Your manifestation."
)
T[(10, 15)] = (
    "You alone know Yourself by Yourself, O supreme Person, "
    "source of beings, Lord of beings, God of gods, Lord of the world."
)
T[(10, 16)] = (
    "Please declare in full Your divine vibhutis, "
    "by which vibhutis You pervade these worlds and abide."
)
T[(10, 17)] = (
    "How shall I know You, O Yogin, by constant meditation? "
    "In what various aspects are You, O Lord, to be meditated upon by me?"
)
T[(10, 18)] = (
    "O Janardana, tell me again in full of Your yoga and Your vibhutis; "
    "for I am never satiated hearing Your nectar-like words."
)
T[(10, 19)] = (
    "The Blessed Lord said:\n"
    "Well, I shall declare to you My divine vibhutis — only the principal ones, O best of the Kurus; "
    "for there is no end to the detail of My manifestation."
)
T[(10, 20)] = (
    "I am the Self, O Gudakesha, seated in the hearts of all beings. "
    "I am the beginning, the middle, and also the end of all beings."
)
T[(10, 21)] = (
    "Of the Adityas I am Vishnu; of lights, the radiant sun; "
    "of the Maruts I am Marichi; of stars (nakshatras), I am the moon."
)
T[(10, 22)] = (
    "Of the Vedas I am the Sama; of the gods, I am Indra; "
    "of the senses I am the mind; in living beings I am consciousness."
)
T[(10, 23)] = (
    "Of the Rudras I am Shankara; of yakshas and rakshasas, I am Kubera; "
    "of the Vasus I am Agni; of mountains, I am Meru."
)
T[(10, 24)] = (
    "Know Me, O Partha, the chief of household priests, as Brihaspati. "
    "Of generals I am Skanda; of bodies of water, I am the ocean."
)
T[(10, 25)] = (
    "Of the great rishis I am Bhrigu; of utterances, I am the single syllable Om. "
    "Of sacrifices I am the japa (silent repetition); of the immovable, the Himalayas."
)
T[(10, 26)] = (
    "Of all trees I am the Ashvattha; of the divine rishis, Narada; "
    "of the gandharvas, Chitraratha; of the perfected, the sage Kapila."
)
T[(10, 27)] = (
    "Of horses know Me to be Ucchaisravas, born from the churning for nectar; "
    "of lordly elephants, Airavata; of men, the king."
)
T[(10, 28)] = (
    "Of weapons I am the thunderbolt; of cows, Kamadhenu; "
    "of begetters I am Kandarpa (the god of love); of serpents, I am Vasuki."
)
T[(10, 29)] = (
    "Of nagas I am Ananta; of water-beings, Varuna; "
    "of the ancestors, Aryaman; among rulers, I am Yama."
)
T[(10, 30)] = (
    "Of the daityas I am Prahlada; of reckoners, Time; "
    "of beasts, the king of beasts (lion); of birds, the son of Vinata (Garuda)."
)
T[(10, 31)] = (
    "Of purifiers I am the wind; of warriors, Rama; "
    "of fishes I am the makara; of rivers, I am the Ganga."
)
T[(10, 32)] = (
    "Of creations I am the beginning, the end, and also the middle, O Arjuna. "
    "Of sciences I am the knowledge of the Self; in disputants, I am the debate."
)
T[(10, 33)] = (
    "Of letters I am the letter 'A'; of compounds, I am the dvandva (pair). "
    "I alone am imperishable Time; I am the dispenser facing all directions."
)
T[(10, 34)] = (
    "I am all-devouring Death, and the origin of what is yet to be; "
    "of feminine qualities: fame, fortune, speech, memory, intelligence, constancy, forbearance."
)
T[(10, 35)] = (
    "Of hymns likewise I am the Brihat-saman; of meters, I am Gayatri; "
    "of months I am Margashirsha; of seasons, the flowering spring."
)
T[(10, 36)] = (
    "I am the gambling of the cheats, the splendor of the splendid; "
    "I am victory, I am determination, I am the goodness of the good."
)
T[(10, 37)] = (
    "Of the Vrishnis I am Vasudeva; of the Pandavas, Dhananjaya; "
    "of sages I am Vyasa; among poets, Ushanas the poet."
)
T[(10, 38)] = (
    "Of those who chastise, I am the rod; of those who seek victory, I am statecraft. "
    "Of secrets I am silence; I am the knowledge of the knowers."
)
T[(10, 39)] = (
    "Whatever is the seed of all beings, that am I, O Arjuna. "
    "There is no being, moving or unmoving, that could exist without Me."
)
T[(10, 40)] = (
    "There is no end to My divine vibhutis, O scorcher of foes. "
    "This is only a brief statement by Me, an instance of the expanse of My glory."
)
T[(10, 41)] = (
    "Whatever being there is that is glorious, prosperous, or mighty — "
    "know that every such one has sprung from a fragment of My splendor."
)
T[(10, 42)] = (
    "But what use is it for you to know all this in detail, O Arjuna? "
    "I stand supporting this entire universe with a single fragment of Myself."
)


# ============================================================================
# CHAPTER 11 — Vishvarupa Darshana Yoga (55 verses)
# Arjuna asks to see the Lord's cosmic form; Krishna grants divine sight;
# the overwhelming theophany, gods, sages, and all worlds seen within Him;
# Time devouring the warriors; Arjuna's terror and plea to return to the
# gentle human form.
# ============================================================================

T[(11, 1)] = (
    "Arjuna said:\n"
    "As a favor to me, You have spoken of the supreme secret known as the Self; "
    "by those words of Yours, my delusion is dispelled."
)
T[(11, 2)] = (
    "O lotus-eyed one, I have heard from You in detail of the origin and dissolution of beings, "
    "and also of Your imperishable majesty."
)
T[(11, 3)] = (
    "So it is, O supreme Lord, just as You have declared Yourself. "
    "I desire to see Your Ishvara form, O supreme Person."
)
T[(11, 4)] = (
    "If You think, O Lord, that it can be seen by me, "
    "then, O Lord of yoga, show me Your imperishable Self."
)
T[(11, 5)] = (
    "The Blessed Lord said:\n"
    "Behold, O Partha, My forms, by hundreds and thousands, of various kinds, "
    "divine, of many colors and shapes."
)
T[(11, 6)] = (
    "Behold the Adityas, the Vasus, the Rudras, the two Ashvins, and the Maruts. "
    "Behold, O Bharata, many wonders never seen before."
)
T[(11, 7)] = (
    "Here today behold the whole universe, moving and unmoving, united in My body, O Gudakesha, "
    "and whatever else you wish to see."
)
T[(11, 8)] = (
    "But you cannot see Me with this, your own eye. "
    "I give you a divine eye — behold My sovereign yoga!"
)
T[(11, 9)] = (
    "Sanjaya said:\n"
    "Having spoken thus, O king, the great Lord of yoga, Hari, "
    "revealed to Partha His supreme Ishvara form:"
)
T[(11, 10)] = (
    "with many mouths and eyes, with many wondrous sights, "
    "with many divine ornaments, with many divine weapons uplifted;"
)
T[(11, 11)] = (
    "wearing divine garlands and robes, anointed with divine perfumes, "
    "all-wonderful, effulgent, infinite, with faces on every side."
)
T[(11, 12)] = (
    "If the splendor of a thousand suns were to blaze forth all at once in the sky, "
    "it might resemble the splendor of that Great Soul."
)
T[(11, 13)] = (
    "There Pandava saw the entire universe, in its manifold divisions, "
    "gathered together in one, in the body of that God of gods."
)
T[(11, 14)] = (
    "Then, filled with astonishment, his hair standing on end, Dhananjaya, "
    "bowing down his head before the Lord, with folded hands, said:"
)
T[(11, 15)] = (
    "Arjuna said:\n"
    "O God, I see all the gods in Your body, and all the hosts of beings — "
    "Brahma the Lord seated on the lotus-seat, all the rishis, and the divine serpents."
)
T[(11, 16)] = (
    "With many arms, bellies, mouths, and eyes, I behold You, of infinite form on every side. "
    "I see neither Your end, nor middle, nor beginning, O Lord of the universe, O Form universal."
)
T[(11, 17)] = (
    "I see You with crown, club, and discus — a mass of splendor blazing on all sides, "
    "hard to see on every side, with the brilliance of blazing fire and sun, immeasurable."
)
T[(11, 18)] = (
    "You are the Imperishable, the supreme to be known; You are the final resting-place of this universe. "
    "You are the imperishable guardian of the eternal dharma; You, I hold, are the primal Person."
)
T[(11, 19)] = (
    "Without beginning, middle, or end, of infinite power, of numberless arms, "
    "with the sun and moon for eyes, with blazing fire for mouth, scorching this universe with Your radiance — I see You."
)
T[(11, 20)] = (
    "This space between heaven and earth and all the directions are pervaded by You alone. "
    "Seeing this wondrous, terrible form of Yours, the three worlds tremble, O Great Soul."
)
T[(11, 21)] = (
    "Into You enter the hosts of gods. Some, in fear, with folded hands, praise You. "
    "The great rishis and the perfected, crying 'May it be well!', glorify You with abundant hymns."
)
T[(11, 22)] = (
    "The Rudras, Adityas, Vasus, and Sadhyas, the Vishvedevas, the two Ashvins, the Maruts, the ancestors, "
    "the hosts of gandharvas, yakshas, asuras, and siddhas — they all gaze upon You in wonder."
)
T[(11, 23)] = (
    "Seeing Your great form, of many mouths and eyes, O mighty-armed one, of many arms, thighs, and feet, "
    "of many bellies, of many fearsome tusks — the worlds tremble, and so do I."
)
T[(11, 24)] = (
    "Seeing You touching the sky, blazing with many colors, with gaping mouths and great, flaming eyes, "
    "my inmost soul trembles; I find neither firmness nor peace, O Vishnu."
)
T[(11, 25)] = (
    "Seeing Your mouths terrible with tusks, like the fires of cosmic dissolution, "
    "I know not the directions, nor do I find any refuge. Be gracious, O Lord of gods, O Abode of the worlds."
)
T[(11, 26)] = (
    "Into You rush all the sons of Dhritarashtra, together with the hosts of kings; "
    "Bhishma, Drona, and the charioteer's son (Karna) as well, and also our chief warriors,"
)
T[(11, 27)] = (
    "rush hastening into Your mouths, fearsome with tusks, terrifying to see. "
    "Some, clinging in the gaps between the tusks, are seen with their heads crushed to powder."
)
T[(11, 28)] = (
    "As the many torrents of rivers rush toward the ocean alone, "
    "so these heroes of the world of men enter Your flaming mouths."
)
T[(11, 29)] = (
    "As moths, with quickened speed, enter a blazing fire for their destruction, "
    "so do these creatures enter Your mouths with quickened speed for their destruction."
)
T[(11, 30)] = (
    "Swallowing all the worlds on every side with Your flaming mouths, You lick them up. "
    "Filling the whole universe with Your radiance, Your fierce rays burn, O Vishnu."
)
T[(11, 31)] = (
    "Tell me who You are, O fearsome-formed one — I bow to You, O best of gods; be gracious. "
    "I wish to know You, the primal one, for I understand not Your purpose."
)
T[(11, 32)] = (
    "The Blessed Lord said:\n"
    "I am Time, mighty destroyer of the worlds, set to destroy the worlds. "
    "Even without you, none of these warriors arrayed in the opposing armies shall live."
)
T[(11, 33)] = (
    "Therefore arise; win fame. Defeat your enemies and enjoy a prosperous kingdom. "
    "By Me these have already been slain; be you merely the outward cause, O left-handed archer."
)
T[(11, 34)] = (
    "Drona, Bhishma, Jayadratha, Karna, and the other warrior-heroes — they are slain by Me. "
    "Do you slay them! Do not tremble. Fight! You shall conquer your enemies in battle."
)
T[(11, 35)] = (
    "Sanjaya said:\n"
    "Having heard this speech of Keshava, Kiriti (Arjuna), trembling, hands folded, bowing down, "
    "spoke again to Krishna, stammering, overcome with fear, prostrating himself:"
)
T[(11, 36)] = (
    "Arjuna said:\n"
    "Rightly, O Hrishikesha, the world delights and rejoices in Your praise; "
    "the rakshasas, afraid, flee in all directions; all the hosts of the perfected bow down to You."
)
T[(11, 37)] = (
    "And why should they not bow down to You, O Great Soul — greater than Brahma, the first creator? "
    "O infinite Lord of gods, refuge of the worlds, You are the Imperishable, being and non-being and what is beyond."
)
T[(11, 38)] = (
    "You are the primal Deity, the ancient Person; You are the supreme resting-place of this universe. "
    "You are the knower and the to-be-known, the supreme goal. By You is this universe pervaded, O Form of infinite forms."
)
T[(11, 39)] = (
    "You are Vayu, Yama, Agni, Varuna, the Moon, Prajapati, the great grandsire. "
    "Salutation to You a thousand times; again and again, salutation, salutation to You!"
)
T[(11, 40)] = (
    "Salutation to You from the front and from behind; salutation to You on every side, O All; "
    "infinite in valor, of immeasurable might, You pervade all — therefore You are all."
)
T[(11, 41)] = (
    "Whatever I said rashly, whether in madness or in love, addressing You as 'O Krishna,' 'O Yadava,' 'O friend' — "
    "thinking You a friend, not knowing this Your greatness,"
)
T[(11, 42)] = (
    "and whatever disrespect I showed You in jest, while playing, resting, sitting, or at meals, "
    "alone or in the presence of others — O Unshaken One, I beg forgiveness from You, the immeasurable."
)
T[(11, 43)] = (
    "You are the father of the world, of the moving and unmoving; its object of worship, its most venerable teacher. "
    "There is none equal to You — how could there be one greater? — in the three worlds, O incomparable Power."
)
T[(11, 44)] = (
    "Therefore, prostrating myself and bowing down my body, I beg Your grace, O adorable Lord. "
    "As father to son, as friend to friend, as beloved to beloved — please bear with me, O God."
)
T[(11, 45)] = (
    "Seeing what was never seen before, I am filled with joy; yet my mind is shaken with fear. "
    "Show me, O God, that other form. Be gracious, O Lord of gods, O Abode of the worlds."
)
T[(11, 46)] = (
    "I wish to see You even as before, with crown, club, and discus in hand. "
    "Assume that four-armed form, O thousand-armed one, O Form universal."
)
T[(11, 47)] = (
    "The Blessed Lord said:\n"
    "By My grace, O Arjuna, this supreme form has been shown to you, by My own yogic power — "
    "luminous, universal, infinite, primal — which none but you has ever seen."
)
T[(11, 48)] = (
    "Not by study of the Vedas, nor by sacrifices, nor by gifts, nor by rituals, nor by severe austerities, "
    "can I be seen in such a form in the world of men by any other than you, O hero of the Kurus."
)
T[(11, 49)] = (
    "Be not afraid, nor bewildered, on beholding this terrible form of Mine. "
    "Freed from fear, with gladdened heart, behold again this other form of Mine."
)
T[(11, 50)] = (
    "Sanjaya said:\n"
    "Having spoken thus to Arjuna, Vasudeva showed him again His own form; "
    "and the Great Soul, assuming once more His gentle form, consoled the frightened one."
)
T[(11, 51)] = (
    "Arjuna said:\n"
    "Seeing this Your gentle human form, O Janardana, "
    "my thoughts are now composed; I am restored to my own nature."
)
T[(11, 52)] = (
    "The Blessed Lord said:\n"
    "This form of Mine that you have seen is very hard to behold. "
    "Even the gods are ever eager to behold this form."
)
T[(11, 53)] = (
    "Not by the Vedas, nor by austerities, nor by gifts, nor by sacrifice, "
    "am I to be seen in the form in which you have seen Me."
)
T[(11, 54)] = (
    "But by undivided devotion, O Arjuna, I can thus be known, truly seen, "
    "and entered into, O scorcher of foes."
)
T[(11, 55)] = (
    "He who does work for Me, who holds Me as his supreme goal, who is devoted to Me, "
    "free from attachment, without enmity toward any being — he comes to Me, O Pandava."
)


# ============================================================================
# CHAPTER 12 — Bhakti Yoga (20 verses)
# Which is better: the worship of the manifest personal God or the
# unmanifest Absolute? Krishna favors the former as easier; the marks of
# the beloved devotee.
# ============================================================================

T[(12, 1)] = (
    "Arjuna said:\n"
    "Those devotees who, ever-yoked, worship You, and those who worship the imperishable Unmanifest — "
    "of these, who are the better knowers of yoga?"
)
T[(12, 2)] = (
    "The Blessed Lord said:\n"
    "Those who, fixing their mind on Me, ever-yoked, worship Me endowed with supreme faith — "
    "them I regard as the most deeply yoked."
)
T[(12, 3)] = (
    "But those who worship the Imperishable — the Indefinable, the Unmanifest, the Omnipresent, "
    "the Unthinkable, the Unchanging, the Immovable, the Constant —"
)
T[(12, 4)] = (
    "controlling the senses, of even-minded everywhere, delighting in the welfare of all beings — "
    "they too attain Me alone."
)
T[(12, 5)] = (
    "The trouble is greater for those whose minds are fixed on the unmanifest; "
    "for the goal of the unmanifest is attained with difficulty by the embodied."
)
T[(12, 6)] = (
    "But those who, surrendering all actions to Me, intent on Me, "
    "worship Me, meditating on Me with undivided yoga —"
)
T[(12, 7)] = (
    "of those whose mind has entered into Me, I am soon the redeemer "
    "from the ocean of the mortal cycle, O Partha."
)
T[(12, 8)] = (
    "Fix your mind on Me alone; let your intellect dwell in Me. "
    "Thereafter, without doubt, you shall dwell in Me alone."
)
T[(12, 9)] = (
    "But if you cannot fix your mind steadily on Me, "
    "then seek to reach Me through the practice of yoga, O Dhananjaya."
)
T[(12, 10)] = (
    "If you are incapable even of practice, devote yourself to working for Me. "
    "Even performing actions for My sake, you shall attain perfection."
)
T[(12, 11)] = (
    "If you are unable to do even this, then taking refuge in yoga in Me, "
    "give up the fruits of all action, self-controlled."
)
T[(12, 12)] = (
    "Knowledge is indeed superior to practice; meditation is superior to knowledge; "
    "renunciation of the fruit of action to meditation; from such renunciation, peace immediately follows."
)
T[(12, 13)] = (
    "He who hates no creature, who is friendly and compassionate to all, "
    "free from the sense of 'mine' and 'I,' even-minded in pleasure and pain, forgiving;"
)
T[(12, 14)] = (
    "ever content, yoked, self-controlled, of firm resolve, "
    "with mind and intellect offered to Me — he, My devotee, is dear to Me."
)
T[(12, 15)] = (
    "He by whom the world is not disturbed, and who is not disturbed by the world, "
    "free from delight, anger, fear, and agitation — he too is dear to Me."
)
T[(12, 16)] = (
    "He who is not dependent, pure, skillful, unconcerned, untroubled, "
    "renouncing all undertakings — he, My devotee, is dear to Me."
)
T[(12, 17)] = (
    "He who neither rejoices nor hates, neither grieves nor desires, "
    "renouncing both good and evil, full of devotion — he is dear to Me."
)
T[(12, 18)] = (
    "The same to foe and friend, the same in honor and dishonor, "
    "the same in cold and heat, in pleasure and pain, free from attachment;"
)
T[(12, 19)] = (
    "to whom blame and praise are equal, silent, content with anything, homeless, "
    "of steady mind, full of devotion — that man is dear to Me."
)
T[(12, 20)] = (
    "But those who follow this nectar of dharma as declared, with faith, holding Me as the supreme goal — "
    "the devotees, they are exceedingly dear to Me."
)


# ============================================================================
# CHAPTER 13 — Kshetra Kshetrajna Vibhaga Yoga (35 verses)
# The field (kshetra = body/prakriti) and the knower of the field
# (kshetrajna = Purusha); the components of the field; the marks of true
# knowledge; the description of the supreme knowable (Brahman); the
# interplay of Purusha and Prakriti.
# ============================================================================

T[(13, 1)] = (
    "Arjuna said:\n"
    "Prakriti and Purusha, the field (kshetra) and the knower of the field (kshetrajna), "
    "knowledge and that which is to be known — these I desire to know, O Keshava."
)
T[(13, 2)] = (
    "The Blessed Lord said:\n"
    "This body, O son of Kunti, is called the field; "
    "him who knows this, the knowers of truth call the knower of the field."
)
T[(13, 3)] = (
    "Know Me also, O Bharata, as the knower of the field in every field. "
    "The knowledge of the field and its knower — that I hold to be true knowledge."
)
T[(13, 4)] = (
    "What this field is, of what nature, of what modifications, whence it is, "
    "who He (its knower) is and what His powers — hear from Me briefly."
)
T[(13, 5)] = (
    "This has been sung in many ways by the rishis, distinctly in various hymns, "
    "and in the well-reasoned, decisive verses of the Brahma-sutras."
)
T[(13, 6)] = (
    "The great elements, egoism, intellect, the unmanifest (prakriti), "
    "the ten senses and the one (mind), and the five fields of the senses;"
)
T[(13, 7)] = (
    "desire, aversion, pleasure, pain, the aggregate (body), intelligence, steadfastness — "
    "this, in brief, is described as the field with its modifications."
)
T[(13, 8)] = (
    "Absence of pride, absence of hypocrisy, non-injury, forbearance, uprightness, "
    "service to the teacher, purity, steadiness, self-control;"
)
T[(13, 9)] = (
    "dispassion toward the objects of the senses, and absence of egoism; "
    "insight into the evils of birth, death, old age, sickness, and pain;"
)
T[(13, 10)] = (
    "non-attachment, non-identification with son, wife, home, and the rest; "
    "and constant evenness of mind in the happening of the desirable and the undesirable;"
)
T[(13, 11)] = (
    "and unswerving devotion to Me by the yoga of non-separation; "
    "resort to solitary places, distaste for the company of men;"
)
T[(13, 12)] = (
    "constancy in the knowledge of the Self, and insight into the end of the knowledge of truth — "
    "this is declared to be knowledge; what is opposed to it is ignorance."
)
T[(13, 13)] = (
    "I shall declare that which is to be known, by knowing which one attains immortality — "
    "the beginningless supreme Brahman, which is said to be neither being nor non-being."
)
T[(13, 14)] = (
    "With hands and feet everywhere, with eyes, heads, and faces everywhere, "
    "with ears on all sides — it stands enveloping everything in the world."
)
T[(13, 15)] = (
    "Appearing to have the qualities of all the senses, yet free from all senses; "
    "unattached, yet supporting all; free from the gunas, yet the experiencer of the gunas."
)
T[(13, 16)] = (
    "Within and without all beings; the unmoving and also the moving; "
    "because of its subtlety, it is incomprehensible; it is far and yet near."
)
T[(13, 17)] = (
    "Undivided, yet It seems to stand divided in beings; "
    "It is to be known as the supporter of beings — their devourer and their creator."
)
T[(13, 18)] = (
    "The Light of lights, It is said to be beyond darkness; "
    "It is Knowledge, the Knowable, the Goal of knowledge — seated in the hearts of all."
)
T[(13, 19)] = (
    "Thus the field, knowledge, and the knowable have been briefly declared. "
    "My devotee, knowing this, attains to My state of being."
)
T[(13, 20)] = (
    "Know both Prakriti and Purusha to be without beginning. "
    "Know also that modifications and the gunas are born of Prakriti."
)
T[(13, 21)] = (
    "Prakriti is said to be the cause in the production of cause and effect (bodily activities); "
    "Purusha is said to be the cause in the experience of pleasure and pain."
)
T[(13, 22)] = (
    "For Purusha, seated in Prakriti, experiences the gunas born of Prakriti. "
    "Attachment to the gunas is the cause of his birth in good and evil wombs."
)
T[(13, 23)] = (
    "The supreme Purusha in this body is also called the spectator, the permitter, "
    "the sustainer, the experiencer, the great Lord, the supreme Self."
)
T[(13, 24)] = (
    "He who thus knows Purusha and Prakriti together with the gunas, "
    "however he may be engaged, is not born again."
)
T[(13, 25)] = (
    "Some by meditation behold the Self in themselves by the self; "
    "others by the yoga of Sankhya, and others by the yoga of action."
)
T[(13, 26)] = (
    "Yet others, not knowing, worship as they have heard from others; "
    "they too cross beyond death, clinging to what they have heard."
)
T[(13, 27)] = (
    "Whatever being is born, moving or unmoving, know that, O best of the Bharatas, "
    "to arise from the union of the field and the knower of the field."
)
T[(13, 28)] = (
    "He who sees the supreme Lord dwelling equally in all beings, "
    "imperishable among the perishing — he truly sees."
)
T[(13, 29)] = (
    "For seeing the same Lord established everywhere, "
    "he does not destroy the Self by the self, and therefore attains the supreme goal."
)
T[(13, 30)] = (
    "He who sees that all action is performed by Prakriti alone, "
    "and that the Self is therefore a non-doer — he truly sees."
)
T[(13, 31)] = (
    "When he sees the diverse states of beings as abiding in the One, "
    "and their expansion from That alone — then he attains Brahman."
)
T[(13, 32)] = (
    "Because of being without beginning and without qualities, this imperishable supreme Self, "
    "O son of Kunti, though dwelling in the body, neither acts nor is tainted."
)
T[(13, 33)] = (
    "As the all-pervading ether, because of its subtlety, is not tainted, "
    "so the Self, seated everywhere in the body, is not tainted."
)
T[(13, 34)] = (
    "As the one sun illumines this whole world, "
    "so the Lord of the field (the Self) illumines the entire field, O Bharata."
)
T[(13, 35)] = (
    "Those who thus perceive, by the eye of knowledge, the distinction between the field and the knower of the field, "
    "and the liberation of beings from Prakriti — they attain the Supreme."
)


# ============================================================================
# CHAPTER 14 — Gunatraya Vibhaga Yoga (27 verses)
# The three gunas (sattva, rajas, tamas) — their natures, how each binds,
# how each manifests at death, how to transcend them; the marks of the
# gunatita (one who has transcended the gunas).
# ============================================================================

T[(14, 1)] = (
    "The Blessed Lord said:\n"
    "Again I shall declare the supreme knowledge, the best of all knowledge, "
    "knowing which all sages have passed from this world to supreme perfection."
)
T[(14, 2)] = (
    "Resorting to this knowledge, having come to identity with Me, "
    "they are not born at the creation, nor troubled at the dissolution."
)
T[(14, 3)] = (
    "My womb is the great Brahman (prakriti); in it I place the seed. "
    "From that, O Bharata, is the birth of all beings."
)
T[(14, 4)] = (
    "Whatever forms come forth from all wombs, O son of Kunti, "
    "of these, the great Brahman is the womb; I am the seed-giving father."
)
T[(14, 5)] = (
    "Sattva, rajas, and tamas — these gunas, born of Prakriti, O mighty-armed one, "
    "bind in the body the imperishable embodied one."
)
T[(14, 6)] = (
    "Among these, sattva, because of its purity, is illuminating and free from disease; "
    "it binds, O sinless one, by attachment to happiness and by attachment to knowledge."
)
T[(14, 7)] = (
    "Know rajas to be of the nature of passion, the source of thirst and attachment. "
    "It binds, O son of Kunti, the embodied by attachment to action."
)
T[(14, 8)] = (
    "Know tamas to be born of ignorance, the deluder of all embodied beings. "
    "It binds, O Bharata, through heedlessness, indolence, and sleep."
)
T[(14, 9)] = (
    "Sattva attaches to happiness, rajas to action, O Bharata; "
    "but tamas, veiling knowledge, attaches to heedlessness."
)
T[(14, 10)] = (
    "Sattva arises overcoming rajas and tamas, O Bharata; "
    "rajas, overcoming sattva and tamas; and tamas, overcoming sattva and rajas."
)
T[(14, 11)] = (
    "When the light of knowledge streams forth at all the gates of this body, "
    "then it should be known that sattva is predominant."
)
T[(14, 12)] = (
    "Greed, activity, undertaking of actions, restlessness, longing — "
    "these are born when rajas is predominant, O bull of the Bharatas."
)
T[(14, 13)] = (
    "Darkness, inactivity, heedlessness, and delusion — "
    "these arise when tamas is predominant, O joy of the Kurus."
)
T[(14, 14)] = (
    "If the embodied one goes to dissolution when sattva prevails, "
    "then he attains the pure worlds of those who know the Supreme."
)
T[(14, 15)] = (
    "Going to dissolution in rajas, he is born among those attached to action; "
    "and dissolving in tamas, he is born in the wombs of the deluded."
)
T[(14, 16)] = (
    "The fruit of good action is said to be sattvic and pure; "
    "the fruit of rajas is pain; the fruit of tamas is ignorance."
)
T[(14, 17)] = (
    "From sattva arises knowledge; from rajas, greed; "
    "from tamas arise heedlessness, delusion, and ignorance."
)
T[(14, 18)] = (
    "Those established in sattva go upwards; those in rajas remain in the middle; "
    "those in tamas, abiding in the function of the lowest guna, go downwards."
)
T[(14, 19)] = (
    "When the seer perceives no agent other than the gunas, "
    "and knows that which is higher than the gunas — he attains to My state of being."
)
T[(14, 20)] = (
    "Transcending these three gunas, the source of the body, the embodied one, "
    "freed from birth, death, old age, and pain, attains immortality."
)
T[(14, 21)] = (
    "Arjuna said:\n"
    "By what marks, O Lord, is he known who has transcended these three gunas? "
    "What is his conduct, and how does he pass beyond these three gunas?"
)
T[(14, 22)] = (
    "The Blessed Lord said:\n"
    "O Pandava, he who does not hate illumination, activity, or delusion when present, "
    "nor longs for them when absent;"
)
T[(14, 23)] = (
    "he who, seated as if indifferent, is not shaken by the gunas; "
    "who, thinking 'the gunas act,' stands firm and does not waver;"
)
T[(14, 24)] = (
    "the same in pleasure and pain, self-contained, to whom a clod, stone, and gold are alike, "
    "the same to the dear and the undear, steadfast, the same in blame and praise of himself;"
)
T[(14, 25)] = (
    "the same in honor and dishonor, the same to friend and foe, "
    "abandoning all undertakings — he is said to have transcended the gunas."
)
T[(14, 26)] = (
    "He who serves Me with unswerving yoga of devotion — "
    "crossing beyond the gunas, he becomes fit to become Brahman."
)
T[(14, 27)] = (
    "For I am the abode of Brahman, the immortal and imperishable, "
    "of eternal dharma, and of absolute bliss."
)


# ============================================================================
# CHAPTER 15 — Purushottama Yoga (20 verses)
# The inverted ashvattha tree of samsara; cutting it with the axe of
# detachment; the jiva enters and departs carrying the senses; the three
# Purushas — perishable, imperishable, and the Supreme (Purushottama).
# ============================================================================

T[(15, 1)] = (
    "The Blessed Lord said:\n"
    "They speak of the imperishable ashvattha (peepul) tree, with its roots above and branches below; "
    "its leaves are the Vedic hymns. He who knows it, knows the Vedas."
)
T[(15, 2)] = (
    "Below and above its branches spread, nourished by the gunas; the objects of sense are its twigs. "
    "Below, also, its roots stretch forth, giving rise to action in the world of men."
)
T[(15, 3)] = (
    "Its form is not perceived here as such — neither its end, nor its beginning, nor its foundation. "
    "Cutting this firmly-rooted ashvattha with the strong axe of non-attachment,"
)
T[(15, 4)] = (
    "one should seek that place, reaching which they do not return: "
    "'I take refuge in that primal Person from whom the ancient stream of activity has flowed.'"
)
T[(15, 5)] = (
    "Free from pride and delusion, having conquered the evil of attachment, ever dwelling in the Self, "
    "desires withdrawn, freed from the pairs of opposites known as pleasure and pain — "
    "the undeluded reach that imperishable abode."
)
T[(15, 6)] = (
    "Neither the sun, nor the moon, nor fire illumines that place; "
    "having reached which they do not return — that is My supreme abode."
)
T[(15, 7)] = (
    "An eternal part of Me, becoming a jiva in the world of living beings, "
    "draws to itself the mind and the five senses resting in Prakriti."
)
T[(15, 8)] = (
    "When the Lord (of the body) takes up a body and when He departs from it, "
    "He takes these and goes, as the wind carries scents from their places."
)
T[(15, 9)] = (
    "Presiding over the ear, eye, touch, taste, smell, and also the mind, "
    "he experiences the objects of the senses."
)
T[(15, 10)] = (
    "Whether departing or remaining, or experiencing, united with the gunas — "
    "the deluded do not see; but those who possess the eye of knowledge see."
)
T[(15, 11)] = (
    "The striving yogis also see Him seated in themselves; "
    "but the unintelligent, with uncultivated selves, though striving, do not see Him."
)
T[(15, 12)] = (
    "That radiance of the sun that illumines the whole world, "
    "and which is in the moon and in fire — know that radiance to be Mine."
)
T[(15, 13)] = (
    "Entering the earth, I sustain all beings with My energy. "
    "Becoming the sap-full moon, I nourish all plants."
)
T[(15, 14)] = (
    "Becoming the fire Vaishvanara that dwells in the body of breathing creatures, "
    "joining the prana and apana, I digest the fourfold food."
)
T[(15, 15)] = (
    "And I am seated in the hearts of all; from Me come memory, knowledge, and their loss. "
    "I alone am to be known through all the Vedas; I am the author of Vedanta, and the knower of the Vedas."
)
T[(15, 16)] = (
    "There are these two persons (purushas) in the world — the perishable and the imperishable. "
    "The perishable is all creatures; the imperishable is called the unchanging (kutastha)."
)
T[(15, 17)] = (
    "But the highest Person is another, called the supreme Self, "
    "the imperishable Lord who, entering the three worlds, sustains them."
)
T[(15, 18)] = (
    "Since I transcend the perishable, and am higher even than the imperishable, "
    "I am celebrated in the world and in the Veda as Purushottama (the Supreme Person)."
)
T[(15, 19)] = (
    "He who, undeluded, thus knows Me as Purushottama, "
    "knows all; he worships Me with all his being, O Bharata."
)
T[(15, 20)] = (
    "Thus, O sinless one, this most secret teaching has been declared by Me. "
    "Having understood this, one becomes wise, and has fulfilled all his duties, O Bharata."
)


# ============================================================================
# CHAPTER 16 — Daivasura Sampad Vibhaga Yoga (24 verses)
# The divine and demoniac endowments; the nature, conduct, and destiny of
# those with the demoniac disposition; three gates to hell; the authority
# of scripture.
# ============================================================================

T[(16, 1)] = (
    "The Blessed Lord said:\n"
    "Fearlessness, purity of heart, steadfastness in the yoga of knowledge, "
    "charity, self-restraint, sacrifice, study of scripture, austerity, uprightness;"
)
T[(16, 2)] = (
    "non-injury, truthfulness, absence of anger, renunciation, tranquility, absence of calumny, "
    "compassion for beings, freedom from covetousness, gentleness, modesty, freedom from fickleness;"
)
T[(16, 3)] = (
    "vigor, forgiveness, fortitude, purity, freedom from malice, absence of pride — "
    "these belong to one born with the divine endowment, O Bharata."
)
T[(16, 4)] = (
    "Ostentation, arrogance, self-conceit, anger, harshness, and ignorance — "
    "these belong, O Partha, to one born with the demoniac endowment."
)
T[(16, 5)] = (
    "The divine endowment leads to liberation; the demoniac to bondage. "
    "Grieve not, O Pandava; you were born with the divine endowment."
)
T[(16, 6)] = (
    "There are two kinds of beings created in this world: the divine and the demoniac. "
    "The divine has been described at length; hear now from Me of the demoniac, O Partha."
)
T[(16, 7)] = (
    "Demoniac men know neither action nor abstention from action. "
    "Purity, good conduct, truth — none of these is in them."
)
T[(16, 8)] = (
    "'The world is without truth, without moral basis, without a Lord,' they say; "
    "'produced by mutual union, what else? — driven by lust.'"
)
T[(16, 9)] = (
    "Holding this view, these lost souls of little understanding and cruel deeds "
    "arise as enemies of the world for its destruction."
)
T[(16, 10)] = (
    "Clinging to insatiable lust, full of hypocrisy, pride, and arrogance, "
    "holding evil ideas through delusion, they engage in action with impure resolve."
)
T[(16, 11)] = (
    "Given over to immeasurable cares that end only with death, making the gratification of desires their highest aim, "
    "convinced that this is all —"
)
T[(16, 12)] = (
    "bound by hundreds of fetters of expectation, given over to lust and anger, "
    "they strive to amass wealth by unjust means, to gratify their desires."
)
T[(16, 13)] = (
    "'This has been gained by me today; this desire I shall fulfil. "
    "This is mine; this wealth shall also be mine hereafter.'"
)
T[(16, 14)] = (
    "'That enemy has been slain by me; and others also I shall slay. "
    "I am the lord; I am the enjoyer; I am successful, mighty, and happy.'"
)
T[(16, 15)] = (
    "'I am wealthy and well-born. Who else is equal to me? "
    "I shall sacrifice, I shall give, I shall rejoice' — thus deluded by ignorance,"
)
T[(16, 16)] = (
    "bewildered by many thoughts, caught in the net of delusion, "
    "attached to the gratification of desires, they fall into a foul hell."
)
T[(16, 17)] = (
    "Self-conceited, stubborn, full of the intoxication of wealth and pride, "
    "they perform sacrifices in name only, with hypocrisy, not according to the rule."
)
T[(16, 18)] = (
    "Resorting to egotism, power, insolence, lust, and anger, "
    "these malignant ones hate Me in their own bodies and in those of others."
)
T[(16, 19)] = (
    "These hateful and cruel evildoers, the lowest of men, "
    "I repeatedly hurl into demoniac wombs in the cycle of rebirths."
)
T[(16, 20)] = (
    "Entering demoniac wombs, the deluded, not attaining Me from birth to birth, "
    "thereafter go to the lowest state, O son of Kunti."
)
T[(16, 21)] = (
    "Threefold is the gate of hell, destructive of the self: lust, anger, and greed. "
    "Therefore one should abandon these three."
)
T[(16, 22)] = (
    "The man who is freed from these three gates of darkness, O son of Kunti, "
    "practices what is good for himself and thereby attains the supreme goal."
)
T[(16, 23)] = (
    "He who, casting aside the ordinance of the scriptures, acts under the impulse of desire, "
    "attains neither perfection, nor happiness, nor the supreme goal."
)
T[(16, 24)] = (
    "Therefore let the scripture be your authority in determining what should be done and what should not be done. "
    "Knowing what is enjoined by the rule of the scripture, you should perform action here."
)


# ============================================================================
# CHAPTER 17 — Shraddhatraya Vibhaga Yoga (28 verses)
# The three kinds of faith (sattvic, rajasic, tamasic); food, sacrifice,
# austerity, and charity in each; the meaning of Om Tat Sat.
# ============================================================================

T[(17, 1)] = (
    "Arjuna said:\n"
    "Those who, setting aside the ordinance of scripture, yet worship with faith — "
    "what is their state, O Krishna? Is it sattva, rajas, or tamas?"
)
T[(17, 2)] = (
    "The Blessed Lord said:\n"
    "The faith of the embodied is of three kinds, born of their own nature — "
    "sattvic, rajasic, and tamasic. Hear of it."
)
T[(17, 3)] = (
    "The faith of each is according to his own nature, O Bharata. "
    "A person is formed by his faith; as his faith is, so is he."
)
T[(17, 4)] = (
    "Sattvic men worship the gods; rajasic, the yakshas and rakshasas; "
    "tamasic folk worship ghosts and the hosts of bhutas."
)
T[(17, 5)] = (
    "Those who undertake fearsome austerities, not enjoined by scripture, "
    "bound by hypocrisy and egoism, impelled by the force of desire and passion,"
)
T[(17, 6)] = (
    "senseless, tormenting the group of elements in the body — and Me who dwell within the body — "
    "know them to be of demoniac resolve."
)
T[(17, 7)] = (
    "The food dear to each is also of three kinds, "
    "and so too sacrifice, austerity, and charity. Hear their distinction."
)
T[(17, 8)] = (
    "Foods that promote life, vitality, strength, health, happiness, and cheerfulness; "
    "that are savory, smooth, firm, and pleasing to the heart — these are dear to the sattvic."
)
T[(17, 9)] = (
    "Foods that are bitter, sour, salty, excessively hot, pungent, dry, and burning, "
    "causing pain, grief, and sickness — are dear to the rajasic."
)
T[(17, 10)] = (
    "Food that is stale, insipid, putrid, decayed, refuse, and impure "
    "is dear to the tamasic."
)
T[(17, 11)] = (
    "The sacrifice which is offered according to rule by those who do not desire its fruit, "
    "convinced that 'this is a duty to be performed' — that is sattvic."
)
T[(17, 12)] = (
    "But the sacrifice that is offered seeking its fruit, or for ostentation, O best of the Bharatas — "
    "know that to be rajasic."
)
T[(17, 13)] = (
    "A sacrifice which is contrary to the ordinance, in which no food is distributed, without sacred verses, without gifts, "
    "devoid of faith — they call tamasic."
)
T[(17, 14)] = (
    "Worship of the gods, the twice-born, teachers, and the wise; purity, uprightness, celibacy, and non-injury — "
    "these are called the austerity of the body."
)
T[(17, 15)] = (
    "Speech that causes no pain, truthful, pleasing and beneficial, "
    "and the regular recitation of the Vedas — these are called the austerity of speech."
)
T[(17, 16)] = (
    "Serenity of mind, gentleness, silence, self-control, and purity of disposition — "
    "this is called the austerity of the mind."
)
T[(17, 17)] = (
    "This threefold austerity, practiced with supreme faith by men who are yoked and do not desire fruit — "
    "they call sattvic."
)
T[(17, 18)] = (
    "The austerity that is practiced with hypocrisy for the sake of respect, honor, and reverence — "
    "is said to be rajasic, unstable and fleeting."
)
T[(17, 19)] = (
    "The austerity that is performed out of foolish notion, with torture of oneself, "
    "or for the ruin of another — is called tamasic."
)
T[(17, 20)] = (
    "That gift given with the thought 'it must be given,' to one who cannot repay, "
    "at the proper place, time, and to a worthy person — that gift is held to be sattvic."
)
T[(17, 21)] = (
    "That gift given grudgingly, or with the desire for a return, or for the sake of its fruit — "
    "is held to be rajasic."
)
T[(17, 22)] = (
    "The gift given at a wrong place and time, to unworthy persons, "
    "without respect, with contempt — is declared to be tamasic."
)
T[(17, 23)] = (
    "Om Tat Sat — this is declared to be the threefold designation of Brahman. "
    "By this, of old, were the brahmanas, the Vedas, and the sacrifices ordained."
)
T[(17, 24)] = (
    "Therefore, with 'Om' as the opening, acts of sacrifice, gift, and austerity "
    "as enjoined by the scriptures are always begun by the knowers of Brahman."
)
T[(17, 25)] = (
    "With 'Tat' uttered, without aim at fruit, the various acts of sacrifice and austerity "
    "and the acts of gift are performed by the seekers of liberation."
)
T[(17, 26)] = (
    "The word 'Sat' is used in the sense of reality and in the sense of goodness; "
    "and in an auspicious act also, O Partha, the word 'Sat' is used."
)
T[(17, 27)] = (
    "Steadiness in sacrifice, in austerity, and in gift is also called 'Sat'; "
    "and action for the sake of That is indeed called 'Sat.'"
)
T[(17, 28)] = (
    "Whatever is sacrificed, given, or performed, and whatever austerity is practiced without faith — "
    "it is called 'asat,' O Partha; it is nothing here, and nothing in the hereafter."
)


# ============================================================================
# CHAPTER 18 — Moksha Sanyasa Yoga (78 verses)
# The summation: tyaga (relinquishment) vs. sannyasa (renunciation); the
# three kinds of tyaga; the five factors of action; knowledge, action, and
# the agent in three forms each; the intellect, steadiness, happiness in
# three forms; svadharma; the final teaching — surrender all dharmas and
# take refuge in Me alone; Sanjaya's closing benediction.
# ============================================================================

T[(18, 1)] = (
    "Arjuna said:\n"
    "O mighty-armed one, I wish to know the truth of sannyasa (renunciation), O Hrishikesha, "
    "and of tyaga (relinquishment), O Keshinisudana, each separately."
)
T[(18, 2)] = (
    "The Blessed Lord said:\n"
    "The sages know sannyasa to be the giving up of desire-prompted actions; "
    "the wise call tyaga the relinquishment of the fruit of all actions."
)
T[(18, 3)] = (
    "Some thinkers say action should be abandoned as evil; "
    "others, that acts of sacrifice, gift, and austerity should not be abandoned."
)
T[(18, 4)] = (
    "Hear My decision on this matter of tyaga, O best of the Bharatas. "
    "Tyaga has been declared to be of three kinds, O tiger among men."
)
T[(18, 5)] = (
    "Acts of sacrifice, gift, and austerity are not to be abandoned, but are to be performed; "
    "for sacrifice, gift, and austerity are purifiers of the wise."
)
T[(18, 6)] = (
    "But even these actions should be performed abandoning attachment and fruits — "
    "this, O Partha, is My final and decisive opinion."
)
T[(18, 7)] = (
    "Verily the renunciation of obligatory action is not proper. "
    "Its relinquishment through delusion is declared to be tamasic."
)
T[(18, 8)] = (
    "He who abandons action merely because it is painful, from fear of bodily trouble — "
    "performs rajasic relinquishment; he does not obtain its fruit."
)
T[(18, 9)] = (
    "But when obligatory action is performed, O Arjuna, abandoning attachment and fruit, "
    "because it ought to be done — that relinquishment is considered sattvic."
)
T[(18, 10)] = (
    "The relinquisher, endowed with sattva, of steady intellect, whose doubts are rent, "
    "neither hates disagreeable action nor is attached to agreeable action."
)
T[(18, 11)] = (
    "It is not possible for the embodied to renounce actions without residue. "
    "But he who relinquishes the fruit of action — he is called the relinquisher."
)
T[(18, 12)] = (
    "Undesired, desired, and mixed — threefold is the fruit of action that accrues after death "
    "to those who have not relinquished; but there is no such fruit for the sannyasins."
)
T[(18, 13)] = (
    "Learn from Me, O mighty-armed one, these five causes declared in the Sankhya-siddhanta "
    "for the accomplishment of all actions:"
)
T[(18, 14)] = (
    "the body, the agent, the various instruments, "
    "the various and distinct activities, and divine providence as the fifth."
)
T[(18, 15)] = (
    "Whatever action a man undertakes with his body, speech, or mind, "
    "whether right or wrong — these five are its causes."
)
T[(18, 16)] = (
    "Therefore, he who, with an unformed intellect, looks upon the pure Self alone as the agent — "
    "that dull-witted one sees not."
)
T[(18, 17)] = (
    "He whose state is free from egoism, whose intellect is not tainted — "
    "though he slay these people, he slays not, nor is he bound."
)
T[(18, 18)] = (
    "The knower, the object of knowledge, and knowledge — this is the threefold impulse to action. "
    "The instrument, the action, and the agent — this is the threefold constituent of action."
)
T[(18, 19)] = (
    "Knowledge, action, and agent are declared in the Sankhya doctrine to be of three kinds only, "
    "according to the distinction of the gunas. Hear them duly also."
)
T[(18, 20)] = (
    "That knowledge by which one sees in all beings the one, imperishable Being, "
    "undivided in the divided — know that knowledge to be sattvic."
)
T[(18, 21)] = (
    "The knowledge which sees in all beings, by reason of differentiation, various entities of distinct kinds — "
    "know that knowledge to be rajasic."
)
T[(18, 22)] = (
    "But that which clings to one single effect as if it were the whole, without reason, "
    "not based on truth, and trivial — that is declared to be tamasic."
)
T[(18, 23)] = (
    "The obligatory action which is performed without attachment, without desire or hatred, "
    "by one who seeks no fruit — is declared to be sattvic."
)
T[(18, 24)] = (
    "But the action which is performed with great effort by one who seeks his desires "
    "or impelled by egoism — is declared to be rajasic."
)
T[(18, 25)] = (
    "The action undertaken through delusion, without regard to consequence, loss, injury, or ability — "
    "is declared to be tamasic."
)
T[(18, 26)] = (
    "Free from attachment, without speaking of 'I,' endowed with fortitude and vigor, "
    "unmoved in success and failure — the agent is called sattvic."
)
T[(18, 27)] = (
    "Passionate, desiring the fruit of action, greedy, harmful by nature, impure, "
    "full of joy and sorrow — the agent is declared rajasic."
)
T[(18, 28)] = (
    "Unyoked, vulgar, stubborn, deceitful, malicious, slothful, "
    "despondent, and procrastinating — the agent is called tamasic."
)
T[(18, 29)] = (
    "Now hear, O Dhananjaya, the threefold division of the intellect and of steadiness "
    "according to the gunas — being declared separately and fully."
)
T[(18, 30)] = (
    "The intellect which knows action and abstention from action, what ought to be done and what ought not, "
    "fear and fearlessness, bondage and liberation, O Partha — that is sattvic."
)
T[(18, 31)] = (
    "The intellect by which one incorrectly understands dharma and adharma, "
    "what ought to be done and what ought not — that, O Partha, is rajasic."
)
T[(18, 32)] = (
    "The intellect which, enveloped in darkness, conceives adharma as dharma, "
    "and sees all things inverted — that, O Partha, is tamasic."
)
T[(18, 33)] = (
    "The unswerving steadiness by which, through yoga, one restrains the functions of the mind, life-breaths, and senses — "
    "that steadiness, O Partha, is sattvic."
)
T[(18, 34)] = (
    "But the steadiness, O Arjuna, by which one holds fast to dharma, pleasure, and wealth, "
    "with attachment, craving the fruit — that steadiness is rajasic."
)
T[(18, 35)] = (
    "That by which a fool does not give up sleep, fear, grief, depression, and conceit — "
    "that steadiness, O Partha, is tamasic."
)
T[(18, 36)] = (
    "Now hear from Me, O bull of the Bharatas, the three kinds of happiness "
    "in which one rejoices through long practice, and comes to the end of pain."
)
T[(18, 37)] = (
    "That which is like poison at first but like nectar at the end, "
    "born of the clear insight of the Self — that happiness is declared sattvic."
)
T[(18, 38)] = (
    "That which at first, through the contact of the senses with their objects, is like nectar, "
    "but in the end like poison — that happiness is held to be rajasic."
)
T[(18, 39)] = (
    "That happiness which, both at the beginning and afterwards, deludes the self, "
    "arising from sleep, indolence, and heedlessness — is declared tamasic."
)
T[(18, 40)] = (
    "There is no being on earth, nor again in heaven among the gods, "
    "that is free from these three gunas born of Prakriti."
)
T[(18, 41)] = (
    "The duties of brahmanas, kshatriyas, vaishyas, and shudras, O scorcher of foes, "
    "are distributed according to the gunas born of their own nature."
)
T[(18, 42)] = (
    "Calmness, self-restraint, austerity, purity, forbearance, uprightness, "
    "knowledge, realization, faith in the next world — these are the duties of the brahmana, born of his nature."
)
T[(18, 43)] = (
    "Valor, splendor, fortitude, skill, not fleeing in battle, generosity, and lordliness — "
    "these are the duties of the kshatriya, born of his nature."
)
T[(18, 44)] = (
    "Agriculture, cattle-rearing, and trade are the duties of the vaishya, born of his nature. "
    "Action consisting of service is the duty of the shudra, born of his nature."
)
T[(18, 45)] = (
    "Engaged each in his own duty, man attains perfection. "
    "How one engaged in his own duty attains perfection — hear that."
)
T[(18, 46)] = (
    "From whom the activity of all beings proceeds, by whom all this is pervaded — "
    "worshipping Him by his own duty, man attains perfection."
)
T[(18, 47)] = (
    "Better is one's own dharma, though imperfect, than another's dharma well performed. "
    "Doing the action ordained by his own nature, one incurs no sin."
)
T[(18, 48)] = (
    "One should not abandon the duty to which one is born, O son of Kunti, though it be faulty; "
    "for all undertakings are enveloped by fault, as fire by smoke."
)
T[(18, 49)] = (
    "With intellect unattached everywhere, the self subdued, desire gone, "
    "one attains through renunciation the supreme perfection of freedom from action."
)
T[(18, 50)] = (
    "How one who has attained perfection reaches Brahman — that supreme consummation of knowledge — "
    "learn from Me, O son of Kunti, only in brief."
)
T[(18, 51)] = (
    "Endowed with a pure intellect, restraining the self by firmness, giving up sound and other objects, "
    "and casting aside attraction and aversion;"
)
T[(18, 52)] = (
    "dwelling in solitude, eating lightly, controlling body, speech, and mind, "
    "ever intent on the yoga of meditation, taking refuge in dispassion;"
)
T[(18, 53)] = (
    "abandoning egoism, force, arrogance, desire, anger, and possession; "
    "free from the sense of 'mine,' at peace — he becomes fit for becoming Brahman."
)
T[(18, 54)] = (
    "Having become Brahman, serene in self, he neither grieves nor desires. "
    "The same to all beings, he attains supreme devotion to Me."
)
T[(18, 55)] = (
    "By devotion he comes to know Me, how great I am and who I am in truth; "
    "then, having known Me in truth, he enters into Me at once."
)
T[(18, 56)] = (
    "Performing all actions, ever taking refuge in Me, "
    "by My grace he attains the eternal, imperishable abode."
)
T[(18, 57)] = (
    "Mentally renouncing all actions in Me, intent on Me as the highest goal, "
    "resorting to the yoga of the intellect, fix your mind ever on Me."
)
T[(18, 58)] = (
    "With your mind on Me, you shall, by My grace, cross over all obstacles. "
    "But if, through egoism, you will not listen, you shall perish."
)
T[(18, 59)] = (
    "If, clinging to egoism, you think 'I will not fight' — "
    "this resolve of yours is vain; Prakriti itself will constrain you."
)
T[(18, 60)] = (
    "Bound, O son of Kunti, by your own karma born of your nature, "
    "even what through delusion you wish not to do, you shall helplessly do."
)
T[(18, 61)] = (
    "The Lord dwells in the hearts of all beings, O Arjuna, "
    "causing all beings to revolve as if mounted on a machine, by His maya."
)
T[(18, 62)] = (
    "Take refuge in Him alone with all your being, O Bharata. "
    "By His grace you shall attain supreme peace and the eternal abode."
)
T[(18, 63)] = (
    "Thus has wisdom, more secret than any secret, been declared to you by Me. "
    "Reflecting on this fully, then do as you wish."
)
T[(18, 64)] = (
    "Hear again My supreme word, the most secret of all. "
    "You are dearly beloved of Me; therefore I shall speak for your welfare."
)
T[(18, 65)] = (
    "Fix your mind on Me, be devoted to Me, sacrifice to Me, bow down to Me. "
    "You shall come to Me alone; truly do I promise you — you are dear to Me."
)
T[(18, 66)] = (
    "Abandoning all dharmas, take refuge in Me alone. "
    "I shall liberate you from all sins. Do not grieve."
)
T[(18, 67)] = (
    "This is never to be told by you to one without austerity, nor to one without devotion, "
    "nor to one who does not wish to hear, nor to one who speaks ill of Me."
)
T[(18, 68)] = (
    "He who shall teach this supreme secret to My devotees, "
    "performing supreme devotion to Me, shall without doubt come to Me."
)
T[(18, 69)] = (
    "And among men, none shall do dearer service to Me than he; "
    "nor shall any on earth be more beloved by Me."
)
T[(18, 70)] = (
    "And he who shall study this righteous dialogue between us — "
    "by him I shall be worshipped through the sacrifice of knowledge; such is My conviction."
)
T[(18, 71)] = (
    "Even the man who, full of faith and without ill-will, should but hear it — "
    "he too, liberated, shall attain the auspicious worlds of those of meritorious deeds."
)
T[(18, 72)] = (
    "Has this been heard by you, O Partha, with a one-pointed mind? "
    "Has your delusion born of ignorance been destroyed, O Dhananjaya?"
)
T[(18, 73)] = (
    "Arjuna said:\n"
    "My delusion is destroyed; memory is regained by Your grace, O Achyuta. "
    "I stand free from doubt. I shall do Your word."
)
T[(18, 74)] = (
    "Sanjaya said:\n"
    "Thus I heard this dialogue between Vasudeva (Krishna) and the noble-souled Partha — "
    "wonderful and making the hair stand on end."
)
T[(18, 75)] = (
    "By the grace of Vyasa, I have heard this supreme secret of yoga "
    "directly from Krishna, the Lord of yoga, who declared it in person."
)
T[(18, 76)] = (
    "O king, as I recall again and again this wondrous and holy dialogue "
    "between Keshava and Arjuna, I rejoice again and again."
)
T[(18, 77)] = (
    "And as I recall again and again that most wondrous form of Hari, "
    "great is my wonder, O king, and I rejoice again and again."
)
T[(18, 78)] = (
    "Wherever is Krishna, the Lord of yoga, wherever is Partha, the wielder of the bow — "
    "there, I am convinced, are fortune, victory, prosperity, and sound policy."
)


def build():
    out = {
        "source_sanskrit": "bhagavad_gita_sanskrit.json",
        "script": "English",
        "translator": "Claude (Opus 4.7) — verse-by-verse translation from Devanagari Sanskrit",
        "notes": (
            "Faithful translation, not paraphrase. Speaker tags preserved. "
            "Philosophical terms (dharma, karma, yoga, atman, Brahman, guna) "
            "are retained in transliteration where English flattens the meaning."
        ),
        "chapters": [],
    }

    for ch in src["chapters"]:
        cn = ch["chapter_number"]
        ch_out = {
            "chapter_number": cn,
            "chapter_title_sanskrit": ch["chapter_title_sanskrit"],
            "chapter_title_english": CHAPTER_TITLES[cn],
            "verses": [],
        }
        for v in ch["verses"]:
            vn = v["verse_number"]
            ch_out["verses"].append({
                "verse_number": vn,
                "sanskrit": v["text"],
                "translation": T.get((cn, vn), None),
            })
        out["chapters"].append(ch_out)

    (ROOT / "bhagavad_gita_english.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2)
    )

    total = sum(len(c["verses"]) for c in out["chapters"])
    translated = sum(
        1 for c in out["chapters"] for v in c["verses"]
        if v["translation"] is not None
    )
    print(f"Total verses: {total}")
    print(f"Translated:   {translated}")
    print(f"Remaining:    {total - translated}")


if __name__ == "__main__":
    build()
