


# The game starts here.
label start:


    #Generate and modify Adults

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg marketplace_day

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show jonah happy

    # These display lines of dialogue.
    
    jon "Lets start trading"
    #call trading_start()
    jon "Trading complete"

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    e "Lets find something."
    #call lbl_itemPickingTest()
    
    e "Lets go somewhere."
    
    call lbl_mapTest
    
    
    e "Lets sell something."
    
    show jonah bored at left
    show mallory panic at right
    
    call screen sale_screen()
    
    e "Sold for [_return] gold!"
    
    e "All done."

    # This ends the game.

    return

    #------------------------------------------------------
    
label char_test:
    $AdultCount = 1
    $ADULT_LIST = GenerateCharacters(AdultCount)
    $cust = ADULT_LIST[0]
    $Customer_Name = ADULT_LIST[0].Name
    #customer "Hi Im the customer."
    
    customer "My name is [cust.Name]. I am a [cust.Gender] [cust.Type]. I have [cust.Funds] gold to spend. I like [cust.Likes] and i dislike [cust.Dislikes]."
    
    menu: 
      "Try again?"
      "Yes":
        jump char_test
      "No":
        pass
    #------------------------------------------------------
    

label lbl_mapTest:
    scene bg white
    "The point of this feature is to showcase a map style click-able interface for travelling between various locations."
    jump lbl_mapTest_City
    
label lbl_mapTest_City:

    scene bg marketplace_day
    show jonah happy at right
    e "Lets explore the city."
    call screen map_screen
    
    $res = _return
    
    "You picked [res]"
    
    #if (res=="Apartment"): 
    #    call lbl_Apartment    
    #if (res=="Disco"): 
    #    call lbl_Disco
    #if (res=="School"): 
    #    call lbl_School
    #if (res=="Shrine"): 
    #    call lbl_Shrine
    #if (res=="Station"): 
    #    call lbl_Station
    #if (res=="TVStation"): 
    #    call lbl_TVStation
        
    menu:
        e "Try somewhere else?"
        "Yes, I might've missed something!":
            jump lbl_mapTest_City
        "No, I think we are finished here.":
            pass
    
    e "I guess thats the end of that then."
    
    return

    #------------------------------------------------------

label lbl_story_chapter0:
    "..."
    
    #Jonah arrives in town
    #find cursed ring
    #set up stall
    #sell ring to Mallory  
    #celibrate in town - lots of booze
    #wake up hungover af
    #get accosted/Threatened by mallory and her Bodyguard (puts her fist through a wooden board with a crudely drawn picture of jonah on it)
    #Ordered to pay to un-curse the ring $1000
    #Need to sell stuff to make that money - One week time limit
    
    ## Shop minigame ##
    # Night trash diving
    # Day selling
    # Locations available - Peasents quarters / Forest?
    # Customers available - Commoners
    
    # Failure - Beat up / Game over
    
    # Success - Ring uncursed. Informed of an even greater debt.
    # Given a small stall in the marketplace to sell stuff
    