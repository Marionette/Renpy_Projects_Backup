# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
label start:

    "So? What first?"
    
    menu:
      "Random NPC Generation test":
        jump lbl_RandomGen
      "Navigation test":
        jump lbl_mapStart
      "Music test":
        jump lbl_MusicTest
      "Nothing":
        pass
        
    return
      
label lbl_MusicTest:
    "Setting up random music queue...Well hopefully."
    
    jump lbl_MusicTestChoice
    
label lbl_MusicTestChoice:
    $StartCallbackMusicQueue()
    "Just listen for a while."
    menu: 
      "Ready to go?"
      "Keep Listening.":
        jump lbl_MusicTestChoice
      "Yeah im done.":
        pass
        
    "Time to stop the music."
    $EndCallbackMusicQueue()
    "Hopefully you can't hear anything now."
    
    "Guess thats that then."
    return


label lbl_RandomGen:
    $ _seed = renpy.random.random()
    $ renpy.random.seed(renpy.random.random())
        
    image arcade = "images/bg/arcades.png"
    scene arcade
    
    image randomguy = getRandomCharacter()
    show randomguy
    #  xalign -0.3
    e "Random guy test"
    show randomguy at right
    e "Same Random guy test 1"
    show randomguy at left
    e "Same Random guy test 2"
    show randomguy:
      xalign 0.5
      yalign 0.5
    e "Same Random guy test 3"
    show randomguy:
        linear 0.40 xalign 0.1
        linear 0.40 xalign 1.0
        repeat
    e "Same Random guy test 4"
    hide randomguy
    
    show expression getRandomCharacter() as randomguy2:
      xalign 0.3
    e "Different Random Guy Test"
    
    show expression getRandomCharacter() as randomguy1:
      xalign -0.3
    e "Different Random Guy Test"
    
    show expression getRandomCharacter() as randomguy2:
      xalign 0.3
    e "Different Random Guy Test"
    
    show expression getRandomCharacter() as randomguy3:
      xalign 0.6
    e "Different Random Guy Test"
    
    show expression getRandomCharacter() as randomguy2:
      xalign 0.3
    e "Different Random Guy Test"
    
    show expression getRandomCharacter() as randomguy1:
      xalign -0.3
    e "Different Random Guy Test"
    
    show expression getRandomCharacter() as randomguy3:
      xalign 0.6
    e "Different Random Guy Test"
    
    show expression getRandomCharacter() as randomguy2:
      xalign 0.3
    e "Different Random Guy Test"
    
    show expression getRandomCharacter() as randomguy1:
      xalign -0.3
    e "Different Random Guy Test"
    
    show expression getRandomCharacter() as randomguy3:
      xalign 0.6
    e "Different Random Guy Test"
    
    show expression getRandomCharacter() as randomguy2:
      xalign 0.3
    e "Different Random Guy Test"
    
    show expression getRandomCharacter() as randomguy1:
      xalign -0.3
    e "Different Random Guy Test"
    
    
    show expression getRandomCharacter(1) as randomguy1:
      xalign -0.2
    show expression getRandomCharacter(1) as randomguy2:
      xalign 0.0
    show expression getRandomCharacter(1) as randomguy3:
      xalign 0.2
    show expression getRandomCharacter(1) as randomguy4:
      xalign 0.4
    show expression getRandomCharacter(1) as randomguy5:
      xalign 0.6
    show expression getRandomCharacter(1) as randomguy6:
      xalign 0.8
    show expression getRandomCharacter(1) as randomguy7:
      xalign 1.0
    show expression getRandomCharacter(1) as randomguy8:
      xalign 1.2
    e "Base 1 only!!"
    
    show expression getRandomCharacter(2) as randomguy1:
      xalign -0.2
    show expression getRandomCharacter(2) as randomguy2:
      xalign 0.0
    show expression getRandomCharacter(2) as randomguy3:
      xalign 0.2
    show expression getRandomCharacter(2) as randomguy4:
      xalign 0.4
    show expression getRandomCharacter(2) as randomguy5:
      xalign 0.6
    show expression getRandomCharacter(2) as randomguy6:
      xalign 0.8
    show expression getRandomCharacter(2) as randomguy7:
      xalign 1.0
    show expression getRandomCharacter(2) as randomguy8:
      xalign 1.2
    e "Base 2 only!!"
    
    show expression getRandomCharacter(3) as randomguy1:
      xalign -0.2
    show expression getRandomCharacter(3) as randomguy2:
      xalign 0.0
    show expression getRandomCharacter(3) as randomguy3:
      xalign 0.2
    show expression getRandomCharacter(3) as randomguy4:
      xalign 0.4
    show expression getRandomCharacter(3) as randomguy5:
      xalign 0.6
    show expression getRandomCharacter(3) as randomguy6:
      xalign 0.8
    show expression getRandomCharacter(3) as randomguy7:
      xalign 1.0
    show expression getRandomCharacter(3) as randomguy8:
      xalign 1.2
    e "Base 3 only!!"
    
    show expression getRandomCharacter() as randomguy1:
      xalign -0.2
    show expression getRandomCharacter() as randomguy2:
      xalign 0.0
    show expression getRandomCharacter() as randomguy3:
      xalign 0.2
    show expression getRandomCharacter() as randomguy4:
      xalign 0.4
    show expression getRandomCharacter() as randomguy5:
      xalign 0.6
    show expression getRandomCharacter() as randomguy6:
      xalign 0.8
    show expression getRandomCharacter() as randomguy7:
      xalign 1.0
    show expression getRandomCharacter() as randomguy8:
      xalign 1.2
    e "Any Base!!"
    
    return
