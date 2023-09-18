  #-----------------------------------------------
  # CHAPTER 2
  #-----------------------------------------------
label lbl_PathC_2_0:

  #B2.0"
  #(Continuation of 1.9)

  #play music music_Sugar_On_My_Tongue #(Continue from 1.9)
  #scene cg forest7 #(as in 1.9 before)
  #TODO [fade out Duran
  $ renpy.transition(slow_dissolve, layer="master")
  hide duran
  show merona t content OM#; position as before
  show cimaria neutral
  mk "Okay. Dur-"

  show merona t surprised
  show cimaria surprised
  "I turned to talk to Duran, but he was already walking to Kreita and Rett."

  show merona t sadSmile OM
  show cimaria gentle
  mk "*sigh* Thanks, Cimaria."

  play music music_Travel_Light
  #TODO [fade in CG forest7
  #TODO [fade in CS duran t annoyed#; center
  #TODO [fade in CS merona t serious#; right
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest7
  show duran t annoyed
  show merona t serious:
    yalign 1.0
    xalign 0.75
  "I ran up to him, and he glanced at me."

  show duran t annoyed OM
  dt "Oh, you again."

  show duran t annoyed S
  show merona t serious OM
  mk "Yeah, me again. You didn't have to walk away so quickly."

  show duran t annoyed OM S
  show merona t angry
  dt "No, I didn't, but I just had to escape."

  show duran t annoyed
  show merona t angry CE
  mi "Wonderful."

  #TODO [fade in CS wagon#; left
  #TODO [fade in CS kreita content#; left from center
  #TODO [fade in CS rett neutral#; left from Kreita
  $ renpy.transition(slow_dissolve, layer="master")
  show wagon at left
  show kreita content:
    yalign 1.0
    xalign 0.25
  show rett neutral:
    yalign 1.0
    xalign 0.0
  show duran t neutral
  show merona t serious
  "Luckily, our conversation didn't last any longer, for we came up to Kreita and Rett soon enough."

  show merona t content
  show kreita happy
  kh "Hey guys! You two need something?"

  show merona t content OM
  show kreita neutral
  mk "Yeah. We wanted to help you and Rett with whatever you need-separately, that is."

  show duran t annoyed
  show merona t sadSmile
  show kreita surprised
  kh "Separately? So... Not working together?"

  show duran t annoyed OM
  show kreita neutral
  dt "Yep."

  show kreita sceptical
  show duran t annoyed
  "Kreita gave us a strange look, but she shrugged."

  show merona t content
  show kreita content OM
  kh "Alright. A little weird why you two would want to do that, but anything works, I guess."

  show duran t neutral
  show kreita content
  show rett content
  "Rett paused from organizing the cart and stretched his head to see us."

  show rett content OM
  rt "We could use some help in gathering extra firewood. Food and water too."

  show duran t smirk
  show merona t surprised
  show rett content
  "Duran raised his hand."

  show duran t smirk OM
  show merona t serious
  show kreita grin2
  dt "I'll find the firewood."

  show duran t neutral
  show rett content OM
  rt "I think I saw some fallen beech trees around the bend we passed back there, so you could-"

  show duran t evilGrin OM
  show kreita content
  show rett surprised
  dt "Yeah, yeah, yeah, I know what to find. I'll find something good."

  show duran t evilGrin#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide duran
  
  show merona t sadSmile
  show kreita grin
  show rett smirk
  "He swiveled around and headed away. I looked at Kreita and Rett, trying to silently apologize for his... abruptness."

  play music music_Dark_Red_Wine
  show merona t content
  show rett laugh
  rt "*laugh* He's a fun one. I'm excited to hang around with him. So Merona, you're fine with getting water and food?"

  show merona t content OM
  show kreita content
  show rett content
  mk "Yeah. Hopefully I can find a brook nearby or some nice nettle... I'll be back soon."

  show merona t content
  show rett content OM
  rt "Be safe."

  play music music_Lafayette
  #TODO [fade in CG forest8
  #TODO [fade in CS merona t content#; center#; walking animation
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest8
  show merona t content at center
  show merona t content at walkBounce
  "Rett and Kreita waved me off, and I strolled over to the forest. The closer I went, the more I felt at ease. There was something about all those trees that made me feel better. "

  #TODO [play animation sunShine~
  show sunrays movie
  
  "Maybe it's the branches. All the branches lace together to form a roof, protecting me from anything up above but also allowing beautiful splotches of sunlight to paint a golden tone over the younger plants and the ground."

  show merona t content CE
  "Maybe it's the pure sheen of green that washes across everything. This lush shade of green that only nature could create is the one color I'd be willing to see forever."

  play sound sound_ambiance
  show merona t content
  "Maybe it's the music the forest produces. The melody of cicadas and grasshoppers along with the accompaniment from wind rustling through leaves forms the most lovely orchestra I've ever heard."

  
  show merona t grin:
    yalign 1.0 #; stop walking animation
  "Scanning my surroundings for anything edible, a smile grew on my face when I spotted clusters of red and black in a shrub right ahead of me."

  #TODO [Stop Sound Nature Ambiance
  #TODO [stop animation sunShine~
  stop sound 
  #hide sunrays movie
  show merona t determinedGrin OM
  mk "Didn't think I'd get to see you guys so quickly."

  play music music_Green_Leaves
  #TODO [fade in CG raspberry
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg raspberry
  "I crouched down and opened one of my stained satchels. Though a couple of berries were underripe, most were at just the right stage for eating and could be kept for a few days."

  "I plucked a shiny raspberry from its stem and observed it for a few seconds."

  mi "Even if we declare the natural world to be too wild for civilization, there's already so much order in a simple berry."

  scene bg white with fade
  "I filled my bag close to the brim with the fruit. Getting up, I continued walking forward."

  #TODO [fade in CG forest9
  #TODO [fade in CS merona t reflective#; center#; walking animation
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest9
  show sunrays movie
  show merona t reflective at center
  show merona t reflective at walkBounce
  
  mi "It'd be really great if I could find some clover too... Dandelion and chickweed would also be good..."

  show merona t serious
  "A few minutes passed with nothing to be found, but a shifting pitch soon caught my ears and grew louder the further I went."

  show merona t grin at RunBounce #; faster walking animation
  #TODO [start sunShine animation again please
  "I quickened my pace and reached the top edge of the small slope I was walking on."

  play sound sound_water loop #(loop until end of chapter please)
  show merona t happy#; stop walking animation
  mk "Even more perfect."

  play music music_Lafayette
  "A gurgling creek, basking in full sunlight, greeted me from below."

  mi "Water seems rather clean too... It works for drinking."

  show merona t content :
    yalign 2.5#; move her sprite down 200px
  "I hopped down to the creek's edge, took my gloves off, and stuck the jug in, letting the current fill it up. The cool water soothed my hand, and I immediately put in my other hand."

  mi "Ah... If only I could jump in and take a bath right now!"

  show merona t content CE
  "With the sun warming my back, the faint hum of the forest, and the water trickling over my skin, I closed my eyes and could only think of one thing."

  mi "This is home."

  $ renpy.transition(slow_dissolve, layer="master")
  hide sunrays movie
  scene bg black
  stop sound
  pause(1.0)
  
  return
  
  #-----------------------------------------------
label lbl_PathC_2_1:

  #B2.1"

  #TODO [just info for myself: Music: Life
  #TODO [just info for myself:  CG forest11
  #TODO [fade in merona t content#; app. x=70%
  #TODO [fade in cimaria neutral#; app. x=25%
  $ renpy.transition(slow_dissolve, layer="master")
  show cg forest11
  show merona t content:
    yalign 1.0
    xalign 0.7
  show cimaria neutral:
    yalign 1.0
    xalign 0.25
  
  "Cimaria tapped my shoulder."
  show merona t surprised
  show cimaria neutral OM
  ck "How has this been?"
  show merona t surprised OM
  show cimaria neutral
  mk "My shoulder? So far there haven't been any issues that I've taken notice of. It's functioning."
  show merona t content
  show cimaria gentle OM
  ck "Good. I'm going to take a look at it when we're stopped tonight. Please continue to make sure that you don't do anything too strenuous for it."
  play music music_She_dreams_in_blue
  show merona t content OM
  show cimaria gentle
  mk "Of course. Thanks for looking after it and everything else you've done."
  show merona t grin
  show cimaria grin
  "Cimaria smiled."
  show merona t content
  show cimaria laugh
  ck "It's what I do. It's all that I can do for you."
  show cimaria content#; fade out  
  $ renpy.transition(slow_dissolve, layer="master")
  hide cimaria
  "She walked towards the others."
  play music music_meronatheme
  show merona t reflective
  mi "I wonder what it's like to be a healer and have that power of knowing what's wrong with someone's body. My ability kind of makes me a healer, right? I'm like a plant and animal healer in a way, but I don't necessarily cure them."
  show merona t grin
  mi "I like what my ability does though! It'll be real useful to me when I'm done with my studies, so even better."
  show merona t grin ER
  "I looked around at my surroundings."
  show merona t determinedGrin
  mi "Are these trees and plants healthy? I'm almost tempted to go and try to feel if there're any problems. What a good idea, suddenly run out and grab a mess of dirt of roots to diagnose plants. I think that-"



  return
  #"-------------------------------------------------------"
  
label lbl_PathC_2_3:


  #B2.3"

  play music music_White
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t surprised OM:
    yalign 1.0
    xalign 0.75
  show cimaria serious
  show rett neutral
  show kreita sceptical:
    yalign 1.0
    xalign 0.1
  mk "I'm guessing that he's here inside, but maybe he had to go do something privately. Bathroom, perhaps? He definitely went inside with us."


  return
  
  #-----------------------------------------------
  
  
label lbl_PathC_2_8:

  #B2.8"

  play music music_potHappy
  $ renpy.transition(slow_dissolve, layer="master")
  show prowen neutral:
    yalign 1.0
    xalign 0.25
  show merona at ShoulderTap2
  "I was also hanging around at the back, and I tapped his arm."

  show prowen surprised
  mi "It'd be nice to talk to him, since he doesn't know anyone. I can get to know more about him too if he's okay with it."

  show prowen neutral
  show merona t surprised OM
  mk "Uh, hi... Prowen. Can I call you that?"

  show merona t serious
  "He looked down at me, not changing his expression."

  show prowen neutral OM
  show merona t content
  pm "Sure. Sorry, what was your name again? I don't have the best memory, and I'm getting old too..."

  show prowen neutral
  show merona t content OM
  mk "Oh, that's fine! It's Merona. Merona Kovene. You can just call me Merona."

  show prowen neutral OM
  show merona t content
  pm "Alright, Merona. What do you need from me? Or is something wrong?"

  show prowen neutral
  show merona t content OM
  mk "No, nothing's wrong. And I guess you can say that I need something from you... I'd like to know more about you?"

  show prowen neutral OM
  show merona t content
  pm "Uh... sure. What do you want to know?"

  show prowen neutral
  show merona t reflective
  mk "..."

  play music music_Words
  show prowen sceptical
  show merona t happy
  mk "...Whatever you're okay with sharing?"

  #TODO [fade in CS prowen neutral
  $ renpy.transition(slow_dissolve, layer="master")
  show prowen neutral:
    yalign 1.0
    xalign 0.25
  show merona t grin
  "Prowen raised an eyebrow, but brought it back down soon."

  show prowen neutral OM
  show merona t content
  pm "Well..."

  pm "You know my name. Prowen Mair."

  pm "I'm from the southwest coast area."

  show prowen neutral
  mk "..."

  show prowen neutral OM
  show merona t grin
  pm "And I'm interested in... nature."

  show prowen neutral
  show merona t happy
  mk "Really? So am I! I have the ability of plant and animal life manipulation, so that is right up my field of semi-expertise."

  show prowen neutral OM
  show merona t grin
  pm "That's... nice."

  show prowen neutral
  show merona t content OM
  mk "What do you like about nature?"

  show prowen neutral OM
  show merona t content
  pm "Nature... is interesting. It has interesting things in it."

  show prowen neutral
  show merona t content OM
  mk "Yeah, it sure does. What's your ability?"

  stop music fadeout 1.0
  show prowen neutral OM
  show merona t surprised
  pm "Memory manipulation."

  show prowen neutral
  show merona t reflective
  mi "Ooh, that seems like a good one. I wonder what kind of jobs he can do with that ability. Hopefully, he doesn't do any brainwashing or trickery to others..."

  play music music_recollections
  show merona t content OM
  mk "Oh cool, I haven't met anyone with a mental manipulation type ability before. Can you do memory manipulation to your own memory then? It'd be a big help to remember everyone's names here, ha ha."

  show prowen tired OM
  show merona t surprised
  pm "Well, abilities don't apply to the person him or herself. Your ability doesn't affect humans, so I suppose you wouldn't know of this."

  show prowen forcedSmile
  show merona t surprised OM
  mk "Oh, I didn't know. Better not mess with my memory then! *laugh*"

  show prowen tired
  show merona t content
  pm "Mm hm."

  show merona t sadSmile
  mi "It'd be funny if he actually did tamper with my memory of our journey, and everything that happened was fake."

  scene bg black with fade



  return
  
  #-----------------------------------------------
  
  #-----------------------------------------------
  # CHAPTER 3
  #-----------------------------------------------
  
label lbl_PathC_3_3:

  #TODO [fade out Boyen
  $ renpy.transition(slow_dissolve, layer="master")
  show black at Blinking
  hide boyen
  "I collapsed onto the ground and remembered the mini-storms of dust that bloomed around me after I was pushed down by the monster."

  #TODO [fade in CS kreita serious OM and show it "blinking" like Boyen's sprite#; right side
  show kreita serious OM behind black:
    xalign 0.75
    yalign 1.0
  kh "Merona, we're here!"

  show kreita serious#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide kreita
  #TODO [fade in CS rett aggressive OM and show it "blinking" like Boyen's sprite#; left side
  $ renpy.transition(slow_dissolve, layer="master")
  show rett aggressive OM behind black:
    xalign 0.25
    yalign 1.0
  rt "You're safe, everything is under control!"

  play sound sound_harshFootsteps loop
  show rett aggressive#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide rett
  "I could feel everybody's footsteps closing in on me."

  #(voice continues shaking)
  scene cg danger
  mi "It just sounds like more monsters."

  mi "There's even more to tear me apart."

  #TODO [Stop sound loop of harshFootsteps
  stop sound
  scene bg white with fade
  ck "Everyone, stop and give her some space! You're all scaring her more.."

  "The footsteps paused."

  stop music fadeout 1.0
  mi "It's Cimaria."


  #TODO [fade in CS cimaria gentle#; transparency down to 30%, center
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria gentle
  show black:
    alpha 0.7
  mi "Cimaria."

  play music music_River_Meditation
  #TODO [erase Cimarias sprite
  #TODO [fade in CG sunsetScape6, transparency down to 40%
  $ renpy.transition(slow_dissolve, layer="master")
  hide cimaria
  show cg sunsetScape6:
    alpha 0.4
  mi "She was there when I woke up."

  #TODO [fade in CG cimaria leaving1, transparency down to 50%
  $ renpy.transition(slow_dissolve, layer="master")
  show cg C_leaving1:
    alpha 0.5
  mi "The first time I met her."

  #TODO [fade in CG examination2, transparency down to 60%
  $ renpy.transition(slow_dissolve, layer="master")
  show cg examination2:
    alpha 0.6
  mi "She was helping me."

  #TODO [white screen
  scene bg white
  mi "I was... "

  mi "Okay."

  #TODO [fade in CG campingFire
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg campingFire
  "I lifted my head a smidge and turned to a different angle."

  play music music_piano
  mi "I was okay."


  return
  #"-------------------------------------------------------"
  
  
  
  
  #-----------------------------------------------
  # CHAPTER 4
  #-----------------------------------------------
  
label lbl_PathC_4_4:
  
  play music music_White
  #(Continuation of 4.3)
  show cg hillSide2
  #TODO [Positions as in 4.3
  show lexan neutral
  show merona t determined OM
  mk "Sorry, but I'm going to have to secure this monster down somewhere first. I need to put it somewhere safer!"

  show lexan content CE#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide lexan
  show merona t serious
  "Lexan nodded and continued packing up the cart."

  show merona t worried
  mi "Sorry Duran, I hope you can get woken up by someone else or even wake up on your own-The first thing I have to deal with is finding the proper place to put this little monster. But where would be good?"

  show merona t disappointed OM
  mk "Ugh, I need to find somewhere fast... Um...Oh!"

  show merona t grin
  mi "I think I have a little bag inside my main one. That should work."

  show merona t content
  "I grabbed my bag and thrusted my hand inside, feeling around for the smaller one. I threw it out and held it next to the monster."

  play music music_Words
  show merona t reflective
  mi "Hm... Should be good. I think I'll leave it a bit open, so it doesn't get corded up too tightly and tie it onto my bag."

  $ renpy.transition(slow_dissolve, layer="master")
  scene cg hillSide
  show wagon
  show lexan neutral:
    yalign 1.0
    xalign 0.7
  
  show duran t tired:
    yalign 1.0
    xalign 0.9
  show merona t content:
    yalign 1.0
    xalign 0.3
  "I trotted to the cart and waited for everyone else. I gave Lexan, who was finished with his duties, a nod, and I saw that Duran was indeed up and cleaning up his belongings."

  show merona t determinedGrin
  mi "I have to say, at least on the bright side we have a monster. An actual monster, I'm pretty sure. All these years, people have been making such a big fuss over the threat of monsters growing and growing, but now we actually have one in our hands."

  show merona t serious
  mi "..."

  play music music_Soporific
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg FishmonsterEyes
  "I untied the monster pouch from my bag and took out the monster, laying it out on my palm."

  mi "I guess its eyes stayed opened right when it died. It has lovely eyes though, not just for a monster, but in general. If you look at it from certain angles and lighting, you could also say that it's... kind of good looking."

  mi "But the more I look at it, the more it just seems odd to me. It's like it's familiar in a sense, but it's also quite foreign. Moreover, it's dead, so it's going to look even stranger. Perhaps I'm feeling this way because it did happen to be another living, breathing thing."

  mi "I wonder if we'll be able to preserve it in time. What's the difference between monsters and animals health-wise? When will it really start decomposing? What's the internal structure of a monster like? So many things we don't know yet..."

  play music music_newBegin
  mi "It's already been several years since I've heard about monster sightings and the problems coming with them. But as a society, we still don't have that much information on them as we'd like-I suppose too many people got killed trying to get more knowledge on them or not enough were brave enough to volunteer."

  mi "Now, we have something that can actually help people understand these creatures more. What we're going to do with this small monster now... we don't know yet."


  $ renpy.transition(slow_dissolve, layer="master")
  scene cg hillSide
  show wagon
  show lexan neutral:
    yalign 1.0
    xalign 0.7
  show duran t neutral:
    yalign 1.0
    xalign 0.8
  show merona t content:
    yalign 1.0
    xalign 0.1
    
  pause(0.5)
  #TODO [fade in #(later)...
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria neutral:
    yalign 1.0
    xalign 0.0
  # [CS cimaria neutral#; left from Merona
  # [CS rett neutral#; center - behind cart
  show rett neutral behind wagon
  show kreita content:#; between cart and Merona
    yalign 1.0
    xalign 0.3
  # [CS boyen content#; right from Duran
  show boyen content:
    yalign 1.0
    xalign 1.1

  "Everyone came by the cart once they prepared all their things."
  $ renpy.transition(slow_dissolve, layer="master")
  scene bg black #and from black#; move Merona to center #(show her again after black is gone), erase all other sprites including the wagon
  show merona t content
  pause(1.5)
  #TODO [change CG to hillSide2 with a fade in #(leave Merona visible)
  scene cg hillSide2
  show merona t content
  
  return
  #-----------------------------------------------
label lbl_PathC_4_5:
  
  
  play music music_piano
  #(Continuation of 4.4)
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest18
  #TODO [fade in CG forest18
  show merona t worried OM#; center
  
  mk "*sigh*"
  show merona t worried
  mi "What a situation we're in."
  show merona t serious
  "Chattering between the others rose up as we moved forward."

  "I looked back at the monster in my palm."
  show merona t determined
  mi "I'm going to try and make the best out of this dead monster as much as possible. Such a good opportunity is right here in my hands... the only question is what exactly can I do with it?"
  play music music_Under_the_Stairs
  show merona t surprised
  show prowen sceptical OM at right#; right
  pm "What are you holding?"
  show merona t content
  show prowen sceptical
  "I turned halfway around to see Prowen, straining his eyes to get a better look at the monster."
  show merona t content OM
  show prowen neutral
  mk "Oh, it's just the monster we got. Want to see it?"

  show merona t content
  "He extended his arm, and I placed both the bag and monster in his hand."
  show prowen content
  pm "..."
  show merona t grin
  show prowen content OM
  pm "Interesting..."
  show merona t happy
  show prowen content
  mk "Yeah, I think so too. Doesn't seem like your typical monster you hear about."
  show merona t content
  show prowen serious
  "He continued scrutinizing it, prodding away at it as well."
  show merona t serious
  show prowen serious OM
  pm "As a society, we still haven't been able to gather much information on these creatures."
  show prowen appalled OM
  pm "Haven't even been able to give a proper name to them."
  show merona t serious OM
  show prowen serious
  mk "Huh... they are simply called 'monsters'. Strange how we haven't really even done something like label them."
  stop music
  show merona t serious
  show prowen neutral OM
  #TODO [fade in sunShine animation
  $ renpy.transition(slow_dissolve, layer="master")
  show sunrays movie
  pm "'Monster'."
  show prowen neutral
  pm "..."
  play music music_Ill_be_right_behind_you_Josephine
  show merona t surprised
  show prowen neutral OM
  pm "What do you think when you hear that term?"
  show merona t worried OM
  show prowen neutral
  mk "Dangerous. Bad..."
  show merona t serious OM
  mk "Overall, just negative things."
  show merona t serious
  show prowen forcedSmile OM
  pm "Exactly. It has a negative connotation."
  show prowen neutral
  mi "True. Anything called a monster isn't exactly all that likable. That applies to actual monsters."
  show merona t surprised OM
  show prowen serious
  mk "Ever since they cropped up, everyone called them monsters. Even the government. The title just stuck, I suppose."
  show merona t surprised
  show prowen content OM
  pm "What if they didn't?"
  show merona t serious OM
  show prowen content
  mk "Didn't have a negative implication?"
  show merona t serious
  show prowen content OM
  pm "What if..."
  play music music_eerie
  show merona t surprised
  show prowen determined OM
  pm "...they were beneficial in their own way?"
  show prowen determined
  mi "Beneficial... beneficial to us? Beneficial to nature? Monsters seem to have only caused trouble in the past through the present not only to people but to the natural world as well. If they were to be beneficial, how could that work? What would we do?"

  show merona t disappointed
  show prowen serious OM
  #(Murmuring, low voice) "
  pm "It could have both positive and negative effects... much like a double edged sword."

  stop music
  show merona t disappointed OM
  show prowen neutral
  mk "What? Um, I couldn't catch what you just said."

  show merona t serious
  show prowen serious
  pm "..."
  show prowen neutral CE
  "Prowen shook his head."
  play music music_Under_the_Stairs
  show prowen neutral OM
  pm "Never mind."
  show merona t surprised
  show prowen sceptical OM
  pm "Forget all that I said."
  show merona t worried OM
  show prowen sceptical
  mk "Huh? What for? Sorry, did I say something to offend you?"
  show merona t worried
  show prowen sadSmile OM
  pm "No. Nothing like that."
  show merona t sadSmile
  #TODO [fade out sunShine animation
  $ renpy.transition(slow_dissolve, layer="master")
  hide sunrays
  pm "Just forget what I said. I ramble sometimes. It's been a while since I've been with the same people for an extended amount of time."

  play music music_White
  show merona t content OM
  show prowen sadSmile
  mk "Oh, it's alright. I don't mind listening to people talk."
  show merona t surprised
  show prowen annoyed OM
  pm "That's what they all say until they find something to disagree with."
  show merona t surprised OM
  show prowen annoyed
  mk "...I can't argue against that."
  show merona t content
  show prowen serious
  pm "..."
  show prowen neutral
  "He handed the monster back to me."
  show prowen neutral OM
  pm "Thanks for showing me this. I have to speak with Cimaria about something now, so... bye."
  show merona t content OM
  show prowen content
  mk "Thanks for the chat!"
  play music music_Lafayette
  show merona t content
  show prowen neutral#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide prowen
  "Prowen shuffled forward, and I moved the monster into a better position in my hands."
  show merona t grin
  mi "Prowen... I'm glad that I got to talk to him a bit more. I haven't really had the chance to get to know him."
  show merona t reflective
  mi "What he said about monsters being beneficial... being good..."
  show merona t serious
  "I looked down at the monster again."
  mi "Perhaps a day will come when we'll know what exactly these creatures are and give them a respectable name. But for now, there isn't any room for us to hold and cherish them."
  return
  #-----------------------------------------------
label lbl_PathC_4_7:

  #TODO [As before:
  #play music music_recollections
  #scene cg forestGround
  #show mattress#; center
  #show merona t determined#; center, use Merona hair u please
  #show blanket#; center

  #show Clouds dark#; opacity around 30-50%#; "
  #"if possible, use a "multiply" mode for them please#; "
  #"slowly move from right to left please
  mi "You know what? I'm going to climb a tree. I'm just going to go and throw myself up a tree. Because why not?"
  #TODO [move the blanket down by 200px
  show blanket:
    yalign 4.5
  "I tossed aside my covers and stretched my sides out."
  #TODO [fade out Merona's sprite
  $ renpy.transition(slow_dissolve, layer="master")
  hide merona
  mi "I think the others are still sleeping, so I'll have to stay on the quiet side. Here's to hoping that I don't fall down or see anything too shocking... I need to at least go somewhere farther from here."

  play music music_Green_Leaves
  scene cg forest19
  show tree at right
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content behind tree#; with Merona hair t again please
  "I walked out of the clearing and wandered into the forest, peering around for a suitable tree. Stroking the bark of each one I passed, I grimaced at how sharp most of them were. There weren't a lot of great trees with branches to hang onto either."
  show merona t determined
  mi "Ugh, I have to do something! Might as well just close my eyes and climb the tree I walk right into."
  show merona t serious
  mi "..."
  show merona t surprised
  mi "Actually, I think I just might try doing that."
  show merona t content CE
  "I squeezed my eyes shut and braced my teeth."
  mi "..."
  mi "......"
  show merona t sadSmile CE
  mi "This feels like a pretty bad idea, but... I really want to do anything to get myself awake."
  mi "I don't know. This is confusing me. But I'm just going to do this for giggles."
  play sound sound_grassFootsteps
  show merona t content CE:#; move her sprite a bit to the right
    yalign 1.0
    xalign 0.6
  "I turned around in a circle a few times, and took a tiny step to the left."
  mi "..."
  #TODO [move her sprite to right a bit more
  show merona t content CE:
    yalign 1.0
    xalign 0.7
  mi "Okay. I haven't touched anything. That's both good and bad. Take another bigger step, Merona."

  play sound sound_punch
  show merona t disappointed OM CE at RightBump#; bump her against CS tree and back
  mk "Ow!"
  play sound sound_punch
  show merona t disappointed CE
  "I went forward this time, banging my foot against a tree trunk, and I wobbled from the impact. I vigorously shook the foot that was hit."
  show merona t sad CE
  mi "Well, I can only blame myself for not expecting something like that to happen."
  play music music_meronatheme
  show merona t content
  "I opened my eyes and scanned the tree in front of me."
  show merona t reflective
  mi "Hm..."
  show merona t grin
  mi "Decent branching, almost-rough-enough-to-cut-into-your-skin bark, and really tall. Not the best, but not the worst. It'll make do. I'm the one here who's so desperate to climb a tree right now after all..."
  show merona t determined
  "I jogged a few meters away from it and positioned my body in a bent stance."
  show merona t determinedGrin
  mi "Time to commence an attack on this colossal tree."
  scene cg climb2
  "I ran up and threw myself at the trunk with the air beating against my face, trying to get my feet and hands to grip onto the trunk or a branch. Luckily, there was a lower branch on the right, and I managed to clasp my right hand onto that one."
  mi "Excellent."
  mi "The last time I tried climbing a tree was for Kreita and Rett I believe. If I remember correctly, I think this attempt was much better than the last one. Or maybe I'm only thinking of how I was dragged on the ground, and that's the only memory I have of the time I spent with them."
  "Taking my time, I hiked up one of my legs and used my lower body to push up my entire body, getting my left hand onto the next highest branch. I placed another leg higher and pushed myself up again, continuing to grip onto branches with my hands. As I repeated this process, I managed to climb up onto a sturdier branch that I could sit on and see some scenery."
  play sound sound_ambiance loop #(loop)
  scene cg forestTop
  show merona t content OM:#; sprite positioned 250px lower than usually
    yalign 2.5
    xalign 0.5
  #TODO [sunShine animation
  show sunrays movie
  mk "Ah, this is pretty nice."
  play music music_potHappy
  show merona t content
  "I swung my legs back and forth and let my eyes gaze over what I could see from my position."
  show merona t grin
  mi "Even if it's not at a height where I can see the tops of trees, I like feeling this elevated. Maybe I'll even see some little forest animals crawling over the other trees since I have a direct view of these higher branches."
  play sound sound_wind
  show merona t content
  "The wind blew in. I scooted back against the trunk and propped my legs straight on the branch, but I still managed to get touched by the wind through the fluttering leaves. The leaves continued to waver over my head."
  show merona t sleepy
  mi "So... I guess I'm feeling more awake now. The bark piercing into my palms sure helped, but these little breezes coming in might make me sleepy..."
  #TODO [Fade out Sound Nature ambiance
  stop sound fadeout 1.0
  show merona t sadSmile
  mi "At least if I fall asleep, I'll fall down and immediately be fully awake."
  show merona t content CE
  "I closed my eyes."
  play music music_Epilogue
  mi "I wonder how things are back in Laneo."
  mi "It's only been a few weeks, but I wonder what my friends are up to these days. It's summer break at the moment, so I'm sure they're having loads of fun with their time."

  $ renpy.transition(slow_dissolve, layer="master")
  scene bg black
  mi "..."
  
  mi "I wonder how my parents are doing."
  mi "I haven't really contacted them all that much...did I even write a letter to them about what I'm doing? I can't remember much. But even if I didn't, the headmaster surely would have sent one."

  #TODO [fade out sprites
  #hide Mum
  #hide Dad
  mi "I wonder if they're okay. I wonder if my pets are okay. I wonder how my other friends at my hometown are."
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forestTop
  
  #TODO [fade in #(at the same time) CS merona t sad#; sprite positioned 250px lower than usually
  show merona t sad:
    yalign 2.5
    xalign 0.5
  #TODO [sunShine animation
  show sunrays movie
  mi "..."
  play music music_Ill_be_right_behind_you_Josephine
  "I sighed."
  show merona t disappointed
  mi "I should start thinking about the people I don't see as often a bit more. I feel like I'm almost neglecting them in a way...so I hope that letters from me right now will suffice for those people."
  show merona t serious
  mi "I should concentrate on Rett's situation more at the moment though. Ugh, so many things to think about. I feel muddled. But..."
  play music music_newBegin
  show merona t determined
  mi "...I want to think about more than what I'm thinking of right now."
  show merona t worried
  mi "I don't know how I can be much use, but if I could discover something or have something just pop out of the blue that'd let me help... that'd be nice."
  show merona t determined
  #TODO [stop sunShine animation
  hide sunrays
  mi "For now, I'm going to try the best I can to do things for a little bit of everything. Letters to people. Better lessons on my part. Rett. Food. Monsters."
  play sound sound_fallInDirt_short
  scene cg climb2
  "I let my legs down and placed my feet down one at a time on each alternating branch, almost like stepping down a wide ladder, and I jumped off the tree."
  scene cg forest19
  show merona t content OM
  mk "Alright... Here we go. *laugh* Maybe if everyone else is still sleeping I can wake them up."
  return
  #-----------------------------------------------
  
  
  #-----------------------------------------------
  # CHAPTER 5
  #-----------------------------------------------
label lbl_PathC_5_2_1:
  
  #play music music_life #(from before)
  show cg forest22 #(from before)
  #(sprite positions as before)
  show cimaria content:#; left from Kreita:
    yalign 1.0
    xalign 0.3
  show kreita grin#, center
  show merona t surprised OM:#, right from Kreita:
    yalign 1.0
    xalign 0.7
  show rett content:#, right from Merona
    yalign 1.0
    xalign 0.9
    
  mk "Hm... can I try helping both actually?"
  show merona t sadSmile
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan neutral:#, right from Merona
    yalign 1.0
    xalign 0.9
  show rett content:#, right from Merona
    yalign 1.0
    xalign 1.0
  "Lexan wrinkled his nose."
  show merona t serious
  show lexan neutral OM
  ln "I suppose that sounds alright, but it may be too troublesome for you to go back and forth between the two groups."
  show merona t reflective
  show lexan neutral
  "I tried thinking of a reason to counter back with, and an idea flower popped out of the soil in my mind."
  play music music_Dark_Red_Wine
  show merona t content OM
  mk "How about I try helping one group out first, and then for the second half of time, I could go to the other group? When I switch groups, I could also be somewhat of a messenger. Rett can switch as well."
  show merona t content
  show lexan serious
  "The others stopped to think about my proposition for a bit."
  show merona t grin
  show lexan content
  show rett content OM
  rt "That sounds good enough. We could work that out."
  show rett content
  show cimaria content OM
  ck "I don't see a problem with it if it goes smoothly..."
  show cimaria content
  show kreita content OM
  kh "Okay, so Merona will try to participate in both groups then! Which one will you go to first?"
  show kreita content
  show merona t content OM
  mk "I'll go to... the marketplace first!"
  return
  #-----------------------------------------------
label lbl_PathC_5_2_2:
  
  play music music_Travel_Light
  #TODO [fade in CG town
  $ renpy.transition(slow_dissolve, layer="master")
  hide tree
  show cg town behind merona
  show clouds behind cg at leftright
  show cg_sky1 behind clouds 
  show rett neutral#; center
  show cimaria neutral:#; left from center
    yalign 1.0
    xalign 0.25
  show boyen content at left
  show merona t content:#; right from center
    yalign 1.0
    xalign 0.75
  show lexan content at right
  hide kreita
  "Kreita huddled her group together, and the rest of us gathered into a cluster as well. Cimaria placed her hands on her hips."
  show cimaria neutral OM
  show boyen neutral
  ck "The herb you should look for can be commonly found in this area, if the map is accurate. I assume that it may or may not be on display in some shops since it's more of an unique plant used for certain medical reasons, so you can also try asking the owner if they have it."
  show cimaria neutral
  show rett neutral OM
  show merona t grin
  show lexan grin
  rt "What's it called? Don't tell me it's some long, hard-to-pronounce name."
  play music music_Shes_on_my_Mind
  show cimaria laugh
  show rett neutral
  "Cimaria laughed and tilted her head to the side."
  show cimaria content OM
  show rett smirk
  show boyen content
  ck "It does have a 'long, hard-to-pronounce' name, but it also has a normal one: yander. It was named after the person who discovered and identified it."
  show cimaria grin
  show merona t serious
  show lexan content
  "After finishing her sentence, Cimaria's smile became wry."

  show cimaria wink OM
  show rett pouty
  show boyen grin
  show lexan determined
  ck "Is that basic enough for you?"
  show cimaria wink
  show rett grin
  show merona t surprised
  show lexan content
  "I raised my eyebrows. Rett snorted and over-exaggeratedly rolled his eyes."
  show cimaria grin
  show merona t determinedGrin
  mi "Looks like my theories of her and Rett are starting to get more and more proof... Let's see if Rett will add even more."
  show rett laugh
  show merona t content
  show lexan sceptical
  rt "Ha ha, yeah. But still, it was on the verge of being too much. I just can't handle words longer than four letters, you know? That's as long as my name is after all."
  play music music_Travel_Light
  show cimaria grin CE
  show rett neutral
  show boyen content OM
  show merona t grin
  bg "Your last name is six letters, you know."
  show cimaria content
  show rett pouty
  show boyen content
  "Rett, feigning dismay, nodded at Boyen."
  show rett pouty OM
  show boyen grin
  show lexan content
  rt "Touché, pal. Touché."
  show rett surprised
  show boyen content
  show merona t determinedGrin
  "Cimaria patted Rett's shoulder, and kept her hand there. She looked at all four of us."
  show cimaria content OM
  show rett content
  ck "Well, if you've had enough of that revelation, I say we should start looking. We ca-"
  stop music fadeout 1.0
  show cimaria neutral
  show rett neutral
  show merona t surprised
  show lexan neutral
  "She stopped and stared at Rett. He gazed at her as well with one of his eyebrows raised. Cimaria raised a corner of her mouth and shook her head."
  show cimaria serious
  show rett surprised
  ck "..."
  show rett surprised OM
  show boyen neutral
  rt "Hm? What is it?"
  show cimaria serious OM
  show rett surprised
  show boyen grin
  show merona t sadSmile
  show lexan surprised
  ck "You should be in the other group."
  play music music_Greek_Dance
  show cimaria serious
  show rett surprised OM
  show lexan neutral
  rt "What?! But isn't Mer-"
  show rett neutral
  "He looked over at the preservationist group still standing there, and his head shot back over to ours. He scanned us over and locked eyes with me."
  show cimaria neutral
  show rett laugh S
  show boyen content
  show merona t content
  show lexan content
  rt "Oh... Oh, okay! Sorry, I thought you went with the others. Guess I wasn't paying attention."
  show cimaria content
  show rett embarrassedGrin
  show merona t content OM
  mk "Uh, don't worry, that's fine! We all can't notice every detail sometimes, ha ha..."

  play music music_Radio_Martini
  show merona t content
  "Rett chuckled, his cheeks flushing a shade of pink, and he placed his hand at the back of his head."
  show cimaria neutral
  show rett embarrassedGrin OM
  show merona t grin
  rt "Yeah... I usually end up doing stuff with Cimaria, so..."
  show cimaria neutral CE
  show rett smirk
  "Cimaria shrugged."
  show cimaria neutral OM
  show rett pouty
  show merona t determinedGrin
  ck "Well, you're not always going to end up with me."
  show cimaria serious OM
  show rett grin S
  show merona t serious
  show lexan serious
  ck "You should probably hurry to the other group now though. Go before they forget about you."
  show cimaria serious
  "Rett nodded, but gave an unfortunate smile."

  play music music_Shes_on_my_Mind
  show cimaria surprised
  show rett content OM
  show merona t content
  show lexan content
  rt "It'd be nice if I could do more things with you now... But I'll get going. Have fun shopping, soon-to-be-with-again group!"
  show cimaria neutral
  show rett neutral#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide rett
  "Cimaria didn't react much to his words, and she spun back towards us who remained."
  show merona t determinedGrin
  mi "Yep, I definitely got some more proof from that little banter we had going on here. This might be one of my few theories that have a higher probability of coming true."
  show cimaria neutral OM
  show boyen grin CE
  show merona t content
  show lexan determined
  ck "So... let's get the yander."
  return
  #-----------------------------------------------
label lbl_PathC_5_3:
  
  play music music_Cool_Steel_Breeze
  #scene cg town #(from before)
  #TODO [leave the sprites visible as before please...

  show cg town behind merona
  show clouds behind cg at leftright
  show cg_sky1 behind clouds 
  show boyen grin CE #(pos from before)#; fade out
  show lexan determined #(pos from before)#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide boyen
  hide lexan

  show cimaria neutral at walkBounce #(pos from before)#; start walking animation
  show merona t content at walkBounce #(pos from before)#; start walking animation
  "Shuffling forward, I followed Cimaria down to the shops."

  mi "The streets aren't well-developed enough for high-trade activity, and this area seems to offer many natural resources, so I assume that this town produces a lot of its goods locally. Though yander may not be quite plentiful around here, they might have traded for it since it seems like an useful herb."

  show merona t determined
  mi "If we don't find it, maybe there'll be alternatives. We have to try and do whatever we can to help Rett after all. Does Cimaria have something like that in mind?"

  show merona t worried
  mi "Speaking of Cimaria, I wonder how she's doing."

  show merona t serious
  show cimaria gentle
  "I hopped over and caught up with her steps. She looked over at me and smiled."

  show cimaria gentle OM
  ck "Do you need something?"

  show merona t serious OM
  show cimaria gentle
  mk "Actually, I just have some stuff I wanted to talk to you about."

  show merona t surprised
  show cimaria surprised
  ck "Nothing bad, I hope."

  show merona t content
  show cimaria gentle
  "I shook my head and smiled back."

  show merona t content OM
  show cimaria neutral
  mk "No, no. I just wanted to ask you how you were."

  play music music_River_Meditation
  show merona t sadSmile
  show cimaria worried
  "Cimaria pursed her lips and looked up, like she was trying to find the answer above in her mind."

  show merona t worried
  show cimaria worried OM
  ck "How I am? Well, I'm alright I suppose. Sort of tired, but more like a fatigued kind of tired rather than the drowsy kind."

  show merona t content
  show cimaria gentle OM
  mk "Thanks for asking."

  show merona t content OM
  show cimaria content
  mk "No problem!"

  show merona t surprised OM
  mk "Also...can I ask you more questions about the yander?"

  show merona t content
  show cimaria content OM
  ck "Yes, what of?"

  show merona t content OM
  show cimaria content
  mk "What exactly will the yander do?"

  show merona t surprised
  show cimaria neutral CE
  "Cimaria clapped and rubbed her hands together."

  show merona t grin
  show cimaria content OM
  ck "Time for a mini healing lesson, Merona."

  show merona t serious
  show cimaria neutral OM
  mk "You know what is going on with Rett? His life flow has a strange feel and pulsation to it. It does not have qualities of a critical one, nor is it a regular type, so that is what is confusing me. Though it doesn't appear to be major at the moment, I don't know if the monster venom will kick in more."

  show merona t serious OM
  show cimaria neutral
  mk "Life flow is pretty important... But it's weird that he doesn't feel uncomfortable or all that different from usual. Shouldn't he be able to tell there's something up internally?"

  show merona t serious
  show cimaria serious OM
  ck "Life flow is not automatically noticed even when changes occur because it's such a deep inner-mechanism. Like a heartbeat, it'll only become obvious to the person during serious moments. You can't exactly feel your life flow unless you try and search for it right? Your ability is connected with flora and fauna so it should be easier to detect in your case because you deal with life."

  show merona t serious CE
  show cimaria serious
  "I nodded."

  show merona t serious OM
  mk "I see what you mean. Does Rett's ability not cover that then?"

  play music music_Swimming_To_Cambodia
  show merona t surprised
  show cimaria serious OM
  ck "No. But what his ability is makes things even more confusing."

  show merona t serious
  show cimaria serious
  mk "..."

  show merona t surprised OM
  show cimaria sadSmile
  mk "Manipulation of... poison! Yeah, poison."

  play music music_Words_Fall_Apart
  show merona t nervous
  show cimaria serious CE
  "Cimaria sighed and crossed her arms."

  show cimaria serious OM
  ck "Exactly. Poison."

  show cimaria serious
  "I stared at her."

  show merona t surprised OM
  mk "Wait... poison, but... What?"

  show merona t worried
  show cimaria neutral OM
  ck "You would think that he should be able to handle it then, yes? But no. It must be the uniqueness of the monster venom that's causing this..."

  show merona t worried OM
  show cimaria serious
  mk "Is the poison still inside him then?"

  show merona t worried
  show cimaria serious OM
  ck "Yes. This time, I couldn't get it out of him like I did with you. This poison imbedded itself into some difficult spots, and I need to remove it before it starts manifesting in more places. So far, it has not been spreading much, but I figure that it will. I would almost need to perform a surgery to get rid of it."

  show merona t determined OM
  show cimaria neutral
  mk "...And this is where yander comes in, I guess. You need yander to help get the poison out?"

  play music music_River_Meditation
  show merona t content
  show cimaria wink OM
  ck "Smart kid."

  show merona t serious
  show cimaria neutral OM
  mk "The yander has some properties that help with attracting this poison, though I may need to mutate it, but there's the chance that it can do it."

  show merona t determined OM
  show cimaria neutral
  mk "Is there anything other than yander that can be used if we can't find it here? Maybe we should also look for other herbs."

  return
  #-----------------------------------------------
label lbl_PathC_5_4:
  
  #play music music_River_Meditation #(continue from before)
  #(Continuation of 5.3)
  show cg_sky1
  show clouds at leftright
  show cg town #(from before)
  #show merona t worried #(pos from before)#; with walking animation
  #show cimaria serious CE #(pos from before)#; with walking animation
  "Cimaria shook her head."

  show cimaria serious OM
  ck "It is already rather sketchy if yander will be sufficient, and it is the best herb I can think of that we don't already have. There isn't a point in getting any others."

  play music music_recollections
  show merona t disappointed OM
  show cimaria worried
  mk "*sigh* How unfortunate."

  show merona t worried
  show cimaria neutral
  mi "I wonder what else our group can do to help. Most of our abilities may not be as useful as Cimaria's though, since the others don't deal with living beings. Lexan works with non-body water, Duran works with fire, Boyen works with food, Kreita manipulates forces and motion, and Prowen deals with memory..."

  stop music fadeout 1.0
  show merona t serious
  mi "..."

  show merona t nervous
  mi "I wonder if he's used his ability yet."

  play music music_Soporific
  show merona t shocked
  mi "I mean, it tampers with memory, so could he have used it already on us? We wouldn't remember at all... "

  show merona t serious CE
  mi "..."

  play music music_piano
  show merona t serious
  mi "I think I'm getting ahead of myself."

  show merona t content
  mi "Prowen doesn't really seem to come off as that kind of person to trick us. I should trust him more. He's been helping us out and has no reason to mess around with us. We're not exactly loaded with money nor are we carrying valuable goods, so he should be fine."

  show merona t sadSmile
  mi "Just stop overthinking it, Merona."

  play music music_Words
  show cimaria neutral OM
  show merona t serious
  ck "You know Merona, since you work with plant life, what do you think you could do to enhance yander's properties? I was pondering over mutating it with some other essences I have, but perhaps you have some better ideas."

  show cimaria neutral
  show merona t nervous OM
  mk "Well..."

  show merona t reflective
  mi "Hm, what other ways can you increase a plant's potency? I feel like that question was a chapter title I've read before. If only I could recall what was in it..."

  show merona t content
  mi "Nonetheless, I think I may know some things that'll help. I've practiced some techniques before with Lexan, so if I remember them and execute them well, it can work. "

  show cimaria content
  show merona t content OM
  mk "I could enhance the yander if you'd like, Cimaria. I just need to use some of your stuff, and it should be okay."

  show cimaria content OM
  show merona t grin
  ck "That's actually perfect if you could do that! I think it's even good for you to practice your skills more, so this is a win-win. Is it hard to do so?"

  show cimaria content
  show merona t content OM
  mk "Well, it's more like advanced basics. Not exactly something that needs a lot of time and effort to be mastered, but something more complex than any other skill, which was where the enhancer came in handy."

  show merona t serious OM
  mk "Mutating plants is all about connecting parts of one to the other. I'm extracting what I want from the plant to add to the main one, and it only requires a partial connection of life flow to let the element easily added in. The more I want to extract, the stronger connection I need, and thus the more difficult the enhancement."

  return
  #-----------------------------------------------
label lbl_PathC_5_5:
  
  #play music music_Words #(continue from before)
  show cg_sky1
  show clouds at leftright
  show cg town #(from before)
  #show merona t content #(pos from before)#; with walking animation
  #show cimaria content OM #(pos from before)#; with walking animation
  ck "That makes sense. Later would you like to take a look at what herbs I already have to see if they are suitable for use?"
  show merona t content OM
  show cimaria content
  mk "Sure. Even if there isn't anything effective available, I can still enhance the yander by itself, though it may not be as strong as a well-mutated plant."
  show merona t surprised OM
  mk "And, I suppose it is better if the yander is merely enhanced by itself rather than a bad mutation with something useless."
  show merona t content
  show cimaria content CE
  "Cimaria nodded."
  show cimaria gentle OM
  ck "Of course."
  play music music_Travel_Light
  #TODO [fade in CG townShops
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg townShops
  show merona t content:#; right #; no walking animation
    yalign 1.0
    xalign 0.8
  show cimaria neutral:#; left from Merona#; no walking animation
    yalign 1.0
    xalign 0.6
  "We finally came into close proximity to the line of shops. Lexan and Boyen were already rummaging around in a store, so we stopped and scanned over the whole street to catch other places Cimaria and I could go to."
  show cimaria neutral OM
  ck "It's convenient that there's an herb shop that's at the front of this line of shops, but those two have got that place covered. I think not too far down the road is a pharmaceutical store judging from the symbol plastered on its windows, so perhaps we can try going there?"
  show merona t content OM
  show cimaria content
  mk "Sounds good. But by pharmaceutical, would you expect to see actual living plants there, or would they be already pressed into powders or something?"
  show merona t content
  show cimaria neutral OM
  ck "They may have plants, but definitely not in abundance like at that herb place. It's a possibility that's not too unlikely. If we can only find something like yander extract or crushed yander, do you think you could enhance it somehow?"
  show merona t reflective
  show cimaria neutral
  mi "Enhancing-and essentially most of what I know-is based on a connection to the life flow. So... nope."
  show merona t serious OM
  show cimaria sadSmile
  mk "Well... if it's dead I can't do much to it. Kind of like how a healer can't do much for a rotting corpse."
  show merona t content OM
  show cimaria content
  mk "But I think... I can mix it in with another living plant. Otherwise, you probably know about how to use and mix these kinds of things more than I do."
  show merona t content
  show cimaria content OM
  ck "That's fine. We will just have to see what we can find there then, so let's go."
  play music music_Summer_Day
  show cimaria content
  show merona t grin
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan content at left#; left
  "As we started walking again, Lexan left the place he was examining and greeted us."

  show lexan content OM
  ln "Hello! I have a good feeling we may be able to find the stuff where Boyen and I are searching now."
  show cimaria content OM
  show lexan content
  ck "A good feeling?"
  show merona t content OM
  show cimaria grin
  show lexan grin
  mk "I'm guessing being surrounded by all the greenery makes it seem like 'a good feeling' of finding it."
  show merona t content
  show lexan laugh CE
  ln "*laugh* Something along those lines."
  show cimaria content OM
  show lexan content
  ck "Hopefully your 'good feeling' will give you something real."
  show merona t grin
  show cimaria content
  show lexan determined OM
  ln "We're working on it."
  show merona t content
  show cimaria content OM
  show lexan content
  ck "Well, Merona and I are heading off to another store, so see you soon!"
  play music music_Cool_Steel_Breeze
  scene bg white with fade
  "We waved each other off and continued our own ways. Reaching the pharmacy, I pulled open the door for Cimaria, and we entered."
  return
  #-----------------------------------------------
label lbl_PathC_5_6:
  
  #play music music_Cool_Steel_Breeze #(Continue from before)
  #TODO [fade in CG pharmacy
  $ renpy.transition(slow_dissolve, layer="master")
  show cg pharmacy
  mi "Ah, the classic scent of dried flora warming under the sun. The good thing is that this place seems to sell a more traditional style of medicine, so there would be more natural products."
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content: #(pos from before)
    yalign 1.0
    xalign 0.8
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria neutral OM: #(pos from before)
    yalign 1.0
    xalign 0.6
  ck "Hm... these medicines are a bit different from what's in Laneo, but I see an abundance of local plants, so perhaps we'll find something containing yander."
  show merona t content OM
  show cimaria gentle
  mk "Let's look around then."
  show merona t grin
  show cimaria gentle OM
  ck "Great. Let me ask the clerk over there for some information then. That should be a good start."
  show merona t content OM
  show cimaria gentle
  mk "Alright. I'll go ahead and take a quick look first while you do that, in case I find something."
  play music music_life
  show merona t content
  #TODO [fade out Cimaria please~
  $ renpy.transition(slow_dissolve, layer="master")
  hide cimaria
  mi "Now then, is there living plants in here for sale?"
  show merona t serious
  "I glanced around but nothing of the sort caught my eye."
  mi "Let me observe this row of loose leaf herbs for now."
  show merona t reflective
  "I leaned in closer to the shelf on the wall behind me, squinting to read the small labels on each glass bottle."
  show merona t serious
  mi "I hope the plants here are priced by weight so that we can take however much we'd need rather than a prearranged amount... This is a common way of pricing for loose leaf herbs anyways, so I wouldn't be surprised if this was the case."
  show merona t content
  mi "We don't need too much, so it would be better cost wise to buy only a necessary clum-"

  stop music fadeout 1.0
  show merona t surprised
  mi "Wait."
  show merona t serious
  "My eyes stopped at a bottle towards the end of the lineup."
  show merona t determined
  mi "If I'm not misreading it..."

  play music music_Infinite_Perspective
  show merona t laugh
  mi "I think this says \"yander\" on it."
  show merona t grin
  "The bottle was fuller compared to its neighbors, but it did not look like it was untouched for a while-they seemed almost as if they were not completely dead yet."
  show merona t serious
  "I turned to Cimaria, but she was still talking to the clerk. I looked back at the entire text of the label on the bottle."
  show merona t content
  mi "These yander leaves are not that old... Perhaps I could still make a connection with them if we use them quickly. Are there fresh herbs here?"
  play music music_Words
  show merona t grin
  mi "For now, I'll keep track of this. I can ask Cimaria or the clerk when they're finished speaking. I'll go and check other sections in case I come across other useful items."
  return
  #-----------------------------------------------
label lbl_PathC_5_7:
  
  #play music music_Words #(continue from before)
  #scene cg pharmacy #(from before)
  #show merona t content #(pos from before)
  "Moving on, I checked out the smaller packets lined up in boxes on the bottom shelves. The \"Assorted Powders\" sign immediately identified the products."

  show merona t surprised
  mi "What could powders be used for though? I can only think of supplementing them into liquids to create serums, but do we really need that?"

  show merona t serious
  "I flipped through them, observing the variety sitting there. Towards the end, I spotted and plucked out the powdered yander."

  show merona t worried
  mi "I'll have to ask Cimaria about her exact method of using it. What if she takes a liquid extract or crushes it? A pre-done one would save us time if it's available here. But what if she needs it to be fresh?"

  show merona t content
  mi "I'll only know if I ask her."

  "I placed the packet down and glanced over to where Cimaria and the clerk were, but both had gone ahead back to their own doings. Cimaria was at another wall, looking inside a small box clutched in her hand."

  #TODO [move Merona to the center
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content:
    yalign 1.0
    xalign 0.5
  show cimaria surprised:#; left #(pos from before)
    yalign 1.0
    xalign 0.25
  "I trotted over and tapped her shoulder."

  show merona t content OM
  mk "Hey. How are things?"

  show merona t content
  show cimaria neutral
  "She turned around and crossed one arm over her body."

  show cimaria neutral OM
  ck "They're alright."

  show cimaria neutral
  "She shook the box in her hand."

  play music music_River_Meditation
  show merona t surprised
  show cimaria neutral OM
  ck "Probably going to buy this set of disposable needles."

  show merona t surprised OM
  show cimaria neutral
  mk "Needles? For..."

  show merona t serious
  show cimaria serious OM
  ck "I have some anesthesia that can numb down pain, but I may need more needles since I'm going to be using other liquids as well and need to quickly inject multiple places at once to cover a large area of the body..."

  show cimaria serious
  "Her voice trailed off and she looked to the ground beside her."

  show cimaria neutral OM
  ck "Having more quick, ready-to-use syringes will be a safety net for me in case I break one of my own. It's not likely that I will, but if I need someone else to help me, more is definitely better as well seeing how everyone in our group is not experienced in these tasks."

  show merona t surprised
  show cimaria sadSmile OM
  ck "The next choice would be to either beat Rett unconscious or get him ridiculously drunk. Spending money on all that alcohol would be a waste of our money anyhow, so I was already deciding that I would have to take him down."

  show merona t laugh
  show cimaria sadSmile
  mk "*chuckle* Yeah, those choices aren't exactly ideal. And if you do want to get him drunk, why not get cheap alcohol? He doesn't need to enjoy it."

  show merona t grin
  show cimaria laugh
  ck "Haha, I don't know. Beating Rett up and having him consent to it sounds sort of amusing."

  show cimaria grin
  "She paused and sheepishly grinned."

  show merona t content
  show cimaria content OM
  ck "By the way..."

  play music music_Radio_Martini
  show merona t sadSmile
  show cimaria wink OM
  ck "Don't take any of that seriously."

  show merona t sadSmile OM
  show cimaria gentle
  mk "Ha... Yeah... I know!'"

  show merona t worried
  mi "But if it was going to happen, it would have been... interesting."

  show merona t content
  show cimaria content OM
  ck "So how did your own search go? Find anything?"

  show merona t content OM
  show cimaria content
  mk "Possibly. I found loose leaf yander that seems to be sort of fresh, definitely not very old."

  play music music_She_dreams_in_blue
  show merona t content
  show cimaria neutral OM
  ck "Can you enhance the loose leaf kind?"

  show merona t serious OM
  show cimaria neutral
  mk "If we use it immediately, possibly. It may be difficult for me though, because it's best to find a life flow through the root of a plant. I'll possibly have to get knocked up on my own enhancer to help me become hyper-aware of the flow through the leaf veins."

  show merona t serious
  show cimaria serious
  "Cimaria squinted at me."

  show merona t worried
  show cimaria serious OM
  ck "That... does not sound very good for your health. I advise you not to overdose on those things."

  show merona t worried CE
  show cimaria worried
  "I nodded and held up my palms in surrender."

  show merona t content OM
  show cimaria sadSmile
  mk "I'll heed your words, wise healer."

  show merona t happy
  show cimaria neutral
  mk "I did happen to find some powders though. Yander powder included. If you need to make a serum, maybe you could use that?"

  show merona t content
  show cimaria neutral OM
  ck "Well, I do expect myself to make some serum with yander in it, but a fresh one is optimal. We could take some powder as a backup though. There's a good number of needles in here if we want to use several mixes."

  show merona t serious OM
  show cimaria neutral
  mk "Fresh yander..."

  show merona t serious
  "I pursed my lips and frowned."

  play music music_Swimming_To_Cambodia
  show merona t disappointed OM
  show cimaria worried
  mk "Hey Cimaria, didn't you say that this area had a plentiful amount of it? Shouldn't we be able to find it around here? Judging from the loose leaf ones I saw, it's not that camouflaged-looking."

  show merona t disappointed
  show cimaria worried OM
  ck "*sigh* My thoughts exactly. I don't understand why I couldn't spot them either. Yes, they're not hard to spot all. And yes, this region should have a fair amount of them. More and more things just don't add up..."

  show merona t content OM
  show cimaria worried
  mk "Then... do you want to get some powders or pre-made serums for now? We could buy some supplies for future use too, in case more things happen."

  show merona t content
  show cimaria sadderSmile
  "Cimaria gave a tight-lipped smile and furrowed her eyebrows."

  play music music_River_Meditation
  show merona t worried
  show cimaria sadderSmile OM
  ck "Ha, I have a feeling that more will certainly happen to us... There's bound to be more trouble along the way, so we might as well become broke and spend all of our money trying to help our future injuries before they destroy us. "

  show cimaria worried CE
  "Her face drooped. She closed her eyes and took a deep breath."

  show cimaria neutral CE
  ck "..."

  show merona t sadSmile
  show cimaria neutral OM
  ck "Apologies for being so negative about this. I get rather bitter when I'm confused, and I'm used to venting it out to myself... I know it's not pleasant to listen to me like this."

  show merona t sadSmile OM
  mk "Happens to all of us, Cimaria. I don't blame you."

  show merona t worried
  show cimaria worried
  mi "I can imagine that for her, the notion of Rett's situation is a heavy load in her mind. It seems like his injury is not serious and that everything is fine, but Cimaria can most clearly see that it isn't."

  "The pressure to keep it from truly becoming critical or fatal must be hurting her thoughts."

  show merona t serious
  show cimaria sadSmile
  "She flashed me a weak smile."

  play music music_recollections
  show merona t surprised
  show cimaria sadSmile OM
  ck "You seem to be pretty good at keeping a happy mind. Are you okay? How are you feeling right now?"

  show merona t serious OM
  show cimaria neutral
  mk "Mm, I've got more of a muddled mind than a happy one."

  show merona t disappointed OM
  mk "And it's certainly making me more frustrated than happy."

  show merona t content OM
  mk "But, I do try not to let things jumble up and twist me around inside, so I pay attention to how I'm thinking."

  show merona t content
  show cimaria neutral OM
  ck "It's nice that you can keep a grip on your emotions and deal with them accordingly. It's something you have to become great at as you get older..."

  play music music_life
  show merona t grin
  show cimaria wink OM
  ck "But you're only sixteen. *laugh* Worry more about your grades."

  "She patted me on the back once and smiled."

  show merona t content
  show cimaria content OM
  ck "Why don't you show me to the items you found. We will most likely have to make use of some of them, and if not, still have them as a backup."

  show merona t content OM
  show cimaria neutral
  mk "No problem! Then, are we covered? I can check the time on the clock tower to see if the hour has passed while you pay."

  return
  #-----------------------------------------------
label lbl_PathC_5_8:
  
  #play music music_life #(continue from before)
  #scene cg pharmacy #(from before)
  show merona t content #(pos from before)
  show cimaria neutral OM #(pos from before)
  ck "How about we go together? It won't take long."

  show merona t sadSmile
  show cimaria serious OM
  ck "Not to mention that even though this is a small town, you look rather young and naive... I have the slight feeling that you're going to get mugged or something like that."

  show merona t grin
  show cimaria surprised
  "I waved my hands at her in denial."

  show merona t happy
  show cimaria sadSmile
  mk "It's fine, it's fine! I'm won't even go that far from here, I just need to get to a spot where I can see the face of the clock."

  show merona t determinedGrin OM
  show cimaria content
  mk "And if I were to be mugged, I can put up a fight! Maybe? Sort of. I can at least try to scare the person off by acting delirious. Since I don't carry any money, I'm not technically losing anything!"

  show merona t grin
  show cimaria grin CE
  "Cimaria scoffed and shook her head."

  play music music_piano
  show merona t sadSmile
  show cimaria wink OM
  ck "We're going to pay and leave together. It is settled. No more peeps out of your mouth."

  show merona t sadSmile OM
  show cimaria content
  mk "Okay, haha..."

  show merona t content
  mi "Not gonna argue back with that final statement."

  show cimaria content OM
  ck "Can you show me the things you've found then?"

  play music music_potHappy
  show cimaria neutral
  "I nodded and led her to the area with the loose leaf herbs and assorted powders. She squinted and got close up to observe the innards of the glass bottles. I grabbed some powdered yander from the bottom shelves and fidgeted with them in my hands."

  show merona t content OM
  mk "What do you think of them?"

  show merona t content
  show cimaria worried#, change to cimaria content after a short time
  pause(0.5)
  show cimaria content
  "Cimaria squeezed her lips together and smiled."

  show cimaria content OM
  ck "Like I said before, it'd be best to have fresh yander, but this isn't a bad option either. Let's also take some of the powder as a back up."

  show merona t grin
  show cimaria gentle OM
  ck "Thanks for finding this. I am sure that they'll be of good use."

  show cimaria gentle
  "I beamed back at her."

  show merona t happy
  mk "Oh, you're welcome! Just doing what I was supposed to be doing."

  show merona t content OM
  show cimaria content
  mk "If we have all that we need now, then let's pay up and go."

  show merona t content
  scene bg white with fade
  "She nodded. We went up to the counter, exchanged money with the cashier, and headed out with our items to the spot."

  play music music_Travel_Light
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg townShops
  show merona t serious:
    yalign 1.0
    xalign 0.75
  show cimaria neutral OM:
    yalign 1.0
    xalign 0.25
  ck "How do you think the others did? With their search."

  show merona t surprised
  show cimaria neutral
  "I shrugged my shoulders and crossed my arms."

  show merona t content OM
  mk "If they had good luck, Lexan and Boyen could have found a little yander plant in that herb shop. The others could have found someone to preserve our little friend too."

  show merona t disappointed
  show cimaria serious OM
  ck "And that's if they had good luck. If they had bad luck, they would only find nothing."

  show merona t grin
  show cimaria surprised
  "I snorted and remembered what she warned me about earlier."

  show merona t laugh
  show cimaria abashed
  mk "Nah, if it was really bad luck, they would gotten mugged. I guess they look pretty 'innocent and naive' too..."

  play music music_Dark_Red_Wine
  show merona t grin
  show cimaria grin
  "Cimaria chuckled and playfully punched me."

  show cimaria laugh
  ck "Oh my bad, I accidentally swung my arm into you. Sure hope that didn't damage your fragile monster-clawed shoulder."

  show merona t shocked
  show cimaria grin
  "I screwed up my face in feigned pain and grasped that very shoulder."

  show merona t shocked OM
  mk "I have been broken..."

  show merona t content
  show cimaria content
  "We continued walking along with little smiles dancing on our faces, not concentrating about much else. The swift, fluttering wind was a nice complement to the partly cloudy, partly sunny day."

  show merona t grin
  mi "I'd like to believe that good weather hints of a good future, just as how bad weather warrants bad future events."

  scene bg black with fade
  mi "Does this mean that we'll be met with better things soon?"

  mi "Then again, it's just one of my theories."
  return
  #-----------------------------------------------
label lbl_PathC_5_9:
  
  stop music
  $ renpy.transition(slow_dissolve, layer="master")
  scene black
  pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg_sky1
  show clouds at leftright
  show cg town
  show merona t nervous:#; right:
    yalign 1.0
    xalign 1.0
  show cimaria serious:#; left from Merona:
    yalign 1.0
    xalign 0.75
  show kreita fishAnimated grin:#; center#; use bodyFish and bodyFish2 #(animated please):
    yalign 1.0
    xalign 0.5
  show duran t annoyed:#; left from Kreita:
    yalign 1.0
    xalign 0.3
  show lexan confused:#; left:
    yalign 1.0
    xalign -0.1
  show boyen surprised:#; right from Lexan/ left from Duran:
    yalign 1.0
    xalign 0.1
  mi "I don't believe I've ever had the chance to see old, rotting flesh, but there's a first time for everything."

  play music music_Nincompoop
  mi "Today was my first time."

  show merona t surprised
  show kreita fishAnimated happy
  show duran t annoyed CE
  show lexan neutral
  show boyen sceptical
  kh "We just so happened to chance upon a little meat shop, and they gave us this!"

  show kreita fishAnimated laugh
  show duran t annoyed
  "Kreita stuck out her fistful of decomposing fish, all held by the tails and dangling around in a special party of its own. Duran simply gave her the side-eye."

  show merona t sadSmile
  show cimaria serious OM
  show kreita fishAnimated grin
  show lexan surprised
  ck "And... you accepted it, because...?"

  show merona t surprised
  show cimaria neutral
  show kreita fishAnimated happy
  show lexan sceptical
  kh "We told the people about our thingy, and they recommended us to use dead fish to help fertilize the soil. For free too! It benefited both sides."

  show merona t serious
  show kreita fishAnimated grin2
  mi "I can understand how it'd help for growing in the soil, but we're not growing yander. Or anything at the moment."

  show merona t sadSmile
  show cimaria serious
  show kreita fish pouty
  show duran t angry
  show lexan serious
  show boyen sceptical OM
  bg "It can't be eaten. It's too late for that, even with my magic."

  show merona t sadSmile OM
  show kreita fish sad
  show duran t angry CE
  show boyen sweaty 
  mk "We're also not gonna grow yander... Cimaria and I found the dried versions and some powders as well."

  play music music_Words
  show merona t content OM
  show cimaria neutral
  show kreita fish worried
  show duran t annoyed
  show lexan neutral
  mk "Did the people say it had any other uses though?"

  show merona t disappointed
  show cimaria worried
  show kreita fish sad
  show boyen worried
  "Kreita sulked and crossed her arms, still letting the fish flop in her hand."

  show kreita fish sad OM
  show duran t annoyed CE
  show lexan worried
  kh "Tch, that's unfortunate. Here I was, thinking I was doing something right."

  show kreita fish sad
  show duran t annoyed
  "Rett reached out an arm and patted her shoulder."

  show merona t content
  show cimaria sadSmile
  show kreita fish serious
  show duran t neutral
  show lexan sadSmile
  show boyen neutral
  rt "It's the thought that counts."

  show merona t worried
  show kreita fish serious OM
  show duran t worried
  kh "*sigh* Yeah, I'm sure only thought will help you a lot. But is there really nothing we can do with this? Duran and I spent a good amount of time searching, and this was the best we could muster."

  show merona t serious#; fade out
  show cimaria surprised OM#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide merona
  hide cimaria
  show kreita fish serious
  show duran t neutral
  show lexan neutral OM
  ln "How did Rett and Prowen fare then?"

  show lexan neutral
  $ renpy.transition(slow_dissolve, layer="master")
  show prowen neutral:#; at Merona's former position:
    yalign 1.0
    xalign 1.0
  show rett neutral:#; at Cimaria's former position:
    yalign 1.0
    xalign 0.75
  "Prowen shrugged."

  show prowen neutral OM
  pm "Eh."

  show kreita fish worried
  show lexan worried
  show boyen worried
  pm "Not much better."

  show prowen neutral
  show rett neutral OM
  rt "We tried, but the places we looked into were only dealing with butchering and things like that."

  play music music_Radio_Martini
  show prowen serious
  show rett neutral
  "Prowen's face shifted, and he straightened up."

  show kreita fish neutral
  show duran t surprised
  show lexan surprised
  show boyen content
  show prowen serious OM
  show rett surprised
  pm "We did get something."

  show duran t neutral
  show lexan content
  show prowen neutral OM
  show rett confused
  pm "Got tips for preservation."

  show lexan confused
  show boyen neutral
  show prowen sceptical
  show rett confused OM
  rt "Tips for preservation? What are you talking about?"

  show kreita fish sceptical
  show duran t annoyed
  show boyen sceptical
  show prowen sceptical OM
  show rett confused
  pm "You don't remember?"

  play music music_Travel_Light
  show lexan neutral
  show boyen worried
  show prowen neutral OM
  show rett worried
  pm "Maybe you zoned out while he told us. Or were focusing on something else."

  show kreita fish neutral
  show prowen neutral
  show rett pouty
  "Rett frowned and looked up, as if he was trying to search for the tips in his mind."

  show kreita fish worried
  show rett neutral OM
  rt "I guess I did. I was thinking a lot about what we could do, so stuff may have slipped out of my mind."

  return
  #-----------------------------------------------
  
  
  #-----------------------------------------------
  # CHAPTER 6
  #-----------------------------------------------
label lbl_PathC_6_0_1:
  

  play music music_Travel_Light #(continue from before)
  #scene cg town #(from before)
  #TODO [Positions as in C5.9...
  show rett neutral#; left from Prowen
  show prowen neutral#; right
  show kreita fishAnimated neutral#; center#; use bodyFish and bodyFish2 #(animated please)
  show duran t neutral#; left from Kreita
  show lexan serious OM#; left
  show boyen neutral#; right from Lexan/ left from Duran

  ln "Nonetheless, what were the tips, Prowen?"

  show prowen neutral OM
  pm "Uh..."
  return
  #-----------------------------------------------
label lbl_PathC_6_0_o:
  
  ##OPTIONAL##"
  #TODO [ATTENTION! The sprite positions will be different here than in the B path #(to fit the earlier dialogues better)
  show lexan surprised
  show boyen content
  show kreita fishAnimated grin
  show duran t surprised
  show prowen surprised
  show rett grin at RightBump#; move his sprite a bit towards Prowen's and then back to the initial position
  "Rett chuckled and slapped Prowen on the back."

  show lexan confused
  show kreita fish grin2
  show duran t annoyed
  show prowen forcedSmile
  show rett laugh ER
  rt "*laugh* Now if he forgot about them too, that'd be funny."

  show lexan neutral
  show prowen forcedSmile CE
  show rett grin
  "Prowen shook his head and closed his eyes for a moment."

  show kreita fish content
  show prowen neutral OM
  show rett smirk
  pm "Don't worry, I remember."

  show lexan serious
  show boyen neutral
  show duran t neutral
  show prowen sceptical OM
  show rett neutral
  pm "The guy gave a number of methods, but some of them may not work out well for us."

  pm "For example, a lot of them involved cutting the meat into slabs."

  show lexan annoyed
  show boyen happy
  show kreita fish grin
  show duran t annoyed CE
  show prowen appalled
  show rett grin S
  bg "If we were eating the monster, that'd be good. In fact, if it comes down to us needing to eat it, we could-"

  show lexan serious
  show duran t annoyed
  show prowen appalled OM
  show boyen happy S
  pm "-Um, moving on..."

  show prowen sceptical
  show kreita fish content
  show rett neutral
  show boyen worried
  "Boyen held up his palms."


  show lexan serious CE
  show duran t annoyed EL
  show prowen annoyed
  show rett grin CE S
  show boyen worried OM:#; move to the left while fading sprite out
    yalign 1.0
    linear 10.0 xalign -1.0 
  pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")  
  hide boyen
  bg "Sorry, I'll stop talking now."

  show lexan serious
  show duran t neutral
  show prowen sceptical OM
  show rett neutral
  pm "So, all of his advice revolved around preserving meat when it's cut into smaller pieces."

  show kreita fish neutral
  show prowen sceptical OM
  pm "There's no mention of it being applicable to the animal-or monster in our case-when it's whole."

  show prowen neutral
  pm "..."

  show lexan determined
  show kreita fish fierce
  show prowen determined OM
  show rett content
  pm "We could still try it though."

  show kreita fish content
  show prowen neutral
  "He finished but quickly jumped back in."

  #(slightly more urgent voice)
  show lexan surprised
  show kreita fish neutral
  show prowen determined OM
  show rett surprised
  pm "I've tried storing meat on my own a long, long time ago. But that was for typical meats, so I didn't think of doing the same thing for this situation."

  show lexan worried
  show prowen determined
  mi "This is probably the most that I've heard Prowen say all at once. He's onto something good... I want to keep poking him for more info, but he would probably get annoyed back into saying very little."

  show lexan worried OM
  show kreita fish content
  show duran t surprised
  show prowen content
  show rett content
  ln "*sigh* I mean, it's better than nothing. And if you've already got experience with any kind of preservation of that sort, then we should gladly accept it. Thank you for informing us."

  show lexan neutral
  show duran t annoyed
  show prowen neutral
  "Duran crossed his arms and frowned, turning into an officer waiting for the witness to provide more information."

  show duran t annoyed OM
  show rett neutral
  dt "Okay, but... You still haven't told us exactly what to do. Care to share?"

  show lexan surprised
  show kreita fish grin
  show duran t surprised
  show prowen neutral OM
  show rett surprised
  pm "Salt the monster."

  show lexan sceptical
  show duran t surprised
  show prowen neutral
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria serious OM:#; fade in at Boyen's former position #(right from Lexan/ left from Duran)
    yalign 1.0
    xalign 0.2
  ck "That's all? Just put salt on it?"

  show kreita fish content
  show duran t surprised
  show cimaria serious
  show rett grin
  "Prowen nodded and looked to the side."

  show lexan content
  show duran t content
  show prowen content OM
  pm "Yes. And since we're not going to be eating it, there's more flexibility on how much salt to put in and for how long."

  show duran t neutral
  show prowen determined OM
  pm "Even better, this monster is holding up much better than a regular animal carcass, so it should be able to be preserved for a long time."

  show cimaria sadSmile
  show prowen determined
  show rett content
  "The overcast sky that had been looming on Cimaria's face had brightened into a partially sunny one."

  show kreita fish grin2
  show cimaria sadSmile OM
  show prowen content
  ck "Wow, that's a good tip. In fact, that's probably good enough that we don't need to actively search for another alternative. We should use this technique as soon as possible."

  show lexan surprised
  show kreita fish content
  show cimaria neutral
  show prowen content OM
  pm "We'll need more salt, so I'll run out and buy more. Should be pretty easy to find."

  show lexan neutral
  show prowen neutral#; fade out his sprite
  $ renpy.transition(slow_dissolve, layer="master")
  hide prowen
  "Before anyone could reply, he strolled down to the nearby street of shops."

  $ renpy.transition(slow_dissolve, layer="master")
  show merona t reflective:#; fade in at Prowen's former position #(right)
    yalign 1.0
    xalign 1.0
  
  mi "Would they sell salt by the bulk in this kind of town? I mean, usually you'd expect to find large quantities of spices available for purchase in port cities, so a place like this wouldn't sell a big amount."

  show merona t reflective CE
  mi "Maybe we'll have to buy dozens upon dozens of salt packets."
  ## OPTIONAL END ##"
  return
  #-----------------------------------------------
label lbl_PathC_6_0_2:
  
  play music music_Travel_Light
  show merona t content
  show cimaria content OM
  show kreita fish determined
  show rett smirk
  show lexan content
  ck "Okay. Good, so far we can start preserving the monster, we have dried yander, powders, and questionable dead fish."

  show boyen grin:
    yalign 1.0
    xalign -0.2
  $ renpy.transition(slow_dissolve, layer="master")
  show boyen grin:#; left #(move into screen from outside)#; also please move Lexan slightly more to the right once Boyen becomes visible~
    yalign 1.0
    linear 5 xalign 0.05
  show merona t surprised
  show cimaria surprised
  show duran t annoyed
  "Boyen bobbled up and down, jiggling in his jolly fashion."

  $ renpy.transition(slow_dissolve, layer="master")
  show boyen happy:
    yalign 1.0
    xalign 0.05
  show merona t content
  show cimaria content
  show kreita fish content
  show rett content
  show lexan sadSmile
  show duran t neutral
  bg "Oh! Lexan and I couldn't find anything yander-related, but we did get more supplements and enhancers that could help with strengthening the plant itself."

  show boyen content
  show lexan sadSmile OM
  ln "We... were sort of banking on someone else finding yander, ha ha. So that's the best we did."

  show boyen grin
  show merona t content OM
  show cimaria gentle
  show kreita fish grin2
  show rett grin
  show lexan content
  mk "Cimaria and I kind of found yander! I might be able to use enhancers on the dried versions, since it still has its properties in it... May not be as strong, but it might turn out helpful. Thanks though!"

  play music music_Cool_Steel_Breeze
  show merona t content
  show kreita fish content
  show rett content
  show lexan content OM
  ln "Looks like we're all covered now. And no need for Merona to do that little group swap we planned beforehand too."

  show boyen neutral
  show cimaria neutral
  show kreita fish pouty
  show rett neutral
  show lexan neutral
  "Kreita's face became overcast in turn after the clouds had passed from Cimaria's."

  show boyen sweaty
  show merona t serious
  show cimaria sadSmile
  show kreita fish pouty OM
  show duran t tired
  kh "I guess we'll just forget about my fish... Might as well donate it to the local forest's soil. Make the trees happy."

  show merona t reflective
  show kreita fish pouty
  mi "The trees certainly would be happy over that, but I think we should still keep it! If we end up bumping into yander along the way, or yander sprouts, we could cultivate them on our own. "

  show merona t sadSmile
  mi "Sorry trees, but life isn't always fair, and humans have to take your potential fertilizer for their own sake."

  play music music_Radio_Martini
  show merona t grin
  "I beamed at Kreita."

  show boyen neutral
  show merona t happy
  show kreita fish neutral
  show cimaria surprised
  show rett smirk
  show lexan surprised
  show duran t surprised
  mk "Let's keep it!"

  show boyen content
  show merona t content OM
  show kreita fish content
  show cimaria neutral
  show lexan content
  show duran t annoyed
  mk "I think we'd be better off having the fish. We already have soil for my studies, and if we collect the local soil, we can keep it prepared in case we find yander around here. It'd take no extra space."

  show merona t serious
  show kreita fish grin
  show rett grin
  show duran t annoyed OM
  dt "Technically, it would take extra spa-"

  show merona t determined
  show duran t angry
  "I hovered my hand in front of Duran and kept my eyes on Kreita."

  show boyen grin
  show merona t determinedGrin OM
  show kreita fish content
  show cimaria content
  show lexan grin
  show duran t annoyed
  mk "Shhhhh... Let's keep it."

  show merona t grin
  show kreita fish neutral
  show lexan content
  show rett content OM
  show duran t neutral
  rt "I agree, Kreita. If it can be used, let's use it."

  show merona t content
  show kreita fish worried
  show rett content
  "She looked at Rett and I with a blank face, and played around with the thought in her mind and the fish in her hand."

  show kreita fish worried OM
  kh "If no one else protests against it..."

  show kreita fish worried
  "Kreita eyed all of us, waiting for any sign or sound of disapproval."

  show boyen grin CE
  show merona t grin
  show kreita fish content OM
  show rett smirk
  show lexan content CE
  kh "...Then, okay!"

  show boyen content
  show kreita fish content CE
  show rett content
  show lexan content
  "Kreita kept her eyes downcast but still smiled to herself."
  return
  #-----------------------------------------------
label lbl_PathC_6_1:
  
  #play music music_Radio_Martini #(continue from before)
  #scene cg town #(from before)
  #TODO [Positions as in C6.0...

  show boyen content
  show merona t happy
  show kreita fish content
  show rett smirk
  show lexan content
  show duran t neutral
  mk "Hooray! We're good for now. Just have to wait for Prowen to come back."

  play music music_eerie
  show boyen sceptical
  show merona t surprised
  show kreita fish sceptical
  show rett confused
  show lexan confused
  show duran t surprised OM
  dt "Hm... What if he never comes back?"

  show merona t nervous
  show duran t neutral
  show cimaria serious
  "Cimaria squinted at Duran."

  show rett sceptical
  show cimaria serious OM
  ck "Never come back? What do you mean? Did he say something to you?"

  show merona t surprised
  show kreita fish worried
  show rett sceptical OM
  show lexan serious
  rt "What could he be planning? Don't tell me he was all along a deranged lunatic who broke out of prison."

  show boyen scared OM
  show merona t worried
  show rett sceptical
  show duran t neutral
  bg "Have I been feeding a criminal this whole time? Does that make me an accomplice?!"

  play music music_Pilot_Error
  show boyen serious
  show merona t serious
  show kreita fish neutral
  show rett neutral
  show lexan neutral
  show duran t annoyed
  "Duran scoffed at all of us, and you could see the disgust floating over his face like the moon against a night sky."

  show duran t annoyed OM
  dt "Wow people, you guys sure can get your pants in a bunch."

  show boyen neutral
  show merona t sadSmile
  show kreita fish grin
  show rett surprised
  show lexan annoyed
  show duran t neutral OM
  dt "I was just joking about Prowen since he left so quickly. Calm yourselves down and drink a cup of tea or whatever."

  play music music_White
  show boyen surprised
  show merona t sadSmile OM
  show kreita fish worried
  show rett sceptical
  show lexan surprised
  show duran t surprised
  mk "I mean, what if he actually never comes back? What if he got sick of our shenanigans and used the salt as an excuse to go?"

  show boyen worried
  show merona t worried OM
  show rett neutral
  show duran t worried
  mk "Does he even have enough money with him to buy stuff? And would he be so willing to help us out like that?"

  show merona t worried
  show lexan neutral
  show duran t neutral
  mi "Oh my... Prowen seemed quite casual when we first literally bumped into him a few weeks ago, but maybe he was hiding something. Maybe he has secret plans that are being carried out right as we stand here."

  show merona t reflective
  mi "You know, I'm starting to wonder why I didn't think about all this when we were debating whether to take him in or not."

  show merona t shocked
  mi "Did the others consider these factors too? If they didn't... Well, we could be screwed."

  show merona t serious CE
  mi "Emphasis on \"could\". It's only a theory..."

  play music music_recollections
  show boyen neutral
  show merona t serious
  show kreita fish neutral
  show rett smirk
  show lexan sadSmile
  show cimaria content OM
  ck "Slow down there, Merona. I'm sure Prowen is doing what he said, and I wouldn't worry about it. We've been with him for a while, and he seems like a decent person."

  show boyen grin
  show merona t content
  show kreita fish content
  show duran t smirk
  ck "As Duran would say, 'don't get your pants in a bunch'."

  show lexan neutral
  show duran t smirk CE
  show cimaria content
  "Duran saluted her, and Cimaria continued speaking."

  show merona t grin
  show duran t neutral
  show cimaria neutral OM
  ck "It hasn't even been ten minutes since he left. We're all probably a bit high strung from these issues nipping at us recently, so let's stop overthinking everything."

  play music music_Radio_Martini
  show boyen content
  show merona t surprised
  show kreita fishAnimated grin#; use Kreita bodyFish with its animation
  show rett smirk behind kreita
  show cimaria content
  "Kreita wiggled her fish."

  show merona t content
  show kreita fish laugh
  show rett content
  show lexan content
  show duran t annoyed
  kh "Yeah... I think we all need a break. Let's all have a mini relaxation session as we wait for Prowen to return."

  show merona t content OM
  #TODO [Stop Kreita bodyFish animation
  show kreita grin
  mk "That sounds nice. What do you do in mini relaxation sessions?"

  show merona t content
  show kreita happy
  show duran t neutral
  kh "Oh you know... relax. But really, do whatever you can to simmer down. Close your eyes, don't move, pace around, look at the sky, be one with nature, and so on."

  show kreita content OM
  kh "When I'm hunting, being calm is key to honing in your focus and insuring the most precise shot you can get at slaying the creature. Fun fact of the day."

  play music music_piano
  show kreita neutral
  show rett neutral
  show lexan neutral
  show duran t bored
  "Everyone glanced at each other, trying to find someone to emulate in this activity, but the only thing we accomplished was not-so-subtly staring around for ten seconds. Ten whole seconds."

  show boyen neutral
  show merona t serious
  show kreita pouty
  mi "We've been \"relaxing\" for quite a long time it feels... I don't know what else to do."

  kh "..."

  play music music_Cool_Steel_Breeze
  show boyen surprised
  show merona t surprised
  show kreita fishAnimated grin#; use Kreita bodyFish with its animation
  show rett surprised
  show lexan surprised
  show duran t surprised
  "Kreita flopped her fish left and right."

  show boyen content
  show merona t grin
  show kreita fishAnimated fierce OM
  show rett smirk
  show lexan grin
  show duran t neutral
  kh "You know, we should try another thing. Never mind what I said. How about going over our plan again."

  show kreita fierce#; Stop Kreita bodyFish animation
  show rett laugh S
  show lexan content
  rt "Yes... I guess that was kind of relaxing...-ish."

  show merona t content
  show kreita content
  show rett content
  show lexan content OM
  ln "As for our plan, we are going to try out the dried yander, powdered yander for serums, use the fish to fertilize, use the new enhancers, and attempt preserving the monster with salt."

  show boyen grin
  show lexan happy OM
  ln "If all goes well, we will be dandy again. Did I miss anything?"

  show lexan content
  show duran t neutral OM
  dt "Sounds plausible."

  show boyen content
  show duran t smirk OM
  dt "Then again I'm not always fully focused on one thing, so I could have missed out on a detail."

  show merona t content OM
  show duran t neutral
  mk "I'm pretty sure that's the entire general plan. We've hit the points we were aiming for, so that's commendable! Once we get the salt, we should be ready to go, yeah?"

  show merona t grin
  show kreita grin2
  show rett smirk
  show lexan content OM
  ln "And speaking of salt, here comes our resident salt-man right this moment."
  return
  #-----------------------------------------------
label lbl_PathC_6_2:
  
  play music music_recollections
  #scene cg town #(from before)
  #TODO [Positions as in C6.0...

  show boyen content
  show merona t grin:
    yalign 1.0
    xalign 0.9
  show kreita grin2
  show rett smirk
  show lexan content
  show duran t neutral

  $ renpy.transition(slow_dissolve, layer="master")
  show prowen neutral OM:#, at a free spot - if possible at the edge of the screen #(I lost track of where they all stand, sorry...)
    yalign 1.0
    xalign 1.1
  pm "I'm back."

  show prowen neutral
  "Prowen indeed was the resident salt-man at this moment. He hung a medium sized bag, looking three quarters full of salt, on his forearm like it was a thick towel. Duran frowned."

  show boyen grin
  show merona t surprised
  show kreita content
  show rett neutral
  show lexan neutral
  show duran t surprised OM
  dt "Do they really sell that much salt to normal people? I know some people really like all their food to be super salty, but an entire bag is only worth it for some kind of restaurant or organization."

  show merona t content OM
  show duran t neutral
  mk "It's not like salt can go bad. Maybe they want to stock up since buying it in a bulk size is cheaper. Then again, I wouldn't consider this country's cuisine to be quite salty..."

  show boyen content
  show merona t content
  show prowen surprised
  "Prowen shrugged and looked at the bag."

  show prowen neutral OM
  pm "Eh. I asked the shopkeeper for their largest size, and he gave me this. The only other sizing option they had were only good for a few times use."

  play music music_potHappy
  show boyen grin
  show merona t grin
  show kreita grin
  show rett content
  show lexan content
  show duran t content OM
  show prowen neutral
  dt "On the bright size, we could dry and smoke some tasty meat with that salt. I've been craving some animal flesh lately, and I bet we could catch a deer or rabbit no problem."

  show boyen happy2
  show lexan grin
  show duran t grin
  show prowen content
  bg "Our food has been a bit bland overall, so this salt could pack a good punch of flavor!"

  show boyen grin
  show prowen content OM
  pm "Do whatever you want. Just save enough to preserve the monster."

  show boyen content
  show merona t content
  show kreita content
  show rett neutral
  show lexan content
  show duran t neutral
  show prowen neutral
  show cimaria content OM
  ck "Thank you for getting this, Prowen. So with that, we should be totally prepared to depart, yes? Unless anyone wishes to stay here while we're near a town and begin using our newfound items, I suggest moving further along and settling down there. We must keep forging ahead, after all."

  show rett neutral OM
  show cimaria neutral
  rt "I mean, there really isn't any other point to stay here anymore. We've got all the supplies that we need, and we have a destination to get to."

  play music music_Ill_be_right_behind_you_Josephine
  show boyen worried
  show merona t serious
  show kreita worried
  show rett sadSmile OM
  show lexan neutral
  show duran t worried
  show prowen serious
  rt "Speaking of destination, this journey was one to help Merona and Duran out with their studies and ability, so don't forget that it's about them! Not me. I think I can tell when my body is heavily affected, so if something comes up, I'll just let you all know."

  show merona t worried
  show kreita worried OM
  show rett worried
  show lexan worried
  kh "Rett, don't downplay your injury too much. You got bit by a monster! A small, fish-like monster, but nonetheless, it was a monster that injected you with questionable, unknown venom."

  show boyen content
  show merona t sadSmile
  show kreita content OM
  show rett neutral
  show lexan determined
  show duran t smirk
  show prowen sadSmile
  kh "The well being of you and the rest of us are just as important as our two fellow young cuties! So while we focus in on them, don't shy away from getting some attention if needed."

  show merona t surprised
  show kreita fierce
  show duran t surprised
  show prowen neutral
  "Like a disciplinarian, Kreita turned herself to exaggeratedly wag her finger and wink at Duran and I."

  play music music_Dark_Red_Wine
  show boyen grin
  show merona t grin
  show kreita fierce OM
  show rett smirk
  show lexan grin
  show duran t annoyed
  show prowen grin
  kh "And don't think that you two rascals can get away with skimping out on your work! Now it's time to work just as hard or even harder!"

  show merona t shocked OM
  show kreita grin
  "I gasped and fluttered my eyelashes, acting along as the offended, lazy student. Duran on the other hand scoffed and refused to take on his role."

  show boyen neutral
  show merona t serious
  show kreita content
  show rett neutral
  show lexan neutral
  show duran t angry OM
  show prowen neutral
  dt "Don't put me in the same category as her. I'm only here because the headmaster just flung me right into this little crew for the vague reason of 'advancing my ability'. How advanced does she want me to get when I'm already at the top of the fire abilities already?"
  return
  #-----------------------------------------------
label lbl_PathC_6_3:
  
  #play music music_Dark_Red_Wine #(continue from before)
  #scene cg town #(from before)
  #TODO [Positions as in C6.0...

  show boyen neutral
  show merona t nervous
  show kreita grin2 S
  show rett neutral
  show lexan strict OM
  show duran t angry
  show prowen neutral
  ln "Let's just move on now and get going. We have got quite a bit of things on our plate, and it would be best to start doing these tasks right away..."

  show merona t serious
  show kreita content
  show lexan neutral
  show duran t annoyed
  show prowen forcedSmile OM
  pm "I'll put this in the cart."

  $ renpy.transition(slow_dissolve, layer="master")
  show prowen neutral: #next to cart
    yalign 1.0
    xalign 0.75
  show wagon behind prowen
  "Prowen swung the bag of salt on top of some crates and leaned against the side of the wagon."

  show boyen content
  show merona t content
  show rett smirk
  show lexan sadSmile
  show duran t neutral
  $ renpy.transition(slow_dissolve, layer="master")
  show prowen content OM:# at former position
    yalign 1.0
    xalign 1.1
  pm "Now we're ready."

  play music music_Radio_Martini
  show kreita grin#; use Kreita body again instead of Kreita bodyFish
  show lexan neutral
  show prowen content
  "Kreita hopped over there as well and settled her fish in a partially filled crate."

  show merona t sadSmile
  show kreita laugh
  show rett grin
  show lexan grin
  show prowen neutral
  kh "Hope you guys don't mind the temporary, fishy smell that'll be over this stuff... We're gonna have to use up the fish soon, so let's let them settle here until our next stop."

  show boyen happy
  show kreita grin2
  bg "I mean, we all don't bathe as often as we're used to, so we already are fine and don't notice our own cloud of odors..."

  show boyen grin
  show merona t grin
  show kreita content
  show rett laugh
  show lexan neutral
  rt "Okay, we get it! Let's just go."

  show boyen content
  show merona t content
  show kreita content OM
  show rett content
  kh "I'll man the cart then."

  show kreita content
  show lexan neutral OM
  ln "Are we settled?"

  #TODO [start walking animations
  
  $ renpy.transition(slow_dissolve, layer="master")
  
  show cimaria content at WalkBounce
  show duran t neutral at WalkBounce
  show prowen neutral at WalkBounce
  show rett laugh at WalkBounce
  show merona t content at WalkBounce
  show kreita content at WalkBounce
  show boyen neutral at WalkBounce
  show lexan neutral at WalkBounce
  "Kreita started pushing the cart ahead, and we slowly followed suit. Lexan nodded."

  show merona t grin
  show rett smirk
  show lexan sadSmile OM
  ln "I guess we are."

  show merona t content
  show lexan content
  "We picked up to a faster pace, leaving the town and going into the forest once more."

  scene bg black with fade
  return
  #-----------------------------------------------
label lbl_PathC_6_4:
  
  play music music_SoT
  #TODO [fade in CG forest24
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest24
  show merona t content:#; a bit left from center
    yalign 1.0
    xalign 0.4
  show merona t content at walkBounce
  mi "Ah, back on the road. I wonder if we'll bump into more civilization soon, but then again, the town was the first one we went into."

  show merona t sadSmile
  mi "Technically, we are avoiding going through those places since we don't have enough money to stay at any inns. I guess we'll be hanging out with the trees even more."

  show merona t content
  "As we strolled on, I felt like the air had lightened a little. There was tension stuck around us before, tugging at the knots in our shoulders and controlling us like marionettes. Now the strings have slackened, and we're carrying ourselves once more."

  show merona t reflective
  mi "I shouldn't relax too much though. I still need to think about how to use the dried yander, how to make the serums, fish fertilization, and so on..."

  show merona t worried
  mi "There's also the monster to worry about! Yep, our special fish friend is still safe and snug with me."

  show merona t determined
  "I should discuss this stuff while we're walking. It'd be good to plan it out right away, so how about I go to Cimaria first? We're going to be working together, after all."

  show merona t surprised OM
  mk "Cim-"

  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria serious OM:#; left from Merona
    yalign 1.0
    xalign 0.3
  show lexan serious:#; left from Cimaria
    yalign 1.0
    xalign 0.15
  show rett worried:#; left from Lexan
    yalign 1.0
    xalign -0.1
  show merona t serious
  "I stopped myself from calling out her full name. She was already speaking to Lexan and Rett, and they all had tense faces. I didn't want to interrupt them."

  #TODO [fade out Cimaria, Lexan and Rett
  $ renpy.transition(slow_dissolve, layer="master")
  hide cimaria
  hide lexan
  hide rett
  show merona t disappointed
  mi "I should've noticed that earlier. Well, if I wasn't going to talk to Cimaria, I'd try speaking to Lexan about the enhancers or Rett about the venom and his bites. I'll let them deal with whatever they're chatting about, but who else is there?"

  $ renpy.transition(slow_dissolve, layer="master")
  show duran t neutral:#; right from Merona
    yalign 1.0
    xalign 0.6
  show kreita neutral OM:#; right from Duran
    yalign 1.0
    xalign 0.8
  show boyen content:#; right from Kreita
    yalign 1.0
    xalign 1.0
  show wagon:#; at Kreita's position
    yalign 1.0
    xalign 1.0
  show merona t serious
  "I glanced ahead, only to find that Kreita was also occupied with Duran and Boyen walking next to her and the cart. One other person wasn't involved in any of these conversations though."

  play music music_Sugar_On_My_Tongue
  #TODO [fade out Duran, Kreita, Boyen and the wagon
  $ renpy.transition(slow_dissolve, layer="master")
  hide duran
  hide kreita
  hide boyen
  hide wagon
  show prowen neutral:#; a bit right from center
    yalign 1.0
    xalign 0.75
    
  show prowen at walkBounce
  "Sure enough, Prowen was-as usual-going solo behind us all."

  show merona t surprised
  mi "I've only spoken to Prowen personally once or twice, I believe. He should be useful to talk to about the plans!"

  show prowen serious
  show merona t serious
  "I slowed down and waited for him to catch up to me. The wrinkles under Prowen's eyes deepened as he looked down at me."

  show prowen serious OM
  pm "Do you... need something?"

  show prowen serious
  show merona t content
  "I smiled and nodded."

  show prowen surprised
  show merona t content OM
  mk "Kind of. Just wanted possible help from you about what we're doing and everything."

  return
  #-----------------------------------------------
label lbl_PathC_6_5:
  
  #play music music_Sugar_On_My_Tongue #(continue from before)
  show cg forest24 #(from before)
  show merona t content#; a bit left from center #(as before)
  show prowen neutral OM#;  a bit right from center #(as before)
  pm "Alright. How can I help?"

  show merona t surprised OM
  show prowen neutral
  mk "Well... could you tell me more about how to properly preserve the monster?"

  play music music_recollections
  show merona t grin
  mi "I probably won't be handling preserving it, but you never know! Not to mention that Prowen seems more familiar with the process than the others."

  show merona t serious
  show prowen neutral OM
  pm "It isn't difficult-the way we're doing it is pretty simple actually, since we're not aiming to consume the creature."

  show prowen serious
  "He pursed his lips as he crossed his arms."

  show merona t surprised
  show prowen neutral OM
  pm "We might cut some slits into the monster, but salting it whole could work as well. That's all it is."

  show merona t happy
  show prowen neutral
  mk "Oh, that really is easy. Nice."

  show merona t serious
  mk "..."

  show merona t serious OM
  mk "Prowen, can I ask you more on the stuff we're going to do?"

  stop music fadeout 1.0
  show merona t disappointed
  show prowen annoyed
  "Prowen frowned, and he stared at me with an unreadable expression."

  mi "Uh oh. Is he annoyed already?"

  play music music_White
  show merona t serious
  show prowen annoyed OM
  pm "I don't think I can help you that much with the other things. I'm not familiar in how the plant magic works. You should talk to Lexan or Cimaria about that, instead."

  show merona t sadSmile OM
  show prowen neutral
  mk "Yeah, I totally get it! I wanted to talk to them about it at first, but they're kind of busy with each other right now, so that's why I'm here with you at the moment."

  show merona t serious OM
  mk "I can speak to them later about the plans, I suppose. Since we're already in a conversation currently though, can you tell me more about preserving or even just monsters? I feel like you know a lot about them."

  show merona t surprised
  show prowen tired
  "He shrugged but nodded at the same time."

  show merona t grin
  show prowen tired OM
  pm "I guess that's fine. You're expecting a little too much from me though... I'm no expert at these topics. I only know what I know from living in the streets."

  show prowen tired
  mi "That sounds like a lot more knowledge than the rest of us!"

  show merona t laugh
  show prowen neutral
  mk "*laugh* Don't worry, I'm not going to ask about anything really specific. But since you said that you've lived on the streets, what kind of experiences have you had?"

  play music music_Under_the_Stairs
  show merona t serious
  show prowen serious
  "He paused and looked up, gathering his thoughts. I imagined that he was in his mind digging through a whole archive of predicaments that he has faced. Must have been a brain crowded with tons of exciting situations, so he was having trouble picking which one to retell."

  pm "Hm..."

  show merona t grin
  "I grinned, looking up at him."

  show merona t happy
  show prowen neutral
  mk "The tension of waiting is firing me up."

  show merona t grin
  show prowen forcedSmile
  "He scoffed, looking back down at me."

  show merona t surprised
  show prowen forcedSmile OM
  pm "Better blow out the flame in that case, because I don't think there's anything really worthwhile to say."

  play music music_meronatheme
  show merona t disappointed
  show prowen neutral
  "I made an exaggerated scowl and huffed, bringing out my inner actress."

  show merona t disappointed OM
  mk "Really? Ah man, and you got my hopes up. I hope you're satisfied now."

  show merona t grin CE
  show prowen serious
  "My facade quickly dropped, and I giggled to myself."

  show merona t happy
  mk "Sorry, I couldn't help but do that. No worries! Even if isn't all that thrilling, what would you say was the most dangerous thing to happen to you before?"

  play music music_Swimming_To_Cambodia
  show merona t serious
  show prowen serious OM
  pm "Uh... I'm sure that some bad events happened when I was younger, in my teens or early twenties, but I can't recall them. Must have blocked them out of me or something like that."

  show merona t surprised
  show prowen surprised OM
  pm "As for something more recent... Almost getting trampled by a wild boar near the borders of this country was quite a lively situation, to say the least.'"

  show merona t serious
  show prowen serious CE
  "He shook his head and sighed."

  show merona t sadSmile
  show prowen sceptical OM
  pm "I can't really offer much on monsters though, because I haven't had an encounter with them until I joined your group. Thankfully, I must add."

  show merona t content
  show prowen serious OM
  pm "Was that a suitable answer for you?"

  play music music_life
  show merona t grin
  show prowen serious
  "I clapped my hands together. My animated eyes were enough to show my excitement."

  show merona t happy
  mk "Wow, a wild boar does sound exhilarating! You must have had an interesting life so far, and you're lucky that it's been mostly monster-free, especially considering more and more sightings of them. Thanks for telling me a little bit about yourself!"

  show merona t content
  show prowen serious OM
  pm "No problem... And by the way, I think Cimaria and Lexan are free right now."

  show merona t serious
  show prowen serious
  "Sure enough, the two were finished talking to Rett and walking at their own pace. Cimaria was recording something in her little pocket notebook, and Lexan was reading a general flora and fauna book."
  
  show merona t reflective
  mi "They still seem rather preoccupied... I think I'll wait a little more before going to them."

  play music music_Ill_be_right_behind_you_Josephine
  show merona t worried
  mi "But if Prowen told me that they're available now, maybe it's because he doesn't want to talk anymore. Completely understandable I suppose, seeing how I made him tell me about his past traumas."

  show merona t surprised
  show prowen appalled#; after a short time fade to CS prowen serious again
  "When I glanced at Prowen, he quickly flicked his own eyes away from me and back to Lexan and Cimaria's area. "

  show merona t serious
  "He had a strange, concentrated look on his face for that brief fraction of a second that we held eye contact. It was a very focused expression, but I could almost swear that he looked frustrated."

  mi "Wait..."

  play music music_Under_the_Stairs
  show merona t disappointed
  mi "Don't tell me that I brought back something in Prowen's past that he didn't want to remember."

  show merona t nervous
  mi "He did say that he doesn't remember what happened when he was younger, but maybe he actually did and didn't want to mention it. Maybe it was something quite serious."

  show merona t disappointed CE
  mi "Gosh, I feel like a jerk now."

  show merona t worried OM
  mk "Uh, Pro-"

  show merona t worried
  show prowen serious OM
  pm "You can go to Cimaria and Lexan now. They can help you better than I can."

  show prowen serious
  "His face seemed a little more sunken now, like more shadows had been cast across his eyes."

  show merona t determined
  mi "I think I actually am a jerk."

  play music music_She_dreams_in_blue
  show merona t sadSmile OM
  show prowen tired
  mk "Okay, I'll go talk to them then."

  show merona t sadSmile
  "I started walking ahead to the two, but I turned around to wave at Prowen."

  show merona t sadSmile OM
  show prowen forcedSmile
  mk "Thanks again! I really appreciate the stuff you told me."

  show merona t worried
  show prowen serious
  "He nodded, but his face still looked a bit ashen. As I walked over to Cimaria and Lexan, I wondered what it was that had happened to Prowen."

  mi "Hopefully he's okay... And if I really did bring back unwanted memories, I'm sure that they'll pass over him quickly."

  show merona t serious
  mi "Memories are weird like that. Sometimes they linger and feel like they're never going to leave, but sometimes you just forget that they were ever there."

  scene bg black with fade
  return
  #-----------------------------------------------
label lbl_PathC_6_6:
  # C6.6 missing?
  return
  #-----------------------------------------------
label lbl_PathC_6_8:
  
  play music music_Cool_Steel_Breeze
  show cg forest25 #(from before)
  #TODO [walking animations please #(except for the wagon)

  show kreita content#; center
  show wagon#; #(in front of Kreita)
  show merona t content OM#; left
  show lexan content#; left from Merona
  show duran t tired#; right from Kreita
  show rett smirk#; right from Duran
  mk "The monster is in fair shape. The salt's been doing its job nicely."

  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria content OM behind kreita:
    yalign 1.0
    xalign 0.41
  show cimaria content OM at walkBounce
  show merona t content
  show rett neutral
  ck "That's good to hear. Do we have to treat the monster every so often? I imagine its moisture may be taken out."

  $ renpy.transition(slow_dissolve, layer="master")
  show prowen neutral behind wagon:#; left from Cimaria
    yalign 1.0
    xalign -0.14
  show prowen neutral at walkBounce
  show cimaria neutral
  show merona t serious
  show lexan neutral
  "Prowen cleared his throat."

  show prowen neutral OM
  show kreita neutral
  show duran t neutral
  pm "Salt initially dries the meat, but over time, meat will moisturize again, which makes the salt absorb into the flesh even more. So over time, the monster will keep a balanced texture."

  show prowen neutral
  $ renpy.transition(slow_dissolve, layer="master")
  show boyen content behind duran:
    yalign 1.0
    xalign 0.95
  show boyen content at walkBounce behind duran
  "Boyen nodded, making an approving grunt."

  show boyen content OM
  show cimaria surprised
  show kreita grin
  show merona t content
  show lexan surprised
  show duran t surprised
  bg "I can attest to that! If you want to cure meats the manual way, that's what you have to do, but my magical ability speeds up the whole process."

  show boyen content
  show kreita neutral
  show merona t surprised
  show lexan surprised OM
  show rett surprised
  ln "Oh, if that's the case, would it be useful if you were to preserve the monster?"

  show boyen grin
  show cimaria neutral
  show lexan neutral
  show duran t neutral
  "Boyen nodded his head."

  show boyen content OM
  show cimaria gentle
  show merona t serious
  show rett content
  bg "At our next stop, I could try to see if it makes a difference. In cooking, it's important for the meat to be evenly seasoned all the way through, but in our case, we're not eating it."

  show boyen happy2
  show prowen appalled
  show cimaria shocked
  show kreita grin2
  show merona t sadSmile
  show lexan sceptical
  show duran t nervous
  show rett smirk
  bg "Unless we run out of food. Then, the beast will already be fully salted."

  show boyen grin2
  show cimaria serious
  show kreita content
  show merona t nervous
  show lexan neutral
  mi "That does sound better than unseasoned monster. A little flavor would distract me from the fact that I was eating... well, a monster."

  show boyen content
  show prowen serious OM
  show cimaria neutral
  show merona t content
  show duran t content
  show rett neutral
  pm "I'll be the main one caring for the monster... If it becomes too moist or needs more salt, I can deal with it."

  show prowen neutral
  show duran t content CE
  "Duran sighed and smiled to himself."

  play music music_Radio_Martini
  show boyen surprised
  show prowen forcedSmile
  show cimaria sadSmile
  show kreita grin
  show merona t sadSmile
  show lexan grin
  show duran t content OM
  show rett grin
  dt "Thankfully you're here, otherwise Boyen probably would have forced us to eat this thing by now."

  show boyen serious OM
  show duran t annoyed
  bg "Meat is meat! You're not going to die from it once it's cooked."

  play music music_Cool_Steel_Breeze
  show boyen content
  show prowen neutral
  show cimaria neutral
  show kreita neutral OM
  show merona t content
  show lexan neutral
  show duran t neutral
  show rett content
  kh "Okay, now that we know the monster is all fine and dandy, how about the rest?"

  show kreita sceptical
  "Kreita paused, looking up and thinking."

  show kreita happy
  show merona t serious
  show rett neutral
  kh "We've got... enhancers? Yeah, we've got enhancers! How's the enhancing?"

  show boyen neutral
  show kreita neutral
  show merona t disappointed OM
  mk "I tried soaking the dried yander overnight in the enhancer, but it's questionable if that'll make a difference yet."

  show merona t disappointed
  "Cimaria shrugged."

  play music music_Words
  show cimaria neutral OM
  show merona t content
  ck "We'll see. I'll try them out later."

  show cimaria neutral
  show merona t serious OM
  mk "I've gotten used to strengthening living plants with just my ability alone, but that might not be enough for a dried plant without its roots. I'm also drinking the enhancer to see if my magic can make a difference..."
  return
  #-----------------------------------------------
label lbl_PathC_6_9:
  

  #play music music_Words #(continue from before)
  show cimaria gentle OM
  show merona t content
  ck "That sounds fine. There's not much else we can meddle with for the dried yander... I'll deal with it before the time comes."

  show cimaria neutral
  show kreita content CE
  "Kreita clapped her hands together."

  play music music_Dark_Red_Wine
  show boyen surprised
  show cimaria surprised
  show kreita laugh
  show merona t surprised
  show lexan confused
  show duran t surprised
  show rett surprised
  kh "You know what we should do after the operation? Give Rett back his usual night shifts."

  show boyen neutral
  show cimaria serious
  show kreita neutral OM
  show merona t serious
  show lexan neutral
  show duran t neutral
  show rett neutral
  kh "No offense Cimaria-you're pretty cool to hang out with even when I'm sleep-deprived-but I'm sure that Rett wants to help out more."

  show kreita neutral
  show rett pouty
  "He sighed, crossing his arms."

  show cimaria neutral
  show kreita content
  show lexan worried
  show rett pouty OM
  rt "For the record, I do feel bad about not doing as much. I want to help out more... Okay, I'll take back my shifts."

  show cimaria worried
  show rett content
  "Rett straightened up."

  show boyen content
  show prowen content
  show cimaria gentle
  show kreita grin
  show merona t content
  show lexan content
  show duran t smirk
  show rett content OM
  rt "In fact, I look forward to them."

  play music music_Shes_on_my_Mind
  show boyen grin
  show cimaria content OM
  show kreita grin2
  show merona t grin
  show duran t neutral
  show rett content
  ck "*sigh* Whatever. You two both end up falling asleep by the time the sun comes up anyways, so it makes no difference to me."

  show cimaria content
  show rett laugh S
  rt "What!? I think I'm a much better night shift partner than Kreita. We had tons of fun."

  show boyen content
  show prowen neutral
  show cimaria abashed
  show merona t surprised
  show rett embarrassedGrin
  "Cimaria smirked and tucked a few strands of hair behind her ear."

  $ renpy.transition(slow_dissolve, layer="master")
  scene cg CimariaRettFlirting
  ck "Guess you'll have to prove yourself again."
  "Rett laughed and shook his head as Cimaria's cheeks grew pink.  "

  mi "Hm... Does Cimaria still like Rett? Ever since she hinted at it a few weeks ago, I haven't been too sure if she truly felt strongly about him, but I definitely can tell that she treats him a little differently than the rest of us."

  mi "And it's not because he's injured..."

  mi "Even when Rett turned to speak to Kreita, Cimaria's eyes lingered on him. It wasn't a normal linger though. It was... affectionate. "

  mi "Right in between longing and loving."

  "I glanced around, seeing if anyone else was paying attention, but the others were caught up in their own mini conversations."

  mi "The glow on her face isn't due to the beauty sleep she's been getting either..."

  mi "If Cimaria doesn't like Rett as more than a friend, I'm going to question the world for giving me all these signs."

  mi "However..."

  mi "Does Rett feel the same way?"

  mi "I can't tell from his behavior, and I don't know what went on between the two during their night shifts, but now I kind of want 'Cimaria and Rett' to happen."

  play music music_life
  $ renpy.transition(slow_dissolve, layer="master")
  #TODO [fade back to former scene #(forest25 + same sprite positions)
  scene cg forest25
  show boyen neutral:
    yalign 1.0
    xalign 1.0
  show cimaria neutral:
    yalign 1.0
    xalign 0.1
  show kreita neutral:
    yalign 1.0
    xalign 0.5
  show merona t reflective:
    yalign 1.0
    xalign 0.3
  show lexan neutral:
    yalign 1.0
    xalign 0.25
  show rett neutral OM:
    yalign 1.0
    xalign 0.8
  show duran t neutral:
    yalign 1.0
    xalign 0.6
  show prowen neutral:
    yalign 1.0
    xalign -0.1
  
  
  show boyen neutral at walkBounce
  show cimaria neutral at walkBounce
  show kreita neutral at walkBounce
  show merona t reflective at walkBounce
  show lexan neutral at walkBounce
  show rett neutral OM at walkBounce
  show duran t neutral at walkBounce
  show prowen neutral at walkBounce
  show wagon
  "Kreita doesn't seem to notice anything out of the ordinary either. She didn't treat the two any different, and I swear, she'd be making fun of them if she knew that they had a special relationship."

  show kreita content OM
  show merona t serious
  show rett content
  "I honed in as Kreita and Rett's conversation grew louder."

  show boyen content
  show cimaria surprised
  show kreita content
  show merona t surprised
  show lexan content
  show duran t surprised
  show rett laugh
  rt "You know, I think we should turn the cart into a makeshift bed for people on the night shift. Pretty luxurious, don't you think?"

  show cimaria serious
  show kreita sceptical OM
  show merona t sadSmile
  show duran t neutral
  show rett pouty
  kh "Psh, that's basically the same as sleeping on the floor, only slightly more elevated. Besides, the ground is probably more comfortable since there's some cushion to it."

  show kreita sceptical
  show rett pouty OM
  rt "No, the cart would be perfect! The sides act like a barrier, and because it's elevated, it'll feel more like a bed. All the items can be cleared out since we're at a stop and-"

  show rett pouty
  return
  #-----------------------------------------------
  
  #-----------------------------------------------
  # CHAPTER 7
  #-----------------------------------------------
label lbl_PathC_7_3:

  play music music_White
  show merona t sadSmile
  show lexan neutral
  "Poking the sprouts that already popped up, I sighed."

  show kreita grin
  show merona t sadSmile OM
  show duran t evilGrin
  show cimaria sadSmile
  show rett grin
  show boyen content
  show lexan content
  mk "By the time these plants are ready to be used, there'll be no more fish-just nutrient-rich soil."

  show merona t content
  show duran t neutral
  mi "It'll be fun to test out these new enhancers. I only drank generic ones before, but these are a little more specialized for plant manipulators. "

  show kreita content
  show cimaria content
  show rett surprised
  show boyen content OM
  bg "We should have taken some wildflowers and grown them too. There's so much room for more plants! Flowers would be so nice for brightening our days up."

  show merona t content OM
  show rett neutral
  show boyen content
  mk "Well, we still need to leave room in case we run into yander along the way."

  show merona t sadSmile
  "I pursed my lips."

  show merona t sadSmile OM
  show cimaria content CE
  show rett smirk
  show boyen grin
  show lexan grin CE
  mk "Wildflowers do seem really pretty to have though..."

  show merona t sadSmile
  show cimaria neutral
  show boyen neutral CE
  show lexan neutral
  "Boyen shook his head."

  show kreita grin2
  show merona t grin
  show duran t surprised
  show cimaria gentle
  show rett grin
  show boyen happy
  show lexan content
  bg "Oh well. Instead, I'll start arranging the food as flowers! Pay attention to their plates next time!"

  return
  #-----------------------------------------------
  
  #-----------------------------------------------
  # CHAPTER 8
  #-----------------------------------------------
label lbl_PathC_8_4:

  $ renpy.transition(slow_dissolve, layer="master")
  hide duran
  #TODO [fade in merona t serious, right from Prowen
  show merona t serious:
    xalign 0.65
    yalign 1.0
  "Feeling dizzy, I clung onto Prowen's cape and rose all the way up. "
  
  return
  #-----------------------------------------------
label lbl_PathC_8_8_1:
  
  #TODO [positions as before...
  show cg forest29

  show cimaria serious CE
  show merona t determined
  show rett operation
  show rain movie
  "I scanned over the contents again, checking if I overlooked anything, and this time around, I spotted a bottle of dried yander."

  mi "That's right! I knew we had something else."

  show merona t serious
  mi "I'll add some enhancer before I give it to Cimaria. In the worst case scenario, it won't be effective at all, but it's worth a shot!"

  show cimaria neutral CE
  "I fumbled around for the enhancer vial on my hip and poured a few drops onto the shriveled up leaves. Tapping Cimaria's shoulder again, I placed the dried yander in her extended hand, and she resumed concentration."

  #(whisper)
  play music music_White
  show merona t determined OM
  mk "Good luck."

  show cimaria serious CE
  show merona t nervous
  mi "We're still okay... right?"

  mi "This isn't the last resort, is it?"

  show merona t serious
  mi "Or..."

  play music music_Words_Fall_Apart
  show merona t shocked
  mi "I think I'm the last resort."
  show merona t serious
  mi "Hopefully, all the accumulated healing Cimaria has done will be enough. This dried yander could be the finishing touch!"

  show merona t nervous
  "Yet as I continued to watch Cimaria, her scrunched up shoulders, tightly pursed lips, and shaking hands told me otherwise."

  show merona t serious
  mi "Let's not rush things-she only just started to use the dried yander. Give it some time, and..."

  show cimaria shocked CE
  mi "..."

  show merona t desperate
  mi "I'm getting scared now."

  show merona t nervous
  "I shifted my focus to the rain, distracting myself while I could, but the downpour and still overcast sky failed to take my mind off the situation."

  stop music
  show cimaria serious OM CE
  "Cimaria let out a guttural sigh and threw her hands to the ground."

  show cimaria serious
  ck "..."

  show merona t desperate
  mi "Should I say something?"

  mk "..."

  show merona t nervous OM
  mk "...Cimaria?"

  show cimaria shocked
  mk "Are you okay?"

  show merona t nervous
  show cimaria serious
  "Keeping her eyes down, she slowly turned her head toward me."

  play music music_Infinite_Horizon
  show cimaria serious OM
  ck "Merona."

  show merona t serious
  ck "Do whatever you can think of to help him."

  show cimaria serious
  show merona t serious OM
  mk "What?"

  show cimaria serious OM
  show merona t nervous
  ck "It's not impossible for you to make a difference-you manipulate plant and animal life. Humans are also animals, correct?"

  show cimaria serious
  show merona t shocked OM
  mk "Well, yes, but... I'm not that great at animal manipulation. I don't practice it as often as I do with plant manipulation."

  show merona t nervous OM
  mk "Besides, it's kind of different..."

  play music music_Sovereign
  show cimaria neutral OM
  show merona t nervous
  ck "Biologically, we are animals. This is all that matters. As strange as it may seem, if you treat Rett like you would an injured creature, then you may be able to help him."

  show cimaria determined OM
  ck "Try, Merona. I did manage to heal him a bit-he's in slightly better shape than before."

  show cimaria serious OM
  ck "If nothing works, I'll deal with the aftermath."

  show cimaria serious
  show merona t nervous OM
  mk "I..."

  show merona t nervous
  "I stared at Rett, sprawled across the dirt like a beat-up dog, then back at my hands. Hands capable of manipulating plants. Animals. And... humans?"

  show merona t determined
  mi "No more time wasting."

  mi "I have to try."

  return
  #-----------------------------------------------
label lbl_PathC_8_9:
  #TODO [positions as before...
  show cg forest29

  show cimaria serious CE
  show merona t determined
  show rett operation
  show rain movie
  "Moving to Rett's body, I took off my gloves, placed my fingers in the opening of his wound, and closed my eyes."

  scene bg black with fade
  mi "Life flow found. It's on the weaker side, but definitely strong enough to keep him alive."

  mi "I've healed animals before, but it wasn't for external injuries like this. If you count sickness, I suppose that I have dealt with extracting poison... But still, that's too much of a stretch."

  $ renpy.transition(slow_dissolve, layer="master")
  show cg danger
  mi "This monster venom has overpowered his life flow mainly near his arms. I can feel him trying to push past it, but the poison refuses to budge."

  mi "If I could break down the venom..."

  "I deeply inhaled, as if the extra air could boost my power."

  mi "Removing blockages from life flow is a simple task, but when it's something as stubborn as this monster's venom... "

  mi "..."

  mi "This isn't going to work. "

  scene bg black with fade
  mi "Time to put the gloves back on."

  return
  
  #-----------------------------------------------
  # CHAPTER 9
  #-----------------------------------------------
label lbl_PathC_9_3:


  play music music_Lafayette
  $ renpy.transition(slow_dissolve, layer="master")
  show prowen worried:#; right from Merona
    yalign 1.0
    xalign 0.9
  "I sensed footsteps pacing around, just a few feet away. Turning my head over, I found Prowen, head bent down, walking in circles."

  mi "What's he worried about?"

  show prowen neutral
  "Prowen sighed to himself and raised his head, freezing in his tracks as he met my eyes."

  show prowen forcedSmile OM
  pm "Oh... hello."

  show prowen forcedSmile
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content OM#; center
  mk "Hey Prowen."

  show prowen neutral
  show merona t happy OM
  mk "What's up?"

  show prowen worried OM
  show merona t surprised
  pm "Oh you know... everything has been the same."

  show prowen worried
  mi "I don't feel like that's particularly true though."

  show prowen serious
  show merona t worried OM
  mk "You seem worried about something... Are you sure that you're okay?"

  show prowen sadSmile
  show merona t sadSmile OM
  mk "You've been more groggy as of late."

  show prowen forcedSmile OM
  show merona t serious
  pm "Uh... I guess I've had a harder time falling asleep, so I've been a little more tired. But that's all."



  show prowen forcedSmile
  show merona t serious OM
  mk "Oh, okay."

  show prowen neutral
  show merona t nervous
  mk "..."

  show prowen sad
  pm "..."

  show prowen appalled
  show merona t nervous OM
  mk "So..."

  show merona t reflective
  "I racked my brain, thinking about what I could say next."

  play music music_Pride
  show prowen neutral
  show merona t serious OM
  mk "What's your plan after we arrive at our destination? You said you were going to leave us, but what exactly will you do after that?"

  show prowen neutral OM
  show merona t serious
  pm "What I did before I met you all."

  show prowen appalled OM
  show merona t surprised
  pm "Survive."

  show prowen neutral OM
  show merona t serious
  pm "I'll go back to moving around on my own and picking up the odd job here and there."

  show prowen neutral
  show merona t serious OM
  mk "Have you always lived like that? If you don't mind answering, that is."




  show prowen sadSmile OM
  show merona t serious
  pm "Not always. But for a long time now. I stopped keeping count of the years... It doesn't matter how it's been. As long as I'm still alive."

  show prowen surprised
  show merona t content OM
  mk "It's pretty amazing that you're able to live this way though!"

  show prowen neutral
  show merona t surprised OM
  mk "Why did you want to join our group, then?"

  show merona t serious
  "He paused and stared at me for a moment, keeping his neutral expression plastered across his face."

  show prowen neutral OM
  show merona t content
  pm "I was... interested. In what you all were doing."

  show prowen content OM
  show merona t grin
  pm "But I have to admit, I've had some fun with you guys."

  show prowen neutral
  show merona t sadSmile OM
  mk "Even the monster attacks?"

  show prowen smirk
  show merona t serious
  "Prowen, hanging his head down, smirked to himself."

  show prowen smirk OM
  show merona t nervous
  pm "Oh yes. Yes, indeed..."

  show prowen smirk
  mi "Is he being sarcastic or serious? It's hard to tell, especially for him."




  play music music_Under_the_Stairs
  show prowen serious OM
  show merona t serious
  pm "I'm not surprised about all the attacks though. Their numbers are growing, you know?"

  show prowen serious
  show merona t surprised OM
  mk "I mean, you had that antidote with you, so you seemed prepared."

  show prowen sad
  show merona t worried OM
  mk "Have you had much exposure to them alone?"

  show merona t worried
  pm "..."

  show prowen sad OM
  show merona t nervous
  pm "...Yes. I suppose I have."

  #TODO [fade out Music
  play sound sound_ambiance loop
  show prowen sad
  show merona t worried
  "Seeing his jaw tighten just the tiniest bit, I decided not to probe any further."

  show prowen neutral
  show merona t content OM
  mk "Well then, Prowen... I think I'll go now. Can't keep Lexan waiting."

  show prowen sadSmile OM
  show merona t grin
  pm "Thanks for the conversation."

  show prowen sadSmile#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide prowen
  #TODO [stop Nature Ambiance
  play music music_Summer_Day
  show merona t content#; move next to L and back to center
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan neutral:#; left from M, placed at 200px lower than usually
    yalign 2.0
    xalign 0.9
  "I fast-walked over to where Lexan was sitting in the grass and tapped his shoulder. He looked up at me from the notebook he was writing in."


  show merona t grin
  show lexan content OM
  ln "Ready?"

  show merona t determinedGrin OM
  show lexan grin
  mk "Let's do this."

  show merona t grin
  #TODO [move L up to normal Y position
  show lexan grin:
    yalign 1.0
    xalign 0.9
  "Lexan smiled and set aside his notebook."

  show merona t serious
  show lexan determined OM
  ln "As I was taking some notes over our situation, I decided to mull over the first monster attack you faced back at the academy."

  return
  #-----------------------------------------------

label lbl_PathC_9_6:
  play sound sound_bump
  show merona t surprised:
    yalign 1.0
    xalign 0.5
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita grin behind merona:
    yalign 1.0
    xalign 0.4
  "Kreita hopped up from behind me and placed her hands on my shoulders, making me jolt."

  show merona t grin
  show kreita laugh
  kh "Merona! I feel like I haven't gotten to talk to you at all in so long."

  $ renpy.transition(slow_dissolve, layer="master")
  show boyen serious OM:#; right from Merona
    yalign 1.0
    xalign 0.9
  show merona t sadSmile
  show kreita pouty
  bg "Don't scare the poor kid, Kreita..."

  play music music_Greek_Dance
  show kreita tongue
  show boyen sceptical
  "She stuck her tongue out at Boyen and continued clinging onto me."

  show merona t content
  show kreita fierce OM
  show boyen worried
  kh "Doesn't a person need excitement in one's life? I just had to do that to her, for the sake of her well being."

  show merona t happy
  show kreita fierce
  show boyen content
  mk "*laugh* Don't worry, I'm okay! I'm all in one piece."

  play music music_Epilogue
  $ renpy.transition(slow_dissolve, layer="master")
  hide boyen
  show merona t surprised
  show kreita content OM:
      yalign 1.0
      xalign 0.3
  #TODO [move Kreita left from Merona
  kh "You doing okay though, Merona? After everything that happened, I never checked to see how you were."

  show merona t surprised OM
  show kreita content
  show merona at walkBounce
  show kreita at walkBounce
  mk "I'm fine, I'm fine! I was a little more shook last week, but now, I feel much better."

  show merona t worried OM
  show kreita neutral
  mk "What about you? How have you been holding up?"

  show merona t worried
  "She shrugged, smile faltering for a brief moment."

  show merona t nervous
  show kreita neutral OM
  kh "I guess I'm alright. Things could be better, but... It's okay."

  show merona t disappointed OM
  show kreita neutral
  mk "I'm sorry, Kreita. Rett's your cousin, so I know it must have been really hard for you to see him go through that..."

  show merona t surprised
  show kreita aggressive CE
  "She furiously shook her head."

  show merona t serious
  show kreita fierce OM
  kh "No, don't worry! I... knew that he would be fine. Ever since we were kids, he always turned out okay no matter what we faced."

  show merona t surprised
  show kreita serious OM
  kh "Usually, it was me always getting into trouble and injuring myself, but this time..."

  show merona t worried
  show kreita verySad
  "When I glanced up at her face, her cheery expression had resigned, becoming something I had never seen before. She let her words trail off and took her hands off me."

  show kreita verySad OM
  kh "Never mind."

  show merona t sad
  show kreita verySad
  "I nodded, letting the silence fall between us."

  show merona t worried
  show kreita serious
  mi "I guess Kreita is still sensitive over everything that happened. I don't blame her though-she's had a big role in defending our group against the monsters and in leading our group's route, despite being falsely guided by Prowen's manipulation. It's a lot to deal with."

  return
  #-----------------------------------------------