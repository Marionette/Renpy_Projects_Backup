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
            else:
                text "" id "who"
              

            text what id "what" xpos 48 ypos 17

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

    style say_who_window is text:
        color "#f00"

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.65)
        xmaximum int(config.screen_width * 0.65)
        background Frame("images/ui/framechoice_idle.png", 24, 24)
        hover_background Frame("images/ui/framechoice_hover.png", 24, 24)
        top_padding 10
        bottom_padding 10

    style menu_choice is button_text:
        clear
        color "#f00"

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
        
    imagemap:
        auto "images/ui/mm_%s.png"        
        hotspot (965, 90, 60, 60) action Start()
        hotspot (965, 150, 60, 60) action ShowMenu("load")
        hotspot (965, 210, 60, 60) action ShowMenu("gallery")
        hotspot (965, 270, 60, 60) action ShowMenu("preferences")
        hotspot (965, 330, 60, 60) action Quit(confirm=False)
        
    if persistent.SolEnd == True: 
      add "images/ui/mainmenu_SolEnd.png"
    if persistent.MiloEnd == True: 
      add "images/ui/mainmenu_MiloEnd.png"
    if persistent.JoelEnd == True: 
      add "images/ui/mainmenu_JoelEnd.png"

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
    
    imagebutton auto "images/ui/exit_%s.png" focus_mask True xpos 1060 ypos 67 action Return()
        
    imagemap:
        xpos 188
        ypos 120
        auto "images/ui/navigation_%s.png"        
        hotspot (0,  5, 185, 82) action MainMenu()
        hotspot (0, 90, 185, 82) action ShowMenu("save")
        hotspot (0, 170, 185, 82) action ShowMenu("load")
        hotspot (0, 250, 185, 82) action ShowMenu("preferences")
        hotspot (0, 330, 185, 82) action ShowMenu("gallery")
        hotspot (0, 410, 185, 82)  action Quit()

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

    # Include the navigation.
    use navigation
    
    vbox:
      frame:
        background None
        area (400,125,690,550)
        style "file_picker_frame"

        has vbox

        $ columns = 3
        $ rows = 2

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                vbox:
                  button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                  text "[file_name]. [file_time!t]\n[save_name!t]" xpos 10

                  key "save_delete" action FileDelete(i)


        frame:
          background None
          ypos 70
          # The buttons allow the user to pick a
          # page of files.
          hbox:
          
              style_group "file_picker_nav"

              textbutton _("Previous"):
                  action FilePagePrevious()

              textbutton _("Auto"):
                  action FilePage("auto")

              textbutton _("Quick"):
                  action FilePage("quick")

              for i in range(1, 5):
                  textbutton str(i):
                      action FilePage(i)

              textbutton _("Next"):
                  action FilePageNext()

screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    
    add "images/ui/menu_base.png"
    add "images/ui/save_text.png"
    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    add "images/ui/menu_base.png"
    add "images/ui/load_text.png"
    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text

    style file_picker_button:
        idle_background Frame("images/ui/savebox_idle.png", 24, 24)
        hover_background Frame("images/ui/savebox_hover.png", 24, 24)
        insensitive_background Frame("images/ui/savebox_idle.png", 24, 24)
        selected_idle_background Frame("images/ui/savebox_idle.png", 24, 24)
        selected_hover_background Frame("images/ui/savebox_idle.png", 24, 24)
        top_padding 15
        bottom_padding 12
        left_padding 12
        right_padding 12
        xminimum 341
        yminimum 170

    style file_picker_nav_button:
        idle_background Frame("images/ui/pixelframe_idle.png", 24, 24)
        hover_background Frame("images/ui/pixelframe_hover.png", 24, 24)
        insensitive_background Frame("images/ui/pixelframe_ground.png", 24, 24)
        selected_idle_background Frame("images/ui/pixelframe_selected_idle.png", 24, 24)
        selected_hover_background Frame("images/ui/pixelframe_selected_hover.png", 24, 24)
        top_padding 5
        bottom_padding 5
        
    style file_picker_frame:
        insensitive_background Frame("images/ui/pixelframe_ground.png", 24, 24)
    
    style file_picker_nav_button_text:
      font "misc/ProggyClean.ttf"
      size 32
      
init -2 python:
    
    config.thumbnail_width = 200
    config.thumbnail_height = 144
##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu
    
    add "images/ui/menu_base.png"
    add "images/ui/preferences_title.png"
    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 2 1:
        style_group "prefs"
        xfill True
        area (400,120,690,560)

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("{font=misc/ProggyClean.ttf}{size=+10}Display{/size}{/font}")
                textbutton _("{font=misc/ProggyClean.ttf}{size=+10}Window{/size}{/font}") action Preference("display", "window")
                textbutton _("{font=misc/ProggyClean.ttf}{size=+10}Fullscreen{/size}{/font}") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("{font=misc/ProggyClean.ttf}{size=+10}Transitions{/size}{/font}")
                textbutton _("{font=misc/ProggyClean.ttf}{size=+10}All{/size}{/font}") action Preference("transitions", "all")
                textbutton _("{font=misc/ProggyClean.ttf}{size=+10}None{/size}{/font}") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("{font=misc/ProggyClean.ttf}{size=+10}Text Speed{/size}{/font}")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox
                textbutton _("{font=misc/ProggyClean.ttf}{size=+10}Joystick...{/size}{/font}") action Preference("joystick")
                
            #vbox:
            frame:
                style_group "pref"
                has vbox
                #add "assets/ui/h-font.png"
                #hbox:
                label _("{font=misc/ProggyClean.ttf}{size=+10}Text Font{/size}{/font}")
                textbutton "{font=misc/Dosis-Regular.ttf}Dosis{/font}" action StylePreference("text", "dosis")
                textbutton "{font=misc/OpenDyslexic-Regular.otf}Open Dyslexic{/font}" action StylePreference("text", "open-dyslexic")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("{font=misc/ProggyClean.ttf}{size=+10}Skip{/size}{/font}")
                textbutton _("{font=misc/ProggyClean.ttf}{size=+10}Seen Messages{/size}{/font}") action Preference("skip", "seen")
                textbutton _("{font=misc/ProggyClean.ttf}{size=+10}All Messages{/size}{/font}") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("{font=misc/ProggyClean.ttf}{size=+10}Begin Skipping{/size}{/font}") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("{font=misc/ProggyClean.ttf}{size=+10}After Choices{/size}{/font}")
                textbutton _("{font=misc/ProggyClean.ttf}{size=+10}Stop Skipping{/size}{/font}") action Preference("after choices", "stop")
                textbutton _("{font=misc/ProggyClean.ttf}{size=+10}Keep Skipping{/size}{/font}") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("{font=misc/ProggyClean.ttf}{size=+10}Auto-Forward Time{/size}{/font}")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("{font=misc/ProggyClean.ttf}{size=+10}Wait for Voice{/size}{/font}") action Preference("wait for voice", "toggle")

        #vbox:
            frame:
                style_group "pref"
                has vbox

                label _("{font=misc/ProggyClean.ttf}{size=+10}Music Volume{/size}{/font}")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("{font=misc/ProggyClean.ttf}{size=+10}Sound Volume{/size}{/font}")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("{font=misc/ProggyClean.ttf}{size=+10}Test{/size}{/font}"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("{font=misc/ProggyClean.ttf}{size=+10}Voice Volume{/size}{/font}")
                    bar value Preference("voice volume")

                    textbutton _("{font=misc/ProggyClean.ttf}{size=+10}Voice Sustain{/size}{/font}") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("{font=misc/ProggyClean.ttf}{size=+10}Test{/size}{/font}"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 8
        background Frame("images/ui/pixelframe_idle.png", 24, 24)
        hover_background Frame("images/ui/pixelframe_hover.png", 24, 24)
        insensitive_background Frame("images/ui/pixelframe_ground.png", 24, 24)
        top_padding 10
        bottom_padding 10

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0
        idle_background Frame("images/ui/pixelframe_idle.png", 24, 24)
        hover_background Frame("images/ui/pixelframe_hover.png", 24, 24)
        insensitive_background Frame("images/ui/pixelframe_ground.png", 24, 24)
        selected_idle_background Frame("images/ui/pixelframe_selected_idle.png", 24, 24)
        selected_hover_background Frame("images/ui/pixelframe_selected_hover.png", 24, 24)
        top_padding 5
        bottom_padding 5

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
  use MessageBox_prompt(message, yes_action, no_action, None)

screen info_prompt(message, ok_action):
  use MessageBox_prompt(message, None, None, ok_action)


screen MessageBox_prompt(_message, _yes_action=None, _no_action=None, _ok_action=None):

    modal True

    window:
        #style "gm_root"
        background "images/ui/confirm_box.png"

    frame:
        background None
        area (245,122,800,338)
        style_group "pref"

        xfill True
        xmargin .05
        #ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label "{font=misc/ProggyClean.ttf}{size=+10}" + _(_message) + "{/size}{/font}":
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100
            if _yes_action:
              textbutton _("{font=misc/ProggyClean.ttf}{size=+10}Yes{/size}{/font}") action _yes_action
            if _no_action:
              textbutton _("{font=misc/ProggyClean.ttf}{size=+10}No{/size}{/font}") action _no_action
            if _ok_action:
              textbutton _("{font=misc/ProggyClean.ttf}{size=+10}Okay{/size}{/font}") action _ok_action

    # Right-click and escape answer "no".
    if _no_action:
      key "game_menu" action _no_action
    else:
      if _ok_action:
        key "game_menu" action _ok_action

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
        
    imagemap:
        ypos -8
        xpos 20
        auto "images/ui/quick_%s.png"        
        hotspot (942, 530, 54, 54) action ShowMenu("save")
        hotspot (942, 586, 54, 54) action ShowMenu("load")
        hotspot (942, 640, 54, 54) action ShowMenu("email_menu")
        hotspot (942, 690, 54, 54) action ShowMenu("preferences")

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
# Reply email Menu
#
screen draft_menu(Name=""):
    tag menu
    modal True
  
    #use mailbox_overlay_exit
    
    add "images/ui/email/email_overlay_ground.png"
    
    imagemap:
        auto "images/ui/email/email_overlay_%s.png"        
        #hotspot (830, 90, 60, 60) action Start()
        #hotspot (830, 150, 60, 60) action ShowMenu("load")
        #hotspot (830, 210, 60, 60) action ShowMenu("cg_gallery")
        #hotspot (860, 620, 50, 30) action ShowMenu("contacts") #change this to send messages
        hotspot (270, 263, 67, 25) action ShowMenu("contacts")
        hotspot (1000, 190, 40, 40) action Return()
        

    add "images/ui/email/Compose Text.png"
    label Simone_email xpos 345 ypos 236
    if (Name == ""):
      pass
    else:
      label GetAddressFromSender(Name) xpos 345 ypos 260
      
  

screen send_menu(_To, _From, _Subject, _Messages):
    tag menu
    modal True
    use send_menuDisplay(_To, _From, _Subject, _Messages)
    
screen send_menuDisplay(_To, _From, _Subject, _Messages):
  
    #use mailbox_overlay_exit
    
    add "images/ui/email/email_overlay_ground.png"
    
    imagemap:
        auto "images/ui/email/email_overlay_%s.png"        
        #hotspot (830, 90, 60, 60) action Start()
        #hotspot (830, 150, 60, 60) action ShowMenu("load")
        #hotspot (830, 210, 60, 60) action ShowMenu("cg_gallery")
        #hotspot (860, 620, 50, 30) action ShowMenu("contacts") #change this to send messages
        #hotspot (140, 263, 67, 25) action ShowMenu("contacts")
        hotspot (1000, 190, 40, 40) action Return()
        #hotspot (860, 620, 45, 25) action [Hide('send_menu'), Return("Send")]
        hotspot (990, 620, 45, 25) action [Hide('send_menu'), Return("Send")]
        

    add "images/ui/email/Compose Text.png"  
    
    vbox:
      xpos 345
      ypos 237
      text ("{color=#000}{font=misc/Inconsolata-Regular.ttf}" + GetAddressFromSender(_From) + "{/font}{/color}")
      text ("{color=#000}{font=misc/Inconsolata-Regular.ttf}" + GetAddressFromSender(_To) + "{/font}{/color}")  
      text ("{color=#000}{font=misc/Inconsolata-Regular.ttf}RE:" + _Subject + "{/font}{/color}")
      side "c r":
        area (-60,10,750,295)
        viewport id "view_message":
            draggable True mousewheel True
            vbox:                  
                vbox:
                  $i=-1
                  for _reply in reversed(_Messages): 
                    $i+=1
                    if i == 0:
                      text "{color=#000}{font=misc/Inconsolata-Regular.ttf}" + _reply + "{/font}{/color}"
                    else:
                      frame:
                        xminimum 738
                        $replytext = ""
                        for j in range(1,i):
                          $replytext += ">"
                        $replytext += _reply
                        text ("{color=#000}{font=misc/Inconsolata-Regular.ttf}>" + replytext + "{/font}{/color}")
        vbar value YScrollValue("view_message")
      
      
##############################################################################
# Main email Menu
#
screen screen_noTime():
    modal True
    hbox:
        xalign 0.5
        yalign 0.5
        style_group "file_picker_nav"

        textbutton _("I don't have time for this right now...") action Hide('screen_noTime')

screen email_menu(_modal=True):
    tag menu
    if _modal == True:
      modal True
  
    default current_message = None
    $ available_drafts = [i for i in contacts if i.draft_label]   
    #use mailbox_overlay_exit
    
    add "images/ui/email/email_ground_base.png"
    
    imagemap:
        auto "images/ui/email/email_%s.png"        
        
        #draft new
        if available_drafts:
          if EmailEnabledFlag:
            hotspot (535, 75, 80, 25) action  Show("contacts")
          else:
            hotspot (535, 75, 80, 25) action Show('screen_noTime')
        else:
          hotspot (535, 75, 80, 25) action None
          
        #reply
        if current_message and current_message.reply_label:
          if EmailEnabledFlag:
            hotspot (620, 75, 50, 25) action current_message.reply
          else:
            hotspot (620, 75, 50, 25) action Show('screen_noTime')
        else:
          hotspot (620, 75, 50, 25) action None
            
        #delete
        if current_message:
          hotspot (670, 75, 65, 25) action  [current_message.delete, SetScreenVariable("current_message", None)]
        else:
          hotspot (670, 75, 65, 25) action None
        
        #mark all read        
        if new_message_count() > 0:
            hotspot (740, 75, 105, 25) action mark_all_read
        else:
            hotspot (740, 75, 105, 25) action None
            
        #restore all
        hotspot (850, 75, 90, 25) action restore_all
        
        #exit
        hotspot (1060, 25, 35, 35) action [Hide("email_menu"), Return()] # Show("mailbox_overlay")]


    #Email display
    hbox:
      xpos 270
      ypos 70
      if new_message_count() > 0:
          text ("{size=-5}{color=#000}{font=misc/Inconsolata-Regular.ttf}- Messages: %d (%d unread){/font}{/color}{/size}") % (message_count(), new_message_count())
      else:
          text ("{size=-5}{color=#000}{font=misc/Inconsolata-Regular.ttf}- Messages: %d{/font}{/color}{/size}") % message_count()
    #frame:
        #style_group "mailbox"
    vbox:
      hbox:
        vbox:
          #label "{color=#000}{u}{b}Inbox{/b}{/}{/color}" xpos 65 ypos 150
          side "c r":
              area (193,104,321,600)
              viewport id "message_list":
                  draggable True mousewheel True
                  vbox:
                      for i in mail:
                          if i.view:
                              if not i.read:
                                  textbutton ("{font=misc/Inconsolata-Regular.ttf}*NEW* " + i.sender + " - " + i.subject + "{/font}") action [SetScreenVariable("current_message",i), i.mark_read] xfill True
                              else:
                                  textbutton ("{font=misc/Inconsolata-Regular.ttf}" + i.sender + " - " + i.subject + "{/font}") action SetScreenVariable("current_message",i) xfill True
              vbar value YScrollValue("message_list")
      #hbox:
        #  null height 20
    if current_message:          
      vbox:
        xpos 610
        ypos 108
        text ("{color=#000}{font=misc/Inconsolata-Regular.ttf}" + GetAddressFromSender(current_message.sender) + "{/font}{/color}")
        text ("{color=#000}{font=misc/Inconsolata-Regular.ttf}" + GetAddressFromSender("Simone") + "{/font}{/color}")  
        text ("{color=#000}{font=misc/Inconsolata-Regular.ttf}" + current_message.subject + "{/font}{/color}")
        side "c r":
          area (-60,10,545,510)
          viewport id "view_message":
              draggable True mousewheel True
              vbox:
                  if current_message:                  
                    vbox:
                      $i=-1
                      for _reply in reversed(current_message.body): 
                        $i+=1
                        if i == 0:
                          text "{color=#000}{font=misc/Inconsolata-Regular.ttf}" + _reply + "{/font}{/color}"
                        else:
                          frame:
                            xminimum 530
                            $replytext = ""
                            for j in range(1,i):
                              $replytext += ">"
                            $replytext += _reply
                            text ("{color=#000}{font=misc/Inconsolata-Regular.ttf}>" + replytext + "{/font}{/color}")
          vbar value YScrollValue("view_message")

screen mailbox_overlay:

    imagebutton auto "images/ui/desktop_%s.png" focus_mask True action [Hide('mailbox_overlay'), Show("email_menu")] 
    #hbox:
    #    xalign 1.0 yalign 0.0
    #    if new_message_count() > 0:
    #        textbutton "Mailbox (%d New)" % (new_message_count()) action [Hide('mailbox_overlay'), Show("email_menu")]
    #    else:
    #        textbutton "Mailbox" action [Hide('mailbox_overlay'), Show("email_menu")]

screen screen_desktop():
    add "images/ui/desktop_ground.png"
    #if TutorialInProgress:
    #  imagebutton auto "images/ui/desktop_%s.png" focus_mask True action None
    #else:  
    imagebutton auto "images/ui/desktop_%s.png" focus_mask True action [ Show("email_menu")] 
    
screen circle_highlight(_xpos=0, _ypos=0):
  add "images/ui/circle_highlight.png" xpos _xpos ypos _ypos
  
screen screen_tutorialShow(_imageno, textdisplay):
  add "images/ui/tut/%s.png"%_imageno
  add "images/ui/tut/overlay.png"
  
  frame : 
    xalign 0.5 yalign 0.7
    background "#fff"
    text "{color=#000}{font=misc/Inconsolata-Regular.ttf}" + textdisplay + "{/font}{/color}"#0.992
    #text "{color=#fff}{font=misc/Inconsolata-Regular.ttf}" + textdisplay + "{/font}{/color}" xalign 0.5 yalign 0.5#0.99
  imagebutton idle "images/ui/tut/empty.png" focus_mask None action Return()
  
##############################################################################
# Galleries Menu
#
screen gallery_nav():

          hbox:
              xpos 750
              ypos 120
              style_group "file_picker_nav"

              textbutton _("Gallery"):
                  action ShowMenu('gallery')

              textbutton _("Credits"):
                  action ShowMenu("credits")

              textbutton _("Help"):
                  action Help()
    
screen gallery():
    tag menu
    add "images/ui/menu_base.png"

    # Include the navigation.
    use navigation
    use gallery_nav
    
          
    $ columns = 3
    $ rows = 1
    $ j = 0
    $ next_cg_page = cg_page + 1     
    $ prev_cg_page = cg_page - 1          
    if next_cg_page > int(len(gallery_cg_items)/gal_cells):
        $ next_cg_page = int(len(gallery_cg_items)/gal_cells)       
    if prev_cg_page < 0:
        $ prev_cg_page = 0
        
    for gal_item in gallery_cg_items:      
      $ j += 1
      $index = j
      if (index > int(columns*rows)):
        $index = j - int(columns*rows*cg_page)
      $ipos = 170*int((index-1)/columns)
      $index = ((j-1)%columns) + 1
      $jpos = 220*(index-1)
        
      if j <= (cg_page+1)*gal_cells and j>cg_page*gal_cells: 
        #frame:
          #
          #if j> 1:
          #  imagebutton auto "images/ui/savebox_%s.png" focus_mask None  xpos 275+jpos ypos (270+ipos) #action pass
          #else:
            add g_cg.make_button(gal_item + " butt", gal_item + " butt", "images/ui/savebox_insensitive.png", xpos=405+jpos-1, ypos=(270+ipos)+10, background=None)
            #add im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y) xpos 275+jpos+10 ypos (270+ipos)+10
            imagebutton auto "images/ui/savebox_%s.png" focus_mask None  xpos 405+jpos ypos (270+ipos) action gal_item + " butt"
            vbox:
              area (445+jpos+10,(450+ipos)+10,200,100)
              style_group "file_picker_nav"
              #xpos 310+jpos+10 ypos (450+ipos)+10
              $title = gallery_cg_titles[j-1]
              text "{color=#000}{font=misc/Inconsolata-Regular.ttf}[title]{/font}{/color}"
            vbox:
              style_group "file_picker_nav"
              textbutton _("Replay") action Start() xpos 445+jpos+20 ypos (450+ipos)+60
          
        
        #add g_cg.make_button(gal_item + " butt", gal_item + " butt", "images/ui/savebox_ground.png",  xpos=275+jpos, ypos=(170+ipos), idle_border="images/ui/savebox_idle.png", hover_border="images/ui/savebox_hover.png", background=None, left_padding=9,top_padding=6)

    #imagemap:
    #    auto "images/ui/menu_pagenav_%s.png" alpha False        
    #    if cg_page > 0:    
    #      hotspot (800, 115, 60, 65)  action [SetVariable('cg_page', prev_cg_page), ShowMenu("gallery")]
    #    for i in range(1, 5):
    #      if (i-1 < int(len(gallery_cg_items)/gal_cells)+1):
    #        hotspot (800+(63*i), 115, 60, 65)  action [SetVariable('cg_page', i-1), ShowMenu("gallery")]  
    #      text "{size=40}{b}[i]{/b}{/size}"  xpos 815+(63*i) ypos 125
    #    if cg_page < int(len(gallery_cg_items)/gal_cells):
    #      hotspot (1115, 115, 60, 65)  action [SetVariable('cg_page', next_cg_page), ShowMenu("gallery")]
          
          
    vbox:    
      null  height 30
      frame:
        background None
        area (400,125,690,550)
        style "file_picker_frame"
        frame:
          background None
          ypos 450
          # The buttons allow the user to pick a
          # page of files.
          hbox:
          
              style_group "file_picker_nav"
    
              textbutton _("Previous"):
                  action [SetVariable('cg_page', prev_cg_page)]
    
              for i in range(1, 8):
                if (i-1 < int(len(gallery_cg_items)/gal_cells)+1):
                  textbutton str(i):
                      action  [SetVariable('cg_page', i-1)]
    
              textbutton _("Next"):
                  action [SetVariable('cg_page', next_cg_page)]
                  
screen credits():
    tag menu
    add "images/ui/menu_credits.png"

    # Include the navigation.
    use navigation
    use gallery_nav
    
init python:
    #Galleries settings - start
    #list the CG gallery images here:
    gallery_cg_items = ["bg office","bg office2","bg office3","bg office4", ]
    gallery_cg_titles = ["Joel: Gentle Giant","$olomon","Magic Milo", "Forever Alone",]
    #how many rows and columns in the gallery screens?
    gal_rows = 3
    gal_cols = 1
    #thumbnail size in pixels:
    thumbnail_x = 207
    thumbnail_y = 150
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

#-------------------------------------------------------  

init python:
    TimeOfDay = ['Morning', 'Noon', 'Afternoon', 'Evening', 'Night']
    TODXOffset = 256
    
init -2:
    transform TOD_eff(_oldY, _moveToY):
      ypos _oldY
      time 0.5
      linear 0.8 ypos _moveToY
      
screen screen_TOD():

  add "images/ui/TOD/TOD_bg.png" xpos TODXOffset
  add "images/ui/TOD/TOD_sidebar.png" xpos TODXOffset
  $oldYPos = 240+83*(currentTimeOfDay-1)
  $newYPos = 240+83*currentTimeOfDay
  if (currentTimeOfDay-1 < 0):
    $oldYPos = 240+83*(4)
    
  add "images/ui/TOD/TOD_indicator.png" xpos 745+TODXOffset ypos at TOD_eff(oldYPos, newYPos)
  add "images/ui/TOD/TOD_sidebar_Text.png" xpos TODXOffset
  
  #add "images/ui/TOD/TOD_noon.png"
  #add "images/ui/TOD/TOD_afternoon.png"
  #add "images/ui/TOD/TOD_evening.png"
  #add "images/ui/TOD/TOD_night.png"
  use screen_TOD_indicator
  
screen screen_TOD_indicator():
  $timeImage = TimeOfDay[currentTimeOfDay]
  #text "[timeImage]"
  add "images/ui/TOD/TOD_%s.png"%timeImage xpos TODXOffset
  
screen screen_TOD_indicator_sml():
  $timeImage = TimeOfDay[currentTimeOfDay]
  add "images/ui/TOD/Banner.png" xpos TODXOffset
  add "images/ui/TOD/%s Indicator.png"%timeImage xpos TODXOffset
  #text "[timeImage]"
  #$ratio = 2
  #$x = 1024/ratio
  #$y = 768/ratio
  #add "images/ui/TOD/TOD_corner.png"
  #add im.Scale("images/ui/TOD/TOD_%s.png"%timeImage, x,y) xpos x+20 ypos -10
#-------------------------------------------------------  

screen office_work:
    imagemap:
        ground "images/ui/Overlay.png"
        idle "images/ui/icons_idle.png"
        hover "images/ui/icons_hover.png"
        
        hotspot (183, 202, 146, 148) clicked Return("coffee") #go_out coffee
        hotspot (224, 497, 146, 148) clicked Return("call") #conf call
        hotspot (454, 349, 146, 148) clicked Return("milo") #milo
        hotspot (898, 127, 146, 148) clicked Return("solomon") #solomon
        hotspot (851, 349, 146, 148) clicked Return("joel") #joel
        hotspot (964, 499, 146, 148) clicked Return ("kitchen") #kitchen