init:
    ###### POSITION DEFINES ############
    transform left:
      yalign 1.0 xanchor .5 xalign 0.25
      
    #transform right:
    #  yalign 1.0 xanchor .5 xalign 0.75
    
    ######### MISC DEFINES #############
    define slow_dissolve = Dissolve(2.0)
    
    define yael_romance = 0
    define freya_romance = 0
    define makeup_skill = 0
    define papa_trust = 0
    define clues_collected = 0
    define sheet_music = False
    define music_box = False
    define invisible_barrier = False
    define death_cause = False
    define photo_album = False
    define papa_violin = False
    define miniature_rose = False
    define lolo_cane = False
    define stopped_music = False
    define yael_abandoned = False
    define weapon_cane = False
    define weapon_hammer = False
    define path_one = False
    define path_three = False
    define ghostname = "Ghost"
    define ending_theme = "worst"
                        
    # Declare characters used by this game. The color argument colorizes the
    # name of the character.

    ######### CHARACTER DEFINES #############
    define Sari = Character("Sari", image="sari")
    define Papa = Character("Papa")
    define Yael = Character("Yael")
    define Freya = Character("Freya", window_background="gui/textbox_ghost.png")
    define Ghost = DynamicCharacter("ghostname", window_background="gui/textbox_ghost.png")
    define Unknown = Character("Unknown", window_background="gui/textbox_ghost.png")
    
  
    ######### SOUND DEFINES #############
    $aria = "audio/music/aria.mp3"
    $aria_guitar = "audio/music/aria_guitar.mp3"
    $aria_guitar_reverse = "audio/music/aria_guitar_reverse.mp3"
    $bgm = "audio/music/bgm.mp3"
    $ending = "audio/music/ending.mp3"
    $ending_bad = "audio/music/ending_bad.mp3"
    $ending_best = "audio/music/ending_best.mp3"
    $ending_good = "audio/music/ending_good.mp3"
    $ending_worst = "audio/music/ending_worst.mp3"
    $mellow = "audio/music/mellow.mp3"
    $menumusic = "audio/music/menu.mp3"
    $paghahandog = "audio/music/paghahandog.mp3"
    $suspense = "audio/music/suspense.mp3"
    
    ######### CG/BG IMAGE DEFINES #############
    image black = Solid("#000000")  
    image bg black = Solid("#000000")     
    image bg white = Solid("#ffffff")
    
    #TODO REPLACE #Backgrounds
    image NVLMODE = Solid("#000000")  
    image bg darkness = "images/bg/darkness.jpg"
    image bg foyer = "images/bg/foyer.png"
    image bg foyer_open = "images/bg/foyer_open.png"
    image bg morgue = "images/bg/morgue.png"
    image bg morgue_corpse = "images/bg/morgue_corpse.png"
    image bg morgue_open = "images/bg/morgue_open.png"
    image bg office = "images/bg/office.png"
    image bg viewing = "images/bg/viewing.png"
    image bg viewing_open = "images/bg/viewing_open.png"
    
    #TODO REPLACE #CG images
    image cg ending01 = "images/cg/ending01.jpg"
    image cg ending01_pic = "images/cg/ending01_pic.png"
    image cg ending02 = "images/cg/ending02.jpg"
    image cg ending02_pic = "images/cg/ending02_pic.png"
    image cg ending03 = "images/cg/ending03.jpg"
    image cg ending04 = "images/cg/ending04.jpg"
    image cg ending05 = "images/cg/ending05.jpg"
    image cg ending05_pic = "images/cg/ending05_pic.png"
    image cg ending06 = "images/cg/ending06.jpg"
    image cg ending07 = "images/cg/ending07.jpg"
    image cg ending08 = "images/cg/ending08.jpg"
    image cg ending09 = "images/cg/ending09.jpg"
    image cg ending09_pic = "images/cg/ending09_pic.png"
    image cg ending10 = "images/cg/ending10.jpg"
    image cg ending11 = "images/cg/ending11.jpg"
    image cg ending12 = "images/cg/ending12.jpg"
    image cg makeup_pic = "images/cg/makeup_pic.png"
    
    #image sari = "images/sprites/Sari/empty.png"
    image side sari default = im.FactorScale(im.Crop("images/sprites/Sari/sari_default.png", 500, 0, 1500, 1900), 0.3)
    image side sari anxious = im.FactorScale(im.Crop("images/sprites/Sari/sari_anxious.png", 500, 0, 1500, 1900), 0.3)
    image side sari blush = im.FactorScale(im.Crop("images/sprites/Sari/sari_blush.png", 500, 0, 1500, 1900), 0.3)
    image side sari laugh = im.FactorScale(im.Crop("images/sprites/Sari/sari_laugh.png", 500, 0, 1500, 1900), 0.3)
    image side sari mad = im.FactorScale(im.Crop("images/sprites/Sari/sari_mad.png", 500, 0, 1500, 1900), 0.3)
    image side sari sad = im.FactorScale(im.Crop("images/sprites/Sari/sari_sad.png", 500, 0, 1500, 1900), 0.3)
    image side sari shock = im.FactorScale(im.Crop("images/sprites/Sari/sari_shock.png", 500, 0, 1500, 1900), 0.3)
    image side sari smile = im.FactorScale(im.Crop("images/sprites/Sari/sari_smile.png", 500, 0, 1500, 1900), 0.3)
    
    #Invisible character images to go with side images
    #image sari = "images/sprites/Sari/empty.png"
    image sari default = "images/sprites/Sari/empty.png"
    image sari anxious = "images/sprites/Sari/empty.png"
    image sari blush = "images/sprites/Sari/empty.png"
    image sari laugh = "images/sprites/Sari/empty.png"
    image sari mad = "images/sprites/Sari/empty.png"
    image sari sad = "images/sprites/Sari/empty.png"
    image sari shock = "images/sprites/Sari/empty.png"
    image sari smile = "images/sprites/Sari/empty.png"
    
    #image papa = "images/sprites/Papa/empty.png"
    image papa default = im.FactorScale("images/sprites/Papa/papa_default.png", 0.4)
    image papa anxious = im.FactorScale("images/sprites/Papa/papa_anxious.png", 0.4)
    image papa cry = im.FactorScale("images/sprites/Papa/papa_cry.png", 0.4)
    image papa smile = im.FactorScale("images/sprites/Papa/papa_smile.png", 0.4)
    
    #image yael = "images/sprites/Yael/empty.png"
    image yael default = im.FactorScale("images/sprites/Yael/yael_default.png", 0.35)
    image yael anxious = im.FactorScale("images/sprites/Yael/yael_anxious.png", 0.35)
    image yael blush = im.FactorScale("images/sprites/Yael/yael_blush.png", 0.35)
    image yael cry = im.FactorScale("images/sprites/Yael/yael_cry.png", 0.35)
    image yael groovy = im.FactorScale("images/sprites/Yael/yael_groovy.png", 0.35)
    image yael laugh = im.FactorScale("images/sprites/Yael/yael_laugh.png", 0.35)
    image yael mad = im.FactorScale("images/sprites/Yael/yael_mad.png", 0.35)
    image yael sad = im.FactorScale("images/sprites/Yael/yael_sad.png", 0.35)
    image yael shock = im.FactorScale("images/sprites/Yael/yael_shock.png", 0.35)
    image yael smile = im.FactorScale("images/sprites/Yael/yael_smile.png", 0.35)
    
    #image ghost = "images/sprites/Ghost/empty.png"
    image ghost default = im.FactorScale("images/sprites/Ghost/ghost_default.png", 0.4)
    image ghost anxious = im.FactorScale("images/sprites/Ghost/ghost_anxious.png", 0.4)
    image ghost shock = im.FactorScale("images/sprites/Ghost/ghost_shock.png", 0.4)
    image ghost smile = im.FactorScale("images/sprites/Ghost/ghost_smile.png", 0.4)
    
    #image freya = "images/sprites/Freya/empty.png"
    image freya default = im.FactorScale("images/sprites/Freya/freya_default.png", 0.35)
    image freya anxious = im.FactorScale("images/sprites/Freya/freya_anxious.png", 0.35)
    image freya blush = im.FactorScale("images/sprites/Freya/freya_blush.png", 0.35)
    image freya laugh = im.FactorScale("images/sprites/Freya/freya_laugh.png", 0.35)
    image freya mad = im.FactorScale("images/sprites/Freya/freya_mad.png", 0.35)
    image freya sad = im.FactorScale("images/sprites/Freya/freya_sad.png", 0.35)
    image freya shock = im.FactorScale("images/sprites/Freya/freya_shock.png", 0.35)
    image freya smile = im.FactorScale("images/sprites/Freya/freya_smile.png", 0.35)
    