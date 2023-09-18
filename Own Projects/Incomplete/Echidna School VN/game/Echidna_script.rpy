init python:
  Kid1_Name = "Kid" 
  current_speaker = ""
  current_speaker_number = -1
  ArrayStartYear = 2020
  current_date = 14
  current_month = 6
  current_year = 2017
  current_time = "Morning"
  CHILD_LIST = []
  ADULT_LIST = []
  CharacterCount = 0
  ChildCount = 0
  AdultCount = 0
  PLAYER_LIST = []
  EndDate = [2020,6,30]
  

init python:
        
    def active_narrator(event, interact=True, **kwargs):
        global current_speaker
        if not interact:
            return
            
        current_speaker = ''
        SetCurrentCharacterNumber(-1)
        
    def active_kid1(event, interact=True, **kwargs):
        global current_speaker
        if not interact:
            return
            
        current_speaker = Kid1_Name
        SetCurrentCharacterNumber(SelectCharacterByName(Kid1_Name))
        
    def active_kid2(event, interact=True, **kwargs):
        global current_speaker
        if not interact:
            return
            
        current_speaker = Kid2_Name
        SetCurrentCharacterNumber(SelectCharacterByName(Kid2_Name))
        
    def active_mc(event, interact=True, **kwargs):
        global current_speaker
        if not interact:
            return
            
        current_speaker = 'Mainus Characterus'
        SetCurrentCharacterNumber(SelectCharacterByName('Mainus Characterus'))
        
    def active_e(event, interact=True, **kwargs):
        global current_speaker
        if not interact:
            return
            
        current_speaker = 'Eileen'
        SetCurrentCharacterNumber(SelectCharacterByName('Eileen'))
            
init:
  $gbl_SavedYear = 0
  $day = 0
  $renpy.random.seed() #get a new seed each game to ensure randomnesss.
  # You can place the script of your game in this file.

  # Declare images below this line, using the image statement.
  # eg. image eileen happy = "eileen_happy.png"

  # Declare characters used by this game.
  define narrator = Character(None,
                              what_prefix="{font=assets/PermanentMarker.ttf}{size=26}",
                              what_suffix="{/font}{/size}",
                              who_prefix="{font=assets/PermanentMarker.ttf}{size=28}",
                              who_suffix="{/font}{/size}",
                              callback=active_narrator)
                              
  define mc = DynamicCharacter('Mainus Characterus', 
                      color="#c8ffc8", 
                      what_prefix="{font=assets/PermanentMarker.ttf}{size=26}",
                      what_suffix="{/font}{/size}",
                      who_prefix="{font=assets/PermanentMarker.ttf}{size=28}",
                      who_suffix="{/font}{/size}",
                      callback=active_mc)
  
  define e = Character('Eileen', 
                      color="#c8ffc8", 
                      what_prefix="{font=assets/PermanentMarker.ttf}{size=26}",
                      what_suffix="{/font}{/size}",
                      who_prefix="{font=assets/PermanentMarker.ttf}{size=28}",
                      who_suffix="{/font}{/size}",
                      callback=active_e)
                      
  define k1 = DynamicCharacter('Kid1_Name', 
                      color="#c8ffc8", 
                      what_prefix="{font=assets/PermanentMarker.ttf}{size=26}",
                      what_suffix="{/font}{/size}",
                      who_prefix="{font=assets/PermanentMarker.ttf}{size=28}",
                      who_suffix="{/font}{/size}",
                      callback=active_kid1)
                      
  define k2 = DynamicCharacter('Kid2_Name', 
                      color="#c8ffc8", 
                      what_prefix="{font=assets/PermanentMarker.ttf}{size=26}",
                      what_suffix="{/font}{/size}",
                      who_prefix="{font=assets/PermanentMarker.ttf}{size=28}",
                      who_suffix="{/font}{/size}",
                      callback=active_kid2)
                      
  # Declare Images used by the game
  image bg classroom morning = "img/bg/classroom_morning.jpg"
  image bg classroom afternoon = "img/bg/classroom_afternoon.jpg"
  
  image teach1 happy = "img/sprites/teacher/teach1_content.png"
  image kid1 happy = "img/sprites/student/kid1_happy.png"
  
  image mc content = "img/sprites/mc/mc_content.png"

  #Define date time variables
  $current_date = 14
  $current_month = 6
  $current_year = 2017
  $current_time = "Morning"

  #------------------------------------------------------
label lbl_SetupGame:
  $FillEventList() 
  $SetSpecialEvents(current_year)
  scene bg classroom morning
  $SetDate(2020, 6, 1)
  $gbl_FillEventList = True
  #$FillEventList(current_year, current_month+1, 1 )
  #$SetSpecialEvents(current_year)
  #"Starting a new Game... "#Day [current_date] Month [current_month] Year [current_year]"
  #show teach1 happy at left
  #show kid1 happy:
  #  xalign 0.7
  
  #Generate Children
  $ChildCount = 10
  $CHILD_LIST = GenerateCharacters(ChildCount)
  python:
    for child in CHILD_LIST:
      child.SetSpecificAge(11,1)
  
  #Generate and modify Adults
  $AdultCount = 2
  $ADULT_LIST = GenerateCharacters(AdultCount)
  $ADULT_LIST[0].SetSpecificAppearance("img/sprites/teacher/teach1_content.png")
  $ADULT_LIST[1].SetSpecificAppearance("img/sprites/teacher/teach2_content.png")
  python:
    for adult in ADULT_LIST:
      adult.IsAStudent = False
      adult.Gender = "Female"
      adult.SetSpecificAge(22,3)
    
  #Track total NPC count
  $CharacterCount = ChildCount + AdultCount
  
  #Set Specific values for Player Chracter
  $PLAYER_LIST = GenerateCharacters(1)
  $PLAYER_LIST[0].SetUniqueCharacter( "Player Namehere", 
                                      22, 
                                      "Female",
                                      [16,11], 
                                      List_Personalities[0], 
                                      [List_Traits[0],List_Traits[1]], 
                                      [List_Preferences[0],List_Preferences[1],List_Preferences[2]], 
                                      [List_Preferences[0],List_Preferences[1],List_Preferences[2]], 
                                      "img/sprites/mc/mc_content.png")
                                      
  return
  
  #------------------------------------------------------
# The game starts here.
label start:
  call lbl_SetupGame
  #-- Debug testing
  call lbl_testingMenu
  #--
  
  call lbl_StartGame
  
  return
     
  #------------------------------------------------------

  
label lbl_StartGame:                
  call lbl_SchoolDay
  
  return

  #------------------------------------------------------
label lbl_testingMenu:     
  menu:
    "Testing menu"
    "Emotions test":
      call lbl_faceTest
    "Random Kid name/image test":
      call lbl_randomKidTest
    "Generic Event test":
      call lbl_GenericEventTesting
    "Continue with your day":
      show mc content at left
      pass
                                      
  jump lbl_StartGame

  return

  #------------------------------------------------------
label lbl_GenericEventTesting:

  call lbl_genericEventTest
  call lbl_genericEventTest
  call lbl_genericEventTest
  call lbl_genericEventTest
  call lbl_genericEventTest
  call lbl_genericEventTest
  call lbl_genericEventTest
  
  return 
  #------------------------------------------------------
label lbl_testing:
  "Starting a new day... Day [current_date] Month [current_month] Year [current_year] - Character Count = [CharacterCount]"
  $NewEvent = [("All day", "A random kids Birthday.")]
  $AddNewEvent(current_year, current_month+1, current_date, NewEvent)
  $HasEvent = DayHasEvent(current_year, current_month+1, current_date)
  if (HasEvent):
    $Events = GetEventList(current_year, current_month+1, current_date)
    "New Event Added for today - [Events]"
  else:
    "No Event Added for today"

  #------------------------------------------------------
label lbl_NextDay():
  $current_time = "Morning"
  $AddDay(1)
  $save_name = "~%d/%d/%d~"%(current_year, current_month+1, current_date)
  $schoolday = IsSchoolDay(current_year, current_month+1, current_date)
  
  $daysLeft = DaysUntil(EndDate[0], EndDate[1]-1, EndDate[2])
  
  "There are [daysLeft] left until the end of the school year."
  
  if (daysLeft > 0):
    if schoolday:
      "Its a schoolday"
      jump lbl_SchoolDay
    else:
      "Its not a schoolday"
      jump lbl_NoSchoolDay
  else:
    "Thats all folks."
    
  return
  
  #------------------------------------------------------
label lbl_SchoolDay():
  $current_time = "Morning"
  #$AddDay(1)
  
  #jump lbl_testing
  play music GetMusicByMood("light")
  #"Starting a new day..."
  
  show screen day_menu()
  call lbl_Morning_rand from _call_lbl_Morning_rand
  call lbl_FirstPeriod_rand from _call_lbl_FirstPeriod_rand
  call lbl_Lunch_rand from _call_lbl_Lunch_rand
  call lbl_SecondPeriod_rand from _call_lbl_SecondPeriod_rand
  call lbl_AfterSchool_rand from _call_lbl_AfterSchool_rand
  call lbl_Evening_rand from _call_lbl_Evening_rand
  
  #$current_time = "Night"
  jump lbl_NextDay
  return
  
  #------------------------------------------------------
label lbl_NoSchoolDay():
  play music GetMusicByMood("light")
  "Starting a new day..."
  
  show screen day_menu()
  #call lbl_NoSchool_Morning_rand from _call_lbl_NoSchool_Morning_rand
  #call lbl_NoSchool_Noon_rand from _call_lbl_NoSchool_Noon_rand
  #call lbl_NoSchool_Evening_rand from _call_lbl_NoSchool_Evening_rand
  
  $current_time = "Night"
  jump lbl_NextDay
  return
  
  #------------------------------------------------------
label lbl_faceTest:
  "Emotions test"
  
  scene bg classroom morning
  "Ready..."
  
  $CHILD_LIST[0].Mood = 1
  show image CHILD_LIST[0].Appearance()
  "1..."
  
  $CHILD_LIST[0].Mood = 2
  show image CHILD_LIST[0].Appearance()
  "2..."
  
  $CHILD_LIST[0].Mood = 3
  show image CHILD_LIST[0].Appearance()
  "3..."
  
  
  return

  #------------------------------------------------------
label lbl_randomKidTest:

  "Random Kid name/image test"
  show image CHILD_LIST[0].Appearance():
    yalign 1.0
    xalign 0.2
  "Random Kid name swap and image swap test"
  $Kid1_Name = "Kid" 
  k1 "Hi im a kid."
  $Kid1_Name = CHILD_LIST[0].Name
  k1 "My name is [CHILD_LIST[0].Name]"
  show image CHILD_LIST[1].Appearance():
    yalign 1.0
    xalign 0.4
  $Kid1_Name = CHILD_LIST[1].Name
  k1 "My name is [CHILD_LIST[1].Name]"
  show image CHILD_LIST[2].Appearance():
    yalign 1.0
    xalign 0.6
  $Kid1_Name = CHILD_LIST[2].Name
  k1 "My name is [CHILD_LIST[2].Name]"
  show image CHILD_LIST[3].Appearance():
    yalign 1.0
    xalign 0.8
  $Kid1_Name = CHILD_LIST[3].Name
  k1 "My name is [CHILD_LIST[3].Name]"
  
  "adult image display"
  show image ADULT_LIST[0].Appearance():
    yalign 1.0
    xalign 0.9
  show image ADULT_LIST[1].Appearance():
    yalign 1.0
    xalign 0.1
    
  "hiding children..."
  hide image CHILD_LIST[0].Appearance()
  hide image CHILD_LIST[1].Appearance()
  hide image CHILD_LIST[2].Appearance()
  hide image CHILD_LIST[3].Appearance()
  
  "children hidden"
  return
  
  
label lbl_genericEventTest:
  scene bg classroom morning
  "Testing generic event"
  "Choosing Random Child."
  $Child1 = SelectRandomChild()
  $Kid1_Name = Child1.Name
  show image Child1.Appearance():
    yalign 1.0
  k1 "My name is [Child1.Name]"
  
  k1 "I like [Child1.Likes[0]], [Child1.Likes[1]] and [Child1.Likes[2]]"
  k1 "I really can't stand [Child1.Dislikes[0]], [Child1.Dislikes[1]] and [Child1.Dislikes[2]]"
  
  $Child2 = SelectRandomChild()
  $Kid2_Name = Child2.Name
  show image Child2.Appearance():
    yalign 1.0
    xalign 0.5
  k2 "My name is [Child2.Name]"
  k1 "[Child2.Forename] likes [Child2.Likes[0]], [Child2.Likes[1]] and [Child2.Likes[2]]"
  $He = Child2.GetPronoun('He')
  k1 "[He] really can't stand [Child2.Dislikes[0]], [Child2.Dislikes[1]] and [Child2.Dislikes[2]]"
  
  
  "Ending Generic Test event"
  return