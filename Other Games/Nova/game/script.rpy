 
init:
  # You can place the script of your game in this file.

  # Declare images below this line, using the image statement.
  # eg. image eileen happy = "eileen_happy.png"
  $currentPath = "A"
  $revivalExperimentFlag = False
  $PathB_4_5_o_Flag = False
  $AChoiceCount = 0
  $BChoiceCount = 0
  $CChoiceCount = 0


# The game starts here.
label start:
    #show ranan past content
    #"..."
    #play music music_Words
    #"play words"
    #"..."
    #show ranan  content
    #"..."
    #show ranan past content OM 
    #"..."
    #show ranan  content OM 
    #"..."
    #show ranan past grim
    #"..."
    #show ranan  grim
    #"..."
    #show ranan past neutral
    #"..."
    #show ranan past neutral OM 
    #"..."
    #show ranan past resentful
    #"..."
    #show ranan past sad
    #"..."




    #Comment out this jump to run test code.
    jump lbl_introduction 
    
    #jump lbl_scriptTest
    
    #jump lbl_jumpTest
    
    #menu:
    #  "Introduction":
    #    jump lbl_introduction
    #  "1.1":
    #    jump lbl_chapter1
    #  "1.9":
    #    jump lbl_1_9
    #  "next...":
    #    pass
    #    
    #menu:
    #  "A2.0":
    #    jump lbl_chapter2
    #  "A3.0":
    #    jump lbl_chapter3
    #  "A4.0":
    #    jump lbl_chapter4
    #  "A5.0":
    #    jump lbl_chapter5
    #  "A6.0":
    #    jump lbl_chapter6
    #  "next...":
    #    pass
    #    
    #menu:
    #  "A7.0":
    #    jump lbl_chapter7
    #  "A8.0":
    #    jump lbl_chapter8
    #  "A9.0":
    #    jump lbl_chapter9
    #  "A10.0":
    #    jump lbl_chapter10
    #  "Magic Test":
    #    jump testpart1
    #  "next...":
    #    pass
    
    ##Test code goes here##
    #show fa1t  
    #show fa2  
    #show fa3  
    #show fa4  
    #show fa5  
    #show fa6  
    #show fa7  
    #show fa8  
    #show fa9  
    #show fa10 
    #scene bg
    #
    #"Hi I am the narrator. Say hi everyone else. (Story starts after the introductions. tehe~)"
    #
    #show merona content
    #mk "Hi"
    #show merona sleepy 
    #mi "Hi"
    #dt "Hi"
    #ln "Hi"
    #pm "Hi"  
    #ns "Hi"
    #rs "Hi"
    #show cimaria content
    #ck "Hi"
    #rt "Hi"
    #show kreita content
    #kh "Hi"
    #bg "Hi"
    #hw "Hi"
    #qv "Hi"
    #kd "Hi"
    #mf "Hi"
    #mm "Hi"
    
    return
    
label testpart1:
    scene cg MeronasRoom_2
    
    show fireAttack movie
    show fireAttackBig movie
    show airAttack movie
    show steam movie
    show swordAttack movie
    pause(0.5)
    hide fireAttack
    hide fireAttackBig
    hide airAttack
    hide steam
    hide swordAttack
    mi "..."
    show swordAttack movie
    pause(1.24)
    hide swordAttack    
    mi "1.0"
    show swordAttack movie
    pause(0.9)
    hide swordAttack    
    mi "0.9"
    show swordAttack movie
    pause(0.8)
    hide swordAttack    
    mi "0.8"
    show swordAttack movie
    pause(0.7)
    hide swordAttack    
    mi "0.7"
    show swordAttack movie
    pause(0.6)
    hide swordAttack    
    mi "0.6"
    show swordAttack movie
    pause(0.5)
    hide swordAttack    
    mi "0.5"
    show swordAttack movie
    pause(0.4)
    hide swordAttack    
    mi "0.4"    
    show swordAttack movie
    pause(0.3)
    hide swordAttack    
    mi "0.3"    
    show swordAttack movie
    pause(0.2)
    hide swordAttack    
    mi "0.2"
    
    mi "..."
    mi "..."
    
    return
    
    
    
label splashscreen:
    $ renpy.movie_cutscene('img/Nova Opening WebM_80 percent quality.webm')
    scene bg black    
    show startupCredits with Dissolve(2.0, alpha=True)
    $renpy.pause(delay=None)
    scene bg black with Dissolve(2.0, alpha=True)

    return

label lbl_jumpTest:
    

    scene cg dormOutside with fade 
    show merona surprised OM:
      xalign 0.75 #(Merona on the right, behind Kreita, can slightly overlap with her to indicate distance)
      yalign 1.0
    show rett laugh:
      yalign 1.0
      xalign 0.25 #(Rett on the left)
    show kreita grin2:
      yalign 1.0
      xalign 0.5 #(Kreita in the middle)
    show rett content at RunBounce
    show kreita grin at RunBounce
    rt "We'll run in front of you! Just follow us!"
    show rett content at RunBounce
    show kreita grin at RunBounce
    "Before I could give any confirmation, they already began hurrying their way down the path out of the academy grounds."
    show merona disappointed OM at RunBounce
    mk "Egh!"
    scene cg forest5 with fade
    show merona determined:
      yalign 1.0
      xalign 0.75 
    show kreita surprised:
      yalign 1.0
      xalign 0.45 
    show rett content:
      yalign 1.0
      xalign 0.2 
    
    pause(0.1)
    show merona determined at RunBounce:
      xalign 0.75 
    show merona determined at RunBounce:
      linear 1.0 xalign 0.65 
    show kreita surprised at RunBounce:
      xalign 0.45 
    show rett content at RunBounce:
      xalign 0.2 
    "I brushed my bangs back and rushed forward to catch up to them, almost ramming straight into Kreita's back."

    show merona veryScared:
      yalign 1.0
      xalign 0.65 
    show kreita grin at RunBounce
    show merona veryScared at RunBounce:
      linear 1.0 xalign 0.85 
    mi "No, get away from the arrows! There are arrows on that back!"
    show merona determined at RunBounce
    show kreita content at RunBounce
    "I tried making up for my sudden burst forward by slowing myself down, which also led me to being some distance apart from them. Being aware of it this time, I sped up a bit, and got the nice breathing room behind the two that was needed."
    show merona determined at RunBounce#:
    #  linear 1.0 xalign 0.75 
    #pause(0.5)
    show merona worried OM at RunBounce
    $ renpy.transition(slow_dissolve, layer="master")
    mi "Today, I seem to have a talent for accidentally getting people hurt."
    $ renpy.transition(slow_dissolve, layer="master")
    show cg laneo #with dissolve
    #show laneoPeople behind merona #with dissolve 
    show merona determined at RunBounce       
    "Okay, the trees are thinning, so we're approaching the main road and the middle of the city. I flicked my eyes to both sides and caught the flashes of faces looking at us. While Kreita and Rett were dressed for the outdoors, I was still in my uniform. Maybe I should've put on my casual clothes."
    
    
    
    show merona determined CE
    "CreateLiveComposite('Merona' , \"determined\" , \"_u\" , \"_CE\", \"\")"
    show merona disappointed OM CE
    "CreateLiveComposite('Merona' , \"disappointed\" , \"_u\" , \"_OM_CE\", \"\")"
    show merona embarrassed CE
    "CreateLiveComposite('Merona' , \"embarrassed\" , \"_u\" , \"_CE\", \"\")"
    show merona grin CE
    "CreateLiveComposite('Merona' , \"grin\" , \"_u\" , \"_CE\", \"\")"
    show merona nervous CE
    "CreateLiveComposite('Merona' , \"nervous\" , \"_u\" , \"_CE\", \"\")"
    

    $ renpy.transition(slow_dissolve, layer="master")
    #TODO [fade from black into...
    scene cg nightFire at ScrollDown#; show at 100% size #(it is twice the HD size) starting from the top center, zoom out to 50% size and move the camera until the lower end is reached#; here's also an info image for the camera movement: https://drive.google.com/file/d/0By2EUlNeLO3Mbl9iOW5ERDRneVE/view?usp=sharing 

    show nightFire_BoyenKreitaLexanDuran at ScrollUpFromBottom
    #show nightFire Prowen
    #show nightFire Merona
    show nightFire_campFire at ScrollUpFromBottom#; might be animated as a png sequence later if I have time :3
    show nightFire_RettCimaria at ScrollUpFromBottom

    #TODO [Please place the facial expressions directly on top of the corresponding base layer - I'll just summarize them here for easier editing
    show prowen nightFire open behind nightFire_RettCimaria at ScrollUpFromBottom
    show boyen nightFire closed at ScrollUpFromBottom
    show duran nightFire closed at ScrollUpFromBottom
    show kreita nightFire closed at ScrollUpFromBottom
    show lexan nightFire closed at ScrollUpFromBottom
    show merona nightFire closed at ScrollUpFromBottom
    show rett nightFire closed at ScrollUpFromBottom

    #TODO [The following characters have hair over their eyes/ eyebrows, so please place these above the expression layers:
    show nightFire_BoyenKreitaLexanDuran_outlines behind prowen at ScrollUpFromBottom
    #show nightFire Merona outlines
    #show nightFire Rett outlines

    show nightFire_frontPlants at ScrollUpFromBottom
    pm "How long have you all been travelling for?"
    
    return
    