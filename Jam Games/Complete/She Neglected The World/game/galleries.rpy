################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## Gallery  ####################################################################
################################################################################
init:
  
  # These cg buttons are 480x270
  image intro_button = im.FactorScale("images/cg/cg_intro.png", 0.25)
  image dream_button = im.FactorScale("images/cg/cg_butterfly_dream.png", 0.25)
  image fight_button = im.FactorScale("images/cg/cg_fight.png", 0.25)
  image death_button = im.FactorScale("images/cg/cg_death.png", 0.25)
  image finale_button = im.FactorScale("images/cg/cg_finale.png", 0.25)
  
  image gallerylock_button = "gui/button/button_gallery_locked.png"

init python:
    g_cg = Gallery()
    g_cg.button("CG_intro")
    g_cg.unlock_image("CG_intro")
    g_cg.unlock_image("CG_intro2")

    g_cg.button("CG_butterfly_dream")
    g_cg.unlock_image("CG_butterfly_dream")
    g_cg.unlock_image("CG_butterfly_dream2")
    
    g_cg.button("CG_fight")
    g_cg.unlock_image("CG_fight")
    g_cg.unlock_image("CG_fight2")

    g_cg.button("CG_death")
    g_cg.unlock_image("CG_death")

    g_cg.button("CG_finale")
    g_cg.unlock_image("CG_finale")
    
    g_cg.locked_button = "gallerylock_button"
    
    current_page = 1

## Gallery screen ##################################################################
screen gallery():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Gallery"), _extras=True):

        grid 2 2:
            xpos 60
            ypos 10
            xfill True
            #yfill True
            xspacing 30
            yspacing 10

            # Call make_button to show a particular button.
            if current_page == 1:
                button:
                  background "gui/button/button_gallery_background.png"
                  foreground "gui/button/button_gallery_foreground.png"
                  hover_foreground "gui/button/button_gallery_foreground_hover.png"
                  add g_cg.make_button("CG_intro", "intro_button", xalign=0.5, yalign=0.55) xoffset 11 yoffset 2
                button:
                  background "gui/button/button_gallery_background.png"
                  foreground "gui/button/button_gallery_foreground.png"
                  hover_foreground "gui/button/button_gallery_foreground_hover.png"
                  add g_cg.make_button("CG_butterfly_dream", "dream_button", xalign=0.5, yalign=0.55) xoffset 11 yoffset 2
                button:
                  background "gui/button/button_gallery_background.png"
                  foreground "gui/button/button_gallery_foreground.png"
                  hover_foreground "gui/button/button_gallery_foreground_hover.png"
                  add g_cg.make_button("CG_fight", "fight_button", xalign=0.5, yalign=0.55) xoffset 11 yoffset 2
                button:
                  background "gui/button/button_gallery_background.png"
                  foreground "gui/button/button_gallery_foreground.png"
                  hover_foreground "gui/button/button_gallery_foreground_hover.png"
                  add g_cg.make_button("CG_death", "death_button", xalign=0.5, yalign=0.55) xoffset 11 yoffset 2
            else:
                button:
                  background "gui/button/button_gallery_background.png"
                  foreground "gui/button/button_gallery_foreground.png"
                  hover_foreground "gui/button/button_gallery_foreground_hover.png"
                  add g_cg.make_button("CG_finale", "finale_button", xalign=0.5, yalign=0.55) xoffset 11 yoffset 2
                  
                null
                null
                null
            
        hbox:
            style_prefix "page"
            
            xfill True
            #xalign 0.5
            yalign 0.5
            xoffset -0

            spacing gui.page_spacing

            textbutton _("{size=+50}<{/size}") xalign 0.0 xoffset -40 action [SetVariable('current_page', 1), ShowMenu("gallery")]

            textbutton _("{size=+50}>{/size}") xalign 1.0 xoffset 50  action [SetVariable('current_page', 2), ShowMenu("gallery")]



################################################################################
## Music Box  ##################################################################
################################################################################

## Music Box setup #############################################################

init python:
    mr = MusicRoom()
    
    ######## ADD MUSIC FILES HERE ##############
    
    # Add music file references here.
    # The format goes:
    # ["path to music file.ogg",'Title', 'Composer']
    
    song_list = [ 
                  ["audio/music/Title Screen Theme.ogg",'Title Screen Theme', 'Damare'],
                  ["audio/music/Title Screen Theme 2.ogg",'Title Screen Theme - Alt', 'Damare'],
                  ['audio/music/Action (Full).ogg','Action', 'Damare'],
                  #['audio/music/Action (Loop).ogg','Action (Loop)', 'Damare'],
                  ["audio/music/Peaceful (Full).ogg",'Peaceful', 'Damare'],
                  #["audio/music/Peaceful (Loop).ogg",'Peaceful (Loop)', 'Damare'],
                  ["audio/music/Sad (Full).ogg",'Sad', 'Damare'],
                  #["audio/music/Sad (Loop).ogg",'Sad (Loop)', 'Damare'],
                  ["audio/music/Suspenseful (Full).ogg",'Suspenseful', 'Damare'],
                  #["audio/music/Suspenseful (Loop).ogg",'Suspenseful (Loop)', 'Damare'],
                ]
    
    # This lists default values for song_name and song_description to prevent errors.
    song_name = ""
    song_description = ""
    
    # This automatically adds an mr.add record for every song in the list.
    # Songs are always unlocked while always_unlocked = True.
    for track in song_list:
        mr.add(track[0], always_unlocked = True, action=[SetVariable('current_track', track[0]), SetVariable("song_name",track[1]),SetVariable("song_description",track[2])])
    
    #default to the first song    
    current_track = song_list[0][0] 
    
## Music Box screen ############################################################

screen musicbox():

    default loopMatch = ""
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Music Box"), _extras=True):

        hbox:
          xfill True
          yoffset 150
          vbox:
            style_prefix "playlist"
            spacing 20
                  
            $count = 0
            for track in song_list:
              if count < 3:
                textbutton "[track[1]]" action  mr.Play(track[0])#[SetVariable('current_track', track[0]), mr.Play(track[0])]
              $count +=1
              
          vbox:
            xalign 1.0
            style_prefix "playlist"
            spacing 20
                  
            $count = 0
            for track in song_list:
              if count > 2:
                textbutton "[track[1]]" action  mr.Play(track[0])
              $count +=1
          
        vbox:
            xalign 0.5
            yalign 0.5
            xoffset 10
            xfill True
            vbox:
              xalign 0.5 yalign 0.55
              yoffset -100
              spacing 15
              label song_name:
                  xalign 0.5
                  text_size 65
                  text_color "#562827"
                  text_outlines [ (absolute(2), "#ffffff", absolute(0), absolute(0)) ]
              text song_description.upper():
                  xalign 0.5
                  color "#562827"
          
            vbox:
              xalign 0.5 yalign 0.55
              frame:
                background None
                area (0,0, 400, 160)
                
                imagebutton:
                    focus_mask True
                    idle "gui/button/button_music_prev_idle.png"
                    hover "gui/button/button_music_prev_hover.png"
                    action [
                            mr.Previous()
                            ]
                
                imagebutton:
                    focus_mask True
                    idle "gui/button/button_music_next_idle.png"
                    hover "gui/button/button_music_next_hover.png"
                    action [
                            mr.Next()
                            ]
                if not renpy.music.is_playing():
                  imagebutton:
                      focus_mask True
                      idle "gui/button/button_music_play_idle.png"
                      hover "gui/button/button_music_play_hover.png"
                      action [
                              SetVariable('current_track', renpy.music.get_playing()), 
                              mr.Play(current_track)
                              ]
                else:
                  imagebutton:
                      focus_mask True
                      idle "gui/button/button_music_pause_idle.png"
                      hover "gui/button/button_music_pause_hover.png"
                      action [
                              SetVariable('current_track', renpy.music.get_playing()),
                              mr.Stop()
                              ]
    
    # Make music change upon entering / exiting room.
    on "replace" action Stop("music")
    on "replaced" action Play("music", config.main_menu_music, fadeout=1.0)
    
style playlist_button is gui_button
style playlist_button_text is gui_button_text

style playlist_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/select_idle.png"
    hover_foreground "gui/button/select_hover.png"
    selected_foreground "gui/button/select_hover.png"
    
style playlist_button_text:
    hover_color gui.hover_color
    selected_idle_color "#ffffff"
    outlines [ (absolute(2), "#9b0a0a", absolute(0), absolute(0)) ]
    hover_outlines [ (absolute(2), "#c63d3d", absolute(0), absolute(0)) ]
    selected_idle_outlines [ (absolute(2), "#d85f5f", absolute(0), absolute(0)) ]
    