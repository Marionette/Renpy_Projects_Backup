
#############################################################################
label lbl_minigame_rhythm:
    
    scene bg black
    call lbl_minigame_rhythm_setup from _call_lbl_minigame_rhythm_setup
    call screen countdown2
    
    return
    
    
init:
    default DatingMinigameActive = False   
    $DatingTimerActive = True
    $timer2_limit = 1.0
    $timer2_range = 100.0
    $timer2_step = 1.0
    $timer2_direction = 1
    #Max speed dependant on number of steps as well as speed
    $timer2_speed = 1000 # 1.0/timer2_speed (minimum of 0.01 on timer)
    $timer2_result = -1
    $timer_jump = 'lbl_minigame_dating_timeout'
    
screen countdown2:

    add "gui/overlay/game_menu_r.png"
    style_prefix "dating"
    hbox:
      xpos 280
      ypos 580
      if DatingTimerActive:
          timer 1.0/timer2_speed repeat True action If(timer2_limit > 0 and timer2_limit < timer2_range, true=SetVariable('timer2_limit', timer2_limit - (timer2_step * timer2_direction)), false=[SetVariable('timer2_limit', timer2_limit + (timer2_step * timer2_direction)), SetVariable('timer2_direction', timer2_direction *-1), ])
      
      #text "Time:" xpos 50 ypos 50
      bar value timer2_limit range timer2_range xpos 0 ypos 0 xmaximum 704 ymaximum 30 top_bar "gui/slider/horizontal_idle_bar_r.png" left_bar "gui/slider/horizontal_idle_bar_r.png" right_bar "gui/slider/horizontal_idle_bar_r.png" thumb "gui/slider/horizontal_idle_thumb.png" thumb_offset 11 #at alpha_dissolve # This is the timer bar. 
      if DatingTimerActive:
          text "{size=-30}[timer2_limit]{/size}" xpos 30 ypos 10
    vbox:
      xpos 80
      ypos 555
      textbutton "Push!" action SetVariable('timer2_result',timer2_limit)
    
    vbox:
      xalign 0.5
      yalign 0.3
      $speed = 1.0/timer2_speed
      text "Speed [speed]"
      if timer2_result == -1:
        pass
      else:
        if timer2_result < 20 or timer2_result > 80:
          text "OK! [timer2_result]"
        else:
          if timer2_result < 35 or timer2_result > 65 :
            text "Fine! [timer2_result]"
          else:
            if timer2_result < 47 or timer2_result > 53:
              text "Good! [timer2_result]"
            else:
              if timer2_result >= 47 and timer2_result <= 53:
                text "PERFECT! [timer2_result]"
        

style dating_text is button_text:
    size 124
    color "#000000"
    #outlines [ (absolute(1), "#000000", absolute(1), absolute(1)) ]
    
style dating_button_text is button_text:
    size 84
    #color "#000000"
    #outlines [ (absolute(1), "#000000", absolute(1), absolute(1)) ]
        
label lbl_minigame_rhythm_setup:
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
    return
    
    
#############################################################################