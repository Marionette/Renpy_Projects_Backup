label q1:

menu:
    "Well, I guess.":
        jump q1a
    "Not really.":
        jump q1b 
label q1a:
y "Well, sorta."
y "After all, it's not everyday you meet an exact replica of yourself."
$ agree +=1
$ agreecount += 1
return
label q1b:
y "Not really."
y "I'm not vain enough to talk to my clone, thanks."
$ disagree +=1
$ disagreecount += 1
return

#####################################################
label q2:
menu:
    "Nah, she'll be fine!":
        jump q2a
    "Yeah, take it back!":
        jump q2b
label q2a:
y "She'll be fine!"
y "She's a police officer!"
y "She's used to these kinds of stressful situations, right?"
m "I don't think you know what you're talking about."
$ disagree +=1
$ disagreecount += 2
return
label q2b:
y "Do you think we can still undo this?"
m "I don't think so."
$ agree +=1
$ agreecount += 2
return
################# SARAH ARRIVES ################################################
label q3:
menu:
    "Tell the truth.":
        jump q3b
    "Tell a lie.":
        jump q3a
label q3a:
show sarah dubious at left
y "Eating dinner with you and falling asleep in front of the T.V.?"
show mike unsure3 at right
show sarah suspicious at left
s "Very poignant."
$ lie +=1
$ liecount += 1
return
label q3b:
y "I remember hearing a noise in the kitchen but I thought it was nothing."
y "I grabbed a beer from the fridge."
y "Then something hit me in the head."
$ truth +=1
$ truthcount += 1
return
#################################################################
label q4:
menu:
    "Ugh, I hate that carpet.":
        jump q4b
    "No, you hit me with the bat.":
        jump q4a
label q4a:
y "You hit me in the head with the bat!"
show sarah sidesuspicious at left
m "I did {i}not{/i}. I was too busy freaking out!"
m "And don't you blame your clumsiness on me!"
m "I already have plenty to spare!"
show mike shy at right
show sarah sideamused at left
s "I should second that."
show sarah dubious at left
s "..."
y "..."
s "Guess it's time for that joke to retire."
$ disagree +=1
$ disagreecount += 3
return
label q4b:
show sarah dubious at left
y "I hate that carpet."
show sarah sidedubious at left
y "And what's with that smirk?"
show mike annoyed at right
y "Like you never tripped on that carpet yourself?"
show mike annoyed2 at right
m "...Bleh."
show sarah exasperated at left
s "My sister gave us that carpet out of the goodness of her heart."
show mike smirk at right
show sarah sidesuspicious at left
m "...That explains so much."
show sarah ohplease at left
s "Hmp."
$ agree +=1
$ agreecount += 3
return
#################################################################
label q5:
menu:
    "Yes. Let's think about it later":
        jump q5a
    "Nope! The fake has to leave.":
        jump q5b
label q5a:
show sarah dubious at left
y "Yeah. Let's not rush into that conclusion yet."
y "Take it one step at a time."
$ agree +=1
$ agreecount += 4
return
label q5b:
show mike normalsad at right
show sarah suspicious at left
y "Well, it doesn't have to be hard."
y "The fake has to leave. Simple as that."
y "It's only fair."
show mike unsure2 at right
show sarah thinking at left
y "And for that, we need a judge."
$ disagree +=1
$ disagreecount += 4
return
#################################################################
label q6:
menu:
    "Yep. February 26.":
        jump q6a
    "February 27!":
        jump q6b
label q6a:
show sarah dubious at left
y "February 26, Thursday."
$ agree +=1
$ agreecount += 5
return
label q6b:
y "February 27!"
show mike annoyed at right
show sarah confused at left
m "Huh?"
show sarah suspicious
y "Well, it was midnight. {w} So technically, it was the 27th!"
show mike annoyed2 at right
m "Hmp."
m "Devil's in the details!"
$ disagree +=1
$ disagreecount += 5
return
#################################################################
label q7:
menu:
    "Myles Jordan Jansen.":
        jump q7a
    "What? Who?":
        jump q7b
label q7a:
show sarah dubious at left
y "Myles Jordan Jansen."
show sarah dubious at left
y "And exactly why I call him that every chance I get!"
show mike victory at right
show sarah ohplease at left
m "Right on!"
$ agree +=1
$ agreecount += 6
return
label q7b:
show sarah confused at left
y "Who?"
show sarah ohplease at left
y "The only brother I have is a beaver-faced alien named Buckteeth."
show mike happy at right
show sarah exasperated at left
m "Haha!"
show sarah dubious2 at left
s "Come on guys, his teeth aren't that big!"
show mike victory at right
m "Yes, they are!"
$ disagree +=1
$ disagreecount += 6
return
#################################################################
label q8:
menu:
    "Yes! I love dogs!":
        jump q8a
    "Hyenas.":
        jump q8b
label q8a:
$ agree +=1
$ agreecount += 7
show sarah dubious at left
y "Yeah! I adore dogs!"
show sarah ohplease at left
y "I should remember to get one after this whole thing is over."
show sarah amused at left
s "Oh, sure! As long as you remember to water the plants everyday."
show mike shy at right
show sarah smug2 at left
b "{i}*whine*{/i}"
return
label q8b:
show sarah comicshock at left
y "Hyenas, man!"
y "Hyenas are cool!"
show mike excited at right
m "Oh! Yes! They are!"
show sarah concerned at left
s "Are you guys kidding?"
s "That is so random."
show mike happy at right
show sarah sidesuspicious at left
m "I was just watching a feature on them in Animal Planet."
show mike unsure at right
m "Before all this..."
show mike excited at right
m "But they're so cool!"
show sarah suspicious at left
y "And wicked smart too!"
show mike happy at right
y "There might be a rerun tonight. Maybe we should watch it."
show sarah exasperated at left
s "Oh, good god."
$ disagree +=1
$ disagreecount += 7
return
#################################################################
label q9:
menu:
    "Tell the truth":
        jump q9a
    "Tell a lie":
        jump q9b
label q9a:
show mike shy at right
show sarah angrythinking at left
y "But that's why it's a secret!"
y "I can't tell you!"
show sarah amused2 at left
s "Honey!"
s "Is it about my cooking?"
show sarah smug2 at left
y "Uh..{w}.{w}.{w}"
y "...I dunno..."
show sarah amused2 at left
s "..."
$ truth +=1
$ truthcount += 2
return
label q9b:
show mike shy at right
show sarah dubious at left
y "Uhmm..."
y "I broke the lamp and made it look like an accident?"
show mike unsure at right
show sarah amused2 at left
s "That's not a secret, Mike."
$ lie +=1
$ liecount += 2
return
#################################################################
label q10:
menu:
    "*snicker*":
        jump q10a
    "Naw. It's not {i}that{/i} bad.":
        jump q10b
label q10a:
show sarah dubious at left
y "*snicker*"
$ agree +=1
$ agreecount += 8
return
label q10b:
y "Well..."
y "It's not {i}that{/i} bad."
show mike worried at right
m "Hey! Don't you wash your hands off of this!"
show mike annoyed at right
m "You thought about it too!"
show sarah smug2 at left
y "Err..."
$ disagree +=1
$ disagreecount += 8
return
#################################################################
label q11:
menu:
    "Tell the truth.":
        jump q11a
    "Tell a lie.":
        jump q11b
label q11a:
show sarah pissed2 at left
show mike nervous at right
y "Uhm...{w} Okay..."
y "Well, there was way too much chili, first of all."
y "My bottom was on fire for days. It was horrible."
y "Mmm... the texture too, {i}*shivers*{/i}. I dunno. It just felt like eating barf."
y "I mean, It looked like barf..."
y "It tasted like pure death..."
y "And the smell of the kitchen afterwards--"
y "I thought something really {i}did{/i} die--"
show mike nervous2 at right
m "...shhhhhhhh...{w} shut {w}up!"
m "...shut up!"
y "B-b-b-ut, other than all that, it's okay!"
y "The plates had a nice floral pattern!"
show mike nervous at right
m "Ahehehe..."
show sarah pissed at left
s "The plates!"
$ truth +=1
$ truthcount += 3
return
label q11b:
y "It was a bit undercooked."
show mike unsure at right
show sarah pissed2 at left
m "Yeah, darling."
m "You just need a {i}bit{/i} more practice!!"
show mike shy at right
s "Oh really?"
show mike cringe at right
show sarah pissed at left
s "Is that why you order take-out {i}everytime{/i} I cook?"
s "Should've disposed of the evidence better, sweetie."
show mike shy at right
$ lie +=1
$ liecount += 3
return
#################################################################
label q12:
menu:
    "Tell the truth":
        jump q12a
    "Tell a lie":
        jump q12b
label q12a:
show sarah pissed2 at left
y "I liked the macaroni."
show mike unsure at right
m "Yeah, those were good too."
show mike shy at right
show sarah pissed at left
s "The macaroni was a microwave meal."
show sarah pissed2 at left
y "..."
$ truth +=1
$ truthcount += 4
return
label q12b:
show sarah dubious at left
show sarah pissed2 at left
show mike nervous at right
y "Yeah."
y "I love those pizzalets."
show mike nervous2 at right
show sarah pissed at left
s "My mom cooked those."
show sarah pissed2 at left
y "...Oh."
$ lie +=1
$ liecount += 4
return
#################################################################
label q13:
menu:
    "Tell the truth.":
        jump q13a
    "Tell a lie.":
        jump q13b
label q13a:
show mike nervous2 at right
y "Ask {i}him{/i} first!"
show sarah verypissed at left
s "So, that's a yes."
y "No!"
$ truth +=1
$ truthcount += 5
return
label q13b:
show mike unsure4 at right
show sarah pissed2 at left
y "I believe that both Paris and my girlfriend, Sarah Ellis, are attractive females that are worthy of praise and this fact matters little to the deep and enduring relationship I have with Sarah Ellis, the love of my life."
s "..."
s "..."
show sarah pissed at left
s "Bullshit."
show mike cringe at right
$ lie +=1
$ liecount += 5
return
#################################################################
label q14:
menu:
    "Tell the truth":
        jump q14a
    "Tell a lie":
        jump q14b
label q14a:
show mike unsure at right
y "She's friendly..."
show sarah ohplease at left
y "I've talked to her a few times."
y "She was nice."
s "..."
y "What?"
show sarah annoyed at left
s "Hmp!"
show mike shy at right
y "I mean, she wasn't intimidating! Didn't try to bite my head off or anything--"
show sarah dubious at left
s "Oh sure!"
show sarah annoyed at left
s "And the fact that she flashes her jewels around the neighborhood has {i}nothing{/i} to do with her being {i}nice{/i}."
y "I didn't even know that!"
y "But you should call me next time she does! Hehe--"
show sarah ohplease at left
y "--hehe{w=0.2}.{w=0.2}.{w=0.2}.h{w=0.2}e{w=0.2}--{w=0.2}{i}*gulps*{/i}"
s "..."
$ truth +=1
$ truthcount += 9
return
label q14b:
show sarah dubious at left
y "She's just a girl! No big deal!"
show sarah annoyed at left
s "Yeah, and you've been making house calls."
show mike sideconfused at right
m "Whut?"
show sarah ohplease at left
s "Something about fixing her email. Yeah, right!"
show mike cringe at right
y "No, no! It's just that!"
y "She's got some serious malware problem."
show mike unsure4 at right
m "I've told her to stop clicking on those 'Lose your Flab' emails--"
show mike shy at right
m "Honestly, that woman--"
show sarah annoyed at left
s "{w=0.2}.{w=0.2}.{w=0.2}."
y "I was just being nice!"
s "..."
show sarah scary2 at left
s "Just don't let me catch you doing something you shouldn't, bucko."
s "I have ears everywhere."
show mike freaked at right
m "Guh.."
$ lie +=1
$ liecount += 9
return
#################################################################
label q15:
menu:
    "Tell the truth.":
        jump q15a
    "Tell a lie.":
        jump q15b
label q15a:
show sarah huh at left
y "Paris Beaufort is as dumb as a brick."
show mike snicker at right
m "{i}*snicker*{/i}"
y "I'm sorry... {w}but she is."
y "She's a sweet girl. But dude."
y "Poor girl even thinks England is in Africa."
y "Also, if you try sunbathing in a polluted, overpopulated, middle-class residential area with low walls--"
y "Chances are, you are a little soft in the head."
show mike happy at right
m "Haha! That's true!"
s "..."
show sarah amused3 at left
s "{i}*snicker*{/i}"
$ truth +=1
$ truthcount += 6
return
label q15b:
show sarah dubious at left
show mike normalsad at right
y "Ever since I laid eyes on you.."
show sarah blush at left
y "I haven't found any other girl attractive."
show mike normal at right
show sarah suspicious at left
s "Liar."
show sarah sweet at left
s "*smiles*"
$ lie +=1
$ liecount += 6
return
#################################################################
label q16:
menu:
    "Tell the truth":
        jump q16a
    "Tell a lie":
        jump q16b
label q16a:
show sarah normalcross at left
show mike smirk at right
y "Hey! You know, I'm all for that!"
y "I might get lucky!"
show sarah smug2 at left
m "Right."
$ truth +=1
$ truthcount += 7
return
label q16b:
show sarah dubious at left
y "I could almost agree."
y "I just want this all to be over."
show sarah pain at left
$ lie +=1
$ liecount += 7
return
#################################################################
label q17:
menu:
    "I agree with that.":
        jump q17a
    "Battle it out.":
        jump q17b
label q17a:
show sarah dubious at left
y "I agree with that."
y "But I'm the one who's staying."
$ agree +=1
$ agreecount += 9
return
label q17b:
show sarah comicshock at left
y "Battle it out the classic way!"
show mike annoyed2 at right
show sarah confused at left
y "Through a duel, maybe. Or a fist fight."
y "Best man wins!"
show sarah dubious at left
s "I hope you aren't serious."
$ disagree +=1
$ disagreecount += 9
return
#################################################################
label q18:
menu:
    "Tell the truth.":
        jump q18a
    "Tell a lie.":
        jump q18b
label q18a:
show sarah normalcross at left
y "Yes, I am the real Mike."
$ truth +=1
$ truthcount += 8
return
label q18b:
show sarah dubious at left
y "Yes, I am the real Mike!"
$ lie +=1
return
#################################################################
label q19:
menu:
    "No, I can't convince you":
        jump q19a
    "Yeah, we both did our best":
        jump q19b
label q19a:
y "I can't convince you."
y "There's no way to tell. You said so yourself."
y "All I know is I am Mike, and there's nobody else I can be."
$ disagree +=1
$ disagreecount += 10
return
label q19b:
show sarah dubious at left
y "Like he said,"
y "We answered your questions. It's the most we can do for now."
y "But you need to believe me when I say I'm the real Mike."
$ agree +=1
$ agreecount += 10
return
#################################################################
label q20:
menu:
    "Tell the truth.":
        jump q20a
    "Tell a lie.":
        jump q20b
label q20a:
show sarah normalcross at left
y "I don't know."
y "I can't leave. {w}I don't want to!"
$ truth +=1
$ truthcount += 10
return
label q20b:
show sarah dubious at left
y "I'm going to take it like a man and leave on my own."
$ lie +=1
$ liecount += 10
return
