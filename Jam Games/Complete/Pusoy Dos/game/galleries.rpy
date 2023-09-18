################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## Gallery  ####################################################################
################################################################################
init:
  
  image gallerylock_button = "gui/button/locked_screen.png"

  image cg_suits_button = im.Scale("images/cg/cg_suits.png", 383, 215)
  image cg_hands_button = im.Scale("images/cg/cg_hands.png", 383, 215)
  image cg_nightmare_button = im.Scale("images/cg/cg_nightmare.png", 383, 215)
  
  image bg_bar_button = im.Scale("images/bg/bg_bar.png", 383, 215)
  image bg_slots_button = im.Scale("images/bg/bg_slots.png", 383, 215)
  image bg_roulette_button = im.Scale("images/bg/bg_roulette.png", 383, 215)

init python:
    g_cg = Gallery()

    g_cg.button("cg cg_suits")
    g_cg.unlock_image("cg cg_suits")
    
    g_cg.button("cg cg_hands")
    g_cg.unlock_image("cg cg_hands")
    g_cg.unlock_image("cg cg_hands_bloody")
    g_cg.unlock_image("cg cg_hands_creepy")
    
    g_cg.button("cg cg_nightmare")
    g_cg.unlock_image("cg cg_nightmare")
    
    g_cg.locked_button = "gallerylock_button"
    
    #----------------------------------------
    
    g_bg = Gallery()
    
    g_bg.button("bg bg_bar")
    g_bg.image("bg bg_bar")
    g_bg.unlock("bg bg_bar")
    
    g_bg.button("bg bg_slots")
    g_bg.unlock_image("bg bg_slots")
    
    g_bg.button("bg bg_roulette")
    g_bg.unlock_image("bg bg_roulette")
    g_bg.unlock_image("bg bg_roulette_missing")
    g_bg.unlock_image("bg bg_roulette_creepy")
    
    g_bg.locked_button = "gallerylock_button"

## CG Gallery screen ##################################################################
screen cg_gallery():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Event Gallery"), extra_navigation=True):

        grid 3 1:
            xpos 60
            ypos 160
            xspacing 30
            yspacing 30

            # Call make_button to show a particular button.
            button:
              add g_cg.make_button("cg cg_suits", "cg_suits_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              add g_cg.make_button("cg cg_hands", "cg_hands_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              add g_cg.make_button("cg cg_nightmare", "cg_nightmare_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
              
screen bg_gallery():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Background Gallery"), extra_navigation=True):

        grid 3 1:
            xpos 60
            ypos 160
            xspacing 30
            yspacing 30

            # Call make_button to show a particular button.
            button:
              add g_bg.make_button("bg bg_bar", "bg_bar_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              add g_bg.make_button("bg bg_slots", "bg_slots_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              add g_bg.make_button("bg bg_roulette", "bg_roulette_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
              

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
                ["audio/music/music_menu.mp3",'Ante','Beans'],
                ["audio/music/music_bar.mp3",'River','Beans'],
                ["audio/music/music_roulette.mp3",'Split','Beans'],
                ["audio/music/music_slots.mp3",'Jackpot','Beans'],
                ["audio/music/music_flashback.mp3",'Isolation','Beans'],  
                ["audio/music/music_reveal.mp3",'Showdown','Beans'],                
                ["audio/music/music_nightmare.mp3",'Kill Game','Beans'],              
                ["audio/music/music_ending.mp3",'Royal Flush','Beans'],
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
    use game_menu(_("Music Box"), extra_navigation=True):

        hbox:
          xfill True
          vbox:
            style_prefix "playlist"
            spacing -10
                  
            $count = 0
            label "Tracks:" xoffset -20
            for track in song_list:
              textbutton "[track[1]]"  xoffset 0 action  mr.Play(track[0])
              $count +=1
          #add "gui/overlay/options_extra_verticalbar.png"
          vbox:
            xalign 1.0
            yalign 0.7
            xoffset 10
            xfill True
            vbox:
              xalign 0.5 yalign 0.55
              yoffset -100
              spacing 15
              label song_name:
                  xalign 0.5
                  text_size 55
                  #text_outlines [ (5, "#fff1", 0, 0), (3, "#fff2", 0, 0),  (1, "#fff4", 0, 0) ]
              text song_description.upper():
                  xalign 0.5
          
            vbox:
              xalign 0.5 yalign 0.55
              spacing 10
              style_prefix "playback"
              frame:
                xalign 0.5
                background None
                area (0,0, 400, 160)
                hbox:
                  xalign 0.5
                  textbutton "Previous":
                      action [
                              mr.Previous()
                              ]
                  if not renpy.music.is_playing():
                    textbutton "Play":
                        action [
                                SetVariable('current_track', renpy.music.get_playing()), 
                                mr.Play(current_track)
                                ]
                  else:
                    textbutton "Pause":
                        action [
                                SetVariable('current_track', renpy.music.get_playing()),
                                mr.Stop()
                                ]
                  
                  textbutton "Next":
                      action [
                              mr.Next()
                              ]
    
    # Make music change upon entering / exiting room.
    on "replace" action Stop("music")
    on "replaced" action Play("music", config.main_menu_music, fadeout=1.0)
    
style playlist_button is gui_button
style playlist_button_text is gui_button_text
style playback_button is radio_button
style playback_button_text is radio_button_text

style playlist_button:
    right_padding 30
    top_padding 30
    #idle_background Frame("gui/button/button_idle.png", Borders(0, 0, 80, 0))
    #hover_background Frame("gui/button/button_hover.png", Borders(0, 0, 80, 0))
    #selected_background Frame("gui/button/button_hover.png", Borders(0, 0, 80, 0))
    #xsize 550
    #ysize 100
    
style playlist_button_text:
    #hover_outlines [ (5, "#fb81", 0, 0), (3, "#fb82", 0, 0),  (1, "#fb84", 0, 0) ]
    xalign 0.0

#style playback_button:
  #xsize 250
  
## Endings screen ############################################################

screen endings():

    default loopMatch = ""
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Endings"), extra_navigation=True):
    
            
            vbox:
                xsize 1050
                yfill True
                spacing 0
                style_prefix "endings"

                if persistent.ending_seen_01:
                    text "Ending 1: Nightmares of Hearts" text_align 0.5 xalign 0.5
                else:
                    text "Ending 1: ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_02:
                    text "Ending 2: Approximations of Man" text_align 0.5 xalign 0.5
                else:
                    text "Ending 2: ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_03:
                    text "Ending 3: Forces of Malevolence" text_align 0.5 xalign 0.5
                else:
                    text "Ending 3: ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_04:
                    text "Ending 4: Memories of Fallen" text_align 0.5 xalign 0.5
                else:
                    text "Ending 4: ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_05:
                    text "Ending 5: Frame of Mind" text_align 0.5 xalign 0.5
                else:
                    text "Ending 5: ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_06:
                    text "Ending 6: Cuffs of Silver" text_align 0.5 xalign 0.5
                else:
                    text "Ending 6: ???" text_align 0.5 xalign 0.5

        
style endings_text is history_text

style endings_text:
  size 44
  outlines [ (absolute(2), "#000000", absolute(0), absolute(0)) ]
  
style gui_overlay_title:
  size 22