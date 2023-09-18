label lbl_chapter6:
  #"A6.0"
  #TODO [FINAL








  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"
  #(Continuation of 5.9)
  if (currentPath == "A"):
    call lbl_PathA_6_0_1 from _call_lbl_PathA_6_0_1
  if (currentPath == "B"):
    call lbl_PathB_6_0_1 from _call_lbl_PathB_6_0_1_1 
    call lbl_PathB_6_0_o from _call_lbl_PathB_6_0_o_1 
    call lbl_PathB_6_0_2 from _call_lbl_PathB_6_0_2_1 
  if (currentPath == "C"):
    call lbl_PathC_6_0_1 from _call_lbl_PathC_6_0_1_1 
    call lbl_PathC_6_0_o from _call_lbl_PathC_6_0_o_1 
    call lbl_PathC_6_0_2 from _call_lbl_PathC_6_0_2_1  

  #(Continued in A6.1)
  #"A6.1"
  #TODO [FINAL








  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"
  #(Continuation of 6.0)
  if (currentPath == "A"):
    call lbl_PathA_6_1 from _call_lbl_PathA_6_1_1
  if (currentPath == "B"):
    call lbl_PathB_6_1 from _call_lbl_PathB_6_1_1
  if (currentPath == "C"):
    call lbl_PathC_6_1 from _call_lbl_PathC_6_1_1
  #(Continued in A6.2)
  #"A6.2"
  #TODO [FINAL








  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"
  #(Continuation of 6.1)
  if (currentPath == "A"):
    call lbl_PathA_6_2 from _call_lbl_PathA_6_2_1
  if (currentPath == "B"):
    call lbl_PathB_6_2 from _call_lbl_PathB_6_2_1
  if (currentPath == "C"):
    call lbl_PathC_6_2 from _call_lbl_PathC_6_2_1
  #(Continued in 6.3)
  #"A6.3"
  #TODO [FINAL








  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"
  #(Continuation of 6.2)
  if (currentPath == "A"):
    call lbl_PathA_6_3 from _call_lbl_PathA_6_3_1
  if (currentPath == "B"):
    call lbl_PathB_6_3 from _call_lbl_PathB_6_3_1
  if (currentPath == "C"):
    call lbl_PathC_6_3 from _call_lbl_PathC_6_3_1
  #(Continued in A6.4)
  #"A6.4"
  #TODO [FINAL








  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"
  #(Continuation of 6.3)
  if (currentPath == "A"):
    call lbl_PathA_6_4 from _call_lbl_PathA_6_4_1
  if (currentPath == "B"):
    call lbl_PathB_6_4 from _call_lbl_PathB_6_4_1
  if (currentPath == "C"):
    call lbl_PathC_6_4 from _call_lbl_PathC_6_4_1
  #(Continued in 6.5)
  #"A6.5"
  #TODO [FINAL








  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"
  #(Continuation of 6.4)
  if (currentPath == "A"):
    call lbl_PathA_6_5 from _call_lbl_PathA_6_5_1
  if (currentPath == "B"):
    call lbl_PathB_6_5 from _call_lbl_PathB_6_5_1
  if (currentPath == "C"):
    call lbl_PathC_6_5 from _call_lbl_PathC_6_5_1
  #(Continued in A6.6)
  #"A6.6"
  #TODO [FINAL








  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"
  #(Continuation of 6.5)
  if (currentPath == "A"):
    call lbl_PathA_6_6 from _call_lbl_PathA_6_6_1
  if (currentPath == "B"):
    call lbl_PathB_6_6 from _call_lbl_PathB_6_6_1
  if (currentPath == "C"):
    call lbl_PathC_6_6 from _call_lbl_PathC_6_6
  #"A6.7"
  #TODO [FINAL








  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"
  scene bg black
  #TODO [fade from black
  $ renpy.transition(slow_dissolve, layer="master")

  play music music_SoT
  scene cg forest25
  #TODO [walking animations please #(except for the wagon)
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita content:
    yalign 1.0
    xalign 0.6
  show kreita content at walkBounce
  show wagon#; #(in front of Kreita)
  show merona t serious behind wagon:
    yalign 1.0
    xalign 0.25#; left
  show merona t serious at walkBounce
  mi "I never realized how funky fish could smell."

  show merona t nervous
  mi "They may be buried under soil, but their odor still sneaks out to hover around our noses. When you near our makeshift garden, it's almost like the stench is attacking you."

  show merona t sadSmile
  mi "Poor Kreita. She doesn't seem too troubled by it, although she's the closest one. "

  show merona t serious
  mi "Perhaps she's sniffed even worse."

  show kreita neutral
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t neutral OM behind wagon:
    yalign 1.0
    xalign 0.8#; right from Kreita
  show duran t neutral OM at walkBounce
  dt "Hey... do you think we could find an actual rest stop soon?"

  show duran t sad OM
  dt "We've been walking for almost three days straight and simply plopping down at a random place by the time night falls. Jeez, you guys still wanted to walk even when it got dark!"

  show merona t sadSmile
  show kreita grin
  show duran t worried OM
  dt "There are minors here that you're liable for... And traveling at night time isn't a wise choice for their safety..."

  show merona t content
  show duran t worried
  "I scoffed, shaking my head."

  show merona t content OM
  show duran t annoyed
  mk "Duran, we have to travel as far as we can. You agreed to be our human oil lamp two days ago! As long as we have some kind of light, we're fine."

  show merona t sadSmile
  show kreita sceptical
  show duran t annoyed OM
  dt "No, we're not exactly fine since having a fire in the evening attracts wild animals. I'm trying to look out for both of us, okay? We're too young to die."

  play music music_Travel_Light
  show merona t content
  show kreita sceptical OM
  show duran t surprised
  kh "Actually, wild animals tend to avoid fires unless they're ravenous or curious. Most stay away. The only animal that would come is most likely another human."

  show merona t grin
  show kreita laugh
  show duran t worried
  kh "Besides, it doesn't matter what we do. *laugh* They're all out to get us anyways!"

  show merona t content
  show kreita content
  show duran t surprised
  $ renpy.transition(slow_dissolve, layer="master")
  show rett smirk behind duran:
    yalign 1.0
    xalign 1.05#; right from Duran
  show rett smirk at walkBounce
  "Rett lightly thumped Duran's head."

  show duran t annoyed
  show rett smirk OM
  rt "As much as I appreciate your lack of concern for everyone else, what Merona said is true. Besides, we're getting at least six to seven hours of sleep, right? That's doable."

  show duran t sad OM
  show rett smirk
  dt "*sigh* I'm a growing boy. I need more sleep so that I can grow taller than all of you, but looks like that isn't happening."

  show merona t sadSmile
  show duran t sad
  mi "Duran, there are things you choose to say that aren't necessary-this is one of those things."

  show merona t content
  show kreita content OM
  show duran t tired
  show rett content
  kh "I'm sure that we'll find a spot sooner or later. Three days has been the max amount of time we've spent traveling without stopping at a proper place. Wait just a little longer."

  play music music_recollections
  show kreita content
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan neutral OM behind wagon:
    yalign 1.0
    xalign 0.05#; left from Merona
  show lexan neutral OM at walkBounce
  ln "We do need to find it as soon as possible because of what's on our plate. A thorough check up for everything we've done should take place."

  show merona t sadSmile
  #TODO [fade out Lexan please~ #(except for C path#; please show lexan content there)
  $ renpy.transition(slow_dissolve, layer="master")
  if currentPath == "C":
    show lexan content
  if currentPath != "C":
    hide lexan
  mi "At least the fish is definitely working its magic."

  #(Continued in 6.8)
  #"A6.8"
  #TODO [FINAL








  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue. Any sections that also appear in the other paths will be pink."
  #"-----------------------------------------------------------"
  #(Continuation of 6.7)
label lbl_chapter6_8_optional:
  if (currentPath == "A"):
    pass
  if (currentPath == "B"):
    pass
  if (currentPath == "C"):
    jump lbl_chapter6_8_optionalEnd
    
  #play music music_recollections #(from before)
  show cg forest25 #(from before)
  #(Positions as in last chapter)
  show kreita content
  show wagon
  show merona t content OM
  show duran t neutral
  show rett content
  mk "Well, the yander is growing up pretty quickly. I think it should be fully grown in another two to three days."

  show kreita neutral
  show merona t determined
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria serious behind wagon:
    yalign 1.0
    xalign 0.0#; left from Merona
  show cimaria serious OM at walkBounce
  ck "If that's the case, we should definitely make a pit stop by then. Yander does not have a long lifespan once it has finished developing, so we need to utilize it as much as we can with it."

  show cimaria serious
  "Cimaria tapped her fingers on her chin."

  play music music_River_Meditation
  show kreita worried
  show merona t nervous
  show duran t worried
  show cimaria neutral OM
  show rett surprised
  ck "Perhaps... I could do the operation at that time as well."

  show cimaria neutral
  show rett worried#; then fade to rett worried OM
  pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")
  show rett worried OM
  "Rett rose his brows, his mouth parting a bit."

  show merona t worried
  show cimaria worried
  rt "So soon?"

  show rett worried
  "Cimaria crossed her arms and stared at the tiny pebbles being flung around by her feet."

  show kreita determined
  show merona t serious
  show duran t nervous
  show cimaria worried OM
  ck "Why not? Better to get the venom out as soon as we can when you are still relatively well rather than wait for its effects to show."

  show cimaria neutral OM
  show rett neutral
  ck "This isn't even a difficult or dangerous procedure-all I am doing is using yander to attract the venom out of your system."

  show cimaria neutral
  "She shifted her gaze to the side."

  show kreita sad
  show merona t worried
  show cimaria serious OM
  show rett worried
  ck "Or at least.. That's what I hope will happen."

  show cimaria serious CE
  mi "I guess it's the reason why Cimaria can't look him in the eye."

  show duran t nervous CE
  show cimaria serious
  show rett worried OM
  rt "That's what you hope? What else could happen?"

  show kreita sad CE
  show merona t sad
  show duran t sad
  show cimaria serious OM
  show rett confused
  ck "Nothing. Nothing could happen. Your venom would still be embedded inside you, and it would be stuck there..."

  show kreita worried
  show cimaria neutral
  "She finally rose her head and focused on the path ahead."

  play music music_White
  show merona t serious
  show duran t neutral
  show cimaria neutral OM
  show rett neutral
  ck "Yander should work. Do not worry about it... That's my job."

  show cimaria neutral
  show rett neutral OM
  rt "Cimaria..."

  show cimaria gentle
  show rett neutral
  "She nodded."

  show merona t determined
  show duran t surprised
  show cimaria gentle OM
  show rett sadSmile
  ck "You are going to be fine, Rett. I'll make sure of it."

  show kreita determined
  show duran t neutral
  show cimaria gentle
  "Kreita, forcing herself to smile, took one hand off the cart and thumped him on the back."

  #(pronounce "cous" like the first part of "cousin")
  show kreita determined OM
  show merona t worried
  show cimaria surprised
  show rett neutral
  kh "Have some faith in our trusty healer, cous. She knows what she's doing. Besides, it's not even your fault that you're in this whole deal."

  play music music_Words_Fall_Apart
  show kreita sad OM
  show merona t surprised
  show duran t sad
  show cimaria worried
  show rett confused
  kh "It's mine."

  show kreita sad
  show rett aggressive
  "Rett frowned and shot his head at Kreita."

  show kreita serious
  show merona t sadSmile
  show rett aggressive OM
  rt "Don't say that. There's no need to blame anyone because no one could have predicted it. I just happened to be unlucky enough to have it happen to me."

  show kreita serious CE
  show cimaria serious
  show rett worried
  "She sighed, shaking her head."

  show kreita determined OM
  show merona t content
  show duran t content
  show rett sadSmile
  kh "Alright, alright... But you better not get worse or suddenly be on the verge of death on this trip. You gotta take over this cart after you're completely better because pushing it for three days straight is not fun!"

  show kreita determined
  show rett smirk
  "Rett gestured to the handles."

  show kreita worried
  show duran t surprised
  show cimaria neutral
  show rett smirk OM
  rt "Let me take it now then! I'm not completely nonfunctional after all, and I owe you big time for taking over my job like this."


  play music music_Radio_Martini
  show kreita serious OM
  show merona t grin
  show cimaria sadSmile
  show rett surprised
  kh "Nope, you're not gonna do that. You'll pay me back by giving me a portion of your dinner after you're a hundred percent human fluid."

  show kreita weakWink OM
  show duran t annoyed
  show rett grin
  kh "And by buying me the new set of arrows I've been wanting."

  show kreita neutral
  show cimaria gentle
  show rett laugh
  rt "*laugh* You've got a deal. I'll make sure to start eating my food really quickly though, before you can notice it's already gone."

  show kreita content#; fade to kreita grin
  pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita grin
  show merona t content
  show rett content
  "Kreita rolled her eyes while a grin grew on her face."

  show kreita happy
  show duran t neutral
  show cimaria neutral
  kh "Whatever. Anyways, how has everything else been holding up? I know the fish has been extremely effective on the soil."

  show kreita grin
  show merona t happy
  show cimaria content
  mk "Actually, yeah! The soil has been quite fertile, and I'm sure that's why the yander has been growing so fast."

  show kreita surprised
  show merona t content
  "Kreita pumped her fist in the air, but she didn't notice how close the branches of one of the trees were."

  play sound sound_bump
  show merona t sadSmile
  show duran t annoyed
  show cimaria sadderSmile
  show rett smirk
  kh "I knew i-OW! That better not make me need an operation..."

  show kreita pouty
  show merona t content
  show duran t neutral
  show cimaria content
  "Cimaria perked up and looked at everyone."

  show kreita neutral
  show cimaria content OM
  show rett neutral
  ck "Ah, is the monster still okay at this point?"

  #"-----------------------------------------------------------"

label lbl_chapter6_8_optionalEnd:
  if (currentPath == "A"):
    call lbl_PathA_6_8 from _call_lbl_PathA_6_8
  if (currentPath == "B"):
    call lbl_PathB_6_8 from _call_lbl_PathB_6_8
  if (currentPath == "C"):
    call lbl_PathC_6_8 from _call_lbl_PathC_6_8_1

  #(Continued in 6.9)

  #"A6.9"
  #TODO [FINAL








  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"
  #(Continuation of 6.8)
  if (currentPath == "A"):
    call lbl_PathA_6_9 from _call_lbl_PathA_6_9_1
  if (currentPath == "B"):
    call lbl_PathB_6_9 from _call_lbl_PathB_6_9_1
  if (currentPath == "C"):
    call lbl_PathC_6_9 from _call_lbl_PathC_6_9_1
  #"-----------------------------------------------------------"

  play music music_recollections
  show kreita neutral
  show merona t sadSmile
  show duran t neutral
  show cimaria serious OM
  ck "Sorry to interrupt this significant conversation, but I just want to confirm-is everything settled? Is everything under control?"

  show merona t content
  show cimaria surprised
  hide rett
  $ renpy.transition(slow_dissolve, layer="master")
  show boyen sceptical behind duran: #at right#; right from Duran
    yalign 1.0
    xalign 0.95
  show boyen sceptical at walkBounce
  "Boyen tut-tutted at her."

  show kreita content
  show cimaria serious
  show boyen neutral OM
  bg "Cimaria. You've been so focused on our plans-which is great, and thanks for keeping us on track-but it's alright if we relax a little and take our minds off of the serious stuff."

  play music music_Afterglow
  show duran t worried
  show cimaria neutral
  show boyen happy
  bg "You especially should take your mind off of everything for even a few minutes. It'll help refresh yourself!"

  show kreita worried
  show merona t serious
  show cimaria shocked
  show boyen content
  "She frowned, slightly furrowing her brows."

  show kreita content
  show merona t content
  show duran t surprised
  show cimaria shocked CE
  show boyen content OM
  bg "I'm a firm believer that one should cool down and chill out."

  show merona t grin
  show duran t neutral
  show cimaria serious OM
  show boyen grin
  ck "There's so much to do and think about... But you are right. I need to force myself to simmer."

  #(Continued in 7.0)


  jump lbl_chapter7




