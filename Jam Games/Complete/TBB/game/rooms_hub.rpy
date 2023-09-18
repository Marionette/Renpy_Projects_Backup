# Room Hub 

label nueroom_hub:

    if not Nuehatesyou:
        hide screen walkaround
        scene bg nuebase      
        menu:
            "Talk":
                call nueroom
            "Look around":
                "Nue room description."
                call nueroom_hub
            "Leave":    
                hide nue base
                call lbl_mapStart_hallway1 
    else:
        "The room is locked from the inside."
return

label deisroom_hub:
    hide screen walkaround
    scene bg deisroom
    menu:
        "Knock":
            call deisroom    
        "Leave":    
            hide mc base
    jump lbl_mapStart_hallway1
            
return

label maryroom_hub:
    hide screen walkaround
    menu:
        "Talk":
            call maryroom
        "Read a book":
            call readabookinlibrary
        "Leave":    
            hide mr base
            call lbl_mapStart_hallway2
            
return

label morcoroom_hub:
    hide screen walkaround
    scene bg clockroomcat
    menu:
        "Talk":
            call morcoroom
        "Look at clock":
            "The time is frozen."
            call morcoroom_hub
        "Leave":    
            hide morc base
            call lbl_mapStart_hallway1 
            
return

label moguroom_hub:
    hide screen walkaround
    show bg starroom
    menu:
        "Talk":
            call moguroom
        "Talk to the stars":
            call talktostars
        "Leave":    
            hide morc base
            call lbl_mapStart_hallway2 
            
return
