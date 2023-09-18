
################################################################################
## Map screens
################################################################################
init:
    $currentLocation = 1360

label lbl_mapStart_hallway1:
    #show bg hallway1:
    #  xpos 0+ currentLocation
    e "Looks like we're in a hallway."
    call screen MapScreen_hallway1(currentLocation)
    #$renpy.call_screen('MapScreen_hallway1', currentLocation, _layer='mapLayer')
    
    #jump to returned label
    call expression _return from _call_expression
    
screen FrameScreen():
    zorder -1
    #add "images/frame.png"
    add Animation( "images/f00.png", 0.2, 
                   "images/f01.png", 0.2, 
                   "images/f02.png", 0.2, 
                   "images/f03.png", 0.2,)

screen MapScreen_hallway1(_xPosOffset=0):
    tag map
    zorder -2
    #add "images/map/bg-hallway01_for prog.png" xpos 0 - _xPosOffset 
        
    $RightPos = _xPosOffset+100
    $LeftPos = _xPosOffset-100
    
    if LeftPos < 0:
      $LeftPos = 0
      
    if RightPos > 2753 - 800:
      $RightPos = 2753 - 800
      
    text "[currentLocation]" xpos -300 - _xPosOffset ypos 300
    
    key 'K_RIGHT' action [SetVariable('currentLocation', RightPos), Show('MapScreen_hallway1',None,RightPos)]
    key 'K_LEFT' action [SetVariable('currentLocation', LeftPos), Show('MapScreen_hallway1',None,LeftPos)]

    imagemap:
        auto "images/map/bg-hallway01_%s.png"
        xpos 0 - _xPosOffset 
        hotspot (1540, 50, 185, 320) clicked Return("lbl_hallway1_stairs")
        hotspot (110, 115, 160, 270) clicked Return("lbl_hallway1_door1")
        hotspot (420, 120, 253, 267) clicked Return("lbl_hallway1_door2")
        hotspot (770, 120, 126, 266) clicked Return("lbl_hallway1_door3")
        hotspot (1070, 95, 135, 290) clicked Return("lbl_hallway1_door4")
        hotspot (1337, 97, 160, 290) clicked Return("lbl_hallway1_door5")
        hotspot (1745, 106, 166, 280) clicked Return("lbl_hallway1_door6")
        hotspot (2030, 122, 160, 266) clicked Return("lbl_hallway1_door7")

    imagebutton auto "images/map/bg-hallway01_darkness_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("lbl_hallway1_darkness") 
    imagebutton auto "images/map/bg-hallway01_holes_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("lbl_hallway1_holes") 
    
    if not HasItem('clock'):
      imagebutton auto "images/map/bg-hallway01_clock_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("lbl_hallway1_clock") 
    
label lbl_hallway1_stairs:
  "[currentLocation]" 
  "These are stairs."
  jump lbl_mapStart_hallway1
  return
  
label lbl_hallway1_door1:
  "[currentLocation]" 
  "This is a door. The 1st one."
  jump lbl_mapStart_hallway1
  return
  
label lbl_hallway1_door2:
  "This is a door. The 2nd one."
  jump lbl_mapStart_hallway1
  return
  
label lbl_hallway1_door3:
  "This is a door. The 3rd one."
  jump lbl_mapStart_hallway1
  return
  
label lbl_hallway1_door4:
  "This is a door. The 4th one."
  jump lbl_mapStart_hallway1
  return
  
label lbl_hallway1_door5:
  "This is a door. The 5th one."
  jump lbl_mapStart_hallway1
  return
  
label lbl_hallway1_door6:
  "This is a door. The 6th one."
  jump lbl_mapStart_hallway1
  return
  
label lbl_hallway1_door7:
  "This is a door. The 7th one."
  jump lbl_mapStart_hallway1
  return
  
label lbl_hallway1_darkness:
  "What is this darkness?"
  jump lbl_mapStart_hallway1
  return
label lbl_hallway1_holes:
  "What are these holes?"
  jump lbl_mapStart_hallway1
  return
  
label lbl_hallway1_clock:
  "Ooh, a clock." 
  "I bet this will be useful. I better take it."
  $AddItem('clock')
  jump lbl_mapStart_hallway1
  return