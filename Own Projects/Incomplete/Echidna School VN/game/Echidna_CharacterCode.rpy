
  #------------------------------------------------------
init python:

  #######################################################
  def debug_print(_msg):
    return # comment out to print debug messages
    with open("F:\[Projects]\RenpyGames\Echidna School VN\game\log.txt", "a") as myfile:
      myfile.write(_msg)
      myfile.write("\n")
  #######################################################
    
  #------------------------------------------------------  
  List_MF_ChildBodyPartsCount = [[1, 1], #Uniform [M, F]
                                 [3, 3], #EyeCol [M, F]
                                 [3, 6], #Hair [M, F]
                                 [4, 3], #HairCol [M, F]
                                 [4, 4], #Mood [M, F]
                                 ]
                                 
  def GetPartCount(_part, _gender):
    
    gender = 1
    if (_gender == "Male"):
        gender = 0
        
    return List_MF_ChildBodyPartsCount[GetBodyPartIndex(_part)][gender]
      
  def GetBodyPartIndex(_part):
    part = 0 #Uniform
    if (_part == "EyeColour"):
      part = 1
    if (_part == "Hair"):
      part = 2
    if (_part == "HairColour"):
      part = 3
    if (_part == "Mood"):
      part = 4
      
    return part
      
  #------------------------------------------------------
  def GetMoodFromIndex(_mood, _eyeCol):
    mood = "neutral_e%d" %_eyeCol
    
    if(_mood == 0):
      mood = "displease_e%d" %_eyeCol
    if(_mood == 2):
      mood = "glee_e%d" %_eyeCol
    if(_mood == 3):
      mood = "happy"
    if(_mood == 4):
      mood = "neutral_e%d" %_eyeCol

      
    return mood

  #------------------------------------------------------        
  def get_char(gender, uniform, hair, hairCol, eyeCol, mood): 
      debug_print("Get_char - " + str(gender) + ", " + str(hair) + ", " + str(hairCol) + ", " + str(eyeCol) + ", " + str(mood))
      
      if (gender == "Male"):
        _gen = 'M'
        _uniform = uniform
        _hair = hair
        _hairCol = hairCol
        _eyeCol = eyeCol
        _exp = mood
      else: 
        _gen = 'F'
        _uniform = uniform
        _hair = hair
        _hairCol = hairCol
        _eyeCol = eyeCol
        _exp = mood
        
      debug_print(" = = " + str(_gen) + ", " + str(_uniform) + ", " + str(_hair) + ", " + str(_hairCol) + ", " + str(_eyeCol) + ", " + str(_exp))
      
      ratio = 0.5
      #(930*ratio, 1623*ratio),
      #return LiveComposite(
      #(930, 1623),
      #(0, 0), im.Scale("img/sprites/Composite/Student/child_base.png", 930*ratio, 1623*ratio),
      #(0, 0), im.Scale("img/sprites/Composite/Student/child_uniform_%s.png" %_gen, 930*ratio, 1623*ratio),
      #(0, 0), im.Scale("img/sprites/Composite/Student/child_expression_%s.png" %GetMoodFromIndex(_exp, _eyeCol), 930*ratio, 1623*ratio),
      #(0, 0), im.Scale("img/sprites/Composite/Student/child_hair_%s_t%d_c%d.png" %(_gen, _hair, _hairCol), 930*ratio, 1623*ratio))
              
      return im.Scale(im.Composite(
      (930, 1623),
      (0, 0), "img/sprites/Composite/Student/child_base.png",
      (0, 0), "img/sprites/Composite/Student/child_uniform_%s.png" %_gen,
      (0, 0), "img/sprites/Composite/Student/child_expression_%s.png" %GetMoodFromIndex(_exp, _eyeCol),
      (0, 0), "img/sprites/Composite/Student/child_hair_%s_t%d_c%d.png" %(_gen, _hair, _hairCol)), 930*ratio, 1623*ratio)
        
      
  #------------------------------------------------------
  def GetLikesImage(string): 
    Likes = "img/ui/symbol/Likes_Unknown.png"
    for like in DiscoveredLikes:
      if (like == string):
        Likes = "img/ui/symbol/Likes_" + string + ".png"
    return Likes
      

  #------------------------------------------------------
  def GetRandomName(_gender):
    forname = renpy.random.choice(List_Forenames_M)
    if _gender == "Female":
      forname = renpy.random.choice(List_Forenames_F)
      
    return [forname,(renpy.random.choice(List_Surnames))]
    #return forname +" "+(renpy.random.choice(List_Surnames))
    
  #------------------------------------------------------
  def GetRandomPersonality():
    return renpy.random.choice(List_Personalities)
    
  #------------------------------------------------------
  def GetRandomTraitPair():
    Trait1 = renpy.random.choice(List_Traits)
    Trait2 = renpy.random.choice(List_Traits)
    
    while (Trait2 == Trait1) :
      Trait2 = renpy.random.choice(List_Traits)
      
    return [Trait1, Trait2]
  
  #------------------------------------------------------
  def GetRandomPreferences():
    Pref1 = renpy.random.choice(List_Preferences)
    Pref2 = renpy.random.choice(List_Preferences)
    Pref3 = renpy.random.choice(List_Preferences)
    
    while (Pref2 == Pref1) :
      Pref2 = renpy.random.choice(List_Preferences)
      
    while (Pref3 == Pref1 or Pref3 == Pref2) :
      Pref3 = renpy.random.choice(List_Preferences)
      
    return [Pref1, Pref2, Pref3]
      
  def GetRandomLikesAndDislikes():
    #Likes
    Pref1 = renpy.random.choice(List_Preferences)
    Pref2 = renpy.random.choice(List_Preferences)
    Pref3 = renpy.random.choice(List_Preferences)
    #Dislikes
    Pref4 = renpy.random.choice(List_Preferences)
    Pref5 = renpy.random.choice(List_Preferences)
    Pref6 = renpy.random.choice(List_Preferences)
    
    while (Pref2 == Pref1) :
      Pref2 = renpy.random.choice(List_Preferences)
      
    while (Pref3 == Pref1 or Pref3 == Pref2) :
      Pref3 = renpy.random.choice(List_Preferences)
      
    while (Pref4 == Pref1 or Pref4 == Pref2 or Pref4 == Pref3) :
      Pref4 = renpy.random.choice(List_Preferences)
      
    while (Pref5 == Pref1 or Pref5 == Pref2 or Pref5 == Pref3 or Pref5 == Pref4) :
      Pref5 = renpy.random.choice(List_Preferences)
      
    while (Pref6 == Pref1 or Pref6 == Pref2 or Pref6 == Pref3 or Pref6 == Pref4 or Pref6 == Pref5) :
      Pref6 = renpy.random.choice(List_Preferences)
      
    return [[Pref1, Pref2, Pref3],[Pref4, Pref5, Pref6]]
    
  #------------------------------------------------------
  class CharacterClass:
    #stats
    Name = "???"
    Age = 13
    Gender = "Male"
    Birthday = [1,1]
    
    Mood = "Neutral"
    
    Personality = "???"
    Traits = ["???", "???"]
    
    Likes = ["???","???","???"]
    Dislikes = ["???","???","???"]
    
    PersonalityKnown = 0
    TraitsKnown = [0,0]
    LikesKnown = [0,0,0]
    DislikesKnown = [0,0,0]
    
    IsAStudent = True
    Relationship = 1
    Happiness = 50
    
    English = 0
    Science = 0
    Maths = 0
    Art = 0
    Music = 0
    PE = 0
    
    #appearance
    Uniform = 1
    Hair = 1
    HairColour = 1
    EyeColour = 1
    IsUnique = 0
    UniqueAppearance = ""
    
    #def __init__(self):
    
    def RandomizeStats(self):
      self.Gender = renpy.random.choice(["Male", "Female"])
      name = GetRandomName(self.Gender)
      self.Forename = name[0]
      self.Surname = name[1]
      self.Name =  name[0] + " " + name[1]
      self.Age = renpy.random.randint(6,12)
      
      #Get random birthday
      month = renpy.random.randint(1,12)
      day = renpy.random.randint(1,MonthsOfTheYear[month-1][2])
      self.Birthday = [day, MonthsOfTheYear[month-1][0]]
      
      self.Personality = GetRandomPersonality()
      self.Traits = GetRandomTraitPair()
      
      self.Relationship = renpy.random.randint(1,99)
      self.Happiness =  renpy.random.randint(1,99)
      
      self.English =  renpy.random.randint(1,99)
      self.Science =  renpy.random.randint(1,99)
      self.Maths =  renpy.random.randint(1,99)
      self.Art =  renpy.random.randint(1,99)
      self.Music =  renpy.random.randint(1,99)
      self.PE =  renpy.random.randint(1,99)
      #self.Likes = GetRandomPreferences()
      #self.Dislikes = GetRandomPreferences()
      [self.Likes, self.Dislikes] = GetRandomLikesAndDislikes()
    
    def RandomizeAppearance(self):
      self.IsUnique = False
      self.Uniform = renpy.random.randint(1, GetPartCount("Uniform", self.Gender))
      self.Hair = renpy.random.randint(1, GetPartCount("Hair", self.Gender))
      self.HairColour = renpy.random.randint(1, GetPartCount("HairColour", self.Gender))
      self.EyeColour = renpy.random.randint(1, GetPartCount("EyeColour", self.Gender))
      self.Mood = renpy.random.randint(0, GetPartCount("Mood", self.Gender))   

      
    def AddScoresToSelf(self, other):
      self.Relationship = other.Relationship + self.Relationship
      self.Happiness    = other.Happiness    + self.Happiness   
      self.English      = other.English      + self.English     
      self.Science      = other.Science      + self.Science     
      self.Maths        = other.Maths        + self.Maths       
      self.Art          = other.Art          + self.Art         
      self.Music        = other.Music        + self.Music       
      self.PE           = other.PE           + self.PE       

    def DivideScores(self, division):
      self.Relationship = self.Relationship / division
      self.Happiness    = self.Happiness    / division
      self.English      = self.English      / division
      self.Science      = self.Science      / division
      self.Maths        = self.Maths        / division
      self.Art          = self.Art          / division
      self.Music        = self.Music        / division
      self.PE           = self.PE           / division
      
    def GetKnownPersonality(self):
      personality = "???"
      if self.PersonalityKnown == 1:
        personality = self.Personality
        
      if self.Personality in DiscoveredPersonalities:
        personality = self.Personality
        
      return personality
      
    def GetKnownTraits(self, pos):
      trait = "???"
      if self.TraitKnown[pos] == 1:
        trait = self.Traits[pos]
        
      if self.Traits[pos] in DiscoveredPersonalities:
        trait = self.Traits[pos]
        
      return trait
      
    def GetKnownLikes(self, pos):
      like = "???"
      if self.LikesKnown[pos] == 1:
        like = self.Likes[pos]
        
      if self.Likes[pos] in DiscoveredLikes:
        like = self.Likes
        
      return like
      
    def GetKnownDislikes(self, pos):
      dislike = "???"
      if self.DislikesKnown[pos] == 1:
        dislike = self.Dislikes[pos]
        
      if self.Dislikes[pos] in DiscoveredLikes:
        dislike = self.Dislikes[pos]
        
      return dislike
      
    #functions to allow character class to be used for non random characters
    def SetUniqueCharacter(self, Name, Age, Gender, Birthday, Personality, Traits, Likes, Dislikes, UniqueAppearance):
      self.Name = Name
      self.Age = Age
      self.Gender = Gender
      self.Birthday = [Birthday[0], MonthsOfTheYear[Birthday[1]-1][0]] 
      self.Personality = Personality
      self.Traits = Traits
      self.Likes = Likes
      self.Dislikes = Dislikes
      self.UniqueAppearance = UniqueAppearance  
      self.IsUnique = True  
    
    def SetCharacterStats(self, Relationship, Happiness, English, Science, Maths, Art, Music, PE):
      self.Relationship = Relationship
      self.Happiness = Happiness
      self.English = English
      self.Science = Science
      self.Maths = Maths
      self.Art = Art
      self.Music = Music
      self.PE = PE
    
    def SetSpecificAge(self, age, variance = 0):
      self.Age = renpy.random.randint(age - variance, age + variance)
    
    def SetSpecificAppearance(self, appearance):
      self.UniqueAppearance = appearance
      self.IsUnique = True
    
    def Appearance(self):
      if self.IsUnique:
        return self.UniqueAppearance
      else:        
        return get_char(self.Gender, self.Uniform, self.Hair, self.HairColour, self.EyeColour, self.Mood)
    
    def GetSubjectMoodModifier(self, _subject):
      like = 0
      dislike = 0
      for _subject in self.Likes:
        like += 1
        
      for _subject in self.Dislikes:
        dislike += 1
        
      #Apply extra modifiers based on traits etc here        
      return like - dislike
    
    def GetSubjectLearningModifier(self, _subject):
      value = 0
      #Apply extra modifiers based on traits etc here        
      return value
      
    def UpdateSubjectScore(self, _subject, _modifier=1):
    
      #self.Relationship = Relationship
      
      value = 1 * _modifier + self.GetSubjectLearningModifier(_subject)
      HappinessValue = 1 + self.GetSubjectMoodModifier(_subject)
      
      if _subject == "English":
        self.English += value
      
      if _subject == "Science":
        self.Science += value
      
      if _subject == "Maths":
        self.Maths += value
      
      if _subject == "Art":
        self.Art += value
      
      if _subject == "Music":
        self.Music += value
      
      if _subject == "PE":
        self.PE += value
    
      self.Happiness -= HappinessValue
      
      self.BoundsClampScores()
        
      return
      
      
    def BoundsClampScores(self):
    
      if self.Relationship < 0:
        self.Relationship = 0
      if self.Relationship > 100:
        self.Relationship = 100
        
      if self.Happiness < 0:
        self.Happiness = 0
      if self.Happiness > 100:
        self.Happiness = 100
        
    
      if self.English < 0:
        self.English = 0
      if self.English > 100:
        self.English = 100
    
      if self.Science < 0:
        self.Science = 0
      if self.Science > 100:
        self.Science = 100
    
      if self.Maths < 0:
        self.Maths = 0
      if self.Maths > 100:
        self.Maths = 100
    
      if self.Art < 0:
        self.Art = 0
      if self.Art > 100:
        self.Art = 100
    
      if self.Music < 0:
        self.Music = 0
      if self.Music > 100:
        self.Music = 100
    
      if self.PE < 0:
        self.PE = 0
      if self.PE > 100:
        self.PE = 100
        
      return
      
    def GetPronoun(self, _pronoun):
      if self.Gender == "Male":
        return _pronoun
      else:
        if _pronoun == "he":
          return "she"
        if _pronoun == "He":
          return "She"
        if _pronoun == "Him":
          return "Her"
        if _pronoun == "him":
          return "her"
        if _pronoun == "His":
          return "Her"
        if _pronoun == "his":
          return "her"
      
      
  #------------------------------------------------------
  def GenerateCharacters(number):
    CharacterList = []
    for i in range(0,number):
      character = CharacterClass()
      character.RandomizeStats()
      character.RandomizeAppearance()
      
      CharacterList.append(character)
      
    return CharacterList  
  
  def GetClassAverage():
    average = CharacterClass()
    average.Name = "Class Average"
    
    for child in CHILD_LIST:
      average.AddScoresToSelf(child)
    
    average.DivideScores(ChildCount)
    
    return average
  #------------------------------------------------------
    
  #------------------------------------------------------
  ## Game Code 
  
  def ApplyTeaching(_subject):
    for child in CHILD_LIST:
      child.UpdateSubjectScore(_subject)
    
    return
  #------------------------------------------------------
  
  def SelectRandomChild():
      chosen = renpy.random.randint(1,ChildCount)
      
      return CHILD_LIST[chosen-1]
  
  def SelectChildByName(_name):
    for i in range(0, ChildCount):
      if "{font=assets/PermanentMarker.ttf}{size=28}" + CHILD_LIST[i].Name + "{/font}{/size}" == _name:
        return i
      if CHILD_LIST[i].Name == _name:
        return i
        
  def SelectCharacterByName(_name):
    debug_print("SelectCharacterByName - " + str(_name)  )
    for i in range(0, AdultCount):
      if "{font=assets/PermanentMarker.ttf}{size=28}" + ADULT_LIST[i].Name + "{/font}{/size}" == _name:
        return "%d"%int(i)
      if ADULT_LIST[i].Name == _name:
        return "%d"%int(i)
        
    for j in range(0, ChildCount):
      if "{font=assets/PermanentMarker.ttf}{size=28}" + CHILD_LIST[j].Name + "{/font}{/size}" == _name:
        return "%d"%int(j + AdultCount)
      if CHILD_LIST[j].Name == _name:
        return "%d"%int(j + AdultCount)
    
    return "-1"
  #------------------------------------------------------
  