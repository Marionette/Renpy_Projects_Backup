# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Girl")
define a = Character("Veni", image="veni")
define long = Character("The Princess")


image bg beds = "images/twobeds.png"
image girl = im.FactorScale("images/neutral.png", 0.35)

#Invisible sprite to go with side images
image veni smile = "images/empty.png"
image side veni smile = im.FactorScale("images/normal_smile.png", 0.4)


image cg _1 = "images/twobeds.png"
image cg _2 = "images/twobeds.png"
image cg _3 = "images/twobeds.png"
image cg _4 = "images/twobeds.png"
image cg _5 = "images/twobeds.png"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show Solid("#000000")
    show bg beds
    show cg _2
    show cg _4

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show veni smile
    # These display lines of dialogue.

    a "You've created a new Ren'Py game."

    a "Once you add a story, pictures, and music, you can release it to the world!"
    
    show girl
    e "Once you add a story, pictures, and music, you can release it to the world!"

    long "Once you add a story, pictures, and music, you can release it to the world!"
    
    a "Rgerg th rthrt rt htfh rhrhfh  t rgerg th rthrt rt htfh rhrhfh  t rgerg th rthrt rt jkljkljlhtfh rhrhfh  tkljkljkl rgerg th rtjklhrt rt htfh rhrhfh  t rgerg th rjkljñkl."
    
    menu:
      "Option 1":
        pass
      "Rgerg th rthrt rt htfh rhrhfh  t rgerg th rthrt rt htfh rhrhfh":
        pass

    e "And again..."
    
    menu:
      "Menu Question"
      "Option 1":
        pass
      "Option 2":
        pass
      "Option 3":
        pass
      "Option 4":
        pass

    e "All done"
    # This ends the game.

    return
