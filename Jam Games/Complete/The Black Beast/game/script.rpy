define mc = Character("[mcname]")
define mcu = Character("???")
define mg = Character("Mogu")
define bk = Character(None, kind=nvl)
define shn = Character(None, kind=nvl, what_font="fonts/shadow.ttf", what_size=23)
define da = Character(None, what_font="fonts/shadow.ttf", what_size=23)
define sh = Character(None, what_font="fonts/shadow.ttf", what_size=23)

define ed = Character("Edelia")
define mr = Character("Mary")
define nu = Character("Nue")
define de = Character("Deis")
define oro = Character("Ororo")
define mg = Character("Mogu")
define mor = Character("Morcobashi")
define pon = Character("Ponchu")
define so = Character("Sol")

#Masks
define gk = Character("Gokiboki (Nue)")
define ido = Character("Ido (Nue)")
define po =  Character("Popo (Nue)")
define jac = Character("Jacques (Nue)")
define lop = Character("Lopi (Nue)")
define kar = Character("Karaga (Nue)")


label start:
    call lbl_memoryTest
    
    call intro from _call_intro
    
# Chapter 1:

label chap1:
    show screen FrameScreen with dissolve
    #show blackframe movie onlayer frameLayer
    
    show bg hallway01 with dissolve
    play sound dooropen
    $ renpy.music.play("audio/music/hallway.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)   
    "I am in the hallway."

    "*sob sob*"
    "Someone is crying over to the right."
    menu:
        "Follow the crying.":
            show mogu at center
            mg "But Edelia, I am so hungry!"
            mg "All the food in the house is gone!"
            hide mogu
            
            show ede at center
            ed "..."
            hide ede
            
            show mogu at center
            mg "Just one bite, please?"
            hide mogu
            
            show ede blink at center
            ed "..."
            hide ede base           
            
            scene bg hallway01
            show mc at mcleft
            show ede at center
            show mogu at chfarright
            mc "Hello."
            mg "Oh! A new person! He looks tasty!"
            show ede blink at center
            ed "..."
            show ede at center
            mc "My name is [mcname]."
            mg "Hello [mcname]! Do you have any food?"
            mc "Err... No."
            mg "Oh yeah, my name is Mogu, and this is Edelia."
            show mogu blink at chfarright
            mg "She won't give me her fingernails to eat."
            show ede blink at center
            show mc huh at mcleft
            show mogu at chfarright
            mc "..."
            show ede at center
            show mc at mcleft
            mc "I don't think you should eat fingernails, Mogu."  
            show mogu huh at chfarright
            mg "Huh?! Why not?!"
            show mogu at chfarright
            mg "Big Bro said it's full keratims! He said it will make your eyelashes grow long."
            mc "Keratims?"
            mg "Hair vitamin."
            show ede blink at center
            "Edelia coughed."
            hide ede blink
            "She took out a wax board from behind her and wrote something."
            show ede at center   
            ed "..."
            "The board read 'keratin'."
            mg "I'm pretty sure it's keratim."
            mg "Big bro is never wrong."
            show ede blink
            "Edelia sighed."
            show ede
            mg "Anyway, I'm so hungry I can't move."
            show mogu blink
            mg "Please, [mcname], will you find me some food?"
            show mogu 
            mg "I'll eat anything!"
            mg "Even your shoe!"
            mc "..."
            mg "I'm kidding."
            mg "Shoes don't have nutritional value."          
            
            menu:
                "Help Mogu find food.":
                    mc "..."
                    mc "Okay."
                    mc "Any kind of food right?"
                    show mogu happy
                    show ede smile
                    mg "Yes! And Thank you!"
                    $ helpMogufindfood = True
                    show screen walkaround
                    call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1
                "I have to go.":
                    mc "I'm sorry, I can't."
                    mc "I'm on a mission."
                    mg "Ohh..."
                    mg "...Okay."
                    ed "..."
                    mg "Well, I'm gonna go somewhere to look for food."
                    mg "Bye."
                    hide mogu
                    $ librarypathclear = True
                    $ ignoreMogu = True
                    show screen walkaround
                    call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_1
        "Ignore.":
            $ ignoreMogu = True
            $ librarypathclear = True
            show screen walkaround
            call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_2
    show screen walkaround
    call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_3
    
label chap2:
    show screen FrameScreen with dissolve
    play sound dooropen
    show bg hallway01 with dissolve:
        xpos 0 + (2800/2) - currentLocation
    show pon at chright 
    if mcramhorns:
        show mc horns at mcleft
    else:
        show mc at mcleft
    "I go out of the hallway and I see a creature."  

    mc "..."
    "..."
    show pon at outofscreen with MoveTransition(0.5)
    hide pon 
    "It runs away before I can catch it."
    call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_4     


      
label chap3:
    call demo from _call_demo

    return
