
################################################################################
## Map screens - Hallway01
################################################################################
init:
    $currentLocation = 1270

label lbl_mapStart_hallway1:
    #show bg hallway1:
    #  xpos 0+ currentLocation
    show screen walkaround
  
    call screen MapScreen_hallway1(currentLocation)
    #$renpy.call_screen('MapScreen_hallway1', currentLocation, _layer='mapLayer')
    
    #jump to returned label
    call expression _return from _call_expression
    
    

#################################################################################

screen MapScreen_hallway1(_xPosOffset=0):
    tag map
    zorder -2
    #add "images/map/bg-hallway01_for prog.png" xpos 0 - _xPosOffset 
    add Solid("#ffffff")    
    add "images/map_hallway01/bg-hallway01_lines.png" xpos 0 - _xPosOffset 
        
    $RightPos = _xPosOffset+200
    $LeftPos = _xPosOffset-200
    
    if LeftPos < 0:
      $LeftPos = 0
      
    if RightPos > 2753 - 800:
      $RightPos = 2753 - 800
      
    #text "[currentLocation]" xpos -300 - _xPosOffset ypos 300
    
    key 'K_RIGHT' action [SetVariable('currentLocation', RightPos), Show('MapScreen_hallway1',None,RightPos)]
    key 'K_LEFT' action [SetVariable('currentLocation', LeftPos), Show('MapScreen_hallway1',None,LeftPos)]
     
    

    #imagemap:
    #    auto "images/map_hallway01/bg-hallway01_%s.png"
    #    xpos 0 - _xPosOffset 
    #    if librarypathclear or ignoreMogu:
    #        hotspot (1540, 50, 185, 320) clicked Return("lbl_mapStart_hallway2")
    #    hotspot ( 110, 115, 160, 270) clicked Return("darkroom")
    #    hotspot ( 431, 125, 232, 257) clicked Return("lbl_hallway1_locked")
    #    hotspot ( 781, 125, 120, 257) clicked Return("deisroom_hub")
    #    hotspot (1070, 95, 135, 290) clicked Return("lbl_hallway1_locked")
    #    hotspot (1337, 97, 160, 290) clicked Return("lbl_hallway1_locked")
    #    hotspot (2040, 124, 153, 255)clicked Return("morcoroom_hub")
    #    hotspot (2327, 91, 93, 277) clicked  Return("nueroom_hub")

#    imagebutton auto "images/map_hallway01/bg-hallway01_darkness_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("lbl_hallway1_darkness") 
#    imagebutton auto "images/map_hallway01/bg-hallway01_holes_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("lbl_hallway1_holes") 
    
    imagebutton auto "images/map_hallway01/bg-hallway01_door1_%s.png" xpos (110 - _xPosOffset) focus_mask None action Return("darkroom") 
    imagebutton auto "images/map_hallway01/bg-hallway01_door2_%s.png" xpos (431 - _xPosOffset) focus_mask None action Return("lbl_hallway1_locked") 
    imagebutton auto "images/map_hallway01/bg-hallway01_door3_%s.png" xpos (781 - _xPosOffset) focus_mask None action Return("deisroom_hub") 
    imagebutton auto "images/map_hallway01/bg-hallway01_door4_%s.png" xpos (1070  - _xPosOffset) focus_mask None action Return("lbl_hallway1_locked") 
    imagebutton auto "images/map_hallway01/bg-hallway01_door5_%s.png" xpos ( 1300- _xPosOffset) focus_mask None action Return("lbl_hallway1_locked") 
    imagebutton auto "images/map_hallway01/bg-hallway01_door6_%s.png" xpos ( 1747- _xPosOffset) focus_mask None action Return("morcoroom_hub") 
    imagebutton auto "images/map_hallway01/bg-hallway01_door7_%s.png" xpos (2040 - _xPosOffset) focus_mask None action Return("nueroom_hub") 
    imagebutton auto "images/map_hallway01/bg-hallway01_door8_%s.png" xpos (2327 - _xPosOffset) focus_mask None action Return("lbl_hallway1_locked")  
    
    
    if not librarypathclear:
        imagebutton auto "images/map_hallway01/bg-hallway01_mogu_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("moguroomfirst") 

    imagebutton auto "images/map_hallway01/bg-hallway01_ede_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("edelia")   
     
    imagebutton auto "gui/E_%s.png" xpos (600) yalign 0.4 focus_mask True action [SetVariable('currentLocation', RightPos), Show('MapScreen_hallway1',None,RightPos)]
    imagebutton auto "gui/W_%s.png" xpos (130) yalign 0.4 focus_mask True action [SetVariable('currentLocation', LeftPos), Show('MapScreen_hallway1',None,LeftPos)]


label lbl_hallway1_locked:
    hide screen walkaround
    show bg hallway01:
        xpos 0 + (2753/2) - currentLocation
    #"[currentLocation]" 
    "It is locked."
    jump lbl_mapStart_hallway1
return
  
label lbl_hallway1_door2:
    hide screen walkaround
    #"[currentLocation]" 
    "It is locked."
    jump lbl_mapStart_hallway1
return
  
label lbl_hallway1_door3:
    hide screen walkaround
    call deisroom_hub
    jump lbl_mapStart_hallway1
return
  
label lbl_hallway1_door4:
    hide screen walkaround
    "It is locked."
    jump lbl_mapStart_hallway1
return
  
label lbl_hallway1_door5:
    hide screen walkaround
    "It is locked."
    jump lbl_mapStart_hallway1
return
  
label lbl_hallway1_door6:
    hide screen walkaround
    call morcoroom_hub
    jump lbl_mapStart_hallway1
return
  
label lbl_hallway1_door7:
    hide screen walkaround
    call nueroom_hub
    jump lbl_mapStart_hallway1
return
    
return
  