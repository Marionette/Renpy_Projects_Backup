# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init python:
    iCurrDress = 0
    iCurrHair = 0
    
    
    #TODO: Parameterize everything so one function does all possible combinations
    #TODO: Add possibility for Action poses for different emotions (May mean renaming sprites)
    #TODO: Change all sprites to be the same size as the base so i can supply (0 , 0) for the positions and simplify the issues with different size emotion sprites
    def draw_char(st, at): 
        return LiveComposite( 
            (174,479),
            (0, 0),         "character/sketch_body_base1.png",
            (-175, -48),    "character/sketch_hair_long%d.png" %iCurrHair, 
            (60, 25),       "character/sketch_face_happy1.png",
            (-175, -48),    "character/sketch_%s_dress%d.png" %("outfit", iCurrDress),
            ), .1
            
        #return LiveComposite( 
        #    (106,294),
        #    (-300, -400),         "character/marionette_Body.png",
        #    (-300, -400),         "character/marionette_hime.png",
        #    (-300, -400),         "character/marionette_really-happy.png",
        #    (-300, -400),         "character/marionette_maid.png",
        #    ), .1
    #TODO: Get this side image to update correctly
    #TODO: Get Side image to display correctly. 
    def draw_char_side(st, at): # same thing as above, just scaled and positioned for the sideimage; there's probably more elegant solution than this...
        return LiveComposite(
            (174,479),
            (0, 0),         im.FactorScale("character/sketch_body_base1.png", .45, .45),
            (-175, -48),    im.FactorScale("character/sketch_hair_long%d.png" %iCurrHair, .45, .45),
            (60, 25),       im.FactorScale("character/sketch_face_happy1.png", .45, .45),
            (-175, -48),    im.FactorScale("character/sketch_%s_dress%d.png" %("outfit", iCurrDress), .45, .45),
            ), .1
            
            
init:
    # Declare characters used by this game.
    define e = Character('Eileen', color="#c8ffc8")
    image bg black = "#000000"
    image bg white = "#ffffff"
    image sketch only1eye = "character/sketch_full_1eye.png"
    image sketch happy = "character/sketch_full_happy.png"
    image sketch shock = "character/sketch_full_shock.png"
    image side sketch happy = DynamicDisplayable(draw_char_side)
    $ sketchName = "????"
    $ sketch = DynamicCharacter("sketchName", color=(192, 64, 64, 255), window_left_padding=180, image="sketch")
    image sketch dress happy = DynamicDisplayable(draw_char) # using DynamicDisplayable ensures that any changes are visible immediately
    #story flags


# The game starts here.
label start:

label lbl_DRAWING_ARC:
    #TODO: remove test code from the middle of the introduction scene! D:<
    $ iCurrDress = 0
    $ iCurrHair = 0
    $ bSawEventPuppy1 = False
    $ bStayBald = False

    show bg black with dissolve
    #show text "Hey"
    sketch "Hey."
    sketch "Hey!"
    sketch "HEY!!!"
    
    show bg white with dissolve
    show sketch only1eye
    show sketch dress happy
    
    sketch "Oh you're awake. Hi."
    $ iCurrDress = 3
    hide sketch
    show sketch dress happy
    sketch "Do you know what time it is?"
    $ iCurrDress = 2
    hide sketch
    show sketch dress happy
    sketch "What?"
    "What?"
    $ iCurrHair = 1
    hide sketch
    show sketch dress happy
    sketch "Who am i?"
    $ iCurrHair = 2
    hide sketch
    show sketch dress happy
    sketch "I dunno, you haven't given me a name yet."
    
    $ sketchName = renpy.input("Give her a name.")
    
    sketch "Hmm, %(sketchName)s. I guess it'll have to do."
    sketch "Anyways i think you still have to finish your work."
    sketch "Don't just stand there staring. Hurry up and draw."
    
label lbl_drawEyesMenu:
    menu:
        "What will you draw?"
        "Draw eyes":
            jump lbl_drawEyesEvent
        "Draw boobs":
            call lbl_drawBoobsEvent
        "Draw a puppy":
            call lbl_drawPuppyEvent
    jump lbl_drawEyesMenu




label lbl_drawEyesEvent:
    "..scribble scribble..."
    show sketch happy
    sketch "Fiiiiiiinally."
    sketch "Depth perception here i come!"
    jump lbl_drawMirror
    
label lbl_drawBoobsEvent:
    "..scribble scribble..."
    sketch "WHOA!"
    sketch "What do you think you're doing mister?!"
    "...erase erase..."
    sketch "H-Hey, i didn't say...nevermind."
    sketch "Easy come easy go. ;-;"
    return
    #jump lbl_drawEyesMenu
    
label lbl_drawPuppyEvent:
    $ bSawEventPuppy1 = True
    "..scribble scribble..."
    sketch "Awwwwwwwww, how cute."
    sketch "Who's a good boy?" 
    sketch "Whosagoodboy?" 
    sketch "whoosagooodboooy?"
    sketch "Ahhh! It bit me. D:"
    sketch "Anyways, thats not what i meant when i said draw."
    "...erase erase..."
    return
    #jump lbl_drawEyesMenu


    
label lbl_drawMirror:
    sketch "Hmmm... What should we have you do next?"
    sketch "You know this would be a lot easier if i could tell what i looked like."
    sketch "Can you think of anything that would help?"
    
label lbl_drawMirrorMenu:
    menu:
        "What would help her see what she looks like?"
        "Draw mirror":
            jump lbl_drawMirrorEvent
        "Draw photograph":
            call lbl_drawPhotoEvent
        "Draw a puppy":
            call lbl_drawPuppyEvent2
    jump lbl_drawMirrorMenu



label lbl_drawMirrorEvent:
    "..scribble scribble..."
    sketch "Awesome i can see what i look like now."
    sketch "Hmm...There's not a lot to look at right now, is there?"
    sketch "Somebody needs to stop slacking."
    sketch "..."
    sketch "I mean you."
    jump lbl_drawHair

label lbl_drawPhotoEvent:
    "..scribble scribble..."
    sketch "Oh hey a photo, pretty cool."
    sketch "Is this me?"
    sketch "I dont look like much at the moment."
    sketch "Wait, if you change anything this photo wont show it."
    sketch "...Damn."
    "...erase erase..."    
    return

label lbl_drawPuppyEvent2:
    "..scribble scribble..."
    if (bSawEventPuppy1 == True):
        sketch "This guy again?"
    sketch "I really want to play fetch now."
    sketch "I wish i had something to throw"
    "..scribble scribble..."
    sketch "cool, a stick"
    sketch "*throws*"
    sketch "Fetch!"
    sketch "Go get it boy!"
    sketch "You're supposed to fetch it."
    sketch "..."
    sketch "Stupid dog."
    "...erase erase..."    
    return
            
            

label lbl_drawHair:
    sketch "Now that i look at myself i kindof feel like theres something lacking."
    sketch "My head seems really big for some reason."
    sketch "Oh wait, silly me, i know why."
    sketch "I have no hair."
    sketch "Be a dear and sort that out would you?"
    sketch "What kind of hair would i like?"
    sketch "Er, i dunno you're the artist."
    sketch "Maybe something cute..."
    sketch "Or maybe something cool..."
    sketch "Maybe something awesome..."
    jump lbl_drawHairMenu
    
        
label lbl_drawHairMenu:
    menu:
        "What kind of hairstyle will you give her?"
        "Long hair":
            call lbl_drawHairLongEvent
        "Short hair":
            call lbl_drawHairShortEvent
        "Curls":
            call lbl_drawHairCurlsEvent
        "Bald":
            call lbl_drawHairNoneEvent
            if (bStayBald == False):
                jump lbl_drawHairMenu
    #jump lbl_drawMirrorMenu
    jump lbl_drawClothes


label lbl_drawHairLongEvent:
    "..scribble scribble..."
    sketch "Hmm, lets see..."
    sketch "Its so long and beautiful."
    sketch "I feel like a princess~"
    sketch "One should like a cup of tea, post haste~"
    sketch "Ahem. "
    sketch "Sorry i got carried away."
    sketch "Anyways, i love it. Thanks. ^_^"
    return
    

label lbl_drawHairShortEvent:
    "..scribble scribble..."
    sketch "Hmm, lets see..."
    sketch "Its short and cute."
    sketch "I feel like a bit of a tomboy now~"
    sketch "Anyways, i like it. Thanks. ^_^"
    return

label lbl_drawHairCurlsEvent:
    "..scribble scribble..."
    sketch "Hmm, lets see..."
    sketch "So curly!"
    sketch "Im like a rich girl now."
    sketch "Look at all the common people struggling down there like ants."
    sketch "Ohohohohoho~"
    sketch "Ahem. "
    sketch "Sorry i got carried away."
    sketch "Anyways, i love it. Thanks. ^_^"
    return
    
    

label lbl_drawHairNoneEvent:
    "..scribble scribble..."
    sketch "Hmm, lets see...  "  
    show sketch shock
    sketch "AHHH! So bright!"
    sketch "HEY!"
    sketch "You just made my big bald head shiney!"
    sketch "I am so not okay with this."
    sketch "Fix it now."
    
    menu:
        "Will you change it?"
        "Yes":
            $ bStayBald = False
        "No":
            $ bStayBald = True
    
    if (bStayBald == True):
        sketch "...I hate you."
    else: 
        sketch "Thank goodness. "
          
    show sketch happy
    return

    
    
label lbl_drawClothes:
    sketch "What now?"
    sketch "Cold?"
    sketch "Why would i be cold?"
    sketch "Oh because im naked."
    sketch "..."
    show sketch shock
    sketch "I-IM N-N-NAKED?!"
    sketch "Dont look!"
    sketch "Draw me some clothes right now!"
    sketch "D-Don't look, you pervert!"
    sketch "DRAW WITH YOUR EYES CLOSED IF YOU HAVE TO!"
    "..scribble scribble..."
    sketch "Whats that? I cant wear that!"
    sketch "What use is a screen to me?!"
    sketch "Hide behind it so you can look at what you're drawing without seeing me?" 
    sketch "...thats actually a good idea."
    sketch "Ok tell me when you are done with the outfit and ill try it on."
    show sketch happy
    
    jump lbl_drawClothesMenu
    

label lbl_drawClothesMenu:
    menu:
        "What kind of clothes will you draw?"
        "A Dress":
            call lbl_drawDressEvent
        "Trousers":
            call lbl_drawTrousersEvent
        "A certain outfit":
            call lbl_drawOutfitEvent
    jump GOOD_END
    

label lbl_drawDressEvent:
    $ bLongDress = False
    $ bCompliment = False
    menu:
        "What kind of dress will you draw?"
        "A long Dress":
            $ bLongDress = True
        "Something short":
            $ bLongDress = False
        
    "..scribble scribble..."
    sketch "..."
    sketch "Oh, you're finished?"
    sketch "Lets try it on."
    sketch "Oh a dress, cool."
    sketch "..."
    if (bLongDress == False):
        sketch "Hmm, this seems pretty short..."
    sketch "There, done."
    sketch "So?"
    sketch "How do i look?"
    menu:
        "How do you think she looks?"
        "How Elegant" if (bLongDress == True):
            $ bCompliment = True
        "So Sexy" if (bLongDress == False):
            $ bCompliment = True
        "Pretty Cute":
            $ bCompliment = True
        "Eww":
            $ bCompliment = False
    
    if (bCompliment == False):
        sketch "Have i told you how much i dislike you lately?"
        sketch "Give me something else then."
        jump lbl_drawClothesMenu
    
    sketch "Awww, thanks~"
    sketch "I have to say i like it too. :3"
    
    return
    
    
label lbl_drawTrousersEvent:
    "..scribble scribble..."
    $ bShorts = False
    $ bCompliment = False
    menu:
        "What kind of trousers will you draw?"
        "Long ones":
            $ bShorts = False
        "Shorts":
            $ bShorts = True
        
    "..scribble scribble..."
    sketch "..."
    sketch "Oh, you're finished?"
    sketch "Lets try it on."
    if (bShorts == False):
        sketch "Oh trousers and a t-shirt, cool."
    else:
        sketch "Oh shorts and a t-shirt, cool."
    sketch "..."
    sketch "There, done."
    sketch "So?"
    sketch "How do i look?"
    menu:
        "How do you think she looks?"
        "How Sporty" if (bShorts == True):
            $ bCompliment = True
        "Totally cool" if (bShorts == False):
            $ bCompliment = True
        "Pretty Cute":
            $ bCompliment = True
        "Eww":
            $ bCompliment = False
    
    if (bCompliment == False):
        sketch "Have i told you how much i dislike you lately?"
        sketch "Give me something else then."
        jump lbl_drawClothesMenu
    
    sketch "Awww, thanks~"
    sketch "I have to say i like it too. :3"
    return

label lbl_drawOutfitEvent:
    "..scribble scribble..."
    $ iOutfit = 0
    $ bCompliment = False
    menu:
        "What kind of outfit will you draw?"
        "School Uniform":
            $ iOutfit = 1
        "Nurse Outfit":
            $ iOutfit = 2  
        "Maid Outfit":
            $ iOutfit = 3          
        "Martial Arts Garb" if (bStayBald == True):
            $ iOutfit = 4
            #lol krillan
    
    if (iOutfit == 1):
        sketch "We're gonna be late for class Onii-chan~"
    if (iOutfit == 2):
        sketch "Are you hurt anywhere?"
    if (iOutfit == 3):
        sketch "Welcome Home Master~"
    if (iOutfit == 4):
        sketch "DISTRUCTO DISK!!!!"
    
    sketch "But in all seriousness, are you really going to make me wear..."
    sketch "...this?"
    
    menu:
        "How will you respond?"
        "Yes":
            sketch "W-Well i guess that says a lot about your...tastes."
        "No":
            sketch "Thank goodness."
            sketch "Now lets try something else"
            jump lbl_drawClothesMenu
    jump lbl_goodnight
    
    
label lbl_goodnight:
    sketch "Hmm, looks like we're pretty much done now."
    sketch "Its late?"
    sketch "You better get some sleep then."
    "zzzzzzz..."
    
    jump lbl_ADVENTURE_ARC
    

label GOOD_END:
    "And they all lived happily ever after..."
    return





