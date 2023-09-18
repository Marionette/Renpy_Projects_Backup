# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init python:

  adv_menu = menu

init:
  # Declare characters used by this game.
  ####Character defines####
  define e = Character('Eileen', window_background="images/ui/textbox/textbox.png")
  define b = Character('Brian', window_background="images/ui/textbox/textbox.png")
  define narrator = Character(None, window_background="images/ui/textbox/textbox.png")
  
  define o = Character(None, kind = nvl,  what_xalign=0.5)
  define en = Character('Eileen', kind = nvl,  what_xalign=0.5, who_xalign=0.3)
  define bn = Character('Brian', kind = nvl,  what_xalign=0.5, who_xalign=0.3)
  
init:

  image cg brianf = "images/cg/CG_brianf.png"  
  image cg brianr = "images/cg/CG_brianr.png"  
  image cg leef = "images/cg/CG_leef.png"  
  image cg leer = "images/cg/CG_leef.png"  
  
  image nvl_window = "images/ui/textbox/NVL.png"

# The game starts here.
label start:

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    e "The girl's bullet blasts past my head, shards of broken glass crash to the floor from the window behind me.  My bare legs trembling in fear, I fall to the ground without the strength to stand. A young woman stands facing in my direction, somewhere in her early twenties." 
    
    "A black dress adorns her body, like the midnight sky in a lonely grave.  I'm scared. My eyes refuse to turn away, despite the struggles I put forth, entangled in the horrifying scene before me while my limbs hang limply by my side, as the barrel of the gun stays primed towards my being."
    
    menu:
      "This is a choice."
      "Option 1 - brianf":
        show cg brianf
        pass
      "Option 2 - leef":
        show cg leef
        pass
        
    menu:
      "This is a different choice."
      "This is a really long option, i wonder how well it will look":
        pass
      "I wonder":
        pass
      "How it":
        pass
      "Will look":
        pass
      "With so":
        pass
      "Many Options":
        pass
        
    e "just kidding these do nothing."
    
    show nvl_window
    nvl clear
    o "Now testing Nvl."
    
    o "The girl's bullet blasts past my head, shards of broken glass crash to the floor from the window behind me.  My bare legs trembling in fear, I fall to the ground without the strength to stand. A young woman stands facing in my direction, somewhere in her early twenties." 
    
    nvl clear
    bn "A black dress adorns her body, like the midnight sky in a lonely grave."
    en "I'm scared. My eyes refuse to turn away, despite the struggles I put forth, entangled in the horrifying scene before me while my limbs hang limply by my side, as the barrel of the gun stays primed towards my being."
    
    nvl clear
    
    $menu = nvl_menu
    menu:
      bn "What now?"
      "Option 1 - brianf":
        show cg brianf
        pass
      "Option 2 - leef":
        show cg leef
        pass
    
    en "Oh i see."
    
    menu:
      bn "And then?"
      "Option 1 - brianf":
        show cg brianf
        pass
      "Option 2 - leef":
        show cg leef
      "Option 3 - leef":
        show cg leef
      "Option 4 - leef":
        show cg leef
        pass
    
    en "Oh ok."
    
    o "Done testing Nvl."
    hide nvl_window
    
    ""
    $menu = adv_menu
    
    menu:
      e "What now?"
      "Option 1 - brianf":
        show cg brianf
        pass
      "Option 2 - leef":
        show cg leef
        pass
        
    e "thats all folks."
    return
