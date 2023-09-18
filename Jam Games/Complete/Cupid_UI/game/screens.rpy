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
    bold True

style say_dialogue:
    properties gui.text_properties("dialogue")
    xalign 0.5
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
    add "gui/choicebg.png"

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
    ypos 0.5
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
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            add "gui/misc/dot_spacer_small.png" yalign 0.5
            textbutton _("Save") action ShowMenu('save')
            add "gui/misc/dot_spacer_small.png" yalign 0.5
            textbutton _("Q.Save") action QuickSave()
            add "gui/misc/dot_spacer_small.png" yalign 0.5
            textbutton _("Q.Load") action QuickLoad()
            add "gui/misc/dot_spacer_small.png" yalign 0.5
            #textbutton _("History") action ShowMenu('history')
            #add "gui/misc/dot_spacer_small.png" yalign 0.5
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            add "gui/misc/dot_spacer_small.png" yalign 0.5
            textbutton _("F. Skip") action Skip() alternate Skip(fast=True, confirm=False)
            add "gui/misc/dot_spacer_small.png" yalign 0.5
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            add "gui/misc/dot_spacer_small.png" yalign 0.5
            textbutton _("Options") action ShowMenu('preferences')
            add "gui/misc/dot_spacer_small.png" yalign 0.5
            textbutton _("Chapters") action ShowMenu('extra_chapter_select')
            #if config.developer:
            #  add "gui/misc/dot_spacer_small.png" yalign 0.5
            #  textbutton _("Dev Mode") action ShowMenu('chapter_select') #for dev


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

screen navigation(navOffset=0):

    hbox:
        style_prefix "navigation_mm"

        ypos gui.navigation_ypos
        xalign 0.5
        yoffset navOffset
        

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()
            add "gui/misc/dot_spacer_big.png" yalign 0.5

        else:

            textbutton _("Return") action Return()
            add "gui/misc/dot_spacer_big.png" yalign 0.5

            #textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")
            add "gui/misc/dot_spacer_big.png" yalign 0.5

        textbutton _("Load") action ShowMenu("load")
        add "gui/misc/dot_spacer_big.png" yalign 0.5

        textbutton _("Options") action ShowMenu("preferences")

        if _in_replay:

            add "gui/misc/dot_spacer_big.png" yalign 0.5
            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            add "gui/misc/dot_spacer_big.png" yalign 0.5
            textbutton _("Main Menu") action MainMenu()

        #textbutton _("About") action ShowMenu("about")

        add "gui/misc/dot_spacer_big.png" yalign 0.5
        textbutton _("Chapter Select") action ShowMenu("extra_chapter_select")

        #if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            #textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            add "gui/misc/dot_spacer_big.png" yalign 0.5
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    xalign 0.5

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 0.5
    
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
    #use navigation
    
    vbox:
        style_prefix "navigation"
        xalign 0.5
        yalign 0.5
        xoffset 16

        spacing gui.navigation_spacing
        
        textbutton _("START") action Start()
        textbutton _("CONTINUE") action ShowMenu("load")        
        
        hbox:
          style_prefix "navigation_mm"
          ypos 250
          xalign 0.5
          textbutton _("OPTIONS") action ShowMenu("preferences")
          textbutton _("BONUS") action ShowMenu("extra_chapter_select")
          textbutton _("UNLOCK") action Replay("unlock_everything", locked=False)
          if renpy.variant("pc"):
              ## The quit button is banned on iOS and unnecessary on Android and
              ## Web.
              textbutton _("QUIT") action Quit(confirm=not main_menu)

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "v [config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text
style main_menu is gui_button
style main_menu is gui_button_text
style navigation_mm is main_menu

style main_menu_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    xalign 0.5

style main_menu_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 0.5

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 0.5
    

style navigation_mm_button_text:
    properties gui.button_text_properties("navigation_button")
    xalign 0.5
    #size 18
    
style navigation_mm_hbox:
    xoffset -20
    spacing 50

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 0.5
    xoffset 20
    #xmaximum 800
    #yalign 1.0
    #yoffset -20

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

screen game_menu(title, scroll=None, yinitial=0.0, navOffset=0):

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
                #background Solid("#123123")
                #xalign 0.5

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

    use navigation(navOffset)

    vbox:
        xalign 0.5
        yoffset 120
        style "game_menu_title"
        spacing 0      
        add "gui/misc/menu_heart_top.png" xalign 0.5  yoffset 2
        hbox:
            spacing 5
            
            add "gui/misc/menu_heart_left.png" yalign 0.5 yoffset -5
            label title            
            add "gui/misc/menu_heart_right.png" yalign 0.5 yoffset -5
        add "gui/misc/menu_heart_bottom.png" xalign 0.5 yoffset -8

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


style game_menu_title_label is gui_label
style game_menu_title_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 80
    top_padding 220
    xpadding 80
    
    background None #"gui/overlay/game_menu.png"

    #background Solid("#123123")#"gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 0
    yfill True
    #background Solid("#222222")

style game_menu_content_frame:
    left_margin 40
    right_margin 40
    ymargin 10
    #background Solid("#333333")

style game_menu_viewport:
    xsize 1080

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 0
    #ysize 120

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
    add "gui/overlay/game_menu.png"
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

screen save():

    tag menu

    use file_slots(_("SAVE"))


screen load():

    tag menu

    use file_slots(_("LOAD"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    add "gui/overlay/game_menu.png"
    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True
            vbox:
                xalign 0.5
                ## The page name, which can be edited by clicking on a button.
                #button:
                #    style "page_label"
                #
                #    key_events True
                #    xalign 0.5
                #    action page_name_value.Toggle()
                #
                #    input:
                #        style "page_label_text"
                #        value page_name_value

                ## Buttons to access other pages.
                hbox:
                    style_prefix "page"

                    xalign 0.5
                    yalign 1.0
                    xoffset -36

                    spacing gui.page_spacing

                    textbutton _("PREVIOUS") action FilePagePrevious()
                    add "gui/misc/dot_spacer_big.png" yalign 0.5

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 6):
                        textbutton "[page]" action FilePage(page)

                    add "gui/misc/dot_spacer_big.png" yalign 0.5
                    textbutton _("NEXT") action FilePageNext()                    
                    
                    null width (5 * gui.pref_spacing)
                    
                    if config.has_autosave:
                        textbutton _("{#auto_page}AUTO") action FilePage("auto")
                        add "gui/misc/dot_spacer_big.png" yalign 0.5                        
                        textbutton _("{#auto_page}NORMAL") action FilePage(1)

                    if config.has_quicksave:
                        add "gui/misc/dot_spacer_big.png" yalign 0.5
                        textbutton _("{#quick_page}QUICK") action FilePage("quick")

                null height (3 * gui.pref_spacing)
                
                ## The grid of file slots.
                grid gui.file_slot_cols gui.file_slot_rows:
                    style_prefix "slot"

                    xalign 0.5
                    yalign 0.5
                    xoffset 10

                    spacing gui.slot_spacing

                    for i in range(gui.file_slot_cols * gui.file_slot_rows):

                        $ slot = i + 1

                        button:
                            action FileAction(slot)

                            has vbox

                            #add FileScreenshot(slot) xalign 0.5

                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"

                            text FileSaveName(slot):
                                style "slot_name_text"

                            key "save_delete" action FileDelete(slot)


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
    #base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    background Frame("gui/button/savebox_ground.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    hover_background Frame("gui/button/savebox_hover.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    idle_background Frame("gui/button/savebox_idle.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    insensitive_background Frame("gui/button/savebox_insensitive.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)

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

    add "gui/overlay/game_menu.png"
    use game_menu(_("OPTIONS"), scroll="viewport"):

        vbox:
            
            hbox:
                xfill True
                #box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Windowed") action Preference("display", "window")
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
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                vbox:
                    style_prefix "check"
                    label _("Filter")
                    #Note: Filter ON means Adult OFF
                    textbutton _("Mature Filter ON") action SetField(persistent,'adult', False) 
                    textbutton _("Mature Filter OFF") action SetField(persistent,'adult', True)

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (2 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                xfill True
                box_wrap True
                xoffset 50

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
style pref_hbox is hbox

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
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    #xsize 225
    xalign 0.5
    #background Frame(Solid("#123456"))

style pref_hbox:
    #xsize 225
    xalign 0.5

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    #foreground "gui/button/radio_[prefix_]foreground.png"
    ypadding -0
    xpadding 20
    idle_background Frame("gui/button/button_idle.png", Borders(0, 0, 0, 0))
    hover_background Frame("gui/button/button_hover.png", Borders(20, 0, 20, 0))

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    #foreground "gui/button/check_[prefix_]foreground.png"
    ypadding -0
    xpadding 20
    idle_background Frame("gui/button/button_idle.png", Borders(0, 0, 0, 0))
    hover_background Frame("gui/button/button_hover.png", Borders(20, 0, 20, 0))

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350
    left_bar "gui/slider/bar_full.png"
    right_bar "gui/slider/bar_empty.png"
    thumb "gui/slider/bar_thumb.png"
    thumb_offset 7
    xoffset 50

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450

style mute_all_button:
    xalign 1.0

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

    add "gui/overlay/game_menu.png"
    use game_menu(_("HISTORY"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

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

    add "gui/overlay/game_menu.png"
    use game_menu(_("HELP"), scroll="viewport"):

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
            yalign .2
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

        hbox:
                xalign 0.5
                yalign .65
                yoffset -10
                spacing 200

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
    background None#Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .9
    yalign .45
    ysize 300

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
        #style "nvl_window"
        if nvl_darkbg:
            style "nvl_window_dark"
        else:
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

    #background "gui/nvl.png"
    padding gui.nvl_borders.padding
    
    
style nvl_window_dark:
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
    #xpos gui.nvl_text_xpos
    #xanchor gui.nvl_text_xalign
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
## Extra screens ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

    
screen extras():
    tag menu
    use extra_nav
    
screen extra_nav():  
    hbox:   
      
        style_prefix "navigation_extra"

        ypos 100
        xalign 0.5

        spacing gui.navigation_spacing

        textbutton _("CHAPTER SELECT") action ShowMenu("extra_chapter_select")
        add "gui/misc/dot_spacer_big.png" yalign 0.5

        textbutton _("GALLERY") action ShowMenu("extra_gallery")
        add "gui/misc/dot_spacer_big.png" yalign 0.5

        textbutton _("MUSIC BOX") action ShowMenu("extra_music_box")
        
        null width(8 * gui.pref_spacing)

        textbutton _("CREDITS") action ShowMenu("extra_credits")
        add "gui/misc/dot_spacer_big.png" yalign 0.5

        textbutton _("PRODUCTION NOTES") action Replay("prodnotes", {}, False)  
        add "gui/misc/dot_spacer_big.png" yalign 0.5

        textbutton _("BONUS") action ShowMenu("extra_bonus")
        
  
      
    #use navigation

style navigation_extra is navigation_mm
#style navigation_extra_button is navigation_button
#style navigation_extra_button_text is navigation_button_text

#init:
        
screen extra_chapter_select(): 
    $chapter_label_names = [["intro", "mother", "intro", persistent.IntroUnlocked],
                          ["chapter 1", "the star and the rose", "chap1", persistent.Chapter1Unlocked],
                          ["chapter 2", "la piqûre", "chap2", persistent.Chapter2Unlocked],
                          ["chapter 3", "portraits, candlelit", "chap3", persistent.Chapter3Unlocked],
                          ["chapter 4", "metamorphoses", "chap4", persistent.Chapter4Unlocked],
                          ["chapter 5", "psyche", "chap5", persistent.Chapter5Unlocked],
                          ["chapter 6", "\"good intentions\"", "chap6", persistent.Chapter6Unlocked],
                          ["chapter 7", "the taste of honey", "chap7", persistent.Chapter7Unlocked], 
                          ["chapter 8", "transience", "chap8", persistent.Chapter8Unlocked],
                          ["ending 1", "temperance", "end1", persistent.Ending1Unlocked],
                          ["ending 2", "dawning", "end2", persistent.Ending2Unlocked],
                          ["ending 3", "surrogate", "glives", persistent.Ending3Unlocked],
                          ["ending 4", "mutation", "gdies", persistent.Ending4Unlocked],
                          ["secret end", "bliss", "secretend", persistent.BonusEndingUnlocked]]
    tag menu
    add "gui/overlay/extras_menu.png"
    use game_menu(_("CHAPTER SELECT"), scroll="viewport", navOffset=100):
      vbox:
        #xalign 0.5
        grid 1 1:        
            style_prefix "chapter_slot"
            xalign 0.5
            yalign 0.5
            $index = 0
            $chapter = chapter_label_names[index][0]
            $chapter_title = chapter_label_names[index][1]
            $chapter_label = chapter_label_names[index][2]
            $chapter_unlocked = chapter_label_names[index][3]
            if chapter_label_names[0][3]:
              button:            
                  action Start(chapter_label)
                  has vbox
                  xalign 0.5
                  text "[chapter_label_names[0][0]]" xalign 0.5
                  text "{i}[chapter_label_names[0][1]]{/i}" xalign 0.5
            else:
              button:            
                  action NullAction()
                  add "gui/misc/icon_locked.png" xalign 0.5 yalign 0.5
              
        
        null height (3 * gui.pref_spacing)
        label "CHAPTER SELECT" xalign 0.5      
        
        null height (1 * gui.pref_spacing)
        
        ## The grid of file slots.
        grid 4 2:
            style_prefix "chapter_slot"
        
            xalign 0.5
            yalign 0.5
        
            spacing gui.slot_spacing
        
            for i in range(8):
                $index = i+1
                $chapter = chapter_label_names[index][0]
                $chapter_title = chapter_label_names[index][1]
                $chapter_label = chapter_label_names[index][2]
                $chapter_unlocked = chapter_label_names[index][3]
                if chapter_unlocked:
                    button:
                        action Start(chapter_label)
                        has vbox
                        xalign 0.5
                        text "[chapter]" xalign 0.5
                        text "{i}[chapter_title]{/i}" xalign 0.5
                else:
                    button:            
                        action NullAction()
                        add "gui/misc/icon_locked.png" xalign 0.5 yalign 0.5
        
        null height (3 * gui.pref_spacing)
        label "ENDINGS" xalign 0.5      
        
        null height (1 * gui.pref_spacing)
        if persistent.BonusEndingUnlocked:
          $endings_shown = 5
        else:
          $endings_shown = 4
        grid endings_shown 1:
            style_prefix "ending_slot"
        
            xalign 0.5
            yalign 0.5
        
            spacing gui.slot_spacing
        
            for i in range(endings_shown):
                $index = i+9
                $chapter = chapter_label_names[index][0]
                $chapter_title = chapter_label_names[index][1]
                $chapter_label = chapter_label_names[index][2]
                $chapter_unlocked = chapter_label_names[index][3]
                if chapter_unlocked:
                    button:
                        action Start(chapter_label)
                        has vbox
                        xalign 0.5
                        text "[chapter]" xalign 0.5
                        text "{i}[chapter_title]{/i}" xalign 0.5
                else:
                    button:            
                        action NullAction()
                        add "gui/misc/icon_locked.png" xalign 0.5 yalign 0.5
                        
    $totalblocks = renpy.count_dialogue_blocks()
    $currentBlocks = renpy.count_seen_dialogue_blocks()
    $percentComplete = round((currentBlocks / float(totalblocks)) * 100.0, 2)
    hbox: 
      xalign 0.5 
      yalign 0.98
      spacing gui.navigation_spacing
      #text "{size=-7}%s%% complete{/size}"%GetCompletionPercentage() xalign 0.5 yalign 0.98
      #textbutton "{color=#ffffff}[currentBlocks] / [totalblocks] = [percentComplete]% Complete{/color}"
      textbutton "{color=#ffffff}[percentComplete]% Complete{/color}"
      add "gui/misc/dot_spacer_big.png" yalign 0.5
      textbutton _("Achievements") action ShowMenu("extra_achievments")
    use extra_nav 
  
style chapter_slot is slot
style chapter_slot_button is slot_button
style chapter_slot_button_text is slot_button_text
style ending_slot is slot

style chapter_slot_button:
  xsize 250
  ysize 65
  
style chapter_slot_button_text:
    ypadding 5
    bold True
  
style ending_slot_button:
  xsize 200
  ysize 65

#screen extra_gallery():   
#    tag menu
#    use extra_nav
#
#screen extra_music_box():  
#    tag menu
#    use extra_nav

screen extra_credits():   
    tag menu
    add "gui/overlay/extras_menu.png"
    use extra_nav
    add "gui/overlay/credits.png"

screen extra_prod_notes():  
    tag menu
    add "gui/overlay/extras_menu.png"
    use extra_nav
    

screen extra_bonus():   
    tag menu
    add "gui/overlay/extras_menu.png"
    use game_menu(_("BONUS"), scroll="viewport", navOffset=100):
      frame:
        xfill True
        background None
      
        vbox:     
          xalign 0.5
          xoffset 10
          style_prefix "chapter_slot"
          spacing gui.pref_spacing
            
          if persistent.Ending1Unlocked and persistent.Ending2Unlocked and persistent.Ending3Unlocked and persistent.Ending4Unlocked and persistent.BonusEndingUnlocked:
            button:            
                action Replay("origin", {}, False) 
                has vbox
                xalign 0.5
                text "extra" xalign 0.5
                text "{i}\"origin\"{/i}" xalign 0.5
          else:
            button:            
                action NullAction()
                add "gui/misc/icon_locked.png" xalign 0.5 yalign 0.5
                
          null height (5 * gui.pref_spacing)
            
          if persistent.Ending1Unlocked and persistent.Ending2Unlocked and persistent.Ending3Unlocked and persistent.Ending4Unlocked: 
            button:            
                action Replay("epilogue", {}, False) 
                has vbox
                xalign 0.5
                text "epilogue" xalign 0.5
                text "{i}\"old times' sake\"{/i}" xalign 0.5
          else:
            button:            
                action NullAction()
                add "gui/misc/icon_locked.png" xalign 0.5 yalign 0.5
             
          if GetEndingCount() >= 3: 
            button:            
                action Replay("jokejournal", {}, False)
                has vbox
                xalign 0.5
                text "extra end" xalign 0.5
                text "{i}gilly's secret journal{/i}" xalign 0.5
          else:
            button:            
                action NullAction()
                add "gui/misc/icon_locked.png" xalign 0.5 yalign 0.5
              
          if GetEndingCount() >= 1:
            button:            
                action Replay("bonus", {}, False) 
                has vbox
                xalign 0.5
                text "insider content" xalign 0.5
                text "{i}production jokes{/i}" xalign 0.5
          else:
            button:            
                action NullAction()
                add "gui/misc/icon_locked.png" xalign 0.5 yalign 0.5
               
    
    use extra_nav

#-------------------------------------------------------         

init -2:
  transform ScrollUp:
      yalign 1.0
      linear 4.0 yalign 0.1
    
init python:
    #Achievments
    achievement_list = ["Playing as an Adult",
                          "Angry Start",
                          "Mother's Intuition",
                          "Cynical Mother",
                          "Justice Fighter",
                          "A Grudge",
                          "Insensitive",
                          "Nonchalant",
                          "Catherine's 24k",
                          "Bull by the Horns",
                          "The Promise",
                          "Freedom",
                          "The Talk",
                          "The Creature",
                          "Filthy Colours",
                          "Domestic Abuse",
                          "Sacrilege and Sex",
                          "Marquis de Sade",
                          "Incomplete Journal",
                          "More Entries to unlock",
                          "Unlocked all entries",
                          "Green-Eyed",
                          "Monster",
                          "Spectral Handjob",
                          "Oral Sex from Hell",
                          "Nightmare Fuel",
                          "Jealousy",
                          "Bloody Cupid",
                          "Wet Dream Gone Bad",
                          "Does not Form Scars",
                          "Victim Mentality",
                          "Father and Child",
                          "Love is my Drug",
                          "Sound Advice",
                          "New Beginnings",
                          "Agape's Blessing",
                          "Emilie's Fate",
                          "Jealous Catherine",
                          "Guilleme's Soliloquy",
                          "What makes a good parent?",
                          "Dysfunctional Family",
                          "Mother's Past",
                          "Mother",
                          "Little Thief",
                          "Closure",
                          "Love is Bittersweet",
                          "Guilleme's Redemption",
                          "Poison and Cure",
                          "Play it Again",
                          "Never Pure",
                          "Dedication!",
                          "Dark Fairytale",
                          "Pat the Bunny",
                          "Drawing Blood",
                          "Punisher",
                          "Angel of Vengeance",
                          "Squick",
                          "Fan Disservice",
                          "Fourth Wall",
                          "Emptiness",
                          "Hostage",
                          "Implied Incest",
                          "This should have been a comedy",
                          "Modern Day Cupid",
                          "Unlocked All Endings",
                          "Unlocked all of Guilleme's entries",
                          "You don't mean..?", ]
    #Galleries settings - start
    #list the CG gallery images here:
    gallery_cg_items = ["bg rchurch",
                        "bg cfirstpiano",
                        "bg ckidg",
                        "bg rawe",
                        "bg csuicide3",
                        #chap2
                        "bg grhug",  
                        "bg rpow",
                        "bg rosachoke",
                        "bg rosachokesafe",
                        "bg needles",
                        "bg needlessafe",
                        #piano
                        "bg gchappy",
                        #sweet
                        "bg rcbed",
                        "bg rcsweet3",
                        "bg cgbed",
                        #darktimes
                        "bg gcsexay",
                        "bg gcsexay2",
                        "bg gcneckiss",
                        "bg gscary",
                        "bg cupidsexay",
                        #cathdown
                        "bg cathcrazy",
                        "bg cathscratch",
                        "bg cathscratchsafe",
                        #chap6
                        "bg scaredrosa",
                        "bg rgdread",
                        #chap7
                        "bg gattacks",
                        #chap8
                        "bg angrycupid3",
                        #end01
                        "bg gclutch2",
                        #badend
                        "bg rgtension",
                        "bg rgseduce",
                        "bg rosacray",
                        #end 04
                        "bg gdiesdagger",
                        "bg gdiesdaggersafe",
                        "bg gdiesknife",
                        "bg gdiesknifesafe",
                        "bg rgchoke",
                        "bg guilchoke",
                        #end02
                        "bg gdiespeace",
                        "bg gdiespeace2kiss",
                        #end03
                        "bg rgcarry",
                        #secret end
                        "bg rgkiss",
                        "bg rgdeepkiss",
                        "drunkpic", ]
    MatureGalleryList = ["",
                        "",
                        "",
                        "",
                        "Mature", 
                        #chap2
                        "",  
                        "",
                        "Mature",
                        "",
                        "Mature",
                        "",
                        #piano
                        "",
                        #sweet
                        "",
                        "",
                        "",
                        #darktimes
                        "",
                        "Mature",
                        "Mature",
                        "",
                        "",
                        #cathdown
                        "",
                        "Mature",
                        "",
                        #chap6
                        "",
                        "",
                        #chap7
                        "Mature",
                        #chap8
                        "",
                        #end01
                        "",
                        #badend
                        "",
                        "",
                        "",
                        #end 04
                        "Mature",
                        "",
                        "Mature",
                        "",
                        "",
                        "",
                        #end02
                        "",
                        "",
                        #end03
                        "",
                        #secret end
                        "",
                        "",
                        ""]    
    
    
    #list the Music Box songss here 
    gallery_music_items =  ["sfx/intro2.ogg",
                            "sfx/churchraw.ogg",
                            "sfx/partyraw.ogg",
                            "sfx/catsfirstperf.ogg",
                            "sfx/waltz.ogg",
                            "sfx/garden.ogg",
                            "sfx/quietsadness.ogg",
                            "sfx/sorrow.ogg",
                            "sfx/cathsadsong.ogg",
                            "sfx/fastsong.ogg",
                            "sfx/library.ogg",
                            "sfx/nature.ogg",
                            "sfx/friends.ogg",
                            #demo
                            "sfx/catsaria.ogg",
                            "sfx/sweetune2.ogg",
                            "sfx/loverstango.ogg",
                            "sfx/mellow.ogg",
                            "sfx/spooks.ogg",
                            "sfx/journal0.ogg",
                            "sfx/night2.ogg",
                            "sfx/darksexy.ogg",
                            "sfx/cathsfinal.ogg",
                            "sfx/bitterness.ogg",
                            "sfx/sadness.ogg",
                            "sfx/gbeat.ogg",
                            "sfx/journal.ogg",
                            "sfx/rosadecides.ogg",
                            "sfx/nightterror.ogg",
                            "sfx/intro.ogg",
                            "sfx/confront.ogg",
                            "sfx/spider.ogg",
                            "sfx/badend.ogg",
                            "sfx/bittersweet.ogg" ]
    gallery_music_text =  ["{size=-4}\"tea leaf melancholy\"\n       {i}krichotomy{/i}{/size}",
                            "{size=-4}         \"agnus dei\"\n{i}      william byrd{/i}{/size}",
                            "{size=-4}   \"goldberg var 1a1\"\n            {i}j.s. bach{/i}{/size}",
                            "{size=-4}         \"liebesleid\"\n{i}sergei rachmaninoff{/i}{/size}",
                            "{size=-4}           \"parisian\"\n{i}      kevin mcleod{/i}{/size}",
                            "{size=-4}            \"garden\"\n{i}         yasupochi{/i}{/size}",
                            "{size=-4}  \"to be continued2\"\n{i}         yasupochi{/i}{/size}",
                            "{size=-4}           \"despair\"\n{i}         yasupochi{/i}{/size}",
                            "{size=-4}          \"l'enclume\"\n{i}      circus marcus{/i}{/size}",
                            "{size=-4} \"goldberg var 14a2\"\n            {i}j.s. bach{/i}{/size}",
                            "{size=-4}    \"fermer les yeux\"\n      {i}circus marcus{/i}{/size}",
                            "{size=-4}         \"ittekimasu\"\n          {i}yasupochi{/i}{/size}",
                            "{size=-4}            \"friends\"\n {i}         jon coyle{/i}{/size}",
                            "{size=-4}       \"winter wind\"\n     {i}frédéric chopin{/i}{/size}",
                            "{size=-4}             \"muck\"\n{i}         yasupochi{/i}{/size}",
                            "{size=-4}            \"sardana\"\n {i}      kevin mcleod{/i}{/size}",
                            "{size=-4}             \"sasasa\"\n {i}  nagami yukitaka{/i}{/size}",
                            "{size=-4} \"spooky music box\"\n          {i}speedenza{/i}{/size}",
                            "{size=-4}         \"alfonsina\"\n{i}         yasupochi{/i}{/size}",
                            "{size=-4}       \"lonely town\"\n         {i}yasupochi{/i}{/size}",
                            "{size=-4}            \"urgana\"\n{i}djinn (hanchi remix){/i}{/size}",
                            "{size=-4}  \"pompas de jabón\"\n     {i}circus marcus{/i}{/size}",
                            "{size=-4}         \"bitterness\"\n{i}        autumnelm{/i}{/size}",
                            "{size=-4}   \"goodbye, aunt k\"\n          {i}yasupochi{/i}{/size}",
                            "{size=-4}         \"loop (mix)\"\n          {i}wikbeats{/i}{/size}",
                            "{size=-4}        \"la chambre\"\n      {i}circus marcus{/i}{/size}",
                            "{size=-4}  \"la tapa del jueves\"\n       {i}circus marcus{/i}{/size}",
                            "{size=-4}        \"night terror\"\n{i}        autumn elm{/i}{/size}",
                            "{size=-4}  \"la tapa del viernes\"\n     {i}circus marcus{/i}{/size}",
                            "{size=-4}          \"snowdrop\"\n       {i}kevin mcleod{/i}{/size}",
                            "{size=-4}        \"spider eyes\"\n      {i}kevin mcleod{/i}{/size}",
                            "{size=-4}         \"ice demon\"\n       {i}kevin mcleod{/i}{/size}",
                            "{size=-4}           \"sorrow\"\n        {i}yasupochi{/i}{/size}",]
    #how many rows and columns in the gallery screens?
    gal_rows = 4
    gal_cols = 2
    #thumbnail size in pixels:
    thumbnail_x = 234
    thumbnail_y = 132
    #the setting above (267x150) will work well with 16:9 screen ratio. Make sure to adjust it, if your are using 4:3 or something else.
    #Galleries settings - end
    
    gal_cells = gal_rows * gal_cols    
    g_cg = Gallery()
    for gal_item in gallery_cg_items:    
      g_cg.button(gal_item + " butt") 
      g_cg.image(gal_item)
      g_cg.unlock(gal_item)       
      if gal_item == "bg rchurch":
        g_cg.transform(ScrollUp)
    g_cg.transition = fade
    cg_page=0
    
    g_mr = MusicRoom(fadeout=1.0)
    #add title screen music
    AlwaysUnlockedCount = 3
    i = 0
    for mr_item in gallery_music_items:
      if (i < AlwaysUnlockedCount):
        g_mr.add(mr_item, always_unlocked=True)
        i+=1
      else:
        g_mr.add(mr_item)
    g_mr.transition = fade
    mr_page=0
    
    
init +1 python:
    #Here we create the thumbnails. We use a special "locked" image for CGs to prevent spoilers.
    for gal_item in gallery_cg_items:
        renpy.image (gal_item + " butt", im.Scale(im.Crop(ImageReference(gal_item),0,0, 1280, 720,), thumbnail_x, thumbnail_y))

#-------------------------------------------------------  


screen extra_gallery():   
    tag menu
    add "gui/overlay/extras_menu.png"
    use game_menu(_("GALLERY"), scroll=None, navOffset=100):
    
      vbox:
        $ columns = 4
        $ rows = 2
        $ j = 0
        $ next_cg_page = cg_page + 1     
        $ prev_cg_page = cg_page - 1          
        if next_cg_page > int(len(gallery_cg_items)/gal_cells):
            $ next_cg_page = int(len(gallery_cg_items)/gal_cells)       
        if prev_cg_page < 0:
            $ prev_cg_page = 0
        hbox:
          style_prefix "page"

          xalign 0.5

          spacing gui.page_spacing
          
          textbutton _("PREVIOUS") action [SetVariable('cg_page', prev_cg_page), SensitiveIf(cg_page > 0)]
          add "gui/misc/dot_spacer_big.png" yalign 0.5

          ## range(1, 10) gives the numbers from 1 to 9.
          for page in range(1, 7):
              textbutton "[page]" action [SetVariable('cg_page', page-1)]#, ShowMenu("extra_gallery")]    

          add "gui/misc/dot_spacer_big.png" yalign 0.5
          textbutton _("NEXT") action [SetVariable('cg_page', next_cg_page), SensitiveIf(cg_page < next_cg_page)]
        frame:          
          background None
          for gal_item in gallery_cg_items:
              $ j += 1
              $index = j
              if (index > int(columns*rows)):
                $index = j - int(columns*rows*cg_page)
              $ipos = 160*int((index-1)/columns)
              $index = ((j-1)%columns) + 1
              $jpos = 260*(index-1)
              if j <= (cg_page+1)*gal_cells and j>cg_page*gal_cells: 
                add g_cg.make_button(gal_item + " butt", gal_item + " butt", "gui/button/galbox_insensitive.png",  xpos=5+jpos, ypos=(40+ipos), idle_border="gui/button/galbox_idle.png", hover_border="gui/button/galbox_hover.png", background=None, bottom_margin=24)
                if ((MatureGalleryList[j-1] == "Mature") and (persistent.adult == False)):
                     text "{color=#f00}{size=-8}Mature{/size}{/color}" xpos 185+jpos ypos (156+ipos)
    use extra_nav
            


screen extra_music_box():  
    tag menu
    add "gui/overlay/extras_menu.png"
    use game_menu(_("MUSIC BOX"), scroll=None, navOffset=100):
    
      vbox:
      
        $ columns = 4
        $ rows = 2
        $ j = 0
        $ next_mr_page = mr_page + 1     
        $ prev_mr_page = mr_page - 1          
        if next_mr_page > int(len(gallery_music_items)/gal_cells):
            $ next_mr_page = int(len(gallery_music_items)/gal_cells)       
        if prev_mr_page < 0:
            $ prev_mr_page = 0
        hbox:
          style_prefix "page"

          xalign 0.5

          spacing gui.page_spacing
          
          textbutton _("PREVIOUS") action [SetVariable('mr_page', prev_mr_page), SensitiveIf(mr_page > 0)]
          add "gui/misc/dot_spacer_big.png" yalign 0.5

          ## range(1, 10) gives the numbers from 1 to 9.
          for page in range(1, 6):
              textbutton "[page]" action [SetVariable('mr_page', page-1)]

          add "gui/misc/dot_spacer_big.png" yalign 0.5
          textbutton _("NEXT") action [SetVariable('mr_page', next_mr_page), SensitiveIf(mr_page < next_mr_page)]
        frame:          
          background None
          for gal_item in gallery_music_items: #50x38
              $ j += 1
              $index = j
              if (index > int(columns*rows)):
                $index = j - int(columns*rows*mr_page)
              $ipos = 160*int((index-1)/columns)
              $index = ((j-1)%columns) + 1
              $jpos = 260*(index-1)
              if j <= (mr_page+1)*gal_cells and j>mr_page*gal_cells: 
                imagebutton auto "gui/button/mrbox_%s.png" xpos 5+jpos ypos (40+ipos)focus_mask None action g_mr.Play(gal_item)
                if g_mr.is_unlocked(gallery_music_items[j-1]):
                  text gallery_music_text[j-1] xpos 30+jpos ypos (120+ipos)
                else:
                  text "{size=-4}Locked{/size}" xpos 90+jpos ypos (120+ipos)
    use extra_nav
            

screen extra_achievments():  
    tag menu
    add "gui/overlay/extras_menu.png"
    use game_menu(_("ACHIEVEMENTS"), scroll="viewport", navOffset=100):
      $totalAchievements = len(achievement_list)
      $currentAchievements = 0
      vbox:
        xfill True
        for achievo in achievement_list:
        
          if not achievement.has(achievo):
              text "{color=#444444}[achievo]{/color}" xalign 0.5
          else:
            text "{color=#ffffff}[achievo]{/color}" xalign 0.5
            $currentAchievements+=1
        null height (1 * gui.pref_spacing)
        text "You have earned [currentAchievements] / [totalAchievements] achievements" xalign 0.5
    use extra_nav

################################################################################


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

    if quick_menu:

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
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

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
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

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
    xsize 600
