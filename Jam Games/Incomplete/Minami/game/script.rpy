# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

label splashscreen:
    $ renpy.movie_cutscene("videos/splashscreen.webm")
    $ renpy.movie_cutscene("videos/warning.webm")
    #$quick_menu = False
    #call screen trigger_warning()
    #$quick_menu = True

    return
#NOTES from Izanami Paradox

#For transitions, I want the scenes to fade in and out.
#Every time the character changes expression, the sprite bounces up then down.
#When the character gets off screen, I want them to bounce off the screen (Minami/Takehito to the right side, Eiichi to the left) (Unless stated otherwise)
#I want the letters to typing effect out instead of them just popping up. Then the player can't click until it's done typing.
#Some words will be highlighted, so I want them to have the font as the character title when highlighted. They will he highlighted with -.
#Some sound effects isn't working, so please help me fix them! Thanks so much! <3
#I want the font of the text to be Times new Roman and Bold with the color being #000000 (Black).
#I also want like a little notification pop up after the choice the player selected stating the name of the route they picked. I want it placed on the top left of the screen. And it goes off after the next text.
#Also when it comes to warning about this game being a demo, I want a warning box to come up and the toolbox gone. The warning box will be in the center of the screen. I also want a x button near it so they can go back to the game.
#Thank you so much!! <3

define e = Character("Minami")


# The game starts here.

label start:
    stop music
    
    jump lbl_minigames
    
    jump lbl_start # real game start, comment out for testing
    
    "Testing code, you probably shouldn't be here."
    call lbl_showCredits from _call_lbl_showCredits
    scene bg MorningBedroom with fade

    "..."
    show eiichi normal at bounceInLeftToLeft
    pause (2.0)
    show eiichi normal at hopLeft
    "..."
    
    
    show eiichi normal at hopLeft
    show minami angry at hopCenter
    show takehito normal at hopRight
    "..."
    show eiichi cry at bounceOutToLeftFromLeft
    show minami upset at bounceOutToRightFromCenter
    show takehito disgusted at bounceOutToRightFromRight
    "..."
    show eiichi happy at straightInLeftToLeft
    show minami happy at bounceInRightToCenter
    show takehito happy at bounceInRightToRight
    "..."
    show eiichi normal at hopCenterLeft
    show minami angry at hopCenter
    show takehito normal at hopCenterRight
    "..."
    show eiichi cry at hopLeft
    show minami upset at hopCenterRight
    show takehito disgusted at hopRight
    "..."
    show eiichi happy at hopCenterLeft
    show minami happy at hopCenter
    show takehito happy at hopRight
    "..."
    show eiichi happy at hopLeft
    show minami happy at hopCenterLeft
    show takehito happy at hopRight
    "..."
    call screen demo_warning()

    call screen trigger_warning()

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.


    "A black dress adorns her body, like the midnight sky in a lonely grave.  I'm scared. My eyes refuse to turn away, despite the struggles I put forth, entangled in the horrifying scene before me while my limbs hang limply by my side, as the barrel of the gun stays primed towards my being."

    menu:
      "This is a choice."
      "Option 1":
        pass
      "Option 2":
        pass

    menu:
      "This is a different choice."
      "This is a really long option, i wonder how well it will look":
        pass
      "I wonder":
        pass
      "How it":
        pass
      "Will look":
        pass
      "With so":
        pass
      "Many Options":
        pass

    e "just kidding these do nothing."

label lbl_minigames:
    menu:
        "Dating":
            e "Try the dating minigame"

            call lbl_minigame_dating from _call_lbl_minigame_dating
        "Trivia":
            e "Try the trivia minigame"

            call lbl_minigame_trivia_start from _call_lbl_minigame_trivia_start


    e "thats all folks."

    return
    
label lbl_cheating:
    $cheat = renpy.input("Enter Code...")
    $cheat = cheat.strip()
    
    if cheat == "cheat1":
      "cheat1 Active"
    if cheat == "cheat2":
      "cheat2 Active"
    if cheat == "cheat3":
      "cheat3 Active"
    return

label lbl_start:
    scene bg black
    #show screen route_indicator()
    play sound S_AlarmNoise loop
    "Alarm rings"
    clock "*Ring ring* *Ring Ring*"
    "Eiichi suddenly wakes up, shaking his hands."
    "He moves over to the clock on the right side of his bed. He put his hand over "
    play sound S_ObjectImpact
    stop sound #S_AlarmNoise
    scene bg MorningBedroom with fade
    #show screen route_indicator("Main Route")
    "The lamp and slams it off the floor to the ground."
    #hide screen route_indicator
    play sound S_PhoneVibrate loop
    "His phone rings from under the bed. Eiichi gets up from the bed, Wandering around the room searching for the ringing noise."
    eiichi "where's that damn phone!!"
    "Eiichi looks on the shelves, and in the drawers and storage cabinets, but there's nothing to be found."
    "He looks under the bed and sees his phone light up. He gets on his knees and reaches under his bed."
    eiichi "Mother fudger it's under the bed today... Eiichi you really are deaf .."
    stop sound #S_PhoneVibrate
    play sound S_PhoneTap
    "Eiichi gets out from under the bed and turns the alarm off his phone."
    scene bg black with fade
    "He gets himself washed and dressed, and makes breakfast. He sits down in the chair in his kitchen, grabs the remote and turns the TV on."
    "The TV plays a music channel."
    play music youlikejazz
    #Eiichi says while having a bagel in his mouth
    show eiichi normal at bounceInLeftToLeft
    pause (2.0)
    show eiichi normal at hopLeft
    eiichi "Some kind of jazz today i guess.."
    eiichi "My life is horribly boring. I wake up, go to work, go home, go to sleep."
    eiichi "Sometimes I would go out on dates, hang out with 2 of my friends, or go on company vacations around the world."
    eiichi "But for some reason I don't enjoy these things. It feels.. boring."
    eiichi "It feels like human life is boring. Even the most exciting thing us humans ever do, it's really boring for me."
    eiichi "I wonder if something's wrong with me. No, something's gotta be wrong with me."
    eiichi "I mean I can't be this bored with a semi-exciting life. maybe life is exciting for me on the other side.."
    eiichi "let's not get those thoughts again.. tonight after work i have a date with another girl I met on this dating app."
    eiichi "She seem awfully nice.. and a bit cute.. I hope {font=[gui.name_text_font]}nothing{/font} goes wrong on this date."
    "Eiichi finishes his food, grabs his wallet, and leaves for work."
    stop music #youlikejazz
    play sound S_SubwayAmbience loop
    scene bg Subway
    show eiichi normal at bounceInLeftToLeft
    pause (0.2)
    show eiichi normal at hopLeft
    "Taking the Shinjuku train to work, He notices his ex waiting to go to work as well. She looks at him then turns around. Eiichi then looks away to the door."
    eiichi "Yuko sure hates me after what I did.. I did not mean to injure her little sister!! I ACCIDENTALLY bumped her and she fell on the train tracks."
    eiichi "She's lucky... No i'm lucky that she only lost.. both of her legs.. yeah i guess seeing her sister suffer for months and months, She couldn't even lay her eyes on me again."
    play sound mizuki
    "The announcer comes on the loudspeaker"
    announcer "Now-entering Nakano city, now-entering Nakano city"
    "The train arrives and the doors open."
    "Eiichi walks out of the train and walks to his office."
    show eiichi at bounceOutToLeftFromLeft
    "Yuko looks outside the door while Eiichi walks away."
    scene bg OutsideCafe with fade
    play music funM
    "After Eiichi arrives at his office and then hours pass. It's lunch time and he's sitting outside eating some of his bento box he made the night before. "
    show eiichi normal at bounceInLeftToLeft
    pause (0.2)
    show eiichi normal at hopLeft
    "A guy and a girl comes out and sit with Eiichi."
    #??? with aN excited tone
    qq "Heyy Eiichi!! what's up?"
    eiichi "Hey.. aren't you guys supposed to be in the kitchen?"
    "??? laughs"
    qq "We don't do the kitchen today. Every friday the 13th the kitchen is closed."
    eiichi "That rule didn't exist until now.. Takehito you did something didn't you?"
    show takehito happy at bounceInRightToRight
    pause (0.2)
    show takehito happy at hopRight
    takehito "I didn't do annyything, right minami-chan?"
    show minami disappointed at bounceInRightToCenterRight
    pause(2.0)
    show minami disappointed at hopCenterRight
    minami "He burnt everyone's food. Everyone had to go to the takoyaki truck down the street."
    eiichi "Minami-chan usually cooks.. why do you even try?"
    takehito "Because I want to learn how to cook, Right Minami-chan?"
    minami "He almost burnt down the house several times."
    show minami happy at hopCenterRight
    minami "Don't worry Taki-kun I still love you even if you burnt the new stove we just got a month ago.."
    show minami normal at hopCenterRight
    show takehito normal at hopRight
    takehito "You'll love me even if I burn the whole house down."
    show minami happy at hopCenterRight
    minami "yep! but you'll get a lecture- a huge one."
    show takehito happy at hopRight
    eiichi "Even if it causes you financial ruin trying to get another house, you still would be so lovey dovey.."
    "Minami kisses Takehito on the cheek and Takehito smiles."
    hide minami at dissolve
    hide takehito at dissolve

    show eiichi normal at straightInLeftToCenter
    pause (2.0)
    show eiichi normal at hopCenter

    #eiichi thinks to himself
    eiichi "Their relationship is so perfect it kinda scares me."
    eiichi "But then again I wish I could achieve such a thing.. through numerous break ups due to UNFORTUNATE events."
    eiichi "Why should I even attempt it again? I guess it's because of hope... "
    eiichi "I mean my life is just beginning after all."
    show eiichi normal at bounceOutToLeftFromCenter
    pause (2.0)
    show eiichi normal at bounceInLeftToLeft
    pause (2.0)
    show eiichi normal at hopLeft
    show takehito normal at bounceInRightToRight
    pause (2.0)
    show takehito normal at hopRight
    pause (0.7)
    show minami normal at bounceInRightToCenterRight
    pause (0.2)
    show minami normal at hopCenterRight
    takehito "Hey Eiichi, Minami-chan and I wanted to invite you to dinner tomorrow after your ping pong tournament."
    takehito "We want to celebrate you winning the finals."
    eiichi "I didn't win yet.. I heard the guy in the finals was unbeatable for 10 years.. I honestly think he's a hacker.."
    show takehito disappointconcerned at hopRight
    takehito "Am i more up to date than you?"
    takehito "You're right because 2 days ago he got disqualified after the admins found him cheating and banned him for exactly 10 years."
    takehito "The guy you beat faithfully is his replacement."
    takehito "They didn't want to default it because you know... National Tv.. but easy win."
    eiichi "Oh great! Well this is something I just do in my spare time.. I don't really care. I only do the tournaments for extra cash.."
    "While they talk Minami holds Takehito close and rubs her head repeatedly on his arm."
    takehito "I don't call 550,000 yen extra cash from a national tournament."
    takehito "Rewind those words for me."
    show eiichi happy at hopLeft
    eiichi "Blah blah blah what ever.."
    "Eiichi laughs while they sit and eat lunch."
    show takehito normal at hopRight
    minami "You have a date tonight, right?"
    show eiichi normal at hopLeft
    eiichi "Yeah with some girl named Umeko-san. She's really nice and kinda cute.."
    takehito "hittin' those dating apps again."
    show minami concerned at hopCenterRight
    minami "Eiichi-kun, she's so outstandish and a bit young.. are you sure she's your age?"
    eiichi "Yeah I face-timed her she's my age. Her appearance is nothing compared to what she sounds like.."
    show takehito disappointconcerned at hopRight
    takehito "She looks kinda familiar... like I know her.."
    minami "You know her?"
    "Minami freezes"
    show takehito normal at hopRight
    takehito "It takes her so long to remember.. it's like she's an android."
    takehito "Yeah.. anyways good l-"
    "Takehito's watch rings"
    play sound S_RepeatDoorbell
    watch "*Ding Dong*"
    eiichi "Why the hell does your watch sounds like a doorbell now?"
    takehito "I love the doorbell sound.. reminds me of my pro gamer days."
    eiichi "Your mixer days, alright then.."
    eiichi "why did you quit, anyways?"
    show takehito upset at hopRight
    "Takehito frowns while looking at Eiichi"
    takehito "Stuff happened and I kinda just ran away.. it waSN'T RIGHT BUT IT WAS THE ONLY THING I COULD DO BEFORE THINGS GOT WORSe."
    "Minami unfreezes in time"
    show minami normal at hopCenterRight
    minami "I remember now. She used to work at the supermarket 3 years ago.. She randomly quit before you came into town Eiichi-kun."
    "Takehito's watch rings again"
    play sound S_RepeatDoorbell
    watch "*Ding ding ding ding*"
    show takehito normal at hopRight
    takehito "Welp.. come on minami-chan."
    "Takehito and Minami get up"
    show minami happy at hopCenterRight
    minami "It's time already? back to work!"
    show takehito happy at hopRight
    takehito "Good luck on your date."
    "Takehito and Minami walk away while talking"
    show takehito at bounceOutToRightFromRight
    show minami at bounceOutToRightFromCenterRight
    minami "You know... I really do like strawberries."
    takehito "I'll get you some later sweetheart.."
    "Eiichi packs up his lunch while he thinks to himself:"
    eiichi "I love them.. i hate their relationship.. i need to stop being jealous. tonight is it."
    eiichi "i hope I can achieve happiness like them. I mean they should be married by now.. but I guess it takes time."
    hide eiichi with fade
    stop music
    scene bg PastelScenery
    "Eiichi gets up and goes inside the office to work. Hours later it's time for his date. He waits outside of the Shibuya station for Umeko. Umeko is seen from afar wearing something like a child would wear."
    umeko "yaho!"
    "Umeko runs up to Eiichi and give Eiichi a hug and a kiss."
    show umeko normal at bounceInRightToRight
    pause (2.0)
    show umeko normal at hopRight
    pause (0.3)
    show eiichi happy at bounceInLeftToLeft
    pause (0.2)
    show eiichi happy at hopLeft
    eiichi "Well, your voice {font=[gui.name_text_font]}is{/font} a bit different from last night.."
    umeko "I didn't have my pills last night. The pharmacy made a mistake and I had to wait a few hours."
    eiichi "Well.. alright.. wanna head over to the restaurant?"
    "Umeko nods violently and holds Eiichi's arm. Eiichi and Umeko enter the restaurant."

    #Window pops up with warning about minigame it says:
    #This is a demo, the dating minigame will appear in the full version due to there being little to no assets! Please follow @IzanamiParadoxV for more information!


    $quick_menu = False
    call screen demo_warning("This is the {size=+20}Demo Version{/size}\nThe dating minigame will appear in the full version!\n\nPlease follow {a=https://twitter.com/IzanamiParadoxV}@IzanamiParadoxV{/a} on Twitter for more information!", 36)
    $quick_menu = True
    
    #"MAIN ROUTE"


    scene bg black with fade

    show screen route_indicator("Main Route")
    "Eiichi and Umeko leave and part ways. Eiichi walks away from Umeko"
    ", while Umeko walks away but looks back with a smile. Eiichi gets home, time passes and he's in bed."
    hide screen route_indicator
    eiichi "I'm now envious. Should I even have hope at this point? I know she didn't like me. Yet takehito and minami-chan have it all!!"
    eiichi "I wish umeko-san was like that to me.. but she wasn't."
    eiichi "There's no way Takehito and Minami-chan are the perfect couple. There must be some flaws.."
    eiichi "Maybe at home they're covering their arguments when no one is home. I gotta see what their flaw is."
    eiichi "I would say tomorrow is the perfect time, but i've went over to their house many many times and there stood the perfect couple."
    eiichi "But maybe they have evidence of a relationship in a facade through their house.. after all there's one room that I never went to."
    eiichi "They say it's their 'pleaaaaaaaasure' room but maybe i can find something in it."
    eiichi "Tomorrow is the night where i'll finally discover that room."
    "Eiichi falls asleep."
    "The morning comes and it's Saturday. The timer goes off for the tournament."
    "Eiichi wakes up, does his normal saturday routine of sitting at the table and eating his oyakudon he made for himself."
    "He looks at the TV, watching the saturday news."
    "Eiichi -i-s dumbfounded."
    "He discovered Umeko on the news being arrested for attempted kidnapping and 1st degree murder."
    "She was carrying a bag full of rope, torture utensils, and murder weapons."
    "She ended up in a unfortunate circumstance when she came out with cops in front of her door from a previous event that had happened next door to her apartment."
    "She had that same look she had when Eiichi was at the restaurant with her."
    "Eiichi dropped his fork and starred at the TV."
    "He began to tremble, thinking that he could've been dead last night if an unfortunate coincidence had happened to her."
    #Eiichi with his trembling voice
    eiichi "She... was gonna kill me..."
    "Eiichi closed his eyes and took a deep breath."
    "He got up and threw his oyakudon in the trash and began to leave out the door."
    "He was gonna end up early to the tournament but it was worth it to get his mind off of his fortunate luck. He couldn't even finish eating."
    "It was time for the tournament."
    scene bg TournamentArena with fade
    play sound S_ArenaAmbience loop
    "After hours of beating the poor man to a pulp once again in a VR-like advanced ping-pong championship, Eiichi won."
    "The crowd cheered, the judges sighed but still were satisfied. The way Eiichi beat this man was like a grown adult man falcon punching a toddler."
    "Everyone watching this tournament kept their eyes on the torture fest, almost making everyone in the crowd sadistic fiends yearning for questionable entertainment."
    "Eiichi got his earnings and left the building. Through everything he didn’t speak much."
    "After all he found out he could’ve died this morning."
    scene bg Subway with fade
    play sound S_SubwayAmbience loop
    "Eiichi is afraid of death."
    "He had a problem trying to stomach it all day."
    "It was that moment while riding the train, he deleted his account and the app off his phone while his hands were trembling."
    "He didn’t want to do anything associated with death."
    stop sound
    scene bg black with fade
    "Before heading to Takehito and Minami’s home all the way in Osaka, he stopped at his house to change."
    scene bg BathFoggy with fade
    play music Sad1M
    "He took a long thoughtful shower, having is head on the shower wall while the water fell on him."
    "Every now and then, he could feel slender hands crawling on his skin"
    "Images races in his head from his childhood."
    "Sometimes he would scream, sometimes he would cry, and sometimes he would try to scratch his skin to the point where it would become scars"
    "Today, he added more scars to the collection of his bruised arms."
    "He always wears sweaters because of it."
    "It doesn't matter if it's 37 C or not."
    "Eiichi thinks it's embarrassing to show the marks engraved on his arm."
    "It was not only marks of his own doing but marks from his unplesant past with his mother."
    "Sometimes the images would get worst"
    "It feels like the whole bathroom would change."
    "Eiichi really gets sick of the sudden images of his mother."
    "Even though his mother died from cancer, it feels like she's still there just to torment him."
    "The thoughts, his thoughts, circling through his head around and around."
    "'why would she do this?'"
    "'I should've never let her do that!!'"
    "'this isn't love, this is pain'"
    "'I want to be loved!'"
    "'I want to be loved!'"
    "'I want to be loved!'"
    "'i want it the right way.. not this disgusting love..'"
    "'Mother.. loved me too much.'"
    "The thoughts began to calm."
    "He took a deep breathe as he closes his eyes."
    "1"
    "2"
    "3"
    "He awakens out of the illusion and turns off the water."

    scene bg DoorEntrance
    stop music
    stop sound
    show eiichi normal at bounceInLeftToLeft
    pause (2.0)
    show eiichi normal at hopLeft
    "It's an hour or so later, he finally reaches Takehito's and Minami's house."
    play sound S_Doorbell
    "He rings the doorbell and all Eiichi hears is utter chaos trying to get to the door."
    "The door opens and he sees Takehito with a bunch of feathers and paint on him."
    show takehito embarassed at bounceInRightToRight
    pause (2.0)
    show takehito embarassed at hopRight
    takehito "Heyyy Eiiichi I totally forgot we invited you!"
    "Minami yells from a distance speaks.."
    minami "We didn't, we were playing so many games we ended up forgetting to make dinner."
    "Takehito smiles"
    show takehito normal at hopRight
    takehito "Heeeeey just come in."
    scene bg DiningRoom
    play music idleM
    "Eiichi comes in their house. Their house is clean, as usual."
    "Despite both Minami and Takehito being plastered with paint and feathers from an unknown source, the living room and dining room was as clean as a baby's bottom."
    "Eiichi sat down in the dining room while Minami started to cook. Takehito sat in front of Eiichi with a deck of cards."
    show takehito normal at bounceInRightToRight
    pause (2.0)
    show takehito normal at hopRight
    show eiichi normal at bounceInLeftToLeft
    pause (2.0)
    show eiichi normal at hopLeft
    takehito "How was the tournament? Did you enjoy it?"
    eiichi "I committed murder and everyone liked it."
    takehito "Sounds like a snuff film on live television."
    eiichi "It was a noob vs 10 year champion.. it hurts to even challenge the dude.."
    eiichi "but if  forfeited he would've won and I wasn't lett- heyy you didn't watch it didn't you?"
    takehito "I already knew you were gonna win. and besides Minami-chan and I had so much fun from the beginning of the day to now."
    takehito "We did take a break though, but we missed it by then."
    eiichi "I kinda feel bad.. I should share my earnings with him on monday."
    show takehito happy at hopRight
    takehito "That's nice.. share some with me maybe?"
    "Minami yells from a distance"
    minami "Taki-kun no!"
    "Takehito laughs"
    eiichi "Yeah.. you have enough yourself."
    show takehito normal at hopRight
    takehito "Yeah.. let's play some games.."
    "Eiichi thinks to himself while they play a game of old maiden"
    eiichi "He's really in a playful mood today.. he should be playful with Minami-chan not me. I'm not a playful person."
    eiichi "I wonder how Minami-chan's doing in the kitchen?"
    show minami happy at hopCenter
    "Minami comes out with a platter full of food. It was filled with Rice, Curry, Natto, Sukiyaki, and Motsunabe."
    show takehito upset at hopRight
    "So many filled onto one platter it was unbelievable."
    "But Eiichi wasn't pleased. In fact he was disgusted."
    eiichi "Minami-chan....?"
    show minami confused at hopCenter
    "Minami paused for a minute."
    "She completely forgot Eiichi doesn't eat none of what's showed on that platter."
    "Takehito looked at Minami and gave her a \"cut it out\" hand signal."
    show minami disappointed at hopCenter
    minami "I'll order take out."
    show minami at bounceOutToLeftFromCenter
    "Minami goes back into the kitchen and throws out the food."
    hide eiichi
    hide takehito
    "Hours pass by. Minami, Takehito, and Eiichi are eating the food Minami had ordered."
    "The food was better, looked better, tasted better, everything was better, according to Eiichi."
    "Eiichi realized this was the restaurant he ate at a week ago."
    "Takehito pauses for a minute then speaks."
    show takehito normal at hopRight
    takehito "I gotta do something.. be back!"
    "Takehito gets out of his chair and leaves the table."
    show takehito normal at bounceOutToRightFromRight
    "Eiichi was curious as to why he left in such a manner."
    "While Eiichi was in continous thought. Minami began to speak to Eiichi."
    show minami happy at hopCenter
    minami "How did your date go last night?"
    "Eiichi froze and started sweating."
    "He didn't want to be reminded of that psychotic woman."
    "Eiichi's hands were shaking once again."
    "Minami noticed his hands and quickly changed the subject."
    show minami concerned at hopCenter
    minami "Are you still having nightmares?"
    "Eiichi calmed down.. it took him some minutes to calm down but it worked."
    show eiichi normal at hopLeft
    eiichi "Yeah.. every so on I still have them.."
    eiichi "Some nights i don't want to sleep but I end up falling asleep and succumbing to the nightmares."
    show eiichi cry at hopLeft
    stop music
    eiichi "I hate it so much... It makes me just wanna let myself die..."
    show bg white
    play music Sad2M fadeout 1.0 fadein 1.0
    minami "Eiichi-kun your mother isn't with you anymore.. besides, you're worth a lot.. if you don't know, so many people look up to you!"
    show minami normal at hopRight
    minami "They want to be the world's best vr ping pong player!"
    minami "They want 500,000 yen under them every year! you should live for them!"
    minami "You're already living your purpose! Live it to the best you can!"
    "Eiichi begins to tear up."
    show eiichi happy at hopLeft
    eiichi "You always encourage me.. I appreciate it.. you're such a great friend."
    eiichi "Without you I would be gone right now.."
    hide eiichi at dissolve
    hide minami at dissolve
    "Minami gets up from her chair and hugs Eiichi."
    minami "There there.."
    minami "We're here for you.. and you are here for your fans that you pretty much didn't know you had."
    minami "THINK OF THE PEOPLE WHO CHEERED YOU ON, THINK OF ALL THE AUTOGRAPHS YOU COULD GIVE IF YOU HAD OPENED UP YOURSELF.."
    "Minami stops hugging him and gets back to her seat."
    stop music
    show bg DiningRoom
    play music funM
    show minami happy at hopCenter
    show eiichi happy at hopLeft
    "She begins eating her food while Eiichi sits there and smiles."
    "Eiichi wipes his face and begins eating."
    "Takehito comes out and sits back in his chair with silence."
    show takehito normal at bounceInRightToRight
    pause (2.0)
    show takehito normal at hopRight
    "Eiichi stares at him while he eats."
    eiichi "What's wrong? are you ok?"
    "Takehito smiles to Eiichi"
    show takehito happy at hopRight
    takehito "The cat ran out the bag don't worry!"
    "Takehito went back to eating his food."
    show eiichi normal at hopLeft
    "Eiichi looked at Takehito with a confused face."
    "Then he continues to eat anyways."
    hide eiichi at dissolve
    hide minami at dissolve
    hide takehito at dissolve
    "A hour later, Minami, Takehito, and Eiichi are playing on the Nintendo D69 in their living room."
    "Eiichi's stomach starts to bubble."
    show eiichi normal at hopLeft
    eiichi "Guys I need to go to the bathroom stat."
    show takehito happy at hopRight
    takehito "Alright but don't take too long or I'm taking over your controller!"
    "Takehito snickers while Eiichi gets up and goes to the bathroom."
    stop music
    scene bg ApartmentHallway
    "After his poop fiasco, Eiichi walks out of the bathroom."
    "Eiichi notices a door slightly opened. A flashback from a previous time appears."
    show bg white
    show takehito normal at hopCenter
    takehito "After the bathroom this is the pleaaaasure room."
    takehito "Do not... do not, I repeat, DO NOT go in there."
    takehito "That room is off limits. I don't even let Minami-chan come in here."
    eiichi "Then what's the point of the pleeeassure room if minami-chan can't go in there?"
    show takehito happy at hopCenter
    takehito "there's just some things that can't be revealed. alright?"
    eiichi "alright..."
    hide takehito
    "The flashback ends and Eiichi thinks to himself."
    show bg ApartmentHallway
    show eiichi normal at hopCenter
    eiichi "That was 5 years ago.. I was suspicious of him for a while after that but it stopped."
    eiichi "Should I check the room out?"
    hide eiichi

    #This is where the choices comes in.

    #Choice 1: Eh... It's probably nothing in the room. (Unlocks Route 3)
    #Choice 2: This was the moment I was looking for! (Continues main route)


    menu:
        "Should he check the room out?"
        "Eh... It's probably nothing in the room.":
            jump routethree
        "This was the moment I was looking for!":
            jump mainroute1

label routethree:

    #ROUTE 3 "SOOOO HAPPPPPYYY SONG"
    show screen route_indicator("SOOOO HAPPPPPYYY")
    eiichi "it's not important.."
    scene bg DiningRoom
    hide screen route_indicator
    "Eiichi goes back to the room and plays the Nintendo D69 for the rest of the time."
    "Eiichi was tired."
    "He left their house and headed home to sleep."
    scene bg black
    stop music
    "Once he got home, he got his pajamas on and got into bed."
    "He couldn't sleep, thinking about the nightmares he was going to have again."
    eiichi "I don't think i'll ever get away from mother.. there's no way.. I can try to get through this..."

    "{font=[gui.name_text_font]}BAD END{/font}"
    #Avi plays

    # -??? end- would show up on screen.

    return

    #"MAIN ROUTE"

label mainroute1:

    show screen route_indicator("Main route")

    "Eiichi decides to walk through the half open door."

    scene bg HouseRoom
    "The room was definitely not what he expected."
    hide screen route_indicator
    "Instead, it was a messy office with papers, boxes, bookcases, and a lit up computer."
    "The room had no windows, nothing but a lamp with no shade."
    "The room's floor was filled with papers, photos."
    "It was the exact description of what a NEET's room would be like."
    "Eiichi took the opportunity to seek what he had thought back at home."
    "It wasn't even planned at all, but he decided to go with the flow."
    "Eiichi walked across mountains of papers towards the desk."
    "Once at the desk, he notices a door besides the bookcase."
    "He decided not to get to the door yet. He shuffled through the papers on the desk, soon to run across a notebook."
    "The notebook was titled, \"My 30 day Diary.\"."
    "It had no name on it."
    "Eiichi sat down next to the huge pile of books next to the desk."
    "He was about to read the diary."
    "He assumed it was Minami's diary."
    "Eiichi knew Minami had a thing for writing."
    "In fact she loved to write."
    "Eiichi was curious what Minami's diary could contain."
    "Eiichi opened the book, and on the first page he realized this wasn't Minami's book."
    "This was Takehito's book."
    "Eiichi has never seen Takehito open a single book in his life,"
    "Let alone write a diary."
    "Eiichi was intrigued."
    "The first page surprised him."
    "Actually, it did more than that."
    "He was spooked, disturbed."
    "The first page was something he was looking for all along, but wasn't what he was expecting to find."
    "Eiichi read through the second page, and was even more horrified."
    "He found out their little {font=[gui.name_text_font]}perfect{/font} couple status was a facade."
    "Finally, something to make Eiichi happy"
    "Or... so he thought"
    "Reading this didn't make Eiichi happy..."
    "He felt worried."
    "This actually concerned him."
    "Eiichi remembers the story Takehito told about how he met Minami."
    "The flashback goes on:"
    show bg white
    takehito "I was an outcast for all of my years of primary school."
    takehito "The 3 girls who bullied me always put me through such torture."
    takehito "I came home with bruises, missing shoes, my hair burnt."
    takehito "They were one of the most brutal bullies you could have ever known."
    takehito "The last year of primary school. Minami transferred into my school."
    takehito "Minami was the most popular girl in school instantly."
    takehito "Everyone adored her looks, her smile, her kindness, her intelligence."
    takehito "She was a diamond in the dump."
    takehito "Everyone told her to stay away from me."
    takehito "Because I was an outcast, people pushed her away from me."
    takehito "It was one day, where she saw me get beat up by those 3 girls."
    takehito "It was the usual for me.. it hurt as usual."
    takehito "I dealt with it. but Minami stood up for me."
    takehito "When she stood up for me, she went from the popular girl to the outcast just like me."
    takehito "But minami didn't mind."
    takehito "She told me she never saw someone go through such inhuman acts and deal with these acts every day."
    takehito "Minami sacrified everything to become like me. to get the same treatment like me."
    takehito "But she got it worst because she was a girl."
    takehito "It was a truly brutal year for both of us."
    takehito "The first year of middle school was horrible, until one day."
    takehito "There was a outcast in middle school that our 3 bullies also attacked."
    takehito "But they chose the wrong person."
    takehito "The guy was done with everything."
    takehito "The whole school saw something... different."
    takehito "He took the bullying, then left without his usual tears."
    takehito "The next day, all 4 of them went missing."
    takehito "It took weeks for them to find all 4 of them."
    takehito "The police just stopped searching."
    takehito "My 2nd year of high school, they finally found them in an abandoned building."
    takehito "They only found the guy alive. the 3 girls were dead."
    takehito "But it was the most disgusting scene you could ever imagine."
    takehito "I remember seeing it on the news."
    takehito "Even the police officers were crying after walking into that \"tragic\" scene."
    takehito "Minami and I didn't think it was tragic. We were the only ones who appreciated what he did."
    takehito "He did something we weren't brave enough to do."
    takehito "He did something I wasn't brave enough to do."
    takehito "Even though he took it too far, it was satisfying to hear the descriptions of that scene from multiple police officers."
    takehito "He saved us torture for the rest of our lives."
    takehito "And Minami and I were happy."
    takehito "We've been happy ever since.."
    "Flashback returns."
    scene bg HouseRoom
    "Eiichi realized his story was nothing but a lie.."
    "because.."

    $quick_menu = False
    call screen demo_warning("This is the {size=+20}Demo Version{/size}\n To see the rest of the story, please wait to the full version!\n\nPlease follow {a=https://twitter.com/IzanamiParadoxV}@IzanamiParadoxV{/a} on Twitter for more information!", 36)


    #Warning pops up saying:

    #This ends here. This is only a demo. To see the rest of the story, please wait to the full version! Follow @izanamiparadoxV for more information!

    return
