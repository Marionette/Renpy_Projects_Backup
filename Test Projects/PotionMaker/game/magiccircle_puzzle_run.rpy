###################################################################
# The dialogue here probably wants to be updated in the real game #
###################################################################

init:
  define ingredient_count = 3

# Call this label to start the puzzle
label puzzle_start():
    scene bg black
    jc "Ok, so i just need to add the right ingredients to make the potion. Which ones should i use though?"
    
    $mc_dragged = []
    $mc_dropped = []
    $puzzle_complete = False
    $xloc = []
    $yloc = []
    
    #Randomise the locations the sigils appear in at the start of each puzzle run
    python:
        ylist = [0.2, 0.3, 0.4,0.5, 0.6, 0.7, 0.8, 0.25, 0.35, 0.45,0.55, 0.65, 0.75]
        xlist = [0.05, 0.1, 0.15, 0.2, 0.80, 0.85, 0.9, 0.95]
        for i in range (8):
            x = renpy.random.choice(xlist)
            xlist.remove(x)
            xloc.append(x)  
            y = renpy.random.choice(ylist)
            ylist.remove(y)            
            yloc.append(y) 
    
    while not puzzle_complete:
        call puzzle_magiccircle() from _call_puzzle_magiccircle
    jump puzzle_finished


label puzzle_finished():
    #hide screen puzzle_trade_status
    #jc "Looks like I made [puzzle_trades] trades and collected [puzzle_teeth] teeth."
    #if puzzle_teeth >= 7:
    #    jc "I won! What do I win?"
    #else:
    #    jc "Looks like I came up short of what I needed. Oh well."
    return


################################################################
# You may wish to customize the screen, but it is not required #
################################################################

screen current_circle():
    add "images/icons/WitchCraftIcons_71_t.png" xpos 440 ypos 435
    $index =0
    #for drops in mc_dropped:
    #    if drops == "drop_target1":
    #        $sigil = "images/minigame/MagicCircle/Sigil" + mc_dragged[index] + ".png"
    #        add sigil xpos 845 ypos 145
    #    if drops == "drop_target2":
    #        $sigil = "images/minigame/MagicCircle/Sigil" + mc_dragged[index] + ".png"
    #        add sigil xpos 345 ypos 145
    #    if drops == "drop_target3":
    #        $sigil = "images/minigame/MagicCircle/Sigil" + mc_dragged[index] + ".png"
    #        add sigil xpos 595 ypos 580
    #    if drops == "drop_target4":
    #        $sigil = "images/minigame/MagicCircle/Sigil" + mc_dragged[index] + ".png"
    #        add sigil xpos 595 ypos 290
    #    $index += 1
        

screen show_potion(_index):
    $potionnumber = 86+ _index
    add "images/icons/WitchCraftIcons_[potionnumber]_t.png" xalign 0.5 yalign 0.5

screen draggable(_name, _icon, _xpos=0, _ypos=0):
                drag:
                    drag_name _name
                    child _icon
                    droppable False
                    dragged sigil_dragged
                    xpos _xpos
                    ypos _ypos
                    
                    #ycenter 0#200 + i%3*200#yloc[i]
                    #xcenter 0#800 + j*200#xloc[i]  

screen puzzle_drag_magiccircle():
      
    tag puzzle    
    use current_circle
    
    text "Drag the ingredients into the pot." xalign 0.5 yalign 0.0 yoffset 52 xoffset 2 color "#000"
    text "Drag the ingredients into the pot." xalign 0.5 yalign 0.0 yoffset 50 color "#fff"
        
    $j=0
    draggroup:
        #Places a draggable sigil for each of the 8 available sigils
        #grid 3 3:
        use draggable(0,"images/icons/WitchCraftIcons_09_t.png", 1050, 250)
        use draggable(1,"images/icons/WitchCraftIcons_37_t.png", 1300, 250)
        use draggable(2,"images/icons/WitchCraftIcons_38_t.png", 1550, 250)
        use draggable(3,"images/icons/WitchCraftIcons_39_t.png", 1050, 500)
        use draggable(4,"images/icons/WitchCraftIcons_51_t.png", 1300, 500)
        use draggable(5,"images/icons/WitchCraftIcons_63_t.png", 1550, 500)
        use draggable(6,"images/icons/WitchCraftIcons_70_t.png", 1050, 750)
        use draggable(7,"images/icons/WitchCraftIcons_74_t.png", 1300, 750)
        use draggable(8,"images/icons/WitchCraftIcons_75_t.png", 1550, 750)
        
        # Transparent drag target for each droppable location
        if not "drop_target1" in mc_dropped:
            drag:
                drag_name "drop_target1" #right
                child Transform("#fff0", size=(300, 300))
                draggable False
                xpos 440
                ypos 435
        if not "drop_target2" in mc_dropped:
            drag:
                drag_name "drop_target2" #left
                child Transform("#fff0", size=(300, 300))
                draggable False
                xpos 440
                ypos 435
        if not "drop_target3" in mc_dropped:
            drag:
                drag_name "drop_target3" #center
                child Transform("#fff0", size=(300, 300))
                draggable False
                xpos 440
                ypos 435
        #if not "drop_target4" in mc_dropped:
        #    drag:
        #        drag_name "drop_target4" #bottom
        #        child Transform("#fff0", size=(100, 100))
        #        draggable False
        #        xpos 590
        #        ypos 570
    

####################################################
# You should not need to touch anything under here #
####################################################

init python:
    def sigil_dragged(drags, drop):
    
        if not drop:
            return
        
        #Adds the dragged and dropped positions to a list 
        #so they can be removed from the selections        
        store.mc_dragged.append(drags[0].drag_name)
        store.mc_dropped.append(drop.drag_name)
        
        return True

label puzzle_magiccircle():

    show bg black behind thefigure
    window hide
    
    call screen puzzle_drag_magiccircle()
    #hide bg black
    window auto
    
    if len(mc_dropped) == ingredient_count:
        $puzzle_complete = True
        
        # The correct solution will have the correct numbered sigil in the spot with the same number (ie 1-4)
        if ((mc_dragged[0] in mc_dropped[0]) and (mc_dragged[1] in mc_dropped[1]) and (mc_dragged[2] in mc_dropped[2])):            
            hide screen current_circle
            
            show circle complete
            jc "I think thats correct."
            show circle complete_glow with dissolve
            jc "Wow, i can practcally feel the magic comming off this one."
            show circle complete with dissolve
            jc "Once i have everything else set up ill be ready for the spell."
            #$Boilerroom_MagicCircleComplete = True
        else:
            show screen show_potion(1)
            jc "Hmm, I wonder what it does though."
            hide screen show_potion
            
    return