label chap8:
    stop music fadeout 2.0
    $save_name = "chap8: transience"
    $persistent.Chapter8Unlocked = True
    
    scene bg chap08 with slowdissolve
    with Pause(2)
    scene bg black with fade
    nvl clear
    
    o "{i}What in me is dark.{/i}"
    nvl clear
    play sound "sfx/heartbeat.ogg"
    show bg polaroid1 with fade
    show bg black  
    nvl clear
    o "{i}No light, but rather darkness visible.{/i}"
    nvl clear
    play sound "sfx/heartbeat.ogg"
    show bg polaroid1 with fade
    show bg black  

    "But that is not me."
    show bg polaroid2 with zoomin
    show bg polaroid3 with zoomin
    show bg polaroid4 with zoomin
    show bg black with zoomin
    play sound "sfx/heartbeat.ogg"
    "What is in me, is not me."
    "I fought with it, lived with it, survived."
    play sound "sfx/heartbeat.ogg"
    "Yet, we become what we subdue."
    "If this is true, then I was never myself."
    show bg polaroid5 with zoomin
    show bg polaroid10 with zoomin
    show bg polaroid7 with zoomin
    show bg black with zoomin
    play sound "sfx/heartbeat.ogg"
    "I am not a monster."
    scene bg cath08 with Dissolve (3.0, alpha=True)
    m "Then what are you?"
    "..."
    "...tired."
    
    c "Did you even really love me?"
    c "Or were you just hungry?"
    "It is hard to divide that line sometimes."
    "Hunger hovers over every action I take."
    "...Maybe I was bored."
    c "That's sweet of you, Gilly. Truly, marvelously classy."
    play music "sfx/intro.ogg"
    "What are you doing in my dream, Catherine?"

    if persistent.adult:
        c "I came to punch you in the face, you fucking bastard."
    else:
        c "I came to punch you in the face, you bastard."
    c "And then, perhaps..."
    c "...Say goodbye."
    
    "Pain wells up in my throat and I answer it with anger."
    "Goodbyes are pointless."
    "I have no need for them."
    "You're just another voice in my conscience that will fade away in time."
    
    c "No, I am not."
    c "You're still a bastard, mind you."
    c "But I love you still."
    
    "And I loved you."
    "But does that matter now?"
    "I will love another one quite like you in the future."
    c "You know, I can always tell when you're lying to me."
    c "Your mouth does that little twitch, and your nose flares up like you smell something bad."
    
    "That man you knew is gone."   
    "He was nothing but an illusion you yourself designed, my dear."
    "I only adapt."
    "..."

    c "Then why do you still do it?"
    c "How can I still tell you're lying?"
    
    "I'm not."
    c "Liar."
    
    scene bg cathsky with None
    "{i}You were holding a telescope.{/i}"
    c "{i}I don't see it!{/i}"
    "{i}\"Sagittarius is over there!\" I laughed, pointing your hand to the night sky.{/i}"
    "{i}Beneath this blanket of stars, the brightest one was sitting right beside me.{/i}"
    
    "{i}That night...{/i}"
    "{i}Would you believe me if say I didn't mean to kiss you?{/i}"
    "{i}I had hoped you wouldn't see my hand shake.{/i}"
    scene bg black with None
    m "\"In your eyes, I feel like I am somebody worth loving.\""
    "{i}I am a lie.{/i}"
    "{i}But that was the truth.{/i}"

    scene bg cath08 with None
    c "The arrow you struck my heart with worked both ways, darling."
    c "I have loved you since I was a child."
    c "And you had to keep this mask on for years, longer than you usually had to."
    c "But, you see..."
    c "When you become something for a long time, it imprints on you like a seed."
    c "Maybe you liked keeping this face, hm?"
    
    scene bg cath11 with Dissolve(0.2, alpha=True)
    "{i}Your cat died today and we buried it in my garden.{/i}"
    "{i}You were crying so hard, nobody could comfort you.{/i}"
    "{i}Candies or sweets and bribes didn't work.{/i}"
    "{i}In my desperation, I said \"Everything dies\", as if that was a truth worthy to be told to a child.{/i}"
    "{i}\"Did you know that the baker's dog also died?\"{/i}"
    "{i}\"Things die, so please don't be upset.\"{/i}"
    "{i}Your eyes stared up at me.{/i}"
    show bg cath01 with Dissolve (0.5, alpha=True)
    "{i}To my surprise, you began to laugh.{/i}"

    show bg cath02 with Dissolve (0.5, alpha=True)
    cm "{i}Gilly, you are such an idiot!{/i}"
    cm "{i}\"The baker's dog also died.\" Are you really trying to cheer me up?{/i}"
    show bg white with Dissolve (2.0, alpha=False)    
    "{i}I shifted uncomfortably in my boots, but your laughter had you in stitches.{/i}"
    show bg cath12 with Dissolve (3.0, alpha=False)
    cm "You took away my love."
    cm "But you can't take away my memories."
    
    "Memories falter and fade."
    "When you have lived as long as I have, memories are cheap."
    "Love is cheap, Catherine."
    
    "So, would you please leave me now?"
    "I don't want to remember you anymore."
    "I don't want this."
    "I--"
    
    cm "Once upon a time, there was a man who lost his heart."
    cm "So he eats others'."
    "I never lost it. I have always been cursed without it."
    cm "Then take mine."
    "Yours?"
    cm "Take my love with you until the end of time."
    cm "You will never go hungry again."
    "That's not true."
    "You hated me at the very end, like everyone else."
    cm "Well, you ruined my life, so of course I hated you."
    cm "You lied to me."
    cm "You used me."
    cm "But..."
    cm "Love and hate can be so similar."
    cm "It's as simple as flipping a coin."
    
    cm "But don't give me apathy, Guilleme."
    cm "I want my memory to burn as bright as a star in your mind."
    cm "And this memory I want you to remember me by, is not my body hanging lifelessly by a rope."
    show bg cath03 with Dissolve (2.0, alpha=True)
    cm "Remember me as the child who loved you."
    cm "My dear, Guilleme."
    cm "I love you."
    cm "I forgive you."
    
    "An unfamiliar bitterness washes over my tongue."
    "It threatens to sting my eyes with tears, clenching my throat with pain."
    "Curiously, it is a sensation almost foreign in its rarity."
    "{i}Love...{/i}"
    "Is it possible?"
    "Can I love a memory?"
    "Can I survive with only your love to give me sustenance?"
    show bg handreach  
    "I take a step towards you."
    play sound "sfx/glassbreak.ogg"
    stop music
    show bg black with flash
    show bg red with flashblood
    show bg cath05 with pixellate
    show bg cath08 with Dissolve(0.2, alpha=True)

    show bg red with pixellate
    "Something stirred in my dreamscape, and suddenly you are not there anymore."
    show bg cath03 with None
    show bg cath09 with pixellate
    show bg cath10 with Dissolve(0.1, alpha=True)
    show bg cath09 with Dissolve(0.6, alpha=True)
    show bg cath04 with fade
    play music "sfx/doom.ogg" fadein 4.0
    "I see you in the distance."
    "A semblance of your visage upon a grassy hill."
    "The sky is dark."

    "The moon hangs ominously upon your head."
    scene bg red with None
    m "Catherine!"
    m "Run!"
    scene bg black with None
    "But you cannot hear me."
    "My legs are draped in clear jelly."
    "In dreams, everything is slow."
    "I cannot get to you in time."
    play sound "sfx/monster.ogg"
    scene bg cathmonster with Dissolve (3.0, alpha=True)

    "Your face begins to change."
    "You are Catherine."
    "You are Émilie."
    "You are Marcus."
    "You are Psyche."
    "Your head begins to snap and distort."
    "The skin bubbles and the flesh tears to reveal the pulsing hide of the monster inside."
    "Your glistening heart pumps in your chest."
    "Your feathers pruned and majestic from recent feeding."
    "Yet I am not afraid of this thing and its many mouths."
    "This was nothing but a reflection, a mirror held up to what I really am."
    #"You are merely holding a mirror up to me."
    play sound "sfx/gripsquish.ogg"
    "A slithering hand wraps around my neck and lifts me from the ground."
    "The pressure tightens as I struggle."
    "One of your tongues licks at the side of my belly, as if sampling the food before the course."
    
    gt "Running away again?"
    gt "Content to starve yourself and feed off a memory?"
    gt "Pathetic."
    
    "You still look like Catherine."
    "Maybe that is the most painful part."
    "I can't bear to look at you."
    
    gt "Why starve yourself when there is plenty to eat?"
    gt "Why beg for scraps when you can gorge?"
    
    gt "Did you really think your life could change?"
    
    "..."
    
    gt "You know better."
    gt "Son of beauty."
    gt "Brother of night."
    gt "{i}Love.{/i}"
    gt "That is you."
    gt "You are a sickness."
    gt "Wherever you will go, this shadow will haunt you."
    gt "Collect your trinkets, by all means. Relive your precious memory."
    gt "But know that you will be nothing more than a hypocrite."
    gt "A clean man walking in a mountain of filth."
    gt "Open your eyes."
    gt "{size=50}{i}Open them{/i}{/size}"
    gt "Behold my true, glorious form."
    
    "..."
    
    gt "Humans are insatiable."
    "Men and women, they are all rabid for love."
    gt "How many times have you been their toy?"
    "Humans are cruel to things they desire."
    gt "I must be powerful. I must be on top."
    "I control them instead of them controlling me."
    gt "I will not be a piece of meat."
    bg "Never again."

    "Your face softens, and the grip on my neck drags me close to your lips."
    scene bg cathmonsterkiss
    "You claim my mouth with yours, and it tastes just like honey."
    "Spit ropes between our lips."    
    scene bg black
    gt "Love is my sustenance."
    bg "Love is my sustenance."
    gt "I will take what I can..."
    bg "...because they so willingly give."
    show bg angrycupid1 with Dissolve (0.5, alpha=True)
    gt "I must get rid of this dastardly spell I am under."
    #gt "It is playing with my mind."
    
    gt "Catherine is gone, like her memory."


    gt "In the end, this was all an old, vile magic. A cheap parlour trick."
    show bg angrycupid2 with Dissolve (0.5, alpha=True)
    show bg angrycupid3 with Dissolve (1.0, alpha=True)    
    gt "Whoever touched me will pay."
    if persistent.chap8WasReadBefore   is None:
        $persistent.chap8WasReadBefore  = True
        $persistent.currentLinesRead +=1
    scene bg black with None
    $renpy.pause(delay=None)        
    if openlocket is False:
        call end2 from _call_end2
    # to get the ending 1, the following things should be fulfilled:
    # open the locket
    # do not say cath is selfish
    # do not hint that rosa loves guilleme romantically
    # be nice to rosa
    # family is more important
    # do not take the dagger
    # mother is bent on revenge, not on justice
    # believe that guilleme can "change"
    # tell rosa to take care of herself
 

    if knife:
        call end2 from _call_end2_1
    if dagger:
        call end2 from _call_end2_2
    if justice:
        call end2 from _call_end2_3
    if nochange:
        call end2 from _call_end2_4
    if cathselfish:
        call end2 from _call_end2_5
    if badmom:
        call end2 from _call_end2_6
    if closelocket:
        call end2 from _call_end2_7
    if rosajealous:
        call end2 from _call_end2_8
    if friends:
        call end2 from _call_end2_9
    if rglove >= 1:
        call end2 from _call_end2_10
    if rgloves:
        call end2 from _call_end2_11
    else:
        if persistent.Ending2Unlocked:
            call end1 from _call_end1
        else:
            call end2 from _call_end2_12
return    
