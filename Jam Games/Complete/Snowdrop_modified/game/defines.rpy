init:
  image snow = Snow("gui/snowflake.png")
  $ anjali_score = 0
  $ archer_score = 0
  $ archer_romanceEndScoreNeeded = 45
  $ archer_comfortScoreNeeded = 15
  $ fc_score = 1 # I have no idea what this is for?
  $ flag_BringAgreement = False
  $ flag_snowballFight = False
  $ flag_CheckedMarketStalls = False
  image animation_heart = Animation("images/heart/heart1.png", 0.25,
                                "images/heart/heart2.png", 0.25,
                                "images/heart/heart3.png", 0.25,
                                "images/heart/heart4.png", 0.25,
                                "images/heart/heart5.png", 0.25,
                                "images/heart/heart6.png", 0.25,
                                "images/heart/heart7.png", 0.25,
                                "images/heart/heart8.png", 0.25,
                                "images/heart/heart9.png", 0.25,
                                "images/heart/heart10.png", 0.25,
                                "images/heart/heart11.png", 0.25,
                                "images/heart/heart12.png", 0.25,
                                "images/heart/heart13.png", 0.25,
                                "images/heart/heart14.png", 0.25)

  define an = Character('Anjali', color="#000000")
  define ar = Character('Archer', color="#000000")
  define li = Character('Lilah', color="#000000", image="lilah") 
  define ta = Character('Train Announcer', color="#000000")
  define que = Character('???', color="#000000")
  define will = Character('Willis', color="#000000")
  define judge = Character('Judge', color="#000000")
  define cash = Character('Cashier', color="#000000")
  define ow = Character('Old Woman', color="#000000")
  define mom = Character('Mom', color="#000000")
  define ann = Character('Announcer', color="#000000")

  #Here are the images of the sprites
  image anjali mad = "images/sprites/AnjaliMad.png"
  image anjali happy = "images/sprites/AnjaliSmile.png"
  image anjali smile = "images/sprites/AnjaliSmile.png"
  image anjali normal = "images/sprites/AnjaliNeutral.png"
  image anjali neutral = "images/sprites/AnjaliNeutral.png"
  image anjali sad = "images/sprites/AnjaliSad.png"
  #TODO
  #image anjali happy = "images/sprites/AnjaliHappy.png"

  image archer blush = "images/sprites/ArcherBlush.png"
  image archer scarfblush = "images/sprites/ArcherBlushScarf.png"
  image archer winterblush = "images/sprites/ArcherBlushWinter.png"
  image archer happy = "images/sprites/ArcherHappy.png"
  image archer scarfhappy = "images/sprites/ArcherHappyScarf.png"
  image archer winterhappy = "images/sprites/ArcherHappyWinter.png"
  image archer mad = "images/sprites/ArcherMad.png"
  image archer scarfmad = "images/sprites/ArcherMadScarf.png"
  image archer wintermad = "images/sprites/ArcherMadWinter.png"
  image archer normal = "images/sprites/ArcherNeutral.png"
  image archer scarfnormal = "images/sprites/ArcherNeutralScarf.png"
  image archer winternormal = "images/sprites/ArcherNeutralWinter.png"
  image archer neutral = "images/sprites/ArcherNeutral.png"
  image archer scarfneutral = "images/sprites/ArcherNeutralScarf.png"
  image archer winterneutral = "images/sprites/ArcherNeutralWinter.png"
  image archer sad = "images/sprites/ArcherSad.png"
  image archer scarfsad = "images/sprites/ArcherSadScarf.png"
  image archer wintersad = "images/sprites/ArcherSadWinter.png"
  image archer smile = "images/sprites/ArcherSmile.png"
  image archer scarfsmile = "images/sprites/ArcherSmileScarf.png"
  image archer wintersmile = "images/sprites/ArcherSmileWinter.png"
  image archer wintertalk = "images/sprites/Archertalkwinter.png"
  image archer talk = "images/sprites/Archertalk.png"
  image archer scarftalk = "images/sprites/Archertalkwinter.png"
  #out = winter
  image archer neutralout = "images/sprites/ArcherNeutralWinter.png"
  image archer smileout = "images/sprites/ArcherSmileWinter.png"
  image archer happyout = "images/sprites/ArcherHappyWinter.png"
  image archer sadout = "images/sprites/ArcherSadWinter.png"
  #TODO

  image lilah blush = "images/sprites/LBlush.png"
  image lilah blushout = "images/sprites/LBlushOut.png"
  image lilah happy = "images/sprites/LHappy.png"
  image lilah happyout = "images/sprites/LHappyOut.png"
  image lilah mad = "images/sprites/LMad.png"
  image lilah madout = "images/sprites/LMadOut.png"
  image lilah normal = "images/sprites/LNeutral.png"
  image lilah normalout = "images/sprites/LNeutralOut.png"
  image lilah neutral = "images/sprites/LNeutral.png"
  image lilah neutralout = "images/sprites/LNeutralOut.png"
  image lilah sad = "images/sprites/LSad.png"
  image lilah sadout = "images/sprites/LSadOut.png"
  image lilah sadblush = "images/sprites/LSadBlush.png"
  image lilah sadblushout = "images/sprites/LSadBlushOut.png"
  #TODO
  image lilah smile = "images/sprites/LHappy.png"
  image lilah smileout = "images/sprites/LHappyOut.png"

  #Background images
  image bg transition = "gui/background.png" 
  image bg black = Solid("#000000")     
  image bg white = Solid("#ffffff")  
  image bg street_ordinary = "images/backgrounds/street_ordinary.jpg"
  image bg train_one = "images/backgrounds/train_one.jpg"
  image bg trainmorning = "images/backgrounds/trainmorning.jpg"
  image bg treetops = "images/backgrounds/treetops.jpg"
  image bg brown1 = "images/backgrounds/brown1.jpg"
  image bg lobby = "images/backgrounds/brown1.jpg"
  image bg kitchen = "images/backgrounds/kitchen.jpg"
  image bg brown2 = "images/backgrounds/brown2.jpg"
  image bg innhallway = "images/backgrounds/brown2.jpg" 
  image bg hallway = "images/backgrounds/brown2.jpg"  
  image bg grocery = "images/backgrounds/grocery.jpg"
  image bg librarynight = "images/backgrounds/librarynight.jpg"
  image bg livingroom = "images/backgrounds/librarynight.jpg" 
  image bg NightBedroom = "images/backgrounds/NightBedroom.jpg"
  image bg lilahsroom = "images/backgrounds/NightBedroom.jpg" 
  image bg lilahscabin = "images/backgrounds/NightBedroom.jpg" 
  image bg corner = "images/backgrounds/corner.jpg"
  image bg park = "images/backgrounds/park.jpg"
  image bg patio = "images/backgrounds/patio.jpg"
  image bg bathroom = "images/backgrounds/bathroom.jpg"
  image bg SnowStreet = "images/backgrounds/SnowStreet.jpg"
  image bg Snowmarket = "images/backgrounds/Snowmarket.jpg"
  image bg SnowMarket = "images/backgrounds/Snowmarket.jpg"
  image bg NYC = "images/backgrounds/NYC.jpg"
  image bg car = "images/backgrounds/car.jpg"
  image bg ChristmasTreeInn = "images/backgrounds/ChristmasTreeInn.jpg"
  image bg cafe = "images/backgrounds/cafe.jpg" 
  image bg SnowPark = "images/backgrounds/SnowPark.jpg"
  image bg fields = "images/backgrounds/Field.jpg"  
  image bg treetown = "images/backgrounds/TreeTown.jpg"
  image bg gazebo = "images/backgrounds/gazebo.jpg"
  image bg archerroom = "images/backgrounds/archerroom.jpg" 
  
  #TODO
 
  #CG Images
  image cg kiss = "images/cg/kiss_gloves.png"  

  #Chapter Screens
  image transition_prologue = "gui/transition_prologue.png"
  image transition_chapter1 = "gui/transition_chapter1.png"
  image transition_chapter2 = "gui/transition_chapter2.png"
  image transition_chapter3 = "gui/transition_chapter3.png"
  image transition_chapter4 = "gui/transition_chapter4.png"
  image transition_chapter5 = "gui/transition_chapter5.png"
  image transition_chapter6 = "gui/transition_chapter6.png"
  image transition_chapter7 = "gui/transition_chapter7.png"
  image credits = "credits image.jpg"

  #Extras
  image heart = "heart.png" 

  #Music
  $music_autumn  = "audio/music/Autumn.ogg"
  $music_calmer_times  = "audio/music/Calmer-Times.ogg"
  $music_gentlepiano  = "audio/music/gentlepiano.ogg"
  $music_home  = "audio/music/Home.ogg"
  $music_interlude  = "audio/music/Interlude.ogg"
  $music_morning_snowflake  ="audio/music/Morning_Snowflake.ogg"
  $music_silentnight  = "audio/music/SilentNight.ogg"
  $music_themesong  = "audio/music/themesong.ogg"
  $music_thinkingofyou  = "audio/music/ThinkingofYou.ogg"
  $music_whatchild  = "audio/music/WhatChild.ogg"
  $music_archersong  = "audio/music/ArcherSong.ogg"
  $music_passingtime  = "audio/music/PassingTime.ogg"
  $music_sunbathing  = "audio/music/sunbathing.ogg"
  $music_warmth = "audio/music/warmth.ogg"
  $music_foreverfriends = "audio/music/Foreverfriend.ogg"
  $music_sadness = "audio/music/sadness.ogg"

  #TODO:
  $music_peaceofmind  = "audio/music/emanuel.ogg"
  $music_craig1 = "audio/music/emanuel.ogg"
  

  #Sounds  
  $sound_doorclose  = "audio/sound/doorclose.ogg"
  $sound_footsteps  = "audio/sound/footsteps.ogg"
  $sound_footstepsoutside  = "audio/sound/footstepsOutside.ogg"
  $sound_opendoor  = "audio/sound/OpenDoor.ogg"
  $sound_peopleambient  = "audio/sound/PeopleAmbient.ogg"
  $sound_phone  = "audio/sound/phone.ogg"
  $sound_plasticbag  = "audio/sound/plasticbag.ogg"
  $sound_success  = "audio/sound/success.ogg"
  $sound_train  = "audio/sound/train.ogg"
  
  #TODO:
  $sound_trainpullingin  = "audio/sound/footsteps.ogg"
  $sound_interlude  = "audio/sound/footsteps.ogg"
  $sound_doorpound  = "audio/sound/footsteps.ogg"
