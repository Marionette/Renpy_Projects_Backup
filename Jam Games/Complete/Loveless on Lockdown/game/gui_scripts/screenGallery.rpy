init offset = -1

################
# INSTRUCTIONS #
################

# Step 1:
# Set up your CG imagebuttons at Line 26.

# Step 2:
# Fill your CG pages starting at Line 148.
# You can copy and paste the template.

# Step 3:
# Set up your page navigation at Line 120.


##############
# BEGIN CODE #
##############

init python:
    g = Gallery()
    g.transition = fade
    
    ######## ADD BUTTONS AND IMAGES BELOW HERE ##############
    
    # A button that contains an image that automatically unlocks
    # when it's seen in game.
    g.button("cg ending3_pic")
    g.unlock_image("cg ending3_pic")
    
    g.button("cg ending5_pic")
    g.unlock_image("cg ending5_pic")
    
    g.button("cg laptop")
    g.unlock_image("cg laptop")  
    g.unlock_image("cg laptop_video")
    g.unlock_image("cg laptop_game")
    
    # You can also associate multiple images/variations
    # with one CG reference.
    # Check the Ren'Py documentation for more info:
    # https://www.renpy.org/doc/html/rooms.html
    
    
###########
# CG SLOT #
###########

# Setup code. Ignore this.

screen cg_slot(cgname, cgthumb):
    $ cgaction = g.Action(cgname)
    
    button:
        xsize 334 ysize 188
        at gui_cgbutton
        
        if cgaction:
            hovered Play("system",guisfx_button_hover)
            action [Play("system",guisfx_button_click),
                cgaction]
            add cgthumb 
        else:
            action None
            add "gui/cg_locked.png":
                alpha 0.3
    

##########
# SCREEN #
##########

screen cg_gallery(page=1,doTrans=True):
    
    key "game_menu" action ShowMenu('extras',fromMain=True,doTrans=False)
    
    add gui.mm_background
    
    fixed:
        at gui_fade_out
            
        add "gui_overlay"
        
        use exit_button(clickaction=ShowMenu('extras',fromMain=True,doTrans=False),doTrans=False)
        
        if doTrans:
            add "gui/log_decor_top.png" at gui_overlaydecor_top
        else:
            add "gui/log_decor_top.png" xalign 0.5 ypos 104 alpha 0.3
        
    frame:
        background None
        xsize 1200 
        if doTrans:
            at gui_overlaydecor_bottom
        else:
            xalign 0.5 ypos 967
        
        add "gui/cg_decor_bottom.png":
            alpha 0.3
        
        text "CG GALLERY":
            style "gui_overlay_title"
                
    # Page navigation.
    hbox:
        xalign 0.5
        ypos 0.19
        ysize 60

        spacing 18
        
        if doTrans:
            at gui_fade(1.0)
        
        #text "PAGE.":
        #    style "page_text"
        
        ############## CHANGE YOUR PAGES HERE ################
        
        #textbutton "COMMON":
        #    text_style "page_text"
        #    style "page_textbutton"
        #    
        #    if page is not 1:
        #        hovered Play("system",guisfx_button_hover)
        #    action [Play("system",guisfx_button_click),
        #            SelectedIf(page==1),
        #            ShowMenu("cg_page1",page=1,doTrans=False)]
        #    
        #    at gui_buttonfade
        #    
        #textbutton "BAE1":
        #    text_style "page_text"
        #    style "page_textbutton"
        #    
        #    if page is not 2:
        #        hovered Play("system",guisfx_button_hover)
        #    action [Play("system",guisfx_button_click),
        #            SelectedIf(page==2),
        #            ShowMenu("cg_page2",page=2,doTrans=False)]
        #    
        #    at gui_buttonfade
    
  
############
# CG PAGES #
############  
  
screen cg_page1(page=1,doTrans=True):
    tag menu
    
    use cg_gallery(page=page,doTrans=doTrans)
    
    grid 3 1:
        xalign 0.5
        yalign 0.5
        style "cgpage_grid"
        
        if doTrans:
            at gui_fade(1.0)
        
        ############### ADD CGS HERE ##################
        
        # The first string is the name of your button, which should
        # correspond to your g.button() definitions at line ??.
        
        # The second string is the path to your thumbnail.
        # Make sure your thumbnail is 334x188. 
        
        use cg_slot("cg laptop", "images/cg/laptop_thumb.png")
        use cg_slot("cg ending3_pic",  "images/cg/ending3_pic_thumb.png")
        use cg_slot("cg ending5_pic", "images/cg/ending5_pic_thumb.png")
        
        # Since a grid must be full, null objects are added to fill the last
        # 2 cells.
        #null
        #null
        
screen cg_page2(page=2,doTrans=False):
    tag menu
    
    use cg_gallery(page=page,doTrans=doTrans)
    
    grid 3 2:
        style "cgpage_grid"
        
        null
        null
        null
        null
        null
        null
        
        
##########
# STYLES #
##########
        
style cgpage_grid:
    xalign 0.5 yalign 0.55
    spacing 60
    ypos 10