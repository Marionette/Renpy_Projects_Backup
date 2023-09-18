
#------------------------------------------------------------------------------------------
# Main menu animations

image menu_logo:
    "gui/MinamiLogo.png"
    subpixel True
    xalign 0.4
    ypos -100
    zoom 0.60
    menu_logo_move
    
image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 0.5
    easein_quint 1 xoffset 0

transform menu_item_move(_ystart=-1000, _timeStart=0.6):
    subpixel True
    yoffset _ystart
    time _timeStart
    ease .2 yoffset 50
    ease .2 yoffset 0

transform menu_item_move(_ystart=-1000, _timeStart=0.6):
    subpixel True
    yoffset _ystart
    time _timeStart
    ease .2 yoffset 50
    ease .2 yoffset 0
#------------------------------------------------------------------------------------------
# character does a little hop when shown
transform chibihop():
    subpixel True
    yoffset 1200
    time 0.1
    ease .5 yoffset 500
    time 2.1
    ease .5 yoffset 1200
#------------------------------------------------------------------------------------------
# character does a little hop when shown
transform hop(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0

#------------------------------------------------------------------------------------------
# character bounces out to the left when shown    
transform leftbounceout(x=640, z=0.80):
    parallel:
        xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
        easein 2.25 xcenter -300 
    parallel:
        ease .2 yoffset 25
        ease .2 yoffset 0
        repeat

# character bounces in from the left when shown    
transform leftbouncein(x=640, z=0.80):
    parallel:
        xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
        easein 2.25 xcenter x
    parallel:
        ease .2 yoffset 25
        ease .2 yoffset 0
        repeat
        
# character rushes straight in from the left when shown 
transform leftin(x=640, z=0.80):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x

#------------------------------------------------------------------------------------------
# character bounces out to the right when shown    
transform rightbounceout(x=640, z=0.80):
    parallel:
        xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
        easein 2.25 xcenter 1920+300 
    parallel:
        ease .2 yoffset 25
        ease .2 yoffset 0
        repeat

# character bounces in from the right when shown    
transform rightbouncein(x=640, z=0.80):
    parallel:
        xcenter 1920+300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
        easein 2.25 xcenter x
    parallel:
        ease .2 yoffset 25
        ease .2 yoffset 0
        repeat
        
# character rushes straight in from the right when shown 
transform rightin(x=640, z=0.80):
    xcenter 1920+300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x


#------------------------------------------------------------------------------------------

#Redefined for easy calls based on character onscreen position

#------------------------------------------------------------------------------------------
#static hops
transform hopLeft:
    hop(240)
transform hopCenterLeft:
    hop(480)
transform hopCenter:
    hop(960)
transform hopCenterRight:
    hop(1440)
transform hopRight:
    hop(1680)

#------------------------------------------------------------------------------------------
#Left moves
transform straightInLeftToLeft:
    leftin(240)
transform straightInLeftToCenterLeft:
    leftin(480)
transform straightInLeftToCenter:
    leftin(960)
transform straightInLeftToCenterRight:
    leftin(1440)
transform straightInLeftToRight:
    leftin(1680)

transform bounceInLeftToLeft:
    leftbouncein(240)
transform bounceInLeftToCenterLeft:
    leftbouncein(480)
transform bounceInLeftToCenter:
    leftbouncein(960)
transform bounceInLeftToCenterRight:
    leftbouncein(1440)
transform bounceInLeftToRight:
    leftbouncein(1680)

transform bounceOutToLeftFromLeft:
    leftbounceout(240)
transform bounceOutToLeftFromCenterLeft:
    leftbounceout(480)
transform bounceOutToLeftFromCenter:
    leftbounceout(960)
transform bounceOutToLeftFromCenterRight:
    leftbounceout(1440)
transform bounceOutToLeftFromRight:
    leftbounceout(1680)
#------------------------------------------------------------------------------------------
#right moves
transform straightInRightnToLeft:
    rightin(240)
transform straightInRightToCenterLeft:
    rightin(480)
transform straightInRightToCenter:
    rightin(960)
transform straightInRightToCenterRight:
    rightin(1440)
transform straightInRightToRight:
    rightin(1680)

transform bounceInRightToLeft:
    rightbouncein(240)
transform bounceInRightToCenterLeft:
    rightbouncein(480)
transform bounceInRightToCenter:
    rightbouncein(960)
transform bounceInRightToCenterRight:
    rightbouncein(1440)
transform bounceInRightToRight:
    rightbouncein(1680)

transform bounceOutToRightFromLeft:
    rightbounceout(240)
transform bounceOutToRightFromCenterLeft:
    rightbounceout(480)
transform bounceOutToRightFromCenter:
    rightbounceout(960)
transform bounceOutToRightFromCenterRight:
    rightbounceout(1440)
transform bounceOutToRightFromRight:
    rightbounceout(1680)
#------------------------------------------------------------------------------------------