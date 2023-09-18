
  #------------------------------------------------------
init python:

  #######################################################
  def debug_print(_msg):
    return # comment out to print debug messages
    with open("F:\[Projects]\RenpyGames\School Road\game\log.txt", "a") as myfile:
      myfile.write(_msg)
      myfile.write("\n")
  #######################################################
    
  #------------------------------------------------------  
  # Variables
  #------------------------------------------------------ 
  CurrentDay = 0
  CurrentTime = [0,0]
  CurrentLocation = "Nowhere"
  IsTimeStopped = False
  #------------------------------------------------------ 
  
  #------------------------------------------------------ 
  ## Time Funtions
  #------------------------------------------------------ 
  def SetTime(_hour, _min):
    global CurrentTime    
    CurrentTime = [_hour, _min]  
    #debug_print(str(CurrentTime) + ", " + str(_hour) + ", " + str(_min) + " = ")  
    return 
  #------------------------------------------------------ 
  
  def GetTime():
    global CurrentTime        
    return CurrentTime
  #------------------------------------------------------ 
  
  def AdvanceTimeMins(_min=10):
    global CurrentTime    
    CurrentTime[1] += _min
    
    if CurrentTime[1] >= 60:      
      CurrentTime[0] += 1
      CurrentTime[1] = CurrentTime[1] - 60
      
    return 
  #------------------------------------------------------ 
  
  def IsTimePast(_time):
    global CurrentTime    
      
    if CurrentTime[0] > _time[0]:
      return true
      
    return CurrentTime[0] == _time[0] and CurrentTime[1] > _time[1]
  #------------------------------------------------------ 
    
  def GetCurrentTimeString(): 
    global CurrentTime    
    if CurrentTime[0] < 10:
      hstr = "0" + str(CurrentTime[0])
    else:
      hstr = str(CurrentTime[0])
      
    if CurrentTime[1] < 10:
      mstr = "0" + str(CurrentTime[1])
    else:
      mstr = str(CurrentTime[1])
      
    return hstr + ":" + mstr
  #------------------------------------------------------ 
  #------------------------------------------------------ 
  ## Location Funtions
  #------------------------------------------------------ 
  def SetLocation(_location):
    global CurrentLocation    
    CurrentLocation = _location      
    return 
  #------------------------------------------------------ 
  
  def GetLocation():
    global CurrentLocation        
    return CurrentLocation
  #------------------------------------------------------ 
    