init:
  #event flags
  #should try and move these to the main script for easy reference
  $Bahini_Arc_CurrentVisit = 0
  $Bahini_Arc_TalkCount = 0
  $asked_to_visit = False
  $asked_in_session = False
  $askedAboutCraig = False
  $askedAboutHecate = False
  $askedAboutSanura = False
  $Bahini_Arc_Weekly = 0
  $Bahini_Arc_VisitAllowed = False  
  $questions_cut_short = True
  $Hecate_Arc_BahiniQuestioned = False 
  $Sanura_Arc_BahiniQuestioned1 = False 
  $Sanura_Arc_BahiniQuestioned2 = False 
  
label lbl_event_call_bahini:
  nvl clear
  #"DEBUG: Bahini Relationship score: [Character_Bahini.Relationship]"
  Bahini "Yo, whats up?"
  Caragh "Just wanted to talk to you about something."
  b_phone "Did you have any questions for me about the students?"
  $questions_cut_short = False 
  call lbl_event_bahini_questions from _call_lbl_event_bahini_questions
  "Afterwards you spend some time just chatting with Bahini."
  Caragh "Bahini is always such fun to talk to."
  call update_stress(-10) from _call_update_stress_22
  $Bahini_Arc_TalkCount = Bahini_Arc_TalkCount + 1
  nvl clear
  return

  
#------------------------------------------------------  WEEKLY
label lbl_event_bahini_weekly:

  nvl clear
  $eventName = "None"
  if Bahini_Arc_Weekly == 0:
    $eventName = "lbl_event_bahini_weekly_1"
  if Bahini_Arc_Weekly == 1:
    $eventName = "lbl_event_bahini_weekly_2"
  if Bahini_Arc_Weekly == 2:
    $eventName = "lbl_event_bahini_weekly_3"
  if Bahini_Arc_Weekly == 3:
    $eventName = "lbl_event_bahini_weekly_4"
    
  if not eventName == "None":
    #"testing - [eventName]"
    call expression eventName from _call_expression_27
  nvl clear
  return

label lbl_event_bahini_weekly_1:
  #  Bahini (Week 1)
  #show  Phone 
  nvl clear
  play music  music_bedroom
  b_phone "How was your first week, Kara?"  # Week 1
  c_phone "Eventful and yet not."
  b_phone "First weeks are always like that. Trust me, I'm a veteran."
  b_phone "So, did you get to talk to the three kids I pointed out?"
  c_phone "I did. "

  #Flag/Outcome "Tutored all 3 / Tutored some / Tutored none"     # No good/bad choices as it's just to prompt the player to talk to the kids
  $tutorcount = 0
  if Craig_Arc_CurrentEvent > 0:
    $tutorcount = tutorcount+1
  if Hecate_Arc_CurrentEvent > 0:
    $tutorcount = tutorcount+1
  if Sanura_Arc_CurrentEvent > 0:
    $tutorcount = tutorcount+1

  if tutorcount == 3:
    # + All 3         
    c_phone "I even had time to do an after-class tutoring session with all of them."
    #show  Optional: shocked pikachu face or something similar
    b_phone "Whoa! You work fast! You're like some superhero!"

  if tutorcount > 0 and tutorcount < 3:
    # + Some         
    c_phone "I had time to tutor some of them after class."
    b_phone "That's great! You can always catch up with the rest later. Although, the earlier you talk to them, the more time you have to see how you can help them."

  if tutorcount == 0:
    # + None         
    c_phone "Although, I didn't have any chances to talk to them after the first day."
    b_phone "It's alright. First weeks are tough on everyone. I'm sure you'll find time sometime next week. I believe in you!"

  
  b_phone "Now that you've spent some time with the kids, what do you think of them? "
  b_phone "No, no. They're so different. We can't just talk about them in general."
  b_phone "Let's start with Craig."
  
  b_phone "What do you think about our little snake boy?"


  menu:
    "Reserved":
      # + Quiet         
      c_phone "Craig's rather reserved."
      b_phone "Yes! That's what I thought so too. I remember his old teacher telling me he was such a sweet kid who's always going on about rocks. I wonder if something happened between then and now."
      b_phone "To be fair, Mog's distracted state probably didn't help him much."
    "Polite":
      # + Polite         
      c_phone "He's very polite. "
      b_phone "That he is. He's also a quiet kid. I heard he was a very helpful and sweet kid a few years ago."
      b_phone "I'm glad he wasn't affected by Mog leaving."
    "I don't know": 
      # + I don't know         
      c_phone "I can't get a good grasp of his character."
      b_phone "Really? Craig's such a sweet kid. Didn't you say you had a chance to talk to him?"
      b_phone "Maybe you were confused by his quiet nature."

  b_phone "Now, what about Hecate, our magical prodigy?"

  menu:
    "Sassy":
      c_phone "She's quite sassy."
      b_phone "I thought the same thing too! Especially with how the sparks around her always react to her mood. "
      b_phone "I'm glad she wasn't disheartened by Mog ignoring them."
    "In love with magic":
      # + In love with magic         
      c_phone "She seems in love with magic."      
      b_phone "She wouldn't be the greatest witch of her age if she wasn't. Okay, we don't have a lot of witches her age. But it's still something that can only be born from a love of magic!"     # is it okay to put this?
      b_phone "It would've been terrible if Mog's distracted state dimmed her love."
    "Proud":
      c_phone "She has a lot of pride."
      b_phone "As she should! Who wouldn't feel good after being named the greatest witch of her age? "
      b_phone "Okay, I might've overreacted there. Maybe her confidence made her seem proud to you."

  b_phone "Last of all, what do you think about Sanura?"

  menu:
    "Bubbly":
      c_phone "She's so bubbly."
      b_phone "That she is. Our little sphinx loves to make everyone happy and at home. I'm glad you weren't scared off by her enthusiasm."
      b_phone "Mog told me he was a little intimidated at first."
    "Friendly":
      c_phone "She's very friendly."
      b_phone "Our sphinx loves making friends. She's always available for anyone who needs help. "
      b_phone "She helped Mog a lot throughout the year."
    "Bad at riddles":  
      c_phone "I don't think she's that good at riddles."
      b_phone "She's just a kid. She's learning. "
      b_phone "They aren't that bad. I liked some of them. Even Mog did."
      b_phone "Phew. Now I'm sure you know who I'm talking about. It actually happened to me once. One of the other teachers came up to me and started talking about some of the kids we've taught."
      b_phone "I was so confused. Her descriptions of the kids were so off that I thought I was suffering from amnesia."
      b_phone "It wouldn't be a surpise. I fall so often that it's a miracle my brain still works."
      b_phone "We went round and round and round. Finally, I realized what was going on."
      b_phone "She had mixed up the kids' names!"
      b_phone "When I told her that, she let out such a huge sigh of relief that, I kid you not, the entire hallway was covered in frost."
      b_phone "Oh, I forgot to tell you. She has ice magic."
      b_phone "Anyway, it turns out that she was using me to test her own memory!"
      b_phone "That incident has now been seared into my brain. I swore to myself:"
      b_phone "Never again will I let this happen to me. I will test the other person!"
      c_phone "I see... That must've been traumatizing."
      b_phone "Thanks for being so understanding. Not many people do."
      b_phone "Oh, by the way, about Mog..."
      b_phone "Oh, shoot. The doctor's here."
      b_phone "I have to go. I'll talk to you next week!"
      c_phone "Take care."
  $Bahini_Arc_Weekly = 1
  return

label lbl_event_bahini_weekly_2:
  # "Bahini (Week 2)"
  play music  music_bedroom
  b_phone "How's my favorite Dullahan doing? " # Week 2
  b_phone "How are the kids? Anything interesting happen this week?"
  c_phone "They're good."

  #Flag/Outcome "RANDOM EVENT TEXT TABLE"     # insert comment for every random event that occurred in the past week
  call lbl_event_bahini_random_summary from _call_lbl_event_bahini_random_summary

  if len(List_Random_Event_Messages) > 0:
    b_phone "That's great to hear! Oh, I'm sorry about how I left you hanging last week."
    #clear the list      
    $List_Random_Event_Messages = []
  else:    
    b_phone "Oh, I'm sorry about how I left you hanging last week."     
  b_phone "About Mog..."
  b_phone "I was supposed to tell you about him before your classes so you'd be prepared."
  b_phone "Sorry for forgetting about that. I'll make it up to you one day!"
  b_phone "But it looks like you were more than capable for the job than Nyx thought."
  b_phone "So, Mog is the teacher 5C had for most of the year."
  b_phone "We didn't realize it until late in the year that Mog had been very distracted."
  b_phone "During break between this year and last, his mother was diagnosed with a terminal illness."
  b_phone "I know, ogres rarely fall sick to terminal illnesses."
  b_phone "It was just...bad luck."
  b_phone "When Nyx found out, she forced Mog to go home and take care of his mother."
  b_phone "He'll be coming back one day but 5C needed a teacher until then."
  b_phone "We didn't realize how far behind the kids were until I gave them a pop quiz to see where they left off."
  b_phone "Most of them were going to fail the year-end exams if we didn't do anything."
  b_phone "Of course, that's no problem for me. I'm one of the best teachers around!"
  b_phone "Until my accident and now I'm stuck at the hospital."
  b_phone "I'm really glad you were able to pick up the slack. "
  b_phone "It's bad enough that I left the kids when they needed a teacher the most."
  b_phone "It would've been worse if Nyx couldn't find a replacement in time."
  c_phone "It's not your fault. It was an accident."
  b_phone "That it was, but I'm always getting into accidents."
  b_phone "But hey, you wouldn't have that class list I put together for you if I wasn't."
  b_phone "I knew it was highly likely something would happen to me."
  c_phone "Bahini..."
  c_phone "Thank you."
  b_phone "You're welcome! "
  b_phone "Right! Do you have any questions for me?"

  #if not already alowed see if bahini will invite caragh to visit
  call lbl_event_bahini_visit_permission from _call_lbl_event_bahini_visit_permission
  b_phone "Now, do you have any questions for me about the students?"
  $questions_cut_short = True
  call lbl_event_bahini_questions from _call_lbl_event_bahini_questions_1
  $Bahini_Arc_Weekly = 2
  return

label lbl_event_bahini_weekly_3:
  # "Bahini (Week 3)"      #show  Phone 
  play music  music_bedroom
  b_phone "Heya, Kara! How's it going?" # Week 3
  b_phone "Anything interesting happen while I've been stuck in bed?"
  c_phone "Hi, Bahini!"

  #Flag/Outcome "RANDOM EVENT TEXT TABLE"     # insert comment for every random event that occurred in the past week
  call lbl_event_bahini_random_summary from _call_lbl_event_bahini_random_summary_1

  if len(List_Random_Event_Messages) > 0:
    b_phone "I see. What an interesting week you've had."
    #clear the list      
    $List_Random_Event_Messages = []
  b_phone "Next week is the last week before the exams. Nervous?"

  menu:
    "Yes":
        c_phone "I am. I've never taught kids before."
        c_phone "I'm worried I've failed them."
        b_phone "I believe in you. You can do it!"
        c_phone "Thanks for the encouragement and tips, Bahini."   
    "A little":
        c_phone "I am, a little. Some of them are still lagging behind."
        c_phone "I'm worried about them and how they'll do."
        b_phone "Don't worry so much! You've done a lot already. I can see that."
        # Insert some last-minute tips on gameplay/scoring mechanics
        c_phone "Thanks, Bahini. You're the best."
    "No":
        c_phone "Not at all. "
        c_phone "I've done the best I can for these kids and I know they've done their best."
        b_phone "Amazing! I love how confident you are. It shows just how well you know the kids."
        b_phone "After nearly a year without any proper guidance, I'm sure the kids appreciate all you've done for them in the past month."


  b_phone "So, any other questions? "     # If there are no options available, skip this line and go to the alternate script starting at G146
  
  #if not already alowed see if bahini will invite caragh to visit
  call lbl_event_bahini_visit_permission from _call_lbl_event_bahini_visit_permission_1
  b_phone "Now, do you have any questions for me about the students?" 
  $questions_cut_short = True
  call lbl_event_bahini_questions from _call_lbl_event_bahini_questions_2
  
  $Bahini_Arc_Weekly = 3
  return

label lbl_event_bahini_weekly_4:
  # "Bahini (Week 4)"
  play music  music_bedroom
  b_phone "Kara, Kara, Kara!"
  b_phone "I'll be getting out of the hospital soon! I finally have a tentative date."
  b_phone "It's going to be the first Friday of November."
  c_phone "Congratulations! "
  b_phone "Thank you! "
  b_phone "Right. Tell me all the new stuff that's going on with the kiddies. Anything interesting happen?"

  #Flag/Outcome "RANDOM EVENT TEXT TABLE"     # insert comment for every random event that occurred in the past week
  call lbl_event_bahini_random_summary from _call_lbl_event_bahini_random_summary_2

  if len(List_Random_Event_Messages) > 0:
    b_phone "Haha, what a fun week you've had."
    #clear the list      
    $List_Random_Event_Messages = []
  b_phone "It's the last Sunday of October. The exams are on Monday."
  b_phone "There's no much we can do now but wait and hope."
  b_phone "I believe you've done all you could and you have excelled in taking care of the kids."
  b_phone "Those little monsters will handle themselves fine."
  b_phone "So, sit back, relax and try not to worry too much."
  b_phone "Take care and good luck!"
  c_phone "Thank you, Bahini. For being here and supporting me through the month."
  c_phone "I don't know what I'd do with the kids without you."

  if Bahini_Arc_TalkCount > 6 or Bahini_Arc_CurrentVisit > 2: #Flag/Outcome "Total number of visits = 2 or more"
    show  Caragh
    Caragh "I can't imagine life without your sunshine now."
    
  $Bahini_Arc_Weekly = 4
  return

#------------------------------------------------------  VISITS
label lbl_event_bahini_visit_permission:
  #Flag/Outcome "Total number of chats with Bahini: >2"  
  if not Bahini_Arc_VisitAllowed and Bahini_Arc_TalkCount > 2:
    b_phone "Oh wait before that, are you doing anything on Sunday?"
    b_phone "I didn't have anything planned, why?"
    b_phone "Do you want to visit me at the hospital?"
    c_phone "Is it okay?"      
    b_phone "Please! You'd be doing me a favor, breaking up the monotony of this dreary hospital"
    c_phone "Then sure."      
    b_phone "Of course! You're free to come over anytime, but Sundays are the best. There aren't as many people waking me up and asking me how I'm feeling then. If you come any other day of the week, I'd probably be asleep and that won't do!"      
    b_phone "My room is 1208. That's floor 1, ward 2, and room 8. If you're ever lost, just ask for the resident Mummy patient. They'll know who I am."      
    c_phone "Got it."       
  $Bahini_Arc_VisitAllowed = True
  return

label lbl_event_bahini_visit:
  nvl clear
  $eventName = "None"
  if Bahini_Arc_VisitAllowed:
    if Bahini_Arc_CurrentVisit == 0:
      $eventName = "lbl_event_bahini_visit_1"
    if Bahini_Arc_CurrentVisit == 1:
      $eventName = "lbl_event_bahini_visit_2"
    if Bahini_Arc_CurrentVisit == 2:
      $eventName = "lbl_event_bahini_visit_3"
    
  if not eventName == "None":
    call expression eventName from _call_expression_28
  nvl clear
  return

label lbl_event_bahini_visit_1:
  #"Hospital Visit 01"
  show bg room
  play music  music_bedroom
  show  Caragh
  Caragh "Room 1208. Remember, Bahini is in Room 1208. "
  Caragh "It'll be easy. The hospital has clear signs. There's no way I can get lost, right?"
  show bg hospital with fade
  play music  music_hospital
  Caragh "Ward 2, Room 1208!"
  Caragh "This is it. I just need to find Bahini's bed."
  Caragh "Okay, calm down. Deep breaths."
  Caragh "It's fine. I'm only visiting Bahini. We've talked a lot. We're not strangers. This won't be awkward."
  Caragh "The nurse said I have 45 minutes until visiting hours are over."
  Caragh "Should I have come later?"
  Caragh "No!"
  Caragh "No, Bahini has done a lot for you. She's bored in the hospital."
  Caragh "Is 45 minutes of socializing with someone new really that bad? "
  Caragh "I..."
  Bahini "\"Kara, is that you?\""
  show  Bahini
  Bahini "\"That is you, right? You're Kara from Echidna's School for Little Monsters?\""
  Caragh "\"Yes, that's me.\""
  Caragh "\"Hello, Bahini. It's great to see you in person.\""
  show Bahini smile with dissolve
  Bahini "\"Great to see you too, Kar-\""
  show Bahini sad with dissolve
  Bahini "\"Wait! Why are you being so formal with me?\""
  Bahini "\"You know I don't do that.\""
  Bahini "\"Kara, what took you so long?\""
  Bahini "\"I couldn't eat. I couldn't sleep. I was up all day thinking about you!\""
  show Caragh snark with dissolve
  Caragh "The plate of nearly-finished food begs to differ, Bahini."
  Caragh "\"Sorry, I didn't want to distract you from your meal.\""
  Bahini "\"Not a problem! Food is never as important as a first meeting with an old friend.\""
  show Bahini wink with dissolve
  Description "Bahini winks, a cheeky smile hanging off her lips."
  show Bahini happy with dissolve
  Bahini "\"Come, sit! Don't just stand there. You're a visitor and we have another hour before the nurse would come by to kick you out.\""
  Caragh "\"The nurse at the desk said 45 minutes.\""
  show Bahini wink with dissolve
  Bahini "\"Bah, what does she know? She's not the one who's tasked with kicking visitors out today.\""
  Bahini "\"I know the guy who has that job. He's too soft. He always takes an extra 5 to 10 minutes when it comes to chasing away-\""
  Description "Bahini is interrupted by loud laughter from the room next door."
  Bahini "\"-ahem. As I was saying, he needs more time to get that room's guests out of here.\""
  Caragh "\"Are they that bad?\""
  Bahini "\"No, they're not bad or rude. The patient is the reason.\""
  show Bahini sad with dissolve
  Bahini "\"He's really crotchety, likes waking up every 2 hours to shout for the nurses to help him to the toilet.\""
  Bahini "\"He's adamant that he's strong enough to walk to the toilet, do his business and then walk out without help.\""
  Bahini "\"That means the nurses are forced to leave him be and come back when he rings for them.\""
  Bahini "\"Determination and persistence isn't a bad thing when you're an old man.\""
  Bahini "\"It just means more noise.\""
  show Bahini smile with dissolve
  Bahini "\"Now, imagine that this old man is only ever happy when his sons drop by at lunch and you're a nurse new to this hospital, this ward and just nursing in general.\""
  show Bahini sad with dissolve
  Bahini "\"Wouldn't you find it challenging to chase away the only source of the old man's joy?\""
  Caragh "\"That does seem like a tough job.\""
  Caragh "It sounds harder than herding teenagers. Only half of them are as bull-headed as this guy seems to be and most of them have better things to do than to fight with you all day."
  show Bahini smile with dissolve
  Bahini "\"The new kid's done a pretty good job so far. Some of the others take as long as 30 minutes before they can get away from the old man's lecture.\""
  Caragh "\"It sounds like you know the patient next door and the nurses pretty well.\""
  Bahini "\"What can I say? Perks of being the clumsiest mummy alive.\""
  Bahini "\"I've been in here so often that I even know the names of Jonathan's grandnephews, and they only visit him on the second last day of his stays.\""     # Random name for random character. Is the name off compared to the rest of the world's?
  Bahini "\"Jonathan's the old man, by the way.\""
  Caragh "\"Clumsiest? You mentioned being in here a lot but was it all just due to that?\""
  Bahini "\"Well, most of it is due to bad luck. I don't like viewing it that way though.\""
  show Bahini sad with dissolve
  Bahini "\"The world will seem like a bleak place if everything that ever happened to me is because of bad luck.\""
  Bahini "\"That means I'm such a horribly mummy that the world hates me!\""
  show Bahini wink with dissolve
  Bahini "\"No, no. Much better to say I'm clumsy.\""
  Bahini "\"It's technically not wrong.\""
  Bahini "\"Alright! Enough about me.\""
  show Bahini sad with dissolve
  Bahini "\"Our conversations are always about me and you're making me feel bad about it.\""
  show Bahini happy with dissolve
  Bahini "\"Tell me about yourself.\""
  Bahini "\"You never say anything over the phone.\""
  show Bahini wink with dissolve
  Bahini "\"What is your favorite color? What about favorite food? Who's your favorite kid so far? Which kid gets on your nerves? Do you have a favorite riddle from Sanura?\""
  Caragh "\"Well, I...\""
  Caragh "Time flies when I'm with Bahini. It's a sensation that only grows stronger when I'm physically there with her and not just talking to her over black-and-white words. It's a wonderful feeling."
  play sound sfx_knock  
  Nurse "\"Hi, Bahini and Bahini's guest. Visiting hours are over. We'd appreciate it if you could wrap up now.\""
  show Bahini wink with dissolve
  Bahini "\"Got'cha! Don't worry about us. Kara will be out of your hair right away.\""
  Description "..."
  show Bahini smile with dissolve
  Caragh "\"It was nice talking to you, Bahini.\""
  Bahini "\"Great chat today, Kara. Come back soon.\""
  Bahini "\"Please? At least during Sunday lunchtimes?\""
  Bahini "\"It's so boring in here and there's only so much of Jonathan's lecture I can overhear before I've memorized every word in every variation he's done.\""
  Caragh "\"I'll do my best. Talk to you later.\""
  Bahini "\"Take care!\""
  
  $Bahini_Arc_CurrentVisit = 1
  return#  END SCENE

label lbl_event_bahini_visit_2:
  #"Hospital Visit 02"
  show bg hospital with fade
  play music  music_hospital
  show Bahini wink with dissolve
  Bahini "\"Kara, welcome back to my humble abode!\""
  Bahini "\"Thank you so much for visiting me again!\""
  show Bahini sad with dissolve
  Bahini "\"The only person I ever see is Nyx when she asks me for my notes.\""
  Caragh "\"Hi, Bahini. How was lunch?\""
  show Bahini smile with dissolve
  Bahini "\"It wasn't bad. Could do with less salt.\""
  Bahini "\"How do you have such good timing? Last time, you also came in just as I've finished my lunch.\""
  Caragh "\"Good luck, I guess.\""
  Caragh "Well, I did come at the same time as last time."
  Caragh "It's probably for the best that she doesn't know I'm doing it deliberately."
  Description "Bahini's eyes squint into slits as her gaze bore into mine."
  Caragh "\"What is it?\""
  show Bahini wink with dissolve
  Bahini "\"I bet you planned this, didn't you?\""
  Bahini "\"You knew that if you came here a few minutes earlier, you would have to deal with the Great War of Peas.\""
  Bahini "\"You intentionally came late to the party because you've turned to the Dark Side, the Peas' side.\""
  
  show Caragh rly with dissolve
  Caragh "The Peas' side?"
  show Caragh happy with dissolve
  Description "A chuckle escapes my nose."
  Bahini "\"Aha! An admission of guilt! Traitor!\""
  Caragh "This is so absurd but she's having fun. It's not like me but if I just play along..."
  show Caragh snark with dissolve
  Caragh "\"Okay, okay. I admit defeat!\""
  Caragh "\"Please have mercy, o Mighty Bahini!\""
  Bahini "\"That depends. Will you be staying until visiting hours are over and swear to shield my ears from Jonathan's lecture?\""
  Caragh "\"Of course, my liege.\""
  Bahini "\"Then, you may sit.\""
  Caragh "\"Thank you, o Merciful One.\""
  Caragh "\"So, how did you know?\""
  Bahini "\"Hm? Know what?\""
  Caragh "\"How did you know my plan was not to come at the start of visiting hours?\""
  Bahini "\"I didn't. It was a guess.\""
  Caragh "\"Oh. Well, Bahini, I-\""
  show Bahini smile with dissolve
  Bahini "\"It's fine. Don't apologize for it. I'm not your girlfriend or family. I also didn't specify I'd like you to be here throughout the time slot. I only asked that you visit me.\""
  Bahini "\"What's there for me to be angry about?\""
  Bahini "\"All I need to know is that you're here as promised.\""
  Caragh "\"Thank you, Bahini.\""
  show Bahini wink with dissolve
  Bahini "\"Although, it'd be different if I were your girlfriend. Such a breakdown of miscommunication is a big no-no in my books.\""
  Bahini "\"Queen Bahini will insist that you grovel for forgiveness then.\""
  show Caragh content with dissolve
  Caragh "\"I'll keep that in mind.\""
  show Caragh sad with dissolve
  Caragh "Wait, what? Keep that in mind for what? For when I'm her girlfriend? Caragh, get yourself together."
  show Caragh happy with dissolve
  Caragh "\"Anyway, what's going on with 'The Great War of Peas'?\""
  Caragh "\"Do you have peas that much?\""
  Bahini "\"Oh, I like peas. I just don't like the way they cook it here.\""
  Bahini "\"It's so grainy and mushy. It's the textbook example of 'ick'.\""
  Caragh "\"Aren't peas meant to be grainy and mushy?\""
  show Bahini sad with dissolve
  Bahini "\"No! How dare you utter such attrocities!\""
  show Bahini wink with dissolve
  Bahini "\"Kara, if you weren't one of my best friends, I would be flinging a spoon of peas in your face.\""
  Caragh "There are no more peas left on your plate. "
  Caragh "\"One of your best friends? I'm...\""
  show Caragh sad with dissolve
  Caragh "Why do I feel sad? I should be happy, right?"
  Caragh "\"-honored.\""
  Bahini "\"Darn right, you should be!\""
  Bahini "\"When I'm finally back in my home and free to cook again, I'll show you the glorious world of peas cooked right!\""
  Caragh "\"I look forward to the day.\""
  Caragh "If I'm still around then."
  Description "..."
  Description "..."
  Bahini "\"You know, being stuck here has left me with nothing to do but think and wonder.\""
  Bahini "\"I'm halfway through my twenties now. Time flies.\""
  Bahini "\"It seems like it was only yesterday that I went on adventures and fought imaginary foes. Every day was a wonder.\""
  Caragh "\"I wouldn't call it yesterday. You did just wage war with some peas a few minutes ago.\""
  Bahini "\"Oh, hush. I was trying to make things less awkward!\""
  Caragh "\"Sorry, do go on.\""
  Bahini "\"I can't get back into the mood anymore. Nostalgia's not my thing anyway.\""
  Bahini "\"I don't like dwelling on the past. I much prefer to focus on the present and the bright future that awaits me.\""
  Bahini "\"For example, what food will you bring me on your next visit?\""
  Caragh "\"What food? Did I promise to do that?\""
  Bahini "\"You just did with your interruption just now.\""
  Bahini "\"Be careful when interrupting the Great Bahini! Do so again and I might just confess my love for you.\""
  Caragh "\"I... Yes, my liege?\""
  Caragh "Why did my heart just skip a beat there? Have I...?"
  Caragh "No, it can't be. We've known each other for less than a month. "
  Caragh "Maybe..."
  
  $Bahini_Arc_CurrentVisit = 2
  return#  END SCENE   # Bit of an unnatural-ish end here and I've merged with the "realize feelings for Bahini" plot point here.

label lbl_event_bahini_visit_3:
  #"Hospital Visit 03"
  show bg hospital with fade
  play music  music_hospital # By my calculations, this visit will only happen on the 28th
  show  Bahini
  Bahini "\"Kara, you're here early!\""
  Bahini "\"Show me! What did you bring me for lunch?\""
  Caragh "\"Well, you mentioned you wanted something with a little spice in it.\""
  Caragh "\"I don't know how much spice you can take, so I brought you a bowl of hot stew.\""
  Bahini "\"Hot soup? That's not...\""
  Bahini "\"Oh! You mean, spicy stew!\""
  Caragh "\"Aw, you realized what I meant too quickly.\""
  Caragh "\"I thought I could have some fun.\""
  Bahini "\"Hang around 5C's kids for long enough and you'll get the hang of knowing when a joke is coming.\""
  Caragh "\"Or a riddle. I've heard a lot from Sanura.\""
  Bahini "\"She's probably nervous. Tomorrow's the exams.\""
  Bahini "\"Frankly, I didn't expect you to be here.\""
  Caragh "\"Why not?\""
  Bahini "\"If it were me, I'd be tearing my hair out with anxiety.\""
  Caragh "\"Well, I took some advice from a certain mummy and decided to sit back, relax and not worry too much.\""
  Bahini "\"Hey, that's not fair! You can't use my own words against me.\""
  Caragh "\"You are an important part of my life. Whose words would I use if not yours?\""
  Bahini "\"I...\""
  Bahini "\"Maybe...\""
  Caragh "\"Anyway, you're going to be leaving the hospital soon.\""
  Caragh "\"Again, congratulations. Any plans for what you'll be doing first once you're out?\""
  Bahini "\"The first thing I'll be doing is go home and have 12 hours of uninterrupted sleep.\""
  Bahini "\"Then, I'll whip up a meal to show you just what peas should taste like. I'll make you eat so much of them that you'll have to stay the night.\""
  Caragh "\"Is that a promise?\""
  Bahini "\"Of course! Even if you turn traitor again and refuse to eat everything I serve you, you will still have to stay the night. You need to repent for your sins.\""
  Caragh "\"I'll be sure to repent properly.\""
  Bahini "\"You'd better.\""
  Description "Out of nowhere, our cheerful banter drops into an awkward silence."
  Bahini "\"...\""
  Bahini "\"Right. I've made up my mind. You need to start repenting now.\""
  Caragh "\"Wait, what?\""
  Bahini "\"You have two choices: feed me the stew or I feed you the stew.\""
  Caragh "\"But the food is meant for you and I only have two hands...\""
  Bahini "\"I have two hands and a table. Do you trust me?\""
  Caragh "\"I do. I'm fine with anything but what are you...\""
  scene cg bahini_feed with dissolve
  play music music_good_vibes
  $renpy.pause(delay=2.0, hard=False)
  show Caragh body
  Description "For a moment, everything before my eyes spins. The room shifts and I'm surrounded by a soft warmth. Bahini had grabbed my head and put it on her lap."
  Caragh "\"B-Bahini...?\""
  Caragh "\"We're still at the hospital. I...\""
  Bahini "\"Be a good girl and feed me my food.\""
  Caragh "\"Okay but, um, I...\""
  Bahini "\"This stew's pretty good. What did you put in there?\""
  Caragh "\"Bahini, the door's still open...\""
  Bahini "\"No, don't tell me. Peas?\""
  Caragh "\"I...\""
  Caragh "There's no point fighting Bahini when she's this stubborn."
  Caragh "\"Not everything is about peas, Bahini.\""
  Bahini "\"Darn it. I thought you were going somewhere with it.\""
  Bahini "\"On second thought, don't tell me. I'm going to unravel your secrets right before your eyes!\""
  Bahini "\"Is there any...meat?\""
  Caragh "\"Yes...\""
  Bahini "\"Pea-meat?\""
  Caragh "\"What? No! Just focus on your food!\""
  Bahini "\"Shoot! I thought you were just bluffing.\""
  Caragh "I don't think I've ever had to talk about peas for so long. I didn't even think anyone would be interested enough to keep up such a ridiculous conversation."
  Caragh "It's also the first time my head has ever felt so comfortable outside of my own arms. It's nice."
  Caragh "Bahini..."
  #show  FADE AWAY
  scene bg black with dissolve
  
  $Bahini_Arc_CurrentVisit = 3
  return
  #"END OF BAHINI-SPECIFIC SCRIPT - EVENING TEXTS ARE TO BE FOUND IN EVENING/NYX"

#------------------------------------------------------  QUESTIONS
$Bahini_Question_Craig_1 = False
label lbl_event_bahini_questions:
  $bahini_helped = False
  $askedAboutCraig = True
  $askedAboutHecate = True
  $askedAboutSanura = True
  if Craig_Arc_CurrentEvent > 0 and Craig_Arc_CurrentEvent < 3 and not Craig_Arc_BahiniQuestioned:
    $askedAboutCraig = False
  if Hecate_Arc_CurrentEvent == 1 and not Hecate_Arc_BahiniQuestioned:
    $askedAboutHecate = False
  if (Sanura_Arc_CurrentEvent == 2 and not Sanura_Arc_BahiniQuestioned1) and (Sanura_Arc_CurrentEvent == 4 and not Sanura_Arc_BahiniQuestioned2):
    $askedAboutSanura = False
    
  if not askedAboutCraig and not askedAboutHecate and not askedAboutSanura:
    return

label lbl_event_bahini_questions_ask:

  $ asked_in_session = False #to reset flag jic
  menu:
      "Ask about Craig" if not askedAboutCraig:
        call lbl_event_bahini_questions_craig from _call_lbl_event_bahini_questions_craig
        $ askedAboutCraig = True
        $bahini_helped = True
        jump lbl_event_bahini_questions_ask
      "Ask about Hecate" if not askedAboutHecate:
        call lbl_event_bahini_questions_hecate from _call_lbl_event_bahini_questions_hecate
        $ askedAboutHecate = True
        $bahini_helped = True
        jump lbl_event_bahini_questions_ask
      "Ask about Sanura" if not askedAboutSanura:
        call lbl_event_bahini_questions_sanura from _call_lbl_event_bahini_questions_sanura
        $ askedAboutSanura = True
        $bahini_helped = True
        jump lbl_event_bahini_questions_ask
      "No, not really." :
        call lbl_event_bahini_questions_end from _call_lbl_event_bahini_questions_end
  return  

label lbl_event_bahini_questions_craig:
  if Craig_Arc_CurrentEvent <= 2:
    # + Craig "Craig (AFTER Learn about Problem)"      
    c_phone "I've encountered a problem with Craig."
    b_phone "Oh, what is it? How can I help?"
    c_phone "You know about Craig's hood?"
    c_phone "He always keeps it pulled so low that I can never see his face."
    b_phone "Yes, I remember that hood. I chalked it up to being shy but I hear he didn't do that when he was still a little boy."
    b_phone "Maybe he's experimenting with his style. He is going through puberty."
    c_phone "Craig told me he does it because he's scared of his own eyes."
    c_phone "According to him, his gaze has gone out of control since last year. "
    c_phone "He's afraid of hurting someone."
    b_phone "Oh no, poor thing! I thought Basilisks could always control their petrifying gaze."
    c_phone "Do you have any ideas what we can do to help him be free of the hood?"
    c_phone "He won't even look up at the board when I'm teaching."
    c_phone "I don't think anyone can learn in that state."
    b_phone "That's true! Why didn't I realize the hood would be blocking his eyes from seeing as well?"
    b_phone "Hm..." #show  optional: thinking hard image/sticker
    b_phone "I'll look through my phone and see if I can find anyone who can help me."
    b_phone "I'm sure I have a Cockatrice or two saved up in here."
    b_phone "In the meantime, do you want to talk to his parents and see if they can help?"
    #Flag/Outcome "Have talked to parents / Have not talked to parents"      

  if Craig_Arc_CurrentEvent == 2:
    #- Have talked         
    c_phone "Oh, I have. "
    c_phone "They couldn't provide me with any help as they didn't have any paralysis or petrification powers."
    b_phone "They don't? That's strange. Kids usually inherit their parents' powers."
    c_phone "It's a special situation."
    b_phone "Right! Tell me no more. Craig didn't mention anything to me and neither did Mog. If Craig wanted us to know, he would've told us."
    b_phone "I'll wait until Craig feels comfortable enough to tell me."
    c_phone "Thanks for understanding."
    b_phone "Don't worry about it!"
    b_phone "Oh, right. I found our guy! I'll ask him about a solution for you."
    c_phone "Thank you."     # Would it be better if Bahini contacted him instead?
    b_phone "I'll let you know if I find out anything."

    #Decided to leave this to use the same mini event as the not talked verion, will allow some time to pass instead of her receiving a perfect response in the middle of texting with Caragh
    #b_phone "Whoa, Ambrose replies fast!"     # Cockatrice name is = ??? (I'm bad with names, haha)
    #b_phone "He's forwarded me a link to some spectacles his kind uses during puberty. Apparently, all monsters with paralysis or petrification powers go through an unstable period. The more powerful they are, the longer the period is. Here, I'll send the link to you!"      
    #b_phone "\[Bahini has shared a link with you: Shield Specs\]"      
    #b_phone "Hopefully, these will help Craig."      
    b_phone "So, do you have any other questions?"     # Loop back to original choice without Craig available
    $Craig_Arc_BahiniQuestioned = True
    return
  else:
      #- Haven't talked         
      c_phone "I planned on doing so."
      b_phone "Their number should be in Craig's file."
      b_phone "I'll let you know when I find someone who can help you with Craig."
      b_phone "Until then, stay strong and keep looking!"
      b_phone "So, do you have any other questions?"
      $Craig_Arc_BahiniQuestioned = True
  return

label lbl_event_bahini_questions_hecate:
  if Hecate_Arc_CurrentEvent == 1:
    # + Hecate "Hecate (AFTER Learn about Problem)"      
    c_phone "I've bumped into some issues with Hecate."
    b_phone "Oh, what is it? How can I help?"
    c_phone "I can't seem to get through to her."
    c_phone "I can tell that she's smart but she doesn't pay attention in class. She keeps playing around with her magic."
    c_phone "It's not the usual fidgeting either. I can see her focus all her attention on the sparks and manipulating them into different shapes and colours."
    c_phone "I've tried asking her to at least hold back from working on her magic during our tutoring sessions."
    c_phone "It works. A little. She doesn't do it anymore but her mind is still not focused on what I'm teaching."
    c_phone "It's like dealing with a teenager but not. "
    c_phone "With a teenager, I could use the carrot-and-stick method."
    c_phone "With Hecate, neither the carrot nor the stick works."
    c_phone "How did the teachers handle Hecate before?"
    b_phone "Hecate has always been proud of her magic. In fact, that might be the only subject I've ever seen her be proud of."
    b_phone "Even so, she's never been so close to failing her other subjects before."
    b_phone "Mog's notes were..."
    b_phone "Let's just say they might not have existed when it came to Hecate."
    b_phone "Have you tried talking to her parents?"
    b_phone "They're both great witches. She might listen if they speak to her."
    c_phone "I don't know..."
    c_phone "She didn't have much to say about her parents."
    b_phone "Oh..."
    b_phone "To be fair, her parents are quite busy."
    b_phone "I've heard some teachers comment on it in the past."
    b_phone "Because of their schedules, it's hard to get in touch with them."
    c_phone "Schedules?"
    b_phone "Hecate's parents are usually working on projects that require the moonlight."
    c_phone "Oh, they're nocturnal?"
    b_phone "Yeah. I don't think there's a teacher in the school who has met them yet."
    c_phone "I see..."
    b_phone "I don't know if this will be of any help but..."
    b_phone "Our school does have a therapist."
    if not Jo_Arc_LearnedAboutJo:
      c_phone "We do?"
      b_phone "Yup! Monster kids traumatize each other and themselves so easily. Nyx had the idea that we needed one, even though nothing has happened yet."
      c_phone "Who is it?"
      b_phone "Have you been to the library yet?"
      b_phone "It's Librarian Jo. They're invisible so you'll only see a floating mask."
    else:
      c_phone "Oh right, of course. Jo the Librarian."
    if Jo_Arc_CurrentEvent == 1:
        c_phone "I've met them before."
    else:
        c_phone "No, I haven't met them yet."

    b_phone "I'm sure they can help you with Hecate."
    c_phone "I see. Thanks for the tip, Bahini."
    b_phone "No problem! "
    b_phone "Okay. Any other questions for me?"     # Loop back to original choice without Hecate available
    $Jo_Arc_LearnedAboutJo = True
    $Hecate_Arc_BahiniQuestioned = True
    return

label lbl_event_bahini_questions_sanura:
  if Sanura_Arc_CurrentEvent == 2:
    # + Sanura "Sanura (AFTER Learn about Problem # + 1 class)"      
    c_phone "I'm not sure what to do with Sanura."
    b_phone "Oh, what happened? She's such a sweet and attentive girl. Surely, she'll be no problem?"
    c_phone "Sanura is sweet and attentive. She's just..."
    c_phone "I don't mean to insult her riddling abilities. I like some of them."
    c_phone "However, she's not that good at riddles."
    c_phone "That won't do for her since she loves riddles."
    c_phone "She pays attention during tutoring sessions but classes are a completely different matter."
    c_phone "She's always drifting off. I can see her lips move as she tries out new riddles."
    c_phone "I've talked to her about it and she said she'll be better."
    c_phone "But I don't think the talk made a difference."
    c_phone "I don't want to be mean and reprimand her again but I don't feel like I have a choice."
    b_phone "That is a tough situation, especially for a teacher who hasn't dealt with kids before."
    b_phone "Honestly, some of her riddles do fall flat. They're not bad. They're just not the best."
    b_phone "It's strange though. Her mother is such a good spinner of riddles."
    b_phone "I loved hearing about Sanura's parent-teacher conferences because of that."
    c_phone "Just the mom?"
    b_phone "Oh, yeah. I don't think I've put it in the class list. Sanura is raised in a single-parent household. I don't know what happened to the dad but he is out of the picture."
    c_phone "Oh..."
    b_phone "On the bright side, Sanura's mom has done a great job so far and Sanura has somehow side-stepped all of the issues most single-parent kids face."
    b_phone "Okay, not all. "
    b_phone "Mog sometimes thought she's a little too keen on being helpful."
    b_phone "I..."     # slight 1 second pause to indicate shift of topic
    b_phone "I think you should try talking to Sanura's mom. When she first enrolled Sanura, she told us we could call her anytime for anything related to Sanura."
    b_phone "Maybe she can give you some advice or she might talk sense into Sanura."
    c_phone "Maybe. It'd be good if she could shift most of her focus from riddles. Just for the month will do. I don't want to take something she loves away from her."
    c_phone "I'm just worried..."
    b_phone "You can do it! I believe in your abilities to help Sanura out. "
    c_phone "Thanks, Bahini. "
    b_phone "No problem! Anything else I can help with?"     # Loop back to original choice without Sanura 
    $Sanura_Arc_BahiniQuestioned1 = True
    
    
  if Sanura_Arc_CurrentEvent == 4 and not Jo_Arc_LearnedAboutJo:      
    c_phone "Maybe you could help. I'm looking for a book on riddles, but i have no idea what books are good."      
    b_phone "Have you asked Jo?"      
    c_phone "Jo?" 
    b_phone "The librarian Jo, the invisible person who has a mask on."     # Flag for knowing Jo?
    c_phone "I don't think I've seen them around."
    c_phone "...no pun intended."    
    b_phone "They've always been able to help me find any books I've been looking for."
    b_phone "They are usually there in the evenings, so if you visit the library after class when you're not tutoring you should be able to find them."
    b_phone "I'm sure they can help you with your book problem."    
    b_phone "They also act as the school therapist so if you ever need someone to talk to or to help relieve some stress go talk to Jo."
    c_phone "Thanks, Bahini. "      
    b_phone "No problem! Anything else I can help with?"     # Loop back to original choice without Sanura available
    $Jo_Arc_LearnedAboutJo = True  
    $Sanura_Arc_BahiniQuestioned2 = True    
  return

label lbl_event_bahini_questions_end:
  if bahini_helped:
    c_phone "No, that's all. You've been very helpful, Bahini. Thank you."
    b_phone "Anything for the kids and for my dear substitute!"
  else:
    c_phone "No, not really."
    b_phone "Okay then. Do let me know if there's anything you need help with."

  if questions_cut_short:
    b_phone "Ooh, lunch time! I have to go now."
    b_phone "Talk to you another time!"
    c_phone "See you."
  return

#------------------------------------------------------  RANDOMS

label lbl_event_bahini_random_summary:
  #TODO: Do this as a list that gets added to by the events as they happen.
  $eventcount = len(List_Random_Event_Messages)
  #"[eventcount]"
  #"[List_Random_Event_Messages]"
  if eventcount > 0:
    $messagecount = 0
    python:
      for eventmessage in List_Random_Event_Messages:
        renpy.say(c_phone, eventmessage)
        messagecount = messagecount+1
        if messagecount < eventcount:
          betweentext = renpy.random.choice(["Oh, and...", "And then...", "Also...", "That's not all."])
          renpy.say(c_phone, betweentext)
  else:
    c_phone "No, nothing really happened."
  
  return
  
  #"RANDOM EVENT SUMMARY TEXT"
  #Oversleep "I actually overslept one morning and was late to class. It was a little stressful but the lesson went on as usual."     # Format:
  ## LINE
  #Caragh Forgets Lunch "I forgot my lunch. I was so stressed about it..."     # Oh, and...
  #IF teacher "But then one of the other teachers shared some food with me and the stress went away."     # LINE
  #IF student "And then one of the kids from 5C approached me and shared some of their food with me. It was such a cute scene!"     # And then...
  ## LINE
  #Student Forgets Lunch "One of the students forgot to bring their lunch so I shared some of mine. I'm just glad I brought enough food."     # Also...
 
  #Jo "I was looking for a textbook in the library when I met the librarian. They were rather...unique. I don't think I've ever met a monster who doesn't speak and can only be spotted by a mask they wear."
