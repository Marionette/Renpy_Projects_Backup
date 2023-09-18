image Love Ending:
    "cgs/Love Ending.png"
image Sachi shot:
    "cgs/Sachi shot.png"
image Kusanagi stabbed:
    "cgs/Kusanagi stabbed.png"
image examplepic1:
    "cgs/examplepic.png"
init python:

    # Step 1. Create the gallery object.
    g = Gallery()

    # Step 2. Add buttons and images to the gallery.

    g.button("Love Ending")
    g.unlock_image("Love Ending")
    g.button("Sachi shot")
    g.unlock_image("Sachi shot")
    g.button("Kusanagi stabbed")
    g.unlock_image("Kusanagi stabbed")
    g.button("examplepic1")
    g.unlock_image("examplepic1")

    # The transition used when switching images.
    g.transition = dissolve
    
    #Stylings
    style.cg_rm_button = Style(style.button)
    style.cg_rm_button.background = Frame("GUI/cg_frame.png",40,35)
    style.cg_rm_button.hover_background = Frame(im.MatrixColor("GUI/cg_frame.png",im.matrix.brightness(-0.1)),40,35)
    style.cg_rm_button.xpadding = 40
    style.cg_rm_button.ypadding = 40
    style.cg_rm_button.xalign = 0.5
    style.cg_rm_button.yalign = 0.5
    
    g.idle_border =  Frame("GUI/cg_overlay.png",40,40)
    g.hover_border = Frame("GUI/cg_overlay_hover.png",40,40)
    g.locked_button = "GUI/cg_locked.png"
    
screen cg_gallery:
    # Ensure this replaces the main menu.
    tag menu

    # The background.
    add "GUI/gm_bg.jpg"
    add "upsidedown_nav" xalign 0.5 yalign 0.0
    
    add "GUI/title_cg.png" xalign 0.5 yalign 0.09

    # A grid of buttons.
    grid 4 3:

        spacing 15 xalign 0.5 yalign 0.55

        # Call make_button to show a particular button.
        add g.make_button("Love Ending", "cgs/examplepic_s.png",  style="cg_rm_button") 
        add g.make_button("Sachi shot", "cgs/Sachi shot_s.png", style="cg_rm_button")
        add g.make_button("Kusanagi stabbed", "cgs/Kusanagi stabbed_s.png", style="cg_rm_button")
        add g.make_button("examplepic1", "cgs/examplepic_s.png", style="cg_rm_button")
        add g.make_button("examplepic1", "cgs/examplepic_s.png", style="cg_rm_button")
        add g.make_button("examplepic1", "cgs/examplepic_s.png", style="cg_rm_button")
        add g.make_button("examplepic1", "cgs/examplepic_s.png", style="cg_rm_button")
        add g.make_button("examplepic1", "cgs/examplepic_s.png", style="cg_rm_button")
        add g.make_button("examplepic1", "cgs/examplepic_s.png", style="cg_rm_button")
        add g.make_button("examplepic1", "cgs/examplepic_s.png", style="cg_rm_button")
        add g.make_button("examplepic1", "cgs/examplepic_s.png", style="cg_rm_button")
        add g.make_button("examplepic1", "cgs/examplepic_s.png", style="cg_rm_button")

    # The screen is responsible for returning to the main menu. It could also
    # navigate to other gallery screens.
    add "GUI/nav_bar.png" xalign 0.5 yalign 1.0
    textbutton "Return" action ShowMenu("extras") xalign 0.5 yalign 0.98
    

################################# MUSIC ROOM

init python:

    # Step 1. Create a MusicRoom instance.
  mr = MusicRoom(fadeout=1.0)

    # Step 2. Add music files.
  mr.add("BGM/Reprieve.ogg", always_unlocked=True)
  mr.add("BGM/Nostalgia.ogg")
  mr.add("BGM/Demise.ogg")
  mr.add("BGM/Emergency.ogg")
  mr.add("BGM/casual.ogg")
  mr.add("BGM/contemplation.ogg")
  mr.add("BGM/Ending Forgotten.ogg")
  mr.add("BGM/Ending Untold.ogg")
  mr.add("BGM/guilt.ogg")
  mr.add("BGM/Gunpoint2.ogg")
  mr.add("BGM/heartwarming.ogg")
  mr.add("BGM/Imminet Danger2.ogg")
  mr.add("BGM/intense.ogg")
  mr.add("BGM/Mornings Rise.ogg")
  mr.add("BGM/Proximate Hearts.ogg")
  mr.add("BGM/reflective.ogg")
  mr.add("BGM/Revive.ogg")
  mr.add("BGM/Rift.ogg")
  mr.add("BGM/Sunset.ogg")
  mr.add("BGM/The Ground Trembles.ogg")
  mr.add("BGM/Through.ogg")
  mr.add("BGM/Question.ogg")
    

  style.music_rm_button.selected_background = Frame("GUI/button2_music.png",60,0)
  style.music_rm_button.xminimum = 700


# Step 3. Create the music room screen.
screen music_gallery:

    tag menu
    # The background.
    add "GUI/gm_bg.jpg"
    add "upsidedown_nav" xalign 0.5 yalign 0.0
    
    add "GUI/title_music.png" xalign 0.5 yalign 0.125

    vbox xalign 0.5 yalign 0.5:
        # The buttons that play each track.
        textbutton "Track 1" action mr.Play("BGM/Reprieve.ogg") style "music_rm_button" at mm_button_hover
        textbutton "Track 2" action mr.Play("BGM/Nostalgia.ogg")  style "music_rm_button" at mm_button_hover
        textbutton "Track 3" action mr.Play("BGM/Demise.ogg") style "music_rm_button" at mm_button_hover
        textbutton "Track 4" action mr.Play("BGM/Emergency.ogg")  style "music_rm_button" at mm_button_hover
        textbutton "Track 5" action mr.Play("BGM/casual.ogg") style "music_rm_button" at mm_button_hover
        textbutton "Track 6" action mr.Play("BGM/contemplation.ogg") style "music_rm_button" at mm_button_hover
        textbutton "Track 7" action mr.Play("BGM/Ending Forgotten.ogg") style "music_rm_button" at mm_button_hover
        textbutton "Track 8" action mr.Play("BGM/Ending Untold.ogg") style "music_rm_button" at mm_button_hover
        textbutton "Track 9" action mr.Play("BGM/guilt.ogg")style "music_rm_button" at mm_button_hover
        textbutton "Track 10" action mr.Play("BGM/Gunpoint2.ogg") style "music_rm_button" at mm_button_hover


    add "GUI/nav_bar.png" xalign 0.5 yalign 1.0
    hbox xalign 0.5 yalign 0.98 spacing 25:
        # Buttons that let us advance tracks.
        textbutton "Next Song" action mr.Next()
        # The button that lets the user exit the music room.
        textbutton "Return" action ShowMenu("extras")
        textbutton "Previous Song" action mr.Previous()
        
    add SnowBlossom("GUI/bokeh.png", count=10, border=10, xspeed=(5, 250), yspeed=(50, 200), start=0, horizontal=True)

    # Start the music playing on entry to the music room.
    on "replace" action mr.Play()

    # Restore the main menu music upon leaving.
    on "replaced" action mr.Stop()



init python:
    
    
    style.scg_button = Style(style.button)
    style.scg_button.background = Frame("gui/cg_frame.png",40,35)
    style.scg_button.hover_background = Frame(im.MatrixColor("gui/cg_frame.png",im.matrix.brightness(-0.1)),40,35)
    style.scg_button.xpadding = 40
    style.scg_button.ypadding = 40
    style.scg_button.xalign = 0.5
    style.scg_button.yalign = 0.5

screen scene_gallery:

    tag menu
    # The background.
    add "GUI/gm_bg.jpg"
    add "upsidedown_nav" xalign 0.5 yalign 0.0
    
    add "GUI/title_scene.png" xalign 0.5 yalign 0.09

    grid 4 3:
        
        spacing 15 xalign 0.5 yalign 0.55
        
        button:
            style"scg_button"
            action If(persistent.Love_Scene, Replay("Love_Scene")) 
            if persistent.Love_Scene :
                image ("cgs/examplepic_s.png")
            else :
                image ("gui/cg_locked.png")
        
        button:
            style"scg_button"
            action If(persistent.Yandere, Replay("Holding")) 
            if persistent.Yandere :
                image ("cgs/Sachi shot_s.png")
            else :
                image ("gui/cg_locked.png")
        
        button:
            style"scg_button"
            action If(persistent.Alfheim, Replay("Alfheim")) 
            if persistent.Alfheim :
                image ("cgs/Kusanagi stabbed_s.png")
            else :
                image ("gui/cg_locked.png")
        
        button:
            style"scg_button"
            action If(persistent.myfirstscene, Replay("Regret")) 
            if persistent.myfirstscene :
                image ("cgs/examplepic_s.png")
            else :
                image ("gui/cg_locked.png")
        
        button:
            style"scg_button"
            action If(persistent.myfirstscene, Replay("Arrested")) 
            if persistent.myfirstscene :
                image ("cgs/examplepic_s.png")
            else :
                image ("gui/cg_locked.png")
        
        button:
            style"scg_button"
            action If(persistent.myfirstscene, Replay("Yandere")) 
            if persistent.myfirstscene :
                image ("cgs/examplepic_s.png")
            else :
                image ("gui/cg_locked.png")
        
        button:
            style"scg_button"
            action If(persistent.myfirstscene, Replay("Hope, Joy and Despair")) 
            if persistent.myfirstscene :
                image ("cgs/examplepic_s.png")
            else :
                image ("gui/cg_locked.png")
        
        button:
            style"scg_button"
            action If(persistent.myfirstscene, Replay("Confusion and Misunderstandings")) 
            if persistent.myfirstscene :
                image ("cgs/examplepic_s.png")
            else :
                image ("gui/cg_locked.png")
        
        button:
            style"scg_button"
            action If(persistent.myfirstscene, Replay("Love_Scene")) 
            if persistent.myfirstscene :
                image ("gui/cg_overlay.png")
            else :
                image ("gui/cg_locked.png")
        
        button:
            style"scg_button"
            action If(persistent.myfirstscene, Replay("Love_Scene")) 
            if persistent.myfirstscene :
                image ("gui/cg_overlay.png")
            else :
                image ("gui/cg_locked.png")
        
        button:
            style"scg_button"
            action If(persistent.myfirstscene, Replay("Love_Scene")) 
            if persistent.myfirstscene :
                image ("gui/cg_overlay.png")
            else :
                image ("gui/cg_locked.png")
        
        button:
            style"scg_button"
            action If(persistent.myfirstscene, Replay("Love_Scene")) 
            if persistent.myfirstscene :
                image ("gui/cg_overlay.png")
            else :
                image ("gui/cg_locked.png")
        
        #textbutton "Love Ending" action Replay("Love_Scene")
        #textbutton "Earthquake" action Replay("Earthquake")
        #textbutton "Holding her tight" action Replay("Holding_her_tight")
        #textbutton "Regret" action Replay("Regret")
        #textbutton "Arrested" action Replay("Arrested")
        #textbutton "Yandere Mode" action Replay("Yandere_Mode")
        #textbutton "Hope, Joy and Despair" action Replay("Hope_Joy_and_Despair")
        #textbutton "Confusion and Misunderstandings" action Replay("Confusion_and_Misunderstandings")


    add "gui/nav_bar.png" xalign 0.5 yalign 1.0
    
    textbutton "Return" action ShowMenu("extras") xalign 0.5 yalign 0.98
        
    add SnowBlossom("GUI/bokeh.png", count=10, border=10, xspeed=(5, 250), yspeed=(50, 200), start=0, horizontal=True)


################################# MISC
    
screen extras:
    tag menu
    
    add "gui/mm_bg.jpg"
    
    add "gui/logo.png" at lower_down

    # The main menu buttons.
    vbox:
        style_group "mm"
        xalign .5
        yalign .75
        spacing 10
    
    
        imagebutton idle "gui/gallery1.png" hover "gui/gallery2.png" xalign 0.5 action ShowMenu("cg_gallery") at mm_button_hover
        imagebutton idle "gui/music1.png" hover "gui/music2.png" xalign 0.5 action ShowMenu("music_gallery") at mm_button_hover
        imagebutton idle "gui/scene1.png" hover "gui/scene2.png" xalign 0.5 action ShowMenu("scene_gallery") at mm_button_hover
        imagebutton idle "gui/main1.png" hover "gui/main2.png" xalign 0.5 action Return() at mm_button_hover
    
    add SnowBlossom("gui/bokeh.png", count=10, border=10, xspeed=(5, 250), yspeed=(50, 200), start=0, horizontal=True)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"