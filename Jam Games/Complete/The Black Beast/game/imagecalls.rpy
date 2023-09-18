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
    image bg clockroom_cg_base = "images/bg/bg-clockroom_cg_base.png"
    image bg clockroom_cg_moved = "images/bg/bg-clockroom_cg_moved.png"
    image bg clockroom_moved = "images/bg/bg-clockroom_base_moved.png"
    image bg clockroomcat_moved = "images/bg/bg-clockroomcat_moved.png"
     
    
    image bg flowerroom = "images/bg/bg-flowerroom.png"
    image bg ororo = "images/bg/bg-ororo.png"
    image bg library = "images/bg/bg-library.png"
    image bg hallway01 = "images/map_hallway01/bg-hallway01.png"
    image bg hallway02 = "images/map_hallway02/bg-hallway02.png"
    
    image bg nue = "images/bg/bg-nue_base.png"
    image bg nuebase = "images/bg/bg-nue.png"
    image bg nuebasemask = "images/bg/bg-nue_base_withmask.png"
    image bg nuemask = "images/bg/bg-nue_withmask.png"
    
    image bg deisroom = "images/bg/bg-deisroom.png"
    image bg librarymary = "images/bg/bg-librarymary.png"
    image bg clockroomcat = "images/bg/bg-clockroomcat.png"
    image bg flowerroom_mask = "images/bg/bg-flowerroom_mask.png"
    
    # CG
    image bg beast = "images/cg/beast.png"
    image bg door = "images/cg/door.png"    
    image bg ramskull = "images/bg/bg-ramskull.png"
    image bg ramskullnohorn = "images/bg/bg-ramskull_nohorn.png"
    image bg boy = "images/cg/boy.png"
    image bg boyhorns = "images/cg/boyhorns.png"
    image bg boytail = "images/cg/boytail.png"
    image bg boyhornstail = "images/cg/boyhornstail.png"

init:
    $ mcleft = Position(xpos=0.085, xanchor='left')
    $ mctaileft = Position(xpos=0.15, xanchor='left')
    $ chright = Position(xpos=0.93, xanchor='right')
    $ chfarright = Position(xpos=0.95, xanchor='right')

    $ solright = Position(xpos=0.85, xanchor='right', ypos=0.99)
    $ deisright = Position(xpos=0.85, xanchor='right')
    $ maryright = Position(xpos=0.89, xanchor='right')
    $ outofscreen = Position(xpos=1.5, xanchor='right')
    $ centeredtext = Position(xpos=0.5, xanchor='center', ypos=0.82)
    
    $ move = MoveTransition(1.0)
    $ movefast = MoveTransition(0.5)
    $ slowdissolve = Fade(0, 0, 2.0)
    $ flash = Fade(0.05, 0, 0.05, color="#fff")
    
init:
    $ sound_tick = "audio/sfx/clocktick.ogg"
    $ itemtwinkle = "audio/sfx/twinkle.ogg"
    $ doorslam = "audio/sfx/doorslam.ogg"
    $ knock = "audio/sfx/knock.ogg"
    $ stargiggle = "audio/sfx/starsgiggling.ogg"
    $ horndrop = "audio/sfx/horndrop.ogg"
    $ slash = "audio/sfx/knifeslash.ogg"
    $ nvlmusic = "audio/music/peryton.ogg"
    $ memory = "audio/music/memory.ogg"
    $ dooropen = "audio/sfx/dooropen.ogg"
    $ darkmagic = "audio/sfx/darkmagic.ogg"

# ATL

    image clock animated:
        "bg/bg-clockroom_cg_base.png"
        pause 3.0
        "bg/bg-clockroom_cg_moved.png" with Dissolve(0.5, alpha=True)
        pause 3.0

