
init python:
    #-----------------------------------------------------------------------------------
    def CreateLiveCompositeChimera(_character="sam", _emotion="", _mouth="", _extra=""):    
      
      #Initial values
      charWidth = 773
      charHeight = 602
      xoff = 0
      yoff = -98
      type = "snake"
      extra = _extra
      emotion = _emotion
      
      if extra == "":
        extra = "blank"
      if _emotion == "":
        _emotion = "blank"
      if _mouth == "":
        _mouth = "mouthClosed"
      if _emotion == "love":
        _mouth = "mouthLove"
      
      ### Character Adjusts ###
      #Adjust for specific characters
      if _character == "sam":
        type = "snake"
        _mouth = "blank"
      if _character == "leo":
        type = "lion"
        if _emotion == "love":
          emotion = "excited"
      if _character == "gor":
        type = "goat"
          
        
      ### Live Composite function ###
      return LiveComposite( 
      (charWidth, charHeight),
      #(0, 0), "images/sprites/composite/chimera/ChimeraBodyBase.png",
      (xoff, yoff), "images/sprites/composite/chimera/%s_base.png"%(type),
      (xoff, yoff), "images/sprites/composite/chimera/%s_%s.png"%(type, emotion),
      (xoff, yoff), "images/sprites/composite/chimera/%s_%s.png"%(type, _mouth),
      (xoff, yoff), "images/sprites/composite/chimera/%s_%s.png"%(type, extra))   
      
    #-----------------------------------------------------------------------
    def CreateLiveCompositeGirl(_character="mel", _emotion="", _mouth="", _extra=""):    
      
      #Initial values
      charWidth = 531
      charHeight = 700
      type = "medusa"
      extra = _extra
      emotion = _emotion
      mouth = _mouth
      
      if extra == "":
        extra = "blank"
      if _emotion == "":
        _emotion = "blank"
      if _mouth == "":
        mouth = "mouthDull"
      if _emotion == "sad":
        mouth = "mouthSad"
      if _emotion == "dull":
        mouth = "mouthDull"
      if _emotion == "happy":
        mouth = "mouthHappy"
        
      if _mouth == "sad":
        mouth = "mouthSad"
      if _mouth == "dull":
        mouth = "mouthDull"
      if _mouth == "happy":
        mouth = "mouthHappy"
        
      
      ### Character Adjusts ###
      #Adjust for specific characters
      if _character == "mel":
        type = "medusa"
      if _character == "hel":
        type = "harpy"
        mouth = "blank"
        if extra == "blush":
          extra = "blushHarpy"
      if _character == "pea":
        type = "human"
          
        
      ### Live Composite function ###
      return LiveComposite( 
      (charWidth, charHeight),
      #(0, 0), "images/sprites/composite/chimera/ChimeraBodyBase.png",
      (0, 0), "images/sprites/composite/girls/%s_base.png"%(type),
      (0, 0), "images/sprites/composite/girls/%s.png"%(emotion),
      (0, 0), "images/sprites/composite/girls/%s.png"%(mouth),
      (0, 0), "images/sprites/composite/girls/%s.png"%(extra))   
      
    #-----------------------------------------------------------------------
# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    define slow_dissolve = Dissolve(1.0)
    
    # background images and CG
    image bg forest day = "images/bg/bg_forest_day2.png"
    image bg shop day = "images/bg/bg_shop_day2.png"
    image bg home day = "images/bg/bg_home_day2.png"
    image bg street day = "images/bg/bg_street_day2.png"
    image bg bakery day = "images/bg/bg_bakery_day2.png"
    image bg lake day = "images/bg/bg_lake_day2.png"
    image bg library day = "images/bg/bg_library_day2.png"
    image bg black = Solid("#000000")
    image GOOD_END = "images/GOOD_END.png"
    
    # Music and SFX
    
    #$music_enchantedValley = "audio/Enchanted_Valley.ogg"
    
    $music_gameshop = "audio/Magical Full.ogg"
    $music_bakery   = "audio/Quircky Shop.ogg"
    $music_home     = "audio/Evans.ogg"
    $music_park     = "audio/Time for Rest.ogg"
    $music_library  = "audio/Relax.ogg"
    $music_fight  = "audio/Fight On Main.ogg"
    
    
    $sound_ambient = "audio/Store Ambience 2.wav"
    $sound_ui_confirm = "audio/UI Simple Confirm.wav"
    $sound_ui_cancel = "audio/UI Simple Cancel.wav"
    $sound_ui_select = "audio/UI Simple Select.wav"
    
    $sound_transition_sad = "audio/Piano Jingle 3.ogg"
    $sound_transition_happy = "audio/Transition 1.ogg"
    # InGame Flags and Variables
    
    $bLionHelped = False
    $bGoatHelped = False
    $bMatchLion = False
    $bMatchGoat = False
    $bMatchSnake = False
    
    $iPoints = 0
    $bMarrage = False
    $bBakery = False
    $iMovie = 0
    $bLoveMovieFlag = False
    
    # Declare characters used by this game.
    define s = Character('Samuel', color="#66b95e", window_left_padding=0, image="Chimera")
    define l = Character('Leonardo', color="#c0c446", window_left_padding=0, image="Chimera")
    define g = Character('Gordon', color="#416680", window_left_padding=0, image="Chimera")
    define m = Character('Melissa', color="#51ad99", window_left_padding=0, image="medusa")
    define h = Character('Helen', color="#e0922e", window_left_padding=0, image="harpy")
    define p = Character('Persephone', color="#f4e8d8", window_left_padding=0, image="human")
    define shopkeep = Character('Shopkeeper', color="#b5a164", window_left_padding=0, image="shopkeep")
    define f = Character('The Father', color="#902b2b", window_left_padding=0, image="father")
    
    #$player_name = "???"
    #define dynamic = Character("player_name", dynamic=True)
    #-----------------------------------------------------------------------
    image ChimeraBase = "images/sprites/composite/chimera/ChimeraBodyBase2.png"
    image ChimeraBase Up = "images/sprites/composite/chimera/ChimeraBodyBase2.png"
    image Girls = "images/sprites/Girls.png"
    #-----------------------------------------------------------------------
    image sam happy = CreateLiveCompositeChimera("sam", "happy")
    image sam love = CreateLiveCompositeChimera("sam", "love")
    image sam mad = CreateLiveCompositeChimera("sam", "mad")
    image sam excited = CreateLiveCompositeChimera("sam", "excited")
    image sam sad = CreateLiveCompositeChimera("sam", "sad")
    image sam embarrassed = CreateLiveCompositeChimera("sam", "embarassed", "", "blush")
    image sam dull = CreateLiveCompositeChimera("sam", "dull")
    image sam shock = CreateLiveCompositeChimera("sam", "shock")
    image sam pissed = CreateLiveCompositeChimera("sam", "pissed")
    image sam skeptic = CreateLiveCompositeChimera("sam", "skeptic")
    
    #-----------------------------------------------------------------------
    image leo happy = CreateLiveCompositeChimera("leo", "happy")
    image leo love = CreateLiveCompositeChimera("leo", "love")
    image leo mad = CreateLiveCompositeChimera("leo", "mad", "", "anger")
    image leo excited = CreateLiveCompositeChimera("leo", "excited")
    image leo sad = CreateLiveCompositeChimera("leo", "dull")
    image leo embarrassed = CreateLiveCompositeChimera("leo", "embarassed", "", "blush")
    image leo skeptic = CreateLiveCompositeChimera("leo", "embarassed")
    image leo sleep = CreateLiveCompositeChimera("leo", "dull", "", "sleeping")
    image leo dull = CreateLiveCompositeChimera("leo", "dull")
    image leo pissed = CreateLiveCompositeChimera("leo", "pissed")
    image leo shock = CreateLiveCompositeChimera("leo", "happy", "mouthShock", "shock")
    
    #-----------------------------------------------------------------------
    image gor happy = CreateLiveCompositeChimera("gor", "happy")
    image gor love = CreateLiveCompositeChimera("gor", "love")
    image gor mad = CreateLiveCompositeChimera("gor", "mad")
    #image gor excited = CreateLiveCompositeChimera("gor", "excited")
    image gor sad = CreateLiveCompositeChimera("gor", "dull")
    image gor embarrassed = CreateLiveCompositeChimera("gor", "embarassed", "", "blush")
    image gor skeptic = CreateLiveCompositeChimera("gor", "embarassed")
    image gor sleep = CreateLiveCompositeChimera("gor", "dull", "", "sleeping")
    image gor dull = CreateLiveCompositeChimera("gor", "dull")
    image gor pissed = CreateLiveCompositeChimera("gor", "pissed")
    image gor shock = CreateLiveCompositeChimera("gor", "happy", "mouthShock", "shock")
    
    #-----------------------------------------------------------------------
    #-----------------------------------------------------------------------
    
    image melissa happy = CreateLiveCompositeGirl("mel", "happy")
    image melissa sad = CreateLiveCompositeGirl("mel", "happy", "sad")
    image melissa neutral = CreateLiveCompositeGirl("mel", "happy", "dull")
    image melissa pissed = CreateLiveCompositeGirl("mel", "dull", "dull", "anger")
    image melissa mad = CreateLiveCompositeGirl("mel", "embarassed", "sad", "anger")
   #image melissa excited = CreateLiveCompositeGirl("mel", "happy")
    image melissa content = CreateLiveCompositeGirl("mel", "dull", "happy", "blush")
    image melissa embarrassed = CreateLiveCompositeGirl("mel", "embarassed", "dull", "blush")
    image melissa love = CreateLiveCompositeGirl("mel", "embarassed", "happy", "blush")
    image melissa upset = CreateLiveCompositeGirl("mel", "embarassed", "sad")
    image melissa skeptic = CreateLiveCompositeGirl("mel", "embarassed", "dull", "")
    image melissa dull = CreateLiveCompositeGirl("mel", "dull", "happy", "")
    image melissa coy = CreateLiveCompositeGirl("mel", "embarassed", "happy", "")
    
    #-----------------------------------------------------------------------
    
    image helen happy = CreateLiveCompositeGirl("hel", "happy")
    image helen sad = CreateLiveCompositeGirl("hel", "happy", "sad")
    image helen neutral = CreateLiveCompositeGirl("hel", "happy", "dull")
    image helen pissed = CreateLiveCompositeGirl("hel", "dull", "dull", "anger")
    image helen mad = CreateLiveCompositeGirl("hel", "embarassed", "sad", "anger")
   #image helen excited = CreateLiveCompositeGirl("hel", "happy")
    image helen content = CreateLiveCompositeGirl("hel", "dull", "happy", "blush")
    image helen embarrassed = CreateLiveCompositeGirl("hel", "embarassed", "dull", "blush")
    image helen love = CreateLiveCompositeGirl("hel", "embarassed", "happy", "blush")
    image helen upset = CreateLiveCompositeGirl("hel", "embarassed", "sad")
    image helen skeptic = CreateLiveCompositeGirl("hel", "embarassed", "dull", "")
    image helen dull = CreateLiveCompositeGirl("hel", "dull", "happy", "")
    image helen coy = CreateLiveCompositeGirl("hel", "embarassed", "happy", "")
    
    #-----------------------------------------------------------------------
    
    image pea happy = CreateLiveCompositeGirl("pea", "happy")
    image pea sad = CreateLiveCompositeGirl("pea", "happy", "sad")
    image pea neutral = CreateLiveCompositeGirl("pea", "happy", "dull")
    image pea pissed = CreateLiveCompositeGirl("pea", "dull", "dull", "anger")
    image pea mad = CreateLiveCompositeGirl("pea", "embarassed", "sad", "anger")
   #image pea excited = CreateLiveCompositeGirl("pea", "happy")
    image pea content = CreateLiveCompositeGirl("pea", "dull", "happy", "blush")
    image pea embarrassed = CreateLiveCompositeGirl("pea", "embarassed", "dull", "blush")
    image pea love = CreateLiveCompositeGirl("pea", "embarassed", "happy", "blush")
    image pea upset = CreateLiveCompositeGirl("pea", "embarassed", "sad")
    image pea skeptic = CreateLiveCompositeGirl("pea", "embarassed", "dull", "")
    image pea dull = CreateLiveCompositeGirl("pea", "dull", "happy", "")
    image pea coy = CreateLiveCompositeGirl("pea", "embarassed", "happy", "")
    
    #-----------------------------------------------------------------------
    #-----------------------------------------------------------------------
    
    image photo medusa = im.FactorScale("images/Medusa_photo.png", .8, .8)
    image shopkeep happy = "images/sprites/Cyclops_happy.png"
    image father happy = "images/sprites/father_happy.png"
    image father mad = "images/sprites/father_mad.png"
    
    #-----------------------------------------------------------------------
