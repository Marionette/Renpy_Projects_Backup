init:
  #event flags
  $Hecate_Arc_CurrentEvent = 0
  $Hecate_Arc_MetJo = False
#--------------- Hecate Events ----------------------
label lbl_event_tutoring_hecate:
  #"DEBUG: Hecate Relationship score: [Character_Hecate.Relationship]"
  #"You talk to Hecate."
  #call update_relationship(Character_Hecate, 5)

  Caragh "Okay. I'll be tutoring Hecate today."


  if Hecate_Arc_CurrentEvent == 0:
    #  Craig's Route : Tutoring Event 01
    call lbl_event_hecate_problem_tutoring_1 from _call_lbl_event_hecate_problem_tutoring_1
  elif Hecate_Arc_CurrentEvent == 2:
    call lbl_event_hecate_problem_tutoring_3 from _call_lbl_event_hecate_problem_tutoring_3
    Caragh "I don't think shes in the mood to study now, so I'll just head on home."

  elif Hecate_Arc_CurrentEvent == 3:
    call lbl_event_hecate_problem_tutoring_4 from _call_lbl_event_hecate_problem_tutoring_4

  elif Hecate_Arc_CurrentEvent == 5:
    call lbl_event_hecate_problem_tutoring_6 from _call_lbl_event_hecate_problem_tutoring_6

  else:
    if Hecate_Arc_CurrentEvent == 1:
    # "Hecate's Route: Talk to Jo (Lunch - Doesn't take up time)"
      if Jo_Arc_LearnedAboutJo:
        Caragh "Jo also works as a Therapist as well as a Librarian, maybe I should see if they can help with Hecate."
      else:
        Caragh "Maybe Bahini has some ideas?"
    if Hecate_Arc_CurrentEvent == 4:
    # "Hecate's Route: Talk to Father (Evening aka End of Time)"
      Caragh "Hecate said i could talk to her Parents, so I should try that soon."
    if Hecate_Arc_CurrentEvent == 6:
    # "Hecate's Route: Talk to Mother (Early Morning)"
      Caragh "Hecate father was a bust, so I'll have to try her mother. Apparently she works opposite hours to her husband so I will have to try in the morning."
    call lbl_event_hecate_problem_tutoring_0 from _call_lbl_event_hecate_problem_tutoring_0
      
  return


#------------------------------------------------------

label lbl_event_hecate_problem_tutoring_0:
  #Generic Tutoring Event when no others are available
  show bg classroom empty
  play music music_quiet
  show  Hecate
  Hecate "\"Hey, Miss Caragh!\""
  Caragh "\"Hecate, hello.\""
  #jump lbl_event_hecate_problem_tutoring_0_mid

label lbl_event_hecate_problem_tutoring_0_mid:
  #Tutoring starts here if taking place after another event
  Caragh "Today, we are going to focus on your weakest subject."
  $weakestSubject = Character_Hecate.GetWeakestSubject()
  Caragh "Which at the moment seems to be [weakestSubject]."
  Hecate "\"Yes, Miss Caragh.\""
  #jump lbl_event_hecate_problem_tutoring_0_mid2

label lbl_event_hecate_problem_tutoring_0_mid2:
  Description "We spend the time we have going over the fundamentals of [weakestSubject]."
  if Hecate_Arc_CurrentEvent == 8:
    call update_score_specific(Character_Hecate, weakestSubject, 10) from _call_update_score_specific_2
    Description "Hecate is really focused today and plows through the questions I had prepared."
    Caragh "Wow, you did really good today."
    show Hecate happy
    Hecate "Thanks!"
    Description "Hecate spends the remaining time practicing her magic on me before she has to leave."
    #jump lbl_event_problem_tutoring_end
  else:
    call update_score_specific(Character_Hecate, weakestSubject, 5) from _call_update_score_specific_3
    Description "Hecate seems to have picked up a few things during the tutoring session."
    #jump lbl_event_problem_tutoring_end
  call lbl_event_problem_tutoring_end from _call_lbl_event_problem_tutoring_end_3 #END SCENE
  return

label lbl_event_hecate_problem_tutoring_science:
  $weakestSubject = "Science"
  call lbl_event_hecate_problem_tutoring_0_mid2 from _call_lbl_event_hecate_problem_tutoring_0_mid2
  return
#------------------------------------------------------

label lbl_event_hecate_problem_tutoring_1:
  # "Hecate's Route: Tutoring Event 01"
  show bg classroom empty
  play music music_quiet
  show  Hecate
  Hecate "\"Hey, Miss Caragh!\""
  Caragh "\"Hecat-\""
  Description "Before I could finish my sentence, Hecate sits down on the chair and lounges back. Sparks begin forming at her fingertips while her eyes remained on me."
  Caragh "\"Ahem. According to your last teacher's notes, your weakest subject is Mathematics.\""
  Caragh "\"What seems to be the major problem?\""
  Hecate "\"Because Maths isn't important.\""
  Hecate "\"After all, who cares if the greatest witch of her time is bad at numbers?\""
  Hecate "\"It's not like Maths is required for magic.\""
  Caragh "\"Sadly, Maths is important for a kid still in monster school.\""
  Description "Hecate huffs."
  Caragh "She laughed but in the typical teenager \"here we go again\" fashion. What triggered it -\"kid\" or \"monster school\"?"
  Caragh "\"The world is tough on kids, Hecate.\""
  Caragh "\"What we teach in school may seem useless to you but it trains you in certain skills.\""
  Caragh "\"For example, Science may not be taught in the best way to tell you everything about the world and how it works but the way it's taught will teach you how to find out by yourself.\""
  Caragh "\"Maths may not directly help you in magic but it trains your brain on how to solve problems in magic.\""
  Hecate "\"If you say so, teacher.\""
  Caragh "She didn't laugh or scoff. "
  Caragh "\"Even if you don't believe me, we are here to work on your scores. Just for the few hours we have here, let's work on Maths. Okay?\""
  Hecate "\"Fine.\""
  Caragh "\"Great. To find out what you're having troubles with, I've prepared a test for you.\""
  Description "Hecate sulkily picks up a pen and begins working through the quiz. She's slow at first but halfway through the paper, she suddenly speeds up. Magic sparks twinkle around her pen as it flies across the papers. With every question answered, the sparks changed colours and formation."
  Caragh "Strange. I distinctly remember saving the hardest questions for the last. "
  Caragh "Is she the kind of student who's good at hard topics but bad at understanding the simple basics?"
  Description "On the last question, the sparks around Hecate burst into a display of colourful rainbows. She pushes the paper over to me before turning her focus to playing with the sparks hovering in her palms."
  Hecate "\"I'm done.\""
  Caragh "\"Thank you. Let me see...\""
  Caragh "Everything in the second half is wrong while everything in the first half is correct."
  Caragh "Did she give up on answering? Is that why she started playing with her magic?"
  Caragh "\"We have a lot to work on.\""
  Hecate "\"Fine.\""
  Caragh "She's really distracted. She didn't even look back up at me."
  Caragh "\"Hecate, your magic is wonderful. I admire your dedication. You truly are a great member of monster society.\""
  Description "Hecate pauses. Her eyes squint in suspicion as she stares into my eyes."
  Hecate "\"Really?\""
  Hecate "\"Am I truly a 'great member of {i}monster{/i} society'?\""
  Caragh "Aha, the trigger was \"monster\"."
  Caragh "\"Yes, you are. Otherwise, no one would call you the greatest witch of your age.\""
  Hecate "\"Thanks.\""
  Description "Hecate turns her head to look out of the window. It's hard to tell what she's thinking"
  Caragh "\"But, Hecate, could I ask something of you? It might be a hard task.\""
  Hecate "\"Of course! There's no task too hard for the Great Hecate!\""
  Caragh "\"Okay. Thank you. Could you put away your magic during our tutoring sessions?\""
  Hecate "\"It's practice. My parents say practice makes perfect.\""
  Caragh "\"Your parents did? And what did they think of your grades?\""
  Hecate "\"Grades are grades. There's no need to bother them with trivial nonsense.\""
  Caragh "\"I see. Still, no task is too hard for the Great Hecate, right?\""
  Hecate "\"...yes.\""
  Hecate "\"...\""
  Hecate "\"Okay.\""
  Caragh "\"Great. Thank you so much. I appreciate the effort you're putting into our tutoring sessions.\""
  Hecate "\"Yeah...\""
  Description "Minutes pass by as the two of us go through the quiz together. No sparks are seen but Hecate's focus soon drifts."
  Caragh "\"Hecate, focus! You'll fail if you don't.\""
  Description "Hecate distractedly hums but it's clear she's not focused."
  Caragh "\"Hecate, if you can get through the next five questions without blanking out, I'll let you experiment on me with your magic later.\""
  Hecate "\"It's a promise!\""
  Description "For the next two questions or so, Hecate tries to focus. However, her focus soon drifts and she blanks out once more."
  Description "The session soon ends. "
  Caragh "\"Thank you, Hecate, for holding back from practicing with your magic during our session.\""
  Caragh "\"Unfortunately, you blanked out two questions after our promise. No experiments on me today. Next time perhaps.\""
  Caragh "\"I'll let you know later when our next session is.\""
  Hecate "\"Yeah, okay.\""
  hide Hecate
  Description "Hecate walks out of the room. As her hat flops and flounces out of the room, magical sparks could be seen twinkling around the rim."
  Caragh "Well, victory? There was no magic but her mind wasn't completely there."
  Caragh "Is she bored or is she still thinking about magic? "
  $Hecate_Arc_CurrentEvent = 1
  call lbl_event_problem_tutoring_end from _call_lbl_event_problem_tutoring_end_4 #END SCENE
  return

label lbl_event_hecate_problem_tutoring_2:
  # "Hecate's Route: Talk to Jo (Lunch - Doesn't take up time)"
  #TODO: Rearrange this to fit into a Jo visit in the library
  show bg classroom empty
  play music music_quiet
       # flag for Jo encounter

  if Jo_Arc_LearnedAboutJo == True:
      Description "The classroom door slides open, revealing a mask floating in thin air."
      show  Jo
      Caragh "\"Thanks for meeting me, Jo. Bahini said you're also the therapist here?\""
  else:
      Caragh "I've messaged Jo, the librarian. Bahini said asking to meet over text messages is the best way to contact Jo. But Jo is apparently invisible. How do I know if they're here?"
      Description "The classroom door slides open, revealing a mask floating in thin air."
      show  Jo
      Caragh "\"Jo...?\""
      Description "The mask nods."
      Caragh "\"Thanks for meeting me during lunch, Jo.\""
      Caragh "\"I got your contact through Bahini. You're the therapist here, right?\""

  Description "The mask nods again, now smiling."
  Caragh "\"I'm worried about one of my students. Bahini said you might be able to help.\""
  Description "The mask tilts sideways."
  Caragh "Jo's saying nothing but I feel like I hear a \"do go on\" from the mask."
  Caragh "\"It's Hecate. I know, she's a great girl. The greatest witch of her age has surely nothing that she needs a therapist for, right? But I'm at a loss on how to handle her.\""
  Caragh "\"She focuses a lot on her magic. She experiments with it all the time. It's affecting her studies.\""
  Caragh "\"The year-end exams are coming up and she's going to fail if she doesn't focus on her studies.\""
  Caragh "\"I've asked her to stop during our tutoring sessions but she's still distracted.\""
  Description "The mask nods reassuringly as I continue to ramble about my worries for Hecate."
  Caragh "\"...um, so, yeah. That's why I was wondering if you could have a talk with Hecate?\""
  Description "The mask nods once more. Then, a note appears with a flourish out of thin air. "
  Caragh "\"Oh, thanks.\""
  Caragh "The note reads,"
  Caragh "\"Please let Hecate know that I'll be waiting for her here tomorrow during lunch. You should also tell her this is going to be a therapy session. It'll make it better for her. - Jo\""
  Caragh "\"Alright. Thanks, Jo.\""
  Description "The mask bobs up and down in another nod before leaving the room."
  hide Jo
  Caragh "That was...interesting. I'll talk to Hecate about this later."
  $Jo_Arc_LearnedAboutJo = True
  $Hecate_Arc_CurrentEvent = 2
  return

label lbl_event_hecate_problem_tutoring_3:
  # "Hecate's Route: Talk to Hecate about Therapy (Class - After/Doesn't take up time)"
  show bg classroom afternoon
  play music  music_5c
  play sound sfx_schoolbell
  Caragh "\"That's it for today, class.\""
  show bg classroom empty
  Caragh "\"Hecate, could I talk to you for a second?\""
  play music music_quiet
  show  Hecate
  Description "Hecate bounces up to me, sparks lighting up the air behind her."
  Hecate "\"Sure thing, teach'!\""
  Hecate "\"What is it?\""
  Caragh "\"Hecate, I've been observing you a lot during class and I'm worried about you.\""
  Caragh "\"I might be overthinking this but I feel like you could use a listening ear.\""
  Caragh "\"I know, I'm just a new teacher who hasn't known you for long. But I feel like you need some space to talk about how you're feeling. Therapy, to be more exact.\""
  Caragh "\"I've asked our school therapist, Jo, if they're available and they said they're okay to see you tomorrow during lunch.\""
  Caragh "\"The session will take place in an empty classroom. I won't be there. It'll just be you and Jo, the best listener anyone could ever ask for.\""
  Caragh "\"What do you think?\""
  Description "Hecate's sparks slowly fizz out with every word I spoke."
  Hecate "\"A therapist? I...\""
  Hecate "\"No.\""
  Caragh "\"There's nothing the Great Hecate can't do, right?\""
  Description "Hecate's scowl deepends."
  Hecate "\"Fine! Fine, I'll go to see some mind-shrink.\""
  Hecate "\"Where's the classroom?\""
  Hecate "\"Written on this paper? Okay, fine.\""
  Description "Hecate snatches away the note I was holding."
  Hecate "\"I see this. I'm going. Bye.\""
  Description "Hecate stomps out of the room. Her oversized hat squishes through the door frame as per usual but no sparks is seen."
  Caragh "That could have gone better. That could've gone so much better! I don't think the book was right on this point."
  Caragh "Why did I take this job in the first place? I'm not qualified to teach kids this young..."
  $Hecate_Arc_CurrentEvent = 3
  return #END SCENE  # Need to make sure this happens on a day where the player doesn't tutor Hecate after school. Maybe the event cancels the tutoring session?

label lbl_event_hecate_problem_tutoring_4:
  # "Hecate's Route: Permission to Talk to Parents (Tutoring Event 02)"
  show bg classroom empty
  play music music_quiet # Must happen at least 1 day after asking Hecate to see Jo
  show  Hecate
  Hecate "\"Hey, Miss Caragh!\""
  Description "Sparks twirl around Hecate as she skips into the room and takes her seat."
  Caragh "\"Hi. Someone's happy today.\""
  Hecate "\"Yup! Jo has been great help.\""
  Caragh "\"I'm glad. You were so upset at the notion that I was worried I'd overstepped.\""
  Hecate "\"I didn't know that's what therapy was about. My parents always made it seem so... They say that I'm...\""     # note to self to add to talk with Hecate's parents
  Caragh "\"It's okay to not talk about it. I'm just happy that you're happy.\""
  Hecate "\"No, no. Jo suggested I do this. I want to do this but I just...\""
  Description "The sparks fade away."
  Description "\"Teacher, do you mind talking to my parents?\""
  Caragh "\"Oh?\""
  Hecate "\"I...\""
  Hecate "\"Can you keep this a secret?\""
  Caragh "\"Of course.\""
  Hecate "\"I don't like the word 'monster'. I never have. It just reminds me of how I'll never fit in.\""
  Hecate "\"Sure, I'm a witch which makes me part of monster society.\""
  Hecate "\"But if witches are monsters, why do some people still look down on us for being too much like humans? Aren't there a lot of monsters who look like humans too?\""
  Hecate "\" Why are witches the only ones bullied for it? Aren't all monsters meant to be equal, even if they look weird and different?\""
  Hecate "\"Why do witches have to work so much harder than everyone else just to be acknowledged?\""
  Hecate "\"Why can other people do the least they can and still be 'a pride to monster society' while witches need to be the best at magic to stand a chance at being called that?\""
  Hecate "\"I just...\""
  Hecate "\"I want to ask the other kids that but I don't know how and I know they'll just laugh at me. I'm sure they already laugh at me and mock me because I'm really not that powerful anyway and I can't...\""
  Hecate "\"I don't know how to...\""
  Hecate "\"So, yeah. Miss Caragh, if you could talk to my parents and tell them...\""
  Description "A tear rolls down Hecate's cheek."
  Hecate "\"I don't know. Just talk to them?\""
  Caragh "\"I'll do my best. Hecate, how much of this conversation are you okay with me sharing to your parents?\""
  Hecate "\"Anything. Everything. I...\""
  Description "By now, tears are streaming down her face. I wrap my arms around Hecate."     # This scene would make a great CG (if i had more time)
  Caragh "\"It's alright. I'll talk to them. I'll tell them just how brave you are and all the wonderful things you've done. I'll make them understand that you are the best daughter they could ever have and you need them. Okay?\""
  Hecate "\"I don't need them. I just... I wish being good at magic is enough for them to look at me. I wish... I want a hug from them. That's all.\""
  Caragh "\"I see.\""
  Caragh "\"You've had a tough time so far. It's okay to want a hug.\""
  Description "The room falls silent as Hecate buries herself in my embrace."
  Description "Minutes later, the young witch pulls back."
  Hecate "\"Today, can we work on Science instead?\""
  Caragh "\"Of course.\""
  call lbl_event_hecate_problem_tutoring_science from _call_lbl_event_hecate_problem_tutoring_science
  $Hecate_Arc_CurrentEvent = 4
  return #END SCENE

label lbl_event_hecate_problem_tutoring_5:
  # "Hecate's Route: Talk to Father (Evening aka End of Time)"
  show bg room
  play music music_bedroom
  Caragh "Bahini said Hecate's parents are nocturnal and Hecate said they're usually up by now. "
  Caragh "Should I give it a few more minutes to call or should I do it now? If I wait too long, Hecate might be in bed by the time we're done."
  Caragh "I don't want that to happen. It'll be better for Hecate if she has the night to process her feelings."
  Caragh "Alright. Now. "
  show Phone    
  play sound sfx_phonecall
  HecateFather "\"Hello? Who's this?\""
  Caragh "\"Hi, are you Hecate's father? This is Caragh, your daughter's new teacher.\""
  HecateFather "\"Oh. What do you want?\""
  Caragh "\"Are you free to talk right now?\""
  HecateFather "\"This is about, um, Hecate. Yes? Yeah, go ahead.\""
  Caragh "\"Thank you.\""
  Caragh "\"Pardon me for asking this, but how do you think your daughter has been doing? Particularly during this year.\""
  HecateFather "\"Well, we know she's doing very well in her magic. She did have some problems manifesting a full rainbow projection a few months ago.\""
  HecateFather "\"Don't know what happened there. She's always been a bright kid.\""
  HecateFather "\"Still, we're so proud of the progress she's made. No witch has ever been able to summon sparks at her age, let alone manipulate the colors.\""
  HecateFather "\"And she has such fine control with them! She can make double rainbows with her sparks! How amazing is that?\""
  Caragh "\"Yes, that is amazing...\""
  Caragh "Well, I see why Hecate feels so strongly about having me talk to her parents instead of telling them herself. All he's talked about is her magic. Nothing about her personally or her grades."
  Caragh "\"Hecate might be the most powerful witch of her age but her grades have been slipping.\""
  HecateFather "\"Pssh. Who cares about grades? Do you think my wife and I got to where we are now because of grades? No. Being the best witches in the land gave us this life of luxury.\""
  HecateFather "\"If not for us, do you think a mere witch would be able to enroll in an Echidna's school? No way!\""
  Caragh "\"Oh?\""
  HecateFather "\"Monster society is a tough one and we witches need to prove ourselves to be better than all monsters.\""
  HecateFather "\"Otherwise, we'd be backstabbed, beaten, killed and robbed in broad daylight! No monster trusts a witch and a witch shouldn't either!\""
  Caragh "\"Now, sir, that's not...\""
  HecateFather "\"Bah, you're a monster. What do you know?\""
  HecateFather "\"Anyway, don't get between my daughter and her magic. Got it?\""
  HecateFather "\"That's all she has, all she will ever have and all she will ever need!\""
  HecateFather "\"If you put any ideas in her head, you will dearly regret it!\""
  play sound sfx_phonecallend
  hide Phone    
  Caragh "I don't think Hecate's parents are going to be of much help."
  Caragh "His beliefs are too deep-rooted for me to do anything in less than a month. It'll take time to change his views. Meanwhile, Hecate needs my help. In fact, she needs more than my help."
  Caragh "I have Jo helping out but Hecate needs more than therapy."
  Caragh "Hecate needs other social ties that'll ease her anxieties, peers who can help her with her insecurity and talk her out of this internalized hate."
  Caragh "But who?"
  $Hecate_Arc_CurrentEvent = 5
  return #END SCENE

label lbl_event_hecate_problem_tutoring_6:
  # "Hecate's Route: After Calling Father (Tutoring Event 03)"
  show bg classroom empty
  play music music_quiet
  show  Hecate
  Description "Hecate walks in, sparks trailing in her wake. "
  Caragh "\"You seem to be in a good mood today, Hecate.\""
  Hecate "\"I was able to project a double rainbow the other day without using my sparks!\""
  Hecate "\"My father was so happy that he decided to cancel magic lessons that evening. We just sat around at home, playing with rainbow projections.\""
  Caragh "\"You have additional magic lessons after you go home?\""
  Caragh "Playing around with your magic also doesn't sound like a relaxing break away from magic lessons. In fact, it sounds like a magic lesson."
  Hecate "\"Yeah!\""
  Hecate "\"It's...the only time I ever have with my father.\""
  Hecate "\"He's always so busy. I rarely get to see him, not like my mother.\""
  Caragh "This is going into a direction I don't think we should be exploring this close to the year-end exams. It's definitely not one that should be explored with me. After all, what do I know of kids and parenting?"
  Caragh "But then again, the mother..."
  Caragh "\"What do you mean by 'not like your mother'?\""
  Hecate "\"My parents don't wake up at the same time. Father wakes up before dinner and goes to bed before I even wake up at 6. Mother wakes up at midnight and only goes to bed after lunch.\""
  Caragh "\"I see...\""
  Caragh "Maybe talking to the mother would help? It's very unlikely but I should give her the benefit of the doubt."
  Caragh "\"Well, you must cherish your lesson with your father then.\""
  Hecate "\"I do!\""
  Caragh "\"In that case, why don't you go through this quiz? It's a little test to see how much you've improved. The faster you get it done, the faster you can go home to your father.\""
  Hecate "\"Got it!\""
  Caragh "Okay. While she's going through the quiz, I can think on my next move."
  Caragh "I really don't like what Hecate said just now but what can I do? It's her family. Maybe things will develop to the point where she can get what she needs without going through all this hardship."
  Caragh "Jo seems to have helped her a lot over the past few days. Hopefully, their sessions can continue and Jo will have an idea how to help afterwards."
  Caragh "Maybe it'd be good for her to get to know her classmates better. There is the cram session. I can put the students into groups."
  Caragh "It will be good for her to be grouped up with someone {b}friendly and soft{/b} or maybe someone who's {b}so blunt and honest that Hecate won't feel the need to wonder what they truly think{/b}."

  #-----------------
  #Choice "Choose 2 characters from the list of students."      
  #call lbl_event_func_group_picker from _call_lbl_event_func_group_picker_1
  call screen group_planning("Hecate")
  #$Hecate_Cram_Partner_01 = _return[0]
  #$Hecate_Cram_Partner_02 = _return[1]
  
  $Hecate_Cram_Partner_Correct = False
  if Hecate_Cram_Partner_01 in ["Rudolph", "Fayette"] and Hecate_Cram_Partner_02 in ["Rudolph", "Fayette"]:
      $Hecate_Cram_Partner_Correct = True
  #-----------------   

  Hecate "\"I'm done, teach'!\""
  Caragh "\"Whoa, that's fast! Let me see...\""
  Caragh "\"Nice work, Hecate! You've improved on all fronts since our first lesson.\""
  Description "A grin spreads across Hecate's face as sparks begin twirling around her hat."
  Caragh "\"I think we're almost done here. After one last session to go through the topics you're having trouble with, you'll have caught up with everyone and you won't need additional tutoring anymore.\""
  Hecate "\"Really?\""
  Caragh "\"Yes. Now, as promised, you may go.\""
  Hecate "\"Thank you, Miss Caragh!\""
  Description "Hecate immediately hops to her feet, gathers her belongings and runs out the door without another look backwards."
  hide Hecate
  Caragh "Now, time to call the mother. Hecate's father goes to sleep before she wakes up at 6 and I can't call the house after 6 because Hecate needs to get ready for school then."
  Caragh "I guess I'll call them right after the witching hour."
  $Hecate_Arc_CurrentEvent = 6
  call lbl_event_problem_tutoring_end from _call_lbl_event_problem_tutoring_end_5 #END SCENE
  return

label lbl_event_hecate_problem_tutoring_7:
  # "Hecate's Route: Talk to Mother (Early Morning)"
  show bg room
  play music music_bedroom
  show  Caragh
  Caragh "Ugh... It's only 5. Why did I set an alarm..."
  Caragh "Oh, right. Hecate's mother."
  Caragh "Get up, Caragh. You signed up for this when you decided to teach. You knew teaching wouldn't be easy..."
  Caragh "Ah, who am I kidding? I became a teacher because that's what I'm good at. All these pep talks do nothing for me."
  Caragh "..."
  Caragh "Right. Time to call Hecate's mother. I hope she answers the phone."
  #hide Caragh
  show Phone
  play sound sfx_phonecall
  HecateMother "\"Hello, who is it?\""
  HecateMother "\"If you're looking for my husband, he has just fallen asleep.\""
  Caragh "\"Hi, this is Caragh Dullahan. I'm Hecate's teacher. I was wondering if I could speak to you?\""
  HecateMother "\"Oh, what is it? Has something bad happened to my daughter?\""
  HecateMother "\"Are her grades that bad? Is she expelled? Did she get into a fight? What do we need to do? Also, why are you calling in the middle of the night? Don't you teachers usually email us instead?\""
  Caragh "\"No, nothing bad has happened to your daughter and Hecate's grades have been improving.\""
  HecateMother "\"Thank goodness. So, what is it? Wait, why are you her teacher? Wasn't it Mog or Bahini?\""
  HecateMother "\" Did Bahini get into an accident? I knew it. My crystal balls would never lie to me. That and the years I've spent listening in on gossip sessions.\""
  Caragh "How am I meant to answer her questions if she doesn't give me time to? She knows more about her daughter's school life than the father does. That's for sure."
  Caragh "While I don't like the thought of her eavesdropping on the teachers, it's not illegal."
  Caragh "\"Unfortunately, yes. Bahini has been hospitalized due to an accident. As for Hecate...\""
  HecateMother "\"I sense hesitation.\""
  HecateMother "\"This is serious, isn't it?\""
  Caragh "Her tone changes fast! "
  Caragh "\"Yes.\""
  Caragh "\"How much do you know of your daughter's fears?\""
  HecateMother "\"Fears? Hecate doesn't have fears. She hasn't had any since she was two. She had her first magic lesson then. My husband was so proud when Hecate set the bed on fire.\""
  Caragh "\"I see...\""
  Caragh "How can a kid not have any fears? Even without what Hecate told me, I would never have thought she's completely fearless. She wears a large hat and her first words were an offer to set the place on fire!"
  Caragh "\"Well, I've heard a few things from Hecate that I wouldn't normally expect to come from a kid. There was something about the word 'monster'.\""
  HecateMother "\"Oh, I know that one. She doesn't like it. It's a family rule: the word 'monster' is evil and forbidden.\""
  Caragh "\"Oh...\""
  Caragh "\"Hecate also mentioned something about how she wants to talk to her classmates about certain subjects but she's afraid they'd laugh at her.\""
  HecateMother "\"Oh, what's the problem with a little social anxiety? It's fine. She'll turn out fine.\""
  Caragh "This really isn't working. I don't think this chat is going anywhere."
  HecateMother "\"But okay, I'll keep a closer eye on her. I'll talk to her more often, ask after her and all that jazz.\""
  Caragh "\"Thank you, ma'am. While Hecate is one of the best in magic and her grades aren't bad, it's best for her to be mentally healthy.\""
  HecateMother "\"Mental health? What kind of crazy talk is that? Oh, whatever.\""
  HecateMother "\"Hecate's fine outside of whatever weird social thing you're worried about, right?\""
  HecateMother "\"Thanks for letting me know. I'll do the thing and what-not. Okay, bye.\""
  play sound sfx_phonecallend
  hide Phone    
  Caragh "That was a horrible talk. The mother is better than the father, but not by much."
  Caragh "Oh, I give up on thinking about this. It's too early. "
  Caragh "I'll think about it after my nap."
  $Hecate_Arc_CurrentEvent = 7
  return #END SCENE

label lbl_event_hecate_problem_tutoring_8:
  # "Hecate's Route: After Calling Mother (Lunch/ Doesn't take up time)"
  show bg hallway
  play music music_good_vibes
  Description "I'm passing by the library on my way to the cafeteria when I hear Hecate's excited voice."
  show cg hecate_chat
  Hecate "\"...and then she told me it's okay to be afraid and fail sometimes. Then, she gave me a hug! And she woke my father up and he gave me a hug too!\""
  Hecate "\"I'm just so happy! I don't know. Is this normal? Jo, what is normal?\""
  Caragh "I'm glad the calls worked. There's still more work to do so that Hecate can grow up as a happy witch and free from the fears that usually terrorize her."
  # Trigger flag for boost to Hecate
  Caragh "But, at least for now, she should be in a good enough place to concentrate in class."
  $Hecate_Arc_CurrentEvent = 8
  return #END SCENE  # The last step is in cram session
  #" END OF HECATE'S ROUTE "
