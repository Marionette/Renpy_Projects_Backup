###################################################################
# The dialogue here probably wants to be updated in the real game #
###################################################################

# Call this label to start the minigame
label minigame_start():
    scene limbokin_grey
    #minigame_player "This is an introduction to the mini game! This text probably wants to be re-written."
    #show screen minigame_trade_status
    while minigame_current_buyer < len(minigame_buyer_map):
        call minigame_buyer() from _call_minigame_buyer
        if minigame_trades >= 5:
            #minigame_player "Oh, I'm out of things to trade..."
            #jump minigame_finished
            return
    #minigame_player "No one else seems to be coming. I guess that was everyone I could trade with..."
    #jump minigame_finished
    return


#label minigame_finished():
    #hide screen minigame_trade_status
    #minigame_player "Looks like I made [minigame_trades] trades and collected [minigame_teeth] teeth."
    #if minigame_teeth >= 7:
    #    minigame_player "I won! What do I win?"
    #else:
    #    minigame_player "Looks like I came up short of what I needed. Oh well."
    #return


################################################################
# You may wish to customize the screen, but it is not required #
################################################################

screen minigame_drag_clothing():
    if store.minigame_current_buyer == 0:
        text "Drag a clothing item to the Limbokin." text_align 0.5 xalign 0.5 yalign 0.0 yoffset 50 color "#000"

    draggroup:
        drag:
            drag_name "0"
            child "minigame_buyer[minigame_current_buyer] clothes0"
            droppable False
            dragged clothing_dragged
            ycenter 0.3 xcenter 0.1
        drag:
            drag_name "1"
            child "minigame_buyer[minigame_current_buyer] clothes1"
            droppable False
            dragged clothing_dragged
            yalign 0.5 xcenter 0.85
        if minigame_current_buyer not in minigame_fewer_options:
            drag:
                drag_name "2"
                child "minigame_buyer[minigame_current_buyer] clothes2"
                droppable False
                dragged clothing_dragged
                ycenter 0.8 xcenter 0.2

        # Transparent drag target because the sprite is already centered
        drag:
            drag_name "drop_target"
            child Transform("#fff0", size=(500, 800))
            draggable False
            xalign 0.5 yalign 1.0
    
#################################################################################
# Customize or remove this screen (if you don't want current status to display) #
#################################################################################
screen minigame_trade_status():
    vbox:
        xalign 1.0
        yalign 0.0
        xoffset -50
        yoffset 50
        text "Trades Made: [minigame_trades]" color "#000" xalign 1.0
        text "Teeth: [minigame_teeth]" color "#000" xalign 1.0

####################################################
# You should not need to touch anything under here #
####################################################

init python:
    def clothing_dragged(drags, drop):
        if not drop:
            return
        store.minigame_selected_clothing = drags[0].drag_name
        return True

label minigame_buyer():
    $ minigame_selected_clothing = ""
    $ minigame_buyer_obj = minigame_buyer_map[minigame_current_buyer]
    $ minigame_buyer_name = minigame_buyer_obj.name
    show expression "images/minigame/POKERFIGURE.png" at center as thefigure with dissolve
    #minigame_buyer "[minigame_buyer_obj.greeting]"
    call expression minigame_buyer_obj.greeting from _call_expression
    menu:
        "What question should you ask?"
        "How did you die?":
            call expression minigame_buyer_obj.die_response from _call_expression_1
        "How do you feel about life in purgatory?":
            call expression minigame_buyer_obj.life_response from _call_expression_2
        "What do you miss most about life on Earth?":
            call expression minigame_buyer_obj.earth_response from _call_expression_3
    minigame_buyer "[minigame_buyer_obj.trade_dialogue]"
    show minigame_white_bg behind thefigure with dissolve
    window hide
    call screen minigame_drag_clothing() with dissolve
    if minigame_selected_clothing == str(minigame_buyer_obj.clothing_order[0]):
        if minigame_current_buyer in minigame_fewer_options:
            show expression "images/minigame/SMILEFIGURE.png" at center as thefigure with dissolve
            $ minigame_buyer_offer = 1
        else:
            show expression "images/minigame/HEARTFIGURE.png" at center as thefigure with dissolve
            $ minigame_buyer_offer = 2
    elif (minigame_current_buyer not in minigame_fewer_options) and minigame_selected_clothing == str(minigame_buyer_obj.clothing_order[1]):
        show expression "images/minigame/SMILEFIGURE.png" at center as thefigure with dissolve
        $ minigame_buyer_offer = 1
    else:
        show expression "images/minigame/ANGRYFIGURE.png" at center as thefigure with dissolve
        $ minigame_buyer_offer = 0
    hide minigame_white_bg with dissolve
    window auto
    if minigame_buyer_offer > 0:
        if minigame_buyer_offer > 1:
            if minigame_buyer_obj.trade2_label is not None:
                call expression minigame_buyer_obj.trade2_label from _call_expression_4
            else:
                minigame_buyer "[minigame_buyer_obj.trade2_response]"
        else:
            minigame_buyer "[minigame_buyer_obj.trade1_response]"
        menu:
            "Accept the offer":
                $ minigame_teeth += minigame_buyer_offer
                $ minigame_trades += 1
                "Congratulations! The trade has been closed!"
                if minigame_buyer_offer == 2:
                    "The Limbokin walks away, looking very happy."
                else:
                    "The Limbokin walks away, looking satisfied."
            "Reject the offer":
                "You decide to reject the offer. "
                "The Limbokin walks away, looking dissatisfied."
    else:
        #minigame_buyer "[minigame_buyer_obj.reject_response]"
        "The Limbokin hates your offer!"
        "The Limbokin walks away, looking upset."
    #minigame_buyer "[minigame_buyer_obj.closing]"
    hide thefigure with dissolve
    $ minigame_current_buyer += 1
    return