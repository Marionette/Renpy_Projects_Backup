label intro:
    scene bg black
    "I had a dream."
    "In my dream I was always running."
    "Sometimes I am running through forests, sometimes through a maze of 
    buildings so tall the light from the skies have dimmed."
    "Most of the time though, I am in a corridor with no end, decked with 
    doors that lead both nowhere and somewhere."
    "I open one of the many doors, and another, and another, until I am dizzy, and I do not know 
    where a room had ended or where it began."
    "I am lost."
    "Sometimes there is a monster after me."
    "A black beast."
    "I don't have to look back at my shoulder to see him."
    "He is there."
    "He is insisted."
    "But I am getting tired of running, so when I saw a door up ahead, 
    I jump into the inky darkness and slammed the door shut."
    
    "A beast is after me."
    "It is nowhere to be seen."
    "Tears fell from my eyes."
    
    "*sniff*"
    "*sniff*"
    play sound "audio/sfx/shadowgiggle03.ogg"    
    "{w}"
    "...!"
    play sound "audio/sfx/shadowgiggle02.ogg"  
    play music "audio/sfx/shadowbg.ogg" fadein 3.0

    "Wh-Who's there...?"

    da "*giggle*"
    play sound "audio/sfx/shadowgiggle.ogg"   
    da "Poor boy..."
    da "You're all alone now"
    "Go away! *sniff*"
    play sound "audio/sfx/shadowhum.ogg"
    
    shn "once upon a dreary time"
    shn "a blackened beast doth lived"
    shn "he prowls the dreams of little kids
    and "
    shn "He took the moon and ate the sun"
    shn "and little children, did."
    nvl clear
    
    "Who's there?"
    da "Who's there?"
    "The voice that came back was an echo of my own."
    
    $ random_name = renpy.random.choice(['Dante', 'Elem', 'Aris', 'Dar', 'Moris', 'Philip', 'Tora', 'Ashi', 'Gis', 'Popo', 'Lorei', 'Pose'])
    $ mcname = renpy.input("My name is", default=random_name)
    $ mcname = mcname.strip() 
    mc "[mcname]"    
    da "Well, [mcname], I don't believe you..."
    play sound "audio/sfx/shadowgiggle03.ogg"
    da "I think you're afraid!"
    da "Crying yourself to sleep until the manticore comes and gobbles you up."
    da "You can't even get yourself out of your cage! You're not worth talking to!"
    da "You are nothing but the Manticore's next meal~!"
    "The boy felt tears in his eyes."
    da "T-That's not true!"
    da "I can do it!"
    da "I can defeat the Manticore--"
    da "Ohh~kay{font=fonts/cour.ttf}♪{/font}"
    da "It's decided."
    play music "audio/sfx/shadowbg.ogg" fadein 3.0
    da "I will help you out, [mcname]! I see potential~!"
    mc "O-Oh!"
    da "But let me warn you, I don't take kindly to naughty, disobedient children."
    da "You will follow what I say if you want to defeat the Manticore."
    da "Understood?"
    da "..."    
    sh "What's the matter? You still want your brother back, don't you?"
    mc "I... I do..."
    da "Don't want to be eaten by the Manticore, do you?"
    mc "...No..."
    play sound "audio/sfx/shadowgiggle02.ogg" 
    da "Then do as I say, little boy, or you will regret it."
    mc "..."
    sh "Just kidding!"
    sh "...But not really."
    mc "..."
    mc "W-Who are you...?"
    sh "Me?"
    sh "I am what everybody fears--"
    sh "--even the Manticore."
    play sound "audio/sfx/shadowgiggle.ogg" 
    sh "{cps=10}I am the Dark.{/cps}"
    sh "And it's time for me to take back what is mine."
    sh "{w}Now, run along."
    sh "Find me an item both dead and alive, both unending and ended."
    sh "A weapon and a treasure, the horn of a dead god."
    sh "Then, we will defeat the Manticore, together."
    sh "I have a gift for you."   
    "I put my hand in my pocket and felt a cool round item in my palm."
    "A soft incessant ticking filled my ears."
    "A pocketwatch?"
    $ResetTimer()
    show screen pocketwatch
    $ minutes = 540
    sh "This watch will guide you to your goal."
    sh "Time is the only treasure in this forgotten place."
    sh "Make haste and fulfill your quest, and you will be victorious."
    call chap1
return
    
