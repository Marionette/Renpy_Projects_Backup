
init python:
  items = []
  seenItems = []
  
  def AddItem(_item):
    global items
    items.append(_item)
    
  def RemoveItem(_item):
    global items
    items = [item for item in items if item != _item]
    
  def HasItem(_item):    
    if _item in items:
      return True
    return False

  def SeenItem(_character, _item): 
    #Sets up a flag that the _item has been seen before by the _character
    global seenItems
    seenItems.append((_character, _item))
    
  def UnseenItemFlag(_character, _item): 
    #Return early if you dont have the item
    if not HasItem(_item):
      return False
    
    #Check if the item has already been seen
    for item in seenItems:
      if _character in item[0] and _item in item[1]:
        return False
        
    return True
  
init:
  # The script of the game goes in this file.

  # Declare characters used by this game. The color argument colorizes the
  # name of the character.

  define e = Character("Eileen")
  
  image frameAnim = Movie(channel="f", play="images/f_real.webm", mask="images/f_mask.webm") 
  image frameNotAnim = "images/frame.png" 
  
  image bg hallway1 = "images/map/bg-hallway01_for prog.png"
  
  $sound_tick = "sounds/117280__alexsani__front-tick.wav"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    show screen FrameScreen
    #show frameNotAnim onlayer frameLayer

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ckcheer

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    menu:
      "Map":
        jump lbl_mapTest
      "Timer":
        jump lbl_clockTest
      "Items":
        jump lbl_itemsTest
      
    
    
    # This ends the game.
    return

label lbl_clockTest:
    $StopTimer()
    show screen clock
    $ minutes = 540

    "It is already 9:00AM."
    "The game will end in 2 hours."
    
    "Ready?"
    $ResetTimer()
    "Start!"
    
    "Maybe you should wait?"
    
label lbl_timerwait:
    scene bg room with fade
    "..."
    $currenttime = GetTime()
    "The time is: [currenttime]"
    jump lbl_timerwait
    

    return

label lbl_itemsTest:
    
    e "lets get something."
    menu:
      "Pick up an apple" if HasItem("apple") == False:
        $AddItem("apple")
      "Drop an apple" if HasItem("apple"):
        $RemoveItem("apple")
      "Pick up an orange" if HasItem("orange") == False:
        $AddItem("orange")
      "Drop an orange" if HasItem("orange"):
        $RemoveItem("orange")
      "Nothing. Im done here" if HasItem("apple") and HasItem("orange"):
        jump lbl_clockTest
        
    if HasItem("apple"):
      e "I have an apple"
      
    if HasItem("orange"):
      e "I have an orange"
      
    if UnseenItemFlag('narrator', 'apple'):
      "Thats a good apple."
      $SeenItem('narrator', 'apple')  
      
    if UnseenItemFlag('narrator', 'orange'):
      "Thats a good orange."
      $SeenItem('narrator', 'orange')
      
    jump lbl_itemsTest
    
    return

label lbl_mapTest:
    "Lets check the hallway."
    jump lbl_mapStart_hallway1
    
    return