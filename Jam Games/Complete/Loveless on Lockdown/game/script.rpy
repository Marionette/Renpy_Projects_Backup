# The script of the game goes in this file.


# The game starts here.

label start:
    show screen betatest_mode
    #Jump to the start of the game.
    jump lbl_part_01
    
    # This ends the game.

    return
    
label lbl_part_01:

  #reset variables
  $jian_romance = 0
  $grace_romance = 0
  $jian_route = False
  $grace_route = False

  play music online_subdued fadein 2.0

  scene cg laptop_video with slow_dissolve

  show mara poker #as side image"

  "It's Friday evening, and I'm video-conferencing with my family."

  "We're celebrating the second birthday of my nephew Mikel."

  show mara sad #as side image"

  "I can't lie, I'm tearing up. I'm blaming the pandemic and all its resulting restrictions in the Philippines."

  "Because of the COVID-19 crisis, I couldn't pay my brother and my sister-in-law any visits. "

  "I missed so many magical moments of my baby nephew growing up."

  "As I blubber to my family about all my regrets, they only laugh and tease me."

  Kuya "You should have landed a boyfriend before the lockdowns took effect! Then you wouldn't be so lonely right now!"

  show mara angry #as side image"

  Mara "Kuya! Why do you always bully me like this?"

  "My sister-in-law backs me up. Gently but firmly, she chides my brother. She tells him not to antagonize me."

  show mara poker #as side image"

  "But of course, my mother decides at this point to ventilate her unwanted opinions."

  Ma "Your Kuya has a point, you know? Mara, if only you weren't so stubborn! "

  Ma "If you listened to me when I told you to hurry up and tie the knot, who knows? "

  Ma "You could be in quarantine with a good husband right now! Maybe even with a child as cute as Mikel!"

  show mara angry #as side image"

  Mara "Ma, come on. How many times do I have to tell you? I had my reasons for ending things with Seph."

  Mara "Plus I don't want my own kids. Never did."

  show mara poker #as side image"

  Ma "You only {i}think{/i} you don't want kids. I thought so too, then I met your Papa. "

  Ma "Your Papa helped me understand why building a family and a home is important."

  Ma "Isn't that right, Pa?"

  "Pa only grunts. When Ma is going on a tirade like this, he doesn't like to interfere."

  "As for my sister-in-law, she also stays silent. "

  "Sure, my sister-in-law is sympathetic to my plight, but she gets that this discussion is confined to the immediate family."

  "Though stung by my mother's words, I put on a brave face as the conversation sputters out on a sour note. "

  show mara smile #as side image"

  "I smile as we all say our goodbyes."

  "Finally, I jab on the button to exit the video conference."

  #hide cg laptop_video

  stop music fadeout 1.0

  play music offline_subdued fadein 2.0

  scene bg bedroom_curtain with slow_dissolve

  show mara sad #as side image"

  "I blow out a massive sigh. "

  "What a downer ending to a birthday party."

  #hide bg bedroom_curtain

  scene cg laptop with slow_dissolve

  "Seeking solace now, I shoot a MatteApp message to wallflower95, my closest online friend."

  #hide cg laptop

  stop music fadeout 1.0

  play music online fadein 2.0

  #"START NVL MODE"
  scene cg laptop # Using the laptop as a background for NVL chats

  show mara angry #as side image"

  Marginalia "UGH I can't believe my mother!"

  wallflower95 "why, what happened?"

  Marginalia "Girl, she practically GUILT-TRIPPED me for dumping my ex-boyfriend! "


  Marginalia "Oh the sin of being single in my late twenties! I may as well be a shriveled old lady in my mother's eyes!"

  Marginalia "My ex was SO TOXIC! The freaking bane of my existence! "

  Marginalia "Kicking his controlling butt to the curb two years ago was the best decision I ever made!"

  wallflower95 "yes, men can truly be the worst."

  Marginalia "Gimme all your juicy stories about your ex-boyfriends! Wanna commiserate with someone who gets it!"

  wallflower95 "no ex-boyfriends, i'm afraid. my exes were women."

  show mara shock #as side image"

  Marginalia "WHAT!!!"

  Marginalia "You're a lesbian? Nice! Can't believe I'm only finding out now!"

  wallflower95 "regrettably, no. not a lesbian. i'm a man. as straight as they come."

  Marginalia "!!!"

  Marginalia "OMG why did I always assume you were a gal like me?"

  Marginalia "We vibed INSTANTLY when we first talked on the BTBB Pinoy forums! "

  Marginalia "Guess that's why I always saw you as the BFF I never had in my all-girls high school! I'm SO sorry!"

  show mara poker #as side image"

  wallflower95 "no, i get it. i'm used to it. i honestly don't mind."

  wallflower95 "most people in the btbb fandom are women, after all. this isn't the first time i've been mistaken as one. "

  Marginalia "I won't make the same mistake again! Promise!"

  wallflower95 "hey, don't sweat it. if you really want to make it up to me, let me lead our next co-op mission."

  show mara smile #as side image"

  Marginalia "You're on! Imma be the best support you've ever had! I won't go rogue this time, I swear!"

  wallflower95 "i'm looking forward to it."

  show mara poker #as side image"

  Marginalia "Logging out in a bit BTW. Gotta shop for my weekly groceries."

  wallflower95 "today? don't you usually go on saturdays?"

  Marginalia "Bruh, can't wait till tomorrow! I NEED ice cream! My comfort food! "

  Marginalia "Ice cream is my one true way to cheer up when I'm in a foul mood! Don't judge!"

  wallflower95 "haha, i'm not judging. take care of yourself out there."

  show mara smile #as side image"

  Marginalia "Talk to you later!"

  nvl clear
  nvl hide

  #END NVL MODE"

  stop music fadeout 1.0

  play music offline_subdued fadein 2.0

  scene bg bedroom_curtain with slow_dissolve

  show mara poker #as side image"

  "I rise from the bed. I snatch my bag and sweep everything I need inside it."

  "Last but definitely not least, I retrieve my freshly laundered cloth mask."

  #hide bg bedroom_curtain

  show bg bedroom_entrance with slow_dissolve

  "As I head for the door, I hook the elastics behind my ears, then adjust the mask so that it properly covers my nose. "

  show mara masked_poker #as side image"

  "Okay, time to go."

  #hide bg bedroom_entrance

  show bg elevator with slow_dissolve

  show jian masked_poker at center with dissolve

  "As I enter the elevator to head down, I nod at the single person standing inside. "

  "The guy makes no response whatsoever."

  "The elevator stops at a lower floor to let in an older woman. Because of the three-person limit, there won't be any more stops."

  "For some reason, the woman is glaring daggers at the guy. But he doesn't respond to her either."

  "Seemingly incensed due to being ignored, the woman whips out her smartphone."

  "She starts speaking loudly. Obnoxiously."

  stop music fadeout 1.0

  Woman "{i}Mare,{/i} remind me to speak to the admin of the Goldray Apartment when I get back. I need to file a complaint."

  show mara masked_shock #as side image"

  show jian masked_shock at center

  Woman "How can they allow {i}mainland Chinese{/i} to continue living in this building?"

  Woman "{i}Mare,{/i} I'm telling you. The sheer irresponsibility! The incompetence!"

  "I notice the guy flinching while listening to these words. "

  show mara masked_poker #as side image"

  show jian masked_blush at center

  "Feigning indifference, he takes his phone from his pocket, but his ears have flushed red."

  "Should I speak up? If I make a big deal out of this, I may risk making the poor guy feel even more uncomfortable."

  menu:
    "Stand up for the stranger.":
      jump lbl_part_02
    "Mind my own business.":
      jump lbl_part_03

label lbl_part_02:

  $ jian_romance += 1

  "That's right! I need to stand up for what's just!"

  "I press my phone against my ear and commence speaking loudly to absolutely no one."

  play music chaotic fadein 2.0

  show mara masked_angry #as side image"

  Mara "Hello? Is this the admin office of the Goldray Apartment? I need to file a complaint."

  Mara "Yes, for the past two years I've lived here, I've had no major issues. However, the admin has been sloppy as of late."

  Mara "How can you permit {i}racists{/i} and {i}bigots{/i} to reside in this building? How irresponsible! How incompetent!"

  show jian masked_shock at center

  "The woman freezes. "

  "Slowly, she turns toward me, her expression as sour as calamansi. "

  "With my mission of getting her to shut up accomplished, I now say a brusque goodbye to my phone."

  show mara masked_poker #as side image"

  show jian masked_poker at center

  "Grumbling, the woman escapes from the elevator once we reach the next floor, although that obviously wasn't her original stop."

  stop music fadeout 1.0

  "As for the guy, he simply keeps staring down at his phone."

  "Sure, I don't expect to be thanked. But it would be nice to at least be acknowledged."

  hide jian

  jump lbl_part_04

label lbl_part_03:

  "Yes, I should mind my own business. "

  "For this guy's sake, I shouldn't make this situation more awkward than it already is."

  "The woman keeps saying rude things over the phone. "

  "Her voice rings out, as grating as nails on a chalkboard, in the otherwise silent elevator."

  "God, I can't wait to get out of here."

  hide jian

  jump lbl_part_04

label lbl_part_04:

  #hide bg elevator

  play music offline fadein 2.0

  show bg grocery_night with slow_dissolve

  "Careful to abide by all the applicable health and safety protocols, I shop for my weekly necessities."

  "Next stop, the frozen foods section."

  "I can't wait to get home and dig into some scrumptious ice cream. Yum!"

  "On the way to the frozen foods section, however, I pause to admire the juicy apples in the fruit stall."

  "There are no other customers here, so I saunter forward to more closely examine the luscious red fruits."

  "Just then, a pleasant voice calls my attention. I raise my head to look."

  show mara masked_shock #as side image"

  show grace masked_poker_apron at center with dissolve

  Stranger "What can I get you? Fuji apples? Red Delicious?"

  "Such wide eyes. Full of soul. Depth. Expression."

  show mara masked_blush #as side image"

  "Even though I can only see half of this man's face, I can tell that he's my ideal type."

  "Who knew that such dreamboats worked here on weekdays? From now on, I should do my groceries every Friday!"

  "The stranger squints at my stupefied expression. He repeats his question."

  Stranger "Can I get you anything?"

  "Without thinking, I blurt out a response."

  Mara "Your name?"

  show grace masked_shock_apron at center

  "In apparent confusion, the stranger raises his eyebrows. "

  "His voice comes out muffled due to his mask."

  show grace masked_poker_apron at center

  Stranger "Gray."

  "Belatedly, I'm struck by the weirdness of my own behavior for the entirety of this interaction. "

  "I scurry away without another word. "

  hide grace

  "Off to the frozen foods section!"

  stop music fadeout 1.0

  play music offline_subdued fadein 2.0

  show mara masked_poker #as side image"

  "As I'm stacking cartons of my favorite ice cream brand in my shopping cart, my family's words reverberate around my skull. "

  "{i}So lonely,{/i} my brother called me."

  "{i}So stubborn,{/i} said my mother."

  "As infuriating as they can be, they may have a point. Maybe I {i}am{/i} lonely. Maybe I {i}am{/i} too stubborn."

  "Maybe this moment is fate, and I shouldn't keep fighting it."

  "Should I just go for it? Should I take this reckless shot at romance?"

  menu:
    "Make a move on the stranger.":
      jump lbl_part_05
    "Don't make a fool of myself.":
      jump lbl_part_09

label lbl_part_05:

  stop music fadeout 1.0

  play music offline fadein 2.0

  $ grace_route = True

  "Yes, it's now or never! "

  "If there's one lesson this pandemic has taught the world, it's that life is often short, often unfair!"

  "I need to take this risk while I still can! I need to make my move!"

  "A bottle of hand sanitizer is dangling from a keychain on my bag. "

  "I rub the citrusy substance on my palms. 60\% alcohol, as recommended by the public health authorities. "

  "I then take a notepad and a ballpen from my bag."

  "What can I say to make an impression? What should I write to the handsome stranger?"

  menu:
    "Write something flirty.":
      jump lbl_part_06
    "Write something polite.":
      jump lbl_part_07

label lbl_part_06:

  $ grace_romance += 1

  "Yes, flirty is the way to go, if I want to be unforgettable."

  "I write, {i}Hey there! Just gonna come out and say it. You're super cute.{/i}"

  "{i}If you feel like it, why don't we talk sometime? My MatteApp username is Marginalia.{/i}"

  jump lbl_part_08

label lbl_part_07:

  "Yes, it's safest to be prim and proper. I don't want to scare him away, after all."

  "I write, {i}Good evening! I hope you don't find this too forward, but I'd love to get to know you.{/i}"

  "{i}If this appeals to you too, please let me know. My MatteApp username is Marginalia.{/i}"

  jump lbl_part_08

label lbl_part_08:

  "I rip the sheet from the notepad and fold it twice."

  "I take a deep breath, then walk back to the fruit stall."

  stop music fadeout 1.0

  play music chaotic fadein 2.0

  show mara masked_blush #as side image"

  show grace masked_poker_apron at center with dissolve

  "Upon seeing that I've returned, the handsome stranger cocks his head to the side."

  "I'm not surprised by his bewilderment. My behavior earlier was undoubtedly bizarre."

  Stranger "Have you decided on what you want?"

  "I make a big show of slathering hand sanitizer all over my hands again. "

  "Only then do I carefully balance the folded note on top of a Honeycrisp apple."

  show grace masked_shock_apron at center

  Mara "This is for you, Sir!"

  "Without waiting for the stranger's reaction, I walk away once more."

  hide grace

  "My heart is hammering now, loudly enough that everyone else in the grocery must hear it too. "

  "Wow! What a rush!"

  show mara masked_poker #as side image"

  jump lbl_part_10

label lbl_part_09:

  stop music fadeout 1.0

  play music offline fadein 2.0

  $ jian_route = True

  "Right, I shouldn't make a fool of myself. "

  "I shouldn't act so desperate just because my family likes to torment me."

  "Besides, I'm blowing everything out of proportion. This isn't fate. This is only a regular old Friday."

  jump lbl_part_10

label lbl_part_10:

  "I head to the cash register to pay for my items. I then go home for the night."

  #hide bg grocery_night

  stop music fadeout 1.0

  play music offline_subdued fadein 2.0

  show bg bedroom_curtain with slow_dissolve

  show mara smile #as side image"

  "Back home, I unwind with a carton of rocky road ice cream by my side."

  "I'm playing Bubble Tea Brewer Bros, my favorite game in the world."

  #hide bg bedroom_curtain

  scene cg laptop_game with slow_dissolve

  show mara poker #as side image"

  "As I'm watering my pixelated plants, my laptop pings. "

  "It's a new message on MatteApp from wallflower95."

  if jian_route == True:
    jump lbl_part_11
  if grace_route == True:
    jump lbl_part_12

label lbl_part_11:

  "I open the new message."

  #hide cg laptop

  stop music fadeout 1.0

  play music online fadein 2.0

  #"START NVL MODE"
  scene cg laptop_game # Using the laptop as a background for NVL chats

  show mara smile #as side image"

  wallflower95 "not playing btbb tonight?"

  Marginalia "I'm logged in, actually! Just in invisible mode."

  wallflower95 "i see. how's your ice cream, incidentally?"

  Marginalia "Heaven. PURE HEAVEN. Thanks for asking!"

  wallflower95 "are you full yet?"

  Marginalia "I imagine it would take about TEN cartons of this deliciousness to make me full! "

  show mara poker #as side image"

  Marginalia "Why do you ask?"

  wallflower95 "because you'll need to eat a slice of humble pie. "

  wallflower95 "how else will you serve as the second-in-command for our co-op mission?"

  show mara smile #as side image"

  Marginalia "LMAO can I take a rain check on missions? Postpone the wild fun till next time?"

  Marginalia "I'm feeling a relaxing grind tonight. Farming, brewing, redecorating my cottage. That sorta stuff."

  wallflower95 "yeah, no problem. can i still talk your ear off, even if you're in full relaxation mode?"

  show mara shock #as side image"

  Marginalia "DUDE. Do you even have to ask? "

  Marginalia "I'm your designated sounding board, aren't I?"

  show mara smile #as side image"

  Marginalia "You know what they say. Even if your bestie talks one ear off, you have another ear left. That's why God gave us two ears."

  wallflower95 "ah yes, that very popular and enduring saying."

  stop music fadeout 1.0

  play music online_subdued fadein 2.0

  show mara poker #as side image"

  Marginalia "So what's up?"

  wallflower95 "today i was pissed off about something. long story. point is, my mind spiraled back to that dark place."

  show mara sad #as side image"

  Marginalia ":("

  Marginalia "Are you OK?"

  show mara poker #as side image"

  wallflower95 "yeah, i'm feeling much better now. don't worry about it."

  wallflower95 "but around an hour ago? i felt so alone."

  wallflower95 "i badly needed to talk to someone. so of course i called my therapist."

  Marginalia "And? What did she tell you?"

  wallflower95 "nothing. i received an automated voice message - the number you have dialed is out of service."

  stop music fadeout 1.0

  play music online fadein 2.0

  show mara shock #as side image"

  Marginalia "OMG that sucks!"

  show mara poker #as side image"

  wallflower95 "what can i say? that automated response did wonders for my colorful history of abandonment issues. haha."

  wallflower95 "anyway, my therapist emailed to explain. her smartphone had been hacked, so she had her line disconnected."

  Marginalia "Oh boy. I get it, though. I've heard that cyberattacks have been getting more and more aggressive lately."

  wallflower95 "as a programmer, i can confirm that the shadowy cabal of cybercriminals is thriving these days. "

  wallflower95 "but i haven't gotten to the best part of the story yet."

  show mara shock #as side image"

  Marginalia "Oh the SUSPENSE! Tell me NOW!"

  show mara poker #as side image"

  wallflower95 "when sending the email, my therapist forgot to use the BCC feature. "

  wallflower95 "in other words, every client's email address was broadcasted to all other clients."

  wallflower95 "so much for doctor-patient confidentiality, huh?"

  show mara shock #as side image"

  Marginalia "!!!"

  Marginalia "Y I K E S ! ! !"

  wallflower95 "i even recognized a couple of recipients, one of whom i used to see in the office every day before the quarantine."

  Marginalia "Double Y I K E S ! ! !"

  show mara poker #as side image"

  wallflower95 "double yikes is right. "

  stop music fadeout 1.0

  play music online_subdued fadein 2.0

  wallflower95 "if nothing else, that major blunder showed me that i'm not the only one struggling."

  wallflower95 "if i have to suffer, at least i'm suffering with twenty others. i'm not alone."

  show mara smile #as side image"

  Marginalia "OF COURSE you're not alone! I'm always here for you! Don't you ever forget that!"

  wallflower95 "thanks. i really appreciate it."

  wallflower95 "hey, can i say something? something that's a little cheesy, i suppose?"

  Marginalia "Sure! I happen to LOVE cheese! Give me a good chunk of gouda, and I'll DEMOLISH it gladly!"

  wallflower95 "haha, good to know."

  show mara poker #as side image"

  wallflower95 "ok, here's the thing. i'm so thankful that i met you this year. "

  wallflower95 "with the pandemic and all, things have been harder on me, as it has been on everybody. "

  wallflower95 "everything sucks, sure. but at least i got to know you."

  show mara blush #as side image"

  wallflower95 "it means so much to me. just knowing i have someone with whom i can play games or talk nonsense."

  wallflower95 "someone to whom i can rant without being judged."

  wallflower95 "so thank you. thank you for being you."

  nvl clear
  nvl hide

  #END NVL MODE"

  stop music fadeout 1.0

  play music offline_subdued fadein 2.0

  scene cg laptop_game with slow_dissolve

  show mara sad #as side image"

  "wallflower95's words are turning blurry. I only then realize that my eyes are swimming."

  "I understand what he means because that's how I feel about him too. "

  "I can tell him this, but I suspect he already knows. "

  show mara poker #as side image"

  "How many times have I ranted to him about Kuya or Ma or Pa getting on my nerves? "

  "How many times have I moaned to him about the repetitive aspects of my work as a freelance researcher?"

  show mara smile #as side image"

  "I perk up as an idea comes to me. Something I can do instead of telling him something he already knows."

  "I can send him a gift on BTBB! Funky decor he can display in his cottage!"

  #hide cg laptop

  stop music fadeout 1.0

  play music online fadein 2.0

  #"START NVL MODE"
  scene cg laptop_game # Using the laptop as a background for NVL chats

  show mara blush #as side image"

  Marginalia "OK listen up. I gotta tell you three things. "

  Marginalia "One, your cheese is the tastiest kind of cheese. I mean WTF you're making me tear up here!"

  Marginalia "Two, you are the literal BEST. My favorite part of 2020 BY FAR."

  Marginalia "Three, to show you how much I appreciate you, I'm sending you something on BTBB. Keep an eye out."

  wallflower95 "i'm only saying this stuff because it's true."

  wallflower95 "can't wait to see what you're sending me. my eyes are wide. my body is ready."

  nvl clear
  nvl hide

  #END NVL MODE"

  stop music fadeout 1.0

  play music offline fadein 2.0

  scene cg laptop_game with slow_dissolve

  show mara smile #as side image"

  "With a smile, I make my BTBB avatar go to the cottage improvement shop. I chat up the shop owner. "

  "I then scroll past the cheaper decor to get to the gold-tier offerings."

  show mara poker #as side image"

  "wallflower95 likes all shades of purple, so a lava lamp of that color may work. "

  "On the other hand, a flamingo chair may match the kitsch aesthetic of his cottage."

  menu:
    "Buy the lavender lava lamp.":
      jump lbl_part_13
    "Buy the flamingo wrought-iron chair.":
      jump lbl_part_14

label lbl_part_12:

  "Before I can open the new message, another ping from my laptop alerts me."

  "It's a message request from ChainCustard404, a username I don't recognize."

  show mara shock #as side image"

  "Can this be who I think it is?"

  "I swallow. My throat is suddenly as dry as a desert."

  "Taking a deep breath, I accept the request, then open the new message from ChainCustard404."

  #hide cg laptop

  stop music fadeout 1.0

  play music online fadein 2.0

  #"START NVL MODE"
  scene cg laptop # Using the laptop as a background for NVL chats

  show mara blush #as side image"

  ChainCustard404 "Hey!! :3 it's me from the grocery!! "

  Marginalia "Hey there!"

  ChainCustard404 "Course I wouldn't mind getting to know u!! Let's be friends!! We can all use a friend in the time of corona, right??"

  Marginalia "OH I'm glad! "

  show mara smile #as side image"

  Marginalia "I was SO worried I came across as a stalker earlier! I was just about to drown myself in melted ice cream and shame!"

  ChainCustard404 "Lol don't be silly!! What u did was so so brave :O"

  ChainCustard404 "I could never walk up to someone like that out of nowhere!! Ur my hero now lol <3"

  ChainCustard404 "How do u wanna go about this?? Been a while since I made a new friend :))"

  Marginalia "UGH me too! As you could probably tell earlier, my social skills have gone WHACK. "

  show mara poker #as side image"

  Marginalia "Guess we should get the basics out of the way? I'm Mara. 27 years old. I work as a freelance researcher."

  ChainCustard404 "Nice to meet u mara!!"

  Marginalia "And you're Gray, right? Or is it Grey?"

  ChainCustard404 "Umm either is fine :)) i'm not picky about spelling!!"

  ChainCustard404 "23 y/o. I work the 2-10pm weekday shift at the grocery!!"

  ChainCustard404 "Then I work toward my masters degree in the morning!! Online ofc :)"

  show mara smile #as side image"

  Marginalia "Wow! That's super cool! That must take A LOT of energy!"

  ChainCustard404 "Thanks it does but it's worth it for sure!! I'm that rare animal who enjoys both work and study :3"

  Marginalia "What are you studying, if I may ask?"

  ChainCustard404 "Inclusive education <3 "

  ChainCustard404 "I took math in college but volunteered for a disability org!! Discovered my passion there!!"

  ChainCustard404 "So even tho it's stressful every day i'm grateful to be chasing my dream :D"

  Marginalia "You're so lucky! "

  show mara poker #as side image"

  Marginalia "As for me, I don't know IF I even have a realistic dream, let alone HOW to go about chasing it."

  Marginalia "I just get by. Work, eat, sleep. Work, eat, sleep. Repeat unto infinity."

  ChainCustard404 "Oh do u hate ur job?? That's hard :("

  Marginalia "My research work is whatever. I don't like or dislike it. "

  Marginalia "It does pay the bills. Plus it allows me to make in-game purchases in BTBB."

  show mara smile #as side image"

  Marginalia "Do you play BTBB?"

  ChainCustard404 "What's that??"

  Marginalia "Bubble Tea Brewer Bros. It's pretty popular. The fandom is surprisingly active, especially for an indie game."

  ChainCustard404 "Never heard of it sorry :( sadly not much of a gamer :'("

  show mara shock #as side image"

  Marginalia "NO it's fine! "

  show mara smile #as side image"

  Marginalia "It's not like I expect everybody to enjoy or to even understand my niche interests!"

  Marginalia "I approached you because I was interested in getting to know YOU, after all!"

  ChainCustard404 "What do u wanna know?? :)"

  ChainCustard404 "No wait I have an idea!! There's this cool way to skip all the boring stuff and get real close real fast :D"

  ChainCustard404 "Gimme a few minutes ok?? Gonna message my pal who remembers this sorta stuff way better than I can!!"

  nvl clear
  nvl hide

  #END NVL MODE"

  stop music fadeout 1.0

  play music offline fadein 2.0

  show bg bedroom_curtain with slow_dissolve

  show mara blush #as side image"

  "As I'm waiting, I glance up from my laptop. I'm telling myself not to freak out."

  "Not only is Gray totally my type, but he's driven and passionate too? Plus shockingly easy to talk to? "

  "Can he get any more perfect? Seriously!"

  "I haven't been to church since several Christmases ago, but I'm overcome by the urge to start singing {i}Alleluia!{/i}"

  "I'm flailing over my bed and making squealing noises. "

  show mara shock #as side image"

  "Then an idea hits me. "

  "The best idea in the world, or the worst ever, depending on the response."

  show mara smile #as side image"

  "Should I send Gray a selfie? People do that, right? Friends? Strangers on their way to being friends?"

  "Besides, didn't Gray himself say that he wanted to skip all the boring stuff? Doesn't he want to get really close, really fast?"

  show mara poker #as side image"

  "Fluffing up my hair, I pick up my phone. Here I go!"

  "Gray seems like the playful type, so should I make him laugh? Or should I just take a regular photo without any gimmicks?"

  menu:
    "Take a funny selfie.":
      jump lbl_part_16
    "Take a basic selfie.":
      jump lbl_part_17

label lbl_part_13:

  show mara smile #as side image"

  "Let's go for the lavender lava lamp!"

  "Upon completing the transaction, I send the gift to wallflower95."

  "I go on MatteApp again to see whether wallflower95 appreciates his new decor."

  #hide cg laptop

  stop music fadeout 1.0

  play music online fadein 2.0

  #"START NVL MODE"
  scene cg laptop_game # Using the laptop as a background for NVL chats

  show mara blush #as side image"

  Marginalia "So what do you think?"

  wallflower95 "this is a very rad gift from a very rad person. thanks a lot."

  show mara smile #as side image"

  Marginalia "I even got it in your favorite color!"

  wallflower95 "yeah, i noticed. i'm putting it in the living room. right beneath my jellyfish chandelier."

  Marginalia "Nice! This way, whenever guests come over, you can have an impromptu PARTY in your living room!"

  jump lbl_part_15

label lbl_part_14:

  $ jian_romance += 1

  show mara smile #as side image"

  "Let's go for the flamingo wrought-iron chair!"

  "Upon making my purchase, I send the gift to wallflower95."

  "I then check MatteApp to see whether wallflower95 is liking his new decor."

  #hide cg laptop

  stop music fadeout 1.0

  play music online fadein 2.0

  #"START NVL MODE"
  scene cg laptop_game # Using the laptop as a background for NVL chats

  show mara blush #as side image"

  Marginalia "So what do you think?"

  wallflower95 "asdfjkglgk"

  show mara poker #as side image"

  Marginalia "Positive keysmash or negative keysmash?"

  wallflower95 "are you kidding me? positive. of course."

  show mara smile #as side image"

  wallflower95 "it's amazing how well you can read me. i was saving up for that chair exactly. thanks so much."

  Marginalia "No prob! Where you putting it?"

  wallflower95 "right beside my bed. it's perfect. "

  wallflower95 "sending you a screenshot, hang on."

  show mara shock #as side image"

  Marginalia "OMG!"

  Marginalia "It looks ridiculous! And by ridiculous I do mean ridiculously GOOD!"

  show mara smile #as side image"

  Marginalia "Whenever your avatar wakes up and sees it, it's gonna hit her like a shot of espresso. "

  Marginalia "She'll jump from the bed and just FLAMINGO-GO-GO!"

  jump lbl_part_15

label lbl_part_15:

  wallflower95 "yep. my thoughts exactly."

  wallflower95 "btw i'm thinking of visiting olivieri's popping boba factory tonight. wanna come with?"

  Marginalia "Yeah, let's DO IT! I miss that orange orangutan already! That lovable goofball!"

  wallflower95 "haha, it's not enough for you to sleep next to a giant plush of olivieri?"

  Marginalia "Olivieri is STILL the best Christmas gift I've ever given myself. "

  Marginalia "All the companionship I crave with none of the risks. Your Honor, I rest my case."

  nvl clear
  nvl hide

  #END NVL MODE"

  jump lbl_part_19

label lbl_part_16:

  "Yeah! If I can make my new crush laugh, then I can call tonight a victory!"

  "I scoot back in bed to grab Olivieri, my giant plush of an orange orangutan. "

  "Olivieri is a character from BTBB, which Gray doesn't know. Even so, that toothy smile alone will make anyone giggle, right?"

  show mara smile #as side image"

  "I position the orangutan's arm over my shoulder and mimic its goofy grin before snapping a photo. "

  "That should do it!"

  #hide bg bedroom_curtain

  scene cg laptop with slow_dissolve

  show mara poker #as side image"

  "Back on MatteApp, I send the selfie to Gray, accompanied by a short message."

  "{i}Just me and my fur baby, striking a pose for the camera!{/i}"

  "A minute passes before my laptop pings again."

  #hide cg laptop

  stop music fadeout 1.0

  play music online fadein 2.0

  #"START NVL MODE"
  scene cg laptop # Using the laptop as a background for NVL chats

  show mara blush #as side image"

  ChainCustard404 "Cute!! :D what's ur furbaby's name??"

  ChainCustard404 "U got any real pets??"

  show mara smile #as side image"

  Marginalia "Olivieri the Orangutan! And it's just Olivieri and I over here, unfortunately. "

  Marginalia "My apartment doesn't allow tenants to keep pets."

  ChainCustard404 "Aww that's too bad!! i'd show u my kitty but unlike ur oliveri she's too squirmy to take a selfie with D:"

  Marginalia "LMAO you can always send me a selfie with just you!"

  Marginalia "Or just the cat! Whichever!"

  ChainCustard404 "Maybe next time :)"

  jump lbl_part_18

label lbl_part_17:

  $ grace_romance += 1

  "Yeah! I should just be myself and {i}look{/i} like myself, without trying too hard or going too far!"

  show mara smile #as side image"

  "I take a selfie with my usual smile. "

  "My eyes may crinkle a bit at the sides, but that will only prove that I'm being sincere, right?"

  #hide bg bedroom_curtain

  scene cg laptop with slow_dissolve

  show mara poker #as side image"

  "On MatteApp, I send the photo to Gray with a short message."

  "{i}Felt like sending you this. No reason. No pressure to send anything back!{/i}"

  show mara shock #as side image"

  "When my laptop pings again, I gasp. "

  "Gray has sent a selfie in return! "

  show mara blush #as side image"

  "He's wearing a mask, just like earlier in the grocery, but it's a selfie nonetheless!"

  "Oh my God! He's so dreamy! He's way prettier than I am!"

  #hide cg laptop

  show bg bedroom_curtain with slow_dissolve

  "I'm back to squealing and flailing over the bedsheets again. "

  "In my excitement, I'm practically squeezing the stuffing out of Olivieri, my giant orange orangutan plush."

  "The real Olivieri, a character from BTBB, would never stand for such manhandling, that's for sure."

  "It's a hot minute before I calm down enough to type a coherent message to Gray."

  #hide bg bedroom_curtain

  stop music fadeout 1.0

  play music online fadein 2.0

  #"START NVL MODE"
  scene cg laptop # Using the laptop as a background for NVL chats

  show mara smile #as side image"

  Marginalia "I'm sure you must get this all the time, but I just gotta say it. You're so handsome! "

  ChainCustard404 "Lol it's the first time someone's used that word to describe me actually!! But thank u :3"

  ChainCustard404 "Ur so pretty so ofc I had to return the favor <3 "

  show mara blush #as side image"

  ChainCustard404 "Even my kitty thinks so!! She meowed at my laptop just now :))"

  Marginalia "STOP!!! "

  Marginalia "You should see my face, I'm blushing so much it's EMBARRASSING!!!"

  ChainCustard404 "Hehe ur welcome ;)"

  jump lbl_part_18

label lbl_part_18:

  show mara poker #as side image"

  ChainCustard404 "Btw I just realized I have a bunch of errands to do tmrw :O gotta go to bed soon!!"

  ChainCustard404 "But my pal helped me find the thingy I was looking for!! "

  ChainCustard404 "So i'll send u the link once I get back home tmrw!! Promise :)"

  show mara smile #as side image"

  ChainCustard404 "Good night mara!!"

  Marginalia "Good night, Gray!"

  nvl clear
  nvl hide

  #END NVL MODE"

  stop music fadeout 1.0

  play music offline_subdued fadein 2.0

  scene cg laptop with slow_dissolve

  show mara poker #as side image"

  "Once Gray has logged out, I check my unread messages from wallflower95."

  "His first message asks whether I'm playing BTBB tonight."

  "A subsequent message questions whether I'm down for a co-op mission."

  "I reply that I'm currently logged into the game, except in invisible mode."

  "wallflower95 sends no further messages. Perhaps he's gone to bed, just like Gray."

  show mara smile #as side image"

  "I'll get back to wallflower95 next time. That co-op mission I promised him should be fun."

  #hide cg laptop

  jump lbl_part_19

label lbl_part_19:

  stop music fadeout 1.0

  play music offline fadein 2.0

  show bg bedroom_day with slow_dissolve

  show mara poker #as side image"

  "It's the next day. Saturday. A lazy afternoon. "

  "Like most other weekends in the year of our Lord and Savior 2020, I'm bummed out in bed and waiting for my life to get started."

  "I'm checking out random TV shows. Stuff I see acquaintances raving about across various social media platforms."

  "As a particularly boring KismetFlix series drones on, I scroll through various group chats on my phone."

  "When my friends tag me in memes, I reply with laugh-cry emojis. I've seen these jokes before, but it's the thought that counts."

  show mara shock #as side image"

  "MatteApp now alerts me to a new message. "

  "Ah! It's from the one person I've been waiting all day to see online!"

  show mara smile #as side image"

  "I jolt out of my lethargic state. A smile instantly spreads over my face."

  #hide bg bedroom_day

  if jian_route == True:
    jump lbl_part_20
  if grace_route == True:
    jump lbl_part_24

label lbl_part_20:

  stop music fadeout 1.0

  play music online fadein 2.0

  #"START NVL MODE"
  scene cg laptop # Using the laptop as a background for NVL chats

  wallflower95 "i liked your gift so much that i posted a btbb screenshot on my only social media account with my real name."

  wallflower95 "believe me, i was ready to be ignored, or to be called out as the weeb i am. but that's not what happened."

  show mara shock #as side image"

  Marginalia "OOH what happened then?"

  show mara poker #as side image"

  wallflower95 "surprise, surprise. the comments were actually positive."

  wallflower95 "a few closet btbb players crawled out of the woodwork to express their envy for my gold-tier decor."

  show mara shock #as side image"

  Marginalia "AHH I wanna read the comments! Link it to meeeee!"

  Marginalia "Oh, wait. The account has your real name, doesn't it? Never mind then!"

  show mara smile #as side image"

  Marginalia "LMAO I'm not a scammer trying to trick you into divulging your personal info!"

  wallflower95 "nah, it's fine. i don't mind you finding out my name."

  show mara poker #as side image"

  wallflower95 "my name's so dull and generic as to be virtually unstalkable."

  wallflower95 "plus, i'm a nobody. haha."

  wallflower95 "i'm more self-conscious about my appearance. but my account doesn't have any photos like that."

  nvl clear
  nvl hide

  #END NVL MODE"

  stop music fadeout 1.0

  play music online_subdued fadein 2.0

  scene cg laptop with slow_dissolve

  show mara smile #as side image"

  "I click on the PhaseNook link that wallflower95 sends me. My eyes immediately gravitate toward his name."

  "Jian Zhang. He may have called it dull, but to my ears, at least, the name has a nice ring to it."

  "As he claimed, he doesn't display images of his face. "

  "But there are other photos posted from before the COVID-19 outbreak. "

  "Streets bustling with pedestrians. "

  "A shopping district strung with fairy lights for the holiday season. "

  "A concrete overpass in shadow, against a backdrop of an urban sunset. Fiery yellows and oranges."

  show mara blush #as side image"

  "All these sights are so achingly familiar. "

  "Is it possible that wallflower95 and I have lived in the same city this entire time?"


  show mara shock #as side image"

  "A ping from my laptop. I just then remember what I'm supposed to be looking at. Ack!"

  show mara poker #as side image"

  "I scroll swiftly through the comments section of the BTBB screenshot that wallflower95 posted."

  #hide cg laptop

  stop music fadeout 1.0

  play music online fadein 2.0

  #"START NVL MODE"
  scene cg laptop # Using the laptop as a background for NVL chats

  show mara smile #as side image"

  wallflower95 "so what do you think? "

  Marginalia "YEAH BOY let 'em all know know you're an alpha in the wild world of BTBB!"

  wallflower95 "alpha? haha. now that's definitely a word no one but you would ever use to describe me."

  show mara poker #as side image"

  Marginalia "BTW I don't mean to be creepy, but I just have to ask. "

  Marginalia "You don't live in Pasig, do you? Or at least close to the city?"

  Marginalia "OMG I sound like a stalker! I'm just guessing based on the photos you posted!"

  wallflower95 ". . . . . . . . . ."

  show mara shock #as side image"

  Marginalia "AHHH SORRY I'll shut up now! I swear!"

  wallflower95 "fine. yes. i live in pasig. do you live here too?"

  show mara smile #as side image"

  Marginalia "Yep! At Ortigas Center!"

  wallflower95 "same. that's so weird. never would have guessed we'd be this close."

  Marginalia "Yeah TBH I'm freaking out a bit over here. Or freaking out A LOT."

  show mara poker #as side image"

  Marginalia "Can I ask you something?"

  wallflower95 "sure, ask me anything."

  Marginalia "Would you ever wanna meet up? "

  Marginalia "I mean, not right now. Not when a pandemic is raging and people are dying. Obviously."

  wallflower95 "obviously."

  Marginalia "But hypothetically, would you? People do meet up with their online friends IRL. It happens all the time."

  wallflower95 "hmm. what do you think? do you want to meet me in person?"

  show mara smile #as side image"

  Marginalia "Nice try! I asked you first!"

  wallflower95 "haha, be that as it may, i won't answer your question unless you answer first."

  nvl clear
  nvl hide

  #END NVL MODE"

  stop music fadeout 1.0

  play music offline fadein 2.0

  scene cg laptop with slow_dissolve

  show mara blush #as side image"

  "For some reason or another, my heart is thumping loudly now."

  "While wallflower95 and I have always gotten along effortlessly, we've never talked about such things."

  "Seeing my closest online friend, face-to-face. Why does such a simple prospect make me feel this way?"

  show mara poker #as side image"

  "What should I say? Should I tell wallflower95 I want to see him? What if I end up scaring him away?"

  "Besides, don't I enjoy the way things are right now? I don't want him to suspect that I've had motives beyond friendship. "

  menu:
    "Tell him we should meet up sometime.":
      jump lbl_part_21
    "Tell him I'm satisfied with the way we are now.":
      jump lbl_part_22

label lbl_part_21:

  $ jian_romance += 1

  "Yeah, I should just go for it. Be honest about my feelings."

  #hide cg laptop

  stop music fadeout 1.0

  play music online fadein 2.0

  #"START NVL MODE"
  scene cg laptop # Using the laptop as a background for NVL chats

  show mara blush #as side image"

  Marginalia "NGL I do wanna see you! You're SUCH a blast to talk to online. I just know you'll be even MORE fun in person!"

  wallflower95 "that's a relief. i want to meet you too. it's crossed my mind, even before i realized you were close by."

  wallflower95 "but if you'd told me otherwise, i might have lied and denied it, haha."

  show mara shock #as side image"

  Marginalia "Really? That's kinda sad."

  wallflower95 "not as sad as being the only one interested in taking things further. "

  wallflower95 "isn't it scary to admit you want more from someone?"

  nvl clear
  nvl hide

  #END NVL MODE"

  stop music fadeout 1.0

  play music offline fadein 2.0

  scene cg laptop with slow_dissolve

  show mara blush #as side image"

  "Is wallflower95 saying what I think he's saying? "

  "If my heart was thumping loudly before, it's outright thrashing against my rib cage now."

  #hide cg laptop

  stop music fadeout 1.0

  play music online fadein 2.0

  #"START NVL MODE"
  scene cg laptop # Using the laptop as a background for NVL chats

  show mara poker #as side image"

  Marginalia "You're right. That IS scary."

  wallflower95 "but worth it, right?"

  show mara smile #as side image"

  Marginalia "TOTALLY worth it."

  jump lbl_part_23

label lbl_part_22:

  show mara shock #as side image"

  "Yes, I shouldn't scare him away! I can't be too eager, too available."

  #hide cg laptop

  stop music fadeout 1.0

  play music online fadein 2.0

  #"START NVL MODE"
  scene cg laptop # Using the laptop as a background for NVL chats

  show mara poker #as side image"

  Marginalia "I'm happy with the way we are right now."

  wallflower95 "yeah. same."

  Marginalia "If there's one thing I'm learning in this so-called unprecedented reality, it's that physical contact is overrated."

  show mara smile #as side image"

  Marginalia "Emotional intimacy, on the other hand? That's what's truly important."

  wallflower95 "couldn't have said it better myself."

  jump lbl_part_23

label lbl_part_23:

  show mara poker #as side image"

  Marginalia "Hey. Do you mind if I call you by your name, now that I know what it is?"

  wallflower95 "of course not. call me whatever you want. "

  show mara smile #as side image"

  wallflower95 "how about you? do you mind divulging your name?"

  Marginalia "Mara. That's my real name."

  wallflower95 "mara. a lovely name for a lovely person. i don't even need to see you to know that for sure."

  nvl clear
  nvl hide

  #END NVL MODE"

  stop music fadeout 1.0

  play music offline fadein 2.0

  scene cg laptop with slow_dissolve

  show mara blush #as side image"

  "My face is suddenly, alarmingly hot."

  "This guy! This Jian!"

  "The nerve of him, including the word {i}wallflower{/i} in his username when, in actuality, his flirting style is so smooth!"

  #hide cg laptop

  stop music fadeout 1.0

  play music online fadein 2.0

  #"START NVL MODE"
  scene cg laptop # Using the laptop as a background for NVL chats

  show mara smile #as side image"

  Marginalia "Jian."

  wallflower95 "yes?"

  Marginalia "Nothing. I just wanted to try saying it."

  wallflower95 "does it feel weird, using that name?"

  show mara shock #as side image"

  Marginalia "No way! It suits you! I can't explain it, but it just does!"

  wallflower95 "well then, mara. shall we go on that co-op mission you still owe me? what do you say?"

  show mara smile #as side image"

  Marginalia "I say let's DO IT! Let's freaking GO! Dream team of the century, coming through!"

  wallflower95 "dream team of the century, huh. i'm liking the sound of that."

  nvl clear
  nvl hide

  #END NVL MODE"

  scene cg laptop_game with slow_dissolve

  show mara smile #as side image"

  "We intend to go on a single co-op mission, then revel over the heaps of our spoils for the day. "

  "But one mission morphs into two, then three, then four. Loot piles up in our inventory, but we just keep going for more."

  "Our party differs depending on which of our BTBB buddies are online, but it's always either Jian or I who acts as party leader."

  "Whenever Jian leads, missions tend to abide by a strategically sound sequence of events."

  "Whenever I lead, however, it's every man for himself. Grab your own gold, and good luck getting outta there on your own. "

  "I do, however, stay behind every time to save the skins of neophyte party members."

  "So while higher-level players have more faith in Jian's technical prowess, lower-level players are loyal to my leadership."

  #hide cg laptop

  stop music fadeout 1.0

  play music offline_subdued fadein 2.0

  show bg bedroom_sunset with slow_dissolve

  show mara poker #as side image"

  "The sun is rising beyond my window when I finally consider getting some shut-eye."

  "Wow, I'm beat."

  #hide bg bedroom_sunset

  stop music fadeout 1.0

  play music online_subdued fadein 2.0

  #"START NVL MODE"
  scene cg laptop_game # Using the laptop as a background for NVL chats
  
  show mara poker #as side image

  Marginalia "BRUH I'm gonna crash. I can't anymore."

  wallflower95 "ugh, same. i was nodding off by the end of that last one, tbh."

  wallflower95 "there's one good thing we're getting from staying up this late, though. or this early."

  Marginalia "Which is what?"

  wallflower95 "the sunrise. such an exquisite color."

  Marginalia "Hmm, I would've taken you for a sunset aficionado, based on your PhaseNook photos."

  wallflower95 "i like both sunrises and sunsets. they're equally pretty, just in different ways."

  show mara smile #as side image"

  Marginalia "I'm officially claiming the sunrise camp, so you have no choice but to stan sunsets from now on BWAHAHA!!!"

  wallflower95 "haha, as you wish. i'll take what i can get. i've already told you that i appreciate them equally. "

  show mara shock #as side image"

  Marginalia "OH GOD I'm talking nonsense now! WELP it's a sign I should call it a night!"

  show mara smile #as side image"

  Marginalia "Nighty-night, Jian! Have OLIVIERI sweet dreams!"

  wallflower95 "good night, mara. sending olivieri sweet dreams back to you."

  nvl clear
  nvl hide

  #END NVL MODE"

  stop music fadeout 1.0

  play music offline_subdued fadein 2.0

  show bg bedroom_sunset with slow_dissolve

  show mara poker #as side image"

  "It's only after I've logged out and crawled beneath my blanket when the humiliation of my last words to Jian hits me."

  "That Olivieri pun has to be the worst one I've ever made in my life."

  show mara smile #as side image"

  "Jian must be nothing less than a saint to let a joke that unfunny slide so easily."

  #hide bg bedroom_sunset

  stop music fadeout 1.0

  play music offline fadein 2.0

  show bg urban_sunset with slow_dissolve

  show mara masked_poker #as side image"

  "A late Sunday afternoon. I've set out to remedy a crucial failing of my last trip to the grocery. "

  "My stock of ice cream is dangerously low. I may not survive the next week without enough sugary fortification."

  "Remembering what happened there last time, I've opted to avoid going to the grocery. "

  "Luckily, a nearby convenience store carries my favorite brand of ice cream."

  #hide bg urban_sunset

  show bg urban2_sunset with slow_dissolve

  "As I head back to the apartment, I notice that someone seems to be following me."

  show jian masked_poker at center with dissolve

  "This person isn't breaching any distancing protocols, but he isn't lagging too far behind me either."


  show mara masked_shock #as side image"

  "Oh, don't I recognize this guy? Isn't he a tenant of the Goldray Apartment too?"

  "Yes, we were both in the elevator last Friday, together with that insufferable woman spouting her bigotry."

  show mara masked_poker #as side image"

  "The guy isn't paying any attention to me, so I ignore him too. "

  "I stare off into the sky instead. Oh, that's a nice sunset. "

  "I wonder what Jian would think about that. I should send him a picture."

  "An abandoned construction site obstructs my view, so I decide to wait for a better vantage point before snapping any photos."

  hide jian

  #hide bg urban2_sunset

  show bg apartment_sunset with slow_dissolve

  "As my apartment building comes into view, so too does the sky. This will do nicely."

  show jian masked_poker at center with dissolve

  "Just as I'm about to extract my smartphone from my pocket, I notice that my co-tenant is busy with the exact same goal."

  show mara masked_shock #as side image"

  "This guy is holding up his phone against the sky in an attempt to secure a snapshot of the vivid sunset hues."

  "As I silently watch him, a strange feeling descends over me. An inkling of the inexplicable importance of this moment."

  show mara masked_poker #as side image"

  "Instead of taking a picture of my own, I activate my phone's mobile data feature to access MatteApp."

  "I take a surreptitious glance sideward. The guy has stopped snapping photos by now. "

  "He's looking down at his phone. Thumbs tapping rapidly over the screen, seemingly in the process of drafting a message."

  show mara masked_shock #as side image"

  "Just in time, my phone vibrates to notify me of a new message."

  hide jian

  #hide bg apartment_sunset

  stop music fadeout 1.0

  play music online_subdued fadein 2.0

  #"START NVL MODE"
  scene cg apartment_sunset2 # Using apartment_sunset2 as a background for NVL chats

  show mara masked_poker #as side image"

  wallflower95 "i don't know how to break this to you, but the sunset camp has clobbered the sunrisers today. "

  wallflower95 "you'd better switch allegiances while you can. don't worry. i'll keep your defection a secret."

  wallflower95 "do you require proof?"

  nvl clear
  nvl hide

  #END NVL MODE"

  stop music fadeout 1.0

  play music offline_subdued fadein 2.0

  show bg apartment_sunset with slow_dissolve

  show mara masked_shock #as side image"

  show jian masked_poker at center with dissolve

  "I glance at my co-tenant once more. He neither looks up nor appears aware of my presence beside him."

  "My phone commences vibrating again. "

  show mara masked_poker #as side image"

  "As expected, I'm receiving pictures of the vivid orange sky. The same sunset, the same location, the same angle. "

  "My mystical hunch transforms into something close to mathematical certainty."

  "It turns out, after all this time, that Jian and I were living not only in the same district, but also in the exact same building. "

  "How can this be? What's going on?"

  "Now that I've realized the truth, I should let him know. Shouldn't I? "

  "Yes, I should try saying his name!"

  stop music fadeout 1.0

  play music chaotic fadein 2.0

  show mara masked_blush #as side image"

  Mara "Jian."

  "He gives no sign that he's heard me. "

  show mara masked_poker #as side image"

  "Am I mistaken, after all? Should I just leave this stranger, whoever he is, alone?"

  "No, it can't be a mistake. It's too much of a coincidence."

  "I call his name again. A little louder this time."

  show mara masked_blush #as side image"

  Mara "Jian. {i}Jian.{/i}"

  "Still nothing. "

  show mara masked_poker #as side image"

  "I then notice that he's wearing wireless earbuds. That should explain why he can't hear me."

  "What should I do? I obviously can't tap his shoulder. Considering the public health crisis, people take offense to physical contact."

  "Should I wave to catch his attention? Or should I send a message to let him know I'm right beside him?"

  menu:
    "Wave at him.":
      jump lbl_part_35
    "Send him a message.":
      jump lbl_part_36

label lbl_part_24:

  stop music fadeout 1.0

  play music online fadein 2.0

  #"START NVL MODE"
  scene cg laptop # Using the laptop as a background for NVL chats

  ChainCustard404 "Hey how's it going??"

  Marginalia "Hey! How'd your errands go today?"

  ChainCustard404 "Fine tysm for asking!!"

  ChainCustard404 "Imma send u the link now :) this is the thing I was telling u about last night!!"

  nvl clear
  nvl hide

  #END NVL MODE"

  stop music fadeout 1.0

  play music online_subdued fadein 2.0

  scene cg laptop with slow_dissolve

  show mara poker #as side image"

  "I click on the link, which takes me to a PDF of some sort of psychological research paper."

  "{i}The Experimental Generation of Interpersonal Closeness: A Procedure and Some Preliminary Findings,{/i} the study is called."

  "It's authored by Arthur and Elaine Aron, plus three others."

  "I scroll through the document and see questions somewhere near the end. Thirty-six questions, divided into three sets of twelve."

  "I read through a few questions. Hmm. This can indeed be an interesting way to get closer to Gray."

  #hide cg laptop

  stop music fadeout 1.0

  play music online fadein 2.0

  #"START NVL MODE"
  scene cg laptop # Using the laptop as a background for NVL chats

  show mara smile #as side image"

  ChainCustard404 "See it?? Task slips for closeness-generating procedure??"

  Marginalia "Yep, I see it!"

  ChainCustard404 "Apparently the questions ramp up in intensity as u go along :O and u know what i've heard??"

  Marginalia "What?"

  ChainCustard404 "At least one pair who tried this experiment ended up as BF/GF afterward!!"

  show mara blush #as side image"

  Marginalia "Oh. Oh my."

  ChainCustard404 "So u wanna give it a shot?? :))"

  show mara smile #as side image"

  Marginalia "Why not? LMAO let's fall in love or something! Kidding!"

  ChainCustard404 "Nice!! Quick question do u live somewhere close to the grocery??"

  Marginalia "SUPER close, actually! Why do you ask?"

  ChainCustard404 "Instead of doing this cooped up alone let's take a walk :D wear ur mask and let's go!!"

  Marginalia "OK good idea! Where do we meet?"

  ChainCustard404 "South exit of the grocery :) i'll be there in 10 mins tops!!"

  nvl clear
  nvl hide

  #END NVL MODE"

  stop music fadeout 1.0

  play music offline fadein 2.0

  show bg urban_day with slow_dissolve

  show mara masked_poker #as side image"

  show grace masked_poker at center

  "Gray and I are now walking side-by-side over the streets of Ortigas. "

  "I almost can't wrap my mind around it. Only yesterday, Ma was giving me grief over my miserable single life."

  show mara masked_blush #as side image"

  "Today, however, I have a gorgeous guy by my side. And he, by his own admission, wants to get closer to me."

  "We may be standing two meters apart, as mandated by the public health guidelines imposed amidst the COVID-19 pandemic. "

  "But our hearts, at least, are open to proximity."

  "We've mutually decided not to strictly abide by the rules of the psychological experiment. "

  "We're not in a laboratory or a classroom, after all. The only science we want to learn is the science of each other."

  show mara masked_poker #as side image"

  Gray "Here's how we'll do it. You'll choose a question, any question, from the list. Tell me the number, and I'll answer. "

  Gray "Then we'll switch. I'll ask a question, and you'll answer."

  Mara "Sounds good. Who's going first?"

  Gray "You start. Pick a question for me."

  "I nod, then start scrolling through the questions on my phone, which I've saved via the notes app."

  "These questions supposedly increase in intensity, right? In that case, I should go easy on Gray, at least at first."

  "Hmm, which question should I choose?"

  menu:
    "Whom would you want as a dinner guest?":
      jump lbl_part_25
    "What would constitute a perfect day for you?":
      jump lbl_part_26

label lbl_part_25:

  Mara "Question number one."

  "Using his own phone, Gray reads the question aloud. He then answers without skipping a beat."

  Gray "Easy. I'd invite my mother to dinner."

  stop music fadeout 1.0

  play music offline_subdued fadein 2.0

  show mara masked_shock #as side image"

  Mara "Your mother? Why her?"

  Gray "Because she's dead."

  "There's a short beat of silence as my mind scrambles for something tactful to say in response."

  show mara masked_poker #as side image"

  Mara "Um, am I allowed to ask?"

  "But Gray only chuckles. He doesn't appear bothered by the follow-up question."

  Gray "No need to walk on eggshells. It's not like I cry myself to sleep thinking about her. I was a baby when she died."

  Gray "She died in childbirth. It's a tragedy I've had over two decades to process."

  Gray "But I don't miss her, because I didn't know her. I've heard stories about her from my father and uncles. That's about it."

  Gray "I guess that's why I'd ask her to dinner. To get to know her in her own words, you know?"

  Mara "Yes, I understand."

  stop music fadeout 1.0

  play music offline fadein 2.0

  jump lbl_part_27

label lbl_part_26:

  $ grace_romance += 1

  Mara "Question number four."

  "Using his own phone, Gray reads the question out loud. He then continues speaking, without even pausing to think."

  Gray "You already know what I'm about to answer, don't you?"

  show mara masked_shock #as side image"

  Mara "Eh? No? That's why I'm asking."

  Gray "What would be a perfect day for me? I don't even have to think so hard. Today's a good benchmark, I have to say."

  Mara "Today? Really?"

  Gray "Sure. I got all my errands and chores done, and now I'm taking a leisurely walk with a pretty lady by my side."

  show mara masked_blush #as side image"

  "Oh. Wow."

  "Good thing I'm wearing my trusty mask, or else the violent red of my blush would instantly give me away."

  show mara masked_poker #as side image"

  jump lbl_part_27

label lbl_part_27:

  Gray "Okay, my turn. You have to answer question number thirty-one."

  show mara masked_shock #as side image"

  "Thirty-one of thirty-six questions? "

  "I went out of my way to go easy on Gray, but he sure wants to dig as deeply as possible!"

  show mara masked_poker #as side image"

  "Scrolling to the chosen question, I clear my throat then read it out loud."

  Mara "Tell your partner something that you like about them already."

  show mara masked_blush #as side image"

  "Oh boy. Should I praise Gray's pretty face? His subtly melodic voice? His towering height?"

  "No, I should go deeper than all that."

  Mara "I like that you went for a question like that, right off the bat. I admire that part of you."

  Gray "And which part of me is that, exactly? Can you describe it a little more?"

  Mara "It's the part of you that goes straight for what you want, without holding back."

  show grace masked_blush at center

  Gray "Indeed. We have that in common, don't we?"

  "His gaze is something else. It's so unbearably intense that I have to look away first. "

  show mara masked_poker #as side image"

  show grace masked_poker at center

  "I've got an excuse to avert my eyes, at least. I have to pick my next question. "

  "Perhaps it's time to amp it up. This experiment is designed to generate closeness, after all."

  "I should pick something from the second set, from questions thirteen to twenty-four. But which one?"

  menu:
    "What is your most treasured memory?":
      jump lbl_part_28
    "What is your most terrible memory?":
      jump lbl_part_29

label lbl_part_28:

  $ grace_romance += 1

  Mara "Question number seventeen."

  Gray "My most treasured memory? Oh, that's a good one."

  "Gray takes a few minutes to think about this. By the time we've reached the park, the sun has started to set."

  hide grace

  #hide bg urban_day

  stop music fadeout 1.0

  play music offline_subdued fadein 2.0

  show bg park_sunset with slow_dissolve

  show grace masked_poker at center

  "Gray sits on a swing. I notice that he's cautious not to touch anything with his hands."

  Gray "To be honest, an answer came immediately to mind, but I kept trying to push it away and think of something else."

  Gray "I can't keep denying it though. I really only have one answer to that question."

  Gray "My most treasured memory is the day my ex-boyfriend first told me he loved me."

  show mara masked_shock #as side image"

  Gray "It didn't end well between us, needless to say. I haven't been with anyone else since we broke up."

  Gray "But that first day? Those first few months? They were great. "

  show mara masked_poker #as side image"

  Gray "My ex was the sweetest, or at least he used to be. He put the {i}honey{/i} in {i}honeymoon phase.{/i}"

  jump lbl_part_30

label lbl_part_29:

  Mara "Question number eighteen."

  Gray "My most terrible memory? That's an interesting one, for sure."

  "Gray actually mulls over his answer now. By the time we've arrived at the park, the sun has begun to set."

  hide grace

  #hide bg urban_day

  stop music fadeout 1.0

  play music offline_subdued fadein 2.0

  show bg park_sunset with slow_dissolve

  show grace masked_poker at center

  "Gray sinks down onto a swing. He's cautious not to touch anything with his hands, I note."

  Gray "I've had my fair share of terrible memories. But the worst one has to be the day it ended with my ex-boyfriend."

  show mara masked_shock #as side image"

  Gray "Like every other lovesick fool, I gave him everything. "

  Gray "I thought about him constantly when I was awake, dreamt about him every night."

  Gray "Of course, it all came crashing down when I caught him red-handed, cheating on me with another girl in our block."

  show mara masked_poker #as side image"

  Gray "It took me years, but I eventually came to see that moment for what it was. A blessing in disguise."

  Gray "When I think back to how deluded I was that time, with my rose-tinted glasses, it only makes me laugh now."

  jump lbl_part_30

label lbl_part_30:

  "I remain quiet, absorbing this information."

  "When I speak again, I'm careful to sound cheerful. Casual, even."

  Mara "You mean you're bisexual, then? Cool! I'm the same way!"

  Mara "I mean, I've only dated men in the past, but I've had countless crushes on women! I mean, who hasn't?"

  "Gray just looks at me. He doesn't say anything."

  "After a minute of excruciating silence, Gray gets up from the swing, and we resume walking."

  hide grace

  #hide bg park_sunset

  show bg street_sunset with slow_dissolve

  show grace masked_poker at center

  "Once we've come upon a practically deserted street, I finally summon the courage to speak up."

  Mara "Are you rejecting me because you're only attracted to men? Is that what you're trying to tell me with your silence?"

  "Gray stops dead in his tracks. "

  show grace masked_shock at center

  Gray "No! That's not what I'm trying to tell you at all!"

  show grace masked_poker at center

  Gray "We're exactly in the same boat. I've only been with men in the past, but I've fallen for women as well."

  Gray "I'm glad you're bi too, just like I am. Don't get me wrong."

  show grace masked_blush at center

  Gray "But there's something you should know. Something I should have brought up last night."

  Gray "I was curious to see how it would play out, I admit. So I didn't tell you, even though I should have."

  "Standing two meters away from me, he now lowers his mask."

  stop music fadeout 1.0

  play music chaotic fadein 2.0

  show mara masked_shock #as side image"

  show grace blush at center

  "I stare at Gray's fully exposed face for the first time."

  "The wheels have started spinning in my skull."

  show grace poker at center

  "Once recognition has blatantly dawned on me, Gray snugly repositions the mask. "

  show grace masked_poker at center

  "Gray then speaks, voice muffled once more."

  Gray "You misheard me when I told you my name. I said {i}Grace,{/i} not {i}Gray.{/i}"

  Grace "I realized right away that you mistook me as a man. But when would be the right time to correct your misconception?"

  Grace "I was uncertain about the timing. Before I knew it, I was playing along, pretending to be who you wanted me to be."

  Grace "I'm sorry. Regardless of my reasons, I lied. I shouldn't have done that."

  stop music fadeout 1.0

  play music offline_subdued fadein 2.0

  show mara masked_poker #as side image"

  "Not knowing what to say, I keep walking. I hear footsteps behind me as Gray shadows me."

  "No, not Gray. Grace. "

  "I repeat the correct name in my head, over and over, as I attempt to grow accustomed to it."

  hide grace

  #hide bg street_sunset

  show bg apartment_night with slow_dissolve

  show grace masked_poker at center

  "Night has fallen by the time my apartment building comes into view."

  "I turn back to Grace now. She looks at me expectantly."

  "What should I say? Should I tell Grace that this was all just a mistake? Or can we move past this, after all?"

  menu:
    "This was a mistake.":
      jump lbl_part_31
    "We can move past this.":
      jump lbl_part_32

label lbl_part_31:

  "I take a deep breath before launching into my next words."

  show grace masked_shock at center

  Mara "Look. You shouldn't have lied to me, but I shouldn't have assumed you were a guy either. We've both made mistakes."

  Mara "But this was all wrong from the start. Who even sets out to get to know a total stranger in the middle of a pandemic?"

  Mara "I'm sorry, Grace. I do appreciate what little time we spent together. Thank you for indulging my whims."

  show grace masked_poker at center

  "Grace nods, accepting my decision to end things prematurely."

  Grace "I enjoyed this time too, Mara. Sorry again. Get home safe, okay?"

  "Grace turns away, walking back the same path from which we've just come. "

  hide grace

  "As for me, it's time to go home."

  #hide bg apartment_night

  show bg bedroom_curtain with slow_dissolve

  show mara poker #as side image"

  "Back in my apartment again."

  "After a quick but thorough bath, I fling myself over the bed and grab my laptop."

  #hide bg bedroom_curtain

  scene cg laptop with slow_dissolve

  show mara shock #as side image"

  "Ah, wallflower95 is online! Just the guy I wanted to talk to!"

  "I chat him up right away on MatteApp."

  #hide cg laptop

  stop music fadeout 1.0

  play music online_subdued fadein 2.0

  #"START NVL MODE"
  scene cg laptop # Using the laptop as a background for NVL chats

  show mara poker #as side image"

  Marginalia "Guess WHAT?"

  Marginalia "When I tell you the past two days have been wild, BUDDY I mean it. 100\%."

  wallflower95 "oh dear. i can't wait to hear about your thrilling life. already strapping in for this roller coaster ride. "

  Marginalia "How have you been, incidentally?"

  wallflower95 "the past couple of days have also been peculiar for me. but you go first."

  Marginalia "OK OK remember when I told you yesterday that I wouldn't make the same mistake of assuming someone's gender?"

  wallflower95 "yeah, i remember."

  show mara sad #as side image"

  Marginalia "Well, guess who went and did it again, to DISASTROUS consequences. "

  wallflower95 "oh no."

  Marginalia "Go ahead and lock me up in gender jail. I'm pleading guilty. I fully accept my punishment."

  hide mara

  nvl clear
  nvl hide

  #END NVL MODE"

  scene cg ending1 with slow_dissolve
  $ persistent.ending_seen_1 = True
  pause
  jump lbl_credits
  
  return

label lbl_part_32:

  "I take a deep breath before saying what I want to say."

  show grace masked_shock at center

  Mara "Listen, Grace. We can move past this. We don't have to let our mistakes get in the way of this good thing between us."

  Mara "Maybe you were wrong for lying to me, but I was also wrong for misgendering you. "

  Mara "You've apologized, and I have to apologize too. I'm sorry for putting you in that weird position in the first place."

  show grace masked_poker at center

  "Grace shakes her head."

  Grace "It was obviously an honest mistake on your part. I'm sorry for not correcting you right away."

  Grace "Are we good now?"

  Mara "We're good."

  "There's a brief pause as we settle into the renewed peace between us."

  Mara "Hey. You know what I can't stop thinking about? The worst part?"

  Grace "What's the worst part?"

  show mara masked_shock #as side image"

  Mara "This is the second time in two days that I've gotten someone's gender wrong! "

  Mara "I'm telling you, it takes a special class of tactlessness to make the same type of mistake in close succession!"

  Mara "Lock me up in gender jail until I've truly learned my lesson! I beg of you!"

  show mara masked_poker #as side image"

  "Grace snickers at this."

  Grace "Now we can't have that. I'll take the witness stand for you. I'll bail you out."

  "Grace asks whether she can walk me to the entrance of my apartment building, and I say sure."

  hide grace

  #hide bg apartment_night

  show bg bedroom_curtain with slow_dissolve

  show mara poker #as side image"

  "Back in my apartment once more."

  "After a quick but thorough bath, the turbulence of today's events sends me instantly to bed. "

  #hide bg bedroom_curtain

  show bg bedroom_night with slow_dissolve

  "Hair still somewhat damp, I succumb to slumber."

  #hide bg bedroom_night

  stop music fadeout 1.0

  play music offline fadein 2.0

  show bg bedroom_day with slow_dissolve

  show mara smile #as side image"

  "When morning comes, I pulse with the infinite currents of possibilities."

  "Yesterday, these possibilities seemed to unfold before my eyes, to electrify my veins."

  show mara poker #as side image"

  "I pick up my laptop so that I can log into MatteApp."

  #hide bg bedroom_day

  scene cg laptop with slow_dissolve

  show mara blush #as side image"

  "There are new messages from Grace."

  "Heart in my mouth, I start to read them."

  #hide cg laptop

  stop music fadeout 1.0

  play music online fadein 2.0

  #"START NVL MODE"
  scene cg laptop # Using the laptop as a background for NVL chats

  show mara poker #as side image"

  ChainCustard404 "Good morning mara!! :D"

  ChainCustard404 "Are u up for continuing yesterday's experiment?? Wasn't it my turn next??"

  ChainCustard404 "Chose an easy one for u this time :) if we're gonna do this right maybe we should take it slow huh??"

  ChainCustard404 "Number 2!! Would you like to be famous, and if yes, in what way?"

  nvl clear
  nvl hide

  #END NVL MODE"

  stop music fadeout 1.0

  play music online_subdued fadein 2.0

  scene cg laptop with slow_dissolve

  show mara smile #as side image"

  "Smiling from ear to ear, I stretch my fingers and get ready to type."

  "Okay, maybe my fantasy of being a world-famous BTBB pro gamer is bonkers, but hey. A dream's a dream."

  "Even if it's unrealistic, it serves as a private source of comfort. Grace is a dreamer too, so I think she'll get it."

  show mara poker #as side image"

  "When I finish typing out my answer, it's several paragraphs long."

  "Grace responds a mere minute after I've sent my reply."

  #hide cg laptop

  stop music fadeout 1.0

  play music online fadein 2.0

  #"START NVL MODE"
  scene cg laptop # Using the laptop as a background for NVL chats

  show mara smile #as side image"

  ChainCustard404 "U should totally do it!! I'll back u up all the way :3"

  Marginalia "LMAO thanks, I guess?"

  ChainCustard404 "Pro gamers are more financially secure in recent years or so i've heard!! So don't give up <3"

  Marginalia "AWW you're the sweetest!"

  Marginalia "Oh lookie here. You'll just LOVE the question I've picked for you to answer."

  ChainCustard404 "Bring it on ;)"

  Marginalia "Number 7. Do you have a secret hunch about how you will die?"

  ChainCustard404 "Now that's exactly the cheerful kinda thing I wanna think about on a sunday morning :')"

  Marginalia "Heh, I warned you."

  nvl clear
  nvl hide

  #END NVL MODE"

  stop music fadeout 1.0

  play music online_subdued fadein 2.0

  scene cg laptop with slow_dissolve

  show mara poker #as side image"

  "Grace and I go back and forth this way for the rest of the day."

  "As it turns out, thirty-six questions are a lot to go through, even divided between us."

  "It takes time to grant each question its due consideration."

  show mara smile #as side image"

  "Fortunately for us, time is something we're mutually willing to share."

  if grace_romance < 3:
    jump lbl_part_33
  if grace_romance >= 3:
    jump lbl_part_34

label lbl_part_33:

  hide mara

  #hide cg laptop

  scene cg ending2 with slow_dissolve
  $ persistent.ending_seen_2 = True
  pause
  jump lbl_credits
  
  return

label lbl_part_34:

  hide mara

  #hide cg laptop

  stop music fadeout 1.0

  play music romantic fadein 2.0

  show bg darkness with slow_dissolve

  "And time indeed goes by. "

  "Days. Weeks. Months, even."

  "Once Grace and I finish our respective halves of the thirty-six questions, we switch. "

  "We each answer the questions we skipped before."

  "What was the most embarrassing moment of our lives?"

  "While I recount a day in Boracay when my string bikini snapped off and floated away, Grace recalls fainting onstage."

  "In a final dash into our burning homes, what item would we rescue?"

  "While I would retrieve my laptop, Grace would save her medications. She can't function without her happy pills, she says. "

  "When did we last cry in front of someone else?"

  "While I talk about Mikel's second birthday party, Grace tells me of the first and last time she ever entered a church."

  "Grace couldn't find a priest, so she spoke to the only person there. A stranger she'd never seen, before or since."

  #hide cg darkness

  stop music fadeout 1.0

  play music online fadein 2.0

  scene cg laptop_video with slow_dissolve

  show mara poker #as side image"

  "Over a MatteApp video call, her voice takes on a nostalgic tone."

  Grace "You look a lot like the stranger I met that day, come to think of it. She listened. She understood."

  Grace "Maybe that's why I decided to trust you, almost right away. I had a good feeling about you."

  show mara smile #as side image"

  Mara "But then you got to know me, and you soon realized what a mistake that was."

  "As always, her laughter is a spark of warmth. Like a sip of wine, fizzy to the head and fuzzy to the heart."

  Grace "Biggest mistake of my life. I should've stuck with the church lady. Can you recite your Bible verses like she can, huh?"

  show mara angry #as side image"

  Mara "What impossible standards! If you force your suitors to jump through these hoops, you'll die an old maid, I'm warning you!"

  Grace "You would know, wouldn't you? Seeing as you're nearly an old maid yourself, at almost thirty years old."

  Mara "You meanie! You're lucky you're cute! If you weren't, I'd have excommunicated you from my religion long ago!"

  show mara smile #as side image"

  Grace "If I tricked you into admitting that I'm cute, then every cruel word was worth it."

  "Grace giggles again, and I once more revel in the intoxicating quality of her laughter."

  show mara blush #as side image"

  "Fizzy. Fuzzy. All those flowering feelings."

  #hide cg laptop_video

  stop music fadeout 1.0

  play music romantic fadein 2.0

  show bg grocery_night with slow_dissolve

  show mara masked_poker #as side image"

  "As yet another Friday night rolls around, I'm still single. But I hope not to be for much longer."

  "I stride down the grocery aisle with a sense of purpose. "

  "Sure, I need to get my weekly provisions too. But before that, there's something I need to do."

  "Fist holding up a folded note, I march right up to the woman supervising the fruit stall."

  show grace masked_poker_apron at center

  "At the sight of me, her eyes light up instantly."

  Grace "What I can get you? Apples? Oranges? Some strawberries, perhaps?"

  "First, I disinfect my hands."

  "I then balance my message atop a rambutan, her favorite fruit."

  "Her gaze lingers a little too long on mine. "

  show mara masked_blush #as side image"

  show grace masked_blush_apron at center

  "She then picks up my note. Silently, she reads it. "

  "Her eyes meet mine again."

  hide mara

  hide grace

  scene cg ending3_pic with slow_dissolve

  Mara "So how about it? Can you give me what I want?"

  Grace "You want that one, huh? I can get that for you, but only after my shift ends."

  Mara "Perfect. I'm willing to wait. Is it on the house?"

  Grace "You bet."

  #hide cg ending3_pic

  scene cg ending3 with slow_dissolve
  $ persistent.ending_seen_3 = True
  pause
  jump lbl_credits
  
  return

label lbl_part_35:

  show mara masked_blush #as side image"

  "And so I begin to wave. Tentatively, at first. "

  "Then with more energy."

  "I'm practically flailing like a dying fish by the time he notices me."

  show mara masked_poker #as side image"

  show jian masked_shock at center

  "As he removes his wireless earbuds, he conspicuously takes one, two, then three steps away from me. "

  "Only then does he address my obvious attempts at communication."

  show jian masked_poker at center

  Jian "Did you need something?"

  "He may be wearing his mask, but something {i}strikes{/i} me instantly about the husky tone of his voice."

  show mara masked_blush #as side image"

  "This is the first time I'm hearing him speak, but I already want to keep hearing more. "

  "Does he sideline as a DJ or something?"

  show mara masked_poker #as side image"

  "As I muse about such things, he keeps staring at me suspiciously. "

  "There's no point putting this off. Here goes. Why in God's name am I so nervous?"

  show mara masked_blush #as side image"

  Mara "Um! You're Jian, right? The same Jian who's blowing up my phone with sunset photos right now? "

  show jian masked_shock at center

  Mara "I, um, I wanted to formally introduce myself! I'm Mara!"

  "His eyes are wide with alarm."

  jump lbl_part_37

label lbl_part_36:

  $ jian_romance += 1

  "It feels distinctly stalkerish to be doing this, even though that's obviously not the situation."

  "But what else can I do, if Jian is going to keep being so oblivious to the live human being right next to him?"

  "I begin typing on my smartphone."

  hide jian

  #hide cg apartment_sunset

  stop music fadeout 1.0

  play music online fadein 2.0

  #"START NVL MODE"
  scene cg apartment_sunset2 # Using apartment_sunset2 as a background for NVL chats

  Marginalia "I concede defeat. PLEASE do adopt me into the sunset camp."

  wallflower95 "you're conceding without any struggle whatsoever? was my proof persuasive enough to break your spirit?"

  Marginalia "Don't need proof. I happen to be looking at the sky too. I can see the sunset's beauty with my own eyes."

  wallflower95 "really? what a coincidence."

  Marginalia "LMAO a coincidence is one way to call it. Hey, you know what I love to do while sky-watching?"

  wallflower95 "what?"

  Marginalia "Eat ice cream. Ice cream goes with EVERYTHING but especially with croissant moons and blood orange suns."

  wallflower95 "what a way to describe that. i'm sold. i'm even hungry now."

  Marginalia "Care to join me, then? Ice cream party in five?"

  wallflower95 "sounds fun. i don't have ice cream right now, unfortunately. will a bowl of lucky charms suffice?"

  Marginalia "You don't need Lucky Charms. And you don't need ice cream either. I can share mine."

  wallflower95 "haha, are you actually going to deliver a tub of ice cream to me?"

  Marginalia "No, you can get it HERE. Just look to your right. But we've been standing here for ages so it's melty now."

  nvl clear
  nvl hide

  #END NVL MODE"

  stop music fadeout 1.0

  play music chaotic fadein 2.0

  show bg apartment_sunset with slow_dissolve

  show mara masked_blush #as side image"

  show jian masked_shock at center with dissolve

  "With a mixture of apprehension and amusement, I watch as he reads my latest message and freezes."

  "As stiffly as can be, he twists his neck to stare at me."

  show mara masked_poker #as side image"

  "By way of greeting, I lift the cloth bag with the half-melted cartons of ice cream."

  "Eyes still glued to mine, he finally removes his wireless earbuds. "

  Mara "I noticed that the sunset photos blowing up my phone were from this exact same location and angle."

  Mara "You're Jian, aren't you? Otherwise known as wallflower95? "

  Mara "I wanted to formally introduce myself. I'm Mara."

  Jian "Mara?"

  "In response to everything I've said, he only echoes my name. "

  "Just one word, but the deep and husky quality of his voice is undeniable. "

  show mara masked_blush #as side image"

  "It's the type of voice that can conceivably silence an entire room. Unexpected, given his understated appearance."

  "My own voice is sheepish as I speak again."

  Mara "Is that a yes to the party, then? If we stand here any longer, we'll have to split a carton of ice cream soup."

  jump lbl_part_37

label lbl_part_37:

  show mara masked_poker #as side image"

  "I hold my breath, waiting for him to say something. Anything."

  show jian masked_blush at center

  "But he doesn't say anything. He only looks more and more petrified with every passing second."

  "He then bolts away without warning, straight to the Goldray Apartment."

  hide jian

  show mara masked_shock #as side image"

  "Enshrouded in the cloud of dust he's kicked up in his escape, I can only gape in utter shock."

  #hide cg apartment_sunset

  stop music fadeout 1.0

  play music offline_subdued fadein 2.0

  show bg bedroom_curtain with slow_dissolve

  show mara poker #as side image"

  "Once I've arrived back in the apartment, I'm dreading checking MatteApp."

  "What is Jian even going to say? Will he berate me for infringing upon his sacred personal space?"

  show mara sad #as side image"

  "Does he hate me now? Has he always hated me? "

  "Why wasn't he happy to see me, when I was so excited to finally meet him? "

  "The thing is, neither of us planned to meet. It just happened. "

  "Serendipity. Just like all those cheesy KismetFlix rom-coms."

  "But what if he presumes I plotted for this fateful moment to happen? Hunted him down. Bought my own place in his building. "

  "Jian, a man so sweet and sincere that I assumed he was a woman for months. This Jian now sees me as a creep."

  "My most trusted confidante, and no less than {i}my favorite part of 2020,{/i} now hates me. "

  "This blows. This is the absolute worst."

  show mara poker #as side image"

  "After a bath, I go on KismetFlix to watch the most obnoxious movie I can find. "

  "Full of gunfire and explosions. A thunderous score."

  show mara sad #as side image"

  "I just want to turn my brain off. "

  "But at several points of the movie, I still find myself dabbing at the corners of my eyes. Upset over what happened."

  "After the movie is done and there's nothing left to distract me, I finally log into MatteApp. "

  #hide cg bedroom_curtain

  scene cg laptop with slow_dissolve

  show mara shock #as side image"

  "There are twenty unread messages from wallflower95 here! Why so many?"

  "How many ways can he phrase the message that we've crossed the line and can't go back to the way we used to be?"

  hide mara

  #hide cg laptop

  stop music fadeout 1.0

  play music romantic fadein 2.0

  #"START NVL MODE"
  scene cg laptop # Using the laptop as a background for NVL chats

  wallflower95 "mara, i'm so sorry."

  wallflower95 "i panicked, i messed up, i'm so sorry."

  wallflower95 "do you know the feeling when your chest seizes up and you're all at once out of breath and breathing too fast?"

  wallflower95 "i had such a distinct image of you in my head. you're funny and competitive and irreverent and your voice -"

  wallflower95 "your voice, or at least the way i imagined your voice to be based on your words, was so clear to me."

  wallflower95 "but then you appeared as if out of thin air, suddenly beside me, and nothing like i'd pictured you at all."

  wallflower95 "it's not a bad thing but it's a strange thing. i can't wrap my mind or heart around it -"

  wallflower95 "at least not yet, but i'd like to, if you'd only give me a chance to redeem myself and be a part of your life."

  wallflower95 "the way i acted was unacceptable, i know. i confess that with me such things happen more often than i'd like."

  wallflower95 "when i'm overwhelmed, which isn't rare, i run away. i remove myself from the situation to process it in private."

  wallflower95 "it's one of many things i'm working through in therapy. i can't tell you how sorry i am to show you that side of me -"

  wallflower95 "during our first encounter, when i've been yearning this whole time to meet you personally and know you deeply."

  wallflower95 "i do realize we've met before, brushing shoulders in the building, crashing carts in the grocery, prowling streets -"

  wallflower95 "and friday in the elevator. for obvious reasons, i don't count these as encounters. especially that horrid last one."

  wallflower95 "i want to start over. i want to start something real with a soul i already adore even while it intimidates me -"

  wallflower95 "to see a face more delicately formed than the crude collage my mind constructed using other faces."

  wallflower95 "please let me know if you're amenable to the possibility of a rekindled connection, despite my strange behavior."

  wallflower95 "of course, if you only want to laugh about the way i ran, or the way i stared at you as if you were a ghost -"

  wallflower95 "feel free to slip hate mail under my door. i will welcome anything if it's by your hand."

  wallflower95 "unit 1402."

  nvl clear
  nvl hide

  #END NVL MODE"

  #stop music fadeout 1.0

  #play music offline_subdued fadein 2.0

  scene cg laptop with slow_dissolve

  show mara blush #as side image"

  "After I'm done reading all these messages, I'm the one who's overwhelmed now. "

  "Okay, it's safe to say Jian doesn't hate me. Not even close. I completely misinterpreted his act of running away."

  #hide cg laptop

  show bg bedroom_curtain with slow_dissolve

  show mara poker #as side image"

  "Leaning against my giant Olivieri plushie, I attempt to formulate my response. I shovel spoonfuls of ice cream into my mouth."

  show mara angry #as side image"

  "It's no good!"

  "No words I possess, no matter how much I try to rearrange them, can match the intensity of Jian's MatteApp monologue!"

  show mara poker #as side image"

  "As I slump backward in defeat, Olivieri's fuzzy arm flops over my shoulder, as if to tell me everything will be okay."

  "Ah, Olivieri. For an inanimate object, this orange orangutan can certainly comfort me without fail. "

  "Just like this carton of rocky road ice cream."

  show mara shock #as side image"

  "Then an inspired idea comes to me. "

  "An honest-to-God flashbulb moment. "

  show mara smile #as side image"

  "A way to tell Jian without words that I care. That I understand and want the same things from him as he wants from me."

  "Yes, this is the right answer."

  #hide cg bedroom_curtain

  stop music fadeout 1.0

  play music offline fadein 2.0

  show bg hallway with slow_dissolve

  show mara poker #as side image"

  "Up on the apartment's fourteenth floor, I carefully position Olivieri in front of a certain door."

  "I rope Olivieri's long arms around the ice cream carton perched over its lap."

  "Propped up against the orangutan's chest is a sheet of paper with a message."

  "{i}My owner took me for a spin in the washing machine,{/i} the message says. {i}As such, I come bringing comfort and safe hugs.{/i}"

  "{i}My owner hopes to soon replace my role as courier,{/i} the message goes on. {i}Until then, please return me to unit 1105.{/i}"

  show mara smile #as side image"

  "I nod once I'm satisfied. "

  "I thoroughly disinfect my hands again with hand sanitizer. 60\% alcohol, as widely recommended."

  "I press the doorbell. Three times."

  "I then stride down the hallway, toward the elevators that can take me back."

  if jian_romance < 3:
    jump lbl_part_38
  if jian_romance >= 3:
    jump lbl_part_39

label lbl_part_38:

  hide mara

  #hide cg hallway

  scene cg ending4 with slow_dissolve
  $ persistent.ending_seen_4 = True
  pause
  jump lbl_credits
  
  return

label lbl_part_39:

  hide mara

  #hide cg hallway

  show bg darkness with slow_dissolve

  "It takes months of in-depth discussion."

  "Together, Jian and I explore topics ranging from stringent hygiene habits to vaccination plans."

  "We meticulously navigate every intricacy that can safeguard or jeopardize this connection between us."

  "Only then does he finally agree to step inside my apartment."

  #hide cg darkness

  stop music fadeout 1.0

  play music romantic fadein 2.0

  show bg bedroom_entrance with slow_dissolve

  show mara masked_poker #as side image"

  show jian masked_poker at center with dissolve

  "Sure, we're both still standing a cautious distance apart, but it's surreal to simply see him inside this closed space."

  Mara "Welcome to my humble abode! I'm so thrilled to have you here! Finally!"

  Jian "I'm happy to be here."

  "Even though Jian is still wearing a mask, I can tell by his eyes that he's smiling."

  show mara masked_blush #as side image"

  "So freaking cute!"

  "I have to repress every urge to embrace him as tightly as I can."

  show mara masked_poker #as side image"

  "Jian is holding Olivieri under his right arm. In this instance, he monopolized the plush for an entire month. The longest time yet."

  "One of these days, I might finally accept that Jian needs Olivieri more than I do and surrender my fuzzy friend for good."

  "But first things first. I open the lid of my washing machine and ask Jian to deposit Olivieri inside."

  "I also make Jian wash his hands with soap and water, then we move toward the bedroom."

  #hide cg bedroom_entrance

  show bg bedroom_curtain with slow_dissolve

  "We both sit on the bedroom floor, some two meters apart."

  "Jian's eyes are silently roving around the room. "

  "He's seen parts of my apartment during MatteApp video calls, but this is the first time he's seeing everything beyond the screen."

  show jian poker at center with dissolve

  "He tugs down his mask to take a sip from the same silver tumbler that he carries whenever we go on walks together."

  "He just now notices that I'm staring intently at him."

  Jian "Why are you looking at me like that?"

  Mara "No reason."

  Jian "Your sneaky expression betrays you. Tell me, Mara."

  show mara masked_blush #as side image"

  Mara "Fine. I'm just admiring how handsome my boyfriend is. "

  show jian blush at center

  Mara "Happy now?"

  show jian masked_blush at center

  "Within a split-second, the mask is covering the lower half of his face again."

  show mara masked_poker #as side image"

  Mara "Oh. You're trying to hide a blush, aren't you?"

  Jian "No! No, I'm not!"

  show mara masked_angry #as side image"

  Mara "So evil. You don't think that I, of all people in the world, deserve to see your adorable blushing face?"

  Jian "I told you! I'm not blushing!"

  Mara "Don't make me go over there and pull your mask off!"

  Jian "You wouldn't dare! "

  "From my laptop, a melodic triad of pings interrupts our playful verbal sparring."

  show mara masked_poker #as side image"

  show jian masked_poker at center

  Mara "What awful timing. Give me a sec."

  "I check my laptop to see what's up."

  hide jian

  #hide cg bedroom_curtain

  scene cg laptop_video with slow_dissolve

  show mara masked_shock #as side image"

  "Huh, an invitation from Ma to an ongoing video conference?"

  "Just then, I realize my massive mistake. Oh no."

  "I've overlooked something important in my excitement to have Jian over at my place for the first time."

  #hide cg laptop

  show bg bedroom_curtain with slow_dissolve

  show jian masked_poker at center

  Mara "Oh my God! It's Kuya's thirtieth birthday! I totally spaced! I forgot!"

  Mara "My family's celebrating via a MatteApp party!"

  show jian masked_shock at center

  "Alarmed by this announcement, Jian starts to stand up."

  Jian "I should go. I can come back another time."

  Mara "Wait! Please don't go! Stay!"

  show mara masked_poker #as side image"

  show jian masked_poker at center

  "Jian hesitates."

  Jian "Do you want me to hide, then?"

  Mara "No way! You're staying here beside me. In any case, you'll have to meet my parents sooner or later, right?"

  "At this point, I pause to think about what I'm saying. "

  "No, I can't force Jian into something like this, without warning. He has to {i}want{/i} to do this."

  Mara "Are you ready for this, Jian? It's your choice."

  "Jian seems to dwell on the question for a few seconds. He then nods."

  hide mara

  hide jian

  #hide cg bedroom_curtain

  scene cg ending5_pic with slow_dissolve

  Jian "Yes, I'm ready. I want to meet your family. "

  Jian "They're important to you, so they matter to me too."

  Mara "Thanks, Jian. I appreciate that."

  "And so, with my boyfriend by my side, I click on the button to accept the invitation."

  #hide cg ending5_pic

  scene cg ending5 with slow_dissolve
  $ persistent.ending_seen_5 = True
  pause
  jump lbl_credits
  
  return

## ------------------------------------------------------------------------------------------------
#init python:
#
#    ## This creates the End Credits portion.
#    
#    credits =   ('Writing', 'ilyilaice'),     ('Art', 'chymesoo'),     ('Programming and GUI', 'Marionette'),     ('Music', 'ejtanmusic'),     ('GUI Assets', 'Birctreel'),     ('Background Photo Filters', 'LunaPic.com')
#    
#    credits_s = "{size=80}Credits\n\n"
#    c1 = ''
#    for c in credits:
#        if not c1==c[0]:
#            credits_s += "\n{size=40}" + c[0] + "\n"
#        credits_s += "{size=60}" + c[1] + "\n"
#        c1=c[0]
#    credits_s += "\n\nMade with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]."
init:
    image cred = Text("[gui.about!t]\n\nMade with Ren'Py [renpy.version_only]", text_align=0.5, xmaximum=800)
    image theend = Text("{size=80}Fin", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)

label lbl_credits_from_menu:
    call lbl_credits from _call_lbl_credits
    return
    
label lbl_credits:
    
    # End Credits
    
    #Play menu music if in replay mode
    if (_in_replay):
        play music romantic fadein 1.0

    ## We hide the quickmenu for the End Credits so they don't appear at the bottom.
    $ quick_menu = False

    $ credits_speed = 20 # Scrolling speed in seconds
    scene bg black # Replace with a proper background if desired
    with dissolve
    show cred at Move((0.5, 1.9), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    
    #replay to show credits without the thanks for playing bit
    $ renpy.end_replay()
    
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks with dissolve


    if persistent.extras_unlocked:

        pass

    else:

        centered "You've unlocked the Extras Menu.\nAccess it through the Main Menu."
        # show extras_unlock with dissolve
        # with Pause(3)
        # hide extras_unlock with dissolve

        $ persistent.extras_unlocked = True
        
    ## We re-enable the quickscreen as the credits are over.

    $ quick_menu = True

    # This ends the game.

    return
