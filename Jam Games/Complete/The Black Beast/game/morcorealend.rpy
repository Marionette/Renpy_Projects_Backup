label morcorealend:
    mor "I cannot stop you now, can I?"
    mor "You have proven that you do not care about this world, but your own goal."
    mor "Fine, then. Take your prize."
    mc "..."
    play sound slash
    hide morc
    $renpy.pause(delay=None)
    play sound itemtwinkle
    "Got Gryphon wings"
    show mc wings at mctaileft with dissolve
    scene bg black with dissolve
    hide screen FrameScreen
    $renpy.pause(delay=None)
    call demo from _call_demo_2
return
    
    
    
