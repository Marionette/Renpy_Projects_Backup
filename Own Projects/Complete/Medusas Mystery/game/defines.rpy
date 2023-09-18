init:
    
    ###### POSITION DEFINES ############
    #transform left:
    #  yalign 1.0 xanchor .5 xalign 0.25
      
    #transform right:
    #  yalign 1.0 xanchor .5 xalign 0.75
        
    transform show_snake(_y=1.0, _x=1.0, _zoom=1.0, _time=1.0):
      parallel:
        linear _time yalign _y
      parallel:
        linear _time xalign _x
      parallel:
        linear _time zoom _zoom
    
    transform show_medusa_instant():
      xalign 0.5
      yalign 1.0
      zoom 0.3
    
    transform show_medusa_head_instant():
      xalign 0.5
      yalign 0.1
      zoom 0.5
    transform show_medusa_head():
      show_snake(0.1, 0.5, 0.5, 1.0)
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
        linear 1.0 zoom 0.3
    
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
      
    
    transform show_snake1():
      show_snake(0.5, 0.1, 1.0, 1.0)
    
    transform show_snake2():
      show_snake(0.1, 0.3, 1.0, 1.0)
    
    transform show_snake3():
      show_snake(0.2, 0.75, 1.0, 1.0)
    
    transform show_snake4():
      show_snake(0.0, 0.45, 1.0, 1.0)
    
    transform show_snake5():
      show_snake(0.7, 0.8, 1.0, 1.0)
    
    transform show_snake6():
      show_snake(0.4, 0.95, 1.0, 1.0)
      
    transform show_donut:
      show_snake(0.9, 0.6, 4.0, 1.0)
    
    ######### MISC DEFINES #############
    define slow_dissolve = Dissolve(2.0)
    
    define persistent.donut_spelling = "donut"
    
    define ending = 0
    define crumbsFound = False
    define sandwichEatingSeen = False
    define haveInvestigated = False
    define haveInterrogated = False
                        
    # Declare characters used by this game. The color argument colorizes the
    # name of the character.
    define Agnesss_name      = "Agnesss"
    define Beatrisss_name    = "Beatrisss" 
    define Casssie_name      = "Casssie"
    define Daisssy_name      = "Daisssy"
    define Elissse_name      = "Elissse"
    define Francesssca_name  = "Francesssca"
    define Any_name  = "Anyone"

    ######### CHARACTER DEFINES #############Characters:
    #Medusa - Melissa
    define m = Character("Melissa")
    #Snake 1 - Agnesss
    define a = DynamicCharacter("Agnesss_name")
    #Snake 2 - Beatrisss
    define b = DynamicCharacter("Beatrisss_name")
    #Snake 3 - Casssie
    define c = DynamicCharacter("Casssie_name")
    #Snake 4 - Daisssy
    define d = DynamicCharacter("Daisssy_name")
    #Snake 5 - Elissse
    define e = DynamicCharacter("Elissse_name")
    #Snake 6 - Francesssca
    define f = DynamicCharacter("Francesssca_name")
    
   
    define named = DynamicCharacter("Any_name")
    
    define everyone = Character("All")
  
    ######### SOUND DEFINES #############
    #$bgm = "audio/music/bgm.mp3"
    
    define audio.music_all = "<loop 5.130>audio/I36.ogg"
    define audio.music_all_noKick = "<from 5.130>audio/I36.ogg"
    define audio.music_kick = "<to 5.130>audio/I36.ogg"
    define audio.music_mystery = "<from 5.930 to 33.135>audio/I36.ogg"
    define audio.music_interrogation = "<from 33.135 to 60.387>audio/I36.ogg"
    
    ######### CG/BG IMAGE DEFINES #############
    image black = Solid("#000000")  
    image bg black = Solid("#101012") #almost black
    image bg white = Solid("#ffffff")
    
    #Backgrounds 
    image bg kitchen = Composite((1920, 1080), (0, 0), "images/bg_kitchen.png", (0, 0),"images/item_donut.png")
    image bg kitchen nodonut = "images/bg_kitchen.png"
    
    #CG images
    
    #image medusa = "images/Medusa.png"
    image medusa = Composite((5760, 3240), (0, 0), "images/Medusa_exp_base.png", (0, 0),"images/Medusa_exp_neutral.png")
    image medusa mad = Composite((5760, 3240), (0, 0), "images/Medusa_exp_base.png", (0, 0),"images/Medusa_exp_mad.png")
    
    image medusa default = "images/Medusa.png"
    image medusa anxious = "images/Medusa.png"
    image medusa blush = "images/Medusa.png"
    image medusa laugh = "images/Medusa.png"
    image medusa sad = "images/Medusa_sad.png"
    image medusa shock = "images/Medusa.png"
    image medusa smile = "images/Medusa.png"
    
    #---------------- Agness expresssions      -----------   
    
    image medusa aglass = Composite((5760, 3240), (0, 0), "images/Medusa_exp_base.png", 
    #(0, 0),"images/Medusa_exp_neutral.png", 
    (1214,1024), im.Crop("images/Medusa_exp_misc1.png", 1214,1024,527,496), #Agnesss
    (1714,528), im.Crop("images/Medusa_exp_neutral.png", 1714,528,717,496), #Beatrisss    
    (3615,528), im.Crop("images/Medusa_exp_neutral.png", 3615,528,664,496), #Casssie
    (2458,0000), im.Crop("images/Medusa_exp_neutral.png", 2458,0000,807,528), #Daisssy
    (3815,1845), im.Crop("images/Medusa_exp_neutral.png", 3815,1845,664,496), #Elissse
    (4015,1024), im.Crop("images/Medusa_exp_neutral.png", 4015,1024,664,596), #Francesssca
    (2570,855), im.Crop("images/Medusa_exp_neutral.png", 2570,855,1140,1181)  #Medusa
    ) 
    
    image medusa aexasp = Composite((5760, 3240), (0, 0), "images/Medusa_exp_base.png", 
    #(0, 0),"images/Medusa_exp_neutral.png", 
    (1214,1024), im.Crop("images/Medusa_exp_mad.png", 1214,1024,527,496), #Agnesss
    (1714,528), im.Crop("images/Medusa_exp_neutral.png", 1714,528,717,496), #Beatrisss    
    (3615,528), im.Crop("images/Medusa_exp_neutral.png", 3615,528,664,496), #Casssie
    (2458,0000), im.Crop("images/Medusa_exp_neutral.png", 2458,0000,807,528), #Daisssy
    (3815,1845), im.Crop("images/Medusa_exp_neutral.png", 3815,1845,664,496), #Elissse
    (4015,1024), im.Crop("images/Medusa_exp_neutral.png", 4015,1024,664,596), #Francesssca
    (2570,855), im.Crop("images/Medusa_exp_neutral.png", 2570,855,1140,1181)  #Medusa
    ) 
    #---------------- Beatrisss expresssions   -----------
    
    image medusa bsad = Composite((5760, 3240), (0, 0), "images/Medusa_exp_base.png", 
    #(0, 0),"images/Medusa_exp_neutral.png", 
    (1214,1024), im.Crop("images/Medusa_exp_neutral.png", 1214,1024,527,496), #Agnesss
    (1714,528), im.Crop("images/Medusa_exp_misc1.png", 1714,528,717,496), #Beatrisss    
    (3615,528), im.Crop("images/Medusa_exp_neutral.png", 3615,528,664,496), #Casssie
    (2458,0000), im.Crop("images/Medusa_exp_neutral.png", 2458,0000,807,528), #Daisssy
    (3815,1845), im.Crop("images/Medusa_exp_neutral.png", 3815,1845,664,496), #Elissse
    (4015,1024), im.Crop("images/Medusa_exp_neutral.png", 4015,1024,664,596), #Francesssca
    (2570,855), im.Crop("images/Medusa_exp_neutral.png", 2570,855,1140,1181)  #Medusa
    )
    
    image medusa bscared = Composite((5760, 3240), (0, 0), "images/Medusa_exp_base.png", 
    #(0, 0),"images/Medusa_exp_neutral.png", 
    (1214,1024), im.Crop("images/Medusa_exp_neutral.png", 1214,1024,527,496), #Agnesss
    (1714,528), im.Crop("images/Medusa_exp_mad.png", 1714,528,717,496), #Beatrisss    
    (3615,528), im.Crop("images/Medusa_exp_neutral.png", 3615,528,664,496), #Casssie
    (2458,0000), im.Crop("images/Medusa_exp_neutral.png", 2458,0000,807,528), #Daisssy
    (3815,1845), im.Crop("images/Medusa_exp_neutral.png", 3815,1845,664,496), #Elissse
    (4015,1024), im.Crop("images/Medusa_exp_neutral.png", 4015,1024,664,596), #Francesssca
    (2570,855), im.Crop("images/Medusa_exp_neutral.png", 2570,855,1140,1181)  #Medusa
    )
    #---------------- Casssie expresssions     -----------
    
    image medusa chappytears = Composite((5760, 3240), (0, 0), "images/Medusa_exp_base.png", 
    #(0, 0),"images/Medusa_exp_neutral.png", 
    (1214,1024), im.Crop("images/Medusa_exp_neutral.png", 1214,1024,527,496), #Agnesss
    (1714,528), im.Crop("images/Medusa_exp_neutral.png", 1714,528,717,496), #Beatrisss    
    (3615,528), im.Crop("images/Medusa_exp_misc1.png", 3615,528,664,496), #Casssie
    (2458,0000), im.Crop("images/Medusa_exp_neutral.png", 2458,0000,807,528), #Daisssy
    (3815,1845), im.Crop("images/Medusa_exp_neutral.png", 3815,1845,664,496), #Elissse
    (4015,1024), im.Crop("images/Medusa_exp_neutral.png", 4015,1024,664,596), #Francesssca
    (2570,855), im.Crop("images/Medusa_exp_neutral.png", 2570,855,1140,1181)  #Medusa
    )
    
    image medusa csus = Composite((5760, 3240), (0, 0), "images/Medusa_exp_base.png", 
    #(0, 0),"images/Medusa_exp_neutral.png", 
    (1214,1024), im.Crop("images/Medusa_exp_neutral.png", 1214,1024,527,496), #Agnesss
    (1714,528), im.Crop("images/Medusa_exp_neutral.png", 1714,528,717,496), #Beatrisss    
    (3615,528), im.Crop("images/Medusa_exp_mad.png", 3615,528,664,496), #Casssie
    (2458,0000), im.Crop("images/Medusa_exp_neutral.png", 2458,0000,807,528), #Daisssy
    (3815,1845), im.Crop("images/Medusa_exp_neutral.png", 3815,1845,664,496), #Elissse
    (4015,1024), im.Crop("images/Medusa_exp_neutral.png", 4015,1024,664,596), #Francesssca
    (2570,855), im.Crop("images/Medusa_exp_neutral.png", 2570,855,1140,1181)  #Medusa
    )
    #---------------- Daisssy expresssions     -----------
    
    image medusa dwink = Composite((5760, 3240), (0, 0), "images/Medusa_exp_base.png", 
    #(0, 0),"images/Medusa_exp_neutral.png", 
    (1214,1024), im.Crop("images/Medusa_exp_neutral.png", 1214,1024,527,496), #Agnesss
    (1714,528), im.Crop("images/Medusa_exp_neutral.png", 1714,528,717,496), #Beatrisss    
    (3615,528), im.Crop("images/Medusa_exp_neutral.png", 3615,528,664,496), #Casssie
    (2458,0000), im.Crop("images/Medusa_exp_misc1.png", 2458,0000,807,528), #Daisssy
    (3815,1845), im.Crop("images/Medusa_exp_neutral.png", 3815,1845,664,496), #Elissse
    (4015,1024), im.Crop("images/Medusa_exp_neutral.png", 4015,1024,664,596), #Francesssca
    (2570,855), im.Crop("images/Medusa_exp_neutral.png", 2570,855,1140,1181)  #Medusa
    )
    
    image medusa mad dwink = Composite((5760, 3240), (0, 0), "images/Medusa_exp_base.png", 
    #(0, 0),"images/Medusa_exp_neutral.png", 
    (1214,1024), im.Crop("images/Medusa_exp_mad.png", 1214,1024,527,496), #Agnesss
    (1714,528), im.Crop("images/Medusa_exp_mad.png", 1714,528,717,496), #Beatrisss    
    (3615,528), im.Crop("images/Medusa_exp_mad.png", 3615,528,664,496), #Casssie
    (2458,0000), im.Crop("images/Medusa_exp_misc1.png", 2458,0000,807,528), #Daisssy
    (3815,1845), im.Crop("images/Medusa_exp_mad.png", 3815,1845,664,496), #Elissse
    (4015,1024), im.Crop("images/Medusa_exp_mad.png", 4015,1024,664,596), #Francesssca
    (2570,855), im.Crop("images/Medusa_exp_mad.png", 2570,855,1140,1181)  #Medusa
    )
    #---------------- Elissse expresssions     -----------
    
    image medusa esrs = Composite((5760, 3240), (0, 0), "images/Medusa_exp_base.png", 
    #(0, 0),"images/Medusa_exp_neutral.png", 
    (1214,1024), im.Crop("images/Medusa_exp_neutral.png", 1214,1024,527,496), #Agnesss
    (1714,528), im.Crop("images/Medusa_exp_neutral.png", 1714,528,717,496), #Beatrisss    
    (3615,528), im.Crop("images/Medusa_exp_neutral.png", 3615,528,664,496), #Casssie
    (2458,0000), im.Crop("images/Medusa_exp_neutral.png", 2458,0000,807,528), #Daisssy
    (3815,1845), im.Crop("images/Medusa_exp_misc1.png", 3815,1845,664,496), #Elissse
    (4015,1024), im.Crop("images/Medusa_exp_neutral.png", 4015,1024,664,596), #Francesssca
    (2570,855), im.Crop("images/Medusa_exp_neutral.png", 2570,855,1140,1181)  #Medusa
    )
    
    image medusa escared = Composite((5760, 3240), (0, 0), "images/Medusa_exp_base.png", 
    #(0, 0),"images/Medusa_exp_neutral.png", 
    (1214,1024), im.Crop("images/Medusa_exp_neutral.png", 1214,1024,527,496), #Agnesss
    (1714,528), im.Crop("images/Medusa_exp_neutral.png", 1714,528,717,496), #Beatrisss    
    (3615,528), im.Crop("images/Medusa_exp_neutral.png", 3615,528,664,496), #Casssie
    (2458,0000), im.Crop("images/Medusa_exp_neutral.png", 2458,0000,807,528), #Daisssy
    (3815,1845), im.Crop("images/Medusa_exp_mad.png", 3815,1845,664,496), #Elissse
    (4015,1024), im.Crop("images/Medusa_exp_neutral.png", 4015,1024,664,596), #Francesssca
    (2570,855), im.Crop("images/Medusa_exp_neutral.png", 2570,855,1140,1181)  #Medusa
    )
    
    #---------------- Francesssca expresssions -----------
    
    image medusa fsarcastic = Composite((5760, 3240), (0, 0), "images/Medusa_exp_base.png", 
    #(0, 0),"images/Medusa_exp_neutral.png", 
    (1214,1024), im.Crop("images/Medusa_exp_neutral.png", 1214,1024,527,496), #Agnesss
    (1714,528), im.Crop("images/Medusa_exp_neutral.png", 1714,528,717,496), #Beatrisss    
    (3615,528), im.Crop("images/Medusa_exp_neutral.png", 3615,528,664,496), #Casssie
    (2458,0000), im.Crop("images/Medusa_exp_neutral.png", 2458,0000,807,528), #Daisssy
    (3815,1845), im.Crop("images/Medusa_exp_neutral.png", 3815,1845,664,496), #Elissse
    (4015,1024), im.Crop("images/Medusa_exp_misc1.png", 4015,1024,664,596), #Francesssca
    (2570,855), im.Crop("images/Medusa_exp_neutral.png", 2570,855,1140,1181)  #Medusa
    )
    
    image medusa fworried = Composite((5760, 3240), (0, 0), "images/Medusa_exp_base.png", 
    #(0, 0),"images/Medusa_exp_neutral.png", 
    (1214,1024), im.Crop("images/Medusa_exp_neutral.png", 1214,1024,527,496), #Agnesss
    (1714,528), im.Crop("images/Medusa_exp_neutral.png", 1714,528,717,496), #Beatrisss    
    (3615,528), im.Crop("images/Medusa_exp_neutral.png", 3615,528,664,496), #Casssie
    (2458,0000), im.Crop("images/Medusa_exp_neutral.png", 2458,0000,807,528), #Daisssy
    (3815,1845), im.Crop("images/Medusa_exp_neutral.png", 3815,1845,664,496), #Elissse
    (4015,1024), im.Crop("images/Medusa_exp_mad.png", 4015,1024,664,596), #Francesssca
    (2570,855), im.Crop("images/Medusa_exp_neutral.png", 2570,855,1140,1181)  #Medusa
    )
    
    
    #TODO Serious ,  FrancessscaElise
    
    
    #Agnesss = suspicious confused 
    #Beatrisss = Serious sad
    #Casssie = suspicious angry happy
    #Daisssy = Happy, confused
    #Elissse = Serious
    #Francesssca = Disappointed, Sarcastic