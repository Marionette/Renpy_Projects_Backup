#You are the clone. Sarah says you're the clone
label badend:
scene bg room
stop music fadeout 2.0
show mike sideglance at right
show sarah normalcross at left
"Sarah turned to me."
s "So. Mike."
y "Yes?"
show mike sidepanic at right
show sarah determined at left

"To my horror, Sarah pointed a gun at me. Her face was stern."
play music "sfx/finaldecision2.ogg"
scene bg gunsarah with fade
s "Who are you, really?"
y "Woah, Sarah! What are you doing?!"
m "Sarah?! Why do you have your gun?!"
s "Well, aren't you glad?"
y "Alright, let's just calm down here."
s "Oh-hoh. Don't try my patience, bucko. {w} My trigger finger is getting itchy."
s "Answer the question."
s "Who are you and what are you doing in my boyfriend's skin?"
m "Ugh.{w=0.2}.{w=0.2}.{w=0.2} This is just like watching a nightmare come to life."
menu:
    "Deny":
        jump this
    "Come clean":
        jump nothis
label this: 
y "Sarah, please put the gun away."
s "Did you really think lying your way through this whole thing was going to end well for you?"
s "I'm going to ask you again."
s "Why are you doing this?"

menu:
    "Deny":
        jump this2
    "Come clean":
        jump nothis
label this2:
y "Sarah, I {i}am{/i} Mike!"
y "You're making a big mistake!"
s "Oh, am I? {i}Am I{/i}, motherfucker? Do you wanna bet?"
play sound "sfx/gunclick.ogg"
"Sarah's eyes blazed with anger."
"My body began to tense up too. Sweat poured out of my orifices."
m "Sarah, you're scaring me."
s "Good. You {i}should{/i} be scared."
"She nudged the gun's nose at me."
s "Him, most of all."
s "Are there more of you? What's your end game? Answer!"
menu:
    "Deny":
        jump this3
    "Come clean":
        jump nothis
label this3:
y "Put the gun down, Sarah!"
play sound "sfx/gunshot.ogg"
scene bg bloodyfoot with flash
"My ears rang as a gunshot was fired."
y "ARHGH!"
m "{fast}{i}Oh my god!! You just shot him on the foot!{/i}"

with flashblood
play sound "sfx/dripcrack.ogg"
"A hot throbbing pain started to bubble in my leg."
s "Now, you can't run away."
s "Next bullet will be in your gullet."
m "Sarah! I think you need to calm down with the torturing!"
s "Don't tell me to calm down, Mike."
s "Whatever he is, he does {i}not{/i} mean well."
m "I'm just concerned, you know."
m "I mean, you just shot {i}'other me'{/i} with a straight face!"
m "You are being way too {i}calm{/i} about this."
s "Let's just say my imagination has had enough practice."
m "W-What?!"
s "Don't worry, honey. It's going to be alright."
menu:
    "Deny":
        jump this4
    "Come clean":
        jump nothis
label this4:
y "Sarah...! P-please!"
y "I told you everything I can."
s "No, you didn't."
s "You're a liar."
s "And this is your last chance."
s "I'm going to ask you for the last time."
s "Who are you?"
menu:
    "Deny":
        jump this5
    "Come clean":
        jump nothis
label this5:
y "Believe me, Sarah!"
s "Wrong answer."
stop music
play sound "sfx/gunshot.ogg"
with flashblood
play sound "sfx/dripcrack.ogg"
"The bullet rang in my ears."
scene bg black with fade
"There was no pain."
"Just darkness."
scene bg black with flashbloodfinale
stop music fadeout 4.0
"End 8 - The Dead Ringer"
scene bg black with fade
return
jump start

label nothis:
stop music fadeout 2.0
y "{w=0.2}.{w=0.2}.{w=0.2}."
y "I was just playing the game."

scene bg room with fade
show dopey smallsmile with dissolve
y "Thought it might be fun."
s "So. {w}You finally show your true face."
show dopey closed
play music "sfx/double.ogg"
y "I don't have a {i}'true'{/i} face. {w}That's boring."
y "You humans get attached to the pettiest things."
"I watched as Sarah's stance changed ever so slightly."
show dopey smallsmile
"She meant business now."
"Even Mike picked the bat up again."
show dopey closedsmile
s  "What are you?"
menu:
    "Answer":
        jump answer1
    "Attack":
        jump attack
label answer1:
show dopey talk2
y "Does it really matter?"
show dopey cheeky
y "I'm simply a lost soul that got hungry."
show dopey normal
y "Let's keep it at that."
m "Why me? Why my face? Did I do anything to deserve this?"
menu:
    "Answer":
        jump answer2
    "Attack":
        jump attack
label answer2:
show dopey smallsmile
y "No particular reason. Maybe it's fate."
show dopey closedsmile
"I shrugged."
y "But really, it was just a while since my last meal. Your life looked tasty enough."
show dopey normal 
s "Ugh!"
m "Uhm.{w=0.2}.{w=0.2}.{w=0.2} Thanks?"
show dopey smallsmile
y "Don't mention it."
s "Mike!{w} Are you humoring the supernatural creature mimicking {i}your{/i} face?!"
m ".{w=0.2}.{w=0.2}.{w=0.2}."
show dopey talk
y "Haha!"
s "Are there more of you out there?"
menu:
    "Answer":
        jump answer3
    "Attack":
        jump attack
label answer3:
show dopey talk2
y "Do you really want to dig deeper?"
y "It's better if you don't. I don't think you'd survive the truth."
show dopey closed
y "But there {i}are{/i} more of us."
y "We are old. We are hungry. We lie in the shadows looking for prey."
show dopey normal
y "That's all you need to know."
m "..."
s "So you are eating Mike's life?!"
menu:
    "Answer":
        jump answer4
    "Attack":
        jump attack
label answer4:
show dopey calm
y "Yes. {w}It takes about a week."
y "His skills, knowledge, and personality are disintegrating as we speak."
m "...!"
y "Even his memories."
show dopey normal
y "That is probably why Mike can't remember anything from yesterday."
show dopey calm
y "Soon, without any of his humanity to sustain him, his own body will fail and atrophy."
y "Starting from the heart, to his internal organs, to his brain."
y "And when he is nothing more than a husk, I will assimilate what is left of his life force."
show dopey normal
m "{w=0.2}.{w=0.2}.{w=0.2}. "
m "Sounds like heaps of fun."
s "I will not let that happen!"
stop music fadeout 2.0
menu:
    "Leave peacefully":
        jump leave
    "Attack":
        jump attack
label leave:
show dopey closed 
y "During this moment of digestion, I am at my weakest."
y "I am most--"
y ".{w=0.2}.{w=0.2}.{w=0.2}Human."
show dopey normal
show dopey closedsmile
s "..."
show dopey talk2
y "Sarah. Everything I said is still true."
show dopey calm
y "I am still Mike. Heart and Mind.{w} I am he. And he is I."
show dopey normal
y "Right now, at least."
y "I can't hurt you, Sarah.I can feel the chemicals in my blood."
y "My memories..."
y "My judgement.{w} It's clouded."
show dopey closed
y "{i}*Sigh*{/i}"
y "It's just my luck I picked one of the few humans with a pure heart."
m "{i}P-Pure{/i}..?!"
m "How about {i}'all around nice guy'{/i}, hm? Can we just call me that?"
s "Better get rid of thy porn stash soon, pure boy. Angels a-weeping."
show dopey calm
y "If you let me go now, I will break the curse."
m "...!"
m "You can break the curse!?"
y "It's not going to be easy."
y "But yes, I can do that."
y "I'm the only one who can."
show dopey normal
s "How can we be sure?"
s "You might be tricking us into let you go!"
show dopey closed
y "{w=0.2}.{w=0.2}.{w=0.2}."
play music "sfx/fakesarahdeath.ogg"
y "If you trust Mike, then trust me."
show dopey mike
y "I'm never a good liar when it comes to you--"
y ".{w=0.3}.{w=0.3}.{w=0.3}Sarah."
"{w=0.2}.{w=0.2}.{w=0.2}."
"Sarah's grip on the gun relaxed."
scene bg angrysarah with fade
s "Do it then. Fix this mess."
s "But let's just make something clear."
s "If Mike shows any kind of deterioration during this week, you can bet your ass I will hunt you down."
s "If you're still Mike, you know how serious I am."
s "Am I understood?"
y "Yes. I'll keep in contact."
scene black with fade
"{w=0.2}.{w=0.2}.{w=0.2}."
"Goodbye, Sarah..."
scene bg black with flashfinale
stop music fadeout 4.0
"End 7 - The Stranger"
scene bg black with fade
return
jump start

label attack:
show dopey angrysmile
y "I think this has gone on long enough!"
"I lunged for the gun."
m "SARAH!"
stop music
play sound "sfx/gunshot.ogg"
with flash
scene bg black 
"The sound of the gun shot echoed in my ears and in my body."
"I didn't know why I did it."
"{w=0.2}.{w=0.2}.{w=0.2}."
"I could've easily overpowered them."
"But somehow{w=0.5}.{w=0.5}.{w=0.5}."
"I hesitated at the last second."
scene bg black with flashbloodfinale
stop music fadeout 4.0
"End 8 - The Dead Ringer"
scene bg black with fade
return
jump start