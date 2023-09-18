# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

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

screen choice:
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

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

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

screen nvl:

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

image blossoms = SnowBlossom("gui/blossoms1.png", count=10, border=50, xspeed=(20, 50), yspeed=(100, 200), start=0, horizontal=True)

transform lower_down:
    yanchor 0.5 ypos -.2 xalign 0.5
    linear 3.0 ypos .2    
    

transform mm_button_hover:
    on hover:
        linear 0.1 yoffset -5
        linear 0.1 yoffset 0
        linear 0.1 yoffset -1
        linear 0.1 yoffset 0
    on idle:
        linear 0.1 yoffset 0

screen main_menu:

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    add "gui/mm_bg.jpg"
    
    add "gui/logo.png" at lower_down

    # The main menu buttons.
    vbox:
        style_group "mm"
        xalign .5
        yalign .75
        spacing 10
        
        imagebutton idle "gui/start1.png" hover "gui/start2.png" xalign 0.5 action Start() at mm_button_hover
        imagebutton idle "gui/load1.png" hover "gui/load2.png" xalign 0.5 action ShowMenu("load") at mm_button_hover
        imagebutton idle "gui/options1.png" hover "gui/options2.png" xalign 0.5 action ShowMenu("preferences") at mm_button_hover
        imagebutton idle "gui/extras1.png" hover "gui/extras2.png" xalign 0.5 action ShowMenu("extras") at mm_button_hover
        #imagebutton idle "gui/about1.png" hover "gui/about2.png xalign 0.5" action Help() at mm_button_hover
        imagebutton idle "gui/quit1.png" hover "gui/quit2.png" xalign 0.5 action Quit(confirm=False) at mm_button_hover
        
    add SnowBlossom("gui/bokeh.png", count=10, border=10, xspeed=(5, 250), yspeed=(50, 200), start=0, horizontal=True)

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
screen navigation:

    # The background of the game menu.
    add "gui/gm_bg.jpg"

    add "gui/nav_bar.png" xalign 0.5 yalign 1.0
    
    # The various buttons.
    hbox:
        style_group "gm_nav"
        xalign .5
        yalign .98
        textbutton _("Return") action Return() at mm_button_hover
        textbutton _("Preferences") action ShowMenu("preferences") at mm_button_hover
        textbutton _("Save Game") action ShowMenu("save") at mm_button_hover
        textbutton _("Load Game") action ShowMenu("load") at mm_button_hover
        textbutton _("Main Menu") action MainMenu() at mm_button_hover
        textbutton _("Quit") action Quit() at mm_button_hover

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
init:
    $ config.thumbnail_width = 158
    $ config.thumbnail_height = 89
image upsidedown_nav:
    "gui/nav_bar.png"
    yzoom -1
    xzoom -1
    

screen file_picker:
    add "upsidedown_nav" xalign 0.5 yalign 0.0
    add "gui/title_saveload.png" xalign 0.5 yalign 0.1
    vbox ypos 20:
        style "file_picker_frame"

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox xalign 0.5:
            style_group "file_picker_nav"

            textbutton _("Previous") at mm_button_hover:
                action FilePagePrevious()

            textbutton _("Auto") at mm_button_hover:
                action FilePage("auto")

            textbutton _("Quick") at mm_button_hover:
                action FilePage("quick")

            for i in range(1, 6):
                textbutton str(i) at mm_button_hover:
                    action FilePage(i)

            textbutton _("Next") at mm_button_hover:
                action FilePageNext()

        $ columns = 3
        $ rows = 3

        # Display a grid of file slots.
        null height 90
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    background Frame("gui/textbox.png",50,50) top_padding 60 bottom_padding 80 xpadding 60 yminimum 250 xminimum 600 xalign 0.5 
                    insensitive_background Frame(im.MatrixColor("gui/textbox.png",im.matrix.opacity(0.5)),50,50)
                    hover_background Frame(im.MatrixColor("gui/textbox.png",im.matrix.brightness(-0.1)),50,50)

                    hbox xalign 0.2 yalign 0.5:

                        # Add the screenshot.
                        frame background Frame("gui/button2.png",20,20) xpadding 8 ypadding 8 yminimum 0 hover_background Frame(im.MatrixColor("gui/button2.png",im.matrix.brightness(-0.1)),20,20) insensitive_background Frame("gui/button3.png",20,20):
                            add FileScreenshot(i)
    
                        $ file_name = FileSlotName(i, columns * rows)
                        $ file_time = FileTime(i, empty=_("Empty Slot."))
                        $ save_name = FileSaveName(i)
                        null width 10
                        text "[file_name]. [file_time!t]\n[save_name!t]" size 28
    
                        key "save_delete" action FileDelete(i)


screen save:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

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

screen preferences:

    tag menu

    # Include the navigation.
    use navigation
    
    add "upsidedown_nav" xalign 0.5 yalign 0.0
    add "gui/title_options.png" xalign 0.5 yalign 0.08

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True  ypos 140

        # The left column.
        vbox:
            frame xfill True:
                vbox xalign 0.5:
                    text ("Display") xalign 0.5 style "pref_label_text"
                    hbox xalign 0.5:
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame xfill True:
                vbox xalign 0.5:
                    text ("Transitions") xalign 0.5 style "pref_label_text"
                    hbox xalign 0.5:
                        textbutton _("All") action Preference("transitions", "all")
                        textbutton _("None") action Preference("transitions", "none")

            frame xfill True:
                vbox xalign 0.5:
                    text ("Text Speed") xalign 0.5 style "pref_label_text"
                    bar value Preference("text speed")



        vbox:
            frame xfill True:
                vbox xalign 0.5:

                    text ("Skip") xalign 0.5 style "pref_label_text"
                    hbox xalign 0.5:
                        textbutton _("Seen Text") action Preference("skip", "seen")
                        textbutton _("All Text") action Preference("skip", "all")
                    textbutton _("Begin Skipping") action Skip() xalign 0.5

            frame xfill True:
                vbox xalign 0.5:
    
                    text ("After Choices") xalign 0.5 style "pref_label_text"
                    hbox xalign 0.5:
                        textbutton _("Stop") action Preference("after choices", "stop")
                        textbutton _("Keep Going") action Preference("after choices", "skip")

            frame xfill True:
                vbox xalign 0.5:

                    text ("Auto-Forward Time") xalign 0.5 style "pref_label_text"
                    bar value Preference("auto-forward time")
    
                    if config.has_voice:
                        textbutton _("Wait for Voice") action Preference("wait for voice", "toggle") xalign 0.5

        vbox:
            frame xfill True:
                vbox xalign 0.5:

                    text ("Music Volume") xalign 0.5 style "pref_label_text"
                    bar value Preference("music volume")

            frame xfill True:
                vbox xalign 0.5:

                    text ("Sound Volume") xalign 0.5 style "pref_label_text"
                    bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button" xalign 0.5

            if config.has_voice:
                frame xfill True:
                    vbox xalign 0.5:

                        text ("Voice Volume") xalign 0.5 style "pref_label_text"
                        bar value Preference("voice volume")
    
                        textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                        if config.sample_voice:
                            textbutton _("Test"):
                                action Play("voice", config.sample_voice)
                                style "soundtest_button" xalign 0.5

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
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
image ctc_tree:
    xpos 1545 ypos 940 xanchor 0.0 yanchor 0.0
    "GUI/ctc1.png"
    "GUI/ctc2.png" with Dissolve(1.0, alpha=True)
    1.0
    "GUI/ctc3.png" with Dissolve(1.0, alpha=True)
    1.0
    "GUI/ctc4.png" with Dissolve(1.0, alpha=True)
    1.0
    "GUI/ctc1.png" with Dissolve(1.0, alpha=True)
    1.0
    repeat

screen yesno_prompt:

    modal True

    
    add "gui/mm_bg.jpg" xalign 0.5 yalign 0.5

    frame:
        style_group "yesno"
        xminimum 1000 xalign 0.5 ypadding 100 xpadding 100
        xmargin .05
        yalign 0.35
        yanchor 0

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action at mm_button_hover
            textbutton _("No") action no_action at mm_button_hover

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
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 0.0
        yalign 0.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 25
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

