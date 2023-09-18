init python:
  player_name = "MC"
  player_gender = "M"
  player_childStatus = "son"
  player_siblingStatus = "brother"
  player_identifierHECaps = "He"
  player_identifierHE = "he"
  player_identifierHIM = "him"
  player_identifierHIS = "his"
  

init:
    #Transitions
    $slowfade = Fade(0.5, 0.5, 0.5)
      
      
    # Declare characters used by this game.
    ####Character defines####
    define narrator = Character(None)
      
    define MC = Character("[player_name]")
    define Olin = Character('Olin')
    define Alarad = Character('Alarad')
    define Laurin = Character('Laurin')
    ######### CHARACTER DEFINES #############
    # Declare characters used by this game.
    define e = Character('Eileen', color="#c8ffc8")

  
  
    ######### CG/BG IMAGE DEFINES #############
    image bg black = Solid("#000000")    
    image bg white = Solid("#ffffff")    
    
    ## Locations ##
    #TradeOutpost - 1
    #VillageWest  - 2
    #Belgran      - 3
    #VillageEast  - 4
    #ForestFort   - 5
    #LyrTaer      - 6
    #YourHouse    - 7
    #SacredGrove  - 8
    image bg WorldMap = "images/ui/map/map2.jpg"
    image bg TradeOutpost = "images/bg/trade1.png"
    image bg VillageWest = "images/bg/village2.png"
    image bg Belgran = "images/bg/town2.png"
    image bg VillageEast = "images/bg/village1.png"
    image bg ForestFort = "images/bg/forestfort.png"
    image bg LyrTaer = "images/bg/town1.png"
    image bg YourHouse = "images/bg/house.jpg"
    image bg SacredGrove = "images/bg/sacred_grove.jpg"
    
    