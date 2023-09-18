
init python:

    ## This creates the End Credits portion.
    
    credits =   ('Writing', 'ilyilaice'),     ('Art', 'chymesoo'),     ('Programming and GUI', 'Marionette'),     ('Music', 'ejtanmusic'),     ('GUI Assets', 'Birctreel'),     ('Background Photo Filters', 'LunaPic.com')
    
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n\nMade with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]."

init:

    # Tracks how much of the game the player has seen.

    # default result = 0

    ## Image Displayables generated in-engine for use in the End Credits.

    # image cred = Text(credits_s, font="font.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.3)
    image theend = Text("{size=80}Fin", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
    #image game_results = Text("{size=80}You've seen [result]\% of the game.{/s}", text_align=0.5)
    #image devnote_unlock = Text("{size=80}You've unlocked a special message. Access it through the Extras Menu.", text_align=0.5)
    #image extras_unlock = Text("{size=80}You've unlocked the Extras Menu. Access it through the Main Menu.", text_align=0.5)

    ## Lets the engine know that this variable is False when the game is first played.
    define persistent.extras_unlocked = False
    define persistent.ending_seen_1 = False
    define persistent.ending_seen_2 = False
    define persistent.ending_seen_3 = False
    define persistent.ending_seen_4 = False
    define persistent.ending_seen_5 = False
    define persistent.ending_seen_6 = False
    define persistent.ending_seen_7 = False
    define persistent.ending_seen_8 = False
    define persistent.ending_seen_9 = False
    
# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
    #jump lbl_credits
    jump lbl_part_1

    return

label lbl_part_1:

    scene bg TRAFFIC
    

    play music DREAMS fadein 1.0

    #"TESTING testing - < > ( ) Pokémon? 0123456789 "

    "You're gazing out the car window. "

    "A boy is running alongside your car, darting inside and outside the sporadic glow of streetlights."

    "No one in the world sees this boy but you."

    "No, this isn't the first time this has happened. No, you're not losing your mind."

    "Sometimes it's just nice to allow your brain to wander. To escape from your skull and the skin you live in."

    "For a moment, you're not you. You're not anybody. "

    "You're not Bee, fourteen years old, high school freshman at St. Philomena's Academy, Marikina City."

    "The irony of it is, when you're not anybody, you can be absolutely anybody. Tonight, you can be--"

    stop music fadeout 1.0

    "A sharp elbow jabs your ribs, jerking you out of your reverie."

    bee "What? What do you want?"

    play music SLICE_OF_LIFE fadein 1.0

    show ATE POKERFACED with dissolve 

    "Despite this rude awakening, your elder sister refuses to meet your eye. "

    "She resumes rambling away at Mom, who's sitting behind the wheel."

    ate "Anyway, as I was saying, I didn't think much of the new priest's homily."

    ate "I wish Father Santos would return to our parish. He told the best jokes."

    hide ATE with dissolve 
    show MOM with dissolve 

    "Mom doesn't respond. She's too busy glaring at you via the rearview mirror."

    mom "Bee, did you hear my question? You didn't, did you?"

    bee "What que--"

    hide MOM with dissolve 
    show ATE POKERFACED with dissolve 

    "Ate elbows you again, presumably to shut you up."

    ate "This new priest--what's his name again? He just goes on and on about the struggles and the drama of priesthood."

    ate "Yeah, yeah. Maybe that stuff's interesting for him."

    ate "But for us? Boring!"

    hide ATE with dissolve 
    show MOM with dissolve 

    "Again, Mom ignores Ate's commentary. Her next words are clearly directed at you."

    mom "I was asking you how you liked the homily tonight."

    mom "But were you even listening back at the church? You sure aren't listening to me now."

    hide MOM with dissolve 

    "Of course you weren't listening. "

    "You stopped paying attention around the time the priest began singing along loudly to {i}Papuri sa Diyos{/i}. "

    "Which is the first hymn of the entire mass. Go figure."

    "I mean, why sing right into the mic like that? Especially if you can't hit any of those high notes? "

    "What is this, karaoke night? Ugh."
    
    show MOM with dissolve 

    mom "ARE. YOU. LISTENING. TO. ME. RIGHT. NOW."

    "Oh, boy. If looks could kill. "

    "No wonder Mom's so effective at her job as an operations manager."

    bee "I'm listening."

    mom "Are you? So can you tell me what today's Gospel was about?"

    hide MOM with dissolve 
    show ATE SHOCKED with dissolve 

    "You shoot a look of pure panic in Ate's direction. A silent cry for help."

    "Your horror is echoed on her face."

    "She starts waving her hands and mouthing something. She then points very deliberately at your face."

    "What does that even mean?"

    hide ATE with dissolve 

    menu:
        "What was today's Gospel about?"
        "Unless you become like a child, you can't enter the kingdom of heaven.":
            jump lbl_part_2
        "If you ever dare to look at a woman lustfully, gouge out your eyes.":
            jump lbl_part_3
        "If Jesus tells you to wait for Him while He prays, don't go to sleep. Don't be lazy like the apostles.":
            jump lbl_part_4



label lbl_part_2:

    "Ate was pointing at you, right? You're fourteen years old, practically still a child. "

    "So the Gospel must have been about children!"

    bee "So Jesus is talking to the apostles, right?"

    bee "So the apostles ask Jesus, who has the best shot at entering heaven?"

    bee "And Jesus says--"

    jump lbl_part_5



label lbl_part_3:

    "Ate was pointing at your eyes, right? Maybe she was miming gouging out your eyes. "

    "So the Gospel must have been about poking out eyes!"

    bee "So Jesus is talking to the apostles, right? Teaching them the Beatitudes and stuff."

    bee "Then Jesus says, poke out your eye if it causes you to sin--"

    jump lbl_part_5



label lbl_part_4:

    "Ate was pointing at you, right? You were practically falling asleep during the mass. "

    "So the Gospel must have been about the apostles taking a nap!"

    bee "So Jesus is telling the apostles to wait for Him while He prays."

    bee "But when He returns--wouldn't you know it?--they're asleep."

    bee "So He scolds them for being lazy."

    show MOM with dissolve 

    "Mom's nodding along. Seems like you nailed it!"

    mom "{i}The spirit is willing, but the flesh is weak.{/i}"

    "Ate gives an audible sigh of relief beside you."

    mom "It's good you listened. Remember, you can't just ignore everything that bores you."

    mom "Otherwise, you miss out on certain things. Important things."

    mom "Personally, I thought Father's homily was wonderful."

    mom "Even though he talked about his priestly life, the underlying message was universal...."

    hide MOM with dissolve 

    "You want to listen. Really, you do. "

    "But a boy is running alongside your car. And, try as you might, you can't stop watching."

    scene bg black with fade

    jump lbl_part_6



label lbl_part_5:

    show MOM with dissolve 

    "Mom interrupts you with a massive sigh."

    mom "So you weren't listening. As usual."

    mom "Mrs. Ocampo called me at work last Friday. She expressed concerns about your behavior in class."

    "Uh-oh."

    mom "She says you never listen. You're too busy daydreaming all the time."

    mom "I get it, school can be boring. But you can't just ignore everything that bores you."

    mom "Otherwise, you miss out on certain things. Important things."

    mom "Like the Gospel. The Word of God is important."

    mom "Listen, in today's Gospel, God is telling us...."

    hide MOM with dissolve 

    "You want to listen. Really, you do. "

    "But a boy is running alongside your car. And, try as you might, you can't stop watching."

    scene bg black with fade

    jump lbl_part_6



label lbl_part_6:

    scene bg LIVING_ROOM with fade

    "The new episode of your all-time favorite anime, {i}Psychowrath{/i}, is airing on TV tonight."

    "The Filipino dub is as awful as ever. It's 2006, the pinnacle of Japanese animation. Can't the dubbing quality just catch up already?"

    "But the characters! Oh, the characters! You'd die for these characters. "

    show ATE SMILING with dissolve 

    "Side by side on the couch, you and Ate plunge your hands into supersized bags of Tomi sweet corn chips."

    "The two of you exchange gleeful glances after each exciting new development."

    hide ATE with dissolve 

    stop music fadeout 1.0

    play music DREAMS fadein 1.0

    show SORA_X_UMI_ANIME_FAN_SERVICE_CG with dissolve 

    "In the midst of all the chaos, your two favorite characters, Sora and Umi, are having This Special Moment."

    "Long Lingering Looks. "

    "Hurt and Comfort."

    "Look at all these relationship flags! "

    "Your ship is sailing! Alleluia!"

    hide SORA_X_UMI_ANIME_FAN_SERVICE_CG with dissolve 

    stop music fadeout 1.0

    show ATE IRRITATED with dissolve 

    ate "Lame."

    bee "What's lame?"

    ate "Umi's lame. Why the hell's he crying like that? Is he a girl?"

    ate "He even looks like a girl. What's up with that hair?"

    bee "Didn't Umi's whole family just die? Weren't they brutally murdered?"

    ate "God, I hate stupid sob stories like that."

    ate "Sorry, I know you love Umi, but I can't stand him. Sora's way cooler."

    bee "But Umi's the stronger one right?"

    bee "Remember when Sora was infected by the virus back in episode eight, and Umi had to knock some sense into him--"

    ate "Umi is a Mary Sue."

    hide ATE with dissolve 

    "Silence follows this statement, punctuated only by the crunch of chips. "

    "{i}Mary Sue{/i} is a magic incantation to end all arguments. It's the worst thing a character can be called."

    "Luckily, the silence is broken when Dr. Karigari's mind-controlled troops arrive!"

    "They've come to ravage the abandoned laboratory where Sora and Umi are seeking refuge!"

    play music SLICE_OF_LIFE fadein 1.0

    show ATE SMILING with dissolve 

    "You and Ate squeal in unison. You grasp hands in breathless excitement. "

    "Her palm is powdered with starchy yellow dust. But you don't care--so is yours."

    "Just as Sora and Umi stand back to back and draw their trusty weapons, the episode ends. The ending theme begins to play."

    ate "Sora's such a badass! God, I wish Sora was my boyfriend."

    bee "You already have a boyfriend."

    ate "If Sora was 3-D, I'd leave Jaime in a heartbeat. No questions asked."

    ate "You know what I mean, right? You feel the same way about Umi."

    hide ATE with dissolve 

    "Umi as your boyfriend? Not bad. "

    "But you prefer thinking of Sora and Umi as each other's boyfriends. They're perfect for each other."

    "You open your mouth, wanting to tell Ate all about it. "

    "But do you really need to fight with Ate again? "

    "About Umi being like a girl? About Umi being so gay, and therefore so gross?"

    "Why does she always need to make a fight out of it anyway? You close your mouth."

    show ATE POKERFACED with dissolve 

    "Ate turns off the TV and spreads her nursing textbooks all over the sala table. She lines up a rainbow of highlighters."

    "She poises a highlighter over a page, then pauses to shoot her boyfriend a text. "

    show ATE SMILING

    "He must reply instantly, because her face lights up like a Christmas tree."

    "When she sees you watching her with amusement, she narrows her eyes at you."

    show ATE IRRITATED

    ate "Shouldn't you be studying?"

    "You groan in response."

    bee "I hate Sunday nights. Weekends would be perfect if they didn't include Sunday nights."

    hide ATE with dissolve 

    "Sighing, you yank out your {i}Panitikan{/i} textbook from your backpack. "

    "So will Don Juan manage to capture the Ibong Adarna? Guess you're going to find out!"

    "Within minutes of thumbing through endless pages of the 16th-century epic poem, you feel like your head will roll off from boredom."

    "You get up and pop a disc into the CD player. "

    "Your friend Vida burned it for your birthday. Anime themes and bubbly J-pop anthems abound."

    show ATE IRRITATED with dissolve 

    "You're singing along to the {i}Psychowrath{/i} opening theme--the romaji lyrics you've printed out are spot on!--when Ate cuts in."

    ate "Do you need to be so loud? Mom's sleeping, you know?"

    ate "She has an early day tomorrow. We all do."

    hide ATE with dissolve 

    scene bg black with fade

    scene bg BEDROOM with fade

    "Given Ate's foul mood and your own deathly boredom, you decide to retire early to your bedroom for the night."

    "As you lie in bed, your brain replays scenes from the latest {i}Psychowrath{/i} episode. "

    "You can't get over how good Sora and Umi look together. "

    "Once upon a time, you thought you were alone. "

    "But one day, as you and your friends were discussing {i}Psychowrath{/i}, Vida came right out with it."

    "Sora and Umi belonged together, Vida said. They were obviously gay for each other, so Vida shipped their pairing."

    "Your other friend, Karis, laughed like she thought Vida was joking."

    "But you? You saw an opportunity and took it. "

    "You agreed with Vida. Yes, Sora and Umi were meant for each other."

    "Vida, a self-proclaimed expert fujoshi, taught you the logistics of hot yaoi smex using Barbie and Ken dolls she brought from home. "

    "Sora, the seme, was Ken. Umi, the uke, was Barbie."

    "Vida wanted to drill a hole between Barbie's legs using a pencil, but you stopped her. You said you got it."

    "Karis, being Karis, howled with laughter. But also, being Karis, she let you two fujoshis be fujoshis. She never told anyone."

    "Embarrassing as it is to admit right now, reminiscing about Vida's Barbie-and-Ken demonstration is beginning to get you all hot and bothered."

    "Are you truly a pervert? Or is this just what it's like to be fourteen?"

    "Dr. Karigari's mind-control magic must be messing with your head, because before you know it, your hand has crept under your shorts."

    "Maybe you should just get this over with. Imagine Sora and Umi doing what Ken and Barbie did."

    "Sora topping as Ken. Umi bottoming as Barbie."

    "But to your surprise, as your mind begins to replay the scene, your mind's eye zooms in on one particular aspect of it."

    "You're not focusing on the dolls bucking into each other. You're focusing on the hands controlling the dolls."

    "The hands are Vida's hands."

    "This realization startles and scares you."

    "On the one hand, it makes sense. Vida taught you everything you know about smut. Of course your brain would make that connection."

    "But on the other hand, yikes. A girl picturing a fellow girl in this type of situation? Are you the world's biggest pervert or what?"

    "So what should you think about now? Who should you imagine?"

    menu:
        "Who should you think about as you touch yourself?"
        "Imagine Sora and Umi.":
            jump lbl_part_7
        "Imagine Vida.":
            jump lbl_part_8
        "Imagine a socially acceptable crush.":
            jump lbl_part_9



label lbl_part_7:

    scene bg black with fade

    stop music fadeout 1.0

    play music DREAMS fadein 1.0

    "You try to picture Sora and Umi naked. Vida stripped the dolls before the demonstration, after all. "

    "But you're having trouble imagining that. You like Sora's and Umi's outfits way too much to strip them off so callously."

    "Instead, let's say their pants are unzipped and lowered by the bare minimum number of millimeters. "

    "There, that should do it."

    "After you settle on a rhythm, you only need a minute to finish."

    "Satisfied now, you drift off easily to sweet slumberland."

    stop music fadeout 1.0

    scene bg black with fade

    jump lbl_part_10



label lbl_part_8:

    scene bg black with fade

    stop music fadeout 1.0

    play music DREAMS fadein 1.0

    "You decide to imagine Vida."

    "But you can't linger too long on her face. Too weird."

    "Instead, you picture her hands. Her long fingers. "

    "During Music, when the class all sings together, she always volunteers to do the accompaniment on the piano."

    "She says it's just to get out of singing Bisayan folk songs none of you can understand. "

    "But that's a lie. She loves playing the piano. You can tell."

    "You settle on a rhythm now. It's a rhythm akin to piano-playing. "

    "You finish almost instantly."

    "Satisfied now, you drift off easily to sweet slumberland."

    stop music fadeout 1.0

    scene bg black with fade

    jump lbl_part_11



label lbl_part_9:

    "You can't go wrong with picturing a generic cute boy, right? "

    "The thing is, studying in an all-girls Catholic school run by nuns severely limits your options. "

    "You don't know too many boys, let alone cute boys."

    "There's this one boy from St. Michael's who rides the same bus as you. All the girls go crazy for him. "

    "You should too, right?"

    scene bg black with fade

    stop music fadeout 1.0

    play music DREAMS fadein 1.0

    "You try picturing this boy's face, but even that is a challenge. "

    "You barely ever notice him, after all. He's just kind of there."

    "Theoretically, you do know the features that make up his face. "

    "Dimples? Check. Hair styled like the latest heartthrob in showbiz? Check."

    "You piece these parts together to form a face. The body comes next. "

    "What's a boy supposed to look like underneath his clothes? You have no idea. "

    "The penis stands when excited, right? Is it ... like some kind of animal? "

    "Like a meerkat, maybe, from a Discovery Channel documentary?"

    "Or maybe it's like a Pokémon? Like Pikachu psyching itself up to release a thunderbolt?"

    stop music fadeout 1.0

    "You groan in frustration. "

    "Not sexual frustration. Just regular frustration."

    "Then a gasp follows your groan. "

    "But the gasp didn't come from your mouth."

    scene bg BEDROOM
    

    play music PARANOIA fadein 1.0

    "Your eyes fly open."

    "No. "

    "This isn't real."

    "It can't be real."

    show ATE SHOCKED with dissolve 

    "Ate's standing by the open bedroom door. "

    "She's staring down at you in horror."

    "You yank your hand out of your shorts. "

    "But the damage is done."

    hide ATE with dissolve 

    "As the door slams shut behind her, your world collapses all around you."

    #ENDING 1/9: Discovery by Ate
    #scene bg black with fade
    #"Ending 1/9: Discovery by Ate"

    $ quick_menu = False
    scene ENDING_1 with dissolve 
    $ persistent.ending_seen_1 = True
    pause
    jump lbl_credits
    
    return



label lbl_part_10_reuse:

    scene bg CLASSROOM with fade

    play music SLICE_OF_LIFE fadein 1.0

    "The only thing in the world you hate more than Sunday nights is Monday mornings."

    show TEACHER with dissolve 

    ocampo "When the Ibong Adarna sings, its sweet melody lulls everyone in the vicinity into deep sleep."

    "Is that what's happening here? Is your teacher the personification of the Ibong Adarna? Because you're nodding off like there's no tomorrow."

    "Quick! Do something to distract yourself! "

    "If Mrs. Ocampo catches you sleeping, who knows what she'll do?"

    "She might even phone home. It wouldn't be the first time you've been busted."

    hide TEACHER with dissolve 
    
    return

label lbl_part_10:
    call lbl_part_10_reuse from _call_lbl_part_10_reuse
    menu:
        "What should you do to keep yourself from sleeping in class?"
        "Doodle.":
            jump lbl_part_12
        "Daydream.":
            jump lbl_part_13



label lbl_part_11:

    call lbl_part_10_reuse from _call_lbl_part_10_reuse_1

    menu:
        "What should you do to keep yourself from sleeping in class?"
        "Doodle.":
            jump lbl_part_15
        "Daydream.":
            jump lbl_part_16



label lbl_part_12:

    stop music fadeout 1.0

    play music DREAMS fadein 1.0

    "You decide to doodle in your notebook. "

    "You let your pen wander over a blank page without dwelling too deeply on its direction."

    "When you look down at what you've drawn, you find a rough sketch of two bodies laying on top of each other, blob-like and indistinguishable. "

    show SORA_X_UMI_DOODLE_MINI_CG with dissolve 

    "You draw hair to differentiate the two bodies. "

    "Spiky hair for the body on top. Floppy hair for the body on the bottom."

    "After some hesitation, you draw a sausage shape between the legs of each body."

    "With this simple addition, your heart begins to thump. "

    "You've never drawn anything like this before. Now you can't bring yourself to stop."

    "You start filling in the details of your drawing. "

    "The dark fuzz of armpits. Exes for nipples."

    hide SORA_X_UMI_DOODLE_MINI_CG
    

    stop music fadeout 1.0

    "Suddenly, you feel a hand clamp down on your shoulder."

    "Sharp nails dig into your skin."

    "Wincing, you jerk up your head. "

    play music PARANOIA fadein 1.0

    "When you first started doodling, Mrs. Ocampo was pacing in front of the teacher's table."

    "She's not there anymore."

    "You swivel your head "

    "as if you're starring "

    "in a slow-motion scene "

    "in a movie."

    show TEACHER with dissolve 

    "Mrs. Ocampo is looming behind you."

    "Already staring down at the drawing in front of you."

    #ENDING 2/9: Discovery by Your Teacher

    #scene bg black with fade
    #"Ending 2/9: Discovery by Your Teacher"
    $ quick_menu = False
    scene ENDING_2 with dissolve 
    $ persistent.ending_seen_2 = True
    pause
    jump lbl_credits
    
    return


label lbl_part_13:

    scene bg black with fade

    play music SLICE_OF_LIFE fadeout 1.0

    play music DREAMS fadein 1.0

    "You decide to drift into a daydream. You let your mind wander as it pleases."

    "In the scenario selected by your subconscious, Sora and Umi are living blissfully together in a neat little house with a flower garden."

    "But in the dead of the night, Umi sneaks out from the bed he shares with Sora. "

    "Umi packs his bags, polishes his weapon."

    "He's going on a journey alone to seek revenge against the brutes who murdered his family in cold blood."

    "Just as he's about to cross the gate, Sora embraces Umi from behind and begs him to stay, please stay. "

    "With tears in his blue eyes, Umi whirls around. "

    "Deep down, he doesn't really want to go! "

    "So Umi catches Sora's face between his hands, but before he can kiss him--"

    stop music fadeout 1.0

    jump lbl_part_14



label lbl_part_14_reuse:

    scene bg CLASSROOM
    

    show TEACHER
    

    ocampo "Pop quiz, everybody! Take out a 1/4 sheet of pad paper. Ten questions only."

    play music PARANOIA fadein 1.0

    "Oh no."

    "You pray for multiple-choice questions, but you must not be praying hard enough. "

    "As Mrs. Ocampo reads out the identification-type questions, you chew on your pen and pull plausible-sounding answers out of thin air."

    ocampo "Okay, pens down. Exchange papers with your seatmates."

    hide TEACHER with dissolve 
    show KARIS SMILING with dissolve 

    "Karis, your seatmate, grabs your paper with a careless smile on her face. Doesn't look like she had any trouble."

    "Predictably, you bomb the quiz with a whopping 2/10 points. "

    "Karis, on the other hand, scores a perfect 10."

    hide KARIS with dissolve 
    show TEACHER with dissolve 

    ocampo "Okay, pass your papers forward."

    "Ugh! You don't want any of your classmates to see your score!"

    stop music fadeout 1.0

    hide TEACHER with dissolve 
    show KARIS POKERFACED with dissolve 

    bee "Hey, Karis. Flip my paper over before you pass it, okay?"

    karis "Yeah, all right."

    hide KARIS with dissolve 

    "And on this depressing note, the lunch bell rings."

    scene bg black with fade
    return

label lbl_part_14:
    call lbl_part_14_reuse from _call_lbl_part_14_reuse
    jump lbl_part_18



label lbl_part_15:

    stop music fadeout 1.0

    play music DREAMS fadein 1.0

    "You decide to doodle in your notebook. "

    "You let your pen wander over a blank page without dwelling too deeply on its direction."

    "When you look down at what you've drawn, you find a rough sketch of a girl's face. "

    show VIDA_DOODLE_MINI_CG with dissolve 

    "Short hair."

    "Small eyes. "

    "She's looking strangely familiar...."

    hide VIDA_DOODLE_MINI_CG with dissolve 

    "You glance up from your notebook. "

    "You gaze at the girl seated a few rows in front of you."

    show VIDA POKERFACED with dissolve 

    "The girl twirls a pen with her long fingers."

    "She's half paying attention to the teacher, half gazing out the window."

    hide VIDA with dissolve 

    stop music fadeout 1.0

    "Suddenly, you're no longer sleepy. "

    "You tear the sketch from your notebook and crumple it into a ball, which you then stuff into your skirt pocket."

    "Yeah, let's just pretend that never happened."

    play music SLICE_OF_LIFE fadein 1.0

    "You try to tune back into Mrs. Ocampo's endless extolling of Don Juan's virtues and condemning of his brothers' vices."

    "It's boring, sure, but it keeps you from dwelling on other things. Uncomfortable things."

    "Good thing you're listening too, because with five minutes to the bell--"

    show TEACHER with dissolve 

    ocampo "Pop quiz, everybody! Take out a 1/4 sheet of pad paper. Ten questions only."

    "You still find yourself struggling with the quiz. "

    "Luckily, however, some of the questions pertain to matters mentioned toward the end of the lecture. Which you listened to."

    ocampo "Okay, pens down. Exchange papers with your seatmates."

    hide TEACHER with dissolve 
    show KARIS SMILING with dissolve 

    "Karis, your seatmate, grabs your paper with a careless smile on her face. Doesn't look like she had any trouble."

    "You've managed to scrape 5/10 points. "

    "Karis, on the other hand, scores a perfect 10."

    hide KARIS with dissolve 
    show TEACHER with dissolve 

    ocampo "Okay, pass your papers forward."

    "Amidst the rustle of papers, you can't help sighing in relief. "

    "One mistake more and this quiz could have been a total disaster."

    hide TEACHER with dissolve 
    show KARIS POKERFACED with dissolve 

    bee "Karis, I wish I was as smart as you. You really studied, huh?"

    karis "Nah, I didn't. I just played {i}Pokémon{/i} on my Game Boy."

    karis "Can't believe you found it hard. As long as you were listening, you'd be able to answer everything easily."

    hide KARIS with dissolve 

    stop music fadeout 1.0

    "Well, that's just the problem, isn't it? "

    "On this sobering note, the lunch bell rings."

    scene bg black with fade

    jump lbl_part_19



label lbl_part_16:

    scene bg black with fade

    stop music fadeout 1.0

    play music DREAMS fadein 1.0

    "You decide to drift into a daydream. You let your mind wander as it pleases."

    "In the scenario selected by your subconscious, you're walking alone down hallways of the school."

    "You see no students or teachers. You hear no voices."

    "Suddenly, you hear the tinkling melody of a piano. It's coming from the music room."

    "Somehow, you already know who's playing. "

    "You also know that she's alone, and that she's been waiting for you. Maybe for a long time now."

    "As you come closer and closer, the music rises to a crescendo. "

    "Fingers pounding on the keys now."

    "Your heart thumping, you extend your hand toward the knob, but before you can twist it--"

    stop music fadeout 1.0

    jump lbl_part_17



label lbl_part_17:
    call lbl_part_14_reuse from _call_lbl_part_14_reuse_1

    jump lbl_part_20



label lbl_part_18:

    scene bg LIBRARY with fade

    play music SLICE_OF_LIFE fadein 1.0

    "Still upset about flunking the quiz, you decide to spend the lunch break alone in the library."

    "Even though Vida fussed over you, you totally iced her out."

    "Pity. You're dying to discuss last night's {i}Psychowrath{/i} episode with her. But once you put on your Mean Face, you gotta stick to it."

    "After surveying the spines lined up in the shelves, you select {i}The Picture of Dorian Gray{/i} by Oscar Wilde. "

    "You find an unoccupied table and settle down to read. "

    "Just as you've turned to the first page, you sense a curious presence close to you."

    "You look up. Someone has taken the seat beside you."

    stop music fadeout 1.0
    play music DREAMS fadein 1.0

    show UMI POKERFACED with dissolve 

    "It's Umi, but not really. He looks like Umi, but he's someone you've known since you were a child."

    "You saw him just last night, running alongside the family car. "

    "It's the first time you've seen him don Umi's face. You don't know why he's changed his face again. "

    "Maybe he just likes Umi's face. You like it too."

    show UMI SMILING

    "He points at the notebook you've brought with you. Even without a word, you already know what he wants."

    "Whenever he visits you alone in your bedroom, he speaks aloud, no qualms about it. "

    "But in a public place like this, he prefers to communicate in writing."

    hide UMI with dissolve 

    menu:
        "What should you do to pass the time in the library?"
        "Communicate with your old friend.":
            jump lbl_part_21
        "Read the book.":
            jump lbl_part_22



label lbl_part_19_reuse:

    scene bg CAFETERIA with fade
    #scene bg black with fade

    play music SLICE_OF_LIFE fadein 1.0

    show VIDA POKERFACED with dissolve :
        xalign 0.25

    show KARIS SMILING with dissolve  :
        xalign 0.75

    "At the cafeteria, Vida and Karis buy bean sprout lumpias for lunch. You, on the other hand, buy two packs of Hansel mocha biscuit sandwiches. "

    "Two reasons for this. One, nothing in the world can compare to the peculiar salty sweetness of Hansel. Two, a single pack just isn't enough."

    "Vida gobbles her lumpia in about two bites, then extracts a melty lollipop from her skirt pocket."

    show VIDA IRRITATED:
        xalign 0.25

    vida "So how'd you guys do in the pop quiz? I was totally blindsided!"

    vida "I mean, jeez, it was practically lunchtime by then."

    vida "One of my butt cheeks was already hovering over my seat. Just ready to take off and never look back."

    show KARIS LAUGHING:
        xalign 0.75

    "Karis chuckles."

    show VIDA POKERFACED:
        xalign 0.25

    show KARIS SMILING:
        xalign 0.75

    karis "I did all right."

    bee "Karis got a perfect score. I checked her paper."

    vida "That's insane. I just got a 5/10."

    vida "Bee, what did you get?"

    return
    
label lbl_part_19:
    call lbl_part_19_reuse from _call_lbl_part_19_reuse
    
    jump lbl_part_25



label lbl_part_20:

    call lbl_part_19_reuse from _call_lbl_part_19_reuse_1

    jump lbl_part_26



label lbl_part_21:

    show UMI SMILING with dissolve 

    "You open your notebook and begin to write."

    nvl clear
    koizumi_riyuu "{i}hey there.{/i}"

    "Koizumi Riyuu is the Japanese name you made up for yourself back when you first started getting into anime as a kid."

    umi404 "{i}Good afternoon, Koizumi-san.{/i}"

    koizumi_riyuu "{i}whoa you're really going by the name umi now?{/i}"

    umi404 "{i}Identity is a construct. I am whoever you need me to be.{/i}"

    koizumi_riyuu "{i}well ok then. how's sora-kun doing these days, umi-kun?{/i}"

    umi404 "{i}Sora shall never cease to be a special person to me.{/i}"

    koizumi_riyuu "{i}yeah you two look super cute together.{/i}"

    show UMI POKERFACED

    umi404 "{i}Even so, I find myself grappling with a strange sort of dissatisfaction these days.{/i}"

    koizumi_riyuu "{i}oh no what's wrong?{/i}"

    umi404 "{i}It is difficult to describe. Sora is my rock. He is a shoulder to cry on. However, I can't shake the sense that what we share is not quite real.{/i}"

    koizumi_riyuu "{i}not real? you mean cause he's 2-D? cause if so i got some bad news for you.{/i}"

    show UMI SMILING

    umi404 "{i}I am aware of my own two-dimensional nature, Koizumi-san. Yet I am here with you right now, am I not?{/i}"

    koizumi_riyuu "{i}yeah that's true.{/i}"

    umi404 "{i}You are real to me, and I am real to you. In fact, you are the only real thing to me, in this half-life I lead.{/i}"

    koizumi_riyuu "{i}what ... what are you saying?{/i}"

    show UMI BLUSHINGSMILE

    umi404 "{i}I am saying that I love you. I am in love with you, Koizumi-san.{/i}"

    koizumi_riyuu "{i}wow ok. this is ... this is a lot to take in. not sure how i feel about this.{/i}"

    umi404 "{i}Perhaps, if we kiss, we may know for certain whether you have feelings for me.{/i}"

    "You tear your eyes from the page and look up. Umi stares steadily at you. "

    "His eyes are so impossibly blue. They draw you in."

    "Closer and closer. Maybe you'll drown in those blue-blue eyes...."

    stop music fadeout 1.0
    
    hide UMI with dissolve 
    show VIDA POKERFACED
    

    vida "Why're you staring into space?"

    "Startled by Vida's sudden appearance, you jerk backward. "

    "She's sitting on the chair Umi previously occupied."

    "Umi is nowhere to be seen."

    "You slam your notebook shut before Vida can see what you've written."

    bee "None of your business."

    "Vida stares down at your palm laying flat over your notebook. She then shrugs, apparently deciding that it's nothing important."

    jump lbl_part_23



label lbl_part_22:

    "You bury your nose in the book and ignore the presence beside you until it gradually disappears. "

    "Like smoke merging with the air you breathe."

    "Seems like the book you chose is a classic novel. The language it employs is a tad old-fashioned. "

    "Which makes its homoerotic overtones all the more shocking. "

    "The first chapter alone is the gayest thing you've ever read outside of a yaoi fanfic."

    "You can't help slapping on Sora's and Umi's faces over the characters of the book. "

    "The scenario suits them so well. All you need to do is change the names."

    "Umi is Dorian Gray, the exquisite blond youth. "

    "Sora is Basil Hallward, the infatuated artist who seeks to capture Umi's unparalleled beauty in a painting."

    "Should you retain Lord Henry Wotton's character in your fantasy? Maybe Dr. Karigari can play his role?"

    "Just then, someone once again occupies the seat next to you. "

    stop music fadeout 1.0

    show VIDA POKERFACED with dissolve 

    "This time, it's Vida. "

    vida "Why're you staring into space?"

    bee "None of your business."

    jump lbl_part_24



label lbl_part_23_reuse:

    play music SLICE_OF_LIFE fadein 1.0

    show VIDA IRRITATED

    vida "Don't be moody. I just came to bring you lunch."

    "She drops two packs of Hansel mocha biscuit sandwiches on your lap. Your favorite."

    "Your Mean Face dissolves instantly."

    bee "Hey, thanks."

    show VIDA POKERFACED

    "Throwing furtive glances all around, you surreptitiously open a pack under the table and sneak a biscuit into your mouth in the guise of a yawn."

    vida "Look, I know you're upset about something."

    vida "Karis wouldn't tell me, but I'm guessing this is about that pop quiz?"

    "You grunt noncommittally. Some biscuit crumbs flutter down from your lips and fall to your skirt. "

    vida "I don't get why you're even worrying about it."

    vida "Sure, you suck at Filipino. But doesn't everybody?"

    bee "Karis doesn't suck at Filipino."

    show VIDA IRRITATED

    vida "Duh. Karis is the exception."

    vida "She's a freaking genius."

    show VIDA POKERFACED

    vida "Point is, aside from Karis, we all suck equally at it."

    vida "But no one can beat you at English. Not even Karis."

    vida "You read more than anyone I know. You even unlocked the highest SRA color. That's your edge over everybody else."

    vida "If anything, I should be upset. I have no talents."

    "You swallow the last of the biscuit crumbs just so you can dispute this."

    bee "You can play the piano. You're like a pro."

    show VIDA IRRITATED

    "Vida rolls her eyes."

    vida "Oh, because that's such a useful life skill. That will help me get into a good college and find a sustainable job. Why not."

    show VIDA SMILING

    vida "Come on. Let's go."

    vida "Lunch break's almost over. You can eat while we walk."

    "On the way back to the classroom, you and Vida discuss last night's {i}Psychowrath{/i} episode. There's a lot of squealing and shrieking involved."

    hide VIDA with dissolve 

    scene bg black with fade
    return

label lbl_part_23:
    call lbl_part_23_reuse from _call_lbl_part_23_reuse
    jump lbl_part_28



label lbl_part_24:

    call lbl_part_23_reuse from _call_lbl_part_23_reuse_1

    jump lbl_part_29



label lbl_part_25:

    bee "Oh, man. Same."

    show VIDA SMILING:
        xalign 0.25

    vida "Hey, at least we passed, right?"

    vida "I think that deserves a high five. High fives for us fellow fives!"

    "Grinning, you high-five Vida. The moment your palms connect, however, you suddenly remember sketching her face in class."

    "Then you remember last night. Last night was weird. And intense."

    "But you probably shouldn't be thinking about last night, especially right now."

    "Not when Vida's toying with her strawberry Chupa Chups like that."

    karis "So did you guys watch {i}Psychowrath{/i} last night?"

    jump lbl_part_27



label lbl_part_26:

    bee "The real question is, how's it possible for one of your butt cheeks to hover over the seat, while the other butt cheek's still firmly seated?"

    show KARIS LAUGHING:
        xalign 0.75

    "Karis chuckles again, but Vida brushes this off without missing a beat."

    vida "I was seated at a tilt. Why are you avoiding my question?"

    "You heave out a sigh."

    show KARIS POKERFACED:
        xalign 0.75

    bee "What do you want me to say? I flunked big-time."

    bee "But it's not a big deal. I've always sucked at Filipino anyway. The whole subject is lame."

    "Of course, you don't tell Vida that part of the reason you failed so miserably was because you were lost in a daydream that may or may not involve her."

    "You're trying and failing not to think about last night, back when your fantasy wasn't quite so ambiguous, when a hand on your shoulder startles you."

    "It's Karis, trying to comfort you."

    karis "Bee, don't worry about it, okay? I'll help you catch up before the periodical exams."

    "You weren't worrying about the exams at all, actually. Still, it's a sweet offer on her part."

    bee "Really? Thanks!"

    show KARIS SMILING:
        xalign 0.75

    karis "No prob."

    karis "So how about the new {i}Psychowrath{/i} episode, huh? Did you guys catch it?"

    jump lbl_part_27



label lbl_part_27:

    "You jump gratefully at the topic. Nothing like your favorite anime to distract you from unnecessary thoughts."

    bee "Hell yeah! Best episode so far, hands down!"

    show VIDA BLUSHINGSMILE:
        xalign 0.25

    vida "Watched it, loved it, tattooed the episode summary over my heart."

    show KARIS LAUGHING:
        xalign 0.75

    karis "Yeah, okay. Stupid question."

    show KARIS SMILING:
        xalign 0.75

    bee "Attention, everyone! The ship has sailed. I repeat, the ship--"

    vida "No kidding. The gayness was off the charts this week. Wouldn't be surprised if they transcended into canon at this point."

    bee "If Sora x Umi became canon, I'd just drop dead on the spot."

    "In between the shrieks of fangirlish delight, Karis can barely get a word in edgewise."

    "But when she does, she only raves about how awesome Dr. Karigari is."

    "You have a theory about that. When God created Karis, He must have realized that He forgot to include any flaws."

    "Thus, at the last minute, He slapped onto her an unfortunate sympathy for all fictional villains, no matter how deplorable."

    "No wonder she's the only one at school who can even stand to be friends with extreme fujoshis like you and Vida."

    "Even when the bell rings, signalling the start of afternoon classes, you and Vida babble about {i}Psychowrath{/i} all the way back to the classroom."

    hide VIDA with dissolve 

    hide KARIS with dissolve 

    scene bg black with fade

    jump lbl_part_30



label lbl_part_28_reuse:

    scene bg CLASSROOM with fade
    #scene bg black with fade

    "If Math is the ninth circle of Hell, then Social Studies is Purgatory. "

    "Math is a steaming trainwreck of dread, but Social Studies? There's a glimmer of hope. A light at the end of the tunnel."

    "This light is called the last bell. The bell that signals dismissal. Freedom from this prison cell."

    "The bell's still a long way away though. "

    "Elbows resting on the desk, chin pressed against your palms, you try to fight the flutter of your eyes. "

    "It's a losing battle."

    "Siesta time is siesta time. Your brain can't even sustain a daydream under these extreme circumstances."

    return
    
label lbl_part_28:
    call lbl_part_28_reuse from _call_lbl_part_28_reuse
    jump lbl_part_31



label lbl_part_29:

    call lbl_part_28_reuse from _call_lbl_part_28_reuse_1

    jump lbl_part_32



label lbl_part_30:

    call lbl_part_28_reuse from _call_lbl_part_28_reuse_2

    jump lbl_part_33



label lbl_part_31:

    show KARIS POKERFACED with dissolve 

    "Beside you, Karis catches a note. Most likely, it's from Vida, who's seated a few rows in front of you."

    show KARIS LAUGHING

    "Karis chuckles as she reads the note. You half expect her to lean over and share whatever joke she's read."

    show KARIS SMILING

    "But she doesn't. Instead, she crumples the note then dives to grab your backpack from the floor."

    bee "What the heck are you doing with my bag?"

    karis "Just need some paper. Gotta reply to this note."

    "You open your mouth to protest, but then close it right away. "

    hide KARIS with dissolve 
    show TEACHER with dissolve 

    "Mrs. Pineda, the Social Studies teacher, is looking in your direction now."

    "Under Mrs. Pineda's watchful gaze, you stare dutifully down at your desk. "

    hide TEACHER with dissolve 

    "You pass the time by reading the messages carved there. "

    "The grammar's all over the place, but at least these vandals have a safe space to vent."

    "By the time you dare to look up again, the bell's ringing. "

    "Dismissal time!"

    show TEACHER with dissolve 

    "Before you can escape, however, Mrs. Pineda summons you to the teacher's table."

    pineda "Bee, why were you talking in class?"

    "The better question is, why's it always you who gets caught? Karis was talking too!"

    pineda "If you have something to say, you should raise your hand."

    "Vida can pass notes. Karis can touch stuff that isn't hers. "

    "But you? The moment you so much as open your mouth, you're busted!"

    pineda "Bee, are you listening?"

    bee "Yes, Ma'am. I'm sorry, Ma'am."

    "You promise Mrs. Pineda you'll never chat in her class again."

    hide TEACHER with dissolve 

    stop music fadeout 1.0

    "You return to your seat to get your backpack."

    show VIDA POKERFACED with dissolve :
        xalign 0.25

    show KARIS POKERFACED with dissolve :
        xalign 0.75

    "You see a bunch of girls gathered around Karis. Vida's there too, sitting on your chair."

    "They all turn to stare at you as you approach. "

    play music PARANOIA fadein 1.0

    "Karis reads aloud from an open notebook on top of her desk. "

    karis "What ... what are you saying?"

    "Vida also reads aloud from the notebook."

    vida "I am saying that I love you. I am in love with you, Koizumi-san."

    "Your heart stops, then resumes thumping triple-time."

    show VIDA SMILING :
        xalign 0.25

    show KARIS LAUGHING :
        xalign 0.75

    "You rush forward to snatch the notebook, but Vida whips it out of reach. "

    "She dashes toward the door. "

    "Before she can make her exit, she whirls around to yell another line from the notebook."

    vida "Perhaps, if we kiss, we may know for certain whether you have feelings for me."

    "Mimicking the smacking sound of a kiss, she flounces out the doorway. "

    hide VIDA with dissolve 

    "Karis races out right after her, cackling crazily all the while. "

    hide KARIS with dissolve 

    "For a second, the horror of the situation freezes you where you stand. "

    "All around you, your classmates are sniggering. Making kissing noises."

    "Then you remember how to run."

    "You barrel out of the room, chasing down the friends who have betrayed you."

    #ENDING 3/9: Discovery by Your Classmates

    #scene bg black with fade
    #"Ending 3/9: Discovery by Your Classmates"
    $ quick_menu = False
    scene ENDING_3 with dissolve 
    $ persistent.ending_seen_3 = True
    pause
    jump lbl_credits
    
    return


label lbl_part_32_reuse:

    "Maybe you'll close your eyes for a little bit. Just for a few seconds...."

    scene bg black with fade

    stop music fadeout 1.0

    play music DREAMS fadein 1.0

    "Suddenly, you're running on a crowded street. "

    "Bicycles leap out to ambush you. "

    "Pedestrians seem to go out of their way just to cross your path and trip you."

    "You don't know where you're going. "

    "You just know you have to get away. Now."

    "Someone--you don't know who--is chasing you down."

    "You keep willing your legs to go faster. But they move as if in deep water."

    stop music fadeout 1.0

    scene bg CLASSROOM
    

    "The shrill ring of the bell jerks you awake. "

    "Dismissal time!"

    play music SLICE_OF_LIFE fadein 1.0

    show TEACHER with dissolve 

    "Just as you're wiping off the drool from your mouth, Mrs. Pineda, the Social Studies teacher, summons you to the teacher's table."

    pineda "Bee, were you sleeping in my class?"

    "Yikes. What are you even supposed to say to that?"

    pineda "Please tell me you weren't sleeping in my class. Did you find it that boring?"

    "Damned if you agree, damned if you don't."

    pineda "Bee, are you listening?"

    bee "Yes, Ma'am. I'm sorry, Ma'am."

    "You promise Mrs. Pineda you'll never sleep in her class again."

    hide TEACHER with dissolve 

    "You return to your seat to get your backpack."

    show VIDA POKERFACED with dissolve :
        xalign 0.25

    show KARIS POKERFACED with dissolve :
        xalign 0.75

    "Vida's there too, sitting on your chair."

    vida "What was that about?"

    karis "Let me guess. She caught you napping."

    bee "Gee, thanks for waking me up."

    karis "I tried. Kicked your chair and everything."

    karis "But you were sleeping like you were dead, you know?"

    hide VIDA with dissolve 

    hide KARIS with dissolve 

    scene bg black with fade

    scene bg TRAFFIC with fade

    "On the ride home, the other girls on the bus giggle and bat their eyes at the St. Michael's boys."

    "Well, one boy in particular. From the very first day he transferred to your bus, the girls have been talking."

    "One girl says he looks like Coco Martin. Another girl says he looks just like Jericho Rosales. "

    "You have nothing to contribute to this conversation since you have no idea what these celebrities look like. You don't watch telenovelas."

    "You don't blame your schoolmates for gushing though. "

    "Outside of the few St. Michael's boys who take this bus, there aren't many other opportunities to meet boys."

    "It begins to rain outside. "

    "The sudden sort of rain that seems to explode, angry, from the sky. That's tropical climate for you."

    "Everyone on the bus begins fumbling with the windows, yanking them shut so the rain can't get in."

    "You don't, though. The raindrops feel nice and cool on your face, especially after the day's humid weather."

    "Yeah, the rain isn't all good. It has acid and chemicals and stuff. "

    "You know that, but still. It sure beats the stuffy atmosphere of this bus."

    "At this point, you catch the resident heartthrob staring at you. "

    "Maybe he's wondering why you're smiling even as you welcome the acid rain on your face."

    "What's his name again? Paolo? Or is it Piolo?"

    "Paolo/Piolo flashes a smile at you."

    "You return his stare with a deadpan expression. His smile stiffens somewhat."

    "Once he breaks eye contact, you resume gazing out the window at the rain. "

    "The momentum of the bus has slowed to a crawl. This usually happens when it rains. Traffic gets bad. "

    "You don't really get the logic behind it, but that's the way it is."

    "Maybe you have time to squeeze in a quick daydream before the bus reaches your house."
    return
    
label lbl_part_32:
    call lbl_part_32_reuse from _call_lbl_part_32_reuse
    jump lbl_part_34



label lbl_part_33:

    call lbl_part_32_reuse from _call_lbl_part_32_reuse_1

    jump lbl_part_35



label lbl_part_34:

    stop music fadeout 1.0

    play music DREAMS fadein 1.0

    show UMI POKERFACED with dissolve 

    umi_q "If you tell me to run, I shall run."

    "The boy who looks and sounds like Umi--but who isn't really Umi--has suddenly appeared beside you on the bus."

    umi_q "The rain does not matter. I shall not get wet, or sick, or tired."

    umi_q "As long as you ask, I can do anything in the world."

    "You incline your head once."

    "Without further ado, the boy sails out the window, landing on the concrete outside."

    hide UMI with dissolve 

    "He walks alongside the bus, weaving around tricycles and jeepneys. "

    "When the bus finally untangles itself from the traffic jam, he begins to run. "

    "He ducks around passers-by with a grace that resembles dancing."

    "He leaps over fences and gates. No obstruction is too tall for how high he can jump."

    "He can even reach the tops of streetlights and telephone poles."

    "And every time he returns to the ground, his landing leaves a crater in its wake."

    "These craters may be invisible to everyone except you, but that doesn't make them any less impressive."

    stop music fadeout 1.0

    "You begin to hum the {i}Psychowrath{/i} opening theme as you watch his progress outside. "

    "You only stop once one of the girls on the bus gives you a weird look."

    scene bg black with fade

    jump lbl_part_36



label lbl_part_35:

    "For some reason, your brain jumps instantly to Vida. "

    "Almost like it's been dying to picture her all this time and just needs permission to begin."

    "Well, you won't give your brain that permission. "

    "Your brain's a pervert. You gotta rein it in before it rampages."

    scene bg black with fade

    stop music fadeout 1.0

    play music DREAMS fadein 1.0

    "Instead, you try to imagine being in a relationship with Paolo/Piolo."

    "Let's say he's holding your hand as you walk the short distance from the bus to the front door of your house."

    "The girls on the bus crane their necks to watch through the windows. They elbow each other as Paolo/Piolo pecks your cheek as a farewell."

    "The girls are burning with jealousy, as you've somehow managed to win over a boy as hot as Coco Martin or Jericho Rosales (whichever is the hotter one)."

    "The bus driver watches too, hoping Paolo/Piolo hurries up and returns to the bus, so that he can get on with his bus route and go home to his wife."

    "But as the bus driver witnesses this touching scene between young lovers, even he recalls the long-lost days of his first love...."

    stop music fadeout 1.0

    scene bg TRAFFIC
    

    "This entire scenario is just way too ridiculous. "

    "You can't help giggling to yourself."

    "You only stop once one of the girls on the bus gives you a weird look."

    scene bg black with fade

    jump lbl_part_37



label lbl_part_36_reuse:

    scene bg LIVING_ROOM with fade

    play music SLICE_OF_LIFE fadein 1.0

    "Sprawled over the sala couch, you're secretly reading {i}A Little Princess{/i} by Frances Hodgson Burnett behind your {i}Philippine History{/i} textbook."

    "Just as the imaginary royal feast of Sara, Becky, and Ermengarde is interrupted by Ms. Minchin, a burst of laughter causes you to look up."

    show ATE SMILING at center with dissolve

    "Ate's grinning down at her cellphone."

    bee "Let me guess. Jaime said a funny thing?"

    ate "Yeah. But you wouldn't get it. Inside joke."

    "You watch as she texts him back at the speed of light."

    bee "You think Mom will ever buy me a phone?"

    show ATE POKERFACED at center

    ate "Who would you even text?"

    bee "My friends? But I can always talk to them at school, I guess."

    ate "When you get a boyfriend, then you get a phone."

    hide ATE with dissolve 

    "Why is getting a boyfriend a prerequisite for getting a phone? "

    "But you don't ask this question out loud. "

    "Ate's the expert when it comes to boyfriends. You don't want her to call you a clueless loser."
    return
    
label lbl_part_36:
    call lbl_part_36_reuse from _call_lbl_part_36_reuse
    jump lbl_part_38



label lbl_part_37:

    call lbl_part_36_reuse from _call_lbl_part_36_reuse_1

    jump lbl_part_39



label lbl_part_38:

    "You've never really pictured getting a boyfriend before. If a 3-D boy was as cool and smart and beautiful and strong as Umi, maybe. "

    "But it's highly unlikely that someone that perfect exists in real life."

    jump lbl_part_40



label lbl_part_39:

    "You grimace as you recall your ridiculous daydream back on the bus. "

    "Gross. Maybe you'll just never get a boyfriend."

    jump lbl_part_41



label lbl_part_40_reuse:

    show ATE POKERFACED with dissolve 

    "As you're busy musing about boyfriends, Ate finally puts down her cellphone and goes back to perusing the pages of her gigantic textbook on human anatomy."

    "Ate's textbooks are so riddled with highlights at this point that they're more colorful than white. "

    "You pick up a pink highlighter and draw a heart on the corner of a page of your textbook."

    show ATE IRRITATED

    ate "What are you doing?"

    "Ate's looking suspiciously at you."

    "You shove away {i}A Little Princess{/i} so that the novel tumbles unceremoniously to the floor."

    bee "Nothing. Just marking this page of my textbook. It's super important."

    ate "Don't use my pink highlighter. It's my favorite, so the ink's running out."

    ate "Here, use this one instead."

    "You take the orange highlighter she beckons to you. "

    "Because she's still watching, you take it upon yourself to color a random line of text."

    hide ATE with dissolve 

    "Is it important to remember that Imelda Marcos left behind fifteen mink coats and over a thousand pairs of shoes when she fled Malacañang Palace?"

    "No? Well, it's highlighted in sickly orange now."

    "Within minutes of pretending to be keenly interested in the corrupt legacies of your country's roster of presidents, you're nodding off."

    "You smoosh your cheek against a grayscale photograph of Fidel Ramos smoking a cigar. "

    "You'll just rest your eyes for a bit. Just five minutes, tops."

    scene bg black with fade

    stop music fadeout 1.0

    play music DREAMS fadein 1.0

    "Mmm. Sweet oblivion."

    "When you open your eyes, you're still lying on the couch. "

    "Rain still slashes against the windows."

    "But someone must have switched off all the lights. Or the power must be out. "

    "It's dark, but not so dark that you can't see that Ate's not hunched over the sala table like she should be."

    "You seem to be alone."

    "Then something stirs at the edge of your vision."

    bee "Who's there?"
    return
    
label lbl_part_40:

    call lbl_part_40_reuse from _call_lbl_part_40_reuse
    jump lbl_part_42



label lbl_part_41:

    call lbl_part_40_reuse from _call_lbl_part_40_reuse_1

    jump lbl_part_43



label lbl_part_42:

    mystery "There is no need to fear. It is only I."

    "That voice...."

    bee "Umi-kun?"

    "You squint as you search the room for him. "

    "There. That dark figure standing on the other side of the sala table. "

    "That must be Umi. Or at least the boy who looks and sounds just like Umi."

    bee "Can you get the lights? I can barely see you."

    "A hand touches your shoulder."

    umi_q "Do not fret. I am here now, right behind you."

    "Your blood runs cold."

    bee "Then who--"

    "The dark figure you've mistaken as Umi begins to walk around the sala table."

    umi_q "You have been afraid for far too long. Let go of your fear now."

    umi_q "Sora and I are here for you. We are a part of you."

    bee "Sora-kun is here too?"

    "The dark figure sits on the edge of the sala table directly in front of you. His silvery hair gleams in the darkness. "

    "Umi joins him. "

    "Just as you open your mouth to ask what they're up to, the TV suddenly switches on behind them. "

    "The opening theme of {i}Psychowrath{/i} blares."

    "Backlit by the flickering glow, Sora and Umi lock lips right in front of you."

    "Their kiss is so achingly passionate that it's hard to watch. "

    "Instinctively, you avert your gaze, opting instead to stare down at your hands knotted over your lap."

    "You're holding the remote control for the TV."

    menu:
        "Should you turn off the TV?"
        "Turn off the TV.":
            jump lbl_part_44
        "Keep the TV on.":
            jump lbl_part_45



label lbl_part_43:

    "A finger touches your lips. "

    "Its owner makes a soothing sound, then a shushing sound."

    "Maybe you should be scared, but the sudden acceleration of your heartbeat has nothing to do with fear. You just know."

    "The mysterious person settles next to you on the couch and guides your hands toward some soft fabric."

    "Your fingers detect the indentation of buttons. You trace the miniscule circular shapes. "

    "Do you dare?"

    mystery "Go on. Open it."

    "That voice...."

    bee "Vida?"

    vida "Who else would I be? How long do you intend to keep me waiting?"

    "You swallow. Your throat is suddenly parched."

    "It's now or never."

    menu:
        "Do you dare to open it?"
        "Yes, you do dare.":
            jump lbl_part_53
        "No, you don't dare.":
            jump lbl_part_54



label lbl_part_44:

    "Your arm trembles as you lift the remote control to press the power button."

    "For just a split second, the room is once more enveloped in darkness, and the silhouettes in front of you break apart. "

    "But then--"

    stop music fadeout 1.0

    scene bg LIVING_ROOM
    

    "The sala lights suddenly pop open, like a punch to your eyes."

    "Sora and Umi have vanished."

    "You jerk up from your prone position on the couch. "

    "Oh no, you've drooled all over Fidel's poor face. His cigar's all wavy now."

    play music SLICE_OF_LIFE fadein 1.0

    show ATE POKERFACED with dissolve 

    ate "Have a nice nap?"

    bee "I had a weird dream."

    ate "Oh yeah? What about?"

    "Blowing on the damp spot on your textbook, you consider what you're going to tell her."

    bee "Umi was in it. He was here in the sala with me."

    show ATE IRRITATED

    ate "You already see Gay Boy on TV when you're awake. Now you gotta see Gay Boy in your dreams too? God, what a nightmare."

    bee "It wasn't that bad. Weird, yeah, but not bad."

    ate "So what was Gay Boy doing? Crying again? Telling you his sob story for the bajillionth time?"

    bee "I can't really remember."

    hide ATE with dissolve 

    scene bg black with fade

    jump lbl_part_48



label lbl_part_45:

    "You toss the remote control aside. "

    "Taking a deep breath, you look up from your lap. "

    "You face Sora and Umi head-on."

    "At this point, Umi tears off Sora's shirt. "

    "As if in retaliation, Sora pins Umi down on the table."

    "Sora dives down to crush their lips together again. "

    "Umi groans as Sora forces his knee between Umi's legs."

    "There's a distinctive bulge in Umi's pelvic region. "

    "You lean in to look more closely at it. "

    "You're on the edge of your seat now--"

    stop music fadeout 1.0

    scene bg LIVING_ROOM
    

    "You crash down to the floor with a strangled yelp."

    show ATE SHOCKED  at center with dissolve

    ate "Holy shi--"

    ate "Bee, are you okay? What the hell happened?"

    "You jump back up, forcing a smile."

    bee "Just fell off the couch. I'm okay."

    play music SLICE_OF_LIFE fadein 1.0

    show ATE POKERFACED at center

    "Ate sighs, one hand over her heart."

    ate "God, you really scared me."

    bee "Sorry. Just dozed off. I didn't plan to."

    ate "Yeah, no kidding. You were tossing and turning before that."

    ate "And talking in your sleep. Just a little bit."

    hide ATE with dissolve 

    "Sleep talking? You cast your mind back to the dream. "

    "Could you have said anything embarrassing? Or even incriminating? "

    "Even now, you're forgetting the details. But you do remember how it made you feel. "

    "How your heart hammered as you leaned in closer."

    "But now all you feel is this overwhelming urge to write. This chaos in your head and heart can't be contained otherwise."

    scene bg black with fade

    scene bg BEDROOM with fade

    "Alone now in your bedroom, the idea hits you. "

    "Why not write your own fanfic? You've read enough fanfics to last you a lifetime, so why not write your own this time?"

    "You boot up your ancient PC and poise your fingers over the keys."

    "You run through the internal catalogue you keep of scenarios and scenes. "

    "Once you decide on a suitable one, it's time to type."

    stop music fadeout 1.0

    play music INSPIRING fadein 1.0

    nvl clear 
    nvl_narrator "{i}On the 40th day of their journey into the desert they ran out of food. All they had left was a half jug of water.{/i}"

    nvl_narrator "{i}Umi formulated a plan. What if Dr. Karigari's last mind-controlled minion took the water jug and ran as fast as possible to fetch more food and water?{/i}"

    nvl_narrator "{i}The others could wait in the desert. Since they would be stationary they could bear their hunger and thirst.{/i}"

    nvl_narrator "{i}\"You're a genius!\" Sora hugged Umi tightly but stopped when Dr. Karigari glared at them suspiciously.{/i}"

    nvl_narrator "{i}They all agreed this was their best bet. "

    nvl_narrator "{i}It was tiresome waiting. Dr. Karigari played solitaire. Umi read a book so boring only he could read it.{/i}"

    nvl_narrator "{i}Sora polished his weapon until he could see his reflection on it. He then saw something else reflected.{/i}"

    nvl_narrator "{i}Something behind him. The jug of water!{/i}"

    nvl_narrator "{i}Sora called to the other two. Like identical twins they gasped when they saw the jug nestled in the sand.{/i}"

    nvl_narrator "{i}\"The minion must have left it,\" Sora said, looking thoughtful. \"No use saving it for him now. He's too far.\"{/i}"

    nvl_narrator "{i}\"Only a few gulps left,\" Dr. Karigari declared. \"It's useless dividing it among us. One of us should have it.\"{/i}"

    nvl_narrator "{i}They all looked at each other then at the jug. And then came the attempts to grab it. {/i}"

    nvl_narrator "{i}Sora swiftly scooped up the jug. Umi's and Dr. Karigari's hands collided as they reached out to snatch it. The two glared at each other in displeasure.{/i}"

    nvl_narrator "{i}Sora teasingly juggled the jug over their heads. Umi caught it in midair as Sora carelessly tossed it.{/i}"

    nvl_narrator "{i}All dignity forgotten Dr. Karigari charged and tackled Umi to the sand. {/i}"

    nvl_narrator "{i}Sora stared at them in shock. The two intellectuals were brawling like wrestlers.{/i}"

    nvl_narrator "{i}Sora pulled them apart and pried the jug from Dr. Karigari's sweaty fingers. He had them sit in a triangle with the jug at its center.{/i}"

    nvl_narrator "{i}\"Cool down,\" Sora said exasperatedly. \"Let's talk this over.\" And then the protesting began.{/i}"

    nvl_narrator "{i}\"I should have it,\" Dr. Karigari said loudly. \"If not for my mind-control powers my minion wouldn't be fetching us food and water now.\"{/i}"

    nvl_narrator "{i}\"No, I should have it,\" Umi snapped. \"It was my idea to use your minion in the first place. If I hadn't suggested it we'd all be dead now.\"{/i}"

    nvl_narrator "{i}\"I'm the youngest and the fastest here,\" Sora stated furiously. \"In case of emergencies I'm the best candidate to save our dehydrated butts.\"{/i}"

    nvl_narrator "{i}After a stinging silence Umi sighed defeatedly. \"You're right, Sora. The situation's critical. The water's yours.\"{/i}"

    nvl_narrator "{i}As Sora tipped the jug over his lips he glanced at Umi. Before he knew it he was handing the bottle over to Umi. \"Here, this is for you.\"{/i}"

    nvl_narrator "{i}\"What do you mean?\" Umi said puzzledly. \"We all agreed you should have it.\"{/i}"

    nvl_narrator "{i}\"You have a point. If not for you I'd be dead now.\"{/i}"

    nvl_narrator "{i}\"Sora, I can't take this.\"{/i}"

    nvl_narrator "{i}\"Take it. I don't want it.\" Sora then stood up and walked away leaving silence in his wake.{/i}"

    
    stop music fadeout 1.0

    "At this point, you pause to crack your knuckles. "

    "You grin. You're getting to the good stuff now."

    show ATE POKERFACED with dissolve 

    ate "Hey."

    "Ate's suddenly standing by your bedroom door."

    "Yikes. How long has she been standing there? "

    "Is she a ninja?"

    play music SLICE_OF_LIFE fadein 1.0

    bee "What's up?"

    ate "Mom called. She's on the way home."

    ate "She's bringing a Chickenjoy bucket, so we should set the table."

    "Ugh. You're just getting into the groove. You don't want to stop now."

    "On the other hand, Ate might get pissed if you leave her to set the table on her own."

    hide ATE with dissolve 

    menu:
        "Should you keep the momentum going?"
        "Keep the momentum going and continue writing.":
            jump lbl_part_46
        "Take a break for dinner.":
            jump lbl_part_47



label lbl_part_46:

    "You're in the zone now, and you don't want to get out."

    show ATE POKERFACED with dissolve 

    bee "Sorry, can you go ahead without me?"

    ate "Not hungry?"

    "Maybe you can go along with that."

    bee "Yeah. I ate ... ten Hansels for lunch."

    ate "You do know we have a family history of diabetes, right?"

    bee "Yeah, I'll eat healthy from now on. No Chickenjoy for me."

    show ATE SMILING

    ate "You're going on a diet? Okay. Good idea."

    "With this, she finally exits your room. "

    hide ATE with dissolve 

    "Did she really need to insult you before leaving you alone? "

    "Ugh. Whatever. "

    "You turn back to your PC and resume writing."

    stop music fadeout 1.0

    play music INSPIRING fadein 1.0

    nvl clear
    nvl_narrator "{i}Night fell. Umi was drifting to sleep when hands shook him awake.{/i}"

    nvl_narrator "{i}\"What?\" he muttered drowsily. His eyes widened when he saw Sora sitting beside him on the sand.{/i}"

    nvl_narrator "{i}\"I'm so thirsty,\" Sora murmured.{/i}"

    nvl_narrator "{i}\"There's no water left,\" Umi said sadly. \"You gave me the remaining water, remember?\"{/i}"

    nvl_narrator "{i}\"I gave you that water because I knew,\" Sora said passionately. \"I knew you could pay me back easily. With something else.\"{/i}"

    nvl_narrator "{i}\"Something else....\" Umi echoed, his voice fading. He tried not to fall into the trap Sora was setting. But he knew he was fighting a losing battle....{/i}"

    nvl_narrator "{i}Every instinct told Umi to touch Sora. Hold him. Never let him go.{/i}"

    nvl_narrator "{i}\"It's okay, Umi,\" Sora coaxed in a sensual whisper. \"No one's watching....\"{/i}"

    nvl_narrator "{i}Enough was enough. Umi drew Sora into a heated kiss with their tongues battling for dominance.{/i}"

    stop music fadeout 1.0

    play music SLICE_OF_LIFE fadein 1.0

    "It's long past midnight when you finally finish the story. "

    "Your stomach is churning and your fingers are cramping, but you've never been so high on adrenaline."

    "On impulse, you decide to post your story to FanFiction.Net. "

    "You initially signed up to follow your favorite fanfic authors. Now, for the first time ever, you have your own story to share."

    "The second after you post it, you flop onto the bed and fall asleep, exhausted beyond belief."

    scene bg black with fade

    scene bg BEDROOM with fade

    "You only get about three hours of blissful slumber before you jerk awake again. "

    "It's not even light out yet. Or maybe that's because of the rain."

    "You dive toward your desk to check your PC, which you've neglected to switch off."

    "Heart in your mouth, you refresh the page."

    stop music fadeout 1.0

    play music INSPIRING fadein 1.0

    "There are already some reviews! Even a few favorites!"

    "You click on the reviews. "

    "A quick scan tells you that the feedback is all positive so far."

    "Even one-word reviews like \"nice :)\" and \"gay\" warm the cockles of your heart. "

    "In this context, \"gay\" is a positive response, right?"

    "With a stupid smile plastered over your face, you start typing replies to each and every review."

    "Maybe no one will respond. Maybe no one really cares."

    "But maybe, just maybe, you'll make a new friend who understands you."

    #ENDING 8/9: FanFiction.Net

    #scene bg black with fade
    #"Ending 8/9: Fanfiction.net"
    $ quick_menu = False
    scene ENDING_8 with dissolve 
    $ persistent.ending_seen_8 = True
    pause
    jump lbl_credits
    
    return


label lbl_part_47:

    show ATE POKERFACED with dissolve 

    "Nodding, you save your document and get up."

    bee "Let's go."

    "You follow Ate out of the room for dinner."

    hide ATE with dissolve 

    scene bg black with fade

    jump lbl_part_49



label lbl_part_48_reuse:

    scene bg CLASSROOM with fade

    "Tuesdays are just like Mondays, except to a lesser degree. "

    "The week isn't halfway over yet. Freedom is so far away."

    "You're muttering mutinously under your breath, minding your own business, when Vida pounces on you."

    show VIDA POKERFACED with dissolve 

    vida "Hey, have you read the new chapter yet?"

    "When you just stare blankly at her, she flicks your forehead with her fingers."

    show VIDA SMILING

    vida "I mean the new chapter of {i}My Boyfriend and His Invisible Scars{/i}, of course! You know, the Sora x Umi lemon I showed you last week?"

    "You gasp."

    bee "No!"

    vida "Yes!"

    "She whips out a stapled set of printed pages from behind her back and slams it down on your desk."

    vida "Here you go! You're welcome. Now, come on, read it before the teacher comes."

    "Because Karis hasn't arrived yet, Vida plops down on her seat. "

    "She drags the chair close to your desk so that the two of you can read side by side."
    return
    
label lbl_part_48:
    call lbl_part_48_reuse from _call_lbl_part_48_reuse
    jump lbl_part_51



label lbl_part_49:

    call lbl_part_48_reuse from _call_lbl_part_48_reuse_1

    jump lbl_part_52



label lbl_part_50:

    call lbl_part_48_reuse from _call_lbl_part_48_reuse_2

    jump lbl_part_57



label lbl_part_51:

    hide VIDA with dissolve 

    "You scan the first page of the fanfic. "

    "Clearly, this author combed the dictionary for as many synonyms for the male genitalia as they could find."

    "Should you really keep reading this stuff? You're already having weird dreams as it is."

    "If you keep indulging yourself like this, who knows what sort of graphic details your brain will conjure next?"

    "Your brain may be a pervert, but maybe it can be trained."

    "You take a deep breath, then shove the fanfic away from you."

    "The papers flutter to the floor."

    show VIDA POKERFACED with dissolve 

    bee "I don't want to read this anymore."

    vida "What? Why?"

    bee "I just don't want to. It makes me feel gross."

    vida "But we read this stuff all time. You never complained before."

    bee "So? I'm not allowed to change my mind?"

    show VIDA IRRITATED

    "Vida narrows her eyes at you. Then she grabs the print-out from the floor."

    vida "Fine. Whatever. Be that way. I don't care."

    "You watch her back as she stalks off."

    hide VIDA with dissolve 

    "Sighing, you take your {i}Philippine History{/i} textbook from your backpack and turn to the assigned page. "

    "There's a pink heart on the corner of the page. "

    "But it doesn't really look like a heart. It's too wonky. "

    "It looks more like a boy's testi--"

    "No. Concentrate."

    "Stop seeing things where there's nothing to see."

    "Be pure. Be holy."

    #ENDING 7/9: Gay Minus

    #scene bg black with fade
    #"Ending 7/9: Gay Minus"
    $ quick_menu = False
    scene ENDING_7 with dissolve 
    $ persistent.ending_seen_7 = True
    pause
    jump lbl_credits
    
    return


label lbl_part_52:

    "Maybe you should tell her what you were up to last night."

    bee "You know, I brought my own too. A Sora x Umi fanfic."

    show VIDA POKERFACED

    vida "Is it by KissyKitsune69?"

    bee "No."

    vida "KissyKitsune69 understands the Sora x Umi dynamic best. Let's read that other one later, okay?"

    bee "I wrote this one."

    "Because you didn't have time to finish writing your fanfic last night, you decided to print it out before going to school."

    "There's a pause as you beckon the draft of your fanfic toward Vida. "

    "Will she laugh at you? Tease you?"

    stop music fadeout 1.0

    play music INSPIRING fadein 1.0

    "She doesn't."

    "She snatches the print-out from your hand and leans forward eagerly to read it."

    show VIDA BLUSHINGSMILE

    "There's a hungry expression in her eyes. "

    "You've seen this look before, but you've never been the one to trigger it. It's an odd feeling."

    "After an excruciating five minutes, she finally looks up. "

    "You steel yourself for an unfavorable comparison with KissyKitsune69's superior oeuvre."

    vida "So what happens next?"

    "You blink in surprise."

    bee "Haven't written it yet."

    vida "Write it now. I need to know."

    #ENDING 9/9: Fujoshi Fanclub

    #scene bg black with fade
    #"Ending 9/9: Fujoshi Fanclub"
    $ quick_menu = False
    scene ENDING_9 with dissolve 
    $ persistent.ending_seen_9 = True
    pause
    jump lbl_credits
    
    return


label lbl_part_53:

    "Taking a deep breath, you begin to undo the buttons of her blouse."

    "Once it's fully unbuttoned, you hesitate. "

    "She says nothing. Maybe she's still waiting for something. "

    "Fingers trembling, you pull the blouse open, peeling it back until her shoulders are exposed."

    vida "Well? Aren't you going to touch?"

    bee "I want to see right now. I want to see it."

    stop music fadeout 1.0

    scene bg LIVING_ROOM
    

    "The sala lights suddenly pop open, like a punch to your eyes."

    "But Vida is nowhere to be found."

    show ATE POKERFACED with dissolve 

    ate "See what? What do you want to see?"

    "You jerk up from your prone position on the couch. "

    "Oh no, you've drooled all over Fidel's poor face. His cigar's all wavy now."

    play music SLICE_OF_LIFE fadein 1.0

    ate "You were sleep talking just now."

    hide ATE with dissolve 

    "Sleep talking? You cast your mind back to the dream. "

    "Could you have said anything embarrassing? Or even incriminating? "

    "Even now, you're forgetting the details. But you do remember how it made you feel. "

    "How your heart accelerated. How your hands shook in anticipation."

    "But now all you feel is this overwhelming urge to write. This chaos in your head and heart can't be contained otherwise."

    scene bg black with fade

    scene bg BEDROOM with fade

    "Alone now in your bedroom, you pull out your diary from your underwear drawer."

    "You flop down the bed and flip through the pages. These entries date back to 2005. "

    "Used to be you wrote here nearly every day, but ever since you entered high school, all the writing has happened inside your head."

    "However, the moment you uncap your pen, the words fall on the page as easily as if they've never stopped flowing."

    stop music fadeout 1.0

    play music INSPIRING fadein 1.0

    nvl clear 
    
    nvl_narrator "{i}Dear Diary,{/i}"

    nvl_narrator "{i}Today I had a dream. It was weird and overwhelming. When I woke up I felt guilty. Like I did something wrong.{/i}"

    nvl_narrator "{i}I never told you about this girl. This new friend I made at school. Dunno if she's pretty but she has this way about her.{/i}"

    nvl_narrator "{i}I can talk to her about everything (except this). She won't judge. How can she, she's worse than me. Way worse. I mean perverted.{/i}"

    nvl_narrator "{i}In my dream I took off her shirt. Or I almost did. It was dark and hard to see.{/i}"

    nvl_narrator "{i}She asked me if I wanted to touch. And I did. But I woke up before I did. {/i}"

    nvl_narrator "{i}My body felt funny when I woke up. My head was all messed up.{/i}"

    nvl_narrator "{i}I can't talk about this to anyone or they'll hate me. I'm gross. But you won't hate me so it's okay if it's you.{/i}"

    stop music fadeout 1.0

    "You pause. Maybe you should just sign off here. "

    "You still feel dirty, but at least some of the dirt has rubbed off you and onto the page."

    "But a certain itch nags at your brain. Have you really said everything you needed to say?"

    menu:
        "Should you keep writing in your diary?"
        "Keep writing in your diary.":
            jump lbl_part_55
        "Stop writing in your diary.":
            jump lbl_part_56



label lbl_part_54:

    stop music fadeout 1.0

    "No. "

    "You're not doing this. This just doesn't feel right."

    "You can't do something like this to a friend. Not even if it's just a dream."

    "It's time to wake up."

    scene bg LIVING_ROOM
    

    "You open your eyes. "

    "You pull yourself up from your prone position on the couch. "

    "Oh no, you've drooled all over Fidel's poor face. His cigar's all wavy now."

    play music SLICE_OF_LIFE fadein 1.0

    show ATE POKERFACED with dissolve 

    ate "Have a nice nap?"

    bee "I had a weird dream."

    ate "Oh yeah? What about?"

    "Blowing on the damp spot on your textbook, you consider what you're going to tell her."

    bee "I was sitting here in the dark. You weren't here, but someone else was. She whispered things to me."

    ate "Creepy. What was she whispering about?"

    bee "I can't really remember."

    hide ATE with dissolve 

    scene bg black with fade

    jump lbl_part_50



label lbl_part_55:

    "You pick up your pen and resume writing."

    play music INSPIRING fadein 1.0

    nvl clear
    nvl_narrator "{i}Wait. No. That's not the full story here.{/i}"

    nvl_narrator "{i}I've had other dreams before. But I never wrote about them. I felt ashamed.{/i}"

    nvl_narrator "{i}I mean dreams about ... girls. Yeah. I know.{/i}"

    nvl_narrator "{i}Disgusting. Dirty. Perverted. That's me.{/i}"

    nvl_narrator "{i}Before my friend there was Assunta de Rossi. And before Assunta there was Beyoncé Knowles from Destiny's Child. {/i}"

    nvl_narrator "{i}All girls. Girls I find ... sexy. Yeah. I really said that. Gross, right?{/i}"

    nvl_narrator "{i}Boys I don't really dream about. I mean 3-D boys, of course.{/i}"

    nvl_narrator "{i}Boys are gross. Girls aren't gross but I'm gross for dreaming about them.{/i}"

    nvl_narrator "{i}Maybe I just don't know any boys. But I don't understand what there is to like about them. {/i}"

    nvl_narrator "{i}I've never liked a boy and maybe I never will. Not like the way Ate does anyway. {/i}"

    nvl_narrator "{i}Ate's got a boyfriend so she knows everything there is to like about boys.{/i}"

    nvl_narrator "{i}I wish I was like Ate. {/i}"

    nvl_narrator "{i}Everything's so easy for her. I wish it was the same for me.{/i}"

    stop music fadeout 1.0

    show ATE POKERFACED with dissolve 

    ate "Hey."

    "Ate's suddenly standing by your bedroom door."

    "Yikes. How long has she been standing there? "

    "Is she a ninja?"

    "You slam your diary shut."

    play music SLICE_OF_LIFE fadein 1.0

    bee "What's up?"

    ate "Mom called. She's on the way home."

    ate "She's bringing a Chickenjoy bucket, so we should set the table."

    bee "Oh. Great."

    ate "Hey, you okay? You look kinda freaked."

    "Well, Ate did materialize out of thin air just as you were writing about her in your diary, so...."

    bee "Yeah, I'm okay. Let's go."

    "You drag yourself up from the bed, shoving your diary under your pillow as you go. "

    "Then you follow Ate out of the room for dinner."

    hide ATE with dissolve 

    scene bg black with fade

    scene bg BEDROOM with fade

    "That night, you toss and turn in bed. "

    "Now that you've learned this scary new thing about yourself, will everything change?"

    stop music fadeout 1.0

    "Because you take too long to drift off, you end up oversleeping the next morning."

    "The moment you check the time on your watch, you're jumping off the bed and rushing out the room."

    scene bg black with fade

    scene bg LIVING_ROOM with fade

    show MOM with dissolve 

    "In the sala, Mom's sitting alone on the couch."

    "What's she doing here? Why isn't she at work?"

    bee "Mom, why didn't you wake me up?"

    bee "Are classes suspended because of the rain?"

    play music PARANOIA fadein 1.0

    "Mom stares silently at you for a moment before she replies."

    mom "You're not going to school today. I need a good long talk with you."

    mom "Thanks to your sister, something ... {i}troubling{/i} has come to my attention."

    "She gazes down at her lap. "

    "Your eyes follow hers."

    "A familiar notebook rests on her lap, underneath her clasped hands."

    "It's dirty. Filled with secrets."

    "Just like you, come to think of it."

    #ENDING 4/9: Discovery by Mom

    #scene bg black with fade
    #"Ending 4/9: Discovery by Mom"
    $ quick_menu = False
    scene ENDING_4 with dissolve 
    $ persistent.ending_seen_4 = True
    pause
    jump lbl_credits
    
    return


label lbl_part_56:

    "Maybe that's enough for now. "

    "You don't even fully understand what you feel, so how can you hope to write about it?"

    "You sign off the entry. You then tuck the diary carefully underneath your rattiest panties. "

    "No one will ever touch those, so no one will check there."

    play music SLICE_OF_LIFE fadein 1.0

    "Maybe you should head back to the sala now. Reacquaint yourself with the mink-coat-wearing Imelda and the cigar-smoking Fidel."

    "Groaning at the prospect, you drag yourself up from the bed."

    scene bg black with fade

    jump lbl_part_50



label lbl_part_57:

    "Though you attempt to train your eyes on the page, they can't help straying to Vida's hands resting on your desk."

    "Every so often, her index finger traces a line in the story that she finds particularly funny or thrilling."

    "Even though you've barely absorbed a word of the story, you laugh when she laughs, and gasp when she gasps."

    "She's sitting so close. "

    "Close enough that if you lean forward by just a few centimeters, you can whisper into her ear."

    "Maybe you should just tell her."

    hide VIDA with dissolve 

    menu:
        "Should you take this opportunity to tell Vida your true feelings?"
        "Tell Vida you like her.":
            jump lbl_part_58
        "Don't tell Vida you like her.":
            jump lbl_part_59



label lbl_part_58:

    stop music fadeout 1.0

    play music INSPIRING fadein 1.0

    "You lean in, close enough that she must feel your breath tickling her ear."

    "Then you whisper the truth."

    bee "I like you."

    show VIDA POKERFACED with dissolve 

    "She jerks backward. Have you scared her away now?"

    "Maybe you should take it back. Pass it off as a bad joke."

    "But then--"

    vida "You like me?"

    vida "Just ... 'like'? That's all?"

    bee "No! I mean, I ... I love you."

    "A brilliant smile lights up her face."

    show VIDA BLUSHINGSMILE

    vida "Good, because I love you too."

    "Just as the {i}Alleluia{/i} chorus starts playing inside your head, Vida leans in, and--"

    hide VIDA with dissolve 

    show BEE_X_VIDA_KISS_CG with dissolve 

    "She kisses you."

    "Her kiss is soft, like cumulus clouds."

    "Her kiss is sweet, like strawberry-flavored Chupa Chups."

    "Her kiss is--"

    "Too good to be true."

    hide BEE_X_VIDA_KISS_CG
    

    stop music fadeout 1.0

    show VIDA IRRITATED
    

    vida "Bee? Are you listening?"

    vida "You still here with me? Earth to Bee! Earth to Bee!"

    "Her voice drags you down from the daydream."

    "You're hurtling back to Earth from the clouds."

    play music SLICE_OF_LIFE fadein 1.0

    bee "Yeah, sorry. I'm here now."

    show VIDA POKERFACED

    "She shakes her head and tuts at you."

    vida "Jeez, get your head out of the clouds, okay?"

    "You wish you could."

    #ENDING 6/9: Head in the Clouds

    #scene bg black with fade
    #"Ending 6/9: Head in the Clouds"
    $ quick_menu = False
    scene ENDING_6 with dissolve 
    $ persistent.ending_seen_6 = True
    pause
    jump lbl_credits
    
    return


label lbl_part_59:

    "No, that's stupid. Confessing will just ruin everything."

    "She'll hate you. She won't want to be your friend anymore."

    "Besides, do you even really like her that way? "

    "So you dream about her. So what? "

    "That's just because you don't have anyone better to dream about, right?"

    "You force yourself to stare directly at the print-out in front of you. "

    "You're still not taking in a word it says. Might as well be gibberish."

    "Just like this, faking it all the way until the end, you finally reach the last page of the story."

    show VIDA BLUSHINGSMILE with dissolve 

    vida "It's good, huh? Smexy goodness? A real hot ending?"

    bee "Yeah. A real hot ending."

    #ENDING 5/9: A Real Hot Ending

    #scene bg black with fade
    #"Ending 5/9: A Real Hot Ending"
    $ quick_menu = False
    scene ENDING_5 with dissolve 
    $ persistent.ending_seen_5 = True
    pause
    jump lbl_credits
    return
    
label lbl_credits_from_menu:
    call lbl_credits from _call_lbl_credits
    return
    
label lbl_credits:
    
    # End Credits
    
    #Play menu music if in replay mode
    if (_in_replay):
        play music SLICE_OF_LIFE fadein 1.0

    ## We hide the quickmenu for the End Credits so they don't appear at the bottom.
    $ quick_menu = False

    $ credits_speed = 20 # Scrolling speed in seconds
    scene bg sketchbook # Replace with a proper background if desired
    with dissolve
    #show theend:
    #    yanchor 0.5 ypos 0.5
    #    xanchor 0.5 xpos 0.5
    #with dissolve
    #with Pause(0.5)
    #hide theend with dissolve
    show cred at Move((0.5, 2.2), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    
    #replay to show credits without the thanks for playing bit
    $ renpy.end_replay()
    
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks with dissolve


    if persistent.extras_unlocked:

        pass

    else:

        centered "You've unlocked the Extras Menu.\nAccess it through the Main Menu."
        # show extras_unlock with dissolve
        # with Pause(3)
        # hide extras_unlock with dissolve

        $ persistent.extras_unlocked = True
        
    ## We re-enable the quickscreen as the credits are over.

    $ quick_menu = True

    # This ends the game.

    return
