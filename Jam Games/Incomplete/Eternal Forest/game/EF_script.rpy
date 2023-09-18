

# The game starts here.
label start:
    $current_location = YourHouse

    e "Ready to go on an adventure?." 
    
    menu:
      "Start Story":
        jump lbl_character_gen
      "Yes! Lets go!":
        jump lbl_mapTest
      "No, I want to quit.":
        pass
      "Other Debug Tests":
        menu:
          "Map Test":
            jump lbl_mapTest
          "Calendar Test":
            jump lbl_calendarTest
          "Indicator Test":
            jump lbl_indicatorTest
          "Activities Test":
            jump lbl_activitiesTest
          "Quit":
            pass

    return

#-------------------------------------------------------------    
label lbl_mapTest:
    
    show bg WorldMap with fade
    $have_arrived = False
    call screen Map_Screen()
    
    #"Now arriving at...[_return]"
    #$loc = _return -1
    call expression LocationLabelList[_return -1] from _call_expression
    
    jump lbl_activitiesTest
    #jump start
    return
    
#-------------------------------------------------------------    
  ## Locations ##
    
label lbl_locations_TradeOutpost:
  #TradeOutpost - 1
    show bg TradeOutpost with fade
    "Now arriving at...TradeOutpost"
    
    return
#-------------------------------------------------------------    
    
label lbl_locations_VillageWest:
  #VillageWest  - 2
    show bg VillageWest  with fade
    "Now arriving at...VillageWest"
    
    return
#-------------------------------------------------------------    
    
label lbl_locations_Belgran:
  #Belgran      - 3
    show bg Belgran with fade
    "Now arriving at...Belgran"
    call screen Town2Map_Screen()
    
    #"Now arriving at...[_return]"
    call expression "lbl_locations_Belgran_" + str(_return) from _call_expression_1
    menu:
      "Go somewhere else in Town?":
        jump lbl_locations_Belgran
      "Leave":
        pass
    return
    
label lbl_locations_Belgran_1:
  #Belgran      - 3
    show bg Belgran with fade
    "Now arriving at...Location 1 in Belgran"    
    return
    
label lbl_locations_Belgran_2:
  #Belgran      - 3
    show bg Belgran with fade
    "Now arriving at...Location 2 in Belgran"    
    return
    
label lbl_locations_Belgran_3:
  #Belgran      - 3
    show bg Belgran with fade
    "Now arriving at...Location 3 in Belgran"    
    return
    
#-------------------------------------------------------------    
label lbl_locations_VillageEast:
  #VillageEast  - 4
    show bg VillageEast with fade
    "Now arriving at...VillageEast"
    
    return
#-------------------------------------------------------------    

label lbl_locations_ForestFort:
  #ForestFort   - 5
    show bg ForestFort with fade
    "Now arriving at...ForestFort"
    
    return
#-------------------------------------------------------------    
    
label lbl_locations_LyrTaer:
  #LyrTaer      - 6
    show bg LyrTaer with fade
    "Now arriving at...LyrTaer"
    call screen LyrTaerMap_Screen()
    
    #"Now arriving at...[_return]"
    #call expression "lbl_locations_LyrTaer_" + str(_return) from _call_expression_2
    call expression "lbl_locations_" + str(_return) from _call_expression_2
    
    #menu:
    #  "Go somewhere else in Town?":
    #    jump lbl_locations_LyrTaer
    #  "Leave":
    #    pass
    return
    
label lbl_locations_LyrTaer_1:
  #LyrTaer      - 6
    show bg LyrTaer with fade
    "Now arriving at...Location 1 in LyrTaer"    
    return
    
label lbl_locations_LyrTaer_2:
  #LyrTaer      - 6
    show bg LyrTaer with fade
    "Now arriving at...Location 2 in LyrTaer"    
    return
    
label lbl_locations_LyrTaer_3:
  #LyrTaer      - 6
    show bg LyrTaer with fade
    "Now arriving at...Location 3 in LyrTaer"    
    return
    
label lbl_locations_LyrTaer_4:
label lbl_locations_LyrTaer_5:
label lbl_locations_LyrTaer_6:
label lbl_locations_LyrTaer_7:
label lbl_locations_LyrTaer_8:
  #LyrTaer      - 6
    show bg LyrTaer with fade
    "Now arriving at...Location 3 in LyrTaer"    
    return
    
    
label lbl_locations_LyrTaer_Palace:
    "Now arriving somewhere in LyrTaer...Palace"    
    return
label lbl_locations_LyrTaer_Inn:
    "Now arriving somewhere in LyrTaer...Inn"    
    return
label lbl_locations_LyrTaer_Shop:
    "Now arriving somewhere in LyrTaer...Shop"    
    return
label lbl_locations_LyrTaer_MagesGuild:
    "Now arriving somewhere in LyrTaer...MagesGuild"    
    return
label lbl_locations_LyrTaer_WarriorsGuild:
    "Now arriving somewhere in LyrTaer...WarriorsGuild"    
    return
label lbl_locations_LyrTaer_Library:
    "Now arriving somewhere in LyrTaer...Library"    
    return
label lbl_locations_LyrTaer_ArtSchool:
    "Now arriving somewhere in LyrTaer...ArtSchool"    
    return
label lbl_locations_LyrTaer_Prison:
    "Now arriving somewhere in LyrTaer...Prison"    
    return
label lbl_locations_LyrTaer_MainSquare:
    "Now arriving somewhere in LyrTaer...MainSquare"    
    return
    
    
    
#-------------------------------------------------------------    
    
    
label lbl_locations_YourHouse:
  #YourHouse    - 7
    show bg YourHouse with fade
    "Now arriving at...YourHouse"
    
    return
#-------------------------------------------------------------    
    
    
label lbl_locations_SacredGrove:
  #YourHouse    - 8
    show bg SacredGrove with fade
    "Now arriving at...SacredGrove"
    
    return
#-------------------------------------------------------------    
    


    
label lbl_calendarTest:
        
    $RandomiseHoroscopeList()
    show screen DateDisplay_Screen()

    e "Initial Date."
    $SetDate(9023, 2, 22)
    e "SetDate(9023, 2, 22)"
    $SetDate(9027, 9, 40)
    e "SetDate(9027, 9, 40)"
    $SetDate(9023, 7, 32)
    e "SetDate(9023, 7, 22)"
    $SetDate(9023, 1, 3)
    e "SetDate(9023, 1, 3)"
    
    $SetDate(9023, 1, 1)
    e "Now lets step through"
    $AddDay(1)
    e "AddDay(1)"
    $AddDay(1)
    e "AddDay(1)"
    $AddDay(1)
    e "AddDay(1)"
    $AddDay(1)
    e "AddDay(1)"
    $AddDay(1)
    e "AddDay(1)"
    $AddDay(1)
    e "AddDay(1)"
    $AddDay(1)
    e "AddDay(1)"
    $AddDay(1)
    e "AddDay(1)"
    $AddDay(2)
    e "AddDay(2)"
    $AddDay(3)
    e "AddDay(3)"
    $AddDay(4)
    e "AddDay(4)"
    $AddMonth(1)
    e "AddMonth(1)"
    $AddMonth(1)
    e "AddMonth(1)"
    $AddMonth(1)
    e "AddMonth(1)"
    $AddMonth(1)
    e "AddMonth(1)"
    $AddMonth(1)
    e "AddMonth(1)"
    $AddMonth(1)
    e "AddMonth(1)"
    $AddMonth(1)
    e "AddMonth(1)"
    $AddMonth(2)
    e "AddMonth(2)"
    $AddMonth(3)
    e "AddMonth(3)"
    $AddWeek(1)
    e "AddWeek(1)"
    $AddWeek(1)
    e "AddWeek(1)"
    $AddWeek(1)
    e "AddWeek(1)"
    $AddWeek(1)
    e "AddWeek(1)"
    $AddWeek(1)
    e "AddWeek(1)"
    $AddWeek(2)
    e "AddWeek(2)"
    $AddWeek(3)
    e "AddWeek(3)"
    $AddWeek(4)
    e "AddWeek(4)"
    
    
    "Thats all folks"
    hide screen DateDisplay_Screen
    jump start
    return
    
    
    
label lbl_indicatorTest:
    $reflexes = 0
    $strength = 0
    $intelligence = 0
    $stat = 0
    menu:
      "Test Reflexes Fail":
        $reflexes = 10
        $show_test('Reflexes',reflexes>=20)
      "Test Reflexes Pass":
        $reflexes = 20
        $show_test('Reflexes',reflexes>=20)
          
      "Test Strength Fail":
        $strength = 10          
        $show_test('Strength',strength>=20)        
      "Test Strength Pass":
        $strength = 20
        $show_test('Strength',strength>=20)    
          
      "Test Intelligence Fail":
        $intelligence = 10             
        $show_test('Intelligence',intelligence>=20)       
      "Test Intelligence Pass":
        $intelligence = 20
        $show_test('Intelligence',intelligence>=20)    
        
      "Test Indicator during script test":
        jump lbl_indicatorTest2    
        
      "Stop Test":
        jump start
    
    "Stat check..."
    jump lbl_indicatorTest    
    return
    
label lbl_indicatorTest2:
    $reflexes = 0
    $strength = 0
    $intelligence = 0
    menu:
      "My main skill is..."
      "Reflexes":
        $reflexes = 20
      "Strength":
        $strength = 20
      "Intelligence":
        $intelligence = 20
      
    "I was walking along when suddenly..."
    "I boulder fell towards me."
    
    if show_test('Reflexes',reflexes>=20):
      "Luckily, I dodged it like a pro."
    else:
      "Unfortunatly i was unable to dodge."
      
      "I tried to catch the boulder instead"
      if show_test('Strength',strength>=20):
        "I caught and deflected the boulder and avoided getting hurt."
      else:
        "It was heaver than id expected so i was unable to catch it."
      "Luckily, I didn't take any serious damage."
      
    "It wasn't long after that when i came across a crossroads with a sweet smell comming from the left path."
    "I recognised the smell as the Jam from the town i passed through earlier."
    
    if show_test('Intelligence',intelligence>=20):
      "Theres no reason for there to be this strong smell of jam out here, especially since i can't see or hear any other people around that might be having a sandwich."
      "I better take the other path to be safe."
    else:
      "By the time i realised it was a trap it was too late."
    


    jump lbl_indicatorTest    
    return
    
label lbl_activitiesTest:
    show screen DateDisplay_Screen()
    call screen AvailableActivities_Screen()
    
    if _return == "Map":
        jump lbl_mapTest
    
    if _return[0] == "Job":
      "Looks like ill be working as a [_return[1]]."
    
    if _return[0] == "Class":
      "Looks like ill be studying [_return[1]]."
    "..."
    $ randomnum = renpy.random.randint(1,20) 
    
    if show_test('Luck',randomnum>=10):
      "How lucky, they noticed what a good job im doing."
    else:
      "How unlucky, they noticed my mistake, this is sure to reflect badly on me."
    
    
    $AddWeek(1)
    
    "Well that was fun, what next?"
    jump lbl_activitiesTest    
    
    return
  
  