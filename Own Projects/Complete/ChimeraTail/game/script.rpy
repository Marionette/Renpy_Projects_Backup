# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init:
    image bg forest day = "img/bg_forest_day2.png"
    image bg shop day = "img/bg_shop_day2.png"
    image bg home day = "img/bg_home_day2.png"
    image bg street day = "img/bg_street_day2.png"
    image bg bakery day = "img/bg_bakery_day2.png"
    image bg lake day = "img/bg_lake_day2.png"
    image bg library day = "img/bg_library_day2.png"
    image bg black = Solid("#000000")
    image GOOD_END = "img/GOOD_END.png"
    
    $bLionHelped = False
    $bGoatHelped = False
    $bMatchLion = False
    $bMatchGoat = False
    $bMatchSnake = False
    
    $iPoints = 0
    $bMarrage = False
    $bBakery = False
    $iMovie = 0
    
    # Declare characters used by this game.
    define s = Character('Samuel', color="#c8ffc8", window_left_padding=140, image="Chimera")
    define l = Character('Leonardo', color="#c8ffc8", window_left_padding=140, image="Chimera")
    define g = Character('Gordon', color="#c8ffc8", window_left_padding=140, image="Chimera")
    define m = Character('Melissa', color="#c8ffc8", window_left_padding=140, image="medusa")
    define h = Character('Helen', color="#c8ffc8", window_left_padding=140, image="harpy")
    define p = Character('Persephone', color="#c8ffc8", window_left_padding=140, image="human")
    define shopkeep = Character('Shopkeeper', color="#c8ffc8", window_left_padding=140, image="shopkeep")
    define f = Character('The Father', color="#c8ffc8", window_left_padding=140, image="father")
    
    image Chimera Sam happy = "img/Chimera_snakeL.png"
    image Chimera Sam love = "img/Chimera_snakeL.png"
    image Chimera Sam mad = "img/Chimera_snakeL.png"
    image Chimera Sam awe = "img/Chimera_snakeL.png"
    image Chimera Sam cry = "img/Chimera_snakeL.png"
    image Chimera Sam embarassed = "img/Chimera_snakeL.png"
    image Chimera Sam shock = "img/Chimera_snakeL.png"
    
    image Chimera Sam2 happy = "img/Chimera_snakeG.png"
    image Chimera Leo happy = "img/Chimera_lion.png"
    image Chimera Leo sleep = "img/Chimera_lion.png"
    image Chimera Leo cry = "img/Chimera_lion.png"
    image Chimera Gor happy = "img/Chimera_goat.png"
    image Chimera Gor sleep = "img/Chimera_goat.png"
    image Chimera Gor cry = "img/Chimera_goat.png"
    
    image medusa happy = "img/Medusa_happy.png"
    image harpy happy = "img/Harpy_happy.png"
    image human happy = "img/Human_happy.png"
    image photo medusa = im.FactorScale("img/Medusa_photo.png", .8, .8)
    image shopkeep happy = "img/cyclops_happy.png"
    image father happy = "img/father_happy.png"
    image father mad = "img/father_mad.png"

    image side Chimera Sam happy = "img/SideImage_snake_happy.png"
    image side Chimera Sam love = "img/SideImage_snake_love.png"
    image side Chimera Sam mad = "img/SideImage_snake_mad.png"
    image side Chimera Sam awe = "img/SideImage_snake_awe.png"
    image side Chimera Sam cry = "img/SideImage_snake_cry.png"
    image side Chimera Sam embarassed = "img/SideImage_snake_embarassed.png"
    image side Chimera Sam shock = "img/SideImage_snake_shock.png"
    
    image side Chimera Sam2 happy = "img/SideImage_snake_happy.png"
    image side Chimera Leo happy = "img/SideImage_lion_happy.png"
    image side Chimera Leo sleep = "img/SideImage_lion_sleep.png"
    image side Chimera Leo cry = "img/SideImage_lion_sleep.png"
    image side Chimera Gor happy = "img/SideImage_goat_happy.png"
    image side Chimera Gor sleep = "img/SideImage_goat_sleep.png"
    image side Chimera Gor cry = "img/SideImage_goat_sleep.png"
    image side medusa happy = "img/SideImage_medusa_happy.png"
    image side harpy happy = "img/SideImage_harpy_happy.png"
    image side human happy = "img/SideImage_human_happy.png"
    image side father happy = "img/SideImage_father_happy.png"
    image side father mad = "img/SideImage_father_mad.png"
    image side shopkeep happy = "img/SideImage_cyclops_happy.png"

#----------------------------------------------------------------------
#----------------------------------------------------------------------

# The game starts here.
label start:
    play music "audio/Enchanted_Valley.ogg"
    $bLionHelped = False
    $bGoatHelped = False
    
#----------------------------------------------------------------------
#----------------------------------------------------------------------
label lbl_introductions:
    scene bg forest day
    show Chimera Sam happy 
    s Sam happy "So, What do you think of my plan?"
    s Sam happy "..."
    s Sam happy "Guys?"
    l Leo sleep "..."
    g Gor sleep"..."
    s Sam mad "Oh they're sleeping. Typical."
    
    s Sam happy "Well hello there. This is me. Samuel, or Sam if you'd prefer. I'm 1/3 of this particular chimera."
    s Sam cry "Its not easy being me. I mean when you think of a chimera, you always think of the lion head, or maybe even the goat head. Never the tail. I'm always an afterthought."
    s Sam happy "Heck if you had been shocked that I was even alive you wouldn't be the first."
    s Sam happy "But anyway. Enough moaning. What this snake is really interested in is..."
    s Sam embarassed " Well its kind of embarrassing to say..."
    g Gor happy "..."
    s Sam embarassed "...Its love. I'm in love. Yes, shocking I know. "
    show Chimera Sam happy at left
    show photo medusa at right
    s Sam love "This is the object of my affections. "
    s Sam love "Her name is Melissa, she's basically the perfect girl."
    g Gor happy "..."
    s Sam awe "Those beautiful eyes..."
    s Sam awe "That cute smile..."
    s Sam awe "Those smooth scales and that slithering hair..."
    s Sam love "Just thinking about her makes me go all fuzzy inside."
    g Gor happy "Who are you talking to?"
    hide photo
    s Sam shock "AHH! Y-You're awake."
    s Sam embarassed "I-I didn't realise I was saying that all out loud."
    g Gor happy "Yeeeeaaaaah."
    
    s Sam happy "Annnyway. How much of my plan do you remember hearing before falling asleep?"
    g Gor happy "..."
    g Gor happy "What plan?"
    s Sam mad"..."
    s Sam happy "You know what? Never mind."
    l Leo happy "GUYS!"
    s Sam shock "Waaah!"
    l Leo happy "Guys. I just had. The weirdest dream. Like seriously."
    l Leo happy "I mean there was this shark, only like it was huge. And we were like riding on its back."
    g Gor happy "We were riding a shark?"
    l Leo happy "Yeah, only like, it was flying. And that girl was there too."
    g Gor happy "Who?"
    s Sam happy "Girl?"
    l Leo happy "I er, never mind that's not important. Then the shark exploded and when I woke up in the dream Sammy was droning on and on about something boring so I went back to sleep."
    s Sam mad "...I don't think that was the dream"
    l Leo happy "but the shark didn't come back so I woke up again, only for real this time."
    s Sam happy "That's so strange."
    l Leo happy "Yeah, I thought for sure it'd come back."
    s Sam happy "Er that's not really what I meant..."
    g Gor happy "By the way guys, weren't we supposed to be somewhere by now?"
    l Leo happy "We were?"
    s Sam happy "Aww nuts. We need to hurry or they'll be sold out."
    
    
label lbl_intro_shopping:
    scene bg shop day
    ""
    show Chimera Sam happy at left
    s Sam happy "Finally we're here!"
    l Leo happy "..."
    g Gor happy "..."
    s Sam happy "We still need to hurry or the new Pocket Humans game will be old out!"
    l Leo happy "Its easy...for you...you never...do any of...the running."
    g Gor happy "..."
    s Sam happy "Hey! I help us...er steer."
    
    s Sam happy "Anyway lets get in there."
    "*BUMP*"
    h "HEY!"
    h "Watch where you're going you big oaf!"
    g Gor happy "How about you wat..."
    
    show harpy happy at right
    g Gor happy "..." 
    g Gor happy "..I mean, Pardon us." 
    g Gor happy "I hope you're not hurt."
    h happy "W-Well I guess I'm OK."
    
    
    s Sam happy "I haven't seen her around here before..."
    
    menu:
        "Should i talk to her?"
        "Are you new here?":
            jump lbl_shop_harpy
        "I dont have time for chit chat!":
            hide harpy
            jump lbl_shop_game
            
label lbl_shop_harpy:
    $bBakery = True
    g Gor happy "..."
    s Sam happy "I haven't seen you around, are you new here?"
    h "What? I don't work here."
    s Sam happy "No I mean in the area."
    h "I don't work in the area either."
    s Sam happy "I'm not asking about your job, I'm asking about you."
    h "What about me?"
    g Gor happy "..."
    s Sam happy "Did you move here."
    h "To the store?"
    s Sam happy "The area."
    h "OOOOh you mean did I move to town. "
    s Sam happy "Yeah, that's what I meant."
    g Gor happy "..."
    h "Then yeah, we moved here from back home."
    s Sam happy "We?"
    h "Yeah me and my parents. They run the new bakery on the other side of town."
    l Leo happy "I LOVE CAKE!"
    h "Whoa!"
    g Gor happy "..."
    s Sam happy "Sorry about him. He's gets excited easily. Its true though, he really does. One time he ate so much all three of us got sick. "
    h "Haha you guys are strange."
    s Sam happy "Well we try. "
    h "Well I gotta get going. I should be back at the bakery by now. "
    s Sam happy "See you again sometime."
    h "Bye~"
    hide harpy
    g Gor happy "..."
    s Sam happy "..."
    s Sam happy "Gor you're being awful quiet."
    g Gor happy "I-It's n-nothing."
    s Sam happy "I'm sure it is."
    s Sam happy "Crap! I forgot the game."
    jump lbl_shop_nogame
    
label lbl_shop_nogame:
    #chat with harpy - get info 
    s Sam happy "We want to buy a copy of Pocket Humans!"
    show shopkeep happy at right
    shopkeep "Sorry I just sold the last copy. And it'll probably be a while before we can get more stock."
    s Sam cry "Noooooooo..."
    l Leo cry "...ooooooooo..."
    g Gor cry "...ooooooooo"
    shopkeep happy "I still have a copy of the Digital Humans game though if you're interested."
    l Leo happy"Yeah, you still have it because nobody wants to play it. "
    g Gor happy "Well actually..."
    s Sam happy "Well something is better than nothing I guess."
    hide shopkeep
    jump lbl_shop_medusa
    
label lbl_shop_game:
    #rush into store - get game
    s Sam happy "We don't have time for chit chat! Lets go!"
    s Sam happy "We want to buy a copy of Pocket Humans!"
    show shopkeep happy at right
    shopkeep happy "Lucky you, here's the last copy."
    s Sam happy "AWESOME!"
    l Leo happy "YES!"
    g Gor happy "WHOOO!"
    s Sam happy "We got it, and the last copy too. Its a good thing we ran here after all."
    l Leo happy "You mean good that we ran."
    s Sam happy "Dont sweat the small stuff."
    l Leo happy "Dibs on first go."
    s Sam happy "...nuts. I wanted to go first."
    g Gor happy "Seconds!"
    s Sam happy "Aw for flips sakes."
    l Leo happy "Ha ha looks like sammy takes up the rear as always. "
    s Sam happy "Life is so unfair sometimes."
    hide shopkeep
    jump lbl_shop_medusa

label lbl_shop_medusa:
    s Sam happy "Ok lets go home and try it out then."
    s Sam happy "*BUMP*"
    m "Oh my, im so sorry"
    s Sam happy "No, its our fa..."
    show medusa happy at right
    s Sam shock "(OMG ITS HER! OHSHITSHITSHIT! WHAT DO I DO NOW?)"
    m "Oh its you guys. Hi~"
    s Sam happy "..."
    g Gor happy "Hello there."
    m "Oh you dropped something, Is it that something humans game everyone is raving about?"
    s Sam happy "..."
    l Leo happy "We're just heading home to play it now!"
    s Sam happy "(Speak up dammit!)"
    m "Well have fun with that."
    l Leo happy "See ya."
    g Gor happy "Goodbye"
    m "Bye~"
    
label lbl_shop_menu:
    menu:
        "(Say somthing dammit!)"
        "I LOVE YOU MELISSA!":
            s Sam mad "(Yeah right. If I could say that there would be no need for this game.)"
            jump lbl_shop_menu
        "Will you go out on a date with me sometime?":
            s Sam mad "(Yeah right. If I could say that there would be no need for this game.)"
            jump lbl_shop_menu
        "...bye.":
            s Sam cry "(Sigh. What is wrong with me?)"
    
    #meet Medusa at counter
    #get dragged away
    s Sam happy "Lets just go home."
    l Leo happy "I can't wait to play~"
    g Gor happy "Yeah its getting late, lets go."
    jump lbl_home
    
    #go to sleep
   
label lbl_home:
    scene bg home day
    ""
    show Chimera Sam happy at left
    l Leo happy "Time to play this~."
    g Gor happy "I'll just read a book then."
    s Sam happy "I think I'm just going to go to sleep now."
    l Leo happy "Ha ha, Sammy's mad that he couldn't talk to his giiiirrrrllllfriend~"
    g Gor happy "Again."
    s Sam happy "S-Shut up you two!"
    s Sam happy "(But he hit the mark. Why am I fine in any other situation, but as soon as she appears it's like I lose the ability to speak.)"
    s Sam happy "(I just never know what to say to her. Maybe I need to get these guys to help me out.)"
    s Sam happy "(I guess ill ask in the morning...)"
    
    scene bg black
    jump lbl_morning

#----------------------------------------------------------------------
#----------------------------------------------------------------------

label lbl_morning:
    #wake up
    "Beep beep beep"
    s Sam happy "Mmmm its morning already?"
    scene bg home day
    show Chimera Sam happy at left
    l Leo happy "Umm...no don't...bring her back..."
    s Sam happy "Looks like Leo is talking in his sleep again. Wonder what he's dreaming about?"
    g Gor happy "Probably something weird like always."
    s Sam happy "Oh you're awake, Morning."
    g Gor happy "Good morning Sam."
    l Leo happy "Mumble...mumble...DAMN YOU SHARK!"
    s Sam happy "..."
    g Gor happy "Good morning Leo."
    s Sam happy "Morning."
    s Sam happy "Bad dream?"
    l Leo happy "I dunno, it was weird."
    g Gor happy "All your dreams are weird though."
    l Leo happy "I guess you're right. Ha ha."
    
    #talk about plans
    s Sam happy "Anyway guys. I need your help with something."
    g Gor happy "What is it?"
    s Sam happy "Ok ok, you know Melissa."
    l Leo happy "Your giiiirrrrllllfriend?"
    s Sam happy "..."
    s Sam happy "I want to ask her out on a date."
    g Gor happy "And?"
    s Sam happy "Well you've seen how I get around her. "
    s Sam happy "I need you guys to like prompt me when I'm talking to her so I don't just sit there with my foot in my mouth the whole time."
    l Leo happy "You don't have feet though?"
    s Sam happy "I mean i just need to guys to say something to me if I start to clam up while talking to her. To keep the conversation flowing until I'm able to ask her out."
    l Leo happy "Sounds easy, OK."
    g Gor happy "Well actually..."
    
    s Sam happy "Gordon?"
    
    g Gor happy "I wouldn't want to mess it up."
    s Sam happy "Mess it up? That's not like you."
    g Gor happy "I don't know what's wrong with me, but ever since yesterday I cant think straight."
    s Sam happy "...yesterday?"
    g Gor happy "That harpy we bumped into yesterday. I can't get her out of my mind."
    g Gor happy "I've no idea why but suddenly I find that everything reminds me of her."
    
    s Sam happy "Hmmm..."
    s Sam happy "Ok, how about this. If I help you with your problem then you're mind will be at ease and you'll be able to help me, right?"
    g Gor happy "Well I guess that makes sense, but how?"
    s Sam happy "I think I have an idea."
    
    l Leo happy "Oh now that you mention it."
    s Sam happy "Hmm?"
    l Leo happy "I have something you can help with too. If you want my help that is."    
    s Sam happy "What but you already..."
    l Leo happy "What was before you were offering help as well."
    s Sam happy "But..."
    l Leo happy "I've already decided."
    s Sam happy "Aww for flips sakes."
    s Sam happy "OK, then ill help both of you."
    s Sam happy "But then you guys have to help me. Deal?"
    l Leo happy "Deal."
    g Gor happy "Deal."
    s Sam happy "Well then lets get started right away."
    jump lbl_MatchMaker_Choice
    
    #offer to help the others with something in exchange for their help
    #gor asks for help with harpy
    #leo asks for advice
    
label lbl_day_end:
    jump lbl_MatchMaker_Choice
    
    
label lbl_MatchMaker_Choice:
    scene bg home day
    show Chimera Sam happy at left
    s Sam happy "So what should I do now?"
    menu:
        "So what should I do now?"
        "Lets help Leon!" if (bLionHelped == False):
            call lbl_MatchMaker_Lion
        "Lets help Gordon!" if (bGoatHelped == False):
            call lbl_MatchMaker_Goat
        "I think its time to help myself":
            jump lbl_MatchMaker_Snake
        
    jump lbl_MatchMaker_Choice
    
#----------------------------------------------------------------------
#----------------------------------------------------------------------

label lbl_MatchMaker_Lion:
    $bLionHelped = True
    $iPoints = 0
    s Sam happy "I guess im helping Leon then."
    
    #leo asks about girls
    s Sam happy "So leo, er how can i help you?"
    l Leo happy "Well i guess what i really want is to ask you a few things."
    
    l Leo happy "You know Melissa?"
    s Sam happy "Y-Yeah?"
    l Leo happy "When you see her how does it make you feel?"
    menu:
        "How does seeing Melissa make me feel?"
        "Like my chest is going to explode":
            $iPoints +=1
        "Like i might throw up at any second":
            $iPoints +=1
        "Makes me want to punch her in the face!":
            $iPoints +=0
        "I don't feel anything.":
            $iPoints +=0
        
    l Leo happy "Hmm."
    
    l Leo happy "What about when you think of you both together"
    menu:
        "The thought of me and Melissa together?"
        "I want to cry":
            $iPoints +=0
        "BE STILL MY HEART!":
            $iPoints +=1
        "No reaction.":
            $iPoints +=0
        
    l Leo happy "Hmm, i see."
    s Sam happy "Why do you ask?"
    
    l Leo happy "Wait one more question."
    l Leo happy "When you think about Melissa and the Future what comes to mind most often?"
    
    menu:
        "What comes to mind when I think of Melissa and the future"
        "How many others would be in my harem by then!":
            $iPoints +=0
            l Leo happy "What's a harem?"
            g Gor happy "Y-You don't need to know that Leo."
        "How our wedding will be!":
            $iPoints +=1
        "What other girl ill have at that point!":
            $iPoints +=0
        "What our kids will look like!":
            $iPoints +=1
        
    
    l Leo happy "OK, I think that's enough."
    s Sam happy "So are you going to explain what the questions were for?"
    s Sam happy "I thought you wanted me to help you."
    
    l Leo happy "I just wanted to see if what I was feeling was the same as what you are"
    s Sam happy "And is it?"
    if (iPoints == 3):
        l Leo happy "Yes. Its a perfect match!"
    if (iPoints == 2):
        l Leo happy "Eh... close enough."
    if (iPoints < 2):
        l Leo happy "Nah, seems like its something different."
        jump lbl_Lion_noMatch
    jump lbl_Lion_Match    
        
    
label lbl_Lion_noMatch:
    s Sam happy "Will I still be able to help?"
    l Leo happy "Nah its ok, you've helped enough, I know what I have is something different so ill just deal with it on my own at some point."
    jump lbl_day_end
    
label lbl_Lion_Match:
    #leo asks about asking out on a date
    s Sam happy "So what now?"
    l Leo happy "Ok, now for the bonus question~"
    s Sam happy "More questions?"
    l Leo happy "This is the last one for reals."
    s Sam happy "Ok, hit me."
    l Leo happy "Ok, when you see Melissa what is it you want to ask her and why?"
    
label lbl_Lion_Match_menu:
    menu:
        "What is it I want to ask Melissa?"
        "Will you Lend me some money?":
            s Sam happy "You know, because I'm broke."
            g Gor happy "Come on Sam, take this seriously."
            jump lbl_Lion_Match_menu
        "Will you marry me?!":
            $bMarrage = True
            s Sam happy "So we can spend the rest of our lives together."
        "Will you go out on a date with me?":
            s Sam happy "So we can get to know one another better."
       
    #Leo asks if you'll back him up
    l Leo happy "OK I think I have enough information. Thanks guys."
    s Sam happy "No problem."
    s Sam happy "So are you going to tell us who it is you fancy?"
    
    l Leo happy "You'll find out when we get there."
    s Sam happy "Gor, do you know who it is?"
    g Gor happy "I think I have a fair idea."
    s Sam happy "How come I never noticed anything before?"
    g Gor happy "Probably because all you ever think about is that Medusa."
    s Sam happy "...oh. (I guess its true, I'm always so wrapped up in my own problems that i never really think about theirs.) "
    g Gor happy "Ha Ha, don't worry about it. I think you've helped him out considerably with this."
    g Gor happy "He's never been the sharpest claw in the paw after all, so he needs a little push every now and then."
    g Gor happy "Anyway, you'll see one way or another soon enough."
    
label lbl_Lion_Date:
    $iPoints = 3
    scene bg street day
    show Chimera Leo happy at left
    
    #leo asks Persephone
    show human happy at right
    p "Oh hello there guys, heading out?"
    s Sam happy "Oh hi Persephone. "
    s Sam happy "(Persephone is our neighbour, she's been around here almost as long as we have. Which is strange considering that she's a Human. They don't often settle near monsters like us.)"
    g Gor happy "Hello there."
    p "Oh yeah Leo. I got something for you."
    l Leo happy "A fish?"
    l Leo happy "Awesome!"
    p "Who's a good kitty?"
    s Sam happy "(Is she rubbing his chin? What a strange person.)"
    l Leo happy "Prrrr. No wait."
    l Leo happy "Persephone. There's something I want to ask you."
    s Sam happy "(Wait, its her?!)"
    p "Ask me? What is it?"
    
    p "Persephone..."
    
    if (bMarrage == True):
        l Leo happy "Will you marry me?"
        s Sam happy "W-W-W-WHAT?!"
        g Gor happy "..."
        s Sam happy "T-That's not what I meant when I..."
        
    if (bMarrage == False):
        l Leo happy "Will you go out on a date with me?"
    
    s Sam happy "So that's why you were asking."
    s Sam happy "You had feeling for Persephone but weren't sure what they were or what to do about them."
    
    g Gor happy "Well for now lets see how this pans out."
    
    #Persephone agrees
    p "Hmmmm..."
    l Leo happy "..."
    g Gor happy "..."
    s Sam happy "..."
    p "OK~"
    
    s Sam happy "W-What?!"
    l Leo happy "She said yes!"
    g Gor happy "Good for you Leo."
    
    if (bMarrage == True):
        p "But lets start with a date first, OK?"
        l Leo happy "Okay~"
    
    s Sam happy "Well that was easy. I guess this like this happen too. Maybe I shouldn't be so nervous about asking Melissa?"
    #cheers . ... but wait
    #Persephone gives a condition
    p "But, there is one small thing..."
    s Sam happy "What is it?"
    p "You have to convince my father to allow it."
    
    # per says they have to convince her father to allow it
    g Gor happy "Y-Your father?"
    l Leo happy "Y-You mean the big scary guy who lives in the same house as you?"
    s Sam happy "(The reason you don't see many humans near monsters is because they fear us. But not this one. They say killed a Minotaur with his bare hands!)"
    p "Yes, unfortunately he's very protective and wont allow me to do anything without his permission."
    s Sam happy "And you just listen to him?"
    p "Its a little stifling but I know he does it because he's worried about me, and I love him so its only right that I follow his wishes."
    
    p "U-Unless you have changed your mind about us..."
    l Leo happy "N-No. O-Of course not. I-I'll convince him!"
    p "Perfect~ Ill go get him now, he's in the house."
    l Leo happy "W-What?! R-Right now?"
    
    #per says he's on his way
    l Leo happy "What should I do?"
    menu:
        "What should Leo do?"
        "Man up Leo, its now or never!":
            jump lbl_Lion_Fight
        "He who runs away lives to fight another day.":
            jump lbl_Lion_Run
        
label lbl_Lion_Run:
    l Leo happy "You're right Sammy."
    l Leo happy "I-I'll come back when im more prepared."
    s Sam happy "Yeah lets get out of here before we get killed."
    jump lbl_MatchMaker_Lion_End

label lbl_Lion_Fight:
    s Sam happy "I-I guess you're right. If i want this i have to face the music."
    g Gor happy "Well said."
    s Sam happy "(At least if we die we'll die together.)"
    p "Hi guys. He's on his way out. Said he had to get his helmet or something."
    s Sam happy "Ohshi.."
    g Gor happy "Preparing for a fight?"
    s Sam happy "W-What should I do?"
    
    #choice -just be yourself leo
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
    f "Ahem!"
    hide human
    show human happy
    show father mad at right
    f "So which one is it?"
    p "This one father"
    #greetings
    l Leo happy "Y-Yeah, its me. Hello there."
    
    #he doesnt like leo
    f "I dont like him."
    s Sam happy "*Gulp*"
    
    #perservere
    if (iOption==1):
        $iPoints+=1
        l Leo happy "Yes sir, i agree!"
        s Sam happy "(W-What is he saying?!)"
        f "You...You agree? You mean you don't like me either?"
        l Leo happy "Yes sir!"
        f "Heh, well at least he's got some balls."
    if (iOption==2):
        l Leo happy "Tch, well I don't like your face."
        s Sam happy "(W-What is he saying?!)"
        f "You really like this Jerk, Pea dear?"
        p "H-He's not normally like this I don't know what's going on."
        l Leo happy "Er Well I..."
    if (iOption==3):
        $iPoints+=2
        l Leo happy "But you don't even know me yet!"
        s Sam happy "(W-What is he saying?!)"
        f "What did you say?"
        l Leo happy "I-I said, you should get to know me better before you decide you don't like me."
        p "H-He's right father!"
        f "Quiet. This is between the two of us."
        
    #still doesnt
    #dont give up
    #he insults
    #choice -ignore it - wimp
    #choice -stand up to him - manly
    f "Ok, im going to cut to the chase here."
    f "I dont like you and i wont have my daughter taken away from me by some freakish cat with other stupid animals stuck on it."
    menu:
        "That was pretty harsh."
        "Are you going to stand for that?":
            jump lbl_Lion_noWimp
        "Just let it go, its not worth it.":
            if (iOption==3):
                l Leo happy "Yeah, I guess... No wait."
                l Leo happy "I won't let that one slide."
                jump lbl_Lion_noWimp
            jump lbl_Lion_Wimp
    
    
label lbl_Lion_Wimp:
    #if wimp father drags her away
    #calls leo a wimp
    l Leo happy "..."
    f "Thats what i thought. Come with me Pea."
    p "Leo..."
    l Leo happy "..."
    s Sam happy "..."
    g Gor happy "..."
    l Leo happy "Lets go home guys."
    jump lbl_MatchMaker_Lion_End

label lbl_Lion_noWimp:
    l Leo happy "I'm going to have to ask you to apologize."
    f "I'm sorry, what?"
    s Sam happy "(Holy crap he looks pissed now.)"
    l Leo happy "Say what you want about me, but i can't let you say things like that about the people i care about."
    s Sam happy "(He's deadly serious about this, its been a long time since I' saw Leo this worked up.)"
    f "..."
    l Leo happy "..."
    f "I apologize."
    l Leo happy "If you wont I'll hav... What?!"
    
    f "Im sorry i didn't mean to offend you or the others. "
    s Sam happy "(What is going on? I dont understand at all.)"
    #if manly father approves of the pair
    #says wants a strong guy to look after her
    show father happy
    f "I'm just so worried about my daughter you see, i had to make sure you were the sort of guy to stand up for yourself, and most of all stand up for her."
    f "Honestly I knew this day would come eventually. She talks about you a lot, and you really seem like a nice fellow."
    
    f "So now that I'm satisfied that you're not a wimp I'm not against this union."   
    f "So I guess its up to Persephone now."
    l Leo happy "So Persephone, will you by my Girlfriend?"
    
    
    if (iPoints < 5):
        p "Well actually during this I've learned some things about you I didn't know before Leo."
        p "I don't think it would work out after all, I'm sorry."
        l Leo happy "..."
        s Sam happy "Leo..."
        g Gor happy "..."
        l Leo happy "Lets just go home guys."
        jump lbl_MatchMaker_Lion_End
    
    #per decides he's good enough 
    p "Yes!"
    l Leo happy "WHOOHOO!"
    s Sam happy "Good Job Leo."
    g Gor happy "Congratulations Leo."
    p "Let me know when you've figured out where you're talking me on our first date~"
    p "Bye Leo~"
    f "Goodbye Leo, I'm sure we'll be seeing a lot of each other from now on."
    l Leo happy "Goodbye Sir."
    l Leo happy "Bye Pea~"
    
    g Gor happy "Well all well that ends well."
    l Leo happy "Yep, lets go home."
    s Sam happy "Yeah, I'm surprisingly tired after all that."
    g Gor happy "I agree, even though we weren't really involved it was still nerve-wracking."
         
    $bMatchLion = True
    
    jump lbl_MatchMaker_Lion_End    

label lbl_MatchMaker_Lion_End:
    return
    
#----------------------------------------------------------------------
#----------------------------------------------------------------------
    
label lbl_MatchMaker_Goat:
    $bGoatHelped = True
    $iPoints = 0
    s Sam happy "I guess im helping Gordon then."
    #Gordon asks for help asking Helen on a date
    g Gor happy "So about that Harpy."
    g Gor happy "What do you suggest i do?"
    
    menu:
        "What should Gordon do about the harpy?"
        "Give up on her":
            jump lbl_Goat_Giveup
        "Talk to her":
            s Sam happy "You should get to know her better and see how it goes"
            jump lbl_Goat_Talk
        "Ask her out":
            s Sam happy "It'll be a good chance to get to know her better"
            jump lbl_Goat_Talk
        
label lbl_Goat_Giveup:
    g Gor happy "Yeah maybe you're right."
    g Gor happy "I'll just try to forget her."
    jump lbl_MatchMaker_Goat_End
    
label lbl_Goat_Talk:
    g Gor happy "You're right. I need to get to know her better."
    l Leo happy "Yeah, because you don't even know her name."
    g Gor happy "Yeah, we don't know much about her at all."
    g Gor happy "How will we find her?"
    s Sam happy "I guess all we can do is look around town and hope we find her."
    if (bBakery==True):
        l Leo happy "Didn't she say something about cakes?"
        s Sam happy "No that was you Leo."
        s Sam happy "But she did mention a bakery, maybe we should check it out?"
    
    #try to use info to find her
    #look in places 
    #choice -library
    #choice -gamestore
    #choice -park
    #choice -bakery - helen here (extra points for finding her faster) 
    $iPoints = 3
label lbl_goat_locationMenu:
    menu:
        "Where should we look?"
        "Lets check the library" if (iPoints > 0):
            $iPoints -= 1
            call lbl_goat_library
        "Lets check the game store" if (iPoints > 0):
            $iPoints -= 1
            call lbl_goat_gamestore
        "lets check the park" if (iPoints > 0):
            $iPoints -= 1
            call lbl_goat_park
        "Lets check the bakery" if (bBakery==True):
            jump lbl_goat_bakery
        "Lets go home."  if (iPoints == 0):
            jump lbl_goat_home
            
    jump lbl_goat_locationMenu

label lbl_goat_home:
    scene bg home day
    show Chimera Sam happy at left
    g Gor happy "All right, lets just call it a day."
    s Sam happy "Yeah I'm tired."
    l Leo happy "I'm hungry. Lets get some cake."
    s Sam happy "Uh...why cake?"
    l Leo happy "I like cake."
    g Gor happy "You like a lot of things."
    l Leo happy "Yeah but there's a bakery across the street."
    g Gor happy "Oh, so there is. Should we go in?"
    s Sam happy "Sure, why not?"
    
    jump lbl_goat_bakery
    
label lbl_goat_library:
    scene bg library day
    show Chimera Sam happy at left
    g Gor happy "I don't think she's here."
    g Gor happy "Wait since we're here I want to see if they have that book in stock yet."
    "..."
    g Gor happy "They still don't have it."
    s Sam happy "I'd have thought you of all people wouldn't want to waste time."
    g Gor happy "Its a really good book though!"
    s Sam happy "Well its your choice."
    return
    
label lbl_goat_gamestore:
    scene bg shop day
    show Chimera Sam happy at left
    g Gor happy "I don't think she's here."
    s Sam happy "OK give me a second, I want to see if they have any new games in."
    g Gor happy "Can't we do it another time?"
    s Sam happy "We're already here, it'll only take a second."
    "..."
    s Sam happy "Ha ha, that took longer than expected. I didn't even know they were making a sequel to that one."
    return
    
label lbl_goat_park:
    scene bg forest day
    show Chimera Sam happy at left
    s Sam happy "Well its a pretty big park lets split up and look for her."
    g Gor happy "..."
    l Leo happy "..."
    s Sam happy "Come on, not even a chuckle?"
    l Leo happy "I don't get it."
    s Sam happy "(Why do i even bother?)"
    "..."
    g Gor happy "I don't think she's here."
    return
    
label lbl_goat_bakery:
    scene bg bakery day
    show Chimera Sam happy at left
    
    s Sam happy "I don't think we've been in this one before."
    g Gor happy "I don't think so."
    show harpy happy at right
    h "Welcome~"
    l Leo happy "We found her!"
    l Leo happy "Hi!"
    h "Oh its the guys from the game store."
    h "Hows it going?"
    
    #helen comments on the time (depends on how long it took to find her)
    g Gor happy "We were wondering if you have some time to talk to us?"   
    if (iPoints == 3):
        h "Well you're pretty early so sure. We dont get many customers at this time so i was getting bored anyway."
    elif (iPoints > 0):
        h "I guess theres still some time before the rush starts so sure, why not?"
    elif (iPoints == 0):
        h "Its getting pretty busy so you'll have to make it quick."
        
    h "So how can I help you"
    #convince gordon to talk to her
    
    s Sam happy "Just talk to her Gor."
    g Gor happy "I don't know what to ask. How do I start a conversation?"
    s Sam happy "Don't worry I'll give you cues."
    g Gor happy "Er first of all..."
    menu:
        "What should Gordon ask first?"
        "Her name":
            g Gor happy "Definitely a good place to start."
            pass
        "Her 3 sizes":
            l Leo happy "3 sizes?"
            g Gor happy "I-I can't ask that!"
            pass
        "What life as a baker is like":
            g Gor happy "That might be an interesting story to hear."
            l Leo happy "Or ask her what being a cake is like."
            g Gor happy "I think you should stop trying to help Leo."
            l Leo happy "Aww."
            pass
        
    h "Wait wait, before you start I just realised I don't know what to call you guys. "
    g Gor happy "Oh my Apologies, my name is Gordon."
    s Sam happy "Mine is Samuel."
    l Leo happy "I'm Leo."
    h "My Name is Helen, nice to meet you~"

    menu:
        "What should Gordon ask first?"
        "Does she work here?":
            g Gor happy "So do you work here?"
            h "Not normally, but one of the part timers called in sick so I got drafted."
            h "I wouldn't mind if I was getting paid."
            g Gor happy "You don't get paid."
            h "No, apparently getting dinner every day should be payment enough."
            g Gor happy "That's pretty harsh."
            h "Such is life i guess."
        "What is it like to fly?":
            g Gor happy "You can fly right? What's it like?"
            h "Well technically, yes I can."
            g Gor happy "Technically?"
            h "Technically."
            g Gor happy "Er what do you mean?"
            h "It's kind of embarrassing."
            g Gor happy "What is?"
            h "I don't fly much."
            g Gor happy "You don't?"
            h "No, I don't."
            s Sam happy "(Wow this girl likes to beat around the bush, doesn't she?)"
            g Gor happy "Can I ask why not."
            h "I-I'm afraid."
            g Gor happy "Afraid?"
            h "Yeah, I'm afraid of heights. Pretty shameful problem for a harpy."
            g Gor happy "I see, it must be hard for you."
            h "Y-You're not going to laugh or make fun of me?"
            g Gor happy "Why would I? It's not like being afraid of heights is that uncommon."
            s Sam happy "(I dunno, I personally want to poke fun at her now...I'm a horrible fellow, aren't I?)"
            h "I-I guess."
            h "Most people I tell certainly find it amusing. You're a strange fellow."
            g Gor happy "I-I'm sorry?"
            h "Haha, I don't mean in a bad way."
            $iPoints +=1
        "Ask about her interests":
            jump lbl_goat_AskInterests
            
    g Gor happy "What next?"
    s Sam happy "Why not ask about her interests?"

label lbl_goat_AskInterests:
    g Gor happy "So what kinds of things are you interested in?"
    
    h "Hmmm...Guess."
    g Gor happy "What?"
    h "Guess."
    g Gor happy "Guess what?"
    h "Guess my interests."
    g Gor happy "Can't you tell me?"
    h "Don't be so boring."
    g Gor happy "O-Ok"
    
    #ask about
    #choice -movies
    #choice -games
    #choice -wilderness
    #choice -flying

    menu:
        "What should Gordon suggest?"
        "Movies.":
            g Gor happy "Do you like movies?"
            h "Well it depends on the movie I guess. As long as its nothing sappy or boring I'm generally OK."
            h "Unfortunately I don't get to go as often as I like."
            g Gor happy "No? Why not."
            h "Lets just say I have a sweet tooth and a small allowance and leave it at that."
            g Gor happy "Haha. Poor girl."
            h "Hey don't laugh!"
            g Gor happy "Im sorry."
            h "Actually now that I think about it, you always look so serious, you should smile more often."
            g Gor happy "..."
            l Leo happy "Ha, he's blushing!"
            g Gor happy "S-Shut up Leo!"
            $iPoints +=1
            
        "Video Games.":
            g Gor happy "Do you like Video Games?"
            h "Bing Bong! We have a winner!"
            g Gor happy "W-What?"
            h "I love video games. Especially the Digital Human ones."
            g Gor happy "Ha ha, Sam is always telling me that nobody likes those. I think they're a lot more interesting than the Pocket Humans games. "
            g Gor happy "Being outnumbered sucks."
            s Sam happy "Pfft. Pocket Humans rules."
            h "Hahahaha. You guys crack me up."
            $iPoints +=2
        "Hiking.":
            g Gor happy "Do you like hiking and things like that?"
            h "Er not really, im more of an indoor person."
            g Gor happy "I see."
        "Flying.":
            g Gor happy "Do you like flying?"
            h "...No."
            s Sam happy "(Guess its a sore point.)"
    
    
    h "Well I guess I better get back to work now."
    g Gor happy "Well it was nice talking to you."
    h "You too Gordon."
    h "See you later guys~"
    g Gor happy "..."
    g Gor happy "Wait..."
    h "Yes?"
    #choice - ask her out to the movies
    #choice - ask her out for coffee
    menu:
        "Ask her out?"
        "Ask her out for coffee.":
            g Gor happy "Would you like to go out for coffee some time?"
            if (iPoints > 4):
                h "Hmmm...Sure why not."
                g Gor happy "Awesome!"
                l Leo happy "Good job Gor!"
                s Sam happy "Congrats."
                h "Let me know when you think of a date and time."
                g Gor happy "Okay!"
                g Gor happy "Lets go home guys."
                $bMatchGoat = True
                jump lbl_MatchMaker_Goat_End
            else:
                h "Hmm... Maybe another time. I've been really busy lately."
                g Gor happy "O-Okay, i understand."
                l Leo happy "..."
                s Sam happy "..."
                g Gor happy "Goodbye"
                h "Bye guys."
                g Gor happy "Lets go home guys."
            jump lbl_MatchMaker_Goat_End                
                
        "Ask her out to the movies.":
            jump lbl_goat_movies
        "Don't ask her out.":
            g Gor happy "N-Nevermind. "
            g Gor happy "Lets go home guys."
            jump lbl_MatchMaker_Goat_End
        
    
    #choice -Digital Humans: Beta release (OHMYGODYES!!! Ahem. Yeah sure, whatever.)
    #choice -Sappy Treant Love Story 2 (Eww. Im not into that sort of movie)
    #choice -The Minotaurix (Isn't that the one with Kaiju Reeeves? I guess it might be ok.)
label lbl_goat_movies:
    g Gor happy "Would you like to go to the movies with me?"
    h "Hmm...what movie?"
    menu:
        "What movie?"
        "Digital Humans: Beta release":
            h "OHMYGODYES!!!"
            h "Ahem. I mean, Yeah sure, whatever."
            $iMovie = 1
            $iPoints += 2
        "Sappy Treant Love Story 2 ":
            h "Eww. I'm not into that sort of movie"
            g Gor happy "Oh, nevermind then."
            g Gor happy "Lets go guys."
            jump lbl_MatchMaker_Goat_End
        "The Minotaurix":
            "Isn't that the one with Kaiju Reeves? I guess it might be OK."
            $iPoints += 1
            $iMovie = 2
            
    g Gor happy "Awesome."
        
    if (iPoints > 5):
        #decides they can make the last showing of the movie if picked
        h "Actually if you come back when my shift is over we can still make the last showing."
        h "I-I mean if that is okay with you."
        g Gor happy "S-Sure!"
        "..."
        if (iMovie == 1):
            h "That was AMAZING!"
            g Gor happy "It was pretty good."
            s Sam happy "OK so it didn't put me to sleep, but I still prefer Pocket Humans."
            l Leo happy "Ahahaha. So stubborn Sammy."
        else:  
            h "That was pretty interesting."
            g Gor happy "I enjoyed it too."
            g Gor happy "Just interesting? Ill never understand some people."
            l Leo happy "I ran out of popcorn before the movie started. "
            s Sam happy "I told you to slow down Leo."
        
        h "Anyway I had fun Gordon. Thanks for walking me back."
        g Gor happy "I did too Helen. And no problem."
        
        h "So Gordon."
        g Gor happy "Yes?"
        
        h "Will you go out with me again sometime?"
        g Gor happy "I-I would be glad to!"
        
        l Leo happy "Sam...does it still count if the girl asks the guy?"
        s Sam happy "I-I don't see why not."
        l Leo happy "Good job Gor!"
        s Sam happy "Congrats man.      "
        g Gor happy "Lets go home guys."
        h "See you again guys."
        s Sam happy "Bye."
        l Leo happy "Bye."
        g Gor happy "Goodbye Helen."
        
        $bMatchGoat = True
        jump lbl_MatchMaker_Goat_End
        
    else:
        h "Actually on second thoughts, im pretty busy so i wont be able to join you after all."
        h "Sorry."
        g Gor happy "I-It's ok. I understand."
        s Sam happy "..."
        l Leo happy "..."
        g Gor happy "Goodbye."
        h "Bye guys."
        g Gor happy "Lets go home guys."
        jump lbl_MatchMaker_Goat_End
        

label lbl_MatchMaker_Goat_End:
    return
    
#----------------------------------------------------------------------
#----------------------------------------------------------------------

label lbl_MatchMaker_Snake:
    if (bLionHelped == False or bGoatHelped == False):
        s Sam happy "Hmm, if I don't help out the others I might not be able to rely on them if something comes up..."
        menu:
            "Should I still continue?"
            "Yeah, who needs those guys anyway?":
                pass
            "Perhaps I should reconsider...":
                jump lbl_MatchMaker_Choice
    
    $iPoints = 0
    s Sam happy "I guess that means its my turn."

    s Sam happy "I wont be able to avoid doing this much longer I guess."
    if (bLionHelped == True):
        l Leo happy "I've got your back Sammy."
    if (bGoatHelped == True):
        g Gor happy "I'm right behind you Sam. You don't have to worry."
        
    if (bLionHelped == True or bGoatHelped == True):
        s Sam happy "Thanks"
    
    s Sam happy "OK, I'm going to ask her out today."
    l Leo happy "Go for it Sammy!"
    
    #wonder how you're going to ask her out
    #realise you don't know where she is
    s Sam happy "Wait, how will I find her?"
    g Gor happy "Well what do you know about her?"
    
    s Sam happy "Well she's amazing!"
    g Gor happy "I mean, like where she lives, or what she does etc."
    s Sam happy "I-I don't know. I was never able to ask much before."
    #if bMatchGoat mentions he often sees her in the park 
    if (bMatchGoat == True):
        g Gor happy "Well now that I think about it, I often see her in the park so it might be a good idea to check there."
    else:
        s Sam happy "(Hmmm... Gordon seems to be lost in thought about something. I wonder what it is?)"
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
            call lbl_snake_library
        "Lets check the game store" if (iPoints > 0):
            $iPoints -= 1
            call lbl_snake_gamestore
        "lets check the park" if (iPoints > 0):
            jump lbl_snake_park
        "Lets check the bakery" if (iPoints > 0):
            $iPoints -= 1
            call lbl_snake_bakery
        "Lets go home."  if (iPoints == 0):
            jump lbl_snake_home
            
    jump lbl_snake_locationMenu

label lbl_snake_home:
    scene bg home day
    show Chimera Sam happy at left
    g Gor happy "All right, its getting late. Lets just call it a day."
    s Sam happy "Yeah, we can try again some other day."    
    jump lbl_MatchMaker_Snake_End
    
label lbl_snake_library:
    scene bg library day
    show Chimera Sam happy at left
    s Sam happy "I don't think she's here."
    g Gor happy "Wait since we're here I want to see if they have that book in stock yet."
    "..."
    g Gor happy "They still don't have it."
    s Sam happy "I don't really want to waste too much time."
    g Gor happy "Its a really good book though!"
    return
    
label lbl_snake_gamestore:
    scene bg shop day
    show Chimera Sam happy at left
    l Leo happy "Up to 50% off?!"
    s Sam happy "I don't think she's here."
    s Sam happy "OK give me a second, I want to see if they have any new games in."
    g Gor happy "Can't we do it another time?"
    s Sam happy "We're already here, it'll only take a second."
    l Leo happy "Yeah the good stuff might be gone later"
    "..."
    return
    
label lbl_snake_bakery:
    scene bg bakery day
    show Chimera Sam happy at left
    s Sam happy "I don't think she's here."
    l Leo happy "We should some cake."
    s Sam happy "But the line is so long."
    l Leo happy "But I'm hungry"
    g Gor happy "You're not going to budge are you?"
    l Leo happy "Nope."
    "..."
    s Sam happy "Happy now?"
    l Leo happy "Yep."    
    return
    
label lbl_snake_park:
    scene bg forest day
    show Chimera Sam happy at left
    s Sam happy "I don't think she's here."
    g Gor happy "Why don't we ask around and see if anyone has seen her today."
    "..."
    s Sam happy "So she's at the lake?"
    l Leo happy "That's what the lady at the fountain said."
    s Sam happy "OK then, lets go."
    
label lbl_snake_lake:
    scene bg lake day
    show Chimera Sam happy at left
    #meet at the lake (extra points for finding her faster) 
    #if places 2 or less shes swimming 
    #else finished swimming
    s Sam happy "OK OK. You can do this. Just breathe. You're ready for this."
    g Gor happy "Er Sam, you're talking to yourself out loud again."
    s Sam happy "S-Sorry. I'm just nervous."
    
    s Sam happy "Oh there she is."
    if (iPoints > 1 ): 
        s Sam happy "Looks like she's swimming in the Lake."
        $bSwimming = True
    else : 
        s Sam happy "She's all wet, I wonder if she was in the water."
        $bSwimming = False
        
label lbl_snake_Swim:
    #if swimming
    #chat
    #what are you doing? (Swimming. If you cant tell by looking i must be doing it wrong...)
    #Arent you cold? (Nah the scales keep out the cold)
    show medusa happy at right
    m "Oh hello there guys. What brings you around here?"
    l Leo happy "Oh nothing much."
    g Gor happy "Just happened to be in the area."
    g Gor happy "...Right Sam?"
    menu:
        "...Right Sam?"
        "(OHSHITSON!) Y-Yeah, just passing by.":
            s Sam happy "That's nice. Lovely day for a stroll isn't it?"
            m "Y-Yeah, it sure is."
            s Sam happy "Yeah, this weather is perfect for swimming."
        "(OHSHITSON!) I-I came to see you.":
            m "Oh? Did you want me for something?"
            s Sam happy "(What have you done?!)"
            s Sam happy "..."
            m "No?"
            s Sam happy "Y-Yes, I just wanted to talk to you."
            m "Oh I see. What did you want to talk about?"
            
        "(OHSHITSON! I can't do it! Impossible!)":
            jump lbl_MatchMaker_Snake_GoHome
        
    
    l Leo happy "..."
    g Gor happy "Sam"
    s Sam happy "S-So what are you doing?"
    if (bSwimming == True):
        m "Well I'm swimming. If you cant tell by looking I must be doing it wrong..."
        s Sam happy "N-No not at all. You look like you're doing great."
    else:
        m "Well I just finished swimming."
        
    l Leo happy "Why don't you ask her about it Sam?"
    
    s Sam happy "Erm Melissa..."
    m "Yes?"
    #ask about swimming
    #choice -Are you swimming for fun? [a] (I'm training)
    menu:
        "Ask about swimming?"
        "A-Are you swimming for fun?":
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
            m "I'm racing for the local team against another team from the neighbouring town."
            s Sam happy "Sounds pretty cool."
            m "Yeah, but I heard they were very good. Hence the training."
            s Sam happy "Well best of luck with that."
            m "Thanks~"
            jump lbl_snake_SwimTrain
        "I-I bet we could beat you in a race!":
            m "Well well, kind of cocky aren't we?"
        "Y-You should race against us, the competition will do you good.":
            m "I suppose a little competition wouldn't hurt."
            $iPoints +=1
        "(I can't do it after all!)":
            jump lbl_MatchMaker_Snake_GoHome
        
    if (bSwimming == False):
        m "However I already finished my training for the day, so you'll have to challenge me another time."
        jump lbl_snake_AfterSwim
    else:
        m "How about right now then?"
    
        #Leo refuses to get wet.
        l Leo happy "Wait wait. Swimming?"
        s Sam happy "What's up Leo?"
        l Leo happy "I don't want to get wet."      
        s Sam happy "B-But Leo..."
        #convince leo to help if bMatchLion
        #else (So much for that idea.)
        if (bMatchLion == True):
            l Leo happy "Well, I guess you did help me out before."
            l Leo happy "So Ill do it. But you better appreciate it. I hate getting wet."
            s Sam happy "Thanks Leo."
        else:
            l Leo happy "I'm not getting wet. No way no how."
            s Sam happy "(If only I had some way to get him to help.)"
            
            s Sam happy "W-Well so much for that idea."
            s Sam happy "S-Sorry Melissa."
            m "Don't worry about it."
            jump lbl_snake_AfterSwim
        
        #if race 
        #if helped gor and leo try hardest and only lose by a hairs breadth
        #else if only one helped lose by a lot.
        m "Well let me know when you're ready then. "
        s Sam happy "OK guys, I feel like we need to take this seriously, otherwise there's no point."
        l Leo happy "OK I'll do my best!"
        if (bMatchGoat == True):
            g Gor happy "You can count on me!"
        else:
            s Sam happy "(Hmm. Gordon seems distracted.)"
            g Gor happy "What? Oh yeah, sure."
        #medusa comments on the result (extra points for comming close)
        "..."
        if (bMatchGoat == True):
            m "Wow you guys did pretty good."
            l Leo happy "We...still...lost."
            m "But I had to go all out just to stay ahead."
            m "Maybe I should train with you guys more often."
            $iPoints +=1
        else:
            m "After all that talk you didn't present much of a challenge."
            m "It didn't seem like your hearts were really in it."
            s Sam happy "I-I'm sorry."
    
    m "Well we better get out and dry off."
    "..."
    #after swimming or if late
label lbl_snake_AfterSwim:
    m "So was there anything else you wanted?"
    
    g Gor happy "Ask what else she likes Sam"
    
    s Sam happy "So er..."
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

    m "I actually recently got into Video games after playing a few my cousin brought over."
    m "Oh so that's why you were in the store that time?"
    s Sam happy "Yeah, buying something for myself."
    
    menu:
        "I wonder what she got..."
        "Was it Centaur Princess Pony and Friends?":
            m "Wait, is that the one that's so pink you need sunglasses to look at the box?"
            s Sam happy "Er...yeah?"
            m "And you think it's my kind of game?"
            s Sam happy "Erm..."
            m "Because I'm a girl?"
            s Sam happy "Uh...I..."
            m "..."
            m "Ha ha, I'm just messing with you. "
            s Sam happy "But no, its not my kind of game."
        "Was it 'Something' Monsters?":
            m "Ha ha ha. You remembered."
            m "It actually was."
            m "Well sort of."
            s Sam happy "Sort of?"
            m "Yeah I wanted to get the same one my cousin had, but I couldn't remember the name."
            m "And when I got there there were two 'Something' monster games. But apparently I picked the wrong one."
            s Sam happy "Ha ha ha ha."
            m "Hey don't laugh. But actually this one is pretty fun too, so it worked out in the end I guess."
            s Sam happy "So which one did you get?"
            m "..."
            s Sam happy "Still don't remember the name?"
            m "...no."
            s Sam happy "Haha."
            m "Shush."
            $iPoints +=1
        "Was it Call of Boo-ty: Modern Scarefare 3?":
            m "What's that?"
            s Sam happy "Its a boo-t em up."
            s Sam happy "Oh I don't really like those, all the screen shaking gives me a headache."
            
    #medusa says she has to go soon.
    m "Well its been fun hanging out with you guys, but I've got to head back."
    m "Its especially nice to hear you talking so much Sam."
    
    s Sam happy "Wait..."
    m "Hmm?"
    g Gor happy "Go for it Sam."
    l Leo happy "You can do it Sammy."
    
    #Ask her out?
    #choice -Yes of course (pluck up the courage)
    #choice -ill try another day (Fail to get)
    menu:
        "Should I ask her out?"
        "(Hell yes!)":
            s Sam happy "Melissa."
            m "Yes?"
            s Sam happy "W-Will you got out with me?"
            m "Like a date?"
            s Sam happy "Y-Yes."
            m "Hmm..."
        "(I'll try another day)":
            jump lbl_MatchMaker_Snake_GoHome    
    
    #ask her out
    if (iPoints > 5):
        m "I'd be happy to."
        s Sam happy "Yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
        g Gor happy "I think he's happy."
        l Leo happy "Ahahahaha. Good job hanging in there Sam."
        #She agrees to go out with Sam the comming weekend
        $bMatchSnake = True
    else:   
        m "I'm afraid I can't."
        s Sam happy "Y-You can't?"
        m "No, with the match coming up I can't afford to be distracted."
        m "I'm sorry."
        s Sam happy "I-It's OK. I understand what you're saying."
        g Gor happy "Sam..."
        l Leo happy "..."
        s Sam happy "Lets go home guys."
    jump lbl_MatchMaker_Snake_End

label lbl_MatchMaker_Snake_GoHome:

    s Sam happy "..."
    m "..."
    l Leo happy "..."
    g Gor happy "..."
    g Gor happy "We'll we better be off."
    m "Okay, see you again sometime."
    s Sam happy "..."
    s Sam happy "I-I messed up didn't I?"
    g Gor happy "Yes."
    l Leo happy "There there Sammy."
    s Sam happy "Lets go home guys."
    jump lbl_MatchMaker_Snake_End
    
label lbl_MatchMaker_Snake_End:
    jump lbl_Ending
    
label lbl_Ending:
    scene bg home day
    show Chimera Sam happy at left
    
    s Sam happy "So to summarise..." 
    if (bMatchLion == True):
        s Sam happy "Leon is together with Persephone"
    else:
        s Sam happy "Leon is alone."
        
    if (bMatchGoat == True):    
        s Sam happy "Gordon is together with Helen" 
    else:
        s Sam happy "Gordon is on his own" 
        
    if (bMatchSnake == True):
        s Sam happy "I am together with Melissa" 
    else:
        s Sam happy "I don't have anyone." 
    
    if ((bMatchLion == True) and (bMatchGoat == True) and (bMatchSnake == True)):
        s Sam happy "Looks like everything went according to plan."
        jump lbl_GOODEND
    else:
        s Sam happy "Looks like I messed up somewhere."
        jump lbl_BADEND

label lbl_GOODEND:
    scene GOOD_END
    s Sam happy "And so everyone got someone of their own to be with." 
    s Sam happy "Time for us to make triple dates a thing." 
    "GOOD END"
    $persistent.bonus_unlocked = True
    "(Bonus chapter unlocked)"
    jump end

label lbl_BADEND:   
    scene bg black
    s Sam happy "And so I ended up spending the rest of my life alone." 
    s Sam happy "Well as alone as one can be while attached to two others..."
    "BAD END"
    $persistent.bonus_unlocked = True
    "(Bonus chapter unlocked)"
    jump end 

 
label end: 
    return
    
    
label lbl_Bonus:
    scene bg library day
    if ( not persistent.bonus_unlocked):
        "It seems there's nobody here..."
        "(Come back after completing the game to learn more about the monsters that appear in it.)"
        return
    "Teach me Miss Melissa~"
    show medusa happy at left
    m "Ok, be seated class. Today we are going to be learning about different monsters."
    m "What monsters?"
    m "Well the ones that appear in this particular story of course."
    m "So what would you like to hear about first?"

label lbl_learn_menu:
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
    m "Hmm... I'm not really sure. Lets consult the manual."
    m "The Chimera was, according to Greek mythology, a monstrous fire-breathing hybrid creature, composed of the parts of three animals – a lion, a snake and a goat." 
    m "...sounds scary."
    m "Our own Chimera isn't nearly as scary sounding as that."
    m "Oh here they are now"
    show Chimera Sam happy at right
    m "Ok, lets count the heads to see if the book was correct."
    m "1... The Lion, Leonardo"
    l Leo happy "Hi"
    m "2... The Goat, Gordon"
    g Gor happy "Hello Melissa."
    m "3... The Snake, Samuel"
    s Sam happy "Hi Melissa"
    
    m "Yes, it seems the book was correct. 3 heads."
    m "But i have an important question guys."
    s Sam happy "What is it?"
    m "C-Can you really breathe fire?"
    l Leo happy "Er...I dunno, can we?"
    s Sam happy "Why are you asking me?"
    g Gor happy "I cant say that I've tried it before."
    m "..."
    s Sam happy "...Maybe we should try it now?"
    l Leo happy "...haaa"
    g Gor happy "...paaa"
    s Sam happy "...saaa"
    
    m "Well it looks like this might take a while so why don't we move on?"    
    hide Chimera 
    jump lbl_learn_menu
    
label lbl_learn_medusa:
    m "Medusa? You want to learn more about me?"
    m "I'm flattered~"
    m "I mean I could talk about myself all day long, but I'm kind of curious what the Manual says about me..."
    m "In Greek mythology Medusa was a monster, a Gorgon, generally described as having the face of a hideous human female with living venomous snakes in place of hair. Gazing directly into her eyes would turn onlookers to stone."
    m "Whoa whoa. It says I'm hideous?!"
    m "I'm cute as a frigging button. I need to find out who wrote this book and give them a piece of my mind."
    m "Maybe ill turn them to stone!"
    m "...wait, I don't think I can do that in real life."
    m "Bah, this book sucks."
    
    m "Anyway, lets move on kids."
    jump lbl_learn_menu
    
label lbl_learn_harpy:
    m "Ahh the new girl, what was her name? Oh right Helen."
    m "The Trusty Manual says..."
    m "In Greek mythology , harpies were female monsters in the form of birds with human faces. They steal food from their victims while they are eating and carry evildoers away. Their name means 'snatchers'."
    m "I guess I need to be careful of my lunch when Helen is around."
    show harpy happy at right
    h "Did someone say my name?"
    m "Oh hi Helen."
    h "Hi Melissa."
    m "You can't have my food."
    h "What?"
    m "I'm keeping it."
    h "...what?"
    m "..."
    h "..."
    m "Ok ill share some with you later."
    h "I have no idea what's going on."
    
    m "You'll have to come back later though, its not lunch time yet."
    h "...Okaaay."
    hide harpy
    jump lbl_learn_menu
    
label lbl_learn_cyclops:
    m "Wait is there even one of those in this?"
    m "Oh right, the shopkeeper. You guys don't miss a beat, do you?"
    m "Anyways the Manual says..."
    m "A Cyclops, in Greek mythology, was a member of a primordial race of giants, each with a single eye in the middle of his forehead."
    m "I wonder if it makes it hard for them to judge distance, since they'd have no depth perception..."
    m "Oh I asked the shopkeeper if he'd pop over for this, but apparently he's busy selling games or something."
    m "He's not that important anyway so don't worry about it."
    m "So what next?"
    jump lbl_learn_menu

label lbl_learn_human:
    m "A human?"
    m "I don't need to consult the Manual this time. Everyone knows those don't exist."
    show human happy at right
    p "What doesn't exist?"
    m "AHHHH!!!"
    hide medusa
    p "..."
    p "Was it something I said?"
    p "..."
    p "I better get back, father will get worried."
    hide human
    m "..."
    m "...is it gone?"
    show medusa happy at left
    m "Who'd have thought they were actually real."
    
    m "So what now?"
    jump lbl_learn_menu


label lbl_learn_end:
    m "Well I hope you remember all that, because its going to be on the test."
    m "Class dismissed."
    
    return