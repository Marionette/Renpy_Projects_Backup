


init python:
    #Galleries settings - start
    #list the CG gallery images here:
    gallery_cg_items = ["bg gunsarah",
                        "bg angrysarah",
                        "bg bloodyfoot",
                        "bg choke",
                        "bg choke2",
                        "bg sarahcries",
                        "bg sarahcriesblur",
                        "bg door",
                        "bg angrymike",
                        "bg bloodysarah",
                        "bg bloodysarahsmirk",
                        "bg sarahshot",
                        "bg sarahchoke",
                        "bg sarahchokeglance",
                        "bg scarydope",
                        "bg bloodymike",
                        "bg gun",
                        "bg mirror",
                        "bg mikedies",
                        "bg mikewins",
                        "bg dopewins"]
    #list the BG gallery images here (if a BG includes several variations, such as night version, include only one variation here):
    gallery_bg_items = ["bg room", "bg blur", "bg room2"]
    
    #how many rows and columns in the gallery screens?
    gal_rows = 3
    gal_cols = 3
    #thumbnail size in pixels:
    thumbnail_x = 267
    thumbnail_y = 163
    #the setting above (267x150) will work well with 16:9 screen ratio. Make sure to adjust it, if your are using 4:3 or something else.
    #Galleries settings - end
    
    gal_cells = gal_rows * gal_cols    
    g_cg = Gallery()
    for gal_item in gallery_cg_items:
        g_cg.button(gal_item + " butt")
        g_cg.image(gal_item)
        g_cg.unlock(gal_item)
    g_cg.transition = fade
    cg_page=0
    prev_cg_page = 0  
    next_cg_page = 0  

    g_bg = Gallery()
    for gal_item in gallery_bg_items:
        g_bg.button(gal_item + " butt")
        g_bg.image(gal_item)
        g_bg.unlock(gal_item)
        #if BGs have variations, such as night version, uncomment the lines below and include the code for each BG with variations
#        if gal_item == "bg kitchen":
#            g_bg.image("bg kitchen dining")
#            g_bg.unlock("bg kitchen dining")
    g_bg.transition = fade
    bg_page=0  
    
init +1 python:
    #Here we create the thumbnails. We create a grayscale thumbnail image for BGs, but we use a special "locked" image for CGs to prevent spoilers.
    for gal_item in gallery_cg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
    for gal_item in gallery_bg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
        renpy.image (gal_item + " butt dis", im.Grayscale(ImageReference(gal_item + " butt")))
        
screen cg_gallery:
    tag menu
    add "img/bg/ui/MiscMenu_background.png"
    use Navigation2    
    
    $ prev_cg_page = cg_page - 1  
    $ next_cg_page = cg_page + 1          
    $pagetext = "Page [next_cg_page]" 
    text pagetext xpos 27 ypos 10
    frame background None xpos 10 ypos 25:
        grid gal_rows gal_cols:
            ypos 10
            $ i = 0
            if next_cg_page > int(len(gallery_cg_items)/gal_cells):
                $ next_cg_page = 0          
            if prev_cg_page < 0:
                $ prev_cg_page = 0
            for gal_item in gallery_cg_items:
                $ i += 1
                if i <= (cg_page+1)*gal_cells and i>cg_page*gal_cells:
                    add g_cg.make_button(gal_item + " butt", gal_item + " butt", im.Scale("img/bg/ui/gallery/locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
            for j in range(i, (cg_page+1)*gal_cells): #we need this to fully fill the grid
                null

    imagebutton auto "img/bg/ui/gallery/Next_%s.png" xpos 20 ypos 600 focus_mask None action [SetVariable('cg_page', next_cg_page), ShowMenu("cg_gallery")]
    imagebutton auto "img/bg/ui/gallery/Previous_%s.png" xpos 20 ypos 640  focus_mask None action [SetVariable('cg_page', prev_cg_page), ShowMenu("cg_gallery")]
screen bg_gallery:
#The BG gallery screen is more or less copy pasted from the CG screen above, I only changed "make_button" to include a grayscale thumbnail for locked items
    tag menu
    add "img/bg/ui/MiscMenu_background.png"
    use Navigation2
    frame background None xpos 10:
        grid gal_rows gal_cols:
            ypos 10
            $ i = 0
            $ next_bg_page = bg_page + 1
            if next_bg_page > int(len(gallery_bg_items)/gal_cells):
                $ next_bg_page = 0
            for gal_item in gallery_bg_items:
                $ i += 1
                if i <= (bg_page+1)*gal_cells and i>bg_page*gal_cells:
                    add g_bg.make_button(gal_item + " butt", gal_item + " butt", gal_item + " butt dis", xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
            for j in range(i, (bg_page+1)*gal_cells):
                null
        frame:
            yalign 0.97
            vbox:
                if len(gallery_bg_items)>gal_cells:
                    textbutton _("Next Page") action [SetVariable('bg_page', next_bg_page), ShowMenu("bg_gallery")]