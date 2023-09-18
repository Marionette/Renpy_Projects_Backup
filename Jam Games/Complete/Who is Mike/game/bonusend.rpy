#You are the clone. Sarah says you're Mike. 
label bonusend:
stop music fadeout 2.0
scene bg room
show mike unsure3 at right
show sarah sidenormalcross at left
"Sarah turned to the other Mike."
s "Mike."
show mike sideerr at right
show sarah exasperated
m "Yes?"
show sarah sidepain at left
play music "sfx/doom.ogg" fadein 3.0
s "Were you telling the truth about leaving the house if I think you're the fake?"
show mike sidepanic at right
show sarah exasperated at left
m "S-sarah?"
s "{w=0.2}.{w=0.2}.{w=0.2}."
m "No! {w}Sarah! {w}I'm the real Mike!"
show sarah sidenormalcross at left
s "{w=0.2}.{w=0.2}.{w=0.2}.I don't know about that."
"I sighed with genuine pity."
show mike veryangry at right
show sarah goofypain at left
y "{w=0.2}.{w=0.2}.{w=0.2}.I'm sorry."
m "Shut up!"
show mike sidepanic at right
show sarah exasperated at left
m "Sarah, {w}why?! {w}What did I do wrong?"
m "T-Tell me!"
show mike worried at right
show sarah concerned at left
s "You didn't do anything wrong."
s "Both of you didn't."
show sarah sideconcerned at left
s "That's why this is so hard."
show mike sidepanic at right
show sarah exasperated at left
m "T-Then you have to believe me!"
m "I'm the real Mike!"
show sarah confused2 at left
s "My instincts are telling me otherwise, and I'm pretty certain about it."
show mike sideangry at right
show sarah sideconcerned at left
m "Then your instincts are wrong!"
with flash
m "Will you just listen to me?"
"The other Mike grabbed Sarah by the shoulders and shook her."
"Sarah winced in discomfort."
menu:
    "Push him away":
        jump push
    "Calmly tell him off":
        jump telloff

label telloff:
"I didn't really plan on interrupting."
"For the sake of civility and his deflated ego, I thought it better to shut up."
"But I had to intervene when he almost hurt Sarah."
"His emotions were out of check and running hot. There's no knowing what he'll do."
show mike cornered at right
show sarah pain at left
y "Mike. Stop that."
"The sound of his name coming from my lips made him wince."
show sarah exasperated at left
y "You're hurting her."
show mike defeat at right
m "..."
show sarah pain at left
"The atmosphere between the three of us turned to a glaring chill."
"He quietly took his hands off Sarah's shoulders, his jaw set grim like stone."
"But I could see his hands visibly shaking in silent rage."
"After telling him off like that, more than ever, he was now the villain."
"A position that was both demeaning and hostile."
"Even worse, it was pushing him nearer to the edge of reasonable doubt."
y "Look, I know this is hard for you too, okay?"
y "But don't blame Sarah for this."
m ".{w=0.2}.{w=0.2}."
show sarah exasperated at left
y "She made her decision and we should respect that."
show mike veryangry at right
m "Of course!"
m "Easy for you to say that, you smug bastard--"
show mike cornered at right
y "You really should calm down, buddy--"
show mike veryangry at right
play sound "sfx/woosh.ogg"
scene bg black with fade
s "Mike!"
"We were all surprised as the other Mike swiped the bat from the table and pushed me to the ground."
play sound "sfx/thump2.ogg"
with flash
m "So you're acting like my {i}pal{/i} now, huh, {w}{i}buddy?{/i}"
m "Must be nice playing the innocent!"
jump fighty

label push:
show mike veryangry at right
scene bg black with fade
with flash
play sound "sfx/grip.ogg"
"I grabbed the guy at the collar and yanked him away from Sarah."
play sound "sfx/thump2.ogg"
scene bg room
"He staggered for a bit. His eyes glinted with rage and hurt."
"We regarded each other with blinding hate."
"I could never forgive him for hurting Sarah."
"So his ego was hurt. So Sarah said he was the fake."
"Well, that just proves it! That was the point of this whole exercise!"
"As far as I am concerned, a stranger has {i}no{/i} fucking right to lay a finger on my girlfriend."
"I bared my teeth at him."
y "Don't you touch her."
y "{i}Imposter{/i}."
"{i}'Other Mike'{/i} gnashed his teeth."
play sound "sfx/woosh.ogg"
"He picked up the wooden bat from the floor and charged at me."
play sound "sfx/thump2.ogg"
with flash
jump fighty

label fighty:
scene bg room
m "{i}Fucking asshole!{/i}"
play sound "sfx/punch1.ogg"
with flash
"We rolled and struggled on the floor."
play sound "sfx/hit.ogg"
scene bg room
with flash
play sound "sfx/punch1.ogg"
scene bg room
play sound "sfx/punch2.ogg"
with flashb
play sound "sfx/bigcrash2.ogg"
play sound "sfx/punch2.ogg"
with flashb
"I could feel the hot rage radiating from his skin like vapor."
"Sarah tried to break us up, but with adrenaline running high, it was futile."
"In the end, he got the better of me."
with flashblood
play sound "sfx/grip.ogg"
y "Ughk!"
"He pushed the wooden bat into my throat. My air passages clung onto scarce breaths."
scene bg angrymike with fade
s "S-Stop!!"
"Sarah tried to push him away."
with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
with flash
play sound "sfx/grip.ogg"
y "Aghk!"
m "You come into my house, steal away my life, {w}my face--"
m "Why don't you just {w}{i}die{/i}?!"
with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
with flashblood 
"He raised his fist to make one final blow to break my neck and silence me forever."
play sound "sfx/gunshot.ogg"
stop music
with flash
scene black with dissolve
"The gunshot rang in the air like a blade."
play sound "sfx/thump2.ogg"
"The man in front of me crumpled into a limp pile."
scene bg sarahcries with fade
"{i}So Sarah brought her gun with her.{/i}"
"{i}Why am I not surprised?{/i}"
play sound "sfx/fall.ogg"
"A second passed, and Sarah fell to her knees in tears."
play music "sfx/fakesarahdeath.ogg"
"I ran to her and held her in my arms."
"Her eyes were wide and glazed over."
scene bg mikedies with fade
y "{w=0.2}.{w=0.2}.{w=0.2}."
s "{w=0.2}.{w=0.2}.{w=0.2}."
s "I shot you.."
s "I-I{w} didn't know what to do.. I--"
s "He wouldn't stop--"
y "Shh..{w} I know, honey.. I know."
s "{w=0.2}.{w=0.2}.{w=0.2}."
s "{w=0.2}.{w=0.2}.{w=0.2}.but I shot you."
"Tears began to well up in her eyes."
"She didn't sob or cry though."
"She just let them fall, almost confused at the wet fluid running down her cheeks."
y "No, Sarah."
"I wiped her tears off patiently."
y "Hey. Look at me."
"I place my hands on her face and looked into her eyes."
y "Look at me."
y "I'm still alive, aren't I?"
y "I'm still here."
"She stared back through the tears."
"For the briefest of moments, a flicker of doubt crossed her face."
"I expected her to ask something. To make sure."
"But Sarah gave one last look at the dying Mike and shuddered."
"She closed her eyes and nodded, tired and desperate."
"She rested her ear on my chest, comforted by my beating heart."
s "{w=0.2}.{w=0.2}.{w=0.2}."
s "I'm{w=0.2}.{w=0.2}.{w=0.2}. shaking."
s "I guess, you never really get used to shooting a person. Even in my line of work."
y "That's a good thing."
s "I... didn't know it would be this bad with a loved one involved."
s "I-It was terrible."
s "..."
s "I'm going to need fucking therapy after this."
y "You did what you had to do, Sarah. Don't blame yourself."
s "{w=0.2}.{w=0.2}.{w=0.2}."
scene bg room with fade
y "It's over now."
y "Let's forget this ever happened."
s "{w=0.2}.{w=0.2}.{w=0.2}."
s "...yeah."
"I held her tighter and she snuggled in my chest."
scene bg mikewins with dissolve
s "{w=0.2}.{w=0.2}.{w=0.2}."
s "Mike."
y "Hmm?"
s "I love you{w=0.2}.{w=0.2}.{w=0.2}."
s "But if you ever show up as two of you again, I am out."
y "I love you too, Sarah."
#Mike's eyes glow red.
"I can feel a smile escape my lips."
scene bg dopewins with Dissolve (0.5, alpha=True)
y "Never again{w=0.2}.{w=0.2}.{w=0.2}." 
y "I promise."
scene bg black with flashfinale
stop music fadeout 4.0
"End 6 - The Sly"
scene bg black with fade
return
