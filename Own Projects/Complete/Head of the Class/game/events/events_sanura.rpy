init:
  #event flags
  $Sanura_Arc_CurrentEvent = 0
  $Sanura_Arc_RiddleBookFound = False
  $Sanura_Arc_Distracted_1 = False
  $Sanura_Arc_MorningBreak = False
#--------------- Sanura Events ----------------------
label lbl_event_tutoring_sanura:
  #"DEBUG: Sanura Relationship score: [Character_Sanura.Relationship]"
  #"You talk to Sanura."
  #call update_relationship(Character_Sanura, 5)

  Caragh "Okay. I'll be tutoring Sanura today."


  if Sanura_Arc_CurrentEvent == 0:
    # "Sanura's Route: Tutoring Event 01"
    call lbl_event_sanura_problem_tutoring_1 from _call_lbl_event_sanura_problem_tutoring_1

  elif Sanura_Arc_CurrentEvent == 6 and Sanura_Arc_RiddleBookFound:
    # "Sanura's Route: Give Book (Tutoring Event 02)"
    call lbl_event_sanura_problem_tutoring_5 from _call_lbl_event_sanura_problem_tutoring_5

  else:
    #Hints:
    #1 - Before class
    if Sanura_Arc_CurrentEvent == 1:
      Caragh "I'm just getting to know Sanura. I'll keep an eye on her and see how she is doing."
    #2 - after calss
    if Sanura_Arc_CurrentEvent == 2:
      Caragh "I'm just getting to know Sanura. I'll keep an eye on her and see how she is doing."
    #3 - call parents
    if Sanura_Arc_CurrentEvent == 3:
      Caragh "Sanuras riddles are getting out of hand. I need to talk to her parents."
    #4 - before class
    if Sanura_Arc_CurrentEvent == 4:
      Caragh "Sanura is still absorbed in riddles, but its different somehow. I'll keep an eye on her for now."
    #5 - after class
    if Sanura_Arc_CurrentEvent == 6:
      Caragh "Oh right, I was supposed to find a riddle book for Sanura."
      if Jo_Arc_LearnedAboutJo:
        Caragh "Maybe I check out the Library and see if Jo has any recommendations?"
      else:
        Caragh "Maybe Bahini has some ideas?"
    #7  -give book
    call lbl_event_sanura_problem_tutoring_0 from _call_lbl_event_sanura_problem_tutoring_0

  return
  

#------------------------------------------------------

label lbl_event_sanura_problem_tutoring_0:
  #Generic Tutoring Event when no others are available
  show bg classroom empty
  play music music_quiet
  show  Sanura
  Sanura "\"Miss Caragh! Hi!\""
  Description "Sanura walks into the room with a bounce in her steps."
  Caragh "\"Sanura, hello. Come, sit.\""
  #jump lbl_event_sanura_problem_tutoring_0_mid

label lbl_event_sanura_problem_tutoring_0_mid:
  #Tutoring starts here if taking place after another event
  Caragh"Today we are going to focus on your weakest subject."
  $weakestSubject = Character_Sanura.GetWeakestSubject()
  Caragh"Which at the moment seems to be [weakestSubject]."
  Sanura "\"Yes, Miss Caragh.\""
  Description "We spend the time we have going over the fundamentals of [weakestSubject]."
  if Sanura_Arc_CurrentEvent == 9:
    call update_score_specific(Character_Sanura, weakestSubject, 10) from _call_update_score_specific
    Description "Sanura is really focused today and plows through the questions I had prepared."
    Caragh "Wow, you did really good today."
    show Sanura happy
    Sanura "Thanks!"
    Description "Sanura spends the remaining time practicing her riddles on me before she has to leave."
    #jump lbl_event_problem_tutoring_end
  else:
    call update_score_specific(Character_Sanura, weakestSubject, 5) from _call_update_score_specific_1
    Description "Sanura seems to have picked up a few things during the tutoring session."
    #jump lbl_event_problem_tutoring_end

  call lbl_event_problem_tutoring_end from _call_lbl_event_problem_tutoring_end
  return

#------------------------------------------------------
# "Sanura's Route: Tutoring Event 01"
label lbl_event_sanura_problem_tutoring_1:
  show bg classroom empty
  play music music_quiet
  show  Sanura
  Sanura "\"Miss Caragh! Hi!\""
  Description "Sanura walks into the room with a bounce in her steps."
  Caragh "\"Sanura, hello. Come, sit.\""
  Description "The girl sits on the chair. In her excitement, her ears swivel back and forth while her tail swishes from left to right."
  Caragh "\"Now, according to your last teacher's notes, your weakest subject is Literacy.\""
  Caragh "\"Which topic do you feel good about and which are you uncertain of?\""
  Sanura "\"I...don't know.\""
  Description "Sanura's ears swivel back and her tail droops low."
  Caragh "From what I've read on cats, those aren't good signs. Sanura might be afraid or nervous. If it's the second, that's understandable. If it's the first..."     #
  Caragh "\"That's okay. It takes a lot of practice and skill to know those. I had a quiz prepared just in case. How about you go through it now?\""
  Sanura "\"Okay!\""
  Description "Sanura immediately starts working through the quiz. Occassionally, she'd stop and look up as if trying to recall something but she'll always go back to her paper within a minute."
  Caragh "She's doing well. She's not stuck and she's thinking hard."
  Caragh "What would be the reasons for her bad grade then?"
  Sanura "\"I'm done, Miss Caragh!\""
  Caragh "\"Thank you, Sanura. Give me a moment while I look through your answers.\""
  Caragh "..."
  Caragh "Ah. I see."
  Caragh "Everything here is written in riddles. I don't mind students scribbling and doodling on their papers but..."
  Caragh "The answers are all wrong and these riddles aren't...the best."
  Caragh "\"I see...\""
  Caragh "\"Shall we start going through your answers, Sanura?\""
  Sanura "\"What? Oh, no. Did I get a lot of them wrong? I'm so sorry.\""
  Caragh "\"There's no need to apologize, Sanura. A wrong answer is a chance to learn more.\""
  Caragh "\"It's why I'm here - to help you.\""
  Description "We begin going through the answers. Sanura's tail droops on the first answer and starts flicking nervously by the third. By the time they had gone through all of Sanura's questions, she is close to tears while her tail is thumping hard against her chair."
  Sanura "\"I don't get it. I worked so hard on this...\""
  Sanura "\"Why are my riddles so bad? I'm such a bad sphinx.\""
  Caragh "That's your focus? "
  Caragh "\"Sanura, what do you think of your answers?\""
  Sanura "\"Hm? They're okay, I guess. I promise I'll do better!\""
  Caragh "\"I understand your love for riddles, Sanura, but that doesn't mean you can ignore your studies.\""
  Caragh "\"Do you think you can put riddles aside in class and in our tutoring sessions?\""
  Sanura "\"But...\""
  Caragh "\"Great riddles come from great minds and great minds are great because they know a lot.\""
  Sanura "\"Alright...\""
  Caragh "\"Thank you, Sanura. I appreciate it.\""
  Description "The tutoring session soon comes to an end."     # can replace with transition and/or tutoring session game text (+10 scores etc)
  Caragh "\"See you, Sanura.\""
  hide Sanura
  Caragh "Well, some wins and some losses. On one hand, she did concentrate for most of today. On the other hand, I could see her mumbling about riddles when left to work on the questions alone. "
  Caragh "It's a habit she has to change. Maybe she just needs time."
  Caragh "Let's wait and see."
  $Sanura_Arc_Distracted_1 = True
  $Sanura_Arc_CurrentEvent = 1
  call lbl_event_problem_tutoring_end from _call_lbl_event_problem_tutoring_end_1 #END SCENE
  return

label lbl_event_sanura_problem_tutoring_2a:
  # "Sanura's Route: Observation before Bahini Text (After Class Additional Text - Morning Class)"
  show bg classroom morning
  play music  music_5c
  Caragh "Sanura hasn't been focusing in class today. I'll just give her a gentle reminder. Hopefully things get better in the afternoon."
  show  Sanura
  Caragh "\"Sanura, could I talk to you for a minute?\""
  Sanura "\"What is it, Miss Caragh?\""
  Caragh "\"Do you remember what we talked about during our last tutoring session?\""
  Sanura "\"Put riddling aside when in class. Oh, right...\""
  Sanura "\"I'm sorry, Miss. I won't do it again.\""
  Caragh "\"Thank you. Now, go enjoy lunch.\""
  Sanura "\"You too, Miss!\""
  $Sanura_Arc_CurrentEvent = 2
  #hideSanura
  return

label lbl_event_sanura_problem_tutoring_2b:
  #" Afternoon Class "
  show bg classroom afternoon
  play music music_5c
  Caragh "Sanura's still mumbling about riddles. Oh, what do I do with this kid?"
  Caragh "Nothing in the books ever mentioned this. She's not old enough for me to be stricter with her but she's also not young enough for simple bluffs and encouragements to work."
  Caragh "If only there's someone who could help..."
  $Sanura_Arc_CurrentEvent = 3
  return

label lbl_event_sanura_problem_tutoring_3:
  # "Sanura's Route: Talk to Parents (Evening)"
  show bg room
  play music music_bedroom
  Caragh "This is it. The number for Sanura's mother."
  show Phone
  play sound sfx_phonecall
  SanuraMother "\"Hello! I am always hungry and will die if not fed, but whatever I touch will soon turn red. What am I?\""
  Caragh "A riddle as your greeting? What?"
  Caragh "\"Fire?\""
  SanuraMother "\"Ding-ding-ding! Correct!\""
  SanuraMother "\"Now, how can I help you?\""
  Caragh "\"Hi, this is Caragh. I'm Sanura's new teacher.\""
  SanuraMother "\"Oh, yes! The Dullahan. I've heard about you.\""
  SanuraMother "\"Well, you've called me so that must mean it's about Sanura. What is it? Is she being bullied? Did she hurt herself?\""
  Caragh "\"No, nothing of the kind.\""
  Caragh "\"It's about Sanura's focus during classes. She's always spacing out, thinking of new riddles.\""
  SanuraMother "\"Thinking of new riddles? Oh, that's amazing! She's improving so much.\""
  Caragh "\"Normally, this wouldn't be a major concern. However, she answered the quiz I gave her in riddles. There were nothing but riddles written on her paper.\""
  SanuraMother "\"That's so smart of her. She can improvise!\""
  Caragh "\"Unfortunately, I couldn't make any sense out of her answers for a while. When I finally did, all of the answers were wrong.\""
  SanuraMother "\"Oh dear, that's bad. Could you read me one of her answers?\""
  Caragh "\"They have ten fingers. They also are a pair and they aren't alive.\""
  SanuraMother "\"Oh, I know that one. They're gloves!\""
  SanuraMother "\"But that's not how the riddle is supposed to go. It should be 'eight' fingers and 'have a pair of thumbs'.\""
  SanuraMother "\"It's still a good effort.\""
  Caragh "\"Sanura spends her whole day thinking about these riddles. She barely focuses on her studies.\""
  SanuraMother "\"Don't worry, Miss Caragh. I'll give her a stern talk about this.\""
  Caragh "\"I appreciate it but that's not the purpose of my call.\""
  Caragh "\"During my talks with Sanura, I heard something rather concerning.\""
  Caragh "\"When we went through the quiz I gave her, Sanura said, and I quote, 'Why are my riddles so bad? I'm such a bad sphinx'.\""
  Caragh "\"Not only that, she stated she was 'slow' when I asked her about her grades.\""
  SanuraMother "\"Oh...\""
  Caragh "\"Sanura adores you. When I talked to her, she said she didn't want to disappoint you.\""
  Caragh "\"That's not something you hear often from kids at Sanura's age.\""
  Caragh "At least, that's what teenagers are like. The book said it's the same with younger kids. I hope it's right."
  Caragh "\"Ma'am, I've heard of your reputation from my colleagues. You are a great riddler and Sanura clearly wants to be like you.\""
  Caragh "\"Do you think it's possible that she's under a little too much pressure from trying to emulate you?\""
  Caragh "It's just a hunch but Sanura keeps mentioning how much she loves riddles and she keeps expecting herself to spout out great riddles on the spot."
  SanuraMother "\"No way. I've always told Sanura she can just be who she is and that's fine.\""
  Caragh "\"Every kid is unique. Everyone has their own strengths. However, judging by how upset she was over being a 'bad sphinx',  I think it's safe to say Sanura might be facing a few challenges on being who she is.\""
  SanuraMother "\"I see.\""
  SanuraMother "\"I'll talk to Sanura.\""
  SanuraMother "\"Have a good evening.\""
  play sound sfx_phonecallend
  hide Phone    
  Caragh "That ended a little too abruptly for my liking."
  Caragh "I'll check in on Sanura tomorrow."
  $Sanura_Arc_Distracted_1 = False
  $Sanura_Arc_CurrentEvent = 4
  return

label lbl_event_sanura_problem_tutoring_4a:
  #" The Next Morning (Before Class) "
  show bg room
  play music music_bedroom
  Caragh "Hm? A message from Sanura's mom."
  sm_phone "Hi, Miss Caragh. Thank you for calling me yesterday. Sanura and I had a little talk. Emotions ran high and Sanura didn't get to sleep until late last night. She'll be missing out on this morning's class but will be there after lunch. "
  Caragh "It'll be good for Sanura to take a break."
  $Sanura_Arc_CurrentEvent = 5
  $Sanura_Arc_MorningBreak = True
  call update_mood_specific(Character_Sanura, 10) from _call_update_mood_specific
  return

label lbl_event_sanura_problem_tutoring_4b:
  #" After Lunch-Before Afternoon Class "
  show bg classroom afternoon
  play sound sfx_schoolbell
  show  Sanura
  Description "Just as the bell rings, Sanura bounces into the classroom. Immediately, she dashes straight for me and gives me a big hug."
  Sanura "\"Miss Caragh, I love you!\""
  Caragh "\"What happened, Sanura?\""
  Caragh "Her eyes don't look puffy. Maybe the talk did go well."
  Sanura "\"I had the bestest talk ever with my mom last night. She showed me our family book of riddles and they were so wonderful! I know exactly how to improve now. I just have to read more!\""
  Sanura "\"I've always thought Mommy made those riddles up herself.\""
  Caragh "At least she has a goal to focus on?"
  Caragh "\"That sounds like a great plan, Sanura.\""
  Sanura "\"Yes, but I do need...\""
  Sanura "\"Miss Caragh, could you help me find a few books on riddles?\""
  Sanura "\"I showed Mommy the ones I've found and she said they weren't the best.\""
  Sanura "\"I don't want to bother her any more than I already have...\""
  Caragh "\"I'll do my best to find you the best book there is on riddles.\""
  Caragh "We have a library. Maybe there'll be something there."
  $Sanura_Arc_MorningBreak = False
  $Sanura_Arc_CurrentEvent = 6
  return #END SCENE

label lbl_event_sanura_problem_tutoring_5:
  # "Sanura's Route: Give Book (Tutoring Event 02)"
  show bg classroom empty
  play music music_quiet
  show  Sanura
  Sanura "\"Hi, Miss Caragh! What are we doing today? What are we studying? Can I ask you a riddle?\""
  Caragh "\"We're having a little quiz today. If over half of your answers are correct, you may ask me a riddle.\""
  Sanura "\"I'll do my best!\""
  Description "Sanura focuses on the piece of paper before her. A few minutes later, she's done. "
  Caragh "Yes, yes, yes, no, yes, no..."
  Caragh "\"Congratulations, Sanura. Most of your answers are correct.\""
  Caragh "\"As promised, you may now tell me your riddle, but-\""
  Sanura "\"Ooh, ooh! I have just the perfect riddle.\""
  Caragh "\"Haha, now hold on. I'm not finished yet.\""
  Sanura "\"Oops!\""
  Caragh "\"Now, you may tell me your riddle but I have something for you first.\""
  Caragh "\"Here's the book you asked me for.\""
  Sanura "\"The Whats, Whys and Hows of Riddles! Miss Caragh, I've heard all about this book! It's written by last year's International Master Riddler of Monsters! I've been looking everywhere for it!\""
  Description "Sanura starts flipping through the pages. Her ears quivers with excitement. Her gaze is glued to the words. However, her brows slowly drop into a frown."
  Caragh "\"Oh? You know of the International Master Riddler of Monsters?\""
  Caragh "Who's that? What's that? I only bought the book Jo recommended. Thank goodness this school has such an amazing librarian. I don't know how I'd have found this book. I've looked everywhere for it."
  Sanura "\"Of course! The International Monster Riddling Tournament is the one event I'll never miss out on.\""
  Sanura "\"There was a year when the tournament was being held on the other side of the globe. I stayed up all night to watch it.\""
  Caragh "\"Well, I'm glad you like the book.\""
  Sanura "\"I love it! Thank you, Miss Caragh!\""
  Caragh "\"Well? Give it a try. You still haven't asked me any riddles yet.\""
  Sanura "\"Hm...okay! I've found one.\""
  Sanura "\"W-What room avoids ghosts? Wait, that's not it. Let me try again.\""
  Sanura "\"What room do ghosts avoid?\""
  Caragh "\"Oh, that's a good one. I'm guessing...\""
  Caragh "Think harder. Think harder. Don't let her know you've already read some of the book. And...go!"
  Caragh "\"A living room?\""
  Sanura "\"Yes! Isn't it a great riddle?\""
  Caragh "\"Yes, it is. Great job, Sanura.\""
  Caragh "\"Alright, our time is up for today.\""
  Sanura "\"Thank you so much, Miss Caragh! See you around!\""
  hide Sanura
  Caragh "She stuttered and messed up the riddle. However, she just received her book. Maybe she'll be more confident if she spends a little more time with it."
  $Sanura_Arc_CurrentEvent = 7
  call lbl_event_problem_tutoring_end from _call_lbl_event_problem_tutoring_end_2 #END SCENE
  return

label lbl_event_sanura_problem_tutoring_6:
  # "Sanura's Route: Sanura's Practice (Lunch)"
  show bg classroom morning
  play music music_5c
  Caragh "\"And that's the bell. Thank you, everyone. See you after lunch.\""
  show  Sanura
  Description "Sanura stands up from her desk, head buried in her book of riddles. Her brows are locked in a deep frown as she mouths along to the riddles."
  Caragh "\"Sanura, everything alright?\""
  Sanura "\"Hm?\""
  Description "Startled, her head snaps up to look at me."
  Sanura "\"Oh, I'm fine. I'm just trying to make sense of these riddles. I want to know how to come up with riddles as amazing as these.\""
  Caragh "\"Remember to take a break once in a while.\""
  Sanura "\"Will do...\""
  hide Sanura
  Description "Sanura's voice slowly drifts off as she turns her attention back to the book. She walks out of the door. She never looked up, not even when she banged her shoulder against the door on the way out."
  Caragh "I'm still worried. I didn't think Sanura would have so much trouble with the book. Sanura's mother didn't even know Sanura loves coming up with new riddles, and Bahini and the other teachers said Sanura has been doing that for years. "
  Caragh "That means Sanura has no one to talk to about riddles. It doesn't matter much in the future but one day, she'll be distracted again in class. It won't be as easy for her to catch up on what she's missed then. What else can I do?"
  Caragh "I've talked to Sanura's mother. Nothing much has come out of it. But maybe..."
  Caragh "Maybe she'll find the book easier if she doesn't have to work through the riddles by herself? What if she has a partner or two to bounce ideas off of?"
  Caragh "Who would be a good partner for her though? There is the cram session. If I put her in a group with some other {b}students with similar interests in comedy or humor{/b}, she might build some friendships that'll help her with her riddles."

  #-----------------
  #Choice "Choose 2 characters from the list of students."      
  call screen group_planning("Sanura")     
  #call lbl_event_func_group_picker from _call_lbl_event_func_group_picker
  #$Sanura_Cram_Partner_01 = _return[0]
  #$Sanura_Cram_Partner_02 = _return[1]
  
  $Sanura_Cram_Partner_Correct = False
  if Sanura_Cram_Partner_01 in ["Dougal", "McCoy"] and Sanura_Cram_Partner_02 in ["Dougal", "McCoy"]:
      $Sanura_Cram_Partner_Correct = True
  #-----------------    

  Caragh "They were classmates before but I don't think they interacted much. I hope Sanura gets along well with them. "
  $Sanura_Arc_CurrentEvent = 8
  return #END SCENE

label lbl_event_sanura_problem_tutoring_7:
  # "Sanura's Route: Encouragement (After Class/ Doesn't take up time)"
  show bg classroom empty
  play music music_quiet
  show  Sanura
  Caragh "\"Sanura, could I talk to you for a second?\""
  Sanura "\"Sure thing, Miss Caragh. What is it?\""
  Caragh "\"How has the book been?\""
  Caragh "\"The last time I saw you with it, you were frowning hard. I haven't seen it for a while.\""
  Caragh "\"Is anything the matter?\""
  Sanura "\"I...I'm...\""
  play music music_good_vibes
  Description "Suddenly, Sanura bounces around my desk to wrap her arms around me."
  Sanura "\"Thank you, Miss Caragh. Thank you for the book. Thank you for listening to my riddle.\""
  show cg sanura_pat
  # Trigger flag for boost to Sanura
  Description "With a little juggling, I'm able to free a hand to pet Sanura on the head. The girl then backs away to smile up at me."
  Caragh "\"No need to thank me, Sanura.\""
  Sanura "\"No, I... Thank you for saying I did well back then. It's the first time anyone other than my mother told me I've did a good job even if I messed the riddle up.\""
  Sanura "\"Thank you for...for asking if I need help, even though I'm a Sphinx and should know how to read out riddles immediately.\""
  Sanura "\"Thank you.\""
  $Sanura_Arc_CurrentEvent = 9
  return #END SCENE  # The last step is in cram session
