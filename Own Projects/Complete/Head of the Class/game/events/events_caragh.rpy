
init:
  #event flags
  $Caragh_flag_arcs_completed = 0
  $Caragh_lonely_completed = False
  #I think the above flag should be in the main file?


label lbl_get_event_caragh_evening_events:
  $random_event = "None"

  $ randomnum = renpy.random.randint(0, 5)
  if randomnum < 3:
    $kidArcsComplete = 0
    if Craig_Arc_CurrentEvent == 5:
      $kidArcsComplete += 1
    if Hecate_Arc_CurrentEvent == 8:
      $kidArcsComplete += 1
    if Sanura_Arc_CurrentEvent == 9:
      $kidArcsComplete += 1
    if random_event == "None" and kidArcsComplete == 0 and Caragh_flag_arcs_completed == 0 and current_day > 10:
      #Dealing with Kids 00 After Week 1 + Before finishing any arcs + Not Relax during Evening
      $random_event = "lbl_event_caragh_kids_0"

    if random_event == "None" and kidArcsComplete == 1 and Caragh_flag_arcs_completed == 1 and current_day > 15:
      #Dealing with Kids 01 Arcs Done: 1 Kid
      $random_event = "lbl_event_caragh_kids_1"

    if random_event == "None" and kidArcsComplete == 2 and Caragh_flag_arcs_completed == 2 and current_day > 20:
      #Dealing with Kids 02 Arcs Done: 2 Kids
      $random_event = "lbl_event_caragh_kids_2"

    if random_event == "None" and kidArcsComplete == 3 and Caragh_flag_arcs_completed == 3 and current_day > 20:
      #Dealing with Kids 03 Arcs Done: 3 Kids
      $random_event = "lbl_event_caragh_kids_3"

    if random_event == "None" and Caragh_lonely_completed == False and Bahini_Arc_CurrentVisit < 1 and current_day > 20:
      #Bored or LonelyTriggers on Week 3 if player hasn't visited Bahini yet
      $random_event = "lbl_event_caragh_lonely"
  
  if not random_event == "None":
    call expression random_event from _call_expression_29 
  
  return 
  
  #CARAGH EVENING EVENTS
label lbl_event_caragh_kids_0:
  #Dealing with Kids 00 After Week 1 + Before finishing any arcs + Not Relax during Evening
  scene bg room night with dissolve
  play music music_bedroom
  show Caragh content with dissolve
  Caragh "Aah, I can finally relax. No kids to teach and no more classes to plan. "
  Caragh "I've worked with teenagers for years, but kids? "
  show Caragh mad with dissolve
  Caragh "Kids are tiring. There's so much hard work. One wrong word or move and the whole day's wasted. They won't be learning anything."
  Caragh "I miss teaching teenagers, in spite of all the headaches they've given me."
  show Caragh sad with dissolve
  Caragh "Enough, Caragh! Don't think about work and just breathe. Relax."
  $Caragh_flag_arcs_completed = 1
  return #END SCENE

label lbl_event_caragh_kids_1:
  #Dealing with Kids 01 Arcs Done: 1 Kid
  scene bg room night with dissolve
  play music music_bedroom
  Caragh "One special kid settled and two more to go."
  Caragh "I might've had to work my tail off for the past week or so but it feels so rewarding."
  Caragh "It feels so nice when I can help. Teenagers have so much more complex problems and families."
  Caragh "It's not a bad feeling."
  $Caragh_flag_arcs_completed = 2
  return #END SCENE

label lbl_event_caragh_kids_2:
  #Dealing with Kids 02 Arcs Done: 2 Kids
  scene bg room night with dissolve
  play music music_bedroom
  show Caragh happy with dissolve
  Caragh "Working with kids isn't as bad as I thought."
  Caragh "From the recent homework answers, I think I'm actually making good progress. They've improved quite a bit."
  show Caragh content with dissolve
  Caragh "The kids might all pass at this rate."
  $Caragh_flag_arcs_completed = 3
  return #END SCENE

label lbl_event_caragh_kids_3:
  #Dealing with Kids 03 Arcs Done: 3 Kids
  scene bg room night with dissolve
  play music music_bedroom
  show Caragh happy with dissolve
  Caragh "All three of the special kids are doing okay now in their classes."
  Caragh "This has been the most rewarding month I've ever experienced in all the years I've worked as a teacher."
  show Caragh content with dissolve
  Caragh "Maybe this school's not bad. Maybe kids aren't that bad. Maybe it'd be nice to keep teaching at this school instead of moving around all the time."
  Caragh "Maybe..."
  $Caragh_flag_arcs_completed = 4
  return #END SCENE
  #END OF DEALING WITH KIDS

label lbl_event_caragh_lonely:
  #Bored or LonelyTriggers on Week 3 if player hasn't visited Bahini yet
  scene bg room night with dissolve
  play music music_bedroom
  show Caragh content with dissolve
  Caragh "Another quiet evening. No colleagues, no kids, no work. It's only just me and me alone. I love it."
  Caragh "..."
  show Caragh sad with dissolve
  Caragh "Peace is rather boring. "
  Caragh "It's too quiet here. I wish there was someone I could talk to, someone I could laugh with."
  Caragh "Will there ever be a day when that wish will come true?"
  $Caragh_lonely_completed = False
  return #END SCENE
  #END OF CARAGH EVENING EVENTS
  
label lbl_event_caragh_stress_faint:
  stop music
  show Caragh surprise with dissolve
  Caragh "Wait... What did I say?"  
  Caragh "I feel...faint. I... "  
  scene bg black with dissolve
  show bg classroom empty
  play music music_quiet
  show Caragh sad with dissolve
  Caragh "\"Ugh...\""  
  show Nyx sad with dissolve
  Nyx "\"You worried everyone, Caragh. The kids were all panicking.\""  
  show Nyx huh with dissolve
  Nyx "\"The kids' grades are important but you shouldn't overwork yourself.\""  
  show Nyx happy with dissolve 
  Nyx "\"I've found someone to take care of the kids for this period. Don't worry about them. Get some rest first.\""   
  Nyx "\"I look forward to seeing you on your feet once more.\"" 
  show Caragh content with dissolve 
  Caragh "\"Thanks, Nyx.\""   
  Description "I spend the rest of the period recovering from my blackout." 
  call update_stress(-20) from _call_update_stress_23
  return