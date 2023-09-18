init:
    
    ######### MISC DEFINES #############
    $NumberStringList=["zero",
                        "one"  ,
                        "two"  ,
                        "three",
                        "four" ,
                        "five" ,
                        "six"  ,
                        "seven",
                        "eight",
                        "nine" ,
                        "ten"]
                        
    define slow_dissolve = Dissolve(2.0)
                        
    # Declare characters used by this game. The color argument colorizes the
    # name of the character.

    ######### CHARACTER DEFINES #############
    define ate = Character("Ate Yasmin")
    define mom = Character("Mom")
    define cris = Character("Cris", image="CRIS")
    define narrator = Character(None, image="CRIS")
    define girl = Character("Girl")
    define stranger = Character("Stranger")
    define rafa = Character("Rafa")
    define sami = Character("Sami")
    define limbokin = Character("Limbokin")
    define brave = Character("{size=-15}Brave Limbokin{/size}")
    define no1 = Character("{size=-15}Limbokin No. 1{/size}")
    define no2 = Character("{size=-15}Limbokin No. 2{/size}")
    define no3 = Character("{size=-15}Limbokin No. 3{/size}")
    define no4 = Character("{size=-15}Limbokin No. 4{/size}")
    define no5 = Character("{size=-15}Limbokin No. 5{/size}")
    define no6 = Character("{size=-15}Limbokin No. 6{/size}")
    define no7 = Character("{size=-15}Limbokin No. 7{/size}")
    define you = Character("You")
    define nvlnarrator = Character(None, kind = nvl,  what_xalign=0.5)
    
  
    ######### SOUND DEFINES #############
    #$SUBDUED = "audio/SUBDUED.ogg"
    $TENSION = "audio/TENSION.ogg"
    #$SINISTER = "audio/SINISTER.ogg"
    $MINIGAME = "audio/MINIGAME.ogg"
    $THEMESONG = "audio/THEMESONG.ogg"
    $BACKGROUND = "audio/BACKGROUND.ogg"
    $HORROR = "audio/HORROR.ogg"
    
    ######### CG/BG IMAGE DEFINES #############
    image black = Solid("#000000")  
    image bg black = Solid("#000000")     
    image bg white = Solid("#ffffff")
    #image bg whitescreen = Solid("#b7b5b6")
    
    #TODO REPLACE #Backgrounds
    image NVLMODE = Solid("#000000")  
    image bg bedroom = "images/bg/BEDROOM.png"
    image bg purgatory = "images/bg/PURGATORY.png"
    image bg riverstyx = "images/bg/RIVERSTYX.png"
    image bg sky = "images/bg/SKY.png"
    #TODO REPLACE #CG images
    image cg closet = "images/cg/CLOSET.png"
    image cg flight = "images/cg/FLIGHT.png"
    image cg limbokin = "images/cg/LIMBOKIN.png"
    image cg limbokin_grey = "images/cg/LIMBOKIN_GREY.png"
    image cg ending1 = "images/cg/ENDING1.png"
    image cg ending2 = "images/cg/ENDING2.png"
    image cg ending3 = "images/cg/ENDING3.png"
    image cg doodle1 = "images/cg/CG DOODLE1.png"
    image cg doodle2 = "images/cg/CG DOODLE2.png"
    image cg doodle3 = "images/cg/CG DOODLE3.png"
    image cg doodle4 = "images/cg/CG DOODLE4.png"

    #TODO REPLACE #Characters
    image ATE YASMIN ANGRY = "images/sprites/ATE YASMIN ANGRY.png"
    image ATE YASMIN POKERFACE = "images/sprites/ATE YASMIN POKERFACE.png"
    image ATE YASMIN SAD = "images/sprites/ATE YASMIN SAD.png"
    image ATE YASMIN SHOCK = "images/sprites/ATE YASMIN SHOCK.png"
    image ATE YASMIN SMILE = "images/sprites/ATE YASMIN SMILE.png"
    
    image CRIS ANGRY = "images/sprites/CRIS BLANK.png"
    image CRIS LAUGH = "images/sprites/CRIS BLANK.png"
    image CRIS POKERFACE = "images/sprites/CRIS BLANK.png"
    image CRIS SAD = "images/sprites/CRIS BLANK.png"
    image CRIS SHOCK = "images/sprites/CRIS BLANK.png"
    image CRIS SMILE = "images/sprites/CRIS BLANK.png"
    
    image side CRIS ANGRY = "images/sprites/CRIS ANGRY.png"
    image side CRIS LAUGH = "images/sprites/CRIS LAUGH.png"
    image side CRIS POKERFACE = "images/sprites/CRIS POKERFACE.png"
    image side CRIS SAD = "images/sprites/CRIS SAD.png"
    image side CRIS SHOCK = "images/sprites/CRIS SHOCK.png"
    image side CRIS SMILE = "images/sprites/CRIS SMILE.png"
    
    image RAFA ANGRY = "images/sprites/RAFA ANGRY.png"
    image RAFA LAUGH = "images/sprites/RAFA LAUGH.png"
    image RAFA POKERFACE = "images/sprites/RAFA POKERFACE.png"
    image RAFA SAD = "images/sprites/RAFA SAD.png"
    image RAFA SHOCK = "images/sprites/RAFA SHOCK.png"
    image RAFA SMILE = "images/sprites/RAFA SMILE.png"
    
    image SAMI ANGRY = "images/sprites/SAMI ANGRY.png"
    image SAMI POKERFACE = "images/sprites/SAMI POKERFACE.png"
    image SAMI SHOCK = "images/sprites/SAMI SHOCK.png"
    image SAMI SMILE = "images/sprites/SAMI SMILE.png"
    
    image WINGLESSSAMI ANGRY = "images/sprites/WINGLESSSAMI ANGRY.png"
    image WINGLESSSAMI POKERFACE = "images/sprites/WINGLESSSAMI POKERFACE.png"
    image WINGLESSSAMI SHOCK = "images/sprites/WINGLESSSAMI SHOCK.png"
    image WINGLESSSAMI SMILE = "images/sprites/WINGLESSSAMI SMILE.png"