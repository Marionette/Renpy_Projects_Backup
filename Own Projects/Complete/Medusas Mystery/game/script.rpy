# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")


# The game starts here.

label start:
    #scene bg kitchen
    
    #show medusa at show_medusa
    
    call lbl_intro from _call_lbl_intro
    
label lbl_investigation_loop:
    menu:
      "Investigate!":
        call lbl_investigation from _call_lbl_investigation
        $haveInvestigated = True
        jump lbl_investigation_loop
      "Interrogate!":
        call lbl_interrogation from _call_lbl_interrogation
        $haveInterrogated = True
        jump lbl_investigation_loop
      "Accuse!" if haveInvestigated and haveInterrogated:
        call lbl_accusation from _call_lbl_accusation
    
    #call lbl_audioTest
    #
    #call lbl_paramTest("Agnesss", "seconds")
    #call lbl_paramTest(_name="Daisssy", _time="minutes")
    #call lbl_paramTest(_time="miliseconds", _name="Everyone simultaneously")
    #call lbl_paramTest
    
    return
    
#------------------------ Misc repeated lines
label lbl_everyoneNods:
  show medusa at show_medusa_head_nod
  everyone "*nods in unison*"
  return


#------------------------ 
label lbl_intro:
  scene bg black
  
  #intro
  $notgood = _("This is not good")
  a "[notgood]."
  a "[notgood] at all."
  
  show medusa at show_medusa_instant with dissolve
  a "Pssst everyone wake up."
  show medusa at show_snake2
  b "Huh? What is it?"
  show medusa aexasp at show_snake1
  a "Shhhh, don't wake Melissa"
  show medusa at show_snake4
  d "What's going on?"
  play music music_all
  #show medusa at show_snake1
  hide medusa
  show bg kitchen at show_donut
  a "The [persistent.donut_spelling] has a bite missing."
  show medusa escared at show_snake5
  e "Are you serious?!"
  show medusa bscared at show_snake2
  b "Oh My God."
  show medusa fworried at show_snake6
  f "Melissa was looking forward to that [persistent.donut_spelling]."
  show medusa at show_snake4
  d "She specifically said not to touch it!"
  show medusa at show_snake1
  a "Who did it?"
  show medusa at show_medusa_head
  everyone "..."
  show medusa at show_snake1
  a "Unless the culprit turns themselves in we'll all be in trouble."
  show medusa at show_medusa_head
  everyone "..."
  show medusa aglass at show_snake1
  a "I guess we are doing this the hard way."
  show medusa dwink at show_snake4 #show_medusa_instant #
  d "Detective Agnesss is on the case!"
  show medusa aexasp at show_snake1
  a "Don't get too excited, you're also a suspect!"
  show medusa at show_snake4
  d "Wha?!"
  show medusa at show_snake3
  c "Aren't you a suspect too?!"
  show medusa fsarcastic at show_snake6
  f "Like 'Saint Agnesss' would ever do anything interesting like that."
  show medusa esrs at show_snake5
  e "She's got a point, you being such a square and all."
  call lbl_everyoneNods from _call_lbl_everyoneNods
  show medusa aexasp at show_snake1
  a "...ANYWAYS!"
  
  #timeline
  show medusa at show_snake1
  a "Let's walk through the time leading up to the crime."
  show medusa at show_snake2
  b "Ok so we arrived home at like 8pm"
  show medusa at show_snake4
  d "Which was later than usual..."
  show medusa at show_snake5
  e "...because Melissa just finished closing out that last case."
  show medusa dwink at show_snake4
  d "No crime can sneak past the watchful eye of Detective Melissa!"
  show medusa fsarcastic at show_snake6
  f "...except this one."
  show medusa at show_snake4
  d "Ok, but like when she's awake."
  show medusa at show_snake6
  f "Of course."
  show medusa at show_medusa
  call lbl_everyoneNods from _call_lbl_everyoneNods_1
  show medusa aexasp at show_snake1
  a "We're getting off track!"
  show medusa at show_snake3
  c "So after we got home Melissa took the [persistent.donut_spelling] out of the cupboard"
  show medusa at show_snake2
  b "She got it this morning from her favourite bakery"
  show medusa at show_snake5
  e "But when she sat at the table, the days' exhaustion hit her."
  show medusa at show_snake6
  f "All of us really."
  show medusa at show_snake4
  d "So we like decided to take a quick nap, like 10 minutes max."
  show medusa aexasp at show_snake1
  a "But it's like 11pm now."
  show medusa fsarcastic at show_snake6
  f "Yeah, I've no idea how, these chairs aren't that comfortable."
  show medusa at show_snake1
  a "So we came home and slept in front of the [persistent.donut_spelling]."
  show medusa at show_snake4
  d "Pretty much."
  show medusa aglass at show_snake1
  a "Alright, that covers the lead-up, next I need to look for clues."
  
  return

#---------------------------------------------------------------
label lbl_finishup(_text = "done"):
  menu:
    "I'm [_text].":
      return True
    "Wait...":
      return False

label lbl_investigation:
  show bg kitchen
  play music music_mystery fadein 1.0
  show medusa aglass at show_snake1
  a "Let's check out the crime scene!"
  
  
label lbl_investigation_screen:
  call screen investigation_screen
  
  $res = _return
  
  show medusa at show_snake1
  if res == "donut":
    play music music_kick
    queue music music_mystery
    "Our victim, a delicious [persistent.donut_spelling], but with a large bite taken out of it."
  else:
    if res == "sandwich" : 
      $crumbsFound = True
      "The remains of a jam sandwich, whoever finished this off made a mess, there are crumbs everywhere."
    else:
      if res == "tjuice" : 
        "Tomato Juice, Yuck. Only two snakes drink this stuff, probably because it looks like blood."
      else:
        if res == "window" : 
          "It's still dark out." # The perfect time for a crime."
        else:
          #if res == "table" : 
          #  "A large wooden table, how Melissa managed to fall asleep at it is beyond me."
          #else: 
          "I don't think that's relevant to my investigation."
  
  call lbl_finishup("done") from _call_lbl_finishup
  $isDone =  _return
  if not isDone:
    jump lbl_investigation_screen
  
  return
  
screen investigation_screen:
  
  style_prefix "invisible"
  
  add "images/bg_kitchen.png"
  add "images/item_donut.png"
  
  #vbox:
  textbutton " " action Return("anythingelse")xpos 0 ypos 0 xsize 1980 ysize 1080
  #textbutton " " action Return("table")xpos 0 ypos 750 xsize 1920 ysize 330
  textbutton " " action Return("donut") xpos 950 ypos 750 xsize 400 ysize 200
  textbutton " " action Return("sandwich")xpos 1500 ypos 570 xsize 200 ysize 200
  textbutton " " action Return("tjuice")xpos 950 ypos 570 xsize 200 ysize 200
  textbutton " " action Return("window")xpos 0 ypos 0 xsize 600 ysize 670

style invisible_button is gui_button

#style invisible_button:
#  hover_background "#123456"
#---------------------------------------------------------------
label lbl_pickSelf:
    show medusa at show_snake1
    a "Why would I pick myself?" 
    return
    
label lbl_interrogation:
  play music music_interrogation fadein 1.0
  scene bg black
  show medusa aglass at show_snake1
  a "Let's interrogate the suspects!"

  
label lbl_interrogation_screen:
  call screen interrogation_screen
  
  $res = _return
    
  if res == "a":
    show medusa at show_snake1
    call lbl_pickSelf from _call_lbl_pickSelf
    jump lbl_interrogation_screen
  if res == "b": 
    show medusa at show_snake2
    call lbl_interrogation_B from _call_lbl_interrogation_B
  if res == "c":
    show medusa at show_snake3
    call lbl_interrogation_C from _call_lbl_interrogation_C
  if res == "d": 
    show medusa at show_snake4
    call lbl_interrogation_D from _call_lbl_interrogation_D
  if res == "e": 
    show medusa at show_snake5
    call lbl_interrogation_E from _call_lbl_interrogation_E
  if res == "f":
    show medusa at show_snake6
    call lbl_interrogation_F from _call_lbl_interrogation_F
  if res == "m":
    show medusa at show_medusa_head
    a "Better let her sleep."
    jump lbl_interrogation_screen
  
  call lbl_finishup("done") from _call_lbl_finishup_1
  $isDone =  _return
  if not isDone:
    jump lbl_interrogation_screen
  
  return
  
label lbl_interrogation_questions:
  menu:
    "Tell me what you did between 8pm and 11pm":
      return "alibi"
    "Then how do you explain...":
      return "clue"
    "Anything else you'd like to say?":
      return "extra"
      
label lbl_interrogation_questions_more:
  menu:
    "That's all":
      return "done"
    "Actually...":
      return "more"
      
label lbl_interrogation_more_info:
  #show medusa at show_snake1
  a "I'm gonna need more info to push this."
  return
  
label lbl_interrogation_nothing(_name="Nobody"):
  $Any_name  = _name
  named "Nope."
  return
  
#---Interrogations Start---#      
label lbl_interrogation_B:
  call lbl_interrogation_questions from _call_lbl_interrogation_questions
  $question = _return
  if question == "alibi":
    show medusa at show_snake2
    b "Where's my lawyer?!"
    show medusa at show_snake1
    a "Calm down, this isn't one of your cop shows."
    show medusa bsad at show_snake2
    b "*sigh* Before I went to sleep I made a bet with Elissse, around 8:30, that I could go without eating for a whole day."
    show medusa at show_snake2
    b "So obviously I couldn't have done it. Since I'm tough."
  if question == "clue":
    show medusa aglass at show_snake1
    a "These crumbs!"
    if not crumbsFound == True and not sandwichEatingSeen == True:
      show medusa at show_snake2
      b "I've no idea what you are talking about."
      call lbl_interrogation_more_info from _call_lbl_interrogation_more_info
    else:
      if crumbsFound:
        show medusa at show_snake1
        a "They look like sandwich crumbs"
      else:
        if sandwichEatingSeen:
          show medusa at show_snake1
          a "Elissse said she saw you eating a sandwich."
      show medusa bsad at show_snake2
      b "You got me. Guess I lose the bet, fair and square."
      show medusa at show_snake1
      a "If you were sneaking food..."
      show medusa at show_snake2
      b "Fair. And. Square."
      show medusa aexasp at show_snake1
      $ok = "Ok"
      $ok2 = ok + " " + ok
      a "[ok2]."
  if question == "extra":
      call lbl_interrogation_nothing("Beatrisss") from _call_lbl_interrogation_nothing
  
  
  call lbl_interrogation_questions_more from _call_lbl_interrogation_questions_more  
  if _return == "more":
      jump lbl_interrogation_B
      
  return
  
label lbl_interrogation_C:
  call lbl_interrogation_questions from _call_lbl_interrogation_questions_1
  $question = _return
  if question == "alibi":
    show medusa chappytears at show_snake3
    c "What are you saying?"
    show medusa at show_snake1
    a "Just trying to piece together what happened."
    show medusa at show_snake3
    c "The only time I woke up was at around 10, and I saw Beatrisss and Francesssca sniffing around."
    show medusa at show_snake3
    c "They were being mighty suspicious if you ask me."
    show medusa at show_snake1
    a "Oh, what were they doing? "
    show medusa at show_snake3
    c "I don't know, but they looked like they maybe finished eating or something."

  if question == "clue":
      show medusa aglass at show_snake1
      a "The sprinkles on your face!"
      show medusa csus at show_snake3
      c "Must've fallen off the true culprit onto me!"
  if question == "extra":
      call lbl_interrogation_nothing("Casssie") from _call_lbl_interrogation_nothing_1
  
  
  call lbl_interrogation_questions_more from _call_lbl_interrogation_questions_more_1  
  if _return == "more":
      jump lbl_interrogation_C
      
  return
  
label lbl_interrogation_D:
  call lbl_interrogation_questions from _call_lbl_interrogation_questions_2
  $question = _return
  if question == "alibi":
    show medusa at show_snake4
    d "I went to sleep at the same time as Elissse and Beatrisss. They were talking about eating or something."
    show medusa at show_snake1
    a "Eating a [persistent.donut_spelling]?"
    show medusa at show_snake4
    d "I dunno, but like it was about how tough Beatrisss was or something. I didn't really get it."
  if question == "clue":
    show medusa aglass at show_snake1
    a "The sweetness on your breath!"
    show medusa dwink at show_snake4
    d "OH LOL, I was really hungry when we got back so I had a jam sandwich."
    show medusa at show_snake1
    a "Jam sandwich?"
    show medusa dwink at show_snake4
    d "Yeah!"
    show medusa aexasp at show_snake1
    a "...Right."
  if question == "extra":
    show medusa at show_snake4
    d "Oh, I woke up later and I think saw Elissse and Francesssca arguing."
    show medusa at show_snake1
    a "What time was this?"
    show medusa at show_snake4
    d "*shrugs* I was tired and went right back to sleep."
      
  
  call lbl_interrogation_questions_more from _call_lbl_interrogation_questions_more_2  
  if _return == "more":
      jump lbl_interrogation_D
      
  return
  
label lbl_interrogation_E:
  call lbl_interrogation_questions from _call_lbl_interrogation_questions_3
  $question = _return
  if question == "alibi":
    show medusa esrs at show_snake5
    e "I was too busy fighting Ninjas to keep track. See this scar?"
    show medusa at show_snake1
    a "That you've drawn on yourself?"
    show medusa esrs at show_snake5
    e "Ninjas."
    show medusa at show_snake5
    e "They woke Francesssca, but I calmed her with a blood offering."
    show medusa at show_snake1
    a "Blood?"
    show medusa esrs at show_snake5
    e "Yes at 9:30, then she rested. She would need her strength for battles to come."
    show medusa aexasp at show_snake1
    a "I'm just not gonna ask."
  if question == "clue":
    show medusa aglass at show_snake1
    a "These sprinkles on your head!"
    show medusa esrs at show_snake5
    e "No doubt placed there by THEM in an attempt to frame me!"

  if question == "extra":
    $ sandwichEatingSeen = True
    show medusa at show_snake5
    e "Oh, I did see Daisssy eat a sandwich before we went to sleep."
    show medusa at show_snake5
    e "Even saw Beatrisss finish it off!"
    show medusa esrs at show_snake5
    e "We had an agreement where she would not eat to display her strength of will!"
    show medusa esrs at show_snake5
    e "She failed!"
  
  
  call lbl_interrogation_questions_more from _call_lbl_interrogation_questions_more_3  
  if _return == "more":
      jump lbl_interrogation_E
      
  return
  
label lbl_interrogation_F:
  call lbl_interrogation_questions from _call_lbl_interrogation_questions_4
  $question = _return
  if question == "alibi":
    show medusa fsarcastic at show_snake6
    f "Ugh, do I have to play along with this?"
    show medusa at show_snake1
    a "Just humor me."
    show medusa fsarcastic at show_snake6
    f "*sigh* Elissse woke me up shouting about something stupid, as usual, at around 9:30."
    show medusa fsarcastic at show_snake6
    f "As far as I could tell everyone was sleeping."
    show medusa fsarcastic at show_snake6
    f "I got a drink and then went back to sleep."
  if question == "clue":
    show medusa aglass at show_snake1
    a "Your Redish lips!"
    show medusa fsarcastic at show_snake6
    f "Really? That's the best you'd got?"
    show medusa fsarcastic at show_snake6
    f "It's Tomato Juice."
    show medusa at show_snake1
    a "Yuck."
    show medusa fsarcastic at show_snake6
    f "You have no taste."
  if question == "extra":
    show medusa fsarcastic at show_snake6
    f "I don't eat sweet things."
    show medusa at show_snake1
    a "That's it?"
    show medusa fsarcastic at show_snake6
    f "That's it."
  
  
  call lbl_interrogation_questions_more from _call_lbl_interrogation_questions_more_4 
  if _return == "more":
      jump lbl_interrogation_F
      
  return
  
  
#---Interrogations End---#  
screen interrogation_screen:
  style_prefix "invisible"
  add "images/bg_kitchen.png"
  add "images/item_donut.png"
  add ImageReference("medusa") at show_medusa_close
  
  #vbox:
  textbutton " " action Return("a")xpos 330 ypos 370 xsize 200 ysize 200
  textbutton " " action Return("b")xpos 540 ypos 175 xsize 200 ysize 200
  textbutton " " action Return("c") xpos 1330 ypos 130 xsize 200 ysize 200
  textbutton " " action Return("d")xpos 800 ypos 40 xsize 200 ysize 200
  textbutton " " action Return("e")xpos 1420 ypos 690 xsize 200 ysize 200
  textbutton " " action Return("f")xpos 1420 ypos 340 xsize 200 ysize 200
  textbutton " " action Return("m")xpos 880 ypos 370 xsize 400 ysize 400
  

#---------------------------------------------------------------
label lbl_accusation:
  play music music_mystery fadein 1.0
  scene bg kitchen
  show medusa aglass at show_snake1
  a "The culprit is..."

  
label lbl_accusation_screen:
  call screen interrogation_screen
  
  $res = _return
  
  #"You picked [res]"
  call lbl_finishup("sure") from _call_lbl_finishup_2
  $isSure =  _return
  if not isSure:
    jump lbl_accusation_screen
  
  if res == "a":
    #Accuse Agnesss: 
    show medusa aexasp at show_snake1    
    call lbl_pickSelf from _call_lbl_pickSelf_1
    jump lbl_accusation
  if res == "b":
    #Accuse Beatrisss: (Incorrect) 
    show medusa at show_snake2
    b "Doing time for a crime I didn't commit? Classic." 
    call lbl_ending_3("Beatrisss") from _call_lbl_ending_3
  if res == "c":
    #Accuse Casssie:  (Correct) 
    show medusa at show_snake3
    c "All right you caught me!" #(choose to forgive: jump lbl_ending_1; else jump lbl_ending_2)
    menu:
      "Turn her in...":
        jump lbl_ending_2
      "Or...":
        jump lbl_ending_1
  if res == "d":
    #Accuse Daisssy: (Incorrect) 
    show medusa dwink at show_snake4
    d "You're picking me? So what do I win?" 
    call lbl_ending_3("Daisssy") from _call_lbl_ending_3_1
  if res == "e":
    #Accuse Elissse: (Incorrect) 
    show medusa esrs at show_snake5
    e "You've been sent by THEM to take me out, haven't you?!" 
    call lbl_ending_3("Elissse") from _call_lbl_ending_3_2
  if res == "f":
    #Accuse Francesssca: (Incorrect) 
    show medusa fsarcastic at show_snake6
    f "Wow, you're really doing this. Ok." 
    call lbl_ending_3("Francesssca") from _call_lbl_ending_3_3
  if res == "m":
    #Accuse Melissa:  (Incorrect) 
    show medusa at show_medusa_close
    m "..."
    jump lbl_ending_4
  
  return
  
#---------------------------------------------------------------

label lbl_interrogation_gulp(_name="Nobody"):
  $Any_name  = _name
  named "*Gulp*"
  return
  
#Result
label lbl_ending_1:
#Ending 1 – All for 1
  $ending = 1
  show medusa at show_snake3
  c "I'll take responsibility to spare the rest of you!"
  show medusa at show_snake1
  a "There is another option."
  show medusa at show_snake3
  c "Really?"
  show medusa at show_snake1
  a "*whisper whisper*"
  show medusa chappytears at show_snake3
  c "You guys would do that for me?"
  show medusa at show_snake1
  a "Ok on the count of 3."
  show medusa chappytears at show_medusa_head
  everyone "...3!"
  call lbl_ending_mid("Everyone") from _call_lbl_ending_mid
  #jump lbl_ending_final
  centered "Ending 1: All for One!"
  $ persistent.ending_seen_1 = True 
  
  jump lbl_credits
  return

label lbl_ending_2:
  #Ending 2 – In for a Penny
  $ending = 2
  show medusa at show_snake1
  a "We are going to turn you in as soon as Melissa wakes up."
  show medusa at show_snake3
  call lbl_ending_mid("Casssie") from _call_lbl_ending_mid_1
  centered "Ending 2: In for a Penny..."
  $ persistent.ending_seen_2 = True
  
  jump lbl_credits
  return

label lbl_ending_3(_name="Nobody"):
  #Ending 3 - Falsely Accused
  $ending = 3
  call lbl_ending_mid(_name) from _call_lbl_ending_mid_2
  if _name == "Daisssy":
    centered "Ending 3B: Falsely Accused (Oblivious)"
    $ persistent.ending_seen_3B = True
  else:
    centered "Ending 3: Falsely Accused"
    $ persistent.ending_seen_3 = True
  
  jump lbl_credits
  return

label lbl_ending_mid(_name="Nobody"):
  $Any_name  = _name
  if not _name == "Everyone":
    if _name == "Daisssy":
      named "The [persistent.donut_spelling]?"
    else:
      named "Well if this is how it's going to be."
  "[_name] lunges for the [persistent.donut_spelling] and takes a bite."
  if not ending == 1:
    everyone "What are you doing?!"
  hide medusa
  show bg kitchen nodonut at show_donut
  "It's not long before the whole thing is gone."
  jump lbl_ending_final
  
label lbl_ending_final:
  "The commotion wakes Melissa"
  if not Any_name  == "Daisssy":
    show medusa at show_medusa   
  else:    
    show medusa dwink at show_medusa
  m "What's going on?"
  
  if not Any_name  == "Daisssy":
    show medusa mad at show_medusa_close 
  else:    
    show medusa mad dwink at show_medusa_close   
  m "...Where is my [persistent.donut_spelling]?"
  if not Any_name  == "Daisssy":
    call lbl_interrogation_gulp(Any_name) from _call_lbl_interrogation_gulp
    
  scene bg black with fade
  return


label lbl_ending_4:
  #Ending 4 – Gaslighting?
  $ending = 4
  show medusa at show_snake1
  a "The only possible explanation is that Melissa ate it herself."
  show medusa at show_medusa
  m "Oh?"
  show medusa at show_snake1
  a "Everyone's alibi checks out and we all know how much of a glutton she is..."
  show medusa at show_medusa
  everyone "Shhhhhhhhhhhhhhhhhhh!"
  show medusa mad at show_medusa_close
  m "Is that so."
  show medusa mad at show_snake1
  a "W-what I mean is..."
  show medusa mad at show_medusa
  m "Well then, oh great DETECTIVE..."
  show medusa mad at show_medusa_close
  m "If I ate it myself then why am I still hungry?"
  #show medusa at show_snake1
  a "..."
  show medusa mad at show_medusa_closer
  m "Hmmmmmmmm?!"
  show medusa mad at show_snake1
  call lbl_interrogation_gulp("Angnesss") from _call_lbl_interrogation_gulp_1
  scene bg black with fade
  centered "Ending 4: A Bold Move, Let's see if it pays off."
  $ persistent.ending_seen_4 = True
  
  jump lbl_credits
  return

init:
    image cred = Text("[gui.about!t]\n\nMade with Ren'Py [renpy.version_only]", text_align=0.5, xmaximum=1200)
    image theend = Text("{size=80}Fin", text_align=0.5)
    #image thanks = Text("{size=80}Thanks for playing!", text_align=0.5)

label lbl_credits_from_menu:
    call lbl_credits from _call_lbl_credits
    return
    
label lbl_credits:
        
    #if (_in_replay):
    #    play music ending fadein 1.0
    #else:
    #    $ending_track = "audio/music/ending_" + ending_theme + ".mp3"
    #    play music ending_track fadein 1.0

    $ quick_menu = False

    $ credits_speed = 20
    scene bg black
    with dissolve
    show cred at Move((0.5, 1.2), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    
    $ renpy.end_replay()
    
    #show thanks:
    #    yanchor 0.5 ypos 0.5
    #    xanchor 0.5 xpos 0.5
    #with dissolve
    #with Pause(3)
    #hide thanks with dissolve

    #if persistent.extras_unlocked:
    #
    #    pass
    #
    #else:
    #
    #    centered "You've unlocked the Endings Menu.\nAccess it through the Main Menu."
    #
    #    $ persistent.extras_unlocked = True
        
    $ quick_menu = True

    return




