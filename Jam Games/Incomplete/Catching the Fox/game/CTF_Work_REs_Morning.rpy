# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label md1:
    
    si "Let's see what's on my itinerary for today..."
    
    ##Simone chibi at desk working, speech bubble "..."
    
    si "Oh, okay."
    
    si "I've got to email this agent asking for their client schedule so we can get that actress on board for the web commercial."
    
    si "Let me send that now!"
    
    show black with dissolve
    
    hide black with dissolve
    
    si "Oh, nice. They answered already."
    
    ##speech bubble, heart
    
    si "...And we're on board!"
    
    si "I'll send the contract to Solomon for him to look over now."
    
    return

label md2:
    
    $ randomnum = renpy.random.randint(1,6) # (randomize between 1 and 10)
    
    if randomnum==11:
        $ number = "forty"
        
    elif randomnum==12:
        $ number = "a hundred"
        
    elif randomnum==13:
        $ number = "twenty"
        
    elif randomnum==14:
        $ number = "eighty-five"
    
    elif randomnum==15:
        $ number = "thirty"
    
    elif randomnum==16:
        $ number = "sixty-seven or sixty-eight"
    
    "If I'm reading this right, they want me to email every single staff member in the financial department data spreadsheets about last month's distribution. {w}And..."
    
    si "There's over a hundred email addresses."
    
    #Working Simone chibi, speech bubble "..."
    
    "At least I can send the emails altogether, but typing in all of the address is going to be a pain."
    
    si "Sounds boring and tedious, but I'll get right on it."
    
    show black with dissolve
    
    hide black with dissolve
    
    si "Phew! I'm chugging on through them!"
    
    si "Let me just send the first wave..."
    
    #speech bubble, exclamation note
    
    "...!" with hpunch
    
    si "...You've {i}got{/i} to be kidding me."
    
    "My email browser froze?!"
    
    "But I'd already put in at least %(number)s of the addresses!"
    
    #speech bubble, scribble
    
    si "It didn't save my draft either... {w}Time to start over..."
    
    return

label md3:
    
    "Hm?"
    
    si "There's a post-it note on my desk."
    
    ##can I get this as a game asset?
    
    "{i}Simone, can you email these to the Art Department head for me?{/i}"
    
    "{i}I wrote the file names here, but I put them in the shared folder.{/i}"
    
    "{i}Thanks.{/i}"
    
    "{i}Fox{/i}"
    
    "Wait a second... The top is folded over. I straighten the post and a wave of alarm washes over me."
    
    ##Simone working chibi, speech bubble "!"
    
    si "It's got yesterday's date on it!"
    
    si "Oh, no!"
    
    show black with dissolve
    
    hide black with dissolve
    
    #speech bubble "..."
    
    si "At least I got it done, though..."
    
    return
    
label mk1:

    si "Maybe I'll go make some coffee..."
    
    scene black with dissolve
    
    scene o_kitchen with pixellate
    
    si "...!"
    
    ##Simone chibi with coffee pot, "!"
    
    si "Oh, there's coffee already here!"
    
    "I pour myself a cup."
    
    ##speech bubble: "!"
    
    si "Bleh!"
    
    si "That's not coffee, that's tea!"
    
    si "Who makes tea in a coffee pot?"
    
    "I don't want tea, but I guess I can't pour it out..."
    
    scene black with dissolve
    
    scene office cubicle with pixellate
    
    return
    
label mk2:
    
    si "I think I'll pop into the kitchen for some coffee."
    
    scene black with dissolve
    
    scene o_kitchen
    
    ##Simone chibi, coffee maker "!"
    
    jo "Simone! There you are!"
    
    si "Huh?"
    
    jo "Uhm, can you tell Solomon I'll be right back?"
    
    si "Sure, what's the problem?"
    
    jo "The coffeemaker's acting up, so I'm going to take it down to maintenance."
    
    jo "Again."
    
    ##speech bubble "..."
    
    si "..."
    
    ##speech bubble, scribble
    
    si "So much for a coffee..."
    
    scene black with dissolve
    
    scene office cubicle with pixellate
    
    return

label mk3:
    
    si "I feel like I need something hot to drink..."
    
    scene black with dissolve
    
    scene o_kitchen
    
    ##Simone chibi, coffee maker "!"
    
    "Oh, Joel's here."
    
    si "Good morning, Joel."
    
    "He jumps like I've caught him doing something suspicious."
    
    jo "Simone! Hi."
    
    si "Haha, hi. What're you doing?"
    
    jo "Oh, I'm making coffee. It just started though, so it'll be a little while until it's ready..."
    
    jo "Sorry about that."
    
    ##speech bubble "..."
    
    si "Hm..."
    
    ##speech bubble, "!"
    
    si "No problem! I'll just make some tea, Joel."
    
    "He looks relieved."
    
    jo "Okay, cool. Here's where we keep the tea."
    
    show black with dissolve
    
    hide black with dissolve
    
    si "Thanks, Joel! I'll be getting back to work now."
    
    jo "It's not a problem, Simone."
    
    scene black with dissolve
    
    scene office cubicle with dissolve
    
    "I take a sip of my fresh tea."
    
    ## speech bubbe, heart
    
    "Success!"
    
    return

label min1:
    
    $ randomnum = renpy.random.randint(1,2) # (randomize between 1 and 10)
    
    if randomnum==1:
        $ season = "Spring/Summer"
        
    elif randomnum==13:
        $ season = "Fall/Winter"
        
    $ randomnum = renpy.random.randint(3,8) # (randomize between 1 and 10)
    
    if randomnum==3:
        $ designer_name = "Encha"
        
    elif randomnum==4:
        $ designer_name = "Kenneth Kennedy"
        
    elif randomnum==5:
        $ designer_name = "Fucci"
        
    elif randomnum==6:
        $ designer_name = "Bobo Bhanel"
    
    elif randomnum==7:
        $ designer_name = "Saul Frenk"
    
    elif randomnum==8:
        $ designer_name = "Jark Makobs"
    
    si "Alright, I should do a little research. Let's see what's hot in mens' fashion."
    
    "I dip into the shared office folder."
    
    ##Simone working chibi, speech bubble "!"
    
    si "Oh?"
    
    "There's a video here..."
    
    si "%(season)s Season Collection by %(designer)s."
    
    "This is as good a place to start as any."
    
    show black with dissolve
    
    hide black with dissolve
    
    ##speech bubble "..."
    
    "..."
    
    si "Well. I won't say that was the {i}worst{/i} collection I've ever seen, but..."
    
    si "I... I'll just put these notes in the folder for now, then."
    
    return
    
label min2:
    
    "Hm, I wonder what's coming in for next season."
    
    ##Simone speech bubble "..."
    
    si "According to this blog, they're predicting that suede and silk will be the next big thing."
    
    "I could see it... they seem like they're popular enough fabrics."
    
    si "I'll take some notes of how many new things pop up using the two of them and see if I can get some kind of poll together."
    
    si "Ooh, these jackets are so nice though."
    
    si "I should get one for my brother..."
    
    "He's just a teenager, but he'd look great in this one..."
    
    #speech bubble, heart
    
    si "He'll be really happy if I get it for him. Let me just see how much it is..."
    
    return

label min3:
    
    si "Hmm... that's the fourth blog I've seen this designer mentioned..."
    
    si "Just who are these guys?"
    
    ##"..."
    
    si "Let me see if they have a website."
    
    si "..."
    
    ##"!"
    
    si "Wow! These are really different!"
    
    si "I think I'll forward their information to Solomon in case he'll want to contact them."
    
label ml1:

    "Hm, I was just thinking I needed a new jacket, too."
    
    ##Simone chibi, speech bubble "..."

    si "..."
    
    si "Okay, I don't know who's been designing jackets lately, but they need to consider finding a day job."
    
    si "And fast."
    
    ##speech bubble, scribble
    
    si "I didn't see a single design I liked..."
    
    return
    
label ml2:

    si "Ah, that reminds me--"
    
    "I still haven't picked a pair of shoes to go with my bridesmaid dress."
    
    si "I can look for some now and email them to Trina asking her opinion."
    
    ##Simone chibi working, "..."
    
    si "Let's see..."
    
    #speech bubble "!"
    
    si "Ooh, these are cute!"
    
    si "These aren't bad either!"
    
    si "But which one..."
    
    #speech bubble, heart
    
    si "I'll just send her both pairs and let her choose."
    
    return

label ml3:
    
    "I want a new bag for work."
    
    "The one I have now is good, but I want something I can also throw my shoes in when I ride the train home."
    
    "I can't believe I still haven't found time to buy one."
    
    ##Simone chibi "!"
    
    si "This one's not bad!"
    
    si "But this price..."
    
    #speech bubble, "..."
    
    si "I'll just bookmark it for now."
    
    return
    
label mim1:
    
    si "Let's see-- looking at the itinerary, the next meeting is supposed to be about the next three issues."
    
    si "What're some topics we could discuss?"
    
    #"..."
    
    si "Looking through the website, I've noticed there's a lot of articles on distinct types of ties-- I think it'd be a bad idea for us to do another article on them."
    
    si "How about... great go-to looks for the Spring/Summer season?"
    
    si "It's been a little warm lately, so that would probably work."

    return
    
label mim2:

    return
    
label mim3:
    
    return
    
label mh1:
    
    "Honesty: Peer review
    Intellect: Compile data reports about the latest trends.
    Imagination: Brainstorm ideas for the next meeting.
    Laziness: Online shop for shoes."
    

    return
    
label mh2:
    return
    
label mh3:
    return