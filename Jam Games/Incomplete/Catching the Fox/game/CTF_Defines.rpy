init:
  ####Variable Defines####
  $TutorialInProgress = False
  #last day should be sunday 3rd June
  $ gamestart_dayofweek = 1
  $ gamestart_dayofmonth = 3
  $ gamestart_month = 6
  
  #Number of ingameWeeks
  $ numberOfGameWeeks = 2
  
  if numberOfGameWeeks == 1: #start on sunday 1 week before wedding
    $ gamestart_dayofweek = 1
    $ gamestart_dayofmonth = 27
    $ gamestart_month = 5
    
  else:
    if numberOfGameWeeks == 2: #start on sunday 2 weeks before wedding
      $ gamestart_dayofweek = 1
      $ gamestart_dayofmonth = 20
      $ gamestart_month = 5
      #20 13 6
    else:
      if numberOfGameWeeks == 3: #start on sunday 3 weeks before wedding
        $ gamestart_dayofweek = 1
        $ gamestart_dayofmonth = 13
        $ gamestart_month = 5
        #20 13 6
    
  if persistent.SolEnd is None:
    $persistent.SolEnd = False
  if persistent.MiloEnd is None:
    $persistent.MiloEnd = False
  if persistent.JoelEnd is None:
    $persistent.JoelEnd = False    
    
  if persistent.TutorialComplete is None:
    $persistent.TutorialComplete = False

  ####Background images####
  image bg office = "images/bgs/office_cubicle.png"
  image bg office2 = "images/bgs/office_cubicle.png"
  image bg office3 = "images/bgs/office_cubicle.png"
  image bg office4 = "images/bgs/office_cubicle.png"
  
  
  ####Character defines####
  # CHARACTERS
  define si = Character('Simone', image="simone", window_background="images/ui/text_box_no_buttons.png", what_prefix="{color=e87e21}",  what_suffix="{/color}", who_prefix="{color=924603}",  who_suffix="{/color}")
  define so = Character('Solomon', image="solomon", color="#7CD79E", window_background="images/ui/text_box_no_buttons.png", what_prefix="{color=e87e21}",  what_suffix="{/color}", who_prefix="{color=924603}",  who_suffix="{/color}")
  define mi = Character('Milo', image="milo", color="#FFB14A", window_background="images/ui/text_box_no_buttons.png", what_prefix="{color=e87e21}",  what_suffix="{/color}", who_prefix="{color=924603}",  who_suffix="{/color}")
  define jo = Character('Joel', image="joel", color="#FFFBB2", window_background="images/ui/text_box_no_buttons.png", what_prefix="{color=e87e21}",  what_suffix="{/color}", who_prefix="{color=924603}",  who_suffix="{/color}")
  define tr = Character('Trina', image="trina", color="#FF98B0", window_background="images/ui/text_box_no_buttons.png", what_prefix="{color=e87e21}",  what_suffix="{/color}", who_prefix="{color=924603}",  who_suffix="{/color}")
  
  define narrator = Character(None, who_prefix="{color=924603}",  who_suffix="{/color}", window_background="images/ui/text_box_no_buttons.png", what_prefix="{color=e87e21}",  what_suffix="{/color}", what_italic='True')
  
  define z = Character('???', color="#FFFBB2", window_background="images/ui/text_box_no_buttons.png", what_prefix="{color=e87e21}",  what_suffix="{/color}", who_prefix="{color=c8ffc8}",  who_suffix="{/color}")
  
  #SINGLE-USE CHARACTERS
  
  define g = Character('Scott', color="#FF98B0", window_background="images/ui/text_box_no_buttons.png", what_prefix="{color=e87e21}",  what_suffix="{/color}", who_prefix="{color=924603}",  who_suffix="{/color}")
  define c = Character('Guillaume', color="#FF98B0", window_background="images/ui/text_box_no_buttons.png", what_prefix="{color=e87e21}",  what_suffix="{/color}", who_prefix="{color=924603}",  who_suffix="{/color}")
  define d = Character('Debra', color="#FF98B0", window_background="images/ui/text_box_no_buttons.png", what_prefix="{color=e87e21}",  what_suffix="{/color}", who_prefix="{color=924603}",  who_suffix="{/color}")
  define w = Character('Wait Staff', color="#FF98B0", window_background="images/ui/text_box_no_buttons.png", what_prefix="{color=e87e21}",  what_suffix="{/color}", who_prefix="{color=924603}",  who_suffix="{/color}")
  define n = Character('Nick', color="#FF98B0", window_background="images/ui/text_box_no_buttons.png", what_prefix="{color=e87e21}",  what_suffix="{/color}", who_prefix="{color=924603}",  who_suffix="{/color}")
  define sp = Character('Spade', color="#FF98B0", window_background="images/ui/text_box_no_buttons.png", what_prefix="{color=e87e21}",  what_suffix="{/color}", who_prefix="{color=924603}",  who_suffix="{/color}")
  define sin = Character('Simone', color="#FF98B0", window_background="images/ui/text_box_no_buttons.png", what_prefix="{color=e87e21}",  what_suffix="{/color}", who_prefix="{color=924603}",  who_suffix="{/color}")
  define se = Character('Paulo', color="#FF98B0", window_background="images/ui/text_box_no_buttons.png", what_prefix="{color=e87e21}",  what_suffix="{/color}", who_prefix="{color=924603}",  who_suffix="{/color}")
  define ob = Character('Old Boss', color="#FF98B0", window_background="images/ui/text_box_no_buttons.png", what_prefix="{color=e87e21}",  what_suffix="{/color}", who_prefix="{color=924603}",  who_suffix="{/color}")
  
  ####Character images####
    
  ##SIMONE

  image simone angry = "images/sprites/Simone/Sim_default_angry.png"
  image simone bored = "images/sprites/Simone/Sim_default_bored.png"
  image simone depressed = "images/sprites/Simone/Sim_default_depressed.png"
  image simone happy = "images/sprites/Simone/Sim_default_happy.png"
  image simone incredulous = "images/sprites/Simone/Sim_default_incredulous.png"
  image simone lovesick = "images/sprites/Simone/Sim_default_lovesick.png"
  image simone neutral = "images/sprites/Simone/Sim_default_default.png"
  image simone panic = "images/sprites/Simone/Sim_default_panic.png"
  image simone sad = "images/sprites/Simone/Sim_default_sad.png"
  image simone sigh = "images/sprites/Simone/Sim_default_sigh.png"
  image simone smile = "images/sprites/Simone/Sim_default_smile.png"
  image simone surprised = "images/sprites/Simone/Sim_default_surprised.png"
  image simone thinking = "images/sprites/Simone/Sim_default_thinking.png"
  image simone uncomf = "images/sprites/Simone/Sim_default_uncomfortable.png"
  image simone worried = "images/sprites/Simone/Sim_default_worried.png"

  image simone w angry = "images/sprites/Simone/Sim_wed_angry.png"
  image simone w bored = "images/sprites/Simone/Sim_wed_bored.png"
  image simone w depressed = "images/sprites/Simone/Sim_wed_depressed.png"
  image simone w happy = "images/sprites/Simone/Sim_wed_happy.png"
  image simone w incredulous = "images/sprites/Simone/Sim_wed_incredulous.png"
  image simone w lovesick = "images/sprites/Simone/Sim_wed_lovesick.png"
  image simone w panic = "images/sprites/Simone/Sim_wed_panic.png"
  image simone w sad = "images/sprites/Simone/Sim_wed_sad.png"
  image simone w sigh = "images/sprites/Simone/Sim_wed_sigh.png"
  image simone w smile = "images/sprites/Simone/Sim_wed_smile.png"
  image simone w surprised = "images/sprites/Simone/Sim_wed_surprised.png"
  image simone w thinking = "images/sprites/Simone/Sim_wed_thinking.png"
  image simone w uncomf = "images/sprites/Simone/Sim_wed_uncomfortable.png"
  image simone w worried = "images/sprites/Simone/Sim_wed_worried.png"


  ##SOLOMON

  image solomon disappointed = "images/sprites/Solomon/Sol_default_disappointed.png"
  image solomon neutral = "images/sprites/Solomon/Sol_default_neutral.png"
  image solomon serious = "images/sprites/Solomon/Sol_default_serious.png"
  image solomon sigh = "images/sprites/Solomon/Sol_default_sigh.png"
  image solomon smile = "images/sprites/Solomon/Sol_default_smiling.png"
  image solomon surprised = "images/sprites/Solomon/Sol_default_surprised.png"
  image solomon upset = "images/sprites/Solomon/Sol_default_upset.png"

  image solomon w disappointed = "images/sprites/Solomon/Sol_wed_disappointed.png"
  image solomon w neutral = "images/sprites/Solomon/Sol_wed_neutral.png"
  image solomon w serious = "images/sprites/Solomon/Sol_wed_serious.png"
  image solomon w sigh = "images/sprites/Solomon/Sol_wed_sigh.png"
  image solomon w smile = "images/sprites/Solomon/Sol_wed_smiling.png"
  image solomon w surprised = "images/sprites/Solomon/Sol_wed_surprised.png"
  image solomon w upset = "images/sprites/Solomon/Sol_wed_upset.png"

  ##MILO

  image milo disappointed = "images/sprites/Milo/M_default_disappointed.png"
  image milo neutral = "images/sprites/Milo/M_default_nutral.png"
  image milo serious = "images/sprites/Milo/M_default_serious.png"
  image milo sigh = "images/sprites/Milo/M_default_sigh.png"
  image milo smile = "images/sprites/Milo/M_default_smiling.png"
  image milo surprised = "images/sprites/Milo/M_default_surprised.png"
  image milo upset = "images/sprites/Milo/M_default_upset.png"

  image milo w disappointed = "images/sprites/Milo/M_wed_disappointed.png"
  image milo w neutral = "images/sprites/Milo/M_wed_neutral.png"
  image milo w serious = "images/sprites/Milo/M_wed_serious.png"
  image milo w sigh = "images/sprites/Milo/M_wed_sigh.png"
  image milo w smile = "images/sprites/Milo/M_wed_smiling.png"
  image milo w surprised = "images/sprites/Milo/M_wed_surprised.png"
  image milo w upset = "images/sprites/Milo/M_wed_upset.png"

  ##JOEL

  image j blush = "images/sprites/Joel/J-blush.png"
  image j blush2 = "images/sprites/Joel/J-blushMORE.png"

  image joel disappointed = "images/sprites/Joel/J_default_disappointed.png"
  image joel neutral = "images/sprites/Joel/J_default_neutral.png"
  image joel serious = "images/sprites/Joel/J_default_serious.png"
  image joel sigh = "images/sprites/Joel/J_default_sigh.png"
  image joel smile = "images/sprites/Joel/J_default_smile.png"
  image joel surprised = "images/sprites/Joel/J_default_surprised.png"
  image joel upset = "images/sprites/Joel/J_default_upset.png"

  image joel w disappointed = "images/sprites/Joel/J_wed_disappointed.png"
  image joel w neutral = "images/sprites/Joel/J_wed_neutral.png"
  image joel w serious = "images/sprites/Joel/J_wed_serious.png"
  image joel w sigh = "images/sprites/Joel/J_wed_sigh.png"
  image joel w smile = "images/sprites/Joel/J_wed_smile.png"
  image joel w surprised = "images/sprites/Joel/J_wed_surprised.png"
  image joel w upset = "images/sprites/Joel/J_wed_upset.png"

  ##TRINA

  image trina neutral = "images/sprites/Trina/T_def_default.png"
  image trina disappointed = "images/sprites/Trina/T_def_disappointed.png"
  image trina happy = "images/sprites/Trina/T_def_happy.png"
  image trina smirk = "images/sprites/Trina/T_def_smirk.png"
  image trina surprised = "images/sprites/Trina/T_def_surprised.png"

  image trina w neutral = "images/sprites/Trina/T_wed_default.png"
  image trina w disappointed = "images/sprites/Trina/T_wed_disappointed.png"
  image trina w happy = "images/sprites/Trina/T_wed_happy.png"
  image trina w smirk = "images/sprites/Trina/T_wed_smirk.png"
  image trina w surprised = "images/sprites/Trina/T_wed_surprise.png"
  
  # BACKGROUNDS
  image map = "images/ui/overlay.png"
  image comp_bg = "images/ui/Tut/0.png"
  image office = "images/bgs/office space.png"
  image office cubicle = "images/bgs/office_cubicle.png"
  image meeting_room = "images/bgs/conf_room.png"
  image west_home = "images/bgs/apartment.png"
  image fox_office = "images/bgs/sol office.png"
  image o_kitchen = "images/bgs/office_kitchen.png"
  image wedding = "images/bgs/wedding.png"
  image balcony = "images/bgs/balcony.png"
  image old_cafe = "images/bgs/cafe_day.png"
  image trina_cafe = "images/bgs/cafe_day.png"
  image past_filter = "images/bgs/past_filter.png"

  image kicon = "images/ui/kicon.png"
  image licon = "images/ui/licon.png"
  image cicon = "images/ui/cicon.png"
  image sicon = "images/ui/sicon.png"
  image micon = "images/ui/micon.png"
  image jicon = "images/ui/jicon.png"

  define config.say_attribute_transition = dissolve
  

init:
    $ cleft = Position (xpos=0.25, xanchor=0.25)
    $ cright = Position (xpos=0.75, xanchor=0.75)
    
