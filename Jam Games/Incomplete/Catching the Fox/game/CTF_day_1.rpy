# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label mon1_morning:
    
    $Sol_pts = GetPoints('Solomon')
    $Milo_pts = GetPoints('Milo')
    $Joel_pts = GetPoints('Joel')
    
    scene black with dissolve

    show text "{size=60}Five Years Later{/size}\nMay 21st, 20XX" with Pause(3.0)
    
    play music "music/home.wav"
    
    scene west_home with pixellate
    
    show screen screen_TOD_indicator_sml()
    $ currentTimeOfDay = 0 # 0 = morning
    
    "Current Points:\nkindness = [stat_kindness],
     honesty = [stat_honesty],
     intellect = [stat_intellect],
     dependability = [stat_dependability],
     imagination = [stat_imagination],
     laziness = [stat_laziness]"
    
    window show
    
    show simone thinking at cleft
    
    si "\"Got my keys, got my phone--\""
    
    #phone ring tone sound effect
    show simone surprised
    
    si "\"Hm?\""
    
    si "\"Hello?\""
    
    tr "\"Oh, great, you're awake!\""
    
    tr "\"Last night, we talked about the wedding so long, I got worried that you wouldn't wake up on time for work.\""
    show simone smile
    
    si "\"No, no, I did. I'm just about to leave out now, actually. I still can't believe you're getting married in two weeks!\""
    
    tr "\"I can, trust me. It couldn't come fast enough.\""
    show simone sigh
    
    si "\"Mhm...\""
    
    "She pauses."
    
    tr "\"I avoided mentioning it last night but... are you still upset about not having a date to the wedding? I keep trying to tell you that it really doesn't matter if my sister comes with a date and you don't--\""
    show simone incredulous
    
    si "\"Except it does because I can't stand Nhung. Since we were kids, she's always tried to one up me and I just can't anymore, Trina. {w}Her very {i}presence{/i} irks my soul.\""
    show simone sad
    
    si "\"Even if by some miracle, I {i}did{/i} show up with a date, she'd probably show up with six--one from each continent, plus a scientist from Antarctica for good measure!\""
    show simone angry
    
    si "\"And honestly! {w}When I woke up, I {i}wasn't{/i} thinking about it at all but now that you've reminded me, I can experience my first emotion of the day. {w}Bitterness.\""
    
    tr "\"I'm sorry! I mean, something could happen in the next two weeks and you--\""
    
    si "\"{i}Extreme{/i} bitterness.\""
    
    tr "\"Okay, okay, forget I said anything, you big baby. What {i}were{/i} you thinking about then?\""
    show simone thinking
    
    si "{i}Well{/i}, I just woke up from a weird dream about my first interview with 5/7. \""
    
    tr "\"Oh, wow! With the eyebrow lady?\""
    show simone uncomf
    
    si "...I still can't believe you named one of the drinks on the menu 'De-Brow of Levitation.'\""
    
    tr "\"And {i}I'm{/i} still not sorry that I did. How could I let such a moment of comedic genius fade away in the hallowed halls of comics past?\""
    
    "She lets out a loud laugh, then sighs. I can still hear the smile in her voice."
    
    tr "\"...Simone, can you believe it's been five whole years?\""
    
    "I snort aloud."
    show simone sigh
    
    si "Oh, I believe it, alright. Every day I wake up {i}not{/i} as an intern is a blessed one, in my opinion.\""
    
    tr "\"Well, can't deny that.\""
    
    tr "\"Oh! {w}Since you're already awake, I probably shouldn't hold you up. Isn't today the day you report to your new senior editor?\""
    
    "She's right, of course. It comes to me as no surprise that Trina's more on top of my schedule than I am."
    
    "As much as I enjoyed being a copy-editor for 'The Daily Dollar', I am beyond ready to move on. One can edit but so many articles about finance before losing their mind."
    
    tr "\"See? New magazine, new day. Maybe you'll meet that hottie you told me about from the photocopier incident.\""
    
    si "\"Didn't you promise me that we'd never speak of that again?\""
    
    tr "\"Yeah, yeah. I still think I should've named a drink after that incident, too. Just imagine, customer after customer coming in to order a tall 'Xerox Machine of Doom.'\""
    
    tr "\"It'd be coffee, a dark roast as black as ink.\""
    show simone bored
    
    si "\"...You really do like to hurt me, don't you?\""
    
    tr "\"Ah, don't be so hung up on it! If {i}I{/i} recall correctly, you were the one all, {i}'Not all heroes wear capes, Trina.'{/i}\""
    
    tr "\"{i}'Right when I thought it was the pits, he came in like a herald of light, stapler in hand, and helped me put together those two hundred--'{/i}\""
    
    si  worried "\"First of all, the fact that you remember my exact words is highly disturbing, and second, let's stop talking about this. {w}Please.\""
    show simone uncomf
    
    si "\"That utter {i}nightmare{/i} was four months into my internship and it almost cost me my job. And it was actual factual years ago. So please, for the love of all that is good and holy, forget about it.\""
    
    si "\"For all I know, he might not even work for 5/7 Publishing anymore.\""
    
    tr "\"For all you know. Which is nothing.\""
    
    si "\"He might've been a guest and not even a full on employee!\""
    
    tr "\"But he might not have been one.\""
    
    si "\"Trina, I never even learned his name.\""
    
    tr "\"Bet you remember his face, though.\""
    
    "Touché."
    show simone angry
    
    si "\"...Don't you have a café to be opening somewhere?\""
    
    "Trina just laughs."
    
    tr "\"Bye, Simone. See you soon, I'm sure.\""
    
    "We hang up, and I sling a jacket over my arm and hit the door."
    
    scene black with dissolve
    
    scene trina_cafe with pixellate
    
    "As I do every morning before work, I make a stop at Trina's for breakfast and more banter."
    
    "Like clockwork, she's outside right as I approach."
    
    show trina surprised at cright with dissolve
    
    tr "\"Oh, good, you made it! I was starting to worry.\""
    
    show simone depressed at cleft with dissolve
    
    si "\"I left right after we hung up but traffic was awful.\""
    
    show trina disappointed at cright with dissolve
    
    "Trina looks at me guiltily, but I pretend that I don't notice."
    
    "With her getting married and all, I had to move out from our formerly shared apartment above the coffee shop a few weeks ago. {w}With my space vacated, he could move in with her so she could still be close to the business."
    
    "It's not like it bothers me, but since commuting isn't quite my strong suit, Trina still feels obliged to call me in the morning to make sure I'm awake."
    
    "The puppy eyes weigh on me more than moving out ever did, so I hastily change the subject."
    show simone smile
    
    si "\"Can I have--\""
    
    show trina neutral at cright with dissolve
    
    #half-smile
    
    "She holds out a paper bag."
    
    tr "\"Already taken care of. I had it made for you and even threw in a bagel. {w}Your caffeine addiction is a little worrying, by the way.\""
    show simone uncomf
    
    si "\"...says the owner of a coffee shop.\""
    
    "Trina's tone is defensive but her face betrays the fact that she doesn't mind at all."
    
    show trina happy
    tr "\"Hey, now! We cater, too!\""
    
    "I take the offered cup and gesture with it."
    show simone happy
    
    si "\"On the house?\""
    
    #happy
    
    show trina neutral
    tr "\"Don't be cheap, Simone.\""
    
    menu:
        
        "{i}'Don't be cheap, huh?'{/i}"
    
        "Accept the price.": #honesty
            
            $ stat_honesty +=1
    
            si sigh "\"Alright, alright.\""
            
            si "\"But I want you to know you're a hater.\""
            
            tr smirk "\"A hater who's paying for a wedding.\""
            
            "I grin teasingly."
            
            si "\"Wedding, schmedding. You just want my money.\""
            
            tr happy "\"You're right.\""
            
        "Protest.": #intellect
            
            $ stat_intellect +=1
            
            si uncomf "\"You seriously want me to pay for a meal that {i}you{/i} made for me in advance?\""
            
            tr neutral "\"What can I say? I'm a businesswoman who knows her clients.\""
            
            si "\"That's extortion.\""
            
            tr happy "\"Welcome to the highway, meet the bandit.\""
            
            show simone sigh at cleft with dissolve
            
            "I roll my eyes, opting to take a deep whiff of the coffee rather than acknowledge her tomfoolery."
            
            tr neutral "\"Aw, come on, don't ignore me. That was funny! {w}And since you're totally not sick of my antics...\""
            
        "Bargain.": #imagination
            
            $ stat_imagination +=1
            
            si "\"Aw, come on. You know I'm too cute to pay full price.\""
            
            tr disappointed "\"Hmmm, I feel a rude awakening approaching...\""
            
            si "\"Come on, don't doubt my greater judgement. {w}After all, my greater judgement also says that you're too cute to charge me full price.\""
            
            tr neutral "\"Fine. The coffee is free. Bagel's still full price though.\""
            
            "She rummages in her apron pocket and tosses me a packet of cream cheese spread."
            
            tr "\"And of course, you'll be showering me with your goodwill as thanks?\""
            
            si bored "\"Meaning what, exactly?\""
    
    tr happy "\"If you can, you should come by at lunch, too!\""
    
    tr smirk "\"Just make sure to bring a bunch of your rich, new co-workers with you, too.\""
    
    "I scoff."
    show simone uncomf
    
    si "\"Trina, 5/7 is right down the street.\""
    
    tr "\"So?\""
    show simone surprised
    
    si "\"You know as well as I do that people from work come here for lunch all the time. {i}Meaning{/i} you'd probably recognize them before me, too.\""
    
    show trina neutral at cright with dissolve
    
    "She shrugs bashfully."
    
    tr happy "\"Fair enough. {w}Anyway, you're going to be late if you keep hovering here.\""
    show simone smile
    
    si "\"Right!\""
    
    "I thank her again and, waving good bye, rush off to the office."
    
    stop music fadeout 1.0
    
    scene black with dissolve
    
    scene office with pixellate
    
    play music "music/work.mp3"
    
    "When the elevator doors open, I step off onto the unfamiliar floor."
    
    "As unprofessional as it may be, it occurs to me that I don't even know the name of my new publication."
    
    "I'd gotten the email about the transfer when I was out with Trina and because I like to keep my work and private lives separate, I... admittedly I didn't check it at the time."
    
    "And promptly forgot to do so."
    
    "Can't blame me for being busy, though--tax articles don't edit themselves."
    
    "The executive secretary eyes me, presumably waiting for me to speak. I take a moment to note his name tag, then meet his eyes. As expected, the moment we make eye contact, he speaks."
    
    se "\"Can I help you?\""
    
    show simone surprised at cleft
    with dissolve
    
    si "\"Oh!\""
    show simone smile
    
    si "\"I just want to make sure I'm on the right floor.\""
    
    se "\"This is the floor for Cufflinks, the flagship publication of...\""
    
    show simone surprised at cleft
    with dissolve
    
    "His voice filters to the background as he hands me a business card, and although the words are right in front of me, I can scarcely believe what I'm reading."
    
    "There's no way... {w}I got transferred to Cufflinks?"
    
    "As in... {b}Cufflinks{/b} Cufflinks?"
    
    "The shock washing over me like a wave, I take out my phone to read the email--half to reassure myself I'm in the right place, half to prove myself wrong--when a warm, deep voice surprises me."
    
    z "\"Excuse me, are you the new transfer?\""
    
    "I turn around."
    
    show solomon neutral at cright with dissolve
    
    "I was already grasping at straws for some composure, but this one takes the cake."
    
    "I don't know his name, but Trina's smug voice echoes in my head--"
    
    "\"Bet you didn't forget his face, though.\""
    
    "She's 100\% right--without a doubt, it's that guy from the photocopier incident!"
    show simone uncomf
    
    si "\"Oh, that's... that's me. I'm--\""
    
    z "\"Ms. West.\""
    
    "I swear I feel my blood pressure drop when he says my name. Please don't tell me he recognizes me, too."
    
    "Don't get me wrong--{w}any other time, I'd be {i}beyond{/i} thrilled that someone in my new office has taken note of me, but considering he might remember the lowest moment of my then-budding career, I can't say that such a first impression would be very... {w}flattering."
    
    show solomon smile at cright with dissolve
    
    "He holds out a hand accompanied with a warm smile."
    
    "When I take it, the man envelopes my hand in both of his and gives it a firm shake. Chuckling at my obvious surprise, he lets go."
    
    show solomon neutral at cright with dissolve
    
    z "\"Don't worry, Ms. West. I'm well acquainted with both you and your work.\""
    show simone uncomf
    
    si "\"In what... way?\""
    
    "I feign ignorance, just in case he's addressing The Xerox Incident, but he mostly just looks surprised."
    
    z "\"I heard about the work you did for the accounting magazine on the ninth floor.\""
    
    "He lowers his voice and leans in secretively."
    
    show solomon smile at cright with dissolve
    
    z "\"I've only been in this position for two years, but if there's one thing my mentor ever left with me, it's that you should never let competance go to waste.\""
    
    "I brighten at that--if he remembers me as competant, then he probably doesn't remember me."
    show simone happy
    
    si "\"It sounds like you, um, had an excellent mentor.\""
    
    show solomon neutral at cright with dissolve
    
    z "\"There are some moments more than others where I certainly agree.\""
    
    "It might be my imagination but his eyes linger on my face a little longer than necessary, his gaze mildly appraising."
    
    si "\"I'm pleased to meet you. And you are?\""
    
    "And then the bright smile's back, accompanied by a mischievous wink."
    
    show solomon smile at cright with dissolve
    
    z "\"Solomon Fox, Editor-in-Chief.\""
    
    "So in other words... my boss."
    
    so "\"I wish I could spend a little time showing you the ropes but I've got an unnecessarily full schedule.\""
    
    so "\"I've assigned our resident fashion editor to lend a hand. Mr. Matthews is one of my best and I don't doubt you're a quick study if your reputation is anything to go by.\""
    
    so serious "\"Just a second, Ms. West.\""
    
    hide solomon
    show simone surprised
    with dissolve
    
    "As he turns away to pin some kind of sheet on a corkboard, it dawns on me that he hasn't called me by my first time."
    
    "He must be the formal type, so I may as well reciprocate."
    
    "\"Mr. Fox.\" {w}Has a nice ring to it."
    
    "I'm trying my best not to stare but... it's really him."
    
    "There's no mistaking the crisp British accent and those eyes. They're exactly the same as when I first saw them."
    
    "He looks just as good as he did four years ago when he sat at the table stapling two-hundred sets of printouts and single-handedly saving my job on the worst day of my life."
    
    "So far, anyway. There's always room for more after all."
    
    "I always thought that Trina gave off good vibes, but this level of prediction is just..."
    
    "I paste a smile back on my face."
    
    show simone smile
    show solomon smile at cright
    with dissolve
    
    so "\"Sorry about that. {w}So, Mr. Matthews isn't in right now. In the meantime, the least I can do is give you a brief rundown of our office so you can be acquainted with your new workspace.\""
    
    hide solomon
    
    hide simone
    
    #OFFICE MAP
    
    window hide
    
    show map with moveinbottom
    
    so "\"Of course, we're in the lobby right now.\""
    
    show licon with dissolve
    
    so "\"If you need to run to get lunch or dinner, of course, you'd have to cross through the lobby.\""
    
    hide licon with dissolve
    
    show sicon with dissolve
    
    so "\"My office is this far room on the right. If you need anything, just let me know and it'll be yours.\""
    
    "Oh? {w}Sounds interesting."
    
    so "\"I like to make sure my employees are well equipped with anything they could ever need--{w}for their work, of course.\""
    
    "Oh. {w}Less interesting."
    
    hide sicon with dissolve
    
    show cicon with dissolve
    
    so "\"If you need to host any conference calls, this'll be the room. Of course, we also have meetings here. I'll always send out emails before meetings, so don't worry too much.\""
    
    hide cicon with dissolve
    
    show micon with dissolve
    
    so "\"This is the desk space of Mr. Matthews, the fashion editor... I'm sure you'll be working closely with him as copy editor.\""
    
    so "\"He'll be in later.\""
    
    hide micon with dissolve
    
    show jicon with dissolve
    
    so "\"Mr. Cabrara, our intern, doesn't have a desk, but he tends to hover around my office.\""
    
    so "\"I'm sure you won't have too much of a hard time trying to find him.\""
    
    hide jicon with dissolve
    
    show kicon with dissolve
    
    so "\"Last but not least, the kitchen!\""
    
    "The tour is going pretty swimmingly--but as soon as he says 'kitchen', a chill goes down my back."
    
    hide map
    hide kicon
    show past_filter
    with pixellate
    
    ##greyscale everything cause it's a memory
    
    ob "\"There's dishes that need washing, West.\""
    
    sin "\"Excuse me?\""
    
    ob "\"Was I unclear?\""
    
    sin "\"No, I heard you crystal, but--\""
    
    ob "\"But?\""
    
    sin "\"B-but that's... that's not in my job description! I did {i}not{/i} join this company just to be an office maid!\""
    
    ob "\"Too good to do a little cleaning, hm? {w}Well, before you get uppity, just look around you. Is there anyone else in this room whose job is as expendable as yours?\""
    
    sin "\"Expendable?\""
    
    ob "\"I don't see any other interns on this floor.\""
    
    sin "\"...\""
    
    ob "\"That's what I thought. This breakroom should be sparkling under your care. I know how eager you are to please, after all.\""
    
    hide past_filter
    show map
    show kicon
    with pixellate
    
    ##back to the present
    
    window show
    
    "I don't know why I thought of it now, but I feel myself stiffen."
    
    "I'm not an expendable intern anymore, but I am well aware that some departments treated new transfers worse than others."
    
    "I can only hope that I'm on the better end of the spectrum."
    
    so "\"It's the most important place in the office, and I'm sure you'll find yourself in here more often than you'd like to admit.\""
    
    "I have a distinct sinking feeling in my stomach."
    
    so "\"You drink coffee?\""
    
    "I smile weakly."
    
    si "\"Every morning, Mr. Fox.\""
    
    so "\"After all, Mr. Cabrera makes excellent coffee and like all great masterpieces, he tends to hover in the kitchen and take his time with it. Be sure to grab a cup when you get a chance.\""
    
    "Right, there's already an intern here. {w}I feel a little guilty for being so relieved but... better him than me."
    
    "Solomon moves on."
    
    so "\"Over here is the bathroom, and of course that's the lobby.\""
    
    so "\"These cubicles are for the main staff and this one will be yours.\""
    
    "He lets out the same rolling chuckle, a teasing light in his eyes."
    
    so "\"It's right outside my office so make sure you're actually working because when my door's open, I can see your screen--regardless of if I actually want to.\""
    
    #HIDE MAP
    hide kicon
    hide map with moveouttop
    
    show solomon disappointed at cright
    show simone smile at cleft
    with dissolve
    
    "He's joking but he looks a little uncomfortable all the same."
    
    "I'm guessing he's seen some things."
    
    "Shaking it off, he gestures at me."
    
    show solomon neutral at cright with dissolve
    
    so "\"If you'll just follow me--\""
    
    show joel surprised at right with moveinright
    
    z "\"Sir!\""
    
    "A young man approaches Solomon, a stack of folders cradled in his arms."
    
    so smile "\"Oh, Mr. Cabrera. {w}Have you met our new copy-editor?\""
    show simone happy
    
    si "\"Hello, nice to meet you...\""
    
    "I trail off to allow space for an introduction, especially since I only know his last name, but \"Mr. Cabrera\" gives me a rushed greeting."
    
    z "\"Oh, um, yes. Hello. Listen, boss, I'm sorry to interrupt because you know how I hate to bother you but a-actually...\""
    
    show simone neutral with dissolve
    
    so serious "\"There's a problem.\""
    
    show joel sigh with dissolve
    
    z "\"Not just a {i}problem{/i}--we have a full-blown emergency on our hands.\""
    
    z "\"Some of the Art Department staff are saying the newer deadline for the article on the Mouangue Collection is too soon and they can't get the photos in to Edison in time to pre-format them.\""
    
    so disappointed "\"And Pierre is... where in all of this?\""
    
    "The intern shoots him a queasy look."
    
    so sigh "\"Of course.\""
    
    "Solomon lets out a sigh, meeting my eyes with a regretful sigh."
    
    so neutral "\"I did mention that I'm obscenely busy, right?\""
    
    "He turns his attention back to the young man, who I notice stands straighter."
    
    so "\"Mr. Cabrera, thanks for letting me know. I'll be right on it.\""
    
    so sigh "\"Ms. West, I'm sorry--I'll be back a little later. Why don't the two of you acquaint yourselves with each other while I'm gone? I have some important calls to make.\""
    
    show simone smile with dissolve
    
    si "Sounds good and don't worry about it. I appreciate the partial tour, at least."
    
    hide solomon with dissolve
    
    "He disappears into the room he'd spoken of as his personal office."
    
    show joel surprised at cright with dissolve
    
    z "\"...\""
    
    "Mr. Cabrera stares at me silently for a long, uncomfortable moment. He'd been fine a moment ago talking to Solomon, so I can't help but wonder what his reluctance to speak is for--"
    
    show j blush2 at cright
    with dissolve
    
    "And even though he's the one doing the staring, strangely enough, he's also starting to sweat."
    
    show simone sigh with dissolve
    
    "Well, then. {w}I guess I'll be the one starting introductions since Mr. Cabrera has his whole deer-in-the-headlights concept going for him."
    show simone smile
    
    si "\"Hi, I'm Simone. I was just transferred here so today's my first day at 'Cufflinks.'\""
    
    hide j blush2
    
    show joel disappointed with dissolve
    
    z "\"I-I know, sorry. {w}You just, uhm, weren't what I was expecting.\""
    
    "Oh? The comment is too vague for me to pinpoint his meaning, so I look at him pointedly."
    
    "I tease him lightly."
    show simone happy
    
    si "\"Am I even better?\""
    
    show joel surprised with dissolve
    
    z "\"Better?\""

    "He blinks at me so I rephrase the question."
    show simone surprised
    
    si "\"Well, what were you expecting?\""
    
    show joel serious with dissolve
    
    z "\"Ah... well... I g-guess I didn't expect you to be so...\""
    
    si "\"So...?\""
    
    show j blush2 at cright with dissolve
    
    z "\"...\""
    
    "I look at him expectantly, waiting for him to finish his statement--or to at least drop a last name and basic introductory details."
    
    "Instead of responding, he starts to laugh nervously."
    
    "...Alrighty then."
    
    "It's not too hard to guess his job at least--even if Solomon hadn't told me, Joel has the distinct look of an intern. I'd never met someone so..."
    
    "It's only then that I realize I'm staring. And the only reason I note it is because he looks slightly sweatier than before."
    
    hide j blush2
    show joel neutral at cright with dissolve
    
    z "\"S-sorry, I-I'm Joel. Joel Cabrera.\""
    
    "Joel Cabrera, got it. Hm, interesting."
    show simone happy
    
    si "\"Wow, what a coincidence.\""
    
    jo surprised "\"Huh? What is?\""
    show simone smile
    
    si "\"Your last name. {w}It's Cabrera, just like Miguel Cabrera, the company founder? I met him once, you know. He's nicer than you'd expect for somebody so loaded.\""
    
    "I make the joke to help the poor kid lighten up but he just smiles awkwardly instead."
    
    jo serious "\"Ah, yeah, he's really... down-to-earth.\""
    
    si "\"Nice, have you met him too?\""
    
    show j blush at cright
    show joel surprised at cright
    with dissolve
    
    "Joel reddens, his mouth opening, then shutting. He hums and haws for a few more seconds before settling on something to say."
    
    jo "\"Ah, well, uhm... sort of.\""
    
    jo serious "\"He's my uncle.\""
    
    "Wow. {w}That's not 'sort of' at all."
    
    show simone surprised with dissolve
    
    "It's hard not to let my jaw drop, but I manage. If Joel didn't seem so genuinely embarrassed, I'd find it impossible to believe."
    
    "You can't blame me though--Miguel Cabrera is a man that, even in his sixties, oozed enough charisma to make a three-piece suit jealous."
    
    "I'd only met him once when he came to the office for a peer review but by the time he'd left even my training manager was bowing over himself to appease him."
    
    "I won't say I didn't enjoy it but..."
    
    "Well, anyway."
    
    "I touch his arm lightly."
    show simone happy
    
    si "\"You don't have to be so shy about your silver spoon. I promise I won't treat you any differently.\""
    
    "Joel looks nervous, but I think I'm starting to understand that nervousness is simply his default expression."
    
    jo neutral "\"A-actually, no silver spoon to be found--at least not in the Cabrera-Silva household. I grew up in the countryside.\""
    show simone surprised
    
    si "\"{i}Ooh{/i}, a farmboy?\""
    
    "He nods."
    
    jo serious "\"I come from a long line of {i}rancheros{/i}, to be specific.\""
    
    si neutral"\"A fashionable bi-lingual farmboy, then?\""
    
    "I wink playfully."
    show simone happy
    
    si "\"I'll bet you know your way around a haystack. I give you a call when I need a man to find a needle.\""
    
    show joel neutral at cright with dissolve
    
    "Joel offers a timid, slightly brighter smile."
    
    jo "\"I don't know about fashionable... My uncle did give me this job, admittedly. But I should say, I do prefer horses to hay.\""
    show simone thinking
    
    si "\"Hm... now that I think about it I've never ridden a horse--raised strictly in the concrete jungle and all.\""
    
    jo "\"You should try it sometime. I mean, I-I'm pretty good at that kind of thing, but it's not really useful in the big city, you know?\""
    show simone incredulous
    
    si "\"Honestly, my skills lie elsewhere--but I'll keep it in mind."
    
    jo "\"Besides, Solomon thinks so well of you... He said you were going to bring a lot to the team and to the magazine in general--l-like Lois Lane to our Daily Planet.\""
    
    show simone surprised with dissolve
    
    "My phone buzzes in my pocket, distracting me."
    
    show simone smile with dissolve
    
    "{i}Ooh, my manucurist is free on Wednesday. Good to know.{/i}"
    
    jo smile "\"{size=-6}A lot more beautiful though.{/size}\""
    show simone happy
    
    si "\"...{w}Sorry, what was that? I got distracted.\""
    
    jo surprised "\"N-nothing! Nothing, sorry. Nothing.\""
    
    jo "\"I-I-I have work to do, and I-I should go and, um, do that. Work. Now.\""
    
    jo neutral "\"Milo's supposed to be helping you around the office, right?\""
    
    si "\"That's \"Mr. Matthews\", right? If yes, then apparently so, but he's out at the moment.\""
    
    jo serious "Yeah... that's him."
    show simone smile
    
    si "\"It was nice meeting you, Joel--I'll wander around a little bit and get to know the office as best I can in the meantime.\""
    
    jo smile "\"I'll be right back, Ms. West--\""
    show simone happy
    
    si "\"Sure. But Joel, just call me 'Simone', alright?\""
    
    show j blush at cright with dissolve
    
    "He flushes, still smiling sweetly."
    
    jo "\"Okay. Simone. {w}I, um, I need to go get the mail cart but I'll be back...\""
    
    jo serious "\"If Milo comes by, can you give him these for me?\""
    
    "I shrug. {w}It shouldn't be too inconvenient and honestly, Joel seems like he needs the type of friend to step in to cover a favor or two."
    
    "I wonder why he's so nervous. Solomon doesn't seem like a particularly over-demanding boss to work under so..."
    
    "Mystery unsolved, I pop into the kitchen to grab myself some water as Joel disappears toward the lobby, leaving me to my own devices."
    
    hide joel serious
    
    hide j blush
    
    scene o_kitchen
    show simone bored at cleft
    with blinds
    
    si "\"...\""
    
    "Of which I have none."
    
    "No matter--there's no better time than the present to acquaint myself with this room, especially if I was going to be working long into the night."
    
    "As I survey the kitchen, my phone buzzes quietly in my pocket."
    
    "It's an email from Trina."
    
    "Smart, since I won't be able to use my phone at the desk."
    
    "I'm technically at work so I really shouldn't, but--"
    
    "Right when I'm about to open the email client, the door swings open. Even though I'm technically not working anyway, I jump, feeling strangely caught."
    
    show milo serious at cright
    with dissolve
    show simone smile
    
    si "\"Oh! Hi, I'm--\""
    
    z "\"Yeah, yeah, the new chick.\""
    
    show simone surprised with dissolve
    
    z "\"No need for niceties. I work here.\""
    
    "He sounds disgruntled as he shuffles through the drawers, pulling out a white mug from one of the cabinets."
    
    "Now... usually, I can handle disgruntled. {w}In fact, you could say that I'm {i}employed{/i} to handle disgruntled since I'm a professional who edits creative types, the most sensitive bunch of children on this planet, but..."
    
    "Maybe it's the fact that he's caught me so offguard that I find myself bristling."
    
    "I mean, really. 'New chick?' {w}{b}'New chick?'{/b}"
    
    "If he was going to make the effort to grace my presence with his then he could've taken the time to learn my name."
    
    "He doesn't even have an excuse not to know it either--I'd passed by a notice board when I came in and my transfer notice was clearly posted with my full name on it."
    
    show milo serious at cright with dissolve
    show simone uncomf
    
    si "\"My name is Simone West. And you must be...?\""
    
    "A little bit of sarcasm sneaks its way in. Call me petty."
    show simone bored
    
    si "\"Please, remind me. I'm sure your name would ring a bell--{w}if I've heard of it.\""
    
    show milo sigh at cright with dissolve
    
    z "\"Matthews. {w}Milo Matthews.\""
    show simone thinking
    
    si "\"Matthews, Matthews...\""
    show simone sigh
    
    si "\"Nope, crickets.\""
    
    "He scoffs."
    show simone incredulous
    
    si "\"Honestly, I'm as surprised as you are. Someone so important would've definitely left an impression but... the name 'Matthews' brings absolutely nothing to mind.\""
    show simone smile
    
    si "\"If you're as important as you say I'm sure I would've at least heard of you. {w}But then again, people do tend to forget to tell things to the 'new chick.'\""
    
    "It's a lie--both Joel and Solomon himself have mentioned him to me by name--{w}but he doesn't need to know that."
    
    "I'm starting to wonder about Solomon's judgment, though."
    
    show simone sigh with dissolve
    
    "{i}This{/i} is the guy he wants to show me the ropes?"
    
    "He looks like he couldn't show a chicken out of an egg."
    
    "Milo snorts at me, either deciding I'm not an easy target or that I've got issues and he doesn't want to be bothered with me. Whatever he's thinking, common sense tells him not to try it."
    
    "He glances around."
    
    mi surprised "\"Where's Joel, anyway? Doesn't he have my coffee ready?\""
    
    "Ah."
    
    "And just like that, the missing work dynamic link clicks into place. {i}This{/i} piece of work must be the reason that Joel's a nervous wreck, mild-mannered Clark Kent or not."
    
    "A rush of annoyance flows through me."
    
    show simone angry with dissolve
    
    "I know how it feels to be treated like the pack mule edition of an intern and I'm not having it."
    
    si "\"Sorry, don't know, don't care. These are yours."
    
    "I pick up the stack of folders Joel gave me earlier and press them forcibly into Milo's chest, earning myself a satisfying {i}'oof.'{/i}"
    
    "He glances down at them with interest, his eyes then flickering to me with something like respect."
    
    mi serious "\"Is this a draft of the new page-seven column?\""
    
    "I have no clue what he's talking about, but I don't feel like honoring him with a reply."
    show simone incredulous
    
    si "\"I don't know, is it? You're the man in charge.\""
    
    show milo neutral at cright with dissolve
    
    "He ignores my sarcasm."
    
    mi "\"So... you're a new journalist, eh?\""
    
    mi "\"I'll have you know that Solomon's particular about the things he approves for publishing so it'd better be in line with the 'Cufflink' standard--especially if you don't want to find yourself writing for Carpet Monthly.\""
    
    mi "\"I don't know what you've been doing before you got here, but you're running with the big dogs now.\""
    
    show simone surprised with dissolve
    
    "Wait, journalist? This guy is clearly mistaken. I'm a copy-editor. I edit drafts, not write them."
    show simone bored
    
    si "\"{i}Actually{/i}, those are--\""
    
    "A cell phone rings, effectively cutting me off as Milo answers it quickly."
    
    #phone ring noise
    
    mi surprised "\"Hello? This is Matthews speaking.\""
    
    mi serious "\"...No, I'm not busy.\""
    show simone angry
    
    si "\"Milo!\""
    
    show milo disappointed at cright with dissolve
    
    "He shoots me a glare over his shoulder and steps away to continue the conversation."
    
    hide milo disappointed with dissolve
    
    "Then proceeds to walk out completely, folder under his arm."
    show simone sigh
    
    si "\"...Great.\""
    
    scene office cubicle with blinds
    
    "I take a seat at my new desk, trying not to feel exasperated. A small shining square on the corner makes me brighten."
    show simone happy
    
    si "\"Look at that, I have a shiny placard with my name on it. {w}{i}Fancy.{/i}\""
    
    "But right about there, it gets a little less exciting."
    show simone sad
    
    si "\"You'd think for a mens' fashion magazine that the interior decorating would be...\""
    
    "Well. {w}Not pitiful."
    
    "A small potted miniature fern droops sadly on the side beside my chair."
    
    si "\"I really need to get some decorations in here.\""
    
    "I look listlessly around the office, completely taskless as employees rush around the room in a blur. Right when I'm about to die from boredom, the only normal person in the entire office returns."
    
    "Hopefully with tasks for me to do."
    
    show solomon neutral at right with dissolve
    
    so "\"Ms. West, I apologize for the wait.\""
    
    "{i}Dream job, Simone. Keep your eye on the prize.{/i}"
    show simone happy
    
    si "\"It was... {w}fine. {w}Fine!\""
    
    si "\"I met Milo and Joel, but uh... Joel went to get the office mail, and Milo got a phone call and went out again.\""
    
    so sigh "\"I see... so no one got to show you around.\""
    
    si "\"On the brightside, so far, your partial tour has been the best.\""
    
    "Solomon claps his hands together."
    
    so smile "\"Well, you know what they say--if you want a job done right, you do it yourself.\""
    
    so "\"Let's get on with it then. Next up...\""
    
    "He opens the door to his office."
    
    so "\"Let me familiarize you with my office.\""
    
    scene black with dissolve
    
    $ currentTimeOfDay = 1 # 0 = noon
    show screen screen_TOD()
    pause 3
    hide screen screen_TOD
    
    scene office cubicle with dissolve
    show simone worried
    
    si "\"I can't believe it's only lunch.\""
    
    "Or I can, because I haven't done much of anything all day."
    
    "I pull out my phone to check the time when I notice the little notification hasn't quite disappeared."
    
    "Trina's email! I still haven't replied yet."
    
    "I turn toward my computer and type in my login. Promotion or no promotion, that shouldn't have changed."
    
    "First order of business--read her email. Second order of business--to give Trina the deets on my new boss and co-workers. Now to click the email browser..."
    
    "{i}What OS do we run here again?{/i}"
    
    window hide
    
    stop music fadeout 1.0
    
    play music "music/wedding.mp3"
    
    $ name = "Simone"
    $ mail = []
    $ mail_later = []
    $ mail_queue = []
    $ contacts = []     
    
    # create a contact the player can send messages to
    #$ Contact_Trina = Contact("Joel", "lbl_Email_Misc_JoelCorrections")
    # to change the draft message, do something like $ fredo.draft = "fred_draft2"
    # $ fredo.delete() if you don't want him on the list anymore (sorry fred)
    
    #$message = GetRelationshipHintEmail("Solomon", 0, 1)
    #$ add_message("Relationship with Solomon", "Trina", ["We seriously need to talk about...Solomon. Specifically {i}me{/i} and Solomon. Together. \nRomantically.", message])
    #$message = GetRelationshipHintEmail("Milo", 0, 1)
    #$ add_message("Relationship with Milo", "Trina",  [message], reply_label="fred_reply")
    #$message = GetRelationshipHintEmail("Solomon", 0, 1)
    #$ add_message("Relationship with Solomon", "Trina",  [message])
    #$message = GetRelationshipHintEmail("Solomon", 0, 1)
    #$ add_message("Relationship with Solomon", "Trina",  "", message)
    #$message = GetRelationshipHintEmail("Joel", 5, 1)
    #$ add_message("Relationship with Joel", "Trina",  "", message)
    #$message = GetRelationshipHintEmail("Solomon", 10, 5)
    #$ add_message("Relationship with Solomon", "Trina",  "", message)
    #$message = GetRelationshipHintEmail("Solomon", 10, 15)
    #$ add_message("Relationship with Solomon", "Trina",  "", message)
    $new_messages = new_message_count()
    #show simone neutral
    #si "\"You now have [new_messages] messages.  Click the overlay to open the inbox."
    
    #si "\"Yes No test"
    #call screen yesno_prompt("Yes no message Test", Return(""),Return(""))
    #si "\"Ok test"    
    #call screen info_prompt("ok message Test", Return(""))
    
    scene black with dissolve
    
    scene comp_bg with dissolve
    
    call lbl_Email_Tutorial_Start from _call_lbl_Email_Tutorial_Start
    
    scene office cubicle
    with dissolve
    
    window show
    
    stop music fadeout 1.0
    
    play music "music/work.mp3"
    
    "Satisfied that I've done my duty as a best friend, I jump at the sight of Joel beside my desk."
    
    scene office
    show joel surprised at cright
    show simone surprised at cleft
    with dissolve
    
    jo "\"O-oh! Sorry to scare you! I just wanted to know h-how your first day is going, Ms. We--erm, Simone?\""
    
    "I shrug my shoulders, gesturing to my empty \"out\" folder."
    show simone bored
    
    si "\"Not much going on in the West, sadly--mostly following people and observing, but that's what first days are like, you know?\""
    show simone thinking
    
    si "\"One thing I can say, though--this office is like a finely tuned machine. I can tell why Solomon was promoted to 5/7's flagship publication as such a young age.\""
    
    show joel neutral at cright with dissolve
    
    "Joel is nodding with me before I can get the sentence fully out."
    
    jo "\"He is! I mean, he's doing his best even with me, you know. I'm not really the most--\""
    
    "I hush him, giving him a light pat on the shoulder."
    
    si depressed "\"Joel, I understand your struggle. It's hard to succeed when you've got someone constantly harping on you.\""
    
    si "\"Whatever that guy's putting you through--don't pay him any mind. Just take it one day at a time, Joel. We were all interns once.\""
    
    "Joel nods slowly, then stops."
    
    jo surprised "\"Wait, don't don't pay 'who' any mind? What do you--\""
    
    hide joel surprised
    
    show joel surprised
    show milo upset at right
    show simone neutral
    with dissolve
    
    mi "\"What is {i}this{/i}?\""
    
    "Speak the devil and he appears."
    
    "Milo approaches us and slaps down the folders he'd taken earlier onto the desk beside us. I glance at them--it's the same ones Joel'd given me."
    
    mi "\"The spacing! Those bizarre margins! You majored in English and your proposals look like {i}this{/i}? What, did you print your degree at the library?\""
    
    show simone incredulous with dissolve
    
    "I'm about to deny it but I note beside me that Joel is trying his best to appear invisible."
    
    hide joel surprised
    hide simone incredulous
    
    show joel surprised at left
    show simone incredulous at cleft
    with dissolve
    
    "He slowly edges behind me."
    
    "Amazing, considering the fact that he's taller than both me {i}and{/i} Milo, but I can't blame him for trying."
    
    "I somehow get the vision of a mouse trying to hide behind a toothpick."
    
    show simone sigh with dissolve
    
    "I sigh inwardly, resigned."
    
    "Even though it's annoying to hear Milo go on, I can't bear to tell him that whatever he's holding actually came from Joel."
    
    "{i}Call me Simone West, defender of the weak.{/i}"
    
    "And anyway, I'm still anticipating the moment he realizes that I'm a new copy-editor."
    
    si "\"...\""
    
    "Wait, has he been talking all this time? Still?"
    
    mi "\"--and I'll expect them on my desk, {i}edited properly{/i}, by this evening.\""
    
    hide milo with dissolve
    
    "And just like that, he stalks off, fuming."
    
    show joel surprised at cright
    with dissolve
    
    "When Joel finally defrosts, he looks down at the folder warily--{w}then stares at it, his expression turning to abject horror."
    
    si "\"What is it?\""
    
    "He offers the folder to me."
    
    jo sigh "\"L-let's just... say I-I know why you didn't have any work to do today?\""
    
    "I look at Joel, blinking once."
    
    show simone surprised with dissolve

    menu:

        "He accidentally gave Milo an unedited set of printouts meant for... me?"

        "It reminds me of the Xerox incident. Poor kid.": #kindness
            
            $ stat_kindness +=1
            
            show simone uncomf with dissolve
            
            "A rush of empathy flows over me."
            
            "I'm reminded of my own crappy intern mistakes and can't help but try to comfort him."
            
            si "\"Don't worry, Joel. I've only been here for a matter of hours and even I know that Milo is a overreacting jerk.\""
    
            si bored "\"For the record, {i}he{/i} is who I was talking about when I said 'don't worry about him.'\""
    
            si "\"I've got your back, Cabrera.\""
            
            show joel surprised with dissolve
            
            "Joel blinks at me, before smiling. I swear I can see flowers blooming around his face."
    
            jo smile "\"Thanks, but... you didn't make the mistake, I did.\""
            
            show simone neutral with dissolve
            
            "I shake my head, but Joel looks at me stubbornly."
            
            jo serious "\"Really, I should be the one to--\""
            
        "I'm not mad. At least I got to relax today.": #laziness

            $ stat_laziness +=1
            
            "I shrug my shoulders mildly."
            
            si neutral "\"Come on, Joel. It could be worse.\""
            
            si bored "\"I mean, was today obscenely boring? Yes. Yes, it was.\""
            
            "I accept the stack of folders."
            
            si thinking "\"Do I want to even {i}look{/i} at these, with the day half over? {w}No. No, I don't.\""
            
            si neutral "\"But it's whatever. I may as well get to work since I have it now.\""
            
            jo serious "\"You're... not mad?\""
            
            si smile "\"Nope. Don't sweat it. I never do.\""
            
        "This is nothing I can't take care of. I'll get it done.": #dependability
            
            $ stat_dependability +=1
            
            "He looks down, reaching for the folder."
            
            jo serious "\"I should just... take care of this. It was my mistake, so--\""
            
            "I laugh, pushing his hands away."
            
            si happy "\"Are you kidding me? I've been bored all day! It would be a {i}breeze{/i} to edit this. {w}A pleasant breeze.\""
            
            jo disappointed "\"B-but--\""
            
            si incredulous "\"Joel, I'm paid to do this. And I love to do it! {w}So step away from my manila folders and no one gets hurt.\""
            
            "Joel doesn't quite look convinced, but a sound interrupts us."
        
    ##phone ringing sound
    
    play sound "sounds/ringing.wav"
    
    "Hm?"
    show simone surprised
    
    si "\"Excuse me, Joel, let me just take this--\""
    
    stop sound
    
    si "\"Hello?\""
    
    so "\"Ms. West, it's Solomon. Mr. Cabrera's not answering his work phone so if you see him before I do, can you tell him to come here? I'll need him for the rest of the afternoon.\""
    
    si neutral "\"Yes, Mr. Fox.\""
    
    "I hang up the phone and look at Joel with a shrug."
    
    si "\"You overheard the man. Get in there.\""
    
    jo disappointed "But... but the corrections--\""
    
    "I sigh aloud."
    show simone sigh
    
    si "\"I'll do it, Joel.\""
    
    jo sigh "But your lunch--\""
    show simone smile
    
    si "\"Don't worry about all that. Now go!\""
    
    "He hesitates before nodding once."
    
    jo smile "Th-thanks again, Simone.\""
    
    window hide
    
    jump mon1_afternoon
    
label mon1_afternoon:
    
    scene black with dissolve
    
    $ currentTimeOfDay = 2
    show screen screen_TOD()
    pause 3
    hide screen screen_TOD
    
    window show
    
    scene office cubicle with dissolve
    
    si "\"Alright, it's the afternoon!\""
    
    "I look around the busy office. The day's almost over but at least I've got some work to do of my own."
    
    "The paper in front of me cheers me up, just a little. {w}There's nothing like hard-copy editing to brighten the mood."
    
    "The afternoon hums by as I work, losing myself in the letters."
    
    scene office cubicle with fade
    
    ## chibi CG simone scribble scribble
    
    si "\"...Oh, come on. Everyone knows that \"douche bag\" has a space. Definitely two words.\""
    
    scene office cubicle with fade
    
    ## chibi CG simone heart heart
    
    si "\"That's a poetic passage. {w}I'm sold.\""
    
    scene office cubicle with fade
    
    "I look up at the clock in satisfaction."
    
    "Almost the entire afternoon gone and I was done."
    
    si "\"They don't call me the Typo Gunslinger for nothing.\""
    
    "Nor do they call me the typo gunslinger at all. {w}Meh."
    
    si "\"Now to get it to Milo...\""
    
    "I place it gingerly in my outbox, knowing that Joel will pick it up and--well, hopefully--deliver it to the right place this time."
    
    si "\"Hm...\""
    
    "The corrections weren't as bad as I thought they'd be judging by Milo's dramatics, but the author definitely needed to improve if he wants to move up in the company."
    
    "{i}Maybe I'll just add a quick note before I send it.{/i}"
    
    "I grab a memo pad from the cubicle beside me and tear out a sheet, then quickly put it back before someone sees me."
    
    menu:
        
        si "\"Let me think...\""
        
        "Give constructive criticism.": #honesty
            
            $ stat_honesty +=1
            
            "{i}\"Hey, I don't want to seem like a teacher, but you made a lot of simple mistakes that can easily be corrected if you're a little more careful.\"{/i}"
            
            "{i}\"For example, the article is called \"The Tux Effect\"--but you wrote \"The Tux {i}Affect{/i}\" instead."
            
            "{i}\"In paragraph six, you accidentally wrote 'tei' instead of 'tie', so looking for spelling mistakes or running it through a spell check might be best, especially when the editor correcting your work is Milo of all people.\"{i}"
            
            "{i}\"Make sure you read through it all very carefully, combing for simple mistakes such has these. And great article!\"{i}"
            
        "Remind Joel to send it on time instead.": #dependability
            
            $ stat_dependability +=1
            
            "But then, no point in writing a note to the author that would never make it in the first place."
            
            "I decide to write a note to Joel instead."
            
            "{i}\"Hey, Joel. Don't forget to get this to Milo by tonight. I don't want him marching to my desk tomorrow because if he comes to me early morning with some foolishness, we might throwdown and it'll look bad for Solomon. Haha.\"{/i}"
            
            "{i}\"Thanks a lot!\"{/i}"
            
        "Try to get a free meal from Joel. It was a favor, after all.": #imagination
            
            $ stat_imagination +=1
            
            "My stomach grumbles quietly."
            
            "And then I remember that I definitely skipped lunch."
            
            "{i}How can I get lunch without leaving the office?{/i}"
            
            "And then it dawns on me. Granted, Joel was responsible for this little mix-up anyway, even if I still ended up doing with work without complaint."
            
            "I scratch out my note cheerfully."
            
            "{i}'You definitely owe me one. I heard you can cook from Solomon. How about we work out some kind of edible form of repayment?'{/i}"
    
    "I place the note on top of the folder into the outbox, stretching."
    
    si "\"Finally.\""
    
    "I feel like I'm forgetting something though... {w}oh! {w}Trina's reminder!"
    
    "{i}\"Don't forget to get off for my final fitting on Thursday.\"{/i}"
    
    si "\"Ah, right!\""
    
    "Trina's wedding is in two weeks and since it's on a Sunday, I definitely won't need to take off--{w}but the final dress fitting is on Thursday. I'll need to leave early for that."
    
    "This is my first day so it won't look good to take off so soon, but... as the maid of honor, Trina would die without me being there."
    
    "Right at that moment, I hear Joel's voice as he leaves Solomon's office."
    
    jo "\"Yes, sir. I'll get it to you right away.\""
    
    show joel smile at right with dissolve
    
    "He glances at me with a slight smile before hastily moving towards the elevator."
    
    hide joel with dissolve
    
    "Hm... that means Solomon's free now..."
    
    si "\"Well, best to get it out of the way.\""
    
    "I push myself backwards from my cubicle and knock on the door to Solomon's office."
    
    so "\"Come in.\""
    
    "I take a breath."
    
    "Come on, Simone! Time to turn up the charm!"
    
    window hide
    
    stop music fadeout 1.0
    play music "music/battle.wav"
    
    call screen preBattle_screen('solomon', "Ask for to leave early to do the dress fitting.", "Be reasonable in your request. It's a new job, so don't come off like a slacker!")
    $WriteToFile("Starting Battle 1")    
    $Battle_FailureLabel = "lbl_battle_1_Failure"
    $Battle_TimeoutLabel = "lbl_battle_1_Timeout"
    
    scene fox_office
    show simone uncomf at cleft
    
    window show
    
    si "\"Hello, Mr. Fox?\""
    
    so "\"Oh, Ms. West. Come in. How was your first day?\""
    show simone happy
    
    si "\"It was great! Joel got some files for me to edit, so I got to work. If possible, though, I'd love some previous examples so that I can make sure that my editing style stays mimics the current in-house style of editing.\""
    
    "He laughs."
    
    so "\"I can do that for you.\""
    
    so "\"Already, I can tell bringing you on board was a good decision. It's good to know that you aren't shy about getting what you need. I'd like to assure you that you can be open about letting me know your needs.\""
    
    so "\"But I'm sure that's not what you came to discuss. How can I help you?\""
    
    "Oh, perfect! There's a window."
    show simone uncomf
    
    si "\"Actually, I'm glad you mentioned it... I know that I'm a new transfer, but I'd like to know--would it be possible for me to be able to take off early on Thursday afternoon?\""

    window hide

    $ResetBattleStatus()
    $Battle_Question_Current = 0
    $SetResult(Battle_Question_Current, 'progress')
    $ResetBattleTimer()
    #show screen Battle_screen_background
    call screen Battle_screen(Battle_1_QuestionList, Battle_1_AnswersList, Battle_1_AnswersLabels,  4, 3)
    
    jump expression _return

    return
    
label B1_fin:
    
    stop music fadeout 1.0
    
    scene office cubicle with dissolve
    
    play music "music/work.mp3"
    
    "I return to my desk, feeling triumphant."
    
    si "\"And that's another win for the Westside.\""
    
    scene black with dissolve
    
    $ currentTimeOfDay = 3 # 0 = noon
    show screen screen_TOD()
    pause 3
    hide screen screen_TOD
    
    scene office cubicle with dissolve
    
    "I'm almost off for the night. Considering how much I struggled to fill my schedule, it's no surprise that there's really not much left to do today..."
    
    si "\"Hm... let me think.\""
    
    "The phone was ringing off the hook when I was on my lunch break so I could return those phone calls."
    
    "Milo is available... I guess I can always see what he's up to. I'd rather not, though."
    
    "There's Solomon--I could always ask him if he has any work for me."
    
    "Joel is probably delivering mail, but he's a sweet kid. I wouldn't mind chatting with him if he's not busy."
    
    "The office kitchen might need to be restocked."
    
    "Or I could run out to grab something for everyone to eat. I may not have been doing much today, but it's been busy for pretty much everyone else. Food would be a good pick-me-up and help the work go more smoothly."
    
    "...And of course, it'll put me in a better light as a newcomer."

    call screen office_work
           
    $ result = _return
        
    if result == "kitchen": #kindness_ restock the kitchen

        call expression renpy.random.choice(EventLabels_KindnessEvening)
        
        jump next_event
        
    elif result == "solomon": #imagination_ she can talk to Solomon!
        
        window show
        
        #call expression renpy.random.choice(EventLabels_ImaginationEvening)
        
        "I just spoke to Solomon but... I guess it'll be fine to drop in again?"
        
        si "\"Kind of awkward, though.\""
        
        "I walk to the door."
        
        si "\"Mr. Fox? Can I come in?\""
        
        scene fox_office
        show simone worried at cleft
        with dissolve
        
        "At the sight of me, Solomon smiles coolly."
        
        show solomon smile at cright with dissolve
        
        so "\"So you've come back for more.\""
        
        "I relax, seeing that he doesn't look annoyed."
        
        si happy "\"What can I say? I'm a glutton for punishment.\""
        
        si neutral "\"Actually, though, I just want to say 'thank you'.\""
        
        so surprised "\"For?\""
        
        si thinking "\"Where do I begin...?\""
        
        si happy "\"\I mean, if I can be frank, this is a highly competitive magazine and a men's magazine on top of that. As a woman, I'm more surprised than I probably should be that you wanted me on board.\""
        
        si "\"In this industry, it's unfortunately rarer than you'd think. I'm grateful the opportunity, Mr. Fox.\""
        
        so neutral "\"Oh, trust and believe, I've noticed. {w}Boss after boss passing over excellent candidates for trivial reasons that wouldn't have been even a blip on their résumés otherwise--{w}but you don't have to worry about that here.\""
        
        so "\"Not in my magazine.\""
        
        so "\"The dream is to make 'Cufflinks' the kind of magazine anyone can aspire to work for--and I'll need the very best to execute it.\""
        
        so smile "\"I might be a little demanding, but I believe you're up for the challenge. Do you?\""
        
        si incredulous "\"Who do you think you're asking?\""
        
        so neutral "\"That's what I'd like to hear.\""
        
        "He laughs sheepishly."
        
        so "\"But you probably didn't drop in to hear me go on either, now did you?\""
        
        si neutral "\"I didn't, true, but I don't mind. You seem... driven. As an employee, it's relieving to have a confident team lead. So, I guess I can thank you for that, too.\""
        
        so "\"It's my pleasure. I'm sorry, I've got to get back to work, but thank you for dropping by. Please--feel free to join me again, any time.\""
        
        window hide
        
        jump next_event
        
    elif result == "calls" : # dependability_ she can make phone calls
        
        call expression renpy.random.choice(EventLabels_DependabilityEvening)
        
        jump next_event
        
    elif result == "milo": #honesty_ start rejecting manuscripts
        
        window show
        
        #call expression renpy.random.choice(EventLabels_HonestyEvening)
        
        "...Ugh..."
        
        "I don't really want to, but I should go speak with Milo."
        
        "Regardless of whether I like him or not, Solomon did intend for him to be the person meant to \"show me the ropes.\" It's probably best to ask him if I have any questions."
        
        scene office
        show simone uncomf at cleft
        with dissolve
        
        "I approach his desk."
        
        "Surprisingly, he looks like he's been expecting me."
        
        show milo disappointed at cright with dissolve
        
        mi "\"Hey, you.\""
        
        "Ugh, what is with his tone? And why is he always looking at me like I did something to him?\""
        
        si sigh "\"Yes, Matthews?\""
        
        mi "\"I...\""
        
        "He won't look me in the eye. Strange.\""
        
        mi serious "{size=-7}\"I'm sorry.\"{/size}"
        
        si uncomf "\"Come again?\""
        
        mi upset "\"I am. {w}{i}Sorry.{/i}\""
        
        mi "\"The paperwork. Joel... told me that I made a mistake so I'm apologizing.\""
        
        mi "\"I still expect a lot from you, so don't think you're off the hook!\""
        
        "He sniffs derisively."
        
        mi disappointed "\"You'd better be on time tomorrow, too.\""
        
        "Milo stalks off quickly."
        
        hide milo with moveoutright
        
        si bored "\"...If you're going to be like that, you may as well have not even bothered to apologize.\""
        
        "I'm pretty sure he heard me, but he doesn't reply anyway."
        
        show simone thinking at cleft with dissolve
        
        "Tsk. I didn't even get to ask him any questions. Maybe I can shoot him an email or something tomorrow."
            
        window hide
        
        jump next_event
        
    elif result == "joel": #laziness
        
        #call expression renpy.random.choice(EventLabels_IntellectEvening)
        
        window show
        
        "As Solomon predicted, Joel is hovering outside of his office."
        
        scene office
        show joel surprised at cright
        with dissolve
        
        "I approach him, making sure he knows I'm there before greeting him by clearing my throat multiple times as I get closer."
        
        "It might seem... extra, but he seems like he scares easy."
        
        show simone neutral at cleft
        with dissolve
            
        jo "\"Simone?\""
        
        si "\"Hey, what's up? You have a minute?\""
        
        jo smile "\"Yeah, I do! I'm just about wrapping up for the day. Actually, though, I'm glad to see you.\""
        
        si incredulous "\"Why? What is it?\""
        
        jo surprised "\"Nothing bad, don't worry! I just wanted to say 'bye', is all. Oh, and thank you. {w}So... uhm... {w}bye. {w}And thank you.\""
        
        si neutral "\"Aw, thanks.\""
        
        "Haha. What a sweetheart."
        
        jo smile "\"What about you, Simone? Are you... going home yet?\""
        
        si sigh "\"Not yet.\""
        
        si neutral "\"I did finish that work, by the way. Thankfully, they made it light on my first day so it wasn't too much.\""
        
        jo serious "\"Ah... that... well, I'm glad it worked out.\""
        
        si incredulous "\"How are you getting home anyway?\""
        
        jo surprised "\"Oh, I usually just catch a cab.\""
        
        show simone thinking with dissolve
            
        "A cab to {i}and{/i} from work? {w}{i}Every{/i} day? {w}Talk about money to blow."
        
        "Still, must be nice."
        
        jo neutral "\"What about you?\""
        
        si neutral "\"I usually take the train but I drove today. I should really get out of here before rush hour traffic.\""
        
        jo "\"Oh, that's true...\""
        
        show joel sigh with dissolve
        
        "He shifts from foot to foot, apparently ready to leave but too awkward to cut our conversation short. I get the hint."
        
        si happy "Haha, bye, Joel."
        
        jo surprised "Oh! Um, see you tomorrow, Simone."
        
        window hide
        
        jump next_event
        
    elif result == "coffee": #intellect
        
        call expression renpy.random.choice(EventLabels_LazinessEvening)

        jump next_event
            
label next_event:
    
    scene black with dissolve
    
    $ currentTimeOfDay = 3 # 0 = noon
    show screen screen_TOD()
    pause 3
    hide screen screen_TOD
    
    window show
    
    scene office cubicle with pixellate
    
    "Oh, it's look at that. It's the end of the longest day ever."
    
    "Finally."
    
    "As I pick up my purse from beneath my desk, Solomon calls out my name."
    
    so "Ms. West, may I see you briefly? It'll be just for a moment.\""
    
    "I feel myself straightening without knowing why. We've spoken so many times today, but I can't help it, somehow."
    
    si "\"Yes, Mr. Fox, I'll be right there.\""
    
    scene black with dissolve
    
    scene fox_office
    show solomon serious at cright
    with pixellate
    
    so "\"You're leaving now, yes?\""
    
    show simone surprised at cleft with dissolve
    
    si "\"Yes. Is there a problem, or--\""
    
    so surprised "\"Oh, no, not at all. I just wanted to apologize. I'm sorry that I didn't get to introduce you to the team like I intended to.\""
    
    so neutral "\"I'm glad to have you here, Ms. West. I'm sure you'll be a valued member of the Cufflinks team, and I look {i}very{/i} forward to working hard alongside you.\""
    
    "With a boss as fine as Solomon--and I mean that both phyically and mentally--I'd work hard alongside him if we were employed in a button factory."
    
    "I can't help but smile."
    show simone happy
    
    si "\"Thank you, Mr. Fox. I look forward to working with you, too.\""
    
    show solomon smile with dissolve
    
    "He smiles briefly before looking back on his computer."
    
    so neutral "\"Good night, Ms. West.\""
    
    "He glances up at me one last time."
    
    so "\"I'll be looking forward to seeing you tomorrow, bright and early.\""
    
    scene black with dissolve
    
    scene office
    show simone thinking cleft
    with pixellate
    
    si  "\"Hm...\""
    
    "Something about Solomon is... attractive, but not in a normal, 'what a handsome man' kind of way. In a strange, I want to work hard and impress him kind of way."
    
    "I would say he should go into politics, but he seems to actually like accomplishing things."
    
    "Putting my purse on my shoulder, I leave towards the elevator."
    
    scene black with dissolve
    
    jump mon1_home
    
label mon1_home:
    
    window hide
    
    stop music fadeout 1.0
    
    $ currentTimeOfDay = 4 # 0 = noon
    show screen screen_TOD()
    pause 3
    hide screen screen_TOD
    
    window show 
    
    scene west_home with pixellate
    
    play music "music/home.wav"
    
    show simone thinking with dissolve
    
    si  "\"Ah, I'm finally home.\""
    
    "Today went by much faster than I expected."
    
    "I collapse onto my couch tiredly."
    
    show simone worried with dissolve
    
    "Jeez, I barely feel like moving, but... life goes on."
    
    "Let's see."
    
    "I haven't had dinner or made lunch for tomorrow... I need to go to the kitchen for that."
    
    "I can stay right here in the living room and order out for dinner though. Oh, and I need to call Mom and see how she's doing."

    "Urgh... but... my bedroom's still a mess from when I was rushing this morning... My laptop's in there too, so I could also work from home, too."
    
    "What should I do?"
    
    #call screen house map, three locations
    
    menu:
        
        "Kitchen.":
            
            call expression renpy.random.choice(EventLabels_Kitchen)
            
            jump mon1_sleep
            
        "Bedroom.":
            
            call expression renpy.random.choice(EventLabels_Bedroom)
            
            jump mon1_sleep
            
        "Living room.":
            
            call expression renpy.random.choice(EventLabels_LivingRoom)
            
            jump mon1_sleep

label mon1_sleep:
    
    scene black with dissolve
    
    window show
    
    "Done with everything I needed to get done for the day, I climb under the covers."
    
    "As I lay in bed, I review today's events in my head."
    
    #dissolve in Solomon at center
    
    si "\"Hm...\""
    
    "Trina's words from her email echo in my head."
    
    "\"Something could happen in the next two weeks.\""
    
    "I snort."
    
    si "\"I {i}wish{/i} something would happen in the next two weeks.\""
    
    "I think of Milo."
    
    si "\"Except for with him. Definitely not with him.\""
    
    si "\"But... I mean, I could definitely do worse than Solomon.\""
    
    show solomon neutral with dissolve
    
    si "\"He's rich, he's smart, he's good-looking and a natural leader. {w}My kind of man.\""
    
    si "\"If {i}we{/i} went to the wedding...\""
    
    "Honestly, that'd be good and all, but real rap--if me and Solomon could {b}have{/b} a wedding, Nhung would have to forfeit."
    
    "She could bring a thousand dates and it wouldn't be enough. {w}Everyone knows that in the rock-paper-scissors of the romance world, husband {i}clearly{/i} trumps date."
    
    si "\"Right.\""
    
    "..."
    
    "But there's no way I can convince Solomon to marry me in the next two weeks. {w}And Trina would kill me."
    
    #dissolve in Joel at right
    
    "If anything, I could probably convince Joel to marry me."
    
    show joel neutral at right with dissolve
    
    "Or at least, bully--erm, convince... convince him to fake-marry me. Just for the wedding."
    
    si "\"Okay, maybe that's a little bit too wild.\""
    
    "But... people in movies got fake-married all the time. Nhung wouldn't have to know!"
    
    "But if I got Joel in on it, he might crack under pressure and accidentally admit that the whole thing is fake. I feel like that's definitely something he would do."
    
    "I mean, there's always..."
    
    show milo neutral at left with dissolve
    
    #dissolve in Milo
    
    "Okay, no. I'm definitely not that desperate--"
    
    "But... the truth is I only need a date so I can look... well, good when I stand on the stage to watch my best friend get married."
    
    si "\"Even if Milo does have a trash personality, he's still, unfortunately, handsome and fashionable--which means he'd make great eye candy and, more importantly, he'll will reflect well on me.\""
    
    si "\"Nhung would die if I came with him.\""
    
    "Hm... there's only two weeks left, though."
    
    si "\"Maybe I can just ask one of them to go with me, so if I explained about Nhung beforehand...?\""
    
    "No, because there's always a chance that one of them--or, I guess me--could blow it and ruin everything."
    
    si "\"If they actually {i}liked{/i} me, then I'd be golden.\""
    
    "Solomon would be the best because he's total package; charasmatic, handsome, tall, rich--but probably the hardest to convince."
    
    hide solomon with dissolve
    
    "Joel seems like he's easily influenced, but he's also the most likely to blow it. I could probably make him fall in love with me to take care of that , though."
    
    hide joel with dissolve
    
    "Milo is... {w}ugh. {w}Objectively, he's good looking-ish appearance-wise and since both he and Nhung are jerks, I'm pretty sure he's Nhung's type."
    
    hide milo with dissolve
    
    "...{w}What am I thinking?"
    
    "Am I seriously considering trying to make a co-worker fall in love with me just to show up Trina's sister?"
    
    "Even for me, that's kind of..."
    
    si "\"Simone, are you really debating the ethics of this?\""
    
    "I let out a sigh."
    
    "I should just go to sleep. I've got work tomorrow."
    
    window hide
    
    jump tues1_pre_morning