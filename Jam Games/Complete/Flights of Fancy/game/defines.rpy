init:
    # The script of the game goes in this file.

    # Declare characters used by this game. The color argument colorizes the
    # name of the character.

    ######### CHARACTER DEFINES #############
    #define nvl_narr = Character(None, kind=nvl)
    define koizumi_riyuu = Character("<koizumi_riyuu>", kind=nvl, what_prefix="\"", what_suffix="\"")
    define umi404 = Character("<Umi404>", kind=nvl, what_prefix="\"", what_suffix="\"")
    
    define ate = Character("ATE", what_prefix="\"", what_suffix="\"")
    define bee = Character("BEE", what_prefix="\"", what_suffix="\"")
    define mom = Character("MOM", what_prefix="\"", what_suffix="\"")
    define karis = Character("KARIS", what_prefix="\"", what_suffix="\"")
    define vida = Character("VIDA", what_prefix="\"", what_suffix="\"")
    define pineda = Character("MRS. PINEDA", what_prefix="\"", what_suffix="\"")
    define ocampo = Character("MRS. OCAMPO", what_prefix="\"", what_suffix="\"")
    define mystery = Character("A MYSTERIOUS VOICE", what_prefix="\"", what_suffix="\"")
    define umi = Character("UMI", what_prefix="\"", what_suffix="\"")
    define umi_q = Character("UMI (?)", what_prefix="\"", what_suffix="\"")

    ######### SOUND DEFINES #############
    #TODO replace with actual music files
    $DREAMS = "audio/music/DREAMS.mp3"
    $INSPIRING = "audio/music/INSPIRING.mp3"
    $PARANOIA = "audio/music/PARANOIA.mp3"
    $SLICE_OF_LIFE = "audio/music/SLICE_OF_LIFE.mp3"

    ######### CG/BG IMAGE DEFINES #############
    image black = Solid("#000000")  
    image bg black = Solid("#000000")     
    image bg white = Solid("#ffffff") 
    image bg white = Solid("#ffffff") 
    image bg sketchbook = "gui/game_menu.png"
    
    #TODO Backgrounds
    image bg TRAFFIC = "images/bg/TRAFFIC.jpg" 
    image bg LIVING_ROOM = "images/bg/LIVING_ROOM.jpg" 
    image bg BEDROOM = "images/bg/BEDROOM.jpg" 
    image bg CLASSROOM = "images/bg/CLASSROOM.jpg" 
    image bg LIBRARY = "images/bg/LIBRARY.jpg" 
    image bg CAFETERIA = "images/bg/CAFETERIA.jpg" 
    
    
    #TODO CG images
    image BEE_X_VIDA_KISS_CG = "images/cg/BEE_X_VIDA_KISS_CG.png" 
    image SORA_X_UMI_ANIME_FAN_SERVICE_CG = "images/cg/SORA_X_UMI_ANIME_FAN_SERVICE_CG.png" 
    image SORA_X_UMI_DOODLE_MINI_CG = "images/cg/SORA_X_UMI_DOODLE_MINI_CG.png" 
    image VIDA_DOODLE_MINI_CG = "images/cg/VIDA_DOODLE_MINI_CG.png" 
    
    image ENDING_1 = "images/cg/Ending Cards/ENDING_1.jpg" 
    image ENDING_2 = "images/cg/Ending Cards/ENDING_2.jpg" 
    image ENDING_3 = "images/cg/Ending Cards/ENDING_3.jpg" 
    image ENDING_4 = "images/cg/Ending Cards/ENDING_4.jpg" 
    image ENDING_5 = "images/cg/Ending Cards/ENDING_5.jpg" 
    image ENDING_6 = "images/cg/Ending Cards/ENDING_6.jpg" 
    image ENDING_7 = "images/cg/Ending Cards/ENDING_7.jpg" 
    image ENDING_8 = "images/cg/Ending Cards/ENDING_8.jpg" 
    image ENDING_9 = "images/cg/Ending Cards/ENDING_9.jpg" 
    
    #TODO Characters
    
    image ATE IRRITATED = im.FactorScale("images/sprites/ATE IRRITATED.png", .35)
    image ATE POKERFACED = im.FactorScale("images/sprites/ATE POKERFACED.png", .35)
    image ATE SHOCKED = im.FactorScale("images/sprites/ATE SHOCKED.png", .35)
    image ATE SMILING = im.FactorScale("images/sprites/ATE SMILING.png"  , .35)
    
    image KARIS LAUGHING = im.FactorScale("images/sprites/KARIS LAUGHING.png", .35)
    image KARIS POKERFACED = im.FactorScale("images/sprites/KARIS POKERFACED.png", .35)
    image KARIS SMILING = im.FactorScale("images/sprites/KARIS SMILING.png"  , .35)
    
    image MOM = im.FactorScale("images/sprites/MOM.png", .35)
    
    image TEACHER = im.FactorScale("images/sprites/TEACHER.png", .35)
    
    image UMI BLUSHINGSMILE = im.FactorScale("images/sprites/UMI BLUSHINGSMILE.png", .35)
    image UMI POKERFACED = im.FactorScale("images/sprites/UMI POKERFACED.png", .35)
    image UMI SMILING = im.FactorScale("images/sprites/UMI SMILING.png", .35)
    
    image VIDA BLUSHINGSMILE = im.FactorScale("images/sprites/VIDA BLUSHINGSMILE.png", .35)
    image VIDA IRRITATED = im.FactorScale("images/sprites/VIDA IRRITATED.png", .35)
    image VIDA POKERFACED = im.FactorScale("images/sprites/VIDA POKERFACED.png", .35)
    image VIDA SMILING = im.FactorScale("images/sprites/VIDA SMILING.png", .35)

    