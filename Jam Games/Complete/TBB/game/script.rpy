define mc = Character("[mcname]", what_size=27)
define mcu = Character("???")
define mg = Character("Mogu")
define bk = Character(None, kind=nvl)
define shn = Character(None, kind=nvl, what_font="fonts/shadow.ttf", what_size=25)
define da = Character(None, what_font="fonts/shadow.ttf", what_size=25)
define sh = Character(None, what_font="fonts/shadow.ttf", what_size=25)

define ed = Character("Edelia")
define mr = Character("Mary")
define nu = Character("Nue")
define de = Character("Deis")
define oro = Character("Ororo")
define mg = Character("Mogu")
define mor = Character("Morcobashi")
define po = Character("Ponchu")
define so = Character("Sol")

label start:
    call intro
    
# Chapter 1:

label chap1:
    show screen FrameScreen
    $ renpy.music.play("audio/music/hallway.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    #show blackframe movie onlayer frameLayer
    
    show bg hallway01


    "The door opens and the neverending hallway stretches beyond me."
    "I have a quest and I must fulfill it."
    "To my left though, I hear someone crying."
    menu:
        "Follow the crying.":
            "If you follow the crying, you meet Mogu."
            menu:
                "Help.":
                    "Help Mogu out."
                    $ helpMogufindfood = True
                    show screen walkaround
                    call lbl_mapStart_hallway1
                "Ignore.":
                    "Got no time for this."
                    $ librarypath = clear
                    $ ignoreMogu = True
                    show screen walkaround
                    call lbl_mapStart_hallway1
        "Ignore.":
            $ ignoreMogu = True
            $ librarypathclear = True
            show screen walkaround
            call lbl_mapStart_hallway1
    show screen walkaround
    call lbl_mapStart_hallway1
    
label chap2:
    show screen FrameScreen
    show bg hallway01
    if mcramhorns:
        show mc horns at mcleft
    else:
        show mc base at mcleft
    show pon base at chright
    "So you have another quest."
    "You see a creature whizzing about."
    hide pon base on chright with dissolve
    "it disappears before you can catch it."
    call lbl_mapStart_hallway1     


      
label chap3:
 
    # if good route:
    # call ororo room peace

    "You go to the star room, but it's cloudy, they're all afraid of the Manticore."
    "You find a new room, and there are some stone statues. One of them is broken."
    "They have name clues, puzzle game."
    "You talk to everyone and they give you clues, until you get his name, which is Talion."
    "Deis says that Manticore is like her, who is afraid of going out, and she doesn't want to 
    hide anymore."
    "She goes out gives you the final clue."
    "Finally, a door unlocks, and you talk to the Manticore."
    "You talk to the Manticore and he's actually a happy weirdo."
    "He tells you joke number 3."
    "Talk to him a couple of times, until he realizes you're the one with the clock."
    "You talk to him a little bit and he's angry at you for making the big clock tick, he doesn't know 
    why he's scared of the sound of the clock, and he takes your pocket watch and 
    destroys it."
    "Morcobashi talks to him and distracts him. Can't go into the room again."
    "You run out of the room. YOu examine the clock pieces and it looks like it could be a key."
    "If you go to the star room again, somebody giggles, and you get a drop of star laugh."
    "Go to the room and feed it to the flower."
    "Go back to Ororo, and when you free him, he hesitates. By this time, we should know that 
    Ororo is going to turn to stone once he is free."
    "Big wave like an earthquake. flashes."
    "Ororo disappears from his room and the dark finally falls."
    "You wake up with a lot of stars, and there's the moon in the sky."
    "There's a door at the end of it. Morcobashi is waiting at the end."
    "He thanks you for what you've done for everyone and gives you a choice whether you 
    want to go back to the house, or to return home."
    "If you wanna go back, you need some of the items ish."
    "If you go home, you wake up in your room, and you feel like you've lost something."
    "But life is just like that, and someone calls you from the door."
    
    "If you choose to go back, go to the flower room and a cute sun creature will talk to you a bit 
    and he says he has a job to do. He said he was asleep for a long time and had such a
    funny dream."
    "Don't you just hate it when you can't remember your dream? He gives you a gift that will 
    make you remember your dream."
    
    #If bad route:
    "Ororo protects Edelia and Ponchu."
    "Ororo talks to the dark like he knows her."
    "You've been talking too much with the shadows!"
    "Well I can't help it, he imprisoned me!"
    "You swing your sword at him and the chains in his leg breaks."
    "Flashes and stuff."
    "You have a choice to kill Edelia and Ponchu, and you can't say no anymore."
    "Once you kill Ponchu, you realize he is your brother."
    "Finally the dark emerges, and she is the Night. Her name is Nyx."
    "Edelia manages to escape."
    "The manticore is hiding from Nyx, so you are tasked to look for him. Nyx calls you her trusted 
    knight."
    "The hallway turns to black."
    "The hunt the Manticore, and you look like the unicorn."
    "Finally, you find him and the ticking clock is making him weak."
    "Nyx enters and tells manticore he is dethroned as Master of the house. 
    He has betrayed everyone. A new mistress is in the throne."
    "Come my faithful knight. The night shall rule endlessly."
    "Psst psst. Hey."
    "Edelia says huh."
    "I'm bot happy with this are you?"
    "They gotta be stopped."
    "Yes yes."
    
    
    
    
    
    
    
    
            
    
    
            

            
            
            
            
        
    

    return
