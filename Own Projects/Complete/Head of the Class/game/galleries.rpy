################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## Gallery  ####################################################################
################################################################################
init:
  
  image gallerylock_button = "gui/button/gallery_locked.png"

  image cg_bahini_feed_button = im.Scale("images/cg/bahini_feed.png", 383, 215)
  image cg_craig_rock_button = im.Scale("images/cg/craig_rock.png", 383, 215)
  image cg_hecate_chat_button = im.Scale("images/cg/hecate_chat.png", 383, 215)
  image cg_sanura_pat_button = im.Scale("images/cg/sanura_pat.png", 383, 215)
  image cg_end_bad_button = im.Scale("images/cg/end_bad.png", 383, 215)
  #image cg_end_good_button = im.Scale("images/cg/end_good.png", 383, 215)
  image cg_fullcast_photo_button = im.Scale("images/cg/fullcast_photo.png", 383, 215)
  
  image bg_classroom_button = im.Scale("images/bg/classroom_full.png", 383, 215)
  image bg_hallway_button = im.Scale("images/bg/hallway.png", 383, 215)
  image bg_hospital_button = im.Scale("images/bg/hospital.png", 383, 215)
  image bg_room_button = im.Scale("images/bg/room.png", 383, 215)
  image bg_library_button = im.Scale("images/bg/library.png", 383, 215)

init python:
    g_cg = Gallery()

    g_cg.button("cg bahini_feed")
    g_cg.unlock_image("cg bahini_feed")

    g_cg.button("cg craig_rock")
    g_cg.unlock_image("cg craig_rock")

    g_cg.button("cg hecate_chat")
    g_cg.unlock_image("cg hecate_chat")

    g_cg.button("cg sanura_pat")
    g_cg.unlock_image("cg sanura_pat")

    g_cg.button("cg end_bad")
    g_cg.unlock_image("cg end_bad")
    g_cg.unlock_image("cg end_good")

    g_cg.button("cg fullcast_photo")
    g_cg.unlock_image("cg fullcast_photo")
    g_cg.unlock_image("cg fullcast_photo_B")
    #g_cg.unlock_image("cg fullcast_photo_C")
    
    g_cg.locked_button = "gallerylock_button"
    
    #----------------------------------------
    
    g_bg = Gallery()
    
    g_bg.button("bg classroom")
    g_bg.unlock_image("bg classroom morning")
    g_bg.unlock_image("bg classroom afternoon")
    g_bg.unlock_image("bg classroom empty")
    
    g_bg.button("bg hallway")
    g_bg.unlock_image("bg hallway")
    
    g_bg.button("bg hospital")
    g_bg.unlock_image("bg hospital")
    
    g_bg.button("bg room")
    g_bg.unlock_image("bg room")
    g_bg.unlock_image("bg room night")
    
    g_bg.button("bg library")
    g_bg.unlock_image("bg library")
    
    g_bg.locked_button = "gallerylock_button"

## CG Gallery screen ##################################################################
screen cg_gallery():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Event Gallery"), _useAltNavigation="Extra"):

        grid 3 2:
            xpos 60
            ypos 60
            xspacing 30
            yspacing 20

            # Call make_button to show a particular button.
            button:
              add g_cg.make_button("cg bahini_feed", "cg_bahini_feed_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              add g_cg.make_button("cg craig_rock", "cg_craig_rock_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              add g_cg.make_button("cg hecate_chat", "cg_hecate_chat_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              add g_cg.make_button("cg sanura_pat", "cg_sanura_pat_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              add g_cg.make_button("cg end_bad", "cg_end_bad_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              add g_cg.make_button("cg fullcast_photo", "cg_fullcast_photo_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
              
screen bg_gallery():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Background Gallery"), _useAltNavigation="Extra"):

        grid 3 2:
            xpos 60
            ypos 60
            xspacing 30
            yspacing 20

            # Call make_button to show a particular button.
            button:
              add g_bg.make_button("bg classroom", "bg_classroom_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              add g_bg.make_button("bg hallway", "bg_hallway_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              add g_bg.make_button("bg hospital", "bg_hospital_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              add g_bg.make_button("bg room", "bg_room_button", xalign=0.5, yalign=0.55) xoffset 205 yoffset -5
            button:
              add g_bg.make_button("bg library", "bg_library_button", xalign=0.5, yalign=0.55) xoffset 205 yoffset -5
            null  
              

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
                ["audio/music/3_Corgi on beach by Ean Grimm.mp3",'Corgi on beach','Ean Grimm'],
                ["audio/music/4_Cat and Dog by Ean Grimm.mp3",'Cat and Dog','Ean Grimm'],
                ["audio/music/21_Alexander Nakarada - Drifting Minds (no drums).mp3",'Drifting Minds (no drums)','Alexander Nakarada'],
                ["audio/music/19_Alexander Nakarada - Spring.mp3",'Spring','Alexander Nakarada'],
                ["audio/music/8_I_m Alright by Ean Grimm.mp3","I'm Alright",'Ean Grimm'],                
                ["audio/music/24_Alexander Nakarada - Untold Stories.mp3",'Untold Stories','Alexander Nakarada'], 
                ["audio/music/13_Alexander Nakarada - Emotionalism (no drums).mp3",'Emotionalism (no drums)','Alexander Nakarada'],
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
    use game_menu(_("Music Box"), _useAltNavigation="Extra"):
    
        #if not renpy.music.is_playing():
        #  add "images/sprites/Yael/yael_smile.png" yalign 0.5 at yael_nofade_mr()
        #else:
        #  add "images/sprites/Yael/yael_groovy.png" yalign 0.5 at yael_fade_mr()

        hbox:
          xfill True 
          xoffset 20
          vbox:
            style_prefix "playlist"
            spacing -30
                  
            $count = 0
            label "Tracks:" xoffset -20
            for track in song_list:
              textbutton "[track[1]]"  xoffset 0 action  mr.Play(track[0])#[SetVariable('current_track', track[0]), mr.Play(track[0])]
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
                    textbutton "Play":
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
    use game_menu(_("Endings"), _useAltNavigation="Extra"):
  
  
            
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

        
style endings_text is history_text

style endings_text:
  size 44
  outlines [ (absolute(2), "#ffffff", absolute(0), absolute(0)) ]
  
style gui_overlay_title:
  size 22