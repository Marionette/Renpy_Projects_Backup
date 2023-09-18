init:
    #Random Event Flags
    default Random_Oversleep = False
    default Random_Lunch_Forget = False
    default Random_Lunch_Teacher = False
    default Random_Lunch_Craig = False
    default Random_Lunch_Hecate = False
    default Random_Lunch_Sanura = False
    default Random_Lunch_Student = False
    default Random_Lunch_Share_Student = False
    default Random_Lunch_Share_Teacher = False
    default Random_Lost = False
    default Random_AAA = False
    default Random_Athan = False
    default Random_Bestia = False
    default Random_Craig = False
    default Random_Dougal = False
    default Random_Dougal_Scold = False
    default Random_Dougal_Join = False
    default Random_Fayette = False
    default Random_Florence = False
    default Random_Hecate = False
    default Random_Juniper = False
    default Random_Lateef = False
    default Random_McCoy = False
    default Random_Roark = False
    default Random_Sanura = False
    default Random_Sophia = False
    default Random_Xisreia = False
    default Random_Una = False



    #random event lists
    $List_events_random_morning = ["lbl_event_random_morning_sleep_1",
                                  "lbl_event_random_morning_sleep_2",
                                  "lbl_event_random_morning_traffic_1",
                                  "lbl_event_random_morning_traffic_2",]
    $List_events_random_lunch = ["lbl_event_random_lunch_youforgot_1",
                                "lbl_event_random_lunch_youforgot_2",
                                "lbl_event_random_lunch_youforgot_3",
                                "lbl_event_random_lunch_theyforgot_1",
                                "lbl_event_random_lunch_theyforgot_2"]
    $List_events_random_evening = ["lbl_event_random_evening_eatingout_1",
                                "lbl_event_random_evening_eatingin_1",
                                "lbl_event_random_evening_eatingin_2"]

    #Class events can happen Before, During, After, Instead
    $List_events_random_class = [["lbl_event_random_class_any_dougal", "Before"],
                             ["lbl_event_random_class_any_lateef", "Before"],
                             ["lbl_event_random_class_any_lostsupplies", "Instead"],
                             ["lbl_event_random_class_una", "After"],
                             ["lbl_event_random_class_any_lateef", "Before"],
                             ["lbl_event_random_class_any_athan", "During"],
                             ["lbl_event_random_class_any_bestia", "During"],
                             ["lbl_event_random_class_any_craig", "During"],
                             ["lbl_event_random_class_any_florence", "During"],
                             ["lbl_event_random_class_any_hecate", "During"],
                             ["lbl_event_random_class_any_juniper", "During"],
                             ["lbl_event_random_class_any_mccoy", "After"],
                             ["lbl_event_random_class_any_sophia", "During"],
                             ["lbl_event_random_class_any_xisreia", "During"]]
    #Specific Class Events
    $List_events_random_art = [["lbl_event_random_class_art_cerberus", "During"],
                              ["lbl_event_random_class_art_roark", "During"]]

    $List_events_random_pe = [["lbl_event_random_class_pe_fayette", "During"]]

    $List_events_random_math = [["lbl_event_random_class_math_sanura", "During"]]
####################### SKITS ########################################

#--------------- General/Class ----------------------
label lbl_event_random_class_any_lostsupplies:
    show bg hallway with dissolve
    play music music_school
    Caragh "Good job, Caragh. Thanks for saying you'll help look for art supplies when you're still new to the school."
    Caragh "Thanks for being so smart as to charge ahead without bringing a map. Thanks for getting us lost!"
    Caragh "Look at us now. Late, late, late and late! We won't even have time to teach anything now!"
    Description "I wander around for a bit before one of the other teachers spots me. After a brief exchange of words, they put me back on the right path."
    Caragh "Thank goodness for faculty."
    Description "Finally, I arrive at the art room. I grab what I need and deliver them to where they need to be before heading back to 5C."
    show bg classroom morning
    play music music_5c
    Caragh "\"My apologies for being la-\""
    Description "Before I could finish my sentence, an eraser soars past above my neck. Mayhem has taken over the class. The kids are chaos incarnate."
    Caragh "\"Alright, class! I'm here!\""
    Description "Finally, the kids notice my presence. They immediately scramble back to their seats, tidying up as they go. In a few minutes, the room went from hell to the cleanest classroom in the school."
    Description "I open my mouth, intent on lecturing them for their behavior, when I hear giggles. I take a good look of the class. The kids are all smiling, pure joy shimmering in their eyes. "
    Caragh "Oh, I'll just let it go this one time. They cleaned up after themselves at least."
    Description "The kids miss out on a lesson but they're in a much better mood now."
    call update_mood_all(5) from _call_update_mood_all_9
    $ Random_Lost = True
    #clear the list      
    $List_Random_Event_Messages += ["It's not my first day in the school and yet I could get lost searching for art supplies. It's a little ridiculous and kind of stressful. In hindsight, I also had some fun."] 
    if current_time == "Morning":
      $RecordClassOutcome(morning_class, "Got Lost")
    else:
      $RecordClassOutcome(afternoon_class, "Got Lost")
    return


#--------------- Student ----------------------
label lbl_event_random_class_any_dougal:
  if not Random_Dougal:
    #Dougal Event
    Description "As I walk into the classroom, I find the students crowded around Dougal the Jack-o'-Lantern. The boy has taken his head off."
    Dougal "\"My name is {i}Caragh{/i} Dullahan. As you can tell, I am a {i}Dullahan{/i}. You may call me {i}Miss{/i} Caragh.\""
    Caragh "Strange emphasis aside..."
    $List_Random_Event_Messages += ["I walked into class one day to find Dougal holding his head like how I hold mine. I was so conflicted. I didn't know if I should've scolded him for it or join in the fun."]
    $ Random_Dougal = True
    menu:
        "How should I respond?"
        "Lecture":
            Caragh "\"Dougal.\""
            Dougal "\"Eep! Miss Caragh. Haha... Fancy seeing you here...?\""
            Description "I give Dougal the biggest, most universally hated punishment I could ever think of for a student - double the homework."
            $ Random_Dougal_Scold = True
            $List_Random_Event_Messages += ["In the end, I had to establish my authority as the teacher."]
        "Join in":
            Description "I put my head on my neck, keeping my hands around it to make sure I it didn't fall off."
            Caragh "\"And I am Dougal, the funniest Jack-o'-Lantern alive in Echidna's School for Little Monsters!\""
            Description "The kids let out an audible gasp as they turn to look at me. There's a moment of silence before Dougal jumps back into character. Soon, the classroom is filled with cheers and laughter."
            $ Random_Dougal_Join = True
            $List_Random_Event_Messages += ["In the end, I played along. What harm can a little fun do?"]
  return

label lbl_event_random_class_any_lateef:
  if not Random_Lateef:
    #Lateef event
    Lateef "\"Miss Caragh, what do you think of my new outfit?\""
    Description "I turn around to be greeted by the most bedazzling outfit I have ever seen, to put it kindly. Upon noticing my gaze on him, Lateef the Mummy twirls to show off his new outfit."
    Caragh "\"It looks...amazing.\""
    Lateef "\"Oh, you flatter me, Miss Caragh. I just knew this outfit would win you over.\""
    Description "Lateef then skips to his desk, leaving watery eyes in his wake."
    $ Random_Lateef = True
    $List_Random_Event_Messages += ["Do you remember Lateef, the kid who loves fashion? One day, he came in an outfit that was so over the top that I felt extremely underdressed in comparison."]
  return

label lbl_event_random_class_art_cerberus:
  if not Random_AAA:
    Achilles "\"Flower!\""
    Adonis "\"Fire!\""
    Atlas "\"No! Ball!\""
    Caragh "The three of them have been arguing for a while now. Is it that hard to just draw all three objects?"
    Description "Suddenly, paint starts flying everywhere. The Cerberus heads must've decided arguing wasn't good enough. They had to settle on what to draw via a paint fight."
    Caragh "\"Achilles! Adonis! Atlas!\""
    Description "The kids froze. One of their hands is holding a paintbrush up to Achilles' sheepish face while the other laid its rainbow fingers on Adonis' cheek."
    Caragh "I do not look forward to cleaning the room after this."
    $ Random_AAA = True
    $List_Random_Event_Messages += ["Do you remember the Cerberus kids, Achilles, Adonis and Atlas? They were fighing in Art over what to paint. The mess could've been worse."]
  return

label lbl_event_random_class_any_athan:
  if not Random_Athan:
    Rudolph "\"Miss Caragh!\""
    Description "In the middle of class, Rudolph the Yeti shrieks. I look over to see the boy holding up a bleeding finger."
    Caragh "Oh no."
    Description "As I expected, I soon hear a thump as Athan the Vampire faints."
    Caragh "Oh dear. Now, where's my first aid kit?"
    $ Random_Athan = True
    $List_Random_Event_Messages += ["A kid cut their finger in class and Athan, the vampire kid, passed out."]
  return

label lbl_event_random_class_any_bestia:
  if not Random_Bestia:
    Caragh "Why do I hear snoring...?"
    Description "I turn to scan the room. Soon, I find the culprit. It's Bestia. I walk over to her desk and tap her on the shoulders."
    Caragh "\"Bestia, wake up!\""
    Description "The Werewolf jerk up. Her bleary eyes look at me."
    Bestia "\"Ah, Miss Caragh. I'm sorry. I didn't get any sleep last night. There was a new season of my show, {i}The Intergalactic{/i}...\""
    Caragh "And she's asleep again. Oh well, I'd rather she sleep now so she can study later instead of staying awake and learning nothing. I'll give her some extra materials to revise then."
    $ Random_Bestia = True
    $List_Random_Event_Messages += ["You know that werewolf kid who's afraid of the dark? She fell asleep in class. Apparently, she stayed up all night watching sci-fi shows."]
  return

label lbl_event_random_class_any_craig:
  if not Random_Craig:
    Caragh "\"Now, who would like to answer this question?\""
    Description "Out of the corner of my eye, I spot Craig passing a note to Roark, the Gargoyle kid sitting next to him. A second later, a soft giggle could be heard coming from Roark."
    Caragh "\"Craig, could you come up and write the answer on the board?\""
    Description "Craig stiffly turns to look in my direction. His tail drags across the floor as he shuffles over. It takes him a few long moments but he finally writes down his answer."
    Caragh "\"Good job, Craig. That is correct. Thank you for listening to my lessons.\""
    Description "Craig heaves a sigh of relief. For the rest of the class, Craig's focus is stuck to the lesson."
    Description "As for Roark, he's doing his best impression of the best Gargoyle in history by staying as still as a statue. It's clear the implicit reprimand is noted."
    $ Random_Craig = True
    $List_Random_Event_Messages += ["You won't believe what happened. I saw Craig passing notes to Roark. Craig is so shy that I thought it was impossible!"]
  return

label lbl_event_random_class_pe_fayette:
  if not Random_Fayette:
    Description "In the middle of telling the class what we'll be doing in PE today, Fayette flies up to my face."
    Fayette "\"Miss Caragh, I want to do it too!\""
    Caragh "\"Pardon?\""
    Fayette "\"I want to do whatever the other kids are doing! I don't want to be left out anymore! Anything they can do, I can do better!\""
    Caragh "\"But, Fayette, we're going to be-\""
    Fayette "\"I don't care! I'm a monster! I want equal t-treatme-ment!\""
    Caragh "I'd believe that if you didn't stutter and mispronounce the word \"treatment\"."
    Caragh "\"Okay, okay. If that's what you want...\""
    Description "For the rest of PE class, I give Fayette the same assignments as everyone else. If the kids are to run three laps, so too does Fayette."
    Description "By the end of class, Fayette is sprawled out on the ground."
    Caragh "\"Are you okay, Fayette?\""
    Fayette "\"No more, Miss Caragh! I don't want to do this anymore!\""
    Caragh "Thank goodness, she didn't hurt herself."
    Caragh "Today's class has been nerve-wrecking. I hope whoever taught Fayette the phrase \"equal treatment\" teaches her what it truly means."
    $ Random_Fayette = True
    $List_Random_Event_Messages += ["During PE, Fayette demanded to be treated as an equal even though we physically can't do that. She soon regretted it."]
  return

label lbl_event_random_class_any_florence:
  if not Random_Florence:
    Caragh "\"Kids, please hand in your homework before flipping to page 74 on your textbook.\""
    Description "The sound of rustling paper soon fills the room. Every kid in the room is handing in their homework, every kid except Florence the Zombie. She's looking down at her desk with an upset face. I walk over to her desk."
    Caragh "\"Florence, is something wrong?\""
    Description "Florence looks up at me before looking back down."
    Florence "\"I'm sorry, Miss. I forgot to do my homework...\""
    Caragh "\"It's okay, Florence. Thank you for being honest.\""
    Description "Florence nods, eyes still staring at her desk."
    Caragh "\"Now, do you think you can finish it and today's homework, and then hand it in to me tomorrow morning?\""
    Description "Florence's head snaps up to look at me, a hopeful look in her eyes."
    Florence "\"Really, Miss? Thank you! I'll have it done tomorrow!\""
    Caragh "Did she expect me to punish her or something? We have less than a month until the exams are here. Homework isn't as important as her catching up on everything else."
    $ Random_Florence = True
    $List_Random_Event_Messages += ["Well, Florence forgot to do her homework. In all honesty, I'm just glad she didn't tell me her dog ate her homework."]
  return

label lbl_event_random_class_any_hecate:
  if not Random_Hecate:
    Caragh "\"According to-\""
    Description "Boom!"
    Description "Halfway through the lesson, I'm interrupted by a bright flash of light and a loud bang."
    Hecate "\"Pssh. That's nothing!\""
    Description "Bang! Boom! Pop!"
    Description "This time, it's a series of blinding and colourful lights right in my face. My vision goes black while a loud buzz echoes in my head."
    Xisreia "\"That's what you call a spell? Come on, Hecate. This is better.\""
    Description "When the black spots fade away from view, I'm greeted again by another series of flashing lights accompanied by music that screeches more than it sings."
    Caragh "\"Hecate! Xisreia! Stop it and sit down!\""
    Description "By sheer luck, my guess is right and I'm able to establish order once more in the classroom. However, my head is still spinning by the end of the class."
    $ Random_Hecate = True
    $List_Random_Event_Messages += ["Things were a little explosive in class this week. Hecate was comparing her spells with Xisreia's. I won't say more than that. You should be happy I'm not in the bed next to you."]
  return

label lbl_event_random_class_any_juniper:
  if not Random_Juniper:
    Description "The kids are working on some questions when I hear someone snoring. In fact, the snoring came from someone who's definitely serpentile. I look around. There she is, Juniper."
    Description "The Lamia is always falling asleep in class. We're not sure what the problem is but her parents have been trying all sorts of treatments."
    Caragh "I'll take this time to make a copy of my lesson notes for her."
    $ Random_Juniper = True
    $List_Random_Event_Messages += ["Juniper fell asleep in class. Again. I know it's normal but I wish there was something we can do about her problem."]
  return

label lbl_event_random_class_any_mccoy:
  if not Random_McCoy:
    Description "As I'm wrapping up class, McCoy the Skeleton stands up, making everyone pause and look at them."
    McCoy "\"What do you get when you combine a rhetorical question and a joke?\""
    Description "..."
    Description "For a few long, awkward moments, everyone stares in silence."
    Caragh "\"What do you get, McCoy?\""
    McCoy "\"That's it.\""
    McCoy "\"Great jokes don't need punchlines.\""
    Caragh "\"I see...\""
    Caragh "I think that's a joke better written than told."
    $ Random_McCoy = True
    $List_Random_Event_Messages += ["McCoy tried to tell some jokes. No surprise, I don't think anyone really understood them."]
  return

label lbl_event_random_class_art_roark:
  if not Random_Roark:
    Roark "\"Hnnng...\""
    Description "Roark the Gargoyle is glaring hard down at their paper. Their nostrils flare and puff out tiny flames."
    Caragh "\"What's wrong, Roark?\""
    Roark "\"I'm thinking.\""
    Caragh "Um...Okay."
    Caragh "\"About what?\""
    Roark "\"How to draw my self portrait. I can't really see myself. I have a short neck.\""
    Caragh "True..."
    Caragh "\"How about we find a mirror for you to use? That might help.\""
    Description "I put my head on the desk and dig around in my bag before pulling out a compact mirror. When I open it for Roark to see, they gasp in joy."
    Caragh "\"Try this. I'll hold it while you draw.\""
    Description "Roark looks a bit unsure but they take up their pencil and start drawing."
    Description "Eventually, they stop and hold up their paper for me to see."
    Caragh "Where's the rest of them? They only drew their face! Oh well, I guess that's better than nothing."
    Caragh "\"Whoa, nice job!\""
    Roark "\"You really think so?\""
    Caragh "\"Of course! You could be a professional.\""
    Description "Pleased at the praise they received, Roark gives a toothy grin while they sheepishly rub the back of their head."
    Roark "\"Thank you! Thank you very much! Hold on a second. Let me draw you, Miss Caragh!\""
    Description "Roark starts drawing on a fresh sheet of paper. I can only imagine how it'll turn out since I'm not holding my head."
    $ Random_Roark = True
    $List_Random_Event_Messages += ["We were doing self-portraits in Art and Roark had a few...problems with the assignment."]
  return

label lbl_event_random_class_math_sanura:
  if not Random_Sanura:
    Caragh "\"Now, who can answer this question for me?\""
    Sanura "\"Oh, I know! The answer is 37.\""
    Caragh "\"Good job, Sanura. Now, for the next question...\""
    Sanura "\"It's 24!\""
    Caragh "\"Thank you, Sanura. And now this next question...\""
    Sanura "\"It's 62!\""
    Caragh "\"Yes, Sanura. Thank you. You've answered all three questions. I think you can take a break from answering.\""
    Caragh "\"Class, can anyone answer this next question?\""
    Sanura "\"42!\""
    Caragh "It's going to be one of those days, isn't it?"
    Description "The rest of the class passes by in bliss for the kids as Sanura answers all of the questions posed, despite my numerous attempts to get her to stop."
    $ Random_Sanura = True
    $List_Random_Event_Messages += ["During one of our Maths classes, Sanura answered all of the maths questions. She didn't get any wrong at all!"]
  return

label lbl_event_random_class_any_sophia:
  if not Random_Sophia:
    Caragh "What's that?"
    Description "In the middle of teaching, I see something flickering out of the corner of my eye. I look up and around but find nothing."
    Description "As I look back down at my notes, my senses tell me something is flickering again. Once more, I look up and find nothing. This cycle repeated over and over again."
    Caragh "There's nothing there but an empty desk and some pens. No one's saying anything or doing anything. Just what could it be?"
    Description "Just then, a pen rolls off the unoccupied desk."
    Caragh "Huh, strange. Maybe it's just the wind..."
    Caragh "Wait."
    Caragh "\"Sophia?\""
    Description "As soon as I call out, a strong wind blows from the empty desk to me then out the door. I look down to find a note left on my desk."
    Description "\"Miss Caragh, I really need to go pee. Sorry. - Sophia (Ghost_)\""
    Caragh "Heh. I should've known."
    $ Random_Sophia = True
    $List_Random_Event_Messages += ["You know the ghost kid? I...I have some issues noticing when she wants my attention."]
  return

label lbl_event_random_class_any_xisreia:
  if not Random_Xisreia:
    Description "During one of our brief breaks from the lesson, I have everyone share something about them that they like."
    Xisreia "\"I can speak any language that has ever existed!\""
    Bestia "\"Oh, yeah? Prove it!\""
    Description "Xisreia the Demon begins speaking in a lilting language. Then, she switches to another language that sounds like gravels grinding against each other in the most ear-piercing manner possible."
    Xisreia "\"Ta-da!\""
    Bestia "\"I bet you can't speak Loringsorit!\""
    Xisreia "\"Loringsorit? What's that?\""
    Caragh "Isn't Loringsorit from that sci-fi show Bestia's obsessed about? Xisreia has been sleeping for the past 5000 years. Bestia, come on."
    Bestia "\"Hah! So you can't do it!\""
    Xisreia "\"Can too!\""
    Bestia "\"No, you can't!\""
    Caragh "I'd better stop this before a fight breaks out."
    Caragh "\"Okay, class. Let's get back to our lesson!\""
    $ Random_Xisreia = True
    $List_Random_Event_Messages += ["I had a battle of languages this week. Xisreia was showing off how many archaic and obscure languages she knew when Bestia decided it was a good idea to challenge her. "]
    $List_Random_Event_Messages += ["It would've been fine if Bestia hadn't decided to use a fantasy language from her books or shows. Glad I stopped it before it got out of hand."]
  return

#--------------- Teacher ----------------------
label lbl_event_random_class_una:
  if not Random_Xisreia:
    #Una event
    show bg hallway
    play music music_school
    Caragh "As I weave my way around crowds of chattering students, I spot a few students running ahead of me. Then, I hear a Banshee screech coming from behind me."
    UnaLoud "\"No running in the halls!\""
    Description "Overwhelmed by the volume of the teacher's screech, the students stop dead in their tracks. For a moment, silence reigned supreme. Suddenly, a student starts crying."
    UnaQuiet "\"Oh no...\""
    Description "The Banshee strides past me and kneels down before the crying kid."
    UnaQuiet "\"Hey, it's me - Ms Una. I'm sorry for making you cry. Are you okay? Were you hurt?\""
    Description "The crying stops. The kid stares at the Banshee, confused as to why the teacher who had just yelled at him would be worried about him. Slowly, he shakes his head."
    UnaQuiet "\"No? That's good. But, hey, you shouldn't be running in the hallways. You might trip and fall. Understand?\""
    Description "The kid gives a tiny nod."
    UnaLoud "\"Okay. Now, go on. I'm sure you have somewhere to be.\""
    Description "The kid smiles and runs off."
    Caragh "Una... She sounds like a good teacher."
    $ Random_Una = True
    $List_Random_Event_Messages += ["I ran into one of the other teachers screeching at the kids running in the halls. A kid cried and, I can't believe this, the kid was louder."]
    $List_Random_Event_Messages += ["Una, I think, felt so bad that she stopped and tried to comfort the kid."]
  return


####################### Morning/Pre-Class Events #################################
label lbl_event_random_morning_sleep_1:
  Caragh "What time is it?"
  Description "I glance over at the clock...and freeze. It's this late already?"
  Caragh "\"The lies you tell!\""
  Description "I refuse to believe the hour and minute hands. I snatch my phone off the bedside table."
  Description "My eyes go wide."
  Description "I leap out of bed."
  Caragh "\"Oh man, oh man, oh man!\""
  Caragh "At this rate, I'm going to be late for work! Ugh, I can feel my stress meter rising. It's a good thing I don't have one or it'd be through the roof!"
  call update_stress(5) from _call_update_stress_3
  $ Random_Oversleep = True
  return

label lbl_event_random_morning_sleep_2:
  Caragh "It's morning already?"
  Caragh "Time flies when you're sleeping, I guess. Speaking of which..."
  Description "I check the time."
  Caragh "It's pretty early so that means I can take my time in the shower today. Yes!"
  call update_stress(-5) from _call_update_stress_4
  return

#----------------------------------------------------------
label lbl_event_random_morning_traffic_1:
  show bg streets with fade
  play music music_school
  Description "The light changes and I turn the corner."
  Description "Traffic is backed up all along the street. It keeps going and going!"
  Caragh "Ugh! I'll never make it to work like this!"
  call update_stress(5) from _call_update_stress_5
  return

label lbl_event_random_morning_traffic_2:
  show bg school with fade
  play music music_school
  Description "There's hardly any traffic at all this morning."
  Caragh "This must be my lucky day!"
  Description "I turn on the radio and listen to music."
  call update_stress(-5) from _call_update_stress_6
  return

####################### Lunch Events #################################

#--------------- You Forget ----------------------
label lbl_event_random_lunch_youforgot_1:
  #No help
  Description "It's finally lunchtime. I reach into my bag and touch the bottom of it."
  Caragh "No way!"
  Caragh "I forgot my lunch."
  Caragh "Ah, wait, I should have a couple of notes in my wallet."
  Description "Unfortunately, that's gone too."
  Caragh "Well, at least the water's free..."
  call update_stress(5) from _call_update_stress_7
  $ Random_Lunch_Forget = True
  return


label lbl_event_random_lunch_youforgot_2:
  #Teachers help
  Description "It's finally lunchtime. I reach into my bag and touch the bottom of it."
  Caragh "No way!"
  Caragh "I forgot my lunch."
  Caragh "Ah, wait, I should have a couple of notes in my wallet."
  Description "Unfortunately, that's gone too."
  Caragh "Well, at least the water's free..."
  Description "Just as I get up from the table, one of the other teachers walks over to me."
  $option = renpy.random.choice(["A", "B"])
  call expression "lbl_event_random_lunch_youforgot_2" + option from _call_expression_23

  return

label lbl_event_random_lunch_youforgot_2A:
  #1
  Teacher "\"Hey there, Caragh. I have some leftovers, if you want any. My eyes are a tad bit bigger than my stomach, I'm afraid.\""
  Caragh "\"Would I ever!\""
  Description "Before I can say anything more, he chuckles and drops not one, not two but three containers of food in front of me. How he was planning on eating all of this, I have no idea, but today's my lucky day."
  Description "I eat and eat and eat but the food just keeps coming!"
  Description "By the end of lunch, I'm full but there's still more."
  Caragh "I'm stuffed! I don't even think I can make it to the door. I just want to sleep..."
  $ Random_Lunch_Teacher = True
  return

label lbl_event_random_lunch_youforgot_2B:
  #2
  Teacher "\"...\""
  Caragh "\"S-Something wrong?\""
  Caragh "She's not saying anything."
  Caragh "\"Um, I'll be right back-\""
  Description "The other teacher holds out a few sandwiches."
  Teacher "\"H-H-Have lunch with me?\""
  Caragh "She looks really nervous. I can't help but smile."
  Caragh "\"Um, okay.\""
  Description "The teacher seems relieved for some reason and she relaxes as she sits across from me."
  Description "Eventually, we end up talking while we eat. It's nice to chat for once instead of just scarfing food down."
  call update_stress(-5) from _call_update_stress_8
  $ Random_Lunch_Teacher = True
  return


label lbl_event_random_lunch_youforgot_3:
  #Students help
  Description "It's finally lunchtime. I reach into my bag and touch the bottom of it."
  Caragh "No way!"
  Caragh "I forgot my lunch."
  Caragh "Ah, wait, I should have a couple of notes in my wallet."
  Description "Unfortunately, that's gone too."
  Caragh "Well, at least the water's free..."
  Description "I start to pull out my wallet when one of the kids come up to my table."
  $option = renpy.random.choice(["A", "B", "C", "D"])
  call expression "lbl_event_random_lunch_youforgot_3" + option from _call_expression_24
  return

label lbl_event_random_lunch_youforgot_3A:
  Description "It's Craig!"
  show Craig
  Description "He's not saying anything. All he's doing is fidgeting with a wad of napkin, clearly wrapped around something."
  Caragh "\"Did you need something, Craig?\""
  Craig "\"...\""
  Caragh "\"Um...\""
  Description "Before I can say anything else, he places the napkin in my hand and scurries off."
  Description "It's strangely heavy."
  Description "I unwrap it and stare down at a piece of fried food."
  Caragh "That kid is precious."
  Description "I take a bite. It's not that bad but it's way too crunchy, whatever it is. I eat the rest in a few more bites."
  Description "As I wipe my mouth, I notice Craig watching me from a nearby table."
  Description "He stares."
  Description "I stare back."
  Description "He stares some more while fidgeting with his tail."
  Description "I smile and give him the thumbs up."
  call update_relationship(Character_Craig, 5) from _call_update_relationship
  Description "Craig ducks his head but not before I catch the grin on his face. At least, I hope he's grinning. His tail kind of jiggled so I hope he's happy at least."
  hide Craig
  $ Random_Lunch_Craig = True
  return

label lbl_event_random_lunch_youforgot_3B:
  Description "It's Hecate!"
  show Hecate
  Description "She silently stands there for a few moments. I can see her hesitance to speak up."
  Hecate "\"No lunch, Teacher?\""
  Caragh "\"No. Sadly, I forgot to bring some.\""
  Description "..."
  Caragh "This is getting a little awkward..."
  Hecate "\"You can have this. I don't want it. I don't even like it.\""
  Description "She slams a small pot on the table."
  Caragh "\"No, it's yours. I can't...\""
  Hecate "\"I have more.\""
  Caragh "You just said you didn't like it."
  Caragh "\"Thank you, Hecate.\""
  Description "Hecate stomps back to her table."
  hide Hecate
  Description "I take the lid off Hecate's pot and..."
  Caragh "This looks horrible. I can tell it's a chowder of some sort but why is it purple? What are these blobs of...meat? What are they? "
  Caragh "Hm? It smells delicious. Maybe..."
  Description "I muster up my courage and scoop up a bite of the purple stew."
  Caragh "It tastes as amazing as it smells!"
  Caragh "It looks so revolting though..."
  Caragh "Food is food, Caragh. Just close your eyes!"
  Description "With closed eyes, I begin to work my way through the chowder."
  Description "When my spoon begin to scrape the bottom of the pot, I feel a sense of sadness yet I feel more relaxed. I'm sad that the food's gone but the food is so good that my stress just melts away. "
  call update_stress(-5) from _call_update_stress_9
  show Hecate
  Caragh "\"That was delicious, Hecate. Thank you so much for sharing.\""
  Hecate "\"Yeah, whatever.\""
  Description "She snatches the pot out of my hands before swiftly turning away."
  Description "Even so, I could spot a faint blush on her cheeks."
  call update_relationship(Character_Hecate, 5) from _call_update_relationship_1
  $ Random_Lunch_Hecate = True
  return

label lbl_event_random_lunch_youforgot_3C:
  Description "It's Sanura!"
  show Sanura
  Description "She plops herself down beside me and lays her lunch box of sandwiches open on the table."
  Sanura "\"Answer this riddle and I'll share some of my sandwiches with you.\""
  Caragh "\"Um...\""
  Sanura "\"It's okay. This is a riddle my mom told me when I was just a baby.\""
  Caragh "I shouldn't feel relieved at hearing it's a riddle for toddlers, yet I am. I can't help it. Those sandwiches look wonderful."
  Sanura "\"What gets wetter the more it dries?\""
  Sanura "\"It's okay if you can't figure this out.\""
  Caragh "She looks so smug, as she should be. She didn't mess up the riddle this time."
  menu:
    "What gets wetter the more it dries?"
    "A Towel":
      Caragh "\"A towel.\""
      Sanura "\"Correct.\""
      Caragh "Don't look so disappointed. Aren't you supposed to be happy I understood the riddle instead of being confused like the previous few times?"
      Description "She slowly takes out two sandwiches from her lunchbox and hands them over."
      Sanura "\"Your prize is some of my favorite tuna sandwiches.\""
      Sanura "\"I hope you like them, Miss Caragh. My mom made them just for me.\""

    "A Scarecrow":
      Caragh "\"A scarecrow.\""
      Sanura "\"Bzzt! Nope!\""
      call update_mood_specific(Character_Sanura, 5) from _call_update_mood_specific_1
      Description "Expecting an answer, I keep quiet. However, Sanura keeps staring at me."
      Caragh "She's trembling with excitement. I made the right move then. She wants her riddles to be understood yet confusing at the same time."
      Caragh "\"Oh, no. What is it then.\""
      Sanura "\"It's a towel!\""
      Sanura "\"Wasn't it a tough one? My mom is just the best at riddles!\""
      Sanura "\"As consolation, you can have two of my sandwiches.\""
      Description "She takes out two sandwiches from her lunchbox and hands them over."
      Sanura "\"Here, these are tuna sandwiches. They're my favorite and my mom made them for me.\""

  Caragh "\"Thank you, Sanura. I'm sure they'll taste amazing.\""
  Description "Sanura's tail flicks with joy. We then spend the rest of the lunch period enjoying our sandwiches."
  call update_relationship(Character_Sanura, 5) from _call_update_relationship_2
  $ Random_Lunch_Sanura = True
  return

label lbl_event_random_lunch_youforgot_3D:
  $student = GetRandomSideStudent()
  Description "It's [student[0]] the [student[1]] from 5C!"
  Description "A plate piled with food is shoved into my hands with the explanation that I was seen without lunch so the kids of 5C decided to share some of their lunch with me."
  Caragh "This plate of food is actually quite horrifying to look at. Before today, I could never have imagined seeing food from over ten different monster cuisines mixed into a single plate."
  Caragh "If these kids were older, I'd assume this is their attempt at hazing."
  Caragh "I can't say no, not to those innocent eyes. "
  Caragh "\"Thank you.\""
  Caragh "This is why it's a bad idea for teachers to eat in the same place as the kids. They're watching me so intently that there's no way I can get out of this without eating some of the food."
  Description "I begin eating, smiling at any kid whose gaze I happen to catch. The more I eat, the faster I swallow. The mix of flavors tastes as bad as it looks."
  Description "Soon, I'm done with the plate. As I move to clear my spot, I thank the kids of 5C as I pass by them. "
  Caragh "\"Thank you. It was so thoughtful of you to share with me some of your food. I appreciate it.\""
  Description "Every kid I thanked would cheer and grin up at me. They look so happy to hear that I enjoyed the meal."
  call update_mood_all(5) from _call_update_mood_all_10
  Description "I excuse myself as soon as I can to rush for the bathrooms. There, the nightmare food haunts me once more."
  Caragh "I swear to never forget my lunch ever again."
  call update_stress(5) from _call_update_stress_10
  $ Random_Lunch_Student = True
  return

#------------------ They Forget ----------------------------------------
label lbl_event_random_lunch_theyforgot_1:
  $student = GetRandomSideStudent()
  Description "As I sit down with my lunch, I spot [student[0]] the [student[1]] staring down at the table."
  Caragh "\"[student[0]], are you okay?\""
  Description "A few moments go by in silence."
  Caragh "I don't see any food around."
  Caragh "\"Oh no, I feel like having some chicken for lunch but I've brought lunch already. [student[0]], could you help me? Do you mind sharing with me?\""
  Description "[student[0]] looks up at me, eyes shimmering with hope and happily nods."
  Description "Word of what happened at lunch spreads. The kids look happier the next time I see them."
  call update_mood_all(5) from _call_update_mood_all_11
  $ Random_Lunch_Share_Student = True
  return

label lbl_event_random_lunch_theyforgot_2:
  Caragh "Ah, lunch. Hm?"
  Description "Out of the corner of my eye, I see one of the other teachers looking rather down with no lunch in sight. "
  Caragh "\"Hey, you doing okay?\""
  Teacher "\"Oh, it's nothing. I left my lunch and wallet at home.\""
  Caragh "\"Ah, well... Would you like to share some food with me? I made a little too much today.\""
  Teacher "\"Really? Thank you so much, Caragh!\""
  Description "We spend the rest of our lunch chatting away. It's so fun. I wonder why I never talked to them before."
  Description "I feel more relaxed afterwards."
  call update_stress(5) from _call_update_stress_11
  $ Random_Lunch_Share_Teacher = True
  return

####################### Evening Events  #################################

label lbl_event_random_evening_eatingout_1:
  #TODO
  show bg streets night
  play music music_school
  Caragh "I don't feel like cooking tonight. I'll just eat out."
  Description "I drive around for a bit, looking for a place to eat."
  $option = renpy.random.choice(["A", "B", "C"])
  call expression "lbl_event_random_evening_eatingout_1" + option from _call_expression_25

  return

label lbl_event_random_evening_eatingout_1A:
  Description "In the end, I give up and walk into a shabby-looking restaurant that's nearby. The food turns out to be surprisingly amazing. It's a feast fit for a king and priced for a peasant."
  call update_stress(-10) from _call_update_stress_12
  return

label lbl_event_random_evening_eatingout_1B:
  Description "I stop by a fast food restaurant. It's one of the greasiest meals I've ever had but it's exactly what I need."
  call update_stress(-5) from _call_update_stress_13
  return

label lbl_event_random_evening_eatingout_1C:
  Description "I decide to dine in a nearby restaurant. It's posh and expensive but the portions are one of the tiniest I've ever seen. I leave as hungry as I arrived."
  call update_stress(5) from _call_update_stress_14
  return


label lbl_event_random_evening_eatingin_1:
  show bg room night
  play music music_bedroom
  Caragh "I'm home early today. I should try out the new recipe I found yesterday."
  $option = renpy.random.choice(["A", "B"])
  call expression "lbl_event_random_evening_eatingin_1" + option from _call_expression_26
  return

label lbl_event_random_evening_eatingin_1A:
  Description "With a few last-minute improvisations and substitutions, dinner is ready."
  Caragh "I didn't follow the recipe to the letter but it's still good."
  call update_stress(-10) from _call_update_stress_15
  return

label lbl_event_random_evening_eatingin_1B:
  Description "I try and follow the recipe..."
  Caragh "It looks burnt. It tastes burnt. At least it's edible. Oh, why did I let myself watch that video on rabbits? I should've been paying attention to my cooking!"
  call update_stress(5) from _call_update_stress_16
  return

label lbl_event_random_evening_eatingin_2:
  show bg room night
  play music music_bedroom
  Caragh "I'm exhausted. I don't feel like cooking or going out for dinner."
  Caragh "I'll just have something delivered."
  Description "When the takeout arrived, it's dripping with the glorious scent of grease."
  Caragh "Aah, that hit the spot. It's exactly what I've been craving lately."
  call update_stress(-5) from _call_update_stress_17
  $renpy.pause(1.0)
  return
