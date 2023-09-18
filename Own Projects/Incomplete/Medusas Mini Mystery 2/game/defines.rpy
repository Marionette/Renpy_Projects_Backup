init:
    
    ###### POSITION DEFINES ############
    #transform left:
    #  yalign 1.0 xanchor .5 xalign 0.25
      
    #transform right:
    #  yalign 1.0 xanchor .5 xalign 0.75
    
    transform rotateButton(_rotate=0):
      rotate _rotate
        
    transform show_snake(_y=1.0, _x=1.0, _zoom=1.0, _time=1.0):
      #crop(00,00,1920, 1080)
      #parallel:#        
      #  linear _time crop(800,400,200, 200)
      parallel:
        linear _time yalign _y
      parallel:
        linear _time xalign _x
      parallel:
        linear _time zoom _zoom
        
    transform PositionBg(_zoom=1.0, _xpan=1.0, _ypan=1.0, _time=1.0):
      parallel:
        linear _time zoom _zoom
      parallel:
        linear _time xpan _xpan
      parallel:
        linear _time ypan _ypan
      
      #linear 36 xpan 360
      #xpan 0
      #repeat
        
    transform PositionBgInstant(_zoom=1.0, _xpan=1.0, _ypan=1.0):
      zoom _zoom
      xpan _xpan
      ypan _ypan
    
    transform show_medusa_instant():
      xalign 0.5
      yalign 1.0
      zoom 0.3
    
    transform show_medusa_head_instant():
      xalign 0.5
      yalign 0.1
      zoom 0.5
    transform show_medusa_head():
      show_snake(0.1, 0.5, 1.5, 1.0)
      #xalign 0.5
      #parallel:
      #  linear 0.8 yalign 0.1
      #parallel:
      #  linear 0.8 zoom 0.5
    
    transform show_medusa_head_nod():
      show_medusa_head()
      linear 0.3 yalign 0.2
      linear 0.3 yalign 0.1
      linear 0.3 yalign 0.2
      linear 0.3 yalign 0.1
    
    transform show_medusa():
      xalign 0.5
      parallel:
        linear 1.0 yalign 1.0
      parallel:
        linear 1.0 zoom 1.0
    
    transform show_medusa_close():
      xalign 0.5
      parallel:
        linear 1.0 yalign 0.2
      parallel:
        linear 1.0 zoom 0.4
    
    transform show_medusa_closer():
      xalign 0.5
      parallel:
        linear 1.0 yalign 0.3
      parallel:
        linear 1.0 zoom 0.5
      
    
    transform show_side_medusa_instant():
      crop (550,100,820, 680)
      xalign 0.0
      yalign 1.0
      zoom 1.0
      
    transform show_snake1():
      show_snake(0.5, 0.45, 3.0, 1.0)
    
    transform show_snake2():
      show_snake(0.5, 0.3, 3.0, 1.0)
    
    transform show_snake3():
      show_snake(0.10, 0.70, 3.0, 1.0)
    
    transform show_snake4():
      show_snake(0.3, 0.3, 3.0, 1.0)
    
    transform show_snake5():
      show_snake(0.5, 0.75, 3.0, 1.0)
    
    transform show_snake6():
      show_snake(0.40, 0.70, 3.0, 1.0)
      
    transform show_donut:
      show_snake(0.9, 0.6, 4.0, 1.0)
      
      
    
    transform show_side_snake1():
      crop (550,100,820, 680)
      #crop(00,00,1920, 1080)
      #parallel:#        
      #  show_snake(0.52, 0.45, 3.0, 1.0)
      #parallel:
      #  linear 1.0 yalign 0.52
      #parallel:
      #  linear 1.0 xalign 0.45
      parallel:
        linear 1.0 crop(750,450,200, 200)
      parallel:
        linear 1.0 zoom 3.0
    
    transform show_side_snake2():
      crop(00,00,1920, 1080)
      parallel:#        
        linear 1.0 crop(800,400,200, 200)
      show_snake(0.5, 0.3, 3.0, 1.0)
    
    transform show_side_snake3():
      crop(00,00,1920, 1080)
      parallel:#        
        linear 1.0 crop(800,400,200, 200)
      show_snake(0.10, 0.70, 3.0, 1.0)
    
    transform show_side_snake4():
      crop(00,00,1920, 1080)
      parallel:#        
        linear 1.0 crop(800,400,200, 200)
      show_snake(0.3, 0.3, 3.0, 1.0)
    
    transform show_side_snake5():
      crop(00,00,1920, 1080)
      parallel:#        
        linear 1.0 crop(800,400,200, 200)
      show_snake(0.5, 0.75, 3.0, 1.0)
    
    transform show_side_snake6():
      crop(00,00,1920, 1080)
      parallel:#        
        linear 1.0 crop(800,400,200, 200)
      show_snake(0.40, 0.70, 3.0, 1.0)
      
    transform show_side_donut:
      show_snake(0.9, 0.6, 4.0, 1.0)
    
    ######### MISC DEFINES #############
    define slow_dissolve = Dissolve(2.0)
                        
    # Declare characters used by this game. The color argument colorizes the
    # name of the character.
    define Agnesss_name      = "Agnesss"
    define Beatrisss_name    = "Beatrisss" 
    define Casssie_name      = "Casssie"
    define Daisssy_name      = "Daisssy"
    define Elissse_name      = "Elissse"
    define Francesssca_name  = "Francesssca"
    define Any_name  = "Anyone"
    
    #variables
    default selected_item = ""
    default potion_philstone_found = False
    default potion_philstone = False
    
    default ingredient_list = []

    ######### CHARACTER DEFINES #############Characters:
    #Medusa - Melissa
    define m = Character("Melissa", image="medusa")
    #Snake 1 - Agnesss
    define a = DynamicCharacter("Agnesss_name", image="medusa")
    #Snake 2 - Beatrisss
    define b = DynamicCharacter("Beatrisss_name", image="medusa")
    #Snake 3 - Casssie
    define c = DynamicCharacter("Casssie_name", image="medusa")
    #Snake 4 - Daisssy
    define d = DynamicCharacter("Daisssy_name", image="medusa")
    #Snake 5 - Elissse
    define e = DynamicCharacter("Elissse_name", image="medusa")
    #Snake 6 - Francesssca
    define f = DynamicCharacter("Francesssca_name", image="medusa")
    
   
    define named = DynamicCharacter("Any_name")
    
    define everyone = Character("All")
    define minotaur = Character("Minotaur")
    define cb = Character("Voice")
    
  
    ######### SOUND DEFINES #############
    #$bgm = "audio/music/bgm.mp3"
    
    #define audio.music_all = "<loop 5.130>audio/I36.ogg"
    #define audio.music_all_noKick = "<from 5.130>audio/I36.ogg"
    #define audio.music_kick = "<to 5.130>audio/I36.ogg"
    #define audio.music_mystery = "<from 5.930 to 33.135>audio/I36.ogg"
    #define audio.music_interrogation = "<from 33.135 to 60.387>audio/I36.ogg"
    
    ######### CG/BG IMAGE DEFINES #############
    image black = Solid("#000000")  
    image bg black = Solid("#101012") #almost black
    image bg white = Solid("#ffffff")
    
    #Backgrounds 
    #image bg kitchen = Composite((1920, 1080), (0, 0), "images/bg_kitchen.png", (0, 0),"images/item_donut.png")
    #image bg kitchen nodonut = "images/bg_kitchen.png"
    
    #CG images
    
    image medusa = im.Crop("images/Medusa3.png",(550,0,820, 1080))
    #image side_medusa = im.Crop("images/Medusa3.png",(570,100,820, 580))
    image side_medusa = "images/Medusa3.png"