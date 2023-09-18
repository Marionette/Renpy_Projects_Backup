
#All Characters
    #type - Type of character Common/Noble/Old etc
    #Funds - Money available - cant spend more than this
    #likes - Increases mood when in stock
    #dislikes - decreases mood when in stock
    #mood? - Changes the amount over the base price they are willing to pay
    
#Unique only
    #relationship? - Gets better items in their locations / Increases base mood / extra benefits at high ranks?
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
  #character type
    
  #Type           [Typename, Gender,   Funds, Likes,     Dislikes ] 
  type_common_M = ["Common", "Male",   500,   "Tools",   "Nothing"]
  type_common_F = ["Common", "Female", 500,   "Flowers", "Nothing"]
  type_old_M    = ["Old",    "Male",   500,   "Food",    "Weapons"]
  type_old_F    = ["Old",    "Female", 500,   "Food",    "Weapons"]
  type_child_M  = ["Child",  "Male",   200,   "Candy",   "Vegetables"]
  type_child_F  = ["Child",  "Female", 200,   "Candy",   "Vegetables"]
  type_bum_M    = ["Bum",    "Male",   0,     "Nothing",        "Nothing"]
  
  
  List_CharacterTypes = [type_common_M ,
                         type_common_F ,
                         type_old_M    ,
                         type_old_F    ,
                         type_child_M  ,
                         type_child_F  ,
                         type_bum_M    ]
      
  #------------------------------------------------------
  #def GetMoodFromIndex(_mood, _eyeCol):
  #  mood = "neutral_e%d" %_eyeCol
  #  
  #  if(_mood == 0):
  #    mood = "displease_e%d" %_eyeCol
  #  if(_mood == 2):
  #    mood = "glee_e%d" %_eyeCol
  #  if(_mood == 3):
  #    mood = "happy"
  #  if(_mood == 4):
  #    mood = "neutral_e%d" %_eyeCol
  #
  #    
  #  return mood

  #------------------------------------------------------   
  
  def get_char(_type):   
    
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
  def GetRandomName(_type, _gender):
    forname = "Dude"
    if _gender == "Female":
      forname = "Dudette"
    #forname = renpy.random.choice(List_Forenames_M)
    #if _gender == "Female":
    #  forname = renpy.random.choice(List_Forenames_F)
    #  
    #return [forname,(renpy.random.choice(List_Surnames))]
    #return forname +" "+(renpy.random.choice(List_Surnames))
    return forname
    
  #------------------------------------------------------      
  def GetLikesAndDislikes(_type):
  
    type = type_common_M
    like = type[3]
    dislike = type[4]
      
    return [like, dislike]
    
    
  #------------------------------------------------------
  class CharacterClass:
    #stats
    Name = "???"
    #Age = 21
    Gender = "Male"
    #Birthday = [1,1]
    
    Mood = "Neutral"
    
    Type = "???"
    Funds = 1000
    
    Likes = "???"
    Dislikes = "???"
    
    Relationship = 1
    Happiness = 50
    
    #appearance
    IsUnique = 0
    UniqueAppearance = ""
    
    #def __init__(self):
    
    def Appearance(self):
      if self.IsUnique:
        return self.UniqueAppearance
      else:        
        #Get based on Type
        return get_char(self.Gender, self.Uniform, self.Hair, self.HairColour, self.EyeColour, self.Mood)
        #return self.UniqueAppearance
    
    def RandomizeType(self):
      type = renpy.random.choice(List_CharacterTypes)
      self.Type = type[0]
      self.Gender = type[1]
      self.Funds = type[2]
      self.Likes = type[3]
      self.Dislikes = type[4]
      
      self.Name = GetRandomName(self.Type, self.Gender)

  def GenerateCharacters(number):
    CharacterList = []
    for i in range(0,number):
      character = CharacterClass()
      character.RandomizeType()
      #character.RandomizeAppearance()
      
      CharacterList.append(character)
      
    return CharacterList     