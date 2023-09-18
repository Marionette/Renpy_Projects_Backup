init python:
    mp = MultiPersistent("rosaxcath4eva")
    defaultMemoryList = ["memory1.txt", "memory2.png" ,"memory3.ogg" ]
    newMemoryList = ["memory4.ogg", "memory5.txt", "memory6.png" ]
    

    #######################################################
    def debug_print(_msg):
      return # comment out to print debug messages
      with open(r"F:\[Projects]\RenpyGames\test\game\log.txt", "a") as myfile:
        myfile.write(_msg)
        myfile.write("\n")
    #######################################################
    
    def ensure_dir(file_path):
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

    def delete_memory(name):
    
        debug_print("deleting - " + str(name))
        import os
        try: os.remove(config.basedir + "/memory/" + name)
        except: debug_print("deletion failed")#                pass
        
    def delete_all_memories():
        for filename in os.listdir(config.basedir + "/memory/"):
          delete_memory(filename)
        
    def add_memory(name):
        #import os
        ensure_dir(config.basedir + "/memory/")
        try: renpy.file("../memory/"+ name)
        except: open(config.basedir + "/memory/"+name, "wb").write(renpy.file("/memories/"+name).read())
        
    def restore_all_memories():
        for name in defaultMemoryList:
          add_memory(name)
          
    
init python:

    class TrackCursor(renpy.Displayable):

        def __init__(self, child):

            super(TrackCursor, self).__init__()

            self.child = renpy.displayable(child)

            self.x = None
            self.y = None

        def render(self, width, height, st, at):

            rv = renpy.Render(width, height)

            if self.x is not None:
                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (self.x - cw / 2, self.y - ch / 2))

            return rv

        def event(self, ev, x, y, st):

            if (x != self.x) or (y != self.y):
                self.x = x
                self.y = y
                renpy.redraw(self, 0)

screen torch:
    add TrackCursor("images/torch.png")
            
            
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image bg room = "images/bg room.png"
image black = Solid("#000000")
image bg black = Solid("#000000")
image bg white = Solid("#FFFFFF")
image bg panorama = "images/DSC_MidwinterPano.jpg"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Hello, world."

    e "You've created a new Ren'Py game."
    

    
    menu:
      "Choose?"
      "Parallax test":
        jump lbl_parallax_test
      "Rhythm minigame":
        call lbl_minigame_rhythm from _call_lbl_minigame_rhythm
      "Option 3":
        pass
      "Memory Test":
        jump lbl_memoryTest
      "Panorama test":
        jump lbl_panorama_test
      "Torch test":
        jump lbl_torch_test
      "Skip":
        pass

    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    $HintsActive = True
    call lbl_testhintMenu from _call_lbl_testhintMenu

    $HintsActive = False
    call lbl_testhintMenu from _call_lbl_testhintMenu_1
    
    "End."
    # This ends the game.
    
label lbl_torch_test:
  show screen torch 
  jump lbl_panorama_test
    
label lbl_panorama_test:
  scene bg panorama:
      zoom 2.0
      yalign 0.5
      xpan 0
      #linear 0.1 xpan 60
      #pause 1.0
      #linear 0.1 xpan 120
      #pause 1.0
      #linear 0.1 xpan 180
      #pause 1.0
      #linear 0.1 xpan 240
      #pause 1.0
      #linear 0.1 xpan 300
      #pause 1.0
      #linear 0.1 xpan 360
      #pause 1.0
      linear 10.0 xpan 360
      repeat
  
  "testing panorama" 
  return
  
  
    
label lbl_multipersistant_test:

    # ...

    # Record the fact that the user beat part 1.

    $ mp.beat_part_1 = True
    $ mp.save()

    e "You beat part 1. See you in part 2!"

    return
    
label lbl_memoryTest:
  "testing memory..."
  $restore_all_memories()
  "memories restored."  
  $delete_memory(defaultMemoryList[0])
  "old memory [defaultMemoryList[0]] deleted."
  
  $add_memory(newMemoryList[0])
  "new memory [newMemoryList[0]] added"
  $add_memory(newMemoryList[1])
  "new memory [newMemoryList[1]] added"
  $add_memory(newMemoryList[2])
  "new memory [newMemoryList[2]] added"
  
  $delete_memory(defaultMemoryList[1])
  "memory [defaultMemoryList[1]] deleted."
  $delete_memory(defaultMemoryList[2])
  "memory [defaultMemoryList[2]] deleted."
  
  $delete_all_memories()
  "All memories deleted"
  
  "End Test."
  
  return


label lbl_testhintMenu:

  "Make a choice"
  $choice1 = ["Choice","Hint", "lbl_return"]
  $choice2 = ["Convince", "{color=#123456}Unlocks more choices{/color}", "lbl_convince"]
  $choice3 = ["Nevermind", "{color=#654321}Unlocks extra scene{/color}", "lbl_nevermind"]
  $choice4 = ["No hint Choice","", "lbl_return"]
  
  call HintMenu([choice1, choice2, choice3, choice4]) from _call_HintMenu
  jump expression _return
  
  jump lbl_return
  
label HintMenu(_choices):
  
  python:
    choiceCount = len(_choices)
    choices = []
    for option in _choices:
      hintChoice = option[0]
      if HintsActive and len(option[1]) > 0:
        hintChoice = hintChoice + " (" + option[1] + ")"
      menuOption = [hintChoice, option[2]]
      choices.append(menuOption)
  
  menu:
    "[choices[0][0]]":
      return choices[0][1]
    "[choices[1][0]]" if choiceCount > 1:
      return choices[1][1]
    "[choices[2][0]]" if choiceCount > 2:
      return choices[2][1]
    "[choices[3][0]]" if choiceCount > 3:
      return choices[3][1]
    "[choices[4][0]]" if choiceCount > 4:
      return choices[4][1]

  return ""
  
  
label lbl_return:
  return
  
label lbl_convince:
  "You chose to convince"
  return
  
label lbl_nevermind:
  "You changed your mind."
  return

