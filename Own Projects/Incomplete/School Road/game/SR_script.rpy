# The script of the game goes in this file.
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    #mc "You've created a new Ren'Py game."

    #mc "Once you add a story, pictures, and music, you can release it to the world!"

    
    $SetTime(8,0)
    show screen time_display(CurrentTime[0], CurrentTime[1])
    
    $count_Loops = 0
    $girl_following = False
    $boy_following = False
    
    $shouldRepeat = False
  
    $detour_choice = "None"
    $IsTimeStopped = False
    
    jump lbl_bedroom

    # This ends the game.
    return
    
# ------------------------------------------------------ #
label lbl_restart:
    $SetTime(8,0)
    show screen time_display(CurrentTime[0], CurrentTime[1])
    
    $count_Loops += 1
    $girl_following = False
    $boy_following = False
    
    $shouldRepeat = False
    $shouldEndEarly = False
  
    $breakfast_to_go_choice = "None"
    $detour_choice = "None"
    
    "Loop [count_Loops]"
    $IsTimeStopped = False
    
    jump lbl_bedroom
# ------------------------------------------------------ #

label lbl_bedroom:
    $SetLocation("Bedroom")
    #$timeStr = GetCurrentTimeString()
    #locationStr = GetLocation()
    #mc "It's [timeStr]. It's a [locationStr]"
    scene bg bedroom
    #scene bg bedroom grey
    
    call events_run_period from _call_events_run_period
    
    if (shouldEndEarly):
        jump lbl_restart
        

    jump lbl_kitchen
    return

label lbl_kitchen:
    $SetLocation("Kitchen")
    #$timeStr = GetCurrentTimeString()
    #$locationStr = GetLocation()
    #mc "It's [timeStr]. It's a [locationStr]"
    scene bg kitchen
    
    call events_run_period from _call_events_run_period_1
    
    if (shouldEndEarly):
        jump lbl_restart

    jump lbl_home
    return

label lbl_home:
    $SetLocation("Home")
    #$timeStr = GetCurrentTimeString()
    #$locationStr = GetLocation()
    #mc "It's [timeStr]. It's a [locationStr]"
    scene bg black
    
    call events_run_period from _call_events_run_period_2
    
    if (shouldEndEarly):
        jump lbl_restart

    jump lbl_intersection
    return

label lbl_intersection:
    $SetLocation("Intersection")
    #$timeStr = GetCurrentTimeString()
    #$locationStr = GetLocation()
    #mc "It's [timeStr]. It's a [locationStr]"
    scene bg intersection
    
    call events_run_period from _call_events_run_period_3
    
    if (shouldEndEarly):
        jump lbl_restart

    jump lbl_passage
    return

label lbl_passage:
    $SetLocation("Passage")
    #$timeStr = GetCurrentTimeString()
    #$locationStr = GetLocation()
    #mc "It's [timeStr]. It's a [locationStr]"
    scene bg passage
    
    #"before passage"
    call events_run_period from _call_events_run_period_4
    #"after passage"
    
    if (shouldEndEarly):
        jump lbl_restart

    jump lbl_detour
    return

label lbl_detour:
    #$SetLocation("Detour")
    #$timeStr = GetCurrentTimeString()
    #$locationStr = GetLocation()
    #mc "It's [timeStr]. It's a [locationStr]"
    scene bg passage
    
    #"before detour"
    #"location = [locationStr]"
    $SetLocation(locationStr)
    $locationStr2 = GetLocation()
    #"location = [locationStr2]"
    #"before detour2"
    call events_run_period from _call_events_run_period_5
    #"after detour"
    
    if (shouldEndEarly):
        jump lbl_restart

    jump lbl_passage_end
    return

label lbl_passage_end:
    $SetLocation("Passage_End")
    #$timeStr = GetCurrentTimeString()
    #$locationStr = GetLocation()
    #mc "It's [timeStr]. It's a [locationStr]"
    scene bg passage
    
    #"before passsage end"
    call events_run_period from _call_events_run_period_6
    
    if (shouldEndEarly):
        jump lbl_restart

    jump lbl_school
    return
    
label lbl_school:
    $SetLocation("School")
    #$timeStr = GetCurrentTimeString()
    #$locationStr = GetLocation()
    #mc "It's [timeStr]. It's a [locationStr]"
    scene bg schoolgate
    #scene bg schoolgate grey
    
    #"School_Arrive_On_Time_With_All"
    
    $loc = GetLocation()
    $past = IsTimePast([9,0])
    #"[loc] and count_Loops = [count_Loops] and isTimePast [past] and [girl_following] == girl and [boy_following] == boy"
    
    
    
    
    #"before school"
    call events_run_period from _call_events_run_period_7
    
    if (shouldEndEarly):
        jump lbl_restart

    if (shouldRepeat):
        jump lbl_restart
    else:
        jump lbl_END
        
    jump lbl_restart
    
    return
    
# ------------------------------------------------------ #

label lbl_END:
    "The End!"
    
    return
    
# ------------------------------------------------------ #