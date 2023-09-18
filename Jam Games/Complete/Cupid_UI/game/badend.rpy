#BUILD 12
label badend:
    scene bg black with slowdissolve
    $save_name = "chapter 7: the taste of honey"

    scene bg black  
    
    scene bg hallwaydark  
    show gf petulant with None

    "Voices wafted around Guilleme's ears."
    show gf petulant  :
        xalign 0.52
    "Ever since he woke up from the dream, his vision doubled."
    "He would be walking on the floor one minute, then slipping the next. "
    show gf petulanttalk  :
        xalign 0.5
    "Guilleme held on to the wall."
    "The spell hadn't ended yet."
    play music "sfx/whisper.ogg"    
    "He hated the feeling of being powerless."
    if dagger:
        "He clenched his fists, chewing on his lip to keep himself awake."
    else:
        "He gripped the dagger, chewing on his lip to keep himself awake."
    "The domain of sleep rendered him most vulnerable."
    "His attacker must have known this too."
    "Guilleme tripped and stead himself with difficulty."
    show gf silentpain
    "{i}...Rosa.{/i}"
    "So, she was a witch."
    "How come he never noticed before?"
    "The years had made him soft."
    "Guilleme clenched his jaw."
    show gf petulantsmile  
    g "{i}Either way, it doesn't matter. It was starting to get boring, anyway.{/i}"
    #"Besides, negative sentiment against the nobility have been growing all over France recently."
    #"Something was bound to happen soon."
    "It was almost time to leave."
    show gf petulant  
    "He just had to deal with Rosa tonight. Then he'd pack his bags and leave for Asia."
    show gf petulantsmile  
    "Guilleme smiled, despite his nausea."
    g "Just you wait, my dear."
    show gf petulanttalk    
    g "I'll pay you back for your contempt."
    scene bg black  
    play sound "sfx/churchdoor.ogg"
    "He opened the door to Catherine's room."

    scene bg cathroomeros with slowdissolve
    stop music fadeout 2.0

    "A red candle shone on the table, painting the room an ominous bloody crimson. "
    "The salty musk of sex hung heavy in the air, and Guilleme's vision floundered once again."
    "His anger led him here without enough forethought."
    "Suddenly, he felt unprepared. A prickle of fear stained his pride."
    if dagger:
        "More than anything, he suddenly craved to have any sort of weapon."
    else:
        "His hand tightened on the dagger."
    play music "sfx/creepyfinal.ogg"    
    "Guilleme squinted."
    "The dark figure shifted."
    "Low rousing moans came from the silhouette."
    "The moans increased in speed as he stepped nearer."
    "Guilleme's mouth salivated."
    "A final soft squeal came, and the figure stepped into the light of the candle."
    #$ achievement.grant()
    $achievement.Sync("Pat the Bunny")
    show rs aroused with Dissolve (0.4, alpha=True)
    r "Hi, Gilly!"
    g "..."
    r "Thanks for waiting for me to finish!"
    show rs tongue  
    r "I got so excited at the thought of you coming over that I couldn't help myself."
    r "It feels good to release pent-up frustration, doesn't it?"
    "The woman stepped forward, and Guilleme took a step back, his step faltering."
    r "See..."
    r "You are my {i}biggest{/i} frustration."
    show rs angryaroused  
    r "Years, Guilleme, years!"
    r "I held myself back."
    r "Fighting my own nature!"
    show rs aroused  
    r "For what?"
    r "I don't even know anymore."
    "Sweat dribbled on Guilleme's brow. He wiped it off."
    "He felt his muscles tensing, a clenching in his abdomen akin to being touched."
    g "...What do you want?"
    show rs crazylaugh  
    "Rosa giggled."
    show rs angryaroused  
    if punish:
        r "Punishment."
    else:
        r "Retribution."
    show rs crazylaugh  
    g "..."
    r "But not before I get to play around!"
    r "Mother allowed me just this once."
    r "A reward for being a good girl."
    show rs aroused  
    "Guilleme's vision as spun as a wave of putrid force hit him. Cold sweat broke on his scalp."
    "Suddenly, it was harder to breathe."
    if dagger:
        "He clenched his fist."
    else:
        "He clutched his dagger and brandished it."
    g "R-Release me from this spell now!"
    g "I'm warning you."
    r "That is adorable."
    "She stepped towards him."
    "Guilleme saw a glint of something sharp in one of her hands."
    if dagger:
        "It was his dagger."
        "He gritted his teeth."
    g "D-Damn..."
    "Didn't he sound like a pathetic child just now, whining for his captor to release him?"
    "But what could he do?"
    "He should've planned this better."
    show rs aroused  
    r "Do you really want to fight me, Guilleme?"
    show rs crazylaugh
    r "I {i}know{/i} how to {i}kill{/i} you~!"
    r "A strike to the heart."
    r "A wound that will never heal."
    "She taunted in a sing-song way."
    show rs aroused
    r "And this spell..."
    r "I made this spell especially for you."
    r "Your own power of emitting desire is used against you."
    r "It makes my spell more powerful, while you become weaker."
    show rs crazylaugh
    r "You must admit, it is impressive."
    g "..."
    show rs aroused
    r "I am more powerful than you, Guilleme."
    "Guilleme choked on his own spit. He dragged air into his lungs, but every gulp seemed to drown him."
    r "What does it feel like, being seduced against your own will?"
    scene bg rgseduce
    "She stepped even closer to him, so close that her bosom rubbed on his arm. He couldn't even push her away."
    #"Guilleme couldn't move. His arms felt heavy and numb."
    if dagger:
        "He felt a sharp, light poke of metal on his ribs."
        if persistent.adult:
            "A small patch of red dampened his shirt."
            $ achievement.grant("Drawing Blood")
            $achievement.Sync()
    elif knife:
        "He felt a sharp, light poke of metal on his ribs."
        if persistent.adult:
            "A small patch of red dampened his shirt."
            $ achievement.grant("Drawing Blood")
            $achievement.Sync()
    else:
        "His dagger clattered to the floor as she stepped nearer."
    "Her power was double his own. The spell seemed to magnify it with her proximity."
    "She ran her hands over his chest, chasing a finger down his shirt."
    r "Getting torn down the middle must be--"
    r "{i}Excruciating.{/i}"
    r "Now you know how your victims feel, you dirty monster."
    
    g "W-Who are you?"
    r "I am your judge, Guilleme."
    r "I am your scourge. Your truth."
    r "I am like you, a creature that emanates and feeds on desire."
    r "But unlike you, I am clean. I am pure."
    
    g "W-What?"
    scene bg cathroomeros
    show rs crazylaugh  
    r "Mother's love..."
    r "She keeps me clean."
    r "I am attached to her teat and sucking at her love way after she died."

    r "Isn't it wonderful?"
    show rs angryaroused  
    if openlocket:
        r "You should know, Guilleme!"
        r "You sired me!"
        g "What rubbish are you spouting now?!"
        show rs aroused  
        "Rosa took out the locket Guilleme gave her before."
        "The locket was open now. A woman's face was inside."
        "The portrait was blurry, and the face in the picture could belong to anyone."
        "But Rosa cradled it like it was her child."
        show rs crazylaugh   
        r "Isn't Mother beautiful?"
        r "You've probably forgotten her."
        r "But she was the most beautiful woman ever. It's no wonder you fell for her, Father."
        show rs arousedhuh  
        g "You depraved witch! I am not your father!"
        g "I was never able to--"
        show rs angryaroused  
        r "Don't you dare deny it!"
        r "Mother told me so! Mother is {i}always{/i} right! {b}Always!{/b}"
        r "That is why I am here."
        g "Get away from me!"
        if punish:
            r "I am here to deliver your punishment!"
            $ achievement.grant("Punisher")
            $achievement.Sync()
        if revenge:
            r "I am the angel of vengeance!"
            $ achievement.grant("Angel of Vengeance")
            $achievement.Sync()
        show rs crazylaugh   
        r "Oh, Father, please understand. You hurt her so much."
        r "Her hate only fuelled her love."
        r "She still loves you a lot!"
        show rs aroused  
        g "Shut up!"
        "Guilleme spat."
        g "Stop calling me Father!"
        if persistent.origin:
            g "I have never had a child with that woman!"
        else:
            g "I have never had a child with any woman!"
        show rs crazylaugh  
        "Rosa just laughed."
        r "Why are you so embarrassed, Father?"
        show rs tongue  
        r "Is it because you are aroused by my body?"
        r "Do I confuse you?"
        r "Well, don't hold yourself back!"
        r "I really love you. Mother loved me, too!"
        r "Our own flesh calls out to us."
        show rs crazylaugh  
        r "Ah, isn't it romantic?"
        r "It is beautiful in its perversion."
        $ achievement.grant("Squick")
        $achievement.Sync()
        show rs aroused  
        r "We are creatures of desire."
        r "It is an inherently natural phenomenon."
        r "Any desire is justifiable, no matter how depraved."
        g "..."
        g "...You..."
        g "You are the very kind of creature I despise."
        g "Twisted. Greedy. Self-righteous."
        g "You are nothing but a rabid bitch!"
        show rs tongue  
        "Guilleme's hateful words just heightened Rosa's pleasure."
        show rs crazylaugh  
        r "Ah, I love when you call me such dirty words, Father!"
        r "I love it! I love it!"
        show rs aroused  
        r "If it distresses you, then I won't treat you like my father, but simply a man."
        $ achievement.grant("Fan Disservice")
        $achievement.Sync()
        r "Such little details don't matter to me at all."
        r "Love is all you need, isn't it?"
        show rs crazylaugh  
        r "Love conquers all!"
        "Guilleme gritted his teeth."
        show rs tongue  
        r "Yes, yes, it does."
        r "Mother loved me with her whole heart."
        r "She loved me in thought and body."
        $ achievement.grant("You don't mean..?")
        $achievement.Sync()
        show rs crazylaugh  
        r "That is why I was able to live through centuries without feeding."
        show rs aroused  
        r "Her love is the only love I need."
        if persistent.locket3WasReadBefore   is None:
            $persistent.locket3WasReadBefore = True
            $persistent.currentLinesRead +=1

    show rs angryaroused  
    r "You on the other hand, you--"
    r "You are vile!"
    r "Repugnant!"
    r "{i}Filthy!{/i}"
    
    show rs tongueoutbig  
    "Rosa licked the sweat off Guilleme's neck."
    "Her tongue slid on his skin so enticingly. The hair on Guilleme's arm stood up."
    "She was so near now. Her skin glistened with sweat."
    "Her lips were red and plump like apples."
    "Guilleme shut his eyes. He must escape. He had to run away."
    "But his mind was torn."
    if persistent.adult:
        "A part of him frolicked upon the thought of pulling her corset free and sucking on her breasts."
    else:
        "A part of him frolicked upon the thought of kissing her neck."
    "Pulling her hair."
    "Running his lips on her shoulders."
    "Pushing her wrists down onto the floor and punishing her."
    "He bit his lip, and his teeth broke through skin."
    "The pain gave him momentary control over his drugged mind."
    "If he didn't find a way to stop the spell soon, it would be his downfall."
    scene bg cathroomeros
    show rs crazylaughbig  
    r "Oh, but what a temptation you are, you shameless rake."
    r "You are enticing in your debauchery."
    r "I've been so good all these years. I didn't even feed once."
    r "And you just eat and eat and eat to your little heart's content?"
    show rs angryarousedbig  
    r "Where's your discretion, you pig?!"
    r "You even stole away Catherine's love before I got a taste!"
    r "...It's not fair!"
    show rs arousedbig  
    g "I don't know what you're talking about."
    "Rosa giggled."
    show rs crazylaughbig
    r "Don't play dumb with me."
    r "I am the only one who understands your nature."
    r "We are two of a kind."
    r "You can't lie to me!"
    show rs arousedbig  
    g "Then release me. I've done nothing to you!"
    "Rosa licked her lips."
    r "I'm sorry, darling, but I can't."
    r "As long as you exist, I can never have peace."
    r "...Knowing that you're out in the world, feeding."
    show rs crazylaughbig
    r "I'll get jealous, you see."
    show rs arousedbig  
    g "..."
    g "...You crazy witch."
    show rs crazylaughbig  
    "Rosa just laughed, and Guilleme felt a rising terror as she pressed her body against his."
    r "I love you so much."
    "Her voice was barely above a whisper."
    r "I can't control myself any longer."
    r "You will be my first and last feeding!"
    show rs tongueoutbig  
    r "Did you enjoy your dream of me, Guilleme?"
    r "I made the spell stronger now."
    r "I'll make sure you won't get away this time."
    "Guilleme was silent for a moment."
    show rs annoyedhuhbig  
    "Then, a low snicker escaped from his mouth."
    r "..."
    r "What's so funny?"
    g "You."
    g "Pathetic little girl."
    g "I pity you."
    "With these words, the spell wavered just a little bit."
    g "At least I have the decency to own my curse and not hide under self-righteous proclamations."
    g "I get to enjoy the scraps of our despicable lives."
    g "And you?"
    g "How does it taste living under your mother's rotting love?"
    g "You're probably tired of it by now, aren't you?"
    g "Mommy's love doesn't taste so good after decades of sucking on it?"
    show rs furiousarousedbig  
    "Guilleme's haunch was correct."
    "The spell was a charm to entice and seduce."
    "It was linked directly to the caster."
    "If he could distract Rosa, the hold of the charm would weaken."
    "Already, he felt sensation return to his fingers."
    g "In the end, you're just a leech; feeding off an ancient, decomposing love."
    g "It's no wonder you're insane."
    stop music fadeout 2.0
    scene bg cathroomeros
    play sound "sfx/slump.ogg"

    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    "Rosa pushed Guilleme. His back hit the floor with a thud."
    "She was still powerful, the curse hadn't lost all of its effect."
    play music "sfx/tension.ogg"
    scene bg rgchoke
    "Rosa climbed on top of him."
    if persistent.adult:
        "She rubbed her hips on his crotch furiously, angrily."
        "Her hands grabbed his manhood and squeezed."
    else:
        "She pushed on his neck with her weight and squeezed."
    "Guilleme groaned."
    play sound "sfx/grip.ogg"
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=3)
    r "{i}You do not talk about my mother that way!{/i}"
    
    "The levels of hate and desire mixed and saturated the air."
    "His mind went blank."
    r "I will make you pay for your words!"
    r "I will suck you dry until you are nothing but a husk!"
    r "I will devour your mind. I will take it all!"
    r "Your love will fill me up--"
    r "But I know Mother's love will still be the best!"
    with flash
    play sound "sfx/rip.ogg"
    "Guilleme felt the cold, sharp knife savagely tearing at his clothes."
    "Fear shook him awake from his momentary stupor."
    "But he answered this fear with laughter."
    g "Take it. Take my body."
    g "Make yourself feel good, Rosa."
    g "I feel sorry for you."
    "It had been a while since he was violated like this."
    "He thought he was able to run away by being smarter, being dominant."
    "The bitterness of being an object of desire sent a coating of gall up his throat."
    "But he only flashed a sadistic grin."
    scene bg guilchoke
    g "You don't even have to kill me soon."
    g "Why not make me your slave?"
    g "I'm sure that's a worthy punishment for all the victims I've claimed."
    "Rosa stopped again, confused at his words."
    g "You're just like the rest of them."
    "He laughed maniacally."
    if persistent.origin:
        g "Just like her."
    g "Just like everyone else."
    g "Go on, darling. Why did you stop?"
    "He was chuckling now. He stared at Rosa with eyes drenched in malice."
    "Pain sifted through the cracks."
    g "It is most {i}humbling{/i} to be reminded of my real purpose, Rosa."
    g "Use me."
    g "Use me for your pleasure, for your vengeance, or your justice."
    g "...Then throw me away."
    g "In the end, we are all just using each other."
    "He laughed again."
    g "{i}Love?{/i}"
    g "Love doesn't exist! It is just fear wrapped in a pretty package."
    g "Only desire is real."
    g "Only need."
    "He looked up at Rosa with a sneer."
    g "How much of your Mother do you really remember?"
    g "I don't remember any creature birthing me. Do you?"
    "Rosa recoiled."
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=3)
    r "S-Shut up, you worm!"
    if persistent.origin:
        g "She is not your real mother, and you know it!"
        g "This mother you speak of--"
    else:  
        g "You must admit."
        g "This mother you speak of--"
    g "--Is simply be a lunatic who wanted to believe you were her daughter."
    g "None of it is real."
    "Rosa's mouth hung open in shock."
    g "Must be why it is easy for you to use her memory to justify your filth."
    scene bg cathroomeros
    r "T-That is not true!"
    r "I love Mother with all my heart!"
    r "I'm doing what Mother wants!"
    r "I just follow her orders!"
    r "I am her vessel! She lives through me!"
    g "..."
    g "Then answer me this."
    g "Why would any mother who loves her child want her to be a murderer?"
    g "She doesn't love you. She's just using you."
    g "Same as how you are using her to survive."

    play sound "sfx/grip.ogg"
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=3)
    "Rosa clamped her hands tighter on Guilleme's neck."
    r "Shut up! Shut up!"
    r "I'm doing this because Mother is always right!"
    if punish:
        r "It's for the greater good!"
    else:
        r "I am avenging her!"
    g "...R-Really?"
    "Guilleme choked."
    g "Go on, then... why don't... you ask your Mother... why you are h-here?"
    g "Why you're {i}r-really{/i} here?"
    g "...M-Maybe she's just... enjoying the show."
    $ achievement.grant("Fourth Wall")
    $ achievement.Sync()
    r "That's not true!"
    r "Mother loves me!"
    scene bg rosacray

    "Rosa's eyes lost focus. She struggled to listen to Mother's voice."
    r "M-Mother...?"
    r "Should I really be doing this?"
    if persistent.badendWasReadBefore   is None:
        $persistent.badendWasReadBefore  = True
        $persistent.currentLinesRead +=1
    
    call m024 from _call_m024
    call lovemom from _call_lovemom

label finalmom: 
    stop music fadeout 2.0
    scene bg cathroomeros
    m "..."
    r "What? Are you not going to speak again?"
    r "Have you run out of your gall?"
    m "..."
    if persistent.adult:
        r "Say something, you bitch!"
    else:
        r "{i}Say something!{/i}"
    "Rosa screamed. Her eyes filled with tears."
    r "All this time that I have spent with you, I have always obeyed you."
    r "I loved you, Mother!"
    r "You were always so cruel to me!"
    m "..."
    r "So many times you called me a monster, blamed me and hurt me."
    r "...Despite the hurt, I never wanted to get rid of you."
    r "I-I thought..."
    r "To endure the pain... Isn't that real love?"
    r "To continue hurting proves how true my love is?"
    r "All my tears should mean something!"
    m "..."
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    r "{i}Nobody told me that was a lie!{/i}"
    m "..."
    "She continued sobbing, crumpled by the wall and pulling desperately on her hair."
    "She shouted angrily sometimes, whispered sometimes."
    "Then, her head snapped back in alert."
    "She cupped her hands on her ears. Her face contorted into worry."
    r "M-Mother?"
    r "D-Did you say something?"
    r "I didn't hear you."
    m "..."
    r "P-Please, I'm sorry."
    r "I... I didn't mean to say those things."
    r "I was just..."
    m "..."
    r "Please don't be angry."
    r "I-- I love you, Mother, please come back!"
    r "I'm nothing without you!"
    m "..."
    r "I don't want to be alone..."
    "Rosa sobbed with grief."
    r "Just come back to me, Mother! I'll never question you again!"
    "Guilleme felt his full consciousness return to him."
    "The sickly, nauseating atmosphere in the room dissipated gradually."
    "The spell was losing effect, but his body still refused to follow his orders."
    
    if dagger:
        "He crawled to where she dropped his dagger."
    else:
        "He crawled to where she dropped the large knife."
    "He stretched out his fingers to reach the weapon."
    if persistent.finalmomWasReadBefore   is None:
        $persistent.finalmomWasReadBefore  = True
        $persistent.currentLinesRead +=1
    call m023 from _call_m023
return    
label gdies:
    scene bg black  
    stop music fadeout 2.0
    $save_name = "end4: mutation"
    if(persistent.Ending4Unlocked == False):
      $persistent.Ending4Unlocked = True
      $ persistent.EndingUnlocked +=1
    "Rosa's eyes lost their sadness."
    
    stop music fadeout 2.0
    "She smiled in pure bliss at the sound of Mother's command."
    "She brought her foot down on Guilleme's outstretched hand."
    play music "sfx/badend.ogg"
    g "Aghk!"
    if dagger:
        "She picked up the dagger. It glinted at her with malice."
        "It was very sharp."
    else:
        "She picked up the meat cleaver."
        
    "Rosa lifted the blade."
    play sound "sfx/stab.ogg"
    with flashblood
    
    if persistent.adult:
        "The knife sunk deep into Guilleme's chest, almost halfway to its hilt."
        "Guilleme groaned in pain, his breath cut short by the sudden spurt of blood in his throat."
    else:
        "The knife struck his chest."
        "Guilleme groaned in pain."
    
    play sound "sfx/stabslash.ogg"
    with flashblood
    if persistent.adult:
        "She brought it up again, plunged the blade deeper, and carved downwards."
    else:
        "She brought it up again."
        
    play sound "sfx/blood.ogg"
    if persistent.adult:
        "His mouth flooded with blood."
    else:
        pass
    "Happy tears fell from Rosa's eyes."
    r "You had me so worried, Mother!"
    r "I'm so happy you're back!"
    r "I will never question you again!"
    "Guilleme sputtered, flecks of red flew as he laughed."
    g "T-Thank you, thank you."
    g "...B-Been waiting for this."
    with flashblood
    play sound "sfx/bigstab.ogg"
    "Rosa raised the weapon higher and brought it down again."
    "It pierced his heart this time."
    "Guilleme's hands clenched and flailed."
    "But he was laughing at the end."
    "{i}Oh, bliss.{/i}"
    "The pain was beginning to fade."
    "Every weight he carried shrunk as his heart went into shock."
    "..."
    if dagger:
        if persistent.adult:
            scene bg gdiesdagger
        else:
            scene bg gdiesdaggersafe
    else:
        if persistent.adult:
            scene bg gdiesknife
        else:
            scene bg gdiesknifesafe
    "Rosa watched as the life left Guilleme's body."
    "It annoyed her that his face was contorted into a sneer, as if even in his death he continued to taunt her."
    "Finally, he stopped moving."
    play sound "sfx/slump.ogg"
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=3)
    "She kicked at him with spite."
    r "Bastard!"
    r "I'm glad you're dead!"
    if persistent.adult:
        "She wiped her bloody hands on her skirt, turning the white garment red."
    else:
        "She wiped her hands on her skirt."
    r "It's a shame you didn't want to die the fun way, Gilly."
    r "You could've lived a little longer."
    "Rosa giggled."
    r "No matter."
    r "Anyone who disrespects Mother deserves to die painfully."
    "Rosa sighed with satisfaction."
    r "What shall I do now, Mother?"
    
    scene bg black
    call silence from _call_silence
    
    scene bg cathroomerosdark with Dissolve (3.0, alpha=True)
    "Rosa ran to Guilleme's body in desperation."
    "She dropped the knife."
    r "...Gilly?"
    r "Gilly?!"
    r "I-I'm sorry!"
    r "Please, don't be dead!"
    "Rosa touched Guilleme's face and slapped his cheek."
    r "Please!"
    r "You're the only one left!"
    r "...Gilly!"
    "Rosa shook his shoulders, calling his name."
    "She attempted to patch up the wound on his chest, scooping the blood back into his body."
    "His body was still warm."
    "But there was no breath left in him."
    "There was no beat in his heart."
    "Rosa had a sudden idea."
    r "If I give you my love, will it revive you? If I can take love, can I give it back?"
    r "Guilleme, I still do love you!"
    r "I do!"
    "She kissed Guilleme's lips, forcing whatever power she had into him."
    "But he didn't move, no matter what she tried."
    r "Aren't we supposed to live long lives, Guilleme?"
    r "We're supposed to be the same!"
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    r "{i}...Why are you so fragile?!{/i}"
    "Rosa hit his chest in distress."
    r "You can't be dead!"
    r "I... I've never been alone..."
    r "Please don't leave me alone..."
    "Rosa began to giggle."
    r "Mother is playing with me."
    r "Mother? Is this a game?"
    r "Are you playing hide and seek?"
    "She tore at her hair and laughed."
    r "Is Gilly also playing?"
    r "Catherine! Come join!"
    m "..."
    "Rosa sobbed."

    scene bg black  
    m "Mother!"
    m "..."
    m "Please..."
    m "I don't want to be alone!"
    m "...Please..."
    m "{i}...please...{/i}"
    $ achievement.grant("Emptiness")
    $achievement.Sync()
    scene bg black  
    $renpy.pause(delay=None)
    scene bg end04 with slowdissolve
    with Pause (2)
    scene bg black with fade
    if persistent.gdiesWasReadBefore   is None:
        $persistent.gdiesWasReadBefore  = True
        $persistent.currentLinesRead +=1
    $renpy.pause(delay=None)
    call endcredits from _call_endcredits_3

    return
    

return

label glives:
    scene bg black  
    stop music fadeout 2.0    
    $save_name = "end3: surrogate"
    if(persistent.Ending3Unlocked == False):
      $persistent.Ending3Unlocked = True
      $ persistent.EndingUnlocked +=1
    play music "sfx/whisper.ogg" fadein 2.0
    "Rosa whimpered in a corner, searching for Mother's voice."
    
    "She kept calling for Mother to talk to her, but she didn't seem to be answering."
    "She would laugh for a bit, and then stare blankly at the ceiling."
    "The candle died out - the spell lifted from the room as the last glimmer of its light faded."
    "Without Mother, without magic, Rosa sobbed, grasping at the tiny shards of her sanity."
    "Guilleme moved his limbs experimentally."
    scene bg cathroomeros
    "He pushed himself up from the floor, watching the broken girl press herself into a corner."
    "His lips stretched into a smile, an idea forming in his head."
    g "Well, I did offer to take care of you."
    g "Didn't I, Rosa?"
    "He approached the girl gingerly."
    "She scuttled away from his touch, but he cooed and coaxed until she let him touch her."
    "He stroked her head gently, smoothing her messy hair."
    "Rosa clung to his hand, kissing and nibbling at his fingers fondly."
    r "Gilly...!"
    g "Aww, you poor thing."
    r "I-I'm sorry, Gilly. Mother is not talking to me anymore."
    r "...B-But I hate her anyways."
    r "She has always been mean to me. Always so cruel..."
    g "I see."
    r "...B-But you!"
    r "You were always kind to me!"
    r "You always were!"
    r "Will you stay with me? Please tell me you'll stay with me!"
    "Guilleme tapped his finger on his chin, pretending to mull it over. He grinned."
    g "Hmm... Why not?"
    "Rosa clapped with glee and hugged Guilleme's neck."
    r "I love you, Guilleme! I always have!"
    g "Really?"
    g "Do you really love me, Rosa?"
    r "Yes, I do!"
    r "I really do!"
    r "I'm sorry!"
    r "Please don't leave me!"
    r "I don't want to be alone!"
    "Guilleme smiled."
    scene bg rgcarry2
    "He scooped the broken girl off the floor, her arms still draped around his neck."
    "She giggled to herself, still talking to the non-existent voice in her head."
    g "Do you want to come with me, Rosa?"
    g "I'm going on a trip."
    r "A trip?"
    g "Far away."
    r "You'll take me with you?"
    r "You aren't angry at me anymore?"
    r "D-{w=0.2}Do you forgive me?"
    "Guilleme dug his tongue inside Rosa's ear."
    "She moaned."
    scene bg black with None
    g "{i}Never.{/i}"
    g "But I'll take you with me, if you want."
    g "Would you like that?"
    r "I would!"
    g "In return..."
    g "You will feed me... won't you, Rosa?"
    if openlocket:
        g "You'll give your Father love?"
        r "Yes, Father! Anything you want!"
        r "Just don't leave me!"
        g "You promise?"
        $ achievement.grant("Implied Incest")
        $achievement.Sync()
    r "Yes!"
    r "I'll do anything for you!"
    g "Such a sweet girl, you are."
    scene bg rgcarry
    g "Don't worry, I won't ever leave you."
    g "You're going to be a good girl."
    "Rosa whimpered."
    "The two figures disappeared into the shadows."
    $ achievement.grant("Hostage")
    $achievement.Sync()
    scene bg black with Dissolve (3.0, alpha=True)
    $renpy.pause(delay=None)
    scene bg end03 with slowdissolve
    with Pause(2)
    scene bg black with fade
    $renpy.pause(delay=None)
    call endcredits from _call_endcredits_4
    
return
