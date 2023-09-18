
  
  #-----------------------------------------------
label lbl_chapter2:
  if (currentPath == "A"):
    call lbl_PathA_2_0 from _call_lbl_PathA_2_0
  if (currentPath == "B"):
    call lbl_PathB_2_0 from _call_lbl_PathB_2_0
  if (currentPath == "C"):
    call lbl_PathC_2_0 from _call_lbl_PathC_2_0   
  
  #-----------------------------------------------
  #"A2.1"
  #TODO [FINAL
  #"The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. The path's storyline is in blue."
  #"-----------------------------------------------------------"
  #(Taking place while walking in the forest during the early afternoon)
  $ renpy.transition(slow_dissolve, layer="master")
  play music music_SoT
  #TODO [Fade from black
  scene cg forest10
  show rett pouty OM#; in the center
  show wagon#; in front of Rett please
  rt "Ugh, there's more fallen trees ahead. I swear, there must be some kind of tree hater on the loose."
  show rett pouty
  #TODO [fade in CS merona t serious#; on the right side
  show merona t serious at right
  $ renpy.transition(slow_dissolve, layer="master")
  "We no longer detected a definable path to follow.-the soil was almost untouched by people, except for occasional animal tracks. Now we had to be more alert of what we were stepping on."
  show merona t content
  mi "It's a little more \"natural\" out here, but it isn't that bad, right?"
  #TODO [fade in CS cimaria neutral OM; left side behind Rett - rather close to him
  show cimaria neutral OM behind rett:
      xalign 0.35 
      yalign 1.0
  $ renpy.transition(slow_dissolve, layer="master")
  ck "If you're careful you should be okay. Though I must admit, we have been seeing them quite often."
  show merona t surprised OM
  show cimaria neutral
  mk "Those trees don't even look like they have scratchy or peeling bark on them. At least from where we're at right now. The others back there weren't so nice on the skin."
  show merona t surprised
  #TODO [fade in CS duran t sad OM#; at the very left end
  show duran t sad OM at left behind wagon
  $ renpy.transition(slow_dissolve, layer="master")
  dt "Yeah, but a person can only take so much of trying to walk without tripping or ripping up their skin. And it's even worse when you're like me and have to carry all this junk on my back. It's so hard to do. Really hard."

  show merona t worried
  show duran t sad
  mi "These past few days, we've been noticing that the land was getting more and more... unused? It's a little strange seeing how this route we're taking is supposed to be used more often, but it's as if there's no major usage at all."
  show merona t shocked
  mi "I hope we're not lost."
  show merona t serious
  show cimaria serious
  show rett neutral
  show duran t annoyed
  "We got to the area of thick fallen trunks that did, indeed, have rough bark on the surface."
  show merona t sadSmile
  "I can just hear the inward groans of everyone piercing my eardrums."
  show merona t sad
  "What's most difficult about crossing them is not that we have trouble doing it, but that the cart can be a pain to lift over and not spill over."
  show merona t disappointed
  "And boy, did it spill over a lot."
  stop music fadeout 1.0
  show rett neutral OM
  rt "Okay guys, I need some help here again."

  #TODO [fade in CG fallenTrunks
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg fallenTrunks #with fade
  "Everyone gathered around their own section of the cart and prepared themselves. Kreita, Lexan, and Duran handled the front, which was the open side. They slowly lifted it over the first tree and got it over without it falling over too far."
  mi "Luckily, this group of trees have their trunks closer together, so it's not as hard to keep it up and moving."
  "We managed to get it over without making too big of a scene, and it was back to flat ground."
  play music music_Green_Leaves
  #TODO [fade in CG forest11
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest11 #with fade
  #TODO [fade in CS kreita happy#; center
  show kreita happy
  kh "Yay! Nothing fell off. I feel really accomplished now."
  show kreita content
  #TODO [fade in CS cimaria surprised#; left from Kreita, rather close please
  show cimaria surprised behind kreita:
      xalign 0.35 
      yalign 1.0
  "Cimaria pointed off to the left."
  show cimaria content OM
  ck "Everyone, it's more cleared there. How about we walk along that area?"
  #TODO [fade in CS boyen neutral OM#; right from Kreita
  show boyen neutral OM behind kreita:
      xalign 0.75 
      yalign 1.0
  show cimaria content
  bg "It looks like it'd be easier."
  show kreita fierce OM
  show boyen neutral
  kh "We should definitely be there then."
  #TODO [fade in CS rett grin#; left from Cimaria
  show rett grin behind kreita:
      xalign 0.05 
      yalign 1.0
  show kreita fierce
  "Rett raised his fist into the air."
  show rett laugh
  show boyen content
  rt "Onwards!"
  #TODO [fade out the sprites but leave the CG please~
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest11 #with fade
  "Quickly, we got over there. Like Cimaria said, it was much more open. We could walk more freely and with some personal space."
  #"-------------------------------------------------------"
  if (currentPath == "A"):
    call lbl_PathA_2_1 from _call_lbl_PathA_2_1
  if (currentPath == "B"):
    call lbl_PathB_2_1 from _call_lbl_PathB_2_1
  if (currentPath == "C"):
    call lbl_PathC_2_1 from _call_lbl_PathC_2_1
    
  #"-------------------------------------------------------"
  stop music
  play sound sound_lionRoar
  scene cg monsterCat at ScrollUp#; please pan from bottom to top of the image #(height will be double than normally)
  mo "*Roar*"
  rt "Quick, everyone, watch out!"
  #(continued in next script)
  #"A2.2"
  #TODO [FINAL

  #(Continuation of 2.1)
  #scene cg monsterCat#; Continuation from before
  play music music_Future_Gladiator
  "The hunched over monster slapped aside the bushes along the trees and pounced up in the air, skidding down onto the dirt. The dust that rose clouded my vision, but I could still make out the shape of the creature."

  mi "Okay... stay calm. I can't stress out over this too much."

  mi "This could be my chance to try out what I did before. I can't exactly do it on command, but it can also come out naturally if I'm in a dire situation."

  mi "I shouldn't do something stupid and place myself in danger though. For now, it'd be best to simply help drive the monster away and if it comes down to needing to kill it, I'll have to do what I have to do."

  scene cg forest11
  show cimaria shocked OM#; at center please
  ck "No sudden movements from anyone."

  show cimaria shocked
  #TODO [fade in CS boyen scared OM#; left from Cimaria please
  $ renpy.transition(slow_dissolve, layer="master")
  show boyen scared OM behind cimaria:
      xalign 0.25 
      yalign 1.0
  bg "If we don't appear threatening... I'm sure that it'll go away with some guidance."

  #TODO [fade in CS merona worried OM#; right from Cimaria please
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t worried OM behind cimaria:
      xalign 0.75 
      yalign 1.0
  show boyen scared
  mk "That's how it is with normal animals, but I don't know if it'd apply to monsters. Even wilder normal animals can be hard to control or lead away."

  #TODO [fade in CS rett aggressive OM #; right from Merona please
  $ renpy.transition(slow_dissolve, layer="master")
  show rett aggressive OM behind cimaria:
      xalign 0.9 
      yalign 1.0
  show cimaria surprised
  rt "If that's the case, then it might be the best to attack and wound it so that it goes away."

  #TODO [fade in CS lexan determined OM#; left from Boyen please
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan determined OM behind cimaria:
      xalign 0.15 
      yalign 1.0
  show rett aggressive
  show cimaria serious
  ln "We need to have a plan for that, if we're going along with it."


  play music music_movement
  scene cg monsterCat:
    yalign 0.0
  play sound sound_lionRoar
  "The monster lunged forward and began crawling towards us. I tensed up. Glancing at my surroundings, I tried finding things I could use my ability to help."

  mi "If my ability is labeled as plant and animal life \"manipulation\", then I should be able to manipulate the plants to move by my control, right? I don't have any experience in this at all, but I think I've heard it being doable before."

  mi "The problem is that I need to have some kind of feeling of its life flow before going through with it. My enhancer would help me, but I'd have to drink such an amount that would probably be unsafe on the first try."

  show cg forest11 #and CSs from before the CG monsterCat; except for lexan determined #(no OM)
  show cimaria serious
  show boyen scared behind cimaria:
      xalign 0.25 
      yalign 1.0
  show merona t worried OM behind cimaria:
      xalign 0.75 
      yalign 1.0
  show rett aggressive behind cimaria:
      xalign 0.9 
      yalign 1.0
  show lexan determined behind cimaria:
      xalign 0.15 
      yalign 1.0
  show kreita aggressive OM at center:
      xalign 0.45 
      yalign 1.0
  #TODO [fade in CS kreita aggressive OM, in the center in front of Cimaria
  kh "Everyone, don't move. I'll try to distract it, and then attack it."

  play music music_uplifting
  show merona t scared OM
  show kreita aggressive
  mk "By yourself? Is that okay for you?"

  show merona t serious
  show kreita aggressive OM
  kh "I know what I'm doing. And if any of you move, there's a higher chance of you getting attacked with the weapons I'm using, so it'd be best to stay where you are."

  show rett aggressive OM
  show kreita aggressive
  show boyen worried
  rt "Kreita, I can help you too. I know your methods."

  show rett aggressive
  show kreita aggressive OM
  kh "That's mainly for animals, not monsters. I've witnessed what works against them and what doesn't. But I figure that you'll still try and help me."

  show rett smirk OM
  show kreita fierce
  show boyen content
  show merona t sadSmile
  rt "Of course. I can't lose my cousin to some monster now, can I?"

  show rett smirk
  show kreita fierce OM
  kh "Of course you can't. But as for the others, I highly recommend you to stay still."

  show lexan worried OM
  show kreita aggressive
  show boyen worried
  show merona t worried
  ln "Kreita, what if you can't weaken it? What if something doesn't work out?"

  stop music
  show lexan determined
  show kreita determined OM
  show boyen happy S
  show cimaria worried
  show merona t determined
  kh "Then we'll just have to do what we can. But for now, gamble some trust for me. I'm going to need it."

  scene cg monsterCat:
    yalign 0.0
  "The monster was, in a sense, somewhat quiet. The only hostility it gave was in its body language and its eyes. Perhaps staying still did prove to be effective."

  play music music_movement
  scene cg KreitaAttack
  "Kreita was one of the closer people to the monster. She eyed the monster briefly, and thrust one of her arms out. The monster got pushed back into a small space surrounded by fallen trees."

  play sound sound_lionRoar2
  play sound sound_airAttack
  "She swiped her arm down. The monster was getting smothered down by something invisible, and it was pushing it down to the point of the monster being unable to get up. I could hear its voice growling and straining."

  #TODO [fade to CG forest12
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest12
  show kreita aggressive
  "Kreita flipped around, wide-eyed with her brows furrowed."

  show kreita aggressive OM
  kh "Run now, before it rises again!"

  show kreita determined with Pause(0.5)#; start to move her up and down #(running) after #(half?) a second please
  
  show kreita determined at RunBounce # with Pause(0.5)
  "No one hesitated, and we all ran past her while Rett scurried to get a good hold of the cart, getting in the front. She pushed our backs forward, and thrust out her arms one last time before running to join us."

  #TODO [fade in CS merona t nervous OM#; animated moving up and down please
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t nervous OM behind kreita:
    xalign 0.7
    yalign 1.0
  show merona at RunBounce
  mk "Kreita, what exactly did you do!?"

  show kreita determined OM
  show merona t nervous at RunBounce
  kh "Don't ask any questions right now, Merona! Just focus on getting out of here for now!"

  stop music fadeout 1.0
  show kreita determined
  show merona t surprised at RunBounce
  mi "There's no point in arguing back with her and forcing her to tell me."
  #TODO [fade out the sprites please, Merona first, then Kreita
  $ renpy.transition(slow_dissolve, layer="master")
  hide merona with Pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")
  hide kreita
  "We kept running, the dust of the drier dirt was puffing up and collecting on the folds of our clothes. I could hear everyone's heavy breathing and wheezes."

  play music music_Pride
  #TODO [fade in cg_sky1
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg_sky1
  show clouds at leftright #, moving from left to right please~
  mi "What exactly was Kreita's ability again? Wind manipulation? Air pressure manipulation? I'm not entirely sure on what she did, but it did look like it involved those elements."

  mi "She's a hunter though. Those kinds of magical abilities aren't particularly common for that job."

  #TODO [fade in CG forest13
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest13
  show boyen sweaty
  "Boyen was panting as he slowed down and stopped to point somewhere."

  show boyen sweaty OM
  bg "I see a house over there!"

  #TODO [fade in CG forestHouse
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forestHouse
  "Sure enough, there was a small wooden house past the trees, peeking right through the gaps of the tree trunks. I sighed, relieved to be able to stop."

  bg "Even if the monster followed us, we should at least hide somewhere. That house should be a good location."

  kh "I guess that's what's best. We probably lost it anyways. I don't know how good its sense of smell is, but I'm going to assume that it's pretty good. Oh well, let's just go."

  "We went at walking speed now, and everyone was gradually getting more energy. The monster seemed to be out of sight, and we all relaxed."

  play music music_recollections
  scene cg forest13
  show cimaria worried OM
  ck "Is anyone hurt? Does anyone need treatment from me?"

  #TODO [fade in CS duran worried OM#; left from Cimaria
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t worried OM:
    yalign 1.0
    xalign 0.25
  show cimaria surprised
  dt "I think you might want to look at something for me."

  show duran t neutral
  show cimaria worried OM
  ck "Do you need me to do it right now or can you wait until we get to the house?"

  show duran t neutral OM
  show cimaria gentle
  dt "Meh, I can wait."

  #(Continued in next script)
  #"A2.3"
  #TODO [FINAL

  #"The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. The path's storyline is in blue."

  #"------------------------------------------------------"

  #(Continuation of 2.2)
  #play music music_recollections#; continuation from 2.2
  show cg forest13
  #(positions as before:)
  show duran t neutral
  show cimaria serious OM
  ck "If you say so. But be careful with it."

  #TODO [fade in CS boyen sweaty OM, right from Cimaria
  
  $ renpy.transition(slow_dissolve, layer="master")
  show boyen sweaty OM:
    yalign 1.0
    xalign 0.75
  show cimaria serious
  bg "Let's hurry. We can't take too many risks."

  play music music_SoT
  #TODO [fade in CG forestHouse
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forestHouse
  "We all waddled to the house, careful not to make any sudden noises and to avoid anything in our way. "

  "It's good that we happened to chance upon this house, even if we're technically not completely safe. At least we can use it as a resting stop and possibly stay overnight. No one's majorly hurt either, so it's still okay. I wonder what happened to Duran though."

  "As we approached the house, it appeared in relatively good shape. It was no five story brick building of course, but it didn't look like it was about to collapse any second. There probably wasn't any resident either because of the location and the state of the house."

  mi "That's a little questionable-having a house right out in the middle of the forest. However, it's a rather small one story wooden building, so maybe whoever built it used it whenever he or she felt like getting away from people. Pretty possible explanation."

  "We didn't hesitate to roll inside. The house was holding everyone nicely, and the cart's wheels were wiped down a bit before being brought in."

  play music music_Pride
  scene cg forestHouse inside
  show rett neutral OM#, center
  rt "Everyone's inside? Okay. We probably need a person or two to stay on watch outside."

  #TODO [fade in CS cimaria serious OM#; left from Rett
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria serious OM:
    yalign 1.0
    xalign 0.25
  show rett worried
  ck "Where's Duran? I don't see him here. He was just with us..."

  #"-------------------------------------"

  #"-------------------------------------------------------"
  if (currentPath == "A"):
    call lbl_PathA_2_3 from _call_lbl_PathA_2_3
    jump lbl_chapter2_3_optionalEnd
  if (currentPath == "B"):
    call lbl_PathB_2_3 from _call_lbl_PathB_2_3
  if (currentPath == "C"):
    call lbl_PathC_2_3 from _call_lbl_PathC_2_3
    
label lbl_chapter2_3_optional:

  #OPTIONAL AFTER HERE#"

  show merona t serious
  #TODO [fade in CS lexan neutral OM#; right from Merona
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan neutral OM:
    yalign 1.0
    xalign 0.95
  #TODO [fade in CS kreita sceptical#; left from Cimaria
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita sceptical:
    yalign 1.0
    xalign 0.1
  ln "We can wait a little longer for him I suppose. If he doesn't come out here shortly, that's when we should start getting worried."

  play music music_recollections
  show rett neutral
  show lexan neutral
  show cimaria neutral
  show kreita neutral
  "Everyone nodded."

  show rett neutral OM
  show kreita content
  rt "Kreita, can I talk to you about some things about the monster?"

  show rett neutral
  show kreita content OM
  #TODO [fade both Kreita and Rett out
  $ renpy.transition(slow_dissolve, layer="master")
  hide rett
  hide kreita
  kh "Sure."

  show merona t content
  #TODO [fade in CS boyen content OM#; center
  $ renpy.transition(slow_dissolve, layer="master")
  show boyen content OM
  bg "I'll get some of our supplies in."

  show boyen content
  show cimaria neutral OM
  ck "I'll prepare for Duran a little."

  #TODO [fade out Boyen
  $ renpy.transition(slow_dissolve, layer="master")
  hide boyen
  show cimaria neutral
  show merona t surprised
  mk "..."

  ln "..."

  show merona t worried
  mi "I hope he's okay, wherever he is. He's probably in this house, just minding his own business, so maybe it's good that we aren't searching for him."

  play music music_Cool_Steel_Breeze
  show merona t surprised
  show cimaria surprised
  show lexan surprised
  #TODO [fade in CS duran t annoyed#; center
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t annoyed
  dt "*cough*"

  show cimaria neutral OM
  show merona t content
  show lexan neutral
  ck "Duran?"

  show cimaria neutral
  show merona t grin
  show duran t annoyed OM
  dt "I'm here."

  show cimaria worried OM
  show merona t serious
  show duran t annoyed
  ck "Do you still need me to check up on you?"

  show cimaria surprised
  show lexan sceptical
  show duran t neutral OM
  dt "Nah, I'm fine right now. Took care of it myself."

  show cimaria worried OM
  show merona t surprised
  show duran t neutral
  ck "Are you sure? What happened anyway?"

  show cimaria serious
  show lexan worried
  show duran t neutral OM
  dt "Just burned my hand a little. Nothing too big. It's not causing me any pain now, and I've had burns before. This is nothing."

  show cimaria serious OM
  show merona t surprised
  show duran t neutral 
  ck "If you say so... Just continue being careful, okay?"

  show cimaria annoyed
  show merona t sadSmile#; fade out
  show lexan confused
  show duran t neutral OM
  dt "Whatever. I'll keep doing what I'm doing."
  #TODO [fade out Cimaria and Duran
  #TODO [move Lexan to the center
  $ renpy.transition(slow_dissolve, layer="master")
  hide cimaria
  hide duran
  hide lexan
  show lexan confused
  
label lbl_chapter2_3_optionalEnd:
    
  #"--------------------------------"
  play music music_Pride
  scene cg forestHouse inside
  #TODO [erase the former CSs and show...
  show lexan content#; center
  "Lexan cleared his throat."

  show lexan content OM
  ln "Now that Duran's okay, we can discuss more on what our plans are for tonight."

  #TODO [fade in CS rett neutral OM#; slightly left from Lexan
  $ renpy.transition(slow_dissolve, layer="master")
  show rett neutral OM:
    yalign 1.0
    xalign 0.25
  show lexan content
  rt "If we can, we should stay in this house for a night. It'll be safer in here after all, and more comfortable too."

  #TODO [fade in CS kreita content OM#; at the very left of the scene
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita content OM at left
  show rett neutral
  kh "I second that! We can continue our normal tasks too, and all shall be well for tomorrow if nothing interferes. We'll still need a night watch and have the door blockaded. Don't forget about the closing the curtains of the windows!"

  show kreita content
  mi "Oh good, I'll get to sleep in an actual house. Not that sleeping outside is terrible, but if we stay here, everyone can finally get some good rest without worrying so much."

  #TODO [fade in CS kreita content OM#; right from Lexan
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria content OM:
    yalign 1.0
    xalign 0.75
  ck "I also agree. It will not interfere with our travel plans either, so it's for the best if we stay here for now until morning."

  show lexan laugh
  show cimaria content
  show rett smirk
  ln "Let's get started then."

  #TODO [erase the former CSs and show...
  scene cg forestHouse inside
  show boyen surprised#; center
  "Boyen was looking around, and he lit up as he saw something."

  show boyen happy
  bg "There's a fireplace over there. We can still light a fire in here."

  #TODO [fade in CS merona t content OM#; left from Boyen
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content:
    yalign 1.0
    xalign 0.25
  show boyen grin
  mk "I can get some wood outside if you'd like."

  show merona t content
  show boyen happy
  bg "That'd be lovely! Are you okay with going outside though? It still might be dangerous."

  play music music_meronatheme
  show merona t content OM
  show boyen content
  mk "I think it's fine now. Don't worry, I'll be okay. I won't wander off too far, so even if something does happen, you guys will hear it. I can take care of myself too! I survived a monster attack before after all."

  #TODO [fade in kreita grin#; right from Boyen
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita grin:
    yalign 1.0
    xalign 0.75
  show merona t surprised
  "Overhearing it, Kreita snorted."

  show kreita content OM
  show merona t sadSmile
  kh "Tch. Yeah, by accident. But you'll still be okay."

  show kreita grin2
  show merona t sadSmile OM
  show boyen grin
  mk "Thanks for your support, Kreita..."

  show kreita happy
  kh "Anytime."

  scene cg forest13
  show merona t serious
  "I headed out the door and scanned around for any suspicious shadows or shapes. No unusual sounds were alerting my ears, and everything looked in place."

  show merona t grin
  mi "Everything's clear. Time to gather wood!"

  #(Continued in next script)


  #"A2.4"
  #TODO [FINAL

  #"The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. The path's storyline is in blue. The pink text means that that section is in one of the other scripts, and you don't have to record the other script for it."

  #"------------------------------------------------------"

  #(Continuation of 2.3)
  #play music music_meronatheme #(from before)
  #scene cg forest13 #(from before)
  show merona t content
  "I skipped over to the trees and began picking up whatever wood I could. It was slightly windy, and the breeze would occasionally tug on my hair."

  show merona t reflective
  mi "I wonder how much longer it'll be until we get to our destination. The days have been going by faster and faster to me, so sometimes I feel giddy about when we'll arrive. I've been learning well enough, and I think I'm getting good progress through."

  show merona t grin ER
  mi "The whole point of this journey was for me to do better on my studies and improve my skills with my ability, and I'd like to think that it's been working out well."

  #"------------------------------------------------------"

label lbl_chapter2_4_optional:
  if (currentPath == "A"):
    pass
  if (currentPath == "B"):
    call lbl_PathB_2_4 from _call_lbl_PathB_2_4
    jump lbl_chapter2_4_optionalEnd
  if (currentPath == "C"):
    pass
    
  play music music_Lafayette
  show merona t serious
  mk "Hm..."

  show merona t grin
  mi "Is there anything else I can get? Maybe there are some plants I'll be able to recognize and use. It'll show some proof that I actually learned something, right? Or if not, I'll try and find some berries or other edible plants."

  show merona t surprised
  mi "Am I feeling brave enough to get a small animal and bring it back to be slaughtered?"

  stop music fadeout 1.0
  show merona t sadSmile
  mi "..."

  show merona t disappointed OM
  "I shuddered internally.  "

  show merona t disappointed
  mi "Not today."

  play music music_life
  show merona t content
  mi "I'll just look for plants that I've learned of and those that we could use. I don't think there's a water source nearby here, so it'd also be best if I don't wander off somewhere looking for one and lose our spot."

  show merona t grin ER
  "My eyes flicked over to the left and I spotted clusters of dark circular sprouts growing out of the ground."

  show merona t happy
  mk "I knew that I was able to learn something! I forgot your name, but I'm still able to recognize you, so that's all that counts."

  show merona t content
  #(Varpal is pronounced VAR-pull)
  mi "Not to mention that I remember some of your attributes! How about I name you instead? I think... Varpal... sounds good."

  show merona t sadSmile
  mi "Well, I'm pretty sure that I'll forget about it soon, but for now, that name works."

  show merona t content at Crouch#; animation: move her down on the y axis #(approximately) 200 pixels and let her rest there please
  "I squatted down and plucked out a few from the ground. The roots were releasing from the soil with ease, and I placed the plants into a spare empty pouch I had."

  #TODO [Move Merona's CS up to it's normal height position please~
  show merona t content at center
  mi "That plant apparently is supposed to help slow infections, so perhaps I'll give it to Cimaria later."

label lbl_chapter2_4_optionalEnd:
  #"------------------------------------------------------"
  #TODO: Pathchoice option here?
  play music music_Lafayette #(for all paths#; just continue if A path is picked)
  "I went further into the forest and looked around for more wood. We had enough unused wood from before, so I think it should be okay to stop now."

  show merona t worried
  mi "A quick run, but a good one. I better hurry back into the house before I get too paranoid and or actually get mauled by a wild animal or the unexpected tree branch right in my face."

  show merona t content
  "I jogged back to the building, and popped my head in."

  play music music_meronatheme
  scene cg forestHouse inside
  show merona t happy
  mk "I'm back! And I've got the wood."

  #TODO [fade in boyen content#; left from Merona
  $ renpy.transition(slow_dissolve, layer="master")
  show boyen content:
    yalign 1.0
    xalign 0.25
  show merona t content
  "Boyen was the first to notice me."

  show boyen happy
  bg "Oh good! Come in, come in. I can boil some of our food now. I'm glad the fireplace has a latch for a pot. And Duran?"

  show boyen content
  "Duran was sitting on the floor against the wall. He looked like he was trying to sleep, or at least just trying to rest. He jerked, but kept his eyes half-closed. He grumbled a little."

  #TODO [fade in CS duran t tired OM#; right from Merona
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t tired OM:
    yalign 1.0
    xalign 0.75
  dt "What do you need?"

  play music music_Afterglow
  show boyen content OM
  show duran t tired
  bg "If it's alright with you, can you start a fire for me? You're probably quite bored just sitting there."

  show boyen content
  show duran t surprised OM
  show merona t grin
  dt "Just start a fire? Sure, doesn't sound that bad."

  show boyen content OM
  show duran t neutral
  show merona t content
  bg "Thank you! Merona, can you set the wood in there?"

  show boyen content
  "I nodded and hopped over to throw the pieces in. Boyen followed and hooked a medium-sized open pot onto the latch inside."

  show boyen happy
  show merona t grin
  show duran t annoyed
  bg "Good, the wood and pot don't take that mushroom. Duran, go ahead."

  show boyen grin
  show duran t neutral
  "Duran crawled over to the fireplace and put his hand out, the flames bursting. The smell of burning wood invaded my nose."

  show boyen happy
  show merona t sadSmile
  show duran t annoyed EL
  bg "Thanks again. I'm very a-peas-ed with how it turned out."

  show boyen grin
  show merona t grin ER
  show duran t annoyed OM S
  dt "That was almost funny, and I almost laughed. Ha... Ha ha... Ha..."

  play music music_Pride
  show boyen happy CE S
  show merona t content
  show duran t neutral
  "The others joined us in the room."

  #TODO [remove the CSs and show...
  #TODO [fade in CS cimaria neutral OM#; center
  scene cg forestHouse inside
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria neutral OM
  ck "Is everything in place? The door is blocked, everything we have is inside, and the curtains are closed?"

  #TODO [fade in CS rett content OM#; left from Cimaria
  show cimaria neutral
  $ renpy.transition(slow_dissolve, layer="master")
  show rett content OM:
    yalign 1.0
    xalign 0.25
  rt "I think we're covered. We can actually let the fire keep burning even after the cooking is done, and blow it out right before we go to sleep. All that's left is for us to wait and take the night watch, and we should be safe. The supplies are in, no one's missing, and we can leave early tomorrow morning."

  #TODO [fade in CS lexan content OM#; right from Cimaria
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan content OM:
    yalign 1.0
    xalign 0.75
  show cimaria content
  show rett smirk
  ln "We can get on with our duties and rest at night. I'm glad everything worked out."

  #TODO [fade in CS merona t happy#; slightly left from Cimaria #(can overlap)
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t happy:
    yalign 1.0
    xalign 0.35
  mk "Until tomorrow morning then!"

  scene bg black with fade


  #"A2.5"

  #TODO [FINAL
  #(taking place walking in the forest a few days later, in mid morning to early afternoon)

  play music music_title
  #TODO [fade from black
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest14
  #TODO [ fade in CS merona t disappointed OM#; center
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t disappointed OM
  mk "You know, it was really comfortable sleeping in that house. I had almost forgotten what it was like to have walls around me."

  #TODO [fade in CS cimaria gentle OM#; right from Merona
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria gentle OM:
    yalign 1.0
    xalign 0.75
  show merona t sadSmile
  ck "Still thinking about that? I have to agree that being indoors is a whole lot more relaxing than out in the open."

  #TODO [fade in CS rett neutral OM#; right from Cimaria
  $ renpy.transition(slow_dissolve, layer="master")
  show rett neutral OM behind cimaria:
    yalign 1.0
    xalign 0.95
  show cimaria content
  show merona t content
  rt "Even if it's been a few days since we've left it, it's definitely so much easier to live in a house. Makes me want to try and find more empty houses every time we stop."

  show rett neutral
  show merona t reflective
  mi "But unfortunately, not everyone has built a house out in the forest that is empty and available for use."


  #TODO [fade in CS duran t neutral OM#; left from Merona
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t neutral OM:
    yalign 1.0
    xalign 0.25
  show cimaria neutral
  show merona t surprised
  dt "Do any of you know where we are right now? As in the actual location?"

  show duran t neutral
  mi "Hm... It's been several days since we've departed. I think around one to two weeks already. We should be out of the province already."

  #TODO [fade in CS kreita happy#; left from Duran
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita happy behind duran:
    yalign 1.0
    xalign 0.05
  show cimaria content
  show merona t content
  kh "It takes about six weeks to get to where we are heading. If we've been moving at the expected speed, then we're probably a third of the way there."

  show kreita pouty
  show duran t annoyed OM
  show rett smirk
  show cimaria neutral
  show merona t surprised
  dt "Aren't you guys supposed to know things like the layout of the land or whatnot? Can't you tell exactly by what you see from our surroundings?"

  show kreita fierce
  show duran t annoyed
  show rett wink OM
  show merona t sadSmile
  rt "We aren't walking maps, and we don't go this direction too often, so no."

  show kreita grin
  show duran t annoyed OM
  show rett content
  dt "Fine."

  show kreita happy
  show duran t neutral
  show merona t content
  kh "We haven't bumped into any rivers yet, so that's a definite sign we're going the right direction. The nearest one to our starting point is in the northeast direction, so we've been going northwest, which is the correct way."

  show kreita grin
  show duran t neutral OM
  dt "Whatever you say."

  show duran t neutral
  show merona t happy
  mk "If we know that we're going the right way, we'll eventually find ourselves in a nearby city or town that's on the correct path. For now, we can just keep going."

  stop music fadeout 1.0
  play sound sound_rustling
  scene cg bushRustle
  qq "*rustle rustle*"

  "Everyone stopped and looked behind for whatever made the sound."

  play music music_eerie
  ln "Did anyone hear that?"

  ck "There's something in the bushes. That must be the source of the sound."

  bg "Another... monster?"

  kh "The sound was too small. No way it was a monster. Those things are usually way larger too, so we would've been able to see it behind a bush if it was."

  mk "It's a small animal then. Or something like that."

  dt "Anyone willing to be a sacrifice and look at it?"

  play music music_Up_Kilkenny
  #TODO "All CS positions as in the beginning of the chapter please~"
  scene cg forest14
  show duran t surprised:
    yalign 1.0
    xalign 0.25
  show rett wink OM:
    yalign 1.0
    xalign 0.95
  show kreita grin2:
    yalign 1.0
    xalign 0.05
  show cimaria serious:
    yalign 1.0
    xalign 0.75
  show merona t nervous
  rt "Since you offered Duran, you can do it."

  show rett smirk
  show duran t flabber OM
  dt "What?! No."

  show duran t flabber
  show kreita fierce OM
  kh "You suggested it; you do it."

  show cimaria worried
  show merona t sadSmile
  kh "Unless you want me to push you."

  show rett neutral
  show kreita fierce
  show duran t angry OM
  dt "Don't make me burn your face."

  show kreita fierce OM
  show duran t angry
  show cimaria serious
  kh "We have a little someone who's a healer here, so even if you do, it wouldn't work. Tough luck, pal."

  show kreita fierce
  show duran t angry OM
  dt "I still won't do it. I don't care. You can't make me."

  show duran t angry
  show merona t laugh
  mk "Duran, it's not a monster. Just go and look at it."

  show duran t angry OM
  show merona t sadSmile
  dt "Then why don't you look at it yourself."

  show kreita grin
  show duran t angry
  #"fade out Kreita's and Duran's CSs please~"
  $ renpy.transition(slow_dissolve, layer="master")
  hide kreita
  hide duran
  
  show cimaria surprised
  show merona t surprised
  show rett grin
  "Kreita shook her head and chuckled. She grabbed Duran by the armpits and lifted his feet off the ground."

  show cimaria neutral
  show merona t grin ER
  kh "Since you feel scared and need a little adult supervision, I'll help you."

  dt "Let. Go. Of. Me."

  show merona t sadSmile
  dt "...Please."

  show rett laugh
  show cimaria serious
  rt "I'm surprised, you know how to be semi-polite."

  show rett grin
  kh "Alright, let's be a big boy and go and see what the scary thing behind the bushes is."

  scene cg forest15
  
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita grin
  show duran t angry:
    yalign 1.0
    xalign 0.45
  #TODO [fade in CS kreita grin#; center
  #TODO [fade in CS duran t angry#; mostly centered but a slight bit left from Kreita #(something like the middle of the image at 45-48% x of the screen)
  "She carried him in front of the bush and set him down right in front of it."

  play music music_Aces_High
  show kreita fierce OM
  kh "Look over it."

  show kreita fierce
  show duran t angry OM
  dt "No."

  show kreita grin
  show duran t annoyed
  "Kreita smirked."

  show kreita fierce OM
  show duran t surprised
  kh "Do you want me to count to three?"

  show kreita fierce
  show duran t annoyed OM
  dt "What? Ha, that is seriously the stupidest thing ever. You think that will work on me? I'm not five years old."

  show kreita fierce OM
  show duran t annoyed EL
  kh "Have it your way."

  play music music_Up_Kilkenny
  show kreita happy
  show duran t annoyed
  kh "One."

  show kreita grin
  show duran t annoyed EL
  dt "..."

  show kreita sceptical
  show duran t annoyed OM
  dt "No."

  show kreita sceptical OM
  show duran t annoyed EL
  kh "Two."

  show kreita sceptical
  show duran t annoyed
  dt "..."

  show kreita fierce
  show duran t nervous
  kh  "......"

  show kreita pouty
  show duran t annoyed
  dt  "..."

  show kreita angry
  show duran t angry OM
  dt "Still, no."

  show kreita angry OM
  show duran t angry
  kh "Last chance: two and a half."

  show kreita pouty
  show duran t annoyed OM
  dt "Whatever."

  show kreita fierce OM
  show duran t annoyed
  kh "Have it your way."

  play music music_Greek_Dance
  scene cg KreitaGrab
  "Kreita grabbed him by his hood and dragged him forward before going on to lift him up by his armpits again."

  kh "Just take a good look. I'm with you."

  mk "You know... that kind of reminds me of how a mother cat grabs onto its offspring."

  ck "That's... a fitting analogy for it."

  "Kreita and Duran were looking over the bush for a few seconds now, but they didn't say anything yet or move."

  mi "I wonder what's over there. It sure is captivating them..."

  scene bg black with fade
  "Duran's \"straitjacket\" yanked him a little forward, but he ended up crashing into the bush."

  play sound sound_fallInDirt
  kh "AH! Sorry, Duran!"

  stop music fadeout 1.0
  #TODO [fade in CG forest15
  #TODO [fade in CS kreita grin2 S with the background #(center as before) and fade her out
  
  $ renpy.transition(slow_dissolve, layer="master")
  show cg forest15
  show kreita grin2 S with Pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")
  hide kreita
  "Kreita went over the bush as well and got a hold of him while pushing branches down. Duran kept staring wide-eyed and scowled at whatever lay there."

  "Everyone hurried to the bush to see what it was."

  #(this double question mark represents Prowen)
  #TODO [fade in CG ProwenAwakes
  scene cg ProwenAwakes
  qq "*groaning*"

  ln "It's..."

  play music music_Words
  ln "A... man?"

  #(continued in next script)
  #"A2.6"
  #TODO [FINAL



  #(Continuation of 2.5)
  #play music music_Words #(from before)
  #scene cg ProwenAwakes #(as before)
  #(question mark representing Prowen)
  qq "Um..."

  #TODO [fade in CG forest15
  
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest15
  #"with the CG fade in..."
  show prowen tired:#; center but positioned about 250pixels lower #(as he sits)
    yalign 2.5
    xalign 0.5
  show kreita grin2 S:#; left from Prowen
    yalign 1.0
    xalign 0.25
  show duran t neutral:#; left from Kreita
    yalign 1.0
    xalign 0.0
  "He squinted up at everyone surrounding him. Without saying anything else, he put his palms down and sat himself up."

  show prowen tired OM
  qq "Uh... *yawn* who are you? Need something or what, since some of you collapsed onto me..."

  show prowen neutral
  show kreita lol
  show duran t annoyed EL
  kh "*cough* Well..."

  show kreita neutral OM
  kh "We just happened to be walking around and all, but then... we thought that there was something here where you were, and... yeah. Now we're here."

  stop music fadeout 1.0
  show prowen surprised
  show kreita pouty
  show duran t angry OM
  dt "She means that I was forcibly  pushed down into the bush and landed on top of you."

  show prowen appalled
  show kreita laugh S
  show duran t angry
  kh "Ha ha, ha...Yeah."

  show duran t neutral
  "He stared at them for a few seconds, not responding."

  show prowen tired
  show kreita neutral
  mi "Hey, if I was woken up like that, I probably wouldn't be saying too much either. Not to mention that he practically got attacked."

  play music music_Sugar_On_My_Tongue
  #TODO [fade in cimaria worried OM#; right from Prowen
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria worried OM:
    yalign 1.0
    xalign 0.70
  show kreita worried
  ck "Um, we're quite sorry for what had happened. Are you alright?"

  show cimaria worried
  show prowen neutral
  show duran t bored
  "The man's eyes flicked over to Cimaria, his face neutralizing."

  show cimaria neutral
  show prowen neutral OM
  show kreita content
  qq "Nothing really seems to be wrong with me so, no. I'm fine. Thank you."

  show prowen neutral
  show kreita content OM
  kh "Phew, was worried a little. But you were sleeping here. Do you need any help at all? Where are you from?"

  show prowen neutral OM
  show kreita content
  "He lolled his head onto his shoulder and opened his mouth without saying anything for a moment."

  show prowen tired OM
  show kreita neutral
  qq "*sigh* I could ask you the same thing. I don't see a lot of people around here usually."

  play music music_Travel_Light
  show prowen neutral
  #TODO [fade in merona t content OM#; right from Cimaria
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content OM:
    yalign 1.0
    xalign 1.1
  mk "Oh, we're traveling to a city in the northern regions. We came from Laneo if you've heard of it."

  show prowen neutral OM
  show merona t content
  qq "Traveling. Okay. But what's the reason?"

  show prowen surprised
  show merona t content OM
  show kreita grin
  show duran t tired
  mk "It's for educational purposes. To get first-hand knowledge on the environment and the life here."

  show prowen surprised OM
  show merona t grin
  qq "That's... different."

  #TODO [fade in CS lexan neutral OM#; between Cimaria and Merona please
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan neutral OM:
    yalign 1.0
    xalign 1.0
  show prowen surprised
  show merona t content
  show kreita content
  ln "So then, what about you?"

  show lexan neutral
  $ renpy.transition(slow_dissolve, layer="master")
  show prowen neutral:#; please move his sprite now up to the normal y-position
    yalign 1.0
    xalign 0.5
  "The man stood up and stretched out his arms and back. He exhaled."

  show prowen neutral OM
  show merona t grin
  show kreita sceptical
  show duran t neutral
  qq "You can say that I'm a traveler. Though maybe not for the same reasons you all are traveling for."

  #TODO [fade in CS boyen neutral OM#; between Kreita and Duran please
  $ renpy.transition(slow_dissolve, layer="master")
  show boyen neutral OM:
    yalign 1.0
    xalign 0.1
  show prowen neutral
  bg "Do you have a home?"

  show boyen neutral
  show prowen neutral OM
  show merona t sadSmile
  show kreita grin S
  show duran t evilGrin
  qq "Yeah. But right now, I'm only temporarily traveling for... work. I usually stay in the inns, but I must have been too tired to find one nearby and ended up falling asleep here."

  show boyen content OM
  show prowen neutral
  bg "Oh."

  show lexan neutral OM
  show boyen content
  show merona t serious
  show kreita neutral
  show duran t bored
  ln "Where do you need to go?"

  show cimaria surprised
  show lexan surprised
  show prowen neutral OM
  qq "My destination isn't exact. I'm only moving forward, seeing what I can get."

  play music music_Cool_Steel_Breeze
  show cimaria gentle OM
  show lexan neutral
  show prowen surprised
  show merona t surprised
  show kreita content
  show duran t surprised
  ck "In that case... um, could I speak to the group privately for a moment?"

  show cimaria gentle
  show prowen tired OM
  qq "Psh. Whatever you need."

  scene cg forest16
  #TODO [fade in CS cimaria serious#; center
  #TODO [fade in CS rett neutral#; left from Cimaria
  #TODO [fade in CS kreita neutral#; left from Rett
  #TODO [fade in CS boyen content#; left from Kreita
  #TODO [fade in CS merona t surprised#; right from Cimaria
  #TODO [fade in CS duran t annoyed#; right from Merona
  #TODO [fade in CS lexan neutral#; right from Duran
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria serious:
    yalign 1.0
    xalign 0.5
  show rett neutral:
    yalign 1.0
    xalign 0.30
  show kreita neutral:
    yalign 1.0
    xalign 0.10
  show boyen content:
    yalign 1.0
    xalign -0.05
  show merona t surprised:
    yalign 1.0
    xalign 0.70
  show duran t annoyed:
    yalign 1.0
    xalign 0.85
  show lexan neutral:
    yalign 1.0
    xalign 1.2
  "Cimaria led us a few feet away before saying anything else, and we all huddled together on the other side of the path."

  show cimaria serious OM
  show kreita pouty
  show boyen sweaty
  ck "We've all been noticing how we're more alert right? Because now that we've seen a monster, every rustle of even small animals seems dangerous."

  show cimaria serious
  show rett neutral OM
  show merona t serious
  rt "We've only encountered one though."

  play music music_River_Meditation
  show cimaria serious OM
  show rett worried
  show duran t nervous
  show lexan worried
  show merona t worried
  ck "Yes, but we could encounter more."

  show cimaria worried OM
  show rett sceptical
  show kreita worried
  show boyen worried
  show merona t surprised
  show duran t tired
  ck "This person that we found also seems to have some troubles going on, and we could... help him out."

  show cimaria neutral
  "She raised her eyebrows briefly."

  "By helping him out, you mean..."

  show cimaria serious OM
  show rett neutral
  show kreita sceptical
  show merona t content
  show duran t neutral
  ck "Also by helping him out, we get extra help from him as well. If he's been sleeping in the forest like that before, it shows that he can handle it."

  show cimaria serious
  show rett surprised
  show kreita sceptical OM
  show duran t worried
  show lexan confused
  kh "So you're suggesting that we bring him along."

  show cimaria serious OM
  show kreita neutral
  show duran t annoyed
  ck "Yes."

  show cimaria neutral
  show rett neutral
  show kreita grin2 S
  show boyen scared
  show merona t sadSmile
  show duran t annoyed OM
  show lexan serious
  dt "So you're absolutely okay with taking along a stranger that we don't know much about and could be someone like... I don't know, a criminal. Yeah. It must be easy to be an adult."

  show cimaria neutral OM
  show boyen neutral
  show duran t annoyed
  show merona t serious
  ck "This is only a suggestion. We can travel with him for a short period of time, and then decide and offer if he'd like to continue with us. Think of it as a trial."

  show cimaria neutral
  show kreita neutral
  show merona t nervous
  show duran t neutral
  mi "It does sound shaky, but it could be not a bad plan. We'd have to be careful about it though. Who knows, he could be a murderer."

  show rett neutral
  show kreita worried
  show boyen worried
  show lexan serious OM
  ln "Risky. A risky trial."

  show cimaria serious OM
  show rett pouty
  show merona t surprised
  show duran t worried
  show lexan determined
  ck "We'd be capable of doing something if he happens to prove to be bad. And we can drop him if he truly is someone not to be around."

  play music music_newBegin
  show cimaria neutral
  show rett surprised
  show kreita determined
  show boyen content
  show merona t content OM
  show duran t flabber
  show lexan surprised
  mk "In my opinion... I think it's okay. Like she said, we don't have to keep him the whole time and can let him go his own way if we'd like. It's his choice too anyway."

  show cimaria content
  show rett content
  show boyen content OM
  show merona t content
  show lexan content
  bg "Let's just try it out."

  show cimaria content OM
  show boyen content
  show duran t surprised
  ck "Is everyone okay with it? If not, then we don't have to do it."

  show cimaria neutral
  show rett neutral
  show kreita neutral
  show duran t worried
  show lexan serious
  "Silence prevailed."

  show cimaria content OM
  show rett content
  show lexan content
  ck "I take that as no objections. Thank you."

  #TODO [fade in CG forest15
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest15
  #"with the CG fade in..."
  show prowen neutral#; center
  "We walked over to the man again."

  show prowen neutral OM
  #TODO [fade in CS cimaria content#; left from Prowen please
  hide cimaria
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria content in:
    yalign 1.0
    xalign 0.25
  qq "Yes? What is it?"

  play music music_piano
  show prowen surprised
  show cimaria content OM
  ck "We were contemplating over if you would like to join us on our trip, that is, if you yourself would want to. It'd be safer to travel in a group, and more helpful for everyone if there were more people."

  show prowen neutral
  show cimaria gentle
  mi "I wonder why he thinks we're asking him this. It's out of the blue for strangers to request people to join them after all, but we'll have to see."

  qq "..."

  show prowen neutral OM
  qq "So... you want me to come with you guys?"

  show prowen neutral
  show cimaria gentle OM
  ck "Yes. Again, it is only if you are willing to."

  show prowen sceptical OM
  show cimaria neutral
  qq "Are you going to make me do any specific things?"

  show prowen neutral
  show cimaria content OM
  ck "Only necessary tasks regarding survival, but other than that, no. You're free to do what you will."

  stop music fadeout 1.0
  show cimaria content
  qq "..."

  show prowen sceptical OM
  show cimaria neutral
  qq "Personally, I prefer being alone. I have things I need to do myself, but..."

  play music music_life
  show prowen sceptical
  show cimaria serious
  mi "Oh, there's a \"but\". Looks like what I think it is."

  show prowen neutral OM
  show cimaria content
  qq "...on your terms, I suppose that I can join your group."

  show prowen neutral
  show cimaria content OM
  ck "Alright then. You're allowed to leave whenever you'd like, but if you have your own things that you need to do, it would be courteous of you to inform us of your whereabouts."

  show prowen neutral OM
  show cimaria content
  qq "Yeah. Got it."

  show prowen neutral
  #TODO [fade in CS kreita neutral OM#; left from Cimaria please
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita neutral OM behind cimaria:
    yalign 1.0
    xalign 0.0
  kh "What's your name? Er, if you're okay with telling us."

  play music music_Main_Theme
  play sound sound_bell
  show prowen neutral OM
  show kreita content
  pm "Prowen. Prowen Mair."

  #(Continued in next script)
  #"A2.7"
  #TODO [FINAL
  #(Continuation of 2.6)
  #play music music_Main_Theme #(from before)
  #show cg forest15 #(from before)
  show prowen neutral#; center
  show cimaria gentle OM#; left from prowen as before
  ck "Thank you. I'm Cimaria Kinoten."
  #TODO [fade in CS merona t happy#; between Cimaria and Kreita please
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria gentle 
  show merona t happy:
    yalign 1.0
    xalign 0.10
  mk "I'm Merona Kovene."
  #TODO [fade in CS boyen happy#; right from Prowen please
  $ renpy.transition(slow_dissolve, layer="master")
  show boyen happy:
    yalign 1.0
    xalign 0.70
  show merona t grin
  bg "Boyen Grattis."
  #TODO [fade in CS duran t tired OM#; at the very right of the screen please
  $ renpy.transition(slow_dissolve, layer="master")
  show boyen content
  show duran t tired OM:
    yalign 1.0
    xalign 0.90
  
  dt "Duran Trist."
  hide kreita
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita happy behind merona:
    yalign 1.0
    xalign 0.0
  show duran t tired
  kh "Kreita Henik."
  #TODO [fade in CS lexan content OM#; right from Boyen please
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan content OM:
    yalign 1.0
    xalign 0.90
  show kreita grin
  ln "Lexan Nerion."
  #TODO [fade in CS rett wink OM#; between Lexan and Duran please
  $ renpy.transition(slow_dissolve, layer="master")
  show rett wink OM behind duran:
    yalign 1.0
    xalign 1.1
  show lexan content
  rt "Rett Toikas."
  show prowen forcedSmile OM
  show rett grin
  pm "Nice to meet you all."
  play music music_Travel_Light
  show prowen forcedSmile
  show lexan content OM
  ln "So are you ready to go right now? If you're feeling too tired, we can stay here for a bit."
  show lexan content
  show prowen neutral CE
  "Prowen shook his head."
  show prowen neutral OM
  pm "No. We can go."
  show prowen neutral
  ln "Alright then."
  show cimaria content OM
  ck "Just let us know when you have to stop, alright?"
  show cimaria content
  show prowen neutral CE
  pm "Mm hm."

  #(Continued in next script)
  #"A2.8"
  #TODO [FINAL

  #"The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. The path's storyline is in blue. ----------------------------------------------------------"

  #(Continuation of 2.7)
  #play music music_Travel_Light #(from before)
  #TODO [fade in CG forest16
  #TODO [fade in CS merona t content#; center
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest16
  show merona t content
  "Everyone proceeded. Prowen dawdled around until he was at the back of the group, following us there."

  #"----------------------------------------------------------"

  if (currentPath == "A"):
    call lbl_PathA_2_8 from _call_lbl_PathA_2_8
  if (currentPath == "B"):
    call lbl_PathB_2_8 from _call_lbl_PathB_2_8
  if (currentPath == "C"):
    call lbl_PathC_2_8 from _call_lbl_PathC_2_8
  #"----------------------------------------------------------"
  
  #"A2.9"
  #TODO [FINAL

  #menu:
  #  "stop here"
  #  "stop":
  #      pass
  #  "stop":
  #      pass


  #"The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. The path's storyline is in blue. ----------------------------------------------------------"

  #(taking place in a clearing, resting and sitting on the ground around a fire at night)

  stop music
  play sound sound_nighttimeAmbience loop #TODO [to be prepared#; looped please
  #(Extra info: the nightFire CG will show the characters without faces around the camping fire, faces are named as characterAbbreviation NF#(=NightFire) expressionName "
  #"Prowen is separate so he can leave the scene later and Merona too in order to be shown separate from the BG later."
  #"Cimaria has no faces because she's seen from behind. >=3)

  $ renpy.transition(slow_dissolve, layer="master")
  #TODO [fade from black into...
  #scene cg nightFire at ScrollDown#; show at 100% size #(it is twice the HD size) starting from the top center, zoom out to 50% size and move the camera until the lower end is reached#; here's also an info image for the camera movement: https://drive.google.com/file/d/0By2EUlNeLO3Mbl9iOW5ERDRneVE/view?usp=sharing 
  show cg_composite nightFire_full at ScrollDown# behind cg # Show here to enable gallery
  #hide cg_composite
  #
  #show nightFire_BoyenKreitaLexanDuran at ScrollUpFromBottom
  ##show nightFire Prowen
  ##show nightFire Merona
  #show nightFire_campFire at ScrollUpFromBottom#; might be animated as a png sequence later if I have time :3
  #show nightFire_RettCimaria at ScrollUpFromBottom
  #
  ##TODO [Please place the facial expressions directly on top of the corresponding base layer - I'll just summarize them here for easier editing
  #show prowen nightFire open behind nightFire_RettCimaria at ScrollUpFromBottom
  #show boyen nightFire closed at ScrollUpFromBottom
  #show duran nightFire closed at ScrollUpFromBottom
  #show kreita nightFire closed at ScrollUpFromBottom
  #show lexan nightFire closed at ScrollUpFromBottom
  #show merona nightFire closed at ScrollUpFromBottom
  #show rett nightFire closed at ScrollUpFromBottom
  #
  ##TODO [The following characters have hair over their eyes/ eyebrows, so please place these above the expression layers:
  #show nightFire_BoyenKreitaLexanDuran_outlines behind prowen at ScrollUpFromBottom
  ##show nightFire Merona outlines
  ##show nightFire Rett outlines
  #
  #show nightFire_frontPlants at ScrollUpFromBottom
  pm "How long have you all been travelling for?"

  # sets the scene to the end of the animation
  hide cg_composite
  scene cg nightFire:
    yalign 1.0
  show nightFire_BoyenKreitaLexanDuran:
    yalign 1.0
  show nightFire_campFire:
    yalign 1.0
  show nightFire_RettCimaria:
    yalign 1.0
  show prowen nightFire open behind nightFire_RettCimaria:
    yalign 1.0
  show boyen nightFire closed:
    yalign 1.0
  show duran nightFire closed:
    yalign 1.0
  show kreita nightFire closed:
    yalign 1.0
  show lexan nightFire closed:
    yalign 1.0
  show merona nightFire closed:
    yalign 1.0
  show rett nightFire closed:
    yalign 1.0
  show nightFire_BoyenKreitaLexanDuran_outlines behind prowen:
    yalign 1.0
  show nightFire_frontPlants:
    yalign 1.0
    
  show prowen nightFire closed
  "I glanced at Prowen. The fire emphasized the contours and hollows of his face. He stared down into the burning wood."

  mi "I myself can't remember very well. When did we start again? I wrote dates in my journal and simply kept track of it that way, but who knows, I could be off."
  #show cimaria nightFire open
  ck "Not too long. About two weeks."

  show prowen nightFire open
  #show cimaria nightFire closed
  pm "How long do you expect to travel until you reach your destination?"

  show rett nightFire open
  show prowen nightFire closed
  rt "Three times the amount we've already gone."

  #TODO [fade out the night ambience and 
  stop sound fadeout 1.0
  play music music_Green_Leaves
  show rett nightFire closed
  mi "Already a third of the way there. I'm going to have to move along with my studies and really try to improve my skills more. Get fully off the enhancer. Be good without the enhancer. And then... boom, I've done what I needed!"

  show prowen nightFire open
  pm "I see."

  show kreita nightFire open
  show prowen nightFire closed
  kh "You're okay with staying that long, right? I mean, a month more is not exactly a short time."

  show rett nightFire open
  show kreita nightFire closed
  rt "What? Four weeks is nothing. It'll pass by really quick, and we're always on the move."

  show kreita nightFire open
  show rett nightFire closed
  kh "Don't be an overripe apple, Rett, and try to make it sound okay. It's still considerably a long time, especially since we're not doing that much except trying not to kill ourselves or starve to death."

  show boyen nightFire open
  show kreita nightFire closed
  bg "*laugh* We're all fine as it is though, right? I do agree that four more weeks is a bit on the longer end, but we should be fine."

  show prowen nightFire open
  show boyen nightFire closed
  pm "It's alright. If we end up finding a nearby city, I can leave."

  #show cimaria nightFire open
  show prowen nightFire closed
  ck "That's understandable. You are free to do what you will, so you may leave anytime you wish."

  #show cimaria nightFire closed
  mi "I'm not too sure what kind of jobs he can get with a memory manipulation ability, when it's not even his own memory that's getting affected. Perhaps his ability can do things like clearing foggy memories and helping with memory loss. That would be very useful."

  "He leaned back against a tree behind him and looked up at the sky."

  show prowen nightFire open
  pm "I'm going to get some sleep. Energize for tomorrow."

  show lexan nightFire open
  show prowen nightFire closed
  ln "Good night."

  show lexan nightFire closed
  show prowen nightFire closed CE
  "Prowen closed his eyes."

  show prowen nightFire open CE
  pm "Hopefully it will be."

  show prowen nightFire closed
  #TODO [fade out CS nightFireProwen and CS prowen nightFire closed at the same time please~
  $ renpy.transition(slow_dissolve, layer="master")
  #hide prowen
  hide prowen nightFire 
  "He got up and shuffled over to the sleep spot we chose for the night."
  
  
  #return #return to start
  jump lbl_chapter3

  #(Continued in next script)
