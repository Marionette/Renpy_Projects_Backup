init:

    #------------ VARIABLES ---------------#
    $shouldRepeat = False
    $shouldEndEarly = False
    $count_Loops = 0
    $girl_following = False
    $boy_following = False

    $breakfast_to_go_choice = "None"
    $detour_choice = "None"
    
    
    #Character Defines
    # Declare characters used by this game. The color argument colorizes the
    # name of the character.
    $cg_name = "???" 
    $ab_name = "???"
    $ts_name = "???"

    define mc = Character("Martin", image="martin") #Martin Clarke
    define mci = Character('Martin', what_prefix="( ", what_suffix=" )", image="martin") # MC inner thoughts
    
    define cg = DynamicCharacter("cg_name") #Charles Grove
    define ab = DynamicCharacter("ab_name") #Alex Barr   
    define ts = DynamicCharacter("ts_name") #Moirai the time spider

    define dog = Character("Dog") #Dog
    
    define qq = Character("???") # ??? unknown speaker


    #------------ IMAGES ---------------#
    #Character Images

    #MC
    image martin normal     = "images/sprite/mc/Male_01_blank.png"
    image martin angry      = "images/sprite/mc/Male_01_blank.png"
    image martin shy        = "images/sprite/mc/Male_01_blank.png"
    image martin sad        = "images/sprite/mc/Male_01_blank.png"
    image martin smile      = "images/sprite/mc/Male_01_blank.png"
    image martin surprise   = "images/sprite/mc/Male_01_blank.png"
    
    image side martin normal     = "images/sprite/mc/Male_01_Side_Normal.png"
    image side martin angry      = "images/sprite/mc/Male_01_Side_Anger.png" 
    image side martin shy        = "images/sprite/mc/Male_01_Side_BeShy.png" 
    image side martin sad        = "images/sprite/mc/Male_01_Side_Sadness.png" 
    image side martin smile      = "images/sprite/mc/Male_01_Side_Smile.png" 
    image side martin surprise   = "images/sprite/mc/Male_01_Side_Surprise.png" 

    # Falling Boy
    image charlie normal    = "images/sprite/boy/Male_04_Normal.png" 
    image charlie angry     = "images/sprite/boy/Male_04_Anger.png" 
    image charlie shy       = "images/sprite/boy/Male_04_BeShy.png" 
    image charlie sad       = "images/sprite/boy/Male_04_Sadness.png" 
    image charlie smile     = "images/sprite/boy/Male_04_Smile.png" 
    image charlie surprise  = "images/sprite/boy/Male_04_Surprise.png" 
    ## Dog
    image dog normal  = "images/sprite/dog.png" 

    # Delinquent Girl
    # Delinquent Girl(Glasses)
    image alex normal    = "images/sprite/girl/Female_02_Normal.png" 
    image alex angry     = "images/sprite/girl/Female_02_Anger.png" 
    image alex shy       = "images/sprite/girl/Female_02_BeShy.png" 
    image alex sad       = "images/sprite/girl/Female_02_Sadness.png" 
    image alex smile     = "images/sprite/girl/Female_02_Smile.png" 
    image alex surprise  = "images/sprite/girl/Female_02_Surprise.png" 

    # Sister

    # Time master
    image moirai normal    = im.FactorScale("images/sprite/spider/spidergalneutral.png", .7) 
    image moirai happy    = im.FactorScale("images/sprite/spider/spidergalhappy.png" , .7)
    image moirai sad    = im.FactorScale("images/sprite/spider/spidergalsad.png" , .7)
    image moirai angry    = im.FactorScale("images/sprite/spider/spidergalupset.png" , .7)

    #Background images
    image bg black = Solid("#000000")   

    #Locations:
    # Bedroom
    image bg bedroom = "images/bg/room_morning_light_off.jpg"
    image bg bedroom grey = "images/bg/room_grey.png"
    # Kitchen
    image bg kitchen = "images/bg/kitchen_day.png"
    # Crossing/Corner
    image bg intersection = "images/bg/street_bg_morning.png"
    # Narrow street
    image bg passage = "images/bg/street_background_01.png"
    # Park
    image bg park = "images/bg/park.png"
    # Side Streets
    image bg sidestreets = "images/bg/street.png"
    # School Gate
    image bg schoolgate = "images/bg/generic_school_gate.png"
    image bg schoolgate grey = "images/bg/generic_school_gate_grey.png"

    #CG Images
    #Extras


    #------------ Audio ---------------#
    #Music
    $music_mystical = "audio/music/F4_v1.mp3"
    #Sounds  
    

    #TODO    
    #$sound_birds = "audio/sound/djhalleu__stavanger-nightingale1.ogg"