# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black
    
    jump story_start

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    rf "You've created a new Ren'Py game."

    rf "Once you add a story, pictures, and music, you can release it to the world!"
    
    menu:
      "Dare to Continue?"
      "Yes":
        show catscare movie:
          yalign 0.5
          xalign 0.5
        "Boo!"
        pass
      "No":
        pass

    # This ends the game.
    
    
    "email test"
    
    $ name = "Robert"
    $ mail = []
    $ mail_later = []
    $ mail_queue = []
    $ contacts = []     
    
    #jump lbl_end
    $new_messages = new_message_count()
    
    scene black with dissolve
    
    $email_active = True
    
    call lbl_Email_IT_Maintenance_start from _call_lbl_Email_IT_Maintenance_start
    call lbl_Email_Dave_Phone_start from _call_lbl_Email_Dave_Phone_start
    call lbl_Email_Derek_Party_start from _call_lbl_Email_Derek_Party_start
    
    call lbl_Email_ChainLetter_start from _call_lbl_Email_ChainLetter_start
    
    #---
    call lbl_Email_Dave_Phone_start() from _call_lbl_Email_Dave_Phone_start_1
    call lbl_Email_Dave_Days_start() from _call_lbl_Email_Dave_Days_start
    call lbl_Email_Dave_Party_start() from _call_lbl_Email_Dave_Party_start
    call lbl_Email_Dave_Bannister_start() from _call_lbl_Email_Dave_Bannister_start
    call lbl_Email_Dave_Feeling_start() from _call_lbl_Email_Dave_Feeling_start
    call  lbl_Email_Dave_Birds_start() from _call_lbl_Email_Dave_Birds_start
    call  lbl_Email_Dave_Need_Sleep_start() from _call_lbl_Email_Dave_Need_Sleep_start
    call  lbl_Email_Dave_Bed_start() from _call_lbl_Email_Dave_Bed_start
    call  lbl_Email_Dave_cant_sleep_start() from _call_lbl_Email_Dave_cant_sleep_start
    call  lbl_Email_Dave_Freaking_Out_start() from _call_lbl_Email_Dave_Freaking_Out_start
    call  lbl_Email_Dave_You_Awake_start() from _call_lbl_Email_Dave_You_Awake_start
    call  lbl_Email_Dave_Dude_start() from _call_lbl_Email_Dave_Dude_start
    call  lbl_Email_Dave_Seriously_start() from _call_lbl_Email_Dave_Seriously_start
    call  lbl_Email_Dave_Respond_start() from _call_lbl_Email_Dave_Respond_start
    call  lbl_Email_Dave_Sent_On_start() from _call_lbl_Email_Dave_Sent_On_start
    call  lbl_Email_Dave_Didnt_Work_start() from _call_lbl_Email_Dave_Didnt_Work_start
    call  lbl_Email_Dave_Fuck_1_start() from _call_lbl_Email_Dave_Fuck_1_start
    call  lbl_Email_Dave_Fuck_2_start() from _call_lbl_Email_Dave_Fuck_2_start
    call  lbl_Email_Dave_Fuck_3_start() from _call_lbl_Email_Dave_Fuck_3_start
    call  lbl_Email_Dave_Fuck_4_start() from _call_lbl_Email_Dave_Fuck_4_start
    call  lbl_Email_Dave_Fuck_5_start() from _call_lbl_Email_Dave_Fuck_5_start
    call  lbl_Email_Dave_Fuck_6_start() from _call_lbl_Email_Dave_Fuck_6_start
    call  lbl_Email_Dave_Fuck_7_start() from _call_lbl_Email_Dave_Fuck_7_start
    call  lbl_Email_Dave_Fuck_8_start() from _call_lbl_Email_Dave_Fuck_8_start
    call  lbl_Email_Dave_Here_start() from _call_lbl_Email_Dave_Here_start
    call  lbl_Email_Dave_Thanks_start() from _call_lbl_Email_Dave_Thanks_start
    #---

    
    #call lbl_Email_Tutorial_Start from _call_lbl_Email_Tutorial_Start
    
    "Maybe i should check my emails?"
    
    #call screen email_menu(True)
    
    "A new email?"
    
label email_loop:
    menu:
      "Next":
        $deliver_next()
        $add_next()
      "All":
        $ add_now()
      "None":
        pass
    "."
    
    jump email_loop
    
    
    "end test"

    return


label story_start():
    
  $ name = "Robert"
  $ mail = []
  $ mail_later = []
  $ mail_queue = []
  $ contacts = []     
    
  
  scene bg black
  play music music_Melancholy fadeout 1.0
  "I turn off the TV and set the remote down having finally finished the last episode of the new season. "
  rf "Ended on a cliffhanger as expected, but still well worth the binge."
  
  "\'3pm\' I read from my watch."
  rf "Not a bad way to spend a Friday when you have no classes, but I should probably do some studying before I start anything new."
  
  #chair scrape noise?
  scene bg desk day1
  
  rf "Well i can't start anything before I check my emails. After all there might be important information present."
  
  $email_active = True
  "Classic procrastinator move."
  
  #call lbl_Email_IT_Maintenance_start
  
  call lbl_Email_IT_Maintenance_DontPanic1 from _call_lbl_Email_IT_Maintenance_DontPanic1_1
  call lbl_Email_IT_Maintenance_DontPanic2 from _call_lbl_Email_IT_Maintenance_DontPanic2_1
  call lbl_Email_IT_Maintenance_ScheduledMaintenance1 from _call_lbl_Email_IT_Maintenance_ScheduledMaintenance1_1
  call lbl_Email_IT_Maintenance_ScheduledMaintenance2 from _call_lbl_Email_IT_Maintenance_ScheduledMaintenance2_1
  call lbl_Email_Dave_Phone_start() from _call_lbl_Email_Dave_Phone_start_2
  call lbl_Email_IT_Maintenance_ScheduledMaintenance3 from _call_lbl_Email_IT_Maintenance_ScheduledMaintenance3_1
  $deliver_next()
  $add_next()
  
label email_loop1:
  if not email_response_dave1:
    "Looks like  got an email from Dave, maybe i should reply?"
    jump email_loop1
    
  $deliver_next()
  $add_next()
  "Oh that was quick, I guess Dave is online right now."
  
  "..."
  
  "Ok, I've put it off long enough. Time to get some studying done."
  
  call lbl_Email_Derek_Party() from _call_lbl_Email_Derek_Party_1
  call lbl_Email_Derek_Party1() from _call_lbl_Email_Derek_Party1_1
  call lbl_Email_Derek_Party2() from _call_lbl_Email_Derek_Party2_1
  play music music_Mystery fadeout 1.0
  call lbl_Email_ChainLetter_start from _call_lbl_Email_ChainLetter_start_1
  call lbl_Email_Derek_Party3() from _call_lbl_Email_Derek_Party3_1
  
  "..."
  "Wait what?..."
  "Oh, i get it..."
  "Is that a chain mail? Do people even still send those around?"
  
label email_loop2:
  if not forward_Curse_Anne:
    rf "Maybe i should send it on to Anne, she loves this sort of thing, urban legends and stuff."
    jump email_loop2
  else:
    if not anne_once:
      $anne_once = True
      rf "Did she get locked out again? I'll have to ask her next time I'm down home."
      "Anne may be my sister but technology was never her strong suit."
  
label email_loop3:
  if not forward_Curse_Dave:
    rf "Maybe i should send it on to Dave, he might get a kick out of a \'curse\' this close to Halloween."
    jump email_loop2
  
  scene bg desk day2
  
  #4pm
  play music music_Melancholy fadeout 1.0
  rf "Its only 4pm? Ugh, this stuff is so boring it feels like I've been at this for hours."
  call lbl_Email_Dave_Days_start() from _call_lbl_Email_Dave_Days_start_1
  rf "Maybe ill take a little break."
  "I play a game on my computer for a while."
  #5
  call lbl_Email_Dave_Party_start() from _call_lbl_Email_Dave_Party_start_1
  "Ok i better get back to studying."
  "..."
  "Hmm..."
  "I see..."
  #6 - dinner
  "My stomach grumbles, reminding me that it exists and i should feed it."
  rf "6pm already? I guess time really does fly when you're having \'Fun\'."
  call lbl_Email_Dave_Bannister_start() from _call_lbl_Email_Dave_Bannister_start_1
  
  scene bg black
  "I fix myself a simple dinner. It's nothing fancy but considering the ingredients i had to work with it didn't turn out too bad."
  
  "..."
  "Unfortunately i made too much. Normally its fine since my housemate would eat any left-overs but since he has gone home for the weekend I'm the only one here."
  
  rf "Waste not want not."
  
  "It doesn't take long for it to become \'Waist not\'"
  
  rf "Ugh. I need to digest this before i go back to studying."
  
  
  "I slump into the sofa and regret my life choices."
  
  #7
  scene bg desk evening
  play music music_LonelyHouse fadeout 1.0
  call lbl_Email_Dave_Feeling_start() from _call_lbl_Email_Dave_Feeling_start_1
  "Its nearly 7pm by the time i drag myself off the sofa and go back to my desk."
  
  "I decide to pick another subject to study, telling myself its to mix it up a little."
  "..."
  "....?"
  "oh....OH"
  
  #8 - Storm
  play ambient sound_rain_inside
  "I snap out of \'the zone\' with the realization that it has started to rain pretty hard."
  scene bg desk night1
  call  lbl_Email_Dave_Birds_start() from _call_lbl_Email_Dave_Birds_start_1
  
  "It has also gotten pretty dark. I reach over to turn on my lamp."
  scene bg desk night2
  rf "Much better."
  
label email_loop4:
  if not email_response_dave2:
    rf "What has gotten into Dave, maybe I should email him back?"
    jump email_loop4
  
  "I decide to listen to some music while i wind down for the evening."  
  play music music_Loneliness fadeout 1.0
  #9
  "The rain seems to be getting heavier."
  rf "I'd have expected to hear about a storm like this on the forecast, but i guess the ones here are about as reliable as looking at the sky and guessing myself."
  call  lbl_Email_Dave_Need_Sleep_start() from _call_lbl_Email_Dave_Need_Sleep_start_1
  
label email_loop5:
  if not email_response_dave3:
    rf "Dave seems to be losing it. I should get back to him."
    jump email_loop5
    
  "Remembering that i still need to finish off one of my other assignments, i decide to quickly do it now so i have the rest of the weekend free."
  
  "..."
  "..."
  #10 - Blackout
  call  lbl_Email_Dave_Bed_start() from _call_lbl_Email_Dave_Bed_start_1
  "...aannd done. Finally."
  
  
label email_loop6:
  if not email_response_dave4:
    rf "Dave really needs to get some sleep. I should wish him a good night."
    jump email_loop6
  
  stop music
  $email_active = False
  scene bg desk blackout
  play ambient sound_rain_inside
  "Suddenly the power goes out."
  rf "What?!"
  "All i can hear is the sound of the rain, as my desk is illuminated by the moonlight."
  "I squint and try to read the time on my watch, it's just after 10pm."
  
  "I wait a while after digging out some candles to see if the power comes back on, but it doesn't seem to have any intention of returning."
  
  rf "Guess theres not much i can do about it, so i might as well turn in early."
  #Sleep
  scene bg black
  
  "I climb into bed and drift off to sleep."
  "I wonder if Dave also got to sleep, Lord knows he needs it."
  "..."
  #Lights on
  scene bg white
  "I have awoke suddenly by a blinding light."
  rf "Ah what the hell"
  "I blink a lot trying to figure out what is going on."
  
  rf "Oh i guess the lights are back on."
  "After a while of sitting on my bed waiting for my eyes to adjust, i check my watch."
  
  rf "1am? fuuuuck."
  "I yawn deeply. I want to go back to bed but even if i do It'll take a while to fall asleep so i decide to check my emails again while I'm up."
  
  
label lbl_end:
  scene bg desk night2
  rf "I wonder if Dave managed to get some sleep after all."
  
  $email_active = False
  call screen email_menu(True)
  $email_active = True
  
  rf "No new emails, i guess so then."
  
  #1am
  play music music_Horror
  call  lbl_Email_Dave_cant_sleep_start() from _call_lbl_Email_Dave_cant_sleep_start_1
  
  rf "Oh wait, i guess not."
  
  call  lbl_Email_Dave_Freaking_Out_start() from _call_lbl_Email_Dave_Freaking_Out_start_1
  call  lbl_Email_Dave_You_Awake_start() from _call_lbl_Email_Dave_You_Awake_start_1
  call  lbl_Email_Dave_Dude_start() from _call_lbl_Email_Dave_Dude_start_1
  
  "It looks like the emails are slowly trickling in as the server syncs up to my pc."
  
  call  lbl_Email_Dave_Seriously_start() from _call_lbl_Email_Dave_Seriously_start_1
  call  lbl_Email_Dave_Respond_start() from _call_lbl_Email_Dave_Respond_start_1
  call  lbl_Email_Dave_Sent_On_start() from _call_lbl_Email_Dave_Sent_On_start_1
  
  "My heart sinks as i read through the emails. Each new email sending a chill through me. The timestamps all from before midnight."
  
  call  lbl_Email_Dave_Didnt_Work_start() from _call_lbl_Email_Dave_Didnt_Work_start_1
  call  lbl_Email_Dave_Fuck_1_start() from _call_lbl_Email_Dave_Fuck_1_start_1
  call  lbl_Email_Dave_Fuck_2_start() from _call_lbl_Email_Dave_Fuck_2_start_1
  call  lbl_Email_Dave_Fuck_3_start() from _call_lbl_Email_Dave_Fuck_3_start_1
  call  lbl_Email_Dave_Fuck_4_start() from _call_lbl_Email_Dave_Fuck_4_start_1
  call  lbl_Email_Dave_Fuck_5_start() from _call_lbl_Email_Dave_Fuck_5_start_1
  call  lbl_Email_Dave_Fuck_6_start() from _call_lbl_Email_Dave_Fuck_6_start_1
  call  lbl_Email_Dave_Fuck_7_start() from _call_lbl_Email_Dave_Fuck_7_start_1
  call  lbl_Email_Dave_Fuck_8_start() from _call_lbl_Email_Dave_Fuck_8_start_1
  
  rf "I don't know what has happened, but Dave needs serious help."
  
  call  lbl_Email_Dave_Here_start() from _call_lbl_Email_Dave_Here_start_1
  $email_active = False
  call screen email_menu(True)
  $email_active = True
  
  rf "Wait, this one is timestamped just before midnight."
  
  "I wait a little longer to see if anymore emails pop up, but no more show up."
  "I can feel my own heart beating in my chest with every second that passes."
  
  play music music_Pulsing
  call  lbl_Email_Dave_Thanks_start() from _call_lbl_Email_Dave_Thanks_start_1
  $email_active = False
  call screen email_menu(True)
  $email_active = True
  
  rf "What the fuck. This has to be some elaborate prank. Dave is just fucking with me."
  
  "I grab my coat, my stomach is in my throat." 
  
  rf "I swear if hes fucking with me ill kill him myself."
  "I try to convince myself that its Dave's poor attempt at being funny."
  "But i have a sense of dread hanging over me. What if its true, what if it really was my fault?"
  
  "I need to know. I don't care if it's still raining as i grab my coat and leave the house."
  
  $email_active = False
  scene bg black with fade
  window hide
  play ambient sound_rain
  centered "{color=#ffffff}We will be laughing about this later.{/color}"
  centered "{color=#ffffff}I'm sure of it.{/color}"
  centered "{color=#ffffff}Classic Dave.{/color}"
  
  play sound sound_crow
  pause
  
  return
  
  "I'm running down the street towards the house Dave said he was staying in."

  "When suddenly my blood runs cold."
  
  #meet Olivia-Rose Murphy
  
  scene cg rainynight girl
  "I stop running and turn to see a girl with an umbrella, playing in the rain."
  "She is looking around as if shes seeing for the first time."
  "And there is something about her."
  "Something unsettling."
  "Maybe I'm just being paranoid because of Dave's Prank. I half heartedly try to convince myself."
  
  "..."
  
  "The girl doesn't ever look at me. But i can feel myself being watched."
  "I squint in the darkness, and make out a bird on her shoulder."
  play sound sound_crow
  
  scene bg black
  
  "Caught off guard by the crows sudden caw, I wince, closing my eyes."
  
  
  scene cg rainynight nogirl
  "When i open them again, both the girl and the bird are gone."
  
  rf "I have a really bad feeling about this."
  
  "I take off running again."
  
  scene bg black with fade
  pause
  
  return