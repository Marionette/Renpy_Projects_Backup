init:
  #variables
  default morning_class = ""
  default evening_class = ""
  default after_school_tutoring = "None"

  default class_random_event = "None"

  #event flags
  default Caragh_Arc_CurrentEvent = 0
  default Bahini_Arc_CurrentEvent = 0
  default Nyx_Arc_CurrentEvent = 0
  default Jo_Arc_CurrentEvent = 0

  default Jo_Arc_LearnedAboutJo = False

  default Craig_Cram_Partner_01 = ""
  default Craig_Cram_Partner_02 = ""
  default Craig_Cram_Partner_Correct = False

  default Hecate_Cram_Partner_01 = ""
  default Hecate_Cram_Partner_02 = ""
  default Hecate_Cram_Partner_Correct = False

  default Sanura_Cram_Partner_01 = ""
  default Sanura_Cram_Partner_02 = ""
  default Sanura_Cram_Partner_Correct = False

  default Una_Arc_Encountered = False

  default List_Random_Event_Messages = []


  $List_Students_Side = ["Achilles, Adonis, Atlas",
                         "Athan ",
                         "Bestia",

                         "Dougal",
                         "Fayette",
                         "Florence",

                         "Juniper",
                         "Lateef",
                         "McCoy",
                         "Roark",
                         "Rudolph",

                         "Sophia",
                         "Xisreia"]


  #Other students list
  $List_Students_Side = [["Achilles, Adonis, Atlas", "Cerberus"],
                         ["Athan ",     "Vampire"],
                         ["Bestia",     "Werewolf"],

                         ["Dougal",     "Jack O Lantern"],
                         ["Fayette",    "Fairy"],
                         ["Florence",   "Zombie"],

                         ["Juniper",    "Lamia"],
                         ["Lateef",     "Mummy"],
                         ["McCoy",      "Skeleton"],
                         ["Roark",      "Gargoyle"],
                         ["Rudolph",    "Yeti"],

                         ["Sophia",     "Ghost"],
                         ["Xisreia",  "Demon"]]

  $List_Students_Side2 = [ ["Achilles, Adonis, Atlas", "Male", "12", "Cerberus", "Excitable/Studious/Sleepy", "Has trouble getting along with themselves and avoiding distractions.", "PE/Literacy/Geography", ""],
                          ["Athan", "Male", "11", "Vampire", "Polite", "Apparently faints at the sight of blood.", "Science", "Math"],
                          ["Bestia", "Female", "12", "Werewolf", "Nerd", "Seems to have a fear of the dark.", "History", "Geography"],
                          #["Craig", "Male", "13", "Basilisk", "Shy", "Seems to be afraid to get close to people.", "Geography", "Art"],
                          ["Dougal", "Male", "12", "Jack o lantern", "Class clown", "Avoids emotions with humour.", "Languages", "Literacy"],
                          ["Fayette", "Female", "12", "Fairy", "Short fuse", "Wishes she were bigger.", "Literacy", "PE"],
                          ["Florence", "Female", "13", "Zombie", "Daydreamer", "Has a habit of forgetting things.", "Music", "History"],
                          #["Hecate", "Female", "12", "Witch", "Snarky/Aloof", "Seems more interested in Magic than studying.", "Science", "Math"],
                          ["Juniper", "Female", "12", "Lamia", "Tired/helpful", "Has trouble staying awake in class.", "History", "Geography"],
                          ["Lateef", "Male", "13", "Mummy", "haughty/posh", "Always exceptionally dressed, sometimes too exceptionally.", "Art", "History"],
                          ["McCoy", "None", "12", "Skeleton", "Comedian", "Wants to be funny but none of their jokes land.", "Literacy", "Languages"],
                          ["Roark", "None", "11", "Gargoyle", "Friendly", "Seems to struggle with fitting in with the boys or girls in the class.", "PE", "Art"],
                          ["Rudolph", "Male", "12", "Yeti", "Cuddly", "Seems to have some worries for the future.", "Literacy", "PE"],
                          #["Sanura", "Female", "11", "Sphinx", "Eager to please / Praise seeker", "Spends a lot of time trying to practice her riddles.", "Math", "Literacy"],
                          ["Sophia", "Female", "12", "Ghost", "Attention seeker", "Feels like she is always ignored.", "Art", "Music"],
                          ["Xisreia", "Female", "?(12)", "Demon", "Overly Proud", "Claims to have awoken after 5000 years and says everything is different now.", "Languages", "History"]]
                          
  default List_side_characters = []


label SetupSideCharacters:
  
  python:
    for character in List_Students_Side2:
      _character = CharacterClass()
      _character.SetCharacter(character[0], [2], character[1], [3], "Student", [6], [7], [4], [5])
      _character.SetMood(50)
      _character.RandomizeAllScores(50, 80)
      List_side_characters += [_character]
      
  return


##################### Character Specific Arc Events ##############################################


#--------------- Jo Events ----------------------
label lbl_event_visit_library:

  $random_event = "None"

  if random_event == "None" and Jo_Arc_CurrentEvent == 0 and Jo_Arc_LearnedAboutJo == False:
    #Meet Jo
    $random_event = "lbl_event_meet_jo"

  if random_event == "None" and Hecate_Arc_CurrentEvent == 1:
    # "Hecate's Route: Talk to Jo
    $random_event = "lbl_event_hecate_problem_tutoring_2"

  if random_event == "None" and Sanura_Arc_CurrentEvent == 6:
    #Ask Jo for a riddle book
    $random_event = "lbl_event_talk_jo_riddle_book"

  #if no story events try rolling a random event
  if random_event == "None":
    $ randomnum = renpy.random.randint(0, 5)
    if randomnum < 3 and Jo_Arc_LearnedAboutJo == True:
      $random_event = "lbl_event_talk_jo"
    else:
      $random_event = "lbl_event_library_empty"

  if not random_event == "None":
    call expression random_event from _call_expression

  return

label lbl_event_library_empty:
  show bg library
  Caragh "The library's empty. I'm not looking for anything special anyway."
  Caragh "Guess I'll just head home."
  $eveningTimeAvailable = True
  return

label lbl_event_meet_jo:
  #"TODO: You meet Jo, the invisible mute, for the first time. You find out they act as librarian and school councilor."
  show bg hallway
  Caragh "The library... Where is it again?"
  Caragh "I didn't have much paperwork to do today. I should have time to see what the library's like here."
  show Jo with dissolve
  Description "Suddenly, a mask floats before me."
  Caragh "\"Hi...?\""
  Description "The mask smiles and floats over to a doorway I had yet to peek into. Then, as if sensing my confusion, it bobs up and down. Somehow, it seems like it was beckoning me over."
  show Jo happy with dissolve
  Description "Curious, I walked over."
  show bg library with dissolve
  Description "Oh, this is the library."
  show Jo small with dissolve
  Description "The mask floats around into my sight again. It, somehow, raises a paper up for me to look at."
  Caragh "\"Jo...?\""
  Caragh "\"Oh! Your name is Jo?\""
  show Jo happy with dissolve
  Description "The mask nods."
  Caragh "\"Pleased to meet you, Jo. I'm guessing you're the librarian?\""
  Description "The mask nods again."
  Caragh "\"I'm, uh, looking for a book?\""
  hide Jo
  Description "The mask floats away into the shelves."
  Caragh "I guess I'm to follow it? Them?"
  Caragh "Oh well, at least I found the library."
  $Jo_Arc_CurrentEvent = 1
  $Jo_Arc_LearnedAboutJo = True
  return

label lbl_event_talk_jo_riddle_book:
  #Ask Jo for a riddle book
  if Jo_Arc_CurrentEvent == 1 or Hecate_Arc_CurrentEvent > 1:
      show bg library with dissolve
      show Jo
      Caragh "\"Hi, Jo.\""
  else:
      show bg hallway with dissolve
      Caragh "Where is this library?"
      show Jo small with dissolve
      Description "Out of nowhere, a mask pops into my view. Startled, I take a step back."
      Caragh "\"Oh, hi! You are...?\""
      show Jo happy with dissolve
      Description "The mask smiles and, somehow, raises a piece of paper up for me to look at. \"Jo\" is written on it."
      Description "It then floats over to a doorway I had yet to check out."
      show bg library with dissolve
      Description "It's the library."
      Caragh "\"Oh, you must be the librarian then. Jo, right?\""
      show Jo excited with dissolve
      Description "The mask bobs up and down in a nod."

  Caragh "\"I'm looking for a book on riddles.\""
  Caragh "\"I have this kid, Sanura. She's a sphinx who lives and breathes riddles.\""
  show Jo confused with dissolve
  Description "Jo tilts their head and pauses for a second. Then, it zooms away and disappears between the shelves."
  hide Jo with dissolve
  pause
  show Jo with dissolve
  Description "A few minutes later, Jo is back. They hand me a note before disappearing once more."
  hide Jo 
  Caragh "{i}The Whats, Whys and Hows of Riddles{/i}. That sounds like a good book. Let me look it up right now..."
  Description "In what seems like an hour, I scour through the entire internet, looking for the book Jo recommended. Nothing. Everywhere I looked, the book is sold out."
  Caragh "There's this one listing but it's going to take two whole months before it can reach us. That takes too long."
  show Jo happy with dissolve
  Description "Just as I'm about to give up, Jo floats back to me with a book in tow. They place it on the table in front of me, nod and leave."
  hide Jo
  Caragh "This is... This is the book I've been looking for! Oh, Jo, you are a hero!"
  Caragh "Oh, it's getting late. I should head back."
  Description "I quickly scribble out a thank-you note using one of the papers Jo used to communicate and walk out of the library."
  scene bg black with dissolve
  $Sanura_Arc_RiddleBookFound = True
  return

label lbl_event_talk_jo:
  Description "I spend some time chatting with Jo."
  Description "It's a one sided conversation but Jo would swap masks every so often in reaction to what's being said."
  Caragh "\"I hope I'm not bothering you.\""
  Jo "\"...\""
  Description "Jo's mask shakes to reassure me that I'm not bothering them."
  call update_stress(-10) from _call_update_stress
  Caragh "Something about talking with Jo is very relaxing. I find myself opening up much more than I usually would when talking to other people."
  return


#--------------- Nyx and Teachers' Lounge Events ----------------------

init:
  #event flags
  $Nyx_flag_seen_checkin_1 = False
  $Nyx_flag_seen_checkin_2 = False
  $Nyx_flag_seen_checkin_3 = False

label lbl_event_teachers_lounge:

  $random_event = "None"

  #if no story events try rolling a random event
  if random_event == "None":
    $ randomnum = renpy.random.randint(0, 5)
    if randomnum < 2:
      $random_event = "lbl_event_talk_una"
    elif randomnum < 4:
      $random_event = "lbl_event_talk_nyx"
    else:
      $random_event = "lbl_event_teachers_lounge_empty"

  if not random_event == "None":
    call expression random_event from _call_expression_1

  return

label lbl_event_teachers_lounge_empty:
  scene bg teachers lounge
  play music music_quiet
  Description "There doesn't seem to be anyone around today."
  Caragh "Guess I'll just head home."
  $eveningTimeAvailable = True
  return

#Una teachers' lounge event
label lbl_event_talk_una:
    scene bg teachers lounge
    play music music_quiet
    if Una_Arc_Encountered == False:
      Description "I walk into the teachers' lounge to find a Banshee enjoying a cup of coffee."
      Caragh "\"Hi, I'm Caragh, the new temp.\""
      Una "\"Oh, I've heard of you from Nyx. \""
      UnaLoud "\"I'm Una.\""
      UnaQuiet "\"Well? What do you think of your class?\""
      Description "Minutes fly by as I get to know Una."
      Caragh "\"It's getting late. I should go.\""
      UnaLoud "\"Okay. See you around.\""
      UnaQuiet "\"I'm often here, taking a break from life before I have to go back to my home and kids.\""
      $ Una_Arc_Encountered = True
      $ eveningTimeAvailable = False
      return
    elif Una_Arc_Encountered == True:
      Description "I walk into the teachers' lounge to find Una enjoying a cup of coffee."
      Caragh "\"Hi, Una.\""
      UnaLoud "\"Caragh, there you are!\""
      UnaQuiet "\"I was wondering when you'd be by. You're quite late today.\""
      UnaLoud "\"I've already gone through two cups of coffee!\""
      Description "I spend a relaxing hour or so catching up with Una."
      call update_stress(-10) from _call_update_stress_1
      Caragh "\"I don't know how you do it. You have so many kids to juggle.\""
      Una "\"Life is the best teacher.\""
      Caragh "\"Ah, your kids back home.\""
      Caragh "\"Oh, it's getting late. I should go.\""
      Una "\"See you around.\""
      $ eveningTimeAvailable = False
      return

#nyx encounter in teachers' lounge
label lbl_event_talk_nyx:
  scene bg teachers lounge
  play music music_quiet
  show Nyx mad with dissolve
  Description "I walk into the teachers' lounge to find Nyx working hard."
  Description "She is trying to work her way through what seems to be a mountain of paperwork."
  Caragh "I'd better not disturb her."
  Caragh "Guess I'll just head home."
  hide Nyx
  $eveningTimeAvailable = True
  return
## NO MAIN ARC

label lbl_get_event_nyx_checkin_events:
  $random_event = "None"

  $ randomnum = renpy.random.randint(0, 5)
  if randomnum < 3:
    if random_event == "None" and Nyx_flag_seen_checkin_1 == False and current_day > 10:
      #NYX EVENTS   AFTER WEEK 2 + RNG (MON-THURS)
      #Nyx Checkin 1
      $random_event = "lbl_event_nyx_checkin_1"

    if random_event == "None" and Nyx_flag_seen_checkin_2 == False and current_day > 15:
      #Nyx Checkin 2
      $random_event = "lbl_event_nyx_checkin_2"

    if random_event == "None" and Nyx_flag_seen_checkin_3 == False and current_day > 20:
      #Nyx Checkin 3
      $random_event = "lbl_event_nyx_checkin_3"

  return random_event

label lbl_event_nyx_checkin_1:
  #NYX EVENTS   AFTER WEEK 2 + RNG (MON-THURS)
  #Check-in 01
  show bg hallway
  play music music_school
  show Nyx happy with dissolve
  Description "I'm walking down the hallway when I meet Nyx with a large, swaying pile of papers in her arms."
  Nyx "\"Oh, Caragh. Hello.\""
  Caragh "\"Are you alright?\""
  Nyx "\"I'm, ah, good.\""
  show Nyx mad with dissolve
  Nyx "\"Papers, you are not allowed fall. No!\""
  Caragh "\"Let me help you with that.\""
  show Nyx happy with dissolve
  Nyx "\"Oh, thank you.\""
  Nyx "\"Now, tell me. How are things? Everything going well in class? The kids aren't giving you any trouble, are they?\""
  Caragh "\"The kids are behaving, as much as kids can.\""
  Nyx "\"Oh, yes. I know that feeling well.\""
  show Nyx mad with dissolve
  Nyx "\"Jonah. don't even think about pulling the fire alarm.\""
  show Nyx happy with dissolve
  Nyx "\"Ahem, as I was saying... Oh, we're here. That's fast.\""
  Nyx "\"Thank you so much for your help, Caragh. See you around.\""
  hide Nyx
  Caragh "\"See you.\""
  show Caragh surprise with dissolve
  Caragh "Whoa, her voice went from friendly to stern in a split second. She didn't even have to raise her voice to get that kid back off. Amazing.   "
  $Nyx_flag_seen_checkin_1 = True
  return #END SCENE

label lbl_event_nyx_checkin_2:
  #Check-in 02
  show bg hallway
  play music music_school
  show Nyx
  Nyx "\"Hello!\""
  Caragh "\"Nyx.\""
  show Nyx happy with dissolve
  Nyx "\"I heard from Bahini that you've been trying to help the kids with some issues. Everything going good?\""
  Caragh "\"Things are...progressing.\""
  Nyx "\"Ah, I know what you mean. Don't be too hard on yourself. You may be an experienced teacher but you're no miracle worker.\""
  show Nyx sad with dissolve
  Nyx "\"Don't stress yourself out. It's so hard to find good teachers who are willing to fully take on a class on such short notice.\""
  Caragh "\"I'll be sure not to.\""
  show Nyx mad with dissolve
  Nyx "\"Please do. I'm still busy looking for Mog's replacement.\""
  show Nyx happy with dissolve
  Nyx "\"Right. This is me. Take care.\""
  hide Nyx
  $Nyx_flag_seen_checkin_2 = True
  return #END SCENE

label lbl_event_nyx_checkin_3:
  #Check-in 03
  show bg hallway
  play music music_school
  show Nyx
  Nyx "\"Caragh, doing alright?\""
  Caragh "\"I'm okay.\""
  Nyx "\"Hang in there. We're nearly through the month. You've been doing okay so far.\""
  Caragh "\"Thank you.\""
  show Nyx huh with dissolve
  Nyx "\"Have you thought about what you'll be doing afterwards?\""
  Caragh "\"I'm still undecided myself.\""
  show Nyx happy with dissolve
  Nyx "\"Well, work hard and you might have an option open to you soon.\""
  hide Nyx
  Nyx "\"Ah, I have to go now. Good luck in the exams, Caragh.\""
  show Caragh surprise with dissolve
  Caragh "An option open to me soon...   "
  Caragh "Was she saying I could stay if my work impresses her?  "
  $Nyx_flag_seen_checkin_3 = True
  return #END SCENE
  #END OF NYX EVENTS


####################### Class Events #################################

#--------------- Exam Subjects ----------------------
label lbl_event_class_history:
  Caragh "I'm teaching History."
  #Random event if applicable
  if not class_random_event == "None" and EventTime == "During":
    call expression class_random_event from _call_expression_2
    Caragh "\"Alright, kids. Back to your seats.\""
  call update_score_all("History", 5) from _call_update_score_all
  call update_mood_all(-5) from _call_update_mood_all
  $renpy.pause(1.0)
  return

label lbl_event_class_science:
  Caragh "For this period, I'll be teaching Science."
  #Random event if applicable
  if not class_random_event == "None" and EventTime == "During":
    call expression class_random_event from _call_expression_3
    Caragh "\"Alright, kids. Back to your seats.\""
  call update_score_all("Science", 5) from _call_update_score_all_1
  call update_mood_all(-5) from _call_update_mood_all_1
  $renpy.pause(1.0)

  return

label lbl_event_class_math:
  Caragh "It's time to teach some Math."
  #Random event if applicable
  if not class_random_event == "None" and EventTime == "During":
    call expression class_random_event from _call_expression_4
    Caragh "\"Alright, kids. Back to your seats.\""
  call update_score_all("Math", 5) from _call_update_score_all_2
  call update_mood_all(-5) from _call_update_mood_all_2
  $renpy.pause(1.0)

  return

label lbl_event_class_literacy:
  Caragh "It's Literacy class now."
  #Random event if applicable
  if not class_random_event == "None" and EventTime == "During":
    call expression class_random_event from _call_expression_5
    Caragh "\"Alright, kids. Back to your seats.\""
  call update_score_all("Literacy", 5) from _call_update_score_all_3
  call update_mood_all(-5) from _call_update_mood_all_3
  $renpy.pause(1.0)

  return

label lbl_event_class_language:
  Caragh "Language class is scheduled for this period."
  #Random event if applicable
  if not class_random_event == "None" and EventTime == "During":
    call expression class_random_event from _call_expression_6
    Caragh "\"Alright, kids. Back to your seats.\""
  call update_score_all("Language", 5) from _call_update_score_all_4
  call update_mood_all(-5) from _call_update_mood_all_4
  $renpy.pause(1.0)
  return

label lbl_event_class_geography:
  Caragh "I'm teaching Geography!"
  #Random event if applicable
  if not class_random_event == "None" and EventTime == "During":
    call expression class_random_event from _call_expression_7
    Caragh "\"Alright, kids. Back to your seats.\""
  call update_score_all("Geography", 5) from _call_update_score_all_5
  call update_mood_all(-5) from _call_update_mood_all_5
  $renpy.pause(1.0)

  return

#--------------- Non-Exam Subjects ----------------------
label lbl_event_class_art:
  Caragh "\"Put away your books, kids. We're doing Art!\""
  #Random event if applicable
  if not class_random_event == "None" and EventTime == "During":
    call expression class_random_event from _call_expression_8
    Caragh "\"Alright, kids. Back to your seats.\""
  call update_mood_all(10) from _call_update_mood_all_6
  Description "Everyone seems to be in a better mood after that."

  return

label lbl_event_class_music:
  Caragh "Time to make some Music!"
  #Random event if applicable
  if not class_random_event == "None" and EventTime == "During":
    call expression class_random_event from _call_expression_9
    Caragh "\"Alright, kids. Back to your seats.\""
  call update_mood_all(10) from _call_update_mood_all_7
  Description "Everyone seems to be in a better mood after that."

  return

label lbl_event_class_physical_education:
  Caragh "\"Class, get changed. It's Physical Education class!\""
  #Random event if applicable
  if not class_random_event == "None" and EventTime == "During":
    call expression class_random_event from _call_expression_10
    Caragh "\"Alright, kids. Back to your seats.\""
  call update_mood_all(10) from _call_update_mood_all_8
  Description "Everyone seems to be in a better mood after that."

  return

####################### Time Of Day Events #################################

label lbl_event_time_morning:
  #Morning/Before class events
  call update_time("Morning") from _call_update_time
  scene bg room
  play music music_bedroom
  $random_event = "None"

  if random_event == "None" and Hecate_Arc_CurrentEvent == 6:
    # "Hecate's Route: Talk to Mother (Early Morning)"
    $random_event = "lbl_event_hecate_problem_tutoring_7"

  if random_event == "None" and Sanura_Arc_CurrentEvent == 4:
    #"Mom Phonecall - The Next Morning (Before Class) "
    $random_event = "lbl_event_sanura_problem_tutoring_4a"

  #if no story events try rolling a random event
  if random_event == "None":
    $ randomnum = renpy.random.randint(0, len(List_events_random_morning)*2)
    if randomnum < len(List_events_random_morning):
      $random_event = List_events_random_morning[randomnum]

  if not random_event == "None":
    call expression random_event from _call_expression_11
  else:
    "You wake up and make your way to work."

  return

label lbl_event_time_morning_class:
  call update_time("Morning Class") from _call_update_time_1
  scene bg classroom morning
  play music music_5c
  #Teach first class
  $EventTime = "None"
  $class_random_event = "None"
  #Story events override other events
  if class_random_event == "None" and Craig_Arc_CurrentEvent == 3:
    # "Craig's Route : Spectacles (Before Class)"
    $class_random_event = "lbl_event_craig_problem_tutoring_4"
    $EventTime = "Before"

  if class_random_event == "None" and Sanura_Arc_CurrentEvent == 1:
    # "Sanura's Route: Observation before Bahini Text (After Class Additional Text - Morning Class)"
    $class_random_event = "lbl_event_sanura_problem_tutoring_2a"
    $EventTime = "After"

  if class_random_event == "None" and Sanura_Arc_CurrentEvent == 7:
    # "Sanura's Route: Sanura's Practice (Lunch)"
    $class_random_event = "lbl_event_sanura_problem_tutoring_6"
    
  #stress wont stop main story parts from happening but will otherwise  
  if feature_unlock_penalty_stress:
    if Character_Caragh.Mood >= 100:
      $class_random_event = "lbl_event_caragh_stress_faint"
      $EventTime = "Instead"
      $RecordClassOutcome(morning_class, "I fainted from stress.")

  #if no story events try rolling a random event
  #add class-specific events to the list
  $random_event_list = List_events_random_class
  if morning_class == "Art":
    $random_event_list += List_events_random_art
  if morning_class == "Physical Education":
    $random_event_list += List_events_random_pe
  if morning_class == "Math":
    $random_event_list += List_events_random_math
  #all classes
  if class_random_event == "None":
    $ randomnum = renpy.random.randint(0, len(random_event_list)*2)
    if randomnum < len(random_event_list):
      $class_random_event = random_event_list[randomnum][0]
      $EventTime = random_event_list[randomnum][1]
    else:
      call lbl_get_event_nyx_checkin_events from _call_lbl_get_event_nyx_checkin_events
      $class_random_event = _return
      if not class_random_event == "None":
        $EventTime = "After"


  if EventTime == "Before":
    call expression class_random_event from _call_expression_12

  #if EventTime == "During":
  #  $class_random_event = List_events_random_class[randomnum][0]

  if EventTime == "Instead":
    call expression class_random_event from _call_expression_13
  else:
    Caragh "Now, what's my morning class today?"
    Caragh "Ah, it's [morning_class]."
    call expression "lbl_event_class_" + morning_class.lower().replace(" ", "_") from _call_expression_14
    $RecordClassOutcome(morning_class, "Success")
    call update_stress(5) from _call_update_stress_24

  if EventTime == "After":
    call expression class_random_event from _call_expression_15

  return

label lbl_event_time_lunch:
  call update_time("Lunch") from _call_update_time_2
  #TODO replace with canteen or eating space?
  scene bg cafeteria with fade
  play music music_school
  #Lunch events
  $random_event = "None"

  if random_event == "None" and Hecate_Arc_CurrentEvent == 7:
    # "Hecate's Route: Talk to Mother (Early Morning)"
    $random_event = "lbl_event_hecate_problem_tutoring_8"


  #if no story events try rolling a random event
  if random_event == "None":
    $ randomnum = renpy.random.randint(0, len(List_events_random_lunch)*2)
    if randomnum < len(List_events_random_lunch):
      $random_event = List_events_random_lunch[randomnum]

  if not random_event == "None":
    call expression random_event from _call_expression_16
  else:
    Caragh "At last, some peace."
    #Caragh "Why did I become a teacher again? I don't even like talking to other people."
    play sound sfx_schoolbell
    Caragh "Well, that's the bell. Back to the fray I go."

  return

label lbl_event_time_afternoon_class:
  call update_time("Afternoon Class") from _call_update_time_3
  scene bg classroom afternoon with fade
  play music music_5c
  #Teach second class
  $EventTime = "None"
  $class_random_event = "None"

  if class_random_event == "None" and Sanura_Arc_CurrentEvent == 2 and Sanura_Arc_Distracted_1:
    # "Sanura's Route: Observation before Bahini Text (After Class Additional Text - Morning Class)"
    $class_random_event = "lbl_event_sanura_problem_tutoring_2b"
    $EventTime = "During"

  if class_random_event == "None" and Sanura_Arc_CurrentEvent == 5 and Sanura_Arc_MorningBreak:
  #" After Lunch-Before Afternoon Class "
    $class_random_event = "lbl_event_sanura_problem_tutoring_4b"
    $EventTime = "Before"
    
  if class_random_event == "None" and Sanura_Arc_CurrentEvent == 7:
    $class_random_event = "lbl_event_sanura_problem_tutoring_6"
    $EventTime = "After"
  if class_random_event == "None" and Sanura_Arc_CurrentEvent == 8:
    $class_random_event = "lbl_event_sanura_problem_tutoring_7"
    $EventTime = "After"
    
    
  #stress wont stop main story parts from happening but will otherwise  
  if feature_unlock_penalty_stress:
    if Character_Caragh.Mood >= 100:
      $class_random_event = "lbl_event_caragh_stress_faint"
      $EventTime = "Instead"
      $RecordClassOutcome(afternoon_class, "I fainted from stress.")

  #if no story events try rolling a random event
  #add class-specific events to the list
  $random_event_list = List_events_random_class
  if afternoon_class == "Art":
    $random_event_list += List_events_random_art
  if afternoon_class == "Physical Education":
    $random_event_list += List_events_random_pe
  if afternoon_class == "Math":
    $random_event_list += List_events_random_math
    # all classes
  if class_random_event == "None":
    $ randomnum = renpy.random.randint(0, len(random_event_list)*2)
    if randomnum < len(random_event_list):
      $class_random_event = random_event_list[randomnum][0]
      $EventTime = random_event_list[randomnum][1]
    else:
      call lbl_get_event_nyx_checkin_events from _call_lbl_get_event_nyx_checkin_events_1
      $class_random_event = _return
      if not class_random_event == "None":
        $EventTime = "After"

  if EventTime == "Before":
    call expression class_random_event from _call_expression_17

  #if EventTime == "During":

  if EventTime == "Instead":
    call expression class_random_event from _call_expression_18
  else:
    Caragh "Now, what am I teaching in the afternoon today?"
    Caragh "Ah, it's [afternoon_class]."
    call expression "lbl_event_class_" + afternoon_class.lower().replace(" ", "_") from _call_expression_19
    $RecordClassOutcome(afternoon_class, "Success")
    #Degredation only applied after afternoon classes
    $ApplyScoreDegredation()
    call update_stress(5) from _call_update_stress_25

  if EventTime == "After":
    call expression class_random_event from _call_expression_20

  return

label lbl_event_time_after_school:
  call update_time("After School") from _call_update_time_4
  scene bg classroom afternoon
  play music music_school
  #Choose to hang out with one of the students / Talk to Bahini / Head home.
  Caragh "Finally, classes are over."

  $eveningTimeAvailable = False
  #TODO Swap for more generic tutoring event label?
  if not after_school_tutoring == "Free Time":
    call expression "lbl_event_tutoring_"+after_school_tutoring.lower() from _call_expression_21
  else:
    menu:
      Caragh "What should I do now?"
      #"Ask Craig to hang back after class.":
      #  call lbl_event_talk_craig
      #"Ask Hecate to hang back after class.":
      #  call lbl_event_talk_hecate
      #"Ask Sanura to hang back after class.":
      #  call lbl_event_talk_sanura
      "Maybe I should see what Bahini is up to?":
        #Bahini
        call lbl_event_call_bahini from _call_lbl_event_call_bahini
      "Maybe I should visit the library?":
        #Jo
        call lbl_event_visit_library from _call_lbl_event_visit_library
      "Maybe I should see if anyone is still in the teachers lounge?":
        #Nyx
        call lbl_event_teachers_lounge from _call_lbl_event_teachers_lounge
      "I should just head home and relax.":
        #Caragh
        $eveningTimeAvailable = True
        pass


  return

label lbl_event_time_evening:
  call update_time("Evening") from _call_update_time_5
  #TODO replace with town or let events handle?
  $random_event = "None"

  #Evening Phonecalls
  if random_event == "None" and Sanura_Arc_CurrentEvent == 3:
  # "Sanura's Route: Talk to Parents (Evening)"
    $random_event = "lbl_event_sanura_problem_tutoring_3"
    
  if random_event == "None" and Hecate_Arc_CurrentEvent == 4:
  # "Hecate's Route: Permission to Talk to Parents (Tutoring Event 02)"
    $random_event = "lbl_event_hecate_problem_tutoring_5"
    
  if random_event == "None" and Craig_Arc_CurrentEvent == 1:
  # "Craig's Route : Talking to Parents (Evening)"
    $random_event = "lbl_event_craig_problem_tutoring_2"
    
  if random_event == "None" and Craig_Arc_CurrentEvent == 2 and Craig_Arc_BahiniQuestioned:
  # "Mini-Scene " - Get glasses spec from Bahini
    $random_event = "lbl_event_craig_problem_tutoring_3"
    
  #Evening events (if no after school event happened)
  if eveningTimeAvailable or not random_event == "None":

    #if no story events try rolling a random event
    if random_event == "None":
      $ randomnum = renpy.random.randint(0, len(List_events_random_evening)*2)
      if randomnum < len(List_events_random_evening):
        $random_event = List_events_random_evening[randomnum]

    if not random_event == "None":
      call expression random_event from _call_expression_22
    else:
      Caragh "I had some extra time so I decided to rest."
      scene bg room
      play music music_bedroom
      Caragh "Aah, an evening alone with my favorite room and bed."
      Caragh "No kids to manage. No lessons to teach."
      Caragh "How can it get any better than this?"
      call update_stress(-20) from _call_update_stress_2
  
  call lbl_get_event_caragh_evening_events from _call_lbl_get_event_caragh_evening_events    
  #Plan next days classes
  call lbl_event_func_class_planning from _call_lbl_event_func_class_planning
  return


####################### Functional Events #################################

label lbl_event_func_class_planning:
  show bg room night with dissolve
  Caragh "What should I teach tomorrow?"
  call screen class_planning
  "Ok, so I'll teach [morning_class] in the morning and [afternoon_class] after lunch."

  return

label lbl_event_func_group_picker:
  #TODO: Update this to be a string
  $partners = ["", ""]
  menu:
    "Pick first partner"
    "Achilles, Adonis, Atlas":
      $partners[0] = "Achilles, Adonis, Atlas"
    "Athan":
      $partners[0] = "Athan"
    "Bestia":
      $partners[0] = "Bestia"
    "Dougal":
      $partners[0] = "Dougal"
    "Florence":
      $partners[0] = "Florence"
    "Juniper":
      $partners[0] = "Juniper"
    "Lateef":
      $partners[0] = "Lateef"
    "McCoy":
      $partners[0] = "McCoy"
    "Roark":
      $partners[0] = "Roark"
    "Rudolph":
      $partners[0] = "Rudolph"
    "Sophia":
      $partners[0] = "Sophia"
    "Xisreia":
      $partners[0] = "Xisreia"

  Caragh "Ok, first partner is [partners[0]]."

  menu:
    "Pick first partner"
    "Achilles, Adonis, Atlas":
      $partners[1] = "Achilles, Adonis, Atlas"
    "Athan":
      $partners[1] = "Athan"
    "Bestia":
      $partners[1] = "Bestia"
    "Dougal":
      $partners[1] = "Dougal"
    "Florence":
      $partners[1] = "Florence"
    "Juniper":
      $partners[1] = "Juniper"
    "Lateef":
      $partners[1] = "Lateef"
    "McCoy":
      $partners[1] = "McCoy"
    "Roark":
      $partners[1] = "Roark"
    "Rudolph":
      $partners[1] = "Rudolph"
    "Sophia":
      $partners[1] = "Sophia"
    "Xisreia":
      $partners[1] = "Xisreia"
  Caragh "Ok, second partner is [partners[1]]."

  return partners

#------------------------------------------------------
# updates day/time vars and updates the save name to match
label update_day(_day=0):
    $current_day = _day
    call update_save_name from _call_update_save_name
    return

label update_time(_time="???"):
    $current_time = _time
    call update_save_name from _call_update_save_name_1
    call update_UI_timeDisplay(_time) from _call_update_UI_timeDisplay
    return

label update_difficulty(_difficulty="???"):
    $current_difficulty = _difficulty
    call update_save_name from _call_update_save_name_2
    return

label update_save_name():
    #$save_name = "Day "+str(current_day)+" | "+current_time+" | "+current_difficulty+" Mode"
    $save_name = ""
    if use_day:
      $save_name = save_name + "Day " + str(current_day)
    if use_time:
      $save_name = save_name + " | " + current_time
    if use_difficulty:
      $save_name = save_name + " | " + current_difficulty + " Mode"
    return

label update_UI_timeDisplay(_time="???"):
    $current_time_hour = "08"
    if _time == "Morning":
      $current_time_hour = "08"
    if _time == "Morning Class":
      $current_time_hour = "09"
    if _time == "Lunch":
      $current_time_hour = "12"
    if _time == "Afternoon Class":
      $current_time_hour = "13"
    if _time == "After School":
      $current_time_hour = "16"
    if _time == "Evening":
      $current_time_hour = "18"
    $current_weather = renpy.random.choice(List_weather)
    $current_temp = str(renpy.random.randint(15,25))
    return
#--------------- Stat Updates / Notifications ----------------------

label update_mood_all(_change):
  $AddMoodToAll(_change)
  $show_moodChange(_change)
  return

label update_mood_specific(character, _change):
  $character.AddMood(_change)
  $show_moodChange(_change)
  return


label update_stress(_change):
  if feature_unlock_penalty_stress:
    if Character_Caragh.Mood >=90:
      #stress warning
      Caragh "I don't feel so good. Maybe I should think about taking a rest."
  #Stress only affects Caragh
  $Character_Caragh.AddMood(_change)
  #Stress is displayed as Mood inverted
  $show_moodChange(_change*-1)
  return

label update_relationship(character, _change):
  $character.AddRelationship(_change)
  #disabling relationship display
  #$show_relationshipChange(_change)
  return

label update_score_all(_subject, _change):
      
  $AddScoreToAll(_subject, _change)
  $show_scoreChange(_change)
  $CalculateAverageScores()
  if feature_unlock_bonus_Mood:
    $moodeffect = MoodMultiplierInEffect()
    if moodeffect[0]:
      Caragh "Some of the students seemed to be in a really good mood today and learned a little extra."
    if moodeffect[1]:
      $show_moodChange(0)
      Caragh "Some of the students seemed to be in a really foul mood today and learned nothing."
  return

label update_score_specific(character, _subject, _change):
  $character.AddScore(_subject, _change)
  $show_scoreChange(_change)
  return
