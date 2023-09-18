label lbl_ending_academy:
  #"A - ACADEMY ENDING"
  #TODO [FINAL








  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. A path's storyline is red. B path's storyline is blue. C path's storyline is green. If two paths share the same text, it will be in pink."
  #"-----------------------------------------------------------"
  #(8/22/17)
  #TODO [FINAL
  play music music_life
  scene cg castleGate
  show wagon:#; right, always behind the characters
    yalign 1.0
    xalign 1.0
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content#; center
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita content behind merona:#; right from Merona
    yalign 1.0
    xalign 0.7
  $ renpy.transition(slow_dissolve, layer="master")
  show rett smirk:#; right from Kreita
    yalign 1.0
    xalign 1.05
  "Kreita threw the last of our bags onto our new wagon and sighed."

  show merona t worried
  show kreita pouty OM
  kh "We better not run into any monsters on the way back. I don't think I could handle another destroyed wagon..."

  show merona t grin
  show kreita pouty
  show rett laugh
  rt "Oh come on, you're the indestructible Kreita! You could totally carry all our bags and not break a sweat."

  show kreita fierce OM
  show rett grin
  kh "Don't make me personally find another monster to bite you."

  $ renpy.transition(slow_dissolve, layer="master")
  show lexan worried OM behind merona:#; left
    yalign 1.0
    xalign 0.3
  show merona t serious
  show kreita neutral
  show rett neutral
  ln "Are those all the things we need to bring back? Anybody need to double-check their belongings?"

  $ renpy.transition(slow_dissolve, layer="master")
  show boyen serious OM behind lexan:#; left from Lexan
    yalign 1.0
    xalign 0.06
  show merona t content
  show lexan surprised
  show kreita grin
  show rett grin
  bg "Lexan, we've already checked twice. We can start heading home now."

  show merona t grin
  show boyen neutral
  show lexan content
  mi "Home."

  mi "Such a good word to hear..."

  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria neutral OM behind merona:#; left from Merona
    yalign 1.0
    xalign 0.83
  show merona t content
  show kreita content
  show rett content
  show boyen content
  ck "The queen has been notified of our departure, I presume, so we should be allowed to leave."

  $ renpy.transition(slow_dissolve, layer="master")
  show duran t annoyed OM:#; left edge of the screen
    yalign 1.0
    xalign -0.03
  show merona t sadSmile
  show lexan neutral
  show cimaria neutral
  dt "Yeah, can we hurry up? I've got a bed to go back to, and I'd prefer if we didn't waste anymore time sleeping on dirt."

  show merona t happy OM
  show duran t annoyed
  show lexan content
  show cimaria gentle
  show rett smirk
  mk "Be patient, Duran. Besides, it's nice to sleep under the stars, isn't it?"

  show merona t grin
  show duran t annoyed CE
  "He shook his head and groaned."

  show duran t annoyed OM
  show kreita grin
  show rett grin
  show boyen grin
  dt "Stars don't protect me against unidentifiable bug bites."
  show merona t sadSmile
  show duran t angry
  show lexan grin
  show cimaria grin
  show kreita fierce OM
  kh "Just set yourself on fire-that should be enough to drive them away, right?"

  show merona t content
  show kreita fierce
  show rett smirk
  "Duran swatted his hand out at Kreita."

  show merona t grin
  show duran t angry OM
  show kreita grin
  dt "Get away from me, mosquito."

  show merona t content
  show duran t annoyed
  show kreita laugh
  show rett content
  show boyen content
  "She rolled his eyes and laughed at him."

  show duran t content
  show lexan content
  show cimaria content
  show kreita grin2
  show rett content OM
  show boyen grin
  rt "Guys, let's get going. Laneo is waiting for us!"

  show merona t reflective CE
  show kreita content
  show rett content
  "Heading out the castle doors, we stepped back into our familiar routine. I closed my eyes and took a deep breath, sucking in the refreshing ocean air of Calil."

  show merona t content
  mi "Feels good to reconnect with nature. Like I'm returning to my roots."

  mi "I wonder if we have time to stop back home and visit my parents... I'd love for them to meet the people I've been traveling with."

  show merona t surprised
  mi "Speaking of those people..."

  play music music_newBegin
  show merona t surprised OM
  show duran t surprised
  show lexan surprised
  show cimaria neutral
  show kreita neutral
  show rett surprised
  show boyen neutral
  mk "Hey everyone! I have a few things I want to say before I forget."

  show merona t content
  show duran t neutral
  show lexan content
  show cimaria content
  show kreita content
  show rett content
  show boyen content
  "I cleared my throat and glanced around, making sure everyone was listening."

  show merona t happy OM
  show lexan grin
  show duran t grin
  show cimaria grin
  show boyen grin
  show kreita grin
  show rett grin
  mk "You guys were the best people I could have gone on a journey with, and I'm so happy that I did this whole thing."

  show merona t sadSmile OM
  show lexan sadSmile
  show duran t sadSmile
  show cimaria sadSmile
  show boyen sadSmile
  show kreita sadSmile
  show rett sadSmile
  mk "I've grown in so many ways I couldn't have imagined all because of everyone here. We've had troubling times and moments where we felt helpless, but we made it through them."

  show merona t content OM
  show lexan content
  show duran t content
  show cimaria gentle
  show boyen content
  show kreita content
  show rett content
  mk "Look where we are now! It's amazing what we've accomplished."

  show merona t happy OM
  #TODO [In path B: CS lexan blushSmile#; In path A and C: CS lexan grin
  #TODO [In path A: CS duran t blushSmile#; In path B and C: CS duran t grin
  if (currentPath == "A"):
    show duran t blushSmile
    show lexan grin
  if (currentPath == "B"):
    show duran t grin
    show lexan blushSmile
  if (currentPath == "C"):
    show duran t grin
    show lexan grin
  show cimaria grin
  show boyen grin
  show kreita grin
  show rett grin
  mk "Thank you, thank you, thank you."

  show merona t grin
  "Boyen patted my shoulder."

  show merona t blushSmile
  show lexan grin
  show duran t content
  show boyen happy OM
  show cimaria gentle
  show kreita grin
  show rett smirk
  bg "We should be thanking you too, Merona."

  show boyen content OM
  bg "Everyone here went on their own personal journeys, and you were definitely a big part of it."

  show merona t grin
  show cimaria gentle OM
  show boyen grin
  ck "Thank you, Merona."

  show cimaria gentle
  show kreita happy
  kh "Thanks!"

  #TODO [In path B: CS lexan blushSmile OM#; In path A and C: CS lexan content OM
  if (currentPath == "A"):
    show lexan content OM
  if (currentPath == "B"):
    show lexan blushSmile OM
  if (currentPath == "C"):
    show lexan content OM
  show kreita grin
  ln "Thank you."

  show lexan grin
  show duran t surprised
  show rett content OM
  rt "Thanks, Merona."

  show duran t embarrassed OM
  show rett grin
  dt "...Thank you, Merona."

  #TODO [fade to and from black
  show black with fade

  #if (currentPath == "C"): 
  #if ((AChoiceCount < 2) and (BChoiceCount < 2)):
  if (AChoiceCount >= 2) :
    jump lbl_ending_academy_A
  if (BChoiceCount >= 2):
    jump lbl_ending_academy_B
    
  jump lbl_ending_academy_C
  
label lbl_ending_academy_A:
  #TODO [A PATH
  play music music_piano
  #TODO [fade in CG forest33
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest33
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t embarrassed:#; left
    yalign 1.0
    xalign 0.35
  show duran at walkBounce
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content:#; right
    yalign 1.0
    xalign 0.65
  show merona at walkBounce
  "As we all fell back into our usual patterns of silence and conversation, Duran hung by my side and tapped my shoulder."

  show duran t embarrassed OM
  show merona t surprised
  dt "Hey."

  show duran t embarrassed
  show merona t content OM
  mk "Hey Duran! What's up?"

  show duran t embarrassed OM
  show merona t serious
  dt "I..."

  show duran t embarrassed
  dt "..."

  show duran t determined CE
  show merona t surprised
  "He hesitated for a few seconds before slapping his cheeks and furiously shaking his head."

  show duran t determined OM
  show merona t worried
  dt "Come on, you can do this."

  show merona t serious
  dt "Merona..."

  show duran t embarrassed OM
  show merona t surprisedBlush
  dt "I like you. A lot."

  show duran t worried OM
  dt "I know I'm really weird and not that fun to be around, but when we get back to the academy... Would you be willing to be with me?"

  #(Player choice)
  show duran t worried
  menu:
    "Yes.":
      pass
    "No.":
      jump lbl_ending_academy_A_no

label lbl_ending_academy_A_yes:
  play music music_romance
  show duran t surprised
  show merona t blushSmile OM
  mk "You know, I'm much weirder than you are."

  show duran t flabber
  mk "And you're super fun to be with."

  #TODO [fade in 
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg MeronaDuranRomance3
  mk "Let's try it out!"

  scene cg MeronaDuranRomance1
  "Duran couldn't keep an uncharacteristic grin from growing on his face."

  scene cg MeronaDuranRomance2
  dt "You're not kidding, right? This is actually happening?"
  scene cg MeronaDuranRomance3
  mk "Why are you so surprised? It's not like I hated you."

  scene cg MeronaDuranRomance2
  dt "Did you know that I liked you?"

  scene cg MeronaDuranRomance3
  mk "Well, it's hard to tell if you like anything."

  scene cg MeronaDuranRomance2
  dt "That's... different now."

  scene cg MeronaDuranRomance3
  mk "Aw, you sure know how to make a girl feel special."

  #TODO [fade back to former scene
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest33
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t blushSmile:#; left
    yalign 1.0
    xalign 0.35
  show duran at walkBounce
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t blushSmile:#; right
    yalign 1.0
    xalign 0.65
  show merona at walkBounce
  "Duran scoffed but still held the grin on his face. He lost his slump and straightened up his posture as we kept walking. For a moment, he almost seemed taller than me."
  
  jump lbl_ending_academy_final

label lbl_ending_academy_A_no:
  play music music_recollections
  show duran t sad
  show merona t worried OM
  mk "I don't know, Duran... For now, I want to focus more on my ability and school stuff. We both have a lot going on."

  show duran t nervous
  show merona t sad OM
  mk "I do like you, but I think we should remain friends."

  show duran t nervous OM
  show merona t sadSmile
  dt "Oh well. At least I tried."

  show duran t surprised
  show merona t grin
  "I fake-punched him on the arm and grinned."

  show duran t embarrassed
  show merona t happy OM
  mk "Yeah! You tried. How very un-Duran-like of you."

  show duran t embarrassed OM
  show merona t surprised
  dt "Don't make me regret trying."

  show duran t embarrassed
  show merona t surprised OM
  mk "What's there to regret? Just because it's not very characteristic of you doesn't mean you can't change yourself. This is a good change."

  show duran t embarrassed OM
  show merona t content
  dt "I get it, I get it. But when we're back in Laneo, you better not tell anyone. I got a reputation to uphold."

  show duran t surprised
  show merona t determinedGrin OM
  mk "And you're going to change it just by hanging around me."

  show duran t content
  show merona t content
  "With a hint of a smile on his lips, Duran rolled his eyes and continued walking by my side. We didn't talk anymore, but Duran was someone I was comfortable staying in silence with."

  jump lbl_ending_academy_final

label lbl_ending_academy_B:                                     

  #TODO [B PATH

  play music music_piano
  #TODO [fade in CG forest33
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest33
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan embarrassed:#; right
    yalign 1.0
    xalign 0.75
  show lexan at walkBounce
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t surprised:#; left
    yalign 1.0
    xalign 0.3
  show merona at walkBounce
  "As we all fell back into our usual patterns of silence and conversation, Lexan hung by my side and tapped my shoulder."

  show lexan embarrassed OM
  show merona t embarrassed
  ln "Merona... Can I talk to you for a moment?"

  show lexan embarrassed
  show merona t serious
  "I nodded. Lexan gestured us to slow down until we were at the back of the group, and he didn't say a word for a few seconds."

  show lexan embarrassed OM
  show merona t worried
  ln "So... I wanted to ask you something."

  show lexan worried OM
  show merona t embarrassed
  ln "I may be mistaken, but for these past number of weeks, I've felt like you... "

  show lexan sadSmile OM
  ln "Hold feelings for me."

  show lexan worried
  show merona t embarrassed CE
  mk "..."

  show lexan surprisedBlush
  show merona t embarrassedSmile OM
  mk "I... I like you."

  show merona t embarrassedSmile
  "It felt like I had finally cleared that giant fallen tree out of the way in my mind. Just by saying those words aloud, I could finally keep moving forward."

  show lexan sad OM
  show merona t worried
  ln "Merona..."

  play music music_Ill_be_right_behind_you_Josephine
  show merona t sad
  ln "We can't be together."

  show lexan worried OM
  ln "I'm your teacher, and you're my student."

  show lexan worried
  show merona t sad CE
  mk "..."

  show merona t sad OM
  mk "I know."

  show lexan surprised
  show merona t worried OM
  mk "But I can't help who I like."

  show lexan serious
  show merona t disappointed
  ln "..."

  show lexan serious OM
  show merona t nervous
  ln "Neither can I."

  show lexan sadSmile
  show merona t sadSmile OM
  mk "Don't worry, I wasn't expecting for us to become a couple or whatever. It's for the best."

  show lexan sadSmile OM
  show merona t worried
  ln "Thank you for being so understanding."

  show lexan surprised
  show merona t surprised OM
  mk "Wait..."

  show lexan surprisedBlush
  show merona t worried OM
  mk "Would you consider being together after I graduate?"

  show lexan wink
  show merona t embarrassed
  "He winked."

  show lexan happy OM
  show merona t blushSmile
  ln "Okay, let's wait and see."

  show lexan content#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide lexan
  show merona t serious
  "Lexan walked ahead of me and joined Cimaria and Rett's conversation. I stayed behind at the back, mulling over what just happened."

  show merona t content
  mi "I can let go of this... for now."

  jump lbl_ending_academy_final

label lbl_ending_academy_C:                                               

  #TODO [C PATH
  play music music_title
  #TODO [fade in CG 
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest33
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t grin#; center
  show merona at walkBounce
  mi "I hope that I can still see everyone often even in Laneo... Just because we're not journeying together anymore doesn't mean we can't meet up!"

  show merona t content
  mi "Boyen is in the kitchen, Cimaria and Lexan are in their offices, Kreita and Rett are constantly travelling, and Duran is in the classroom."

  show merona t determinedGrin
  "As much as I'm sad that our journey is coming to an end, I'm so excited to go back home."

label lbl_ending_academy_final:
  if (currentPath == "A"):
    $ renpy.transition(slow_dissolve, layer="master")
    hide duran
    play music music_title
  if (currentPath == "B"):
    play music music_title
  show merona t content CE
  mi "Back to the books. Back to the classroom."

  show merona t grin
  mi "It's certainly not as exciting as staying at the castle or journeying, but I want to learn more! I want to stuff my head with more knowledge about my ability and monsters, and staying in school is the best option for the current me."

  #TODO [fade in CG 
  scene cg ANewJourney with fade
  mi "Besides, it's not like things are going to be completely the same."

  "It's a new life, a new adventure, and..."

  "Dare I say a new journey?"

  jump lbl_END

label lbl_ending_journey:
  #########################################################"
  #"A - JOURNEY ENDING"
  #TODO [FINAL








  #The dashed line separates where the main storyline and path separate. The main storyline will"
  #"be the same text in scripts A, B, and C. A path's storyline is red. B path's storyline is blue. C path's storyline is green. If two paths share the same text, it will be in pink."
  #"-----------------------------------------------------------"
  #(8/22/17)
  #TODO [FINAL

  play music music_life
  scene cg castleGate
  $ renpy.transition(slow_dissolve, layer="master")
  show wagon:#; right, always behind the characters
    yalign 1.0
    xalign 1.0
  "As Rett rolled the wagon down the path, he had a bounce in his step and whistled a little ditty."

  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content#, center
  $ renpy.transition(slow_dissolve, layer="master")
  show rett content OM:#, right
    yalign 1.0
    xalign 0.83
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria annoyed behind merona:#, left from Rett
    yalign 1.0
    xalign 0.64
  rt "This wagon is pretty sturdy! I bet it would take at least two monsters to destroy it."

  show rett smirk
  show cimaria annoyed OM
  ck "Ugh, please don't mention monsters..."

  $ renpy.transition(slow_dissolve, layer="master")
  show kreita grin behind merona:#, left from Merona
    yalign 1.0
    xalign 0.3
  show merona t surprised
  show rett surprised
  show cimaria surprised
  "Kreita smacked my back."

  show merona t sadSmile
  show kreita fierce OM
  show rett grin
  show cimaria grin
  kh "Don't worry, we've got Merona to take care of them now!"


  show merona t sadSmile OM
  show kreita fierce
  mk "Don't place such high expectations on me!"

  show merona t serious CE
  show kreita lol
  show rett laugh
  show cimaria laugh
  "Everyone laughed, but I shook my head."

  show merona t determined OM
  show kreita neutral
  show rett neutral
  show cimaria neutral
  mk "I still have so much to learn about monsters..."

  $ renpy.transition(slow_dissolve, layer="master")
  show boyen content OM behind kreita:#, left from Kreita
    yalign 1.0
    xalign 0.09
  show kreita grin2
  show merona t content
  show rett content
  show cimaria gentle
  bg "Well that's why you're going to continue journeying! You'll run into more monsters, learn about the world right at your fingertips, and travel all across the country."

  $ renpy.transition(slow_dissolve, layer="master")
  show duran t annoyed OM:#, left from Boyen
    yalign 1.0
    xalign -0.03
  show boyen neutral
  show kreita grin
  show merona t surprised
  show rett smirk
  show cimaria annoyed
  dt "I wish I was in your place... I can't stand the classroom any longer."

  $ renpy.transition(slow_dissolve, layer="master")
  show lexan neutral OM:#, right from Rett
    yalign 1.0
    xalign 1.15
  show duran t annoyed
  show boyen content
  show merona t content
  ln "Duran, you'll graduate in a few short years. The classroom isn't a terrible place to be."

  show merona t serious
  show lexan strict
  show duran t annoyed OM
  show kreita neutral
  show rett grin
  show cimaria serious
  dt "Yeah, because you lived in it for the past twenty years."

  show merona t grin
  show lexan content
  show duran t neutral
  show boyen content
  show kreita content
  show rett content
  show cimaria serious OM CE
  ck "I do have to say, working out in the real world is much more exciting."

  show merona t content
  show duran t content
  show kreita grin
  show cimaria content OM
  ck "As soon as I started my practical training, that was when I really became passionate about healing. I could directly see the effects of my ability."

  show kreita happy
  show cimaria gentle
  kh "Same for me as a hunter! On my first hunt, it felt like all my training finally had a purpose."

  show kreita content
  show rett content OM
  rt "I can relate too, especially to the training-having-a-purpose part. Practice and learning always feels so tedious, but once they're put to use, you'll appreciate it."

  show merona t happy OM
  show lexan grin
  show duran t grin
  show boyen grin
  show kreita grin
  show rett grin
  show cimaria grin
  mk "I'm getting more and more excited now..."

  play music music_newBegin
  show merona t disappointed OM
  show lexan worried
  show duran t sad
  show boyen worried
  show kreita worried
  show rett worried
  show cimaria worried
  mk "But I'm also disappointed that I won't do this with you guys."

  show merona t happy OM
  show lexan grin
  show duran t grin
  show cimaria grin
  show boyen grin
  show kreita grin
  show rett grin
  mk "You were the best people I could have gone on a journey with, and I'm so happy that I did this whole thing."

  show merona t sadSmile OM
  show lexan sadSmile
  show duran t sadSmile
  show cimaria sadSmile
  show boyen sadSmile
  show kreita sadSmile
  show rett sadSmile
  mk "I've grown in so many ways I couldn't have imagined all because of everyone here. We've had troubling times and moments where we felt helpless, but we made it through them."

  show merona t content OM
  show lexan content
  show duran t content
  show cimaria gentle
  show boyen content
  show kreita content
  show rett content
  mk "Look where we are now! It's amazing what we've accomplished."

  show merona t happy OM
  #TODO [In path B: CS lexan blushSmile#; In path A and C: CS lexan grin
  #TODO [In path A: CS duran t blushSmile#; In path B and C: CS duran t grin
  if (currentPath == "A"):
    show duran t blushSmile
    show lexan grin
  if (currentPath == "B"):
    show duran t grin
    show lexan blushSmile
  if (currentPath == "C"):
    show duran t grin
    show lexan grin
  show cimaria grin
  show boyen grin
  show kreita grin
  show rett grin
  mk "Thank you, thank you, thank you."

  show merona t grin
  "Boyen patted my shoulder."

  show merona t blushSmile
  show lexan grin
  show duran t content
  show boyen happy OM
  show cimaria gentle
  show kreita grin
  show rett smirk
  bg "We should be thanking you too, Merona."

  show boyen content OM
  bg "Everyone here went on their own personal journeys, and you were definitely a big part of it."

  show merona t grin
  show cimaria gentle OM
  show boyen grin
  ck "Thank you, Merona."

  show cimaria gentle
  show kreita happy
  kh "Thanks!"

  #TODO [In path B: CS lexan blushSmile OM#; In path A and C: CS lexan content OM
  if (currentPath == "A"):
    show lexan content OM
  if (currentPath == "B"):
    show lexan blushSmile OM
  if (currentPath == "C"):
    show lexan content OM
  show kreita grin
  ln "Thank you."

  show lexan grin
  show duran t surprised
  show rett content OM
  rt "Thanks, Merona."

  show duran t embarrassed OM
  show rett grin
  dt "...Thank you, Merona."

  #TODO [fade to and from black

  #if (currentPath == "C"): 
  #if ((AChoiceCount < 2) and (BChoiceCount < 2)):
  if (AChoiceCount >= 2) :
    jump lbl_ending_journey_A
  if (BChoiceCount >= 2):
    jump lbl_ending_journey_B
  
  jump lbl_ending_academy_C
    
label lbl_ending_journey_A:
  #TODO [A PATH
  play music music_piano
  #TODO [fade in CG forest33
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest33
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t embarrassed OM:#; left
    yalign 1.0
    xalign 0.35
  show duran at walkBounce
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content:#; right
    yalign 1.0
    xalign 0.65
  show merona at walkBounce
  $ renpy.pause(1.0)
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t embarrassed
  "Duran hung by my side as the others settled with their usual conversation partners. He glanced up at my face and opened his mouth but immediately closed it."

  show merona t surprised
  dt "..."

  show merona t surprised OM
  mk "Hey Duran. What's wrong?"


  show duran t embarrassed OM
  show merona t serious
  dt "I..."

  show duran t embarrassed
  show merona t content
  "He looked away, but his rosy cheeks signaled what he was about to say. I couldn't help but let a smile break out over my face."

  show duran t angryBlush
  show merona t happy OM
  mk "...Yes?"

  show duran t angryBlush OM
  show merona t content
  dt "Why do you look so smug?"

  show duran t embarrassed
  show merona t blushSmile OM
  mk "What did you want to say?"

  show duran t embarrassed OM
  show merona t blushSmile
  dt "*sigh* I like you, Merona."

  show duran t determined
  show merona t embarrassedSmile
  "As soon as he said it, he looked at me square in the face with determination in his eyes."

  show duran t determined OM
  dt "I know we won't see each other for a long time because of your journeying, but... I really want to be with you."

  show duran t worried OM
  show merona t surprisedBlush
  dt "After you're done with all this... Would you be willing to be with me?"

  #(Player choice)
  show duran t worried
  menu:
    "Yes.":
      pass
    "No.":
      jump lbl_ending_journey_A_no
    
label lbl_ending_journey_A_yes:
  play music music_romance
  show duran t flabber
  show merona t blushSmile OM
  mk "Are trees living things?"

  "Duran furrowed his brows."

  show duran t flabber OM
  show merona t grin
  dt "Your living or everyone else's living?"

  show duran t embarrassed
  show merona t blushSmile OM
  mk "*laugh* The answer is yes."

  show duran t blushSmile OM
  show merona t blushSmile
  dt "That was such a roundabout way of answering me."

  show duran t blushSmile
  show merona t blushSmile OM
  mk "Hey, how else would I have responded?"

  show merona t blushSmile
  "He shook his head and lightly punched my upper arm."

  #TODO [fade in CG 
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg MeronaDuranRomance2
  dt "Point taken."

  dt "You're going to become even stranger after you're done travelling, aren't you?"

  scene cg MeronaDuranRomance3
  mk "You know it."

  scene cg MeronaDuranRomance2
  dt "Good."

  play music music_title
  #TODO [fade back to former scene
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest33
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t blushSmile:#; left
    yalign 1.0
    xalign 0.35
  show duran at walkBounce
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t blushSmile:#; right
    yalign 1.0
    xalign 0.65
  show merona at walkBounce
  "Duran and I continued walking together in silence, staring ahead of us, wondering what the future would entail. He reached his palm out to me, and my hand met his."
  
  jump lbl_ending_journey_end
  
label lbl_ending_journey_A_no:
  play music music_recollections
  show duran t confused
  show merona t worried OM
  mk "It's going to be hard, Duran..."




  show duran t sad
  show merona t sad OM
  mk "You won't be able to contact me even by mail, and we won't see each other for years."

  show duran t serious
  show merona t sadSmile OM
  mk "I like you too, but I think we should move on from each other. The timing just isn't right."

  show duran t surprised
  show merona t content OM
  mk "Just open up, and I'm sure you'll find someone else."

  show duran t sad
  show merona t sadSmile
  "He nodded, remaining silent."

  show duran t sad CE
  dt "..."

  show duran t worried
  show merona t worried OM
  mk "We're still friends, aren't we?"

  show duran t neutral
  show merona t sadSmile OM
  mk "You can still laugh at the weird things I do, and I'll laugh at the weird things you do."

  show duran t sadSmile
  show merona t content OM
  mk "When I'm back in Laneo, I'll make sure to visit you, and we can hang out."

  show duran t sadSmile OM
  show merona t content
  dt "...Yeah. Yeah, we can."

  show duran t worried OM
  show merona t sadSmile
  dt "I'm gonna miss you, Merona."

  show duran t sadSmile
  show merona t sadSmile OM
  mk "Me too."

  play music music_title
  show duran t serious
  show merona t serious
  "Duran and I wordlessly followed the group down the path to the entrance into the forest, the exit out of Calil. We stared ahead of us, wondering what the future would entail."

  jump lbl_ending_journey_end           


label lbl_ending_journey_B:
  #TODO [B PATH
  play music music_piano
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest33
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan embarrassed:#; right
    yalign 1.0
    xalign 0.75
  show lexan at walkBounce
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t serious:#; left
    yalign 1.0
    xalign 0.3
  show merona at walkBounce
  "We started our trek and walked for a while before Lexan stopped in his tracks and cleared his throat. "

  show lexan embarrassed OM
  show merona t surprised
  ln "Merona, wait... Can we speak for a moment?"

  show lexan embarrassed
  show merona t embarrassed OM
  mk "Okay...?"

  show merona t embarrassed
  "We hung around farther back from everyone and continued following the others."

  show lexan embarrassed OM
  show merona t content
  ln "Merona, I've had an amazing time with you and the others on this trip."

  show lexan embarrassed OM CE
  show merona t surprisedBlush
  ln "I've noticed something though, and feel free to correct me if I'm wrong..."

  show lexan embarrassed OM
  ln "Do you-"

  show lexan surprisedBlush
  show merona t surprisedBlush OM
  mk "I like you."

  show lexan embarrassed
  show merona t surprisedBlush
  "Dumping out the words that had been wreaking havoc in my over-cluttered mind felt like freeing myself extra breathing room."

  show lexan blushSmile
  show merona t embarrassedSmile
  ln "..."

  show lexan blushSmile OM
  ln "I figured."

  show merona t surprisedBlush
  ln "And I... like you too."

  show lexan sad OM
  show merona t sad
  ln "But I'm your teacher, and you're my student."

  show lexan serious OM
  show merona t nervous
  ln "There is another option though..."

  show lexan sadSmile OM
  show merona t surprised
  ln "When you're finished journeying, and I'm not your teacher anymore... Would you be willing to start seeing each other again?"

  #(Player choice)
  show lexan sadSmile
  menu:
    "Yes.":
      pass
    "No.":
      jump lbl_ending_academy_B_no

  play music music_romance
  show lexan surprisedBlush
  show merona t sadSmile OM
  mk "Well now I can't wait to be done with journeying."

  show lexan laugh
  show merona t grin
  ln "*laugh* I think travelling through Diolacov is way more exciting than being in a relationship with me."

  #TODO [fade in CG 
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg MeronaLexanRomance3
  mk "We'll see. When I'm finished, I'll compare notes. Each have their own merits!"

  scene cg MeronaLexanRomance1
  "He shook his head."

  scene cg MeronaLexanRomance2
  ln "You're being too nice."

  scene cg MeronaLexanRomance3
  mk "Would you ever want to go travelling for so long?"

  scene cg MeronaLexanRomance2
  ln "I don't know... I've been in Laneo forever. This is the farthest I've been away."

  scene cg MeronaLexanRomance3
  mk "Maybe I could show you some of my favorite places in the country once I'm back."

  scene cg MeronaLexanRomance2
  ln "Yeah... I'd like that."


  play music music_title
  #TODO [fade back to former scene
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest33
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan content:#; right
    yalign 1.0
    xalign 0.75
  show lexan at walkBounce
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content:#; left
    yalign 1.0
    xalign 0.3
  show merona at walkBounce
  "Lexan and I continued walking together, ambling along the road and watching the world around us."
  
  jump lbl_ending_journey_end  

label lbl_ending_academy_B_no:
  play music music_recollections
  show lexan worried
  show merona t worried OM
  mk "I don't know, Lexan..."

  show merona t sad OM
  mk "I'm going to be gone for so long, and we won't be in contact at all."

  show lexan sad
  show merona t determined OM
  mk "This won't work out, and I don't want you to keep waiting. We should move on from each other and focus on other things."

  show lexan sad CE
  show merona t sad
  "Lexan nodded, closing his eyes."

  show lexan sadSmile OM
  show merona t sadSmile
  ln "That's fine."

  show lexan content OM
  show merona t surprised
  ln "Thanks for being such a wonderful person to be around though, Merona. I had a lot of fun on this journey, and I wish you the best in your future."

  show lexan content
  show merona t content
  "I smiled."

  show merona t content OM
  mk "Likewise."

  play music music_title
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg ocean
  "Lexan walked forwards and joined Kreita and Rett's ongoing conversation. I remained in the back and stared out over the cliff and at the horizon line of the ocean and sky."


  jump lbl_ending_journey_end  

label lbl_ending_journey_C:                                 

  #TODO [C PATH

  play music music_piano
  #TODO [fade in CG ocean
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg ocean
  mi "At least I have a little more time to spend with these guys while we head back."

  mi "Travelling becomes difficult because you're always missing some other place. You never truly feel at home."

  "I'm going to miss Laneo so much, but as long as there are forests and nature around, there'll always be a piece of home with me. And who knows? Maybe one day, a tree will become my new friend."

  play music music_title
  #TODO [fade in CG ANewJourney
  "In exchange for giving up the familiar, I might discover something I wouldn't get anywhere else."


label lbl_ending_journey_end:                                     
  #TODO [fade in CG ANewJourney#; only path A and B
  if (currentPath == "A"):
    scene cg ANewJourney with fade
  if (currentPath == "B"):
    scene cg ANewJourney with fade
  "It's a new life, a new adventure, and..."

  "Dare I say a new journey?"

  jump lbl_END


  #########################################################"\
label lbl_ending_royal:
  #"A - ROYAL ENDING"
  #TODO [FINAL








  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. A path's storyline is red. B path's storyline is blue. C path's storyline is green. If two paths share the same text, it will be in pink."
  #"-----------------------------------------------------------"
  #(8/22/17)
  #TODO [FINAL

  play music music_Ill_be_right_behind_you_Josephine
  #TODO [Sound:fallInDirt
  scene cg castleGate
  show wagon:#; right, always behind the characters
    yalign 1.0
    xalign 1.0
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t grin#; center
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita grin2 behind merona:#; left from Merona
    yalign 1.0
    xalign 0.35
  $ renpy.transition(slow_dissolve, layer="master")
  show rett grin behind merona:#; right from Merona
    yalign 1.0
    xalign 0.65
  "Kreita and Rett went in to hug me at the same time, causing all three of us to crash down."

  show merona t sadSmile
  show kreita sadSmile OM
  kh "We're going to miss you so much, Merona! Don't forget about us!"

  show kreita sadSmile
  show rett content OM
  rt "This isn't our last goodbye though-we'll try to visit Calil as much as we can!"

  #TODO [move the characters up to normal height again
  show merona t sadSmile OM
  show rett sadSmile
  mk "Aw, guys..."

  $ renpy.transition(slow_dissolve, layer="master")
  show boyen content behind merona:#; right from Merona where Rett was
    yalign 1.0
    xalign 0.7
  $ renpy.transition(slow_dissolve, layer="master")
  show rett content:#; right from Boyen
    yalign 1.0
    xalign 0.9
  show merona t grin
  show kreita content
  show rett content
  "Boyen patted my head."


  show boyen content OM
  bg "Don't forget to take it easy and relax once in a while, Merona. The cooking here is probably way better than mine, so give me some tips when I see you again."

  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria gentle OM behind merona:#; left from Merona where Kreita was
    yalign 1.0
    xalign 0.35
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita grin:#; left from Cimaria
    yalign 1.0
    xalign 0.13
  show merona t content
  show boyen content
  show rett smirk
  ck "If you ever need our help, do not hesitate to reach out to us. We'll always be willing to lend a hand for anything."

  show merona t surprised
  show cimaria wink
  "Cimaria winked and put her arm around me, squeezing my shoulder."

  show merona t grin
  show cimaria content OM
  show boyen grin
  show kreita grin2
  show rett grin
  ck "I'm sure no healer here has as much experience dealing with monster wounds as I am."

  $ renpy.transition(slow_dissolve, layer="master")
  show duran t annoyed:#, left from Kreita
    yalign 1.0
    xalign -0.03
  show merona t content
  show cimaria content
  show boyen content
  show kreita content
  show rett content
  "Duran rolled his eyes."

  show duran t annoyed OM
  show cimaria grin
  dt "That'll surely boost your resume..."

  $ renpy.transition(slow_dissolve, layer="master")
  show lexan content OM:#; right from Rett
    yalign 1.0
    xalign 1.18
  show duran t content
  show cimaria gentle
  ln "Come to the academy anytime. You'll always be a student there, and feel free to find me if you need more tutoring."

  show merona t sadSmile
  show lexan sadSmile
  show duran t sadSmile
  show cimaria sadSmile
  show boyen sadSmile
  show kreita sadSmile
  show rett sadSmile OM
  rt "Alright everyone, we should get going. It's a long way back to Laneo..."

  show rett worried
  rt "..."

  show merona t worried
  show lexan worried
  show duran t worried
  show cimaria worried
  show boyen worried
  show kreita worried
  show rett worried OM
  rt "Send our regards to Prowen, Merona."

  show merona t verySad
  show lexan sad
  show duran t sad
  show cimaria sad
  show boyen sad
  show kreita sad
  show rett sadSmile
  "I nodded, already feeling the tears well up in my eyes."

  play music music_newBegin
  show merona t sadSmile OM
  show lexan sadSmile
  show duran t sadSmile
  show cimaria sadSmile
  show boyen sadSmile
  show kreita sadSmile
  show rett grin
  mk "One last hug from everyone?"

  show merona t grin CE
  show lexan grin CE
  show duran t grin CE
  show cimaria grin CE
  show boyen grin CE
  show kreita grin CE
  show rett grin CE
  "Everyone gathered around me and huddled together, squishing me right in the center. I felt like I was about to burst, both physically and emotionally."

  show merona t content
  show lexan grin
  show duran t grin
  show cimaria grin
  show boyen grin
  show kreita grin
  show rett grin
  "In a muffled voice, I blurted out the last words I wanted to say to them."

  show merona t happy OM
  mk "You guys were the best people I could have gone on a journey with, and I'm so happy that I did this whole thing."

  show merona t sadSmile OM
  show lexan sadSmile
  show duran t sadSmile
  show cimaria sadSmile
  show boyen sadSmile
  show kreita sadSmile
  show rett sadSmile
  mk "I've grown in so many ways I couldn't have imagined all because of everyone here. We've had troubling times and moments where we felt helpless, but we made it through them."

  show merona t content OM
  show lexan content
  show duran t content
  show cimaria gentle
  show boyen content
  show kreita content
  show rett content
  mk "Look where we are now! It's amazing what we've accomplished."

  show merona t happy OM
  #TODO [In path B: CS lexan blushSmile#; In path A and C: CS lexan grin
  #TODO [In path A: CS duran t blushSmile#; In path B and C: CS duran t grin
  if (currentPath == "A"):
    show duran t blushSmile
    show lexan grin
  if (currentPath == "B"):
    show duran t grin
    show lexan blushSmile
  if (currentPath == "C"):
    show duran t grin
    show lexan grin
  show cimaria grin
  show boyen grin
  show kreita grin
  show rett grin
  mk "Thank you, thank you, thank you."

  show merona t laugh
  #TODO [In path B: CS lexan blushSmile OM#; In path A and C: CS lexan laugh
  #TODO [In path A: CS duran t blushSmile OM#; In path B and C: CS duran t grin OM
  show cimaria laugh
  show boyen happy2
  show kreita laugh
  show rett laugh
  "The group unknotted from each other's arms and laughed."

  show merona t blushSmile
  show lexan grin
  show duran t content
  show boyen happy OM
  show cimaria gentle
  show kreita grin
  show rett smirk
  bg "We should be thanking you too, Merona."

  show boyen content OM
  bg "Everyone here went on their own personal journeys, and you were definitely a big part of it."

  show merona t grin
  show cimaria gentle OM
  show boyen grin
  ck "Thank you, Merona."

  show cimaria gentle
  show kreita happy
  kh "Thanks!"

  #TODO [In path B: CS lexan blushSmile OM#; In path A and C: CS lexan content OM
  if (currentPath == "A"):
    show lexan content OM
  if (currentPath == "B"):
    show lexan blushSmile OM
  if (currentPath == "C"):
    show lexan content OM
  show kreita grin
  ln "Thank you."

  show lexan grin
  show duran t surprised
  show rett content OM
  rt "Thanks, Merona."

  show duran t embarrassed OM
  show rett grin
  dt "...Thank you, Merona."

  show merona t sadSmile
  show lexan sadSmile
  show duran t sadSmile
  show cimaria content
  show boyen content
  show rett laugh
  rt "Alright, no more water works. We really ought to be moving along."


  #if (currentPath == "C"): 
  #if ((AChoiceCount < 2) and (BChoiceCount < 2)):
  #  jump lbl_ending_royal_C
    
  if (AChoiceCount >= 2):
    jump lbl_ending_royal_A
  if (BChoiceCount >= 2):
    jump lbl_ending_royal_B
    
  jump lbl_ending_royal_C
    
label lbl_ending_royal_A:
  #TODO [A PATH

  play music music_piano
  show rett content
  #TODO [fade out everyone except for Duran and Merona
  $ renpy.transition(slow_dissolve, layer="master")
  hide kreita
  hide cimaria
  hide boyen
  hide rett
  hide lexan
  hide wagon
  show merona t content
  show duran t embarrassed:
    yalign 1.0
    xalign 0.25
  "I waved the group off and watched them walk a few paces ahead. Before the guards could fully shut the door, someone slammed it with his hands and stopped it from fully closing. "

  show merona t surprised
  show duran t embarrassed OM
  dt "Wait, Merona! Don't go yet."

  show duran t embarrassed
  "The baffled guards allowed the panting, tomato-faced Duran in."

  show merona t embarrassed
  show duran t embarrassed OM
  dt "I... I..."

  show merona t surprised OM
  show duran t embarrassed
  mk "Duran?"

  show merona t grin
  show duran t determined OM
  dt "Um... I told the others I'd be back in a few minutes."

  show merona t embarrassed
  show duran t angryBlush
  "He side-eyed the guards next to us."

  show merona t blushSmile
  show duran t worried OM
  dt "Can we go somewhere a little more private?"



  #TODO [fade in CG royalGardens
  $ renpy.transition(slow_dissolve, layer="master")
  show cg RoyalGardens behind merona
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t embarrassedSmile:#; right
    yalign 1.0
    xalign 0.65
  show duran t embarrassed:#; left
    yalign 1.0
    xalign 0.35
  "I nodded and led him out to the nearby royal gardens. Hydrangeas were in bloom, basking in the warm rays of sunlight while they accompanied the two of us. Duran took a deep breath and looked straight into my eyes. "

  show merona t surprisedBlush
  show duran t embarrassed OM
  dt "You know I like you, right?"

  show merona t worried
  show duran t worried OM
  dt "We haven't had many chances to spend time together alone in the past few weeks of our journey, but..."

  show merona t blushSmile
  show duran t embarrassed OM
  dt "I really, really like you."

  show merona t worried
  show duran t sad OM
  dt "Since you're staying here, I know that we won't be able to see each other very often or even at all until a long time from now."

  show merona t sadSmile
  show duran t determined OM
  dt "But I'm okay with that. I'm okay with waiting. Until we grow up and become boring adults."

  show merona t serious
  show duran t worried OM
  dt "Are you okay with waiting?"

  show duran t worried
  #(Player choice)
  menu:
    "Yes.":
      pass
    "No.":
      jump lbl_ending_royal_A_no
    
label lbl_ending_royal_A_yes:

  play music music_romance
  show merona t blushSmile OM
  show duran t surprised
  mk "I think we'll become very interesting adults and have exciting lives together."

  $ renpy.transition(slow_dissolve, layer="master")
  scene cg MeronaDuranRomance1
  "Duran broke out into a relieved grin and pulled me into a hug."

  scene cg MeronaDuranRomance2
  dt "I promise I won't be such a jerk in the future."

  scene cg MeronaDuranRomance3
  mk "If you break it, I'll still help you become a little nicer."

  scene cg MeronaDuranRomance2
  dt "*laugh* I'll need all the help I can get."

  dt "Next time we see each other, I'm gonna be so much taller than you too."

  play music music_title
  scene cg MeronaDuranRomance1
  "I shook my head."

  scene cg MeronaDuranRomance3
  mk "We'll see."

  #TODO [fade back to scene from before
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg RoyalGardens
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t blushSmile:#; right
    yalign 1.0
    xalign 0.65
  show duran t blushSmile:#; left
    yalign 1.0
    xalign 0.35
  hide duran
  "He waved me off, promising to write me every month, and ran back out to the group while little sparks flew out from his fingertips. "
  jump lbl_ending_royal_end

label lbl_ending_royal_A_no:
  play music music_recollections
  show merona t sadSmile OM
  show duran t sad
  mk "Duran... We're going to change so much and forget about each other if we're so far apart for this long."

  show merona t sad OM
  show duran t nervous
  mk "I like you, too. But I don't think this can work out."

  show merona t sad
  show duran t neutral OM CE
  "He nodded, taking a deep breath in and out."

  show merona t worried
  show duran t sadSmile OM
  dt "I get it..."

  show merona t sadSmile
  show duran t neutral OM
  dt "Have fun here, Merona. You deserve this opportunity, and... You're doing the right thing."

  show merona t surprised
  show duran t blushSmile OM
  dt "*laugh* I don't know if I'll ever find someone as crazy as you."

  show merona t serious
  show duran t embarrassed
  "I shrugged."

  show merona t happy OM
  show duran t surprised
  mk "You attract crazy. I'm sure you're gonna find someone crazier who'll love being with you."

  show merona t grin
  show duran t content
  $ renpy.transition(slow_dissolve, layer="master")
  hide duran
  "After exchanging our last round of goodbyes, Duran rushed out and rejoined the group."

  play music music_title
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content#; center
  "I sat down on one of the garden's benches and admired the bundles of flowers all around. The me from a year ago never would have pictured myself ever living in an estate as grand as this one."
  jump lbl_ending_royal_end

label lbl_ending_royal_B:                                              

  #TODO [B PATH
  play music music_piano
  #TODO [fade out characters except Lexan and Merona
  $ renpy.transition(slow_dissolve, layer="master")
  hide kreita
  $ renpy.transition(slow_dissolve, layer="master")
  hide cimaria
  $ renpy.transition(slow_dissolve, layer="master")
  hide boyen
  $ renpy.transition(slow_dissolve, layer="master")
  hide rett
  $ renpy.transition(slow_dissolve, layer="master")
  hide duran
  $ renpy.transition(slow_dissolve, layer="master")
  hide wagon
  show merona t surprised
  show lexan determined OM
  ln "Hold on-you guys go ahead. I have one more thing that I need to say to Merona."

  show merona t embarrassed
  show lexan determined
  "My breath hitched, but I quickly tried to resume normal breathing again."

  show merona t embarrassedSmile
  mi "Don't overthink this, Merona."

  show merona t embarrassed
  show lexan embarrassed OM
  ln "Can we go somewhere more private?"


  #TODO [fade in CG royalGardens
  $ renpy.transition(slow_dissolve, layer="master")
  show cg RoyalGardens behind merona
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t surprised:#; left
    yalign 1.0
    xalign 0.3
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan embarrassed:#; right
    yalign 1.0
    xalign 0.75
  "I nodded and led him out to the nearby royal gardens. Hydrangeas were in bloom, basking in the warm rays of sunlight while they accompanied the two of us."

  show lexan blushSmile
  "Lexan turned to me and paused for a second before giving me a sheepish smile."

  show merona t surprisedBlush
  show lexan embarrassed OM
  ln "Sorry. This is not a very appropriate time to discuss this with you, but... I wanted to address this before we parted ways."

  show merona t embarrassedSmile
  ln "Please correct me if I've misinterpreted things, but I have a feeling that you..."

  show merona t embarrassedSmile OM
  show lexan surprisedBlush
  mk "I like you."

  show merona t embarrassed
  show lexan embarrassed
  "I blurted out the words before I could think of anything else. They had been jumping around the back of my mind for a while, causing a relentless mess that could never clean itself up."

  show lexan sadSmile
  ln "..."

  show merona t embarrassedSmile
  show lexan sadSmile OM
  ln "That's what I thought."

  show merona t sad
  show lexan sad OM
  ln "I'm your teacher, and you're my student. We can't do anything reckless, for the sake of both of us."

  show merona t surprisedBlush
  show lexan embarrassed OM
  ln "But know that I... Feel the same way."

  show lexan embarrassed CE
  "He swallowed a big gulp down his throat."

  show merona t blushSmile
  show lexan blushSmile OM
  ln "When you're no longer a student and leave the castle, would you be willing to... try seeing each other?"

  #(Player choice)
  show lexan blushSmile
  menu:  
    "Yes.":
      pass
    "No.":
      jump lbl_ending_royal_B_no

label lbl_ending_royal_B_yes: 
  play music music_romance
  show merona t blushSmile OM
  show lexan surprisedBlush
  mk "As long as it's not for tutoring."

  show merona t embarrassedSmile
  show lexan surprisedBlush OM
  ln "*laugh* I promise I won't tutor you, but only if you don't want it. There still might be some things I could teach you."

  #TODO [fade in CG MeronaLexanRomance3
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg MeronaLexanRomance3
  mk "Actually, by that time, I might be the one teaching you things. I'm gonna learn so much about monsters while I'm here. I can't wait to tell you about it."

  scene cg MeronaLexanRomance1
  "He grinned."

  scene cg MeronaLexanRomance2
  ln "Looking forward to it."

  ln "You could become the first master mage specializing in monsters."

  scene cg MeronaLexanRomance3
  mk "Maybe! But there may be no more need for one once I'm finished with my time here."

  mk "Besides, I'd get too distracted by this other genius water master mage to ever complete my studies."

  scene cg MeronaLexanRomance1
  "Shaking his head, Lexan flashed me one last smile. Time stood still in this moment."

  play music music_title
  #TODO [fade back to former scene...
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg RoyalGardens
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t blushSmile:#; left
    yalign 1.0
    xalign 0.3
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan blushSmile:#; right
    yalign 1.0
    xalign 0.75
  $ renpy.transition(slow_dissolve, layer="master")
  hide lexan
  "He waved me goodbye before scurrying back to the group."
  jump lbl_ending_royal_end

label lbl_ending_royal_B_no: 
  play music music_recollections
  show merona t sadSmile OM
  show lexan sadSmile
  mk "Lexan... I don't think we should happen."

  show merona t sad OM
  mk "Me staying at the castle is the perfect opportunity for us to move on from each other and focus on other stuff. Our work. Your career. My education. Ourselves."

  show merona t worried OM
  mk "This is for the best."

  show merona t worried
  "He nodded."

  show merona t sadSmile
  show lexan sadSmile OM
  ln "I completely understand."

  show merona t surprised
  show lexan content OM
  ln "Before I go, let me thank you for teaching me so many things too. I really enjoyed spending time with you, and I know you are going to soar in your future."

  show merona t laugh
  show lexan grin
  mk "*laugh* No guarantee about that, but I will do my best."

  show merona t content
  $ renpy.transition(slow_dissolve, layer="master")
  hide lexan
  "He gave me his final goodbye and jogged out the door, back to the group and back to Laneo."

  play music music_title
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content#; center
  "I sat down on one of the garden's benches and admired the bundles of flowers all around. The me from a year ago never would have pictured myself ever living in an estate as grand as this one."
  jump lbl_ending_royal_end

label lbl_ending_royal_C: 
  #TODO [C PATH
  play music music_piano
  show merona t content
  $ renpy.transition(slow_dissolve, layer="master")
  hide kreita
  hide cimaria
  hide boyen
  hide rett
  hide duran
  hide lexan
  hide wagon
  "The group walked out, equipped with a new wagon, courtesy of the crown, and I watched them until they became another unidentifiable speck down the road."

  show merona t determinedGrin
  mi "Like they said, this isn't the final goodbye."

  show merona t grin
  mi "I'm already looking forward to the stories we'll tell each other when we meet again!"

  show merona t sadSmile
  mi "Nonetheless, I'm going to miss them so much."

  play music music_title
  #TODO [fade in CG 
  scene cg ANewJourney with fade
  "I pivoted away from the door and strolled up the stairs to my new room, where I would be spending the next few years of my life in. The me from a year ago never would have pictured myself ever living in an estate as grand as this one."


label lbl_ending_royal_end:

  #TODO [fade in CG ANewJourney#; only path A and B
  if (currentPath == "A"):
    scene cg ANewJourney with fade
  if (currentPath == "B"):
    scene cg ANewJourney with fade
  "It's a new life, a new adventure, and..."

  "Dare I say a new journey?"

  jump lbl_END

