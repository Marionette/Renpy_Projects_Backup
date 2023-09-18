    
label morco_demo:
    #hide screen FrameScreen
    scene bg black with dissolve
    hide screen walkaround
    hide screen pocketwatch
    show screen FrameScreen 
    stop music fadeout 2.0
    $renpy.pause(delay=1)
    show clock animated with slowdissolve
    $renpy.pause(delay=None)
    scene bg black with dissolve
    scene bg clockroom_moved with dissolve
    show morc base at chright
    if mcramhorns:
        show mc horns at mcleft
    if mctail:
        show mc tail at mctaileft
    if mcwings:
        show mc wings at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc base at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc base at mcleft
    mor "The clock moved."
    mor "Your timer run out a long while ago, did you notice?"
    mor "You gave away your time instead of keeping it to yoursef."
    mor "Thank you."
    mor "In this crumbling world, Time is one of the most precious things you can offer to people."
    mor "By giving it to us you are slowly lifting the spell."
    mor "The beast will arrive soon."
    mor "But we will help you."
    $renpy.pause(delay=None)
    mor "Can you grant me a request?"
    mor "Will you come back here when you have more time to give?"
    mor "I want to know what happened to this place."
    mor "Why it fell to ruin..."
    mor "And how to save it..."
    scene bg black with dissolve
    hide screen FrameScreen
    mor "But this time, this is where we say goodbye."
    mor "Come back soon, okay?"
    $renpy.pause(delay=None)
    call demo from _call_demo_1
    $ renpy.full_restart()
return

label morco_demo_bad:
    hide screen pocketwatch
    hide screen walkaround
    stop music fadeout 3.0
    show morc base at chright
    show bg clockroom
    if mcramhorns:
        show mc horns at mcleft
    elif mctail:
        show mc tail at mctaileft
    elif mchornstail:
        show mc hornstail at mctaileft
    else:
        show mc base at mcleft
    mor "..."    
    mor "So you have come."
    if ramhorn:
        mor "You are brandishing a very old and powerful weapon."
        mor "I regret that I even helped you at all."
    if darkunicorn:
        mor "You are brandishing a cursed object."
    if Nuetailcut:
        mor "You have even taken Nue's tail."
    $renpy.pause(delay=None)
    mor "Tell me, what really is your purpose here?"
    menu:
        "To defeat the Beast.":
            mc "I want to defeat the Beast."
            mor "What beast?"
            mor "I don't see him."
            mor "The only beast I see right now is you."
            mc "You're wrong. I'm trying to help."
            mc "He is imprisoning this world."
            mor "Help?"
            mor "By hurting my friends?"
            mc "But I must--"
            $ purpose = True
        "I don't know.":
            mc "I've forgotten."
            mc "I simply want to fulfill my goal."
            
    mor "So you will do whatever it takes to fulfill your goal, is that it?"
    menu:
        "Yes.":
            mc "Of course."
            $ resolve = True
        "No.":
            mc "..."
    mc "..."
    if doubtedDark:
        pass
    else:
        mor "Tell me, have you ever once doubted the path you are in?"
        mc "..."
    mor "You must know that there is another way. There is always another way."
    mor "It may not be the most clear path, but it is there, beaneath the barbs and thickets untread."
    mc "I don't understand what you are talking about."
    mc "I am only trying to rid this world of a menace."
    mc "It is the beast that we must be afraid of."
    $renpy.pause(delay=None)
    mor "This beast you speak of..."
    mor "Are you really afraid of him or is that an excuse to forward your goal?"
    mc "..."
    mor "No."
    mor "You are not afraid of him."
    mor "What you are afraid of is losing time, so you hoard it."
    mor "You are afraid of failing, so you take."
    mor "Afraid of losing, so you destroy."
    mor "If you are so afraid of such things, then your place is not here, not with us."
    mor "Your place is out there."
    mor "Stop devouring our world."
    mor "We should not be made to pay for your cowardice."
    mc "..."
    mc "Enough of this."
    mc "Give me your wings."
    mor "..."
    $renpy.pause(delay=None)
    if purpose and resolve and beatTimer:
        call morcorealend from _call_morcorealend
    else:  
        mor "No."
        mor "This time, you will not take them. Not in this lifetime."
        scene bg black with dissolve
        hide screen FrameScreen
        mor "Goodbye."
        $ triggerblackmm = True
        $renpy.quit(relaunch=False, status=0)
    $renpy.quit(relaunch=False, status=0)    
return



label demo:
    play music nvlmusic
    scene bg black
    nvl clear
    bk "This is the end of the demo."
    nvl clear
    bk "Credits:"
    bk "\nart and writing - ameliori \n programming - marionette/ameliori \n writing team - colacat/ameliori"
    nvl clear
    bk "Special Thanks:"
    bk "\n jia bumatay \n jana champion\nsatoshi kamanaka\n jaia vucetich"
    nvl clear
    bk "This work is dedicated to you, darling. \nThanks for putting up with me during devhell! \n- ame"
    nvl clear
    bk "If you want to know more about this project, drop by our 
    {a=https://ferventdev.wordpress.com/blog/}devblog{/a} or our {a=https://fervent.itch.io/}itchio{/a} page."
    nvl clear
    if goodpathdone:
        bk "Thank you for spending your Time with us."
    if badpathdone:
        bk "May you fulfill your purpose."
    scene bg black
    $ renpy.full_restart()
