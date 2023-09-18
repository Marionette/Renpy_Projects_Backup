
#-----------------------------------------------------------------------
screen ClickableItem(_ItemName, _Xpos, _Ypos):
    
    $itemImage = "images/items/items_"+_ItemName.lower()+"_%s.png"
    
    #Test use only
    $itemImage = "images/items/items_unknown_%s.png"
    
    #text itemImage
    #text inventory.inventory_hand[0].lower()
    $currentItem = ""
    if inventory.inventory_hand:
      $currentItem = inventory.inventory_hand[0]
      
    if(not _ItemName == currentItem):
      imagebutton auto itemImage xpos _Xpos ypos _Ypos action Return(_ItemName)
    
#-----------------------------------------------------------------------
screen FixedItem(_RoomName, _ItemName, _Xpos, _Ypos):
    
    $room_status_modifier = "_"
    #if Inventory_active == 'CatEyes':
    #  if(_ItemName == 'blanket_bump' or _ItemName == 'blanket'): 
    #    $room_status_modifier = "_nv_"
      
    #$itemImage = "images/items/"+_RoomName.lower()+room_status_modifier+_ItemName.lower()+"_%s.png"
    $itemImage = "images/items/"+_RoomName.lower()+"/"+_RoomName.lower()+"_"+_ItemName.lower()+".png"
    
    #Test use only
    #$itemImage = "images/items/items_unknown_%s.png"
    
    #text itemImage
    #text inventory.inventory_hand[0].lower()
    #$currentItem = ""
    #if inventory.inventory_hand:
    #  $currentItem = inventory.inventory_hand[0]
      
    #if(not _ItemName == currentItem):
    #imagebutton auto itemImage xpos _Xpos ypos _Ypos focus_mask True action Return(_ItemName)
    imagebutton idle itemImage hover itemImage xpos _Xpos ypos _Ypos focus_mask True mouse "interest" action Return(_ItemName)
    
#-----------------------------------------------------------------------

##############################################################################
# Rooms Screens 
#
  
#-----------------------------------------------------------------------
init -2:
    transform config_eff(_rotate):
        on idle:
            easein 0.1 rotate _rotate+0
        on selected_idle:
            easein 0.5 rotate _rotate+0
        on hover:
            easein 0.1 rotate _rotate+5
            easein 0.1 rotate _rotate-5
            repeat
        on selected_hover:
            easein 0.3 rotate _rotate+5
            easein 0.3 rotate _rotate-5
            repeat

    $rotate_north = 0
    $rotate_N = 0
    $rotate_NE = 45
    $rotate_E = 90
    $rotate_SE = 135
    $rotate_S = 180
    $rotate_SW = 225
    $rotate_W = 270
    $rotate_NW = 315
    
screen Map_arrow(_leadsTo, _direction, _xpos, _ypos, _size = 75):
  $idleimg = im.Scale("gui/N_idle.png", _size, _size)
  $hoverimg = im.Scale("gui/N_hover.png", _size, _size)
  $groundimg = im.Scale("gui/N_ground.png", _size, _size)
  imagebutton idle idleimg hover hoverimg insensitive groundimg xpos _xpos ypos _ypos focus_mask True action Return(_leadsTo) at config_eff(_direction)
  
screen Exploration_Navigation:
    if roomName == 'bedroom1':
      if not Bedroom1_DoorLocked:
        use Map_arrow(['Move','lbl_hallway'], rotate_E, 300,300)
    if roomName == 'bedroom2':
      use Map_arrow(['Move','lbl_hallway'], rotate_E, 1150,200)
    if roomName == 'hallway':
      use Map_arrow(['Move','lbl_bedroom1'], rotate_E, 1150,200)
      if Hallway_Bedroom2DoorUnlocked:
        use Map_arrow(['Move','lbl_bedroom2'], rotate_W, 350,200)
      use Map_arrow(['Move','lbl_bathroom1'], rotate_NE, 550,500)
      use Map_arrow(['Move','lbl_livingroom1'], rotate_SW, 100,500)
    if roomName == 'bathroom1':
      use Map_arrow(['Move','lbl_hallway'], rotate_S, 600,600)
      
    if roomName == 'livingroom1':
      use Map_arrow(['Move','lbl_hallway'], rotate_NE, 1150,200)
      if Livingroom1_PhoneCallHappened:
        use Map_arrow(['Move','lbl_livingroom2'], rotate_SE, 950,200)
        use Map_arrow(['Move','lbl_kitchen'], rotate_E, 750,200)
    if roomName == 'livingroom2':
      use Map_arrow(['Move','lbl_hallway'], rotate_NW, 900,200)
      if Livingroom2_BasementDoorUnlocked:
        use Map_arrow(['Move','lbl_basement1'], rotate_N, 300,400)
      use Map_arrow(['Move','lbl_livingroom1'], rotate_E, 800,500)
      use Map_arrow(['Move','lbl_kitchen'], rotate_W, 50,600)
    if roomName == 'kitchen':
      use Map_arrow(['Move','lbl_livingroom1'], rotate_E, 1100,200)
      use Map_arrow(['Move','lbl_livingroom2'], rotate_SW, 1150,300)
      
    if roomName == 'basement1':
      use Map_arrow(['Move','lbl_livingroom2'], rotate_NE, 1150,200)
      if not Basement1_SpiderAlive:
        use Map_arrow(['Move','lbl_basement2'], rotate_SE, 900,200)
    if roomName == 'basement2':
      use Map_arrow(['Move','lbl_livingroom2'], rotate_NW, 1150,200)
      use Map_arrow(['Move','lbl_basement1'], rotate_SE, 600,600)
      if Basement2_OfficeDoorUnlocked:
        use Map_arrow(['Move','lbl_office'], rotate_NW, 250,360)
      if Basement2_Bathroom2DoorUnlocked:
        use Map_arrow(['Move','lbl_bathroom2'], rotate_NE, 560,300)
      if Basement2_BoilerroomDoorUnlocked:
        use Map_arrow(['Move','lbl_boilerroom'], rotate_N, 420,350)
    if roomName == 'bathroom2':
      use Map_arrow(['Move','lbl_basement2'], rotate_S, 600,600)
    if roomName == 'office':
      use Map_arrow(['Move','lbl_basement2'], rotate_S, 600,600)
    if roomName == 'boilerroom':
      use Map_arrow(['Move','lbl_basement2'], rotate_S, 600,600)
  
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
screen Exploration_Bedroom1:
    #if Inventory_active == 'CatEyes':
    #  add "images/backgrounds/bedroom1_nv.png"    
    #else:
    add 'bg bedroom1'   
    $roomName = "bedroom1"
    use FixedItem(roomName, "bedsidetable", 0,0)
    use FixedItem(roomName, "door", 0,0)
    if not Bedroom1_DoorHandleYarn:
      use FixedItem(roomName, "doorhandle", 0,0)
    else:
      use FixedItem(roomName, "yarnhandle", 0,0)
    use FixedItem(roomName, "drawers_front", 0,0)
    use FixedItem(roomName, "drawers_top", 0,0)
    use FixedItem(roomName, "books", 0,0)
    use FixedItem(roomName, "lamp", 0,0)
    use FixedItem(roomName, "mirror", 0,0)
    use FixedItem(roomName, "laundrybasket", 0,0)
    if Bedroom1_ClawdiaAwake:
      use FixedItem(roomName, "bed", 0,0)
    else:  
      use FixedItem(roomName, "bed_bump", 0,0)
    
    if inventory.inventory_hand:
      if not Boilerroom_Bedroom1CandlePlaced:
        if not inventory.inventory_hand[0] == 'candle_bedroom1':
          use FixedItem(roomName,"candle_bedroom1", 0, 0)
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == roomName:
          use FixedItem(roomName,"MouseToy", 0, 0)
      if not inventory.inventory_hand[0] == 'Pencil':
        use FixedItem(roomName,"Pencil", 0, 0)
    else:
      if not Boilerroom_Bedroom1CandlePlaced:
        use FixedItem(roomName,"candle_bedroom1", 0, 0)
      if ClawdiaLocation == roomName:
        use FixedItem(roomName,"MouseToy", 0, 0)
      use FixedItem(roomName,"Pencil", 0, 0)
      
    
    #In bedsidetable drawer
    #use ClickableItem("LazerPen", 450, 350)
    #use ClickableItem("YarnBall", 450, 050)
    if NightVision_active:
      if Bedroom1_LightsOff:
        add "images/backgrounds/NightVision.png" 
      else:
        add "images/backgrounds/NightVision_Bright.png" 
    else:
      if Bedroom1_LightsOff:
        add "images/backgrounds/Dark.png"
    
    use Exploration_Navigation
    use hand_inventory
    if Bedroom1_CollectionsActive:
      use room_inventory(roomName)
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#---
label ShowBedroom1():
    $CurrentRoomName = "bedroom1"

    #"Show bedroom 1"
    scene bg bedroom1
    if Bedroom1_ClawdiaAwake:
      show item blanket
    else:
      show item blanket bump
    #scene bg bedroom1
      
    if inventory.inventory_hand:
      if not Boilerroom_Bedroom1CandlePlaced:
        if not inventory.inventory_hand[0] == 'candle_bedroom1':
          show item_bedroom1_candle
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == CurrentRoomName:
          show item_bedroom1_mousetoy
      if not inventory.inventory_hand[0] == 'Pencil':
        show item_bedroom1_pencil
    else:
        #"Show all items"
        if not Boilerroom_Bedroom1CandlePlaced:
            show item_bedroom1_candle
        show item_bedroom1_pencil
        if ClawdiaLocation == CurrentRoomName:
          show item_bedroom1_mousetoy
          
    if Bedroom1_DoorHandleYarn:
      show item_bedroom1_yarnhandle
    
    if inventory.inventory_hand:
      if inventory.inventory_hand[0] == 'MouseToy':
        $ClawdiaLocation = CurrentRoomName
        
    if NightVision_active:
      if Bedroom1_LightsOff:
        show roomeffect nightvision
      else:
        show roomeffect nightvision_bright
    else:
      if Bedroom1_LightsOff:
        show roomeffect dark
        
    return
    
label ShowBedroom1WithChars:
    $CurrentRoomName = "bedroom1"
    call ShowBedroom1
              
    if ClawdiaLocation == CurrentRoomName:
      show jessicaperson neutral:
        yalign -0.5
        xalign 0.7
        
    show jessicat happy at left
    return
#---
  
label lbl_bedroom1:
    #scene bg bedroom1
    #if Bedroom1_ClawdiaAwake:
    #  show item blanket
    #else:
    #  show item blanket bump
    call ShowBedroom1WithChars
    jc "Its my Bedroom"
    jc "Lets see what else we can find here..."
    

label lbl_bedroom1_explore:
    $roomName = "bedroom1"
    $inventory.SetCurrentRoom(roomName)
    call screen Exploration_Bedroom1
    $res = _return
    $ShouldPickUp = False
    
    #scene bg bedroom1
    #if NightVision_active:
    #  show roomeffect nightvision
    #else:
    #  if Bedroom1_LightsOff:
    #    show roomeffect dark
    call ShowBedroom1WithChars
    
    #if Bedroom1_LightsOff:
    #  if not NightVision_active:
    #    "I can't see what that is right now."
    #    jump lbl_bedroom1_explore
        
    if res[0] == 'Move':
      $labelname = res[1]
      if config.developer:
        jc "Ok lets go to [labelname]"
      jump expression labelname
      
    if Bedroom1_LightsOff:
      if not NightVision_active:
        "I can't see what that is right now."
        jump lbl_bedroom1_explore
      
    #"Look, its a [res]."
        
    if (res=="bedsidetable"):
        jc "Its my bedside table."
        if Bedroom1_SideTableLocked:
          jc "The drawer is open a crack. Its pretty stiff, I don't think ill be able to open this with these paws."
        else:
          jc "The drawer is already open. Lets look inside."
          if (not inventory.inventory_hand) or (inventory.inventory_hand and (not inventory.inventory_hand[0] == 'LazerPen')):
            jc "Theres a Lazer Pen in here. Clawdia loves to chase this little red dot."
          if (not inventory.inventory_hand and (not Bedroom1_DoorHandleYarn)) or (inventory.inventory_hand and ((not inventory.inventory_hand[0] == 'YarnBall') and (not Bedroom1_DoorHandleYarn))):
            jc "Theres a Ball of Yarn in here. Reminds of that time i tried to crochet a scarf and Clawdia managed to get herself tangled up in it."
          menu:
            "Should i take something?"
            "Take the lazer pen" if (not inventory.inventory_hand) or (inventory.inventory_hand and (not inventory.inventory_hand[0] == 'LazerPen')):
              $inventory.AddItemToHand('LazerPen')
            "Take the yarn ball" if (not inventory.inventory_hand and (not Bedroom1_DoorHandleYarn)) or (inventory.inventory_hand and ((not inventory.inventory_hand[0] == 'YarnBall') and (not Bedroom1_DoorHandleYarn))):
              $inventory.AddItemToHand('YarnBall')
            "Leave them here.":
              if (not inventory.inventory_hand) or ((inventory.inventory_hand) and (not inventory.inventory_hand[0] == 'LazerPen')):
                $inventory.AddItemToRoomInventory('LazerPen', current_room[0])
              if (not inventory.inventory_hand) or ((inventory.inventory_hand) and (not inventory.inventory_hand[0] == 'YarnBall')):
                $inventory.AddItemToRoomInventory('YarnBall', current_room[0])
          jump lbl_bedroom1_explore
    if (res=="books"):
        jc "My books."
    if (res=="door"):
        jc "The door is closed. I'm not sure how I'm supposed to open this as i am now."
    if (res=="yarnhandle"):
      if Bedroom1_DoorLocked:
        if Bedroom1_DoorHandleYarn:
          "Alright, the yarn is on the handle."
          menu:
            "How should i pull it?"
            "Pull the right end":
              jc "OK here goes."
              "..."
              jc "Darn it unraveled and the yarn fell off the handle."
              $Bedroom1_DoorHandleYarn = False
              $inventory.AddItemToHand('YarnBall')
            "Pull the left end":
              jc "OK here goes."
              "..."
              jc "Darn it unraveled and the yarn fell off the handle."
              $Bedroom1_DoorHandleYarn = False
              $inventory.AddItemToHand('YarnBall')
            "Pull both ends":
              jc "OK here goes."
              "..."
              jc "Looks like its holding. Now to gently pull the handle."
              "..."
              jc "Yes! Its open!"
              $Bedroom1_DoorLocked = False
              #jump lbl_chapter1_Escaped
              return #Escape the room
            "Give up":
              pass
      else:
        "The yarn is still on the handle."            
      jump lbl_bedroom1_explore
    if (res=="doorhandle"):
          jc "The door handle. Maybe theres some way i can pull it down to open the door?"
          jc "I can't reach it from the floor."
          $TryReach = True
          if inventory.inventory_hand:
            if inventory.inventory_hand[0] == 'YarnBall':
              $TryReach = False
          if TryReach:
            menu:
              "Try somewhere else?"
              "From the Bed":
                "Its too far away."
              "From the Floor":
                "Its too far away. I could jump up, but i don't think i could grip the handle with these paws."
              "From the Chest of Drawers":
                "Its close, but i just can't quite reach the handle on my own."
              "Give up":
                pass
          
    if (res=="drawers_front"):
        jc "Its my chest of drawers."
        jc "Normally I would push them to have them click open, but theres no way i could produce enough force like this."
    if (res=="drawers_top"):
        jc "Its my chest of drawers."
        jc "Luckily I am as agile it seems as Clawdia was, so jumping up here is no problem at all."
    if (res=="lamp"):
        jc "Its my bedside lamp. I like it because it has a USB port for charging my phone."
        jc "Where is my phone? Did i leave it somewhere?"
    if (res=="mirror"):
        jc "Its a mirror. Theres nothing particularly interesting about it beyond it reflecting what it sees."
        $mirrorjoke = renpy.random.choice(List_MirrorJokes)
        jc "[mirrorjoke]"  
    if (res=="laundrybasket"):
        jc "Its just the basket i use to hold my dirty laundry."
        jc "Its probably more full than it really should be, but hey, its been a long week."
        #Smells?
    if (res=="bed"):
        jc "My warm cozy blanket."
        jc "Clawdia was under this. Or rather i was, well my body. This is confusing."
        jc "How i wish i could just curl up and go back to sleep."
        jc "I mean, if this is a dream that might be the way to wake up from it."
        menu:
          "Sleep?"
          "Time for a cat nap!":
            jc "..."
            jc "..."
            jc "Its not working. I'm not tired at all."
          "Furget it!":
            jc "I don't have time for that. Not to mention after that last sleep i feel like I've enough energy to go all day"
        
    if (res=="candle_bedroom1"):
        jc "A scented candle i got as a present. 'Amaranth and Jasmine' it says. I'm not 100\% sure what an amaranth is, but it smells nice."
        $ShouldPickUp = True
    if (res=="MouseToy"):
        jc "Oh its Clawdias' favourite mouse toy. She is rarely ever seen too far from it."
        "Jessica picks up the toy and notices Clawdia watching her intently."
        jc "Does she think I'm going to steal it?"
        jc "Well I guess to her I'm just another cat playing with her favourite toy."
        "Jessica tries moving around with the toy. Clawdia watches very closely."
        jc "Hmm, maybe I can use this somehow?"
        if not Bedroom1_DoorLocked:
          if not Bedroom1_MouseToyHint:
            cp "..."
            "As Jessica starts to move towards the door, Clawdia starts to follow slowly."
            jc "If I leave with this will she follow me?"
            
            "*If you leave the room while holding the cat toy Clawdia will follow you. You can use this to have Clawdia move to certain rooms when necessary*"
            $Bedroom1_MouseToyHint = True
        $ShouldPickUp = True
    if (res=="Pencil"):
        jc "Ah the trusty pencil. Good for so many things."
        jc "I mean theres writing of course, a fidget spinner and uh, doing that thing where you hold it with your top lip under your nose like a mustache. Basically endless possibilities."
        $ShouldPickUp = True
        
    if (res=="dropItem"):
        $inventory.DropItemFromHand()
        jc "You stay here for a bit Clawdia."
        
    if (res=="callClawdia"):
        if ClawdiaLocation == CurrentRoomName:
            jc "Oh wait, shes already here."
        else:
            jc "I guess she can't hear me."
    
    #In bedsidetable drawer
    #"LazerPen"
    #"YarnBall"
        
    #jc "Look, its a [res]."
    #"Inventory active: [Inventory_active]"
    if inventory.inventory_hand and Inventory_active == 'HeldItem':
      #jc "I'm holding [inventory_hand]"
      if inventory.inventory_hand[0] == 'Pencil':
        if res == 'bedsidetable':
          if Bedroom1_SideTableLocked:
            jc "Maybe i can leverage the pencil to push the drawer on the table to open enough to see inside?"
            "Jessica jammed the pencil halfway into the crack and pulled it backwards, pushing the drawer out further."
            jc "I managed to open it!"
            $Bedroom1_SideTableLocked = False
        else:
          jc "Should i write on it?"
      if 'candle' in inventory.inventory_hand[0]:
        jc "I'm not sure i can use a Candle on that."
      if inventory.inventory_hand[0] == 'MouseToy':
        if res == 'bedsidetable' or res == 'bed' or res == 'laundrybasket':
          jc "I don't think Clawdia will approve if i hide her favorite toy like that."
        else:  
          jc "I'm not sure that the toy will do anything with that."
      if inventory.inventory_hand[0] == 'LazerPen':
        jc "I'm not sure that using the Lazer Pen on that will help."
      if inventory.inventory_hand[0] == 'YarnBall':
        if not Bedroom1_DoorYarnHint:
          if res == 'doorhandle':
            jc "Maybe i can use the Yarn to pull the handle?"
            jc "If i got it wrapped around and got i good enough grip i think i could pull the handle."
            jc "Getting it wrapped around is the problem."
            jc "I don't think i can reach it from the floor."
            $Bedroom1_DoorYarnHint = True
          else:  
            jc "I'm not sure that will help."
        else:  
          if res == 'doorhandle':
            jc "I don't think i can reach it from the floor."
          if res == 'bed':
            jc "I don't think i can reach it from the bed."
          if res == 'drawers_top':
            jc "Actually i think i should be able to throw the yarn ball around the door handle from here."
            jc "..."
            jc "There we go. If i pull that correctly it should open."
            jc "I hope"
            $Bedroom1_DoorHandleYarn = True
            $inventory.EmptyHand()
    
    #"[Bedroom1_CollectionsActive] and [ShouldPickUp]"
    if not Inventory_active == 'HeldItem':
      if Bedroom1_CollectionsActive and ShouldPickUp:
        if inventory.IsItemCollectable(res):
          menu:
            "Take it?"
            "Yes":
              $inventory.AddItemToHand(res)
            "No":
              $inventory.AddItemToRoomInventory(res, current_room[0])
            #"Leave":
            #  jump lbl_exploration_end
        else:
          jc "I can't take that."
    
    if inventory.inventory_hand:
      if not SeenTutorial_ItemUse:
        jc "Looks like I'm able to pick things up."
        jc "I'm only able to hold one thing at a time, since i have to carry them around in my mouth. So if i pick up anything new ill have to leave the old item behind."
        "*To use the item, click the large button with the item in it, and then click where you want to use it.*"
        $SeenTutorial_ItemUse = True
        $Inventory_HeldItem_unlocked = True
            
    jump lbl_bedroom1_explore

  
#-----------------------------------------------------------------------
    
label lbl_bedroom1_intro_blanket_mirror:
    
    call ShowBedroom1()
    if Bedroom1_ClawdiaAwake:
      show item blanket
    else:
      show item blanket bump
    if Bedroom1_Intro_MirrorUsed:
      show jessicat angry at left
    if Bedroom1_Intro_BlanketUsed:
      show jessicaperson neutral:
        yalign -0.5
        xalign 0.7
    c "I need to find something that will help me figure out what has happened to me."
    
    call screen Exploration_Bedroom1
    $res = _return
    $ShouldPickUp = False
    
    $itemPicked = ""
    #"room [res]"
    if (res=="bed_bump" and (not Bedroom1_Intro_BlanketUsed)): 
      jc "This bump..."
      jc "Is there something under here?"
      $itemPicked = "bed_bump"
    else:
      if (res=="mirror" and (not Bedroom1_Intro_MirrorUsed)): 
        jc "Of course, the mirror!"
        $itemPicked = "mirror"
      else:
        jc "I don't think this is going to help right now."
    
    if itemPicked == "":
      jump lbl_bedroom1_intro_blanket_mirror
    else:
      return itemPicked
    
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------

label lbl_exploration_end:
  #"All done"
  return
  
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
screen Exploration_Bedroom2:
    add 'bg bedroom2'
    $roomName = "bedroom2"  
    $inventory.SetCurrentRoom(roomName)
    
    use FixedItem(roomName, "table_top", 0,0)
    use FixedItem(roomName, "table_drawers", 0,0)
    use FixedItem(roomName, "stool", 0,0)
    use FixedItem(roomName, "bed", 0,0)
    use FixedItem(roomName, "curtains", 0,0)
    if not Bedroom2_FanTurned:
      use FixedItem(roomName, "fan_forward", 0,0)
    else:
      use FixedItem(roomName, "fan_turn", 0,0)
    use FixedItem(roomName, "mirror", 0,0)
    
    use FixedItem(roomName, "journal", 0,0)
    
    
    #use ClickableItem("Incense", 1200, 450)
    #use ClickableItem("Candle", 1200, 450)
    if inventory.inventory_hand:
      if not inventory.inventory_hand[0] == 'VPen':
        use FixedItem(roomName,"VPen", 0, 0)
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == roomName:
          use FixedItem(roomName,"MouseToy", 0, 0)
    else:
      use FixedItem(roomName,"VPen", 0, 0)
      if ClawdiaLocation == roomName:
        use FixedItem(roomName,"MouseToy", 0, 0)
        
    if NightVision_active:
      if Bedroom2_LightsOff:
        add "images/backgrounds/NightVision.png" 
      else:
        add "images/backgrounds/NightVision_Bright.png" 
    else:
      if Bedroom2_LightsOff:
        add "images/backgrounds/Dark.png"
    
    use Exploration_Navigation 
    use hand_inventory
    use room_inventory(roomName)
    
#-----------------------------------------------------------------------
#---
label ShowBedroom2():
    $CurrentRoomName = "bedroom2"

    #"Show bedroom 2"
    scene bg bedroom2
      
    if not Bedroom2_FanTurned:
      show item_bedroom2_fan_forward
    else:
      show item_bedroom2_fan_turn
      
    if inventory.inventory_hand:
      if not inventory.inventory_hand[0] == 'VPen':
        show item_bedroom2_vpen
      if not inventory.inventory_hand[0] == 'MouseToy':
        show item_bedroom2_mousetoy
    else:
        #"Show all items"
        show item_bedroom2_vpen
        show item_bedroom2_mousetoy
        
    if inventory.inventory_hand:
      if inventory.inventory_hand[0] == 'MouseToy':
        $ClawdiaLocation = CurrentRoomName
        
    if NightVision_active:
      if Bedroom1_LightsOff:
        show roomeffect nightvision
      else:
        show roomeffect nightvision_bright
    else:
      if Bedroom1_LightsOff:
        show roomeffect dark
        
    return
    
label ShowBedroom2WithChars:
    $CurrentRoomName = "bedroom2"
    call ShowBedroom2
              
    if ClawdiaLocation == CurrentRoomName:
      show jessicaperson neutral:
        yalign -0.5
        xalign 0.7
        
    show jessicat happy at left
    return
#---
label lbl_bedroom2:
     
    #scene bg bedroom2
    call ShowBedroom2WithChars
    jc "Its Veronicas' Bedroom"
    jc "Lets see what else we can find here..."
    
label lbl_bedroom2_explore:
    $roomName = "bedroom2"
    $inventory.SetCurrentRoom(roomName)
    call screen Exploration_Bedroom2
    $res = _return
    $ShouldPickUp = False
    call ShowBedroom2WithChars
    
    if res[0] == 'Move':
      $labelname = res[1]
      if config.developer:
        jc "Ok lets go to [labelname]"
      jump expression labelname
      
    if Bedroom2_LightsOff:
      if not NightVision_active:
        "I can't see what that is right now."
        jump lbl_bedroom2_explore
      
    #"Look, its a [res]."
    
    if (res=="table_top"):
        jc "Its a small table. Looks like theres a few things on it."
        if (inventory.inventory_hand) and (inventory.inventory_hand[0] == 'VPen'):
          if Bedroom2_JournalRead:
            jc "There's a small desk fan on the table and Veronicas Journal is here too."
          else:
            jc "There's an open book and a small desk fan."
        else:
          if Bedroom2_JournalRead:
            jc "There's a small desk fan and a fancy pen on the table and Veronicas Journal is here too."
          else:
            jc "There's an open book, a fancy pen and a small desk fan."          
    if (res=="table_drawers"):
        jc "The drawers for the table."
        if Boilerroom_Bedroom2CandlePlaced or (inventory.inventory_hand and (not inventory.inventory_hand[0] == 'candle_bedroom2')):
            jc "There doesn't seem to be anything interesting in them."
        else:
            jc "Oh theres a candle in here."
            if baconCandleStorySeen == False:
                jc "I think this is the one i got for Veronica for her birthday. Its Bacon scented, and honestly it smells delicious."
                jc "We had this running joke about her loving the smell of bacon, but honestly this one is too strong to actually use."
                jc "Veronica lit it for 20 minutes in the living room when she got it, and the room smelled like bacon for a week."
            menu:
              "Should i take it?"
              "Take the candle.":
                $inventory.AddItemToHand('candle_bedroom2')
              "Leave them here.":
                  $inventory.AddItemToRoomInventory('candle_bedroom2', current_room[0])
            
        
    if (res=="stool"):
        jc "It's a small stool."
    if (res=="bed"):
        jc "Veronicas Bed. It looks pretty comfortable."
        jc "I should stay off it though. If she catches Clawdia on her bed again she'll flip out."
        jc "Again."
    if (res=="curtains"):
        jc "Some blackout curtains. When closed they should leave the room in pitch blackness."
        jc "Or at least thats what the guy in the store said. I don't know how good they actually are."
        if Bedroom2_FanTurned:
          "The curtain wafted in the breeze created by the fan."
          if not Boilerroom_IncensePlaced and (not inventory.inventory_hand) or (inventory.inventory_hand and (not inventory.inventory_hand[0] == 'Incense')):
              jc "Is there something behind the curtain here?"
              if not Office_MagicInstructionsFound:
                jc "Oh its just some sticks. They look a little burnt on the ends."
              else:
                jc "Is this incense? It definitely smells funny."
                jc "I wonder if i can use this?"            
                menu:
                  "Should i take it?"
                  "Take the incense.":
                    $inventory.AddItemToHand('Incense')
                  "Leave them here.":
                      $inventory.AddItemToRoomInventory('Incense', current_room[0])
    if (res=="fan_forward") or (res=="fan_turn"):
        jc "This must be the fan she was talking about."
        jc "Looks like i can turn it on and off or turn it."
        menu:
          "Turn it on.":
            "A cool breeze blows from the fan."
            jc "This is pretty refreshing actually."
          "Turn it off.":
            jc "Guess I'll turn it off." 
            jc "I miss the breeze already."            
          "Turn it around.":          
            if Bedroom2_FanTurned:
              jc "I'll have it face forwards then."
              $Bedroom2_FanTurned = False
            else:
              jc "I'll have it face to the side then."
              $Bedroom2_FanTurned = True
            
    if (res=="mirror"):
        jc "A small mirror mounted above this small table. It doubles as a vanity now i suppose."
        $mirrorjoke = renpy.random.choice(List_MirrorJokes)
        jc "[mirrorjoke]"  
    if (res=="journal"):
        jc "Hmm... Its Veronicas Journal. Maybe theres something in here that can help me."
        return #lbl_chapter2_Journal
    if (res=="VPen"):
        jc "Its Veronicas pen. It's pretty fancy actually."
        "I guess if I was gonna spend a lot of time writing I would want to use a good pen too."
        $ShouldPickUp = True        
    #if (res=="Incense"):
    #    jc "..."
    #    $ShouldPickUp = True
    #if (res=="candle_bedroom2"):
    #    jc "..."
    #    $ShouldPickUp = True
    if (res=="MouseToy"):
        jc "Clawdias' favourite mouse toy. She is rarely ever seen too far from it."
        $ShouldPickUp = True
        
    if (res=="dropItem"):
        $inventory.DropItemFromHand()
        jc "You stay here for a bit Clawdia."
        
    if (res=="callClawdia"):
        if ClawdiaLocation == CurrentRoomName:
            jc "Oh wait, shes already here."
        else:
            jc "I guess she can't hear me."
        
        
    if ShouldPickUp:
      if inventory.IsItemCollectable(res):
        menu:
          "Take it?"
          "Yes":
            $inventory.AddItemToHand(res)
          "No":
            $inventory.AddItemToRoomInventory(res, current_room[0])
      else:
        jc "I can't take that."
    
    #menu:
    #  "Look again":
    #    pass
    #  "Leave":
    #    return
    jump lbl_bedroom2_explore
    
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
screen Exploration_Bathroom1:
    add 'bg bathroom1'   
    $roomName = "bathroom1"  
    $inventory.SetCurrentRoom(roomName)
    #text "current_room [current_room]"
    
    #use FixedItem(roomName, "toilet", 0,0)
    use FixedItem(roomName, "showercurtain", 0,0)
    #use FixedItem(roomName, "bathtub", 0,0)
    use FixedItem(roomName, "sink", 0,0)
    use FixedItem(roomName, "mirror", 0,0)
    use FixedItem(roomName, "cupboard", 0,0)
    #use FixedItem(roomName, "catlitter", 0,0)
    
    #In cupboard
    #use ClickableItem("ToiletBrush", 1200, 450)
    #use ClickableItem("Plunger", 1200, 450)
    
    #use ClickableItem("Makeup", 1200, 450)
    if inventory.inventory_hand:
      if not Boilerroom_TokenPlaced_silver and not inventory.inventory_hand[0] == 'token_silver':
        use FixedItem(roomName, "token_silver", 0,0)
      if not Boilerroom_HairbrushPlaced_Jessica and not inventory.inventory_hand[0] == 'JessicaHairbrush':
        use FixedItem(roomName, "JessicaHairbrush", 0,0)
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == roomName:
          use FixedItem(roomName,"MouseToy", 0, 0)
    else:
      if not Boilerroom_TokenPlaced_silver:
        use FixedItem(roomName, "token_silver", 0,0)
      if not Boilerroom_HairbrushPlaced_Jessica:
        use FixedItem(roomName, "JessicaHairbrush", 0,0)
      if ClawdiaLocation == roomName:
        use FixedItem(roomName,"MouseToy", 0, 0)
    
    if NightVision_active:
      if Bathroom1_LightsOff:
        add "images/backgrounds/NightVision.png" 
      else:
        add "images/backgrounds/NightVision_Bright.png" 
    else:
      if Bathroom1_LightsOff:
        add "images/backgrounds/Dark.png"
    
    use Exploration_Navigation 
    use hand_inventory
    use room_inventory(roomName)
    
#-----------------------------------------------------------------------
#---
label ShowBathroom1():
    $CurrentRoomName = "bathroom1"

    #"Show Bathroom1"
    scene bg bathroom1
      
    if inventory.inventory_hand:
      if not Boilerroom_TokenPlaced_silver and not inventory.inventory_hand[0] == 'token_silver':
        show item_bathroom1_token_silver
      if not Boilerroom_HairbrushPlaced_Jessica and not inventory.inventory_hand[0] == 'JessicaHairbrush':
        show item_bathroom1_JessicaHairbrush
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == CurrentRoomName:
            show item_bathroom1_mousetoy
    else:
        #"Show all items"
        if not Boilerroom_TokenPlaced_silver:
          show item_bathroom1_token_silver
        if not Boilerroom_HairbrushPlaced_Jessica:
          show item_bathroom1_JessicaHairbrush
        if ClawdiaLocation == CurrentRoomName:
          show item_bathroom1_mousetoy
    
    if inventory.inventory_hand:
      if inventory.inventory_hand[0] == 'MouseToy':
        $ClawdiaLocation = CurrentRoomName
        
    if NightVision_active:
      if Bathroom1_LightsOff:
        show roomeffect nightvision
      else:
        show roomeffect nightvision_bright
    else:
      if Bathroom1_LightsOff:
        show roomeffect dark
        
    return
    
label ShowBathroom1WithChars:
    $CurrentRoomName = "bathroom1"
    call ShowBathroom1
              
    if ClawdiaLocation == CurrentRoomName:
      show jessicaperson neutral:
        yalign -0.5
        xalign 0.7
        
    show jessicat happy at left
    return
#---
label lbl_bathroom1:
     
    #scene bg bathroom1
    #if NightVision_active:
    #  show roomeffect nightvision
    #else:
    #  if Bathroom1_LightsOff:
    #    show roomeffect dark
    play music music_SlowlyCreeping
    call ShowBathroom1WithChars
    jc "Its the upstairs bathroom"
    if (Bathroom1_LightsOff) and (not NightVision_active):
      jc "Its pretty dark in here."
    else:
      jc "Lets see what else we can find here..."
    
label lbl_bathroom1_explore:
    $roomName = "bathroom1"
    $inventory.SetCurrentRoom(roomName)
    #"Current room is [current_room]"
    call screen Exploration_Bathroom1
    $res = _return
    $ShouldPickUp = False
    call ShowBathroom1WithChars
        
    if res[0] == 'Move':
      $labelname = res[1]
      if config.developer:
        jc "Ok lets go to [labelname]"
      jump expression labelname    
    
    
    if Bathroom1_LightsOff:
      if not NightVision_active:
        "I can't see what that is right now."
        if not Inventory_CatEyes_unlocked:
          jc "Aren't cats supposed to have good night vision?"
          jc "Maybe if i try to focus on it i'll be able to see."
          $Inventory_CatEyes_unlocked = True
          "*Now you can use the Cats Eyes ability to enable your night vision*"
        jump lbl_bathroom1_explore
          
    
    #"Look, its a [res]."
    #if (res=="toilet"):
    #    jc "..."
    if (res=="showercurtain"):
        jc "Behind this curtain is a small bath and probably the most temperamental shower I've ever had the displeasure of using."
        jc "If you are ever thinking 'I'm not sure if I want to be scalded or frozen today' then this is the shower for you."
        jc "On the bright side, I'm probably world record holder for speed showers now."
    #if (res=="bathtub"):
    #    jc "..."
    if (res=="sink"):
        jc "The bathroom sink. It doesn't look like theres anything in it at the moment."
    if (res=="mirror"):
        jc "A large bathroom mirror. I makes this small bathroom look a lot bigger."
        $mirrorjoke = renpy.random.choice(List_MirrorJokes)
        jc "[mirrorjoke]"  
    if (res=="cupboard"):
        jc "We keep the toilet paper and other bits and bobs under the sink here."
        
        jc "Lets look inside."
        if (not inventory.inventory_hand) or ((inventory.inventory_hand) and (not inventory.inventory_hand[0] == 'ToiletBrush')):
          jc "The toilet brush. Used for scrubbing the bowl."
          jc "I guess i could take it, it might be useful to get things out of reach, but I'd feel bad for Clawdia having to carry it around in her mouth."
        if (not inventory.inventory_hand) or ((inventory.inventory_hand) and (not inventory.inventory_hand[0] == 'Plunger')):
          jc "Its a small plunger."
          jc "Mostly used for unblocking the sink, they can back up at times. We should get someone to look into that someday."
        menu:
          "Should i take something?"
          "Take the Toilet Brush" if (not inventory.inventory_hand) or ((inventory.inventory_hand) and (not inventory.inventory_hand[0] == 'ToiletBrush')):
            $inventory.AddItemToHand('ToiletBrush')
          "Take the Plunger" if (not inventory.inventory_hand) or ((inventory.inventory_hand) and (not inventory.inventory_hand[0] == 'Plunger')):
            $inventory.AddItemToHand('Plunger')
          "Leave them here.":
            if (not inventory.inventory_hand) or ((inventory.inventory_hand) and (not inventory.inventory_hand[0] == 'ToiletBrush')):
              $inventory.AddItemToRoomInventory('ToiletBrush', current_room[0])
            if (not inventory.inventory_hand) or ((inventory.inventory_hand) and (not inventory.inventory_hand[0] == 'Plunger')):
              $inventory.AddItemToRoomInventory('Plunger', current_room[0])
    #if (res=="catlitter"):
    #    jc "..."
    #if (res=="ToiletBrush"):
    #    $ShouldPickUp = True
    #if (res=="Plunger"):        
    #    $ShouldPickUp = True
    if (res=="JessicaHairbrush"):
        jc "Oh its my hairbrush."
        jc "Its covered in old hair that gets pulled out when I'm brushing. I really should clean it off more often."
        $ShouldPickUp = True
    if (res=="token_silver"):
        jc "It looks like a strange token, made of silver perhaps?"
        $ShouldPickUp = True
    #if (res=="Makeup"):
    #    jc "..."
    #    $ShouldPickUp = True
    if (res=="MouseToy"):
        jc "Clawdias' favourite mouse toy. She is rarely ever seen too far from it."
        $ShouldPickUp = True
        
    if (res=="dropItem"):
        $inventory.DropItemFromHand()
        jc "You stay here for a bit Clawdia."
        
    if (res=="callClawdia"):
        if ClawdiaLocation == CurrentRoomName:
            jc "Oh wait, shes already here."
        else:
            jc "I guess she can't hear me."
        
        
    if ShouldPickUp:
      if inventory.IsItemCollectable(res):
        menu:
          "Take it?"
          "Yes":
            $inventory.AddItemToHand(res)
          "No":
            $inventory.AddItemToRoomInventory(res, current_room[0])
      else:
        jc "I can't take that."
        
    jump lbl_bathroom1_explore
    
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
screen Exploration_Hallway:
    add 'bg hallway'   
    $roomName = "hallway" 
    $inventory.SetCurrentRoom(roomName)
    
    use FixedItem(roomName, "door_bedroom1", 0,0)
    use FixedItem(roomName, "door_bedroom2", 0,0)
    use FixedItem(roomName, "door_bathroom1", 0,0)
    use FixedItem(roomName, "stairs_livingroom1", 0,0)
    #use FixedItem(roomName, "mirror", 0,0)
    use FixedItem(roomName, "cupboards", 0,0)
    if Hallway_BroomMoved:
      use FixedItem(roomName, "broom_pushed", 0,0)
    else:
      use FixedItem(roomName, "broom_normal", 0,0)
    #use ClickableItem("Candle", 1200, 450)
    
    if inventory.inventory_hand:
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == roomName:
          use FixedItem(roomName,"MouseToy", 0, 0)
    else:
      if ClawdiaLocation == roomName:
        use FixedItem(roomName,"MouseToy", 0, 0)
    
    if NightVision_active:
      if Hallway_LightsOff:
        add "images/backgrounds/NightVision.png" 
      else:
        add "images/backgrounds/NightVision_Bright.png" 
    else:
      if Hallway_LightsOff:
        add "images/backgrounds/Dark.png"
    
    use Exploration_Navigation 
    use hand_inventory
    use room_inventory(roomName)
    
#-----------------------------------------------------------------------

#---
label ShowHallway():
    $CurrentRoomName = "hallway"

    #"Show Hallway"
    scene bg hallway
      
    if inventory.inventory_hand:
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == CurrentRoomName:
            show item_hallway_mousetoy
    else:
      #"Show all items"
      if ClawdiaLocation == CurrentRoomName:
        show item_hallway_mousetoy
        
    if Hallway_BroomMoved:
      show item_hallway_broom_pushed
    else:
      show item_hallway_broom_normal
    
    if inventory.inventory_hand:
      if inventory.inventory_hand[0] == 'MouseToy':
        $ClawdiaLocation = CurrentRoomName
        
    if NightVision_active:
      if Hallway_LightsOff:
        show roomeffect nightvision
      else:
        show roomeffect nightvision_bright
    else:
      if Hallway_LightsOff:
        show roomeffect dark
        
    return
    
label ShowHallwayWithChars:
    $CurrentRoomName = "hallway"
    call ShowHallway
              
    if ClawdiaLocation == CurrentRoomName:
      show jessicaperson neutral:
        yalign -0.5
        xalign 0.7
        
    show jessicat happy at left
    return
#---
label lbl_hallway:
     
    #scene bg hallway
    #if NightVision_active:
    #  show roomeffect nightvision
    #else:
    #  if Bedroom1_LightsOff:
    #    show roomeffect dark
    play music music_LoungeLizard
    call ShowHallwayWithChars
    jc "Its the hallway outside my room."
    jc "Lets see what else we can find here..."
    
label lbl_hallway_explore:
    call screen Exploration_Hallway
    $res = _return
    $ShouldPickUp = False
    call ShowHallwayWithChars
    
    if res[0] == 'Move':
      # --- DEMO END
      #if res[1] == 'lbl_livingroom1':
      #  jump DEMO_END
      $labelname = res[1]
      if config.developer:
        jc "Ok lets go to [labelname]"
      jump expression labelname
      
    if Hallway_LightsOff:
      if not NightVision_active:
        "I can't see what that is right now."
        jump lbl_hallway_explore
      
    
    #"Look, its a [res]."
    if (res=="door_bedroom1"):
        jc "This leads back to my room."
    if (res=="door_bedroom2"):
        jc "Its the door to Veronicas room."
        if not Hallway_Bedroom2DoorUnlocked:
          jc "She normally keeps it locked. Always complaining that Clawdia keeps getting into her room and getting cat hair everywhere."
          jc "Which i guess is a reasonable complaint given her allergies."
          if (not inventory.inventory_hand) or ((inventory.inventory_hand) and (inventory.inventory_hand[0] == 'VeronicasKeys')):
            jc "Maybe I could unlock it with these keys?"
            if not Hallway_BroomMoved:
              jc "If only i could reach the lock. Is there something i could stand on?"
            else:
              if Inventory_active == 'HeldItem':
                "Jessica carefully climbed up the broom and using her mouth put the key in the lock and turned it."
                "It turned a little quicker than she was expecting and she tumbled to the floor as she heard a 'click'."
                $Hallway_Bedroom2DoorUnlocked = True
                jc "Ahh!"
                "Luckly she landed on her feet unharmed."
                jc "Gotta love that muscle memory."
        else:
          jc "It's already unlocked."
    if (res=="door_bathroom1"):
        jc "This door leads to the bathroom."
        jc "Looks like it's open a little so i should have no problems getting inside."
    if (res=="stairs_livingroom1"):
        jc "The stairs here lead downstairs to the living room."
    #if (res=="mirror"):
    #    jc "..."
    if (res=="cupboards"):
        jc "This is the cupboards where we keep the towels and spare bed linen."
        jc "They are pretty stiff though so i don't see me getting them open while I'm like this."
    if (res=="broom_normal") :
        jc "Its just a floor brush."
        if not Hallway_BroomMoved:
          jc "I could probably push it over."
          menu:
            "Push it over?"
            "Yes":
              "Jessica pushes the broom down and it falls towards the bedroom door."
              $Hallway_BroomMoved = True
            "No":
              pass
    if (res=="broom_pushed") :
        jc "Its just a floor brush."
        if not Hallway_Bedroom2DoorUnlocked:
          jc "I could probably walk up this brush shaft to reach the lock if i needed to."
    if (res=="MouseToy"):
        jc "Clawdias' favourite mouse toy. She is rarely ever seen too far from it."
        $ShouldPickUp = True
        
    if (res=="dropItem"):
        $inventory.DropItemFromHand()
        jc "You stay here for a bit Clawdia."
        
    if (res=="callClawdia"):
        if ClawdiaLocation == CurrentRoomName:
            jc "Oh wait, shes already here."
        else:
            if "livingroom" in ClawdiaLocation:
                "Clawdia comes strolling over to see whats going on. She stretches slowly once she arrives."
                show jessicaperson happy:
                    yalign -0.5
                    xalign 0.7
                jc "I guess even in my body you're never in a hurry to go anywhere."
                $ClawdiaLocation = CurrentRoomName            
            else:
                jc "I guess she can't hear me."
        
    if ShouldPickUp:
      if inventory.IsItemCollectable(res):
        menu:
          "Take it?"
          "Yes":
            $inventory.AddItemToHand(res)
          "No":
            $inventory.AddItemToRoomInventory(res, current_room[0])
      else:
        jc "I can't take that."
        
    jump lbl_hallway_explore
    
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
screen Exploration_Livingroom1:
    add 'bg livingroom1'  
    $roomName = "livingroom1"  
    $inventory.SetCurrentRoom(roomName)
    
    use FixedItem(roomName, "stairs_hallway", 0,0)
    use FixedItem(roomName, "Sofa", 0,0)
    use FixedItem(roomName, "sidetable", 0,0)
    #use FixedItem(roomName, "sofa_cushion1", 0,0)
    #use FixedItem(roomName, "sofa_cushion2", 0,0)
    #use FixedItem(roomName, "sofa_cushion3", 0,0)
    use FixedItem(roomName, "diningtable", 0,0)
    use FixedItem(roomName, "photos", 0,0)
    use FixedItem(roomName, "bookshelf", 0,0)
    
    #use ClickableItem("Phone", 350, 400)
    #use ClickableItem("ClawdiaBrush", 560, 310)
    #use ClickableItem("Candle", 500, 360)
    
    if inventory.inventory_hand:
      if not inventory.inventory_hand[0] == 'Phone':
        use FixedItem(roomName, "Phone", 0,0)
      if not Boilerroom_HairbrushPlaced_Clawdia and not inventory.inventory_hand[0] == 'ClawdiaHairbrush':
        use FixedItem(roomName, "ClawdiaHairbrush", 0,0)
      if not Boilerroom_Livingroom1CandlePlaced:
        if not inventory.inventory_hand[0] == 'candle_livingroom1':
            use FixedItem(roomName, "candle_livingroom1", 0,0)
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == roomName:
          use FixedItem(roomName,"MouseToy", 0, 0)
    else:
      use FixedItem(roomName, "Phone", 0,0)
      if not Boilerroom_HairbrushPlaced_Clawdia:
        use FixedItem(roomName, "ClawdiaHairbrush", 0,0)
      if not Boilerroom_Livingroom1CandlePlaced:
        use FixedItem(roomName, "candle_livingroom1", 0,0)
      if ClawdiaLocation == roomName:
        use FixedItem(roomName,"MouseToy", 0, 0)
      
    
    #behind cushions
    #use ClickableItem("LooseChange", 1200, 450)
    #use ClickableItem("Buttons", 1200, 450)
    #use ClickableItem("Pen", 1200, 450)
    
    #under sofa
    #use ClickableItem("token_bronze", 1200, 450)
    
    if NightVision_active:
      if Livingroom1_LightsOff:
        add "images/backgrounds/NightVision.png" 
      else:
        add "images/backgrounds/NightVision_Bright.png" 
    else:
      if Livingroom1_LightsOff:
        add "images/backgrounds/Dark.png"
    
    use Exploration_Navigation 
    use hand_inventory
    use room_inventory(roomName)
    
#-----------------------------------------------------------------------
#---
label ShowLivingroom1():
    $CurrentRoomName = "livingroom1"

    #"Show Livingroom1"
    scene bg livingroom1
      
    if inventory.inventory_hand:
      if not inventory.inventory_hand[0] == 'Phone':
        show item_livingroom1_Phone
      if not Boilerroom_HairbrushPlaced_Clawdia and not inventory.inventory_hand[0] == 'ClawdiaHairbrush':
        show item_livingroom1_ClawdiaBrush
      if not Boilerroom_Livingroom1CandlePlaced:
          if not inventory.inventory_hand[0] == 'candle_livingroom1':
            show item_livingroom1_Candle
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == CurrentRoomName:
            show item_livingroom1_mousetoy
    else:
      #"Show all items"
      show item_livingroom1_Phone
      if not Boilerroom_HairbrushPlaced_Clawdia:
        show item_livingroom1_ClawdiaBrush
      if not Boilerroom_Livingroom1CandlePlaced:
        show item_livingroom1_Candle
      if ClawdiaLocation == CurrentRoomName:
        show item_livingroom1_mousetoy
    
    if inventory.inventory_hand:
      if inventory.inventory_hand[0] == 'MouseToy':
        $ClawdiaLocation = CurrentRoomName
        
    if NightVision_active:
      if Livingroom1_LightsOff:
        show roomeffect nightvision
      else:
        show roomeffect nightvision_bright
    else:
      if Livingroom1_LightsOff:
        show roomeffect dark
        
    return
    
label ShowLivingroom1WithChars:
    $CurrentRoomName = "livingroom1"
    call ShowLivingroom1
              
    if ClawdiaLocation == CurrentRoomName:
      show jessicaperson neutral:
        yalign -0.5
        xalign 0.7
    "ClawdiaLocation = [ClawdiaLocation] || CurrentRoomName = [CurrentRoomName]"  
        
    show jessicat happy at left
    return
#---
label lbl_livingroom1:
     
    #scene bg livingroom1
    #if NightVision_active:
    #  show roomeffect nightvision
    #else:
    #  if Bedroom1_LightsOff:
    #    show roomeffect dark
    call ShowLivingroom1WithChars
    jc "Its the Living room"
    jc "Lets see what else we can find here..."
    
label lbl_livingroom1_explore:
    call screen Exploration_Livingroom1
    $res = _return
    $ShouldPickUp = False
    call ShowLivingroom1WithChars
    
    if res[0] == 'Move':
      $labelname = res[1]
      if config.developer:
        jc "Ok lets go to [labelname]"
      jump expression labelname
      
    if Livingroom1_LightsOff:
      if not NightVision_active:
        "I can't see what that is right now."
        jump lbl_livingroom1_explore
      
    
    #"Look, its a [res]."
        
    if (res=="stairs_hallway"):
        jc "These lead back upstairs."
    if (res=="Sofa"):
        jc "Its a sofa."
        jc "At a glance it looks pretty tidy, if a little stiff." 
        jc "I, however, know better, if theres one thing I've learned about this black hole in sofa form, its that things have a habit of turning up in and around it."
        menu:
          "Take a closer look?"
          "Check the Left Cushion":
            jc "Oh look, some loose change."
            jc "I'm not sure why I would need these right now though."
          "Check the Center Cushion":
            jc "Oh look, some loose buttons."
            jc "I'm not sure why I would need these right now though."
          "Check the Right Cushion":
            jc "My favourite pen! That's where it went."
            menu:
              "Take it?"
              "Yes":
                $inventory.AddItemToHand('SofaPen')
              "No":
                $inventory.AddItemToRoomInventory('SofaPen', current_room[0])
          "Check underneath":
            if not Boilerroom_TokenPlaced_bronze and (inventory.inventory_hand) and not inventory.inventory_hand[0] == 'token_bronze':
                jc "I can see something faintly shining under there."
                jc "The space isn't big enough to fit my whole body under but i could try to reach something."
                "..."
                if (inventory.inventory_hand) and (inventory.inventory_hand[0] == 'Spoon'):
                  jc "If i use the spoon i can reach a little further in."
                  "..."
                  jc "I can't seem to reach anything."
                if (inventory.inventory_hand) and (inventory.inventory_hand[0] == 'ToiletBrush'):
                  jc "If i use the toilet brush i can reach further in."
                  "..."
                  jc "I think i got something."
                  "It looks like a strange coin, made of bronze or something."
                  menu:
                    "Take it?"
                    "Yes":
                      $inventory.AddItemToHand('token_bronze')
                    "No":
                      $inventory.AddItemToRoomInventory('token_bronze', current_room[0])
            else:
                jc "I can't see anything else under there."
            
            
    #if (res=="sofa_cushion1"):
    #    jc "Its the left cushion"
    #if (res=="sofa_cushion2"):
    #    jc "..."
    #if (res=="sofa_cushion3"):
    #    jc "..."
    if (res=="sidetable"):
        jc "..."
    if (res=="diningtable"):
        jc "Its the dining table."
        jc "Its a little too big for the room so we have to push it up against the wall."
        jc "I got it for free from my mother though so i cant really complain."
    if (res=="photos"):
        jc "Just various photos of mine and Veronica families."
        jc "...and a few obligatory snaps of Clawdia of course."
    if (res=="Phone"):
        if Livingroom1_PhoneCallHappened:
          jc "Its my phone. Its not much use to me when I'm stuck like this."
          menu:
            "Should i check the texts again?"
            "Check the text from Veronica":              
              "Jessica fumbled around with the phone to select Veronicas text to see what she had sent."
              
              v "Hey Jessica, I know you're probably still sleeping, but i forgot to get the fan out of my room for you before i left."
              v "Stayed up late working on an experiment and I overslept, so i was in a rush. But if you need into my room, the keys are in the bowl on top of the fridge."
              v "PLEASE lock the door again after you leave. I don't want your cat in my room again. You know how my alergies are."
              v "OH! And (if it wasn't just you messing with me), then your cat somehow answered the phone and was trying to talk to me."
              v "Was so cute, OMG! I'll be done around 6pm so if you give me a call we can catch up."
              
              jc "Doesn't seem like shes sent anything else"
              
            "Do something else":
              "After fumbling around on the phone, Jessica manges to open the camera app."
              "Click"
              jc "Whoops, didn't mean to do that."
              ". . ."
              jc "Actually, that picture is not too bad."
              jc "Let me see if i can take a good one to use as my wallpaper, its impossible to get Clawdia to sit for a photo unless she is asleep."
              ". . ."
              "After a handful of photos were taken, Jessica realized she was wasting time."
              jc "Ok ok, i have more important things to worry about."
              jc ". . . After i take this last one that makes it look like Clawdia is taking a selfie, because it'll be so cute."
            "Nevermind":
              pass
        else:
          return #lbl_chapter2_Phonecall
        #$ShouldPickUp = True
    if (res=="ClawdiaHairbrush"):
        jc "Oh its Clawdias' brush."
        if not Office_MagicInstructionsFound:
          jc "I need to remember to brush her coat if i ever get out of this body. I'm feeling kinda fuzzy at the moment."
        else:
          jc "I wonder if i could use this?"
        $ShouldPickUp = True
    if (res=="candle_livingroom1"):
        jc "Its a simple candle."
        jc "I'm not entirely sure i know what 'Amber and Vanilla Blossom' is, but boy does it smell good."
        $ShouldPickUp = True
    if (res=="MouseToy"):
        jc "Clawdias' favourite mouse toy. She is rarely ever seen too far from it."
        $ShouldPickUp = True
        
    if (res=="dropItem"):
        $inventory.DropItemFromHand()
        jc "You stay here for a bit Clawdia."
        
    if (res=="callClawdia"):
        if ClawdiaLocation == CurrentRoomName:
            jc "Oh wait, shes already here."
        else:
            if "livingroom" in ClawdiaLocation or "kitchen" in ClawdiaLocation or "hallway" in ClawdiaLocation:
                "Clawdia comes strolling over to see whats going on. She stretches slowly once she arrives."
                show jessicaperson happy:
                    yalign -0.5
                    xalign 0.7
                jc "I guess even in my body you're never in a hurry to go anywhere."
                $ClawdiaLocation = CurrentRoomName            
            else:
                jc "I guess she can't hear me."
        
    if ShouldPickUp:
      if inventory.IsItemCollectable(res):
        menu:
          "Take it?"
          "Yes":
            $inventory.AddItemToHand(res)
          "No":
            $inventory.AddItemToRoomInventory(res, current_room[0])
      else:
        jc "I can't take that."
    jump lbl_livingroom1_explore
    
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
screen Exploration_Livingroom2:
    add 'bg livingroom2'  
    $roomName = "livingroom2" 
    $inventory.SetCurrentRoom(roomName)
    
    use FixedItem(roomName, "door_basement", 0,0)
    use FixedItem(roomName, "tv", 0,0)
    use FixedItem(roomName, "tvstand", 0,0)
    use FixedItem(roomName, "bookshelf_wall", 0,0)
    use FixedItem(roomName, "bookshelf_floor", 0,0)
    
    #use ClickableItem("LargeBox", 1200, 450)
    #use ClickableItem("MediumBox", 1200, 450)
    #use ClickableItem("SmallBox", 1200, 450)
    
    use FixedItem(roomName, "box_large", 0,0)
    
    if (Livingroom2_MediumBoxPosition == 1):
      use FixedItem(roomName, "box_med_1", 0,0)
    if (Livingroom2_MediumBoxPosition == 2):
      use FixedItem(roomName, "box_med_2", 0,0)
    if (Livingroom2_MediumBoxPosition == 3):
      use FixedItem(roomName, "box_med_3", 0,0)
    
    if (Livingroom2_SmallBoxPosition == 1):
      use FixedItem(roomName, "box_small_1", 0,0)
    if (Livingroom2_SmallBoxPosition == 2):
      use FixedItem(roomName, "box_small_2", 0,0)
    if (Livingroom2_SmallBoxPosition == 3 and Livingroom2_MediumBoxPosition == 3):
      use FixedItem(roomName, "box_small_3b", 0,0)
    else:
        if (Livingroom2_SmallBoxPosition == 3):
            use FixedItem(roomName, "box_small_3", 0,0)
    
    if inventory.inventory_hand:
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == roomName:
          use FixedItem(roomName,"MouseToy", 0, 0)
    else:
      if ClawdiaLocation == roomName:
        use FixedItem(roomName,"MouseToy", 0, 0)
    
    if NightVision_active:
      if Livingroom2_LightsOff:
        add "images/backgrounds/NightVision.png" 
      else:
        add "images/backgrounds/NightVision_Bright.png" 
    else:
      if Livingroom2_LightsOff:
        add "images/backgrounds/Dark.png"
    
    use Exploration_Navigation 
    use hand_inventory
    use room_inventory(roomName)
    
#-----------------------------------------------------------------------
#---
label ShowLivingroom2():
    $CurrentRoomName = "livingroom2"

    #"Show Livingroom2"
    scene bg livingroom2
      
    if inventory.inventory_hand:
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == CurrentRoomName:
            show item_livingroom2_mousetoy
    else:
      #"Show all items"
      if ClawdiaLocation == CurrentRoomName:
        show item_livingroom2_mousetoy
        
    show item_livingroom2_box_large
    
    if (Livingroom2_MediumBoxPosition == 1):
      show item_livingroom2_box_med_1
    if (Livingroom2_MediumBoxPosition == 2):
      show item_livingroom2_box_med_2
    if (Livingroom2_MediumBoxPosition == 3):
      show item_livingroom2_box_med_3
    
    if (Livingroom2_SmallBoxPosition == 1):
      show item_livingroom2_box_small_1
    if (Livingroom2_SmallBoxPosition == 2):
      show item_livingroom2_box_small_2
    if (Livingroom2_SmallBoxPosition == 3):
      show item_livingroom2_box_small_3
    
    if inventory.inventory_hand:
      if inventory.inventory_hand[0] == 'MouseToy':
        $ClawdiaLocation = CurrentRoomName
        
    if NightVision_active:
      if Livingroom2_LightsOff:
        show roomeffect nightvision
      else:
        show roomeffect nightvision_bright
    else:
      if Livingroom2_LightsOff:
        show roomeffect dark
        
    return
    
label ShowLivingroom2WithChars:
    $CurrentRoomName = "livingroom2"
    call ShowLivingroom2
              
    if ClawdiaLocation == CurrentRoomName:
      show jessicaperson neutral:
        yalign -0.5
        xalign 0.7
      "ClawdiaLocation = [ClawdiaLocation] || roomName = [roomName]"  
        
    show jessicat happy at left
    return
#---
label lbl_livingroom2:
     
    #scene bg livingroom2
    #if NightVision_active:
    #  show roomeffect nightvision
    #else:
    #  if Bedroom1_LightsOff:
    #    show roomeffect dark
    call ShowLivingroom2WithChars
    jc "Its the other side of the Living room"
    jc "Lets see what else we can find here..."
    
    
    if not Inventory_CatMouth_unlocked and not ClawdiaLocation == CurrentRoomName:
        jc "Where did Clawdia get to?."
        jc "If only it was as easy for me to call her as it was for her to call for me when she wants food."
        jc "...I mean i guess i haven't actually tried yet. I suppose if she was close enough to hear she would probably come to see what was going on."
        $Inventory_CatMouth_unlocked = True
        "*Now you can use the Cats Meow ability to call Clawdia to your current location. This will only work in an open plan area or from differnt parts of the same room*"
        jump lbl_livingroom2_explore
    
label lbl_livingroom2_explore:
    call screen Exploration_Livingroom2
    $res = _return
    $ShouldPickUp = False
    call ShowLivingroom2WithChars
    
    if res[0] == 'Move':
      $labelname = res[1]
      if config.developer:
        jc "Ok lets go to [labelname]"
      jump expression labelname
      
    if Livingroom2_LightsOff:
      if not NightVision_active:
        "I can't see what that is right now."
        jump lbl_livingroom2_explore
      
    
    "Look, its a [res]."
        
    if (res=="door_basement"):
        jc "Its the door to the basement."
        if not Livingroom2_BasementDoorUnlocked:
          jc "Its locked. If i remember correctly Veronica said the door wasn't staying closed so she put a combination lock she had lying around on it to keep it closed."
          if not Livingroom2_BoxesArranged:
            jc "I will have to figure out a way to reach the lock though."
          else:
            if not Bedroom2_JournalRead:
              jc "She told me the combination but i cant for the life of me remember what it was since i hardly ever go into the basement."
            else:
              jc "If i can figure out the combination i will be able get the door open."
              jc "Nothing left to do but try i suppose."
              
              #menu:
              #  What is the first number?
              
              call screen combination_lock()
              $lockResult = _return
              
              if (lockResult=="Success"): 
                "With a loud click the lock popped open."
                $Livingroom2_BasementDoorUnlocked = True
                jc "Yay, it worked."
                return #lbl_chapter3_Basement
              else:
                "Hmm, it didn't open. I guess that was the wrong combination."
                
              
    if (res=="tv"):
        jc "Its my flat-screen TV. I mean its not as big as I'd like, but it will have to do for now."
    #if (res=="tvstand"):
    #    jc "..."
    if (res=="bookshelf_wall"):
        jc "Its a bookshelf. I can't reach it like this though."
    if (res=="bookshelf_floor"):
        jc "Its a bookshelf."
        if not Bedroom2_JournalRead:
          jc "Its a handful of Veronicas books."
        else:
          jc "Are these the books Veronica was talking about in her journal?"
          jc "Lets take a closer look."
          jc "Cry of the Doppelganger volume 1"
          jc "Love Vampires volume 3"
          jc "Office Fox volume 4"
          jc "Demonic Dreams volume 6"
          jc "Magical Auction volume 8"
          jc "Chimera Love volume 9"
          jc "Animal Transformations volume 10"
          jc "And thats it. An odd mix of books."
          
    if (res=="box_large") or (res=="box_med_1") or (res=="box_med_2") or (res=="box_med_3") or (res=="box_small_1") or (res=="box_small_2") or (res=="box_small_3"):
        jc "Theres a few empty boxes here."
        
        if not Livingroom2_BoxesKnockedOver:
          jc "They're stacked up so i can't jump up onto them."
          jc "Is there some way i can knock them over?"
          if ( ClawdiaLocation == 'livingroom1' or ClawdiaLocation == 'livingroom2'):
            jc "Maybe I can get Clawdia to help?"
            if Inventory_active == 'HeldItem':
              if (inventory.inventory_hand) and (inventory.inventory_hand[0] == 'LazerPen'):
                "As soon as the little red dot from the lazer pen catches her eye, Clawdias cat instincts kick in."
                "She chases around the room after the dot, and finally as the dot lands on the stacked boxes she swats at it and sends the boxes tumbling down."
                $Livingroom2_BoxesKnockedOver = True                
                $Livingroom2_MediumBoxPosition = 2
                $Livingroom2_SmallBoxPosition = 2
                cp "!!!"
                "Clawdia jumps back as the boxes fall and ends up half way up the stairs before she realizes shes not under attack and comes back down."
                jc "Well they came down pretty easily, were they empty?"              
        else:
          if (Livingroom2_MediumBoxPosition == 3 and Livingroom2_SmallBoxPosition == 3):
            jc "Ok, If I walk carefully I should be able to climb up these boxes now."
            $Livingroom2_BoxesArranged = True
          else:
            jc "Unfortunately they are too light to just jump onto, as if i do they're liable to just fall down."
            jc "On the bright side they're so light i should be able to move them around."
            jc "Maybe if i rearrange them i can carefully climb up?"
    
    if (res=="box_med_1") or (res=="box_med_2") or (res=="box_med_3"):
    
        if Livingroom2_BoxesKnockedOver:
          menu:
            "Move the Medium Box?"
            "Yes":
              "Jessica pushes the box with all the force her tiny body can muster and the box slides slowly across the floor."
              if Livingroom2_MediumBoxPosition == 2:
                $Livingroom2_MediumBoxPosition = 3
              else:
                $Livingroom2_MediumBoxPosition = 2
              jc "It wasnt easy but there we go."              
            "No":
              pass      
    
    if (res=="box_small_1") or (res=="box_small_2") or (res=="box_small_3"):
        if Livingroom2_BoxesKnockedOver:
          menu:
            "Move the Small Box?"
            "Yes":
              "Jessica pushes the box with all the force her tiny body can muster and the box slides quickly across the floor."
              if Livingroom2_SmallBoxPosition == 2:
                $Livingroom2_SmallBoxPosition = 3
              else:
                $Livingroom2_SmallBoxPosition = 2
              jc "There we go, that one was light even for me."              
            "No":
              pass
              
          #menu:
          #  "Move the boxes?"
          #  "Move the Large Box":
          #    menu:
          #      "Move the Large Box"
          #      "Move it forwards":
          #        if Livingroom2_LargeBoxPosition > 1:
          #          if Livingroom2_MediumBoxPosition == Livingroom2_LargeBoxPosition - 1:
          #            jc "Ok lets swap it with the Medium Box"
          #            $Livingroom2_MediumBoxPosition = Livingroom2_LargeBoxPosition
          #            $Livingroom2_LargeBoxPosition = Livingroom2_LargeBoxPosition - 1
          #          else:
          #            jc "Ok lets swap it with the Small Box"
          #            $Livingroom2_SmallBoxPosition = Livingroom2_LargeBoxPosition
          #            $Livingroom2_LargeBoxPosition = Livingroom2_LargeBoxPosition - 1
          #        else:
          #          jc "I can't move it any closer."
          #          
          #      "Move it backwards":
          #        if Livingroom2_LargeBoxPosition < 3:
          #          if Livingroom2_MediumBoxPosition == Livingroom2_LargeBoxPosition + 1:
          #            jc "Ok, lets swap it with the Medium Box"
          #            $Livingroom2_MediumBoxPosition = Livingroom2_LargeBoxPosition
          #            $Livingroom2_LargeBoxPosition = Livingroom2_LargeBoxPosition + 1
          #          else:
          #            jc "Ok, lets swap it with the Small Box"
          #            $Livingroom2_SmallBoxPosition = Livingroom2_LargeBoxPosition
          #            $Livingroom2_LargeBoxPosition = Livingroom2_LargeBoxPosition + 1
          #        else:
          #          jc "There's not much point moving it any further away."
          #      "Do Nothing":
          #        pass
          #  "Move the Medium Box":
          #    menu:
          #      "Move the Large Box"
          #      "Move it forwards":
          #        if Livingroom2_MediumBoxPosition > 1:
          #          if Livingroom2_LargeBoxPosition == Livingroom2_MediumBoxPosition - 1:
          #            jc "Ok lets swap it with the Large Box"
          #            $Livingroom2_LargeBoxPosition = Livingroom2_MediumBoxPosition
          #            $Livingroom2_MediumBoxPosition = Livingroom2_MediumBoxPosition - 1
          #          else:
          #            jc "Ok lets swap it with the Small Box"
          #            $Livingroom2_SmallBoxPosition = Livingroom2_MediumBoxPosition
          #            $Livingroom2_MediumBoxPosition = Livingroom2_MediumBoxPosition - 1
          #        else:
          #          jc "I can't move it any closer."
          #          
          #      "Move it backwards":
          #        if Livingroom2_MediumBoxPosition < 3:
          #          if Livingroom2_LargeBoxPosition == Livingroom2_MediumBoxPosition + 1:
          #            jc "Ok, lets swap it with the Medium Box"
          #            $Livingroom2_LargeBoxPosition = Livingroom2_MediumBoxPosition
          #            $Livingroom2_MediumBoxPosition = Livingroom2_MediumBoxPosition + 1
          #          else:
          #            jc "Ok, lets swap it with the Small Box"
          #            $Livingroom2_SmallBoxPosition = Livingroom2_MediumBoxPosition
          #            $Livingroom2_MediumBoxPosition = Livingroom2_MediumBoxPosition + 1
          #        else:
          #          jc "There's not much point moving it any further away."
          #      "Do Nothing":
          #        pass
          #  "Move the Small Box":
          #    menu:
          #      "Move the Large Box"
          #      "Move it forwards":
          #        if Livingroom2_SmallBoxPosition > 1:
          #          if Livingroom2_MediumBoxPosition == Livingroom2_SmallBoxPosition - 1:
          #            jc "Ok lets swap it with the Medium Box"
          #            $Livingroom2_MediumBoxPosition = Livingroom2_SmallBoxPosition
          #            $Livingroom2_SmallBoxPosition = Livingroom2_SmallBoxPosition - 1
          #          else:
          #            jc "Ok lets swap it with the Large Box"
          #            $Livingroom2_LargeBoxPosition = Livingroom2_SmallBoxPosition
          #            $Livingroom2_SmallBoxPosition = Livingroom2_SmallBoxPosition - 1
          #        else:
          #          jc "I can't move it any closer."
          #          
          #      "Move it backwards":
          #        if Livingroom2_SmallBoxPosition < 3:
          #          if Livingroom2_MediumBoxPosition == Livingroom2_SmallBoxPosition + 1:
          #            jc "Ok, lets swap it with the Medium Box"
          #            $Livingroom2_MediumBoxPosition = Livingroom2_SmallBoxPosition
          #            $Livingroom2_SmallBoxPosition = Livingroom2_SmallBoxPosition + 1
          #          else:
          #            jc "Ok, lets swap it with the Large Box"
          #            $Livingroom2_LargeBoxPosition = Livingroom2_SmallBoxPosition
          #            $Livingroom2_SmallBoxPosition = Livingroom2_SmallBoxPosition + 1
          #        else:
          #          jc "There's not much point moving it any further away."
          #      "Do Nothing":
          #        pass
          
        #$ShouldPickUp = True
    #if (res=="MediumBox"):
    #    jc "..."
        #$ShouldPickUp = True
    #if (res=="SmallBox"):
    #    jc "..."
        #$ShouldPickUp = True
    if (res=="MouseToy"):
        jc "Clawdias' favourite mouse toy. She is rarely ever seen too far from it."
        $ShouldPickUp = True
        
    if (res=="dropItem"):
        $inventory.DropItemFromHand()
        jc "You stay here for a bit Clawdia."
        
    if (res=="callClawdia"):
        if ClawdiaLocation == CurrentRoomName:
            jc "Oh wait, shes already here."
        else:
            if "livingroom" in ClawdiaLocation or "kitchen" in ClawdiaLocation or "hallway" in ClawdiaLocation:
                "Clawdia comes strolling over to see whats going on. She stretches slowly once she arrives."
                show jessicaperson happy:
                    yalign -0.5
                    xalign 0.7
                jc "I guess even in my body you're never in a hurry to go anywhere."
                $ClawdiaLocation = CurrentRoomName            
            else:
                jc "I guess she can't hear me."
        
            
        
    if ShouldPickUp:
      if inventory.IsItemCollectable(res):
        menu:
          "Take it?"
          "Yes":
            $inventory.AddItemToHand(res)
          "No":
            $inventory.AddItemToRoomInventory(res, current_room[0])
      else:
        jc "I can't take that."
    jump lbl_livingroom2_explore
    
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
screen Exploration_Kitchen:
    add 'bg kitchen'   
    $roomName = "kitchen" 
    $inventory.SetCurrentRoom(roomName)
    
    use FixedItem(roomName, "fridge_side", 0,0)
    use FixedItem(roomName, "fridge_door", 0,0)
    use FixedItem(roomName, "fridge_top", 0,0)
    use FixedItem(roomName, "cerealboxes", 0,0)
    use FixedItem(roomName, "cupboards_left", 0,0)
    if not Kitchen_CupboardDoorClosed:
      use FixedItem(roomName, "cupboards_door", 0,0)
    else:
      use FixedItem(roomName, "cupboards_right_top", 0,0)
    use FixedItem(roomName, "cupboards_right_bottom", 0,0)
    use FixedItem(roomName, "oven", 0,0)
    use FixedItem(roomName, "stove", 0,0)
    use FixedItem(roomName, "sink", 0,0)
    use FixedItem(roomName, "blinds", 0,0)
    #use FixedItem(roomName, "drawer", 0,0)
    use FixedItem(roomName, "magnets", 0, 0)
    
    use FixedItem(roomName, "note", 0,0)
    #use FixedItem(roomName, "Food", 0,0)
    
    
    #use ClickableItem("VeronicasKeys", 1200, 450)
    #use ClickableItem("Spoon", 1200, 450)
    #use ClickableItem("Bowl", 1200, 450)
    #use ClickableItem("PlasticCup", 1200, 450)
    #use ClickableItem("Magnets", 1200, 450)
    #under fridge
    #use ClickableItem("token_gold", 1200, 450)
    
    if inventory.inventory_hand:
      if not inventory.inventory_hand[0] == 'token_gold' and not Boilerroom_TokenPlaced_gold:
        use FixedItem(roomName,"fridge_under", 0, 0)
      if not inventory.inventory_hand[0] == 'Spoon':
        use FixedItem(roomName,"Spoon", 0, 0)
      if not inventory.inventory_hand[0] == 'Magnets_loose':
        use FixedItem(roomName,"Magnets_loose", 0, 0)
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == roomName:
          use FixedItem(roomName,"MouseToy", 0, 0)
    else:
        if not Boilerroom_TokenPlaced_gold:
            use FixedItem(roomName,"fridge_under", 0, 0)
        use FixedItem(roomName,"Spoon", 0, 0)
        use FixedItem(roomName,"Magnets_loose", 0, 0)
        if ClawdiaLocation == roomName:
            use FixedItem(roomName,"MouseToy", 0, 0)
    
    if NightVision_active:
      if Kitchen_LightsOff:
        add "images/backgrounds/NightVision.png" 
      else:
        add "images/backgrounds/NightVision_Bright.png" 
    else:
      if Kitchen_LightsOff:
        add "images/backgrounds/Dark.png"
    
    use Exploration_Navigation 
    use hand_inventory
    use room_inventory(roomName)
    
#-----------------------------------------------------------------------
#---
label ShowKitchen():
    $CurrentRoomName = "kitchen"

    #"Show Kitchen"
    scene bg kitchen
      
    if inventory.inventory_hand:
      if not inventory.inventory_hand[0] == 'token_gold' and not Boilerroom_TokenPlaced_gold:
        show item_kitchen_fridge_under
      if not inventory.inventory_hand[0] == 'Spoon':
        show item_kitchen_spoon
      if not inventory.inventory_hand[0] == 'Magnets_loose':
        show item_kitchen_magnets_loose
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == CurrentRoomName:
            show item_kitchen_mousetoy
    else:
      #"Show all items"
      if not Boilerroom_TokenPlaced_gold:
        show item_kitchen_fridge_under
      show item_kitchen_spoon
      show item_kitchen_magnets_loose
      if ClawdiaLocation == CurrentRoomName:
        show item_kitchen_mousetoy
        
    if (not Kitchen_CupboardDoorClosed):
      show item_kitchen_cupboardOpen
      
    if inventory.inventory_hand:
      if inventory.inventory_hand[0] == 'MouseToy':
        $ClawdiaLocation = CurrentRoomName
        
    if NightVision_active:
      if Kitchen_LightsOff:
        show roomeffect nightvision
      else:
        show roomeffect nightvision_bright
    else:
      if Kitchen_LightsOff:
        show roomeffect dark
        
    return
    
label ShowKitchenWithChars:
    $CurrentRoomName = "kitchen"
    call ShowKitchen
              
    if ClawdiaLocation == CurrentRoomName:
      show jessicaperson neutral:
        yalign -0.5
        xalign 0.7
        
    show jessicat happy at left
    return
#---
label lbl_kitchen:
     
    #scene bg kitchen
    #if NightVision_active:
    #  show roomeffect nightvision
    #else:
    #  if Bedroom1_LightsOff:
    #    show roomeffect dark
    call ShowKitchenWithChars
    jc "Its the Kitchen"
    jc "Lets see what else we can find here..."
    
label lbl_kitchen_explore:
    call screen Exploration_Kitchen
    $res = _return
    $ShouldPickUp = False
    call ShowKitchenWithChars
    
    if res[0] == 'Move':
      $labelname = res[1]
      if config.developer:
        jc "Ok lets go to [labelname]"
      jump expression labelname
      
    if Kitchen_LightsOff:
      if not NightVision_active:
        "I can't see what that is right now."
        jump lbl_kitchen_explore
      
    
    "Look, its a [res]."
        
    if (res=="fridge_side"):
        jc "Its the refrigerator. The side is good for sticking notes and things on."
    if (res=="fridge_door"):
        jc "Its the refrigerator. The door is pretty stiff."
        jc "I have a hard enough time getting it open as a person, so opening it as a cat is pretty much impossible."
    if (res=="fridge_top"):
        jc "The top of the fridge is mostly covered in various cereal boxes."
        if Livingroom1_PhoneCallHappened:
          jc "Isn't this is where Veronica said she had put her keys?"
        if not Kitchen_CupboardDoorClosed:
          jc "I'm not going to be able to get up while the cupboard door is blocking the way up."
        else:
          "Theres a small container up here with some loose change."
          if (not inventory.inventory_hand) or ((inventory.inventory_hand) and (not inventory.inventory_hand[0] == 'VeronicasKeys')):
            "Veronicas Keys are up here too."
            menu:
              "Take them?"
              "Yes": 
                $inventory.AddItemToHand('VeronicasKeys')
              "No":
                $inventory.AddItemToRoomInventory('VeronicasKeys', current_room[0])
            
    if (res=="fridge_under"):
        if not Kitchen_TokenRetrieved:
            jc "Huh. Looks like theres something shiny wedged under the fridge."
            jc "I dont think its stuck, but theres not a lot of space so even with my little cat paws i can't reach under and get it out."
            if (not inventory.inventory_hand) or ((inventory.inventory_hand) and (not inventory.inventory_hand[0] == 'Magnets_loose')):
              jc "Wonder if i could find something to help pull it out?"
            else:
              jc "Wonder if i could pull it out using this magnet?"
            if Inventory_active == 'HeldItem':
                if (inventory.inventory_hand) and (inventory.inventory_hand[0] == 'Magnets_loose'):
                    jc "Lets just stick this on the egde here and slooowly pull..."
                    jc "There we go."
                    jc "Looks like a golden disk of some sort. I dont recognise it, must belong to Veronica"
                    $Kitchen_TokenRetrieved = True
                    menu:
                        "Should i take it with me?"            
                        "Yes": 
                            $inventory.AddItemToHand('token_gold')
                        "No":
                            jc "Ok, ill just leave it sticking out a little so i can pick it up again later if i need to."
                            $inventory.AddItemToRoomInventory('token_gold', current_room[0])
        else:
            jc "Looks like the golden coin is still sitting by the fridge."
            menu:
              "Should i take it with me?"            
              "Yes": 
                $inventory.AddItemToHand('token_gold')
              "No":
                $inventory.AddItemToRoomInventory('token_gold', current_room[0])
        
        
    if (res=="cerealboxes"):
        jc "Various boxes of cereal." 
        jc "You may be thinking how can two people eat so much cereal, but its one person. I have toast for breakfast but Veronica likes to have 'options'."
        jc "Either way I can't jump on top of the fridge from the dining table since they are in the way."
    if (res=="cupboards_left"):
        jc "This is where we keep the dishes"
        jc "It's closed so i can't get inside."
    if (res=="cupboards_door"):
        jc "The door to the cupboard is open."
        jc "Its blocking the way so i cant jump onto the fridge but it's too high up for me to just push closed."
        jc "I could jump into the cupboard but there's nothing useful in here, just food."
        if ( ClawdiaLocation == 'kitchen' ):
          jc "Maybe I can get Clawdia to help?"
          if Inventory_active == 'HeldItem':
            if (inventory.inventory_hand) and (inventory.inventory_hand[0] == 'LazerPen'):
                "As soon as the little red dot from the lazer pen catches her eye, Clawdias cat instincts kick in."
                "She chases the dot across the kitchen counter, and finally as the dot lands on the open cupboard door she swats at it and it slams closed with a bang."
                $Kitchen_CupboardDoorClosed = True
                cp "!!!"
                "Clawdia jumps back at the sudden noise, but its not long before shes looking for the dot again."
                jc "Thanks Clawdia. Now i should be able to reach the top of the fridge."
    if (res=="cupboards_right_top"):
        jc "This is where we keep the food."
        jc "It's closed so i can't get inside."
    if (res=="cupboards_right_bottom"):
        jc "This is where we keep the pots and pans."
        jc "It's closed so i can't get inside."
    if (res=="oven"):
        jc "Ahh, my trusty oven."
        jc "Thinking about it is making me hungry."
        jc "I should find something to fix me before I start worrying about what I'm having for dinner."
    if (res=="stove"):
        jc "Its the stove top. I probably shouldn't mess with this while I'm stuck as a cat."
    if (res=="sink"):
        jc "Its the sink. Theres nothing in it at the moment."
    if (res=="blinds"):
        jc "The blinds are closed but theres still enough light getting through to see the kitchen."
    #if (res=="drawer"):
    #    jc "This is where we keep the cutlery."
    if (res=="note"):
        jc "Oh, looks like Veronica put up a shopping list."
        jc "Lets see what she wants; chalk, candles, matches and incense."
        jc "It's a little odd that there's no food on the list."
        $Kitchen_ListFound = True
    #if (res=="Food"):
    #    jc "..."
        
    #if (res=="VeronicasKeys"):
    #    jc "..."
    #    $ShouldPickUp = True
    if (res=="Spoon"):
        jc "Oh a spoon. I guess i forgot to put it away."
        $ShouldPickUp = True
    #if (res=="Bowl"):
    #    jc "..."
        #$ShouldPickUp = True
    #if (res=="PlasticCup"):
    #    jc "..."
        #$ShouldPickUp = True
    if (res=="magnets"):
        jc "Our fridge magnets, Its crazy how much fun it actually is writing silly messages on the fridge with these."
    if (res=="Magnets_loose"):
        jc "Our fridge magnets, one of them has fallen low enough that i could probably take it if i wanted to."
        $ShouldPickUp = True
    if (res=="MouseToy"):
        jc "Clawdia's favourite mouse toy. She is rarely ever seen too far from it."
        $ShouldPickUp = True
        
    if (res=="dropItem"):
        $inventory.DropItemFromHand()
        jc "You stay here for a bit Clawdia."
    if (res=="callClawdia"):
        if ClawdiaLocation == CurrentRoomName:
            jc "Oh wait, shes already here."
        else:
            if "livingroom" in ClawdiaLocation or "kitchen" in ClawdiaLocation:
                "Clawdia comes strolling over to see whats going on. She stretches slowly once she arrives."
                show jessicaperson happy:
                    yalign -0.5
                    xalign 0.7
                jc "I guess even in my body you're never in a hurry to go anywhere."
                $ClawdiaLocation = CurrentRoomName            
            else:
                jc "I guess she can't hear me."
        
    if ShouldPickUp:
      if inventory.IsItemCollectable(res):
        menu:
          "Take it?"
          "Yes":
            $inventory.AddItemToHand(res)
          "No":
            $inventory.AddItemToRoomInventory(res, current_room[0])
      else:
        jc "I can't take that."
    jump lbl_kitchen_explore
    
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
screen Exploration_Basement1:
    add 'bg basement1'  
    $roomName = "basement1"  
    $inventory.SetCurrentRoom(roomName)
    
    if Basement1_SpiderAlive:
      use FixedItem(roomName, "spider", 0,0)
    
    use FixedItem(roomName, "stairs_livingroom2", 0,0)
    use FixedItem(roomName, "lightswitch", 0,0)
    use FixedItem(roomName, "washingmachine", 0,0)
    use FixedItem(roomName, "shelves", 0,0)
    
    #On Shelves - In box
    #use ClickableItem("Candle", 1200, 450)
    #use ClickableItem("Matches", 1200, 450)
    #if not inventory.inventory_hand[0] == 'Candle':
    #  use FixedItem(roomName,"Candle", 0, 0)
    #if not inventory.inventory_hand[0] == 'Matches':
    #  use FixedItem(roomName,"Matches", 0, 0)
    
    if inventory.inventory_hand:
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == roomName:
          use FixedItem(roomName,"MouseToy", 0, 0)
    else:
      if ClawdiaLocation == roomName:
        use FixedItem(roomName,"MouseToy", 0, 0)
    
    if NightVision_active:
      if Basement1_LightsOff:
        add "images/backgrounds/NightVision.png" 
      else:
        add "images/backgrounds/NightVision_Bright.png" 
    else:
      if Basement1_LightsOff:
        add "images/backgrounds/Dark.png"
    
    use Exploration_Navigation 
    use hand_inventory
    use room_inventory(roomName)
    
#-----------------------------------------------------------------------
#---
label ShowBasement1():
    $CurrentRoomName = "basement1"

    #"Show Basement1"
    scene bg basement1
      
    if inventory.inventory_hand:
      #On Shelves - In box
      #if not inventory.inventory_hand[0] == 'Candle':
      #  show item_basement1_candle
      #if not inventory.inventory_hand[0] == 'Matches':
      #  show item_basement1_matches
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == CurrentRoomName:
            show item_basement1_mousetoy
    else:
      #"Show all items"
      if ClawdiaLocation == CurrentRoomName:
        show item_basement1_mousetoy
        
    if (Basement1_SpiderAlive):
      show item_basement1_spider
      
    if inventory.inventory_hand:
      if inventory.inventory_hand[0] == 'MouseToy':
        $ClawdiaLocation = CurrentRoomName
        
    if NightVision_active:
      if Basement1_LightsOff:
        show roomeffect nightvision
      else:
        show roomeffect nightvision_bright
    else:
      if Basement1_LightsOff:
        show roomeffect dark
        
    return
    
label ShowBasement1WithChars:
    $CurrentRoomName = "basement1"
    call ShowBasement1
              
    if ClawdiaLocation == CurrentRoomName:
      show jessicaperson neutral:
        yalign -0.5
        xalign 0.7
        
    show jessicat happy at left
    return
#---
label lbl_basement1:
     
    #scene bg basement1
    #if NightVision_active:
    #  show roomeffect nightvision
    #else:
    #  if Basement1_LightsOff:
    #    show roomeffect dark
    call ShowBasement1WithChars
    if not Basement1_Arrival:
      return #lbl_chapter3_Basement
    jc "Its the Basement"
    if (Basement1_LightsOff) and (not NightVision_active):
      jc "Its pretty dark in here."
    else:
      jc "Lets see what else we can find here..."
    
label lbl_basement1_explore:
    call screen Exploration_Basement1
    $res = _return
    $ShouldPickUp = False
    call ShowBasement1WithChars
    
    if res[0] == 'Move':
      $labelname = res[1]
      if config.developer:
        jc "Ok lets go to [labelname]"
      jump expression labelname
      
    if Basement1_LightsOff:
      if not NightVision_active:
        "I can't see what that is right now."
        if not Inventory_CatEyes_unlocked:
          jc "Aren't cats supposed to have good night vision?"
          jc "Maybe if i try to focus on it i'll be able to see."
          $Inventory_CatEyes_unlocked = True
          "*Now you can use the Cats Eyes ability to enable your night vision*"
        jump lbl_basement1_explore
    
    "Look, its a [res]."
        
    if Basement1_LightsOff:
      if (res=="lightswitch"):
          jc "Oh! Here's the light switch."
          jc "Lets turn that on."
          $Basement1_LightsOff = False
          scene bg basement1
          if NightVision_active:
            show roomeffect nightvision
    if Basement1_SpiderAlive:
      if (res=="spider"):
        if Basement1_SpiderMet:
          jc "Its a freaking spider."
          jc "I don't know if its because I'm a cat or whatever, but i feel like that thing is freaking huge."
          #jc "Theres no way I'm doing anything else in here until its gone."
          if ( ClawdiaLocation == 'basement1' ):
              jc "Maybe I can get Clawdia to help?"
              if Basement1_LightsOff:
                jc "She wont be able to see anything in the dark though."
              else:
                  if Inventory_active == 'HeldItem':
                    if (inventory.inventory_hand) and (inventory.inventory_hand[0] == 'LazerPen'):
                        "As soon as the little red dot from the lazer pen catches her eye, Clawdias cat instincts kick in."
                        "As she starts the chase the dot the spider skitters away startled."
                        "The spiders movement catches her eye and she starts to chase it."
                        jc "YESSS. Get it Clawdia! My Hero! Stomp on it!"
                        "She pounces on the spider and cups her hands over it"
                        jc "Ew, omg dont touch it. I hope you squished it at least."
                        "Jessica shivers just thinking about the spider crawling around on her hands"
                        jc "Wait, what are you doing."
                        "Clawdia is holding her hands up to her face, staring intently into her cupped hands."
                        jc "C-Clawdia?"
                        return #lbl_chapter3_Spider_End
        else:
          return #lbl_chapter3_Spider
    if (res=="stairs_livingroom2"):
        jc "These stairs lead back up to the living room."
        if Basement1_SpiderAlive:
          jc "Where it's safe."
    if (res=="washingmachine"):
        jc "It's the washing machine. I've actually never used this one before."
    if (res=="shelves"):
      if Basement1_SpiderAlive:
        jc "Can't you see that giant spider? Theres no way im going over there while its in the way"
      else:
        jc "Looks like theres various boxes on the shelves filled with various bits and bobs."
        jc "I wonder if any of it is usefull."
        if Boilerroom_BasementCandlePlaced and Boilerroom_MatchesPlaced:
            jc "Doesnt look like theres anything else i can use here."
        else:
            if not Boilerroom_BasementCandlePlaced and((not inventory.inventory_hand) or ((inventory.inventory_hand) and (not inventory.inventory_hand[0] == 'candle_basement'))):
              jc "Looks like theres a spare candle on the shelf."
            if not Boilerroom_MatchesPlaced and((not inventory.inventory_hand) or ((inventory.inventory_hand) and (not inventory.inventory_hand[0] == 'Matches'))):
              jc "Looks like theres a box of Long reach matches in one of these boxes."
            menu:
              "Should i take something?"
              "Take the candle" if not Boilerroom_BasementCandlePlaced and((not inventory.inventory_hand) or ((inventory.inventory_hand) and (not inventory.inventory_hand[0] == 'candle_basement'))):
                  $inventory.AddItemToHand('candle_basement')
              "Take the matches" if not Boilerroom_MatchesPlaced and((not inventory.inventory_hand) or ((inventory.inventory_hand) and (not inventory.inventory_hand[0] == 'Matches'))):
                  $inventory.AddItemToHand('Matches')
              "Leave them here.":
                if not Boilerroom_BasementCandlePlaced and((not inventory.inventory_hand) or ((inventory.inventory_hand) and (not inventory.inventory_hand[0] == 'candle_basement'))):
                  $inventory.AddItemToRoomInventory('candle_basement', current_room[0])
                if not Boilerroom_MatchesPlaced and((not inventory.inventory_hand) or ((inventory.inventory_hand) and (not inventory.inventory_hand[0] == 'Matches'))):
                  $inventory.AddItemToRoomInventory('Matches', current_room[0])
    if (res=="MouseToy"):
        jc "Clawdia's favourite mouse toy. She is rarely ever seen too far from it."
        $ShouldPickUp = True
        
    if (res=="dropItem"):
        $inventory.DropItemFromHand()
        jc "You stay here for a bit Clawdia."
        
    if (res=="callClawdia"):
        if ClawdiaLocation == CurrentRoomName:
            jc "Oh wait, shes already here."
        else:
            if "basement" in ClawdiaLocation:
                "Clawdia comes strolling over to see whats going on. She stretches slowly once she arrives."
                show jessicaperson happy:
                    yalign -0.5
                    xalign 0.7
                jc "I guess even in my body you're never in a hurry to go anywhere."
                $ClawdiaLocation = CurrentRoomName            
            else:
                jc "I guess she can't hear me."
        
        
    if ShouldPickUp:
      if inventory.IsItemCollectable(res):
        menu:
          "Take it?"
          "Yes":
            $inventory.AddItemToHand(res)
          "No":
            $inventory.AddItemToRoomInventory(res, current_room[0])
      else:
        jc "I can't take that."
    jump lbl_basement1_explore
    
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
screen Exploration_Basement2:
    add 'bg basement2'  
    $roomName = "basement2"
    $inventory.SetCurrentRoom(roomName)
    
      
    use FixedItem(roomName, "door_office", 0,0)
    use FixedItem(roomName, "door_boilerroom", 0,0)
    use FixedItem(roomName, "door_bathroom2", 0,0)
    
    use FixedItem(roomName, "shelves", 0,0)
    use FixedItem(roomName, "boxes", 0,0)
    
    #use ClickableItem("Candle", 1200, 450)
    if inventory.inventory_hand:
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == roomName:
          use FixedItem(roomName,"MouseToy", 0, 0)
    else:
      if ClawdiaLocation == roomName:
        use FixedItem(roomName,"MouseToy", 0, 0)
    
    if NightVision_active:
      if Basement2_LightsOff:
        add "images/backgrounds/NightVision.png" 
      else:
        add "images/backgrounds/NightVision_Bright.png" 
    else:
      if Basement2_LightsOff:
        add "images/backgrounds/Dark.png"
    
    use Exploration_Navigation 
    use hand_inventory
    use room_inventory(roomName)
    
#-----------------------------------------------------------------------
#---
label ShowBasement2():
    $CurrentRoomName = "basement2"

    #"Show Basement2"
    scene bg basement2
      
    if inventory.inventory_hand:
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == CurrentRoomName:
            show item_basement2_mousetoy
    else:
      #"Show all items"
      if ClawdiaLocation == CurrentRoomName:
        show item_basement2_mousetoy
      
    if inventory.inventory_hand:
      if inventory.inventory_hand[0] == 'MouseToy':
        $ClawdiaLocation = CurrentRoomName
        
    if NightVision_active:
      if Basement2_LightsOff:
        show roomeffect nightvision
      else:
        show roomeffect nightvision_bright
    else:
      if Basement2_LightsOff:
        show roomeffect dark
        
    return
    
label ShowBasement2WithChars:
    $CurrentRoomName = "basement2"
    call ShowBasement2
              
    if ClawdiaLocation == CurrentRoomName:
      show jessicaperson neutral:
        yalign -0.5
        xalign 0.7
        
    show jessicat happy at left
    return
#---
label lbl_basement2:
     
    #scene bg basement2
    #if NightVision_active:
    #  show roomeffect nightvision
    #else:
    #  if Basement2_LightsOff:
    #    show roomeffect dark
    call ShowBasement2WithChars
    jc "Its the other side of the Basement"
    jc "Lets see what else we can find here..."
    
label lbl_basement2_explore:
    call screen Exploration_Basement2
    $res = _return
    $ShouldPickUp = False
    call ShowBasement2WithChars
    
    if res[0] == 'Move':
      $labelname = res[1]
      if config.developer:
        jc "Ok lets go to [labelname]"
      jump expression labelname
      
    if Basement2_LightsOff:
      if not NightVision_active:
        "I can't see what that is right now."
        jump lbl_basement2_explore
      
    
    "Look, its a [res]."
        
    if (res=="door_office"):
      jc "Its the door to Veronicas home office."
      if not Basement2_OfficeDoorUnlocked:
        jc "It seems to be locked. I don't see any keyhole though."
        jc "There seems to be a sensor beside the door, maybe it needs some kind of electronic key?"
        #jc "A card or a keyfob or something like that."
        if Inventory_active == 'HeldItem':
            if (inventory.inventory_hand) and (inventory.inventory_hand[0] == 'VeronicasKeys'):
                jc "Lets see if the fob on this keychain is the key to getting in here."
                jc "Oh, it worked!"
                $Basement2_OfficeDoorUnlocked = True
        
        
    if (res=="door_boilerroom"):
      jc "Its the door to the boiler room."
      if not Office_MagicInstructionsFound:
        jc "I don't think there's much point going in there right now."
      else:
        jc "I guess i should check this out."
        $Basement2_BoilerroomDoorUnlocked = True
    if (res=="door_bathroom2"):
      jc "Its the door to the basement bathroom."
      if not Basement2_Bathroom2DoorUnlocked:
        jc "TODO: Is this supposed to be locked? I dont remember"
        $Basement2_Bathroom2DoorUnlocked = True
    if (res=="MouseToy"):
        jc "Clawdia's favourite mouse toy. She is rarely ever seen too far from it."
        $ShouldPickUp = True
        
    if (res=="boxes"):
      jc "More boxes, these ones are taped closed so i can't see what's inside."
    if (res=="shelves"):
      jc "Shelves full of useless bits and bobs. Why do we even keep all this junk?"
        
    if (res=="dropItem"):
        $inventory.DropItemFromHand()
        jc "You stay here for a bit Clawdia."
        
    if (res=="callClawdia"):
        if ClawdiaLocation == CurrentRoomName:
            jc "Oh wait, shes already here."
        else:
            if "basement" in ClawdiaLocation:
                "Clawdia comes strolling over to see whats going on. She stretches slowly once she arrives."
                show jessicaperson happy:
                    yalign -0.5
                    xalign 0.7
                jc "I guess even in my body you're never in a hurry to go anywhere."
                $ClawdiaLocation = CurrentRoomName            
            else:
                jc "I guess she can't hear me."
        
    if ShouldPickUp:
      if inventory.IsItemCollectable(res):
        menu:
          "Take it?"
          "Yes":
            $inventory.AddItemToHand(res)
          "No":
            $inventory.AddItemToRoomInventory(res, current_room[0])
      else:
        jc "I can't take that."
    jump lbl_basement2_explore
    
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
screen Exploration_Office:
    add 'bg office'   
    $roomName = "office" 
    $inventory.SetCurrentRoom(roomName)
    
    use FixedItem(roomName, "computer", 0,0)
    use FixedItem(roomName, "keyboard", 0,0)
    use FixedItem(roomName, "printer", 0,0)
    use FixedItem(roomName, "bookshelf", 0,0)
    use FixedItem(roomName, "picture_left", 0,0)
    use FixedItem(roomName, "picture_right", 0,0)
    use FixedItem(roomName, "drawers_left", 0,0)
    use FixedItem(roomName, "drawers_right", 0,0)
    #use FixedItem(roomName, "desk", 0,0)
    use FixedItem(roomName, "chair", 0,0)
    use FixedItem(roomName, "notepad", 0,0)
    use FixedItem(roomName, "bookpile_left", 0,0)
    use FixedItem(roomName, "bookpile_middle", 0,0)
    use FixedItem(roomName, "bookpile_right", 0,0)
    use FixedItem(roomName, "cupboard", 0,0)
    
    #use ClickableItem("Candle", 1200, 450)
    
    if inventory.inventory_hand:
      if not inventory.inventory_hand[0] == 'OfficePen':
          use FixedItem(roomName, "OfficePen", 0, 0)
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == roomName:
          use FixedItem(roomName,"MouseToy", 0, 0)
    else:
      use FixedItem(roomName, "OfficePen", 0, 0)
      if ClawdiaLocation == roomName:
        use FixedItem(roomName,"MouseToy", 0, 0)
    
    if NightVision_active:
      if Office_LightsOff:
        add "images/backgrounds/NightVision.png" 
      else:
        add "images/backgrounds/NightVision_Bright.png" 
    else:
      if Office_LightsOff:
        add "images/backgrounds/Dark.png"
    
    use Exploration_Navigation 
    use hand_inventory
    use room_inventory(roomName)
    
#-----------------------------------------------------------------------
#---
label ShowOffice():
    $CurrentRoomName = "office"

    #"Show Office"
    scene bg office
      
    if inventory.inventory_hand:
      if not inventory.inventory_hand[0] == 'OfficePen':
        show item_office_pen
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == CurrentRoomName:
            show item_office_mousetoy
    else:
      #"Show all items"
      if ClawdiaLocation == CurrentRoomName:
        show item_office_mousetoy
      show item_office_pen
      
    if inventory.inventory_hand:
      if inventory.inventory_hand[0] == 'MouseToy':
        $ClawdiaLocation = CurrentRoomName
        
    if NightVision_active:
      if Office_LightsOff:
        show roomeffect nightvision
      else:
        show roomeffect nightvision_bright
    else:
      if Office_LightsOff:
        show roomeffect dark
        
    return
    
label ShowOfficeWithChars:
    $CurrentRoomName = "office"
    call ShowOffice
              
    if ClawdiaLocation == CurrentRoomName:
      show jessicaperson neutral:
        yalign -0.5
        xalign 0.7
        
    show jessicat happy at left
    return
#---
label lbl_office:
     
    #scene bg office
    #if NightVision_active:
    #  show roomeffect nightvision
    #else:
    #  if Bedroom1_LightsOff:
    #    show roomeffect dark
    call ShowOfficeWithChars
    jc "Its Veronicas home office"
    jc "Lets see what else we can find here..."
    
label lbl_office_explore:
    call screen Exploration_Office
    $res = _return
    $ShouldPickUp = False
    call ShowOfficeWithChars
    
    if res[0] == 'Move':
      $labelname = res[1]
      if config.developer:
        jc "Ok lets go to [labelname]"
      jump expression labelname
      
    if Office_LightsOff:
      if not NightVision_active:
        "I can't see what that is right now."
        jump lbl_office_explore
      
    
    "Look, its a [res]."
            
    if (res=="computer"):
      jc "I wonder if i can find anything useful on the computer."
      if Office_ComputerUnlocked:
        jc "Ok, its unlocked."
        if Office_MagicInstructionsFound:
          jc "I could take another look at the Instructions again if i wanted."
          menu:
            "Take another look?"
            "Yes":
              call lbl_chapter3_MagicInstructions from _call_lbl_chapter3_MagicInstructions_1
            "No":
              pass
        else:
          return #lbl_chapter3_Instructions
      else:
        jc "Oh, its locked. "
        if Office_ComputerPasswordHint:
            jc "Oh, i wonder if that thing i read earlier would help here."
            #menu:
            #    "*Password puzzle here*"
            #    "Correct":
            #        jc "Awesome, it worked."
            #        $Office_ComputerUnlocked = True
            #    "Incorrect":
            #        jc "Well, that didn't work. Should i try something else?"
        $password = renpy.input("Enter Password...")
        if password == Office_ComputerPassword:
            jc "Awesome, im in."
            $Office_ComputerUnlocked = True
        else:
            jc "Hmm, that didn't work."
    if (res=="printer"):
        jc "A printer. Theres a few printed pages in the tray."
        jc "\"Luna Bloodgood and the Curse of the Forest.\""
        jc "Looks like a few pages from the start of the book shes been writing."
        jc "I guess its about magic. That explains all the magic related books on the shelves in here i suppose."
    if (res=="bookshelf"):
        jc "Lots of books line the shelves."
        jc "Seems to be various magic reference books and other novels."
        jc "They're packed in pretty tight though, so i don't think ill be able to take any of them off the shelves."
    if (res=="picture"):
        jc "It's 'Art'. Or so Veronica tries to tell me. It just looks like someone spilled a bunch of paint to me."
    if (res=="drawers_left"):
        jc "These drawers seem to be locked."
    if (res=="drawers_right"):
        jc "These drawers are easy enough to open. They're only filled with general office supplies though."
        if Office_MagicInstructionsFound:
            if (not inventory.inventory_hand) or ((inventory.inventory_hand) and (not inventory.inventory_hand[0] == 'Chalk')):
                "Looks like theres some chalk in here too."
                menu:
                  "Should i take some?"
                  "Take the chalk":
                      $inventory.AddItemToHand('Chalk')
                  "Leave it here.":
                      $inventory.AddItemToRoomInventory('Chalk', current_room[0])
    if (res=="desk"):
        jc "It's Veronicas desk. It's pretty tidy. Apart from the computer stuff the only thing on it is a small notepad."
    if (res=="chair"):
        jc "Its an office chair. It looks pretty comfy actually."
    if (res=="notepad"):
        jc "Its a small notepad with some scribbles on it."
        "*Computer Password hint*"
        $Office_ComputerPasswordHint = True
    if (res=="MouseToy"):
        jc "Clawdia's favourite mouse toy. She is rarely ever seen too far from it."
        $ShouldPickUp = True
    if (res=="OfficePen"):
        jc "Looks like theres a few pens here. Nothing special about them, I guess they are spares."
        $ShouldPickUp = True
        
    if (res=="dropItem"):
        $inventory.DropItemFromHand()
        jc "You stay here for a bit Clawdia."
        
    if (res=="callClawdia"):
        if ClawdiaLocation == CurrentRoomName:
            jc "Oh wait, shes already here."
        else:
            jc "I guess she can't hear me."
        
    if ShouldPickUp:
      if inventory.IsItemCollectable(res):
        menu:
          "Take it?"
          "Yes":
            $inventory.AddItemToHand(res)
          "No":
            $inventory.AddItemToRoomInventory(res, current_room[0])
      else:
        jc "I can't take that."
    jump lbl_office_explore
    
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
screen Exploration_Bathroom2:
    add 'bg bathroom2'   
    $roomName = "bathroom2"
    $inventory.SetCurrentRoom(roomName)
    
    if Bathroom2_SinkBlocked:
      use FixedItem(roomName, "water", 0,0)
    else:
      use FixedItem(roomName, "sink", 0,0)
      if not inventory.inventory_hand[0] == 'token_wood' and not Boilerroom_TokenPlaced_wood:
        use FixedItem(roomName, "token_wood", 0,0)
    use FixedItem(roomName, "soap", 0,0)
    use FixedItem(roomName, "mirror", 0,0)
    use FixedItem(roomName, "cupboard", 0,0)
    use FixedItem(roomName, "tap", 0,0)
    
    #use ClickableItem("AllergyMeds", 1200, 450)
    #use ClickableItem("VeronicaHairbrush", 1200, 450)
    
    #In sink
    #use ClickableItem("token_wood", 1200, 450)
    
    if inventory.inventory_hand:
      if not inventory.inventory_hand[0] == 'AllergyMeds':
        use FixedItem(roomName,"AllergyMeds", 0, 0)
      if not inventory.inventory_hand[0] == 'VeronicaHairbrush':
        use FixedItem(roomName,"VeronicaHairbrush", 0, 0)
      if not inventory.inventory_hand[0] == 'MouseToy':
        #use FixedItem(roomName,"AllergyMeds", 0, 0)
        #use FixedItem(roomName,"VeronicaHairbrush", 0, 0)
        if ClawdiaLocation == roomName:
          use FixedItem(roomName,"MouseToy", 0, 0)
    else:
      if ClawdiaLocation == roomName:
        use FixedItem(roomName,"MouseToy", 0, 0)
    
    if NightVision_active:
      if Bathroom2_LightsOff:
        add "images/backgrounds/NightVision.png" 
      else:
        add "images/backgrounds/NightVision_Bright.png" 
    else:
      if Bathroom2_LightsOff:
        add "images/backgrounds/Dark.png"
    
    use Exploration_Navigation 
    use hand_inventory
    use room_inventory(roomName)
    
#-----------------------------------------------------------------------
#---
label ShowBathroom2():
    $CurrentRoomName = "bathroom2"

    #"Show Bathroom2"
    scene bg bathroom2
      
    if inventory.inventory_hand:
        if Bathroom2_SinkBlocked:
            show item_bathroom2_water
        else:
          if not inventory.inventory_hand[0] == 'token_wood' and not Boilerroom_TokenPlaced_wood:
            show item_bathroom2_token_wood
        if not inventory.inventory_hand[0] == 'AllergyMeds':
            show item_bathroom2_AllergyMeds
        if not inventory.inventory_hand[0] == 'VeronicaHairbrush':
            show item_bathroom2_VeronicaHairbrush
        if not inventory.inventory_hand[0] == 'MouseToy':
            if ClawdiaLocation == CurrentRoomName:
                show item_bathroom2_mousetoy
    else:
      #"Show all items"
      show item_bathroom2_AllergyMeds
      show item_bathroom2_VeronicaHairbrush
      if ClawdiaLocation == CurrentRoomName:
        show item_bathroom2_mousetoy
      if not Boilerroom_TokenPlaced_wood:
        show item_bathroom2_token_wood
      
    if inventory.inventory_hand:
      if inventory.inventory_hand[0] == 'MouseToy':
        $ClawdiaLocation = CurrentRoomName
        
    if NightVision_active:
      if Bathroom2_LightsOff:
        show roomeffect nightvision
      else:
        show roomeffect nightvision_bright
    else:
      if Bathroom2_LightsOff:
        show roomeffect dark
        
    return
    
label ShowBathroom2WithChars:
    $CurrentRoomName = "bathroom2"
    call ShowBathroom2
              
    if ClawdiaLocation == CurrentRoomName:
      show jessicaperson neutral:
        yalign -0.5
        xalign 0.7
        
    show jessicat happy at left
    return
#---
label lbl_bathroom2:
     
    #scene bg bathroom2
    #if NightVision_active:
    #  show roomeffect nightvision
    #else:
    #  if Bedroom1_LightsOff:
    #    show roomeffect dark
    call ShowBathroom2WithChars
    jc "Its the Basement Bathroom"
    jc "Lets see what else we can find here..."
    
label lbl_bathroom2_explore:
    call screen Exploration_Bathroom2
    $res = _return
    $ShouldPickUp = False
    call ShowBathroom2WithChars
    
    if res[0] == 'Move':
      $labelname = res[1]
      if config.developer:
        jc "Ok lets go to [labelname]"
      jump expression labelname
      
    if Bathroom2_LightsOff:
      if not NightVision_active:
        "I can't see what that is right now."
        jump lbl_bathroom2_explore
      
    
    jc "Look, its a [res]."
        
    #if (res=="sink_blocked"):
    #    jc "The sink is full of water. Its a little cloudy, i guess from the soap from the last time it was used to wash hands."
    #    "I can't see if theres anything else in the water or not."
    #if (res=="sink_unblocked"):
    #    jc "The sink has been drained."
    #    if (inventory.inventory_hand) and (not inventory.inventory_hand[0] == 'WoodenToken'):
    #        jc "Theres a Wooden Token in here."
    #        if Office_MagicInstructionsFound:
    #          jc "I wonder if this could be used for the spell?"
    #          menu:
    #            "Should i take it?"
    #            "Yes":
    #              $inventory.AddItemToHand('WoodenToken')
    #            "Leave it here.":
    #              $inventory.AddItemToRoomInventory('WoodenToken', current_room[0])
    #        else:
    #          jc "I wonder what this is for, playing checkers maybe?"
    if (res=="tap"):
        jc "Its a tap. It's kinda stiff so im not sure id be able to turn it even if i wanted to."
        if not sink_unblocked:
            jc "Not that i really want to unless im planning on flooding the basement right now."
        else:
            jc "Not that i really want to, after all the trouble i went to to empty the sink out."
    if (res=="cupboard"):
        jc "It's a cupboard. The doors are super stuck though, so theres no chance of me getting them open."
    if (res=="soap"):
        jc "Its Veronicas hand soap. Its got a wierd fruity smell, but i can't quite figure out what fruit exactly."
    if (res=="water"):
        jc "It's a sink. Looks like it's filled with water at the moment."
        jc "Actually it looks like theres something blocking the drain. If i could move it maybe the water would drain away."
        
        menu:
            "Should i try something?"
            "Use the Hairbrush" if (inventory.inventory_hand and (inventory.inventory_hand[0] == 'VeronicaHairbrush')):
                jc "No way. Veronica will 100\% kill me."
            "Use the Hairbrush" if (inventory.inventory_hand and (inventory.inventory_hand[0] == 'JessicaHairbrush')):
                jc "I really don't want to get this wet. Its a good brush."
            "Use the Hairbrush" if (inventory.inventory_hand and (inventory.inventory_hand[0] == 'ClawdiaHairbrush')):
                jc "I really don't want to get this wet. It wasn't cheap."
            "Use the Spoon" if (inventory.inventory_hand and (inventory.inventory_hand[0] == 'Spoon')):
                jc "This could work, its just the right size to reach the bottom of the sink."
                "Jessica manages to get the tip of the spoon wedged under the item blocking the drain. As she starts to push it to one side the water level starts to drop."
                jc "Awesome, it's working."
                "Its not long before the sink is completely drained."
                $Bathroom2_SinkBlocked = False
            "Use the Plunger" if (inventory.inventory_hand and (inventory.inventory_hand[0] == 'Plunger')):
                jc "This could work, after all a plunger is a blocked drains worst enemy!"
                "Jessica manages to get the plunger propped up in the sink, being careful not to touch the water she starts pushing it up and down to \'plunge\'"
                jc "What the heck? Why isn't it working?"
                jc "I guess the plunger only works if the blockage is in the drain itself, but this one seems to be something sitting over the drain, so its not getting flushed away."
                jc "Maybe i should try and see if i can find something to move the blockage enough to let the water out."
            "Use the Toilet Brush" if (inventory.inventory_hand and (inventory.inventory_hand[0] == 'ToiletBrush')):
                jc "Its not working, the bristles don't seem to be moving the blockage and its hard to maneuver it correctly since its so big."
                jc "Maybe i should try something smaller?"
            "Use my paw": 
                if not Bathroom2_TriedPaw:
                    jc "Its not too deep, i should be able to reach it."
                    "Jessica reaches for the water, but as soon as he paw touches the water a huge shiver runs along her spine causing her to jump back and start licking her paw instinctively."
                    jc "YIKES. What the heck was that?"
                    jc "Does Clawdia really dislike water that much? I guess that explains why i get practically mauled every time i try to bathe her."
                    jc "I suppose that means that doing it myself is out then. I'm just gonna need to find some sort of tool to unblock it."
                    $Bathroom2_TriedPaw = True
                else:
                    jc "After last time i really would rather not try that again. Even thinking about it sends shivers up my spine."
            "Nevermind" :
                pass
        
    if (res=="sink"):
        jc "It's a sink. Thankfully its all emptied out now."
    if (res=="mirror"):
        jc "It's a little dustier than the others but its clearly a mirror."
        "Jessica waves her paws in front of the mirror. Her reflection waves back."
        jc "Hi me."
    if (res=="AllergyMeds"):
        jc "A bottle of pills."
        jc "Looks like these are Veronicas allergy meds. I guess she uses these when her allergies get particularly bad."
        $ShouldPickUp = True
    if (res=="token_wood"):
        jc "A wooden token."
        if Office_MagicInstructionsFound:
          jc "I wonder if this could be used for the spell?"
        else:
          jc "Looks like theres a wierd symbol carved on one side of it. I wonder what it means?"
        $ShouldPickUp = True
    if (res=="VeronicaHairbrush"):
        jc "It's Veronicas hairbrush."
        if Office_MagicInstructionsFound:
          jc "Could this be what she used for her version of the spell?"
        $ShouldPickUp = True
    if (res=="MouseToy"):
        jc "Clawdia's favourite mouse toy. She is rarely ever seen too far from it."
        $ShouldPickUp = True
        
    if (res=="dropItem"):
        $inventory.DropItemFromHand()
        jc "You stay here for a bit Clawdia."
        
    if (res=="callClawdia"):
        if ClawdiaLocation == CurrentRoomName:
            jc "Oh wait, shes already here."
        else:
            jc "I guess she can't hear me."
        
    if ShouldPickUp:
      if inventory.IsItemCollectable(res):
        menu:
          "Take it?"
          "Yes":
            $inventory.AddItemToHand(res)
          "No":
            $inventory.AddItemToRoomInventory(res, current_room[0])
      else:
        jc "I can't take that."
    jump lbl_bathroom2_explore
    
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
screen Exploration_Boilerroom:
    add 'bg boilerroom'   
    $roomName = "boilerroom"
    $inventory.SetCurrentRoom(roomName)
    
    if Boilerroom_MagicCircleComplete:
        #add "images/backgrounds/br_circle_complete.png"
        use FixedItem(roomName, "chalkcircle_main_complete", 0,0)
        use FixedItem(roomName, "chalkcircle_part1_complete", 0,0)
        use FixedItem(roomName, "chalkcircle_part2_complete", 0,0)
        use FixedItem(roomName, "chalkcircle_part3_complete", 0,0)
    else:
        #add "images/backgrounds/br_circle_smudge.png"
        use FixedItem(roomName, "chalkcircle_main_smudge", 0,0)
        use FixedItem(roomName, "chalkcircle_part1_smudge", 0,0)
        use FixedItem(roomName, "chalkcircle_part2_smudge", 0,0)
        use FixedItem(roomName, "chalkcircle_part3_smudge", 0,0)
    
    use FixedItem(roomName, "boiler", 0,0)
    #use FixedItem(roomName, "fusebox", 0,0)
    
    use FixedItem(roomName, "shelf", 0,0)
    use FixedItem(roomName, "boxes", 0,0)
    
    use FixedItem(roomName, "candlespace_1_full", 0,0)
    if Boilerroom_Candle2Placed:
        use FixedItem(roomName, "candlespace_2_full", 0,0)
    else:
        use FixedItem(roomName, "candlespace_2_empty", 0,0)
    if Boilerroom_Candle3Placed:
        use FixedItem(roomName, "candlespace_3_full", 0,0)
    else:
        use FixedItem(roomName, "candlespace_3_empty", 0,0)
    use FixedItem(roomName, "candlespace_4_full", 0,0)
    if Boilerroom_Candle5Placed:
        use FixedItem(roomName, "candlespace_5_full", 0,0)
    else:
        use FixedItem(roomName, "candlespace_5_empty", 0,0)
    if Boilerroom_Candle6Placed:
        use FixedItem(roomName, "candlespace_6_full", 0,0)
    else:
        use FixedItem(roomName, "candlespace_6_empty", 0,0)
        
    
    if Boilerroom_CandlesLit:
        use FixedItem(roomName, "candle_flames", 0,0)
    
    
    if Boilerroom_TokenPlaced_gold:
        use FixedItem(roomName, "token_gold", 0,0)
    if Boilerroom_TokenPlaced_silver:
        use FixedItem(roomName, "token_silver", 0,0)
    if Boilerroom_TokenPlaced_bronze:
        use FixedItem(roomName, "token_bronze", 0,0)
    if Boilerroom_TokenPlaced_wood:
        use FixedItem(roomName, "token_wood", 0,0)
    if Boilerroom_HairbrushPlaced_Jessica:
        use FixedItem(roomName, "JessicaHairbrush", 0,0)
    if Boilerroom_HairbrushPlaced_Clawdia:
        use FixedItem(roomName, "ClawdiaHairbrush", 0,0)
    if Boilerroom_IncensePlaced:
        use FixedItem(roomName, "Incense", 0,0)
    #if Boilerroom_MatchesPlaced:
    #    use FixedItem(roomName, "Matches", 0,0)
    
    #use ClickableItem("Candle", 1200, 450)
    
    if inventory.inventory_hand:
      #if not inventory.inventory_hand[0] == 'Candle':
      #  use FixedItem(roomName,"Candle", 0, 0)
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == roomName:
          use FixedItem(roomName,"MouseToy", 0, 0)
      if Boilerroom_MatchesPlaced:
        if not inventory.inventory_hand[0] == 'Matches':
          use FixedItem(roomName,"Matches", 0, 0)
    else:
      #use FixedItem(roomName,"Candle", 0, 0)
      if ClawdiaLocation == roomName:
        use FixedItem(roomName,"MouseToy", 0, 0)
      if Boilerroom_MatchesPlaced:
        use FixedItem(roomName,"Matches", 0, 0)
    
    if NightVision_active:
      if Boilerroom_LightsOff and not Boilerroom_CandlesLit:
        add "images/backgrounds/NightVision.png" 
      else:
        add "images/backgrounds/NightVision_Bright.png" 
    else:
      if Boilerroom_LightsOff and not Boilerroom_CandlesLit:
        add "images/backgrounds/Dark.png"
      if Boilerroom_CandlesLit:
        add "images/backgrounds/Dark_candlelight.png"
        
    
    use Exploration_Navigation 
    use hand_inventory
    use room_inventory(roomName)
    
#-----------------------------------------------------------------------
#---
label ShowBoilerroom():
    $CurrentRoomName = "boilerroom"

    #"Show Boilerroom"
    scene bg boilerroom
    if Boilerroom_MagicCircleComplete:
      show item_boilerroom_circle_complete
    else:
      show item_boilerroom_circle_smudge
      
    if inventory.inventory_hand:
      #if not inventory.inventory_hand[0] == 'Candle':
      #  show item_boilerroom_candle
      if not inventory.inventory_hand[0] == 'MouseToy':
        if ClawdiaLocation == CurrentRoomName:
            show item_boilerroom_mousetoy
      if Boilerroom_MatchesPlaced:
        if not inventory.inventory_hand[0] == 'Matches':
          show item_boilerroom_matches
    else:
      #"Show all items"
      #show item_boilerroom_candle
      if ClawdiaLocation == CurrentRoomName:
        show item_boilerroom_mousetoy
      if Boilerroom_MatchesPlaced:
        show item_boilerroom_matches
      
    #if Boilerroom_Candle1Placed:
    #  show item_boilerroom_candle1
    if Boilerroom_Candle2Placed:
      show item_boilerroom_candle2
    if Boilerroom_Candle3Placed:
      show item_boilerroom_candle3
    #if Boilerroom_Candle4Placed:
    #  show item_boilerroom_candle4
    if Boilerroom_Candle5Placed:
      show item_boilerroom_candle5
    if Boilerroom_Candle6Placed:
      show item_boilerroom_candle6
    
    if Boilerroom_CandlesLit:
      show item_candle_flame
      
    if Boilerroom_TokenPlaced_gold:
      show item_boilerroom_token_gold
    if Boilerroom_TokenPlaced_silver:
      show item_boilerroom_token_silver
    if Boilerroom_TokenPlaced_bronze:
      show item_boilerroom_token_bronze
    if Boilerroom_TokenPlaced_wood:
      show item_boilerroom_token_wood
    if Boilerroom_HairbrushPlaced_Jessica:
      show item_boilerroom_JessicaHairbrush
    if Boilerroom_HairbrushPlaced_Clawdia:
      show item_boilerroom_ClawdiaHairbrush
    if Boilerroom_IncensePlaced:
      show item_boilerroom_incense
        
    if NightVision_active:
      if Boilerroom_LightsOff and not Boilerroom_CandlesLit:
        show roomeffect nightvision
      else:
        show roomeffect nightvision_bright
    else:
      if Boilerroom_LightsOff and not Boilerroom_CandlesLit:
        show roomeffect dark
      if Boilerroom_CandlesLit:
        show roomeffect dark_candlelight
      
    if inventory.inventory_hand:
      if inventory.inventory_hand[0] == 'MouseToy':
        $ClawdiaLocation = CurrentRoomName
        
    return
    
label ShowBoilerroomWithChars:
    $CurrentRoomName = "boiler"
    call ShowBoilerroom
              
    if Spell_Success:
      if ClawdiaLocation == CurrentRoomName:
        show jessicat neutral:
          yalign 0.5
          xalign 0.7
          
      show jessicaperson happy at left:
          yalign -0.5
          xalign 0.0
    else:
      if ClawdiaLocation == CurrentRoomName:
        show jessicaperson neutral:
          yalign -0.5
          xalign 0.7
          
      show jessicat happy at left
    return
#---
label lbl_boilerroom:
    #scene bg boilerroom
    #if NightVision_active:
    #  show roomeffect nightvision
    #else:
    #  if Bedroom1_LightsOff:
    #    show roomeffect dark
    call ShowBoilerroomWithChars
    jc "Its the Boiler room"
    jc "Lets see what else we can find here..."
    
label lbl_boilerroom_explore:
    call screen Exploration_Boilerroom
    $res = _return
    $ShouldPickUp = False
    call ShowBoilerroomWithChars
    
    if res[0] == 'Move':
      $labelname = res[1]
      if config.developer:
        jc "Ok lets go to [labelname]"
      jump expression labelname           
    
    if Boilerroom_LightsOff and not Boilerroom_CandlesLit:
      if not NightVision_active:
        "I can't see what that is right now."
        jump lbl_boilerroom_explore
    
    if not Boilerroom_MagicCircleFound:
        return #lbl_chapter4_Collection
    
    jc "Look, its a [res]."
    
    $candleSetName = ""
    $tokencount = 0
    if Boilerroom_TokenPlaced_gold:
        $tokencount +=1
    if Boilerroom_TokenPlaced_silver:
        $tokencount +=1
    if Boilerroom_TokenPlaced_bronze:
        $tokencount +=1
    if Boilerroom_TokenPlaced_wood:
        $tokencount +=1
    
    #Collection + Circle complete!
    if Boilerroom_MagicCircleComplete and tokencount > 1 and Boilerroom_CandlesLit and Boilerroom_HairbrushPlaced_Jessica and Boilerroom_HairbrushPlaced_Clawdia and Boilerroom_IncensePlaced:
        jc "Ok, it looks like everything is set up for the spell now."
        return  #lbl_chapter4_MagicSpell
        
    
    if (res=="boiler"):
        jc "Its the boiler. I don't think i can do anything useful with it right now."
    if ("chalkcircle_main" in res):#center circle
        if Boilerroom_MagicCircleComplete:
          jc "Looks like the circle is complete."
          jc "This rune looks like RUNE DESCRIPTION HERE"
        else:
          jc "Looks like the circle is incomplete."
          jc "This part looks smudged"          
    if ("chalkcircle_part1" in res): #top circle
        if Boilerroom_MagicCircleComplete:
          jc "Looks like the circle is complete."
          jc "This rune looks like RUNE DESCRIPTION HERE"
        else:
          jc "Looks like the circle is incomplete."
          jc "This part looks smudged"  
    if ("chalkcircle_part2" in res):#right circle
        if Boilerroom_MagicCircleComplete:
          jc "Looks like the circle is complete."
          jc "This rune looks like RUNE DESCRIPTION HERE"
        else:
          jc "Looks like the circle is incomplete."
          jc "This part looks smudged"  
    if ("chalkcircle_part3" in res):#left circle
        if Boilerroom_MagicCircleComplete:
          jc "Looks like the circle is complete."
          jc "This rune looks like RUNE DESCRIPTION HERE"
        else:
          jc "Looks like the circle is incomplete."
          jc "This part looks smudged"  
    if ("chalkcircle" in res):   
        if not Boilerroom_MagicCircleComplete:
            if inventory.inventory_hand:
              if Inventory_active == 'HeldItem':
                if inventory.inventory_hand[0] == 'Chalk': 
                  "In thoery i should be able to use this chalk to redraw the symbols and fix the magic circle."              
                  "*Magic Circle Puzzle*"    
                  call puzzle_start()
                  if Boilerroom_MagicCircleComplete:
                    jc "Now that that is complete i just have to finish gathering everything else and ill be good to go."  
                    $inventory.EmptyHand()
                  else: 
                    jc "I just can't figure it out. Maybe i should re-check Veronicas notes again?"
            
        if inventory.inventory_hand:
          if Inventory_active == 'HeldItem':
            if inventory.inventory_hand and inventory.inventory_hand[0] == 'token_gold': 
                jc "Ok, i've brought a Token for the spell. I should leave it here for now."
                $Boilerroom_TokenPlaced_gold = True
                $inventory.EmptyHand()
            if inventory.inventory_hand and inventory.inventory_hand[0] == 'token_silver': 
                jc "Ok, i've brought a Token for the spell. I should leave it here for now."
                $Boilerroom_TokenPlaced_silver = True
                $inventory.EmptyHand()
            if inventory.inventory_hand and inventory.inventory_hand[0] == 'token_bronze': 
                jc "Ok, i've brought a Token for the spell. I should leave it here for now."
                $Boilerroom_TokenPlaced_bronze = True
                $inventory.EmptyHand()
            if inventory.inventory_hand and inventory.inventory_hand[0] == 'token_wood': 
                jc "Ok, i've brought a Token for the spell. I should leave it here for now."
                $Boilerroom_TokenPlaced_wood = True
                $inventory.EmptyHand()
            if inventory.inventory_hand and inventory.inventory_hand[0] == 'JessicaHairbrush': 
                jc "Ok, i've brought my hairbrush for the spell. This should make a good catalyst. I should leave it here for now."
                $Boilerroom_HairbrushPlaced_Jessica = True
                $inventory.EmptyHand()
            if inventory.inventory_hand and inventory.inventory_hand[0] == 'ClawdiaHairbrush': 
                jc "Ok, i've brought clawdias hairbrush for the spell. This should make a good catalyst. I should leave it here for now."
                $Boilerroom_HairbrushPlaced_Clawdia = True
                $inventory.EmptyHand()
            if inventory.inventory_hand and inventory.inventory_hand[0] == 'Incense': 
                jc "Ok, i've brought the incense for the spell. I should leave it here for now."
                $Boilerroom_IncensePlaced = True
                $inventory.EmptyHand()
    if ("candlespace_1" in res):
        jc "Theres a candle here."
        jc "I should leave it alone for now."
        #if Boilerroom_Candle1Placed:
        #  jc "Theres a candle here."
        #  jc "I should leave it alone for now."
        #else:
        #  jc "Based on the wax marks on the floor there should be a candle here."
        #  if Inventory_active == 'HeldItem':
        #    if (inventory.inventory_hand) and (inventory.inventory_hand[0] == 'Candle'):
        #        jc "Lets try placing this candle here."
        #        $Boilerroom_Candle1Placed =  True
        #        $inventory.EmptyHand()
    if ("candlespace_2" in res):
        if Boilerroom_Candle2Placed:
          jc "Theres a candle here."
          jc "I should leave it alone for now."
        else:
          jc "Based on the wax marks on the floor there should be a candle here."
          if Inventory_active == 'HeldItem':
            if (inventory.inventory_hand) and ('candle' in inventory.inventory_hand[0]):
                jc "Lets try placing this candle here."
                $Boilerroom_Candle2Placed =  True
                $candleSetName = inventory.inventory_hand[0]
                $inventory.EmptyHand()
    if ("candlespace_3" in res):
        if Boilerroom_Candle3Placed:
          jc "Theres a candle here."
          jc "I should leave it alone for now."
        else:
          jc "Based on the wax marks on the floor there should be a candle here."
          if Inventory_active == 'HeldItem':
            if (inventory.inventory_hand) and ('candle' in inventory.inventory_hand[0]):
                jc "Lets try placing this candle here."
                $Boilerroom_Candle3Placed =  True
                $candleSetName = inventory.inventory_hand[0]
                $inventory.EmptyHand()
    if ("candlespace_4" in res):
        jc "Theres a candle here."
        jc "I should leave it alone for now."
    if ("candlespace_5" in res):
        if Boilerroom_Candle5Placed:
          jc "Theres a candle here."
          jc "I should leave it alone for now."
        else:
          jc "Based on the wax marks on the floor there should be a candle here."
          if Inventory_active == 'HeldItem':
            if (inventory.inventory_hand) and ('candle' in inventory.inventory_hand[0]):
                jc "Lets try placing this candle here."
                $Boilerroom_Candle5Placed =  True
                $candleSetName = inventory.inventory_hand[0]
                $inventory.EmptyHand()
    if ("candlespace_6" in res):
        if Boilerroom_Candle6Placed:
          jc "Theres a candle here."
          jc "I should leave it alone for now."
        else:
          jc "Based on the wax marks on the floor there should be a candle here."
          if Inventory_active == 'HeldItem':
            if (inventory.inventory_hand) and ('candle' in inventory.inventory_hand[0]):
                jc "Lets try placing this candle here."
                $Boilerroom_Candle6Placed =  True
                $candleSetName = inventory.inventory_hand[0]
                $inventory.EmptyHand()
    if ("candlespace" in res):
        if (inventory.inventory_hand) and (inventory.inventory_hand[0] == 'Matches'):
            if Boilerroom_Candle1Placed and Boilerroom_Candle2Placed and Boilerroom_Candle3Placed and Boilerroom_Candle4Placed and Boilerroom_Candle5Placed and Boilerroom_Candle6Placed:
                jc "Now that call the candles are in place i can light them."
                jc "With all this fur, playing with fire seems like a terrible idea, but i dont have much choice, so ill just have to be careful."
                "Carefully striking up a match for each candle, Jessica lights each one in turn, making sure to be extra careful not to singe any of Clawdias fur on the flames."
                $Boilerroom_CandlesLit = True
                show item_candle_flame
                jc "Phew, managed to get through that without setting myself on fire. Now i just have to be careful when walking around here too."
            else:
                jc "I should wait untill all the candles are in place before i try lighting them."
                jc "I could just leave the matches here though since i know im going to need them later."
                jc "Would save me having to go looking for them again."
                menu:
                    "Leave the matches here?"
                    "Yes":
                        $Boilerroom_MatchesPlaced = True
                        "Jessica sets the matches in the back of the room so she can easily find them again later."
                        $inventory.EmptyHand()
                    "No":
                        pass
        if candleSetName == "candle_bedroom1":
            $Boilerroom_Bedroom1CandlePlaced = True
        if candleSetName == "candle_bedroom2":
            $Boilerroom_Bedroom2CandlePlaced = True
        if candleSetName == "candle_livingroom1":
            $Boilerroom_Livingroom1CandlePlaced = True
        if candleSetName == "candle_basement":
            $Boilerroom_BasementCandlePlaced = True
            
            
    if (res=="candle_flames"):
        jc "The flickering of the flames on the candles is kindof hypnotic."
        jc "I better steer clear of them though, I want to avoid getting singed."
    if (res=="shelf"):
        jc "There are a lot of smaller boxes on these shelves."
        jc "Doesn't seem to be anything useful here."
    if (res=="boxes"):
        jc "More boxes. No idea whats in them, some of them have words written on them."
        jc "I don't think i can open any of them. They're all taped up pretty good."
    #if (res=="Candle"):
    #    jc "..."
    #    #$ShouldPickUp = True
    if (res=="MouseToy"):
        jc "Clawdia's favourite mouse toy. She is rarely ever seen too far from it."
        $ShouldPickUp = True
    if (res=="Matches"):
        jc "It's the matches i left here earlier."
        $ShouldPickUp = True
        
    if (res=="dropItem"):
        $inventory.DropItemFromHand()
        jc "You stay here for a bit Clawdia."
        
    if (res=="callClawdia"):
        if ClawdiaLocation == CurrentRoomName:
            jc "Oh wait, shes already here."
        else:
            jc "I guess she can't hear me."
        
    if ShouldPickUp:
      if inventory.IsItemCollectable(res):
        menu:
          "Take it?"
          "Yes":
            $inventory.AddItemToHand(res)
          "No":
            $inventory.AddItemToRoomInventory(res, current_room[0])
      else:
        jc "I can't take that."
    jump lbl_boilerroom_explore
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------