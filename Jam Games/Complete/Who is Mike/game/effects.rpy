#Dissolve effect:

init python:
    def callback_transition(event, interact=True, **kwargs):
        if event == "begin":
            renpy.transition(dissolve, layer="master")
        
    config.all_character_callbacks = [callback_transition] 
    #This line is for testing. It's better to define each characters you want to apply transitions instead of using this line.

init:
    #Defining persistent variables 
    
    #Show intro scene only once
    if persistent.ShowIntro is None:
      $persistent.ShowIntro = False     
      
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.02), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

label splashscreen:
    play sound "sfx/night.ogg"
    scene black 
    with Pause (2)
    show bg fervent with dissolve
    with Pause (3)
    scene black with dissolve
    stop sound fadeout 2.0    
    with Pause (2)
    with dissolve
    if persistent.ShowIntro:
      call intro from _call_intro
      $persistent.ShowIntro = False

    return
    

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

#

# Flash Effect

init:
    $ flash = Fade(0.05, 0, 0.05, color="#fff")
    $ flashblood=  Fade(0.07, 0, 0.07, color="#E00000")
    $ flashbloodslow=  Fade(0.7, 0, 0.7, color="#E00000")
    $ flashbloodfinale=  Fade(2.0, 0, 1.0, color="#E00000")
    $ flashfinale=  Fade(2.0, 0, 2.0, color="#FFF")
    $ flashb =  Fade(0.05, 0, 0.05, color="#000")
    $ flashbl = Fade(0.75, 1.0, 1.0)
    
init:
    $ timer_range = 0
    $ timer_jump = 0

