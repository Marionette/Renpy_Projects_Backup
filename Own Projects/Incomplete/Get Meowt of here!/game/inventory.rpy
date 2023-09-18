
  #------------------------------------------------------
init python:
  import renpy.store as store
  import renpy.exports as renpy # we need this so Ren'Py properly handles rollback with classes

  #######################################################
  def debug_print(_msg):
    return # comment out to print debug messages
    with open("F:\[Projects]\RenpyGames\Get Meowt of here!\game\log.txt", "a") as myfile:
      myfile.write(_msg)
      myfile.write("\n")
  #######################################################

  
  #Test items
  item_unknown = ["???", "item unknown", "???"]
  item_globe = ["Globe", "item globe", "Its a globe."]
  item_clock = ["Clock", "item clock", "Its a clock."]
  item_fan = ["Fan", "item fan", "Its a fan."]
  item_book = ["BookL", "item book", "Its a book."]
  
  #Bedroom items
  item_candle = ["Candle", "item candle", "Its a candle."]
  item_candle_bedroom1 = ["candle_bedroom1", "item candle", "Its a candle from my bedroom."]
  item_lazerpen = ["LazerPen", "item lazerpen", "Its a lazer pen."]
  item_mousetoy = ["MouseToy", "item mousetoy", "Its a mouse shaped cat toy."]
  item_pencil = ["Pencil", "item pencil", "Its a pencil."]
  item_yarnball = ["YarnBall", "item yarnball", "Its a ball of yarn."]
  
  
  #Bedroom 2 items
  item_vpen = ["VPen", "item vpen", "Its a fancy pen."]
  item_incense = ["Incense", "item incense", "Its some incense."]
  item_candle_bedroom2 = ["candle_bedroom2", "item candle", "Its a candle from Veronicas bedroom."]
  
  #Bathroom 1 items
  item_token_silver = ["token_silver", "item token_silver", "Its a silver token."]
  item_jessicahairbrush = ["JessicaHairbrush", "item jessicahairbrush", "Its my hairbrush."]
  item_toiletbrush = ["ToiletBrush", "item toiletbrush", "Its a toilet brush."]
  item_plunger = ["Plunger", "item plunger", "its a plunger."]
  
  #Hallway items
  
  #Livingroom1 items
  #Livingroom2
  item_phone = ["Phone", "item phone", "Its my phone."]
  item_clawdiabrush = ["ClawdiaHairbrush", "item clawdiahairbrush", "Its clawdias brush."]
  item_candle_livingroom = ["candle_livingroom1", "item candle_livingroom", "Its a fancy pen."]
  
  item_change = ["Change", "item change", "Its some loose change."]
  item_buttons = ["Buttons", "item buttons", "Its some buttons."]
  item_pen = ["SofaPen", "item pen_sofa", "Its a simple pen."]
  item_token_bronze = ["token_bronze", "item token_bronze", "Its a bronze token."]
  
  
  #Kitchen items
  item_spoon = ["Spoon", "item spoon", "Its a spoon."]
  item_magnets = ["Magnets_loose", "item magnets", "Its a fridge magnet."]
  item_veronicaskeys = ["VeronicasKeys", "item veronicaskeys", "Its Veronicas keys."]
  item_token_gold = ["token_gold", "item token_gold", "Its a golden token."]
  
  
  #Basement1 items
  #Basement2
  item_candle_basement = ["candle_basement", "item candle", "Its a candle i found in the basement."]
  item_matches = ["Matches", "item matches", "Its a box of matches."]
  
  
  #Office items
  item_chalk = ["Chalk", "item chalk", "Its a piece of chalk."]
  item_office_pen = ["OfficePen", "item office_pen", "Its a standard pen."]
  
  #Bathroom 2 items
  item_token_wood = ["token_wood", "item token_wood", "Its a wooden token."]
  item_allergymeds = ["AllergyMeds", "item allergymeds", "Its Veronicas allergy meds."]
  item_veronicahairbrush = ["VeronicaHairbrush", "item veronicahairbrush", "Its veronicas hairbrush."]
  
  
  #Boilerroom items
  
  List_AllItems = [
                    item_candle,
                    item_candle_bedroom1,
                    item_lazerpen,
                    item_mousetoy,
                    item_pencil,
                    item_yarnball,
                    
                    item_vpen,
                    item_incense,
                    item_candle_bedroom2,
                    
                    item_token_silver,
                    item_jessicahairbrush,
                    item_toiletbrush,
                    item_plunger,
                    
                    item_phone,
                    item_clawdiabrush,
                    item_candle_livingroom,
                    #item_change,
                    #item_buttons,
                    item_pen,
                    item_token_bronze,
                    
                    item_spoon,
                    item_magnets,
                    item_veronicaskeys,
                    item_token_gold,
                    
                    item_candle_basement,
                    item_matches,
                    
                    item_chalk,
                    item_office_pen,
                    
                    item_token_wood,
                    item_allergymeds,
                    item_veronicahairbrush,
                    ]                  
  
  
  
  #store.inventory_hand = []
  #
  #store.inventory_basement1 = []
  #store.inventory_basement2 = []
  #store.inventory_bathroom1 = []
  #store.inventory_bathroom2 = []
  #store.inventory_bedroom1 = []
  #store.inventory_bedroom2 = []
  #store.inventory_boilerroom = []
  #store.inventory_hallway = []
  #store.inventory_kitchen = []
  #store.inventory_livingroom1 = []
  #store.inventory_livingroom2 = []
  #store.inventory_office = []
  
  room_unknown = ["???", "lbl_unknown", "???", inventory_hand ]  
  room_basement1 = ["basement1 ", "lbl_basement1", "This is the basement.", inventory_basement1 ]
  room_basement2 = ["basement2", "lbl_basement2", "This is the other side of the basement.", inventory_basement2 ]
  room_bathroom1 = ["bathroom1", "lbl_bathroom1", "This is the upstairs bathroom.", inventory_bathroom1 ]
  room_bathroom2 = ["bathroom2", "lbl_bathroom2", "This is the basement bathroom.", inventory_bathroom2 ]
  room_bedroom1 = ["bedroom1", "lbl_bedroom1", "This is my bedroom.", inventory_bedroom1 ]
  room_bedroom2 = ["bedroom2", "lbl_bedroom2", "This is Veronicas bedroom.", inventory_bedroom2 ]
  room_boilerroom = ["boilerroom", "lbl_boilerroom", "This is the basement boilerroom.", inventory_boilerroom ]
  room_hallway = ["hallway", "lbl_hallway", "This is the upstairs hallway.", inventory_hallway ]
  room_kitchen = ["kitchen", "lbl_kitchen", "This is the kitchen.", inventory_kitchen ]
  room_livingroom1 = ["livingroom1", "lbl_livingroom1", "This is the livingroom.", inventory_livingroom1 ]
  room_livingroom2 = ["livingroom2", "lbl_livingroom2", "This is the other side of the livingroom.", inventory_livingroom2 ]
  room_office = ["office", "lbl_office", "This is the upstairs office.", inventory_office ]
  
  List_AllRooms = [
                    room_unknown,
                    
                    room_basement1,
                    room_basement2,
                    room_bathroom1,
                    room_bathroom2,
                    room_bedroom1, 
                    room_bedroom2,
                    room_boilerroom,
                    room_hallway,
                    room_kitchen,
                    room_livingroom1,
                    room_livingroom2,
                    room_office,]
                    
  #current_room = room_bedroom1
  
  
  #------------------------------------------------------
  class Inventory(store.object):
    def __init__(self):
        self.List_AllItems = List_AllItems
        self.List_AllRooms = List_AllRooms
        self.inventory_hand = []
    def GetItemByName(self, _item): 
        Item = item_unknown
        for itm in self.List_AllItems:
          if (itm[0] == _item):
            Item = itm
        return Item

    def GetItemImage(self, _item): 
        Item = item_unknown[1]
        for itm in self.List_AllItems:
          if (itm[0] == _item):
            Item = itm[1]
        return Item

    def GetItemDescription(self, _item): 
        Item = item_unknown[2]
        for itm in self.List_AllItems:
          if (itm[0] == _item):
            Item = itm[2]
        return Item

    def IsItemCollectable(self, _item):
        Collectable = False
        for itm in self.List_AllItems:
          if (itm[0] == _item):
            Collectable = True
        return Collectable


    #------------------------------------------------------
    def GetRoomByName(self, _room): 
        Room = room_unknown
        for room in self.List_AllRooms:
          if (room[0] == _room):
            Room = room
        return Room

    def RoomContains(self, _item, _room):
        debug_print("RoomContains - " + str(_item) + ", " + str(_room))
        room = self.GetRoomByName(_room)  
        room_inventory = room[3]
        #debug_print("RoomContains inventory - " + str(room_inventory) + ", " + str(_room))
        for itm in room_inventory:
          #debug_print("RoomContains itm - " + str(itm) + ", " + str(_room))
          if (itm == _item):
            debug_print("RoomContains True - " + str(_item) + ", " + str(_room))
            return True
        debug_print("RoomContains False - " + str(_item) + ", " + str(_room))
        return False

    def AddItemToRoomInventory(self, _item, _room):
        debug_print("AddItemToRoomInventory - " + str(_item) + ", " + str(_room))
        if self.RoomContains(_item, _room):
          return
        room = self.GetRoomByName(_room)  
        room[3].append(_item)
        return

    def RemoveItemFromRoomInventory(self, _item, _room):
        debug_print("RemoveItemFromRoomInventory - " + str(_item) + ", " + str(_room) + ", " + str(self.GetRoomByName(_room)))
        if not self.RoomContains(_item, _room):
          return
        room = self.GetRoomByName(_room)  
        room[3].remove(_item)
        return

    #------------------------------------------------------

    def AddItemToHand(self, _item):
        debug_print("AddItemToHand - " + str(_item))
        if self.inventory_hand:
          self.AddItemToRoomInventory(self.inventory_hand[0], current_room[0])
          self.inventory_hand.remove(self.inventory_hand[0])

        if self.RoomContains(_item, current_room[0]):
          #debug_print("AddItemToHand RoomContains- " + str(_item))
          self.RemoveItemFromRoomInventory(_item, current_room[0])
        self.inventory_hand.append(_item)
        return

    def DropItemFromHand(self):
        debug_print("DropItemFromHand - " + str(self.inventory_hand[0]))    
        if self.inventory_hand:
          self.AddItemToRoomInventory(self.inventory_hand[0], current_room[0])
          self.inventory_hand.remove(self.inventory_hand[0])      
        return

    def EmptyInventories(self):
        debug_print("EmptyInventories ")
        self.EmptyHand()
        self.EmptyRooms()
        return 

    def EmptyHand(self):
        #debug_print("Hand - " + str(self.inventory_hand[0]) )
        if self.inventory_hand:
            self.inventory_hand.remove(self.inventory_hand[0])
        #debug_print("Hand - " + str(self.inventory_hand[0]) )
        return 

    def EmptyRooms(self):
        debug_print("EmptyRooms ")
        for room in self.List_AllRooms:
         room[2] = []
        return 

    def SetCurrentRoom(self, _roomName):
        global current_room
        current_room = self.GetRoomByName(_roomName)
        debug_print("SetCurrentRoom: " + str(_roomName) + " =>" + str(current_room))
          
        return

  #------------------------------------------------------