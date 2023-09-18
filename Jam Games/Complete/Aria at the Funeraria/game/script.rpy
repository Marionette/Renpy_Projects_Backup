label start:

  #reset variables
  $yael_romance = 0
  $freya_romance = 0
  $makeup_skill = 0
  $papa_trust = 0
  $clues_collected = 0
  $sheet_music = False
  $music_box = False
  $invisible_barrier = False
  $death_cause = False
  $photo_album = False
  $papa_violin = False
  $miniature_rose = False
  $lolo_cane = False
  $stopped_music = False
  $yael_abandoned = False
  $weapon_cane = False
  $weapon_hammer = False
  $path_one = False
  $path_three = False
  $ending_theme = "worst"
  
  # Start the game
  jump lbl_001
  
  return

label lbl_001:

  play music aria_guitar fadein 2.0

  show bg office with slow_dissolve

  show sari default #as side image"

  "An eerie melody wakes me from my nap in the back office of Roxas & Roxas Funeraria, the funeral home run by my father."

  show yael groovy at center with dissolve

  "My friend Yael is strumming the sinister song on his guitar."

  "I sit up on the small sofa and give a humongous yawn."

  show sari smile #as side image"

  Sari "That's a catchy tune, Yael. Is that your newest composition?"

  Yael "Nah. I can only dream of being this talented."

  stop music fadeout 1.0

  show yael smile at center

  "Yael's hand pauses over the strings."

  "As I move closer to him, he shows me a crumpled page of sheet music."

  Yael "I found this just lying around. Neat, eh?"

  show sari default #as side image"

  Sari "Just lying around? Where?"

  play music aria_guitar fadein 2.0

  show yael groovy at center

  "With a shrug, Yael starts strumming on his guitar once more."

  Yael "Just here in the office. Discarded on the floor."

  Sari "Then this music is probably haunted, isn't it?"

  stop music fadeout 1.0

  show yael shock at center

  "Yael freezes at once, his eyes as wide as saucers."

  Yael "Haunted? Why?"

  play music bgm fadein 2.0

  show sari smile #as side image"

  Sari "We have no idea how this sheet music got here, right? It wasn't here when we arrived from school."

  Sari "Did any client drop by while I was sleeping?"

  Yael "No. No one."
  
  Sari "Then where did this come from? It just appeared out of nowhere, without any explanation?"

  Sari "It certainly doesn't belong to Papa. He despises music with every fiber of his being."

  Sari "Papa complains about migraines if I even play a CD in my bedroom upstairs. I always have to use earphones."

  show sari laugh #as side image"

  Sari "What a delicious mystery! We should get to the bottom of this!"

  show sari default #as side image"

  "If Yael's eyes grow any wider than this, they'd more closely resemble dinner plates, not saucers."

  "With a sigh, I decide to nip my desire for adventure in the bud. Games are fun and all, but I don't want to drive Yael away."

  Sari "Or we can just pretend that none of this ever happened?"

  show yael default at center

  Yael "Good idea. Let's do that."

  "Yael sweeps the sheet music from the desk to the floor, where he originally found it."

  Yael "This is a regular Friday night. No spooky mysteries in sight."

  Yael "I'm just doing my part-time job, while you're chilling at home."

  Sari "Speaking of home, shouldn't you be leaving? It's past your working hours."

  Sari "You're a part-timer. You can afford to slack off."

  Sari "There'll be plenty of opportunities for overtime and sleepless nights after we graduate."

  show yael laugh at center

  "Yael flashes a wide smile."

  Yael "It's only seven! I can still hang out and keep you company!"

  show yael smile at left with dissolve

  show papa default at right with dissolve

  "Papa enters the office at this point."

  Papa "Rosario, Yael. I have a horrible migraine so I'm heading up to bed early."

  Papa "You can order pizza for dinner."

  show sari smile #as side image"

  Sari "Okay, Pa. Get some rest."

  show sari default #as side image"

  Sari "You haven't had one of those migraines in a long time, have you?"

  show papa anxious at right

  Papa "I heard music."

  show yael sad at left

  "Yael sheepishly raises a hand."

  Yael "Sorry, that was me."

  "Papa purses his lips, but he says nothing more on the matter. He turns toward me instead."

  show yael default at left

  show papa smile at right

  Papa "Rosario, I saw what you did with the cadaver for tomorrow. Good job with her makeup."

  show sari smile #as side image"

  Sari "You don't think it's too plain? I'm considering certain changes. You know, to ensure that her eyes really {i}pop.{/i}"

  Papa "As I've said many times before, no need for fancy makeup. We're preparing the poor girl for her funeral, not for a party."

  Papa "You should take some photographs. She would be a suitable addition to your mortuary cosmetology portfolio."

  Sari "Yeah, maybe I will. I might as well dress her up for tomorrow. Her family wants her in a wedding dress, right?"

  show papa default at right

  Papa "That wedding dress is an heirloom. The mother of the deceased prefers for us not to cut up the garment."

  Papa "It will be difficult to wrestle her into that outfit without my assistance."

  show sari default #as side image"

  "An idea occurs to Papa. He turns toward Yael now."

  Papa "Yael, if you're staying late, why don't you give Rosario a hand? Dressing a cadaver is interesting work."

  show yael shock at left

  Yael "Um."

  show yael anxious at left

  Papa "You never know. What if your lofty dream of becoming the biggest musical sensation in the Philippines falls through?"

  Papa "You may want to consider going into the mortuary business full-time, just like Rosario."

  Papa "You can still shift courses without issue as a sophomore, can't you?"

  Papa "Since there's only one block for Mortuary Science in your college, you and Rosario can even attend the same classes."

  show yael shock at left

  Yael "Mr. Roxas, I appreciate this learning opportunity! Really, I do!"

  Yael "I'll always be grateful that you hired me as your assistant, even though I'm unwilling to do certain tasks!"

  show yael anxious at left

  Yael "But I think I'll leave that stuff to Sari. She's way more competent than I am at your family business."

  Sari "Yeah, Pa. I can handle the corpse on my own. I don't need any help."

  "Papa holds up his hand to silence me. He continues addressing Yael."

  show papa anxious at right

  Papa "Yael, you've been a mortician's assistant for half a year now. How can you still be too squeamish to touch the cadavers?"

  Papa "You come in here one day with a new name. You tell Rosario and me that you're a man."

  Papa "Why aren't you acting like a man, then?"

  show papa default at right

  "Yael doesn't answer. He only fidgets."

  Papa "Don't you know that dead bodies can't hurt you? It's the living we should fear, not the dead."

  Papa "Look at Rosario here. Even though she's your age, cadavers don't scare her at all."

  show yael shock at left

  Yael "Mr. Roxas —"

  "But before Yael can get in another word, Papa interrupts him."

  show papa anxious at right

  Papa "I'm still speaking. You shouldn't interrupt your elders when they're trying to get you to see things from their perspective."

  show yael anxious at left

  "Yael bites his bottom lip and says nothing else."

  show sari mad #as side image"

  "Papa is being unfair! He shouldn't be so strict with Yael!"

  "Should I stand up for Yael? Or should I just let Papa finish saying his piece so that he'll leave us sooner?"

  menu:
    "Speak up on Yael's behalf.":
      jump lbl_002
    "Don't butt in.":
      jump lbl_003

label lbl_002:

  $ papa_trust += 1
  $ yael_romance += 1

  "Yes, I should stand up for my friend!"

  show yael shock at left

  show papa default at right

  Sari "Pa, you shouldn't be too hard on Yael! He's tougher than you think!"

  show sari default #as side image"

  Sari "For you and me, maybe, corpses are our livelihood. But for almost everyone else, corpses are the stuff of nightmares."

  show yael default at left

  Papa "But nightmares can't harm anyone either. You would know that best, wouldn't you, Rosario?"

  Papa "Remember your pet cat? You named her Rosanna after your Mama."

  jump lbl_004

label lbl_003:

  show sari default #as side image"

  "Yes, the sooner Papa gets to his point, the sooner Yael and I will be free from this tiresome lecture."

  Papa "I'll take a wild guess about what's truly bothering you."

  Papa "Do dead bodies appear in your nightmares? Do they deter you from sleeping at night with the lamp off?"

  Papa "Listen to me. No matter how frightening your nightmares can get, they can't really harm you."

  show papa default at right

  show yael default at left

  Papa "If you still harbor any doubts, take a look at Rosario here. She understands this best."

  show sari shock #as side image"

  "Suddenly dragged into Papa's sermon, I momentarily forget my resolution to refrain from interfering."

  Sari "Me? Why me?"

  show sari default #as side image"

  Papa "Rosario, do you remember your pet cat? The one you named Rosanna after your Mama?"

  jump lbl_004

label lbl_004:

  Papa "For a long time after losing that cat, you suffered from night terrors and bed-wetting episodes."

  show sari mad #as side image"

  "Argh! Why is Papa talking about this shameful stuff right in front of Yael?"

  menu:
    "Protest.":
      jump lbl_005
    "Stew in silence.":
      jump lbl_006

label lbl_005:

  $ papa_trust += 1

  "I've had enough of Papa's tirade!"

  Sari "Pa! Do we really have to take a trip down memory lane {i}now?{/i}"

  show papa anxious at right

  "Papa's voice is defensive."

  Papa "I'm just trying to make a point here, Rosario."

  Papa "Despite those nightmares from your childhood, you've managed to grow up into a brave young woman —"

  Sari "That's it, Pa. Time for bed. Time to rest your aching head. {i}Good night.{/i}"

  jump lbl_007

label lbl_006:

  "So I say nothing. I am, however, scowling."

  "I'm letting Papa know without speaking that I disapprove of the things he's saying."

  show papa anxious at right

  Papa "Don't look at me like that, Rosario. I'm just trying to make a point here."

  Papa "Despite those nightmares from your childhood, you've managed to grow up into a brave young woman and a dutiful daughter."

  "When only silence follows, Papa clutches his throbbing temples. He winces."

  Papa "Well, I should be getting to bed. Otherwise, this migraine will send me crashing to the floor."

  jump lbl_007

label lbl_007:

  "Papa finally bids us both good night, then leaves the back office to go upstairs."

  hide papa

  "Good riddance."

  show yael default at center with dissolve

  show sari default #as side image"

  "Alone with Yael again, I heave a heavy sigh."

  Sari "Just ignore the stuff Papa says when he's in a mood. That's what I do." 

  Sari "He never knows when to stop. He's always embarrassing me like this."

  show yael smile at center

  "Yael shakes his head."

  Yael "If it makes you feel any better, I don't think the things he said about you are embarrassing at all."

  Yael "Your father's right about one thing. You're the bravest person I know."

  menu:
    "Accept the compliment.":
      jump lbl_008
    "Return the compliment.":
      jump lbl_009

label lbl_008:

  show sari smile #as side image"

  Sari "Well, if you say so."

  jump lbl_010

label lbl_009:

  $ yael_romance += 1

  show sari smile #as side image"

  Sari "You're brave too, you know? Brave in a different way."

  show yael blush at center

  Yael "Eh? Brave?"

  Yael "That might be the {i}last{/i} word I'd ever use to describe myself."

  show yael default at center

  Sari "I mean it."

  show sari default #as side image"

  Sari "Wasn't Tito Eduardo expecting you to take a pre-med course so that you can become a doctor just like he is?"

  Sari "Yet you stood firm. You looked your father right in the eye, and you said it."

  show sari mad #as side image"

  Sari "You said, listen here, old man! I'm studying music in college, and there's nothing you can do about it!"

  Sari "You said, I'm starting my own band! And we're leading the Filipino youth revolution, within the OPM scene and beyond!"

  show sari smile #as side image"

  show yael laugh at center

  "Yael chuckles."

  Yael "Yeah, that's not exactly how it happened."

  show yael default at center

  Yael "There were lots of slammed doors during that time. Severed phone lines."

  show yael smile at center

  Yael "But I do appreciate your dramatic reenactment, artistic liberties and all."

  Yael "Thank you for calling me brave, even though I'm not sure I deserve it."

  jump lbl_010

label lbl_010:

  Sari "Speaking of bravery, why don't we do a test of bravery right now?"

  show yael shock at center

  Yael "Uh. This isn't about solving the mystery of the haunted sheet music again, is it?"

  show sari laugh #as side image"

  Sari "Nope!"

  show sari smile #as side image"

  show yael default at center

  "I snatch my laptop from my schoolbag, then reposition my chair next to Yael's."

  Sari "Have you heard of {i}Corpses Come Calling,{/i} the new scary movie that people at school have been raving about?"

  Sari "Let's watch it together! Watching horror movies is the best way to get over your fear of real-life horrors!"

  show yael shock at center

  Yael "Um. Are you sure about that?"

  Yael "Won't that just worsen —"

  show sari default #as side image"

  show yael anxious at center

  "Shushing Yael, I punch the space bar of my laptop to begin the movie."

  "Yael remains quiet beside me, at least until the first jump scare happens."

  show yael shock at center

  "The film's female protagonist shrieks as a door slams. In the same beat, Yael yells and grabs my arm."

  Yael "Oh my God, oh my God, oh my God! Sari, make it go away!"

  show sari laugh #as side image"

  show yael anxious at center

  Sari "Yael, it's just a movie."

  Sari "It can't hurt you because it's not —"

  stop music fadeout 1.0

  show sari shock #as side image"

  show yael shock at center

  "BANG!"

  "With a deafening crash, the office door has slammed shut behind me and Yael."

  "I leap to my feet and spin around."

  play music suspense fadein 2.0

  show sari anxious #as side image"

  Sari "Huh. That's weird."

  "I tug away from Yael's grasp on my arm. In his terror, his fingernails have left imprints over my skin."

  show yael anxious at center

  "I press the space bar on the laptop to pause the movie, then get up to examine the door."

  "I swing the door open and closed. Once, twice. Several times."

  show sari default #as side image"

  "The door is working just fine."

  Sari "It must have been a gust of wind. It's June, after all. Rainy season."

  "Yael parts his mouth to respond, but another noise drowns out his voice."

  show sari shock #as side image"

  show yael shock at center

  "THUMP! THUMP! THUMP!"

  "Beyond the back office, there's the thunderous sound of knocking, coming from the front door."

  show sari anxious #as side image"

  Sari "A visitor? Who can it be?"

  show yael anxious at center

  Yael "Is that the pizza boy? Maybe?"

  Sari "But we haven't ordered dinner yet."

  show sari default #as side image"

  "I'm just about to march out of the office to check, when Yael dashes forward to block my progress."

  show yael shock at center

  Yael "This is a bad idea! The worst!"

  Yael "If we were in a horror movie right now, answering the door would be a surefire way to die!"

  show yael anxious at center

  Sari "But this isn't a movie. This is real life."

  Yael "Let's stay here! If we ignore whatever's waiting by the door, it will grow bored and go away!"

  show sari anxious #as side image"

  Sari "What are you even talking about? Papa's asleep now, so it's my responsibility to deal with prospective clients."

  Sari "I may not be a licensed funeral director like Papa, but at the very least, I can hand over a pamphlet and a calling card."

  show sari default #as side image"

  hide yael

  "With this, I stride around Yael's body and head for the foyer."

  show bg foyer with slow_dissolve

  "I know that, despite his protests, Yael is hot on my heels."

  "I can hear him hyperventilating behind me when I reach the entranceway."

  "As I'm fiddling with the locks, Yael speaks again. His voice is barely audible amidst the chorus of knocking on wood."

  show yael anxious at center with dissolve

  Yael "Are you sure about this? Absolutely sure?"

  Sari "Of course I'm sure."

  show yael blush at center

  Yael "Then, before we're both murdered in cold blood, I should tell you —"

  show sari laugh #as side image"

  "I have to laugh at this."

  Sari "Don't be so melodramatic, Yael! Nobody's dying tonight!"

  show sari default #as side image"

  "Shushing Yael's stammering reply, I yank open the front door."

  show bg foyer_open with slow_dissolve

  show sari shock #as side image"

  show yael shock at center

  "There's no one there."

  "No one except Yael and I, standing stock-still in utter silence."

  show sari default #as side image"

  "Yael's voice is shakier than ever. For once, I can't fault him for it."

  Yael "That's it. I don't care how dark it is outside. I'm done. I'm heading home."

  show sari shock #as side image"

  show yael anxious at center

  Sari "What? Now?" 

  Sari "But think of the adventure that you're gonna miss!"

  show sari smile #as side image"

  Sari "We may have a real haunting in our hands! This is way more exciting than any old horror movie!"

  "Simply hearing the word {i}haunting{/i} causes Yael to squirm."

  show sari default #as side image"

  show yael sad at center

  Yael "I wish I didn't have to leave you behind, but. . . ."

  stop music fadeout 1.0

  "Yael's voice trails off. He's fidgeting again, waiting for me to say something."

  "Should I convince Yael to stay, or allow him to leave uncontested?"

  menu:
    "Persuade Yael to stay in the funeral home.":
      jump lbl_011
    "Let Yael leave.":
      jump lbl_012

label lbl_011:

  play music mellow fadein 2.0

  "Yeah, I should convince Yael to stay. I don't want him to miss out on this adventure of a lifetime!"

  Sari "Come on, Yael. Don't go."

  show yael default at center

  Sari "Sure, I can probably deal with a haunting on my own. As you know, nothing scares me."

  show sari smile #as side image"

  Sari "But won't everything be twice as fun if we're doing it together?"

  show yael blush at center

  "Yael stares into my eyes, then nods stiffly."

  Yael "You're right. Of course you're right. As long as we're together, we'll be fine."

  show yael smile at center

  Yael "Thank you, Sari."

  show sari default #as side image"

  Sari "Why are you thanking me? I should be the one thanking you for staying."

  Yael "Thanks for not letting me run away, like I always do. I can't chicken out now. Not when it really counts."

  stop music fadeout 1.0

  show sari smile #as side image"

  "Flashing a grin at him, I turn around to shut the front door and secure its three locks."

  show bg foyer with slow_dissolve

  "I face Yael again."

  play music aria fadein 2.0

  show sari shock #as side image"

  show yael shock at center

  "Just then, a familiar melody commences playing."

  show sari anxious #as side image"

  "I lean against the closed door as I listen. I strain my ears, but I can't tell where the song's coming from."

  Sari "That melody, it was the same one you played on your guitar earlier, right?"

  show sari default #as side image"

  "But Yael might as well be petrified in terror in front of me."

  "Perhaps predictably, unexplained sounds in the funeral home aren't Yael's jam."

  Sari "I gotta go check. You can wait here if you're too scared."

  show yael anxious at center

  "But Yael grabs the cloth of my shirt and clings to me, even as I start to move. I guess he wants to tag along, then."

  show sari anxious #as side image"

  "Which area of the funeral home should we begin our investigation?"

  "Should we return to the back office, where Yael found the sheet music?"

  "Or how about the viewing room? It has to be a hotbed for paranormal activity, given that coffins are laid there for funerals."

  "Of course, there's always the morgue. The corpse for tomorrow's wake is lying there now, right inside the refrigeration unit."

  show sari default #as side image"

  "Where should Yael and I go?"

  menu:
    "The back office.":
      jump lbl_071
    "The viewing room.":
      jump lbl_072
    "The morgue.":
      jump lbl_076

label lbl_012:

  play music bgm fadein 2.0

  "If Yael truly wants to leave, then I don't have any right to stop him, do I?"

  "In the first place, I made him watch that horror movie with me. He didn't want to, but I forced him."

  "Now that we may be dealing with real horrors, can I blame him if he wants to bail?"

  Sari "If you wanna go, then go. Stay safe on your way home, all right?"

  show yael anxious at center

  Yael "Of course. Please stay safe too." 

  Yael "I'll never forgive myself if something happened to you, and I wasn't here to help."

  show yael default at center

  "Yael steps over the threshold, then hesitates at the last moment."

  Yael "Call me if you need anything. No matter what it is, contact me and I'll come back right away. I promise."

  show sari smile #as side image"

  Sari "I'll keep that in mind."

  Yael "Good night, Sari."

  Sari "Good night, Yael."

  stop music fadeout 1.0

  hide yael

  show sari default #as side image"

  "Once Yael walks off, I secure the front door."

  show bg foyer with slow_dissolve

  "Three locks. {i}Click, click, click.{/i}"

  play music aria fadein 2.0

  show sari shock #as side image"

  "Just as the last {i}click{/i} echoes around the foyer, a familiar melody commences playing somewhere behind me."

  "That song. Wasn't that the same melody that Yael was playing on his guitar?"

  show sari anxious #as side image"

  "I lean against the front door as I listen. Although I'm straining my ears, I can't tell where exactly the melody's coming from."

  "Which part of the funeral home should I check? Should I return to the back office, where the sheet music was found?"

  "Or how about the viewing room? As the area where coffins are laid for funerals, it must be a hotbed for paranormal activity."

  "Of course, I can't discount the morgue. The corpse for tomorrow's wake is lying there now, right inside the refrigeration unit."

  show sari default #as side image"

  "Which area of the funeral home should I investigate?"

  menu:
    "The back office.":
      jump lbl_013
    "The viewing room.":
      jump lbl_014
    "The morgue.":
      jump lbl_015

label lbl_013:

  $sheet_music = True
  $ clues_collected += 1

  show bg office with slow_dissolve

  "I return to the back office."

  "There's nothing here. The eerie melody continues playing elsewhere."

  "I crouch down to retrieve the sheet music that Yael left on the floor earlier."

  "I have no idea whether this item will aid my investigation. But it can't hurt, right?"

  "Now, where should I go next?"

  menu:
    "The viewing room.":
      jump lbl_014
    "The morgue.":
      jump lbl_015

label lbl_014:

  show bg viewing_open with slow_dissolve

  "In the viewing room, the sinister melody is significantly louder."

  "The sound is coming from the coffin for tomorrow's wake."

  "Glancing around the empty room and all its empty chairs, I approach the coffin."

  "Laying atop the coffin's velvet interior is a music box. Ah, so this is what's been playing that melody."

  "What is this music box doing here? Should I take a closer look?"

  menu:
    "Reach for the music box.":
      jump lbl_016
    "Don't touch it.":
      jump lbl_017

label lbl_015:

  show bg morgue_open with slow_dissolve

  "In the morgue, the sinister melody sounds more distant than ever."

  "Wrong room, then. I should check elsewhere."

  stop music fadeout 1.0

  show bg foyer with slow_dissolve

  show sari shock #as side image"

  "Right after leaving the morgue, the music that's been playing stops."

  "I halt in my tracks."

  show sari default #as side image"

  "I savor the sudden silence. Musing."

  play music suspense fadein 2.0

  "Just then, I realize something strange. Something off-kilter about the morgue I've left."

  show sari anxious #as side image"

  "The door to the refrigeration unit, where Papa stores corpses before they're laid in their coffins, was open."

  "The cold air will be pouring out. Our electric bills will rack up in no time."

  "Who left the door to the refrigeration unit open anyway? What a rookie mistake."

  show sari default #as side image"

  "I should go back and close the door."

  show bg morgue with slow_dissolve

  "I'm back in the morgue again."

  show sari shock #as side image"

  "Huh? The door to the refrigeration unit is closed?"

  "That door was open just now. I saw it. I'm {i}sure{/i} of it."

  show sari default #as side image"

  "Throwing inquisitive glances around the room, I approach the refrigeration unit with cautious steps."

  "I yank open the door. A cloud of chilly air disperses at once."

  show bg morgue_open with slow_dissolve

  show sari anxious #as side image"

  "Eh, why's the unit empty? Where's the corpse?" 

  "Just this afternoon, as soon as I got home from school, I applied makeup on her. Plain, the way Papa likes it."

  "I'm standing there, puzzling over the cadaver's absence, when —"

  show sari shock #as side image"

  Unknown "BOO!"

  "Someone has screamed right behind me, right into my ear."

  "With my heart pounding, I whirl around."

  show freya default at center with dissolve

  "It's the missing corpse!"

  "She's already wearing the wedding gown. The one Papa told me to put on her."

  stop music fadeout 1.0

  "I stare. The sight has scrambled all my speech-related skills."

  show freya smile at center

  "Even though I gape, at an utter loss regarding my next move, the corpse bride smiles brightly at me."

  play music bgm fadein 2.0

  show sari anxious #as side image"

  Unknown "Well, hello there! How nice of you to visit my humble abode!"

  Unknown "If you hadn't come to play, I might have crawled back inside the wall. Wallowed alone in my disappointment."

  Unknown "Hey, where's your scaredy-cat friend? Yael, right? You should've taken him along with you! He was super cute!"

  show freya default at center

  Unknown "No, never mind that now."

  jump lbl_105

label lbl_016:

  $music_box = True
  $ clues_collected += 1

  "I pick up the music box from the coffin and examine the dusty contraption."

  "Where a ballerina usually spins, an intricately carved miniature rose is turning slowly."

  show sari shock #as side image"

  "Just then, a voice floats toward me."

  "The voice comes from a source inside this room. Mere meters away. And yet it sounds strangely distant. Like an echo."

  Unknown "You should not touch things that do not belong to you."

  show ghost default at center with dissolve

  "Frozen with shock, I stare at the ghostly presence suddenly by my side. It stares back."

  show sari default #as side image"

  "A minute or so passes, then my body unfreezes."

  stop music fadeout 1.0

  "I close the music box."

  "I return the contraption to the coffin's velvet interior."

  play music bgm fadein 2.0

  Sari "Sorry. It's not every day that I get to see spirit-owned music boxes. The novelty alone stoked my curiosity."

  jump lbl_018

label lbl_017:

  "Without laying a hand on the music box, I lean in to examine it."

  "The contraption seems ancient. Just breathing in its vicinity causes the lid of the music box to waver."

  stop music fadeout 1.0

  "The lid of the music box snaps shut, snuffing out the melody it plays."

  "The closing motion of the lid raises a cloud of dust. Of course, I sneeze spectacularly."

  play music suspense fadein 2.0

  show sari shock #as side image"

  "Just then, a voice reaches my ears."

  "The voice comes from a source inside the viewing room. Mere meters away. But it sounds strangely distant, like an echo."

  Unknown "You should not defile things that do not belong to you."

  show ghost default at center with dissolve

  "I stare at the ghostly presence suddenly beside me. It stares back."

  stop music fadeout 1.0

  show sari default #as side image"

  "A minute or so passes before my body unfreezes."

  "I straighten up from my position of bending over the coffin."

  play music bgm fadein 2.0

  Sari "Sorry. I can't smother a sneeze when I get a faceful of dust like this. It's an unstoppable physiological reaction."

  jump lbl_018

label lbl_018:

  show ghost shock at center

  Unknown "You wait a moment. You can hear my voice?"

  Sari "Hear you, see you. The whole shebang. I've never seen anything like you before."

  show sari laugh #as side image"

  show ghost default at center

  Sari "Does this mean I've got ESP? Awesome!"

  Sari "I've always wanted to see ghosts!"

  show sari smile #as side image"

  "As I continue to gush, the ghost reaches toward the music box in the coffin and presses it against his chest."

  "Just like that, the contraption is swallowed into the gelatinous substance of his body."

  show sari shock #as side image"

  "My jaw drops."

  Sari "Wow! That's so cool! Is that how ghosts keep their earthly possessions close to them?"

  show sari default #as side image"

  Unknown "This music box is not an earthly possession, as you call it. This music box is my heart."

  Sari "Your {i}heart?{/i} How does that even work? Do all other ghosts have music boxes for hearts?"

  Unknown "I cannot truthfully address your query, for I perceive no ghosts. The only spectral existence I know is my own."

  Sari "You don't have any friends who are ghosts? You've been alone all this time?"

  "The ghost nods."

  Sari "That must have been lonely."

  show sari smile #as side image"

  Sari "Don't worry! I'll be your friend!"

  show ghost smile at center

  "With a small smile, the ghost bows his head to assent once more."

  Sari "Then, as your friend, can I be totally candid with you?"

  show sari default #as side image"

  show ghost default at center

  "I clear my throat for effect, while closing the coffin at the same time."

  show bg viewing with slow_dissolve

  Sari "I personally don't have any issues with ghosts like you, but you'd better not try those tricks on Papa or anyone else."

  Sari "Papa and I are running a small-town business here. We have one major competitor — Tiya Nena's funeral parlor two blocks over."

  Sari "If even one client hears the melody of your music box, our customer base will dwindle then disappear."

  show sari anxious #as side image"

  Sari "You don't wanna haunt a boarded-up funeral home without espers like me to converse with, do you?"

  Sari "So you'd better get in line and confine your haunting habits to when we're alone! You already scared off my buddy Yael!"

  show sari default #as side image"

  Unknown "I assure you that I will not cause you any trouble. This was not my intention when I permitted the music to play."

  Sari "So what were you trying to do?"

  Unknown "Your companion earlier strummed a strikingly familiar melody on his instrument."

  Unknown "I opened my heart then, as I had not done in a long time, to verify whether his melody and mine truly bore a resemblance."

  Sari "Yeah, I noticed that similarity too. What a mysterious coincidence, huh?"

  show sari smile #as side image"

  Sari "Here's an idea. Why don't we investigate this mystery together, you and I?"

  show ghost smile at center

  Unknown "I believe that investigating together is a splendid idea."

  show ghost default at center

  show sari default #as side image"

  Unknown "I have only ever drifted around this funeral home without touching a thing."

  Unknown "I phase through matter in the same way that fingers fail to grasp water."

  Unknown "My inability to hold tangible objects not already in my possession prevents me from making much headway on my own."

  show sari smile #as side image"

  Sari "It's settled, then. You and I are now paranormal detective partners!"

  Sari "If we're gonna be teammates, we should introduce ourselves. My name's —"

  show sari default #as side image"

  Unknown "Your name is Rosario Roxas, daughter of Rogelio and Rosanna Roxas."

  Unknown "I have resided exclusively in this funeral home for as long as memory serves me. I know nearly everything about you."

  Sari "Everything about me, huh? If I were another type of person, I might've found your omnipotence flattering."

  Unknown "I did not claim to know absolutely everything. I cannot read your mind."

  show sari smile #as side image"

  Sari "Good to hear!"

  Sari "Won't you tell me your name and your story, then? It's only fair!"

  show sari default #as side image"

  "When the ghost doesn't respond, I go ahead and prompt him."

  Sari "Let me guess. You've got an old-fashioned name from centuries ago."

  Sari "Hey, no matter what your name is, I won't laugh. I promise."

  Unknown "Your impending mirth is not the reason for my hesitation."

  Unknown "I know not my name, nor the way I lived or died, nor the occurrences that in between transpired."

  Unknown "I know not how I arrived here, nor why I am unable to step beyond the premises of this building."

  show sari anxious #as side image"

  Sari "So you've been stuck here in the funeral home, which has belonged to Papa's family for generations. But you don't know why."

  "I rub my chin as I contemplate."

  show sari shock #as side image"

  Sari "This probably means you have unfinished business in the funeral home!"

  Sari "That's how ghosts work in horror movies!"

  show sari default #as side image"

  Unknown "My interrupted affairs in this place, if those are indeed what tethers me to this plane, are a mystery to even myself."

  show sari smile #as side image"

  Sari "Then that's another mystery we should solve together!"

  Sari "How about this? Since you said you can't touch anything, I'll hold up random objects to you."

  Sari "We'll see whether any object sparks your memory."

  Unknown "I agree with this proposed methodology."

  show sari default #as side image"

  Sari "Before we get started, I should give you a name. Just a temporary one until we can figure out what you're called."

  $ ghostname = renpy.input("What name should I give to the ghost? Type a name now!")
  $ ghostname = ghostname.strip()

  if not ghostname:
       $ghostname = "Ghost"
  
  show sari smile #as side image"

  Sari "Yeah, let's call you [ghostname]! How do you like that?"

  Ghost "The name you have bestowed has an intriguing ring to it. I thank you, Rosario."

  Sari "Don't call me Rosario! The name's too stuffy! Just call me Sari!"

  Sari "With that out of the way, we can start investigating!"

  Ghost "We shall begin our inquiry where, Sari?"

  show sari default #as side image"

  "Where should [ghostname] and I commence our investigation?"

  menu:
    "The foyer.":
      jump lbl_019
    "The back office.":
      jump lbl_020
    "The morgue.":
      jump lbl_021

label lbl_019:

  show bg foyer with slow_dissolve

  "[ghostname] and I go to the foyer."

  Sari "There's nothing here. Why did I think we'd find anything here?"

  "I turn on my heel to go elsewhere, then hesitate as I remember something."

  show sari anxious #as side image"

  Sari "That knocking on the front door earlier, you were doing that, right?"

  Ghost "I heard those sounds as well. It may alleviate your anxieties to know that I bore no responsibility for those."

  Sari "Yeah, that doesn't make me feel better at all. If you didn't knock, who did?"

  show sari default #as side image"

  "Maybe I should check on the front door again, just to be sure?"

  menu:
    "Check on the front door a second time.":
      jump lbl_022
    "Once was enough.":
      jump lbl_023

label lbl_020:

  show bg office with slow_dissolve

  "[ghostname] and I enter the back office."

  if sheet_music == True:
    jump lbl_028
  if sheet_music == False:
    jump lbl_029

label lbl_021:

  $death_cause = True
  $ clues_collected += 1

  show bg morgue with slow_dissolve

  "[ghostname] and I enter the morgue."

  Sari "Now there's not much to investigate here, is there?"

  Sari "But we might as well look at the cadaver. Perhaps staring death in the face will help you remember your own."

  "I open the refrigeration unit."

  show bg morgue_corpse with slow_dissolve

  "[ghostname] and I both stare down at the corpse. Neither of us speaks."

  show sari anxious #as side image"

  "There's a sinking sensation in my chest. I puzzle over this feeling, then my mind catches up."

  Sari "Hang on. This can't be right."

  Sari "Why's she already in her outfit for tomorrow? I was supposed to dress her."

  Sari "I was looking forward to it too. I wanted to do it all on my own, for the first time ever."

  Sari "Is Papa pulling my leg? But why? Is he trying to make a twisted point?"

  "[ghostname] glances down at my feet."  

  Ghost "No one is pulling your leg. You and I are entirely by ourselves."

  show sari default #as side image"

  "I blow out a sigh."

  Sari "I {i}know{/i} that. It's a figure of speech. Have you ever heard of it?"

  stop music fadeout 1.0

  "[ghostname] only regards me with dignified silence, perhaps not wanting to appear uninformed."

  "As I'm endeavoring to explain the linguistic concept to him, I keep gazing down at the mysteriously clothed cadaver."

  play music suspense fadein 2.0

  show sari shock #as side image"

  "Wait. What was that?"

  "Did the corpse's eyelids flutter just now?"

  "No. No way."

  "That was probably a trick of the light overhead. Or an optical illusion. Right?"

  menu:
    "Yes, the flutter was simply a trick of the light.":
      jump lbl_025
    "I should check the corpse's pulse.":
      jump lbl_026
  
label lbl_022:

  $invisible_barrier = True
  $ clues_collected += 1

  stop music fadeout 1.0

  show sari anxious #as side image"

  "Yeah, it never hurts to be safe!"

  "I fiddle with the three locks, then push the front door open again."

  play music suspense fadein 2.0

  show bg foyer_open with slow_dissolve

  "Like before, there's nothing there."

  Sari "I wonder what it was. What made that knocking noise before?"

  Sari "But maybe there are some things we just aren't meant to know."

  show sari default #as side image"

  "As I continue staring out the doorway, [ghostname] stands beside me."

  "He also gazes outside."

  Sari "How often have you tried stepping beyond this threshold?"

  Ghost "I have attempted this feat more times than I can plausibly count."

  Ghost "I have also tried the windows, but the same thing always happens."

  "He sticks his arm beyond the doorway."

  stop music fadeout 1.0

  show sari shock #as side image"

  "The ghostly essence of his form distorts, as if it's pushing against an invisible barrier."

  Sari "Hard-core!"

  play music bgm fadein 2.0

  show sari smile #as side image"

  Sari "I mean, this limitation must frustrate you to no end, but it does look cool. Like some kinda sci-fi movie."

  show ghost smile at center

  Ghost "I am then glad that the visual aspect of this mysterious phenomenon pleases you, if nothing else."

  Sari "Yet another mysterious phenomenon to add to the pile."

  show sari default #as side image"

  show ghost default at center

  "With this, I lock the front door securely once more."

  show bg foyer with slow_dissolve

  jump lbl_024

label lbl_023:

  "I shouldn't let paranoia get the better of me. If I've checked the door once, there's no need to check it again."

  jump lbl_024

label lbl_024:

  Sari "We should go, [ghostname]. There's nothing to investigate here."

  "Which place should we check next?"

  menu:
    "The back office.":
      jump lbl_020
    "The morgue.":
      jump lbl_021

label lbl_025:

  $ papa_trust += 1

  stop music fadeout 1.0

  show sari default #as side image"

  "It's been a long and eventful day. No wonder I'm seeing things."

  "I shake my head to clear it, then turn toward [ghostname]."

  play music bgm fadein 2.0

  Sari "I'm guessing that, while Yael and I were watching a movie, Papa came back downstairs to dress the cadaver himself."

  Sari "Perhaps Papa was worried I'd do it wrong — cut up this fancy wedding dress or something."

  show sari anxious #as side image"

  Sari "But I wouldn't have ruined the dress, you know?"

  Sari "Ever since I was a kid, I've watched Papa dress countless corpses. I've learned all the tricks of the trade."

  Sari "Papa could've counted on me. I should let him know that next time."

  show sari default #as side image"

  Sari "Okay, okay. Let's focus on what we came here to do."

  jump lbl_027

label lbl_026:

  show sari anxious #as side image"

  "Yes, I should check the corpse's pulse, regardless of whether the flutter was caused by some trickery of light."

  "When I got home from classes today, Papa told me he'd finished the embalming process and left me to do the makeup."

  "But who knows? Papa might have missed some crucial step of his procedure this time."

  "I hold my breath before I check the corpse's neck and wrists."

  stop music fadeout 1.0

  show sari smile #as side image"

  Sari "Yep. Definitely dead."

  "I exhale a sigh of relief."

  play music bgm fadein 2.0

  show sari default #as side image"

  Ghost "The lifelessness of this lady is a preferable thing for you?"

  Sari "Indeed. Here at Roxas & Roxas Funeraria, we only bury the definitely dead."

  jump lbl_027

label lbl_027:

  Sari "So what do you think, [ghostname]?"

  Sari "Is looking at this dead body sparking any memories of your own death?"

  show ghost anxious at center

  "[ghostname] squints down at the cadaver."

  Ghost "I have seen corpse after corpse pass through this funeral home and yet never clued in to the cause of my own demise."

  Ghost "Absolutely nothing comes to mind, even after spending nearly two decades here."

  show sari shock #as side image"

  show ghost default at center

  Sari "Almost two decades? Then you've been haunting the funeral home for as long as I've been alive!"

  Sari "Maybe your death took you totally by surprise! That's why you have no memory of it!"

  show sari default #as side image"

  Ghost "I sometimes amuse myself by speculating that I never died at all."

  Sari "But how else can you be a ghost, if you never died?"

  Ghost "This speculation shall perhaps forever remain speculation."

  Ghost "We are checking which room after this one?"

  "As I close the door to the refrigeration unit, I consider his question."

  show bg morgue with slow_dissolve

  Sari "The more I think about it, the more I realize that the back office is the best place for us to buckle down to our detective work."

  Sari "Unlike the morgue, the office has way more stuff for us to look at."

  Sari "None of these corpses that can somehow dress themselves when you've left them alone for long enough."

  Ghost "We should then trust your instincts and transfer to the office."

  jump lbl_020

label lbl_028:

  show sari shock #as side image"

  Sari "Oh, I almost forgot!"

  show sari default #as side image"

  Sari "My buddy Yael found this on the office floor earlier."

  "I extract the sheet music from my pocket and unfold it."

  Sari "The song that Yael was playing on his guitar? This is it. So this is probably the same song your music box plays."

  "I beckon the crumpled paper toward [ghostname], just before remembering that he can't hold solid objects, or so he claims."

  "Perhaps impulsively, he presents his palm to me, ready to receive the sheet music."

  show sari shock #as side image"

  "And the seemingly impossible happens. The piece of paper makes contact with his skin."

  "The sheet music rests on his palm. It doesn't fall."

  show sari anxious #as side image"

  "I furrow my brows."

  Sari "Has this ever happened before?"

  Ghost "I can touch and keep a limited list of objects, which I presume I took with me when I came into this new class of existence."

  show sari default #as side image"

  Sari "Like your music box, right?"

  show ghost smile at center

  Ghost "You are correct. I knew not before this moment that the list was susceptible of any extension."

  Ghost "This is a momentous revelation. I thank you for making this possible."

  show ghost default at center

  "As he silently surveys the neatly penned notes of the sheet music, I leave him to it."

  jump lbl_030

label lbl_029:

  show sari shock #as side image"

  "The tattered remains of paper, discarded on the floor, catch my attention at once."

  Sari "Oh! Oh no!"

  Sari "This could've been a juicy clue! Rats must have ravaged it while I was away!"

  show sari default #as side image"

  Ghost "This shredded paper was once what?"

  Sari "Sheet music. But it doesn't matter now. It's gone."

  Sari "We should look for other clues instead."

  jump lbl_030

label lbl_030:

  stop music fadeout 1.0

  show sari smile #as side image"

  "It's time to investigate!"

  "Humming happily, I dig into the filing cabinets for any potential hints as to [ghostname]'s unfinished business."

  play music menumusic fadein 2.0

  show sari default #as side image"

  "Within five minutes, I manage to heap a mountain of promising objects on the desk."

  "[ghostname] drifts closer so that he can visually inspect my selection."

  Sari "Which one do you want me to show you?"

  Ghost "I shall leave this decision to your sound judgment."

  "Which item should I hold up to [ghostname] first?"

  menu:
    "A photo album with yellowing pages.":
      jump lbl_031
    "Mama's pocket mirror.":
      jump lbl_032

label lbl_031:

  $photo_album = True
  $ clues_collected += 1

  "I go for the Roxas family's photo album first."

  "[ghostname] leans over my shoulder as I slowly flip through yellowing pages filled with sepia photographs."

  "For the most part, he silently regards the faces of my deceased family members. He nods as I read out their names."

  "When we reach the wedding picture of my parents, he holds up his hand — a signal for me to stop."

  Sari "If you're bound to the funeral home, you probably wouldn't have known my Mama."

  Sari "She and Papa lived elsewhere. Papa only took up the family's mortuary business after Mama died giving birth to me."

  Ghost "I believe I recognize your mother. I know not how, but her face is as familiar to me as this music box I keep."

  show sari smile #as side image"

  Sari "You met Mama when you were alive, then! That's a major clue!"

  "As I keep flipping through comparatively recent pictures, he makes more noises of recognition."

  Sari "You don't look like anybody in these photos, but maybe you were a distant relative. Or a family friend. That makes sense."

  show sari default #as side image"

  show ghost anxious at center

  "He points toward a particularly faded photograph. A man with a somber smile, sleepy eyes."

  Ghost "This person is who?"

  Sari "Lolo Rizaldo, my paternal great-grandfather. He was the one who originally established Roxas & Roxas Funeraria."

  Sari "Lolo peacefully passed away in his sleep some years ago."

  show sari shock #as side image"

  show ghost shock at center

  "Then the strangest thing happens."

  "I never would have imagined a ghost could shiver, but that's what [ghostname] does."

  show sari default #as side image"

  show ghost default at center

  Ghost "I would now like to move on to the next item."

  jump lbl_033

label lbl_032:

  "I hold up Mama's pocket mirror to [ghostname] first."

  "As expected, he doesn't have a reflection."

  Sari "So you have no idea what you look like, huh."

  Ghost "My knowledge of the particulars of my own appearance is essential to our quest?"

  Sari "I suppose not. Let's move on."

  jump lbl_033

label lbl_033:

  "Which prospective clue should I show [ghostname] next?"

  menu:
    "Torn movie tickets.":
      jump lbl_034
    "Mama's violin.":
      jump lbl_035

label lbl_034:

  "I hold up the used movie tickets to [ghostname]. The tickets are for {i}The Exorcist,{/i} the 1973 horror flick."

  "He only stares, not saying anything."

  Sari "Now that I think about it, these tickets — for this specific movie — seem fairly ominous to show to a ghost."

  Ghost "I would indeed advise you not to present these tickets to a spectral entity more threatening than myself."

  Sari "I'll keep that in mind, if and when I befriend other ghosts."

  Sari "Let's just move on."

  jump lbl_041

label lbl_035:

  $papa_violin = True
  $ clues_collected += 1

  "At least I presume this violin was Mama's, based on a photograph I once saw in Papa's room."

  "In the photo, Mama was lovingly polishing the violin."

  "When I went to search for the picture again, purely because I wanted to gaze at the woman I'd never known, I couldn't find it anymore."

  "Papa must have noticed that I'd found the picture, and purposefully hid it from me."

  "As I dwell on this memory, I hold up Mama's violin to [ghostname]."

  if sheet_music == True:
    jump lbl_036
  if sheet_music == False:
    jump lbl_037

label lbl_036:

  "Similarly to what happened with the sheet music earlier, he reaches for the violin, as if by impulse."

  show sari shock #as side image"

  "And just like with the sheet music, his skin manages to make contact with it."

  show ghost smile at center

  "I watch as he cradles the violin in his arms, rocking it like it's an infant."

  show sari smile #as side image"

  Sari "You seem to have a real affinity with musical items."

  jump lbl_038

label lbl_037:

  "Perhaps impulsively, he extends his arms to receive the instrument."

  show sari shock #as side image"

  "And the seemingly impossible happens. The violin makes contact with his skin."

  "Cautious as can be, I let it go. The instrument stays in his arms. It doesn't tumble to the floor."

  show sari anxious #as side image"

  "I furrow my brows."

  Sari "Has this ever happened before?"

  Ghost "I can touch and keep a limited list of objects, which I presume I took with me when I came into this new class of existence."

  show sari default #as side image"

  Sari "Like your music box, right?"

  Ghost "You are correct. I knew not before this moment that the list was susceptible of any extension."

  show ghost smile at center

  Ghost "This is a momentous revelation. I thank you for making this possible."

  "I watch as he cradles the violin in his arms, rocking it like it's an infant."

  show sari smile #as side image"

  Sari "Maybe you have an affinity with musical items."

  jump lbl_038

label lbl_038:

  Ghost "This violin is not just any musical item. This used to belong to me. I am certain of it."

  show sari default #as side image"

  show ghost default at center

  Sari "Maybe so, but that's in the past now. You can't keep it. In fact, I might get in trouble for even touching it."

  Sari "Papa seems to hate music and all things related to music. He must have kept this violin for a reason."

  "All reluctance, [ghostname] holds out the instrument to me."

  show sari smile #as side image"

  Sari "Keep your chin up! This is definitely an important clue!"

  Sari "We're getting somewhere now! We'll figure out your unfinished business soon enough!"

  if music_box == True:
    jump lbl_039
  if music_box == False:
    jump lbl_040

label lbl_039:

  $miniature_rose = True
  $ clues_collected += 1

  show sari anxious #as side image"

  "I'm about to return the violin to the place where I found it, when I notice a peculiar feature."

  "A subtle engraving on the varnished wood. A rose, which calls to mind something I saw earlier tonight."

  show sari default #as side image"

  "I motion for [ghostname] to come even closer. I show him the engraving."

  Sari "Doesn't this remind you of the miniature rose? The one that spins when the melody plays in your music box?"

  "He says nothing, but his expression is contemplative as I return the violin to its proper place."

  jump lbl_041

label lbl_040:

  show sari default #as side image"

  "He doesn't protest as I carefully return the violin to the place where I found it."

  jump lbl_041

label lbl_041:

  "I'm now hunting for another potential clue on the overcrowded desk."

  "To check on the items underneath it, l shove a broken umbrella past the edge of the desk."

  show sari shock #as side image"

  "One of the umbrella's steel rods snags on a stained-glass candleholder, which crashes down too."

  "The candleholder shatters into countless prismic pieces."

  show sari default #as side image"

  show ghost anxious at center

  "[ghostname] frets over me, not unlike an excessively protective parent."

  "I insist that I'm fine. Everything's fine."

  show ghost default at center

  Sari "That candleholder was a pointless kindergarten project. Papa was too attached to ever use it or discard it."

  Sari "Now it's ended up a hazard, with nothing to show for it. Just ignore the mess."
 
  "I recommence excavating the mini mountain I've made on the desk. Which item should I select next?"

  menu:
    "Papa's ledger of accounts.":
      jump lbl_042
    "My great-grandfather's walking cane.":
      jump lbl_043

label lbl_042:

  "I show [ghostname] Papa's ledger of accounts."

  "The book is filled with figures representing debits, credits, assets, liabilities, owners' equity, revenues, and expenses."

  "[ghostname] nods."

  Ghost "You have my everlasting gratitude for imparting this illuminating information."

  "Well, that was a tactful way to thank me for something so utterly useless."

  jump lbl_044

label lbl_043:

  $lolo_cane = True
  $ clues_collected += 1

  hide ghost

  "I hold up Lolo Rizaldo's old cane. Sleek, carved of ebony. Tarnished silver handle."

  "Just as I'm wondering why this cane is still here, I notice that [ghostname] is suddenly on the far side of the room."

  show sari anxious #as side image"

  show ghost shock at center with dissolve

  Sari "[ghostname]? What are you doing over there? What's wrong?"

  "Can ghosts even hyperventilate? That's what [ghostname] appears to be doing."

  Ghost "I beseech you to keep that cursed object in a place where I can no longer see it."

  "As requested, I swiftly stuff the cane back inside the filing cabinet."

  show sari default #as side image"

  show ghost anxious at center

  "With the cane out of sight, [ghostname] drifts toward me again."

  Ghost "I sincerely apologize. I did not intend to speak so imperiously, when you have been the very portrait of patience with me."

  show ghost default at center

  Sari "Hey, don't worry about it. Something about that cane clearly triggered you. That's a useful clue, if nothing else."

  jump lbl_044

label lbl_044:

  Sari "Let's look for more stuff."

  stop music fadeout 1.0

  "At this point, I ransack the filing cabinets again for even more prospective clues."

  "I dump another mound of items on top of the pile already on the desk. Numerous objects cascade down to the floor."

  play music suspense fadein 2.0

  show sari shock #as side image"

  hide ghost

  "All of a sudden, a voice booms by the doorway."

  show ghost anxious at left with dissolve

  show papa anxious at right with dissolve

  Papa "What on earth are you doing, Rosario?"

  "Papa is staring at me as if I'm some criminal intruder, instead of his own daughter."

  "I freeze, caught in the act."

  Papa "I heard the sound of breaking glass."

  Papa "You should sweep up these fragments with a broom! You could really hurt yourself!"

  "Papa marches into the office, but stops short of the area strewn with stained-glass shards."

  "He now glares at the jumbled mess I've heaped on the desk and at the assorted objects that have rolled down to the floor."

  Papa "What's all this? Why are you going through my private things?"

  show sari anxious #as side image"

  show ghost default at left

  show papa default at right

  "I glance at [ghostname], but of course he can't save me now."

  "Papa doesn't seem to even see [ghostname]. Wherever my new ability came from, it doesn't appear to be hereditary."

  show sari default #as side image"

  "What should I say? Should I spin some lie, or should I avoid answering Papa's questions directly?"

  menu:
    "Lie outright.":
      jump lbl_045
    "Evade Papa's questions.":
      jump lbl_046

label lbl_045:

  stop music fadeout 1.0

  "I should at least attempt to worm my way out of this predicament, right?"

  "Papa probably won't believe me, but there's always the chance that he will."

  play music bgm fadein 2.0

  Sari "I was looking for something, but I couldn't find it anywhere."

  Papa "What were you looking for?"

  "I spit out the very first thing that comes to mind."

  Sari "An old photo of Mama, polishing a violin."

  show ghost anxious at left

  show papa anxious at right

  "Papa raises an eyebrow."

  Papa "I keep that photo in my bedroom. I know you know that it's there."

  "I can try to formulate more lies, perhaps."

  "But considering the skepticism in Papa's expression, I'll only be digging a deeper hole for myself if I do."

  jump lbl_047

label lbl_046:

  $ papa_trust += 1

  stop music fadeout 1.0

  "Yeah, Papa isn't easy to fool."

  "He'll most likely see through any lie I tell him."

  play music bgm fadein 2.0

  Sari "Look, I didn't think this stuff was private. If you wanted privacy, you wouldn't leave everything lying around here."

  Sari "None of the cabinets have any locks." 

  Sari "Yael can access this stuff easily. The clients too, every time they're left alone inside the office."

  show ghost anxious at left

  show papa anxious at right

  Papa "Rosario, you're just attempting to dodge my questions."

  "Just as I suspected, Papa isn't one I can ever fool. He knows me too well."

  jump lbl_047

label lbl_047:

  show sari anxious #as side image"

  show ghost default at left

  show papa default at right

  "I stand there in awkward silence."

  "What else can I even say?"

  show ghost anxious at left

  show papa anxious at right

  Papa "What's gotten into you, Rosario? Why can't you just speak to me, openly and honestly, the way you used to?"

  Papa "How can I trust you to take over the mortuary business someday, if you can't do something as simple as {i}talk{/i} to me?"

  show sari mad #as side image"

  show ghost default at left

  show papa default at right

  "These words rub me the wrong way. Before I know it, I'm lashing out."

  Sari "You think it's easy for me, or for anybody else, to talk to you? You {i}never{/i} make it easy!"

  Sari "Haven't you noticed the way Yael reacts to you? He never shuts up around me, but practically turns into stone around you!"

  Sari "You twist every conversation into an argument or lecture! It's exhausting!"

  show ghost anxious at left

  show papa anxious at right

  Papa "Rosario, you don't know what {i}exhausting{/i} means until you've been in my shoes."

  Papa "Do you think it's a simple matter to run this place alone? To raise a daughter alone?"

  Sari "But you've never run this place alone! I was always here with you, helping you with everything!"

  Sari "And if you never wanted to raise a daughter, why didn't you just chuck me into a foster home?"

  Papa "How can you even say that, Rosario? You know I'd {i}never{/i} do that. You're my daughter, and —"

  Sari "But the thought of giving me up must have crossed your mind sometime!"

  Sari "Mama died giving birth to me! {i}Of course{/i} you'd want to get rid of me!"

  show sari anxious #as side image"

  "The moment the words leave my lips, I wonder whether I've gone too far."

  "Papa stares at me in disbelief."

  hide papa

  show sari default #as side image"

  "He then turns on his heel and stomps out of the office."

  show ghost default at center with dissolve

  "I'm alone with [ghostname] once more."

  if papa_trust >= 2:
    jump lbl_048
  if papa_trust < 2:
    jump lbl_049

label lbl_048:

  if clues_collected >= 4:
    jump lbl_050
  if clues_collected < 4:
    jump lbl_068

label lbl_049:

  show sari anxious #as side image"

  "With an almighty groan, I sink down onto one of the chairs in the office."

  Ghost "You will not attempt to chase and to converse with your father?"

  show sari mad #as side image"

  Sari "What's the point? Believe me, it's impossible to win against Papa when he's being all hostile like this." 

  Sari "Arguing with him when he's in a dark mood is as productive as beating yourself on the head with a baseball bat."

  Sari "No matter what I say now, he'll only warp my words so that he gets the upper hand."

  show sari default #as side image"

  Sari "Luckily for me, you're here. You're much better company than that stubborn old man."

  if clues_collected >= 4:
    jump lbl_051
  if clues_collected < 4:
    jump lbl_070

label lbl_050:

  $path_one = True

  "I'm about to follow Papa out of the room — whether to apologize to him or to argue some more, I don't even know."

  "But [ghostname] stops me in my tracks."

  Ghost "Sari, I need to divulge something significant before you converse with your father."

  show sari anxious #as side image"

  Sari "Can't it wait?"

  Sari "Knowing Papa, he might already be on the phone with our Pangasinan relatives, making arrangements to ship me off!"

  show sari default #as side image"

  "But [ghostname] shakes his head. He remains quiet until I've taken a seat on one of the chairs."

  jump lbl_052

label lbl_051:

  $path_three = True

  Ghost "I have something important to tell you while we are here. You will listen to my story?"

  Sari "Yeah, of course. We're friends, after all."

  jump lbl_052

label lbl_052:

  stop music fadeout 1.0

  Sari "So what is it? I'm listening."

  show ghost smile at center

  Ghost "I should first thank you for embarking on this investigation with me."

  play music mellow fadein 2.0

  Ghost "I have finally come to terms with my own nature and identity, as a result of your tireless efforts."

  Ghost "The clues that you uncovered for me have succeeded in sparking deeply buried memories."

  show sari shock #as side image"

  "Wide-eyed, I lean forward on my chair."

  Sari "Seriously? That's awesome! Then at least one thing went right today!"

  show sari smile #as side image"

  Sari "So who are you?"

  Sari "I can't wait to call you by your actual name!"

  show sari default #as side image"

  show ghost default at center

  Ghost "Names are a privilege bestowed upon humans and tamed animals."

  Ghost "I have no name other than the one you gave me, for I was neither of those."

  show sari shock #as side image"

  Sari "Huh? Then who are you?"

  Ghost "I am nothing more and nothing less than an embodiment of a dream that has come to die in this funeral home."

  Sari "An embodiment of a dream?"

  show sari default #as side image"

  if invisible_barrier == True:
    jump lbl_053
  if invisible_barrier == False:
    jump lbl_054

label lbl_053:

  Ghost "I earlier tried to stick my arm beyond the doorway at the foyer."

  Ghost "I could not, because by my very nature, I am trapped inside here."

  jump lbl_054

label lbl_054:

  if death_cause == True:
    jump lbl_055
  if death_cause == False:
    jump lbl_056

label lbl_055:

  Ghost "I was never born in the same manner that men are born."

  Ghost "I also never died and will never die in the usual manner of men. This is why I cannot remember my death."

  jump lbl_056

label lbl_056:

  Ghost "I owe my existence solely to my original dreamer."

  Ghost "My dreamer's visionary strength was such that I developed my own sentience once he abandoned me."

  Ghost "You intimately know this person who dreamed me into being. You have after all lived within his walls for the past nineteen years."

  show sari shock #as side image"

  Sari "Do you mean Papa?"

  Sari "{i}Papa{/i} created you? You're {i}his{/i} abandoned dream?"

  show sari default #as side image"

  Ghost "Your father was a proficient violinist in the years foregone."

  Ghost "He aspired to compose melodies that might resurrect even those possessed of the most lifeless of hearts."

  show sari shock #as side image"

  Sari "Papa plays the violin?"

  Sari "But he hates music! He claims that music gives him migraines!"

  show sari default #as side image"

  Ghost "Letting go of his music indeed pains him every day, but he has never hated it."

  Ghost "His musical ambitions had detractors that deterred him in his youth."

  Ghost "His parents indulged his talent as dinner entertainment, but desired for him to someday take over the family's mortuary business."

  show ghost anxious at center

  Ghost "Others in the family, however, were more stringent with their standards. They sought to dictate every step your father took."

  if photo_album == True:
    jump lbl_057
  if photo_album == False:
    jump lbl_058

label lbl_057:

  Ghost "Lolo Rizaldo, in particular, tolerated no talk of music or similarly fanciful endeavors. He belittled your father at every encounter."

  jump lbl_058

label lbl_058:

  if lolo_cane == True:
    jump lbl_059
  if lolo_cane == False:
    jump lbl_060

label lbl_059:

  Ghost "Lolo Rizaldo would measure your father's every move by his own archaic standard of masculinity."

  Ghost "Your father was forever falling short, and for every instance he was deemed deficient, he earned another strike from his Lolo's cane."

  jump lbl_060

label lbl_060:

  show ghost smile at center

  Ghost "Your father's life only took a turn for the better when he met a woman whose dreams roared as loudly as his own."

  "I've been all but rendered silent by the story that [ghostname] tells me, but I can't help interjecting now."

  show sari sad #as side image"

  show ghost default at center

  Sari "Mama, right? Papa loved her so much. As far as I know, he's never loved anyone since she died."

  Sari "That violin in Papa's office — it was Mama's, wasn't it?"

  show sari default #as side image"

  Ghost "Your mother's dreams were multitudinous, while your father's dreams were few and ardent."

  if papa_violin == True:
    jump lbl_061
  if papa_violin == False:
    jump lbl_062

label lbl_061:

  Ghost "She saved up to purchase that violin as a gift, shortly after your father's Lolo smashed the instrument he had kept since his youth."

  jump lbl_062

label lbl_062:

  if miniature_rose == True:
    jump lbl_063
  if miniature_rose == False:
    jump lbl_064

label lbl_063:

  Ghost "Your mother engraved the spruce of the violin's soundboard with the flower for which she was named." 

  jump lbl_064

label lbl_064:

  Ghost "Your father would think of your mother every time he played the violin, no matter how far or how frequently she traveled."

  Ghost "He composed a song for her while she was away. It is the same melody that plays in my music box, in my heart."

  if sheet_music == True:
    jump lbl_065
  if sheet_music == False:
    jump lbl_066

label lbl_065:

  Ghost "He kept the sheet music he penned back then, all to hear the notes in his head, even after he had stowed away the instrument."

  jump lbl_066

label lbl_066:
  
  Ghost "Your mother came home to your father just in time to bring you into the world."

  Ghost "Your father played the song for her, and for you in her belly, only once before everything fell apart."

  stop music fadeout 1.0

  "Silence follows this ominous ending."

  show sari sad #as side image"

  Sari "Your story ends right there? After Mama bore me, then passed away soon afterward?"

  play music bgm fadein 2.0

  Ghost "It does."

  Sari "Papa moved back here, to raise me where he'd been raised. To inherit the family business instead of pursuing his ambition."

  "[ghostname] bows his head."

  Sari "And that was when his dreams broke down, to bear the full weight of his new reality."

  show sari default #as side image"

  "[ghostname] nods again."

  if path_one == True:
    jump lbl_067
  if path_three == True:
    jump lbl_069

label lbl_067:

  "I rise from the chair."

  show sari smile #as side image"

  Sari "Thank you for telling me everything. I know what to say to Papa now."

  Sari "Just wait here, okay? I'll be back for you soon."

  show ghost smile at center

  Ghost "I bid you the best of luck."

  hide ghost

  show bg viewing with slow_dissolve

  show papa anxious at center with dissolve

  "I find Papa in the viewing room."

  "He's glaring down at the coffin, wiping off fingerprints from its polished surface with a dustcloth."

  show sari anxious #as side image"

  Sari "Pa, I'm sorry for saying all those things earlier. I was way out of line."

  stop music fadeout 1.0

  show papa default at center

  "Pa only grunts in response to this apology."

  "Still, I forge on."

  play music mellow fadein 2.0

  show sari sad #as side image"

  Sari "I understand how hard things have always been for you — taking care of both me and the mortuary business, without Mama."

  Sari "You must miss Mama terribly, every single day."

  show papa anxious at center

  "Papa finally meets my eyes."

  Papa "I do miss her. I loved your Mama very much, you know."

  Sari "I know."

  show sari default #as side image"

  Papa "But I {i}never{/i} want you to blame yourself for what happened to her." 

  Papa "Rosario, you were and {i}are{/i} such a blessing to us both. I'm sorry if I can't always express that."

  show sari smile #as side image"

  Sari "It's okay, Pa. I know you're trying, but your words sometimes come out the wrong way."

  show papa smile at center

  Papa "You did make a fair point earlier. I was never alone."

  Papa "You were always such a bright child."

  Papa "And you grew up to become a curious and courageous individual, eager to help wherever you were needed."

  show papa default at center

  Papa "How could I ever give away the best part of my life to a foster home?"

  show sari anxious #as side image"

  Sari "About that, I didn't really mean what I said."

  Sari "Sorry, I was just being a tad melodramatic."

  show papa smile at center

  Papa "You might have gotten that melodramatic streak from me."

  Papa "Your Mama was always relentlessly optimistic, no matter how hard things got."

  show sari default #as side image"

  show papa default at center

  "As a comfortable silence settles between us, we both gaze down at the coffin."

  Sari "Do you ever imagine yourself being inside one of these?"

  Papa "We'll all end up inside one of these coffins soon enough, whether we want to or not."

  Papa "That is, unless you're smart enough to mention in your will that —"

  Sari "Cremation is the best choice."

  show sari smile #as side image"

  show papa smile at center

  "I finish the sentence for Papa. I've heard him say these words often enough, though never in front of the clients."

  "Papa and I are smiling at each other."

  show sari default #as side image"

  show papa default at center

  Sari "Pa, you understand better than anyone that we'll all die someday."

  Sari "But did you know that parts of you can die long before you're laid inside one of these coffins?"

  show papa anxious at center

  Papa "What do you mean?"

  Sari "Let's sit down. This is going to be a long story."
  
  hide papa

  show bg darkness with slow_dissolve

  "I tell Papa about everything I've learned tonight."

  "About [ghostname], the physical manifestation of Papa's broken dream of becoming a professional musician and composer."

  "About everything [ghostname] told me regarding Papa's past."

  "No matter how seemingly ridiculous my story is, Papa has no choice but to believe me."

  "How else would I know the most specific details of secrets about which Papa has never told a soul?"

  stop music fadeout 1.0

  "Once I finish telling Papa the story of tonight, we both return to the back office."

  "We need to sweep the mess and tidy things up."

  play music bgm fadein 2.0

  show bg office with slow_dissolve

  show papa default at center with dissolve

  Papa "You mean [ghostname] is here right now? Watching us clean everything?"

  show sari smile #as side image"

  Sari "Yep, he's right here."

  Papa "Should I say hi?"

  Sari "Yeah, why not? Consider me your official translator for spectral entities you can neither hear nor see."

  show papa default at left with dissolve

  show ghost default at right with dissolve

  "Papa waves toward the apparent nothingness."

  "[ghostname] silently observes him."

  show papa smile at left

  show ghost smile at right

  Papa "Hi."

  Ghost "I am extraordinarily pleased to officially make your acquaintance."

  show sari default #as side image"

  show papa default at left

  show ghost default at right

  "I repeat to Papa the exact phrasing of [ghostname]'s response to him."

  Papa "Eh, why does he talk like that?"

  show sari laugh #as side image"

  Sari "Because your old musical ambitions were a little stuffy, a little pompous, I suppose."

  "I do, however, face [ghostname] and give a hoot of laughter, just to let him know that I'm only teasing."

  show sari default #as side image"

  "Papa and I return everything in the office to its rightful place, with one notable exception."

  show papa anxious at left

  show ghost anxious at right

  "My great-grandfather's ebony cane."

  Papa "I'm throwing this away. I had no idea it was even still here."

  show sari smile #as side image"

  show papa default at left

  show ghost default at right

  "Once we've chucked the cane into the trash can, I finally hand Papa the violin."

  Sari "Pa, will you play me and [ghostname] something?"

  stop music fadeout 1.0

  show sari default #as side image"

  "It's been almost two decades since Papa last played the violin, but he's managed to keep it in perfect condition all this time."

  "Papa expertly twists the pegs to tune the instrument."

  "He gives a little cough as he positions the instrument beneath his chin."

  play music mellow fadein 2.0

  "His first few notes are shaky at best."

  "But simply seeing Papa reunited with the music he's denied for so long renders me speechless."

  "[ghostname], as if drawn forward by an irresistible magnetic force, drifts toward Papa as he continues playing."

  show papa smile at left

  show ghost smile at right

  "[ghostname] flashes a brief smile in my direction."

  hide ghost

  show sari shock #as side image"

  show papa default at center with dissolve

  "Then [ghostname] merges his being with Papa's."

  "At that exact split-second of fusion, a shudder seems to course all over Papa's bones."

  scene cg ending01_pic with slow_dissolve

  "The music that Papa plays transforms into something so deeply imbued with emotion."

  "I'm so moved that it's all I can do not to fall on my knees."

  "His melody is the most ethereally beautiful thing I've ever heard."

  scene cg ending01 with slow_dissolve
  $ persistent.ending_seen_01 = True
  $ ending_theme = "best"
  pause
  jump lbl_credits

  return

label lbl_068:

  show sari anxious #as side image"

  "I need to chase Papa — whether to apologize to him or to argue some more, I don't even know."

  "By the door, I turn to face [ghostname]."

  show sari default #as side image"

  show ghost anxious at center

  "His eyes look a little lost."

  Sari "I gotta talk to Papa. He's a real pain in the neck, but he's still family."

  show sari smile #as side image"

  Sari "Just stay here, okay? I'll be back for you soon."

  Sari "We'll figure out your unfinished business together. I promise."

  show sari default #as side image"

  "Without waiting for an answer, I hurry out the doorway to follow Papa."

  hide ghost

  show bg viewing with slow_dissolve

  show papa anxious at center with dissolve

  "I locate Papa in the viewing room."

  "He's glaring down at the coffin, wiping off fingerprints from its shiny surface with a dustcloth."

  show sari mad #as side image"

  Sari "Pa! How can you accuse me of being incapable of holding a proper conversation, when you're the one storming away?"

  "Papa turns, his icy glare directed toward me now."

  Papa "Rosario, you're being out of line. You shouldn't talk back to your elders so freely."

  Sari "What do you want me to do, then? Do you want me to be your silent and dutiful daughter forever?"

  Sari "Why don't you take the corpse in the morgue and preserve her in stinky chemicals instead! At least she'll never talk back!"

  Sari "If I want to be mad at you, I should be allowed to be mad at you!"

  Sari "How is it fair that you're the only one who gets to rant all the time?"

  Sari "Just because you're old, it doesn't mean you're always right!"

  "Just like this, Papa and I commence volleying insults and complaints back and forth."

  "We yell at each other for many minutes, as if competing to see who can holler the loudest."

  show sari default #as side image"

  show papa default at center

  "Eventually, we collapse on the chairs. We're both tuckered out due to our circuitous argument."

  "When I finally speak again, I keep my voice low, as my throat is swollen from all the screaming."

  show sari anxious #as side image"

  Sari "Pa, I can't help feeling like you secretly resent me."

  Sari "For trapping you in this job you only pretend to like, and in this funeral home forced on you by your family."

  stop music fadeout 1.0

  show sari default #as side image"

  "For once, Papa doesn't fire back at once. He stares ahead, seeming to contemplate, before replying to me."

  "His voice is also low, due to overuse. Raspy now."

  play music mellow fadein 2.0

  show papa anxious at center

  Papa "It's true. Being a funeral director was never my dream."

  Papa "But I need you to know something."

  Papa "I may have resented the rest of my family for the way they raised me. But I {i}never{/i} hated you."

  Papa "How can I hate you when you're the only reason this job is even a little bearable?"

  show papa default at center

  Papa "I never understood the subtle beauty of mortuary science before I started seeing the cadavers through your curious eyes."

  Papa "You love the minutiae of the work that goes on here, every day, in a way that I never will."

  Papa "I may not have been living my dream, but I was nurturing yours. So these decades in the funeral home were far from a waste."

  Papa "I kept this place running through the years for you, until the day arrives when you're ready to take over from me."

  Papa "And even then, I'll always be on standby, ready to help you as you've always helped me."

  show sari smile #as side image"

  "Without consciously planning it, I reach for Papa's hand."

  Sari "Thank you, Pa. And thanks for telling me all this."

  stop music fadeout 1.0

  show papa smile at center

  "I squeeze his hand. After a pause, he squeezes back."

  "We fall silent again, but the silence between us is comfortable now. Full of understanding, rather than bitterness."

  play music aria fadein 2.0

  show sari shock #as side image"

  show papa anxious at center

  "All of a sudden, the familiar melody of a music box plays, somewhere beyond the doorway of the viewing room."

  "I speak without thinking."

  Sari "[ghostname], what in the world are you —"

  "I clap my palm over my mouth as I remember that Papa isn't supposed to know anything about [ghostname]."

  show sari anxious #as side image"

  "This renewed peace between Papa and me is too fragile for me to risk it with stories of spectral entities only I can see."

  show papa cry at center

  "But Papa isn't paying any attention to me just now."

  "He's crying when I turn to look at him."

  Sari "Pa? What's wrong?"

  "But Papa is practically sobbing now, sobbing too hard to talk."

  show sari sad #as side image"

  "So I simply put my arm around him." 

  "I try to comfort Papa without words, until he regains enough composure to find his own again."

  Papa "Rosario, there are things I never told you. Memories I should have shared long ago. Will you listen?"

  Sari "Of course, Pa. I'll listen."

  hide papa

  stop music fadeout 1.0

  show bg darkness with slow_dissolve

  "So I listen as Papa tells me his story. It's a sad one, full of pain and death."

  "Nevertheless, I sense a weight gradually lifting from his shoulders, with every new detail he uncovers."

  play music mellow fadein 2.0

  "How long has he kept all these emotions locked within his hardened heart?"

  "What matters is he's telling me now. He has things to work through, but I swear that we'll work on them together."

  "He's not alone. He never was."

  "Once Papa returns upstairs to sleep, I head toward the back office to tidy up the mess I've made." 

  "I also need to update [ghostname] about the night's most recent developments."

  "Perhaps we can talk about all that as we continue searching for clues regarding his unfinished business."

  show bg office with slow_dissolve

  show sari shock #as side image"

  "But in the office, [ghostname] is nowhere to be found."

  "He's vanished into thin air, seemingly without a trace."

  show sari sad #as side image"

  "With my shoes crunching over the stained-glass shards, I step closer toward the desk, then spot something."

  scene cg ending02_pic with slow_dissolve

  "[ghostname] has left the music box there. The music box that makes up his heart."

  scene cg ending02 with slow_dissolve
  $ persistent.ending_seen_02 = True
  $ ending_theme = "good"
  pause
  jump lbl_credits

  return

label lbl_069:

  "I lean back on my chair. Gazing at the ceiling. Thinking about everything that [ghostname] has told me."

  "After a minute, I lean forward and meet [ghostname]'s eyes again."

  show sari anxious #as side image"

  Sari "So Papa had a difficult life, huh? But here's the thing."

  Sari "I know it's all the rage now to encourage everyone to chase their dreams. But I don't think that applies to Papa's specific case."

  Sari "His decision to turn away from his dreams in the past — and turn toward the reality of the present instead — makes sense to me."

  show sari sad #as side image"

  Sari "Maybe he loved music, once upon a time. But right now, music only seems to summon his worst memories."

  Sari "I mean, the mere sound of Yael strumming on a guitar is enough to trigger Papa's migraines."

  Sari "Yael probably reminds Papa of his younger self. Bright-eyed. Filled with dreams of hit singles and sold-out stages."

  Sari "No wonder Papa likes to lecture Yael. And no wonder Papa is strict with me as well."

  show sari default #as side image"

  Sari "Papa expects a lot from me. Too much, maybe. Unlike him, I've always loved the work we do here in the funeral home."

  Sari "Knowing where he's coming from, I'm beginning to understand what makes him tick."

  show sari smile #as side image"

  Sari "Thanks for telling me this stuff, [ghostname]."

  Ghost "You should perhaps speak with your father, equipped as you are with this new insight."

  show sari default #as side image"

  "I shake my head."

  Sari "Bad idea."

  show sari anxious #as side image"

  Sari "What would I even say? Should I tell him that a little bird whispered his entire life story to me?"

  Sari "Even if I know Papa's secrets, I have no believable way to explain how I found out about everything."

  Sari "Forget chucking me into a foster home. He'll send me straight to a psychiatric institution if I tell him the truth, or a version of it."

  show sari default #as side image"

  Sari "That's just the way Papa is, unfortunately."

  "I rise from the chair and stretch."

  show sari anxious #as side image"

  "As I survey the stained-glass fragments scattered around my feet, I groan."

  Sari "Ugh. I'll tidy up this mess first thing in the morning."

  Sari "All that bickering with Papa drained the last remnants of my energy."

  show sari default #as side image"

  Sari "I should go to bed. I have a lot to think about. And so does Papa, I'm sure."

  Sari "Once we've both cooled off from the big blow-up tonight, it will be easier to work out a truce with him."

  Sari "Since I can never win against Papa, a truce is the best result I can ever achieve."

  show sari smile #as side image"

  Sari "Let's talk more tomorrow, [ghostname]."

  Sari "Now that we understand how you got here, we just need to figure out how to get you out."

  show ghost smile at center

  "[ghostname] gives me a wavering smile."

  Ghost "I then look forward to tomorrow's adventure."
  
  scene cg ending03 with slow_dissolve
  $ persistent.ending_seen_03 = True
  $ ending_theme = "bad"
  pause
  jump lbl_credits

  return

label lbl_070:

  Sari "Can I rant to you? Just to blow off some steam?"

  Ghost "I will gladly listen to whatever you wish to share with me."

  show sari mad #as side image"

  "I suck in a shaky breath, then launch into a furious tirade about my problems with Papa."

  "All these problems have only snowballed with every passing day, so as it turns out, I have endless things to rant about."

  "[ghostname] listens attentively the entire time, not interrupting even once."

  show sari default #as side image"

  "I only stop when my throat is turning sore from blabbering too much."

  Ghost "I trust that unburdening your heart has offered you some measure of catharsis?"

  show sari anxious #as side image"

  "Staring down at the floor, I shake my head."

  "I don't feel any better. At all."

  show sari mad #as side image"

  "If anything, articulating every single reason for why Papa always grinds my gears has only intensified my fury."

  Ghost "You know of other methods to assuage your frustrations?"

  stop music fadeout 1.0

  show sari anxious #as side image"

  show ghost anxious at center

  "Rather than replying, I jump to my feet. The suddenness of my movement sends my chair crashing backward."

  "The clattering sound my chair makes is strangely satisfying."

  play music suspense fadein 2.0

  show sari mad #as side image"

  "Before I know it, I'm hollering wordlessly as I throw everything within reach across the room."

  "Whatever it takes to recreate that brief sense of satisfaction."

  "The photo album. The book of accounts. The busted umbrella."

  "No. None of those objects satisfies me. Not even a little bit."

  "Next, the pocket mirror. It smacks against a filing cabinet and shatters into myriad splinters."

  "That was marginally more satisfying. But still not enough."

  "I wildly whip my head around, hunting for better ammunition in this office, but a part of me already knows."

  "I know the best object to throw. The one thing that, when broken, will surely cause the most pain."

  "I unearth Mama's violin from its hiding place. Despite the instrument's age, there's not a speck of dust on the varnished wood."

  "With both fists firmly clamping the violin's neck, I smash it, using all my strength, against the filthy floor."

  show sari smile #as side image"

  show ghost shock at center

  "The crisp crunching of yielding wood."

  "Yes. The satisfaction of pure destruction, at its best."

  "With the ghost of a smile on my face, I notice a tumultuous noise rising now." 

  show sari shock #as side image"

  "From the corner of the office, where [ghostname] has been observing, there's a near-deafening discordant sound."

  "Like a grand piano being shoved beyond a window, falling several stories, then dying in an explosion of keys."

  "Again and again and again."

  hide ghost

  "Before my very eyes, [ghostname] splits in two jagged halves, with a horrible shriek."

  show bg darkness with slow_dissolve

  show sari sad #as side image"

  "Then, after all that, nothing."

  "[ghostname] is gone. Never to be seen again."
  
  scene cg ending04 with slow_dissolve
  $ persistent.ending_seen_04 = True
  $ ending_theme = "worst"
  pause
  jump lbl_credits

  return

label lbl_071:

  show bg office with slow_dissolve

  "We return to the back office."

  "I crouch down, intending to retrieve the sheet music that Yael left on the floor a while ago."

  "But Yael stops me."

  show yael shock at center

  Yael "Don't touch that! It's dangerous!"

  Sari "Dangerous? Why?"

  Yael "It's haunted! You said so earlier!"

  show sari anxious #as side image"

  show yael anxious at center

  Sari "I meant that the melody is haunted, not the paper itself."

  Sari "This sheet music could be a clue as to the source of the melody."

  "But Yael remains adamant that keeping the sheet music in my pocket will trigger some irreversible curse, so I relent."

  show sari default #as side image"

  "I leave the sheet music where it is on the floor."

  "Now, where should we go next?"

  menu:
    "The viewing room.":
      jump lbl_072
    "The morgue.":
      jump lbl_076

label lbl_072:

  $stopped_music = True

  show bg viewing_open with slow_dissolve

  "We enter the viewing room. An empty room full of empty chairs."

  "The sinister melody is much louder here. It comes from the coffin for tomorrow's wake."

  "I want to march forward to examine the open coffin, but Yael grips my arm."

  show sari anxious #as side image"

  show yael shock at center

  Sari "Let me go. I gotta check."

  Yael "Do you have a death wish or something? You can't!"

  show yael anxious at center

  show sari smile #as side image"

  Sari "Come on. It's just a coffin. How many coffins have you seen in all your months of working here?"

  Sari "What's the worst thing that can jump from a coffin to attack me? Something already dead, surely!"

  show yael shock at center

  Yael "That's even worse!"

  show sari default #as side image"

  Sari "You know, maybe Papa was being harsh earlier, but I do agree with one thing he said."

  Sari "Dead things can't hurt us. Living beings, on the other hand, like to destroy each other."

  show yael anxious at center

  Yael "Don't say that sort of stuff! You might be taunting something demonic lurking near the coffin!"

  show sari anxious #as side image"

  Sari "Something demonic? Why would a demon waste its time prowling a place like this?"

  Sari "We're college students! And Papa is a senior citizen with a modest income!"

  Sari "Whatever invisible entity is haunting us — it will be much better off possessing someone with the power to ruin the world!"

  "Yael and I continue to debate over the wisdom of approaching the coffin that's emitting the mysterious music, but then —"

  stop music fadeout 1.0

  show sari shock #as side image"

  show yael shock at center

  "THUD!"

  show bg viewing with slow_dissolve

  "The lid of the coffin has fallen shut, without warning."

  "The music playing has also stopped."

  play music suspense fadein 2.0

  hide yael

  show sari anxious #as side image"

  "While Yael yelps and huddles behind a chair, I take the opportunity to dash forward and open the coffin." 

  show bg viewing_open with slow_dissolve

  "There's nothing inside the coffin, as expected."

  "However, something about the coffin's velvet interior puts me on guard."

  "Curious indentations, as if some unidentifiable object has recently been resting here."

  show sari default #as side image"

  Sari "Hey, Yael! Come check this out!"

  show yael anxious at center with dissolve

  "But when I turn toward my friend, he's peeking from behind a chair. He hisses an urgent plea now."

  Yael "Sari, let's go! This room is probably haunted by hundreds of ghosts!"

  stop music fadeout 1.0

  show sari smile #as side image"

  "I can't suppress an indulgent smile."

  "Yael can be so adorable sometimes."

  play music bgm fadein 2.0

  show sari laugh #as side image"

  Sari "Surely not hundreds? Isn't a single ghost more than enough to scare you to death?"

  show yael mad at center

  Yael "Sari, come on!"

  show sari default #as side image"

  "Whoops, Yael is glaring, looking deadly serious. Is it time to go?"

  menu:
    "Crack one more joke.":
      jump lbl_073
    "Don't test Yael's patience.":
      jump lbl_074

label lbl_073:

  $ yael_romance += 1

  show sari smile #as side image"

  "Surely, just one joke won't hurt!"

  show yael default at center

  Sari "Oy, Yael! Before we leave, can you answer something for me? It's a crucial question about the ghost."

  Sari "You know, one ghost of the hundreds that you imagine are surrounding the coffin right now."

  show yael anxious at center

  "Yael scrunches up his face, his expression a cross between confusion and panic."

  Yael "What?"

  Sari "What's the ghost's favorite type of coffee?"

  "Yael only stares. Not comprehending."

  show sari laugh #as side image"

  "Delighted that he's stayed to listen to the entire joke, I crow the punchline."

  Sari "The ghost's favorite coffee is the {i}de-coffin-ated{/i} type!"

  show sari smile #as side image"

  "There's a beat of silence."

  show yael laugh at center

  "Then Yael seems to momentarily forget his fears."

  "He chuckles. Just a brief burst of laughter."

  show yael smile at center

  "It might have been a crappy joke, but if it made Yael smile in this situation, then it's good enough for me."

  jump lbl_075

label lbl_074:

  show sari anxious #as side image"

  "Yeah, Yael is obviously agitated."

  "Now isn't the appropriate time for jokes."

  jump lbl_075

label lbl_075:

  show sari default #as side image"

  show yael default at center

  "I close the coffin."

  show bg viewing with slow_dissolve

  Sari "Okay. Let's go."

  "Yael and I leave the viewing room."

  show bg foyer with slow_dissolve

  "We loiter in the foyer to discuss where we should investigate next."

  show sari shock #as side image"

  "Then I hear a strange sound."

  "Something that sounds like footsteps, coming from the morgue."

  show sari anxious #as side image"

  Sari "Did you hear that?"

  show yael anxious at center

  Yael "Hear what?"

  show sari default #as side image"

  Sari "There's something moving in the morgue."

  Yael "What? But —"

  "Despite Yael's protests, I march toward the morgue to check on what I've heard."

  jump lbl_076

label lbl_076:

  show bg morgue_open with slow_dissolve

  "We enter the morgue."

  if stopped_music == True:
    jump lbl_077
  if stopped_music == False:
    jump lbl_078

label lbl_077:

  "There's nothing here, and no one. Was I only imagining I heard something?"

  "Yael tugs on my arm."

  jump lbl_079

label lbl_078:

  "The sinister melody sounds farther away from here. This can't be the right room, then."

  "I'm about to leave to check elsewhere, when Yael tugs on my arm."

  jump lbl_079

label lbl_079:

  show yael shock at center

  Yael "Sari, it's open."

  Sari "Open?"

  show sari anxious #as side image"

  show yael anxious at center

  "I just then notice that the door to the refrigeration unit, where corpses are stored, is wide open when it shouldn't be."

  Sari "That's odd."

  "I move closer to the refrigeration unit."

  stop music fadeout 1.0

  if stopped_music == True:
    jump lbl_081
  if stopped_music == False:
    jump lbl_080

label lbl_080:

  "In my distracted state, I only faintly notice that the mysterious melody has faded away, leaving silence in its wake."

  jump lbl_081

label lbl_081:

  "The refrigeration unit is completely empty. Where's the corpse that should be here?"

  "Just this afternoon, when I arrived home from school, I applied makeup on her."

  "Did Papa transfer her somewhere else while I was taking my nap? Where?"

  "And why would Papa move her, in the first place?"

  play music suspense fadein 2.0

  show sari shock #as side image"

  show yael shock at center

  "Yael suddenly shrieks beside me, as I'm still silently pondering the possibilities."

  "I part my mouth to ask Yael what's the matter."

  show sari anxious #as side image"

  hide yael

  "But he's already barreling out the doorway, leaving me behind in the morgue."

  Sari "Yael! Wait!"

  show sari shock #as side image"

  "I'm about to follow him out, but a figure is standing in my way."

  show freya default at center with dissolve

  "The missing corpse!"

  "She's already wearing the wedding gown I was supposed to dress her in."

  "The unexpected sight knocks all the breath from my chest."

  show freya anxious at center

  Unknown "Are you going to run away, just like your friend did? His name's Yael, right?"

  "But I can only stare. Blankly."

  show sari anxious #as side image"

  show freya default at center

  "This girl, who's supposed to be dead, can not only walk, but can also talk?"

  "Is she actually alive? Or is she truly dead, but somehow zombified?"

  "Am I still asleep in the back office? Am I only dreaming?"

  show sari default #as side image"

  "What should I do? If I stay and chat with this corpse bride, I just might discover the answers to these burning questions."

  "But should I go check on Yael instead? The poor boy seemed close to having a heart attack, even at the tender age of nineteen."

  menu:
    "Stay and chat with the corpse bride.":
      jump lbl_083
    "Chase after Yael.":
      jump lbl_082

label lbl_082:

  show sari anxious #as side image"

  "Yeah, I should check on Yael. I'm the one who stopped him from leaving the funeral home."

  "I don't want Yael to be permanently traumatized by tonight's events."

  show sari mad #as side image"

  "I rearrange my face into a stern expression as I shut the door to the refrigeration unit."

  show bg morgue with slow_dissolve

  Sari "You. Whoever or whatever you are, you stay right here in the morgue."

  Sari "I gotta go check on Yael first, but I'll deal with you later."

  stop music fadeout 1.0

  show sari default #as side image"

  "I head for the exit before the corpse bride can protest."

  "I brush against her shoulder on my way out. Cold, but definitely real."

  hide freya

  play music mellow fadein 2.0

  show bg foyer with slow_dissolve

  show sari anxious #as side image"

  show yael shock at center with dissolve

  "Yael is huddled by the front door. Muttering to himself."

  Yael "The zombie is a dream. Just a dream. Only a dream."

  show sari default #as side image"

  "I crouch beside him."

  "I myself just ascertained that the corpse bride was real and definitely not a dream. So how can I comfort Yael?"

  menu:
    "Declare to Yael that I'll protect him.":
      jump lbl_084
    "Soothingly rub his arm.":
      jump lbl_085

label lbl_083:

  $yael_abandoned = True

  stop music fadeout 1.0

  "I have every intention of commencing a conversation with the corpse bride, but when I open my mouth, no words emerge."

  show sari anxious #as side image"

  "What in the world am I supposed to say? The mere sight of her has scrambled all my speech-related skills."

  "Regardless of my silence, however, the corpse bride looks pleased just to have a companion."

  play music bgm fadein 2.0

  show freya smile at center

  Unknown "Hello there! I'm delighted to receive visitors to my humble abode!"

  Unknown "If no one had come to play, I might have crawled back inside the wall. Wallowed alone in my disappointment."

  Unknown "It's too bad that your scaredy-cat friend has bolted! He was super cute!"

  show freya default at center

  Unknown "But never mind that now."

  jump lbl_105

label lbl_084:

  show sari anxious #as side image"

  "Right! I got Yael into this mess in the first place!"

  "I should let him know that he has nothing to fear! I'll keep him safe!"

  show sari default #as side image"

  Sari "Listen, Yael."

  "Yael meets my eyes, but he doesn't stop his fretful murmuring."

  show sari smile #as side image"

  Sari "You don't have to be scared, because I'm right here. I'll protect you from every monster out there."

  show yael anxious at center

  "Yael's clenched fists finally relax."

  Yael "You will?"

  Sari "I promise."

  jump lbl_086

label lbl_085:

  $ yael_romance += 1

  show sari anxious #as side image"

  "Yes, Yael is too caught up in his own thoughts to listen to any chivalrous declarations."

  "I'm sure that what he needs, more than anything, is the simple assurance that he's not alone."

  show sari default #as side image"

  "I pat his arm, in an effort to provide comfort."

  show yael blush at center

  "After about a minute of this, Yael gives a little cough. His face is red."

  Yael "Sari, it's okay. I'm okay. I'm ready now." 

  show sari anxious #as side image"

  Sari "You sure?"

  show yael anxious at center

  Yael "I don't have a choice, do I? I agreed to stay here tonight. I can't keep running away."

  jump lbl_086

label lbl_086:

  show sari default #as side image"

  "I straighten up from my crouching position, then hold out a hand to Yael."

  "Grasping my hand, he allows me to pull him to his feet."

  show yael smile at center

  "Standing with his own strength again, he manages a smile."

  Yael "Thanks, Sari. I rely on you way too much."

  Yael "I want to be someone you can also rely on. Someone you can trust."

  show sari smile #as side image"

  Sari "Hey, don't worry about it. What are friends for, eh?"

  stop music fadeout 1.0

  show yael sad at center

  "Yael purses his lips. He doesn't reply."

  show sari default #as side image"

  "I now bring up the crucial question, because someone has to do it."

  play music bgm fadein 2.0

  show yael default at center

  Sari "What do you think we should do about the corpse?"

  Sari "On the upside, she's already wearing the wedding dress for tomorrow's funeral. The one Papa told me to put on her."

  Sari "On the downside, we need to get her back inside the refrigeration unit, before Papa wakes up and sees her walking around."

  Sari "I dunno how exactly. But we've gotta do it somehow."

  Yael "I don't have any bright ideas either. But I do know one thing."

  show yael mad at center

  Yael "We can't let that zombie get too close! She might gobble up our brains!"

  Yael "Or rip out our hearts! Or something!"

  Yael "We should be properly armed! We need to protect ourselves!"

  show sari smile #as side image"

  show yael anxious at center

  "Even though the situation is dire, I have to beam at Yael's words."

  "I was craving an adventure with him tonight, and what can be better than this?"

  "The idea of squaring off against a hostile corpse, with Yael by my side and ready to fight, is thrilling indeed."

  Sari "Let's go to the back office! I bet we can find makeshift weapons to wield!"

  show bg office with slow_dissolve

  show sari shock #as side image"

  show yael default at center

  "In the office, I notice the tattered remains of paper, discarded on the floor."

  Sari "Oh! This was the sheet music you found earlier, wasn't it?"

  show sari default #as side image"

  Yael "Seems like it."

  Sari "Rats must have ravaged the paper while we were away. What a waste."

  show sari smile #as side image"

  Sari "But we can't dwell on that now! We should search for weapons!"

  "Yael and I scour the filing cabinets for promising objects."

  show sari default #as side image"

  Yael "Hey, Sari. What's this thing doing here?"

  "Yael shows me a violin. There's not a speck of dust on the flawlessly varnished wood."

  Yael "This doesn't belong to Mr. Roxas, does it?"

  show yael laugh at center

  Yael "I can't imagine your father owning a musical instrument! Not by choice!"

  "The idea is apparently so absurd to Yael that he chuckles despite himself."

  show sari anxious #as side image"

  show yael smile at center

  "I recognize this violin from photographs I chanced upon in the past."

  Sari "I think this violin was Mama's. Papa probably kept it for sentimental reasons, so we shouldn't touch it."

  show sari default #as side image"

  show yael default at center

  "Yael nods, then returns the instrument to its sleek black case."

  "Elsewhere in the filing cabinets, I eventually find the ebony walking cane of Lolo Rizaldo, my deceased paternal great-grandfather."

  "The cane's silver handle may be tarnished, but it's got a steady grip if I'm seeking to strike something."

  "Then, in Papa's toolbox under the desk, I unearth a hammer. Suitable for whacking enemies, I'd imagine."

  "Which weapon should I choose?"

  menu:
    "The walking cane.":
      jump lbl_087
    "The hammer.":
      jump lbl_088

label lbl_087:

  $weapon_cane = True

  show sari smile #as side image"

  "I grasp the cane's silver handle as if it's the hilt of a sword. By way of practice, I slash the air a few times."

  Sari "Not bad."

  show sari default #as side image"

  "I hold out the hammer to Yael."

  Sari "I'm using the cane as my weapon, so why don't you use this hammer to protect yourself?"

  jump lbl_089

label lbl_088:

  $weapon_hammer = True

  show sari smile #as side image"

  "I take a few practice swings with the hammer."

  Sari "Perfect."

  show sari default #as side image"

  "I hold out the walking cane to Yael."

  Sari "I'm using the hammer as my weapon, so why don't you use this cane to protect yourself?"

  jump lbl_089

label lbl_089:

  "Yael shakes his head. He gestures toward his guitar case, which is strapped around his body."

  show yael smile at center

  Yael "I'm okay. My music is all I need."

  Yael "Plus, I found a bottle of holy water in one of the drawers. It's in my pocket now."

  Sari "Suit yourself."

  show yael default at center

  "I return the weapon that Yael has rejected to the place where I found it."

  show sari smile #as side image"

  Sari "Let's go confront the corpse bride! We're ready now!"

  show yael anxious at center

  Yael "Sari, wait."

  Yael "I — I should probably tell you something. Before we go and risk our lives, I mean."

  show sari default #as side image"

  Sari "Tell me what?"

  show yael blush at center

  "Yael just stares at me. The color is intensifying on his cheeks."

  show sari anxious #as side image"

  Sari "You're not feeling sick, are you? Do you need to lie down for a bit?"

  "I lean closer, then place my palm on Yael's forehead."

  Yael "You don't need to do that!"

  Sari "I'm just checking your temperature. We can't battle any evil entities if you've got a fever, can we?"

  Yael "I'm fine! I'm not sick at all!"

  show sari default #as side image"

  Sari "No? Then what were you going to tell me?"

  Yael "Um. Never mind. We can talk about it later. Or never. Whichever."

  show yael default at center

  "I gaze curiously at him, but he turns away, ready to leave."

  "For once, I'm the one who has to follow his lead."

  show bg foyer with slow_dissolve

  show sari anxious #as side image"

  show yael anxious at center

  "When we reach the entrance to the morgue again, we stop and listen by the door."

  stop music fadeout 1.0

  Yael "Can you hear anything?"

  "Yael whispers these words, so I whisper in return."

  Sari "Nope. Can you?"

  "Yael shakes his head."

  play music suspense fadein 2.0

  "With careful fingers, he extracts his guitar from its case."

  Yael "Well, there's no point in delaying this any longer."

  Sari "Yeah, let's go. We gotta wrestle that corpse into the refrigeration unit somehow."

  show bg morgue with slow_dissolve

  show yael anxious at left with dissolve

  show freya default at right with dissolve

  "When we burst through the doorway, the corpse bride turns toward us."

  show freya smile at right

  "Her puffy face splits into a broad smile."

  Unknown "My dears, I've been awaiting your return."

  show sari mad #as side image"

  "As the corpse bride commences her slow approach toward us, I grip my weapon behind my back."

  "I'm ready to attack if I need to. If this corpse bride gives me any reason to."

  stop music fadeout 1.0

  show sari shock #as side image"

  show yael mad at left

  "But to my infinite surprise, Yael leaps in front of me."

  "He seems set on shielding me from any potential threats."

  play music paghahandog fadein 2.0

  show sari anxious #as side image"

  show yael groovy at left

  "Without further ado, Yael starts strumming his guitar."

  show freya shock at right

  "Taken aback, the corpse bride stops in her tracks."

  "She listens, as if captivated, to the chords of Yael's melody."

  show sari default #as side image"

  show freya anxious at right

  "I recognize these chords. I've heard this song often enough during Sunday Mass."

  "{i}Paghahandog{/i} by Hangad."

  "The first day I ever noticed Yael, he played this same song, among others."

  "We were both eleven then. We went to the same church."

  "It was quite the sight. Yael, tiny for his age, almost the same size as the guitar he held."

  "Small as he was, he seemed somehow bigger whenever he strummed his guitar."

  show sari blush #as side image"

  "The same still holds true today."

  "As Yael stands in front of me and sings, his shoulders appear broader. His arms look strong."

  Yael "{i}Ang himig Mo, ang awit ko. Lahat ng ito'y nagmula sa Iyo.{/i}"

  Yael "{i}Muling ihahandog sa 'Yo, buong puso kong inaalay sa 'Yo.{/i}"

  Yael "{i}O Diyos, O Panginoon, lahat ay biyayang aming inampon.{/i}"

  Yael "{i}Aming buhay at kakayahan, ito'y para lamang sa 'Yong kaluwalhatian.{/i}"

  stop music fadeout 1.0

  show sari default #as side image"

  show yael default at left

  show freya default at right

  "When Yael stops singing, there's absolute silence in the room."

  "Nobody moves."

  "Is that it? Did Yael's religious song incapacitate this unholy threat we're facing?"

  play music suspense fadein 2.0

  show sari anxious #as side image"

  show yael anxious at left

  show freya smile at right

  "But then the corpse bride breaks the spell."

  "Smiling once more, she takes a sizable step forward."

  show yael mad at left

  "Within a split-second, Yael has shifted into a fighting stance — knees slightly bent, feet firmly planted apart."

  "I'm about to make my move too, but Yael throws out his arm to prevent me from stepping forward."

  Yael "Sari, let me handle this."

  show yael anxious at left

  "I notice that Yael's arm, the one he's holding out to keep me safe behind him, is trembling."

  "This is Yael, after all. He's obviously scared out of his wits, even if he's trying not to show it."

  show sari default #as side image"

  "What should I do? Should I insist on fighting too, despite Yael's wishes to the contrary?"

  menu:
    "Fight by Yael's side.":
      jump lbl_090
    "Let him handle this.":
      jump lbl_091

label lbl_090:

  show sari mad #as side image"

  Sari "Yael, you don't need to act so tough! I can see that you're shaking!"

  Sari "We're a team, so we should fight together!"

  show sari anxious #as side image"

  "Yael begins to protest, but I sidestep his outstretched arm."

  "I brandish my chosen weapon toward the cadaver."

  Sari "Miss Corpse Bride! We don't know how you came back to life, but we can't risk you wandering around unattended!"

  Sari "As long as you climb back into the refrigeration unit where you belong, we won't harm you!"

  show freya laugh at right

  Unknown "Harm me? I'd unironically like to see you try!"

  Unknown "I'm already dead! I can't feel any pain!"

  Unknown "If you fight me, you'll always be worse off!"

  show sari mad #as side image"

  show freya smile at right

  Sari "This is my official warning, Miss Corpse Bride! If you take one step closer, I'll stop playing nice!"

  "The corpse bride's smile only widens, as if entertained."

  "Conspicuous as can be, she takes one more step toward me."

  Sari "You're asking for it!"

  show yael shock at left

  Yael "Sari! Wait!"

  "But I'm already sprinting forward, with my weapon held high."

  if weapon_cane == True:
    jump lbl_092
  if weapon_hammer == True:
    jump lbl_093

label lbl_091:

  $ yael_romance += 1

  show sari smile #as side image"

  show yael default at left

  Sari "All right, Yael. You can do this. I trust you."

  "Yael doesn't take his eyes off from the corpse bride, but I see him nod in response to my words."

  show sari anxious #as side image"

  "Yael swiftly repositions the guitar in his arms."

  show yael mad at left

  "Gripping the guitar's neck with his fists, he takes a wild swing toward the cadaver coming closer."

  show freya shock at right

  "She springs backward, only narrowly avoiding being bashed by the guitar's varnished wooden body."

  "Her expression is deeply offended now."

  Unknown "Oh, come on! What's wrong with you?"

  Yael "Stay back! Don't you {i}dare{/i} lay a hand on Sari!"

  show freya anxious at right

  Unknown "I'm not trying to lay a hand on anyone! I just —"

  Yael "Go back inside the refrigeration unit! You belong there! You should stay there!"

  "Yael keeps swiping his guitar, and the corpse bride keeps dodging his attacks."

  show yael anxious at left

  "Once Yael has her backed against the wall, his right hand darts toward his pocket to retrieve the holy water."

  show freya shock at right

  "He quickly unscrews the bottle's cap, then dumps the contents over the corpse bride's head."

  "A beat of silence."

  show freya mad at right

  "The cadaver's skin doesn't start shriveling up like in horror movies. But the expression on her face is turning uglier by the second."

  jump lbl_095

label lbl_092:

  show yael anxious at left

  "I slash the walking cane as if it's a sword."

  show freya shock at right

  "The corpse bride manages to dart away just in time."

  "However, the cane's tip snags on the hem of her wedding dress."

  jump lbl_094

label lbl_093:

  show yael anxious at left

  "I swing the hammer. Its silver claw makes a wide arc in the air."

  show freya shock at right

  "The tool strikes the floor, for the corpse bride has managed to dart away just in time."

  "However, the hammer catches on the hem of her wedding dress."

  jump lbl_094

label lbl_094:

  show sari anxious #as side image"

  "There's a tearing sound. The ripping of expensive cloth."

  "A single beat of silence."

  show freya mad at right

  "Then the corpse bride starts hollering."

  jump lbl_095

label lbl_095:

  "Once she starts hollering, she doesn't stop for a long time."

  show sari shock #as side image"

  show yael shock at left

  Unknown "ARE YOU TRYING TO RUIN MY WEDDING DRESS?! THIS IS A PRECIOUS HEIRLOOM!"

  Unknown "HOW DARE YOU!"

  Unknown "I'LL NEVER FORGIVE YOU!"

  show sari anxious #as side image"

  "She continues yelling about her dress and its history. It was passed on from her ancestors, apparently."

  "Her voice is so shrill that I'm amazed that Papa hasn't woken yet in his bedroom upstairs."

  "Yael seems stunned by the corpse bride's unbridled rage, so I tug on his hand to bring him back to earth."

  "At the moment of contact, he sucks in a startled breath."

  show yael anxious at left

  Sari "Yael, that move did a lot of damage, though not in the way we might have expected."

  Sari "Let's get out of here for now. Let's regroup and think of our next move."

  stop music fadeout 1.0

  "While the corpse bride is kneeling on the floor and examining every inch of her skirt, we begin to creep out of the morgue."

  "Yael lets me lead, this time. His hand is warm and rough in mine."

  hide freya

  play music bgm fadein 2.0

  show bg office with slow_dissolve

  show sari default #as side image"

  show yael default at center with dissolve

  "We're back in the office."

  "I take a swig of coffee from the thermos in my schoolbag."

  show yael anxious at center

  "Yael extracts a water bottle from his own schoolbag, but it's empty. He sighs."

  "Should I offer him my coffee? There's not much of it left."

  menu:
    "Give up what's left of my coffee.":
      jump lbl_096
    "He'll be fine.":
      jump lbl_097

label lbl_096:

  $ yael_romance += 1

  show sari smile #as side image"

  Sari "Want some of my coffee? It will keep you energized."

  show yael blush at center

  Yael "Uh. Okay. If you don't mind."

  "It's par for the course for Yael to be shy about sharing stuff. He always is with me."

  show sari blush #as side image"

  show yael default at center

  "But for some reason, I feel strangely apprehensive as I hold out my thermos to him."

  "When Yael tips back the thermos, I can't tear my eyes away."

  "I watch as his lips close over the mouth of the thermos. As his Adam's apple bobs with every gulp."

  "Why in the world am I watching his every move so intently?"

  show sari default #as side image"

  show yael smile at center

  "When he hands back the thermos, his fingers brush with mine."

  Yael "I do feel newly energized. Thanks."

  show sari anxious #as side image"

  show yael default at center

  "I'm thinking hard as I stash the thermos back inside my schoolbag."

  "Once I zip my bag closed, I look toward his face again."

  show sari blush #as side image"

  show yael blush at center

  "Yael is already staring at me, I realize."

  "We came back here for a reason, didn't we? To discuss our next move against the corpse bride. Or something of the sort."

  "But neither of us offers any suggestions, or outlines the steps of a plan."

  "We're simply staring into each other's eyes. Wordlessly."

  jump lbl_098

label lbl_097:

  show yael default at center

  "It's just one night. He'll be okay without the sip of a drink in the meantime."

  "We should focus on figuring out our next move against the corpse bride."

  Sari "Now what —"

  jump lbl_098

label lbl_098:

  stop music fadeout 1.0

  show sari shock #as side image"

  show yael shock at center

  "SMACK!"

  "Yael and I both jump."

  "It's the sound of palms hitting the door. Loud. Angry."

  "Someone seems to be trying to barge in, but failing."

  play music suspense fadein 2.0

  show sari anxious #as side image"

  show yael anxious at center

  "The doorknob twists. Slowly, at first."

  "Then the doorknob starts rattling hard. The person on the other side must be getting more and more furious."

  "It can only be the corpse bride, dying to get inside. She must want revenge for the damage to her wedding dress."

  show sari default #as side image"

  "I glance sideward at Yael."

  Sari "You locked the door when we came in? I know I didn't."

  show yael default at center

  Yael "Yeah. I just wanted to be safe."

  Sari "Good call."

  "As I reach for my weapon, which is resting on the desk, Yael stops me."

  Yael "Sari, don't you think we should try another strategy this time?"

  Sari "What strategy? I'm all ears."

  show yael anxious at center

  "Yael fingers the strap of his guitar case. He's chewing on his bottom lip."

  Yael "Weren't we too quick to pick a fight? Even if she's raving mad, maybe we should try talking her down."

  Yael "It's just this odd feeling I have."

  "Is Yael's instinct right? Should we adopt a pacifist stance, even if the corpse bride appears to be showing signs of aggression?"

  menu:
    "Try talking to the corpse bride.":
      jump lbl_099
    "Stay vigilant and prepare for a fight.":
      jump lbl_100

label lbl_099:

  show sari smile #as side image"

  Sari "Yeah, okay. Let's do it. Let's try talking to her."

  show sari default #as side image"

  show yael default at center

  "I walk toward the door now. The knob hasn't stopped rattling as we've been talking."

  "Yael touches my shoulder, so I glance backward at him."

  Sari "What is it?"

  Yael "Your weapon. You should leave it on the desk."

  Yael "We need to persuade her that we don't mean to harm her, don't we?"

  show sari anxious #as side image"

  "He does have a point, but I still hesitate."

  Sari "I'm not sure about this, Yael."

  show yael anxious at center

  Yael "I know it's a lot to ask of you."

  Yael "I mean, I was the one who insisted that we arm ourselves, in the first place."

  show yael default at center

  Yael "But how about this? Let me face her. Let me talk to her."

  Yael "If my instinct is wrong, then I'm the one who has to face the consequences."

  show sari default #as side image"

  "Just like before, when Yael stepped forward to shield me in the morgue, he's visibly trembling. But his eyes are determined."

  if yael_romance >= 3:
    jump lbl_101
  if yael_romance < 3:
    jump lbl_102

label lbl_100:

  "I shake my head at Yael."

  show sari smile #as side image"

  show yael default at center

  Sari "I'm proud of you, Yael. Really, I am."

  Sari "You're taking the lead. You're trying your best to make rational decisions despite this high-stress situation." 

  show sari default #as side image"

  Sari "But unfortunately, I have to disagree with your decision this time."

  Sari "We can't let our guard down around that corpse bride. Especially when she seems more hostile than ever."

  show yael anxious at center

  Yael "She's mad that we messed up her dress. She said as much, right? So maybe if we just apologize —"

  show sari anxious #as side image"

  Sari "{i}Apologize?{/i} What if, before either of us can open our mouths, she leaps forward and scratches out our eyes?"

  Sari "This is a risk we can't afford to take. I can't put my safety — or yours — at stake for something neither of us understands."

  show sari default #as side image"

  Sari "So you're either fighting with me, or I'm fighting alone. Your call."

  "By way of reply, Yael gets a good grip on the neck of his guitar, then nods at me."

  "He's trembling, but his eyes are determined."

  show sari anxious #as side image"

  "Armed with my weapon, I move toward the door, which hasn't stopped rattling as we've been talking."

  "I take a deep breath, then throw the door open."

  show yael anxious at left with dissolve

  show freya mad at right with dissolve

  "The corpse bride barges into the office."

  show yael mad at left

  "Yael is the first to strike. He swings his guitar toward her head."

  "But the corpse bride succeeds in dancing away from his attack."

  show sari mad #as side image"

  show yael anxious at left

  "As she hurtles away from Yael, I'm right there, ready to meet her."

  if weapon_hammer == True:
    jump lbl_103
  if weapon_cane == True:
    jump lbl_104

label lbl_101:

  show sari anxious #as side image"

  Sari "Are you sure? I dragged you into this mess tonight."

  Sari "You've had to push yourself this hard, all because of me."

  show sari default #as side image"

  show yael smile at center

  Yael "If you want me to blame you for this horror movie that's come to life, then I will."

  Yael "Before tonight, I could barely even look for more than five seconds at a corpse neatly laid out in a coffin."

  Yael "But tonight I got to face off against an actual zombie. Now that I've done that, I feel like I can face off against anything."

  Yael "So let me blame you for that, then. I'm blaming you for reminding me that I can be brave when I really need to be."

  show sari blush #as side image"

  "Yael is smiling so sweetly at me. I feel the sudden urge to hug him."

  "But before I can even reach out to him, he spins around and unlocks the door."

  show sari anxious #as side image"

  show yael anxious at left with dissolve

  show freya mad at right with dissolve

  "Yael backs away several steps as the corpse bride stalks into the office."

  "Yael holds up both arms, as if surrendering, and I follow suit."

  Yael "We don't want to fight. On the contrary, we wanted to have a civil conversation with you."

  Yael "Plus apologize for ruining your wedding dress, of course."

  "When the corpse bride glares daggers at him, Yael hastens to add a compliment."

  stop music fadeout 1.0

  show yael smile at left

  Yael "It's a very pretty dress. I'd be honored if I could someday marry a bride wearing a dress that beautiful."

  show sari shock #as side image"

  show freya smile at right

  "Oh, she actually looks pleased by this praise."

  play music bgm fadein 2.0

  "I suppose Yael's instinct was right. The corpse bride didn't originally intend to fight."

  show sari smile #as side image"

  Sari "Would you mind telling us your name, Miss? My name's Sari, and my friend here is named Yael."

  Unknown "Freya. That's what they called me when I was alive."

  Yael "A lovely name. Just as lovely as your dress."

  show sari default #as side image"

  show yael default at left

  "Smiling from ear to ear now, the corpse called Freya flounces toward the back of the office and sits on the chair behind the desk."

  "She gestures for us to take our seats, looking for all the world like she's the new queen of this shabby office, this modest funeral home."

  "Yael offers the small sofa to me, the one where I was napping earlier, then sinks down on a free chair."

  show freya default at right

  Freya "You wanted to have a civil conversation, right? First of all, let me say my piece."

  Sari "Go ahead."

  Freya "This is my first day — or my first night, rather — of being undead."

  Freya "So I suppose I have no real benchmark by which to measure the undead experience."

  show freya sad at right

  Freya "Even so, this night has gone nothing like expected."

  Freya "I expected, or perhaps hoped, that those running a funeral home would be as excited as I am to learn there is life after death."

  Freya "Or, in the alternative, I hoped that you two would be reasonably accustomed to such a phenomenon."

  Sari "I've never seen or heard of anything like this happening, for the record."

  Yael "Me neither. And unlike Sari, who's always lived here, I've only been employed as a mortician's assistant for six months."

  show freya anxious at right

  Freya "Even if this has never happened to either of you before, does it mean it's automatically bad? Worthy of an unprovoked attack?"

  show sari anxious #as side image"

  show yael anxious at left

  "Neither Yael nor I know how to reply."

  show freya default at right

  Freya "I saw the two of you watching a horror film earlier."

  Freya "I thought it would be a fun prank to pretend to be one of those demonic entities in those types of movies."

  show sari default #as side image"

  show yael default at left

  show freya smile at right

  Freya "But I can tell you now. I'm not some evil entity summoned from hell."

  Freya "At least, I don't {i}feel{/i} like I'm evil. That must count for something, right?"

  "Yael and I glance at each other. When he nods, I speak first."

  show sari smile #as side image"

  Sari "Yeah, that's the crucial thing, I guess."

  Sari "As long as you're not planning to hurt us, then we don't need to resort to violence either."

  show sari default #as side image"

  show freya default at right

  Sari "I was just concerned. I wanted to get you back inside the refrigeration unit somehow, before Papa can spot you."

  show yael anxious at left

  Yael "As for me, I was scared that you were going to attack us, then chomp on our brains."

  show freya laugh at right

  "Freya giggles at Yael's words."

  Freya "Chomp on your brains? Since dying, I've felt no urge whatsoever to eat or drink anything!"

  Freya "And on the off-chance that my taste buds still function, your brains would be the last thing I'd devour! They'd surely be bitter!"

  show yael blush at left

  show freya smile at right

  "Yael coughs, embarrassed now."

  Yael "I just see it in movies and in games. Zombies are always chasing after human brains."

  show yael anxious at left

  Freya "I'm not even sure I'm a zombie, in the first place. But if I was a ghost instead, would you fear me any less?"

  "Yael squirms on his seat. He doesn't answer her question."

  Freya "You're a big scaredy-cat, aren't you? How adorable."

  show sari anxious #as side image"

  show freya default at right

  "When Yael remains silent, I jump in to defend him."

  show yael blush at left

  Sari "Fear is just an innate emotion, meant to keep humans safe from external threats."

  Sari "If we sense danger, it's only natural to run."

  Sari "Despite this flight instinct, Yael stayed. He {i}chose{/i} to fight by my side."

  Sari "I don't think it's accurate to call him a scaredy-cat at all."

  show sari default #as side image"

  show yael smile at left

  Yael "Thanks for sticking up for me, Sari. But it's okay."

  Yael "I can admit that I've got way too many irrational phobias."

  show yael anxious at left

  Yael "Ghosts. Zombies. Corpses. All that horror-movie stuff."

  show freya smile at right

  "Freya leans over the desk. Amusement flickers over her dark eyes as she regards Yael."

  Freya "So riddle me this. If you're frightened of corpses, why are you working in a {i}funeral home,{/i} of all possible places?"

  Freya "I candidly shared my feelings about tonight's events, so be honest with me now."

  stop music fadeout 1.0

  show sari anxious #as side image"

  show yael shock at left

  "Yael seems stricken by this sudden interrogation."

  "I'm just about to tell Freya to lay off him, when Yael speaks, all in a rush."

  play music mellow fadein 2.0

  show sari default #as side image"

  show yael default at left

  Yael "When Mr. Roxas posted about an opening to be his assistant, I applied right away." 

  Yael "A bunch of Sari's Mortuary Science blockmates applied too, but I convinced Mr. Roxas to hire me."

  Yael "I told him that I'd work harder than anyone."

  Freya "And why did you do that?"

  Yael "I wanted to be here for one simple reason. Not for the coffins. Or the corpses. Or the crying families."

  show yael blush at left

  Yael "I just wanted to be closer to Sari, because —"

  Yael "Because I. . . ."

  Freya "Go on."

  show sari blush #as side image"

  Yael "Because I'm in love with Sari."

  Yael "I mean, I've {i}always{/i} had a massive crush on her, ever since the first day I saw her during Sunday Mass."

  Yael "That's why I joined the church choir."

  Yael "Even though I had stage fright, and even though I despised the scratchy dresses my parents forced me to wear."

  Yael "I just wanted Sari to notice me. So I got in front of everyone and sang and played my guitar."

  "Yael turns toward me. His strawberry-hued face is now staring at my own."

  Yael "I — I love you, Sari."

  "I part my mouth, ready to respond, when Freya claps loudly."

  show sari shock #as side image"

  show yael shock at left

  "Startled, Yael and I both turn toward her."

  show freya laugh at right

  Freya "Well, then. Before the two of you start kissing madly, can I leave first?"

  Freya "My superior matchmaking services were more than enough to win me my freedom, don't you think?"

  hide yael

  hide freya

  show bg darkness with slow_dissolve

  show sari default #as side image"

  "So Yael and I say our goodbyes to Freya."

  "Sure, our brief brush with this walking and talking cadaver was surreal, but we are undeniably thankful to her."

  show bg foyer_open with slow_dissolve

  show sari smile #as side image"

  show yael smile at center with dissolve

  "In the foyer, we both stand by the entrance and wave at Freya."

  "She departs toward her uncertain future, and we wish her the best."

  show yael blush at center

  "Yael reaches for my hand. With his face aflame, he asks me if it's okay to hold me like this."

  Sari "It's okay. It's {i}more{/i} than okay."

  "Yael still looks apprehensive."

  show sari blush #as side image"

  show yael shock at center

  "So to drive in my point, I smooch his forehead."

  "At the point of contact, Yael makes a strangled noise in the back of his throat."

  Sari "In case that wasn't obvious enough, I do feel the same way about you."

  Yael "Eh? You do?"

  show sari smile #as side image"

  show yael blush at center

  Sari "Sure, I do. You were very heroic tonight, you know? How can I resist?"

  Yael "Then. . . ."

  Yael "Can the hero kiss his heroine too?"

  scene cg ending05_pic with slow_dissolve

  "I stoop over to move my face closer to Yael's."

  "He plants a sweet kiss on my cheek."

  scene cg ending05 with slow_dissolve
  $ persistent.ending_seen_05 = True
  $ ending_theme = "best"
  pause
  jump lbl_credits

  return

label lbl_102:

  show sari anxious #as side image"

  Sari "You're actually scared to death, aren't you?"

  show yael shock at center

  "Yael's eyes widen, and he answers too quickly."

  Yael "No! I'm not afraid at all!" 

  show sari default #as side image"

  show yael anxious at center

  "I stare him down until he sheepishly admits the truth."

  Yael "Okay, okay. I feel like I might faint at any moment. But {i}someone{/i} has to do it."

  show sari smile #as side image"

  Sari "Let me do it, then."

  Sari "If one of us is going to try talking our way out of a fight, then it's better if that person can stay calm, right?"

  Yael "Right."

  Sari "So it's settled."

  show sari anxious #as side image"

  "Leaving my weapon on the desk, I walk toward the door and open it."

  show yael anxious at left with dissolve

  show freya mad at right with dissolve

  "The corpse bride rushes through the doorway, but skids to a stop once she realizes that I'm standing right there."

  show sari mad #as side image"

  "With both fists parked on my hips, I try to mimic the authoritative tone that Papa has mastered."

  Sari "Miss Corpse Bride, we don't want to fight anymore. As you can see, we've let go of our weapons."

  Sari "All we want now is a civil conversation. This way, we can air our grievances without resorting to violence."

  stop music fadeout 1.0

  show sari anxious #as side image"

  show freya anxious at right

  "The corpse bride squints suspiciously in response to my words, but she doesn't protest."

  "She doesn't make a move against us either."

  play music bgm fadein 2.0

  "I suppose Yael's instinct about her was right. She wasn't planning on fighting."

  show sari default #as side image"

  "I gesture toward the chairs now."

  Sari "Why don't we all sit down and talk?"

  show yael default at left

  show freya default at right

  "I opt for the chair behind the desk. Once we're all seated, I clear my throat, then begin to speak."

  Sari "First of all, my name's Sari, and my friend here is named Yael."

  Sari "Would you mind telling us your name?"

  Unknown "The name's Freya. That's what they called me when I was alive."

  Sari "Nice to meet you, Freya."

  "I stick out my hand to shake hers, but she only stares at my proffered palm with stony silence until I withdraw it."

  Sari "No need for small talk, then? You want to get down to business right away? I can respect that."

  Sari "So let me ask you a question —"

  show yael anxious at left

  show freya mad at right

  Freya "Hang on a freaking minute. You're not even going to apologize?"

  Freya "This wedding dress is the one and only thing I have left, and you nearly ruined it with your recklessness!"

  show sari anxious #as side image"

  "I make a big show of looking the wedding dress up and down."

  Sari "What are you talking about? The dress is totally intact! Spick and span!"

  Sari "Let's make a deal. Yael and I won't say sorry for the nonexistent damage to your outfit."

  Sari "In return, you won't have to apologize for scaring Yael half to death with your horror-movie antics."

  show freya anxious at right

  "Freya releases a frustrated sigh."

  Freya "Whatever. So what did you want to talk about?"

  show sari default #as side image"

  show yael default at left

  Sari "We need you to recount everything you remember from today. I figure that's the best way to figure out how to undo this mess."

  Sari "Something must have happened in the time between the embalming process and our first sighting of you standing in the morgue."

  Sari "You certainly {i}seemed{/i} dead when I was dabbing makeup on your face, after I got home from school."

  show freya shock at right

  Freya "Wait, you're the one who did my makeup?"

  Sari "Guilty as charged."

  show freya default at right

  Freya "What a thankless profession. Putting makeup on clients who literally can't convey their gratitude."

  Freya "On behalf of the rest of your lifeless clientele, thank you for your service."

  Sari "No problem."

  Sari "So? Can you recall the events from this afternoon? Or from tonight?"

  Freya "Yeah, the first thing I remember, as I awoke in that charming little fridge, is the sound of a guitar. Probably that one."

  "Freya points toward the guitar case slung around Yael's body."

  show sari anxious #as side image"

  show yael shock at left

  Yael "Eh? You can hear my guitar all the way over there in the morgue?"

  Freya "I could hear your melody as clearly as if you were screaming every note into my ear."

  "Yael parts his mouth to reply to this, but I raise my hand to silence him."

  show yael default at left

  "My mind is elsewhere. It's whirring with the beginnings of an epiphany."

  Sari "I knew it. So I'd guessed it right from the start, huh?"

  show sari smile #as side image"

  show yael anxious at left

  "I glance up from the desk and beam at Yael. But he only stares back, nonplussed."

  Sari "Don't you get it yet, Yael?"

  Yael "No, I have no idea what you're saying or thinking. You'll have to enlighten me."

  Sari "That song! From the sheet music you found lying around here! It's haunted, just as I suspected!"

  Sari "We don't know the mechanics of that melody, but it somehow succeeded in resurrecting a corpse close enough to hear it!"

  show sari default #as side image"

  show yael default at left

  show freya anxious at right

  Sari "It's too bad that the sheet music is gone. Playing that song again might be the answer to our problem."

  Yael "I don't need the sheet music. I still remember all the notes."

  show sari smile #as side image"

  Sari "Of course you do! Yael the musical prodigy has come to rescue us all!"

  show yael blush at left

  "I reach over the desk to ruffle Yael's hair."

  "Yael's cheeks are distinctly pink as he extracts his guitar from its case."

  show yael anxious at left

  Yael "You really want me to play that melody again? What if we end up reviving even more cadavers?"

  Sari "Whatever happens, happens. We'll deal with it together."

  show sari default #as side image"

  Sari "But I believe that we have to try this. Just once."

  Sari "I want to verify with my own eyes whether the song will have any effects on nearby corpses like Freya."

  show freya mad at right

  Freya "Hey! What about what I want?"

  Freya "Am I supposed to sit pretty here and serve as your willing guinea pig?"

  stop music fadeout 1.0

  Freya "If the two of you are planning to callously experiment on me, I'm getting out of here!"

  "Freya jumps to her feet and hurries toward the door."

  play music aria_guitar_reverse fadein 2.0

  show yael groovy at left

  "However, Yael just then commences plucking on the strings of his guitar."

  "All it takes is a few notes."

  hide freya

  show sari shock #as side image"

  show yael shock at center with dissolve

  "Then Freya crashes spectacularly to the floor. Stiff as a board."

  "Both Yael and I wince at her fleshy impact on the linoleum."

  show sari anxious #as side image"

  "As I crouch by Freya's body to check on her, I instruct Yael to continue playing the melody, just to be absolutely certain."

  show yael groovy at center

  "I'm checking on Freya's vital signs. Watching her eyelids for any telltale flickers."

  "I then notice something. But it's not something about Freya."

  show sari default #as side image"

  "I glance up at Yael."

  Sari "That song you're playing, it sounds nothing like the one you were playing earlier."

  Yael "That's because I'm playing the notes backward. The melody has an intriguing palindromic structure, doesn't it?"

  Sari "Palindromic?"

  show yael default at center

  "Yael shrugs."

  Yael "It just made sense to me. If playing the melody as written wakes the dead, then playing its reverse should lull them back to sleep."

  stop music fadeout 1.0

  "Yael's hand halts over the guitar strings now."

  show yael anxious at center

  Yael "So? Is she dead again?"

  show sari smile #as side image"

  Sari "Yep. Definitely dead."

  Sari "Or deader than she was a moment ago, at least."

  hide yael

  play music mellow fadein 2.0

  show bg darkness with slow_dissolve

  show sari default #as side image"

  "And so concludes our brief brush with the corpse bride named Freya."

  "Working in the funeral home as we do, Yael and I already understand that cadavers are much heavier than they look." 

  "But Freya takes this challenge to another level entirely. The burden of her weight, even split between Yael and me, seems to spite us."

  show bg morgue with slow_dissolve
  
  show sari anxious #as side image"

  show yael anxious at center with dissolve

  "Yael and I are both sweating like pigs as we shut the door to the refrigeration unit."

  "Freya is finally back inside, where she belongs."

  Sari "Let's spare Papa from hearing about our misadventure. For a senior citizen like him, it won't take much for him to keel over."

  Yael "Agreed. Let's keep this a secret between us."

  show sari blush #as side image"

  show yael blush at center

  "Yael's eyes meet mine."

  "For a moment I wonder whether we will seal our secret with something momentous to mark it."

  "A kiss, perhaps? A touch of hands?"

  "Or shall we hook our pinkies as a promise never to breathe a word of this to anyone else?"

  show sari default #as side image"

  show yael anxious at center

  "But Yael breaks eye contact, then turns toward the door."

  scene cg ending06 with slow_dissolve
  $ persistent.ending_seen_06 = True
  $ ending_theme = "good"
  pause
  jump lbl_credits

  return

label lbl_103:

  show freya shock at right

  "The hammer I'm wielding smashes against the corpse bride's abdomen."

  show sari anxious #as side image"

  "I hear the dull crunching of bone, but the gasp she gives is more exasperated than agonized."

  "She can't feel any pain at all, right?"

  show sari mad #as side image"

  show freya mad at right

  "The impact of my first blow has thrown her against the wall. While she's cornered, I raise my hammer again for the second hit."

  "But even as the hammer connects with her skull with a mighty {i}crack,{/i} she manages to shove me backward."

  "The force makes me crash against the desk, then topple painfully on my backside."

  show sari shock #as side image"

  show yael shock at left

  "Before I can get back up, the corpse bride pounces on top of me." 

  "I struggle to heave her off my body, but she pins me down firmly by my wrists."

  show sari anxious #as side image"

  show yael mad at left

  Yael "No! Don't you {i}dare{/i} hurt Sari!"

  "Yael brings down the guitar over her head, so swiftly that the varnished wood is a blur above me."

  show freya shock at right

  "There's a sickening crunch. The sound of splintering wood."

  "The corpse bride rolls away from my body."

  hide freya

  "She darts toward a corner of the office, with both hands massaging her now misshapen head."

  show yael shock at center with dissolve

  show sari default #as side image"

  Yael "Sari! Can you hear me? Are you okay?"

  Sari "Yeah. I might have a few bruises, but otherwise, I'm totally fine."

  stop music fadeout 1.0

  show yael anxious at center

  "I sit up, then Yael helps me up to my feet again."

  "I now assess the mess all around me."

  play music mellow fadein 2.0

  "Toppled paperwork. Sheets strewn all over the office floor."

  "My hammer, by the far wall now. I must have kicked it away during the struggle on the floor."

  "Splinters of wood. A decimated instrument."

  show sari anxious #as side image"

  Sari "Yael, your guitar. . . ."

  show yael sad at center

  Yael "Sari, as long as you're okay, nothing else matters."

  Yael "It's fine. It's all going to be fine."

  "With cautious fingers, I lift the crushed guitar by its still intact neck."

  show sari shock #as side image"

  "The guitar's soundboard detaches, dropping to the floor."

  show yael cry at center

  "And all of a sudden, Yael is sobbing."

  show sari sad #as side image"

  "And who can blame him? Tonight was a lot for him. Way too much for him to survive unscathed."

  show yael cry at left with dissolve

  show freya anxious at right with dissolve

  "As I pull Yael into a hug, rubbing his back to comfort him as best as I can, the corpse bride clears her throat."

  "Looks like she somehow squeezed her bashed-in head into an acceptable shape."

  show sari mad #as side image"

  "I glare at her over Yael's shuddering shoulders."

  Sari "What? What do you want now?"

  Sari "Can't you give us a minute before we resume wrestling on the floor again?"

  Sari "This guitar meant everything to my friend! He's grieving! Let him!"

  show freya sad at right

  Unknown "Look, I never wanted to fight, in the first place. I only wanted to play some games."

  "When I only snort in disbelief, the corpse bride shrugs at me."

  show sari anxious #as side image"

  Unknown "If you don't want to believe me, then don't. I don't care."

  Unknown "All I want is for you to allow me to walk out of here in peace."

  Unknown "No more fighting. I just want my freedom now."

  Unknown "Earlier tonight, I wanted friendship too, but I can see that I went about it the wrong way."

  Unknown "For what it's worth, I apologize about this. All of this."

  show sari sad #as side image"

  show freya anxious at right

  "The corpse bride eyes the ruined guitar, then Yael's snivelling form, so small in my arms."

  Unknown "I'll go, then. I don't expect we'll ever see each other again."

  hide freya

  "I don't say a word as the corpse bride disappears beyond the doorway."

  scene cg ending07 with slow_dissolve
  $ persistent.ending_seen_07 = True
  $ ending_theme = "bad"
  pause
  jump lbl_credits

  return

label lbl_104:

  "I jab the walking cane against the corpse bride's abdomen."

  show sari shock #as side image"

  show yael shock at left

  show freya shock at right

  "However, the cane snaps in half at the point of contact."

  "The cane's broken portion does tear through the fabric of the wedding dress."

  show sari anxious #as side image"

  show yael anxious at left

  show freya mad at right

  "This, of course, enrages the corpse bride even more."

  "Before she can bear down her full fury on me, Yael dives in between us."

  "He holds her off with his guitar, then twists his head around to yell at me."

  show sari shock #as side image"

  show yael mad at left

  Yael "Run, Sari! Just get out of here!"

  Sari "But —"

  Yael "I'll catch up to you soon, I swear! Just go!"

  hide yael

  hide freya

  show bg foyer with slow_dissolve

  show sari anxious #as side image"

  "So I run."

  "Will Yael truly be okay alone? Should I go back and fight by his side again?"

  "But recalling the determination on his face deters me from returning."

  show bg morgue with slow_dissolve

  "Yes, the morgue is the best place to hide as I wait for Yael."

  show bg morgue_open with slow_dissolve

  "I yank open the door to the refrigeration unit."

  "I clamber inside the dark hole in the wall, then pull the door closed behind me."

  hide sari

  show bg darkness with slow_dissolve

  "Sure, it's cold as death inside here, but I should be okay, as long as Yael doesn't take too long to join me."

  "I blow warm breath against my cupped hands, then rub my palms together."

  "I realize that I'm still holding the top half of the walking cane, the one with the tarnished silver handle."

  "Where the cane has severed from the rest of its body, the tip is pointed. But is it sharp enough to serve as a useful weapon?"

  "I test the cane's tip against my thumb. I wince as it draws a droplet of blood."

  "As I stick my thumb into my mouth and taste that uniquely metallic flavor, the reality of what I'm doing jolts me."

  "What the heck am I doing here? Why did I run? Why did I hide?"

  "Of course I need to fight by Yael's side! He may be bleeding profusely by now, his face draining of color due to blood loss!"

  "The corpse bride is already dead as a doornail, so she feels no pain! No exhaustion! Nothing can stop her from prevailing!"

  "There's no way that Yael can ever win against her!"

  "I'm about to shove open the door to the refrigeration unit so that I can rejoin the battle in the office, if it's still in progress."

  "But a force from the other side is already pulling the door open."

  "In the split-second before the bright light of the morgue floods my world again, I decide to attack. Use the element of surprise."

  show bg morgue_open with slow_dissolve

  show sari mad #as side image"

  "I lunge forward with all my strength, with my sharp-tipped cane held at the ready."

  "Spearing my cane through the flesh of my enemy, I tumble to the floor of the morgue."

  "My knees are wedged against the chest of the body beneath me, pinning it down."

  show sari shock #as side image"

  "But it's not the body that I expected. Not the body I intended to maim."

  "This is wrong. I was wrong. All wrong."

  show yael cry at center with dissolve

  "No one other than Yael is howling underneath my weight."

  "The sharp half of my cane is now sticking straight through the palm of his right hand."

  show sari sad #as side image"

  Sari "Oh my God. Yael. I'm so sorry, Yael."

  Sari "I didn't mean to. I promise I never meant to hurt you."

  "Easing my weight off his body, I wrench the cane from where it's rooted deep inside his hand."

  show sari shock #as side image"

  "Blood blooms, fresh and crimson, from the gaping wound in Yael's palm, then pours freely over his clothes."

  "I can only stand over Yael."

  "I can only stare down in mute horror at the worst mistake I've ever made."

  scene cg ending08 with slow_dissolve
  $ persistent.ending_seen_08 = True
  $ ending_theme = "worst"
  pause
  jump lbl_credits

  return

label lbl_105:

  Unknown "You want to know something odd? Something they never tell you when you're alive?"

  show freya shock at center

  Unknown "When you die, you don't automatically acquire teleportation powers!"

  Unknown "You can't appear and disappear like ghosts do in movies! What an outrage!"

  show freya default at center

  Unknown "Instead, you have to lumber around, as fleshy and unwieldy as ever. And the {i}rigor mortis{/i} certainly doesn't help."

  Unknown "So picture this, if you will. Me, donning the glamorous outfit that I begged my mother to bury me in."

  Unknown "I was meant to wear this dress someday, you know?"

  Unknown "My mother inherited it from my grandmother, who in turn inherited it from my great-grandmother."

  Unknown "If this wedding dress was my birthright, shouldn't it be my {i}death-right{/i} too? It's only fair!"

  show freya smile at center

  Unknown "But let me get back to my thrilling tale, for thrilling it is."

  Unknown "So imagine me, fancy as can be in my wedding dress, sneaking toward the room where the two of you are watching a movie."

  Unknown "I'm slamming the door to scare you! Then sprinting away before you can catch me!"

  Unknown "I'm leaping straight out the window! Racing around the building's perimeter to reach the front door!"

  Unknown "Once I arrive at the front door, I'm knocking! Knocking loudly!"

  Unknown "Knocking until I hear your voices on the other side! Then the sound of locks popping open!"

  Unknown "I'm diving headfirst into a thicket of bushes! Stifling my giggles as you gaze into the nothingness beyond the doorway!"

  Unknown "Then, as you and your cute friend start to bicker, I'm creeping away, back to the open window!"

  show freya default at center

  Unknown "Okay, I'll admit it. The climb back inside the funeral home was much more difficult, for some reason."

  Unknown "But if I can battle the greedy claws of blood cancer for years and years, then I can definitely scale a wall."

  show freya smile at center

  Unknown "So here I am now."

  Unknown "And here you are, the lucky participant in my first game as a. . . ."

  show freya anxious at center

  Unknown "Wait, what am I exactly?"

  Unknown "A zombie? Or {i}aswang?{/i}"

  show freya smile at center

  Unknown "Well, whatever it is that I am, what I really want to be is your friend."

  Unknown "That's why I went through all this trouble to prank you and entertain you tonight."

  Unknown "I've been bedridden for far too long! If I couldn't maximize my life, then I can maximize my death, right?"

  Unknown "And I figure that a blossoming friendship is the perfect place to start!"

  Unknown "My name's Freya. And your name's Sari, I know."

  Freya "I heard your friend Yael calling you by that name earlier."

  "The corpse bride finally falls quiet, an expectant expression on her face."

  "I struggle to think of what to say."

  "As I bite my bottom lip and contemplate potential topics of conversation, I shut the door to the refrigeration unit."

  show bg morgue with slow_dissolve

  show sari default #as side image"

  "What should I say to Freya the corpse bride?"

  menu:
    "Ask Freya about the mysterious music.":
      jump lbl_106
    "Ask her about the rat on her shoulder.":
      jump lbl_107

label lbl_106:

  show freya default at center

  "Right, I should prioritize figuring out where that sinister music came from."

  Sari "Did you hear that mysterious melody? I've been searching the funeral home for its source."

  Freya "I did hear the music too. But I have no clue regarding its source, I'm afraid."

  "Freya addresses the rat perched on her shoulder."

  show freya smile at center

  Freya "How about you, Keso? Do you know where that music came from?"

  "Keso the rat squeaks in response. Freya endeavors to translate for me."

  Freya "Keso said he doesn't have an idea either."

  Freya "Keso's been following me around since I woke up earlier tonight, so I decided to keep him as a pet."

  Freya "Keso, say hello to Sari."

  "Keso squeaks again."

  jump lbl_108

label lbl_107:

  $ freya_romance += 1

  show freya default at center

  "I guess I'll let my curiosity prevail this time. I {i}have{/i} to ask Freya about that rat."

  Sari "Why do you have a rat perched on your shoulder? Is it your pet?"

  show freya smile at center

  "Freya brightens. She fondly pats the tiny head of the rodent."

  Freya "Yes, this little sweetheart's been following me around since I woke up earlier tonight, so I've decided to tame him."

  Freya "His name's Keso. Keso, say hello to the pretty girl. She's Sari, our new friend."

  "Keso the rat squeaks. It's a chipper sound, so I wave in return."

  jump lbl_108

label lbl_108:

  show sari smile #as side image"

  Sari "Hey there, Keso!"

  "Against all odds, I seem to have befriended not only a walking and talking cadaver, but also her pet rat."

  "This night is downright surreal."

  show sari default #as side image"

  show freya default at center

  Freya "Can I ask you a question too?"

  Sari "Sure. What is it?"

  Freya "Do you happen to have a mirror that I can borrow?"

  Freya "I caught a hazy glimpse of myself when I was climbing through the window, but I'd prefer to access a clearer reflection."

  Freya "I want to know what the undead version of myself looks like."

  Sari "There should be a mirror in the back office. Let's go get it."

  if yael_abandoned == True:
    jump lbl_109
  if yael_abandoned == False:
    jump lbl_113

label lbl_109:

  show bg foyer with slow_dissolve

  show sari shock #as side image"

  "As we pass by the foyer, I gasp as I just then remember something."

  show freya anxious at center

  Freya "What's the matter, Sari?"

  Sari "I totally forgot about Yael!"

  Sari "I gotta check on him! He must be totally freaking out!"

  show sari anxious #as side image"

  "I dig my hand into my pocket for my phone, but it's not here."

  "As I'm trying to recall when I last used my phone, Freya approaches the front door."

  show sari default #as side image"

  show freya default at center

  "Freya returns to my side with a page seemingly torn from a notebook."

  Freya "I found this message by the doorjamb. It must be for you."

  "In his neat handwriting, Yael apologizes for leaving, then implores me to call him right away if I need him for something. Anything."

  "As I secure the three locks on the front door, Freya reads the note that Yael left for me."

  show freya sad at center

  "She frowns."

  Freya "It's a real pity that he ran away. He would have made for an amusing yet adorable playmate."

  show freya default at center

  "What's that supposed to mean? How should I respond to Freya's description of Yael?"

  menu:
    "Ask Freya if she wanted to scare Yael some more.":
      jump lbl_110
    "Ask her if Yael is her type.":
      jump lbl_111
    "Say nothing.":
      jump lbl_112

label lbl_110:

  show sari mad #as side image"

  Sari "Let me take a wild guess."

  Sari "You wanted to prank Yael with some more of your creepy tricks, didn't you?"

  show sari default #as side image"

  show freya laugh at center

  "Freya bursts out laughing."

  Freya "Can you blame me? His reactions to everything were endlessly entertaining!"

  show freya smile at center

  Sari "Do me a favor. If you ever meet the guy again, go easy on him. You'll give him a heart attack if you overdo it."

  Freya "Fine. Even for a cheery corpse like myself, death isn't exactly a dream come true."

  Freya "I'd be the last person to ever subject someone else to death before their time. So don't worry about that."

  show freya default at center

  "I nod approvingly, then we move on."

  jump lbl_113

label lbl_111:

  $ freya_romance += 1

  Sari "Let me guess. Yael's your type, isn't he?"

  show freya shock at center

  Freya "My type?"

  Sari "You keep calling him cute. Or adorable. You're obviously interested in him!"

  show freya smile at center

  Freya "I do find his reactions interesting, yes. But I doubt that it's the type of interest you're thinking about."

  show freya blush at center

  Freya "To be perfectly blunt, I've never felt romantic interest toward a boy."

  Freya "But for girls, yes. All the time."

  show sari blush #as side image"

  show freya default at center

  Sari "Oh. I see. Okay."

  "My face feels suddenly warm, as my misjudgment sinks in."

  show sari default #as side image"

  Sari "Let's move on."

  jump lbl_113

label lbl_112:

  "Yeah, there's no point in continuing a conversation purely for the sake of it. We should just move on."

  jump lbl_113

label lbl_113:

  show bg office with slow_dissolve

  "Freya and I enter the back office."

  "She flips through a brochure for Roxas & Roxas Funeraria while I putter through the filing cabinets."

  show sari anxious #as side image"

  Sari "I'm sure I saw a mirror here once."

  Freya "How about in the bathroom? Surely there's a mirror there?"

  show sari default #as side image"

  Sari "Papa took out the mirror in the guest bathroom a few years ago."

  Sari "Clients kept complaining about seeing disembodied faces reflected back while they were washing their hands and stuff."

  Sari "Papa tells me privately that these are cases of pareidolia. You know, the tendency to see patterns where there aren't any."

  Sari "But that hasn't stopped me from hoping for a paranormal occurrence to happen in the funeral home."

  Sari "Ghosts, especially. I've always wished that I could see ghosts."

  Freya "You've lost someone important to you, haven't you?"

  show sari sad #as side image"

  Sari "My Mama died giving birth to me, so I never knew her."

  Sari "Does that count as losing someone?"

  show sari default #as side image"

  Freya "Of course it does. Being robbed of a mother's love since birth? It's difficult to imagine a loss more profound than that."

  Sari "Have you ever lost anyone important to you, then?"

  Freya "No one within my immediate family, no. No one close."

  show freya sad at center

  Freya "I was, however, diagnosed with leukemia as a small child, so there was a lot of grief around me, from everyone I knew."

  Freya "There was grief in me too."

  Freya "For all the things I dreamed of having and all the experiences I yearned to live through, but never would."

  show sari sad #as side image"

  show freya default at center

  "I halt in my search to turn toward her."

  Sari "That must have sucked big-time. I'm so sorry to hear that."

  "But she brushes off these condolences with a wave of her hand."

  show sari default #as side image"

  show freya smile at center

  Freya "I can honestly say, with every fiber of my being, that I'm just thankful that the suffering is over."

  Freya "In virtually every possible way, death has so far been a vast improvement over the life I led."

  show freya default at center

  "I face the filing cabinet again. My hand almost immediately brushes against the object I've been searching for."

  show sari smile #as side image"

  Sari "Aha! Here it is!"

  "Beaming now, I show Freya the pocket mirror."

  Sari "I believe this mirror belonged to Mama."

  show freya smile at center

  "Freya hums with interest as she takes the mirror from me."

  show sari blush #as side image"

  "When her hand brushes against mine, I note that it's smooth and cool."

  "For a reanimated corpse, the feel of her skin isn't unpleasant at all. It's the reverse, rather."

  show sari default #as side image"

  show freya default at center

  "Freya surveys her own reflection for a full minute."

  "When she finally speaks, her voice sounds as if she's halfway in a dream."

  Freya "I look. . . ."

  "Her words trail off, leaving the remainder of her sentence a mystery."

  "Should I finish her sentence for her, or allow her to regard her reflection in silence?"

  menu:
    "Finish Freya's sentence.":
      jump lbl_114
    "Stay silent.":
      jump lbl_115

label lbl_114:

  $ freya_romance += 1

  show sari blush #as side image"

  "I open my mouth, and a word falls out before I can even arrange what I mean to say."

  Sari "Beautiful."

  show freya blush at center

  "Freya raises her gaze toward mine."

  Freya "Thanks, Sari. You sure know how to bring back color to these lifeless cheeks."

  show sari default #as side image"

  show freya default at center

  Sari "In this case, I've also done that in a very literal way."

  Freya "What do you mean?"

  jump lbl_116

label lbl_115:

  "I quietly observe as Freya continues to examine her own reflection."

  Freya "Keso, what do you think? Do I look good for a dead girl?"

  "Keso the rat releases a chorus of squeaks."

  Sari "What did your pet say?"

  show freya smile at center

  Freya "Keso said that, for a dead girl, I look more appealing than a block of cheese."

  show sari smile #as side image"

  Sari "Couldn't have said it better myself."

  Freya "Thanks, Sari. By the way, your father runs this funeral home, right?"

  show sari default #as side image"

  show freya default at center

  Sari "Yep. He's a licensed funeral director."

  Freya "Then he applied my makeup too?"

  jump lbl_116

label lbl_116:

  show sari smile #as side image"

  Sari "Papa did the rest of the embalming procedure, but I was the one who did your makeup."

  Sari "Your foundation, your eyeshadow, your eyeliner, your blush, your lipstick. Everything."

  show freya shock at center

  Freya "That's incredible! Do you do this often?"

  Sari "More and more often lately."

  show freya default at center

  Sari "I'm enrolled as a sophomore student in the Mortuary Studies program at the local college."

  Sari "Once Papa retires, I'm planning to take over this place."

  Sari "And doing the makeup of the deceased clientele is undoubtedly my favorite part of the embalming process."

  Sari "Papa lets me practice on the cadavers, although he occasionally redoes the makeup if he thinks I've gone too far."

  Sari "I then take photographs to include in my mortuary cosmetology portfolio, with the consent of the family of the deceased."

  Sari "I don't plan to apply to other funeral parlors after I graduate, but I can always show my portfolio to prospective clients."

  Sari "This way, I can prove that I've had plenty of prior experience even though I'm still young."

  "As I explain all of this to Freya, she listens with genuine interest."

  show freya smile at center

  Freya "That sounds wonderful, Sari."

  Freya "You have such a clear vision for your future, and you're taking concrete steps to achieve it."

  show sari default #as side image"

  show freya default at center

  "I wonder whether I should ask Freya if she harbored her own big dreams when she was alive."

  "Is the subject of dreams too sensitive for someone who died at around my age? Should I talk about something cheerful instead?"

  menu:
    "Ask Freya about her dreams.":
      jump lbl_117
    "Talk about a lighter topic.":
      jump lbl_118

label lbl_117:

  $ freya_romance += 1

  "We're already talking about dreams, so it only makes sense to continue this conversation, right?"

  Sari "How about you? What did you dream about?"

  show freya sad at center

  Freya "Given my early diagnosis, I wasn't encouraged to think that far ahead."

  Freya "But the years went by, and I continued fighting for my life."

  show freya smile at center

  Freya "I eventually began to nurture a dream, if only in secret."

  show sari anxious #as side image"

  Sari "If it's a secret, then you don't have to talk about it."

  Freya "No, I {i}want{/i} to talk about it. You don't know how refreshing it is — even being asked about something this indulgent."

  show sari default #as side image"

  Sari "So what was your dream, then?"

  Freya "I wanted to travel. I wanted to see the world beyond the windows of the house, or of the hospital."

  Sari "Where did you dream of going?"

  show freya default at center

  Freya "No specific location, really. I just wanted to walk toward any direction that I desired."

  Freya "Without being hooked up to tubes, and without needing to keep track of a plethora of health indicators."

  jump lbl_121

label lbl_118:

  "Yes, a cheerful topic is the ticket, especially when it comes to conversation with someone who's already dead."

  "But what exactly should I talk to Freya about?"

  menu:
    "My classes today at school.":
      jump lbl_119
    "The weather outside.":
      jump lbl_120

label lbl_119:

  "I tell Freya about the classes I attended at the college today, which included microbiology and thanatochemistry."

  Freya "You enjoy the biological sciences, huh? Science in general was never my strong suit."

  Sari "What was your favorite subject in school?"

  Freya "I was homeschooled for the most part, but I enjoyed all the mathematical subjects. Math is my Lola's specialty."

  Freya "Lola somehow stays super sharp about everything mathematical, even though she's forgetful about almost everything else."

  show sari anxious #as side image"

  Sari "Ugh, math."

  show freya laugh at center

  "Freya giggles as I scrunch up my nose in distaste."

  Freya "Oh, come on. Surely you have to do sums too, if you're planning to operate a funeral home on your own?"

  show freya smile at center

  Sari "And that's what a calculator is for."

  show sari default #as side image"

  "Freya seems to be fighting back another giggle."

  show freya default at center

  jump lbl_121

label lbl_120:

  "Sure, the weather might not be the most riveting topic, but it's {i}something{/i} to talk about."

  Sari "So the sky outside is cloudy, huh? You must've noticed it while you were running around the funeral home earlier tonight."

  Freya "I wasn't really paying attention. I was too caught up in the theatricality of my prank."

  Sari "There were lots of gray clouds. Yael pointed them out while we were in the jeepney on the way home from school."

  Freya "Then perhaps it will rain tonight."

  Sari "Yeah, maybe."

  "And that's that. Freya and I have fully exhausted this thrilling conversational topic."

  jump lbl_121

label lbl_121:

  "She now returns the mirror to me, and I slip it into my pocket."

  Freya "Hey, Sari?"

  Sari "Yeah?"

  show freya smile at center

  Freya "I want to see you in your natural element. Why don't you do my makeup again?"

  Sari "Do you dislike your current look?"

  Freya "No, it's not that. You mentioned that your father reapplies the makeup of the corpses whenever he thinks you've gone too far."

  Freya "That got me curious."

  Freya "What would it look like if you could have your way? If you could go {i}too far,{/i} without anyone holding you back?"

  Freya "Will you show me that?"

  show sari smile #as side image"

  "I only need to think about this for a second, then my face breaks into a broad smile."

  Sari "Yeah! Let's do it!"

  Sari "We'll have to transfer to the morgue. All my makeup stuff is there."

  Freya "Sure, let's go."

  show bg morgue with slow_dissolve

  show sari default #as side image"

  show freya default at center

  "Back in the morgue, I arrange my cosmetic tools in the usual manner."

  "Should I ask Freya about what kind of makeup she's partial to?"

  menu:
    "Ask Freya about her preferences.":
      jump lbl_122
    "Trust my instincts.":
      jump lbl_123

label lbl_122:

  $ freya_romance += 1

  Sari "Do you have any particular preferences? Any soft or hard limits?"

  show freya blush at center

  Freya "I'll leave all of that to you. I'm trusting you blindly here."

  show sari smile #as side image"

  Sari "Got it."

  jump lbl_124

label lbl_123:

  show sari smile #as side image"

  "I have to be confident in my own skills. Otherwise, I can't perform to the best of my ability."

  jump lbl_124

label lbl_124:

  stop music fadeout 1.0

  show freya smile at center

  Sari "Let's start!"

  "It's mortuary makeup time!"

  play music menumusic fadein 2.0

  scene cg makeup_pic with slow_dissolve

  "First things first — I ready my canvas with some handy makeup remover, then reapply the foundation."

  "As I'm putting on the foundation, I initiate conversation."

  Sari "By the way, I don't know the rules of being a walking cadaver, but you might want to research long-term embalming methods."

  Sari "Formalin injections. That sort of stuff."

  Sari "More likely than not, you'll still have to contend with the natural process of decomposition."

  Freya "Thanks for the heads-up. I'll look into it." 

  "There, the foundation is finished."

  "As for Freya's eyebrows, they're already in lovely shape. No need to do any work on them."

  "Which color of eyeshadow should I select?"

  menu:
    "Go for gold.":
      jump lbl_125
    "Purple packs some drama.":
      jump lbl_126

label lbl_125:

  "Yes, this gold shimmer will accentuate Freya's dark eyes wonderfully."

  jump lbl_127

label lbl_126:

  $ makeup_skill += 1

  "Yes, when else am I going to get the chance to dab on such bold colors?"

  "If Papa was watching me, he'd make me wipe off this color straight away. I should take this opportunity while I can."

  jump lbl_127

label lbl_127:

  "Once the application of eyeshadow is over, I pencil in some eyeliner." 

  "Should I add some mascara too?"

  menu:
    "Apply mascara.":
      jump lbl_128
    "Mascara would be overkill.":
      jump lbl_129

label lbl_128:

  $ makeup_skill += 1

  "Yeah, why not? Mascara will make Freya's pretty eyes pop even more."

  jump lbl_130

label lbl_129:

  "Yeah, adding mascara at this point would be going overboard."

  jump lbl_130

label lbl_130:

  "Okay, her eyes are done."

  "Next comes the blush. Which hue should I go for?"

  menu:
    "Rose is a classic.":
      jump lbl_131
    "Tawny rose will give the classic a kick.":
      jump lbl_132

label lbl_131:

  "I apply the rose blush with a careful hand."

  jump lbl_133

label lbl_132:

  $ makeup_skill += 1

  "Tawny rose it is. I meticulously trace the contours of her cheekbones with my makeup brush."

  jump lbl_133

label lbl_133:

  "All right! Her cheeks are looking perfectly rosy!"

  "Lipstick is last. Which one should I pick?"

  menu:
    "Latte lips will round out this look.":
      jump lbl_134
    "Pull out all the stops with cherry red.":
      jump lbl_135

label lbl_134:

  "This latte color complements both her complexion and the rest of the look."

  jump lbl_136

label lbl_135:

  $ makeup_skill += 1
  $ freya_romance += 1

  "As I twist open the cap of the lipstick, Freya speaks up for the first time since I was putting on the foundation."

  Freya "What lipstick color is that?"

  Sari "Cherry red."

  "She smiles and sings the lyrics of a song."

  Freya "{i}The taste of her cherry chapstick.{/i}"

  "My cheeks heat up as I recognize the line from {i}I Kissed A Girl{/i} by Katy Perry."

  "In the interest of professionalism, however, I maintain my composure."

  jump lbl_136

label lbl_136:

  stop music fadeout 1.0

  show bg morgue with slow_dissolve

  show sari smile #as side image"

  show freya default at center with dissolve

  "There! Freya's new look is all done!"

  "I hand her the pocket mirror again so that she can see the end result for herself."

  play music bgm fadein 2.0

  show sari default #as side image"

  if makeup_skill >= 3:
    jump lbl_137
  if makeup_skill < 3:
    jump lbl_138

label lbl_137:

  show freya shock at center

  "Her eyes widen at the sight of her reflection."

  show sari anxious #as side image"

  Sari "Is it too much? Now this is a look that Papa would definitely classify as going {i}way too far.{/i}"

  show freya smile at center

  Freya "It's so {i}dramatic.{/i} I love {i}everything{/i} about it."

  Sari "You're not just saying that to be diplomatic?"

  Freya "I'm not! This look is a perfect match for my personality, isn't it?"

  show sari smile #as side image"

  Sari "You and your theatrical tendencies."

  Freya "You see what I mean? We haven't been talking long, but you already know me so well!"

  "Freya pirouettes, allowing the hem of her skirt to flounce around."

  show freya laugh at center

  Freya "I have my best face on! I'm wearing the prettiest dress I've ever worn!"

  Freya "I may have just died, but I've never felt more alive! What delicious irony!"

  Freya "I feel so free! I feel like I can do anything!"

  show freya smile at center

  Sari "So what do you want to do now?"

  Freya "Travel! I want to wander wide and far! It doesn't matter where I go!"

  Freya "I'm yearning to see things I've never seen — places I've never been — before!"  

  if freya_romance >= 3:
    jump lbl_139
  if freya_romance < 3:
    jump lbl_140

label lbl_138:

  show freya smile at center

  "She flashes a winning smile at the mirror. Blows her reflection a kiss."

  show sari smile #as side image"

  Sari "I take it that you approve of your new look, then?"

  Freya "I do. This is a very polished and professional look indeed."

  Freya "Why don't you include this look in your portfolio?"

  Sari "Yeah, you're right! I should take a photo!"

  show sari default #as side image"

  show freya default at center

  "I reach into a cabinet for my camera. Papa got it for me last year, for my eighteenth birthday."

  "I raise the camera and position the viewfinder in front of my right eye."

  Sari "May I?"

  show freya smile at center

  "Parking her hands on her hips, Freya strikes a pose and beams at the camera."

  Sari "On second thought, maybe you should lie down and close your eyes."

  Sari "This is for a mortuary cosmetology portfolio, after all."

  show freya shock at center

  Freya "Oh, right! Silly me!"

  show freya default at center

  "Without awaiting further instructions, Freya stretches out over the floor."

  "She lays her arms in a cross over her chest."

  Freya "Like this?"

  Sari "Yeah, that's perfect."

  "As I move closer to hover over Freya's supine position, I accidentally knock the pocket mirror to the floor."

  show sari shock #as side image"

  show freya shock at center

  "It shatters into jagged fragments."

  "The splintering noise is surprisingly loud, echoing around the morgue."

  show sari anxious #as side image"

  Sari "Ack! Freya, are you okay? Are you hurt?"

  show freya default at center

  Freya "I'm totally fine. Just take the pictures. You can sweep away this mess later."

  show sari default #as side image"

  "Freya does seem okay, so I do as she says."

  "Carefully toeing around the shards of the broken mirror, I snap photo after photo."

  show sari smile #as side image"

  "As I gaze at Freya through the viewfinder, I'm arriving at the slow realization that this may be my best work yet."

  "I'm smiling to myself now."

  hide freya

  show sari shock #as side image"

  "But just then, the sound of a door swinging open makes me freeze."

  "Oh. {i}Oh no.{/i}"

  show papa anxious at center with dissolve

  Papa "Rosario? What's going on here? What's with this strange setup?"

  "The sound of the breaking mirror must have woken him up!"

  Sari "Um. This. . . . This is. . . ."

  if freya_romance >= 3:
    jump lbl_141
  if freya_romance < 3:
    jump lbl_142

label lbl_139:

  Sari "We'll do that, then."

  show freya default at center

  "Freya's gigawatt grin fades."

  Freya "{i}We?{/i}"

  Sari "Yeah. You and me."

  show sari anxious #as side image"

  Sari "Why? You don't want me to come with you?"

  show freya anxious at center

  Freya "Of course I want you to come. But. . . ."

  Sari "But what? Who else is going to perform the embalming procedures to help your body stave off decomposition?"

  stop music fadeout 1.0

  Freya "But what about your family? Your home?"

  Freya "I can't just ask you to uproot your life and abandon your dream to help me achieve mine."

  play music mellow fadein 2.0

  show sari default #as side image"

  show freya default at center

  Sari "But I want to do this too, you know? Look at it this way."

  Sari "Ever since I was young, I've only ever been interested in the science of death, and the rituals of those who mourn it."

  Sari "The phenomenon of life and death colliding — nothing enthralls me as much as that."

  show sari smile #as side image"

  Sari "And you're an anomaly. You may be physically dead, but I've honestly never met anyone as spirited and as vibrant as you."

  Sari "My education isn't confined to a classroom. And I just have this feeling that I'll learn more about everything I love if I'm with you."

  Sari "I can take a leave from school. I'm nineteen, so I don't need anyone's permission to do that."

  show freya anxious at center

  Freya "But how will your father take it? He might be unable to stop you, but he'll still be upset."

  show sari anxious #as side image"

  "I think about this for a minute, then sigh."

  Sari "You're right. I can't just leave without any explanation."

  Sari "Papa will worry himself to death if he doesn't know where I am and what I'm doing."

  show sari smile #as side image"

  Sari "There's no other way, then. I'll have to introduce you to Papa."

  show freya laugh at center

  Freya "Oh! Is this going to be a meet-the-parents situation, then?"

  Freya "How exciting!"

  show sari default #as side image"

  show freya smile at center

  Sari "On the contrary, we have to make this meeting as unexciting as possible. We'll need to take it slow."

  Sari "Papa is a senior citizen. I don't want to give him a heart attack by springing you on him."

  show freya default at center

  Sari "But I do believe that taking it slow is for the best. This way, we can stay for your funeral rites too."

  Sari "Are you going to let your family know what's happened to you?"

  show freya sad at center

  "Freya shakes her head."

  Freya "I don't think that's a good idea. In the first place, I don't even know how long this weird half-life of mine will last."

  Freya "While I'm still so uncertain, I should grant my family their peace of mind."

  Freya "I'll let them mourn my loss and begin the process of moving on."

  show sari sad #as side image"

  "Seeing the sorrow in Freya's eyes, I reach for her hand."

  "Her skin is cold, yes, but when she squeezes my palm in response, the pressure emits an undeniable warmth."

  show sari smile #as side image"

  show freya blush at center

  Sari "Hey, you're not alone, okay? I'm here."

  Sari "Things around the funeral home might be upsetting for a while, but I promise you that we'll get away soon enough."

  Sari "Soon you'll see everything you ever wanted to see, and I'll learn everything I ever wanted to learn."

  Sari "Best of all, we'll be together."

  show freya smile at center

  "Freya flashes a wry smile."

  Freya "I should thank my lucky stars that you developed a scientific interest in me."

  Freya "For a corpse like me, it's hard to imagine a better traveling companion than you."

  Freya "You've already been trained in embalming, and as a bonus, you specialize in mortuary cosmetology."

  show freya laugh at center

  Freya "My own personal makeup artist! This is just like winning the lottery!"

  show sari laugh #as side image"

  "When she laughs — a tinkling laugh like bells — I follow suit, even though my mind is elsewhere now."

  show sari blush #as side image"

  show freya smile at center

  "Freya may presume that my interest in her is solely scientific, but I doubt that's the case."

  "I wouldn't have proposed this excursion to destinations unknown, if it was any other corpse that was reanimated in this morgue."

  "Beyond scientific curiosity, something about Freya, specifically, draws me in."

  "I want to know everything about {i}her.{/i} Not just about the way she works."

  "But a confession of this nature is perhaps better said down the line, once we've gotten to know each other better."

  show sari smile #as side image"

  "Freya and I, we're taking this new life slow for now."

  scene cg ending09_pic with slow_dissolve

  "For one of us, it may always be a half-life, but that doesn't mean it isn't a life worth living to the fullest."

  scene cg ending09 with slow_dissolve
  $ persistent.ending_seen_09 = True
  $ ending_theme = "best"
  pause
  jump lbl_credits

  return

label lbl_140:

  Sari "Why don't you do that, then? Who's going to stop you now?"

  show sari default #as side image"

  show freya default at center

  Freya "You're not going to stop me?"

  Sari "Do you want me to?"

  Freya "I don't know much about running a funeral home, but I'd imagine that it would be bad business to let corpses walk away."

  show sari smile #as side image"

  Sari "True, but now that I've befriended you, I'd feel guilty about forcing you to stay when you don't really want to."

  hide freya

  show bg darkness with slow_dissolve

  "So Freya and I say our farewells."

  "We may have only known each other briefly, but I'm certainly not going to forget her anytime soon. Or ever."

  "How often is it that one meets a walking and talking cadaver, after all?"

  stop music fadeout 1.0

  show bg foyer_open with slow_dissolve

  show sari default #as side image"

  show freya default at center with dissolve

  "Before Freya goes, I hand her the camera that Papa got for me last year, for my eighteenth birthday."

  "This camera may be handy for buffing up my mortuary cosmetology portfolio, but it will surely prove more useful to Freya."

  play music mellow fadein 2.0

  show sari smile #as side image"

  Sari "Take photos of all the places you see. I want to see them too."

  Sari "You {i}are{/i} coming to visit Roxas & Roxas Funeraria, right?"

  show freya smile at center

  Freya "Of course. There's no way I can resist sampling more of your makeup magic."

  Freya "Your skills can give a girl the boost of confidence she needs."

  Sari "I'll be sure to practice as much as I can."

  Sari "And after Papa stops being mad at me for losing a corpse, I'll convince him that there's a market for bolder makeup looks among the dead."

  Sari "A minuscule market, maybe. But it's there. Tried and tested."

  Freya "You do that."

  Freya "Keep fighting the good fight for the corpses, Sari. Send out the dead with the pizzaz they deserve."

  show sari laugh #as side image"

  show freya laugh at center

  "We're both laughing as we wave goodbye."

  "Freya blows me a kiss as she goes, so I blow kisses back. Kisses for Freya, and for Keso too."

  "This definitely isn't goodbye for good. Just goodbye for now."

  scene cg ending10 with slow_dissolve
  $ persistent.ending_seen_10 = True
  $ ending_theme = "good"
  pause
  jump lbl_credits

  return

label lbl_141:

  show sari anxious #as side image"

  "I can say nothing more, so Papa resumes his ranting."

  Papa "Why haven't you swept this broken glass? Don't stomp around recklessly like this. You'll hurt yourself."

  Papa "Don't tell me you purposely included all this broken junk in your shots, just for dramatic effect?"

  Papa "You young people and your radical ideas! I'm always having to give both you and Yael a reality check!"

  Papa "And what did you do to this poor girl's makeup? What do you think her family will say once they see her like this tomorrow?"

  Papa "The look you gave her this afternoon was the best I've ever seen from you! What a waste!"

  "I'm thankful that, throughout Papa's entire tirade, Freya has the good sense to remain motionless on the floor."

  show sari default #as side image"

  show papa default at center

  "When Papa pauses to draw breath, I just then interrupt his sermon."

  Sari "Pa, don't you have a migraine? You should lie down."

  Sari "If you don't get a full night's sleep, you'll feel worse tomorrow."

  Sari "Don't you always say that the clients are our priority? For the family of the deceased, we should be on our best behavior at the funeral."

  Papa "I took some paracetamol before I went to bed."

  show papa anxious at center

  "But even as he says this, he's massaging both temples of his still sore head."

  Papa "Fine. I'm going back to sleep."

  Papa "But don't think for a moment that you're off the hook for this, Rosario. Whatever this is."

  show sari anxious #as side image"

  show papa default at center

  "He crouches down, seemingly to help me return Freya's body to the refrigeration unit, but I stop him."

  Sari "I'll do that, Pa. I can do it."

  Sari "I made this mess, so I should be the one to take care of it, right?"

  show papa anxious at center

  "With a world-weary sigh, Papa finally retreats from the morgue."

  "He shuts the door behind him."

  hide papa

  show sari default #as side image"

  "I wait until I hear Papa's footsteps thumping up the stairs, then offer my hand to Freya on the floor."

  show freya default at center with dissolve

  "She takes my hand as she gets back to her feet."

  show sari anxious #as side image"

  Sari "That was a close call, huh?"

  Sari "Sorry about Papa. He's twice as grumpy if his sleep has been interrupted."

  show sari default #as side image"

  Freya "Some of the things he said were needlessly harsh. However, he does seem to genuinely care for you."

  Sari "Yeah. We bicker a lot, but since our other relatives are living in the Pangasinan province, we're all each other has."

  show freya sad at center

  Freya "Hey, I know you said those things about the funeral just to drive your father away, but you do have a point."

  Freya "We all have a long day tomorrow, as well as a long week ahead. You, your father, and I."

  Freya "My family's coming to see me, after all."

  show sari sad #as side image"

  Sari "Are you okay with that? Lying quietly in the coffin for an entire week?"

  Freya "I don't have a choice, do I? I need to give my family a chance to say their final goodbyes."

  show sari default #as side image"

  show freya default at center

  "Freya pulls open the door to the refrigeration unit."

  show bg morgue_open with slow_dissolve

  show sari anxious #as side image"

  "I shiver at the sudden burst of chilly air."

  "But Freya doesn't, of course. She doesn't get cold."

  "She doesn't feel anything anymore."

  show sari default #as side image"

  Freya "I should get back inside here, right? To slow the process of my body's decay?"

  Sari "Right. I'll see you here, early tomorrow morning."

  Sari "I have to redo your makeup before your family arrives, or else Papa will yell at me again."

  Freya "Of course."

  "Freya clambers back inside the refrigeration unit."

  hide freya

  show bg morgue_corpse with slow_dissolve

  Freya "Good night, Sari."

  Sari "Good night, Freya."

  show bg morgue with slow_dissolve

  "Closing the door to the refrigeration unit, I return Freya into the icy darkness once more."

  scene cg ending11 with slow_dissolve
  $ persistent.ending_seen_11 = True
  $ ending_theme = "bad"
  pause
  jump lbl_credits

  return

label lbl_142:

  stop music fadeout 1.0

  show sari anxious #as side image"

  "I'm grasping for words. Fruitlessly."

  show sari shock #as side image"

  show papa default at right with dissolve

  show freya default at left with dissolve

  "Before I can say anything more, Freya springs up from the floor."

  play music suspense fadein 2.0

  "She reaches for Papa's hand to shake it."

  show papa anxious at right

  "Papa doesn't move at all. He permits Freya to shake his hand."

  "Up, down. Up, down."

  show sari anxious #as side image"

  show freya laugh at left

  Freya "Hello there, Sir! You must be Sari's beloved Papa!"

  Freya "Sari has told me so much about you!"

  show freya smile at left

  Freya "She told me, for instance, that you performed most of the embalming procedure on my body, save for the cosmetics?"

  Freya "I laud you for your excellent work in patching me up to a presentable state! I feel fit as a fiddle!"

  Freya "As for the cosmetics, I asked Sari just now to show me an alternative makeup look!"

  show freya laugh at left

  Freya "Your daughter did a fine job, didn't she?"

  Freya "Look at what she's done to me!"

  show freya anxious at left

  "Just then, Papa wrenches back his right hand from Freya's."

  "His fingers are scrabbling wildly against his own chest."

  show sari shock #as side image"

  show freya shock at left

  "With a choked gasp, Papa falls backward on the floor."

  hide papa

  show freya shock at center with dissolve

  Sari "Papa!"

  "Sweat pours forth from Papa's forehead."

  "He's hyperventilating. Hard."

  Sari "My phone! Where is it? Where?"

  "It's not in my pockets. It's nowhere."

  "Panic is clawing up my throat."

  "Panic roots me to the floor, even though I know I should run."

  scene cg ending12 with slow_dissolve
  $ persistent.ending_seen_12 = True
  $ ending_theme = "worst"
  pause
  jump lbl_credits

  return

init:
    image cred = Text("[gui.about!t]\n\nMade with Ren'Py [renpy.version_only]", text_align=0.5, xmaximum=1200)
    image theend = Text("{size=80}Fin", text_align=0.5)
    image thanks = Text("{size=80}Thanks for playing!", text_align=0.5)

label lbl_credits_from_menu:
    call lbl_credits from _call_lbl_credits
    return
    
label lbl_credits:
        
    if (_in_replay):
        play music ending fadein 1.0
    else:
        $ending_track = "audio/music/ending_" + ending_theme + ".mp3"
        play music ending_track fadein 1.0

    $ quick_menu = False

    $ credits_speed = 20
    scene bg black
    with dissolve
    show cred at Move((0.5, 1.9), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    
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

        $ persistent.extras_unlocked = True
        
    $ quick_menu = True

    return




