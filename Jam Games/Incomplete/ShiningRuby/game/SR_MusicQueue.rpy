
  #------------------------------------------------------
init python:
  #------------------------------------------------------
  #Music functions
  #------------------------------------------------------
  def GetMusicByMood():
    return renpy.random.choice(List_Music)
        
  #------------------------------------------------------
  def QueueNextMusic():
    renpy.music.queue(GetMusicByMood())
    
    return
  #------------------------------------------------------
  def StartCallbackMusicQueue():
    renpy.music.set_queue_empty_callback(QueueNextMusic)
    
    return
  #------------------------------------------------------
  def EndCallbackMusicQueue():
    renpy.music.set_queue_empty_callback(EmptyFunction)
    renpy.music.stop()
    
    return
  #------------------------------------------------------
  #Empty function to pass to the callback (effectivly killing it)
  def EmptyFunction():
    return
  #------------------------------------------------------
  
  List_Music = ["sound/music/light/Aretes.mp3",
                      "sound/music/light/Daily Beetle.mp3",
                      "sound/music/light/Deliberate Thought.mp3",
                      "sound/music/light/Easy Lemon 30 second.mp3",
                      "sound/music/light/Fretless.mp3",
                      "sound/music/light/Groundwork.mp3"]