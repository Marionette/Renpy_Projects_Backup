# The script of the game goes in this file.



# The game starts here.

label start:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show craig
    #show hecate:
    #  xpos -200
    #  yalign 1.0
    #show sanura at right

    # These display lines of dialogue.

    #c "You've created a new Ren'Py game."

    #c "Once you add a story, pictures, and music, you can release it to the world!"


    #jump lbl_indicatorTest

    call lbl_game_run from _call_lbl_game_run


    # This ends the game.
    return



label lbl_game_setup:
    #------------------------------------------------------
    #Initialize Characters

    #Students
    $Character_Craig = CharacterClass()
    $Character_Craig.SetCharacter("Craig", 13, "Male", "Basilisk", "Student", "Geography", "Art", "Shy", "Seems to be afraid to get close to people.")
    $Character_Craig.SetMood(50)
    $Character_Craig.RandomizeAllScores(40, 60)

    $Character_Hecate = CharacterClass()
    $Character_Hecate.SetCharacter("Hecate", 12, "Female", "Witch", "Student", "Science", "Math", "Snarky", "Seems more interested in Magic than studying.")
    $Character_Hecate.SetMood(40)
    $Character_Hecate.RandomizeAllScores(40, 60)

    $Character_Sanura = CharacterClass()
    $Character_Sanura.SetCharacter("Sanura", 11, "Female", "Sphinx", "Student", "Math", "Literacy", "Eager to please", "Spends a lot of time trying to practice her riddles.")
    $Character_Sanura.SetMood(60)
    $Character_Sanura.RandomizeAllScores(40, 60)

    $Character_Average = CharacterClass()
    $Character_Average.SetCharacter("Class Average", 12, "???", "???", "Student", "???", "???")
    $Character_Average.SetMood(50)
    $Character_Average.RandomizeAllScores(50, 50)

    #Add all students to a list
    $List_Students = [Character_Craig, Character_Hecate, Character_Sanura, Character_Average]
    
    call SetupSideCharacters from _call_SetupSideCharacters
    $CalculateAverageScores()

    #Teachers
    $Character_Bahini = CharacterClass()
    $Character_Bahini.SetCharacter("Bahini", 25, "Female", "Mummy", "Teacher", "Science", "Literacy",  Notes="If you want to know more about me, just ask. :)")
    $Character_Bahini.SetMood(70)

    $Character_Nyx = CharacterClass()
    $Character_Nyx.SetCharacter("Nyx", "?", "Female", "???", "Principal", "Literacy", "Geography",  Notes="Always seems to have endless paperwork to do. No idea how she manages it all.")
    $Character_Nyx.SetMood(50)

    $Character_Mog = CharacterClass()
    $Character_Mog.SetCharacter("Mog", "34", "Male", "Ogre", "Teacher (On Leave)", "History", "Music",  Notes="The first teacher of class 5C.")
    $Character_Mog.SetMood(50)

    $Character_Una = CharacterClass()
    $Character_Una.SetCharacter("Una", "30", "Female", "Banshee", "Teacher", "Art", "PE",  Notes="Two words: Volume Control.")
    $Character_Una.SetMood(50)

    $Character_Jo = CharacterClass()
    $Character_Jo.SetCharacter("Jo", "?", "?", "Invisible", "Librarian / Counselor", "Music", "Languages",  Notes="Doesn't talk but listens well.")
    $Character_Jo.SetMood(50)

    #MC
    $Character_Caragh = CharacterClass()
    $Character_Caragh.SetCharacter("Caragh", "28", "Female", "Dullahan", "Teacher", "Math", "Art")
    #Treating Mood as stress for Player character
    $Character_Caragh.SetMood(0)

    #$current_day = 0
    #$current_time = "Morning"
    #$current_difficulty = "Normal"
    call update_day() from _call_update_day
    call update_time() from _call_update_time_6
    call update_difficulty() from _call_update_difficulty

    $feature_unlock_roster = False
    $feature_unlock_status_self = False
    $feature_unlock_status_others = False
    $feature_unlock_calendar = False

    #python:
    #   basic_point = Text("F")
    #   # Example Screen 3 Charts
    #   animated_points = RadarChart(
    #       size=200,
    #       values=[100, 134, 222, 122, 77, 99, 101],
    #       max_value=350,
    #       data_colour=(229, 99, 153, 255),
    #       line_colour=(80, 81, 79, 255),
    #       background_colour=(135, 145, 158, 255),
    #       point=basic_point,
    #       visible={
    #           "base": True,
    #           "data": True,
    #           "lines": True,
    #           "points": False,
    #           "labels": True
    #       }
    #   )
    #
    #   animated_spider_web = RadarChart(
    #       size=400,
    #       values=[50, 70, 30, 60, 50, 90],
    #       max_value=100,
    #       labels = [
    #           Text("History"),
    #           Text("Science"),
    #           Text("Math"),
    #           Text("Literacy"),
    #           Text("Language"),
    #           Text("Geography")
    #       ],
    #       data_colour=(115, 52, 182, 255),
    #       line_colour=(166, 103, 219, 255),
    #       background_colour=(88, 82, 74, 0),
    #       lines={"webs": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
    #       visible={"base":False}
    #   )

    #------------------------------------------------------

    return

label lbl_testing_character_class:
    #TESTING
    "Character class testing"

    "Character 1"
    "My name is [Character_Craig.Name], I am a [Character_Craig.Age] year old [Character_Craig.Species]. My favourite subject is [Character_Craig.FavouriteSubject], but i'm not a fan of [Character_Craig.WorstSubject]."
    "My mood is [Character_Craig.Mood]."
    "My Scores are: History = [Character_Craig.History], Science = [Character_Craig.Science], Math = [Character_Craig.Math], Literacy = [Character_Craig.Literacy], Language = [Character_Craig.Language] and Geography = [Character_Craig.Geography]."

    "Character 2"
    "My name is [Character_Hecate.Name], I am a [Character_Hecate.Age] year old [Character_Hecate.Species]. My favourite subject is [Character_Hecate.FavouriteSubject], but i'm not a fan of [Character_Hecate.WorstSubject]."
    "My mood is [Character_Hecate.Mood]."
    "My Scores are: History = [Character_Hecate.History], Science = [Character_Hecate.Science], Math = [Character_Hecate.Math], Literacy = [Character_Hecate.Literacy], Language = [Character_Hecate.Language] and Geography = [Character_Hecate.Geography]."

    "Character 3"
    "My name is [Character_Sanura.Name], I am a [Character_Sanura.Age] year old [Character_Sanura.Species]. My favourite subject is [Character_Sanura.FavouriteSubject], but i'm not a fan of [Character_Sanura.WorstSubject]."
    "My mood is [Character_Sanura.Mood]."
    "My Scores are: History = [Character_Sanura.History], Science = [Character_Sanura.Science], Math = [Character_Sanura.Math], Literacy = [Character_Sanura.Literacy], Language = [Character_Sanura.Language] and Geography = [Character_Sanura.Geography]."

    "Character 4"
    "My name is [Character_Bahini.Name], I am a [Character_Bahini.Age] year old [Character_Bahini.Species]. My favourite subject is [Character_Bahini.FavouriteSubject], but i'm not a fan of [Character_Bahini.WorstSubject]."
    "My mood is [Character_Bahini.Mood]."
    "I am a [Character_Bahini.Job]"

    "Character 5"
    "My name is [Character_Nyx.Name], I am a [Character_Nyx.Age] year old [Character_Nyx.Species]. My favourite subject is [Character_Nyx.FavouriteSubject], but i'm not a fan of [Character_Nyx.WorstSubject]."
    "My mood is [Character_Nyx.Mood]."
    "I am a [Character_Nyx.Job]"
    #TESTING

    return

label lbl_game_run:
  #initial game setup
  call lbl_game_setup from _call_lbl_game_setup
  #Introduction/Prologue
  call lbl_day_0 from _call_lbl_day_0
  #First Day / Introductions
  call lbl_day_1 from _call_lbl_day_1
  #First teaching day = tutorial/instructions
  call lbl_day_2 from _call_lbl_day_2

  #Main game loop
  while current_day < 28:
    if current_day == 25:
      #Special cram day / Last school day before tests
      call lbl_day_26 from _call_lbl_day_26
    else:
      #Standard teaching day
      call lbl_day_loop from _call_lbl_day_loop
  #Exams day
  call lbl_day_29 from _call_lbl_day_29
  #Exam results
  call lbl_day_30 from _call_lbl_day_30

  if Ending_Flag_passedCount > 0:
    call lbl_day_31 from _call_lbl_day_31

  #"You finished the game!"
  #menu:
  #  "Roll credits":
  #    pass
  call lbl_credits from _call_lbl_credits_1

  return


label lbl_introduction:
    return

#------------------------------------------------------


#------------------------------------------------------------------------
label lbl_day_0:
    call update_day(0) from _call_update_day_1
    scene bg black with fade
    #"Its day [current_day]. You get the job, 'grats."
    show bg room
    play music music_bedroom
    n_phone "\"Hey, Caragh! Thanks for accepting our request on such short notice!\""
    n_phone "\"I've sent you an email with your official start day and some information about the class you'll be taking over.\""
    #show  Highlight email notification
    #play music  Email/Phone
    c_phone "Email received."
    c_phone "See you then, Nyx."
    #Action "Check email"     # Do we want to do a joke continuation where you don't check the email and arrive late for the job?
    $ waitemail = False
    menu:
        "It can wait.":
          $ waitemail = True
          Caragh "I'll check my email another time. I don't feel like looking at work today."
          show bg room with fadeblack
          "Some time later..."
          #show bg room with dissolve
          #play music music_bedroom

        "Check email now.":
          pass

    $nvl_mode = None
    nvl clear

    nvl_narrator "\nDear Caragh Dullahan,"
    nvl_narrator "Thank you for accepting the offer to work at Echidna's School for Little Monsters. You'll be starting on the 1st of October. Please find attached a brief on your future class."
    nvl_narrator "See you on the 1st!"
    nvl_narrator "Kind Regards,\nNyx Echidna\nPrincipal of Echidna's School for Little Monsters"


    if waitemail == True:
        show Caragh surprise with dissolve
        Caragh "October...1st..."
        Caragh "That's tomorrow! Shoot, I have to book a train over now or I'll be late!"
        show Caragh mad with dissolve
        Caragh "Aargh! Why did I forget about this? The email came two weeks ago!"
        Caragh "Okay, okay. I can't rock up unprepared. I have to speed through this email attachment and have a vague idea of what I should do first."
        show Caragh sad with dissolve
        Caragh "Ah, I can already feel the stress building up."
        call update_stress(+10) from _call_update_stress_18

    #show  Stat menu/Class List

    $feature_unlock_roster = True
    #show screen class_roster
    #Stats Tutorial "FOCUS: Class List (name, age, species, favorite/hated subjects, scribbled notes on the side about different personalities or comments from Bahini)"
    show Caragh happy with dissolve
    Caragh "The kids' names, their ages, species... Oh, the subjects they love or hate are written here too."
    show Caragh surprise with dissolve
    Caragh "Hm? There are more notes about the kids. A werewolf who's afraid of the dark and a demon who has been asleep for around 5,000 years? Whoa. That's not information most teachers would jot down."
    $feature_unlock_roster = True
    call screen class_roster
    Caragh "Who made these notes? This is a very well-written list."
    #give time for players to click around and explore
    #hide screen class_roster

    $nvl_mode = "phone"
    nvl clear
    b_phone "\"Hi, Caragh! This is Bahini from Echidna's School for Little Monsters. Thanks for taking over my class while I'm stuck in the hospital.\"" #show  Phone
    b_phone "I'm sure Nyx has sent you the class list by now. Hopefully, my notes will be of use to you."
    b_phone "I'm really glad you're helping us out. The kids need as much help as they can get before their year-end exams on the 30th."
    b_phone "Oh, I've marked out 3 students that need extra attention."
    b_phone "Their grades are so low that they'll need to repeat the year if they don't pass this time."
    c_phone "Don't worry. I'll take care of your class."
    b_phone "Great! Thanks, Caragh!"
    b_phone "By the way, can I call you Kara? Your name's a little too hard to type with the way my hands are bandaged right now."
    c_phone "Kara's fine."
    b_phone "{image=gui/game_phone/emoji/thumbsup.png}"
    b_phone "Well, I've got to go. Talk to you another time!"

    scene bg room
    show Caragh content with dissolve
    Caragh "Bahini's a very cheerful monster. I wonder what she's like in person. "

    show Caragh happy with dissolve
    Caragh "So, the first day will be a busy day with introductions and lots of paperwork. There's usually a meeting with the principal or someone else after classes are over. I should block the evening out, just in case."
    Caragh "I can leave the lesson planning to after I've met everyone. I think the flexibility of a daily plan, tailored to their specific needs, will let me provide these kids with exactly what they need."
    Caragh "Actually, let me just update my calendar first with the exam dates."
    #show screen show_calendar with dissolve
    Caragh "Oh, and I'll set aside some time for a last ditch cram session. Hopefully, that will get the kids over the passing line. A group study project should work well for that."
    # give time for players to click around and explore
    $feature_unlock_calendar = True
    
    #TODO add some introduction to these screens too
    $feature_unlock_status_self = True    
    $feature_unlock_status_others = True
    
    call screen show_calendar
    Caragh "Okay. I think I'm all ready."

    if waitemail == False:
        Caragh "I just have to wait for the start date to roll around."
        scene bg black with dissolve
        return

    elif waitemail == True:
        Caragh "Now, time to pack up."
        scene bg black with dissolve
        return


label lbl_tutorial_lesson_plan:
    show Caragh happy with dissolve
    Caragh "Okay. Now that I've met everyone, I should try and draft up some lesson plans."
    #Lesson Plan Tutorial    show  Tablet   # Lesson Plan Tutorial moved forward
    Caragh "Classes are split between morning and afternoon in this school, so I can only teach two subjects a day."     # Classes
    #IF Back-to-Back Penalty implemented
    if feature_unlock_penalty_backToBack:
      Caragh "Of course, I can teach History for the whole day but the kids might get bored. Their attention spans aren't as good as teenagers."     # Back-to-Back
label lbl_tutorial_backToBack:
    if feature_unlock_penalty_backToBack:
      menu:
        "Disable 'back to back' Penalty? (You can toggle this setting in the Options menu)"
        "Yes, Disable it.":
          $feature_unlock_penalty_backToBack = False
        "No, Keep it on.":
          $feature_unlock_penalty_backToBack = True
        "More info":
          "The back to back penalty will cause classes to be less effective if done multiple times in a row."
          "Teaching the same class [btb_length] or more times in a row will apply a x[btb_multiplier] penalty to points earned for the class."
          jump lbl_tutorial_backToBack
    #IF Score Degradation implemented
    if feature_unlock_penalty_ScoreDegradation:
      Caragh "I should also make sure I teach all of the subjects frequently. If I neglect a topic for too long, the students will start to forget what they've learned."     # Score Degradation
label lbl_tutorial_ScoreDegradation:
    if feature_unlock_penalty_ScoreDegradation:
      menu:
        "Disable score degradation? (You can toggle this setting in the Options menu)"
        "Yes, Disable it.":
          $feature_unlock_penalty_ScoreDegradation = False
        "No, Keep it on.":
          $feature_unlock_penalty_ScoreDegradation = True
        "More info":
          "The score degradation feature will cause students to slowly lose points in any classes not taken recently."
          "Scores will be reduced by [degradation_pointsLost] for each class that hasn't been taught in the last [degradation_length] days."
          jump lbl_tutorial_ScoreDegradation

    if feature_unlock_bonus_favourites:
      Caragh "Every kid has a favourite subject and a subject they hate. If I teach them something they hate, their mood will worsen. Conversely, if I teach them something they like, they'll be in a better mood. "     # Fav/Hated Subject

    # Exam/Non-Exam
    Caragh "It looks like the following subjects will be on the exams; History, Science, Maths, Literacy, Language and Geography."
    Caragh "Most kids don't like to study. For 5C's kids to get those grades up, they will have to study pretty hard. Their mood will worsen for every class they attend."
    Caragh "On the other hand, if we have a more laid back class, something they won't be tested on, their mood will improve. Classes like Art, Music or Physical Education could help in making sure they stay enthusiastic about learning."

    if feature_unlock_bonus_Mood:
      Caragh "If the students are in a bad mood, they won't learn as much as they should. On the other hand, if they're in a good mood, they'll learn better."
      
      #"Dev Note: For accessibility you can disable this feature in the options menu if you'd rather not play with it."
label lbl_tutorial_bonus_Mood:
    if feature_unlock_bonus_Mood:
      menu:
        "Disable Mood multiplier? (You can toggle this setting in the Options menu)"
        "Yes, Disable it.":
          $feature_unlock_bonus_Mood = False
        "No, Keep it on.":
          $feature_unlock_bonus_Mood = True
        "More info":
          "The mood multiplier will adjust the points gained during teaching based on the current mood of the students."
          "Keeping your students at high mood will give a bonus of up to x[max_multiplier] going all the way down to x[min_multiplier] for any students at a low mood."
          jump lbl_tutorial_bonus_Mood

    Caragh "I should try and make sure everyone's happy or my job will be harder than it already is."

    Caragh "In the evenings, I should have the chance to tutor one of the kids Bahini mentioned, prepare for the next day's classes or just relax."     # Evenings
    if feature_unlock_penalty_stress:
      Caragh "I must manage my stress properly. I'd probably faint if I overwork myself. I've also heard from a Nymph that stress will lead to bad luck."     # Stress
      
      #"Dev Note: For accessibility you can disable this feature in the options menu if you'd rather not play with it."
label lbl_tutorial_stress:
    if feature_unlock_penalty_stress:
      menu:
        "Disable stress Penalty? (You can toggle this setting in the Options menu)"
        "Yes, Disable it.":
          $feature_unlock_penalty_stress = False
        "No, Keep it on.":
          $feature_unlock_penalty_stress = True
        "More info":
          "The stress penalty will cause Caragh to faint if her stress level ever maxes out while teaching."
          "This will cause the current class to have no learning effect as she recuperates."
          jump lbl_tutorial_stress

    call screen class_planning
    return

#------------------------------------------------------------------------
label lbl_day_1:
    #Add day to save name from here onwards
    $use_day = True
    call update_day(1) from _call_update_day_2
    scene bg black with dissolve
    $dayName = weekDay(current_day)
    #"Its day [current_day]. Its a [dayName]. First day of school, you meet everyone"
    #Record empty entries to keep calendar correct
    $RecordClassOutcome("", "")
    $RecordClassOutcome("", "")

    #"Day 1 - Morning Class"
    call update_time("Morning Class") from _call_update_time_7
    show bg hallway with dissolve
    play music music_school
    show Caragh
    Caragh "This is a nice school. Cleaner than I ever thought a school could be."
    Caragh "Ah, 5C. So this is my new class."
    show Caragh sad with dissolve
    Caragh "I hope the kids aren't as terrifying as they seem in the book I bought about kids."
    show bg classroom morning with dissolve
    play music music_5c fadein 1.0
    show Caragh happy with dissolve
    Caragh "\"Good morning, students. I will be your teacher for the time you have until your year-end exams.\""
    Caragh "\"My name is Caragh Dullahan. As you can tell, I am a Dullahan. You may call me Miss Caragh.\""
    Caragh "\"Since today's our first day, why don't we introduce ourselves and get to know each other?\""
    Caragh "\"Starting from you, the sphinx up front. Tell me your name, age, species and something fun about yourself.\""
    hide Caragh with dissolve
    show Sanura excited with dissolve
    Description "The little girl bounces up to her feet with a beaming grin. Her ears and tail flop and sway with the force of her movements."
    Caragh "This is one of the kids Bahini marked as needing extra attention."
    Sanura "\"Hi, my name is Sanura and I'm 11! I'm a sphinx and I like riddles!\""
    Sanura "\"Oh, oh! Do you want to hear one, miss? It goes like this: what can't talk but will echo when spoken to?\""
    Caragh "I...? Was that meant to be the riddle? "
    show Sanura upset with dissolve
    Sanura "\"Wait! I meant 'what will talk back when spoken to?' I...\""
    Sanura "\"I-It's an e-echo...\""
    show Sanura sad with dissolve
    Sanura "\"I-It's not very good. Is it? I read it in a book. I didn't think it was that good either...\""
    Description "Sanura slides back down into her chair, dejected. Her ears and tail droop as her voice drifts off into a soft mumble."
    Caragh "I see now what kind of help she needs. This should be easy, right?"
    hide Sanura
    Caragh "\"Okay. Thank you, Sanura. Next, the girl behind Sanura.\""
    show  Hecate with dissolve
    Description "Slowly, the girl with the large hat stands up from her seat behind Sanura."
    show Hecate snarky with dissolve
    Hecate "\"Hecate. 12. Witch. I can turn set this entire place on fire with one word.\""
    Caragh "\"I see...\""
    Caragh "No, I don't see. Are kids always this weird, or is this a human thing? "
    Caragh "Anyway, Hecate. Another kid Bahini marked out. She sounds smart, if she can really burn this place down at her age. What would she need help with?"
    Caragh "\"Thank you, Hecate.\""
    hide Hecate
    Caragh "\"Next?\""
    show  Craig with dissolve
    Description "From behind the shadow of Hecate's large hat, a boy cloaked in a hooded robe stands up."
    Craig "\"Hi, my name is Craig and I'm 13. I'm...\""
    show Craig worried with dissolve
    Description "Craig's voice drifts off into a whisper."
    Caragh "\"I'm sorry, Craig. I didn't quite catch that. Could you repeat yourself?\""
    Caragh "Craig... Another kid to keep an eye out for."
    show Craig neutral with dissolve
    Craig "\"I'm sorry! I said I'm...a Basilisk. I collect rocks.\""
    Caragh "\"Collecting rocks? That's a nice hobby. I'm a collector too.\""
    show Caragh snark with dissolve
    Caragh "Yeah, collector of pay slips. I'll regret saying that one day. "
    Caragh "The book said bringing up something in common would make it easier for the kid to accept you as a teacher. But what can I say? "
    Caragh "Rocks are boring. Why do you collect them? I'm not dumb enough to say that."
    Caragh "\"Alright. Thank you, Craig. Now, who's behind Craig?\""
    scene bg black with fade # SLOW FADE OUT   # If we're not introducing more students, we can start fading out here. If we are, fade out happens later.
    "The rest of the class introduce themselves in a similar fashion."
    $renpy.pause()
    show bg classroom morning with fade
    Caragh "\"Thank you for the introductions, class.\""
    Caragh "\"I think it's just about lunch time, so I'll meet everyone back here after.\""
    Everyone "Yes Miss!"
    Description "It doesn't take long for the class to grab their lunches and vacate the room"
    Caragh "Guess I better go too."
    #Caragh "\"Now, for the morning, we'll be learning [Subject Name]...\""
    #"INSERT THE USUAL CLASS TEXT HERE"

    #------------------------------------------------------------------------

    call update_time("Lunch") from _call_update_time_8
    #"Day 1 - Lunch"
    scene bg cafeteria with dissolve
    play music music_school
    Caragh "So this is the cafeteria. The kids eat in the same place as the teachers. That's interesting. "
    Caragh "Is it something most schools for young kids do or is it unique to this school?"
    Caragh "Right. I have to hurry up and finish my lunch."
    Caragh "This afternoon, I'd like to have a talk with the three kids Bahini said needed special attention, and Nyx said she'll touch base with me later in the afternoon."
    Caragh "I'd like to get a head start on the paperwork waiting for me."
    #return #END SCENE
    #------------------------------------------------------------------------

    #"Day 1 - Afternoon Class - Talk to kids"
    call update_time("Afternoon Class") from _call_update_time_9
    scene bg classroom empty with dissolve
    play music music_quiet
    show Caragh at left
    play sound sfx_schoolbell
    Caragh "Goodbye, peace and quiet. Hello, working with kids. Okay, which of the 3 kids should I talk to first?"

    $day1_flag_talkedToCraig = False
    $day1_flag_talkedToHecate = False
    $day1_flag_talkedToSanura = False

label lbl_day_1_1on1_choice:
    #Choice "Craig / Hecate / Sanura"
    menu:
      "Okay, which of the 3 kids should I talk to first?"

      "Craig" if day1_flag_talkedToCraig == False:
        call lbl_day_1_1on1_craig from _call_lbl_day_1_1on1_craig
        $day1_flag_talkedToCraig = True
      "Hecate" if day1_flag_talkedToHecate == False:
        call lbl_day_1_1on1_hecate from _call_lbl_day_1_1on1_hecate
        $day1_flag_talkedToHecate = True
      "Sanura" if day1_flag_talkedToSanura == False:
        call lbl_day_1_1on1_sanura from _call_lbl_day_1_1on1_sanura
        $day1_flag_talkedToSanura = True

    if day1_flag_talkedToCraig and day1_flag_talkedToHecate and day1_flag_talkedToSanura:
      #Merge choice: 3 kids
      Caragh "Well, I've talked to all 3 of them. I guess all that's left is the meeting with Principal Nyx and finishing up my lesson plans."
      play sound sfx_schoolbell
      Caragh "Whoa, time flies."
      jump lbl_day_1_1on1_after
    else:
      jump lbl_day_1_1on1_choice



label lbl_day_1_1on1_craig:
    #+ Craig
    show  Craig at right
    show Craig worried with dissolve
    Craig "\"Miss Caragh, you asked for me?\""
    Caragh "\"Yes, Craig. Please, sit.\""
    Description "Craig shuffles slowly into the room, tail flicking nervously. The fabric of his cloak slid and pooled on the floor as he slouched on the chair placed before my desk."
    Caragh "\"Craig, is there something wrong?\""
    show Craig neutral with dissolve
    Craig "\"No, Miss. Why?\""
    Caragh "\"I had a look at your grades over the past year. You haven't been doing well. Is there anything I can help you with?\""
    show Craig worried with dissolve
    Craig "\"N-No...\""
    Caragh "This isn't going to work. Let's try another angle."
    Caragh "\"You said you like to collect rocks. What kind of rocks do you like?\""
    show Craig neutral with dissolve
    Craig "\"I-I like rocks that have stories.\""
    Caragh "\"Oh? What stories are there in your collection?\""
    show Craig happy with dissolve
    Craig "\"There's a rock I have that's a fossil. It has a little spiral on it and there are rings in the rocks that show what the rock has gone through and...\""
    Description "Craig's voice slowly escalates from a soft whisper into a stream of excited chatter. His hood sways as he begins to sit upright and his hands move around to emphasize his points."
    Caragh "That's more like it. Open up so we can get to the bottom of why you're failing."
    Caragh "But..."
    Caragh "It's been a while now. Doesn't he need to stop to breathe?"
    Caragh "I..."
    Caragh "What do I do?"
    Craig "\"...and then there's another rock I found on the road that's pretty and shiny.\""
    show Craig sad with dissolve
    Description "Craig's voice comes to a halt. His excitement flees his body as he slouches back down. His hands fall to grip tightly at the folds of his cloak."
    Caragh "\"A-Amazing. That was nice of you to share, Craig.\""
    Caragh "I don't think I can get anything more concrete from him. I should just leave it, right? What did the book say?"

    #Choice "Push for more information / Leave it"

    menu:
      "Push for more information":
        #- Push
        Caragh "\"From how well you know your rocks, it's clear you have a smart mind. What's stopping you from focusing on your study?\""
        show Craig sad with dissolve
        Description "Craig remains silent. His hands clench harder around his cloak. "
        Description "..."
        Caragh "You could hear a pin drop in here. I don't think this was the right move to make." # wrong choice
        call update_mood_specific(Character_Craig, -5) from _call_update_mood_specific_2 

      "Leave it":
        #- Leave it
        Caragh "\"Thank you so much for your time, Craig. It was good to find out more about you.\""
        show Craig neutral with dissolve
        Description "Craig remains silent. His grip around his cloak loosened. His hands shifted to hang by his side."
        Caragh "Well, he's not clamming up. That's a good sign, right?"  # right choice
        call update_mood_specific(Character_Craig, 5) from _call_update_mood_specific_3


    #Merge Choice: Craig
    Caragh "\"Craig, if you don't pass the year-end exams, you'll have to repeat the year.\""
    Caragh "\"You only have a month left and if we don't bring your grades up somehow, you will fail.\""
    Caragh "\"What do you think about tutoring after classes? It'll just be you and me. We can focus on what you're weak at and go at your pace.\""
    show Craig sad with dissolve
    Description "Craig nods. "
    Caragh "\"Okay. I'll let you know when our first tutoring session will be. See you tomorrow, Craig.\""
    hide Craig
    Description "Craig nods once more before shuffling out of the room."
    Caragh "Okay. Now, who else?"
    #LOOP "Back to start"
    return

label lbl_day_1_1on1_hecate:
    #+ Hecate
    show  Hecate at right
    Hecate "\"You called, Miss Caragh?\""
    Caragh "\"I did, Hecate. Please, sit.\""
    Description "Hecate strides into the room. Her large hat bobs and sways as she confidently walks into the room and plops herself down on the chair placed before Caragh's desk."
    show Hecate snarky with dissolve
    Hecate "\"Is it about my grades? Or were you tempted by my offer to burn this place down?\""
    Caragh "\"Yes about the grades and no about the offer.\""
    Hecate "\"Aw, that's sad.\""
    Description "Unphased by the rejection, Hecate's smirk doesn't falter. She leans back on the chair, as comfortable as can be. Her fingers twitch and fiddle with each other, occassionally letting off magical sparks of ember."     # Is it okay to have sparks as part of her character?
    Caragh "This is familiar territory. How can someone so young act and sound exactly like a teenager from the boarding schools I'd taught in?"
    Caragh "How should I handle this situation?"

    #Choice "Blunt and honest / Tactful"

    menu:
      "Blunt and honest":
        #- Blunt        # right choice
        Caragh "\"I'll be honest with you, Hecate. You're failing. Over the past year, your grades have been steadily dropping. At this rate, you'll fail your year-end exams and have to repeat the year.\""
        show Hecate unamused with dissolve
        Hecate "\"Grades aren't everything. What's more important is how amazing and powerful I am.\""
        Caragh "\"A witch who only knows how to set things on fire will never be respected. You won't be amazing and powerful. You'll be hated and despised as a villain.\""
        show Hecate mad with dissolve
        Hecate "\"I... What do you know? You're a Dullahan!\""
        Caragh "\"I'm also a teacher. I've taught hundreds of kids who grow up to be amazing, respected and also kids who are hated. I know what they did wrong and what they did right.\""
        Caragh "\"The one thing most of them did wrong? Letting their grades drop and failing. What kind of respect can they gain if they can't even answer what 21 multiplied by 5 and divided by 2 is?\""
        show Hecate snarky with dissolve
        Hecate "\"I'm not that stupid. I know the answer.\""
        Caragh "\"Do you? That question was one that you answered wrongly in the last exam.\""
        Hecate "\"I do know the answer! It's 52.5!\""
        Caragh "\"Your answer was 55.\""
        show Hecate unamused with dissolve
        Description "Hecate goes silent. Her fingers are still but sparks could still be seen appearing at the tips of her fingers."
        Caragh "\"Look. I'm not saying you're stupid. You're not. I can see that from your control over your magic. But maybe a few tutoring sessions will help.\""
        Caragh "\"Your grades aren't that bad. You can pass with just a little more work.\""
        Caragh "\"Well?\""
        Hecate "\"...okay. I'll do it. When is our first session?\""
        Caragh "Phew, looks like I got through to her. I wasn't sure if that would work."
        Caragh "\"I'll let you know tomorrow. Thank you, Hecate.\""
        Description "Hecate gives a small nod as her eyes dart up to look into Caragh's. She then stands up and walks out the door. "
        hide Hecate
        Caragh "That went well. I expected her to blow up at me. Instead, she just accepted my offer. Strange."
        call update_mood_specific(Character_Hecate, 5) from _call_update_mood_specific_4

      "Tactful":
        #- Tactful        # wrong choice
        show Hecate snarky with dissolve
        Caragh "\"Has there been something bothering you lately, Hecate?\""
        Hecate "\"No. Why would there be?\""
        Caragh "\"Are you sure?\""
        show Hecate happy with dissolve
        Hecate "\"Of course I am! I'm the greatest witch in my year.\""
        Hecate "\"What could be bothering me?\""
        Caragh "\"Well, your grades have been pretty low during the past year.\""
        show Hecate unamused with dissolve
        Hecate "\"Great witches don't need to have good grades. I just need to be the best at magic and no one will care what my grades are.\""
        Caragh "\"Even if it means having to repeat the year?\""
        show Hecate mad with dissolve
        Hecate "\"Who cares?\""
        Caragh "\"I care. Miss Bahini cares.\""
        Caragh "\"Your classmates will because they'll be separated from you.\""
        show Hecate unamused with dissolve
        Description "Hecate scoffs. She crosses her arms before her chest."
        Caragh "\"Look, we only have a month before the year-end exams. Why don't you come for a few tutoring sessions after class is over? It'll just be you and me. Once your grades are good enough to pass, you can stop coming.\""
        show Hecate snarky with dissolve
        Hecate "\"And what's in it for me?\""
        Caragh "\"You get to keep studying new magic and your classmates will still be your classmates.\""
        Hecate "\"...fine. Can I go now?\""
        Caragh "\"You may. I'll let you know when our first tutoring session will be.\""
        show Hecate mad with dissolve
        Hecate "\"Whatever.\""
        Description "Hecate stomps out of the room, leaving sparks in her wake. A few moments later, kids yelping could be heard coming from the hallway. "
        hide Hecate
        Caragh "That didn't go as well as I'd hoped. I hope those sparks didn't hurt too much."
        call update_mood_specific(Character_Hecate, -5) from _call_update_mood_specific_5 

    #Merge Choice: Hecate
    Caragh "Right. Anyone else?"
    #LOOP "Back to start"
    return

label lbl_day_1_1on1_sanura:
    #+ Sanura
    show Sanura excited with dissolve
    Sanura "\"Hi, Miss Caragh!\""
    Caragh "\"Hello, Sanura. Please, come in and take a seat.\""
    Sanura "\"Okay!\""
    Description "Sanura bounces into the room and sits down on the chair before Caragh's desk. Her furry tail keeps flicking and swishing with joy."
    show Sanura happy with dissolve
    Sanura "\"What is it, Miss Caragh? Is there something wrong? What do you need help with?\""
    Caragh "She's so bubbly and... This is how kids should act, Caragh. Pull yourself together. You are a teacher."
    Caragh "\"Sanura, I'd like to talk to you about your grades.\""
    Caragh "\"Based on your past teacher's reports, they've started slipping. Did you have problems understanding the material or the way it was taught?\""
    show Sanura sad with dissolve
    Sanura "\"It's not Mr Mog or Miss Bahini's fault! I'm just a little...slow.\""
    Caragh "\"That's not what Miss Bahini said. She said you're a smart girl. You just have your head up in the clouds too much.\""
    Caragh "\"Why, Sanura? What are you thinking about?\""
    show Sanura excited with dissolve
    Sanura "\"Nothing, Miss Caragh. I'm just...really into riddles and I keep finding all these good ones. Riddles are so fun!\""
    Caragh "That's not the answer I'm looking for but it might also be it. Riddles. I wonder..."

    #Choice "Talk about riddles / Talk about grades"
    menu:
      "Talk about riddles":
          #- Riddles        # Right choice
          Caragh "\"You found this morning's riddle in a book. What book is it? It must be good if you keep thinking about the riddles.\""     # Sanura's hiding the fact that she made up the riddle
          show Sanura sad with dissolve
          Sanura "\"O-Oh, erm, nah. That book's rubbish. I only keep thinking about it because the riddles are so bad that I wonder if they work.\""
          Caragh "\"I see.\""
          Caragh "I can see that you're hiding something from me. Should I tell her?"

          #Choice "Expose her lie / Talk around it"
          menu:
            "Expose her lie":
                #-- Expose        # wrong choice
                Caragh "\"I don't think you're telling the truth, Sanura.\""
                Caragh "\"Can you please tell me the truth? No one will punish you for it.\""
                show Sanura mad with dissolve
                Sanura "\"I'm not lying. Really! I just keep stumbling across super bad riddles.\""
                Sanura "\"But I'll study harder! I won't fail my exams! I can do it, Miss Caragh!\""
                Caragh "It was worth a shot. If she gave in this easily, she would've told me in the first place. Still, the riddles are involved. Somehow."
                call update_mood_specific(Character_Sanura, -5) from _call_update_mood_specific_6 

            "Talk around it":
                #-- Talk Around        # right choice
                Caragh "\"Perhaps the author just needed more practice. I know it took me a lot of practice before I found the best way to hold my head.\""
                Caragh "\"Speaking of practice, you should be practising for the year-end exams. I know you're a smart girl but your grades don't show it. At this rate, you'll fail the year-end exams and have to repeat the year.\""
                show Sanura sad with dissolve
                Sanura "\"Really? Oh, no! My mother would be so upset if I do. What do I do, Miss? I can't disappoint her.\""
                Caragh "Mother? It's not often you hear kids being so afraid of disappointing their parents. Maybe that's a clue. I wonder how the riddles fit in with everything."
                call update_mood_specific(Character_Sanura, 5) from _call_update_mood_specific_7 

      "Talk about grades":
        #- Grades        # wrong choice
        Caragh "\"Now, Sanura, about your grades. I think you need to focus if you want to pass the year-end exams. From what I can see, you're failing and failing the year-end exams means you'll have to repeat the year.\""
        show Sanura sad with dissolve
        Sanura "\"I hear you, Miss. I've been studying and studying. I'm just slow and bad at studying. I'm sorry, Miss.\""
        Caragh "Some of the teenagers from my old classes loved saying that about themselves. It was always a toss-up between snark and unhealthy behavior. Sanura doesn't seem like the type of kid to snark. I wonder..."
        Caragh "\"Why do you think that, Sanura? Why do you think you're slow?\""
        Sanura "\"I just am. There's no changing it, Miss. I've always been slow.\""
        Caragh "She's getting defensive. Maybe I should've eased her into the topic instead."
        call update_mood_specific(Character_Sanura, -5) from _call_update_mood_specific_8 

    #Merge Choice: Sanura
    Caragh "\"What do you think about tutoring, Sanura?\""
    Caragh "\"I can help you with your studies after class. Just a few one-on-one sessions. An hour or two of focusing on your weak subjects will help pull up your average.\""
    show Sanura happy with dissolve
    Sanura "\"Sure thing, Miss Caragh! Thank you so much!\""
    Caragh "\"You're welcome. I'll let you know tomorrow when our first session is.\""
    show Sanura excited with dissolve
    Sanura "\"Okay, Miss Caragh! Bye-bye!\""
    hide Sanura
    Description "Sanura skips out of the room. Her tail flicks and swishes as merrily as it did when she came in the room but her ears are still. It's clear that something is bothering Sanura."
    return
    #------------------------------------------------------------------------

label lbl_day_1_1on1_after:
    call update_time("After School") from _call_update_time_10
    #"Day 1 - Evening/After Classes"
    play sound sfx_knock
    Caragh "\"Who is it?\""
    show  Nyx at right
    Nyx "\"I hope I'm not bothering you.\""
    Caragh "\"Principal Nyx! I was just about to head to your office to see you.\""
    Nyx "\"Please, call me Nyx.\""
    Nyx "\"I was just heading back to my office when I realized I was near the classroom you asked for. I thought it'd be easier to have the meeting here instead.\""
    Nyx "\"Well? How has your first day been?\""

    #Choice "Fine / A little worried / Hard"
    menu:
      "Fine":
          #+ Fine
          show  Nyx happy
          Caragh "\"Today has been going well. Nothing bad has happened so far.\""
          Nyx "\"Good, good. I know Bahini has been in touch with you about your kids. Feel free to contact her if you ever need help. Of course, the other staff members and I are all here if you ever need a hand.\""

      "A little worried":
          #+ A little worried
          show  Nyx huh
          Caragh "\"Today has been mostly alright but what I learned in the past few hours has me a little worried.\""
          Nyx "\"That's just life as usual when it comes to teaching kids. Bahini will be checking in on you every week. If you need advice or some help, you can ask her. Naturally, the rest of the staff and myself are all here if you ever need a hand.\""

      "Hard":
          #+ Hard
          show  Nyx sad
          Caragh "\"It's been an eventful day. I feel like there's a long, hard path ahead of me.\""
          Nyx "\"That sounds worrying. If you need anything, please speak up. Bahini will be in touch if you ever need advice. The other staff members and I are here if you need us. Do take care of yourself.\""


    #Merge Choices: First Day?
    Caragh "\"Thank you, Principal Nyx.\""
    show  Nyx happy
    Nyx "\"Now, what did I tell you before? Just call me Nyx.\""
    Caragh "\"Yes, my bad. Thank you, Nyx.\""
    Nyx "\"I see you're finishing up your lesson plans. I'll just leave you to it. Try to get some rest as early as you can. It'd be bad for us if you collapse from overworking.\""
    Description "Nyx walks out of the room. The ends of her hair happily wave at me just before she closes the door behind her."
    hide Nyx
    Caragh "That was...interesting. "
    Caragh "Right. Just a few more notes and..."
    show bg classroom afternoon with fadeblack
    Caragh "All done. "
    Caragh "Time to clock out. What should I get for dinner?"
    #------------------------------------------------------------------------
    call update_time("Evening") from _call_update_time_11
    scene bg room with dissolve
    play music music_bedroom
    #Tutorial replaces standard events
    $morning_class = "History"
    $afternoon_class = "Science"
    $after_school_tutoring = "Free Time"
    #"First the tutorial! Let me explain how i teach to Nyx."
    call lbl_tutorial_lesson_plan from _call_lbl_tutorial_lesson_plan

    Caragh "Now that that's sorted, I have an early start in the morning. I'd better get some sleep."
    scene bg black with dissolve

    return

#------------------------------------------------------------------------
label lbl_day_2:
    #Add time of day to save name from here onwards
    $use_time = True

    call update_day(2) from _call_update_day_3
    scene bg room with dissolve
    play music music_bedroom
    $dayName = weekDay(current_day)
    "It's October [current_day], a [dayName]. Time to teach!"

    call lbl_event_time_morning_class from _call_lbl_event_time_morning_class
    call lbl_event_time_lunch from _call_lbl_event_time_lunch
    call lbl_event_time_afternoon_class from _call_lbl_event_time_afternoon_class
    call lbl_event_time_after_school from _call_lbl_event_time_after_school
    call lbl_event_time_evening from _call_lbl_event_time_evening

    return

#------------------------------------------------------------------------
label lbl_day_loop:
    call update_day(current_day+1) from _call_update_day_4
    scene bg room with dissolve
    play music music_bedroom
    $dayName = weekDay(current_day)
    if IsSchoolDay(current_day):
      Description "It's day [current_day], a [dayName] and a school day. Time to teach!"
      call lbl_day_weekday from _call_lbl_day_weekday
    else:
      Description "It's day [current_day], a [dayName]. It's not a school day. What should I do with my time off?"
      call lbl_day_weekend from _call_lbl_day_weekend
    return


label lbl_day_weekday:
    call lbl_event_time_morning from _call_lbl_event_time_morning
    call lbl_event_time_morning_class from _call_lbl_event_time_morning_class_1
    call lbl_event_time_lunch from _call_lbl_event_time_lunch_1
    call lbl_event_time_afternoon_class from _call_lbl_event_time_afternoon_class_1
    call lbl_event_time_after_school from _call_lbl_event_time_after_school_1
    call lbl_event_time_evening from _call_lbl_event_time_evening_1
    return

label lbl_day_weekend:
    call update_time("Morning") from _call_update_time_12
    scene bg room
    play music music_bedroom
    #"Its day [current_day]. Its a [dayName]. Its the weekend, What should i do with my time off?"
    #Record empty entries for weekends to keep calendar correct
    if dayName == "Saturday":
      call lbl_event_bahini_weekly from _call_lbl_event_bahini_weekly
      $RecordClassOutcome("", "")
      call update_stress(-20) from _call_update_stress_19
      "Afterwards I spent the rest of the day resting."
    else:
      if Bahini_Arc_VisitAllowed:
        Caragh "Bahini did say i could visit her on Sundays, should i go?"
        menu:
          "Go":
            Caragh "Yeah, I don't have anything else planned for today so lets go."
            call lbl_event_bahini_visit from _call_lbl_event_bahini_visit
            call update_stress(-10) from _call_update_stress_20
            Caragh "Talking to Bahini always leaves me in a good mood."
            $RecordClassOutcome("Visited Bahini in Hospital", "")
          "Stay home":
            call update_stress(-20) from _call_update_stress_21
            Caragh "Maybe ill just stay home and get rested and ready for next week instead."
    $RecordClassOutcome("", "")
    #Weekend events here
    return

#------------------------------------------------------------------------
label lbl_day_26:
    call update_day(26) from _call_update_day_5
    $dayName = weekDay(current_day)
    call update_time("Morning Class") from _call_update_time_13
    #"Its day [current_day]. Its a [dayName]. Last chance to cram!"
    #"Day 26 (Cram Session)"
    show  Caragh at left
    show bg classroom morning with dissolve
    play music music_5c # Should this be split into Morning/Lunch/Afternoon?
    Caragh "\"Everyone, settle down.\""

    Caragh "\"I know everyone's looking forward to the holidays but you have a year-end exam to get through first. Next Monday will be the day that decides whether you'll be staying classmates for another year or if you'll be held back.\""
    Caragh "\"To help you combat your nerves, we'll be revising what will be important to you tomorrow.\""
    Caragh "\"I'll be splitting you up into groups of four. Please stay seated while I announce your groupmates. Once I'm done, you may move to the tables with your group number on them.\""
    show  Craig at right

    #-----------------------
    #partner selection

    #copy list
    $available_students = [x[0] for x in List_Students_Side]

    #Remove already chosen partners from list
    if not Craig_Cram_Partner_01 == "":
      $available_students = [x for x in available_students if x != Craig_Cram_Partner_01]
      #$available_students.Remove(Craig_Cram_Partner_01)
    if not Craig_Cram_Partner_02 == "":
      #$available_students.Remove(Craig_Cram_Partner_02)
      $available_students = [x for x in available_students if x != Craig_Cram_Partner_02]

    if not Hecate_Cram_Partner_01 == "":
      #$available_students.Remove(Hecate_Cram_Partner_01)
      $available_students = [x for x in available_students if x != Hecate_Cram_Partner_01]
    if not Hecate_Cram_Partner_02 == "":
      #$available_students.Remove(Hecate_Cram_Partner_02)
      $available_students = [x for x in available_students if x != Hecate_Cram_Partner_02]

    if not Sanura_Cram_Partner_01 == "":
      #$available_students.Remove(Sanura_Cram_Partner_01)
      $available_students = [x for x in available_students if x != Sanura_Cram_Partner_01]
    if not Sanura_Cram_Partner_02 == "":
      #$available_students.Remove(Sanura_Cram_Partner_02)
      $available_students = [x for x in available_students if x != Sanura_Cram_Partner_02]


    #Randomly assign the rest

    #Assign initial partners if not picked during arcs
    if Craig_Cram_Partner_01 == "":
      $Craig_Cram_Partner_01 = renpy.random.choice(available_students)
      $available_students = [x for x in available_students if x != Craig_Cram_Partner_01]
    if Craig_Cram_Partner_02 == "":
      $Craig_Cram_Partner_02 = renpy.random.choice(available_students)
      $available_students = [x for x in available_students if x != Craig_Cram_Partner_02]
    
    if Hecate_Cram_Partner_01 == "":
      $Hecate_Cram_Partner_01 = renpy.random.choice(available_students)
      $available_students = [x for x in available_students if x != Hecate_Cram_Partner_01]
    if Hecate_Cram_Partner_02 == "":
      $Hecate_Cram_Partner_02 = renpy.random.choice(available_students)
      $available_students = [x for x in available_students if x != Hecate_Cram_Partner_02]
    
    if Sanura_Cram_Partner_01 == "":
      $Sanura_Cram_Partner_01 = renpy.random.choice(available_students)
      $available_students = [x for x in available_students if x != Sanura_Cram_Partner_01]
    if Sanura_Cram_Partner_02 == "":
      $Sanura_Cram_Partner_02 = renpy.random.choice(available_students)
      $available_students = [x for x in available_students if x != Sanura_Cram_Partner_02]
    
    #assign rest of partners
    $Craig_Cram_Partner_03 = renpy.random.choice(available_students)
    #$available_students.Remove(Craig_Cram_Partner_03)    
    $available_students = [x for x in available_students if x != Craig_Cram_Partner_03]
    $Hecate_Cram_Partner_03 = renpy.random.choice(available_students)
    #$available_students.Remove(Hecate_Cram_Partner_03)
    $available_students = [x for x in available_students if x != Hecate_Cram_Partner_03]
    $Sanura_Cram_Partner_03 = renpy.random.choice(available_students)
    #$available_students.Remove(Sanura_Cram_Partner_03)
    $available_students = [x for x in available_students if x != Sanura_Cram_Partner_03]

    $Last_group_1 = renpy.random.choice(available_students)
    #$available_students.Remove(Last_group_1)
    $available_students = [x for x in available_students if x != Last_group_1]
    $Last_group_2 = renpy.random.choice(available_students)
    #$available_students.Remove(Last_group_2)
    $available_students = [x for x in available_students if x != Last_group_2]
    $Last_group_3 = renpy.random.choice(available_students)
    #$available_students.Remove(Last_group_3)
    $available_students = [x for x in available_students if x != Last_group_3]
    $Last_group_4 = renpy.random.choice(available_students)

    #-----------------------

    Caragh "\"Now, for Group 1, we have Craig, [Craig_Cram_Partner_01], [Craig_Cram_Partner_02] and [Craig_Cram_Partner_03].\""
    Description "Craig timidly looks around."
    if Craig_Arc_CurrentEvent == 5:
      "His tail flicks and waves at every groupmate he finds."
    else:
      "Well, as much as a boy drowning in his hood could."
    hide Craig

    show  Hecate at right   # Replace [] with names the player has selected in Hecate's arc. If the player didn't get to the event, just roll with random names (aka [Random]).
    Caragh "\"Group 2, you are Hecate, [Hecate_Cram_Partner_01], [Hecate_Cram_Partner_02] and [Hecate_Cram_Partner_03].\""
    Description "With a flick of her hands, Hecate sends sparks flying around the room. "
    if Hecate_Arc_CurrentEvent == 8:
      "The sparks sneakily weave around the room, as if they're in a game of hide and seek with Hecate's groupmates. They're so discreet that none of the kids noticed."
    else:
      "Whenever the sparks find a groupmate of Hecate, they explode into a shower of light and sparkles above the groupmate. Some of the explosions are rather blinding."
    hide Hecate

    show  Sanura at right   # Replace [] with names the player has selected in Sanura's arc. If the player didn't get to the event, just roll with random names (aka [Random]).
    Caragh "\"Group 3, you are Sanura, [Sanura_Cram_Partner_01], [Sanura_Cram_Partner_02] and [Sanura_Cram_Partner_03].\""
    Description "Sanura's ears perk up as she looks around for her groupmates."

    if Sanura_Arc_CurrentEvent == 9:
      "As she does so, her hands start tidying her desk and gathering up her notes. Of course, there's a sticky note stuck on top with a few riddles scribbled on it."
    else:
      "It's easy to tell when Sanura has found a groupmate. Her eyes would glaze over and she'd start practising what riddles she'll use later."
    hide Sanura

    Caragh "\"Lastly, Group 4. You are [Last_group_1], [Last_group_2], [Last_group_3] and [Last_group_4].\""
    Caragh "\"You may now swap seats.\""
    Description "Everyone scrambles to their groups."
    Caragh "\"Alright, let's start.\""
    Description "The day swiftly flies by as the kids go through subject after subject."
    Description "The cram session is a success! Everyone's grades and mood improve."
    play sound sfx_schoolbell
    Caragh "\"That's it for today. Good luck on the exams tomorrow.\""

    #TODO: IF Correct partners chosen
    if Craig_Cram_Partner_Correct and Hecate_Cram_Partner_Correct and Sanura_Cram_Partner_Correct:
      call update_score_all("All", 10) from _call_update_score_all_6
      Caragh "I think today went quite well. The kids were all focused on their work but they were having fun."     # Bonus?
    else:
      call update_score_all("All", 5) from _call_update_score_all_7
      Caragh "The group work was a bit of a mixed bag. But at least they all learned something."

    if Craig_Cram_Partner_Correct:
      call update_score_specific(Character_Craig, "All", 5) from _call_update_score_specific_4
      Caragh "Craig's not hiding in his shell anymore and he was talking to his groupmates on his way out."
    if Hecate_Cram_Partner_Correct:
      call update_score_specific(Character_Hecate, "All", 5) from _call_update_score_specific_5
      Caragh "Hecate's group might've bickered but Hecate was smiling so brightly that she lights up the room."
    if Sanura_Cram_Partner_Correct:
      call update_score_specific(Character_Sanura, "All", 5) from _call_update_score_specific_6
      Caragh "Sanura's group was laughing the loudest. I even heard a few good riddles from Sanura."
    #return #END SCENE

    #"Day 26 - After Class (Evening)"
    call update_time("After School") from _call_update_time_14
    show  bg hallway
    play music music_school
    show Caragh at left
    Caragh "Paperwork takes so much out of me. I need to enjoy some tea in a quiet nook somewhere before I brave the traffic."
    Caragh "Hm? Someone is still hanging around."
    $metSomeone = False

    #Choice "Craig / Hecate / Sanura / Don't know them "     # Options are only available if arc is finished and made right decision for Cram. Otherwise, it's just"don't know them"
    # don't know if this should be option to choose, a menu to loop back into or just lines that auto-trigger.
    #+ Craig
    if Craig_Cram_Partner_Correct and Craig_Arc_CurrentEvent == 5:
      show Craig at right
      play music music_good_vibes
      Caragh "\"Craig! What are you doing here? Shouldn't you be home by now?\""
      Craig "\"I...\""
      Craig "\"I wanted to thank you for all you've done for me, Miss Caragh.\""
      Description "Craig gives me a quick hug, wrapping his tail around me for a moment, before he runs off."
      hide Craig
      Caragh "Craig has come a long way from the shy kid who hides behind his hood all the time."
      $metSomeone = True

    #+ Hecate
    if Hecate_Cram_Partner_Correct and Hecate_Arc_CurrentEvent == 8:
      if metSomeone == True:
          Caragh "Oh?"
      elif metSomeone == False:
          pass

      show Hecate at right
      play music music_good_vibes
      Caragh "\"Hecate? What are you doing here still?\""
      Description "Hecate spins around to look at me. There's a rare soft smile on her lips."
      Hecate "\"Thank you, Miss Caragh, for all that you've done. You're a great teacher.\""
      Description "Hecate then leaves."
      hide Hecate
      Caragh "Hecate surprises me at every turn. I didn't think she'd stay behind just to tell me that. After all, she loves her magic lessons so."
      $metSomeone = True

    #+ Sanura
    if Sanura_Cram_Partner_Correct and Sanura_Arc_CurrentEvent == 9:
      if metSomeone == True:
          Caragh "Hm?"
      elif metSomeone == False:
          pass
    show Sanura at right
    play music music_good_vibes
    Caragh "\"Sanura, hello. Still hanging around?\""
    Sanura "\"Hey, Miss Caragh. Riddle me this.\""
    Sanura "\"What is often returned but never borrowed?\""
    Caragh "\"Oh? What is it?\""
    Sanura "\"Thanks!\""
    Sanura "\"Thank you so much, Miss Caragh, for the past month.\""
    hide Sanura
    Description "Before I could say another word, Sanura sprints off."
    Caragh "That was a good riddle. A good riddle from one of the best kids I've ever taught."
    $metSomeone = True

    if not metSomeone:
      #+ Don't Know Them
      Caragh "I don't recognize them. Probably not important. Now, peace and quiet..."

    call update_time("Evening") from _call_update_time_15
    Caragh "Well, there's not much point in planning for classes. I've done all I can for these kids. The rest is up to them."
    Caragh "It's been a long day. For now, I'll just get started on my weekend by going to bed early."
    scene bg black with dissolve
    return

#------------------------------------------------------------------------
label lbl_day_29:
    call update_day(29) from _call_update_day_6
    $dayName = weekDay(current_day)
    scene bg room with dissolve
    play music music_bedroom
    Caragh "Today's the day. It's time for the year-end exams."
    # "Day 29 (Exams)"
    show bg classroom morning
    play music music_quiet
    Description "The room is quiet. Pens scribble across papers as the students work through the questions before their eyes. "
    show Caragh at left
    Description "I slowly walk down the aisles, glancing at the papers of each student as I pass by them."
    Caragh "...Fourteen, fifteen, sixteen. Turn. One, two, three..."

    #Flag/Outcome "If Grades < C / >= C / Mix"

    if Character_Sanura.HasPassedExams():
    #+ >=C
      show  Sanura at right
      Description "I pass by Sanura, hard at work with a smile on her lips. Her ears are raised up high as her pen speeds across line after line. Her tail swishes and brushes across my legs as I walk past her desk."
      Caragh "Good. She looks confident."
      hide Sanura
    else:
      show  Sanura at right
      Description "I pass by Sanura, frowning down at her paper. Her ears swivel from left to right as she taps her pen to her lips. Her tail flicks and twitches, smacking my legs as I walk past her desk."
      Caragh "She looks like she's struggling."
      hide Sanura

    if Character_Hecate.HasPassedExams():
      Description "The next desk on my path is Hecate's desk. "
      show  Hecate at right
      Description "Sparks merrily dance along the edge of Hecate's hat. The girl's eraser and pens float around her. A tap on her head from me put a stop to the floating staionary. The girl smirks up at me before turning her attention back to her paper."
      Caragh "If she has energy to spend on magic, she must be feeling good."
      hide Hecate
    else:
      Description "The next desk on my path is Hecate's desk."
      show  Hecate at right
      Description "The girl's pen thumps on the desk, leaving behind an ink spot. Scattered all over the desk are ink spots of the similar shape and colour. Hecate's free hand is raised, fiddling with the edges of her hat. As I walk by her, the girl looks up with a frown before looking back at her paper."
      Caragh "This isn't a good sign. There's not a single spark around her."
      hide Hecate

    if Character_Craig.HasPassedExams():
      Description "The last desk I'll pass by before I have to turn around again is Craig's. "
      show  Craig at right
      Description "Sprawled out over his desk, Craig swiftly scribbles answer after answer onto his paper. His tail taps away to a song only known to Craig as it lays curled up around the legs of his chair."
      Caragh "He's singing. That's a good sign."
      hide Craig
    else:
      Description "The last desk I'll pass by before I have to turn around again is Craig's."
      show  Craig at right
      Description "The boy slouches in his seat. His tail hangs limp and lifeless. His paper is wrinkled, a victim of Craig's hands clenching and unclenching."
      Caragh "Oh dear, that doesn't look good."
      hide Craig

    show bg classroom morning with fadeblack
    $CalculateAverageScores()
    if Character_Average.HasPassedExams():
      Caragh "Everyone else seems to be doing well. I'm sure they'll pass."     # LAST LINE
    #+ <C
    else:
      Caragh "It's so tense in here. I hope things go well for the rest of the class."     # LAST LINE
    #show bg black with fade

    #+ Mix "(Put together any combination of the above. The only change is the last line.)"
    #Caragh "Some of them look confident, some of them not so much. Hopefully, most of them will scrape by with a pass."     # LAST LINE
    show bg black with dissolve
    play sound sfx_schoolbell
    Caragh "I guess that's it. The last test is over. All that's left to do is to grade them."
    return

#------------------------------------------------------------------------
label lbl_day_30:
    call update_day(30) from _call_update_day_7
    $dayName = weekDay(current_day)
    scene bg room with dissolve
    play music music_bedroom
    Caragh "This is it. Exam results day!"

    #menu:
    #  "Show scores!":
    #    pass
    ##TODO: Display average scores as a screen instead of text
    #call lbl_show_results(Character_Average)
    #call lbl_show_results(Character_Craig)
    #call lbl_show_results(Character_Hecate)
    #call lbl_show_results(Character_Sanura)

    #"Day 30 (Results)"
    show  bg classroom morning
    stop music
    show Caragh at left
    Description "When Caragh steps into the room, the kids' heads snap to look at her. "
    play music music_5c
    Caragh "\"Good morning, students. I'm sure you're all eager to know your results.\""
    Caragh "\"Lucky for you, your papers are all here and ready for you.\""
    Caragh "\"I'll be handing them out as I go. Feel free to chat while I do so, but don't be too loud.\""
    show  Sanura at right
    Sanura "\"Oh, I'm first! How did I do, Miss Caragh?\""
    Description "Caragh hands Sanura her paper."

    #Flag/Outcome "Grades < C / >= C"


    if Character_Craig.HasPassedExams():
      Caragh "\"Congratulations, Sanura.\""
      Description "When Sanura sees the grade on her paper, her tail swishes faster with joy. Her ears relax from the tense position they were in."
      Sanura "\"I passed!\""
      Sanura "\"Mom's going to be so happy! Thank you, Miss Caragh!\""
      Caragh "\"Don't thank me, Sanura. You did all the hard work.\""
      Caragh "I'm so glad for her. She's come a long way since the start of the month."
    else:
      Description "When Sanura sees the grade on her paper, her ears droop down. Her tail, previously swishing with excitement, goes still. "
      Sanura "\"I...failed.\""
      Sanura "\"Mom's going to be so disappointed.\""
      Caragh "\"There's always next year.\""
      Sanura "\"...\""
      Caragh "I wish I know what to say to her. There's no way I can comfort her by saying her mom will be okay with her grade. That would be a lie."

    hide Sanura
    show  Hecate at right
    Caragh "Next up, Hecate."
    Hecate "\"Well, teach? What did I get?\""
    Description "Caragh hands Hecate her paper."

    #Flag/Outcome "Grades < C / >= C"

    if Character_Craig.HasPassedExams():
      Caragh "\"Congratulations, Hecate. You passed.\""
      Description "When Hecate sees her grade, the sparks around her dance and twinkle around her in various colours"     # What are the limits on animation? Should we do something for the magic or keep it stationary, classic VN style?
      Hecate "\"I knew I could do it!\""
      Hecate "\"The Great Hecate never fails!\""
      Hecate "\"Thanks for your help, Miss Caragh.\""
      Caragh "\"You're welcome.\""
      Caragh "A lone human in a world of monsters will always face challenges. I'm glad Hecate could overcome this one."
    else:
    #+ < C
      Description "When Hecate sees her grade, her entire being freezes. The sparks that were shimmering around her face vanish."
      Hecate "\"A fail.\""
      Hecate "\"It's...fine.\""
      Caragh "\"There's always next year.\""
      Hecate "\"Y-Yeah! I'll show everyone that the Great Hecate won't be foiled by something as simple as a bad grade!\""
      Caragh "At least she can pick herself up. She'll be fine, right?"

    #>= C
    hide Hecate
    show  Craig at right
    Caragh "Now, Craig."
    Craig "\"Miss Caragh?\""
    Description "Caragh hands Craig his paper."

    #Flag/Outcome "Grades < C / >= C"

    if Character_Craig.HasPassedExams():
      Caragh "\"Congratulations, Craig.\""
      Description "Craig perks up at the sight of his grade. His tip of his tail begins to flick and tap."
      Craig "\"I passed.\""
      Craig "\"I passed! I really passed!\""
      Craig "\"Thank you, Miss Caragh!\""
      Caragh "\"No, thank you, Craig. You've worked hard.\""
      Caragh "He's so happy. I wonder how long has it been since his grades brought him joy. I'm glad I could help him."
    else:
    #+ < C
      Description "Craig's tail curls tightly around him as his eyes bores into the grade written on his paper. "
      Craig "\"F-Fail...\""
      Caragh "The heartbreak in his eyes is devastating. I've never felt so bad before for failing a student."
      Caragh "\"There's always next year.\""
      Craig "\"Y-Yes...\""
      Description "Craig sinks further into his seat."
      Caragh "If only..."

    #> = C
    #show  TRANSITION
    #Flag/Outcome "Grades Pass and Mix / Fail"
    hide Craig
    show bg classroom morning with fadeblack
    $CalculateAverageScores()
    if Character_Average.HasPassedExams():
      #+ Pass and Mix
      Caragh "\"Overall, everyone else did quite well. Some of you would do better with more studying but you all did great.\""
    else:
      #+ Fail
      Caragh "\"I understand everyone's worked hard in spite of the circumstances. Unfortunately, a lot of you didn't pass the year-end exams. I hope you guys are able to do better next year.\""

    play sound sfx_schoolbell
    Caragh "\"That's the bell. Have a great holiday, kids.\""
    play music music_quiet
    Caragh "..."
    Caragh "It's the last day. "
    Caragh "Come on, Caragh. You've been through countless \"last days\". This is nothing."
    Caragh "..."
    Caragh "I should be packing up but..."
    Caragh "A few more minutes. I only need a few more minutes."
    Caragh "..."
    Caragh "I'll miss the kids."
    play sound sfx_knock
    show  Nyx at right
    Nyx "\"Hey, Caragh.\""

    #Flag/Outcome "All Fail / Mixed / All Pass"

    $Ending_Flag_passedCount = 0

    if Character_Craig.HasPassedExams():
      $Ending_Flag_passedCount = Ending_Flag_passedCount + 1
    if Character_Hecate.HasPassedExams():
      $Ending_Flag_passedCount = Ending_Flag_passedCount + 1
    if Character_Sanura.HasPassedExams():
      $Ending_Flag_passedCount = Ending_Flag_passedCount + 1
      
    $CalculateAverageScores()
    if Character_Average.HasPassedExams():
      $Ending_Flag_passedCount = Ending_Flag_passedCount + 1



    if Ending_Flag_passedCount == 0:
      call lbl_bad_end from _call_lbl_bad_end
      return

    if Ending_Flag_passedCount < 4:
      Nyx "\"I hear some of your kids failed while some of them passed.\""
      Nyx "\"It's alright. This is your first time working with kids, right?\""
      Nyx "\"Bahini thought you could do it and the kids were okay with you.\""
      Nyx "\"Did you need more time to get used to the place?\""
      Nyx "\"Thanks for helping us when we needed you.\""
      Nyx "\"Oh, we're still looking for Mog's replacement.\""
      Nyx "\"What do you think? I won't push you for an answer now but think on it.\""
      Nyx "\"You'd have more time to get the kids ready for their exams next year.\""
      Nyx "\"Let me know by tomorrow.\""
      hide Nyx
      Caragh "Stay and keep teaching kids?"
      Caragh "Hm..."

    else:
      Nyx "\"I heard all of your kids passed, even the three we were worried about.\""
      Nyx "\"Congratulations on a job well done!\""
      Caragh "\"Thank you, Nyx.\""
      Nyx "\"Have you thought about what you'll be doing after this?\""
      Nyx "\"We are still looking for Mog's replacement. Goodness knows Bahini will be hospitalized again one day.\""
      Nyx "\"After seeing how well you've handled the kids, I think you'd thrive as a teacher here.\""
      Nyx "\"Would you like to stick around?\""
      Nyx "\"No, don't answer me just yet. You just had a big morning.\""
      Nyx "\"Sleep on it and let me know your decision tomorrow.\""
      hide Nyx
      Caragh "Stick around? I didn't think that was possible at the start of this month. "
      Caragh "I..."
      Caragh "Nyx is right. I should sleep on it."
      return

label lbl_day_31:
    call update_day(31) from _call_update_day_8

    #"Day 31 (Only available for mixed and all pass)"
    show bg room
    play music music_bedroom
    Caragh "I have so missed sleeping in. Breaks are the best."
    #play sound sfx_notification
    #show  Phone
    b_phone "Caragh, congratulations on your passing students!"
    b_phone "Oh, and I heard Nyx offered you a job."
    b_phone "Well? What do you think?"
    c_phone "I don't know. "
    c_phone "This is a permanent job and, you know, I have been thinking about taking a break from jumping between schools all the time."
    c_phone "Maybe? I'm not sure if this will be the right job for me."
    c_phone "This month is the only month I've ever taught kids this young."
    b_phone "I understand. It's a big move. I respect your decision, whatever it may be."
    b_phone "But hear me out. Let me plead our case."
    b_phone "If you stay here, you'll be with familiar faces."

    $kidNames = ""
    if Craig_Arc_CurrentEvent == 5:
      $kidNames = kidNames + "Craig"
    if Hecate_Arc_CurrentEvent == 8:
      if not kidNames == "" and Sanura_Arc_CurrentEvent == 9:
        $kidNames = kidNames + ", "
      if not kidNames == "" and not Sanura_Arc_CurrentEvent == 9:
        $kidNames = kidNames + "and "
      $kidNames = kidNames + "Hecate"
    if Sanura_Arc_CurrentEvent == 9:
      if not kidNames == "":
        $kidNames = kidNames + "and "
      $kidNames = kidNames + "Sanura"

    if not kidNames == "" :
      b_phone "You'll see [kidNames] again. I know you've gotten quite close to them."
    b_phone "If you stay, I can help you out with things."
    if Bahini_Arc_CurrentVisit == 3:
      b_phone "If you stay, maybe we can..."
      b_phone "No. No. It is your choice. It'd be unfair of me to dangle that over your head. "
    b_phone "Anyway, my lunch is here. I'll talk to you later!"
    b_phone "I'll be here whenever you've made up your mind."
    if Bahini_Arc_CurrentVisit == 3:
      b_phone "Nothing will change between us."
      b_phone "I promise."
      Caragh "Bahini... "
      scene cg bahini_feed with fade
      #show Bahini
      $ renpy.pause ()
      scene bg room with fade
      Caragh "How can you be so selfless?"
    Caragh "..."
    Caragh "All that's left is to email Nyx my decision."

    #Choice "I... / Go"
    menu:
      Caragh "Should I stay or should I go?"
      "I...":
        #+ Stay
        play music music_sad_vibes
        Caragh "Over the past few weeks, I've grown to love teaching the kids."
        Caragh "They're always so lively, eager for the next thing in life."
        if Craig_Arc_CurrentEvent == 5:
          Caragh "If I go, I won't learn the song Craig's always tapping to."
        if Hecate_Arc_CurrentEvent == 8:
          Caragh "If I go, I won't ever know if Hecate can really burn a building down."
        if Sanura_Arc_CurrentEvent == 9:
          Caragh "If I go, I won't get to watch Sanura's riddling abilities grow."
        Caragh "If I go, life will be the way it was before."
        Caragh "Dull, monotonous, always moving around, always..."
        Caragh "...alone."
        Caragh "I..."
        Caragh "No, I should go."
        Caragh "I've never been good with kids. Did I think one good month is enough to teach me all I need to know about teaching kids for life?"
        if Bahini_Arc_CurrentVisit == 3 and Craig_Arc_CurrentEvent == 5 and Hecate_Arc_CurrentEvent == 8 and Sanura_Arc_CurrentEvent == 9:
          Caragh "I..."
          scene  cg craig_rock with slow_dissolve   # If possible, sequence is arranged according to which ones are "collected" first.
          $ renpy.pause (1.0)
          scene  cg hecate_chat with slow_dissolve
          $ renpy.pause (1.0)
          scene  cg sanura_pat with slow_dissolve
          $ renpy.pause (1.0)
          scene  cg bahini_feed with slow_dissolve   # Optional because I'm not sure if most players would get that at first
          $ renpy.pause (1.0)
          scene bg white with slow_dissolve
          $ renpy.pause (1.0)
          scene bg black with slow_dissolve
          $ renpy.pause (1.0)
          scene cg end_good with slow_dissolve
          play music music_good_vibes
          Caragh "It's only the first day! How can I oversleep?"
          Caragh "Okay, get dressed and then..."
          Caragh "Where's my tablet?"
          Caragh "Ah, there it is!"     # Do we want to extend this ending? It feels a little anti-climactic but I'm out of ideas on how to do this. We can do an epilogue?
          Caragh "Okay, go!"
          show bg white with dissolve
          $ renpy.pause ()
          #scene cg end_good with dissolve
          scene  cg fullcast_photo with slow_dissolve
          Caragh "It's been two years since I sent that email to Nyx."
          Caragh "I can't imagine a life where I sent the other email instead. "
          scene  cg fullcast_photo_B with slow_dissolve
          Caragh "I can't imagine a life without Craig, Hecate, Sanura and, most importantly, Bahini."

          show bg black with dissolve
          Caragh "A teacher's job is never ending however, so I better get to school. My class awaits."
          call lbl_end from _call_lbl_end
        else:
          jump lbl_end_turnDown
        return
      "Go.":
        #+ Go
        play music music_sad_vibes
        Caragh "The past month has been fun."
        Caragh "The kids are always so excited."
        Caragh "It has been amazing, watching Craig, Hecate and Sanura grow and be the best they can be."
        Caragh "But..."
label lbl_end_turnDown:
        Caragh "Maybe my next stop in life will be where I belong. Maybe it won't be."
        Caragh "All I know is that this isn't it."
        c_phone "Hi, Nyx. I am honored that you thought so highly of me but I won't be accepting the offer to stay on as a teacher in Echidna's School for Little Monsters. I've enjoyed my time here. Thank you for having me."
        show bg black with dissolve
        show  cg end_bad
        Caragh "It's been two years since I taught at Echidna's School for Little Monsters."
        Caragh "I never found a place to settle down. I kept moving and moving."
        Caragh "When I have a moment to pause, I find myself thinking back to the time  spent there and the people I met. Every time, I feel a strange tugging at my heart."
        Caragh "I miss them."
        if Craig_Arc_CurrentEvent > 1:
            Caragh "I miss Craig's smile, his enthusiasm for rocks."
        if Hecate_Arc_CurrentEvent > 1:
            Caragh "I miss Hecate and her sparks."
        if Sanura_Arc_CurrentEvent > 1:
            Caragh "I miss Sanura and her unwavering determination at mastering riddles."
        if not Bahini_Arc_CurrentVisit == 0:
            Caragh "Most of all, I miss Bahini. I miss her chirpy messages. I miss her smile."
        Caragh "I tried to keep in contact but..."
        Caragh "There's no use wallowing in regrets. I can't go back in time and change the email."
        Caragh "All I can do is move on and live out my life."
        Caragh "All I can do is move on but..."
        call  lbl_end from _call_lbl_end_1
        return

label lbl_bad_end:
    Nyx "\"I hear most of your kids failed, particularly the three we were worried about.\""
    play music music_sad_vibes
    Nyx "\"I'm disappointed. You were so highly recommended.\""
    Nyx "\"Everyone I spoke to sang your praises.\""
    Nyx "\"Bahini said she had a good feeling about you and the kids like you.\""
    Nyx "\"What happened?\""
    Caragh "\"I-\""
    Nyx "\"No, it's fine. I don't need an answer. I wasn't expecting one anyway.\""
    Nyx "\"I had hoped we've found Mog's replacement.\""
    Nyx "\"I guess it's back to recruiting for me.\""
    Nyx "\"Still, thanks for taking care of 5C the past few weeks.\""
    hide Nyx
    Caragh "Why do I feel so bad?"
    Caragh "I did the best I could, right?"
    show bg black with dissolve
    scene cg end_bad
    Caragh "It's been two years since I taught at Echidna's School for Little Monsters."
    Caragh "I never found a place to settle down. I kept moving and moving."
    Caragh "When I have a moment to pause, I find myself thinking back to the time  spent there and the people I met. Every time, I feel a strange tugging at my heart."
    Caragh "I miss them."
    if Craig_Arc_CurrentEvent > 1:
        Caragh "I miss Craig's smile, his enthusiasm for rocks."
    if Hecate_Arc_CurrentEvent > 1:
        Caragh "I miss Hecate and her sparks."
    if Sanura_Arc_CurrentEvent > 1:
        Caragh "I miss Sanura and her unwavering determination at mastering riddles."
    if not Bahini_Arc_CurrentVisit == 0:
        Caragh "Most of all, I miss Bahini. I miss her chirpy messages. I miss her smile."
    Caragh "I tried to keep in contact but..."
    Caragh "There's no use wallowing in regrets. I can't go back in time and change the email."
    Caragh "All I can do is move on and live out my life."
    Caragh "All I can do is move on but..."
    call lbl_end from _call_lbl_end_2
    return

label lbl_end:

  pause

  return

init:
    image cred = Text("[gui.about!t]\n\nMade with Ren'Py [renpy.version_only]", text_align=0.5, xmaximum=1200)
    image theend = Text("{size=80}Fin", text_align=0.5)
    image thanks = Text("{size=80}Thanks for playing!", text_align=0.5)

label lbl_credits_from_menu:
    call lbl_credits from _call_lbl_credits
    return
    
label lbl_credits:
        
    $ quick_menu = False

    $ credits_speed = 20
    scene bg black
    with dissolve
    show cred at Move((0.5, 1.9), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    
    $ renpy.end_replay()
    
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks with dissolve
        
    $ quick_menu = True

    return





#------------------------------------------------------------------------
label lbl_show_results(character):
    if character.History >= 70:
      "[character.Name] has passed History."
    else:
      "[character.Name] has failed History."

    if character.Science >= 70:
      "[character.Name] has passed Science."
    else:
      "[character.Name] has failed Science."

    if character.Math >= 70:
      "[character.Name] has passed Math."
    else:
      "[character.Name] has failed Math."

    if character.Literacy >= 70:
      "[character.Name] has passed Literacy."
    else:
      "[character.Name] has failed Literacy."

    if character.Language >= 70:
      "[character.Name] has passed Language."
    else:
      "[character.Name] has failed Language."

    if character.Geography >= 70:
      "[character.Name] has passed Geography."
    else:
      "[character.Name] has failed Geography."

    return

#------------------------------------------------------------------------

