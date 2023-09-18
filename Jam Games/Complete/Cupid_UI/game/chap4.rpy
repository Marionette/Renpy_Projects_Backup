
label chap4:
    scene bg black 
    stop music fadeout 2.0
    $persistent.Chapter4Unlocked = True   
    $save_name = "chap4: metamorphoses"
    
    scene bg chap04 with slowdissolve
    with Pause(2)
    scene bg black with fade
    play sound "sfx/matchflare.ogg"
    scene bg candle1 with slowdissolve
    
    nvl clear
    o "The second candle is lit."
    nvl clear
    o "Its name is Philia."
    o "The love for friends."
    "The yellow candle shone and danced with her breath."
    nvl clear
    o "Let this candle burn until its wick is spent."
    o "Encourage friendship. Bring forth memories."
    nvl clear
    o "Let me walk in his halls without any suspicion."
    o "Let me rummage through his belongings invisibly."
    nvl clear
    o "His journal."
    nvl clear
    o "He guards his journal fiercely."
    nvl clear
    o "I must find it."
    nvl clear
    scene bg black 
    stop sound fadeout 4.0
    $ renpy.pause(delay=None)

    play music "sfx/theatrechatter.ogg" fadein 2.0
    show bg theatre 
    show rf annoyed 
    "Rosa adjusted her coat as she sat on one of the reserved seats."
    show rf huh 
    "The theatre was packed. The air buzzed with excitement."
    "She hadn't expected this many people would come tonight."

    show rf sad 
    r "Oh, Mother. I wish they would stop staring at me."
    "And why not? This was Mdm. Catherine Perride's first solo concierto."
    "Her name had been slowly gathering recognition the past few years. It was feasible to expect a full house."
    "Still, the turn-out was more than they had expected."
    "Paris had taken Rosa and Catherine by surprise."
    "The sheer number of people and their liveliness were well above the usual sights of their small town."
    "Catherine was obviously thrilled with the opportunity to play in such an esteemed venue for her debut."
    "Rosa tried her best to keep her anxiety under control."
    show rf huh 
    "This was for Catherine."
    show rf think 
    "Yes, for her."

    "This was her night."
    "Rosa took a deep breath and released it slowly."
    show rf smile 
    "It relaxed her."
    r "I hope the show starts soon."
    show rf normal 
    "Rosa's eye drifted towards the stage and then to the throng of people gathered on her far left."
    show rf huh 
    "In the middle of the huddle stood a familiar shape of a man."
    "He had his back to her, but the posture and the build were unmistakable."
    show rf shockblush 
    r "T-That is Guilleme."
    show rf happy 
    "Her heart made a sudden, gleeful jump."
    "She was delighted that he had made it to Catherine's show."
    "He had been travelling extensively recently."
    "What if she walked over and made sure?"
    "Guilleme would greet her kindly."
    "She was sure Catherine would be thrilled to know he was here--"
    show rf huh 
    "..."
    show rf hmp 
    "Rosa pondered for a bit, reminded of a sudden wince of pain."
    show rf dep 
    r "..."
    show rf normal 
    "Soon, the Master of Ceremonies obliged people to take their seats."
    show rf huh 
    "Guilleme turned around and walked towards her."
    "He stopped midway and took a seat without noticing her presence."
    show rf dep 
    "Rosa seemed deep in thought."
    m "What's wrong, sweetheart? Is something bothering you?"
    r "N-Nothing, Mother..."
    m "Don't lie to me."
    r "..."
    r "...I just didn't expect to see him here, that's all."
    m "Oh, I see."
    m "It is the same problem, isn't it?"
    show rf dep 
    call gorc from _call_gorc
    r "..."
    m "Oh, you are making your life so complicated, darling!"
    m "Why do you even bother yourself with these people?"
    show rf dep 
    call theatre2 from _call_theatre2
    show rf sad 
    r "It's not like that, Mother."
    r "We're friends."
    m "{i}Friends?{/i}"
    m "Darling, friendship is nothing but a shallow kind of relationship."
    m "People change friends as easily as the weather."
    m "You don't even remember the friends you make at a certain age."
    call theatre3 from _call_theatre3
    m "But soon, they will abandon you, too."
    show rf hmp 
    "Rosa's tongue felt bitter in her mouth."
    "She was filled with annoyance for her Mother."
    "Wasn’t happiness as fleeting as friendship? Yet it was not any less real than sadness."
    if family:
        "Yes, family was important."
        "These familial bonds kept her from losing herself."
        "It was her rock, her foundation."
        show rf dep
        "But were these bonds the only constant value?"
    "These friends..."
    "These were people who accepted her."
    "They shared laughter and tears, their own regrets and dreams."
    if family:
        "In her heart, she had found a home with them."
    show rf hmp
    "What more was needed?"
    "Rosa's confused feelings began to arrange themselves neatly in her mind."
    show rf think 
    "Guilleme and Catherine's happiness was important to her. That was the main thing."
    "She knew they felt the same way for her."
    "Her insecurities were real, but they were insignificant. If anything, they were bittersweet."
    "She had no regrets."
    show rf hmp 
    "For the first time in her life, she wanted to talk back to Mother."
    show rf dep 
    "She bit her lip, quelling the nerves as she opened her mouth to speak."
    r "I-I know that."
    m "What?"
    if rosajealous:
        show rf think 
        r "I know that Catherine matters more to him than I do."
    r "I know they might abandon me one day for whatever reason."
    show rf think
    r "It might be today or next year."
    r "Or even sooner."
    r "But that doesn't matter in the long run."
    r "I am happy with them."
    r "We've had years together that I will treasure."
    show rf smile 
    r "Like I treasure memories of you too, Mother."
    r "My memories of you keep me sustained."
    r "That is why I love you."
    r "The years we spent together, no matter how fleeting, are still worth something."
    r "So let me care for them right now."
    show rf think 
    "{i}Everything changes, but nothing is lost.{/i}"
    "Rosa was sure she had read it somewhere."
    show rf hmp 
    "Rosa waited for Mother to answer with a vicious voice, to burst out screaming at her cheekiness."
    show rf huh 
    "But no voice came."
    show rf smile 
    "Rosa smiled to herself."
    hide rf smile 
    stop music fadeout 2.0
    "The lights dimmed."
    "A low hush descended on the pews."
    play sound "sfx/theatreapplause.ogg"
    "Soon, Catherine entered, clad in the loveliest gown and an even lovelier smile."
    "She was beautiful. She belonged on the stage."
    "The lights shone on her, but they paled in comparison to her radiance."
    "Catherine bowed to the audience and took a seat in front of the piano."
    stop sound fadeout 2.0
    "She began to play."
    play music "sfx/catsaria.ogg"
    $ renpy.pause(delay=None, music=True)
    "Rosa gripped the handle of her seat."
    "She felt surges of emotion with every note."
    "A kind of energy passed through her, touching her skin and making her break into goosebumps."
    "Oh, Catherine!"
    "Rosa hadn’t known of such an effect before this moment."
    "Music that could so strike the heart as if it was fiddling with the soul."
    "It was different from practice, different from when she was performing in front of smaller groups."
    "This was a stage, and here was a woman with strings."
    "She was tugging the rights keys, touching your heart and electrifying your soul."
    "Rosa realised she wasn't alone in this feeling."
    "The whole room was mesmerized."
    "She looked at the lady beside her seat. She had her hand to her open mouth."
    "A teardrop dangled precariously on her eye."
    "The man to her left seemed to have forgotten to blink."
    "Rosa beamed and savoured a rush of kinship with them."
    "They were experiencing the same emotions with her."
    "It made her love them just a little bit."
    "Rosa closed her eyes and savored the night."
    $renpy.pause(delay=None)
    nvl clear
    o "A bead of sweat fell from Catherine’s chin."
    o "She was out of her body now."
    o "Her stress from the beginning of the show had thawed and turned into passion."
    o "It ran down her fingers to the keys."
    nvl clear
    o "It did not escape Catherine’s notice that most people in the crowd came to the show to gawk at her."
    nvl clear
    o "{i}Catherine Perride, the one that the infamous Marquis de Gul had been courting for years?{/i}"
    nvl clear    
    o "{i}Didn't he pay for this event? Lucky broad.{/i}"
    nvl clear
    o "{i}Catherine Perride, I heard she was some pianist.{/i}"
    nvl clear
    o "{i}Any good?{/i}"
    o "{i}Who knows? Must be.{/i}"
    nvl clear
    o "Catherine Perride."
    nvl clear
    o "{i}Some female pianist.{/i}"
    nvl clear
    o "{i}Pretty face, nice flesh on her.{/i}"
    nvl clear
    o "{i}Let us watch her show.{/i}"
    nvl clear
    o "Her fingers caressed the keys, playing them with the force of her heart."
    nvl clear
    o "Did she play to prove them wrong?"
    nvl clear
    o "Her music saturated the theatre with her fervor."
    nvl clear
    o "No, not to prove them wrong."
    nvl clear
    o "To set it right."
    nvl clear
    o "{i}Catherine Perride is my name.{/i}"
    o "{i}I am more than just a pretty face.{/i}"
    o "{i}And I am playing this piece for you.{/i}"
    o "{i}It is my gift.{/i}"
    nvl clear
    o "{i}Let me touch your soul.{/i}"
    $renpy.pause(delay=None)
    
    "Rosa felt her eye get moist."
    "This was Catherine's heart transcribed into music."
    "All energy and beauty with the strength of the wind."
    "The mischief of a sudden gale that whips at ladies' skirts and tips gentlemen's hats."
    "The cold breeze that carried the loneliness of the coming winter."
    "Everyone in the audience felt it."
    "Rosa searched for Guilleme's face in the darkness."
    "She couldn't see him clearly."
    "But it didn't matter. She knew what he was feeling."
    "She felt it, too."
    "Rosa's heart began to ache."
    "It was a sting she didn't know how to name."
    scene bg black
    $renpy.pause(delay=None)
    stop music fadeout 2.0
    "After the show, Rosa greeted Catherine in her backstage dressing room."
    scene bg dressingroomopen
    show rf smile at nearleft 
    show cn normal 
    play music "sfx/theatrechatter.ogg" fadein 2.0
    "She was smothered in flowers from the audience. Sweat glistened on her forehead."
    show cn smile 
    "Catherine gave her a tight hug."
    show rf happy at nearleft 
    r "Congratulations, Cath!"
    r "You were marvelous onstage."
    show cn happy 
    c "Thank you, Rosie!"
    show rf smile at nearleft 
    "Catherine covered her cheeks with her hands."
    show cn smile 
    c "I'm still shaking! The excitement from the stage hasn’t left."
    show cn happy 
    c "Look at my hands!"
    show cn smile 
    show rf happy at nearleft 
    r "Haha! Oh dear!"
    show rf smile at nearleft 
    r "So I would call this show a success, yes?"
    show cn mischief 
    c "Pour the champagne, {i}chérie!{/i} It is a night to remember!"
    show rf happy at nearleft 
    "Catherine and Rosa hugged again."
    show cn normal 
    show rf smile at nearleft 
    c "Let me just finish up here, Rosa!"
    show cn happy 
    c "Then we'll celebrate properly!"
    show cn seethe
    c "Two young, ravishing ladies sampling the best of what Paris has to offer."
    show cn taunt
    c "I like it!"
    show rf happy at nearleft
    show cn evilsmile 
    "Rosa laughed."
    show rf huh at nearleft 
    show cn mischief
    r "Just don't let go of my hand. You might get lost being so starry-eyed."
    show rf happy at nearleft 
    "She was teasing, but smiling brightly all the same."
    show cn evilsmile

    c "I would never!"
    show cn normal
    show rf smile at nearleft  
    c "Anyway, shall I meet you outside in a few minutes?"
    show rf huh at nearleft 
    r "Very well. I'll see you later!"
    show rf smile at nearleft 
    hide rf smile 
    hide cn normal     
    "Rosa was thankful to leave the backstage area."
    "She had almost forgotten her anxiety during the show, but the backstage was an ill reminder of the crowd."
    "She looked forward to the night ahead, wondering vaguely why she hadn't mentioned Guilleme's presence to Cath."
    "She shrugged it off."
    "It had simply slipped her mind, that was all."
    $renpy.pause(delay=None)
    show cn normal at left 
    "Catherine went back to her dressing room, humming as she was about to grab her coat."
    "She wasn't the least bit tired."
    "Visions of the city, exploring new sights and gaining experiences made her giddy with excitement."
    "It will end the night on the best note, she was sure."
    play sound "sfx/knock.ogg"
    show cn smile at left 
    "A small knock interrupted her thoughts."
    c "Who's there?"
    "Catherine turned around and the cheerful smile froze on her face."
    show cn huh at left 
    show gn smile at right 
    "The Marquis peeked from the open door and stepped inside."
    $renpy.music.set_volume(0.3, delay=2.0)

    g "Hello, Cath."
    show cn sad at left 
    c "..."
    "A tingling passed through Catherine's neck."
    "Although she was aware he had returned, this was the first time she'd seen him in two years--"
    show cn annoyed at left 
    "--After she rebuked his intentions of wooing her."
    "Catherine shook her head at the memory."
    "They grew up together."
    "It was normal to develop feelings for someone you shared most of your life with, was it not?"
    "Yet Catherine had promised herself not to dabble with the Marquis."
    "With all the rumors and the past flings--"
    "She knew too much."
    "{i}Too close. Too complicated{/i}, she had reasoned."    
    "The rumors were still alive in some circles."
    show cn dep at left
    "But hadn't Guilleme come clean with his romantic escapades?"
    "Hadn't he vowed to be faithful since he had made his intentions clear?"
    "{i}Who to believe--?{/i}"
    "{i}Perhaps it was possible that--{/i}"
    show cn seethe at left 
    "Catherine pushed away the insinuation of that last thought and rearranged her face into a merry smile."
    "She curtsied."
    show gn huh at right 
    show cn taunt at left
    c "My Lord, Marquis! Thank you for coming!"
    show cn annoyed at left
    "That last bit came out too loud in her ears."
    show gn talk at right
    "It felt like her voice was compensating. She suppressed a groan."
    show cn seethe at left 
    c "I hope you found the show satisfactory?"
    show gn huh at right 
    g "{i}\"My lord, Marquis\"{/i}?"
    show cn huh at left 
    show gn smile at right
    g "What happened to \"Gilly Monster\"?"
    show cn sad at left 
    "At once, the memories flooded her mind."
    "That used to be her greeting every time she had visited him back then."
    "She would scream that when she saw him, right before she flung her arms around his neck."
    "Catherine didn't know what to do. Suddenly her hands--"
    "--the hands that had never betrayed her felt like they belonged to someone else."
    show cn seethe at left 
    "She cleared her throat and felt the smile harden on her face."
    show gn talk at right 
    show cn taunt at left
    c "Pardon my past slights, Sire. I was a bit of a precocious child."
    show gn bitchface at right 
    c "After all, I must give my due respects to the sponsor of this event."
    show cn seethe at left
    c "Thank you, by the way. It didn't have to be so extravagant."
    show gn huh at right
    show cn sad at left
    g "Wasn't it your dream to play in Paris, Cath?"
    g "I thought your debut would be the perfect opportunity to fulfill that dream."
    play sound "sfx/softdoorclose.ogg"
    show bg dressingroom
    stop music fadeout 2.0
    show gn normal at right
    "The Marquis stepped into her quarters and closed the door."
    show cn uncomfortable at left 
    "Catherine flinched, afraid that the small room would draw them even closer." 
    c "{i}Just the effect that he wanted, probably. The sly fox.{/i}"
    show cn sad at left 
    "She floundered for a bit, and contented herself in fussing with the flowers on the table."
    "She should chase him out. Why wasn't she chasing him out?"
    c "{i}Damn it, Catherine!{/i}"
    c "I-I didn't think you'd be attending tonight, Sire."
    c "Weren't you travelling?"
    show gn huh at right 
    g "Yes, I was."
    show gn smile at right 
    g "But I wouldn't miss your concierto for the whole of France."

    "Guilleme stepped forward."
    show gn blank 
    g "And it seems..."
    g "My investments were well placed."
    show gn blank :
        xalign 0.4
    show cn angryblush at left :
        xalign 0.1
    "Guilleme drew closer to Catherine, so near that she could smell the mint in his breath."
    "He appeared to reached out to her face."
    "...But changed direction at the last minute."
    show gn huh :
        xalign 0.4
    g "O-Oh, these flowers are from the Duke."
    show gn happy :
        xalign 0.4
    g "How pretty."
    "He examined the card dangling a hair away from Catherine's ear, trying to look fascinated by the piece of decorative paper."
    show gn shy at right 
    "Then he stepped back, grinning like an idiot. A tinge of red colored his cheeks."
    g "Err... He really has great taste."
    show cn annoyed at left 
    c "..."
    c "{i}Wherever did you learn{/i} that, {i}you dork?{/i}"
    "If he thought that kind of ploy would make her swoon, then he was dead wrong."
    "In fact, all it made her want to do was wipe that stupid grin off his face."
    "...With the backside of the vase."
    show cn seethe at left 
    show gn smile at right
    c "Yes, he does. Doesn't he?"
    "She gritted her teeth, unable to take the acidic edge off her voice."
    "It wouldn't be so hard."
    "All she had to do was grab the neck of the expensive vase and fling it at his head."
    "She wasn't sure if the vase would break."
    "Maybe not."
    "Maybe she would need to hit him again for the full effect."
    show gn huh at right 

    g "...Catherine, did you hear what I just said?"
    show cn huh at left 
    c "...Huh?"
    show gn smile at right 
    g "I said, now that I'm back in town, would you consider playing for me again?"
    g "It was part of our original arrangement, after all."
    show cn seethe at left 
    "She felt the tendons in her neck tighten."
    show cn taunt at left 
    c "I have a full schedule this week, Sire. But I'll let you know when I'm free."
    show gn huh at right 
    show cn seethe at left 
    g "..."
    show gn sad at right 
    g "Oh..."
    show cn happy at left 
    c "Sire, I must retire for the night."
    show cn seethe at left 
    c "I am exhausted from my performance, after all. Excuse me!"
    "Catherine turned around and went for her coat, but she felt Guilleme grab her hand."
    show gn huh at nearright
    g "W-Wait. Uhm."
    g "I..."
    show gn depblush at nearright 
    g "..."
    show cn annoyed at left 
    c "..."
    "They stared at each other for a couple of seconds."
    "Guilleme looked like he was about to say something."
    "His mouth opened and closed as if debating the correct words in his head."
    "But he just dropped Catherine's hand a moment later."
    g "..."
    show gn depblush at right 
    g "I'm sorry, you're right. You must be tired."
    show cn sad at left 
    "His shoulders dropped."
    show cn annoyed at left
    "Catherine felt a tinge of disappointment, but she ignored it quickly."
    "Guilleme let out a sigh."
    show gn sad at right 
    g "You know I am not good at this, Catherine."
    show cn seethe at left 
    c "Oh, what do I know?"
    show cn annoyed at left 
    c "You seem to do just fine."
    c "You have an {i}amazing{/i} track record."
    show gn huh at right 
    g "Huh...?"
    "Catherine folded her arms over her chest with a pout."
    c "..."
    g "Oh... That?"
    show gn sad at right
    g "...That is just because of my face."
    show cn what at left 
    c "What?"
    show gn bitchface at right 
    g "Most people think I am very deep and thoughtful when I stare at them like this."
    show gn blank at right 
    g "..."
    g "......."
    show gn huh at right
    g "I just run with it."
    show cn angryblush at left
    c "..."
    "Catherine bit her lip to prevent the chuckle from escaping."

    show cn mischief at left
    "But the laughter burst out from her."
    "Before she could stop herself, a mischievous smile appeared on her lips."
    show cn taunt at left
    show gn bitchface at right
    c "No, no! Actually, it is your inability to make big gestures, Gilly."
    show gn huh at right 
    g "Huh?"
    c "Well, look at you!"
    show gn blank at right
    show cn annoyed at left:
        xalign 0.14
    "She copied his tight, alert posture."
    show cn taunt at left

    c "You stand stiff as a board!"
    show cn mischief at left
    c "I guess it fools people into believing you are a graceful, dashing soul."
    show gn unsure at right
    "Guilleme made a pout."
    g "B-But I am dashing, though."
    #show gn sad at right
    #g "...Maybe."
    show cn seethe at left
    c "{i}Au contraire, messire!{/i}"
    show cn evilsmile at left
    c "I {i}did{/i} have the misfortune of being victim to your dancing."
    g "..."
    show gn sad at right
    show cn mischief at left
    g "Must you always bring that up? It was a long time ago."
    show cn uncomfortable at left 
    "He looked so distressed that Catherine couldn't help but tease him further."
    show cn taunt at left
    c "I mourned the death of my little toe, Sire. It was a traumatic experience."
    show cn mischief at left
    show gn amused at right
    "Before long they were laughing, like it was the most natural thing in the world."
    show cn sadsmile at left
    show gn happy at right
    "When did it change? Hadn't it always been like this?"
    show cn sad at left
    show gn smile at right
    "Catherine settled back into her own skin, mulling the confusion in her veins."
    show cn dep at left
    g "Cath..."
    show cn aww at left
    "She looked up at him. Her own emotions stung her."
    g "You can't keep running away from me."
    show cn dep at left
    c "..."
    show cn annoyed at left
    "She sighed deeply."
    "Her hands tightened around her resolve, for lack of a solid thing to hold on to."
    c "Perhaps not, but I have already given you an answer."
    show gn serious at right
    g "..."
    show gn sad at right
    g "I am aware."
    show cn sad at left
    c "..."
    show gn think at right
    g "I have tried to accept it."
    show gn huh at right
    g "Please don't take offense, but I thought it would be easy."
    show gn wistful at right
    g "I left to clear my head, to fill my mind with other things."
    show gn think at right
    g "Travelling usually does the trick."
    g "For a while, at least, I thought I was successful."
    show gn sad at right
    g "But even during my trip, I would catch myself thinking such absurd things like,"
    show gn huh at right
    g "{i}'I wonder what Cath will say when she sees that--'{/i}"
    g "{i}'No, I don't think Catherine will like this too much--'{/i}"
    g "{i}'Hm. Well, Cath used to say--'{/i}"
    show gn think at right
    g "..."
    show gn wistful at right
    g "It was funny, but also a little infuriating to know that you have never left my mind."
    #g "The distance did nothing but made me miss you more."
    show gn dep at right
    g "So I wish I knew how to do this."
    g "I am..."
    show gn think at right
    "He sighed."
    show gn serious at right    
    g "I am too used to people leaving me, that I do not know how to quit on my own."
    show cn sad at left
    c "..."
    show gn wistful at right
    show cn dep at left
    g "It must bother you, the amount of lovers I had in the past."
    g "I am sorry for that."
    g "I almost wish I really was that adept."
    g "But like I have told you, most are simply rumors."
    show gn huh at right
    show cn sad at left
    c "..."
    show cn aww at left
    g "The rest were people realising I am not as interesting as they initially thought."
    show cn sad at left
    show gn wistful at right
    c "Guilleme..."
    g "They never stay long, Cath."
    g "One could say I am {i}amazing{/i} with first impressions."
    g "There is a nagging feeling that that's all I am ever good for."
    g "A sort of exotic trophy people like to collect for its sake, and then put aside when its novelty expires."
    show cn aww at left
    g "I can't blame them."
    g "By now, I am quite sure that I am what is {i}\"wrong\"{/i}."
    show cn sad at left
    c "..."
    g "I must be better at letting people go." 
    show gn huh at right
    g "But you..."
    
    show gn sad at right
    g "Please don't make me let go."
    show cn awwblush at left
    play music "sfx/sweetune2.ogg"

    g "You see through me, Cath."
    g "In your eyes, I feel like I am somebody worth loving."
    show cn sadblush at left
    g "Is it any wonder I'd like to continue thinking of you fondly?"
    show gn huh at right
    g "Old habits die hard, I suppose."
    show gn think at right
    show cn awwblush at left
    #g "Maybe if I uproot my heart and implant a new set of feelings."
    #show gn wistful at right
    #g "Maybe then..."
    #show gn huh at right
    show gn wistful at right
    #g "Even so, I doubt that I can scrub your image completely off my mind."
    show cn annoyed at left
    "Catherine bit her lip."
    show cn seethe at left
    c "Those are impressive words, Sire, but do you have a point?"
    show gn huh at right 
    g "My point?"
    g "Err..."
    show gn sad at right 
    g "It's simple, really."

    g "I--"
    show gn shy at right
    g "I don't think I'll be able to stop my feelings for you."
    show cn awwblush at left
    c "..."
    show cn sadblush at left
    g "You may reject me as many times as you wish."
    g "It will not change."
    g "I have already come to the conclusion that I don't mind."
    g "U-Until you find somebody else worthy, I will always be here."
    show gn serious at right
    "He shrugged."
    show gn bitchface at right
    show cn sad at left
    g "So, I propose that you either get used to me chasing you,"
    show gn smirk at right
    show cn seethe at left
    g "Or you give in to my dashing, toe-mashing charms."
    show cn mischief at left
    "Catherine chuckled despite herself."
    show cn taunt at left
    c "Or I could just kill you with the Duke's fashionable vase."
    show gn huh at right
    show cn seethe at left
    g "Please do not give my superior the pleasure."
    show gn blank at right
    g "I would rather you rip my heart out of my chest and offer it as a dark sacrifice to the gods."
    show gn amused at right
    show cn taunt at left
    c "Gory!"
    show cn seethe at left
    show gn smirk at right
    c "Very poetic. Dashing points for you."
    show gn huh at right
    g "You think so?"
    show cn what at left
    show gn amused at right
    g "I've been reading a lot of romance novels lately."
    show cn mischief at left
    c "What kind of romance novels are you even talking about?!"
    show cn evilsmile at left
    show gn smirk at right
    g "I must learn to be more suave to make the lady of my dreams swoon."
    g "Is it working?"
    show cn mischief at left
    "Catherine laughed."
    show cn evilsmile at left
    c "Hardly."
    show gn amused at right
    g "I believe this is how they do it in the big finale."
    show cn embrblush at left 
    show gn serious
    "Guilleme cleared his throat and knelt down on one knee."

    scene bg gchappy
    #show cn mischief at left
    "He took Catherine's hand awkwardly, trying to act as natural as he could."
    "His serious face made Catherine burst out laughing."
    c "What in the world are you doing, idiot?!"
    #show gn amused
    g "Stop laughing, Madame! I must try this at least once."
    c "I'm simply concerned for an older gentleman and his knee."
    c "Will you be able to stand up from that position later, given your obvious grace?"
    g "Terrible! Dare you call me an old man. I don't look my age, you know?"
    c "Sure, sure!"
    g "Oh, stop laughing, will you? I am trying to concentrate."
    "He cleared his throat again."
    #show gn smile
    g "Will Mademoiselle Catherine Perride allow me an audience tonight?"
    g "As such, perhaps she might allow me to stay by her side for a while longer?"
    #show cn uncomfortable at left 
    g "It would make me a very happy man."
    #show cn mischief at left
    #show gn happy
    "It was sappy and ridiculous, and yet hearing the words did stir Catherine's heart."
    #show gn amused
    "They were giggling like fools now, like children, her heart heavy with love for him."
    #show cn awwblush at left

    "{i}Love?{/i}"
    #show cn sadblush at left
    #show gn smile
    "{i}Did she just think love?{/i}"
    #show cn wistful at left
    "Of course she did."
    "She had always loved him."
    #show cn awwblush at left 
    "Why was she fighting her feelings again?"
    "The reasons seemed unclear all of a sudden."
    scene bg dressingroom
    show cn uncomfortable at left 
    show gn smile
    c "Alright, Sire, your gallantry has convinced this lady to accept your offer for tonight."
    "She bowed with an exaggerated curtsy."
    show gn amused
    "Guilleme took her hand theatrically as he stood up."
    show gn smirk
    show cn mischief at left
    g "This gentleman is relieved he didn't have to sing."
    show gn smile
    show cn evilsmile at left
    c "A few rules for tonight!"
    show cn seethe at left
    c "As we are in Paris, you must be on your best behaviour."
    show gn amused 
    show cn taunt at left
    c "No embarrassing jokes like making friends with the street mimes."
    show cn mischief at left
    show gn smirk
    g "Agreed."
    show cn seethe at left
    c "As such, I must retire by eight."
    show gn bitchface
    g "Ten."
    show cn angryblush at left 
    c "{i}Eight.{/i}"
    show gn serious
    g "Nine-Thirty."
    show cn uncomfortable at left 
    c "Nine. Take it or leave it."
    show cn sadsmile at left 
    show gn sad
    "Guilleme grumbled, but Catherine just chuckled at his frustration."
    g "Fine. Nine-fifteen it is."
    show cn seethe at left 
    c "Sire, I meant, nine {i}sharp{/i}!"
    "Guilleme's face brightened like a little boy's."
    show gn huh
    g "Oh, I know where we can go."
    show gn happy
    g "There is a quaint little {i}piazza{/i} just south of here."
    show cn sadsmile at left     
    g "They have a breathtaking view of the city. They're on a hill, you see."
    g "I know the owner personally, so we're already guaranteed the best seats."
    g "And they serve the best {i}gratin!{/i}"
    show cn taunt at left 
    show gn huh
    c "Gratin {i}again{/i}?"
    c "If you continue eating that at every given opportunity, there wouldn't be potatoes left in all of France!"
    show cn sadsmile at left 
    "Catherine sighed."
    show cn sad at left 
    show gn smile
    c "{i}Why must he be so...{/i}"
    c "{i}...{/i}"
    show cn annoyed at left 
    c "{i}This better not be a game like all your other flings, Sire.{/i}"
    c "{i}I deserve to be treated like more than a prize.{/i}"
    show cn sadsmile at left 
    "But Catherine watched Guilleme's face beam as he talked about that little house on the hill."
    "How when the weather was perfect, the stars would soak the sky."

    show gn smile
    show cn mischief at left
    "She giggled to herself with fondness."
    show cn uncomfortable at left
    "{i}What a dolt!{/i}"
    "A night in Paris and he would rather eat cheesed potatoes."
    show cn sadsmile at left 
    "It was just like him to pick the stars instead of the city, wasn't it?"
    "It pleased her to know that she adored this side of him that others did not see."
    show cn sad at left 
    "But... was this the real him?"
    "Did she really see through him like he said?"
    "Or was this a face he put on for her sake, like most flirts could?"
    "If it was, then she had been watching this face since she was a little girl."
    show cn dep at left
    "From awe to admiration. From friends to lovers."
    "They had seen the best and worst of each other through the years."
    "Surely there was something to that?"
    "Surely it couldn't all be a lie?"
    "...Right?"
    show gn huh 
    g "I'm sorry. I got carried away. Shall we go?"
    show cn huh at left 
    c "Yes."
    show gn smile at right 
    show cn normal at left 
    "Catherine grabbed her coat and Guilleme took her purse."
    show cn huh at left 
    c "Oh, I almost forgot! Rosa is waiting outside!"
    show gn huh at right 
    g "Then let us hurry and meet up with her."
    show gn smile at right 
    g "I haven't seen her for a long time. I missed her too."
    show cn normal at left 
    g "It will be a treat to spend the evening with two esteemed ladies."
    c "She'll be thrilled to see you."
    g "Just like old times, us three?"
    show cn sadsmile at left 
    c "Yes."
    show gn shy at right 
    show cn normal 
    "She slipped her hand on his arm nonchalantly, and caught Guilleme smile to himself."
    show cn sadsmile 
    c "At the very least, let that smile be real."

    play sound "sfx/glasshatter.ogg"
    stop music
    scene bg cathroom with None
    show cc cryangry at left with None
    show gc huh at right with None

    c "You're lying!"
    show cc crysad at left 
    c "Lady Claudette saw you in Nîmes!"

    show gc unamused at right 
    "Tears and snot ran down her face. She was holding a vintage 1610 bottle of wine."
    show cc angrysneer at left 
    "She gripped the neck of the bottle and flung it at the wall where Guilleme was standing."
    play sound "sfx/glasshatter2.ogg"
    show gc concern at right 
    "He ducked just in time to avoid the glass."
    g "{i}Chérie!{/i}"
    show cc cryangry at left 
    c "Don't you {i}chérie{/i} me, you bastard!"
    show gc sad at right 
    g "Can we not take it out on my wine collection again?"
    show cc angrysneer at left 
    "Catherine threw another bottle in response."
    play sound "sfx/glasshatter.ogg"
    show gc annoyedtalk at right 
    g "Stop, Catherine! You're going to hurt yourself!"
    show cc cryangry at left 
    c "Hurt myself?"
    show cc angrysneer at left 
    c "Like you care!"
    show gc annoyed at right 
    c "You tell me you're off to Avignon last weekend, but you're actually in Nîmes?"
    show gc angry at right 
    g "Why are you making this into a huge deal?"
    g "So I had a stop over at a neighboring town, it was no--"
    show cc cryangry at left 
    c "It's a lie if you omit things!"
    c "I told you at the very start of this relationship, Guilleme."
    show cc angrysneer at left 
    c "I want a hundred percent honesty from you!"
    show gc annoyedtalk at right 
    g "And I've told you as well."
    show cc cryannoy at left 
    g "I have a reputation."
    g "Rumors follow me. Idle mouths can't help but chatter."
    g "Did you know that Lady Claudette once indecently proposed to me?"
    g "And right in her husband's birthday gathering as well."
    show cc cryangry at left 
    c "S-So what?"
    c "That is all beside the point."
    show gc unamused at right
    show cc angrysmile at left  
    c "You know what they say... Where there is smoke there is fire."
    show cc angrysneer at left
    c "How about a name to further torch the bush? {i}Lalaine de Monteclaire?{/i}"
    g "Lalaine is the shop girl of the town. A nice girl."
    show gc boredspeak at right
    g "Or at least, I surmise from all those {i}three{/i} times I made the mistake to enter her shop, it looks like?"
    show gc bitchface at right
    g "Is there anything else you would like to insinuate?"
    show cc angrysmile at left
    c "Oh, nothing at all, Sire."
    show cc cryannoy at left  
    c "Why? Is there anything I should know?"
    show gc annoyed at right
    "Guilleme sighed and tried to speak calmly."
    show gc think at right
    g "Darling, I promised you when we got engaged, didn't I?"
    show gc unamused at right
    g "I will be faithful to only you."
    g "There is no one else--"
    show cc angrysneer at left  
    "But Catherine gritted her teeth."
    show gc annoyed at right
    c "{i}Again with this{/i}!"
    c "You are no clearer from a monkey's spit!"
    show cc cryangry at left  
    c "Answer me straight right now, yes or no! Are you having an affair?!"
    show cc cryannoy at left
    show gc angrytalk at right 
    "Guilleme threw his hands up in annoyance."
    g "Goddammit, Catherine, I am not! I have already answered this!"
    g "Why does it seem like you only hear what you want to hear?"
    show gc angry at right
    show cc cryangry at left  
    c "I just want to understand everything and make it crystal clear. Is that so bad?"
    c "Now explain to me what Lady Claudette--"
    show gc angrytalk at right 
    g "Lady Claudette? You are taking that bitter, conniving woman's words over mine?"
    show cc angrysmile at left 
    show gc angry at right 
    c "Hmph!"
    show cc cryangry at left
    show gc concern at right
    c "Well, I try to get information from the source, but the source isn't very reliable."
    show cc angrysneer at left
    show gc sad at right
    "Guilleme’s shoulders slumped in an irritated surrender. She heard him curse under his breath."
    show gc angrytalk at right 
    show cc cryannoy at left
    g "I am {i}tired{/i} of this, Cath. This is a {i}waste{/i} of time."
    g "What is the point of this if we keep going around in circles?"
    show cc crysad at left 
    "Catherine snuffled, wiping her nose savagely with her hand."
    show cc cryannoy at left 
    show gc angry at right 
    g "You always do this! You go off on a tangent and pick things apart."
    g "You don't even listen to my side at all."
    show gc angrytalk at right 
    g "Could you stop acting like a child for one minute?"
    g "Maybe then we can have a real conversation!"
    show cc cryangry at left 
    c "A conversation with a liar is always one-sided!"
    show cc angrysneer at left 
    show gc angry at right 
    
    "Catherine grabbed two bottles this time."    

    "What would happen if she brought the two bottles crashing in front of her?"
    "Would the pieces of glass stab her face? Her eyes, maybe?"
    "What a random thought."
    "The morbid picture gave her an out of body experience."
    scene bg black with None
    "It was a nasty fight. Depressingly familiar."
    "But they were dancing to the same tune once again."
    scene bg bloverlay with None
    play music "sfx/loverstango.ogg"    
    nvl clear
    o "Here be the lovers."
    nvl clear
    show cc angrysneer at left with dissolve
    play sound "sfx/lightson.ogg"
    show bg spotlightleft with dissolve
    o "Enter left, the hothead."
    nvl clear
    o "Watch her dance with anger blazing."
    o "Tears are sparkling bitter rage."
    o "The fight goes on until she's spent,"
    o "The reasons hazy in her head. "
    play sound "sfx/lightsoff.ogg"
    show bg bloverlay 
    nvl clear
    hide cc angrysneer 
    show gc angry at right with dissolve
    play sound "sfx/lightson.ogg"
    show bg spotlightright with dissolve
    o "Pan right, the rake."
    nvl clear
    o "Both the victim and accused,"
    o "Words are poison or an unlit fuse."
    o "Migraines taunt his pride and temper,"
    o "He grudgingly takes on logic's mantle."
    nvl clear
    play sound "sfx/lightsoff.ogg"
    show bg bloverlay
    show gc angrytalk at right 
    o "The words they throw reach fever pitch."
    o "The dance will crest, he'll choose to leave."
    o "\"Enough of this,\" he says in rage."
    show gc think at right
    o "Temper rising, he exits frame."
    nvl clear
    hide gc think
    show bg bloverlay2 

    show cc angrysneer at left  
    o "Her unspent fervor burning hot."
    o "She cries it off, \"That cowardly sod!\""
    show cc cry at left 
    o "\"What did you expect?\" she asks herself."
    o "He'll take abuse with a bowed head?"
    nvl clear
    show cc angrysneer at left  
    o "{i}The least he could do!{/i} her anger shouts."
    nvl clear
    show cc cryclose at left 
    o "A hint of guilt, a hint of doubt."
    hide cc cryclose 
    show bg bloverlayl 
    show gc angry at right 
    nvl clear
    o "The migraine throbs as he is pacing,"
    o "Annoyed and angered, his face aflush."
    show gc angrytalk at right 
    o "{i}Capricious woman, irrational!{/i}"
    o "He shakes his head with a tired breath."
    nvl clear
    show gc think at right 
    o "Yet he basks in torture and savors the taste."
    o "\"This is love,\" he nods, \"This is love,\" he says."
    o "Love and pain go hand and hand,"
    o "It is painful, yes, but never bland."
    hide gc think 
    nvl clear
    show bg bloverlay 
    o "He nips a morsel and takes a bite."
    nvl clear
    o "\"Exquisite.\" he trembles."
    nvl clear
    o "A rush."
    nvl clear
    o "A charge."
    nvl clear
    o "He feels his heart is struck by love."
    o "Decides that it is worth the gripe."
    nvl clear
    o "A dainty flower he must protect,"
    o "To watch it bloom until it's ripe."
    nvl clear
    o "\"But not right now\", he says, still sore."
    o "His pride's too hard to swallow whole."
    nvl clear
    show bg bloverlay with fade
    o "Hours pass, he wouldn't call."
    o "She forms the words she knows will hurt."
    o "She plans to cut, and make him bleed,"
    o "Yet when he arrives, she all but weeps."
    nvl clear
    o "{i}\"Why'd you leave?\"{/i}"
    nvl clear
    o "{i}\"I shouldn't have.\"{/i}"
    nvl clear
    o "{i}\"Are you angry still?\"{/i}"
    nvl clear
    o "{i}\"I'm here now, love.\"{/i}"
    nvl clear
    o "Her arms are snug upon his neck,"
    o "He'll promise to change, to do what's best."
    nvl clear
    o "For both their sakes, he admits he's wrong,"
    o "A little lie to complete the song."
    nvl clear
    show bg black
    o "Ladies and gentlemen."
    nvl clear
    o "I present to you..."
    nvl clear
    play sound "sfx/lightson.ogg"
    show bg spotlightmiddle with None
    o3 "{i}\"Love\"{/i}"
    play sound "sfx/lightsoff.ogg"
    show bg bloverlay
    show bg black with slowdissolve
    c "Just tell me when you're tired of me or when you find some other pretty thing, you bastard."
    scene bg cathroom with None
    show cc angrysneer at left with None
    show gc angry at right with None
    "Catherine slipped back into her brain just as the last sentence left her lips."
    show cc cryangry at left 
    c "If you are going to leave me, then just leave."
    show cc crysad at left 
    show gc concern at right 
    c "Stop playing me for a fool."
    show gc unamused at right
    "This was a new tempo."
    "She dropped the bottles to her side but did not let go."
    "He noticed the change of song and timed his step accordingly."
    show gc sad at right 
    g "I never once thought or treated you like a fool."
    show gc unamused at right 
    g "I love you."
    g "I'm never going to leave you."
    "New tears churn and bubble from her eyes."
    show cc cryclose at left 
    c "Liar."
    hide cc cryclose 
    "It was her turn to leave this time. And she did."
    show gc sad at right 
    "He was left to perform a solo."
    "Contemplation. Regret. Penance."
    "A vow of new beginnings forming in his head."
    scene bg black 
    $renpy.pause(delay=None)
    stop music 
    
    scene bg rosaroomnorm 
    show rc huh at nearleft
    play sound "sfx/fall.ogg"
    r "Cath?"
    show cc mischief at right 
    c "Rosie-wosie!!"
    show cc mischiefsmile at right 
    "Catherine stumbled into Rosa's room that evening, drunk to high heaven."
    "Her half-lidded eyes surveyed Rosa's meager space."
    "She let herself fall on the bed, regretting it instantly."
    "The ceiling spun in a waltz of throbbing headaches and acid-laced throats."
    show cc mischief at right 
    show rc sad at nearleft 
    c "Bad idea."
    "Catherine stood up and her woobly legs tripped her."
    show rc sad at center 
    "Rosa caught her and sat Cath on her small bed."    
    show cc mischiefsmile at right 
    r "My goodness. You stink of alcohol!"
    show rc hmp at center 
    "She propped some pillows behind her back and fixed the stray hairs that had littered her face."
    show cc mischief at right 
    c "Thanks, hun. You're a dear."
    show cc mischiefsmile at right 
    show rc huh 
    r "How much have you had, Cath?"
    "Catherine counted on her fingers."
    show rc annoyed 
    r "Nevermind."
    show rc huh 
    r "Would you like some water?"
    c "Nope!"
    c "..."
    c "Interesting."
    r "Huh?"
    show cc mischief at right 
    c "I can almost hear liquid sloshing around in my brain when I shake my head."
    show rc annoyed 
    "Rosa pursed her lips. Catherine was in no shape to make decisions right now."
    show rc annoyed at nearleft 
    "She stood up to get her something to sober up."
    show cc awwblush 
    "But Catherine grabbed Rosa's hand and tugged at it gently."
    c "No, no. You."
    c "You sit."
    show rc sad at nearleft 
    r "Uhm."
    c "Please?"
    "Rosa complied."
    "Catherine revealed a bottle about three quarters full."
    show cc mischief 
    c "Snuck another one from the Gilly Monster's closet. Serves him right for calling me a child."
    "Rosa began to protest. Catherine paid her no mind."
    show cc mischiefsmile 
    c "Come on, Rosa!"
    show rc hmp at nearleft 
    c "When have we ever drunk ourselves to the point of insanity?"
    c "And I call you my best friend."
    show cc mischief 
    "Catherine took a huge swig of the bittersweet liquid and offered it to Rosa."
    show rc annoyed at nearleft 
    show cc mischiefsmile 
    "Rosa examined it carefully and took a mouthful."
    show rc huh at nearleft 
    "She gargled it in her mouth, admiring the sweet and sour flavor of the wine."
    r "I've never had anything this rich before."
    show cc mischief 
    show rc normal at nearleft 
    c "Good, right?"
    show cc mischiefsmile 
    c "It had to be. It's the last bottle."
    show rc huh at nearleft 
    r "...So..."
    show cc angrysmileblush 
    r "Had another fight with Gui--"
    c "Shush. Bad wind follows that name."
    c "I am not talking about that egocentric pompadour tonight."
    show cc mischiefsmile 
    c "We are going to drink."
    c "We are going to reminisce."
    show cc mischief 
    c "And tomorrow, we'll hate ourselves together."
    c "Agreed?"
    show rc happy at nearleft 
    "Rosa giggled."
    r "If you say so."
    scene bg black 
    $renpy.pause(delay=None)
    
    
    play music "sfx/mellow.ogg"
    show bg rcbed 
    c "Alright, alright, last one."
    "Rosa puffed her cheeks in mock disgust."
    r "Fine!"
    c "How do you make Holy Water?"
    r "How?"
    c "Boil the hell out of it."
    "Rosa and Catherine were assaulted by fits of hysterical laughter."
    "Catherine felt the muscles of her cheeks ache."
    r "That is {i}so{/i} bad. I don't even have the words."
    "Catherine wiped the tears of laughter from her eyes."
    c "I heard that from one of your suitors, Sire Adrien."
    "Rosa rolled her eyes."
    c "How come I always end up talking to your suitors more than you?"
    c "I must start charging you a fee."
    r "I'll pay it with my gratitude."
    c "What is wrong with Sire Adrien, anyway? He seems like a nice man."
    c "Nice hair. Nice teeth. Nicely groomed mutton chops."
    "The women laughed."

    c "How about Sire Ferrand? He sent you that lovely bouquet of flowers."
    r "Ah... I am not interested in a relationship at the moment."
    c "At the moment? You don't seem interested ever."
    r "I am!"
    r "...Sometimes."
    r "It is just hard to connect to people for me beyond physical."
    r "Relationships seem out of the question."
    c "You don't have any difficulty with me or that idiot in the upper room. It means you are not incapable."
    r "..."
    r "...That is only because you are my closest friends."
    c "Well, there {i}must{/i} be someone!"
    r "..."
    c "Oh, you are so picky. If you go on like that, you might end up an old maid!"
    r "So be it."
    r "I'd rather take care of your children anyway. I shall be an amazing godmother."
    scene bg rosaroom
    show cc awwblush
    show rc smile at nearleft
    "Catherine smiled wistfully."
    show cc sadsmile
    c "I'm not sure I want any."
    show rc huh at nearleft
    r "What?"
    c "Children."
    c "I love children, but..."
    show cc sad
    c "It's a little scary..."
    "Catherine bit her lip."
    show rc normal at nearleft
    "{i}What if she becomes her own mother?{/i}"
    "It was such a terrifying possibility, wasn't it?"
    "She barely remembered her mother. Her malady had struck as soon as Catherine was born."
    "She had never called Catherine by her name, not even on the day she had died."
    "All she knew was that their family struggled with that crisis."
    "Her father, exhausted and depressed, and her sister forced to grow up too fast."
    "{i}To be a blight to the people you love, how horrible would it be?{/i}"
    "{i}How much of my own defects will I impress on my child?{/i}"
    show cc huh
    show rc smile at nearleft
    r "Catherine..."
    "Rosa smiled at her, interrupting her thoughts."
    show cc aww 
    r "You will be a good mother."
    r "Your past does not matter."
    show cc awwblush
    "Catherine stared at Rosa, almost enchanted at her ability to know what she was thinking."
    show cc shysmile
    "She really was her best friend, wasn't she?"
    "The thought warmed her heart."
    show cc awwblush
    c "You really think so?"
    r "Yes."
    show rc thinksmile at nearleft
    r "The fact that you are so concerned about them, before they are even born, speaks much of your care."
    show rc smile at nearleft
    show cc shysmile
    r "Whatever happens, those children will grow up loved."
    "Catherine blushed and changed the subject."
    show cc happy
    c "Ohh, we're out of booze. We finished it."
    show rc huh at nearleft
    show cc smile
    r "I'm quite buzzed."
    show cc mischief
    show rc smile at nearleft
    c "Hey, remember the first time we drank?"
    show rc huh at nearleft
    r "Do you mean the party or the potato incident?"
    show cc huh
    c "Of course I meant the potato incident."
    show rc happy at nearleft
    r "Oh! How can I forget?"
    show rc laugh at nearleft
    "Rosa burst out laughing."
    r "That was hilarious!"
    show cc embr
    c "Wench, stop laughing! I almost went to jail!"
    show rc happy at nearleft
    show cc angrysmileblush
    c "Goodness, I was so stupid!"
    "Rosa laughed again."
    show rc laugh at nearleft
    r "Amen!"
    show cc mischief
    c "Hey! You're supposed to say {i}'No, Catherine, we do dumb things when we're young!'{/i}"
    show rc happy at nearleft

    r "Catherine, we do dumb things when we're young."
    show rc laugh at nearleft
    show cc embr 
    r "It's about time you learn your lesson."
    show rc happy at nearleft
    r "I can't wait to tell your children endless tales of your shenanigans."
    show cc superannoyed 
    show rc laugh at nearleft
    c "Wench!"
    r "Tut-tut."
    scene bg black 
    "Catherine grabbed Rosa's waist and attempted to tickle her, but Rosa slipped away laughing."

    "Catherine's stomach lurched and she stopped, her hands still hugging Rosa's waist."
    "The room spun, but it wasn't unpleasant."
    "She felt like being gently rocked in a cradle."
    "She closed her eyes and smiled."

    "She took in Rosa's scent, always smelling slightly of apples."

    "Rosa scratched her head and smoothed her hair."
    c "This is nice."
    r "...Yes."
    c "Rosa."
    r "Hm?"
    c "Thank you for being with me."
    r "Of course."
    c "No, I mean--"
    scene bg rosaroom
    show cc huh at nnnearleft
    show rc thinksmile at nearleft
    "She sat up on the bed."
    show rc huh at nearleft
    show cc normalclose at nnnearleft
    c "You've been with me all my life."
    show rc smile at nearleft
    c "You are my oldest friend."
    show cc sadsmile at nnnearleft
    c "When we first met... I didn't have many friends."
    c "I just studied my piano lessons night and day, because that's all I ever knew to do."
    c "It was all I had..."
    c "Maybe that was why I begged Papa to let you stay with us."
    c "I was so happy..."
    show rc thinksmile at nearleft
    "Rosa smiled fondly at the memory."
    show cc shysmile at nnnearleft
    c "You were there for me, always."
    show cc mischief at nnnearleft
    c "Ugh. That sounds disgustingly melodramatic."
    show rc happy at nearleft
    show cc mischiefsmile at nnnearleft
    r "You're drunk. I understand."
    show rc laugh at nearleft
    show cc happy at nnnearleft
    "They laughed again."
    show cc mischiefsmile at nnnearleft
    show rc thinksmile at nearleft
    r "Would you like to hear something worse?"
    c "What?"
    show rc smile at nearleft
    show cc awwblush at nnnearleft
    r "You changed my life."
    show cc mischief at nnnearleft
    show rc laugh at nearleft
    c "Ugh, that {i}is{/i} worse!"
    show cc normalclose at nnnearleft
    show rc thinksmile at nearleft
    "Rosa smiled fondly as she played with Catherine's hair."
    r "I'm the lucky one, Catherine."
    show cc normal at nnnearleft
    r "You took me home and treated me like I was family."
    show cc shysmile at nnnearleft
    r "I wouldn't have known what a real family was like without you, Papa Francois and Émilie."
    r "Even if Papa Francois always did avoid me, I knew he cared for me like his own."
    show cc huh at nnnearleft
    show rc depsmile at nearleft
    c "Hm, yes, why is that?"
    r "..."
    r "...That was why I liked him. He was a good man."
    show rc happy at nearleft


    r "And you know, Guilleme is almost family, too."
    show rc smile at nearleft
    show cc mischiefsmile at nnnearleft
    "Catherine made a face at the mention of the man."
    show cc sadsmile at nnnearleft
    "But her eyes softened."
    if openlocket:
        show rc depsmile at nearleft
        c "...I miss my father."
        r "Me, too."
    show cc sad at nnnearleft 
    show rc thinksmile at nearleft
    "There was a pause. Catherine shifted awkwardly in her skin."
    show cc shy at nnnearleft
    c "..."
    show cc embrblush at nnnearleft
    c "C-Can I tell you a secret?"
    show rc huh at nearleft
    show cc shy at nnnearleft
    r "Of course."
    show rc smile at nearleft
    c "..."
    show cc embrblush at nnnearleft
    c "Guilleme and I..."
    show cc blurt at nnnearleft
    show rc shockblush at nearleft
    c "W-We haven't had intercourse."
    show cc shy at nnnearleft
    r "Recently...?"
    show cc depshysmile at nnnearleft
    c "No, I mean... At all."
    show rc annoyedblush at nearleft
    r "Oh..."
    show rc annoyedblushclose at nearleft
    "Rosa cleared her throat."
    show rc annoyedblush at nearleft
    r "I see..."
    show rc shockblush at nearleft
    r "After all these years?"
    c "W-Well..."
    show cc embrblushhuh at nnnearleft
    c "We kind of... try sometimes... But I always get freaked out."
    show cc depshysmile at nnnearleft    
    show rc annoyedblush at nearleft
    "Rosa blushed."
    "Her head knitted together images of the two people she considered her friends."
    show rc annoyedblushclose at nearleft
    "Rosa tried to push them away, but all she was able to do was paint the warped fantasies in gossammer and fuzz."
    show rc annoyedblush at nearleft
    "She cleared her throat."
    show rc shockblush at nearleft
    r "Is that why you have separate rooms even when we moved here to the {i}château?{/i}"
    show cc embrblushhuh at nnnearleft
    show rc normal at nearleft
    c "No, that was his idea. He's very peculiar with his sleep."
    show cc depshysmile at nnnearleft
    c "I imagine we'll be keeping the separate bedrooms even when we get married."
    c "I don't really mind."
    show rc think at nearleft
    r "Well, your wedding is soon, isn't it?"
    show rc normal at nearleft
    r "Perhaps you are just nervous."
    c "No, I don't think it's like that."
    show rc shockblush at nearleft
    c "Recently, we'd get intimate, but I always stop when things get too far."
    r "O-Oh..."
    show rc think at nearleft
    c "He gets upset sometimes, but he says it's alright."
    "Catherine looked down ruefully on her toes."
    c "He doesn't push me into it. I should be glad."
    show rc normal at nearleft
    c "...But..."
    show cc embrblushhuh at nnnearleft
    c "...Don't you think it's strange?"
    show cc depshysmile at nnnearleft
    c "What if I... stay like this even after we get married?"
    c "I don't understand why..."
    c "Sometimes I get these doubts, and I wonder why they are there."
    c "Isn't that unfair for him?"
    c "..."
    show cc embrblushhuh at nnnearleft
    c "I do love him! I know I do..."

    show cc depshysmile at nnnearleft
    c "I just feel like there is something wrong with me..."
    show rc huh at nearleft
    r "There is nothing wrong with you."
    show rc normal at nearleft
    show cc embrblush at nnnearleft
    c "...But it makes me really insecure."
    show cc depshysmile at nnnearleft
    c "This... lack of, you know..."
    show cc angrysmileblush at nnnearleft
    c "What if he's getting it somewhere else?"
    show cc embrblush at nnnearleft
    c "It drives me crazy."
    show cc shy at nnnearleft
    c "And believe me, I want to!"
    show cc depshysmile at nnnearleft
    c "I just... can't. For some reason."
    show rc think at nearleft
    c "I get this horrible feeling I can't explain."
    c "..."
    show rc hmp at nearleft
    "Rosa examined Catherine's face and came to a conclusion."
    show rc think at nearleft
    r "It took me a while to understand sex."
    show cc huh at nnnearleft
    "The sudden no-nonsense comment surprised Catherine."
    show rc normal at nearleft
    "Rosa went on."
    show cc sad at nnnearleft
    r "I was the same as you."
    r "I had always had an adverse feeling for it."
    show rc think at nearleft
    r "Like it's dirty and that I should be ashamed for enjoying it."
    r "I had always thought love would make sex clean."
    show rc normal at nearleft
    r "But..."
    show cc huh at nnnearleft
    r "That's not how it works."
    show rc think at nearleft
    show cc sad at nnnearleft
    r "They are two separate things."
    c "..."
    r "So just because you don't like sex,"
    show rc smile at nearleft
    show cc depshysmile at nnnearleft
    r "It doesn't mean you don't love him, Cath."
    show cc embrblushhuh at nnnearleft
    "Catherine looked up at her."
    r "Why do you even care so much to hurt him? What do you think love is?"
    c "..."
    r "If you need time to understand sex further,"
    r "then the best partner would be somebody you know
    who will take care of you and your feelings."
    r "That goes both ways. For you and for him, too."
    show cc shysmile at nnnearleft
    "The warm feeling returned to Catherine's heart."
    c "...How do you do that?"
    show rc huh at nearleft
    r "Huh?"
    show rc shockblush at nearleft
    c "You always know the right thing to say. Always."
    show cc awwblush at nnnearleft
    show rc annoyedblush at nearleft
    "Rosa blushed at this, suddenly aware that they were still in a loose tangle of an embrace."
    show rc laugh at nearleft
    r "I've read a lot of smart books lately."
    show rc shockblush at nearleft
    "She tried to diffuse the situation with a laugh, but Catherine didn't drop her look."
    show rc depsmileblush at nearleft
    "Candlelight played pretty shadows on her skin."
    show rc depblush at nearleft
    "It illuminated the glint in her eyes."
    show rc depblush at nearleft
    show cc depshysmile at nnnearleft
    "The moist on her lips."
    "Rosa felt the warmth of the alcohol rise up to her face."
    "Her heartbeat increased steadily."
    show rc shockblush at nearleft
    r "A-Anyway. Maybe you will feel better about it when you are married."
    show cc depshysmile at nnnearleft
    r "You are probably just nervous about the whole thing."
    show rc annoyedblush at nearleft
    show cc normalcloseblush at nnnearleft
    "She made attempts to curl away from Catherine's arms."
    show rc depblush at nearleft
    "Slowly, subtly run away."
    "Disperse the proximity."
    show rc shockblush at nearleft
    show cc awwblush at nnnearleft
    "But she couldn't run away from her stare."
    "Catherine's hand caressed Rosa's face."
    show rc depblush at nearleft
    "She touched her scars daintily, tracing them with her fingers."
    show rc shockblush at nearleft
    c "You're really pretty, Rosa."
    show rc depblush at nearleft
    c "Especially... Right now."
    r "..."
    show rc depsmileblush at nearleft
    r "...Thank you, I think?"
    show rc depblush at nearleft
    show cc huh at nnnearleft
    c "..."
    c "You don't believe me."
    r "..."
    r "I..."
    show rc depsmileblush at nearleft
    show cc huh at nnnearleft
    r "I don't think I am."
    show cc mm at nnnearleft
    show rc dep at nearleft
    r "..."
    r "I... I look in the mirror and I see a freak."
    show cc shock at nnnearleft
    c "Rosa!"
    show cc aghast at nnnearleft
    c "That's not true--"
    show rc depsmile at nearleft
    r "It is fine!"
    show cc aww at nnnearleft
    r "I... liked being a freak. I wanted to be ugly."
    show cc mm at nnnearleft
    r "I used to bind my breasts and hide in the shabbiest clothes I could find."
    "Rosa touched her eye."
    show rc dep at nearleft
    "{i}This was penance{/i}, she rememberd herself saying."
    show rc depthink at nearleft
    "For being a sinner and a freak."
    "For attracting attention and spite."
    "For dressing nicely."
    "For letting her hair grow long."
    "But really..."
    show rc dep at nearleft

    r "I did this to myself... To hide."
    show cc aww at nnnearleft
    c "...To hide?"
    show rc depthink at nearleft
    "Rosa's mouth quivered."
    show rc depsmile at nearleft
    r "I thought people..."
    show rc dep at nearleft
    show cc shock at nnnearleft
    r "...Don't touch ugly things."
    c "..."
    r "But the truth is, they do."
    show rc depsmile at nearleft
    show cc crysad at nnnearleft
    r "So what I'd rather be is invisible."
    show cc cryclose at nnearleft
    "Catherine wrapped her arms around Rosa's neck."
    "She heard Catherine sniff and wipe tears behind her embrace."
    scene bg rcsweet3 
    "She pushed Rosa's hair away and kissed her defective eye."
    c "You're not a freak. And you're not ugly."
    c "I love every part of you."
    c "They're all beautiful."
    "Rosa forgot how close they were now, forgot Catherine's hands on her own."
    "Here was somebody who accepted her, with all her faults and ugliness."
    r "You..."
    r "You always made me feel I am worth something."
    c "Because you are..."
    c "You are beautiful, Rosa, inside and out."
    "Rosa saw her face reflected in Catherine's eyes."
    "In them, she did indeed look beautiful."
    "A lump formed in Rosa's throat."
    "Catherine's face hovered above her cheek."
    "She planted a little seed of a kiss on it, just barely away from her lips."
    "Rosa kissed her nose in return. It made Catherine giggle."
    show bg rosaroom
    "At first, the kisses were sweet. Innocent."
    "The kind of punch drunk kisses that sent them both into bouts of giggling."

    "But Catherine's hand carressed her neck."
    stop music fadeout 7.0
    "The kisses lingered."
    "Lips melded."
    "Hands explored."
    "And Rosa sucked on Catherine's tongue inside her mouth."
    "Wine."
    "Candle wax."
    "Spit."
    "That was what it tasted like."
    "Rosa's head began to swoon."
    "Catherine's hand squeezed her right breast."
    play music "sfx/spooks.ogg"
    "Tripe."
    "Grapes."
    "Plush."
    show bg polaroid2
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=3)
    play sound "sfx/heartbeat.ogg"
    show bg black
    "Rosa began to taste more of her."
    "Longing."
    "Regrets."
    "Tears."
    "A sensational flavour she had never tasted before hovered at the edge of her tongue."
    "Suddenly she was hungry for it."
    gt "Take it all."

    play sound "sfx/heartbeat.ogg"
    show bg polaroid4 
    show bg black
    "Rosa savored the taste. She breathed deeply."

    gt "All mine."
    play sound "sfx/heartbeat.ogg"
    show bg black 
    m "Child!"
    gt "I want it."
    gt "Her heart. I want her heart."
    gt "Her love is sweet."
    play sound "sfx/heartbeat.ogg"
    m "Listen to my voice."
    "M-Mother?"

    gt "B...But I'm so hungry."
    gt "{i}So... hungry...{/i}"

    play sound "sfx/heartbeat.ogg"
    m "Stop!"
    scene bg rosaroom 
    "Rosa flung her eyes open."
    "A sinking feeling of menace overcame her."
    r "{i}No!{/i}"
    "Rosa pulled away."
    "She pushed Catherine away from her face."
    "Catherine's eyes snapped open, startled by Rosa's outburst."
    gt "Why did you stop?!"
    gt "Greedy, selfish bitch!"
    

    show cc awwbig 

    "She blinked for a few seconds."
    show cc aghast 
    "A look of horror creeped on her face."
    c "..."
    show cc disgust 
    c "I..."
    c "I-I'm sorry..."
    c "I didn't mean--"
    r "N-No, Cath--"
    "Rosa couldn't stand the hurt in her eyes."
    "She was probably blaming herself."
    "Rosa wanted to shout how wrong she was, but the lump in her throat became a rapacious mouth."
    "A tumor had grown inside of her, a parasite."
    "She could feel it pulse and slither inside her neck."
    "She couldn't speak at all."
    "Catherine wobbled off the bed."
    play sound "sfx/fall.ogg"
    show cc disgust at right 
    "She wiped her mouth and cheeks which were covered with a thin layer of drool."

    c "I-I'm so sorry, Rosa."
    c "I'm going to leave now."
    r "Cath..."
    c "Good night."
    hide cc disgust 
    play sound "sfx/softdoorclose.ogg"
    "Rosa should've followed her."
    "But when she tried to stand, the floor twirled."
    "She choked at the flavor left in her throat."
    "Sick and cloying. Sticky sweet like honey."
    "The taste both repulsed and enticed her."
    "Thick spit leaked out of her mouth. She felt the urge to vomit."
    r "T-This is nothing, Mother."
    r "Just a bad after-effect of alcohol."
    r "No."
    r "Please, don't call me that!"
    r "It was an accident!"
    r "..."
    r "Everything is fine!"
    "She would talk to Catherine tomorrow, assure her that this was not her fault."
    "Everything was fine."
    show bg black 
    $renpy.pause(delay=None)

    stop music
    
    show bg black 
    play sound "sfx/urgentknock.ogg"
    "There was an urgent knock at Guilleme's door."
    play music "sfx/journal0.ogg" 
    show bg guilroom 
    show gf annoyed at right 
    "The clock read a quarter past two in the morning."
    play sound "sfx/urgentknock.ogg"
    "He closed his journal and stood up from his desk."
    play sound "sfx/urgentknock.ogg"
    show gf talk at right 
    g "Yes, coming!"
    "He opened his door."
    show gf huh at right 
    show cc cry 
    "Catherine stood in front of him, her cheeks stained with hastily-wiped tears."
    g "Cath?"
    show cc crysad 
    c "..."
    c "Guilleme, can we talk?"
    g "Oh. Isn't it quite late?"
    c "Please. It's urgent."
    show cc cryclose 
    g "A-Alright..."
    "Guilleme led her inside."
    show cc crysad 
    show gf smirk at right 
    g "Lady, you smell like my vintage bottle of Bourgogne."
    g "Did you get so drunk you actually thought of apologizing first?"
    g "I didn't think I'd see the day!"
    c "..."
    show gf huh at right 
    g "Darling, what's wrong?"
    "Catherine's thumb went to her mouth without thinking."
    "How could she even begin to tell Guilleme what she had done?"
    $ nvl_darkbg = True
    nvl clear
    o "{i}Honey, I was really upset with you today.{/i}"
    o "{i}So despite any good sense, I went and got myself drunk.{/i}"
    o "{i}This time, I dragged Rosa along with me.{/i}"
    o "{i}Things have a tendency to go out of hand when alcohol is involved, as you know.{/i}"
    nvl clear
    o "{i}Long story short, I came unto Rosa.{/i}"
    nvl clear
    o "{i}You know Rosa? The girl who is almost like my sister?{/i}"
    o "{i}Yes, I may have forced myself on her.{/i}"
    nvl clear
    o "{i}And I did that right after she told me she has been abused before.{/i}"
    show gf err at right 
    "She felt Guilleme's hand take her thumb away from her mouth."
    g "Cath."
    show cc shock 
    "She looked at her fingers in horror."
    "Her habit had surfaced again."
    "She thought she had gotten rid of this as she grew up."
    "Replacing the nail-biting with a meticulous, almost obsessive care for her fingers."
    "\"{i}My fingers are my livelihood. I must take care of them.{/i}\""
    show cc disgust 
    "Now the nails  were chewed down to jagged stumps, and a couple of them had tiny blistering cuts."
    show gf talk at right 
    g "Cath? Can you talk?"
    show cc cry 
    show gf err at right 
    "Catherine's eyes snapped back to Guilleme, as if he had just materialized in the room beside her."
    nvl clear
    o "{i}So yes, like I was saying, darling.{/i}"
    o "{i}Which is the worst thing, what do you think?{/i}"
    nvl clear
    o "{i}This abuse of my best friend, or my infidelity to you?{/i}"
    nvl clear
    o "{i}Hmm...{/i}"
    nvl clear
    o "{i}Or if that doesn't cut it, dear, may I divulge to you one last point--{/i}"
    o "{i}I felt something worrying when I kissed her.{/i}"
    nvl clear
    o "{i}Excitement.{/i}"
    o "{i}If she hadn't stopped me, something else would've--{/i}"
    nvl clear
    o "{i}It felt so real. It didn't feel like a mistake.{/i}"
    o "{i}It felt like it had always been there, buried deeply.{/i}"
    nvl clear
    o "{i}So much so that it felt like cheating.{/i}"
    nvl clear
    o "{i}It was like a craving. I wanted it.{/i}"
    o "{i}It was something I haven't felt with you, when we...{/i}"
    nvl clear
    show cc cryclose 
    o "{i}Why is this happening?!{/i}"
    o "{i}I don't know---{/i}"
    nvl clear
    o "{i}I don't even know who I am anymore!{/i}"
    nvl clear
    show gf sad at right 
    g "Cath, you are scaring me. Tell me what's wrong?"
    nvl clear
    o "{i}Would you still want to marry me?{/i}"
    o "{i}Would you still love me if you knew?{/i}"
    nvl clear
    o "{i}I wouldn't.{/i}"
    o "{i}I can't even look at myself in the mirror.{/i}"
    nvl clear
    o "{i}But I think I know who I am now.{/i}"
    nvl clear
    o "{i}I am a selfish, depraved bitch.{/i}"
    nvl clear
    o "{i}I have always been the controlling, jealous lover to you.{/i}"
    o "{i}And just one night of drunken frenzy--{/i}"
    nvl clear
    o "{i}I went and took advantage of the two people I care for the most.{/i}"
    #nvl clear
    #o "{i}Not enough wine to justify this.{/i}"
    $ nvl_darkbg = False
    c "I--"
    c "..."
    show cc cryangry 
    c "I want to call off the engagement."
    show cc cryannoy 
    show gf huh at right 
    "At first, Catherine saw that Guilleme treated it as a joke, but the panic in his eyes set in immediately."
    show gf annoyedtalk at right 
    g "What?"
    
    c "I said, I'm calling off the engagement."
    show gf angry at right 
    g "Well, I refuse."
    show cc cryangry 
    c "You don't have a choice. I'm leaving tomorrow."
    g "No."
    show cc cry 
    g "Not until you tell me what's wrong."
    "Guilleme's eyes didn't flinch."
    show cc crysad 
    "These were the looks he gave her that melted her heart. They were so sure and steadfast in their care."
    "They were just fighting this morning, a fight {i}she{/i} had started, as usual."
    "Yet, there was no doubt in his eyes at all."
    "If she were to see that certainty fade away from his eyes, she knew it would break her."
    c "..."
    show gf annoyedtalk at right 
    g "Is it about the fight earlier?"
    show gf angry at right 
    g "Because, Cath, I swear to you, I haven't done any of th--"
    show cc cryclose 
    c "No, stop."
    "Hearing him reinstate his devotion to her just made it more painful."
    "Tears pooled in her eyes and fell in huge, ugly globs."
    "She had been doing so well, too. She had thought she could hold it in until she left."
    "She wiped the tears as best she could, but more kept pouring out."
    c "It--It isn't about that."
    show gf sadtalk at right 
    g "Then what is it? What do you want me to do?"
    g "Whatever it is, I shall do it."
    "This was so hard. Why did this have to be so hard?"
    "Why did she even go here?"
    c "...I--"
    "Because she wanted to see his face."
    show cc cry 
    "She wondered what it would be like for a cheater to go back to the arms of her lover."
    "Would it change somehow?"
    "Did she still love him? How could she even tell?"
    "All her emotions were wrapped in a thick layer of guilt."
    "It was hard to distinguish every painful thought."
    "She'd started to sob now, yes indeed. Ugly, unflattering snorts came out of her nose."
    "It felt comforting to hold on to guilt."
    "Its existence made the hatred towards herself bite less."
    show cc cryclose 
    g "Cath, please tell me what's bothering you!"
    c "..."
    show cc blurt
    show gf huh at right
    c "Idont d-deserve y-you! I'm... ahorribleperson!"
    c "Y-You ought to f-findsomeoneelset-tomarry!"
    show cc cryclose
    show gf err at right 
    "Catherine let the words tumble out of her mouth, slightly relieved to be rid of them."
    show cc cry 
    show gf think at right 
    "She looked tearfully up at Guilleme to gauge his reaction, but he just stared back at her blankly."
    show gf err at right 
    c "..."
    g "..."
    show cc cryclose
    c "{i}Why wouldn't he say anything?{/i}"
    "Catherine sobbed, fearing the worst."
    show gf blank at right 
    show cc cry
    "Guilleme cleared his throat and spoke hesitantly."
    g "Err... uh..."
    g "Could you, uhm... repeat that?"
    show cc angrysmileblush 
    "He cupped his hand to his ear and angled it closer to her face."
    "He apparently hadn’t caught any of her heartfelt words."
    "Catherine snarled angrily at him."
    show cc superannoyed 
    c "You idiot!!"
    c "I'm having a breakdown here!"
    show gf sad at right 
    g "B-But I didn't understand what you said..."
    show cc cryangry 
    c "I said you ought to find someone else because I am a horrible person--"
    show gf angry at right 
    show cc cry at nearrightc
    "Guilleme pulled her to him."
    show gf huh at right 
    g "Oh, that's it?"

    show gf smile at right 
    g "Whatever made you think that I'll accept that reason?"
    show cc cryclose at nearrightc
    "Catherine's tears soaked his shirt."
    c "You don't know what I've done."
    g "Then tell me."
    c "You'll hate me. I guarantee it."
    show gf smirk at right 
    g "Did you punch a baby?"
    c "No."
    show cc mischief at nearrightc 
    "The inside joke made her laugh out of the blue."
    show gf smile at right 
    "She buried her face in his chest in a half-sob, half-laugh."
    show cc awwblush at nearrightc
    "Suddenly, her doubts were cleared."
    show cc cryclose at nearrightc
    "Suddenly, she didn't want to marry anyone else."
    "Catherine's arms tightened around Guilleme's waist."
    c "{i}I've been taking you for granted, haven't I?{/i}"
    c "{i}I've been arrogant, expecting you to always adjust to me and my whims.{/i}"
    show cc annoy at nearrightc
    "A new fervor sprung out of her love for him."
    c "{i}I don't deserve you right now.{/i}"
    c "{i}But I'll work on that, if you give me another chance.{/i}"
    "First, she would tell him what she had done."
    "Then it would be up to him if he still wanted her."
    "He deserved that decision."
    
    c "What I did--"
    show cc aww at nearrightc
    "But Guilleme stopped her with a kiss on her forehead."
    g "Tomorrow."
    g "After a hearty breakfast and a good night's rest."
    g "I'll listen to what you have to say."
    show gf huh at right 
    g "Though I'm quite sure my answer will be the same."
    show cc awwblush 
    "Catherine's face melted into a smile and he beamed at her."
    show gf happy at right 
    g "My star finally smiles."
    show gf norm at right 
    "Catherine wiped her eyes."
    c "I love you so much."
    "She sighed with content, part of her anxiety put to rest."
    show cc sad 
    c "I do. I really do."
    "She whispered that last one under her breath, as if trying to console herself."
    show cc aww 
    c "Guilleme..."
    g "Yes, dear?"
    c "Will you make love to me?"
    show gf huh at right 
    "Guilleme's brow shot up in surprise."
    show gf err at right 
    g "Right... now?"
    show cc sad 
    c "Yes..."
    c "No..."
    c "Well, if you're not ready, later is also fine."
    c "Or tomorrow."
    c "But since it's already morning, then technically it's {i}today{/i}, right?"
    show gf smirk at right 
    "Guilleme's head tilted slightly, an amused smirk plastered on his face."
    show cc superannoyed 
    c "Please, take me seriously, Guilleme."
    c "This is important to me!"
    show cc sad 
    c "I have to know. I have to make sure."
    show gf huh at right 
    g "Make sure of what?"
    show gf smile at right 
    show cc crysad 
    c "..."
    g "Catherine."
    "Guilleme held her hand."
    g "I think you are tired."
    show gf smirk at right 
    g "And just a little bit barmy... More that usual, I mean."
    show gf norm at right 
    show cc angrysmileblush 
    g "But this is what we will do."
    show cc aww 
    stop music fadeout 2.0
    "Guilleme guided the woman to the bed and sat her down."
    g "We are going to lay on the bed."
    g "I am going to pat your hair until you fall asleep."
    g "I shall skip work in the morning, have that trifling little talk you want."
    show gf happy at right 
    g "And as such, if you're still in the lovemaking type of mood--"
    show gf smile at right 
    g "Then {i}mademoiselle{/i}, I will take you up on your offer."
    show cc awwblush 

    "Catherine's eyes moistened, but this time they were happy tears."
    #"He has always been so considerate. Always caring."
    c "I love you."
    show gf annoyed at right 
    "Guilleme shrugged and lifted Catherine's legs up onto the bed."
    show gf smirk at right 
    g "I love you too, and aren't you lucky."


    show cc angrysmileblush 
    c "Save it!"
    show gf smile at right 
    "He climbed on the bed beside her."
    show cc awwblush 
    "Catherine draped her arm over him."

    "He searched for her hand, brought it up to his lips and patted it."
    scene bg guilbednorm
    "She closed her eyes and rested her head on his chest, comforted by the warmth of his embrace."
    c "Honey, can I ask you something?"
    g "Hm?"
    play music "sfx/night2.ogg"
    c "Why do you love me so much?"
    "Guilleme mused for a while."
    g "Is that a trick question? It feels like a trick question."
    "Catherine whined. Guilleme laughed."
    g "Fine, fine. I shall humor you for now because you are in such a state."
    g "Hm... I love you simply because it's easy to love you, darling."
    g "You are my star, my light. You keep me right, always."
    g "You make me want to do good by you, to be a better person."
    g "You aren't even my wife yet, but the townspeople are already calling you their Lady."
    g "I may have to hand you the marquisdom myself!"
    c "That is only because everyone in town knows who I am."
    g "Oh, I wonder why that is?"
    g "Is it because you help sell vegetables in the marketplace on weekends?"
    g "Or because you conspire with my cooks to hold impromptu picnics with the locals?"
    c "...You know about that?"
    g "One can only sneak out that much food without getting noticed, Madame."
    g "It amuses me how the servants cover for you upon inquiry, as well." 
    c "It was my idea. They're not to blame."
    g "I know, darling. I know."
    "Guilleme chuckled and kissed her temple."
    g "It goes to show how your presence uplifts everyone's lives."
    g "Including mine."
    c "..."
    g "But honestly, those reasons aren't exactly why."
    g "I love you, Cath. I just do. Beyond what I thought I was capable of."
    "Catherine's heart cracked with his last utterance."
    c "If I did something... bad, would you still love me?"
    g "Yes, I would."
    c "Are you sure?"
    g "I'm sure."
    c "What if I've hurt an innocent person?"
    c "What if I've hurt you?"
    "She bit her lip."
    c "...What if I was unfaithful?"
    "Guilleme stared at her questioningly. Catherine buried her face in his chest."
    "She felt his hand smooth away her hair. He whispered gently into her ear."
    g "If you'll still have me,{w=0.2} come back to me."
    c "Guilleme..."
    g "What happened doesn't matter to me at all."
    g "You are not your mistakes, Cath."
    "Guilleme cleared his throat. Suddenly, he seemed to have trouble breathing."
    g "You have the power to... {w=0.2}to change."
    g "..."
    scene bg cgbed 
    g "How about you?"
    g "If I told you that--"
    g "I am not what I say I am, would you--"
    c "Hm?"
    c "What do you mean?"
    g "N-Nevermind."
    g "It's a silly question."
    c "What?"
    c "Is something bothering you, Guilleme?"
    "Guilleme turned his head away and closed his eyes."
    g "Nothing, darling."
    g "We should sleep now."
    "Catherine patted away the frown on his brow."
    "She traced his cheeks with her fingers."
    c "Guilleme, I do love you. Now, I am more than certain."
    c "It gives my heart happiness to know for sure."
    c "What reminded me was your generosity."
    c "You..."
    c "You give every bit of yourself to the people you love, do you know that?"
    g "Because I have to, darling."
    c "Well, you have always inspired me, {i}chou{/i}."
    c "I have always looked up to you."
    c "You treat everyone, no matter their status, with kindness."
    c "Never have I met a man more generous and thoughtful about others."
    c "A man with so much love to give."
    c "And that is why I love you."
    c "You are a good man."
    g "..."
    g "...But if that's not what I really am?"
    "Catherine shook her head."
    c "You can't fake sacrifice, {i}mon chou{/i}."
    c "I have seen you care for the people in this town."
    c "I've seen how you've loved me."
    c "I don't care much for intention, you see."
    c "It's what we actually do that defines us."
    "Guilleme paused, his voice choked up in his throat."
    g "Not always..."
    g "...not always..."
    "Guilleme found Catherine's hand on his face and squeezed it."
    "She stretched her neck and kissed his cheek."
    g "Catherine."
    g "You are always scared I will leave you."
    c "..."
    g "But the truth is, I know it is {i}you{/i} who will leave me."
    g "And it... it hurts."
    c "What?"
    g "You are different..."
    g "I've loved you for so long."
    g "It scares me, how deep I have rooted myself..."
    g "Sometimes I..."
    g "...I deem it better to end this wretched existence."
    g "T-To save you from--"
    c "What are you talking about, Guilleme? You're not making any sense."
    c "Is it your turn to scare me?"
    g "..."
    g "I-I'm sorry."
    "They didn't speak for a while."
    "The air became a little uncomfortable. She could feel Guilleme's stressful breathing on her forehead."
    "Catherine wondered what Guilleme was talking about."
    "But it didn't seem like he wanted to discuss it further."
    "When Guilleme started to calm down, Catherine thought it was best to sleep and ask him about it the next day."
    "But Guilleme spoke again. His voice was low and serious."

    g "Catherine, do you love me?"
    c "With all my heart, Guilleme."
    c "I've loved you for what it seems like my whole life."
    "The candle flickered."


    scene bg black 
    "Guilleme slipped his hands on Catherine's hair and gently pushed her face towards his."
    scene bg guilbednorm
    "She closed her eyes and let the sensations of his lips take her."
    "His mouth left sweet traces on her skin."
    "As if washing away her sins, blessing her, anointing her."
    "Catherine tasted salt in his kiss, like the taste of tears."
    "She wanted to take away all his sorrows."
    "Guilleme held her tightly, longingly. She drowned herself in his embrace."
    stop music fadeout 2.0
    "His palm caressed her neck as he kissed her, sliding down her arm and the curve of her waist."
    "His fingers tugged gently on her skin."
    "Catherine darted her tongue inside his mouth, and Guilleme answered it with his own."
    "She wanted his every kiss. She felt pleasure to know he was hers."
    "Her hands ran up and down his back as their kisses grew heavier."
    if persistent.adult:        
        "She felt him get excited, and she moved her hand between his legs."
    "Guilleme broke away."
    g "Cath..."
    g "L-Let's stop..."
    g "...You're tired."
###SEXY TIMES! WOOH
    "Catherine looked into his eyes and saw he wanted her despite his protests."
    "After the events of that night, there was a despair in Catherine that longed to be quenched."
    "It was a selfish atonement, perhaps, a hunger for self-worth."
    "She ran her tongue over his lips."
    c "I want this."
    g "Cath--"
    if persistent.adult:
        "Catherine straddled him, dipping her head and plunging her tongue deep into his mouth."
    else:
        "Catherine sat up beside him, massaging his shoulders and neck."
        "She dipped her head and gave him a long, deep kiss."
    "She opened his shirt, nibbling on his ear as she did."
    if persistent.adult:
        "She could feel his manhood alive on her thigh."
        "She moved her hips. A distraught moan left his throat."
        "She bit her lip coyly."
        "It made her want to do more."
    "The clench of his jaw."
    "His aroused breath."
    "The cord of his neck."
    "They were her little trophies, her bliss."
    "Catherine pulled his shirt free."
    if persistent.adult:
        "She traced a finger down his bare stomach, keeping the rhythm on her hips."
        "He opened his mouth, his eyes fluttering."
    else:
        "She traced a finger down his bare stomach."   
    "She watched in ecstacy as he bit his lip." 
    "To know that he couldn't resist her made her swell with pride."
    if persistent.adult:
        "Guilleme grinded with her."
        "He began to answer her passion with his own energy."
    "Guilleme sat up on the bed, finally reaching for her, finally giving in."
    "It felt like a victory to her."
    scene bg guilbeddark
    scene bg gcsexay
    play music "sfx/darksexy.ogg" fadein 5.0
    "Guilleme grabbed her neck and pulled her face to him."
    "His tongue bore deeply into her."
    "Catherine pulled on his hair, surprised at his sudden intensity."
    "Heat ran through her body."
    "She savored his dominance."
    "His lips ran down her neck to her chest."
    scene bg guilbeddark
    if persistent.adult:
        scene bg black
        "He sucked on her collarbone while working the buttons on her blouse."
        "He slipped the garment down with his teeth and kissed the bare skin experimentally."
    "Every nerve felt tender."
    "Every length of skin felt raw."
    "It was a reminder, an awareness that her flesh was a living thing."
    if persistent.adult:
        scene bg gcsexay2
        "There was a build up of tension as he squeezed her breast, planting soft, tiny kisses on its fullness."
        "His hands hovered near her crotch. A stray finger would brush her sensitive spots, almost innocently."
        "It drove her mad."
        "He was teasing her, studying her reactions with every touch."
        "Catherine drew a sharp breath as Guilleme sucked on her nipple."
        "His tongue played with it until it was hard and pert."
        "Catherine felt like a melting candle."
        "Hot and ablaze. Dripping, thawing in her own heat."
        "Her heart began to pace in time with their kisses."
        "Growing steadily heavier, beating louder."
        "From sweet affection to wanton lust."
    else:
        scene bg guilbeddark
        "Tension built up in her insides."
        "Guilleme's breath tickled her ear."
    "He whispered her name, and it sent a violent tremor throughout her skin."
    "It would start in her torso, surging through her, startling the roots of her hair."
    "Her throat made short, hurt sounds."
    if persistent.adult:
        scene bg guilbeddark
    "She would usually stop here."
    "An irksome apathy would take hold of her, and she would stop."
    "Now--"
    "This wasn't like the other times."
    "Catherine felt a hot throbbing at the pit of her stomach."
    "A clench in her body wound her up tighter and tighter, putting her in danger of release."
    "This was {i}different{/i}."
    "This was--"
    g "Do you love me, Catherine?"
    c "Guilleme, I--"
    "Her voice came out throaty and thick."
    "Guilleme laid her down on the bed."
    if persistent.adult:
        scene bg gcneckiss
        "His finger slipped easily inside her, the sensation smooth like silk."
        "She felt him moving around inside, pressing on her walls experimentally."
        "It didn't take long for him to find her weakness."
        "He was surprisingly, worryingly adept."
        "Catherine squirmed. She didn't have time to marvel at his expertise."     
        "His left hand massaged her breasts, while the other tickled the lips of her opening."
        "His little finger petted her other hole."
        "Guilleme's lips ran down her shoulder."
        "She barely noticed him slipping another finger inside."
        "When she did, her mind went white for a few seconds."
        "A sharp breath, then a sigh."
        "Her hips were moving on their own while their tongues flickered and danced."
        "Another heart seemed to beat and throb furiously in her groin."
        "She felt for him. She found his shaft stiff under his trousers."
        "She squeezed his stiffness, eager for its girth."
        "Cloth against flesh. Soft against hard."
        "Lips and teeth. Spit and sweat."
        "Their bodies began to rock together. Their breaths were hot and audible."
        "Guilleme dug his tongue on the hollow of her neck."
        "Catherine whined."
    else:
        scene bg guilbeddark
        "Guilleme dug his tongue on the hollow of her neck as his hands explored her."
    "The soft sounds returned to her lips, but Guilleme covered them with his mouth."
    "Her voice echoed in their heads."
    "She wanted to scream, and the scream would come from very deep."

    if persistent.adult:
        scene bg guilbeddark
    g "Do you love me?"
    c "Oh God--"
    c "Oh God, I love you--"
    "She said in an urgent, desperate frenzy."
    if persistent.adult:
        "In and out his fingers went, each time touching her places."
        "With every movement, he seemed to steal her breath."
        "Faster now."
        "Then she twitched and something snapped inside of her."
        "Her toes curled, and a squeal escaped through her nose."
    else:    
        "A high pitched sob escaped her mouth as something snapped inside her."
    "Catherine opened her eyes."
    scene bg gscary 
    "She caught something alarming as she stared up at him."
    "He didn't look like Guilleme in the shadows unlicked by candlelight."
    "His features were the same. His eyes were in the same place."
    "His nose and lips were the same shape."
    "But this man was a stranger."
    "He did not care for her, like how a snake didn't care for its prey."
    "For a brief second she was afraid."
    "A tiny voice told her to run away, but that voice was washed away by a wave of carnal desire."
    "The stranger grinned at Catherine."
    bg "\"{i}Mine.\"{/i}"
    scene bg guilbeddark
    "Faster now, deeper his kisses went, as if reaching for something inside her."
    "His weight on her body excited her, but it also felt like a prison."
    scene bg black with None
    ra "run rabbit!"
    #show text "{=iloveu}Run, rabbit!{/iloveu}"
    #show text "{=iloveu}Run, rabbit, run!{/iloveu}"
    ra "run, rabbit, run!"
    scene bg guilbeddark with None
    "Catherine viciously devoured his lips."
    "Her hands cruised south, kneading and clutching greedily. Her legs draped around his waist."       
    "A force overtook her."
    "A hunger."
    scene bg black with None

    #show text "{=iloveu}here comes the farmer's gun{/iloveu}"
    ra "here comes the farmer's gun!"
    scene bg guilbeddark with None
    "She tried to ignore the growing coldness in Guilleme's eyes."
    "She tried to ignore the way her body moved on its own."
    scene bg black with None
    #show text "{=iloveu}Run, rabbit!{/iloveu}"
    #show text "{=iloveu}Run, rabbit, run!{/iloveu}"
    ra "run, rabbit!"
    ra "run, rabbit, run!"
    scene bg guilbeddark with None
    "Her hands found the clasps of his trousers, and she undid them."
    "Quickly, now."
    "Quickly."
    if persistent.adult:
        "She clutched his hardness, moving her hand up and down."
        "Catherine's mouth salivated."
    "He bit on her shoulder."
    "She felt more of his teeth than his lips on her body."
    "Catherine scolded herself for being aroused."
    "Her mounting terror only served to aggravate her urges."
    "She wanted this."
    "{i}I want this...{/i}"
    "She was hungry."
    "{i}I am hungry.{/i}"
    "She heard the man snicker."
    scene bg black with None
    #show text "{=iloveu}He wants his farmer's pie!{/iloveu}"
    #show text "{=iloveu}So don't stand idly by!{/iloveu}"
    #show text "{=iloveu}Run, rabbit, run!{/iloveu}"
    ra "he wants his farmer's pie!"
    ra "so don't stand idly by!"
    ra "{size=70}run, rabbit, run!{/size}"
    scene bg guilbeddark with None
    if persistent.adult:
        "He entered her without warning."
    else:
        "He pulled her neck back with a jolt, exposing her bare neck."
        "His tongue slid down, as if tasting her."
    "Catherine gasped."
    "The shiver was from both pleasure and fear. A dangerous mix."
    "...But it was {i}cruel.{/i}"
    "There was no warmth."
    "Just cold, hard greed."
    if persistent.adult:   
        "And yet, she couldn't help but want him. She pushed her hips to move with him."
        "She wanted to please him."
        "Slowly at first, savoring the warmth of this new territory."
        "Then faster, keeping a steady pace."
        "Catherine's voice kept in time, her breaths were high and hot."
    else:
        "And yet, she couldn't help but want him."
        "She wanted to please him."
    scene bg black    
    "With their every movement, Catherine felt her energy wither away."
    "A heady, nauseous feeling of malady clawed at her."
    "What was missing?"
    "What was taken away?"
    "She didn't know what was gone until it was."
    "The final scream of protest died in her mind, the last that was left of her lucidity."
    "The urge to escape left."
    "No more reasons to stop."
    "Catherine moaned."
    "{i}Stop?{/i}"
    "{i}N-No! No! I must not stop. Why did I even think that?!{/i}"
    "What if he'd hate her?!"
    "It was an agonizing thought."
    "She had to give him more."
    "{i}More.{/i}"
    "His eyes observed her with cold amusement."
    "Catherine touched his chest in reverence."
    "His eyes were cold, but his body was like fire."
    scene bg cupidsexay with Dissolve (3.0, alpha=True)
    "In her mind's eye, he had started to become something else."
    "A winged creature engulfed in flame."
    "Both hot and cold and magnificent."
    "Both beautiful and terrible."
    "Both dark and light."
    "{i}A god.{/i}"
    scene bg black
    "At times, she would be on the bed with a man she might remember she once loved."
    show cupidwalls
    "Other times, she would be floating, suspended on a dark chasm of flesh."
    "There was a creature with her, somebody she both loathed and adored."
    "Sometimes there were two people."
    "Sometimes there was only him."
    "{i}Only him.{/i}"
    "The woman called Catherine didn't exist."
    "She was merely an extension of his mind."
    "Soon all of her would be gone, little by little disintegrating to be a part of him forever."
    if persistent.adult:
        "Catherine screamed."
        "She came again with that thought."
    "{i}O-Oh, bliss.{/i}"
    "She was prepared to give everything to him."
    "It didn't even seem a worthy sacrifice to lay at his feet."
    "But no, all he asked for was her heart."
    "That small, pathetic thing."
    "It had always been his, anyway."
    "She gave it gleefully to the ruler of hearts."
    "He was so generous and considerate."
    "Benevolent."
    "{i}Fair.{/i}"
    if persistent.adult:
        "She savored his fullness inside her body."
    "She worshipped him."
    "He was her god."
    "{i}Please want me.{/i}"
    "{i}Please find me pretty.{/i}"
    "She craved his love above anything else."
    "Above fear and confusion."
    "Above the mourning at something precious lost."
    "{i}Love me, please.{/i}"
    "{i}Love me.{/i}"
    "She begged."
    "{i}I'll do anything for you.{/i}"
    bg "{i}Anything?{/i}"
    "His lips did not move, save for a smile."
    "The words simply dropped in her head, echoed, and took root."
    "Catherine's eyes lost their glimmer."
    "{i}A-Anything...{/i}"
    bg "Then tell me again."
    bg "I want to hear it."
    $renpy.pause(delay=None)
    bg "{i}Do you love me, Catherine?{/i}"
    show heat
    "{i}I...{/i}"
    "Her name on his lips was the only reminder of her former self."
    "{i}I do!{/i}"
    "{i}I-I love you!{/i}"
    "{i}I love you so much!{/i}"
    if persistent.adult:
        "With these words, she felt him stiffen inside her."
        "He moved faster, aroused by her devotion to him."
    "A wave of fire burnt her lips as their mouths entwined."
    "His passion heightened. His back arched."
    "Sweat beaded on his forehead and traced his temple."
    "What a wondrous sight."
    "He was ice beginning to thaw. A sun on the verge of eclipse."
    "His coldness replaced by a radiating heat that melded and fastened her to him like fire with metal."
    if persistent.adult:
        "She felt another orgasm threaten her insides."
    bg "{i}Really? Do you really love me?{/i}"
    "{i}...Yes!{/i}"
    "She screamed."
    "{i}...Y-Yes.{/i}"
    "The candle fizzled out."
    scene bg black with None
    "Beneath the depths of her hazy mind, she was relieved she didn't have to look at his face."

    $renpy.pause(delay=None)
    show pulse
    bg "She tastes just like the richest chocolate."
    bg "The finest wine."
    bg "I can't stop."
    bg "My whole body shivers with the taste of her."
    bg "Her breath on my neck."
    bg "Her fingers scratching at my back."
    if persistent.adult:
        bg "The sounds she makes as I push into her."
    bg "Her lust gives me sustenance to move faster."
    bg "To devour her faster."
    hide pulse with None
    gi "Stop."
    show pulse
    bg "I knew waiting so long would be worth it."
    bg "I have been her lover for years."
    bg "And this flavour is divine."
    bg "My head spins."
    bg "My appetite swells."
    bg "I can't stop."
    if persistent.adult:
        bg "I bind her hands into a tight grip, push them above her head."
        bg "Her legs squeeze my waist."
    bg "I can feel her excitement mounting with her helplessness."
    bg "I lick my lips in delight."
    bg "I haven't breathed so deeply for a long time."
    hide pulse with None
    gi "You're taking too much."
    show pulse
    bg "Her love is exquisite."
    bg "It is laced with anger."
    bg "Reverence."
    bg "Disappointment."
    bg "Pain."
    bg "{i}Memories.{/i}"

    bg "All different relishes and morsels melding into one."
    hide pulse with None
    gi "Stop it!"
    show pulse 
    bg "Her love is a delicacy."
    hide pulse
    gi "You're destroying her!"
    show pulse
    bg "I can't stop myself."
    bg "I haven't tasted this kind of love for so long."
    bg "Flirtations and physical attraction can only get me by for so long."
    hide pulse with None
    gi "I was going to wait!"
    show pulse
    bg "There is a waning in her love."
    bg "Confusion. Doubt?"
    bg "But that helping of guilt tinged the flavor perfectly."
    bg "I must feed now."
    bg "Her love is the most perfect tonight."
    bg "My body wants her."
    bg "I couldn't stop now even if I wanted to."
    hide pulse with None
    gi "Liar."
    show pulse
    bg "..."
    bg "And I almost let you escape."
    hide pulse with None
    gi "To save her."
    show pulse
    bg "I almost ran away."
    hide pulse with None
    gi "I love her!"
    show pulse
    bg "I love her."
    hide pulse with None
    gi "And tomorrow?"
    show pulse
    bg "Maybe--"
    hide pulse with None
    gi "What will become of her?"
    show pulse
    bg "I will find another."
    bg "...Next time."
    bg "Something insignificant."
    bg "I want to relish this taste a bit more."
    hide pulse with None
    gi "No!"
    gi "{size=35}{i}NO!{/i}{/size}"
    show pulse
    if persistent.adult:
        bg "The mounting pleasure in my bones clamps on my groin."
        bg "The numbness spreads to my stomach."
        bg "It is almost painful."
        bg "It goads me to increase my rhythm, and she follows my lead."
        bg "Good girl."
        bg "{i}Good girl.{/i}"
    bg "With every move, I feel her love osmose into my other mouth."
    bg "She clings to me, her moans louder, her bare chest glistens with sweat."
    bg "She is beautiful."
    bg "..."
    bg "I-It won't be long now."
    bg "A final drawing of breath."
    bg "Do you love me, Catherine?"
    bg "Give me all your love."
    bg "All of it."
    bg "Give it to me."
    bg "I want it all."    
    bg "It's mine."
    bg "{i}Mine{/i}."
    bg "Catherine."
    bg "Give me more."
    bg "I want more."
    bg "More."
    play sound "sfx/exhale.ogg"
    stop music fadeout 2.0
    hide pulse
    bg "{i}{k=40}M{w=0.1}O{w=0.1}R{w=0.1}E{w=0.1}{/k}{/i}"


    $renpy.pause(delay=None)

##CATHERINE DOWNFALL##
    scene bg hallway     
    show rn sad 
    "Rosa stood in front of the door to Catherine's room, her hand raised to knock."
    show rn dep 
    "She hesitated."
    #"Doubt was creeping into her mind like a spider crawling on a wall."
    show rn shyblush 
    "That night..."
    "That night Catherine and her kissed..."
    show rn depblush 
    "The sweet feelings mixed with the horrid feeling of hunger. It tainted it grossly, making Rosa feel sick and confused."
    r "W-What happened?"
    "She didn't know what it could've been, but it was both familiar and utterly alien, like an instinct."
    show rn shyblush 
    "A shiver ran down her spine at the memory."
    show rn dep
    "But before that, she {i}must{/i} confront Catherine first."
    r "She's avoiding me, isn't she?"
    "She hadn't seen Catherine for a few days since that night."
    "She had been spending a lot of her time alone, locked away in her room."
    "Whenever Rosa saw her in the Château, she would excuse herself and leave."    
    "Rosa never got the courage to push the issue."
    "But days had passed, and Catherine's behaviour began to worry her even more."
    
    call cath from _call_cath
    

    show rn dep 
    r "..."
    m "No matter."
    m "She's never going to love you like mother does."
    m "Like all of the others, she's going to leave you in the end, and then you're all alone."
    m "Only Mother will stay with you forever and love you."
    m "So be a good child and listen to what I tell you."
    

    "Rosa bit her lower lip."
    "This was all her fault, wasn't it?"
    show rn hmp 
    "She needed to make it right."
    "If Rosa talked to her properly, she was sure they would come to an understanding."
    "She had to explain to her--"
    "What, exactly?"
    show rn depblush 
    "They had both been drunk and the kisses didn't mean anything?"
    "Her stomach churned at this thought."
    show rn sad
    "In the end, it didn't matter what Rosa wanted."
    show rn dep
    "Catherine obviously regretted what had happened."
    show rn hmp 
    "She didn't want to lose her friend because of a drunken mistake."
    "Rosa gently knocked on Catherine's door."
    
    show rn huh 
    play sound "sfx/knock.ogg"
    r "Catherine? May I come in?"
    show rn sad 
    r "Please, Catherine. I'm sorry for the mess, but can we talk?"
    
    show rn hmp 
    "Rosa waited for an answer."
    "None came."
    "Rosa turned the handle slowly and entered."
    play sound "sfx/churchdoor.ogg"
    play music "sfx/scary.ogg" fadein 2.0
    scene bg cathroomdark with slowdissolve
    "Usually, Catherine's room was brightly lit."
    "The windows let in a fresh breeze, often carrying the sweet smell of flowers in spring."
    "Right now, however, the curtains were drawn closed."
    "The few candles burning on a desk weren't enough to banish the darkness completely."

    play sound "sfx/scrape3.ogg"
    scene bg cathcrazy with slowdissolve
    "The air hung heavy in the room."
    "Catherine didn't turn around when the door opened."

    "She just stood there, unmoving, in front of a wall."
    play sound "sfx/scrape2.ogg"
    "The sounds of something scratching along a rough surface filled the air."

    "Rosa felt a shiver run down her spine at this sound, and her muscles tensed instinctively."
    "She approached Catherine slowly and apprehensively."
    play sound "sfx/scrape.ogg"     
    "When she came closer, she could hear that Catherine was whispering the same few words, over and over again."
    play sound "sfx/scrape2.ogg"
    c "He loves me...."
    play sound "sfx/scrape3.ogg"
    c "He loves me not..."
    "Catherine giggled."
    play sound "sfx/scrape4.ogg"
    c "He loves me...!"
    play sound "sfx/scrape2.ogg"
    c "He loves me not..."

    
    r "Catherine? Are you alright?"
    
    "Rosa stepped next to Catherine and peered at her outstretched hand."
    play sound "sfx/scrape.ogg"
    "In the dim light, it took a moment for her to make sense of what she saw."
    if persistent.adult:
        scene bg cathscratch with slowdissolve
    else:
        scene bg cathscratchsafe with slowdissolve
    "Catherine was scratching at the wall."
    "The damage she had done to the wall was nothing compared to what she had done to her fingers."
    if persistent.adult:
        "They were dripping with blood from where her skin was cracked and peeled back."
    
    r "Cath--?"
    r "Oh my God, Catherine! Stop!"
    scene bg cathroomdark 
    show rn freaked at nearright 
    show cs normal at right 
    "Rosa's guts twisted horribly."
    "She grabbed Catherine's shoulder to turn her around, away from the wall."
    "She blinked a couple of times before finally reacting to Rosa's presence."
    show cs cry at right 
    "Tears welled up in Catherine's bloodshot eyes at the sight of her friend, spilling over her pale cheeks and chapped lips."
    "She held on tightly to Rosa and started sobbing uncontrollably."
    show rn scared at nearright 
    r "Cath! What's going on?"
    r "Why are you hurting yourself?"   
    if persistent.adult:
        "Catherine tried to pull herself together as best she could, wiping her nose on the sleeve of her bloody dress."
    else:
        "Catherine tried to pull herself together as best she could, wiping her nose on the sleeve of her soiled dress."
    "It was heartwrenching to look at the mess that her friend had become."
    
    show cs crydesp at right 
    c "Oh, Rosa, you need to help me!"
    c "You need to protect me from him!"
    c "Don't let him touch me!"
    r "Who--?"
    r "Let him what? Why do you need me to protect you?"
    
    show cs cry at right 
    "Suddenly, Catherine shushed her, a finger to her lips and with a scared expression on her face."
    "She leaned an ear towards the door and listened intensely for a moment."
    
    show cs crylaugh at right 
    c "Oh, he's here?"
    
    "The scared expression turned into manic and frightening glee."
    c "I think he's coming!"
    show cs crazylaugh at right 
    c "Guilleme, honey!"
    c "Guilleme, I love you!"
    
    show cs cry at right 
    "After yelling the last words, Catherine started sobbing again, with more tears streaming down her face."
    show cs crazylaugh at right 
    "Before Rosa could try to console her, however, her sobs faded into hysterical laughter."
    "It barely left time for her to gasp for breath."
    
    show cs crylaugh at right 
    c "Oh, Guilleme, I love the way you pull me close to hug me!"
    c "A-And how kind you are to everyone you meet--"
    c "And your eyes-- your eyes--"
    
    g "What's going on here?"
    show gn angry at left 
    "Guilleme stood in the door, frowning."
    show gn shock at left 
    "His eyes wandered across the room and caught sight of Catherine."
    "His face froze in shock."
    
    #show Guilleme's sprite with a shocked expression
    #show Catherine's sprite with an angry expression
    
    show cs angry at right 
    "Catherine stared wide-eyed for a second, then she snarled at him like a ferocious animal."
    
    c "You bastard! Get out of my room!"
    c "Get lost!"
    show rn freaked at nearright     
    "She stormed over to the desk and grabbed a letter opener from the table."
    "With this weapon in a firm grip and malice in her eyes, she rushed to Guilleme."
    
    c "Don't you dare show your face to me!"
    play sound "sfx/runshort.ogg"
    r "Catherine! No!"



    scene bg black with flashblood
    play sound "sfx/knifeslash.ogg"

    "The knife plunged into Guilleme's arm."
    "Blood quickly stained his sleeve red."
    "But Catherine only recoiled to strike back, with no hint of stopping."
    r "Oh my God!"
    g "Catherine!"
    scene bg cathroomdark
    play sound "sfx/bigcrash.ogg"
    "They wrestled for a moment until Guilleme was able to grab Catherine's hand."
    "She dropped the letter opener and slumped to the floor, sobbing uncontrollably."
    "Rosa quickly picked up the blade and stepped out of reach."
    "When she turned around again, Guilleme had already pulled Catherine into a tight embrace."
    "Between her sobs and hiccups, Rosa could hear her apologizing."
    
    #show Catherine's sprite with a sad expression
    
    c "Oh god, I'm so sorry, Guilleme."
    c "What--"
    c "I'm so sorry. Do you love me?"
    c "Please, Guilleme, do you love me?"
    
    "She repeated the question over and over again, no matter how many times Guilleme reassured her."
    "It was probably a good idea to find something to calm her down."
    "Rosa didn't feel completely at ease doing so, but she left her friend alone with the Marquis for a few minutes."
    "Later, she returned with a glass of water laced with valerian root."
    "Guilleme had already coaxed Catherine to lie down on her bed, while Rosa helped her drink the nightcap."
    "They watched her in silence as she drifted into a fitful sleep."
    
    "Guilleme and Rosa left the room."
    
    #remove Catherine's sprite
    #show Guilleme's sprite with a concerned expression
    #show Rosa's sprite with a concerned expression
    
    play sound "sfx/doorslam.ogg"
    stop music 
    scene bg hallway 
    # "Outside, she closed the door and folded her arms in front of her chest."
    #"Mother was shouting angrily about the man in front of her being to blame for Catherine's state ... as well as her friend."
    
    show rn hmp 
    show gn serious at left 
    "They didn't speak for a while, both still dazed and shocked by the turn of events."
    r "..."
    r "How is your arm?"
    "Guilleme hid the injured arm away from view."

    show gn angrylookdown at left 
    g "..."
    g "Fine."
    g "Just a scratch."
    
    "The bleeding hadn't stopped yet. Rosa could tell the cut was deeper than Guilleme let on."
    
    show rn sad 
    r "What is happening? What has gotten into Catherine?"
    show gn think at left 
    "Guilleme just shrugged with a cold expression of worry on his face."
    g "I wish I knew, Rosa. The state she is in scares me, to be honest."
    g "It might be an onset of an episode waiting to happen."
    g "Like her sister before--"
 
    show rn angry 
    "Rosa's mouth tightened."
    show gn serious at left   
    r "How dare you say that! She is not crazy!"
    show gn angrylookdown at left     
    g "..."
    
    show rn fuming 
    "Rosa searched his face for traces of a lie, but it was like a mask contorted by worry."
    "She couldn't tell whether he was lying or telling the truth."
    
    show rn angry 
    r "Did you know what she said to me?"
    r "She asked me to protect her from you."
    r "What did you do to her, Guilleme?"
    r "Did you hurt her!?"
    show gn annoyedtalk at left 
    show rn fuming 
    g "You know I wouldn't."
    show gn think at left
    g "I didn't do anything."
    show gn annoyedtalk at left 
    g "All I know is that she is unwell. And I am somehow the target of her psychotic state."
    g "That's it."

    show gn serious at left   
    show rn angry     
    r "But why--?"
    show gn think at left 
    show rn fuming 
    g "Stop."
    show gn annoyedtalk at left 
    g "Stop it, Rosa."
    g "It hurts me too, seeing her like this."
    g "Please stop questioning me further."
    show gn serious at left 
    g "I'm going to call for a physician."
    show gn angrylookdown at left 
    g "Please stay with her in the meantime."
    g "See that she... doesn't harm herself again."
    
    show gn serious at left 
    "For a moment, he met her eyes."
    show gn angrylookdown at left    
    
    "Before she could say more, however, he turned around and left."
    hide gn angrylookdown 
    r "..."
    m "See if his pants have caught fire yet, child."
    r "..."
    
    "There was nothing she could do about him for now."
    "Rosa left to get a bowl of fresh water and a towel to tend to Catherine's fingers."
    
    scene bg bedside 
    play music "sfx/cathsfinal.ogg" fadein 2.0
    "Catherine had an uneasy sleep while Rosa cleaned her wounds as best as she could."
    "She muttered, squealed, and whimpered like a child."
    "It seemed that she was having a nightmare, but Rosa didn't dare wake her before the physician arrived."
    "Instead, she stroked her hair, told her that everything would be alright."
    "She tried to appease the growing confusion of voices in her head."
    "What had happened between Catherine and Guilleme?"
    "Their relationship was often erratic, but Rosa dismissed the possibility that this was one of their usual fights."
    "Rosa remembered Catherine's face, filled with utter spite at the man."
    "She had never seen that much hatred in Catherine."
    
    "After a few minutes, Catherine's eyelids fluttered open."
    "She looked around with some confusion, then her gaze settled on Rosa."

    
    "Tears welled up in her eyes."
    c "R-Rosa--"
    "Rosa held her outstretched hand. Her heart broke when she saw Catherine wince."
    c "Oh, Rosa, I'm so scared."
    c "Everything is such a mess."
    r "It's going to be alright, Cath. Don't worry now, just try to sleep some more."
    c "No, you don't understand!"
    
    "Catherine tried to sit up, but Rosa pushed her down gently."
    r "You need rest, Cath--"
    c "I hate him!"
    c "This is all his fault!"
    "She sniffed, but settled down on her pillow once more."
    "When she spoke again, it was in a whisper."
    c "Rosa, I..."
    "She chewed on her dry, chapped lips for a moment, as if she couldn't get the words out."
    c "I don't think I love him anymore!"
    r "What?"
    
    "A dry sob escaped her, followed by tears rolling down her cheeks."
    "Had Catherine really just said that?"
    
    c "But I don't understand this!"
    c "When... when I think of him, I..."
    "Her voice cracked."
    "She shuddered under the blanket like an ill breeze had just sprung up in the room."
    
    c "It's like bugs are crawling under my skin!"
    c "I can't bear to look at him anymore, I just can't!"
    c "I can't even say his name--"
    r "Why? Do you remember when exactly you started feeling this way?"
    c "T-That night..."
    "Rosa winced."
    "Catherine covered her face with her hands."
    c "It was a horrible night."
    r "..."
    "Rosa's chest hurt."
    "Was this her fault?"
    "She didn't know what she had done. But didn't she do something to her...?"
    r "I-I'm sorry."
    "Catherine went on like she hadn't heard her."
    c "I went to his room."
    c "We spent the night together."
    c "..."
    "Rosa waited for Catherine to continue, but the girl stared blankly."
    "She just stopped speaking, as if forgetting she ever spoke at all."
    r "Cath."
    r "Did he hurt you that night?"
    c "N-No."
    c "Maybe?"
    c "..."
    "Catherine shook her head."
    c "I don't know!"
    "She grabbed her head and sobbed."
    "The grip on Rosa's heart tightened."
    
    c "How can this be?"
    
    "Her eyes drowned in tears."
    c "I love him Rosa, don't I?"
    c "I--I... I remember everything..."
    c "I love him. I know I do..."
    c "I'm {i}sure{/i} I do!"
    c "But I hate him too, to the very core."
    c "I want to hurt him and punish him."
    c "...For something..."
    c "I want to snuff out the breath from his throat."
    c "But sometimes I..."
    "Catherine's eyes went blank."
    c "I just don't care for him at all."
    c "Sometimes..."
    c "I feel nothing."
    c "Nothing at all."
    c "..."
    c "...And that scares me more."
    
    "She laid on the bed, quiet now, letting the tears flow out of her eyes without wiping them."
    c "I--I'm going mad, Rosa."
    r "Catherine..."
    c "I am, aren't I?!"
    c "Like my sister?!"
    c "L-Like my mother..."
    c "It runs in our blood!"
    c "They said I am a child of a madwoman!"
    c "They said I'm going to turn out exactly like her!"
   
    "Rosa stroked her hair and tried her best to soothe her, saying that everything would be alright."
    "They were empty words, but she didn't know what else to say."
    "She wanted them to be true so badly, for her friend's sake as well as her own."
    "Was Guilleme really the cause of Catherine's confusion and pain?"
    "Pangs of guilt pricked her like tiny needles."
    "Or was this her fault?"
    
    m "Rubbish! You fool!"
    m "This is all his fault! I can feel it!"
    m "We must get to the bottom of this."
    r "..."
    r "Y-Yes, mother."
    "Rosa looked down on her best friend and nodded slightly to herself."
    
    r "Everything will be alright, Catherine. I promise."
    "She would make it alright, somehow."
    "She had to."
    
    #fadeout to black background
    scene bg cathroomdark
    "The physician arrived shortly, but he did little to help Catherine."
    "Catherine never regained her personality."
    "She remained moody and irritable, breaking out into fits of hysterical laughter or heartbreaking sobs at seemingly random intervals."
    "Guilleme and Rosa would take turns to tend to her."
    "Her moods fluctuated, her temper uncontrollable."
    "There were times she begged for attention from Guilleme, almost clinging to him in despair, never letting him out of her sight."
    "Other times, she couldn't stand his very presence."
    scene bg black
    "Soon, neither Guilleme nor Rosa could console her anymore."
    "She withdrew entirely from the household."
    "She starved herself, stopped eating, stopped caring for herself."
    "Her manic episodes degraded to long stretches of blank silence."
    "Emptiness ruled her life."
    "Looking at her eyes in those last days, it was like a fire had been snuffed out behind them."
    "Like the star that had been shining through had imploded."
    stop music fadeout 3.0
    $renpy.pause(delay=None)
    if persistent.chap4WasReadBefore   is None:
        $persistent.chap4WasReadBefore  = True
        $persistent.currentLinesRead +=1
    call chap5 from _call_chap5

return

