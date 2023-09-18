init python:
    #-------------------------------------------------------------------------------------------------------------------
    def CreateLiveComposite(_character="Merona", _emotion="", _outfit="", _mouthOpen="", _extra=""):    
      
      #Initial values
      charWidth = 0
      charHeight = 0
      xoffset = 0
      yoffset = 0
      characterLetter = ""
      hair = ""
      extra=_extra
      mouthOpen1 = _mouthOpen
      mouthOpen2 = _mouthOpen
      blinkTime = renpy.random.randint(2,7)
      
      ### Expresssion Adjusts ###
      #Adjust for eye left expression
      if _mouthOpen == "_EL":
        mouthOpen1 = "_EL"
        mouthOpen2 = ""
      if _mouthOpen == "_EL_OM":
        mouthOpen1 = "_EL_OM"
        mouthOpen2 = "_OM"
        
      #Adjust for eye right expression
      if _mouthOpen == "_ER":
        mouthOpen1 = "_ER"
        mouthOpen2 = ""
        
      #Adjust for closed eyes expression
      if _mouthOpen == "_CE":
        mouthOpen1 = "_CE"
        mouthOpen2 = ""
      #Adjust for closed eyes expression
      if _mouthOpen == "_OM_CE":
        mouthOpen1 = "_OM_CE"
        mouthOpen2 = "_OM"
      
      #Adjust for no extra part
      if extra == "":
        extra = "blank"
      
      ### Character Adjusts ###
      #Adjust for specific characters
      if _character == "Merona":
        characterLetter = "M"
        charWidth = 579
        charHeight = 949
        hair = "_u"
      
      if _character == "Boyen":
        characterLetter = "B"
        charWidth = 519
        charHeight = 873
      
      if _character == "Cimaria":
        characterLetter = "C"
        charWidth = 336
        charHeight = 929      
      
      if _character == "Duran":
        characterLetter = "D"
        charWidth = 340
        charHeight = 805
        
      if _character == "Kreita":
        characterLetter = "K"
        charWidth = 470
        charHeight = 898
        if _outfit == "_map":
          xoffset = 70
          yoffset = 0
        
      if _character == "Lexan":
        characterLetter = "L"
        charWidth = 589
        charHeight = 1000
        
      if _character == "Prowen":
        characterLetter = "P"
        charWidth = 576
        charHeight = 950
        if _outfit == "_nony":
          hair = "_nony"
    
      if _character == "Rett":
        characterLetter = "R"
        charWidth = 497
        charHeight = 966
      
      if _character == "Ranan":
        characterLetter = "RA"
        charWidth = 312
        charHeight = 879
        if _outfit == "_past":
          #charWidth = 373
          hair = "_past"
          xoffset = 40
          yoffset = 0
        
      if _character == "Wriane":
        characterLetter = "W"
        charWidth = 815
        charHeight = 1076
        extra = "outlines"
        
      if _character == "Voya":
        characterLetter = "V"
        charWidth = 509
        charHeight = 1003
        
      if _character == "Drae":
        characterLetter = "DR"
        charWidth = 910
        charHeight = 1050
        
      ### Live Composite function ###
      if _outfit == "_fishAnimated":        
        return LiveComposite( 
        (charWidth, charHeight),
        (0, 0), Animation(  "img/sprites/%s/%s_body_fish.png"%(_character, _character), 0.2,
                            "img/sprites/%s/%s_body_fish2.png"%(_character, _character), 0.2,
                            "img/sprites/%s/%s_body_fish.png"%(_character, _character), 0.2,
                            "img/sprites/%s/%s_body_fish2.png"%(_character, _character), 0.2,
                            "img/sprites/%s/%s_body_fish.png"%(_character, _character), 2.0) ,
        (xoffset, yoffset),  Animation( "img/sprites/%s/%s_%s%s.png"%(_character, characterLetter, _emotion, mouthOpen1), blinkTime,
                            "img/sprites/%s/%s_%s%s_CE.png"%(_character, characterLetter, _emotion, mouthOpen2), 0.2),
        (xoffset, yoffset), "img/sprites/%s/%s_hair%s.png"%(_character, _character, hair),
        (xoffset, yoffset), "img/sprites/%s/%s_%s.png"%(_character, _character, extra))        
      else:
        return LiveComposite( 
        (charWidth, charHeight),
        (0, 0), "img/sprites/%s/%s_body%s.png"%(_character, _character, _outfit),
        (xoffset, yoffset),  Animation( "img/sprites/%s/%s_%s%s.png"%(_character, characterLetter, _emotion, mouthOpen1), blinkTime,
                            "img/sprites/%s/%s_%s%s_CE.png"%(_character, characterLetter, _emotion, mouthOpen2), 0.2),
        (xoffset, yoffset), "img/sprites/%s/%s_hair%s.png"%(_character, _character, hair),
        (xoffset, yoffset), "img/sprites/%s/%s_%s.png"%(_character, _character, extra))   
      
    #-------------------------------------------------------------------------------------------------------------------
    
    
init:
    ######### CHARACTER IMAGE DEFINES #############
    
    ### Merona Emotions ###
    
    image merona angry =  CreateLiveComposite('Merona' , "angry" , "_u" , "", "")
    image merona angry CE =  CreateLiveComposite('Merona' , "angry" , "_u" , "_CE", "")
    image merona angry OM =  CreateLiveComposite('Merona' , "angry" , "_u" , "_OM", "")
    image merona blushSmile = CreateLiveComposite('Merona' , "blushSmile" , "_u" , "", "")
    image merona blushSmile OM = CreateLiveComposite('Merona' , "blushSmile" , "_u" , "_OM", "")
    image merona confused = CreateLiveComposite('Merona' , "confused" , "_u" , "", "")
    image merona confused OM = CreateLiveComposite('Merona' , "confused" , "_u" , "_OM", "")
    image merona content = CreateLiveComposite('Merona' , "content" , "_u" , "", "")
    image merona content OM = CreateLiveComposite('Merona' , "content" , "_u" , "_OM", "")
    image merona desperate = CreateLiveComposite('Merona' , "desperate" , "_u" , "", "")
    image merona desperate OM = CreateLiveComposite('Merona' , "desperate" , "_u" , "_OM", "")
    image merona determined = CreateLiveComposite('Merona' , "determined" , "_u" , "", "")
    image merona determined OM = CreateLiveComposite('Merona' , "determined" , "_u" , "_OM", "")
    image merona determinedGrin = CreateLiveComposite('Merona' , "determinedGrin" , "_u" , "", "")
    image merona disappointed = CreateLiveComposite('Merona' , "disappointed" , "_u" , "", "")
    image merona disappointed OM =  CreateLiveComposite('Merona' , "disappointed" , "_u" , "_OM", "")
    image merona embarrassed = CreateLiveComposite('Merona' , "embarrassed" , "_u" , "", "")
    image merona embarrassed EL = CreateLiveComposite('Merona' , "embarrassed" , "_u" , "_EL", "")
    image merona embarrassed OM = CreateLiveComposite('Merona' , "embarrassed" , "_u" , "_OM", "")
    image merona embarrassedSmile = CreateLiveComposite('Merona' , "embarrassedSmile" , "_u" , "", "")
    image merona embarrassedSmile OM = CreateLiveComposite('Merona' , "embarrassedSmile" , "_u" , "_OM", "")
    image merona eyesRight = CreateLiveComposite('Merona' , "grin" , "_u" , "_ER", "")
    image merona grin = CreateLiveComposite('Merona' , "grin" , "_u" , "", "")
    image merona grin EL = CreateLiveComposite('Merona' , "grin" , "_u" , "_EL", "")
    image merona grin ER = CreateLiveComposite('Merona' , "grin" , "_u" , "_ER", "")
    image merona happy = CreateLiveComposite('Merona' , "happy" , "_u" , "", "")
    image merona laugh = CreateLiveComposite('Merona' , "laugh" , "_u" , "", "")
    image merona nervous = CreateLiveComposite('Merona' , "nervous" , "_u" , "", "")
    image merona nervous OM = CreateLiveComposite('Merona' , "nervous" , "_u" , "_OM", "")
    image merona neutral = CreateLiveComposite('Merona' , "content" , "_u" , "", "") #TODO: neutral as content?
    image merona neutral OM = CreateLiveComposite('Merona' , "content" , "_u" , "_OM", "") #TODO: neutral as content?
    image merona reflective = CreateLiveComposite('Merona' , "reflective" , "_u" , "", "")
    image merona sad = CreateLiveComposite('Merona' , "sad" , "_u" , "", "")
    image merona sad OM = CreateLiveComposite('Merona' , "sad" , "_u" , "_OM", "")
    image merona sadSmile = CreateLiveComposite('Merona' , "sadSmile" , "_u" , "", "")
    image merona sadSmile OM = CreateLiveComposite('Merona' , "sadSmile" , "_u" , "", "")
    image merona sadSmile Tears = CreateLiveComposite('Merona' , "sadSmile_tears" , "_u" , "", "")
    image merona scared = CreateLiveComposite('Merona' , "scared" , "_u" , "", "")
    image merona serious = CreateLiveComposite('Merona' , "serious" , "_u" , "", "")
    image merona serious OM = CreateLiveComposite('Merona' , "serious" , "_u" , "_OM", "")
    image merona shocked = CreateLiveComposite('Merona' , "shocked" , "_u" , "", "")
    image merona shocked OM = CreateLiveComposite('Merona' , "shocked" , "_u" , "_OM", "")
    image merona sleepy = CreateLiveComposite('Merona' , "sleepy" , "_u" , "", "")
    image merona surprised = CreateLiveComposite('Merona' , "surprised" , "_u" , "", "")
    image merona surprised OM = CreateLiveComposite('Merona' , "surprised" , "_u" , "_OM", "")
    image merona surprisedBlush = CreateLiveComposite('Merona' , "surprisedBlush" , "_u" , "", "")
    image merona surprisedBlush OM = CreateLiveComposite('Merona' , "surprisedBlush" , "_u" , "_OM", "")
    image merona sweaty = CreateLiveComposite('Merona' , "sweaty" , "_u" , "", "")
    image merona sweaty laugh = CreateLiveComposite('Merona' , "sweaty_laugh" , "_u" , "", "")
    image merona sweaty OM = CreateLiveComposite('Merona' , "sweaty" , "_u" , "_OM", "")
    image merona verySad = CreateLiveComposite('Merona' , "verySad" , "_u" , "", "")
    image merona verySad OM = CreateLiveComposite('Merona' , "verySad" , "_u" , "_OM", "")
    image merona veryScared = CreateLiveComposite('Merona' , "veryScared" , "_u" , "", "")
    image merona veryWorried = CreateLiveComposite('Merona' , "veryWorried" , "_u" , "", "")
    image merona veryWorried OM = CreateLiveComposite('Merona' , "veryWorried" , "_u" , "_OM", "")
    image merona wink = CreateLiveComposite('Merona' , "wink" , "_u" , "", "")
    image merona wink OM = CreateLiveComposite('Merona' , "wink" , "_u" , "_OM", "")
    image merona worried =  CreateLiveComposite('Merona' , "worried" , "_u" , "", "")
    image merona worried CE =  CreateLiveComposite('Merona' , "worried" , "_u" , "_CE", "")
    image merona worried OM =  CreateLiveComposite('Merona' , "worried" , "_u" , "_OM", "")
    
    image merona determined CE = CreateLiveComposite('Merona' , "determined" , "_u" , "_CE", "")
    image merona disappointed OM CE = CreateLiveComposite('Merona' , "disappointed" , "_u" , "_OM_CE", "")
    image merona embarrassed CE = CreateLiveComposite('Merona' , "embarrassed" , "_u" , "_CE", "")
    image merona grin CE = CreateLiveComposite('Merona' , "grin" , "_u" , "_CE", "")
    image merona nervous CE = CreateLiveComposite('Merona' , "nervous" , "_u" , "_CE", "")
    
    image merona serious CE = CreateLiveComposite('Merona' , "serious" , "_u" , "_CE", "")
    image merona sleepy CE = CreateLiveComposite('Merona' , "sleepy" , "_u" , "_CE", "")
    image merona surprised OM CE = CreateLiveComposite('Merona' , "surprised" , "_u" , "_OM_CE", "")
    image merona worried CE = CreateLiveComposite('Merona' , "worried" , "_u" , "_CE", "")
    
    # flashback version
    image meronaflashback scared = CreateLiveComposite('Merona' , "scared" , "_u" , "", "")
    
    ##Travel Outfit##
    image merona t angry =  CreateLiveComposite('Merona' , "angry" , "_t" , "", "hat")
    image merona t angry CE =  CreateLiveComposite('Merona' , "angry" , "_t" , "_CE", "hat")
    image merona t angry OM =  CreateLiveComposite('Merona' , "angry" , "_t" , "_OM", "hat")
    image merona t blushSmile = CreateLiveComposite('Merona' , "blushSmile" , "_t" , "", "hat")
    image merona t blushSmile OM = CreateLiveComposite('Merona' , "blushSmile" , "_t" , "_OM", "hat")
    image merona t confused = CreateLiveComposite('Merona' , "confused" , "_t" , "", "hat")
    image merona t confused OM = CreateLiveComposite('Merona' , "confused" , "_t" , "_OM", "hat")
    image merona t content = CreateLiveComposite('Merona' , "content" , "_t" , "", "hat")
    image merona t content OM = CreateLiveComposite('Merona' , "content" , "_t" , "_OM", "hat")
    image merona t content CE = CreateLiveComposite('Merona' , "content" , "_t" , "_CE", "hat")
    image merona t desperate = CreateLiveComposite('Merona' , "desperate" , "_t" , "", "hat")
    image merona t desperate OM = CreateLiveComposite('Merona' , "desperate" , "_t" , "_OM", "hat")
    image merona t determined = CreateLiveComposite('Merona' , "determined" , "_t" , "", "hat")
    image merona t determined OM = CreateLiveComposite('Merona' , "determined" , "_t" , "_OM", "hat")
    image merona t determinedGrin = CreateLiveComposite('Merona' , "determinedGrin" , "_t" , "", "hat")
    image merona t determinedGrin OM = CreateLiveComposite('Merona' , "determinedGrin" , "_t" , "_OM", "hat")
    image merona t disappointed = CreateLiveComposite('Merona' , "disappointed" , "_t" , "", "hat")
    image merona t disappointed OM =  CreateLiveComposite('Merona' , "disappointed" , "_t" , "_OM", "hat")
    image merona t disappointed OM CE =  CreateLiveComposite('Merona' , "disappointed" , "_t" , "_OM_CE", "hat")
    image merona t embarrassed = CreateLiveComposite('Merona' , "embarrassed" , "_t" , "", "hat")
    image merona t embarrassed EL = CreateLiveComposite('Merona' , "embarrassed" , "_t" , "_EL", "hat")
    image merona t embarrassed OM = CreateLiveComposite('Merona' , "embarrassed" , "_t" , "_OM", "hat")
    image merona t embarrassedSmile = CreateLiveComposite('Merona' , "embarrassedSmile" , "_t" , "", "hat")
    image merona t embarrassedSmile OM= CreateLiveComposite('Merona' , "embarrassedSmile" , "_t" , "_OM", "hat")
    image merona t eyesRight = CreateLiveComposite('Merona' , "grin" , "_t" , "_ER", "hat")
    image merona t grin = CreateLiveComposite('Merona' , "grin" , "_t" , "", "hat")
    image merona t happy = CreateLiveComposite('Merona' , "happy" , "_t" , "", "hat")
    image merona t laugh = CreateLiveComposite('Merona' , "laugh" , "_t" , "", "hat")
    image merona t nervous = CreateLiveComposite('Merona' , "nervous" , "_t" , "", "hat")
    image merona t nervous OM = CreateLiveComposite('Merona' , "nervous" , "_t" , "_OM", "hat")
    image merona t neutral = CreateLiveComposite('Merona' , "content" , "_t" , "", "hat") #TODO: neutral as content?
    image merona t neutral OM = CreateLiveComposite('Merona' , "content" , "_t" , "_OM", "hat") #TODO: neutral as content?
    image merona t noGloves content = CreateLiveComposite('Merona' , "content" , "_t_noGloves" , "", "hat")
    image merona t noGloves content OM = CreateLiveComposite('Merona' , "content" , "_t_noGloves" , "_OM", "hat")
    image merona t reflective = CreateLiveComposite('Merona' , "reflective" , "_t" , "", "hat")
    image merona t sad = CreateLiveComposite('Merona' , "sad" , "_t" , "", "hat")
    image merona t sad OM = CreateLiveComposite('Merona' , "sad" , "_t" , "_OM", "hat")
    image merona t sadSmile = CreateLiveComposite('Merona' , "sadSmile" , "_t" , "", "hat")
    image merona t sadSmile OM = CreateLiveComposite('Merona' , "sadSmile" , "_t" , "_OM", "hat")
    image merona t sadSmile CE = CreateLiveComposite('Merona' , "sadSmile" , "_t" , "_CE", "hat")
    image merona t scared = CreateLiveComposite('Merona' , "scared" , "_t" , "", "hat")
    image merona t serious = CreateLiveComposite('Merona' , "serious" , "_t" , "", "hat")
    image merona t serious OM = CreateLiveComposite('Merona' , "serious" , "_t" , "_OM", "hat")
    image merona t shocked = CreateLiveComposite('Merona' , "shocked" , "_t" , "", "hat")
    image merona t shocked OM = CreateLiveComposite('Merona' , "shocked" , "_t" , "_OM", "hat")
    image merona t sleepy = CreateLiveComposite('Merona' , "sleepy" , "_t" , "", "hat")
    image merona t surprised = CreateLiveComposite('Merona' , "surprised" , "_t" , "", "hat")
    image merona t surprised OM = CreateLiveComposite('Merona' , "surprised" , "_t" , "_OM", "hat")
    image merona t surprisedBlush = CreateLiveComposite('Merona' , "surprisedBlush" , "_t" , "", "hat")
    image merona t surprisedBlush OM = CreateLiveComposite('Merona' , "surprisedBlush" , "_t" , "_OM", "hat")
    image merona t sweaty = CreateLiveComposite('Merona' , "sweaty" , "_t" , "", "hat")
    image merona t sweaty laugh = CreateLiveComposite('Merona' , "sweaty_laugh" , "_t" , "", "hat")
    image merona t sweaty OM = CreateLiveComposite('Merona' , "sweaty" , "_t" , "_OM", "hat")
    image merona t verySad = CreateLiveComposite('Merona' , "verySad" , "_t" , "", "hat")
    image merona t verySad OM = CreateLiveComposite('Merona' , "verySad" , "_t" , "_OM", "hat")
    image merona t veryScared = CreateLiveComposite('Merona' , "veryScared" , "_t" , "", "hat")
    image merona t veryWorried = CreateLiveComposite('Merona' , "veryWorried" , "_t" , "", "hat")
    image merona t veryWorried OM = CreateLiveComposite('Merona' , "veryWorried" , "_t" , "_OM", "hat")
    image merona t wink = CreateLiveComposite('Merona' , "wink" , "_t" , "", "hat")
    image merona t wink OM = CreateLiveComposite('Merona' , "wink" , "_t" , "_OM", "hat")
    image merona t worried =  CreateLiveComposite('Merona' , "worried" , "_t" , "", "hat")
    image merona t worried CE =  CreateLiveComposite('Merona' , "worried" , "_t" , "_CE", "hat")
    image merona t worried OM =  CreateLiveComposite('Merona' , "worried" , "_t" , "_OM", "hat")
    
    image merona t serious CE = CreateLiveComposite('Merona' , "serious" , "_t" , "_CE", "hat")
    image merona t sleepy CE = CreateLiveComposite('Merona' , "sleepy" , "_t" , "_CE", "hat")
    image merona t surprised OM CE = CreateLiveComposite('Merona' , "surprised" , "_t" , "_OM_CE", "hat")
    image merona t worried CE = CreateLiveComposite('Merona' , "worried" , "_t" , "_CE", "hat")
    image merona t angry CE = CreateLiveComposite('Merona' , "angry" , "_t" , "_CE", "hat")
    image merona t blushSmile CE = CreateLiveComposite('Merona' , "blushSmile" , "_t" , "_CE", "hat")
    image merona t content CE = CreateLiveComposite('Merona' , "content" , "_t" , "_CE", "hat")
    image merona t content OM CE = CreateLiveComposite('Merona' , "content" , "_t" , "_OM_CE", "hat")
    image merona t desperate CE = CreateLiveComposite('Merona' , "desperate" , "_t" , "_CE", "hat")
    image merona t determined CE = CreateLiveComposite('Merona' , "determined" , "_t" , "_CE", "hat")
    image merona t determined OM CE = CreateLiveComposite('Merona' , "determined" , "_t" , "_OM_CE", "hat")
    image merona t disappointed CE = CreateLiveComposite('Merona' , "disappointed" , "_t" , "_CE", "hat")
    image merona t serious OM CE = CreateLiveComposite('Merona', "serious", "_t", "_OM_CE", "hat")
    image merona t disappointed OM CE = CreateLiveComposite('Merona' , "disappointed" , "_t" , "_OM_CE", "hat")
    image merona t embarrassed CE = CreateLiveComposite('Merona' , "embarrassed" , "_t" , "_CE", "hat")
    image merona t grin CE = CreateLiveComposite('Merona' , "grin" , "_t" , "_CE", "hat")
    image merona t nervous CE = CreateLiveComposite('Merona' , "nervous" , "_t" , "_CE", "hat")
    image merona t nervous OM CE = CreateLiveComposite('Merona' , "nervous" , "_t" , "_OM_CE", "hat")
    image merona t reflective CE = CreateLiveComposite('Merona' , "reflective" , "_t" , "_CE", "hat")
    image merona t sad CE = CreateLiveComposite('Merona' , "sad" , "_t" , "_CE", "hat")
    image merona t sadSmile CE = CreateLiveComposite('Merona' , "sadSmile" , "_t" , "_CE", "hat")
    image merona t sadSmile tears CE = CreateLiveComposite('Merona' , "sadSmile_tears" , "_t" , "_CE", "hat")
    image merona t serious CE = CreateLiveComposite('Merona' , "serious" , "_t" , "_CE", "hat")
    image merona t shocked CE = CreateLiveComposite('Merona' , "shocked" , "_t" , "_CE", "hat")
    image merona t sleepy CE = CreateLiveComposite('Merona' , "sleepy" , "_t" , "_CE", "hat")
    image merona t surprised CE = CreateLiveComposite('Merona' , "surprised" , "_t" , "_CE", "hat")
    image merona t surprised OM CE = CreateLiveComposite('Merona' , "surprised" , "_t" , "_OM_CE", "hat")
    image merona t verySad CE = CreateLiveComposite('Merona' , "verySad" , "_t" , "_CE", "hat")
    image merona t veryWorried CE = CreateLiveComposite('Merona' , "veryWorried" , "_t" , "_CE", "hat")
    image merona t worried CE = CreateLiveComposite('Merona' , "worried" , "_t" , "_CE", "hat")
    image merona t worried OM CE = CreateLiveComposite('Merona' , "worried" , "_t" , "_OM_CE", "hat")
    
    # Travel Outfit NoHat
    image merona t sleepy noHat = CreateLiveComposite('Merona' , "sleepy" , "_t" , "", "")
    image merona t content CE noHat = CreateLiveComposite('Merona' , "content" , "_t" , "_CE", "")
    image merona t determined noHat = CreateLiveComposite('Merona' , "determined" , "_t" , "", "")
    image merona t determined OM noHat = CreateLiveComposite('Merona' , "determined" , "_t" , "_OM", "")
    image merona t determinedGrin noHat = CreateLiveComposite('Merona' , "determinedGrin" , "_t" , "", "")
    image merona t disappointed noHat = CreateLiveComposite('Merona' , "disappointed" , "_t" , "", "")
    image merona t disappointed OM noHat =  CreateLiveComposite('Merona' , "disappointed" , "_t" , "_OM", "")
    image merona t disappointed CE noHat =  CreateLiveComposite('Merona' , "disappointed" , "_t" , "_CE", "")
    image merona t reflective noHat = CreateLiveComposite('Merona' , "reflective" , "_t" , "", "")    
    image merona t sad noHat = CreateLiveComposite('Merona' , "sad" , "_t" , "", "")
    image merona t sad OM noHat = CreateLiveComposite('Merona' , "sad" , "_t" , "_OM", "")
    image merona t sadSmile CE noHat = CreateLiveComposite('Merona' , "sadSmile" , "_t" , "_OM", "")
    image merona t serious noHat = CreateLiveComposite('Merona' , "serious" , "_t" , "", "")
    image merona t serious CE noHat = CreateLiveComposite('Merona' , "serious" , "_t" , "_OM", "")
    image merona t sleepy noHat = CreateLiveComposite('Merona' , "sleepy" , "_t" , "", "")
    image merona t surprised noHat = CreateLiveComposite('Merona' , "surprised" , "_t" , "", "")
    image merona t surprised OM noHat = CreateLiveComposite('Merona' , "surprised" , "_t" , "_OM", "")
    
    image merona t content CE noHat = CreateLiveComposite('Merona' , "content" , "_t" , "_CE", "")
    image merona t disappointed CE noHat = CreateLiveComposite('Merona' , "disappointed" , "_t" , "_CE", "")
    image merona t serious CE noHat = CreateLiveComposite('Merona' , "serious" , "_t" , "_CE", "")
    image merona t sadSmile CE noHat = CreateLiveComposite('Merona' , "sadSmile" , "_t" , "_CE", "")
    
    #other
    image merona behind1 = "img/sprites/Merona/M_u_behind1.png"
    image merona behind2 = "img/sprites/Merona/M_u_behind2.png"
    image merona behind3 = "img/sprites/Merona/M_u_behind3.png"
    
    
    ### Boyen Emotions ###
    
    image boyen angry = CreateLiveComposite('Boyen' , "angry" , "" , "", "")
    image boyen angry OM = CreateLiveComposite('Boyen' , "angry" , "" , "_OM", "")
    image boyen content = CreateLiveComposite('Boyen' , "content" , "" , "", "")
    image boyen content OM = CreateLiveComposite('Boyen' , "content" , "" , "_OM", "")
    image boyen content CE = CreateLiveComposite('Boyen' , "content" , "" , "_CE", "")
    image boyen content OM CE = CreateLiveComposite('Boyen' , "content" , "" , "_OM_CE", "")
    image boyen grin = CreateLiveComposite('Boyen' , "grin" , "" , "", "")
    image boyen grin CE = CreateLiveComposite('Boyen' , "grin" , "" , "_CE", "")
    image boyen grin2 = CreateLiveComposite('Boyen' , "grin2" , "" , "", "")
    image boyen happy = CreateLiveComposite('Boyen' , "happy" , "" , "", "")
    image boyen happy S = CreateLiveComposite('Boyen' , "happy_S" , "" , "", "")
    image boyen happy CE = CreateLiveComposite('Boyen' , "happy" , "" , "_CE", "")
    image boyen happy CE S = CreateLiveComposite('Boyen' , "happy_S" , "" , "_CE", "")
    image boyen happy2 = CreateLiveComposite('Boyen' , "happy2" , "" , "", "")
    image boyen neutral = CreateLiveComposite('Boyen' , "neutral" , "" , "", "")
    image boyen neutral CE = CreateLiveComposite('Boyen' , "neutral" , "" , "_CE", "")
    image boyen neutral OM = CreateLiveComposite('Boyen' , "neutral" , "" , "_OM", "")
    image boyen sad = CreateLiveComposite('Boyen' , "sad" , "" , "", "")
    image boyen sad OM = CreateLiveComposite('Boyen' , "sad" , "" , "_OM", "")
    image boyen sadSmile = CreateLiveComposite('Boyen' , "sadSmile" , "" , "", "")
    image boyen sadSmile OM = CreateLiveComposite('Boyen' , "sadSmile" , "" , "_OM", "")
    image boyen scared = CreateLiveComposite('Boyen' , "scared" , "" , "", "")
    image boyen scared OM = CreateLiveComposite('Boyen' , "scared" , "" , "_OM", "")
    image boyen sceptical = CreateLiveComposite('Boyen' , "sceptical" , "" , "", "")
    image boyen sceptical OM = CreateLiveComposite('Boyen' , "sceptical" , "" , "_OM", "")
    image boyen serious = CreateLiveComposite('Boyen' , "serious" , "" , "", "")
    image boyen serious OM = CreateLiveComposite('Boyen' , "serious" , "" , "_OM", "")
    image boyen shocked = CreateLiveComposite('Boyen' , "shocked" , "" , "", "")
    image boyen shocked OM = CreateLiveComposite('Boyen' , "shocked" , "" , "_OM", "")
    image boyen surprised = CreateLiveComposite('Boyen' , "surprised" , "" , "", "")
    image boyen sweaty = CreateLiveComposite('Boyen' , "sweaty" , "" , "", "")
    image boyen sweaty = CreateLiveComposite('Boyen' , "sweaty" , "" , "_CE", "")
    image boyen sweaty OM = CreateLiveComposite('Boyen' , "sweaty" , "" , "_OM", "")
    image boyen tired =  CreateLiveComposite('Boyen' , "tired" , "" , "", "")
    image boyen tired OM = CreateLiveComposite('Boyen' , "tired" , "" , "_OM", "")
    image boyen verySerious = CreateLiveComposite('Boyen' , "verySerious" , "" , "", "")
    image boyen verySerious CE= CreateLiveComposite('Boyen' , "verySerious" , "" , "_CE", "")
    image boyen verySerious OM = CreateLiveComposite('Boyen' , "verySerious" , "" , "_OM", "")
    image boyen worried =  CreateLiveComposite('Boyen' , "worried" , "" , "", "")
    image boyen worried OM = CreateLiveComposite('Boyen' , "worried" , "" , "_OM", "")
    
    ### Cimaria Emotions ###
    
    image cimaria abashed = CreateLiveComposite('Cimaria' , "abashed" , "" , "", "")
    image cimaria abashed OM = CreateLiveComposite('Cimaria' , "abashed" , "" , "_OM", "")
    image cimaria aggressive = CreateLiveComposite('Cimaria' , "aggressive" , "" , "", "")
    image cimaria aggressive OM = CreateLiveComposite('Cimaria' , "aggressive" , "" , "_OM", "")
    image cimaria aggressive OM CE = CreateLiveComposite('Cimaria' , "aggressive" , "" , "_OM_CE", "")
    image cimaria annoyed = CreateLiveComposite('Cimaria' , "annoyed" , "" , "", "")
    image cimaria annoyed OM = CreateLiveComposite('Cimaria' , "annoyed" , "" , "_OM", "")
    image cimaria annoyed CE = CreateLiveComposite('Cimaria' , "annoyed" , "" , "_CE", "")
    image cimaria blushSmile = CreateLiveComposite('Cimaria' , "blushSmile" , "" , "", "")
    image cimaria blushSmile OM = CreateLiveComposite('Cimaria' , "blushSmile" , "" , "_OM", "")
    image cimaria blushSmile CE = CreateLiveComposite('Cimaria' , "blushSmile" , "" , "_CE", "")
    image cimaria confused = CreateLiveComposite('Cimaria' , "confused" , "" , "", "")
    image cimaria confused OM = CreateLiveComposite('Cimaria' , "confused" , "" , "_OM", "")
    image cimaria content = CreateLiveComposite('Cimaria' , "content" , "" , "", "")
    image cimaria content OM = CreateLiveComposite('Cimaria' , "content" , "" , "_OM", "")
    image cimaria content CE = CreateLiveComposite('Cimaria' , "content" , "" , "_CE", "")
    image cimaria content OM CE= CreateLiveComposite('Cimaria' , "content" , "" , "_OM_CE", "")
    image cimaria determined = CreateLiveComposite('Cimaria' , "determined" , "" , "", "")
    image cimaria determined OM = CreateLiveComposite('Cimaria' , "determined" , "" , "_OM", "")
    image cimaria determined OM CE = CreateLiveComposite('Cimaria' , "determined" , "" , "_OM_CE", "")
    image cimaria embarrassed = CreateLiveComposite('Cimaria' , "embarrassed" , "" , "", "")
    image cimaria embarrassed OM = CreateLiveComposite('Cimaria' , "embarrassed" , "" , "_OM", "")
    image cimaria embarrassed CE = CreateLiveComposite('Cimaria' , "embarrassed" , "" , "_CE", "")
    image cimaria embarrassed OM CE = CreateLiveComposite('Cimaria' , "embarrassed" , "" , "_OM_CE", "")
    image cimaria embarrassedSmile = CreateLiveComposite('Cimaria' , "embarrassedSmile" , "" , "", "")
    image cimaria embarrassedSmile OM = CreateLiveComposite('Cimaria' , "embarrassedSmile" , "" , "_OM", "")
    image cimaria gentle = CreateLiveComposite('Cimaria' , "gentle" , "" , "", "")
    image cimaria gentle OM = CreateLiveComposite('Cimaria' , "gentle" , "" , "_OM", "")
    image cimaria gentle CE = CreateLiveComposite('Cimaria' , "gentle" , "" , "_CE", "")
    image cimaria gentle OM CE = CreateLiveComposite('Cimaria' , "gentle" , "" , "_OM_CE", "")
    image cimaria grin = CreateLiveComposite('Cimaria' , "grin" , "" , "", "")
    image cimaria grin CE = CreateLiveComposite('Cimaria' , "grin" , "" , "_CE", "")
    image cimaria laugh = CreateLiveComposite('Cimaria' , "laugh" , "" , "", "")
    image cimaria neutral = CreateLiveComposite('Cimaria' , "neutral" , "" , "", "")
    image cimaria neutral CE = CreateLiveComposite('Cimaria' , "neutral" , "" , "_CE", "")
    image cimaria neutral OM = CreateLiveComposite('Cimaria' , "neutral" , "" , "_OM", "")
    image cimaria sad = CreateLiveComposite('Cimaria' , "sad" , "" , "", "")
    image cimaria sad CE = CreateLiveComposite('Cimaria' , "sad" , "" , "_CE", "")
    image cimaria sad OM = CreateLiveComposite('Cimaria' , "sad" , "" , "_OM", "")
    image cimaria sadderSmile = CreateLiveComposite('Cimaria' , "sadderSmile" , "" , "", "")
    image cimaria sadderSmile OM = CreateLiveComposite('Cimaria' , "sadderSmile" , "" , "_OM", "")
    image cimaria sadderSmile CE = CreateLiveComposite('Cimaria' , "sadderSmile" , "" , "_CE", "")
    image cimaria sadderSmile OM CE = CreateLiveComposite('Cimaria' , "sadderSmile" , "" , "_OM_CE", "")
    image cimaria sadSmile = CreateLiveComposite('Cimaria' , "sadSmile" , "" , "", "")
    image cimaria sadSmile OM = CreateLiveComposite('Cimaria' , "sadSmile" , "" , "_OM", "")
    image cimaria sceptical = CreateLiveComposite('Cimaria' , "sceptical" , "" , "", "")
    image cimaria sceptical OM = CreateLiveComposite('Cimaria' , "sceptical" , "" , "_OM", "")
    image cimaria serious = CreateLiveComposite('Cimaria' , "serious" , "" , "", "")
    image cimaria serious OM = CreateLiveComposite('Cimaria' , "serious" , "" , "_OM", "")
    image cimaria serious CE = CreateLiveComposite('Cimaria' , "serious" , "" , "_CE", "")
    image cimaria serious OM CE = CreateLiveComposite('Cimaria' , "serious" , "" , "_OM_CE", "")
    image cimaria shocked = CreateLiveComposite('Cimaria' , "shocked" , "" , "", "")
    image cimaria shocked OM = CreateLiveComposite('Cimaria' , "shocked" , "" , "_OM", "")
    image cimaria surprised = CreateLiveComposite('Cimaria' , "surprised" , "" , "", "")
    image cimaria wink = CreateLiveComposite('Cimaria' , "wink" , "" , "", "")
    image cimaria wink OM = CreateLiveComposite('Cimaria' , "wink" , "" , "_OM", "")
    image cimaria worried = CreateLiveComposite('Cimaria' , "worried" , "" , "", "")
    image cimaria worried CE = CreateLiveComposite('Cimaria' , "worried" , "" , "_CE", "")
    image cimaria worried OM = CreateLiveComposite('Cimaria' , "worried" , "" , "_OM", "")
    image cimaria worried OM CE = CreateLiveComposite('Cimaria' , "worried" , "" , "_OM_CE", "")
    #Missing
    #image cimaria nervous = CreateLiveComposite('Cimaria' , "nervous" , "" , "", "")
    #image cimaria nervous OM = CreateLiveComposite('Cimaria' , "nervous" , "" , "_OM", "")
    
    #Tired version
    image cimaria tired content = CreateLiveComposite('Cimaria' , "content" , "_Tired" , "", "")
    image cimaria tired content OM = CreateLiveComposite('Cimaria' , "content" , "_Tired" , "_OM", "")
    
    ### Duran Emotions ###
    
    image duran angry = CreateLiveComposite('Duran' , "angry" , "_u" , "", "")
    image duran angry OM = CreateLiveComposite('Duran' , "angry" , "_u" , "_OM", "")
    image duran angry OM CE = CreateLiveComposite('Duran' , "angry" , "_u" , "_OM_CE", "")
    image duran angryBlush = CreateLiveComposite('Duran' , "angryBlush" , "_u" , "", "")
    image duran angryBlush OM = CreateLiveComposite('Duran' , "angryBlush" , "_u" , "_OM", "")
    image duran annoyed = CreateLiveComposite('Duran' , "annoyed" , "_u" , "", "")
    image duran annoyed EL = CreateLiveComposite('Duran' , "annoyed" , "_u" , "_EL", "")
    image duran annoyed OM = CreateLiveComposite('Duran' , "annoyed" , "_u" , "_OM", "")
    image duran annoyed CE = CreateLiveComposite('Duran' , "annoyed" , "_u" , "_CE", "")
    image duran annoyed OM CE = CreateLiveComposite('Duran' , "annoyed" , "_u" , "_OM_CE", "")
    image duran annoyed S = CreateLiveComposite('Duran' , "annoyed_S" , "_u" , "", "")
    image duran annoyed OM S = CreateLiveComposite('Duran' , "annoyed_S" , "_u" , "_OM", "")
    image duran blushSmile = CreateLiveComposite('Duran' , "blushSmile" , "_u" , "", "")
    image duran blushSmile OM = CreateLiveComposite('Duran' , "blushSmile" , "_u" , "_OM", "")
    image duran bored = CreateLiveComposite('Duran' , "bored" , "_u" , "", "")
    image duran bored OM = CreateLiveComposite('Duran' , "bored" , "_u" , "_OM", "")
    image duran confused = CreateLiveComposite('Duran' , "confused" , "_u" , "", "")
    image duran confused OM = CreateLiveComposite('Duran' , "confused" , "_u" , "_OM", "")
    image duran content = CreateLiveComposite('Duran' , "content" , "_u" , "", "")
    image duran content OM = CreateLiveComposite('Duran' , "content" , "_u" , "_OM", "")
    image duran determined = CreateLiveComposite('Duran' , "determined" , "_u" , "", "")
    image duran determined OM = CreateLiveComposite('Duran' , "determined" , "_u" , "_OM", "")
    image duran embarrassed = CreateLiveComposite('Duran' , "embarrassed" , "_u" , "", "")
    image duran embarrassed OM = CreateLiveComposite('Duran' , "embarrassed" , "_u" , "_OM", "")
    image duran evilGrin = CreateLiveComposite('Duran' , "evilGrin" , "_u" , "", "")
    image duran evilGrin OM = CreateLiveComposite('Duran' , "evilGrin" , "_u" , "_OM", "")
    image duran flabber = CreateLiveComposite('Duran' , "flabber" , "_u" , "", "")
    image duran flabber OM = CreateLiveComposite('Duran' , "flabber" , "_u" , "_OM", "")
    image duran grin = CreateLiveComposite('Duran' , "grin" , "_u" , "", "")
    image duran grin OM = CreateLiveComposite('Duran' , "grin" , "_u" , "_OM", "")
    image duran nervous = CreateLiveComposite('Duran' , "worried" , "_u" , "", "")
    image duran nervous OM = CreateLiveComposite('Duran' , "nervous" , "_u" , "_OM", "")
    image duran neutral = CreateLiveComposite('Duran' , "nervous" , "_u" , "", "")
    image duran neutral OM = CreateLiveComposite('Duran' , "neutral" , "_u" , "_OM", "")
    image duran neutral OM S = CreateLiveComposite('Duran' , "neutral_S" , "_u" , "_OM", "")
    image duran neutral S = CreateLiveComposite('Duran' , "neutral" , "_u" , "", "")
    image duran sad = CreateLiveComposite('Duran' , "sad" , "_u" , "", "")
    image duran sad OM = CreateLiveComposite('Duran' , "sad" , "_u" , "_OM", "")
    image duran sadSmile = CreateLiveComposite('Duran' , "sadSmile" , "_u" , "", "")
    image duran sadSmile OM = CreateLiveComposite('Duran' , "sadSmile" , "_u" , "_OM", "")
    image duran serious = CreateLiveComposite('Duran' , "serious" , "_u" , "", "")
    image duran serious OM = CreateLiveComposite('Duran' , "serious" , "_u" , "_OM", "")
    image duran smirk = CreateLiveComposite('Duran' , "smirk" , "_u" , "", "")
    image duran smirk OM = CreateLiveComposite('Duran' , "smirk" , "_u" , "_OM", "")
    image duran surprised = CreateLiveComposite('Duran' , "surprised" , "_u" , "", "")
    image duran surprised OM = CreateLiveComposite('Duran' , "surprised" , "_u" , "_OM", "")
    image duran tired = CreateLiveComposite('Duran' , "tired" , "_u" , "", "")
    image duran tired OM = CreateLiveComposite('Duran' , "tired" , "_u" , "_OM", "")
    image duran worried = CreateLiveComposite('Duran' , "worried" , "_u" , "", "")
    image duran worried OM = CreateLiveComposite('Duran' , "worried" , "_u" , "_OM", "")
    
    #Bandaged version
    image duran b angry = CreateLiveComposite('Duran' , "angry" , "_bandaged" , "", "")
    image duran b angry OM = CreateLiveComposite('Duran' , "angry" , "_bandaged" , "_OM", "")
    image duran b angryBlush = CreateLiveComposite('Duran' , "angryBlush" , "_bandaged" , "", "")
    image duran b angryBlush OM = CreateLiveComposite('Duran' , "angryBlush" , "_bandaged" , "_OM", "")
    image duran b annoyed = CreateLiveComposite('Duran' , "annoyed" , "_bandaged" , "", "")
    image duran b annoyed EL = CreateLiveComposite('Duran' , "annoyed" , "_bandaged" , "_EL", "")
    image duran b annoyed OM = CreateLiveComposite('Duran' , "annoyed" , "_bandaged" , "_OM", "")
    image duran b annoyed OM S = CreateLiveComposite('Duran' , "annoyed_S" , "_bandaged" , "_OM", "")
    image duran b blushSmile = CreateLiveComposite('Duran' , "blushSmile" , "_bandaged" , "", "")
    image duran b blushSmile OM = CreateLiveComposite('Duran' , "blushSmile" , "_bandaged" , "_OM", "")
    image duran b bored = CreateLiveComposite('Duran' , "bored" , "_bandaged" , "", "")
    image duran b bored OM = CreateLiveComposite('Duran' , "bored" , "_bandaged" , "_OM", "")
    image duran b confused = CreateLiveComposite('Duran' , "confused" , "_bandaged" , "", "")
    image duran b confused OM = CreateLiveComposite('Duran' , "confused" , "_bandaged" , "_OM", "")
    image duran b content = CreateLiveComposite('Duran' , "content" , "_bandaged" , "", "")
    image duran b content OM = CreateLiveComposite('Duran' , "content" , "_bandaged" , "_OM", "")
    image duran b determined = CreateLiveComposite('Duran' , "determined" , "_bandaged" , "", "")
    image duran b determined OM = CreateLiveComposite('Duran' , "determined" , "_bandaged" , "_OM", "")
    image duran b embarrassed = CreateLiveComposite('Duran' , "embarrassed" , "_bandaged" , "", "")
    image duran b embarrassed OM = CreateLiveComposite('Duran' , "embarrassed" , "_bandaged" , "_OM", "")
    image duran b embarrassed OM CE = CreateLiveComposite('Duran' , "embarrassed" , "_bandaged" , "_OM_CE", "")
    image duran b evilGrin = CreateLiveComposite('Duran' , "evilGrin" , "_bandaged" , "", "")
    image duran b evilGrin OM = CreateLiveComposite('Duran' , "evilGrin" , "_bandaged" , "_OM", "")
    image duran b flabber = CreateLiveComposite('Duran' , "flabber" , "_bandaged" , "", "")
    image duran b flabber OM = CreateLiveComposite('Duran' , "flabber" , "_bandaged" , "_OM", "")
    image duran b grin = CreateLiveComposite('Duran' , "grin" , "_bandaged" , "", "")
    image duran b grin OM = CreateLiveComposite('Duran' , "grin" , "_bandaged" , "_OM", "")
    image duran b nervous = CreateLiveComposite('Duran' , "nervous" , "_bandaged" , "", "")
    image duran b nervous OM = CreateLiveComposite('Duran' , "nervous" , "_bandaged" , "_OM", "")
    image duran b neutral = CreateLiveComposite('Duran' , "neutral" , "_bandaged" , "", "")
    image duran b neutral OM = CreateLiveComposite('Duran' , "neutral" , "_bandaged" , "_OM", "")
    image duran b neutral OM S = CreateLiveComposite('Duran' , "neutral_S" , "_bandaged" , "_OM", "")
    image duran b neutral S = CreateLiveComposite('Duran' , "neutral" , "_bandaged" , "", "")
    image duran b sad = CreateLiveComposite('Duran' , "sad" , "_bandaged" , "", "")
    image duran b sad OM = CreateLiveComposite('Duran' , "sad" , "_bandaged" , "_OM", "")
    image duran b sadSmile = CreateLiveComposite('Duran' , "sadSmile" , "_bandaged" , "", "")
    image duran b sadSmile OM = CreateLiveComposite('Duran' , "sadSmile" , "_bandaged" , "_OM", "")
    image duran b serious = CreateLiveComposite('Duran' , "serious" , "_bandaged" , "", "")
    image duran b serious OM = CreateLiveComposite('Duran' , "serious" , "_bandaged" , "_OM", "")
    image duran b smirk = CreateLiveComposite('Duran' , "smirk" , "_bandaged" , "", "")
    image duran b smirk OM = CreateLiveComposite('Duran' , "smirk" , "_bandaged" , "_OM", "")
    image duran b surprised = CreateLiveComposite('Duran' , "surprised" , "_bandaged" , "", "")
    image duran b surprised OM = CreateLiveComposite('Duran' , "surprised" , "_bandaged" , "_OM", "")
    image duran b tired = CreateLiveComposite('Duran' , "tired" , "_bandaged" , "", "")
    image duran b tired OM = CreateLiveComposite('Duran' , "tired" , "_bandaged" , "_OM", "")
    image duran b worried = CreateLiveComposite('Duran' , "worried" , "_bandaged" , "", "")
    image duran b worried OM = CreateLiveComposite('Duran' , "worried" , "_bandaged" , "_OM", "")
    
    #Travel version
    image duran t angry = CreateLiveComposite('Duran' , "angry" , "_t" , "", "")
    image duran t angry OM = CreateLiveComposite('Duran' , "angry" , "_t" , "_OM", "")
    image duran t angryBlush = CreateLiveComposite('Duran' , "angryBlush" , "_t" , "", "")
    image duran t angryBlush OM = CreateLiveComposite('Duran' , "angryBlush" , "_t" , "_OM", "")
    image duran t annoyed = CreateLiveComposite('Duran' , "annoyed" , "_t" , "", "")
    image duran t annoyed EL = CreateLiveComposite('Duran' , "annoyed" , "_t" , "_EL", "")
    image duran t annoyed OM = CreateLiveComposite('Duran' , "annoyed" , "_t" , "_OM", "")
    image duran t annoyed OM S = CreateLiveComposite('Duran' , "annoyed_S" , "_t" , "_OM", "")
    image duran t blushSmile = CreateLiveComposite('Duran' , "blushSmile" , "_t" , "", "")
    image duran t blushSmile OM = CreateLiveComposite('Duran' , "blushSmile" , "_t" , "_OM", "")
    image duran t bored = CreateLiveComposite('Duran' , "bored" , "_t" , "", "")
    image duran t bored OM = CreateLiveComposite('Duran' , "bored" , "_t" , "_OM", "")
    image duran t confused = CreateLiveComposite('Duran' , "confused" , "_t" , "", "")
    image duran t confused OM = CreateLiveComposite('Duran' , "confused" , "_t" , "_OM", "")
    image duran t content = CreateLiveComposite('Duran' , "content" , "_t" , "", "")
    image duran t content OM = CreateLiveComposite('Duran' , "content" , "_t" , "_OM", "")
    image duran t determined = CreateLiveComposite('Duran' , "determined" , "_t" , "", "")
    image duran t determined OM = CreateLiveComposite('Duran' , "determined" , "_t" , "_OM", "")
    image duran t embarrassed = CreateLiveComposite('Duran' , "embarrassed" , "_t" , "", "")
    image duran t embarrassed OM = CreateLiveComposite('Duran' , "embarrassed" , "_t" , "_OM", "")
    image duran t evilGrin = CreateLiveComposite('Duran' , "evilGrin" , "_t" , "", "")
    image duran t evilGrin OM = CreateLiveComposite('Duran' , "evilGrin" , "_t" , "_OM", "")
    image duran t flabber = CreateLiveComposite('Duran' , "flabber" , "_t" , "", "")
    image duran t flabber OM = CreateLiveComposite('Duran' , "flabber" , "_t" , "_OM", "")
    image duran t grin = CreateLiveComposite('Duran' , "grin" , "_t" , "", "")
    image duran t grin OM = CreateLiveComposite('Duran' , "grin" , "_t" , "_OM", "")
    image duran t nervous = CreateLiveComposite('Duran' , "nervous" , "_t" , "", "")
    image duran t nervous OM = CreateLiveComposite('Duran' , "nervous" , "_t" , "_OM", "")
    image duran t neutral = CreateLiveComposite('Duran' , "neutral" , "_t" , "", "")
    image duran t neutral OM = CreateLiveComposite('Duran' , "neutral" , "_t" , "_OM", "")
    image duran t neutral OM S = CreateLiveComposite('Duran' , "neutral_S" , "_t" , "_OM", "")
    image duran t neutral S = CreateLiveComposite('Duran' , "neutral_S" , "_t" , "", "")
    image duran t sad = CreateLiveComposite('Duran' , "sad" , "_t" , "", "")
    image duran t sad OM = CreateLiveComposite('Duran' , "sad" , "_t" , "_OM", "")
    image duran t sadSmile = CreateLiveComposite('Duran' , "sadSmile" , "_t" , "", "")
    image duran t sadSmile OM = CreateLiveComposite('Duran' , "sadSmile" , "_t" , "_OM", "")
    image duran t serious = CreateLiveComposite('Duran' , "serious" , "_t" , "", "")
    image duran t serious OM = CreateLiveComposite('Duran' , "serious" , "_t" , "_OM", "")
    image duran t smirk = CreateLiveComposite('Duran' , "smirk" , "_t" , "", "")
    image duran t smirk OM = CreateLiveComposite('Duran' , "smirk" , "_t" , "_OM", "")
    image duran t surprised = CreateLiveComposite('Duran' , "surprised" , "_t" , "", "")
    image duran t surprised OM = CreateLiveComposite('Duran' , "surprised" , "_t" , "_OM", "")
    image duran t tired = CreateLiveComposite('Duran' , "tired" , "_t" , "", "")
    image duran t tired OM = CreateLiveComposite('Duran' , "tired" , "_t" , "_OM", "")
    image duran t worried = CreateLiveComposite('Duran' , "worried" , "_t" , "", "")
    image duran t worried OM = CreateLiveComposite('Duran' , "worried" , "_t" , "_OM", "")
    image duran t worried CE = CreateLiveComposite('Duran' , "worried" , "_t" , "_CE", "")
    
    
    ### Kreita Emotions ###
    
    image kreita aggressive = CreateLiveComposite('Kreita' , "aggressive" , "" , "", "")
    image kreita aggressive OM = CreateLiveComposite('Kreita' , "aggressive" , "" , "_OM", "")
    image kreita angry = CreateLiveComposite('Kreita' , "angry" , "" , "", "")
    image kreita angry OM = CreateLiveComposite('Kreita' , "angry" , "" , "_OM", "")
    image kreita confused = CreateLiveComposite('Kreita' , "confused" , "" , "", "")
    image kreita confused OM = CreateLiveComposite('Kreita' , "confused" , "" , "_OM", "")
    image kreita content = CreateLiveComposite('Kreita' , "content" , "" , "", "")
    image kreita content OM = CreateLiveComposite('Kreita' , "content" , "" , "_OM", "")
    image kreita determined = CreateLiveComposite('Kreita' , "determined" , "" , "", "")
    image kreita determined OM = CreateLiveComposite('Kreita' , "determined" , "" , "_OM", "")
    image kreita fierce = CreateLiveComposite('Kreita' , "fierce" , "" , "", "")
    image kreita fierce OM = CreateLiveComposite('Kreita' , "fierce" , "" , "_OM", "")
    image kreita fierceWink = CreateLiveComposite('Kreita' , "fierceWink" , "" , "", "")
    image kreita grin = CreateLiveComposite('Kreita' , "grin" , "" , "", "")
    image kreita grin2 = CreateLiveComposite('Kreita' , "grin2" , "" , "", "")
    image kreita grin2 S = CreateLiveComposite('Kreita' , "grin2_S" , "" , "", "")
    image kreita happy = CreateLiveComposite('Kreita' , "happy" , "" , "", "")
    image kreita laugh = CreateLiveComposite('Kreita' , "laugh" , "" , "", "")
    image kreita laugh S = CreateLiveComposite('Kreita' , "laugh_S" , "" , "", "")
    image kreita laugh2 S = CreateLiveComposite('Kreita' , "laugh_S" , "" , "", "") #TODO: No Laugh2_S face available
    image kreita lol = CreateLiveComposite('Kreita' , "lol" , "" , "", "")
    image kreita neutral = CreateLiveComposite('Kreita' , "neutral" , "" , "", "")
    image kreita neutral OM = CreateLiveComposite('Kreita' , "neutral" , "" , "_OM", "")
    image kreita pouty = CreateLiveComposite('Kreita' , "pouty" , "" , "", "")
    image kreita pouty OM = CreateLiveComposite('Kreita' , "pouty" , "" , "_OM", "")
    image kreita pouty S = CreateLiveComposite('Kreita' , "pouty_S" , "" , "", "")
    image kreita pouty S OM = CreateLiveComposite('Kreita' , "pouty_S" , "" , "_OM", "")
    image kreita sad = CreateLiveComposite('Kreita' , "sad" , "" , "", "")
    image kreita sad OM = CreateLiveComposite('Kreita' , "sad" , "" , "_OM", "")
    image kreita sadSmile = CreateLiveComposite('Kreita' , "sadSmile" , "" , "", "")
    image kreita sadSmile OM = CreateLiveComposite('Kreita' , "sadSmile" , "" , "_OM", "")
    image kreita sceptical = CreateLiveComposite('Kreita' , "sceptical" , "" , "", "")
    image kreita sceptical OM = CreateLiveComposite('Kreita' , "sceptical" , "" , "_OM", "")
    image kreita serious = CreateLiveComposite('Kreita' , "serious" , "" , "", "")
    image kreita serious OM = CreateLiveComposite('Kreita' , "serious" , "" , "_OM", "")
    image kreita shocked = CreateLiveComposite('Kreita' , "shocked" , "" , "", "")
    image kreita surprised = CreateLiveComposite('Kreita' , "surprised" , "" , "", "")
    image kreita tongue = CreateLiveComposite('Kreita' , "tongue" , "" , "", "")
    image kreita verySad = CreateLiveComposite('Kreita' , "verySad" , "" , "", "")
    image kreita verySad OM = CreateLiveComposite('Kreita' , "verySad" , "" , "_OM", "")
    image kreita verySad2 = CreateLiveComposite('Kreita' , "verySad2" , "" , "", "")
    image kreita verySad2 OM = CreateLiveComposite('Kreita' , "verySad2" , "" , "_OM", "")
    image kreita weakWink = CreateLiveComposite('Kreita' , "weakWink" , "" , "", "")
    image kreita weakWink OM = CreateLiveComposite('Kreita' , "weakWink" , "" , "_OM", "")
    image kreita worried = CreateLiveComposite('Kreita' , "worried" , "" , "", "")
    image kreita worried OM = CreateLiveComposite('Kreita' , "worried" , "" , "_OM", "")
    
    image kreita aggressive CE = CreateLiveComposite('Kreita' , "aggressive" , "" , "_CE", "")
    image kreita content CE = CreateLiveComposite('Kreita' , "content" , "" , "_CE", "")
    image kreita determined CE = CreateLiveComposite('Kreita' , "determined" , "" , "_CE", "")
    image kreita fierce CE = CreateLiveComposite('Kreita' , "fierce" , "" , "_CE", "")
    image kreita grin CE = CreateLiveComposite('Kreita' , "grin" , "" , "_CE", "")
    image kreita grin2 CE = CreateLiveComposite('Kreita' , "grin2" , "" , "_CE", "")
    image kreita grin2 CE S = CreateLiveComposite('Kreita' , "grin2_S" , "" , "_CE", "")
    image kreita happy CE = CreateLiveComposite('Kreita' , "happy" , "" , "_CE", "")
    image kreita happy OM CE = CreateLiveComposite('Kreita' , "happy" , "" , "_CE", "")
    image kreita laugh CE = CreateLiveComposite('Kreita' , "laugh" , "" , "_CE", "")
    image kreita laugh CE S = CreateLiveComposite('Kreita' , "laugh_S" , "" , "_CE", "")
    image kreita neutral CE = CreateLiveComposite('Kreita' , "neutral" , "" , "_CE", "")
    image kreita neutral OM CE = CreateLiveComposite('Kreita' , "neutral" , "" , "_OM_CE", "")
    image kreita pouty CE = CreateLiveComposite('Kreita' , "pouty" , "" , "_CE", "")
    image kreita pouty CE S = CreateLiveComposite('Kreita' , "pouty_S" , "" , "_CE", "")
    image kreita pouty OM CE = CreateLiveComposite('Kreita' , "pouty" , "" , "_OM_CE", "")
    image kreita sad CE = CreateLiveComposite('Kreita' , "sad" , "" , "_CE", "")
    image kreita serious CE = CreateLiveComposite('Kreita' , "serious" , "" , "_CE", "")
    image kreita shocked CE = CreateLiveComposite('Kreita' , "shocked" , "" , "_CE", "")
    image kreita worried CE = CreateLiveComposite('Kreita' , "worried" , "" , "_CE", "")
    
    #Map version
    image kreita map content = CreateLiveComposite('Kreita' , "content" , "_map" , "", "") 
    
    image kreita map aggressive = CreateLiveComposite('Kreita' , "aggressive" , "_map" , "", "")
    image kreita map aggressive OM = CreateLiveComposite('Kreita' , "aggressive" , "_map" , "_OM", "")
    image kreita map pouty = CreateLiveComposite('Kreita' , "pouty" , "_map" , "", "")
    image kreita map pouty OM = CreateLiveComposite('Kreita' , "pouty" , "_map" , "_OM", "")
    image kreita map worried = CreateLiveComposite('Kreita' , "worried" , "_map" , "", "")
    image kreita map worried OM = CreateLiveComposite('Kreita' , "worried" , "_map" , "_OM", "")
    
    #Fish version
    image kreita fish content = CreateLiveComposite('Kreita' , "content" , "_fish" , "", "")
    image kreita fish content OM = CreateLiveComposite('Kreita' , "content" , "_fish" , "_OM", "")
    image kreita fish happy = CreateLiveComposite('Kreita' , "happy" , "_fish" , "", "")
    image kreita fish grin2 S CE  = CreateLiveComposite('Kreita' , "grin2_S" , "_fish" , "_CE", "")
    image kreita fish grin  = CreateLiveComposite('Kreita' , "grin" , "_fish" , "", "")
    image kreita fish grin2  = CreateLiveComposite('Kreita' , "grin2" , "_fish" , "", "")
    image kreita fish neutral = CreateLiveComposite('Kreita' , "neutral" , "_fish" , "", "")
    image kreita fish pouty = CreateLiveComposite('Kreita' , "pouty" , "_fish" , "", "")
    image kreita fish pouty OM = CreateLiveComposite('Kreita' , "pouty" , "_fish" , "_OM", "")
    image kreita fish sad = CreateLiveComposite('Kreita' , "sad" , "_fish" , "", "")
    image kreita fish sad OM = CreateLiveComposite('Kreita' , "sad" , "_fish" , "_OM", "")
    image kreita fish sadSmile = CreateLiveComposite('Kreita' , "sadSmile" , "_fish" , "", "")
    image kreita fish sceptical = CreateLiveComposite('Kreita' , "worried" , "_fish" , "", "")
    image kreita fish sceptical OM = CreateLiveComposite('Kreita' , "worried" , "_fish" , "_OM", "")
    image kreita fish fierce = CreateLiveComposite('Kreita' , "fierce" , "_fish" , "", "")
    image kreita fish fierce OM = CreateLiveComposite('Kreita' , "fierce" , "_fish" , "_OM", "")
    image kreita fish worried = CreateLiveComposite('Kreita' , "worried" , "_fish" , "", "")
    image kreita fish worried OM = CreateLiveComposite('Kreita' , "worried" , "_fish" , "_OM", "")
    image kreita fish serious = CreateLiveComposite('Kreita' , "serious" , "_fish" , "", "")
    image kreita fish serious OM = CreateLiveComposite('Kreita' , "serious" , "_fish" , "_OM", "")
    image kreita fish determined = CreateLiveComposite('Kreita' , "determined" , "_fish" , "", "")
    image kreita fish determined OM = CreateLiveComposite('Kreita' , "determined" , "_fish" , "_OM", "")
    image kreita fish laugh = CreateLiveComposite('Kreita' , "laugh" , "_fish" , "", "")
    image kreita fish content CE = CreateLiveComposite('Kreita' , "content" , "_fish" , "_CE", "")
    image kreita fish fierce OM CE= CreateLiveComposite('Kreita' , "fierce" , "_fish" , "_OM_CE", "")
    image kreita fish grin2 CE S = CreateLiveComposite('Kreita' , "grin2_S" , "_fish" , "_CE", "")
    
    #Fish animated version
    image kreita fishAnimated grin2 = CreateLiveComposite('Kreita' , "grin2" , "_fishAnimated" , "", "")
    image kreita fishAnimated content = CreateLiveComposite('Kreita' , "content" , "_fishAnimated" , "", "")
    image kreita fishAnimated grin = CreateLiveComposite('Kreita' , "grin" , "_fishAnimated" , "", "")
    image kreita fishAnimated neutral = CreateLiveComposite('Kreita' , "content" , "_fishAnimated" , "", "")
    image kreita fishAnimated neutral OM = CreateLiveComposite('Kreita' , "content" , "_fishAnimated" , "_OM", "")
    image kreita fishAnimated serious = CreateLiveComposite('Kreita' , "content" , "_fishAnimated" , "", "")
    image kreita fishAnimated happy = CreateLiveComposite('Kreita' , "happy" , "_fishAnimated" , "", "")
    image kreita fishAnimated laugh = CreateLiveComposite('Kreita' , "laugh" , "_fishAnimated" , "", "")
    image kreita fishAnimated fierce = CreateLiveComposite('Kreita' , "fierce" , "_fishAnimated" , "", "")
    image kreita fishAnimated fierce OM = CreateLiveComposite('Kreita' , "fierce" , "_fishAnimated" , "_OM", "")

    
    ### Lexan Emotions ###
    image lexan angry = CreateLiveComposite('Lexan' , "angry" , "" , "", "glasses")
    image lexan annoyed = CreateLiveComposite('Lexan' , "annoyed" , "" , "", "glasses")
    image lexan annoyed OM = CreateLiveComposite('Lexan' , "annoyed" , "" , "_OM", "glasses")
    image lexan blushSmile = CreateLiveComposite('Lexan' , "blushSmile" , "" , "", "glasses")
    image lexan blushSmile OM = CreateLiveComposite('Lexan' , "blushSmile" , "" , "_OM", "glasses")
    image lexan confused = CreateLiveComposite('Lexan' , "confused" , "" , "", "glasses")
    image lexan confused OM = CreateLiveComposite('Lexan' , "confused" , "" , "_OM", "glasses")
    image lexan content = CreateLiveComposite('Lexan' , "content" , "" , "", "glasses")
    image lexan content OM = CreateLiveComposite('Lexan' , "content" , "" , "_OM", "glasses")
    image lexan determined = CreateLiveComposite('Lexan' , "determined" , "" , "", "glasses")
    image lexan determined OM = CreateLiveComposite('Lexan' , "determined" , "" , "_OM", "glasses")
    image lexan embarrassed = CreateLiveComposite('Lexan' , "embarrassed" , "" , "", "glasses")
    image lexan embarrassed OM = CreateLiveComposite('Lexan' , "embarrassed" , "" , "_OM", "glasses")
    image lexan grin = CreateLiveComposite('Lexan' , "grin" , "" , "", "glasses")
    image lexan grin OM = CreateLiveComposite('Lexan' , "grin" , "" , "_OM", "glasses")
    image lexan happy OM = CreateLiveComposite('Lexan' , "happy" , "" , "_OM", "glasses")
    image lexan laugh = CreateLiveComposite('Lexan' , "laugh" , "" , "", "glasses")
    image lexan neutral = CreateLiveComposite('Lexan' , "neutral" , "" , "", "glasses")
    image lexan neutral OM = CreateLiveComposite('Lexan' , "neutral" , "" , "_OM", "glasses")
    image lexan sad = CreateLiveComposite('Lexan' , "sad" , "" , "", "glasses")
    image lexan sad OM = CreateLiveComposite('Lexan' , "sad" , "" , "_OM", "glasses")
    image lexan sadSmile = CreateLiveComposite('Lexan' , "sadSmile" , "" , "", "glasses")
    image lexan sadSmile OM = CreateLiveComposite('Lexan' , "sadSmile" , "" , "_OM", "glasses")
    image lexan sceptical = CreateLiveComposite('Lexan' , "sceptical" , "" , "", "glasses")
    image lexan sceptical OM = CreateLiveComposite('Lexan' , "sceptical" , "" , "_OM", "glasses")
    image lexan serious = CreateLiveComposite('Lexan' , "serious" , "" , "", "glasses")
    image lexan serious OM = CreateLiveComposite('Lexan' , "serious" , "" , "_OM", "glasses")
    image lexan serious OM CE = CreateLiveComposite('Lexan' , "serious" , "" , "_OM_CE", "glasses")
    image lexan shocked = CreateLiveComposite('Lexan' , "shocked" , "" , "", "glasses")
    image lexan shocked OM = CreateLiveComposite('Lexan' , "shocked" , "" , "_OM", "glasses")
    image lexan shout = CreateLiveComposite('Lexan' , "shout" , "" , "", "glasses")
    image lexan strict = CreateLiveComposite('Lexan' , "strict" , "" , "", "glasses")
    image lexan strict OM = CreateLiveComposite('Lexan' , "strict" , "" , "_OM", "glasses")
    image lexan surprised = CreateLiveComposite('Lexan' , "surprised" , "" , "", "glasses")
    image lexan surprised OM = CreateLiveComposite('Lexan' , "surprised" , "" , "_OM", "glasses")
    image lexan surprisedBlush = CreateLiveComposite('Lexan' , "surprisedBlush" , "" , "", "glasses")
    image lexan surprisedBlush OM = CreateLiveComposite('Lexan' , "surprisedBlush" , "" , "_OM", "glasses")
    image lexan wink = CreateLiveComposite('Lexan' , "wink" , "" , "", "glasses")
    image lexan wink CE = CreateLiveComposite('Lexan' , "wink" , "" , "_CE", "glasses")
    image lexan wink OM = CreateLiveComposite('Lexan' , "wink" , "" , "_OM", "glasses")
    image lexan worried = CreateLiveComposite('Lexan' , "worried" , "" , "", "glasses")
    image lexan worried CE = CreateLiveComposite('Lexan' , "worried" , "" , "_CE", "glasses")
    image lexan worried OM = CreateLiveComposite('Lexan' , "worried" , "" , "_OM", "glasses")
    
    image lexan annoyed CE = CreateLiveComposite('Lexan' , "annoyed" , "" , "_CE", "glasses")
    image lexan content CE = CreateLiveComposite('Lexan' , "content" , "" , "_CE", "glasses")
    image lexan content OM CE = CreateLiveComposite('Lexan' , "content" , "" , "_OM_CE", "glasses")
    image lexan embarrassed CE = CreateLiveComposite('Lexan' , "embarrassed" , "" , "_CE", "glasses")
    image lexan embarrassed OM CE = CreateLiveComposite('Lexan' , "embarrassed" , "" , "_OM_CE", "glasses")
    image lexan grin CE = CreateLiveComposite('Lexan' , "grin" , "" , "_CE", "glasses")
    image lexan grin OM CE = CreateLiveComposite('Lexan' , "grin" , "" , "_OM_CE", "glasses")
    image lexan laugh CE = CreateLiveComposite('Lexan' , "laugh" , "" , "_CE", "glasses")
    image lexan neutral CE = CreateLiveComposite('Lexan' , "neutral" , "" , "_CE", "glasses")
    image lexan sad CE = CreateLiveComposite('Lexan' , "sad" , "" , "_CE", "glasses")
    image lexan sadSmile CE = CreateLiveComposite('Lexan' , "sadSmile" , "" , "_CE", "glasses")
    image lexan sadSmile OM CE = CreateLiveComposite('Lexan' , "sadSmile" , "" , "_OM_CE", "glasses")
    image lexan serious CE = CreateLiveComposite('Lexan' , "serious" , "" , "_CE", "glasses")
    image lexan worried CE = CreateLiveComposite('Lexan' , "worried" , "" , "_CE", "glasses")
    
    ### Prowen Emotions ###
    image prowen aggressive = CreateLiveComposite('Prowen' , "aggressive" , "" , "", "")
    image prowen aggressive OM = CreateLiveComposite('Prowen' , "aggressive" , "" , "_OM", "")
    image prowen annoyed = CreateLiveComposite('Prowen' , "annoyed" , "" , "", "")
    image prowen annoyed OM = CreateLiveComposite('Prowen' , "annoyed" , "" , "_OM", "")
    image prowen appalled = CreateLiveComposite('Prowen' , "appalled" , "" , "", "")
    image prowen appalled OM = CreateLiveComposite('Prowen' , "appalled" , "" , "_OM", "")
    image prowen content = CreateLiveComposite('Prowen' , "content" , "" , "", "")
    image prowen content OM = CreateLiveComposite('Prowen' , "content" , "" , "_OM", "")
    image prowen determined = CreateLiveComposite('Prowen' , "determined" , "" , "", "")
    image prowen determined OM = CreateLiveComposite('Prowen' , "determined" , "" , "_OM", "")
    image prowen forcedSmile = CreateLiveComposite('Prowen' , "forcedSmile" , "" , "", "")
    image prowen forcedSmile OM = CreateLiveComposite('Prowen' , "forcedSmile" , "" , "_OM", "")
    image prowen grin = CreateLiveComposite('Prowen' , "grin" , "" , "", "")
    image prowen grin OM = CreateLiveComposite('Prowen' , "grin" , "" , "_OM", "")
    image prowen neutral = CreateLiveComposite('Prowen' , "neutral" , "" , "", "")
    image prowen neutral OM = CreateLiveComposite('Prowen' , "neutral" , "" , "_OM", "")
    image prowen neutral CE = CreateLiveComposite('Prowen' , "neutral" , "" , "_CE", "")
    image prowen sad = CreateLiveComposite('Prowen' , "sad" , "" , "", "")
    image prowen sad OM = CreateLiveComposite('Prowen' , "sad" , "" , "_OM", "")
    image prowen sadSmile = CreateLiveComposite('Prowen' , "sadSmile" , "" , "", "")
    image prowen sadSmile OM = CreateLiveComposite('Prowen' , "sadSmile" , "" , "_OM", "")
    image prowen sceptical = CreateLiveComposite('Prowen' , "sceptical" , "" , "", "")
    image prowen sceptical OM = CreateLiveComposite('Prowen' , "sceptical" , "" , "_OM", "")
    image prowen serious = CreateLiveComposite('Prowen' , "serious" , "" , "", "")
    image prowen serious OM = CreateLiveComposite('Prowen' , "serious" , "" , "_OM", "")
    image prowen shocked = CreateLiveComposite('Prowen' , "shocked" , "" , "", "")
    image prowen shocked OM = CreateLiveComposite('Prowen' , "shocked" , "" , "_OM", "")
    image prowen smirk = CreateLiveComposite('Prowen' , "smirk" , "" , "", "")
    image prowen smirk OM = CreateLiveComposite('Prowen' , "smirk" , "" , "_OM", "")
    image prowen surprised = CreateLiveComposite('Prowen' , "surprised" , "" , "", "")
    image prowen surprised OM = CreateLiveComposite('Prowen' , "surprised" , "" , "_OM", "")
    image prowen tired = CreateLiveComposite('Prowen' , "tired" , "" , "", "")
    image prowen tired OM = CreateLiveComposite('Prowen' , "tired" , "" , "_OM", "")
    image prowen veryAnnoyed = CreateLiveComposite('Prowen' , "veryAnnoyed" , "" , "", "")
    image prowen veryAnnoyed OM = CreateLiveComposite('Prowen' , "veryAnnoyed" , "" , "_OM", "")
    image prowen worried = CreateLiveComposite('Prowen' , "worried" , "" , "", "")
    image prowen worried CE = CreateLiveComposite('Prowen' , "worried" , "" , "_CE", "")
    image prowen worried OM = CreateLiveComposite('Prowen' , "worried" , "" , "_OM", "")  

    image prowen aggressive CE = CreateLiveComposite('Prowen' , "aggressive" , "" , "_CE", "")
    image prowen appalled CE = CreateLiveComposite('Prowen' , "appalled" , "" , "_CE", "")
    image prowen forcedSmile CE = CreateLiveComposite('Prowen' , "forcedSmile" , "" , "_CE", "")
    image prowen neutral CE = CreateLiveComposite('Prowen' , "neutral" , "" , "_CE", "")
    image prowen nightFire closed CE = CreateLiveComposite('Prowen' , "nightFire" , "" , "_closed CE", "")
    image prowen nightFire open CE = CreateLiveComposite('Prowen' , "nightFire" , "" , "_open CE", "")
    image prowen sadSmile CE = CreateLiveComposite('Prowen' , "sadSmile" , "" , "_CE", "")
    image prowen serious CE = CreateLiveComposite('Prowen' , "serious" , "" , "_CE", "")
    image prowen serious OM CE = CreateLiveComposite('Prowen' , "serious" , "" , "_OM_CE", "")
    image prowen shocked OM CE = CreateLiveComposite('Prowen' , "shocked" , "" , "_OM_CE", "")
    image prowen tired CE = CreateLiveComposite('Prowen' , "tired" , "" , "_CE", "")
    image prowen tired OM CE = CreateLiveComposite('Prowen' , "tired" , "" , "_OM_CE", "")
    image prowen worried CE = CreateLiveComposite('Prowen' , "worried" , "" , "_CE", "")  
    
    #Tired version
    image prowen tired content = CreateLiveComposite('Prowen' , "content" , "_tired" , "", "")
    image prowen tired content OM = CreateLiveComposite('Prowen' , "content" , "_tired" , "_OM", "")
    
    #Nony version
    image prowen nony aggressive = CreateLiveComposite('Prowen' , "aggressive" , "_nony" , "", "")
    image prowen nony aggressive OM = CreateLiveComposite('Prowen' , "aggressive" , "_nony" , "_OM", "")
    image prowen nony content = CreateLiveComposite('Prowen' , "content" , "_nony" , "", "")
    image prowen nony content OM = CreateLiveComposite('Prowen' , "content" , "_nony" , "_OM", "")
    image prowen nony neutral = CreateLiveComposite('Prowen' , "neutral" , "_nony" , "", "")
    image prowen nony neutral OM = CreateLiveComposite('Prowen' , "neutral" , "_nony" , "_OM", "")
    image prowen nony tired CE = CreateLiveComposite('Prowen' , "tired" , "_nony" , "_CE", "")
    image prowen nony tired OM CE = CreateLiveComposite('Prowen' , "tired" , "_nony" , "_OM_CE", "")
    image prowen nony worried = CreateLiveComposite('Prowen' , "worried" , "_nony" , "", "")
    image prowen nony worried OM = CreateLiveComposite('Prowen' , "worried" , "_nony" , "_OM", "")
    
    ### Rett Emotions ###
    image rett aggressive = CreateLiveComposite('Rett' , "aggressive" , "" , "", "")
    image rett aggressive OM = CreateLiveComposite('Rett' , "aggressive" , "" , "_OM", "")
    image rett angry = CreateLiveComposite('Rett' , "angry" , "" , "", "")
    image rett angry OM = CreateLiveComposite('Rett' , "angry" , "" , "_OM", "")
    image rett confused = CreateLiveComposite('Rett' , "confused" , "" , "", "")
    image rett confused OM = CreateLiveComposite('Rett' , "confused" , "" , "_OM", "")
    image rett content = CreateLiveComposite('Rett' , "content" , "" , "", "")
    image rett content OM = CreateLiveComposite('Rett' , "content" , "" , "_OM", "")
    image rett embarrassedGrin = CreateLiveComposite('Rett' , "embarrassedGrin" , "" , "", "")
    image rett embarrassedGrin OM = CreateLiveComposite('Rett' , "embarrassedGrin" , "" , "_OM", "")
    image rett grin = CreateLiveComposite('Rett' , "grin" , "" , "", "")
    image rett grin S = CreateLiveComposite('Rett' , "grin_S" , "" , "", "")
    image rett laugh = CreateLiveComposite('Rett' , "laugh" , "" , "", "")
    image rett laugh ER = CreateLiveComposite('Rett' , "laugh" , "" , "_ER", "")
    image rett laugh S = CreateLiveComposite('Rett' , "laugh_S" , "" , "", "")
    image rett neutral = CreateLiveComposite('Rett' , "neutral" , "" , "", "")
    image rett neutral OM = CreateLiveComposite('Rett' , "neutral" , "" , "_OM", "")
    image rett neutral OM S = CreateLiveComposite('Rett' , "neutral_S" , "" , "_OM", "")
    image rett pouty = CreateLiveComposite('Rett' , "pouty" , "" , "", "")
    image rett pouty OM = CreateLiveComposite('Rett' , "pouty" , "" , "_OM", "")
    image rett sad = CreateLiveComposite('Rett' , "sad" , "" , "", "")
    image rett sad OM = CreateLiveComposite('Rett' , "sad" , "" , "_OM", "")
    image rett sadSmile = CreateLiveComposite('Rett' , "sadSmile" , "" , "", "")
    image rett sadSmile OM = CreateLiveComposite('Rett' , "sadSmile" , "" , "_OM", "")
    image rett sceptical = CreateLiveComposite('Rett' , "sceptical" , "" , "", "")
    image rett sceptical OM = CreateLiveComposite('Rett' , "sceptical" , "" , "_OM", "")
    image rett shocked = CreateLiveComposite('Rett' , "shocked" , "" , "", "")
    image rett shocked OM = CreateLiveComposite('Rett' , "shocked" , "" , "_OM", "")
    image rett smirk = CreateLiveComposite('Rett' , "smirk" , "" , "", "")
    image rett smirk OM = CreateLiveComposite('Rett' , "smirk" , "" , "_OM", "")
    image rett surprised = CreateLiveComposite('Rett' , "surprised" , "" , "", "")
    image rett surprised OM = CreateLiveComposite('Rett' , "surprised" , "" , "_OM", "")
    image rett wink = CreateLiveComposite('Rett' , "wink" , "" , "", "")
    image rett worried = CreateLiveComposite('Rett' , "worried" , "" , "", "")
    image rett worried CE = CreateLiveComposite('Rett' , "worried" , "" , "_CE", "")
    image rett worried OM = CreateLiveComposite('Rett' , "worried" , "" , "_OM", "")  

    image rett content CE = CreateLiveComposite('Rett' , "content" , "" , "_CE", "")
    image rett grin CE = CreateLiveComposite('Rett' , "grin" , "" , "_CE", "")
    image rett grin CE S = CreateLiveComposite('Rett' , "grin_S" , "" , "_CE", "")
    image rett laugh S  CE = CreateLiveComposite('Rett' , "laugh_S" , "" , "_CE", "")
    image rett neutral CE = CreateLiveComposite('Rett' , "neutral" , "" , "_CE", "")
    image rett sad CE = CreateLiveComposite('Rett' , "sad" , "" , "_CE", "")
    image rett sceptical CE = CreateLiveComposite('Rett' , "sceptical" , "" , "_CE", "")
    image rett worried CE = CreateLiveComposite('Rett' , "worried" , "" , "_CE", "")  
    
    #Injured version
    image rett injured content = CreateLiveComposite('Rett' , "content" , "_injured" , "", "")
    image rett injured content OM = CreateLiveComposite('Rett' , "content" , "_injured" , "_OM", "")
    image rett injured neutral = CreateLiveComposite('Rett' , "neutral" , "_injured" , "", "")
    image rett injured neutral OM = CreateLiveComposite('Rett' , "neutral" , "_injured" , "_OM", "")
    image rett injured worried = CreateLiveComposite('Rett' , "worried" , "_injured" , "", "")
    image rett injured worried CE = CreateLiveComposite('Rett' , "worried" , "_injured" , "_CE", "")
    image rett injured worried OM = CreateLiveComposite('Rett' , "worried" , "_injured" , "_OM", "") 
    image rett injured wink = CreateLiveComposite('Rett' , "wink" , "_injured" , "", "")
    image rett injured smirk = CreateLiveComposite('Rett' , "smirk" , "_injured" , "", "")
    image rett injured smirk OM = CreateLiveComposite('Rett' , "smirk" , "_injured" , "_OM", "")
    
    #Injured2 version
    image rett injured2 content = CreateLiveComposite('Rett' , "content" , "_injured2" , "", "")
    image rett injured2 content OM = CreateLiveComposite('Rett' , "content" , "_injured2" , "_OM", "")
    image rett injured2 neutral = CreateLiveComposite('Rett' , "neutral" , "_injured2" , "", "")
    image rett injured2 neutral OM = CreateLiveComposite('Rett' , "neutral" , "_injured2" , "_OM", "")
    image rett injured2 worried = CreateLiveComposite('Rett' , "worried" , "_injured2" , "", "")
    image rett injured2 worried CE = CreateLiveComposite('Rett' , "worried" , "_injured2" , "_CE", "")
    image rett injured2 worried OM = CreateLiveComposite('Rett' , "worried" , "_injured2" , "_OM", "") 
    image rett injured2 wink = CreateLiveComposite('Rett' , "wink" , "_injured2" , "", "")
    image rett injured2 smirk = CreateLiveComposite('Rett' , "smirk" , "_injured2" , "", "")
    image rett injured2 smirk OM = CreateLiveComposite('Rett' , "smirk" , "_injured2" , "_OM", "")
    
    #operation version
    image rett operation = "img/sprites/Rett/R_operation.png"
    
    ### Ranan Emotions ###
    image ranan content = CreateLiveComposite('Ranan' , "content" , "" , "", "")
    image ranan content OM = CreateLiveComposite('Ranan' , "content" , "" , "_OM", "")
    image ranan determined = CreateLiveComposite('Ranan' , "determined" , "" , "", "")
    image ranan determined OM = CreateLiveComposite('Ranan' , "determined" , "" , "_OM", "")
    image ranan grim = CreateLiveComposite('Ranan' , "grim" , "" , "", "")
    image ranan grim OM = CreateLiveComposite('Ranan' , "grim" , "" , "_OM", "")  
    image ranan hateful = CreateLiveComposite('Ranan' , "hateful" , "" , "", "")
    image ranan hateful OM = CreateLiveComposite('Ranan' , "hateful" , "" , "_OM", "") 
    image ranan laugh = CreateLiveComposite('Ranan' , "laugh" , "" , "", "")    
    image ranan melancholic = CreateLiveComposite('Ranan' , "melancholic" , "" , "", "")
    image ranan melancholic OM = CreateLiveComposite('Ranan' , "melancholic" , "" , "_OM", "")
    image ranan neutral = CreateLiveComposite('Ranan' , "neutral" , "" , "", "")
    image ranan neutral OM = CreateLiveComposite('Ranan' , "neutral" , "" , "_OM", "")
    image ranan neutral2 = CreateLiveComposite('Ranan' , "neutral2" , "" , "", "")
    image ranan neutral2 OM = CreateLiveComposite('Ranan' , "neutral2" , "" , "_OM", "")
    image ranan obsessive = CreateLiveComposite('Ranan' , "obsessive" , "" , "", "")
    image ranan obsessive OM = CreateLiveComposite('Ranan' , "obsessive" , "" , "_OM", "")  
    image ranan obsessive2 = CreateLiveComposite('Ranan' , "obsessive2" , "" , "", "")
    image ranan obsessive2 OM = CreateLiveComposite('Ranan' , "obsessive2" , "" , "_OM", "")   
    image ranan obsessiveLaugh = CreateLiveComposite('Ranan' , "obsessiveLaugh" , "" , "", "")
    image ranan resentful = CreateLiveComposite('Ranan' , "resentful" , "" , "", "")
    image ranan resentful OM = CreateLiveComposite('Ranan' , "resentful" , "" , "_OM", "") 
    image ranan sad = CreateLiveComposite('Ranan' , "sad" , "" , "", "")
    image ranan sad OM = CreateLiveComposite('Ranan' , "sad" , "" , "_OM", "") 
    image ranan sadSmile = CreateLiveComposite('Ranan' , "sadSmile" , "" , "", "")
    image ranan sadSmile OM = CreateLiveComposite('Ranan' , "sadSmile" , "" , "_OM", "")  
    image ranan sceptical = CreateLiveComposite('Ranan' , "sceptical" , "" , "", "")
    image ranan sceptical OM = CreateLiveComposite('Ranan' , "sceptical" , "" , "_OM", "")  
    image ranan shocked = CreateLiveComposite('Ranan' , "shocked" , "" , "", "")
    image ranan shocked OM = CreateLiveComposite('Ranan' , "shocked" , "" , "_OM", "")  
    image ranan smile = CreateLiveComposite('Ranan' , "smile" , "" , "", "")
    image ranan smile OM = CreateLiveComposite('Ranan' , "smile" , "" , "_OM", "")
    image ranan smirk = CreateLiveComposite('Ranan' , "smirk" , "" , "", "")
    image ranan smirk OM = CreateLiveComposite('Ranan' , "smirk" , "" , "_OM", "")
    image ranan surprised = CreateLiveComposite('Ranan' , "surprised" , "" , "", "")
    image ranan surprised OM = CreateLiveComposite('Ranan' , "surprised" , "" , "_OM", "")
    image ranan verySad = CreateLiveComposite('Ranan' , "verySad" , "" , "", "")
    image ranan verySad OM = CreateLiveComposite('Ranan' , "verySad" , "" , "_OM", "")  
    image ranan worried = CreateLiveComposite('Ranan' , "worried" , "" , "", "")
    image ranan worried OM = CreateLiveComposite('Ranan' , "worried" , "" , "_OM", "")
    image ranan worried2 = CreateLiveComposite('Ranan' , "worried2" , "" , "", "")
    image ranan worried2 OM = CreateLiveComposite('Ranan' , "worried2" , "" , "_OM", "") 

    image ranan content OM CE = CreateLiveComposite('Ranan' , "content" , "" , "_OM_CE", "")
    image ranan grim CE = CreateLiveComposite('Ranan' , "grim" , "" , "_CE", "")
    image ranan hateful OM CE = CreateLiveComposite('Ranan' , "hateful" , "" , "_OM_CE", "")
    image ranan melancholic CE = CreateLiveComposite('Ranan' , "melancholic" , "" , "_CE", "")
    image ranan neutral CE = CreateLiveComposite('Ranan' , "neutral" , "" , "_CE", "")
    image ranan neutral OM CE = CreateLiveComposite('Ranan' , "neutral" , "" , "_OM_CE", "")
    image ranan obsessive OM CE = CreateLiveComposite('Ranan' , "obsessive" , "" , "_OM_CE", "")
    image ranan resentful OM CE = CreateLiveComposite('Ranan' , "resentful" , "" , "_OM_CE", "")
    image ranan sadSmile CE = CreateLiveComposite('Ranan' , "sadSmile" , "" , "_CE", "")
    image ranan smirk CE = CreateLiveComposite('Ranan' , "smirk" , "" , "_CE", "")
    image ranan smirk OM CE = CreateLiveComposite('Ranan' , "smirk" , "" , "_OM_CE", "")
    image ranan verySad OM CE = CreateLiveComposite('Ranan' , "verySad" , "" , "_OM_CE", "")
    
    #Past version
    image ranan past content = CreateLiveComposite('Ranan' , "content" , "_past" , "", "")
    image ranan past content OM = CreateLiveComposite('Ranan' , "content" , "_past" , "_OM", "")
    image ranan past grim = CreateLiveComposite('Ranan' , "grim" , "_past" , "", "")
    image ranan past neutral = CreateLiveComposite('Ranan' , "neutral" , "_past" , "", "")
    image ranan past neutral OM = CreateLiveComposite('Ranan' , "neutral" , "_past" , "_OM", "")
    image ranan past resentful = CreateLiveComposite('Ranan' , "resentful" , "_past" , "", "")
    image ranan past sad = CreateLiveComposite('Ranan' , "sad" , "_past" , "", "")
    image ranan past sad OM = CreateLiveComposite('Ranan' , "sad" , "_past" , "_OM", "")
    image ranan past sadSmile = CreateLiveComposite('Ranan' , "sadSmile" , "_past" , "", "")
    image ranan past sadSmile OM = CreateLiveComposite('Ranan' , "sadSmile" , "_past" , "_OM", "")
    image ranan past sceptical OM = CreateLiveComposite('Ranan' , "sceptical" , "_past" , "_OM", "")
    image ranan past smile = CreateLiveComposite('Ranan' , "smile" , "_past" , "", "")
    image ranan past smile OM = CreateLiveComposite('Ranan' , "smile" , "_past" , "_OM", "")
    image ranan past surprised = CreateLiveComposite('Ranan' , "surprised" , "_past" , "", "")
    image ranan past worried = CreateLiveComposite('Ranan' , "worried" , "_past" , "", "")
    image ranan past worried OM = CreateLiveComposite('Ranan' , "worried" , "_past" , "_OM", "")

    ### Wriane Emotions ###
    image wriane angry = CreateLiveComposite('Wriane' , "angry" , "" , "", "")
    image wriane annoyed = CreateLiveComposite('Wriane' , "annoyed" , "" , "", "")
    image wriane annoyed OM = CreateLiveComposite('Wriane' , "annoyed" , "" , "_OM", "")
    image wriane content  = CreateLiveComposite('Wriane' , "content" , "" , "", "")
    image wriane content OM = CreateLiveComposite('Wriane' , "content" , "" , "_OM", "")
    image wriane happy = CreateLiveComposite('Wriane' , "happy" , "" , "", "")
    image wriane laugh = CreateLiveComposite('Wriane' , "laugh" , "" , "", "")
    image wriane neutral = CreateLiveComposite('Wriane' , "neutral" , "" , "", "")
    image wriane neutral OM = CreateLiveComposite('Wriane' , "neutral" , "" , "_OM", "")  
    image wriane serious = CreateLiveComposite('Wriane' , "serious" , "" , "", "")
    image wriane serious OM = CreateLiveComposite('Wriane' , "serious" , "" , "_OM", "")
    image wriane smile = CreateLiveComposite('Wriane' , "smile" , "" , "", "")
    image wriane surprised = CreateLiveComposite('Wriane' , "surprised" , "" , "", "")    
    image wriane worried = CreateLiveComposite('Wriane' , "worried" , "" , "", "")
    image wriane worried OM = CreateLiveComposite('Wriane' , "worried" , "" , "_OM", "")

    image wriane neutral OM CE = CreateLiveComposite('Wriane' , "neutral" , "" , "_OM_CE", "")
    image wriane neutral CE = CreateLiveComposite('Wriane' , "neutral" , "" , "_CE", "")
    image wriane serious CE = CreateLiveComposite('Wriane' , "serious" , "" , "_CE", "")
    image wriane smile CE = CreateLiveComposite('Wriane' , "smile" , "" , "_CE", "")
    
    ### Voya Emotions ###
    image voyaGlow = "img/sprites/voya/voyaGlow.png"
    
    image voya content = CreateLiveComposite('Voya' , "content" , "" , "", "")
    image voya content OM = CreateLiveComposite('Voya' , "content" , "" , "_OM", "")
    image voya determined = CreateLiveComposite('Voya' , "determined" , "" , "", "")
    image voya determined OM = CreateLiveComposite('Voya' , "determined" , "" , "_OM", "")
    image voya neutral = CreateLiveComposite('Voya' , "neutral" , "" , "", "")
    image voya neutral OM = CreateLiveComposite('Voya' , "neutral" , "" , "_OM", "")
    image voya sad = CreateLiveComposite('Voya' , "sad" , "" , "", "")
    image voya sad OM = CreateLiveComposite('Voya' , "sad" , "" , "_OM", "")
    image voya sadSmile = CreateLiveComposite('Voya' , "sadSmile" , "" , "", "")
    image voya sadSmile OM = CreateLiveComposite('Voya' , "sadSmile" , "" , "_OM", "")
    image voya scared = CreateLiveComposite('Voya' , "scared" , "" , "", "")
    image voya scared OM = CreateLiveComposite('Voya' , "scared" , "" , "_OM", "")
    image voya serious = CreateLiveComposite('Voya' , "serious" , "" , "", "")
    image voya serious OM = CreateLiveComposite('Voya' , "serious" , "" , "_OM", "")
    image voya shocked = CreateLiveComposite('Voya' , "shocked" , "" , "", "")
    image voya shocked OM = CreateLiveComposite('Voya' , "shocked" , "" , "_OM", "")
    image voya surprised = CreateLiveComposite('Voya' , "surprised" , "" , "", "")
    image voya surprised OM = CreateLiveComposite('Voya' , "surprised" , "" , "_OM", "")
    image voya verySad = CreateLiveComposite('Voya' , "verySad" , "" , "", "")
    image voya verySad OM = CreateLiveComposite('Voya' , "verySad" , "" , "_OM", "")
    image voya worried = CreateLiveComposite('Voya' , "worried" , "" , "", "")
    image voya worried OM = CreateLiveComposite('Voya' , "worried" , "" , "_OM", "")

    image voya content CE = CreateLiveComposite('Voya' , "content" , "" , "_CE", "")
    image voya content OM CE = CreateLiveComposite('Voya' , "content" , "" , "_OM_CE", "")
    image voya sad CE = CreateLiveComposite('Voya' , "sad" , "" , "_CE", "")
    image voya sad OM CE = CreateLiveComposite('Voya' , "sad" , "" , "_OM_CE", "")
    image voya sadSmile CE = CreateLiveComposite('Voya' , "sadSmile" , "" , "_CE", "")
    image voya verySad CE = CreateLiveComposite('Voya' , "verySad" , "" , "_CE", "")

    #Past version
    image voya past content = CreateLiveComposite('Voya' , "content" , "_past" , "", "")
    image voya past content CE = CreateLiveComposite('Voya' , "content" , "_past" , "_CE", "")
    image voya past content OM = CreateLiveComposite('Voya' , "content" , "_past" , "_OM", "")
    image voya past neutral = CreateLiveComposite('Voya' , "neutral" , "_past" , "", "")
    image voya past neutral OM = CreateLiveComposite('Voya' , "neutral" , "_past" , "_OM", "")
    image voya past sad = CreateLiveComposite('Voya' , "sad" , "_past" , "", "")
    image voya past sad OM = CreateLiveComposite('Voya' , "sad" , "_past" , "_OM", "")
    image voya past sad OM CE = CreateLiveComposite('Voya' , "sad" , "_past" , "_OM_CE", "")
    image voya past sadSmile = CreateLiveComposite('Voya' , "sadSmile" , "_past" , "", "")
    image voya past sadSmile OM = CreateLiveComposite('Voya' , "sadSmile" , "_past" , "_OM", "")
    image voya past surprised = CreateLiveComposite('Voya' , "surprised" , "_past" , "", "")
    image voya past surprised OM = CreateLiveComposite('Voya' , "surprised" , "_past" , "_OM", "")
    image voya past worried = CreateLiveComposite('Voya' , "worried" , "_past" , "", "")
    image voya past worried OM = CreateLiveComposite('Voya' , "worried" , "_past" , "_OM", "")

    
    ### Drae Emotions ###
    image drae neutral = CreateLiveComposite('Drae' , "neutral" , "" , "", "")
    image drae neutral OM = CreateLiveComposite('Drae' , "neutral" , "" , "_OM", "")
    image drae resentful = CreateLiveComposite('Drae' , "resentful" , "" , "", "")
    image drae resentful OM = CreateLiveComposite('Drae' , "resentful" , "" , "_OM", "")
    image drae sceptical = CreateLiveComposite('Drae' , "sceptical" , "" , "", "")
    image drae sceptical OM = CreateLiveComposite('Drae' , "sceptical" , "" , "_OM", "")
    image drae serious = CreateLiveComposite('Drae' , "serious" , "" , "", "")
    image drae serious OM = CreateLiveComposite('Drae' , "serious" , "" , "_OM", "")
    image drae smirk = CreateLiveComposite('Drae' , "smirk" , "" , "", "")
    image drae smirk OM = CreateLiveComposite('Drae' , "smirk" , "" , "_OM", "")
    image drae strict = CreateLiveComposite('Drae' , "strict" , "" , "", "")
    image drae strict OM = CreateLiveComposite('Drae' , "strict" , "" , "_OM", "")    
    
    #Past version
    image drae past neutral = CreateLiveComposite('Drae' , "neutral" , "_past" , "", "")
    image drae past neutral OM = CreateLiveComposite('Drae' , "neutral" , "_past" , "_OM", "")
    image drae past sceptical OM = CreateLiveComposite('Drae' , "sceptical" , "_past" , "_OM", "")
    image drae past smirk = CreateLiveComposite('Drae' , "smirk" , "_past" , "", "")
    image drae past strict = CreateLiveComposite('Drae' , "strict" , "_past" , "", "")
    image drae past strict OM = CreateLiveComposite('Drae' , "strict" , "_past" , "_OM", "")