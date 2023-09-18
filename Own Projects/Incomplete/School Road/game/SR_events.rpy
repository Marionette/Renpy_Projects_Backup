
    ## Loop Overviews
    #Loop_First - First Time awake - Limited options - destined to fail - impossible to reach school in time
    #Loop_Repeat - Second Time awake and onwards - more options - can reach school in time (should still reset time)
    #Loop_Spider - Next Time awake after reaching school on time - Meet Time spider
    #Loop_Repeat2 - Second Time awake and onwards - more options - can reach school in time

    
  #------------------------------------------------------
init:
    #$ event("cafe", "locationStr == 'Cafe'", event.only(), priority=200)
    #$ event("cafe_bad", "locationStr == 'Cafe'", priority=210)
    
    #$ event("cut1", "act == 'cut'", event.choose_one('cut'), priority=200)
    #$ event("cut2", "act == 'cut'", event.choose_one('cut'), priority=200)
    #$ event("fly", "act == 'fly'", event.solo(), priority=200)
    #$ event("study", "act == 'study'", event.solo(), priority=200)
    #$ event("hang", "act == 'hang'", event.solo(), priority=200)
    #$ event("exercise", "act == 'exercise'", event.solo(), priority=200)    
    #$ event("play", "act == 'play'", event.solo(), priority=200)
    
    
    # This is an introduction event, that runs once when we first go
    # to class. 
    #$ event("cafe_introduction", "locationStr == 'Cafe'", event.once(), event.only())
    
    
    #$ event("cafe_closed", "locationStr == 'Cafe' and IsLocationOpen(locationStr)", event.only())
    


    ##Wake Up Events
    #Wake_Up_First - only option is Snooze(10m)
    #Wake_Up_Repeat - Snooze(10m) or Get up(0m)
    #Wake_Up_Spider - Meet time spider - options to ask questions to find out more about your predicament
    #Wake_Up_Repeat2 - Snooze(10m) or Get up(0m) or Sleep In(100m)
    $ event("Wake_Up_First", "GetLocation() == 'Bedroom' and count_Loops == 0", event.once(), priority=200)
    $ event("Wake_Up_Repeat", "GetLocation() == 'Bedroom' and count_Loops > 0", event.solo(), priority=180)
    $ event("Wake_Up_Repeat2", "GetLocation() == 'Bedroom' and count_Loops > 0", event.solo(), event.happened("Wake_Up_Spider"), priority=170)
    $ event("Wake_Up_Spider", "GetLocation() == 'Bedroom' and count_Loops > 0", event.once(), event.happened("School_Arrive_On_Time_First"), priority=160)

    #Get_Ready - Get Ready(10m)

    ##Breakfast Events
    #Breakfast_First - Eat breakfast(10m) - choice of what to eat
    #Breakfast_Repeat - Skip(0m) or Eat breakfast(10m) - choice of what to eat
    #Breakfast_Repeat2 - Skip(0m) or Eat breakfast(10m) or Grab and run(0m)
    $ event("Breakfast_First", "GetLocation() == 'Kitchen' and count_Loops == 0", event.once(), priority=200)
    $ event("Breakfast_Repeat", "GetLocation() == 'Kitchen' and count_Loops > 0", event.solo(), priority=190)
    $ event("Breakfast_Repeat2", "GetLocation() == 'Kitchen' and count_Loops > 0", event.solo(), event.happened("Intersection_Collide"), priority=180)

    #Travel - From house to intersection
    $ event("Travel_HTI", "GetLocation() == 'House' and count_Loops >= 0", priority=200)

    ## Intersection events
    #if arrive within 20mins
    #Intersection_Collide - Crash into girl being chased by a dog -  fight off the dog(10m) or distract dog with toast Frisbee(0m). Help her calm down(10m) or leave her(0m).
    #if arrive after 20mins
    #Intersection_Girl_Crying - Help her calm down(10m) or leave her(0m).
    $ event("Intersection_Collide", "GetLocation() == 'Intersection' and not IsTimePast([8,20])", event.once(), priority=200)
    $ event("Intersection_Collide_Repeat", "GetLocation() == 'Intersection' and not IsTimePast([8,20])", event.solo(), event.happened("Intersection_Collide"), priority=200)
    $ event("Intersection_Crying", "GetLocation() == 'Intersection' and IsTimePast([8,20])", event.solo(), priority=190)


    #Travel - From intersection to street passage(10m)
    $ event("Travel_ITP", "GetLocation() == 'Intersection_End' and count_Loops >= 0", priority=200)

    ## Passage events
    #Passage_First - Push Through(100m) or Take a detour(20m) - Park or Side Streets
    #Passage_Repeat - Talk to Boy - Offer to help(20m), Push Through(100m), Take a detour(20m) - Park or Side Streets
    #Passage_Repeat_With_Girl - Offer to help(10m), Push Through(100m), Take a detour(20m) - Park or Side Streets
    $ event("Passage_First", "GetLocation() == 'Passage' and count_Loops == 0", event.once(), priority=200)
    $ event("Passage_Repeat", "GetLocation() == 'Passage' and count_Loops > 0", event.solo(), priority=190)
    #$ event("Passage_Repeat_With_Girl", "GetLocation() == 'Passage' and count_Loops > 0 and girl_following == True", event.happened("Intersection_Collide"), priority=180)

    ## Detour events
    #Detour_Park - Take a while to get through
    #Detour_Side_Streets - Get lost - Take a while to get through
    $ event("Detour_Park", "GetLocation() == 'Park'", event.solo(), priority=190)
    $ event("Detour_Side_Streets", "GetLocation() == 'Side_Streets'", event.solo(), priority=190)

    #Travel - From Passage/Detour to school(10m)
    $ event("Travel_PTS", "GetLocation() == 'Passage_End'", event.solo(), priority=210)

    ## School events
    #School_Arrive_Late_First - Restart day - Surprised
    #School_Arrive_Late_Repeat - Restart day - Worried
    #School_Arrive_Late_With_All - Restart day - Surprised
    #School_Arrive_On_Time_First - Restart day - Worried
    #School_Arrive_On_Time_Repeat - Restart day - Surprised
    #School_Arrive_On_Time_With_All - Continue Day - End
    $ event("School_Arrive_Late_First", "GetLocation() == 'School' and count_Loops == 0 and IsTimePast([9,0])", event.once(), priority=200)
    $ event("School_Arrive_Late_Repeat", "GetLocation() == 'School' and count_Loops > 0 and IsTimePast([9,0])", event.solo(), priority=190)
    $ event("School_Arrive_Late_With_All", "GetLocation() == 'School' and count_Loops > 0 and IsTimePast([9,0]) and girl_following == True and boy_following == True", event.solo(), priority=180)
    $ event("School_Arrive_On_Time_First", "GetLocation() == 'School' and not IsTimePast([9,0])", event.once(), priority=200)
    $ event("School_Arrive_On_Time_Repeat", "GetLocation() == 'School' and not IsTimePast([9,0])", event.solo(), event.happened("School_Arrive_On_Time_First"), priority=190)
    $ event("School_Arrive_On_Time_With_All", "GetLocation() == 'School' and count_Loops > 0 and not IsTimePast([9,0]) and girl_following == True and boy_following == True", priority=180)
    
  #------------------------------------------------------
  #------------------------------------------------------

label Breakfast_First:
    $locationStr = "Kitchen"
    $timeStr = GetCurrentTimeString()
    #mc "It's [timeStr]. It's a [locationStr]"
    #"Breakfast_First"
  
    #Breakfast_First - Eat breakfast(10m) - choice of what to eat
    menu:
        "Eat Breakfast":
            mc "Most important meal of the day!"
            call Breakfast_Eat from _call_Breakfast_Eat
    
    
    return
  #------------------------------------------------------
label Breakfast_Eat:
    mc "What should I eat for breakfast?"
    menu:
        "Cereal":
            "I grab a bowl of cereal and chow down."
        "Toast":
            "A grab a slice of toast out of the toaster and start munching."
        "Scrambled eggs":
            mc "Looks like mum made scrambled eggs before she went to work."
            "I help myself to some of the scrambled eggs in the pan."
        "Fruit":
            "I grab an apple from the fruit bowl and take a bite."
            mc "An apple a day keeps the doctor away."
        
    $AdvanceTimeMins(10)
    show screen time_display(CurrentTime[0], CurrentTime[1])
    
    "My hunger now satisfied I get ready to leave."
    
    return
  #------------------------------------------------------

label Breakfast_Repeat2:
    $locationStr = "Kitchen"
    $timeStr = GetCurrentTimeString()
    #mc "It's [timeStr]. It's a [locationStr]"
    #"Breakfast_Repeat2"
    
    #Breakfast_Repeat2 - Skip(0m) or Eat breakfast(10m) or Grab and run(0m)
    menu:
        "Eat Breakfast":
            call Breakfast_Eat from _call_Breakfast_Eat_1
        "Skip Breakfast":
            mc "I'll save some time if i skip breakfast."
        "Grab something and run":
            mc "Ill just grab something to go."
            menu:
                "Grab an apple":
                    "I grab an apple and head for the door"
                    $breakfast_to_go_choice = "apple"
                "Grab some Toast":
                    "I grab aslice of toast and head for the door"
                    "I resist the urge to put in in my mouth and run to school 'Anime' style."
                    $breakfast_to_go_choice = "toast"
                    
    return
  #------------------------------------------------------

label Breakfast_Repeat:
    $locationStr = "Kitchen"
    $timeStr = GetCurrentTimeString()
    #mc "It's [timeStr]. It's a [locationStr]"

    #"Breakfast_Repeat"    
    #Breakfast_Repeat - Skip(0m) or Eat breakfast(10m) - choice of what to eat
    menu:
        "Eat Breakfast":
            call Breakfast_Eat from _call_Breakfast_Eat_2
        "Skip Breakfast":
            mc "I'll save some time if I just skip breakfast."
            "I bypass the kitchen and head for the door."
            
    return
  #------------------------------------------------------
  #------------------------------------------------------

label Detour_Park:
    $locationStr = "Park"
    $timeStr = GetCurrentTimeString()
    scene bg park
    #mc "It's [timeStr]. It's a [locationStr]"
    #"Detour_Park"
    #Detour_Park - Take a while to get through
    "It took a while to get through the park."
    $AdvanceTimeMins(20)
    show screen time_display(CurrentTime[0], CurrentTime[1])
    
    return
  #------------------------------------------------------

label Detour_Side_Streets:
    $locationStr = "Side_Streets"
    $timeStr = GetCurrentTimeString()
    scene bg sidestreets
    #mc "It's [timeStr]. It's a [locationStr]"
    #"Detour_Side_Streets"
    #Detour_Side_Streets - Get lost - Take a while to get through
    "It took a while to get through the side streets."
    $AdvanceTimeMins(20)
    show screen time_display(CurrentTime[0], CurrentTime[1])
    
    return
  #------------------------------------------------------
  #------------------------------------------------------

label Intersection_Collide:
    $locationStr = "Intersection"
    $timeStr = GetCurrentTimeString()
    #mc "It's [timeStr]. It's a [locationStr]"
    #"Intersection_Collide"
    #if arrive within 20mins
    #Intersection_Collide - Crash into girl being chased by a dog -  fight off the dog(10m) or distract dog with toast Frisbee(0m). Help her calm down(10m) or leave her(0m).
    
    call Intersection_Collide_Collision from _call_Intersection_Collide_Collision
    
    $SetLocation("Intersection_End")
    return
  #------------------------------------------------------

label Intersection_Collide_Repeat:
    $locationStr = "Intersection"
    $timeStr = GetCurrentTimeString()
    #mc "It's [timeStr]. It's a [locationStr]"
    #"Intersection_Collide"
    #if arrive within 20mins
    #Intersection_Collide - Crash into girl being chased by a dog -  fight off the dog(10m) or distract dog with toast Frisbee(0m). Help her calm down(10m) or leave her(0m).
    
    mc "Well if this happens the same as last time then this is where I run into someone comming around the corner."
    
    menu:
        "Stop to let them pass.":
            call Intersection_Collide_Dodge from _call_Intersection_Collide_Dodge
        "Keep going.":
            "I brace myself for what comes next and maintain the same pace."
            call Intersection_Collide_Collision from _call_Intersection_Collide_Collision_1
    
    
    $SetLocation("Intersection_End")
    return
  #------------------------------------------------------
label Intersection_Collide_Dodge:
    "I stop just before i pass the corner, just in time to see the boy run straight through the space i would've been standing in."
    "The boy then tripped on a rock, falling uncerimoniously into a heap on the ground."
    
    menu:
        "Offer to help":
            call Intersection_Collide_Help from _call_Intersection_Collide_Help
        
        "Ignore":
            call Intersection_Crying_Ignore from _call_Intersection_Crying_Ignore
        
    return
    
label Intersection_Collide_Collision:
    "As i pass the corner someone runs straight into me and full speed, sending both of us rolling across the ground."
    
    "I take a moment to process what just happened and to assess any damage."
    
    mci "Shaken but not stirred."
    "I pick myself up with a groan, largly unhurt."
    
    "The other participant however is still curled up in a ball on the ground."
    
    "..."
    
    mci "Is he ok?"
    
    cg "*sniff*"
    
    mc "He seems to be crying. Is he hurt?"
    
    menu:
        "Offer to help":
            call Intersection_Collide_Help from _call_Intersection_Collide_Help_1
        
        "Ignore":
            call Intersection_Crying_Ignore from _call_Intersection_Crying_Ignore_1
    return
  #------------------------------------------------------
    
label Intersection_Collide_Help:
    "Are you hurt?"
    
    "The boy quickly sits up and wipes his face on his sleeve as if he wanted to pretend he wasn't just crying."
    
    cg "N-No, I-Im ok."
    
    "I hold out my hand to help him to his feet."
    
    mc "So wheres the fire?"
    
    cg "Huh?"
    
    mci "Has he not heard that one before, or is he just still out of it?"
    
    mc "Why were you in such a hurry? Running late?"
    
    cg "N-No, actually i..."
    
    "His voice trails off as his eyes widen."    
    
    mci "What the-"
    
    dog "WOOF!"
    
    "I turned around to find the source of the bark."
    
    dog "WOOF!!"
    mci "Its a small dog, judging from the wags of its tail this one is having fun."
    
    "I felt a light tug on my jacket."
    "It seems the boy had taken up refuge behind me."
    
    mci "Does he not like dogs?"
    mci "This one is about as threatening as a box of kittens though."
    
    cg "S-Stay away."
    
    "The dog starts to walk around me towards the boy, as he edges himself around me in the opposite direction."
    
    dog "WOOF!!!"
    
    "At this point the dogs tail was wagging so fast that i thought it might take off at any moment."
    
    mci "Was it following him? It definatly thinks they are playing a game."
    
    "After about two slow turns around me, the dog barks again and the boy starts running around me with the dog in tow."
    
    dog "WOOF!!! WOOF!!!"
    
    cg "STAY AWAY!!"
    
    "I should help the poor guy."
    
    $something_thrown = False
    
    if(breakfast_to_go_choice == "apple"):
        "I remember the apple in my pocket."
        mci "This is sorta ball shaped, maybe i can get it to chase it instead?"
        menu:
            "Throw the apple":
                $AdvanceTimeMins(20)
                $something_thrown = True
                "I shake the 'ball' in front of the dog to get his attention."
                dog "WOOF!"
                "He stops chasing the boy and turns his attention to me."
                "As soon as im sure the dog is fully focused on the apple i send it sailing down the street with the dog zooming after it."
                "Unfortunatly it doesnt take him long at all to turn back up and drop the apple at my feet, waiting for the next throw."
                mci "I may not have thought this all the way through."
                "It takes a handfull of throws before he stops comming back, maybe he found something else to play with."
                "It was probbaly for the best, the apple had gotten pretty gross, with the impacts and teeth marks leaving it a few throws away from being apple paste."
                "I rub the remaining alpple juice and dog slobber from may hands onto the sides of my trousers."
                "The boy watches me wipe off the mess and looks like he might lose his own breakfast in the process."
                mci "He must really not like dogs."
                show screen time_display(CurrentTime[0], CurrentTime[1])
            "Dont throw the apple":
                mci "I'd rather not waste my breakfast, its a long time till lunch."
                
    if(breakfast_to_go_choice == "toast"):
        "I remember the toast i grabbed at breakfast."
        mci "If i threw this like a frisbee, maybe i could get it to chase it instead?"
        menu:
            "Throw the toast":
                $AdvanceTimeMins(10)
                $something_thrown = True
                "I shake the 'frisbee' in front of the dog to get his attention."
                dog "WOOF!"
                "He stops chasing the boy and turns his attention to me."
                "As soon as im sure the dog is fully focused on the toast I send it sailing down the street with the dog zooming after it."
                "I managed to get a good flick of the wrist on it, because it sails even further than expected and its not long before the dog is out of sight."
                "Meanwhile the boy had stopped running and was gasping for breath with his hands on his knees."
                show screen time_display(CurrentTime[0], CurrentTime[1])
            "Dont throw the toast":
                mci "I'd rather not waste my breakfast, its a long time till lunch."
    
    if(not something_thrown):
        $AdvanceTimeMins(20)
        "I try to grab the dog, to hold it for long enough for the boy to get away, or at least catch his breath."
        "It turns out to be harder than expected, as the dog wriggles madly each time i try to get a grip."
        "After a few minutes i manage to grab a hold of of the dog."
        "The dog is unfazed and starts to lick my face as if rewarding me for a game well played."
        mc "Haha, cut it out."
        
        "Meanwhile the boy had stopped running and was gasping for breath with his hands on his knees."
        "We spend some more time at the intersection before a young girl finds us, me with the dog tucked happily under my arm."
        "We find out that his name was Mr Puddles, and he managed to slip out of his leash just as the boy was going past."
        "And as the dog started to follow him, the boy started to run away and thinking it a game the dog gave chase."
        "The girl thanks me for catching her dog and after securely leashing Mr Puddles the girl leaves."
        show screen time_display(CurrentTime[0], CurrentTime[1])
    
    
    call Intersection_Introduction from _call_Intersection_Introduction
    return
    
  #------------------------------------------------------
label Intersection_Introduction:
    cg "So you go to the same school as me right?"
    "The boy motions to our matching uniforms."
    
    mc "Oh, right. Im Martin Clarke, 2E"
    cg "My name is Charles Grove. Class 2D, but you can call me Charlie."
    $cg_name = "Charlie" 
    
    cg "Thanks for all your help."
    mc "No sweat, so i assume you're heading my way?"
    cg "Pardon?"
    mc "To school?"
    cg "Oh right of course, mind if i tag along with you?"
    mc "No problem. I'll protect you from anymore wild pooches."
    cg "...I-I would appreciate that."
    "I laugh awkwardly."
    mci "I said that as a joke, but i dont think he saw it that way."
    $boy_following = True
    
    return
  #------------------------------------------------------

label Intersection_Crying:
    $locationStr = "Intersection"
    $timeStr = GetCurrentTimeString()
    #mc "It's [timeStr]. It's a [locationStr]"
    #"Intersection_Crying"
    
    "Theres a guy sitting at the corner crying."
    #if arrive after 20mins
    #Intersection_Girl_Crying - Help her calm down(10m) or leave her(0m).
    
    menu:
        "Offer to help":
            call Intersection_Crying_Help from _call_Intersection_Crying_Help
        "Ignore":
            call Intersection_Crying_Ignore from _call_Intersection_Crying_Ignore_2
    
    
    $SetLocation("Intersection_End")
    return
  #------------------------------------------------------
label Intersection_Crying_Ignore:
    mc "I don't have time to deal with this."
    "I ignore the boy and continue on my way."
    
    return
    
label Intersection_Crying_Help:
    mc "Are you ok?"
    "*details of what happened*"
    
    "It takes a while to make out what hes saying through all the tears but eventually he manages to tell me about how he was 'attacked' by what as far as i could tell was an overly friendly dog."
    mci "He must really not like dogs."
    $AdvanceTimeMins(20)
    show screen time_display(CurrentTime[0], CurrentTime[1])
    "Eventually we both go leave together."
    
    call Intersection_Introduction from _call_Intersection_Introduction_1
    return
  #------------------------------------------------------
  #------------------------------------------------------

label Passage_First:
    $locationStr = "Passage"
    $timeStr = GetCurrentTimeString()
    #mc "It's [timeStr]. It's a [locationStr]"
    #"Passage_First"
    #Passage_First - Push Through(100m) or Take a detour(20m) - Park or Side Streets
    
    "There's an angry looking girl stopping people from passing through here."
    
    menu:
        "Push through.":
            call Passage_PushThrough from _call_Passage_PushThrough
        "Take a detour":
            call Passage_Detour from _call_Passage_Detour
    
    $SetLocation("Passage_End")
    return
  #------------------------------------------------------

label Passage_Repeat:
    $locationStr = "Passage"
    $timeStr = GetCurrentTimeString()
    #mc "It's [timeStr]. It's a [locationStr]"
    #"Passage_Repeat"
    
    #Passage_Repeat - Talk to Boy - Offer to help(20m), Push Through(100m), Take a detour(20m) - Park or Side Streets
    "There's an angry looking girl stopping people from passing through here."
    menu:
        "Talk to her.":
            call Passage_Talk from _call_Passage_Talk
            $SetLocation("Passage_End")
        "Push through.":
            call Passage_PushThrough from _call_Passage_PushThrough_1
        "Take a detour":
            call Passage_Detour from _call_Passage_Detour_1
    return
  #------------------------------------------------------

#label Passage_Repeat_With_Girl:
#    $locationStr = "Passage"
#    $timeStr = GetCurrentTimeString()
#    mc "It's [timeStr]. It's a [locationStr]"
#
#    "Passage_Repeat_With_Girl"
#    
#    #Passage_Repeat_With_Girl - Offer to help(10m), Push Through(100m), Take a detour(20m) - Park or Side Streets
#    return
    
  #------------------------------------------------------
label Passage_Talk:
    "You call her over and ask what the problem is."
    "Eventually she tells you she dropped her glasses and was stopping people from passing so they didn't step on them."
    
    if (boy_following):
        cg "P-Perhaps we can help you find them?"
        "Charlie nervously offers to help."
        "With the three of us it doesn't take long to find the glasses."
        $AdvanceTimeMins(10)
    else:
        "You offer to help her find them."
        "It takes a while but eventually you find them."
        $AdvanceTimeMins(20)
    
    show screen time_display(CurrentTime[0], CurrentTime[1])
    
    #Only take 10 mins with boy
    
    
    $girl_following = True
    return
    
label Passage_Detour:
    "I dont want to deal with this right now, i'll just go around."
    #$AdvanceTimeMins(10)
    
    menu:
        "Go through the Park":
            $locationStr = "Park"
            #$SetLocation("Park")
        "Take the side streets":
            $locationStr = "Side_Streets"
            #$SetLocation("Side_Streets")
    
    return
  
label Passage_PushThrough:
    "This girl doesnt own the street. Im just gonna push through."
    "She steps up as soon as I make to push through. I try to continue through but she pushes me back."
    
    "This continues for a while until she gets really pissed off and swings for me."
    "Everything starts to go black as my body crumples to the ground."
    $AdvanceTimeMins(100)
    scene bg black
    
    "..."
    
    $shouldEndEarly = True
    
    return
  #------------------------------------------------------
  #------------------------------------------------------

label School_Arrive_Late_First:
    $locationStr = "School"
    $timeStr = GetCurrentTimeString()
    #mc "It's [timeStr]. It's a [locationStr]"
    #"School_Arrive_Late_First"
    
    mci "Oh no, im late."
    scene bg schoolgate grey
    $IsTimeStopped = True
    #"...fail"
    "..."
    
    # Restart day and go to next loop
    $shouldRepeat = True
    
    return
  #------------------------------------------------------

label School_Arrive_Late_Repeat:
    $locationStr = "School"
    $timeStr = GetCurrentTimeString()
    #mc "It's [timeStr]. It's a [locationStr]"
    #"School_Arrive_Late_Repeat"
    
    mci "Oh no, im late again."
    scene bg schoolgate grey
    $IsTimeStopped = True
    #"...fail"
    "..."
    
    # Restart day and go to next loop
    $shouldRepeat = True
    
    return
  #------------------------------------------------------

label School_Arrive_Late_With_All:
    $locationStr = "School"
    $timeStr = GetCurrentTimeString()
    #mc "It's [timeStr]. It's a [locationStr]"
    #"School_Arrive_Late_With_All"
    
    mci "Oh no, we are all late."
    scene bg schoolgate grey
    $IsTimeStopped = True
    #"...fail"
    "..."
    
    # Restart day and go to next loop
    $shouldRepeat = True
    
    return
  #------------------------------------------------------

label School_Arrive_On_Time_First:
    $locationStr = "School"
    $timeStr = GetCurrentTimeString()
    #mc "It's [timeStr]. It's a [locationStr]"
    #"School_Arrive_On_Time_First"
    
    mci "Yes, i made it on time!"
    scene bg schoolgate grey
    $IsTimeStopped = True
    #"...fail"
    mci "What the hell?"
    "..."
    
    # Restart day and go to next loop
    $shouldRepeat = True
    
    return
  #------------------------------------------------------

label School_Arrive_On_Time_Repeat:
    $locationStr = "School"
    $timeStr = GetCurrentTimeString()
    #mc "It's [timeStr]. It's a [locationStr]"
    #"School_Arrive_On_Time_Repeat"
    
    mci "Yes, i made it on time!"
    scene bg schoolgate grey
    $IsTimeStopped = True
    #"...fail"
    mci "Again?"
    "..."
    
    # Restart day and go to next loop
    $shouldRepeat = True
    
    return
  #------------------------------------------------------

label School_Arrive_On_Time_With_All:
    $locationStr = "School"
    $timeStr = GetCurrentTimeString()
    #mc "It's [timeStr]. It's a [locationStr]"
    #"School_Arrive_On_Time_With_All"
    
    mci "Yes, we made it on time and together!"
    scene bg schoolgate
    #"...success"
    "..."
    "..."
    mc "Time is still going?!"
    cg "What?"
    mci "I didn't mean to say that out loud. They don't know what was happening."
    mci "It's probably better if it stays that way."
    mc "I mean, times a wasting. We better get to our classes."
    
    cg "Oh thats right!"
    
    "We all go our separate ways."
    
    # Stop repeat and go to ending
    $shouldRepeat = False
    
    return
  #------------------------------------------------------
  #------------------------------------------------------

label Travel_HTI:
    $locationStr = "Home"
    $timeStr = GetCurrentTimeString()
    #mc "It's [timeStr]. It's a [locationStr]"

    #"Travel_HTI"
    "I travel from my house to a nearby intersection."
    $AdvanceTimeMins(10)
    show screen time_display(CurrentTime[0], CurrentTime[1])
    
    return
  #------------------------------------------------------

label Travel_ITP:
    $locationStr = "Intersection_End"
    $timeStr = GetCurrentTimeString()
    #mc "It's [timeStr]. It's a [locationStr]"
    #"Travel_ITP"
    "I travel from the intersection to a passage that leads to the school."
    $AdvanceTimeMins(10)
    show screen time_display(CurrentTime[0], CurrentTime[1])
    
    return
  #------------------------------------------------------

label Travel_PTS:
    $locationStr = "Passage_End"
    $timeStr = GetCurrentTimeString()
    #mc "It's [timeStr]. It's a [locationStr]"
    #"Travel_PTS"
    "I travel from the end of the passage to the school."
    $AdvanceTimeMins(10)
    show screen time_display(CurrentTime[0], CurrentTime[1])
    
    return
  #------------------------------------------------------
  #------------------------------------------------------

label Wake_Up_First:
    $SetLocation("Bedroom")
    $timeStr = GetCurrentTimeString()
    $locationStr = GetLocation()
    #mc "It's [timeStr]. It's a [locationStr]"
    #"Wake_Up_First"
    
    mc "Its only 8am. I still have time."
    
    menu:
        "Hit Snooze":
            call Wake_Up_Snooze from _call_Wake_Up_Snooze
    
    call Wake_Up_GetReady_Relaxed from _call_Wake_Up_GetReady_Relaxed
    
    return
  #------------------------------------------------------
  
label Wake_Up_Snooze:
    "I hit snooze and roll back over for a few more minutes in bed before I get up for school."
    $AdvanceTimeMins(10)
    show screen time_display(CurrentTime[0], CurrentTime[1])
    
    "..."
    
    "*Beep Beep*"
    mci "Guess i better get up then."
    
    return
  
label Wake_Up_Sleep:
    mci "Well if the day is just going to repeat anyways, i might as well make the most of it."
    "I turn off the alarm and roll over. Curled up in the blanket i drift off into a deep sleep."
    $AdvanceTimeMins(100)
    
    scene bg black
    "..."
    
    $shouldEndEarly = True
    
    return
    
  #------------------------------------------------------
label Wake_Up_GetReady_Relaxed:
    "I drag myself out of bed with a groan and head to the bathroom to wash my face."
    jump Wake_Up_GetReady
    
label Wake_Up_GetReady_Rushed:
    "I jump out of bed and head to the bathroom."
    jump Wake_Up_GetReady
    
label Wake_Up_GetReady:
    "I throw on my uniform and head to the kitchen for breakfast."
    $AdvanceTimeMins(10)
    show screen time_display(CurrentTime[0], CurrentTime[1])
    
    return
  #------------------------------------------------------

label Wake_Up_Repeat2:
    $SetLocation("Bedroom")
    $timeStr = GetCurrentTimeString()
    $locationStr = GetLocation()
    show martin normal
    #mc "It's [timeStr]. It's a [locationStr]"
    #"Wake_Up_Repeat2"
    
    if (count_Loops > 2):
        mc sad "Am i doing something wrong?"
        mc "Do i need to make it to school in time to break the loop?"
        show bg bedroom grey
        show moirai angry:
            yalign -1.0
            xalign 0.8
        ts "I already explained it to you."
        mc surprise "AHH!"
        mc angry "Don't sneak up on me like that."
        show moirai normal
        ts "Like I said before, you need to untangle your threads by having all crossing points pass the thrshold together."
    
        hide moirai
        show bg bedroom
    menu:
        "Hit Snooze":
            call Wake_Up_Snooze from _call_Wake_Up_Snooze_1
            call Wake_Up_GetReady_Relaxed from _call_Wake_Up_GetReady_Relaxed_1
        "Get Up":
            "I turn off the alarm and jump out of bed."
            call Wake_Up_GetReady_Rushed from _call_Wake_Up_GetReady_Rushed
        "Go back to sleep":
            call Wake_Up_Sleep from _call_Wake_Up_Sleep
    
    return
  #------------------------------------------------------

label Wake_Up_Repeat:
    $SetLocation("Bedroom")
    $timeStr = GetCurrentTimeString()
    $locationStr = GetLocation()
    #mc "It's [timeStr]. It's a [locationStr]"
    #"Wake_Up_Repeat"
    
    if (count_Loops == 1):
        mc "Huh? Was that a dream? It felt so real."
    else :
        mc "Ok, what the heck is going on?!"
        
    if (count_Loops > 2):
        mc "Am i doing something wrong?"
        mc "Do i need to make it to school in time to break the loop?"
    
    menu:
        "Hit Snooze":
            call Wake_Up_Snooze from _call_Wake_Up_Snooze_2
            call Wake_Up_GetReady_Relaxed from _call_Wake_Up_GetReady_Relaxed_2
        "Get Up":
            "I turn off the alarm and jump out of bed."
            call Wake_Up_GetReady_Rushed from _call_Wake_Up_GetReady_Rushed_1
    
    return
  #------------------------------------------------------

label Wake_Up_Spider:
    $SetLocation("Bedroom")
    $timeStr = GetCurrentTimeString()
    $locationStr = GetLocation()
    #mc "It's [timeStr]. It's a [locationStr]"
    #"Wake_Up_Spider"
    
    $asked_q1 = False
    $asked_q2 = False
    $asked_q3 = False    
    $asked_q4 = False
    $asked_q5 = False
    $asked_q6 = False
    $asked_q7 = False
    $asked_q8 = False
    
    scene bg bedroom grey
    show martin normal
    $IsTimeStopped = True
    
    #Realize time is stopped (everything gray?)
    #"Time is stopped"
    mci "Whats going on? Everything is so quiet. Unnaturally so."
    
    #Spider speaks to you.
    show moirai sad:
        yalign -0.0
        xalign 0.8
    ts "How did you manage to get stuck like this?"
    show moirai normal
    
    mc "AHH!!!"
    
label Wake_Up_Spider_q1:
    #Choice: a. Who are you? / b. What do you want? / c. What is going on? (repeat choice until all options picked)
    #a. Spider explains who she is
    #b. Spider explains what she wants
    #c. Spider explains what is happening now
    
    menu:
        "Who are you?" if not asked_q1:
            $asked_q1 = True
            ts "Nobody important. I just spin the threads of fate."
            mc "Fate? Are you god?"
            ts "Haha no, nothing as lofty as that, i just try to keep things moving."
            mc "..."
            ts "If it will make it easier on you then you can just call me Moirai."
            $ts_name = "Moirai"
        "What do you want?"if not asked_q2:
            $asked_q2 = True
            ts"I want to help. You've made a mess somehow and unless i help you out of it we'll both be stuck here repeating this section of time forever."
        "What is going on?"if not asked_q3:
            $asked_q3 = True
            ts"Well you're stuck in this portion of time. I assumed you had realised that by now."
            mc angry "I mean why"
            
    if (not(asked_q1 and asked_q2 and asked_q3)):
        jump Wake_Up_Spider_q1
        
    mc "So uhh...Moirai."
    "I struggle as i try to process what is going on."
    
label Wake_Up_Spider_q2:
    #Choice: a. Are you the reason im stuck in this loop? / b.Why is this happening? 
    #a. Not my fault
    #b. These things happen from time to time.
    #explain the loop and the ties to others.
    menu:
        "Are you the reason im stuck in this loop?"if not asked_q4:
            $asked_q4 = True
            ts "No i am not to blame for your current predicament."
        "Why is this happening?"if not asked_q5:
            $asked_q5 = True
            ts "You've somehow become entangled with some other threads and this entanglment means you cannot progress further through time."

    if (not(asked_q4 and asked_q5)):
        jump Wake_Up_Spider_q2
        
label Wake_Up_Spider_q3:
    #Choice: a. How do i get out of this loop? / b. Can you help me?
    #a. go to explanation
    #b. not directly, i cant interfere too much. go to explanation
    menu:
        "How do i get out of this loop?"if not asked_q6:
            $asked_q6 = True
            pass
        "Can you help me?"if not asked_q7:
            $asked_q7 = True
            ts"Not directly, I can only offer wisdom. You will have to solve this yourself."

    if (not asked_q6):
        jump Wake_Up_Spider_q3
        
    #explanation. Explains what is needed to break the loop.
    "*Full Explanation here*"
    ts "Basically, you need to untangle your threads by having all crossing points pass the thrshold together."
    
    
    scene bg bedroom
    "The alarm resumes its buzzing as time starts to move again."
    
    menu:
        "Get Up":
            mc "I better go get ready for school then."
            "I turn off the alarm and jump out of bed."
            call Wake_Up_GetReady_Rushed from _call_Wake_Up_GetReady_Rushed_2
    
    return
  #------------------------------------------------------
