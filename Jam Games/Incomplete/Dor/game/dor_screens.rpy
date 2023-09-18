# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"
                xpos 65
                ypos 35

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    add "img/ui/textbox.png"  yalign 1.0
    $i = 0
    #window:
            #style "menu_window"
        #xalign -0.2
        #yalign 0.9

        #vbox:
            #style "menu"
            #spacing 2

    for caption, action, chosen in items:

        $i+= 1
        if action:
            $yalignpos = 0.8 + (0.05*i)
            imagebutton auto "img/ui/choice_%s.png" xpos 60 yalign yalignpos action action
            $captionText = "{font=assets/texgyrecursor-r.otf}{size=25}{color=#c8ffff}[caption]{/color}{/font}{/size}"
            text captionText xpos 100 yalign yalignpos-0.005

            #button:
            #    action action
            #    style "menu_choice_button"
            #
            #    $captionText = "{font=assets/texgyrecursor-r.otf}{size=25}[caption]{/font}{/size}"
            #    text captionText style "menu_choice"

        else:
            text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)
        background None


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu
    #add "img/gui/bgs/splash.png"
    imagemap:
        auto "img/ui/mainmenu/main menu_%s.png"        
        hotspot (800, 145, 300, 80) action Start()
        hotspot (800, 225, 300, 80) action ShowMenu("load")
        hotspot (800, 305, 300, 80) action ShowMenu("preferences")
        hotspot (800, 385, 300, 80) action Help()
        #hotspot (800, 465, 300, 80) action ShowMenu("extras")
        hotspot (800, 545, 300, 80) action Quit(confirm=False)




init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    imagemap:
        auto "img/ui/nav_%s.png" alpha False         
        hotspot (320,  75, 200, 120)  action Return()   
        hotspot (530,  75, 200, 120)  action MainMenu()   
        hotspot (740,  75, 200, 120)  action Quit()
        hotspot (135, 555, 200, 120)  action ShowMenu("save")   
        hotspot (350, 555, 200, 120)  action ShowMenu("load")   
        hotspot (555, 555, 200, 120)  action ShowMenu("preferences")   
        hotspot (765, 555, 200, 120)  action Help()


init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

init python:
    config.thumbnail_width = 225
    config.thumbnail_height = 127
    
screen file_picker():

    imagemap:
        auto "img/ui/save/save_%s.png" alpha False        
        hotspot (175, 430, 265, 125)  action FilePage("auto") 
        hotspot (580, 440, 120, 50)  action FilePagePrevious()
        hotspot (780, 440, 120, 50)  action FilePageNext()
        
    $ columns = 2
    $ rows = 1
    for i in range(1, columns * rows + 1):
      $index = i
      $jpos = 440*(i-1)
      imagebutton auto "img/ui/save/savebox_%s.png" xpos 260+jpos ypos 210 focus_mask None action FileAction(i)
      add FileScreenshot(i) xpos 330+jpos ypos 250 
      $ file_name = FileSlotName(i, columns * rows)
      $ file_time = FileTime(i, empty=_("Empty Slot."))
      $ save_name = FileSaveName(i) 
      text "{size=25}[file_name]. [file_time!t]\n\n[save_name!t]{/size}"  xpos 330+jpos ypos 380



screen save():

    # This ensures that any other menu screen is replaced.
    tag menu
    add "img/ui/save/save_groundA.png"

    use file_picker
    use navigation

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu
    add "img/ui/save/load_ground.png"

    use file_picker
    use navigation

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():


    tag menu
    # Include the navigation.
    imagemap:
        auto "img/ui/pref/pref_%s.png" alpha False         
        #621
        hotspot (510, 200, 120, 28)  action Preference("display", "window")
        hotspot (430, 232, 220, 28)  action Preference("display", "fullscreen")
        hotspot (455, 290,  70, 35)  action Preference("transitions", "all")
        hotspot (577, 290,  50, 35)  action Preference("transitions", "none")
        hotspot (425, 360,  50, 35)  action Preference("skip", "all")
        hotspot (545, 360,  80, 35)  action Preference("skip", "seen")
        hotspot (400, 475, 220, 29)  action Preference("after choices", "stop")
        hotspot (400, 505, 220, 28)  action Preference("after choices", "skip") 
        #hotspot (990, 340, 150, 25)  action Skip()
        
    bar:
      style_group "pref"
      xpos 695
      ypos 235
      value Preference("text speed")
    bar:
      style_group "pref"
      xpos 695
      ypos 315
      value Preference("auto-forward time")
      
    bar:
      style_group "pref"
      xpos 695
      ypos 395
      value  Preference("music volume")
    bar:
      style_group "pref"
      xpos 695
      ypos 475
      value Preference("sound volume")
      
    use navigation

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xalign 0
        yalign 0
        left_bar  "img/ui/pref/bar_full.png"
        right_bar "img/ui/pref/bar_empty.png"
        thumb "img/ui/pref/bar_thumb.png"
        xmaximum 344
        ymaximum 20 

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True
    add "img/ui/yesno/80blk.png"
    imagemap:
        ypos 180
        auto "img/ui/yesno/yesno_%s.png" #alpha False       
        hotspot (400, 200, 75, 45) action yes_action
        hotspot (900, 200, 75, 45) action no_action

    
    $sz_message = "{font=assets/mensch.ttf}{size=40}{color=0033CC}[message]{/color}{/size}{/font}"
    label _(sz_message):
        xalign 0.55
        yalign 0.45

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    #imagemap:
    #    auto "img/ui/quick_%s.png" alpha False       
    #    hotspot (900, 400, 50, 45) action ShowMenu('preferences')
    #    hotspot (960, 400, 50, 45) action Rollback()
    #    hotspot (1020, 400, 50, 45) action Skip()
    #    hotspot (1080, 400, 50, 45) action Preference("auto-forward", "True")
    #    hotspot (1125, 400, 50, 45) action Preference("auto-forward", "False")
    #    hotspot (1175, 400, 50, 45) action ShowMenu('preferences')
    # Add an in-game quick menu.
    hbox:
        style_group "quick"
    
        xalign 1.0
        yalign 0.7
    
       #textbutton _("{size=20}{font=assets/texgyrecursor-r.otf}Back{/font}{/size}") action Rollback()
        textbutton _("{size=20}{font=assets/texgyrecursor-r.otf}Q.Save{/font}{/size}") action QuickSave()
        textbutton _("{size=20}{font=assets/texgyrecursor-r.otf}Q.Load{/font}{/size}") action QuickLoad()
        textbutton _("{size=20}{font=assets/texgyrecursor-r.otf}Skip{/font}{/size}") action Skip()
       #textbutton _("{size=20}{font=assets/texgyrecursor-r.otf}F.Skip{/font}{/size}") action Skip(fast=True, confirm=True)
        textbutton _("{size=20}{font=assets/texgyrecursor-r.otf}Auto{/font}{/size}") action Preference("auto-forward", "toggle")
        textbutton _("{size=20}{font=assets/texgyrecursor-r.otf}Prefs{/font}{/size}") action ShowMenu('preferences')
        textbutton _("{size=20}{font=assets/texgyrecursor-r.otf}Save{/font}{/size}") action ShowMenu('save')
        textbutton _("{size=20}{font=assets/texgyrecursor-r.otf}Load{/font}{/size}") action ShowMenu('load')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"


screen extras():
    tag menu
    use extra_nav

screen extra_nav():

    imagemap:
        auto "img/ui/extra/enav_%s.png" alpha False         
        hotspot (35, 150, 300, 160)  action ShowMenu("extra_end")   
        hotspot (35, 225, 300, 160)  action ShowMenu("extra_gall")   
        hotspot (35, 300, 300, 160)  action ShowMenu("extra_juke")   
        hotspot (35, 380, 300, 160)  action ShowMenu("extra_note") 
        hotspot (35, 630, 300, 160)  action Return()    
        
screen extra_end():
    tag menu
    use extra_nav
        
screen extra_gall():
    tag menu
    use extra_nav
    imagemap:
        auto "img/ui/extra/gallery_%s.png" alpha False        
        hotspot (580, 440, 120, 50)  action FilePagePrevious()
        hotspot (780, 440, 120, 50)  action FilePageNext()
        
    $ columns = 3
    $ rows = 2
    for i in range(1, columns * rows + 1):
      $index = i
      $jpos = 250*((i-1)/rows)
      $ipos = 165*(i%rows)
      imagebutton auto "img/ui/extra/galbox_%s.png" xpos 535+jpos ypos 150+ipos focus_mask None action FileAction(i)
        
screen extra_juke():
    tag menu
    use extra_nav
        
screen extra_note():
    tag menu
    use extra_nav
    