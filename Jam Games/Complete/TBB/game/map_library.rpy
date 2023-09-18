
################################################################################
## Map screens - Library
################################################################################
init:
    $currentLocation3 = 1808

label lbl_mapStart_library:
    show screen walkaround
  
    call screen MapScreen_library(currentLocation3)
    
    #jump to returned label
    call expression _return from _call_expression2
    
    

#################################################################################

screen MapScreen_library(_xPosOffset=0):
    tag map
    zorder -2
    #add "images/map/bg-hallway01_for prog.png" xpos 0 - _xPosOffset 
        
    $RightPos = _xPosOffset+100
    $LeftPos = _xPosOffset-100
    
    if LeftPos < 0:
      $LeftPos = 0
      
    if RightPos > 1808 - 800:
      $RightPos = 1808 - 800
      
    text "[currentLocation3]" xpos 0 - _xPosOffset ypos 300
    
    key 'K_RIGHT' action [SetVariable('currentLocation3', RightPos), Show('MapScreen_library',None,RightPos)]
    key 'K_LEFT' action [SetVariable('currentLocation3', LeftPos), Show('MapScreen_library',None,LeftPos)]

    imagemap:
        auto "images/map_library/bg-library_%s.png"
        xpos 0 - _xPosOffset 
        hotspot (355, 133, 175, 258) clicked Return("readabookinlibrary")
        hotspot (571, 116, 140, 208) clicked Return("readabookinlibrary")
        hotspot (1614, 79, 65, 132) clicked Return("lbl_mapStart_hallway2")
        # hotspot (2569, 0, 277, 370) clicked Return("lbl_mapStart_hallway1")
        #hotspot (2327, 91, 93, 277) clicked Return("nueroom_hub")
        
    imagebutton auto "images/map_library/bg-library_mary_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("maryroom") 
    if not ramhorn:
        imagebutton auto "images/map_library/bg-library_horn_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("hornevent")
    
     

label hornevent:
    hide screen walkaround
    scene bg ramskull
    "It's a portrait of a ram skull."
    if bookforDeis and not Marygivesunicornhorn and not chap1done:
        show mr base at chright
        "Hey."
        "Can I ask you why you're looking for that?"
        "She asks for the book you have in your hands and asks you why you need 
        a weapon."
        "She'll give you something else in its place."
        "Maybe a unicorn horn, which is too short to be a weapon."
        "Might be important."
        $ unicornhorn = True
        $ Marylikesyou = True
        $ Marygivesunicornhorn = True
        hide mr base
        hide mc base at mcleft
        call maryroom_hub  
    if not chap1done and not unicornhorn and not puzzlegameforhorndone:
        "Puzzle game to get the weapon."
        $ puzzlegameforhorn = True
        $ puzzlegameforhorndone = True
    if answertohornpuzzle and not answertohornpuzzleMary:
        "What are you doing?!"
        "I told you not to take it!"
        "Mary hates you now."
        "Take the horn and Mary will stop talking to you."
        $ Maryhatesyou = True
        $ ramhorn = True
        $ answertohornpuzzleMary = True
        hide mr base
        hide mc base at mcleft
        call lbl_mapStart_hallway2
    jump lbl_mapStart_library

return
  
