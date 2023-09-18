
init python:
    Total_Questions = 4
    Battle_Question_Current = 0
    Battle_Question_StatusList = ["", "", "", "", "", "", "", "", "", "", ""]
    Battle_1_QuestionList = ["You need vacation time? Is Milo stressing you out already?",
    "What do you need the time for?",
    "Hm… but who’s going to take the notes for the evening meeting?",
    "Can we compromise? Can I give you just the evening off?" ]
    Battle_1_AnswersList = ["Not anymore than usual.",
                            "No, nevermind.",
                            "Yes, but don’t worry.",
                            "Some wedding-related things.",
                            "There’s stuff I need to do.",
                            "For my best friend.",
                            "I’ll ask Milo to do it!",
                            "Joel could probably do it.",
                            "Missing one meeting won’t be so bad.",
                            "No, I need the whole day.",
                            "Yes, that’s works.",
                            "I’m not sure but… the meeting."]
                            
    Battle_1_AnswersLabels = ["lbl_battle_1_Q1A",
                              "lbl_battle_1_Q1B", 
                              "lbl_battle_1_Q1C",
                              "lbl_battle_1_Q2A",
                              "lbl_battle_1_Q2B", 
                              "lbl_battle_1_Q2C",
                              "lbl_battle_1_Q3A",
                              "lbl_battle_1_Q3B", 
                              "lbl_battle_1_Q3C",
                              "lbl_battle_1_Q4A",
                              "lbl_battle_1_Q4B", 
                              "lbl_battle_1_Q4C", ]
                              
    Battle_TimeoutLabel = "lbl_battle_1_Timeout"
    Battle_FailureLabel = "lbl_battle_1_Failure"
                            
    BattleTimerActive = True
    timer_limit = 10
    timer_range = 10
    timer_jump = 'lbl_MissedQuestion'
    
    Battle_MissedQuestionCount = 0
    
    
    
#-----------------------------------------------------------------------
    #Battle Status functions
    def GetStatusButton(state):
      img = "images/ui/battle/question_status_bar_empty.png"
      if state == 'correct':
        img = "images/ui/battle/question_status_bar_correct.png" 
      if state == 'incorrect':
        img = "images/ui/battle/question_status_bar_incorrect.png" 
      if state == 'progress':
        img = "images/ui/battle/question_status_bar_progress.png" 
      
      return img
    
    def ResetBattleStatus():
      global Total_Questions
      global Battle_Question_StatusList
      global Battle_MissedQuestionCount
      Total_Questions = 4
      MissedQuestionCount = 0
      Battle_Question_StatusList = ["", "", "", "", "", "", "", ""]
      WriteToFile("ResetBattleStatus")
      
    def SetResult(currentQuestion, result):
      global Battle_Question_StatusList
      if currentQuestion < len(Battle_Question_StatusList):
        Battle_Question_StatusList[currentQuestion] = result
      WriteToFile("SetResult - " + str(currentQuestion) + " - " + result)
      
    def GetBattleScore():
      score = 0
      for status in Battle_Question_StatusList:
        if status == 'correct':
          score += 1      
      return score
      
#-----------------------------------------------------------------------
    #Logging functions
    def WriteToFile(txt):
      return # comment out to enable logging
      f = open('E:\RenpyGames\Catching the Fox\myfile.txt','a')
      f.write(txt) # python will convert \n to os.linesep
      f.write('\n') # python will convert \n to os.linesep
      f.close() 
      
#-----------------------------------------------------------------------
    #Timer functions
    def StopBattleTimer():
      WriteToFile("StopBattleTimer")
      global BattleTimerActive
      BattleTimerActive = False
      
    def StartBattleTimer():
      WriteToFile("StartBattleTimer")
      global BattleTimerActive
      BattleTimerActive = True
      
    def ResetBattleTimer():
      WriteToFile("ResetBattleTimer")
      global timer_limit
      timer_limit = 10
      StartBattleTimer()
      
      
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script
    
screen countdown:
    if BattleTimerActive:
      timer 0.1 repeat True action If(timer_limit > 0, true=SetVariable('timer_limit', timer_limit - 0.1), false=[ Hide('countdown'), Jump(timer_jump)])
    text "Time:" xpos 720 ypos 300
    bar value timer_limit range timer_range xpos 790 ypos 300 xmaximum 442 top_bar "images/ui/battle/battle_bar_full.png" left_bar None right_bar None thumb None at alpha_dissolve # This is the timer bar.
    
#-----------------------------------------------------------------------
      
    
label lbl_MissedQuestion:
    $WriteToFile("lbl_MissedQuestion" + str(Battle_Question_Current))
    $StopBattleTimer()
    $SetResult(Battle_Question_Current, 'incorrect')
    $Battle_MissedQuestionCount +=1
    
    if Battle_MissedQuestionCount == 2:
      jump expression Battle_FailureLabel
    else:
      jump expression Battle_TimeoutLabel
      
    return

init -2:
    transform q_move1:
        xpos 1200
        linear 1.0 xpos 0
    transform q_move2:
        xpos -1200
        time 2
        linear 1.0 xpos 0
    transform q_move3:
        xpos -830
        ypos 830
        time 3
        linear 0.8 xpos 0 ypos 0
    transform q_move4:
        xpos 830
        ypos -830
        time 4
        linear 0.8 xpos 0 ypos 0
    transform q_move5:
        ypos 830
        time 5
        linear 1.0 ypos 0
    transform q_move6:
        xpos -830
        ypos 830
        time 5
        linear 1.0 ypos xpos 15 ypos 550 
    transform q_move7:
        xpos 830
        ypos -830
        time 5
        linear 1.0 xpos 840 ypos 165

    transform q_moveText1:
        xpos -830
        ypos 830
        time 3
        linear 0.8 xpos 100 ypos 570
    transform q_moveText2:
        xpos 830
        ypos -830
        time 4
        linear 0.8 xpos 925 ypos 200
        
    transform wait5:
      time 5

screen preBattle_screen(_Opponent, _Goal, _Hint, _SimoneVer='executive'):

    tag menu

    default hintTip = Tooltip("")
    default goalTip = Tooltip("")
    
    add "images/ui/battle/pre_background.png" 
    add "images/ui/battle/simone_%s.png"%_SimoneVer at q_move1
    add "images/ui/battle/%s.png"%_Opponent at q_move2
    
    imagebutton idle "images/ui/battle/VS.png" action Return() focus_mask None at q_move5
    #add "images/ui/battle/goal_idle.png" at q_move3
    #add "images/ui/battle/hint_idle.png" at q_move4
    imagebutton idle "images/ui/battle/goal_idle.png" hover "images/ui/battle/goal_hover.png" action Return() hovered goalTip.Action("{color=#f1f125}[_Goal]{/color}") focus_mask True at q_move3
    imagebutton idle "images/ui/battle/hint_idle.png" hover "images/ui/battle/hint_hover.png" action Return() hovered hintTip.Action("{color=#f29d27}[_Hint]{/color}") focus_mask True at q_move4
    #add "images/ui/battle/VS.png" at q_move5
    
    #text "{color=#000000}Enemy name!{/color}" xpos 30 ypos 30
    text hintTip.value xpos 840 ypos 165 at q_moveText2
    text goalTip.value xpos 15 ypos 550 at q_moveText1
    #text "{color=#f29d27}[_Hint]{/color}" xpos 840 ypos 165 at q_moveText2
    #text "{color=#f1f125}[_Goal]{/color}" xpos 15 ypos 550 at q_moveText1
    #imagebutton idle "images/ui/battle/simone_executive.png" action ShowMenu('Battle_screen') focus_mask True at q_move1
    #imagebutton idle "images/ui/battle/solomon.png" action ShowMenu('Battle_screen') focus_mask True at q_move2
    #
    #imagebutton idle "images/ui/battle/goal.png" action ShowMenu('Battle_screen') focus_mask True at q_move3
    #imagebutton idle "images/ui/battle/hint.png" action ShowMenu('Battle_screen') focus_mask True at q_move4
    #imagebutton idle "images/ui/battle/VS.png" action [Hide('preBattle_screen'), ShowMenu('Battle_screen')] focus_mask None at q_move5
    #
    #text "{color=#000000}Simone!{/color}" xpos 400 ypos 640
    
    #textbutton _("{color=#000000}Start!{/color}") action ShowMenu('Battle_screen') xpos 840 ypos 740
    #textbutton _("{color=#000000}Exit!{/color}") action Return() xpos 940 ypos 740
    
    
screen Battle_screen_background(_questions=4, _answers=3):
    $yoff = 30
    $xoff = 30
    $yoff2 = 70
    $xoff2 = 50
    $_firstQuestion = 3*Battle_Question_Current
    $_Battle_Question_StatusList = Battle_Question_StatusList
    add "images/ui/battle/battle_bg.png"
    add "images/ui/battle/speech_bubble.png" xpos 280 ypos 10
    text "{color=#000000}%s{/color}"%(Battle_1_QuestionList[Battle_Question_Current]) xpos 400 ypos 100
    for i in range(_questions):
      add GetStatusButton(_Battle_Question_StatusList[0]) xpos 40+i*50 ypos 465
    #add GetStatusButton(_Battle_Question_StatusList[1]) xpos 120 ypos 500
    #add GetStatusButton(_Battle_Question_StatusList[2]) xpos 170 ypos 500
    #add GetStatusButton(_Battle_Question_StatusList[3]) xpos 220 ypos 500
    
    add "images/ui/battle/question_idle.png" xpos 700-xoff ypos 250-yoff
    text "{color=#000000}%s{/color}"%Battle_1_AnswersList[_firstQuestion+0] xpos 700+xoff2 ypos 250+yoff2
    add "images/ui/battle/question_idle.png" xpos 700-xoff ypos 530-yoff
    text "{color=#000000}%s{/color}"%Battle_1_AnswersList[_firstQuestion+1] xpos 700+xoff2 ypos 530+yoff2
    add "images/ui/battle/question_idle.png" xpos 330-xoff ypos 530-yoff
    text "{color=#000000}%s{/color}"%Battle_1_AnswersList[_firstQuestion+2] xpos 330+xoff2 ypos 530+yoff2

screen Battle_screen(_Opponent, questionList, _answerList, _answerLabels, _questions=4, _answers=3):
    tag menu
    add "images/ui/battle/battle_bg.png"
    add "images/ui/battle/battle_bg_banner.png"
    add "images/ui/battle/battle_bg_shadow.png"
    add "images/ui/battle/%s_battle_sprite.png"%_Opponent xpos 100 ypos 50
    
    #Save Current paramters for failure case
    $Battle_Current_QuestionList = _questionList[:]
    $Battle_Current_AnswersList = _answerList[:]
    $Battle_Current_AnswersLabels = _answerLabels[:]
    $Battle_Current_QuestionTotal = _questions
    $Battle_Current_AnswerTotal = _answers
    
    
    use countdown
    
    $statusXPos = 865
    if _answers == 3:
      $statusXPos = 1065
  
    add "images/ui/battle/speech_bubble.png" xpos 350 ypos 35
    vbox:
      area (370,50,560,160)
      text "{color=#ffffff}%s{/color}"%(_questionList[Battle_Question_Current]) xalign 0.5 yalign 0.5
      #text "{color=#000000}%s{/color}"%(Battle_1_QuestionList[Battle_Question_Current]) xalign 0.5 yalign 0.5
    
    $_Battle_Question_StatusList = Battle_Question_StatusList
    for i in range(_questions):
      add GetStatusButton(_Battle_Question_StatusList[i]) xpos statusXPos+i*50 ypos 240
    
    $firstQuestion = _answers*Battle_Question_Current
    
    use Battle_answers(_answerList, _answerLabels, firstQuestion, _answers )
    #use Battle_answers(Battle_1_AnswersList, Battle_1_AnswersLabels, firstQuestion)
    
screen Battle_answers(_AnswersList, _Labels, _firstQuestion=0, _answers=3):
    
    $yoff = 130
    $xoff = 220
    
    if _answers == 3:
      $yoff = 230
      $xoff = 370
    
    $yoff2 = 70
    $xoff2 = 50
    
    
    if _answers == 3:
      for i in range(_answers):
        imagebutton auto "images/ui/battle/question_%s.png" xpos 40+xoff*i ypos 465 focus_mask None action [Return(str(_Labels[_firstQuestion+i]))]
        vbox:
          #area (735,280,220,130)
          area (130+xoff*i,515,220,130)
          text "{color=#000000}%s{/color}"%_AnswersList[_firstQuestion+i] xalign 0.5 yalign 0.5
    
    else:
      for i in range(_answers):
        $yoffset = 130*(i%2)
        imagebutton auto "images/ui/battle/small_question_%s.png" xpos 40+xoff*i ypos 465+yoffset focus_mask None action [Return(str(_Labels[_firstQuestion+i]))]
        vbox:
          #area (735,280,220,130)
          area (115+(xoff-5)*i,515+yoffset,150,100)
          text "{size=-4}{color=#000000}%s{/color}{/size}"%_AnswersList[_firstQuestion+i] xalign 0.5 yalign 0.5
        
    #imagebutton auto "images/ui/battle/question_%s.png" xpos 700-xoff ypos 530-yoff focus_mask None action [Return(_Labels[_firstQuestion+1])]
    #vbox:
    #  area (735,560,220,130)
    #  text "{color=#000000}%s{/color}"%_AnswersList[_firstQuestion+1] xalign 0.5 yalign 0.5
    #
    #imagebutton auto "images/ui/battle/question_%s.png" xpos 330-xoff ypos 530-yoff focus_mask None action [Return(_Labels[_firstQuestion+2])]
    #vbox:
    #  area (370,560,220,130)
    #  text "{color=#000000}%s{/color}"%_AnswersList[_firstQuestion+2] xalign 0.5 yalign 0.5
    #
    #textbutton _("Quit!") action Return() xpos 840 ypos 740
    
    
#-----------------------------------------------------------------------
# Battle 1
#-----------------------------------------------------------------------
label lbl_battle_1_Start:
    #MONDAY, Week One
    #BATTLE: Simone West, executive assistant vs. Solomon Fox, senior editor
    #GOAL: Ask for to leave early to try on bridesmaid dresses.
    #HINT! Don't go overboard. It's a new job after all, so you don't want to seem lazy... (No Laziness Stat)
    
    call screen preBattle_screen('solomon', "Ask to leave early.", "Don't try to pull one over!")
    $WriteToFile("Starting Battle 1")    
    $Battle_FailureLabel = "lbl_battle_1_Failure"
    $Battle_TimeoutLabel = "lbl_battle_1_Timeout"

    "Intro conversation: Solomon tells Simone she should be open with him about letting him know her needs. Simone realizes that it's her chance to ask for off for the afternoon/evening of the final dress fitting!"

    $ResetBattleStatus()
    $Battle_Question_Current = 0
    $SetResult(Battle_Question_Current, 'progress')
    $ResetBattleTimer()
    #show screen Battle_screen_background
    call screen Battle_screen('solomon', Battle_1_QuestionList, Battle_1_AnswersList, Battle_1_AnswersLabels,  4, 3)
    
    jump expression _return
    "End Battle?!"
    return
    
#-----------------------------------------------------------------------
  
#1. You need vacation time? Is Milo stressing you out already?
label lbl_battle_1_Q1A:
    $WriteToFile("lbl_battle_1_Q1A")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 1
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    ##+CHOICE A: Not anymore than usual. (+Honesty)
    si "Milo's not anymore of a nuisance than he usually is. But yes, I really do need that evening off, though."
    so "I guess that's a fair enough response, especially from a new member of the office. Dealing with Milo does come with a degree of finesse that must be acquired, so I can imagine it taxing at times."
    $ResetBattleTimer()
    call screen Battle_screen('solomon', Battle_1_QuestionList, Battle_1_AnswersList, Battle_1_AnswersLabels,  4, 3)
    
    jump expression _return
    return
  
label lbl_battle_1_Q1B:
    $WriteToFile("lbl_battle_1_Q1B")
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 1
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    ##+CHOICE B: No, nevermind. (+Laziness)
    si "Haha... Milo being stressful. That's a good one, Mr. Fox. Actually, you know what? Nevermind."
    so "Hm? If you're worried about not getting the time, you shouldn't ask in the first place! Haha, I kid. But since you've already mentioned it, you may as well just come out with it. I am a little concerned though..."
    $ResetBattleTimer()
    call screen Battle_screen('solomon', Battle_1_QuestionList, Battle_1_AnswersList, Battle_1_AnswersLabels,  4, 3)
    
    jump expression _return
    return
  
label lbl_battle_1_Q1C:
    $WriteToFile("lbl_battle_1_Q1C")
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 1
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    ###+CHOICE C: Yes, but don't worry. (+Dependability)
    si "Milo does... not have my favorite personality, no-- but I'm working through it. It shouldn't hinder any work we have to do together, if that's what you're worried about."
    so "Said like a true professional! I appreciate your candidness, but if he keeps causing you problems, don't be afraid to write it out in a peer review. I might be able to give some pointers to whip him up in shape."
    $ResetBattleTimer()
    call screen Battle_screen('solomon', Battle_1_QuestionList, Battle_1_AnswersList, Battle_1_AnswersLabels,  4, 3)
    
    jump expression _return
    return
#-----------------------------------------------------------------------
  
#2. What do you need the time for?
label lbl_battle_1_Q2A:
    $WriteToFile("lbl_battle_1_Q2A")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 2
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    window show

    #+CHOICE A: Some wedding-related things. (+Dependability)
    si worried "There's a wedding coming up and I'm the maid-of-honor... I'm sorry, I didn't expect to get transferred so I didn't have a chance to let you know earlier."
    so "For a second, I thought you were going to tell me you're the one getting married! Ha, but that's true. I'm surprised your former department head didn't mention it to me, but then again... knowing what's going on down there, they probably forget to mention it themselves."
    $ResetBattleTimer()
    call screen Battle_screen('solomon', Battle_1_QuestionList, Battle_1_AnswersList, Battle_1_AnswersLabels,  4, 3)
    
    jump expression _return
    return
  
label lbl_battle_1_Q2B:
    $WriteToFile("lbl_battle_1_Q2B")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 2
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    ##+CHOICE B: There's stuff I need to do. (+Laziness)
    si "There's just some important stuff I need to get done that night."
    so "It can't wait? I don't mean to be hard on you, but we really do need you in this office, and you're putting me in something of a hard spot."
    $ResetBattleTimer()
    call screen Battle_screen('solomon', Battle_1_QuestionList, Battle_1_AnswersList, Battle_1_AnswersLabels,  4, 3)    
    jump expression _return
    return
  
label lbl_battle_1_Q2C:
    $WriteToFile("lbl_battle_1_Q2C")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 2
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    ##+CHOICE C: For my best friend. (+Kindness)
    si "It's for my best friend. She's getting married in less than two weeks and we're having an emergency fitting that Thursday."
    so "Oh, I see. That is pretty important, and it's not something you can just move to another day..."

    $ResetBattleTimer()
    call screen Battle_screen('solomon', Battle_1_QuestionList, Battle_1_AnswersList, Battle_1_AnswersLabels,  4, 3)    
    jump expression _return
    return
#-----------------------------------------------------------------------
  
#3. Hm... but who's going to take the notes for the evening meeting?
label lbl_battle_1_Q3A:
    $WriteToFile("lbl_battle_1_Q3A")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 3
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    ##+CHOICE A: I'll ask Milo to do it! (+Intellect)
    si "I could see if Milo would... be willing to, uh..."
    so "Hm, and you think he'll say yes? Well, no one ever said you weren't optimistic. I'm sure he'll listen if I insist on it, though. He hates not turning in work on time, after all."
    $ResetBattleTimer()
    call screen Battle_screen('solomon', Battle_1_QuestionList, Battle_1_AnswersList, Battle_1_AnswersLabels,  4, 3)   
    jump expression _return
    return
  
label lbl_battle_1_Q3B:
    $WriteToFile("lbl_battle_1_Q3B")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 3
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    ##+CHOICE B: Joel could probably do it (+Imagination)
    si "Maybe Joel could do the notes? He might do well with the practice."
    so "Joel's an intern so he's not required to come to meetings, and he's never done it before. I've found that giving Joel new tasks too soon doesn't bode well for the success of the meeting."
    $ResetBattleTimer()
    call screen Battle_screen('solomon', Battle_1_QuestionList, Battle_1_AnswersList, Battle_1_AnswersLabels,  4, 3)  
    jump expression _return
    return
  
label lbl_battle_1_Q3C:
    $WriteToFile("lbl_battle_1_Q3C")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 3
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    ##+CHOICE C: Missing one meeting won't be so bad. (+Laziness)
    si "If it's just one meeting, it'll be fine. Most who work here aren't too familiar with me so maybe whoever usually takes the notes can take them."
    so "Simone, I understand your logic, but we need those notes so I can go over them and keep track of who's on what projects and that particular staff has already been returned to their normal workload. If we can't find a replacement, then I definitely can't give you off."
    $ResetBattleTimer()
    call screen Battle_screen('solomon', Battle_1_QuestionList, Battle_1_AnswersList, Battle_1_AnswersLabels,  4, 3)   
    jump expression _return
    return
#-----------------------------------------------------------------------
  
#4. Can we compromise? Can I give you just the evening off?
label lbl_battle_1_Q4A:
    $WriteToFile("lbl_battle_1_Q4A")    
    $SetResult(Battle_Question_Current, 'correct')
    $StopBattleTimer()
    ##+CHOICE A: No, I need the whole day. (+Laziness)
    si "I don't think so... I'll definitely need the whole day off."
    so "Hm? I thought you were only asking for the afternoon and the evening off. I don't think we can manage the afternoon and evening as it is, let alone the whole day..."
    jump lbl_battle_1_End   
    return
  
label lbl_battle_1_Q4B:
    $WriteToFile("lbl_battle_1_Q4B")    
    $SetResult(Battle_Question_Current, 'correct')
    $StopBattleTimer()
    ##+CHOICE B: Yes, that's works.
    si "I think I can agree to that... I'll definitely need to leave in the evening though. As long as we can make sure that I get off in time, it should work out fine!"
    so "Oh, great! "
    jump lbl_battle_1_End   
    return
  
label lbl_battle_1_Q4C:
    $WriteToFile("lbl_battle_1_Q4C")    
    $SetResult(Battle_Question_Current, 'correct')
    $StopBattleTimer()
    ##+CHOICE C: I'm not sure but... the meeting. (+Intellect)
    si "The evening might work but... I'm a little worried about the meeting. Will it be okay without me?"
    so "Hm... it is a little short notice, but I'll just ask the previous minutes taker to record in your place. I'm sure it'll work out if someone is there to cover the meeting while you're gone."
    jump lbl_battle_1_End   
    return
#-----------------------------------------------------------------------
    
label lbl_battle_1_End:   
    $WriteToFile("lbl_battle_1_End")    
    if GetBattleScore() >= 2:
      jump lbl_battle_1_Success
    else:
      jump lbl_battle_1_Failure

label lbl_battle_1_Success:
    $WriteToFile("lbl_battle_1_Success")   
    #Post Battle, Success: 
    so "Alright, alright... you've convinced me. Enjoy your free Thursday. Can I ask who's getting married?"
    si "It's my friend, Trina. Everything's been extremely busy leading up to it..."
    so "Understandable. I've never been to a wedding myself-- honestly, a few of my friends have bitten the marriage bullet but personally I don't think I've met the right person yet."
    si "Yeah, I know what you mean."
    "Solomon smiles."
    so "I'd say, 'I'm sure you do', but it seems like I'd just be asking for trouble."
    si "...Definitely asking for trouble-- though of course, it depends on your intentions."
    "Instead of replying, Solomon lets out a warm laugh."
    so "Enjoy your free Thursday evening, Simone."
    
    $ battle_one = "yes"

    #$ResetBattleTimer()
    hide Battle_screen
    
    jump B1_fin

label lbl_battle_1_Failure:
    $WriteToFile("lbl_battle_1_Failure")   
    #Post Battle, Failure:
    
    so "\"Simone, I’m sorry, but I really don’t think we can afford to spare you.\""
        
    so "\"You haven’t been here for very long yet and I really want you to get a feel for the office and how we work at Cufflinks.\""

    si "\"I understand.\""

    so "\"I really do apologize; is there some way you can reschedule?\""
    
    si "\"I don’t believe so, but I’ll see what I can do.\""
    
    so "\" Alright. I’ll be seeing you Thursday, then.\""

    si "\"Yes, Mr. Fox.\""

    $ battle_one = "no"
    
    hide Battle_screen
    #$ResetBattleTimer()
    #call screen Battle_screen
    jump B1_fin
    
label lbl_battle_1_Timeout:
    $WriteToFile("lbl_battle_1_Timeout")    
    $SetResult(Battle_Question_Current, 'incorrect')
    $Battle_Question_Current+=1
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    ##+CHOICE C: Missing one meeting won't be so bad. (+Laziness)
    si "..."
    so "Nothing to say?"
    
    $ResetBattleTimer()
    call screen Battle_screen('solomon', Battle_1_QuestionList, Battle_1_AnswersList, Battle_1_AnswersLabels,  4, 3)   
    jump expression _return
    return
#-----------------------------------------------------------------------
# Intro Battle
#-----------------------------------------------------------------------
init python:
    Battle_Question_StatusList = ["", "", "", "","", "", "", ""]
    Battle_intro_QuestionList = [ "So Ms. West, please tell me a little bit about yourself.",
                              "What do you like the most about your current position?",
                              "If you love it so much, why are you looking for a new opportunity now?",
                              "What would you say are your strengths? What will {i}you{/i} bring with you to 5/7 the company?",
                              "What do you think are some potential weaknesses you'll need to overcome if you were to work for our office?",
                              "Why do {i}you{/i} want to work for us? What drew you to our company?",
                              "You seem like you've got a good head on your shoulders; where would you like to see yourself in five years?",
                              "Do you have any questions for me?",]
    Battle_intro_AnswersList = [
        "Talk about what others think of you.", #kindness        
        "Be conscise.", #intellect        
        "Give her background relating to the job.", #dependability            
        "Tell her what you're passionate about.", #honesty            
        "Open with something funny?", #imagination
        "I can express myself.", #imagination
        "Maybe... the group projects?", #dependability        
        "I do have friends, so...", #kindness
        "The learning experience.", #intellect
        "Well, considering I'm just an intern...", #honesty
        "Just a change of scenery.", #kindness
        "I'd like a challenge", #dependability        
        "It's a better career option.", #honesty        
        "I want to network.", #intellect            
        "I want more freedom.", #imagination
        "I can type quickly.", #intellect        
        "I work well in teams.", #dependability        
        "I'm good at objectivity.", #honesty
        "I'm personable.", #kindness            
        "I speak a little French.", #imagination
        "...the get-to-the-point type.", #intellect        
        "...not a fan of criticism.", #kindness        
        "...not as flexible as I'd like to be.", #dependability        
        "...improving my ability to concentrate.", #imagination            
        "...the type to be overly blunt.", #honesty
        "...be interesting.", #Imagination        
        "...be rewarding.", #Intellect        
        "...be a nice place to work.", #kindness        
        "...be more stable.", #honesty            
        "...have better management.", #dependability
        "...in an environment that values my input.", #intellect
        "...from a secure position where I can do my best.", #honesty        
        "...in a creative space where I'm not restricted.", #imagination        
        "...in an environment where I can speak my mind.", #dependability
        "...with people I actually like.", #kindness
        "What's a general work day here like?", #dependability        
        "Do you like working here?", #kindness
        "What do you like best about your job?", #imagination        
        "Where do you think this company will be in five years?", #intellect
        "How did I do?", #honest
        ]
                            
    Battle_intro_AnswersLabels = ["lbl_battle_intro_Q1A",
                              "lbl_battle_intro_Q1B", 
                              "lbl_battle_intro_Q1C",
                              "lbl_battle_intro_Q1D",
                              "lbl_battle_intro_Q1E",
                              
                              "lbl_battle_intro_Q2A",
                              "lbl_battle_intro_Q2B", 
                              "lbl_battle_intro_Q2C",
                              "lbl_battle_intro_Q2D",
                              "lbl_battle_intro_Q2E",
                              
                              
                              "lbl_battle_intro_Q3A",
                              "lbl_battle_intro_Q3B", 
                              "lbl_battle_intro_Q3C",
                              "lbl_battle_intro_Q3D",
                              "lbl_battle_intro_Q3E",
                              
                              
                              "lbl_battle_intro_Q4A",
                              "lbl_battle_intro_Q4B", 
                              "lbl_battle_intro_Q4C",
                              "lbl_battle_intro_Q4D",
                              "lbl_battle_intro_Q4E",
                              
                              
                              "lbl_battle_intro_Q5A",
                              "lbl_battle_intro_Q5B", 
                              "lbl_battle_intro_Q5C",
                              "lbl_battle_intro_Q5D",
                              "lbl_battle_intro_Q5E",
                              
                              
                              "lbl_battle_intro_Q6A",
                              "lbl_battle_intro_Q6B", 
                              "lbl_battle_intro_Q6C",
                              "lbl_battle_intro_Q6D",
                              "lbl_battle_intro_Q6E",
                              
                              
                              "lbl_battle_intro_Q7A",
                              "lbl_battle_intro_Q7B", 
                              "lbl_battle_intro_Q7C",
                              "lbl_battle_intro_Q7D",
                              "lbl_battle_intro_Q7E",
                              
                              
                              "lbl_battle_intro_Q8A",
                              "lbl_battle_intro_Q8B", 
                              "lbl_battle_intro_Q8C",
                              "lbl_battle_intro_Q8D",
                              "lbl_battle_intro_Q8E",
                              ]
       
#-----------------------------------------------------------------------
label lbl_battle_intro_Timeout:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'incorrect')
    $Battle_Question_Current += 1
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    "..."
    "I dont think she approves of my silence."
    
    $ResetBattleTimer()
    call screen Battle_screen (Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)   
    jump expression _return
    return
    
#-----------------------------------------------------------------------
label lbl_battle_intro_Failure:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'incorrect')
    $StopBattleTimer()
    "..."
    
    d "I think i've heard enough."
    
    jump lbl_battle_intro_End  
    
#-----------------------------------------------------------------------
    
label lbl_battle_intro_Q1A:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 1
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_kindness +=1
    
    "Hm..."
            
    "Well, if I talk about what my co-workers think of me, then maybe she'll notice how well I work with others."
            
    "Seems like a safe enough response."
            
    si "People who know me best say that I'm easy to work with and that I'm great at making people feel welcome."
            
    d "And you would agree?"
            
    si "I would, yes."
            
    si "That's actually one the reasons I wanted to work for 5/7 Publishing-- the idea of working with new faces and personalities is pretty exciting for me."
    
    "Finished my answer, I look at her expectantly but she just nods along absently, offering a brief, noncommital comment."
    
    d "I see."
    
    "Debra's expression doesn't change as she glances back down at the file folder and writes down a note on a small pad beside her."
    
    "There's a pause."
    
    d "It says here that you've been interning with Boost Marketing."
    
    $ResetBattleTimer()
    call screen Battle_screen (Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)   
    jump expression _return
    return
    
label lbl_battle_intro_Q1B:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 1
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_intellect +=1
    
    "I decide to answer as briefly but comprehensively as possible."
            
    si "I can summarize who I am in three words."
    
    "Debra looks at me expectantly."
    
    d "Go for it."
    
    si "Passionate, thorough and organize."
    
    si "Meaning I--"
    
    d "Nope, got it."
    
    d "If you only need three words to say it, those are the three I'm taking note of."
    
    d "I'll see how you prove what you mean during the rest of the interview."
    
    d "Anything else?"
    
    si "Oh, I... no."
    
    "Finished my answer, I look at her expectantly but she just nods along absently, offering a brief, noncommital comment."
    
    d "I see."
    
    "Debra's expression doesn't change as she glances back down at the file folder and writes down a note on a small pad beside her."
    
    "There's a pause."
    
    d "It says here that you've been interning with Boost Marketing."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q1C:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 1
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_dependability +=1
    
    "Hm... maybe I should talk about why I want to work here."
            
    "Nothing like a little less than tragic backstory to get someone personally invested."
    
    si "Since I was young, I've always wanted a job where I could be someone I was proud of."
    
    si "I think that vibes really well with the company's motto."
    
    si "'The Best You Is True.'"
    
    si "Getting a job at 5/7 would help me to be true to myself, and I think, fulfill my dream."
    
    "...Okay, so maybe I'm laying it on a little thick. {w}Doesn't mean it didn't do the job, though."
    
    "Finished my answer, I look at her expectantly but she just nods along absently, offering a brief, noncommital comment."
    
    d "I see."
    
    "Debra's expression doesn't change as she glances back down at the file folder and writes down a note on a small pad beside her."
    
    "There's a pause."
    
    d "It says here that you've been interning with Boost Marketing."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q1D:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 1
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_honesty +=1
    
    "I should go with the things that I like."
            
    "People don't really care about what you do--"
    
    "People care about what you are."
    
    "The safest choice would be talking about something I'm passionate about."
    
    si "It may seem strange but supporting and helping others is my passion."
    
    si "Even when I was younger, there was nothing more satisfying then my family's appreciative comments on hold I helped around the house. {w}When it came to doing things, I could always be found helping; whether it was baking or household chores."
    
    si "As I grew older, that habit matured into tutoring and other supportive types of work, and I've found that there's nothing more that I like than helping people get the tools they need to meet their goals."
    
    "{i}Nice, Simone.{/i}"
    
    "Finished my answer, I look at her expectantly but she just nods along absently, offering a brief, noncommital comment."
    
    d "I see."
    
    "Debra's expression doesn't change as she glances back down at the file folder and writes down a note on a small pad beside her."
    
    "There's a pause."
    
    d "It says here that you've been interning with Boost Marketing."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q1E:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 1
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_imagination +=1
    
    "I could always keep it light..."
            
    si "If I could pick a movie title that described my life perfectly, it would be without a doubt, 'Die Hard.'"
    
    "Debra's interest looks piqued for a moment. {w}Or she's looking at me flatly; I can't tell with the misplaced 'brow--"
    
    si "After all, how better to describe my perserverance in one easy sentence?"
    
    "Debra looks at me flatly."
    
    "Okay. So maybe not my best line."
    
    "No more 'West Comedy Hour.'"
    
    "At least, though, she can't say I'm not creative, right?"
    
    "Finished my answer, I look at her expectantly but she just nods along absently, offering a brief, noncommital comment."
    
    d "I see."
    
    "Debra's expression doesn't change as she glances back down at the file folder and writes down a note on a small pad beside her."
    
    "There's a pause."
    
    d "It says here that you've been interning with Boost Marketing."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
#-----------------------------------------------------------------------
    
label lbl_battle_intro_Q2A:
    
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 2
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_imagination +=1
    
    si "I would say... that I can express myself freely."
            
    "Debra lifts an eyebrow--and since it's the lower one, she merely looks surprised."
    
    "I blink for a second, mildly disconcerted."
    
    d "Care to expound on that?"
    
    "Not really. After all, when being an intern meant I explicitly didn't express anything and I was lying through my teeth-- well."
    
    si "I just mean to say that my opinions are valued at my company, mainly because I work hard to be heard."
    
    "Slightly more true."
    
    "For the first time, Dead-pan Deb flashes a little smile."
    
    "I almost think I'm hallucinating."
    
    d "You know, I have a few friends that started out there. It's a great place to work from what they've told me."
    
    si "Oh, I love it there!"
    
    d "..."
    
    "It seems my response comes out a little too enthusiastically for her tastes because Debra's eyebrow goes up."
    
    "At least, it goes up higher than it already is."
    
    "I fight against the urge to stare, forcing myself to pay attention to the questions."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q2B:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 2
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_dependability +=1
    
    si "I would say being able to work well with others."
            
    "If I could even call it 'working with'."
    
    "It's more like I do all the work and then they get the credit because I'm 'just the intern'. I liked working with others, but..."
    
    "I try not to look annoyed as I reflect on what a chore my internship at the management firm has been for the past two years."
    
    "I must've succeeded, too."
    
    "For the first time, Dead-pan Deb flashes a little smile."
    
    "I almost think I'm hallucinating."
    
    d "You know, I have a few friends that started out there. It's a great place to work from what they've told me."
    
    si "Oh, I love it there!"
    
    d "..."
    
    "It seems my response comes out a little too enthusiastically for her tastes because Debra's eyebrow goes up."
    
    "At least, it goes up higher than it already is."
    
    "I fight against the urge to stare, forcing myself to pay attention to the questions."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q2C:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 2
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_kindness +=1
    
    si "I would say... the relationships I've been able to build with people."
            
    si "My co-workers are really great people and I think working with them has made me into a better person."
            
    "It's mostly true, anyway."
            
    "I'd definitely mastered the relationship skill of being an office scapegoat and picking up other people's slack."
            
    "As... infinitely unpleasant as that was, it did make me into a better worker."
            
    "I typed faster than everyone, I filed faster than anyone... and I'd be straight up lying if I'd said part of my joy of getting this job would be watching my former management company crumble in the dust without me."
            
    "I try my best not to let my annoyance show on my face and seem to manage it well enough."
    
    "For the first time, Dead-pan Deb flashes a little smile."
    
    "I almost think I'm hallucinating."
    
    d "You know, I have a few friends that started out there. It's a great place to work from what they've told me."
    
    si "Oh, I love it there!"
    
    d "..."
    
    "It seems my response comes out a little too enthusiastically for her tastes because Debra's eyebrow goes up."
    
    "At least, it goes up higher than it already is."
    
    "I fight against the urge to stare, forcing myself to pay attention to the questions."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q2D:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 2
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_intellect +=1
    
    si "For me, my favorite thing has to be all of the learning experiences that I've had."
            
    "Like the time my co-worker Sarah accidentally printed four thousand print-outs on the new paper I'd put an order for and my boss laid into me for not ordering enough paper."
    
    "Lesson number one, if you want a job done right, do it yourself."
    
    si "Every day, I feel like I'm adding more and more to my skillset."
    
    si "It's definitely..."
    
    "Well, I can't say 'a major nuisance', so I'll go with something more relatable."
    
    si "...fulfilling."
    
    "For the first time, Dead-pan Deb flashes a little smile."
    
    "I almost think I'm hallucinating."
    
    d "You know, I have a few friends that started out there. It's a great place to work from what they've told me."
    
    si "Oh, I love it there!"
    
    d "..."
    
    "It seems my response comes out a little too enthusiastically for her tastes because Debra's eyebrow goes up."
    
    "At least, it goes up higher than it already is."
    
    "I fight against the urge to stare, forcing myself to pay attention to the questions."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q2E:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 2
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_honesty +=1
    
    "Is she for real? I mean, she knows I'm just an intern, right?"
            
    "What's there to like about being an intern?"
            
    "Considering the amount of work that gets dumped on me in a day, I want to tell her the truth, which is a solid 'absolutely nothing.'"
    
    "But that won't look good so I go with the closest thing I have to the truth."
    
    si "I love that... I'm really used in the office."
    
    si "I never really have an idle moment to spare."
    
    d "I see, I see."
    
    "For the first time, Dead-pan Deb flashes a little smile."
    
    "I almost think I'm hallucinating."
    
    d "You know, I have a few friends that started out there. It's a great place to work from what they've told me."
    
    si "Oh, I love it there!"
    
    d "..."
    
    "It seems my response comes out a little too enthusiastically for her tastes because Debra's eyebrow goes up."
    
    "At least, it goes up higher than it already is."
    
    "I fight against the urge to stare, forcing myself to pay attention to the questions."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
#-----------------------------------------------------------------------
    
label lbl_battle_intro_Q3A:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 3
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_kindness +=1
    
    si "It's not really anything about my current job that I don't like--"
            
    si "Really, it's just a change of scenery."
            
    "By change of scenery, I mean I'm trying my best to break free of the trash city of a job I'm working but I digress."
            
    "True honesty isn't valued {i}nearly{/i} enough."
    
    "I hold my breath, but it seems pointless to even summon any nervousness since Debra seems satisfied with my response."
    
    "For the briefest of moments, I even think I see a small smile playing on her lips."
    
    "{i}Nice save, Simone.{/i}"
    
    d "Very... interesting. I appreciate your candidness."
    
    "The moment of triumph is quickly squashed by the serious look in Debra's eyes."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)   
    jump expression _return
    return
    
label lbl_battle_intro_Q3B:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 3
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_dependability +=1
    
    si "I want work that really challenges me."
            
    si "I feel like I have a lot more to offer and I want to be able to showcase my abilities in administrative capacity."
    
    si "I strongly feel that 5/7 will allow me to stretch my wings and push my limits."
    
    si "Overall, I just feel like it'd be more... dependable?"
    
    "I hold my breath, but it seems pointless to even summon any nervousness since Debra seems satisfied with my response."
    
    "For the briefest of moments, I even think I see a small smile playing on her lips."
    
    "{i}Nice save, Simone.{/i}"
    
    d "Very... interesting. I appreciate your candidness."
    
    "The moment of triumph is quickly squashed by the serious look in Debra's eyes."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q3C:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 3
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_honesty +=1
    
    si "I think working here would be a good investment for the future."
            
    si "Most people work a job-- I feel that working for 5/7 will break me out of that and I'll be able to really establish a career in the magazine industry by working here."
            
    "As much fun as slaving-- excuse me, being an intern-- I'm pretty sure that anything would be better than my current job as coffee fetcher and resident scapegoat."
    
    "I hold my breath, but it seems pointless to even summon any nervousness since Debra seems satisfied with my response."
    
    "For the briefest of moments, I even think I see a small smile playing on her lips."
    
    "{i}Nice save, Simone.{/i}"
    
    d "Very... interesting. I appreciate your candidness."
    
    "The moment of triumph is quickly squashed by the serious look in Debra's eyes."
            
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q3D:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 3
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_intellect +=1
    
    si "Being such a prestigious location, I look forward to meeting like-minded others and really networking so that I can make sure that my industry presence will be long-lived."
            
    "Which is kind of, sort of way to say I'll be gold-mining friendships for my future in case this whole thing doesn't work out but I'm pretty sure I worded it nicely enough that it doesn't sound too black-widow-ey."
            
    "The image of me preying on 5/7 staff comes to mind but that's definitely not my intention."
            
    "Definitely."
    
    "I hold my breath, but it seems pointless to even summon any nervousness since Debra seems satisfied with my response."
    
    "For the briefest of moments, I even think I see a small smile playing on her lips."
    
    "{i}Nice save, Simone.{/i}"
    
    d "Very... interesting. I appreciate your candidness."
    
    "The moment of triumph is quickly squashed by the serious look in Debra's eyes."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q3E:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 3
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_imagination +=1
    
    "Can I really call my current position a job, even?"
            
    "They say in the world of journalism to never burn bridges but honestly."
            
    si "Well, as a person in my position, I feel that I'd like more... freedom."
            
    si "I know I'll still have someone operating as oversight but I'd think that I'd like a chance to make my own decisions and not have someone constantly hovering over my shoulder."
            
    "I want to shout {i}\"BECAUSE I'M A GROWN WOMAN!!\"{/i} but I also don't want to be kicked out of this interview so... I'll let it go."
            
    "For now."
            
    "Debra scribbles away without saying anything."
    
    "I hold my breath, but it seems pointless to even summon any nervousness since Debra seems satisfied with my response."
    
    "For the briefest of moments, I even think I see a small smile playing on her lips."
    
    "{i}Nice save, Simone.{/i}"
    
    d "Very... interesting. I appreciate your candidness."
    
    "The moment of triumph is quickly squashed by the serious look in Debra's eyes."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
#-----------------------------------------------------------------------

label lbl_battle_intro_Q4A:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 4
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_intellect +=1
    
    si "I type pretty quickly."
            
    d "Oh, do you? How many words-per-minute? Do you know offhand?"
            
    "Sure do, even if I only knew it because I was bored a few nights before and got curious."
            
    si "Right now, I type about 93 wpm, but my goal is to make it to a nice-even 100."
            
    d "85 wpm... that's impressive, Ms. West."
            
    d "Fast typers are highly valued in any company that produces a lot of writing so I assure that your skills would be used to the full."
            
    "She takes another brief note, then makes eye contact with me."
    
    d "That's great to hear, Simone."
    
    "I perk up a little, but unsurprisingly, her expression doesn't betray her positive reply."
    
    "In fact, it would be totally flat if not for the floating brow of mystery."
    
    "No wonder she's in charge of processing interviews. Stray brow or no stray brow, her pokerface is killer."
    
    "Oh, wait. I should be listening."
    
    d "...excellent asset for this team and I agree that we would love for you to bring on your unique skill set, Simone."
    
    "Wait! She's complementing me?"
    
    si "Oh, uhm, thank you."
    
    "I barely manage to cover my surprise as Debra quickly moves on, taking another glance through my file."
    
    d "Considering how excellent your credentials are, it might be harder to conceptualize, but..."
    
    d "Well, frankly nobody's perfect."
    
    "I know I'm wrong, but I struggle not to look at her levitating eyebrow when she says it."
    
    d "Working for a publishing company is a difficult job and we need to know that you're prepared to deal with the obstacles that come with a job like this."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q4B:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 4
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_dependability +=1
    
    si "I have an objective viewpoint, so I'm great with peer review."
            
    si "I'm certain that whatever tasks I'm assigned, I'll be able to give an unbiased opinion."
    
    "Debra nods mutely as she takes a note but I can tell she probably doesn't know what I'm really thinking."

    "...Which is, frankly, of {i}course{/i} I can be objective."
    
    "It's not like I work here yet, so how I can even be biased toward 5/7 Publishing?"
    
    "If anything, it's pretty easy to step back and say how terrible someone else's work is, but... whatever gets me this job."
    
    "If it means I never have to push papers under incompetant workers again then I'll be glad to give an honest opinion."
    
    d "That's great to hear, Simone."
    
    "I perk up a little, but unsurprisingly, her expression doesn't betray her positive reply."
    
    "In fact, it would be totally flat if not for the floating brow of mystery."
    
    "No wonder she's in charge of processing interviews. Stray brow or no stray brow, her pokerface is killer."
    
    "Oh, wait. I should be listening."
    
    d "...excellent asset for this team and I agree that we would love for you to bring on your unique skill set, Simone."
    
    "Wait! She's complementing me?"
    
    si "Oh, uhm, thank you."
    
    "I barely manage to cover my surprise as Debra quickly moves on, taking another glance through my file."
    
    d "Considering how excellent your credentials are, it might be harder to conceptualize, but..."
    
    d "Well, frankly nobody's perfect."
    
    "I know I'm wrong, but I struggle not to look at her levitating eyebrow when she says it."
    
    d "Working for a publishing company is a difficult job and we need to know that you're prepared to deal with the obstacles that come with a job like this."
    
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q4C:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 4
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_kindness +=1
    
    si "I'm pretty good with people."
            
    d "Do you mean to say that you enjoy situations where you have the opportunity to converse with others? A people-person, if you will?"
    
    "People-person..."
    
    "I don't know if I would say I'm the conversational type, but if by 'people-person' she's asking if I could deal with most people's antics no matter what they threw at me, then yes."
    
    "I smile, taking care to make eye-contact."
    
    si "Definitely a people-person."
    
    d "That's great to hear, Simone."
    
    "I perk up a little, but unsurprisingly, her expression doesn't betray her positive reply."
    
    "In fact, it would be totally flat if not for the floating brow of mystery."
    
    "No wonder she's in charge of processing interviews. Stray brow or no stray brow, her pokerface is killer."
    
    "Oh, wait. I should be listening."
    
    d "...excellent asset for this team and I agree that we would love for you to bring on your unique skill set, Simone."
    
    "Wait! She's complementing me?"
    
    si "Oh, uhm, thank you."
    
    "I barely manage to cover my surprise as Debra quickly moves on, taking another glance through my file."
    
    d "Considering how excellent your credentials are, it might be harder to conceptualize, but..."
    
    d "Well, frankly nobody's perfect."
    
    "I know I'm wrong, but I struggle not to look at her levitating eyebrow when she says it."
    
    d "Working for a publishing company is a difficult job and we need to know that you're prepared to deal with the obstacles that come with a job like this."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q4D:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 4
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_imagination +=1
    
    si "I took some French in school, so I have at least a basic command of that language."
            
    "She looks at me doubtfully."
    
    d "Ms. West... looking over your resumé, I would say that some of your skills are much more note-worthy than a basic command of French... why did you choose to highlight it?"
    
    "Because it was the first thing I thought of."
    
    "...Not that I could say that, but. You know."
    
    si "I..."
    
    "Quick, make something up!"
    
    si "I believe that communication is really important, so... even if it's a basic command of the language, being a person who is one step closer to breaking the language barrier brings us all together as a nation."
    
    "Well, it could've been worse."
    
    "Especially since Debra takes a quick note before looking back at me."
    
    d "That's great to hear, Simone."
    
    "I perk up a little, but unsurprisingly, her expression doesn't betray her positive reply."
    
    "In fact, it would be totally flat if not for the floating brow of mystery."
    
    "No wonder she's in charge of processing interviews. Stray brow or no stray brow, her pokerface is killer."
    
    "Oh, wait. I should be listening."
    
    d "...excellent asset for this team and I agree that we would love for you to bring on your unique skill set, Simone."
    
    "Wait! She's complementing me?"
    
    si "Oh, uhm, thank you."
    
    "I barely manage to cover my surprise as Debra quickly moves on, taking another glance through my file."
    
    d "Considering how excellent your credentials are, it might be harder to conceptualize, but..."
    
    d "Well, frankly nobody's perfect."
    
    "I know I'm wrong, but I struggle not to look at her levitating eyebrow when she says it."
    
    d "Working for a publishing company is a difficult job and we need to know that you're prepared to deal with the obstacles that come with a job like this."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return

label lbl_battle_intro_Q4E:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 4
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_honesty +=1
    
    si "I have an objective viewpoint, so I'm great with peer review."
            
    si "I'm certain that whatever tasks I'm assigned, I'll be able to give an unbiased opinion."
            
    "Debra nods mutely as she takes a note but I can tell she probably doesn't know what I'm really thinking."

    "...Which is, frankly, of {i}course{/i} I can be objective."
            
    "It's not like I work here yet, so how I can even be biased toward 5/7 Publishing?"
            
    "If anything, it's pretty easy to step back and say how terrible someone else's work is, but... whatever gets me this job."
            
    "If it means I never have to push papers under incompetant workers again then I'll be glad to give an honest opinion."
            
    d "That's great to hear, Simone."
    
    "I perk up a little, but unsurprisingly, her expression doesn't betray her positive reply."
    
    "In fact, it would be totally flat if not for the floating brow of mystery."
    
    "No wonder she's in charge of processing interviews. Stray brow or no stray brow, her pokerface is killer."
    
    "Oh, wait. I should be listening."
    
    d "...excellent asset for this team and I agree that we would love for you to bring on your unique skill set, Simone."
    
    "Wait! She's complementing me?"
    
    si "Oh, uhm, thank you."
    
    "I barely manage to cover my surprise as Debra quickly moves on, taking another glance through my file."
    
    d "Considering how excellent your credentials are, it might be harder to conceptualize, but..."
    
    d "Well, frankly nobody's perfect."
    
    "I know I'm wrong, but I struggle not to look at her levitating eyebrow when she says it."
    
    d "Working for a publishing company is a difficult job and we need to know that you're prepared to deal with the obstacles that come with a job like this."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return

#-----------------------------------------------------------------------
    
label lbl_battle_intro_Q5A:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 5
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_intellect +=1
    
    si "I'm... probably not as patient as I'd like to be, so there is that..."
            
    d "Not as patient as you'd like?"
            
    si "Well, specially, I've heard that I can be abrupt and impatient when it comes to deadlines."
            
    si "On the brightside, my projects always get done, but..."
            
    d "On the dim side, you step on toes to get it done. {w}I understand, Ms. West."
    
    "Debra looks satisfied."
    
    "It was an easy enough question-- all I had to do was reply in a way that showed that I had an issue, but not really one that would mess up my work at 5/7 Publishing."
    
    "It's a dangerous line to tread but..."
    
    "I glance at my watch discreetly."
    
    "A half-hour already?"
    
    "I glance at Debra's notepad and try not to feel smug."
    
    "This interview couldn't be more in the bag."
    
    d "Ms. West. Frankly, 5/7 Publishing provides reading content that is primarily geared towards a male demographic between the ages of 18-35 and beyond."
    
    d "You're not our target audience, and while your insights would no doubt be enlightening, I have to ask..."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q5B:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 5
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_kindness +=1
    
    si "I guess my number one issue would be that I don't really enjoy harsh criticism-"
            
    "Debra's hand drifts towards the notepad, sparking someting like panic in my heart."
    
    si "But as I've grown in the business world, I've become better with handling constructive criticism and applying myself."
    
    "Not a total lie."
    
    "I definitely... do not enjoy when people hide behind their own incompetence by making {i}me{/i} seem incompetant, but she's already mentioned that she knows people at my internship."
    
    "I can't exactly put them on Front Street."
    
    "Debra looks satisfied."
    
    "It was an easy enough question-- all I had to do was reply in a way that showed that I had an issue, but not really one that would mess up my work at 5/7 Publishing."
    
    "It's a dangerous line to tread but..."
    
    "I glance at my watch discreetly."
    
    "A half-hour already?"
    
    "I glance at Debra's notepad and try not to feel smug."
    
    "This interview couldn't be more in the bag."
    
    d "Ms. West. Frankly, 5/7 Publishing provides reading content that is primarily geared towards a male demographic between the ages of 18-35 and beyond."
    
    d "You're not our target audience, and while your insights would no doubt be enlightening, I have to ask..."

    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q5C:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 5
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_dependability +=1
    
    si "I'm really not as flexible as I'd like to be."
            
    si "I know deadlines change, and I know not everyone is perfect, but personally it pushes my buttons when not everyone is on top of their game, you know?"
    
    "I lean forward."
    
    si "I'm too much of a hard-worker to not see a project through to the end, so I prefer working with people who can also be sure to see things through to the end."
    
    "Debra looks satisfied."
    
    "It was an easy enough question-- all I had to do was reply in a way that showed that I had an issue, but not really one that would mess up my work at 5/7 Publishing."
    
    "It's a dangerous line to tread but..."
    
    "I glance at my watch discreetly."
    
    "A half-hour already?"
    
    "I glance at Debra's notepad and try not to feel smug."
    
    "This interview couldn't be more in the bag."
    
    d "Ms. West. Frankly, 5/7 Publishing provides reading content that is primarily geared towards a male demographic between the ages of 18-35 and beyond."
    
    d "You're not our target audience, and while your insights would no doubt be enlightening, I have to ask..."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q5D:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 5
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_imagination +=1
    
    "Ah, well... maybe it is a weakness. But..."
            
    si "I've found that I'm better suited with short-term projects."
            
    d "How so?"
            
    "I was hoping she wasn't going to ask that."
            
    si "Well, with long-term projects, I feel that the focus can get lost and it can be more of a struggle to make sure that the quality of the overall work can stay high."
            
    si "Working in a magazine gives opportunities for both, depending on the type of journalism one writes for."
    
    si "I've been improving, however."
    
    "{i}Please don't say, \"How so.\" Just buy it and let's move on."
    
    "The universe must hear me because she just lets out a quiet, thoughtful sigh before jotting down a quick note."
    
    "Debra looks satisfied."
    
    "It was an easy enough question-- all I had to do was reply in a way that showed that I had an issue, but not really one that would mess up my work at 5/7 Publishing."
    
    "It's a dangerous line to tread but..."
    
    "I glance at my watch discreetly."
    
    "A half-hour already?"
    
    "I glance at Debra's notepad and try not to feel smug."
    
    "This interview couldn't be more in the bag."
    
    d "Ms. West. Frankly, 5/7 Publishing provides reading content that is primarily geared towards a male demographic between the ages of 18-35 and beyond."
    
    d "You're not our target audience, and while your insights would no doubt be enlightening, I have to ask..."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q5E:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 5
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_honesty +=1
    
    si "I've been told that I need to be more... tactful at times."
            
    d "Oh?"
            
    si "Yes. That said, I've come to realize the importance of maintaining good relationships with my co-workers, so it's something I strive to overcome."
            
    "Actually, I think I'm pretty mild considering what I go through on a daily basis, but it doesn't hurt to lay it on thick."
            
    "I've never understood people who can dish it out but can't take it."
    
    "Debra looks satisfied."
    
    "It was an easy enough question-- all I had to do was reply in a way that showed that I had an issue, but not really one that would mess up my work at 5/7 Publishing."
    
    "It's a dangerous line to tread but..."
    
    "I glance at my watch discreetly."
    
    "A half-hour already?"
    
    "I glance at Debra's notepad and try not to feel smug."
    
    "This interview couldn't be more in the bag."
    
    d "Ms. West. Frankly, 5/7 Publishing provides reading content that is primarily geared towards a male demographic between the ages of 18-35 and beyond."
    
    d "You're not our target audience, and while your insights would no doubt be enlightening, I have to ask..."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
#-----------------------------------------------------------------------
    
label lbl_battle_intro_Q6A:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 6
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_imagination +=1
    
    "I can't say 'interesting' since that kind of makes me sound like I just want this job because the one I have now is boring."
            
    si "I wanted to do something a little more challenging."
    
    "Not that it isn't the truth, but I can't be showing out before I get hired, so..."
    
    "I smile brightly."
     
    si "The fact that I'm not 5/7 Publishing's target made it seem like working here would help me grow as a person, so when I heard you were hiring I jumped at the chance."
     
    "Debra nods slowly."
    
    d "Back when I was in your shoes, I can't say my reasons for wanting to join the company were similar, but I can definitely agree with your perspective."
    
    "I clear my throat politely."
    
    si "Uhm... Ms. Priestley, can I ask how long you've been working here?"
    
    d "It'll be twenty-eight years come March."
    
    "Wow. I would've never guessed..."
    
    si "And why did you interview to work here?"
    
    "Debra smiles at me wryly."
    
    d "Ask me again if you join the company."
    
    "Touché."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q6B:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 6
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_intellect +=1
    
    si "I earnestly believing working for 5/7 will be rewarding."
            
    "Even if it's my destiny to be working as a office coffee peddler for the next three years, it can't be worse than what I'm doing now."
            
    "Usually, one doesn't think of a 9-5 job as dead-end, but considering that I'd been an intern there since I started college and I'm {i}still{/i} an intern there, it seems more and more that my lack of promotion has to do with me doing my job so well that they're getting all the quality work without the quality pay."
            
    si "I feel my current job doesn't use me to my potential, so I just thought it would be nice to try new challenges in the work place."
    
    "Debra nods slowly."
    
    d "Back when I was in your shoes, I can't say my reasons for wanting to join the company were similar, but I can definitely agree with your perspective."
    
    "I clear my throat politely."
    
    si "Uhm... Ms. Priestley, can I ask how long you've been working here?"
    
    d "It'll be twenty-eight years come March."
    
    "Wow. I would've never guessed..."
    
    si "And why did you interview to work here?"
    
    "Debra smiles at me wryly."
    
    d "Ask me again if you join the company."
    
    "Touché."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q6C:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 6
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_kindness +=1
    
    si "It just seems like a nice place to work."
            
    "Debra blinks at me."
    
    d "Well, I won't say you're wrong but... nice in what way?"
    
    si "Oh! Uhm, well... I mean to say it seems nice because of the... environment."
    
    "Debra looks at me patiently, as though waiting for more, but I honestly don't know. I mean, it's not like I've worked here before."
    
    "My mind races to think of the types of magazines 5/7 Publishing prints."
    
    "Golfmania, The Daily Pitch, Ripped Quarterly, Cufflinks--"
    
    "Oh! Cufflinks!"
    
    si "As an example, fashion has always been--"
    
    "Simone West, if you dare say 'fashion has always been my passion' I'm going to fight you."
    
    si "--something that I enjoy greatly."
    
    "Good girl."
    
    si "If I were to work for one of 5/7 Publishing's flagship publications-- like 'Cufflinks'-- I can't think of anything better than getting to know people who feel the same about design the way that I do."
    
    d "Ah, I see. We have quite a few mens' fashion magazines but you're right in saying that Cufflinks is a flagship publication, so I'm assuming you have your eyes on one of those departments?"
    
    "A flare of panic goes through me and I rush to correct her."
    
    si "I do, but I was speaking hypothetically. I'm not against working in another department."
    
    "I can't seem picky, after all; I just want a job here. I'm so desperate to hand in my two week notice, I'd even work--"
    
    "Well, no. I was going to say 'in mail department' but sifting through piles of envelopes everyday for months seems both tragic and depressing. Not to mention the number it would do on my nails."
                
    "Debra nods slowly."
    
    d "Back when I was in your shoes, I can't say my reasons for wanting to join the company were similar, but I can definitely agree with your perspective."
    
    "I clear my throat politely."
    
    si "Uhm... Ms. Priestley, can I ask how long you've been working here?"
    
    d "It'll be twenty-eight years come March."
    
    "Wow. I would've never guessed..."
    
    si "And why did you interview to work here?"
    
    "Debra smiles at me wryly."
    
    d "Ask me again if you join the company."
    
    "Touché."
                
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q6D:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 6
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_honesty +=1
    
    si "There's a lot of companies on the market, but I feel like 5/7 has a real future."
            
    "Which is just interview talk meaning that I want ths job because 5/7 Publishing is going to keep my bills paid and a roof over my head but you know."
            
    "It'd be nice if I could just say 'I want to work here because you'll give me money and then I can spend it' but that wouldn't be an acceptable answer. It's a shame that true honesty isn't nearly as valued as it should be in the workplace."
    
    si "I think that it'll be extremely fulfilling."
    
    "But not nearly as fulfilling as that direct deposit every two weeks, ha."
    
    "Debra nods slowly."
    
    d "Back when I was in your shoes, I can't say my reasons for wanting to join the company were similar, but I can definitely agree with your perspective."
    
    "I clear my throat politely."
    
    si "Uhm... Ms. Priestley, can I ask how long you've been working here?"
    
    d "It'll be twenty-eight years come March."
    
    "Wow. I would've never guessed..."
    
    si "And why did you interview to work here?"
    
    "Debra smiles at me wryly."
    
    d "Ask me again if you join the company."
    
    "Touché."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q6E:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 6
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_dependability +=1
    
    si "I'm looking forward to having--"
            
    "Wait, I can't say that. If she knows people, she might not exactly like if I criticize the management."
    
    "But I already started talking, ack."
    
    "Debra looks at me expectantly, so I clear my throat and try again."
    
    si "Excuse me, I mean to say that I'm... looking forward to working alongside the editors in this company."
    
    si "I know that there are different styles of leadership and I've heard that 5/7 is one of the best. I just want to experience it myself and work in a, uhm, cohesive team."
    
    "Great. Now I sound like some kind of follower. I try my best to not look as annoyed at myself as I feel."
    
    "Debra nods slowly."
    
    d "Back when I was in your shoes, I can't say my reasons for wanting to join the company were similar, but I can definitely agree with your perspective."
    
    "I clear my throat politely."
    
    si "Uhm... Ms. Priestley, can I ask how long you've been working here?"
    
    d "It'll be twenty-eight years come March."
    
    "Wow. I would've never guessed..."
    
    si "And why did you interview to work here?"
    
    "Debra smiles at me wryly."
    
    d "Ask me again if you join the company."
    
    "Touché."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
#-----------------------------------------------------------------------
    
label lbl_battle_intro_Q7A:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 7
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_intellect +=1
    
    si "I like to think that I'll be working with people that'll listen to me."
            
    si "I don't mean in a leadership position, I just mean people I can work with who'll value what I have to say."
    
    "There's honestly nothing worse than working with people who always think they're right and won't listen to a second opinion, no matter how correct, useful, or helpful--"
    
    "I know that because that's exactly the kind of people I work with now."

    "Debra nods slowly."
    
    d "Back when I was in your shoes, I can't say my reasons for wanting to join the company were similar, but I can definitely agree with your perspective."
    
    "I clear my throat politely."
    
    si "Uhm... Ms. Priestley, can I ask how long you've been working here?"
    
    d "It'll be twenty-eight years come March."
    
    "Wow. I would've never guessed..."
    
    si "And why did you interview to work here?"
    
    "Debra smiles at me wryly."
    
    d "Ask me again if you join the company."
    
    "Touché."
    
    d "You seem like you've got a good head on your shoulders."

    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q7B:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 7
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_honesty +=1
    
    si "I think... I'd be happy if I was just in a position where my coworkers were reliable."
            
    si "For me, it's not so much 'where' I'm working as much as it is 'who' I'm working with."
    
    "Debra makes an interested 'hm' sound."
    
    d "You sound like a flexible person. That's definitely the kind of employee 5/7 Publishing is interested in hiring."
    
    "I smile vaguely."
    
    "I don't need flattery, I need a job offer-- but the sentiment is nice."
    
    "Debra nods slowly."
    
    d "Back when I was in your shoes, I can't say my reasons for wanting to join the company were similar, but I can definitely agree with your perspective."
    
    "I clear my throat politely."
    
    si "Uhm... Ms. Priestley, can I ask how long you've been working here?"
    
    d "It'll be twenty-eight years come March."
    
    "Wow. I would've never guessed..."
    
    si "And why did you interview to work here?"
    
    "Debra smiles at me wryly."
    
    d "Ask me again if you join the company."
    
    "Touché."
    
    d "You seem like you've got a good head on your shoulders."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q7C:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 7
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_imagination +=1
    
    si "Well, I know I love any job where I can stretch my creative muscles."
            
    si "If I got to work in an environment with a lot of room for ideas, I think I'd be pretty happy."
    
    d "Would you now?"
    
    "I pause."
    
    "Am I {i}not{/i} supposed to pick happiness then?"
    
    d "Back when I was in your shoes, I can't say my reasons for wanting to join the company were similar, but I can definitely agree with your perspective."
    
    "I clear my throat politely."
    
    si "Uhm... Ms. Priestley, can I ask how long you've been working here?"
    
    d "It'll be twenty-eight years come March."
    
    "Wow. I would've never guessed..."
    
    si "And why did you interview to work here?"
    
    "Debra smiles at me wryly."
    
    d "Ask me again if you join the company."
    
    "Touché."
    
    d "You seem like you've got a good head on your shoulders."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q7D:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 7
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_dependability +=1
    
    si "The occupation doesn't matter so much as the environment."
            
    si "I'd just like something a little more... freeing, I guess."
            
    d "Freeing in what way?"
            
    si "Just somewhere where I can speak my mind."
    
    "Debra nods slowly."
    
    d "Back when I was in your shoes, I can't say my reasons for wanting to join the company were similar, but I can definitely agree with your perspective."
    
    "I clear my throat politely."
    
    si "Uhm... Ms. Priestley, can I ask how long you've been working here?"
    
    d "It'll be twenty-eight years come March."
    
    "Wow. I would've never guessed..."
    
    si "And why did you interview to work here?"
    
    "Debra smiles at me wryly."
    
    d "Ask me again if you join the company."
    
    "Touché."
    
    d "You seem like you've got a good head on your shoulders."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
    
label lbl_battle_intro_Q7E:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $Battle_Question_Current = 7
    $SetResult(Battle_Question_Current, 'progress')
    $StopBattleTimer()
    
    $stat_kindness +=1
    
    si "In a place with people I actually like, for starters."
            
    "Debra snorts."
    
    d "Amen to that."
    
    "I'm not sure I heard her correctly."
    
    si "Excuse me?"
    
    d "Hm?"
    
    si "Oh, I... {w}nevermind. {w}Just what I was saying before, that I'd like to be around people who I enjoy working with, just on a general basis."

    "Debra nods slowly."
    
    d "Back when I was in your shoes, I can't say my reasons for wanting to join the company were similar, but I can definitely agree with your perspective."
    
    "I clear my throat politely."
    
    si "Uhm... Ms. Priestley, can I ask how long you've been working here?"
    
    d "It'll be twenty-eight years come March."
    
    "Wow. I would've never guessed..."
    
    si "And why did you interview to work here?"
    
    "Debra smiles at me wryly."
    
    d "Ask me again if you join the company."
    
    "Touché."
    
    d "You seem like you've got a good head on your shoulders."
    
    $ResetBattleTimer()
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)    
    jump expression _return
    return
#-----------------------------------------------------------------------
    
label lbl_battle_intro_Q8A:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $StopBattleTimer()
    
    $stat_dependability +=1
    
    si "What would you say is a standard day here?"
            
    "Debra blinks at me strangely."
            
    "I say strangely because she's only using one ey-- oh. {w}She's winking at me."
            
    "How... out of character."
            
    d "An excellent question, but not one I believe you'll be asking for long."
            
    d "I'm sure you'll find out on your first day."
            
    "Wait a second... is Debra saying--"
    
    d "Alright. We're finished here."
    
    "Debra is nodding before I even finish my answer, scribbling notes at a more furious pace than I've seen her do the entire interview."
    
    "I'm... going to take that as a good sign."
    
    "I look at her pointedly but she pays me no attention until she completes her note."
    
    d "...Okay, then."
    
    "Finally satisfied, she places down her pen to meet my eyes with what I'd call a pleased expression on literally anyone else's face, but with the same fierce eyes that make her just look like she'd destroy me anyway."
    
    d "Ms. West, it's been a pleasure getting to know you."
    
    si "Thank you, Ms. Priestley."
    
    d "We'll notify you if we choose to have you on board. If I can just say, you've been a great candidate."
    
    "The words are kind of surprising-- especially since her eyes haven't smiled once this entire time-- but I'll take what I can get."
    
    jump lbl_battle_intro_End  
    
label lbl_battle_intro_Q8B:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $StopBattleTimer()
    
    $stat_kindness +=1
    
    si "Well, between you and me... do you like working here? I mean, you personally."
            
    "She looks surprised at the personal question."
            
    d "I... do, yes."
    
    d "It's definitely not what I expected to be doing after almost three decades, but it's not the type of job you can just walk away from."
    
    d "It's very exciting, and I'm sure you'll fit in right away."
    
    "Wait... 'fit in'?"
    
    d "Alright..."
    
    "Debra is nodding before I even finish my answer, scribbling notes at a more furious pace than I've seen her do the entire interview."
    
    "I'm... going to take that as a good sign."
    
    "I look at her pointedly but she pays me no attention until she completes her note."
    
    d "...Okay, then."
    
    "Finally satisfied, she places down her pen to meet my eyes with what I'd call a pleased expression on literally anyone else's face, but with the same fierce eyes that make her just look like she'd destroy me anyway."
    
    d "Ms. West, it's been a pleasure getting to know you."
    
    si "Thank you, Ms. Priestley."
    
    d "We'll notify you if we choose to have you on board. If I can just say, you've been a great candidate."
    
    "The words are kind of surprising-- especially since her eyes haven't smiled once this entire time-- but I'll take what I can get."

    jump lbl_battle_intro_End  
    
label lbl_battle_intro_Q8C:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $StopBattleTimer()
    
    $stat_imagination +=1
    
    si "Is there anything you like the most about working here?"
            
    d "It keeps the lights on, so I like it just fine."
            
    "When her expressionless appearance doesn't change I realize that I have no clue if she's being serious or not."
            
    "I open my mouth, then close it."
            
    "Maybe... it's better if I don't say anything at all."
    
    d "Alright. We're finished here."
    
    "Debra is nodding before I even finish my answer, scribbling notes at a more furious pace than I've seen her do the entire interview."
    
    "I'm... going to take that as a good sign."
    
    "I look at her pointedly but she pays me no attention until she completes her note."
    
    d "...Okay, then."
    
    "Finally satisfied, she places down her pen to meet my eyes with what I'd call a pleased expression on literally anyone else's face, but with the same fierce eyes that make her just look like she'd destroy me anyway."
    
    d "Ms. West, it's been a pleasure getting to know you."
    
    si "Thank you, Ms. Priestley."
    
    d "We'll notify you if we choose to have you on board. If I can just say, you've been a great candidate."
    
    "The words are kind of surprising-- especially since her eyes haven't smiled once this entire time-- but I'll take what I can get."
    
    
    jump lbl_battle_intro_End  
    
label lbl_battle_intro_Q8D:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $StopBattleTimer()
    
    $stat_intellect +=1
    
    "I mean, she asked about my thoughts on my future, so it won't make me sound too cynical to ask about the future of the company, will it...?"
            
    si "Do you think... 5/7 Publishing will have a future?"
            
    "Debra looks mildly amused."
            
    d "Well, I'm not exactly the type to dabble in our stock portfolio, but we've been pretty stable. There haven't been any economy-related layoffs, if that's what you're asking."
            
    d "Anything else... well, you'll just have to work here and find out."
            
    si "Hm..."
            
    "I flash her a small smile."
            
    si "I guess I will, won't I?"
    
    d "Alright. We're finished here."

    "Debra is nodding before I even finish my answer, scribbling notes at a more furious pace than I've seen her do the entire interview."
    
    "I'm... going to take that as a good sign."
    
    "I look at her pointedly but she pays me no attention until she completes her note."
    
    d "...Okay, then."
    
    "Finally satisfied, she places down her pen to meet my eyes with what I'd call a pleased expression on literally anyone else's face, but with the same fierce eyes that make her just look like she'd destroy me anyway."
    
    d "Ms. West, it's been a pleasure getting to know you."
    
    si "Thank you, Ms. Priestley."
    
    d "We'll notify you if we choose to have you on board. If I can just say, you've been a great candidate."
    
    "The words are kind of surprising-- especially since her eyes haven't smiled once this entire time-- but I'll take what I can get."
    
    jump lbl_battle_intro_End      
    
label lbl_battle_intro_Q8E:
    $WriteToFile("")    
    $SetResult(Battle_Question_Current, 'correct')
    $StopBattleTimer()
    
    $stat_honesty +=1
    
    "Okay, so maybe I {i}shouldn't{/i} ask but..."
            
    "Eh, it's never stopped me before."
            
    si "How did I do in comparison with other candidates you're considering?"
            
    "Debra doesn't look too surprised that I've asked."
            
    d "I'd say you're a strong contender."
            
    "Tsk. A noncommital reply."
    
    d "Alright. We're finished here."
    
    "She breaks eye contact, scribbling notes at a more furious pace than I've seen her do the entire interview."
    
    "I'm... going to take that as a good sign."
    
    "I look at her pointedly but she pays me no attention until she completes her note."
    
    d "...Okay, then."
    
    "Finally satisfied, she places down her pen to meet my eyes with what I'd call a pleased expression on literally anyone else's face, but with the same fierce eyes that make her just look like she'd destroy me anyway."
    
    d "Ms. West, it's been a pleasure getting to know you."
    
    si "Thank you, Ms. Priestley."
    
    d "We'll notify you if we choose to have you on board. If I can just say, you've been a great candidate."
    
    "The words are kind of surprising-- especially since her eyes haven't smiled once this entire time-- but I'll take what I can get."
    
    jump lbl_battle_intro_End  
    
#-----------------------------------------------------------------------

label lbl_battle_intro_End:

    stop music fadeout 1.0
    
    play music "music/work.mp3"

    "She reaches out her hand to shake mine firmly."
    
    d "Alright, thank you for today. I'm sure you'll hear from us very soon."
    
    "{i}Oh?{/i}"
    
    si smile "It was nice meeting you, too, Debrow-- Debra."
    
    "I correct myself quickly as I withdraw my hand. I don't think she caught it, especially not since she's smiling at me with something almost like warmth."
    
    "Or maybe not. The eyebrow makes it hard to tell."
    
    "Oh, geez."
    
    jump Tut_battle_fin
    

###################### Tutorial Battle #######################################

label lbl_Battle_Tutorial_End:
  
  "That's the end of the Tutorial, hope it was useful."
  $persistent.BattleTutorialComplete = True
  return
  
label lbl_Battle_Tutorial_Skip:
  
  window show
  return

label lbl_Battle_Tutorial_Start:

  window hide
  if persistent.BattleTutorialComplete:
    call screen yesno_prompt("Do you wish to see the battle tutorial?", Return("Yes"), Return("No"))
    if _return == "No":
      jump lbl_Email_Tutorial_Skip
      

  call screen screen_tutorialShow(10, "Welcome to the battle introduction screen!")
  
  call screen screen_tutorialShow(10, "Battles are quick ways for Simone to gain stats.")

  call screen screen_tutorialShow(11, "On the battle introduction screen, you can hover over \"GOAL\" to learn what the objective of the battle is.")

  call screen screen_tutorialShow(12, "Hovering over \"HINT\" will help you figure out how to succeed in doing so.")

  call screen screen_tutorialShow(13, "Next, we have the battle screen itself.")

  call screen screen_tutorialShow(13, "There are six stats that Simone can gain over the next two weeks. Respectively, they are honesty, kindness, intellect, imagination, dependability, and laziness.")

  call screen screen_tutorialShow(13, "Six might seem like a lot, but don't worry. You'll be able to track them via \"emails\", which we'll talk about later.")

  call screen screen_tutorialShow(14, "The potential replies on the battle all align with a specific stat.")

  call screen screen_tutorialShow(13, "Usually, battles will give you only three options (thus concentrating on just three stats) but this is just a tutorial and stat-wise, Simone is a clean slate.")

  call screen screen_tutorialShow(13, "Think of this as a beginner's boost!")

  call screen screen_tutorialShow(13, "Based on the \"HINT\" given per-battle, it should be clear that one of the stats should be avoided, so don't give answers that align that way.")

  call screen screen_tutorialShow(15, "If Simone raises a stat--particularly one that grates against a client too often--the battle will end and you will have lost.")  

  call screen screen_tutorialShow(15, "Losing a battle will always have plot consequences.")

  call screen screen_tutorialShow(15, "In addition, Simone take a dip in all stats except the last one she raised.")
  
  call screen screen_tutorialShow(13, "That said, there are no wrong answers in this \"interview\" battle.")

  call screen screen_tutorialShow(13, "And that's all you need to know about battles!")

  window show
  
  jump lbl_Battle_Tutorial_End