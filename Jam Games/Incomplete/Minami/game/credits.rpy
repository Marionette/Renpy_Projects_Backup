
label lbl_showCredits:

    $ quick_menu = False
    play music config.main_menu_music
    $ renpy.pause(0.2, hard=True)

    image splash = "gui/MinamiLogo.png"
    image thanks eng = Text("{color=[gui.idle_color]}{size=80}Thanks for Playing!{/color}", text_align=0.5, drop_shadow = (2, 2), drop_shadow_color = "#000000")
    $ credits_duration = 40 # credits duration in seconds
    scene bg game_menu_overlay with Dissolve(1.0)  #replace this with a fancy background

    image cred_eng = Text("{color=#ffffff}[gui.credits]{/color}", text_align=0.5, drop_shadow = (2, 2), drop_shadow_color = "#000000")
    show cred_eng at Move((0.5, 5.0), (0.5, 0.0), credits_duration, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with dissolve

    # wait for Credits to end, and do not allow user click (can still exit via pause menu)
    $ renpy.pause(credits_duration, hard=True)

    show splash with dissolve
    $ renpy.pause(2.0, hard=True)
    hide splash with dissolve
    $ renpy.pause(1.0, hard=True)
    show thanks eng:
        yalign 0.55
        xalign 0.55
    with dissolve
    $ renpy.pause(2.0, hard=True)
    hide thanks with dissolve
    $ renpy.pause(1.0, hard=True)

    show bg black with dissolve

    stop music fadeout 2.0
    $ renpy.pause(2.0, hard=True)

    return
