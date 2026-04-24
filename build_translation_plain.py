"""
Builds bhagavad_gita_english_plain.json — a plain, modern English translation
of all 701 verses, aimed at ordinary readers with no prior exposure to the
Gita or to Sanskrit.

Style rules:
- Everyday modern English. No "thee/thou," no "O son of Kunti."
- Speakers named plainly: "Krishna said," "Arjuna said," "Sanjaya said."
- Epithets (Partha, Hrishikesha, Madhava, Keshava) replaced with the name
  they refer to, unless the epithet carries meaning in context.
- Sanskrit terms translated, with the Sanskrit word in parentheses only
  where the concept is central and the English rendering is a compromise
  (dharma, karma, yoga, atman, Brahman, guna). Glossed at first use.
- Short sentences. Concrete verbs. No ornamental syntax.
- Meaning is preserved faithfully — this is simplified in form, not watered
  down in content.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent
src = json.loads((ROOT / "bhagavad_gita_sanskrit.json").read_text())

CHAPTER_TITLES = {
    1:  "Arjuna's Despair",
    2:  "The Way of Knowledge",
    3:  "The Way of Action",
    4:  "Knowledge, Action, and Letting Go",
    5:  "The Way of Renunciation",
    6:  "The Way of Meditation",
    7:  "Knowledge and Realization",
    8:  "The Imperishable Reality",
    9:  "The Royal Secret",
    10: "Divine Glories",
    11: "The Vision of the Cosmic Form",
    12: "The Way of Devotion",
    13: "The Body and the One Who Knows It",
    14: "The Three Qualities of Nature",
    15: "The Supreme Person",
    16: "Divine and Demonic Natures",
    17: "Three Kinds of Faith",
    18: "Freedom Through Letting Go",
}

T = {}

# ============================================================================
# CHAPTER 1 — Arjuna's Despair
# ============================================================================

T[(1, 1)] = (
    "Dhritarashtra said:\n"
    "Sanjaya, tell me — my sons and the sons of Pandu gathered on the sacred field "
    "of Kurukshetra, ready to fight. What did they do?"
)
T[(1, 2)] = (
    "Sanjaya said:\n"
    "Seeing the Pandava army drawn up for battle, King Duryodhana went to his teacher Drona "
    "and said:"
)
T[(1, 3)] = (
    "\"Look, teacher, at this great Pandava army, arranged by your own brilliant student, "
    "Drupada's son.\""
)
T[(1, 4)] = (
    "\"Here are heroes, mighty archers — a match in battle for Bhima and Arjuna — "
    "Yuyudhana, Virata, and Drupada, the great charioteer;\""
)
T[(1, 5)] = (
    "\"Dhrishtaketu, Chekitana, and the brave king of Kashi; "
    "Purujit, Kuntibhoja, and Shaibya, a leader of men;\""
)
T[(1, 6)] = (
    "\"the valiant Yudhamanyu, the powerful Uttamaujas, Subhadra's son, "
    "and Draupadi's sons — all great warriors.\""
)
T[(1, 7)] = (
    "\"Now let me name, O best of the twice-born, the best warriors on our side, "
    "the leaders of my army — listen:\""
)
T[(1, 8)] = (
    "\"You yourself, Bhishma, Karna, Kripa — all victorious in battle; "
    "Ashvatthama, Vikarna, and Somadatta's son;\""
)
T[(1, 9)] = (
    "\"and many other heroes, skilled with many weapons, all battle-tested "
    "and ready to die for me.\""
)
T[(1, 10)] = (
    "\"Our army, led by Bhishma, is immense; theirs, led by Bhima, is limited.\""
)
T[(1, 11)] = (
    "\"So all of you, holding your positions at every point in the formation, "
    "protect Bhishma above everyone else.\""
)
T[(1, 12)] = (
    "Then, to cheer Duryodhana, the old grandfather of the Kurus, Bhishma, "
    "roared like a lion and blew his conch loudly."
)
T[(1, 13)] = (
    "Then conches, kettledrums, tabors, trumpets, and horns blared out all at once — "
    "a tremendous noise."
)
T[(1, 14)] = (
    "Then, standing in their great chariot yoked to white horses, "
    "Krishna and Arjuna blew their divine conches."
)
T[(1, 15)] = (
    "Krishna blew his conch Panchajanya; Arjuna blew Devadatta; "
    "and Bhima of terrifying deeds blew the great conch Paundra."
)
T[(1, 16)] = (
    "King Yudhishthira blew Anantavijaya; "
    "Nakula and Sahadeva blew Sughosha and Manipushpaka."
)
T[(1, 17)] = (
    "The king of Kashi, a supreme archer; Shikhandi, the great warrior; "
    "Dhrishtadyumna, Virata, and the unconquered Satyaki;"
)
T[(1, 18)] = (
    "Drupada, the sons of Draupadi, and Subhadra's mighty son — "
    "O king, each of them blew his own conch."
)
T[(1, 19)] = (
    "That tremendous sound, echoing through sky and earth, "
    "shattered the hearts of Dhritarashtra's sons."
)
T[(1, 20)] = (
    "Then, seeing the enemy drawn up, with weapons about to clash, "
    "Arjuna, whose banner carried the image of Hanuman, raised his bow "
    "and said to Krishna:"
)
T[(1, 21)] = (
    "Arjuna said:\n"
    "Krishna, place my chariot between the two armies,"
)
T[(1, 22)] = (
    "so I can see the men standing here eager to fight — "
    "those I'm about to face in this battle."
)
T[(1, 23)] = (
    "I want to see who has gathered here to fight, "
    "those who came to serve the evil-minded Duryodhana."
)
T[(1, 24)] = (
    "Sanjaya said:\n"
    "Asked this by Arjuna, Krishna drove the splendid chariot "
    "into the space between the two armies,"
)
T[(1, 25)] = (
    "facing Bhishma, Drona, and all the kings of the earth, and said: "
    "\"Arjuna, look at these Kurus gathered here.\""
)
T[(1, 26)] = (
    "Arjuna looked and saw, standing in both armies, fathers and grandfathers, "
    "teachers, uncles, brothers, sons, grandsons, and friends,"
)
T[(1, 27)] = (
    "fathers-in-law and companions. Seeing all these relatives lined up for battle, "
    "Arjuna was overwhelmed with pity, and said in sorrow:"
)
T[(1, 28)] = (
    "Arjuna said:\n"
    "Krishna, seeing my own family here, ready to fight, "
    "my limbs give way and my mouth runs dry."
)
T[(1, 29)] = (
    "My body shakes, my hair stands on end, "
    "my bow Gandiva slips from my hand, and my skin is burning."
)
T[(1, 30)] = (
    "I can't stand steady; my mind is reeling. "
    "I see bad omens, Krishna."
)
T[(1, 31)] = (
    "I see nothing good in killing my own people in battle. "
    "I don't want victory, or a kingdom, or pleasures, Krishna."
)
T[(1, 32)] = (
    "What use is a kingdom to us, Govinda? What use are enjoyments or even life, "
    "when the very people for whose sake we want them"
)
T[(1, 33)] = (
    "are standing here ready to fight, giving up their lives and wealth — "
    "teachers, fathers, sons, grandfathers,"
)
T[(1, 34)] = (
    "uncles, fathers-in-law, grandsons, brothers-in-law, other relatives? "
    "Krishna, I don't want to kill them, even if they kill me — "
    "not for all three worlds, much less for this earth."
)
T[(1, 35)] = (
    "What joy would we get, Krishna, from killing Dhritarashtra's sons? "
    "Only sin would stain us, even though they are the aggressors."
)
T[(1, 36)] = (
    "So it's wrong for us to kill Dhritarashtra's sons — our own relatives. "
    "How could we be happy, Krishna, after killing our own family?"
)
T[(1, 37)] = (
    "Even if they, with minds clouded by greed, see nothing wrong "
    "in destroying a family or betraying friends —"
)
T[(1, 38)] = (
    "why shouldn't we, who clearly see the evil of destroying a family, "
    "turn away from this sin?"
)
T[(1, 39)] = (
    "When a family is destroyed, its ancient traditions are lost. "
    "When tradition is lost, lawlessness takes over the whole family."
)
T[(1, 40)] = (
    "When lawlessness dominates, the women become corrupted; "
    "and when women are corrupted, social order breaks down."
)
T[(1, 41)] = (
    "This confusion leads the destroyers of the family — and the family itself — to ruin, "
    "for the ancestors, deprived of the offerings due to them, also fall."
)
T[(1, 42)] = (
    "Through the sins of these family-destroyers, which cause the collapse of social order, "
    "the ancient customs of caste and family are uprooted."
)
T[(1, 43)] = (
    "Krishna, I've heard that people whose family traditions are destroyed "
    "are condemned to suffer for a long time."
)
T[(1, 44)] = (
    "How terrible — we're ready to commit a great sin, "
    "prepared to kill our own relatives out of greed for a kingdom."
)
T[(1, 45)] = (
    "It would be better for me if the sons of Dhritarashtra, weapons in hand, "
    "killed me in battle unarmed and not fighting back."
)
T[(1, 46)] = (
    "Sanjaya said:\n"
    "Having said this on the battlefield, Arjuna cast aside his bow and arrows "
    "and sank down on the seat of his chariot, his mind crushed by grief."
)
T[(1, 47)] = (
    "(In editions that count this as a separate verse:) "
    "So Arjuna, overcome with sorrow, threw down his bow and arrows "
    "and sat down on the chariot seat, his heart broken with grief."
)


# ============================================================================
# CHAPTER 2 — The Way of Knowledge
# The key chapter: the soul's immortality, Krishna's first teaching on
# acting without attachment to results, and the portrait of the person of
# steady wisdom (sthitaprajna).
# ============================================================================

T[(2, 1)] = (
    "Sanjaya said:\n"
    "To Arjuna — overcome with pity, eyes brimming and downcast, mind distressed — "
    "Krishna spoke these words:"
)
T[(2, 2)] = (
    "Krishna said:\n"
    "Where has this weakness come from, Arjuna, at such a critical moment? "
    "It doesn't suit a noble man. It won't bring heaven, and it won't bring honor."
)
T[(2, 3)] = (
    "Don't give in to this cowardice — it isn't you. "
    "Shake off this petty weakness of heart and stand up, Arjuna."
)
T[(2, 4)] = (
    "Arjuna said:\n"
    "Krishna, how can I shoot arrows at Bhishma and Drona on the battlefield? "
    "They deserve my respect, not my weapons."
)
T[(2, 5)] = (
    "Better to live by begging in this world than to kill these great teachers. "
    "If I kill them — even though they seek their own gain — everything I enjoy "
    "will be stained with their blood."
)
T[(2, 6)] = (
    "And I don't know which is better — that we defeat them or they defeat us. "
    "Those very sons of Dhritarashtra stand there, and if I kill them I won't want to live."
)
T[(2, 7)] = (
    "My mind is clouded by weak pity; I'm confused about what's right. "
    "Tell me clearly what's best for me. I am your student. Teach me — "
    "I take refuge in you."
)
T[(2, 8)] = (
    "I see nothing that can remove this grief drying up my senses — "
    "not even a prosperous kingdom on earth without rivals, nor lordship over the gods."
)
T[(2, 9)] = (
    "Sanjaya said:\n"
    "Having said this, Arjuna — the conqueror of sleep, the scorcher of enemies — "
    "told Krishna \"I will not fight,\" and fell silent."
)
T[(2, 10)] = (
    "O king, to Arjuna grieving between the two armies, "
    "Krishna, as if smiling, spoke these words:"
)
T[(2, 11)] = (
    "Krishna said:\n"
    "You grieve for those who should not be grieved for — and yet you speak words of wisdom. "
    "The wise grieve for neither the living nor the dead."
)
T[(2, 12)] = (
    "There was never a time when I did not exist, nor you, nor these kings. "
    "Nor will any of us cease to exist in the future."
)
T[(2, 13)] = (
    "Just as the soul within this body passes through childhood, youth, and old age, "
    "it passes into another body after death. The wise are not troubled by this."
)
T[(2, 14)] = (
    "Contact with the world brings cold and heat, pleasure and pain — "
    "they come and go, they don't last. Endure them, Arjuna."
)
T[(2, 15)] = (
    "The person these things don't disturb — the one steady in pleasure and pain — "
    "that wise person is ready for immortality."
)
T[(2, 16)] = (
    "What isn't real can never truly exist; what is real can never stop existing. "
    "Those who see the truth see both clearly."
)
T[(2, 17)] = (
    "Know that what pervades all this is indestructible. "
    "No one can destroy what does not pass away."
)
T[(2, 18)] = (
    "These bodies have an end — but the embodied one within them is eternal, "
    "indestructible, beyond measure. So fight, Arjuna."
)
T[(2, 19)] = (
    "Anyone who thinks the soul kills, or that the soul is killed — "
    "neither understands. The soul does not kill and is not killed."
)
T[(2, 20)] = (
    "The soul is never born and never dies. Once it exists, it does not cease to be. "
    "Unborn, eternal, everlasting, ancient — it is not killed when the body is killed."
)
T[(2, 21)] = (
    "Arjuna, if someone knows the soul is indestructible, eternal, unborn, unchanging — "
    "how can such a person kill anyone or cause anyone to kill?"
)
T[(2, 22)] = (
    "Just as a person throws away worn-out clothes and puts on new ones, "
    "the soul throws away worn-out bodies and takes on new ones."
)
T[(2, 23)] = (
    "Weapons cannot cut the soul, fire cannot burn it, "
    "water cannot wet it, wind cannot dry it."
)
T[(2, 24)] = (
    "It cannot be cut, burned, wetted, or dried. "
    "It is eternal, everywhere, stable, unmoving, forever."
)
T[(2, 25)] = (
    "The soul is beyond the reach of the senses, beyond thought, unchanging. "
    "Knowing this, you shouldn't grieve."
)
T[(2, 26)] = (
    "And even if you think the soul is constantly being born and dying, "
    "you still have no reason to grieve, Arjuna."
)
T[(2, 27)] = (
    "Whoever is born must die; whoever dies must be born again. "
    "There's no point grieving over the unavoidable."
)
T[(2, 28)] = (
    "Beings are unseen before they appear, visible in the middle, "
    "and unseen again when they go. Why grieve about this?"
)
T[(2, 29)] = (
    "Some look at the soul as a wonder; some speak of it as a wonder; "
    "others hear about it as a wonder — and even after hearing, no one truly knows it."
)
T[(2, 30)] = (
    "The one within every body is eternal and indestructible, Arjuna. "
    "So there's no reason to grieve for any living being."
)
T[(2, 31)] = (
    "Look at it from the standpoint of your own duty, and you won't hesitate. "
    "For a warrior there is nothing better than a righteous battle."
)
T[(2, 32)] = (
    "Fortunate are the warriors, Arjuna, who are offered a battle like this "
    "that comes of its own accord — an open door to heaven."
)
T[(2, 33)] = (
    "But if you refuse to fight this righteous battle, "
    "you'll abandon your duty and your honor — and you'll earn only sin."
)
T[(2, 34)] = (
    "People will speak of your lasting disgrace, "
    "and for an honored man, dishonor is worse than death."
)
T[(2, 35)] = (
    "The great warriors will think you withdrew out of fear, "
    "and those who once respected you will hold you in contempt."
)
T[(2, 36)] = (
    "Your enemies will say cruel things, mocking your strength. "
    "What could be more painful than that?"
)
T[(2, 37)] = (
    "If you're killed, you'll reach heaven; if you win, you'll rule the earth. "
    "So stand up, Arjuna, with the resolve to fight."
)
T[(2, 38)] = (
    "Treat pleasure and pain, gain and loss, victory and defeat as equal, "
    "and then fight. This way you won't incur any sin."
)
T[(2, 39)] = (
    "This wisdom I've described is from the standpoint of knowledge; "
    "now hear it from the standpoint of action (yoga). "
    "Armed with this, you'll break free from the bondage of karma."
)
T[(2, 40)] = (
    "On this path, no effort is wasted, no progress is undone. "
    "Even a little of this practice protects you from great fear."
)
T[(2, 41)] = (
    "On this path, Arjuna, the mind is focused — one resolution, one direction. "
    "But the minds of the unresolved scatter endlessly in many directions."
)
T[(2, 42)] = (
    "The unwise get carried away with the flowery passages of the Vedas, "
    "declaring \"there's nothing more than this,\""
)
T[(2, 43)] = (
    "full of desire, aiming at heaven, offering rituals for rebirth and results — "
    "loaded with specific ceremonies chasing pleasure and power."
)
T[(2, 44)] = (
    "For people attached to pleasure and power, their minds swept away by such talk, "
    "the focused, meditative mind never settles."
)
T[(2, 45)] = (
    "The Vedas deal with the three qualities of nature (sattva, rajas, tamas). "
    "Rise above them, Arjuna — beyond the pairs of opposites, "
    "steady in purity, free from concerns of gain and loss, self-possessed."
)
T[(2, 46)] = (
    "A well is of little use when water is flooding everywhere. "
    "Similarly, all the Vedas are of little use to the one who truly knows."
)
T[(2, 47)] = (
    "You have a right to your action, but never to its results. "
    "Don't let the results be your motivation, and don't cling to inaction either."
)
T[(2, 48)] = (
    "Do your work steadily, Arjuna, letting go of attachment, "
    "indifferent to success and failure. This evenness of mind is what yoga means."
)
T[(2, 49)] = (
    "Action driven by results is far inferior to action done with wisdom. "
    "Take refuge in wisdom. Pitiable are those who act just for results."
)
T[(2, 50)] = (
    "A person whose mind is steady in wisdom drops both good and bad deeds here and now. "
    "So commit yourself to yoga. Yoga is skill in action."
)
T[(2, 51)] = (
    "The wise, their minds steady, let go of the fruits of action, "
    "are freed from the bondage of rebirth, and reach a state beyond all suffering."
)
T[(2, 52)] = (
    "When your mind cuts through the tangle of delusion, "
    "you'll stop caring about what you've heard or have yet to hear."
)
T[(2, 53)] = (
    "When your mind, once confused by scriptures, stands firm and unwavering in deep stillness, "
    "you will have attained yoga."
)
T[(2, 54)] = (
    "Arjuna said:\n"
    "Krishna, what is a person of steady wisdom like — one established in deep stillness? "
    "How does such a person speak? How do they sit and move?"
)
T[(2, 55)] = (
    "Krishna said:\n"
    "When a person lets go of all the desires of the mind and finds contentment "
    "in the Self alone, they are called a person of steady wisdom."
)
T[(2, 56)] = (
    "Not shaken by sorrow, not craving pleasures, free from desire, fear, and anger — "
    "such a person is called a sage of steady mind."
)
T[(2, 57)] = (
    "Unattached to anything, neither pleased by good nor upset by bad — "
    "that person's wisdom is firmly established."
)
T[(2, 58)] = (
    "When a person can pull back their senses from objects "
    "the way a tortoise draws in its limbs — their wisdom is firmly established."
)
T[(2, 59)] = (
    "Objects fall away from the person who abstains, "
    "but the craving for them lingers — until they experience what is higher. "
    "Then even the craving goes."
)
T[(2, 60)] = (
    "The restless senses, Arjuna, can forcibly carry off the mind "
    "even of a wise person who is trying."
)
T[(2, 61)] = (
    "So a person should hold all the senses in check and sit focused, devoted to Me. "
    "When the senses are under control, wisdom is firmly established."
)
T[(2, 62)] = (
    "Dwelling on sense objects breeds attachment to them; "
    "attachment breeds desire; desire breeds anger."
)
T[(2, 63)] = (
    "Anger breeds delusion; delusion breeds loss of memory; "
    "loss of memory breeds destruction of reason; and with reason destroyed, the person is lost."
)
T[(2, 64)] = (
    "But a disciplined person moving among sense objects, senses under control, "
    "free from attachment and aversion, guided by the Self — attains inner peace."
)
T[(2, 65)] = (
    "In peace, all sorrows are destroyed. "
    "For the peaceful-minded, steady wisdom quickly takes root."
)
T[(2, 66)] = (
    "The undisciplined have no understanding and no meditation. "
    "Without meditation, no peace; without peace, how can there be happiness?"
)
T[(2, 67)] = (
    "When the mind follows wandering senses, understanding is carried off — "
    "like a boat being swept away by the wind on water."
)
T[(2, 68)] = (
    "So, Arjuna, the person whose senses are completely withdrawn from their objects "
    "is the one whose wisdom is firmly established."
)
T[(2, 69)] = (
    "What is night for all others, the self-controlled is awake in; "
    "what others are awake in, that is night for the sage who sees."
)
T[(2, 70)] = (
    "The ocean stays full and undisturbed though rivers pour into it. "
    "Likewise, the person desires flow into but who is not disturbed by them reaches peace — "
    "not the one who chases desires."
)
T[(2, 71)] = (
    "The person who gives up all desires, walks without longing, "
    "lets go of \"mine\" and \"I\" — that person reaches peace."
)
T[(2, 72)] = (
    "This is the state of union with the infinite (Brahman), Arjuna. "
    "Reaching it, one is no longer confused. Staying in it even at death, "
    "one attains the ultimate peace."
)


# ============================================================================
# CHAPTER 3 — The Way of Action
# ============================================================================

T[(3, 1)] = (
    "Arjuna said:\n"
    "Krishna, if you say wisdom is better than action, "
    "why are you pushing me into this terrible fight?"
)
T[(3, 2)] = (
    "Your mixed signals are confusing me. "
    "Tell me clearly — one thing — that will lead me to the highest good."
)
T[(3, 3)] = (
    "Krishna said:\n"
    "Arjuna, long ago I taught two paths in this world: "
    "the way of knowledge for the contemplative, and the way of action for the active."
)
T[(3, 4)] = (
    "You don't become free from action by simply avoiding action, "
    "and you don't reach perfection by renouncing alone."
)
T[(3, 5)] = (
    "No one can stay completely inactive, not even for a moment. "
    "Nature's three qualities make everyone act, whether they want to or not."
)
T[(3, 6)] = (
    "The person who forces their body to sit still but lets their mind dwell on sense objects "
    "is a confused hypocrite."
)
T[(3, 7)] = (
    "But the person who controls the senses with the mind "
    "and engages the body in action without attachment — that person is excellent, Arjuna."
)
T[(3, 8)] = (
    "Do your assigned work. Action is better than inaction. "
    "You couldn't even keep your body alive without action."
)
T[(3, 9)] = (
    "This world is bound by action — except action done as a sacred offering. "
    "So do your work as an offering, Arjuna, without attachment."
)
T[(3, 10)] = (
    "In the beginning, the Lord of beings created humans along with sacrifice and said: "
    "\"By this you shall multiply. Let this fulfill your needs.\""
)
T[(3, 11)] = (
    "\"Through this, nourish the gods, and the gods will nourish you. "
    "Supporting each other, you'll attain the highest good.\""
)
T[(3, 12)] = (
    "\"The gods, nourished by your offerings, will give you what you need. "
    "Whoever enjoys their gifts without giving back is a thief.\""
)
T[(3, 13)] = (
    "Good people who eat what's left from an offering are freed from all sins. "
    "But those who cook only for themselves eat only sin."
)
T[(3, 14)] = (
    "Beings come from food; food comes from rain; "
    "rain comes from sacrifice; and sacrifice comes from action."
)
T[(3, 15)] = (
    "Action arises from the Vedic principle, which arises from the Imperishable. "
    "So the all-pervading infinite is always present in sacrifice."
)
T[(3, 16)] = (
    "Whoever doesn't follow this wheel set in motion — living in sin, indulging the senses — "
    "lives in vain, Arjuna."
)
T[(3, 17)] = (
    "But the person who finds joy in the Self, is satisfied in the Self, "
    "content in the Self alone — has nothing more to do."
)
T[(3, 18)] = (
    "Such a person gains nothing from doing and loses nothing from not doing. "
    "They depend on no being for anything."
)
T[(3, 19)] = (
    "So always do the work you ought to do, without attachment. "
    "By acting without attachment, a person reaches the highest."
)
T[(3, 20)] = (
    "King Janaka and others reached perfection purely through action. "
    "You too should act — if only to keep the world going."
)
T[(3, 21)] = (
    "Whatever a great person does, others follow. "
    "Whatever standard they set, the world imitates."
)
T[(3, 22)] = (
    "Arjuna, there's nothing in the three worlds I have to do, "
    "nothing I haven't already attained — yet I keep acting."
)
T[(3, 23)] = (
    "If I didn't tirelessly keep acting, people everywhere would follow my lead."
)
T[(3, 24)] = (
    "If I didn't act, these worlds would fall apart. "
    "I would be the cause of chaos, destroying all creatures."
)
T[(3, 25)] = (
    "The ignorant act attached to their work, Arjuna. "
    "The wise should act just as actively — but without attachment — for the welfare of the world."
)
T[(3, 26)] = (
    "A wise person shouldn't unsettle the ignorant who are attached to their work. "
    "Instead, acting with full engagement himself, he should inspire them to act well."
)
T[(3, 27)] = (
    "Actions are carried out by nature's qualities in every way. "
    "But the person deluded by ego thinks, \"I am the doer.\""
)
T[(3, 28)] = (
    "But someone who understands how the qualities and actions really work "
    "sees that qualities act on qualities — and is not attached."
)
T[(3, 29)] = (
    "People deluded by nature's qualities are attached to the actions the qualities produce. "
    "The one who knows the whole picture shouldn't upset those who don't."
)
T[(3, 30)] = (
    "Surrender all your actions to Me, with your mind fixed on the Self. "
    "Drop hopes and \"mine,\" drop feverish excitement — and fight."
)
T[(3, 31)] = (
    "Those who follow this teaching of mine, with faith and without complaining, "
    "are freed from the bondage of action."
)
T[(3, 32)] = (
    "But those who scoff at this teaching and don't practice it — "
    "know them to be lost, without understanding in anything."
)
T[(3, 33)] = (
    "Even a wise person acts according to their own nature. "
    "Beings follow their nature. What good will suppression do?"
)
T[(3, 34)] = (
    "Attachment and aversion are built into the relationship between each sense and its object. "
    "Don't fall under their sway — they're your enemies."
)
T[(3, 35)] = (
    "Better to fail at your own duty than to succeed at someone else's. "
    "Better to die doing your own duty; another's duty is dangerous."
)
T[(3, 36)] = (
    "Arjuna said:\n"
    "Krishna, what actually pushes a person to act wrongly, "
    "even when they don't want to, as if something were forcing them?"
)
T[(3, 37)] = (
    "Krishna said:\n"
    "It's desire. It's anger. These arise from the quality of rajas (passion). "
    "All-devouring, deeply harmful — know this to be the enemy here."
)
T[(3, 38)] = (
    "As fire is hidden by smoke, a mirror by dust, an embryo by the womb — "
    "wisdom is hidden by desire."
)
T[(3, 39)] = (
    "Arjuna, wisdom is veiled by this constant enemy of the wise — "
    "desire, which burns like an unquenchable fire."
)
T[(3, 40)] = (
    "Desire hides in the senses, the mind, and the intellect. "
    "Through these it confuses the person, veiling their wisdom."
)
T[(3, 41)] = (
    "So, Arjuna, first get your senses under control, "
    "and destroy this harmful thing that destroys wisdom and realization."
)
T[(3, 42)] = (
    "The senses are said to be higher than the body; "
    "the mind is higher than the senses; the intellect is higher than the mind; "
    "and what is higher than the intellect is the Self."
)
T[(3, 43)] = (
    "So, knowing what is higher than the intellect, steady the self with the Self. "
    "Arjuna, destroy this enemy in the form of desire — hard to defeat though it is."
)


# ============================================================================
# CHAPTER 4 — Knowledge, Action, and Letting Go
# ============================================================================

T[(4, 1)] = (
    "Krishna said:\n"
    "I taught this eternal yoga to Vivasvan, the sun god. "
    "He taught it to Manu, and Manu to Ikshvaku."
)
T[(4, 2)] = (
    "Passed down this way, the royal sages knew it. "
    "But over a long stretch of time, that yoga was lost in this world, Arjuna."
)
T[(4, 3)] = (
    "That same ancient yoga I've taught to you today, "
    "because you're my devotee and my friend. This is the supreme secret."
)
T[(4, 4)] = (
    "Arjuna said:\n"
    "You were born recently; Vivasvan was born long ago. "
    "How am I to understand that you taught this at the beginning?"
)
T[(4, 5)] = (
    "Krishna said:\n"
    "Many lifetimes have passed for me — and for you, Arjuna. "
    "I know them all; you don't."
)
T[(4, 6)] = (
    "Though I am unborn, my Self imperishable, though I am the Lord of all beings, "
    "I take my stand in my own nature and come into being through my own power."
)
T[(4, 7)] = (
    "Whenever righteousness (dharma) declines and unrighteousness rises, Arjuna, "
    "I bring myself into being."
)
T[(4, 8)] = (
    "To protect the good, to destroy the wicked, "
    "and to re-establish dharma — I come age after age."
)
T[(4, 9)] = (
    "Anyone who truly understands my divine birth and action "
    "is not born again when they leave the body — they come to me, Arjuna."
)
T[(4, 10)] = (
    "Freed from attachment, fear, and anger, absorbed in me, taking refuge in me, "
    "purified by the discipline of knowledge — many have attained my state."
)
T[(4, 11)] = (
    "Whichever way people approach me, that's how I respond to them. "
    "People follow my path, Arjuna, in all directions."
)
T[(4, 12)] = (
    "Those who seek material success offer sacrifices to the gods here, "
    "because in this world, success from action comes quickly."
)
T[(4, 13)] = (
    "The four social orders were created by me, based on qualities and work. "
    "Though I am their maker, know that I am unchanging and don't act."
)
T[(4, 14)] = (
    "Actions don't stain me, and I don't crave their results. "
    "Anyone who understands this is not bound by actions."
)
T[(4, 15)] = (
    "Knowing this, the ancient seekers of liberation also performed action. "
    "So do your work, just as the ancients did long ago."
)
T[(4, 16)] = (
    "What is action? What is inaction? Even the wise are confused about this. "
    "I'll tell you clearly, so that you may be freed from harm."
)
T[(4, 17)] = (
    "You must understand the nature of right action, of wrong action, and of inaction. "
    "The way of action is deep and hard to see."
)
T[(4, 18)] = (
    "The person who sees inaction in action and action in inaction — "
    "that person is wise, truly yoked, truly active."
)
T[(4, 19)] = (
    "The person whose every undertaking is free from desire-based plans, "
    "whose actions are burned up in the fire of wisdom — the wise call that person truly learned."
)
T[(4, 20)] = (
    "Giving up attachment to results, always content, relying on nothing — "
    "even when doing things, such a person doesn't really do anything."
)
T[(4, 21)] = (
    "Without expectation, with mind and self controlled, giving up all possessions, "
    "acting with only the body — such a person incurs no sin."
)
T[(4, 22)] = (
    "Content with whatever comes unsought, beyond pairs of opposites, free from jealousy, "
    "even in success and failure — though they act, they are not bound."
)
T[(4, 23)] = (
    "For one who is free, whose mind is established in wisdom, who acts as an offering, "
    "all karma dissolves."
)
T[(4, 24)] = (
    "The offering is Brahman; the sacrifice is Brahman; "
    "poured by Brahman into the fire of Brahman. Brahman alone is reached "
    "by the one who sees Brahman in all action."
)
T[(4, 25)] = (
    "Some yogis offer sacrifices to the gods; "
    "others offer the sacrifice itself as an offering into the fire of Brahman."
)
T[(4, 26)] = (
    "Some offer the senses — hearing and the rest — into fires of self-discipline. "
    "Others offer sense objects — sound and the rest — into the fires of the senses."
)
T[(4, 27)] = (
    "Some offer all sense-activities and life-energies into the fire of self-mastery, "
    "kindled by wisdom."
)
T[(4, 28)] = (
    "Some sacrifice with wealth, some with austerity, some with yoga, "
    "some with study and wisdom — people of strict vows."
)
T[(4, 29)] = (
    "Others, practicing breath control, regulate the outflow and inflow, "
    "offering the outbreath into the inbreath and vice versa."
)
T[(4, 30)] = (
    "Others, restricting their food, offer their life-energies into their life-energies. "
    "All of these know sacrifice, and their sins are destroyed through sacrifice."
)
T[(4, 31)] = (
    "Those who eat the leftovers of sacrifice — the true nectar — reach eternal Brahman. "
    "This world isn't even for the non-sacrificer — how could any other world be?"
)
T[(4, 32)] = (
    "So many kinds of sacrifices are spread out at the mouth of Brahman. "
    "Know them all as born of action; knowing this, you'll be free."
)
T[(4, 33)] = (
    "The sacrifice of wisdom is better than the sacrifice of material things, Arjuna. "
    "Every action, in its fullness, culminates in wisdom."
)
T[(4, 34)] = (
    "Seek that wisdom with humility, by asking questions, and by serving. "
    "Those who have seen the truth will teach you."
)
T[(4, 35)] = (
    "Having grasped this, Arjuna, you'll never fall into confusion again. "
    "You'll see every being in yourself — and then in me."
)
T[(4, 36)] = (
    "Even if you were the greatest of all sinners, "
    "you would cross over all evil on the boat of wisdom."
)
T[(4, 37)] = (
    "As a blazing fire reduces firewood to ashes, Arjuna, "
    "the fire of wisdom reduces all actions to ashes."
)
T[(4, 38)] = (
    "Nothing here purifies like wisdom. "
    "A person perfected in yoga finds it within themselves, in time."
)
T[(4, 39)] = (
    "A person with faith, committed to practice, senses under control — attains wisdom. "
    "And once attained, it soon brings supreme peace."
)
T[(4, 40)] = (
    "But the ignorant, the faithless, the doubter — they are lost. "
    "For the doubter there is no happiness here, elsewhere, or anywhere."
)
T[(4, 41)] = (
    "Arjuna, actions do not bind the person who has given up action through yoga, "
    "whose doubts have been cut away by wisdom, who is self-possessed."
)
T[(4, 42)] = (
    "So, with the sword of wisdom, cut away this doubt in your heart — "
    "born of ignorance. Take up yoga and stand up, Arjuna."
)


# ============================================================================
# CHAPTER 5 — The Way of Renunciation
# ============================================================================

T[(5, 1)] = (
    "Arjuna said:\n"
    "Krishna, you praise renouncing action — and then you praise action (yoga). "
    "Tell me clearly which one is better."
)
T[(5, 2)] = (
    "Krishna said:\n"
    "Both renunciation and the way of action lead to the highest. "
    "But of the two, the way of action is better than renouncing action."
)
T[(5, 3)] = (
    "Know this person as a lifelong renunciate: one who neither hates nor desires. "
    "Free from opposites, Arjuna, such a person is easily set free from bondage."
)
T[(5, 4)] = (
    "Only children — not the wise — think of the paths of knowledge and action as different. "
    "Whoever is fully established in one gets the fruit of both."
)
T[(5, 5)] = (
    "The state reached by the path of knowledge is the same state reached by the path of action. "
    "The one who sees these two as one — truly sees."
)
T[(5, 6)] = (
    "But renunciation without the practice of yoga is hard to attain, Arjuna. "
    "The sage committed to yoga reaches the infinite quickly."
)
T[(5, 7)] = (
    "Engaged in yoga, purified in self, with body and senses mastered, "
    "one's self becoming the Self of all beings — such a person isn't stained, even while acting."
)
T[(5, 8)] = (
    "The person who knows the truth thinks: \"I'm not really doing anything,\" "
    "even while seeing, hearing, touching, smelling, eating, walking, sleeping, breathing,"
)
T[(5, 9)] = (
    "speaking, releasing, grasping, opening and closing the eyes — "
    "understanding that it's the senses moving among their objects."
)
T[(5, 10)] = (
    "The person who acts without attachment, offering actions to Brahman, "
    "is not stained by sin — like a lotus leaf untouched by water."
)
T[(5, 11)] = (
    "With body, mind, intellect, or even just the senses alone, yogis act "
    "without attachment, to purify themselves."
)
T[(5, 12)] = (
    "The yogi, letting go of results, reaches lasting peace. "
    "The non-yogi, attached to results by desire, is trapped."
)
T[(5, 13)] = (
    "Mentally letting go of all actions, the self-controlled person rests peacefully "
    "in the \"city of nine gates\" (the body) — neither acting nor causing action."
)
T[(5, 14)] = (
    "The indwelling Self doesn't create agency, actions, or the link of action to result. "
    "It's nature (prakriti) that acts."
)
T[(5, 15)] = (
    "The all-pervading One doesn't take on anyone's sin or merit. "
    "Wisdom is hidden by ignorance, and so beings are confused."
)
T[(5, 16)] = (
    "But for those whose ignorance is destroyed by self-knowledge, "
    "that knowledge lights up the supreme — like the sun."
)
T[(5, 17)] = (
    "With their minds on That, their selves rooted in That, with That as their goal, "
    "devoted to That — they reach a state from which they don't return, their sins wiped clean by wisdom."
)
T[(5, 18)] = (
    "The wise see the same reality in a learned and humble brahmin, "
    "a cow, an elephant, a dog, or even an outcaste."
)
T[(5, 19)] = (
    "Those whose minds are steady in seeing sameness have conquered rebirth even here. "
    "Brahman is spotless and the same everywhere — so they are established in Brahman."
)
T[(5, 20)] = (
    "The one who knows Brahman — steady in intellect, unconfused — "
    "doesn't get excited over what is pleasant or upset by what is unpleasant."
)
T[(5, 21)] = (
    "With the self unattached to external things, such a person finds the joy that lies in the Self. "
    "Joined in yoga with Brahman, they enjoy imperishable happiness."
)
T[(5, 22)] = (
    "Pleasures born of sense-contact are wombs of pain. They have a beginning and an end. "
    "The wise do not take their delight in them, Arjuna."
)
T[(5, 23)] = (
    "Whoever, even here and now, before leaving the body, can withstand the surges of desire and anger — "
    "that person is truly yoked; that person is happy."
)
T[(5, 24)] = (
    "The one whose happiness, delight, and light are all within — "
    "that yogi, becoming Brahman, reaches the peace of Brahman."
)
T[(5, 25)] = (
    "Sages whose sins are gone, whose doubts are dispelled, whose minds are disciplined, "
    "who delight in the welfare of all beings — they reach the peace of Brahman."
)
T[(5, 26)] = (
    "For the disciplined ones free from desire and anger, with minds under control, "
    "knowing the Self — the peace of Brahman is close at hand, all around."
)
T[(5, 27)] = (
    "Shutting out external stimuli, focusing the gaze between the eyebrows, "
    "balancing the inbreath and the outbreath moving through the nostrils,"
)
T[(5, 28)] = (
    "with senses, mind, and intellect under control, the sage aims at liberation, "
    "free from desire, fear, and anger — truly, always free."
)
T[(5, 29)] = (
    "Know me as the receiver of all offerings and disciplines, the great Lord of all worlds, "
    "the friend of all beings — and you reach peace."
)


# ============================================================================
# CHAPTER 6 — The Way of Meditation
# ============================================================================

T[(6, 1)] = (
    "Krishna said:\n"
    "The person who does the work they ought to do without depending on the results — "
    "that person is the true renunciate and the true yogi; "
    "not just the one who lights no ritual fire or does no action."
)
T[(6, 2)] = (
    "Know that what's called renunciation is also yoga, Arjuna. "
    "No one becomes a yogi without giving up self-serving intentions."
)
T[(6, 3)] = (
    "For a sage trying to climb to yoga, action is the means. "
    "For one who has reached yoga, stillness is the means."
)
T[(6, 4)] = (
    "When a person isn't attached to sense objects or to actions, "
    "having given up all self-serving intentions — then they're said to have reached yoga."
)
T[(6, 5)] = (
    "Lift yourself by yourself. Don't let yourself fall. "
    "The Self alone is your friend; the self alone is your enemy."
)
T[(6, 6)] = (
    "For the person who has conquered themselves, the Self is a friend. "
    "But to the one who hasn't, their own self acts like an enemy."
)
T[(6, 7)] = (
    "A self-controlled, peaceful person remains steady in the Supreme Self — "
    "through cold and heat, pleasure and pain, honor and dishonor."
)
T[(6, 8)] = (
    "The yogi who is content with knowledge and realization, unshakable, senses under control — "
    "to whom a clod of earth, a stone, and a lump of gold are alike — is truly yoked."
)
T[(6, 9)] = (
    "Whoever sees with equal mind well-wishers, friends, enemies, neutrals, mediators, "
    "the hateful, relatives, the righteous, and even the sinful — excels."
)
T[(6, 10)] = (
    "Let the yogi constantly concentrate the mind, sitting alone in a quiet place, "
    "with body and mind under control, without possessions, without cravings."
)
T[(6, 11)] = (
    "Setting up a steady seat for oneself in a clean place, neither too high nor too low, "
    "covered with cloth, deerskin, and kusha grass, layered together,"
)
T[(6, 12)] = (
    "sitting there, making the mind one-pointed, controlling the activities of mind and senses, "
    "let the yogi practice to purify the self."
)
T[(6, 13)] = (
    "Holding the body, head, and neck erect and still, gazing steadily at the tip of the nose, "
    "not looking around,"
)
T[(6, 14)] = (
    "with a serene mind, fearless, firm in a vow of celibacy, mind controlled, "
    "thoughts fixed on me — let the yogi sit, absorbed, with me as the goal."
)
T[(6, 15)] = (
    "Always yoking the mind this way, the yogi of disciplined mind "
    "reaches the peace abiding in me — the peace that ends in liberation."
)
T[(6, 16)] = (
    "Yoga is not for someone who eats too much or eats nothing at all, "
    "not for the one who sleeps too much or stays awake too much, Arjuna."
)
T[(6, 17)] = (
    "For the one whose food and recreation are moderate, whose effort in action is measured, "
    "whose sleep and waking are balanced — yoga destroys sorrow."
)
T[(6, 18)] = (
    "When the disciplined mind settles in the Self alone, free from craving for any desire — "
    "that person is said to be truly yoked."
)
T[(6, 19)] = (
    "\"Like a lamp in a windless place that does not flicker\" — "
    "that's the image used for a yogi whose mind is absorbed in concentration on the Self."
)
T[(6, 20)] = (
    "In that state, where the mind becomes still through the practice of yoga, "
    "seeing the Self by the Self, one is satisfied in the Self."
)
T[(6, 21)] = (
    "In that state one knows the infinite happiness grasped by the intellect, beyond the senses — "
    "and established in it, one never wanders from the truth."
)
T[(6, 22)] = (
    "Once gained, the yogi thinks nothing greater can be gained. "
    "Established in it, they aren't shaken even by heavy sorrow."
)
T[(6, 23)] = (
    "That disconnection from pain's hold is what should be known as yoga. "
    "It must be practiced with determination and without discouragement."
)
T[(6, 24)] = (
    "Completely giving up all desires born of intention, "
    "restraining the whole gang of senses with the mind from every side,"
)
T[(6, 25)] = (
    "let the person gradually grow still with an intellect held steady. "
    "With the mind fixed on the Self, let them think of nothing at all."
)
T[(6, 26)] = (
    "Wherever the restless, unsteady mind wanders off — "
    "pull it back from there, bring it under the control of the Self alone."
)
T[(6, 27)] = (
    "Supreme happiness comes to the yogi whose mind is completely peaceful, "
    "whose passion is stilled, who has become one with Brahman, free from stain."
)
T[(6, 28)] = (
    "Yoking the self like this constantly, the yogi, free from stain, "
    "easily reaches the infinite happiness of contact with Brahman."
)
T[(6, 29)] = (
    "Whose self is yoked in yoga sees the same reality everywhere — "
    "sees the Self in all beings and all beings in the Self."
)
T[(6, 30)] = (
    "Whoever sees me everywhere and sees all in me — "
    "I am not lost to them, and they are not lost to me."
)
T[(6, 31)] = (
    "The yogi who, established in oneness, worships me as present in all beings — "
    "however they live, they live in me."
)
T[(6, 32)] = (
    "Whoever, by comparison with themselves, sees everything as equal, Arjuna — "
    "whether pleasure or pain — is considered the highest yogi."
)
T[(6, 33)] = (
    "Arjuna said:\n"
    "Krishna, this yoga of evenness you've described — "
    "I don't see how it can last, because the mind is so restless."
)
T[(6, 34)] = (
    "The mind is really restless, Krishna — turbulent, strong, stubborn. "
    "Controlling it seems as hard as controlling the wind."
)
T[(6, 35)] = (
    "Krishna said:\n"
    "No doubt about it, Arjuna — the mind is hard to control, and restless. "
    "But by practice and by detachment, it can be brought under control."
)
T[(6, 36)] = (
    "I agree, yoga is hard to attain for one without self-control. "
    "But with effort and discipline, the one who strives can reach it."
)
T[(6, 37)] = (
    "Arjuna said:\n"
    "What happens to the person with faith who strives but whose mind wanders, "
    "and who doesn't reach perfection in yoga, Krishna?"
)
T[(6, 38)] = (
    "Having fallen from both paths, don't they perish like a broken cloud — "
    "with no ground under them, deluded on the path to Brahman?"
)
T[(6, 39)] = (
    "Krishna, please completely clear this doubt for me. "
    "There's no one else who can."
)
T[(6, 40)] = (
    "Krishna said:\n"
    "Arjuna, such a person is not destroyed — not in this world or the next. "
    "No one who does good, my friend, ever comes to grief."
)
T[(6, 41)] = (
    "Having reached the worlds of the righteous and lived there for countless years, "
    "the one who fell from yoga is born again in the home of the pure and the prosperous."
)
T[(6, 42)] = (
    "Or they may even be born into a family of wise yogis. "
    "Such a birth is very rare in this world."
)
T[(6, 43)] = (
    "There they recover the understanding from their previous life "
    "and strive again for perfection, Arjuna."
)
T[(6, 44)] = (
    "By that very previous practice they're carried forward, even against their will. "
    "Just the inquiry into yoga takes a person beyond the ritual of the Vedas."
)
T[(6, 45)] = (
    "But the yogi who works hard, purified of sins, "
    "perfected through many lifetimes, reaches the highest goal."
)
T[(6, 46)] = (
    "The yogi is greater than those who practice austerity, greater than the learned, "
    "greater than ritualists. So be a yogi, Arjuna."
)
T[(6, 47)] = (
    "And among all yogis, the one who worships me with faith and inner heart absorbed in me — "
    "I consider the most deeply joined."
)


# ============================================================================
# CHAPTER 7 — Knowledge and Realization
# ============================================================================

T[(7, 1)] = (
    "Krishna said:\n"
    "Arjuna, with your mind fixed on me, taking refuge in me, practicing yoga — "
    "listen to how you can know me completely, beyond doubt."
)
T[(7, 2)] = (
    "I'll tell you fully the knowledge with realization — "
    "knowing which there's nothing else here left to know."
)
T[(7, 3)] = (
    "Among thousands of people, maybe one strives for perfection. "
    "Even among those who strive and attain it, maybe one truly knows me."
)
T[(7, 4)] = (
    "Earth, water, fire, air, space, mind, intellect, and ego — "
    "these are the eight divisions of my lower nature."
)
T[(7, 5)] = (
    "But know, Arjuna, my other, higher nature — "
    "the life-principle by which this whole universe is held up."
)
T[(7, 6)] = (
    "Understand that all beings arise from these two. "
    "I am the origin of the whole universe — and also its dissolution."
)
T[(7, 7)] = (
    "Nothing at all is higher than me, Arjuna. "
    "All this is strung on me like beads on a thread."
)
T[(7, 8)] = (
    "Arjuna, I am the taste in water, the light in the sun and moon, "
    "the sacred sound \"Om\" in all the Vedas, the sound in space, the strength in men."
)
T[(7, 9)] = (
    "I am the pure fragrance in earth, the brilliance in fire, "
    "the life in all beings, the austerity in those who are disciplined."
)
T[(7, 10)] = (
    "Know me, Arjuna, as the eternal seed of all beings. "
    "I am the intelligence of the intelligent, the splendor of the splendid."
)
T[(7, 11)] = (
    "I am the strength of the strong — free from desire and passion. "
    "In beings I am desire that doesn't violate dharma."
)
T[(7, 12)] = (
    "Whatever states of being there are — of purity (sattva), activity (rajas), and inertia (tamas) — "
    "know them as coming from me alone. But I am not in them; they are in me."
)
T[(7, 13)] = (
    "Confused by these three qualities, the world doesn't recognize me — "
    "the one who is beyond them, imperishable."
)
T[(7, 14)] = (
    "This divine illusion (maya) of mine, made of the three qualities, is hard to cross. "
    "Those who take refuge in me alone cross it."
)
T[(7, 15)] = (
    "Evildoers, the confused, the lowest of men, don't take refuge in me. "
    "Their knowledge is carried off by illusion; they cling to a demonic nature."
)
T[(7, 16)] = (
    "Four kinds of good people worship me, Arjuna: "
    "the distressed, the seeker of knowledge, the seeker of success, and the wise."
)
T[(7, 17)] = (
    "Of these, the wise one — ever steady, devoted to the One — is the best. "
    "To the wise, I am exceedingly dear, and they are dear to me."
)
T[(7, 18)] = (
    "All of them are noble, but I hold the wise one to be my very Self. "
    "With a steady mind, they are established in me alone, the highest goal."
)
T[(7, 19)] = (
    "At the end of many lifetimes, the wise person takes refuge in me, "
    "seeing \"Krishna (Vasudeva) is all this.\" Such a great soul is very rare."
)
T[(7, 20)] = (
    "Those whose wisdom is carried off by this or that desire turn to other deities, "
    "following various practices, bound by their own nature."
)
T[(7, 21)] = (
    "Whatever form any devotee sincerely wants to worship — "
    "I make their faith in that form steady."
)
T[(7, 22)] = (
    "Endowed with that faith, they seek what they want from that deity — "
    "and get the results, which are actually given by me."
)
T[(7, 23)] = (
    "But the fruit for such people, whose understanding is limited, is limited. "
    "Worshippers of deities go to those deities. My devotees come to me."
)
T[(7, 24)] = (
    "The unwise think of me — the unmanifest — as having just come into manifestation, "
    "not knowing my higher, imperishable, supreme nature."
)
T[(7, 25)] = (
    "Not everyone can see me clearly; I'm veiled by my yoga-maya. "
    "This confused world doesn't know me — unborn, imperishable."
)
T[(7, 26)] = (
    "I know all beings of the past, present, and future, Arjuna. "
    "But nobody knows me."
)
T[(7, 27)] = (
    "Confused by the pairs of opposites arising from desire and aversion, "
    "all beings in creation are deluded from the start, Arjuna."
)
T[(7, 28)] = (
    "But those of virtuous action, whose sins have ended, "
    "freed from the delusion of opposites, worship me with firm resolve."
)
T[(7, 29)] = (
    "Those who strive for freedom from old age and death, taking refuge in me — "
    "know Brahman completely, the Self, and all action."
)
T[(7, 30)] = (
    "Those who know me as the principle behind beings, behind the gods, and behind sacrifice — "
    "with minds yoked, know me even at the hour of death."
)


# ============================================================================
# CHAPTER 8 — The Imperishable Reality
# ============================================================================

T[(8, 1)] = (
    "Arjuna said:\n"
    "What is Brahman? What is the Self? What is action, Krishna? "
    "What is called the principle behind beings? What is the principle behind the gods?"
)
T[(8, 2)] = (
    "Who is the principle behind sacrifice, and how, in this body? "
    "And how are you to be known at the hour of death by the self-controlled?"
)
T[(8, 3)] = (
    "Krishna said:\n"
    "The Imperishable is the supreme Brahman. Its nature is called the Self. "
    "The offering that causes beings to come into existence is called action (karma)."
)
T[(8, 4)] = (
    "The principle behind beings is perishable nature. The principle behind the gods is the cosmic Person. "
    "The principle behind sacrifice — here in the body — is me."
)
T[(8, 5)] = (
    "The person who, remembering me alone at the moment of death, leaves the body "
    "reaches my state of being. No doubt about it."
)
T[(8, 6)] = (
    "Whatever state of being a person remembers at the last moment when leaving the body — "
    "that's the state they reach, having dwelt on it constantly."
)
T[(8, 7)] = (
    "So remember me always, and fight. "
    "With your mind and intellect fixed on me, you will definitely come to me."
)
T[(8, 8)] = (
    "The person whose mind, disciplined by the practice of yoga, doesn't wander anywhere else "
    "reaches the supreme divine Person, Arjuna — by meditating on him."
)
T[(8, 9)] = (
    "Whoever meditates on the all-knowing, the ancient, the ruler, subtler than the subtle, "
    "the sustainer of all, of unimaginable form, sun-like in color, beyond darkness —"
)
T[(8, 10)] = (
    "at the hour of death, with a steady mind, with devotion and the power of yoga, "
    "fully drawing the life-breath between the eyebrows — reaches the supreme divine Person."
)
T[(8, 11)] = (
    "That which the knowers of the Vedas call the Imperishable, that which the disciplined ascetics, "
    "free from passion, enter; for which they practice celibacy — I'll tell you about that goal briefly."
)
T[(8, 12)] = (
    "Closing all the gates of the body, confining the mind in the heart, "
    "drawing the life-breath into the head, established in yogic concentration,"
)
T[(8, 13)] = (
    "uttering the single syllable \"Om\" (which is Brahman), remembering me — "
    "whoever leaves the body this way reaches the supreme goal."
)
T[(8, 14)] = (
    "The one who always remembers me, thinking of nothing else — "
    "for that ever-yoked yogi, I'm easy to reach, Arjuna."
)
T[(8, 15)] = (
    "Great souls who have come to me, having reached the highest perfection, "
    "are not reborn in this fleeting home of suffering."
)
T[(8, 16)] = (
    "From the world of Brahma the creator on down, all worlds bring return, Arjuna. "
    "But on reaching me, there's no rebirth."
)
T[(8, 17)] = (
    "Those who know that Brahma's day lasts a thousand ages, "
    "and his night also a thousand ages — they are the ones who truly know day and night."
)
T[(8, 18)] = (
    "At the coming of day, all manifestations come out of the unmanifest. "
    "At the coming of night, they dissolve back into that very unmanifest."
)
T[(8, 19)] = (
    "This same multitude of beings, coming into being again and again, "
    "dissolves helplessly at the coming of night, Arjuna, and comes forth again at the coming of day."
)
T[(8, 20)] = (
    "But beyond this unmanifest is another unmanifest — eternal being — "
    "which does not perish when all beings perish."
)
T[(8, 21)] = (
    "That unmanifest, called the Imperishable, is declared the supreme goal. "
    "Whoever reaches it does not return — that is my supreme abode."
)
T[(8, 22)] = (
    "Arjuna, the supreme Person, in whom all beings rest and by whom all this is pervaded, "
    "is reached by unwavering devotion alone."
)
T[(8, 23)] = (
    "Now I'll tell you the times at which yogis depart, Arjuna — "
    "to return or not to return."
)
T[(8, 24)] = (
    "Fire, light, day, the bright half of the month, the six months of the sun's northern course — "
    "departing then, the knowers of Brahman go to Brahman."
)
T[(8, 25)] = (
    "Smoke, night, the dark half of the month, the six months of the sun's southern course — "
    "the yogi going by this path reaches the moonlight and returns."
)
T[(8, 26)] = (
    "These two paths of the world — the bright and the dark — are considered eternal. "
    "By one, a person reaches no-return; by the other, return."
)
T[(8, 27)] = (
    "Knowing these two paths, Arjuna, no yogi is confused. "
    "So at all times, stay yoked in yoga, Arjuna."
)
T[(8, 28)] = (
    "Whatever merit is said to come from studying the Vedas, from sacrifices, austerities, and gifts — "
    "the yogi who knows this goes beyond all of them and reaches the supreme, original abode."
)


# ============================================================================
# CHAPTER 9 — The Royal Secret
# ============================================================================

T[(9, 1)] = (
    "Krishna said:\n"
    "To you who don't criticize, I'll reveal the most profound secret — "
    "knowledge together with realization — and by knowing it you'll be free from evil."
)
T[(9, 2)] = (
    "This is the king of sciences, the king of secrets, the supreme purifier. "
    "It's directly realizable, in line with dharma, easy to practice, never lost."
)
T[(9, 3)] = (
    "People without faith in this teaching don't reach me, Arjuna. "
    "They return to the cycle of birth and death."
)
T[(9, 4)] = (
    "All this world is pervaded by me in my unmanifest form. "
    "All beings rest in me — but I don't rest in them."
)
T[(9, 5)] = (
    "And yet beings don't rest in me — behold my divine power! "
    "Supporting beings but not resting in them, my Self is the source of beings."
)
T[(9, 6)] = (
    "As the mighty wind, moving everywhere, always rests in space — "
    "in the same way, all beings rest in me. Know it."
)
T[(9, 7)] = (
    "All beings, Arjuna, merge into my nature at the end of a cycle. "
    "At the beginning of the next cycle, I send them forth again."
)
T[(9, 8)] = (
    "Taking hold of my own nature, I send forth again and again "
    "this whole multitude of beings — helpless under the force of nature."
)
T[(9, 9)] = (
    "But these actions don't bind me, Arjuna. "
    "I remain as if indifferent, unattached to those actions."
)
T[(9, 10)] = (
    "Under my watch, nature produces everything that moves and everything that doesn't. "
    "That's the reason the world keeps spinning, Arjuna."
)
T[(9, 11)] = (
    "Fools dismiss me when I take a human body, "
    "not knowing my higher nature as the great Lord of beings."
)
T[(9, 12)] = (
    "With futile hopes, futile actions, futile knowledge, without discrimination, "
    "they are filled with a deluding nature — demonic and deceiving."
)
T[(9, 13)] = (
    "But great souls, Arjuna, partaking of the divine nature, "
    "worship me with undistracted minds, knowing me as the imperishable source of beings."
)
T[(9, 14)] = (
    "Always praising me, striving, firm in their vows, "
    "bowing down to me with devotion, ever-yoked, they worship me."
)
T[(9, 15)] = (
    "Others, offering the sacrifice of wisdom, worship me as the One, "
    "as the distinct, as the many, facing everywhere."
)
T[(9, 16)] = (
    "I am the ritual, I am the sacrifice, I am the offering to ancestors, I am the herb, "
    "I am the mantra, I am the clarified butter, I am the fire, I am the act of offering."
)
T[(9, 17)] = (
    "I am the father of this world, and the mother, the sustainer, the ancestor. "
    "I am what is to be known, the purifier, the sacred \"Om,\" and the Rig, Sama, and Yajur Vedas."
)
T[(9, 18)] = (
    "I am the goal, the sustainer, the master, the witness, the abode, the shelter, the friend; "
    "the origin, the dissolution, the ground, the storehouse, the imperishable seed."
)
T[(9, 19)] = (
    "I give heat; I hold back and pour out the rain. "
    "I am immortality and death, what is and what is not, Arjuna."
)
T[(9, 20)] = (
    "The knowers of the three Vedas, the drinkers of soma, their sins cleansed, "
    "worshipping me with sacrifices, pray for the way to heaven. "
    "Reaching the pure world of Indra, they enjoy the heavenly pleasures of the gods."
)
T[(9, 21)] = (
    "Having enjoyed that vast heavenly world, when their merit runs out, they re-enter the world of mortals. "
    "That's how, following the dharma of the three Vedas, desiring pleasures, "
    "they keep coming and going."
)
T[(9, 22)] = (
    "For those who, thinking of nothing else, worship me as ever-united, "
    "I provide what they lack and protect what they have."
)
T[(9, 23)] = (
    "Even those who, with faith, worship other deities — "
    "they too, Arjuna, are worshipping me, though not in the proper way."
)
T[(9, 24)] = (
    "Because I alone am the receiver and the Lord of all sacrifices. "
    "But they don't know me in truth, and so they fall."
)
T[(9, 25)] = (
    "Worshippers of deities go to those deities; ancestor-worshippers go to the ancestors; "
    "worshippers of spirits go to the spirits; and my worshippers come to me."
)
T[(9, 26)] = (
    "Whoever offers me — with devotion — a leaf, a flower, a fruit, or water, "
    "that offering of a pure-hearted devotee I accept."
)
T[(9, 27)] = (
    "Whatever you do, whatever you eat, whatever you offer, whatever you give, "
    "whatever discipline you practice — do it, Arjuna, as an offering to me."
)
T[(9, 28)] = (
    "This way you'll be freed from the bondage of action and its good and bad results. "
    "With your self yoked in the yoga of renunciation, you'll come to me, free."
)
T[(9, 29)] = (
    "I am the same in all beings. No one is hateful or dear to me. "
    "But those who worship me with devotion — they are in me, and I am in them."
)
T[(9, 30)] = (
    "Even the worst sinner — if they worship me with undivided devotion — "
    "should be regarded as good, because they've made the right decision."
)
T[(9, 31)] = (
    "They quickly become righteous and reach lasting peace. "
    "Know this for certain, Arjuna: my devotee is never lost."
)
T[(9, 32)] = (
    "Even those considered of low birth, Arjuna — women, vaishyas, shudras — "
    "taking refuge in me, reach the highest goal."
)
T[(9, 33)] = (
    "How much more so, then, the holy brahmins and devoted royal sages! "
    "Having entered this fleeting, unhappy world, worship me."
)
T[(9, 34)] = (
    "Fix your mind on me, be devoted to me, offer to me, bow down to me. "
    "Fully joined to me, with me as the supreme goal, you'll come to me."
)


# ============================================================================
# CHAPTER 10 — Divine Glories
# ============================================================================

T[(10, 1)] = (
    "Krishna said:\n"
    "Listen again, Arjuna, to my supreme word, "
    "which I'll speak to you, who are dear to me, wanting your good."
)
T[(10, 2)] = (
    "Neither the hosts of gods nor the great sages know my origin. "
    "I am the source of the gods and the great sages, in every way."
)
T[(10, 3)] = (
    "Whoever knows me as unborn, without beginning, the great Lord of the worlds — "
    "that person, not confused among mortals, is freed from all sins."
)
T[(10, 4)] = (
    "Discernment, knowledge, freedom from confusion, patience, truth, self-control, calm, "
    "pleasure, pain, existence, non-existence, fear, fearlessness —"
)
T[(10, 5)] = (
    "non-violence, equanimity, contentment, austerity, generosity, fame, infamy — "
    "these various states of beings come from me alone."
)
T[(10, 6)] = (
    "The seven great sages and the four ancient ones (Manus), sharing in my nature, "
    "were born of my mind. From them came all these creatures in the world."
)
T[(10, 7)] = (
    "Whoever truly understands this glory and power of mine "
    "is united with me in unshakable yoga. No doubt about it."
)
T[(10, 8)] = (
    "I am the source of everything. From me, everything comes. "
    "The wise, understanding this, worship me with devotion."
)
T[(10, 9)] = (
    "With their thoughts on me, their lives surrendered to me, "
    "telling each other about me, always speaking of me — they are content and joyful."
)
T[(10, 10)] = (
    "To those ever-yoked devotees worshipping me with love, "
    "I give the discernment through which they come to me."
)
T[(10, 11)] = (
    "Out of compassion for them, I dwell in their very self "
    "and destroy the darkness of ignorance with the bright lamp of wisdom."
)
T[(10, 12)] = (
    "Arjuna said:\n"
    "You are the supreme Brahman, the supreme abode, the supreme purifier — "
    "the eternal, divine Person, primal God, unborn, all-pervading."
)
T[(10, 13)] = (
    "This is what all the sages say — and so does the divine sage Narada, "
    "and Asita, Devala, and Vyasa. And you yourself say it to me."
)
T[(10, 14)] = (
    "I accept everything you've told me as true, Krishna. "
    "Neither gods nor demons truly understand your manifestation, Lord."
)
T[(10, 15)] = (
    "You alone know yourself by yourself, supreme Person — "
    "source of beings, Lord of beings, God of gods, Lord of the world."
)
T[(10, 16)] = (
    "Please tell me, in full, your divine glories, "
    "through which you pervade all these worlds."
)
T[(10, 17)] = (
    "How shall I know you, yogi, by constant meditation? "
    "In what various aspects should I meditate on you, Lord?"
)
T[(10, 18)] = (
    "Tell me again, in detail, about your yoga and your glories, Krishna. "
    "I never get enough of listening to your nectar-like words."
)
T[(10, 19)] = (
    "Krishna said:\n"
    "Fine — I'll tell you the main ones of my divine glories, Arjuna. "
    "There's no end to the details of my manifestation."
)
T[(10, 20)] = (
    "I am the Self seated in the hearts of all beings, Arjuna. "
    "I am the beginning, the middle, and the end of all beings."
)
T[(10, 21)] = (
    "Of the Adityas I am Vishnu; of lights, the radiant sun. "
    "Of the Maruts (storm-gods) I am Marichi; of the stars, I am the moon."
)
T[(10, 22)] = (
    "Of the Vedas I am the Sama Veda; of the gods, I am Indra. "
    "Of the senses I am the mind; in living beings I am consciousness."
)
T[(10, 23)] = (
    "Of the Rudras I am Shankara (Shiva); of yakshas and rakshasas, I am Kubera. "
    "Of the Vasus I am Fire; of mountains, Meru."
)
T[(10, 24)] = (
    "Among household priests, know me as Brihaspati — the chief. "
    "Among generals I am Skanda; among bodies of water, the ocean."
)
T[(10, 25)] = (
    "Of the great sages I am Bhrigu; of sounds, I am the single syllable \"Om.\" "
    "Of sacrifices I am the silent repetition of a mantra; of things unmoving, the Himalayas."
)
T[(10, 26)] = (
    "Of all trees I am the ashvattha (sacred fig); of divine sages, Narada; "
    "of celestial musicians, Chitraratha; of perfected beings, Kapila."
)
T[(10, 27)] = (
    "Among horses know me as Ucchaishravas, born from the churning for nectar; "
    "among royal elephants, Airavata; among humans, the king."
)
T[(10, 28)] = (
    "Among weapons I am the thunderbolt; among cows, the wish-fulfilling Kamadhenu. "
    "I am the god of love in those who reproduce; among serpents, I am Vasuki."
)
T[(10, 29)] = (
    "Of the nagas I am Ananta; of water-beings, Varuna. "
    "Of ancestors, Aryaman; among rulers, I am Yama (god of death)."
)
T[(10, 30)] = (
    "Of the demons I am Prahlada; of counters, I am Time. "
    "Of animals, the lion; of birds, Garuda."
)
T[(10, 31)] = (
    "Of purifiers I am the wind; of warriors, Rama. "
    "Of fish I am the makara; of rivers, the Ganga."
)
T[(10, 32)] = (
    "Of creations I am the beginning, the end, and the middle, Arjuna. "
    "Of sciences I am the science of the Self; among debaters, I am the debate itself."
)
T[(10, 33)] = (
    "Of letters I am \"A\"; of grammatical compounds, the dual compound. "
    "I alone am imperishable Time; I am the Creator facing all directions."
)
T[(10, 34)] = (
    "I am all-devouring death, and the source of what is yet to come. "
    "Of feminine qualities: fame, fortune, speech, memory, intelligence, steadiness, forgiveness."
)
T[(10, 35)] = (
    "Among hymns I am the Brihat-saman; of meters, the Gayatri. "
    "Of months I am Margashirsha (late autumn); of seasons, flower-bearing spring."
)
T[(10, 36)] = (
    "I am the gambling of cheats, the splendor of the splendid. "
    "I am victory, I am determination, I am the goodness of the good."
)
T[(10, 37)] = (
    "Of the Vrishnis I am Krishna (Vasudeva); of the Pandavas, Arjuna. "
    "Of sages I am Vyasa; among poets, Ushanas."
)
T[(10, 38)] = (
    "Among those who punish, I am the rod; among those who seek victory, I am statecraft. "
    "Of secrets I am silence; I am the wisdom of the wise."
)
T[(10, 39)] = (
    "Whatever is the seed of any being — that is me, Arjuna. "
    "No being, moving or unmoving, exists without me."
)
T[(10, 40)] = (
    "There's no end to my divine glories, Arjuna. "
    "What I've said is just a brief sample of the extent of my magnificence."
)
T[(10, 41)] = (
    "Whatever is glorious, prosperous, or mighty — "
    "know that every such thing has sprung from a fragment of my splendor."
)
T[(10, 42)] = (
    "But what's the use of knowing all this in detail, Arjuna? "
    "I stand holding up this entire universe with a single fragment of myself."
)


# ============================================================================
# CHAPTER 11 — The Vision of the Cosmic Form
# ============================================================================

T[(11, 1)] = (
    "Arjuna said:\n"
    "As a favor to me, you've taught me the supreme secret known as the Self. "
    "By those words, my confusion is gone."
)
T[(11, 2)] = (
    "Lotus-eyed one, I've heard from you in detail about the origin and dissolution of beings, "
    "and about your imperishable majesty."
)
T[(11, 3)] = (
    "That's just how it is, supreme Lord, just as you've described yourself. "
    "I want to see your lordly form, supreme Person."
)
T[(11, 4)] = (
    "If you think it's possible for me to see, Lord, "
    "then, O Lord of yoga, show me your imperishable Self."
)
T[(11, 5)] = (
    "Krishna said:\n"
    "Arjuna, behold my forms — by hundreds and thousands, of different kinds, "
    "divine, of many colors and shapes."
)
T[(11, 6)] = (
    "Behold the Adityas, Vasus, Rudras, the two Ashvins, and the Maruts. "
    "Behold many wonders never seen before, Arjuna."
)
T[(11, 7)] = (
    "Right here today, see the whole universe — moving and unmoving — gathered into one "
    "in my body, Arjuna, and anything else you want to see."
)
T[(11, 8)] = (
    "But you can't see me with your own eye. "
    "I'll give you a divine eye — behold my lordly power of yoga!"
)
T[(11, 9)] = (
    "Sanjaya said:\n"
    "Having said this, O king, the great Lord of yoga, Hari (Krishna), "
    "revealed to Arjuna his supreme lordly form —"
)
T[(11, 10)] = (
    "with many mouths and eyes, with many wondrous sights, "
    "with many divine ornaments, with many divine weapons raised;"
)
T[(11, 11)] = (
    "wearing divine garlands and robes, anointed with divine perfumes — "
    "all-wonderful, radiant, infinite, with faces everywhere."
)
T[(11, 12)] = (
    "If the splendor of a thousand suns were to blaze forth all at once in the sky, "
    "it might resemble the splendor of that Great Soul."
)
T[(11, 13)] = (
    "There Arjuna saw the whole universe, in all its divisions, "
    "gathered together in the body of that God of gods."
)
T[(11, 14)] = (
    "Then, stunned with amazement, hair standing on end, Arjuna, "
    "bowing his head to the Lord, spoke with hands folded:"
)
T[(11, 15)] = (
    "Arjuna said:\n"
    "God, in your body I see all the gods and the hosts of all beings — "
    "Brahma the creator on his lotus, all the sages, and the divine serpents."
)
T[(11, 16)] = (
    "I see you with countless arms, bellies, mouths, and eyes — form without end, everywhere. "
    "I see neither your end, nor middle, nor beginning, Lord of the universe, universal form."
)
T[(11, 17)] = (
    "I see you with crown, club, and discus — a mass of brilliance blazing everywhere, "
    "hard to look at on every side, with the brilliance of blazing fire and sun, beyond measure."
)
T[(11, 18)] = (
    "You are the Imperishable, the supreme to be known; you are the final resting place of this universe. "
    "You are the eternal guardian of dharma; you, I know, are the primal Person."
)
T[(11, 19)] = (
    "Without beginning, middle, or end; of infinite power; of countless arms; "
    "with the sun and moon as your eyes, a blazing fire as your mouth, scorching this universe with your radiance — I see you."
)
T[(11, 20)] = (
    "The space between sky and earth, and all the directions, are filled by you alone. "
    "Seeing this wondrous, terrifying form of yours, the three worlds tremble, Great Soul."
)
T[(11, 21)] = (
    "The hosts of gods enter you. Some, afraid, praise you with folded hands. "
    "The great sages and perfected beings cry \"may it be well!\" and sing your glory in abundant hymns."
)
T[(11, 22)] = (
    "The Rudras, Adityas, Vasus, Sadhyas, Vishvedevas, the two Ashvins, the Maruts, the ancestors, "
    "the hosts of gandharvas, yakshas, demons, and perfected beings — they all gaze at you in wonder."
)
T[(11, 23)] = (
    "Seeing your great form, with many mouths and eyes, Arjuna, with many arms, thighs, feet, "
    "many bellies, many fearsome tusks — the worlds tremble, and so do I."
)
T[(11, 24)] = (
    "Seeing you touching the sky, blazing with many colors, mouths wide, great flaming eyes — "
    "my inmost self trembles; I find no firmness or peace, Vishnu."
)
T[(11, 25)] = (
    "Seeing your mouths, terrible with tusks, like the fires of cosmic dissolution, "
    "I lose my bearings and find no refuge. Be gracious, Lord of gods, home of the worlds."
)
T[(11, 26)] = (
    "Into you rush all the sons of Dhritarashtra, along with the hosts of kings — "
    "Bhishma, Drona, even Karna, and our chief warriors too —"
)
T[(11, 27)] = (
    "hurrying into your mouths, terrifying with tusks, horrifying to behold. "
    "Some, caught between the tusks, are seen with their heads ground to powder."
)
T[(11, 28)] = (
    "As many torrents of rivers rush toward the ocean, "
    "so do these heroes of the world of men rush into your flaming mouths."
)
T[(11, 29)] = (
    "As moths rush headlong into a blazing fire to their destruction, "
    "so these creatures rush into your mouths to their destruction."
)
T[(11, 30)] = (
    "Swallowing all the worlds on every side with your flaming mouths, you lick them up. "
    "Your fierce rays, filling the whole universe with brilliance, burn, Vishnu."
)
T[(11, 31)] = (
    "Tell me who you are, fearsome one — I bow to you, best of gods; be gracious. "
    "I want to understand you, the primal one, because I can't comprehend your purpose."
)
T[(11, 32)] = (
    "Krishna said:\n"
    "I am Time, the mighty destroyer of the worlds, set out to destroy the worlds. "
    "Even without you, none of these warriors arrayed in the opposing armies will live."
)
T[(11, 33)] = (
    "So stand up; win fame. Defeat your enemies and enjoy a prosperous kingdom. "
    "I have already killed these. You just be the outer cause, Arjuna."
)
T[(11, 34)] = (
    "Drona, Bhishma, Jayadratha, Karna, and other warrior-heroes — I have killed them. "
    "Don't hesitate. Fight — you'll defeat your enemies in battle."
)
T[(11, 35)] = (
    "Sanjaya said:\n"
    "On hearing those words of Krishna, Arjuna, trembling, folded his hands and bowed. "
    "Prostrating himself, overcome with fear, he spoke to Krishna again, stammering:"
)
T[(11, 36)] = (
    "Arjuna said:\n"
    "Rightly, Krishna, the world delights and rejoices in your praise. "
    "The demons flee in fear in all directions, and all the perfected beings bow to you."
)
T[(11, 37)] = (
    "And why wouldn't they bow to you, Great Soul — greater than even Brahma the first creator? "
    "Infinite Lord of gods, refuge of the worlds — you are the Imperishable, being and non-being, and what is beyond."
)
T[(11, 38)] = (
    "You are the primal God, the ancient Person. You are the supreme resting place of this universe. "
    "You are the knower and the known, the highest goal. By you, this universe is pervaded, infinite-formed one."
)
T[(11, 39)] = (
    "You are Vayu (the wind), Yama (death), Agni (fire), Varuna (water), the Moon, Prajapati (creator), and the great ancestor. "
    "A thousand salutations to you — again and again, salutations, salutations!"
)
T[(11, 40)] = (
    "Salutations to you from in front and from behind; salutations from every side, O all. "
    "Infinite in valor, immeasurable in might, you pervade everything — so you are everything."
)
T[(11, 41)] = (
    "Whatever I said rashly, in carelessness or in love — calling you \"Krishna,\" \"Yadava,\" \"friend,\" "
    "thinking of you as a friend, not knowing your greatness —"
)
T[(11, 42)] = (
    "and whatever disrespect I showed you, in fun — playing, resting, sitting, eating, "
    "alone or in front of others — I beg you, Unshaken One, to forgive me."
)
T[(11, 43)] = (
    "You are the father of the world — moving and unmoving — its object of worship, its most venerable teacher. "
    "There is no one equal to you — how could anyone be greater? — in the three worlds, O unmatched Power."
)
T[(11, 44)] = (
    "So I prostrate myself, bowing my body, begging your grace, adorable Lord. "
    "As father to son, as friend to friend, as lover to beloved — bear with me, God."
)
T[(11, 45)] = (
    "Seeing what was never seen before, I am full of joy — but my mind shakes with fear. "
    "Show me, God, that other form. Be gracious, Lord of gods, home of the worlds."
)
T[(11, 46)] = (
    "I want to see you as before — with crown, club, and discus in hand. "
    "Take on that four-armed form, thousand-armed one, universal form."
)
T[(11, 47)] = (
    "Krishna said:\n"
    "By my grace, Arjuna, this supreme form has been shown to you, by my own yogic power — "
    "luminous, universal, infinite, primal — seen by no one but you."
)
T[(11, 48)] = (
    "Not by study of the Vedas, nor by sacrifices, nor by gifts, nor by rituals, nor by severe austerities, "
    "can I be seen in such a form in the human world by anyone other than you, Arjuna."
)
T[(11, 49)] = (
    "Don't be afraid or bewildered by seeing this fearsome form of mine. "
    "Fearless, with a happy heart, behold once again this other form of mine."
)
T[(11, 50)] = (
    "Sanjaya said:\n"
    "Having said this, Krishna showed Arjuna his own form once again; "
    "and the Great Soul, resuming his gentle form, comforted the frightened Arjuna."
)
T[(11, 51)] = (
    "Arjuna said:\n"
    "Seeing this gentle human form of yours, Krishna, "
    "my thoughts are calm. I'm back to my natural self."
)
T[(11, 52)] = (
    "Krishna said:\n"
    "This form of mine that you saw is very hard to see. "
    "Even the gods are always eager to behold this form."
)
T[(11, 53)] = (
    "Not by the Vedas, not by austerities, not by gifts, not by sacrifice, "
    "can I be seen in the form you've seen me in."
)
T[(11, 54)] = (
    "But by undivided devotion, Arjuna, I can be known like this, truly seen, "
    "and even entered."
)
T[(11, 55)] = (
    "The one who works for me, holds me as the supreme goal, is devoted to me, "
    "free from attachment, free from hostility toward any being — comes to me, Arjuna."
)


# ============================================================================
# CHAPTER 12 — The Way of Devotion
# ============================================================================

T[(12, 1)] = (
    "Arjuna said:\n"
    "Of those who constantly worship you as you are, and those who worship the imperishable unmanifest — "
    "which of them knows yoga better?"
)
T[(12, 2)] = (
    "Krishna said:\n"
    "Those who fix their minds on me, always yoked, worship me with supreme faith — "
    "I consider them the most deeply joined."
)
T[(12, 3)] = (
    "But those who worship the Imperishable — the indefinable, unmanifest, omnipresent, "
    "unthinkable, unchanging, immovable, eternal —"
)
T[(12, 4)] = (
    "controlling the senses, even-minded toward everything, delighting in the welfare of all beings — "
    "they too reach me."
)
T[(12, 5)] = (
    "But the path is harder for those focused on the unmanifest. "
    "The unmanifest goal is very difficult for embodied beings to reach."
)
T[(12, 6)] = (
    "But those who surrender all their actions to me, with me as their goal, "
    "worship me, meditating on me with undivided yoga —"
)
T[(12, 7)] = (
    "for those whose minds have entered into me, I quickly become the rescuer "
    "from the ocean of death and rebirth, Arjuna."
)
T[(12, 8)] = (
    "Fix your mind on me alone; let your intellect rest in me. "
    "Then, without doubt, you'll live in me alone."
)
T[(12, 9)] = (
    "But if you can't steadily fix your mind on me, "
    "then try to reach me through the practice of yoga, Arjuna."
)
T[(12, 10)] = (
    "If you can't even practice, devote yourself to working for me. "
    "Just performing actions for my sake, you'll reach perfection."
)
T[(12, 11)] = (
    "If you can't do even that, taking refuge in yoga toward me, "
    "give up the fruits of all your actions — with self-control."
)
T[(12, 12)] = (
    "Knowledge is better than practice; meditation is better than knowledge; "
    "renouncing the fruits of action is better than meditation; from that renunciation, peace follows right away."
)
T[(12, 13)] = (
    "The one who hates no creature, who is friendly and compassionate to all, "
    "free from \"mine\" and \"I,\" even-minded in pleasure and pain, forgiving;"
)
T[(12, 14)] = (
    "always content, yoked, self-controlled, firm in resolve, "
    "with mind and intellect offered to me — that devotee is dear to me."
)
T[(12, 15)] = (
    "The one who doesn't disturb the world, and isn't disturbed by the world, "
    "free from delight, anger, fear, and agitation — is dear to me."
)
T[(12, 16)] = (
    "The one who wants nothing, is pure, skilled, detached, untroubled, "
    "giving up all undertakings — that devotee is dear to me."
)
T[(12, 17)] = (
    "The one who neither rejoices nor hates, neither grieves nor desires, "
    "renouncing both good and evil, full of devotion — is dear to me."
)
T[(12, 18)] = (
    "The same toward enemy and friend, the same in honor and dishonor, "
    "the same in cold and heat, in pleasure and pain, free from attachment;"
)
T[(12, 19)] = (
    "to whom blame and praise are the same, silent, content with anything, homeless, "
    "steady in mind, full of devotion — that person is dear to me."
)
T[(12, 20)] = (
    "But those who follow this nectar of dharma that I've described, with faith, with me as the supreme goal — "
    "those devotees are extremely dear to me."
)


# ============================================================================
# CHAPTER 13 — The Body and the One Who Knows It
# ============================================================================

T[(13, 1)] = (
    "Arjuna said:\n"
    "Krishna, I want to know about nature (prakriti) and Person (purusha), "
    "the field (the body) and the knower of the field, knowledge and what is to be known."
)
T[(13, 2)] = (
    "Krishna said:\n"
    "Arjuna, this body is called the \"field.\" "
    "The one who knows this field, those who see clearly call the \"knower of the field.\""
)
T[(13, 3)] = (
    "Know me also as the knower of the field in every field. "
    "Knowledge of the field and its knower — that's what I consider true knowledge."
)
T[(13, 4)] = (
    "What the field is, what its nature, its changes, where it comes from, "
    "who the knower is and what his powers — hear this briefly from me."
)
T[(13, 5)] = (
    "This has been sung by the sages in many ways — in distinct hymns, "
    "and in the well-reasoned, decisive verses of the Brahma-sutras."
)
T[(13, 6)] = (
    "The five great elements, the ego, the intellect, the unmanifest, "
    "the ten senses and the one (mind), the five fields of the senses;"
)
T[(13, 7)] = (
    "desire, aversion, pleasure, pain, the body, intelligence, steadiness — "
    "this is a brief description of the field with its changes."
)
T[(13, 8)] = (
    "Humility, honesty, non-violence, patience, uprightness, "
    "service to the teacher, purity, steadiness, self-control;"
)
T[(13, 9)] = (
    "lack of interest in sense objects, and absence of ego; "
    "insight into the suffering of birth, death, old age, and sickness;"
)
T[(13, 10)] = (
    "non-attachment, not identifying with son, wife, home, and so on; "
    "and constant evenness of mind in both desirable and undesirable events;"
)
T[(13, 11)] = (
    "and unswerving devotion to me through undivided yoga; "
    "going to solitary places, distaste for crowds of people;"
)
T[(13, 12)] = (
    "steadiness in self-knowledge, and insight into the goal of true knowledge — "
    "this is what is called knowledge; anything opposed to it is ignorance."
)
T[(13, 13)] = (
    "I'll describe what should be known — knowing which, one attains immortality: "
    "the beginningless supreme Brahman, which is said to be neither being nor non-being."
)
T[(13, 14)] = (
    "It has hands and feet everywhere, eyes, heads, and faces everywhere, "
    "ears on all sides — it stands enveloping everything in the world."
)
T[(13, 15)] = (
    "Appearing to have the qualities of all the senses, yet free from all senses; "
    "unattached, yet supporting all; free from the qualities, yet the experiencer of the qualities."
)
T[(13, 16)] = (
    "Inside and outside all beings; unmoving and also moving; "
    "because it is so subtle, it can't be grasped; it is far away — and yet near."
)
T[(13, 17)] = (
    "Undivided, yet it seems divided among beings. "
    "It should be known as the sustainer of beings — their devourer and their creator."
)
T[(13, 18)] = (
    "The Light of lights, it is said to be beyond darkness. "
    "It is knowledge, the knowable, the goal of knowledge — seated in the heart of all."
)
T[(13, 19)] = (
    "So the field, knowledge, and what is to be known have been briefly described. "
    "My devotee, understanding this, attains my state of being."
)
T[(13, 20)] = (
    "Know both nature (prakriti) and Person (purusha) to be without beginning. "
    "Know also that changes and the qualities are born of nature."
)
T[(13, 21)] = (
    "Nature is said to be the cause in the production of the body and its activities. "
    "Person is said to be the cause in the experience of pleasure and pain."
)
T[(13, 22)] = (
    "For Person, seated in nature, experiences the qualities born of nature. "
    "Attachment to the qualities is the cause of birth in good and bad wombs."
)
T[(13, 23)] = (
    "The supreme Person in this body is also called the spectator, the permitter, "
    "the sustainer, the experiencer, the great Lord, the supreme Self."
)
T[(13, 24)] = (
    "Whoever understands Person and nature with its qualities in this way — "
    "however they are living — is not born again."
)
T[(13, 25)] = (
    "Some see the Self in themselves by themselves through meditation; "
    "others by the yoga of analysis (Sankhya), and others by the yoga of action."
)
T[(13, 26)] = (
    "Yet others, not knowing, worship as they have heard from others. "
    "They too cross beyond death, sticking to what they have heard."
)
T[(13, 27)] = (
    "Arjuna, whatever being is born — moving or unmoving — "
    "know that it arises from the union of the field and the knower of the field."
)
T[(13, 28)] = (
    "Whoever sees the supreme Lord dwelling equally in all beings, "
    "imperishable among the perishing — truly sees."
)
T[(13, 29)] = (
    "For seeing the same Lord established everywhere, "
    "one doesn't destroy oneself by oneself — and so reaches the supreme goal."
)
T[(13, 30)] = (
    "The one who sees that all action is done by nature alone, "
    "and that the Self is therefore not the doer — truly sees."
)
T[(13, 31)] = (
    "When one sees the diverse states of beings as resting in the One, "
    "and their expansion as coming from that alone — then one attains Brahman."
)
T[(13, 32)] = (
    "Being without beginning and without qualities, the imperishable supreme Self, Arjuna, "
    "though dwelling in the body, neither acts nor is stained."
)
T[(13, 33)] = (
    "As all-pervading space, because of its subtlety, isn't stained, "
    "the Self, seated everywhere in the body, isn't stained either."
)
T[(13, 34)] = (
    "As the one sun lights up this whole world, "
    "the knower of the field (the Self) lights up the entire field, Arjuna."
)
T[(13, 35)] = (
    "Those who, with the eye of knowledge, perceive the distinction between field and knower, "
    "and the freedom of beings from nature — they reach the Supreme."
)


# ============================================================================
# CHAPTER 14 — The Three Qualities of Nature
# ============================================================================

T[(14, 1)] = (
    "Krishna said:\n"
    "Again I'll tell you the supreme knowledge, the best of all knowledge, "
    "by knowing which the sages have gone from this world to supreme perfection."
)
T[(14, 2)] = (
    "Resorting to this knowledge, having become like me, "
    "they are not born at creation or troubled at dissolution."
)
T[(14, 3)] = (
    "My womb is the great Brahman (nature); in it I plant the seed. "
    "From that, Arjuna, all beings are born."
)
T[(14, 4)] = (
    "Whatever forms come out of any womb, Arjuna — "
    "the great Brahman is their womb, and I am the seed-giving father."
)
T[(14, 5)] = (
    "The three qualities — sattva (purity), rajas (passion), and tamas (dullness) — "
    "born of nature, tie the imperishable embodied one down to the body, Arjuna."
)
T[(14, 6)] = (
    "Among these, sattva, because of its purity, is illuminating and healthy. "
    "It binds by attachment to happiness and attachment to knowledge."
)
T[(14, 7)] = (
    "Know that rajas is passion, the source of thirst and attachment. "
    "It binds the embodied, Arjuna, through attachment to action."
)
T[(14, 8)] = (
    "Know that tamas, born of ignorance, confuses all embodied beings. "
    "It binds through carelessness, laziness, and sleep."
)
T[(14, 9)] = (
    "Sattva attaches a person to happiness, rajas to action, Arjuna. "
    "But tamas, veiling knowledge, attaches to heedlessness."
)
T[(14, 10)] = (
    "Sattva rises by overcoming rajas and tamas; "
    "rajas rises by overcoming sattva and tamas; and tamas rises by overcoming sattva and rajas."
)
T[(14, 11)] = (
    "When the light of knowledge streams out through all the gates of this body, "
    "know that sattva is dominant."
)
T[(14, 12)] = (
    "Greed, activity, undertaking of actions, restlessness, craving — "
    "these arise when rajas is dominant, Arjuna."
)
T[(14, 13)] = (
    "Darkness, inactivity, heedlessness, and confusion — "
    "these arise when tamas is dominant, Arjuna."
)
T[(14, 14)] = (
    "If the embodied one dies while sattva prevails, "
    "they reach the pure worlds of those who know the highest."
)
T[(14, 15)] = (
    "Dying in rajas, one is reborn among those attached to action. "
    "Dying in tamas, one is reborn in the wombs of the deluded."
)
T[(14, 16)] = (
    "The fruit of good action is said to be pure — sattvic. "
    "The fruit of rajas is pain; the fruit of tamas is ignorance."
)
T[(14, 17)] = (
    "From sattva comes knowledge; from rajas, greed; "
    "from tamas, heedlessness, confusion, and ignorance."
)
T[(14, 18)] = (
    "Those established in sattva rise upward; those in rajas stay in the middle; "
    "those in tamas, settled in the lowest quality, sink down."
)
T[(14, 19)] = (
    "When one sees no agent other than the three qualities "
    "and knows that which is higher than the qualities — one attains my state of being."
)
T[(14, 20)] = (
    "Transcending these three qualities which are the source of the body, the embodied one, "
    "freed from birth, death, old age, and pain, attains immortality."
)
T[(14, 21)] = (
    "Arjuna said:\n"
    "What are the signs, Lord, by which one who has transcended these three qualities is known? "
    "How does that person behave? How do they go beyond the qualities?"
)
T[(14, 22)] = (
    "Krishna said:\n"
    "Arjuna, the one who neither hates illumination, activity, or confusion when they arise, "
    "nor longs for them when they are absent;"
)
T[(14, 23)] = (
    "who sits as if indifferent, not disturbed by the qualities; "
    "who thinks \"the qualities are doing their work\" and stands firm, unmoved;"
)
T[(14, 24)] = (
    "the same in pleasure and pain, self-contained, treating a clod, stone, and gold the same; "
    "treating the liked and disliked the same, steady, the same in praise and blame of himself;"
)
T[(14, 25)] = (
    "the same in honor and dishonor, the same toward friend and foe, "
    "giving up all undertakings — that person has gone beyond the qualities."
)
T[(14, 26)] = (
    "Whoever serves me with the unswerving yoga of devotion — "
    "going beyond the qualities, becomes fit to become Brahman."
)
T[(14, 27)] = (
    "For I am the foundation of Brahman — immortal, imperishable, "
    "of eternal dharma, and of absolute happiness."
)


# ============================================================================
# CHAPTER 15 — The Supreme Person
# ============================================================================

T[(15, 1)] = (
    "Krishna said:\n"
    "They speak of an imperishable sacred fig tree (ashvattha), with roots above and branches below. "
    "Its leaves are the Vedic hymns. Whoever knows this tree knows the Vedas."
)
T[(15, 2)] = (
    "Below and above its branches spread, fed by the three qualities of nature; "
    "its twigs are the objects of sense. Its roots, also spreading below, give rise to action in the human world."
)
T[(15, 3)] = (
    "The tree's true form isn't seen here — not its end, its beginning, or its foundation. "
    "Cutting down this firmly-rooted tree with the strong axe of non-attachment,"
)
T[(15, 4)] = (
    "one should seek that place, from which, once reached, no one returns: "
    "\"I take refuge in that primal Person, from whom the ancient stream of activity has flowed.\""
)
T[(15, 5)] = (
    "Free from pride and delusion, having conquered the evil of attachment, always abiding in the Self, "
    "desires withdrawn, freed from the pairs of opposites called pleasure and pain — "
    "the unconfused reach that imperishable abode."
)
T[(15, 6)] = (
    "Neither the sun, nor the moon, nor fire lights up that place. "
    "Having reached it, no one returns — that is my supreme abode."
)
T[(15, 7)] = (
    "An eternal part of me, becoming a living being (jiva) in the world of the living, "
    "draws to itself the mind and the five senses that rest in nature."
)
T[(15, 8)] = (
    "When the Lord of the body takes up a body and when he leaves it, "
    "he takes these along and moves on — as the wind carries scents from their sources."
)
T[(15, 9)] = (
    "Presiding over ear, eye, touch, taste, smell — and the mind — "
    "he experiences the objects of sense."
)
T[(15, 10)] = (
    "Whether leaving or staying, or experiencing, joined with the qualities — "
    "the confused don't see him; but those with the eye of knowledge see."
)
T[(15, 11)] = (
    "Striving yogis also see him seated in themselves. "
    "But the unintelligent, with unrefined selves, though striving, don't see him."
)
T[(15, 12)] = (
    "The radiance of the sun that lights up the whole world, "
    "and the radiance in the moon and fire — know that radiance to be mine."
)
T[(15, 13)] = (
    "Entering the earth, I sustain all beings by my power. "
    "Becoming the nourishing moon, I feed all plants."
)
T[(15, 14)] = (
    "Becoming the digestive fire in the body of breathing beings, "
    "joined with the inward and outward breaths, I digest the fourfold food."
)
T[(15, 15)] = (
    "And I am seated in the hearts of all. From me come memory, knowledge, and their loss. "
    "I alone am to be known through all the Vedas; I am the author of Vedanta and the knower of the Vedas."
)
T[(15, 16)] = (
    "There are two persons (purushas) in the world — the perishable and the imperishable. "
    "The perishable is all beings. The imperishable is called the unchanging."
)
T[(15, 17)] = (
    "But the supreme Person is another — called the supreme Self, "
    "the imperishable Lord who enters the three worlds and sustains them."
)
T[(15, 18)] = (
    "Since I transcend the perishable and am higher even than the imperishable, "
    "I am known in the world and in the Veda as Purushottama — the Supreme Person."
)
T[(15, 19)] = (
    "The one who, without confusion, knows me as Purushottama "
    "knows everything — and worships me with their whole being, Arjuna."
)
T[(15, 20)] = (
    "So, Arjuna, this most secret teaching has been given by me. "
    "Having understood it, one becomes wise, and has done all that needs to be done."
)


# ============================================================================
# CHAPTER 16 — Divine and Demonic Natures
# ============================================================================

T[(16, 1)] = (
    "Krishna said:\n"
    "Fearlessness, purity of heart, steadfastness in the yoga of knowledge, "
    "generosity, self-control, sacrifice, study of scripture, discipline, honesty;"
)
T[(16, 2)] = (
    "non-violence, truthfulness, absence of anger, renunciation, calm, not speaking ill of others, "
    "compassion for beings, freedom from greed, gentleness, modesty, steadiness;"
)
T[(16, 3)] = (
    "vigor, forgiveness, strength, purity, freedom from hatred, absence of arrogance — "
    "these are the marks of a person born with divine qualities, Arjuna."
)
T[(16, 4)] = (
    "Showiness, arrogance, self-importance, anger, harshness, and ignorance — "
    "these, Arjuna, belong to a person born with demonic qualities."
)
T[(16, 5)] = (
    "Divine qualities lead to liberation; demonic qualities lead to bondage. "
    "Don't grieve, Arjuna — you were born with divine qualities."
)
T[(16, 6)] = (
    "Two kinds of beings exist in this world: the divine and the demonic. "
    "I've described the divine at length. Now listen as I describe the demonic, Arjuna."
)
T[(16, 7)] = (
    "Demonic people don't know what they should do or what they should not do. "
    "Purity, good conduct, truth — none of these is in them."
)
T[(16, 8)] = (
    "\"The world has no truth,\" they say, \"no moral basis, no God. "
    "It is produced by the union of male and female, driven by lust — what else?\""
)
T[(16, 9)] = (
    "Holding such views, these lost souls — of small understanding and cruel deeds — "
    "arise as enemies of the world, aiming at its destruction."
)
T[(16, 10)] = (
    "Clinging to insatiable lust, full of hypocrisy, pride, and arrogance, "
    "holding corrupt ideas out of confusion, they act with impure resolve."
)
T[(16, 11)] = (
    "Consumed by endless worries ending only at death, making the satisfaction of desires their supreme goal, "
    "convinced that this is all there is —"
)
T[(16, 12)] = (
    "bound by hundreds of chains of expectation, given over to lust and anger, "
    "they strive to pile up wealth by unjust means for the gratification of their desires."
)
T[(16, 13)] = (
    "\"This I've got today; this desire I'll fulfill. "
    "This is mine; and this wealth will also be mine.\""
)
T[(16, 14)] = (
    "\"That enemy I've killed; and others too I'll kill. "
    "I'm the lord; I'm the enjoyer; I'm successful, powerful, and happy.\""
)
T[(16, 15)] = (
    "\"I'm rich and well-born. Who is equal to me? "
    "I'll sacrifice, I'll give, I'll enjoy.\" So, deluded by ignorance,"
)
T[(16, 16)] = (
    "scattered by many anxieties, caught in the net of delusion, "
    "clinging to the gratification of desires — they fall into a foul hell."
)
T[(16, 17)] = (
    "Self-important, stubborn, drunk with wealth and pride, "
    "they perform sacrifices in name only, for show, not according to the proper way."
)
T[(16, 18)] = (
    "Given to egotism, force, insolence, lust, and anger, "
    "these spiteful people hate me — seated in their own bodies and in others."
)
T[(16, 19)] = (
    "These hateful, cruel evildoers, the lowest of men, "
    "I repeatedly hurl into demonic wombs in the cycle of rebirths."
)
T[(16, 20)] = (
    "Entering demonic wombs, the confused, not attaining me from birth to birth, "
    "fall from there to an even lower state, Arjuna."
)
T[(16, 21)] = (
    "Threefold is the gateway to hell, destructive of the self: lust, anger, and greed. "
    "So a person should let go of these three."
)
T[(16, 22)] = (
    "The person freed from these three gates of darkness, Arjuna, "
    "works for their own good — and by that reaches the supreme goal."
)
T[(16, 23)] = (
    "Whoever casts aside the guidance of scripture and acts under the impulse of desire "
    "reaches neither perfection, nor happiness, nor the supreme goal."
)
T[(16, 24)] = (
    "So let scripture be your authority for deciding what to do and what not to do. "
    "Knowing what scripture prescribes, you should act here in this world."
)


# ============================================================================
# CHAPTER 17 — Three Kinds of Faith
# ============================================================================

T[(17, 1)] = (
    "Arjuna said:\n"
    "Krishna, what about those who set aside scriptural rules but still worship with faith? "
    "Is their state one of sattva, rajas, or tamas?"
)
T[(17, 2)] = (
    "Krishna said:\n"
    "The faith of embodied beings is of three kinds, born of their own nature — "
    "sattvic, rajasic, and tamasic. Listen."
)
T[(17, 3)] = (
    "Each person's faith matches their nature, Arjuna. "
    "A person is shaped by their faith: as their faith is, so are they."
)
T[(17, 4)] = (
    "Sattvic people worship the gods; rajasic, the yakshas and demons; "
    "tamasic worship ghosts and spirits."
)
T[(17, 5)] = (
    "Those who practice severe austerities not prescribed by scripture, "
    "bound by hypocrisy and ego, driven by the force of desire and passion,"
)
T[(17, 6)] = (
    "senseless, torturing the group of elements in the body — and me, dwelling within the body — "
    "know them to have demonic resolve."
)
T[(17, 7)] = (
    "The food that each person enjoys is also of three kinds — "
    "and so are sacrifice, austerity, and gifts. Hear the distinction."
)
T[(17, 8)] = (
    "Foods that promote long life, vitality, strength, health, happiness, and cheer — "
    "savory, substantial, satisfying — are dear to sattvic people."
)
T[(17, 9)] = (
    "Foods that are bitter, sour, salty, very hot, pungent, dry, and burning — "
    "causing pain, misery, and sickness — are dear to rajasic people."
)
T[(17, 10)] = (
    "Food that is stale, flavorless, rotten, decayed, leftover, and impure "
    "is dear to tamasic people."
)
T[(17, 11)] = (
    "The sacrifice offered according to proper rules by those not seeking its fruits, "
    "convinced \"this must be done\" — that is sattvic."
)
T[(17, 12)] = (
    "But the sacrifice offered aiming for results, or for show, Arjuna — "
    "know that to be rajasic."
)
T[(17, 13)] = (
    "A sacrifice done contrary to the rules — no food distributed, no sacred verses, no gifts, "
    "and no faith — is called tamasic."
)
T[(17, 14)] = (
    "Worshipping the gods, the twice-born, teachers, and the wise; purity, uprightness, celibacy, non-violence — "
    "these are called the austerity of the body."
)
T[(17, 15)] = (
    "Speech that causes no pain, truthful, pleasant and beneficial, "
    "and regular recitation of the scriptures — these are the austerity of speech."
)
T[(17, 16)] = (
    "Serenity of mind, gentleness, silence, self-control, and purity of disposition — "
    "this is called the austerity of the mind."
)
T[(17, 17)] = (
    "This threefold austerity, practiced with supreme faith by people who are yoked and aren't seeking results — "
    "is called sattvic."
)
T[(17, 18)] = (
    "Austerity performed with showiness for the sake of respect, honor, and reverence "
    "is called rajasic — unstable and fleeting."
)
T[(17, 19)] = (
    "Austerity practiced out of foolish notions, with self-torture, "
    "or aimed at ruining someone else — is called tamasic."
)
T[(17, 20)] = (
    "A gift given with the thought \"it ought to be given,\" to someone who can't repay, "
    "at the proper place, time, and to a worthy person — that gift is considered sattvic."
)
T[(17, 21)] = (
    "A gift given grudgingly, or with the expectation of return, or aiming at the result — "
    "is considered rajasic."
)
T[(17, 22)] = (
    "A gift given in the wrong place, at the wrong time, to the unworthy, "
    "without respect, with contempt — is called tamasic."
)
T[(17, 23)] = (
    "\"Om Tat Sat\" — this is said to be the threefold designation of Brahman. "
    "By these, long ago, the brahmins, the Vedas, and the sacrifices were established."
)
T[(17, 24)] = (
    "So, beginning with \"Om,\" acts of sacrifice, gift, and austerity as prescribed in scripture "
    "are always begun by those who know Brahman."
)
T[(17, 25)] = (
    "With the word \"Tat,\" without aiming at results, the various acts of sacrifice, austerity, "
    "and gift are performed by those seeking liberation."
)
T[(17, 26)] = (
    "The word \"Sat\" is used in the sense of reality and in the sense of goodness; "
    "and for an auspicious act too, Arjuna, the word \"Sat\" is used."
)
T[(17, 27)] = (
    "Steadiness in sacrifice, austerity, and gift is also called \"Sat\"; "
    "and action for the sake of That is indeed called \"Sat.\""
)
T[(17, 28)] = (
    "Whatever is sacrificed, given, or performed — and whatever austerity is done — without faith "
    "is called \"asat,\" Arjuna. It is nothing here and nothing in the hereafter."
)


# ============================================================================
# CHAPTER 18 — Freedom Through Letting Go
# ============================================================================

T[(18, 1)] = (
    "Arjuna said:\n"
    "Krishna, I want to understand the truth of renunciation (sannyasa) — "
    "and also of letting go of action (tyaga) — each separately."
)
T[(18, 2)] = (
    "Krishna said:\n"
    "The sages understand renunciation as giving up desire-driven actions; "
    "the wise call tyaga the letting go of the fruits of all actions."
)
T[(18, 3)] = (
    "Some thinkers say action should be abandoned because it's flawed; "
    "others say acts of sacrifice, gift, and austerity should not be given up."
)
T[(18, 4)] = (
    "Hear my conclusion on this matter of tyaga, Arjuna. "
    "Tyaga has been declared to be of three kinds."
)
T[(18, 5)] = (
    "Acts of sacrifice, gift, and austerity should not be abandoned — they should be done. "
    "Sacrifice, gift, and austerity purify the wise."
)
T[(18, 6)] = (
    "But even these actions should be done while letting go of attachment and fruits — "
    "Arjuna, this is my final, decisive opinion."
)
T[(18, 7)] = (
    "Giving up an obligatory action is not proper. "
    "Giving it up out of confusion is called tamasic renunciation."
)
T[(18, 8)] = (
    "Whoever abandons action because it's painful — afraid of bodily trouble — "
    "performs rajasic renunciation; they won't get its real fruit."
)
T[(18, 9)] = (
    "But when an obligatory action is done, Arjuna, while letting go of attachment and fruit, "
    "because it simply ought to be done — that letting go is considered sattvic."
)
T[(18, 10)] = (
    "The sattvic renunciate, of steady intellect and cut-through doubts, "
    "neither hates unpleasant action nor is attached to pleasant action."
)
T[(18, 11)] = (
    "An embodied being can't give up actions completely. "
    "But whoever lets go of the fruits of action — that person is called the renouncer."
)
T[(18, 12)] = (
    "Undesired, desired, and mixed — threefold is the fruit of action that comes after death "
    "to those who haven't let go. But for those who have renounced, there's no such fruit."
)
T[(18, 13)] = (
    "Listen to these five causes for the accomplishment of all actions, Arjuna, "
    "as declared in the conclusions of Sankhya:"
)
T[(18, 14)] = (
    "the body, the agent, the various instruments, "
    "the various and distinct activities, and divine providence as the fifth."
)
T[(18, 15)] = (
    "Whatever action a person undertakes with body, speech, or mind — "
    "right or wrong — these five are its causes."
)
T[(18, 16)] = (
    "Given that, whoever — with an untrained understanding — sees only the pure Self as the agent "
    "is dull-witted and does not see."
)
T[(18, 17)] = (
    "Whose state is free from ego, whose intellect is unstained — "
    "though they kill these people, they don't really kill, and aren't bound."
)
T[(18, 18)] = (
    "The knower, the object of knowledge, and the knowledge itself — these three move action. "
    "The instrument, the action, and the agent — these three make up action."
)
T[(18, 19)] = (
    "In Sankhya teaching, knowledge, action, and agent are each said to be of three kinds, "
    "according to the three qualities of nature. Hear about these too."
)
T[(18, 20)] = (
    "The knowledge by which one sees in all beings the one, imperishable Being — "
    "undivided in the divided — know that knowledge to be sattvic."
)
T[(18, 21)] = (
    "The knowledge that sees in all beings various distinct entities of different kinds — "
    "know that to be rajasic."
)
T[(18, 22)] = (
    "But the knowledge which clings to one effect as though it were everything, without reason, "
    "without basis in truth, and trivial — is called tamasic."
)
T[(18, 23)] = (
    "An obligatory action done without attachment, without desire or hatred, "
    "by one who seeks no fruit — is called sattvic."
)
T[(18, 24)] = (
    "But the action done with great effort by one who seeks results, "
    "or impelled by ego — is called rajasic."
)
T[(18, 25)] = (
    "An action begun out of confusion, without regard for consequences, loss, injury, or ability — "
    "is called tamasic."
)
T[(18, 26)] = (
    "Free from attachment, not talking about \"me,\" endowed with firmness and energy, "
    "unmoved by success or failure — that agent is called sattvic."
)
T[(18, 27)] = (
    "Passionate, desiring the fruit of action, greedy, naturally harmful, impure, "
    "full of joy and sorrow — that agent is called rajasic."
)
T[(18, 28)] = (
    "Unyoked, vulgar, stubborn, deceitful, malicious, lazy, "
    "depressed, and procrastinating — that agent is called tamasic."
)
T[(18, 29)] = (
    "Now listen, Arjuna, to the threefold division of intellect and steadiness "
    "according to the qualities — I'll tell you fully and separately."
)
T[(18, 30)] = (
    "The intellect that knows action and restraint from action, what should be done and what shouldn't, "
    "fear and fearlessness, bondage and liberation, Arjuna — that is sattvic."
)
T[(18, 31)] = (
    "The intellect that doesn't rightly understand what is dharma and what is not, "
    "what should be done and what shouldn't — that, Arjuna, is rajasic."
)
T[(18, 32)] = (
    "The intellect that, enveloped in darkness, takes unrighteousness for righteousness "
    "and sees everything the wrong way — that is tamasic, Arjuna."
)
T[(18, 33)] = (
    "The unwavering steadiness with which, through yoga, a person controls the functions "
    "of the mind, life-breaths, and senses — that steadiness is sattvic."
)
T[(18, 34)] = (
    "But the steadiness by which one holds on to dharma, pleasure, and wealth, Arjuna, "
    "with attachment and craving for fruits — that steadiness is rajasic."
)
T[(18, 35)] = (
    "The steadiness with which a foolish person doesn't give up sleep, fear, grief, depression, and conceit — "
    "that steadiness, Arjuna, is tamasic."
)
T[(18, 36)] = (
    "Now hear from me, Arjuna, the three kinds of happiness "
    "that come after long practice and bring the end of pain."
)
T[(18, 37)] = (
    "The happiness that seems like poison at first but turns into nectar in the end, "
    "born of the clear insight of the Self — is called sattvic."
)
T[(18, 38)] = (
    "The happiness that arises from sense contact — like nectar at first, poison in the end — "
    "is considered rajasic."
)
T[(18, 39)] = (
    "Happiness that confuses the self from beginning to end, "
    "coming from sleep, laziness, and heedlessness — is called tamasic."
)
T[(18, 40)] = (
    "There is no being on earth or even in heaven among the gods "
    "who is free from these three qualities born of nature."
)
T[(18, 41)] = (
    "The duties of brahmins, warriors, merchants, and laborers, Arjuna, "
    "are distributed according to the qualities born of their own nature."
)
T[(18, 42)] = (
    "Calm, self-control, austerity, purity, patience, uprightness, "
    "knowledge, realization, and faith in the spiritual — these are the natural duties of the brahmin."
)
T[(18, 43)] = (
    "Valor, vigor, firmness, skill, not running from battle, generosity, and a leader's nature — "
    "these are the natural duties of the warrior."
)
T[(18, 44)] = (
    "Farming, cattle-rearing, and trade are the natural duties of the merchant. "
    "Work consisting of service is the natural duty of the laborer."
)
T[(18, 45)] = (
    "A person reaches perfection by being engaged in their own duty. "
    "Hear how one engaged in their own duty reaches perfection."
)
T[(18, 46)] = (
    "By worshipping, through his own work, the One from whom the activity of all beings flows "
    "and by whom all this is pervaded — a person reaches perfection."
)
T[(18, 47)] = (
    "Better to do your own duty imperfectly than someone else's duty perfectly. "
    "Doing the work that comes from your own nature, you don't incur sin."
)
T[(18, 48)] = (
    "Don't abandon the duty you are born to, Arjuna, even if it is flawed. "
    "Every undertaking is wrapped in some flaw, as fire is wrapped in smoke."
)
T[(18, 49)] = (
    "With an intellect unattached everywhere, with the self under control, free from desire — "
    "through renunciation one attains the supreme perfection of freedom from action."
)
T[(18, 50)] = (
    "How, once perfected, one reaches Brahman — the supreme culmination of knowledge — "
    "hear from me in brief, Arjuna."
)
T[(18, 51)] = (
    "With a pure intellect, restraining the self by firmness, giving up sound and the other sense-objects, "
    "setting aside attraction and aversion;"
)
T[(18, 52)] = (
    "living in solitude, eating lightly, controlling body, speech, and mind, "
    "always intent on the yoga of meditation, taking refuge in dispassion;"
)
T[(18, 53)] = (
    "giving up ego, force, arrogance, desire, anger, and possession; "
    "free from \"mine,\" at peace — one becomes fit to become Brahman."
)
T[(18, 54)] = (
    "Having become Brahman, serene in self, one neither grieves nor desires. "
    "The same toward all beings, one attains supreme devotion to me."
)
T[(18, 55)] = (
    "Through devotion one comes to know me — how great I am, who I truly am. "
    "Knowing me in truth, one enters into me at once."
)
T[(18, 56)] = (
    "Performing all actions, always taking refuge in me, "
    "by my grace one reaches the eternal, imperishable abode."
)
T[(18, 57)] = (
    "Mentally surrendering all actions to me, with me as the highest goal, "
    "resorting to the yoga of the intellect — always fix your mind on me."
)
T[(18, 58)] = (
    "With your mind on me, you'll cross all difficulties by my grace. "
    "But if, out of ego, you won't listen, you'll be lost."
)
T[(18, 59)] = (
    "If, clinging to ego, you think \"I will not fight\" — "
    "your resolve is useless. Your nature will compel you."
)
T[(18, 60)] = (
    "Bound, Arjuna, by your own karma born of your nature, "
    "you will helplessly do what, out of confusion, you don't want to do."
)
T[(18, 61)] = (
    "The Lord lives in the hearts of all beings, Arjuna, "
    "making all beings spin as if mounted on a machine, by his illusory power."
)
T[(18, 62)] = (
    "Take refuge in him alone, with all your being, Arjuna. "
    "By his grace you'll attain supreme peace and the eternal abode."
)
T[(18, 63)] = (
    "So the wisdom more secret than any secret has been told to you by me. "
    "Reflect on it fully — then do as you wish."
)
T[(18, 64)] = (
    "Listen again to my supreme word — the most secret of all. "
    "You are deeply loved by me; so I'll tell you, for your welfare."
)
T[(18, 65)] = (
    "Fix your mind on me, be devoted to me, offer to me, bow to me. "
    "You'll come to me — truly, I promise — because you are dear to me."
)
T[(18, 66)] = (
    "Let go of all dharmas and take refuge in me alone. "
    "I will free you from all sins. Do not grieve."
)
T[(18, 67)] = (
    "Never share this teaching with someone without discipline, without devotion, "
    "who doesn't want to listen, or who speaks ill of me."
)
T[(18, 68)] = (
    "Whoever teaches this supreme secret to my devotees, "
    "practicing supreme devotion to me, will without doubt come to me."
)
T[(18, 69)] = (
    "Among humans, no one does more precious service to me than that person, "
    "and no one on earth will be more beloved by me."
)
T[(18, 70)] = (
    "And whoever studies this righteous dialogue between us — "
    "by them, I shall be worshipped through the sacrifice of knowledge. That's my conviction."
)
T[(18, 71)] = (
    "Even the person who, full of faith and without ill-will, simply listens to it — "
    "even they, liberated, will attain the auspicious worlds of the meritorious."
)
T[(18, 72)] = (
    "Have you heard this, Arjuna, with a one-pointed mind? "
    "Has the delusion born of your ignorance been destroyed?"
)
T[(18, 73)] = (
    "Arjuna said:\n"
    "My delusion is destroyed; I've regained my right understanding by your grace, Krishna. "
    "I stand free from doubt. I will do as you say."
)
T[(18, 74)] = (
    "Sanjaya said:\n"
    "Thus I heard this dialogue between Krishna and the noble Arjuna — "
    "wonderful, making the hair stand on end."
)
T[(18, 75)] = (
    "By the grace of Vyasa, I heard this supreme secret of yoga "
    "directly from Krishna, the Lord of yoga, who declared it in person."
)
T[(18, 76)] = (
    "O king, as I recall again and again this wondrous and sacred dialogue "
    "between Krishna and Arjuna, I rejoice again and again."
)
T[(18, 77)] = (
    "And as I remember again and again that most wondrous form of Hari (Krishna), "
    "my wonder is great, O king, and I rejoice again and again."
)
T[(18, 78)] = (
    "Wherever Krishna is — the Lord of yoga — wherever Arjuna is — the wielder of the bow — "
    "there, I am convinced, are fortune, victory, prosperity, and sound judgment."
)


def build():
    out = {
        "source_sanskrit": "bhagavad_gita_sanskrit.json",
        "translation_style": "plain-modern",
        "translator": "Claude (Opus 4.7) — original, plain-modern English rendering from the Sanskrit",
        "notes": (
            "A plain, modern English translation meant for ordinary readers with no "
            "background in Sanskrit or the Gita. Faithful to meaning but free of "
            "archaic style. Speakers are named directly (Krishna, Arjuna, Sanjaya). "
            "Central Sanskrit terms (dharma, karma, yoga, atman, Brahman, guna) are "
            "translated in context and kept untranslated only where the English "
            "flattens the meaning."
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

    (ROOT / "bhagavad_gita_english_plain.json").write_text(
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
