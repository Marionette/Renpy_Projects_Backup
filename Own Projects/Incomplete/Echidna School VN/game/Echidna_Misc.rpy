
  #------------------------------------------------------
init python:
  #------------------------------------------------------
  
  #######################################################
  #Music functions
  #------------------------------------------------------
  def GetMusicByMood(mood):
    if mood == 'gloom':      
      return renpy.random.choice(List_Music_Gloom)
    
    if mood == 'light':
      return renpy.random.choice(List_Music_Light)
      
    return renpy.random.choice(List_Music_Default)
        
  #------------------------------------------------------
  #Adds a random song to the music queue (hardcoded to return 'Light' music atm)
  def QueueNextMusic():
    renpy.music.queue(GetMusicByMood('light'))
    
    return
  #------------------------------------------------------
  #Adds a random song to the music queue every time the queue is empty, ie. infinite music
  def StartCallbackMusicQueue():
    renpy.music.set_queue_empty_callback(QueueNextMusic)
    
    return
  #------------------------------------------------------
  def EndCallbackMusicQueue():
    renpy.music.set_queue_empty_callback(EmptyFunction)
    renpy.music.stop()
    
    return
  #------------------------------------------------------
  #Empty function to pass to the callback (effectivly killing it)
  def EmptyFunction():
    return
  #------------------------------------------------------
  
  #######################################################
  #Value to string converter functions
  #------------------------------------------------------
  def GetHappinessString(happinessValue):
    happiness = "Neutral"
    if happinessValue >= 0 and happinessValue <= 10 :
      happiness = "Depressed"    
    if happinessValue > 10 and happinessValue <= 20:
      happiness = "Sad"
    if happinessValue > 20 and happinessValue <= 30 :
      happiness = "Unhappy"
    if happinessValue > 30 and happinessValue <= 40 :
      happiness = "Neutral"
    if happinessValue > 40 and happinessValue <= 50 :
      happiness = "Content"
    if happinessValue > 50 and happinessValue <= 60 :
      happiness = "Cheerful"
    if happinessValue > 60 and happinessValue <= 70 :
      happiness = "Happy"
    if happinessValue > 70 and happinessValue <= 80 :
      happiness = "Overjoyed"
    if happinessValue > 80 and happinessValue <= 90 :
      happiness = "Ecstatic"
    if happinessValue > 90 and happinessValue <= 100 :
      happiness = "Blissful"
    
    return happiness    
  #------------------------------------------------------
  
  def GetRelationshipString(relationshipValue, isAChild):
    if (isAChild == False):
      relationship = "Acquaintance"
      if relationshipValue >= 0 and relationshipValue <= 20:
        relationship = "Stranger"
      if relationshipValue > 20 and relationshipValue <= 40 :
        relationship = "Acquaintance"
      if relationshipValue > 40 and relationshipValue <= 60 :
        relationship = "Friendly"
      if relationshipValue > 60 and relationshipValue <= 80 :
        relationship = "Romantic"
      if relationshipValue > 80 and relationshipValue <= 100 :
        relationship = "Loved"
    else:
      relationship = "Acquaintance"
      if relationshipValue >= 0 and relationshipValue <= 20:
        relationship = "Stranger"
      if relationshipValue > 20 and relationshipValue <= 40 :
        relationship = "Acquaintance"
      if relationshipValue > 40 and relationshipValue <= 60 :
        relationship = "Friendly"
      if relationshipValue > 60 and relationshipValue <= 80 :
        relationship = "Admired"
      if relationshipValue > 80 and relationshipValue <= 100 :
        relationship = "Idolized"    
    
    return relationship    
  #------------------------------------------------------
      
  def GetScoreGrade(scoreValue):
    grade = "C"
    if scoreValue >= 0 and scoreValue <= 10 :
      grade = "F"    
    if scoreValue > 10 and scoreValue <= 20:
      grade = "E"
    if scoreValue > 20 and scoreValue <= 30 :
      grade = "D"
    if scoreValue > 30 and scoreValue <= 40 :
      grade = "C-"
    if scoreValue > 40 and scoreValue <= 50 :
      grade = "C"
    if scoreValue > 50 and scoreValue <= 60 :
      grade = "B-"
    if scoreValue > 60 and scoreValue <= 70 :
      grade = "B"
    if scoreValue > 70 and scoreValue <= 80 :
      grade = "A"
    if scoreValue > 80 and scoreValue <= 90 :
      grade = "A+"
    if scoreValue > 90 and scoreValue <= 100 :
      grade = "A*"
    
    return grade  
  
  #------------------------------------------------------
  
  def CurrentTimeToInt(currentTime):
    currTime = 0
    if currentTime == "Morning":
      currTime = 0
    if currentTime == "First Period":
      currTime = 1
    if currentTime == "Lunch":
      currTime = 2
    if currentTime == "Second Period":
      currTime = 3
    if currentTime == "After School":
      currTime = 4
    if currentTime == "Evening":
      currTime = 5
    
    return currTime    
  #------------------------------------------------------
  
  def SetCurrentCharacterNumber(_num):
    global current_speaker_number
    global current_speaker
    debug_print("Current Speaker - " + str(current_speaker_number) + ", " + str(current_speaker) )
    
    current_speaker_number = _num
    return
        
  def GetCurrentCharacterNameLength():
    global current_speaker
    return len(current_speaker)
    
  def GetTechingSubject(_dayNum, _period):
  
    index = _dayNum + ((_period - 1) * 5)
    
    return TeachingPlan_ThisWeek[index]
      
  #------------------------------------------------------