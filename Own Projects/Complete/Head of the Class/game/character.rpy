

##Character
#Name 
#Age
#Species
#Favourite Subject
#Worst Subject
#
#MC
#Stress
#
#Teacher
#Job
#Relationship
#
#Student
#Mood
#
#History
#Science
#Math
#Literacy
#Language
#Geography

  #------------------------------------------------------
init python:
  List_Students = []
  #------------------------------------------------------  
  #Initialize Characters
  
  #Character_Craig = CharacterClass()
  #Character_Craig.SetCharacter("Craig", 13, "Male", "Basilisk", "Geography", "Art")
  #Character_Craig.SetMood(30)
  #Character_Craig.RandomizeAllScores()
  #Character_Hecate = CharacterClass()
  #Character_Hecate.SetCharacter("Hecate", 12, "Witch", "Science", "Math")
  #Character_Hecate.SetMood(40)
  #Character_Hecate.RandomizeAllScores()
  #Character_Sanura = CharacterClass()
  #Character_Sanura.SetCharacter("Sanura", 11, "Sphinx", "Math", "Literacy")
  #Character_Sanura.SetMood(60)
  #Character_Sanura.RandomizeAllScores()
  
  #------------------------------------------------------  
  class CharacterClass:
    #Info
    Name = "???"
    Age = 13
    Gender = "???"
    Species = "???"
    Job = "???"
    Relationship = 0
    
    FavouriteSubject = "???"
    WorstSubject = "???"
    Personality = ""
    Notes = ""
    
    #Mood = 0 - 100 
    Mood = 50
    
    #Subject scores
    History = 0
    Science = 0
    Math = 0
    Literacy = 0
    Language = 0
    Geography = 0
    
    def SetCharacter(self, Name, Age, Gender, Species, Job, FavouriteSubject, WorstSubject, Personality="", Notes=""):
      self.Name = Name
      self.Age = Age
      self.Gender = Gender
      self.Species = Species
      self.Job = Job
      self.FavouriteSubject = FavouriteSubject
      self.WorstSubject = WorstSubject
      self.Personality = Personality
      self.Notes = Notes
      #Relationship starts at 0
      self.Relationship = 0
      
    def SetMood(self, MoodValue):
      self.Mood = MoodValue
      self.SanitizeMood()
      
    def AddMood(self, adjustValue):
      self.Mood = self.Mood + adjustValue
      self.SanitizeMood()
      
    def SanitizeMood(self):
      if self.Mood > 100:
        self.Mood = 100
      if self.Mood < 0:
        self.Mood = 0
      
    def AddRelationship(self, adjustValue):
      self.Relationship = self.Relationship + adjustValue
      self.SanitizeRelationship()
      
    def SanitizeRelationship(self):
      if self.Relationship > 100:
        self.Relationship = 100
      if self.Relationship < 0:
        self.Relationship = 0

    def SetScore(self, Subject, Score):
      if Subject == "History":
        self.History = Score
      if Subject == "Science":
        self.Science = Score
      if Subject == "Math":
        self.Math = Score
      if Subject == "Literacy":
        self.Literacy = Score
      if Subject == "Language":
        self.Language = Score
      if Subject == "Geography":
        self.Geography = Score
      self.SanitizeScores() 

    def GetScore(self, Subject):
      if Subject == "History":
        return self.History
      if Subject == "Science":
        return self.Science 
      if Subject == "Math":
        return self.Math 
      if Subject == "Literacy":
        return self.Literacy 
      if Subject == "Language":
        return self.Language
      if Subject == "Geography":
        return self.Geography 
    
    def GetWeakestSubject(self):
      weakest = "History"
      score = self.History
      if self.Science < score:
        weakest = "Science"
        score = self.Science
      if self.Math < score:
        weakest = "Math"
        score = self.Math
      if self.Literacy < score:
        weakest = "Literacy"
        score = self.Literacy
      if self.Language < score:
        weakest = "Language"
        score = self.Language
      if self.Geography < score:
        weakest = "Geography"
        score = self.Geography
        
      return weakest
    
    def GetStrongestSubject(self):
      strongest = "History"
      score = self.History
      if self.Science > score:
        strongest = "Science"
        score = self.Science
      if self.Math > score:
        strongest = "Math"
        score = self.Math
      if self.Literacy > score:
        strongest = "Literacy"
        score = self.Literacy
      if self.Language > score:
        strongest = "Language"
        score = self.Language
      if self.Geography > score:
        strongest = "Geography"
        score = self.Geography
        
      return strongest
      
    def HasPassedExams(self):   
      score = self.History
      if self.Science < score:
        score = self.Science
      if self.Math < score:
        score = self.Math
      if self.Literacy < score:
        score = self.Literacy
      if self.Language < score:
        score = self.Language
      if self.Geography < score:
        score = self.Geography
        
      #check lowest score is greater than 70 ( C )
      return score >= 70
      
    def GetMultiplier(self, _subject):
      moodMultiplier = std_multiplier
      if feature_unlock_bonus_Mood:
        if self.Mood >= 90:
          moodMultiplier = max_multiplier
        if self.Mood >= 70:
          moodMultiplier = high_multiplier
        #if self.Mood < 30:
        #  moodMultiplier = low_multiplier
        if self.Mood == 0:
          moodMultiplier = min_multiplier
        
        #debug_print("ApplyMoodMultiplier: x" +str(moodMultiplier)+ " - " + str(_subject))
          
      if feature_unlock_penalty_backToBack:
        btbMultiplier = 1
        if ClassTaughtSince(_subject, btb_length, includeToday=False):
          btbMultiplier = btb_multiplier
          debug_print("ApplyBackToBackPenalty: " + str(_subject))
      
      return moodMultiplier * btb_multiplier
      
    
    def AddScore(self, Subject, Score, ApplyMultipliers=True):
      Score = int(Score * self.GetMultiplier(Subject))
      if Subject == "All":
        self.History = self.History + Score
        self.Science = self.Science + Score
        self.Math = self.Math + Score
        self.Literacy = self.Literacy + Score
        self.Language = self.Language + Score
        self.Geography = self.Geography + Score      
      if Subject == "History":
        self.History = self.History + Score
      if Subject == "Science":
        self.Science = self.Science + Score
      if Subject == "Math":
        self.Math = self.Math + Score
      if Subject == "Literacy":
        self.Literacy = self.Literacy + Score
      if Subject == "Language":
        self.Language = self.Language + Score
      if Subject == "Geography":
        self.Geography = self.Geography + Score
      if Subject == "PE/Literacy/Geography":
        self.Literacy = self.Geography + Score
        self.Geography = self.Geography + Score
      self.SanitizeScores()  
        
    def ApplyDegredation(self):    
      List_taught_subjects = ["History", "Science", "Math", "Literacy", "Language", "Geography",]  
      if feature_unlock_penalty_ScoreDegradation:
        #only apply if teaching after a week
        if current_day > 5:
          for subject in List_taught_subjects:
            if not ClassTaughtSince(subject, degradation_length):
              self.AddScore(subject, degradation_pointsLost, ApplyMultipliers=False)
              debug_print("ApplyDegredation: " + str(subject))
            
    def SanitizeScores(self):
      if self.History > 100:
        self.History = 100
      if self.Science > 100:
        self.Science = 100
      if self.Math > 100:
        self.Math = 100
      if self.Literacy > 100:
        self.Literacy = 100
      if self.Language > 100:
        self.Language = 100
      if self.Geography > 100:
        self.Geography = 100
        
    def RandomizeAllScores(self, Min, Max):
      self.SetScore("History", renpy.random.randint(Min,Max))
      self.SetScore("Science", renpy.random.randint(Min,Max))
      self.SetScore("Math", renpy.random.randint(Min,Max))
      self.SetScore("Literacy", renpy.random.randint(Min,Max))
      self.SetScore("Language", renpy.random.randint(Min,Max))
      self.SetScore("Geography", renpy.random.randint(Min,Max))
      
      #swap best to match favourites
      #Adjust for favorite
      if not self.FavouriteSubject in ["Art", "Music", "PE"]:
      #  strongest = self.GetScore(self.GetStrongestSubject())
      #  oldScore = self.GetScore(self.FavouriteSubject)
      #  strsub = self.GetStrongestSubject()
      #  self.SetScore(self.FavouriteSubject, strongest)
      #  self.SetScore(strsub, oldScore)
        self.AddScore(self.FavouriteSubject, 10)
      #Adjust for worst
      if not self.WorstSubject in ["Art", "Music", "PE"]:
        self.AddScore(self.WorstSubject, -10)