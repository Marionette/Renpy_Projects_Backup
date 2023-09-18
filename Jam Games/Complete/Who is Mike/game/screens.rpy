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

    # Decide if we want to use the one-window or two-window varaint.
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
            
            for caption, action, chosen in items:
                
                if action:  
                    
                    button:
                        action action
                        style "menu_choice_button"                        

                        text caption style "menu_choice"
                    
                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True
    
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.65)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.65)
    style.menu_choice_button.yminimum =  0.25
    style.menu_choice_button.ymaximum =  0.25
    style.menu_choice_button.background = "img/bg/ui/choice_idle.png"
    style.menu_choice_button.hover_background = "img/bg/ui/choice_hover.png"
    


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

    #This ensures that any other menu screen is replaced.
    tag menu

    #The background of the main menu.
    window:
        style "mm_root"

    # The various buttons.
    imagemap:
        ground "img/bg/ui/splash.png"
        idle "img/bg/ui/splash.png"
        hover "img/bg/ui/splash-mouse.png"
        selected_idle "img/bg/ui/splash-idle.png"
        selected_hover "img/bg/ui/splash-mouse.png"
        
        hotspot (1080, 67,145, 46) action Start()
        hotspot (1080, 117,145, 46) action ShowMenu("load")
        hotspot (1080, 166,145, 46) action ShowMenu("cg_gallery")
        hotspot (1080, 215,145, 46) action ShowMenu("preferences")
        hotspot (1080, 264,145,46) action Quit()


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

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"
    

screen Navigation2: 
    imagebutton auto "img/bg/ui/nav/Navigation_Return_%s.png" xpos 1036 ypos 526 focus_mask None action Return()
    imagebutton auto "img/bg/ui/nav/Navigation_Preferences_%s.png" xpos 1036 ypos 564 focus_mask None action ShowMenu("preferences")
    imagebutton auto "img/bg/ui/nav/Navigation_Save_%s.png" xpos 1036 ypos 604 focus_mask None  action ShowMenu("save")
    imagebutton auto "img/bg/ui/nav/Navigation_Load_%s.png" xpos 1036 ypos 644 focus_mask None action ShowMenu("load")
    #imagebutton auto "img/bg/ui/nav/Navigation_Help_%s.png" xpos 1036 ypos 798 focus_mask None action Help()
    imagebutton auto "img/bg/ui/nav/Navigation_Main_%s.png" xpos 1036 ypos 684 focus_mask None action MainMenu()
    imagebutton auto "img/bg/ui/nav/Navigation_Exit_%s.png" xpos 1036 ypos 724 focus_mask None action Quit()
    
##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.
    
screen file_picker:
    add "img/bg/ui/MiscMenu_background.png"

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"
            ypos 50
            xpos 30
            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)
                    
            textbutton _("Next"):
                action FilePageNext()
                
    $ columns = 2
    $ rows = 3
    for i in range(1, columns * rows + 1):
      $index = i
      $jpos = 574*((i-1)/rows)
      if (i > rows):
        $index = i-rows
      $ipos = 129*(index-1)
      imagebutton auto "img/bg/ui/savebox_%s.png" xpos 40+jpos ypos (110+ipos) focus_mask True action FileAction(i)
      
      add FileScreenshot(i):
        xpos 60+jpos 
        ypos (130+ipos)
        size (117,74)
      
      $ file_name = FileSlotName(i, columns * rows)
      $ file_time = FileTime(i, empty=_("Empty Slot."))
      $ save_name = FileSaveName(i)
  
      text "[file_name]. [file_time!t]\n[save_name!t]":
        xpos 185+jpos 
        ypos (130+ipos)
  
      key "save_delete" action FileDelete(i)
      
screen save:

    # This ensures that any other menu screen is replaced.
    tag menu

    use file_picker
    use Navigation2

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    use file_picker
    use Navigation2

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)
    style.file_picker_frame.background = None     

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)
    style.file_picker_nav_button.background = None
    style.file_picker_nav_button_text.hover_size = 25

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)

    

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
    
screen preferences:

    tag menu
    add "img/bg/ui/options/PrefMenu_background.png"
    # Include the navigation.
    use Navigation2
    
    imagebutton auto "img/bg/ui/options/preferences_window_%s.png" xpos 85 ypos 80 focus_mask None action Preference ("display", "window")
    imagebutton auto "img/bg/ui/options/preferences_fullscreen_%s.png" xpos 85 ypos 120 focus_mask None action Preference ("display", "fullscreen")
    
    imagebutton auto "img/bg/ui/options/preferences_transitions_on_%s.png" xpos 85 ypos 220 focus_mask None action Preference("transitions", "all")
    imagebutton auto "img/bg/ui/options/preferences_transitions_off_%s.png" xpos 85 ypos 260 focus_mask None action Preference("transitions", "none")


    imagebutton auto "img/bg/ui/options/preferences_skipseen_%s.png" xpos 355 ypos 80 focus_mask None action Preference("skip", "seen")
    imagebutton auto "img/bg/ui/options/preferences_skipall_%s.png" xpos 355 ypos 120 focus_mask None action Preference("skip", "all")
    
    imagebutton auto "img/bg/ui/options/preferences_skipafter_on_%s.png" xpos 355 ypos 220 focus_mask None action Preference("after choices", "stop")
    imagebutton auto "img/bg/ui/options/preferences_skipafter_off_%s.png" xpos 355 ypos 260 focus_mask None action Preference("after choices", "skip")
    
    imagebutton auto "img/bg/ui/lang/preferences_eng_%s.png" xpos 733 ypos 311 focus_mask None action Language(None)
  
    imagebutton auto "img/bg/ui/lang/preferences_ger_%s.png" xpos 843 ypos 314 focus_mask None action Language("german")
   
    imagebutton auto "img/bg/ui/lang/preferences_esp_%s.png" xpos 960 ypos 314 focus_mask None action Language("spanish") 
   
    imagebutton auto "img/bg/ui/lang/preferences_rus_%s.png" xpos 1085 ypos 314 focus_mask None action Language("russian")    
  
    frame xpos 35 ypos 365:
        style_group "pref"
        has vbox
        bar value Preference("text speed")
    
    frame xpos 395 ypos 365:
        style_group "pref"
        has vbox
        bar value Preference("auto-forward time")
    
    frame xpos 840 ypos 125:
        style_group "pref"
        has vbox
        bar value Preference("music volume")
    frame xpos 840 ypos 170:
        style_group "pref"
        has vbox
        bar value Preference("sound volume")


init -2 python:
    style.pref_frame.background = None

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 227
    style.pref_slider.xalign = 1.0
    style.pref_slider.left_bar = "img/bg/ui/options/pref_bar_full.png"
    style.pref_slider.right_bar = "img/bg/ui/options/pref_bar_empty.png"
    style.pref_slider.thumb = "img/bg/ui/options/Slider.png"

    style.soundtest_button.xalign = 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen yesno_prompt:

    modal True
    add "img/bg/ui/MiscMenu_background.png"
    imagebutton auto "img/bg/ui/confirm/Yes_%s.png" xalign .3 yalign .5 focus_mask None action yes_action
    imagebutton auto "img/bg/ui/confirm/No_%s.png" xalign .5 yalign .5 focus_mask None  action no_action

    window:
        xalign .5
        yalign .35
        style_group "yesno"   
        background None
        label _(message):
            yalign 0.5
            xalign 0.5
    
    # Right-click and escape answer "no".
    key "game_menu" action no_action
    


init -2 python:    
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5
    style.yesno_label_text.size = 30
 


screen chapter_select():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .04
        yalign .04

        has vbox

        textbutton _("True end") action Start("truend")
        textbutton _("Bad End") action Start("badend")
        textbutton _("Calm") action Start("calmdown")
        textbutton _("Attack") action Start("fight")
        textbutton _("Dead End") action Start("deadend")
        textbutton _("Bonus End") action Start("bonusend")
        textbutton _("Return") action Return()

        

##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"
    
        xalign 1.0
        yalign  0.83
        

        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Skip") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')
       # textbutton _("ends") action ShowMenu("chapter_select")
        
init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = Frame('img/bg/ui/frame.png', 10,10)
    style.quick_button.xpadding = 15
    style.quick_button.ypadding = 5 
    style.quick_button.xmargin = 2

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 13
    style.quick_button_text.idle_color = "#8888"
    style.quick_button_text.hover_color = "#fff"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"
    
    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False
    
