# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.

init:
    define p = Character('Pandora', color="#c8ffc8") #Pandora Bloodworth

    image loli happy = "img/sprite/loliDemon.png"
    image bg black = Solid("#000000")

    image bg map = "img/map/Map_idle.png"
    # color (r, g, b, a)
    #MC Team = 00
    $Team00_colour = (255, 255, 0, 155)
    
    #Enemy teams = 01 - 11
    $Team01_colour = (150, 20, 20, 155)
    $Team02_colour = (150, 90, 0, 155)
    $Team03_colour = (30, 150, 0, 155)
    $Team04_colour = (50, 200, 150, 155)
    $Team05_colour = (50, 100, 200, 155)
    $Team06_colour = (70, 50, 200, 155)
    $Team07_colour = (170, 50, 200, 155)
    $Team08_colour = (200, 40, 110, 155)
    $Team09_colour = (100, 100, 100, 155)
    $Team10_colour = (20, 70, 20, 155)
    $Team11_colour = (200, 70, 100, 155)
    
    $CountryA_colour = Team01_colour
    $CountryB_colour = Team01_colour
    $CountryC_colour = Team02_colour
    $CountryD_colour = Team02_colour
    $CountryE_colour = Team03_colour
    $CountryF_colour = Team03_colour
    $CountryG_colour = Team01_colour
    $CountryH_colour = Team04_colour
    $CountryI_colour = Team04_colour
    $CountryJ_colour = Team06_colour
    $CountryK_colour = Team05_colour
    $CountryL_colour = Team05_colour
    $CountryM_colour = Team06_colour
    $CountryN_colour = Team07_colour
    $CountryO_colour = Team11_colour
    $CountryP_colour = Team10_colour
    $CountryQ_colour = Team07_colour
    $CountryR_colour = Team09_colour
    $CountryS_colour = Team08_colour
    $CountryT_colour = Team00_colour
    
    $CountryList_Name = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]    
    $CountryList_Colours = [CountryA_colour,
                            CountryB_colour,
                            CountryC_colour,
                            CountryD_colour,
                            CountryE_colour,
                            CountryF_colour,
                            CountryG_colour,
                            CountryH_colour,
                            CountryI_colour,
                            CountryJ_colour,
                            CountryK_colour,
                            CountryL_colour,
                            CountryM_colour,
                            CountryN_colour,
                            CountryO_colour,
                            CountryP_colour,
                            CountryQ_colour,
                            CountryR_colour,
                            CountryS_colour,
                            CountryT_colour]
    $CountrySelected = 1
    
    
screen demo_imagemap:
    #imagemap:
        #auto "img/map/Map_%s.png"
        #imagebutton auto "img/gui/MainMenu_Play_%s.png"
    #
    #    hotspot (200, 200, 178, 178) action Return("swimming")
    #    hotspot (340, 200, 178, 178) action Return("science")
    #    hotspot (452, 340, 178, 178) action Return("art")
    #    hotspot (200, 416, 178, 178) action Return("go home")
    #image map_countryA_rc im.Recolor("img/map/Map_CountryA.png", 0, 255, 255, 255)
    #tag menu 
    add "img/map/Map_ground.png"
    imagebutton auto "img/map/Map_CountryA_%s.png" idle im.Recolor("img/map/Map_CountryA_idle.png", CountryList_Colours[ 0][0], CountryList_Colours[ 0][1], CountryList_Colours[ 0][2], CountryList_Colours[ 0][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected",  0), Return("2")]
    imagebutton auto "img/map/Map_CountryB_%s.png" idle im.Recolor("img/map/Map_CountryB_idle.png", CountryList_Colours[ 1][0], CountryList_Colours[ 1][1], CountryList_Colours[ 1][2], CountryList_Colours[ 1][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected",  1), Return("2")]
    imagebutton auto "img/map/Map_CountryC_%s.png" idle im.Recolor("img/map/Map_CountryC_idle.png", CountryList_Colours[ 2][0], CountryList_Colours[ 2][1], CountryList_Colours[ 2][2], CountryList_Colours[ 2][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected",  2), Return("2")]
    imagebutton auto "img/map/Map_CountryD_%s.png" idle im.Recolor("img/map/Map_CountryD_idle.png", CountryList_Colours[ 3][0], CountryList_Colours[ 3][1], CountryList_Colours[ 3][2], CountryList_Colours[ 3][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected",  3), Return("2")]
    imagebutton auto "img/map/Map_CountryE_%s.png" idle im.Recolor("img/map/Map_CountryE_idle.png", CountryList_Colours[ 4][0], CountryList_Colours[ 4][1], CountryList_Colours[ 4][2], CountryList_Colours[ 4][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected",  4), Return("2")]
    imagebutton auto "img/map/Map_CountryF_%s.png" idle im.Recolor("img/map/Map_CountryF_idle.png", CountryList_Colours[ 5][0], CountryList_Colours[ 5][1], CountryList_Colours[ 5][2], CountryList_Colours[ 5][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected",  5), Return("2")]
    imagebutton auto "img/map/Map_CountryG_%s.png" idle im.Recolor("img/map/Map_CountryG_idle.png", CountryList_Colours[ 6][0], CountryList_Colours[ 6][1], CountryList_Colours[ 6][2], CountryList_Colours[ 6][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected",  6), Return("2")]
    imagebutton auto "img/map/Map_CountryH_%s.png" idle im.Recolor("img/map/Map_CountryH_idle.png", CountryList_Colours[ 7][0], CountryList_Colours[ 7][1], CountryList_Colours[ 7][2], CountryList_Colours[ 7][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected",  7), Return("2")]
    imagebutton auto "img/map/Map_CountryI_%s.png" idle im.Recolor("img/map/Map_CountryI_idle.png", CountryList_Colours[ 8][0], CountryList_Colours[ 8][1], CountryList_Colours[ 8][2], CountryList_Colours[ 8][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected",  8), Return("2")]
    imagebutton auto "img/map/Map_CountryJ_%s.png" idle im.Recolor("img/map/Map_CountryJ_idle.png", CountryList_Colours[ 9][0], CountryList_Colours[ 9][1], CountryList_Colours[ 9][2], CountryList_Colours[ 9][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected",  9), Return("2")]
    imagebutton auto "img/map/Map_CountryK_%s.png" idle im.Recolor("img/map/Map_CountryK_idle.png", CountryList_Colours[10][0], CountryList_Colours[10][1], CountryList_Colours[10][2], CountryList_Colours[10][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected", 10), Return("2")]
    imagebutton auto "img/map/Map_CountryL_%s.png" idle im.Recolor("img/map/Map_CountryL_idle.png", CountryList_Colours[11][0], CountryList_Colours[11][1], CountryList_Colours[11][2], CountryList_Colours[11][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected", 11), Return("2")]
    imagebutton auto "img/map/Map_CountryM_%s.png" idle im.Recolor("img/map/Map_CountryM_idle.png", CountryList_Colours[12][0], CountryList_Colours[12][1], CountryList_Colours[12][2], CountryList_Colours[12][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected", 12), Return("2")]
    imagebutton auto "img/map/Map_CountryN_%s.png" idle im.Recolor("img/map/Map_CountryN_idle.png", CountryList_Colours[13][0], CountryList_Colours[13][1], CountryList_Colours[13][2], CountryList_Colours[13][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected", 13), Return("2")]
    imagebutton auto "img/map/Map_CountryO_%s.png" idle im.Recolor("img/map/Map_CountryO_idle.png", CountryList_Colours[14][0], CountryList_Colours[14][1], CountryList_Colours[14][2], CountryList_Colours[14][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected", 14), Return("2")]
    imagebutton auto "img/map/Map_CountryP_%s.png" idle im.Recolor("img/map/Map_CountryP_idle.png", CountryList_Colours[15][0], CountryList_Colours[15][1], CountryList_Colours[15][2], CountryList_Colours[15][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected", 15), Return("2")]
    imagebutton auto "img/map/Map_CountryQ_%s.png" idle im.Recolor("img/map/Map_CountryQ_idle.png", CountryList_Colours[16][0], CountryList_Colours[16][1], CountryList_Colours[16][2], CountryList_Colours[16][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected", 16), Return("2")]
    imagebutton auto "img/map/Map_CountryR_%s.png" idle im.Recolor("img/map/Map_CountryR_idle.png", CountryList_Colours[17][0], CountryList_Colours[17][1], CountryList_Colours[17][2], CountryList_Colours[17][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected", 17), Return("2")]
    imagebutton auto "img/map/Map_CountryS_%s.png" idle im.Recolor("img/map/Map_CountryS_idle.png", CountryList_Colours[18][0], CountryList_Colours[18][1], CountryList_Colours[18][2], CountryList_Colours[18][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected", 18), Return("2")]
    imagebutton auto "img/map/Map_CountryT_%s.png" idle im.Recolor("img/map/Map_CountryT_idle.png", CountryList_Colours[19][0], CountryList_Colours[19][1], CountryList_Colours[19][2], CountryList_Colours[19][3]) xpos 0 ypos 0 focus_mask True action [SetVariable("CountrySelected", 19), Return("2")]
    
    
    #imagebutton auto "img/gui/MainMenu_Play_%s.png" xpos 0 ypos 0 focus_mask True action Jump("start")
        #textbutton _("Start Game") action Start()
        #textbutton _("Load Game") action ShowMenu("load")
        #textbutton _("Preferences") action ShowMenu("preferences")
        #textbutton _("Help") action Help()
        #textbutton _("Quit") action Quit(confirm=False)
    

# The game starts here.
label start:
    scene bg map
    show loli happy at right
    p "You've created a new Ren'Py game."

    p "Once you add a story, pictures, and music, you can release it to the world!"

    p "This looks like a quaint little country. Why not start our world conquest here?"
    
    
label map_screen:
    #window hide None
    call screen demo_imagemap
    $res = _return
    $name = CountryList_Name[CountrySelected]
    $oldCol = CountryList_Colours[CountrySelected]
    #window show None
    "You just conquered Country [name!t]"
    
    $CountryList_Colours[CountrySelected] = Team00_colour
    $NewCol = CountryList_Colours[CountrySelected]
    "Country [name!t] colour was [oldCol[0]], it is now [NewCol[0]]"
    
    menu:
        "Keep going?"
        "Yes, For Conquest!":
            jump map_screen
        "Nah, im out.":
            pass
    
    p "Well that was easy."
    
    return
