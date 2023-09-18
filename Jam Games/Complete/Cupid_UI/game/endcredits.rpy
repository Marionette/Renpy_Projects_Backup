#BUILD 12
label endcredits:
    scene black
    with Pause(1)

    show text "Art, Writing & Direction{p}{p}{font=gui/timesi.ttf}{size=+4}ameliori{/size}{/font}{p}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)
    
    show text "Co-Writers{p}{p}{font=gui/timesi.ttf}{size=+4}tinytim12{p}The Library Cat{/size}{/font}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)

    show text "3D Modeling{p}{p}{font=gui/timesi.ttf}{size=+4}artsvarn{/size}{/font}{p}" with dissolve
    with Pause(3)
    
    hide text with dissolve
    with Pause(1)
    
    show text "Proofs{p}{p}{size=+4}{font=gui/timesi.ttf}The Library Cat{p}ColaCat{p}Saltome{/size}{/font}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)
    
        
    show text "UI Design{p}{p}{font=gui/timesi.ttf}{size=+4}ameliori{p}Marionette{/size}{/font}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)
    
           
    show text "Music{p}{p}{font=gui/timesi.ttf}{size=+4}autumnelm{p}Krichotomy{p}Yasupochi{p}Circus Marcus{p}Kevin Mcleod{p}Freesound.org{/size}{/font}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)

    show text "Art Consultants{p}{p}{font=gui/timesi.ttf}{size=+2}Erik Markus{p}Stijn Zijlstra{p}Skyris Design{p}Leviathan{/size}{/font}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)

    show text "Special thanks to:{p}{p}{font=gui/timesi.ttf}{size=+2}SundownKid{p}janajee{p}{p}Lemmasoft Forumers{p}Sycra Art Forum Hangouts{/size}{/font}" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)

    show bg renpy with Dissolve(2.0, alpha=True)
    with Pause(3)
    
    show bg black
    with Pause(1)
    
    show text "{size=+7}CUPID{/size}{p}a Renpy Game {p}{p}{p}{size=-7}All Rights Reserved 2021. {/size}" with dissolve
    with Pause(3)
    hide text with dissolve
    with Pause(1)
                   
    show text "Thanks for playing!" with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)
    $renpy.pause(delay=None)
    call summary0 from _call_summary0
    $ renpy.full_restart()
    return
