# Room Hub 

label nueroom_hub:  
    hide screen walkaround
    if gotNuemask:
        scene bg nuemask
    else:
        scene bg nuebase      
    menu:
        "Talk":
            call nueroom from _call_nueroom
        "Look around" if not Nueisyourfriend:
            "There is a collection of masks on the wall."
            jump nueroom_hub
        "Talk to masks" if Nueisyourfriend:
            jump Nuemasks
        "Leave":    
            hide nue base
            hide mc horns
            hide mc tail
            call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_6

return

label deisroom_hub:
    hide screen walkaround
    scene bg deisroom
    if mcramhorns:
        show mc horns at mcleft
    else:
        show mc base at mcleft
    menu:
        "Knock":
            play sound knock
            call deisroom from _call_deisroom    
        "Leave":    
            hide mc base
    jump lbl_mapStart_hallway1
    hide mc base        
return

label morcoroom_hub:
    if goodpathdone:
        call morco_demo from _call_morco_demo_1
    hide screen walkaround
    scene bg clockroomcat
    
    menu choicesMorco:
        "Talk":
            call morcoroom from _call_morcoroom
        "Look at clock":
            "The time is frozen."
            call morcoroom_hub from _call_morcoroom_hub_4
        "Leave":    
            jump lbl_mapStart_hallway1
            
return

#label maryroom_hub:
#    hide screen walkaround
#    menu:
#        "Talk":
#            hide screen walkaround
#            call maryroom from _call_maryroom
#        "Read a book":
#            call readabookinlibrary from _call_readabookinlibrary
#        "Leave":    
#            hide mr base
#            call lbl_mapStart_hallway2 from _call_lbl_mapStart_hallway2_6
            
#return 

label moguroom_hub:
    hide screen walkaround
    scene bg starroom
    menu:
        "Talk":
            call moguroom from _call_moguroom
        "Talk to the stars":
            call talktostars from _call_talktostars
        "Leave":    
            hide morc base
            call lbl_mapStart_hallway2 from _call_lbl_mapStart_hallway2_7          
return
