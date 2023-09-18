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
                #if (who == "<Dynamic>"):
                #  pass
                #else:
                #  if (who == None):
                #    pass
                #  else:
                #$current_speaker = who
                #$childNum = SelectChildByName(who)
                #text "This is [current_speaker], child number [childNum]" xalign 0.5 yalign 0.5
                #$current_speaker_number = SelectCharacterByName(who)
                #$SetCurrentCharacterNumber(current_speaker_number)
                #text "This is [current_speaker], character number [current_speaker_number]" xalign 0.5 yalign 0.5

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
    #-- Set to no current character for choice menu, so the info button doesnt show up during choices --#
    $current_speaker = ''
    $SetCurrentCharacterNumber(-1)
    #--
    window:
        style "menu_window"
        #xalign 0.5
        #yalign 0.5

        #vbox:
        #    style "menu"
        #    spacing 1
        $Xpos = 270
        $Ypos = 830
        $i=0
        $j=0
        $max_column = 2
        for caption, action, chosen in items:
            if i >= max_column:
              $i = 0
              $j+=1
            if action:

                use boardButton( caption, action, Xpos + 400*j, Ypos + 55*i, 0, 0)            
            else:
                use boardButton( caption, pass, Xpos + 400*j, Ypos + 55*i, 0, 0)
              #text "{font=assets/PermanentMarker.ttf}{size=18}{color=#ffffff}{i}[caption]{/i}{/color}{/size}{/font}" xpos (Xpos +20 + 200*j) ypos (Ypos +25 + 35*i)
                
            $i+=1

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
    #add "img/ui/blackboardFull.png" 
    #add "img/ui/blackboard_doodle.png" 
    #text "{font=assets/PermanentMarker.ttf}{size=80}{color=#ffffff}Echidnas{/color}{/size}{/font}" xalign 0.5 yalign 0.25
    #text "{font=assets/PermanentMarker.ttf}{size=40}{color=#ffffff}School for Little Monsters{/color}{/size}{/font}" xalign 0.5 yalign 0.37
    #
    #
    #use boardButton( "Start Game", Start(), 300, 270, 10)
    #use boardButton( "Load Game", ShowMenu("load"), 300, 320, 10)
    #use boardButton( "Preferences", ShowMenu("preferences"), 300, 370, 10)
    #use boardButton( "Help", Help(), 300, 420, -10)
    #use boardButton( "Quit", Quit(confirm=False), 300, 470, -10)
    
    
    #imagemap:
    #  ground "img/ui/MainMenu_ground.png"
    #  idle "img/ui/MainMenu_idle.png"
    #  hover "img/ui/MainMenu_hover.png"
    #  
    #  hotspot (90, 255, 260, 115) action Start() hovered Play("sound", "sound/sfx/chalk_stick_single_stroke_on_chalk_board_003.ogg")
    #  hotspot (460, 275, 190, 80) action ShowMenu("load") hovered Play("sound", "sound/sfx/chalk_stick_single_stroke_on_chalk_board_003.ogg")
    #  hotspot (390, 370, 175, 80) action ShowMenu("preferences")  hovered Play("sound", "sound/sfx/chalk_stick_single_stroke_on_chalk_board_003.ogg")
    #  hotspot (245, 430, 120, 55) action Help()  hovered Play("sound", "sound/sfx/chalk_stick_single_stroke_on_chalk_board_003.ogg")
    #  hotspot (120, 475, 90, 45) action Quit(confirm=False)  hovered Play("sound", "sound/sfx/chalk_stick_single_stroke_on_chalk_board_003.ogg")
    
    imagemap:
      ground "img/ui/main_menu_ground.png"
      idle "img/ui/main_menu_idle.png"
      hover "img/ui/main_menu_hover.png"
      alpha False
      
      hotspot (820, 385, 300, 70) action Start() hovered Play("sound", "sound/sfx/chalk_stick_single_stroke_on_chalk_board_003.ogg")
      hotspot (820, 471, 300, 70) action ShowMenu("load") hovered Play("sound", "sound/sfx/chalk_stick_single_stroke_on_chalk_board_003.ogg")
      hotspot (820, 535, 300, 70) action ShowMenu("preferences")  hovered Play("sound", "sound/sfx/chalk_stick_single_stroke_on_chalk_board_003.ogg")
      hotspot (820, 621, 300, 70) action Help()  hovered Play("sound", "sound/sfx/chalk_stick_single_stroke_on_chalk_board_003.ogg")
      #hotspot (820, 690, 300, 70) action ShowMenu("extras")  hovered Play("sound", "sound/sfx/chalk_stick_single_stroke_on_chalk_board_003.ogg")
      hotspot (820, 778, 300, 70) action Quit(confirm=False)  hovered Play("sound", "sound/sfx/chalk_stick_single_stroke_on_chalk_board_003.ogg")
      
    #add "img/ui/main_menu_extra.png"


init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



##############################################################################
screen boardButton(buttonText, DoAction, Xpos, Ypos, Xoffset, Yoffset=0, fontsize=32):
    
    $ydiff = 20
    $xdiff = 25
    #imagebutton auto "img/ui/boardselect_big_%s.png" xpos Xpos+Xoffset ypos Ypos+Yoffset action DoAction
    imagebutton auto "img/ui/boardselect_%s.png" xpos Xpos+Xoffset ypos Ypos+Yoffset action DoAction
    text "{font=assets/PermanentMarker.ttf}{size=[fontsize]}{color=#ffffff}[buttonText]{/color}{/size}{/font}" xpos Xpos+xdiff ypos Ypos+ydiff
    
##############################################################################
screen boardBar( BarName, BarValue, ValueString, xPos, yPos, _big=False):
    if (_big):
      text "{font=assets/PermanentMarker.ttf}{size=28}{color=#ffffff}[BarName]{/color}{/size}{/font}" xpos xPos ypos yPos
      bar value BarValue:
        style_group "pref"    
        xpos xPos+220 
        ypos yPos
        range 100 
        xmaximum 312 
        ymaximum 50   
        #yminimum 50      
      text "{font=assets/PermanentMarker.ttf}{size=24}{color=#ffffff}- [ValueString]{/color}{/size}{/font}" xpos xPos+540 ypos yPos+5
    else:
      text "{font=assets/PermanentMarker.ttf}{size=18}{color=#ffffff}[BarName]{/color}{/size}{/font}" xpos xPos ypos yPos
      bar value BarValue:
        style_group "pref"    
        xpos xPos+120 
        ypos yPos
        range 100 
        xmaximum 212      
      text "{font=assets/PermanentMarker.ttf}{size=14}{color=#ffffff}- [ValueString]{/color}{/size}{/font}" xpos xPos+340 ypos yPos+5
    
##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    #window:
    #    style "gm_root"

    # The various buttons.
     
    $xOffset = 320
    
    use boardButton( "Return", [Hide("calender_day"), Return()], 50 + xOffset, 920, 0)
    use boardButton( "Preferences", [Hide("calender_day"), ShowMenu("preferences")], 200 + xOffset, 920, 20)
    use boardButton( "Save", [Hide("calender_day"), ShowMenu("save")], 450 + xOffset, 920, -10)
    use boardButton( "Load", [Hide("calender_day"), ShowMenu("load")], 570 + xOffset, 920, -10)
    use boardButton( "Main Menu", [Hide("calender_day"), MainMenu()], 700 + xOffset, 920, 10)
    use boardButton( "Help", Help(), 940 + xOffset, 920, -10)
    use boardButton( "Quit", Quit(), 1060 + xOffset, 920, -10)
    use boardButton( "DEBUG", [Hide("calender_day"), ShowMenu("character_menu_debug")], 1340 + xOffset, 920, -10)
    
    
    
    #use boardButton( "Journal", [Hide("calender_day"), ShowMenu("journal_menu")], 1650, 920, 10)
    #use boardButton( "Calender", [Hide("calender_day"), ShowMenu("calender_menu")], 550, 470, 10)
    #use boardButton( "Characters", [Hide("calender_day"), ShowMenu("character_menu")], 550, 500, 10)

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"
        
    define config.thumbnail_height = config.screen_height/12
    define config.thumbnail_width = config.screen_width/12


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


    use boardButton( "Previous", FilePagePrevious(), 160, 160, 10)
    use boardButton( "Auto", FilePage("auto"), 340, 160, -5)
    use boardButton( "Quick", FilePage("quick"), 440, 160, -5)
    for i in range(1, 8):
      use boardButton( i, FilePage(i), 550+(40*i), 160, -20)
    use boardButton( "Next", FilePageNext(), 860, 160, -10)
    
    $ columns = 2
    $ rows = 5

    for i in range(1, columns * rows + 1):
      $index = i
      $jpos = 460*int((i-1)/rows)
      #if (i > rows):
      $index = ((i-1)%rows) + 1
      $ipos = 130*(index-1)
      imagebutton auto "img/ui/savebox_%s.png" xpos 230+jpos ypos (230+ipos) focus_mask None action FileAction(i)
      add FileScreenshot(i) xpos 250+jpos ypos (255+ipos)
      $ file_name = FileSlotName(i, columns * rows)
      $ file_time = FileTime(i, empty=_("Empty Slot."))
      $ save_name = FileSaveName(i) 
      text "{font=assets/PermanentMarker.ttf}{color=#ffffff}{size=24}[file_name]. {b}[file_time!t]{/b}\n[save_name!t]{/size}{/color}{/font}"  xpos 450+jpos ypos (270+ipos)
      
      key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu
    #hide any calender details that might be shown
    add "img/ui/Blackboard_big.png" 
    text "{font=assets/PermanentMarker.ttf}{size=40}{color=#ffffff}{u}Save{/u}{/color}{/size}{/font}" xpos 100 ypos 100

    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu
    add "img/ui/Blackboard_big.png" 
    text "{font=assets/PermanentMarker.ttf}{size=40}{color=#ffffff}{u}Load{/u}{/color}{/size}{/font}" xpos 100 ypos 100

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

screen preferences():

    $Col_1_Head_XPos = 200
    $Col_2_Head_XPos = 670
    $Col_3_Head_XPos = 1140
    $Col_1_SubHead_XPos = 250
    $Col_2_SubHead_XPos = 720
    $Col_3_SubHead_XPos = 1190
    $Table_offsetX = 350

    tag menu
    add "img/ui/Blackboard_big.png" 
    text "{font=assets/PermanentMarker.ttf}{size=40}{color=#ffffff}{u}Preferences{/u}{/color}{/size}{/font}" xpos 100 ypos 100

    # Include the navigation.
    use navigation

    text "{font=assets/PermanentMarker.ttf}{size=38}{color=#ffffff}Display{/color}{/size}{/font}" xpos Col_1_Head_XPos ypos 200
    use boardButton( "Window", Preference("display", "window"), Col_1_SubHead_XPos, 240, 5)
    use boardButton( "Fullscreen", Preference("display", "fullscreen"), Col_1_SubHead_XPos, 280, 10)
    
    text "{font=assets/PermanentMarker.ttf}{size=38}{color=#ffffff}Transitions{/color}{/size}{/font}" xpos Col_1_Head_XPos ypos 380
    use boardButton("All", Preference("transitions", "all"), Col_1_SubHead_XPos, 430, -10)
    use boardButton("None", Preference("transitions", "none"), Col_1_SubHead_XPos, 470, -10)

    text "{font=assets/PermanentMarker.ttf}{size=38}{color=#ffffff}Text Speed{/color}{/size}{/font}" xpos Col_1_Head_XPos ypos 540
    bar value Preference("text speed"):
      style_group "pref"    
      xpos Col_1_Head_XPos + Table_offsetX 
      ypos 600

    use boardButton("Joystick...", Preference("joystick"), Col_1_Head_XPos, 650, 5)
    
    
    text "{font=assets/PermanentMarker.ttf}{size=38}{color=#ffffff}Skip{/color}{/size}{/font}" xpos Col_2_Head_XPos ypos 200
    use boardButton( "Seen Messages", Preference("skip", "seen"), Col_2_SubHead_XPos, 240, 20)
    use boardButton( "All Messages", Preference("skip", "all"), Col_2_SubHead_XPos, 280, 20)
    
    use boardButton( "Begin Skipping",  Skip(), Col_2_SubHead_XPos, 340, 10)
    
    text "{font=assets/PermanentMarker.ttf}{size=38}{color=#ffffff}After Choices{/color}{/size}{/font}" xpos Col_2_Head_XPos ypos 450
    use boardButton( "Stop Skipping", Preference("after choices", "stop"), Col_2_SubHead_XPos, 480, 20)
    use boardButton( "Keep Skipping", Preference("after choices", "skip"), Col_2_SubHead_XPos, 510, 20)
    
    text "{font=assets/PermanentMarker.ttf}{size=38}{color=#ffffff}Auto-Forward Time{/color}{/size}{/font}" xpos Col_2_Head_XPos ypos 600
    bar value Preference("auto-forward time"):
      style_group "pref"    
      xpos Col_2_Head_XPos + Table_offsetX 
      ypos 650
    if config.has_voice:
        use boardButton( "Wait for Voice", Preference("wait for voice", "toggle"), Col_3_SubHead_XPos, 600, 20)
    
    
    text "{font=assets/PermanentMarker.ttf}{size=38}{color=#ffffff}Music Volume{/color}{/size}{/font}" xpos Col_3_Head_XPos ypos 200
    bar value Preference("music volume"):
      style_group "pref"    
      xpos Col_3_Head_XPos + Table_offsetX  
      ypos 250
    text "{font=assets/PermanentMarker.ttf}{size=38}{color=#ffffff}Sound Volume{/color}{/size}{/font}" xpos Col_3_Head_XPos ypos 300
    bar value Preference("sound volume"):
      style_group "pref"    
      xpos Col_3_Head_XPos + Table_offsetX   
      ypos 350
    
    if config.sample_sound:
      use boardButton( "Test Sound",  Play("sound", config.sample_sound), Col_3_SubHead_XPos, 360, 20)
    
    if config.has_voice:
      text "{font=assets/PermanentMarker.ttf}{size=38}{color=#ffffff}Voice Volume{/color}{/size}{/font}" xpos Col_3_Head_XPos ypos 400
      bar value Preference("voice volume"):
        style_group "pref"    
        xpos Col_3_Head_XPos + Table_offsetX   
        ypos 450
      if config.sample_voice:
        use boardButton( "Test Voice",  Play("voice", config.sample_voice), Col_3_SubHead_XPos, 500, 20)
      use boardButton( "Voice Sustain",  Preference("voice sustain", "toggle"), Col_3_SubHead_XPos, 550, 20)


init -2:
    style pref_frame:
        background None
        xfill False
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 300#192
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
    
    add "img/ui/Blackboard_big.png" 
    
    $newMessage = message
    if message == layout.ARE_YOU_SURE:
      $newMessage  = _("Are you sure?")
    if message == layout.DELETE_SAVE:
      $newMessage  = _("Are you sure you want to delete this save?")
    if message == layout.OVERWRITE_SAVE:
      $newMessage  = _("Are you sure you want to overwrite your save?")
    if message == layout.LOADING:
      $newMessage  = _("Loading will lose unsaved progress.\nAre you sure you want to do this?")
    if message == layout.QUIT:
      $newMessage  = _("Are you sure you want to quit?")
    if message == layout.MAIN_MENU:
      $newMessage  = _("Are you sure you want to return to the main menu?\nThis will lose unsaved progress.")
    if message == layout.SLOW_SKIP:
      $newMessage  = _("Are you sure you want to begin skipping?")
    if message == layout.FAST_SKIP_UNSEEN:
      $newMessage  = _("Are you sure you want to skip to the \nnext choice?")
    if message == layout.FAST_SKIP_SEEN:
      $newMessage  = _("Are you sure you want to skip to \nunseen dialogue or the next choice?")

    text "{font=assets/PermanentMarker.ttf}{size=50}{color=#ffffff}[newMessage]{/color}{/size}{/font}" xalign 0.5 yalign 0.3
      
    use boardButton( "Yes",  yes_action, 675, 500, 0, 28, 46)
    use boardButton( "No",  no_action, 1050, 500, 0, 28, 46)

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

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 0.80 
        yalign 0.95

        textbutton _("{font=assets/PermanentMarker.ttf} Back{/font}") action Rollback()
        textbutton _("{font=assets/PermanentMarker.ttf} Save{/font}") action ShowMenu('save')
        textbutton _("{font=assets/PermanentMarker.ttf} Q.Save{/font}") action QuickSave()
        textbutton _("{font=assets/PermanentMarker.ttf} Q.Load{/font}") action QuickLoad()
        textbutton _("{font=assets/PermanentMarker.ttf} Skip{/font}") action Skip()
        textbutton _("{font=assets/PermanentMarker.ttf} F.Skip{/font}") action Skip(fast=True, confirm=True)
        textbutton _("{font=assets/PermanentMarker.ttf} Auto{/font}") action Preference("auto-forward", "toggle")
        textbutton _("{font=assets/PermanentMarker.ttf} Prefs{/font}") action ShowMenu('preferences')
        textbutton _("{font=assets/PermanentMarker.ttf}  {/font}") 
        textbutton _("{font=assets/PermanentMarker.ttf} Journal{/font}") action ShowMenu('journal_menu')
        
    
    #use boardButton( "?", ShowMenu("current_character_menu"), 265, 720, 10)
    #$charNum = SelectCharacterByName(current_speaker)
    if ( not current_speaker_number == -1):
      $XOffset = GetCurrentCharacterNameLength() * 20
      imagebutton auto "img/ui/button_info_%s.png" xpos 220 + XOffset ypos 800 focus_mask None  action ShowMenu('current_character_menu')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 26
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

    
##############################################################################
# Daily UI Menu
#
#
screen day_menu():
  add "img/ui/dateTime.png"
  
  vbox:
    xpos 680
    ypos 50
    $date = current_date
    $month = MonthsOfTheYear[current_month][1]
    $day = weekDay(current_year, current_month+1, current_date )[1]
    $timeOfDay = current_time 
    text "{font=assets/PermanentMarker.ttf}{size=16}{color=#000000}[date] // [month] \n[day] \n[timeOfDay] {/color}{/size}{/font}"
    
    
##############################################################################
# Calender UI Menu
#
#

init python:
  DisplayMonthOffset = 0
  DisplayYearOffset = 0
  
screen calender_menu():
  tag menu
  
  add "img/ui/Blackboard_big.png" 
  use journal_nav_menu
  #use navigation
  
  $boardStartX = 400
  $boardStartY = 120
  #add "img/ui/backblue.png" 
    
  $nextmonth = DisplayMonthOffset+1
  $prevmonth = DisplayMonthOffset-1
  $nextyear = DisplayYearOffset
  $prevyear = DisplayYearOffset
  #if (prevmonth < 1-current_month):
  #  $prevmonth = 12
  
  if (current_month + nextmonth > 11):
    $nextmonth = 0-current_month
    $nextyear = DisplayYearOffset+1
    
  if (current_month + prevmonth < 1):
    $prevmonth = 11-current_month
    $prevyear = DisplayYearOffset-1
  
  use boardButton( "<", [SetVariable('DisplayMonthOffset', prevmonth), SetVariable('DisplayYearOffset', prevyear)], -10+boardStartX, -90+boardStartY, -5, 35, 64)
  use boardButton( ">", [SetVariable('DisplayMonthOffset', nextmonth), SetVariable('DisplayYearOffset', nextyear)], 350+boardStartX, -90+boardStartY, -5, 35, 64)
    
  $displayMonth = current_month + DisplayMonthOffset
  $displayYear = current_year + DisplayYearOffset
  
  $columns = 7
  $rows = 6
  $MaxDaysInCalender = columns*rows
  $daysInMonth = MonthsOfTheYear[displayMonth][2]
  $i=0
  $index = 0
  $FirstDay = weekDay(displayYear, displayMonth+1, 1 )[0]-1
  $FirstDay2 = weekDay(displayYear, displayMonth+1, 1 )[1]
  
  #if the month starts on a sunday it returns -1 and causes trouble with the layout. :(
  if (FirstDay == -1):
    $FirstDay = 6
    
  
  if (gbl_SavedYear != displayYear):
    $SetSpecialEvents(displayYear)
    $gbl_SavedYear = displayYear
    
  $monthName = MonthsOfTheYear[displayMonth][0]
  text "{font=assets/PermanentMarker.ttf}{size=54}{u}[monthName]{/u}{/size}{/font}"  xpos 80+boardStartX ypos -60+boardStartY
  #text "{font=assets/PermanentMarker.ttf}{size=34}{u}[monthName] [displayYear]{/u}{/size}{/font}"  xpos 0+boardStartX ypos -50+boardStartY
  #text "{font=assets/PermanentMarker.ttf}{u}[displayYear]-[displayMonth]-[current_date]{/u}{/font}"  xpos 60+boardStartX ypos 15
  #text "{font=assets/PermanentMarker.ttf}{u}.[DisplayMonthOffset] .[DisplayYearOffset] // .[nextmonth] .[prevmonth]{/u}{/font}"  xpos 260+boardStartX ypos 15
  
  for day_name in DaysOfTheWeek:  
    $index +=1
    $jpos = 140*(index)
    text "{font=assets/PermanentMarker.ttf}{size=28}[day_name[1]]{/size}{/font}"  xpos -10+jpos+boardStartX ypos 20+boardStartY
  
  $bonce = True
  for j in range(1, MaxDaysInCalender):
    $index = j
    $ipos = 140*int((index-1)/columns)
    $index = ((j-1)%columns) + 1
    $jpos = 140*(index-1)
    if bonce:
      #text "[j] - [FirstDay] /  [FirstDay2]" xpos 100 ypos 100
      $bonce =  False
    if (j > FirstDay and i < daysInMonth):
      $i+=1
      imagebutton auto "img/ui/Calenderbox_%s.png" xpos 100+jpos+boardStartX ypos (75+ipos+boardStartY) focus_mask None action ShowMenu("calender_day",displayYear, displayMonth, i)
      text "{font=assets/PermanentMarker.ttf}{size=34}[i]{/size}{/font}"  xpos 115+jpos+boardStartX ypos (85+ipos+boardStartY)
      #hightlight current day
      if (i ==  current_date and displayYear == current_year and displayMonth == current_month):
        add "img/ui/Calenderbox_selected.png" xpos 100+jpos+boardStartX ypos (75+ipos+boardStartY)
      #hightlight days with events
      if (DayHasEvent(displayYear, displayMonth+1, i)):
        add "img/ui/Calender_EventMarker.png" xpos 100+jpos+boardStartX ypos (75+ipos+boardStartY)
      
##############################################################################
# Calender Chosen Date Details Menu
#
#
screen calender_day(chosenyear, chosenmonth, chosenday):
    $boardStartX = 900
    $boardStartY = 50
    $date = current_date
    $month = MonthsOfTheYear[chosenmonth][1]
    $day = weekDay(chosenyear, chosenmonth+1, chosenday )[1]
    $dayNum = weekDay(chosenyear, chosenmonth+1, chosenday )[0]
    $timeOfDay = current_time 
    $Events = [ ("Morning", "Nothing"), 
                ("First Period", "Nothing"),
                ("Lunch", "Nothing"),
                ("Second Period", "Nothing"),
                ("After School", "Nothing")]
    $WeekendEvents = [ ("Morning", "Nothing"), 
                ("Evening", "Nothing")]
                
    $Events2 = GetEventList(chosenyear, chosenmonth+1, chosenday )
    #$WeekendEvents = GetEventList(chosenyear, chosenmonth+1, chosenday )
    #if (dayNum < 6 and dayNum > 0):
    #  text "{font=assets/PermanentMarker.ttf}{size=14}{color=#ffffff}[chosenday] [month] \n[day] \n\n[Events[0][0]] \n-[Events[0][1]]\n\n[Events[1][0]] \n-[Events[1][1]]\n\n[Events[2][0]] \n-[Events[2][1]]\n\n[Events[3][0]] \n-[Events[3][1]]\n\n[Events[4][0]] \n-[Events[4][1]] {/color}{/size}{/font}" xpos 600+boardStartX ypos 55+boardStartY
    #else:
    #  text "{font=assets/PermanentMarker.ttf}{size=14}{color=#ffffff}[chosenday] [month] \n[day] \n\n[WeekendEvents[0][0]] \n-[WeekendEvents[0][1]]\n\n[WeekendEvents[1][0]] \n-[WeekendEvents[1][1]] {/color}{/size}{/font}" xpos 600+boardStartX ypos 55+boardStartY
    text "{font=assets/PermanentMarker.ttf}{size=38}{color=#ffffff}[chosenday] [month] \n  [day]  {/color}{/size}{/font}" xpos 580+boardStartX ypos 55+boardStartY
    $y=1
    for Period in Events2:
      $y+=1
      text "{font=assets/PermanentMarker.ttf}{size=34}{color=#ffffff}[Period[0]]:\n  - {size=28}[Period[1]]{/size} {/color}{/size}{/font}" xpos 600+boardStartX ypos 35+boardStartY+(y*100)
    #text "{font=assets/PermanentMarker.ttf}{size=14}{color=#ffffff}[Events2] {/color}{/size}{/font}" xpos 600+boardStartX ypos 85+boardStartY+(y*30)
    
##############################################################################
# School Map UI Menu
#
#
screen map_school:
    add "img/ui/map/school/map_school_ground.png"
    imagebutton auto "img/ui/map/school/map_school_canteen_%s.png"  xpos 0 ypos 0 focus_mask True action Return("canteen")
    imagebutton auto "img/ui/map/school/map_school_classA_%s.png"  xpos 0 ypos 0 focus_mask True action Return("classA")
    imagebutton auto "img/ui/map/school/map_school_classB_%s.png"  xpos 0 ypos 0 focus_mask True action Return("classB")
    imagebutton auto "img/ui/map/school/map_school_classC_%s.png"  xpos 0 ypos 0 focus_mask True action Return("classC")
    imagebutton auto "img/ui/map/school/map_school_hallway_%s.png"  xpos 0 ypos 0 focus_mask True action Return("hallway")
    imagebutton auto "img/ui/map/school/map_school_office_%s.png"  xpos 0 ypos 0 focus_mask True action Return("office")
    imagebutton auto "img/ui/map/school/map_school_outside_%s.png"  xpos 0 ypos 0 focus_mask True action Return("outside")
    imagebutton auto "img/ui/map/school/map_school_playground_%s.png"  xpos 0 ypos 0 focus_mask True action Return("playground")
    imagebutton auto "img/ui/map/school/map_school_staffroom_%s.png"  xpos 0 ypos 0 focus_mask True action Return("staffroom")
    imagebutton auto "img/ui/map/school/map_school_storage_%s.png"  xpos 0 ypos 0 focus_mask True action Return("storage")
    imagebutton auto "img/ui/map/school/map_school_toilets_%s.png"  xpos 0 ypos 0 focus_mask True action Return("toilets")
     
##############################################################################
# Character Menu
#
#
init python:
  currentCharacter = 0
  currentScreen = "Stats"
  
screen current_character_menu():
  $charNum = SelectCharacterByName(current_speaker)
  #text "[current_speaker] = [charNum]"
  #$current_speaker_number = SelectCharacterByName(who)
  #text "This is [current_speaker], character number [current_speaker_number]" xalign 0.5 yalign 0.5
  use character_menu(False, int(charNum)+1)
  
screen character_menu(isPlayer = False, _currentDisplayCharacter = -1):

    tag menu
    add "img/ui/Blackboard_big.png" 
    use journal_nav_menu
    
    $menuOffsetX = 600
    
    $char_max = CharacterCount
    $bar_valuemax = 100
    $bar_xmax = 212
    
    if (not _currentDisplayCharacter == -1):
      $currentCharacter = int(_currentDisplayCharacter)
    
    #$char_name = "Fumi Yuji"
    #$bar_relationship = 9
    #$bar_happiness = 50
    $isAChild = ((isPlayer == False) and (currentCharacter > AdultCount-1))
    
    #show current character 
    #if currentCharacter == 0:
    #  add "img/sprites/teacher/teach1_happy.png"
    #  $char_name = "Fumi Yuji"
    #  $bar_relationship = 69
    #  $bar_happiness = 70
    #  $isAChild = False
    #if currentCharacter == 1:
    #  add "img/sprites/teacher/teach2_oh.png"
    #  $char_name = "Margaret"
    #  $bar_relationship = 9
    #  $bar_happiness = 40
    #  $isAChild = False
    
    #generate a new character
    if (currentCharacter > CharacterCount):
      $Character = GetClassAverage()
    else:
      if (isPlayer):
        $Character = PLAYER_LIST[0]
        $Character.Name = "Player"
      else: 
        if (isAChild):
          $Character = CHILD_LIST[currentCharacter-AdultCount-1]
        else:
          $Character = ADULT_LIST[currentCharacter-1]
        #$Chrarater.Age = renpy.random.randint(22,32) # TODO: build this into the class?
      #$Character = CharacterClass()
      #$Character.RandomizeStats()
      #$Character.RandomizeAppearance()
    #$Character.RandomizeStats()
    $char_name = Character.Name
    $bar_relationship = Character.Relationship
    $bar_happiness = Character.Happiness
    
    $bar_English = Character.English
    $bar_Science = Character.Science
    $bar_Maths   = Character.Maths
    $bar_Art     = Character.Art
    $bar_Music   = Character.Music
    $bar_PE      = Character.PE
    if(Character.IsUnique):
      add Character.UniqueAppearance yalign 1.0 xalign 0.25
    if (isAChild):
        if(currentCharacter <= CharacterCount):
            add Character.Appearance() yalign 1.0 xalign 0.25
        else:
            $ratio = 0.4
            add im.Scale("img/sprites/student/ClassAverageSillouette.png", 1305*ratio, 1623*ratio) yalign 1.0  xalign 0.25
    # Include the navigation.
    use navigation
    
    text "{font=assets/PermanentMarker.ttf}{size=60}{color=#ffffff}{u}Character Status{/u}{/color}{/size}{/font}" xpos 250 + menuOffsetX ypos 50

    $HappinessString = GetHappinessString(bar_happiness)
    $RelationshipString = GetRelationshipString(bar_relationship, isAChild)
    
    $nextchar = currentCharacter+1
    $prevchar = currentCharacter-1
    if (prevchar < 0):
      $prevchar = 0
      
    if (nextchar > char_max+1):
      $nextchar = char_max+1
    
    text "{font=assets/PermanentMarker.ttf}{size=48}{color=#ffffff}[char_name]{/color}{/size}{/font}" xpos 0 + menuOffsetX ypos 200
    #use boardButton( "Show Bio", [SetVariable('currentScreen', "Bio")], 350 + menuOffsetX, 310, 110)
    #use boardButton( "Show Stats", [SetVariable('currentScreen', "Stats")], 550 + menuOffsetX, 310, 110)
    
    if(isPlayer == False and _currentDisplayCharacter == -1):
      use boardButton( "<", [SetVariable('currentCharacter', prevchar)], -200 + menuOffsetX, 170, -10, 35, 50)
      use boardButton( ">", [SetVariable('currentCharacter', nextchar)], 550 + menuOffsetX, 170, -10, 35, 50)
    
    use boardBar("Happiness", bar_happiness, HappinessString, 420 + menuOffsetX, 370, True) 
    use boardBar("Relationship", bar_relationship, RelationshipString, 420 + menuOffsetX, 420, True) 
    
    #if (currentScreen == "Bio"):
    text "{font=assets/PermanentMarker.ttf}{size=18}{color=#ffffff}{i}Name:{/i}   [Character.Name]{/color}{/size}{/font}" xpos 220 + menuOffsetX ypos 470
    text "{font=assets/PermanentMarker.ttf}{size=18}{color=#ffffff}{i}Age:{/i}   [Character.Age]{/color}{/size}{/font}" xpos 220 + menuOffsetX ypos 490
    text "{font=assets/PermanentMarker.ttf}{size=18}{color=#ffffff}{i}Birthday:{/i}   [Character.Birthday[0]] [Character.Birthday[1]]{/color}{/size}{/font}" xpos 420 + menuOffsetX ypos 490
    text "{font=assets/PermanentMarker.ttf}{size=18}{color=#ffffff}{i}Gender:{/i}   [Character.Gender]{/color}{/size}{/font}" xpos 220 + menuOffsetX ypos 510
    $personality = Character.GetKnownPersonality()
    text "{font=assets/PermanentMarker.ttf}{size=18}{color=#ffffff}{i}Personality:{/i}   [personality]{/color}{/size}{/font}" xpos 220 + menuOffsetX ypos 530
    text "{font=assets/PermanentMarker.ttf}{size=18}{color=#ffffff}{i}Traits:{/i}   [Character.Traits[0]], [Character.Traits[1]]{/color}{/size}{/font}" xpos 220 + menuOffsetX ypos 550
    #text "{font=assets/PermanentMarker.ttf}{size=18}{color=#ffffff}{i}Likes:{/i}\n     [Character.Likes[0]], [Character.Likes[1]], [Character.Likes[2]] {/color}{/size}{/font}" xpos 320 ypos 370
    text "{font=assets/PermanentMarker.ttf}{size=18}{color=#ffffff}{i}Likes:{/i} {/color}{/size}{/font}" xpos 220 + menuOffsetX ypos 580
    hbox xpos 300 + menuOffsetX ypos 580:
      add GetLikesImage(Character.Likes[0])
      add GetLikesImage(Character.Likes[1]) ypos -10
      add GetLikesImage(Character.Likes[2])
    #text "{font=assets/PermanentMarker.ttf}{size=18}{color=#ffffff}{i}Dislikes:{/i}\n     [Character.Dislikes[0]], [Character.Dislikes[1]], [Character.Dislikes[2]]{/color}{/size}{/font}" xpos 320 ypos 420
    text "{font=assets/PermanentMarker.ttf}{size=18}{color=#ffffff}{i}Dislikes:{/i}\n {/color}{/size}{/font}" xpos 220 + menuOffsetX ypos 640
    hbox xpos 300 + menuOffsetX ypos 640:
      add GetLikesImage(Character.Dislikes[0])
      add GetLikesImage(Character.Dislikes[1]) ypos -10
      add GetLikesImage(Character.Dislikes[2])
    
      
    #$menuOffsetX = 800
    if (isAChild == True ):#and currentScreen == "Stats") :
      use boardBar("English", bar_English, GetScoreGrade(bar_English), 720 + menuOffsetX, 475) 
      use boardBar("Science", bar_Science, GetScoreGrade(bar_Science), 720 + menuOffsetX, 500) 
      use boardBar("Maths", bar_Maths, GetScoreGrade(bar_Maths), 720 + menuOffsetX, 525) 
      use boardBar("Art", bar_Art, GetScoreGrade(bar_Art), 720 + menuOffsetX, 550) 
      use boardBar("Music", bar_Music, GetScoreGrade(bar_Music), 720 + menuOffsetX, 575) 
      use boardBar("Pys Ed.", bar_PE, GetScoreGrade(bar_PE), 720 + menuOffsetX, 600) 
    
    
##############################################################################
# Journal Menu
#
# A screen that basically acts as a wrap around and link to other screens

screen journal_nav_menu:
    add "img/ui/Blackboard_line_vert1.png" xpos -50
    text "{font=assets/PermanentMarker.ttf}{size=46}{color=#ffffff}Navigation{/color}{/size}{/font}" xpos 70 ypos 70
    use boardButton( "Journal", [Hide("calender_day"), ShowMenu("journal_menu")], 50, 200, 10)
    use boardButton( "Status", [Hide("calender_day"), ShowMenu("status_menu")], 50, 300, 10)
    use boardButton( "Calender", [Hide("calender_day"), ShowMenu("calender_menu")], 50, 400, 10)
    use boardButton( "Characters", [Hide("calender_day"), ShowMenu("character_menu")], 50, 500, 10)
    use boardButton( "Traits", [Hide("calender_day"), ShowMenu("trait_menu")], 50, 600, 10)
    use boardButton( "Teaching Plan", [Hide("calender_day"), ShowMenu("screen_TeachingPlan")], 50, 700, 10)
    
    
    
screen journal_menu:

    tag menu
    add "img/ui/Blackboard_big.png" 
    
    use journal_nav_menu
    use navigation
    
    $List_Event_shortdesc = ["Woke up early!", "Taught some Art class", "Forgot my lunch.", "Taught Music", "Saw a cat! I tried to pet it."]
    
    text "{font=assets/PermanentMarker.ttf}{size=48}{color=#ffffff}Today I...{/color}{/size}{/font}" xpos 550 ypos 150
    
    vbox:
      xpos 570
      ypos 250
      $currTime = CurrentTimeToInt(current_time)
      $i = 0
      for eventdesc in List_Event_shortdesc:
        if (i <= currTime):
          text "{font=assets/PermanentMarker.ttf}{size=38}{color=#ffffff}- [eventdesc]{/color}{/size}{/font}" 
        
        $i+=1
      
    
##############################################################################
# Trait Menu
#
# A screen that shows all traits with extra information for unlocked ones

screen trait_nav_menu:
    #use boardButton( "Journal", [Hide("traits_gallery"),ShowMenu("journal_menu")], 50, 50, 10)
    use journal_nav_menu
    use boardButton( "Personality", [Hide("journal_menu"), ShowMenu("traits_gallery","personalities")], 550, 100, 10)
    use boardButton( "Traits", [Hide("journal_menu"), ShowMenu("traits_gallery","traits")], 850, 100, 10)
    use boardButton( "Preferences", [Hide("journal_menu"), ShowMenu("traits_gallery","preferences")], 1150, 100, 10)

screen trait_menu:
    tag menu
    add "img/ui/Blackboard_big.png" 
    use trait_nav_menu
    use navigation

screen traits_gallery_personality:
    use traits_gallery("personalities")
    
screen traits_gallery_traits:
    use traits_gallery("traits")
    
screen traits_gallery_prefs:
    use traits_gallery("preferences")
    
    
screen traits_gallery(type=""):

    tag menu
    add "img/ui/Blackboard_big.png"  
    
    use trait_nav_menu
    use navigation
    
    $list = List_Personalities
    
    if type == "traits":
      $list = List_Traits
      
    if type == "preferences":
      $list = List_Preferences
    
    $spacingX = 250
    $spacingY = 60
    $i = 0
    $j = 0
    for trait in list:
      if type == "preferences":
        if trait in DiscoveredLikes: 
          pass
        else:
          $trait = "???"
        
      if type == "personalities":
        if trait in DiscoveredPersonalities:
          pass
        else:
          $trait = "???"
          
      if type == "traits":
        if trait in DiscoveredTraits: 
          pass
        else:
          $trait = "???"
          
      if j <= 7:
        use boardButton( trait, [Hide("traits_gallery"), ShowMenu("trait_detail", trait)], 380 + i*spacingX, 200 + j*spacingY, 10)
      $i += 1
      if i > 5:
        $j += 1
        $i = 0

screen trait_detail(trait == "???"):
  
    tag menu
    add "img/ui/Blackboard_big.png" 
    
    use trait_nav_menu
    use navigation
    
    text "{font=assets/PermanentMarker.ttf}{size=38}{color=#ffffff}[trait]{/color}{/size}{/font}" xpos 400 ypos 250
    
    if trait == "???":
      text "{font=assets/PermanentMarker.ttf}{size=28}{color=#ffffff}You don't know what this means...{/color}{/size}{/font}" xpos 420 ypos 350
    else:
      text "{font=assets/PermanentMarker.ttf}{size=28}{color=#ffffff}This means someone either likes or dislikes [trait].{/color}{/size}{/font}" xpos 420 ypos 350
    

##############################################################################
# Status Menu
#
# A screen that the current status of the Player
screen status_menu:

    tag menu
    add "img/ui/Blackboard_big.png" 
    
    use navigation
    use character_menu(True)
    use journal_nav_menu
    
    
         
##############################################################################
# DEBUG Character Menu
#
#  
screen character_menu_debug():

    tag menu
    add "img/ui/Blackboard_big.png" 
        
    
    $Character = CharacterClass()
    $Character.RandomizeStats()
    $Character.RandomizeAppearance()
    #$Character.RandomizeStats()
    
    add Character.Appearance() yalign 1.0
    
    vbox:
      xpos 720 #+ menuOffsetX 
      ypos 270
      text "{i}Name:{/i}   [Character.Name]" 
      text "{i}Age:{/i}   [Character.Age]" 
      text "{i}Gender:{/i}   [Character.Gender]" 
      text "{i}Birthday:{/i}   [Character.Birthday[0]], [Character.Birthday[1]]" 
      text " " 
     
      text "{i}Mood:{/i}   [Character.Mood]"
      text " "  
      
      text "{i}Personality:{/i}   [Character.Personality]" 
      text "{i}Traits:{/i}   [Character.Traits[0]], [Character.Traits[1]]" 
      text " " 
      
      text "{i}Likes:{/i}   [Character.Likes[0]], [Character.Likes[1]], [Character.Likes[2]]" 
      text "{i}Dislikes:{/i}   [Character.Dislikes[0]], [Character.Dislikes[1]], [Character.Dislikes[2]]" 
      text " " 
    
    
    #PersonalityKnown = 0
    #TraitsKnown = [0,0]
    #LikesKnown = [0,0,0]
    #DislikesKnown = [0,0,0]
    
    #IsAStudent = True
    #Relationship = 1
    #Happiness = 50
    
    #English = 0
    #Science = 0
    #Maths = 0
    #Art = 0
    #Music = 0
    #PE = 0
    
      text "{i}Uniform:{/i}   [Character.Uniform]" 
      text "{i}Hair:{/i}   [Character.Hair]" 
      text "{i}HairColour:{/i}   [Character.HairColour]" 
      text "{i}EyeColour:{/i}   [Character.EyeColour]" 
    #appearance
    #IsUnique = 0
    #UniqueAppearance = ""
    
    
    
    use navigation
    

    use boardButton( "Refresh", [Hide("calender_day"), ShowMenu("character_menu_debug")], 1360, 720, -10)
    
#-------------------------------------------------------  

init python:
    TimeOfDay_Week = ['Morning', 'First Period', 'Lunch', 'Second Period', 'After School', 'Evening']
    TimeOfDay_Weekend = ['Morning', 'Noon', 'Evening']
    TODXOffset = 0
    TODYOffset = 0
    TOD_StepSize = 95
    
init -2:
    transform TOD_eff(_oldY, _moveToY):
      ypos _oldY
      time 0.5
      linear 0.8 ypos _moveToY
      
    transform TOD_sun_eff(_oldX, _moveToX):
      xpos _oldX
      time 0.5
      linear 0.8 xpos _moveToX
      
      
screen screen_TOD():
  $currentTimeOfDay = CurrentTimeToInt(current_time)
  add "img/ui/TOD/TOD_bg.png" xpos TODXOffset
  add "img/ui/TOD/TOD_sidebar.png" xpos TODXOffset
  $oldYPos = TODYOffset+TOD_StepSize*(currentTimeOfDay-1)
  $newYPos = TODYOffset+TOD_StepSize*currentTimeOfDay
  if (currentTimeOfDay-1 < 0):
    $oldYPos = TODYOffset+TOD_StepSize*(4)
    
  add "img/ui/TOD/TOD_indicator.png" xpos 0+TODXOffset ypos at TOD_eff(oldYPos, newYPos)
  if IsSchoolDay(current_year, current_month+1, current_date):
    add "img/ui/TOD/TOD_sidebar_Text.png" xpos TODXOffset
  else:
    add "img/ui/TOD/TOD_sidebar_Text_noschool.png" xpos TODXOffset
  
  use screen_TOD_indicator
  add "img/ui/TOD/TOD_sidebar_border.png"
  
screen screen_TOD_indicator():
    
  $currentTimeOfDay = CurrentTimeToInt(current_time)
  if IsSchoolDay(current_year, current_month+1, current_date):
    $timeImage = TimeOfDay_Week[currentTimeOfDay]
    $sunPosition_old = (int)((currentTimeOfDay - 1 - 2.5)*100)
    $sunPosition = (int)((currentTimeOfDay - 2.5)*100)
  else:
    $timeImage = TimeOfDay_Weekend[currentTimeOfDay]
    $sunPosition_old = (int)((currentTimeOfDay - 1)*250)
    $sunPosition = (int)((currentTimeOfDay)*250)
  
  
  add "img/ui/TOD/TOD_Indicator_Sun.png" xpos  at TOD_sun_eff(sunPosition_old, sunPosition)
  
screen screen_TOD_indicator_sml():
  $currentTimeOfDay = CurrentTimeToInt(current_time)
  $timeImage = TimeOfDay_Week[currentTimeOfDay]
  #add "img/ui/TOD/Banner.png" xpos TODXOffset
  #add "img/ui/TOD/%s Indicator.png"%timeImage xpos TODXOffset
  
#-------------------------------------------------------  
  
init python:

  TeachingPlan_ThisWeek = ['Science', 'Maths', 'English', '=', 'English', 'Maths', 'Music', 'Art', '=', 'Pys Ed.']
  TeachingPlan_LastWeek = TeachingPlan_ThisWeek
  
screen screen_TeachingChoice():
  use screen_TeachingPlan
  
screen screen_TeachingPlan(_canSet=True, _update=False, _index=-1, _value=""):

    $debug_print("screen_TeachingPlan - " + str(_canSet) + ", " + str(_update) + ", " + str(_index)  + ", " + str(_value)  )
    # This ensures that any other menu screen is replaced.
    tag menu
    add "img/ui/Blackboard_big.png" 
    text "{font=assets/PermanentMarker.ttf}{size=58}{color=#ffffff}Teaching Plan - Week 01{/color}{/size}{/font}" xpos 700 ypos 150
    
    add "img/ui/plan/plan_week_bg.png" 
    text "{font=assets/PermanentMarker.ttf}[TeachingPlan_ThisWeek]{/font}"  xpos 500 ypos 130
    
    #if called as an update then set the current value to the plan for the supplied index
    if (_update==True):
      text "{font=assets/PermanentMarker.ttf}############# Updating!!! #################{/font}"  xpos 500 ypos 50
      $TeachingPlan_ThisWeek[_index] = _value
    
    $index=-1
    for subject in TeachingPlan_ThisWeek:  
      $index +=1
      $jpos = 240 * (index%5)
      $ipos = 280 * (index/5)
      if not subject == '=':
        text "{font=assets/PermanentMarker.ttf}[subject]{/font}"  xpos 500+jpos ypos 330+ipos
      #  imagebutton auto "img/ui/plan/plan_selection_%s.png" xpos 470+jpos ypos 278+ipos focus_mask None action NullAction()
      #else:
      if (_canSet==True):
        imagebutton auto "img/ui/plan/plan_selection_%s.png" xpos 470+jpos ypos 278+ipos focus_mask None action If(not (subject == '='), ShowMenu("TeachingPlan_choice_menu", index))
      else:
        if (subject == '='):
          add "img/ui/plan/plan_selection_insensitive.png" xpos 470+jpos ypos 278+ipos 
    
    
    #imagebutton auto "img/gui/relatn_btn/anabtn_%s.png" xpos int(bar_xstart_pos + bar_xspacing * (0 % row_count)) ypos int(bar_ystart_pos + bar_yspacing * int(0/row_count)) focus_mask True action   [SetVariable('char_name', "ana"), ShowMenu("character_menu", val_friend, val_rival, val_roman, val_respec)]
  
    use navigation
    use journal_nav_menu
    
  
#-------------------------------------------------------  
  
screen TeachingPlan_choice_menu(_index):

    modal True
    add "img/ui/plan/plan_week_choice_bg.png"
    #imagebutton auto "img/gui/relatn_char/charselectbtn_%s.png" xpos 340 ypos 460 focus_mask None action [Hide("character_menu"), ShowMenu("relationship_menu")]
    $CurrentChoice = TeachingPlan_ThisWeek[_index]
    text "current choice = [CurrentChoice]"      yalign 0.5      xalign 0.5
    
    #vbox:
    #  xpos 500
    #  ypos 300
    #  hbox:
    use boardButton( "English", [Hide("TeachingPlan_choice_menu"), ShowMenu("screen_TeachingPlan", True, True, _index, "English")], 500, 350, 10)
    use boardButton( "Maths", [Hide("TeachingPlan_choice_menu"), ShowMenu("screen_TeachingPlan", False, True, _index, "Maths")], 700, 350, 10)
    use boardButton( "Science", [Hide("TeachingPlan_choice_menu"), ShowMenu("screen_TeachingPlan", True, True, _index, "Science")], 900, 350, 10)
    #  hbox:
    use boardButton( "Art", [Hide("TeachingPlan_choice_menu"), ShowMenu("screen_TeachingPlan", True, True, _index, "Art")], 500, 450, 10)
    use boardButton( "Music", [Hide("TeachingPlan_choice_menu"), ShowMenu("screen_TeachingPlan", True, True, _index, "Music")], 700, 450, 10)
    use boardButton( "Phys Ed.", [Hide("TeachingPlan_choice_menu"), ShowMenu("screen_TeachingPlan", True, True, _index, "Phys Ed.")], 900, 450, 10)