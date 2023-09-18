
#------------------------------------------------------
label Day_2_WakeUp_FirstTime:
  $AdvanceDay(1)
  $dayStr = GetDayString(GetDay())
  jt "Oh its a new day. Now its [dayStr]"
  jump Day_1_Explore
  
label Day_1_WakeUp_FirstTime:

  #Generate NPCs
  $CHARACTER_LIST = GenerateCharacters()
  
  
  $SetDay(0)
  $SetTime(8)
  $timeStr = GetTimeString(GetTime())
  $dayStr = GetDayString(GetDay())
  
  #$options = []
  #python:
  #  for chara in CHARACTER_LIST:
  #    options.append((chara.Name, 1))
  #$res = renpy.display_menu(options, interact=True, screen="choice")
    
  
  #jt "Picked [res]"
  jt "It's [timeStr] on [dayStr]. I just woke up."
        
  jump Day_1_Explore
  
#------------------------------------------------------
label Day_1_WakeUp_Again:

  $SetDay(0)
  $count_Loops += 1
  $SetTime(8)
  $timeStr = GetTimeString(GetTime())
  $dayStr = GetDayString(GetDay())
  
  jt "It's [timeStr] on [dayStr]. Back here again."
  jt "I've looped [count_Loops] times."
  call reset_events_run
  
  jump Day_1_Explore
  
#------------------------------------------------------
label Day_1_Explore:
  default visitedLocations_list = []
  
  $location = ""
  menu Day_1_MapMenu:
    set visitedLocations_list
    "Where should i go?"
    "[AvailableLocations[0][1]]":
      $SetLocation(0)
      call expression "Day_1_AtLocation"
      #call expression "Day_1_" + AvailableLocations[0][0]
    "[AvailableLocations[1][1]]":
      $SetLocation(1)
      call expression "Day_1_AtLocation"
      #call expression "Day_1_" + AvailableLocations[1][0]
    "[AvailableLocations[2][1]]":
      $SetLocation(2)
      call expression "Day_1_AtLocation"
      #call expression "Day_1_" + AvailableLocations[2][0]
    "[AvailableLocations[3][1]]":
      $SetLocation(3)
      call expression "Day_1_AtLocation"
      #call expression "Day_1_" + AvailableLocations[3][0]
    "[AvailableLocations[4][1]]":
      $SetLocation(4)
      call expression "Day_1_AtLocation"
      #call expression "Day_1_" + AvailableLocations[4][0]
    "[AvailableLocations[5][1]]":
      $SetLocation(5)
      call expression "Day_1_AtLocation"
      #call expression "Day_1_" + AvailableLocations[5][0]
    "[AvailableLocations[6][1]]":
      $SetLocation(6)
      call expression "Day_1_AtLocation"
      #call expression "Day_1_" + AvailableLocations[6][0]
    "[AvailableLocations[7][1]]":
      $SetLocation(7)
      call expression "Day_1_AtLocation"
      #call expression "Day_1_" + AvailableLocations[7][0]
    "Somewhere else...":
      menu:
        "[AvailableLocations[8][1]]":
          $SetLocation(8)
          call expression "Day_1_AtLocation"
          #call expression "Day_1_" + AvailableLocations[8][0]
        "[AvailableLocations[9][1]]":
          $SetLocation(9)
          call expression "Day_1_AtLocation"
          #call expression "Day_1_" + AvailableLocations[9][0]
        "[AvailableLocations[10][1]]":
          $SetLocation(10)
          call expression "Day_1_AtLocation"
          #call expression "Day_1_" + AvailableLocations[10][0]
        "[AvailableLocations[11][1]]":
          $SetLocation(11)
          call expression "Day_1_AtLocation"
          #call expression "Day_1_" + AvailableLocations[11][0]
        "[AvailableLocations[12][1]]":
          $SetLocation(12)
          call expression "Day_1_AtLocation"
          #call expression "Day_1_" + AvailableLocations[12][0]
        "[AvailableLocations[13][1]]":
          $SetLocation(13)
          call expression "Day_1_AtLocation"
          #call expression "Day_1_" + AvailableLocations[13][0]
        "[AvailableLocations[14][1]]":
          $SetLocation(14)
          call expression "Day_1_AtLocation"
          #call expression "Day_1_" + AvailableLocations[14][0]
        "[AvailableLocations[15][1]]":
          $SetLocation(15)
          call expression "Day_1_AtLocation"
          #call expression "Day_1_" + AvailableLocations[15][0]
        "I think im done.":
          jump Day_1_WakeUp_Again
          
  
  #$day = GetDay() + 1
  
  #call expression "Day_1_" + location
          
  #menu Day_1_MapMenu:
  #  set visitedLocations_list
  #  "Where should i go?"
  #  "[AvailableLocations[0][1]]":
  #    call expression "Day_1_" + AvailableLocations[0][0]
  #  "[AvailableLocations[1][1]]":
  #    call expression "Day_1_" + AvailableLocations[1][0]
  #  "[AvailableLocations[2][1]]":
  #    call expression "Day_1_" + AvailableLocations[2][0]
  #  "[AvailableLocations[3][1]]":
  #    call expression "Day_1_" + AvailableLocations[3][0]
  #  "[AvailableLocations[4][1]]":
  #    call expression "Day_1_" + AvailableLocations[4][0]
  #  "[AvailableLocations[5][1]]":
  #    call expression "Day_1_" + AvailableLocations[5][0]
  #  "[AvailableLocations[6][1]]":
  #    call expression "Day_1_" + AvailableLocations[6][0]
  #  "[AvailableLocations[7][1]]":
  #    call expression "Day_1_" + AvailableLocations[7][0]
  #  "Somewhere else...":
  #    menu:
  #      "[AvailableLocations[8][1]]":
  #        call expression "Day_1_" + AvailableLocations[8][0]
  #      "[AvailableLocations[9][1]]":
  #        call expression "Day_1_" + AvailableLocations[9][0]
  #      "[AvailableLocations[10][1]]":
  #        call expression "Day_1_" + AvailableLocations[10][0]
  #      "[AvailableLocations[11][1]]":
  #        call expression "Day_1_" + AvailableLocations[11][0]
  #      "[AvailableLocations[12][1]]":
  #        call expression "Day_1_" + AvailableLocations[12][0]
  #      "[AvailableLocations[13][1]]":
  #        call expression "Day_1_" + AvailableLocations[13][0]
  #      "[AvailableLocations[14][1]]":
  #        call expression "Day_1_" + AvailableLocations[14][0]
  #      "[AvailableLocations[15][1]]":
  #        call expression "Day_1_" + AvailableLocations[15][0]
  #      "I think im done.":
  #        jump Day_1_WakeUp_Again
  
  if IsTimePast(21):
    jt "It's getting late. I should head back."
    #if GetDay() > 1:
    jump Day_1_WakeUp_Again
    #else:
    #  jump Day_2_WakeUp_FirstTime
  jump Day_1_MapMenu
#------------------------------------------------------

#------------------------------------------------------
label Day_1_AtLocation:
  $AdvanceTime()
  $timeStr = GetTimeString(GetTime())
  $locationStr = GetLocationString(GetLocation())
  jt "It's [timeStr]. It's a [locationStr]"
  
  call events_run_period
  
  $options = []
  python:
    for chara in GetCharactersPresent(CurrentLocation, CurrentDay, CurrentTime):
      options.append((chara.Name, chara.Name))
  
  if len(options) == 0:
    jt "Nobody Here..."
  else:
    jt "Oh someone is here, who should i talk to?"
    $res = renpy.display_menu(options, interact=True, screen="choice")   
  
    jt "Picked [res]"
  
  return
#------------------------------------------------------

label Day_1_Cafe:
  $AdvanceTime()
  $timeStr = GetTimeString(GetTime())
  jt "It's [timeStr]. It's a Cafe"
  
  $SetLocation(0)
  $options = []
  python:
    for chara in GetCharactersPresent(CurrentLocation, CurrentDay, CurrentTime):
      options.append((chara.Name, chara.Name))
  
  if len(options) == 0:
    jt "Nobody Here..."
  else:
    jt "Oh someone is here, who should i talk to?"
    $res = renpy.display_menu(options, interact=True, screen="choice")   
  
    jt "Picked [res]"
  
  return
  
label Day_1_Church:
  $AdvanceTime()
  $timeStr = GetTimeString(GetTime())
  jt "It's [timeStr]. It's a Church"
  return
  
label Day_1_ClockTower:
  $AdvanceTime()
  $timeStr = GetTimeString(GetTime())
  jt "It's [timeStr]. It's a Clock Tower"
  return
  
label Day_1_Hospital:
  $AdvanceTime()
  $timeStr = GetTimeString(GetTime())
  jt "It's [timeStr]. It's a Hospital"
  return
  
label Day_1_House:
  $AdvanceTime()
  $timeStr = GetTimeString(GetTime())
  jt "It's [timeStr]. It's a House"
  return
  
label Day_1_Inn:
  $AdvanceTime()
  $timeStr = GetTimeString(GetTime())
  jt "It's [timeStr]. It's a Inn"
  return
  
label Day_1_Library:
  $AdvanceTime()
  $timeStr = GetTimeString(GetTime())
  jt "It's [timeStr]. It's a Library"
  return
  
label Day_1_Mansion:
  $AdvanceTime()
  $timeStr = GetTimeString(GetTime())
  jt "It's [timeStr]. It's a Mansion"
  return
  
label Day_1_MansionGate:
  $AdvanceTime()
  $timeStr = GetTimeString(GetTime())
  jt "It's [timeStr]. It's a Mansion Gate"
  return
  
label Day_1_Park:
  $AdvanceTime()
  $timeStr = GetTimeString(GetTime())
  jt "It's [timeStr]. It's a Park"
  return
  
label Day_1_PoliceStation:
  $AdvanceTime()
  $timeStr = GetTimeString(GetTime())
  jt "It's [timeStr]. It's a Police Station"
  return
  
label Day_1_PostOffice:
  $AdvanceTime()
  $timeStr = GetTimeString(GetTime())
  jt "It's [timeStr]. It's a Post Office"
  return
  
label Day_1_Pub:
  $AdvanceTime()
  $timeStr = GetTimeString(GetTime())
  jt "It's [timeStr]. It's a Pub"
  return
  
label Day_1_School:
  $AdvanceTime()
  $timeStr = GetTimeString(GetTime())
  jt "It's [timeStr]. It's a School"
  return
  
label Day_1_Shop:
  $AdvanceTime()
  $timeStr = GetTimeString(GetTime())
  jt "It's [timeStr]. It's a Shop"
  return
  
label Day_1_TrainStation:
  $AdvanceTime()
  $timeStr = GetTimeString(GetTime())
  jt "It's [timeStr]. It's a Train Station"
  return
  
#------------------------------------------------------
#------------------------------------------------------