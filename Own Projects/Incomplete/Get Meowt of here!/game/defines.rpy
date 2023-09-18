#### Lip flap code
init python:
  
    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None
  
    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None
  
    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)
  
    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))
  
    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking
       
        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None
  
    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)
    
    
init python:
    #-----------------------------------------------------------------------------------
    def CreateLiveCompositeJesssicat(_character="Jessicat", _ears="", _eyes="", _mouth="", _whiskers="", _tail="", _extra=""):    
      
      #Initial values
      charWidth = 0
      charHeight = 0
      xoffset = 0
      yoffset = 0
      extra = _extra
      lipflap = "jessicat mouth normal"
      closedMouth = "images/sprites/Jessicat/Jessicat_mouth_%s.png"%(_mouth)
      blinkTime = renpy.random.randint(2,7)
      
      if extra == "":
        extra = "blank"
      
      ### Character Adjusts ###
      #Adjust for specific characters
      if _character == "Jessicat":
        charWidth = 297
        charHeight = 363
        
      eyes = "jessicat eyes normal"
      if _eyes == "1":
        eyes = "jessicat eyes normal"
      if _eyes == "2":
        eyes = "jessicat eyes angry"
      if _eyes == "3":
        eyes = "jessicat eyes closed happy"
      if _eyes == "4":
        eyes = "jessicat eyes closed"
        
      if _mouth == "2":
        lipflap = "jessicat mouth normal"
        closedMouth = "images/sprites/Jessicat/Jessicat_mouth_1.png"
        
      if _mouth == "3":
        lipflap = "jessicat mouth big"
        closedMouth = "images/sprites/Jessicat/Jessicat_mouth_1.png"
          
        
      ### Live Composite function ###
      return LiveComposite( 
      (charWidth, charHeight),
      (0, 0), "images/sprites/%s/%s_body.png"%(_character, _character),
      (xoffset, yoffset), "images/sprites/Jessicat/Jessicat_tail_%s.png"%(_tail),
      (xoffset, yoffset), "images/sprites/Jessicat/Jessicat_ears_%s.png"%(_ears),
      (xoffset, yoffset),  eyes,
      (xoffset, yoffset), WhileSpeaking("Jessicat", lipflap, closedMouth),
      (xoffset, yoffset), "images/sprites/Jessicat/Jessicat_whiskers_%s.png"%(_whiskers),
      (xoffset, yoffset), "images/sprites/Jessicat/Jessicat_extra_%s.png"%(extra))   
      
    #-----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------
    def CreateLiveCompositeJesssicaperson(_character="Jessicaperson", _body="", _eyes="", _mouth="", _extra=""):    
      
      #Initial values
      charWidth = 0
      charHeight = 0
      xoffset = 0
      yoffset = 0
      extra = _extra
      lipflap = "jessicaperson mouth1 neutral"
      closedMouth = "images/sprites/Jessicaperson/mouth%s_%s.png"%(_body, _mouth)
      blinkTime = renpy.random.randint(2,7)
      
      if extra == "":
        extra = "blank"
      
      ### Character Adjusts ###
      #Adjust for specific characters
      if _character == "Jessicaperson":
        charWidth = 292
        charHeight = 1013
        
      eyes = 'jessicaperson eyes ' + _eyes
      #if _eyes == "1":
      #  eyes = "jessicat eyes normal"
      #if _eyes == "2":
      #  eyes = "jessicat eyes angry"
        
      #if _mouth == "neutral":
      #  lipflap = "jessicaperson mouth1 neutral"
      #  closedMouth = "images/sprites/Jessicaperson/Jessicat_mouth_1.png"
      #  
      #if _mouth == "3":
      #  lipflap = "jessicat mouth big"
      #  closedMouth = "images/sprites/Jessicaperson/Jessicat_mouth_1.png"
          
        
      ### Live Composite function ###
      return LiveComposite( 
      (charWidth, charHeight),
      (0, 0), "images/sprites/%s/Jessica_base%s.png"%(_character, _body),
      (xoffset, yoffset),  eyes,
      (xoffset, yoffset), WhileSpeaking("Jessicaperson", lipflap, closedMouth),
      #(xoffset, yoffset),  Animation( "images/sprites/Jessicaperson/eyes_%s.png"%(_eyes), 
      #                                renpy.random.randint(10,50)*0.1,
      #                                "images/sprites/Jessicaperson/eyes_closed.png", 0.25),
      (xoffset, yoffset), "images/sprites/Jessicaperson/Jessica_hair.png",
      (xoffset, yoffset), "images/sprites/Jessicaperson/extra_%s.png"%(extra))   
      
    #-----------------------------------------------------------------------
    
    
init:  
    
    #misc defines
    define slow_dissolve = Dissolve(1.0)
    define pawwipe = ImageDissolve("gui/wipes/paws4.png", 2.0)
    
    define logodissolve = MultipleTransition([
    False, ImageDissolve("gui/wipes/paws4.png", 1.5),
    "gui/logoscreen.png", Pause(0.5),
    "gui/logoscreen.png", ImageDissolve("gui/wipes/paws5b.png", 1.5),
    True])
    
    define inventory_hand = []

    define inventory_basement1 = []
    define inventory_basement2 = []
    define inventory_bathroom1 = []
    define inventory_bathroom2 = []
    define inventory_bedroom1 = []
    define inventory_bedroom2 = []
    define inventory_boilerroom = []
    define inventory_hallway = []
    define inventory_kitchen = []
    define inventory_livingroom1 = []
    define inventory_livingroom2 = []
    define inventory_office = []    
  
    define List_AllItems = []           
    define room_unknown = []  
    define room_basement1 = []
    define room_basement2 = []
    define room_bathroom1 = []
    define room_bathroom2 = []
    define room_bedroom1 = []
    define room_bedroom2 = []
    define room_boilerroom = []
    define room_hallway = []
    define room_kitchen = []
    define room_livingroom1 = []
    define room_livingroom2 = []
    define room_office = []  
    define List_AllRooms = []

    #Misc Variables
    default chapter_section = "Escape Room"
    default chapter_number = "1"
    #default chapter_subtitle = "Some Most Unusual Bandits"
    
    #Inventory Variables
    $Inventory_HeldItem_unlocked = False
    $Inventory_CatEyes_unlocked = False
    $Inventory_CatNose_unlocked = False
    $Inventory_CatMouth_unlocked = False
    $Inventory_CatClaw_unlocked = False
    $Inventory_active = ''
    
    $Inventory_HeldItem_active = False
    #$Inventory_CatEyes_active = False
    $Inventory_CatNose_active = False
    $Inventory_CatMouth_active = False
    $Inventory_CatClaw_active = False
    $NightVision_active = False

    ## Global story variables ##
    $ClawdiaLocation = 'bedroom1'
    $CurrentRoomName = 'bedroom1'
    
    $current_room = []#room_bedroom1
    
    #Introduction
    $Bedroom1_ClawdiaAwake = True
    $Bedroom1_CollectionsActive = False
    $Bedroom1_Intro_MirrorUsed = False
    $Bedroom1_Intro_BlanketUsed = False
    
    #Escape bedroom 1
    $SeenTutorial_ItemUse = False
    $Bedroom1_DoorLocked = True
    $Bedroom1_SideTableLocked = True
    $Bedroom1_LightsOff = False
    $Bedroom1_DoorYarnHint = False
    $Bedroom1_DoorHandleYarn = False
    $Bedroom1_MouseToyHint = False
    
    #Hallway
    $Hallway_LightsOff = False
    $Hallway_Bedroom2DoorUnlocked = False
    $Hallway_BroomMoved = False
    $BrightVisionEncountered = False
    
    #Bedroom2
    $Bedroom2_LightsOff = False
    $Bedroom2_JournalRead = False
    $Bedroom2_FanTurned = False
    $baconCandleStorySeen = False
    
    #Bathroom1
    $Bathroom1_LightsOff = True
    
    #Bathroom2
    $Bathroom2_LightsOff = True
    $Bathroom2_SinkBlocked = True
    $Bathroom2_TriedPaw = False
    
    #Livingroom1
    $Livingroom1_LightsOff = False
    $Livingroom1_PhoneCallHappened = False
    $combination_lock_result = [2,5,7]
    $combination_lock_number_1 = 0
    $combination_lock_number_2 = 0
    $combination_lock_number_3 = 0
    
    #Livingroom2
    $Livingroom2_LightsOff = False
    $Livingroom2_BasementDoorUnlocked = False
    $Livingroom2_BoxesArranged = False
    $Livingroom2_BoxesKnockedOver = False
    $Livingroom2_LargeBoxPosition = 1
    $Livingroom2_MediumBoxPosition = 1
    $Livingroom2_SmallBoxPosition = 1
    
    #Basement1
    $Basement1_LightsOff = True
    $Basement1_Arrival = False
    $Basement1_SpiderMet = False
    $Basement1_SpiderAlive = True
    
    #Basement2
    $Basement2_LightsOff = False
    $Basement2_OfficeDoorUnlocked = False
    $Basement2_Bathroom2DoorUnlocked = False
    $Basement2_BoilerroomDoorUnlocked = False
    
    #Kitchen
    $Kitchen_LightsOff = False
    $Kitchen_CupboardDoorClosed = False
    $Kitchen_TokenRetrieved = False
    $Kitchen_ListFound = False
    
    #Office
    $Office_LightsOff = True
    $Office_ComputerPasswordHint = False
    $Office_ComputerUnlocked = False
    $Office_MagicInstructionsFound = False
    $Office_ComputerPassword = "5eronica"
    
    #Boilerroom
    $Boilerroom_LightsOff = True
    $Boilerroom_MagicCircleFound = False
    $Boilerroom_MagicCircleComplete = False
    
    $Boilerroom_Candle1Placed = True
    $Boilerroom_Candle2Placed = False
    $Boilerroom_Candle3Placed = False
    $Boilerroom_Candle4Placed = True
    $Boilerroom_Candle5Placed = False
    $Boilerroom_Candle6Placed = False
    $Boilerroom_CandlesLit = False
    
    $Boilerroom_TokenPlaced_gold = False
    $Boilerroom_TokenPlaced_silver = False
    $Boilerroom_TokenPlaced_bronze = False
    $Boilerroom_TokenPlaced_wood = False
    
    $Boilerroom_HairbrushPlaced_Jessica = False
    $Boilerroom_HairbrushPlaced_Clawdia = False
    $Boilerroom_IncensePlaced = False
    $Boilerroom_MatchesPlaced = False
    
    $Boilerroom_Bedroom1CandlePlaced = False
    $Boilerroom_Bedroom2CandlePlaced = False
    $Boilerroom_Livingroom1CandlePlaced = False
    $Boilerroom_BasementCandlePlaced = False
    
    $Spell_Success = False
    #Reusable script parts:
    
    $List_MirrorJokes = [
      "Mirror mirror on the wall, who's the furriest of them all?",
      "Time to reflect on my life so far...",
      "Think I would enjoy working as a mirror cleaner. It’s just something I could really see myself doing.",
      "Yep. I'm still a cat.",
      "I can see myself. I may be a cat but at least i'm not a vampire.",
      "You know mirror, i see a lot of myself in you."]

    # Declare characters used by this game. The color argument colorizes the
    # name of the character.

    #Test chars
    define e = Character("Eileen")
    define c = Character("Jessicat", callback=speaker("Jessicat"))
    
    #Characters
    define jp = Character("Jessica", callback=speaker("Jessicaperson"))
    define jc = Character("Jessicat", callback=speaker("Jessicat"), what_prefix="( ", what_suffix=" )")

    define cc = Character("Clawdia", callback=speaker("Jessicat"))
    define cp = Character("Clawdia", callback=speaker("Jessicaperson"))
    
    define v = Character("Victoria", callback=speaker("Victoria"))
    
    define qqq = Character("???", callback=speaker("Jessicat"))
    define qq = Character("???", callback=speaker("Jessicaperson"))
    
    define journal = Character(None, kind=nvl)
    
    #Test chars
    image mc angry = "images/cat_angry.png"
    image mc angry small = "images/cat_angry_small.png"
    
    image mp neutral = "images/sprites/Jessicaperson/risa_casual_kyu-kyu-nya.png"
    
    #Characters
    
    #UI
    image chapter_screen = "gui/overlay/chapter_menu.png"
    
    #Backgrounds
    image bg black = Solid("#000000")   
    image bg room = "images/room_afternoon_light_off.jpg"
    image bg bedroom1 = "images/backgrounds/bedroom1.png"
    image bg bedroom1 dark = "images/backgrounds/bedroom1_dark.png"
    image bg bedroom1 nightvision = "images/backgrounds/bedroom1_nv.png"
    
    image bg bedroom1 = "images/backgrounds/bedroom1.png"
    image bg bedroom2 = "images/backgrounds/bedroom2.png"
    image bg hallway = "images/backgrounds/hallway.png"
    image bg bathroom1 = "images/backgrounds/bathroom1.png"
    image bg bathroom2 = "images/backgrounds/bathroom2.png"
    image bg livingroom1 = "images/backgrounds/livingroom1.png"
    image bg livingroom2 = "images/backgrounds/livingroom2.png"
    image bg kitchen = "images/backgrounds/kitchen.png"
    image bg basement1 = "images/backgrounds/basement1.png"
    image bg basement2 = "images/backgrounds/basement2.png"
    image bg office = "images/backgrounds/office.png"
    image bg office_computer = "images/backgrounds/office_computer_base.png"
    image office_computer_locked = "images/backgrounds/office_computer_locked.png"
    image office_computer_unlocked = "images/backgrounds/office_computer_unlocked.png"
    image magic_circle = "images/backgrounds/magiccircle.png"
    image sigil y4 = "images/minigame/MagicCircle/Sigil2_drag.png"
    image sigil se = "images/minigame/MagicCircle/Sigil1_drag.png"
    image sigil plant = "images/minigame/MagicCircle/Sigil3_drag.png"
    image sigil deer = "images/minigame/MagicCircle/Sigil4_drag.png"
    
    image bg boilerroom = "images/backgrounds/boilerroom.png"
    
    image roomeffect nightvision = "images/backgrounds/NightVision.png" 
    image roomeffect dark = "images/backgrounds/Dark.png" 
    image roomeffect nightvision_bright = "images/backgrounds/NightVision_bright.png" 
    image roomeffect dark_candlelight = "images/backgrounds/Dark_candlelight.png" 
    
    ######### ITEM IMAGE DEFINES #############
    #test items
    image item unknown = "images/items/items_unknown_idle.png"
    image item globe =   "images/items/items_unknown_idle.png"
    image item clock =   "images/items/items_unknown_idle.png"
    image item fan =     "images/items/items_unknown_idle.png"
    image item book =    "images/items/items_unknown_idle.png"
    #Bedroom 1 items
    #image item candle = "images/items/items_candle_idle.png"
    #image item lazerpen = "images/items/items_lazerpen_idle.png"
    #image item mousetoy = "images/items/items_mousetoy_idle.png"
    #image item pencil = "images/items/items_pencil_idle.png"
    #image item yarnball = "images/items/items_yarnball_idle.png"
    
    image item candle = "images/items/icons/items_candle.png"
    image item lazerpen = "images/items/icons/items_lazerpen.png"
    image item mousetoy = "images/items/icons/items_mousetoy.png"
    image item pencil = "images/items/icons/items_pencil.png"
    image item yarnball = "images/items/icons/items_yarnball.png"
    
    image item candle_small = im.FactorScale("images/items/icons/items_candle.png", 0.5, 0.5)
    image item lazerpen_small = im.FactorScale("images/items/icons/items_lazerpen.png", 0.5, 0.5)
    image item mousetoy_small = im.FactorScale("images/items/icons/items_mousetoy.png", 0.5, 0.5)
    image item pencil_small = im.FactorScale("images/items/icons/items_pencil.png", 0.5, 0.5)
    image item yarnball_small = im.FactorScale("images/items/icons/items_yarnball.png", 0.5, 0.5)
    
    image item_bedroom1_candle = "images/items/bedroom1/bedroom1_candle_bedroom1.png"
    image item_bedroom1_mousetoy = "images/items/bedroom1/bedroom1_mousetoy.png"
    image item_bedroom1_pencil = "images/items/bedroom1/bedroom1_pencil.png"
    image item_bedroom1_yarnhandle = "images/items/bedroom1/bedroom1_yarnhandle.png"
    
    image item blanket = "images/items/bedroom1/bedroom1_bed.png"
    image item blanket bump = "images/items/bedroom1/bedroom1_bed_bump.png"
  
    #Bedroom 2 items
    #image item vpen = "images/items/items_unknown_idle.png" 
    image item vpen = "images/items/icons/items_pen_victoria.png" 
    
    image item vpen_small = im.FactorScale("images/items/icons/items_pen_victoria.png" , 0.5, 0.5)
    
    image item_bedroom2_vpen ="images/items/bedroom2/bedroom2_vpen.png"
    image item_bedroom2_mousetoy = "images/items/bedroom2/bedroom2_mousetoy.png"
    image item_bedroom2_fan_forward = "images/items/bedroom2/bedroom2_fan_forward.png"
    image item_bedroom2_fan_turn = "images/items/bedroom2/bedroom2_fan_turn.png"
    
    #Bathroom 1 items
    #image item token_silver = "images/items/items_unknown_idle.png"
    #image item jessicahairbrush = "images/items/items_unknown_idle.png"
    image item token_silver = "images/items/icons/items_token_silver.png"
    image item jessicahairbrush = "images/items/icons/items_hairbrush_jessica.png"
    image item toiletbrush = "images/items/icons/items_toiletbrush.png"
    image item plunger = "images/items/icons/items_plunger.png"
    
    image item token_silver_small = im.FactorScale("images/items/icons/items_token_silver.png", 0.5, 0.5)
    image item jessicahairbrush_small = im.FactorScale("images/items/icons/items_hairbrush_jessica.png", 0.5, 0.5)
    image item toiletbrush_small = im.FactorScale("images/items/icons/items_toiletbrush.png", 0.5, 0.5)
    image item plunger_small = im.FactorScale("images/items/icons/items_plunger.png", 0.5, 0.5)
    
    image item_bathroom1_mousetoy = "images/items/bathroom1/bathroom1_mousetoy.png"
    image item_bathroom1_token_silver = "images/items/bathroom1/bathroom1_token_silver.png"
    image item_bathroom1_JessicaHairbrush = "images/items/bathroom1/bathroom1_JessicaHairbrush.png"
    
    #Hallway
    image item_hallway_mousetoy = "images/items/hallway/hallway_mousetoy.png"
    image item_hallway_broom_normal = "images/items/hallway/hallway_broom_normal.png"
    image item_hallway_broom_pushed = "images/items/hallway/hallway_broom_pushed.png"
    
    #Livingroom1
    #image item phone = "images/items/items_unknown_idle.png"
    #image item clawdiabrush = "images/items/items_unknown_idle.png"
    #image item candle = "images/items/items_unknown_idle.png"
    image item phone = "images/items/icons/items_phone.png"
    image item clawdiahairbrush = "images/items/icons/items_hairbrush_clawdia.png"
    image item candle_livingroom = "images/items/icons/items_candle.png"
    image item pen_sofa = "images/items/icons/items_pen_sofa.png"
    image item token_bronze = "images/items/icons/items_token_bronze.png"
    
    image item phone_small = im.FactorScale("images/items/icons/items_phone.png", 0.5, 0.5)
    image item clawdiahairbrush_small = im.FactorScale("images/items/icons/items_hairbrush_clawdia.png", 0.5, 0.5)
    image item candle_livingroom_small = im.FactorScale("images/items/icons/items_candle.png", 0.5, 0.5)
    image item pen_sofa_small = im.FactorScale("images/items/icons/items_pen_sofa.png", 0.5, 0.5)
    image item token_bronze_small = im.FactorScale("images/items/icons/items_token_bronze.png", 0.5, 0.5)
    
    image item_livingroom1_mousetoy = "images/items/livingroom1/livingroom1_mousetoy.png" 
    image item_livingroom1_Phone = "images/items/livingroom1/livingroom1_phone.png"
    image item_livingroom1_ClawdiaBrush = "images/items/livingroom1/livingroom1_ClawdiaHairbrush.png"
    image item_livingroom1_Candle = "images/items/livingroom1/livingroom1_candle_livingroom1.png"
    
    #Livingroom2
    image item_livingroom2_mousetoy = "images/items/livingroom2/livingroom2_mousetoy.png" 
    image item_livingroom2_box_large =   "images/items/livingroom2/livingroom2_box_large.png"
    image item_livingroom2_box_med_1 =   "images/items/livingroom2/livingroom2_box_med_1.png"
    image item_livingroom2_box_med_2 =   "images/items/livingroom2/livingroom2_box_med_2.png"
    image item_livingroom2_box_med_3 =   "images/items/livingroom2/livingroom2_box_med_3.png"
    image item_livingroom2_box_small_1 = "images/items/livingroom2/livingroom2_box_small_1.png"
    image item_livingroom2_box_small_2 = "images/items/livingroom2/livingroom2_box_small_2.png"
    image item_livingroom2_box_small_3 = "images/items/livingroom2/livingroom2_box_small_3.png"
    
    #kitchen
    #image item spoon = "images/items/items_unknown_idle.png"
    #image item magnets = "images/items/items_unknown_idle.png"
    #image item token_gold = "images/items/items_unknown_idle.png"
    image item spoon = "images/items/icons/items_spoon.png"
    image item magnets = "images/items/icons/items_magnet.png"
    image item token_gold = "images/items/icons/items_token_gold.png"
    image item veronicaskeys = "images/items/icons/items_VeronicasKeys.png"
    
    image item spoon_small = im.FactorScale("images/items/icons/items_spoon.png", 0.5, 0.5)
    image item magnets_small = im.FactorScale("images/items/icons/items_magnet.png", 0.5, 0.5)
    image item token_gold_small = im.FactorScale("images/items/icons/items_token_gold.png", 0.5, 0.5)
    image item veronicaskeys_small = im.FactorScale("images/items/icons/items_VeronicasKeys.png", 0.5, 0.5)
    
    image item_kitchen_mousetoy = "images/items/kitchen/kitchen_mousetoy.png" 
    image item_kitchen_cupboardOpen = "images/items/kitchen/kitchen_cupboards_door.png"
    image item_kitchen_spoon = "images/items/kitchen/kitchen_spoon.png"
    image item_kitchen_magnets = "images/items/kitchen/kitchen_magnets.png"
    image item_kitchen_magnets_loose = "images/items/kitchen/kitchen_magnets_loose.png"
    image item_kitchen_fridge_under = "images/items/kitchen/kitchen_fridge_under.png"
    
    #Basement1
    image item_basement1_mousetoy = "images/items/basement1/basement1_mousetoy.png" 
    image item_basement1_spider = "images/items/basement1/basement1_spider.png"
    
    #Basement2
    image item_basement2_mousetoy = "images/items/basement2/basement2_mousetoy.png" 
    
    #Office
    image item_office_mousetoy = "images/items/office/office_mousetoy.png" 
    image item_office_pen = "images/items/office/office_OfficePen.png" 
    
    image item office_pen = "images/items/icons/items_pen_office.png"
    image item chalk = "images/items/icons/items_chalk.png" 
    
    image item office_pen_small = im.FactorScale("images/items/icons/items_pen_office.png", 0.5, 0.5)
    image item chalk_small = im.FactorScale("images/items/icons/items_chalk.png", 0.5, 0.5)
    
    #Boilerroom
    image item_boilerroom_mousetoy = "images/items/boilerroom/boilerroom_mousetoy.png"     
    image item_boilerroom_circle_complete = "images/backgrounds/br_circle_complete.png"
    image item_boilerroom_circle_smudge = "images/backgrounds/br_circle_smudge.png"
    #image item_boilerroom_candle1 = "images/items/items_unknown_idle.png"
    image item_boilerroom_candle2 = "images/items/boilerroom/boilerroom_candlespace_2_full.png"
    image item_boilerroom_candle3 = "images/items/boilerroom/boilerroom_candlespace_3_full.png"
    #image item_boilerroom_candle4 = "images/items/boilerroom/boilerroom_candlespace_4_full.png"
    image item_boilerroom_candle5 = "images/items/boilerroom/boilerroom_candlespace_5_full.png"
    image item_boilerroom_candle6 = "images/items/boilerroom/boilerroom_candlespace_6_full.png"    
    image item_candle_flame = "images/items/boilerroom/boilerroom_candle_flames.png"
    
    image item_boilerroom_token_gold = "images/items/boilerroom/boilerroom_token_gold.png"
    image item_boilerroom_token_silver = "images/items/boilerroom/boilerroom_token_silver.png"
    image item_boilerroom_token_bronze = "images/items/boilerroom/boilerroom_token_bronze.png"
    image item_boilerroom_token_wood = "images/items/boilerroom/boilerroom_token_wood.png"
    image item_boilerroom_JessicaHairbrush = "images/items/boilerroom/boilerroom_JessicaHairbrush.png"
    image item_boilerroom_ClawdiaHairbrush = "images/items/boilerroom/boilerroom_ClawdiaHairbrush.png"
    image item_boilerroom_incense = "images/items/boilerroom/boilerroom_incense.png"
    
    image circle empty = "images/minigame/MagicCircle/circle_empty.png"
    image circle complete = "images/minigame/MagicCircle/circle_complete_noglow.png"
    image circle complete_glow = "images/minigame/MagicCircle/circle_complete_glow.png"
    
    image item_boilerroom_incense = "images/items/boilerroom/boilerroom_incense.png"
    image item_boilerroom_matches = "images/items/boilerroom/boilerroom_matches.png"
    
    image item incense = "images/items/icons/items_incense.png"
    image item matches = "images/items/icons/items_matches.png"
    #image item sofapen = "images/items/icons/items_pen_sofa.png"
    
    image item incense_small = im.FactorScale("images/items/icons/items_incense.png", 0.5, 0.5)
    image item matches_small = im.FactorScale("images/items/icons/items_matches.png", 0.5, 0.5)
    #image item sofapen_small = im.FactorScale("images/items/icons/items_pen_sofa.png", 0.5, 0.5)
    
    #Bathroom2
    #image item allergymeds = "images/items/items_unknown_idle.png"
    #image item veronicahairbrush = "images/items/items_unknown_idle.png"
    #image item token_wood = "images/items/items_unknown_idle.png"
    image item allergymeds = "images/items/icons/items_pills.png"
    image item veronicahairbrush = "images/items/icons/items_hairbrush_veronica.png"
    image item token_wood = "images/items/icons/items_token_wood.png"
    
    image item allergymeds_small = im.FactorScale("images/items/icons/items_pills.png", 0.5, 0.5)
    image item veronicahairbrush_small = im.FactorScale("images/items/icons/items_hairbrush_veronica.png", 0.5, 0.5)
    image item token_wood_small = im.FactorScale("images/items/icons/items_token_wood.png", 0.5, 0.5)
    
    image item_bathroom2_water = "images/items/bathroom2/bathroom2_water.png" 
    image item_bathroom2_token_wood = "images/items/bathroom2/bathroom2_token_wood.png" 
    image item_bathroom2_mousetoy = "images/items/bathroom2/bathroom2_mousetoy.png" 
    image item_bathroom2_AllergyMeds = "images/items/bathroom2/bathroom2_AllergyMeds.png"
    image item_bathroom2_VeronicaHairbrush = "images/items/bathroom2/bathroom2_VeronicaHairbrush.png"
    
    ######### AUDIO DEFINES #############
    $music_LoungeLizard = "audio/music/Lounge Lizard.mp3"
    $music_MouseTrap = "audio/music/Mouse Trap.mp3"
    $music_OnTheProwl = "audio/music/On The Prowl.mp3"
    $music_SlowlyCreeping = "audio/music/Slowly Creeping.mp3"    
    
    ######### CHARACTER IMAGE DEFINES #############
    
    #-----------------------------------------------------------------------
    ### Jessicat lipflap ###
    
    image jessicat mouth normal:
        "images/sprites/Jessicat/Jessicat_mouth_2.png"
        choice:
          .1
        choice:
          .2
        choice:
          .3
        "images/sprites/Jessicat/Jessicat_mouth_1.png"
        choice:
          .1
        choice:
          .2
        choice:
          .3
        repeat
        
    image jessicat mouth big:
        "images/sprites/Jessicat/Jessicat_mouth_3.png"
        choice:
          .1
        choice:
          .2
        choice:
          .3
        "images/sprites/Jessicat/Jessicat_mouth_1.png"
        choice:
          .1
        choice:
          .2
        choice:
          .3
        repeat
    
    ### Jessicat eye blink ###
    image jessicat eyes closed happy = "images/sprites/Jessicat/Jessicat_eyes_3.png"
    image jessicat eyes closed = "images/sprites/Jessicat/Jessicat_eyes_4.png"
    image jessicat eyes normal:
      "images/sprites/Jessicat/Jessicat_eyes_1.png"
      choice:
          4.5
      choice:
          3.5
      choice:
          1.5
      # This randomizes the time between blinking.
      "images/sprites/Jessicat/Jessicat_eyes_4.png"
      .25
      repeat
    
    image jessicat eyes angry:
      "images/sprites/Jessicat/Jessicat_eyes_2.png"
      choice:
          4.5
      choice:
          3.5
      choice:
          1.5
      # This randomizes the time between blinking.
      "images/sprites/Jessicat/Jessicat_eyes_4.png"
      .25
      repeat
    
    ### Jessicat Emotions ###
    
    #(name, ears, eyes, mouth, whiskers, tail, extra)
    image jessicat neutral =  CreateLiveCompositeJesssicat('Jessicat' , "1", "1" , "4" , "1", "1", "")
    image jessicat angry =  CreateLiveCompositeJesssicat('Jessicat' , "1", "2" , "3" , "2", "2", "shock")    
    image jessicat happy =  CreateLiveCompositeJesssicat('Jessicat' , "1", "1" , "2" , "1", "1", "")
    image jessicat sad =  CreateLiveCompositeJesssicat('Jessicat' , "2", "4" , "4" , "1", "1", "")
    
    
    #----------------------------------------------------------------------- 
    
    ### Jessica person lipflap ###
    image jessicaperson mouth1 neutral:
        choice:
          "images/sprites/Jessicaperson/mouth1_open.png"        
          choice:
            .1
          choice:
            .2
          choice:
            .3
        choice:
          "images/sprites/Jessicaperson/mouth1_open-smile.png"
          choice:
            .1
          choice:
            .2
          choice:
            .3
        "images/sprites/Jessicaperson/mouth1_neutral.png"
        choice:
          .1
        choice:
          .2
        choice:
          .3
        repeat
        
    ### Jessica person blink ###      
    image jessicaperson eyes closed = "images/sprites/Jessicaperson/eyes_closed.png"
    
    image jessicaperson eyes neutral:
      "images/sprites/Jessicaperson/eyes_neutral.png"
      choice:
          4.5
      choice:
          3.5
      choice:
          1.5
      # This randomizes the time between blinking.
      "images/sprites/Jessicaperson/eyes_closed.png"
      .25
      repeat
    
    image jessicaperson eyes angry:
      "images/sprites/Jessicaperson/eyes_neutral.png"
      choice:
          4.5
      choice:
          3.5
      choice:
          1.5
      # This randomizes the time between blinking.
      "images/sprites/Jessicaperson/eyes_closed.png"
      .25
      repeat      
    
    image jessicaperson eyes confused:
      "images/sprites/Jessicaperson/eyes_neutral.png"
      choice:
          4.5
      choice:
          3.5
      choice:
          1.5
      # This randomizes the time between blinking.
      "images/sprites/Jessicaperson/eyes_closed.png"
      .25
      repeat
      
    image jessicaperson eyes surprised:
      "images/sprites/Jessicaperson/eyes_neutral.png"
      choice:
          4.5
      choice:
          3.5
      choice:
          1.5
      # This randomizes the time between blinking.
      "images/sprites/Jessicaperson/eyes_closed.png"
      .25
      repeat      
    
    image jessicaperson eyes worried:
      "images/sprites/Jessicaperson/eyes_neutral.png"
      choice:
          4.5
      choice:
          3.5
      choice:
          1.5
      # This randomizes the time between blinking.
      "images/sprites/Jessicaperson/eyes_closed.png"
      .25
      repeat
    
      
    ### Jessica person Emotions ###
    #image jessicaperson neutral = "images/sprites/Jessicaperson/JessicaPlaceholder.png" 
    image jessicaperson neutral =  CreateLiveCompositeJesssicaperson('Jessicaperson' , "1", "neutral" , "neutral" , "")
    image jessicaperson happy =  CreateLiveCompositeJesssicaperson('Jessicaperson' , "1", "neutral" , "cat-smile" , "")
    image jessicaperson asleep =  CreateLiveCompositeJesssicaperson('Jessicaperson' , "1", "closed" , "neutral" , "")
    
    image jessicaperson unconcious =  CreateLiveCompositeJesssicaperson('Jessicaperson' , "1", "closed" , "pout" , "")
    image jessicaperson yawn =  CreateLiveCompositeJesssicaperson('Jessicaperson' , "1", "closed" , "open-smile" , "")
    image jessicaperson surprised =  CreateLiveCompositeJesssicaperson('Jessicaperson' , "1", "neutral" , "open" , "")
    image jessicaperson confused =  CreateLiveCompositeJesssicaperson('Jessicaperson' , "1", "confused" , "pout" , "")