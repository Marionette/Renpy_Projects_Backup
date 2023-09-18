# The script of the game goes in this file.

# The game starts here.

label start:

    python:
        inventory = Inventory()
        
    #reset all inventories.
    $store.inventory_hand = []
  
    $store.inventory_basement1 = []
    $store.inventory_basement2 = []
    $store.inventory_bathroom1 = []
    $store.inventory_bathroom2 = []
    $store.inventory_bedroom1 = []
    $store.inventory_bedroom2 = []
    $store.inventory_boilerroom = []
    $store.inventory_hallway = []
    $store.inventory_kitchen = []
    $store.inventory_livingroom1 = []
    $store.inventory_livingroom2 = []
    $store.inventory_office = []
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    ###comment out for testing###
    #jump lbl_introduction
    ###-----------------------###

    scene bg bedroom1 with pawwipe
    "Testing1"
    scene bg livingroom1 with logodissolve
    "Testing2"
    scene bg hallway with pawwipe
    "Testing3"
    scene bg bedroom1 dark with logodissolve
    "Testing4"
    call screen help() with pawwipe

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.
    menu:
      "Testing":
        call lbl_test from _call_lbl_test
      "Lock Testing":
        call lbl_testLock from _call_lbl_testLock
      "Intro":
        jump lbl_introduction
      "Explore the house":
        call lbl_explore_test from _call_lbl_explore_test
      "Magic circle Puzzle": 
        call lbl_magiccircle_puzzle_test
    
    c "I guess thats the end of this tail."
    return
    
label lbl_magiccircle_puzzle_test:       
    call puzzle_start()
    if Boilerroom_MagicCircleComplete:
        jc "Looks like I'm done here."
        return
    else:
        menu: 
            jc "Should i try again?"
            "Yes":
                jump lbl_magiccircle_puzzle_test
            "No":
                return


label lbl_explore_test:

    $Inventory_HeldItem_unlocked = True
    $Inventory_CatEyes_unlocked = True
    $Inventory_CatMouth_unlocked = True
    $Inventory_CatClaw_unlocked = True
    $Inventory_CatNose_unlocked = True  
    $Bedroom1_CollectionsActive = True
    $Bedroom1_DoorLocked = False
    $Hallway_Bedroom2DoorUnlocked = True
    show screen room_inventory()
    show screen test_menu()

    menu:
      "Explore Bedroom1":
        call lbl_bedroom1 from _call_lbl_bedroom1
        return
      "Explore Hallway":
        call lbl_hallway from _call_lbl_hallway
        return
      "Explore Bedroom2":
        call lbl_bedroom2 from _call_lbl_bedroom2
        return
      "Explore Upstairs Bathroom":
        call lbl_bathroom1 from _call_lbl_bathroom1
        return
      "Go Downstairs":
        pass
        
    menu:    
      "Explore Living Room 1":
        call lbl_livingroom1 from _call_lbl_livingroom1
        return
      "Explore Living Room 2":
        call lbl_livingroom2 from _call_lbl_livingroom2
        return
      "Explore Kitchen":
        call lbl_kitchen from _call_lbl_kitchen
        return
      "Go Downstairs":
        pass
    menu:    
      "Go Downstairs":
        pass
      "Explore Basement1":
        call lbl_basement1 from _call_lbl_basement1
        return
      "Explore Basement2":
        call lbl_basement2 from _call_lbl_basement2
        return
      "Explore Office":
        call lbl_office from _call_lbl_office
        return
      "Explore Basement Bathroom":
        call lbl_bathroom2 from _call_lbl_bathroom2
        return
      "Explore Boiler room":
        call lbl_boilerroom from _call_lbl_boilerroom
        return
      "Stop Exploring":
        pass
        
    return

              
label lbl_testLock:
    scene bg livingroom2
    jc "If i can figure out the combination i will be able get the door open."
    jc "Nothing left to do but try i suppose."
    call screen combination_lock()
    $lockResult = _return
    
    if (lockResult=="Success"):
      "*Click*"
      jc "Yay, it opened."
      return #lbl_chapter3_Basement
    else:
      "Hmm, it didn't open. I guess that was the wrong combination."
      jump lbl_testLock
      
label lbl_test:
    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    show screen room_inventory()
    #show screen hand_inventory()
    
    show jessicat angry at left
    show jessicaperson neutral:
      yalign -0.5
      xalign 0.7
    #show mp neutral:
    #  yalign -0.5
    #  xalign 0.5
    c "You've got to be kitten me! This is utterly apawling!"

    cp "Im a person now. I mean Meow."
    
    cp "Meow. Meow. Meow. Meow. Meow. Meow. Meow. "
    cp "Meow. "
    
    #show mc angry small:
    #  yalign 1.0
    c "You've got to be kitten me! This is utterly apawling!"
    
    
    show jessicat happy at left
    c "You've got to be kitten me! This is utterly apawling! You've got to be kitten me! This is utterly apawling! You've got to be kitten me! This is utterly apawling! You've got to be kitten me! This is utterly apawling!"
    
    
    c "a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a b c a"
    
    menu:
      "Are you sure?"
      "Pawsitive.":
        pass
      "Afurmative":
        pass
    # This ends the game.
    
    call lbl_bedroom1 from _call_lbl_bedroom1_1

    return

#-----------------------------------------------------------------------

label lbl_chapter_select:
    window hide
    $ quick_menu = False

    show chapter_screen with fade
        
    show screen chapter_display
    
    $ renpy.pause()
    
    hide screen chapter_display

    $ quick_menu = True
    return
#-----------------------------------------------------------------------
label lbl_introduction:

  $inventory.EmptyInventories()
  
  #-------- TODO: Remove this ---------#
  #$Inventory_HeldItem_unlocked = True
  #$Inventory_CatEyes_unlocked = True
  #$Inventory_CatMouth_unlocked = True
  #$Inventory_CatClaw_unlocked = True
  #$Inventory_CatNose_unlocked = True  
  #------------------------------------#
  
  $save_name = "Chapter 0: Introduction"
  #scene bg bedroom1
  call ShowBedroom1 from _call_ShowBedroom1
  play music music_LoungeLizard
  #Introduction:
  #Come in tired
  show jessicaperson neutral at left:
      yalign -0.5
  jp "Fi-nally!"
  jp "I thought those stairs would never end."
  jp "If i had known i was going to end up on a double shift, i would not have stayed up as late last night."
  "Jessica kicked off her shoes and with arms outstretched she let herself fall backwards onto her bed. "
  jp "I am dead."
  jp "So tired. I can't remember the last time i was this exhausted."
  #jp "Probably that time i had to stay up for a full 24 hours because i had that report due that i had put off doing till the day before. I wish i could say i had learned my lesson after that, but i'd only be lying to myself."
  "*scratch*"
  jp ". . ."
  "*scratch* *scratch*"
  jp ". . ."
  qqq "Meow"
  jp "I'm already comfortable Clawdia, you'll have to open the door yourself if you want in."
  cc "Meow"
  jp "I feel like its time you pulled your weight Clawdia, you're a grown ass cat now. I can't baby you your entire life."
  jp "Think of it as the door to the rest of your life. Figuratively and literally."
  "*scratch* *scratch*"
  jp "UGH. Unfurgivable."
  "Jessica pulled herself up in a dramatic fashion, dragging her arms behind her like she had lead weights around her wrists."
  show jessicat happy:
    xalign 0.7
    yalign 0.6
  "As soon as the door was opened a crack Clawdia slid through, like a fuzzy snake through a space that didnt look nearly big enough."
  "She purred as she walked around jessicas legs, rubbing against her with her head and body as she did." 
  jp "Flattery will get you nowhere young lady."
  "Jessica feigned anger at her cat as she bent down to pick her up."
  #fall asleep on bed
  jp "As punishment you are going to lie here with me."
  "Closing the door behind her Jessica plopped back down on the bed with the cat in her arms."
  "Spooked by the sudden motion, Clawdia tried to wriggle free, but Jessica held her on her chest and rubbed her head until she settled down."
  jp "There there."
  jp "*Yawn*"
  jp "Ok now I'm just going to close my eyes for a second, then ill go put my pyjamas on."
  "Jessica felt Clawdia move around and start kneading at her belly in an effort to get comfortable."
  "It wasnt long before they both drifted off to sleep."
  
  stop music fadeout 1.0
  scene bg black with fade
  
  ". . ."
  #dream ?
  
  #wake up feeling refreshed
  $Bedroom1_ClawdiaAwake = False
  jc "*Yaaawn*"
  jc "Wow i slept like a rock."
  #scene bg bedroom1
  call ShowBedroom1 from _call_ShowBedroom1_1
  show item blanket bump
  #stretch - notice paws
  "Jessica pushed her paws out in front of her as she arched her back in a long stretch."
  play music music_SlowlyCreeping
  jc "P-PAWS?!"  
  #Freak the fuck out. 
  jc "W-Where are my hands?!"
  "Jessica twisted and turned her paws to make sure it was definitely her own 'hands' she was looking at."
  jc "What the heck is going on?"
  jc "I must still be dreaming. It has to be a dream."
  menu:
    "Accept it":
      jc "No, everything feels to real for this to be a dream. I just have to accept it."
    "Try pinching yourself.":
      jc "I should try pinching myself to see if its a dream. Thats what they do in movies, right?"
      jc "Jessica pawsed for a second."
      jc "I don't know how I'm supposed to pinch myself with no thumbs."
      jc "I suppose the idea is that if i can feel pain I'm awake, so it doesn't have to be a pinch."
      menu:
        "Try something else?"
        "Use your claws":
          jc "Jessica pushed out a claw from her paw and poked her other paw with it."
        "Use your teeth":
          jc "Jessica lifted her paw to her mouth and gently bit into it."
      jc "Ouch."
      ". . ."
      jc "Damn. I guess its not a dream."
  jc "Why don't i look around and see if i can figure out whats going on?" 
  
label lbl_introduction_explore_blanket_mirror:
  #[explore a little here, doesnt do much, click on sleeping person to continue]
  #[can click mirror to realise youre clawdia]
  call lbl_bedroom1_intro_blanket_mirror from _call_lbl_bedroom1_intro_blanket_mirror
  $res = _return
    
  #"script [res]"
  if (res=="bed_bump"): 
    call lbl_introduction_blanketBump from _call_lbl_introduction_blanketBump
  if (res=="mirror" ): 
    call lbl_introduction_mirror from _call_lbl_introduction_mirror
  
  if Bedroom1_Intro_BlanketUsed and Bedroom1_Intro_MirrorUsed:
    jump lbl_introduction_continue
  
  #Find a mirror to see self
  if Bedroom1_Intro_BlanketUsed:
    jc "If my body is meowing, then that means. . ."
  #Try to find body
  if Bedroom1_Intro_MirrorUsed:
    jc "If I'm Clawdia, where is my body?"
  
  jump lbl_introduction_explore_blanket_mirror
  
label lbl_introduction_blanketBump:
  $Bedroom1_Intro_BlanketUsed = True
  #jc "This bump. . ."
  #jc "Is there something under here?"
  
  if Bedroom1_Intro_MirrorUsed:
    show jessicat neutral at left
  "Jessica poked and prodded the bump in the blanket. It was hard in places, and squishy in others."
  "She tried walking on it, but was startled when it moved slightly."
  jc "Ahh!"
  
  jc "Is someone sleeping under there?"
  #Realise that her body is still asleep
  #"Wait, if this is my bed, and i'm like this, then theres only one thing this could be."
  "Jessica, with much struggle, pulled the blanket back enough to see the face of the mysterious sleeper."
  show jessicaperson asleep:
    yalign -0.5
    xalign 0.7
  if Bedroom1_Intro_MirrorUsed:
    show jessicat angry at left
  jc "Thats my face!"
  jc "I mean its me!"
  jc "I mean. . .Ahh!"
  "Jessicas mind raced as she tried to process what was going on."
  jc "How is this possible?"
  jc "What has happened?"
  
  "Jessica turned to the person to ask if they knew anymore than she, but realized they were still asleep."
  jc "How can you be asleep at a time like this?!"
  
  if Bedroom1_Intro_MirrorUsed:
    show jessicat neutral at left
  jc "I'm going to have to wake her up if I'm going to get some answers."
  #Try to wake up [sit on face/unlock claws?]
  "Jessica tried calling out to her but there was no response."
  "She tried more poking and prodding but there wasn't much reaction there either."
  if Bedroom1_Intro_MirrorUsed:
    show jessicat angry at left
  jc "If this is going to work I'm going to have to take drastic measures."
  
  menu:
    "How will i wake them up?"
    "Sit on her face":
      jc "I'll sit on her face, that should wake her up."      
      jc "I swear the number of times Clawdia has done this to me. . ."
      
      "Jessica climbed onto her face and made her self comfortable."
      "It wasn't long before a few muffled groans sounded out below her, a sign that the person was stirring."
      "Suddenly with a gasp the person sat up, gasping for breath"
      show jessicaperson surprised
      qq "*GASP*"      
    "Use your claws":
      "Jessica, realizing that her fuzzy paws came with some concealed weapons, decided to put them to good use."
      jc "Looks like i have the perfect tool for the job."
      jc "If it works for Clawdia, it can work for me."
      #$Inventory_CatClaw_unlocked = True
      "Jessica pushed out her claws and raised up her paw. "
      "She took a swipe at the persons nose, scratching the tip of it lightly."
      "With a scream the body jumped awake"
      show jessicaperson surprised
      qq "Ahh!"
      
  #Body wakes up and falls on the floor
  "Startled Jessica leaped backwards and missed the edge of the bed."
  "Luckily for her she managed to land on her feet."
  "The person wasn't so lucky as in a sleepy daze, misjudged where they were putting their hand and also fell off the bed."
  show jessicaperson unconcious
  "Jessica leaped out of the way as they crumpled into a pile at the side of the bed."
  #body gets up
  if Bedroom1_Intro_MirrorUsed:
    show jessicat neutral at left
  jc "Are you okay?"
  show jessicaperson yawn
  "The person simply slid out of their awkward position and stretched their limbs while yawning"
  qq "*Yaaaaawn*"
  #try to talk to body
  jc "Hey!"
  show jessicaperson neutral
  "The person turned to face her."
  if Bedroom1_Intro_MirrorUsed:
    show jessicat angry at left
  jc "Who are you?!"
  jc "Why do you look like me?!"
  jc "Whats happening here?!"
  "Jessica sent a barrage of questions at the person who looked just like she had."
  show jessicaperson confused
  "The person just stared back at her and tilted their head as if unsure what was being said."
  #get a meow - realize its Clawdia an that you swapped
  if Bedroom1_Intro_MirrorUsed:
    show jessicat neutral at left
  jc "Do you understand what i am saying?"
  qq "Meow."
  "A feeling of dread passed over Jessica as the person in front of her, who looked just like her, meowed."
  jc "W-What did you say?"
  qq "Meow."
  
  if Bedroom1_Intro_MirrorUsed:
    show jessicat sad at left
  "Jessica looked down at her fuzzy paws as she thought about what this meant."
  #if Bedroom1_Intro_MirrorUsed: 
  
  $Bedroom1_ClawdiaAwake = True
  scene bg bedroom1
  show item blanket
  if Bedroom1_Intro_MirrorUsed:
    show jessicat neutral at left
  
  return
  
label lbl_introduction_mirror:
  #jc "Of course, the mirror!"
  
  #[explore to find mirror, if not clicked the first time]
  #Realise that you're the cat
  $Bedroom1_Intro_MirrorUsed = True
  show jessicat angry at left
  #jc "Holy Shit I'm a cat!"
  jc "WAAHHH!"
  "Jessica jumped at the sight of her reflection, almost falling off the dresser in the process."
  jc "I-I'm a cat!"
  jc "But this pattern. . ."
  "Jessica soon realized that it wasn't just any cat. it was her cat."
  jc "I'm Clawdia?!"
  show jessicat sad at left
  jc "How is this even possible?"
  
  return
  
#-----------------------------------------------------------------------
label lbl_introduction_continue:
  show jessicat neutral at left
  jc "I need to get out of here to figure out whats going on."
  
  "Jessica looked at the closed door to her room, then at her tiny paws before looking back at the door again."
  show jessicat sad at left
  jc "I can't open the door like this."
  "After thinking about it for a second she turned to Clawdia"
  show jessicat neutral at left
  show jessicaperson neutral:
    yalign -0.5
    xalign 0.7
  jc "Ok Clawdia, time to make use of that beautiful body of mine to get us out of here."
  show jessicaperson confused
  ". . ."
  jc "Open the door Clawdia."
  show jessicaperson confused
  cp "Meow"
  ". . ."
  show jessicat sad at left
  jc "Ugh. I guess talking to her is about as useful now as when we were in our own bodies. The same cat-human language barrier between us."
  stop music fadeout 1.0
  pause(1.0)
  play music music_OnTheProwl fadein 1.0
  show jessicat neutral at left
  show jessicaperson neutral
  
  jump lbl_chapter1_EscapeRoom
  
#-----------------------------------------------------------------------
label lbl_chapter1_EscapeRoom:
  $save_name = "Chapter 1: Escape Room"
  $chapter_section = "\"Escape Room\""
  $chapter_number = "1"
  call lbl_chapter_select
  
  jc "Well I'll have to try and find us another way out of here then."

  show screen room_inventory()
  show screen test_menu()
  
  $Bedroom1_CollectionsActive = True
  call lbl_bedroom1 from _call_lbl_bedroom1_2
  
  jump lbl_chapter1_Escaped
  
  
label lbl_chapter1_Escaped:
  jc "Yay, I'm free."
  
  jump lbl_chapter2_Exploration
  
#-----------------------------------------------------------------------

label lbl_chapter2_Exploration:
  $save_name = "Chapter 2: Exploration"
  $chapter_section = "Exploration"
  $chapter_number = "2"
  call lbl_chapter_select
  
  scene bg bedroom1
  show item blanket
  
  "*Now you can use the Navigation arrows while exploring to move to other parts of the house*"
  jc "Guess I'll check out the rest of the house."
  call lbl_bedroom1_explore from _call_lbl_bedroom1_explore
  
  # --- DEMO END
  #jump lbl_END
  
  jump lbl_chapter2_Phonecall
  
label DEMO_END:
  show bg livingroom1
  show jessicat happy at left
  jc "This is the current end of the demo. Hope you had fun."
  jc "Don't worry, the rest of the game is comming soon!"
  return
    
label lbl_chapter2_Phonecall:
  $save_name = "Chapter 2: Phonecall"
  
  scene bg livingroom1
  
  "*Phonecall with Veronica Happens*"
  "Theres no sound but i can hear the phone buzzing away on the table as it vibrates."
  jc "A phonecall? But nobody ever phones me."
  jc "WAIT!"
  jc "If I can talk to someone on the phone, I can get help!"
  
  "It takes a few fumbling tries to answer the phone with Clawdias fuzzy paws."
  v "Hey Jessica, its Veronica, I just arrived at the hotel."
  jc "Hotel?"
  jc "Oh right, veronica has that writers convention or whatever this weekend."
  v "Hello?"
  jc "Nevermind that, you won't believe what has happened to me!"
  v "Clawdia?"
  jc "What? I Yeah, wait how did you."
  v "Jessica, very funny answer the phone, I'm not gonna sit here an talk to your cat."
  jc "I'm right here, now listen! I got turned-"
  v "JESSICA!"
  jc "Why are you shouting? I'm right here."
  v "Wait, did the cat really answer the phone."
  jc "Are you even listeni-"
  v "OMG! Its like shes trying to have a conversation on the phone with me!"
  jc "Wait, what do you mean?"
  v "Meow meow meow to you too kitty~"
  jc "Meow? Wait, do you not understand me?"
  v "This is amazing, she must've picked it up watching us talking into our phones all the time."
  jc "Veronica! I need your help!"
  v "I can't wait to tell Jessica, she is gonna be so mad that she missed it."
  jc "VERONICA!"
  v "Woah, Jeez. You're getting a little too excited now."
  v "Anyways Jessica must still be in bed, so ill just send a text for her to read when she gets up."
  jc "NO DON'T HANG UP!"
  v "Goodbye to you too Clawdia. Meow Meow Meow."
  "Veronica ends the call"
  "Jessica quietly sobs in the realization that she is all alone in this predicament."
  "Not only can she not talk to anyone to ask for help, but her roommate won't be back until Monday."
  "The phone buzzes"
  jc "Oh right, Veronica said she was going to send a text didn't she?"
  jc "Wait! Text! Of course, if i send a text explaining my situation, maybe she can find some way to help."
  
  "Jessica fumbled around with the phone to select Veronicas text to see what she had sent."
  
  v "Hey Jessica, I know you're probably still sleeping, but i forgot to get the fan out of my room for you before i left."
  v "Stayed up late working on an experiment and I overslept, so i was in a rush. But if you need into my room, the keys are in the bowl on top of the fridge."
  v "PLEASE lock the door again after you leave. I don't want your cat in my room again. You know how my alergies are."
  v "OH! And (if it wasn't just you messing with me), then your cat somehow answered the phone and was trying to talk to me."
  v "Was so cute, OMG! I'll be done around 6pm so if you give me a call we can catch up."
  
  jc "Classic Veronica, sending a bunch of texts instead of one long one."
  jc "Oh yeah, the fan, i wanted it because the forecast said it was gonna be a hot weekend, and mine broke the other day."
  
  jc "BUT ANYWAYS! More importantly, i need to text her back."
  
  jc "Ok, i've picked \'Reply\', what should i type . . ."
  jc "Ill start with '/Help, i am a cat./'"
  jc "Bktdknk nhpjdj krz nhcragu"
  ". . ."
  jc "Stupid paws, its so hard to press only one letter, and the touch screen wont even pick up my claws, the one thing i have enough control to type properly with."
  jc "Never thought i'd say this, but right now i miss phones with buttons."
  
  jc "Hmm, Veronica mentioned an experiment. Could that be related to my current situation?"
  jc "Maybe I should go check her room and see if there are any clues?"
  
  
  $Livingroom1_PhoneCallHappened = True
  
  #jc "Lets get those keys then."
  call lbl_livingroom1_explore from _call_lbl_livingroom1_explore
  
  jump lbl_chapter2_Journal
    
label lbl_chapter2_Journal:
  $save_name = "Chapter 2: Journal"
  
  scene bg bedroom2
  
  #"*Read the journal here. Find out vague hints about the spell.*"
  jc "I feel a little bad about reading her Journal, but Veronica does all kinds of research for her writing, maybe she will have written something related to my current situation?"
  
  jc "Its a long shot, but honestly at this point I'll try anything."
  
  jc "I mean I'm not just snooping."
  
  jc "Its an emergency!"
  
  jc "Veronica will understand."
  
  "Having finally convinced herself that it was ok, given the circumstances she turned to the journal on the desk and started reading random pages in it."
  
  #TODO NVL style?
  nvl clear
  #journal
  #Cat alergies
  nvl clear
  journal "Clawdia is cute but i swear, every time she comes in my room i end up waking up feeling like absolute crap. It's not fun at all."
  jc "Honestly I feel really bad about that everytime it happens. I try my best to keep clawdia away from her room, but shes like a little ninja when she wants to be. "
  #Office
  nvl clear
  journal "Finally got my office redecorating done. Not sure why they thought i would need a security door in a basement office, but they didn't charge me for it so i guess it's ok."
  jc "Oh I remember that. I thinks she said she was doing some freelance work for some government and they needed it for her security clearance."
  jc "It was a bit wierd, but it's not like I ever really go into the basement so it never really bothered me."
  #Cat alergies
  nvl clear
  journal "Damn cat was in my room again. Jessica denies it, but my allergies don't lie. I need to get a lock or something for the door, its way too easy to just push open as it is."
  "Jessica grimaces after reading that passage and mouthes a quiet 'sorry'."
  #fan
  nvl clear
  journal "It was so hot today, whoever invented electric fans deserves a Nobel prize."
  jc "Preach!"
  #basement door
  nvl clear
  journal "The door to the basement seems to be busted, it wont stay closed. Swung open last night while we were watching a horror movie. Took an hour to convince Jess the basement wasn't haunted."
  jc "I swear to God. The timing was unnatural, perfectly matched up with the movie. I didn't sleep a wink for like 3 days."
  #Hairbrush
  nvl clear
  journal "Caught Jess using my hairbrush again. Use your own damn brush. Its bad enough that i sometimes catch the cat sleeping on it. Like how is that even comfortable?"
  jc "Only if I've left mine downstairs and don't want to go all the way down to get it. It's more efficient if i use the one thats already upstairs, right?"
  #Basementlock
  nvl clear
  journal "Finally got a lock for the basement, its a combination lock but i can't figure out how to change the combination. I rearranged the books in the living room to match the code, in case i forget it."
  jc "Oh I assumed it was a decor thing when you said not to move those books around. I guess i should take a closer look if i plan to get into the basement."
  #deadline/trouble sleeping
  nvl clear
  journal "Deadlines coming up. So much to do so little time. Doesn't help that I'm having trouble sleeping. Trying to write while tired suuuuucccckkkksss."
  jc "That explains why shes been looking so out of it lately. I figured it was probably deadline stress, but i didn't realize she wasn't sleeping either."
  #computer password
  nvl clear
  journal "Had to change my computer password again. Making a note here in case I forget it, again. Which I undoubtedly will."
  #TODO change password / hint? Current password is 5eronica
  journal "Note: My name but starting with a number instead of a roman numeral."
  jc "This would be much easier if she had just given the answer."
  #spell
  "Jessica flipped through a few more pages but nothing else jumped out as interesting until she came to what seemed to be the latest entries."
  nvl clear
  journal "Found something while researching for my book. Seems like a long shot but if it'll help me get a decent nights sleep at this point I'll try anything."
  jc "I don't think shes actually told me what her current book is about. She mostly talks to me about all the eligible bachelors her heroine could end up with. I wonder what she has been researching this time?"
  #Yay it worked
  nvl clear
  journal "It took a while to gather everything, but holy crap it worked. I haven't felt this well rested in a long time. Just in time for my trip too. I think I smudged some of the marks while i was putting things back though."
  journal "I've got the steps saved on my PC though so I'll try again when i get back and see if i can repeat the results."
  jc "Smudged the marks? I mean I'm glad it worked, but now I'm kinda curious what she was working on."
  
  "Jessica finished reading and turned away from the journal"
  
  jc "Maybe i should take a closer look at this research of hers and see if it really is related to whats happened to me."
  jc "I'm also a little curious as to what helped her to do a 180 in terms of her insomnia. Anything that good at helping you relax could come in handy."
  
  $Bedroom2_JournalRead = True
  jc "Guess I'll have to go to the basement after all."
  call lbl_bedroom2_explore from _call_lbl_bedroom2_explore
  
  jump lbl_chapter3_Basement
      
#-----------------------------------------------------------------------
label lbl_chapter3_Basement:
  $save_name = "Chapter 3: Basement"
  $chapter_section = "Basement"
  $chapter_number = "3"
  call lbl_chapter_select
  
  scene bg basement1
  "With the padlock removed the door slowly swings open on its own, a low creak sounding as it does."
  jc "Its not creepy, its just a busted door. Its not creepy."
  "Jessica reassured herself and carefully steps down the stairs to the basement. Each step feels so large for her little cat legs. "
  
  #"*Arrival in the basement*"
  jc "The basement is always so dark."
  "It's almost pitch black but luckily with her new found ability to see better in the dark its a lot less of a problem."
  jc "I probably wont be able to bring Clawdia down here without turning the lights on first. My body doesn't have cat vision and i don't want her falling and hurting herself (or my body)."
  "Theres a string switch at the top of the stairs, but its well out of reach for Jessica in her current state."
  jc "I don't really come down here much, ever since we agreed on the cooking/laundry split I don't even need to come down here to use the washing machines."
  "Basements were also kinda spooky in her opinion."
  jc "Victoria on the other hand practically lives down here, since her office is down here."
  jc "'Less distractions' she says."
  "Jessica shakes her head mockingly as she says it."
  
  $Basement1_Arrival = True
  jc "Anyways, lets see what we can find in here."
  call lbl_basement1_explore from _call_lbl_basement1_explore
  
  jump lbl_chapter3_Spider
    
label lbl_chapter3_Spider:
  $save_name = "Chapter 3: Spider"
  
  scene bg basement1
  
  #"*Find the spider*"
  #jc "NopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNopeNope."
  #
  #jc "I need to find a way to get rid of that {i}thing{/i} before i can continue."
  #Is that fluff?
  jc "Is that a bit of fluff? I guess i shouldnt expect the basement to be as clean as the rest of the house."
  "The 'bit of fluff' moves a little."
  jc "W-Wait. D-Did it move?"
  jc "Hahaha, probabaly just a breeze..."
  "Jessica laughs nervously"
  jc "...Except im underground, so there's nowhere for a breeze to come from."
  #nopenopenope
  "The 'bit of fluff' moves again, this time in a different direction."
  jc "NOPE. IM DONE. ITS A SPIDER."
  "Jessica runs upstairs and out of the basement."
  jc "If theres on thing I just can't stand It's spiders. I mean creepy-crawlies in general suck, but spiders are the absolute worst. So fast, so... so UGH. Even thinking about them makes my skin crawl."
  #need some help to get rid of it
  jump lbl_chapter3_Spider_options
label lbl_chapter3_Spider_options:
  jc "I need to get past it though so what am I supposed to do?"
  menu:
    "Wait it out":
      jc "I'll just wait for it to leave."
      jc "But what if it never leaves? What if I'm stuck as a cat forever because of some eight legged freak?!"
    "Get Help?":
      jump lbl_chapter3_Spider_help
    "Burn the house down":
      jc "I'll just burn the whole house down and move to a different city."
      jc "Or nuke it from orbit."
      jc "It's the only way to be sure."
      "After a long pause Jessica lets out a sigh."
      jc "Ok Maybe thats not really a good idea after all."
      
  jump lbl_chapter3_Spider_options

label lbl_chapter3_Spider_help:
  #-Get Help
  jc "Normally I'd ask Veronica to take care of things like this for me. "
  jc "But given my current predicament and the fact that shes going to be gone all weekend I'm going to have to figure a way out of this myself."
  jc "Maybe theres some way i can get clawdia to help out?"
  
  $Basement1_SpiderMet = True
  call lbl_basement1_explore from _call_lbl_basement1_explore_1
  
  ### Leadup from room.rpy
  #"As soon as the little red dot from the lazer pen catches her eye, Clawdias cat instincts kick in."
  #"As she starts the chase the dot the spider skitters away startled."
  #"The spiders movement catches her eye and she starts to chase it."
  #jc "YESSS. Get it Clawdia! My Hero! Stomp on it!"
  #"She pounces on the spider and cups her hands over it"
  #jc "Ew, omg dont touch it. I hope you squished it at least."
  #"Jessica shivers just thinking about the spider crawling around on her hands"
  #jc "Wait, what are you doing."
  #"Clawdia is holding her hands up to her face, staring intently into her cupped hands."
  #jc "C-Clawdia?"
  ###
  
  #"*Clawdia eats the spider*"
  jc "What are you doing? Please just get rid of it. I honestly can't stand the idea that its crawling around in my hands."
  "Jessica shivers all the way to her tail at the thought."
  "Clawdia however continues to watch the spider in her cupped hands very closely as it darts back and forth."
  jc "CLAWDIA?! Are you listeing to me?!"
  "Jessica meows loudly at Clawdia"
  cp "*nom*"
  "It all happens in an instant. Clawdia quickly chows down on the still moving spider."
  jc "Jessicas eyes widen in shock and she takes a few steps back"  
  
  $Basement1_SpiderAlive = False
  jc "OH MY GOD! I'm gonna throw up!"
  "Even just thinking about makes Jessica retch."
  jc "I can't believe you just -ugh."
  jc "With my mouth -ugh."
  "Jessica continued to retch at the thought for some time before she was able to compose herself again."
  "Clawdia, of course, was completely unfazed and played around with some drier lint that was on the floor, it was like she had forgotten there even was a spider once it was gone."
  
  jump lbl_chapter3_Spider_End
    
label lbl_chapter3_Spider_End:  
  scene bg basement1
  
  #"*Spider eaten*"
  jc "On the bright side, to what is now probably the worst day ever, at least I can explore the rest of the basement now. Lets see if we can find a way to fix me."
  jc "I don't know how much mouthwash I can gargle to fix this, but I'll be damned if i don't intend to find out once I get my body back."
  call lbl_basement1_explore
  
  jump lbl_chapter3_Instructions
label lbl_chapter3_Instructions:
  $save_name = "Chapter 3: Instructions"
  
  scene bg office
  call ShowOfficeWithChars
  
  "*Finding information in the Office PC*"
  call lbl_chapter3_MagicInstructions from _call_lbl_chapter3_MagicInstructions
  
  jc "I wonder if i can use this information to turn myself back?"
  
  jc "I should check out the boiler room before i worry about the other things."  
  call lbl_office_explore from _call_lbl_office_explore
    
  jump lbl_chapter4_Collection
  
label lbl_chapter3_MagicInstructions:
  
  show bg office_computer
  show office_computer_unlocked behind jessicat
  jc "Ok looks like it says:"
  "Beginners guide to spells and Magecraft."
  
  jc "Looks like there are 2 sections highlighted in the document: A spell called \'Astral Walk\' and some information on setting up a magic circle."
label lbl_chapter3_MagicInstructions_choice:
  #"*Spell instructions*"
  menu:
    "Which should i read about?"
    "Astral Walk spell":
      jump lbl_chapter3_MagicInstructions_spell
    "Magic Circle setup":
      jump lbl_chapter3_MagicInstructions_circle
    "I'm all done here":  
      $Office_MagicInstructionsFound = True
      hide bg_computer
      
      return
  
label lbl_chapter3_MagicInstructions_spell:
  jc "Here's the spell she highlighted. \'Astral Walk\'."
  jc "As far as i can tell it allows the user to take their spirit from their body to allow them to wander other realms."
  "Veronica seems to have highlighted a passage that implies it allows a restful sleep for the body while the spirit wanders."
  "It looks like the spell uses a magic circle like so."
  show magic_circle
  jc "It looks a little complex. Hope i don't need to draw one of these, as a cat it might take a while to do something this large."
  "Looks like theres certain runes or glyphs that can be used to give slightly different effects to the spell."
  jc "Veronica has highlighted a few already, i assume these were the ones she used."
  jc "There seem to be 4 important ones"
  hide magic_circle
  show sigil y4:
    xalign 0.5
    yalign 0.5
  jc "There is one that looks sort of like a y or a 4 and it says" 
  "\"Sirens Harp - Acts as a compass for wandering souls to guide them to and from peaceful realms if used while spirit walking.\""
  show sigil se
  jc "The one that looks sort of like a s and a backwards e " 
  "\"Edens Shield - Protects the caster from malicious spirits while the spell is in effect\""
  show sigil plant
  jc "The one that looks like a bug or a plant" 
  "\"Gaeas Jar - Captures wandering souls. Can be used to allow the return to the body when placed below a travelling glyph.\""
  show sigil deer
  jc "Then theres a complicated looking one, kinda looks like a deer with horns." 
  "\"Spirit Elk - When used as the main focus of the spell allows the soul of any being within the magic circle to leave the body and travel the spirit realm.\""
  
  jc "Theres also a handwritten note that says: \"As far as i can tell i should have the protection on the east and guidance to the west of the circle.\""
  
  jc "That seems to be all there is for this particular spell."
  
  jump lbl_chapter3_MagicInstructions_choice
  
label lbl_chapter3_MagicInstructions_circle:
  jc "So it looks like instructions for properly setting up a basic magic circle."
  jc "Seems that most magic circles follow the same basic setup, and then branch off with more specific details depending on the type of spell."
  jc "Looks like veronica has highlighted the following information:"
  
  "The following items will be needed for most basic Magic circles:"
  "Chalk - You will of course need to draw the circle, and chalk is normally used so that the circle can be changed to suit different spells or removed once the spell cast is complete."
  "Candles - Aligned at each of the power points on the Circle you have drawn. "
  "The number of candles will depend on the type of circle used, but it will typically be easy to tell how many you need."
  "Any points where the inner markings touch the outer circle tend to be the power points for the Magic circle."
  "Incense - Used to purify the area of any existing spell residue or energy and provide a clean space for the Magic to properly take effect."
  
  "There is also a list of various other objects that may be needed based on the spell being cast."
  jc "Its a long list but it looks like Veronica highlighted these ones:"
  "Hair - Can be used as a binding agent for certain spells. Used to keep the effects of a spell solely on the intended."
  "Token - Used to ground a participant to the current plane so they can find their way back. Mainly used for any spells where the spell caster would leave their body to travel to other realms or dimensions."
  jump lbl_chapter3_MagicInstructions_choice
  
#-----------------------------------------------------------------------
label lbl_chapter4_Collection:
  $save_name = "Chapter 4: Collection"
  $chapter_section = "Collection"
  $chapter_number = "4"
  call lbl_chapter_select
  
  call ShowBoilerroomWithChars
  
  "*Find the spell circle*"
  $Boilerroom_MagicCircleFound = True
  
  jc "I need to find all the things listed in the spell so i can fix this."  
  call lbl_boilerroom_explore from _call_lbl_boilerroom_explore
  
  jump lbl_chapter4_MagicSpell
    
label lbl_chapter4_MagicSpell:
  $save_name = "Chapter 4: MagicSpell"
  
  call ShowBoilerroomWithChars
  
  #Boiler - Spell effect
  "*Spell stuff happens here*"
  $Spell_Success = True
  call ShowBoilerroomWithChars
  
  jump lbl_chapter5_Ending
  
    
#-----------------------------------------------------------------------
label lbl_chapter5_Ending:
  $save_name = "Chapter 5: Ending"
  $chapter_section = "End?"
  $chapter_number = "5"
  call lbl_chapter_select
  
  call ShowBoilerroomWithChars
  #Ending
  "*Ending stuff happens here*"
  
  jp "I'm back to normal!"  
  
  jump lbl_chapter6_Epilogue
  
  
#-----------------------------------------------------------------------
label lbl_chapter6_Epilogue:
  $save_name = "Chapter 6: Epilogue"
  $chapter_section = "Epilogue"
  $chapter_number = "6"
  call lbl_chapter_select
  
  "*Possible Epilogue stuff happens here*"
  jump lbl_END
  
  
#-----------------------------------------------------------------------
label lbl_END:
  
  "*END*"
  return
  
#-----------------------------------------------------------------------
  
  
  
  
  
  
  
  