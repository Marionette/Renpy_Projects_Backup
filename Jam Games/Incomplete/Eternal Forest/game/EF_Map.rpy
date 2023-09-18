init python:

  #######################################################
  def debug_print(_msg):
    return # comment out to print debug messages
    with open("E:\RenpyGames\Eternal Forest\game\log.txt", "a") as myfile:
      myfile.write(_msg)
      myfile.write("\n")
  #######################################################

  DestinationNumber = 0
  MapIcon_xOff = 34/2
  MapIcon_yOff = 57
  character_speed = 1
  current_location = [460, 660]
  current_destination = [460, 660]
  next_destination_index = 0
  next_destination = [460, 660]
  new_path = []
  current_path = []
  have_arrived = False
  Is_Moving = False
  TimeToDestination = 0

  TradeOutpost = [475, 137]
  VillageWest = [550, 448]
  Belgran = [908, 70] 
  VillageEast = [860, 417]
  ForestFort = [864, 550]
  LyrTaer = [742, 634]
  YourHouse = [460, 660]
  SacredGrove = [505, 655]
  
                    
  LocationList = [ TradeOutpost,
                   VillageWest,
                   Belgran,
                   VillageEast,
                   ForestFort,
                   LyrTaer,
                   YourHouse, 
                   SacredGrove]
                   
                    
  LocationLabelList = [ "lbl_locations_TradeOutpost",
                   "lbl_locations_VillageWest",
                   "lbl_locations_Belgran",
                   "lbl_locations_VillageEast",
                   "lbl_locations_ForestFort",
                   "lbl_locations_LyrTaer",
                   "lbl_locations_YourHouse",
                   "lbl_locations_SacredGrove"]
                   
  HouseToSacredGrove = [ YourHouse,
                    [490, 660],
                   SacredGrove]
                   
  SacredGroveToLyrTaer = [SacredGrove,
                    [504, 652],
                    [590, 601], 
                    [674, 566],
                    [685, 574], 
                    [680, 588],
                    [675, 617],
                    [697, 616],
                    [726, 614],
                    LyrTaer ]
                    
  LyrTaerToForestFort = [ LyrTaer,
                    [830,602],
                   ForestFort]
                   
  ForestFortToVillageEast = [ ForestFort,
                    [872,500],
                   VillageEast,]
                   
  VillageEastToVillageWest = [ VillageEast,
                    [706,430],
                   VillageWest,]
                   
  VillageEastToBelgran = [VillageEast,
                    [905,225],
                   Belgran,]
                   
  VillageWestToTradeOutpost = [ VillageWest,
                    [627,300],
                   TradeOutpost,]
                   
  BelgranToTradeOutpost = [ Belgran,
                    [704,80],
                   TradeOutpost,]  
                    
                    
  #------------------------------------------------------
  def GetMovementAmount( _end, _start):
    val = 0
    if HaveArrived():
      val = 0
    else:
      if (_end - _start) > 0:
        val = 1
      else:
        if (_end - _start) < -0:
          val = -1
        
    return val
  #------------------------------------------------------
    
  def HaveArrived():
    match = False
    if (((current_location[0] - next_destination[0] < character_speed) and (next_destination[0] - current_location[0] < character_speed)) and
        ((current_location[1] - next_destination[1] < character_speed) and (next_destination[1] - current_location[1] < character_speed))):
          match = True
    return match
  #------------------------------------------------------
    
  def HaveArrivedEnd():
    match = False
    if (((current_location[0] - current_destination[0] < character_speed) and (current_destination[0] - current_location[0] < character_speed)) and
        ((current_location[1] - current_destination[1] < character_speed) and (current_destination[1] - current_location[1] < character_speed))):
          match = True
    return match
  #------------------------------------------------------
  def getRoundedDays(_days):
    floatdays = _days
    intdays = int(_days + 0.5)
    #debug_print("getRoundedDays - " + str(floatdays) + ",  " + str(intdays) )
    return intdays
    
  def AddTimeElapsed(_remainingDuration, _pointsLeft):  
    if _pointsLeft == 1:
      JourneyDays(_remainingDuration)
    else:
      days = float(_remainingDuration/float(_pointsLeft))
      #debug_print("AddTimeElapsed - float days" + str(days))
      wholeDays = getRoundedDays(days)
      #debug_print("AddTimeElapsed - " + str(_remainingDuration) + ",  " + str(_pointsLeft) + " =  " + str(wholeDays) + ",  " + str(days))
         
      JourneyDays(int(wholeDays))
    #debug_print("AddTimeElapsed - " + str(pointsSinceLastUpdate))
    
  def JourneyDays(_wholeDays):
    global TimeToDestination
    AddDay(_wholeDays)
    TimeToDestination = TimeToDestination - _wholeDays    
    return
    
  def getDistanceBetween(_currentLocation, _destinationLocation):
    return 7
  #------------------------------------------------------
    
  def slide_function(trans, st, at):
      global current_location
      global next_destination_index
      global next_destination
      global have_arrived
      global Is_Moving
      if HaveArrived():
          if Is_Moving: #update time for movments. 
            #AddDay(1)#Need to calculate better
            AddTimeElapsed(TimeToDestination, len(current_path) - next_destination_index)
          if next_destination_index < len(current_path)-1:
            current_location = list(current_path[next_destination_index])
            next_destination_index += 1
            next_destination = list(current_path[next_destination_index])
          else:
            current_location = list(next_destination)
            #debug_print("slide_function - Arrived at -" + str(current_location) +  " - " + str(next_destination) )
            if Is_Moving:
              have_arrived = True
              Is_Moving = False
          trans.xpos = current_location[0]
          trans.ypos = current_location[1]
          return None
      else:
          if Is_Moving:
            trans.xpos = current_location[0] +( GetMovementAmount(next_destination[0] , current_location[0]))
            trans.ypos = current_location[1] +( GetMovementAmount(next_destination[1] , current_location[1]))
            current_location[0] = current_location[0] +( GetMovementAmount(next_destination[0] , current_location[0]))
            current_location[1] = current_location[1] +( GetMovementAmount(next_destination[1] , current_location[1]))
          return 0.01
  #------------------------------------------------------
                   
  def setLocationTo(_locationNumber):
    debug_print("setLocationTo - " + str(_locationNumber))
    global current_location
    global current_destination
    global next_destination
    global next_destination_index
    global have_arrived
    global Is_Moving
    global current_path
    global DestinationNumber
    global TimeToDestination
    
    currentLocationNumber = getLocationNumberFromPosition(current_location)
    if (currentLocationNumber == _locationNumber):
      have_arrived = True
      return #break out early if returning to the same location
      
    new_path = getMultiPath(currentLocationNumber, _locationNumber)
    #new_path = getPath(currentLocationNumber, _locationNumber)
    debug_print("new_path - " + str(new_path))
    if not new_path:
      return #break out early if no valid path found
      
    current_path = list(new_path)
    current_location = list(current_destination)    
    current_destination = list(current_path[len(current_path)-1])
    current_location = list(current_path[0])
    next_destination = list(current_path[1])
    next_destination_index = 1
    have_arrived = False
    Is_Moving = True
    DestinationNumber = _locationNumber 
    TimeToDestination = getDistanceBetween(currentLocationNumber, _locationNumber)
  #------------------------------------------------------
    
    
  def getLocationNumberFromPosition(_location):  
    number = 0
    for loc in LocationList:
      number+=1
      if ((loc[0] == _location[0]) and (loc[1] == _location[1])):
        debug_print("getLocationNumberFromPosition - " + str(_location) + " = " + str(number))
        return number
        
    debug_print("getLocationNumberFromPosition - " + str(_location) + " = Not Found")
    return -1
  #------------------------------------------------------    
  def getPathBetween(_startLocation, _destinationLocation):
  
    path = [_startLocation, _destinationLocation]
    
    if (_startLocation == 8):#SacredGrove
      if (_destinationLocation == 7):
        path = [_startLocation, _destinationLocation]
      if (_destinationLocation == 6):
        path = [_startLocation, _destinationLocation]
      if (_destinationLocation == 5):
        path = [_startLocation, 6, _destinationLocation]
    
    if (_startLocation == 7):#YourHouse
      if (_destinationLocation == 8):
        path = [_startLocation, _destinationLocation]
      if (_destinationLocation == 6):
        path = [_startLocation, 8, _destinationLocation]
      if (_destinationLocation == 5):
        path = [_startLocation, 8, 6, _destinationLocation]
    
    if (_startLocation == 6):#LyrTaer
      if (_destinationLocation == 8):
        path = [_startLocation, _destinationLocation]
      if (_destinationLocation == 7):
        path = [_startLocation, 8, _destinationLocation]
      if (_destinationLocation == 5):
        path = [_startLocation, _destinationLocation]
    
    if (_startLocation == 5):#ForestFort
      if (_destinationLocation == 8):
        path = [_startLocation, 6,  _destinationLocation]
      if (_destinationLocation == 7):
        path = [_startLocation, 6, 8, _destinationLocation]
      if (_destinationLocation == 6):
        path = [_startLocation, _destinationLocation]
        
    return path
    
  def getMultiPath(_startLocation, _destinationLocation):
    debug_print("getMultiPath - " + str(_startLocation) + " -> " + str(_destinationLocation))
    start = _startLocation
    end = _destinationLocation
    
    #while start != end:
    fullpath =[]  
    #path = [8,7,6,5,4,3,1]   
    #path = [1,2,3,4,5,6, 7, 8]   
    path = getPathBetween(_startLocation, _destinationLocation)
    #path = [8,7,6]    
    
    for index, location in enumerate(path, start=1):
      if index < len(path):
        fullpath += list(getPath(location, path[index]))
        
    debug_print("getMultiPath - " + str(fullpath))
    return fullpath
    
  def getPath(_currentLocation, _destinationLocation):
    
    debug_print("getPath - " + str(_currentLocation) + " -> " + str(_destinationLocation))
    ## Locations ##
    #TradeOutpost - 1
    #VillageWest  - 2
    #Belgran      - 3
    #VillageEast  - 4
    #ForestFort   - 5
    #LyrTaer      - 6
    #YourHouse    - 7
    #SacredGrove  - 8
    newPath = []
    
    if (_currentLocation == 1):#TradeOutpost - 1
      debug_print("From TradeOutpost " )
      if (_destinationLocation == 2):
        newPath = list(VillageWestToTradeOutpost)
        newPath.reverse()   
      if (_destinationLocation == 3):
        newPath = list(BelgranToTradeOutpost)
        newPath.reverse()   
        
    
    if (_currentLocation == 2):#VillageWest  - 2
      debug_print("From VillageWest " )
      if (_destinationLocation == 1):
        debug_print("To TradeOutpost " )
        newPath = list(VillageWestToTradeOutpost)
      if (_destinationLocation == 4):
        newPath = list(VillageEastToVillageWest)
        newPath.reverse()   
        
    
    if (_currentLocation == 3):#Belgran      - 3
      debug_print("From Belgran " )
      if (_destinationLocation == 1):
        debug_print("To TradeOutpost " )
        newPath = list(BelgranToTradeOutpost)
      if (_destinationLocation == 4):
        newPath = list(VillageEastToBelgran)
        newPath.reverse()   
        
    
    if (_currentLocation == 4):#VillageEast  - 4
      debug_print("From VillageEast " )
      if (_destinationLocation == 2):
        newPath = list(VillageEastToVillageWest)
      if (_destinationLocation == 3):
        newPath = list(VillageEastToBelgran)
      if (_destinationLocation == 5):
        newPath = list(ForestFortToVillageEast)
        newPath.reverse()   
        
    
    if (_currentLocation == 5):#ForestFort   - 5
      debug_print("From ForestFort " )
      if (_destinationLocation == 4):
        newPath = list(ForestFortToVillageEast)
      if (_destinationLocation == 6):
        newPath = list(LyrTaerToForestFort)
        newPath.reverse()   
        
    
    if (_currentLocation == 6):#LyrTaer      - 6
      debug_print("From LyrTaer " )
      if (_destinationLocation == 5):
        debug_print("To ForestFort " )
        newPath = list(LyrTaerToForestFort)
      if (_destinationLocation == 8):
        debug_print("To SacredGrove " )
        newPath = list(SacredGroveToLyrTaer)
        newPath.reverse()   
        
        
    if (_currentLocation == 7):#YourHouse    - 7
      debug_print("From YourHouse " )
      if (_destinationLocation == 8):
        debug_print("To SacredGrove " )
        newPath = list(HouseToSacredGrove)
        
        
    if (_currentLocation == 8):#SacredGFrove    - 8
      debug_print("From SacredGrove " )
      if (_destinationLocation == 6):
        debug_print("To LyrTaer " )
        newPath = list(SacredGroveToLyrTaer)
      if (_destinationLocation == 7):
        debug_print("To YourHouse " )
        newPath = list(HouseToSacredGrove)
        newPath.reverse()   
        
    return newPath
  #------------------------------------------------------
    
    
  def setStartLocation(_locationNumber):
    global current_location
    global have_arrived
    global Is_Moving
    current_location = list(current_path[0])
    have_arrived = False
    Is_Moving = False
  #------------------------------------------------------
    
  def getLocationIconXpos(_locationNumber):
    return LocationList[_locationNumber-1][0] - MapIcon_xOff
    
  #------------------------------------------------------
  def getLocationIconYpos(_locationNumber):
    return LocationList[_locationNumber-1][1] - MapIcon_yOff
    
  #------------------------------------------------------
init -2:
    transform q_move1:
        function slide_function
        pause 0.01
        repeat
        
screen Map_Screen:
  tag Map
  modal True
  $longtime = 1
  
  #stop the player icon from moving untill a location is chosen.  
  default Is_Moving = False
  
  add "images/ui/map/map2.jpg"
  #add "images/ui/map/map_roadPoints.png"
  
  ## Locations ##
  #TradeOutpost - 1
  #VillageWest  - 2
  #Belgran      - 3
  #VillageEast  - 4
  #ForestFort   - 5
  #LyrTaer      - 6
  #YourHouse    - 7
  #SacredGrove    - 8
  
  #imagebutton idle "images/ui/map/map_icon_1.png" focus_mask None xpos getLocationIconXpos(1) ypos getLocationIconYpos(1) action [Function(setLocationTo, 1)] 
  #imagebutton idle "images/ui/map/map_icon_2.png" focus_mask None xpos getLocationIconXpos(2) ypos getLocationIconYpos(2) action [Function(setLocationTo, 2)] 
  #imagebutton idle "images/ui/map/map_icon_3.png" focus_mask None xpos getLocationIconXpos(3) ypos getLocationIconYpos(3) action [Function(setLocationTo, 3)] 
  #imagebutton idle "images/ui/map/map_icon_4.png" focus_mask None xpos getLocationIconXpos(4) ypos getLocationIconYpos(4) action [Function(setLocationTo, 4)] 
  imagebutton idle "images/ui/map/map_icon_5.png" focus_mask None xpos getLocationIconXpos(5) ypos getLocationIconYpos(5) action [Function(setLocationTo, 5)] 
  imagebutton idle "images/ui/map/map_icon_6.png" focus_mask None xpos getLocationIconXpos(6) ypos getLocationIconYpos(6) action [Function(setLocationTo, 6)] 
  imagebutton idle "images/ui/map/map_icon_7.png" focus_mask None xpos getLocationIconXpos(7) ypos getLocationIconYpos(7) action [Function(setLocationTo, 7)] 
  imagebutton idle "images/ui/map/map_icon_7.png" focus_mask None xpos getLocationIconXpos(8) ypos getLocationIconYpos(8) action [Function(setLocationTo, 8)] 
  
  add "images/ui/map/map_icon_player1.png" xpos current_location[0]-MapIcon_xOff ypos current_location[1]-MapIcon_yOff at q_move1
  
  #close the screen when the movement is finished. #TODO -  Return a new label to jump to a new location on return
  timer 0.1 repeat True action If((have_arrived and not Is_Moving), true=Return(DestinationNumber) , false=SetVariable('time', longtime - 1))
    
  use DateDisplay_Screen
  
  
screen LyrTaerMap_Screen:
  tag Map
  modal True
  
  
  add "images/bg/town1.png"
  
  imagebutton idle "images/ui/map/map_icon_1.png" focus_mask None xpos getLocationIconXpos(1) ypos getLocationIconYpos(1) action Return("LyrTaer_Palace")
  imagebutton idle "images/ui/map/map_icon_2.png" focus_mask None xpos getLocationIconXpos(2) ypos getLocationIconYpos(2) action Return("LyrTaer_Inn")
  imagebutton idle "images/ui/map/map_icon_3.png" focus_mask None xpos getLocationIconXpos(3) ypos getLocationIconYpos(3) action Return("LyrTaer_Shop")
  imagebutton idle "images/ui/map/map_icon_1.png" focus_mask None xpos getLocationIconXpos(4) ypos getLocationIconYpos(1) action Return("LyrTaer_MagesGuild") 
  imagebutton idle "images/ui/map/map_icon_2.png" focus_mask None xpos getLocationIconXpos(5) ypos getLocationIconYpos(2) action Return("LyrTaer_WarriorsGuild") 
  imagebutton idle "images/ui/map/map_icon_3.png" focus_mask None xpos getLocationIconXpos(6) ypos getLocationIconYpos(3) action Return("LyrTaer_Library") 
  imagebutton idle "images/ui/map/map_icon_4.png" focus_mask None xpos getLocationIconXpos(7) ypos getLocationIconYpos(4) action Return("LyrTaer_ArtSchool") 
  imagebutton idle "images/ui/map/map_icon_5.png" focus_mask None xpos getLocationIconXpos(8) ypos getLocationIconYpos(5) action Return("LyrTaer_Prison") 
  imagebutton idle "images/ui/map/map_icon_5.png" focus_mask None xpos getLocationIconXpos(8) ypos getLocationIconYpos(5) action Return("LyrTaer_MainSquare") 
  

screen Town1Map_Screen:
  tag Map
  modal True
  
  
  add "images/bg/town1.png"
  
  imagebutton idle "images/ui/map/map_icon_1.png" focus_mask None xpos getLocationIconXpos(1) ypos getLocationIconYpos(1) action Return(1)
  imagebutton idle "images/ui/map/map_icon_2.png" focus_mask None xpos getLocationIconXpos(2) ypos getLocationIconYpos(2) action Return(2)
  imagebutton idle "images/ui/map/map_icon_3.png" focus_mask None xpos getLocationIconXpos(3) ypos getLocationIconYpos(3) action Return(3)
  
screen Town2Map_Screen:
  tag Map
  modal True
  
  
  add "images/bg/town2.png"
  
  imagebutton idle "images/ui/map/map_icon_1.png" focus_mask None xpos getLocationIconXpos(1) ypos getLocationIconYpos(1) action Return(1)
  imagebutton idle "images/ui/map/map_icon_2.png" focus_mask None xpos getLocationIconXpos(2) ypos getLocationIconYpos(2) action Return(2)
  imagebutton idle "images/ui/map/map_icon_3.png" focus_mask None xpos getLocationIconXpos(3) ypos getLocationIconYpos(3) action Return(3)
