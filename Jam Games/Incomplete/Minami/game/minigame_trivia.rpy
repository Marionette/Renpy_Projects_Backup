
#############################################################################   
                        
init: 
        
  transform flash_effect:
      alpha 0.0
      linear 0.2 alpha 1.0
      linear 0.2 alpha 0.0
      #linear 3.0 matrixcolor HueMatrix(200)
      #linear 3.0 matrixcolor HueMatrix(300)
      repeat 5
    
#############################################################################   
init python:

    #######################################################
    def debug_print(_msg):
      return # comment out to print debug messages
      with open("F:\[Projects]\RenpyGames\Minami\game\log.txt", "a") as myfile:
        myfile.write(_msg)
        myfile.write("\n")
    #######################################################

    active_squares = [   [0,0,0,0,0,0],
                         [0,0,0,0,0,0],
                         [0,0,0,0,0,0],
                         [0,0,0,0,0,0],
                         [0,0,0,0,0,0],
                         [1,1,1,1,1,1]]
                         

    def isActive(x, y):
        return active_squares[x][y] == 1

    def isSuccess(x, y):
        return active_squares[x][y] == 'A'

    def isFail(x, y):
        return active_squares[x][y] == 'X'
    
    def setSurroundingActive(x, y):
        #active_squares[x][y] = 1
        if (x > 0):
            if (active_squares[x-1][y] == 0):
                active_squares[x-1][y] = 1
        if (x < 5):
            if (active_squares[x+1][y] == 0):
                active_squares[x+1][y] = 1
        if (y > 0):
            if (active_squares[x][y-1] == 0):
                active_squares[x][y-1] = 1
        if (y < 5):
            if (active_squares[x][y+1] == 0):
                active_squares[x][y+1] = 1
        return
    
    def setSuccess(x, y):
        global minigame_trivia_win
        if x == 0:
            minigame_trivia_win = True
        active_squares[x][y] = 'A'
        setSurroundingActive(x,y)
        return
    
    def setFail(x, y):
        active_squares[x][y] = 'X'
        return
    
    def hasLost():
        lose = True
        
        path_blocked = [True, True, True, True, True, True]
        for x in range(6):
          for y in range(6):
            debug_print("active_squares[" + str(y) + "][" + str(x) + "] = " + str(active_squares[y][x]))
            if active_squares[y][x] == 1:
              path_blocked[x] = False
              break
            else:
              if active_squares[y][x] == 'X':
                path_blocked[x] = True
                break
                  
        if False in path_blocked:
            lose = False
            
        return lose

# ---------------------------------------------------------------------------
              
    
    #Question_x_y = ["Question Text", correct answer position, "Answer text 1", "Answer text 2", "Answer text 3", 
    Question_test = ["There are 4 words that end in \"gry\" in the dictionary.\nWhat is the last 4th discovered word?", 4, "Hungry", "Angry", "Hangry", "Mungry"] 
    
    
    Question_0_0 = ["Question Text 0_0", 1, "Answer option 1", ] 
    Question_0_1 = ["Question Text 0_1", 1, "Answer option 1", "Answer option 2", ] 
    Question_0_2 = ["Question Text 0_2", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_0_3 = ["Question Text 0_3", 1, "Answer option 1", "Answer option 2", "Answer option 3", "Answer option 4"] 
    Question_0_4 = ["Question Text 0_4", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_0_5 = ["Question Text 0_5", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
                                   
    Question_1_0 = ["Question Text 1_0", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_1_1 = ["Question Text 1_1", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_1_2 = ["Question Text 1_2", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_1_3 = ["Question Text 1_3", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_1_4 = ["Question Text 1_4", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_1_5 = ["Question Text 1_5", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
                                   
    Question_2_0 = ["Question Text 2_0", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_2_1 = ["Question Text 2_1", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_2_2 = ["Question Text 2_2", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_2_3 = ["Question Text 2_3", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_2_4 = ["Question Text 2_4", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_2_5 = ["Question Text 2_5", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
                                   
    Question_3_0 = ["Question Text 3_0", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_3_1 = ["Question Text 3_1", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_3_2 = ["Question Text 3_2", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_3_3 = ["Question Text 3_3", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_3_4 = ["Question Text 3_4", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_3_5 = ["Question Text 3_5", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
                                   
    Question_4_0 = ["Question Text 4_0", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_4_1 = ["Question Text 4_1", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_4_2 = ["Question Text 4_2", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_4_3 = ["Question Text 4_3", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_4_4 = ["Question Text 4_4", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
    Question_4_5 = ["Question Text 4_5", 1, "Answer option 1", "Answer option 2", "Answer option 3"] 
                                   
    Question_5_0 = ["Question Text 5_0", 1, "Answer option 1a", "Answer option 2", "Answer option 3"] 
    Question_5_1 = ["Question Text 5_1", 2, "Answer option 1", "Answer option 2a", "Answer option 3"] 
    Question_5_2 = ["Question Text 5_2", 3, "Answer option 1", "Answer option 2", "Answer option 3a"] 
    Question_5_3 = ["Question Text 5_3", 1, "Answer option 1a", "Answer option 2", "Answer option 3"] 
    Question_5_4 = ["Question Text 5_4", 2, "Answer option 1", "Answer option 2a", "Answer option 3"] 
    Question_5_5 = ["Question Text 5_5", 3, "Answer option 1", "Answer option 2", "Answer option 3a"]     


    #Note position 0 0 is Top Left         0 5 is Top Right
    #              5 0 is Bottom Left      5 5 is Bottom Right                
    List_Questions = [  [Question_0_0, Question_0_1, Question_0_2, Question_0_3, Question_0_4, Question_0_5],
                        [Question_1_0, Question_1_1, Question_1_2, Question_1_3, Question_1_4, Question_1_5],
                        [Question_2_0, Question_2_1, Question_2_2, Question_2_3, Question_2_4, Question_2_5],
                        [Question_3_0, Question_3_1, Question_3_2, Question_3_3, Question_3_4, Question_3_5],
                        [Question_4_0, Question_4_1, Question_4_2, Question_4_3, Question_4_4, Question_4_5],
                        [Question_test, Question_5_1, Question_5_2, Question_5_3, Question_5_4, Question_5_5]]    

    last_answer = ""
# ---------------------------------------------------------------------------
#############################################################################   
screen minigame_trivia:
    add "gui/overlay/trivia_menu.png"
    if last_answer == "":
      add "gui/overlay/trivia_menu_sidebar_r.png" at flash_effect
    if last_answer == "fail":
      add "gui/overlay/trivia_menu_sidebar_y.png" at flash_effect
    if last_answer == "success":
      add "gui/overlay/trivia_menu_sidebar_g.png" at flash_effect
    
    $xpos_start = 500
    $xpos_offset = 160
    $ypos_start = 100
    $ypos_offset = 130

    style_prefix "trivia"
    for i in range(6):
        for j in range(6):
            if isSuccess(i,j):
                add "gui/button/trivia_button_success.png" xpos xpos_start + xpos_offset*j ypos ypos_start + ypos_offset*i
            elif isFail(i,j):
                add "gui/button/trivia_button_fail.png" xpos xpos_start + xpos_offset*j ypos ypos_start + ypos_offset*i 
            elif isActive(i,j):
                imagebutton auto "gui/button/trivia_button_%s.png" xpos xpos_start + xpos_offset*j ypos ypos_start + ypos_offset*i focus_mask True action Call('lbl_minigame_trivia_question',i,j)#[Function(setActive,i,j)]
            else :   
                imagebutton auto "gui/button/trivia_button_%s.png" xpos xpos_start + xpos_offset*j ypos ypos_start + ypos_offset*i focus_mask True
            text "[i],[j]" xpos xpos_start + xpos_offset*j ypos ypos_start + ypos_offset*i
    hbox:
        xalign 0.5
        yalign 0.88
        spacing 100
        textbutton "Restart" action Call('lbl_minigame_trivia_start')
        textbutton "Quit" action [SetVariable('minigame_trivia_lose', True), Return()]
                
#############################################################################   
label lbl_minigame_trivia_question(x,y):
    
    $current_question = List_Questions[x][y]
    $current_answer = current_question[1]
    $chosen_answer = -1
    #menu:
    #    "[current_question[0]]"
    #    "[current_question[2]]":
    #      $chosen_answer = 1
    #    "[current_question[3]]":
    #      $chosen_answer = 2
    #    "[current_question[4]]":
    #      $chosen_answer = 3
    
    call screen minigame_trivia_question(x,y, len(current_question)-2)
    
    $chosen_answer = _return
            
    if chosen_answer == current_answer:
        $setSuccess(x,y)
        $last_answer = "success"
        call lbl_question_success from _call_lbl_question_success
    else:
        $setFail(x,y)
        $last_answer = "fail"
        call lbl_question_failure(x) from _call_lbl_question_failure
        
    return        
     
screen minigame_trivia_question(x, y, answers=2):
    add "gui/overlay/trivia_menu.png"
    
    $current_question = List_Questions[x][y]
    $current_answer = current_question[1]
    
    
    style_prefix "trivia"
    vbox: 
      xmaximum 1000
      xalign 0.5
      yalign 0.5
      label "[current_question[0]]"
      null height (4 * gui.pref_spacing)
      vbox: 
        xalign 0.5
        yalign 0.5
        textbutton "[current_question[2]]" action Return(1)
        if answers > 1:
          textbutton "[current_question[3]]" action Return(2)
        if answers > 2:
          textbutton "[current_question[4]]" action Return(3)
        if answers > 3:
          textbutton "[current_question[5]]" action Return(4)
    
style trivia_label is gui_label
style trivia_label_text is gui_label_text
style trivia_button_text is button_text

style trivia_button_text is default:
    properties gui.button_text_properties("choice_button")
    hover_outlines [ (absolute(1), "#000000", absolute(1), absolute(1)) ]
    outlines [ (absolute(1), "#ffffff", absolute(1), absolute(1)) ]
    
style trivia_label_text:
    color "#ffffff"
    size 50
    outlines [ (absolute(1), "#000000", absolute(1), absolute(1)) ]
    
label lbl_minigame_trivia_start:
    $minigame_trivia_win = False
    $minigame_trivia_lose = False

    $active_squares = [  [0,0,0,0,0,0],
                         [0,0,0,0,0,0],
                         [0,0,0,0,0,0],
                         [0,0,0,0,0,0],
                         [0,0,0,0,0,0],
                         [1,1,1,1,1,1]]

    
label lbl_minigame_trivia:
    
    $quick_menu = False
    call screen minigame_trivia
    
    if minigame_trivia_lose == False:
        $minigame_trivia_lose = hasLost()
    #"lose = [minigame_trivia_lose]"
    if minigame_trivia_win:
        $quick_menu = True
        "You win!"
        return
    if minigame_trivia_lose:
        $quick_menu = True
        "You lose!"
        return
    
    jump lbl_minigame_trivia
    
#############################################################################   

#label format = question_column_row
label lbl_question_success:
    "Good job, that was correct!"
            
    return      

label lbl_question_failure(row=0):
    "Are you even trying? That was not correct! [row]"
    
    if row == 5:
      "On the first row too. Shameful"
    if row == 4:
      "On the second row? Maybe i made the questions too hard?"
    if row == 3:
      "On the third row. Thats only half way!"
      #stop music here
    if row == 2:
      "On the fourth row. You better be careful."
    if row == 1:
      "On the fifth row. Near the end now"
    if row == 0:
      "On the last row! So close!"
      #start creepy ambiance here
            
    return      
