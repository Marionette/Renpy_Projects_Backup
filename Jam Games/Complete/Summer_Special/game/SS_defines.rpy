init python:
  def CreateLiveComposite(character="Cereza", brow="normal", eye="normal", mouth="normal", blush="none", pose=None):    
    if character == 'Cereza':
      if pose == None:
        pose = renpy.random.choice(['1','2'])
      return LiveComposite( 
      (474, 800),
      (0, 0), "images/sprites/Cereza/pose%s.png"%pose,
      (0, 0), "images/sprites/Cereza/brow_%s.png"%brow,
      (0, 0), "images/sprites/Cereza/eye_%s.png"%eye,
      (0, 0), "images/sprites/Cereza/mouth_%s.png"%mouth,
      (0, 0), "images/sprites/Cereza/blush_%s.png"%blush)


    if character == 'June':
      if pose == None:
        leftArm = renpy.random.choice(['1','2', '3'])
        rightArm = renpy.random.choice(['right-down','right-Hip'])
        if leftArm == '1':
          backArm = 'left-down'
          frontArmL = 'none'
        else: 
          if leftArm == '2': 
            backArm = 'left-up'
            frontArmL = 'none'
          else: 
            backArm = 'none'
            frontArmL = 'left-chin'
          
      return LiveComposite( 
      (484, 800),
      (0, 0), "images/sprites/June/back_arm-%s.png"%backArm,
      (0, 0), "images/sprites/June/jacket_back.png",
      (0, 0), "images/sprites/June/body.png",
      (0, 0), "images/sprites/June/pants.png",
      (0, 0), "images/sprites/June/shirt.png",
      (0, 0), "images/sprites/June/jacket_front.png",
      (0, 0), "images/sprites/June/brow_%s.png"%brow,
      (0, 0), "images/sprites/June/eye_%s.png"%eye,
      (0, 0), "images/sprites/June/mouth_%s.png"%mouth,
      (0, 0), "images/sprites/June/blush_%s.png"%blush,
      (0, 0), "images/sprites/June/front_arm-%s.png"%frontArmL,
      (0, 0), "images/sprites/June/front_arm-%s.png"%rightArm)
      
      
    if character == 'Kameron':
      if pose == None:
        leftArm = renpy.random.choice(['1','2'])
        rightArm = renpy.random.choice(['1','2'])
        if leftArm == '1':
          backArmL = 'leftDown'
          frontArmL = 'none'
        else: 
          backArmL = 'none'
          frontArmL = 'LeftOut'
          
        if rightArm == '1': 
          backArmR = 'RightDown'
          frontArmR = 'none'
        else: 
          backArmR = 'none'
          frontArmR = 'RightRaised'
          
      return LiveComposite( 
      (480, 800),
      (0, 0), "images/sprites/Kameron/arm-%s.png"%backArmL,
      (0, 0), "images/sprites/Kameron/arm-%s.png"%backArmR,
      (0, 0), "images/sprites/Kameron/body.png",
      (0, 0), "images/sprites/Kameron/pants.png",
      (0, 0), "images/sprites/Kameron/shirt.png",
      (0, 0), "images/sprites/Kameron/brow_%s.png"%brow,
      (0, 0), "images/sprites/Kameron/eye_%s.png"%eye,
      (0, 0), "images/sprites/Kameron/mouth_%s.png"%mouth,
      (0, 0), "images/sprites/Kameron/blush_%s.png"%blush,
      (0, 0), "images/sprites/Kameron/arm-%s.png"%frontArmL,
      (0, 0), "images/sprites/Kameron/arm-%s.png"%frontArmR)
      
    if character == 'Rafael':
      if pose == None:
        arms = renpy.random.choice(['1','2'])
          
      return LiveComposite( 
      (480, 800),
      (0, 0), "images/sprites/Rafael/body.png",
      (0, 0), "images/sprites/Rafael/hair.png",
      (0, 0), "images/sprites/Rafael/pants.png",
      (0, 0), "images/sprites/Rafael/shirt.png",
      (0, 0), "images/sprites/Rafael/necklace.png",
      (0, 0), "images/sprites/Rafael/ponytail.png",
      (0, 0), "images/sprites/Rafael/brow_%s.png"%brow,
      (0, 0), "images/sprites/Rafael/eye_%s.png"%eye,
      (0, 0), "images/sprites/Rafael/mouth_%s.png"%mouth,
      (0, 0), "images/sprites/Rafael/blush_%s.png"%blush,
      (0, 0), "images/sprites/Rafael/arms%s.png"%arms)

  def CreateLiveCompositeNPC(character="Mona", emotion="normal"):  
      return LiveComposite( 
      (484, 800),
      (0, 0), "images/sprites/Other/%s_body.png"%(character),
      (0, 0), "images/sprites/Other/%s_%s.png"%(character, emotion),
      (0, 0), "images/sprites/Other/%s_hair.png"%(character))  

      
init:
  ######### PERSISTANT VARIABLE DEFINES #############
  if persistent.GameFinished == None:
    $persistent.GameFinished = False
    
  ######### VARIABLE DEFINES #############
  $show_quick_menu = True
  $CurrentTimeOfDayName = 'morning'
  $CurrentDayName = 'monday'
  $relationship_June = 0
  $relationship_Kameron = 0
  $relationship_Rafael = 0
  $HasMetRafael = False
  


  ######### CHARACTER DEFINES #############
  define narrator = Character(None, window_background="images/ui/textbox_base.png")
  define ce = Character('Cereza', color="#fff", window_background="images/ui/textbox_named.png", who_prefix="{font=assets/PWShaded.ttf}", who_suffix="{/font}")
  define ju = Character('June', color="#fff", window_background="images/ui/textbox_named.png", who_prefix="{font=assets/PWShaded.ttf}", who_suffix="{/font}")
  define co = Character('Cody', color="#c8ffc8", window_background="images/ui/textbox_named.png", who_prefix="{font=assets/PWShaded.ttf}", who_suffix="{/font}")
  define ma = Character('Madison', color="#c8ffc8", window_background="images/ui/textbox_named.png", who_prefix="{font=assets/PWShaded.ttf}", who_suffix="{/font}")
  define ra = Character('Rashid', color="#c8ffc8", window_background="images/ui/textbox_named.png", who_prefix="{font=assets/PWShaded.ttf}", who_suffix="{/font}")
  define mo = Character('Mona', color="#c8ffc8", window_background="images/ui/textbox_named.png", who_prefix="{font=assets/PWShaded.ttf}", who_suffix="{/font}")
  define ka = Character('Kameron', color="#c8ffc8", window_background="images/ui/textbox_named.png", who_prefix="{font=assets/PWShaded.ttf}", who_suffix="{/font}")
  define rf = Character('Rafael', color="#c8ffc8", window_background="images/ui/textbox_named.png", who_prefix="{font=assets/PWShaded.ttf}", who_suffix="{/font}")
  define gr = Character('Grandma', color="#c8ffc8", window_background="images/ui/textbox_named.png", who_prefix="{font=assets/PWShaded.ttf}", who_suffix="{/font}")
  define un = Character('???', color="#fff", window_background="images/ui/textbox_named.png", who_prefix="{font=assets/PWShaded.ttf}", who_suffix="{/font}")

  ######### CG/BG IMAGE DEFINES #############
  
  image bg grandmaHouse = "images/bg/bg_grandmaHouse.jpg"
  image bg storeFront = "images/bg/bg_storeFront.jpg"
  image bg storeInside_Register = "images/bg/bg_storeInside_Register.jpg"
  image bg storeOutside back1 = "images/bg/bg_storeOutside1_Back.jpg"
  image bg storeOutside back2 = "images/bg/bg_storeOutside2_Back.jpg"
  image storeRegister = "images/bg/bg_storeRegister.png"
  image bg storeRoof1 = "images/bg/bg_storeRoof1.jpg"
  image bg storeRoof2 = "images/bg/bg_storeRoof2.jpg"
  image bg store breakroom = "images/bg/bg_storeBreakroom.jpg"  
  
  image cg juneIntro1 = "images/cg/cg_juneIntro1.jpg"    
  image cg juneIntro2 = "images/cg/cg_juneIntro2.jpg"    
  image cg chibiJune Eat = "images/cg/cg_chibiJuneEat.png"  
  image cg chibiJune Phone1 = "images/cg/cg_chibiJunePhone1.png" 
  image cg chibiJune Phone2 = "images/cg/cg_chibiJunePhone2.png" 
  image cg chibiJune Phone3 = "images/cg/cg_chibiJunePhone3.png" 
  image cg chibiJune Phone4 = "images/cg/cg_chibiJunePhone4.png" 
  image cg chibiJune Phone5 = "images/cg/cg_chibiJunePhone5.png"  
  image cg chibiJune Phone6 = "images/cg/cg_chibiJunePhone6.png"   
  image cg chibiJune Phone7 = "images/cg/cg_chibiJunePhone7.png" 
  
  image cg kamIntro1 = "images/cg/cg_kamIntro1.jpg"    
  image cg kamIntro2 = "images/cg/cg_kamIntro2.jpg"      
  image cg chibiKam Phone1 = "images/cg/cg_chibiKamPhone1.png" 
  image cg chibiKam Phone2 = "images/cg/cg_chibiKamPhone2.png" 
  image cg chibiKam Phone3 = "images/cg/cg_chibiKamPhone3.png" 
  image cg chibiKam Phone4 = "images/cg/cg_chibiKamPhone4.png" 
  image cg chibiKam Phone5 = "images/cg/cg_chibiKamPhone5.png"  
  image cg chibiKam Phone6 = "images/cg/cg_chibiKamPhone6.png"   
  image cg chibiKam Phone7 = "images/cg/cg_chibiKamPhone7.png"   
  
  
  ## Image list for CG Gallery ##
  $gallery_cg_items = ["cg juneIntro1",  
                      "cg juneIntro2", 
                      "cg chibiJune Eat", 
                      "cg chibiJune Phone1", 
                      "cg chibiJune Phone2", 
                      "cg chibiJune Phone3", 
                      "cg chibiJune Phone4", 
                      "cg chibiJune Phone5", 
                      "cg chibiJune Phone6", 
                      "cg chibiJune Phone7",
                      "cg kamIntro1", 
                      "cg kamIntro2", 
                      "cg chibiKam Phone1", 
                      "cg chibiKam Phone2", 
                      "cg chibiKam Phone3", 
                      "cg chibiKam Phone4", 
                      "cg chibiKam Phone5", 
                      "cg chibiKam Phone6", 
                      "cg chibiKam Phone7" ] 
                      
  ######### CHARACTER IMAGE DEFINES #############
  
  ##Cereza##
   
  #normal
  image cereza normal = CreateLiveComposite('Cereza' , "normal" , "normal" , "normal")
  image cereza happy = CreateLiveComposite('Cereza', "normal" , "upturned" , "happy" , "big")
  image cereza sad = CreateLiveComposite('Cereza', "bunched" , "leftSquint" , "pout")
  image cereza angry = CreateLiveComposite('Cereza', "furrowed" , "rightSquint" , "frown" , "small")
  image cereza grin = CreateLiveComposite('Cereza', "raised" , "upturned" , "grin")
  image cereza tease = CreateLiveComposite('Cereza', "raised" , "wink" , "big-smile")
  image cereza unimpressed = CreateLiveComposite('Cereza', "normal" , "dead" , "small")
  image cereza surprise = CreateLiveComposite('Cereza', "raised" , "wide" , "eh" , "small")
  image cereza pissed = CreateLiveComposite('Cereza', "furrowed" , "normal-right" , "yell")
  image cereza smirk = CreateLiveComposite('Cereza', "quirked" , "normal" , "smirk")
  image cereza tired = CreateLiveComposite('Cereza', "furrowed" , "downturned" , "oh")
  image cereza embarrassed = CreateLiveComposite('Cereza', "bunched" , "leftSquint" , "ehh" , "big")
  image cereza hurt = CreateLiveComposite('Cereza', "bunched" , "cry" , "small" , "big")
  image cereza disbelief = CreateLiveComposite('Cereza', "quirked" , "twitch" , "ehh" , "small", pose='1')
  image cereza confused  = CreateLiveComposite('Cereza', "bunched" , "normal" , "ah" , "big")

  image cereza normal2 = CreateLiveComposite('Cereza', pose='2')
  
  
  ##June##
  image june normal = CreateLiveComposite('June' , "normal" , "normal-left" , "normal")
  image june happy = CreateLiveComposite('June' , "raised" , "upturned" , "big-happy")
  image june sad = CreateLiveComposite('June' , "furrowed" , "downturned" , "frown")
  image june angry = CreateLiveComposite('June' , "furrowed" , "normal-left" , "clench" , "big")
  image june grin = CreateLiveComposite('June' , "raised" , "wink" , "grin")
  image june tease = CreateLiveComposite('June' , "quirked" , "hooded" , "grin")
  image june unimpressed = CreateLiveComposite('June' , "normal" , "dead" , "flat")
  image june surprise = CreateLiveComposite('June' , "raised" , "wide" , "big-happy" , "small")
  image june pissed = CreateLiveComposite('June' , "furrowed" , "hooded" , "snarl")
  image june smirk = CreateLiveComposite('June' , "quirked" , "wink" , "smile")
  image june tired = CreateLiveComposite('June' , "bunched" , "downturned" , "ehh" , "small")
  image june embarrassed = CreateLiveComposite('June' , "bunched" , "hooded" , "ah")
  image june hurt = CreateLiveComposite('June' , "bunched" , "normal-right" , "frown" , "big")
  image june disbelief = CreateLiveComposite('June' , "bunched" , "upturned" , "smile")
  image june confused = CreateLiveComposite('June' , "bunched" , "normal-right" , "ah")
  image june smile = CreateLiveComposite('June' , "normal" , "upturned" , "normal")  
  
  ##Kameron##
  image kameron normal = CreateLiveComposite('Kameron', "normal", "normal", "normal" )
  image kameron happy = CreateLiveComposite('Kameron', "normal", "upturned", "smile", "big")
  image kameron sad = CreateLiveComposite('Kameron', "bunched", "downturned", "frown")
  image kameron angry = CreateLiveComposite('Kameron', "furrowed", "hooded", "frown" )
  image kameron grin = CreateLiveComposite('Kameron', "normal", "normal", "grin")
  image kameron tease = CreateLiveComposite('Kameron', "quirked", "hooded-right", "big-happy", "small")
  image kameron unimpressed = CreateLiveComposite('Kameron', "normal", "dead", "flat" )
  image kameron surprise = CreateLiveComposite('Kameron', "raised", "wide", "yell", "big")
  image kameron pissed = CreateLiveComposite('Kameron', "furrowed", "downturned", "yell")
  image kameron smirk = CreateLiveComposite('Kameron', "bunched", "hooded-right", "smirk", "small")
  image kameron tired = CreateLiveComposite('Kameron', "bunched", "downturned", "eh")
  image kameron embarrassed = CreateLiveComposite('Kameron', "bunched", "wink", "smile", "small")
  image kameron hurt = CreateLiveComposite('Kameron', "bunched", "hooded", "ah" )
  image kameron disbelief = CreateLiveComposite('Kameron', "quirked", "hooded-right", "frown", "big")
  image kameron confused = CreateLiveComposite('Kameron', "bunched", "normal", "ehh", "big")
  
  ##Rafael##
  image rafael happy = CreateLiveComposite('Rafael', "raised", "normal", "smile" )
  image rafael sad = CreateLiveComposite('Rafael', "bunched", "hooded", "flat", "small")
  image rafael angry = CreateLiveComposite('Rafael', "furrowed", "normal", "snarl", "small")
  image rafael grin = CreateLiveComposite('Rafael', "raised", "upturned", "grin", "small")
  image rafael tease = CreateLiveComposite('Rafael', "quirked", "hooded", "smirk" )
  image rafael unimpressed = CreateLiveComposite('Rafael', "normal", "dead", "small", "small")
  image rafael surprise = CreateLiveComposite('Rafael', "bunched", "wide", "ah", "big")
  image rafael pissed = CreateLiveComposite('Rafael', "furrowed", "hooded", "yell")
  image rafael smirk = CreateLiveComposite('Rafael', "normal", "normal-right", "smirk" )
  image rafael tired = CreateLiveComposite('Rafael', "bunched", "downturned", "eh", "small")
  image rafael embarrassed = CreateLiveComposite('Rafael', "bunched", "wide", "flat", "big")
  image rafael hurt = CreateLiveComposite('Rafael', "furrowed", "cry", "ah", "small")
  image rafael disbelief = CreateLiveComposite('Rafael', "quirked", "normal-right", "eh", "small")
  image rafael confused = CreateLiveComposite('Rafael', "quirked", "dead", "ehh", "big")
  image rafael crying = CreateLiveComposite('Rafael', "bunched", "big-cry", "yell", "big")
  
  ##Cody##
  image cody normal = CreateLiveCompositeNPC('Cody', 'normal')
  image cody cry big = CreateLiveCompositeNPC('Cody', 'big-cry')
  image cody cry = CreateLiveCompositeNPC('Cody', 'cry')
  image cody happy = CreateLiveCompositeNPC('Cody', 'happy')
  image cody sad = CreateLiveCompositeNPC('Cody', 'sad')
  image cody shock = CreateLiveCompositeNPC('Cody', 'shock')
  image cody smile = CreateLiveCompositeNPC('Cody', 'smile')
  image cody worry = CreateLiveCompositeNPC('Cody', 'worry')
  
  
  ##Rashied##
  image rashied normal = CreateLiveCompositeNPC('Rashied', 'normal')
  image rashied happy = CreateLiveCompositeNPC('Rashied', 'happy')
  image rashied sad = CreateLiveCompositeNPC('Rashied', 'sad')
  image rashied smile = CreateLiveCompositeNPC('Rashied', 'smile')
  image rashied tease = CreateLiveCompositeNPC('Rashied', 'tease')
  image rashied worry = CreateLiveCompositeNPC('Rashied', 'worry')
  
  
  ##Madison##
  image madison normal = CreateLiveCompositeNPC('Madison', 'normal')
  image madison angry = CreateLiveCompositeNPC('Madison', 'angry')
  image madison happy = CreateLiveCompositeNPC('Madison', 'happy')
  image madison joke = CreateLiveCompositeNPC('Madison', 'joke')
  image madison sad = CreateLiveCompositeNPC('Madison', 'sad')
  image madison tease = CreateLiveCompositeNPC('Madison', 'tease')
  
  
  ##Mona##
  image mona normal = CreateLiveCompositeNPC('Mona', 'normal')
  image mona angry = CreateLiveCompositeNPC('Mona', 'angry')
  image mona embarrased = CreateLiveCompositeNPC('Mona', 'embarrased')
  image mona happy = CreateLiveCompositeNPC('Mona', 'happy')
  image mona sad = CreateLiveCompositeNPC('Mona', 'sad')
  image mona smile = CreateLiveCompositeNPC('Mona', 'smile')
  
  
  ##Robber##
  image robber hood_1 = "images/sprites/Other/Robber1.png"
  image robber hood_2 = "images/sprites/Other/Robber2.png"
  image robber nohood_1 = "images/sprites/Other/Robber3.png"
  image robber nohood_2 = "images/sprites/Other/Robber4.png"
  