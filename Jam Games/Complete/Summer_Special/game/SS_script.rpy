# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.

# The game starts here.
label start:
    
    #commment out for debug stuff
    jump lbl_day_1

    scene bg storeFront
    show screen TimeOfDayDisplay
    show cereza normal at left:
      yalign 1
    ce "You've created a new Ren'Py game."
    show cereza normal pose2 at left:
      yalign 1

    ju "Once you add a story, pictures, and music, you can release it to the world!"
    show cereza normal2
    "You've created a new Ren'Py game."

    "Once you add a story, pictures, and music, you can release it to the world!"
    
    show cereza normal at left:
      yalign 1
    ce "Hi"
    hide cereza
    show june normal at left:
      yalign 1
    ju "Hi"
    hide june
    show kameron normal at left:
      yalign 1
    ka "Hi"
    hide kameron
    show rafael normal at left:
      yalign 1
    rf "Hi"
    hide rafael
    
    
    show cody normal at left:
      yalign 1
    co "Hi"
    hide cody
    show madison normal at left:
      yalign 1
    ma "Hi"
    hide madison
    show rashied normal at left:
      yalign 1
    ra "Hi"
    hide rashied
    show mona normal at left:
      yalign 1
    mo "Hi"
    hide mona
    "Hi"
    
    show cereza angry
    ""
    show cereza confused
    "" 
    show cereza disbelief
    ""
    show cereza embarrassed
    ""
    show cereza grin
    ""
    show cereza happy
    ""
    show cereza hurt
    ""
    show cereza normal
    ""
    show cereza pissed
    ""
    show cereza sad
    ""
    show cereza smirk
    ""
    show cereza surprise
    ""
    show cereza tease
    ""
    show cereza tired
    ""
    show cereza unimpressed
    ""
    show june angry at right
    ""
    show june confused
    ""
    show june disbelief
    ""
    show june embarrassed
    ""
    show june grin
    ""
    show june happy
    ""
    show june hurt
    ""
    show june normal
    ""
    show june pissed
    ""
    show june sad
    ""
    show june smirk
    ""
    show june surprise
    ""
    show june tease
    ""
    show june tired
    ""
    show june unimpressed
    ""

    show kameron angry at left
    ""  
    show kameron confused
    ""  
    show kameron disbelief
    ""  
    show kameron embarrassed
    ""  
    show kameron grin
    ""  
    show kameron happy
    ""  
    show kameron hurt
    ""  
    show kameron normal
    ""  
    show kameron pissed
    ""  
    show kameron sad
    ""  
    show kameron smirk
    ""  
    show kameron surprise
    ""  
    show kameron tease
    ""  
    show kameron tired
    ""  
    show kameron unimpressed
    ""  

    show rafael angry:
      xalign 0.8
    ""  
    show rafael confused
    ""  
    show rafael crying
    ""  
    show rafael disbelief
    ""  
    show rafael embarrassed
    ""  
    show rafael grin
    ""  
    show rafael happy
    ""  
    show rafael hurt
    ""  
    show rafael pissed
    ""  
    show rafael sad
    ""  
    show rafael smirk
    ""  
    show rafael surprise
    ""  
    show rafael tease
    ""  
    show rafael tired
    ""  
    show rafael unimpressed
    ""  

    hide cereza
    hide june
    hide kameron
    hide rafael
    show cody cry
    ""
    show cody cry big
    ""
    show cody happy
    ""
    show cody normal
    ""
    show cody sad
    ""
    show cody shock
    ""
    show cody smile
    ""
    show cody worry
    ""
    hide cody
    show madison angry
    ""
    show madison happy
    ""
    show madison joke
    ""
    show madison normal
    ""
    show madison sad
    ""
    show madison tease
    ""
    hide madison
    show mona angry
    ""
    show mona embarrased
    ""
    show mona happy
    ""
    show mona normal
    ""
    show mona sad
    ""
    show mona smile
    ""
    hide mona
    show rashied happy
    ""
    show rashied normal
    ""
    show rashied sad
    ""
    show rashied smile
    ""
    show rashied tease
    ""
    show rashied worry
    ""

    $CurrentTimeOfDayName = 'afternoon'
    $CurrentDayName = 'tuesday'
    "Tuesday Afternoon"
  
    $CurrentTimeOfDayName = 'evening'
    $CurrentDayName = 'sunday'
    "Sunday Evening"
    menu:
      "Ready to Quit?"
      "Yes":
        pass
      "No, lets go again.":
        jump start
      "No, lets go to day 1.":
        jump lbl_day_1

    return
