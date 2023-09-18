label jokejournal:
    show screen quick_menu
    #$persistent.Chapter6Unlocked = True
    #scene bg chap06 with slowdissolve
    #with Pause(2)
    scene bg black with fade
    stop music fadeout 2.0
    scene bg librarydark
    nvl clear

    $ achievement.grant("This should have been a comedy")
    $achievement.Sync()
    "In the warm, dim light of the library, Rosa opened Guilleme's journal cover."
    play sound "sfx/page.ogg"
    show jkdiary05
    play music "sfx/comedy.ogg" 
    $renpy.pause(delay=None)
    hide jkdiary05
    r "..."


    r "....."
    r "Uh..."
    m "Well, he is kind of a manslut, isn't he?"
    m "Why is he offended?"
    r "..."
    
    play sound "sfx/page.ogg"
    show jkdiary08
    $renpy.pause(delay=None)
    hide jkdiary08
    r "..."
    m "Tap dancing..."
    
    
    play sound "sfx/page.ogg"
    show jkdiary04
    $renpy.pause(delay=None)
    hide jkdiary04
    r "..."
    "Rosa touched her hair on impulse."
    m "I think he's right."
    m "Your hair and skin are so dry!"
    m "You're too stressed and you always sleep so late."
    m "You should get more fluids in you."
    r "Moooom..."
    m "Oh, sorry dear."
    
    
    play sound "sfx/page.ogg"
    show jkdiary03
    $renpy.pause(delay=None)
    hide jkdiary03
    r "..."
    r "God damn it, Gilly."
    r "I am not weird!"
    r "I do not hide behind curtains!"
    r "Argh! Why does he have to make it sound like I'm stalking him!"
    r "That pompous asswipe!"
    m "Well... you do have his picture on your--"
    r "STOP!"
    r "MOM."
    r "Stop."
    m "..."
    m "Just sayin'."
    
    play sound "sfx/page.ogg"
    show jkdiary02
    $renpy.pause(delay=None)
    hide jkdiary02
    r "..."
    m "Princess Sparkles..."
    m "..."
    r "T-The classy penis..."
    r "..."
    m "There is something very wrong with that boy."
    
    play sound "sfx/page.ogg"
    show jkdiary01
    $renpy.pause(delay=None)
    hide jkdiary01
    r "..."
    
    show jkdiary07
    $renpy.pause(delay=None)
    hide jkdiary07
    r "..."    
    r "That's it!"
    r "I am {i}killing{/i} that guy!"
    r "It was {i}one{/i} time his briefs got mixed up with my laundry."
    r "ONE TIME."
    r "I am going to kick that fu--"
    m "Calm down, honey."
    play sound "sfx/page.ogg"

    
    play sound "sfx/page.ogg"
    show jkdiary06
    $renpy.pause(delay=None)
    hide jkdiary06

    play sound "sfx/page.ogg"
    show jkdiary09
    $renpy.pause(delay=None)
    hide jkdiary09
    r "He stole my diary?!"
    r "That little manwhore! I am going to fry his ass!"
    m "Uh... did you forget that you also stole his?"
    r "And a good thing too! He's asleep!"
    "An idea was forming in her mind."    
    "Rosa snapped the book shut and dragged her feet along the floor."

    r "That doofus is sleeping right now."
    r "I'm sure Cath is up for a prank!"
    scene bg black    
    play sound "sfx/camera.ogg"
    with flash
    show drunkpic
    $renpy.pause(delay=None)
    hide drunkpic  
    if persistent.jkjournalWasReadBefore   is None:
        $persistent.jkjournalWasReadBefore  = True
        $persistent.currentLinesRead +=1
    $renpy.call_screen("extra_bonus")

    
return
