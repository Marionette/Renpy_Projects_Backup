init:
    define config.developer = True#False#
    ######### CHARACTER DEFINES #############
    define minami = Character("Minami")
    define qq = Character("???")
    define eiichi = Character("Eiichi")
    define takehito = Character("Takehito")
    define umeko = Character("Umeko")
    define watch = Character("Watch")
    define clock = Character("Clock")
    define announcer = Character("Announcer")
    define page = Character("Page")
    
    #Dating minigame character defines
    define eiichi_d = Character("Eiichi", window_background=Image("gui/textbox_dating.png", xalign=0.5, yalign=1.0))
    define umeko_d = Character("Umeko", window_background=Image("gui/textbox_dating.png", xalign=0.5, yalign=1.0))
    define narrator_d = Character(None, window_background=Image("gui/textbox_dating.png", xalign=0.5, yalign=1.0))


    ######### SOUND DEFINES #############
    $S_ObjectImpact = "audio/sfx/S_ObjectImpact.mp3"
    $S_PhoneTap = "audio/sfx/S_PhoneTap.mp3"
    $S_PhoneVibrate = "audio/sfx/S_PhoneVibrate.mp3"
    $S_SubwayAmbience = "audio/sfx/S_SubwayAmbience.mp3"
    $S_BlackRoom = "audio/sfx/room_ambience/S_BlackRoom.mp3"
    $S_WhiteRoom = "audio/sfx/room_ambience/S_WhiteRoom.mp3"
    $S_AlarmNoise = "audio/sfx/S_AlarmNoise.mp3"
    $S_ArenaAmbience = "audio/sfx/S_ArenaAmbience.mp3"
    $S_Doorbell = "audio/sfx/S_Doorbell.mp3"
    $S_RepeatDoorbell = "audio/sfx/S_RepeatDoorbell.mp3"
    $S_SciFiGunShot = "audio/sfx/S_SciFiGunShot.wav"
    $S_TVGameShowNoise = "audio/sfx/S_TVGameShowNoise.mp3"

    #TODO replace with actual music files
    $mizuki = "audio/sfx/S_mizukisubway.mp3"
    $idleM =  "audio/music/M_botto-hidamari.mp3"
    $youlikejazz = "audio/music/M_Dog-Days.mp3"
    $funM = "audio/music/M_husigityan-o-ra.mp3"
    $Sad1M = "audio/music/M_gomenne.mp3"
    $Sad2M = "audio/music/M_kokyou-no-yuuhi-mbox.mp3"


    ######### CG/BG IMAGE DEFINES #############
    image black = Solid("#000000")
    image bg black = Solid("#000000")
    image bg white = Solid("#FFFFFF")
    image bg game_menu_overlay = "gui/overlay/game_menu.png"


    #TODO Backgrounds

    image bg ApartmentHallway = "images/backgrounds/B_ApartmentHallway.png"
    image bg BathFoggy = "images/backgrounds/B_BathFoggy.png"
    image bg DiningRoom = "images/backgrounds/B_DiningRoom.png"
    image bg MorningBedroom =  "images/backgrounds/B_MorningBedroom.png"
    image bg DoorEntrance =  "images/backgrounds/B_DoorEntrance.jpg"
    image bg HouseRoom =  "images/backgrounds/B_HouseRoom.png"
    image bg OutsideCafe =  "images/backgrounds/B_OutsideCaf.png"
    image bg PastelScenery =  "images/backgrounds/B_PastelScenery.jpg"
    image bg Subway =  "images/backgrounds/B_Subway.png"
    image bg SubwayPlatform =  "images/backgrounds/B_SubwayPlatform.png"
    image bg TournamentArena =  "images/backgrounds/B_Tournament.png"


    #TODO CG images

    #TODO Characters

    image eiichi  cry = "images/sprites/C_EiichiCrySprite.png"
    image eiichi  happy  = "images/sprites/C_EiichiHappySprite.png"
    image eiichi  normal  = "images/sprites/C_EiichiNormalSprite.png"


    image minami  angry = "images/sprites/C_MinamiAngerSprite.png"
    image minami  concerned = "images/sprites/C_MinamiConcernedSprite.png"
    image minami  confused = "images/sprites/C_MinamiConfusedSprite.png"
    image minami  disappointed = "images/sprites/C_MinamiDisappointedSprite.png"
    image minami  happy  = "images/sprites/C_MinamiHappySprite.png"
    image minami  normal  = "images/sprites/C_MinamiNormalSprite.png"
    image minami  shocked = "images/sprites/C_MinamiShockedSprite.png"
    image minami  upset  = "images/sprites/C_MinamiUpsetSprite.png"


    image takehito  angry  = "images/sprites/C_TakehitoAngerSprite.png"
    image takehito  disappointconcerned  = "images/sprites/C_TakehitoDisappointedConcernedSprite.png"
    image takehito  disgusted  = "images/sprites/C_TakehitoDisgustedSprite.png"
    image takehito  embarassed  = "images/sprites/C_TakehitoEmbarassedSprite.png"
    image takehito  happy  = "images/sprites/C_TakehitoHappySprite.png"
    image takehito  normal  = "images/sprites/C_TakehitoNormalSprite.png"
    image takehito  shocked  = "images/sprites/C_TakehitoShockedSprite.png"
    image takehito  upset  = "images/sprites/C_TakehitoUpsetSprite.png"


    image umeko  normal  = "images/sprites/C_UmekoNormalSprite.png"
    image chibi umeko = "gui/dating_chibi.png"

    #TODO Movies
    image menu_movie = Movie(play="videos/menu.webm")