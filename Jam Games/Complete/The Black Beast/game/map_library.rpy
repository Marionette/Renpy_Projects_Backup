
################################################################################
## Map screens - Library
################################################################################
init:
    $currentLocation3 = 1000

label lbl_mapStart_library:
    show screen walkaround
  
    call screen MapScreen_library(currentLocation3)
    call expression _return from _call_expression2
    
    

#################################################################################

screen MapScreen_library(_xPosOffset=0):
    tag map
    zorder -2
    #add "images/map/bg-hallway01_for prog.png" xpos 0 - _xPosOffset 
    add Solid("#000000")    
    add "images/map_library/linebase.png" xpos 0 - _xPosOffset 
        
    imagebutton auto "images/map_library/bg-library_mary_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("maryroom") 
    if not ramhorn:
        imagebutton auto "images/map_library/bg-library_horn_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("hornevent")
    
    imagebutton auto "images/map_library/clockexitlibrary_%s.png" xpos (0 - _xPosOffset) focus_mask True action Return("lbl_mapStart_clockexit1") 
#    imagebutton auto "images/map_library/bookshelf1_%s.png" xpos (355 - _xPosOffset) focus_mask True action Return("lbl_mapStart_bookshelf") 
    imagebutton auto "images/map_library/bookshelf2_%s.png" xpos (571 - _xPosOffset) focus_mask True action Return("lbl_mapStart_bookshelf") 
    
    #Walking navigation
    use MapScreen_navigation("MapScreen_library", _xPosOffset, 0, 1808)
 
#--------------------------------------------------------------------------------

label hornevent:
    hide screen walkaround   
    scene bg ramskull
    "It's a portrait of a ram skull."
    if not MaryknowsweaponMary:
        show mc at mcleft
        show mr at chright
        mr "Hey!"
        mr "Why are you snooping around?"
    if (bookforDeis or didnottakehorn) and not Marygivesunicornhorn and MaryknowsweaponMary:
        show mr at chright
        show mc at mcleft
        mr "Hey."
        mr "Can I ask you why you're looking for a dead god's horn?"
        mr "Do you even know what it's for?"
        mc "..."
        if didnottakehorn:
            mr "I can tell you're not a bad guy because you didn't take the horn."
        else:
            mr "I can tell you're not a bad guy..."
        mr "But I don't think you have a clue."
        mr "That skull belonged to a vengeful spirit, and it's be better if you leave it alone."
        mr "We keep that portrait there because it keeps coming back even though we put it away."
        #TODO: pause
        mr "..."
        mr "Well...?"
        mr "*sighs*"
        mr "Don't make such a sad face."
        mr "Here."
        "Mary hands me a heavy-looking white stone."
        mc "...?"
        "The stone shimmered when I moved it in my hand."
        play sound itemtwinkle
        "Got shimmery stone."
        mr "What? You think that's a piece of rock?!"
        mr "You really are clueless!"
        mr "That's a unicorn horn!"
        mr "That has the same properties of a ram horn, but without the evil magic."
        mr "It looks like a rock because the horn was broken in pieces."
        mr "Anyway, just use that for whatever you want."
        mr "Forget about the ram horn. It'll just give you trouble."
        $ unicornhorn = True
        $ Marylikesyou = True
        $ Marygivesunicornhorn = True
        $ firstmission = False
        hide mr
        hide mc at mcleft
        call lbl_mapStart_library from _call_lbl_mapStart_library  
    if not chap1done and not unicornhorn and not puzzlegameforhorndone and MaryknowsweaponMary:
        show mr at chright
        show mc at mcleft
        mr "Hey, you're a snooper pooper, aren't you."
        mr "You look really shady sneaking around here."
        mr "You want a horn of dead god? Then yeah, it's that portrait."
        mr "Bet you don't even know what you're dealing with, though."
        mr "You just do stuff without fully understanding things."
        mc "..."
        mr "Why do you even need it, hm?"
        mc "..."
        mr "Leave the portrait alone!"
        hide mr
        $renpy.pause(delay=None)
        "I waited for Mary to leave."
        "When she went to another end of the library, I examined the portrait 
        closely."
        $renpy.pause(delay=None)
        "There is a gold plate below it that read:"
        "Bind thy Will to the Light\n
        F E A - - R"
        $ puzzlegameforhorn = True
        $ puzzlegameforhorndone = True
    if answertohornpuzzle and not answertohornpuzzleMary and not didnottakehorn:
        show mc at mcleft
        "I fumbled around the right wall behind the portrait, and I felt a button."
        "I pressed the button and a ramhorn fell out of gold plate."
        show bg ramskullnohorn
        play sound horndrop
        $ horndropped = True
        "When I looked back at the portrait, the skull is missing a horn."
        menu:
            "Take the horn?":
                pass
            "Don't take it.":
                $ didnottakehorn = True
                jump lbl_mapStart_library
                
        play sound itemtwinkle
        "Got ram horn"
        show mr at chright
        mr "What are you doing?!"
        mr "I told you not to take it!"
        mr "Get out!"
        $ Maryhatesyou = True
        $ firstmission = False
        $ ramhorn = True
        $ answertohornpuzzleMary = True
        hide mr
        hide mc at mcleft
        call lbl_mapStart_hallway2 from _call_lbl_mapStart_hallway2
    jump lbl_mapStart_library

return
  
label lbl_mapStart_clockexit1:
    hide screen walkaround
    scene bg black
    hide mc
    hide mc horns
    hide mc tail
    show bg library:
        xpos 0 + (1808/2) - currentLocation3
    if not clockexit1_seen:    
        "There doesn't seem to be an exit in this library."
        "There is a clock that doesn't work."
        "I felt compelled to touch the frozen clock."
        $ clockexit1_seen = True
    "Where do I want to go?"
    menu:
        "First Floor Hallway":
            jump lbl_mapStart_hallway1
        "Second Floor Hallway":            
            jump lbl_mapStart_hallway2
        "Stay here":
            jump lbl_mapStart_library
        "Somewhere else" if chap1done:
            menu:
                "Clockroom":
                    jump morcoroom_hub
                "Nue's Room":
                    if Nuehatesyou:
                        "I can't go there."
                        return
                    jump nueroom_hub
                "Star Room":
                    if Moguhatesyou:
                        "I can't go there."
                        return
                    if not chap1done:
                        "I can't go there yet."
                        return
                    jump moguroom_hub    
                "Garden" if keytoflowerroom:
                    jump flowerroom    
return


label lbl_mapStart_bookshelf:
    hide screen walkaround
    scene bg black
    hide mc
    hide mc horns
    hide mc tail
    show bg library:
        xpos 0 + (1808/2) - currentLocation3
    menu:
        "Read a book?":
            jump readabookinlibrary
        "Do nothing":
            jump lbl_mapStart_library
        
return
