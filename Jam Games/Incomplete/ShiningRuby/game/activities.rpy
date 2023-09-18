# Shining Ruby Test Activities #

label activities:
    
    "Today we are going to test out various activities using the mini map."
    "Make your choice on which activity to choose."
    menu:
        "Activity 1":
            jump activity_1
        "Activity 2":
            jump activity_2
            
label activity_1:
    
    show bg bedroom
    "Good Morning World!"
    "Today I have to go to school."
    "I better get ready."
    
    #Open the bedroom arrows up.
    
    #When they click on the one arrow it will take them to the kitchen. Continue this script in the kitchen
    
    show bg kitchen
    "I better hurry or else I'll be late."
    "I'll have no time to get anything even if I forgot it."
    
    #From here on the player has to route the way to the first hallway in the school (Black and white one)
    #If the player goes back, or makes any wrong turns on the map instead of going directly to school, they become "late"
    #If the player does these things it should call a dialouge saying "Oh no I'm going to be late!!!" or something like that.
    #When the player arrives at the school the dialogue will show either "Yes! I made it on time!" or "Damn I was late because 
    #I watsed time going back or making wrong turns"
    
    #(Optional: if you feel like it, you could have two late states. Late = took one wrong turn. Very Late = Took more than 1 wrong turn. Final
    #Dialogue should also reflect this.)
    
    return
    
    
    
    

label activity_2:
    
    show bg classroom
    "Wow class was so boring today. Good thing it's lunch break now!"
    "I can do anything I want (Except leave the school of course.)"
    
    #Enable map, however leaving the school from the baseball is disabled. You can choose how to do this, either grey out the arrows, 
    #remove the arrow, or have a message pop up saying you an't leave the school when you click it. Your choice.
    
    #Lunch time is active for the duration of 10 "movements" movements being arrow clicks.
    #Player can click around the school and movement count goes down.
    #After 6 moves have been done (4 remaining) message should come up saying "Lunchtime is nearly over. I should head back to class or I'll be late."
    # After this message pops up going back to class concludes lunch (Even if there are still 3 more moves left)
    #Prior to this message going to class should just display something like "Why am I hanging around class, it's lunch time!"
    # If the player makes it back to calss before or on the 10th move they made it "In time"
    #Any later than that and they are late. A message should tell them they are late, when they finally get back to class the teacher yells.
    
    return
    