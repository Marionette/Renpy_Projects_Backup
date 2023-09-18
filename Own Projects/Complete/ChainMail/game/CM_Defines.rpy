init:
  ####Variable Defines####
  default email_active = False
  default current_message = None
  default available_drafts = 0 
  default email_display = 'Inbox'
  default forwarding_email_flag = False
  
  default forward_Curse_Anne = False
  default forward_Curse_Dave = False
  default anne_once = False
  
  #Checked email flags
  default email_response_dave1 = False
  default email_response_dave2 = False
  default email_response_dave3 = False
  default email_response_dave4 = False
  default email_response_dave5 = False
  default email_response_dave6 = False
  default email_response_dave7 = False
  default email_response_dave8 = False
  default email_response_dave9 = False
  default email_response_dave10 = False
  default email_response_dave11 = False
    

  ####Background images####
  image bg black = Solid("#000000") 
  image bg white = Solid("#ffffff") 
  
  image bg desk day1 = "images/bg/desk_day1.png"
  image bg desk day2 = "images/bg/desk_day2.png"
  image bg desk afternoon = "images/bg/desk_afternoon1.png"
  image bg desk evening = "images/bg/desk_evening1.png"
  image bg desk night1 = "images/bg/desk_night1.png"
  image bg desk night2 = "images/bg/desk_night2.png"
  image bg desk blackout = "images/bg/desk_blackout.png"
  
  image cg rainynight girl = "images/cg/rainynight_girl.png"
  image cg rainynight nogirl = "images/cg/rainynight_nogirl.png"
  
  image catscare movie = Movie(channel="catscare", play="images/video/catscare.webm") 
  
  ####Character defines####
  # CHARACTERS
  #Robert 'Bob' Forrest (MC)
  define rf = Character('Bob')
  #David Hudson (Friend)
  define dh = Character("Dave")
  
  #Belle Franks (Sender)
  define bf = Character("Belle")
  #Anne Forrest (Sister)
  define bf = Character("Anne")
  
  
  ####Character images####
    
  
  ####Audio images####
  
  $music_Horror = "audio/Horror Ambience LOOP.ogg"
  $music_Pulsing = "audio/Horror Ambience LOOP.ogg"
  $music_Loneliness = "audio/Loneliness LOOP.ogg"
  $music_LonelyHouse = "audio/Lonely House LOOP.ogg"
  $music_Melancholy = "audio/Melancholy Ambience.ogg"
  $music_Mystery = "audio/Mystery Ambience LOOP.ogg"

  #TODO    
  $ renpy.music.register_channel("ambient","sfx",True,tight=True)
  
  $sound_scare = "audio/Broken Violin SCARE.ogg"
  $sound_rain = "audio/Heavy Rain LOOP.ogg"
  $sound_rain_inside = "audio/Rain on WIndow LOOP.ogg"
  $sound_thunder = "audio/Thunder 3.ogg"
  
  $sound_crow = "audio/54973__nuel__crow1.ogg"
  
