
  #------------------------------------------------------
init python:

  #######################################################
  def debug_print(_msg):
    #return # comment out to print debug messages
    with open("F:\[Projects]\RenpyGames\Justin Thyme\game\log.txt", "a") as myfile:
      myfile.write(_msg)
      myfile.write("\n")
  #######################################################
    
  #------------------------------------------------------  
  # Variables
  #------------------------------------------------------ 
  CurrentDay = 0
  CurrentTime = 0
  CurrentLocation = 0
  #------------------------------------------------------ 
  
  #------------------------------------------------------ 
  ## Time Funtions
  #------------------------------------------------------ 
  def SetTime(_hour):
    global CurrentTime    
    CurrentTime = _hour      
    return 
  #------------------------------------------------------ 
  
  def GetTime():
    global CurrentTime        
    return CurrentTime
  #------------------------------------------------------ 
  
  def AdvanceTime(_hours=1):
    global CurrentTime    
    CurrentTime += _hours
    
    if CurrentTime >= 24:
      CurrentTime = CurrentTime - 24
      
    return 
  #------------------------------------------------------ 
  
  def IsTimePast(_time):
    global CurrentTime    
      
    return CurrentTime > _time
  #------------------------------------------------------ 
    
  def GetTimeString(_time):    
    return TimesOfTheDay[_time]
    return 
  #------------------------------------------------------ 
    
  #------------------------------------------------------ 
  ## Day Funtions
  #------------------------------------------------------  
  def SetDay(_day):
    global CurrentDay    
    CurrentDay = _day     
    return 
  #------------------------------------------------------ 
  
  def GetDay():
    global CurrentDay        
    return CurrentDay
  #------------------------------------------------------ 
  
  def AdvanceDay(_days=1):
    global CurrentDay    
    CurrentDay += _days
    
    if CurrentDay >= 7:
      CurrentDay = CurrentDay - 7
      
    return 
  #------------------------------------------------------ 
  
  def IsDayPast(_Day):
    global CurrentDay    
      
    return CurrentDay > _Day
  #------------------------------------------------------ 
    
  def GetDayString(_day):    
    return DaysOfTheWeek[_day][0]
    return 
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
    
  def GetLocationString(_location):    
    return AvailableLocations[_location][1]
    return 
  #------------------------------------------------------ 
    
  #------------------------------------------------------ 
  ## Character Funtions
  #------------------------------------------------------ 
  
  
    
  #------------------------------------------------------
  #------------------------------------------------------
  class CharacterClass:
    #stats
    Name = "???"
    Age = 13
    Gender = "Male"
    
    Mood = "Neutral"
    
    Schedule = []
    
    Alive = True
    
    def __init__(self, _name="???", _age=20, _gender="Male", _mood = "neutral", _schedule=[]):
      self.Name = _name
      self.Age = _age
      self.Gender = _gender
      self.Mood = _mood
      self.Schedule = _schedule
      
    
    def SetName(self, _name):
      self.Name = _name
    
    def SetAge(self, _age):
      self.Age = _age
    
    def SetGender(self, _gender):
      self.Gender = _gender
    
    def SetMood(self, _mood):
      self.Mood = _mood
    
    def SetSchedule(self, _schedule):
      self.Schedule = _schedule
      
    def SetCharacterStats(self, _name, _age, _gender, _mood = "neutral"):
      self.Name = _name
      self.Age = _age
      self.Gender = _gender
      self.Mood = _mood
    
    def IsAlive(self):
      return self.Alive
  #------------------------------------------------------
  #------------------------------------------------------
  Postman_Schedule_Monday = [ "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "WakeUp",
                              "PostOffice",
                              "PostOffice",
                              "Church",
                              "Inn",
                              "Cafe",
                              "School",
                              "PoliceStation",
                              "Hospital",
                              "Store",
                              "PostOffice",
                              "Pub",
                              "Home",
                              "Home",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep"]
                              
  Barista_F_Schedule_Monday = [ "Sleep",
                                "Sleep",
                                "Sleep",
                                "Sleep",
                                "Sleep",
                                "Sleep",
                                "Sleep",
                                "Sleep",
                                "Wakeup",
                                "School",
                                "Store",
                                "Park",
                                "Park",
                                "Cafe",
                                "Cafe",
                                "Cafe",
                                "Cafe",
                                "School",
                                "Park",
                                "Park",
                                "Home",
                                "Home",
                                "Home",
                                "Sleep"]
  
  Lady_Schedule_Monday = [  "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "WakeUp",
                            "Mansion",
                            "Mansion",
                            "Cafe",
                            "Cafe",
                            "Park",
                            "School",
                            "Cafe",
                            "Hospital",
                            "Mansion",
                            "Mansion",
                            "School",
                            "Park",
                            "Mansion",
                            "Mansion",
                            "Sleep",
                            "Sleep"]

  Teacher_Schedule_Monday = [ "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "WakeUp",
                              "Cafe",
                              "School",
                              "School",
                              "School",
                              "School",
                              "School",
                              "School",
                              "School",
                              "School",
                              "School",
                              "Death",
                              "Home",
                              "Home",
                              "Home",
                              "Sleep",
                              "Sleep"]

  Nun_Schedule_Monday = [ "Sleep",
                          "Sleep",
                          "Sleep",
                          "Sleep",
                          "Sleep",
                          "Sleep",
                          "WakeUp",
                          "Church",
                          "Church",
                          "School",
                          "Church",
                          "Church",
                          "Church",
                          "Cafe",
                          "Church",
                          "Church",
                          "School",
                          "Church",
                          "Church",
                          "Church",
                          "Church",
                          "Sleep",
                          "Sleep",
                          "Sleep"]

  Innkeeper_Schedule_Monday = [ "Sleep",
                                "Sleep",
                                "Sleep",
                                "Sleep",
                                "Sleep",
                                "Sleep",
                                "WakeUp",
                                "Cafe",
                                "Inn",
                                "Inn",
                                "Inn",
                                "Inn",
                                "Inn",
                                "Pub",
                                "Pub",
                                "Inn",
                                "Inn",
                                "Inn",
                                "Store",
                                "Inn",
                                "Inn",
                                "Inn",
                                "Sleep",
                                "Sleep"]

  HomelessGuy_Schedule_Monday = [ "Sleep",
                                  "Sleep",
                                  "Sleep",
                                  "Sleep",
                                  "Sleep",
                                  "Sleep",
                                  "Sleep",
                                  "Sleep",
                                  "Sleep",
                                  "WakeUp",
                                  "Park",
                                  "Park",
                                  "Park",
                                  "Cafe",
                                  "Park",
                                  "Park",
                                  "Pub",
                                  "Church",
                                  "School",
                                  "Church",
                                  "Park",
                                  "Park",
                                  "Park",
                                  "Sleep"]

  Shopkeeper_Schedule_Monday = [ "Sleep",
                                  "Sleep",
                                  "Sleep",
                                  "Sleep",
                                  "Sleep",
                                  "Sleep",
                                  "Sleep",
                                  "WakeUp",
                                  "Cafe",
                                  "Store",
                                  "Store",
                                  "Store",
                                  "Store",
                                  "Cafe",
                                  "Store",
                                  "Store",
                                  "Store",
                                  "Store",
                                  "Store",
                                  "Pub",
                                  "Home",
                                  "Home",
                                  "Sleep",
                                  "Sleep"]

  Barista_M_Schedule_Monday = [ "Sleep",
                                "Sleep",
                                "Sleep",
                                "Sleep",
                                "Sleep",
                                "Sleep",
                                "WakeUp",
                                "Cafe",
                                "Cafe",
                                "Cafe",
                                "Cafe",
                                "Cafe",
                                "Cafe",
                                "Cafe",
                                "Store",
                                "Park",
                                "Hospital",
                                "Hospital",
                                "Pub",
                                "Pub",
                                "Home",
                                "Home",
                                "Sleep",
                                "Sleep"]

  Child_Schedule_Monday = [ "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "WakeUp",
                            "School",
                            "School",
                            "School",
                            "School",
                            "School",
                            "School",
                            "School",
                            "School",
                            "Park",
                            "Park",
                            "Home",
                            "Home",
                            "Sleep",
                            "Sleep",
                            "Sleep"]

  Officer_Schedule_Monday = [ "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "WakeUp",
                              "PoliceStation",
                              "Cafe",
                              "PoliceStation",
                              "PoliceStation",
                              "PoliceStation",
                              "PoliceStation",
                              "Cafe",
                              "PoliceStation",
                              "PoliceStation",
                              "PoliceStation",
                              "PoliceStation",
                              "School",
                              "School",
                              "School",
                              "Home",
                              "Sleep"]

  Lord_Schedule_Monday = [ "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "WakeUp",
                            "Mansion",
                            "Mansion",
                            "Hospital",
                            "Mansion",
                            "Mansion",
                            "Mansion",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep",
                            "Sleep"]

  Doctor_Schedule_Monday = [ "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "WakeUp",
                              "Cafe",
                              "Hospital",
                              "Hospital",
                              "Hospital",
                              "Hospital",
                              "Cafe",
                              "Hospital",
                              "Hospital",
                              "Hospital",
                              "Hospital",
                              "Hospital",
                              "Hospital",
                              "Store",
                              "Pub",
                              "Home",
                              "Sleep",
                              "Sleep"]

  Barman_Schedule_Monday = [ "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "Sleep",
                              "WakeUp",
                              "Store",
                              "Cafe",
                              "Pub",
                              "Pub",
                              "Pub",
                              "Pub",
                              "Pub",
                              "Pub",
                              "Pub",
                              "Pub",
                              "Pub",
                              "Pub",
                              "Pub",
                              "Home"]

                              
  CHARACTER_LIST = []
  Boy_Schedule = [Postman_Schedule_Monday, Postman_Schedule_Monday]
  Girl_Schedule = [Barista_F_Schedule_Monday, Barista_F_Schedule_Monday]
  
  Lady_Schedule = [Lady_Schedule_Monday]
  Teacher_Schedule = [Teacher_Schedule_Monday]
  Nun_Schedule = [Nun_Schedule_Monday]
  Postman_Schedule = [Postman_Schedule_Monday]
  Innkeeper_Schedule = [Innkeeper_Schedule_Monday]
  HomelessGuy_Schedule = [HomelessGuy_Schedule_Monday]
  Shopkeeper_Schedule = [Shopkeeper_Schedule_Monday]
  Barista_M_Schedule = [Barista_M_Schedule_Monday]
  Barista_F_Schedule = [Barista_F_Schedule_Monday]
  Child_Schedule = [Child_Schedule_Monday]
  Officer_Schedule = [Officer_Schedule_Monday]
  Lord_Schedule = [Lord_Schedule_Monday]
  Doctor_Schedule = [Doctor_Schedule_Monday]
  Barman_Schedule = [Barman_Schedule_Monday]
  
    
  #------------------------------------------------------
  
  def GenerateCharacters():
    CharacterList = []
    #boy = CharacterClass()
    #boy.SetCharacterStats("Boy", 13, "Male")
    #boy.SetSchedule(Boy_Schedule)
    #CharacterList.append(boy)
    #
    #girl = CharacterClass()    
    #girl.SetCharacterStats("Girl", 17, "Female")
    #girl.SetSchedule(Girl_Schedule)
    #CharacterList.append(girl)
    
    CharacterList.append(CharacterClass("Lady", 21, "Female", "Angry", Lady_Schedule))
    CharacterList.append(CharacterClass("Teacher", 21, "Female", "Angry", Teacher_Schedule))
    CharacterList.append(CharacterClass("Nun", 21, "Female", "Angry", Nun_Schedule))
    CharacterList.append(CharacterClass("Postman", 21, "Female", "Angry", Postman_Schedule))
    CharacterList.append(CharacterClass("Innkeeper", 21, "Female", "Angry", Innkeeper_Schedule))
    CharacterList.append(CharacterClass("HomelessGuy", 21, "Female", "Angry", HomelessGuy_Schedule))
    CharacterList.append(CharacterClass("Shopkeeper", 21, "Female", "Angry", Shopkeeper_Schedule))
    CharacterList.append(CharacterClass("Barista_M", 21, "Female", "Angry", Barista_M_Schedule))
    CharacterList.append(CharacterClass("Barista_F", 21, "Female", "Angry", Barista_F_Schedule))
    CharacterList.append(CharacterClass("Child", 21, "Female", "Angry", Child_Schedule))
    CharacterList.append(CharacterClass("Officer", 21, "Female", "Angry", Officer_Schedule))
    CharacterList.append(CharacterClass("Lord", 21, "Female", "Angry", Lord_Schedule))
    CharacterList.append(CharacterClass("Doctor", 21, "Female", "Angry", Doctor_Schedule))
    CharacterList.append(CharacterClass("Barman", 21, "Female", "Angry", Barman_Schedule))
      
    return CharacterList  
    
  def GetCharactersPresent(_location, _day, _time):
    #debug_print(str(_location) + ", " + str(_day) + ", " + str(_time) + " = ")
    charactersPresent = []
    for character in CHARACTER_LIST:
      #debug_print(str(character.Name) + ", " + str(character.Schedule[_day][_time]))
      if character.IsAlive():
        if character.Schedule[_day][_time] == AvailableLocations[_location][0]:
          #debug_print(str(character.Name))          
          charactersPresent.append(character)
        
    return charactersPresent
    
    
  
    
  #------------------------------------------------------
  #------------------------------------------------------
  def IsLocationOpen(_location):
    #debug_print(str(_location))
    currentTime = GetTime()
    
    if _location == 'Cafe':
      if currentTime > 6 and currentTime < 18:
        return False
        
    return True
  #------------------------------------------------------