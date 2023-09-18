#BUILD 11

label chap1:
    $save_name = "chap1: the star & the rose"
    $persistent.Chapter1Unlocked = True
    stop music fadeout 2.0
    stop sound
    scene bg chap01 with slowdissolve
    with Pause(2)
    scene bg black with fade
    scene bg chateausoiree
    play music "sfx/party.ogg" fadein 2.0
    show rv huh at right with None
    "A scruffy young girl in tattered clothes peeked through the open gates of Château du Sommeil, where 
    an afternoon party was being held."
    "People from high class estates strolled around the manicured gardens, chatting and laughing."
    "There were beautiful men and women, clad in silk and velvet, their necks adorned with pearls and jewels."
    "A variety of food was displayed on the tables."
    show rv aww at right
    "The girl stared at the exquisitely arranged plates."
    show rv huh at right
    "She hadn't eaten properly for the past few days."
    
    ##################################### 
    call m01 from _call_m01
    show rv sad at right
    ug "S-Surely we can look around for a bit?"
    ug "It's still a little early..."
    show rv huh at right
    "There was something else that called to her, other than the party itself."
    "She walked to and fro from the gates, peeking at the crowd."
    "Despite Mother's urgings to leave, the girl dared to stay a little longer."
    "{i}Just a tiny glance would be enough.{/i}"
    show rv smileblush at right
    "The girl smiled at the thought of him."
    scene bg rgawe with semidissolve
    "The owner of the château, the Marquis de Gul."
    "His charity was well-known in town."
    "He was kind to the townspeople, from the lowliest beggar to the common townfolk."
    "Parties of the noble-born were usually private affairs, exclusive to the other nobles--"
    "But the Marquis's parties were always open to the public."
    "She would sell roses to the manor, sometimes."
    "Whenever the Marquis was around to meet her, he always handed her food and extra coins."
    "But more than that..."
    scene bg chateausoiree with dissolve
    show rv smileblush at right
    "The fact that the Marquis acknowledged her presence--"
    "--To a poor and forgotten rose girl like her, it was more than she could ask for."
    m "This... {w=0.2}Man you're looking for."
    show rv shy at right
    "The rose girl flinched."
    m "You are enamoured by him?"
    ug "..."
    m "Hmph."
    ##################################### 
    call m02 from _call_m02
    
    
    show rv norm at right   
    "The girl stared at her shoes and looked around for a bit, hoping for a glance before she left."
    show rv huh at right
    "Whenever she was hungry, it seemed her feet always took her here, to him."
    "A habit?"
    
    show rv smile at right     
    "Nevertheless, there was no harm in looking."
    "She would never enter the Marquis' world."
    "The rose girl searched the crowd."
    "There he was, entertaining his guests in the midst of the party."
    "He turned his eyes in her direction and offered a nod."
    show rv huhblush at right
    "Her heart skipped a beat."
    "A light, warm feeling filled her, akin to drinking a cup of hot soup."
    show rv smileblush at right     
    "As he went on to entertain his guests, the rose girl smiled to herself, content to take her leave."
    show rv huh at right
    la "My, is this creature deaf as well as dumb?"
    la2 "Poor thing."
    la "Little girl!"
    
    "A voice called to the rose girl."
    show rv aww at right
    "She gasped. Somebody else had noticed her presence."
    show rv aww at right:
        xalign 1.12
    "She picked up her feet and scuttered to the exit."
    la "No, no, my dear. Poor little creature! Don't run away."
    la3 "Charlotte, she stinks. Don't touch her."
    la2 "Came to crash the party, little urchin? You hungry?"
    show rv sad at right:
        xalign 1.15
    "Her stomach gave a low grumble."
    "She was always hungry, it seemed. No matter how much or how little she ate."
    show rv huh
    "Encouraged by the kindness the Marquis had shown her, the girl teetered towards their table."
    show rv shy at center
    la "What are you selling?"
    la2 "Look at this poor creature."
    la3 "Is she selling roses? These are all ugly ones."
    la3 "But not as appalling as the rags she is covering herself in. Are you trying your best to be this repulsive?"
    la "Don't be mean, Antoinette!"
    la "Perhaps it's the commoner fashion. Don't judge!"
    "They laughed while gawking at her and her wares."
    show rv fear at center
    la "Oh, my. She only has one eye!"
    la2 "{i}Ghastly!{/i}"
    la2 "But strange, isn't it? It's like you can't look away."
    "The other lady nodded her head."
    la "Like those freaks at the carnivals, you mean?"
    la2 "Exactly!"
    show rv shy at center
    la "She's darling in her own dirty, monstrous way."
    la2 "Maybe we can keep it!"
    show rv fear at center
    la2 "Hello, do you want some bread, urchin?"
    show rv hmp at center
    ug "..."
    la2 "Well, speak up!"
    show rv shy at center
    la3 "Maybe her tongue is short. Add that to the list of her sterling qualities."
    ug "..."
    la2 "If you want the food, let us hear you speak."
    show rv sad at center
    ug "...Yes, madame."
    la2 "What?"
    show rv fear at center
    ug "Yes, madame. I would be grateful."
    "One of the ladies clapped in mockery at her reply."
    la3 "Oh, she talks!"
    show rv huh at center
    "The ladies handed her the bread."
    show rv aww at center
    "But it was snatched away before her fingers grazed it."
    
    la2 "Ah, ah!"
    show rv shy at center
    la2 "Not before you dance for us first!"
    la "Oh, make her do a handstand! I've seen a street performer do that once! Quite marvellous!"
    la2 "Now, I'd like to see that!"
    la "This party is getting quite boring."
    show rv fear at center
    la3 "Well, come on, little freak. Dance for your food."
    show rv hmp at center
    "The girl looked at the beautiful, cruel faces of the women."
    "That look on them..."
    "It was familiar."
    "A burning desire to hurt something, simply because they could."
    show rv fear at center
    "Before they touched her and hurt her, they had that look burning in their eyes."
    
    la "Aw, look at what you did, Claudette. She's shivering like a leaf! Poor thing."
    "The lady laughed as she spoke."
    show rv shy at center
    la2 "I didn't do anything. She should be grateful we're even offering her this much."
    
    "The girl faltered."
    
    ug "Mother, please save me."
    ug "Mother..."
    ####################################
    call m03 from _call_m03
    
    u "Hey there!"
    show ck huh at left
    "A child's voice called out from behind her."
    "It belonged to a girl around seven, with chubby cheeks and a curios look in her eyes."
    "She wore an old blue dress, somewhat patched at the corners, but kept clean and tidy."
    "She was not rich, but she had an air as if she owned the ground she stood on."

    la2 "Hm? Another commoner? This party is absolutely teeming with them."
    show ck pout at left
    la3 "The Marquis loves these things. Maybe I should get myself one too."
    la2 "Do you think it is fashionable abroad, in his birth country, I mean?"
    la3 "Persia?"
    la2 "No, no, I heard he was from India."
    la "Isn't he a bastard son of a Greek queen?"
    la3 "Goodness, that was just a rumor!"
    la2 "I could barely pronounce his christian name, though."
    la2 "He really ought to change it to something more acceptable."
    la2 "Who knows what kind of demons he 
    might attract with such a blasphemous name."
    la "Aha! It must be why all these nasty, horrid little creatures flock around him!"
    la3 "Hmm..."
    la3 "Demon or not, I'll forgive him if he kisses my hand."
    "The ladies laughed."
    la "You cheeky tramp! Aren't you shameless!"    
    la3 "Don't lie! We all know why we're here."
    
    "The ladies gossiped among themselves, openly ignoring the girl."
    "The young girl took the slighting with a shrug."
    "She approached the table and asserted her presence."
    show ck talk at left
    u "Whatcha doing?"
    la "They don't take a hint, do they?"
    show ck pout at left 
    la2 "Throw something shiny. It might distract them."
    show ck angry at left 
    u "Hey, you've been holding that bread for a long time."
    show ck pout at left 
    show rv huh at center 
    u "Aren't you gonna give it to her?"
    "She pointed at the shabby rose vendor."
    show rv shy at center 
    la2 "Why do you care? Do you want the bread for yourself?"
    la3 "I know, maybe you should toss the bread and see if they'll fight for it."
    "The ladies laughed again."
    "The girl's brows furrowed in understanding."
    hide ck pout
    show bg chateausoiree
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=3)
    "Next thing everyone knew, she had swiped the bread from the woman's hand."
    show ck happy at nearleft  
    show rv huh

    la "W-What?!"
    la2 "H-How... rude!"
    show ck cheer at nearleft
    la3 "Horrible, filthy girl, give that back!"
    
    "The girl sniffed the piece of bread and nibbled at the surface."
    
    u "Mm. Yummy. It's still warm."
    show ck normal at nearleft
    "She shoved the bread in the urchin's face."
    "The scrumptious scent of bread flooded the rose girl's nose."
    
    u "Lick it. The sugared butter tastes good!"
    show ck cheer at nearleft
    la "No! You devil child! Give that back!"
    
    "The urchin licked it. Sweetness coated her tongue."
    "She stood there, squeezing the taste, wishing it to last."
    show ck happy at nearleft
    show rv happy at center
    "The girl grinned at her, and she couldn't help but grin back."
    show ck normal at nearleft 
    show rv smile at center
    u "Sorry, here you go. It's all yours."
    show ck pout at nearleft
    la3 "Ugh! Disgusting!"
    la "Like we're going to eat anything that's been in your filthy mouths!"
    show ck cheer at nearleft
    u "Wow, so this is ours now? You ladies are so nice."
    
    la2 "Cheeky little brat! I'll have you thrown out of this party! I'll have you--"
    
    show gc norm at right with dissolve
    show ck normal at left with dissolve
    show rv huh at nearleft with dissolve
    "A young man strode to the commotion and the ladies curtsied self-consciously."
    "The rose girl's mouth welled up."
    "A sweet flowery taste filled her tongue, like jasmine tea spiked with wine."
    show rv shyblush at nearleft  
    "The girl swallowed."
    "What a strange effect he had."    
    show gc huh at right 
    g "Ladies."

    la "O-Oh, Lord Guilleme!"
    show gc smile at right
    g "I just came to check in on my lovely guests."
    g "Is everything alright? Are you enjoying yourselves?"

    "The rose girl cowered behind the little girl."
    "One of the ladies flicked her fan with obvious annoyance."
    show ck pout at left
    show rv norm at nearleft 
    la3 "Well, these little beasts have been harassing us."
    la2 "Yes, my Lord."
    la2 "We were just minding our own business when this girl swiped the food off our table."
    la3 "Horrible, simply horrible!"
    "The girl stuck out her tongue at them. One of the ladies wailed childishly."
    show gc huh at right
    
    la "See, look at that!"
    la "It's absolutely monstrous how these children act around adults now."
    la "There is no respect, {i}messire{/i}! I worry for the next generation!"
    show gc smile at right
    la2 "Oh, Charlotte, don't cry!"
    la "We would all breathe a little easier if those children were sent on their way, my Lord."
    la3 "Yes! Who knows what kind of mischief they might be up to."
    #la2 "They might set fire to the tables, you see?"
    show gc huh at right
    g "Oh?"
    show gc norm at right
    la3 "What if they're here to steal our jewelry?"
    la3 "In fact, I think my pocket watch is missing!"
    show gc huh at right
    g "No! How unfortunate."
  
    show gc smirk at right
    la "It is, {i}messire{/i}!"
    la "It's unfortunate how you allow your important guests to be treated this way!"
    la2 "Please deal with these vermins! Throw them out now!"
    show gc smile at right
    g "Oh, my sweet ladies. I am stricken with grief at your misfortunes."
    show gc sad at right
    g "Allow me to offer my heartfelt apologies."
    show gc huh at right
    g "Unfortunately, {i}this child{/i}, is in fact, my important guest today."
    g "Meanwhile, you ladies are, sad to say--"
    show gc smile at right
    show ck normal at left
    g "Mere{w=0.2} gate crashers."
    la "E-Excuse me?"
    show gc smirk at right
    g "Madame Charlotte of Montpellier? I don't remember sending you an invite."
    show gc huh at right
    g "Same for you, Lady Antoinette of Rennes and Lady Claudette of Lyon."
    g "Most people I invited are huge patrons of music. That is why they are here today."
    show gc smile at right
    g "They came to listen to Mademoiselle Catherine Louise Perride."
    show ck cheer at left 
    g "She is the seven-year-old piano prodigy who played for the Queen last summer."
    show rv huh at nearleft
    "The man pointed at the girl busy chewing her half of the bread."
    show ck happy at left
    "The rose girl just stared at the unfolding situation."
    show ck normal at left
    la2 "W-Well... That's--"
    show gc huh at right
    g "But I am sure you were aware of that, yes?"
    la3 "..."
    show gc smile at right
    g "No matter. I am always happy to see you, ladies. It is my pleasure to have you here."
    show gc unamused at right
    g "But I hope you don’t mind giving some of the food away to my townspeople."
    g "That is why I keep my gates open."
    g "My servers are instructed to serve anyone who passes by, not just my guests."
    la "But--"
    show gc smirk at right
    g "Oh, and don't fret, darlings. There will be plenty more food left for {i}you{/i}."

    "The ladies reddened in embarrassment."
    show gc smile at right
    g "Excuse me!"
    
    show rv shyblush at left
    show ck normal at nearleft
    "The Marquis walked up to the two girls."
    "The rose girl's heart beat so fast it made her dizzy."
    "She had never been this close to him."
    "Her stomach tightened in knots as Mother's voice screamed in her ears to leave."
    #"It made her feel a mixture of fear and elation."
    
    g "Miss Catherine. Your father has been looking for you."
    g "It is almost time for your performance."
    
    "The girl looked up at the Marquis and did a little curtsy."
    show ck talk at nearleft
    c "My apologies, Sire. I didn't mean to cause a clatter."
    show gc smirk at right 
    "Guilleme chuckled."
    show ck cheer at nearleft
    g "I saw the whole thing, little miss. You put those ladies in their place."

    show ck pout at nearleft 
    c "They were being mean to her."
    show gc smile at right
    "Guilleme narrowed his eyes at the quiet girl. She hid behind her basket of roses."
    show ck normal at nearleft
    show rv shyblush at left 
    show gc huh at right
    show ck normal at center:
        xalign 0.35
    g "I've seen you before, haven't I?"
    show rv huhblush at left
    "The rose girl nodded and made a curtsy."
    show rv smileblush at left
    
    ug "I-I deliver roses to your house sometimes, Sire."
    show gc huh at right
    g "Hm, yes. I remember!"
    show rv huhblush at left
    "The rose girl blushed."
    show gc smile at right
    show rv shylookdownblush at left
    g "I love your roses, by the way."
    g "They stay fresh longer than they should."
    g "You've tended to them with love."
    show rv smileblush at left
    ug "T-Thank you, Sire."
    show rv huh at left
    g "Do you have a name, young lady?"
    show rv shy at left 
    show ck huh
    ug "..."
    ug "I..."
    ug "erhm.."
    show rv aww at left
    c "What's the matter?"
    show rv shy at left
    ug "..."
    show gc norm at right
    g "It is alright. You don't have to force yourself--"
    show ck happy at center:
        xalign 0.35
    show rv huh at left
    c "Let's call her Rosa!"
    show gc huh at right
    g "Hm?"
    show ck cheer
    c "Rosa. It fits her!"
    show ck normal
    c "I think she forgot her name. Or she lost it."
    show gc smile at right
    "The Marquis nodded."
    #g "A valid point."
    show rv smile at left
    g "Indeed. Names are quite flimsy things."
    g "Are you alright with that, {cps=10} Rosa?{/cps}"
    r "...Yes."
    show ck happy
    c "Come on, Rosa. You'll watch me play, right?"
    show rv huh at left
    r "I..."
    show rv aww at left
    "Her eyes darted from the girl to the Marquis."
    show ck happy
    c "Oh, Lord Gilly doesn't mind!"
    show gc huh at right
    g "Gilly--?"
    show ck cheer
    c "He's really nice to me and my family."
    show ck happy
    c "And he helps the people around town, too. He won't throw you out."
    show gc happy at right
    "The Marquis held his right hand in the air as if swearing an oath."
    g "I won't."
    show gc smile at right 
    c "See? Come on, you're invited now! You're my special guest."
    show ck normal 
    g "There's plenty of food inside too, Rosa. Please help yourself."
    show rv smile at left 
    r "...Thank you, Sire."
    show ck cheer
    c "Rosa is coming! Yay!"
    show ck pout
    "But then, Catherine's cheerful face broke into a frown."
    c "..."
    c "Actually..."
    "The girl looked up to the Marquis."
    c "I... I ran away because I am a bit nervous."
    show gc huh at right
    g "Oh?"
    c "I've only ever played my piano in private gatherings. Inside houses and such..."
    c "Now there's a whole bunch of people..."
    "Catherine scratched her head."
    c "What if I make a mistake? Papa will be very upset."
    show gc smile at right
    "The Marquis knelt in front of Catherine and patted her shoulders reassuringly."
    stop music fadeout 4.0    
    show ck huh
    g "Don't worry, little miss."
    show gc norm at right 
    #g "As long as you put your heart into the keys."
    g "If you play to touch your audience's hearts, any mistake won't matter."
    g "Do you understand?"
    "Catherine stared up at him."
    show ck pout 
    c "Not really."
    show gc smirk at right
    "The man chuckled."
    g "How about this?"
    show gc smile at right
    g "Imagine everyone in the audience is asleep..."
    g "...Except for one."
    g "That one special person is listening to you."
    g "So perform as if you want to make that person smile."
    
    "Guilleme held Catherine's clear, young eyes in his gaze."
    g "Do well, my lady!"
    "He gave her hand a little peck."    
    show gc smirk at right
    "It was covered with sticky sugar and bread crumbs."
    show ck blush
    "Catherine blushed, embarrassed by the state of her fingers."
    show ck pout
    c "Somebody special..."
    c "..."
    "The young man led her to the stage."
    g "Are you ready?"
    show ck cheer
    c "Yes!"
    scene bg chateausoiree 
    "Catherine trudged up the wooden podium and walked towards the middle of the stage."
    "The crowd's chatter died down."
    play sound "sfx/lightapplause.ogg"
    "She curtsied in front of her audience and waved to her father."
    show bg cfirstpiano with slowdissolve
    "She sat down in front of the piano, admiring the cream and ebony keys underneath her fingers."
    "Her own piano was broken and beaten. Father had sold his horse for it."
    "The A3 key never played, and the strings would creak when it was cold."
    "But it never failed her. She knew the keys like they were her own fingers."
    "She whispered to the new piano softly, as if coaxing a beautiful, untamed animal."
    c "Let's be friends, okay?" 
    "She saw Rosa at the far end of the podium, watching her diligently."
    "The Marquis settled in his chair in front of the audience."
    "He gave the girl an encouraging nod."
    c "A song that would make someone smile... huh?"
    "Her face redenned and she broke into a shy grin."
    "There was a renewed vigour in her blood. She could hear the keys calling out to her."
    c "Somebody special..."
    "She placed her fingers on the keys."
    "She began to play."
    play music "sfx/catsfirstperf.ogg"


    $renpy.pause(delay=None, music=True)    
    "At the ring of the first few notes, it became apparent to the audience that this girl was exceptional."
    "Here was a little girl, barely tall enough to reach the pedals of the piano, playing as if she owned it."
    "There were times she'd miss a note or two, but that didn't matter."
    "She played the song whole-heartedly, and everyone could tell it as so."
    #"Her musical skill was far beyond her years."
    "Her skillful fingers caressed the keys as if she was making a flower crown, carefully weaving the petals."
    "She knew the correct way to tie the leaves so they wouldn't tear, like all smart little girls did."
    "As the piano sang under her hands, Catherine disappeared right in front of the audience's eyes."
    "She was just a vision, after all, somebody leading them down a dream."
    "A dream of a garden, the springtime, the shade of a tree on a windy day."
    "The couples in the audience tightened their grip on the hands of their partners."
    "Some closed their eyes and let the music saturate their soul."
    "Sweet memories of youth."
    "A first love."
    "The yawn of a newborn."
    show bg rawe
    "Rosa's eye shone as she stared at Catherine."
    "Her heart was captured by this image of her."
    "A young girl swaying her head to the music, smiling as the notes poured out of her."
    "She couldn't take her eye away from Catherine's glowing face."
    "Was this happiness?"
    "Was this {i}love?{/i}"
    "She looked like she was in love."
    "And she was, wasn't she?"
    "In her innocence, she was still in love with life."
    "In love with her family, with her pets, in love with every new discovery."
    "She was full of hope."
    "It was a bittersweet feeling for Rosa."
    "A happy teardrop rolled down her cheek."
    "She wanted to warm herself in that hope, if she could."
    scene bg chateausoiree 
    "In the audience, Guilleme and Catherine's father sat beside each other."
    show gc smile at right
    show f smile at left 
    g "Sire Perride, your daughter is amazing."
    f "She is, isn't she?"
    show f huh at left
    f "I-I mean, pardon my arrogance, my liege."
    f "I-I am a very proud father, you see?"
    g "No pardon necessary, Sire."
    show f normal at left
    g "Has she found a sponsor yet?"
    f "The Duke of Versailles once spoke to me about it, but we have not made any arrangements."
    show gc huh at right
    g "Then I must steal her away as soon as possible!"
    show f huh at left
    f "Sire?"
    show gc norm at right 
    g "I'd like to be Catherine's primary sponsor, if that is alright with you."
    f "Why, Sire--"
    show gc smile at right 
    g "And to further cement my status, that piano she is playing right now--"
    g "It is hers. I've bought it for her."
    show f upset at left 
    "François' eyes widened in astonishment."
    f "T-That is--!"
    "François gulped."
    show f huh at left
    f "That is beyond generous, Sire!"
    "Guilleme smiled."
    show f normal at left 
    g "I'm aware it's quite bold of me to ask you outright,"
    g "But I felt compelled to grab the opportunity."
    show gc huh at right
    g "After all, the Duke might offer you an extravagant piano plated in gold."
    show gc sad at right 
    show f upset at left
    g "In that case, I have no choice but to humbly concede."
    f "W-What?"
    show gc smirk at right 
    g "I'm kidding. The Duke of Versailles is the worst miser you will ever meet."
    show f eh at left 
    "The men chuckled."
    show gc norm at right
    g "Of course, I shall be paying for her musical tutoring as required."
    show f normal at left 
    g "Along with an ample stipend to accomodate your family."
    show f huh at left 
    f "..."
    show gc huh at right 
    g "Ah, you don't have to look so surprised, Monsieur Perride."
    show f eh at left
    g "Your daughter is a star. Genuises like her only appear once or twice a century."
    show gc smile at right 
    g "There is no doubt in my mind that she will succeed."
    show f smile at left 
    f "Thank you deeply, my liege."
    show gc huh at right 
    g "Let me remind you, this generosity isn't without charge!"
    show gc norm at right
    show f normal at left
    g "Her tutoring will be done at my house. I want to monitor her progress."
    g "Apart from that, I'd very much like Catherine to visit the chateau and play from time to time."
    g "Music is one of my true passions."
    show gc smile at right
    g "Her presence would benefit my mood tenfold."
    show f smile at left 
    f "Of course, Sire! That is a small price to pay for all your offers."
    show gc norm at right
    g "On the contrary, {i}messire{/i}."
    g "You don't have to decide now. Kindly think about it."
    f "Thank you, my lord--Sire Guilleme."
    hide f smile 
    hide gc norm 
    stop music fadeout 5.0
    
    
    "After the performance, Catherine and Rosa went to the Marquis' garden to play."
    "François and Guilleme lingered on their table, sorting out the details of Catherine's further education."
    play music "sfx/waltz.ogg"
    show a normal at left 
    "Émilie Perride wandered about the crowd, searching for a familiar face."
    "She arrived halfway through Catherine's performance, just in time to gush at her little sister's applause."
    "Unfortunately, she couldn't find her father in the crowd."
    "When she finally caught sight of the back of his head, she approached him hastily."
    show a smile at left 
    a "Father, there you are! I've been looking all over for you--"
    show a huh at left
    "Émilie stopped as she saw the man her father was talking to."
    show f normal at center:
        xalign 0.3
        yalign 0.9
    show gc norm at right
    "It was none other than the Marquis himself."
    "She curtsied."
    a "My Lord! Pardon my intrusion! I didn't realize--"

    show gc smile at right 
    "Guilleme smiled at her kindly."
    show a normal at left 
    g "You are free to intrude anytime, my lady. "
    "Émilie smiled back. Just as the rumors said, the Marquis was easy on the eyes."
    g "To whom do I owe the pleasure of your acquaintance?"
    show f eh at center:
        xalign 0.3
    f "This is my eldest daughter, Émilie. Pardon me for not introducing her sooner."
    g "Charmed."
    "Guilleme offered her a seat. Émilie sat down across the man."
    show gc huh at right 
    g "Well, it seems talent {i}and{/i} good looks run in the family."
    show f eh  
    show gc norm at right
    "François scratched his head."
    f "Yes, my daughters are my pride and joy. Thankfully, they both took after their mother."
    show gc huh at right 
    g "Surely not, Monsieur Perride. I see earnest strength in her eyes, that much she has taken after you."
    show gc smile at right
    show a bored at left 
    "Émilie snorted at such cliché words."
    show f eh  
    "Her father was clearly basking in the compliments."
    show gc smile at right     
    "If this really was the famous Guilleme the rumours talked about, then he wasn’t exactly much of a charmer, was he?"
    "He was no trobadour nor was he a poet."
    show f normal
    "She didn’t know what all the fuss was about."
    show a hm at left 
    "The ladies in the house she worked for could not seem to stop talking about this man."
    "Admittedly, there {i}was{/i} something morbidly curious about the way he looked at people."
    "He came off vague and distracted; seemed incapable to offer words beyond what were expected of him."
    #"The only way to engage him, it seems, is if you interest him in the first place."
    show a smile at left 
    a "I'm pleased to have finally met you, Sire."
    a "I've heard a lot about you on my travels."
    show a normal at left 
    show gc smirk at right
    g "All good things, I hope."
    show a proud at left 
    show gc smile at right
    a "{i}Depends on the tabloid, and the day of the week,{/i}" 
    "Émilie thought to herself and chuckled."
    show a normal at left 
    g "You are a governess, I was told? Where do you work?"
    show a smile at left 
    a "With the Dmitri household, Sire."
    show gc huh at right 
    g "Ah yes, I heard you were marrying into the family soon."
    show a huh at left 
    a "Oh, Father. I told you not to tell anybody yet!"
    show f huh 
    f "I didn't! But you know how people talk. Word travels fast!"
    show gc huh at right 
    g "Pardon the comment then, my lady."
    show a smile at left
  
    a "Please."
    show gc smile at right 
    g "Your betrothed is a lucky man, I'm sure."
    scene bg chateausoiree 
    $ nvl_darkbg = True
    nvl clear
    o "The conversation endured through the afternoon."
    nvl clear
    o "Small talk about musical composers and their little town..."
    o "Catherine's musical background, François' students, Émilie's work..."
    nvl clear
    o "Émilie played with her napkin, offering droll opinions on equally droll topics."
    o "All throughout the exchange, Émilie observed the infamous Marquis de Gul."
    nvl clear
    o "This... was him?"
    nvl clear
    o "The audacious, shameless flirt of the royal court?"
    nvl clear
    o "According to rumors, he was able to bed both the widowed Countess of Devonshire {i}and{/i} her daughter!"
    o "...At the same time!"
    nvl clear
    o "And even had a tumultuous relationship with the Prince of Garnet."
    nvl clear
    o "He didn't limit himself to royalty, or so the tabloids said."
    nvl clear
    o "His latest fling was with an English poet--"
    o "--who, they say, almost killed him when he was caught with another man--"
    o "Or woman..."
    nvl clear
    o "Ah... at this point, who knew what was real and what was a blatant lie made up by the newspapers?"
    nvl clear
    o "She had looked forward to meeting him."
    o "And here he was, finally."
    nvl clear
    o "...Talking about sampling the new bakery's crème brûlée."
    o "Émilie sighed."
    nvl clear
    o "She couldn't say she was disappointed, exactly. \n The rumours couldn't {i}all{/i} be true."
    o "But the Marquis was a depressingly normal man."
    nvl clear
    o "{i}Maybe even boring{/i}, Émilie ventured."
    nvl clear
    o "She watched as his gaze flickered across her hair and \nher nose before lazily trailing away."
    nvl clear
    o "How infuriating."
    nvl clear
    o "\"Any moment now!\" she thinks. \n \"Any moment now, he will say something coy!\""
    #nvl clear
    # "He would touch her hand, pull her into a dance."
    #nvl clear
    #o "Attempt to sweep her off her feet."
    #nvl clear
    o  "\"S-Something outrageous!\""
    o "{cps=20}Something...{/cps}"
    #o "Wasn't that why he was popular?"
    nvl clear
    #o "He {i}must{/i} do something!"
    #nvl clear
    o "Shamefully, long have Émilie fantasized about this."
    nvl clear
    o "The infamous Marquis Guilleme \n attempting to woo her, Emilie Perride,"
    o "And she, a reasonable woman, \n would scold him and put him in his place,"
    o "This shameless flirt whom everyone adored."
    nvl clear
    o "That would be a small victory for \nsensible women everywhere."
    nvl clear
    o "But regrettably, the Marquis was nothing but polite."
    o "He did not ogle."
    o "He did not touch unnecessarily."
    o "No audacious gestures or suggestive winks of the eye."
    nvl clear
    o "He would not even look at her for more than two seconds!"
    nvl clear
    o "Maybe she was not pretty enough to flirt with?"
    o "Émilie bit her lip. She shouldn't be thinking that."
    nvl clear
    o "But..."
    
    nvl clear
    show bg black 
    show gc lookdownbig

    o "There were also times that he would quietly look into her eyes when the conversation lulled."
    nvl clear
    show gc seriousbig
    o "When the words spoken were without meaning, their eyes would converse further."
    nvl clear

    show gc sadsmilewhite with Dissolve(1.2, alpha=True)
    o "To Émilie, he'd started to look lonely underneath the facade of caprice."
    nvl clear

    o "He seemed tired of all the gallivanting, the rumors and the numerous flings."
    o "We are all a little lonely, aren't we?"
    nvl clear
    o "Perhaps even he?"
    nvl clear
    o "He invited the family over to his château and \ncommented on how empty the building felt sometimes."
    nvl clear
    o "Music was his guilty pleasure."
    nvl clear
    o "It got him through the cold nights, he said with a sad grin."
    nvl clear
    o "How he wouldn't mind a warm soul to touch."
    $ nvl_darkbg = False
    scene bg black
    "And before she could stop herself--"
    "Émilie had begun to imagine his lips on her neck."
    "On one of those..."
    show bg neckiss with fade
    show bg black
    "Cold..."
    show bg neckiss2 with fade
    show bg black  
    "Nights."
    scene bg chateausoiree
    show a hot at left 
    show gc happy at right
    show f huh:
        xalign 0.3
        yalign 0.9
    with None
    "Émilie shook her head, trying to erase the thoughts in her mind."
    show gc huh at right
    show f eh
    "They were having a perfectly mundane conversation."
    a "W-What is wrong with me..."
    show f normal
    "She didn't know where those thoughts came from."
    show gc happy at right
    "Fortunately, her father didn't seem to notice."
    show gc huh at right  
    g "Miss Émilie, your face is flushed. Are you alright?"
    show gc norm at right
    a "I-I'm fine. J-Just the sun, I suppose."
    show a hot at left  
    #"This was not true, of course."
    show f normal
    #"The afternoon sun had already lost most of its heat."
    show gc huh at right
    g "If you'd like, you can rest inside the chateau."
    g "I'll have someone attend to you."
    a "N-No! That's not necessa--"

    scene bg chateausoiree  
    show f huh at right:
        xalign 0.3
        yalign 0.9
    show ck happy  

    c "Papaa!"
    stop music fadeout 3.0
    show rv norm at nearleft  
    "Catherine came bounding up to the huddle."
    "Émilie sighed gratefully at her sister's distraction."
    "The little girl ran towards François flinging her arms around his torso, chattering happily about gardens and butterflies."
    "A young, ragged girl followed behind her."
    show f normal at right:
        xalign 0.3 
    "Émilie wasn't sure how old the girl was. Her dirty blonde hair hid the left side of her face."
    "You could just see faint traces of scars peeking through."

    "A surge of motherly affection caught hold of her heart."
    a "Hello there, young lady."
    show rv huh at nearleft  
    "The girl looked down at her toes, but smiled shyly back at her."
    a "I see you've made a crown of flowers!"
    a "You look very pretty."      
    play music "sfx/garden.ogg"
    show rv smileblush at nearleft  
    r "Thank you, Miss..."
    r "...Catherine gave it to me."
    show ck cheer  
    c "Sister, this is Rosa. She's really nice!"
    c "She knows the name of all the flowers in Lord Gilly's garden!"
    a "Catherine, there you go again with your silly names."
    show rv huh at nearleft  
    c "Sister! Help me convince Papa to let Rosa stay with us!"
    show f huh
    f "Catherine?"
    show ck awwtalk  
    show f upset at right:
        xalign 0.3  
    c "Papa, please! Please let her stay with us!"
    show rv aww at nearleft  
    c "She doesn't have anywhere to go!"
    show ck awwpout  
    show f normal
    f "Catherine, that is not very nice."
    show f huh
    f "Rosa is a girl."
    f "She is not a kitten you can just pluck from the street and take home like you always do!"# with stray animals!"
    show f eh
    f "Goodness knows we have all the stray cats of France living in our house!"
    show f normal
    show ck awwtalk  
    c "Yes, I know she's not a kitten. I know she's a girl."
    c "But shouldn't we take her home even more so?"
    show f eh
    show ck awwpout  
    "François sighed."
    "Guilleme chuckled under his breath."
    g "Your daughter has some very unique views, Sir Perride."
    show ck pout:
        xalign 0.4
    hide f eh
    c "Well, Lord Gilly, what do you think?"
    show gc huh at right  
    g "...Huh?"
    "Guilleme's face lost his casual bystander look."
    c "You're a Marquis. I'm sure my father would follow your orders, right?"
    show ck awwpout  
    c "Shouldn't we take Rosa home?"
    "Guilleme's brows furrowed at being put on the spot so suddenly."
    show gc bitchface at right  
    "He stole a glance at François, who gave him an imploring look."
    "It was clearly not the first time this conversation happened."
    "Guilleme cleared his throat."
    g "Well, I'm sure it's up to your father since he owns the house."
    g "Your father works hard to clothe and feed you and your sister."
    g "And now, he would have to do that for Rosa too. That would be a burden to your father, right?"
    show ck talk  
    c "I earn money! The queen gave me lots last time!"
    show gc huh at right
    c "Father said you'd give me lots today, too."
    show gc smirk at right
    "François blushed furiously."
    show ck cheer
    f "Catherine!!"
    c "Hehehe!"
    show ck normal
    g "You've given this some thought, I see."
    show ck cheer
    c "Yes, I got it all figured out!"
    "Catherine pumped her fists energetically."
    show ck talk
    show gc huh at right  
    c "Ever since Sister moved out to work, nobody minds the house anymore."
    show ck pout  
    c "I have to wash the dishes every time. Ugh."
    c "Papa's so busy, he's rarely at home. There's always enough food for me."
    show ck cheer
    c "If Rosa stays, then we can play together!"

    show ck talk
    c "She'll wear Sister's old clothes and we'll mind the house when both Sister and Father are away."
    c "She can wash the dishes sometimes. And I'll wash them sometimes."
    show ck normal  
    "Guilleme and François shared a look."
    show ck pout  
    c "And besides, if it were up to me, I'd have people take one girl home in their house and give her food."
    show ck talk  
    c "Girls don't even eat that much."# Not sure about boys."
    #show ck pout  
    #"She thought for a bit."
    #show ck angry  
    #c "But I'm sure it's not too much that people can't take them home too."
    show ck pout  
    c "One time, I ate one whole plate of potatoes and my stomach hurt."
    c "If Rosa was there, I wouldn't have eaten so much."
    c "...Maybe."
    show rv happy at nearleft  
    show gc smirk at right  
    "Guilleme snickered. François rubbed his neck in embarrassment."
    show gc norm at right  
    f "Ahh... Catherine... Please!"
    show rv smile at nearleft  
    a "Father, won't you allow it?"
    "Émilie patted her Father's shoulder, whispering quietly to his ear."
    a "I think Catherine needs a friend. She is always alone ever since I left."
    a "Taking Rosa in wouldn't be much trouble for us financially, yes?"
    a "My new work pays better. I'm sure we can manage."
    show gc huh at right
    g "Well, about that."
    g "Perhaps if Rosa works in my household, it wouldn't be much of a burden to your family, Sire Perride."

    show rv huh at nearleft
    show ck huh
    show gc smile at right
    r "..."
    show ck cheer
    c "Wow! Lord Gilly is awesome!"
    f "Ah!"
    f "That would be a wonderful gesture, Sire."
    show gc huh at right
    g "Not at all!"
    show gc smile at right
    g "It is obvious that Catherine has taken to the girl."
    g "And I am always looking for good and honest workers."
    show rv huhblush at nearleft
    show gc smile at right
    g "Rosa, you don't mind taking care of me from now on, do you?"
    show rv shylookdownblush at nearleft
    r "..."
    show ck normal
#    f "Well, I would love to offer my home to Rosa."
    f "Although if she were to stay with us, her situation still worries me, Sire."
    f "What about her family? Or her friends?"
    show rv shy at nearleft  
    #f "Are we violating any laws, perhaps? I am not even sure."
    show gc smile at right  
    #g "As long as it is consensual, Sire. The details can be smoothed out later."

    "The girl was quiet the whole time. She was looking at her toes, or at Catherine."
    show rv huh at nearleft  
    f "Rosa? Do you have any family? Relatives or friends you stay with?"
    r "..."
    show rv sad at nearleft  
    r "No, Sire."
    show ck awwpout
    show gc norm at right
    r "My mother... died a long time ago."
    show rv norm at nearleft  
    r "But she guides me always."
    show rv close at nearleft  
    r "...So, please don't be compelled to mind me."
    show ck awwtalk:
        xalign 0.35
    c "No! Don't go back to the streets, Rosa!"
    c "It's September! It's going to be really cold soon."
    c "Lord Gilly will even give you work!"
    c "Stay with us!"
    show rv aww at nearleft  
    r "But, Catherine..."
    hide gc smile  
    "François sighed in surrender."
    show f huh:
        xalign 0.55
        yalign 0.9
    f "Alright, alright. She can stay with us."
    show rv huh at nearleft  
    show ck happy  
    r "...!"
    c "Papa!"
    show f normal
    f "But just for tonight. Then we'll see if she wants to stay for longer."
    show f huh
    show ck awwtalk
    c "B-But...!"
    show ck awwpout
    "François held her daughter's shoulders."
    f "See here, Catherine."
    f "You cannot hold people in their place just because you want them there."
    f "Do you understand?"
    show ck pout  
    f "If Rosa wants to leave, she may leave."
    f "You cannot keep her like an object just because you like her."
    g "..."
    show f normal
    g "That is sound advice, Sire Perride."
    c "Yes, Papa, I understand!"
    show ck normal  
    show f smile
    f "Rosa, please make yourself comfortable in our home."
    show ck cheer  
    show rv fear at nearleft  
    r "..."
    show rv smileblush at nearleft  
    show ck normal  
    r "...T-Thank you..."
    show ck cheer  
    c "Papa is the best!"
    show ck normal  
    show f normal
    "Catherine turned to Guilleme again."
    show ck talk  
    c "Lord Gilly, don't you think if everyone with a house takes one person home, nobody would freeze in winter?"
    show ck pout  
    c "You should make it into a law."
    c "They'll obey you because you're a Marquis."
    c "And because you're tall."
    "Guilleme chuckled."
    g "Ah, is that why?"
    show f upset
    c "Well, you're taller than my papa, at least. He'll never be a Marquis."
    "François pulled on his daughter's ear with embarrassment."
    f "Catherine! Shh, that's enough from you!"
    #f "I'm so sorry, sire."
    show f eh
    "Guilleme shook his head good-naturedly, his eyes trailing over the Perride family."
    "Émilie watched him curiously. That same sadness once again surfaced for the briefest moment."
    show ck normal  

    g "You have a lovely family, Sire. I am quite jealous."
    show f eh
    g "You make me want to settle down myself, someday."
    "He chuckled."
    g "Maybe."
    "Émilie's heart skipped a beat."
    "Did he look at her when he said that? Was it her imagination?"
    g "Catherine is a wonderful girl."
    g "It is one of the reasons why I am very invested in her."
    scene bg ckidg  
    "Guilleme knelt down so that he was eye to eye with Catherine."
    "He patted her head."
    g "You are a very intelligent and kind-hearted girl, Catherine."
    g "You are a star."
    #g "{i}Mon étoile.{/i}"
    g "Someday, I know you will change the world."
    g "At least, I'd like to see you try!"
    stop music
    show bg black with None
#flashing scenes of Catherine with a noose around her neck.   
 
    play sound "sfx/heartbeat.ogg"
    r "Mother..."
    show bg csuicide with fade
    show bg black with fade
#sound of creaking rope"
    play sound "sfx/heartbeat.ogg"
    r "Help me..."

    show bg rosashock with fade
    show bg black with fade
    play sound "sfx/heartbeat.ogg"
    r "My chest..."
    show bg csuicide2 with fade
    show bg black with fade
    play sound "sfx/heartbeat.ogg"
    r "I can't breathe."
    r "N-No..."
    r "Ca..."
    play sound "sfx/heartbeat.ogg"
    if persistent.adult:
        show bg csuicide3 with fade
#Catherine Hanging on a noose
    r "CATHERINE!"
    show bg black with fade
    if persistent.chap1WasReadBefore   is None:
        $persistent.chap1WasReadBefore  = True
        $persistent.currentLinesRead +=1
    call chap2 from _call_chap2
    
return    
    

    
    

    
   
    


    
