# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label tues1_pre_morning:
    
    $ dayofweek = 3
    $ dayofmonth = 22
    $ currentTimeOfDay = 0
    
    call calendar() from _call_calendar
    
    scene west_home
    show simone thinking at cleft
    with pixellate
    
    window show
    
    si "\"...\""
    
    "It's horning, but I'm still thinking about it."
    
    si sigh "\"It's no use thinking about it on my own.\""
    
    si "\"Let me get ready to go already.\""
    
    scene black with dissolve
    
    stop music fadeout 1.0
    
    scene trina_cafe with pixellate
    
    play music "music/casual.mp3"
    
    "As I do with all my crazy plans, I run them by the one, non-judgemental person I know."
    
    show trina surprised at cright with dissolve
    
    tr "\"You want to do {i}what{/i}?\""
    
    show simone thinking at cleft with dissolve
    
    si "\"Look, okay. I know it sounds crazy, but think of it this way; you were right!\""
    
    si happy "\"You said anything could happen in the next two weeks, and now look! {w}The universe is lining me up with eligible bachelors as far as the eye can see.\""
    
    tr smirk "\"Oh, no, you don't. You are not introducing your antics into my wedding.\""
    
    tr disappointed "\"When I said that, I was {i}joking{/i}! You can't seduce someone to be your wedding date-- especially not just to prove something to my sister!\""
    
    si incredulous "What if I {i}paid{/i}--\""
    
    tr "\"Still wrong! {w}You are not bringing a fake date to my wedding, and you are definitely not paying for someone to come! No one thinks like that, Simone.\""
    
    si "\"Pretty sure CregsList says otherwise.\""
    
    tr smirk "\"Wow, nice to see you've finally found it.\""
    
    si surprised "\"Found what?\""
    
    tr "A new low. {w}I mean your point of reference is seriously CregsList?\""
    
    "I roll my eyes."
    
    si bored "\"Fine, fine, Ms. Normal. What would {i}you{/i} do if you were in my place?\""
    
    tr neutral "\"I... wouldn't do anything you're thinking, that's for sure.\""
    
    "She shakes her head."
    
    tr disappointed "\"And I'm not answering that, by the way. I can't give you any ideas.\""
    
    si thinking "Hm... alright, fine. I've got to go soon anyway.\""
    
    si neutral "\"I'll talk to you later.\""
    
    tr neutral "\"Cool. Don't forget to meet me here after work; we're still supposed to hang out tonight!\""
    
    tr "\"My last trip to the movies before the wedding as a single woman...\""
    
    "I smile teasingly."
    
    si incredulous "\"Technically, you're not a single woman now, so your last trip to the movies was way before tonight.\""
    
    "She makes a face at me."
    
    tr happy "\"Yeah, yeah, but you knew what I meant!\""
    
    tr "\"You should get going before you end up late. {w}One more thing though--\""
    
    si surprised "Huh?"
    
    tr smirk "\"When you saw Solomon, you recognized him right away, didn't you?\""
    
    "I know if I answer, there's nothing but an \"I told you so\" waiting for me. I opt out of replying."
    
    si angry "\"...{w}Bye, Trina.\""
    
    "I hate when she wins."
    
    window hide
    
    scene black with dissolve
    
    jump tues1_boss
    
label tues1_boss:
    
    "{b}This is the end of the demo. Anything after this lacks anything outside of writing so I'll stop it here.{/b}"
    
    "{b}Hope you enjoyed it!{/b}"
    
    return

    scene office with pixellate

    so "\"Ah, Simone. I was waiting for you."
    
    "I blink at that. Waiting for me? Why?"
    
    si "\"Mr. Fox?"
    
    if home == "work":
        
        so "\"I wanted to thank you for the work you completed last night. It was extremely timely. {w}Without it, I doubt we would've made it to press on time."
        
        "Wait-- I can use this to my advantage! Maybe I don't {i}have{/i} to seduce anyone... if I just act myself and impress them with my natural skill, then maybe...?"
        
        si "\"Oh, Mr. Fox, it was nothing."
        
        "I smile."
        
        si "\"I'm sure anyone would've been able to do it."
        
        "Solomon looks surprised for a moment, then chuckles."
        
        so "\"You make it look so easy. If I could get a fraction of your work ethic, then this business would be solid for the next twenty years."
        
        "Is he... teasing? I take a leap and tease back."
        
        si "\"Only twenty, Mr. Fox?"
        
        so "\"Beautiful {i}and{/i} humble, I see."
        
        "He chuckles."
        
        so "\"You're going to be a pleasure to work with, aren't you? I can see it already, Ms. West."
        
        so "\"In ten minutes, did you hear about this morning?"
        
        si "\"Hm? What's supposed to be happening this morning?"
        
    else:
        
        so "\"Ah. I didn't get a chance to inform you yesterday, but we have a meeting in the conference room. If I can ask you to come to the meeting room in ten minutes."
        
        "That's... news to me."
        
        si "\"I didn't see it on the itinerary."
        
        so "\"That's because I didn't write it there."
        
        so "\"Now you know why I need an executive secretary."
        
        "He disappears into his office with a fleeting smile."
        
        jump tues1_morning
        
label tues1_morning:
    
    scene black with dissolve
    
    scene meeting_room with pixellate
    
    "The meeting room is full of buzzing employees who are all looking at the top board with something between anxiety and anticipation."
    
    "I see Solomon in the head of the room and am walking towards him when I hear my name called."
    
    z "Simone!"
    
    "I hadn't even seen him standing there. When I get closer to him, I greet him."
    
    si "\"Joel, good morning!"
    
    jo "\"Morning. This is your, uhm, first meeting, right?"
    
    si "\"Yeah. Honestly, I don't know what to expect."
    
    jo "\"Oh! I can help you... with that. At least a little bit."
    
    jo "\"I'm supposed to give the first presentation, so I have the notes on it."
    
    "He hands me a stapled print-out with slides on it."
    
    si "\"Thanks, Joel."
    
    jo "\"No problem."
    
    "It suddenly occurs to me-- why is Joel heading a major meeting when he's just an intern?"
    
    si "\"Wait a second. You're directing this meeting?"
    
    "Joel looks flustered."
    
    jo "\"N-no! Not at all, thank goodness. Solomon just wanted me to introduce. He feels it'll help me get better with public speaking."
    
    "Hm..."
    
    si "\"I see..."
    
    "So Solomon is... mentoring Joel?"
    
    "I inwardly lift my shoulders."
    
    "If there's anyone who could be mentored into shape, it's Joel, whose major flaw pretty much seemed to be a total lack of confidence."
    
    "He's a nice guy, though. I liked him almost instantly myself-- ah."
    
    "A likable editor... I could almost imagine it, even though I could just as easily imagine him stuttering through every meeting he had."
    
    "Before I know it, Solomon walks into the room."
    
    "Ah, the packet! {w}Even though Joel had gone through the trouble to get it to me, I still haven't looked through it."
    
    "{i}'Article Proposals for Q3.'{/i}"
    
    "Ah, so articles for the July through August editions of Cufflinks. Makes sense."
    
    so "\"Good morning, everyone."
    
    "He approaches me, then lightly places his hand on my shoulder."
    
    so "\"Before we begin, I'd like to introduce Simone West, my new executive assistant. She'll be my eyes and ears in the office, so try your best not to aggravate her-- and by extension, me."
    
    "A round of laughter flows through the room and practically drowning it out before a boisterous voice overpowers it."
    
    z "Is she your hands too?"
    
    "Abruptly, the room falls silent."
    
    z "I wonder where she's been touching to land a job in this department."
    
    "The comment is so shocking that for a long moment, I'm completely speechless."
    
    "My eyes automatically stray to see Solomon's reaction. {w}Reliably, he opens his mouth, but I think both of us are shocked when another strong, British accent cuts in aggressively."
    
    mi "\"Can it, Spade. Everyone knows that you're just bitter because you didn't get that promotion to senior-editor like you wanted to."
    
    mi "\"Writing the tripe that you do, the only promotion you deserve is 'King of the Garbage Heap' since that's where all your articles go, anyway."
    
    "Is that... Milo? Defending me?"
    
    mi "\"I've read her stuff-- let me tell you. West, over there isn't even an editor and she's still a better writer than you are."
    
    "I glance at Solomon, but he mostly looks like he's about to burst into laughter. {w}He quickly composes himself when he catches me looking, though."
    
    so "\"That's enough, Milo. And as for you, Mr. Spade..."
    
    "His face turns deadly serious."
    
    so "\"I personally requested Ms. West to work for me. The tongue is such a gift-- I'm disappointed that you've chosen to use yours with such repulsive speech. You disrespect Ms. West, myself and the Cufflinks brand."
    
    so "\"Please speak with me after the meeting. For now, you may leave."
    
    sp "..."
    
    so "\"That was not a request."
    
    "The disgruntled employee departs the room, slamming the door as he goes."
    
    "Solomon simply reshuffles the papers in front of him, then looks at Joel."
    
    so "\"Mr. Cabrera, you may proceed."
    
    jo "\"...Y-yes, sir."
    
    "He looks nervous, and for some reason his eyes flicker to mine for just a moment."
    
    "I offer an encouraging smile and he seems to straighten, clearing his throat before looking back at the waiting staff."
    
    jo "\"This meeting is to discuss the development of articles for the third quarter months."
    
    jo "\"That's, um, July, August and September."
    
    jo "\"We'll be dividing the office into three teams in order to execute three individual projects for these months."
    
    jo "\"Our editor-in-chief will be providing more information."
    
    "He looks at Solomon, who gives him an imperceptible nod of approval as Joel sits down."
    
    so "\"Thank you, Joel."
    
    "Solomon takes over, and for the rest of the meeting the atmosphere stays completely calm, coming to uneventful conclusion."
    
    scene black with dissolve
    
    scene office cubicle with pixellate
    
    si "\"Alright! That meeting seems like it went pretty well. {w}I'm ready to start the day!"
    
    si "\"I can't start on the project yet because I haven't gotten any files from Joel, but I still have my normal duties."
    
    si "\"Let me think..."
    
    "Hm... I didn't have time to get anything from Ginseng Swallows this morning, so I kind of want some coffee."
    
    "I could always make some."
    
    "There's plenty of emails to send... I'm sure I should do something like that, too."
    
    "If I want to work on Cufflinks itself, I could do some research for the magazine and see what's trendy in mens' fashion?"
    
    "I know we have a meeting about article proposals in a few days, so it'd be a good idea to brainstorm ideas for that."
    
    "And, of course, I've got to fill out these peer review sheets and talk about how I feel about my co-workers."
    
    "Or... {w}well, it's kind of early in the work day and everyone's busy. I could probably get away with doing some online shopping..."
    
    menu:
        
        "Send emails.": #dependability
            
            call expression renpy.random.choice(EventLabels_DependabilityMorning)
        
            jump tues1_lunch
            
        "Make some coffee.":
            call expression renpy.random.choice(EventLabels_KindnessMorning)
            
            jump tues1_lunch
            
        "Research the latest trends.":
            
            call expression renpy.random.choice(EventLabels_IntellectMorning)
            
            jump tues1_lunch
            
        "Do some online shopping.":
            
            call expression renpy.random.choice(EventLabels_LazinessMorning)
            
            jump tues1_lunch
            
        "Brainstorm for the meeting.":
            
            call expression renpy.random.choice(EventLabels_ImaginationMorning)
            
            jump tues1_lunch
            
        "Write peer reviews.":
            
            call expression renpy.random.choice(EventLabels_HonestyMorning)
            
            jump tues1_lunch
        
label tues1_lunch:
    
    "Whew, lunch time."
    
    if home == "lunch":
        
        si "\"Good thing I made my lunch last night."
        
        "I take my lunch out my bag and notice Joel hovering."
        
        "Hm..."
        
        si "\"Hey, Joel, what's going on?"
        
        jo "\"Oh, nothing. I'm about to take my lunchbreak, too."
        
        "Is... that why you're hovering then?"
        
        si "\"Did you want to eat lunch with me?"
        
        jo "\"Can I?"
        
        "He flushes."
        
        jo "\"Uhm, I just mean... It would be nice to not eat alone for once, you know? {w}Or to... actually have a lunch to eat."
        
        "I'm not sure what he means by that last statement but I shrug my shoulders and shift over so he can sit down."
        
        "He scoots his chair from his desk and sits beside me."
        
        "We eat silently for a few moments before I try to strike up a conversation."
        
        si "\"So, how long have you been working for Cufflinks?"
        
        jo "\"Oh, this is my seventh month. This is my first industry job."
        
        si "\"Oh, wow, you must've just graduated! How old are you?"
        
        jo "\"Twenty-three."
        
        "He answers quickly."
        
        jo "\"How about you?"
        
        si "\"Don't you know you should never ask a lady her age?"
        
        si "\"Nah, I'm kidding. I've always hated when women my age said things like that."
        
        si "\"I'm twenty-seven."
        
        jo "\"Oh! That's... a relief."
        
        "Relief?"
        
        "The confusion must show on my face, because Joel smiles timidly."
        
        jo "\"I thought you were my age, so I'm... kind of relieved that you're actually an experienced employee. {w}Otherwise, I'd feel even more inadequate than I already do."
        
        "He says it like he's joking, but the awkward chuckle that follows makes him sound like he vaguely believes it anyway."
        
        "With an employer like Solomon and a co-worker like Milo the Great, no wonder he has such a complex."
        
        "I place my hand on top of his."
        
        si "\"Joel, you shouldn't talk about yourself that way."
        
        jo "\"Solomon seems like a really good boss so I'm sure he has a lot of faith in you."
        
        "Joel's long eyelashes flutter uncertainly before he looks down at the table."
        
        "I pull my hand off of his to pick up my bottle of lemonade."
        
        si "\"But you know, any time you need to talk, you let me know, alright? I'm here for you, Joel."
        
        "Joel looks me in the eyes, then looks away, his voice soft."
        
        jo "\"Okay. And, uhm… thanks a lot."
        
        "He opens his mouth, then closes it, looking as though he wants to say something more. I’m thinking about asking him when he smiles softly."
        
        jo "\"The same to you, Simone. I mean... if you have things you need to talk about, you can let me know, too."
        
        ## Joel email
        
        scene black with dissolve
        
        jump lunch_milo
        
    else:
        
        jump lunch_milo
        
label lunch_milo:

    scene office cubicle with pixellate
    
    "Today is surprisingly peaceful. I'm glad."
    
    mi "\"Hey, West!"
    
    "Spoke too soon."
    
    si "\"What is it, Matthews? I'm on my lunch break which is ample time for you to {i}not{/i} bother me."
    
    mi "\"Ha. Strong words from someone who was trying to shirk her work. I heard you're trying to get off already."
    
    mi "\"I wouldn't have pegged you for a slacker, but even I can be wrong sometimes."
    
    "My voice is dry."
    
    si "\"Oh, I'm not a slacker, am I? {w}I'm glad to see that you have standards that even {i}I{/i} can surpass. {w}Congratulations to me."
    
    if battle_one == "fail":
        
        si "\"It doesn't matter, anyway. I couldn't get it anyway, so..."
        
        mi "\"Hm..."
        
        "I sigh aloud."
        
        si "\"What, are you gearing youself up to gloat about it more?"
        
        mi "\"What did you need off for anyway? To spend time with your {i}boyfriend{/i}?"
        
        "I shoot him a nasty look."
        
        si "\"I don't {i}have{/i} a boyfriend, first of all--"
        
        "He opens his mouth, but I can already predict the words."
        
        si "\"Don't try me, Matthews."
        
        si "\"And anyway, I was trying to get off because my best friend's wedding is in two weeks and the last fitting is this upcoming Thursday evening."
        
        mi "\"I see... and you couldn't get it?"
        
        si "\"No. I did a pretty bad job of convincing him, so... no."
        
        "He shrugs."
        
        mi "\"Well, you are pretty tactless. I can't say I'm surprised."
        
        si "\"Oh, because I forgot that you're s sparkling example of sensitivity."
        
        "He nods along with me, ignoring my blatant sarcasm."
        
        mi "\"Well, I am the best journalist here."
        
        mi "\"Anyway... I'll cover for you."
        
        "...What?"
        
        si "\"...What?"
        
        mi "\"Don't act like you didn't hear me, and don't make me say it again."
        
        mi "\"I owe you one."
        
        mi "\"Because of what happened with... you know. Yesterday's mix-up."
        
        mi "\"Thursday evening, I'll cover you as long as you never mention this. {w}Ever."
        
        si "\"Done."
        
        mi "\"Good."
        
        si "\"And uh... thanks, Milo. That was surprisingly nice of you."
        
        "Milo smirks at me."
        
        mi "\"Well, honestly, I can't imagine who'd want you in their wedding party, so it must be a big deal for you."
        
        mi "\"Don't think too deeply into it, West."
        
        "I can’t help muttering my thoughts under my breath as he goes."
        
        si "\"You really don't know how to be nice, do you."
        
        jump trina_dinner
        
    else:
        
        mi "\"Well, the fact that you got off is a pretty big deal."
        
        mi "\"You must be more charasmatic than I thought."
        
        "I lift an eyebrow."
        
        si "\"You think I'm charasmatic?"
        
        mi "\"Don't misinterpret me on purpose, West."
        
        si "\"Don't you have a job to pretend to be doing?"
        
        "Milo waves his hand dismissively."
        
        mi "\"Yeah, yeah, keep talking. I'll finish my work faster than you could ever dream to."
        
        si "\"I didn't realize we were in a competition."
        
        mi "\"I--"
        
        "He sucks his teeth and stalks off somewhere, looking moody."
        
        si "\"...Speaking of people who need to seriously chill out."
        
        "I let out a sigh."
        
        si "\"I can't wait until tonight."
        
        jump trina_dinner

label trina_dinner:
    
    "I check my watch. Only a few more hours until Trina and I can go to the movies!"
    
    si "\"We haven't had a Girls' Night Out in ages..."
    
    "..."
    
    "A strang pang of loneliness strikes me."
    
    si "\"Trina... I can't believe you're really getting married."
    
    "It's not like she's dying or anything but..."
    
    "Marriage is so... {w}serious. {w}And time-consuming."
    
    "Of course, they'll want to spend a lot of time together, and even I understand how busy she's going to be after the wedding."
    
    "I tap a pen against my lips."
    
    "It's not that I'm against Trina getting married-- if anyone deserves to be get a happily ever after, it's definitely Trina. {w}Her fiancé is a really nice guy so I know he'll treat her well."
    
    "Really, I'm happy for her, too, but..."
    
    "I've definitely got to make more single friends. {w}I don't want to depend on Trina for every little thing or to monopolize her time."
    
    si "\"..."
    
    "Well, no point in thinking about it now."
    
    si "\"Tonight's going to be the best Girls' Night we've ever had."
    
    scene black dissolve
    
    jump tues1_afternoon
    
label tues1_afternoon:
    
    scene office cubicle with pixellate
    
    "It's the afternoon."
    
    "Time to get some work done!"
    
    #call email desktop
    
    si "\"There's a lot of emails in here."
    
    si "\"I probably only have time to take care of two of them..."
    
    #KINDNESS/HONESTY EMAIL
    
        ##From: jhiga@fspub.com
        ##Subject: Favor
        
        ##EMAIL CONTENT
        ##Simone, right? Welcome to the office!
        ##Listen, I need your help. Can you send me Milo's office number?
        ##I need to speak with him, but I left my work phone in my desk before I left for this interview.
        ##Sorry for the inconvenience!
        ##J. Higa
        
            ##"I'll get it for you." //+Kindness
                    
                    ##Thanks for the welcome.
                    ##Actually, though, I'm don't have Milo's number (or his email, yet.)
                    ##Here's Joel's email, though! 
                    ##He'll definitely know how to contact Milo.
                    
                        ##jcabrera@fspub.com
                        
                    ##Hope your interview goes well.
                    ##Simone West
                    
            ##"I don't have it." //+Honesty
            
                    ##Oh, thanks for the welcome email.
                    ##Unfortunately, I don't have Milo's number and he's out of the office at the moment.
                    ##I don't have his email either... I could guess, but if it's sensitive information you're after, I don't want to accidentally mail the wrong person.
                    ##Sorry about all this!
                    ##Simone West
                
            ##The subject should automatically be filled in asi "\"RE:______", so in this case, "RE:Favor"
                
    ##INTELLECT/DEPENDABILITY EMAIL
    
        ##From: sfox@fspub.com
        ##Subject: Meeting
        
        ##EMAIL CONTENT
        ##Simone, when you have a free moment, could I ask you to forward me the information from this morning's meeting?
        
        ##Also, I'm sorry about that outburst from Spade. He's not a bad journalist, but his remarks this morning were reprehensible. I just want to let you know that I've reported him to HR. Hopefully that'll be a lesson.
        
        ##In any case, if you have any problems with anyone else, speak with me immediately and I will provide assistance.
        
        ##S. Fox
        
            ##"Mail him the notes from the meeting.": //+Dependability
            
                ##Solomon, I'm not sure if the minutes I took from the meeting are satisfactory as far as 'information from the meeting', but I'll include them. They're detailed, so I think they'll be helpful for whatever you need them for!
                
                ##Also... thank you. I appreciated the way you and Milo handled it. It was surprising to hear Milo talk like that, though. Kind of unexpected. Thanks for the heads up, I'll let you know.
                
                ##Simone West
            
            ##"Mail him the slides from the meeting.": //+Intellect
            
                ##Joel gave me a copy of these slides
    
    ##LAZINESS/IMAGINATION EMAIL
        
    
    scene black with dissolve
    
    jump tues1_evening
    
label tues1_evening:
    
    scene office cubicle with pixellate
    
    si "\"It's evening already?"
    
    si "\"..."
    
    "I check my itinerary."
    
    si "\"Most of my work is done for the day! Great!"
    
    z "...is impossible."
    
    si "\"Hm? {w}Who's that?"
    
    scene black with dissolve
    
    scene office with pixellate
    
    "Oh, it's one of my co-workers. Hm... I don't think I know their name."
    
    si "\"Uhm, excuse me-- is everything okay?"
    
    "The staff member looks up at me with reddened eyes."
    
    z "Oh... you're the new executive assistant."
    
    si "\"Right. Simone West."
    
    z "I'm Nick. Please, Simone, you've got to help me."
    
    si "\"What's wrong?"
    
    n "I accidentally emailed this client telling them that this information packet would be completed by tomorrow afternoon instead of next week, and now they're threatening to completely void the contract with us if I don't get it to them."
    
    "Yikes."
    
    si "\"Uhm, did you... tell Solomon?"
    
    "Nick turns his fearful eyes on me."
    
    n "I can't tell him. I know Fox is usually a nice guy, but even he would be angry if he finds out I lost the Autumn client based off of a time mistake."
    
    si "\"Oh, geez."
    
    "I would help, but... Trina... our movie night..."
    
    jump third_choice

label third_choice:
    
    "I don't know what I should do."
    
    "Let me think..."
    
    menu:
        
        "I should..."
        
        "Help him.":
            $ help = "total"
            
            "...If I leave him like this, there's no way he's going to finish on time."
            
            "I could always help him a little and then go meet with Trina, but he might not finish on time, even so."
            
            "I could also... cancel my plans with Trina and help him out..."
            
            jump choice_1
            
        "Get him help.":
            
            $ help = "half"
            
            "I guess I have no choice. I'll just have to help him out somehow."
            
            si "\"Let me think..."
            
            "I can ask other staff for help, or I could probably recommend some resources that'd help him finish on time, at least..."
            
            jump choice_2
            
        "Don't help him.":
            
            $ help = "none"
            
            "I don't have time to help him since I'm meeting up with Trina but..."
            
            jump choice_3
            
label choice_1:
    
    menu:
        
        "Revise what he has.": #honesty
            
            $ tues1_home = "go"
            
            "I pull up a chair."
            
            si "\"Have you proofread any of this?"
            
            "Nick lets out a strangled laugh."
            
            si "\"Okay. Right."
            
            si "\"Give me everything you've completed so far. How much of this is done?"
            
            n "Maybe... a fourth of it? I haven't made any of the graphics we'll need, so there {i}is{/i} that, but as far as what I've typed..."
            
            "I nod briskly."
            
            si "\"Don't worry about it."
            
            si "\"I revise pretty quickly, so this'll be finished in no time, I promise."
            
            si "\"I still have to go, but..."
            
            si "\"You might be able to finish if you can just move forward and don't have to come it again for revisions."
            
            "Nick nods in agreement."
            
            n "Sounds good. Let's get to work!"
            
            jump tues1_home
            
        "Stay and help him finish.": #kindness
            
            $ tues1_home = "home"
            
            "I sigh, resigned."
            
            "Our last Girls' Night before the wedding and I'm..."
            
            n "Alright, Nick. I'll help you."
            
            "Nick's reddened eyes turned to me slowly, as if he can hardly believe his ears."
            
            n "You'll... what?"
            
            si "\"Don't make me say it again, because I might just change my mind."
            
            "Nick grabs my hands."
            
            n "Simone... you saved me."
            
            si "\"Not yet I haven't."
            
            si "\"Look, I'm not familiar with the data so you'll have to instruct me on what to do-- I'm an executive {i}assistant{/i} which means I'll help you in anyway I can, but I'm not writing anything."
            n "No, no, of course! I understand completely!"
            
            "He pauses."
            
            n "You're... you're really going to--"
            
            si "\"Nick! Focus, please!"
            
            n "R-right!"
            
            n "Alright, here's what I need you to do."
            
            scene black with dissolve
            
            jump tues1_home
            
        "Change your mind.":
            
            "On second thought..."
            
            "I can't do this."
            
            jump third_choice
            
label choice_2:
    
    menu:
        
        "Ask other staff for help.": #dependability
            
            $ tues1_home = "go"
            
            si "\"Sorry, Nick-- I can't stay, but I'll send out a mass email, alright?"
            
            n "Even that's fine! This is impossible to complete alone, but if I can get someone to help me then that'd be great."
            
            "He looks at me gratefully."
            
            n "Simone, you're a life-saver, you know that?"
            
            "I let out a chuckle."
            
            si "\"That's what they tell me."
            
            scene black with dissolve
            
            scene office cubicle with pixellate
            
            "I return to my desk, and get to work on a mass email to send out department-wide."
            
            "It takes a little bit of effort, especially when I have to scroll through the selected names to deselect Solomon."
            
            si "\"He probably... wouldn't want him to know anout this whole ordeal."
            
            "Satisfied, I return to Nick."
            
            scene black with dissolve
            
            scene office with pixellate
            
            si "\"All done, Nick. It's almost time for me to go, but... I wish you well on your project, alright?"
            
            "He smiles, looking vaguely less anxious."
            
            n "Thanks, Simone. Have a nice night!"
            
            scene black with dissolve
            
            jump tues1_home

        "Recommend resources for the packet.": #Intellect
            
            $ tues1_home = "go"
            
            si "\"Let me see that."
            
            "Nick hands me the incomplete packet. It's thick-- thirty pages at least."
            
            "Glancing over it, I pause, an idea forming in my mind."
            
            si "\"Do you have enough resources for this?"
            
            n "What do you mean?"
            
            si "\"On pages five and seven, you reference previous Jarc Makobs collections, but I don't see any other information about them-- not pictures, not specific piece reference names."
            
            n "Oh... that... y-yeah, I'll just look it up later if I have time."
            
            si "\"Hm... I can help you with this. That should at least cut down on time, right?"
            
            jump tues1_home
            
        "Change your mind.":
            
            "On second thought..."
            
            "I can't do this."
            
            jump third_choice
            
label choice_3:
        
    menu:

        "Do something for him.": #Imagination
            
            $ tues1_home = "go"
            
            "Hmm... I can at least be supportive."
            
            si "\"Nick, why don't you... relax for a moment?"
            
            si "\"Staring at the same information can be kind of overwhelming..."
            
            "I glance at the kitchen."
            
            "I said I wasn't going to do this but..."
            
            si "\"I'll be right back."
            
            show black with dissolve
            
            hide black with dissolve
            
            si "\"Alright, here."
            
            n "Huh, what is it?"
            
            si "\"It's a pot of coffee. There's another one in the coffeemaker, too."
            
            "He looks at the coffee pot I've set down on the table then at me."
            
            n "You made this for me?"
            
            n "I... I don't know what to say."
            
            si "\"Just a thanks will suffice."
            
            si "\"Sorry that I can't do more."
            
            n "No, this is... really helpful, actually. I kind of needed some moral support."
            
            n "Thanks, Simone."
            
            jump tues1_home
            
        "Ignore him.": #Laziness
            
            $ tues1_home = "go"
            
            si "\"Well, no 'but's."
            
            si "\"Sorry that I can't help you, Nick. I'm meeting up with someone after work, so..."
            
            "Nick raises his hands."
            
            n "No, no! Sorry, I didn't actually know you were here anyway, so I wasn't trying to influence you to help me or anything."
            
            n "Have fun tonight!"
            
            n "While... I... suffer."
            
            "I shoot him a sympathetic look as I pack up my purse."
            
            "Sorry, guy."
            
            scene black with dissolve
            
            jump tues1_home
        
        "Change your mind.":
                
            "On second thought..."
            
            "I can't do just leave him like this."
            
            jump third_choice
    
    jump tues1_home

label tues1_home:
    
    if tues1_home == "home":
        
        scene west_home with pixellate
        
        si "\"I am... absolutely beat."
        
        "And I am. I couldn't drag myself to the movies if I wanted to."
        
        "Not that it mattered-- it'd ended four or five hours ago..."
        
        "I send Trina a quick email, then collapse into dreamland."
        
        ##This email should go to the inbox (to be received the following morning)
        
        ##From: t@pmail.com
        ##Subject: RE:Sorry, Trina
        
        ##EMAIL CONTENT
        ##It's okay, Simone!
        
        ##Sometimes things happen, you know? I mean... it's really sad that we didn't get to hang out but... thanks for letting me know. I called Scott and we went to the dinner instead.
        ##I know how much you wanted to see it so let's try to do it another time! Maybe I can rent the movie when it comes out in a few months?
        ##-- T
        
        ##P.S. This is kind of weird but... when I was closing up the shop, guess who I saw? Your co-worker, Miles. Or Milo? (I think it's Milo. I could look back in an older email but I'm too lazy tbh.) We chatted for a bit! He's not bad. Is he rich? He seems rich. You should bring him to Ginseng sometime.
        
        jump wed1_morning
        
    else:
        
        scene office cubicle with pixellate
        
        si "\"I've got to go meet Trina."
        
        si "\"I don't hurry, I won't make it."
        
        mi "\"West?"
        
        "I try my best not to make a face."
        
        "{i}Why do you pick the worst times to bother me, Milo?{/i}"
        
        si "\"I'm sorry, Matthews-- whatever it is can wait tomorrow."
        
        mi "\"...It's not that important, honestly. I'll speak with you about it tomorrow. {w}Actually I'm heading out, too."
        
        "Oh... great... Milo in the morning... Glad I have something to look forward to in the morning."
        
        "I plaster on a smile."
        
        si "\"Great! See you tomorrow!"
        
        "We step aboard the elevator together and ride it silently the whole way down."
        
        scene black with dissolve
        
        scene trina_cafe with pixellate
        
        si "\"..."
        
        mi "\"...{w}..."
        
        si "\"Seriously, Matthews?"
        
        si "\"Don't even start, West. {i}You're{/i} the one who's following me, clearly."
        
        mi "\"Just because we're walking in the same direction doesn't mean I'm following you."
        
        "I shoot him an exasperated look."
        
        si "\"You say that, but I know your kind, Milo Matthews. {w}You don't think it seems suspicious that you tell me you need to speak with me and then {i}happen{/i} to be walking in the same direction as me."
        
        mi "\"It's not because I'm not some kind of workaholic. I told you it could wait until tomorrow, didn't I?"
        
        mi "\"And-- wait a second."
        
        si "\"What?"
        
        mi "\"You..."
        
        mi "\"You're talking differently. I knew it!"
        
        si "\"Matthews, what are you {i}talking{/i} about?"
        
        "He mimics me."
        
        mi "\"{i}Yes, Mr. Fox. No, Mr. Fox. I see, Mr. Fox. Whatever you need, Mr. Fox.{/i}"
        
        mi "\"You faker!"
        
        si "\"It's not being 'fake', it's being 'professional'! I'd explain the difference but I somehow have a feeling you couldn't grasp it anyway."
        
        mi "\"..."
        
        si "\"..."
        
        si "\"Anyway, why are you still here?"
        
        mi "\"This is where you were going? You realize it's closed, right?"
        
        si "\"I'm waiting for my friend. We're supposed to meet here. If you're not intent on bothering me, then you could go."
        
        "Milo stares at me, then pulls out one of the cafe benches."
        
        si "\"..."
        
        "Great."
        
        mi "\"...Still mad about yesterday?"
        
        si "\"I'm not."
        
        jump milo_q
        
label milo_q:
    
    if battle_one == "no":
        
        mi "\"Didn't I say I would cover for you?"
        
        si "\"That and this are separate issues."
        
        "He scoffs."
        
        mi "\"Fine, then. What do I have to do for you to... to stop blowing it all out of proportion?"
        
        si "\"Hm... you could start with leaving. Like, now."
        
        mi "\"...Simone."
        
        mi "\"Why are you so mad at me?"
        
        si "\"I already said that I'm not mad."
        
        jump milo_argue
        
    else:
        
        jump milo_argue
            
label milo_argue:
    
    mi "\"Oh, how convincing."
    
    "Milo sighs in annoyance."
    
    mi "\"Look, Simone."
    
    "Milo won't look me in the eye."
    
    mi "\"Your proposal was... really good. The one you edited for Joel. Even if you're not an editor, you probably could be one."
    
    mi "\"So I'm sorry."
    
    si "\"..."
    
    "I blink at him in surprise. Then smirks."
    
    si "\"You're... what?"
    
    mi "\"I said I think you need your ears checked."
    
    "The sulky comment pushes unwanted laughter from my chest."
    
    si "\"You are so stubborn! But I guess... you're not too bad either."
    
    "Milo looks at me in utter shock."
    
    si "\"I mean, you're terrible. But your work... it's not bad."
    
    "I let out a sigh."
    
    si "\"And... I appreciate what you said during the meeting. It was surprisingly nice of you."
    
    mi "\"Yeah, well... it was true."
    
    si "\"Huh?"
    
    mi "\"Nothing. Is that's your friend?"
    
    "I see a familiar car pull up beside us."
    
    "Trina steps out, then rushes over to us."
    
    tr "\"Simone, I'm so sorry I'm late! Did you wait lo-- oh. "
    
    "She reaches up her hand to push stray hairs behind her ears, evidently forgetting it's in a ponytail."
    
    "Smooth, Trina."
    
    tr "\"Sorry, you must be one of Simone's co-workers. I should probably introduce myself before--"
    
    tr "\"Wait a second."
    
    tr "\"I know you!"
    
    "Getting the dangerous sense that she's about to say more than she should, I tug her aside."
    
    si "\"Of course you know him! {w}Trina, I told you about him in our emails, which you should definitely not mention aloud right now? This is Matthews!"
    
    tr "\"Matthews?"
    
    "A lightbulb goes off as her eyes light up in recognition."
    
    tr "\"Milton?"
    
    "I let out a laugh."
    
    si "\"No, Trina. I think you've got him confused with someone else."
    
    "I smack Milo lightly on the chest but he seems completely frozen."
    
    "No... no way. It can't be true, can it?"
    
    si "\"Am I missing something?"
    
    tr "\"Oh! Sorry, actually I was going to tell you tonight but now's fine too, I guess. So! Turns out Scott's best man came down with a bad case of the flu and he won't be able to make it to the wedding next week."
    
    tr "\"We were worried about him not having a best man, but then Scott was like, ''Hey, Ti, I know this guy I grew up with and he's already invited to the wedding, so why don't we ask him?'' And he said yes!"
    
    "This time, Trina addresses Milo... Milton... Milo directly."
    
    tr "\"Scott showed me a picture of you! I'm sorry I didn't recognize you sooner."
    
    mi "\"..."
    
    si "\"So--"
    
    mi "\"I should go. I'm sorry, it was nice to finally meet you, but I'll..."
    
    mi "\"Goodnight, Trina. West."
    
    "Milo suddenly marches in the other direction with determination."
    
    "I shout after him."
    
    si "\"Hey, Matthews! We came from that direction!"
    
    "He glances over his shoulder."
    
    mi "\"My car is in the lot."
    
    "Car?"
    
    "So why did he walk with me... hm. Milo's so strange."
    
    tr "\"...So?"
    
    tr "\"He's one of the guys, right? One of your wedding date candidates?"
    
    si "\"Wrong. That guy is definitely not coming with me to the wedding."
    
    "Trina looks at me deviously."
    
    tr "\"Apparently, it turns out he doesn't have to. {w}Since he'll already be there, I mean."
    
    "I let out a sigh, feeling too tired to make a rebuttal."
    
    si "\"Come on, let's get out of here."
    
    tr "\"The movie doesn't start until 8, so there's no fire! We can take our time."
    
    si "\"You're right."
    
    tr "\"You know... you're still dressed for work. Did you want to stop by your place so you can change or anything?"
    
    "I shrug noncommitally."
    
    si "\"May as well."
    
    tr "\"Alright, then! Let's go!"
    
    scene black with dissolve
    
    si "\"...Pfft."
    
    tr "\"What is it?"
    
    si "\"Nothing! Nothing. Just... Milton."
    
    tr "\"..."
    
    tr "\"You're terrible, you know that?"
    
    jump wed1_morning