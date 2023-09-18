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
    outlines [ (absolute(2), "#7334b6", absolute(0), absolute(0)) ]
    insensitive_outlines [ (absolute(2), "#594e63", absolute(0), absolute(0)) ]


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)
    outlines [ (absolute(2), "#7334b6", absolute(0), absolute(0)) ]

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
    #base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    #thumb "gui/slider/horizontal_[prefix_]thumb.png"
    left_bar Frame("gui/slider/horizontal_bar_full.png", gui.slider_borders, tile=gui.slider_tile)
    right_bar Frame("gui/slider/horizontal_bar_empty.png", gui.slider_borders, tile=gui.slider_tile)

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


style caption_med:
    #font gui.adv_font_face
    size 34 #* 0.7
    #bold True
    color "#000000"
    #outlines [ (absolute(1), "#ffffff", absolute(0), absolute(0)) ]
    
screen qm_tooltip(ttcontent,ttxpos,ttypos):
    zorder 9999
    text ttcontent:
        style "caption_med"
        xpos ttxpos ypos ttypos
        #at gui_fade_inout(0.0,0.3)


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
    outlines [ (absolute(2), "#270e3c", absolute(0), absolute(0)) ]
    

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
    background Frame("gui/frame_idle.png", 25, 25)
    hover_background Frame("gui/frame_hover.png", 25, 25)

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines [ (absolute(2), "#ffffff", absolute(0), absolute(0)) ]
    hover_outlines [ (absolute(2), "#270e3c", absolute(0), absolute(0)) ]


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
    #for betatesting
    #use renedit_overlay

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.7
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Options") action ShowMenu('preferences') 
            if feature_unlock_calendar:
              textbutton _("Calendar") action ShowMenu('show_calendar')
            if feature_unlock_roster:
              textbutton _("Roster") action ShowMenu('class_roster') 


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

screen navigation(_useReturn=True, _spookleYOffset=0):

    #vbox:
        #style_prefix "navigation"

        #xpos gui.navigation_xpos
        #yalign 0.5

        #spacing gui.navigation_spacing
        
        #button locations
        $startxpos = 400
        $xoffset = 00
        $xincrement = 180
        
        #tooltip location
        $ttx = 600
        $tty = 205 + _spookleYOffset
        
        if main_menu:
            #increase increment for main menu buttons
            $xincrement = 180
            if not _useReturn: 
              $xincrement = 200

            #textbutton _("Start") action Start()
            imagebutton auto "gui/button/start_%s.png" xpos startxpos+xoffset ypos 840 :
              hovered [Show("qm_tooltip",ttcontent="How do I start the game?",ttxpos=ttx,ttypos=tty)]
              unhovered Hide("qm_tooltip") 
              action  [Hide("qm_tooltip"),  Start()]
            $xoffset = xoffset + xincrement
            
            imagebutton auto "gui/button/box_%s.png" xpos startxpos+xoffset ypos 840 :
              hovered [Show("qm_tooltip",ttcontent="Where do I find the extras?",ttxpos=ttx,ttypos=tty)]
              unhovered Hide("qm_tooltip") 
              action  [Hide("qm_tooltip"),  ShowMenu("cg_gallery")]
            $xoffset = xoffset + xincrement

        else:

            #textbutton _("History") action ShowMenu("history")
            imagebutton auto "gui/button/history_%s.png" xpos startxpos+xoffset ypos 840 :
              hovered [Show("qm_tooltip",ttcontent="How do see into the past?",ttxpos=ttx,ttypos=tty)]
              unhovered Hide("qm_tooltip") 
              action  [Hide("qm_tooltip"),  ShowMenu("history")]
            $xoffset = xoffset + xincrement

            #textbutton _("Save") action ShowMenu("save")

        #textbutton _("Load") action ShowMenu("load")
        imagebutton auto "gui/button/folder_%s.png" xpos startxpos+xoffset ypos 840 :
            hovered [Show("qm_tooltip",ttcontent="How do I load or save the game?",ttxpos=ttx,ttypos=tty)]
            unhovered Hide("qm_tooltip") 
            action  [Hide("qm_tooltip"),  ShowMenu("load")]
        $xoffset = xoffset + xincrement

        #textbutton _("Preferences") action ShowMenu("preferences")
        imagebutton auto "gui/button/options_%s.png" xpos startxpos+xoffset ypos 840 :
            hovered [Show("qm_tooltip",ttcontent="How do I change the settings?",ttxpos=ttx,ttypos=tty)]
            unhovered Hide("qm_tooltip") 
            action  [Hide("qm_tooltip"),  ShowMenu("preferences")]
        $xoffset = xoffset + xincrement

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            #textbutton _("Main Menu") action MainMenu()
            imagebutton auto "gui/button/home_%s.png" xpos startxpos+xoffset ypos 840 :
              hovered [Show("qm_tooltip",ttcontent="How do I return to the start menu?",ttxpos=ttx,ttypos=tty)]
              unhovered Hide("qm_tooltip") 
              action  [Hide("qm_tooltip"),  MainMenu()]
            $xoffset = xoffset + xincrement

        #textbutton _("About") action ShowMenu("about")
        imagebutton auto "gui/button/info_%s.png" xpos startxpos+xoffset ypos 840 :
            hovered [Show("qm_tooltip",ttcontent="How do I find out more information?",ttxpos=ttx,ttypos=tty)]
            unhovered Hide("qm_tooltip") 
            action  [Hide("qm_tooltip"),  ShowMenu("about")]
        $xoffset = xoffset + xincrement

        #if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
        #    textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            #textbutton _("Quit") action Quit(confirm=not main_menu)
            imagebutton auto "gui/button/exit_%s.png" xpos startxpos+xoffset ypos 840  :
              hovered [Show("qm_tooltip",ttcontent="How do I exit the game?",ttxpos=ttx,ttypos=tty)]
              unhovered Hide("qm_tooltip") 
              action  [Hide("qm_tooltip"),  Quit(confirm=not main_menu)]
            $xoffset = xoffset + xincrement
            
        if _useReturn:    
          imagebutton auto "gui/button/return_%s.png" xpos startxpos+xoffset ypos 840  :
            hovered [Show("qm_tooltip",ttcontent="How do I get back?",ttxpos=ttx,ttypos=tty)]
            unhovered Hide("qm_tooltip") 
            action  [Hide("qm_tooltip"),  Return()]
          $xoffset = xoffset + xincrement
          
        
        if feature_unlock_roster:
          imagebutton auto "gui/button/roster_%s.png" xpos 1490 ypos 140 :
            hovered [Show("qm_tooltip",ttcontent="How do I find out how my students are doing?",ttxpos=ttx,ttypos=tty)]
            unhovered Hide("qm_tooltip") 
            action  [Hide("qm_tooltip"),  ShowMenu("class_roster")]


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    
    
screen navigation_gameplay(_useReturn=True, _spookleYOffset=0):

        #button locations
        $startxpos = 400
        $xoffset = 00
        $xincrement = 250
        
        #tooltip location
        $ttx = 600
        $tty = 205 + _spookleYOffset
        
        if feature_unlock_roster:
          imagebutton auto "gui/button/roster_%s.png" xpos startxpos+xoffset ypos 840 :
            hovered [Show("qm_tooltip",ttcontent="How do I find out how my students are doing?",ttxpos=ttx,ttypos=tty)]
            unhovered Hide("qm_tooltip") 
            action  [Hide("qm_tooltip"),  ShowMenu("class_roster")]
          $xoffset = xoffset + xincrement
        
        if feature_unlock_status_others:
          imagebutton auto "gui/button/contacts_%s.png" xpos startxpos+xoffset ypos 840 :
              hovered [Show("qm_tooltip",ttcontent="Who else do I know?",ttxpos=ttx,ttypos=tty)]
              unhovered Hide("qm_tooltip") 
              action  [Hide("qm_tooltip"),  ShowMenu("character_status_bahini")]
          $xoffset = xoffset + xincrement

        if feature_unlock_status_self:
          imagebutton auto "gui/button/self_%s.png" xpos startxpos+xoffset ypos 840 :
              hovered [Show("qm_tooltip",ttcontent="How am I doing?",ttxpos=ttx,ttypos=tty)]
              unhovered Hide("qm_tooltip") 
              action  [Hide("qm_tooltip"),  ShowMenu("character_status_caragh")]
          $xoffset = xoffset + xincrement
        
        if feature_unlock_calendar:
          imagebutton auto "gui/button/calendar_%s.png" xpos startxpos+xoffset ypos 840 :
            hovered [Show("qm_tooltip",ttcontent="How do I find out whats happening this month?",ttxpos=ttx,ttypos=tty)]
            unhovered Hide("qm_tooltip") 
            action  [Hide("qm_tooltip"),  ShowMenu("show_calendar")]
          $xoffset = xoffset + xincrement

        #imagebutton auto "gui/button/chat_%s.png" xpos startxpos+xoffset ypos 840 :
        #    hovered [Show("qm_tooltip",ttcontent="How do I find out more information?",ttxpos=ttx,ttypos=tty)]
        #    unhovered Hide("qm_tooltip") 
        #    action  [Hide("qm_tooltip"),  ShowMenu("about")]
        #$xoffset = xoffset + xincrement
            
        if _useReturn:    
          imagebutton auto "gui/button/return_%s.png" xpos startxpos+xoffset ypos 840  :
            hovered [Show("qm_tooltip",ttcontent="How do I get back?",ttxpos=ttx,ttypos=tty)]
            unhovered Hide("qm_tooltip") 
            action  [Hide("qm_tooltip"),  Return()]
          $xoffset = xoffset + xincrement
          
        imagebutton auto "gui/button/options_%s.png" xpos 1490 ypos 140 :
            hovered [Show("qm_tooltip",ttcontent="How do I change the settings?",ttxpos=ttx,ttypos=tty)]
            unhovered Hide("qm_tooltip") 
            action  [Hide("qm_tooltip"),  ShowMenu("preferences")]
    

screen extra_navigation(_useReturn=True, _spookleYOffset=0):

        #button locations
        $startxpos = 400
        $xoffset = 00
        $xincrement = 250
        
        #tooltip location
        $ttx = 600
        $tty = 205 + _spookleYOffset
        
        imagebutton auto "gui/button/image_%s.png" xpos startxpos+xoffset ypos 840 :
          hovered [Show("qm_tooltip",ttcontent="Where can I see some event CGs?",ttxpos=ttx,ttypos=tty)]
          unhovered Hide("qm_tooltip") 
          action  [Hide("qm_tooltip"),  ShowMenu("cg_gallery")]
        $xoffset = xoffset + xincrement
        
        #imagebutton auto "gui/button/image_%s.png" xpos startxpos+xoffset ypos 840 :
        #  hovered [Show("qm_tooltip",ttcontent="Where can I see some backgrounds?",ttxpos=ttx,ttypos=tty)]
        #  unhovered Hide("qm_tooltip") 
        #  action  [Hide("qm_tooltip"),  ShowMenu("bg_gallery")]
        #$xoffset = xoffset + xincrement
        
        imagebutton auto "gui/button/music_%s.png" xpos startxpos+xoffset ypos 840 :
          hovered [Show("qm_tooltip",ttcontent="How do I listen to music?",ttxpos=ttx,ttypos=tty)]
          unhovered Hide("qm_tooltip") 
          action  [Hide("qm_tooltip"),  ShowMenu("musicbox")]
        $xoffset = xoffset + xincrement
        
        imagebutton auto "gui/button/info_%s.png" xpos startxpos+xoffset ypos 840 :
          hovered [Show("qm_tooltip",ttcontent="How do I find out more information?",ttxpos=ttx,ttypos=tty)]
          unhovered Hide("qm_tooltip") 
          action  [Hide("qm_tooltip"),  ShowMenu("about")]
        $xoffset = xoffset + xincrement        
        
            
        if _useReturn:    
          imagebutton auto "gui/button/return_%s.png" xpos startxpos+xoffset ypos 840  :
            hovered [Show("qm_tooltip",ttcontent="How do I get back?",ttxpos=ttx,ttypos=tty)]
            unhovered Hide("qm_tooltip") 
            action  [Hide("qm_tooltip"),  Return()]
          $xoffset = xoffset + xincrement
    #vbox:
    #    style_prefix "navigation"
    #
    #    xpos gui.navigation_xpos
    #    yalign 0.5
    #
    #    spacing gui.navigation_spacing
    #
    #    textbutton _("CG Gallery") action ShowMenu("cg_gallery") 
    #    textbutton _("BG Gallery") action ShowMenu("bg_gallery") 
    #    textbutton _("Music") action ShowMenu("musicbox") 
    #    textbutton _("Endings") action ShowMenu("endings")       
    #    #textbutton _("About") action ShowMenu("about") 
        
## Extra UI element screens ############################################################

screen time_display(_xpos=0, _ypos=0):
    style_prefix "time"
    add "gui/overlay/time_display.png" xpos _xpos ypos _ypos
    
    hbox: 
      xpos 540 + _xpos
      ypos 300 + _ypos
      vbox:
        xpos -50 
        ypos 20
        text "[current_weather], [current_temp]°" color "#ffffff" 
        text "Somewhere" color "#ffffff" 
      $minutes = GetCurrentMinutes()
      $minutes_text = str(minutes)
      if minutes < 10:
        $minutes_text = "0" + str(minutes)
      text "[current_time_hour]:"+ minutes_text color "#ffffff" size 96
      
style time_text is gui_text

style time_text:
    outlines [ (absolute(2), "#a667db", absolute(0), absolute(0)) ]

screen spookle_display(_xpos=0, _ypos=0):
    add "gui/overlay/spookle_search.png" xpos _xpos ypos _ypos

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu


screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use time_display(600,0)
    use spookle_display(0,0)
    use navigation(_useReturn=False)
    add "gui/logo.png" xpos 300 ypos 220

    #if gui.show_name:
    #
    #    hbox:
    #        style "main_menu_vbox"
    #        text "[config.name!t]":
    #            style "main_menu_title"
    #        #text "[config.version]":
    #        #    style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xpos 730
    ypos 130

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")
    color "#ffffff" 
    size 50

style main_menu_version:
    properties gui.text_properties("version")
    color "#ffffff" 


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, _useAltNavigation=False, _useNoNavigation=False):

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

    #use time_display(660,  -175)
    use spookle_display(0, 560)
    if not _useNoNavigation:
      if _useAltNavigation == "Gameplay":
        use navigation_gameplay(_spookleYOffset=560)
      else:
        if _useAltNavigation == "Extra":
          use extra_navigation(_spookleYOffset=560)
        else:
          use navigation(_spookleYOffset=560)

    #textbutton _("Return"):
    #    style "return_button"

    #    action Return()

    label title xsize 1300 xoffset 170

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
    bottom_padding 165
    top_padding 180

    background "gui/overlay/game_menu.png"
    #background "#123456"

style game_menu_navigation_frame:
    xsize 00
    yfill True
    #background "#121212"

style game_menu_content_frame:
    left_margin 300
    right_margin 300
    top_margin 50
    bottom_margin 150
    #background "#654321"

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    #xpos 75
    ysize 180
    xalign 0.2
    ypos 100

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
    use game_menu(_("About"), scroll="viewport", _useAltNavigation="Extra"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


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
        #tooltip location
        $ttx = 600
        $tty = 205 + 550
        if not main_menu:
            if title == "Save":
              imagebutton auto "gui/button/load_%s.png" xpos 50 ypos 400 :
                  hovered [Show("qm_tooltip",ttcontent="How do I load the game?",ttxpos=ttx,ttypos=tty)]
                  unhovered Hide("qm_tooltip") 
                  action  [Hide("qm_tooltip"),  ShowMenu("load")]
            else:
              imagebutton auto "gui/button/save_%s.png" xpos 50 ypos 400  :
                  hovered [Show("qm_tooltip",ttcontent="How do I save the game?",ttxpos=ttx,ttypos=tty)]
                  unhovered Hide("qm_tooltip") 
                  action  [Hide("qm_tooltip"),  ShowMenu("save")]
        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.3

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
                            
                        
                        #text "Day [current_day]":
                        #    style "slot_name_text"
                        #text "[current_time]":
                        #    style "slot_name_text"
                        #text "[current_difficulty] Mode":
                        #    style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 0.8

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
    ypadding 15

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
    use game_menu(_("Options"), scroll="viewport"):

            $difficulty_rating = GetDifficultyRating()

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        hbox:
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
                    hbox:
                      textbutton _("Unseen Text") action Preference("skip", "toggle")
                      textbutton _("After Choices") action Preference("after choices", "toggle")
                      textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (2 * gui.pref_spacing)

            vbox:
                style_prefix "slider"
                box_wrap True
                xoffset 550

                vbox:
                  spacing  -20
                  hbox:
                    label _("Text Speed") yalign 0.5 xsize 310 text_xalign 1.0
                    null width (1 * gui.pref_spacing)
                    bar value Preference("text speed") yalign 0.5

                  hbox:
                    label _("Auto-Forward Time") yalign 0.5 xsize 310 text_xalign 1.0
                    null width (1 * gui.pref_spacing)
                    bar value Preference("auto-forward time") yalign 0.5

                null height (1 * gui.pref_spacing)
            #hbox:
                #style_prefix "slider"
                #box_wrap True
                vbox:

                  vbox:
                    spacing  -20
                    if config.has_music:

                        hbox:
                            label _("Music") yalign 0.5 xsize 310  text_xalign 1.0
                            null width (1 * gui.pref_spacing)
                            bar value Preference("music volume") yalign 0.5

                    if config.has_sound:


                        hbox:
                            label _("Sound") yalign 0.5 xsize 310  text_xalign 1.0
                            null width (1 * gui.pref_spacing)
                            bar value Preference("sound volume") yalign 0.5

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound) yalign 0.5


                  #hbox:
                  #  spacing  (2 * gui.pref_spacing)
                  #  if config.has_voice:
                  #
                  #      hbox:
                  #          label _("Voice") yalign 0.5 xsize 110 
                  #          null width (1 * gui.pref_spacing)
                  #          bar value Preference("voice volume") yalign 0.5
                  #
                  #          if config.sample_voice:
                  #              textbutton _("Test") action Play("voice", config.sample_voice)
                  #
                  #  if config.has_music or config.has_sound or config.has_voice:
                  #      null height gui.pref_spacing
                  #
                  #      textbutton _("Mute All"):
                  #          action Preference("all mute", "toggle")
                  #          style "mute_all_button"

    label _("Text Settings")  xpos 800 ypos 370
    label _("Audio Settings") xpos 800 ypos 540
    vbox:
        style_prefix "check"
        label _("Gameplay Features")
        xpos 300
        ypos 350
        vbox:
          xsize 500
          xoffset 50
          textbutton _("Mood Multiplier") action ToggleVariable("feature_unlock_bonus_Mood")
          textbutton _("Stress Penalty") action ToggleVariable("feature_unlock_penalty_stress")
          textbutton _("Back to Back Penalty") action ToggleVariable("feature_unlock_penalty_backToBack")
          textbutton _("Score Degradation Penalty") action ToggleVariable("feature_unlock_penalty_ScoreDegradation")
          
        label _("Expected Difficulty: [difficulty_rating]") xsize 500 yoffset -10


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox
style pref_hbox is hbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox
style radio_hbox is pref_hbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox
style check_hbox is pref_hbox

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
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338
    
style pref_hbox:
    xsize 538

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    background "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    background "gui/button/check_[prefix_]foreground.png"

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
    
style mute_all_button:
    xsize 300


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

define gui.history_allow_tags = { "alt", "noalt" }


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
    outlines [ (absolute(2), "#7334b6", absolute(0), absolute(0)) ]


style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    outlines [ (absolute(2), "#7334b6", absolute(0), absolute(0)) ]

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

                #textbutton _("Yes") action yes_action
                imagebutton auto "gui/button/confirm_yes_%s.png" action yes_action
                #textbutton _("No") action no_action
                imagebutton auto "gui/button/confirm_no_%s.png" action no_action

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
    xalign .5
    yalign .5

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

    if nvl_mode == "phone":
        use PhoneDialogue(dialogue, items)
    else:
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
                    at(sshake)


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

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900


################################################################################
## Special Screens
################################################################################

init:
        
    transform moving_points:
        zoom 0.0
        align (0.5, 0.5)
        alpha 0.0
        parallel:
            linear 0.5 zoom 1.0
            linear 0.5 zoom 0.9
            repeat
        parallel:
            linear 1.0 alpha 1.0
        
    transform spinner_base:
        zoom 0.0
        align (0.5, 0.5)
        rotate 0.0
        alpha 0.0
        parallel:
            linear 1.0 rotate 360
        parallel:
            linear 1.0 zoom 1.0
        parallel:
            linear 1.0 alpha 1.0
    
    transform spinner_data:
        zoom 0.0
        align (0.5, 0.5)
        rotate 0.0
        alpha 0.0
        parallel:
            linear 1.0 rotate 360
        parallel:
            pause 1.0
            linear 0.5 zoom 1.0
        parallel:
            linear 2.0 alpha 1.0
                
    transform spinner_labels:
        zoom 0.0
        align (0.5, 0.5)
        alpha 0.0
        parallel:
            linear 1.0 zoom 1.0
        parallel:
            linear 1.0 alpha 1.0

screen character_status(_character="???", _showScores=False):
    tag menu
    style_prefix "about"
    #Update values
    python:
        animated_spider_web = RadarChart(
            size=300,
            values=[_character.History, _character.Science, _character.Math, _character.Literacy, _character.Language,_character.Geography],
            max_value=100,
            labels = [
                Text("History: " + GetGradeTextColored(_character.History)),
                Text("Science: " + GetGradeTextColored(_character.Science)),
                Text("Math: " + GetGradeTextColored(_character.Math)),
                Text("Literacy: " + GetGradeTextColored(_character.Literacy)),
                Text("Language: " + GetGradeTextColored(_character.Language)),
                Text("Geography: " + GetGradeTextColored(_character.Geography))
            ],
            data_colour=(115, 52, 182, 255),
            line_colour=(77, 6, 136, 255),
            background_colour=(88, 82, 74, 0),
            lines={"webs": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
            visible={"base":False}
        )
    
    use game_menu(_("Status: "+_character.Name), scroll="viewport", _useAltNavigation="Gameplay"):
      $Relationship = _character.Relationship
      $Mood = _character.Mood
      #Only show stats for Class average
      if _character.Name == "Class Average":
        $_showScores = True
      else:
        hbox:
          vbox:
            add "gui/roster/"+_character.Name.lower()+"_photo.png"
            if _character.Job == "Student":
              if _showScores:
                textbutton "Show Bio" action ShowMenu("character_status", _character, False) background Frame("gui/frame_idle.png", 25, 25) padding(20,5,20,5)
              else:
                textbutton "Show Scores" action ShowMenu("character_status", _character, True) background Frame("gui/frame_idle.png", 25, 25) padding(20,5,20,5)
          null width (2 * gui.pref_spacing)
          if not _showScores:
            vbox:
              spacing 50
              vbox:
                label "[_character.Name]"          
                
                text "Age: [_character.Age]"
                text "Gender: [_character.Gender]"
                text "Species: [_character.Species]"
                if not _character.Personality == "":
                  text "Personality: [_character.Personality]"
                if not _character.Job == "Student":
                  text "Job: [_character.Job]"
                #text "Relationship: [Relationship]"
                text "Favourite Subject: [_character.FavouriteSubject]"
                text "Worst Subject: [_character.WorstSubject]"
                if not _character.Notes == "" and not _character.Job == "Student":
                  text "Bahini's Notes: [_character.Notes]" xsize 800
                elif not _character.Notes == "":
                  text "Bahini's Notes: [_character.Notes]" xsize 600
                #text "Mood: [Mood]"
                #hbox:
                #  $History = _character.History
                #  text "History: [History] "
                #  $Science = _character.Science
                #  text "Science: [Science] "
                #  $Math = _character.Math
                #  text "Math: [Math] "
                #  $Literacy = _character.Literacy
                #  text "Literacy: [Literacy] "
                #  $Language = _character.Language
                #  text "Language: [Language] "
                #  $Geography = _character.Geography
                #  text "Geography: [Geography] "
    if feature_unlock_bonus_Mood and _character.Job == "Student":
      vbox: 
        xpos 1450 
        ypos 265
        spacing 40
        if Mood >= 90:
          label "{color=#46f018}x[max_multiplier]{/color}"
        else:
          label "x[max_multiplier]"
        if Mood >= 70 and Mood < 90:
          label "{color=#46f018}x[high_multiplier]{/color}" 
        else:
          label "x[high_multiplier]" 
        if Mood > 0 and Mood < 70:
          label "{color=#46f018}x[std_multiplier]{/color}"
        else:
          label "x[std_multiplier]"
        #if Mood > 90:
        #  label "{color=#f02318}x[low_multiplier]{/color}"
        #else:
        #  label "x[low_multiplier]"
        if Mood <= 0:
          label "{color=#f02318}x[min_multiplier]{/color}" 
        else:
          label "x[min_multiplier]" 
    hbox:  
      xpos 1350
      ypos 120
      if _character.Job == "Student":
        vbox:
          text "Mood" xalign 0.5
          add "gui/notify/happy.png" xalign 0.5
          vbar:
            xalign 0.5
            #style "status_bar"
            value Mood
            range 100
            ysize 300
          add "gui/notify/unhappy.png" xalign 0.5
        
      #if not _character.Name == "Class Average":
      #  vbox:
      #    #yoffset 50
      #    text "Closeness" xalign 0.5
      #    vbar:
      #      xalign 0.5
      #      #style "status_bar"
      #      value Relationship
      #      range 100
      #      ysize 300
      #    add "gui/notify/relationship_pos.png" xalign 0.5
    
    if _character.Job == "Student" and _showScores:
      frame:
            background None
            xysize (400, 400)
            xpadding 0
            ypadding 0
            xpos 800
            ypos 250
            add animated_spider_web.chart_base at spinner_base
            add animated_spider_web.chart_data at spinner_data
            add animated_spider_web.chart_lines at spinner_base
            add animated_spider_web.chart_labels at spinner_labels
            
#style status_bar:
  #ysize 200
  

screen character_status_side(_characterInfo="???", _showScores=False, _job="Student"):
    tag menu
    style_prefix "about"
    #Update values (use average scores for side students)
    $GenCharacter = [x for x in List_side_characters if x.Name == _characterInfo[0]]
    python:
        animated_spider_web = RadarChart(
            size=300,
            values=[GenCharacter[0].History, GenCharacter[0].Science, GenCharacter[0].Math, GenCharacter[0].Literacy, GenCharacter[0].Language,GenCharacter[0].Geography],
            max_value=100,
            labels = [
                Text("History: " + GetGradeTextColored(GenCharacter[0].History)),
                Text("Science: " + GetGradeTextColored(GenCharacter[0].Science)),
                Text("Math: " + GetGradeTextColored(GenCharacter[0].Math)),
                Text("Literacy: " + GetGradeTextColored(GenCharacter[0].Literacy)),
                Text("Language: " + GetGradeTextColored(GenCharacter[0].Language)),
                Text("Geography: " + GetGradeTextColored(GenCharacter[0].Geography))
            ],
            data_colour=(115, 52, 182, 255),
            line_colour=(77, 6, 136, 255),
            background_colour=(88, 82, 74, 0),
            lines={"webs": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
            visible={"base":False}
        )
        
    $titlename = _characterInfo[0]
    if _characterInfo[0] == "Achilles, Adonis, Atlas":
      $titlename = "{size=-30}Achilles, Adonis, Atlas{/size}"
    use game_menu(_("Status: " + titlename), scroll="viewport", _useAltNavigation="Gameplay"):
      #$Relationship = _character.Relationship
      $Mood = GenCharacter[0].Mood
      #Only show stats for Class average
      
      hbox:
        vbox:
          add "gui/roster/side_photo.png" #default pic for side characters
          if _job == "Student":
            if _showScores:
              textbutton "Show Bio" action ShowMenu("character_status_side", _characterInfo, False) background Frame("gui/frame_idle.png", 25, 25) padding(20,5,20,5)
            else:
              textbutton "Show Scores" action ShowMenu("character_status_side", _characterInfo, True) background Frame("gui/frame_idle.png", 25, 25) padding(20,5,20,5)
        null width (2 * gui.pref_spacing)
        if not _showScores:
          vbox:
            spacing 50
            vbox:
              label "[_characterInfo[0]]"          
              
              text "Age: [_characterInfo[2]]"
              text "Gender: [_characterInfo[1]]"
              text "Species: [_characterInfo[3]]"
              text "Personality: [_characterInfo[4]]"
              if not _job == "Student":
                text "Job: [_job]"
              text "Favourite Subject: [_characterInfo[6]]"
              text "Worst Subject: [_characterInfo[7]]"
              text "Bahini's Notes: [_characterInfo[5]]" xsize 600
     
      #spacing 100
    if feature_unlock_bonus_Mood  and _character.Job == "Student":
      vbox: 
        xpos 1450 
        ypos 265
        spacing 40
        if Mood >= 90:
          label "{color=#46f018}x[max_multiplier]{/color}"
        else:
          label "x[max_multiplier]"
        if Mood >= 70 and Mood < 90:
          label "{color=#46f018}x[high_multiplier]{/color}" 
        else:
          label "x[high_multiplier]" 
        if Mood > 0 and Mood < 70:
          label "{color=#46f018}x[std_multiplier]{/color}"
        else:
          label "x[std_multiplier]"
        #if Mood > 90:
        #  label "{color=#f02318}x[low_multiplier]{/color}"
        #else:
        #  label "x[low_multiplier]"
        if Mood <= 0:
          label "{color=#f02318}x[min_multiplier]{/color}" 
        else:
          label "x[min_multiplier]" 
    
    hbox:  
      xpos 1350
      ypos 120
      if _job == "Student":
        vbox:
          text "Mood" xalign 0.5
          add "gui/notify/happy.png" xalign 0.5
          vbar:
            xalign 0.5
            #style "status_bar"
            value Mood
            range 100
            ysize 300
          add "gui/notify/unhappy.png" xalign 0.5
      
      #No relationship for Side characters
      #if not _character.Name == "Class Average":
      #  vbox:
      #    #yoffset 50
      #    text "Closeness" xalign 0.5
      #    vbar:
      #      xalign 0.5
      #      #style "status_bar"
      #      value Relationship
      #      range 100
      #      ysize 300
      #    add "gui/notify/relationship_pos.png" xalign 0.5
    
    if _job == "Student" and _showScores:
      frame:
            background None
            xysize (400, 400)
            xpadding 0
            ypadding 0
            xpos 800
            ypos 250
            add animated_spider_web.chart_base at spinner_base
            add animated_spider_web.chart_data at spinner_data
            add animated_spider_web.chart_lines at spinner_base
            add animated_spider_web.chart_labels at spinner_labels
            
screen character_status_craig():

  ## This ensures that any other menu screen is replaced.
  tag menu
  use character_status(Character_Craig)
  
screen character_status_hecate():

  ## This ensures that any other menu screen is replaced.
  tag menu
  use character_status(Character_Hecate)
  
screen character_status_sanura():

  ## This ensures that any other menu screen is replaced.
  tag menu
  use character_status(Character_Sanura)
  
screen character_status_average():

  ## This ensures that any other menu screen is replaced.
  tag menu
  use character_status(Character_Average)
  
screen character_nav():
  vbox:
    #$xfill True
    #xsize 1000
    xpos 1400 
    ypos 305
    textbutton "Bahini" action ShowMenu("character_status_bahini") background Frame("gui/frame_idle.png", 25, 25) padding(20,0,20,0) xsize 150 text_xalign 0.5
    textbutton "Nyx" action ShowMenu("character_status_nyx") background Frame("gui/frame_idle.png", 25, 25) padding(20,0,20,0) xsize 150 text_xalign 0.5
    if Bahini_Arc_Weekly > 2:
      textbutton "Mog" action ShowMenu("character_status_mog") background Frame("gui/frame_idle.png", 25, 25) padding(20,0,20,0) xsize 150 text_xalign 0.5
    if Una_Arc_Encountered:
      textbutton "Una" action ShowMenu("character_status_una") background Frame("gui/frame_idle.png", 25, 25) padding(20,0,20,0) xsize 150 text_xalign 0.5
    if Jo_Arc_CurrentEvent >= 1:
      textbutton "Jo" action ShowMenu("character_status_jo") background Frame("gui/frame_idle.png", 25, 25) padding(20,0,20,0) xsize 150 text_xalign 0.5
  
  
screen character_status_bahini():

  ## This ensures that any other menu screen is replaced.
  tag menu
  use character_status(Character_Bahini)
  use character_nav
  
screen character_status_nyx():

  ## This ensures that any other menu screen is replaced.
  tag menu
  use character_status(Character_Nyx)
  use character_nav
  
screen character_status_mog():

  ## This ensures that any other menu screen is replaced.
  tag menu
  use character_status(Character_Mog)
  use character_nav
  
screen character_status_una():

  ## This ensures that any other menu screen is replaced.
  tag menu
  use character_status(Character_Una)
  use character_nav
  
screen character_status_jo():

  ## This ensures that any other menu screen is replaced.
  tag menu
  use character_status(Character_Jo)
  use character_nav


screen character_status_caragh():

  ## This ensures that any other menu screen is replaced.
  tag menu
  style_prefix "about"
  $_character = Character_Caragh
  use game_menu(_("Status: Caragh"), scroll="viewport", _useAltNavigation="Gameplay"):
    hbox:  
      add "gui/roster/caragh_photo.png"
      null width (2 * gui.pref_spacing)
      vbox:
          spacing 50
          vbox:
            label "[_character.Name]"          
            
            text "Age: [_character.Age]"
            text "Gender: [_character.Gender]"
            text "Species: [_character.Species]"
            #text "Job: [character.Job]"
            $Relationship = _character.Relationship
            #text "Relationship: [Relationship]"
            text "Favourite Subject: [_character.FavouriteSubject]"
            text "Worst Subject: [_character.WorstSubject]"
            $Mood = _character.Mood
            
  hbox:  
    xpos 1350
    ypos 120
    vbox:
      text "Stress" xalign 0.5
      #text "[_character.Mood]" xalign 0.5
      add "gui/notify/unhappy.png" xalign 0.5
      vbar:
        xalign 0.5
        #style "status_bar"
        value Mood
        range 100
        ysize 300
      add "gui/notify/happy.png" xalign 0.5

  #------------------------------------------------------  
screen class_roster():

    tag menu
    style_prefix "roster"

    use game_menu(_("Class Roster"), scroll=None, _useAltNavigation="Gameplay"):
      
      $newXpos = 130
      $newYpos = 40
      $xOffset = 220
      $yOffset = 160
      
      #vbox:
      #  for character in List_Students_Side2:
      #    text "[character[0]]"
      #    if character[0] == "Bestia":
      #      text "Craig"
      #    if character[0] == "Florence":
      #      text "Hecate"
      #    if character[0] == "Rudolph":
      #      text "Sanura"
        
      
      grid 6 3:
        xpos 50
        ypos 30
        xspacing 20
        yspacing -30
        for character in List_Students_Side2:
          button:
            background "gui/roster/roster_blank_inactive.png" 
            action ShowMenu("character_status_side", _characterInfo=character)
          
            has vbox
            #add "gui/roster/roster_blank_inactive.png" 
            if character[0] == "Achilles, Adonis, Atlas":
              text "[character[0]]" :
                style "roster_button_text" 
                size 20 
                #yoffset 5
            else:
              text "[character[0]]"  :
                style "roster_button_text"
                
            
          if character[0] == "Bestia":
            button:
              background "gui/roster/roster_craig_idle.png" 
              hover_background "gui/roster/roster_craig_hover.png" 
              action ShowMenu("character_status_craig")

              has vbox
              #add 
              text "Craig":
                style "roster_button_text"
          
          if character[0] == "Florence":
            button:
              background "gui/roster/roster_hecate_idle.png" 
              hover_background "gui/roster/roster_hecate_hover.png" 
              action ShowMenu("character_status_hecate", )

              has vbox
              #add "gui/roster/roster_hecate_idle.png" 
              text "Hecate" :
                style "roster_button_text"
              
          if character[0] == "Rudolph":
            button:
              background "gui/roster/roster_sanura_idle.png" 
              hover_background "gui/roster/roster_sanura_hover.png" 
              action ShowMenu("character_status_sanura")

              has vbox
              #add "gui/roster/roster_sanura_idle.png" 
              text "Sanura" :
                style "roster_button_text"
          
        #fill in empty space with null
        null   
        
        button:
          background "gui/roster/roster_average_idle.png" 
          hover_background "gui/roster/roster_average_hover.png" 
          action ShowMenu("character_status_average")

          has vbox
          #add "gui/roster/roster_average.png" 
          text "Class Average":
            style "roster_button_text"  
            size 26 
            yoffset -5
            xoffset -20

#style roster_label is gui_label
#style roster_label_text is gui_label_text
style roster_vbox is vbox
style roster_button is gui_button
style roster_button_text is gui_button_text

#style roster_vbox:
    #xalign 0.5
    #xsize 200
style roster_button:
    #yoffset -15
    #xoffset -50
    #xalign 0.5
    #xsize 200
    xsize 200
    ysize 195
style roster_button_text:
    #xalign 0.5
    #size 22
    #outlines [ (absolute(0), "#ffffff", absolute(0), absolute(0)) ]
    idle_color gui.idle_small_color
    hover_color gui.hover_color
    ypos 140
    
            
  #------------------------------------------------------  
screen show_calendar():

    ## This ensures that any other menu screen is replaced.
    tag menu
    style_prefix "calendar"

    use game_menu(_("Calendar: October"), scroll="viewport", _useAltNavigation="Gameplay"):
      hbox:
        xpos 70
        ypos -10
        spacing 45
        text "Sun"
        text "Mon"
        text "Tue"
        text "Wed"
        text "Thur"
        text "Fri"
        text "Sat"
      grid 7 5:
        xpos 50
        ypos -20
        #xspacing 20
        yspacing -2
        for i in range(1, 36):
          $day = i - 1
          if day > 31:
            $day = day - 31
          if day < 1:
            $day = 30
          if (i > 1 and i <= 32) and (not List_calander_events[day] == ""):
            $dayText = str(day) + "*"
          else:
            $dayText = str(day)
            
          if i-1 == display_date:
            frame:
              xsize 90
              ysize 90
              background Frame("gui/frame_idle.png", 25, 25)
              hover_background Frame("gui/frame_hover.png", 25, 25)
              text str(dayText) xalign 0.5 yalign 0.5
          else:
            if i > 1 and i <= 32:
              button:
                action SetScreenVariable("display_date", day)
                frame:
                  xsize 90
                  ysize 90
                  background Frame("gui/frame_idle.png", 25, 25)
                  hover_background Frame("gui/frame_hover.png", 25, 25)
                  text str(dayText) xalign 0.5 yalign 0.5
            else:
              button:
                #action SetScreenVariable("display_date", day)
                frame:
                  xsize 90
                  ysize 90
                  background Frame("gui/frame_idle.png", 25, 25)
                  hover_background Frame("gui/frame_hover.png", 25, 25)
                  text str(dayText) xalign 0.5 yalign 0.5
            
    vbox:
        style_prefix "history"
        xpos 900
        ypos 300
        xsize 400
        #text "Day [display_date]"
        
        if display_date == current_day:
          text "Day [display_date] (Today)"
          null height (2 * gui.pref_spacing)
          text "Teaching: [morning_class]"
          text "Teaching: [afternoon_class]"
        else:
          text "Day [display_date]"
        if display_date < current_day:
          $outcomes = GetClassOutcomes(display_date-1)
          $mclass = outcomes[0]
          $aclass = outcomes[1]
          null height (2 * gui.pref_spacing)
          if not mclass[0] == "":
            text "Taught: [mclass[0]], [mclass[1]]"
          if not aclass[0] == "":
            text "Taught: [aclass[0]], [aclass[1]]"
        $events = List_calander_events[display_date]
        if not events == "":
          null height (2 * gui.pref_spacing)
          text "Events: "
          text "[events]"
        
  #------------------------------------------------------  
style calendar_text is gui_label_text
  
screen class_planning_subject_choice(_period):
    ## Ensure other screens do not get input while this screen is displayed.
    modal True
    style_prefix "calendar"
    #tag menu

    use game_menu(_("Subjects"), scroll="viewport", _useNoNavigation=True):
      label "Choose a subject to teach" xalign 0.5 yalign 0.5
      grid 3 3:
        for subject in List_subjects:
          if _period == "Morning":
            button:
              action [SetVariable("morning_class", subject), Return()]
              frame:
                xsize 170
                ysize 140
                background Frame("gui/frame_idle.png", 25, 25)
                hover_background Frame("gui/frame_hover.png", 25, 25)
                text subject xalign 0.5 yalign 0.5
          else:
            button:
              action [SetVariable("afternoon_class", subject), Return()]
              frame:
                xsize 170
                ysize 140
                background Frame("gui/frame_idle.png", 25, 25)
                hover_background Frame("gui/frame_hover.png", 25, 25)
                text subject xalign 0.5 yalign 0.5
                
screen class_planning_tutoring_choice():
    ## Ensure other screens do not get input while this screen is displayed.
    modal True
    style_prefix "calendar"
    #tag menu

    use game_menu(_("Students"), scroll="viewport", _useNoNavigation=True):
      vbox:
        xpos 200
        ypos 50
        label "Choose a student to tutor after class" xalign 0.5 yalign 0.5
        grid 3 2:          
            for student in List_Students:
              if not student.Name == "Class Average":
                button:
                  action [SetVariable("after_school_tutoring", student.Name), Return()]
                  frame:
                    xsize 170
                    ysize 140
                    background Frame("gui/frame_idle.png", 25, 25)
                    hover_background Frame("gui/frame_hover.png", 25, 25)
                    text student.Name xalign 0.5 yalign 0.5
                    
            null
            button:
              action [SetVariable("after_school_tutoring", "Free Time"), Return()]
              frame:
                xsize 170
                ysize 140
                background Frame("gui/frame_idle.png", 25, 25)
                hover_background Frame("gui/frame_hover.png", 25, 25)
                text "Free Time" xalign 0.5 yalign 0.5
            null

screen class_planning():
  
    tag menu
    style_prefix "calendar"
    $weekday = weekDay(current_day)
    if weekday == "Friday":
      $next_day = current_day + 3
    else:
      $next_day = current_day + 1
    $nextDayName = weekDay(next_day)
    use game_menu(_("Planning for " + str(nextDayName) + " - Day "+ str(next_day)), scroll="viewport", _useAltNavigation="Gameplay"):
      vbox:
        xpos 200
        ypos 50
        hbox:
          xalign 0.5
          yalign 0.5
          vbox:
            label "Morning Class" xalign 0.5 yalign 0.5
            button:
              action [ShowMenu("class_planning_subject_choice", "Morning")]
              frame:
                xsize 300
                ysize 300
                background Frame("gui/frame_idle.png", 25, 25)
                hover_background Frame("gui/frame_hover.png", 25, 25)
                text morning_class xalign 0.5 yalign 0.5
          vbox:
            label "Afternoon Class" xalign 0.5 yalign 0.5
            button:
              action [ShowMenu("class_planning_subject_choice", "Afternoon")]
              frame:
                xsize 300
                ysize 300
                background Frame("gui/frame_idle.png", 25, 25)
                hover_background Frame("gui/frame_hover.png", 25, 25)
                text afternoon_class xalign 0.5 yalign 0.5
          vbox:
            label "Tutoring" xalign 0.5 yalign 0.5
            button:
              action [ShowMenu("class_planning_tutoring_choice")]
              frame:
                xsize 300
                ysize 300
                background Frame("gui/frame_idle.png", 25, 25)
                hover_background Frame("gui/frame_hover.png", 25, 25)
                text after_school_tutoring xalign 0.5 yalign 0.5
        textbutton "Continue" action Return() xalign 0.5 background Frame("gui/frame_idle.png", 25, 25) padding(20,0,20,0) xsize 250 text_xalign 0.5
    #imagebutton auto "gui/button/return_%s.png" xpos 1400 ypos 840  :
    #  hovered [Show("qm_tooltip",ttcontent="How do I get back?",ttxpos=600,ttypos=755)]
    #  unhovered Hide("qm_tooltip") 
    #  action  [Hide("qm_tooltip"),  Return()]
    
screen group_planning_choice(_characterName="Craig", _partnerNo=0):
    ## Ensure other screens do not get input while this screen is displayed.
    modal True
    style_prefix "roster"
    #tag menu

    use game_menu(_("Students"), scroll="viewport", _useNoNavigation=True):
    
      $partnerVar = str(_characterName)+"_Cram_Partner_0"+str(_partnerNo)
      grid 6 3:
        xpos 50
        ypos 30
        xspacing 20
        yspacing -30
        for character in List_Students_Side2:
          
          if character[0] == Craig_Cram_Partner_01:
            null
          elif character[0] == Craig_Cram_Partner_02:
            null
          elif character[0] == Hecate_Cram_Partner_01:
            null
          elif character[0] == Hecate_Cram_Partner_02:
            null
          elif character[0] == Sanura_Cram_Partner_01:
            null
          elif character[0] == Sanura_Cram_Partner_02:
            null
          else:
            button:
              background "gui/roster/roster_blank_inactive.png" 
              action [SetVariable(str(partnerVar), character[0]) ,  Return()]          
              has vbox
              #add "gui/roster/roster_blank_inactive.png" 
              if character[0] == "Achilles, Adonis, Atlas":
                text "[character[0]]" :
                  style "roster_button_text" 
                  size 20 
                  #yoffset 5
              else:
                text "[character[0]]"  :
                  style "roster_button_text"
                
            
          if character[0] == "Bestia":
            null
          
          if character[0] == "Florence":
            null
              
          if character[0] == "Rudolph":
            null
          
        #fill in empty space with null
        null   
        null   
    
screen group_planning(_characterName="Craig"):
    tag menu
    style_prefix "calendar"
    if _characterName == "Craig":
      $hint1 = "Friendly"
      $hint2 = "Attention grabbing"
      $partnerVar1 = Craig_Cram_Partner_01
      $partnerVar2 = Craig_Cram_Partner_02
        
    if _characterName == "Hecate":
      $hint1 = "Friendly and soft"
      $hint2 = "Blunt and honest"
      $partnerVar1 = Hecate_Cram_Partner_01
      $partnerVar2 = Hecate_Cram_Partner_02
      
    if _characterName == "Sanura":
      $hint1 = "Interested in Comedy"
      $hint2 = "Interested in Humour"
      $partnerVar1 = Sanura_Cram_Partner_01
      $partnerVar2 = Sanura_Cram_Partner_02
      
    use game_menu(_("Group Planning for " + str(_characterName)), scroll="viewport", _useAltNavigation="Gameplay"):
      hbox:
        vbox:
          xpos 200
          ypos 50
          hbox:
            xalign 0.5
            yalign 0.5
            vbox:
              label "Partner 1" xalign 0.5 yalign 0.5
              button:
                action [ShowMenu("group_planning_choice", _characterName, 1)]
                frame:
                  xsize 300
                  ysize 300
                  background Frame("gui/frame_idle.png", 25, 25)
                  hover_background Frame("gui/frame_hover.png", 25, 25)
                  text partnerVar1 xalign 0.5 yalign 0.5
            vbox:
              label "Partner 2" xalign 0.5 yalign 0.5
              button:
                action [ShowMenu("group_planning_choice", _characterName, 2)]
                frame:
                  xsize 300
                  ysize 300
                  background Frame("gui/frame_idle.png", 25, 25)
                  hover_background Frame("gui/frame_hover.png", 25, 25)
                  text partnerVar2 xalign 0.5 yalign 0.5
                
    vbox:
          xpos 1200
          ypos 400
          
          label "Looking for: "
          text "1. [hint1]"
          text "2. [hint2]"
          textbutton "Continue" action Return() xalign 0.5 background Frame("gui/frame_idle.png", 25, 25) padding(20,0,20,0) xsize 250 text_xalign 0.5