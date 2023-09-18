
# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
#--------------------------------------------------------------------------------------------------
# The game starts here.
label start:
    #set variable defaults
    $DemonEye = False
    
    #start scene
    scene bg white
    show Eileen 
    e "Hello there~"
    e "This is Marionettes feature demo VN application!"
    hide Eileen
    
    menu:
      e "So what do you want to do?"
      "Colour Test":
        jump lbl_colorTest
      "'3D' Camera Test":
        jump lbl_3DCamTest
      "webm test":
        show bg black
        show kid
        show sunrays movie
        "hows that?"
      "Glitch text Test":
        jump lbl_glitchTest
      "E-mote Test":
        jump lbl_emoteTest
      "Animated Background Test":
        jump lbl_backgroundAnimationTest
      "Map Test":
        jump lbl_mapTest
      "Hidden Picture Test":
        jump lbl_hiddenPicTest
      "Investigation Scene Test":
        jump lbl_investigationTest
      "System Voice Test":
        "The purpose of this feature was to allow for voiced menu commands that could be switched to use the voices of different characters"
        e "You'll have to go to the Preferences menu to test that one..."
        e "Just click on any of the options buttons to hear the voice clip for that option. Then use the supplied buttons to change the selected voice and try again."
        e "Easy-peasy~"
      "Nothing":
        pass

    show Eileen 
    e "All done? \nGoodbye then~"
    return

    
#--------------------------------------------------------------------------------------------------
label lbl_colorTest:
  $ temp_color = "#ff0000"
  $ colorString = "{color=%s}" %temp_color
  "Life is better with [colorString]colors{/color}!"
  $ temp_color = "#ffffff"
  $ colorString = "{color=" + temp_color + "}"
  "Life is better with [colorString]colors{/color}!"

  $ temp_color = "#123456"
  "Life is better with {color=[temp_color]}colors{/color}!"
  
  return
label lbl_emoteTest:
    scene bg white
    "The point of this feature is to showcase the implementation of animated sprites created using the software package E-mote (emofuri) within ren'py"
    show Eileen emote
    e "{i}*Boooooing~*{/i}"
    hide Eileen
    show Eileen emote at left
    e "{i}*Boooooing~*{/i}"
    hide Eileen
    show Eileen emote at right
    e "{i}*Boooooing~*{/i}"
    hide Eileen
    show Eileen emote
    e "{i}Boooooing~*{/i} \nErm...What are you staring at?"
    
    return

    
#--------------------------------------------------------------------------------------------------

label lbl_backgroundAnimationTest:
    scene bg cabin animated
    e "Well, isn't this cozy?"
    e "Glad im not out in that snow."
    
    return
    

    
#--------------------------------------------------------------------------------------------------

label lbl_mapTest:
    scene bg white
    "The point of this feature is to showcase a map style click-able interface for travelling between various locations."
    jump lbl_mapTest_City
    
label lbl_mapTest_City:

    scene bg citymap
    show kid at right
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
        l "Try somewhere else?"
        "Yes, I might've missed something!":
            jump lbl_mapTest_City
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
    
    
#--------------------------------------------------------------------------------------------------
    
label lbl_hiddenPicTest:
    "The point of this feature is to showcase the possibility of having 'hidden objects' within a scene that wouldn't affect the game unless clicked on and if not clicked on the game would continue anyways."
    show kid at right
    l "I feel something comming from this classroom, lets check it out."
    scene bg classroom
    show screen Classroom
    l "Did you find anything yet?"
    l "Did you try Clicking the clock?"
    l "Did you try Clicking the book?"
    l "Did you try Clicking the fan?"
    l "Did you try Clicking the globe?"
    l "Good job~"
    return
    

screen Classroom:
    #add "img/bg/classroom/CS_Classroom_background_Light.png"
    imagebutton auto "img/bg/classroom/Classroom_Book_%s.png"  xpos 0 ypos 0 focus_mask True action ShowMenu("itemScreen_book")
    imagebutton auto "img/bg/classroom/Classroom_Clock_%s.png"  xpos 0 ypos 0 focus_mask True action ShowMenu("itemScreen_clock")
    imagebutton auto "img/bg/classroom/Classroom_Fan_%s.png"  xpos 0 ypos 0 focus_mask True action ShowMenu("itemScreen_fan")
    imagebutton auto "img/bg/classroom/Classroom_Globe_%s.png"  xpos 0 ypos 0 focus_mask True action ShowMenu("itemScreen_globe")
    
    
screen itemScreen_book:
    add Solid("#FFFFFF")
    imagebutton auto "img/bg/classroom/Classroom_Book_%s.png"  xpos 0 ypos 0 focus_mask True action Return()
screen itemScreen_clock:
    add Solid("#FFFFFF")
    imagebutton auto "img/bg/classroom/Classroom_Clock_%s.png"  xpos 0 ypos 0 focus_mask True action Return()
screen itemScreen_fan:
    add Solid("#FFFFFF")
    imagebutton auto "img/bg/classroom/Classroom_Fan_%s.png"  xpos 0 ypos 0 focus_mask True action Return()
screen itemScreen_globe:
    add Solid("#FFFFFF")
    imagebutton auto "img/bg/classroom/Classroom_Globe_%s.png"  xpos 0 ypos 0 focus_mask True action Return()

    
    
#--------------------------------------------------------------------------------------------------
label lbl_glitchTest:
    "The point of this was to showcase the possiblity of having some 'glitchy' text for an otherworldy effect."
    "To̷ ́i̕nv̡o̴k̡e͟ ̡t͞he h̷iv̷e-̷m̀in͘d ̢re̢pr͟és̷ȩn͟t͞i̡ng ͝chàos͠."
    "To͝ i͜ņ̵͞v͞o̧k̶̀e t҉͡h́e҉́ ̴hi̵͘v͏e-̢̕m̨͏i̷̛͏n͏̡d͏͘ ̛r̵èp͜͟ŕe̴͝sentį͢ng̷̡͢ ̢͞c̡̕͟h̕a҉͝o͏̡s͘."
    "̯̦W͙̟͍͉̕į̼͚̝t̤̰͎̞͎̼̥ḫ̳͔͎͞ ̳̙ͅo̺u̼͉̩̦͟t̙̭̜̰͓͕̼̀ ̴̣o͏̪͎̝̬̘ŗ̪̮̠d̪̩̫͜e̴̲̺̳̻̜r͈̺̫̠͕̮̪͜.̟̖̳"
    "Ṭ͉̥͎͍h̷͙̟̯̞͎ḙ̤͖͈͚̠ ̫̥N͏̩̦͔͓̦̥̫ẹ̢̭̻̻͎z͏̹̠̹̖p̰̭̼͙̗̱̞eŗ̣̙d҉̥̺̮ͅͅi̳͈͕͕͖͔a̬̬̘n͙ ͏̻̠̞͈̘̘h̨͉̙̤̣͚i̟̲̫̦̯͎͍͝v̛̻e͕̫-͡m͏̪͓̙̘̦͕i̥n̖̙d̺̜͙̼̙́ ̦̯̙̲o͏͚̤̰͇f̧̙͚ ̼̭͓͔͎͟c̰̭̭̙̩͈̮͞h҉̺̳̫̹̻̥̯a̸o̸̹s͕̞.̧͚̩̜͓ͅ ̥̭̗̠̼̤Z̀à͚̲̳͍̳l̜̦̰̬̥̰̕go̝͚̼̦̱͍.̴̱̤̖̣"
    "̛H̫e̤̺͉̣͎ͅ ̩͕̣ͅw̸̙h̟͉̖̘̠͖̥o͍̳ ̬͢W̤̤̝̱̮̭̳a̷̮̘͉̲̗̺i̡̟̲̝͚̞t͖̺̯s͈̹ ͎̻̜B͖͇̗͖͍e̳̗̮͕͚h̵̙͍i͏n̜̼̗͎ḏ͉̹͕ ̶̫̻͓T̰̫̫̗̯̳̦͜h̢̞̥̠̼͈e̛̠̘̜͈̮͍̠ ̯W͏̺̯̞̲̲̮a̗̼̮͔ll̼̼̪̤͖̺.͇̟̠"
    "̥̩Z̞A̹͞L̷͎G̞̩̬̣̻̹͔͘O̡̲!̜̭̲̭͝"
  
    return
  
    
#--------------------------------------------------------------------------------------------------
  
label lbl_3DCamTest:
    "The point of this feature is to showcase the usage of the '3D' camera in game. Creates a parallax scrolling effect when moving the camera around. \nAn implementation of the camera code provided by akakyouryuu."
    "Testing..."
    $ layer_move("m", 1800)
    $ layer_move("f", 1280)
    $ layer_move("b", 2200)
    
    
    $ camera_move(-260, -1350, 1240)
    scene bg cabin onlayer b at truecenter, basicfade:
        subpixel True
        zoom 1.5
        easein 1.0 yoffset -10
    show teach onlayer m :#at right, basicfade:
        xpos 300
        xzoom -1
    show kid onlayer m :#at left, basicfade:
        xpos 700
        
    $ camera_move(1410, 0.0, 0, 0, 6, subpixel=True)# warper='power_in_time_warp_real',
    
    "Testing..."
    $ camera_move(410, 0.0, 0, 0, 6, subpixel=True)# warper='power_in_time_warp_real',
    "Testing..."
    $ camera_move(1410, 0.0, 0, 0, 6, subpixel=True)#, warper='power_in_time_warp_real')
    "Testing..."
    $ camera_move(110, -340.0, 0, 0, 3, subpixel=True)#, warper='power_in_time_warp_real')
    "Testing..."
    $ camera_move(800, -340.0, 800, 0, 6, subpixel=True)#, warper='power_in_time_warp_real')
    "Testing..."
    $ camera_move(700, -540.0, 800, 0, 2, subpixel=True)#, warper='power_in_time_warp_real')
    "Testing..."
    
    e "I guess thats the end of that then."
    
    return
    
#--------------------------------------------------------------------------------------------------
    
screen Crimescene_Classroom_Light:
    add "img/bg/crimescene/classroom/CS_Classroom_background_Light.png"
    imagebutton auto "img/bg/crimescene/classroom/Classroom_Book_%s.png"  xpos 0 ypos 0 focus_mask True action Return("BookL")
    imagebutton auto "img/bg/crimescene/classroom/Classroom_Clock_%s.png"  xpos 0 ypos 0 focus_mask True action Return("Clock")
    imagebutton auto "img/bg/crimescene/classroom/Classroom_Fan_%s.png"  xpos 0 ypos 0 focus_mask True action Return("Fan")
    imagebutton auto "img/bg/crimescene/classroom/Classroom_Globe_%s.png"  xpos 0 ypos 0 focus_mask True action Return("Globe")
    imagebutton auto "img/gui/SkullInterface_%s.png"  xpos 0 ypos 0 focus_mask True action Return("Eye")
    
 
screen Crimescene_Classroom_Dark:
    add "img/bg/crimescene/classroom/CS_Classroom_background_Dark.png"
    imagebutton auto "img/bg/crimescene/classroom/ClassroomDark_Book_%s.png"  xpos 0 ypos 0 focus_mask True action Return("BookD")
    imagebutton auto "img/bg/crimescene/classroom/ClassroomDark_Message_%s.png"  xpos 0 ypos 0 focus_mask True action Return("Message")
    imagebutton auto "img/gui/SkullInterface_%s.png"  xpos 0 ypos 0 focus_mask True action Return("Eye")
    
label lbl_investigationTest:
    "The point of this feature is to showcase a point and click style scene where the player can click freely to interact with the scene without the story continuing on."
    jump lbl_investigation_Classroom
    
label lbl_investigation_Classroom:
    if (DemonEye==True):
        scene classroom dark
        show kid at right
        l "Lets see what else we can find here..."
        call screen Crimescene_Classroom_Dark
        $res = _return
    else: 
        scene classroom light
        show kid at right
        l "Lets see what else we can find here..."
        call screen Crimescene_Classroom_Light
        $res = _return
    
    show kid at right
    
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
        hide kid
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
            jump lbl_investigation_Classroom
        if (DemonEye==False):
            $DemonEye=True
            l "Lets see what this place Really looks like."
            jump lbl_investigation_Classroom
    
    jump lbl_investigation_Classroom
    
#--------------------------------------------------------------------------------------------------
            
            
            
            