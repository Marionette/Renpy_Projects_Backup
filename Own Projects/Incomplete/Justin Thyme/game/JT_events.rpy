
    
  #------------------------------------------------------
init:
    $ event("cafe", "locationStr == 'Cafe'", event.only(), priority=200)
    $ event("cafe_bad", "locationStr == 'Cafe'", priority=210)
    
    #$ event("cut1", "act == 'cut'", event.choose_one('cut'), priority=200)
    #$ event("cut2", "act == 'cut'", event.choose_one('cut'), priority=200)
    #$ event("fly", "act == 'fly'", event.solo(), priority=200)
    #$ event("study", "act == 'study'", event.solo(), priority=200)
    #$ event("hang", "act == 'hang'", event.solo(), priority=200)
    #$ event("exercise", "act == 'exercise'", event.solo(), priority=200)    
    #$ event("play", "act == 'play'", event.solo(), priority=200)
    
    
    # This is an introduction event, that runs once when we first go
    # to class. 
    $ event("cafe_introduction", "locationStr == 'Cafe'", event.once(), event.only())
    
    
    $ event("cafe_closed", "locationStr == 'Cafe' and IsLocationOpen(locationStr)", event.only())
    
    
  #------------------------------------------------------
  #------------------------------------------------------
label cafe:

    "Im back at the cafe."

    return

# For test purposes only.
label cafe_bad:

    "You shouldn't be seeing this."

    "This is because class was declared with event.only(), which
     should suspend processing of further events."

    "This is really for testing purposes only."

    return
    
    
  #------------------------------------------------------
  #------------------------------------------------------
# Below here are special events that are triggered when certain
# conditions are true. 

label cafe_introduction:

    "Its a cafe."

    "This is my first time here."
    
    return

label cafe_closed:

    "Looks like the cafe is closed."
    
    return