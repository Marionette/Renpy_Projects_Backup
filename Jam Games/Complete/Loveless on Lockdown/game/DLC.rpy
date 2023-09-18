label before_main_menu:

  "DLC Found. Would you like to play it?"
  menu:
    "Take me to the DLC":
      jump DLC_script
    "I want to play the main game.":
      return
      
      
      
label DLC_script:

  play music online_subdued fadein 2.0

  scene cg laptop_video with slow_dissolve

  show mara poker #as side image"

  "This is the DLC."
  
  "To celebrate 1000+ downloads."
  
  "Hope everyone enjoyed the game."
  
  return