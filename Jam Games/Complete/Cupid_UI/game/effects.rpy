#BUILD 12

#Text effects
$ narrator=Character(None, ctc="ctc_blink", ctc_position="fixed")

init python:
#Helper functions
    def GetEndingCount():
      count = 0
      
      if persistent.Ending1Unlocked == True:
        count += 1
      if persistent.Ending2Unlocked == True:
        count += 1
      if persistent.Ending3Unlocked == True:
        count += 1
      if persistent.Ending4Unlocked == True:
        count += 1
      if persistent.BonusEndingUnlocked == True:
        count += 1
      return count
      
    def GetCompletionPercentage():
        completionPercent = int(float(float(persistent.currentLinesRead)/float(persistent.totalLines))*100)
        if completionPercent > 100:
            completionPercent = 100
        return completionPercent

init -2:
    # ---------- CTC blinking arrow -------------------
    image ctc_blink:
       "gui/rose.png", #This is your image
       yalign 0.95 xalign 0.93 #Adjust these numbers to fit your own textbox
       linear 0.75 alpha 1.0
       linear 0.75 alpha 0.0
       repeat 

#Positions
init:
    $ left = Position(xpos=0.087, xanchor='left')
    $ nearleft = Position(xpos=0.16, xanchor='left')
    $ nnearleft = Position(xpos=0.2, xanchor='left')    
    $ nnnearleft = Position(xpos=0.24, xanchor='left')  
    $ center = Position(xpos=0.5, xanchor='center')
    $ right = Position(xpos=0.91, xanchor='right')
    $ nnearright = Position(xpos=0.84, xanchor='right')
    $ nearright = Position(xpos=0.80, xanchor='right')
    $ nearrightc = Position(xpos=0.73, xanchor='right')
    $ top = Position(xpos=0.5, xanchor='center', ypos=0.0,
                   yanchor='top')
#######################
#Dissolve effect:

init python:
    def callback_transition(event, interact=True, **kwargs):
        if event == "begin":
            renpy.transition(dissolve, layer="master")
        
    config.all_character_callbacks = [callback_transition] 
    #This line is for testing. It's better to define each characters you want to apply transitions instead of using this line.

#Shake effect
init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    #

#atl
init:
    image pulse:
        "images/extras/colorbg.png"
        linear 3.0 alpha 0.0
        linear 0.5 alpha 1.0
        repeat

init:
    image heat:
        "images/extras/colorbg.png"
        alpha 0.0
        linear 70.0 alpha 1.0
init:
    image cupidwalls:
        "images/bg/fleshroom.png"
        linear 3.0 alpha 0.0
        linear 3.0 alpha 1.0      
        repeat
init:
    image chains:
        "images/extras/chains.png"
        alpha 0.0
        linear 50.0 alpha 1.0       
init:
    image cupidroom:
        "images/bg/guilroomflesh.png"
        alpha 0.0
        linear 15.0 alpha 1.0     

# Flash Effect

init:
    $ flash = Fade(0.05, 0, 0.05, color="#fff")
    $ flashblood=  Fade(0.07, 0, 0.07, color="#E00000")
    $ flashbloodslow=  Fade(0.7, 0, 0.7, color="#E00000")
    $ flashbloodfinale=  Fade(2.0, 0, 1.0, color="#E00000")
    $ flashfinale=  Fade(2.0, 0, 2.0, color="#FFF")
    $ flashb =  Fade(0.05, 0, 0.05, color="#000")
    $ flashbl = Fade(0.75, 1.0, 1.0)
    $ slowdissolve = Fade(0, 0, 2.0)
    $ semidissolve = Fade(0, 0, 1.0)
    $ fastdissolve = Fade(0, 0.07, 0)
    $ alphadissolve = Dissolve(alpha=False)

    $ timer_range = 0
    $ timer_jump = 0
    
init:
    #Defining persistent variables 
    
    if persistent.adult is None:
      $persistent.adult = False
    #Show intro scene only once
    #if persistent.ShowIntro is None:
    #  $persistent.ShowIntro = True    
    if persistent.warning is None:
      $persistent.warning = True    
    if persistent.congrats is None:
      $persistent.congrats = True     
    if persistent.origin is None:    
      $persistent.origin = False 
      
    #Only unlock each chapter after it has been reached
    if persistent.IntroUnlocked is None:
      $persistent.IntoUnlocked = False    
    if persistent.Chapter1Unlocked is None:
      $persistent.Chapter1Unlocked = False
    if persistent.Chapter2Unlocked is None:
      $persistent.Chapter2Unlocked = False
    if persistent.Chapter3Unlocked is None:
      $persistent.Chapter3Unlocked = False
    if persistent.Chapter4Unlocked is None:
      $persistent.Chapter4Unlocked = False
    if persistent.Chapter5Unlocked is None:
      $persistent.Chapter5Unlocked = False
    if persistent.Chapter6Unlocked is None:
      $persistent.Chapter6Unlocked = False
    if persistent.Chapter7Unlocked is None:
      $persistent.Chapter7Unlocked = False
    if persistent.Chapter8Unlocked is None:
      $persistent.Chapter8Unlocked = False
      
    #Only unlock each enddind after it has been reached
    if persistent.Ending1Unlocked is None:
      $persistent.Ending1Unlocked = False
    if persistent.Ending2Unlocked is None:
      $persistent.Ending2Unlocked = False
    if persistent.Ending3Unlocked is None:
      $persistent.Ending3Unlocked = False
    if persistent.Ending4Unlocked is None:
      $persistent.Ending4Unlocked = False
    if persistent.BonusEndingUnlocked is None:
      $persistent.BonusEndingUnlocked = False
    if persistent.EndingUnlocked is None:   
      $persistent.EndingUnlocked = 0
      
    if persistent.totalLines is None: 
      $persistent.totalLines = 53
    if persistent.totalLines < 53: 
      $persistent.totalLines = 53
    if persistent.currentLinesRead is None: 
      $persistent.currentLinesRead = 0

      
label splashscreen:
    if persistent.warning:
        scene bg black
        show warning with Dissolve(2.0, alpha=True)
        $renpy.pause(delay=None)
        hide warning
        show bg warning2
        menu:
            "Mature Filter ON":
                $ persistent.adult = False
            "Mature Filter OFF":
                $ persistent.adult = True
        play sound "sfx/cricket.ogg"
        scene bg black
        show bg fervent with Dissolve(2.0, alpha=True)
        with Pause (2)
        scene bg black with Dissolve(2.0, alpha=True)
        stop sound fadeout 2.0
        $ persistent.warning = False
        
    #if persistent.ShowIntro:
    #    call intro
    #    $persistent.ShowIntro = False

return

