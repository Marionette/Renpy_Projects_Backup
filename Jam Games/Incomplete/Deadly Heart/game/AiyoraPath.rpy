label lbl_AiyoraPathStart:
    show Aiyora happy at left
    Aiyora "...Was that a dream?"
    jump lbl_AiyoraForest

label lbl_AiyoraForest:
    $ iMaikaAffection = 0
    $ iSorbenAffection = 0
    a "W-What is that noise?"
    "Sheepishly rubbing at your eyes you try to figure out what's making such a racket so early in th morning."
    "Unsurprisingly you find the two siblings arguing."
    hide Aiyora
    show Maika happy at left
    show Sorben happy at right
    s "I told you already! This isn't a game!"
    m "I know! But i can't help it if i'm bored!"
    s "I don't care if you're bored! We have a job to do!"
    m "I know! You don't have to yell!"
    a "Guys..."
    s "A-Aiyora?! We're so sorry that we woke you up."
    s "{size=-10}This was because you were being so loud.{/size}"
    m "Y-Yeah, sorry Ai-chan~"
    m "{size=-10}S-Shut up! You were being more loud than me!{/size}"
    hide Maika
    hide Sorben
    show Aiyora happy at left
    "Spying a peach tree your stomach growls in anticipation of something to eat."
    "You pick a peach and take a bite."
    a "Mmm. Delicious"
    "They still seem to be arguing. You wonder about what you can do to settle things"
    menu:
        a "How should i stop them from fighting?"
        "Scold them for fighting":
            a "That's quite enough out of you two!"
            $ iMaikaAffection -= 1
            $ iSorbenAffection += 1
            s "I'm sorry."
            m "I-Im sorry."
            "They both seem upset but you could swear you see a little twinkle of pride in Sorbens eye. Guess he approves of you putting your foot down."
            "Maika on the other hand has only tears in hers. Poor Maika"
        "Hold out the peach":
            a "How about you quit fighting and have some breakfast?"
            $ iMaikaAffection =+ 1
            $ iSorbenAffection =+ 1
            show Maika happy at right
            m "Yay~"
            hide Maika
            show Sorben happy at right
            s "Don't you know that fruit is a bad thing to have for breakfast? All that sugar isn't something a proper demon should be eating."
            a "Aww go on, you know you want to. I need you to cut it for me either way so you might as well have a piece"
            s "Well then i-i guess it can't be helped."
            "They both seem pretty happy as they wolf down the pieces of fruit after Sorben finishes cutting."
        
    hide Maika
    hide Sorben
    show Aiyora happy at left
    a "Maybe ill go for a stroll?"
    "The other two weren't paying attention and didn't notice you wander off"
    "After a few minutes you hear some hurried footsteps closing in behind you and turn to find a Angry Sorben glaring at you."
    show Sorben happy at right
    s "Where do you think youu're going without telling anyone?"
    a "Whats that?"
    "Deciding to have a little fun you point behind him and when he turns to look you skitter off into the forest"
    "It only takes about a minute for him to catch up again. This time he looks pretty annoyed though."
    s "This is no time for games!"
    menu:
        a "How should i respond?"
        "Apologise":
            $ iSorbenAffection += 1
            a "Ok, im sorry. That was pretty silly of me given the circumstance."
            s "Well as long as you understand that we get worried about you."
            a "Im sorry."
            "Hearing you apologise seems to have cheered him up."
        "Tell him to Lighten up":
            $ iSorbenAffection -= 1
            a "Take it easy, i was only playing around"
            s "Do you really think this is the time for games?!"
            "He starts to lecture you, he's obviously upset at you taking things so lightly."
    
    "You decide to return to Maika."
    hide Sorben
    show Maika happy at right
    m "Guys guys, i can hear water over there."
    a "Water?"
    m "Yeah lets go check it out."
    
    "The 3 of you head towards the sound of the water."
    
    m "My affection is at: [iMaikaAffection]"
    hide Maika
    show Sorben happy at right
    s "My affection is at: [iSorbenAffection]"
    
    
    jump lbl_GOOD_END