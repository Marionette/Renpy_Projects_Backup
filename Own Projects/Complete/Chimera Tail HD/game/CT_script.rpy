# The script of the game goes in this file.

# The game starts here.

#----------------------------------------------------------------------
#----------------------------------------------------------------------

label start_old:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "Eileen happy.png" to the images
    # directory.

    show Eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

#----------------------------------------------------------------------
#----------------------------------------------------------------------

# The game starts here.
label start:
    #play music "audio/Enchanted_Valley.ogg"
    $bLionHelped = False
    $bGoatHelped = False
    
    #jump lbl_testing
    jump lbl_introductions
    
    return
    
label lbl_testing:

    #dynamic "Im a dynamic character"    
    #$player_name = "A. Name"
    #dynamic "My name is [player_name]."
    #$player_name = "Not. A. Name"
    #dynamic "Now its [player_name]."


    show ChimeraBase
    show Girls at left
    "testing."
    show Girls at right
    "testing2."
    show ChimeraBase at left
    show sam happy at left
    show leo happy at left
    show gor happy at left
    
    "all happy up"
    
    
    show ChimeraBase
    "image ChimeraBase"
    hide sam
    show sam happy at left
    "image Sam happy"
    show sam love
    "image Sam love"
    show sam mad
    "image Sam mad"
    show sam excited
    "image Sam excited"
    show sam sad
    "image Sam sad"
    show sam embarrassed
    "image Sam embarrassed"
    show gor embarrassed
    "image Gor embarrassed"
    #show gor excited
    #"image Gor excited"
    hide gor
    show gor happy at left
    "image Gor happy"
    show gor love
    "image Gor love"
    show gor mad
    "image Gor mad"
    #show gor sad
    #"image Gor sad"
    hide leo
    show leo embarrassed at left
    "image Leo embarrassed"
    show leo excited
    "image Leo excited"
    show leo happy
    "image Leo happy"
    show leo love
    "image Leo love"
    show leo mad
    "image Leo mad"
    #show leo sad
    #"image Leo sad"
    
    scene bg forest day
    show ChimeraBase
    show sam happy
    show leo happy
    show gor happy
    "all happy"
    show ChimeraBase
    show sam happy
    show leo happy
    show gor happy
    
    "all happy up"
    
    show sam happy
    show leo sleep
    show gor sleep
    "asleep"
    hide sam 
    show sam mad
    "sam mad"
    
    scene bg forest day
    show ChimeraBase
    show sam embarrassed
    show leo embarrassed
    show gor embarrassed
    "everyone embarrassed"
    
    scene bg forest day
    
    show melissa happy
    " ... "
    show melissa sad
    " ... "
    show melissa neutral
    " ... "
    show melissa pissed
    " ... "
    show melissa mad
    " ... "
    show melissa content
    " ... "
    show melissa embarrassed
    " ... "
    show melissa love
    " ... "
    show melissa upset
    " ... "
    show helen happy at left
    " ... "
    show helen sad
    " ... "
    show helen neutral
    " ... "
    show helen pissed
    " ... "
    show helen mad
    " ... "
    show helen content
    " ... "
    show helen embarrassed
    " ... "
    show helen love
    " ... "
    show helen upset
    " ... "
    show pea happy at right
    " ... "
    show pea sad
    " ... "
    show pea neutral
    " ... "
    show pea pissed
    " ... "
    show pea mad
    " ... "
    show pea content
    " ... "
    show pea embarrassed
    " ... "
    show pea love
    " ... "
    show pea upset
    " ... "

    return
#----------------------------------------------------------------------
#----------------------------------------------------------------------
label lbl_introductions:
    scene bg forest day with fade
    play music music_park fadein 1.0
    define slow_dissolve = Dissolve(1.0)
    show ChimeraBase
    show leo sleep
    show gor sleep
    show sam happy
    
    s "So, What do you think of my plan?"
    s "..."
    s "Guys?"
    l "..."
    g "..."
    show sam mad
    s "Oh they're sleeping. Typical."
    
    show sam happy
    s "Well hello there. This is me. Samuel, or Sam if you'd prefer. I'm 1/3 of this particular chimera."
    show sam dull
    s "It's not easy being me. I mean when you think of a chimera, you always think of the lion head, or maybe even the goat head. Never the tail, I'm always an afterthought."
    show sam sad
    s "Heck if you had been shocked that I was even alive you wouldn't be the first."
    show sam happy
    s "But anyway. Enough moaning. What this snake is really interested in is..."
    show sam embarrassed
    s " Well its kind of embarrassing to say..."
    
    show gor happy
    g "..."
    s "...It's love. I'm in love. Yes, shocking I know. "
    show ChimeraBase at left
    show leo sleep at left
    show gor happy at left
    show sam love at left
    show photo medusa at right
    s "This is the object of my affections. "
    s "Her name is Melissa, she's basically the perfect girl."
    g "..."
    show sam excited
    s "Those beautiful eyes..."
    s "That cute smile..."
    s "Those smooth scales and that slithering hair..."
    show sam love
    s "Just thinking about her makes me go all fuzzy inside."
    show gor dull
    g "Who are you talking to?"
    hide photo
    show sam shock
    s "AHH! Y-You're awake."
    show sam embarrassed
    s "I-I didn't realize I was saying that all out loud."
    g "Yeeeeaaaaah."
    
    show sam dull
    s "Annnyway. How much of my plan do you remember hearing before falling asleep?"
    g "..."
    g "What plan?"
    show sam mad
    s "..."
    show sam pissed
    s "You know what? Never mind."
    hide leo
    show leo happy at left
    l "GUYS!"
    show gor happy
    show sam shock
    s "Waaah!"
    show leo skeptic
    show sam dull 
    l "Guys. I just had. The weirdest dream. Like seriously."
    hide leo
    show leo excited at left
    l "I mean there was this shark, only like it was huge. And we were like riding on its back."
    hide gor
    show gor skeptic at left
    g "We were riding a shark?"
    hide leo
    show leo excited at left
    l "Yeah, only like, it was flying. And that girl was there too."
    hide gor
    show gor skeptic at left
    g "Who?"
    show sam dull 
    s "Girl?"
    hide leo
    show leo embarrassed at left
    l "I er, never mind that's not important."
    show leo excited 
    l "Then the shark exploded and when I woke up in the dream but dream Sammy was droning on and on about something boring so I went back to sleep, in the dream."
    show leo dull
    show sam mad
    s "...I don't think that was the dream"
    hide leo
    show leo dull at left
    l "But the shark didn't come back so I woke up again, only for real this time."
    show sam happy
    s "That's so strange."
    show leo mad at left
    l "Yeah, I thought for sure it'd come back."
    show sam dull 
    s "Er that's not really what I meant..."
    hide gor
    show gor skeptic at left
    g "By the way guys, weren't we supposed to be somewhere by now?"
    hide leo
    show leo dull at left
    l "We were?"
    show sam shock
    s "Aww nuts. We need to hurry or they'll be sold out."
    
    
label lbl_intro_shopping:
    scene bg shop day with fade
    play music music_gameshop fadein 2.0
    #$ renpy.transition(slow_dissolve, layer="master")
    show ChimeraBase at left
    show leo dull at left
    show gor dull at left
    show sam happy at left
    s "Finally we're here!"
    l "..."
    g "..."
    s "We still need to hurry or the new Pocket Humans game will be sold out!"
    hide leo
    show leo mad at left
    l "It's easy...for you...you never...do any of...the running."
    g "..."
    show sam mad
    s "Hey! I Help us...er turn."
    
    s "Anyway lets get in there."
    "*BUMP*"
    h "HEY!"
    h "Watch where you're going, you big oaf!"
    hide gor
    show gor mad at left
    g "How about YOU wat..."
    
    show helen mad at right
    show gor skeptic
    g "..." 
    show gor embarrassed
    g "..I mean, Pardon us." 
    g "I hope you're not hurt."
    show helen embarrassed
    h "W-Well I guess I'm OK."
    
    hide sam
    show sam happy at left
    s "I haven't seen her around here before..."
    
    menu:
        "Should I talk to her?"
        "Are you new here?":
            jump lbl_shop_harpy
        "I don't have time for chit-chat!":
            hide helen
            jump lbl_shop_game
            
label lbl_shop_harpy:
    $bBakery = True
    show leo happy
    g "..."
    s "I haven't seen you around, are you new here?"
    show helen neutral
    h "What? I don't work here."
    show sam dull
    s "No I mean in the area."
    h "I don't work in the area either."
    s "I'm not asking about your job, I'm asking about you."
    show helen skeptic
    h "What about me?"
    g "..."
    s "Did you move here."
    h "To the store?"
    s "The area."
    show helen happy
    h "OOOOh, you mean did I move to town. "
    s "Yeah, that's what I meant."
    g "..."
    h "Then yeah, we moved here from back home."
    show sam happy
    s "We?"
    show helen dull
    h "Yeah me and my parents. They run the new bakery on the other side of town."
    hide leo
    show leo excited at left
    l "I LOVE CAKE!"
    show helen happy
    h "Whoa!"
    g "..."
    show sam dull
    s "Sorry about him. He's gets excited easily. Its true though, he really does. One time he ate so much all three of us got sick. "
    show helen embarrassed
    h "Haha you guys are strange."
    show sam embarrassed
    s "Well we try. "
    show helen happy
    h "Well I gotta get going. I should be back at the bakery by now. "
    show sam happy
    s "See you again sometime."
    h "Bye~"
    hide helen
    g "..."
    s "..."
    show sam skeptic
    s "Gor you're being awful quiet."
    hide gor
    show gor embarrassed at left
    g "I-It's n-nothing."
    hide sam
    show sam skeptic at left
    s "I'm sure it is."
    show sam shock
    s "Crap! I forgot the game."
    jump lbl_shop_nogame
    
label lbl_shop_nogame:
    #$ renpy.transition(slow_dissolve, layer="master")
    show ChimeraBase at left
    show leo dull at left
    show gor dull at left
    show sam happy at left
    #chat with harpy - get info 
    s "We want to buy a copy of Pocket Humans!"
    show shopkeep happy at right
    shopkeep "Sorry I just sold the last copy. And it'll probably be a while before we can get more stock."
    show ChimeraBase at left
    show leo pissed at left
    show gor pissed at left
    show sam sad at left
    s "Noooooooo..."
    l "...ooooooooo..."
    g "...ooooooooo"
    shopkeep "I still have a copy of the Digital Humans game though if you're interested."
    hide leo
    show leo skeptic at left
    l "Yeah, you still have it because nobody wants to play it. "
    hide gor
    show gor embarrassed at left
    g "Well actually..."
    show leo happy at left
    show gor happy at left
    hide sam
    show sam dull at left
    s "Well something is better than nothing I guess."
    shopkeep "Here you go. Enjoy."
    hide shopkeep
    jump lbl_shop_medusa
    
label lbl_shop_game:
    #rush into the store - get game
    s "We don't have time for chit-chat! Let's go!"
    #$ renpy.transition(slow_dissolve, layer="master")
    show ChimeraBase at left
    show leo dull at left
    show gor dull at left
    show sam happy at left
    s "We want to buy a copy of Pocket Humans!"
    show shopkeep happy at right
    shopkeep "Lucky you, here's the last copy."
    show ChimeraBase at left
    show leo excited at left
    show gor happy at left
    show sam excited at left
    s "AWESOME!"
    l "YES!"
    g "WHOOO!"
    s "We got it, and the last copy too. It's a good thing we ran here after all."
    hide leo
    show leo skeptic at left
    l "You mean good that we ran."
    hide sam
    show sam dull at left
    s "Don't sweat the small stuff."
    show leo excited 
    l "Dibs on the first go."
    hide sam
    show sam pissed at left
    s "...nuts. I wanted to go first."
    hide gor
    show gor happy at left
    g "Seconds!"
    hide sam
    show sam shock at left
    s "Aw for flips sakes."
    hide leo
    show leo skeptic at left
    l "Haha looks like Sammy takes up the rear as always. "
    hide sam
    show sam sad at left
    s "Life is so unfair sometimes."
    hide shopkeep
    jump lbl_shop_medusa

label lbl_shop_medusa:
    hide sam
    show sam happy at left
    s "Ok let's go home and try it out then."
    "*BUMP*"
    m "Oh my, I'm so sorry"
    s "No, it's our fa..."
    show melissa embarrassed at right
    hide sam
    show sam shock at left
    s "(OMG ITS HER! OHSHITSHITSHIT! WHAT DO I DO NOW?)"
    show melissa happy
    m "Oh it's you guys. Hi~"
    hide sam
    show sam embarrassed at left
    s "..."
    hide gor
    show gor happy at left
    g "Hello there."
    m "Oh you dropped something."
    m "Is it that something humans game everyone is raving about?"
    s "..."
    hide leo
    show leo excited at left
    l "We're just heading home to play it now!"
    show sam mad at left
    s "(Speak up dammit!)"
    m "Well have fun with that."
    show leo happy at left
    l "We will! See ya."
    hide gor
    show gor happy at left
    g "Goodbye."
    m "Bye~"
    
label lbl_shop_menu:
    show sam dull at left
    menu:
        "(Say something dammit!)"
        "I LOVE YOU MELISSA!":
            show sam mad at left
            s "(Yeah right. If I could just say that there would be no need for this game.)"
            jump lbl_shop_menu
        "Will you go out on a date with me sometime?":
            show sam mad at left
            s "(Yeah right. If I could just say that there would be no need for this game.)"
            jump lbl_shop_menu
        "...bye.":
            show sam sad at left
            s "(Sigh. What is wrong with me?)"
    
    #meet Medusa at the counter
    #get dragged away
    s "Let's just go home."
    hide leo
    show leo excited at left
    l "I can't wait to play~"
    hide gor
    show gor happy at left
    g "Yeah it's getting late, let's go."
    jump lbl_home
    
    #go to sleep
   
label lbl_home:
    scene bg home day with fade
    play music music_home fadein 1.0
    #$ renpy.transition(slow_dissolve, layer="master")
    #""
    show ChimeraBase at left
    show leo excited at left
    show gor happy at left
    show sam dull at left
    l "Time to play this~."
    hide gor
    show gor happy at left
    g "I'll just read a book then."
    hide sam
    show sam dull at left
    s "I think I'm just going to go to sleep now."
    hide leo
    show leo skeptic at left
    l "Haha, Sammy's mad that he couldn't talk to his giiiirrrrllllfriend~"
    hide gor
    show gor skeptic at left
    g "Again."
    hide sam
    show sam mad at left
    s "S-Shut up you two!"
    show sam dull 
    s "(But they hit the mark. Why am I fine in any other situation, but as soon as she appears it's like I lose the ability to speak.)"
    s "(I just never know what to say to her. Maybe I need to get these guys to Help me out.)"
    s "(I guess I'll ask in the morning...)"
    
    scene bg black with fade
    jump lbl_morning

#----------------------------------------------------------------------
#----------------------------------------------------------------------

label lbl_morning:
    #wake up
    "Beep beep beep"
    s "Mmmm its morning already?"
    scene bg home day with fade
    play music music_home fadein 1.0
    #$ renpy.transition(slow_dissolve, layer="master")
    show ChimeraBase at left
    show gor dull at left
    show leo sleep at left
    show sam dull at left
    l "Umm...no don't...bring her back..."
    s "Looks like Leo is talking in his sleep again. Wonder what he's dreaming about?"
    hide gor
    show gor dull at left
    g "Probably something weird like always."
    hide sam
    show sam happy at left
    s "Oh you're awake, Morning."
    hide gor
    show gor happy at left
    g "Good morning Sam."
    hide leo
    show leo mad at left
    l "Mumble...mumble...DAMN YOU SHARK!"
    s "..."
    hide gor
    show gor happy at left
    g "Good morning Leo."
    hide leo
    show leo mad at left
    l "Morning."
    hide sam
    show sam dull at left
    s "Bad dream?"
    hide leo
    show leo dull at left
    l "I dunno, it was weird."
    hide gor
    show gor dull at left
    g "All your dreams are weird though."
    hide leo
    show leo happy at left
    l "I guess you're right. Haha."
    
    #talk about plans
    hide sam
    show sam happy at left
    s "Anyway guys. I need your Help with something."
    hide gor
    show gor happy at left
    g "What is it?"
    hide sam
    show sam embarrassed at left
    s "Ok ok, you know Melissa."
    hide leo
    show leo skeptic at left
    l "Your giiiirrrrllllfriend?"
    hide sam
    show sam pissed at left
    s "..."
    hide sam
    show sam embarrassed at left
    s "I want to ask her out on a date."
    hide gor
    show gor dull at left
    g "And?"
    hide sam
    show sam dull at left
    s "Well you've seen how I get around her. "
    s "I need you guys to prompt me when I'm talking to her so I don't just sit there with my foot in my mouth the whole time."
    hide leo
    show leo skeptic at left
    l "You don't have feet though?"
    s "I mean I just need to guys to say something to me if I start to clam up while talking to her. To keep the conversation flowing until I'm able to ask her out."
    hide leo
    show leo happy at left
    l "Sounds easy, OK."
    hide gor
    show gor embarrassed at left
    g "Well actually..."
    
    hide sam
    show sam happy at left
    s "Gordon?"
    
    g "I wouldn't want to mess it up."
    hide sam
    show sam dull at left
    s "Mess it up? That's not like you."
    g "I don't know what's wrong with me, but ever since yesterday I can't think straight."
    hide sam
    show sam happy at left
    s "...yesterday?"
    hide gor
    show gor embarrassed at left
    g "That harpy we bumped into yesterday. I can't get her out of my mind."
    g "I've no idea why but suddenly I find that everything reminds me of her."
    
    hide sam
    show sam dull at left
    s "Hmmm..."
    hide sam
    show sam happy at left
    s "Ok, how about this. If I Help you with your problem then you're mind will be at ease and you'll be able to Help me, right?"
    hide gor
    show gor dull at left
    g "Well I guess that makes sense, but how?"
    s "I think I have an idea."
    
    hide leo
    show leo happy at left
    l "Oh now that you mention it."
    s "Hmm?"
    hide leo
    show leo skeptic at left
    l "I have something you can Help with too. If you want my Help that is."  
    hide sam
    show sam pissed at left  
    s "What but you already..."
    l "What was before you were offering Help as well."
    s "But..."
    l "I've already decided."
    hide sam
    show sam mad at left
    s "Aww for flips sakes."
    s "OK, then ill Help both of you."
    s "But then you guys have to Help me. Deal?"
    hide leo
    show leo happy at left
    l "Deal."
    hide gor
    show gor happy at left
    g "Deal."
    hide sam
    show sam happy at left
    s "Well then let's get started right away."
    jump lbl_MatchMaker_Choice
    
    #offer to Help the others with something in exchange for their Help
    #gor asks for Help with the harpy
    #leo asks for advice
    
label lbl_day_end:
    jump lbl_MatchMaker_Choice
    
    
label lbl_MatchMaker_Choice:
    scene bg home day # with fade
    play music music_home fadein 1.0
    ##$ renpy.transition(slow_dissolve, layer="master")
    show ChimeraBase at left
    show leo happy at left
    show gor happy at left
    show sam happy at left
    s "So what should I do now?"
    menu:
        "So what should I do now?"
        "Lets Help Leon!" if (bLionHelped == False):
            call lbl_MatchMaker_Lion from _call_lbl_MatchMaker_Lion
        "Lets Help Gordon!" if (bGoatHelped == False):
            call lbl_MatchMaker_Goat from _call_lbl_MatchMaker_Goat
        "I think its time to Help myself":
            jump lbl_MatchMaker_Snake
        
    jump lbl_MatchMaker_Choice
    
#----------------------------------------------------------------------
#----------------------------------------------------------------------

label lbl_MatchMaker_Lion:
    $bLionHelped = True
    $iPoints = 0
    s "I guess I'm Helping Leon then."
    
    #leo asks about girls
    s "So Leo, how can I Help you?"
    hide leo
    show leo embarrassed at left
    l "Well I guess what I really want is to ask you a few things."
    
    l "You know Melissa?"
    hide sam
    show sam embarrassed at left
    s "Y-Yeah?"
    hide leo
    show leo happy at left
    l "When you see her how does it make you feel?"
    menu:
        "How does seeing Melissa make me feel?"
        "Like my chest is going to explode":
            hide sam
            show sam embarrassed at left
            $iPoints +=1
        "Like I might throw up at any second":
            hide sam
            show sam embarrassed at left
            $iPoints +=1
        "Makes me want to punch her in the face!":
            hide sam
            show sam mad at left
            $iPoints +=0
        "I don't feel anything.":
            hide sam
            show sam dull at left
            $iPoints +=0
        
    hide leo
    show leo dull at left
    l "Hmm."
    
    l "What about when you think of you both together"
    menu:
        "The thought of me and Melissa together?"
        "I want to cry":
            hide sam
            show sam sad at left
            $iPoints +=0
        "BE STILL MY HEART!":
            hide sam
            show sam embarrassed at left
            $iPoints +=1
        "No reaction.":
            hide sam
            show sam dull at left
            $iPoints +=0
        
    l "Hmm, I see."
    s "Why do you ask?"
    
    l "Wait, one more question."
    l "When you think about Melissa and the Future what comes to mind most often?"
    
    menu:
        "What comes to mind when I think of Melissa and the future"
        "How many others would be in my harem by then!":
            hide sam
            show sam excited at left
            $iPoints +=0
            l "What's a harem?"
            g "Y-You don't need to know that Leo."
        "How our wedding will be!":
            hide sam
            show sam embarrassed at left
            $iPoints +=1
        "Which other girl ill have at that point!":
            hide sam
            show sam skeptic at left
            $iPoints +=0
        "What our kids will look like!":
            hide sam
            show sam embarrassed at left
            $iPoints +=1
        
    
    hide leo
    show leo dull at left
    l "OK, I think that's enough."
    hide sam
    show sam dull at left
    s "So are you going to explain what the questions were for?"
    s "I thought you wanted me to Help you."
    
    l "I just wanted to see if what I was feeling was the same as what you are"
    s "And is it?"
    if (iPoints == 3):
        hide leo
        show leo excited at left
        l "Yes. It's a perfect match!"
    if (iPoints == 2):
        hide leo
        show leo happy at left
        l "Eh... close enough."
    if (iPoints < 2):
        hide leo
        show leo dull at left
        l "Nah, seems like its something different."
        jump lbl_Lion_noMatch
    jump lbl_Lion_Match    
        
    
label lbl_Lion_noMatch:
    s "Will I still be able to Help?"
    hide leo
    show leo dull at left
    l "Nah it's ok, you've Helped enough, I know what I have is something different so I'll just deal with it on my own at some point."
    jump lbl_day_end
    
label lbl_Lion_Match:
    #leo asks about asking out on a date
    hide sam
    show sam happy at left
    s "So what now?"
    hide leo
    show leo happy at left
    l "Ok, now for the bonus question~"
    hide sam
    show sam skeptic at left
    s "More questions?"
    l "This is the last one for reals."
    s "Ok, hit me."
    hide leo
    show leo embarrassed at left
    l "Ok, when you see Melissa what is it you want to ask her and why?"
    
label lbl_Lion_Match_menu:
    show gor happy at left
    show leo embarrassed at left
    show sam happy at left
    menu:
        "What is it I want to ask Melissa?"
        "Will you lend me some money?":
            hide sam
            show sam skeptic at left
            s "You know because I'm broke."
            hide gor
            show gor pissed at left
            g "Come on Sam, take this seriously."
            jump lbl_Lion_Match_menu
        "Will you marry me?!":
            $bMarrage = True
            hide sam
            show sam embarrassed at left
            s "So we can spend the rest of our lives together."
        "Will you go out on a date with me?":
            hide sam
            show sam embarrassed at left
            s "So we can get to know one another better."
       
    #Leo asks if you'll back him up
    show gor happy at left
    hide leo
    show leo happy at left
    l "OK I think I have enough information. Thanks, guys."
    show sam happy at left
    s "No problem."
    s "So are you going to tell us who it is you fancy?"
    
    l "You'll find out when we get there."
    hide sam
    show sam dull at left
    s "Gor, do you know who it is?"
    hide gor
    show gor skeptic at left
    g "I think I have a fair idea."
    hide sam
    show sam shock at left
    s "How come I never noticed anything before?"
    hide gor
    show gor dull at left
    g "Probably because all you ever think about is that Medusa."
    hide sam
    show sam dull at left
    s "...oh. (I guess its true, I'm always so wrapped up in my own problems that I never really think about theirs.) "
    hide gor
    show gor happy at left
    g "Ha Ha, don't worry about it. I think you've Helped him out considerably with this."
    g "He's never been the sharpest claw in the paw, after all, so he needs a little push every now and then."
    g "Anyway, you'll see one way or another soon enough."
    
label lbl_Lion_Date:
    $iPoints = 3
    scene bg street day with fade
    play music music_park fadein 1.0
    #$ renpy.transition(slow_dissolve, layer="master")
    show ChimeraBase at left
    show leo happy at left
    show gor happy at left
    show sam happy at left
    
    #leo asks Persephone
    show pea happy at right
    p "Oh Hello there guys, heading out?"
    s "Oh hi Persephone. "
    s "(Persephone is our neighbor, she's been around here almost as long as we have. Which is strange considering that she's a Human. They don't often settle near monsters like us.)"
    g "Hello there."
    show pea content
    p "Oh yeah Leo. I got something for you."
    hide leo
    show leo excited at left
    l "A fish?"
    l "Awesome!"
    p "Who's a good kitty?"
    s "(Is she rubbing his chin? What a strange person.)"
    hide leo
    show leo dull at left
    l "Prrrr. No, wait."
    hide leo
    show leo embarrassed at left
    l "Persephone. There's something I want to ask you."
    s "(Wait, it's her?!)"
    show pea happy
    p "Ask me? What is it?"
    
    hide leo
    show leo embarrassed at left
    l "Persephone..."
    
    if (bMarrage == True):
        hide leo
        show leo excited at left
        l "Will you marry me?"
        hide sam
        show sam shock at left
        s "W-W-W-WHAT?!"
        hide gor
        show gor skeptic at left
        g "..."
        hide sam
        show sam shock at left
        s "T-That's not what I meant when I..."
        
    if (bMarrage == False):
        hide leo
        show leo excited at left
        l "Will you go out on a date with me?"
    
    hide sam
    show sam skeptic at left
    s "So that's why you were asking."
    s "You had feelings for Persephone but weren't sure what they were or what to do about them."
    
    hide gor
    show gor skeptic at left
    g "Well for now let's see how this pans out."
    
    #Persephone agrees
    show pea embarrassed
    p "Hmm..."
    hide leo
    show leo embarrassed at left
    l "..."
    hide gor
    show gor skeptic at left
    g "..."
    hide sam
    show sam skeptic at left
    s "..."
    show pea content
    p "...OK~"
    
    hide sam
    show sam shock at left
    s "W-What?!"
    hide leo
    show leo excited at left
    l "She said yes!"
    hide gor
    show gor happy at left
    g "Good for you Leo."
    
    if (bMarrage == True):
        show pea embarrassed
        p "But let's start with a date first, OK?"
        hide leo
        show leo happy at left
        l "Okay~"
    
    hide sam
    show sam happy at left
    s "Well that was easy. I guess this like this happen too. Maybe I shouldn't be so nervous about asking Melissa?"
    #cheers . ... but wait
    #Persephone gives a condition
    show pea neutral
    p "But, there is one small thing..."
    l "What is it?"
    show pea skeptic
    p "You have to convince my father to allow it."
    
    # per says they have to convince her father to allow it
    show leo shock
    show sam shock
    hide gor
    show gor shock at left
    g "Y-Your father?"
    hide leo
    show leo shock at left
    l "Y-You mean the big scary guy who lives in the same house as you?"
    s "(The reason you don't see many humans near monsters is that they fear us. But not this one. They say wrestled a Minotaur with his bare hands!)"
    show pea upset
    p "Yes, unfortunately, he's very protective and won't allow me to do anything without his permission."
    show gor happy at left
    hide sam
    show sam dull at left
    s "And you just listen to him?"
    show pea embarrassed
    p "Its a little stifling but I know he does it because he's worried about me, and I love him so its only right that I at least try to get his blessing."
    
    show pea sad
    p "U-Unless you have changed your mind about us..."
    show leo dull
    l "N-No. O-Of course not. I-I'll convince him!"
    show pea content
    p "Perfect~ I'll go get him now, he's in the house."
    hide pea
    show leo shock
    l "W-What?! R-Right now?"
    
    #per says he's on his way
    show leo dull
    l "What should I do?"
    menu:
        "What should Leo do?"
        "Man up Leo, its now or never!":
            jump lbl_Lion_Fight
        "He who runs away lives to fight another day.":
            jump lbl_Lion_Run
        
label lbl_Lion_Run:
    show ChimeraBase at left
    show gor dull at left
    show sam dull at left
    hide leo
    show leo dull at left
    l "You're right Sammy."
    l "I-I'll come back when I'm more prepared."
    hide sam
    show sam dull at left
    s "Yeah lets get out of here before we get killed."
    jump lbl_MatchMaker_Lion_End

label lbl_Lion_Fight:
    show ChimeraBase at left
    show gor dull at left
    show sam dull at left
    hide leo
    show leo dull at left
    l "I-I guess you're right. If I want this I have to face the music."
    hide gor
    show gor dull at left
    g "Well said."
    hide sam
    show sam skeptic at left
    s "(At least if we die we'll die together.)"
    show pea content at right
    p "Hi guys. He's on his way out. Said he had to get his Helmet or something."
    show leo shock at left
    show gor shock at left
    hide sam
    show sam shock at left
    s "Ohshi.."
    hide gor
    show gor shock at left
    g "Preparing for a fight?"
    hide leo
    show leo shock at left
    l "W-What should I do?"
    
    #choice -just be yourself Leo
    $iOption=0
    menu:
        "What should Leo do?"
        "Just agree with whatever he says.":
            $iOption=1
        "Just act tough.":
            $iOption=2
        "Just be yourself.":
            $iOption=3
        
    #meet father
    play music music_fight fadein 1.0
    f "Ahem!"
    hide pea
    show pea happy:
      xalign 0.8
      yalign 1.0
    show father mad at right
    f "So which one is it?"
    show pea embarrassed
    p "This one father"
    #greetings
    show gor dull at left
    show sam dull at left
    hide leo
    show leo embarrassed at left
    l "Y-Yeah, it's me. Hello there."
    
    #he doesn't like Leo
    f "I don't like him."
    show gor shock at left
    show sam shock at left
    hide leo
    show leo shock at left
    s "*Gulp*"
    
    #perservere
    if (iOption==1):
        $iPoints+=1
        show gor dull at left
        show sam dull at left
        hide leo
        show leo happy at left
        l "Yes sir, I agree!"
        hide sam
        show sam shock at left
        s "(W-What is he saying?!)"
        f "You...You agree? You mean you don't like me either?"
        hide leo
        show leo happy at left
        l "Yes sir!"
        f "Heh, well at least he's got some balls."
    if (iOption==2):
        show gor dull at left
        show sam dull at left
        hide leo
        show leo mad at left
        l "Tch, well I don't like your face."
        hide sam
        show sam shock at left
        s "(W-What is he saying?!)"
        f "You really like this Jerk, Pea dear?"
        hide pea
        show pea sad:
          xalign 0.8
          yalign 1.0
        p "H-He's not normally like this I don't know what's going on."
        hide leo
        show leo shock at left
        l "Er Well I..."
    if (iOption==3):
        $iPoints+=2
        show gor dull at left
        show sam dull at left
        hide leo
        show leo pissed at left
        l "But you don't even know me yet!"
        hide sam
        show sam shock at left
        s "(W-What is he saying?!)"
        f "What did you say?"
        hide leo
        show leo embarrassed at left
        l "I-I said you should get to know me better before you decide you don't like me."
        hide pea
        show pea skeptic:
          xalign 0.8
          yalign 1.0
        p "H-He's right father!"
        hide father
        show father mad at right
        f "Quiet. This is between the two of us."
        
    #still doesn't
    #dont give up
    #he insults
    #choice -ignore it - wimp
    #choice -stand up to him - manly
    hide pea
    show pea sad at right
    hide father
    show father mad:
      xalign 0.8
      yalign 1.0
    f "Ok, I'm going to cut to the chase here."
    f "I don't like you and I won't have my daughter taken away from me by some freakish cat with other stupid animals stuck on it."
    show gor shock at left
    show sam shock at left
    hide leo
    show leo shock at left
    menu:
        "That was pretty harsh."
        "Are you going to stand for that?":
            jump lbl_Lion_noWimp
        "Just let it go, it's not worth it.":
            if (iOption==3):
                show gor dull at left
                show sam dull at left
                hide leo
                show leo dull at left
                l "Yeah, I guess... No, wait."
                show leo mad at left
                l "I won't let that one slide."
                jump lbl_Lion_noWimp
            jump lbl_Lion_Wimp
    
    
label lbl_Lion_Wimp:
    #if wimp father drags her away
    #calls Leo a wimp
    show gor dull at left
    show sam dull at left
    hide leo
    show leo skeptic at left
    l "..."
    f "That's what I thought. Come with me Pea."
    hide pea
    show pea sad at right
    p "Leo..."
    hide father
    hide pea
    l "..."
    s "..."
    g "..."
    l "Let's go home, guys."
    jump lbl_MatchMaker_Lion_End

label lbl_Lion_noWimp:
    show gor dull at left
    show sam dull at left
    hide leo
    show leo mad at left
    l "I'm going to have to ask you to apologize."
    show gor shock at left
    show sam shock at left
    f "I'm sorry, what?"
    hide sam
    show sam shock at left
    s "(Holy crap he looks pissed now.)"
    hide leo
    show leo mad at left
    l "Say what you want about me, but I can't let you say things like that about the people I care about."
    hide sam
    show sam shock at left
    s "(He's deadly serious about this, its been a long time since I saw Leo this worked up.)"
    f "..."
    l "..."
    stop music
    f "I apologize."
    l "If you won't I'll hav... What?!"
    hide leo
    show leo shock at left
    f "I'm sorry I didn't mean to offend you or the others. "
    hide sam
    show sam shock at left
    s "(What is going on? I don't understand at all.)"
    #if manly father approves of the pair
    #says wants a strong guy to look after her
    show father happy
    play music music_park fadein 1.0
    f "I'm just so worried about my daughter you see, I had to make sure you were the sort of guy to stand up for yourself, and most of all stand up for her."
    f "Honestly I knew this day would come eventually. She talks about you a lot, and you really seem like a nice fellow."
    
    f "So now that I'm satisfied that you're not a wimp I'm not against this union."   
    f "So I guess it's up to Persephone now."
    show gor happy at left
    show sam happy at left
    hide leo
    show leo excited at left
    hide father
    show father happy at right
    hide pea 
    show pea neutral:
      xalign 0.8
      yalign 1.0
    l "So Persephone, will you by my Girlfriend?"
    
    
    if (iPoints < 5):
        show pea sad
        p "Well actually during this I've learned some things about you I didn't know before Leo."
        show gor shock at left
        show sam shock at left
        hide leo
        show leo shock at left
        p "I don't think it would work out, after all, I'm sorry."
        hide leo
        show leo dull at left
        l "..."
        show gor dull at left
        hide sam
        show sam dull at left
        s "Leo..."
        hide gor
        show gor dull at left
        g "..."
        l "Let's just go home guys."
        jump lbl_MatchMaker_Lion_End
    
    #per decides he's good enough 
    show pea content
    p "Yes!"
    show gor happy at left
    show sam happy at left
    hide leo
    show leo excited at left
    l "WHOOHOO!"
    hide sam
    show sam happy at left
    s "Good Job Leo."
    hide gor
    show gor happy at left
    g "Congratulations Leo."
    hide leo
    show leo excited at left
    p "Let me know when you've figured out where you're talking me on our first date~"
    p "Bye Leo~"
    f "Goodbye Leo, I'm sure we'll be seeing a lot of each other from now on."
    l "Goodbye Sir."
    l "Bye Pea~"
    
    hide gor
    show gor happy at left
    g "Well all well that ends well."
    show gor happy at left
    show sam happy at left
    hide leo
    show leo happy at left
    l "Yep, let's go home."
    hide sam
    show sam happy at left
    s "Yeah, I'm surprisingly tired after all that."
    hide gor
    show gor skeptic at left
    g "I agree, even though we weren't really involved it was still nerve-wracking."
         
    $bMatchLion = True
    
    jump lbl_MatchMaker_Lion_End    

label lbl_MatchMaker_Lion_End:
    return
    
#----------------------------------------------------------------------
#----------------------------------------------------------------------
    
label lbl_MatchMaker_Goat:
    scene bg home day with fade
    play music music_home fadein 1.0
    #$ renpy.transition(slow_dissolve, layer="master")
    show ChimeraBase at left
    show leo happy at left
    show gor happy at left
    show sam happy at left
    $bGoatHelped = True
    $iPoints = 0
    s "I guess I'm Helping Gordon then."
    #Gordon asks for Help asking Helen on a date
    hide gor
    show gor embarrassed at left
    g "So about that Harpy."
    g "What do you suggest I do?"
    
    menu:
        "What should Gordon do about the harpy?"
        "Give up on her":
            jump lbl_Goat_Giveup
        "Talk to her":
            s "You should get to know her better and see how it goes"
            jump lbl_Goat_Talk
        "Ask her out":
            s "It'll be a good chance to get to know her better"
            jump lbl_Goat_Talk
        
label lbl_Goat_Giveup:
    hide sam
    show sam dull at left
    hide gor
    show gor sad at left
    g "Yeah maybe you're right."
    g "I'll just try to forget her."
    jump lbl_MatchMaker_Goat_End
    
label lbl_Goat_Talk:
    g "You're right. I need to get to know her better."
    hide leo
    show leo skeptic at left
    l "Yeah, because you don't even know her name."
    hide gor
    show gor dull at left
    g "Yeah, we don't know much about her at all."
    g "How will we find her?"
    hide sam
    show sam happy at left
    s "I guess all we can do is look around town and hope we find her."
    if (bBakery==True):
        l "Didn't she say something about cakes?"
        hide sam
        show sam dull at left
        s "No that was you, Leo."
        show sam happy at left
        s "But she did mention a bakery, maybe we should check it out?"
    
    #try to use info to find her
    #look in places 
    #choice -library
    #choice -gamestore
    #choice -park
    #choice -bakery - Helen here (extra points for finding her faster) 
    $iPoints = 3
label lbl_goat_locationMenu:
    menu:
        "Where should we look?"
        "Lets check the library" if (iPoints > 0):
            $iPoints -= 1
            call lbl_goat_library from _call_lbl_goat_library
        "Lets check the game store" if (iPoints > 0):
            $iPoints -= 1
            call lbl_goat_gamestore from _call_lbl_goat_gamestore
        "lets check the park" if (iPoints > 0):
            $iPoints -= 1
            call lbl_goat_park from _call_lbl_goat_park
        "Lets check the bakery" if (bBakery==True):
            jump lbl_goat_bakery
        "Lets go home."  if (iPoints == 0):
            hide leo
            show leo dull at left
            l "I'm tired."
            hide sam
            show sam dull at left
            s "It is getting pretty late."
            hide gor
            show gor dull at left
            g "Ok, lets call it a day and head back."
            jump lbl_goat_home
            
    jump lbl_goat_locationMenu

label lbl_goat_home:
    scene bg home day with fade
    play music music_home fadein 1.0
    #$ renpy.transition(slow_dissolve, layer="master")
    show ChimeraBase at left
    show leo dull at left
    show sam dull at left
    hide gor
    show gor sad at left
    g "All right, let's just call it a day."
    hide sam
    show sam dull at left
    s "Yeah I'm tired."
    hide leo
    show leo excited at left
    l "I'm hungry. Let's get some cake."
    s "Uh...why cake?"
    l "I like cake."
    hide gor
    show gor skeptic at left
    g "You like a lot of things."
    hide leo
    show leo happy at left
    l "Yeah but there's a bakery across the street."
    hide gor
    show gor happy at left
    g "Oh, so there is. Should we go in?"
    hide sam
    show sam happy at left
    s "Sure, why not?"
    
    jump lbl_goat_bakery
    
label lbl_goat_library:
    scene bg library day with fade
    play music music_library fadein 1.0
    ##$ renpy.transition(slow_dissolve, layer="master")
    show ChimeraBase at left
    show leo dull at left
    show sam dull at left
    hide gor
    show gor dull at left
    g "I don't think she's here."
    g "Wait since we're here I want to see if they have that book in stock yet."
    scene bg black with fade
    ".{w}.{w}."
    scene bg library day with fade
    show ChimeraBase at left
    show leo dull at left
    show sam dull at left
    hide gor
    show gor sad at left
    g "They still don't have it."
    hide sam
    show sam skeptic at left
    s "I'd have thought you of all people wouldn't want to waste time."
    hide gor
    show gor embarrassed at left
    g "Its a really good book though!"
    s "Well it's your choice."
    return
    
label lbl_goat_gamestore:
    scene bg shop day with fade
    play music music_gameshop fadein 2.0
    #$ renpy.transition(slow_dissolve, layer="master")
    show ChimeraBase at left
    show leo dull at left
    show sam dull at left
    hide gor
    show gor dull at left
    g "I don't think she's here."
    hide sam
    show sam happy at left
    s "OK give me a second, I want to see if they have any new games in."
    hide gor
    show gor pissed at left
    g "Can't we do it another time?"
    show gor dull at left
    hide sam
    show sam dull at left
    s "We're already here, it'll only take a second."
    scene bg black with fade
    ".{w}.{w}."
    scene bg shop day with fade
    show ChimeraBase at left
    show leo dull at left
    show gor dull at left
    hide sam
    show sam happy at left
    s "Haha, that took longer than expected. I didn't even know they were making a sequel to that one."
    return
    
label lbl_goat_park:
    scene bg forest day with fade
    play music music_park fadein 1.0
    #$ renpy.transition(slow_dissolve, layer="master")
    show ChimeraBase at left
    show leo happy at left
    show gor happy at left
    show sam happy at left
    s "Well its a pretty big park, lets split up and look for her."
    hide gor
    show gor pissed at left
    show leo dull at left
    g "..."
    hide leo 
    show leo dull at left
    l "..."
    hide sam
    show sam happy at left
    s "Come on, not even a chuckle?"
    hide leo 
    show leo dull at left
    l "I don't get it."
    hide sam
    show sam dull at left
    s "(Why do I even bother?)"
    scene bg black with fade
    ".{w}.{w}."
    scene bg forest day with fade
    show ChimeraBase at left
    show leo dull at left
    show sam dull at left
    hide gor
    show gor sad at left
    g "I don't think she's here."
    return
    
label lbl_goat_bakery:
    scene bg bakery day with fade
    play music music_bakery fadein 1.0
    #$ renpy.transition(slow_dissolve, layer="master")
    show ChimeraBase at left
    show leo happy at left
    show gor happy at left
    show sam happy at left
    
    s "I don't think we've been in this one before."
    hide gor
    show gor happy at left
    g "I think it's newly opened."
    show helen happy at right
    h "Welcome~"
    hide leo
    show leo excited at left
    l "We found her!"
    show gor embarrassed at left
    l "Hi!"
    show helen content
    h "Oh its the guys from the game store."
    show helen happy
    h "Hows it going?"
    
    #helen comments on the time (depends on how long it took to find her)
    hide gor
    show gor embarrassed at left
    g "We were wondering if you have some time to talk to us?"   
    if (iPoints == 3):
        show helen content
        h "Well you're pretty early so sure. We don't get many customers at this time so I was getting bored anyway."
    elif (iPoints > 0):
        show helen content
        h "I guess there's still some time before the rush starts so sure, why not?"
    elif (iPoints == 0):
        show helen skeptic
        h "It's getting pretty busy so you'll have to make it quick."
        
    h "So how can I Help you"
    #convince Gordon to talk to her
    
    hide sam
    show sam dull at left
    s "Just talk to her Gor."
    hide gor
    show gor embarrassed at left
    g "I don't know what to ask. How do I start a conversation?"
    hide sam
    show sam happy at left
    s "Don't worry I'll give you cues."
    hide gor
    show gor embarrassed at left
    g "Er first of all..."
    menu:
        "What should Gordon ask first?"
        "Her name":
            hide gor
            show gor happy at left
            g "Definitely a good place to start."
            pass
        "Her 3 sizes":
            show sam skeptic
            hide leo
            show leo dull at left
            l "3 sizes?"
            hide gor
            show gor pissed at left
            g "I-I can't ask that!"
            pass
        "What life as a baker is like":
            hide gor
            show gor happy at left
            g "That might be an interesting story to hear."
            hide leo
            show leo excited at left
            l "Or ask her what being a cake is like."
            hide sam
            show sam dull at left
            s "I think you should stop trying to Help Leo."
            hide leo
            show leo dull at left
            l "Aww."
            pass
            
    show helen embarrassed    
    h "Wait wait, before you start I just realized I don't know what to call you guys. "
    show ChimeraBase at left
    show leo happy at left
    show sam happy at left
    hide gor
    show gor happy at left
    g "Oh my apologies, my name is Gordon."
    hide sam
    show sam happy at left
    s "Mine is Samuel."
    hide leo
    show leo happy at left
    l "I'm Leo."
    show helen content   
    h "My Name is Helen, nice to meet you~"

    menu:
        "What should Gordon ask first?"
        "Does she work here?":
            show leo happy at left
            show sam happy at left
            hide gor
            show gor happy at left
            g "So do you work here?"
            show helen pissed
            h "Not normally, but one of the part-timers called in sick so I got drafted."
            show helen mad
            h "I wouldn't mind if I was getting paid."
            hide gor
            show gor skeptic at left
            g "You don't get paid."
            show helen skeptic
            h "No, apparently getting dinner every day should be payment enough."
            hide gor
            show gor dull at left
            g "That's pretty harsh."
            show helen dull
            h "Such is life in the family business, I guess."
            hide gor
            show gor happy at left
            if bBakery == True:
              g "Oh right, last time we met you mentioned that your parents owned the bakery, didn't you?"
            else:
              g "Family business?"
              show helen happy
              h "Oh right, my parents own this place."
            show helen happy
            h "On the bright side though, i get all the leftover bread i want."
            hide leo
            show leo excited at left
            l "All you want?! Sam we should run a bakery too."
            hide sam
            show sam dull at left
            s "(Dammit Leo, you're interrupting the conversation.)"
              
        "What is it like to fly?":
            show leo happy at left
            show sam happy at left
            hide gor
            show gor happy at left
            g "You can fly right? What's it like?"
            show helen skeptic    
            h "Well technically, yes I can."
            g "Technically?"
            h "Technically."
            g "Er what do you mean?"
            show helen embarrassed    
            h "It's kind of embarrassing."
            g "What is?"
            show helen dull    
            h "I don't fly much."
            g "You don't?"
            h "No, I don't."
            hide sam
            show sam dull at left
            s "(Wow this girl likes to beat around the bush, doesn't she?)"
            hide gor
            show gor dull at left
            g "Can I ask why not."
            show helen embarrassed    
            h "I-I'm afraid."
            g "Afraid?"
            show helen upset    
            h "Yeah, I'm afraid of heights. A pretty shameful problem for a harpy."
            g "I see, it must be hard for you."
            show helen embarrassed    
            h "Y-You're not going to laugh or make fun of me?"
            g "Why would I? It's not like being afraid of heights is that uncommon."
            hide sam
            show sam dull at left
            s "(I dunno, I personally want to poke a little fun at her now...I'm a horrible fellow, aren't I?)"
            h "I-I guess."
            show helen pissed    
            h "Most people I tell certainly find it amusing. You're a strange fellow."
            hide gor
            show gor embarrassed at left
            g "I-I'm sorry?"
            show helen content    
            h "Haha, I don't mean in a bad way."
            $iPoints +=1
        "Ask about her interests":
            jump lbl_goat_AskInterests
            
    hide gor
    show gor embarrassed at left
    g "What next?"
    hide sam
    show sam happy at left
    s "Why not ask about her interests?"

label lbl_goat_AskInterests:
    hide gor
    show gor embarrassed at left
    g "So what kinds of things are you interested in?"
    show helen coy
    h "Hmmm...Guess."
    g "What?"
    h "Guess."
    hide gor
    show gor dull at left
    g "Guess what?"
    h "Guess my interests."
    g "Can't you tell me?"
    show helen skeptic
    h "Don't be so boring."
    hide gor
    show gor embarrassed at left
    g "O-Ok"
    
    #ask about
    #choice -movies
    #choice -games
    #choice -wilderness
    #choice -flying

    menu:
        "What should Gordon suggest?"
        "Movies.":
            hide gor
            show gor happy at left
            g "Do you like movies?"
            show helen happy
            h "Well it depends on the movie I guess. As long as its nothing sappy or boring I'm generally OK."
            show helen dull
            h "Unfortunately I don't get to go as often as I like."
            g "No? Why not."
            show helen embarrassed
            h "Let's just say I have a sweet tooth and a small allowance and leave it at that."
            hide gor
            show gor skeptic at left
            g "Haha. Poor girl."
            h "Hey don't laugh!"
            g "I'm sorry."
            show helen content
            h "Actually now that I think about it, you always look so serious, you should smile more often."
            hide gor
            show gor embarrassed at left
            g "..."
            hide leo
            show leo skeptic at left
            l "Ha, he's blushing!"
            hide gor
            show gor pissed at left
            g "S-Shut up Leo!"
            $iPoints +=1
            
        "Video Games.":
            hide gor
            show gor happy at left
            g "Do you like Video Games?"
            show helen content
            h "Bing Bong! We have a winner!"
            g "W-What?"
            h "I love video games. Especially the Digital Human ones."
            hide gor
            show gor happy at left
            g "Haha, Sam is always telling me that nobody likes that series. I think they're a lot more interesting than the Pocket Humans games. "
            hide gor
            show gor skeptic at left
            g "Being outnumbered sucks."
            hide sam
            show sam dull at left
            s "Pfft. Pocket Humans rules."
            h "Hahahaha. You guys crack me up."
            $iPoints +=2
        "Hiking.":
            hide gor
            show gor happy at left
            g "Do you like hiking and things like that?"
            show helen dull
            h "Er not really, I'm more of an indoor person."
            hide gor
            show gor dull at left
            g "I see."
        "Flying.":
            hide gor
            show gor happy at left
            g "Do you like flying?"
            show helen upset
            h "...No."
            s "(Guess its a sore point.)"
    
    show helen dull
    h "Well I guess I better get back to work now."
    hide gor
    show gor happy at left
    g "Well it was nice talking to you."
    show helen happy
    h "You too Gordon."
    h "See you later guys~"
    hide gor
    show gor embarrassed at left
    g "..."
    g "Wait..."
    h "Yes?"
    #choice - ask her out to the movies
    #choice - ask her out for coffee
    menu:
        "Ask her out?"
        "Ask her out for coffee.":
            g "Would you like to go out for coffee sometime?"
            if (iPoints > 4):
                show helen love
                h "Hmmm...Sure why not."
                show sam happy
                show leo happy
                hide gor
                show gor love at left
                g "Awesome!"
                hide leo
                show leo excited at left
                l "Good job Gor!"
                hide sam
                show sam happy at left
                s "Congrats."
                show helen content
                h "Let me know when you think of a date and time."
                hide gor
                show gor love at left
                g "Okay!"
                hide helen
                hide gor
                show gor happy at left
                g "Let's go home, guys."
                $bMatchGoat = True
                jump lbl_MatchMaker_Goat_End
            else:
                show helen dull
                h "Hmm... Maybe another time. I've been really busy lately."
                show sam dull
                show leo dull
                hide gor
                show gor sad at left
                g "O-Okay, I understand."
                hide leo
                show leo dull at left
                l "..."
                hide sam
                show sam dull at left
                s "..."
                hide gor
                show gor sad at left
                g "Goodbye"
                show helen happy at right
                h "Bye guys."
                hide helen
                g "Let's go home, guys."
            jump lbl_MatchMaker_Goat_End                
                
        "Ask her out to the movies.":
            jump lbl_goat_movies
        "Don't ask her out.":
            show sam dull
            show leo dull
            hide gor
            show gor embarrassed at left
            g "N-Nevermind."
            show gor dull
            g "Let's go home, guys."
            jump lbl_MatchMaker_Goat_End
        
    
    #choice -Digital Humans: Beta release (OHMYGODYES!!! Ahem. Yeah sure, whatever.)
    #choice -Sappy Treant Love Story 2 (Eww. I'm not into that sort of movie)
    #choice -The Minotaurix (Isn't that the one with Kaiju Reeves? I guess it might be ok.)
label lbl_goat_movies:
    hide gor
    show gor embarrassed at left
    g "Would you like to go to the movies with me?"
    show helen dull
    h "Hmm...what movie?"
label lbl_goat_movies_choice:
    menu:
        "What movie?"
        "Digital Humans: Beta release":
            show helen content
            h "OHMYGODYES!!!"
            show helen embarrassed
            h "Ahem. I mean, Yeah sure, whatever."
            $iMovie = 1
            $iPoints += 2
        "Sappy Treant Love Story 2":
            if not bLoveMovieFlag:
              show helen skeptic
              h "Eww. I'm not into that sort of movie."
              hide gor
              show gor dull at left
              g "O-Oh, then I'll pick another one..."
              $iPoints -= 1
              $bLoveMovieFlag = False
              jump lbl_goat_movies_choice
            else:
              show helen pissed
              h "If you want to see it that badly, why not just go without me."
              hide helen
              hide gor
              show gor dull at left
              g "Wait, Helen-"
              hide gor
              show gor sad at left
              g "Oh she's gone, nevermind then I guess."
              g "Let's go guys."
              jump lbl_MatchMaker_Goat_End
        "The Minotaurix":
            show helen happy
            "Isn't that the one with Kaiju Reeves? I guess it might be OK."
            $iPoints += 1
            $iMovie = 2
            
    hide gor
    show gor love at left
    g "Awesome."
        
    if (iPoints > 5):
        #decides they can make the last showing of the movie if picked
        show helen embarrassed
        h "Actually if you come back when my shift is over we can still make the last showing."
        h "I-I mean if that is okay with you."
        hide gor
        show gor love at left
        g "S-Sure!"
        scene bg black with fade
        ".{w}.{w}."
        scene bg bakery day with fade
        show ChimeraBase at left
        show leo happy at left
        show gor happy at left
        show sam happy at left
        if (iMovie == 1):
            show helen love
            h "That was AMAZING!"
            hide gor
            show gor skeptic at left
            g "It was pretty good."
            hide sam
            show sam skeptic at left
            s "OK so it didn't put me to sleep, but I still prefer Pocket Humans."
            hide leo
            show leo skeptic at left
            l "Ahahaha. So stubborn Sammy."
        else:  
            show helen happy
            h "That was pretty interesting."
            hide gor
            show gor happy at left
            g "I enjoyed it too."
            hide sam
            show sam shock at left
            s "Just interesting? I'll never understand some people."
            hide sam
            show sam dull at left
            hide leo
            show leo sad at left
            l "I ran out of popcorn before the movie started. "
            hide sam
            show sam dull at left
            s "I told you to slow down Leo."
        
        show helen content
        h "Anyway I had fun, Gordon. Thanks for walking me back."
        hide gor
        show gor happy at left
        g "I did too Helen. And no problem."
        
        show helen content
        h "So Gordon."
        g "Yes?"
        
        show helen content
        h "Will you go out with me again sometime?"
        hide gor
        show gor love at left
        g "I-I would be glad to!"
        
        hide leo
        show leo skeptic at left
        l "Sam...does it still count if the girl asks the guy?"
        hide sam
        show sam happy at left
        s "I-I don't see why not."
        hide leo
        show leo excited at left
        l "Good job Gor!"
        hide sam
        show sam happy at left
        s "Congrats man.    
        hide gor
        show gor happy at left  "
        g "Let's go home, guys."
        show helen content
        h "See you again guys."
        hide sam
        show sam happy at left
        s "Bye."
        hide leo
        show leo happy at left
        l "Bye."
        hide gor
        show gor happy at left
        g "Goodbye Helen."
        hide helen 
        
        $bMatchGoat = True
        jump lbl_MatchMaker_Goat_End
        
    else:
        show helen dull
        h "Actually on second thoughts, I'm pretty busy so I won't be able to join you after all."
        h "Sorry."
        hide gor
        show gor sad at left
        g "I-It's ok. I understand."
        hide leo
        show leo dull at left
        l "..."
        hide sam
        show sam dull at left
        s "..."
        hide gor
        show gor sad at left
        g "Goodbye."
        show helen dull at right
        h "Bye guys."
        hide helen
        g "Let's go home, guys."
        jump lbl_MatchMaker_Goat_End
        

label lbl_MatchMaker_Goat_End:
    return
    
#----------------------------------------------------------------------
#----------------------------------------------------------------------

label lbl_MatchMaker_Snake:
    if (bLionHelped == False or bGoatHelped == False):
        s "Hmm, if I don't Help out the others I might not be able to rely on them if something comes up..."
        menu:
            "Should I still continue?"
            "Yeah, who needs those guys anyway?":
                pass
            "Perhaps I should reconsider...":
                jump lbl_MatchMaker_Choice
    
    $iPoints = 0
    hide sam
    show sam happy at left
    s "I guess that means it's my turn."
    hide sam
    show sam embarrassed at left

    s "I won't be able to avoid doing this much longer I guess."
    if (bLionHelped == True):
        hide leo
        show leo happy at left
        l "I've got your back, Sammy."
    if (bGoatHelped == True):
        hide gor
        show gor happy at left
        g "I'm right behind you Sam. You don't have to worry."
        
    if (bLionHelped == True or bGoatHelped == True):
        hide sam
        show sam happy at left
        s "Thanks"
    
    hide sam
    show sam love at left
    s "OK, I'm going to ask her out today."
    hide leo
    show leo excited at left
    l "Go for it, Sammy!"
    
    #wonder how you're going to ask her out
    #realise you don't know where she is
    hide sam
    show sam dull at left
    s "Wait, how will I find her?"
    hide gor
    show gor happy at left
    g "Well what do you know about her?"
    
    hide sam
    show sam love at left
    s "Well she's amazing!"
    hide gor
    show gor skeptic at left
    g "I mean, like where she lives, or what she does etc."
    hide sam
    show sam embarrassed at left
    s "I-I don't know. I was never able to ask much before."
    #if bMatchGoat mentions he often sees her in the park 
    if (bMatchGoat == True):
        hide gor
        show gor happy at left
        g "Well now that I think about it, I often see her in the park so it might be a good idea to check there."
    else:
        show gor dull
        hide sam
        show sam dull at left
        s "(Hmmm... Gordon seems to be lost in thought about something. I wonder what it is?)"
    #else go searching randomly and take ages to find her
    
    #look in places (up to 3)
    #choice -library
    #choice -gamestore
    #choice -park (someone points you to the lake)
    #choice -bakery 
    #choice -cinema
    
    $iPoints = 3
label lbl_snake_locationMenu:
    menu:
        "Where should we look?"
        "Lets check the library" if (iPoints > 0):
            $iPoints -= 1
            call lbl_snake_library from _call_lbl_snake_library
        "Lets check the game store" if (iPoints > 0):
            $iPoints -= 1
            call lbl_snake_gamestore from _call_lbl_snake_gamestore
        "lets check the park" if (iPoints > 0):
            jump lbl_snake_park
        "Lets check the bakery" if (iPoints > 0):
            $iPoints -= 1
            call lbl_snake_bakery from _call_lbl_snake_bakery
        "Lets go home."  if (iPoints == 0):
            jump lbl_snake_home
            
    jump lbl_snake_locationMenu

label lbl_snake_home:
    scene bg home day with fade
    play music music_home fadein 1.0
    #$ renpy.transition(slow_dissolve, layer="master")
    show ChimeraBase at left
    show leo dull at left
    show sam dull at left
    hide gor
    show gor dull at left
    g "All right, it's getting late. Let's just call it a day."
    hide sam
    show sam sad at left
    s "Yeah, we can try again some other day."    
    jump lbl_MatchMaker_Snake_End
    
label lbl_snake_library:
    scene bg library day with fade
    play music music_library fadein 1.0
    #$ renpy.transition(slow_dissolve, layer="master")
    show ChimeraBase at left
    show leo happy at left
    show gor happy at left
    hide sam
    show sam dull at left
    s "I don't think she's here."
    hide gor
    show gor happy at left
    g "Wait since we're here I want to see if they have that book in stock yet."
    scene bg black with fade
    ".{w}.{w}."
    scene bg library day with fade
    show ChimeraBase at left
    show leo dull at left
    show sam dull at left
    hide gor
    show gor dull at left
    g "They still don't have it."
    hide sam
    show sam dull at left
    s "I don't really want to waste too much time."
    hide gor
    show gor sad at left
    g "{size=-10}It's a really good book though...{/size}"
    return
    
label lbl_snake_gamestore:
    scene bg shop day with fade
    play music music_gameshop fadein 2.0
    #$ renpy.transition(slow_dissolve, layer="master")
    show ChimeraBase at left
    show leo happy at left
    show gor happy at left
    show sam happy at left
    hide sam
    show sam dull at left
    s "I don't think she's here."
    hide leo
    show leo excited at left
    l "Flash sale! Up to 50% off?!"
    hide sam
    show sam excited at left
    s "OK give me a second, I want to see if they have any new games in."
    hide gor
    show gor dull at left
    g "Can't we do it another time?"
    s "We're already here, it'll only take a second."
    hide leo
    show leo skeptic at left
    l "Yeah the good stuff might be gone later"
    scene bg black with fade
    ".{w}.{w}."
    scene bg shop day with fade
    show ChimeraBase at left
    show leo dull at left
    show gor dull at left
    show sam dull at left
    s "Nothing good is on sale."
    return
    
label lbl_snake_bakery:
    scene bg bakery day with fade
    play music music_bakery fadein 1.0
    #$ renpy.transition(slow_dissolve, layer="master")
    show ChimeraBase at left
    show leo happy at left
    show gor happy at left
    hide sam
    show sam dull at left
    s "I don't think she's here."
    hide leo
    show leo excited at left
    l "We should some cake."
    hide sam
    show sam dull at left
    s "But the line is so long."
    hide leo
    show leo dull at left
    l "But I'm hungry!"
    hide gor
    show gor skeptic at left
    g "You're not going to budge are you?"
    hide leo
    show leo skeptic at left
    l "Nope."
    scene bg black with fade
    ".{w}.{w}."
    scene bg bakery day with fade
    show ChimeraBase at left
    show leo excited at left
    show gor dull at left
    hide sam
    show sam pissed at left
    s "Happy now?"
    hide leo
    show leo happy at left
    l "Yep."    
    return
    
label lbl_snake_park:
    scene bg forest day with fade
    play music music_park fadein 1.0
    #$ renpy.transition(slow_dissolve, layer="master")
    show ChimeraBase at left
    show leo happy at left
    show gor happy at left
    hide sam
    show sam dull at left
    s "I don't think she's here."
    hide gor
    show gor happy at left
    g "Why don't we ask around and see if anyone has seen her today."
    scene bg black with fade
    ".{w}.{w}."
    scene bg forest day with fade
    show ChimeraBase at left
    show leo happy at left
    show gor happy at left
    hide sam
    show sam dull at left
    s "So she's at the lake?"
    hide leo
    show leo happy at left
    l "That's what the lady at the fountain said."
    hide sam
    show sam happy at left
    s "OK then, let's go."
    
label lbl_snake_lake:
    scene bg lake day with fade
    play music music_park fadein 1.0
    #$ renpy.transition(slow_dissolve, layer="master")
    show ChimeraBase at left
    show leo happy at left
    show gor happy at left
    #meet at the lake (extra points for finding her faster) 
    #if places 2 or fewer shes swimming 
    #else finished swimming
    hide sam
    show sam happy at left
    s "OK OK. You can do this. Just breathe. You're ready for this."
    hide gor
    show gor skeptic at left
    g "Er Sam, you're talking to yourself out loud again."
    hide sam
    show sam embarrassed at left
    s "S-Sorry. I'm just nervous."
    
    hide sam
    show sam love at left
    s "Oh there she is."
    if (iPoints > 1 ): 
        s "Looks like she's swimming in the Lake."
        $bSwimming = True
    else : 
        s "She's all wet, I wonder if she was in the water."
        $bSwimming = False
        
label lbl_snake_Swim:
    #if swimming
    #chat
    #what are you doing? (Swimming. If you can't tell by looking I must be doing it wrong...)
    #Arent you cold? (Nah the scales keep out the cold)
    show melissa happy at right
    m "Oh Hello there guys. What brings you around here?"
    hide leo
    show leo skeptic at left
    l "Oh nothing much."
    hide gor
    show gor skeptic at left
    g "Just happened to be in the area."
    g "...Right, Sam?"
    menu:
        "...Right, Sam?"
        "(OHSHITSON!) Y-Yeah, just passing by.":
            show melissa content at right
            m "That's nice. Lovely day for a stroll isn't it?"
            hide sam
            show sam embarrassed at left
            s "Y-Yeah, it sure is."
            m "Yeah, this weather is perfect for swimming."
        "(OHSHITSON!) I-I came to see you.":
            m "Oh? Did you want me for something?"
            hide sam
            show sam shock at left
            s "(What have you done Sam?!)"
            s "..."
            show melissa dull at right
            m "No?"
            hide sam
            show sam embarrassed at left
            s "Y-Yes, I just wanted to talk to you."
            show melissa coy at right
            m "Oh I see. What did you want to talk about?"
            
        "(OHSHITSON! I can't do it! Impossible!)":
            jump lbl_MatchMaker_Snake_GoHome
        
    s "..."
    hide leo
    show leo dull at left
    l "..."
    hide gor
    show gor dull at left
    g "Sam."
    hide sam
    show sam embarrassed at left
    s "S-So what are you doing?"
    if (bSwimming == True):
        show melissa coy at right
        m "Well I'm swimming. If you can't tell by looking I must be doing it wrong..."
        hide sam
        show sam embarrassed at left
        s "N-No not at all. You're great."
        s "I-I mean, You look great."
        s "I er ...Y-You look like you're doing great."
        hide sam
        show sam dull at left
        s "(Open foot, insert mouth.)"
    else:
        show melissa coy at right
        m "Well I just finished swimming."
        
    hide leo
    show leo skeptic at left
    l "Why don't you ask her about it, Sam?"
    
    hide sam
    show sam embarrassed at left
    s "Erm Melissa..."
    m "Yes?"
    #ask about swimming
    #choice -Are you swimming for fun? [a] (I'm training)
    menu:
        "Ask about swimming?"
        "A-Are you swimming for fun?":
            show melissa happy at right
            m "Well actually I'm in training."
        "(I can't do it!)":
            jump lbl_MatchMaker_Snake_GoHome
    
label lbl_snake_SwimTrain:
    #choice if [a] -what are you training for?  (for a race against mermaids)
    #choice -I bet we could beat you in a race!
    #choice -You should race against us, the competition will do you good.
    menu: 
        "She's in training..."
        "What are you training for?":
            show melissa dull at right
            m "I'm racing for the local team against another team from the neighboring town."
            hide sam
            show sam happy at left
            s "Sounds pretty cool."
            m "Yeah, but I heard they were very good. Hence the training."
            s "Well good luck with that."
            show melissa happy at right
            m "Thanks~"
            jump lbl_snake_SwimTrain
        "I-I bet we could beat you in a race!":
            show melissa skeptic at right
            m "Well well, confident are we?"
        "Y-You should race against us, the competition will do you good.":
            show melissa happy at right
            m "I suppose a little competition wouldn't hurt."
            $iPoints +=1
        "(I can't do it after all!)":
            jump lbl_MatchMaker_Snake_GoHome
        
    if (bSwimming == False):
        show melissa dull at right
        m "However I already finished my training for the day, so you'll have to challenge me another time."
        jump lbl_snake_AfterSwim
    else:
        show melissa skeptic at right
        m "How about right now then?"
    
        #Leo refuses to get wet.
        hide leo
        show leo dull at left
        l "Wait wait. Swimming?"
        hide sam
        show sam happy at left
        s "What's up, Leo?"
        hide leo
        show leo dull at left
        l "I don't want to get wet." 
        hide sam
        show sam sad at left
        s "B-But Leo..."
        #convince Leo to Help if bMatchLion
        #else (So much for that idea.)
        if (bMatchLion == True):
            hide leo
            show leo dull at left
            l "Well, I guess you did Help me out before."
            hide leo
            show leo pissed at left
            l "So I'll do it. But you better appreciate it. I hate getting wet."
            hide sam
            show sam happy at left
            s "Thanks, Leo."
        else:
            hide leo
            show leo dull at left
            l "I'm not getting wet. No way no how."
            hide sam
            show sam dull at left
            s "(If only I had some way to get him to Help.)"
            
            s "W-Well so much for that idea."
            s "S-Sorry Melissa."
            show melissa dull at right
            m "Don't worry about it."
            jump lbl_snake_AfterSwim
        
        #if race 
        #if Helped Gor and Leo try hardest and only lose by a hair's breadth
        #else if only one Helped lose by a lot.
        show melissa content at right
        m "Well let me know when you're ready then. "
        hide sam
        show sam happy at left
        s "OK guys, I feel like we need to take this seriously, otherwise, there's no point."
        hide leo
        show leo excited at left
        l "OK I'll do my best!"
        if (bMatchGoat == True):
            hide gor
            show gor happy at left
            g "You can count on me!"
        else:
            hide sam
            show sam dull at left
            show gor dull
            s "(Hmm. Gordon seems distracted.)"
            hide gor
            show gor dull at left
            g "What? Oh yeah, sure."
        #medusa comments on the result (extra points for coming close)
        scene bg black with fade
        ".{w}.{w}."
        scene bg lake day with fade
        show ChimeraBase at left
        show leo dull at left
        show gor dull at left
        show sam dull at left
        if (bMatchGoat == True):
            show melissa happy at right
            m "Wow you guys did pretty well."
            show gor dull
            show sam dull at left
            hide leo
            show leo dull at left
            l "We...still...lost."
            show melissa content at right
            m "But I had to go all out just to stay ahead."
            m "Maybe I should train with you guys more often."
            $iPoints +=1
        else:
            show melissa dull at right
            m "After all that talk you didn't present much of a challenge."
            m "It didn't seem like your hearts were really in it."
            hide sam
            show sam sad at left
            s "I-I'm sorry."
    
    m "Well we better get out and dry off."
    scene bg black with fade
    ".{w}.{w}."
    scene bg lake day with fade
    show ChimeraBase at left
    show leo happy at left
    show gor happy at left
    show sam happy at left
    show melissa happy at right
    #after swimming or if late
label lbl_snake_AfterSwim:
    show melissa happy at right
    m "So was there anything else you wanted?"
    
    hide gor
    show gor happy at left
    g "Ask what else she likes Sam"
    
    hide sam
    show sam embarrassed at left
    s "So er..."
    #Ask about
    #choice -what else are you in to? (video games)
    #choice -Video Games (I'm really into that new Pocket Humans game)
    #choice -What kinds of food do you like? (Fast food)
    menu:
        "What should I ask?"
        "What else are you into besides swimming.":
            pass
        "(I can't do it after all!)":
            jump lbl_MatchMaker_Snake_GoHome

    show melissa dull at right
    m "I actually recently got into video games after playing a few my cousin brought over."
    hide sam
    show sam happy at left
    s "Oh so that's why you were in the store that time?"
    show melissa happy at right
    m "Yeah, buying something for myself."
    
    menu:
        "I wonder what she got..."
        "Was it Centaur Princess Pony and Friends?":
            show melissa dull at right
            m "Wait, is that the one that's so pink you need sunglasses to look at the box?"
            hide sam
            show sam embarrassed at left
            s "Er...yeah?"
            show melissa neutral at right
            m "And you think it's my kind of game?"
            hide sam
            show sam dull at left
            s "Erm..."
            show melissa pissed at right
            m "Because I'm a girl?"
            hide sam
            show sam embarrassed at left
            s "Uh...I..."
            m "..."
            show melissa skeptic at right
            m "Haha, I'm just messing with you. "
            show melissa dull at right
            m "But no, they had a demo in store so i tried it out but i don't think it's my kind of game."
        "Was it 'Something' Humans?":
            show melissa happy at right
            m "Ha ha ha. You remembered."
            m "It actually was."
            show melissa skeptic at right
            m "Well sort of."
            hide sam
            show sam skeptic at left
            s "Sort of?"
            show melissa embarrassed at right
            m "Yeah I wanted to get the same one my cousin had, but I couldn't remember the name."
            m "And when I got there, there were two 'Something' Human games. But apparently, I picked the wrong one."
            hide sam
            show sam happy at left
            s "Ha ha ha ha."
            show melissa dull at right
            m "Hey don't laugh. But actually this one is pretty fun too, so it worked out in the end I guess."
            s "So which one did you get?"
            show melissa embarrassed at right
            m "..."
            hide sam
            show sam skeptic at left
            s "Still don't remember the name?"
            m "...no."
            hide sam
            show sam happy at left
            s "Haha."
            show melissa dull at right
            m "Shush."
            $iPoints +=1
        "Was it Call of Boo-ty: Modern Scarefare 3?":
            m "What's that?"
            hide sam
            show sam skeptic at left
            s "It's a boo-t em up."
            show melissa sad at right
            m "Oh I don't really like those, my cousin had a few but all the screen shaking gave me a headache."
            
    #medusa says she has to go soon.
    show melissa happy at right
    m "Well its been fun hanging out with you guys, but I've got to head back."
    show melissa content at right
    m "Its especially nice to hear you talking so much Sam."
    
    hide sam
    show sam embarrassed at left
    s "Wait..."
    show melissa happy at right
    m "Hmm?"
    hide gor
    show gor skeptic at left
    g "Go for it, Sam."
    hide leo
    show leo skeptic at left
    l "You can do it, Sammy."
    
    #Ask her out?
    #choice -Yes of course (pluck up the courage)
    #choice -ill try another day (Fail to get)
    menu:
        "Should I ask her out?"
        "(Hell yes!)":
            hide sam
            show sam embarrassed at left
            s "Melissa."
            show melissa happy at right
            m "Yes?"
            s "W-Will you got out with me?"
            show melissa embarrassed at right
            m "Like a date?"
            s "Y-Yes."
            show melissa dull at right
            m "Hmm..."
        "(I'll try another day)":
            jump lbl_MatchMaker_Snake_GoHome    
    
    #ask her out
    if (iPoints > 5):
        show melissa content at right
        m "I'd be happy to."
        hide sam
        show sam love at left
        s "Yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
        hide gor
        show gor skeptic at left
        g "I think he's happy."
        hide leo
        show leo skeptic at left
        l "Ahahahaha. Good job hanging in there Sam."
        #She agrees to go out with Sam the coming weekend
        hide sam
        show sam happy at left
        show melissa happy at right
        m "I still have to focus on on my training for the upcoming race, but after that I'll be free."
        m "So the weekend after next? If you're free."
        hide sam
        show sam love at left
        s "I-I'm always free!"
        show melissa content at right
        m "Haha, well OK then. Its a date."
        hide gor
        show gor happy at left
        g "Well we better be off."
        show melissa content at right
        m "Okay, goodbye then."
        g "Bye Melissa."
        hide leo
        show leo excited at left
        l "Bye!"
        hide sam
        show sam love at left
        s "Goodbye Melissa"
        show melissa embarrassed
        m "Goodbye Sam."
        hide melissa
        $bMatchSnake = True
    else:   
        show melissa sad at right
        m "I'm afraid I can't."
        hide sam
        show sam sad at left
        s "Y-You can't?"
        show melissa neutral at right
        m "No, with the match coming up I can't afford to be distracted right now."
        m "I'm sorry."
        hide sam
        show sam dull at left
        s "I-It's OK. I understand what you're saying."
        hide gor
        show gor dull at left
        g "Sam..."
        hide leo
        show leo dull at left
        l "..."
        s "Let's go home, guys."
    jump lbl_MatchMaker_Snake_End

label lbl_MatchMaker_Snake_GoHome:

    hide sam
    show sam dull at left
    s "..."
    show melissa happy at right
    m "..."
    hide leo
    show leo dull at left
    l "..."
    hide gor
    show gor dull at left
    g "..."
    g "Well we better be off."
    show melissa dull at right
    m "Okay, see you again sometime."
    hide sam
    show sam dull at left
    s "..."
    hide sam
    show sam sad at left
    s "I-I messed up didn't I?"
    hide gor
    show gor dull at left
    g "A little, yeah."
    hide leo
    show leo dull at left
    l "There there Sammy."
    hide sam
    show sam sad at left
    s "Let's go home, guys."
    jump lbl_MatchMaker_Snake_End
    
label lbl_MatchMaker_Snake_End:
    jump lbl_Ending
    
label lbl_Ending:
    scene bg home day with fade
    play music music_home fadein 1.0
    #$ renpy.transition(slow_dissolve, layer="master")
    show ChimeraBase at left
    show leo happy at left
    show gor happy at left
    show sam happy at left
    
    s "So to summarise..." 
    if (bMatchLion == True):
        hide leo
        show leo love at left
        s "Leon is together with Persephone"
    else:
        hide leo
        show leo sad at left
        s "Leon is alone."
        
    if (bMatchGoat == True):   
        hide gor 
        show gor love at left
        s "Gordon is together with Helen" 
    else:
        hide gor
        show gor sad at left
        s "Gordon is on his own" 
        
    if (bMatchSnake == True):
        hide sam
        show sam love at left
        s "I am together with Melissa" 
    else:
        hide sam
        show sam sad at left
        s "I don't have anyone." 
    
    if ((bMatchLion == True) and (bMatchGoat == True) and (bMatchSnake == True)):
        s "Looks like everything went according to plan."
        jump lbl_GOODEND
    else:
        s "Looks like I messed up somewhere."
        jump lbl_BADEND

label lbl_GOODEND:
    scene GOOD_END with fade
    s "And so everyone got someone of their own to be with." 
    s "Time for us to make triple dates a thing." 
    stop music
    play sound sound_transition_happy
    "GOOD END"
    $persistent.bonus_unlocked = True
    "(Bonus chapter unlocked)"
    jump end

label lbl_BADEND:   
    scene bg black with fade
    s "And so I ended up spending the rest of my life alone." 
    s "Well as alone as one can be while attached to two others..."
    stop music
    play sound sound_transition_sad
    "BAD END"
    $persistent.bonus_unlocked = True
    "(Bonus chapter unlocked)"
    jump end 

 
label end: 
    return
    
    
label lbl_Bonus:
    scene bg library day with fade
    play music music_library fadein 1.0
    #$ renpy.transition(slow_dissolve, layer="master")
    if ( not persistent.bonus_unlocked):
        "It seems there's nobody here..."
        "(Come back after completing the game to learn more about the monsters that appear in it.)"
        return
    "Teach me, Miss Melissa~"
    show melissa happy at left
    show melissa happy at left
    m "Ok, be seated class. Today we are going to be learning about different monsters."
    show melissa skeptic at left
    m "What monsters?"
    show melissa happy at left
    m "Well the ones that appear in this particular story of course."
    show melissa dull at left
    m "So what would you like to hear about first?"

label lbl_learn_menu:
    show melissa happy at left
    menu:
        "What's a Chimera?":
            jump lbl_learn_chimera
        "What's a Harpy":
            jump lbl_learn_harpy
        "What's a Medusa?":
            jump lbl_learn_medusa
        "What's a Cyclops?":
            jump lbl_learn_cyclops
        "What's a Human?":
            jump lbl_learn_human
        "I think I've learned enough":
            jump lbl_learn_end
    return

label lbl_learn_chimera:
    show melissa dull at left
    m "Hmm... I'm not really sure. Let's consult the manual."
    show melissa happy at left
    m "The Chimera was, according to Greek mythology, a monstrous fire-breathing hybrid creature, composed of the parts of three animals – a lion, a snake, and a goat."
    show melissa sad at left 
    m "...sounds scary."
    show melissa happy at left
    m "Thankfully our own Chimera isn't nearly as scary sounding as that."
    m "Oh here they are now"
    show ChimeraBase at right
    show leo happy at right
    show gor happy at right
    show sam happy at right
    m "Ok, let's count the heads to see if the book was correct."
    m "1... The Lion, Leonardo"
    hide leo
    show leo excited at right
    l "Hi!"
    m "2... The Goat, Gordon"
    hide gor
    show gor happy at right
    g "Hello Melissa."
    m "3... The Snake, Samuel"
    hide sam
    show sam embarrassed at right
    s "Hi Melissa."
    
    show melissa content at left
    m "Yes, it seems the book was correct. 3 heads."
    show melissa dull at left
    m "But I have an important question, guys."
    s "What is it?"
    show melissa skeptic at left
    m "C-Can you really breathe fire?"
    hide leo
    show leo skeptic at right
    l "Er...I dunno, can we?"
    hide sam
    show sam dull at right
    s "Why are you asking me?"
    hide gor
    show gor dull at right
    g "I cant say that I've tried it before."
    m "..."
    hide sam
    show sam skeptic at right
    show melissa happy at left
    s "...Maybe we should try it now?"
    show leo happy at right
    show gor happy at right
    show sam happy at right
    hide leo
    show leo happy at right
    l "...haaa"
    hide gor
    show gor happy at right
    g "...paaa"
    hide sam
    show sam happy at right
    s "...saaa"
    
    show melissa skeptic at left
    m "Well it looks like this might take a while so why don't we move on?"  
    hide ChimeraBase 
    hide leo 
    hide gor 
    hide sam 
    jump lbl_learn_menu
    
label lbl_learn_medusa:
    show melissa embarrassed
    m "Medusa? You want to learn more about me?"
    show melissa content
    m "I'm flattered~"
    m "I mean I could talk about myself all day long, but I'm kind of curious what the Manual says about me..."
    show melissa happy
    m "In Greek mythology, Medusa was a monster, a Gorgon, generally described as having the face of a hideous human female with living venomous snakes in place of hair."
    m "Gazing directly into her eyes would turn onlookers to stone."
    show melissa mad
    m "Whoa whoa. It says I'm hideous?!"
    m "I'm cute as a frigging button. I need to find out who wrote this book and give them a piece of my mind."
    show melissa pissed
    m "Maybe ill turn them to stone!"
    show melissa dull 
    m "...wait, I don't think I can do that in real life."
    show melissa skeptic
    m "Bah, this book sucks."
    
    m "Anyway, let's move on kids."
    jump lbl_learn_menu
    
label lbl_learn_harpy:
    show melissa happy 
    m "Ahh the new girl, what was her name? Oh right, Helen."
    m "The Trusty Manual says..."
    m "In Greek mythology, harpies were female monsters in the form of birds with human faces. They steal food from their victims while they are eating and carry evildoers away. Their name means 'snatchers'."
    show melissa skeptic 
    m "I guess I need to be careful of my lunch when Helen is around."
    show helen happy at right
    h "Did someone say my name?"
    show melissa happy
    m "Oh hi Helen."
    h "Hi Melissa."
    show melissa dull 
    m "You can't have my food."
    show helen neutral
    h "What?"
    show melissa skeptic 
    m "I'm keeping it."
    h "...what?"
    m "..."
    h "..."
    show melissa dull 
    m "Ok, I'll share some with you later."
    show helen dull
    h "I have no idea what's going on."
    
    show melissa skeptic 
    m "You'll have to come back later though, it's not lunchtime yet."
    show helen skeptic
    h "...Okaaay."
    hide helen
    jump lbl_learn_menu
    
label lbl_learn_cyclops:
    show melissa skeptic 
    m "Wait is there even one of those in this?"
    show melissa happy 
    m "Oh right, the shopkeeper. You guys don't miss a beat, do you?"
    m "Anyways the Manual says..."
    m "A Cyclops, in Greek mythology, was a member of a primordial race of giants, each with a single eye in the middle of his forehead."
    show melissa skeptic 
    m "I wonder if it makes it hard for them to judge distance since they'd have no depth perception..."
    m "Oh I asked the shopkeeper if he'd pop over for this, but apparently, he's busy selling games or something."
    m "He's not that important anyway so don't worry about it."
    show melissa happy 
    m "So what next?"
    jump lbl_learn_menu

label lbl_learn_human:
    m "A human?"
    show melissa skeptic 
    m "I don't need to consult the Manual this time. Everyone knows those don't exist."
    show pea happy at right
    p "What doesn't exist?"
    show melissa neutral 
    m "AHHHH!!!"
    hide melissa
    show pea neutral 
    p "..."
    show pea sad 
    p "Was it something I said?"
    p "..."
    show pea dull 
    p "I better get back, Father will get worried."
    hide pea
    m "..."
    m "...is it gone?"
    show melissa skeptic at left
    m "Who'd have thought they were actually real."
    
    show melissa happy 
    m "So what now?"
    jump lbl_learn_menu


label lbl_learn_end:
    show melissa content 
    m "Well I hope you remember all that because it's going to be on the test."
    m "Class dismissed."
    
    return