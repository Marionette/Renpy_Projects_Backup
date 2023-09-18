init:
  # Declare characters used by this game. The color argument colorizes the
  # name of the character.

  define e = Character("Eileen")
  define jc = Character("jc")
  
  define b = Character("Bartender")
  define c = Character("Customer")
  
  image bartender_body = "images/bartender_body.png"
  image bartender_shaker = "images/bartender_shaker.png"
  
  transform stopshaking:
    yalign 1.0
    xalign 0.5
    yoffset 150
    rotate 0
    
  transform shakeit:
    yalign 1.0
    xalign 0.5
    yoffset 150
    rotate 0
    shake1()
    shake1()
    shake1()
    shake1()
    shake1()
    shake1()
    shake2()
    shake2()
    shake2()
    shake2()
    shake2()
    shake2()
    shake2()
    repeat
  
  transform shake1():
    easein 0.1 yoffset 170
    easein 0.1 yoffset 120
    #repeat
    
  transform shake2():
    easein 0.1 rotate 20
    easein 0.1 rotate -20
    #repeat