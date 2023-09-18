# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

# The game starts here.

label start:

##MORNING EVENT LABELS
    $ EventLabels_HonestyMorning = ["mh1", "mh2", "mh3"]
    $ EventLabels_ImaginationMorning = ["mim1", "mim2", "mim3"]
    $ EventLabels_IntellectMorning = ["min1", "min2", "min3"]
    $ EventLabels_LazinessMorning = ["ml1", "ml2", "ml3"]
    $ EventLabels_KindnessMorning = ["mk1", "mk2", "mk3"]
    $ EventLabels_DependabilityMorning = ["md1", "md2", "md3"]
    
##EVENING EVENT LABELS
    $ EventLabels_HonestyEvening = ["eh1", "eh2", "eh3"]
    $ EventLabels_ImaginationEvening = ["eim1", "eim2", "eim3"]
    $ EventLabels_IntellectEvening = ["ein1", "ein2", "ein3"]
    $ EventLabels_LazinessEvening = ["el1", "el2", "el3"]
    $ EventLabels_KindnessEvening = ["ek1", "ek2", "ek3"]
    $ EventLabels_DependabilityEvening = ["ed1", "ed2", "ed3"]

##NIGHT EVENT LABELS
    $ EventLabels_Kitchen = ["kk1", "kk2", "ki1", "ki2"]
    $ EventLabels_LivingRoom = ["lrl1", "lrl2", "lrh1", "lrh2"]
    $ EventLabels_Bedroom = ["bi1", "bi2", "bd1", "bd2"]
    
    
    ##################### TESTING
    jump mon1_morning
    #####################

    play music "music/casual.mp3"

    scene old_cafe
    show simone worried at cleft
    with dissolve
    
    window show
    
    "{i}Hm, I wonder if I have time?{/i}"
    
    si "I don't want to be late, but since today is the most important day of my life, I need all the good vibes I can get."
    
    "Skipping out on the chance to see my best friend while on the way to my interview seems like just asking the universe for trouble-- and if there's one person in the universe who gives off enough good vibes to stave off trouble for {i}centuries{/i}, it's Trina Luong."
    
    "As the café where Trina works comes up on my right, the front door bursts open before I get a chance to make a concrete decision."
    
    #happy
    
    show trina happy at cright
    with dissolve
    
    tr "Simone! Wow!"
    
    hide trina
    
    show trina happy at cright
    show simone smile at cleft
    with dissolve
    
    si "Hey, cutie."
    
    "She gives me a once-over, then flashes me a mischevious smile."
    
    show trina smirk
    tr "You're really trying to knock 'em dead today, huh?"
    
    show trina happy
    tr "I knew I was right when I told you to buy that sheer lipgloss."
    
    "Per usual, her excitement doesn't allow me to get a word in edgewise--but also per usual, her words send a flicker of pride through me. As modesty dictates, I wave off her compliments."
    
    show simone happy
    si "Oh, you're just saying that."
    
    show simone neutral
    si "Doesn't mean you have to stop though. Let this moment serve as precedent that you need never cease when it comes to telling me how great I look."
    
    show trina smirk
    tr "You know, I was going to ask if you were nervous, but... clearly all is well if you can deliver a line like that with a straight face."
    
    show simone happy
    si "Vanities aside, just get a good look at the brand new face of 5/7 Publishing."
    
    "Trina looks at me in utter surprise."
    
    show trina surprised
    tr "You got the job and didn't tell me? When?"
    
    "I wave my hand dismissively."
    
    show simone sigh
    si "Okay, fine."
    
    show simone happy
    si "You are looking at the {i}soon-to-be{/i} brand new face of 5/7 Publishing. You and I {i}both{/i} know that this interview is practically in the bag."
    
    show trina neutral
    tr "Fair enough. Your interview is still at 7:30, right?"
    
    show simone smile
    si "You got it, babe."
    
    si "I'm on my way now. Do I look professional? Trustworthy?"
    
    show trina happy
    tr "Yes to both. {w}I mean, I barely recognized you! Once you step off that elevator, those stuffy guys at the publishing company won't know what hit them."
    
    show simone incredulous
    si "I'll just forgive you for the fact that you just associated me looking professional and trustworthy to me being unrecognizable."
    
    show trina smirk at cright
    
    "Trina flashes me a wicked grin, then reaches into her apron to rummage for her order notepad."
    
    show trina surprised
    tr "Can I get you a tea or coffee or something before you go?"
    
    "I check my watch again."
    
    show simone depressed
    si "Hm..."
    
    show simone sigh
    si "I'd love one, but... there's not enough time."
    
    show simone smile
    si "Don't worry though-- I'll be back after my interview and I'll definitely be sure to grab something when I do. May as well take advantage of the fact that this place is so close to the office."
    
    show trina neutral
    tr "Mhm, I know that's right-- if I'm here, then clearly you and this job were meant to be."
    
    show trina happy
    tr "Just step into the future with me, Simone-- {w}you're in your cubicle, writing yet another article for Sweet Teen Magazine, slaving away for The Man late into the night. What do you do?"
    
    si bored "A victory dance in my cubicle because of all that overtime pay I'll be eventually drowning in?"
    
    "Trina ignores me."
    
    show trina disappointed
    tr "...Anyway."
    
    show trina happy
    tr "Exhausted and in desperate need of a pick-me-up, you pick up the phone and dial the number for Impresso Espresso's Coffee & Catering."
    
    si uncomf "Is that this week's name of your hypothetical café? {w}Impresso Espresso?"
    
    show simone sigh
    si "I was kind of a fan of the other one from last week. Captain... something."
    
    show trina surprised
    tr "Captain Cappuccino?"
    
    show simone happy
    si "That's the one!"
    
    #mischievous
    
    show trina smirk
    tr "Well, whatever I name it, the café isn't as hypothetical as you think! {w}At least, not anymore."
    
    show trina happy
    tr "Guess who said they're ready to sell?"
    
    show simone surprised
    si "You're lying!"
 
    "Trina just keeps grinning, elated."
    
    show simone happy
    si "Congrats! You have a purchase date?"
    
    show trina neutral
    tr "I do! We're supposed to start the transition period in about three weeks."
    
    show trina disappointed
    tr "...Which means I really need to think of a good name."
    
    show simone smile
    si "Well, let's have a victory party after you own this place and I get hired at 5/7."
    
    show trina neutral
    tr "You know, if we keep talking like this, you're going to be late. You should go."
    
    si "Right!"
    
    tr "Break a leg and all that good stuff."
    
    show simone happy
    si "Thanks."
    
    show trina happy at cright
    
    "She flashes me a bright smile as I set off towards the publishing house."
    
    scene black with dissolve
    
    scene meeting_room with dissolve
    
    stop music fadeout 1.0
    
    play music "music/work.mp3"
    
    "After a brief wait, I'm escorted to the conference room where I'm supposed to be interviewed."
    
    "I'm... I'm not nervous, but for some reason it takes me a moment to step inside. On the other side of this door is my future."
    
    "There is definitely no room for failure."
    
    "Touching the doorknob lightly, I give myself a last minute pep talk."
    
    show simone thinking with dissolve
    
    si "This is your battlefield, Simone. They liked your cover letter, they loved your resumé and you've already done the phone and video interviews."
    
    si "All you've got to do is prove that you're an essential part of 5/7 Publishing, a journalist of the century in the making. {w}Prove to them how much they need you!"
    
    "Taking a deep breath, I boost my nerves and sit up straighter, waiting for my interviewer to come in."
    
    show simone smile at cleft
    show debra_silhoutte at cright
    with dissolve
    
    "A few minutes pass, and eventually, an older woman enter the room, her eyes sharp and alert despite the wrinkles that cushion them."
    
    "I stand at the sight of her. Frankly speaking, she looks like she eats interns for {i}hors d'oeuvres{/i}."
    
    "I'm not exactly one who flinches away from authority but the fact that there's a strong chance that {i}I{/i} will become one of the aforementioned appetizers makes the thought less amusing than I'd like."
    
    "She shuffles some papers, holding off on greeting me as she organizes herself, then looks up."
    
    "I try not to stare but... something about her features strikes me as... odd. {w}Just slightly."
    
    "Her tone is brisk, snapping me out of my thoughts."
    
    z "You're the seven-thirty appointment?"
    
    show simone surprised
    si "I-- yeah. {w}I mean, yes."
    
    z "Excellent. I'm Debra Priestley from the Human Resources department. I'll be conducting your interview today."
    
    d "Please. Take a seat."
    
    "I sit across from her as instructed while she shuffles through a file folder-- and now that I get a good look at her face, all at once, I realize what about her seems off."
    
    "Her eyebrows have been shaved off and redrawn on and, while the shape is perfect, by some mistake one of them is slightly higher than the other, giving her a look of perpetual incredulity."
    
    "{i}Amazing.{/i}"
    
    d "Name?"
    
    "I try not to stare, blinking rapidly as I focus on her eyes."

    show simone neutral
    si "Simone West, ma’am."
    
    "I hand her a copy of my resumè."
    
    d "Right, Ms. West. First, I'd like to congratulate you for making it this far into the interview process. We had many excellent candidates on paper but the results of your phone interview blew us out of the water."
    
    "She skims the file then looks at me unsmilingly."
    
    "I guess I wouldn't be smiling either if I'd accidentally drawn my eyebrow too high and didn't have time to re-do it because I had to interview someone at seven-thirty in the morning."
    
    d "Let's begin."
    
    #Battle Tutorial
    call lbl_Battle_Tutorial_Start
    
    window hide
    
    #MONDAY, Week One
    #BATTLE: Simone West, executive assistant vs. Debra Garcia, senior editor
    
    $stat_kindness = 0
    $stat_honesty = 0
    $stat_intellect = 0
    $stat_dependability = 0
    $stat_imagination = 0
    $stat_laziness = 0
    
    stop music fadeout 1.0
    play music "music/battle.wav"
    
    call screen preBattle_screen('debra', "Get the Job!", "Be Yourself!")
    $WriteToFile("Starting Battle intro")    
    $Battle_FailureLabel = "lbl_battle_intro_Failure"
    $Battle_TimeoutLabel = "lbl_battle_intro_Timeout"
    
    $ResetBattleStatus()
    $Battle_Question_Current = 0
    $SetResult(Battle_Question_Current, 'progress')
    #$ResetBattleTimer()
    $StopBattleTimer()
    #show screen Battle_screen_background
    call screen Battle_screen('debra', Battle_intro_QuestionList, Battle_intro_AnswersList, Battle_intro_AnswersLabels,  8, 5)
    
    jump expression _return
    
    return
    
label Tut_battle_fin:
    
    stop music fadeout 1.0
    
    play music "music/casual.mp3"
    
    scene black with dissolve
    
    scene old_cafe with dissolve
    
    window show
    
    show simone sad at cleft
    show trina disappointed at cright
    
    tr "\"So... how'd it go?\""
    
    show simone happy
    si "\"It... it went!\""
    
    "Except for the part where I almost blew the entire interview over an eyebrow."
    
    "But Trina doesn't need to know that."
    
    show trina smirk
    tr "\"Wow, that's suspiciously non-descript.\""
    
    si uncomf "\"...\""
    
    "Just remembering it makes me queasy."
    
    show trina happy at cright
    
    "Trina claps me on the back with more force than necessary."
    
    tr "\"That's all? I mean, come on, you just interviewed for your dream job! How do you feel?\""
    
    "I try my best to smile bravely but the sudden realization that Debra might've heard me call her 'Debrow' has me feeling a little... deflated."
    
    "As only a best friend can, she gets the hint."
    
    show trina neutral
    tr "\"You know what you need? {w}A strong dose of Trina's Luong Island Iced Tea.\""
    
    "I can sense the pun, but I ignore it."
    
    show simone neutral
    si "\"Lay it on me.\""
    
    show trina happy
    tr "\"You got it, kiddo.\""
    
    scene black with dissolve
    $ renpy.pause(2.0)
    
    si none "\"...Kiddo?\""
    
    si none "\"Seriously, Trina? Please tell me you didn't think I was going to let that slide.\""
    
    tr "\"It's my new word. Don't fight greatness, Simone. {w}Don't fight it.\""
    
    "I let her placate me with drinks as we chat late into the night, putting the thoughts of my maybe-maybe-not-botched interview behind me."
    
    window hide
    
    stop music fadeout 1.0
    
    jump mon1_morning