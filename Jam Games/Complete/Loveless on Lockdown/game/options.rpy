init -1600 python hide:
    renpy.music.alias_channel(1, "system")
    
define config.main_menu = main_menu

################################################################################
## Initialization
################################################################################

init offset = -1

init python:
    # Creates a layer where ATL can run regardless of skipping.
    # Important for Skip Mode.
    config.top_layers = ['top_layer']
    
    # Custom layers.
    config.layers = [ 'master',
                      'transient',
                      'lens',
                      'screens',
                      'overlay' ]

## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True

## Register a system channel with a separate mixer.
init python:
    renpy.music.register_channel("system",mixer="systemMixer",loop=False)
    
## Game Settings ###############################################################

## Old - kept for backwards compatibility.

#define gui.about = _("")
## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
{b}{size=+10}Credits{/size}{/b}{p}
Writing: {a=https://ilyilaice.itch.io/}ilyilaice{/a}{p}
Coding and Programming: {a=https://marionette.itch.io/}Marionette{/a}{p}
Sprites and CGs: {a=https://onboroo.tumblr.com/}onboroo{/a}{p}
BGs: {a=https://www.dlsite.com/home/circle/profile/=/maker_id/RG08888.html}Minikle{/a}{p}
Music: {a=https://humanpyramids.itch.io/}HUMAN PYRAMIDS{/a}{p}
GUI Art Assets: {a=https://twitter.com/lunachaili/}Luna Chai (@lunachaili){/a}{p}

{b}{size=+10}Special Thanks{/size}{/b}{p}
{a=https://journals.sagepub.com/doi/10.1177/0146167297234003}{i}The Experimental Generation of Interpersonal Closeness: A Procedure and Some Preliminary Findings{/i}{/a} by Arthur Aron, Edward Melinat, Elaine N. Aron, Robert Darrin Vallone, Renee J. Bator.{p}
The writer would like to thank Merry and Caasi.
""")

## Old - kept for backwards compatibility.
image trans_overlay = Solid("#999")

# Language
init -2 python:
    gui.language = "unicode"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 40


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Fade Shortcuts ##############################################################

## Sets game menu to pause menu.
default _game_menu_screen = "pause_menu"

init:
    ## Auto Forward
    $ config.keymap['toggle_afm'].append('a')
    
    ## Screenshot
    $ config.keymap['screenshot'].remove('s')
    $ config.keymap['screenshot'].append('S')
    
    ## Fast skip
    $ config.keymap['toggle_fullscreen'].remove('f')
    $ config.keymap['fast_skip'].append('f')

################################################################################
# FADE GUI PREFERENCES
################################################################################

## Special image defs ##########################################################
    
image ctc_default:
    "gui/adv_ctc.png"
    xoffset 12 yoffset 20 
    alpha 0.0 anchor (0.5,0.5) size (15,15)
    parallel:
        linear 0.4 alpha 1.0
        pause 0.3
        linear 0.4 alpha 0.0
        repeat
        
## Special screens #############################################################

screen exit_button(clickaction=Return(),doTrans=True):
    button:
        xpos gui_exit_xpos ypos gui_exit_ypos
        text "ESC" style "gui_exit_tooltip"
        background "gui/exit_idle.png"
        hovered Play("system",guisfx_button_hover)
        action [Play("system",guisfx_button_click),
                clickaction]
        
        if doTrans:
            at gui_buttonfade_enter(gui_exit_parameters)
        else:
            at gui_buttonfade


################################################################################
# BUILD CONFIGS
################################################################################

## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "LovelessonLockdown-1511469406"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/**.rpy', None)
    build.classify('game/**.rpyb', None)
    build.classify('game/**.0', None)
    build.classify('game/**.rpym', None)
    build.classify('game/**.rpymc', None)
    build.classify('game/**.psd', None)

    ## To archive files, classify them as 'archive'.

    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.rpyc', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
