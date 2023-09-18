################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## Gallery  ####################################################################
################################################################################
init:
  
  image gallerylock_button = "gui/button/gallery_locked.png"

  image cg_ending01_pic_button = "images/cg/ending01_pic_thumb.png"
  image cg_ending02_pic_button = "images/cg/ending02_pic_thumb.png"
  image cg_ending05_pic_button = "images/cg/ending05_pic_thumb.png"
  image cg_ending09_pic_button = "images/cg/ending09_pic_thumb.png"
  image cg_makeup_pic_button = "images/cg/makeup_pic_thumb.png"
  
  image bg_office_button = "images/bg/office_thumb.png"
  image bg_foyer_button = "images/bg/foyer_thumb.png"
  image bg_viewing_button = "images/bg/viewing_thumb.png"
  image bg_morgue_button = "images/bg/morgue_thumb.png"

init python:
    g_cg = Gallery()

    g_cg.button("cg ending01_pic")
    g_cg.image("cg ending01_pic")
    g_cg.unlock("cg ending01_pic")

    g_cg.button("cg ending02_pic")
    g_cg.image("cg ending02_pic")
    g_cg.unlock("cg ending02_pic")

    g_cg.button("cg ending05_pic")
    g_cg.image("cg ending05_pic")
    g_cg.unlock("cg ending05_pic")

    g_cg.button("cg ending09_pic")
    g_cg.image("cg ending09_pic")
    g_cg.unlock("cg ending09_pic")

    g_cg.button("cg makeup_pic")
    g_cg.image("cg makeup_pic")
    g_cg.unlock("cg makeup_pic")
    
    g_cg.locked_button = "gallerylock_button"
    
    #----------------------------------------
    
    g_bg = Gallery()
    
    g_bg.button("bg office")
    g_bg.image("bg office")
    g_bg.unlock("bg office")
    
    g_bg.button("bg foyer")
    g_bg.unlock_image("bg foyer")
    g_bg.unlock_image("bg foyer_open")
    
    g_bg.button("bg viewing")
    g_bg.unlock_image("bg viewing")
    g_bg.unlock_image("bg viewing_open")
    
    g_bg.button("bg morgue")
    g_bg.unlock_image("bg morgue")
    g_bg.unlock_image("bg morgue_open")
    g_bg.unlock_image("bg morgue_corpse")
    
    g_bg.locked_button = "gallerylock_button"

## CG Gallery screen ##################################################################
screen cg_gallery():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("CG Gallery"), extra_navigation=True):

        grid 3 2:
            xpos 60
            ypos 60
            xspacing 30
            yspacing 30

            # Call make_button to show a particular button.
            button:
              add g_cg.make_button("cg ending01_pic", "cg_ending01_pic_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              add g_cg.make_button("cg ending02_pic", "cg_ending02_pic_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              add g_cg.make_button("cg ending05_pic", "cg_ending05_pic_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              add g_cg.make_button("cg makeup_pic", "cg_makeup_pic_button", xalign=0.5, yalign=0.55) xoffset 205 yoffset -5
            button:
              add g_cg.make_button("cg ending09_pic", "cg_ending09_pic_button", xalign=0.5, yalign=0.55) xoffset 205 yoffset -5
            null  
              
screen bg_gallery():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Background Gallery"), extra_navigation=True):

        grid 2 2:
            xpos 60
            ypos 60
            xspacing 30
            yspacing 30

            # Call make_button to show a particular button.
            button:
              add g_bg.make_button("bg office", "bg_office_button", xalign=0.5, yalign=0.55) xoffset 205 yoffset -5
            button:
              add g_bg.make_button("bg foyer", "bg_foyer_button", xalign=0.5, yalign=0.55) xoffset 205 yoffset -5
            button:
              add g_bg.make_button("bg viewing", "bg_viewing_button", xalign=0.5, yalign=0.55) xoffset 205 yoffset -5
            button:
              add g_bg.make_button("bg morgue", "bg_morgue_button", xalign=0.5, yalign=0.55) xoffset 205 yoffset -5
              

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
                ["audio/music/menumusic.mp3",'Welcome to the Funeraria','Beans'],
                ["audio/music/bgm.mp3",'Funeral Home Lo-fi','Beans'],
                ["audio/music/suspense.mp3",'Immense Suspense','Beans'],
                ["audio/music/mellow.mp3",'Ambrosian Emotion','Beans'],
                ["audio/music/aria.mp3",'Mysterious Melody','Beans'],                
                ["audio/music/aria_guitar.mp3",'Mysterious Melody (Guitar)','Beans'],
                ["audio/music/aria_guitar_reverse.mp3",'Mysterious Melody (Reversed Guitar)','Beans'],
                ["audio/music/ending_best.mp3",'Best Ending Theme','Beans'],
                ["audio/music/ending_good.mp3",'Good Ending Theme','Beans'],
                ["audio/music/ending_bad.mp3",'Bad Ending Theme','Beans'],
                ["audio/music/ending_worst.mp3",'Worst Ending Theme','Beans'],
                ["audio/music/paghahandog.mp3",'Paghahandog (Hangad Cover)','downstairsparts'],
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
transform yael_fade_mr():
    xpos 300
    zoom 0.5
    alpha 0.5
    parallel:
      linear 5.0 alpha 0.5
      linear 5.0 alpha 0.5
      repeat
    parallel:
      linear 1.0 xpos 350
      linear 1.0 xpos 300
      repeat
transform yael_nofade_mr():
    xpos 300
    zoom 0.5
    alpha 0.5

screen musicbox():

    default loopMatch = ""
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Music Box"), extra_navigation=True):
    
        if not renpy.music.is_playing():
          add "images/sprites/Yael/yael_smile.png" yalign 0.5 at yael_nofade_mr()
        else:
          add "images/sprites/Yael/yael_groovy.png" yalign 0.5 at yael_fade_mr()

        hbox:
          xfill True
          vbox:
            style_prefix "playlist"
            spacing -10
                  
            $count = 0
            label "Tracks:" xoffset -20
            for track in song_list:
              textbutton "[track[1]]"  xoffset 0 action  mr.Play(track[0])#[SetVariable('current_track', track[0]), mr.Play(track[0])]
              $count +=1
          add "gui/overlay/options_extra_verticalbar.png"
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
                    text "1. Violin Reunion" text_align 0.5 xalign 0.5
                else:
                    text "1. ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_02:
                    text "2. Music Box Heart" text_align 0.5 xalign 0.5
                else:
                    text "2. ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_03:
                    text "3. Unfinished Business" text_align 0.5 xalign 0.5
                else:
                    text "3. ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_04:
                    text "4. Explosion of Keys" text_align 0.5 xalign 0.5
                else:
                    text "4. ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_05:
                    text "5. Hero and Heroine" text_align 0.5 xalign 0.5
                else:
                    text "5. ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_06:
                    text "6. No Pinky Promises" text_align 0.5 xalign 0.5
                else:
                    text "6. ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_07:
                    text "7. Gutted Guitar" text_align 0.5 xalign 0.5
                else:
                    text "7. ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_08:
                    text "8. Blood Blooms" text_align 0.5 xalign 0.5
                else:
                    text "8. ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_09:
                    text "9. Excursion to Destinations" text_align 0.5 xalign 0.5
                else:
                    text "9. ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_10:
                    text "10. Makeup Magic" text_align 0.5 xalign 0.5
                else:
                    text "10. ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_11:
                    text "11. Good Nights and Goodbyes" text_align 0.5 xalign 0.5
                else:
                    text "11. ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_12:
                    text "12. Rooted in Place" text_align 0.5 xalign 0.5
                else:
                    text "12. ???" text_align 0.5 xalign 0.5

        
style endings_text is history_text

style endings_text:
  size 44
  
style gui_overlay_title:
  size 22