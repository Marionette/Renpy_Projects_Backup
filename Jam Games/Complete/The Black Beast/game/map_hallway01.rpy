
################################################################################
## Map screens - Hallway01
################################################################################
init:
    $currentLocation = 1270

label lbl_mapStart_hallway1:
    scene bg black
    show screen FrameScreen
    show screen walkaround
  
    call screen MapScreen_hallway1(currentLocation)
    call expression _return from _call_expression
    
    

#################################################################################
#--------------------------------------------------------------------------------
screen MapScreen_navigation(_locationScreen='MapScreen_hallway1', _xPosOffset=0, _xmin=0, _xmax=2800):
    $mousepos = renpy.get_mouse_pos()
    $newOffset = _xPosOffset-(400-mousepos[0])    
    if newOffset < _xmin:
      $newOffset = _xmin      
    if newOffset > _xmax - 800:
      $newOffset = _xmax - 800
      
    $walkdir = "left"
    if mousepos[0] > 400:
      $walkdir = "right"
    if mousepos[0] > 450 or mousepos[0] < 350:
      imagebutton idle "images/footbase.png" hover "images/footbase.png" ypos 375 focus_mask None mouse "walk"+walkdir action[SetVariable('currentLocation', newOffset), Show(_locationScreen, None, newOffset)] 
    #text "[mousepos[0]], [mousepos[1]] = [newOffset]" color "#000" xalign 0.5 yalign 0.5
#--------------------------------------------------------------------------------
    
screen MapScreen_hallway1(_xPosOffset=0):
    tag map
    zorder -2
    #add "images/map/bg-hallway01_for prog.png" xpos 0 - _xPosOffset 
    add Solid("#ffffff")    
    add "images/map_hallway01/linebase.png" xpos 0 - _xPosOffset 

  
    if DarkAbandon: 
        imagebutton auto "images/map_hallway01/door1_%s.png" xpos (157 - _xPosOffset) focus_mask True action Return("lbl_hallway1_DarkAbandon") 
    else:
        imagebutton auto "images/map_hallway01/door1_%s.png" xpos (157 - _xPosOffset) focus_mask True action Return("darkroom") 
        
    imagebutton auto "images/map_hallway01/door2_%s.png" xpos (454 - _xPosOffset) focus_mask None action Return("lbl_hallway1_locked") 
    imagebutton auto "images/map_hallway01/door3_%s.png" xpos (804 - _xPosOffset) focus_mask None action Return("deisroom_hub") 
    imagebutton auto "images/map_hallway01/door4_%s.png" xpos (1096  - _xPosOffset) focus_mask None action Return("lbl_hallway1_locked") 
    imagebutton auto "images/map_hallway01/door5_%s.png" xpos ( 1323- _xPosOffset) focus_mask None action Return("lbl_hallway1_locked") 
    imagebutton auto "images/map_hallway01/door6_%s.png" xpos ( 1793- _xPosOffset) focus_mask None action Return("lbl_hallway1_locked") 
    
    if badpathdone:
        imagebutton auto "images/map_hallway01/door7_%s.png" xpos (2060 - _xPosOffset) focus_mask None action Return("morco_demo_bad")
    else:  
        imagebutton auto "images/map_hallway01/door7_%s.png" xpos (2060 - _xPosOffset) focus_mask None action Return("morcoroom_hub")  
  
    if Nuehatesyou:  
         imagebutton auto "images/map_hallway01/door8_%s.png" xpos (2351 - _xPosOffset) focus_mask None action Return("nuehatesyou")
    else:
         imagebutton auto "images/map_hallway01/door8_%s.png" xpos (2351 - _xPosOffset) focus_mask None action Return("nueroom_hub")  
    
# Ede and Mogu
    if not librarypathclear:
        imagebutton auto "images/map_hallway01/mogu_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("moguroomfirst") 
    if EdeliaPresent:
        imagebutton auto "images/map_hallway01/ede_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("edelia")   
# Clock Exit
    imagebutton auto "images/map_hallway01/clockexit_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("lbl_hallway1_clockexit") 
# Stairs
    if librarypathclear or ignoreMogu:
        imagebutton auto "images/map_hallway01/stairs_%s.png" xpos (1563 - _xPosOffset) focus_mask True action Return("lbl_mapStart_hallway2") 
       

    #Walking navigation
    use MapScreen_navigation("MapScreen_hallway1", _xPosOffset, 0, 2800)
#--------------------------------------------------------------------------------

  
label lbl_hallway1_locked:
    hide screen walkaround
    show bg black
    hide mc
    hide mc horns
    hide mc tail
    show bg hallway01:
        xpos 0 + (2800/2) - currentLocation
    "It is locked."
    jump lbl_mapStart_hallway1
return
 
label lbl_hallway1_clock:
    hide screen walkaround
    show bg black
    hide mc
    hide mc horns
    hide mc tail
    show bg hallway01:
        xpos 0 + (2800/2) - currentLocation
    "The time is frozen."
    jump lbl_mapStart_hallway1
return

label lbl_hallway1_DarkAbandon:
    hide screen walkaround
    show bg black
    hide mc
    hide mc horns
    hide mc tail
    show bg hallway01:
        xpos 0 + (2800/2) - currentLocation
    "I don't want to go back there anymore."
    jump lbl_mapStart_hallway1
return

label nuehatesyou:
    hide screen walkaround
    show bg black
    hide mc
    hide mc horns
    hide mc tail
    show bg hallway01:
        xpos 0 + (2800/2) - currentLocation
    
    "I can't open this door anymore."
    jump lbl_mapStart_hallway1
return

label lbl_hallway1_clockexit:
    hide screen walkaround
    scene bg black
    hide mc
    hide mc horns
    hide mc tail
    show bg hallway01:
        xpos 0 + (2800/2) - currentLocation
    if not clockexit_seen:    
        "The time is frozen."
        "But I felt compelled to touch the frozen clock."
        $ clockexit_seen = True
        
    #######################################
    menu:
        "DEBUG - DELETE ME"
        "Stay here":
            jump lbl_mapStart_hallway1      
        "Second Floor Hallway":            
            jump lbl_mapStart_hallway2
        "Library" :
            jump lbl_mapStart_library
        "Somewhere else" :
            menu:
                "Clockroom":
                    jump morcoroom_hub
                "Nue's Room":
                    if Nuehatesyou:
                        "I can't go there."
                        return
                    jump nueroom_hub
                "Star Room":
                    if Moguhatesyou:
                        "I can't go there."
                        return
                    if not openStardoor:
                        "I can't go there yet."
                        return
                    jump moguroom_hub    
                "Garden" if keytoflowerroom:
                    jump flowerroom

    ##########################################    
    "Where do I want to go?"
    menu:
        "Stay here":
            jump lbl_mapStart_hallway1      
        "Second Floor Hallway" if ignoreMogu or librarypathclear:            
            jump lbl_mapStart_hallway2
        "Library" if ignoreMogu or FirstTimeMary:
            jump lbl_mapStart_library
        "Somewhere else" if chap1done:
            menu:
                "Clockroom":
                    jump morcoroom_hub
                "Nue's Room":
                    if Nuehatesyou:
                        "I can't go there."
                        return
                    jump nueroom_hub
                "Star Room":
                    if Moguhatesyou:
                        "I can't go there."
                        return
                    if not openStardoor:
                        "I can't go there yet."
                        return
                    jump moguroom_hub    
                "Garden" if keytoflowerroom:
                    jump flowerroom
return