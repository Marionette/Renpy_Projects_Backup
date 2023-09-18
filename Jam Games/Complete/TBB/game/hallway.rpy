# hallway foibles #

label hallway:
    show bg hallway01
    if foundMarystory and not Ponchuiswhizzingabout:
        "There's that creature again!"
        "It runs away before you can chase it."
        $ Ponchuiswhizzingabout = True
    if Manticoreawake and not Manticoreawakedone:
        "Oh you feel like you're being chased."
        "Ponchu comes in"
        "Here! Hide here!"
        "and you enter the hole."
        $ Manticoreawakedone = True
        call ororoom  
    else:
        menu:
            "Nue Room.":
                call nueroom_hub
            "Talk to Deis":
                call deisroom
            "Morcobashi Room.":
                call morcoroom
            "Edelia" if not chap1done:
                call edelia
            "Mogu" if helpMogufindfood and not librarypathclear:
                call moguroomfirst
            "Second floor" if librarypathclear or ignoreMogu:
                call secondhallway
            "Dark Room" if unicornhorn or ramhorn:
                call darkroom
          
return

label secondhallway:
    show bg hallway02
    menu:
        "Go to library":
            call maryroom_hub
        "Go to starroom" if ignoreMogu or librarypathclear:
            call moguroom
        "Go to flowerroom":
            call flowerroom
        "Downstairs":
            call hallway
            
label thirdhallway:
    menu:
        "Go to Ororo's Room":
            call ororoom
        "Go to Throne Room.":
            call throneroom
        "Go Downstairs":
            call secondhallway
