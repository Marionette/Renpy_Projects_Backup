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
    default two_window = True


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
                        size 25
                        outlines [ (1, "#0a0a0a", 0, 0) ]

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
    if show_quick_menu:
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
            spacing 20

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
        color "#845f2e"
        hover_color "#9a6f3c" 
        hover_outlines [(absolute(1), "#dbcfb6", absolute(-1), absolute(1))]

    style menu_choice_button is button:
        xminimum 1393 #int(config.screen_width * 0.75)
        xmaximum 1393 #int(config.screen_width * 0.75)
        yminimum 80
        background "img/gui/choiceButton_normal.png"
        hover_background "img/gui/choiceButton_hover.png"

    ###Code for customization of choice BG
    #style.menu_choice_button.background = Frame("FILE NAME HERE",28,9)
    #style.menu_choice_button.hover_background = Frame("FILE NAME HERE",28,9)
    #style.menu_choice_button.yminimum = 60
    #
    ###Code for customization of text in the choice button
    #style.menu_choice.color = "#fff"
    #style.menu_choice.size = 18
    #style.menu_choice.outlines = [(2, "#3f603e", 0, 0)]
    ## style.menu_choice.hover_color = "#fff"
    ## style.menu_choice.hover_outlines = [(2, "#000", 0, 0)]
    
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

screen main_menu:

    # This ensures that any other menu screen is replaced.
    tag menu

    #add Animation("img/gui/Main-Menu_BG1.png", 3, 
    #               "img/gui/Main-Menu_BG2.png", 0.1, 
    #               "img/gui/Main-Menu_BG3.png", 0.5)
    add "img/gui/MainMenu_blank.png" 
    add Animation("img/gui/MainMenu1.png", 3, 
                   "img/gui/MainMenu2.png", 0.1, 
                   "img/gui/MainMenu3.png", 0.5, 
                   "img/gui/MainMenu2.png", 0.1,) xpos 1198 ypos 340
    imagebutton auto "img/gui/MainMenu_Play_%s.png" xpos 155 ypos 718 focus_mask True action Start()
    imagebutton auto "img/gui/MainMenu_Load_%s.png" xpos 425 ypos 798 focus_mask True  action ShowMenu('load')
    #preferences focus_mask set to None because its just text
    imagebutton auto "img/gui/MainMenu_Options_%s.png" xpos 695 ypos 798 focus_mask True action ShowMenu('preferences')
    imagebutton auto "img/gui/MainMenu_Credits_%s.png" xpos 965 ypos 798 focus_mask True action Start("lbl_Credits")
    #imagebutton auto "img/gui/MainMenu_Extras_%s.png" xpos 1235 ypos 798 focus_mask True action ShowMenu("fa_gallery_custom")
    imagebutton auto "img/gui/MainMenu_Extras_%s.png" xpos 1235 ypos 798 focus_mask True action ShowMenu("gallery_custom")
    imagebutton auto "img/gui/MainMenu_Exit_%s.png" xpos 1670 ypos 892 focus_mask True action Quit(confirm=False) 
    #currently no help button
    #imagebutton auto "img/gui/MainMenu_Help_%s.png" xpos 0 ypos 0 focus_mask True action Help()

      


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
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

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
    
screen file_picker(_menuType="save"):

    #tag menu
    add "img/gui/saveload/SaveLoad_BG.png" 
    
    #imagebutton auto "img/gui/saveload/Previous_%s.png" xpos 155 ypos 190 focus_mask True action FilePagePrevious()
    imagebutton auto "img/gui/saveload/Buttons_Save_Auto_%s.png" xpos 155 ypos 190 focus_mask True action FilePage("auto")
    imagebutton auto "img/gui/saveload/Buttons_Save_Quick_%s.png" xpos 425 ypos 190 focus_mask True action FilePage("quick")
    
    imagebutton auto "img/gui/saveload/Buttons_Save_1_%s.png" xpos (694+(111*(1-1))) ypos 189 focus_mask True action FilePage(1)
    imagebutton auto "img/gui/saveload/Buttons_Save_2_%s.png" xpos (694+(111*(2-1))) ypos 189 focus_mask True action FilePage(2)
    imagebutton auto "img/gui/saveload/Buttons_Save_3_%s.png" xpos (694+(111*(3-1))) ypos 189 focus_mask True action FilePage(3)
    imagebutton auto "img/gui/saveload/Buttons_Save_4_%s.png" xpos (694+(111*(4-1))) ypos 189 focus_mask True action FilePage(4)
    imagebutton auto "img/gui/saveload/Buttons_Save_5_%s.png" xpos (694+(111*(5-1))) ypos 189 focus_mask True action FilePage(5)
    imagebutton auto "img/gui/saveload/Buttons_Save_6_%s.png" xpos (694+(111*(6-1))) ypos 189 focus_mask True action FilePage(6)
    imagebutton auto "img/gui/saveload/Buttons_Save_7_%s.png" xpos (694+(111*(7-1))) ypos 189 focus_mask True action FilePage(7)
    
    
    $ columns = 2
    $ rows = 5
    for i in range(1, columns * rows + 1):
      $index = i
      $jpos = 605*((i-1)/rows)
      if (i > rows):
        $index = i-rows
      $ipos = 83*(index-1)
      imagebutton auto "img/gui/saveload/SaveSlot_%s.png" xpos 310+jpos ypos (321+ipos) focus_mask True action FileAction(i)
      add FileScreenshot(i) xpos 550+jpos ypos (340+ipos)
      $ file_name = FileSlotName(i, columns * rows)
      $ file_time = FileTime(i, empty=_("Empty Slot."))
      #$ save_name = FileSaveName(i) #not used
      $TextColour='#966935'
      $TextColourSelected='#84b3ae'
      if file_time == "Empty Slot.":
        if _menuType == "save":
          text "{color=[TextColour]}[file_time!t]{/color}"  xpos 340+jpos+180 ypos (345+ipos)
        else:
          text "{color=[TextColourSelected]}[file_time!t]{/color}"  xpos 340+jpos+180 ypos (345+ipos)
      else:
        text "{color=[TextColour]}[file_name].                      [file_time!t]{/color}"  xpos 340+jpos ypos (345+ipos)
      


screen save:

    # This ensures that any other menu screen is replaced.
    tag menu

    use file_picker('save')
    use Navigation2

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    use file_picker('load')
    use Navigation2

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
    $display = 'window'
    tag menu
    #Hiding language options
    #add "img/gui/options/Options_BG_lang.png"
    add "img/gui/options/Options_BG.png"
    # Include the navigation.
    use Navigation2

    #Hiding language options
    #imagebutton auto "img/gui/options/Checkbox_%s.png" xpos 350 ypos 550 focus_mask True action Language(None)
    #imagebutton auto "img/gui/options/Checkbox_%s.png" xpos 350 ypos 600 focus_mask True action Language("german")
    #imagebutton auto "img/gui/options/Checkbox_%s.png" xpos 350 ypos 650 focus_mask True action Language("portuguese")
    
    imagebutton auto "img/gui/options/Checkbox_%s.png" xpos 1339 ypos 6 focus_mask True action Preference('display', 'toggle')
    imagebutton auto "img/gui/options/Checkbox_%s.png" xpos 1339 ypos 60 focus_mask True action Preference('transitions', 'toggle')
    
    #imagebutton auto "img/gui/options/OButtons_Joy_%s.png" xpos 859 ypos 111 focus_mask True action Preference("joystick")
    #ShowMenu("joystick_preferences2")

    imagebutton auto "img/gui/options/Checkbox_%s.png" xpos 1339 ypos 196 focus_mask True action Preference("skip", "seen")
    imagebutton auto "img/gui/options/Checkbox_%s.png" xpos 1339 ypos 250 focus_mask True action Preference("skip", "all")
    imagebutton auto "img/gui/options/Checkbox_%s.png" xpos 1339 ypos 304 focus_mask True action Preference("after choices", "toggle")
    
    frame xpos 1123 ypos 370:
        background "img/gui/options/Slider_ends.png"
        style_group "pref"
        has vbox
        bar value Preference("text speed") xpos 37 ypos -6
        
    imagebutton auto "img/gui/options/Checkbox_%s.png" xpos 1339 ypos 433 focus_mask True action Preference("auto-forward", "toggle")
    
    frame xpos 1123 ypos 487:
        background "img/gui/options/Slider_ends.png"
        style_group "pref"
        has vbox
        bar value Preference("auto-forward time") xpos 37 ypos -6
    

    imagebutton auto "img/gui/options/Checkbox_%s.png" xpos 1339 ypos 542 focus_mask True action Preference("wait for voice", "toggle")
    
    frame xpos 1123 ypos 625:
        background "img/gui/options/Slider_ends.png"
        style_group "pref"
        has vbox
        bar value Preference("music volume") xpos 37 ypos -6
    frame xpos 1123 ypos 676:
        background "img/gui/options/Slider_ends.png"
        style_group "pref"
        has vbox
        bar value Preference("sound volume") xpos 37 ypos -6
    frame xpos 1123 ypos 727:
        background "img/gui/options/Slider_ends.png"
        style_group "pref"
        has vbox
        bar value Preference("voice volume") xpos 37 ypos -6

screen Navigation2: 
    imagebutton auto "img/gui/options/OButtons_Return_%s.png" xpos 155 ypos 718 focus_mask True action Return()
    imagebutton auto "img/gui/options/OButtons_Save_%s.png" xpos 425 ypos 798 focus_mask True  action ShowMenu("save")
    imagebutton auto "img/gui/options/OButtons_Load_%s.png" xpos 695 ypos 798 focus_mask True action ShowMenu("load")
    imagebutton auto "img/gui/options/OButtons_Help_%s.png" xpos 965 ypos 798 focus_mask True action ShowMenu("help")
    imagebutton auto "img/gui/options/OButtons_Main_%s.png" xpos 1235 ypos 798 focus_mask True action MainMenu()
    imagebutton auto "img/gui/MainMenu_Exit_%s.png" xpos 1670 ypos 892 focus_mask True action Quit()
    
    
    #imagebutton auto "img/gui2/config_display_window_%s.png" xpos 1339 ypos 6 focus_mask True action Preference('display', 'toggle')
    #imagebutton auto "img/gui2/config_display_window_%s.png" xpos 300 ypos 186 focus_mask True action Preference('transitions', 'toggle')
    # Put the navigation columns in a three-wide grid.
    #grid 3 1:
    #    style_group "prefs"
    #    xfill True
    #
    #    # The left column.
    #    vbox:
    #        frame:
    #            style_group "pref"
    #            has vbox
    #
    #            label _("Display")
    #            textbutton _("Window") action Preference("display", "window")
    #            textbutton _("Fullscreen") action Preference("display", "fullscreen")
    #
    #        frame:
    #            style_group "pref"
    #            has vbox
    #
    #            label _("Transitions")
    #            textbutton _("All") action Preference("transitions", "all")
    #            textbutton _("None") action Preference("transitions", "none")
    #
    #        frame:
    #            style_group "pref"
    #            has vbox
    #
    #            label _("Text Speed")
    #            bar value Preference("text speed")
    #
    #        frame:
    #            style_group "pref"
    #            has vbox
    #
    #            textbutton _("Joystick...") action Preference("joystick")
    #
    #
    #    vbox:
    #        frame:
    #            style_group "pref"
    #            has vbox
    #
    #            label _("Skip")
    #            textbutton _("Seen Messages") action Preference("skip", "seen")
    #            textbutton _("All Messages") action Preference("skip", "all")
    #
    #        frame:
    #            style_group "pref"
    #            has vbox
    #
    #            textbutton _("Begin Skipping") action Skip()
    #
    #        frame:
    #            style_group "pref"
    #            has vbox
    #
    #            label _("After Choices")
    #            textbutton _("Stop Skipping") action Preference("after choices", "stop")
    #            textbutton _("Keep Skipping") action Preference("after choices", "skip")
    #
    #        frame:
    #            style_group "pref"
    #            has vbox
    #
    #            label _("Auto-Forward Time")
    #            bar value Preference("auto-forward time")
    #
    #            if config.has_voice:
    #                textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")
    #
    #    vbox:
    #        frame:
    #            style_group "pref"
    #            has vbox
    #
    #            label _("Music Volume")
    #            bar value Preference("music volume")
    #
    #        frame:
    #            style_group "pref"
    #            has vbox
    #
    #            label _("Sound Volume")
    #            bar value Preference("sound volume")
    #
    #            if config.sample_sound:
    #                textbutton _("Test"):
    #                    action Play("sound", config.sample_sound)
    #                    style "soundtest_button"
    #
    #        if config.has_voice:
    #            frame:
    #                style_group "pref"
    #                has vbox
    #
    #                label _("Voice Volume")
    #                bar value Preference("voice volume")
    #
    #                textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
    #                if config.sample_voice:
    #                    textbutton _("Test"):
    #                        action Play("voice", config.sample_voice)
    #                        style "soundtest_button"

init -2:
    style pref_frame:
        xfill False
        xmargin 0
        top_margin 0

    style pref_vbox:
        xfill False

    style pref_button:
        size_group "pref"
        xalign 1.0

    #style pref_slider:
        #xmaximum 274
        #ymaximum 56
        #xalign 1.0
        #left_bar  "img/gui/options/Slider_full.png"
        #right_bar  "img/gui/options/Slider_empty.png"
        #thumb "img/gui/options/Slider_Flower.png"
        #background None
        #bar_vertical = True
        #bar_invert = False
        #bottom_bar = "Gui/Rose_Prefs_Thermfull.png"
        #top_bar = "Gui/Rose_Prefs_Thermempty.png"

    style soundtest_button:
        xalign 1.0
        

init -2 python: 
    # Styling for the bar sliders:
    # Aleema's Customizing Menus tutorial: http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=9812
    # Bar style properties documentation: http://www.renpy.org/doc/html/style.html#bar-style-properties
    style.pref_frame.background = None
    style.pref_slider.left_bar = "img/gui/options/Slider_mid_full.png"
    style.pref_slider.right_bar = "img/gui/options/Slider_mid_empty.png"
    style.pref_slider.thumb = "img/gui/options/Slider_Flower2.png"
    style.pref_slider.xmaximum = 189
    style.pref_slider.ymaximum = 56   
    style.pref_slider.thumb_offset = 54/2

init 2 python: 
    style.js_prefs_frame.background = None #"img/gui/options/Options_Joystick.png"
    style.js_prefs_frame.xfill = False
    #style.js_prefs_frame.ypadding = 0.2
    #style.js_prefs_frame.xpadding = 0.2
    style.js_prefs_frame.xpos = 1138
    style.js_prefs_frame.ypos = 136
    style.js_prefs_button.xminimum = 0.0
    style.js_prefs_box.box_first_spacing = 10
    style.js_frame_box.background = "img/gui/options/Options_Joystick.png"
    #style.js_prefs_frame.background = None# "img/gui/options/Options_Joystick.png"
    #style.gm_root.background = None#"img/gui/options/Options_Joystick.png"
    #style.menu_frame.background = None
    #style.menu_frame.xops = 300
    #style.vbox.background = "img/gui/options/Options_Joystick.png"
    ##############
    ##########
    
##############################################################################
# Joystick Menu
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

init python:

      config.joystick_keys = [
          (u'Left', 'joy_left'),
          (u'Right', 'joy_right'),
          (u'Up', 'joy_up'),
          (u'Down', 'joy_down'),
          (u'Select/Dismiss', 'joy_dismiss'),
          (u'Rollback', 'joy_rollback'),
          (u'Hold to Skip', 'joy_holdskip'),
          (u'Toggle Skip', 'joy_toggleskip'),
          (u'Hide Text', 'joy_hide'),
          (u'Menu', 'joy_menu'),
          ]

      def _joystick_select_binding():

          for label, key in config.joystick_keys:

              def my_clicked(label=label, key=key):
                  return (label, key)

              layout.button(_(label) + " - " + _(_preferences.joymap.get(key, u"Not Assigned")), "prefs_js", clicked=my_clicked, index=label)

      def _joystick_get_binding():
          ui.saybehavior()
          ui.add(renpy.display.joystick.JoyBehavior())

      def _joystick_take_binding(binding, key):

        if not isinstance(binding, basestring):
            if key in _preferences.joymap:
                del _preferences.joymap[key]
        else:
            _preferences.joymap[key] = binding

      def _joystick_preferencesB():
        def set_binding(label, key):
            layout.navigation(None)

            ui.window(style='js_frame')
            ui.vbox(style='js_frame_box')
            layout.prompt(_(u"Joystick Mapping") + " - " + _(label), "js_function")
            layout.prompt(u'Move the joystick or press a joystick button to create the mapping. Click the mouse to remove the mapping.', 'js_action')
            ui.close()

            _joystick_get_binding()
            binding = ui.interact(mouse="gamemenu")
            _joystick_take_binding(binding, key)

            return True

        ui.vbox(style='js_prefs_box')

        layout.label("Joystick Configuration", "js_prefs")

        for label, key in config.joystick_keys:

            def clicked(label=label, key=key):
                return renpy.invoke_in_new_context(set_binding, label, key)

            layout.button(_(label) + " - " + _(_preferences.joymap.get(key, u"Not Assigned")), "js_prefs", clicked=clicked, index=label)

        ui.close()
    #use Navigation2
    #while True:
    #python:
    
#label joystick_preferences_screenB:
#
#    while True:
#      python:
#        layout.navigation("joystick_preferencesB")
#        _joystick_preferencesB()
#        ui.interact(mouse="gamemenu")
    
screen joystick_preferences2:
    #$display = 'window'
    tag menu
    # Include the navigation.
    add "img/gui/options/Options_Joystick.png"
    #imagebutton auto "img/gui/options/OButtons_Return_%s.png" xpos 155 ypos 718 focus_mask True action set_binding('Left', key)
    #use joystick
    #use joystick_preferences_screenB
    #$_joystick_preferences()
    
    textbutton _("Joystick") action renpy.invoke_in_new_context(set_binding, label, key)

##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    modal True
    add "img/gui/confirm/Confirm_bg.png"
    imagebutton auto "img/gui/confirm/Yes_%s.png" xpos 567 ypos 214 focus_mask True action yes_action
    imagebutton auto "img/gui/confirm/No_%s.png" xpos 1160 ypos 214 focus_mask True  action no_action
    
    window:
        style_group "yesno"   
        background None
        label _(message):
            yalign 0.1
            #style "big_text"

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style big_text:
        size 60
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        is default
        #size 12
        #text_align 0.5
        #layout "subtitle"
        #font "DejaVuSans.ttf"        
        drop_shadow (2, 2)
        drop_shadow_color "#000000"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    # Add an in-game quick menu.
    #hbox:
        #style_group "quick"

        #xalign 1.0
        #yalign 1.0

        ####OLD BUTTONS###
        #textbutton _("Back") action Rollback()
        #textbutton _("Save") action ShowMenu('save')
        #textbutton _("Q.Save") action QuickSave()
        #textbutton _("Q.Load") action QuickLoad()
        #textbutton _("Skip") action Skip()
        #textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        #textbutton _("Auto") action Preference("auto-forward", "toggle")
        #textbutton _("Prefs") action ShowMenu('preferences')
        
        
    imagebutton auto "img/gui/quickmenu/QuickMenu_Save_%s.png" xpos 1649 ypos 780 focus_mask True action ShowMenu('save')
    imagebutton auto "img/gui/quickmenu/QuickMenu_Load_%s.png" xpos 1650 ypos 830 focus_mask True action ShowMenu('load')
    imagebutton auto "img/gui/quickmenu/QuickMenu_Options_%s.png" xpos 1650 ypos 880 focus_mask True action ShowMenu('preferences')
    imagebutton auto "img/gui/quickmenu/QuickMenu_MainMenu_%s.png" xpos 1650 ypos 929 focus_mask True action MainMenu()
    imagebutton auto "img/gui/quickmenu/QuickMenu_Back_%s.png" xpos 1650 ypos 979 focus_mask True action Rollback()
    imagebutton auto "img/gui/quickmenu/QuickMenu_Auto_%s.png" xpos 1735 ypos 979 focus_mask True action Preference("auto-forward", "toggle")
    
    #textbutton _("F.Skip") action Skip(fast=True, confirm=True)    

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


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("{color=#966935}Help{/color}"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:
                style "menu"
                use customButton2("Keyboard", SetScreenVariable("device", "keyboard"), 0, 0, 25, TextXOffset=-380)
                use customButton2("Mouse", SetScreenVariable("device", "mouse"), -300, 0, 25, TextXOffset=-400)
                if GamepadExists():
                  use customButton2("Gamepad", SetScreenVariable("device", "gamepad"), -600, 0, 25, TextXOffset=-380)
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

    #textbutton _("Calibrate") action GamepadCalibrate()
    use customButton2("Calibrate", GamepadCalibrate(), 0, 0, 25, TextXOffset=-230, TextYOffset=-75)


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    #properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    #properties gui.button_text_properties("help_button")
    #outlines [ (1, "#0a0a0a", 0, 0) ]
    drop_shadow (2, 2)
    drop_shadow_color "#000000"

style help_label:
    xsize 350
    right_padding 20

style help_label_text:
    size 30
    xalign 1.0
    text_align 1.0
    color "#966935"
    #outlines [ (1, "#0a0a0a", 0, 0) ]
    
style help_text:
    size 26
    color "#c39055"
    #outlines [ (1, "#0a0a0a", 0, 0) ]
    #drop_shadow (1, 1)
    #drop_shadow_color "#000000"

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    tag menu
    style_prefix "game_menu"
    add "img/gui/extras/FAGalleryBG.png"

    #if main_menu:
    #    add gui.main_menu_background
    #else:
    #    add gui.game_menu_background

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

                        side_yfill True

                        transclude

                else:

                    transclude

    use Navigation2

    #textbutton _("Return"):
    #    style "return_button"

    #    action Return()

    #label title

    #if main_menu:
    #    key "game_menu" action ShowMenu("main_menu")


#style game_menu_outer_frame is empty
#style game_menu_navigation_frame is empty
#style game_menu_content_frame is empty
#style game_menu_viewport is gui_viewport
#style game_menu_side is gui_side
#style game_menu_scrollbar is gui_vscrollbar
#
#style game_menu_label is gui_label
#style game_menu_label_text is gui_label_text
#
#style return_button is navigation_button
#style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    #background "gui/overlay/game_menu.png"
    background None

style game_menu_navigation_frame:
    xsize 280
    yfill True
    background None

style game_menu_content_frame:
    left_margin 140
    right_margin 20
    top_margin 10
    background None

style game_menu_viewport:
    xsize 1220
    #ysize 600

style game_menu_vscrollbar:
    unscrollable "hide"

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 150
    ysize 120

style game_menu_label_text:
    size 50
    #color gui.accent_color
    yalign 0.5
    #outlines [ (1, "#0a0a0a", 0, 0) ]
    #drop_shadow (2, 2)
    #drop_shadow_color "#000000"

#style return_button:
#    xpos gui.navigation_xpos
#    yalign 1.0
#    yoffset -30

style hyperlink_text:
    #properties gui.text_properties("hyperlink", accent=True)
    color "#d7b78e"
    hover_color "#caa068" 
    hover_underline True