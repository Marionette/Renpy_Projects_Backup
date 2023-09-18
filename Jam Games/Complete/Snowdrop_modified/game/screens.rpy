################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

        text what id "what"
    use quick_menu


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

#style window:
#    xalign 0.5
#    xfill True
#    yalign gui.textbox_yalign
#    ysize gui.textbox_height
#
#    background Image("textbox_withbuttons_noname.png", xalign= 0.400, yalign= 1.0)
#
#style namebox:
#    xpos 0.34
#    xanchor gui.name_xalign
#    xsize gui.namebox_width
#    ypos -0.38
#    ysize gui.namebox_height
#
#    background Image("nameboxadj.png", xalign= 0.266, yalign= 0.670)
#    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.58
    yalign 0.4

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos 0.32
    xsize gui.dialogue_width
    ypos 0.1

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
    tag menu
    imagemap:
        auto "gui/menus/quick_%s.png" #alpha False
        hotspot (385, 665, 120, 55)  action QuickSave()
        hotspot (515, 665, 120, 55)  action QuickLoad()
        hotspot (640, 665, 120, 55)  action Preference("auto-forward", "toggle")
        hotspot (775, 665, 120, 55)  action Skip()
        hotspot (910, 665, 120, 55)  action ShowMenu("history")
        hotspot (1040, 665, 120, 55)  action ShowMenu("preferences")

#screen quick_menu():
#
#    tag menu
#    textbutton _("Auto") action Preference("auto-forward", "toggle")
#
#    imagemap:
#        ground "snowflakeSettingsB.png"
#        idle "Invisible screen.png"
#        hover "Invisible screen hover.png"
#        selected_idle "Invisible screen hoverG.png"
#        selected_hover "Invisible screen hoverI.png"
#
#        hotspot (1076,678,107,42) action ShowMenu("save")
#        hotspot (975,680,102,40) action ShowMenu("load")
#        hotspot (1205,0,65,94) action ShowMenu("preferences")
#        hotspot (874,683,101,37) action ShowMenu("history")
#        hotspot (563,683,106,37) action Skip() alternate Skip(fast=True, confirm=True)
#        hotspot (670,683,102,37) action Preference("auto-forward", "toggle")
#        #hotspot (670,683,50,37) action Preference("auto-forward", "enable")
#        #hotspot (720,683,50,37) action Preference("auto-forward", "disable")
#        hotspot (772,683,102,37) action Preference("display", "toggle")

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
#init python:
    #config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")
style quick_button_text:
    properties gui.button_text_properties("quick_button")
################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    imagemap:
        auto "gui/menus/nav_%s.png" alpha False

        hotspot (50, 600, 120, 120) action Return()
        hotspot (260, 600, 120, 120) action ShowMenu("save")
        hotspot (475, 600, 120, 120) action ShowMenu("load")
        hotspot (680, 600, 120, 120) action ShowMenu("preferences")
        hotspot (890, 600, 140, 120) action MainMenu()
        hotspot (1110, 600, 120, 120) action Quit()

#screen navigation():
#
#    vbox:
#        style_prefix "navigation"
#
#        xpos gui.navigation_xpos
#        yalign 0.5
#
#        spacing gui.navigation_spacing
#
#        if main_menu:
#
#            textbutton _("Start") action [Play("sound", "audio/sound/LBegin.ogg"), Start()]
#
#        else:
#
#            textbutton _("History") action ShowMenu("history")
#
#            textbutton _("Save") action ShowMenu("save")
#
#        textbutton _("Load") action ShowMenu("load")
#
#        textbutton _("Preferences") action ShowMenu("preferences")
#
#        if _in_replay:
#
#            textbutton _("End Replay") action EndReplay(confirm=True)
#
#        elif not main_menu:
#
#            textbutton _("Main Menu") action MainMenu()
#
#        textbutton _("About") action ShowMenu("about")
#
#        if renpy.variant("pc"):
#
#            ## Help isn't necessary or relevant to mobile devices.
#            textbutton _("Help") action ShowMenu("help")
#
#            ## The quit button is banned on iOS and unnecessary on Android.
#            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add "gui/background.png"
    add "gui/menus/title.png"

    imagemap:
        auto "gui/menus/mm_%s.png"
        hotspot (150, 600, 120, 120) action [Play("sound", "audio/sound/LBegin.ogg"), Start()]
        hotspot (370, 600, 120, 120) action ShowMenu("load")
        hotspot (580, 600, 120, 120) action ShowMenu("preferences")
        #hotspot (800, 600, 120, 120) action ShowMenu("gallery")
        hotspot (1010, 600, 120, 120) action Quit(confirm=False)

    add "snow"

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    #textbutton _("Return"):
    #    style "return_button"

    #    action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

init python:
    config.thumbnail_width = 200
    config.thumbnail_height = 115

screen file_picker():


    #imagemap:
    #    auto "gui/menus/saveload_quickauto_%s.png"
    #    alpha False
    #    hotspot (1066, 237, 105, 57) action FilePage("quick")
    #    hotspot (1172, 237, 80, 57) action FilePage("auto")

    imagemap:
        #xpos 60
        #ypos 120
        auto "gui/menus/saveload_nav_%s.png"
        alpha False
        hotspot (1150, 45, 75, 75) action FilePagePrevious()
        hotspot (1150, 135, 75, 75) action FilePage(1)
        hotspot (1150, 225, 75, 75) action FilePage(2)
        hotspot (1150, 315, 75, 75) action FilePage(3)
        hotspot (1150, 405, 75, 75) action FilePage(4)
        hotspot (1150, 495, 75, 75) action FilePageNext()

    $ columns = 4
    $ rows = 3

    # Display a grid of file slots.
    grid columns rows:
        area (65,45,1030,530)
        transpose True
        xfill True
        style_group "file_picker"

        # Display ten file slots, numbered 1 - 10.
        for i in range(1, columns * rows + 1):


            # Each file slot is a button.
            button:
                action FileAction(i)
                background "gui/menus/saveload_box_ground.png"
                idle_background "gui/menus/saveload_box_idle.png"
                hover_background "gui/menus/saveload_box_hover.png"
                #xfill True
                yfill True
                xminimum 224
                yminimum 157

                has vbox

                # Add the screenshot.
                add FileScreenshot(i) xpos 6 ypos 3

                $ file_name = FileSlotName(i, columns * rows)
                $ file_time = FileTime(i, empty=_("No Data."))
                $ save_name = FileSaveName(i)

                text "[file_name]. [file_time!t]\n     [save_name!t]" xpos 15 ypos 16

                key "save_delete" action FileDelete(i)

screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    add "gui/background.png"
    #add "gui/menus/save_title_save.png"

    use navigation
    use file_picker


screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    add "gui/background.png"
    #add "gui/menus/save_title_load.png"

    use navigation
    use file_picker

#screen save():
#
#    tag menu
#
#    use file_slots(_("Save"))
#
#
#screen load():
#
#    tag menu
#
#    use file_slots(_("Load"))
#
#
#screen file_slots(title):
#
#    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
#
#    use game_menu(title):
#
#        fixed:
#
#            ## This ensures the input will get the enter event before any of the
#            ## buttons do.
#            order_reverse True
#
#            ## The page name, which can be edited by clicking on a button.
#            button:
#                style "page_label"
#
#                key_events True
#                xalign 0.5
#                action page_name_value.Toggle()
#
#                input:
#                    style "page_label_text"
#                    value page_name_value
#
#            ## The grid of file slots.
#            grid gui.file_slot_cols gui.file_slot_rows:
#                style_prefix "slot"
#
#                xalign 0.5
#                yalign 0.5
#
#                spacing gui.slot_spacing
#
#                for i in range(gui.file_slot_cols * gui.file_slot_rows):
#
#                    $ slot = i + 1
#
#                    button:
#                        action FileAction(slot)
#
#                        has vbox
#
#                        add FileScreenshot(slot) xalign 0.5
#
#                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
#                            style "slot_time_text"
#
#                        text FileSaveName(slot):
#                            style "slot_name_text"
#
#                        key "save_delete" action FileDelete(slot)
#
#            ## Buttons to access other pages.
#            hbox:
#                style_prefix "page"
#
#                xalign 0.5
#                yalign 1.0
#
#                spacing gui.page_spacing
#
#                textbutton _("<") action FilePagePrevious()
#
#                if config.has_autosave:
#                    textbutton _("{#auto_page}A") action FilePage("auto")
#
#                if config.has_quicksave:
#                    textbutton _("{#quick_page}Q") action FilePage("quick")
#
#                ## range(1, 10) gives the numbers from 1 to 9.
#                for page in range(1, 10):
#                    textbutton "[page]" action FilePage(page)
#
#                textbutton _(">") action FilePageNext()


init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text
    style file_picker_text is large_button_text:
      size 20
      color "#dee2e5"

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")

screen load_save_slot:
    $ file_text = "% s\n  %s" % (FileTime(number, empty="Empty Slot"), FileSaveName(number))
    add FileScreenshot(number) xpos -1 ypos 0
    text file_text xpos 11 ypos -24 size 15  color "#000000"
## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    # Include the navigation.
    #use navigation

    add "gui/background.png"
    add "gui/menus/options_labels.png"

    imagemap:
        auto "gui/menus/options_%s.png" alpha False

        #180 400
        #100 220 340 460
        hotspot (180, 100, 180, 80)  action Preference("display", "fullscreen")
        hotspot (400, 100, 180, 80)  action Preference("display", "window")
        hotspot (180, 220, 180, 80)  action Preference("skip", "all")
        hotspot (400, 220, 180, 80)  action Preference("skip", "seen")
        hotspot (180, 340, 180, 80)  action Preference("after choices", "skip")
        hotspot (400, 340, 180, 80)  action Preference("after choices", "stop")
        hotspot (180, 460, 180, 80)  action Preference("transitions", "all")
        hotspot (400, 460, 180, 80)  action Preference("transitions", "none")

    #text "Voice Volume" xpos 800 ypos 550
    bar:
      style_group "pref"
      xpos 670
      ypos 65
      value  Preference("music volume")

    bar:
      style_group "pref"
      xpos 670
      ypos 185
      value Preference("sound volume")

    bar:
      style_group "pref"
      xpos 670
      ypos 295
      value Preference("voice volume")

    bar:
      style_group "pref"
      xpos 670
      ypos 415
      value Preference("text speed")


    #if config.has_voice:
    bar:
      style_group "pref"
      xpos 670
      ypos 530
      value Preference("auto-forward time")

    # Include the navigation.
    use navigation

#screen preferences():
#
#    tag menu
#
#    if renpy.mobile:
#        $ cols = 2
#    else:
#        $ cols = 4
#
#    use game_menu(_("Preferences"), scroll="viewport"):
#
#        vbox:
#
#            hbox:
#                box_wrap True
#
#                if renpy.variant("pc"):
#
#                    vbox:
#                        style_prefix "radio"
#                        label _("Display")
#                        textbutton _("Window") action Preference("display", "window")
#                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
#
#                vbox:
#                    style_prefix "radio"
#                    label _("Rollback Side")
#                    textbutton _("Disable") action Preference("rollback side", "disable")
#                    textbutton _("Left") action Preference("rollback side", "left")
#                    textbutton _("Right") action Preference("rollback side", "right")
#
#                vbox:
#                    style_prefix "check"
#                    label _("Skip")
#                    textbutton _("Unseen Text") action Preference("skip", "toggle")
#                    textbutton _("After Choices") action Preference("after choices", "toggle")
#                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
#
#                ## Additional vboxes of type "radio_pref" or "check_pref" can be
#                ## added here, to add additional creator-defined preferences.
#
#            null height (4 * gui.pref_spacing)
#
#            hbox:
#                style_prefix "slider"
#                box_wrap True
#
#                vbox:
#
#                    label _("Text Speed")
#
#                    bar value Preference("text speed")
#
#                    label _("Auto-Forward Time")
#
#                    bar value Preference("auto-forward time")
#
#                vbox:
#
#                    if config.has_music:
#                        label _("Music Volume")
#
#                        hbox:
#                            bar value Preference("music volume")
#
#                    if config.has_sound:
#
#                        label _("Sound Volume")
#
#                        hbox:
#                            bar value Preference("sound volume")
#
#                            if config.sample_sound:
#                                textbutton _("Test") action Play("sound", config.sample_sound)
#
#
#                    if config.has_voice:
#                        label _("Voice Volume")
#
#                        hbox:
#                            bar value Preference("voice volume")
#
#                            if config.sample_voice:
#                                textbutton _("Test") action Play("voice", config.sample_voice)
#
#                    if config.has_music or config.has_sound or config.has_voice:
#                        null height gui.pref_spacing
#
#                        textbutton _("Mute All"):
#                            action Preference("all mute", "toggle")
#                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

init -2 python:
    # Styling for the bar sliders:
    #style.pref_frame.background = None
    style.pref_slider.left_bar = "gui/menus/options_bar_full.png"
    style.pref_slider.right_bar = "gui/menus/options_bar_empty.png"
    style.pref_slider.thumb = "gui/menus/options_bar_slider.png"
    style.pref_slider.xmaximum = 427
    style.pref_slider.ymaximum = 61
    style.pref_slider.thumb_offset = 18/2

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    add "gui/menus/history_box.png"

    viewport:
        style_prefix "history"
        yinitial 1.0

        yalign 0.5
        xanchor 0.5
        xpos 650

        xmaximum 1100
        ymaximum 559

        draggable True
        mousewheel True

        scrollbars "vertical"

        vbox:
            spacing 25

            for h in _history_list:

                window:

                    ## This lays things out properly if history_height is None.
                    has fixed:
                        yfit True

                    if h.who:

                        label h.who:
                            style "history_name"

                    text h.what

            if not _history_list:
                label _("The dialogue history is empty.")


style history_window is empty

style history_window:
    xfill True
    ysize None

style history_name:
    xpos 0.0
    xanchor 0.0
    ypos 0.0
    yanchor 0.0

style history_name_text:
    font "assets/moonbeam.ttf"
    color "#ffffff"
    size 30
    min_width 225
    text_align 1.0

style history_text:
    font "assets/moonbeam.ttf"
    color "#ffffff"
    size 20
    xpos 260
    ypos 7
    yanchor 0.0
    xanchor 0.0
    xsize 850
    min_width 850
    text_align 0.0
    layout "tex"

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

style history_vscrollbar:
    base_bar "gui/slider/history_slider.png"
    thumb "gui/slider/history_thumb.png"
    thumb_offset 3
    top_gutter 2
    bottom_gutter 2
    xmaximum 19
    ymaximum 559

## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    imagemap:
        auto "gui/menus/yesno_%s.png" alpha False
        hotspot (500, 390, 100, 70) action yes_action
        hotspot (700, 390, 100, 70) action no_action

    frame:
      background None
      area (410,220,470,200)
      label _(message):
        style "confirm_prompt"
        xalign 0.5
        #yalign 0.4

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    #xalign .7
    #yalign .4

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600
