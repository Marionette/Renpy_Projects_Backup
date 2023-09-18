# Image Calls #########################

init:
    # BG Images #

    image bg black = "#000000"
    image bg white = "#ffffff"
    image blackframe movie = Movie(channel="blackframe", play="images/animations/blackframe.webm", mask="images/animations/blackframe_mask.webm") 

    image frameAnim = Movie(channel="f", play="images/f_real.webm", mask="images/f_mask.webm") 
    image frameNotAnim = "images/frame.png" 
    
    image bg hallway = "images/bg/bg-hallway01.png"
    image bg starroom = "images/bg/bg-starroom.png"
    image bg clockroom = "images/bg/bg-clockroom_base.png"
    image bg flowerroom = "images/bg/bg-flowerroom.png"
    image bg ororo = "images/bg/bg-ororo.png"
    image bg library = "images/bg/bg-library.png"
    image bg hallway01 = "images/bg/bg-hallway01.png"
    image bg hallway02 = "images/bg/bg-hallway02.png"
    image bg nue = "images/bg/bg-nue_base.png"
    image bg nuebase = "images/bg/bg-nue.png"
    image bg deisroom = "images/bg/bg-deisroom.png"
    image bg ramskull = "images/bg/bg-ramskull.png"
    image bg librarymary = "images/bg/bg-librarymary.png"
    image bg clockroomcat = "images/bg/bg-clockroomcat.png"
    
# CHAR Images #

    image mc base = "images/ch/mc_base.png"   
    image mc horns = "images/ch/mc_base_horns.png"
    image mc tail = "images/ch/mc_base_tail.png"    
    image mc wings = "images/ch/mc_wings.png"
    
    image ede base = "images/ch/ede_base.png"
    image mant base = "images/ch/mant_base.png"
    image mogu base = "images/ch/mogu_base.png"
    image morc base = "images/ch/morc_base.png"
    image mr base = "images/ch/mr_base.png"
    image nue base = "images/ch/nue_base.png"
    image oro base = "images/ch/oro_base.png"
    image pon base = "images/ch/pon_base.png"
    image deis base = "images/ch/deis_base.png"
    image sol base = "images/ch/sol_base.png"

init:
    $ mcleft = Position(xpos=0.085, xanchor='left')
    $ mctaileft = Position(xpos=0.15, xanchor='left')
    $ chright = Position(xpos=0.93, xanchor='right')
    $ solright = Position(xpos=0.85, xanchor='right', ypos=0.99)
    $ deisright = Position(xpos=0.85, xanchor='right')
    $ maryright = Position(xpos=0.89, xanchor='right')
    $ centeredtext = Position(xpos=0.5, xanchor='center', ypos=0.82)
    
    
init:
    $ sound_tick = "audio/sfx/clocktick.ogg"
