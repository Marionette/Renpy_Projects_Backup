init python:
  ## Possible Jobs ##
  List_Jobs = ["Farmer",
                "Blacksmith",
                "Cook",
                "Tavern Staff",
                "Hunter",
                "Herbalist",
                "Teacher",
                "House Cleaner",
                "Stable Worker",
                "Tanner" ]
  
  List_Classes = ["Archery",
                  "Swordplay",
                  "Magic",
                  "Economics",
                  "Politics",
                  "Medicine",
                  "Husbandry",
                  "Cooking"]
                  
  List_Activities = [  
                      "Combat Classes - Melee", 
                      "Cooking Classes",
                      "Help your Father", 
                      "Help your Mother",
                      "Job - Squad 4",
                      "Job - Squad 7",
                      "Job",
                      "Magic Classes",
                      "Meditate","Have a drink",
                      "Music Classes",
                      "Pickpocket",
                      "Read",
                      "Shop", 
                      "Speech Classes",
                      "Stroll", 
                      "Study Magic",
                      "Thieving Classes",
                      "Thieving Job", 
                      "Train - Archery",
                      "Train - Melee",
                      "Train - Physique",
                                            ] 
                  
  #------------------------------------------------------
  ## Jobs available per location ##
  Jobs_TradeOutpost = [ "Blacksmith",
                        "Cook",
                        "Tavern Staff",
                        "Hunter",
                        "Stable Worker",]
                
  Jobs_VillageWest = ["Farmer",
                      "Blacksmith",
                      "Cook",
                      "Tavern Staff",
                      "Hunter",]
                
  Jobs_Belgran = ["Farmer",
                  "Blacksmith",
                  "Cook",
                  "Tavern Staff",
                  "Hunter",
                  "Herbalist",
                  "Teacher",
                  "House Cleaner",
                  "Stable Worker",
                  "Tanner" ]
                
  Jobs_VillageEast = ["Farmer",
                      "Cook",
                      "Tavern Staff",
                      "Stable Worker",
                      "Tanner" ]
                
  Jobs_ForestFort = [ "Blacksmith",
                      "Cook",
                      "Tavern Staff",
                      "Hunter",
                      "Herbalist",
                      "Teacher",
                      "House Cleaner",
                      "Stable Worker",
                      "Tanner" ]
                
  Jobs_LyrTaer = ["Blacksmith",
                  "Cook",
                  "Tavern Staff",
                  "Hunter",
                  "Herbalist",
                  "Teacher",
                  "House Cleaner",
                  "Stable Worker",
                  "Tanner" ]
                
  Jobs_YourHouse = [ ]
                
  Jobs_SacredGrove = [ ]
  #------------------------------------------------------
  Classes_TradeOutpost = ["Economics",
                          "Politics",]  
                          
  Classes_VillageWest = ["Medicine",
                          "Husbandry" ] 
                          
  Classes_Belgran = [ "Archery",
                      "Swordplay",
                      "Magic",
                      "Politics",
                      "Medicine" ] 
                      
  Classes_VillageEast = [ "Husbandry",
                          "Cooking" ]  
                          
  Classes_ForestFort = ["Archery",
                        "Swordplay",
                        "Magic", ] 
                        
  Classes_LyrTaer = [ ] 
                      
  Classes_YourHouse = [ "Cooking"]
  #------------------------------------------------------
  ## Activities available per location ##
  Activities_YourHouse = ["Help your Mother",
                          "Help your Father", ]
                
  Activities_SacredGrove = ["Meditate", ]
  
  
  Activities_LyrTaer_Palace = [ ] 
                      
  Activities_LyrTaer_Inn = [ "Have a drink",
                              "Job",
                              "Cooking Classes",
                              "Thieving Classes",
                              "Thieving Job", ]  
                      
  Activities_LyrTaer_Shop = [ "Shop", 
                           "Job", ]  
                      
  Activities_LyrTaer_MagesGuild = [ "Magic Classes",]  
                      
  Activities_LyrTaer_WarriorsGuild = [ "Combat Classes - Melee", 
                                        "Job"]  
                      
  Activities_LyrTaer_Library = [ "Read",
                                  "Job", 
                                  "Study Magic"]  
  
  Activities_LyrTaer_ArtSchool = [ "Speech Classes",
                                   "Music Classes"  ]    
  
  Activities_LyrTaer_Prison = []  
  
  Activities_LyrTaer_MainSquare = [ "Stroll", 
                                    "Pickpocket"] 
                                    
  Activities_LyrTaer = [  Activities_LyrTaer_Palace,
                          Activities_LyrTaer_Inn,
                          Activities_LyrTaer_Shop,
                          Activities_LyrTaer_MagesGuild,
                          Activities_LyrTaer_WarriorsGuild,
                          Activities_LyrTaer_Library,
                          Activities_LyrTaer_ArtSchool,
                          Activities_LyrTaer_Prison,
                          Activities_LyrTaer_MainSquare, ]
  
  Activities_ForestFort = [ "Job - Squad 4",
  "Job - Squad 7",
  "Train - Physique",
  "Train - Archery",
  "Train - Melee"] 
  
  
  Activities_TradeOutpost = []                 
  Activities_VillageWest  = []                
  Activities_Belgran      = []             
  Activities_VillageEast  = []  
  #------------------------------------------------------
                
    ## Locations ##
    #TradeOutpost - 1
    #VillageWest  - 2
    #Belgran      - 3
    #VillageEast  - 4
    #ForestFort   - 5
    #LyrTaer      - 6
    #YourHouse    - 7
  JobsAvailableAtLocations = [Jobs_TradeOutpost,                
                              Jobs_VillageWest,                
                              Jobs_Belgran,                 
                              Jobs_VillageEast,                
                              Jobs_ForestFort,                 
                              Jobs_LyrTaer,                
                              Jobs_YourHouse,
                              []]
                              
  ClassesAvailableAtLocations = [ Classes_TradeOutpost,                
                                  Classes_VillageWest,                
                                  Classes_Belgran,                 
                                  Classes_VillageEast,                
                                  Classes_ForestFort,                 
                                  Classes_LyrTaer,                
                                  Classes_YourHouse,
                              []]
                                  
  ActivitiesAvailableAtLocations = [Activities_TradeOutpost,                
                                    Activities_VillageWest,                
                                    Activities_Belgran,                 
                                    Activities_VillageEast,                
                                    Activities_ForestFort,                 
                                    Activities_LyrTaer,                
                                    Activities_YourHouse,                
                                    Activities_SacredGrove]
                                    
  def isJobAvailableAtLocation(_location, _job):
    available = False
    debug_print("isJobAvailableAtLocation - " + str(_location) + " -> " + str(_job))
    
    if _job in JobsAvailableAtLocations[_location-1]:
      available = True
      
    return False#available
    
  def isClassAvailableAtLocation(_location, _class):
    available = False
    debug_print("isJobAvailableAtLocation - " + str(_location) + " -> " + str(_class))
    
    if _class in ClassesAvailableAtLocations[_location-1]:
      available = True
      
    return False#available
    
  def isActivityAvailableAtLocation(_location, _activity):
    available = False
    debug_print("isActivityAvailableAtLocation - " + str(_location) + " -> " + str(_activity))
    
    if _activity in ActivitiesAvailableAtLocations[_location-1]:
      debug_print(str(_location) + " -> " + str(_activity) + " - Found")
      available = True
      
    return available
  #------------------------------------------------------
  