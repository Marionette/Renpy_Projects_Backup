init python:
    import renpy.store as store
    import renpy.exports as renpy # we need this so Ren'Py properly handles rollback with classes
    
    
    #list of memories that the player starts with  
    defaultMemoryList = [ "memory1.txt", 
                          "memory2.png",
                          "memory3.ogg" ]
                          
    #list of new memories that can be added
    newMemoryList = [ "memory4.ogg",
                      "memory5.txt",
                      "memory6.png" ]
    
    #list to store any memories currently held by the player
    store.currentMemories = []
    

    #######################################################
    def debug_print(_msg):
      return # comment out to print debug messages
      with open(r"F:\[Projects]\RenpyGames\test\game\log.txt", "a") as myfile:
        myfile.write(_msg)
        myfile.write("\n")
    #######################################################
    
    def ensure_dir(file_path):
        #check if folder exists
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

    #-------------------------------------------------
    def add_current_memory(name):
      #add memory to current memory list
      if not name in store.currentMemories:
        store.currentMemories.append(name)
        
    def delete_current_memory(name):
      #remove memory from current memory list
      if name in store.currentMemories:
        store.currentMemories.remove(name)
    #-------------------------------------------------

    def delete_memory(name):
        #Remove file from memory directory
        debug_print("deleting - " + str(name))
        import os
        try: os.remove(config.basedir + "/memory/" + name)
        except: debug_print("deletion failed")# pass
        #update current list
        delete_current_memory(name)
        
    def delete_random_default_memory():
      defaultMemories = defaultMemoryList
      deleted = False
      while not deleted and len(defaultMemories) > 0:
        memory = renpy.random.choice(defaultMemories)
        
        if memory in store.currentMemories:      
          delete_memory(memory)
          deleted = True
        else:
          defaultMemories.remove(memory)
          
      if not deleted:
        debug_print("No memories deleted")
      else:
        return memory
      
    def delete_all_memories():
        #delete all memories in memory folder
        for filename in os.listdir(config.basedir + "/memory/"):
          delete_memory(filename)
        
    def add_memory(name):
        #Add file to memory directory
        ensure_dir(config.basedir + "/memory/")
        try: renpy.file("../memory/"+ name)
        except: open(config.basedir + "/memory/"+name, "wb").write(renpy.file("/memories/"+name).read())
        #update current list
        add_current_memory(name)
        
    def add_random_new_memory():
      newMemories = newMemoryList
      added = False
      while not added and len(newMemories) > 0:
        memory = renpy.random.choice(newMemories)
        
        if not memory in store.currentMemories:      
          add_memory(memory)
          added = True
        else:
          newMemories.remove(memory)
          
      if not added:
        debug_print("No memories added")
      else:
        return memory
        
    def restore_all_memories():
        #restore all memories in default memory list
        for name in defaultMemoryList:
          add_memory(name)
            
        
    def restore_current_memories():
        #restore all memories in current memory list - in case of game loaded etc
        for name in store.currentMemories:
          add_memory(name)
            
    #-------------------------------------------------
            
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg white = Solid("#FFFFFF")

    
label lbl_memoryTest:  
  
  $store.currentMemories=[]
  
  "testing memory..."
  $restore_all_memories()
  "default memories restored."  
  
  "currentMemories = [store.currentMemories]"
  
  $delete_memory(defaultMemoryList[0])
  "old memory [defaultMemoryList[0]] deleted."
  
  "currentMemories = [store.currentMemories]"
  
  $add_memory(newMemoryList[0])
  "new memory [newMemoryList[0]] added"
  $add_memory(newMemoryList[1])
  "new memory [newMemoryList[1]] added"
  $add_memory(newMemoryList[2])
  "new memory [newMemoryList[2]] added"
  
  "currentMemories = [store.currentMemories]"
  
  $delete_memory(defaultMemoryList[1])
  "memory [defaultMemoryList[1]] deleted."
  $delete_memory(defaultMemoryList[2])
  "memory [defaultMemoryList[2]] deleted." 
  
  "currentMemories = [store.currentMemories]"
  
  $delete_all_memories()
  "All memories deleted"
  
  
  "testing random memory..."
  $restore_all_memories()
  "default memories restored."  
  
  $deletedMemory = delete_random_default_memory()
  "Randomly chosen memory [deletedMemory] deleted." 
  $deletedMemory = delete_random_default_memory()
  "Randomly chosen memory [deletedMemory] deleted."  
  
  $addedMemory = add_random_new_memory()
  "Randomly chosen memory [addedMemory] added." 
  $addedMemory = add_random_new_memory()
  "Randomly chosen memory [addedMemory] added." 
  
  "currentMemories = [store.currentMemories]"
  
  $delete_all_memories()
  "All memories deleted"
  
  "doubles test..."
  $restore_all_memories()
  "default memories restored." 
  $delete_memory(defaultMemoryList[0])
  "old memory [defaultMemoryList[0]] deleted."
  $delete_memory(defaultMemoryList[0])
  "old memory [defaultMemoryList[0]] deleted."
  
  $add_memory(newMemoryList[0])
  "new memory [newMemoryList[0]] added"
  $add_memory(newMemoryList[0])
  "new memory [newMemoryList[0]] added"
  
  "currentMemories = [store.currentMemories]"
  
  $delete_all_memories()
  "All memories deleted"
  
  "End Test."
  
  return
  
#-------------------------------------------------
label after_load:
  #after_load label is called after any saves are loaded and can be used to reset memories
  
  #Delete all saved memories to clear the folder
  $delete_all_memories()
  #restore all current memories to return the folder to the correct state of the save
  $restore_current_memories()
  
  return