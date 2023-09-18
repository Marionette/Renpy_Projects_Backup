
init python:
    #-----------------------------------------------------------------------------------
    def CreateLiveCompositeCharacter(_emotion="", _hair=""):    
      
      #Initial values
      charWidth = 376
      charHeight = 750
      xoff = 0
      yoff = 0
      emotion = _emotion
          
        
      ### Live Composite function ###
      return LiveComposite( 
      (charWidth, charHeight),
      (xoff, yoff), "images/sprites/composite/base.png",
      (xoff, yoff), "images/sprites/composite/hair_%s_colour.png"%(_hair),
      (xoff, yoff), "images/sprites/composite/hair_%s_outline.png"%(_hair),
      (xoff, yoff), "images/sprites/composite/face_%s.png"%(emotion))   
      
    #-----------------------------------------------------------------------

init:
    # The script of the game goes in this file.

    # Declare characters used by this game. The color argument colorizes the
    # name of the character.

    define e = Character("Eileen")
    define jon = Character("Jonah")
    define mal = Character("Mallory")
                      
    define customer = DynamicCharacter('Customer_Name')
    
    #-----------------------------------------------------------------------
    
    image eileen happy = im.FactorScale("images/sprites/Sprite Female Mage Smirk01.png", 0.65,0.65)
    
    #mc
    image jonah neutral = CreateLiveCompositeCharacter('neutral', '19')
    image jonah angry = CreateLiveCompositeCharacter('angry', '19')
    image jonah blush = CreateLiveCompositeCharacter('blush', '19')
    image jonah bored = CreateLiveCompositeCharacter('bored', '19')
    image jonah embarrassed = CreateLiveCompositeCharacter('embarrassed', '19')
    image jonah happy = CreateLiveCompositeCharacter('happy', '19')
    image jonah panic = CreateLiveCompositeCharacter('panic', '19')
    image jonah sad = CreateLiveCompositeCharacter('sad', '19')
    image jonah surprised = CreateLiveCompositeCharacter('surprised', '19')
    image jonah vhappy = CreateLiveCompositeCharacter('very-happy', '19')
    
    
    #Loli ojo
    image mallory neutral = CreateLiveCompositeCharacter('neutral', '09')
    image mallory angry = CreateLiveCompositeCharacter('angry', '09')
    image mallory blush = CreateLiveCompositeCharacter('blush', '09')
    image mallory bored = CreateLiveCompositeCharacter('bored', '09')
    image mallory embarrassed = CreateLiveCompositeCharacter('embarrassed', '09')
    image mallory happy = CreateLiveCompositeCharacter('happy', '09')
    image mallory panic = CreateLiveCompositeCharacter('panic', '09')
    image mallory sad = CreateLiveCompositeCharacter('sad', '09')
    image mallory surprised = CreateLiveCompositeCharacter('surprised', '09')
    image mallory vhappy = CreateLiveCompositeCharacter('very-happy', '09')


    #-----------------------------------------------------------------------
    
    image bg black = Solid("#000000")
    image bg white = Solid("#ffffff")
    image bg marketplace_day = "images/bg/marketplace_day.png"