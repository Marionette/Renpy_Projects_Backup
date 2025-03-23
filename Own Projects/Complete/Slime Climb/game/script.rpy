# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    image slime climb = "images/slimb climb.png"
    image bg black = Solid("#000")
    default flag_bird = False

transform slime_scroll(x, y, z, t=1.0):
    xoffset 0    
    parallel:
        linear t xalign x
    parallel:
        linear t yalign y
    parallel:
        linear t zoom z
        
transform slime_scroll_shake(x, y, z, t=1.0):
    xoffset 0    
    parallel:
        linear t xalign x
    parallel:
        linear t yalign y
    parallel:
        linear t zoom z
    xoffset -10
    block:
        linear 1.0 xoffset 10
        linear 1.0 xoffset -10
        repeat
transform slime_scroll_shake2(x, y, z, t=1.0):
    yoffset 0    
    parallel:
        linear t xalign x
    parallel:
        linear t yalign y
    parallel:
        linear t zoom z
    yoffset -10
    block:
        linear 1.0 yoffset 10
        linear 1.0 yoffset -10
        repeat

transform cd_transform:
    # This is run before appear, show, or hide.
    #xalign 0.5 yalign 0.5 
    alpha 0.0

    on appear:
        alpha 1.0
    on show:
        zoom .75
        linear .35 zoom 1.0 alpha 1.0
    on hide:
        linear .35 zoom 1.25 alpha 0.0  
        
screen slime_text(_text="", _xalign=0.0, _yalign=0.0):
    #vbox:
    #    yfill True
    #    hbox: 
    #        xalign 0.5
    #        yalign 0.0
    #        text "top"
    #    hbox:
    #        xfill True
    #        #xalign 0.5
    #        yalign 0.5
    #        text "left" xalign 0.0
    #        text "center" xalign 0.5
    #        text "right" xalign 1.0
    #    hbox:
    #        xalign 0.5
    #        yalign 1.0
    #        text "Bottom"
    frame at cd_transform:
        xsize 759
        ysize 268
        xalign _xalign
        yalign _yalign
        background Frame("gui/text_frame.png",5,5,5,5)
        vbox:
            #xmaximum 700
            xalign 0.5
            yalign 0.4
            text _text size 38 text_align 0.5 outlines [ (4, "#FFFFFF", 0, 0) ]

screen slime_text_question(_text="", _xalign=0.0, _yalign=0.0):
    #vbox:
    #    yfill True
    #    hbox: 
    #        xalign 0.5
    #        yalign 0.0
    #        text "top"
    #    hbox:
    #        xfill True
    #        #xalign 0.5
    #        yalign 0.5
    #        text "left" xalign 0.0
    #        text "center" xalign 0.5
    #        text "right" xalign 1.0
    #    hbox:
    #        xalign 0.5
    #        yalign 1.0
    #        text "Bottom"
    frame at cd_transform:
        xsize 759
        ysize 268
        xalign _xalign
        yalign _yalign
        background Frame("gui/text_frame.png",5,5,5,5)
        vbox:
            spacing 50
            #xmaximum 700
            xalign 0.5
            yalign 0.4
            text _text size 38 text_align 0.5 outlines [ (4, "#FFFFFF", 0, 0) ]
            hbox:
                xalign 0.5
                spacing 150
                textbutton "Yes" action Return("Yes")
                textbutton "No" action Return("No")
                

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    #"You've created a new Ren'Py game."

    #"Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
    play music "audio/Wholesome.mp3" fadein 2.0
    window hide
    #show screen slime_text
    
    call lbl_slime_start from _call_lbl_slime_start
    call lbl_slime_1 from _call_lbl_slime_1
    call lbl_slime_2 from _call_lbl_slime_2
    call lbl_slime_3 from _call_lbl_slime_3
    call lbl_slime_4 from _call_lbl_slime_4
    call lbl_slime_5 from _call_lbl_slime_5
    call lbl_slime_6 from _call_lbl_slime_6
    call lbl_slime_7 from _call_lbl_slime_7
    call lbl_slime_8 from _call_lbl_slime_8
    call lbl_slime_9 from _call_lbl_slime_9
    call lbl_slime_10 from _call_lbl_slime_10
    call lbl_slime_11 from _call_lbl_slime_11
    call lbl_slime_12 from _call_lbl_slime_12
    
    call lbl_slime_bird from _call_lbl_slime_bird
    
    call lbl_slime_13 from _call_lbl_slime_13
    call lbl_slime_14 from _call_lbl_slime_14
    call lbl_slime_15 from _call_lbl_slime_15
    call lbl_slime_16 from _call_lbl_slime_16
    call lbl_slime_17 from _call_lbl_slime_17
    call lbl_slime_18 from _call_lbl_slime_18
    call lbl_slime_19 from _call_lbl_slime_19
    call lbl_slime_20 from _call_lbl_slime_20
    call lbl_slime_21 from _call_lbl_slime_21
    call lbl_slime_22 from _call_lbl_slime_22
    
    
    #show slimes layout at slime_scroll(0.4,1.0,0.3,0.0)        
    #pause 916666667
    #show slimes layout at slime_scroll(0.4, 1.0, 0.3 ,0.0)
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.833333333, 0.354545455 )
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.75, 0.409090909 )
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.666666667, 0.463636364 )
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.583333333, 0.518181818 )
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.5, 0.572727273 )
    #pause   
    #
    #show slimes layout at slime_scroll(0.4, 0.458285714, 0.627272727 )
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.422571429, 0.681818182 )
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.382857143, 0.736363636 )
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.357142857, 0.790909091 )
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.311428571, 0.845454545 )
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.275714286, 0.9 )
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.25, 0.954545455 )
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.229166667, 1.009090909 )
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.209166667, 1.063636364 )
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.189166667, 1.118181818 )
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.169166667, 1.172727273 )
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.149166667, 1.227272727 )
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.124166667, 1.281818182 )
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.099166667, 1.336363636 )
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.074166667, 1.390909091 )
    #pause 
    #show slimes layout at slime_scroll(0.4, 0.05, 1.445454545 )
    #pause 
    
    #show slimes layout:
    #    #xanchor 0.5 
    #    xalign 0.4
    #    yalign 0.8
    #    zoom 0.5
    
    #"There once was a slime from the plain,"
    #"He spotted a tower in the rain,"
    #"He climbed to the top,"
    #"Sat down with a plop,"
    #"and thought about getting down again."
    
    show slimes layout at slime_scroll(0.5, 0.5, 0.14, 2.0  )
    pause 
    
    scene bg black with dissolve
    centered "{size=+30}{color=#ffffff}Thanks for playing!{/color}{/size}"
    

    return
    
label lbl_slime_start:

    show slimes layout at slime_scroll(0.078, 0.93, 2.3 ,0.0)
    #0
    show screen slime_text("There was a small but adventurous slime,\n who set out for an arduous climb.", 0.5, 0.2)
    pause 
    hide screen slime_text
    show slimes layout at slime_scroll(0.078, 0.93, 1.3 ,1.0)
    show screen slime_text("Arriving at the huge slime tower,\n the tiny slime did look up and cower.", 0.2, 0.3)
    pause 
    hide screen slime_text
    show slimes layout at slime_scroll(0.098, 0.93, 1.3 ,1.0)
    show screen slime_text("If I get to the top all on my own,\n Across the land my name will be known.", 0.3, 0.3)
    pause 
    hide screen slime_text
    return



    
label lbl_slime_1:
    #1
    show slimes layout at slime_scroll(0.4, 1.0, 0.5 ,2.0)
    show screen slime_text("Determined to climb he came face to face,\n with the huge blue slime who made up the base.",0.4, 0.2)
    pause 
    hide screen slime_text
    show screen slime_text("\"Fair warning young slime, this wont be easy,\n for the top of the tower can get pretty breezy.\"",0.9, 1.0)
    pause 
    hide screen slime_text
    show screen slime_text("\"Thanks for your help\", he quickly replied,\n as he held on tight and climbed the side.",0.2, 1.0)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_2:
    #2
    
    show slimes layout at slime_scroll(0.5, 0.833333333, 0.5 )
    
    show screen slime_text("\"When you get to the top just admire the view\"\n came a voice from below as he crossed the next goo.",0.3, 0.2)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_3:
    #3
    
    show slimes layout at slime_scroll(0.3, 0.7, 0.55 )
    show screen slime_text("\"A climb to the top? You must be quite keen.\"\n Spoke the following slime, a soft shiny green.",0.7, 0.2)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_4:
    #4
    
    show slimes layout at slime_scroll(0.35, 0.6, 0.75 )
    show screen slime_text("\"Just be careful of which side you choose,\n while scaling the tower\", advised the next ooze.",0.5, 0.3)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_5:
    #5
    
    show slimes layout at slime_scroll(0.4, 0.5, 0.8 )
    show screen slime_text("\"Its true\", the following slime agreed,\n \"Not everyone who tries is able to succeed.\"",0.2, 0.1)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_6:
    #6 (orange-ish)
    
    show slimes layout at slime_scroll(0.5, 0.4, 0.8 )
    show screen slime_text("Finally he reached the next slime body,\n Its face all focused, twisted and knotty.",0.6, 0.15)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_7:
    #7
    
    show slimes layout at slime_scroll(0.5, 0.35, 0.9 )
    show screen slime_text("\"Don't mind him\" came down a call from the red.\n \"Hes holding us up with the top of his head.\"",0.1, 0.9)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_8:
    #8
    
    show slimes layout at slime_scroll(0.45, 0.3, 1.1 )
    show screen slime_text("Across the next one he had to creep,\n since this particular slime was still fast asleep.",0.25, 0.25)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_9:
    #9
    
    show slimes layout at slime_scroll(0.4, 0.28, 1.1 )
    show screen slime_text("\"I have to say you're doing quite well\",\n he was told by the next and it made him feel swell.",0.25, 0.4)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_10:

    #10
    
    show slimes layout at slime_scroll(0.4, 0.28, 1.3 )
    show screen slime_text("Our little slime tried to stay out of sight,\n as it seemed the next slimes were having a fight.",0.1, 0.4)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_11:
    #11
    
    show slimes layout at slime_scroll(0.4, 0.25, 1.3  )
    show screen slime_text("\"It's all your fault I've started to slide\",\n heard the little slime as he continued to hide.",0.2, 0.1)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_12:
    #12
    
    show slimes layout at slime_scroll(0.38, 0.23, 1.3  )
    show screen slime_text("\"I think I'll be able to stay here if you drop\",\n smirked a purple slime balanced on top.",0.2, 0.1)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_13:

    show slimes layout at slime_scroll(0.35, 0.21, 1.4 )
    #13 (Blue)
    show screen slime_text("Carefully making sure his step was true,\n he climbed on top of the slime that was blue.",0.2, 0.1)
    pause 
    hide screen slime_text

    #if bird
    if flag_bird:
        show screen slime_text("\"I'm glad to see that you've made it back\n I saw you snatched away in that awful attack.\"",0.4, 0.1)
        pause 
        hide screen slime_text
    return
    
label lbl_slime_14:

    #14
    

    show slimes layout at slime_scroll(0.35, 0.21, 1.4 )
    show screen slime_text("\"Be sure to be careful as you continue\n as how many remain I haven't a clue.\"",0.8, 0.8)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_15:
    #15
    
    show slimes layout at slime_scroll(0.35, 0.2, 1.55  )
    show screen slime_text("\"I don't believe the top is too far\",\n Said a grizzled slime, his face with a scar.",0.3, 0.8)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_16:
    #16
    
    show slimes layout at slime_scroll(0.4, 0.15, 1.6   )
    show screen slime_text("The next slime didn't even notice,\n as the little slime crossed its surface.",0.8, 0.6)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_17:
    #17
    
    show slimes layout at slime_scroll(0.42, 0.15, 1.65   )
    show screen slime_text("Holding the green slime above very tight,\n in the hope it didn't fall out of sight.",0.8, 0.2)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_18:
    #18
    
    show slimes layout at slime_scroll(0.38, 0.13, 1.65  )
    show screen slime_text("The slime above also tried to aid\n \"We've got you so don't be afraid.\"", 0.1, 0.1)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_19:
    #19
    
    show slimes layout at slime_scroll(0.42, 0.09, 1.7 )
    show screen slime_text("The gray slime above seemed to be distracted,\n but luckily the climb wasn't impacted.",0.8, 0.8)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_20:
    #20
    
    show slimes layout at slime_scroll(0.37, 0.06, 1.7 )
    show screen slime_text("Soon he had arrived at the penultimate slime,\n and the end was near for this arduous climb.", 0.1, 0.8)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_21:
    #21 (yellow)
    
    show slimes layout at slime_scroll(0.4, 0.05, 2.0 )
    show screen slime_text("\"I have to say your skills make the chop,\n as you've come all this way and arrived at the top!\"", 0.8, 0.8)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_22:
    #22 (end)
    
    show slimes layout at slime_scroll(0.4, 0.02, 2.5 )
    show screen slime_text("On top of the tower his journey now ended,", 0.1, 0.1)
    pause 
    hide screen slime_text
    show slimes layout at slime_scroll(0.4, 0.02, 3.0 )
    show screen slime_text("He took in the view,\n {size=+20}utterly splendid!{/size}", 0.1, 0.1)
    pause 
    hide screen slime_text
    return
    
label lbl_slime_bird:
    #Bird part
    show slimes layout at slime_scroll(0.45, 0.18, 1.5)
    show screen slime_text("The journey to the top could be quite clean\n thought the little slime watching the dangling green.", 0.8, 0.1)
    pause 
    hide screen slime_text
    
    show slimes layout at slime_scroll(0.45, 0.2, 1.5)
    call screen slime_text_question("Ch-ooze to take a shortcut?",  0.8, 0.1)
    if _return == "Yes":
        #call lbl_slime_bird
        $flag_bird = True
        pass
    else:
        return
        
    show screen slime_text("If I skip a few slimes I could continue with ease\n so he reached out and attempted to sieze,", 0.1, 0.1)
    pause 
    hide screen slime_text
    stop music
    show screen slime_text("However as the little slime started to reach\n he was caught off guard by a terrible screech.", 0.1, 0.1)
    with vpunch
    pause 
    hide screen slime_text

    show slimes layout at slime_scroll_shake(0.75, 0.10, 5.2)
    show screen slime_text("With one great swoop the little slime found\n himself in the air high off the ground.", 0.1, 0.1)
    pause 
    hide screen slime_text
    show slimes layout at slime_scroll_shake(0.78, 0.06, 1.6)
    show screen slime_text("And the source of the screech he had heard\n came from the beak of a fearsome bird.", 0.1, 0.8)
    pause 
    hide screen slime_text

    show slimes layout at slime_scroll_shake(0.78, 0.08, 2.8)
    show screen slime_text("As the bird flew the ground was a blur,\n but to escape he needed to stir.", 0.8, 0.1)
    pause 
    hide screen slime_text
    show screen slime_text("Wrapping himself around the bird he did squeeze\n and as it opened its mouth he was caught by the breeze.", 0.8, 0.8)
    pause 
    hide screen slime_text

    show slimes layout at slime_scroll_shake2(0.82, 0.36, 3.1)
    show screen slime_text("As he fell the slime spun around\n plummeting towards the approaching ground.", 0.5, 0.9)
    pause 
    hide screen slime_text
    show screen slime_text("Up in the air he noticed a stick,\n and thought it was perfect and would do the trick.", 0.9, 0.1)
    pause 
    hide screen slime_text
    
    play music "audio/Wholesome.mp3" fadein 2.0
    show slimes layout at slime_scroll(0.94, 0.63, 1.5)
    show screen slime_text("Flattening his body to slow his descent,\n he aimed for the stick to try and prevent", 0.5, 0.1)
    pause 
    hide screen slime_text
    show slimes layout at slime_scroll(0.88, 0.63, 0.5)
    show screen slime_text("A long fall to the bottom,\n as starting again would be quite a problem.", 0.5, 0.2)
    pause 
    hide screen slime_text

    show slimes layout at slime_scroll(0.5, 0.35, 0.9 )
    show screen slime_text("Remaining careful again he retraced,\n his steps up the tower of slimes with haste.", 0.1, 0.1)
    pause 
    hide screen slime_text
    show slimes layout at slime_scroll(0.45, 0.2, 1.5)
    show screen slime_text("It wasn't long before he managed to reach,\n the same awful spot where he'd heard that screech.", 0.9, 0.1)
    pause 
    hide screen slime_text
    return
