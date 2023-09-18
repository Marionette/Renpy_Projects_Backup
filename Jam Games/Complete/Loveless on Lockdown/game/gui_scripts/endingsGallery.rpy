
## Endings Gallery screen ############################################################
##
## This is a simple screen that shows buttons that endings from the game that have been seen.
screen endings_gallery:

    tag menu
    key "game_menu" action Return()
    
    add gui.mm_background
    
    fixed:
        at gui_fade_inout
        add "gui_overlay"
        
        add "gui/log_decor_top.png" at gui_overlaydecor_top
            
        use exit_button
        
        frame:
            background None
            xsize 1200
            at gui_overlaydecor_bottom
            
            add "gui/about_decor_bottom.png":
                alpha 0.3
            text "ENDINGS":
                style "gui_overlay_title"
                
        viewport id "vp":
            mousewheel True
            draggable False
            xsize 1200 xalign 0.5
            ysize 860 yalign 0.49
            yinitial 0.0
            
            
            vbox:
                xsize 1050
                yfill True
                spacing 0
                at gui_fade(1.3)
                style_prefix "endings"
                
                text " "
                text " "

                #text config.name.upper() style "history_name_text" text_align 0.5 xalign 0.5
                #text "version [config.version!t]\n(c) 2021 [gui.developer_name!t]\n\n[gui.about!t]\n\nMade with Ren'Py [renpy.version_only]":
                #    style "history_text"
                #    text_align 0.5
                #    xalign 0.5
                
                if persistent.ending_seen_1:
                    text "1. Languishing in gender jail" text_align 0.5 xalign 0.5
                else:
                    text "1. ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_2:
                    text "2. Trading answers, sharing time" text_align 0.5 xalign 0.5
                else:
                    text "2. ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_3:
                    text "3. Grabbing a date at the grocery fruit stall" text_align 0.5 xalign 0.5
                else:
                    text "3. ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_4:
                    text "4. Delivering ice cream and safe hugs" text_align 0.5 xalign 0.5
                else:
                    text "4. ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_5:
                    text "5. Accepting the video-conference invitation" text_align 0.5 xalign 0.5
                else:
                    text "5. ???" text_align 0.5 xalign 0.5

                null height 20
                    
                text " "
                text " "
              
            vbox:

                xalign 0.5
                yalign 0.5
        
style endings_text is history_text

style endings_text:
  size 44
  bold True
  
style gui_overlay_title:
  size 22