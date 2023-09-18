#If you leave anytime in the game before Sarah arrives.

label earlyend:
menu:
    "Fine, let's deal with it tomorrow.":
        jump fool
    "I'm staying here.":
        jump cont
label fool:
scene bg room
stop music fadeout 0.2
show mike normalsad2 at right
y "Alright, I'll stay out of this tonight."
"It was difficult, but I managed to quell my emotions and get it under control."
"I knew I wouldn't be able to accomplish anything without a clear head."
show mike normalsad at right
m "I'll deal with Sarah for tonight, okay?"
show mike regret2 at right
m "Maybe I can ease her into the situation."
m "You'll be fine. It'll be better tomorrow."
y "..."
show mike worried at right
m "Quick!"
m "She's coming downstairs!"
scene black with fade
"Before I knew it, my other self ushered me out the door and slammed it behind me."
play sound "sfx/doorslam.ogg"
"I could still hear Sarah's voice in the other room inquiring what I've been up to."
"My heart ached to go back there and tell her everything."
"But I..."
"I chose not to."
"Maybe I was too scared to face her like this."
"Somehow it all felt like my fault."
"{i}I'm such a coward!{/i}"
"..."
"{i}Well, enough of that.{/i}"
"{i}I'll deal with it tomorrow!{/i}"
"I needed time to think.{w} Gather my thoughts and make sense of this situation."
"Maybe he was right."
"Those couple of hours that my memory missed might hold the key to unlocking the mystery."
"I walked on towards the town, thinking of a way around this mess."
scene bg mirror with fade
"As I passed by a store window, I noticed my reflection."
"Strange.."

"Was it just me, or did I look suddenly thinner?"
with flash
play sound "sfx/heartbeat.ogg"
y "Ugh!"
"A sharp pain squeezed my heart as the thought crossed my mind."
"I struggled to breathe."
"My chest heaved in erratic rhythms."
"My... heart!"
play sound "sfx/thump2.ogg"
with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
with flashblood
scene bg black
y "Urhk!"
play sound "sfx/heartbeat.ogg"
"{i}What's... happening to me?{/i}"
"Blood dripped from my nose."
"It was then realized that I didn't have a lot of time left."
"I was{w=0.2}.{w=0.2}.{w=0.2}. dying."
"And I didn't know why..."
play sound "sfx/heartbeat.ogg"
with flashblood
y "S-sarah...!"
"The corners of my visions started to darken, like a curtain falling on a play."
play sound "sfx/heartbeat.ogg"
scene bg black with flashbloodfinale
stop music fadeout 4.0
"End 9 - The Fool"
scene bg black with fade
return
