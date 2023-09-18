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
            null  height 25   
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
    if show_quick_menu:
      use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        $i = 0
        for caption, action, chosen in items:
            $i+= 1
            if action:
                $yalignpos = 0.4 + (0.08*i)
                imagebutton auto "images/ui/menu_choice_%s.png" xpos 625 yalign yalignpos action action
                text caption xpos 685 yalign yalignpos


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
    tag menu
    add "images/ui/menu_base_bg.png"
    
    imagemap:
        auto "images/ui/menu_main_%s.png"        
        hotspot (436, 566, 455, 70) action Start()
        hotspot (436, 636, 455, 70) action ShowMenu("load")
        hotspot (436, 706, 455, 70) action Quit(confirm=False)

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
        auto "images/ui/menu_nav_%s.png" alpha False          
        hotspot (250, 650, 190, 50) action MainMenu()
        hotspot (470, 650, 200, 50) action ShowMenu("load")
        hotspot (700, 650, 120, 50) action ShowMenu("preferences")
        hotspot (850, 650, 90, 50) action ShowMenu("gallery")
        hotspot (975, 650, 120, 50) action Return()


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
        auto "images/ui/menu_pagenav_%s.png" alpha False         
        hotspot (800, 115, 60, 65)  action FilePagePrevious()
        for i in range(1, 5):
          hotspot (800+(63*i), 115, 60, 65)  action FilePage(i)
          text "{size=40}{b}[i]{/b}{/size}"  xpos 815+(63*i) ypos 125
        hotspot (1115, 115, 60, 65)  action FilePageNext()
        
    $ columns = 3
    $ rows = 1
    for i in range(1, columns * rows + 1):
      $index = i
      $jpos = 325*int((i-1)/rows)
      #if (i > rows):
      $index = ((i-1)%rows) + 1
      $ipos = 320*(index-1)
      imagebutton auto "images/ui/menu_savebox_%s.png" xpos 155+jpos ypos (215+ipos) focus_mask None action FileAction(i)
      add FileScreenshot(i) xpos 165+jpos ypos (314+ipos)
      $ file_name = FileSlotName(i, columns * rows)
      $ file_time = FileTime(i, empty=_("Empty Slot."))
      $ save_name = FileSaveName(i) 
      text "{size=22}{color=#000}[file_name]. {b}[file_time!t]{/b}\n[save_name!t]{/color}{/size}"  xpos 217+jpos ypos (245+ipos)

screen save():

    # This ensures that any other menu screen is replaced.
    tag menu
    add "images/ui/menu_base.png"
    add "images/ui/menu_title_save.png"

    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu
    add "images/ui/menu_base.png"
    add "images/ui/menu_title_load.png"

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text

init -2 python:
    
    config.thumbnail_width = 300
    config.thumbnail_height = 188

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu
    add "images/ui/menu_base.png"
    add "images/ui/menu_base.png"
    
    imagemap:
        auto "images/ui/menu_config_%s.png" alpha False    
        
        hotspot (165, 205, 245, 90)  action Preference("display", "window")
        hotspot (415, 205, 245, 90)  action Preference("display", "fullscreen")
        hotspot (165, 305, 245, 90)  action Preference("transitions", "all")
        hotspot (415, 305, 245, 90)  action Preference("transitions", "none")
        hotspot (165, 410, 245, 90)  action Preference("skip", "seen")
        hotspot (415, 410, 245, 90)  action Preference("skip", "all")
        hotspot (165, 520, 245, 90)  action Preference("after choices", "stop")
        hotspot (415, 520, 245, 90)  action Preference("after choices", "skip") 
        
    bar:
      style_group "pref"
      xpos 710
      ypos 235
      value Preference("text speed")
    bar:
      style_group "pref"
      xpos 710
      ypos 335
      value Preference("auto-forward time")
      
    bar:
      style_group "pref"
      xpos 710
      ypos 455
      value  Preference("music volume")
    bar:
      style_group "pref"
      xpos 710
      ypos 560
      value Preference("sound volume")
      
    # Include the navigation.
    use navigation
    
    
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

    style soundtest_button:
        xalign 1.0

init -2 python: 
    # Styling for the bar sliders:
    #style.pref_frame.background = None
    style.pref_slider.left_bar = "images/ui/bar_full.png"
    style.pref_slider.right_bar = "images/ui/bar_empty.png"
    style.pref_slider.thumb = "images/ui/bar_marker.png"
    style.pref_slider.xmaximum = 459
    style.pref_slider.ymaximum = 41   

##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True
    
    if message == layout.ARE_YOU_SURE:
        add "images/ui/menu_yesno_confirm.png"
    if message == layout.DELETE_SAVE:
        add "images/ui/menu_yesno_delete.png"
    if message == layout.OVERWRITE_SAVE:
        add "images/ui/menu_yesno_overwrite.png"
    if message == layout.LOADING:
        add "images/ui/menu_yesno_load.png"
    if message == layout.QUIT:
        add "images/ui/menu_yesno_quit.png"
    if message == layout.MAIN_MENU:
        add "images/ui/menu_yesno_confirm.png"
        
    imagemap:
        auto "images/ui/menu_yesno_%s.png"        
        hotspot (460, 390, 195, 80) action yes_action
        hotspot (675, 390, 195, 80) action no_action
    
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

    imagemap:
        ypos 540
        auto "images/ui/menu_quick_%s.png" alpha False          
        hotspot (815, 35, 65, 38) action Preference("auto-forward", "toggle")
        hotspot (880, 35, 65, 38) action Skip()
        hotspot (945, 35, 65, 38) action ShowMenu('preferences')
        hotspot (1010, 35, 65, 38) action ShowMenu('save')
        hotspot (1075, 35, 65, 38) action ShowMenu('load')
        hotspot (1140, 35, 65, 38) action Quit()

    use TimeOfDayDisplay

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

screen gallery():
    tag menu
    add "images/ui/menu_base.png"
    add "images/ui/menu_title_gallery.png"
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
      $ipos = 325*int((index-1)/columns)
      $index = ((j-1)%columns) + 1
      $jpos = 320*(index-1)
        
      if j <= (cg_page+1)*gal_cells and j>cg_page*gal_cells: 
        add g_cg.make_button(gal_item + " butt", gal_item + " butt", "images/ui/menu_gallerybox_insensitive.png",  xpos=154+jpos, ypos=(287+ipos),  background=None)
            #add g_cg.make_button(gal_item + " butt", gal_item + " butt", "images/ui/savebox_insensitive.png", xpos=275+jpos-1, ypos=(270+ipos)+10, background=None)
            #add im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y) xpos 275+jpos+10 ypos (270+ipos)+10
        imagebutton auto "images/ui/menu_gallerybox_%s.png" focus_mask None  xpos 158+jpos ypos (264+ipos) action g_cg.Action(gal_item + " butt")
    
    imagemap:
        auto "images/ui/menu_pagenav_%s.png" alpha False        
        if cg_page > 0:    
          hotspot (800, 115, 60, 65)  action [SetVariable('cg_page', prev_cg_page), ShowMenu("gallery")]
        for i in range(1, 5):
          if (i-1 < int(len(gallery_cg_items)/gal_cells)+1):
            hotspot (800+(63*i), 115, 60, 65)  action [SetVariable('cg_page', i-1), ShowMenu("gallery")]  
          text "{size=40}{b}[i]{/b}{/size}"  xpos 815+(63*i) ypos 125
        if cg_page < int(len(gallery_cg_items)/gal_cells):
          hotspot (1115, 115, 60, 65)  action [SetVariable('cg_page', next_cg_page), ShowMenu("gallery")]
        
          

screen gallery_nav():
    imagemap:
        auto "images/ui/menu_gallery_nav_%s.png" alpha False          
        hotspot (740, 30, 125, 40) action ShowMenu('gallery')
        hotspot (890, 30, 140, 40) action ShowMenu("credits")
        hotspot (1035, 30, 70, 40) action Help()
        
        
screen credits():
    tag menu
    add "images/ui/menu_base.png"
    add "images/ui/menu_title_credits.png"
    add "images/ui/menu_extra_credits.png"
    use navigation
    use gallery_nav
    
init python:
    #Galleries settings - start
    #list the CG gallery images here:
    #how many rows and columns in the gallery screens?
    gal_rows = 3
    gal_cols = 1
    #thumbnail size in pixels:
    thumbnail_x = 304
    thumbnail_y = 191
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

  CurrentTimeOfDayName = 'morning'
  CurrentDayName = 'monday'
  
screen TimeOfDayDisplay():
  add "images/ui/TOD_bg.png"
  add "images/ui/TOD_%s.png"%CurrentTimeOfDayName
  add "images/ui/TOD_%s.png"%CurrentDayName
