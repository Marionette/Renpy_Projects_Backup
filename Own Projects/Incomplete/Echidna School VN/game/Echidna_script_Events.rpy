init:
  #Define event lists
  $EventLabels_Morning = ["lbl_morning1", "lbl_morning2", "lbl_morning3", "lbl_morningChainChoice"]
  $EventLabels_FirstPeriod = ["lbl_FP1", "lbl_FP2", "lbl_FP3" ]
  $EventLabels_Lunch = ["lbl_lunch1", "lbl_lunch2", "lbl_lunch3"]
  $EventLabels_SecondPeriod = ["lbl_SP1", "lbl_SP2", "lbl_SP3" ]
  $EventLabels_AfterSchool = ["lbl_afterSchool1", "lbl_afterSchool2", "lbl_afterSchool3", "lbl_afterSchoolChoice" ]
  $EventLabels_Evening = ["lbl_evening1", "lbl_evening2", "lbl_evening3" ]
  
  #NoSchool_
  $EventLabels_NoSchool_Morning = ["lbl_noschool_morning1"]
  $EventLabels_NoSchool_Noon = ["lbl_noschool_noon1"]
  $EventLabels_NoSchool_Evening = ["lbl_noschool_evening1"]
  
  
  $EventCount_Morning = 4
  $EventCount_FirstPeriod = 3
  $EventCount_Lunch = 3
  $EventCount_SecondPeriod = 3
  $EventCount_AfterSchool = 4
  $EventCount_Evening = 3
  
  $EventCount_NoSchool_Morning = 1
  $EventCount_NoSchool_Noon = 1
  $EventCount_NoSchool_Evening = 1

  #Placemarkers for chained events
  $Event_morningChain_CurrentEvent = 0
  
#########################################################################  
#Events start here:
#
#Event Types:
# Special Day Event - Full day, Dependant on date
# 
# Birthday Event - Dependant on Date and location
# - Your Birthday events - Based on Date and relationships/locations
#
# Daily Events
# - Morning
# - First Period
# - Lunch
# - Second Period
# - After School
# - Evening

#label lbl_ChoooseEvent(time, )  


#--------------- Morning Events ----------------------
label lbl_Morning_rand:  
  $current_time = "Morning"
  show screen screen_TOD()
  pause 5
  hide screen screen_TOD
  $ randomnum = renpy.random.randint(1,EventCount_Morning) 
  call expression EventLabels_Morning[randomnum-1] from _call_expression
  return
  
label lbl_morning_default:
  e "Nothing happens"
  return

label lbl_morning1:
  #"First morning"
  e "Nothing happens"
  return
  
label lbl_morning2:
  #"Second morning"
  e "Oh i woke up early.."
  return
  
label lbl_morning3:
  #"Third morning"
  e "Oh Shi... i'm late!"
  return
  
#-------------chain event test ----------------
label lbl_morningChainChoice:
  $Event_morningChain_EventsCount = 5
  $Event_morningChain_EventsList = ["lbl_morningChain1", "lbl_morningChain2", "lbl_morningChain3", "lbl_morningChain4", "lbl_morningChain5"]
  
  e "lbl_morningChainChoice!"
  if ((Event_morningChain_CurrentEvent >= 0) and (Event_morningChain_CurrentEvent < Event_morningChain_EventsCount)):
    call expression Event_morningChain_EventsList[Event_morningChain_CurrentEvent] from _call_expression_0
  else:
    jump lbl_morning_default
    
  return
  
label lbl_morningChain1:
  e "Huh? Whats this?"
  e "EventChain1"
  $ Event_morningChain_CurrentEvent = 1
  return
  
label lbl_morningChain2:
  e "Huh? Whats this again?"
  e "EventChain2"
  $ Event_morningChain_CurrentEvent = 2
  return
  
label lbl_morningChain3:
  e "Huh? Whats this for a third time?"
  e "EventChain3"
  $ Event_morningChain_CurrentEvent = 3
  return
  
label lbl_morningChain4:
  e "Im pretty bored of this now."
  e "EventChain4"
  $ Event_morningChain_CurrentEvent = 4
  return
  
label lbl_morningChain5:
  e "Oh, i guess its over now."
  e "EventChain5"
  $ Event_morningChain_CurrentEvent = 5
  return
#-------------chain event test end----------------
  
#--------------- FirstPeriod Events ----------------------
label lbl_FirstPeriod_rand:  
  $current_time = "First Period"
  show screen screen_TOD()
  pause 5
  hide screen screen_TOD
  $ randomnum = renpy.random.randint(1,EventCount_FirstPeriod) 
  call expression EventLabels_FirstPeriod[randomnum-1] from _call_expression_1
  
  if (_return == 1):
    #"Have class now"
    pass
  else:
    #"This has gone differently than i imagined..."
    pass
  
  call lbl_stdClassEvent
  
  "Class is over."
  
  return
  
label lbl_FP1:
  #"First FP"
  e "Nothing happens"
  return 1
  
label lbl_FP2:
  #"Second FP"
  e "Someone forgot their homework..."
  return 2
  
label lbl_FP3:
  #"Third FP"
  e "I forgot my notes..."
  return 3
  
  
label lbl_stdClassEvent:
  #$current_subject = renpy.random.randint(0,5)
  #$labelstring = "lbl_%s_ClassEvent"%AvailableClasses[current_subject]
  
  $period = 1
  if current_time == "Second Period":
    $period = 2
    
  $day = weekDay(current_year, current_month+1, current_date )[0] - 1
  $current_subject = GetTechingSubject(day, period)
  
  $labelstring = "lbl_%s_ClassEvent"%GetTechingSubject(day, period)
  "lbl_stdClassEvent - [day], [period] = [current_subject] - [labelstring]"
  
  if (current_subject == '='):
    "You shoudlnt be seeing this. Teaching attempt on an invalid day. Events should override this possibility in the final build."
  else:
    call expression labelstring
  
  return
  
  
#--------------- Standard Class Events ----------------------
label lbl_English_ClassEvent:
  "I taught some English."
  $ApplyTeaching("English")
  
  return
  
label lbl_Science_ClassEvent:
  "I taught some Science."
  $ApplyTeaching("Science")
  return
  
label lbl_Maths_ClassEvent:
  "I taught some Maths."
  $ApplyTeaching("Maths")
  return
  
label lbl_Art_ClassEvent:
  "I taught some Art."
  $ApplyTeaching("Art")
  return
  
label lbl_Music_ClassEvent:
  "I taught some Music."
  $ApplyTeaching("Music")
  return
  
label lbl_PE_ClassEvent:
  "I taught some Pys Ed."
  $ApplyTeaching("PE")
  return
  
#--------------- Lunch Events ----------------------
label lbl_Lunch_rand:  
  $current_time = "Lunch"
  show screen screen_TOD()
  pause 5
  hide screen screen_TOD
  $ randomnum = renpy.random.randint(1,EventCount_Lunch) 
  call expression EventLabels_Lunch[randomnum-1] from _call_expression_2
  
  return
  
label lbl_lunch1:
  #"First lunch"
  #e "Nothing happens"
  
  e "Where should i eat lunch?"
  call screen map_school
  
  $res = _return
  
  if (res == "canteen"):
      e "Eating lunch in the Canteen. Brings back memories."
  if (res == "classA"):
      e "Lets join Class A for lunch!"
  if (res == "classB"):
      e "Lets join Class B for lunch!"
  if (res == "classC"):
      e "Lets join Class C for lunch!"
  if (res == "hallway"):
      e "But if i eat in the hallway ill be in peoples way..."
  if (res == "office"):
      e "I'd join the Headmistress for lunch...if she didn't scare the life outta me."
  if (res == "outside"):
      e "Its a lovely day, maybe ill eat outside..."
  if (res == "playground"):
      e "How about in the playground, i can keep an eye on the kids while i eat."
  if (res == "staffroom"):
      e "In the staffroom, it's usually pretty quiet"
  if (res == "storage"):
      e "How about the storage shed? Wait is it even open?"
  if (res == "toilets"):
      e "The Toilet? ...Maybe not."
      #return
  #jump lbl_lunch1        
  return
  
label lbl_lunch2:
  #"Second lunch"
  e "Im so tired. Maybe ill sleep this time..."
  return
  
label lbl_lunch3:
  #"Third lunch"
  e "I forgot my lunch..."
  return
  
#--------------- SecondPeriod Events ----------------------
label lbl_SecondPeriod_rand:  
  $current_time = "Second Period"
  show screen screen_TOD()
  pause 5
  hide screen screen_TOD
  $ randomnum = renpy.random.randint(1,EventCount_SecondPeriod) 
  call expression EventLabels_SecondPeriod[randomnum-1] from _call_expression_3
  
  call lbl_stdClassEvent
  
  "Class is over."
  
  return
  
label lbl_SP1:
  #"First SP"
  e "Nothing happens"
  return
  
label lbl_SP2:
  #"Second SP"
  e "Someone forgot their homework..."
  return
  
label lbl_SP3:
  #"Third SP"
  e "I forgot my notes..."
  return
  
#--------------- After School Events ----------------------
label lbl_AfterSchool_rand:  
  $current_time = "After School"
  show screen screen_TOD()
  pause 5
  hide screen screen_TOD
  $ randomnum = renpy.random.randint(1,EventCount_AfterSchool) 
  call expression EventLabels_AfterSchool[randomnum-1] from _call_expression_4
  return
  
label lbl_afterSchool1:
  #"First after School"
  e "Nothing happens"
  return
  
label lbl_afterSchool2:
  #"Second after School"
  e "Nuts its raining. And I didn't bring an umbrella."
  return
  
label lbl_afterSchool3:
  #"Third after School"
  e "Oh a stray kitty. Here kitty kitty... It ran away."
  return
  
label lbl_afterSchoolChoice:
  #"Third after School"
  e "School is over. What should i do now?"
  menu:
    "What should i do now?"
    "Go home":
      e "Guess ill just go home then."
    "After School club":
      e "I'll just see how the after school clubs are doing."
    "Eat out":
      e "Wonder if theres anywhere i can get some food."
    "Visit Somewhere":
      e "Maybe ill check out the sights"
    "Go home and eat":
      e "Guess ill just go home and eat then."
    "Visit someone":
      e "I'll just see how 'Someone' is doing."
  return
#--------------- Evening Events ----------------------
  
label lbl_Evening_rand:  
  $current_time = "Evening"
  show screen screen_TOD()
  pause 5
  hide screen screen_TOD
  $ randomnum = renpy.random.randint(1,EventCount_Evening) 
  call expression EventLabels_Evening[randomnum-1] from _call_expression_5
  return
  
label lbl_evening1:
  #"First evening"
  e "Nothing happens"
  return
  
label lbl_evening2:
  #"Second evening"
  e "I should probably head to bed soon..."
  return
  
label lbl_evening3:
  #"Third evening"
  e "Lets just watch one more episode before bed..."
  return
  
#--------------- Other ----------------------
  
  
#--------------- NoSchool Morning ----------------------
label lbl_NoSchool_Morning_rand:  
  $current_time = "Morning"
  show screen screen_TOD()
  pause 5
  hide screen screen_TOD
  $ randomnum = renpy.random.randint(1,EventCount_NoSchool_Morning) 
  call expression EventLabels_NoSchool_Morning[randomnum-1] from _call_expression_6
  return
  
label lbl_noschool_morning1:
  #"First NoSchool Morning"
  e "Nothing happens"
  return
  
  
#--------------- NoSchool Noon ----------------------
label lbl_NoSchool_Noon_rand:  
  $current_time = "Noon"
  show screen screen_TOD()
  pause 5
  hide screen screen_TOD
  $ randomnum = renpy.random.randint(1,EventCount_NoSchool_Noon) 
  call expression EventLabels_NoSchool_Noon[randomnum-1] from _call_expression_7
  return
  
label lbl_noschool_noon1:
  #"First NoSchool Noon"
  e "Nothing happens"
  return
  
  
#--------------- NoSchool Evening ----------------------
label lbl_NoSchool_Evening_rand:  
  $current_time = "Evening"
  show screen screen_TOD()
  pause 5
  hide screen screen_TOD
  $ randomnum = renpy.random.randint(1,EventCount_NoSchool_Evening) 
  call expression EventLabels_NoSchool_Evening[randomnum-1] from _call_expression_8
  return
  
label lbl_noschool_evening1:
  #"First NoSchool Evening"
  e "Nothing happens"
  return
  
  