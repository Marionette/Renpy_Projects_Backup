# The script of the game goes in this file.


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."
    
    call lbl_potion_test

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label lbl_potion_test:  

    menu:
      "Drinks menu style"
      "A - Menu style":
        jump lbl_potion_test_A
      "B - D&D Separated by Type":
        jump lbl_potion_test_B
      "C - D&D All Together":
        jump lbl_potion_test_C
    #call puzzle_start()
    
    "Now lets shake it!"
    
    show bartender_body
    show bartender_shaker at shakeit
    
    "Shake it!!"
    
    menu: 
        jc "Should i try again?"
        "Yes":
            jump lbl_potion_test
        "No":
            return

label lbl_potion_test_A:  
    $drink_ingredients = ["Nothing", "Nothing", "Nothing"]
    $drink_name = "Mystery Drink"

    show bartender_body
    show bartender_shaker 
    b "So what do you want to drink?"
    c "Gimme something spicy?"
    b "Hmm, I think a Fireball will do the trick."
    
    
    menu:
      "What kind of Spirits should I use?"
      "Vodka":
        $drink_ingredients[0] = "Vodka" 
      "Rum":
        $drink_ingredients[0] = "Rum" 
      "Just use Water idk":
        $drink_ingredients[0] = "Water" 
        
    b "So what brings a person like you do a place like this?"
    c "Oh, you know."
    b "I mean i don't, but ok."
    
    
    menu:
      "What kind of Sugars should I use?"
      "Raspberry":
        $drink_ingredients[1] = "Raspberry" 
      "Cinnamon":
        $drink_ingredients[1] = "Cinnamon" 
      "A Literal sugarcube i guess":
        $drink_ingredients[1] = "Sugar" 
        
    b "Got anything to sell? Human teeth maybe?"
    c "Is this that kind of place?"
    b "It could be, you just never know these days."
    
    
    menu:
      "What kind of Bitters should I use?"
      "Tabasco":
        $drink_ingredients[2] = "Tabasco" 
      "Lime":
        $drink_ingredients[2] = "Lime" 
      "Just be a real bitter person.":
        $drink_ingredients[2] = "Bad Attitude" 
        
    if drink_ingredients ==  ["Rum", "Cinnamon", "Tabasco"]:
      $drink_name = "Fireball"
    if drink_ingredients ==  ["Vodka", "Raspberry", "Lime"]:
      $drink_name = "Raspbery Lime Zinger"
    if drink_ingredients ==  ["Water", "Sugar", "Bad Attitude"]:
      $drink_name = "A Sour Disposition"
    
    b "Now lets shake it!"
    
    show bartender_body
    show bartender_shaker at shakeit
    
    b "Shake it!!"
    c "Having fun?"
    b "Always"
    show bartender_shaker at stopshaking
    
    b "Ok here you go, heres the drink you ordered. Its a {b}[drink_name]{/b}, made from [drink_ingredients[0]], [drink_ingredients[1]] and [drink_ingredients[2]]."

    c "*drinks*"
    if drink_name == "Fireball":
      c "WHOA, thats got a kick! I love it."
      b "Another satisfied customer."
    else:
      c "Not sure what i expected, but its definitely a drink of some sort."
      b "Another satisfied customer."
      c "I'm not sure satisfied is the right word..."
      "Bartender starts to aggressively clean a glass until the customer leaves."
    
    return
    