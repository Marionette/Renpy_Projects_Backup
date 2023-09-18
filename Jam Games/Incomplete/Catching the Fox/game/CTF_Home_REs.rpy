# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label kk1:
    
    $ home = "no"
    
    si "Since I'm home early enough, I should make lunch for tomorrow."
    
    ##chibi CG of Simone cooking, speech bubble: music note
    
    si "..."
    
    ##speech bubble: exclamation point
    
    si "Ooh, I love this song! Let me just check on the sauce now..."
    
    si "Ack! {w}What did I put {i}in{/i} here?" with hpunch
    
    si "...Oh, no."
    
    si "This is sugar, not salt!"
    
    ##speech bubble: a scribble
    
    si "I hate when I get distracted while I'm cooking."
    
    si "I'll just... {w}order a pizza."
    
    return
    
label kk2:
    
    $ home = "lunch"
    
    si "Hm... didn't I go shopping the other day?"
    
    si "What should I pack in my lunch..."
    
    ##chibi CG of Simone cooking, speech bubble: music note
    
    si "..."
    
    ##speech bubble: exclamation point
    
    si "I can also add in leftovers from that soup I made. I'll just bring the rest in."
    
    ##speech bubble: heart
    
    si "Let me just slice up some bread to go with it!"
    
    return

label ki1:
    
    $ home = "no"
    
    si "I'm starving..."
    
    si "What should I make for dinner..."
    
    ##chibi CG of Simone cooking, speech bubble: music note
    
    si "Oh! I forgot I ordered out the other night."
    
    si "I can just heat that back up and call it a day."
    
    ##speech bubble: heart
    
    si "...Mhm, nothing like leftovers when you don't feel like cooking."
    
    return

label ki2:
    
    $ home = "no"
    
    si "I should save some money and make dinner!"
    
    ##chibi CG of Simone cooking, speech bubble: music note
    
    si "Wh-why is my fridge empty?"

    si "I just went shopping... oh."
    
    si "Three weeks ago."
    
    si "..."
    
    ##chibi CG Simone, speech bubble: scribble
    
    si "I'll just eat a bowl of cereal or oatmeal or something."
    
    si "It's better than nothing."
    
    return
    
label lrl1:
    
    $ home = "no"
    
    si "I don't feel like cooking tonight. I guess I can just order out."
    
    si "Hm... what should I have tonight?"
    
    show black with dissolve
    
    hide black with dissolve
    
    ##Chibi CG of Simone with a fork, determined expression
    
    si "Let's see how it tastes..."
    
    ##speech bubble: "..."
    
    si "Hm..."
    
    ##speech bubble: heart
    
    si "It's delcious!"
    
    return
    
label lrl2:
    
    $ home = "no"
    
    $ randomnum = renpy.random.randint(1,10) # (randomize between 1 and 10)
    
    if randomnum==1:
        $ thing= "Indian restaurant"
        
    elif randomnum==2:
        $ thing = "Chinese take-out"
        
    elif randomnum==3:
        $ thing = "pizzeria"
        
    elif randomnum==4:
        $ thing = "Thai restaurant"
    
    elif randomnum==5:
        $ thing = "donut burger place"
    
    elif randomnum==6:
        $ thing = "Jamaican corner store"
        
    elif randomnum==7:
        $ thing = "carry-out sushi"
        
    elif randomnum==8:
        $ thing = "Italian restaurant"
        
    elif randomnum==9:
        $ thing = "Vietnamese sandwich shop"
        
    elif randomnum==10:
        $ thing = "vegan stir-fry restaurant"
        
    si "Oh, there was that %(thing)s I wanted to try..."
    
    si "I'll order from them!"
    
    ##chibi CG with a fork, determined expression
    
    si "..."
    
    show black with dissolve
    
    hide black with dissolve
    
    si "Where are they...?"
    
    si "I'm really hungry..."
    
    z "Delivery!"
    
    ##speech bubble: "..."
    
    si "Finally!"
    
    ##speech bubble: scribble
    
    si "Why did it take so long though..."
    
    return

label lrh1:
    
    si "Oh! I should call home and see how my mom is doing."
    
    show black with dissolve
    
    hide black with dissolve
    
    si "I can't believe your sister-in-law's daughter ran away again..."
    
    ##chibi of Simone on the phone
    
    si "I know she wants to be a popstar but running away for the sixth time is a little dramatic. If you ask me, she should go into acting instead..."
    
    show black with dissolve
    
    hide black with dissolve
    
    ##speech bubble: scribble
    
    si "Geez, things like that remind me why I don't visit home more often. There's always so much drama."
    
    return

label lrh2:
    
    $ home = "no"
    
    "I wonder how my sister's doing."
    
    ##Simone on the phone, speech bubble: "..."
    
    si "..."
    
    si "She must be busy then. She usually picks up on the first ring..."
    
    si "Oh! I didn't realize it was this late."
    
    si "If that's that case, then she's putting the kids to bed."
    
    ##speech bubble: heart
    
    si "I'm sure she'll call me back when she's got time!"
    
    return
    
label bi1:
    
    $ home = "no"
    
    si "I should clean my room."
    
    si "Let me break out the vaccuum..."
    
    show black with dissolve
    
    hide black with dissolve
    
    si "Hm? What's this crackling sound?"
    
    ##Simone chibi with vaccuum, speech bubble: ?

    si "Oh! My favorite bracelet!"
    
    si "I've been looking for this!"
    
    ##speech bubble: heart
    
    si "I know exactly what I'm wearing tomorrow."
    
    return

label bi2:
    
    si "I'll just tidy up a little bit."
    
    ##Simone chibi with vacuum, speech bubble: "..."
    
    si "I didn't realize my room had gotten so messy..."
    
    si "I really need to be more organized in my personal life because that took ages."
    
    si "...Glad it's over with. Alright, I'll just be getting to bed now--"
    
    ##speech bubble: scribble
    
    si "I can't believe it's this late now..."
    
    return

label bd1:
    
    $ home = "work"
    
    si "Hm... I have time so I could always check my email and see if there's any work that needs to be done..."
    
    si "Let me get my laptop out."
    
    ##Simone chibi on laptop, speech bubble "..."
    
    si "...And sent!"
    
    si "Wow, it's a good thing I checked it. I didn't know Solomon needed a copy of that file, too."
    
    ##speech bubble: heart
    
    si "Glad I could be of assistance!"
    
    return
    
label bd2:
    
    $ home = "work"
    
    si "I'll just check my work email real quick."
    
    ##Simone chibi on laptop, speech bubble "..."
    
    si "What?"
    
    si "How could they mess it up so badly?!"
    
    si "Now I have to fix it, of course."
    
    si "We can't go to press with these kind of errors."
    
    ##speech bubble: scribble
    
    si "So much for getting to bed early..."
    
    return