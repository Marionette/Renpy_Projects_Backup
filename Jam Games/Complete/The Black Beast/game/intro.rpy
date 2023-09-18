label intro:
    scene bg black
    nvl clear
    bk "I had a dream."
    nvl clear
    bk "In my dream I am always running."
    nvl clear
    bk "Sometimes I am running through forests, sometimes through a maze of 
    buildings so tall the light from the skies has dimmed."
    nvl clear
    bk "Most of the time though, I am in a corridor with no end, decked with 
    doors that lead both nowhere and somewhere."
    nvl clear
    bk "I open one of the many doors... and another..."
    nvl clear
    bk "And another..."
    nvl clear
    bk "then another until I am dizzy, and I do not know where a room ended or where it began."
    nvl clear
    $renpy.pause(delay=None)
    "Sometimes there is a monster coming after me."
    show bg beast with dissolve
    "A black beast."
    "I don't have to look back over my shoulder to see him."
    "He is there."
    "But I am getting tired of running..."
    
    show bg door with dissolve
    
    "so when I saw a door up ahead, 
    I jumped into the inky darkness and slammed the door shut."
    play sound doorslam
    stop music
    show bg black
    
    "A beast is behind me."    
    "I cowered in the shadows and hid."
    "..."
    $renpy.pause(delay=None)       
    play sound "audio/sfx/shadowgiggle03.ogg"    
    da "*giggle*" 
    "...!"
    play sound "audio/sfx/shadowgiggle02.ogg"  
    play music "audio/sfx/shadowbg.ogg" fadein 3.0
    "Wh-Who's there...?"
    play sound "audio/sfx/shadowgiggle.ogg"   
    da "Who's there?"
    "The voice that came back was an echo of my own."
    
    #$ random_name = renpy.random.choice(['Talion',])
    $ mcname = renpy.input("My name is", default='Talion')
    $ mcname = mcname.strip() 

    da "Who's there...?"
    scene bg boy with Dissolve(4.0)
    mc "[mcname]"      
    da "[mcname] who?"
    mc "..."
    da "[mcname] the brave or [mcname] the weak?"
    mc "..."
    da "How long are you going to stay in here?"
    play sound "audio/sfx/shadowhum.ogg"
    nvl clear
    shn "little boy hiding, what do you fear?"
    shn "the black beast is prowling, its shadow is near"
    shn "poor little fellow, eyes are shut tight."
    shn "is he a coward or will he fight?"
    nvl clear

    mc "..."
    
    da "That beast. He can be defeated."
    da "But..."
    da "Are you brave enough to face him?"
    da "I will help you if you stop running."
    da "Turn around and strike him down where he stands."
    da "Face him, [mcname]. Face him and win."
    $renpy.pause(delay=None)
    da "Or you can just hide here like a little baby until he comes to gobble you up."
    mc "..."
    mc "I can do it!"
    mc "I can defeat the beast--!"
    da "Really?"
    da "Can you {i}really{/i} do it?"
    mc "..."
    mc "Y-Yes."
    da "That's the spirit~{font=fonts/cour.ttf}♪{/font}"
    $renpy.pause(delay=None)    
    da "Well, it's decided."
    play music "audio/sfx/shadowbg.ogg" fadein 3.0
    da "Let's help each other out, [mcname]!"
    da "I'll help you defeat the beast haunting you."
    da "And you'll help me get back the thing I lost."
    da "That... beast took something from me."
    da "He imprisoned me and left this world to crumble."
    da "If you free me [mcname], you will free everyone under his spell as well."
    
    da "But let me warn you, it's not going to be easy."
    da "You must follow my instructions to succeed."
    mc "..."
    da "Or else..."
    play sound "audio/sfx/shadowgiggle02.ogg" 
    da "Let's just say there will be consequences."
    mc "..."
    mc "W-Who are you...?"
    mc "Why did the beast lock you up?"
    sh "Me?"
    sh "I am what everybody fears--"
    sh "--even the beast."
    play sound "audio/sfx/shadowgiggle.ogg" 
    sh "{cps=10}I am the Dark.{/cps}"
    sh "And it's time for me to take back what is mine."
    $renpy.pause(delay=None)
    sh "So will you help me? I will reward you handsomely."
    mc "..."
    mc "Okay..."
    $renpy.pause(delay=None)    
    sh "I need three items to gain back my power."
    sh "The first one is a weapon."
    sh "An artifact both dead and alive, both ephemeral and eternal."
    sh "The horn of a dead god."
    sh "Find it and come back to me."
    sh "I will be waiting here."
    $renpy.pause(delay=None)    
    sh "But before you go, I have a gift for you."   
    play sound itemtwinkle 
    "I put a hand in my pocket and felt a cool round item in my palm."
    "A soft incessant ticking filled my ears."
    mc "A pocketwatch?"
    $ResetTimer()
    show screen pocketwatch
    $ minutes = 375
    sh "I am lending you some of my time."
    sh "It is precious and should not be wasted."
    sh "In this forgotten place, Time is the only thing that can ward off the beast. It is his weakness."
    sh "This watch will protect you from him for a while."
    sh "Use this Time wisely."
    $renpy.pause(delay=None)
    sh "Now, run along."
    sh "Let us defeat the beast together!"
    scene bg black with dissolve 
    call chap1 from _call_chap1
return
    
