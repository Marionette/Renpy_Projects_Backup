# The script of the game goes in this file.


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Fangfei = Character("[fangfei]", color="#fea5a0")
define Lixue = Character("[lixue]", color="#fea5a0")
define Muqing = Character("[muqing]", color="#fea5a0")
define Mengdie = Character("[mengdie]", color="#fea5a0")
define Bird = Character("Bird", color="#fea5a0")

# Declare BGs here

image bg courtyard = "/bg/day_courtyard.png"
image bg night_courtyard = "/bg/night_courtyard.png"
image bg spring_courtyard = "/bg/spring_courtyard.png"
image bg room = "/bg/room.jpg"
image bg night_room = "/bg/night_room.jpg"
image bg realm = "/bg/realm.png"
image pink = "#fff7f8"
image credits = "credits.png"

# Declare CGs here

image CG_intro = "/cg/cg_intro.png"
image CG_intro2 = "/cg/cg_intro2.png"
image CG_butterfly_dream = "/cg/cg_butterfly_dream.png"
image CG_butterfly_dream2 = "/cg/cg_butterfly_dream2.png"
image CG_fight = "/cg/cg_fight.png"
image CG_fight2 = "/cg/cg_fight2.png"
image CG_death = "/cg/cg_death.png"
image CG_finale = "/cg/cg_finale.png"


# Declare music here
#define audio.Action_Intro = "/audio/music/Action (Intro).ogg"
#define audio.Action_Loop = "/audio/music/Action (Loop).ogg"
#define audio.Peaceful_Intro = "/audio/music/Peaceful (Intro).ogg"
#define audio.Peaceful_Loop = "/audio/music/Peaceful (Loop).ogg"
#define audio.Sad_Intro = "/audio/music/Sad (Intro).ogg"
#define audio.Sad_Loop = "/audio/music/Sad (Loop).ogg"
#define audio.Suspenseful_Intro = "/audio/music/Suspenseful (Intro).ogg"
#define audio.Suspenseful_Loop = "/audio/music/Suspenseful (Loop).ogg"

# Declare sfx here
define audio.impact = "/audio/sfx/impact.mp3"
define audio.sword = "/audio/sfx/sword.mp3"
define audio.slash = "/audio/sfx/slash.mp3"

# Check if story completed

$ persistent.complete = False

# The game starts here.

label start:

    # PART I
    #play music Sad_Intro
    #queue music Sad_Loop
    play music "<loop 21.745>/audio/music/Sad (Full).ogg"
    scene CG_intro with fade
    "From that moment on, my life became hers."
    "Under the cold snow, the dark sky, my body could no longer move. My shaky breaths no longer condensed to white mist before me."
    "Snowflakes fell, enveloping me in the only flowers I was ever allowed to touch."
    "These were the only flowers I would receive for my death; these were the only mourning clothes anything would don for me."
    "The heavens would bury me with frozen tears, and once spring came, I would disappear with the melted snow, having never once felt love."
    "I could not even cry."
    "I, who had been born a lonesome, unwanted child, slowly closed my eyes for the last time."
    scene CG_intro2 with dissolve
    "Before my eyelids fell shut, I saw a fairy."
    $ fangfei = "Fairy"
    Fangfei "We share some of our fate together."
    "She tenderly lifted me up in her arms, without a single care that I might stain her pure white garments. Her slender fingers dispelled the chill in my bones."
    Fangfei "If you survive past this night, I will take you in as my disciple."
    "With a quiet murmur, she brought me away."
    stop music fadeout 3.0

    ##
    scene bg room with fade
    "I slept for a long time. Opening my eyes to an unfamiliar ceiling, I awoke under thick, warm blankets soft as new."
    play music "<loop 18.701 >/audio/music/Peaceful (Full).ogg"
    #play music Peaceful_Intro
    #queue music Peaceful_Loop
    "I felt so comfortable that I wanted to go back to sleep and melt in the blankets, but I was afraid that the warmth would vanish like a dream if I slept again."
    "Sitting myself up, I saw her."
    $ lixue = "Girl"
    show small_lixue neutral with dissolve
    Lixue "......"
    "This warmth wasn\'t a dream."
    hide small_lixue
    show fangfei squint_blush mild with dissolve
    Fangfei "Good morning."
    "She placed a cool hand on my forehead. I hadn\'t known that other people\'s hands could feel this soothing and unconsciously leaned forward."
    show fangfei open calm with dissolve
    Fangfei "You\'re still slightly feverish."
    show fangfei talk with dissolve
    Fangfei "I found you in the snow three nights ago and picked you up."
    "She picked up a kettle by the bed and poured a cup of water, placing it in my hands. As if she was unsure if I could hold the cup, her hands lingered on mine for a moment."
    show fangfei mild with dissolve
    Fangfei "Come, drink some water."
    "I glanced at her and at the water before I placed my mouth on the cup and drank."
    "The water quenched a thirst I had not yet been aware of, rolling down my parched throat, and reminded me that I had been asleep for a long time."
    "Sweet, the water tasted sweet."
    "I stared at her. I couldn\'t read her expression, but I thought that I liked her. This beautiful person, I thought that I liked her."
    show fangfei closed talk with dissolve
    Fangfei "I had the feeling you would be awaking soon."
    show fangfei open speak with dissolve
    Fangfei "You must be hungry. Wait here as I get a bowl of congee from the kitchen."
    hide fangfei
    show small_lixue nervous with dissolve
    Lixue "Okay."
    "With soft footsteps, she left the room."
    "I looked around the room from the bed. I had never been in a room like this, never slept in a bed like this, never even had a chance to think about this."
    show small_lixue hesitant with dissolve
    "A soft fragrance like peaches tickled my nose. She smelled like this, or this smelled like her."
    "Soon enough, she returned with a bowl of congee."
    "I ate the congee and couldn\'t help but notice that she had burnt it a little. This congee, how clumsily made it was."
    "I glanced at her. She must have made it herself even though she seemed to be the type to have never cooked before. The thought elicited a gentle warmth in my stomach."
    show small_lixue closed_eyes calm with dissolve
    "This person made food for me."
    "How delicious this was."
    show small_lixue open hesitant with dissolve
    "When I finished eating, she poured me another cup of water."
    hide small_lixue
    show fangfei serious with dissolve
    Fangfei "Are you willing to become my disciple?"
    "I had yet to place the cup to my mouth when she spoke, which was good luck on my part for I would have choked, making me the most short lived disciple in history."
    hide fangfei
    show small_lixue confused with dissolve
    Lixue "Disciple...?"
    hide small_lixue
    show fangfei serious with dissolve
    Fangfei "Yes. When I met you at the base of the mountain, I knew that we shared some of our fate together. Since you\'ve survived to this day, I must ask you to be my disciple."
    "The words she spoke made me wonder."
    "In this world existed two types of people: cultivators and mere mortals."
    "Cultivators were the heroes of fantastical stories. They practiced mystical arts and vanquished monsters. They knew both magic and martial arts."
    "The good fought the bad, maintaining the balance of the realm."
    "Their bodies and souls were resilient, as if they were immortal. Whereas a mortal might live eighty years, a cultivator would live much longer, hundreds, thousands of years."
    "At the end of their epic journeys, they would ascend to the heavens to become truly immortal."
    "So the stories went."
    "This was only wishful thinking, but who didn\'t like fantastical stories? Even I, as a child, had wanted to be rescued by such a hero or to become the protagonist of such a story."
    hide fangfei
    show small_lixue happy with dissolve
    Lixue "Are you a cultivator?"
    hide small_lixue
    show fangfei calm with dissolve
    Fangfei "Yes."
    "Calmly, without hesitation, she said that single word, so much so that I could hardly believe my ears."
    hide fangfei
    show small_lixue nervous with dissolve
    Lixue "...Am I qualified?"
    hide small_lixue
    show fangfei mild with dissolve
    Fangfei "Yes. I am merely following the Heavenly Way."
    show fangfei talk with dissolve
    Fangfei "I was an elder of the Dalin Sect, but I came here to practice closed door cultivation."
    Fangfei "Surely this has no bearing here, where even the major sects are unfamiliar to civilians, but that is what I may say for my credentials as a teacher."
    show fangfei confident with dissolve
    Fangfei "You would be my first and last disciple."
    "A pause, like she had forgotten something."
    show fangfei serious with dissolve
    Fangfei "Given that you accept my tutelage."
    "I wondered again, if I blinked, if I would wake up and realize that this was all a dream. Afraid to even breathe, I looked at my reflection in the water in the cup."
    hide fangfei
    show small_lixue teary with dissolve
    "I complained to the heavens that even in a dream, I could not hold back my tears."
    "Even if this were a dream, I wanted to enjoy it for as long as I could."
    show small_lixue closed_eyes teary_closed with dissolve
    "My heart had long decided on that."
    show small_lixue open teary_smile with dissolve
    Lixue "If someone like me is acceptable..."
    Lixue "Then, please teach me well, Master."
    $ fangfei = "Master"
    hide small_lixue
    show fangfei closed confident with dissolve
    Fangfei "Of course."
    show fangfei open with dissolve
    "I knew not of the etiquette between student and teacher, cultivator to cultivator, but she didn\'t mind. She did not say a single demeaning word."
    "A peaceful air lingered around her eyes as we exchanged promises to that relationship."
    show fangfei calm with dissolve
    Fangfei "I\'ve gone out of order, haven\'t I?"
    Fangfei "I am Bai Fangfei. White like the clouds, fragrant, rich in aroma."
    show fangfei squint mild with dissolve
    Fangfei "What is your name?"
    "I, an uncherished child, could not even give her my name."
    hide fangfei
    show small_lixue hesitant with dissolve
    Lixue "...I don\'t have one."
    Lixue "Master, please give me a name."
    hide small_lixue
    show fangfei open mild with dissolve
    Fangfei "Then I will call you Lixue. A pretty little disciple I picked up in the snow. Isn\'t it a fine name?"
    "Yet she thus gave one to me instead, a wonderful name."
    $ lixue = "Lixue"
    hide fangfei
    show small_lixue smile with dissolve
    Lixue "Lixue."
    show small_lixue closed_eyes happy with dissolve
    Lixue "Yes, thank you for the name."
    "Warmth bubbled in my heart. It was too much, so much that I wanted to never awaken from this dream-like reality. That was my wish, my childish, singular, most precious wish."
    hide small_lixue
    show fangfei confident with dissolve
    Fangfei "Rest and recover well, my dear disciple."
    "She gently pet my head."
    show fangfei mild with dissolve
    Fangfei "Our lessons will begin once your fever subsides."

    ##
    scene bg courtyard with fade
    "I recuperated under her attentive care. Soon enough, winter came to an end."
    "Following after her like a duckling, I listened to her introduce our home. My eyes darted about, taking in the scenery of this humble abode atop a mountain."
    show fangfei sure with dissolve
    Fangfei "This place is named Juyi Peak."
    Fangfei "You and I are its sole inhabitants, aside from the plants and the animals."
    show fangfei confident with dissolve
    Fangfei "I do not enforce many rules like the major sects, and you need not memorize those of even the Dalin Sect. You are not a caged bird."
    show fangfei declare with dissolve
    Fangfei "Just know to follow a righteous path. If I teach you well, then there will be no issues."
    show fangfei serious with dissolve
    "I nodded."
    "We walked and reached a very soothing place. One item caught my eye; a flowerless tree stood by its lonesome self in this courtyard filled with tranquility."
    "I must have paused in my steps for she stopped as well."
    "Before the bare branches of this special tree, we conversed about a topic that I, at that time, did not yet understand."
    show fangfei talk with dissolve
    Fangfei "Are you curious about something, Lixue?"
    hide fangfei
    show small_lixue open sad with dissolve
    Lixue "Yes, I couldn\'t help but notice this tree."
    hide small_lixue
    show fangfei resigned with dissolve
    Fangfei "Are you thinking: is the tree dead or alive?"
    hide fangfei
    show small_lixue confused with dissolve
    Lixue "Surely it must be alive, right, Master?"
    hide small_lixue
    show fangfei thoughtful with dissolve
    Fangfei "Even though she does not flower?"
    hide fangfei
    show small_lixue serious with dissolve
    Lixue "Yes. I thought it was odd, but... does a tree need to flower to be alive? I think it looks lonely. Maybe its flowers are just late this year."
    hide small_lixue
    show fangfei closed resigned with dissolve
    Fangfei "You\'re right. The tree is alive."
    hide fangfei
    show small_lixue calm with dissolve
    Lixue "So it is."
    hide small_lixue
    show fangfei open serious with dissolve
    Fangfei "She is a peach tree, my peach tree, but even if spring comes, the tree will not flower nor will it ever bear fruit."
    show fangfei convicted with dissolve
    Fangfei "When she withers, I will ask you to cut her down from the roots."
    hide fangfei
    show small_lixue hesitant with dissolve
    Lixue "Could I not nourish the tree?"
    hide small_lixue
    show fangfei concerned with dissolve
    Fangfei "My kind hearted disciple, is the tree not in more pain if she must persist even as she rots from the roots?"
    hide fangfei
    show small_lixue neutral with dissolve
    Lixue "So to cut it down would be mercy?"
    hide small_lixue
    show fangfei squint thoughtful with dissolve
    Fangfei "Yes. She is a very tired tree, and even trees follow the Heavenly Way."
    "She gently pet my head."

    ##
    scene bg room with fade
    "We returned inside after the tour of Juyi Peak. She stood before a shelf of books, flipping through the selection as she began my first lesson in cultivation."
    show fangfei serious with dissolve
    Fangfei "You are not yet at the stage where you should think of taking spiritual energy into your body."
    Fangfei "To start, I will teach you about the body\'s acupoints, meridians, and dantian."
    Fangfei "Until you know them by heart, you should not try to circulate spiritual energy. Otherwise, your foundations may be shattered forever."
    "She paused, remembering that her student was still a child who had yet to learn what any of those words meant."
    show fangfei convicted with dissolve
    Fangfei "You could die."
    hide fangfei
    show small_lixue calm with dissolve
    Lixue "Thank you for the guidance, Master."
    hide small_lixue
    show fangfei sure with dissolve
    Fangfei "How could I not tell you the dangers of being too enthusiastic? If you broke yourself in some mistaken haste, I would be left with no disciple."
    hide fangfei
    show small_lixue happy with dissolve
    Lixue "I\'ll be careful and meticulous."
    hide small_lixue
    show fangfei closed mild with dissolve
    Fangfei "Good."
    show fangfei open with dissolve
    "Some books, she returned to the shelf. Others, she placed at the crook of her arm, balancing them."
    "Once she finished, we moved to a desk, and she placed the books down in a pile."
    Fangfei "Study these books well. I will teach you with them."
    "Spotting the plethora of words crawling about the diagrams drawn in the books, my eyes spun and my stomach fell."
    "A little panicked, I tugged at her sleeve and looked to the ground."
    "Would she abandon a useless disciple who couldn\'t learn?"
    hide fangfei
    show small_lixue nervous with dissolve
    Lixue "Master, I... don\'t know how to read or write."
    "I let go of her sleeve like I had been burnt for such an act was probably inappropriate. Before I met her, no one cared to teach me a single thing but to be unseen and forgotten."
    "The dirty child was scared."
    hide small_lixue
    show fangfei squint confident with dissolve
    Fangfei "Then all I have to do is teach you."
    "She gently pet my head, and my anxiety flew away."
    show fangfei open speak with dissolve
    Fangfei "Lixue, no one is born knowing everything. What\'s important is that you are willing to learn. Are you?"
    hide fangfei
    show small_lixue teary_smile with dissolve
    Lixue "Y-yes! I\'m willing."
    hide small_lixue
    show fangfei sure with dissolve
    Fangfei "Good."
    "She placed the anatomy books to the side, retrieving an ink grinder, brush, and paper."
    Fangfei "I am no calligraphy master, but I will still teach you well."
    "She grinded some ink."
    show fangfei mild with dissolve
    Fangfei "First, would you like to write your name?"
    hide fangfei
    show small_lixue confused with dissolve
    Lixue "Could I learn to write yours first?"
    hide small_lixue
    show fangfei surprised with dissolve
    Fangfei "You would prefer that?"
    hide fangfei
    show small_lixue mild with dissolve
    Lixue "Yes."
    show small_lixue smile with dissolve
    Lixue "Since I like Master a lot."
    hide small_lixue
    show fangfei mild with dissolve
    Fangfei "My disciple has a sweet tongue, doesn\'t she?"
    Fangfei "Alright. Then watch my strokes as I write each character. This is Bai Fangfei."
    "She wrote; I watched. Meticulously and slowly, the brush moved, and I seared it into my mind, her name made of three characters."
    "When she finished, she placed the brush into my hand for me to copy and practice writing. As I had never even held a brush before, she cupped my hand and guided me to write."
    "The first words I wrote in this lifetime were the three characters of her name."
    "Such shaky characters appeared on the paper that I felt embarrassed to have written her name when she and hers were so pretty."
    show fangfei sure with dissolve
    Fangfei "Talented strokes."
    hide fangfei
    show small_lixue sad with dissolve
    Lixue "But they look so ugly."
    hide small_lixue
    show fangfei serious with dissolve
    Fangfei "Everyone starts somewhere. Not even a bird knows how to fly when it first hatches. Lixue, try writing those characters again."
    "I followed her instructions, copying her name once more. Glancing at her original example, I did my best to make no mistakes. I wouldn\'t forget how to write that name."
    show fangfei declare with dissolve
    Fangfei "See how you\'ve learned to hold the brush better."
    show fangfei sure with dissolve
    "She adjusted my grip only a little, letting me try writing again."
    Fangfei "And how your strokes are fluider than before."
    "I copied the characters again and again. With each practice, I saw shaky lines turn smoother. I could not reach the perfection I sought, but her praise warmed my chest."
    "She taught me how to write my own name next."
    "Then she taught me many other words as well."
    "When I grew tired of characters, she taught me how to grind ink. Good ink was not too watery nor too thick. Black on the grinder, she taught me the consistency just right for the brush."
    "Secretly, I enjoyed grinding down the ink stone, rubbing it up and down. She may have noticed as from that time on, she allowed me to do it more often than not."
    "Before I realized, summer came and went."
    stop music fadeout 3.0

    ##
    scene bg courtyard with fade
    play music "<loop 25.600>/audio/music/Suspenseful (Full).ogg"
    #play music Suspenseful_Intro
    #queue music Suspenseful_Loop
    "Fall passed filled with studies, and once more winter arrived."
    "I memorized the details of the body within a few months. I felt like a scholar, reading and writing all day, and she taught me how to meditate and feel the spiritual energy in the air."
    "Still, I could only say I was only on step zero."
    "Unable to circulate spiritual energy, I had to eat physical food. What kind of immortal cultivator was I?"
    "Master told me to eat to grow strong. Her disciple could not be stunted by an overreliance on pills, and Master\'s cooking was the most delicious food in the world anyway."
    "However, I could not help but wonder if I was a good disciple, a useful disciple."
    "To enter the Qi Condensation stage, I had to use spiritual energy to refine my body from the inside out."
    "Learning to gather and scatter spiritual energy, I would take my first steps onto the path of cultivation once I opened my meridians and dantian."
    "How many people had tried and failed? How many people had stagnated before they could even break free from their mortal shells?"
    "In this world where no one had ascended for thousands of years, I simply wanted to successfully take the first step."
    show small_lixue worried with dissolve
    Lixue "What if I have no qualifications to cultivate?"
    "I held a fasting pill in my hand. Master had handed it to me so that I could meditate for a number of days and nights consecutively without eating."
    "The pill rolled in my palm like the wobbling of my convictions."
    hide small_lixue
    show fangfei serious with dissolve
    Fangfei "Those sorts of worries will get in the way of your cultivation. If you don\'t believe in Master, believe in the Heavenly Way."
    show fangfei stern with dissolve
    Fangfei "You will surpass me and cut down the root of calamity."
    hide fangfei
    show small_lixue calm with dissolve
    Lixue "Does Master believe in me?"
    hide small_lixue
    show fangfei squint sure with dissolve
    Fangfei "Yes. There is no one I believe in more."
    stop music fadeout 3.0
    "Rather than in the Heavenly Way, I believed in Master. I nodded and swallowed the pill."

    ##
    play music "<loop 18.701 >/audio/music/Peaceful (Full).ogg"
    #play music Peaceful_Intro
    #queue music Peaceful_Loop
    "After a while, I broke through."
    "Even though I was dirty from expelling impurities, once I had refined my body, she took my hand. The pure and clean Master believed in me, and I believed in her."
    "When I washed away the grime, I also washed away a weight from my shoulders."

    ##
    scene bg courtyard with fade
    "Something I noticed about Master: she was really valiant when she flew on her spiritual sword."
    "I told her I wanted to learn, but she said I was not yet ready for my own spiritual sword. She began to teach me martial arts and swordsmanship."
    "She tried to teach me divination, but we stopped after the basics."
    show fangfei open surprised with dissolve
    Fangfei "Even my talented disciple has weak points."
    "As I sulked at the unexpected failure, she pet my head."
    show fangfei mild with dissolve
    Fangfei "You grow up so quickly that I want to pamper you more."
    "When my fairy Master indulged me, caressing my head, I could not help but want to grow up even faster. She pampered me plenty, but I didn\'t want to be a child."
    "She, who had not gone down to the town at the base of the mountain for decades, had descended for the sake of her disciple\'s very mortal needs."
    "She looked uninterested each time she returned from town, neither excited nor dejected."
    "So unworldly she was. Once, I asked if she would ascend soon and leave me behind, but she only told me that she was far from ascending and had reached a ceiling in her cultivation."
    hide fangfei
    show small_lixue confused with dissolve
    Lixue "Master, you said that you are at Soul Transformation."
    "After the Soul Transformation stage came the Ascendant stage, after which came the final tribulation. A cultivator would ascend to true immortality in the heavens or perish."
    "She was so close, and I was so far away."
    hide small_lixue
    show fangfei serious with dissolve
    Fangfei "The last step is the hardest step."
    Fangfei "Whether a cultivator\'s spirit is at peace can determine whether or not they can avoid stagnating, much less move forward."
    hide fangfei
    show small_lixue concerned with dissolve
    Lixue "Are you speaking of heart demons?"
    "Heart demons were the monsters of the mind that haunted the spirit. Formed of regrets and obsessions, they would clog the way and hinder cultivation."
    show small_lixue worried with dissolve
    "Even worse, if let run rampant within, they would attack the cultivator, throwing the cultivator into qi deviation: an irreversible infliction of destructive madness."
    "I shuddered."
    hide small_lixue
    show fangfei thoughtful with dissolve
    Fangfei "Perhaps, but I am in no danger of qi deviation. Don\'t worry, Lixue. It\'s only that I reached a bottleneck."
    hide fangfei
    show small_lixue confused with dissolve
    Lixue "Can I catch up to you?"
    hide small_lixue
    show fangfei sure with dissolve
    Fangfei "Yes. I wish for you to catch up to me, no, for you to surpass me."
    show fangfei stern with dissolve
    Fangfei "You must not rush, Lixue. Take your time; steady your pace. We should have hundreds, if not thousands of years. I would rather you accompany me longer."
    hide fangfei
    show small_lixue mild with dissolve
    Lixue "I do too. I want to accompany you for a long time."
    "Although she lived serene like a flower—I was just about sure she subsisted off of dew—she was a forebear at the peak of the cultivation realm."
    hide small_lixue with dissolve
    "At news of unfortunate events in the town at the base of the mountain, she descended to vanquish a vengeful ghost. The ghost dispersed in an instant."
    "Due to the short incident, she brought me down on her flying sword for the first time. After all, righteous cultivators protected the realm."
    "I explored the town and secretly bought her a gift."

    ##
    scene bg night_room with fade
    "I wondered if she would like it. I hid it in my breast pocket, waiting for a time to give it to her. A gift, I had never given anyone such a thing before, but I thought it suited her."
    "I waited and waited till she noticed my waiting."
    "She combed my hair as I sat in her room. The comb and her fingers moved through my hair comfortably. She hummed as if enjoying the sensation as well."
    $ renpy.notify("GLOSSARY: an idiom about white hairs")
    "I was reminded of an idiom about white hairs of old age I saw in a book."
    show fangfei mild with dissolve
    Fangfei "Lixue, you seem distracted. Were you thinking of the ghost from a few days ago?"
    hide fangfei
    show small_lixue neutral with dissolve
    Lixue "Mm..."
    "She was not quite right, but I didn\'t know how to say that I had prepared a gift for her."
    hide small_lixue
    show fangfei closed calm with dissolve
    Fangfei "This is a good time for a lesson on evil spirits."
    show fangfei open with dissolve
    "The lesson began. We had not talked very much about them before as I had little chance of encountering any on Juyi Peak."
    "However, meticulous as she was, she illustrated the common ghouls to me and how to deal with them. As if speaking from a bestiary, her voice flowed."
    "The ghost she dispersed a few days earlier had been but an insignificant threat amidst the many dangers that lurked in the shadows. At least, it was for her. For me, perhaps it was not."
    show fangfei talk with dissolve
    Fangfei "Worse than simple ghosts or monsters are the ones under the control of demonic cultivators."
    hide fangfei
    show small_lixue thoughtful with dissolve
    Lixue "Are demonic cultivators different from demons?"
    hide small_lixue
    show fangfei convicted with dissolve
    Fangfei "Yes and no. They are cultivators who deviated from the proper path, following an unrighteous path against the Heavenly Way, playing with demonic energy."
    show fangfei stern with dissolve
    Fangfei "They often control evil spirits, so an unnatural movement of ghosts can indicate the presence of a powerful demonic cultivator. They kill and revel in their lusts."
    show fangfei frown with dissolve
    Fangfei "Walking an unnatural path, they more easily go into qi deviation. Perhaps they were mad to begin with, but their obsessions take over their bodies and souls and destroy them."
    show fangfei stern with dissolve
    Fangfei "If you are ever touched with demonic energy..."
    hide fangfei
    show small_lixue concerned with dissolve
    Lixue "......?"
    hide small_lixue
    show fangfei concerned with dissolve
    Fangfei "Cleanse yourself of it as soon as possible. I will teach you when you can."
    hide fangfei
    show small_lixue serious with dissolve
    Lixue "What happens otherwise?"
    hide small_lixue
    show fangfei closed frown with dissolve
    Fangfei "You may be led down the wrong path like them."
    hide fangfei
    show small_lixue worried with dissolve
    Lixue "And become a monster?"
    hide small_lixue
    show fangfei squint frown with dissolve
    Fangfei "That is a possibility. You may lose your mind to the whispers of the demonic energy."
    show fangfei open with dissolve
    Fangfei "Your meridians and dantian may be corrupted and your cultivation shattered, lest you follow the demonic path. You would die in that case."
    show fangfei stern with dissolve
    Fangfei "Or you might continue to live on normally. However, you should never take such risks."
    show fangfei convicted with dissolve
    Fangfei "Some say that they are more monsters than humans. Whether they are is a matter of philosophy, but they\'ve done terrible acts. What you see them as is for you to decide."
    Fangfei "Perhaps to call them monsters is rude to their victims because it was their conscious mind that chose to do those things."
    show fangfei mention with dissolve
    Fangfei "Like the Ancient Calamity."
    hide fangfei
    show small_lixue confused with dissolve
    Lixue "Ancient Calamity?"
    hide small_lixue
    show fangfei stern with dissolve
    Fangfei "She was the last grandmaster of the demonic cultivators. Deceased for thousands of years now, her trail of bloodshed still has not been forgotten. It is a long, long story."
    show fangfei hesitant with dissolve
    Fangfei "If you are curious, I will give you a history lesson tomorrow."
    show fangfei mild with dissolve
    Fangfei "In the Heavenly Way, righteousness prevails."
    "The Heavenly Way was the mandate of the gods, the way that the world was destined to be. Some who were skilled at divination could peek at that mysterious force."
    show fangfei sure with dissolve
    "When she spoke of it, she spoke with an odd sense of certainty. The Heavenly Way was fate."
    "Then she moved her hands away from my hair."
    "I wished that she would continue; I liked the feeling of her hands in my hair. Yet at least now I could move my head as I hadn\'t wanted to bother her while she was at work."
    show fangfei closed confident with dissolve
    Fangfei "My jade girl with hair like silk, who could be your golden boy?"
    "Heat pooled in my cheeks."
    show fangfei squint with dissolve
    "I turned to face her."
    hide fangfei
    show small_lixue calling with dissolve
    Lixue "Master."
    hide small_lixue
    show fangfei open mild with dissolve
    Fangfei "Yes, Lixue?"
    "I put my hand in my breast pocket, retrieving the item I bought for her. It sat coolly, hidden in my palm. Although I wondered once again if she would like it, I made up my mind."
    "The short lesson on demons gave me enough time to prepare my courage."
    hide fangfei
    show small_lixue smile with dissolve
    Lixue "I have something I would like to give you."
    "I presented it to her: a simple jade accessory."
    hide small_lixue
    show fangfei mild with dissolve
    Fangfei "Thank you."
    "She took it from my hand and put it on."
    "In hindsight, Master did not lack for jade, good spiritual jade, not even speaking of the common jade that common people used."
    show fangfei joy squint_blush with dissolve
    Fangfei "My first gift from my most beloved disciple. I\'m happy to receive this jade from you, Lixue."
    show fangfei smile squint_blush with dissolve
    Fangfei " I will treasure it."
    "I..."
    "I..."
    "At that moment, I was blinded. My mild master, her smile was so sweet. I wanted to let her smile more, and I wondered if perhaps:"
    "Was this the first time I saw her truly smile?"

    ##
    scene bg courtyard with fade
    "I continued to practice diligently under her watchful instruction."
    "The faint rumbling of thunder interrupted our modest life. Following the thunder came a brief shower of sweet rain under clear and sunny skies."
    "I broke through to the Foundation Establishment stage."
    "Meditating to stabilize the spiritual energy circulating through my body, I guided the torrents rampaging within my body, ignoring the beads of sweat rolling down my forehead."
    show small_lixue closed_eyes sweat concentrated with dissolve
    Lixue "......"
    "With my breath consciously steadied, my mind was focused entirely on cultivation."
    "After another three days and nights, I finally opened my eyes. I had moved into the second stage in record time."
    "Whereas many lingered in Qi Cultivation for their entire lives, I reached Foundation Establishment already. In exchange, I struggled through quelling the rapids of energy."
    show small_lixue open with dissolve
    "Master worried that my fast progress would become an obstacle for me in the future."
    show small_lixue relieved with dissolve
    Lixue "Master, I broke through."
    hide small_lixue
    show fangfei mild with dissolve
    Fangfei "Congratulations, Lixue."
    Fangfei "Let\'s celebrate. If you have anything you desire, voice it and I will try to obtain it for you."
    show fangfei speak with dissolve
    Fangfei "Yes and let us go visit the Dalin Sect to retrieve a few items."
    hide fangfei
    show small_lixue confused with dissolve
    Lixue "Did you leave an important item there?"
    "After refusing to return to the Dalin Sect for decades, she suddenly brought up the idea. I could not imagine what might have spurred on the initiative."
    hide small_lixue
    show fangfei surprised with dissolve
    Fangfei "Your seniors won\'t mind giving something to their elder\'s most promising disciple."
    "I blinked."
    hide fangfei
    show small_lixue smile with dissolve
    Lixue "How devious of Master."
    "I tried to control my cheek muscles."
    hide small_lixue
    show fangfei surprised with dissolve
    Fangfei "Does Lixue see me as rigid? Having a sharp mind can win you many victories."
    show fangfei confident with dissolve
    Fangfei "That aside, I am sure that they will all like you. They are all good people. Meeting more people will be a good experience. People are beloved and to be protected."
    "I tilted my head. I already had someone I loved dearly: Master. Other people, I did not particularly care for."
    "As if she heard my thoughts, she pet my head."
    show fangfei sure with dissolve
    Fangfei "Go get cleaned up."
    Fangfei "I prepared something special for you for before we head off to the sect."
    hide fangfei
    show small_lixue happy with dissolve
    Lixue "Thank you, Master. I\'ll look forward to it."
    "Bowing once, I ran off to wash away the excess impurities expelled from my body."
    hide small_lixue with dissolve
    scene bg room with dissolve
    "Afterward, I returned to Master\'s room."
    "She handed me a sword, a very special sword. I could feel its radiance from when she held it in her hands and when she stepped to approach me."
    show fangfei talk with dissolve
    Fangfei "This sword shares some of its fate with you."
    show fangfei serious with dissolve
    "With a simple declaration of fate, this and I formed a partnership."
    "As she placed it in my hands, a gentle pulse of spiritual energy rippled through me."
    $ renpy.notify("GLOSSARY: Fenghuang")
    "It was warmth, the warmth of someone\'s love for someone else, the sound of the cry of a feng and huang, a something that reminded me of Master and of someone else."
    "I nearly forgot to speak."
    hide fangfei
    show small_lixue calling with dissolve
    Lixue "...Oh!"
    show small_lixue mild with dissolve
    Lixue "I like it very much, Master!"
    hide small_lixue
    show fangfei mild with dissolve
    Fangfei "This Fenghuang Sword, I\'m sure it\'s happy that you like it."
    "And it became my partner for a long, long time."
    stop music fadeout 3.0

    ##
    "As for what I requested from Master at that time? I simply asked to continue being her pampered disciple."

    # PART II
    scene bg courtyard with fade
    "Just like that, two hundred years passed."
    play music "<loop 18.701 >/audio/music/Peaceful (Full).ogg"
    #play music Peaceful_Intro
    #queue music Peaceful_Loop
    "I grew up, but Master did not change. Just like that night from so long ago, she still seemed like a fairy who would disappear until she touched my head and reminded me she was here."
    "The lifespans of cultivators must have seemed otherworldly to the common people. If I had not been picked up by Master, my halcyon days with her would have been cut short long ago."
    "I reached Nascent Soul one year ago."
    "What she could directly teach me diminished over time. Master was not much of a sword cultivator, whereas we found that my spirit resonated with the sword."
    "At the moment, Master was in closed door cultivation. Temporarily, we could not meet."
    "What a rare occurrence that was. Master\'s cultivation had stayed where it was since we met. For a Soul Transformation forebear, perhaps her lack of movement was unrare."
    show lixue muse with dissolve
    Lixue "......"
    "Like Master\'s cultivation, the peach tree in the courtyard also remained unchanged, non-flowering."
    show lixue hope with dissolve
    Lixue "Fenghuang Sword, when will the peach tree blossom?"
    "My skills in divination had also remained unchanged. Not even an ancient spirit sword could help me."
    show lixue muse with dissolve
    "Fenghuang Sword, this partner that Master gave me, was unexpectedly an ancient treasure, yet Master had no qualms handing it to me."
    "Today as well, I practiced my sword swings."
    show lixue diligent with dissolve
    Lixue "Hm!"
    play sound sword
    "I cut a leaf that had floated before me."
    "I practiced for a number of hours before taking a break to rest. Leaning onto the peach tree, I raised my hand over my eyes as the tree\'s lack of foliage failed to serve as shade."
    hide lixue
    "Somehow in those casual actions, I accidentally cut my hand on my blade."
    "A deep crimson dash of blood fell on the sword and seemed to disappear. The wound, although it stung fiercely, closed up quickly afterward."
    $ muqing = "Spirit"
    show muqing squint subdued with dissolve
    Muqing "...Why did I awaken from my butterfly dream? Fenghuang Sword, you still remember me?"
    hide muqing
    show lixue surprised with dissolve
    Lixue "...!"
    "I jerked around to face the person who had appeared out of thin air, the person whose presence I had not sensed even a little."
    show lixue shout with dissolve
    Lixue "Who are you?"
    "I pointed my sword at her."
    hide lixue
    show muqing open surprised with dissolve
    Muqing "Woah!"
    "She jumped out of the way, landing on the tip of my sword like a feather. As if taunting me, she leaned in to take a closer look at my face before hopping right off."
    show muqing troubled with dissolve
    Muqing "You\'re Fenghuang Sword\'s current wielder?"
    "I felt as if she could have disarmed me easily."
    hide muqing
    show lixue diligent with dissolve
    Lixue "......"
    hide lixue
    show muqing thoughtful with dissolve
    Muqing "To think the person who woke me up was a kid like you. That\'s fine. I\'ll atone; I can do that."
    hide muqing
    show lixue sus with dissolve
    Lixue "What are you talking about?"
    hide lixue
    show muqing neutral with dissolve
    Muqing "What can I say? I was the person who forged your sword."
    "Fenghuang Sword hummed in agreement, pulsing warmly with affection toward this mysterious stranger."
    show muqing ask with dissolve
    Muqing "You woke me up. I should ask you who you are."
    "I slowly lowered my sword."
    hide muqing
    show lixue ask with dissolve
    Lixue "Is that so?"
    hide lixue
    show muqing neutral with dissolve
    Muqing "Mm-hm."
    $ renpy.notify("GLOSSARY: Array")
    hide muqing
    show lixue diligent with dissolve
    Lixue "If you are the person who forged this sword, you must be some sort of lingering spirit? Or are you an array hidden within the sword, imbued with the personality of your maker?"
    show lixue sus with dissolve
    Lixue "Why did you appear here before me?"
    hide lixue
    show muqing squint talk with dissolve
    Muqing "What can I say but that you simply happened to meet the qualifications."
    show muqing closed ask with dissolve
    Muqing "I am... Yes, a lingering spirit is a good way to put it, but be at ease. I have no interest in causing you or yours any harm as long as you don\'t do anything to me or mine."
    show muqing squint grin with dissolve
    Muqing "I can even swear on the Heavenly Way if you want, the whole oath with the lightning strike of retribution and all."
    hide muqing
    show lixue pout with dissolve
    Lixue "I\'m not so pedantic as to make you do that."
    show lixue mild with dissolve
    Lixue "Fenghuang Sword trusts you, so I believe what you say."
    "To be completely honest, I had, a few times, wondered what meeting the maker of my precious partner sword would be like. I admired her to be able to make such a sword."
    "A person long dead, even meeting a remnant of her hidden within her masterpiece of a sword was quite an unexpected miracle."
    "Of course, the person was much different from my imagination."
    hide lixue
    show muqing open neutral with dissolve
    Muqing "You\'re a good kid. A sword cultivator?"
    hide muqing
    show lixue serious with dissolve
    Lixue "Yes."
    hide lixue
    show muqing neutral with dissolve
    Muqing "What a coincidence. I was one as well."
    show muqing grin with dissolve
    Muqing "Since that\'s the case, why don\'t you call me Elder Sister? It\'s impossible for my sword to have fallen into the hands of someone from {i}that{/i} sect."
    show muqing smile with dissolve
    Muqing "So it\'s impossible for you to call me Senior Sister or Martial Aunt."
    hide muqing
    show lixue surprised with dissolve
    Lixue "You must be much older than me. How could I insolently call you Elder Sister?"
    hide lixue
    show muqing pout with dissolve
    Muqing "My hair had yet to turn white when I died."
    show muqing mild with dissolve
    Muqing "The dead are all dead. You and I had no relationship in life, so I don\'t expect any piety between junior and senior. If you\'d rather not call me sister, then just Muqing is fine."
    hide muqing
    show lixue ask with dissolve
    Lixue "Huh?"
    $ muqing = "Muqing"
    hide lixue
    show muqing closed grin with dissolve
    Muqing "I\'m sure you were curious."
    "Spirits did not tell others their names freely as names could be used to bind a spirit\'s origins."
    show muqing squint smile with dissolve
    Muqing "It\'s a piece of insurance I\'m giving you."
    show muqing open smirk with dissolve
    "I did not understand her at all at that time. She was, until the end, the confusing Sister Muqing."
    show muqing squint mild with dissolve
    "She leaned her back onto the peach tree, glancing upward as if saddened that it would not flower. I wondered if she planned to cultivate to maintain a physical body of spiritual energy."
    show muqing open with dissolve
    "Thinking of the time that passed, I decided to return to my sword routine."
    hide muqing
    show lixue serious with dissolve
    Lixue "What will you do now?"
    hide lixue
    show muqing chill with dissolve
    Muqing "I\'ll just be sticking around."
    hide muqing
    show lixue awkward with dissolve
    Lixue "...I see."
    "That would potentially be a bother."
    hide lixue
    show muqing neutral with dissolve
    Muqing "Don\'t let me distract you from your practice, but let this senior of yours give you a few pointers now and then."
    Muqing "And, ah, consider this something like philosophical teachings?"
    show muqing smirk with dissolve
    Muqing "Let\'s have some conversation to fill the time as well."

    ##
    scene bg courtyard with fade
    "The next day and the day after, she was still here."
    show muqing chill with dissolve
    Muqing "You\'re curious about what cultivation practices were popular and what secret manuals were hidden through the realm back in the day?"
    hide muqing
    show lixue mild with dissolve
    Lixue "Yes, I am."
    show lixue smile with dissolve
    Lixue "They say that the predecessors of the current cultivation realm were much closer to ascension than us who cultivate now."
    hide lixue
    show muqing question with dissolve
    Muqing "But you\'ve reached Nascent Soul in just over two hundred years."
    show muqing alas with dissolve
    Muqing "Geniuses are geniuses."
    show muqing neutral with dissolve
    Muqing "I doubt much has changed. Major sects and families will hold onto their secret manuals,  secret lands, and their spiritual veins and resources."
    show muqing ask with dissolve
    Muqing "Maybe some of those secrets have been forever lost, their owners unwilling to share them, preferring to let them perish instead. Is there anything in particular you have in mind?"
    hide muqing
    show lixue talk with dissolve
    Lixue "How to forge a sword like Fenghuang Sword."
    hide lixue
    show muqing chill with dissolve
    Muqing "I can teach you that."
    hide muqing
    show lixue excited with dissolve
    Lixue "Really?"
    hide lixue
    show muqing smirk with dissolve
    Muqing "Of course."
    Muqing "The first step is to manifest Spirit Forging Flames. Call your spiritual energy with the very will of your heart into a fire that can only belong to you."
    show muqing thoughtful with dissolve
    Muqing "Ah, but Fenghuang Sword was a bit of a miracle back then as well. The materials may be a bit hard for you to get your hands on."
    Muqing "To quench the blade, it took the blood of a fenghuang freely given, thousand year spirit water from a volcanic spring, the tears of a nearly enlightened Buddhist cultivator..."
    Muqing "And a scale from a carp that had succeeded in jumping over a waterfall to become a dragon."
    show muqing neutral with dissolve
    Muqing "The spring water and scale, with enough connections, you can get them from the inventory of some major sect."
    Muqing "Those crusty old types hang onto their treasures without ever using them."
    show muqing smirk with dissolve
    Muqing "The tears of a Buddhist cultivator. Well, let\'s just say you’d have to rack your brains to get one of those stoic folks to cry."
    show muqing grin with dissolve
    Muqing "Here\'s a hint: even monks will cry when cutting onions."
    show muqing mild with dissolve
    Muqing "As for the blood of a fenghuang, it came from my friend."
    hide muqing
    show lixue mention with dissolve
    Lixue "Friend?"
    hide lixue
    show muqing soft with dissolve
    Muqing "A dear friend with whom I made a life contract with."
    hide muqing
    show lixue question with dissolve
    Lixue "Are you speaking of the fenghuang?"
    hide lixue
    show muqing troubled with dissolve
    Muqing "Yes. Although I should tell you now that you shouldn\'t make life contracts."
    hide muqing
    show lixue ask with dissolve
    Lixue "Because if the beast dies, you die as well?"
    hide lixue
    show muqing alas with dissolve
    Muqing "No, because if you die, that child will die as well. I wronged him by dying."
    hide muqing
    show lixue sad with dissolve
    Lixue "Oh..."
    Lixue "He must have been a truly precious friend."
    show lixue frown with dissolve
    "Thinking about the mystic beast that contributed to this sword, I gave a quiet word of thanks to him. The fenghuang was gone, but Fenghuang Sword accompanied me well."
    hide lixue
    show muqing pleasant with dissolve
    Muqing "You\'re a good kid."
    hide muqing
    show lixue sad with dissolve
    Lixue "Are your regrets for him the reason your spirit lingers, connected to this sword?"
    hide lixue
    show muqing subdued with dissolve
    Muqing "No. It\'s not. It really isn\'t."
    show muqing squint with dissolve
    "An indescribable emotion flashed in her eyes."
    show muqing open smile with dissolve
    Muqing "I spoke so much about the sword that we veered off topic. Was there something else you were curious about?"
    hide muqing
    show lixue hope with dissolve
    Lixue "Perhaps what the state of affairs with demonic cultivators was like?"
    "Not everyone could receive a history lesson from someone who lived the events themselves."
    hide lixue
    show muqing ask with dissolve
    Muqing "That\'s another thing that likely hasn\'t changed."
    show muqing chill with dissolve
    Muqing "Righteous, no, orthodox cultivators fight with demonic cultivators like snakes and mongooses. Do they still use that analogy?"
    show muqing ask with dissolve
    Muqing "The major difference between now and then is probably just that the world back then was in chaos."
    show muqing sigh with dissolve
    Muqing "Demonic sects sprouting up here and there. Major orthodox sects finding corruption within their midsts. All sorts of messy affairs and all sorts of violence."
    hide muqing
    show lixue ask with dissolve
    Lixue "What about the Ancient Calamity?"
    "The Ancient Calamity was the last grandmaster of the demonic cultivators, the monstrous person who united the demonic sects."
    "She brought the cultivation realm to the brink of collapse before being slain."
    hide lixue
    show muqing question with dissolve
    Muqing "Ancient Calamity? I\'ve never heard that epithet before."
    hide muqing
    show lixue muse with dissolve
    Lixue "Maybe she came after your time, or maybe she went by a different name back then."
    "As I mused, she paused."
    hide lixue
    show muqing subdued with dissolve
    Muqing "Something you should remember is that history is written by the selfish."
    hide muqing
    show lixue question with dissolve
    Lixue "Not by the righteous?"
    hide lixue
    show muqing thoughtful with dissolve
    Muqing "Never by the truly righteous."
    "I wanted to disagree but could not find the words to say."

    ##
    scene bg courtyard with fade
    "While passing time with her, this spirit of yore, I found myself yearning for Master more and more."
    "Although I enjoyed Muqing\'s company, that slight enjoyment only served to emphasize my longing for Master. The greedy part of me did not have these feelings when alone."
    "Only upon finding a companion to spend some idle days with did I realize."
    "Growing up, I no longer clung to Master like a little duckling. Now, I wished I had clung to her a little bit more before she went to cultivate in isolation."
    "Closed door cultivation could extend for years on end."
    show muqing grin with dissolve
    Muqing "Which lover has left you sighing like a young maiden waiting for her husband to return from battle?"
    hide muqing
    show lixue awkward with dissolve
    Lixue "What lover?"
    show lixue retort with dissolve
    Lixue "I was only thinking about my master who is in closed door cultivation right now."
    hide lixue
    show muqing surprised with dissolve
    Muqing "Even though I\'m right here?"
    hide muqing
    show lixue serious with dissolve
    Lixue "Rather than spending time with you, I would prefer to spend it with Master."
    hide lixue
    show muqing sigh with dissolve
    Muqing "So cruel of you to say when you were the one who woke me from my dreams."
    show muqing closed grin with dissolve
    Muqing "Well, I can understand liking some people more than others."
    show muqing open smile with dissolve
    Muqing "To make up for my broken heart, tell me more about your dear master who you prefer over me."
    hide muqing
    show lixue closed sigh with dissolve
    Lixue "Must you phrase it that way?"
    hide lixue
    show muqing smirk with dissolve
    Muqing "Don\'t worry about it."
    hide muqing
    show lixue wry with dissolve
    Lixue "That reassurance makes me even more apprehensive."
    show lixue frown with dissolve
    "Letting out a sigh, I returned to meditation. I searched within me to find my inner flames and draw out Spirit Forging Fire."
    show lixue serious with dissolve
    "The flow of the spiritual energy within me seemed to slow as I waded through it, hoping to direct it into a form it had never held before."
    "The courtyard fell silent."
    "Finally, a flicker of fire appeared in my palm. Just as quickly as it came, it left."
    hide lixue
    show muqing neutral with dissolve
    Muqing "Impressive progress."
    "I closed my palm and opened it again. The flames had no heat. I thought that it would burn me, but instead it felt cold like snow in that singular moment of manifestation."
    hide muqing
    show lixue mild with dissolve
    Lixue "Master is..."
    Lixue "A fairy."
    show lixue bashful with dissolve
    Lixue "At first glance, she seems like an ethereal being far detached from the living, but her heart is so warm and her smile so blindingly beautiful."
    show lixue hope with dissolve
    Lixue "And maybe a little lonely."
    "Even though I had been here with her for the past two hundred years."

    ##
    scene bg courtyard with fade
    "{i}Bonk!{/i}"
    "I let out a gasp of surprise as our spar ended. She was teaching me some sword techniques and pulled me into a spar after a request from me."
    "The end result was a quick loss on my end and a soft bop on the head with her practice sword."
    show muqing chill with dissolve
    Muqing "Whew, as expected, taking on physical form is a bit tedious."
    hide muqing
    show lixue ask with dissolve
    Lixue "A bit tedious? Even so, you\'re skillful. Please give me some pointers so that I might last longer in our next spar."
    hide lixue
    show muqing smile with dissolve
    Muqing "Of course. Of course."
    show muqing neutral with dissolve
    "She began to explain. Showing how she had beaten me with her ghostly body, she re-enacted the spar\'s final moments slowly and then at normal speed."
    "Then she adjusted my stance, saying that my build worked better with a modified form."
    "Her hands on mine, cold like ice, reminded me that she was long dead."
    "Once she finished instructing, she let out a light yawn as if bored. She leaned back against the bare peach tree like a smug feline stretching her limbs."
    show muqing pleasant with dissolve
    Muqing "Talking with you reminds me of someone."
    show muqing squint_blush with dissolve
    Muqing "My butterfly dream, my Xuan Mengdie. No, forget what I said. You two really aren\'t particularly similar."
    show muqing open_blush sigh with dissolve
    Muqing "Mengmeng isn\'t like you at all."
    hide muqing
    show lixue muse with dissolve
    Lixue "Who was she?"
    hide lixue
    show muqing closed_blush mention with dissolve
    Muqing "She was my most precious person."
    show muqing open_blush pleasant with dissolve
    Muqing "How romantic it would be to say that we were fated to be together from the moment we met, but it really wasn\'t like that."
    show muqing soft with dissolve
    Muqing "The first time we met, I brushed her off without even thinking. The young miss of a big clan and a beggar on the street."
    Muqing "The second time we met, we fought without even seeing each other\'s faces."
    show muqing alas with dissolve
    Muqing "In hindsight, before we even exchanged names, before we finally talked with each other for the first time, we met so many times."
    show muqing sad with dissolve
    Muqing "Not a single one of those meetings was a romantic fated meeting."
    Muqing "Rather... wasn\'t one of the first things I said to her \'Not even my father has slapped me before!?\' Incorrigible."
    hide muqing
    show lixue surprised with dissolve
    Lixue "She slapped you?"
    hide lixue
    show muqing open_blush mild with dissolve
    Muqing "Mm-hm."
    hide muqing
    show lixue awkward with dissolve
    Lixue "I... see."
    "I could not imagine a good relationship starting from conflict and violence, but she spoke very fondly of this Xuan Mengdie."
    hide lixue
    show muqing open_blush pleasant with dissolve
    Muqing "Both of us were the hard headed type."
    show muqing smile with dissolve
    Muqing "Heh. Not that this is something to be proud of, but my head was objectively harder. For example, when she tried to headbutt me, her head hurt more than mine in the end."
    "My forehead throbbed with phantom pain."
    hide muqing
    show lixue wry with dissolve
    Lixue "That sort of hard headedness?"
    hide lixue
    show muqing closed_blush smile with dissolve
    Muqing "What can I say?"
    show muqing squint_blush smile with dissolve
    Muqing "She was a really earnest woman. Underneath a cold, hard, cracked exterior, she was more honest than anyone else. To the point that it should have burned me."
    show muqing grin with dissolve
    Muqing "If you let me continue, I\'ll talk about Mengmeng forever."
    hide muqing
    show lixue talk with dissolve
    Lixue "I don\'t mind."
    "Muqing seemed happy to talk. I had no reason to stop her."
    hide lixue
    show muqing open pleasant with dissolve
    Muqing "You\'re a good kid."
    "She pet my head before intentionally ruffling my hair, causing me to sputter as I swatted her hand away to fix the mess she made."
    show muqing squint troubled with dissolve
    Muqing "...She was also my greatest regret."
    "I nearly did not hear her whisper."
    hide muqing
    show lixue question with dissolve
    Lixue "...?"
    "Fenghuang Sword let out a sad cry in my hand."
    hide lixue
    show muqing open neutral with dissolve
    Muqing "Nevermind that. Shouldn\'t you get back to practicing, diligent little student Ming?"
    "Who was \'diligent little student Ming\'?"
    "Feeling an exasperated sigh bubble up in my throat, I wondered if she would give me some sort of demented nickname from a joke I did not understand."
    hide muqing
    show lixue speak with dissolve
    Lixue "You can call me Lixue."
    hide lixue
    show muqing grin with dissolve
    Muqing "Lixue? That\'s a pretty good name."
    hide muqing
    show lixue open_blush smile with dissolve
    Lixue "Yes. After all, Master gave it to me."

    ##
    scene bg courtyard with fade
    "The days continued to pass after I told her my name."
    "With Master still in closed door cultivation, I had little else to do but spend my time with Sister Muqing."
    "A ball of cold fire appeared in my palm, this time not dispersing at the slightest breeze. Only when I closed my hand did it disappear."
    show muqing neutral with dissolve
    Muqing "With the rate of your progress, I\'ll teach you a secret technique."
    Muqing "The forge flames can be used to forge your very essence into a blade. If they can make swords out of ingots, then naturally they can sharpen your soul."
    show muqing mention with dissolve
    Muqing "In cases where you do not want to cut the physical body but rather need to cut the spiritual, would a blade made out of your soul not be better?"
    show muqing talk with dissolve
    Muqing "That was a question posed by a venerated elder of my former... sect."
    Muqing "They wanted so badly to perfect a spirit blade made of one\'s soul itself that they made the idea the secret technique of the sect."
    show muqing thoughtful with dissolve
    Muqing "Not that they succeeded themselves."
    Muqing "I suppose I can thank them for setting the foundations and nothing else."
    hide muqing
    show lixue ask with dissolve
    Lixue "Is it alright for you to share the technique with me?"
    hide lixue
    show muqing confident with dissolve
    Muqing "Of course. After all, I was the one who completed the technique."
    show muqing frown with dissolve
    Muqing "Which sect did you belong to again?"
    hide muqing
    show lixue muse with dissolve
    Lixue "As of now, I belong to none, although Master was part of the Dalin Sect."
    hide lixue
    show muqing ask with dissolve
    Muqing "That\'s fine."
    hide muqing
    show lixue speak with dissolve
    Lixue "Is there a sect that you have a grudge with?"
    hide lixue
    show muqing thoughtful with dissolve
    Muqing "Let\'s just say that I dislike some."
    stop music fadeout 3.0
    "Her feelings could not have been only at the level of dislike, but seeing her expression, I did not bother to pry."

    ##
    scene bg courtyard with fade
    play music "<loop 25.600>/audio/music/Suspenseful (Full).ogg"
    #play music Suspenseful_Intro
    #queue music Suspenseful_Loop
    "I noticed that she was happier than any other time when talking about the mysterious Xuan Mengdie. That person who I had never met was painted in my mind by her descriptions."
    show muqing troubled with dissolve
    Muqing "Mengmeng was a calamitous beauty."
    show muqing frown with dissolve
    Muqing "She was born in the mortal realm below the cultivation realm,{w}"
    show muqing scowl with dissolve
    extend " and she was picked up by some cultivator from a major sect to \'aid\' him in his cultivation."
    hide muqing
    show lixue sad with dissolve
    Lixue "Aid?"
    hide lixue
    show muqing frown with dissolve
    Muqing "It\'s better that you don\'t understand what I mean."
    show muqing irritated with dissolve
    Muqing "Luckily, she rid herself of him and was able to cultivate herself."
    show muqing subdued with dissolve
    Muqing "It\'s only that... Yes, at first, we were really at odds with each other. The entire world was at odds with her. For the longest time, she had lived a misfortunate life."
    show muqing troubled with dissolve
    Muqing "You know how I mentioned that the world was filled with violence? She was embroiled in it, stuck in the eye of the storm with no way out."
    show muqing squint with dissolve
    Muqing "I guess she was tired."
    Muqing "I was also tired of fighting and killing demonic cultivators all the time."
    show muqing open frown with dissolve
    Muqing "What ‘ascension’ and ‘enlightenment’? What ‘balance of the Heavenly Way’? Wasn\'t it all just blood, blood, and blood?"
    Muqing "It wasn\'t uncommon for cultivators to go into qi deviation, filled up to their eyes with bloodlust."
    show muqing talk with dissolve
    Muqing "But somehow, because we were together, we were able to escape from that violence for a while, a little bit at least."
    hide muqing
    show lixue hope with dissolve
    Lixue "How did you do that?"
    hide lixue
    show muqing sad with dissolve
    Muqing "We ran away."
    Muqing "We found a place just for the two of us, far, far away from everything going on in the cultivation realm, and promised each other the future."
    show muqing mention with dissolve
    Muqing "Do you think that\'s cowardly?"
    hide muqing
    show lixue sus with dissolve
    Lixue "Cowardly? Why should that be cowardly?"
    "The world could take and take and take, but a person could only give so much. Rather than to give to a world that hurt her, finding her own happiness seemed like a better choice."
    hide lixue
    show muqing alas with dissolve
    Muqing "Yes. You\'re right."
    show muqing soft with dissolve
    Muqing "Some people just fill the world with light. When you think about them, your heart is warm. Strife is washed away, and hope penetrates the darkness."
    show muqing open_blush pleasant with dissolve
    Muqing "That was the person she became to me."
    show muqing open ask with dissolve
    Muqing "Do you have someone like that?"
    hide muqing
    show lixue thinking with dissolve
    Lixue "I don\'t know."
    show lixue mild with dissolve
    Lixue "What was she to you?"
    hide lixue
    show muqing squint pleasant with dissolve
    Muqing "The person I loved the most in this world."
    "Platonic love or romantic love, I could not identify what sort of love she was talking about. After all, she and that Xuan Mengdie were both women."
    "In the cultivation realm, such a coupling had never been accepted."
    "Even so, I could not reject them. I could not deny them."
    "The intensity of her feelings gripped my heart. As expected, this was the strong flame that forged my sword. As such, I put all of my sincerity into finding an answer to her question."
    "The person I loved the most in this world?"
    "Maybe mine was Master."
    hide muqing
    show lixue hesitant with dissolve
    Lixue "......"
    hide lixue
    show muqing squint smile with dissolve
    Muqing "Make sure you take care of her well."
    show muqing open sad with dissolve
    Muqing "What did Mengmeng do wrong but exist?"
    Muqing "At the very least, I\'m glad for the time we were able to spend together. Since, as you might have guessed, both she and I have died already."
    hide muqing
    show lixue sad with dissolve
    Lixue "...Oh."
    "That was right. That made sense. I simply had not thought of it before. Most likely, the Xuan Mengdie whom she loved, I would never meet her."
    hide lixue
    show muqing pleasant with dissolve
    Muqing "She liked eating peaches, so I would peel and cut them for her."
    Muqing "Before she died, before I died, we had prepared a jar of fruit wine and buried it under the tree we planted together."
    show muqing soft with dissolve
    Muqing "It was meant to be something we would do year and year again. The next year we would dig it up and bury another one. The year after that, we would do the same."
    Muqing "Until our hair turned white and we left the living world, that was what we promised we would do."
    show muqing troubled with dissolve
    Muqing "She gave up ascension for me. She was at the last stage, the Ascendant stage. I was too, but... rather than that, we just wanted to stay together."
    "The goal of cultivators was to ascend or reach enlightenment. That didn\'t mean romance between cultivators did not exist, but rather that cultivators never chose love over cultivation."
    hide muqing
    show lixue ask with dissolve
    Lixue "Why could you not have cultivated together?"
    hide lixue
    show muqing alas with dissolve
    Muqing "That was just how things were."
    Muqing "So she gave it up for me."
    hide muqing
    show lixue speak with dissolve
    Lixue "Did you ever make it up to her?"
    hide lixue
    show muqing squint troubled with dissolve
    Muqing "...No."
    Muqing "I wish I did."
    "She turned her face away from me."
    show muqing subdued with dissolve
    Muqing "Ah, how I wish I could have a cup of fruit wine right now."
    stop music fadeout 3.0
    "Unfortunately, there was no fruit wine I knew of on Juyi Peak."

    ##
    scene bg courtyard with fade
    play music "<loop 18.701 >/audio/music/Peaceful (Full).ogg"
    #play music Peaceful_Intro
    #queue music Peaceful_Loop
    "The more time I spent with Sister Muqing, the more I realized how little I knew about the world. What I had experienced was but a drop in a vast sea."
    "Talking about my breakthrough to Nascent Soul, I happened to mention how Master had blocked one of the lightning strikes that descended."
    show muqing ask with dissolve
    Muqing "Blocking the tribulation lightning of someone else is much more dangerous than taking on your own."
    hide muqing
    show lixue surprised with dissolve
    Lixue "Huh?"
    hide lixue
    show muqing pleasant with dissolve
    Muqing "You have a good master."
    hide muqing
    show lixue closed_blush bashful with dissolve
    Lixue "Yes. She is a truly wonderful master."
    show lixue open_blush with dissolve
    "I realized how much about Master that I had yet to understand."
    "We had so much time, so one day, surely I would learn more and more about her. With that thought in mind, I dreamt about the future without knowing anything."

    ##
    scene bg courtyard with fade
    "One day when I was meditating, a little bird landed on my shoulder."
    show lixue mild bird with dissolve
    Bird "Chirp!"
    show lixue talk with dissolve
    Lixue "I might recognize the pattern on this bird\'s head."
    "I looked at the little bird who stared back at me with big round eyes."
    show lixue smile with dissolve
    Lixue "It looks exactly the same as a pattern I saw a number of decades ago. Perhaps he remembers his ancestor\'s debts to my Master."
    hide lixue
    show muqing chill with dissolve
    Muqing "Even birds have debts in the cultivation realm now?"
    hide muqing
    show lixue open_blush mention bird with dissolve
    Lixue "Perhaps they do. Although to this little bird, I was just joking. Master does not help others with the expectation of repayment."
    Bird "Chirp!"
    hide lixue
    show muqing smirk with dissolve
    Muqing "The bird seems to agree with you. Heh, that\'s pretty cute."
    show muqing neutral with dissolve
    Muqing "What\'s the story, Lixue?"
    "I paused to think, reminiscing."
    hide muqing
    show lixue talk bird with dissolve
    Lixue "It was a number of decades ago. I had yet to break through to Nascent Soul. After a heavy storm near the start of summer, Master and I came out to this courtyard."
    Lixue "There we found this injured little bird."
    show lixue speak with dissolve
    Lixue "Its left wing had broken, nearly torn off its body. Perhaps the wind had blown him here. Wherever his family should have been, he was not with them."
    "I remembered the night I met Master."
    show lixue hope with dissolve
    Lixue "I thought that the bird would die."
    show lixue relief with dissolve
    Lixue "Only to be proven wrong when Master gingerly picked him up, cupping his small, broken body in her palms, and brought him inside."
    Lixue "After that, we nursed him back to health together."
    show lixue talk with dissolve
    Lixue "With steady hands, she sewed his wing back onto his body and fed him so many elixirs."
    hide lixue
    show muqing ask with dissolve
    Muqing "Feeding a bird elixirs... Was she trying to make him into some novel spiritual bird dish?"
    hide muqing
    show lixue thinking bird with dissolve
    Lixue "If that were the case, would not buying a chicken from the town at the base of this mountain be a better choice of meat?"
    show lixue bird_shock
    Bird "Chirp!?"
    hide lixue
    show muqing grin with dissolve
    Muqing "Of course, the little bit of meat on these little bones isn\'t worth eating."
    hide muqing
    show lixue muse bird_angry with dissolve
    Bird "Chirp!!"
    "The bird on my shoulder angrily pecked at Sister Muqing who just laughed and avoided the small creature\'s attacks."
    show lixue smile bird with dissolve
    Lixue "Once the little bird awoke, Master... let me play with him."
    "Clearly she liked the little bird, yet she did not know what to do with him. Thus I found out that Master was a little awkward with small animals."
    "I was happy. Whereas her attention had been focused on the bird while nursing it, leaving me feeling neglected, once the bird awoke, we played with him together."
    show lixue talk with dissolve
    Lixue "Eventually the little bird recovered."
    show lixue speak with dissolve
    Lixue "We spent a few seasons with him, but as animals are wont to do, he could not bear to stay cooped up on this small Juyi Peak forever."
    show lixue smile with dissolve
    Lixue "So on a warm, sunny day, we said goodbye and the little bird flew away."
    Bird "Chirp!"
    hide lixue
    show muqing closed smirk with dissolve
    Muqing "Hm, what a heartwarming story."
    Bird "Chirp!"
    "Satisfied, the bird on my shoulder nodded and flew away. As it flew, the slightest scar on its left wing caught my eye."
    show muqing open smile with dissolve
    Muqing "A funny thought. Maybe that little bird was the same little bird as the one you and your master saved."
    hide muqing
    show lixue question with dissolve
    Lixue "So many years have passed."
    hide lixue
    show muqing ask with dissolve
    Muqing "If it became a yao, it could have cultivated to extend its lifespan and could still be alive. It might really return to repay its debts one day."
    "Animals, plants, even inanimate objects, could gain spiritual awareness after absorbing adequate spiritual energy, becoming a yao."
    "They could eventually even take human form."
    hide muqing
    show lixue wry with dissolve
    Lixue "I would be alright if it doesn\'t."
    hide lixue
    show muqing squint grin with dissolve
    Muqing "Why? Afraid that it would take your dear master\'s attention away again?"
    hide muqing
    show lixue open_blush sus with dissolve
    Lixue "......"
    hide lixue
    show muqing open surprised with dissolve
    Muqing "Did I happen to hit the bullseye?"
    "Whether or not she was correct, I decided to ignore her for a while."

    ##
    scene bg courtyard with fade
    "Then Master came out of closed door cultivation."
    "Upon receiving the message, I immediately set out to find her. For some reason, Sister Muqing was nowhere to be seen."
    "I spotted Master by the barren tree and bounded toward her excitedly."
    show lixue open_blush excited with dissolve
    Lixue "Master!"
    hide lixue
    show fangfei squint resigned with dissolve
    stop music fadeout 3.0
    Fangfei "...Lixue."
    play music "<loop 25.600>/audio/music/Suspenseful (Full).ogg"
    #play music Suspenseful_Intro
    #queue music Suspenseful_Loop
    show fangfei sad with dissolve
    "Her voice sounded distant, subdued. Her gaze seemed to inadvertently avoid my face."
    "Why?"
    "She pulled me into an embrace, burying her face into my shoulder. She was... shorter than me; I hadn\'t realized until now."
    "Fragile, she seemed fragile."
    show fangfei open concerned with dissolve
    "A few moments passed, and she separated herself from me as if nothing had happened."
    hide fangfei
    show lixue sad with dissolve
    Lixue "Master, did something bad happen?"
    hide lixue
    show fangfei hesitant with dissolve
    Fangfei "No, nothing at all."
    show fangfei sad with dissolve
    Fangfei "I must have been tired, coming out of closed door cultivation."
    hide fangfei
    show lixue ask with dissolve
    Lixue "Would you like to go back inside?"
    hide lixue
    show fangfei hesitant with dissolve
    Fangfei "No. I\'ll stay here for a little longer."
    hide fangfei
    show lixue hope with dissolve
    Lixue "Then I\'ll stay with you, Master."
    hide lixue
    show fangfei sad with dissolve
    Fangfei "Alright."
    show fangfei resigned with dissolve
    Fangfei "Have you been diligent in your cultivation?"
    hide fangfei
    show lixue relief with dissolve
    Lixue "Yes."
    "She gestured for me to tell her how my days had been without her, so I began to talk. As if telling her a story, I wanted to put her at ease."
    "For the oddest reason, I didn\'t mention Sister Muqing."
    "Instead, the thought of the lingering spirit who forged my precious sword caused a doubt to come into my mind. I thought surely Master could answer the question."
    show lixue muse with dissolve
    Lixue "I have a question about the cultivation realm, Master."
    "Perhaps I was simply overthinking it, but Sister Muqing hated the major sects."
    hide lixue
    show fangfei surprised with dissolve
    Fangfei "Yes, what is it?"
    hide fangfei
    show lixue frown with dissolve
    Lixue "Have the major sects done bad things before?"
    "She extended her hand and gently pet my head."
    hide lixue
    show fangfei squint speak with dissolve
    Fangfei "Everyone has done bad things before. You and I and even the disciples of major sects all have done bad things before."
    show fangfei mild with dissolve
    Fangfei "That is why sects have rules and punishments."
    show fangfei open serious with dissolve
    Fangfei "Some are stricter than others, but the major sects are looked up to as the moral backbone of the cultivation realm. Evil has harsh consequences."
    show fangfei stern with dissolve
    Fangfei "Coercing others to be human furnaces means to be castrated and subject to death by a thousand cuts. Cultivating the demonic way means to destroy your cultivation or die."
    show fangfei convicted with dissolve
    Fangfei "At the end of the previous age, there was a major sect destroyed as their head disciple had colluded with the Ancient Calamity to harm the common people."
    hide fangfei
    show lixue ask with dissolve
    Lixue "What was the name of that sect?"
    hide lixue
    show fangfei serious with dissolve
    Fangfei "I\'m afraid the name has long been lost to history."
    show fangfei surprised with dissolve
    Fangfei "What brought up the interest?"
    hide fangfei
    show lixue talk with dissolve
    Lixue "I was just curious."
    stop music fadeout 3.0
    play music "<loop 18.701 >/audio/music/Peaceful (Full).ogg"
    #play music Peaceful_Intro
    #queue music Peaceful_Loop
    "Perhaps she thought that I was sick of our halcyon days together in a small world away from the hustle and bustle of the cultivation realm and that I wanted to go and join the revel."
    show lixue closed relief with dissolve
    Lixue "But I\'m happiest being with Master here on Juyi Peak."

    ##
    scene bg night_room
    "When evening fell, we returned indoors."
    "Even now, I loved the feeling of her hands through my hair. After a long hot soak in the bath, more for indulgence\'s sake than anything else, we were chatting as she combed my hair."
    hide fangfei
    show lixue mild with dissolve
    Lixue "Master, will you comb my hair even when our heads have gone white?"
    hide lixue
    show fangfei closed mild with dissolve
    Fangfei "Mm."
    show fangfei squint with dissolve
    Fangfei "If the world was willing."
    show fangfei open with dissolve
    Fangfei "Although you may have ascended before your hair begins to grey."
    hide fangfei
    show lixue pout with dissolve
    Lixue "Master puts too high of an expectation on me."
    hide lixue
    show fangfei resigned with dissolve
    Fangfei "Yes, yes. That is because I love you dearly, Lixue. Don\'t let Master become a heart demon for you."
    hide fangfei
    show lixue thinking with dissolve
    Lixue "...?"
    "She did not elaborate, allowing silence to fill the room. Without any words, she combed my hair."
    show lixue relaxed mild with dissolve
    "In the warmth, my eyelids fluttered shut as I focused on the sound of her breathing. How she smelled like peaches."
    "So comfortable, I must have dozed off for a moment."
    hide lixue
    show fangfei talk with dissolve
    Fangfei "Lixue, you mustn\'t fall asleep here."
    show fangfei surprised with dissolve
    Fangfei "What were you dreaming about? Perhaps exploring the vast cultivation realm on a sabbatical and taking in all of the sights?"
    hide fangfei
    show lixue speak with dissolve
    Lixue "No."
    "I probably did not dream."
    Lixue "I also wonder what I dreamed about."
    hide lixue
    show fangfei mild with dissolve
    Fangfei "Perhaps the dream was simply not fated for you."
    hide fangfei
    show lixue bashful with dissolve
    Lixue "The Heavenly Way dealt me many good hands, so I suppose one dream is but a trifle."
    hide lixue
    show fangfei thoughtful with dissolve
    Fangfei "The Heavenly Way is mysterious but just."
    hide fangfei
    show lixue hesitant with dissolve
    Lixue "Master is skilled at divination, but to me, the Heavenly Way is just mysterious."
    hide lixue
    show fangfei mild with dissolve
    Fangfei "Whether a pleasant dream or not, sometimes living without seeing is kinder. Mysterious is fine, is it not?"
    hide fangfei
    show lixue mild with dissolve
    Lixue "Yes, it is."
    show lixue happy with dissolve
    "Since the Heavenly Way led me to her and her to me, mysterious or not, I was alright with the path it directed us down. At that moment I was."
    "I thought about Sister Muqing since her path seemed very different."
    show lixue talk with dissolve
    Lixue "Master, would you give up cultivation for the sake of love?"
    hide lixue
    show fangfei squint mild with dissolve
    Fangfei "Love and cultivation are not mutually exclusive."
    "I nearly nodded had she not been combing my hair."
    hide fangfei
    show lixue speak with dissolve
    Lixue "But what if they were?"
    "Many cultivators chose cultivation over love. Faced with a partner\'s mortality, a cultivator might steel their heart and decide to never pursue romance."
    hide lixue
    show fangfei squint thoughtful with dissolve
    Fangfei "If they were..."
    show fangfei closed speak with dissolve
    Fangfei "Then I would not be able to answer for I have never fallen in love before."
    hide fangfei
    show lixue open_blush ask with dissolve
    Lixue "Does Master ever dream of falling in love or of dual cultivating with another? N-not in the bed, of course."
    hide lixue
    show fangfei squint laugh with dissolve
    Fangfei "Pfft."
    show fangfei open resigned with dissolve
    Fangfei "No, surely love was not fated for me."
    hide fangfei
    show lixue sigh with dissolve
    Lixue "Why not?"
    hide lixue
    show fangfei hesitant with dissolve
    Fangfei "One day, you will come to understand, Lixue, but I hope you won\'t blame me for not telling you now."
    hide fangfei
    show lixue speak with dissolve
    Lixue "Then if the Heavenly Way allowed?"
    hide lixue
    show fangfei mild with dissolve
    Fangfei "Certainly I might be interested."
    Fangfei "A junior once told me that first kisses tasted sweet like malt candy. Surely it was just that her lover had eaten some candy before the kiss."
    Fangfei "She invited me to their wedding. What a red wedding it was. By now... their child should have already had children."
    show fangfei sure with dissolve
    Fangfei "She seemed happy, very happy."
    show fangfei confident with dissolve
    Fangfei "And I thought: how nice it must be to share a vow for the future."
    show fangfei sure with dissolve
    "I thought about her in a red wedding dress. She would look stunning, like a goddess descended from the heavens."
    "But who would kick down the door of her sedan chair and carry her away?"
    "The idea of blocking the groom yet ultimately giving her away for her to drink wedding wine and share the first night with another seemed wrong."
    "I didn\'t want her to hate her clingy disciple, her clingy Lixue, for these thoughts."
    hide fangfei
    show lixue pout with dissolve
    Lixue "Master is so beautiful that there should be suitors coming to beat down our door even out here on Juyi Peak."
    show lixue relaxed speak with dissolve
    Lixue "I would have to fight them off. What qualifications do they have to see Master if they cannot even beat me?"
    hide lixue
    show fangfei closed confident with dissolve
    Fangfei "Alright, alright. Spare those poor imaginary suitors, Lixue."
    show fangfei open mild with dissolve
    Fangfei "You still have such a sweet mouth."
    hide fangfei
    show lixue relaxed relief with dissolve
    Lixue "That is because Lixue likes Master best."
    hide lixue
    show fangfei closed mild with dissolve
    Fangfei "Mm."
    show fangfei open with dissolve
    Fangfei "Since you are speaking about romance, did someone steal your heart while I was away?"
    hide fangfei
    show lixue open hope with dissolve
    Lixue "No, no such person exists."
    "My heart skipped a beat. If that person existed, would it not be..."
    show lixue open_blush with dissolve
    "She must have interpreted my flustering as a lie and set the comb down, making a noise to say that she had finished combing my hair."
    hide lixue
    show fangfei open mild with dissolve
    Fangfei "Lixue, if you fall in love, I have no objections. Just don\'t let your affections lead you astray."
    "I turned around to face her."
    show fangfei resigned with dissolve
    Fangfei "For now, let Master cling onto you for a little longer, alright?"

    ##
    scene bg courtyard with fade
    show muqing pout with dissolve
    Muqing "Smiling cheek to cheek, did you need to make your master\'s return so obvious?"
    "I put my hands to my cheeks as if checking the veracity of her words. Although my heart rejoiced, my face did not seem to particularly change."
    show muqing neutral with dissolve
    Muqing "Seeing as she isn\'t here, I can assume you didn\'t mention me to her. That\'s good."
    show muqing smirk with dissolve
    Muqing "Or you were monopolizing your dear master from me?"
    hide muqing
    show lixue open_blush retort with dissolve
    Lixue "...No."
    hide lixue
    show muqing neutral with dissolve
    Muqing "Nonetheless, I\'d rather not have to deal with another variable. I\'m satisfied with you talking my ear off about her as if she were your little wife back home."
    hide muqing
    show lixue question with dissolve
    Lixue "Do you not do the same with Miss Xuan?"
    hide lixue
    show muqing chill with dissolve
    Muqing "Who says she wasn\'t my little wife back home? Although... I think she may have divorced me."
    hide muqing
    show lixue soft with dissolve
    Lixue "My condolences."
    Lixue "Was the reason you didn\'t move on because you were afraid that the King of Hell would hand you her divorce papers at the gate?"
    hide lixue
    show muqing awkward with dissolve
    Muqing "When I told you to use Spirit Forging Flames to sharpen something I didn\'t mean for you to sharpen your poisonous tongue."
    hide muqing
    show lixue mention with dissolve
    Lixue "My apologies."
    show lixue ask with dissolve
    Lixue "However, you didn\'t want to meet Master at all?"
    hide lixue
    show muqing mild with dissolve
    Muqing "You never know what can go wrong. If we hit it off, then wouldn\'t that be jolly?"
    show muqing sigh with dissolve
    Muqing " Still, I am a dead person and she is a living one. We don\'t need to meet."
    stop music fadeout 3.0

    ##
    scene bg courtyard with fade
    #play music Sad_Intro
    #queue music Sad_Loop
    play music "<loop 21.745>/audio/music/Sad (Full).ogg"
    show muqing troubled with dissolve
    Muqing "Let me tell you a hypothetical."
    show muqing squint mention with dissolve
    Muqing "Say that there lived a cultivator whose father was the head of a major sect, but she fell in love with someone she shouldn\'t have fallen in love with."
    show muqing closed with dissolve
    Muqing "Disowned from her family, she eloped with her lover to a place far, far away."
    show muqing squint talk with dissolve
    Muqing "After a long time, she thought to herself: perhaps my father did care for me in a strict way for he has not chased after us to punish us."
    show muqing open sad with dissolve
    Muqing "She was at peace with the thought and lived out her days happily."
    show muqing frown with dissolve
    Muqing "Until one day, her father appeared before her again."
    show muqing squint with dissolve
    Muqing "What did that man do? Did he come bearing late wedding gifts? The dowry that he would have promised a youth from another clan had his daughter wed as he wished?"
    show muqing irritated with dissolve
    Muqing "Ha."
    "Ah, my father was also a piece of shit. I didn\'t voice that aloud."
    show muqing open talk with dissolve
    Muqing "He thanked the cultivator for leading the way, to which the cultivator asked what he meant."
    Muqing "Without answering, he beat the cultivator down to the ground, a foot on her head, and told her to stay put. He would give her lover her final goodbyes."
    show muqing hurt with dissolve
    Muqing "Thus the cultivator could no longer meet her lover in the living realm."
    show muqing scowl with dissolve
    Muqing "What she should have done was to never have been born to such a dog of a father."
    show muqing declare with dissolve
    Muqing "If she could not change her blood, she should have never told that man anything about her love."
    Muqing "Maybe she should have faked her death so that their paths would truly never cross again, or better yet, if she had the ability, she should have killed him."
    show muqing frown with dissolve
    Muqing "What did the cultivator do?"
    show muqing troubled with dissolve
    Muqing "In the end, before her death, she simply cried."
    show muqing squint with dissolve
    Muqing "You see... it\'s easy to trust and so hard to pick up the pieces."
    hide muqing
    show lixue frown with dissolve
    Lixue "......"
    show lixue sad with dissolve
    Lixue "What sort of tragedy was that that the Heavenly Way allowed it?"
    hide lixue
    show muqing hurt with dissolve
    Muqing "It was just... a hypothetical."
    show muqing sad with dissolve
    Muqing "Let\'s just say that the story has a happy ending after all. And that the cultivator meets again with her lover, and they reincarnate together."
    Muqing "And that the heavens punish the father and his sect for their cruel deeds."
    "I knew that they did not have a happy ending."
    "The hypothetical story was about her and Xuan Mengdie, who I had yet to meet but had already grown to know from her stories."
    show muqing mention with dissolve
    Muqing "If you cry, how will I explain it to your master?"
    hide muqing
    show lixue cry with dissolve
    Lixue "You don\'t even want to meet her."
    hide lixue
    show muqing surprised with dissolve
    Muqing "What makes people happy...? Money? Candy? Mengmeng liked candied fruits- Ah, I don\'t have any."
    show muqing mild with dissolve
    Muqing "Do you want to switch over to learning more about that secret technique I mentioned?"
    "Unwittingly, I grasped at her shirt, which slipped through my hands like cold dew. That was right; she was dead, long dead."
    hide muqing
    show lixue cry with dissolve
    Lixue "Can I help the cultivator and her lover become happy?"
    hide lixue
    show muqing alas with dissolve
    Muqing "You\'re a good kid, Lixue. No wonder Fenghuang Sword likes you. But it\'s alright. The cultivator and her lover, they were just two characters in a story forgotten by time."
    "I wanted to know how to achieve my own happy ending as well."
    stop music fadeout 3.0

    ##
    scene bg courtyard with fade
    play music "<loop 25.600>/audio/music/Suspenseful (Full).ogg"
    #play music Suspenseful_Intro
    #queue music Suspenseful_Loop
    "On a normal day, like any other day, Master and I were talking about normal topics like anything else."
    "The tree that never bloomed still showed no signs that it would ever bloom."
    "Yes, it was a normal day."
    "As would be normal, the conversation turned to her cultivation."
    show fangfei squint sad with dissolve
    Fangfei "In my closed door cultivation, I was divining the future, and I saw terrible things."
    show fangfei frown with dissolve
    Fangfei "My hands will be stained with blood. I will destroy the cultivation realm, tearing it apart at the seams, razing it to the ground."
    show fangfei mention with dissolve
    Fangfei "That was the future I saw."
    show fangfei closed with dissolve
    Fangfei "The demons will rise. The heavens will fall. My path will be filled with nothing but blood, and I will laugh, alone at the summit, surrounded by corpses."
    "My breath hitched in my throat."
    show fangfei open convicted with dissolve
    Fangfei "Unless you kill me."
    "As if overcome with vertigo, an undulating nausea ran through my entire body. I gripped my shaking palms hoping that I was dreaming, digging my fingers into my flesh till it hurt."
    show fangfei stern with dissolve
    Fangfei "Not too long from now, you must kill me."
    show fangfei mention with dissolve
    Fangfei "Your heart might not be prepared, but... sooner rather than later, you must kill me."
    show fangfei convicted with dissolve
    Fangfei "Lixue, when the time comes, you must cut me down."
    hide fangfei
    show lixue squint shocked with dissolve
    Lixue "What...?"
    "What was she talking about? Master would never do such a thing."
    "She would never kill for the sake of killing, perpetuating a downward spiral of violence. She would never ask of me to kill her, breaking my very heart."
    hide lixue
    show fangfei hesitant with dissolve
    Fangfei "That was the fate that I saw we shared together."
    "I bit my tongue as if to try to awaken from a nightmare. The blood tasted bitter."
    hide fangfei
    show lixue squint sus with dissolve
    Lixue "...Did you raise me to kill you?"
    "A hysterical wheeze came out of my throat that was neither a laughter nor a cry."
    hide lixue
    show fangfei concerned with dissolve
    Fangfei "I raised you to live an upright life."
    show fangfei hesitant with dissolve
    Fangfei "This is for the sake of the entire cultivation world. We cannot allow for the demonic forces to rise again and for the righteous forces to fall."
    show fangfei serious with dissolve
    Fangfei "That will send everything spiraling into darkness and violence once more."
    show fangfei frown with dissolve
    Fangfei "If I could, I would spare you this, but... I am unable to do the deed myself."
    hide fangfei
    show lixue closed shout with dissolve
    Lixue "Master, you are... the most virtuous person I know. That future could never come! Unless you became an entirely different person."
    hide lixue
    show fangfei mild with dissolve
    Fangfei "You speak too highly of me, Lixue."
    show fangfei squint with dissolve
    Fangfei "However, the Heavenly Way does not lie. There are two possible paths: my death at your hands or the world\'s death."
    show fangfei closed calm with dissolve
    Fangfei "If you do not cut me down, then there will be no one else in this world capable of doing so, which is why you must kill me."
    show fangfei open convicted with dissolve
    Fangfei "Kill me sooner rather than later."
    hide fangfei
    show lixue reject with dissolve
    Lixue "Is this the Heavenly Way? The path of righteousness!?"
    "I wanted to puke. I wanted to grab her sleeve only to awaken from a terrible nightmare."
    hide lixue
    show fangfei mention with dissolve
    Fangfei "Lixue, this is your duty as my disciple. Will you not listen to your master\'s orders?"
    hide fangfei
    show lixue squint sob with dissolve
    Lixue "...Master?"
    "How long had it been since I last cried?"
    Lixue "Did you not teach me to not blindly follow?"
    hide lixue
    show fangfei squint mention with dissolve
    Fangfei "This is for everyone\'s good."
    hide fangfei
    show lixue reject with dissolve
    Lixue "For whose good!?"
    hide lixue
    show fangfei squint confident with dissolve
    Fangfei "That of the entire cultivation realm."
    hide fangfei
    show lixue reject
    Lixue "...The entire cultivation realm."
    show lixue closed holding with dissolve
    "The entire cultivation realm? I wanted to yell that I did not need the cultivation realm if it meant that I had to cut her down."
    show lixue squint sob with dissolve
    "Fairy, why did you raise me so tenderly if this was the reason you picked me up from the snow?"
    "Why did you allow me to come to love you!?"
    hide lixue
    show fangfei squint convicted with dissolve
    Fangfei "You must cut off the head of the snake."
    show fangfei open frown with dissolve
    Fangfei "There once was a man who warmed a snake in his bosom on a cold snowy day. His heart was filled with love for the world, but a snake is a snake."
    Fangfei "Upon recovering, the snake bit the man, and thus the man died."
    show fangfei grit with dissolve
    Fangfei "You can be kind, but you cannot be foolish. A snake is a snake to the end."
    hide fangfei
    show lixue reject with dissolve
    Lixue "If I were to kill you, I would be the snake who bites you to death! A white eyed wolf!"
    hide lixue
    show fangfei mention with dissolve
    Fangfei "My life is unimportant. I would forgive you if that is what you seek."
    hide fangfei
    show lixue reject with dissolve
    Lixue "Forgiveness? What I seek is to continue living well with you."
    hide lixue
    show fangfei stern with dissolve
    "She paused, looking right through me."
    "I knew nothing, nothing at all about her, about this madness that had overtaken her, about the kindness that still overflowed from her eyes, about her lonesome figure."
    show fangfei squint thoughtful with dissolve
    Fangfei "Alright."
    show fangfei closed with dissolve
    Fangfei "Lixue, you are too kindhearted."
    show fangfei open with dissolve
    Fangfei "You need not to accept it now. Perhaps I would have been scared if you were willing so quickly."
    show fangfei resigned with dissolve
    Fangfei "Just... remember to put me out of my misery when the time comes."
    hide fangfei
    show lixue squint sad with dissolve
    Lixue "Why...?"
    hide lixue
    show fangfei closed sad with dissolve
    Fangfei "......"
    "She shook her head and walked away."
    hide fangfei with dissolve
    "Once she was gone, I crumpled to my knees and silently sobbed."

    ##
    scene bg courtyard with fade
    "A number of days passed before I digested my emotions, mindlessly throwing myself into cultivation and avoiding her like the plague."
    show muqing question with dissolve
    Muqing "So even you and your master had a fight."
    show muqing soft with dissolve
    Muqing "Do you want to talk about it?"
    hide muqing
    show lixue squint frown with dissolve
    Lixue "...Yes. That might be for the best."
    show lixue relaxed sad with dissolve
    Lixue "Master told me to do something that I do not want to do. Should I respect her as my teacher and follow her instructions or should I follow my heart and disregard her?"
    show lixue squint with dissolve
    Lixue "What if what she asks for is the right thing to do?"
    hide lixue
    show muqing ask with dissolve
    Muqing "If you want to simply respect your master, then the only choice is to follow her instructions. It\'s an easy choice, a simple choice, an undoubtedly correct choice."
    show muqing talk with dissolve
    Muqing "But that makes your relationship one with no heart."
    Muqing "Right or wrong is ultimately your own judgement to make."
    "I disagreed, furrowing my brows."
    show muqing question with dissolve
    Muqing "What did she ask of you?"
    hide muqing
    show lixue scowl with dissolve
    Lixue "To kill her."
    hide lixue
    show muqing troubled with dissolve
    Muqing "Oh."
    show muqing surprised with dissolve
    Muqing "Wait. What?"
    show muqing sigh with dissolve
    Muqing "I\'m afraid you\'ll be offended that I say this, but your master has a few screws loose in her head asking you to kill her."
    hide muqing
    show lixue scowl with dissolve
    Lixue "You!"
    hide lixue
    show muqing pout with dissolve
    Muqing "Me."
    show muqing talk with dissolve
    Muqing "I doubt she asked it due to some masochistic urge to be slaughtered by her disciple, so what was the reasoning? You said that it was the \'right thing to do.\'"
    hide muqing
    show lixue sad with dissolve
    Lixue "She divined the flow of the Heavenly Way."
    Lixue "And she saw that she would bring great calamity and bloodshed, destroying the cultivation realm if I were to not cut her down."
    show lixue frown with dissolve
    Lixue "The demonic cultivators would rise and tip the balance irreversibly."
    hide lixue
    show muqing frown with dissolve
    Muqing "Then and now, this demonic cultivator mess is still ruining everything and everyone."
    Muqing "But you don\'t want to kill her."
    hide muqing
    show lixue sad with dissolve
    Lixue "What about the cultivation realm?"
    hide lixue
    show muqing ask with dissolve
    Muqing "What about it?"
    show muqing talk with dissolve
    Muqing "You are but a single person. Why does the responsibility of the cultivation realm lay on your shoulders? Why does it depend on one person\'s life and death?"
    hide muqing
    show lixue shocked with dissolve
    Lixue "Is deviating from the Heavenly Way wrong?"
    hide lixue
    show muqing question with dissolve
    Muqing "What is the Heavenly Way?"
    show muqing confident with dissolve
    Muqing "Everyone and their fathers and their dogs say \'Heavenly Way this, Heavenly Way that\', pointing fingers at the good and the bad."
    show muqing frown with dissolve
    Muqing "And for what?"
    hide muqing
    show lixue diligent with dissolve
    Lixue "For balance and peace, for the very fabric of our reality."
    hide lixue
    show muqing subdued with dissolve
    Muqing "Apparently, for you to kill your dearest master."
    hide muqing
    show lixue scowl with dissolve
    Lixue "It\'s terrible."
    hide lixue
    show muqing mention with dissolve
    Muqing "Cultivators with their eyes all the way up in the clouds, thinking about the future all the time, forget this one important thing."
    Muqing "To start with, the Heavenly Way is not a mountain but rather an eternally flowing river."
    show muqing thoughtful with dissolve
    Muqing "What did they see? Certainly it will happen, but did they truly understand what had happened? To take steps to mitigate it might even bring greater ruin."
    hide muqing
    show lixue retort with dissolve
    Lixue "Are you saying that the basis of Master\'s request was meaningless?"
    hide lixue
    show muqing mention with dissolve
    Muqing "No."
    Muqing "If she is fated to be cut down or bring ruin to the world, that\'s fate."
    show muqing talk with dissolve
    Muqing "But whether or not you should necessarily be asked to kill her? Isn\'t that just her own selfish, foolish interpretation?"
    hide muqing
    show lixue diligent with dissolve
    Lixue "You do not know her."
    "Nor that she picked me up for the sake of taking her life."
    hide lixue
    show muqing mild with dissolve
    Muqing "You\'re right. I don\'t know her. Perhaps the future she saw could only be interpreted in one way."
    show muqing ask with dissolve
    Muqing "Bluntly putting it, misinterpretation or not, the safest option is to kill her. That is the so-called correct option. In the cultivation realm, evil can not be allowed to live."
    show muqing talk with dissolve
    Muqing "Not even the potential for evil. At least... not even the slightest shadow of demonic cultivation."
    Muqing "Sacrifice one life and one heart for the rest of the world."
    Muqing "A single drop of blood in exchange for the peace of everyone else."
    show muqing sad with dissolve
    Muqing "Even if that single drop of blood is more precious than anything else in the entire world."
    hide muqing
    show lixue frown with dissolve
    Lixue "But even so..."
    show lixue soft with dissolve
    Lixue "Is it alright for me to say no?"
    show lixue frown with dissolve
    Lixue "To selfishly reject her request because I do not believe in the future she saw? Because... even if that was the future she saw, I do not accept it?"
    hide lixue
    show muqing neutral with dissolve
    Muqing "Haven\'t you already made up your mind?"
    hide muqing
    show lixue soft with dissolve
    Lixue "I..."
    Lixue "I suppose I have."
    hide lixue
    show muqing alas with dissolve
    Muqing "Really, kids these days, coming to consult their elders to confirm the decision that they already made."
    hide muqing
    show lixue hope with dissolve
    Lixue "It can\'t be helped."
    hide lixue
    show muqing ask with dissolve
    Muqing "How are you feeling right now?"
    hide muqing
    show lixue serious with dissolve
    Lixue "...A little angry."
    hide lixue
    show muqing mild with dissolve
    Muqing "A reasonable answer."
    show muqing speak with dissolve
    Muqing "Now then, pick up a practice sword and let\'s have a spar."
    "With no notice, she flung a sword at me."
    show muqing sure with dissolve
    Muqing "Show me how good you are with your flames and sharpen that dull blade into something sharp enough to cut steel."
    hide muqing
    show lixue hesitant with dissolve
    Lixue "Alright."
    "I took a deep breath and adjusted my grip on the sword."
    "{i}Clang!{/i}"
    "After getting thoroughly beaten, I felt the slightest weight lifted from my chest."
    stop music fadeout 3.0

    ##
    scene bg courtyard with fade
    #play music Sad_Intro
    #queue music Sad_Loop
    play music "<loop 21.745>/audio/music/Sad (Full).ogg"
    "My interactions with Master became cold, neither of us willing to budge from our stances. I took to avoiding her."
    "Where she went, I could not be. Would we fight if we met? Or would she convince me to deal her a fatal blow?"
    "Studying with Sister Muqing, I found that the spirit had filled the gap of a teacher. I learned the secret techniques of an ancient time with vigor."
    "Before I knew it, I had crafted a small knife. This knife that I normally would have gifted to Master, I could only hold onto and turn it back into scrap metal."
    "I wanted to reconcile, but I was unwilling to compromise. On this Juyi Peak made for just two people, how much effort did I expend to avoid her who I wanted to see?"
    "Amidst my turmoil, unexpectedly, my martial uncle from the Dalin Sect came to visit."
    "Overhearing their conversation, I learned that he wanted to take Master back to the Dalin Sect with him."
    "They seemed so close, and thinking of how well some disciple at the Dalin Sect had called them well-matched when we had visited previously, my heart filled with vinegar."
    "I did not like that."
    "I really did not like that."

    ##
    scene bg courtyard with fade
    "There was something wrong with my heart."
    show muqing frown with dissolve
    Muqing "Your feelings for your master will create a heart demon for you, and you will be unable to proceed in your cultivation."
    "I unconsciously grasped at my chest, at my heart that felt constricted as if knots had formed."
    hide muqing
    show lixue sus with dissolve
    Lixue "What do you mean by that?"
    Lixue "My feelings for my master..."
    hide lixue
    show muqing talk with dissolve
    Muqing "Is it love or is it obsession?"
    hide muqing
    show lixue serious with dissolve
    Lixue "It is nothing more than respect for her."
    "Her eyes pierced me. Even I knew that the words that came out of my mouth were lies and my chest tightened."
    hide lixue
    show muqing confident with dissolve
    Muqing "No."
    show muqing alas with dissolve
    Muqing "I would know the look of someone who has fallen in love too deeply to dig herself out."
    show muqing mention with dissolve
    Muqing "If you\'re willing to let it die like that, that\'s fine too. You have to realize it before you can discard it or pursue it."
    show muqing sad with dissolve
    Muqing "Otherwise, it\'ll just become an obsession."
    hide muqing
    show lixue retort with dissolve
    Lixue "I am her disciple. She is my master."
    "I knew I had long passed the point where she held my hand through my studies. She had less and less to directly teach me."
    hide lixue
    show muqing mention with dissolve
    Muqing "If you saw her as just a teacher, you would have agreed to cut her down."
    hide muqing
    show lixue frown with dissolve
    Lixue "That..."
    hide lixue
    show muqing sigh with dissolve
    Muqing "If I didn\'t care about you, I would\'ve let you continue onward, but I can feel a dangerous fluctuation within your cultivation."
    show muqing troubled with dissolve
    Muqing "At first, I thought that it was just your mood and worries about your master\'s request, but there\'s something else in there."
    show muqing thoughtful with dissolve
    Muqing "I\'ll give you this. You\'re pretty good at hiding it, but I am the one who forged your Fenghuang Sword that touched your blood. Did you think I wouldn\'t notice?"
    Muqing "If you let this go on, it\'ll become a heart demon and lead to qi deviation."
    show muqing squint with dissolve
    Muqing "I won\'t tell you that your love will succeed. I won\'t tell you that you\'ll necessarily achieve a happy ending. I\'m just telling you to face your own emotions."
    hide muqing
    show lixue retort with dissolve
    Lixue "Easy for you to say."
    hide lixue
    show muqing talk with dissolve
    Muqing "I know."
    Muqing "No matter what you do, just don\'t let it become a regret-filled obsession."
    "I fell into silence."
    hide muqing with dissolve
    "She, Master, the fairy who saved my life. Bai Fangfei was warm and kind, and she filled my heart with a soft tenderness."
    "I wanted to spend the rest of my life with her. I wanted to support her just as she supported me. I could not deny that, at some point, I had fallen in love with her."
    "Not just a platonic love but rather a romantic love."
    "Yet she told me to kill her, so this love would never come to fruition. She, who I loved, told me to cut her down with my own two hands."
    show muqing neutral with dissolve
    Muqing "It\'s like I bullied you."
    hide muqing
    show lixue sad with dissolve
    Lixue "Yes, what a bully you are, Sister Muqing."
    show lixue soft with dissolve
    Lixue "Was falling in love supposed to hurt this much?"
    "Hesitantly, she placed her hand on my shoulder."
    hide lixue
    show muqing soft with dissolve
    Muqing "No."
    show muqing sorry with dissolve
    Muqing "I\'m sorry."
    show muqing sad with dissolve
    Muqing "Love is supposed to be something sweet."
    stop music fadeout 3.0

    ##
    scene bg night_courtyard with fade
    play music "<loop 25.600>/audio/music/Suspenseful (Full).ogg"
    #play music Suspenseful_Intro
    #queue music Suspenseful_Loop
    "My martial uncle left soon enough."
    "In the middle of the night, a sharp unease roused me from my sleep. Unable to return to my slumber, I rose to take a quick stroll and breathe in some fresh air."
    "Each step filled me with a greater sense of dread. Was it the snow or the clouds? I felt that something foul must have been afoot."
    "Walking, I chanced upon Master."
    show fangfei squint_night stern with dissolve
    Fangfei "Lixue."
    hide fangfei
    show lixue open_night question with dissolve
    Lixue "Master."
    "Snow fell, dark clouds covering the sky. As the wind blew, the air stirred ominously outside. I seemed to hear a ruckus in the distance."
    "Suddenly, a bright flash of lightning struck down at the town below."
    hide lixue
    show fangfei open_night frown with dissolve
    Fangfei "Inauspicious signs. Demons are stirring."
    "She turned away as the thunder rumbled. In her hand was her sword as if she had prepared to head out at this time of night."
    show fangfei serious with dissolve
    Fangfei "I will head down to the town at the base of the mountain and take care of whatever is happening."
    hide fangfei
    show lixue open_night thinking with dissolve
    Lixue "Master, I will accompany-"
    hide lixue
    show fangfei open_night frown with dissolve
    Fangfei "You stay here."
    hide fangfei
    show lixue open_night frown with dissolve
    Lixue "Huh?"
    hide lixue
    show fangfei open_night stern with dissolve
    Fangfei "Lixue, you stay here."
    "Stunned by Master\'s cold rejection, I wordlessly watched as she stepped upon her flying sword and departed, and I did not follow."
    hide fangfei
    "The town below was on fire."
    "Even so, I did not follow."
    show lixue frown with dissolve
    Lixue "......"
    Lixue "Why did you tell me to stay here?"
    "I continued my late night stroll, having no way to sleep. The time must have been around two hours past midnight."
    "Then I came across Sister Muqing as well."
    hide lixue
    show muqing open_night question with dissolve
    Muqing "Lixue? Why are you awake at such an hour?"
    hide muqing
    show lixue serious with dissolve
    Lixue "I couldn\'t sleep."
    Lixue "She headed down to the town at the base of the mountain, saying that demons were stirring. Was she speaking of evil ghosts or demonic cultivators?"
    hide lixue
    show muqing open_night thoughtful with dissolve
    Muqing "Demon hunting, huh."
    Muqing "She didn\'t take you with her?"
    "I shook my head."
    show muqing mild with dissolve
    Muqing "By the looks of it, you have no intention of sleeping when your dear master is out fighting the forces of evil."
    show muqing neutral with dissolve
    Muqing "You won\'t be doing her any favors wearing yourself out, pacing around. Let\'s talk."
    hide muqing
    show lixue open_night question with dissolve
    Lixue "About what?"
    show lixue hesitant with dissolve
    Lixue "Great ancestor, you should have more interesting stories than me, so I will leave the talking to you."
    hide lixue
    show muqing open_night smirk with dissolve
    Muqing "If I talk about the demons and ghosts of my era, you might be spooked."
    show muqing pout with dissolve
    Muqing "At least right now, you have no strong demonic cultivation sect and no demonic grandmaster uniting the demons and such, right?"
    hide muqing
    show lixue open_night muse with dissolve
    Lixue "Demonic grandmaster..."
    hide lixue
    show muqing open_night confident with dissolve
    Muqing "Evil ghosts are emboldened by leadership, and strong demons tend to mean a strong demonic faction."
    show muqing smirk with dissolve
    Muqing "The good thing is that most of the problems back then should be dead."
    Muqing "Small fries are small fries. No one really cares that much about them, but the strong ones, they got hunted down."
    hide muqing
    show lixue open_night thinking with dissolve
    Lixue "What was it like, hunting demons back then?"
    hide lixue
    show muqing open_night thoughtful with dissolve
    Muqing "Some ordeals were more difficult than others."
    show muqing frown with dissolve
    Muqing "Most troublesome one was a demon with a thousand faces. It didn\'t follow the grandmaster of the demonic cultivators at the time, so it was really a pain."
    hide muqing
    show lixue open_night serious with dissolve
    Lixue "Was it not better for demons to not follow the grandmaster?"
    hide lixue
    show muqing closed_night neutral with dissolve
    Muqing "Mm."
    show muqing open_night with dissolve
    Muqing "The grandmaster had subjugated the demonic cultivation world and brought it under her heel."
    show muqing pleasant with dissolve
    Muqing "Her strong demonic energy made many demons subservient to her by their animal instinct. At the very least, they behaved less like wild beasts."
    show muqing smirk with dissolve
    Muqing "Of course, an army under an organized leader might be worse than a horde of animals."
    hide muqing
    show lixue open_night wry with dissolve
    Lixue "You speak pretty mildly about that demonic grandmaster."
    hide lixue
    show muqing open_night question with dissolve
    Muqing "She wasn\'t too bad, not really."
    hide muqing
    show lixue open_night question with dissolve
    Lixue "Even though she was a demonic cultivator?"
    hide lixue
    show muqing closed_night smirk with dissolve
    Muqing "Demonic cultivators still have their rationality. The orthodox cultivators are just way too quick to assume that they\'re monsters."
    hide muqing
    show lixue open_night thinking with dissolve
    Lixue "Certainly, to call them mere monsters would be demeaning to all those they harmed."
    hide lixue
    show muqing open_night thoughtful with dissolve
    Muqing "Just like there are different personalities amongst the orthodox cultivators, there are different personalities amongst the demonic cultivators."
    Muqing "I won\'t deny that to reach the peak of the demonic world, the grandmaster must have shed a lot of blood."
    show muqing confident with dissolve
    Muqing "But back to that thousand faced demon."
    Muqing "That was one of the first ones Mengmeng and I took down together."
    show muqing alas with dissolve
    Muqing "Mengmeng didn\'t like ghosts or demons. At best she was okay with them, but when push came to shove, she was much better at dealing with them than I was."
    hide muqing
    show lixue open_night wry with dissolve
    Lixue "What a way to put Miss Xuan\'s feelings on demons."
    hide lixue
    show muqing closed_night confident with dissolve
    Muqing "She probably had a grudge against them for bullying her when she was weaker."
    hide muqing
    show lixue open_night wry with dissolve
    Lixue "Bullying, is that really the right way to describe being attacked by demons?"
    hide lixue
    show muqing open_night grin_night with dissolve
    Muqing "Haha, you\'d be surprised."
    "As usual, Xuan Mengdie\'s mysteries continued to grow."
    hide muqing
    show lixue open_night question with dissolve
    Lixue "So, regarding the thousand faced demon, did it truly have one thousand faces?"
    hide lixue
    show muqing open_night thoughtful with dissolve
    Muqing "Yes, it was an ugly thing, faces running down its sides, expressions all in agony. It was a creature that ate people and collected its victims\' faces and souls."
    "I shuddered, imagining what such a demon would look like. At best, my mental image was grotesque."
    show muqing confident with dissolve
    Muqing "To kill it, every single face had to be destroyed. Every single soul had to be released. The demon core would otherwise move from face to face."
    show muqing thoughtful with dissolve
    Muqing "As if taunting its hunters, it would use the faces to speak in the voice of a human and cry, pretending that the victim could still be saved."
    show muqing frown with dissolve
    Muqing "A number of cultivators had fallen to that trick, refusing to kill a face that could still be a living person. It wasn\'t that I didn\'t understand that, but..."
    show muqing troubled with dissolve
    Muqing "As long as one face remained intact, the demon could escape, shedding its mass, and seek out more victims."
    Muqing "In order to stop it once and for all, we had to set a few traps in preparation..."
    "She described the demon hunting, and the night passed."
    "After a long story, she stretched. I hadn\'t expected to be so enraptured by her tales of adventure."
    show muqing mild with dissolve
    "They fought side by side, clashing and tripping over each other as plans fell apart, yet they still watched each other\'s backs after a compromise."
    "Ultimately coming together to strike the last blow, Sister Muqing and Miss Xuan achieved a glorious victory."
    show muqing grin_night with dissolve
    "What a nice story."
    "Although my cultivation had not caught up to Master\'s, I wished that I could be her support like they were for each other and become strong enough to protect her."
    "Yet she wanted me to kill her."
    "The thought dampened my spirits, so I lightly slapped my face."
    show muqing pout with dissolve
    Muqing "Really still, the weather\'s foul."
    show muqing alas with dissolve
    Muqing "I could really do with a drink right now, but it looks like it\'s about time for me to go."
    hide muqing
    show lixue open_night frown with dissolve
    Lixue "Why?"
    hide lixue
    show muqing open_night neutral with dissolve
    Muqing "By my estimates, your master should be returning soon. Like I\'ve said before, I have no intention of meeting with her, so ta-ta."
    hide muqing
    show lixue open_night mild with dissolve
    Lixue "Then, until later."
    "Before I finished saying goodbye, her image faded away."
    stop music fadeout 3.0
    "I wondered how she noticed Master when I could not feel Master\'s spiritual presence. At best, Master was at the edge of Juyi Peak."
    "The snow slowly ceased. As the last snowflake fluttered to the ground, another flash of lightning came, followed by a loud peal of thunder."
    "Master returned."
    play music "<loop 4.796>/audio/music/Action (Full).ogg"
    #play music Action_Intro
    #queue music Action_Loop
    show lixue open_night diligent with dissolve
    "As she descended, I ran over to her, and she fell into my arms. I was at first surprised, and then I smelled the sharp scent of blood."
    "Holding her in my arms, I felt the sting of faint wisps of demonic energy clinging to her."
    show lixue open_night frown with dissolve
    Lixue "Master!"
    hide lixue
    show fangfei squint_night hesitant with dissolve
    Fangfei "Lixue, you\'re still awake..."
    Fangfei "There was a stronger demon than I expected..."
    hide fangfei
    show lixue open_night frown with dissolve
    Lixue "You\'re injured!"
    "She winced and clutched her stomach and chest where the lower and middle dantian were located as if those important places had been injured."
    "I did not see blood there, so I feared that it was not her physical body but her spiritual body that had been damaged."
    "I tried to purify the demonic energy externally, but what I could rid from her seemed to be replenished immediately from something that hid inside of her body."
    hide lixue
    show fangfei squint_night pained with dissolve
    Fangfei "The demon is dead. Half of the town has burned down, but they should be able to rebuild as no one died."
    hide fangfei
    show lixue open_night diligent with dissolve
    Lixue "Do not speak anymore. Let me bring you to a bed."
    "A cold drop of sweat ran down her forehead. She coughed, unable to hold back, and spit up a mouthful of dark, dirty blood."
    hide lixue
    show fangfei squint_night bloody with dissolve
    Fangfei "Such an anxious expression, Lixue..."
    Fangfei "I hate that I put it on your face."
    "Hypocrite."
    hide fangfei
    show lixue open_night frown with dissolve
    stop music fadeout 3.0
    Lixue "......"
    #play music Sad_Intro
    #queue music Sad_Loop
    play music "<loop 21.745>/audio/music/Sad (Full).ogg"
    scene bg night_room with fade
    "I lifted her body, which was as light as a feather, and brought her inside to a warm room, placing her in bed."
    "She seemed in pain, her delicate brows furrowed."
    "I grabbed a number of reference books to find what medicine I should make before I retrieved the materials for it."
    "Grinding herbs and applying spiritual energy to the mush, I listened as her pained breathing steadied."
    "By the time I finished the medicine, it seemed that she was unconscious."
    "I slowly spoonfed her the medicine, hoping that she could swallow and process the healing energy. I apologized internally that the medicine was surely quite bitter."
    "Once the medicine was done with, I sat by her bedside."
    "Thinking that she was unconscious, I kissed her cold fingertips."
    show lixue open soft with dissolve
    Lixue "I love you, Bai Fangfei."
    "I wanted to call her by her name. If someone else had picked me up in the snow, I would not have fallen for them. In my heart was only her."
    "She was asleep, so I could tell her these feelings that I had realized in my chest. Then I would let go of them, these which would never bloom."
    $ fangfei = "Fangfei"
    Fangfei "No, you cannot love me that way."
    show lixue sad with dissolve
    Lixue "......"
    show lixue relaxed with dissolve
    Lixue "I know."

    ##
    scene bg room with fade
    "She stayed bedridden for a number of days after."
    "Not only did the fight with the demon damage her dantian, demonic energy had also snaked its way into her weakened body, forcing her to fight against it."
    "Pretending my words of love had never happened, I continued to tend at her bedside."
    show fangfei burdened with dissolve
    Fangfei "You might have to cut down the tree this year."
    hide fangfei
    show lixue retort with dissolve
    Lixue "Why? Even though it does not bloom, it is still alive."
    hide lixue
    show fangfei hesitant with dissolve
    Fangfei "Cut her down when she wilts and dies. Let the ancient peach tree move on, and perhaps the next tree planted in that spot will live a happier life and bloom."
    "Master always sounded so fatalistic about the unblooming tree, saying without a doubt that it would perish without letting me once see its blossoms."
    hide fangfei
    show lixue retort with dissolve
    Lixue "I don\'t want to plant a new tree. I wish that the tree would flower."
    hide lixue
    show fangfei concerned with dissolve
    Fangfei "The normal peach tree only lives one or two decades. Her time has long been up."
    hide fangfei
    show lixue hope with dissolve
    Lixue "Perhaps it was cultivating to become a yao and hit some stumbling block. It would be nice if the peach tree could succeed."
    hide lixue
    show fangfei resigned with dissolve
    Fangfei "Yes, I suppose it would be."
    hide fangfei
    show lixue soft with dissolve
    Lixue "Juyi Peak is dense with spiritual energy. This should be a good place for a yao to cultivate."
    hide lixue
    show fangfei hesitant with dissolve
    Fangfei "Yes, it is."
    show fangfei squint pained with dissolve
    Fangfei "{i}Cough, cough.{/i}"
    "Seeing her cough, I poured her a cup of warm water."
    "She nursed the cup, taking a few sips, but the coughing did not stop, so she set the cup aside. Instead, coughing turned to wheezing, and between her fingers, I saw a few droplets of red."
    "Dark demonic energy swirled around her, corroding at her spiritual energy that tried to combat it. The miasma sent a chill down my spine."
    "She had not recovered at all."
    hide fangfei
    show lixue worry with dissolve
    Lixue "Master!"
    "She stared me in the eye as if she had given up."
    hide lixue
    show fangfei squint wiped with dissolve
    Fangfei "Lixue, you must... cut me down now. Or else, the whole cultivation realm will be doomed."
    hide fangfei
    show lixue scowl with dissolve
    Lixue "No!"
    hide lixue
    show fangfei squint wiped with dissolve
    Fangfei "Please."
    Fangfei "{i}Cough-{/i} I beg of you, Lixue."
    "Red-black blood came out of her mouth. The demonic energy swarmed to the blood like locusts, festering in it like maggots."
    show fangfei squint bloody with dissolve
    Fangfei "You cannot allow me to bring calamity to this world."
    "She grasped weakly at my sleeve, tugging to convince me."
    hide fangfei
    show lixue stumble with dissolve
    Lixue "N-no..."
    hide lixue
    show fangfei squint wiped with dissolve
    Fangfei "Please..."
    "I panicked, my heart in disarray. I could not stand to see her desperate, pleading form that seemed to suffer immeasurable pain."
    hide fangfei with dissolve
    Muqing "Before you act hastily, knock her out."
    "Sister Muqing\'s clear voice cut through my distress."
    Muqing "I won\'t show myself right now, but follow my instructions. First knock her out. Her own negative emotions should be feeding the demonic energy."
    "I nodded."
    show lixue closed sad with dissolve
    Lixue "I\'m sorry."
    "I followed Sister Muqing\'s instruction and knocked her out."
    hide lixue with dissolve
    Muqing "Let me show you how to seal away the demonic energy."
    "She started to develop an array, making it up in the moment, telling me what to draw."
    show lixue open sad with dissolve
    "With no good spiritual ink at hand, I bit into my fingers and drew with my blood. The markings would disappear once the array was activated."
    "A good hour passed."
    show lixue sus with dissolve
    Lixue "Is this enough?"
    "I activated the array with a flash of white light."
    show lixue frown with dissolve
    "My hands hurt, trembling. Blood oozed out of the multitude of small cuts even as they began to heal.."
    hide lixue with dissolve
    Muqing "No, it\'s only a stop gap before the more complicated steps. This won\'t be enough. Just keep her asleep for now."
    Muqing "You should know how to do that, right?"
    show lixue serious with dissolve
    Lixue "Yes."
    Muqing "And while you\'re at it, seal away her memories of this as well."
    show lixue sus with dissolve
    Lixue "Sealing away memories? That\'s unheard of."
    "At least, it was unheard of outside of demonic arts."
    hide lixue with dissolve
    Muqing "Something as simple as a few memories on someone as weak as your master is easy."
    Muqing "I can seal away the entire realm\'s memory of a name, a place, a history, so why shouldn\'t you be able to at least erect a temporary dam to protect your master\'s mind?"
    "She explained to me how to create a small memory blocking spell."
    show lixue frown with dissolve
    Lixue "Protect? Such an excuse is worse than no excuse at all."
    hide lixue with dissolve
    Muqing "Alright, alright. I don\'t want her to remember feeling my presence here if her spiritual senses were sharp enough to notice me."
    show lixue relaxed frown with dissolve
    "I disagreed with Sister Muqing\'s appraisal of the situation. It felt more for protecting my own heart than anything else."
    show lixue open scowl with dissolve
    Lixue "If you say such a thing..."
    show lixue sad with dissolve
    "I followed her directions, and by the time I finished, Master\'s brows seemed to have relaxed."
    show lixue frown with dissolve
    "Looking at her peacefully sleeping form, I apologized silently and left the room."
    stop music fadeout 3.0
    scene bg courtyard with dissolve
    play music "<loop 25.600>/audio/music/Suspenseful (Full).ogg"
    #play music Suspenseful_Intro
    #queue music Suspenseful_Loop
    "I exited to the familiar courtyard, stopping by the flowerless tree. As I frowned, Sister Muqing showed herself before me."
    show muqing frown with dissolve
    Muqing "Your Master is unlucky."
    hide muqing
    show lixue sus with dissolve
    Lixue "How do you know about all of this? How to deal with demonic energy like that and how to cast mental manipulation spells?"
    hide lixue
    show muqing talk with dissolve
    Muqing "Those are frowned upon, aren\'t they?"
    show muqing squint ask with dissolve
    Muqing "What can I say? I\'m pretty intimate with demonic arts."
    hide muqing
    show lixue shout with dissolve
    Lixue "Are you a demonic cultivator!?"
    hide lixue
    show muqing open frown with dissolve
    Muqing "Put that sword down. You\'ve never beaten me in a spar."
    show muqing speak with dissolve
    Muqing "And I\'m not a demonic cultivator. What is it with kids these days, saying \'demonic cultivator this, demonic cultivator that\' just like those bunch of old fogeys?"
    hide muqing
    show lixue shocked with dissolve
    Lixue "My apologies. I was too hasty."
    hide lixue
    show muqing talk with dissolve
    Muqing "Out of all the people in this world, I should be the so-called righteous cultivator most knowledgeable about demonic cultivators."
    Muqing "Some of the secrets that I\'ll tell you to help you deal with your master\'s problem as she temporarily sleeps... Well, let\'s just say that they\'re {i}really secret{/i} secrets."
    show muqing sure with dissolve
    Muqing "If you\'re caught knowing them by the wrong people, your head might not be connected to your neck for very long."
    hide muqing
    show lixue shocked with dissolve
    Lixue "Are they dark arts? Will they not hurt her?"
    hide lixue
    show muqing confident with dissolve
    Muqing "Fight poison with poison."
    show muqing pout with dissolve
    Muqing "To start with, even demonic cultivators have healing practices. They\'re just... a bit too distasteful for the typical orthodox cultivator to deal with."
    show muqing talk with dissolve
    Muqing "Don\'t worry. I won\'t do anything to hurt her. Do you trust me?"
    "I looked at her, seeing through her ghostly body. Did I trust her? She who had forged my Fenghuang Sword and taught me so many of her secret skills?"
    "The answer to her question seemed so simple."
    hide muqing
    show lixue serious with dissolve
    Lixue "Yes. I trust you."
    hide lixue
    show muqing neutral with dissolve
    Muqing "Good, good."
    hide muqing
    show lixue soft with dissolve
    Lixue "Thank you for trusting in me with your secrets."
    hide lixue
    show muqing pleasant with dissolve
    Muqing "No, I just can\'t stand you losing the person you love yet."
    show muqing squint confident with dissolve
    Muqing "Yeah. I would have disqualified you as a person if you gave up on her."
    stop music fadeout 3.0

    ##
    scene bg courtyard with fade
    play music "<loop 18.701 >/audio/music/Peaceful (Full).ogg"
    #play music Peaceful_Intro
    #queue music Peaceful_Loop
    "Master slept for a while longer, and I cared for her under Sister Muqing\'s guidance."
    "The demonic energy dissipated, and eventually she awoke. The relief I felt as her eyes fluttered open groggily could not be described."
    "She recovered."
    "As if nothing had happened, our idyllic everydays returned. Normal and peaceful, perhaps unmemorable days. I liked our days without strife."
    show fangfei squint surprised with dissolve
    Fangfei "I feel as if I awoke from a long dream."
    show fangfei open thoughtful with dissolve
    "She gently pet my head."

    # PART III
    scene bg courtyard with fade
    "But there was no such thing as a dream that lasts forever."
    "Walking around in the courtyard, having a conversation with Sister Muqing, I complacently thought of the future. Fenghuang Sword was warm in my hand."
    show muqing open ask with dissolve
    Muqing "Are you happy right now?"
    hide muqing
    show lixue hesitant with dissolve
    Lixue "Mm."
    hide lixue
    show muqing mention with dissolve
    Muqing "And the matter with your master?"
    hide muqing
    show lixue mild with dissolve
    Lixue "I gave up pursuing Bai Fangfei."
    show lixue relaxed hesitant with dissolve
    Lixue "My affections, they will never bloom, so... if placing them aside will allow us to continue being as we are, then I will simply continue calling her Master forevermore."
    hide lixue
    show muqing squint troubled with dissolve
    Muqing "Bai... Bai Fangfei."
    show muqing open thoughtful with dissolve
    Muqing "If you\'re satisfied, that\'s fine."
    hide muqing
    show lixue hope with dissolve
    Lixue "I\'m happiest when I can accompany her."
    Lixue "Even if I have to walk behind her a few steps."
    hide lixue
    stop music fadeout 3.0
    show fangfei surprised with dissolve
    #play music Action_Intro
    #queue music Action_Loop
    Fangfei "Lixue?"
    play music "<loop 4.796>/audio/music/Action (Full).ogg"
    "Too caught up in my thoughts, I had not noticed her approach. A sense of dread rose in my chest when she froze, her eyes locked onto Sister Muqing."
    hide fangfei
    show lixue surprised with dissolve
    Lixue "Master?"
    hide lixue
    show fangfei shocked with dissolve
    Fangfei "That spirit- Ngh!"
    show fangfei squint grit with dissolve
    Fangfei "——–! Hah... hah... No! Khh!"
    show fangfei closed agony with dissolve
    "Muffling screams of pain, she fell to her knees, clutching at her head."
    hide fangfei
    "I ran to her before being pushed back by an outburst of demonic energy that sent a sharp ringing through my ears."
    "Her screams stopped, and she slowly rose, hand over her face as if unused to this body."
    show lixue angry with dissolve
    Lixue "...You\'re not Master."
    hide lixue
    show muqing hurt with dissolve
    Muqing "......"
    $ mengdie = "???"
    hide muqing
    show mengdie surprised with dissolve
    Mengdie "...Awakening to this vessel... I\'m surprised."
    show mengdie sneer with dissolve
    Mengdie "I\'m surprised to see your dirty mien before me... Bai Muqing!"
    "...Bai?"
    hide mengdie
    show muqing beg with dissolve
    Muqing "Mengmeng."
    hide muqing
    show mengdie squint shout with dissolve
    Mengdie "Don\'t call me that!"
    show mengdie open sneer with dissolve
    Mengdie "What is it that they call me nowadays, Ancient Calamity? Kukufuhahahyahaha, it really is just so funny."
    $ mengdie = "Mengdie"
    show mengdie smile with dissolve
    Mengdie "The name Xuan Mengdie has been forgotten, but that\'s fine. That\'s fine. I\'m just a vengeful spirit, now aren\'t I?"
    show mengdie squint with dissolve
    Mengdie "Lixue, your master is sorry."
    show mengdie sneer with dissolve
    Mengdie "I slept and I\'ve awoken and I\'ll finally destroy this accursed realm. I can\'t have you fools getting in my way."
    "Xuan Mengdie drew Master\'s sword, pointing the blade at Sister Muqing and me."
    hide mengdie
    show lixue shout with dissolve
    Lixue "You!"
    "That sword did not belong to her."
    "Sister Muqing picked up a sword from nearby."
    hide lixue
    show muqing declare with dissolve
    Muqing "I\'m afraid I can\'t let you leave."
    "She gestured with her hand, triggering a flash of light around the boundary of Juyi Peak."
    "At some point, she must have set up some sort of sealing array around the peak, preventing the Ancient Calamity\'s demonic energy from seeping out and attracting a horde of demons."
    "What, how, and why? I didn\'t know if I could trust her anymore."
    hide muqing
    show mengdie open frown with dissolve
    Mengdie "Tch. That\'s fine. I was going to lop off your head before leaving anyhow."
    hide mengdie
    show muqing sad with dissolve
    Muqing "I\'m dead, so that might be hard."
    hide muqing
    show mengdie squint shout with dissolve
    Mengdie "Shut up!"
    scene CG_fight with vpunch
    "Xuan Mengdie moved like a blur, slashing at Bai Muqing with a blade covered in demonic energy."
    play sound impact
    "{i}Clang!{/i}"
    "Muqing blocked the blow and jumped back."
    Muqing "Hasty!"
    show CG_fight2 with vpunch
    Mengdie "Hasty!? I\'ve waited thousands of years to send you to hell!"
    play sound sword
    "{i}Shing!{/i}"
    "Xuan Mengdie closed in on Muqing once more, slashing at Muqing with mad fervor."
    "Yet I could not deny that there was skill in her swordsmanship, a swordsmanship tainted with demonic insanity."
    play sound impact
    "{i}Clang!{/i}"
    "They locked blades."
    "Xuan Mengdie pushed against Muqing, trying to use her weight to overwhelm Muqing. Her demonic energy swirled, and the air around them seemed to thicken."
    "However, Master\'s build was too small and the demonic art insufficient."
    show CG_fight with vpunch
    Mengdie "You\'re weak!"
    Muqing "Let me speak with you properly instead of fighting! Mengmeng!"
    show CG_fight2 with dissolve
    Mengdie "Who wants to listen to your damn snake tongue? That\'s the first thing I\'ll cut off!"
    "Their standstill lasted only for a moment."
    scene bg courtyard with vpunch
    "Muqing twisted, breaking the tension between their swords, and threw a quick kick toward Xuan Mengdie\'s abdomen."
    play sound slash
    "Leaping back, Xuan Mengdie retaliated, throwing a small hidden weapon toward Muqing."
    "The projectile whistled a ghastly sound as it flew through the air."
    "Muqing dodged, wincing as it shattered into tainted shrapnel that burned like acid through a nearby rock. Even for a spirit with a materialized body, that would not be a laughable injury."
    show CG_fight with vpunch
    "Exchanging blows, they seemed as if in their own universe, dancing to some angry ceremony between the two of them."
    "The Ancient Calamity didn\'t see me as a threat."
    "Even though the body she stole was my master\'s."
    play sound sword
    "{i}Clang!{/i}"
    "Sparks flew as the demonic and spiritual energies imbued in their blades clashed."
    "White against black, black against white. A practice sword sharpened by spiritual energy alone crashed against a proper spirit sword tainted with an incompatible darkness."
    "I watched, training my eyes on their movements."
    scene bg courtyard with vpunch
    "Then I jumped into the fray."
    play sound sword
    "{i}Shing!{/i}"
    show mengdie questioning with dissolve
    Mengdie "Two on one? How honorable you are."
    hide mengdie
    show lixue frown with dissolve
    Lixue "......"
    hide lixue
    show mengdie smile with dissolve
    Mengdie "Not afraid to hurt your dear master, Lixue?"
    "I took a swipe at her, my blow deflected much too easily."
    hide mengdie
    show lixue retort with dissolve
    Lixue "You are not my master, Xuan Mengdie."
    "She was right. Rather than to fight to kill, I wanted to fight to disarm or incapacitate."
    hide lixue
    show mengdie frown with dissolve
    Mengdie "I think you might be a bit of a dimwit. Is that why this body and Bai Muqing seem to like you?"
    hide mengdie
    show muqing sorry with dissolve
    Muqing "...Mengmeng..."
    hide muqing
    show mengdie neutral with dissolve
    Mengdie "You can shut up."
    "I swung my sword, but my strike was dodged. Receiving payback in the form of a barrage of hidden weapons, I had to dash backward."
    "As I evaded, Xuan Mengdie rushed at Muqing."
    play sound impact
    "{i}Clang!{/i}"
    "Metal grated on metal. Master\'s sword was crying out."
    play sound sword
    "{i}Shing!{/i}"
    "I struck, Fenghuang Sword leaving the shadow of spiritual energy as it sliced through the air."
    "Kicking my sword, Xuan Mengdie utilized the momentum of the attack to fly over my head and land behind me. She was in my blind spot."
    "I hastily turned."
    hide mengdie
    show muqing declare with dissolve
    Muqing "Lixue, watch out!"
    "Muqing\'s sword interrupted Xuan Mengdie\'s ambush, the conflicting energies imbued in the swords screeching."
    "She retook Xuan Mengdie\'s attention."
    show muqing hurt with dissolve
    Muqing "This fight should be between just you and me."
    hide muqing
    show mengdie shout with dissolve
    Mengdie "What qualification do you think you have to say that?"
    show mengdie laugh with dissolve
    Mengdie "You should just be a warmup. I\'ll raise the demonic realm again and let those little beasts feast to their hearts delight."
    Mengdie "The cultivation realm, wouldn\'t it be so much better without those so called righteous cultivators?"
    Mengdie "I\'ll cut the ones from the Bai Pavilion limb by limb and skin them alive, and if any of those old fools from back then are still alive..."
    hide mengdie
    show muqing talk with dissolve
    Muqing "The Bai Pavilion has already been destroyed."
    hide muqing
    show mengdie squint frown with dissolve
    Mengdie "...Is that so?"
    Mengdie "Enough talking!"
    "Xuan Mengdie breathed. Her eyes saw. The sword in her hand moved like light. It missed Muqing."
    "A talisman flew out, proving her sword strike to be a feint, and caused a surge of demonic energy to envelop Muqing."
    hide mengdie
    show muqing squint scowl with dissolve
    Muqing "Gkh...!"
    show muqing closed with dissolve
    "The darkness constricted around her body, snaking up to choke her throat. She could not dematerialize back into spirit form, but she did not let go of her sword."
    "Having disabled Muqing, Xuan Mengdie readied her blade."
    hide muqing
    show mengdie squint sneer with dissolve
    Mengdie "Just like before, you\'re easier to catch with nonlethal traps. Bai Muqing, you..."
    "I couldn\'t let her kill Muqing and charged to intercept the attack while she was still focused on Muqing."
    play sound impact
    "{i}Clang!{/i}"
    show mengdie shout with dissolve
    Mengdie "You, you, you! You\'re really annoying! You insect!"
    Mengdie "Don\'t you know not to interrupt your elders when they\'re speaking!?"
    "In an overwhelming assault, we exchanged a few blows and locked blades."
    "I dug my heels into the ground, marking grooves into it as I was physically pushed back by the force of her blade."
    "The air stiffened."
    "Then she drove a heavy kick into my abdomen."
    "My body flew across the courtyard like a ragdoll."
    "I hit the ground with a thud that forced the air out of my lungs. I tasted blood on my tongue as I gasped."
    "She walked over, forcing me up to my knees."
    show mengdie frown with dissolve
    Mengdie "This body will throw a fit if I kill you right now."
    "She grabbed my face with an iron grip."
    show mengdie smile with dissolve
    Mengdie "I don\'t hate complacent people like you."
    "As her fingers dug into my head, she stomped on my hand that she saw inching toward Fenghuang Sword and lightly pushed the sword just out of reach with her foot."
    show mengdie open grin with dissolve
    Mengdie "Just, ah, don\'t get in the way."
    "Was that supposed to be a smile?"
    "On Bai Fangfei\'s face, she made such an ugly expression that I wanted to cry and turn my eyes away, but I couldn\'t."
    hide mengdie with dissolve
    "As if carving into my skull, her grip only tightened when she channeled demonic energy into my head."
    "It was a spell, a curse."
    "Throbbing pain overwhelmed my mind. As if I was being burned alive, ground to pieces, ripped to pieces, my head hurt, hurt, hurt, hurt, hurt."
    stop music fadeout 3.0
    "My vision warped."
    "It hurt."
    scene black with fade
    "And then came darkness."

    ##
    "..."
    "......"
    play music "<loop 18.701 >/audio/music/Peaceful (Full).ogg"
    #play music Peaceful_Intro
    #queue music Peaceful_Loop
    "...What was I doing?"
    scene CG_butterfly_dream with fade
    "I felt as if I had seen a long and terrible nightmare."
    "My eyes fluttered open. I must have fallen asleep with my head on Master\'s lap. So comfortable was the smell of peaches that I had drifted off to the land of dreams."
    "Her cool hand covered my eyes for a moment. Had I been crying?"
    "Now I could no longer remember the nightmare I must have had, and instead tried to think of what we had been doing before I fell asleep."
    Fangfei "You need not think about it."
    "It must have been nothing."
    "My head laid on Master\'s lap so pleasantly that I did not want to get up, but I knew that I should not bother her too much."
    Lixue "Master, I should get up."
    Fangfei "You can stay here as long as you would like, Lixue."
    Lixue "Mm..."
    show CG_butterfly_dream2 with dissolve
    "She gently pet my head, making me hold back a lazy sigh."
    "It was warm. I wondered if spring had already come without me noticing."
    "I reoriented myself to my surroundings, forcing my sleepy eyes open. The courtyard looked as usual without a single scuff."
    "The tree with no blossoms, no buds, stayed the same as well, its branches bare."
    "This spring, it still had not bloomed."
    Lixue "I wish that it would flower."
    Fangfei "Perhaps one day it will."
    Lixue "......"
    Lixue "If it flowers, will it bear fruit? Ripe and juicy sweet peaches?"
    Fangfei "The most fragrant and delicious peaches."
    Lixue "We could make fruit wine together from the peaches, and when a year passes, we could drink it together."
    Fangfei "Lixue has really matured, thinking of drinking alcohol."
    Lixue "I was simply curious how wine we make together would taste."
    Lixue "Sister Muqing would have liked it."
    Fangfei "Who?"
    hide CG_butterfly_dream2 with dissolve
    "My thoughts skidded to a halt. I should not have mentioned Sister Muqing."
    "Then I paused. Who was Muqing? Although the name left my mouth, for some reason, I could not remember who that person was and what her face looked like."
    "When would I have met such a person?"
    Lixue "I wonder."
    "Juyi Peak was a place for just the two of us."
    Fangfei "Perhaps you met that person in a dream."
    "I could not help but think of a story about a man who dreamed."
    $ renpy.notify("GLOSSARY: Butterfly Dream")
    "The man dreamed that he was a butterfly and did not know that he was a man. When he awoke, he knew he was certainly a man."
    "Yet he did not know if he was a man who had dreamed of being a butterfly or a butterfly who was dreaming of being a man."
    "Even now, the story filled me with a strangeness."
    Lixue "Yes, it must have been a truly mysterious dream."
    Fangfei "Was it a good dream?"
    Lixue "It must have been one with ups and downs, but I cherished it. Although I no longer remember, it must have been a wonderful dream."
    "Something felt missing in the hollow of my heart."
    "However, her warmth quickly filled the gap."
    $ renpy.notify("GLOSSARY: Joy of Fish")
    "The ancients wrote that a man might never be able to understand the joy of a fish. Point as he would, he could only say that a fish {i}may{/i} have obtained human happiness."
    "Right now, I was the fish that one might point to and say was happy, but was my fish heart satisfied?"
    "Simple, peaceful days with Master were more than I could ever hope for."
    "A night and a day passed in a blink of an eye."
    Fangfei "Are you happy right now?"
    Lixue "Undoubtedly, but this must be a dream."
    Fangfei "I see."
    Fangfei "Have a good trip, Lixue."
    Lixue "Yes. Goodbye, Master."
    "The butterfly dream shattered."
    stop music fadeout 3.0

    ##
    scene bg realm with fade
    play music "<loop 25.600>/audio/music/Suspenseful (Full).ogg"
    #play music Suspenseful_Intro
    #queue music Suspenseful_Loop
    "I was falling."
    "Falling for a long time, I landed on the ground as if I had fallen on clouds."
    "I pushed myself up to my feet and glanced around at my surroundings, which did not appear to be any place I knew on Juyi Peak. This was an empty and lonely place."
    "A little bit away, I spotted Master alone. She held a piece of old jade in her hand, wistfully looking at it. The jade was no spiritual jade but a familiar looking accessory."
    "I approached with sluggish steps, pushing aside the dull pain in my head that felt like needles stabbing through my skull."
    show lixue ask with dissolve
    Lixue "Master."
    Lixue "Master?"
    show lixue soft with dissolve
    Lixue "Bai Fangfei."
    "She finally reacted, turning to face me."
    hide lixue
    show fangfei squint stern with dissolve
    Fangfei "You should not be here."
    hide fangfei
    show lixue ask with dissolve
    Lixue "Where are we?"
    hide lixue
    show fangfei open talk with dissolve
    Fangfei "I am the spirit of this peach tree, the yao born from its life."
    Fangfei "Here is the liminal space of this tree that will no longer bloom. You should have never come here. This is the place I was born and the place I will disappear."
    show fangfei frown with dissolve
    Fangfei "This is not a place for you."
    "She gripped the jade."
    hide fangfei
    show lixue retort with dissolve
    Lixue "But you are here. I must have come here for a reason, even if I do not understand what it is."
    hide lixue
    show fangfei closed mention with dissolve
    Fangfei "Your master is me, and I am Bai Fangfei, but we are not the same. I am the fragment of Bai Fangfei that stays awake here to see when all will end."
    show fangfei open convicted with dissolve
    Fangfei "The Ancient Calamity has taken my body."
    show fangfei stern with dissolve
    Fangfei "She will destroy the realm and kill while I can at best only watch."
    show fangfei frown with dissolve
    Fangfei "She and I glanced over each other\'s memories for the slightest moment. I saw but a fragment, and I remembered the past... The time long before I awoke as a yao."
    show fangfei serious with dissolve
    Fangfei "The reason you are here may be to hear the story and harden your convictions, so I will tell you about the past, Lixue."
    hide fangfei
    show lixue diligent with dissolve
    Lixue "The past..."
    hide lixue
    show fangfei calm with dissolve
    Fangfei "I am a peach tree."
    show fangfei serious with dissolve
    Fangfei "I was planted on Juyi Peak a long, long time ago by two people who lived a happy life here ages before we had even been born."
    show fangfei hesitant with dissolve
    Fangfei "I, the tree, would flower and bear fruit, and I must have seen those two smile so many times, so happily as if all was right in the world."
    Fangfei "I, as a tree, had very little needs, and those two, alone in their own world, had little conflicts with the outside world."
    show fangfei mild with dissolve
    Fangfei "Bai Muqing and Xuan Mengdie, they lived in peace."
    show fangfei hesitant with dissolve
    Fangfei "That peace was not fated to last."
    show fangfei burdened with dissolve
    Fangfei "I saw her, Xuan Mengdie, the Ancient Calamity, die under my peach tree covered in grievous wounds."
    show fangfei squint with dissolve
    Fangfei "Her grudges lingered and soaked into my roots."
    show fangfei closed with dissolve
    Fangfei "Soon after, the other half of the pair thrust her treasured blade into her chest, watering my roots with her heart blood."
    show fangfei open with dissolve
    Fangfei "I remember that she was crying, unlike how she and her other half used to smile together under my branches."
    Fangfei "She, Bai Muqing, must have made the world forget about what had happened."
    show fangfei resigned with dissolve
    Fangfei "I was alone on Juyi Peak from then on."
    hide fangfei
    show lixue frown with dissolve
    Lixue "......"
    hide lixue
    show fangfei squint concerned with dissolve
    Fangfei "All alone, I absorbed spiritual energy until I woke up as the person named Bai Fangfei."
    show fangfei hesitant with dissolve
    Fangfei "At some point, I left this place and met the people of Dalin Sect on my journey."
    show fangfei open concerned with dissolve
    Fangfei "But when I divined the path of the Heavenly Way, I returned to my solitude upon Juyi Peak."
    "I knew just how long she was alone before we met, and it was an excruciatingly long time."
    show fangfei squint speak with dissolve
    Fangfei "From the start, I saw that you would cut me down or the world would be bathed in blood."
    show fangfei resigned with dissolve
    Fangfei "I\'m sorry. For my selfish reasons, I picked you up."
    hide fangfei
    show lixue soft with dissolve
    Lixue "You treated me tenderly with love, so I don\'t regret the time we spent together."
    hide lixue
    show fangfei open mention with dissolve
    Fangfei "Cut me down."
    hide fangfei
    show lixue serious with dissolve
    Lixue "That cannot be done."
    hide lixue
    show fangfei frown with dissolve
    Fangfei "You have the ability to make the Ancient Calamity\'s plans crumble to pieces. The only cost is a tree long past its due date."
    show fangfei closed mention with dissolve
    Fangfei "As I am right now, I can do nothing."
    show fangfei squint with dissolve
    Fangfei "The Ancient Calamity and I are already inexplicably tied together."
    show fangfei open burdened with dissolve
    Fangfei "There is no blade in this world that can cut our souls apart, so the only option is to eliminate all that is attached to her."
    show fangfei resigned with dissolve
    Fangfei "Lixue, please fulfill this single request of mine. Please..."
    show fangfei squint with dissolve
    Fangfei "I have nothing left that I can do... so please... do not let me destroy this beautiful world."
    hide fangfei
    show lixue sad with dissolve
    Lixue "Will you allow tragedy to repeat?"
    Lixue "...If you were to die... do you even understand how that makes me feel?"
    show lixue angry with dissolve
    Lixue "If you wanted me to kill you, you should have raised me to hate you."
    hide lixue
    show fangfei open hesitant with dissolve
    Fangfei "...Bai Fangfei loved you."
    show fangfei squint with dissolve
    Fangfei "She felt lucky to have met you. I feel lucky to have met you. If I could, would I not also ask for you and I to live in harmony together forever?"
    show fangfei closed mention with dissolve
    Fangfei "However, the Heavenly Way cannot be averted, so please kill me."
    show fangfei open resigned with dissolve
    Fangfei "We are not fated to be together. The little bit of fate we shared was your blade above my neck, so... if I had to choose you or me, I would always choose you."
    show fangfei squint with dissolve
    Fangfei "Rather than to let me devastate the world, hurt you and everyone else, I would rather you live and let me die."
    hide fangfei
    show lixue sus with dissolve
    Lixue "I am unskilled at divination, but you\'ve drawn much too many conclusions from what you\'ve seen."
    Lixue "Can we truly understand what the Heavenly Way says?"
    show lixue retort with dissolve
    Lixue "I reject your interpretation of the Heavenly Way."
    Lixue "And if your interpretation is correct, then I reject the Heavenly Way itself."
    "I said these words that I had no way to back up."
    hide lixue
    show fangfei open grit with dissolve
    Fangfei "If that is what you say..."
    show fangfei burdened with dissolve
    Fangfei "You must not linger here regardless. Leave this place."
    "Images flooded into my mind, telling me how to exit the liminal space. I felt that I would be ejected soon, so I tried to reach out my hand to her."
    hide fangfei
    show lixue soft with dissolve
    Lixue "Come with me."
    hide lixue
    show fangfei open mild with dissolve
    Fangfei "I cannot."
    "She shook her head."
    show fangfei squint teary with dissolve
    Fangfei "Goodbye, Lixue. This is not a promise to meet again but rather a final farewell."
    stop music fadeout 3.0

    ##
    scene bg courtyard with fade
    play music "<loop 4.796>/audio/music/Action (Full).ogg"
    #play music Action_Intro
    #queue music Action_Loop
    "I gasped, opening my eyes once more in the physical world."
    "The pain in my body told me that I had returned to where I was before Xuan Mengdie\'s curse had sent me spiraling through a dream and the liminal space."
    "Muqing had freed herself from her bindings. She and Xuan Mengdie were locked in a fierce battle."
    play sound impact
    "{i}Clang!{/i}"
    "For a second, their eyes noticed my awakening, but neither deigned to do more, returning their attention back to their fight."
    show mengdie tch with dissolve
    Mengdie "Tch!"
    hide mengdie
    show muqing troubled with dissolve
    Muqing "...!"
    hide muqing
    show mengdie shout with dissolve
    Mengdie "I hate you! I hate you! I hate hate hate hate hate you! Why won\'t you just die and disappear already!?"
    show mengdie squint with dissolve
    Mengdie "Did you have to linger around and bother me even after you died!?"
    hide mengdie
    show muqing declare with dissolve
    Muqing "Because I love you too much. I wanted to accompany you even after death! Because I wasn\'t able to accompany you properly during life!"
    hide muqing
    show mengdie laugh with dissolve
    Mengdie "Kukuhahahahaha! What a joke!"
    show mengdie sneer with dissolve
    Mengdie "Bai Muqing! Bai Wuqing! You don\'t know what affection is!" # Ruby text: Wuqing = heartless
    hide mengdie
    show muqing sad with dissolve
    Muqing "That\'s right. I\'m heartless. I\'m useless. Loathe me and hate me, Mengmeng."
    show muqing declare with dissolve
    Muqing "Just let me explain, please!"
    play sound sword
    scene CG_fight with vpunch
    Mengdie "What is there to explain?"
    play sound impact
    "{i}Shing!{/i}"
    play sound sword
    "{i}Clang!{/i}"
    "Their swords collided."
    show CG_fight2 with vpunch
    Mengdie "You tricked me!"
    Mengdie "That\'s why I\'ll kill you!"
    Mengdie "The feeling of losing your autonomy, of being powerless, violated like a puppet... you don\'t understand it at all! I thought you understood!"
    Mengdie "But you\'re the same as everyone else!"
    Mengdie "I also also also wanted everything to be true!"
    Mengdie "I gave you my heart! I gave up my revenge! I gave you everything! And you fucking stepped all over it!"
    Mengdie "Did you think it was kind of you to give the evil demonic cultivator a little taste of happiness before siccing the orthodox sects on her?"
    Mengdie "Intentionally luring me into a trap in the place I thought was home! And then letting them kill me!"
    Mengdie "It hurt! It hurt hurt hurt hurt hurt hurt hurt!"
    Mengdie "You didn\'t even have the decency to kill me yourself."
    Muqing "I didn\'t send them after you! Those dogs!"
    Muqing "I... I wasn\'t the one... I wouldn\'t do something to hurt you like that, much less let them kill you! Mengmeng, believe in me!"
    Mengdie "Do you think I\'d believe that?"
    Mengdie "Swear! Swear on the Heavenly Way! Swear on your very existence!"
    Muqing "I\'ll swear on anything you want."
    show CG_fight with vpunch
    Mengdie "Then go ahead, Bai Muqing. Say your vows to your beloved heavens, and let me see if they\'ll strike you down or not."
    Muqing "I swear on the Heavenly Way that I took no part in the conspiracy that took your life. If I am lying, then may I be painfully incinerated to a second death."
    Muqing "When you died, my world was empty."
    Muqing "I must have gone mad."
    Muqing "I set the Bai Pavilion onto the path of destruction, cursed the major sects, and removed the memory of us and our Juyi Peak from the world."
    Muqing "I wanted to keep our place for just the two of us intact."
    Muqing "Then I... I suppose I ended my life since I wanted to follow you. I just hadn\'t thought that I would wake up again and meet you again like this."
    Muqing "I swear on the Heavenly Way that I love you, Xuan Mengdie, so will you believe me?"
    stop music fadeout 3.0
    scene bg courtyard with dissolve
    show mengdie neutral with dissolve
    play music "<loop 25.600>/audio/music/Suspenseful (Full).ogg"
    #play music Suspenseful_Intro
    #queue music Suspenseful_Loop
    Mengdie "Shut up."
    "They paused and waited. If Sister Muqing had lied, the Heavenly Way would strike her down. She would burn or be struck by lightning or disintegrate another way, but nothing happened."
    "She had told the truth."
    "Xuan Mengdie lowered her sword, stepping closer to Muqing."
    show mengdie tch with dissolve
    Mengdie "...So they lied to me."
    show mengdie neutral with dissolve
    Mengdie "I should\'ve known. Even if they took your identifying items, I should\'ve never listened to those dogs."
    show mengdie smile with dissolve
    Mengdie "That doesn\'t mean I\'ll stop my revenge. The cultivation world must burn, so Muqing, why don\'t you join me?"
    Mengdie "We can deal with them together. You and me, just like the old days, and when things are done... I suppose we can return here and live out the rest of it together."
    show mengdie squint with dissolve
    Mengdie "Ascension? If you want to, we can try that. With no cultivation realm, there\'s no need to worry about demonic cultivator this, demonic cultivator that."
    hide mengdie
    show muqing sorry with dissolve
    Muqing "I\'m sorry. I can\'t."
    hide muqing
    show mengdie frown with dissolve
    Mengdie "Why?"
    hide mengdie
    show muqing alas with dissolve
    Muqing "I can\'t let you destroy the cultivation realm. Our time is long past. Let the youths live their lives."
    hide muqing
    show mengdie upset with dissolve
    Mengdie "Why?"
    Mengdie "This world has wronged me and you. It\'s filled with dirty, dirty things, so what\'s wrong with destroying it?"
    hide mengdie
    show muqing sorry with dissolve
    Muqing "I don\'t want to dirty our hands any further. I don\'t want for us to be consumed by hatred."
    show muqing hurt with dissolve
    Muqing "What comes after you\'re done?"
    hide muqing
    show mengdie tch with dissolve
    Mengdie "Muqing, I don\'t think you understand. I\'m dead. The heart that beats in this chest isn\'t mine. All I have left is a grudge, so there\'s nothing else I have left to do."
    show mengdie squint upset with dissolve
    Mengdie "It\'s empty here, and I need to fill it up."
    hide mengdie
    show muqing hurt with dissolve
    Muqing "......"
    hide muqing
    show mengdie shout with dissolve
    Mengdie "In the end you still won\'t choose me!"
    stop music fadeout 3.0
    scene CG_death with dissolve
    #play music Sad_Intro
    #queue music Sad_Loop
    play music "<loop 21.745>/audio/music/Sad (Full).ogg"
    "Xuan Mengdie rushed in with her blade wrapped in demonic energy, aiming for Muqing\'s heart."
    "Even though Muqing should have been able to dodge such an attack, she didn\'t."
    Muqing "I\'ll always choose you."
    "The darkness covered sword pierced through her body."
    Mengdie "Muqing, what\'s wrong with you?"
    Muqing "I\'m just not willing to let you burn out. Ghk!"
    Mengdie "If you die now, your soul will never be reincarnated! You\'ll really... be gone forever."
    "Muqing began to shatter, her soul eroding to pieces around the heart. Like a thousand butterflies of light, they dissipated."
    Muqing "I\'m sorry I was never able to protect you and make you happy. No, I\'m sure that my existence was what caused you to veer off your path and suffer so much sadness."
    Muqing "Without me there, you would have been able to reach the peak of the world and ascend with no one ever daring to wrong you again."
    Muqing "This is my final apology."
    Muqing "Mengmeng, I love you, so-"
    "She disappeared before she could say her final words."
    "I never understood Sister Muqing until the end."
    scene bg courtyard with dissolve
    show lixue worry with dissolve
    Lixue "...Sister... Muqing...?"
    "Fenghuang Sword cried in my hand and screamed like a blazing flame, knowing that it would never feel the spirit of its creator ever again."
    hide lixue
    show mengdie squint shout with dissolve
    Mengdie "BAI MUQING!"
    show mengdie upset with dissolve
    Mengdie "You..."
    Mengdie "You... weren\'t supposed to do that..."
    show mengdie distraught with dissolve
    Mengdie "No... no no no no! No! No!"
    show mengdie open with dissolve
    Mengdie "You were supposed to dodge. You were supposed to fight me and take me down... and promise me the future... even if we were already dead."
    show mengdie squint upset with dissolve
    Mengdie "...Why?"
    show mengdie cry with dissolve
    "She dropped Master\'s sword to the ground, falling to her knees as she grabbed at the motes of light left behind."
    show mengdie sob with dissolve
    "For a little while, I watched as Xuan Mengdie cried. No, I averted my eyes, but I could not block my ears."
    "She cried."
    hide mengdie
    show lixue stumble with dissolve
    Lixue "......"
    hide lixue
    show mengdie neutral squint with dissolve
    Mengdie "You."
    show mengdie open with dissolve
    Mengdie "Lixue."
    show mengdie frown with dissolve
    Mengdie "How honorable of you to not attack me when I\'m down."
    hide mengdie
    show lixue scowl with dissolve
    Lixue "Sister Muqing loved you."
    hide lixue
    show mengdie frown with dissolve
    Mengdie "......"
    "She didn\'t pick up the sword but instead glared at me as if upset that I dared to say Muqing\'s name."
    show mengdie mild with dissolve
    Mengdie "I\'ll be honest. I\'m not in the mood to fight right now."
    show mengdie squint with dissolve
    Mengdie "You have two choices: kill this body and kill me now or let me consume her and destroy the cultivation realm."
    Mengdie "This is my kindness to you."
    show mengdie smile with dissolve
    Mengdie "I\'m not like Muqing, so I\'ll just let you choose."
    show mengdie sneer with dissolve
    Mengdie "But you don\'t have that much time, so hurry up and decide. Let me see if at least one pair of people can be happy here or if we\'d all been cursed from the start."
    "I knew that if I fought Xuan Mengdie one on one, I would lose, and somehow, I also knew that she was telling the truth when she allowed me to choose an option."
    hide mengdie
    show lixue angry with dissolve
    Lixue "I really don\'t understand you."
    show lixue sus with dissolve
    Lixue "I don\'t understand you or Sister Muqing."
    "I readied Fenghuang Sword."
    hide lixue
    show mengdie open mild with dissolve
    Mengdie "So you\'ll kill me and your master to prevent the destruction of the realm, huh?"
    "We were not having a conversation, not in the truest sense of communication, but rather just saying words to the air."
    "My hands trembled even as Fenghuang Sword emitted a reassuring warmth."
    show mengdie squint pleasant with dissolve
    Mengdie "That sword, Fenghuang Sword, not a terrible blade to die again under."
    "What could I do? What would I do?"
    hide mengdie
    show lixue soft with dissolve
    Lixue "Both of those options are terrible options."
    show lixue relaxed with dissolve
    "Steadying my breaths, I circulated the spiritual energy in my core and called upon my Spirit Forging Flames to make my blade impossibly sharp."
    hide lixue
    show mengdie squint smile with dissolve
    Mengdie "Go ahead. Cut me down."
    "No, that was wrong. What I wanted to make sharp was not just the blade but my very soul."
    "Thus, I set my soul aflame and sharpened it, channeling it into Fenghuang Sword. Even though it hurt, I became the sword and the sword became me."
    "My eyes saw where Master—Bai Fangfei and Xuan Mengdie\'s souls had melded together."
    "Too mixed to cut, perhaps a normal person would say."
    "I was long beyond the point of giving up. If a happy ending was impossible, then I simply had to make a miracle happen."
    "So I cut; I cut the very concept of the connection between their souls."
    "The cry of a fenghuang whistled through the air."
    "As if it had finished its last task, Fenghuang Sword shattered."
    show mengdie mild with dissolve
    Mengdie "Bai Muqing, you goddamn cheater."
    "Xuan Mengdie and Bai Fangfei\'s souls broke away from each other."
    "Free of a physical body, Xuan Mengdie\'s soul appeared before me as she gradually broke into little pieces and faded, unable to sustain herself in the living world any further."
    show mengdie open mild with dissolve
    Mengdie "...I won\'t be reincarnating anyway, not with this broken soul, so I guess... I\'ll see you later, Muqing."
    "I saw as Xuan Mengdie disappeared into tiny bits of light that were just as beautiful as Sister Muqing\'s soul."
    hide mengdie with dissolve
    "I wondered if she was happy."
    "Feeling the backlash of spiritual energy coursing through my body, I dropped to the ground and vomited blood."
    Lixue "I see. This must have been what she saw in the Heavenly Way."
    "I could barely stand, so I crawled over to Master, and I saw her spirit rise from her body as if she was making to leave."
    "She was trying to go just like the other two."
    Lixue "You can\'t go. Not when I didn\'t cut you down. Not when you\'re still alive."
    Lixue "A future without you is unacceptable."
    "She made a blank expression as if she didn\'t know anything, as if her soul had been wiped blank, corrupted by the demonic grandmaster\'s soul for much too long."
    "I could not accept that."
    scene CG_finale with dissolve
    Lixue "I love you."
    "I wanted her to remember all the times we had together. At the very least, I wanted her to live."
    Lixue "I love you more than anyone else in the world, and I want to spend the rest of my days with you."
    Fangfei "Lixue...?"
    Lixue "I want to call your name and stay by your side."
    Lixue "So please, don\'t go."
    "After I spoke, I coughed up another mouthful of blood."
    "She seemed to hold her head in discomfort, a light returning to her eyes, and her soul returned to her body."
    "I waited, seeing her chest move up and down as she breathed once more."
    "Slowly, her eyes fluttered open."
    "She took my hand"
    Fangfei "I\'m happy."
    "While her voice was still weak, I heard her words loud and clear."
    Fangfei "I think I should be allowed to say this to you now, Lixue."
    Fangfei "Yes, I love you too."
    stop music fadeout 3.0
    "Bai Fangfei smiled beautifully."

    # EPILOGUE
    scene bg spring_courtyard with fade
    play music "<loop 18.701 >/audio/music/Peaceful (Full).ogg"
    #play music Peaceful_Intro
    #queue music Peaceful_Loop
    "The two of us stayed bedridden for a long time."
    "I tasted her congee for the first time in years, and just like before, it was delicious, so pleasant and warm in my stomach."
    "The medicine I had to drink tasted bitter, but her kisses were sweeter than any candy given to soften the unpleasant taste."
    "Before we knew it, spring arrived."
    show lixue open_blush speak with dissolve
    Lixue "...The tree... flowered."
    hide lixue
    show fangfei open_blush surprised with dissolve
    Fangfei "Yes. I never thought that I would see the day."
    hide fangfei
    show lixue open_blush hope with dissolve
    Lixue "Fangfei..."
    "I was still a little flustered saying her name."
    show lixue closed_blush relief with dissolve
    Lixue "Her flowers are beautiful."
    "Surely she would bloom next year and the year after for as long as we were here."
    hide lixue
    show fangfei open_blush smile with dissolve
    Fangfei "If she bears fruit, we can eat the peaches in summer."
    hide fangfei
    show lixue open_blush talk with dissolve
    Lixue "In autumn, perhaps we can make some fruit wine."
    hide lixue
    show fangfei closed_blush smile with dissolve
    Fangfei "Then in winter, the wine should be ready."
    "Talking of fruit wine reminded me of Sister Muqing and Xuan Mengdie. The two had passed, but their existences had left a deep impression on both of us."
    "Rather than to say it was a scar, it was more like a precious memory of the past."
    hide fangfei
    show lixue open_blush bashful with dissolve
    Lixue "Do you think we could save a jar for them?"
    "Although I did not say their names, she knew who I was talking about."
    hide lixue
    show fangfei squint_blush mild with dissolve
    Fangfei "Yes."
    "Making such mundane conversation, I was satisfied. My body still hurt, but my heart was filled with warmth."
    "These flowers were celebratory flowers, flowers that would congratulate us each year."
    "I, who loved her, was also loved."
    "When I opened my eyes, I saw her before me."
    "Once upon a time, I never could have imagined the feelings overflowing from my heart, yet this was not a dream but our reality, and we would continue onward together."
    "From that moment on, I must have been happy."

    $ credits_speed = 15
    scene pink with dissolve
    show credits at Move((0.5, 1.0), (0.5, -1.0), credits_speed,
                  xanchor=0.5, yanchor=0)

    pause credits_speed
    stop music fadeout 3.0
    pause 1


    $ persistent.complete = True

    return
