init:
  ###### POSITION DEFINES ############
  transform left:
    yalign 1.0 xanchor .5 xalign 0.5
    
  #transform right:
  #  yalign 1.0 xanchor .5 xalign 0.75

  ######### MISC DEFINES #############
  define slow_dissolve = Dissolve(2.0)
  
  default malice_level = 0
  default heart_item = False
  default heart_show = False
  default intoxication = False
  
  
  ######### CHARACTER DEFINES #############
  define Clubs = Character("Clubs")
  define Diamonds = Character("Diamonds")
  define Spades = Character("Spades")

  ######### SOUND DEFINES #############
  #-- MUSIC ---  
  #TODO Music
  $music_bar        = "audio/music/music_bar.mp3"
  $music_ending     = "audio/music/music_ending.mp3"
  $music_nightmare  = "audio/music/music_nightmare.mp3"
  $music_reveal     = "audio/music/music_reveal.mp3"
  $music_roulette   = "audio/music/music_roulette.mp3"
  $music_slots      = "audio/music/music_slots.mp3"
  #-- SFX ---  
  
  ######### CG/BG IMAGE DEFINES #############
  
  #Backgrounds   
  image black = Solid("#000000")  
  image bg black = Solid("#000000")     
  image bg white = Solid("#ffffff")
  
  #TODO REPLACE #BGs
  image bg bg_bar              = "images/bg/bg_bar.png"
  image bg bg_darkness         = Solid("#000000") 
  image bg bg_roulette         = "images/bg/bg_roulette.png"
  image bg bg_roulette_creepy  = "images/bg/bg_roulette_creepy.png"
  image bg bg_roulette_missing = "images/bg/bg_roulette_missing.png"
  image bg bg_slots            = "images/bg/bg_slots.png"
  
  #TODO REPLACE #CGs
  image cg cg_ending01         = "images/cg/cg_ending01.jpg"    
  image cg cg_ending02         = "images/cg/cg_ending02.jpg"    
  image cg cg_ending03         = "images/cg/cg_ending03.jpg"    
  image cg cg_ending04         = "images/cg/cg_ending04.jpg"    
  image cg cg_ending05         = "images/cg/cg_ending05.jpg"    
  image cg cg_ending06         = "images/cg/cg_ending06.jpg"     
                                            
  image cg cg_hands            = "images/cg/cg_hands.png"        
  image cg cg_hands_bloody     = "images/cg/cg_hands_bloody.png"
  image cg cg_hands_creepy     = "images/cg/cg_hands_creepy.png" 
  image cg cg_nightmare        = "images/cg/cg_nightmare.png"    
  image cg cg_suits            = "images/cg/cg_suits.png"        
  
  #TODO REPLACE #Characters    
  
  image clubs anxious    = "images/sprites/clubs_anxious.png"
  image clubs default    = "images/sprites/clubs_default.png"
  image clubs mad        = "images/sprites/clubs_mad.png"
  image clubs sad        = "images/sprites/clubs_sad.png"
  image clubs shock      = "images/sprites/clubs_shock.png"
  image clubs smile      = "images/sprites/clubs_smile.png"
  
  image diamonds anxious = "images/sprites/diamonds_anxious.png"
  image diamonds default = "images/sprites/diamonds_default.png"
  image diamonds mad     = "images/sprites/diamonds_mad.png"
  image diamonds sad     = "images/sprites/diamonds_sad.png"
  image diamonds shock   = "images/sprites/diamonds_shock.png"
  image diamonds smirk   = "images/sprites/diamonds_smirk.png"
  
  image spades anxious   = "images/sprites/spades_anxious.png"
  image spades creepy    = "images/sprites/spades_creepy.png"
  image spades cry       = "images/sprites/spades_crying.png"
  image spades default   = "images/sprites/spades_default.png"
  image spades mad       = "images/sprites/spades_mad.png"
  image spades shock     = "images/sprites/spades_shock.png"
  image spades smirk     = "images/sprites/spades_smirk.png"
  
  
  
  