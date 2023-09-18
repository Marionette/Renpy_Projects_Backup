﻿################################################################################
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
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

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

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

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
## https://www.renpy.org/doc/html/screen_special.html#choice

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
    ypos 405
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

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:

            xalign 0.9
            yalign 0.98
            vbox:
                style_prefix "quick"

               #xalign 0.8
                #yalign 0.9

                textbutton _("Back") action Rollback()
                textbutton _("History") action ShowMenu('history')
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                #textbutton _("Save") action ShowMenu('save')
                #textbutton _("Q.Save") action QuickSave()
                #textbutton _("Q.Load") action QuickLoad()
                #textbutton _("Prefs") action ShowMenu('preferences')
                
            vbox:
                style_prefix "quick"

                #xalign 0.95
                #yalign 0.9

                #textbutton _("Back") action Rollback()
                #textbutton _("History") action ShowMenu('history')
                #textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                #textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Save") action ShowMenu('save')
                textbutton _("Load") action ShowMenu('load')
                #textbutton _("Q.Save") action QuickSave()
                #textbutton _("Q.Load") action QuickLoad()
                textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

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

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if persistent.extras_unlocked and main_menu:

            textbutton _("Extras") action ShowMenu("bg_gallery")

        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    size 76


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 20
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

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
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

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
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 20
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1220
style game_menu_vpgrid:
    xsize 1220

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


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
            
            textbutton "Show Credits" action Replay("lbl_credits")

            text _("\nMade with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


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

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.3
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.0
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.3
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

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


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                #vbox:
                #    style_prefix "radio"
                #    label _("Rollback Side")
                #    textbutton _("Disable") action Preference("rollback side", "disable")
                #    textbutton _("Left") action Preference("rollback side", "left")
                #    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    #textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


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

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 1

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

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
    xsize 425

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 575


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

    #use game_menu(_("Help"), scroll="viewport"):
    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


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
            spacing 23

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
        label _("Mouse Wheel Up")
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
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

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
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background "gui/frame.png"
    padding gui.confirm_frame_borders.padding
    xalign 1.0
    #yalign .1
    xmaximum 620
    

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    ypos 250
    xpos 20

style confirm_button:
    properties gui.button_properties("confirm_button")
    ypos 250

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
            spacing 9

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
        text "[message!tq]"

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
## https://www.renpy.org/doc/html/screen_special.html#nvl


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
define config.nvl_list_length = gui.nvl_list_length

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



## Extras screens #################################################################
##
## A screen that includes Image Galleries, Music Room, Replay Room, and Developer
## Notes.
## https://www.renpy.org/doc/html/rooms.html

## We let Ren'Py resize our images so we don't have to make buttons in another
## program.


# These cg buttons are 480x270
image BEE_X_VIDA_KISS_CG_button = im.FactorScale("images/cg/BEE_X_VIDA_KISS_CG.png", 0.25)
image SORA_X_UMI_ANIME_FAN_SERVICE_CG_button = im.FactorScale("images/cg/SORA_X_UMI_ANIME_FAN_SERVICE_CG.png", 0.25)
image SORA_X_UMI_DOODLE_MINI_CG_button = im.FactorScale("images/cg/SORA_X_UMI_DOODLE_MINI_CG.png", 0.25)
image VIDA_DOODLE_MINI_CG_button = im.FactorScale("images/cg/VIDA_DOODLE_MINI_CG.png", 0.25)

# These background buttons are 480x270
image bglock_button = "gui/button/bg_locked.png"

image TRAFFIC_button = im.FactorScale("images/bg/TRAFFIC.jpg" , 0.25)
image LIVING_ROOM_button = im.FactorScale("images/bg/LIVING_ROOM.jpg" , 0.25)
image BEDROOM_button = im.FactorScale("images/bg/BEDROOM.jpg" , 0.25)
image CLASSROOM_button = im.FactorScale("images/bg/CLASSROOM.jpg" , 0.25)
image LIBRARY_button = im.FactorScale("images/bg/LIBRARY.jpg" , 0.25)
image CAFETERIA_button = im.FactorScale("images/bg/CAFETERIA.jpg", 0.25)
    
# These sprite buttons are 290x290
image ehappy_button = Crop((170, 245, 290, 290), "eileen happy")
image eneutral_button = Crop((170, 245, 290, 290), "eileen neutral")
image esurprised_button = Crop((170, 245, 290, 290), "eileen surprised")
image eupset_button = Crop((170, 245, 290, 290), "eileen upset")
image eangry_button = Crop((170, 245, 290, 290), "eileen angry")
image spritelock_button = "gui/button/sprite_locked.png"

init python:

    # Images for the CG Gallery
    g_cg = Gallery()

    g_cg.button("BEE_X_VIDA_KISS_CG")
    g_cg.image("BEE_X_VIDA_KISS_CG")
    g_cg.unlock("BEE_X_VIDA_KISS_CG")
    
    g_cg.button("SORA_X_UMI_ANIME_FAN_SERVICE_CG")
    g_cg.image("SORA_X_UMI_ANIME_FAN_SERVICE_CG")
    g_cg.unlock("SORA_X_UMI_ANIME_FAN_SERVICE_CG")
    
    g_cg.button("SORA_X_UMI_DOODLE_MINI_CG")
    g_cg.image("SORA_X_UMI_DOODLE_MINI_CG")
    g_cg.unlock("SORA_X_UMI_DOODLE_MINI_CG")
    
    g_cg.button("VIDA_DOODLE_MINI_CG")
    g_cg.image("VIDA_DOODLE_MINI_CG")
    g_cg.unlock("VIDA_DOODLE_MINI_CG")

    
    # Backgrounds for the BG Gallery
    g_bg = Gallery()

    g_bg.button("bg TRAFFIC")
    g_bg.unlock_image("bg TRAFFIC") 

    g_bg.button("bg LIVING_ROOM")
    g_bg.image("bg LIVING_ROOM")
    g_bg.unlock("bg LIVING_ROOM")

    g_bg.button("bg BEDROOM")
    g_bg.image("bg BEDROOM")
    g_bg.unlock("bg BEDROOM")
    
    g_bg.button("bg CLASSROOM")
    g_bg.image("bg CLASSROOM")
    g_bg.unlock("bg CLASSROOM")
    
    g_bg.button("bg LIBRARY")
    g_bg.image("bg LIBRARY")
    g_bg.unlock("bg LIBRARY")
    
    g_bg.button("bg CAFETERIA")
    g_bg.image("bg CAFETERIA")
    g_bg.unlock("bg CAFETERIA")

    
    # Sprites for the Sprite Gallery
    # We put a background in the first spot so Eileen isn't floating in a void.

    g_sprite = Gallery()
    
    g_sprite.button("eileen happy")
    g_sprite.unlock_image("room", "eileen happy")
    
    g_sprite.button("eileen neutral")
    g_sprite.unlock_image("room", "eileen neutral")
    
    g_sprite.button("eileen surprised")
    g_sprite.unlock_image("room", "eileen surprised")
    
    g_sprite.button("eileen upset")
    g_sprite.image("room", "eileen upset")
    g_sprite.unlock("room", "eileen upset")
    
    g_sprite.button("eileen angry")
    g_sprite.image("room", "eileen angry")
    g_sprite.unlock("room", "eileen angry")

    # The button used for locked images
    g_cg.locked_button = "bglock_button"
    g_bg.locked_button = "bglock_button"
    g_sprite.locked_button = "spritelock_button"

    # The transition used when switching images.
    g_cg.transition = dissolve
    g_bg.transition = dissolve
    g_sprite.transition = dissolve

    # MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    # Add music files.
    mr.add("audio/music/DREAMS.mp3")
    mr.add("audio/music/INSPIRING.mp3")
    mr.add("audio/music/PARANOIA.mp3")
    mr.add("audio/music/SLICE_OF_LIFE.mp3")

## Extras Navigation screen ############################################################
##
## This is the same as the Game Menu Navigation screen, but just for the Extras.

screen extras_navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing


        #textbutton _("Sprite Gallery") action ShowMenu("sprite_gallery")

        textbutton _("CG Gallery") action ShowMenu("cg_gallery")
        textbutton _("Background Gallery") action ShowMenu("bg_gallery")

        textbutton _("Music Room") action ShowMenu("music_gallery")

        textbutton _("Endings Unlocked") action ShowMenu("endings_gallery")
        textbutton _("Glossary") action ShowMenu("Glossary")
        textbutton _("Credits") action  Replay("lbl_credits")

        if persistent.game_clear:

            textbutton _("Developer Notes") action ShowMenu("dev_notes")

        textbutton _("Return") action Return()

## Extras Menu screen ############################################################
##
## This is the same as the Game Menu screen, but just for the Extras.

screen extras_menu(title, scroll=None, yinitial=0.0):

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
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use extras_navigation

    label title

## Sprite Gallery screen ############################################################
##
## This is a simple screen that shows buttons that display a sprite imposed on a
## background.

#screen sprite_gallery():
#
#    tag menu
#
#    ## This use statement includes the extras_menu screen inside this one.
#    use extras_menu("Sprite Gallery"):
#
#        grid 5 1:
#
#            xfill True
#            yfill True
#
#            # Call make_button to show a particular button.
#            add g_sprite.make_button("eileen happy", "ehappy_button")
#            add g_sprite.make_button("eileen neutral", "eneutral_button")
#            add g_sprite.make_button("eileen surprised", "esurprised_button")
#            add g_sprite.make_button("eileen upset", "eupset_button")
#            add g_sprite.make_button("eileen angry", "eangry_button")

## CG Gallery screen ############################################################
##
## This is a simple screen that shows buttons that display a CG.

screen cg_gallery():

    tag menu

    ## This use statement includes the extras_menu screen inside this one.
    use extras_menu("CG Gallery"):

        grid 2 2:
            xpos 50
            ypos 50
            #xfill True
            #yfill True
            xspacing 50
            yspacing 50

            # Call make_button to show a particular button.
            add g_cg.make_button("BEE_X_VIDA_KISS_CG", "BEE_X_VIDA_KISS_CG_button", xalign=0.5, yalign=0.5)
            add g_cg.make_button("SORA_X_UMI_ANIME_FAN_SERVICE_CG", "SORA_X_UMI_ANIME_FAN_SERVICE_CG_button", xalign=0.5, yalign=0.5)
            add g_cg.make_button("SORA_X_UMI_DOODLE_MINI_CG", "SORA_X_UMI_DOODLE_MINI_CG_button", xalign=0.5, yalign=0.5)
            add g_cg.make_button("VIDA_DOODLE_MINI_CG", "VIDA_DOODLE_MINI_CG_button", xalign=0.5, yalign=0.5)

## Background Gallery screen ############################################################
##
## This is a simple screen that shows buttons that display a background.

screen bg_gallery():

    tag menu

    ## This use statement includes the extras_menu screen inside this one.
    use extras_menu("Background Gallery"):

        grid 2 3:
            xpos 50
            #xfill True
            yfill True
            xspacing 50

            # Call make_button to show a particular button.
            add g_bg.make_button("bg TRAFFIC", "TRAFFIC_button", xalign=0.5, yalign=0.5)
            add g_bg.make_button("bg LIVING_ROOM", "LIVING_ROOM_button", xalign=0.5, yalign=0.5)
            add g_bg.make_button("bg CLASSROOM", "CLASSROOM_button", xalign=0.5, yalign=0.5)
            add g_bg.make_button("bg LIBRARY", "LIBRARY_button", xalign=0.5, yalign=0.5)
            add g_bg.make_button("bg BEDROOM", "BEDROOM_button", xalign=0.5, yalign=0.5)
            add g_bg.make_button("bg CAFETERIA", "CAFETERIA_button", xalign=0.5, yalign=0.5)

## Music Gallery screen ############################################################
##
## This is a simple screen that shows buttons that play a music track.

screen music_gallery:

    tag menu

    ## This use statement includes the extras_menu screen inside this one.
    use extras_menu("Music Room", scroll="viewport"):

        vbox:

            xalign 0.5
            yalign 0.5

            # The buttons that play each track.
            if mr.is_unlocked("audio/music/DREAMS.mp3"):
                textbutton "1. Dreams" action mr.Play("audio/music/DREAMS.mp3")
            else:
                textbutton "1. ???" action NullAction()
            if mr.is_unlocked("audio/music/INSPIRING.mp3"):
                textbutton "2. Inspiring" action mr.Play("audio/music/INSPIRING.mp3")
            else:
                textbutton "2. ???" action NullAction()
            if mr.is_unlocked("audio/music/PARANOIA.mp3"):
                textbutton "3. Paranoia" action mr.Play("audio/music/PARANOIA.mp3")
            else:
                textbutton "3. ???" action NullAction()
            if mr.is_unlocked("audio/music/SLICE_OF_LIFE.mp3"):
                textbutton "4. Slice of Life" action mr.Play("audio/music/SLICE_OF_LIFE.mp3")
            else:
                textbutton "4. ???" action NullAction()

            null height 40

            hbox:
            # Buttons that let us advance through tracks.
                textbutton "Previous" action mr.Previous()
                textbutton "Next" action mr.Next()

            null height 20

        # Start the music playing on entry to the music room.
        on "replace" action mr.Play()

        # Restore the main menu music upon leaving.
        on "replaced" action Play("music", "audio/music/SLICE_OF_LIFE.mp3")
            

## Endings Gallery screen ############################################################
##
## This is a simple screen that shows buttons that endings from the game that have been seen.
screen endings_gallery:

    tag menu

    ## This use statement includes the extras_menu screen inside this one.
    use extras_menu("Endings Unlocked", scroll="viewport"):

        vbox:

            xalign 0.5
            yalign 0.5
            
            if persistent.ending_seen_1:
                text "1. Discovery by Ate"
            else:
                text "1. ???"
            if persistent.ending_seen_2:
                text "2. Discovery by Your Teacher"
            else:
                text "2. ???"
            if persistent.ending_seen_3:
                text "3. Discovery by Your Classmates"
            else:
                text "3. ???"
            if persistent.ending_seen_4:
                text "4. Discovery by Mom"
            else:
                text "4. ???"
            if persistent.ending_seen_5:
                text "5. A Real Hot Ending"
            else:
                text "5. ???"
            if persistent.ending_seen_6:
                text "6. Head in the Clouds"
            else:
                text "6. ???"
            if persistent.ending_seen_7:
                text "7. Gay Minus"
            else:
                text "7. ???"
            if persistent.ending_seen_8:
                text "8. FanFiction.Net"
            else:
                text "8. ???"
            if persistent.ending_seen_9:
                text "9. Fujoshi Fanclub"
            else:
                text "9. ???"

            null height 20
            

## Glossary screen ############################################################
##
## This is a simple screen that shows a glossary of terms from the game.
screen Glossary:

    tag menu

    ## This use statement includes the extras_menu screen inside this one.
    use extras_menu("Glossary of Filipino Terms", scroll="viewport"):

        vbox:

            xalign 0.5
            yalign 0.5

            # The glossary terms.
            text "{size=+20}Assunta de Rossi:{/size} {size=-10}A Filipino-Italian actress.{/size}"
            text "{size=+20}Ate:{/size} {size=-10}Elder sister.{/size}."
            text "{size=+20}Bisaya:{/size} {size=-10}An informal term for the Cebuano language.{/size}."
            text "{size=+20}Chickenjoy:{/size} {size=-10}Fried chicken from Jollibee, a fast food restaurant chain.{/size}."
            text "{size=+20}Coco Martin:{/size} {size=-10}A Filipino actor who first rose to prominence in the indie film scene.{/size}."
            text "{size=+20}Don Juan:{/size} {size=-10}The central character of the corrido (narrative ballad) called Ibong Adarna.{/size}."
            text "{size=+20}Fidel Ramos:{/size} {size=-10}The 12th Philippine President.{/size}."
            text "{size=+20}Hansel:{/size} {size=-10}A brand of biscuit sandwiches.{/size}."
            text "{size=+20}Ibong Adarna:{/size} {size=-10}A mythical bird whose powers include lulling people to sleep and turning people to stone.{/size}."
            text "{size=+20}Imelda Marcos:{/size} {size=-10}The wife of Ferdinand Marcos, the 10th Philippine President.{/size}."
            text "{size=+20}Jeepney:{/size} {size=-10}A mode of public transportation that can carry around twenty passengers.{/size}."
            text "{size=+20}Jericho Rosales:{/size} {size=-10}A multitalented Filipino entertainer. "
            text "{size=+20}Lumpia:{/size} {size=-10}Spring roll.{/size}."
            text "{size=+20}Malacanang Palace:{/size} {size=-10}The official residence of the Philippine President.{/size}."
            text "{size=+20}Panitikan:{/size} {size=-10}Literature.{/size}."
            text "{size=+20}Papuri sa Diyos:{/size} {size=-10}Glory to God.{/size}."
            text "{size=+20}Sala:{/size} {size=-10}Living room. Of Spanish origin.{/size}."
            text "{size=+20}Siesta:{/size} {size=-10}Afternoon nap. Of Spanish origin.{/size}."
            text "{size=+20}Telenovela:{/size} {size=-10}Soap opera. Of Spanish origin.{/size}."
            text "{size=+20}Tomi:{/size} {size=-10}A brand of sweet-corn-flavored chips.{/size}."
            text "{size=+20}Tricycle:{/size} {size=-10}A mode of public transportation that can carry around four passengers.{/size}."

            null height 20


################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

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

style radio_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

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
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900





