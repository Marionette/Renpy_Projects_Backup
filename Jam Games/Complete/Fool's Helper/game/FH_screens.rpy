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

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear
        size 16
        yalign 0.6

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.5)
        xmaximum int(config.screen_width * 0.5)
        #xminimum int(364)
        #xmaximum int(364)
        yminimum int(58)
        ymaximum int(58)
        background Frame("images/ui/choice/InGameChoice_idle.png", 5, 5)
        hover_background Frame("images/ui/choice/InGameChoice_hover.png", 5, 5)
        top_padding 5
        bottom_padding 5
        left_padding 58
        
    style nvl_menu_window is default

    style nvl_menu_choice is button_text:
        clear
        size 16
        #yalign 0.5
    style nvl_menu_choice_button is button:
        #xminimum int(config.screen_width * 0.5)
        #xmaximum int(config.screen_width * 0.5)
        xminimum int(564)
        xmaximum int(564)
        yminimum int(48)
        ymaximum int(48)
        background Frame("images/ui/choice/InGameChoice_idle.png", 5, 5)
        hover_background Frame("images/ui/choice/InGameChoice_hover.png", 5, 5)
        #top_padding 5
        #bottom_padding 5
        #left_padding 58


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

    #add "images/ui/textbox/NVL.png"
    window:
        #style "nvl_window"
        area (180,65,440,460)
        background None

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has vbox:
                    spacing 10

                if who is not None:
                    text who id who_id #xalign 0.5

                text what id what_id

        # Display a menu, if given.
    window:
        area (0,300,840,200)
        background None
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

    #use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    
    # This ensures that any other menu screen is replaced.
    tag menu
        
    imagemap:
        auto "images/ui/main/mm_%s.png"        
        hotspot (295, 260, 205, 55) action Start()
        hotspot (295, 317, 205, 55) action ShowMenu("load")
        hotspot (295, 374, 205, 55) action ShowMenu("preferences")
        hotspot (295, 429, 205, 55) action ShowMenu("gallery_menu")
        hotspot (295, 487, 205, 55) action Quit(confirm=False)
        
        hotspot (738, 10, 55, 70) action Help()

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
        #xpos 60
        #ypos 120
        auto "images/ui/menu/GameMenuButtons_%s.png"        
        hotspot (25, 60, 200, 75) action MainMenu()
        hotspot (25, 142, 200, 82) action ShowMenu("save")
        hotspot (25, 222, 200, 75) action ShowMenu("load")
        hotspot (25, 306, 200, 75) action ShowMenu("preferences")
        hotspot (25, 390, 200, 75) action Return()
        hotspot (25, 470, 200, 75) action Quit()

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

screen file_picker():

    imagemap:
        #xpos 60
        #ypos 120
        auto "images/ui/menu/SaveMenu_%s.png"        
        hotspot (275, 108, 43, 40) action FilePagePrevious()
        hotspot (320, 108, 43, 40) action FilePage("auto")
        hotspot (362, 108, 43, 40) action FilePage("quick")
        hotspot (405, 108, 43, 40) action FilePage(1)
        hotspot (450, 108, 43, 40) action FilePage(2)
        hotspot (492, 108, 43, 40) action FilePage(3)
        hotspot (533, 108, 43, 40) action FilePage(4)
        hotspot (578, 108, 43, 40) action FilePage(5)
        hotspot (621, 108, 43, 40) action FilePage(6)
        hotspot (662, 108, 43, 40) action FilePage(7)
        hotspot (708, 108, 43, 40) action FilePageNext()
        
    $ columns = 2
    $ rows = 2

    # Display a grid of file slots.
    grid columns rows:
        area (265,165,500,385)
        transpose True
        xfill True
        style_group "file_picker"
    
        # Display ten file slots, numbered 1 - 10.
        for i in range(1, columns * rows + 1):
    
          
            # Each file slot is a button.
            button:
                action FileAction(i)
                background "images/ui/menu/savebox_ground.png"
                idle_background "images/ui/menu/savebox_idle.png"
                hover_background "images/ui/menu/savebox_hover.png"
                #xfill True
                xminimum 249
                yminimum 170
    
                has vbox
    
                # Add the screenshot.
                add FileScreenshot(i) xpos 14 ypos 18
    
                $ file_name = FileSlotName(i, columns * rows)
                $ file_time = FileTime(i, empty=_("Empty Slot."))
                $ save_name = FileSaveName(i)
    
                text "[file_name]. [file_time!t]\n[save_name!t]" xpos 5 ypos 35
    
                key "save_delete" action FileDelete(i)
                
                
screen save():

    # This ensures that any other menu screen is replaced.
    tag menu
    add "images/ui/menu/GameMenuBG.png"
    add "images/ui/menu/GameMenuTitle_Save.png"

    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu
    add "images/ui/menu/GameMenuBG.png"
    add "images/ui/menu/GameMenuTitle_Load.png"

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text
    
init python:
    config.thumbnail_width = 196
    config.thumbnail_height = 90

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    add "images/ui/menu/GameMenuBG.png"
    add "images/ui/menu/GameMenuTitle_Preferences.png"
    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 2 1:
        style_group "prefs"
        xfill True
        area (250,100,510,450)

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            #frame:
            #    style_group "pref"
            #    has vbox

                #textbutton _("Joystick...") action Preference("joystick")
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        #vbox:

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5
        background Frame("images/ui/frame.png", 24, 24)
        top_padding 10
        bottom_padding 10
        left_padding 10

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0
        idle_background Frame("images/ui/menu/GameMenuPrefsButton_idle.png", 24, 24)
        hover_background Frame("images/ui/menu/GameMenuPrefsButton_hover.png", 24, 24)
        insensitive_background Frame("images/ui/menu/GameMenuPrefsButton_ground.png", 24, 24)
        selected_idle_background Frame("images/ui/menu/GameMenuPrefsButton_select.png", 24, 24)
        selected_hover_background Frame("images/ui/menu/GameMenuPrefsButton_hover.png", 24, 24)
        top_padding 5
        bottom_padding 5
        left_padding 5

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True
    add "images/ui/menu/menubg.png"
    #window:
    #    style "gm_root"

    frame:
        style_group "yesno"
        background Frame("images/ui/frame.png", 24, 24)

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05
        yalign 0.5

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"
        xalign 1.0
        idle_background Frame("images/ui/menu/GameMenuPrefsButton_idle.png", 24, 24)
        hover_background Frame("images/ui/menu/GameMenuPrefsButton_hover.png", 24, 24)
        insensitive_background Frame("images/ui/menu/GameMenuPrefsButton_ground.png", 24, 24)
        selected_idle_background Frame("images/ui/menu/GameMenuPrefsButton_select.png", 24, 24)
        selected_hover_background Frame("images/ui/menu/GameMenuPrefsButton_hover.png", 24, 24)
        top_padding 5
        bottom_padding 5
        left_padding 15
        right_padding 15

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    #hbox:
    #    style_group "quick"
    #
    #    xalign 1.0
    #    yalign 1.0
    #
    #    textbutton _("Back") action Rollback()
    #    textbutton _("Save") action ShowMenu('save')
    #    textbutton _("Q.Save") action QuickSave()
    #    textbutton _("Q.Load") action QuickLoad()
    #    textbutton _("Skip") action Skip()
    #    textbutton _("F.Skip") action Skip(fast=True, confirm=True)
    #    textbutton _("Auto") action Preference("auto-forward", "toggle")
    #    textbutton _("Prefs") action ShowMenu('preferences')
        
        
    imagemap:
        #xpos 60
        #ypos 120
        auto "images/ui/textbox/textbox_%s.png"        
        hotspot (275, 528, 50, 65) action Rollback()
        hotspot (330, 528, 50, 65) action Preference("auto-forward", "toggle")
        hotspot (385, 528, 50, 65) action Skip()
        hotspot (440, 528, 50, 65) action Skip(fast=True, confirm=True)
        hotspot (495, 528, 50, 65) action QuickSave()
        hotspot (550, 528, 50, 65) action QuickLoad()
        hotspot (605, 528, 50, 65) action ShowMenu('save')
        hotspot (660, 528, 50, 65) action ShowMenu('load')
        hotspot (715, 528, 50, 65) action ShowMenu('preferences')

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


##############################################################################
# Extras Menu
#
screen extras_menu():

    imagemap:
        #xpos 60
        #ypos 120
        auto "images/ui/extras/Extras_%s.png"      
        hotspot (590, 520, 55, 70) action ShowMenu("gallery_menu")
        hotspot (660, 520, 55, 70) action ShowMenu("credits_menu")  
        hotspot (725, 520, 55, 70) action Return()
        


screen credits_menu():

    # This ensures that any other menu screen is replaced.
    tag menu
    use extras_menu
    add "images/ui/extras/Extras_credits.png"

screen gallery_menu():

    # This ensures that any other menu screen is replaced.
    tag menu
    use extras_menu
    add "images/ui/extras/Extras_CGgallerytitle.png"

    $ columns = 2
    $ rows = 2

    # Display a grid of file slots.
    grid columns rows:
        area (96,126,621,391)
        transpose True
        xfill True
    
        for gal_item in gallery_cg_items:     
    
            add g_cg.make_button(gal_item + " butt", gal_item + " butt", "images/ui/extras/Extras_gallerybox.png",  background=None)

                
init python:
  
    ## Image list for CG Gallery ##
    gallery_cg_items = ["cg brianr",  
                      "cg brianf", 
                      "cg leef", 
                      "cg leer", ]

    #Galleries settings - start
    #list the CG gallery images here:
    #how many rows and columns in the gallery screens?
    gal_rows = 3
    gal_cols = 1
    #thumbnail size in pixels:
    thumbnail_x = 295
    thumbnail_y = 181
    #Galleries settings - end
    
    gal_cells = gal_rows * gal_cols    
    g_cg = Gallery()
    for gal_item in gallery_cg_items:
        g_cg.button(gal_item + " butt")
        g_cg.image(gal_item)
        g_cg.unlock(gal_item)
    g_cg.transition = fade
    cg_page=0
    
    
init +1 python:
    #Here we create the thumbnails. We use a special "locked" image for CGs to prevent spoilers.
    for gal_item in gallery_cg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
