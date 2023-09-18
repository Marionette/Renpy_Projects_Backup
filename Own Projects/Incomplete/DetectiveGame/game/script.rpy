# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define l = Character('Lucy', color="#c8ffc8")
define s = Character('B. Bones', color="#c8ffc8")
image bg = "img/map/Map_Background.png"
image loli happy = "img/character/loli.png"
image classroom light = "img/crimescene/classroom/CS_Classroom_background_Light.png"
image classroom dark = "img/crimescene/classroom/CS_Classroom_background_Dark.png"

image hell = "img/bg/hell.png"
image skull happy = "img/character/Skull_Happy.png"
image lucy happy = "img/character/Lucy_Happy.png"
image lucy confused = "img/character/Lucy_Confused.png"
image lucy sad = "img/character/Lucy_Sad.png"
image lucy angry = "img/character/Lucy_Angry.png"
image lucy evilsmile = "img/character/Lucy_EvilSmile.png"
image lucy cry = "img/character/Lucy_Cry.png"


# The game starts here.
label start:
    #scene hell
    l "So let me get this straight."
    show lucy confused:
      xalign 0.7
      yalign 1.0
    show skull happy:
      xalign 0.3
      yalign 1.0
    l "My father has, for all intents and purposes, banished me from the palace."
    s "Pretty much."
    l "And taken away my right to be the heir."
    s "To be fair you were already 6th in line so..."
    l "And now, for some reason, I have to solve 666 mysteries in order to prove myself worthy to ascend the throne after him."
    s "More or less, Yeah."
    l "..."
    s "..."
    l "...why?"
    s "Why?"
    l "Why."
    s "Why what?"
    l "Why everything. Why is he doing this? Why am i banished? Why does solving mysteries prove anything?"
    s "Who ever knows what goes through the head of the boss?"
    l "..."
    s "..."
    l "You know more than you're letting on."
    s "Maybe..."
    l "Tell me."
    s "I'm not allowed."
    l "Tell me now or so help me..."
    s "I-I can't!"
    #cg dipped in lava
    s "AHH! All I can tell you is this, each of your siblings were given a similar task. Similar but different."
    l "Different?"
    s "Yes, but I-I can't say any more."
    l "Hmm...ok, but I have one last question."
    s "Y-Yes?"
    l "Why 666?"
    s "Huh?"
    l "Why that number? Why do I have to solve six hundred and sixy six mysteries?"
    s "Isn't it obvious? "
    l "Wha...?"
    s "Because its waaay cooler than other numbers."
    l "Are you serious?"
    s "The boss certainly thought so."
    l "...Idiots."
    
    

    $DemonEye = False
    scene bg
    show lucy happy at right
    l "Lets explore the city."
    call screen Map_City
    
    $res = _return
    
    if (res=="Apartment"): 
        call lbl_Apartment    
    if (res=="Disco"): 
        call lbl_Disco
    if (res=="School"): 
        call lbl_School
    if (res=="Shrine"): 
        call lbl_Shrine
    if (res=="Station"): 
        call lbl_Station
    if (res=="TVStation"): 
        call lbl_TVStation
        
    menu:
        "Try somewhere else?"
        "Yes, I might've missed something!":
            jump start
        "No, I think we are finished here.":
            pass
    
    l "I guess thats the end of that then."
    
    return

    
screen Map_City:
    add "img/map/Map_Background.png"
    imagebutton auto "img/map/Map_Apartment_%s.png"  xpos 0 ypos 0 focus_mask True action Return("Apartment")
    imagebutton auto "img/map/Map_Disco_%s.png"  xpos 0 ypos 0 focus_mask True action Return("Disco")
    imagebutton auto "img/map/Map_School_%s.png"  xpos 0 ypos 0 focus_mask True action Return("School")
    imagebutton auto "img/map/Map_Shrine_%s.png"  xpos 0 ypos 0 focus_mask True action Return("Shrine")
    imagebutton auto "img/map/Map_Station_%s.png"  xpos 0 ypos 0 focus_mask True action Return("Station")
    imagebutton auto "img/map/Map_TVStation_%s.png"  xpos 0 ypos 0 focus_mask True action Return("TVStation")
    
 

label lbl_Apartment:  
    l "Its just an old {b}Apartment{/b} block. There's not much to see."
    return
    
label lbl_Disco:
    l "Night Fever!"
    l "Er I mean, who cares about an old {b}Disco{/b} hall?"
    return
    
label lbl_School:
    l "I hope none of the teachers see me skulking around the {b}School{/b} like this..."
    l "I feel something comming from this classroom, lets check it out."
    jump lbl_classroom
    return
    
label lbl_Shrine:
    l "Wonder if I have time for a quick prayer at this {b}Shrine{/b}?"
    return
    
label lbl_Station:
    l "There doesn't seem to be any Trains at the {b}Station{/b} at the moment."
    return
    
label lbl_TVStation:
    l "While I'm here at the {b}TV Station{/b}, I wonder if I can convince them to un-cancel my favourite show."
    l "...Probably not."
    return
    
    
    
 
    
screen Crimescene_Classroom_Light:
    add "img/crimescene/classroom/CS_Classroom_background_Light.png"
    imagebutton auto "img/crimescene/classroom/Classroom_Book_%s.png"  xpos 0 ypos 0 focus_mask True action Return("BookL")
    imagebutton auto "img/crimescene/classroom/Classroom_Clock_%s.png"  xpos 0 ypos 0 focus_mask True action Return("Clock")
    imagebutton auto "img/crimescene/classroom/Classroom_Fan_%s.png"  xpos 0 ypos 0 focus_mask True action Return("Fan")
    imagebutton auto "img/crimescene/classroom/Classroom_Globe_%s.png"  xpos 0 ypos 0 focus_mask True action Return("Globe")
    imagebutton auto "img/ui/SkullInterface_%s.png"  xpos 0 ypos 0 focus_mask True action Return("Eye")
    
 
screen Crimescene_Classroom_Dark:
    add "img/crimescene/classroom/CS_Classroom_background_Dark.png"
    imagebutton auto "img/crimescene/classroom/ClassroomDark_Book_%s.png"  xpos 0 ypos 0 focus_mask True action Return("BookD")
    imagebutton auto "img/crimescene/classroom/ClassroomDark_Message_%s.png"  xpos 0 ypos 0 focus_mask True action Return("Message")
    imagebutton auto "img/ui/SkullInterface_%s.png"  xpos 0 ypos 0 focus_mask True action Return("Eye")
    
    
label lbl_classroom:
    if (DemonEye==True):
        scene classroom dark
        l "Lets see what else we can find here..."
        call screen Crimescene_Classroom_Dark
        $res = _return
    else: 
        scene classroom light
        l "Lets see what else we can find here..."
        call screen Crimescene_Classroom_Light
        $res = _return
    
    
    if (res=="BookL"): 
        l "Oh someone left their book behind. Lets see what it says."
        l "..."
        l "Just school notes, how boring."
    if (res=="Clock"): 
        l "Hmm..."
        l "I think the clock has stopped."
    if (res=="Fan"): 
        l "The breeze from this fan is just what i need in this heat."
    if (res=="Globe"): 
        l "Lets spin it, then poke it and see what country we land on."
        l "No? How boring. "
    if (res=="BookD"): 
        l "Whoa. There's something scribbled all over this book."
        l "..."
        l "It just says 'KILL' over and over, and in red too."
        l "How creepy."
    if (res=="Message"): 
        l "D-Don't be scared."
        l "I-I'm sure its just one of the kids playing a p-prank."
        l "M-Maybe we should get out of here though, just in case?"
        menu:
            "Leave?"
            "Yes lets go.":
                jump start
            "No, we should stay.":
                pass
            
    if (res=="Eye"): 
        s "Do you want to leave yet? Or look at it differently?"
        menu:
          "Do you want to leave yet? Or look at it differently?"
          "Leave":
            return
          "Look Differently":
            pass
        if (DemonEye==True):
            $DemonEye=False
            l "Ok then, Back to Normalcy."
            jump lbl_classroom
        if (DemonEye==False):
            $DemonEye=True
            l "Lets see what this place Really looks like."
            jump lbl_classroom
    
    jump lbl_classroom
            
            
            
            