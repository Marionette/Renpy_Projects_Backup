
#init python:
#    config.empty_window = renpy.curry(extend)("", interact=False)
#    _last_say_what = ""
    
#init python:
  #define.move_transitions("dissolve", 0.5, layer="master")
  #define.move_transitions("fade", 1.0, layer="master")
    #redefine dissolve to renpy.transition(dissolve, layer="master")

init -2:
    ######### ATL DEFINES #############
    transform Delay:
        pause(0.5)
        
    #transform DelayedRunBounce:
    #    pause(0.5)
    #    yalign 1.0
    #    linear 0.40 yalign 1.1
    #    linear 0.40 yalign 1.0
    #    repeat
        
    transform RunBounce:
        yalign 1.0
        linear 0.40 yalign 1.1
        linear 0.40 yalign 1.0
        repeat
            
    transform RunBounceBig:
        #Full screen size sprites dont work with yalign
        xpos -300
        ypos 1080
        linear 0.40 ypos 1180
        linear 0.40 ypos 1080
        repeat
        
    transform walkBounce:
        #yalign 1.0
        linear 0.80 yalign 1.1
        linear 0.80 yalign 1.0
        repeat
        
    transform WalkBounce:
        #yalign 1.0
        linear 0.80 yalign 1.1
        linear 0.80 yalign 1.0
        repeat
        
    transform highHover:
        #yalign 1.0
        linear 0.80 yalign 2.1
        linear 0.80 yalign 2.0
        repeat
        
    transform hover:
        #yalign 1.0
        linear 0.80 yalign 1.1
        linear 0.80 yalign 1.0
        repeat
        
    transform FallDown2:
        yalign 1.0
        rotate 0
        linear 0.7 yalign -150.0 rotate 60.0
            
    transform FallDown:
        yalign 1.0
        rotate 0
        linear 0.7 yalign -11.3 rotate 45.0
        
    transform FallDown3:
        yalign 1.0
        linear 0.5 yalign 10.0
        
    transform StandUp:
        yalign 2.5
        linear 0.5 yalign 1.0
        
    transform SitUp:
        yalign 6.5
        linear 0.5 yalign 2.5
        
    transform SittingJump:
        yalign 2.5
        linear 0.1 yalign 2.2
        linear 0.1 yalign 2.5
        
    transform leftright:
        xpos -200
        linear 50.0 xpos 1920
        
    transform LeftRight:
        xpos -200
        linear 50.0 xpos 1920
        
    transform bottomtop:
        ypos 600
        linear 0.5 ypos 350
        
    transform leafspin: 
        xpos -100 
        yalign -1.0
        rotate 0
        linear 4.0 xpos renpy.random.randint(2800, 2920) rotate 180 yalign 1.0
        repeat
        
    transform leafspin2:
        xpos -500
        yalign -2.0
        rotate 0
        linear 6.0 xpos renpy.random.randint(2800, 3920) rotate 180 yalign 2.0
        repeat
        
    transform leafspin3:
        xpos -400
        yalign -1.5
        rotate 0
        linear 12.0 xpos renpy.random.randint(2800, 2920) rotate 360 yalign 4.0
        repeat
        
    transform leafspin4:
        xpos 200
        yalign -1.0
        rotate 0
        linear 10.0 xpos renpy.random.randint(2800, 4920) rotate 360 yalign 3.0
        repeat
        
    transform ScrollDown:
        yalign -0.0
        linear 5.00 yalign 1.0
        
    transform ScrollUpFromBottom:
        yalign -0.0
        linear 5.00 yalign 1.0
    
    transform ScrollUp:
        yalign 1.0
        linear 5.00 yalign -0.0
    
    transform Crouch:
        yalign 1.0
        linear 0.50 yalign 1.3
        
    transform QuickCrouch:
        yalign 1.0
        linear 0.50 yalign 2.5
        linear 0.50 yalign 1.0
    
    transform ShoulderTap:
        yalign 1.0
        xalign 0.10
        linear 1.50 xalign 0.30
        linear 1.0 xalign 0.20
    
    transform ShoulderTap2:
        yalign 1.0
        xalign 0.50
        linear 1.50 xalign 0.45
        linear 1.0 xalign 0.50
        
    transform ShoulderTap3:
        yalign 1.0
        xalign 0.70
        linear 1.0 xalign 0.60
        linear 1.0 xalign 0.70
        
    transform RightBump:
        yalign 1.0
        xalign 0.70
        linear 0.5 xalign 0.80
        linear 0.5 xalign 0.70
        
    transform FarRightBump:
        yalign 1.0
        xalign 0.75
        linear 0.5 xalign 0.85
        linear 0.5 xalign 0.75
        
    transform LeftBump:
        yalign 1.0
        xalign 0.0
        linear 0.5 xalign -0.10
        linear 0.5 xalign 0.0
        
    transform LeftBumpSmall:
        yalign 1.0
        xalign 0.0
        linear 0.3 xalign -0.05
        linear 0.3 xalign 0.0
        
    transform SlightLeftBump:
        yalign 1.0
        xalign 0.3
        linear 0.5 xalign 0.25
        linear 0.5 xalign 0.3
        
    transform RightToCenter:
        yalign 1.0
        xalign 0.90
        linear 1.0 xalign 0.50
        
    transform LeftToCenter:
        yalign 1.0
        xalign 0.0
        linear 1.0 xalign 0.50
        
    transform LeftToAlmostCenter:
        yalign 1.0
        xalign 0.0
        linear 1.0 xalign 0.40
    
    transform Blinking:
        alpha 0.3
        linear 1.00 alpha 0.8
        linear 1.00 alpha 0.3
        repeat
        
    transform ZoomIn:
        zoom 2.0
        linear 2.0 zoom 1.0
        
    transform ZoomOut:
        zoom 1.0
        linear 2.0 zoom 0.5
    #Transitions
    define slow_dissolve = Dissolve(1.0)
    define quick_dissolve = Dissolve(0.5)
    
    
init python hide:
    for file in renpy.list_files():
        if file.startswith('bg') and file.endswith('.jpg'):
            name = file.replace('BG/','').replace('/', ' ').replace('.jpg','')
            renpy.image(name, Image(file))
            
            
            
            
init:
    ######### VARIABLE DEFINES #############
    $ show_quick_menu = True
    
    $ style.say_dialogue.drop_shadow = (2, 2)
    $ style.say_dialogue.drop_shadow_color = "#000000"
    
    
    ######### CHARACTER DEFINES #############
    # Declare characters used by this game.
    define narrator = Character(None, show_two_window=True, window_background="img/gui/Textbox/Textbox.png", what_font="DejaVuSans.ttf")
    define centered = Character(None, what_font="DejaVuSans.ttf")
    define mk = Character('Merona', color="#ebc9c8", show_two_window=True, window_background="img/gui/Textbox/Textbox_Merona.png", what_font="DejaVuSans.ttf")
    define mi = Character('Merona', color="#ebc9c8", show_two_window=True, what_prefix="( ", what_suffix=" )", window_background="img/gui/Textbox/Textbox_Merona.png", what_font="DejaVuSans.ttf")
    define dt = Character('Duran', color="#d07552", show_two_window=True, window_background="img/gui/Textbox/Textbox_Duran.png", what_font="DejaVuSans.ttf")
    define ln = Character('Lexan', color="#939cab", show_two_window=True, window_background="img/gui/Textbox/Textbox_Lexan.png", what_font="DejaVuSans.ttf")
    define pm = Character('Prowen', color="#a8a7af", show_two_window=True, window_background="img/gui/Textbox/Textbox_Prowen.png", what_font="DejaVuSans.ttf")
    define ns = Character('Nony', color="#636363", show_two_window=True, window_background="img/gui/Textbox/Textbox_NonySoum.png", what_font="DejaVuSans.ttf")
    define rs = Character('Ranan', color="#749172", show_two_window=True, window_background="img/gui/Textbox/Textbox_Ranan.png", what_font="DejaVuSans.ttf")
    define ra = Character('Ranan', color="#749172", show_two_window=True, window_background="img/gui/Textbox/Textbox_Ranan.png", what_font="DejaVuSans.ttf")
    define ck = Character('Cimaria', color="#c1d8e2", show_two_window=True, window_background="img/gui/Textbox/Textbox_Cimaria.png", what_font="DejaVuSans.ttf")
    define rt = Character('Rett', color="#7d3737", show_two_window=True, window_background="img/gui/Textbox/Textbox_Rett.png", what_font="DejaVuSans.ttf")
    define kh = Character('Kreita', color="#5f466e", show_two_window=True, window_background="img/gui/Textbox/Textbox_Kreita.png", what_font="DejaVuSans.ttf")
    define bg = Character('Boyen', color="#dcada3", show_two_window=True, window_background="img/gui/Textbox/Textbox_Boyen.png", what_font="DejaVuSans.ttf")
    define hw = Character('Wriane', color="#64816f", show_two_window=True, window_background="img/gui/Textbox/Textbox_Wriane.png", what_font="DejaVuSans.ttf")
    define qv = Character('Voya IV', color="#783f52", show_two_window=True, window_background="img/gui/Textbox/Textbox_Voya.png", what_font="DejaVuSans.ttf")
    define kd = Character('Drae VI', color="#7b0f0c", show_two_window=True, window_background="img/gui/Textbox/Textbox_Drae.png", what_font="DejaVuSans.ttf")
    define dr = Character('Drae VI', color="#7b0f0c", show_two_window=True, window_background="img/gui/Textbox/Textbox_Drae.png", what_font="DejaVuSans.ttf")
    define mf = Character('Father', color="#693d30", show_two_window=True, window_background="img/gui/Textbox/Textbox_Father.png", what_font="DejaVuSans.ttf")
    define mm = Character('Mother', color="#957463", show_two_window=True, window_background="img/gui/Textbox/Textbox_Mother.png", what_font="DejaVuSans.ttf")
    define mo = Character('????', color="#ffffff", show_two_window=True, window_background="img/gui/Textbox/Textbox_Unknown.png", what_font="DejaVuSans.ttf")
    define qq = Character('????', color="#000000", show_two_window=True, window_background="img/gui/Textbox/Textbox_QuestionMark.png", what_font="DejaVuSans.ttf")
    
    
    
    ######### FANART DEFINES #############
    
    image fa1 = "img/fanart/FanartGallery_Merona/Images/akkeyroomi.png"
    image fa2 = "img/fanart/FanartGallery_Merona/Images/Animizuu.png"
    image fa3 = "img/fanart/FanartGallery_Merona/Images/Clovis-thecutestcat.png"
    image fa4 = "img/fanart/FanartGallery_Merona/Images/Danimi.png"
    image fa5 = "img/fanart/FanartGallery_Merona/Images/Iriho-chan.png"
    image fa6 = "img/fanart/FanartGallery_Merona/Images/llenviash.png"
    image fa7 = "img/fanart/FanartGallery_Merona/Images/MiLiica.png"
    image fa8 = "img/fanart/FanartGallery_Merona/Images/RuiCarmen.png"
    image fa9 = "img/fanart/FanartGallery_Merona/Images/Suika.png"
    image fa10 = "img/fanart/FanartGallery_Merona/Images/sweetsalad.png"
    image fa11 = "img/fanart/FanartGallery_Merona/Images/Tai-chan104.png"
    image fa12 = "img/fanart/FanartGallery_Merona/Images/tierEight.png"
    image fa13 = "img/fanart/FanartGallery_Merona/Images/Tomoyo Ichijouji.png"
    
    image fa1t = "img/fanart/FanartGallery_Merona/Thumbs/akkeyroomi.png"
    image fa2t = "img/fanart/FanartGallery_Merona/Thumbs/Animizuu.png"
    image fa3t = "img/fanart/FanartGallery_Merona/Thumbs/Clovis-thecutestcat.png"
    image fa4t = "img/fanart/FanartGallery_Merona/Thumbs/Danimi.png"
    image fa5t = "img/fanart/FanartGallery_Merona/Thumbs/Iriho-chan.png"
    image fa6t = "img/fanart/FanartGallery_Merona/Thumbs/llenviash.png"
    image fa7t = "img/fanart/FanartGallery_Merona/Thumbs/MiLiica.png"
    image fa8t = "img/fanart/FanartGallery_Merona/Thumbs/RuiCarmen.png"
    image fa9t = "img/fanart/FanartGallery_Merona/Thumbs/Suika.png"
    image fa10t = "img/fanart/FanartGallery_Merona/Thumbs/sweetsalad.png"
    image fa11t = "img/fanart/FanartGallery_Merona/Thumbs/Tai-chan104.png"
    image fa12t = "img/fanart/FanartGallery_Merona/Thumbs/tierEight.png"
    image fa13t = "img/fanart/FanartGallery_Merona/Thumbs/Tomoyo Ichijouji.png"

    
    
    ######### SOUND DEFINES #############
    
    $music_ambient = "audio/music/Ambient Sound.ogg"
    $music_newBegin = "audio/music/New Beginnings.ogg"
    $music_piano = "audio/music/Piano.ogg"
    $music_potHappy = "audio/music/Potent Happiness.ogg"
    $music_romance = "audio/music/Romance.ogg"
    $music_Romance = "audio/music/Romance.ogg"
    $music_SoTsh = "audio/music/Society of Trees (Short).ogg"
    $music_SoT = "audio/music/Society of Trees.ogg"
    $music_title = "audio/music/Title Theme.ogg"
    $music_uplifting = "audio/music/Uplifting.ogg"
    $music_movement = "audio/music/battle.ogg"
    $music_meronatheme = "audio/music/Merona's Theme.ogg"
    $music_eerie = "audio/music/Eerie.ogg"
    $music_recollections = "audio/music/Recollections.ogg"
    $music_life = "audio/music/Life.ogg"
    
    $music_Aces_High = "audio/music/Aces High.ogg"
    $music_Afterglow = "audio/music/Afterglow.ogg"
    $music_A_Moments_Reflection = "audio/music/A Moments Reflection.ogg"
    $music_A_thousand_Skins_Pt2 = "audio/music/A thousand Skins Pt2.ogg"
    $music_Black_Vortex = "audio/music/Black Vortex.ogg"
    $music_Cool_Steel_Breeze = "audio/music/Cool Steel Breeze.ogg"
    $music_Dark_Red_Wine = "audio/music/Dark Red Wine.ogg"
    $music_Delightful_D = "audio/music/Delightful D.ogg"
    $music_Ecstasy_X = "audio/music/Ecstasy X.ogg"
    $music_Epilogue = "audio/music/Epilogue.ogg"
    $music_Future_Gladiator = "audio/music/Future Gladiator.ogg"
    $music_Gallows_Hill = "audio/music/Gallows Hill.ogg"
    $music_Greek_Dance = "audio/music/Greek Dance.ogg"
    $music_Green_Leaves = "audio/music/Green Leaves.ogg"
    $music_Heart_of_Nowhere = "audio/music/Heart of Nowhere.ogg"
    $music_Heroic_Age = "audio/music/Heroic Age.ogg"
    $music_Ill_be_right_behind_you_Josephine = "audio/music/Ill be right behind you Josephine.ogg"
    $music_Incoherent = "audio/music/Incoherent.ogg"
    $music_Infinite_Horizon = "audio/music/Infinite Horizon.ogg"
    $music_Infinite_Perspective = "audio/music/Infinite Perspective.ogg"
    $music_Inner_Journey = "audio/music/Inner Journey.ogg"
    $music_I_want_to_destroy_something_beautiful = "audio/music/I want to destroy something beautiful.ogg"
    $music_Lafayette = "audio/music/Lafayette.ogg"
    $music_Last_Kiss_Good_Night = "audio/music/Last Kiss Good Night.ogg"
    $music_Main_Theme = "audio/music/Title Theme.ogg"
    $music_Nincompoop = "audio/music/Nincompoop.ogg"
    $music_Oh_Mallory = "audio/music/Oh Mallory.ogg"
    $music_Pilot_Error = "audio/music/Pilot Error.ogg"
    $music_Pompeii = "audio/music/Pompeii.ogg"
    $music_Pride = "audio/music/Pride.ogg"
    $music_Radio_Martini = "audio/music/Radio Martini.ogg"
    $music_Renaissance = "audio/music/Renaissance.ogg"
    $music_Revolution_Now = "audio/music/Revolution Now.ogg"
    $music_River_Meditation = "audio/music/River Meditation.ogg"
    $music_Roll_away_the_Stone = "audio/music/Roll away the Stone.ogg"
    $music_Sailors_Lament = "audio/music/Sailors Lament.ogg"
    $music_Shes_on_my_Mind = "audio/music/Shes on my Mind.ogg"
    $music_She_dreams_in_blue = "audio/music/She dreams in blue.ogg"
    $music_Soporific = "audio/music/Soporific.ogg"
    $music_Sovereign = "audio/music/Sovereign.ogg"
    $music_Sugar_On_My_Tongue = "audio/music/Sugar On My Tongue.ogg"
    $music_Summer_Day = "audio/music/Summer Day.ogg"
    $music_Swimming_To_Cambodia = "audio/music/Swimming To Cambodia.ogg"
    $music_Travel_Light = "audio/music/Travel Light.ogg"
    $music_Under_the_Stairs = "audio/music/Under the Stairs.ogg"
    $music_Up_Kilkenny = "audio/music/Up Kilkenny.ogg"
    $music_White = "audio/music/White.ogg"
    $music_Words = "audio/music/Words.ogg"
    $music_Words_Fall_Apart = "audio/music/Words Fall Apart.ogg"

    #TODO    
    
    $sound_birds = "audio/sound/djhalleu__stavanger-nightingale1.ogg"
    $sound_cukoo = "audio/sound/inchadney__cuckoo_short.ogg"
    $sound_bell = "audio/sound/kaonaya__bell-at-daitokuji-temple-kyoto.ogg"
    $sound_snarl = "audio/sound/Monster Snarling.ogg"
    $sound_ambiance = "audio/sound/Nature Ambiance.ogg"
    $sound_cricket = "audio/sound/weldonsmith__cricket2dopecho.ogg"
    $sound_footsteps = "audio/sound/footsteps.ogg"
    $sound_knock = "audio/sound/knock.ogg"
    $sound_breatheOut = "audio/sound/breatheOut.ogg"
    $sound_fallInDirt = "audio/sound/fallInDirt.ogg"
    $sound_lionRoar = "audio/sound/lionRoar.ogg"
    $sound_lionRoar2 = "audio/sound/lionRoar2.ogg"
    
    $sound_bump = "audio/sound/Bump.ogg"
    $sound_nighttimeAmbience = "audio/sound/night time ambience.ogg"
    $sound_punch = "audio/sound/Punch.ogg"
    $sound_rustling = "audio/sound/rustling.ogg"
    $sound_water = "audio/sound/Water.ogg"
    $sound_clap = "audio/sound/clap.ogg"
    
    $sound_airAttack = "audio/sound/airAttack.ogg"
    $sound_arrow = "audio/sound/arrow.ogg"
    $sound_crash = "audio/sound/crash.ogg"
    $sound_fallInDirt_short = "audio/sound/fallInDirt_short.ogg"
    $sound_fireAttack = "audio/sound/fireAttack.ogg"
    $sound_fluttering = "audio/sound/fluttering.ogg"
    $sound_harshFootsteps = "audio/sound/harshFootsteps.ogg"
    $sound_rain = "audio/sound/rain.ogg"
    $sound_rainAttack = "<from 4 to 5>audio/sound/rain.ogg"
    $sound_swordAttack = "audio/sound/swordAttack.ogg"
    $sound_swordDraw = "audio/sound/swordDraw.ogg"
    $sound_thunder = "audio/sound/thunder.ogg"
    $sound_whistle = "audio/sound/whistle.ogg"
    $sound_wind = "audio/sound/wind.ogg"
    $sound_grassFootsteps = "audio/sound/footsteps.ogg"
    $sound_fire = "audio/sound/fire.ogg" 
    $sound_yawn = "audio/sound/yawn.ogg" 
    $sound_pat = "audio/sound/pat.ogg" 
    $sound_coughing = "audio/sound/coughing.ogg" 
    $sound_ocean = "audio/sound/ocean.ogg"
    
    #TODO
    $sound_rettCallingKreitaQuietly = "audio/sound/footsteps.ogg" 
    
    ######### CG/BG IMAGE DEFINES #############
    
    
    # Animation movies
    image sunrays movie = Movie(channel="sunrays", play="img/animations/sunrays_real.webm", mask="img/animations/sunrays_mask.webm")    
    image airAttack movie = Movie(channel="airAttack", play="img/animations/airAttack_real.webm", mask="img/animations/airAttack_mask.webm", yalign=0.5, xalign=0.5)
    image fireAttack movie = Movie(channel="fireAttack", play="img/animations/fireAttack_real.webm", mask="img/animations/fireAttack_mask.webm", yalign=0.5, xalign=0.5)
    image fireAttackBig movie = Movie(channel="fireAttackBig", play="img/animations/fireAttackBig_real.webm", mask="img/animations/fireAttackBig_mask.webm")
    image swordAttack movie = Movie(channel="swordAttack", play="img/animations/swordAttack_real.webm", mask="img/animations/swordAttack_mask.webm", yalign=0.5, xalign=0.5)
    image rain movie = Movie(channel="rain", play="img/animations/rain_real.webm", mask="img/animations/rain_mask.webm")
    image lightRain movie = Movie(channel="lightRain", play="img/animations/lightRain_real.webm", mask="img/animations/lightRain_mask.webm")
    image steam movie = Movie(channel="steam", play="img/animations/steam_real.webm", mask="img/animations/steam_mask.webm", yalign=0.5, xalign=0.5)
    image magicEnergy movie = Movie(channel="magicEnergy", play="img/animations/magicEnergy_real.webm", mask="img/animations/magicEnergy_mask.webm") 
    #image movie = Movie(size=(1280, 720), xalign=0.5, yalign=0.5)
    #image samovie = Movie(size=(1280, 720),mask="img/animations/swordAttack_mask.webm", xalign=0.5, yalign=0.5)
    
    #Misc Screen images
    image logo = "img/cg/Intro/introLogo.png"
    image startupCredits = "img/gui/Startup Credits.png"  
    
    #cgs / bgs
    image cg intro1 = "img/cg/Intro/intro1.png"
    image cg intro2 = "img/cg/Intro/intro2.png"
    image cg intro3 = "img/cg/Intro/intro3.png"
    image cg intro4 = "img/cg/Intro/intro4.png"  
    image cg handOnBranch1 = "img/cg/handOnBranch/handOnBranch1.png" 
    image cg handOnBranch2 = "img/cg/handOnBranch/handOnBranch2.png" 
    image cg handOnBranch3 = "img/cg/handOnBranch/handOnBranch3.png" 
    image cg monsterRoar = "img/cg/MonsterRoar/MonsterRoar.png"
    image cg M_onGround1 = "img/cg/MOnGround/MOnGround1.png"     
    image cg M_onGround2 = "img/cg/MOnGround/MOnGround2.png"     
    image cg M_onGround3 = "img/cg/MOnGround/MOnGround3.png"     
    image cg M_onGround4 = "img/cg/MOnGround/MOnGround4.png"     
    image cg M_onGround5 = "img/cg/MOnGround/MOnGround5.png"     
    image cg M_zoomShadow1 = "img/cg/M_zoomShadow/M_zoomShadow1.png"  
    image cg M_zoomShadow2 = "img/cg/M_zoomShadow/M_zoomShadow2.png"  
    image cg M_zoomShadow3 = "img/cg/M_zoomShadow/M_zoomShadow3.png"
    image cg rabbit = "img/cg/rabbit/rabbit.png"
    
    #image bg = "img/bg/Laneo_TownSquare.png" # For testing only
    #image bg = Solid("#000000")    
    image black = Solid("#000000")  
    image bg black = Solid("#000000")     
    image bg white = Solid("#ffffff")    
    image cg forest1 = "img/cg/Intro/forest1.png"
    image cg forest1_5 = "img/cg/Intro/forest1_5.png"
    image cg forest2 = "img/cg/Intro/forest2.png"
    image cg forest3 = "img/cg/Intro/forest3.png"
    image cg forest4 = "img/cg/Intro/forest4.png"
    image cg forest5 = "img/cg/Intro/forest5.png"
    image cg forest6 = "img/cg/forest6.png"
    image cg forest7 = "img/cg/forest7.png"
    image cg forest8 = "img/cg/forest8.png"
    image cg forest9 = "img/cg/forest9.png"
    image cg forest10 = "img/cg/forest10.png"
    image cg forest11 = "img/cg/forest11.png"
    image cg forest12 = "img/cg/forest12.png"
    image cg forest13 = "img/cg/forest13.png"
    image cg forest14 = "img/cg/forest14.png"
    image cg_sky1 = "img/cg/Intro/sky1.png"
    image cg_sky2 = "img/cg/sky2/sky2.png"
    image cg_sky3 = "img/cg/sky3.png"
    
    image academy = "img/bg/academy.png"
    
    image cg talkwithtree1 = "img/cg/talkWithTree/talkWithTree1.png"
    image cg talkwithtree2 = "img/cg/talkWithTree/talkWithTree2.png"
    image cg talkwithtree3 = "img/cg/talkWithTree/talkWithTree3.png"
    image cg talkwithtree4 = "img/cg/talkWithTree/talkWithTree4.png"
    image cg talkwithtree5 = "img/cg/talkWithTree/talkWithTree5.png"
    image cg talkwithtree6 = "img/cg/talkWithTree/talkWithTree6.png"
    
    image cg C_leaving1 = "img/cg/C_leaving/C_leaving1.png"
    image cg C_leaving2 = "img/cg/C_leaving/C_leaving2.png"
    image cg C_leaving3 = "img/cg/C_leaving/C_leaving3.png"
    image cg C_leaving4 = "img/cg/C_leaving/C_leaving4.png"
    image cg sunsetScape1 = "img/cg/SunsetScape_1/SunsetScape_1.png"
    image cg sunsetScape2 = "img/cg/SunsetScape2-10/SunsetScape2(2).png"
    image cg sunsetScape2 = "img/cg/SunsetScape2-10/SunsetScape2.png"
    image cg sunsetScape2_cimaria1 = "img/cg/SunsetScape2-10/SunsetScape2_cimaria1.png"
    image cg sunsetScape2_cimaria2 = "img/cg/SunsetScape2-10/SunsetScape2_cimaria2.png"
    image cg sunsetScape2_cimaria_lexan = "img/cg/SunsetScape2-10/SunsetScape2_cimaria_lexan.png"
    image cg sunsetScape3 = "img/cg/SunsetScape2-10/SunsetScape3.png"
    image cg sunsetScape4 = "img/cg/SunsetScape2-10/SunsetScape4.png"
    image cg sunsetScape5 = "img/cg/SunsetScape2-10/SunsetScape5.png"
    image cg sunsetScape6 = "img/cg/SunsetScape2-10/SunsetScape6.png"
    image cg sunsetScape7 = "img/cg/SunsetScape2-10/SunsetScape7.png"
    image cg sunsetScape8 = "img/cg/SunsetScape2-10/SunsetScape8.png"
    image cg sunsetScape9 = "img/cg/SunsetScape2-10/SunsetScape9.png"
    image cg sunsetScape10 = "img/cg/SunsetScape2-10/SunsetScape10.png"

    image cg forest1_evening = "img/cg/forest1_evening.png"
    image cg honey = "img/cg/honey.png"
    image cg stairs    = "img/cg/stairs.png"
    image cg glowingPotCG = "img/cg/glowingPotCG.png"
    image cg hangingPlant = "img/cg/hangingPlant.png"
    image cg hangingPlant2 = "img/cg/hangingPlant2.png"
    
    image cg candles    = "img/cg/Candles/Candles.png"
    image cg candles blur    = "img/cg/Candles/CandlesWBlur.png"
    
    image cg bushRustle    = "img/cg/bushRustle.png"
    
    image cg climb    = "img/cg/climb/climb.png"
    image cg climb2    = "img/cg/climb/climb2.png"
    image bg corridor    = "img/cg/corridor.png"
    image bg corridor2    = "img/cg/corridor2.png"
    
    image cg danger    = "img/cg/danger.png"
    image cg dormOutside    = "img/cg/dormOutside.png"
    
    image cg examination     = "img/cg/examination/examination.png"
    image cg examination1    = "img/cg/examination/examination.png"
    image cg examination2    = "img/cg/examination/examination2.png"
    image cg examination3    = "img/cg/examination/examination3.png"
    image cg examination3b   = "img/cg/examination/examination3b.png"
    image cg examination4    = "img/cg/examination/examination4.png"
    image cg examination4b   = "img/cg/examination/examination4b.png"
    image cg examination5    = "img/cg/examination/examination5.png"
    image cg examination6    = "img/cg/examination/examination6.png"
    image cg examination7    = "img/cg/examination/examination7.png"
    image cg examination8    = "img/cg/examination/examination8.png"
    image cg examination9    = "img/cg/examination/examination9.png"
    
    image cg forest15 = "img/cg/forest15.png"
    image cg forest16 = "img/cg/forest16.png"
    image cg forest17 = "img/cg/forest17.png"
    image cg forest18 = "img/cg/forest18.png"
    image cg forest19 = "img/cg/forest19.png"
    image cg forest20 = "img/cg/forest20.png"
    image cg forest21 = "img/cg/forest21.png"
    image cg forest22 = "img/cg/forest22.png"
    image cg forest23 = "img/cg/forest23.png"
    image cg forest24 = "img/cg/forest24.png"
    image cg forest25 = "img/cg/forest25.png"
    
    image cg forest6 = "img/cg/forest6.png"
    image cg forest7 = "img/cg/forest7.png"
    image cg forest8 = "img/cg/forest8.png"
    image cg forest9 = "img/cg/forest9.png"
    image cg forest10 = "img/cg/forest10.png"
    image cg forest11 = "img/cg/forest11.png"
    image cg forest12 = "img/cg/forest12.png"
    image cg forest13 = "img/cg/forest13.png"
    image cg forest14 = "img/cg/forest14.png"
    image cg forest15 = "img/cg/forest15.png"
    image cg forest16 = "img/cg/forest16.png"
    image cg forest16b = "img/cg/forest16b.png"
    image cg forest17 = "img/cg/forest17.png"
    image cg forest18 = "img/cg/forest18.png"
    image cg forest19 = "img/cg/forest19.png"
    image cg forest20 = "img/cg/forest20.png"
    image cg forest21 = "img/cg/forest21.png"
    image cg forest22 = "img/cg/forest22.png"
    image cg forest23 = "img/cg/forest23.png"
    image cg forest24 = "img/cg/forest24.png"
    image cg forest25 = "img/cg/forest25.png"
    
    image cg forestGround    = "img/cg/forestGround.png"
    image cg forestGroundNight    = "img/cg/forestGroundNight.png"
    image cg forestHouse    = "img/cg/forestHouse.png"
    image cg forestHouse inside = "img/bg/forestHouse_inside.png"
    image cg forestHouse inside2 = "img/bg/forestHouse_inside2.png"
    
    image cg forestTop = "img/bg/forestTop.png"
    
    image cg ground    = "img/cg/ground/ground.png"
    image cg ground2    = "img/cg/ground/ground2.png"
    image cg ground3    = "img/cg/ground/ground3.png"
    
    image cg handInSoil    = "img/cg/handInSoil/handInSoil.png"
    image cg handInSoil2    = "img/cg/handInSoil/handInSoil2.png"
    
    image cg hillSide    = "img/cg/hillside.png"
    image cg hillSide2    = "img/cg/hillside2.png"
    
    image bg laneoOutskirts    = "img/cg/laneoOutskirts.png"
    image bg laneoStreet    = "img/cg/laneoStreet.png"
    
    image cg MeronasDoor    = "img/cg/MeronasDoor/MeronasDoor.png"
    image cg MeronasDoor2    = "img/cg/MeronasDoor/MeronasDoor2.png"
    image cg MeronasRoom    = "img/cg/MeronasRoom.png"
    image cg MeronasRoom_2    = "img/cg/MeronasRoom2.png"
    image cg MeronasRoom_dark    = "img/cg/MeronasRoom_dark.png"
    
    image cg nightSky    = "img/cg/nightSky.png"
    
    image cg office    = "img/cg/office.png"
    image cg officeBack    = "img/cg/officeBack.png"
    image cg office2    = "img/cg/officeBack.png"
    
    image cg pharmacy    = "img/cg/pharmacy.png"
    
    image cg RettOnFloor    = "img/cg/RettOnGround/RettOnGround.png"
    image cg stream    = "img/cg/stream.png"
    
    image cg tailorDress    = "img/cg/tailorDress.png"
    image cg tailorDoor closed    = "img/cg/tailorShop/tailorDoor_closed.png"
    image cg tailorDoor open   = "img/cg/tailorShop/tailorDoor_open.png"
    image cg tailorDoor slightlyOpen   = "img/cg/tailorShop/tailorDoor_slightlyOpen.png"
    image cg tailorShopFront    = "img/cg/tailorShop/tailorFront.png"
    image cg tailorShopWall    = "img/cg/tailorShop/tailorWall.png"
    
    
    
    image cg town skyVersion    =  LiveComposite(
      (1920, 1080), 
      (0, 0), "img/cg/Intro/sky1.png",
      (0, 0), "img/cg/town.png",)
    image cg town    = "img/cg/town.png"
    image cg townHerbShop    = "img/cg/townHerbShop.png"
    image cg townShops    = "img/cg/townShops.png"
    
    image cg duranBurn1 = "img/cg/duranBurn/duranBurn1.png"
    image cg duranBurn2 = "img/cg/duranBurn/duranBurn2.png"
    image cg duranBurn3 = "img/cg/duranBurn/duranBurn3.png"
    image cg duranSulk1 = "img/cg/duranSulk/duranSulk1.png"
    image cg duranSulk2 = "img/cg/duranSulk/duranSulk2.png"
    image cg duranSulk3 = "img/cg/duranSulk/duranSulk3.png"
    image cg duranSulk4 = "img/cg/duranSulk/duranSulk4.png"
    image cg duranSulk5 = "img/cg/duranSulk/duranSulk5.png"
    image cg fallenTrunks = "img/cg/fallenTrunks.png"
    image cg fishMonster = "img/cg/fishMonster.png"
    image cg FishmonsterEyes = "img/cg/FishmonsterEyes.png"
    image cg forest20_5 = "img/cg/forest20_5.png"
    image cg forest20_75 = "img/cg/forest20_75.png"
    image cg forest26 = "img/cg/forest26.png"
    image cg forest26b = "img/cg/forest26b.png"
    image cg forest27 = "img/cg/forest27.png"
    image cg forest28 = "img/cg/forest28.png"
    image cg forest29 = "img/cg/forest29.png"
    image cg forest30 = "img/cg/forest30.png"
    image cg Kreita_ArmsonMR = "img/cg/Kreita_ArmsonMR/Kreita_ArmsonMR.png"
    image cg KreitaAttack = "img/cg/KreitaAttack.png"
    image cg KreitaGrab = "img/cg/KreitaGrab.png"
    image cg Lexan handOnMsArm1 = Animation( "img/cg/Lexan_handOnMsArm/Lexan_handOnMsArm1.png", 4,
                                             "img/cg/Lexan_handOnMsArm/Lexan_handOnMsArm1_b.png", 0.2)
    image cg Lexan handOnMsArm2 = Animation( "img/cg/Lexan_handOnMsArm/Lexan_handOnMsArm2.png", 4,
                                             "img/cg/Lexan_handOnMsArm/Lexan_handOnMsArm2_b.png", 0.2)
    image cg Lexan handOnMsArm3 = "img/cg/Lexan_handOnMsArm/Lexan_handOnMsArm3.png"
    image cg Lexan handOnMsArm4 = "img/cg/Lexan_handOnMsArm/Lexan_handOnMsArm4.png"
    image cg Lexan handOnMsArm5 = "img/cg/Lexan_handOnMsArm/Lexan_handOnMsArm5.png"
    
    
    
    
    image cg LexanRainShield = "img/cg/LexanRainShield.png"
    image cg MeronasMagic = "img/cg/MeronasMagic.png"
    image cg MeronaTreeHug = "img/cg/MeronaTreeHug/MeronaTreeHug.png"
    image cg monsterCat = "img/cg/monsterCat.png"
    image cg raspberry = "img/cg/raspberry.png"
    image RettKreitaSlap = "img/cg/RettKreitaSlap.png" 
    
    image cg antidote = "img/cg/antidote.png"
    image cg Calil = "img/cg/Calil.png"
    image cg campingFire = "img/cg/campingFire.png"
    image cg castleRoom = "img/cg/castleRoom.png"
    image cg cave = "img/cg/cave.png"
    image cg forest31 = "img/cg/forest31.png"
    image cg grave = "img/cg/grave.png"
    image cg InnLobby = "img/cg/InnLobby.png"
    image cg InnRoom = "img/cg/InnRoom.png"
    image cg Laneo = "img/cg/Laneo.png"
    image cg laneo = "img/cg/Laneo.png"
    image cg ocean = "img/cg/ocean.png"
    image cg ProwensHouse1 = "img/cg/ProwensHouse1.png"
    image cg ProwensHouse2 = "img/cg/ProwensHouse2.png"
    image cg ProwensHouse3 = "img/cg/ProwensHouse3.png"
    image cg RanansShopBack = "img/cg/RanansShopBack.png"
    image cg RoyalGardens = "img/cg/RoyalGardens.png"
    image cg RanansLair = "img/cg/RanansLair.png"
    
    image bg castleGate            = "img/bg/castleGate.png"
    image cg castleGate            = "img/bg/castleGate.png"
    image cg MeronaLexan_EyeCover  = "img/cg/MeronaLexan_EyeCover/MeronaLexan_EyeCover.png"
    image cg MeronaLexan_EyeCover2 = "img/cg/MeronaLexan_EyeCover/MeronaLexan_EyeCover2.png"

    image cg DuranPunch = "img/cg/DuranPunch/DuranPunch.png"
    image cg DuranPunch2 = "img/cg/DuranPunch/DuranPunch2.png"
    image cg DuranPunch3 = "img/cg/DuranPunch/DuranPunch3.png"
    image cg DuranPunch4 = "img/cg/DuranPunch/DuranPunch4.png"
    image cg DuranPunch5 = "img/cg/DuranPunch/DuranPunch5.png"
    
    
    image cg forest32 = "img/cg/forest32.png"
    image cg forest33 = "img/cg/forest33.png"
    image cg forest34 = "img/cg/forest34.png"
    image cg forest34_2 = "img/cg/forest34_2.png"
    image cg forest35 = "img/cg/forest35.png"
    image cg forest35_2 = "img/cg/forest35_2.png"
    
    image cg ANewJourney = "img/cg/ANewJourney.png"
    image cg CimariaRettFlirting = "img/cg/CimariaRettFlirting.png"
    image cg MeronaDuranCuddle = "img/cg/MeronaDuranCuddle.png"
    
    image cg MeronaDuranRomance1 = "img/cg/MeronaDuranRomance/MeronaDuranRomance1.png"
    image cg MeronaDuranRomance2 = "img/cg/MeronaDuranRomance/MeronaDuranRomance2.png"
    image cg MeronaDuranRomance3 = "img/cg/MeronaDuranRomance/MeronaDuranRomance3.png"
    
    image cg MeronaLexanRomance1 = "img/cg/MeronaLexanRomance/MeronaLexanRomance1.png"
    image cg MeronaLexanRomance2 = "img/cg/MeronaLexanRomance/MeronaLexanRomance2.png"
    image cg MeronaLexanRomance3 = "img/cg/MeronaLexanRomance/MeronaLexanRomance3.png"
    
    image cg MeronasLove_A = "img/cg/MeronasLove_A.png"
    image cg MeronasLove_B = "img/cg/MeronasLove_B.png"
    
    image cg ProwenAwakes = "img/cg/ProwenAwakes.png"
    image cg riverSide = "img/cg/riverSide.png"
    image cg streamGround    = "img/cg/streamGround.png"
    image cg ProwensGoodbye = "img/cg/ProwensGoodbye.png"
    
    image cg L_holdingM1 = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/L_holdingM/L_holdingM_base.png",
    (470 , 334),  "img/cg/L_holdingM/LFace_1.png", (470 , 334), "img/cg/L_holdingM/LFace_eyes.png", 
    (1238 , 507), "img/cg/L_holdingM/MFace_1.png",(1238 , 507), "img/cg/L_holdingM/MFace_eyes.png",
    (0, 0), "img/cg/L_holdingM/L_holdingM_top.png",)
    
    image cg L_holdingM2 = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/L_holdingM/L_holdingM_base.png",
    (470 , 334),  "img/cg/L_holdingM/LFace_1.png", (470 , 334), "img/cg/L_holdingM/LFace_eyes.png", 
    (1238 , 507), "img/cg/L_holdingM/MFace_2.png",(1238 , 507), "img/cg/L_holdingM/MFace_eyes.png",
    (0, 0), "img/cg/L_holdingM/L_holdingM_top.png",)
    
    image cg L_holdingM3 = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/L_holdingM/L_holdingM_base.png",
    (470 , 334),  "img/cg/L_holdingM/LFace_2.png", (470 , 334), "img/cg/L_holdingM/LFace_eyes.png", 
    (1238 , 507), "img/cg/L_holdingM/MFace_3.png",(1238 , 507), "img/cg/L_holdingM/MFace_eyes.png",
    (0, 0), "img/cg/L_holdingM/L_holdingM_top.png",)
    
    image cg L_holdingM4 = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/L_holdingM/L_holdingM_base.png",
    (470 , 334),  "img/cg/L_holdingM/LFace_1.png", (470 , 334), "img/cg/L_holdingM/LFace_eyes.png", 
    (1238 , 507), "img/cg/L_holdingM/MFace_3.png",(1238 , 507), "img/cg/L_holdingM/MFace_eyes.png",
    (0, 0), "img/cg/L_holdingM/L_holdingM_top.png",)
    
    image cg L_holdingM5 = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/L_holdingM/L_holdingM_base.png",
    (470 , 334),  "img/cg/L_holdingM/LFace_3.png", (470 , 334), "img/cg/L_holdingM/LFace_eyes.png", 
    (1238 , 507), "img/cg/L_holdingM/MFace_3.png",(1238 , 507), "img/cg/L_holdingM/MFace_eyes.png",
    (0, 0), "img/cg/L_holdingM/L_holdingM_top.png",)
    
    image cg L_holdingM6 = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/L_holdingM/L_holdingM_base.png",
    (470 , 334),  "img/cg/L_holdingM/LFace_4.png", (470 , 334), "img/cg/L_holdingM/LFace_eyes.png", 
    (1238 , 507), "img/cg/L_holdingM/MFace_2.png",(1238 , 507), "img/cg/L_holdingM/MFace_eyes.png",
    (0, 0), "img/cg/L_holdingM/L_holdingM_top.png",)
    
    image cg L_holdingM7 = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/L_holdingM/L_holdingM_base.png",
    (470 , 334),  "img/cg/L_holdingM/LFace_4.png", (470 , 334), "img/cg/L_holdingM/LFace_eyes.png", 
    (1238 , 507), "img/cg/L_holdingM/MFace_3.png",(1238 , 507), "img/cg/L_holdingM/MFace_eyes.png",
    (0, 0), "img/cg/L_holdingM/L_holdingM_top.png",)
    
    image cg L_holdingM8 = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/L_holdingM/L_holdingM_base.png",
    (470 , 334),  "img/cg/L_holdingM/LFace_4.png", (470 , 334), "img/cg/L_holdingM/LFace_eyes.png", 
    (1238 , 507), "img/cg/L_holdingM/MFace_4.png",(1238 , 507), "img/cg/L_holdingM/MFace_eyes.png",
    (0, 0), "img/cg/L_holdingM/L_holdingM_top.png",)
    
    image cg L_holdingM9 = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/L_holdingM/L_holdingM_base.png",
    (470 , 334),  "img/cg/L_holdingM/LFace_3.png", (470 , 334), "img/cg/L_holdingM/LFace_eyes.png", 
    (1238 , 507), "img/cg/L_holdingM/MFace_5.png",(1238 , 507), "img/cg/L_holdingM/MFace_eyes.png",
    (0, 0), "img/cg/L_holdingM/L_holdingM_top.png",)
    
    image cg L_holdingM10 = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/L_holdingM/L_holdingM_base.png",
    (470 , 334),  "img/cg/L_holdingM/LFace_4.png", (470 , 334), "img/cg/L_holdingM/LFace_eyes.png", 
    (1238 , 507), "img/cg/L_holdingM/MFace_4.png",(1238 , 507), "img/cg/L_holdingM/MFace_eyes.png",
    (0, 0), "img/cg/L_holdingM/L_holdingM_top.png",)
    
    image cg L_holdingM11 = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/L_holdingM/L_holdingM_base.png",
    (470 , 334),  "img/cg/L_holdingM/LFace_5.png", (470 , 334), "img/cg/L_holdingM/LFace_eyes.png", 
    (1238 , 507), "img/cg/L_holdingM/MFace_5.png",(1238 , 507), "img/cg/L_holdingM/MFace_eyes.png",
    (0, 0), "img/cg/L_holdingM/L_holdingM_top.png",)
    
    image cg L_holdingM12 = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/L_holdingM/L_holdingM_base.png",
    (470 , 334),  "img/cg/L_holdingM/LFace_4.png", (470 , 334), "img/cg/L_holdingM/LFace_eyes.png", 
    (1238 , 507), "img/cg/L_holdingM/MFace_6.png",(1238 , 507), "img/cg/L_holdingM/MFace_eyes12.png",
    (0, 0), "img/cg/L_holdingM/L_holdingM_top.png",)
    
    image cg L_holdingM13 = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/L_holdingM/L_holdingM_base.png",
    (470 , 334),  "img/cg/L_holdingM/LFace_4.png", (470 , 334), "img/cg/L_holdingM/LFace_eyes.png", 
    (1238 , 507), "img/cg/L_holdingM/MFace_7.png",(1238 , 507), "img/cg/L_holdingM/MFace_eyes12.png",
    (0, 0), "img/cg/L_holdingM/L_holdingM_top.png",)
    
    image cg L_holdingM14 = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/L_holdingM/L_holdingM_base.png",
    (470 , 334),  "img/cg/L_holdingM/LFace_6.png", (470 , 334), "img/cg/L_holdingM/LFace_eyes.png", 
    (1238 , 507), "img/cg/L_holdingM/MFace_6.png",(1238 , 507), "img/cg/L_holdingM/MFace_eyes12.png",
    (0, 0), "img/cg/L_holdingM/L_holdingM_top.png",)
    
    image cg L_holdingM15 = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/L_holdingM/L_holdingM_base.png",
    (470 , 334),  "img/cg/L_holdingM/LFace_7.png", (470 , 334), "img/cg/L_holdingM/LFace_eyes.png", 
    (1238 , 507), "img/cg/L_holdingM/MFace_7.png",(1238 , 507), "img/cg/L_holdingM/MFace_eyes12.png",
    (0, 0), "img/cg/L_holdingM/L_holdingM_top.png",)
    
    image cg L_holdingM16 = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/L_holdingM/L_holdingM_base.png",
    (470 , 334),  "img/cg/L_holdingM/LFace_7.png", (470 , 334), "img/cg/L_holdingM/LFace_eyes.png", 
    (1238 , 507), "img/cg/L_holdingM/MFace_6.png",(1238 , 507), "img/cg/L_holdingM/MFace_eyes12.png",
    (0, 0), "img/cg/L_holdingM/L_holdingM_top.png",)
    
    image cg L_holdingM17 = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/L_holdingM/L_holdingM_base.png",
    (470 , 334),  "img/cg/L_holdingM/LFace_7.png", (470 , 334), "img/cg/L_holdingM/LFace_eyes.png", 
    (1238 , 507), "img/cg/L_holdingM/MFace_8.png",(1238 , 507), "img/cg/L_holdingM/MFace_eyes12.png",
    (0, 0), "img/cg/L_holdingM/L_holdingM_top.png",)
    
    image cg L_holdingM18 = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/L_holdingM/L_holdingM_base.png",
    (470 , 334),  "img/cg/L_holdingM/LFace_8.png", (470 , 334), "img/cg/L_holdingM/LFace_eyes.png", 
    (1238 , 507), "img/cg/L_holdingM/MFace_6.png",(1238 , 507), "img/cg/L_holdingM/MFace_eyes12.png",
    (0, 0), "img/cg/L_holdingM/L_holdingM_top.png",)
    
    image cg L_holdingM19 = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/L_holdingM/L_holdingM_base.png",
    (470 , 334),  "img/cg/L_holdingM/LFace_9.png", (470 , 334), "img/cg/L_holdingM/LFace_eyes.png", 
    (1238 , 507), "img/cg/L_holdingM/MFace_6.png",(1238 , 507), "img/cg/L_holdingM/MFace_eyes12.png",
    (0, 0), "img/cg/L_holdingM/L_holdingM_top.png",)
    
    # Tailorshop composite
    image cg tailorshop back = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/tailorDress.png",
    (0, 0), "img/cg/tailorShop/tailorWall.png",
    (0, 0), "img/cg/tailorShop/tailorDoor_closed.png",)
    
    image tailorshop front = "img/cg/tailorShop/tailorFront.png"
    
    image cg tailorshop door closed = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/tailorDress.png",
    (0, 0), "img/cg/tailorShop/tailorWall.png",
    (0, 0), "img/cg/tailorShop/tailorDoor_closed.png",    
    (0, 0), "img/cg/tailorShop/tailorM.png",
    (0, 0), "img/cg/tailorShop/tailorFront.png",)
    
    image cg tailorshop door slightlyOpen = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/tailorDress.png",
    (0, 0), "img/cg/tailorShop/tailorWall.png",
    (0, 0), "img/cg/tailorShop/tailorDoor_slightlyOpen.png",    
    (0, 0), "img/cg/tailorShop/tailorM.png",
    (0, 0), "img/cg/tailorShop/tailorFront.png",)

    image cg tailorshop duran = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/tailorDress.png",
    (0, 0), "img/cg/tailorShop/tailorWall.png",
    (0, 0), "img/cg/tailorShop/tailorD_body.png",
    (0, 0), "img/cg/tailorShop/tailorD_bodyTop.png",
    (0, 0), Animation("img/cg/tailorShop/tailorD_eyesOpen.png", 1.2,
                      "img/cg/tailorShop/tailorD_eyesClosed.png", 0.2),
    (0, 0), "img/cg/tailorShop/tailorD_mouthClosed.png",
    (0, 0), "img/cg/tailorShop/tailorDoor_open.png",    
    (0, 0), "img/cg/tailorShop/tailorM.png",
    (0, 0), "img/cg/tailorShop/tailorFront.png",)
    
    image cg tailorshop duran OM = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/tailorDress.png",
    (0, 0), "img/cg/tailorShop/tailorWall.png",
    (0, 0), "img/cg/tailorShop/tailorD_body.png",
    (0, 0), "img/cg/tailorShop/tailorD_bodyTop.png",
    (0, 0), Animation("img/cg/tailorShop/tailorD_eyesOpen.png", 1.2,
                      "img/cg/tailorShop/tailorD_eyesClosed.png", 0.2),
    (0, 0), "img/cg/tailorShop/tailorD_mouthOpen.png",
    (0, 0), "img/cg/tailorShop/tailorDoor_open.png",    
    (0, 0), "img/cg/tailorShop/tailorM.png",
    (0, 0), "img/cg/tailorShop/tailorFront.png",)
    
    image cg tailorshop duran SO = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/tailorDress.png",
    (0, 0), "img/cg/tailorShop/tailorWall.png",
    (0, 0), "img/cg/tailorShop/tailorD_body.png",
    (0, 0), "img/cg/tailorShop/tailorD_bodyTop.png",
    (0, 0), Animation("img/cg/tailorShop/tailorD_eyesOpen.png", 1.2,
                      "img/cg/tailorShop/tailorD_eyesClosed.png", 0.2),
    (0, 0), "img/cg/tailorShop/tailorD_mouthClosed.png",
    (0, 0), "img/cg/tailorShop/tailorDoor_slightlyOpen.png",  
    (0, 0), "img/cg/tailorShop/tailorM.png",
    (0, 0), "img/cg/tailorShop/tailorFront.png",)
    
    image cg tailorshop duran SO OM = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/tailorDress.png",
    (0, 0), "img/cg/tailorShop/tailorWall.png",
    (0, 0), "img/cg/tailorShop/tailorD_body.png",
    (0, 0), "img/cg/tailorShop/tailorD_bodyTop.png",
    (0, 0), Animation("img/cg/tailorShop/tailorD_eyesOpen.png", 1.2,
                      "img/cg/tailorShop/tailorD_eyesClosed.png", 0.2),
    (0, 0), "img/cg/tailorShop/tailorD_mouthOpen.png",
    (0, 0), "img/cg/tailorShop/tailorDoor_slightlyOpen.png",  
    (0, 0), "img/cg/tailorShop/tailorM.png",
    (0, 0), "img/cg/tailorShop/tailorFront.png",)
    
    # RettAtTree defines
    image cg RettAtTree = LiveComposite(
    (1920, 1080),
    (0, 0), "img/cg/RettAtTree/RettAtTree.png",
    (0, 0), Animation("img/cg/RettAtTree/RettAtTree_RettEyes.png", 3.2,
                      "img/cg/RettAtTree/RettAtTree_RettEyesCE.png", 0.2),)
    
    image CimariaAtTree pose1 = "img/cg/RettAtTree/CimariaAtTree.png"
    image CimariaAtTree pose2 = "img/cg/RettAtTree/CimariaAtTree2.png"
    image CimariaAtTree pose3 = "img/cg/RettAtTree/CimariaAtTree3.png"
    
    image KreitaAtTree pose1 = "img/cg/RettAtTree/KreitaAtTree.png"
    image KreitaAtTree pose2 = "img/cg/RettAtTree/KreitaAtTree2.png"
    
    image RettAtTree face1 = "img/cg/RettAtTree/RettAtTree_face1.png"
    image RettAtTree face2 = "img/cg/RettAtTree/RettAtTree_face2.png"
    image RettAtTree face3 = "img/cg/RettAtTree/RettAtTree_face3.png"
    image RettAtTree face4 = "img/cg/RettAtTree/RettAtTree_face4.png"
    image RettAtTree face5 = "img/cg/RettAtTree/RettAtTree_face5.png"
    
    # Nightfire defines
    image cg nightFire = "img/cg/nightFire/nightFire.png"                      
    image nightFire_BoyenKreitaLexanDuran = "img/cg/nightFire/nightFire_BoyenKreitaLexanDuran.png"
    image nightFire_BoyenKreitaLexanDuran_outlines = "img/cg/nightFire/nightFire_BoyenKreitaLexanDuran_outlines.png"
    image nightFire_campFire = "img/cg/nightFire/nightFire_campfire.png"
    image nightFire_frontPlants = "img/cg/nightFire/nightFire_frontPlants.png"
    image nightFire_RettCimaria = "img/cg/nightFire/nightFire_RettCimaria.png"
    
    # boyen
    image boyen nightFire closed = LiveComposite(
    (1920, 1720),
    (0, 0), Animation("img/cg/nightFire/Boyen/B_NF_closed.png", 2.2,
                      "img/cg/nightFire/Boyen/B_NF_closed_CE.png", 0.2),)                      
    image boyen nightFire open = LiveComposite(
    (1920, 1720),
    (0, 0), Animation("img/cg/nightFire/Boyen/B_NF_open.png", 2.2,
                      "img/cg/nightFire/Boyen/B_NF_open_CE.png", 0.2),)
    
    # Cimeria Not facing camera
    
    # duran 
    image duran nightFire closed = LiveComposite(
    (1920, 1720),
    (0, 0), Animation("img/cg/nightFire/Duran/D_NF_closed.png", 3.2,
                      "img/cg/nightFire/Duran/D_NF_closed_CE.png", 0.2),)                      
    image duran nightFire open = LiveComposite(
    (1920, 1720),
    (0, 0), Animation("img/cg/nightFire/Duran/D_NF_open.png", 3.2,
                      "img/cg/nightFire/Duran/D_NF_open_CE.png", 0.2),)
    image duran nightFire closed annoyed = LiveComposite(
    (1920, 1720),
    (0, 0), Animation("img/cg/nightFire/Duran/D_NF_closed_annoyed.png", 3.2,
                      "img/cg/nightFire/Duran/D_NF_closed_CE.png", 0.2),)                      
    image duran nightFire open annoyed = LiveComposite(
    (1920, 1720),
    (0, 0), Animation("img/cg/nightFire/Duran/D_NF_open_annoyed.png", 3.2,
                      "img/cg/nightFire/Duran/D_NF_open_CE.png", 0.2),)
    
    # kreita 
    image kreita nightFire closed = LiveComposite(
    (1920, 1720),
    (0, 0), Animation("img/cg/nightFire/Kreita/K_NF_closed.png", 3.5,
                      "img/cg/nightFire/Kreita/K_NF_closed_CE.png", 0.2),)                      
    image kreita nightFire open = LiveComposite(
    (1920, 1720),
    (0, 0), Animation("img/cg/nightFire/Kreita/K_NF_open.png", 3.5,
                      "img/cg/nightFire/Kreita/K_NF_open_CE.png", 0.2),)
    image kreita nightFire closed nervous = LiveComposite(
    (1920, 1720),
    (0, 0), Animation("img/cg/nightFire/Kreita/K_NF_closed_nervous.png", 3.5,
                      "img/cg/nightFire/Kreita/K_NF_closed_CE.png", 0.2),)                      
    #image kreita nightFire open nervous = LiveComposite(
    #(1920, 1720),
    #(0, 0), Animation("img/cg/nightFire/Kreita/K_NF_open_nervous.png", 3.5,
    #                  "img/cg/nightFire/Kreita/K_NF_open_CE.png", 0.2),)
    image kreita nightFire closed pouty = LiveComposite(
    (1920, 1720),
    (0, 0), Animation("img/cg/nightFire/Kreita/K_NF_closed_pouty.png", 3.5,
                      "img/cg/nightFire/Kreita/K_NF_closed_pouty_CE.png", 0.2),)
    image kreita nightFire open pouty = LiveComposite(
    (1920, 1720),
    (0, 0), Animation("img/cg/nightFire/Kreita/K_NF_open_pouty.png", 3.5,
                      "img/cg/nightFire/Kreita/K_NF_open_pouty_CE.png", 0.2),)
    
    # lexan 
    image lexan nightFire closed = LiveComposite(
    (1920, 1720),
    (0, 0), Animation("img/cg/nightFire/Lexan/L_NF_closed.png", 4.2,
                      "img/cg/nightFire/Lexan/L_NF_closed_CE.png", 0.2),)                      
    image lexan nightFire open = LiveComposite(
    (1920, 1720),
    (0, 0), Animation("img/cg/nightFire/Lexan/L_NF_open.png", 4.2,
                      "img/cg/nightFire/Lexan/L_NF_open_CE.png", 0.2),)
    image lexan nightFire closed nervous = LiveComposite(
    (1920, 1720),
    (0, 0), Animation("img/cg/nightFire/Lexan/L_NF_closed_nervous.png", 4.2,
                      "img/cg/nightFire/Lexan/L_NF_closed_CE.png", 0.2),)
  
    # Prowen
    image prowen nightFire closed = LiveComposite(
    (1920, 1720),
    (0, 0), "img/cg/nightFire/Prowen/nightFire_Prowen.png",
    (0, 0), Animation("img/cg/nightFire/Prowen/P_NF_closed.png", 5.2,
                      "img/cg/nightFire/Prowen/P_NF_closed_CE.png", 0.2),) 
    image prowen nightFire open = LiveComposite(
    (1920, 1720),
    (0, 0), "img/cg/nightFire/Prowen/nightFire_Prowen.png",
    (0, 0), Animation("img/cg/nightFire/Prowen/P_NF_open.png", 5.2,
                      "img/cg/nightFire/Prowen/P_NF_open_CE.png", 0.2),) 
    image prowen nightFire closed CE = LiveComposite(
    (1920, 1720),
    (0, 0), "img/cg/nightFire/Prowen/nightFire_Prowen.png",
    (0, 0), "img/cg/nightFire/Prowen/P_NF_closed_CE.png",) 
    image prowen nightFire open CE = LiveComposite(
    (1920, 1720),
    (0, 0), "img/cg/nightFire/Prowen/nightFire_Prowen.png",
    (0, 0), "img/cg/nightFire/Prowen/P_NF_open_CE.png",) 
    
    # rett
    image rett nightFire closed = LiveComposite(
    (1920, 1720),
    (0, 0), Animation("img/cg/nightFire/Rett/R_NF_closed.png", 3.2,
                      "img/cg/nightFire/Rett/R_NF_closed_CE.png", 0.2),
    (0, 0), "img/cg/nightFire/Rett/nightFire_Rett_outlines.png",)  
    image rett nightFire closed sassy = LiveComposite(
    (1920, 1720),
    (0, 0), Animation("img/cg/nightFire/Rett/R_NF_closed_sassy.png", 3.2,
                      "img/cg/nightFire/Rett/R_NF_closed_sassy_CE.png", 0.2),
    (0, 0), "img/cg/nightFire/Rett/nightFire_Rett_outlines.png",) 
    #Missing?
    image rett nightFire open = LiveComposite(
    (1920, 1720),
    (0, 0), Animation("img/cg/nightFire/Rett/R_NF_open_sassy.png", 3.2,
                      "img/cg/nightFire/Rett/R_NF_open_sassy_CE.png", 0.2),
    (0, 0), "img/cg/nightFire/Rett/nightFire_Rett_outlines.png",)
    image rett nightFire open sassy = LiveComposite(
    (1920, 1720),
    (0, 0), Animation("img/cg/nightFire/Rett/R_NF_open_sassy.png", 3.2,
                      "img/cg/nightFire/Rett/R_NF_open_sassy_CE.png", 0.2),
    (0, 0), "img/cg/nightFire/Rett/nightFire_Rett_outlines.png",)
    
    # merona
    image merona nightFire closed = LiveComposite(
    (1920, 1720),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona.png",
    (0, 0), Animation("img/cg/nightFire/Merona/M_NF_closed.png", 2.5,
                      "img/cg/nightFire/Merona/M_NF_closed_CE.png", 0.2),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona_outlines.png",) 
    image merona nightFire open = LiveComposite(
    (1920, 1720),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona.png",
    (0, 0), Animation("img/cg/nightFire/Merona/M_NF_open.png", 2.5,
                      "img/cg/nightFire/Merona/M_NF_open_CE.png", 0.2),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona_outlines.png",) 
  
    image merona nightFire closed desperate = LiveComposite(
    (1920, 1720),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona.png",
    (0, 0), Animation("img/cg/nightFire/Merona/M_NF_closed_desperate.png", 2.5,
                      "img/cg/nightFire/Merona/M_NF_closed_desperate_CE.png", 0.2),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona_outlines.png",) 
    image merona nightFire open desperate = LiveComposite(
    (1920, 1720),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona.png",
    (0, 0), Animation("img/cg/nightFire/Merona/M_NF_open_desperate.png", 2.5,
                      "img/cg/nightFire/Merona/M_NF_open_desperate_CE.png", 0.2),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona_outlines.png",) 
    image merona nightFire closed eyesUp = LiveComposite(
    (1920, 1720),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona.png",
    (0, 0), Animation("img/cg/nightFire/Merona/M_NF_closed_eyesUp.png", 2.5,
                      "img/cg/nightFire/Merona/M_NF_closed_CE.png", 0.2),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona_outlines.png",) 
    image merona nightFire closed nervous = LiveComposite(
    (1920, 1720),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona.png",
    (0, 0), Animation("img/cg/nightFire/Merona/M_NF_closed_nervous.png", 2.5,
                      "img/cg/nightFire/Merona/M_NF_closed_nervous_CE.png", 0.2),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona_outlines.png",) 
    image merona nightFire open nervous = LiveComposite(
    (1920, 1720),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona.png",
    (0, 0), Animation("img/cg/nightFire/Merona/M_NF_open_nervous.png", 2.5,
                      "img/cg/nightFire/Merona/M_NF_open_nervous_CE.png", 0.2),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona_outlines.png",) 
    image merona nightFire closed scared = LiveComposite(
    (1920, 1720),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona.png",
    (0, 0), Animation("img/cg/nightFire/Merona/M_NF_closed_scared.png", 2.5,
                      "img/cg/nightFire/Merona/M_NF_closed_scared_CE.png", 0.2),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona_outlines.png",) 
    image merona nightFire closed veryScared = LiveComposite(
    (1920, 1720),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona.png",
    (0, 0), Animation("img/cg/nightFire/Merona/M_NF_closed_veryScared.png", 2.5,
                      "img/cg/nightFire/Merona/M_NF_closed_veryScared_CE.png", 0.2),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona_outlines.png",) 
    image merona nightFire open veryScared = LiveComposite(
    (1920, 1720),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona.png",
    (0, 0), Animation("img/cg/nightFire/Merona/M_NF_open_veryScared.png", 2.5,
                      "img/cg/nightFire/Merona/M_NF_open_veryScared_CE.png", 0.2),
    (0, 0), "img/cg/nightFire/Merona/nightFire_Merona_outlines.png",) 
    
    ######### SPRITE IMAGE DEFINES #############
    
    image leaf1 = "img/sprites/Objects/Leaf1.png"
    image leaf2 = "img/sprites/Objects/Leaf2.png"
    image leaf1_small = "img/sprites/Objects/Leaf1_small.png"
    image leaf2_small = "img/sprites/Objects/Leaf2_small.png"
    image leaf1b = "img/sprites/Objects/Leaf1.png"
    image leaf2b = "img/sprites/Objects/Leaf2.png"
    image leaf1b_small = "img/sprites/Objects/Leaf1_small.png"
    image leaf2b_small = "img/sprites/Objects/Leaf2_small.png"
    image tree = "img/sprites/Objects/Tree.png"
    image clouds = "img/sprites/Objects/Clouds.png"
    
    image bush1 = "img/sprites/Objects/Background elements/bush1.png"
    image bush2 = "img/sprites/Objects/Background elements/bush2.png"
    image bush3 = "img/sprites/Objects/Background elements/bush3.png"
    image bush4 = "img/sprites/Objects/Background elements/bush4.png"
    image bush5 = "img/sprites/Objects/Background elements/bush5.png"
    image bush6 = "img/sprites/Objects/Background elements/bush6.png"
    image clouds dark = "img/sprites/Objects/Background elements/Clouds_dark.png"
    image Clouds dark = "img/sprites/Objects/Background elements/Clouds_dark.png"
    image tree1 = "img/sprites/Objects/Background elements/tree1.png"
    image tree1_moss = "img/sprites/Objects/Background elements/tree1_moss.png"
    image tree1_V2 = "img/sprites/Objects/Background elements/tree1_V2.png"
    image tree1_V2_moss = "img/sprites/Objects/Background elements/tree1_V2_moss.png"
    image tree1_V3 = "img/sprites/Objects/Background elements/tree1_V3.png"
    image tree1_V4 = "img/sprites/Objects/Background elements/tree1_V4.png"
    image tree2 = "img/sprites/Objects/Background elements/tree2.png"
    #image leaf1 = "img/sprites/Objects/Background elements/Leaf1.png"
    #image leaf1_small = "img/sprites/Objects/Background elements/Leaf1_small.png"
    #image leaf2 = "img/sprites/Objects/Background elements/Leaf2.png"
    #image leaf2_small = "img/sprites/Objects/Background elements/Leaf2_small.png"
    image plant1 = "img/sprites/Objects/Background elements/plant1.png"
    image plant2 = "img/sprites/Objects/Background elements/plant2.png"
    image plant3 = "img/sprites/Objects/Background elements/plant3.png"
    image plant4 = "img/sprites/Objects/Background elements/plant4.png"
    image plant5 = "img/sprites/Objects/Background elements/plant5.png"
    image plant6 = "img/sprites/Objects/Background elements/plant6.png"
    image plant7 = "img/sprites/Objects/Background elements/plant7.png"
    image rock1 = "img/sprites/Objects/Background elements/rock1.png"
    image rock2 = "img/sprites/Objects/Background elements/rock2.png"
    image rock3 = "img/sprites/Objects/Background elements/rock3.png"
    image tree3 = "img/sprites/Objects/Background elements/tree3.png"
    image tree4 = "img/sprites/Objects/Background elements/tree4.png"
    image tree5 = "img/sprites/Objects/Background elements/tree5.png"
    image tree6_wide = "img/sprites/Objects/Background elements/tree6_wide tree.png"
    image tree7 = "img/sprites/Objects/Background elements/tree7.png"
    image cypress = "img/sprites/Objects/Background elements/cypress.png"
    image herb1 = "img/sprites/Objects/Background elements/herb1.png"
    image highGrass = "img/sprites/Objects/Background elements/high grass.png"
    image tree_dark = "img/sprites/Objects/tree_dark.png"
    
    image foliage screen1 = "img/sprites/Objects/Background elements/foliage screen.png"
    image foliage screen2 = "img/sprites/Objects/Background elements/foliage screen2.png"
    image plant1b = "img/sprites/Objects/Background elements/plant1b.png"
    image plant4b = "img/sprites/Objects/Background elements/plant4b.png"
    image plant4c = "img/sprites/Objects/Background elements/plant4c.png"
    image plant5b = "img/sprites/Objects/Background elements/plant5b.png"
    image plant5c = "img/sprites/Objects/Background elements/plant5c.png"
    image tree2b = "img/sprites/Objects/Background elements/tree2b.png"
    image tree_long = "img/sprites/Objects/Background elements/tree_long.png"
    
    image blanket = "img/sprites/Objects/blanket.png"
    image mattress = "img/sprites/Objects/mattress.png"
    image townHerbs = "img/sprites/Objects/townHerbs.png"
    image wagon = "img/sprites/Objects/wagon.png"
    image wagon empty = "img/sprites/Objects/wagon_empty.png"
    image desk = "img/sprites/Objects/desk.png"
    image book = "img/sprites/Objects/book.png"
    image glowingPot = "img/sprites/Objects/glowingPot.png"
    image hill = "img/sprites/Objects/hill.png"
    image Meronasdesk = "img/sprites/Objects/Meronasdesk.png"
    image bird = "img/sprites/Objects/bird.png"
    
    image rabbitMonster = "img/sprites/Other/RabbitMonster.png"
    image rabbitMonster shadow = "img/sprites/Other/RabbitMonstershadow.png"
    image birdMonster = "img/sprites/Other/birdMonster.png"
    image finalMonster1 = "img/sprites/Other/finalMonster1.png"
    image finalMonster2 = "img/sprites/Other/finalMonster2.png"
    
    image laneoBoy = "img/sprites/Other/laneoBoy.png"
    
    ## --- Composite images for gallery
    image cg_composite L_holding_M1 = "img/cg/composites/L_holding_M1.png"
    image cg_composite L_holding_M2 = "img/cg/composites/L_holding_M2.png"
    image cg_composite L_holding_M3 = "img/cg/composites/L_holding_M3.png"
    image cg_composite MeronasRoom2_full = "img/cg/composites/MeronasRoom2_full.png"
    image cg_composite nightFire_full = "img/cg/composites/nightFire_full.png"
    image cg_composite Office = "img/cg/composites/Office.png"
    image cg_composite RettAtTree_full1 = "img/cg/composites/RettAtTree_full1.png"
    image cg_composite RettAtTree_full2 = "img/cg/composites/RettAtTree_full2.png"
    image cg_composite RettAtTree_full3 = "img/cg/composites/RettAtTree_full3.png"
    image cg_composite tailorShop_full1 = "img/cg/composites/tailorShop_full1.png"
    image cg_composite tailorShop_full2 = "img/cg/composites/tailorShop_full2.png"
    image cg_composite tailorShop_full3 = "img/cg/composites/tailorShop_full3.png"
    image cg_composite town_full = "img/cg/composites/town_full.png"

    ## ---
    
    
    image cg1 = "img/cg/Intro/intro1.png"
    image cg2 = "img/cg/Intro/intro2.png"
    image cg3 = "img/cg/Intro/intro1.png"
    image cg4 = "img/cg/Intro/intro3.png"
    image cg5 = "img/cg/Intro/intro1.png"
    image cg6 = "img/cg/Intro/intro4.png"
    image cg7 = "img/cg/Intro/intro1.png"
    image cg8 = "img/cg/Intro/intro2.png"
    image cg9 = "img/cg/Intro/intro1.png"
    image cg10 = "img/cg/Intro/intro1.png"
    
    
    ######### CHARACTER IMAGE DEFINES #############
    