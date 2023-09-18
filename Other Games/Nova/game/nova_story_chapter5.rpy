label lbl_chapter5:
  #"A5.0"
  #TODO [FINAL





  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"
  scene bg black
  #TODO [Fade from black
  play sound sound_ambiance 
  #TODO [fade in...
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest21
  show prowen neutral OM#; center
  pm "I see a town over there."
  show prowen neutral
  show kreita map pouty:#; left from Prowen#; please set her body to kreita bodyMap
    yalign 1.0
    xalign 0.8
  "Prowen jerked his head to the direction he was observing. Kreita grabbed the map sticking out of a bag's side pocket, unrolled it, and squinted at our location for a few seconds."
  play music music_Words
  show kreita map pouty OM
  $ renpy.transition(slow_dissolve, layer="master")
  hide prowen
  $ renpy.transition(slow_dissolve, layer="master")
  hide prowen
  kh "Really? Then we must be at a slightly different place than we thought according to the map if there's a town or village nearby."
  show kreita map pouty
  #TODO [fade in CS lexan strict OM#; fade in at right side -> move to center
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan strict OM behind kreita at RightToCenter
  ln "I wouldn't be surprised if that was the case. After all, we may not always be completely accurate with where we are."
  show kreita map aggressive
  show lexan neutral:
    yalign 1.0
    xalign 0.5
  "Kreita leaned into the map a bit more and scrutinized the sheet for a few more moments. Grimacing, she put it away."
  show kreita map worried OM
  show lexan confused
  kh "I don't know... But I guess I shouldn't be too much of a perfectionist with it. Even the map could be a little off. How old is the map anyways? Oh well."

  show kreita map worried
  show lexan neutral
  mi "We could be lucky if they actually have the herbs we need or even better medicine, but I just don't know if it'd be worth going to. Would it waste time for Rett?"
  $ renpy.transition(slow_dissolve, layer="master")
  show rett neutral OM behind kreita:#; left from Kreita
    yalign 1.0
    xalign 0.65  
  rt "Let's just go and scope it out. If there's nothing worth getting there, then we should be able to leave pretty quickly since it's a small town."
  show rett neutral
  show kreita worried OM:#; switch back to her normal mapless body please
    yalign 1.0
    xalign 0.8485
  show lexan worried
  kh "You sure? It's kind of risky since we don't know much about what's going on with you. Are you well enough to continue walking that far?"
  show kreita worried OM
  show rett worried OM
  rt "Well..."
  show kreita sceptical
  show rett neutral OM
  rt "The same as a few days ago. I don't feel anything extremely different."
  show lexan worried OM
  show rett neutral
  ln "What would you consider 'extremely different'?"
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria serious: #, right from Lexan
    yalign 1.0
    xalign 0.25  
  show merona t surprised:
    yalign 1.0
    xalign 1.1  
  show kreita grin CE
  show lexan confused
  show rett smirk OM
  rt "Being in constant soreness? Feeling like my arm is going to fall off?"
  show kreita laugh
  show lexan neutral
  show rett smirk
  show merona t sadSmile
  "Kreita snickered and rolled her eyes."
  show kreita content OM
  show cimaria worried
  kh "Those two things range pretty far from each other."
  show kreita neutral
  show lexan worried
  show rett content OM
  show merona t serious
  rt "Well, that's just how I feel right now! Nothing too weird, only the slight tenseness as usual."
  show rett neutral
  show cimaria worried OM
  ck "*sigh* Those symptoms are not going to help me very much, but at least you are not in pain."

  show rett wink
  show lexan neutral
  show cimaria surprised
  show merona t determinedGrin
  "Rett winked at Cimaria."
  show kreita grin2
  show rett smirk OM
  show cimaria neutral
  show merona t sadSmile
  rt "At least it's only physical pain. I could be an emotional wreck right now sobbing over everyone."
  play music music_Shes_on_my_Mind
  show lexan sadSmile
  show rett grin
  show cimaria serious:
    yalign 1.0
    xalign 0.15
  "Cimaria staggered back a few steps from Rett and stared at him."
  show kreita content
  show rett grin S
  show cimaria serious OM
  ck "What are you suggesting?"
  show rett worried
  show cimaria serious
  show merona t content
  "Rett scrunched his face and held up his hands, as if he was getting arrested."
  show lexan content
  show rett worried OM
  rt "Whoa. I was only saying that I'm fine. At least mentally. That's all."
  show rett worried
  show cimaria neutral OM
  ck "That's all?"
  show rett worried OM
  show cimaria neutral
  rt "...Yeah?"
  show rett neutral
  show cimaria content
  show merona t determinedGrin
  "Cimaria relaxed and shook her head to herself. I stifled a laugh back, and she sheepishly shot a smile at me."
  show kreita grin
  show rett sceptical
  show cimaria abashed OM
  ck "Don't even utter a sound, Merona."
  show cimaria abashed
  show merona t determinedGrin OM
  mk "I wasn't doing anything of that sort, Cimaria."
  show lexan neutral
  show merona t content
  "Rett looked at both of us with his eyebrows raised."
  show kreita grin CE
  show rett sceptical OM
  show cimaria surprised
  rt "What are we talking about now?"
  show rett sceptical
  show cimaria abashed OM
  ck "Nothing important."
  show rett neutral OM
  show kreita content
  show cimaria abashed
  rt "Okay? So-"
  stop music
  show rett neutral
  show kreita neutral
  show lexan confused
  show cimaria neutral
  show merona t surprised
  $ renpy.transition(slow_dissolve, layer="master")
  show prowen neutral OM:#; right from Merona
    yalign 1.0
    xalign -0.15
  pm "Sorry to interrupt, but the town is getting closer."

  show prowen neutral
  show merona t serious
  "He pointed off into the collection of trees. I could see small slits of town beyond the space between the trunks, and we were about ready to round off into the town's entrance."
  play music music_title
  show lexan strict
  show prowen sceptical OM
  pm "Going in or not?"

  show prowen neutral
  show rett content
  show kreita content OM
  show merona t content
  kh "Let's just check it out. We're already here, so we might as well pass through it to move on."
  show rett content OM
  show kreita content
  rt "Yeah, what she said."
  show rett content
  show lexan neutral OM
  ln "I don't mind if they don't. Anyone object?"
  show lexan neutral
  show cimaria neutral CE
  "Nobody responded, and Cimaria nodded."
  show prowen content
  show cimaria neutral OM
  ck "I guess we will be going then."
  $ renpy.transition(slow_dissolve, layer="master")
  #TODO [fade out Cimaria, Kreita and Rett
  hide cimaria 
  hide kreita
  hide rett
  show lexan determined
  show prowen surprised
  show merona t serious OM
  mk "While we're at it, we also need to see if there's a preservationist who could work with our monster we have. That's something we should get checked out fast before it starts decomposing and whatnot."
  play music music_Travel_Light
  show prowen forcedSmile OM
  show merona t serious
  pm "How's the monster doing so far?"
  show prowen forcedSmile
  show merona t surprised OM
  mk "Right now, it's strangely still in pretty good shape. It's starting to develop a bit of an... unpleasant scent, but the odor is coming really gradually. I expected it to start smelling faster, but everything has been happening a lot slower than how I thought it'd be."
  show prowen content
  show merona t content
  "He nodded and crossed his arms."
  show prowen neutral OM
  pm "Yeah, faster decomposition is for normal animals. This is a monster we're dealing with, so it's going to be different."
  show prowen neutral
  show merona t determined OM
  mk "That's what I figured; monsters-or at least this one-seem to last longer than normal animals, so I hope that this one can last for a while until we get it preserved."
  $ renpy.transition(slow_dissolve, layer="master")
  show boyen worried OM:#; left from Lexan  
    yalign 1.0
    xalign 0.15
  show lexan neutral
  show prowen sceptical
  show merona t serious
  bg "We should hurry up and find someone to preserve it. Where did you put the monster anyways? Is it still in your bag?"
  show boyen worried
  show merona t sadSmile OM
  mk "Yep, it's just peacefully resting in there. I'm kind of worried that the smell might transfer to my bag over time though, so I'm thinking of putting it somewhere else."

  show lexan worried
  show prowen sceptical OM
  show merona t sadSmile
  show boyen neutral
  pm "We should really go and find a preservationist before it's too late."
  play music music_Nincompoop
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t flabber:
    yalign 1.0
    xalign 0.7
  show boyen happy
  show lexan confused
  show prowen appalled
  show merona t surprised
  bg "Well, if we ever need to actually get rid of it, we could just cook it for dinner, right? Ha ha."
  show boyen happy S
  show duran t tired OM
  dt "*vomiting sound* Only when the last thing left to eat is our own tongues will I consider that."
  show boyen neutral OM
  show lexan neutral
  show prowen sceptical
  show merona t sadSmile
  show duran t surprised
  bg "Well, it's still meat! I'm sure it'll have some good nutrition."
  show boyen neutral
  show duran t angry CE
  "Duran closed his eyes and shook his head."
  show boyen grin
  show prowen content
  show merona t grin
  show duran t angry OM
  dt "I think I'd rather bite off my own tongue and wash that down with the blood in my mouth than eat monster meat that'd be weeks old."
  show lexan content
  show merona t laugh
  show duran t angry
  mk "That might stop you from complaining so much about everything all the time."
  show merona t grin
  show duran t annoyed OM
  dt "I don't need your sass, Mom."
  show merona t determinedGrin OM
  show duran t annoyed
  mk "Everybody needs my sass, son!"
  show boyen grin CE
  show lexan content OM
  show prowen forcedSmile
  show merona t grin
  show duran t nervous
  ln "*laugh* You two sure know how to have a fun conversation."
  show boyen content
  show lexan content
  show merona t laugh
  show duran t annoyed
  mk "Of course! How could you not with someone like Duran?"
  show merona t content
  show duran t annoyed OM
  dt "How could you with someone like Merona?"
  stop music fadeout 1.0
  scene cg forest22
  show kreita neutral#; center
  show tree#; in front of Kreita #(also center)
  "Kreita stopped walking and stared at something on a tree next to her."
  play music music_SoT
  show kreita neutral OM
  kh "Hey... well that's something new."
  show kreita neutral
  "Everyone else stopped and looked to her as well."
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria neutral OM:#; right from Kreita
    yalign 1.0
    xalign 0.95
  ck "What is it?"
  show cimaria neutral
  show kreita neutral OM
  kh "Oh, I just noticed this poster. We haven't seen a lot of signs of human activity in a while, so this was a weird sight."
  show kreita neutral:#; move a bit towards the right
    yalign 1.0
    xalign 0.7
  "Kreita moved aside and presented the poster affixed on the tree."
  $ renpy.transition(slow_dissolve, layer="master")
  show rett neutral OM:#; left from the tree
    yalign 1.0
    xalign 0.4
  rt "A notice poster?"
  show rett neutral
  show kreita pouty OM
  kh "Yeah. It just says some stuff about a criminal or whatever."
  $ renpy.transition(slow_dissolve, layer="master")
  show prowen sceptical OM:#; left from Rett:
    yalign 1.0
    xalign 0.1
  show kreita pouty
  pm "...Interesting."
  show prowen neutral
  show kreita neutral OM
  kh "Mm hm. Well, we can move on now. I just wanted to see what it was about."
  
  #(Continued in 5.1)
  #"A5.1"
  #TODO [FINAL





  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"
  #(Continuation of 5.0)

  #play music music_SoT #(from before)
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest22
  show tree
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita neutral OM#; center
  kh "Anyways, once we're in the town, it'd be best if we split up and do what we need to right?"
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria gentle OM:#; left from Kreita:
    yalign 1.0
    xalign 0.3
  show kreita neutral
  ck "I'll go to the marketplace and see if they're selling the herbs we need. I could bring a person or two with me to help me look around."
  show cimaria gentle
  $ renpy.transition(slow_dissolve, layer="master")
  hide cimaria
  show kreita surprised
  "Kreita raised her hand."
  show kreita happy
  kh "I can help with finding a preservationist around here. I'd need some others to help me search though."
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan neutral OM:#; right from Kreita:
    yalign 1.0
    xalign 0.7
  show kreita content
  $ renpy.transition(slow_dissolve, layer="master")
  hide kreita
  ln "That should be the only two things we have to do right? Everyone should be able to help with one of those tasks."
  show lexan neutral#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide lexan
  show rett neutral:#; right from Kreita:
    yalign 1.0
    xalign 0.7
  "Rett cleared his throat and placed a hand at his hip."
  play music music_piano
  show rett smirk OM
  #show kreita grin
  rt "I hope you aren't going to make me sit around and do nothing, because I'm capable enough to at least look for things..."
  show rett worried
  #show kreita neutral
  "Everyone turned to the healer for her advice, and she nodded."
  show rett content
  #show kreita grin
  ck "You can help. Just... don't use your arms too wildly. Does your entire body still feel okay in general?"
  show rett content OM
  rt "Yeah. Everything still feels pretty much the same. I'll be careful."

  play music music_Soporific
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg danger
  mi "If Rett were to get more injured here, how lucky we would be... It's almost weird to me that he feels fine though. With monster venom, I expected it to be either really excruciating or quick and fatal, but Rett isn't getting any strong effects."
  mi "At least it's a good thing. With me, my shoulder probably would've been finished if the venom wasn't taken out of my body in due time. I hope the venom doesn't start activating or whatnot all of a sudden for him."
  play music music_Cool_Steel_Breeze
  scene cg forest22
  show tree
  show cimaria gentle OM:#; left from Kreita:
    yalign 1.0
    xalign 0.3
  show kreita grin#, center
  #TODO [no Rett here
  ck "Good. I suppose we can start arranging ourselves into groups now."
  $ renpy.transition(slow_dissolve, layer="master")
  show boyen content OM:#; right from Kreita:
    yalign 1.0
    xalign 0.7
  show cimaria gentle
  bg "I'd like to go to the marketplace. If I spot anything worth buying for cooking purposes, I could also get it for us. I promise not to focus only on buying food though!"
  $ renpy.transition(slow_dissolve, layer="master")
  hide boyen
  show lexan content OM:#; right from Kreita #(replace Boyen):
    yalign 1.0
    xalign 0.7
  ln "I consider myself to have a keen eye for shopping, so I could be of some good use as a part of the marketplace group."
  $ renpy.transition(slow_dissolve, layer="master")
  hide lexan
  show prowen neutral OM:#; right from Kreita #(replace Lexan):
    yalign 1.0
    xalign 0.7
  pm "I'll help the other one then."
  $ renpy.transition(slow_dissolve, layer="master")
  hide prowen
  show duran t neutral OM:#; right from Kreita #(replace Prowen):
    yalign 1.0
    xalign 0.7
  dt "I guess I can go with the preservationist group too. I'm not that great at shopping anyways."
  $ renpy.transition(slow_dissolve, layer="master")
  hide duran
  show merona t surprised OM:#; right from Kreita #(replace Duran):
    yalign 1.0
    xalign 0.7
  mk "Um, I'll go with..."
  show merona t serious
  mk "..."

  show merona t reflective
  mi "Hm... which one should I pick?"
  play music music_Radio_Martini
  $ renpy.transition(slow_dissolve, layer="master")
  show rett content OM:#; right from Merona
    yalign 1.0
    xalign 0.9
  show merona t surprised
  rt "Looks like we're the only two that haven't picked a group yet. I don't really care which one I'm a part of, so you can decide which one you want, Merona. I'll take the one you didn't choose."
  show merona t content OM
  show rett content
  mk "Oh, okay. Thanks."
  show merona t reflective
  mi "Well, both groups would have an even amount of people in them no matter which one I pick, so that reasoning won't work."
  show merona t content
  mi "If I helped to find a preservationist and found one, I could learn some things about the monster, which would be nice. If I helped shop around, I could possibly spot other plants or herbs we may need that I learned of. What if I tried helping both?"

  #(A=red, B=blue, C=pink)
  menu:
    "Go with the shopping group":
      $currentPath = "B"
      $BChoiceCount += 1
    "Go with the preservationist group":
      $currentPath = "A"
      $AChoiceCount += 1
    "Try helping both":
      $currentPath = "C"
      $CChoiceCount += 1

  #(Continued in 5.2A, B, C)
  #"A5.2"
  #TODO [FINAL




  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"
  #(Continuation of 5.1)
  if (currentPath == "A"):
    call lbl_PathA_5_2_1 from _call_lbl_PathA_5_2_1_1 
  if (currentPath == "B"):
    call lbl_PathB_5_2_1 from _call_lbl_PathB_5_2_1_1 
  if (currentPath == "C"):
    call lbl_PathC_5_2_1 from _call_lbl_PathC_5_2_1_1  
  #"--------------------------------"
  show rett content OM#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide rett
  show cimaria neutral
  rt "Okay, I'll join the other one! Let's get going now that we're all split up now."
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan neutral OM:
    yalign 1.0
    xalign 1.1
  show kreita neutral
  ln "We should set a place to meet up later. How about... we go to that clock tower over there since it looks like it's around the center of town. After half an hour, we should try and tell each other of our current statuses. If both groups don't succeed, we can automatically leave."
  show cimaria worried
  show lexan neutral
  "Cimaria pursed her lips and didn't say anything for a few seconds."
  show cimaria worried OM
  show merona t serious
  ck "Half an hour seems a bit short. Time can pass pretty quickly when we're trying to search for something with urgency, so how about an hour? The sun would be setting, but there'd still be enough light for us to travel on some more and find another resting area."
  show cimaria worried
  $ renpy.transition(slow_dissolve, layer="master")
  show prowen neutral OM:#; left from Cimaria:
    yalign 1.0
    xalign 0.1
  pm "Sounds fine. I don't care either way."
  $ renpy.transition(slow_dissolve, layer="master")
  hide prowen
  show merona t surprised
  show cimaria neutral
  "I shrugged as well."
  show merona t surprised OM
  mk "Whatever works best... I wouldn't want it to seem like we weren't spending enough time though, so an hour looks to be better."
  show merona t serious
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t annoyed OM:#; left from Cimaria:
    yalign 1.0
    xalign 0.1
  dt "Personally, I also think an hour works out, but shouldn't we actually be going now? Let's just decide it."
  $ renpy.transition(slow_dissolve, layer="master")
  hide duran
  show lexan serious
  "Lexan nodded and crossed his arms."
  show lexan neutral OM
  ln "An hour is fine to me too, and I don't think there are any other objections, so we'll all meet at the clock tower in about an hour."
  play music music_potHappy
  show lexan content
  show kreita happy
  kh "Alright, off we go!"
  #"--------------------------------"
  if (currentPath == "A"):
    call lbl_PathA_5_2_2 from _call_lbl_PathA_5_2_2_1 
  if (currentPath == "B"):
    call lbl_PathB_5_2_2 from _call_lbl_PathB_5_2_2_1 
  if (currentPath == "C"):
    call lbl_PathC_5_2_2 from _call_lbl_PathC_5_2_2_1  
  #"--------------------------------"
  
  #(Continued in 5.3)
  #"A5.3"
  #TODO [FINAL


  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"


  if (currentPath == "A"):
    call lbl_PathA_5_3 from _call_lbl_PathA_5_3_1 
  if (currentPath == "B"):
    call lbl_PathB_5_3 from _call_lbl_PathB_5_3_1
  if (currentPath == "C"):
    call lbl_PathC_5_3 from _call_lbl_PathC_5_3_1 

  #(Continued in 5.4)

  #"A5.4"
  #TODO [FINAL




  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"

  #(Continuation of 5.3)
  if (currentPath == "A"):
    call lbl_PathA_5_4 from _call_lbl_PathA_5_4_1
  if (currentPath == "B"):
    call lbl_PathB_5_4 from _call_lbl_PathB_5_4_1
  if (currentPath == "C"):
    call lbl_PathC_5_4 from _call_lbl_PathC_5_4_1 


  #(Continued in 5.5)

  #"A5.5"
  #TODO [FINAL





  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"
  #(Continuation of 5.4)
  if (currentPath == "A"):
    call lbl_PathA_5_5 from _call_lbl_PathA_5_5_1
  if (currentPath == "B"):
    call lbl_PathB_5_5 from _call_lbl_PathB_5_5_1
  if (currentPath == "C"):
    call lbl_PathC_5_5 from _call_lbl_PathC_5_5_1 
  #(Continued in 5.6)

  #"A5.6"
  #TODO [FINAL






  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"
  #(Continuation of 5.5)
  if (currentPath == "A"):
    call lbl_PathA_5_6 from _call_lbl_PathA_5_6_1
  if (currentPath == "B"):
    call lbl_PathB_5_6 from _call_lbl_PathB_5_6_1
  if (currentPath == "C"):
    call lbl_PathC_5_6 from _call_lbl_PathC_5_6_1
  #(Continued in 5.7)
  #"A5.7"
  #TODO [FINAL






  #The dashed line separates where the main storyline and path separate. The main storyline will "be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"
  #(Continuation of 5.6)
  if (currentPath == "A"):
    call lbl_PathA_5_7 from _call_lbl_PathA_5_7_1
  if (currentPath == "B"):
    call lbl_PathB_5_7 from _call_lbl_PathB_5_7_1
  if (currentPath == "C"):
    call lbl_PathC_5_7 from _call_lbl_PathC_5_7_1
  #(Continued in 5.8)
  #"A5.8"
  #TODO [FINAL








  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"
  #(Continuation of 5.7)
  if (currentPath == "A"):
    call lbl_PathA_5_8 from _call_lbl_PathA_5_8_1
  if (currentPath == "B"):
    call lbl_PathB_5_8 from _call_lbl_PathB_5_8_1
  if (currentPath == "C"):
    call lbl_PathC_5_8 from _call_lbl_PathC_5_8_1
  #"A5.9"
  #TODO [FINAL








  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"
  if (currentPath == "A"):
    call lbl_PathA_5_9 from _call_lbl_PathA_5_9_1
  if (currentPath == "B"):
    call lbl_PathB_5_9 from _call_lbl_PathB_5_9_1
  if (currentPath == "C"):
    call lbl_PathC_5_9 from _call_lbl_PathC_5_9_1
  #(Continued in A6.0)





  jump lbl_chapter6

