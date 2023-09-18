init:
  ###### POSITION DEFINES ############
  transform left:
    yalign 1.0 xanchor .5 xalign 0.05

  #transform right:
  #  yalign 1.0 xanchor .5 xalign 0.75

  ###### TRANSFORMS DEFINES ############
  define fade = Fade(0.5, 0.0, 0.5)
  define fadeblack = Fade(0.5, 1.0, 0.5, color="#000")
  define slow_dissolve = Dissolve(2.0)
  ######### MISC DEFINES #############
  define config.adv_nvl_transition = None
  define config.nvl_adv_transition = Dissolve(0.3)

  define persistent.hide_feedback = False
  default current_day = 0
  default current_time = "Morning"
  default current_difficulty = "Normal"
  default use_day = False
  default use_time = False
  default use_difficulty = False
  #Class tracking list
  default List_classes_taught = []
  
  define small_increase = 5
  define large_increase = 10
  
  define max_multiplier = 2
  define high_multiplier = 1.5
  define std_multiplier = 1
  define low_multiplier = 1
  define min_multiplier = 0
  
  define btb_length = 1
  define btb_multiplier = 0.5
  
  define degradation_length = 5
  define degradation_pointsLost = 1

  ######### MISC UI DEFINES #############

  default feature_unlock_roster = False
  default feature_unlock_status_self = False
  default feature_unlock_status_others = False
  default feature_unlock_calendar = False

  #Unlock if implemented
  default feature_unlock_penalty_backToBack = True
  default feature_unlock_penalty_ScoreDegradation = True
  default feature_unlock_bonus_Mood = True
  default feature_unlock_bonus_favourites = False
  default feature_unlock_penalty_stress = True

  define List_weather = ["Clear", "Cloudy", "Rain", "Sunny", "Foggy"]

  #Used for UI Flavor text
  default current_time_hour = "10"
  default current_weather = "Cloudy"
  default current_temp = "20"

  #used to show calandar dates
  default display_date = 1

  define List_calander_events=[
  "",
  "First Day of Teaching!\nSpend the day introducing ourselves",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "",
  "Group Project and Final Cramming Session!",
  "",
  "",
  "Exams!",
  "Exam Results!",
  "",
  ]


  define List_subjects = ["History",
                          "Science",
                          "Math",
                          "Literacy",
                          "Language",
                          "Geography",
                          "Art",
                          "Music",
                          "Physical Education",
                          ]

  #used to display tooltips in the correct place
  default spookle_offset = 0

  # Declare characters used by this game. The color argument colorizes the
  # name of the character.

  ######### CHARACTER DEFINES #############
  define c = Character("Caragh", image="Caragh")
  #alt Narrator
  define Description = Character(None)
  define Everyone = Character("Everyone")

  define AAA = Character("Achilles, Adonis, Atlas")
  define Achilles = Character("Achilles")
  define Adonis = Character("Adonis")
  define Atlas = Character("Atlas")
  define Athan = Character("Athan ")
  define Bahini = Character("Bahini ")
  define Bestia = Character("Bestia")
  define Caragh = Character("Caragh", image="Caragh")
  define Craig = Character("Craig")
  define Dougal = Character("Dougal")
  define Fayette = Character("Fayette")
  define Florence = Character("Florence")
  define Hecate = Character("Hecate")
  define Jo = Character("Jo")
  define Juniper = Character("Juniper")
  define Lateef = Character("Lateef")
  define McCoy = Character("McCoy")
  define Mog = Character("Mog")
  define Nyx = Character("Nyx")
  define Roark = Character("Roark")
  define Rudolph = Character("Rudolph")
  define Sanura = Character("Sanura")
  define Sophia = Character("Sophia")
  define Una = Character("Una")
  define UnaQuiet = Character("Una", what_prefix="{size=-10}", what_suffix="{/size}")
  define UnaLoud  = Character("Una", what_prefix="{size=+20}", what_suffix="{/size}")
  define Xisreia = Character("Xisreia")
  define Teacher = Character("Teacher")

  #nvl used for phone display
  define c_phone = Character("Caragh", kind=nvl, image="caragh", callback=Phone_SendSound)
  define b_phone = Character("Bahini", kind=nvl, callback=Phone_ReceiveSound)
  define n_phone = Character("Nyx", kind=nvl, callback=Phone_ReceiveSound)


  define sm_phone = Character("Sanura's Mom", kind=nvl, callback=Phone_ReceiveSound)

  #define nvl_narrator = Character(None, kind=nvl)

  define CraigMother = Character("Craig's Mother")
  define HecateMother = Character("Hecate's Mother")
  define HecateFather = Character("Hecate's Father")
  define SanuraMother = Character("Sanura's Mother")
  define Nurse = Character("Nurse")

  ######### SOUND DEFINES #############

  #-- MUSIC ---

  #5C		kiddy, lively music that has a few muffled chatters sprinkled within
  $music_5c = "audio/music/3_Corgi on beach by Ean Grimm.mp3"
  #School		Subtle lively music that's also quiet
  $music_school = "audio/music/4_Cat and Dog by Ean Grimm.mp3"
  #Bedroom		Quiet and serene. Fitting for bedtime routines.
  $music_bedroom = "audio/music/21_Alexander Nakarada - Drifting Minds (no drums).mp3"
  #Good Vibes		Something that can be both romantic and friendly
  $music_good_vibes = "audio/music/19_Alexander Nakarada - Spring.mp3"
  #Hospital		Muffled chatter, some humming noise but the music should be lively
  $music_hospital = "audio/music/8_I_m Alright by Ean Grimm.mp3"
  #Quiet		Something solemn with a few paper shuffling noises
  $music_quiet = "audio/music/24_Alexander Nakarada - Untold Stories.mp3"
  #Sad Vibes		Something that's sad but in a subtle way
  $music_sad_vibes = "audio/music/13_Alexander Nakarada - Emotionalism (no drums).mp3"

  #TODO Music

  #-- SFX ---

  #times change sfx
  $sfx_scene = "sceneswitch1.mp3"

  #Email/Phone		Notification boop
  $sfx_notification = "audio/ReceiveText.ogg"
  #Knock		Knocking on door
  $sfx_knock = "audio/door-wood-knock1.mp3"
  #Bell ring		school bell
  $sfx_schoolbell = "audio/school_bell.ogg"
  #Call		Ringing phone
  $sfx_phonecall = "audio/phone_ring.ogg"
  #Hang up		Hang up click
  $sfx_phonecallend = "audio/phone_hangup.ogg"

  #Hospital chatter
  $sfx_hospital_ambience = "audio/hospital_ambience.ogg"
  #classroom chatter
  $sfx_classroom_ambience = "audio/classroom_ambience.ogg"
  #quiet exam ambience
  $sfx_exam_ambience = "audio/exam_ambience.ogg"

  #TODO SFX
  #Chattering		muffled kids chattering (a few seconds long)
  #Laughter		Kids laughing
  #paper shuffling

  ######### CG/BG IMAGE DEFINES #############

  #Backgrounds
  image black = Solid("#000000")
  image bg black = Solid("#000000")
  image bg white = Solid("#ffffff")

  image bg classroom morning = "images/bg/classroom_full.png"
  image bg classroom afternoon = "images/bg/classroom_full.png"
  image bg classroom empty = "images/bg/classroom_full_afternoon.png"

  image bg hallway = "images/bg/hallway.png"
  image bg library = "images/bg/library.png"
  image bg hospital  = "images/bg/hospital.png"
  image bg room = "images/bg/room.png"
  image bg room night = "images/bg/room_night.png"
  image bg school = "images/bg/school_front.png"
  image bg teachers lounge = "images/bg/teacher_lounge.png"

  image bg cafeteria = "images/bg/classroom_empty.png"
  image bg streets = "images/bg/street_day.png"
  image bg streets night = "images/bg/street_night.png"

  #TODO REPLACE #CGs

  image cg bahini_feed    = "images/cg/bahini_feed.png"
  image cg craig_rock     = "images/cg/craig_rock.png"
  image cg hecate_chat    = "images/cg/hecate_chat.png"
  image cg sanura_pat     = "images/cg/sanura_pat.png"
  image cg end_bad        = "images/cg/end_bad.png"
  image cg end_good       = "images/cg/end_good.png"
  image cg fullcast_photo = "images/cg/fullcast_photo.png"
  image cg fullcast_photo_B = "images/cg/fullcast_photoB.png"
  image cg fullcast_photo_C = "images/cg/fullcast_photoC.png"

  #TODO REPLACE #Characters
  image Phone = "gui/game_phone/phone_calling.png"

  #----------------------------
  image Jo  = "images/sprites/jo_neutral.png"
  image Jo confused = "images/sprites/jo_confused.png"
  image Jo excited = "images/sprites/jo_excited.png"
  image Jo happy = "images/sprites/jo_happy.png"
  image Jo neutral = "images/sprites/jo_neutral.png"
  image Jo sad = "images/sprites/jo_sad.png"
  image Jo small = "images/sprites/jo_smallface.png"
  
  #----------------------------
  #image Nyx = "images/sprites/nyx_neutral.png"
  image Nyx = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/nyx_base.png",
    (0, 0), "images/sprites/nyx_happy.png")
    
  image Nyx happy = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/nyx_base.png",
    (0, 0), "images/sprites/nyx_happy.png")
    
  image Nyx huh = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/nyx_base.png",
    (0, 0), "images/sprites/nyx_huh.png")
    
  image Nyx mad = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/nyx_base.png",
    (0, 0), "images/sprites/nyx_mad.png")
    
  image Nyx sad = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/nyx_base.png",
    (0, 0), "images/sprites/nyx_sad.png")
  
  
  #----------------------------
  #image Bahini = "images/sprites/bahini_neutral.png"
  image Bahini = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/bahini_base.png",
    (0, 0), "images/sprites/bahini_wink.png")
  
  image Bahini wink = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/bahini_base.png",
    (0, 0), "images/sprites/bahini_wink.png")
    
  image Bahini sad = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/bahini_base.png",
    (0, 0), "images/sprites/bahini_sad.png")
  image Bahini smile = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/bahini_base.png",
    (0, 0), "images/sprites/bahini_smile.png")
  image Bahini happy = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/bahini_base.png",
    (0, 0), "images/sprites/bahini_smile.png")
  
  #----------------------------
  #image Craig = "images/sprites/craig_neutral.png"
  #image Craig happy = "images/sprites/craig_neutral.png"
  #image Craig spectacles = "images/sprites/craig_neutral.png"
  image Craig = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/craig_base2.png",
    (0, 0), "images/sprites/craig_neutral.png",
    (0, 0), ConditionSwitch( 
    "Craig_Arc_HasGlasses == False", Null(), 
    "True", "images/sprites/craig_glasses.png" ) )
    
  image Craig happy = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/craig_base2.png",
    (0, 0), "images/sprites/craig_happy.png",
    (0, 0), ConditionSwitch( 
    "Craig_Arc_HasGlasses == False", Null(), 
    "True", "images/sprites/craig_glasses.png" ) )
    
  image Craig neutral = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/craig_base2.png",
    (0, 0), "images/sprites/craig_neutral.png",
    (0, 0), ConditionSwitch( 
    "Craig_Arc_HasGlasses == False", Null(), 
    "True", "images/sprites/craig_glasses.png" ) )
    
  image Craig sad = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/craig_base2.png",
    (0, 0), "images/sprites/craig_sad.png",
    (0, 0), ConditionSwitch( 
    "Craig_Arc_HasGlasses == False", Null(), 
    "True", "images/sprites/craig_glasses.png" ) )
    
  image Craig worried = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/craig_base2.png",
    (0, 0), "images/sprites/craig_worried.png",
    (0, 0), ConditionSwitch( 
    "Craig_Arc_HasGlasses == False", Null(), 
    "True", "images/sprites/craig_glasses.png" ) )


  #----------------------------
  image Hecate = "images/sprites/hecate_neutral.png"
  image Hecate happy = "images/sprites/hecate_neutral.png"
  image Hecate = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/hecate_base.png",
    (0, 0), "images/sprites/hecate_unamused.png")
  image Hecate unamused = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/hecate_base.png",
    (0, 0), "images/sprites/hecate_unamused.png")
  image Hecate happy = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/hecate_base.png",
    (0, 0), "images/sprites/hecate_happy.png")
  image Hecate mad = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/hecate_base.png",
    (0, 0), "images/sprites/hecate_mad.png")
  image Hecate snarky = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/hecate_base.png",
    (0, 0), "images/sprites/hecate_snarky.png")

  #----------------------------
  #image Sanura = "images/sprites/sanura_neutral.png"
  #image Sanura happy = "images/sprites/sanura_neutral.png"
  image Sanura = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/sanura_base.png",
    (0, 0), "images/sprites/sanura_excited.png",
    (0, 0), "images/sprites/sanura_ears.png")
  image Sanura excited = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/sanura_base.png",
    (0, 0), "images/sprites/sanura_excited.png",
    (0, 0), "images/sprites/sanura_ears.png")
  image Sanura happy = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/sanura_base.png",
    (0, 0), "images/sprites/sanura_happy.png",
    (0, 0), "images/sprites/sanura_ears.png")
  image Sanura mad = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/sanura_base.png",
    (0, 0), "images/sprites/sanura_mad.png",
    (0, 0), "images/sprites/sanura_ears.png")
  image Sanura sad = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/sanura_base.png",
    (0, 0), "images/sprites/sanura_sad.png",
    (0, 0), "images/sprites/sanura_ears.png")
  image Sanura upset = Composite(
    (1227, 1080),
    (0, 0), "images/sprites/sanura_base.png",
    (0, 0), "images/sprites/sanura_upset.png",
    (0, 0), "images/sprites/sanura_ears.png")
  
  #----------------------------
  
  #invisble sprites to make showing the side image easy
  image Caragh = "images/sprites/empty.png"
  image Caragh body = "images/sprites/empty.png"
  image Caragh happy = "images/sprites/empty.png"
  image Caragh content = "images/sprites/empty.png"
  image Caragh mad = "images/sprites/empty.png"
  image Caragh rly = "images/sprites/empty.png"
  image Caragh pout = "images/sprites/empty.png"
  image Caragh sad = "images/sprites/empty.png"
  image Caragh snark = "images/sprites/empty.png"
  image Caragh surprise = "images/sprites/empty.png"
  
  image side Caragh body = "images/sprites/caragh_side_body.png"
  image side Caragh = Composite(
    (1920, 1080),
    (0, 0), "images/sprites/caragh_side_body.png",
    (0, 0), "images/sprites/caragh_side_head.png",
    (0, 0), "images/sprites/caragh_side_happy.png")
    
  image side Caragh happy = Composite(
    (1920, 1080),
    (0, 0), "images/sprites/caragh_side_body.png",
    (0, 0), "images/sprites/caragh_side_head.png",
    (0, 0), "images/sprites/caragh_side_happy.png")
    
  image side Caragh content = Composite(
    (1920, 1080),
    (0, 0), "images/sprites/caragh_side_body.png",
    (0, 0), "images/sprites/caragh_side_head.png",
    (0, 0), "images/sprites/caragh_side_content_eyesClosed.png")
    
  image side Caragh mad = Composite(
    (1920, 1080),
    (0, 0), "images/sprites/caragh_side_body.png",
    (0, 0), "images/sprites/caragh_side_head.png",
    (0, 0), "images/sprites/caragh_side_mad.png")
    
  image side Caragh rly = Composite(
    (1920, 1080),
    (0, 0), "images/sprites/caragh_side_body.png",
    (0, 0), "images/sprites/caragh_side_head.png",
    (0, 0), "images/sprites/caragh_side_rly.png")
    
  image side Caragh pout = Composite(
    (1920, 1080),
    (0, 0), "images/sprites/caragh_side_body.png",
    (0, 0), "images/sprites/caragh_side_head.png",
    (0, 0), "images/sprites/caragh_side_pout.png")
    
  image side Caragh sad = Composite(
    (1920, 1080),
    (0, 0), "images/sprites/caragh_side_body.png",
    (0, 0), "images/sprites/caragh_side_head.png",
    (0, 0), "images/sprites/caragh_side_sad_eyesClosed.png")
    
  image side Caragh snark = Composite(
    (1920, 1080),
    (0, 0), "images/sprites/caragh_side_body.png",
    (0, 0), "images/sprites/caragh_side_head.png",
    (0, 0), "images/sprites/caragh_side_snark.png")
    
  image side Caragh surprise = Composite(
    (1920, 1080),
    (0, 0), "images/sprites/caragh_side_body.png",
    (0, 0), "images/sprites/caragh_side_head.png",
    (0, 0), "images/sprites/caragh_side_surprise.png")
