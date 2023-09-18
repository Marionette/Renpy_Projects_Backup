
label lbl_ADVENTURE_ARC:
    sketch "Hey!"
    sketch "HEY!!"
    sketch "How long are you going to sleep for?!"
    
    sketch "Oh there you are."
    sketch "I thought maybe id lost you."
    sketch "You know \"Don't go into the light~\" etc"
    sketch "Hahahaha"
    sketch "So what are we going to do today?"
    sketch "Do i get some friends?"
    sketch "How about some colour?"
    
    sketch "A Deadline?"
    sketch "What for?"
    sketch "What kind of story?"
    
    jump lbl_storyChoiceMenu

    
label lbl_storyChoiceMenu:
    menu:
        "What kind of story do you have to write?"
        "Adventure":
            jump lbl_storyAdveture
        "Romance":
            jump lbl_storyRomance
        "Mystery":
            jump lbl_storyMystery
            
            
label lbl_storyAdveture:
    sketch "Ohhhh an adventure! Count me in!"
    


label lbl_storyRomance:
    sketch "Romance?"
    sketch "You mean... i could... fall in love? <3"
    
label lbl_storyMystery:
    sketch "There's a mystery somewhere going unsolved?!"
    sketch "Detective %(sketchName)s is on the case!"
    
    
    
    jump lbl_GOOD_END