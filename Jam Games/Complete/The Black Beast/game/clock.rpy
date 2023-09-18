init:
  image clock = "clock/clock.png" # Short Clockhand
  image clock_1 = "clock/clock_1.png" # Long Clockhand
  image clock_2 = "clock/clock_2.png" # Clockface
  $CurrentRoute = 'good'
  
init python:
  minutes = 0
  # 12:00 MN - 0
  # 1:00  AM - 60
  # 2:00  AM - 120
  # 3:00  AM - 180
  # 4:00  AM - 240
  # 5:00  AM - 300
  # 6:00  AM - 360
  # 7:00  AM - 420
  # 8:00  AM - 480
  # 9:00  AM - 540
  # 10:00 AM - 600
  # 11:00 AM - 660
  # 12:00 NN - 720 
  # 1:00  PM - 780
  # 2:00  PM - 840
  # 3:00  PM - 900
  # 4:00  PM - 960
  # 5:00  PM - 1020
  # 6:00  PM - 1080
  # 7:00  PM - 1140
  # 8:00  PM - 1200
  # 9:00  PM - 1260
  # 10:00 PM - 1320
  # 11:00 PM - 1380

  TimerActive = True
  #timer_range = 60 #use this value for actual minutes
  timer_range = 1
  
  timer_limit = timer_range
  timer_jump = 'lbl_timePassed'
  
  timer_end_limit = 720
  
  def StopTimer():
    global TimerActive
    TimerActive = False
      
  def StartTimer():
    global TimerActive
    TimerActive = True
    
  def ResetTimer():
    global timer_limit
    timer_limit = timer_range
    StartTimer()
    
  def GetTime():  
    hours = minutes/60
    min = minutes%60
    return str(hours) + ":" + str(min).zfill(2)
  
transform rotateshort:
    xanchor 0.38
    yanchor 0.48
    xalign 0.38
    yalign 0.52
    rotate (minutes*6)
    
transform rotatelong:
    xanchor 0.38
    yanchor 0.48
    xalign 0.38
    yalign 0.52
    rotate (minutes*0.5)

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade in the clock.

screen pocketwatch:
    use pocketwatch_countdown
    frame: #at alpha_dissolve:
        background None
        foreground None
        xmaximum 150 # X size of clock graphic
        ymaximum 150 # Y size of clock graphic
        xalign 0.01 # X placement on screen
        yalign 0.9 # Y placement on screen
        add "clock_2"
        add "clock_1" at rotatelong
        add "clock" at rotateshort
        
        
screen pocketwatch_countdown:
    if TimerActive:
        if (minutes >= timer_end_limit and badpathdone) and CurrentRoute == 'bad':
            $ TimerActive = False            
            $ beatTimer = True  
            
        elif (minutes >= timer_end_limit and CurrentRoute == 'bad'):
            $ TimerActive = False
             
        else:
            timer 0.1 repeat True action If(timer_limit > 0, true=SetVariable('timer_limit', timer_limit - 0.1), false=[ Hide('pocketwatch_countdown'), Hide("pocketwatch"),  SetVariable('minutes', minutes + 1), Show("pocketwatch"),  SetVariable('timer_limit', timer_range), Play("audio", sound_tick)]) 
    #bar value timer_limit range timer_range xpos 790 ypos 300 xmaximum 442 at alpha_dissolve # This is the timer bar.
    #text "Time: [minutes]" xpos 720 ypos 300

    
