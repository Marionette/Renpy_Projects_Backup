init: # You can place the script of your game in this file.

  # Declare images below this line, using the image statement.
  # eg. image eileen happy = "eileen_happy.png"

  # Declare characters used by this game.
  define narrator = Character('',
                              what_prefix="{font=assets/texgyrecursor-r.otf}{size=25}",
                              what_suffix="{/font}{/size}",
                              who_prefix="{font=assets/mensch.ttf}{size=36}",
                              who_suffix="{/font}{/size}")
                              
  define e = Character('Eloise', 
                      color="#c8ffc8", 
                      what_prefix="{font=assets/texgyrecursor-r.otf}{size=25}",
                      what_suffix="{/font}{/size}",
                      who_prefix="{font=assets/mensch.ttf}{size=36}",
                      who_suffix="{/font}{/size}")
                      
  define f = Character('Finn', 
                      color="#c8ffc8", 
                      what_prefix="{font=assets/texgyrecursor-r.otf}{size=25}",
                      what_suffix="{/font}{/size}",
                      who_prefix="{font=assets/mensch.ttf}{size=36}",
                      who_suffix="{/font}{/size}")

  define a = Character('Tag', 
                      color="#c8ffc8", 
                      what_prefix="{font=assets/texgyrecursor-r.otf}{size=25}",
                      what_suffix="{/font}{/size}",
                      who_prefix="{font=assets/mensch.ttf}{size=36}",
                      who_suffix="{/font}{/size}")

  define m = Character('Mom', 
                      color="#c8ffc8", 
                      what_prefix="{font=assets/texgyrecursor-r.otf}{size=25}",
                      what_suffix="{/font}{/size}",
                      who_prefix="{font=assets/mensch.ttf}{size=36}",
                      who_suffix="{/font}{/size}")
                      
  define k = Character('Kelsey', 
                      color="#c8ffc8", 
                      what_prefix="{font=assets/texgyrecursor-r.otf}{size=25}",
                      what_suffix="{/font}{/size}",
                      who_prefix="{font=assets/mensch.ttf}{size=36}",
                      who_suffix="{/font}{/size}")
                      
  define w = Character('????', 
                      color="#c8ffc8", 
                      what_prefix="{font=assets/texgyrecursor-r.otf}{size=25}",
                      what_suffix="{/font}{/size}",
                      who_prefix="{font=assets/mensch.ttf}{size=36}",
                      who_suffix="{/font}{/size}")
                      
  define qq = Character('????', 
                      color="#c8ffc8", 
                      what_prefix="{font=assets/texgyrecursor-r.otf}{size=25}",
                      what_suffix="{/font}{/size}",
                      who_prefix="{font=assets/mensch.ttf}{size=36}",
                      who_suffix="{/font}{/size}")
                      
  # Declare character images used by this game.
  
  ######### ELOISE DEFINES #############
  image el neutral nj = LiveComposite(
    (317, 915),
    (0, 0), "img/sprite/eloise/el_body-lines.png",
    (0, 0), "img/sprite/eloise/el_jacket-off.png",
    (0, 0), "img/sprite/eloise/el_exp_neutral.png",
    (0, 0), "img/sprite/eloise/el_hair-pins.png")
    
  image el angry nj = LiveComposite(
    (317, 915),
    (0, 0), "img/sprite/eloise/el_body-lines.png",
    (0, 0), "img/sprite/eloise/el_jacket-off.png",
    (0, 0), "img/sprite/eloise/el_exp_angry.png",
    (0, 0), "img/sprite/eloise/el_hair-pins.png")
    
  image el sad nj = LiveComposite(
    (317, 915),
    (0, 0), "img/sprite/eloise/el_body-lines.png",
    (0, 0), "img/sprite/eloise/el_jacket-off.png",
    (0, 0), "img/sprite/eloise/el_exp_sad.png",
    (0, 0), "img/sprite/eloise/el_hair-pins.png")
    
  image el smiling nj = LiveComposite(
    (317, 915),
    (0, 0), "img/sprite/eloise/el_body-lines.png",
    (0, 0), "img/sprite/eloise/el_jacket-off.png",
    (0, 0), "img/sprite/eloise/el_exp_smiling.png",
    (0, 0), "img/sprite/eloise/el_hair-pins.png")
    
  image el surprised nj = LiveComposite(
    (317, 915),
    (0, 0), "img/sprite/eloise/el_body-lines.png",
    (0, 0), "img/sprite/eloise/el_jacket-off.png",
    (0, 0), "img/sprite/eloise/el_exp_surprised.png",
    (0, 0), "img/sprite/eloise/el_hair-pins.png")
    
  image el terrified nj = LiveComposite(
    (317, 915),
    (0, 0), "img/sprite/eloise/el_body-lines.png",
    (0, 0), "img/sprite/eloise/el_jacket-off.png",
    (0, 0), "img/sprite/eloise/el_exp_terrified.png",
    (0, 0), "img/sprite/eloise/el_hair-pins.png")
    
    #el with jacket
  image el neutral wj = LiveComposite(
    (317, 915),
    (0, 0), "img/sprite/eloise/el_body-lines.png",
    (0, 0), "img/sprite/eloise/el_jacket.png",
    (0, 0), "img/sprite/eloise/el_exp_neutral.png",
    (0, 0), "img/sprite/eloise/el_hair-pins.png")
    
  image el angry wj = LiveComposite(
    (317, 915),
    (0, 0), "img/sprite/eloise/el_body-lines.png",
    (0, 0), "img/sprite/eloise/el_jacket.png",
    (0, 0), "img/sprite/eloise/el_exp_angry.png",
    (0, 0), "img/sprite/eloise/el_hair-pins.png")
    
  image el sad wj = LiveComposite(
    (317, 915),
    (0, 0), "img/sprite/eloise/el_body-lines.png",
    (0, 0), "img/sprite/eloise/el_jacket.png",
    (0, 0), "img/sprite/eloise/el_exp_sad.png",
    (0, 0), "img/sprite/eloise/el_hair-pins.png")
    
  image el smiling wj = LiveComposite(
    (317, 915),
    (0, 0), "img/sprite/eloise/el_body-lines.png",
    (0, 0), "img/sprite/eloise/el_jacket.png",
    (0, 0), "img/sprite/eloise/el_exp_smiling.png",
    (0, 0), "img/sprite/eloise/el_hair-pins.png")
    
  image el surprised wj = LiveComposite(
    (317, 915),
    (0, 0), "img/sprite/eloise/el_body-lines.png",
    (0, 0), "img/sprite/eloise/el_jacket.png",
    (0, 0), "img/sprite/eloise/el_exp_surprised.png",
    (0, 0), "img/sprite/eloise/el_hair-pins.png")
    
  image el terrified wj = LiveComposite(
    (317, 915),
    (0, 0), "img/sprite/eloise/el_body-lines.png",
    (0, 0), "img/sprite/eloise/el_jacket.png",
    (0, 0), "img/sprite/eloise/el_exp_terrified.png",
    (0, 0), "img/sprite/eloise/el_hair-pins.png")
    
    
  ######### FINN DEFINES #############
  image fi default nj = LiveComposite(
    (386, 1064),
    (0, 0), "img/sprite/finn/fi_body.png",
    (0, 0), "img/sprite/finn/fi_jacket_off.png",
    (0, 0), "img/sprite/finn/fi_exp_default.png",
    (0, 0), "img/sprite/finn/fi_eye_sparkle.png")
    
  image fi angry nj = LiveComposite(
    (386, 1064),
    (0, 0), "img/sprite/finn/fi_body.png",
    (0, 0), "img/sprite/finn/fi_jacket_off.png",
    (0, 0), "img/sprite/finn/fi_exp_angry.png",
    (0, 0), "img/sprite/finn/fi_eye_sparkle.png")
    
  image fi apologetic nj = LiveComposite(
    (386, 1064),
    (0, 0), "img/sprite/finn/fi_body.png",
    (0, 0), "img/sprite/finn/fi_jacket_off.png",
    (0, 0), "img/sprite/finn/fi_exp_apologetic.png",
    (0, 0), "img/sprite/finn/fi_eye_sparkle.png")
    
  image fi crazy nj = LiveComposite(
    (386, 1064),
    (0, 0), "img/sprite/finn/fi_body.png",
    (0, 0), "img/sprite/finn/fi_jacket_off.png",
    (0, 0), "img/sprite/finn/fi_exp_crazy.png",
    (0, 0), "img/sprite/finn/fi_eye_sparkle.png")
    
  image fi nervous nj = LiveComposite(
    (386, 1064),
    (0, 0), "img/sprite/finn/fi_body.png",
    (0, 0), "img/sprite/finn/fi_jacket_off.png",
    (0, 0), "img/sprite/finn/fi_exp_nervous.png",
    (0, 0), "img/sprite/finn/fi_eye_sparkle.png")
    
  image fi sad nj = LiveComposite(
    (386, 1064),
    (0, 0), "img/sprite/finn/fi_body.png",
    (0, 0), "img/sprite/finn/fi_jacket_off.png",
    (0, 0), "img/sprite/finn/fi_exp_sad.png",
    (0, 0), "img/sprite/finn/fi_eye_sparkle.png")
    
  image fi serious nj = LiveComposite(
    (386, 1064),
    (0, 0), "img/sprite/finn/fi_body.png",
    (0, 0), "img/sprite/finn/fi_jacket_off.png",
    (0, 0), "img/sprite/finn/fi_exp_serious.png",
    (0, 0), "img/sprite/finn/fi_eye_sparkle.png")
    
  image fi smiling nj = LiveComposite(
    (386, 1064),
    (0, 0), "img/sprite/finn/fi_body.png",
    (0, 0), "img/sprite/finn/fi_jacket_off.png",
    (0, 0), "img/sprite/finn/fi_exp_smiling.png",
    (0, 0), "img/sprite/finn/fi_eye_sparkle.png")
    
  image fi surprised nj = LiveComposite(
    (386, 1064),
    (0, 0), "img/sprite/finn/fi_body.png",
    (0, 0), "img/sprite/finn/fi_jacket_off.png",
    (0, 0), "img/sprite/finn/fi_exp_surprised.png",
    (0, 0), "img/sprite/finn/fi_eye_sparkle.png")
    
    #fi with jacket
  image fi default wj = LiveComposite(
    (386, 1064),
    (0, 0), "img/sprite/finn/fi_body.png",
    (0, 0), "img/sprite/finn/fi_jacket.png",
    (0, 0), "img/sprite/finn/fi_exp_default.png",
    (0, 0), "img/sprite/finn/fi_eye_sparkle.png")
    
  image fi angry wj = LiveComposite(
    (386, 1064),
    (0, 0), "img/sprite/finn/fi_body.png",
    (0, 0), "img/sprite/finn/fi_jacket.png",
    (0, 0), "img/sprite/finn/fi_exp_angry.png",
    (0, 0), "img/sprite/finn/fi_eye_sparkle.png")
    
  image fi apologetic wj = LiveComposite(
    (386, 1064),
    (0, 0), "img/sprite/finn/fi_body.png",
    (0, 0), "img/sprite/finn/fi_jacket.png",
    (0, 0), "img/sprite/finn/fi_exp_apologetic.png",
    (0, 0), "img/sprite/finn/fi_eye_sparkle.png")
    
  image fi crazy wj = LiveComposite(
    (386, 1064),
    (0, 0), "img/sprite/finn/fi_body.png",
    (0, 0), "img/sprite/finn/fi_jacket.png",
    (0, 0), "img/sprite/finn/fi_exp_crazy.png",
    (0, 0), "img/sprite/finn/fi_eye_sparkle.png")
    
  image fi nervous wj = LiveComposite(
    (386, 1064),
    (0, 0), "img/sprite/finn/fi_body.png",
    (0, 0), "img/sprite/finn/fi_jacket.png",
    (0, 0), "img/sprite/finn/fi_exp_nervous.png",
    (0, 0), "img/sprite/finn/fi_eye_sparkle.png")
    
  image fi sad wj = LiveComposite(
    (386, 1064),
    (0, 0), "img/sprite/finn/fi_body.png",
    (0, 0), "img/sprite/finn/fi_jacket.png",
    (0, 0), "img/sprite/finn/fi_exp_sad.png",
    (0, 0), "img/sprite/finn/fi_eye_sparkle.png")
    
  image fi serious wj = LiveComposite(
    (386, 1064),
    (0, 0), "img/sprite/finn/fi_body.png",
    (0, 0), "img/sprite/finn/fi_jacket.png",
    (0, 0), "img/sprite/finn/fi_exp_serious.png",
    (0, 0), "img/sprite/finn/fi_eye_sparkle.png")
    
  image fi smiling wj = LiveComposite(
    (386, 1064),
    (0, 0), "img/sprite/finn/fi_body.png",
    (0, 0), "img/sprite/finn/fi_jacket.png",
    (0, 0), "img/sprite/finn/fi_exp_smiling.png",
    (0, 0), "img/sprite/finn/fi_eye_sparkle.png")
    
  image fi surprised wj = LiveComposite(
    (386, 1064),
    (0, 0), "img/sprite/finn/fi_body.png",
    (0, 0), "img/sprite/finn/fi_jacket.png",
    (0, 0), "img/sprite/finn/fi_exp_surprised.png",
    (0, 0), "img/sprite/finn/fi_eye_sparkle.png")
    
  image fi surprised wj anim = LiveComposite(
    (386, 1064),
    (0, 0), "img/sprite/finn/fi_body.png",
    (0, 0), "img/sprite/finn/fi_jacket.png",
    (0, 0),  Animation("img/sprite/finn/fi_exp_surprised.png", 4,"img/sprite/finn/fi_exp_smiling.png", 0.2),
    (0, 0), "img/sprite/finn/fi_eye_sparkle.png")
    
  
  # Declare bg images used by this game.
  image bg black = Solid("#000000")
  image bg attic = "img/bg/PicsArt_1428883323584.png"
  image bg bedroom = "img/bg/PicsArt_1428883349733.png"
  image bg dining = "img/bg/PicsArt_1428883425451.png"
  image bg kitchen = "img/bg/PicsArt_1428883248480.png"
  image bg living = "img/bg/PicsArt_1428883175419.png"
  image bg sky aurora = "img/bg/PicsArt_1428883373503.png"
  image bg sky blue = "img/bg/PicsArt_1428883397284.png"
  image bg sky clouds = "img/bg/PicsArt_1428883108038.png"
  image bg sky clouds2 = "img/bg/PicsArt_1428883277536.png"
  image bg sky night = "img/bg/PicsArt_1428883069114.png"
  
  
  
  # Declare cg images used by this game.
  

  ######### ATL DEFINES #############
  transform leftE:
      xalign 0.1
      yalign -0.65
  transform rightE:
      xalign 0.9
      yalign -0.65
  
  transform rightF:
      xalign 0.9
      yalign -0.1  

  transform leftF:
      xalign 0.1
      yalign -0.1
  
  
    
    ######### SOUND DEFINES #############
    
    #$music_believe = "audio/music/New Beginnings.ogg"
    #$music_closeto = "audio/music/Piano.ogg"
    #$music_crying = "audio/music/Potent Happiness.ogg"
    #$music_prisoner = "audio/music/Romance.ogg"
    #$music_rains = "audio/music/Society of Trees (Short).ogg"
    #$music_suspicious = "audio/music/Society of Trees.ogg"
    #$music_sympathy = "audio/music/Ambient Sound.ogg"
    #
    ##TODO
    #$music_eerie = "audio/music/Merona's Theme.ogg"
    #$music_recollections = "audio/music/Merona's Theme.ogg"
    #$music_life = "audio/music/Merona's Theme.ogg"
    #
    #
    #$sound_birds = "audio/sound/djhalleu__stavanger-nightingale1.ogg"
    #$sound_cukoo = "audio/sound/inchadney__cuckoo_short.ogg"
    #$sound_bell = "kaonaya__bell-at-daitokuji-temple-kyoto.ogg"
    #$sound_snarl = "audio/sound/Monster Snarling.ogg"
    #$sound_ambiance = "audio/sound/Nature Ambiance.ogg"
    #$sound_cricket = "audio/sound/weldonsmith__cricket2dopecho.ogg"
    #
    ##TODO
    #$sound_footsteps = "audio/sound/weldonsmith__cricket2dopecho.ogg"
    #$sound_knock = "audio/sound/weldonsmith__cricket2dopecho.ogg"
    #$sound_breatheOut = "audio/sound/weldonsmith__cricket2dopecho.ogg"
    #$sound_fallInDirt = "audio/sound/weldonsmith__cricket2dopecho.ogg"
    