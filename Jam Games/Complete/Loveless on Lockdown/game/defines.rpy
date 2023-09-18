init:
    
    ######### MISC DEFINES #############
    define slow_dissolve = Dissolve(2.0)
    
    default jian_romance = 0
    default grace_romance = 0
    default jian_route = False
    default grace_route = False
                        
    # Declare characters used by this game. The color argument colorizes the
    # name of the character.

    ######### CHARACTER DEFINES #############
    define Kuya = Character("Kuya")
    define Ma = Character("Ma")
    define Mara = Character("Mara", image="mara")
    define narrator = Character(None, image="mara")
    define Woman = Character("Woman")
    define Stranger = Character("Stranger")
    define Gray = Character("Gray")
    define Grace = Character("Grace")
    define Jian = Character("Jian")
    
    define Marginalia = Character("Marginalia", image="mara", kind = nvl,  what_xalign=1.0, who_xalign=1.0)
    define wallflower95 = Character("wallflower95", image="mara", kind = nvl,  what_xalign=0.0, who_xalign=0.0)
    define ChainCustard404 = Character("ChainCustard404", image="mara", kind = nvl,  what_xalign=0.0, who_xalign=0.0)
    define nvlnarrator = Character(None, image="mara", kind = nvl,  what_xalign=0.5)
    
  
    ######### SOUND DEFINES #############
    $online = "audio/music/online.ogg"
    $online_subdued = "audio/music/online_subdued.ogg"
    $offline = "audio/music/offline.ogg"
    $offline_subdued = "audio/music/offline_subdued.ogg"
    $chaotic = "audio/music/chaotic.ogg"
    $romantic = "audio/music/romantic.ogg"
    
    ######### CG/BG IMAGE DEFINES #############
    image black = Solid("#000000")  
    image bg black = Solid("#000000")     
    image bg white = Solid("#ffffff")
    #image bg whitescreen = Solid("#b7b5b6")
    
    #TODO REPLACE #Backgrounds
    image NVLMODE = Solid("#000000")  
    image bg bedroom_curtain = "images/bg/bedroom_curtain.jpg"
    image bg bedroom_entrance = "images/bg/bedroom_entrance.jpg"
    image bg bedroom_sunset = "images/bg/bedroom_sunset.jpg"
    image bg bedroom_day = "images/bg/bedroom_day.jpg"
    image bg bedroom_night = "images/bg/bedroom_night.jpg"
    image bg elevator = "images/bg/elevator.jpg"
    image bg grocery_night = "images/bg/grocery_night.jpg"
    image bg urban_day = "images/bg/urban_day.jpg"
    image bg urban_sunset = "images/bg/urban_sunset.jpg"
    image bg urban2_sunset = "images/bg/urban2_sunset.jpg"
    image bg park_sunset = "images/bg/park_sunset.jpg"
    image bg apartment_night = "images/bg/apartment_night.jpg"
    image bg apartment_sunset = "images/bg/apartment_sunset.jpg"
    image bg street_sunset = "images/bg/street_sunset.jpg"
    image bg hallway = "images/bg/hallway.jpg"
    image bg darkness = "images/bg/darkness.jpg"
    
    #TODO REPLACE #CG images
    image cg laptop = "images/cg/laptop.png"
    image cg laptop_video = "images/cg/laptop_video.png"
    image cg laptop_game = "images/cg/laptop_game.png"
    image cg ending1 = "images/cg/ending1.jpg"
    image cg ending2 = "images/cg/ending2.jpg"
    image cg ending3 = "images/cg/ending3.jpg"
    image cg ending3_pic = "images/cg/ending3_pic.png"
    image cg ending4 = "images/cg/ending4.jpg"
    image cg ending5 = "images/cg/ending5.jpg"
    image cg ending5_pic = "images/cg/ending5_pic.png"
    image cg apartment_sunset2 = "images/bg/apartment_sunset.jpg"

    image side mara angry = im.FactorScale(im.Crop("images/sprites/Mara/mara_angry.png", 300, 0, 1330, 1850), 0.3)
    image side mara masked_angry = im.FactorScale(im.Crop("images/sprites/Mara/mara_masked_angry.png", 300, 0, 1330, 1850), 0.3)
    image side mara blush = im.FactorScale(im.Crop("images/sprites/Mara/mara_blush.png", 300, 0, 1330, 1850), 0.3)
    image side mara masked_blush = im.FactorScale(im.Crop("images/sprites/Mara/mara_masked_blush.png", 300, 0, 1330, 1850), 0.3)  
    image side mara poker = im.FactorScale(im.Crop("images/sprites/Mara/mara_poker.png", 300, 0, 1330, 1850), 0.3)
    image side mara masked_poker = im.FactorScale(im.Crop("images/sprites/Mara/mara_masked_poker.png", 300, 0, 1330, 1850), 0.3)
    image side mara shock = im.FactorScale(im.Crop("images/sprites/Mara/mara_shock.png", 300, 0, 1330, 1850), 0.3)
    image side mara masked_shock = im.FactorScale(im.Crop("images/sprites/Mara/mara_masked_shock.png", 300, 0, 1330, 1850), 0.3)
    image side mara sad = im.FactorScale(im.Crop("images/sprites/Mara/mara_sad.png", 300, 0, 1330, 1850), 0.3)
    image side mara smile = im.FactorScale(im.Crop("images/sprites/Mara/mara_smile.png", 300, 0, 1330, 1850), 0.3)
    
    #Invisible mara sprite to go with side images
    image mara = "images/sprites/Mara/empty.png"
    image mara angry = "images/sprites/Mara/empty.png"
    image mara masked_angry = "images/sprites/Mara/empty.png"
    image mara blush = "images/sprites/Mara/empty.png"
    image mara masked_blush = "images/sprites/Mara/empty.png"   
    image mara poker = "images/sprites/Mara/empty.png"  
    image mara masked_poker = "images/sprites/Mara/empty.png"  
    image mara shock = "images/sprites/Mara/empty.png"   
    image mara masked_shock = "images/sprites/Mara/empty.png"  
    image mara sad = "images/sprites/Mara/empty.png"     
    image mara smile = "images/sprites/Mara/empty.png" 
    
    image grace blush = im.FactorScale(im.Crop("images/sprites/Grace/grace_blush.png", 0, 0, 1630, 1850), 0.55)
    image grace masked_blush = im.FactorScale(im.Crop("images/sprites/Grace/grace_masked_blush.png", 0, 0, 1630, 1850), 0.55)
    image grace masked_blush_apron = im.FactorScale(im.Crop("images/sprites/Grace/grace_masked_blush_apron.png", 0, 0, 1630, 1850), 0.55)     
    image grace poker = im.FactorScale(im.Crop("images/sprites/Grace/grace_poker.png", 0, 0, 1630, 1850), 0.55)  
    image grace masked_poker = im.FactorScale(im.Crop("images/sprites/Grace/grace_masked_poker.png", 0, 0, 1630, 1850), 0.55)
    image grace masked_poker_apron = im.FactorScale(im.Crop("images/sprites/Grace/grace_masked_poker_apron.png", 0, 0, 1630, 1850), 0.55)   
    image grace masked_shock = im.FactorScale(im.Crop("images/sprites/Grace/grace_masked_shock.png", 0, 0, 1630, 1850), 0.55)
    image grace masked_shock_apron = im.FactorScale(im.Crop("images/sprites/Grace/grace_masked_shock_apron.png", 0, 0, 1630, 1850), 0.55)   
    
    image jian blush = im.FactorScale(im.Crop("images/sprites/Jian/jian_blush.png", 0, 0, 1630, 1850), 0.55)
    image jian masked_blush = im.FactorScale(im.Crop("images/sprites/Jian/jian_masked_blush.png", 0, 0, 1630, 1850), 0.55)   
    image jian poker = im.FactorScale(im.Crop("images/sprites/Jian/jian_poker.png", 0, 0, 1630, 1850), 0.55)  
    image jian masked_poker = im.FactorScale(im.Crop("images/sprites/Jian/jian_masked_poker.png", 0, 0, 1630, 1850), 0.55)  
    image jian masked_shock = im.FactorScale(im.Crop("images/sprites/Jian/jian_masked_shock.png", 0, 0, 1630, 1850), 0.55) 
    image jian shock = im.FactorScale(im.Crop("images/sprites/Jian/jian_shock.png", 0, 0, 1630, 1850), 0.55) 
    image jian smile = im.FactorScale(im.Crop("images/sprites/Jian/jian_smile.png", 0, 0, 1630, 1850), 0.55) 