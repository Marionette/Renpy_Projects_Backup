label lbl_chapter8:
  #"A8.0"
  #TODO [FINAL

  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. A path's storyline is red. B path's storyline is blue. C path's storyline is green. If two paths share the same text, it will be in pink."
  #"-----------------------------------------------------------"
  #(Continuation of 7.9)

  play music music_Summer_Day
  scene cg LexanRainShield
  "Lexan took a deep breath and scanned over everyone. Looking at the sky, he raised his right arm forward, palms up, and concentrated on the rain. The droplets coming down by the wagon dodged Kreita's head and the vehicle instead of falling onto them."

  kh "Hey, I'm not getting pelted by rain anymore! Hooray for Lexan!"

  "He smiled and brought his other arm back to the rest of us behind him. We all huddled closer together as the rain redirected itself away from us as well."

  ln "I hope this makes walking easier. I will try to hold this up as long as I can."

  mi "Oh, this definitely makes walking a bit easier! Not to mention lighten up the mood a little-nothing like getting drenched in the rain to make you feel depressed."

  mi "Lexan has to keep holding his position though... I wonder how much effort this takes."

  #TODO [fade in...
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest27
  #(Positions as before)

  show prowen neutral:
    yalign 1.0
    xalign -0.1
  show boyen content:
    yalign 1.0
    xalign 1.1
  show cimaria worried:
    yalign 1.0
    xalign 0.2
  show merona t worried OM:
    yalign 1.0
    xalign 0.3
  show kreita content:
    yalign 1.0
    xalign 0.5
  show rett neutral:
    yalign 1.0
    xalign 0.7
  show lexan content:
    yalign 1.0
    xalign 1.0
  show duran t neutral:
    yalign 1.0
    xalign 0.1
  show wagon

  show duran t neutral at walkBounce
  show prowen neutral at walkBounce
  show lexan content at walkBounce
  show boyen content at walkBounce
  show cimaria worried at walkBounce
  show merona t worried OM at walkBounce
  show kreita content at walkBounce
  show rett neutral at walkBounce
  
  show rain movie
  mk "Lexan, are you sure you can keep your arms up for a while? It's probably going to get tiring pretty quickly..."

  show lexan content OM
  show merona t content
  ln "Maybe not for half an hour straight, but I should be able to last a few solid minutes. I would need a little time to reinvigorate both my arms and my ability. Dealing with rain can become quite taxing..."

  show lexan content
  show cimaria neutral
  "Kreita turned her head back to us."

  show kreita content OM
  show rett content
  kh "If you want, Lexan, you could trade places with me, and I'll create an air bubble around us or try to blow the rain away with some wind."

  show duran t annoyed
  show boyen grin
  show lexan grin
  show merona t sadSmile
  show kreita pouty OM
  show rett grin
  kh "Then again, pushing this wagon would also tire your arms out..."

  show duran t neutral
  show lexan laugh
  show merona t content
  show kreita content
  show rett content
  ln "*laugh* Thanks for the offer. I'll switch with you if needed, but for now, let's see how long I can last on my own."

  show boyen content
  show lexan content
  show merona t grin
  mi "I'll relish these few minutes of dryness. Perhaps we'll chance upon some kind of place to settle down soon too, so we won't have to worry about the rain's comeback on us."

  play music music_Lafayette
  show merona t sadSmile
  mi "For once, I want to see something besides trees..."

  show duran t annoyed OM
  show prowen surprised
  show boyen neutral
  show lexan neutral
  show cimaria serious
  show merona t surprised
  show kreita sceptical
  show rett smirk
  dt "It's so annoying having to be so close to you guys. We're all warm and moist-this is not a good time to be warm and moist."

  show duran t annoyed
  show prowen neutral
  show merona t serious
  show rett wink
  "Rett winked at Duran."

  show prowen grin
  show boyen grin2
  show lexan grin
  show cimaria grin
  show merona t grin
  show kreita grin2
  show rett wink OM
  rt "When is a good time to be warm and moist, then?"

  show duran t annoyed OM S
  show rett wink
  dt "Never if you're involved."

  show duran t annoyed
  show prowen content
  show lexan neutral
  show cimaria content
  show merona t grin CE
  show kreita content
  show rett content
  "I stifled a laugh and kept moving forward. Though we were all a bit too close for comfort, there was a cozy aspect to it. I felt connected to everyone."

  show duran t neutral
  show prowen neutral
  show boyen neutral
  show cimaria neutral
  show merona t content
  show kreita neutral
  "Another round of silence began, and there were still no signs of good stopping ground."

  show merona t serious
  mi "How long has it been since this storm started? I feel like it became heavier so fast. Why did the clouds hold in this much water for so long?"

  show merona t content
  mi "The good thing is that the plants on our wagon are getting lots of water. It'll save us some effort from watering them ourselves. The soil must be getting nice and nutrient-rich from all the fish we put in too!"

  "Duran cleared his throat."

  play music music_Dark_Red_Wine
  show duran t neutral OM
  show prowen surprised
  show boyen content
  show lexan surprised
  show merona t grin
  show kreita content
  show rett neutral
  dt "So, um... What were you saying again, Prowen? You never finished telling us your fun facts."

  show duran t neutral
  show prowen sceptical OM
  show lexan neutral
  show cimaria content
  show rett content
  pm "You're still interested?"

  show prowen sceptical
  "Duran shrugged."

  show duran t neutral OM
  show prowen neutral
  show cimaria neutral
  show merona t disappointed
  show kreita pouty
  dt "I mean, no one else has much to offer."

  show duran t neutral
  "Kreita twisted her head back again."

  show duran t annoyed
  show prowen forcedSmile
  show kreita pouty OM
  kh "Hey, we have plenty to offer! We've all got lots of spectacular fun facts!"

  show merona t serious
  show kreita angry
  "Duran rolled his eyes and ignored her."

  show duran t neutral OM
  show prowen neutral
  show kreita neutral
  dt "Anyways, Prowen..."

  show duran t neutral
  show prowen content OM
  show lexan content
  show cimaria content
  show merona t content
  show kreita content
  pm "Ha. I suppose if you insist..."

  show duran t content
  show prowen neutral OM
  pm "I'm a vagrant."

  pm "I'm... 38 years old."

  show prowen appalled
  "He furrowed his brows."

  play music music_life
  show prowen appalled OM
  show boyen grin
  show lexan sadSmile
  show cimaria grin
  show merona t sadSmile
  show kreita grin
  show rett grin
  pm "Damn, I'm almost 40..."

  show prowen neutral OM
  show boyen content
  show lexan neutral
  show cimaria neutral
  show kreita content
  show rett content
  pm "Uh..."

  show duran t grin
  show prowen serious OM
  show boyen grin2
  show merona t content
  pm "I like eating meat-any kind of meat, but beef especially."

  show duran t content
  show prowen neutral OM
  show boyen content
  show cimaria worried
  show merona t surprised
  show kreita surprised
  pm "Once, I stayed awake for three nights in a row."

  show cimaria neutral
  show merona t content
  show kreita content
  pm "Anything else you would like to know?"

  show prowen neutral
  mi "That was a decent amount of fun and fact in those fun facts. We ought to have a beef dinner with Prowen before he leaves."

  show boyen content OM
  show lexan content
  show cimaria content
  bg "You sound like you have a unique life, especially since you're so nomadic."

  show duran t neutral
  show prowen neutral CE
  show boyen content
  "Prowen shook his head."

  show prowen serious OM
  show boyen neutral
  show merona t serious
  show rett surprised
  pm "It's not that different from any other homeless person. My life is all about survival. I suppose that's what everyone's goal is, but living is less guaranteed for someone with my circumstances."

  play music music_Words
  show prowen neutral
  show boyen content
  show lexan determined
  show cimaria content OM
  show merona t content
  show kreita determined
  show rett content
  ck "Even so, know that we will ensure your survival while you travel with us."

  show prowen forcedSmile
  show cimaria sadSmile
  show rett content OM
  rt "Yeah. It'd be a shame if you were able to live on your own for all these years, but we just let you die!"

  show duran t neutral
  show prowen surprised
  show cimaria content
  show merona t content OM
  show rett smirk
  mk "You're basically a team member now, so you're not completely homeless."

  show duran t annoyed
  show prowen neutral
  show merona t content
  "Duran wrinkled his nose."

  show duran t annoyed OM
  show boyen neutral
  show lexan neutral
  show cimaria neutral
  show merona t surprised
  show kreita grin2
  show rett grin
  dt "Ew, don't call us a home."

  show duran t annoyed S
  show merona t content OM
  mk "Okay, we're not a home because we're not made of walls and a roof, but we are a home because-"

  show duran t annoyed OM S
  show lexan strict
  show cimaria annoyed
  show merona t disappointed
  show kreita grin
  dt "Cut the cheesefest before I do it myself."

  show duran t annoyed S
  mi "But I live for the cheesefest!"

  show prowen forcedSmile
  show lexan neutral
  show cimaria neutral
  show merona t serious
  show kreita content
  show rett content
  "Prowen gave us a faint smile."

  show duran t neutral
  show prowen forcedSmile OM
  show boyen content
  show lexan content
  show cimaria content
  show merona t content
  pm "What a lively bunch."

  show prowen forcedSmile
  show merona t laugh
  mk "*laugh* I hope we don't annoy you too mu-"

  stop music
  play sound sound_snarl
  scene bg black with fade
  "Lexan's arms immediately jerked down, but no water fell on us."

  "The colossal, winged creature hovering above us was already doing his job by blocking the rain."

  mi "Not again."

  #(Continued in 8.1)
  #"A8.1"
  #TODO [FINAL




  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. A path's storyline is red. B path's storyline is blue. C path's storyline is green. If two paths share the same text, it will be in pink."
  #"-----------------------------------------------------------"
  #(Continuation of 8.0)

  play music music_Future_Gladiator
  #TODO [no walking animations anymore please
  #TODO [fade from black
  $ renpy.transition(slow_dissolve, layer="master")
  show cg forest28
  show rain movie #(ongoing)
  show birdMonster:
    yalign 1.0
    
  show birdMonster at hover
  
  show rain movie
  "Everyone jolted to a stop. We could only stare up at the monster, watching its wings blow the rain away each time they beat down. But we couldn't stay paralyzed forever."

  mi "In a way, I don't feel so surprised to see this anymore. Is this the fourth monster I've ever seen? It's almost like I'm getting desensitized..."

  play sound sound_snarl

  mi "Being desensitized doesn't matter to this guy though."

  #TODO [move the monster's sprite upwards by 150px
  show birdMonster:
    linear 1.0 yalign 2.0
  show birdMonster at highHover
  "While scanning over everyone, the monster flapped higher into the sky. Lexan spun around and placed one hand on my shoulder and the other on Duran's."

  scene cg forest27
  #show prowen neutral:
  #  yalign 1.0
  #  xalign -0.1
  #show boyen content:
  #  yalign 1.0
  #  xalign 1.1
  #show cimaria worried:
  #  yalign 1.0
  #  xalign 0.2
  #show merona t worried OM:
  #  yalign 1.0
  #  xalign 0.3
  #show kreita content:
  #  yalign 1.0
  #  xalign 0.5
  #show rett neutral:
  #  yalign 1.0
  #  xalign 0.7
  #show lexan content:
  #  yalign 1.0
  #  xalign 1.0
  #show duran t neutral:
  #  yalign 1.0
  #  xalign 0.1
  #show wagon
  
  show lexan strict OM:#; center:
    yalign 1.0
    xalign 0.5
  show duran t flabber:#; a bit left from Lexan:
    yalign 1.0
    xalign 0.3
  show merona t shocked:#; a bit right from Lexan:
    yalign 1.0
    xalign 0.6
  ln "Take cover."

  play sound sound_crash
  show lexan strict
  #TODO [move Duran's and Merona's sprite quickly to the right while fading them out
  show merona:
    yalign 1.0
    parallel:
      linear 1.0 xalign -0.1
    parallel:
      linear 1.0 alpha 0.0
  show duran:
    yalign 1.0
    parallel:
      linear 1.0 xalign -0.1
    parallel:
      linear 1.0 alpha 0.0
  "Lexan thrust us into the edge of the forest just as the monster dived right towards our group. Its jaws snapped at the cart and pierced the heart of our garden, shattering the pots and plants we had nurtured."

  $ renpy.transition(slow_dissolve, layer="master")
  show kreita aggressive:#; left from Lexan
    yalign 1.0
    xalign 0.2 
  show rett aggressive:#; rightt from Lexan:
    yalign 1.0
    xalign 0.75
  play sound [ sound_airAttack, "<silence .1>", sound_rainAttack, sound_swordDraw] #- play the sounds one after another
  "Kreita shot out her hands, penetrating the monster with a gust of air and recoiling from the force. Lexan struck the creature with high speed rain while Rett unsheathed his sword."

  scene cg forest28
  show birdMonster:#; move position down to 200px lower than initially/ at the beginning of the chapter
    yalign 1.0
  show birdMonster:
    linear 0.2 yalign 0.5
  "The monster stumbled to the ground, but the hits barely took it down. It shook its body, splashing everyone with water, and prepared to charge forward again. I snapped my head to Duran."

  scene cg forest27
  show merona t scared:#; position 200px lower than normally#; right
    yalign 2.5
    xalign 0.6
  show duran t confused:#; position 200px lower than normally#; left
    yalign 2.0
    xalign 0.3
  mk "We can't just lie aroun-"

  show merona t shocked
  show duran t determined:#; move up back to normal Y position
    linear 0.2 yalign 1.0
    xalign 0.3
  "Before I could finish, Duran got up and raced over to join the rest of the gang. He looked back at me with fire in his eyes."

  stop music fadeout 1.0
  show duran t determined OM
  dt "Get up!"

  show merona t determined:#; move back to normal Y position
    linear 0.2 yalign 1.0
    xalign 0.6
  show duran t determined
  mi "No need to tell me twice."

  play music music_movement
  scene cg forest28
  show birdMonster:#; position 200px lower than initially/ at the beginning of the chapter
    yalign 0.5
  play sound sound_fireAttack
  show fireAttack movie
  pause(0.8)
  hide fireAttack
  show steam movie
  pause(1.24)
  hide steam
  "I scurried up from the mud and followed Duran's lead. He already shot a great burst of flames from his palms to the monster, but the monster's wet body steamed instead of catching fire. "

  show airAttack movie
  play sound sound_airAttack
  #TODO ["Shake" the monster's sprite left and right, e.g. similar to Pokemon battle animations
  pause(0.6)
  hide airAttack
  show birdMonster with hpunch
  "Another streak of air from Kreita hit the monster's legs, and it lost its balance. Looking more intense than I could ever imagine, Lexan turned to Duran and me."

  scene cg forest27
  show lexan shout#; center
  show duran t nervous:#; left
    yalign 1.0
    xalign 0.2
  show merona t sad:#; right
    yalign 1.0
    xalign 0.8
  ln "You two need to get back down there! We can't risk you two-"

  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria serious behind lexan:#; slightly right from Lexan
    yalign 1.0
    xalign 0.6
  show lexan surprised
  "Cimaria put a hand on Lexan's shoulder and glared at him."

  show cimaria serious OM
  show lexan serious
  ck "No, we need them."

  show cimaria determined OM
  show lexan worried
  ck "If we fail... Those two will be in a much worse predicament."

  scene cg forest28
  show birdMonster:#; position 200px lower than initially/ at the beginning of the chapter
    yalign 0.5
  $ renpy.transition(slow_dissolve, layer="master")
  show rett aggressive:#; right from birdMonster
    yalign 1.0
    xalign 0.9
  show swordAttack movie
  play sound sound_swordAttack
  pause(0.4)
  hide swordAttack
  "Rett dashed to the monster while it was down and stabbed near the base of the wing."

  play sound sound_snarl
  #TODO [Move CS birdMonster up by 200px and down again #(end position 200px lower than at beginning of chapter)
  show birdMonster:
    linear 0.3 yalign 1.0
  #TODO [Move Rett down by 200px 
  pause(0.2)
  show rett confused OM behind birdMonster:
    linear 0.2 yalign 2.5 
  "The monster lifted its wings and beat down hard, knocking away Rett. It hovered over his body, and its teeth grazed Rett's shoulder."

  play sound sound_fireAttack
  show fireAttack movie:#; place animation at the birdMonster's eyes
    xalign 0.7
    yalign 0.3
  pause(0.8)
  hide fireAttack
  show steam movie: #(after fireAttack on same spot)
    xalign 0.7
    yalign 0.2
  pause(1.24)
  hide steam
  show rett confused
  "Duran fired another round of flames, but this time, he aimed for the monster's eye..."

  #TODO [Move CS birdMonster to the left
  show birdMonster:
    linear 0.3 xalign -0.7
  show rett sceptical
  "...successfully making it jump back from Rett as well."

  #(Continued in 8.2)
  #"A8.2"
  #TODO [FINAL





  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. A path's storyline is red. B path's storyline is blue. C path's storyline is green. If two paths share the same text, it will be in pink."
  #"-----------------------------------------------------------"
  #(Continuation of 8.1)
  #play music music_movement #(from before)
  #scene cg forest28
  #show birdMonster#; position as in end of last chapter
  #show rett worried
  show rain movie #(ongoing)
  mi "Don't tell me that another round of venom just went into Rett's body..."

  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria determined:#; right from Rett
    yalign 1.0
    xalign 1.0
  "Right as Cimaria lunged forward, Rett jumped up and shook his head."

  show rett worried OM
  rt "I'm fine! I'm totally fine!"

  $ renpy.transition(slow_dissolve, layer="master")
  hide cimaria serious
  hide rett
  show rett aggressive:#; move the center
    yalign 1.0
    xalign 0.7
  show swordAttack movie: #(at the monster's position)
    yalign 0.5
    xalign 0.4
  play sound [sound_swordAttack, sound_snarl]#; Monster Snarling
  pause(0.4)
  hide swordAttack
  "He grasped his sword once more and dove to the monster, who was still recovering from Duran's attack. Rett stabbed the side of the bird creature's throat, eliciting a harsh screech from it."

  play sound sound_arrow
  show rett smirk
  "Before the monster could attack Rett, Kreita simultaneously shot two arrows on the other side of its throat, making it shriek and unfurl its wings. "

  show rett aggressive:#; move to the center
    yalign 1.0
    xalign 0.5
  #TODO [move birdMonster up by 300px
  show birdMonster:
    linear 0.3 yalign 2.0
  "Rett yanked his sword out from the flesh and dashed away as the monster flew up again. It twisted its neck around several times, but the arrows refused to dislodge. "

  play music music_Ecstasy_X
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita serious:#; right from Rett
    xalign 0.7
    yalign 1.0
  show rett neutral
  "Kreita whistled as Rett ran next to her."

  show kreita serious OM
  show rett sceptical
  kh "Looks like we'll need to target a few other spots before we can take it down."

  show kreita serious
  show rett sceptical OM
  rt "Base of skull, heart..."

  show kreita serious OM
  kh "And everywhere else. He may be big, but the more we stab him, the sooner he'll die."

  $ renpy.transition(slow_dissolve, layer="master")
  hide birdMonster
  show kreita fierce
  show rett sceptical
  "The monster hovered over the treetops, using the branches to pull out the arrows. Every so often, Kreita's eyes flicked over to it."

  show kreita fierce OM
  show rett confused
  kh "You could even cut off his wings if you want. Cut off a foot too. It'll disable him."

  play music music_Future_Gladiator
  show kreita fierce
  show rett confused OM
  rt "Geez, I'll just cut him to pieces. Why are you grinning now of all times?"

  show kreita fierce OM
  show rett confused
  "Kreita laughed right when the monster roared."

  play sound sound_snarl
  #TODO [fade in birdMonster#; left
  $ renpy.transition(slow_dissolve, layer="master")
  show birdMonster:
    yalign 1.0
    xalign -2.0
  show rett surprised
  kh "I live for chances like these. Literally."

  show kreita aggressive
  show rett aggressive
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan strict:#; left from Kreita
    xalign 0.4
    yalign 1.0
  show airAttack movie: #(at monster's position)
    xalign 0.0
    yalign 0.4
  pause(0.6)
  hide airAttack
  "The monster flew to us again. Lexan and Kreita pelted rain and wind at it, trying to block it from coming closer, but it wasn't enough."

  play music music_Words_Fall_Apart
  mi "Will anything ever be enough?"

  #(Continued in 8.3)
  #"A8.3"
  #TODO [FINAL





  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. A path's storyline is red. B path's storyline is blue. C path's storyline is green. If two paths share the same text, it will be in pink."
  #"-----------------------------------------------------------"
  #(Continuation of 8.2)

  #play music music_Words_Fall_Apart #(from before)
  scene cg forest27
  show cimaria determined:#; left
    yalign 1.0
    xalign 0.4
  show merona t desperate:#; right
    yalign 1.0
    xalign 0.6
  show rain movie #(ongoing)
  "The rain continued falling, oblivious to all that was happening. With her fists tightly balled up, Cimaria looked as if she was ready to attack the monster, but she didn't move. I could feel my own nails digging into my palms. "

  mi "We both have nothing to offer for this attack."

  scene cg forest28
  show rain movie #(ongoing)
  show birdMonster:#; position as in end of last chapter:
    yalign 1.0
    xalign -2.0
  play sound sound_fireAttack
  show fireAttack movie:#; place animation next to the birdMonster's position #(a bit different from the one following two lines below)
    yalign 0.5
    xalign 0.3

  show rett aggressive:#; center
    yalign 1.0
    xalign 0.5
  show duran t determined:#; right from Rett
    yalign 1.0
    xalign 0.6
  show lexan strict:#; right from Duran
    yalign 1.0
    xalign 0.9
  show kreita aggressive:#; right from Lexan
    yalign 1.0
    xalign 1.0
  pause(0.8)
  hide fireAttack
  "Duran shot another round of flames at the monster, and Rett readied his sword."

  mi "Why did I even step out?"



  play music music_movement
  play sound sound_fireAttack
  show fireAttack movie:#; place animation right from the birdMonster's position
    yalign 0.5
    xalign 0.3
  #TODO [move birdMonster to the left, away from fireAttack
  show birdMonster:
    linear 0.3 xalign -2.2
  pause(0.8)
  hide fireAttack
  
  show birdMonster:
    linear 0.5 xalign -1.7
  #TODO [after the fire animation is over, move birdMonster towards Rett #(not overlapping)
  "The creature managed to swerve out of the way before a lick of fire could singe its feathers. Locking eyes with Rett, it surged towards him once more."

  play sound sound_swordAttack
  show swordAttack movie: #(at monster's feet)
    yalign 0.7
    xalign 0.1
  pause(0.4)
  hide swordAttack
  #TODO [Move birdMonster down by 250px and a bit to the left#; if possible make its movement "tumbly" or slightly "jumping"
  show birdMonster:
    linear 0.2 yalign 1.2
    linear 0.4 yalign 0.0
  pause(0.6)
  #TODO [move CS kreita aggressive to the left until she stands right from Rett
  show kreita aggressive:
    yalign 1.0
    xalign 0.7
  play sound sound_swordAttack
  show swordAttack movie: #(at monster's wings)
    yalign 0.5
    xalign 0.0
  pause(0.4)
  hide swordAttack
    
  "Rett swung his sword at the monster's foot once it came close enough, managing to make it tumble to the ground. Kreita, gripping a dagger in both hands, dashed over to them and slashed the monster's wings. "

  #play sound [sound_swordAttack, sound_swordAttack, sound_swordAttack]#, 3 times, in sync with animations if possible please
  play sound sound_swordAttack
  show swordAttack movie:#, 3 times at the monster's legs, neck and eyes
    yalign 1.4
    xalign 0.0
  pause(0.4)
  play sound sound_swordAttack
  show swordAttack movie:#, 3 times at the monster's legs, neck and eyes
    yalign 0.6
    xalign 0.2
  pause(0.4)
  play sound sound_swordAttack
  show swordAttack movie:#, 3 times at the monster's legs, neck and eyes
    yalign 0.8
    xalign 0.3
  pause(0.4)
  hide swordAttack
  play sound sound_snarl
  pause(0.4)
  play sound sound_crash
  #TODO [after the attack animations, move the monster to the right towards Rett again
  hide birdMonster
  show birdMonster:
    yalign 0.0
    xalign -1.4
  "The two took turns finding new places to jab. Leg. Neck. Eye. Each one made the creature howl and convulse as its bodily fluids oozed out of the new wounds and onto Kreita and Rett. Before any of them could stab it one more time, the monster still found the strength to spring up and tackle the duo."

  scene cg forest27
  show cimaria determined OM:#; position as before#; move more the left and fade out
    yalign 1.0
    xalign 0.4
  show merona t desperate:#; right
    yalign 1.0
    xalign 0.6
  ck "That's it."

  scene cg forest28
  show birdMonster:#; #(position as before Cimaria's line):
    yalign 0.0
    xalign -1.4

  show rett aggressive behind birdMonster#; center
  show kreita aggressive:#; right from Rett #(as before)
    yalign 1.0
    xalign 0.7
  show duran t flabber:#; right from Kreita
    yalign 1.0
    xalign 1.0    
  show lexan strict:#; right from Duran
    yalign 1.0
    xalign 1.0

  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria aggressive:#; left from Rett
    yalign 1.0
    xalign 0.3
    
  play sound sound_swordAttack
  show swordAttack movie:
    yalign 0.6
    xalign 0.2
  pause(0.4)
  hide swordAttack
  "Cimaria sprinted to Kreita and Rett. She grabbed the sword that Rett dropped after getting tackled and jammed it deep into the monster's flank, repeatedly penetrating the flesh. Screeching and bucking its head down, the monster sank its teeth into Rett's shoulder, eliciting a scream from him as well."
  
  hide swordAttack
  show duran t flabber OM
  show lexan shocked behind duran
  dt "Rett!"

  #TODO [move Duran more to the left
  show duran t flabber OM:
    xalign 0.8
  show fireAttackBig movie behind cimaria:#; on birdMonster
    xalign 0.1
    yalign 0.5
  play sound sound_fireAttack
  pause(0.1)
  show steam movie: #(after fireAttackBig on same spot)
    xalign 0.15
    yalign 0.4
    
  pause(0.3)
  #TODO [move birdMonster to the left
  $ renpy.transition(slow_dissolve, layer="master")
  hide fireAttackBig
  hide steam
  show birdMonster:
    yalign 0.0
    xalign -2.2
  #TODO [move Kreita, Cimaria and Rett a bit to the right
  hide kreita
  show kreita aggressive:#; right from Rett #(as before)
    yalign 1.0
    xalign 0.9
  show cimaria aggressive:#; left from Rett
    yalign 1.0
    xalign 0.5
  show rett aggressive:
    yalign 1.0
    xalign 0.7
  pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")
  hide kreita
  pause(0.2)
  #TODO [Then move Cimaria and Rett down by 350px
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria aggressive:#; left from Rett
    yalign 3.0
    xalign 0.5
  show rett aggressive:
    yalign 3.5
    xalign 0.7
  "Duran ran over and blasted the monster in the face with the biggest flame we had ever seen him use, causing the monster to jump back and release itself from Rett. Cimaria, still hanging onto the sword lodged in its body, also got thrown back, and the two slid into the muddy road."

  #TODO [move Duran and Lexan to the right while fading them out
  show lexan shocked: 
    parallel:
      linear 1.0 xalign 1.3
    parallel:
      linear 1.0 alpha 0.0
  show duran t flabber OM:
    parallel:
      linear 1.0 xalign 1.3
    parallel:
      linear 1.0 alpha 0.0
  pause(1.0)
  #TODO [move Cimaria and Rett to their normal y position again
  #TODO [then move them a bit to right, fading them out
  show cimaria aggressive:#; left from Rett
    linear 1.0 yalign 1.0
    xalign 0.5
  show rett aggressive:
    linear 1.0 yalign 1.0
  pause(1.0)
  $ renpy.transition(slow_dissolve, layer="master")
  hide cimaria
  hide rett
  "Cimaria quickly staggered up to get to the half-conscious Rett. She placed his uninjured arm around her neck and dragged him away from us as fast as she could."

  play music music_Gallows_Hill
  scene cg forest27
  show kreita pouty CE:#; left#; placed lower by 350px
    xalign 0.3
    yalign 3.0
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t desperate:#; right, move her towards Kreita, then abruptly away to the right a bit #(gets pushed away)
    xalign 0.7
    yalign 1.0
  pause(0.1)
  show merona t desperate:
    linear 0.5 xalign 0.5
    yalign 1.0
  pause(0.7)
  show merona t desperate:
    linear 0.2 xalign 0.6
    yalign 1.0
  "Kreita moaned as she tried to sit up. Her braid and clothes clung to the mud, and she fell onto her back again. I rushed to her side, but she pushed me aside."

  #(croaking voice)
  show kreita weakWink OM
  show merona t nervous
  kh "I'm fine, Merona."

  show kreita pouty OM
  kh "I just need to lie down for a bit. I'll be okay."

  show kreita pouty
  show merona t desperate OM
  mk "Okay!? No way. Are you hallucinating from monster venom!?"

  show kreita neutral CE
  show merona t desperate
  "She closed her eyes and shook her head."

  show kreita neutral OM CE
  show merona t nervous
  kh "This happens all the time to me. Let me rest a little, alright?"

  show kreita pouty OM CE
  show merona t sad
  kh "Ugh, it feels like I'm taking a shower. A really dirty shower that could use a janitor to clean it up."

  show merona t sadSmile tears
  kh "Or maybe it's like a dozen grubby kids crying on me. I'd much rather have the dirty shower then."

  show kreita serious CE
  mi "I feel like crying on you, Kreita."

  mi "Even when you're so beaten down, you keep making me smile."

  show kreita serious OM
  show merona t sadSmile tears CE
  mi "I really hope you can continue making me and everyone else smile after this is over..."

  scene cg forest28
  show birdMonster:#; #(position as before):
    yalign 0.0
    xalign -2.2
  show wagon behind birdMonster:#, left from birdMonster
    yalign 1.0
    xalign 1.5

  show duran t nervous:#; right
    xalign 0.7
    yalign 1.0
  show lexan serious behind duran:#; right from Duran
    xalign 1.0
    yalign 1.0
  "The monster squawked and rose again. It shook the water off itself, and snapped its head at the crushed wagon this time."

  stop music fadeout 1.0
  mi "How is this bird still alive!? Are its wounds... gone?"

  scene cg forest27
  show kreita pouty CE:#; left#; placed lower by 350px
    xalign 0.3
    yalign 3.0
  show merona t sad:#; #(position as before)
    xalign 0.6
    yalign 1.0
    
  kh "Go to Cimaria and Rett. She's probably carrying out the operation now. Rett's in a much worse position than I am in... And Cimaria needs all the help she can get. Go, go, go."

  show merona t determined CE
  "I furiously nodded and jumped up."

  show merona t determined OM
  mk "Kreita, I-"
  
  
  play sound sound_snarl
  scene bg black
  #TODO [black screen, no text
  pause(1.0)

  play music music_Under_the_Stairs
  scene cg forest28
  show birdMonster:#; #(position as before):
    yalign 0.0
    xalign -2.0
  play sound sound_swordAttack
  show swordAttack movie:
    xalign 0.0
    yalign 0.9
  pause(0.4)
  hide swordAttack
  
  $ renpy.transition(slow_dissolve, layer="master")
  show prowen aggressive#, a bit right from the monster
  "Prowen leaped straight at the monster and managed to push it onto its back using his bodyweight alone. Taking out a knife inside his cape, he stabbed the monster's abdomen and ripped it open. "

  play sound sound_crash
  show birdMonster:#; move upwards and down aiming at Prowen
    parallel:
      linear 0.5 yalign 0.9
    parallel:
      linear 0.5 xalign -1.6
    linear 0.3 yalign 0.7
  pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")
  show prowen aggressive CE behind birdMonster:#, move down by 250px
    yalign 2.0
  "Prowen reached inside his shirt, but the monster jolted up into the air and flung him back onto the ground. Its wound was healing right before my eyes-the slit stitched itself up."

  show birdMonster:#; move back to former position before it attacked Prowen
    parallel:
      linear 0.5 yalign 0.0
    parallel:
      linear 0.5 xalign -2.0
  mi "I'm just about ready to actually cry."

  play music music_A_Moments_Reflection
  scene cg forest27
  show kreita sad:#; left#; placed lower by 350px
    xalign 0.3
    yalign 3.0
  show merona t sad OM:#; #(position as before)
    xalign 0.6
    yalign 1.0
  mk "Kreita, nothing we do is going to weaken the monster!"

  show merona t desperate OM
  mk "It heals itself so quickly... I don't think we can handle it much longer..."

  show kreita sad OM
  show merona t desperate
  kh "Merona... No..."

  stop music fadeout 1.0
  show kreita sad
  "I looked over and made eye contact with the monster."

  show merona t desperate OM
  mk "I-I..."

  play sound sound_snarl
  show kreita shocked
  show merona t desperate
  "The monster dove straight at Kreita and I."

  show merona t determined OM CE
  mk "No!"

  play music music_uplifting
  hide rain movie
  #TODO [show black screen, then fade to CG danger
  scene bg black
  pause(0.2)
  $ renpy.transition(slow_dissolve, layer="master")
  show cg danger
  "As the creature came closer and closer, I remembered the first time I encountered a monster. "

  "It was only a few weeks ago... Right at school..."

  "And it came running towards me..."

  "Getting ready to kill me..."

  "Bite my head off..."

  "Crush my body..."

  play music music_newBegin
  #TODO [quickly fade to white
  $ renpy.transition(dissolve, layer="master")
  scene bg white
  show magicEnergy movie #(ongoing/ looped)
  "But I also remembered something else-this other feeling."

  "This new feeling that only came the first time I faced that monster. A feeling that has always seemed to be with me but could never be found."

  mi "This... "
  hide magicEnergy movie
  scene cg MeronasMagic
  "This is what I've been missing!"

  "A new energy suddenly bloomed inside me. As the monster was a second away from piercing Kreita and me, I propelled the energy at it. A flash of light overwhelmed my entire field of view."

  $ renpy.transition(dissolve, layer="master")
  scene bg white
  pause(1.0)
  #TODO [Light immediately fades after above line

  $ renpy.transition(dissolve, layer="master")
  scene bg black
  #TODO [black screen
  "I collapsed down face first into the mud, feeling incredibly weak. Everything became woozy. The only reason I didn't immediately float into unconsciousness was because the others were yelling my name. Someone was shaking my shoulders, but I couldn't tell who it was."

  mi "I... can't..."

  mi "I..."

  mi "I need to..."

  mi "...stay awake..."

  play music music_Ill_be_right_behind_you_Josephine
  pm "Merona, can you hear us?"

  ln "Merona, are you alright!?"

  dt "Ugh, just wake up, Merona!"

  #(still croaking voice)
  kh "Merona..."

  bg "Merona, please be okay..."

  $ renpy.transition(slow_dissolve, layer="master")
  #TODO [fade in CG forest27#; 60% opacity on black
  scene cg forest27
  show rain movie #(ongoing), 60% opacity
  show black:
    alpha 0.6
  "Their voices became clearer as the seconds passed. I half-opened my eyes."

  mi "Yes, that's right."

  mi "Cimaria."

  mi "Operation."

  mi "Rett."

  #(Continued in 8.4)
  #"A8.4"
  #TODO [FINAL




  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. A path's storyline is red. B path's storyline is blue. C path's storyline is green. If two paths share the same text, it will be in pink."
  #"-----------------------------------------------------------"
  #(Continuation of 8.3)
  #play music music_Ill_be_right_behind_you_Josephine
  #TODO [as before
  #scene cg forest27#; 60% opacity on black
  #show rain movie#(ongoing), 60% opacity
  mk "Ugh..."

  mi "Rett."

  mi "Cimaria."

  mi "Operation."

  $ renpy.transition(slow_dissolve, layer="master")
  hide black
  #TODO [fade to CG forest27, 100% opacity
  show rain movie #(ongoing) also 100% opacity again please
  mi "Now."

  play music music_Swimming_To_Cambodia
  $ renpy.transition(slow_dissolve, layer="master")
  show prowen serious OM#; center
  pm "Can you hear us?"

  show prowen serious
  "It was Prowen who grasped my shoulders. As he gently shook me again, I peered up at him and nodded."

  show prowen neutral
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t worried OM:#; right from Prowen
    yalign 1.0
    xalign 0.8
  dt "Phew, you're not dead..."

  show prowen surprised
  show duran t determined OM
  dt "But it's time to stop acting drunk and get a move on."

  show prowen serious
  show duran t nervous OM
  dt "There's someone who needs your help."

  show duran t nervous
  "I could hear clear enough, but my vision was still somewhat blurry. I slowly brought my knees in and tried to stand up, finding balance in my feet."

  mk "Yes, I need to go..."

  #"-----------------------------------------------------------"
  
  if (currentPath == "A"):
    call lbl_PathA_8_4 from _call_lbl_PathA_8_4
  if (currentPath == "B"):
    call lbl_PathB_8_4 from _call_lbl_PathB_8_4
  if (currentPath == "C"):
    call lbl_PathC_8_4 from _call_lbl_PathC_8_4
    
  #"-----------------------------------------------------------"

  #"-----------------------------------------------------------"

  #"-----------------------------------------------------------"
  play music music_Roll_away_the_Stone
  show merona t worried OM
  mk "Where are Cimaria and Rett?"

  $ renpy.transition(slow_dissolve, layer="master")
  show lexan worried OM:
    xalign 0.2
    yalign 1.0
  #TODO [ #(if not path B, fade in) CS lexan worried OM, left from Prowen
  show merona t worried
  ln "Are you sure you're okay, Merona? Do you also need to get treated?"

  show lexan worried
  show merona t serious
  "The world is becoming clearer now... Everything seems to be stabilizing..."

  show merona t serious OM
  mk "I don't know for sure..."

  show lexan surprised
  show merona t determined OM
  show prowen sadSmile
  mk "But whether I do or don't, I have to be with Cimaria right now."

  #(Continued in 8.5)

  #mi "A8.5"
  #TODO [FINAL




  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. A path's storyline is red. B path's storyline is blue. C path's storyline is green. If two paths share the same text, it will be in pink."
  #"-----------------------------------------------------------"
  #(Continuation of 8.4)
  #play music music_Roll_away_the_Stone #(from before)
  #TODO [as before...
  #scene cg forest27
  show rain movie #(ongoing)

  show lexan serious
  show merona t serious
  show prowen serious
  mi "Where are they?"

  "Prowen placed his hand on my shoulder."

  show prowen serious OM
  pm "Follow me."

  play music music_Words_Fall_Apart
  $ renpy.transition(slow_dissolve, layer="master")
  hide lexan
  if (currentPath == "A"):
    hide duran
  show prowen serious
  "Clutching his cape, I staggered behind him as he led me through the forest. The rain was still coming down hard, but the trees helped block some of it out."

  show merona t nervous OM
  mk "Are the others coming too?"

  show merona t nervous
  show prowen serious OM
  pm "No."

  show merona t sadSmile OM
  show prowen serious
  mk "Are you going to stay with us?"

  show merona t disappointed
  show prowen serious OM
  pm "...No."

  show merona t surprised
  pm "She just needs you."

  show merona t sadSmile OM
  show prowen annoyed
  mk "B-But, the others, they-"

  show merona t serious
  show prowen annoyed OM
  pm "She just needs you."

  show prowen neutral
  mk "..."

  show merona t nervous
  mi "Just me... "

  show merona t surprised
  "Because of the yander?"

  play music music_River_Meditation
  #TODO [fade in CG forest29
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest29 
  show rain movie 
  #(at the same time fade in...)
  show cimaria neutral:#; lowered by 250px, x position at Rett's shoulder - might need adjustment later when rett operation is finished
    yalign 2.0
    xalign 0.2
  show rett operation #(this will be Rett lying on the ground)
  "Soon enough, we found Cimaria and Rett at the base of a giant tree. Cimaria was already injecting something into Rett, who lay on a blanket."

  #TODO [both behind rett operation please
  $ renpy.transition(slow_dissolve, layer="master")
  show prowen serious OM behind rett:#; right
    yalign 1.0
    xalign 1.1
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t nervous behind rett:#; left from Prowen
    yalign 1.0
    xalign 0.9
  pm "Okay. If you need me, just yell. I'll be waiting neaby."

  show merona t shocked OM
  show prowen neutral
  mk "Wait-are you sure?"

  show merona t shocked
  "Nodding, Prowen turned around and started walking back."

  show merona t nervous
  show prowen determined OM
  pm "She just needs you."

  show merona t determined
  show prowen determined#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide prowen
  mi "I'll have to trust his word then."

  $ renpy.transition(slow_dissolve, layer="master")
  show merona t nervous:
    yalign 2.0
    xalign 0.5
  #TODO [move Merona to center and lower y position by 250px
  "I rushed to Cimaria and Rett. A dizzy air still hung around me, but my vision finally cleared up."

  show cimaria neutral OM
  ck "Get the white pouch in my bag, Merona."

  show cimaria neutral
  show merona t serious
  "If she was nervous, it didn't show. She kept her focus on Rett, quickly injecting multiple spots around his upper body with a substance I couldn't recognize."

  #(Continued in 8.6)
  #"A8.6"
  #TODO [FINAL




  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. A path's storyline is red. B path's storyline is blue. C path's storyline is green. If two paths share the same text, it will be in pink."
  #"-----------------------------------------------------------"
  #(Continuation of 8.5)

  play music music_River_Meditation #(from before)
  #TODO [positions as before...
  #scene cg forest29

  show cimaria neutral
  show merona t determined
  show rett operation
  show rain movie #(ongoing)
  mi "Alright, there's no more time to waste."

  "Digging through the bag, I pulled out the white pouch and brought it over to Cimaria."

  show cimaria neutral OM
  show merona t serious
  ck "A bottle of antiseptic and some cotton pads are inside. Soak the pads and apply it over Rett's injured shoulder and both of his arms while I prepare my tools."

  play music music_piano
  show cimaria neutral#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide cimaria
  
  show merona t worried:#; move closer to Rett's shoulder but with a small distance to Cimaria
    xalign 0.4
  "I nodded and dropped to Rett's body. Cimaria must have sedated him-his face was still somewhat tense, but it gradually relaxed. As soon as the antiseptic touched his shoulder, he sharply inhaled."

  show merona t worried OM
  mk "You can do this Rett..."

  show merona t sadSmile
  rt "Mm..."

  play music music_She_dreams_in_blue
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria neutral behind rett:# at former position #(again lowered by 250px)
    yalign 2.0
    xalign 0.2
  show merona t serious
  "Cimaria sat down next to me with a box in her hands."

  show cimaria neutral OM
  ck "Hand me the antiseptic."

  show cimaria neutral
  "So far, so good."

  "After I gave her the bottle, she opened her box and took out three tools, wiping them down."

  show cimaria neutral OM
  show merona t nervous
  ck "Today, you are my assistant."

  ck "Do what I say, and everything will go smoothly."

  show cimaria serious OM
  show merona t determined
  ck "Act quickly and efficiently."

  show cimaria sadSmile
  show merona t surprised
  "She set down her tools and gave me a rueful smile."

  show cimaria sadSmile OM
  show merona t sadSmile
  ck "I hope you don't think I'm being too cold. This is how I work best in these kinds of situations."

  show cimaria gentle
  show merona t content OM
  mk "No, I understand. You're the boss here. I'll do whatever I can to help."

  show cimaria gentle OM
  show merona t content
  ck "You'd be a good medical assistant, Merona."

  show cimaria determined OM
  show merona t serious
  ck "But we can talk about that later."

  #(Continued in A8.7)
  #"A8.7"
  #TODO [FINAL




  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. A path's storyline is red. B path's storyline is blue. C path's storyline is green. If two paths share the same text, it will be in pink."
  #"-----------------------------------------------------------"
  #(Continuation of 8.6)

  #TODO [positions as before...
  #scene cg forest29

  play music music_River_Meditation
  show cimaria determined
  show merona t serious
  show rett operation
  show rain movie #(ongoing)
  "The sedatives had worked their magic-Rett was completely under. Making the first incision was the only thing left to do."

  show cimaria neutral
  show merona t determined
  mi "Okay, Merona. It's going to be alright... Just do what you're told, and everything will be okay..."

  show merona t serious
  "Taking the scalpel, Cimaria honed in on Rett's wounded shoulder. She made a clean slit across the skin and slightly spread the opening."

  show cimaria neutral OM
  show merona t surprised
  ck "Hand me the dropper bottle."

  show cimaria neutral CE
  show merona t serious
  "She squeezed a few drops of the bottle's contents into the slit and set it down. Keeping her eyes shut, her fingers gently pressed into Rett's flesh. We sat in silence, letting the falling rain take over our ears."

  mi "..."

  show merona t worried
  mi "Magical operations aren't long, right? It can't last more than half an hour..."

  play music music_Sovereign
  show cimaria serious CE
  show merona t nervous
  "I clenched my jaw, unable to stop staring at Cimaria. Her furrowed brows and growing grimace made me queasy."

  mi "Once again, I'm just sitting here, doing nothing."

  mi "Is there really nothing else I can do?"

  show cimaria serious
  "Still frowning, Cimaria cracked open her eyes and fixated on Rett."

  show cimaria serious OM
  show merona t scared
  ck "His body is so weak right now-no matter how much I try to fight it, the new venom combined with the fish monster's venom wrestles away from my grasp."

  show cimaria worried
  show merona t worried
  "Her gaze darted up to the sky."

  show cimaria worried OM
  ck "If it weren't raining, then..."

  show cimaria annoyed CE
  "Shaking her head, she groaned."

  show cimaria annoyed OM
  ck "No, no, no, that's not it."

  show cimaria serious OM
  show merona t sad
  ck "This is frustrating..."

  show cimaria serious
  show merona t sad OM
  mk "Cimaria-"

  show cimaria serious CE
  show merona t sad
  "Before I could say any more, Cimaria closed her eyes again and refocused on Rett's shoulder. "

  show merona t desperate
  mi "If she can't do this..."

  show merona t determined
  mi "No, I can't think like that! She can totally do this. She always does everything successfully."

  show merona t nervous
  "Cimaria's scowl was carved into her skin. As I continued watching her, doubt ebbed across me."

  show merona t serious
  mi "I don't know what to make of this anymore."

  show merona t worried
  mi "Rett looked so healthy over the past few days... even weeks. The venom didn't seem to do much."

  mi "I assumed that we'd get out of this fine, but thanks to this new monster..."

  show merona t nervous CE
  "I swallowed hard."

  show merona t worried
  mi "I don't know."

  play music music_newBegin
  show merona t determined
  mi "But I need to do something-there has to be a way for me to be more useful than just staring."

  mi "There's... There's..."

  show merona t shocked
  "I widened my eyes."

  mi "Yander."

  show merona t determined
  mi "How could I forget about yander!?"

  #(Continued in 8.8)
  #"A8.8"
  #TODO [FINAL





  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. A path's storyline is red. B path's storyline is blue. C path's storyline is green. If two paths share the same text, it will be in pink."
  #"-----------------------------------------------------------"
  #(Continuation of 8.7)
  if (currentPath == "A"):
    call lbl_PathA_8_8_1 from _call_lbl_PathA_8_8_1_1
    jump lbl_chapter8_8_optional_1End
  if (currentPath == "B"):
    pass
  if (currentPath == "C"):
    pass
  
label lbl_chapter8_8_optional_1:
  #(Continuation of 8.7)
  #(B + C Path)
  #play music music_newBegin #(from before)
  #TODO [positions as before...
  #scene cg forest29

  show cimaria serious CE
  show merona t determined
  show rett operation
  show rain movie #(ongoing)
  mi "The monster may have destroyed our garden, but we still have the powdered yander-the stuff Cimaria made into serums."

  mi "It's not the real deal, but... It's better than nothing!"


  play music music_White
  show merona t serious
  "Lunging for her bag, I quickly found the container of serums. The two mini dropper bottles filled with the yellowish-green substance in this moment were the most beautiful things I had ever seen."

  show cimaria neutral CE
  show merona t determined OM
  mk "Cimaria! Open your eyes!"

  show cimaria neutral
  show merona t serious OM
  mk "I have yander serum!"

  show merona t serious
  "Cimaria wordlessly held out her hand. Immediately after she grasped the battle, she squeezed a shot of the runny liquid into Rett's wound, pressed her hands over it, and closed her eyes again."

  play music music_Soporific
  show cimaria serious CE
  show merona t nervous
  mi "I wonder if the yander's properties will come through enough in this form... "

  mi "It was initially dried when we purchased it. I don't know how to handle lifeless plants with my ability, so I'm not sure if I can enhance it while it's in that state. Probably not."

  show merona t serious
  mi "Let's just hope that the serum is good enough on its own."

  "As the seconds dragged on, a deepening scowl continued to grace Cimaria's face."

  show merona t disappointed
  mi "This serum isn't doing so well... "

  show merona t determined
  mi "Is there anything else we can use?"

  "I rummaged through Cimaria's bag, opening up every little pouch packed inside. Empty bottles. Needles. Cloth. More disinfectant. Nothing worthwhile to be found yet."
label lbl_chapter8_8_optional_1End:

label lbl_chapter8_8_optional_2:
  if (currentPath == "A"):
    pass
  if (currentPath == "B"):
    pass
  if (currentPath == "C"):
    call lbl_PathC_8_8_1 from _call_lbl_PathC_8_8_1_1 
    jump lbl_chapter8_8_optional_2End
  #TODO [PINK TEXT IS SHARED WITH B8.9
  show merona t serious OM
  mk "Cimaria!"

  show merona t serious
  "I hastened over to her and shook her shoulder. She refused to budge."

  show merona t nervous OM
  mk "Cimaria, open your eyes. Take this."

  show cimaria shocked CE
  show merona t serious
  "Wordlessly, she squeezed her eyes shut even tighter. Her face was still contorted as if she was in pain. It looked like tears instead of raindrops were running down her cheeks. "

  show merona t nervous
  "Maybe it was both."

  "I wrenched one of her hands away from Rett and pressed the yander into her palm."

  show cimaria serious CE
  show merona t determined OM
  mk "You can do this."

  show merona t determined
  "Cimaria's lip quivered as she wrapped her fingers around the yander."

  show cimaria serious OM CE
  show merona t sadSmile
  ck "Thank you, Merona."

  show cimaria neutral
  show merona t serious
  "She took a deep breath and opened her eyes."

  play music music_Ill_be_right_behind_you_Josephine
  show cimaria serious OM
  show merona t nervous
  ck "If this doesn't work..."

  show cimaria determined OM
  show merona t shocked
  ck "...You need to enhance the yander."

  show cimaria determined
  show merona t shocked OM
  mk "What?"

  show cimaria serious OM
  show merona t nervous
  ck "I know this yander isn't good right now-it could be too wilted for me to effectively use it."

  show cimaria determined OM
  show merona t serious
  ck "But you...you may be able to connect with it better or even increase its potency, yes?"

  show cimaria determined
  show merona t serious OM
  mk "I-I don't know, I... I can't guarantee-"

  show cimaria serious OM
  show merona t nervous
  #(slight voice crack at end of sentence)
  ck "Nobody can guarantee anything, Merona."

  show merona t serious
  ck "Just try."

  show cimaria sadderSmile OM
  ck "We won't let him die without trying everything we can."

  show cimaria sadderSmile CE
  "Once again, she placed her hand with the yander over Rett's wounds and closed her eyes."

  show merona t desperate
  mi "The yander doesn't have its roots fully intact. I don't know if I'll achieve anything because of that... I've only enhanced plants by connecting with their roots."

  show merona t nervous
  mi "Perhaps I could find a connection through the stem? The veins? "

  mi "Its life flow must be rather weak at this point though. What if it's not enough?"

  play sound sound_clap
  show cimaria serious CE
  show merona t disappointed CE
  "I slapped my cheeks."

  play music music_She_dreams_in_blue
  show merona t determined
  mi "No, I can't think like this."

  mi "Cimaria isn't stopping herself from doing anything she can-I can't stop myself either. Enhancing is the most important thing I'm able to do, so I need to try as hard as I can to make it work."

  show merona t serious
  mi "Remember your lessons with Lexan... Remember all the things you learned. It's time to apply that knowledge in the real world!"

  show merona t worried
  mi "Never did I think that I would use this knowledge to save a life, however."

  show cimaria serious
  show merona t surprised
  "Cimaria suddenly thrust her hand with the yander at me."

label lbl_chapter8_8_optional_2End:
  #(Continued in A8.9)
  #"A8.9"
  #TODO [FINAL

  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. A path's storyline is red. B path's storyline is blue. C path's storyline is green. If two paths share the same text, it will be in pink."
  #"-----------------------------------------------------------"

  if (currentPath == "A"):
    pass
  if (currentPath == "B"):
    pass
  if (currentPath == "C"):
    call lbl_PathC_8_9 from _call_lbl_PathC_8_9_1
    jump lbl_chapter8_9_optionalEnd
  #"-----------------------------------------------------------"
    
label lbl_chapter8_9_optional:
  #(Continuation of 8.8)
  #(Shared text with B8.9!)
  play music music_Lafayette
  #TODO [positions as before...
  #scene cg forest29

  show cimaria serious
  show merona t determined
  show rett operation
  show rain movie #(ongoing)
  mi "Alright, Merona. Let's do this."

  #TODO [move Merona to Cimaria's position and vice versa
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t determined:
    yalign 2.0
    xalign 0.1
  show cimaria serious:
    yalign 2.0
    xalign 0.4
  "I grasped the leaves and scooched over to Rett. Cimaria gave my shoulder a quick squeeze and moved out of the way."

  show cimaria sadderSmile OM
  show merona t serious
  ck "Thank you, Merona..."

  show merona t sadSmile
  ck "Whatever happens, I'm very grateful that you're here with me."

  show cimaria sadderSmile
  show merona t sadSmile
  mk "Yeah... Me too."

  show merona t determined CE
  scene bg black with fade
  "I took a deep breath. Before focusing on Rett's shoulder, I closed my eyes and concentrated on connecting with the yander leaves in my hands."

  
  show magicEnergy movie
  mi "Let's start with the stems."

  mi "All I have to do is dig into the plant and find its essence."

  play music music_Swimming_To_Cambodia
  "But as time passed, I only grew more aware of the feeling of the hard stem rather than the pulse of a life flow."

  mi "..."

  mi "This can't be completely dead right? It doesn't feel that dry and brittle, so..."

  mi "I need to do something different-perhaps placing the leaves near Rett would help. Feeling his life flow could trigger me to find the yander's life flow."

  $ renpy.transition(slow_dissolve, layer="master")
  hide magicEnergy
  "But even after that, I couldn't feel anything."

  mi "..."

  mi "This yander is completely dead."

  mi "I don't know what else to do now."

  mi "The only thing I could have done was to enhance the yander, but looks like there's no way that can happen anymore..."
label lbl_chapter8_9_optionalEnd:
  if (currentPath == "A"):
    pass
  if (currentPath == "B"):
    call lbl_PathB_8_9 from _call_lbl_PathB_8_9_1
  if (currentPath == "C"):
    pass
    
    
  #(Continued in A9.0)
  jump lbl_chapter9
