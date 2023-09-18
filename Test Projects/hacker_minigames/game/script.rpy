# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image bg black = Solid("#000000")  


# The game starts here.

init python:
  def GetHostName():
    import socket
    return socket.gethostname()
    
  def GetUsername():
    import os
    return os.getlogin( ) 


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene testbg

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    $ host = GetHostName()
    $ user = GetUsername()
    
    "So its [user] on [host] then."
    
    menu:
      "Hangman":
        call hangman_start
      "Mastermind":
        call mastermind_start
      "Filehack(incomplete)":
        call filehack_start

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
