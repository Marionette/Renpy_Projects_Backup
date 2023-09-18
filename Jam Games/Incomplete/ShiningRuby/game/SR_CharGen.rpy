
  #------------------------------------------------------
init python:
  #------------------------------------------------------
  def getRandomCharacter(base=-1):  
    character = CharacterClass()
    character.RandomizeAppearance(base)
      
    return get_char(character.Base, character.Bottom, character.Top, character.Brows, character.Eyes, character.Hair, character.Mouth, character.Nose, character.Face)
    
  #------------------------------------------------------
  def get_char(base, bottom, top, brows, eyes, hair, mouth, nose, face): 
      if (base == 2):
        compositeImage = LiveComposite(
        (800, 1000),
        (0, 0), "images/SpriteGen/base%d/base%d.png" %(base, base),
        (0, 0), "images/SpriteGen/base%d/bottoms/bottom%d.png" %(base, bottom),
        (0, 0), "images/SpriteGen/base%d/hair/hair%d.png" %(base, hair),
        (0, 0), "images/SpriteGen/base%d/shirt/shirt%d.png" %(base, top),
        (0, 0), "images/SpriteGen/base%d/faces/face%d.png" %(base, face))      
      else:
        compositeImage = LiveComposite(
        (800, 1000),
        (0, 0), "images/SpriteGen/base%d/base%d.png" %(base, base),
        (0, 0), "images/SpriteGen/base%d/bottoms/bottom%d.png" %(base, bottom),
        (0, 0), "images/SpriteGen/base%d/hair/hair%d.png" %(base, hair),
        (0, 0), "images/SpriteGen/base%d/tops/top%d.png" %(base, top),
        (0, 0), "images/SpriteGen/base%d/brows/brow%d.png" %(base, brows),
        (0, 0), "images/SpriteGen/base%d/eyes/eyes%d.png" %(base, eyes),
        (0, 0), "images/SpriteGen/base%d/mouth/mouth%d.png" %(base, mouth),
        (0, 0), "images/SpriteGen/base%d/nose/nose%d.png" %(base, nose) )
      
      return compositeImage
  
  #------------------------------------------------------  
  class CharacterClass:
    #stats
    Name = "???"
    
    Mood = "???"
    
    #appearance
    Base = 1
    
    Bottom = 1
    Top = 1
    
    Brows = 1
    Eyes = 1
    Hair = 1
    Mouth = 1
    Nose = 1
    
    Face = 1
    
    def RandomizeAppearance(self, base=-1):     
      if base == -1:
        self.Base = renpy.random.randint(1,3)
      else:
        self.Base = base
      
      self.Bottom = renpy.random.randint(1,4)
      self.Top = renpy.random.randint(1,4)
      
      self.Brows = renpy.random.randint(1,4)
      self.Eyes = renpy.random.randint(1,4)
      self.Hair = renpy.random.randint(1,4)
      self.Mouth = renpy.random.randint(1,4)
      self.Nose = renpy.random.randint(1,4)
      
      if self.Base == 2:
        self.Bottom = renpy.random.randint(1,2)
        self.Top = renpy.random.randint(1,2)        
        self.Face = renpy.random.randint(1,3)
        self.Hair = renpy.random.randint(1,2)
        
  #------------------------------------------------------