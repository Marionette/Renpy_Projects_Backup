
#############################################################################
label lbl_minigame_dating:
    
    scene bg OutsideCafe
    call lbl_minigame_dating_setup from _call_lbl_minigame_dating_setup
    show screen countdown
    
label lbl_minigame_dating_questions:
    $questionsleft = len(Uquestion_list)
    
    narrator_d "There are [questionsleft] questions left."
    call lbl_minigame_dating_UQuestion_Ask from _call_lbl_minigame_dating_UQuestion_Ask
    
    narrator_d "Current score is [minigame_dating_score]"
    if (minigame_questions_answered < minigame_questions_total):
        jump lbl_minigame_dating_questions
    else:
        call lbl_minigame_dating_questions_complete from _call_lbl_minigame_dating_questions_complete

return

label lbl_minigame_dating_UQuestion_Ask:
    umeko_d "Uquestion ask"
    $question = renpy.random.choice(Uquestion_list)
    
    menu:
        umeko_d "[question[0]]"
        "[question[1][0]]":
            call expression question[1][1] from _call_expression
        "[question[2][0]]":
            call expression question[2][1] from _call_expression_1
        "[question[3][0]]":
            call expression question[3][1] from _call_expression_2
            
    $minigame_questions_answered +=1
    # Remove question from the list
    $Uquestion_list.remove(question)

return

label lbl_minigame_dating_EQuestion_Ask:

    eiichi_d "Equestion ask"
    $question1 = renpy.random.choice(Equestion_list)
    $question2 = renpy.random.choice(Equestion_list)
    $question3 = renpy.random.choice(Equestion_list)
    menu:
        eiichi_d "What should i ask?"
        "[question1[0]]":
            call expression question1[1] from _call_expression_3
        "[question2[0]]":
            call expression question2[1] from _call_expression_4
        "[question3[0]]":
            call expression question3[1] from _call_expression_5
        
return


label lbl_minigame_dating_UQuestion_answer_good:
    $minigame_dating_score += minigame_score_large
    show screen successful_answer
    narrator_d "She liked that answer."
    hide screen successful_answer
return


label lbl_minigame_dating_UQuestion_answer_neutral:
    $minigame_dating_score += minigame_score_medium
    narrator_d "She didn't seem to care much about that answer."
return

label lbl_minigame_dating_UQuestion_answer_bad:
    
    $minigame_dating_score += minigame_score_small
    narrator_d "She did not like that answer."
    narrator_d "You better make it up with a question of your own."
    call lbl_minigame_dating_EQuestion_Ask from _call_lbl_minigame_dating_EQuestion_Ask
    
        
return

label lbl_minigame_dating_questions_complete:
    narrator_d "You answered all the questions."
    call lbl_minigame_dating_score from _call_lbl_minigame_dating_score
        
return

label lbl_minigame_dating_timeout:
    narrator_d "You ran out of time."
    call lbl_minigame_dating_score from _call_lbl_minigame_dating_score_1
        
return
    
label lbl_minigame_dating_score:
    if minigame_dating_score >= minigame_score_max:
        $minigame_result_route = 2        
    elif minigame_dating_score > (minigame_score_max / 2):
        $minigame_result_route = 1
    else:
        $minigame_result_route = 0
    
    narrator_d "Your result is route [minigame_result_route]"
    $DatingMinigameActive = False
    hide screen countdown
    hide screen lovemeter
    hide screen successful_answer
        
return
    
#############################################################################   
init:
    default DatingMinigameActive = False   
    $DatingTimerActive = True
    $timer_limit = 300
    $timer_range = 300
    $timer_jump = 'lbl_minigame_dating_timeout'
      
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script
    
screen countdown:
    style_prefix "dating"
    hbox:
      xpos 45
      ypos 34
      if DatingTimerActive:
          timer 0.1 repeat True action If(timer_limit > 0, true=SetVariable('timer_limit', timer_limit - 0.1), false=[ Hide('countdown'), Jump(timer_jump)])
          #$timerInt = int(timer_limit)
          $minutes = int(timer_limit/60)
          $seconds = int(timer_limit%60)
      
      #text "Time:" xpos 50 ypos 50
      bar value timer_limit range timer_range xpos 0 ypos 0 xmaximum 601 ymaximum 52 top_bar "gui/slider/horizontal_hover_bar_dating.png" left_bar None right_bar None thumb None at alpha_dissolve # This is the timer bar. 
      if DatingTimerActive:
          text "{size=-30}[minutes:02]:[seconds:02]{/size}" xpos 30 ypos 10
    
      
    
screen lovemeter:
    add "gui/datingbars_base.png"
    #vbar value 50 range 100 xmaximum 222  ymaximum 600  top_bar "gui/slider/vertical_hover_bar.png" left_bar None right_bar None thumb None at alpha_dissolve
    vbar value (minigame_score_max - minigame_dating_score) range minigame_score_max xmaximum 222 ymaximum 600 ypos 500 bar_invert True base_bar "gui/slider/love_bar.png" left_bar None right_bar None thumb "gui/slider/love_bar_thumb.png" thumb_offset 42 at alpha_dissolve
    style_prefix "dating"
    vbox:
      text "[minigame_dating_score]" xpos 150 ypos 400 
      #text "0123456789" xpos 150 ypos 380 

#style dating_vbox is button_text

style dating_text is button_text:
    size 124
    color "#ffffff"
    outlines [ (absolute(1), "#000000", absolute(1), absolute(1)) ]
    
screen successful_answer:
    add "gui/dating_chibi.png" at chibihop
        
label lbl_minigame_dating_setup:
    "Setup"
    $DatingMinigameActive = True
    $minigame_dating_score = 0
    $minigame_questions_answered = 0
    $minigame_questions_total = 3
    $minigame_result_route = 0
    
    $minigame_score_small = 1
    $minigame_score_medium = 5
    $minigame_score_large = 10
    $minigame_score_max = (minigame_score_large * minigame_questions_total)
    show screen lovemeter
    
    python:
        #start timer for 5 mins
        #Answer_State = "None", "Correct", "Incorrect"
        UQuestion_1 = ["UQuestion1", ["Answer1", "lbl_uq1_answer1"], ["Answer2", "lbl_uq1_answer2"], ["Answer3", "lbl_uq1_answer3"]]
        UQuestion_2 = ["UQuestion2", ["Answer1", "lbl_uq2_answer1"], ["Answer2", "lbl_uq2_answer2"], ["Answer3", "lbl_uq2_answer3"]]
        UQuestion_3 = ["UQuestion3", ["Answer1", "lbl_uq3_answer1"], ["Answer2", "lbl_uq3_answer2"], ["Answer3", "lbl_uq3_answer3"]]
        #UQuestion_4 = ["UQuestion4", ["Answer1", "lbl_uq4_answer1"], ["Answer2", "lbl_uq4_answer2"], ["Answer3", "lbl_uq4_answer3"]]
        #UQuestion_5 = ["UQuestion5", ["Answer1", "lbl_uq5_answer1"], ["Answer2", "lbl_uq5_answer2"], ["Answer3", "lbl_uq5_answer3"]]
        #UQuestion_6 = ["UQuestion6", ["Answer1", "lbl_uq6_answer1"], ["Answer2", "lbl_uq6_answer2"], ["Answer3", "lbl_uq6_answer3"]]
        #UQuestion_7 = ["UQuestion7", ["Answer1", "lbl_uq7_answer1"], ["Answer2", "lbl_uq7_answer2"], ["Answer3", "lbl_uq7_answer3"]]
        #UQuestion_8 = ["UQuestion8", ["Answer1", "lbl_uq8_answer1"], ["Answer2", "lbl_uq8_answer2"], ["Answer3", "lbl_uq8_answer3"]]
        #UQuestion_9 = ["UQuestion9", ["Answer1", "lbl_uq9_answer1"], ["Answer2", "lbl_uq9_answer2"], ["Answer3", "lbl_uq9_answer3"]]
        #UQuestion_10 = ["UQuestion10", ["Answer1", "lbl_uq10_answer1"], ["Answer2", "lbl_uq10_answer2"], ["Answer3", "lbl_uq10_answer3"]]
        
        EQuestion_1 = ["EQuestion1", "lbl_eq_question1"]
        EQuestion_2 = ["EQuestion2", "lbl_eq_question2"]
        EQuestion_3 = ["EQuestion3", "lbl_eq_question3"]
        #EQuestion_4 = ["EQuestion4", "lbl_eq_question4"]
        #EQuestion_5 = ["EQuestion5", "lbl_eq_question5"]
        #EQuestion_6 = ["EQuestion6", "lbl_eq_question6"]
        #EQuestion_7 = ["EQuestion7", "lbl_eq_question7"]
        #EQuestion_8 = ["EQuestion8", "lbl_eq_question8"]
        #EQuestion_9 = ["EQuestion9", "lbl_eq_question9"]
        #EQuestion_10 = ["EQuestion10", "lbl_eq_question10"]
        
        
        
        
        Uquestion_list = [  UQuestion_1,
                            UQuestion_2,
                            UQuestion_3,
                            #UQuestion_4,
                            #UQuestion_5,
                            #UQuestion_6,
                            #UQuestion_7,
                            #UQuestion_8,
                            #UQuestion_9,
                            #UQuestion_10
                            ]
        
        Equestion_list = [  EQuestion_1,
                            EQuestion_2,
                            EQuestion_3,
                            #EQuestion_4,
                            #EQuestion_5,
                            #EQuestion_6,
                            #EQuestion_7,
                            #EQuestion_8,
                            #EQuestion_9,
                            #EQuestion_10
                            ]
    return
    
    
#############################################################################

#--------------------------------
# UQuestion 1
#--------------------------------
label lbl_uq1_answer1:
    
    narrator_d "You chose answer 1."
    call lbl_minigame_dating_UQuestion_answer_good from _call_lbl_minigame_dating_UQuestion_answer_good
    return
#--------------------------------
label lbl_uq1_answer2:
    
    narrator_d "You chose answer 2."
    call lbl_minigame_dating_UQuestion_answer_bad from _call_lbl_minigame_dating_UQuestion_answer_bad
    return
#--------------------------------
label lbl_uq1_answer3:
    
    narrator_d "You chose answer 3."
    call lbl_minigame_dating_UQuestion_answer_neutral from _call_lbl_minigame_dating_UQuestion_answer_neutral
    return
#--------------------------------

#--------------------------------
# UQuestion 2
#--------------------------------
label lbl_uq2_answer1:
    
    narrator_d "You chose answer 1."
    call lbl_minigame_dating_UQuestion_answer_bad from _call_lbl_minigame_dating_UQuestion_answer_bad_1
    return
#--------------------------------
label lbl_uq2_answer2:
    
    narrator_d "You chose answer 2."
    call lbl_minigame_dating_UQuestion_answer_good from _call_lbl_minigame_dating_UQuestion_answer_good_1
    return
#--------------------------------
label lbl_uq2_answer3:
    
    narrator_d "You chose answer 3."
    call lbl_minigame_dating_UQuestion_answer_neutral from _call_lbl_minigame_dating_UQuestion_answer_neutral_1
    return
#--------------------------------

#--------------------------------
# UQuestion 3
#--------------------------------
label lbl_uq3_answer1:
    
    narrator_d "You chose answer 1."
    call lbl_minigame_dating_UQuestion_answer_neutral from _call_lbl_minigame_dating_UQuestion_answer_neutral_2
    return
#--------------------------------
label lbl_uq3_answer2:
    
    narrator_d "You chose answer 2."
    call lbl_minigame_dating_UQuestion_answer_bad from _call_lbl_minigame_dating_UQuestion_answer_bad_2
    return
#--------------------------------
label lbl_uq3_answer3:
    
    narrator_d "You chose answer 3."
    call lbl_minigame_dating_UQuestion_answer_good from _call_lbl_minigame_dating_UQuestion_answer_good_2
    return
#--------------------------------

#############################################################################

#--------------------------------
# EQuestions
#--------------------------------
label lbl_eq_question1:
    
    narrator_d "You chose to ask question 1."
    return
#--------------------------------
label lbl_eq_question2:
    
    narrator_d "You chose to ask question 2."
    return
#--------------------------------
label lbl_eq_question3:
    
    narrator_d "You chose to ask question 3."
    return
#--------------------------------

#############################################################################