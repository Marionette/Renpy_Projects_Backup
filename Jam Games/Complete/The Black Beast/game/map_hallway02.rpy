
################################################################################
## Map screens - Hallway02
################################################################################
init:
    $currentLocation2 = 1250

label lbl_mapStart_hallway2:
    show screen walkaround
  
    call screen MapScreen_hallway2(currentLocation2)
    
    #jump to returned label
    call expression _return from _call_expression1
    
    

#################################################################################

screen MapScreen_hallway2(_xPosOffset=0):
    tag map
    zorder -2
    add Solid("#ffffff")    
    add "images/map_hallway02/linebase.png" xpos 0 - _xPosOffset 
        
    imagebutton auto "images/map_hallway02/3rdfloor_%s.png" xpos (211 - _xPosOffset) focus_mask True action Return("lbl_hallway2_3rdfloor") 
    imagebutton auto "images/map_hallway02/library_%s.png" xpos (553 - _xPosOffset) focus_mask True action Return("lbl_mapStart_library") 
    imagebutton auto "images/map_hallway02/normaldoor_%s.png" xpos (1398 - _xPosOffset) focus_mask True action Return("lbl_hallway2_lockednormal") 
   
    if openStardoor:
        imagebutton auto "images/map_hallway02/star_%s.png" xpos (1694- _xPosOffset) focus_mask True action Return("moguroom_hub") 
    else:
        imagebutton auto "images/map_hallway02/star_%s.png" xpos (1694 - _xPosOffset) focus_mask True action Return("lbl_hallway2_locked") 

    if keytoflowerroom:
        imagebutton auto "images/map_hallway02/garden_%s.png" xpos (1951 - _xPosOffset) focus_mask True action Return("flowerroom") 
    else:
        imagebutton auto "images/map_hallway02/garden_%s.png" xpos (1951 - _xPosOffset) focus_mask True action Return("lbl_hallway2_locked") 

    imagebutton auto "images/map_hallway02/black_%s.png" xpos (2279 - _xPosOffset) focus_mask True action Return("lbl_hallway2_locked") 
    imagebutton auto "images/map_hallway02/stairs2_%s.png" xpos (2565 - _xPosOffset) focus_mask True action Return("lbl_mapStart_hallway1") 

 
#Clock
    imagebutton auto "images/map_hallway02/clockexit2_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("lbl_hallway2_clockexit2")  
    imagebutton auto "images/map_hallway02/brokenclock_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("lbl_hallway2_brokenclock")  
    
# Dark
    imagebutton auto "images/map_hallway02/darkroom2_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("lbl_hallway2_dark")  
    

    #Walking navigation
    use MapScreen_navigation("MapScreen_hallway2", _xPosOffset, 0, 2800)


#--------------------------------------------------------------------------------
  
label lbl_hallway2_locked:
    hide screen walkaround
    scene bg black
    show bg hallway02:
        xpos 0 + (3150/2) - currentLocation2
    #"[currentLocation]" 
    "It is locked."
    jump lbl_mapStart_hallway2
return

label lbl_hallway2_brokenclock:
    hide screen walkaround
    scene bg black
    show bg hallway02:
        xpos 0 + (3150/2) - currentLocation2
    #"[currentLocation]" 
    "It is broken."
    jump lbl_mapStart_hallway2
return

label lbl_hallway2_dark:
    hide screen walkaround
    scene bg black
    show bg hallway02:
        xpos 0 + (3150/2) - currentLocation2
    #"[currentLocation]" 
    "It doesn't seem like a good idea to go in there."
    jump lbl_mapStart_hallway2
return

label lbl_hallway2_3rdfloor:
    hide screen walkaround
    scene bg black
    show bg hallway02:
        xpos 0 + (3150/2) - currentLocation2
    #"[currentLocation]" 
    "I don't think I can go in there yet."
    jump lbl_mapStart_hallway2
return

label lbl_hallway2_lockednormal:
    hide screen walkaround
    scene bg black
    show bg hallway02:
        xpos 0 + (3150/2) - currentLocation2
    #"[currentLocation]" 
    if not FirsttimeNormalDoor:
        "It is locked."
        "...But there was a muffled bump on the other side."
        menu:
            "Knock":
                play sound knock
                "..."
                "....."
                "You don't hear anything anymore."
            "Leave it alone":
                pass
        
        $ FirsttimeNormalDoor = True
        jump lbl_mapStart_hallway2
    "It is locked."    
    jump lbl_mapStart_hallway2
return

label lbl_hallway2_clockexit2:
    hide screen walkaround
    scene bg black
    hide mc
    hide mc horns
    hide mc tail
    show bg hallway02:
        xpos 0 + (3150/2) - currentLocation2
    if not clockexit_seen: 
        "The time is frozen."
        "But I felt compelled to touch the frozen clock."
        $ clockexit2_seen = True
    "Where do I want to go?"
    menu:
        "Stay here.":
            jump lbl_mapStart_hallway2      
        "First Floor Hallway":            
            jump lbl_mapStart_hallway1
        "Somewhere else" if chap1done:
            menu somewhereelse:
                "Clockroom":
                    jump morcoroom_hub
                "Nue's Room":
                    if Nuehatesyou:
                        "You can't go there."
                        jump somewhereelse
                    jump nueroom_hub
                "Star Room":
                    if Moguhatesyou:
                        "You can't go there."
                        jump somewhereelse
                    if not chap1done:
                        "You can't go there yet."
                        jump somewhereelse
                    jump moguroom_hub    
                "Garden" if keytoflowerroom:
                    jump flowerroom
return
