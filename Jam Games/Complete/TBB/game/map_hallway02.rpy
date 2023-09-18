
################################################################################
## Map screens - Hallway02
################################################################################
init:
    $currentLocation2 = 0

label lbl_mapStart_hallway2:
    show screen walkaround
  
    call screen MapScreen_hallway2(currentLocation2)
    
    #jump to returned label
    call expression _return from _call_expression1
    
    

#################################################################################

screen MapScreen_hallway2(_xPosOffset=0):
    tag map
    zorder -2
    #add "images/map/bg-hallway01_for prog.png" xpos 0 - _xPosOffset 
        
    $RightPos = _xPosOffset+100
    $LeftPos = _xPosOffset-100
    
    if LeftPos < 0:
      $LeftPos = 0
      
    if RightPos > 3050 - 800:
      $RightPos = 3050 - 800
      
    #text "[currentLocation2]" xpos 0 - _xPosOffset ypos 300
    
    key 'K_RIGHT' action [SetVariable('currentLocation2', RightPos), Show('MapScreen_hallway2',None,RightPos)]
    key 'K_LEFT' action [SetVariable('currentLocation2', LeftPos), Show('MapScreen_hallway2',None,LeftPos)]

    imagemap:
        auto "images/map_hallway02/bg-hallway02_%s.png"
        xpos 0 - _xPosOffset 
        hotspot (1700, 84, 108, 294) clicked Return("moguroom_hub")
        hotspot (2569, 0, 277, 370) clicked Return("lbl_mapStart_hallway1")
        #hotspot (2327, 91, 93, 277) clicked Return("nueroom_hub")
        
    imagebutton auto "images/map_hallway02/bg-hallway02_librarydoor_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("lbl_mapStart_library") 
    imagebutton auto "images/map_hallway02/bg-hallway02_flower_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("flowerroom") 

   

return
  
label lbl_hallway2_locked:
    hide screen walkaround
    show bg hallway02:
        xpos 0 + (2753/2) - currentLocation
    #"[currentLocation]" 
    "It is locked."
    jump lbl_mapStart_hallway2
return
