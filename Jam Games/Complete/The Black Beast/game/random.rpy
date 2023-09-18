# Random Dialogue##

# MOGU ######################################################
label mogu_random_set1:
    $ mogu_random = "mogu_random_" + str(renpy.random.randint(1, 10))
    call expression mogu_random from _call_expression_1  
    return
    
label mogu_random_1:
    # Convo 1:
    mg "The stars are really pretty."
    return
label mogu_random_2:
    # Convo 2:
    mg "Yesterday I went to the sky in my dream and then 
    there were pink clouds and purple seagulls falling from the sky."
    mg "And then I can see the bear painting."
    mg "Do you like bears?"
    mc "They're alright."
    "I like bears."
    return
    
label mogu_random_3:
    # Convo 3:
    mg "Here, I will give you this flower."
    mg "It's pretty and will always give you happiness."
    mc "Thank you."
    mg "Don't eat it even though it's hard. It will give you stomach ache."
    return

label mogu_random_4:
    # Convo 4:
    mg "I miss ice cream. We don't have ice cream here in the house anymore."
    mg "I can't even remember what ice cream is. I just know I like it."
    mc "Do you have a favorite flavor?"
    mg "Onion and chives!"
    return

label mogu_random_5:
    # Convo 5:
    mg "Big Brother is off travelling the world right now. He's a mighty 
    dragon and I hope I become like him in the future."
    return
    
label mogu_random_6:
    # Convo 6:
    mg "Edelia is really nice."
    mg "She gave me a little bird yesterday and 
    I ates it. It struggled a bit in my mouth but I chewed really hard 
    and soon it got yummy."
    return

label mogu_random_7:
    # Convo 7:
    mg "I think you have nice hair."
    mg "Mine  looks like a bird's nest but it reminds me of soup so I likes it. I likes yours too."
    return
label mogu_random_8:
    # Convo 8:
    mg "Don't stay too long in the dark. They say weird stuff."
    mg "Don't talk to them [mcname]."
    return
    
label mogu_random_9:
    # Convo 9:
    mg "Mary is really cute. *blushes*"
    return

label mogu_random_10:
    #Convo 20:
    mg "You look tasty."
    mg "That's a compliment."

    return
    
# BOOKS  ######################################################
label books_random_set:
    $ books_random = "books_random_" + str(renpy.random.randint(1, 5))
    call expression books_random from _call_expression_2  
    return

    
label books_random_1:
    # Convo 1:
    "I  opened a book." 
    nvl clear
    call alicebook from _call_alicebook 
    nvl clear
    $ readabook += 1
    $ readabookcount += 1
    return
label books_random_2:
    # Convo 2:
    "I  opened a book." 
    nvl clear
    call aboutstory from _call_aboutstory
    nvl clear
    $ readabook += 1
    $ readabookcount += 1
    return
    
label books_random_3:
    # Convo 3:
    "I  opened a book." 
    nvl clear
    call aboutcats from _call_aboutcats
    nvl clear
    $ readabook += 1
    $ readabookcount += 1
    return

label books_random_4:
    # Convo 4:
    "I  opened a book." 
    nvl clear
    call sleeping from _call_sleeping
    nvl clear
    $ readabook += 1
    $ readabookcount += 1
    return

label books_random_5:
    # Convo 5:
    "I  opened a book." 
    nvl clear
    call aboutbasement from _call_aboutbasement
    nvl clear
    $ readabook += 1
    $ readabookcount += 1
    return

# DEIS  ######################################################
label deisjoke_random_set:
    $ deisjoke_random = "deisjoke_random_" + str(renpy.random.randint(1, 3))
    call expression deisjoke_random from _call_expression_3  
    return

    
label deisjoke_random_1:
    # Convo 1:
    de "A crow and a pelican walk into a bar..."
    return
label deisjoke_random_2:
    # Convo 2:
    de "... So there was this little cuckoo bird..."
    return
label deisjoke_random_3:
    # Convo 3:
    de "...And then said, 'I'm not a dodo, I'm a masked booby!"
    return
    
    
    
label deisfacts_random_set:
    $ deisfacts_random = "deisfacts_random_" + str(renpy.random.randint(1, 5))
    call expression deisfacts_random from _call_expression_4  
    return

label deisfacts_random_1:
    # Convo 1:
    de "Did you know that there's a real bird called a Bananaquit?"
    return
label deisfacts_random_2:
    # Convo 2:
    de "A snail can sleep for three years without waking up!"
    de "Three years must be forever to snail life span."
    de "Now I'm imagining Sleeping Beauty as a snail."
    de "..."
    return
label deisfacts_random_3:
    # Convo 3:
    de "Did you know that if you shave a tiger, their skin underneath will still be striped?"
    de "I wouldn't recommend trying it, though."
    return
    
label deisfacts_random_4:
    de "If you ever get a goldfish, don't keep them in a dark room!"
    de "They'll turn pale as a ghost!"
    return
    
label deisfacts_random_5:
    de "Did you know cat urine glows under a black light? Ew."
    return
    

