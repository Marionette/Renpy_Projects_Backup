init:
  #event flags
  $Craig_Arc_CurrentEvent = 0
  $Craig_Arc_BahiniQuestioned = 0
  $Craig_Arc_HasGlasses = False

#--------------- Craig Events -----------------------
label lbl_event_tutoring_craig:
  #"DEBUG: Craig Relationship score: [Character_Craig.Relationship]"
  #"You talk to Craig."
  #call update_relationship(Character_Craig, 5)

  Caragh "Okay. I'll be tutoring Craig today."

  if Craig_Arc_CurrentEvent == 0:
    #  Craig's Route : Tutoring Event 01
    call lbl_event_craig_problem_tutoring_1 from _call_lbl_event_craig_problem_tutoring_1

  elif Craig_Arc_CurrentEvent == 4:
    call lbl_event_craig_problem_tutoring_5 from _call_lbl_event_craig_problem_tutoring_5

  else:
    #Hints:
    if Craig_Arc_CurrentEvent == 1:
      Caragh "I'm not sure how I can help. I should call his parents when I get a chance."
    if Craig_Arc_CurrentEvent == 2:
      Caragh "Craigs parents weren't able to help, I wonder if Bahini has any ideas."
    if Craig_Arc_CurrentEvent == 3:
      Caragh "I sent those plans to Bahini, I guess we just have to wait and see if it pans out for Craig."
    call lbl_event_craig_problem_tutoring_0 from _call_lbl_event_craig_problem_tutoring_0
  return

label lbl_event_problem_tutoring_end:
  scene bg black with fade
  scene bg classroom empty with fade
  Caragh "It's getting late. I should head home now."
  return

#------------------------------------------------------

label lbl_event_craig_problem_tutoring_0:
  #Generic Tutoring Event when no others are available
  show bg classroom empty
  play music music_quiet
  show  Craig
  Caragh "\"Craig, come in.\""
  Craig "\"Hi, Miss Caragh.\""
  #jump lbl_event_craig_problem_tutoring_0_mid

label lbl_event_craig_problem_tutoring_0_mid:
  #Tutoring starts here if taking place after another event
  Caragh "\"Today, we are going to focus on your weakest subject.\""
  $weakestSubject = Character_Craig.GetWeakestSubject()
  Caragh "\"Which at the moment seems to be [weakestSubject].\""
  Craig "\"Yes, Miss Caragh.\""
  Description "We spend the time we have going over the fundamentals of [weakestSubject]."

  if Craig_Arc_CurrentEvent == 5:
    call update_score_specific(Character_Craig, weakestSubject, 10) from _call_update_score_specific_7
    Description "Craig is really focused today and plows through the questions I had prepared."
    Caragh "Wow, you did really good today."
    show Craig happy
    Craig "Thanks!"
    #jump lbl_event_problem_tutoring_end

  else:
    call update_score_specific(Character_Craig, weakestSubject, 5) from _call_update_score_specific_8
    Description "Craig seems to have picked up a few things during our session."
    #jump lbl_event_problem_tutoring_end

  call lbl_event_problem_tutoring_end from _call_lbl_event_problem_tutoring_end_6 #END SCENE
  return


#------------------------------------------------------

label lbl_event_craig_problem_tutoring_1:
  #  Craig's Route : Tutoring Event 01
  show bg classroom empty
  play music music_quiet
  show  Craig
  Caragh "\"Craig, come in. Take a seat.\""
  Caragh "He nearly scared my head off! I know he's a Basilisk and snakes are generally silent, but he's even quieter than a ghost."
  Craig "\"Hi, Miss Caragh.\""
  Caragh "\"According to your last teacher's notes, you weren't focusing in class.\""
  Caragh "\"What seems to be the major problem?\""
  Craig "\"I...\""
  Craig "\"I don't...\""
  Craig "\"...know...\""
  Caragh "\"Okay, that's fine. That's what tutoring is for. I'm here to help you.\""
  Caragh "\"I have here a little test. Just a few questions that would appear in the exams.\""
  Caragh "\"Please, take your time going through it. We'll discuss about the answers later.\""
  Craig "\"Yes, Miss Caragh.\""
  Description "Craig's hood dips low as he goes through the quiz. Minutes passed and he has yet to write down a single answer. The tail he has been hugging since the beginning of class curls around his arm."
  Caragh "This is obviously going nowhere. Should I stop him though? It'd be bad for his confidence if I interrupt him when I said he can take his time."
  Caragh "On the other hand, I can tell it's going to be futile just letting him take the quiz without guidance."
  Description "As if sensing my thoughts, Craig's head droops even lower as the boy visibly shrinks into himself."
  Caragh "I can't let this go on any longer."
  Caragh "\"I see you're having some difficulties. Would it be okay if we switch things up?\""
  Caragh "\"Instead of letting you go through the test alone, why don't we do it together?\""
  Description "Craig mutely nods."
  Caragh "\"Alright. First question...\""
  Description "We go through the questions quickly. The moment I'm done reading a question, Craig provides an answer without further prompting."
  Caragh "He knows the answers. So why wasn't he putting them down? What's going on?"
  Caragh "Wait. What if...?"
  Caragh "\"I'm feeling a little thirsty. Craig, do you mind reading out the next question while I take a sip of water?\""
  Craig "\"I... Okay.\""
  Craig "\"Number t-ten. Which of the following...is...c- false?\""
  Craig "\"One, a-acrylic... oil...painting is...\""
  Craig "\"I...\""
  Caragh "I knew it."
  Caragh "\"Craig, do you mind looking up for a second?\""
  Description "Craig freezes. His body tenses up as his tail tightens around his arm."
  Craig "\"Miss, I'm s-scared...\""
  Caragh "\"It's okay, Craig. I'm here to help.  Please look up.\""
  Description "Craig's hood slowly raises from the table. Moments pass by. Finally, I am greeted with green eyes. Craig's eyes flicker and dart about the room."
  Caragh "\"Now, Craig, could you please tell me read to me what's on the paper over there?\""
  Description "Craig's head snaps to look at the poster pointed at."
  Craig "\"Medusa and her sisters were the first Gorgons known to humankind but Gorgons as a species go further back. In fact, Gorgons share a common ancestor with Basilisks.\""
  Caragh "\"That's enough. Thank you, Craig. That was very well done. I thought you'd have trouble with some of the words.\""
  Description "Craig's face lights up with a smile as his eyes flickers over to meet mine. A weird sensation runs through my body. A look of horror spreads across Craig's face as my body grows stiff."
  Craig "\"I'm sorry, Miss! I...\""
  Craig "\"I'm sorry!\""
  Description "Craig hurriedly looks down. His eyes hide behind his hood once more. His fingers fidget with the tip of his tail."
  Caragh "\"Craig? It's fine, Craig.\""
  Description "Craig's head snaps up as he audibly gasped. His teary eyes grow wide with shock"
  Craig "\"Miss, you can still talk!\""
  Caragh "\"Yes, I can.\""
  Caragh "\"Craig, could you please put my head down on the desk? I'm afraid my arms aren't going to support me any longer.\""
  Craig "\"Oh, okay!\""
  Description "Craig reaches up and gently holds my head. Then, he lifts it out of my arms and places it on the desk."
  Caragh "\"Ah, much better.\""
  Craig "\"Miss, your body...\""
  Caragh "\"Haha, did you forget what I am, Craig?\""
  Caragh "\"I'm a Dullahan. Paralysis doesn't work that well on me.\""
  Craig "\"Oh. I didn't know. I've never met a Dullahan before.\""
  Caragh "\"And you wouldn't have learned about my race until next year.\""
  Caragh "\"It's fine, Craig.\""
  Caragh "\"Now, is this why you refused to look at me earlier?\""
  Craig "\"I'm sorry...\""
  Caragh "\"No apologies, Craig. After all, you didn't mean to do this me. Did you?\""
  Craig "\"No, Miss! I would never dream of doing that.\""
  Craig "\"I just...\""
  Caragh "\"How long has it been like this, Craig?\""
  Craig "\"A while...\""
  Caragh "\"Does anyone else know?\""
  Craig "\"I'm scared...\""
  Caragh "\"Scared? Craig, paralysis is a normal power for Basilisks.\""
  Craig "\"But if I accidentally paralyze someone in the middle of class, everyone will be afraid of me!\""
  Craig "\"They won't talk to me again and they'll start walking around me. I don't want that to happen.\""
  Caragh "\"And that's why you hide behind the hood and never look up?\""
  Craig "\"Yes, Miss.\""
  Caragh "\"But how are you supposed to look at the board then, Craig? How are you supposed to learn?\""
  Craig "\"I've been trying to study off my text books.\""
  Caragh "\"But, Craig, you can't even read a paper placed on your desk.\""
  Craig "\"Yes, Miss...\""
  Caragh "\"I...\""
  Caragh "\"Is this why you've been doing badly in the exams?\""
  Caragh "\"You're too busy hiding your eyes behind your hood that you can't focus on making sure you can properly read what's in front of you?\""
  Craig "\"Yes, Miss.\""
  Caragh "\"I see...\""
  Caragh "\"Do your parents know?\""
  Craig "\"They're good people! They try their best to help me and they're always there when I need them.\""
  Craig "\"I'm just...\""
  Description "Craig lowers his head once more."
  Caragh "\"It's okay, Craig. I'm here to help, not judge.\""
  Description "Craig's breathing turns heavy. His fingers dig into his tail."
  Caragh "\"Craig? Craig!\""
  Caragh "\"Craig, can you take a deep breath for me?\""
  Description "There's no response from Craig."
  Caragh "\"Craig, listen to me. Follow me.\""
  Caragh "\"Come, breathe in.\""
  Description "Craig's shoulders rise."
  Caragh "\"Breathe out.\""
  Description "His shoulders fall."
  Caragh "\"Breathe in...\""
  Description "Minutes later, Craig's breathing evens out and his grip around his tail loosens. "
  Craig "\"I'm sorry for that, Miss.\""
  Caragh "\"It's okay, Craig. It's perfectly normal.\""
  Caragh "\"Now, Craig, the reason why I asked about your parents is because I want to ask if it's okay for me to talk to your parents about this.\""
  Craig "\"I see.\""
  Caragh "\"So, may I talk to your parents about your unstable powers, Craig?\""
  Craig "\"Yes...\""
  Caragh "\"Thank you, Craig.\""
  Caragh "\"Thank you for trusting me with your secret.\""
  Description "A tiny smile appears on Craig's face."
  Caragh "\"Well, my body may be stuck but I can still tutor you.\""
  Caragh "\"How about we continue our lesson?\""
  Caragh "\"Of course, you'll have to read the questions for me since I can't read the paper right now. Is that okay?\""
  Craig "\"Yes, Miss!\""

  $Craig_Arc_CurrentEvent = 1
  call lbl_event_problem_tutoring_end from _call_lbl_event_problem_tutoring_end_7 #END SCENE
  return

label lbl_event_craig_problem_tutoring_2:
  # "Craig's Route : Talking to Parents (Evening)"
  show bg room
  play music music_bedroom
  show  Caragh
  Caragh "The number for Craig's home is..."
  Caragh "Okay, everything's correct. "
  Caragh "Craig said they'd be free today."
  show Phone    
  play sound sfx_phonecall
  CraigMother "\"Hello? Who's this?\""
  Caragh "\"Hi, is this Craig's house? I'm Caragh, his new teacher.\""
  CraigMother "\"Oh, Miss Caragh! We've heard all about you from Craig.\""
  CraigMother "\"Thank you so much for your patience with Craig's powers.\""
  CraigMother "\"We're so sorry about what happened during the tutoring session.\""
  Caragh "\"Don't worry about it.\""
  Caragh "\"I see Craig has told you what's happened the other day. That's good to hear. Not a lot of the kids I've taught tell their parents what happened in school.\""
  CraigMother "\"Oh, we know! Craig's such a blessing. We've known that since the day the social worker introduced him to us.\""
  CraigMother "\"He's the sun of our lives.\""
  Caragh "\"Social worker?\""
  CraigMother "\"We adopted Craig when he was a little baby.\""
  CraigMother "\"He was so cute back then.\""
  Caragh "\"Oh, I see. Does that mean...?\""
  CraigMother "\"Yes. Unfortunately, as Lamias, neither of us have any experience with paralysis or petrification powers.\""
  Caragh "\"Thank you for sharing this with me. I appreciate the trust.\""
  CraigMother "\"Oh, it's no big deal.\""
  CraigMother "\"We appreciate what you've done for Craig. If you have any ideas on how to help Craig, please contact us anytime.\""
  Caragh "\"I will. Thank you for taking the time out of your day to talk to me.\""
  CraigMother "\"Thank you, Miss Caragh.\""
  play sound sfx_phonecallend
  hide Phone    
  Caragh "Well, that's a bust."
  Caragh "Still, that was such a pleasant experience. None of my talks with parents had ever gone as smoothly or as quickly."
  $Craig_Arc_CurrentEvent = 2
  return #END SCENE

label lbl_event_craig_problem_tutoring_3:
  # "Mini-Scene "

  #Flag/Outcome "If talked to Bahini before"
  #nvl_narrator "Bahini added Caragh to the group"
  #show  Phone
  #play sound  Email/Phone
  b_phone "Hey, Kara!"
  b_phone "I just had a chat with Ambrose, a Cockatrice I know."
  b_phone "He said all monsters with paralysis or petrification powers go through an unstable period during puberty. The more powerful they are, the longer the period is. "
  b_phone "He's forwarded me a link to some spectacles his kind uses."
  b_phone "\[Bahini has shared a link with you: Shield Specs\]"
  b_phone "Hopefully, these will help Craig."
  c_phone "Thank you, Bahini. Craig will appreciate these."
  $Craig_Arc_CurrentEvent = 3
  return #END SCENE

label lbl_event_craig_problem_tutoring_4:
  # "Craig's Route : Spectacles (During Class)"
  show bg classroom morning
  play music  music_5c
  $Craig_Arc_HasGlasses = True
  show  Craig  at left
  Description "I step into the classroom to find Sanura standing by Craig's desk, happily chattering away."
  show  Sanura at right
  Sanura "\"Whoa, Craig! Your eyes are so pretty!\""
  Craig "\"T-Thanks...\""
  Sanura "\"What kind of specs are these, Craig? What do they do? Can I try them on? Can I? Can I?\""
  Craig "\"I-I...\""
  Description "Sanura's arm reaches out to grab Craig's new spectacles."
  Description "Craig visibly shrinks back, his tail wraps tightly around his arm. It's obvious that Craig isn't comfortable with what's going on."
  Caragh "I'd better stop this before something bad happens."
  Caragh "\"Kids, back to your seats.\""
  Description "Sanura's hand stops in the air. With a disappointed pout, she slinks back to her seat."
  hide Sanura
  Description "Craig lets out a relieved sigh and gives me a grateful smile."
  hide Craig
  Caragh "Craig might be able to concentrate on listening in class now but there's still enough going on that I don't think Craig will be able to properly focus on the upcoming exams."
  Caragh "If I hadn't stepped in, who knows what would've happened."
  Caragh "Craig needs to work on his confidence but maybe a more controlled environment would be a better first step."
  Caragh "Now, who would be good candidates?"
  $Craig_Arc_CurrentEvent = 4
  return #END SCENE

label lbl_event_craig_problem_tutoring_5:
  # "Craig's Route : Introduce friendlies idea (Tutoring Event 02)"
  show bg classroom empty
  play music music_quiet
  show  Craig 
  Craig "\"Hello, Miss Caragh.\""
  Caragh "\"Hey, Craig.\""
  Caragh "\"How are the new spectacles? I've noticed you're more attentive in class now.\""
  Craig "\"They're wonderful. Thank you so much for telling my parents about them.\""
  Caragh "\"Well, you've had some time to get used to them. Now, how about we see how you'll do in an exam.\""
  Craig "\"Okay.\""
  Caragh "Craig seems to be doing well. He's speeding through the questions."
  Caragh "Now, how do I build up his confidence? Who will be good for him?"
  Caragh "After what happened in class, it shouldn't be Sanura. Even if I think there's potential, it's a little too early for Craig and Sanura to interact alone with minimal supervision."
  Caragh "It will be good for him to be grouped up with someone {b}friendly{/b} or someone who's {b}talkative but insists on having the attention of their listener{/b}."
  Caragh "I know there are a few kids who fit the bill here, but who?"

  #-----------------
  #Choice "Choose 2 characters from the list of students." 
  call screen group_planning("Craig")     
  #call lbl_event_func_group_picker
  #$Craig_Cram_Partner_01 = _return[0]
  #$Craig_Cram_Partner_02 = _return[1]
  
  $Craig_Cram_Partner_Correct = False
  if Craig_Cram_Partner_01 in ["Roark", "Sophia"] and Craig_Cram_Partner_02 in ["Roark", "Sophia"]:
      $Craig_Cram_Partner_Correct = True
  #-----------------

  Craig "\"Miss Caragh, I'm done.\""
  Caragh "\"Let me see...\""
  Caragh "\"Good job! You've improved a lot since our first lesson.\""
  Description "Craig beams happily as his tail begins tapping."
  Caragh "\"Well, Craig, I think we're done with our tutoring sessions.\""
  Description "Craig's tail stops tapping. His shoulders droop."
  Craig "\"Oh...\""
  Caragh "\"You've come quite a long way. If you want to continue our sessions though, I'll be more than happy to arrange another.\""
  Description "Craig's eyes lit up as his tail begins tapping once more."
  Craig "\"Really?\""
  Caragh "\"Yes. My door is open to you at all times.\""
  Craig "\"Thank you, Miss Caragh!\""
  # Trigger flag for boost to Craig
  Craig "\"...Miss Caragh? I, um, I wanted to...\""
  Craig "\"I wanted to say thank you for helping me with my studies, my eyes and stuff.\""
  play music music_good_vibes
  show cg craig_rock
  Craig "\"Here, Miss Caragh. I got this for you.\""
  Description "Craigh hands over a rock embedded with glimmering speckles of a rainbow."
  Caragh "\"It's beautiful. Thank you, Craig.\""
  Description "Craig wraps his arms around me. I can't help but smile at the sight."
  Caragh "It's good to be able to see his smile. It's so warm. Makes the stress melt away."
  $Craig_Arc_CurrentEvent = 5
  call lbl_event_problem_tutoring_end from _call_lbl_event_problem_tutoring_end_8 #END SCENE
  return
  #" END OF CRAIG'S ROUTE "
