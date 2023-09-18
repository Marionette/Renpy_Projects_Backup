
init -1 python :
  #######################################################
  def debug_print(_msg):
    return # comment out to print debug messages
    with open("F:\[Projects]\RenpyGames\Head of the Class\game\log.txt", "a") as myfile:
      myfile.write(_msg)
      myfile.write("\n")
  #######################################################
  
  #------------------------------------------------------  
  
  def weekDay(day):
    #Note: Only works for 30 days where Monday starts at 1
    week   = ['Monday', 
              'Tuesday', 
              'Wednesday', 
              'Thursday',  
              'Friday', 
              'Saturday',
              'Sunday'] 
    dayOfWeek = day
    while dayOfWeek > 7:
      dayOfWeek = dayOfWeek - 7
    #debug_print(str(dayOfWeek)+" ,"+week[dayOfWeek-1])
    return week[dayOfWeek-1]
  
  def IsSchoolDay(day):
    
    day = weekDay(day)
    
    if (day == 'Saturday' or day == 'Sunday'):
      return False
      
    return True
  
  #------------------------------------------------------  
  
  def AddScoreToAll(Subject, value):
    for character in List_Students:
      character.AddScore(Subject, value)
      
    for character in List_side_characters:
      character.AddScore(Subject, value)
      
    return
    
  def AddMoodToAll(value):
    for character in List_Students:
      character.AddMood(value)
      
    for character in List_side_characters:
      character.AddMood(value)
      
    return
    
  def ApplyScoreDegredation():
    for character in List_Students:
      character.ApplyDegredation()  
      
    for character in List_side_characters:
      character.ApplyDegredation() 
    
  def MoodMultiplierInEffect():
    multiplier = False
    penalty = False
    for character in List_Students:
      if character.Mood > 70:
        multiplier = True
      if character.Mood == 0:
        penalty = True
      
    for character in List_side_characters:
      if character.Mood > 70:
        multiplier = True
      if character.Mood == 0:
        penalty = True
      
    return [multiplier, penalty]
    
  def CalculateAverageScores():
    history = 0
    science = 0
    math = 0
    literacy = 0
    language = 0
    geography = 0
    for character in List_side_characters:
      history += character.History
      science += character.Science
      math += character.Math
      literacy += character.Literacy
      language += character.Language
      geography += character.Geography
      
    count = len(List_side_characters)
    
    Character_Average.History =   int(history/count)
    Character_Average.Science =   int(science/count)
    Character_Average.Math =      int(math/count)
    Character_Average.Literacy =  int(literacy/count)
    Character_Average.Language =  int(language/count)
    Character_Average.Geography = int(geography/count)
    
    
  #------------------------------------------------------
  
  def GetRandomSideStudent():
    return renpy.random.choice(List_Students_Side)
  
  #------------------------------------------------------ 
  def GetCurrentMinutes(): 
    from datetime import datetime  
    return datetime.now().minute
    
  #------------------------------------------------------  
  def RecordClassOutcome(_subject, _outcome):
    outcome = [_subject, _outcome]
    List_classes_taught.append(outcome)
    
  def GetOutcomeDescription(_outcome):
    outcomeText="Not sure what this means: "+ _outcome
    #standard
    if _outcome == "Success":
      outcomeText="The class was a Success!"
    if _outcome == "Fail":
      outcomeText="The class was a Failure!"
      
    #mood modifiers
    if _outcome == "Bad Mood":
      outcomeText="The class was in a bad mood and didn't pay as much attention as usual!"
    if _outcome == "Good Mood":
      outcomeText="The class was in a good mood and paid more attention than usual!"
      
    #stress
    if _outcome == "Fainted":
      outcomeText="The stress was too much and I fainted and didn't get a chance to teach anything!"
    if _outcome == "Zen":
      outcomeText="I was so relaxed my teaching just kept flowing!"
    
    #bonus
    if _outcome == "Bonus Craig":
      outcomeText="The class was a Success, Craig learned a lot!"
    if _outcome == "Bonus Hecate":
      outcomeText="The class was a Success, Hecate learned a lot!"
    if _outcome == "Bonus Sanura":
      outcomeText="The class was a Success, Sanura learned a lot!"
    
    #random events
    if _outcome == "Got Lost":
      outcomeText="I got lost and didn't get a chance to teach anything!"
      
    return outcomeText
    
  def GetClassOutcomes(_day):
    if _day*2+1 < len(List_classes_taught):
      
      morning_class = List_classes_taught[_day*2+0]
      afternoon_class = List_classes_taught[_day*2+1]
      
      return [morning_class, afternoon_class]
    else:
     return [["Nothing", ""], ["Nothing", ""]]
     
  def ClassTaughtSince(_subject, _daysAgo, includeToday=True):  
    classlist = [] 
    classes = []
    startDay = 0
    if not includeToday:
      startDay = 1
    daysOffset = _daysAgo*2
    #for count in range(startDay, _daysAgo):
    #  classlist += GetClassOutcomes(current_day-count)
    if len(List_classes_taught) > daysOffset:
      classlist = List_classes_taught[-daysOffset:]
    else:
      classlist = List_classes_taught
    
    for outcome in classlist:
      classes += outcome

    #debug_print("ClassTaughtSince: " + str(classes))    
    if _subject in classes:
      return True
        
    return False
  #------------------------------------------------------  
      
  def GetGrade(scoreValue):
    grade = "F"
    if scoreValue >= 0 and scoreValue <= 44 :
      grade = "F"    
    if scoreValue >= 45 and scoreValue <= 49:
      grade = "E-"   
    if scoreValue >= 50 and scoreValue <= 54:
      grade = "E"   
    if scoreValue >= 55 and scoreValue <= 59:
      grade = "D-"
    if scoreValue >= 60 and scoreValue <= 64 :
      grade = "D"
    if scoreValue >= 65 and scoreValue <= 69 :
      grade = "C-"
    if scoreValue >= 70 and scoreValue <= 74 :
      grade = "C"
    if scoreValue >= 75 and scoreValue <= 79 :
      grade = "B-"
    if scoreValue >= 80 and scoreValue <= 84 :
      grade = "B"
    if scoreValue >= 85 and scoreValue <= 89 :
      grade = "A-"
    if scoreValue >= 90 and scoreValue <= 94 :
      grade = "A"
    if scoreValue >= 95 and scoreValue <= 99 :
      grade = "A+"
    if scoreValue >= 100 :
      grade = "A*"
    
    return grade  
  
  
  def GetGradeTextColored(_score):
    grade = GetGrade(_score)
    
    if _score >= 100:
      return "{color=#f3f130}" + grade + "{/color}"
    else:
      if _score >= 70:
        return "{color=#46f018}" + grade + "{/color}"
      else:
        return "{color=#f02318}" + grade + "{/color}"
        
  def GetDifficultyRating():
    difficulty = 0
    if feature_unlock_penalty_backToBack:
      difficulty += 2
    if feature_unlock_penalty_ScoreDegradation:
      difficulty += 2
    if feature_unlock_bonus_Mood:
      difficulty += 2
    #if feature_unlock_bonus_favourites:
    #  difficulty -= 1
    if feature_unlock_penalty_stress:
      difficulty += 1
      
    difficulty_text  = "Easy"
    if difficulty <= 1:
      difficulty_text  = "Easy"
    if difficulty >= 2:
      difficulty_text  = "Normal"
    if difficulty >= 4:
      difficulty_text  = "Difficult"
    if difficulty >= 6:
      difficulty_text  = "Hard"
      
    return difficulty_text
  
  #------------------------------------------------------  
transform testbubble:
    xalign .8
    yanchor .5
    ypos (bubble_ybase+400)
    alpha 0.0
    on show:
        ypos (bubble_ybase+400)
        pause bubble_delay
        parallel:
            linear 1.0 alpha 1.0
            pause 1.0
            linear 1.0 alpha 1.0 
            Null()
        parallel:
            linear 3.0 ypos (bubble_ybase-10)
    on hide:
        ypos (bubble_ybase+600)
            
init python:
    bubble_ybase = 0
    bubblenum = 0
    bubble_delay = 0.001
    
    def bubble_ybase_tick():
        global bubble_ybase
        bubble_ybase -= 50
        
    def bubble(s,bg,delay=0.001):
        #if persistent.hide_feedback:
        #    return
        global bubblenum
        bubbles = 'bubble'+str(bubblenum)
        w = ui.window(background=Frame(bg,16,16),xminimum=740,yminimum=483,xfill=False,xmaximum=1140,left_padding=20,right_padding=20)
        w.add(ui.text(s,xmaximum=800,color='#000',xalign=.5))
        ui.remove(w)
        global bubble_delay
        bubble_delay = delay
        renpy.show(bubbles,what=w,at_list=[testbubble,])
        #renpy.hide(bubbles)
        bubblenum += 1
        
    def show_test(caption, val, invert=False, delay=0.001, partial=None):
        s = 'Test: '+caption+u' ? '
        if invert ^ val:
            res_s = 'Success'
        elif partial:
            res_s = 'Partial Success'
        else:
            res_s = 'Failed'
        s = _(u'Test: %(caption)s -> %(result)s')%dict(caption=_(caption),result=_(res_s))
        
        bg = ((invert ^ val) and 'gui/bubble-success.png') or 'gui/bubble-fail.png'
        bubble(s,bg,delay=delay)
        return val
        
    def show_moodChange(val=-5, invert=False, _delay=0.001, partial=None):
      if val > 0:
        bg = 'gui/notify/mood_pos.png'
        s = ""#"Mood" + " +" + str(val)
      else:
        bg = 'gui/notify/mood_neg.png'
        s = ""#"Mood" + " " + str(val)
        
      bubble(s,bg,delay=_delay)
      
        
    def show_scoreChange(caption="", val=0, invert=False, delay=0.001, partial=None):
        bg = 'gui/notify/learn_pos.png'
        s = ""#caption + " +" + str(val)
        bubble(s,bg,delay=delay)
        
    def show_relationshipChange(caption="", val=0, invert=False, _delay=0.001, partial=None):
        bg = 'gui/notify/relationship_pos.png'
        s = ""#caption + " +" + str(val)
        bubble(s,bg,delay=_delay)
  #------------------------------------------------------  