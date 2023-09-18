label lbl_minigame_1_Intro:
  ### MINIGAME STARTS ###
  #call minigame_start() from minigametime

  stop music fadeout 1.0

  play music MINIGAME fadein 2.0
  #scene cg limbokin

  "The first Limbokin approaches! "

  "It's a teenage girl, maybe around your sister's age. She has red pigtails and freckles all over her face. "

  no1 "Guess I'm up first. You gonna ask me something or what? "

  "She's chewing loudly as she talks. You ask her what she's chewing on. "

  no1 "Gum. Was chewing it the day I died. Been chewing it ever since. "

  no1 "Why, you got a problem with that? "

  no1 "Also, was that your question? Stupid question. "

  #menu:
  #"What question should you ask? "
  #"How did you die? {GO TO PART 2} "
  #"How do you feel about life in purgatory? {GO TO PART 3} "
  #"What do you miss most about life on Earth? {GO TO PART 4} "
  
  return

label lbl_minigame_1_Die:

  no1 "Drowned. "

  no1 "It was in the school swimming pool. Pretty damn tragic, huh? "

  no1 "You know, there are a bunch of Limbokin here who went to the same school. "

  no1 "The ones who died after me, they said the school built a bench in honor of my memory. "

  no1 "The bench even had a plaque with my name on it! Neat, eh? "

  "Very neat! "

  "You wonder if you're special enough for your school to build a bench, with your name on a plaque. "

  no1 "It's not about how special you are. You get a plaque if you die within school grounds. "

  no1 "Did you die in school? "

  no1 "If you did, the school board overcompensates, so that the school won't be blamed. "

  "Oh. No plaque for you then. "

  #TODO {GO TO PART 5} "
  return

label lbl_minigame_1_Purgatory:
  #TODO {PART 3}"

  no1 "It's whatever. Could be worse, I guess. "

  no1 "I know you're new here, so we look like a bunch of freaks to you. "

  no1 "Don't blame you. I thought the same thing when I first got here. "

  no1 "But some of the guys here aren't that bad. Some are actually pretty damn fun. "

  "She's looking over your shoulder. You follow her gaze. "

  "Seems like she's staring at the next guy in line, Limbokin No. 2. "

  "You ask her if she's referring to that guy. "

  no1 "Wha-- "

  no1 "Him?! No! No way! Not if he was the last guy in purgatory! "

  no1 "I was just looking! Can't a girl look where she wants? "

  no1 "It's not like I like him or anything!!! "

  "Heh. Sure. "

  #TODO {GO TO PART 5} "
  return

label lbl_minigame_1_Earth:
  #TODO {PART 4}"

  no1 "I know this is gonna sound totally nerdy. And I get it, believe me. "

  no1 "But I actually miss school most of all. And I gotta say, I was {i}not{/i} a good student. "

  no1 "It was boring most of the time, sure. But I miss that same old, same old boring routine. "

  no1 "How about you, do you miss school? "

  "You tell her you haven't been away long enough to miss it. "

  no1 "Yeah, I guess. "

  "But you do miss your school friends. They were a rowdy bunch, but they had your back. "

  "She smiles at this. "

  no1 "You took the words right outta my mouth. "

  #TODO {GO TO PART 5} "

  #TODO {PART 5}"
  return

#  hide  cg limbokin
#
#  show bg white
#
#  "Which item should you offer? "
#
#  #show MINIGAME ASSETS: POKERFIGURE, UNIFORM, PEUNIFORM, SWIMSUIT
#
#  #"[MINIGAME FEATURE: Player must choose between UNIFORM, PEUNIFORM, SWIMSUIT. Player must drag and drop the chosen item over to POKERFIGURE.
#
#  #TODO {IF PLAYER CHOSE UNIFORM: POKERFIGURE is replaced with HEARTFIGURE.} "
#  #TODO {IF PLAYER CHOSE PEUNIFORM: POKERFIGURE is replaced with SMILEFIGURE.} "
#  #TODO {IF PLAYER CHOSE SWIMSUIT: POKERFIGURE is replaced with ANGRYFIGURE.} "
#
#  #HIDE ALL MINIGAME ASSETS
#
#  hide  bg white
#
#  scene cg limbokin
#
#  #TODO {IF PLAYER CHOSE UNIFORM} "
#
#  "The Limbokin loves your offer and counter-offers two teeth! "
#
#  #menu:
#  "Do you accept or reject this counter-offer? "
#
#  "Accept the counter-offer "
#
#  "Congratulations! The trade has been closed! "
#
#  "The Limbokin walks away, looking very happy. "
#
#  #(X+2) #(Y+1) "
#
#  #TODO {GO TO PART 6} "
#
#  "Reject the counter-offer "
#
#  "You decide to reject the counter-offer. "
#
#  "The Limbokin walks away, looking dissatisfied. "
#
#  #TODO {GO TO PART 6} "
#
#  #TODO {IF PLAYER CHOSE PEUNIFORM} "
#
#  "The Limbokin likes your offer and counter-offers one tooth! "
#
#  #menu:
#  "Do you accept or reject this counter-offer? "
#
#  "Accept the counter-offer "
#
#  "Congratulations! The trade has been closed! "
#
#  "The Limbokin walks away, looking satisfied. "
#
#  #(X+1) #(Y+1) "
#
#  #TODO {GO TO PART 6} "
#
#  "Reject the counter-offer "
#
#  "You decide to reject the counter-offer. "
#
#  "The Limbokin walks away, looking dissatisfied. "
#
#  #TODO {GO TO PART 6} "
#
#  #TODO {IF PLAYER CHOSE SWIMSUIT} "
#
#  "The Limbokin hates your offer and refuses to counter-offer! "
#
#  "The Limbokin walks away, looking upset. "
#
#  #TODO {GO TO PART 6} "

label lbl_minigame_2_Intro:
  #TODO {PART 6}"

  "The second Limbokin approaches! "

  "It's a massive dude who immediately goes in for a bro hug, never mind how small you are compared with him. "

  no2 "Wassup, homie? How's it hanging? "

  "You doubt this macho dude can fit in your sister's clothes. You tell him so, but he laughs heartily. "

  no2 "That's the idea, bro. Even as an Earthling I always bought my shirts several sizes smaller. "

  no2 "Really makes my muscles pop. "

  no2 "I say if you've got it, flex it! "

  ##menu:
  #"What question should you ask? "
  #"How did you die? {GO TO PART 7} "
  #"How do you feel about life in purgatory? {GO TO PART 8} "
  #"What do you miss most about life on Earth? {GO TO PART 9} "
  return

label lbl_minigame_2_Die:
  #TODO {PART 7}"

  no2 "It's a sad story, bro. You trying to make me cry? "

  "You definitely weren't trying to do that. "

  no2 "Nah, just messing with you, bro. "

  no2 "I only cry when something sweet touches this big old heart of mine. "

  no2 "See, I was on a morning jog. "

  no2 "Lifting is more my jam, but you know, you gotta do your cardio too. "

  no2 "And my heart just gave out. Kaput. Myocardial infarction, bro. "

  "Myo-what? "

  no2 "It's the fancy term for a heart attack, little dude. "

  #TODO {GO TO PART 10} "
  return

label lbl_minigame_2_Purgatory:
  #TODO {PART 8}"

  no2 "Oh, dude! It's the best! "

  no2 "Here, I can work out all day! I have no other responsibilities! "

  no2 "No bad vibes to ruin my juju. "

  no2 "Got all the time in the world for gainz now. "

  "Do muscles still grow after you die? "

  no2 "You got me there, bro. They don't. I just imagine that they do. "

  no2 "If this was Earth, oh boy. I'd be a beast by now, bro! "

  no2 "But even back on Earth, it was more about companionship. "

  no2 "I loved my gym bros like they were my blood bros. "

  no2 "Here in purgatory, the company's just as dope, if not more! "

  "He shoots a smile at Limbokin No. 1. "

  "She's obviously flustered, though she pretends not to care. "

  #TODO {GO TO PART 10} "
  return

label lbl_minigame_2_Earth:

  #TODO {PART 9}"

  no2 "The colors, little dude. The colors. "

  "You take a look around you. Seems colorful enough to you. "

  no2 "The land, yeah. But I'm talking about the people, bro. "

  no2 "Stay here long enough, and you'll turn gray as a grandma. "

  "There's a grandma among the other Limbokin. She shakes her fist at him. "

  no2 "Chill out, Gam-Gam! I ain't talking about you. "

  no2 "I'm talking about the vibe. Gray vibes give me the heebie-jeebies, man. "

  no2 "If I was in charge, I'd do something to make the colors pop. Bring back life to this place. "

  #TODO {GO TO PART 10} "
  return


  ##TODO {PART 10}"
  #
  #hide  cg limbokin
  #
  #show bg white
  #
  #"Which item should you offer? "
  #
  ##show MINIGAME ASSETS: POKERFIGURE, POLO, FLANNEL, SWEATSHIRT
  #
  ##[MINIGAME FEATURE: Player must choose between POLO, FLANNEL, SWEATSHIRT. Player must drag and drop the chosen item over to POKERFIGURE.
  #
  ##TODO {IF PLAYER CHOSE POLO: POKERFIGURE is replaced with HEARTFIGURE.} "
  ##TODO {IF PLAYER CHOSE FLANNEL: POKERFIGURE is replaced with SMILEFIGURE.} "
  ##TODO {IF PLAYER CHOSE SWEATSHIRT: POKERFIGURE is replaced with ANGRYFIGURE.} "
  #
  ##[HIDE ALL MINIGAME ASSETS
  #
  #hide  bg white
  #
  #scene cg limbokin
  #
  ##TODO {IF PLAYER CHOSE POLO} "
  #
  #"The Limbokin loves your offer and counter-offers two teeth! "
  #
  ##menu:
  #"Do you accept or reject this counter-offer? "
  #
  #"Accept the counter-offer "
  #
  #"Congratulations! The trade has been closed! "
  #
  #"The Limbokin walks away, looking very happy. "
  #
  ##(X+2) #(Y+1) "
  #
  ##TODO {GO TO PART 11} "
  #
  #"Reject the counter-offer "
  #
  #"You decide to reject the counter-offer. "
  #
  #"The Limbokin walks away, looking dissatisfied. "
  #
  ##TODO {GO TO PART 11} "
  #
  ##TODO {IF PLAYER CHOSE FLANNEL} "
  #
  #"The Limbokin likes your offer and counter-offers one tooth! "
  #
  ##menu:
  #"Do you accept or reject this counter-offer? "
  #
  #"Accept the counter-offer "
  #
  #"Congratulations! The trade has been closed! "
  #
  #"The Limbokin walks away, looking satisfied. "
  #
  ##(X+1) #(Y+1) "
  #
  ##TODO {GO TO PART 11} "
  #
  #"Reject the counter-offer "
  #
  #"You decide to reject the counter-offer. "
  #
  #"The Limbokin walks away, looking dissatisfied. "
  #
  ##TODO {GO TO PART 11} "
  #
  ##TODO {IF PLAYER CHOSE SWEATSHIRT} "
  #
  #"The Limbokin hates your offer and refuses to counter-offer! "
  #
  #"The Limbokin walks away, looking upset. "
  #
  ##TODO {GO TO PART 11} "
  
label lbl_minigame_3_Intro:
  #TODO {PART 11}"

  "The third Limbokin approaches! "

  "The old woman looks a bit like your grandma, Lola Jesusa. She pinches your cheeks just like Lola Jesusa! "

  no3 "My, my. You remind me of my grandson. "

  no3 "When I last saw him, he was just about your age. Oh, but that was lifetimes ago. "

  no3 "He must have been sent to heaven. He was such a good boy. "

  "Unlike you, a bad boy who was sent to purgatory. "

  no3 "You're not bad for harboring regrets, my child. "

  no3 "I might even argue that those who feel guilt have purer souls than those who don't. "

  #menu:
  #"What question should you ask? "
  #"How did you die? {GO TO PART 12} "
  #"How do you feel about life in purgatory? {GO TO PART 13} "
  #"What do you miss most about life on Earth? {GO TO PART 14} "

  return

label lbl_minigame_3_Die:
  #TODO {PART 12}"

  no3 "I was tending to my garden when a bee stung me. "

  "Was she allergic to bees? "

  no3 "No, I got into my car with no issues. I drove to the hospital to get the bee sting treated. "

  "Did she fall asleep behind the wheel? Did she crash the car? "

  no3 "My, what a colorful imagination you have! "

  no3 "No, dear. Nothing like that. "

  no3 "This notorious serial killer escaped from a nearby prison. "

  no3 "He stole a doctor's coat and carved out my heart with a scalpel. "

  "Your jaw drops. "

  no3 "But if you think about it, it can all be traced back to that garden. "

  no3 "If only I hadn't tried to win the Greenest Thumb Award for the tenth year in a row! "

  #TODO {GO TO PART 15} "

  return

label lbl_minigame_3_Purgatory:
  #TODO {PART 13}"
  no3 "It is perfectly adequate. "

  "Can she explain? "

  no3 "The Limbokin are all very nice, but I can never get anyone to come over for tea. "

  no3 "Would you honor me with a teatime visit one of these days, my child? We can have some crumpets. "

  "There's tea in purgatory? "

  no3 "Tea is a state of mind, my dear. "

  "Great, she talks about tea the same way your math teacher talked about math. "

  #TODO {GO TO PART 15} "

  return

label lbl_minigame_3_Earth:
  #TODO {PART 14}"

  no3 "Oh, this is an easy one to answer. I miss my grandson, with my whole heart. "

  no3 "He was a very good boy, and a very gay boy. "

  no3 "You look just like my beloved grandson. Are you also a gay boy? "

  "You don't know. You haven't really thought about it. "

  no3 "My grandson loved clothes more than anything. He wanted to grow up to be a fashion designer. "

  no3 "He especially adored big poofy pieces, the kind that could only work on a fashion runway. "

  no3 "Sometimes he would raid my closet. The clothes I didn't wear anymore, he made good use of. "

  "Well, you and her grandson have that one thing in common. "

  #TODO {GO TO PART 15} "

  return

  ##TODO {PART 15}"
  #
  #hide  cg limbokin
  #
  #show bg white
  #
  #"Which item should you offer? "
  #
  ##show MINIGAME ASSETS: POKERFIGURE, FAUXFUR, KIMONO, HAWAIIAN
  #
  ##MINIGAME FEATURE: Player must choose between FAUXFUR, KIMONO, HAWAIIAN. Player must drag and drop the chosen item over to POKERFIGURE.
  #
  ##TODO {IF PLAYER CHOSE FAUXFUR: POKERFIGURE is replaced with HEARTFIGURE.} "
  ##TODO {IF PLAYER CHOSE KIMONO: POKERFIGURE is replaced with SMILEFIGURE.} "
  ##TODO {IF PLAYER CHOSE HAWAIIAN: POKERFIGURE is replaced with ANGRYFIGURE.} "
  #
  ##HIDE ALL MINIGAME ASSETS
  #
  #hide  bg white
  #
  #scene cg limbokin
  #
  ##TODO {IF PLAYER CHOSE FAUXFUR} "
  #
  #"The Limbokin loves your offer and counter-offers two teeth! "
  #
  ##menu:
  #"Do you accept or reject this counter-offer? "
  #
  #"Accept the counter-offer "
  #
  #"Congratulations! The trade has been closed! "
  #
  #"The Limbokin walks away, looking very happy. "
  #
  ##(X+2) #(Y+1) "
  #
  ##TODO {GO TO PART 16} "
  #
  #"Reject the counter-offer "
  #
  #"You decide to reject the counter-offer. "
  #
  #"The Limbokin walks away, looking dissatisfied. "
  #
  ##TODO {GO TO PART 16} "
  #
  ##TODO {IF PLAYER CHOSE KIMONO} "
  #
  #"The Limbokin likes your offer and counter-offers one tooth! "
  #
  ##menu:
  #"Do you accept or reject this counter-offer? "
  #
  #"Accept the counter-offer "
  #
  #"Congratulations! The trade has been closed! "
  #
  #"The Limbokin walks away, looking satisfied. "
  #
  ##(X+1) #(Y+1) "
  #
  ##TODO {GO TO PART 16} "
  #
  #"Reject the counter-offer "
  #
  #"You decide to reject the counter-offer. "
  #
  #"The Limbokin walks away, looking dissatisfied. "
  #
  ##TODO {GO TO PART 16} "
  #
  ##TODO {IF PLAYER CHOSE HAWAIIAN} "
  #
  #"The Limbokin hates your offer and refuses to counter-offer! "
  #
  #"The Limbokin walks away, looking upset. "

  #TODO {GO TO PART 16} "
label lbl_minigame_4_Intro:
  #TODO {PART 16}"

  "The fourth Limbokin approaches! "

  no4 "G-Greetings. I'm happy t-to meet you. "

  "They don't look happy at all. More than anything, it seems like they want to crawl under a rock. "

  no4 "I was g-grateful t-to be chosen for t-this opportunity. My wardrobe c-could use an upg-grade. "

  no4 "I am in a shameful c-condition, I know. I rarely g-go out, t-to keep my dig-g-gnity int-tact. "

  "You thank them for bothering to come out at all. "

  #menu:
  #"What question should you ask? "
  #"How did you die? {GO TO PART 17} "
  #"How do you feel about life in purgatory? {GO TO PART 18} "
  #"What do you miss most about life on Earth? {GO TO PART 19} "

  return

label lbl_minigame_4_Die:
  #TODO {PART 17}"

  "They make a nervous sort of peeping sound. "

  no4 "I was on a beach with my friends. I st-stayed under my umbrella. I felt safe t-there. "

  no4 "C-Come swim, t-they said. "

  no4 "I t-tried saying no. But I was t-too scared t-to really say no. "

  no4 "T-The shark t-took out half my leg with one bite. "

  no4 "T-Then I bled t-to death. "

  "They lift their left pants leg to show you the metal rod hidden there. "

  no4 "My family must have put t-this is in when t-they buried me. "

  #TODO {GO TO PART 20} "

  return

label lbl_minigame_4_Purgatory:
  #TODO {PART 18}"

  no4 "It is t-the same as life on Earth. "

  "Is that a good thing or a bad thing? "

  no4 "Both scare me t-to death. "

  "But you can't die again, can you? "

  no4 "No one ever has. But who's t-to say I won't be t-the first? "

  #TODO {GO TO PART 20} "

  return

label lbl_minigame_4_Earth:
  #TODO {PART 19}"
  
  no4 "I miss having my own home. Here, t-there is no place t-to hide. "

  "But didn't they just say that they rarely go out? "

  no4 "T-There is t-this c-class of Limbokin who have st-stopped c-caring. "

  no4 "T-They don't even move. "

  no4 "T-They barely react when I move t-their bodies around t-to use as walls. "

  "You use their bodies as walls?! "

  no4 "Yes. And as chairs. And as beds. "

  #TODO {GO TO PART 20} "

  return

  ##TODO {PART 20}"
  #
  #hide  cg limbokin
  #
  #show bg white
  #
  #"Which item should you offer? "
  #
  ##show MINIGAME ASSETS: POKERFIGURE, BATHROBE, PJS, ONESIE
  #
  ##MINIGAME FEATURE: Player must choose between BATHROBE, PJS, ONESIE. Player must drag and drop the chosen item over to POKERFIGURE.
  #
  ##TODO {IF PLAYER CHOSE BATHROBE: POKERFIGURE is replaced with HEARTFIGURE.} "
  ##TODO {IF PLAYER CHOSE PJS: POKERFIGURE is replaced with SMILEFIGURE.} "
  ##TODO {IF PLAYER CHOSE ONESIE: POKERFIGURE is replaced with ANGRYFIGURE.} "
  #
  ##HIDE ALL MINIGAME ASSETS
  #
  #hide  bg white
  #
  #scene cg limbokin
  #
  ##TODO {IF PLAYER CHOSE BATHROBE} "
  #
  #"The Limbokin loves your offer and counter-offers two teeth! "
  #
  ##menu:
  #"Do you accept or reject this counter-offer? "
  #
  #"Accept the counter-offer "
  #
  #"Congratulations! The trade has been closed! "
  #
  #"The Limbokin walks away, looking very happy. "
  #
  ##(X+2) #(Y+1) "
  #
  ##TODO {GO TO PART 21} "
  #
  #"Reject the counter-offer "
  #
  #"You decide to reject the counter-offer. "
  #
  #"The Limbokin walks away, looking dissatisfied. "
  #
  ##TODO {GO TO PART 21} "
  #
  ##TODO {IF PLAYER CHOSE PJS} "
  #
  #"The Limbokin likes your offer and counter-offers one tooth! "
  #
  ##menu:
  #"Do you accept or reject this counter-offer? "
  #
  #"Accept the counter-offer "
  #
  #"Congratulations! The trade has been closed! "
  #
  #"The Limbokin walks away, looking satisfied. "
  #
  ##(X+1) #(Y+1) "
  #
  ##TODO {GO TO PART 21} "
  #
  #"Reject the counter-offer "
  #
  #"You decide to reject the counter-offer. "
  #
  #"The Limbokin walks away, looking dissatisfied. "
  #
  ##TODO {GO TO PART 21} "
  #
  ##TODO {IF PLAYER CHOSE ONESIE} "
  #
  #"The Limbokin hates your offer and refuses to counter-offer! "
  #
  #"The Limbokin walks away, looking upset. "
  #
  ##TODO {GO TO PART 21} "
  
label lbl_minigame_5_Intro:
  #TODO {PART 21}"

  "The fifth Limbokin approaches! "

  "She's a middle-aged woman with a gentle smile on her heart-shaped face. "

  "Just like the grandma, she swoops down to pinch your cheeks. "

  "What is with the Limbokin and pinching cheeks?! "

  "You tell her she reminds you a bit of the grandma. "

  no5 "Really, I'm just like Gam-Gam? Makes sense! "

  no5 "Gam-Gam and I are related after all. I'm her actual daughter! "

  "Really? Wow. "

  no5 "No, not really. Hee-hee! "

  "Um, what? "

  #menu:
  #"What question should you ask? "
  #"How did you die? {GO TO PART 22} "
  #"How do you feel about life in purgatory? {GO TO PART 23} "
  #"What do you miss most about life on Earth? {GO TO PART 24} "

  #TODO {PART 22}"
  return

label lbl_minigame_5_Die:
  no5 "It was spontaneous combustion. "

  no5 "I was just relaxing in bed, waiting for the love of my life to return home from work. "

  no5 "Then, out of nowhere, I burst into flames! "

  "What?! Really?! "

  no5 "No, not really. Hee-hee! "

  no5 "I was making some soup for my wife. "

  no5 "Then I took a sip and keeled over. Dead. "

  no5 "You see, I was a very experimental cook. "

  #TODO {GO TO PART 25} "
  return

label lbl_minigame_5_Purgatory:

  #TODO {PART 23}"
  no5 "Oh, it's wonderful, dear. You'll enjoy it here. "

  no5 "If you need help with anything at all, feel free to approach me anytime. "

  no5 "I didn't have kids when I was alive. I've wondered what it's like to be a mother. "

  no5 "Oh! Will you let me adopt you? "

  "Really, she wants to adopt you? "

  no5 "No, not really. I don't want to! "

  no5 "I'm only pulling your leg! Hee-hee! "

  "What a weird woman. "

  #TODO {GO TO PART 25} "
  return

label lbl_minigame_5_Earth:

  #TODO {PART 24}"
  no5 "I miss my beloved more than everyone and everything on Earth combined. "

  no5 "You know I used to pole-dance for my wife, every night before going to bed? "

  no5 "I was an exotic dancer, but I happily retired to be a housewife. "

  no5 "My wife adored my dance routines! She was my biggest fan! "

  "Really? "

  no5 "Yes, really. "

  #TODO {GO TO PART 25} "
  return


  ##TODO {PART 25}"
  #
  #hide  cg limbokin
  #
  #show bg white
  #
  #"Which item should you offer? "
  #
  ##show MINIGAME ASSETS: POKERFIGURE, FISHNET, YOGA, APRON
  #
  ##MINIGAME FEATURE: Player must choose between FISHNET, YOGA, APRON. Player must drag and drop the chosen item over to POKERFIGURE.
  #
  ##TODO {IF PLAYER CHOSE FISHNET: POKERFIGURE is replaced with HEARTFIGURE.} "
  ##TODO {IF PLAYER CHOSE YOGA: POKERFIGURE is replaced with SMILEFIGURE.} "
  ##TODO {IF PLAYER CHOSE APRON: POKERFIGURE is replaced with ANGRYFIGURE.} "
  #
  ##HIDE ALL MINIGAME ASSETS
  #
  #hide  bg white
  #
  #scene cg limbokin
  #
  ##TODO {IF PLAYER CHOSE FISHNET} "
  #
  #"The Limbokin loves your offer and counter-offers two teeth! "
  #
  ##menu:
  #"Do you accept or reject this counter-offer? "
  #
  #"Accept the counter-offer "
  #
  #"Congratulations! The trade has been closed! "
  #
  #"The Limbokin walks away, looking very happy. "
  #
  ##(X+2) #(Y+1) "
  #
  ##TODO {IF Y<5: GO TO PART 26} "
  #
  ##TODO {IF Y=5: GO TO PART 36} "
  #
  #"Reject the counter-offer "
  #
  #"You decide to reject the counter-offer. "
  #
  #"The Limbokin walks away, looking dissatisfied. "
  #
  ##TODO {GO TO PART 26} "
  #
  ##TODO {IF PLAYER CHOSE YOGA} "
  #
  #"The Limbokin likes your offer and counter-offers one tooth! "
  #
  ##menu:
  #"Do you accept or reject this counter-offer? "
  #
  #"Accept the counter-offer "
  #
  #"Congratulations! The trade has been closed! "
  #
  #"The Limbokin walks away, looking satisfied. "
  #
  ##(X+1) #(Y+1) "
  #
  ##TODO {IF Y<5: GO TO PART 26} "
  #
  ##TODO {IF Y=5: GO TO PART 36} "
  #
  #"Reject the counter-offer "
  #
  #"You decide to reject the counter-offer. "
  #
  #"The Limbokin walks away, looking dissatisfied. "
  #
  ##TODO {GO TO PART 26} "
  #
  ##TODO {IF PLAYER CHOSE FISHNET} "
  #
  #"The Limbokin hates your offer and refuses to counter-offer! "
  #
  #"The Limbokin walks away, looking upset. "
  #
  ##TODO {GO TO PART 26} "
  
label lbl_minigame_6_Intro:
  #TODO {PART 26}"

  "The sixth Limbokin approaches! "

  "The boy just stands in front of you. "

  no6 ". . . "

  "You stick out your hand for a handshake. He shakes your hand. "

  "You ask him how he's doing. "

  no6 ". . . "

  "Seems like this is going to be harder than usual. "

  ##menu:
  #"What question should you ask? "
  #"How did you die? {GO TO PART 27} "
  #"How do you feel about life in purgatory? {GO TO PART 28} "
  #"What do you miss most about life on Earth? {GO TO PART 29} "

  return

label lbl_minigame_6_Die:
  #TODO {PART 27}"
  no6 ". . . "

  no6 "Choked. "

  "Oh, like on dinner or something? "

  "He doesn't say anything more. "

  #TODO {GO TO PART 30} "
  return

label lbl_minigame_6_Purgatory:

  #TODO {PART 28}"
  no6 ". . . "

  no6 "Okay. "

  "Okay? "

  "He doesn't say anything more. "

  #TODO {GO TO PART 30} "
  return

label lbl_minigame_6_Earth:

  #TODO {PART 29}"

  no6 ". . . "

  no6 "Life. "

  "So he misses life itself? What about life, specifically? "

  "He doesn't say anything more. "

  #TODO {GO TO PART 30} "
  return

label lbl_minigame_6_two_teeth:
    no6 ". . . Good pick. Don't talk much."
    "Yeah, you've noticed. "
    no6 "Want my clothes to talk for me. "
    no6 "Can give you two teeth."
    return

  ##TODO {PART 30}"
  #
  #hide  cg limbokin
  #
  #show bg white
  #
  #"Which item should you offer? "
  #
  ##show MINIGAME ASSETS: POKERFIGURE, XMAS, CABLEKNIT, TURTLENECK
  #
  ##"[MINIGAME FEATURE: Player must choose between XMAS, CABLEKNIT, TURTLENECK. Player must drag and drop the chosen item over to POKERFIGURE.
  #
  ##TODO {IF PLAYER CHOSE XMAS: POKERFIGURE is replaced with HEARTFIGURE.} "
  ##TODO {IF PLAYER CHOSE CABLEKNIT: POKERFIGURE is replaced with SMILEFIGURE.} "
  ##TODO {IF PLAYER CHOSE TURTLENECK: POKERFIGURE is replaced with ANGRYFIGURE.} "
  #
  #"[HIDE ALL MINIGAME ASSETS
  #
  #hide  bg white
  #
  #scene cg limbokin
  #
  ##TODO {IF PLAYER CHOSE XMAS} "
  #
  #no6 ". . . "
  #
  #no6 "Good pick. Don't talk much. "
  #
  #"Yeah, you've noticed. "
  #
  #no6 "Want my clothes to talk for me. "
  #
  #"The Limbokin loves your offer and counter-offers two teeth! "
  #
  ##menu:
  #"Do you accept or reject this counter-offer? "
  #
  #"Accept the counter-offer "
  #
  #"Congratulations! The trade has been closed! "
  #
  #"The Limbokin walks away, looking very happy. "
  #
  ##(X+2) #(Y+1) "
  #
  ##TODO {IF Y<5: GO TO PART 31} "
  #
  ##TODO {IF Y=5: GO TO PART 36} "
  #
  #"Reject the counter-offer "
  #
  #"You decide to reject the counter-offer. "
  #
  #"The Limbokin walks away, looking dissatisfied. "
  #
  ##TODO {GO TO PART 31} "
  #
  ##TODO {IF PLAYER CHOSE CABLEKNIT} "
  #
  #"The Limbokin likes your offer and counter-offers one tooth! "
  #
  ##menu:
  #"Do you accept or reject this counter-offer? "
  #
  #"Accept the counter-offer "
  #
  #"Congratulations! The trade has been closed! "
  #
  #"The Limbokin walks away, looking satisfied. "
  #
  ##(X+1) #(Y+1) "
  #
  ##TODO {IF Y<5: GO TO PART 31} "
  #
  ##TODO {IF Y=5: GO TO PART 36} "
  #
  #"Reject the counter-offer "
  #
  #"You decide to reject the counter-offer. "
  #
  #"The Limbokin walks away, looking dissatisfied. "
  #
  ##TODO {GO TO PART 31} "
  #
  ##TODO {IF PLAYER CHOSE TURTLENECK} "
  #
  #"The Limbokin hates your offer and refuses to counter-offer! "
  #
  #"The Limbokin walks away, looking upset. "
  #
  ##TODO {GO TO PART 31} "
  
label lbl_minigame_7_Intro:
  #TODO {PART 31}"

  "The seventh Limbokin approaches! "

  "Head held high, the last man grabs your hand and shakes it so hard you feel like you're in an earthquake. "

  no7 "I've been waiting for ages, my dear boy. "

  no7 "Chop-chop! Let's get to it! "

  no7 "This man has things to do, Limbokin to see! "

  #menu:
  #"What question should you ask? "
  #"How did you die? {GO TO PART 32} "
  #"How do you feel about life in purgatory? {GO TO PART 33} "
  #"What do you miss most about life on Earth? {GO TO PART 34} "

  return

label lbl_minigame_7_Die:
  #TODO {PART 32}"

  no7 "I don't look backward. Only forward. "

  "He puffs out his chest. "

  no7 "You'd be wise to follow my lead. "

  no7 "This theme of forward-thinking makes up the eighth chapter of my new book, coming out soon. "

  no7 "The book is called \"Don't Beat a Dead Horse: Lessons to Be Brave Beyond the Grave.\""

  no7 "I can have one of the Limbokin deliver a copy straight to you the moment it's out. "

  "Tempting, but no thanks. "

  #TODO {GO TO PART 35} "
  return

label lbl_minigame_7_Purgatory:

  #TODO {PART 33}"

  no7 "Everyone in purgatory has a story. "

  no7 "You, boy, what's your story? "

  "You open your mouth to tell him, but he quickly butts in. "

  no7 "My story is I'm a survivor. Knock me down a million times, and I'll get up a billion times. "

  no7 "This theme of survival makes up the seventh chapter of my new book, coming out soon. "

  no7 "The book is called \"Don't Beat a Dead Horse: Lessons to Be Brave Beyond the Grave.\""

  no7 "You see, I like everything in my life to tell a story. "

  no7 "From the way I walk, to the way I dress, to the way I carry myself each and every moment. "

  no7 "I want to inspire everyone with my actions, without even a single word. "

  "Without even a single word? Is that why he wrote an entire book? "
  #TODO {GO TO PART 35} "
  return

label lbl_minigame_7_Earth:

  #TODO {PART 34}"

  no7 "I do not miss what has gone. I only miss the opportunities I do not take. "

  no7 "I seize each moment, for each moment is a chance to transform into a better version of myself. "

  no7 "This theme of reinvention makes up the ninth chapter of my new book, coming out soon. "

  no7 "The book is called \"Don't Beat a Dead Horse: Lessons to Be Brave Beyond the Grave.\""

  no7 "I can have one of the Limbokin deliver a copy straight to you the moment it's out. "

  "You thank him for the offer, but you'll pass. "

  #TODO {GO TO PART 35} "
  return


  ##TODO {PART 35}"
  #
  #hide  cg limbokin
  #
  #show bg white
  #
  #"Which item should you offer? "
  #
  ##show MINIGAME ASSETS: POKERFIGURE, HALLOWEEN, STATEMENT
  #
  ##MINIGAME FEATURE: Player must choose between HALLOWEEN, STATEMENT. Player must drag and drop the chosen item over to POKERFIGURE.
  #
  ##TODO {IF PLAYER CHOSE HALLOWEEN: POKERFIGURE is replaced with SMILEFIGURE.} "
  ##TODO {IF PLAYER CHOSE STATEMENT: POKERFIGURE is replaced with ANGRYFIGURE.} "
  #
  ##HIDE ALL MINIGAME ASSETS
  #
  #hide  bg white
  #
  #scene cg limbokin
  #
  ##TODO {IF PLAYER CHOSE HALLOWEEN} "
  #
  #"The Limbokin likes your offer and counter-offers one tooth! "
  #
  ##menu:
  #"Do you accept or reject this counter-offer? "
  #
  #"Accept the counter-offer "
  #
  #"Congratulations! The trade has been closed! "
  #
  #"The Limbokin walks away, looking satisfied. "
  #
  ##(X+1) #(Y+1) "
  #
  ##TODO {GO TO PART 36} "
  #
  #"Reject the counter-offer "
  #
  #"You decide to reject the counter-offer. "
  #
  #"The Limbokin walks away, looking dissatisfied. "
  #
  ##TODO {GO TO PART 36} "
  #
  ##TODO {IF PLAYER CHOSE STATEMENT} "
  #
  #"The Limbokin hates your offer and refuses to counter-offer! "
  #
  #"The Limbokin walks away, looking upset. "
  #
  ##TODO {GO TO PART 36} "
  #
  ##TODO {PART 36}"

  #MINIGAME ENDS