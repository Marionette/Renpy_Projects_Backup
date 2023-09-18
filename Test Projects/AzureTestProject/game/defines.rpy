init python:
    register_3d_layer('b', 'm', 'f')
    
    
init:
  image sunrays movie = Movie(channel="sunrays", play="img/sunrays/out.webm", mask="img/sunrays/mask.webm")
  # Declare backgrounds used by this game.
  image bg white = Solid("#FFFFFF")
  image bg black = Solid("#000000")

  # Declare characters used by this game.
  define e = Character('Eileen', color="#c8ffc8")
  define e2 = Character('Eileen2', color="#c8ffc8")
  define s = Character('Skull', color="#c8ffc8")
  define l = Character('Lucy', color="#c8ffc8")

  
  image Eileen = "img/sprite/girl1/frame_000.gif"
  image kid = "img/sprite/Other/kid.png"
  image teach = "img/sprite/Other/teach.png"
  
  image Eileen emote =      Animation("img/sprite/girl1/frame_000.gif", 0.03,
                                      "img/sprite/girl1/frame_001.gif", 0.03,
                                      "img/sprite/girl1/frame_002.gif", 0.03,
                                      "img/sprite/girl1/frame_003.gif", 0.03,
                                      "img/sprite/girl1/frame_004.gif", 0.03,
                                      "img/sprite/girl1/frame_005.gif", 0.03,
                                      "img/sprite/girl1/frame_006.gif", 0.03,
                                      "img/sprite/girl1/frame_007.gif", 0.03,
                                      "img/sprite/girl1/frame_008.gif", 0.03,
                                      "img/sprite/girl1/frame_009.gif", 0.03,
                                      "img/sprite/girl1/frame_010.gif", 0.03,
                                      "img/sprite/girl1/frame_011.gif", 0.03,
                                      "img/sprite/girl1/frame_012.gif", 0.03,
                                      "img/sprite/girl1/frame_013.gif", 0.03,
                                      "img/sprite/girl1/frame_014.gif", 0.03,
                                      "img/sprite/girl1/frame_015.gif", 0.03,
                                      "img/sprite/girl1/frame_016.gif", 0.03,
                                      "img/sprite/girl1/frame_017.gif", 0.03,
                                      "img/sprite/girl1/frame_018.gif", 0.03,
                                      "img/sprite/girl1/frame_019.gif", 0.03,
                                      "img/sprite/girl1/frame_020.gif", 0.03,
                                      "img/sprite/girl1/frame_021.gif", 0.03,
                                      "img/sprite/girl1/frame_022.gif", 0.03,
                                      "img/sprite/girl1/frame_023.gif", 0.03,
                                      "img/sprite/girl1/frame_024.gif", 0.03,
                                      "img/sprite/girl1/frame_025.gif", 0.03,
                                      "img/sprite/girl1/frame_026.gif", 0.03,
                                      "img/sprite/girl1/frame_027.gif", 0.03,
                                      "img/sprite/girl1/frame_028.gif", 0.03,
                                      "img/sprite/girl1/frame_029.gif", 0.03,
                                      "img/sprite/girl1/frame_030.gif", 0.03,
                                      "img/sprite/girl1/frame_031.gif", 0.03,
                                      "img/sprite/girl1/frame_032.gif", 0.03,
                                      "img/sprite/girl1/frame_033.gif", 0.03,
                                      "img/sprite/girl1/frame_034.gif", 0.03,
                                      "img/sprite/girl1/frame_035.gif", 0.03,
                                      "img/sprite/girl1/frame_036.gif", 0.03,
                                      "img/sprite/girl1/frame_037.gif", 0.03,
                                      "img/sprite/girl1/frame_038.gif", 0.03,
                                      "img/sprite/girl1/frame_039.gif", 0.03,
                                      "img/sprite/girl1/frame_040.gif", 0.03,
                                      "img/sprite/girl1/frame_041.gif", 0.03,
                                      "img/sprite/girl1/frame_042.gif", 0.03,
                                      "img/sprite/girl1/frame_043.gif", 0.03,
                                      "img/sprite/girl1/frame_044.gif", 3)
                                      
                                      

  
  image bg cabin = "img/bg/cabin/frame_000.gif"
  image bg cabin animated = Animation("img/bg/cabin/frame_000.gif", 0.04,
                                      "img/bg/cabin/frame_001.gif", 0.04,
                                      "img/bg/cabin/frame_002.gif", 0.04,
                                      "img/bg/cabin/frame_003.gif", 0.04,
                                      "img/bg/cabin/frame_004.gif", 0.04,
                                      "img/bg/cabin/frame_005.gif", 0.04,
                                      "img/bg/cabin/frame_006.gif", 0.04,
                                      "img/bg/cabin/frame_007.gif", 0.04,
                                      "img/bg/cabin/frame_008.gif", 0.04,
                                      "img/bg/cabin/frame_009.gif", 0.04,
                                      "img/bg/cabin/frame_010.gif", 0.04,
                                      "img/bg/cabin/frame_011.gif", 0.04,
                                      "img/bg/cabin/frame_012.gif", 0.04,
                                      "img/bg/cabin/frame_013.gif", 0.04,
                                      "img/bg/cabin/frame_014.gif", 0.04,
                                      "img/bg/cabin/frame_015.gif", 0.04,
                                      "img/bg/cabin/frame_016.gif", 0.04,
                                      "img/bg/cabin/frame_017.gif", 0.04,
                                      "img/bg/cabin/frame_018.gif", 0.04,
                                      "img/bg/cabin/frame_019.gif", 0.04,
                                      "img/bg/cabin/frame_020.gif", 0.04,
                                      "img/bg/cabin/frame_021.gif", 0.04,
                                      "img/bg/cabin/frame_022.gif", 0.04,
                                      "img/bg/cabin/frame_023.gif", 0.04,
                                      "img/bg/cabin/frame_024.gif", 0.04,
                                      "img/bg/cabin/frame_025.gif", 0.04,
                                      "img/bg/cabin/frame_026.gif", 0.04,
                                      "img/bg/cabin/frame_027.gif", 0.04,
                                      "img/bg/cabin/frame_028.gif", 0.04,
                                      "img/bg/cabin/frame_029.gif", 0.04,
                                      "img/bg/cabin/frame_030.gif", 0.04,
                                      "img/bg/cabin/frame_031.gif", 0.04,
                                      "img/bg/cabin/frame_032.gif", 0.04,
                                      "img/bg/cabin/frame_033.gif", 0.04,
                                      "img/bg/cabin/frame_034.gif", 0.04,
                                      "img/bg/cabin/frame_035.gif", 0.04,
                                      "img/bg/cabin/frame_036.gif", 0.04,
                                      "img/bg/cabin/frame_037.gif", 0.04,
                                      "img/bg/cabin/frame_038.gif", 0.04,
                                      "img/bg/cabin/frame_039.gif", 0.04,
                                      "img/bg/cabin/frame_040.gif", 0.04,
                                      "img/bg/cabin/frame_041.gif", 0.04,
                                      "img/bg/cabin/frame_042.gif", 0.04)

                                      
  image bg classroom = "img/bg/classroom/CS_Classroom_background_Light.png"
  image classroom light = "img/bg/crimescene/classroom/CS_Classroom_background_Light.png"
  image classroom dark = "img/bg/crimescene/classroom/CS_Classroom_background_Dark.png"
  image bg citymap = "img/map/Map_Background.png"
  
  
  transform basicfade:
      on show:
          alpha 0.0
          linear 0.3 alpha 1.0
      on hide:
          linear 0.3 alpha 0.0