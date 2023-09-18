# Items


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

