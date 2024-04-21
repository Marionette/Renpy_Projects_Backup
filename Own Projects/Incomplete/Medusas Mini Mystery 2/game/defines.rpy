init:
    # A preference that enables or disables timed choices.
    default torch_brightness = 0.98
    
    ###### POSITION DEFINES ############
    #transform left:
    #  yalign 1.0 xanchor .5 xalign 0.25
      
    #transform right:
    #  yalign 1.0 xanchor .5 xalign 0.75
    
    transform rotateButton(_rotate=0):
      rotate _rotate
        
    transform show_snake(_y=1.0, _x=1.0, _zoom=1.0, _time=1.0):
      #crop(00,00,1920, 1080)
      #parallel:#        
      #  linear _time crop(800,400,200, 200)
      parallel:
        linear _time yalign _y
      parallel:
        linear _time xalign _x
      parallel:
        linear _time zoom _zoom
        
    transform PositionBg(_zoom=1.0, _xpan=1.0, _ypan=1.0, _time=1.0):
      align (0.0,0.0)
    
      parallel:
        linear _time zoom _zoom
      parallel:
        linear _time xpan _xpan
      parallel:
        linear _time ypan _ypan
      
      #linear 36 xpan 360
      #xpan 0
      #repeat
        
    transform PositionBgInstant(_zoom=1.0, _xpan=1.0, _ypan=1.0):
      align (0.0,0.0)
      zoom _zoom
      xpan _xpan
      ypan _ypan
    
    transform show_medusa_instant():
      xalign 0.5
      yalign 1.0
      zoom 0.3
    
    transform show_medusa_head_instant():
      xalign 0.5
      yalign 0.1
      zoom 0.5
    transform show_medusa_head():
      show_snake(0.1, 0.5, 1.5, 1.0)
      #xalign 0.5
      #parallel:
      #  linear 0.8 yalign 0.1
      #parallel:
      #  linear 0.8 zoom 0.5
    
    transform show_medusa_head_nod():
      show_medusa_head()
      linear 0.3 yalign 0.2
      linear 0.3 yalign 0.1
      linear 0.3 yalign 0.2
      linear 0.3 yalign 0.1
    
    transform show_medusa():
      xalign 0.5
      parallel:
        linear 1.0 yalign 1.0
      parallel:
        linear 1.0 zoom 1.0
    
    transform show_medusa_close():
      xalign 0.5
      parallel:
        linear 1.0 yalign 0.2
      parallel:
        linear 1.0 zoom 0.4
    
    transform show_medusa_closer():
      xalign 0.5
      parallel:
        linear 1.0 yalign 0.3
      parallel:
        linear 1.0 zoom 0.5
      
    
    transform show_side_medusa_instant():
      crop (550,100,820, 680)
      xalign 0.0
      yalign 1.0
      zoom 1.0
      
    transform show_snake1():
      show_snake(0.5, 0.45, 3.0, 1.0)
    
    transform show_snake2():
      show_snake(0.5, 0.3, 3.0, 1.0)
    
    transform show_snake3():
      show_snake(0.10, 0.70, 3.0, 1.0)
    
    transform show_snake4():
      show_snake(0.3, 0.3, 3.0, 1.0)
    
    transform show_snake5():
      show_snake(0.5, 0.75, 3.0, 1.0)
    
    transform show_snake6():
      show_snake(0.40, 0.70, 3.0, 1.0)
      
    transform show_donut:
      show_snake(0.9, 0.6, 4.0, 1.0)
      
    transform show_snake_crop(_left=0, _top=0, _width=1080, _height=1920, _zoom=3.0): #x, y, width, height
      #crop (550,100,820, 680)
      parallel:
        linear 1.0 crop(_left, _top, _width, _height)
      parallel:
        linear 1.0 zoom _zoom
      
    
    transform show_side_full(): #Melissa
      yalign 1.0
      show_snake_crop(550,100,820, 680, 1.0)
        
    transform show_side_snake1(): #Agnesss
      #show_snake(0.52, 0.45, 3.0, 1.0)
      show_snake_crop(750,450,200, 200)
    
    transform show_side_snake2(): #Beatrisss
      #show_snake(0.5, 0.3, 3.0, 1.0)
      show_snake_crop(600,400,200, 200)
    
    transform show_side_snake3(): #Casssie
      #show_snake(0.10, 0.70, 3.0, 1.0)
      show_snake_crop(1100,100,400, 200)
    
    transform show_side_snake4(): #Daisssy
      #show_snake(0.3, 0.3, 3.0, 1.0)
      show_snake_crop(600,250,200, 200)
    
    transform show_side_snake5(): #Elissse
      #show_snake(0.5, 0.75, 3.0, 1.0)
      show_snake_crop(1150,450,200, 200)
    
    transform show_side_snake6(): #Francesssca
      #show_snake(0.40, 0.70, 3.0, 1.0)
      show_snake_crop(1100,350,200, 200)
      
    
    ######### MISC DEFINES #############
    define slow_dissolve = Dissolve(2.0)
                        
    # Declare characters used by this game. The color argument colorizes the
    # name of the character.
    define Agnesss_name      = "Agnesss"
    define Beatrisss_name    = "Beatrisss" 
    define Casssie_name      = "Casssie"
    define Daisssy_name      = "Daisssy"
    define Elissse_name      = "Elissse"
    define Francesssca_name  = "Francesssca"
    define Any_name  = "Anyone"
    
    #variables
    default selected_item = ""
    default potion_philstone_found = False
    default potion_philstone = False
    
    default ingredient_list = []

    ######### CHARACTER DEFINES #############Characters:
    #Medusa - Melissa
    define m = Character("Melissa", image="medusa")
    #Snake 1 - Agnesss
    define a = DynamicCharacter("Agnesss_name", image="medusa")
    #Snake 2 - Beatrisss
    define b = DynamicCharacter("Beatrisss_name", image="medusa")
    #Snake 3 - Casssie
    define c = DynamicCharacter("Casssie_name", image="medusa")
    #Snake 4 - Daisssy
    define d = DynamicCharacter("Daisssy_name", image="medusa")
    #Snake 5 - Elissse
    define e = DynamicCharacter("Elissse_name", image="medusa")
    #Snake 6 - Francesssca
    define f = DynamicCharacter("Francesssca_name", image="medusa")
    
   
    define named = DynamicCharacter("Any_name")
    
    define everyone = Character("All")
    define minotaur = Character("Minotaur")
    define cb = Character("Voice")
    
  
    ######### SOUND DEFINES #############
    #$bgm = "audio/music/bgm.mp3"
    
    #define audio.music_all = "<loop 5.130>audio/I36.ogg"
    #define audio.music_all_noKick = "<from 5.130>audio/I36.ogg"
    #define audio.music_kick = "<to 5.130>audio/I36.ogg"
    #define audio.music_mystery = "<from 5.930 to 33.135>audio/I36.ogg"
    #define audio.music_interrogation = "<from 33.135 to 60.387>audio/I36.ogg"
    
    ######### CG/BG IMAGE DEFINES #############
    image black = Solid("#000000")  
    image bg black = Solid("#101012") #almost black
    image bg white = Solid("#ffffff")
    
    #Backgrounds 
    #image bg kitchen = Composite((1920, 1080), (0, 0), "images/bg_kitchen.png", (0, 0),"images/item_donut.png")
    #image bg kitchen nodonut = "images/bg_kitchen.png"
    
    #CG images
    
    image medusa = im.Crop("images/Medusa3.png",(550,0,820, 1080))
    image medusa shock = im.Crop("images/Medusa3.png",(550,0,820, 1080))
    #image side_medusa = im.Crop("images/Medusa3.png",(570,100,820, 580))
    image side_medusa = "images/Medusa3.png"
    
    
    ######### GAME DEFINES #############
    default string_2_found = False
    default string_3_found = False
    default string_4_found = False
    
    define item_default = ["default", "Something", "a thing.", "I'm not sure we can do anything with this."]
    define item_list = [
        #["item_id", "Item Name", "item description", "hint text"]
        ##Items at wall 1 ##
        ["door", "Door", "A solid wooden door.", "We need to unlock this to be able to leave."],
        ["door_symbol", "Door Symbol", "A magical symbol.", "I this this is just for show."],
        ["door_lock_1", "Lock 1", "A magical lock with a keyhole.", "We need a key to unlock this lock."],
        ["door_lock_2", "Lock 2", "A magical lock with a keyhole.", "We need a key to unlock this lock."],
        ["door_lock_3", "Lock 3", "A magical lock with a keyhole.", "We need a key to unlock this lock."],
        ["door_lock_4", "Lock 4", "A magical lock with a keyhole.", "We need a key to unlock this lock."],
        ["plant_left", "Plant", "A curious plant.", "I this this is just for show."],
        ["plant_right", "Plant", "A curious plant.", "I this this is just for show."],
        ["stairs", "Stairs", "The stairs to the floor above.", "These stairs lead to the door out."],
        ["crystal ball", "Crystal Ball", "A crystal ball.", "I wonder if we can activate it?"],
        ["table_small", "Small Table", "A small table.", "I think this this is just for show."],
        ["table_small_drawer", "Drawer", "A small drawer on the table.", "The drawer doesn't seem to open, maybe theres a way to unlock it?"],
        ["recipe_l2g_torn_right", "Torn Recipe", "A torn recipe.", "This looks like part of a recipe."],
        ["hint_papers_1", "Papers", "A pile of papers.", "Maybe we can find something useful among these papers."],
        
        ##Items at wall 2 ##", "##Items At Wall 2 ##", "##Items at wall 2 ##", "##Items at wall 2 ##
        ["notes", "Notes", "notes", "notes"],
        ["painting_1", "Painting", "painting of a penguin.", "Painting of a penguin."],
        ["painting_2", "Painting", "Painting of a cactus.", "Painting of a cactus."],
        ["painting_3", "Painting", "Painting of a hand.", "Painting of a hand."],
        ["painting_4", "Painting", "Painting of a mermaid.", "Painting of a mermaid."],
        ["painting_5", "Painting", "Painting of a demon.", "Painting of a demon."],
        ["painting_6", "Painting", "Painting of a frog.", "Painting of a frog."],
        ["painting_7", "Painting", "Painting of a snake.", "Painting of a snake."],
        ["painting_8", "Painting", "Painting of some teeth.", "Painting of some teeth."],
        ["painting_9", "Painting", "Painting of a mushroom.", "Painting of a mushroom."],
        ["painting_10", "Painting", "Painting of a devil.", "Painting of a devil."],
        ["painting_11", "Painting", "Painting of a skull.", "Painting of a skull."],
        ["painting_12", "Painting", "Painting of a ship.", "Painting of a ship."],
        ["painting_13", "Painting", "Painting of a fish.", "Painting of a fish."],
        ["painting_14", "Painting", "Painting of a broom.", "Painting of a broom."],
        ["painting_15", "Painting", "Painting of a cat on a pumpkin.", "Painting of a cat on a pumpkin."],
        ["painting_16", "Painting", "Painting of a witch.", "Painting of a witch."],
        ["painting_17", "Painting", "Painting of a cat with many eyes.", "Painting of a cat with many eyes."],
        ["lyre", "Lyre", "A musical instrument.", "A musical instrument."],
        ["lyre_string_1", "Lyre String", "A string that makes a sound when plucked.", "A string that makes a sound when plucked."],
        ["lyre_string_2", "Lyre String", "A string that makes a sound when plucked.", "A string that makes a sound when plucked."],
        ["lyre_string_3", "Lyre String", "A string that makes a sound when plucked.", "A string that makes a sound when plucked."],
        ["lyre_string_4", "Lyre String", "A string that makes a sound when plucked.", "A string that makes a sound when plucked."],
        ["lyre_string_5", "Lyre String", "A string that makes a sound when plucked.", "A string that makes a sound when plucked."],
        ["lyre_pedestal", "Pedestal", "A stone pedestal.", "A stone pedestal."],
        ["lyre_pedestal_drawer", "Pedestal Drawer", "A small drawer.", "A small drawer."],
        ["drawers", "Drawers", "A chest of drawers.", "A chest of drawers."],
        ["drawers_notes", "Drawers Scratches", "Some scratches on the side of some drawers.", "Some scratches on the side of some drawers."],
        ["drawers_hint_papers", "Papers", "A pile of papers.", "A pile of papers."],
        ["drawers_top", "Drawer", "A drawer with a handle.", "A drawer with a handle."],
        ["drawers_middle", "Drawer", "A drawer with musical notes.", "A drawer with musical notes."],
        ["drawers_bottom", "Combination Lock", "A drawer with a combination lock.", "A drawer with a combination lock."],
        
        ##Items at wall 3 ##", "##Items At Wall 3 ##", "##Items at wall 3 ##", "##Items at wall 3 ##
        ["poster", "Poster", "a strange poster.", "Is this related to potion making somehow?"],
        ["fire_mantle", "Fire Mantle", "Fire mantle above the fireplace.", "Doesn't look like theres anything on the mantelpiece."],
        ["fire_place", "Fire Place", "The fireplace.", "The cauldron fits snugly in this fireplace."],
        ["cauldron", "Cauldron", "An empty witches cauldron.", "Looks like a black key is stuck to the bottom of the inside of it."],
        ["shelf_left", "Ingredient Shelves", "Shelves full of ingredients.", "Looks like all the ingredients on these shelves can be used to make potions."],
        ["shelf_right", "Ingredient Shelves", "Shelves full of ingredients.", "Looks like all the ingredients on these shelves can be used to make potions."],
        ["ingredient_salt", "Salt", "A jar of salt.", "A jar of salt. I think it can be used to make potions."],
        ["ingredient_allspice", "Allspice", "A jar of allspice.", "A jar of allspice. I think it can be used to make potions."],
        ["ingredient_cumin", "Cumin", "A jar of cumin.", "A jar of cumin. I think it can be used to make potions."],
        ["ingredient_coriander", "Coriander", "A jar of coriander.", "A jar of coriander. I think it can be used to make potions."],
        ["ingredient_garlic", "Garlic", "A jar of garlic.", "A jar of garlic. I think it can be used to make potions."],
        ["ingredient_dust", "Dust", "A jar of dust.", "A jar of dust. I think it can be used to make potions."],
        ["ingredient_tears", "Tears", "A jar of tears.", "A jar of tears. I think it can be used to make potions."],
        ["ingredient_harpy_feather", "Harpy Feather", "A jar of harpy feathers", "A jar of harpy feathers I think it can be used to make potions."],
        ["ingredient_slime_red", "Slime Red", "a cube of red slime.", "a cube of red slime. I think it can be used to make potions."],
        ["ingredient_onion", "Onion", "An onion.", "An onion. I think it can be used to make potions."],
        ["ingredient_slime_blue", "Slime Blue", "A box of blue slime.", "A box of blue slime. I think it can be used to make potions."],
        ["ingredient_book_worms", "Book Worms", "Books crawling with bookworms.", "Books crawling with bookworms. I think it can be used to make potions."],
        ["ingredient_campfire_ash", "Campfire Ash", "A dish of campfire ash.", "A dish of campfire ash. I think it can be used to make potions."],
        ["ingredient_cheese_holes", "Cheese Holes", "A wedge of cheese filled with holes.", "A wedge of cheese filled with holes. I think it can be used to make potions."],
        ["ingredient_music_sheet", "Music Sheet", "Some sheet music.", "You think we can play this music somewhere? Or is it for something else?"],
        ["ingredient_recipe", "Recipe", "A potion recipe.", "I wonder if this potion would be useful at all?"],
        ["ingredient_dragon_fang", "Dragon Fang", "A skull filled with dragon fangs.", "A skull filled with dragon fangs. I think it can be used to make potions."],
        ["ingredient_candle_wax", "Candle Wax", "Some candle wax", "Some candle wax. I think it can be used to make potions."],
        ["ingredient_quicksilver", "Quicksilver", "a pot of quicksilver.", "a pot of quicksilver. I think it can be used to make potions."],
        ["ingredient_poison", "Poison", "Bottles of poison.", "Bottles of poison. I think it can be used to make potions."],
        ["ingredient_candle_wicks", "Candle Wicks", "A pile of candles with extended wicks.", "A pile of candles with extended wicks. I think it can be used to make potions."],
        ["ingredient_dragon_orbs", "Dragon Orbs", "A few magical spheres.", "A few magical spheres. I think it can be used to make potions."],
        ["ingredient_harpy_talon", "Harpy Talon", "A harpys talon.", "A harpys talon. I think it can be used to make potions."],
        ["ingredient_dragon_scale", "Dragon Scale", "Some dragon scales.", "Some dragon scales. I think it can be used to make potions."],
        ["ingredient_emerald_ice", "Emerald Ice", "Some emerald ice.", "Some emerald ice. I think it can be used to make potions."],
        ["ingredient_cyclops_eye", "Cyclops Eye", "A jar of cyclops eyes.", "A jar of cyclops eyes. I think it can be used to make potions."],
        ["ingredient_cupboard_left", "Cupboard", "A cupboard.", "It doesn't look like theres anything useful in here."],
        ["ingredient_cupboard_right", "Frozen Cupboard", "A frozen cupboard.", "Its frozen solid, is there a way to melt the ice so we can get inside?"],
        ["recipe_l2g_torn_left", "Torn Recipe", "A torn recipe.", "This looks like part of a recipe."],
        ##Items at wall 4 ##", "##Items At Wall 4 ##", "##Items at wall 4 ##", "##Items at wall 4 ##
        ["poster_maze", "Poster", "a strange poster.", "It looks kindof like a maze. Could these symbols mean something?"],
        ["poster_1", "Poster", "A strange poster.", "Is this something we can use?"],
        ["poster_2", "Poster", "A strange poster.", "Is this something we can use?"],
        ["poster_3", "Poster", "A strange poster.", "Is this something we can use?"],
        ["table_large", "Large Table", "A large table.", "A large table with various materials strewn across it."],
        ["box", "Magic Box", "A magic box.", "This box is magically sealed. Do we need some sort of spell to open it?"],
        ["table_hint_papers_left", "Papers", "A pile of papers.", "Maybe we can find something useful among these papers."],
        ["table_hint_papers_right", "Papers", "A pile of papers.", "Maybe we can find something useful among these papers."],
        ["table_book", "Magic Book", "A magical book.", "Its a magical tome but most of the pages have been torn our or are blank. Are the ones that remain important?"],
        ]
        
    
init python:
    def GetItemDetails(_id=""):
        if _id == "":
            return item_default
        for item in item_list:
            if item[0] == _id:
                return item