  #-----------------------------------------------
  # CHAPTER 2
  #-----------------------------------------------

label lbl_PathA_2_0:
  #"A2.0"
  #TODO [FINAL
  #(Continuation of 1.9)
  #play music music_Ill_be_right_behind_you_Josephine #(Continue from 1.9 please~)
  scene cg forest7 #(as in 1.9 before)
  show cimaria neutral #(Positons same as before)

  show merona t content behind cimaria:
      xalign 0.75 
      yalign 1.0
  show duran t neutral OM:
      xalign 0.1 
      yalign 1.0
  dt "Whatever. I'll just do what I have to do."
  show duran t neutral #-> fade out please
  $ renpy.transition(slow_dissolve, layer="master")
  hide duran
  "He trudged off to a log at the edge of the clearing, but I stayed where I was."
  stop music fadeout 1.0
  show merona t surprised
  mi "What's he doing? Where's he going?"
  scene cg duranSulk1
  "Duran grabbed and dragged the log out, and he plopped down on it, resting his head on his propped up arm."
  mi "Sitting?"
  play music music_piano
  scene cg duranSulk2
  "I shuffled over, and he looked up at me with his signature face. The one where he looks almost angry but which could be his neutral face."
  scene cg duranSulk3
  dt "Hi."
  scene cg duranSulk2
  mk "Hi."
  "He stayed still."
  mk "..."
  scene cg duranSulk3
  dt "So, are you just going to stand here watching me?"
  scene cg duranSulk2
  mk "Um, well, I was just wondering why you suddenly got up and went here, so I came over here too."
  scene cg duranSulk3
  dt "Thanks for your concern. Are you going to follow me all the time whenever I don't exactly tell you what I'm going to do?"
  scene cg duranSulk2
  mk "Huh? No, of course not."
  stop music fadeout 1.0
  scene cg duranSulk4
  dt "That was a rhetorical question."
  scene cg duranSulk5
  mk "Oh."
  mi "I'm not exactly the sharpest knife in the kitchen, but that did not feel like a rhetorical question at all."
  scene cg duranSulk4
  dt "Yeah."
  scene cg forest8
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita content
  "From my peripheral vision, I saw Kreita galloping over."
  play music music_Aces_High
  show kreita happy
  $ renpy.transition(slow_dissolve, layer="master")
  kh "Hey, you two!"
  show kreita grin2
  #TODO [fade in
  show merona t content:
      xalign 0.1 
      yalign 1.0
  show duran t annoyed: 
      xalign 0.75 
      yalign 1.0
  $ renpy.transition(slow_dissolve, layer="master")
  "She reached us and put her hands on both of our shoulders."
  show kreita happy
  kh "Right now, you guys can collect some wood for the fire. I'm going to get the food and water. You do know what kind of wood is good, right?"
  show kreita content
  show duran t evilGrin OM
  dt "Oh, I definitely know what wood is good for burning..."
  show kreita grin
  show merona t content OM
  show duran t evilGrin
  mk "I know too."
  show kreita fierce OM
  show merona t content
  show duran t neutral
  kh "Yay. Go away and stay out of trouble. Make sure to come back, or else."
  stop music
  show kreita fierce
  show merona t surprised
  show duran t annoyed OM
  dt "Or else what?"
  show duran t annoyed
  "She smiled."
  play music music_Aces_High
  show kreita fierce OM
  show merona t sadSmile
  kh "Or else."
  show kreita fierce
  show duran t annoyed OM
  dt "Or else what exactly?"
  show kreita fierce OM
  show merona t grin
  show duran t annoyed
  kh "Just or else."
  show kreita fierce
  show duran t annoyed EL
  "He rolled his eyes."
  play music music_Radio_Martini
  show kreita grin
  show merona t content OM
  show duran t annoyed
  mk "...I'm going to go now. Duran, you coming?"
  show merona t content
  show duran t annoyed OM
  dt "*sigh* Yeah."
  #TODO [fade out CS kreita happy
  hide kreita
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t grin
  show duran t annoyed
  kh "Have fun, kids."
  play music music_Green_Leaves
  #TODO [fade to CG forest9 #(but keep the CSs please)
  show cg forest9
  $ renpy.transition(slow_dissolve, layer="master")
  "We headed out of the clearing, and we were only surrounded by trees. The others were no longer a part of our background. Just trees."
  show merona t grin ER
  show duran t annoyed EL
  mi "It can be so nice to be outside with only trees and no one else! Well, almost no one else. Duran doesn't seem that strong of a talker, so it's sort of like no one else is here, but I don't mind conversation."
  show merona t sad
  mi "As long as it's not the conversation where he ends up complaining about everything."

  show merona t content
  #TODO [fade out Merona's sprite
  $ renpy.transition(slow_dissolve, layer="master")
  hide merona
  "I crouched down to get some pieces of wood, and I frowned. I held it out and turned it around, fingering it a little. I turned around."
  show duran t surprised
  mk "Duran, can you tell me if this wood is wet or not?"
  show duran t content OM
  dt "Give it."
  show duran t content
  #TODO [fade Merona's sprite back in
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content:
      xalign 0.1 
      yalign 1.0
  "I threw it over to him, and he caught it in one hand."
  show duran t evilGrin OM
  dt "I'll test it out."
  stop music fadeout 1.0
  scene cg duranBurn1
  "He held it out..."

  play sound sound_fireAttack
  $ renpy.transition(dissolve, layer="master")
  scene cg duranBurn2 #with dissolve
  "And it lit up on fire."
  mk "Duran!?"
  mi "So he really can manipulate fire."
  play music music_Nincompoop
  $ renpy.transition(dissolve, layer="master")
  scene cg duranBurn3 #with dissolve
  dt "It's not wet."
  $ renpy.transition(dissolve, layer="master")
  scene cg duranBurn2 #with dissolve
  mk "Why did you have to light it on fire!?"
  $ renpy.transition(dissolve, layer="master")
  scene cg duranBurn3 #with dissolve
  dt "Hey, I couldn't tell if it was wet or not too. It's good use for my ability right?"
  play music music_piano

  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest9 #with fade
  show merona t nervous OM:
      xalign 0.1 
      yalign 1.0
  show duran t annoyed: 
      xalign 0.75 
      yalign 1.0
  $ renpy.transition(slow_dissolve, layer="master")      
  mk "Ugh, never mind. It's a waste of wood to light it up right now, so you shouldn't do it again, okay?"
  show merona t serious
  show duran t annoyed OM
  dt "Of course, Mother, I'm an obedient child and shall do as you say."
  show merona t surprised
  show duran t annoyed
  mi "So we're playing that game, huh?"
  show merona t determinedGrin
  mi "Alright, I'll play along."
  show merona t laugh
  show duran t neutral
  mk "That's right, son. Listen to your dear mommy, and everything will be alright."
  show merona t grin
  show duran t content OM
  dt "*chuckle* Yes, of course. I'm a good child."

  stop music fadeout 1.0
  show merona t content OM
  show duran t content OM
  $ renpy.transition(slow_dissolve, layer="master")
  "We both laughed, but that died soon. In the midst of our silence, we remembered what we had to do, and gathered wood again."
  scene bg black with fade
  
  return
  
  #-----------------------------------------------
label lbl_PathA_2_1:

  play music music_Dark_Red_Wine
  #" [CG and CS tags are red in blue text areas for better distinction... ^^'
  #TODO [fade in merona t content#; app. x=70%
  #TODO [fade in duran t tired#; app. x=25%
  show merona t content:
      xalign 0.70 
      yalign 1.0
  show duran t tired:
      xalign 0.25 
      yalign 1.0
  "Being right next to Duran, I think I'll chat with him a little."

  show merona t content OM
  mk "So Duran, how are you feeling?"
  show merona t content
  "He didn't hesitate to answer or even turn his head towards me."
  show merona t surprised
  show duran t tired OM
  dt "Tired. Really tired."
  show merona t surprised CE
  show duran t tired
  "I nodded."
  show merona t content OM
  mk "Oh. Yeah, it can get pretty tiring walking around so many hours every day. I'm feeling tired myself, but I can keep myself occupied with other thoughts to distract me."
  show merona t content
  show duran t tired OM
  dt "Well good for you. You know how to think about more than one thing at once."
  show merona t laugh
  show duran t tired
  mk "*laugh* Yep."
  show merona t sadSmile
  show duran t worried OM
  dt "*sigh* That wasn't exactly a compliment."
  show merona t sadSmile OM
  show duran t surprised
  mk "It could kind of be a compliment."
  show merona t surprised
  show duran t worried OM
  dt "Maybe in your own screwed up way. But not mine."

  show merona t sadSmile
  show duran t tired
  mi "It's still a compliment to me."
  play music music_Ill_be_right_behind_you_Josephine
  show merona t content OM
  show duran t neutral
  mk "So Duran, even after all these days, I don't know that much about you. Why don't you tell me about yourself?"
  show merona t serious
  show duran t neutral OM
  dt "You already know everything you need to know about me."
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content behind duran:
      xalign 0.35 
      yalign 1.0
  
  #; fade in this CS closer to Duran and behind him please so that the shoulders overlap slightly#; #(if it helps: approximately 100 pixels right from Duran's left edge should be a nice start point for Merona's left edge)
  show duran t surprised
  "I patted his back."
  show merona t happy
  show duran t embarrassed
  mk "There's no harm in learning more right? All I know about you is your name, and that's it. You could be someone completely unexpected."
  show merona t serious
  show duran t embarrassed OM
  dt "Don't touch me. And what's unexpected to you?"
  show merona t sadSmile OM
  show duran t embarrassed
  mk "Um... You could be a girl who likes dressing as a boy."
  play music music_Nincompoop
  show merona t sadSmile
  show duran t annoyed OM
  dt "Do you think that this is the voice of a girl?"
  show merona t grin ER
  show duran t annoyed
  mk "..."
  show merona t sadSmile OM
  show duran t annoyed S
  mk "...No."
  show merona t sadSmile
  show duran t angry OM
  dt "Did you just hesitate?"
  show merona t sadSmile OM
  show duran t angry
  mk "No, no! You're not a girl; that was only the first thing that came to mind. You could be..."
  play music music_potHappy
  show merona t determined OM
  show duran t flabber
  mk "You could be a super genius little boy who's so brilliant that he skipped five grade levels."
  show merona t content
  show duran t angry OM
  dt "Once again, did you think about my voice?"
  show merona t sadSmile OM
  show duran t angry
  mk "Hey, I'm not saying that you're a toddler, but maybe someone who's only ten or twelve. And you never know, some boys that age have a voice like yours."
  show merona t sadSmile
  show duran t annoyed OM
  dt "You're wrong anyways."
  show merona t content OM
  show duran t annoyed EL
  mk "How old are you then?"
  show merona t content
  show duran t neutral OM
  dt "Fifteen."
  show merona t happy
  show duran t neutral
  mk "Whoa, I'm sixteen! Pretty close age, huh?"
  play music music_Revolution_Now
  show merona t surprised
  show duran t evilGrin OM
  dt "You're older than me. I bet I'm smarter than you."

  show merona t worried
  show duran t evilGrin
  mi "Don't disrespect your elders, Duran! I'll brush it off though."
  show merona t happy
  show duran t neutral
  mk "Ha ha... At least I'm a bit taller than you, Duran. "

  show merona t surprised
  show duran t angry OM
  dt "No you're not. Shut up."

  stop music
  show merona t scared
  show duran t angry
  mk "Alright, alright! Sorr-"

  return
  #"-------------------------------------------------------"
  
label lbl_PathA_2_3:

  #"-------------------------------------------------------"
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t surprised:
    yalign 1.0
    xalign 0.75
  show cimaria serious
  "I raised my hand."

  show merona t surprised OM
  show cimaria neutral
  show rett content
  mk "I'll go look for him if that's okay with you."

  show merona t determinedGrin
  mk "Besides, it's a good chance to talk more with him, right?"

  show cimaria content OM
  ck "Oh, alright. Find him quickly. I don't know what his case his, so it's best not to waste any time."

  show merona t happy
  show cimaria content
  mk "Don't worry, I'll do my best. It's not that big of a place anyways, so I'll find him in no time."


  show merona t serious
  #TODO [fade out Cimaria and Rett please~
  $ renpy.transition(slow_dissolve, layer="master")
  hide rett
  hide cimaria
  "I peered around at the possible places for him to go-which basically was either outside at the back of the house or another room down a short hall."
  
  show merona t sadSmile
  mi "I'll opt to go into the room. No way is he outside. He must be crazy if he's outside."

  stop music fadeout 1.0
  scene cg forestHouse inside2
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t serious#; in the center now please
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t serious
  "I went over to the room, and as expected, he was there. His back was turned away from me, but from his bent over head and rotating arm, I could tell he was wrapping something."

  show merona t worried OM
  mk "Are you okay?"

  $ renpy.transition(slow_dissolve, layer="master")
  show duran t surprised#; left from Merona#; from here on, please use his Duran body bandaged version until I mark the scene where he's back to his normal sprite. :3
  $ renpy.transition(slow_dissolve, layer="master")
  show duran b surprised:
    yalign 1.0
    xalign 0.25
  show merona t worried
  "He jerked up and turned his head toward the sound of my voice."

  play music music_piano
  show duran b surprised
  show merona t content
  dt "What? Yeah. Yeah, I'm fine."

  show duran b neutral
  show merona t content OM
  mk "Cimaria's looking for you."

  show merona t serious
  "He shrugged his shoulders and didn't turn around. He continued wrapping."

  show duran b neutral OM
  show merona t shocked
  dt "It's not as bad as I thought. I accidentally burned through one of my gloves."

  show duran b neutral
  show merona t shocked OM
  mk "Wait... you burned yourself? How does that happen? Especially since the flames come out of your hands."

  show duran b annoyed OM
  show merona t shocked
  dt "*sigh* It's not like my entire body is immune to fire. Sure, it comes from my hands, but one hand's flame can burn the other hand not being used."

  show duran b embarrassed
  show merona t surprised OM
  mk "Did you accidentally forget about that hand and ended up burning yourself?"

  show duran b embarrassed OM CE
  show merona t surprised
  dt "Something like that. I panicked about the monster as we were running and a little fire came out."

  show duran b annoyed EL
  show merona t reflective
  mi "Was he trying to help us?"

  show duran b neutral
  show merona t serious OM
  mk "Is it hard to control?"

  show duran b annoyed OM
  show merona t worried
  dt "It's not that it's hard to control; I did it on purpose, with a hundred percent intent on doing it. I just forgot about it for a second, and it burned through my glove, and a little bit of my skin."

  show duran b neutral
  show merona t worried OM
  mk "Are you really okay? You don't need anything to rub on the burn or at least ease the pain?"

  show duran b annoyed EL
  show merona t worried
  "He turned around, his hand wrapped up with an old-looking stained white cloth."

  show duran b annoyed OM
  dt "I told you already, I'm fine-geez, you don't need to keep nagging me on it. I get your concern and all, but it can be a little too much."

  show duran b annoyed
  show merona t sadSmile OM
  mk "*laugh*"


  show merona t sadSmile
  mi "I've gotten told that before. I guess I should watch myself a little about that."

  show merona t content
  "I looked down at my belt and tried to remember which pouch contained what I was looking for. I peeked through a few before finding it. Grasping it, I thrust it out to Duran."

  show duran b surprised
  show merona t happy
  mk "Sorry. But here, I've got some herbs with me that are supposed to help soothe the skin. I bought them at the market, and it's supposed to really work. Forgot what the name of it was, ha ha, but that doesn't matter."

  show merona t content
  "He stared at the bag for a few seconds before coming up to me and taking it."

  show duran b embarrassed OM
  dt "*cough* Thanks."

  show duran b embarrassed
  show merona t happy
  mk "You're welcome!"

  stop music fadeout 1.0
  show duran b bored
  show merona t surprised
  "He stared at my neck for a few seconds."

  show merona t disappointed OM
  mk "Um... Duran? Something wrong?"

  show merona t disappointed
  "He continued staring."

  show duran b neutral
  dt "..."

  show merona t surprised
  "Duran started unwrapping his hand a little and tore off a piece of the cloth, placing it on my shoulder."

  show merona t worried
  mi "Okay?"

  play music music_romance
  show duran b tired OM
  show merona t serious
  dt "Wipe your neck. Your left side."

  show duran b tired
  mi "My neck? "

  show duran b neutral
  "I grabbed the cloth and pressed it against my skin."

  show duran b neutral OM
  dt "It'll dry up later... but you should wipe it up a little and try to stop it."

  show duran b neutral
  show merona t worried
  "Releasing the cloth, a small streak of crimson was blooming on the faded white."

  show merona t surprised
  mi "I wonder when I got this. It's blood probably from a small cut, so it's not too severe."

  show duran b neutral OM
  show merona t content
  dt "You're welcome."

  show duran b neutral
  show merona t happy
  mk "Thank you."

  show duran b content
  show merona t content
  mk "..."

  show duran b neutral
  show merona t content OM
  mk "Let's go to the others, okay? I promised to get you to Cimaria as soon as possible, and we should not make them wait for us."

  show duran b neutral OM
  show merona t content
  dt "Sure, I guess. Nothing to do in here anyway."

  show duran b neutral
  show merona t sadSmile
  mi "Thanks, Duran."

  play music music_She_dreams_in_blue
  #TODO [fade to CG forestHouse inside
  $ renpy.transition(slow_dissolve, layer="master")
  show cg forestHouse inside
  #TODO [no fading and changes for CSs please, except...
  show merona t content
  "We left the room, and I brought him to Cimaria."

  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria neutral OM#; on the right side
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria neutral OM at right
  ck "You're here. What do you need?"

  show cimaria neutral
  show duran b neutral OM
  dt "Nothing now. I took care of it myself."

  show cimaria serious OM
  show duran b neutral
  show merona t surprised
  ck "What did you do? You might still need to be checked over."

  show cimaria serious
  show duran b neutral OM
  show merona t content
  dt "Really small burn. Really small. Not even a noticeable one."

  show duran b neutral
  show merona t content OM
  mk "It just went through his glove."

  show cimaria neutral
  show duran b content OM
  show merona t grin
  dt "Yep, nothing indeed."

  show cimaria neutral OM
  show duran b neutral
  show merona t content
  ck "Let me see it at least. I don't know what you would qualify as a 'really small burn'."

  #TODO [back to the normal Duran body t version now please~
  show duran t neutral
  show cimaria neutral
  "He fully unwrapped his hand, and stretched his palm out. The glove indeed had a hole in it, but the skin itself did not look to be quite as burnt as Cimaria probably assumed."

  show cimaria serious
  ck "..."

  play music music_Words
  show cimaria content OM
  ck "Well alright. It doesn't need special treatment. If it's hurting, I can give you some-"

  show cimaria surprised
  show duran t neutral OM
  show merona t surprised
  dt "I'm fine, I'm fine. It doesn't hurt."

  show cimaria gentle OM
  show duran t neutral
  show merona t sadSmile
  ck "*laugh* You really aren't one for accepting help, are you?"

  show cimaria gentle
  show duran t annoyed EL
  "He shrugged and didn't say anything."

  show cimaria gentle OM
  show duran t neutral
  show merona t content
  ck "Don't hesitate to ask me for help again if you need it, Duran. I hope your hand will feel better."

  show cimaria gentle with Pause(0.5)#; fade out please~
  $ renpy.transition(slow_dissolve, layer="master")
  hide cimaria
  "She turned around to speak to Rett who was a few feet away near the door. I looked at Duran, smiling."

  play music music_piano
  show duran t surprised
  show merona t happy
  mk "You really are someone who keeps to himself, huh?"

  show duran t neutral OM
  show merona t grin
  dt "Sure."

  show duran t neutral S
  show merona t happy
  mk "I can tell."

  show duran t neutral OM S
  show merona t grin
  dt "Sure."

  show duran t neutral S
  show merona t determinedGrin OM
  mk "Yeah."

  show duran t tired OM
  show merona t determinedGrin
  dt "Sure."

  show duran t tired
  show merona t laugh
  mk "Ha ha..."


  return
  
  #-----------------------------------------------
  
  
label lbl_PathA_2_8:

  
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t nervous#; left from Merona
  
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t nervous:
    yalign 1.0
    xalign 0.3
  "Duran nudged my arm."

  show merona t surprised
  show duran t nervous OM
  dt "So what do you think of him?"

  show merona t serious
  show duran t nervous
  "I paused and forced myself not to look back at him. Duran and I were relatively close to the front of the group."

  show merona t serious OM
  show duran t surprised
  mk "What do I think of him? I would say he seems okay."

  show merona t sadSmile
  show duran t annoyed OM
  dt "He's sort of weird, just accepting to come along with us. I mean, we could be serial killers to him or something since he doesn't know that much about us."

  show merona t sadSmile OM
  show duran t tired
  mk "I don't think we seem to be the serial killer type or even the dangerous type to him. Rather, we don't even look that threatening at all. Who knows, he could be desperate for some help or need the company of others."

  show merona t surprised
  mk "We don't even have things of value with us, nor do we look like wealthy nobles. Certainly not dangerous."

  show merona t worried
  show duran t tired OM
  dt "Maybe. His story does make some kind of sense, not to mention he looks pretty raggedy to me."

  play music music_Radio_Martini
  show merona t happy
  show duran t surprised
  mk "He kind of reminds of you in a way."

  show merona t sadSmile
  show duran t angry
  "Duran frowned and looked at me in his second favorite face other than his already negative neutral one- something that I'd like to call \"The Duran\"."

  show duran t angry OM
  dt "Wow, you really are a nice person."

  show merona t sadSmile OM
  show duran t angry
  mk "*laugh* I don't mean it in a bad way. And actually not exactly in a good way either, but more of an in between kind of way."
  show merona t sadSmile
  show duran t angry OM CE
  dt "Go on."

  show merona t content OM
  show duran t nervous
  mk "You two are just similar in the way that you carry yourself to others, albeit Prowen being slightly more responsive. It's a similar kind of air."

  play music music_piano
  show merona t content
  show duran t nervous OM
  dt "I guess that's... okay."

  show merona t determinedGrin OM
  show duran t annoyed EL
  mk "I will admit though, he's a bit more polite than you."

  show merona t grin
  show duran t annoyed OM
  dt "Meh, I don't care so much about that. Just as long as I won't be bothered, you won't be bothered."

  show merona t content OM
  show duran t surprised
  mk "That's good- at least you're not the type of person who lets the words of others bother you so much."

  show merona t content
  show duran t neutral OM
  dt "...I guess so."

  show merona t determinedGrin OM
  show duran t neutral
  mk "Not 'I guess so'. It's 'I know so'."

  show merona t determinedGrin
  show duran t neutral OM S
  dt "Alright."

  stop music fadeout 1.0
  show merona t content
  show duran t embarrassed
  dt "..."

  show merona t grin
  show duran t embarrassed OM
  dt "Thanks."

  show duran t embarrassed
  "He turned his head away and didn't say anything else. I patted his shoulder as a response, but he shrugged my hand off."

  show merona t laugh
  show duran t annoyed
  mk "*laugh* No problem."

  play music music_life
  scene cg DuranPunch
  "He reached up and lightly \"punched\" the side of my head, making me twitch."

  scene cg DuranPunch2
  mk "And that was for...?"

  scene cg DuranPunch3
  "He smiled."

  scene cg DuranPunch4
  dt "Don't you remember what I said? I don't bother anyone unless they bother me. You patted my shoulder."

  scene cg DuranPunch5
  mk "Pffft, I get a punch for a pat?"

  scene cg DuranPunch4
  dt "*laugh* At least I stick to my word."

  scene cg DuranPunch3
  mi "That you do, Duran. That you do."
  scene bg black with fade

  return
  
  #-----------------------------------------------
  # CHAPTER 3
  #-----------------------------------------------
  
label lbl_PathA_3_3:

  
  $ renpy.transition(slow_dissolve, layer="master")
  show black at Blinking
  hide boyen
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t worried behind black:
    xalign 0.5
    yalign 1.0
  "Duran yanked my wrist, and I fell back onto the log he was on."

  show duran t worried OM:
    xalign 0.5
    yalign 1.0#; same animation pattern as before
  dt "Merona."

  $ renpy.transition(slow_dissolve, layer="master")
  show duran t worried#, fade in Duran's opacity to 100%
  hide black 
  "My entire body spasmed, and I managed to tear my gaze away from the fire. Duran grappled one of my wrists using two finger and lifted it up for me."

  $ renpy.transition(slow_dissolve, layer="master")
  scene cg campingFire
  show duran t worried
  #(voice continues to shake)
  mk "What... what are you doing?"

  show duran t nervous
  "I couldn't stop my entire arm from quivering. It was vibrating in the way that a cow I had cared for before shook right after it took a tumble, and I was enraptured by my arm's fast speed."

  show duran t tired
  mi "Stop shaking... please stop shaking."

  stop music fadeout 1.0
  show duran t neutral OM
  dt "Breathe a little."

  show duran t neutral
  mi "In and out. In and out."


  #TODO [move Duran's sprite to the right and fade it out please#; approximately 70%X
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t neutral at right
    
  $ renpy.transition(slow_dissolve, layer="master")
  hide duran
    
  play music music_piano
  "I inhaled a round of fresh air, and its coolness hit me inside. I shuddered out a deep exhale. As I kept repeating, the exhales became shorter, and my shaking slowed down to nothing."
  
  return
  #"-------------------------------------------------------"
  
  
  
  #-----------------------------------------------
  # CHAPTER 4
  #-----------------------------------------------
  
label lbl_PathA_4_4:
  #(Continuation of 4.3)
  #play music music_recollections #(from before)
  show cg hillSide2
  show lexan neutral#; position as in 4.3
  show merona t surprised OM#; position as in 4.3
  mk "We need to get everyone up and running-which means that I need to wake Duran up immediately! Sorry!"

  $ renpy.transition(slow_dissolve, layer="master")
  scene cg hillSide
  show merona t serious#; fade in at center now
  "I scrambled over to his limp body, clutched the monster to one of my arms, and shook his side with the other."

  show merona t worried OM:#; move the sprite down by 250 px
    yalign 2.5
    xalign 0.5
  mk "Duran, wake up! We have to leave now!"

  show merona t worried
  mi "No response. "

  show merona t shocked
  mi "Um... I could hit him, but that might be a bit too much."

  show merona t disappointed
  mi "..."

  show merona t sadSmile
  mi "I'll try to be gentle."

  show merona t embarrassed
  "I hovered my hand above his face for a moment and wrinkled my nose."

  play music music_Up_Kilkenny
  show merona t determined
  mi "Here goes!"

  play sound sound_punch #(Same as in 3.8)
  "I slapped his cheek, holding back, but Duran only twitched."

  show merona t sadSmile
  "Ugh, do I just need to hit him harder? I don't want to actually hurt him... Oh well."

  show merona t determined
  play sound sound_punch #(Same as in 3.8)
  "I paused and slapped his entire face."

  show merona t desperate
  mi "Still not waking up? "

  show merona t surprised
  "You know what, I just have to do something to get him to wake up."

  show merona t reflective
  "What else can I do?"

  stop music fadeout 1.0
  show merona t determined
  mi "..."

  #TODO [move the sprite down by another 250 px
  show merona t determined:
    yalign 4.5
    xalign 0.5
  "I put my mouth near his ear and inhaled a big gulp of air."

  play music music_Up_Kilkenny
  show merona t determined OM
  #(loud voice, almost to the point of yelling)
  mk "DURAN! Wake up!"

  show merona t determinedGrin
  dt "BLERGH!"

  show merona t surprised:
    yalign 2.5
    xalign 0.5#; move back up to 250px down from normal position
  show duran t flabber OM:
    yalign 10.0
    xalign 0.6
  show duran t flabber OM at SitUp#; move more quickly up from the bottom of the image but only up to 250 down from normal position#; positioned slightly right from Merona
  "Duran spasmed up and started slapping the air in front of him with his eyes squeezed shut. I shot out my hands, grabbing his wrists and forcing his arms down. He opened his eyes halfway. "

  show merona t serious
  show duran t angry OM
  dt "Why'd you do that?! Do you like making people go partially deaf? Ugh!"

  play music music_Ecstasy_X
  show merona t serious OM
  show duran t angry
  mk "Doesn't matter if I like to make people deaf or not. We have to go right now, so please get up!"

  show merona t sad
  show duran t annoyed OM
  dt "What's going on? Did something bad come up?"

  show merona t sadSmile OM
  show duran t surprised
  mk "I'll explain to you later. We really need to leave now though!!"

  show merona t nervous
  show duran t annoyed OM CE S
  dt "Hey, just use a few words and tell m-"

  show merona t determined OM
  show duran t flabber
  mk "Accidentally caught a monster. Rett was poisoned. Need to get meds. Leaving now."

  show merona t determined
  show duran t flabber OM
  dt "What happened!?"

  show merona t determined OM
  show duran t nervous
  mk "Duran, if you don't move, I will pick you up and piggyback you to where everyone else is. Do you want that to happen?"

  show merona t serious
  "I set the monster down and reached my hands out, scanning over where to grab him#; Duran squirmed away."

  show merona t sadSmile
  show duran t surprised OM
  dt "Don't touch me, I'll get up! Argh, let's go."

  play music music_Radio_Martini
  show merona t content
  show duran t annoyed
  "I picked up the monster again and patted his head. He glared at me again."

  show merona t disappointed
  show duran t angry OM
  dt "I just said not to touch me."

  show merona t determined OM
  show duran t angry
  mk "And I just said that I'd piggyback you if you don't get up and go."

  show merona t determinedGrin OM
  show duran t worried CE
  mk "I see that you aren't going."

  show merona t determinedGrin
  show duran t angry
  dt "Urgh!"

  show merona t sadSmile
  #TODO [Move both sprites to their normal height position please~
  
  show merona t sadSmile at StandUp
  show duran t angry at StandUp
  "I sighed and smiled."

  show merona t content CE
  show duran t annoyed
  mi "Another win for Merona."

  play music music_piano
  #TODO [fade CG to hillSide2
  $ renpy.transition(slow_dissolve, layer="master")
  show cg hillSide2
  show merona t serious
  show duran t neutral
  "We hurried over to the cart. Everything looked like it was in place, and nothing seemed to be missing, so all that was left was to wait for the others."

  show merona t surprised
  show duran t neutral OM
  dt "You know... it doesn't exactly feel like we really had to rush."

  show merona t serious OM
  show duran t tired
  mk "What do you mean?"

  show merona t serious
  show duran t tired OM
  dt "I don't think you needed to push me so much to hurry up."

  show merona t disappointed OM
  show duran t annoyed EL
  mk "*sigh* Duran, just be glad that I didn't leave you behind and 'forget' about you."

  #(mumbling)

  show merona t disappointed
  show duran t tired OM
  dt "I'd much rather want to be forgotten than be here..."

  show merona t shocked OM
  show duran t worried
  mk "Don't even think about it."

  show merona t nervous
  show duran t neutral#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide duran
  "One by one, everyone gathered around once they were finished with their business."
  return
  #-----------------------------------------------
label lbl_PathA_4_5:
  
  play music music_Words
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest18
  #TODO [fade in CG forest18
  #TODO [fade in with CG: CS merona t serious#; center
  show merona t serious
  #TODO [fade in #(a bit later) CS duran t neutral#; position right from Merona #(not at the right edge of the image but something like 60-70% of x)#; move him a bit towards Merona so that the sprites slightly overlap, then move him back to the start position
  pause(0.5)
  show duran t neutral behind merona:
    yalign 1.0
    xalign 0.7
  show duran t neutral at ShoulderTap3
  "As we all walked, Duran tapped my shoulder."

  show merona t surprised
  show duran t tired OM:
    yalign 1.0
    xalign 0.7
  dt "What exactly did you guys find out?"

  show merona t serious OM
  show duran t worried
  mk "Simply put, the creature Rett caught is most likely a monster. Since he caught it by smashing into it, it bit into him a few times, and Cimaria found out that there was venom from the bites."

  show merona t worried
  show duran t worried OM
  dt "Oh..."

  show merona t serious
  dt "...Do you think that he'll be okay?"

  show merona t worried OM
  show duran t worried
  mk "Mm... I can't exactly say."

  show merona t disappointed OM
  show duran t nervous
  "I mean, this is monster venom we're dealing with, and that can do some fatal stuff."

  show merona t worried
  show duran t nervous OM
  dt "Yeah. He seems to be fine right now, but that could change, you know? We don't even know how exactly the venom will work, how long it'll take for us to find what we need to make the medicine, or which specific town we're going to."

  show merona t sad OM
  show duran t neutral
  mk "Well, we don't have time right now to figure out those details anyways. We just need the basics and start moving, so it can't be helped."

  show merona t sad
  show duran t neutral OM
  dt "I guess so."

  show merona t nervous
  show duran t neutral
  mi "I wonder what Cimaria saw when she found the venom. What was it doing to Rett's body, if anything?"

  play music music_Soporific
  show merona t serious
  show duran t neutral OM
  dt "What do you think about the monster he got?"

  show merona t determined OM
  show duran t neutral
  mk "The monster? It was like what you'd expect I suppose-weird looking. Weird feeling. But then again, it was dead so who knows? It could have been different when it was alive."

  show merona t serious
  show duran t neutral OM
  dt "Then I assume that Rett squashed it to death when he caught it."

  show merona t serious OM
  show duran t neutral
  mk "Probably... It's pretty small after all, so that seems to be the most likely situation."

  show merona t surprised
  show duran t sad OM
  dt "It's not as if the trees killed it or anything."

  stop music
  show merona t surprised OM
  show duran t surprised
  mk "Or did they?"

  show merona t surprised
  show duran t flabber OM
  dt "What?"

  show merona t sadSmile OM
  show duran t flabber
  mi "It's possible, isn't it? "

  play music music_life
  show merona t serious OM
  show duran t annoyed EL
  mk "Just a random assumption. You don't know, what if the trees actually did do something while we weren't looking?"

  show merona t worried
  show duran t annoyed OM
  dt "That's... no, that's just..."

  show merona t disappointed
  show duran t annoyed OM CE S
  dt "...No."

  show merona t serious OM
  show duran t nervous
  mk "Before we started traveling I pondered about that stuff a lot#; what trees or animals could do when we aren't looking. It was interesting."

  show merona t serious
  show duran t nervous OM
  dt "Uh..."

  show merona t serious OM
  show duran t nervous
  mk "I tried observing stuff before. Never saw something definite, but imagined a lot of possible things."

  show merona t surprised
  "He gave me a blank look."

  show merona t serious
  show duran t nervous OM
  dt "Are you... okay?"

  show merona t sadSmile
  show duran t nervous
  mi "Duran, you're making it sound like I need mental help. Ha ha."

  show merona t sadSmile OM
  show duran t tired
  mk "Look, I know this all sounds kind of crazy and is probably not real, but there isn't any harm in just thinking about this stuff! I had a lot of time on my hands and merely let my mind roam free. "

  show merona t sadSmile
  show duran t tired OM
  dt "Um..."

  show merona t serious
  show duran t neutral OM CE S
  dt "Okay."

  show duran t nervous OM
  dt "Do you, uh... think about that kind of stuff a lot?"

  show merona t serious CE
  show duran t nervous
  "I shrugged and tilted my head to the side."

  show merona t content OM
  show duran t tired
  mk "Not a lot a lot, but you know, every now and then. Whenever I saw something that reminded me of it."

  show merona t content
  show duran t nervous OM
  dt "So... a lot."

  show merona t content OM
  show duran t nervous
  mk "Since we've started this trip, I'm pretty sure I haven't thought about it all until now. I really tried to focus on learning, and I guess that worked."

  show merona t happy
  show duran t surprised
  mk "It'd be amazing if trees and animals actually could communicate with humans though, don't you agree? Even if it's so unlikely."

  play music music_Pilot_Error
  show merona t surprised
  show duran t annoyed
  "Duran rolled his eyes."

  show merona t disappointed
  show duran t annoyed OM
  dt "I don't want to start fantasizing about talking trees and whatnot."

  show merona t sadSmile OM
  show duran t annoyed EL
  mk "Ha, I think I'm not really trying to convert people into whatever it is I'm thinking. I don't even think that I'd actually truly believe something like that to believe in, but it's still fun to think of things like that, right?"

  show merona t disappointed
  show duran t annoyed OM
  dt "Whatever works for you. That's kind of pointless to me."

  show merona t disappointed OM
  show duran t tired
  mk "I'll give you credit, for it actually is kind of pointless. But there's nothing really wrong with that though."

  show merona t disappointed
  show duran t annoyed OM S
  dt "*sigh* I'd rather not waste my time with pointless things, so to me, there is something wrong with that."

  show merona t disappointed
  show duran t annoyed#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide duran
  mk "..."

  show merona t nervous OM
  mi "Well..."

  show merona t determined OM
  mk "Fine."

  return
  #-----------------------------------------------
label lbl_PathA_4_7:

  
  #TODO [As before:
  #play music music_Green_Leaves
  #scene cg forestGround
  #show mattress#; center
  #show merona t determined#; center, use Merona hair u please
  #show blanket#; center

  #show Clouds dark#; opacity around 30-50%#; "
  #"if possible, use a "multiply" mode for them please#; "
  #"slowly move from right to left please
  mi "I suppose I'll splash some water on my face and see if that'll help. It's not like it will make me drowsy after all!"
  #TODO [fade out Merona's sprite while moving the blanket down by 200px
  show blanket:
    yalign 4.5
  $ renpy.transition(slow_dissolve, layer="master")
  hide merona
  "I crawled out of my sheets and stretched my arms."
  play music music_life
  scene cg forest19
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content#; with Merona hair t again please
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content
  mi "Alright. Let's see if I can get down to the stream without falling into it. I think I'll stay there for a bit too and just wind myself down. Staring at the water seems to be relaxing."
  play sound sound_water #(looped)
  "Shuffling out of the clearing, I entered into the forest and headed to the stream. A few fallen trees and medium-sized rocks were by the water, so I scanned around for a nice one to sit on. I began skipping down."
  #TODO [fade to CG stream#; #(don't erase sprite)
  $ renpy.transition(slow_dissolve, layer="master")
  show cg stream
  show merona t content OM
  mk "Ah, here we are."
  show merona t content CE:#; move sprite down by 280px please
    yalign 2.5
    xalign 0.5
  "I reached the stream and crouched down to cup some of the gently running water in my hands. Squeezing my eyes shut, I splashed the cold water onto my face. I shivered a bit as stray drops of water trickled over my neck."
  show merona t grin:#; move sprite up again by 150px please
    yalign 1.5
    xalign 0.5
  mi "Well, that certainly woke me up! I feel a lot more refreshed. Time to go and sit on that rock now I suppose."
  show merona t content:#; move sprite to the left, leaving some space to the edge #(about 400px)
    yalign 1.5
    xalign 0.7
  "I wiped off the excess water on my clothes and pushed myself up halfway. The rock was only a few steps away, so I scooted my feet back, waiting to hit the rock. There were a few things I had to dodge, but I still faced forward."
  mi "Hopefully, I won't run into anything. But if I do, at least it wo-"
  stop music
  play sound sound_bump
  show merona t surprised OM
  mk "Oomph!"
  scene bg black with fade
  "My heels hit into something soft, and I fell back onto it."
  $ renpy.transition(slow_dissolve, layer="master")
  #TODO [fade to CG streamGround
  scene cg streamGround
  #TODO [at the same time fade in...
  show duran t flabber OM:#; rotated counter-clockwise by about 20°
    yalign 2.0
    xalign 0.5
    rotate -20
  show merona t scared:#; rotated clockwise by about 25°
    yalign -7.0
    xalign 0.6
    rotate 25
  #(the feet of both shouldn't be cut off, so please move the sprites down as much as needed :3)
  dt "Ergh!!"
  show duran t flabber
  show merona t worried OM
  mk "Duran!?"
  show duran t flabber OM
  show merona t disappointed
  dt "You!?"
  play music music_Radio_Martini
  show merona t serious#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide merona
  "I scrambled to get myself off him and slid away."
  scene cg stream
  show merona t worried OM:#; right side#; 250px lower than normal position:
    yalign 2.5
    xalign 0.6
  show duran t annoyed:#; left side#; 250px lower than normal position:
    yalign 2.0
    xalign 0.2
    rotate 0
  mk "Whoa, I'm really sorry!! I didn't notice you here. Are you okay? Did I hurt you in any way?"
  show merona t worried
  show duran t angry
  "Duran didn't move and glared at me."
  show merona t disappointed
  show duran t angry OM
  dt "Thanks for stepping onto my stomach and then collapsing onto me. No really, thanks. Ugh."
  show merona t shocked OM
  show duran t surprised
  mk "Look Duran, I'm really sorry. I didn't mean to do anything bad, but are you seriously okay?"
  show merona t worried
  show duran t embarrassed OM
  "He opened his mouth and hesitated for a moment."
  dt "I-I'm..."
  play music music_romance
  show merona t sadSmile
  show duran t nervous OM
  dt "...fine."
  show merona t sadSmile OM
  show duran t nervous
  mk "Good."
  show merona t serious
  show duran t embarrassed
  dt "..."
  show merona t surprised
  show duran t tired OM
  dt "So... why are you here?"
  show merona t surprised OM
  show duran t neutral
  mk "Me? I just wanted to do something, so I came down here. How about you?"
  show merona t surprised
  "He shrugged."
  show merona t content
  show duran t neutral OM
  dt "Same thing more or less."
  show duran t neutral
  mk "..."
  show merona t grin ER
  dt "..."
  show merona t grin
  show duran t annoyed OM
  dt "So..."
  show merona t sadSmile OM
  show duran t annoyed EL
  mk "So..."
  show merona t surprised
  show duran t tired OM
  dt "Uh... are you going to stay here?"
  show merona t surprised OM
  show duran t neutral
  mk "Um... I guess so. Yeah."
  show merona t content OM
  show duran t tired
  mk "How'd you sleep last night?"
  show merona t content
  show duran t tired OM
  dt "How'd I sleep? Fine."

  play music music_Pilot_Error
  show merona t disappointed
  show duran t annoyed OM
  dt "If you're going to keep asking questions like this, you can just leave now. I don't really need your company."
  show merona t determinedGrin
  show duran t annoyed EL
  mi "Huh. Seems like a good challenge-see if I can keep a conversation with Duran."
  show merona t determinedGrin OM
  show duran t annoyed
  mk "Well... if I ask you more interesting questions would you be willing to answer them?"
  show merona t grin
  show duran t surprised
  "He raised an eyebrow."
  show duran t tired OM
  dt "Interesting questions?"
  show merona t happy
  show duran t tired
  mk "Interesting questions."
  show merona t content
  show duran t tired OM CE
  dt "I don't know."
  show merona t sadSmile OM
  show duran t neutral
  mk "Never mind. How about some regular questions?"
  show merona t sadSmile
  show duran t annoyed OM
  dt "Uh-"
  play music music_meronatheme
  show merona t content OM
  show duran t neutral
  mk "What have you been doing with Lexan?"
  show merona t content
  show duran t neutral OM
  dt "Lexan? Uh... you know, regular stuff. Fire-y things."
  show merona t serious
  show duran t worried OM
  dt "How have you been doing? Did you find out a lot about what you did to that monster or something like that?"
  show merona t serious OM
  show duran t worried
  mk "Actually, I haven't done anything about that yet. I've just been working on my current lessons and the like, but they've been going pretty well."
  show merona t serious
  show duran t neutral
  mk "..."
  "I paused for a moment."
  play music music_Swimming_To_Cambodia
  show merona t serious OM
  mk "Regarding with what I did to that monster..."
  show merona t worried OM
  show duran t worried
  mk "...I still don't have any idea what happened. I don't even know if what happened had anything to do with me."
  show merona t sadSmile
  show duran t worried OM
  dt "Can you... tell me what exactly did happen then? I never really got to know the full story on that. Or if I did, I don't remember."
  show merona t sadSmile OM
  show duran t surprised
  mk "Basically when a monster almost killed me, I closed my eyes and when I opened them, a black rabbit was there."
  show merona t grin
  show duran t flabber OM
  dt "A black rabbit was there? Just there?"
  show merona t happy
  show duran t surprised
  mk "Yeah. I don't know much beyond that."
  show merona t serious OM
  show duran t worried
  mk "I guess that open question is another reason why we're doing this. This journey."

  show merona t surprised
  show duran t worried OM
  dt "If that's another reason... what are you going to do about it?"
  show merona t surprised OM
  show duran t worried
  mk "I... haven't really thought about it too much to be honest. I'm trying to focus more on what I'm doing right now rather than that. But after I've got my current things settled, I think that'll be a better time to think about what actually happened and if I did anything."
  show merona t content
  show duran t annoyed OM
  dt "That's fine, I guess. Not really any of my business."
  play music music_piano
  show merona t content OM
  show duran t neutral
  mk "Why are you here anyways? Any specific reason?"
  show merona t worried OM
  show duran t annoyed EL
  "Duran sighed and turned his head away."
  show merona t disappointed
  show duran t annoyed OM
  dt "Well, that's not really any of your business, but I'm not here for a reason like yours. I'm just another 'assistant' for you. I'm here for who knows why."
  show merona t serious CE
  show duran t annoyed
  "I shook my head."
  show merona t serious OM
  show duran t surprised
  mk "I don't think you're here to specifically help me like the others; even they have objectives of their own, I'm sure. But was there something you needed help on like me?"
  show merona t surprised
  show duran t annoyed OM S
  dt "I don't know. Frankly, I don't even care. At least I got to get out of that place."
  show merona t disappointed
  show duran t annoyed S
  mk "..."
  show merona t nervous
  show duran t annoyed EL
  dt "..."
  show duran t annoyed OM
  dt "If you don't mind, I kind of want to be alone right now."
  show merona t sadSmile OM
  show duran t annoyed
  mk "Oh, of course. I'll leave you be. See you around, Duran."

  show merona t serious
  show duran t annoyed CE
  "He didn't move, but he nodded."

  show duran t annoyed EL
  #TODO [fade out Merona#; at the same time move a bit to the right please
  $ renpy.transition(slow_dissolve, layer="master")
  hide merona
  dt "Mhm."
  #TODO [Stop sound loop of Water
  stop sound
  play music music_SoT
  $ renpy.transition(slow_dissolve, layer="master")
  #TODO [fade to CG forest19
  scene cg forest19
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t serious#; normal height position now
  show merona t serious
  "I got up and headed back up the hill, paying attention to my surroundings so that I wouldn't slip and fall."
  show merona t nervous
  mi "Duran doesn't know why he's here... what's the real reason for why he was chosen to come along then? Surely the headmaster didn't take my request to have another student around my age to come along..."
  
  return
  
  
  #-----------------------------------------------
  # CHAPTER 5
  #-----------------------------------------------
label lbl_PathA_5_2_1:

  play music music_Radio_Martini #(from before)
  scene cg forest22
  show tree
  #TODO [Positions as in the end of A5.1
  show cimaria content:#; left from Kreita:
    yalign 1.0
    xalign 0.3
  show kreita grin#, center
  show merona t content OM:#, right from Kreita:
    yalign 1.0
    xalign 0.7
  show rett content:#, right from Merona
    yalign 1.0
    xalign 0.9

  mk "I'll go with the preservationist group."
  show merona t content
  mi "Might as well help look around!"
  
  return
  #-----------------------------------------------
label lbl_PathA_5_2_2:
  
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest23
  #TODO [fade to CG forest23
  #TODO [#(later) fade inCS kreita content
  pause(0.5)
  show kreita content
  "Kreita glanced at those in her group and gestured for us to come together."
  show kreita fierce OM
  kh "Well, I guess I'm kind of the group leader here since I volunteered first. But anyways, how do you guys want to look? All together? All alone? Or what else?"
  show kreita fierce
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t surprised OM:#; left from Kreita
    yalign 1.0
    xalign 0.25
  
  mk "It'd be better if none of us is alone so we can keep in contact with a person about how we're doing. How about we go in pairs or something like that?"
  show kreita grin
  show merona t worried
  mi "Not to mention the possibility of if one person got hurt. You would need someone else to be there for you."
  show kreita fierce OM
  show merona t content
  kh "Yeah... Yeah, that sounds great! Pairs. You and Duran could be a unit, and I'll go with Prowen here."

  play music music_Pilot_Error
  show kreita grin2
  show merona t surprised
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t annoyed:#; right from Kreita
    yalign 1.0
    xalign 0.75
  "Duran clenched his teeth and sighed."
  show kreita neutral
  show merona t sadSmile
  show duran t annoyed OM
  dt "Uh... Could I go with you or him instead? I already spend enough time with Merona on other things, so..."
  show duran t evilGrin
  "Duran smirked at me."
  show kreita pouty
  show merona t serious
  show duran t evilGrin OM
  dt "No offense."
  show merona t determinedGrin
  show duran t evilGrin
  "I grinned right back at him."
  show merona t determinedGrin OM
  mk "None taken."
  show kreita grin
  show merona t determinedGrin
  mi "Just keep trying to run away from me, Duran. You'll most like only get pulled in tighter."
  play music music_romance
  show kreita fierce OM
  show duran t nervous
  kh "Aw, Duran, if you wanted to be with Merona so bad, you should have just said so! Don't worry, you two will be paired up."
  show kreita fierce
  show merona t grin
  show duran t bored
  mi "You see, Duran?"
  show merona t content OM
  show duran t neutral
  mk "Well, we should use up the time we have and go now. Duran and I can go towards the east side."
  show kreita content OM
  show merona t content
  kh "Fantastic. We'll take the west side then."
  show kreita content
  $ renpy.transition(slow_dissolve, layer="master")
  show prowen sceptical:#; slightly right from Kreita #(they should overlap a bit)
    yalign 1.0
    xalign 0.6
  show duran t flabber
  "Kreita slapped her arm around Prowen's shoulder, and he jumped up."
  show kreita fierce OM
  show prowen forcedSmile
  show merona t grin ER
  show duran t nervous
  kh "Come on, Prowen. I think it's time we get to know each other a little more."
  show kreita fierce#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide kreita
  hide prowen
  #TODO [fade out Prowen as well
  show merona t content
  "Prowen, unanswering, simply stared at Kreita, but she led him off to begin their searching. I placed my hands at my hips and looked to Duran."

  stop music fadeout 1.0
  show merona t surprised
  show duran t neutral OM
  dt "Well..."
  show merona t surprised OM
  show duran t neutral
  mk "What?"
  show merona t surprised
  show duran t annoyed EL
  dt "..."
  play music music_piano
  show duran t annoyed OM
  dt "*huff* Fine."
  show merona t content OM
  show duran t tired
  mk "*laugh* Fine for what?"
  show merona t content
  show duran t annoyed OM
  dt "Fine, let's go."
  show merona t happy
  show duran t annoyed
  mk "Yeah. That's what I thought."
  play music music_Travel_Light
  show merona t grin:
    yalign 1.0
    linear 0.40 xalign 0.60
    linear 0.40 xalign 0.25#; move Merona towards Duran's direction and stop about 100px before him and then back
  show duran t angry
  "I patted his shoulder, but he slithered my hand right off."
  show merona t disappointed:
    yalign 1.0
    xalign 0.25
  show duran t angry OM
  dt "Don't touch me."
  show duran t angry
  "I held up both hands in front of me and backed off."
  show merona t disappointed OM
  show duran t annoyed EL
  mk "Alright, alright, I'll keep my paws to myself."
  return
  #-----------------------------------------------
label lbl_PathA_5_3:
  
  #(Continuation of 5.2)
  #play music music_Travel_Light #(from before)
  #scene cg forest23 #from before
  show merona t surprised#; position as in the end of the former chapter
  show duran t annoyed
  "Duran shuffled forward, and I skipped over to catch up a step. I bent down to tap my head on his shoulder."
  show duran t nervous
  show merona t disappointed OM
  mk "Don't leave me behind, Duran! Or else I might just 'accidentally' crash into your back."
  show duran t nervous OM
  show merona t serious
  dt "Is that a threat?"
  show duran t nervous
  show merona t determinedGrin
  mi "...Yes."
  show duran t surprised
  show merona t determinedGrin OM
  mk "It's whatever you want it to be. Your dreams, your nightmares, your hopes, your despair..."
  show duran t nervous OM
  show merona t determinedGrin
  dt "Yeah... Okay."
  $ renpy.transition(slow_dissolve, layer="master")
  show cg town behind merona
  show cg_sky1 behind cg 
  show clouds behind cg at leftright
  show duran t neutral
  show merona t content
  play music music_Words
  "We continued on walking, soon entering the town. I scanned my surroundings, and Duran glanced right and left as well."
  show merona t reflective
  mi "What exactly does a preservationist's place of business look like?"

  show duran t tired
  show merona t worried
  mi "It's not a typical thing you would see out and about on display, but there has to be some kind of sign or indicator of one... I mean, if our entire group knew of this type of industry without questioning it, it shouldn't be too exotic."
  show duran t neutral
  "I turned to Duran."
  show merona t worried OM
  mk "Duran, do you know what to look for?"
  show duran t worried OM
  show merona t worried
  dt "Uh..."
  show duran t worried
  show merona t sadSmile
  "I nodded."
  show duran t neutral
  show merona t sadSmile OM
  mk "I take that as a no."
  show merona t serious OM
  mk "I've never really noticed where preservationists work, so I don't know how to actively find it either."
  show duran t tired
  show merona t serious
  "Duran crossed his arms and shrugged."
  show duran t tired OM
  show merona t surprised
  dt "We have such a high success rate here, huh?"
  show duran t neutral
  show merona t grin:
    yalign 1.0
    linear 0.40 xalign 0.70
    linear 0.40 xalign 0.25#; move her sprite towards Duran's and back
  "I nudged him and grinned."

  play music music_Dark_Red_Wine
  show duran t angry
  show merona t laugh
  mk "So high that it's taller than you. Then again, most things are."
  show duran t evilGrin
  show merona t grin ER
  "Duran gave me an exaggerated smile."
  show duran t evilGrin OM
  show merona t sadSmile
  dt "How about we just stop talking now and start searching?"
  show duran t evilGrin
  show merona t sadSmile OM
  mk "*laugh* Alright, alright. Let's get back on track. Still, there's nothing wrong with some communication seeing how we both don't know what to find."

  show duran t annoyed OM
  show merona t surprised
  dt "I think if we telepathically communicate, that's enough. Even better than speaking aloud. Try it."
  stop music fadeout 1.0
  show duran t neutral
  mk "..."
  show merona t serious
  "I waited for a few seconds, letting him revel in the silence."
  show duran t tired
  show merona t serious OM
  mk "Duran?"
  show duran t tired OM
  show merona t surprised
  dt "Don't break the moment."
  show duran t tired
  show merona t surprised OM
  mk "The moment?"
  show merona t surprised
  dt "..."
  show duran t neutral
  show merona t content
  mk "..."
  show merona t grin
  dt "..."
  show duran t tired
  show merona t laugh
  mk "...Durrrrran?"
  show duran t evilGrin
  show merona t grin
  "Duran sighed, but he still snorted at me."
  play music music_Dark_Red_Wine
  show duran t neutral OM
  show merona t sadSmile
  dt "You broke the moment."
  show duran t surprised
  show merona t happy
  mk "Can I tape the moment back together?"
  show duran t content
  show merona t content
  "He nodded."
  show duran t content OM
  dt "Using liquid cement would make the moment a lot stronger, but if you can't do that, just use tape."
  show duran t surprised
  show merona t content OM
  mk "Cool. I don't think I really want to have the moment again though, so you're going to have to deal with this new moment where we're talking out loud."
  show duran t neutral
  show merona t grin ER
  mi "Another point for Merona. Not that there's a score being kept, but I think I'm winning."
  show merona t content
  "Duran looked up and around for a few seconds and then back at me."
  show duran t neutral OM
  dt "Hey, do you think that some of these buildings have more stores on the upper level?"
  show duran t neutral
  show merona t serious OM
  mk "There's no sign or anything pointing up to them, so it's most likely the store owners' homes. That's how it usually works. No business wants zero advertising for them either."
  show duran t surprised OM
  show merona t serious
  dt "Oh right, I forgot about that."
  show duran t neutral OM
  dt "Why don't we just ask some local people if they know of a preservationist in town? That'd definitely help shave some time off."
  return
  #-----------------------------------------------
label lbl_PathA_5_4:
  
  #play music music_Dark_Red_Wine #(from before)
  #scene cg town #from before
  $ renpy.transition(slow_dissolve, layer="master")
  show cg town behind merona
  show cg_sky1 behind cg 
  show clouds behind cg at leftright
  show duran t neutral#; pos as last chapter
  show merona t reflective#; pos as last chapter
  "I shrugged."

  show merona t serious OM
  mk "I don't see why not. But we can only do that if we happen to bump into anyone around here, and we haven't exactly seen a person strolling around..."

  play music music_White
  show merona t surprised
  show duran t neutral OM
  dt "People are probably working. This isn't the best time to be shopping really, if you look at the clock."

  show merona t sadSmile OM
  show duran t neutral
  mk "*sigh* I guess so."

  show merona t content
  show duran t surprised
  "I squinted at the ground, digging in my head for more possibilities, and my face lit up. I clapped my hands."

  show merona t content OM
  show duran t neutral
  mk "I know! Do you want to go into some stores and ask the people there? That could help."
  show merona t content
  show duran t content OM
  dt "Sure, we can go into this one right here then."

  show duran t content
  "Duran pointed to the building at our right."

  show merona t grin
  mi "It's a tailoring place, but.... they still might know. No big harm in asking them!"

  show merona t happy
  mk "Okay. Let's go in."
  play music music_Sugar_On_My_Tongue
  scene cg tailorshop back# -> consists of the parts: tailorWall #(back layer), tailorDoor closed #(on wall layer/ behind characters)#; tailorFront #(in front of character sprites)
  show cg_composite tailorShop_full1 behind cg # Show here to enable gallery
  show cg_composite tailorShop_full2 behind cg # Show here to enable gallery
  show cg_composite tailorShop_full3 behind cg # Show here to enable gallery
  hide cg_composite
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t neutral:#; at approximately 85%x
    yalign 1.0
    xalign 0.8
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content:#; right from Duran
    yalign 1.0
    xalign 1.0
  show tailorshop front
  "Duran walked over to the door and pulled it open. These buildings on this block had most of the shops or offices contained inside, unlike vendors, and this one we entered was no exception. There was a medium sized window that allowed some sun to stream in, but it was the only one on this floor. "

  show merona t surprised
  "Some bolts of fabric were piled up in baskets in the corners. Clothes that looked finished were lain on a table, and more unfinished pieces were placed there as well. Other than the audience of cloth, nobody else was in our vicinity."
  return
  #-----------------------------------------------
label lbl_PathA_5_5:
  
  #play music music_Sugar_On_My_Tongue#(from before)
  #scene cg tailorshop #from before
  show duran t annoyed OM:#; at approximately 85%x#; move to the center
    yalign 1.0
    xalign 0.5
  show merona t sadSmile#; as in the end of last chapter
  dt "Ah, how wonderful. This may be the best customer service I've ever experienced."
  show duran t annoyed
  show merona t grin:#; move a little towards the center
    yalign 1.0
    xalign 0.75
  "I scoffed and scanned over the room again."
  show merona t sadSmile OM
  mk "I rather agree with you, Duran..."
  show duran t neutral
  show merona t happy
  mk "But I do see something a little better."
  show duran t annoyed OM
  show merona t grin
  dt "Do you mean a mannequin? Because being able to look at a faceless head is a lot better, definitely."
  show duran t surprised
  show merona t laugh
  "I laughed and smiled."
  show duran t neutral
  show merona t happy
  mk "Actually there really is a disassembled mannequin in a box tucked under a table on your right, but even better than that!"
  show merona t grin
  "I pointed over to the far end of the shop."

  play music music_Cool_Steel_Breeze
  show merona t content OM
  mk "See that door? And the sign on it that's the same color?"
  show duran t tired
  show merona t content
  "Duran squinted his eyes to where I indicated."
  show duran t tired OM
  dt "Didn't notice it at all at first. It really blends into the rest of the wall..."
  show duran t neutral
  show merona t content OM
  mk "Same with me. Even the knob sticking out is the same color as the door... It might not be a part of this store, so it may be like that on purpose. Do you think there would be people in that room?"
  show duran t tired
  show merona t serious
  "He shrugged and crossed his arms."
  show duran t tired OM
  dt "May as well be where some employees work on these clothes. What does the sign even say? From here it looks like..."
  stop music
  show duran t tired
  show merona t serious OM
  mk "...'Do not enter?'"
  show merona t surprised
  "His half-shut eyes flicked up to mine."
  play music music_Nincompoop
  show duran t evilGrin OM
  show merona t shocked
  dt "Then, do you wanna enter?"
  show duran t evilGrin
  show merona t nervous
  "My eyes blinked to look at the door, and I bit my lip."
  mi "Well, what do you think the purpose of a \"Do not enter\" sign is?"
  show duran t surprised
  show merona t nervous OM
  mk "Eh... there are probably people working behind there. Let's just leave and go to another place. That'd be more convenient."
  show duran t annoyed EL
  show merona t nervous
  "Duran rolled his eyes and scowled for a second."
  show duran t annoyed OM
  show merona t surprised
  dt "We're already in here, so let's make things 'more convenient' for us by actually getting to talk to someone."
  show duran t annoyed
  show merona t disappointed CE
  "I still shook my head."
  play music music_Pilot_Error
  show merona t disappointed OM
  mk "No thanks, it's okay. Stepping into this store in the first place didn't promise us to get any info, so let's just go."
  show merona t worried
  "Duran didn't move and didn't look like he was going to move anytime soon. I reached down to grab his wrist in his crossed arms, but he shuffled back and smirked."
  show duran t annoyed OM S
  show merona t disappointed
  dt "I hold my own hand, thank you very much. No need to keep dragging me around, Mom. I've gotten old enough to wander outside by myself. You can go out yourself if you'd like, but I'm going into that room."
  show duran t annoyed
  $ renpy.transition(slow_dissolve, layer="master")
  hide duran
  show merona t disappointed OM
  mk "Uh-"
  stop music
  show merona t surprised
  "But that was the only sound I managed to drop out of my mouth for him to hear. Duran already skipped over to the door and slipped in without any hesitation or trouble."
  show merona t nervous OM
  mk "*sigh*"
  show merona t disappointed
  mi "I can't just leave him here. What if he gets into trouble? Me not being near wouldn't be good."
  return
  #-----------------------------------------------
label lbl_PathA_5_6:
  

  scene cg tailorshop door closed
  mk "Duran! Find anything?"

  play sound sound_knock
  "A muffled bang on the door replied."

  play music music_Radio_Martini
  mi "I guess he's fine enough to respond like that."

  mi "Unless he's being held against his will and managed to get out a kick to call my attention. But a scream would have accompanied that knock on the door, so I trust that he's safe."

  play sound sound_knock
  #TODO [fade door part to CS tailorDoor slightlyOpen after playing the knock sound please
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg tailorshop door slightlyOpen

  "I knocked on the door before opening it up a bit and peering inside. Wild fabric was strewn all over, even more than the fabric in the room upon entrance, and the air had the scent of freshly washed clothes with a hint of the outside to it."


  mk "Duran?"

  scene cg tailorshop duran
  "I swung open the door, but his hand stopped it before it was fully open."

  stop music fadeout 1.0
  scene cg tailorshop duran OM
  dt "Shhhh...."

  scene cg tailorshop duran
  "He hissed at me and was slouched over, voice low."

  scene cg tailorshop duran OM
  dt "There are some people in here sleeping, presumably employees. The floorboards in this room are a little squeaky, and I accidentally knocked down some piles of clothes, so... I need to quietly slip out of this room..."


  scene cg tailorshop duran
  "I nodded and half-smiled at him."

  play music music_Ecstasy_X

  mk "Didn't I tell you not to go in? Should have listened a little more... And fabric spilling over doesn't make a loud noise, so you shouldn't worry about that."


  "He kept his voice down."

  scene cg tailorshop duran OM
  dt "Whatever, I'll listen more once I'm out of here... and I want to move out fast so that they don't know that I was the one who messed up their workplace, so that's another reason why I can't wake them up."
  return
  #-----------------------------------------------
label lbl_PathA_5_7:
  

  #play music music_Ecstasy_X #(from before)
  #TODO [Scene as before
  scene cg tailorshop duran 
  mk "Did you at least try to put things back the way they were?"

  scene cg tailorshop duran OM
  dt "They're sleeping and they'll think that they knocked it down themselves, so..."

  scene cg tailorshop door slightlyOpen
  "I gave him a tight-lipped smile and shut the door closer in."

  scene cg tailorshop duran SO OM
  dt "What are you doing?!"

  scene cg tailorshop duran SO 
  "I shrugged at his sharp question. He kept his voice down, but his facial expression was loud on its own with him glaring at me, a betrayal-like look in his eyes."

  mi "It might not be the best choice for both of us, but I'm just a little done with Duran, and I think it should be time to truly do something about it. "


  mk "So, you can pick up what you messed with, and at least attempt to get it back in decent order. Don't be a jerk."

  scene cg tailorshop duran SO OM
  dt "You're kind of being the jerk here."

  play music music_Up_Kilkenny
  scene cg tailorshop duran SO 
  mk "Don't they say to fight fire with fire? *laugh* So attacking you in your own way should be super effective."

  scene cg tailorshop duran SO OM
  dt "That made as much sense as your rotting brain."

  scene cg tailorshop duran SO 
  mk "Ah, so it was very hard to grasp for you because of my complex mind. It's rotting because I've been using it so much, so thank you for the praise."

  dt "..."

  scene cg tailorshop duran SO #; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg tailorshop door slightlyOpen
  "Duran's face loosened a bit, looking deflated, and he kept mumbling things to himself. I still held the door in the same place, and tensed up in case he tried to ram against it. However, he proceeded to trudge back into the room and fix his misdoings."

  "I peered through the little opening and saw him toss silky fabrics next to some of the sleeping men and women carefully, aiming for them to not flutter on top of the person. He moved onto a mannequin and bent down, lifting up the item like it was a sleeping cub."

  mi "That's..."

  return
  #-----------------------------------------------
label lbl_PathA_5_8:
  

  play music music_eerie
  #TODO [Scene as before
  "His hands trembled as he slid the pinned garment in short segments over the curves of the mannequin, making the pins loosen little by little as it rubbed against the body."

  mi "Oh geez... That dress isn't even sewn. If he accidentally pulls too hard on it, the fabric is going to come apart. And if it comes apart, then..."

  mi "Hm..."

  "Duran's breathing was steady and uncontrolled, at an audible level as well due to no accompanying sounds. The higher he pulled up the dress, the smaller and faster his hands shook."

  mi "Can't let that pretty, structured dress lose its form..."

  mi "..."

  mi "I'll go and help him."

  play music music_recollections
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg tailorDress
  show duran t nervous at right
  show merona t worried
  "Tip-toeing in, I crept up to the mannequin as well and kept my voice down to a whisper."
  
  $fontSizeModifier = -10
  #(Keep font size down)
  show duran t surprised
  show merona t worried OM
  mk "{size=[fontSizeModifier]}Hey.{/size}"

  show merona t serious#; move a bit more towards the right #(where a dress in the BG will be depicted)
  show duran t worried
  "I lightly pinched one sleeve of the dress, motioning Duran with my eyes to pick up the other one as well. The sleeves were already around the stomach area, but getting the waistline of the dress to rise above the hips without having the pins fall out was proving to be a threat."

  mi "Maybe we should try pushing the pins deeper in and then loosening them once this is situated. There seems to be enough room to do so."

  show merona t serious OM
  show duran t neutral
  mk "{size=[fontSizeModifier]}Duran, try this.{/size}"

  show merona t serious
  show duran t tired
  "I proceeded with my idea while keeping eye contact with him. Duran paused for a second, as if he was analyzing my technique, but he soon nodded and followed my lead."

  show merona t content
  "The dress was a bit stabler now, and we obtained more space and ease to prop it back up on the mannequin's shoulders. When it was dusted off and arranged, nothing looked out of place."

  show merona t nervous
  show duran t neutral
  mi "I don't know how it was before, but let's hope that these people don't remember that either."

  show merona t surprised
  show duran t nervous
  "Duran coughed in a low grunt."

  play music music_Up_Kilkenny
  show merona t serious
  show duran t nervous OM
  dt "{size=[fontSizeModifier]}Let's actually get out of here.{/size}"

  show merona t content OM
  show duran t neutral
  mk "{size=[fontSizeModifier]}Lead the way, pal.{/size}"

  show merona t serious
  "Duran ignored me and step by step approached the exit as I joined him. The floorboards thankfully weren't the creaky kind, so our escape felt pretty seamless."

  show merona t sadSmile
  mi "Just don't wake up employees... get all the beauty sleep you need."

  play sound sound_fallInDirt
  stop music
  show merona t shocked
  show duran t flabber:#; move sprite down by 250px
    yalign 2.5
    xalign 0.75
  "But alas, a certain red-haired fire boy stumbled and collapsed to the hard, wooden floor."

  $fontSizeModifier = 10
  dt "{size=+[fontSizeModifier]}Pf!{/size}"

  show merona t scared
  show duran t neutral S
  "As Duran let out a breath of discomfort on his back, I caught a woman's face scrunching up."

  show merona t disappointed
  show duran t worried
  mi "So much for seamless escape. We've got our thread beginning to loosen here."

  "I hopped on my toes over Duran to open the door wider and grabbed his forearm. He shot an alarmed look over at me, but I only leaned in to whisper in his ear."

  $fontSizeModifier = -10
  show merona t disappointed OM
  show duran t flabber
  mk "{size=[fontSizeModifier]}Stop. Don't move.{/size}"

  show merona t serious
  show duran t nervous
  "I gave a small tug at his arm first, and he didn't say anything."

  show merona t worried OM
  mi "Okay... Please don't start fighting me with what I'm going to do next..."

  play music music_Nincompoop
  show merona t worried:#; move towards Duran's sprite so that they are close to each other
    yalign 1.0
    xalign 0.65
  show duran t flabber OM#; fade to neutral S
  pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t neutral S
  "I pulled harder and wrenched Duran out at the same pace as I would with a hearty bag of potatoes-only difference being that Duran wasn't food and considerably lighter than that. He scrambled his legs at my lugging initially, but soon surrendered to me once he saw the sleeping workers again."

  show merona t disappointed:#; move Merona and Duran next to each other to the center
    yalign 1.0
    xalign 0.4
  show duran t neutral S:
    yalign 2.5
    xalign 0.55
  mi "We're so close to the exit anyways. Duran would make some noise by getting up and creaking the floor with his boots and weight. At least his clothes rubbing against the floorboards won't make loud sounds. This is my instinct choice, so I hope it works out..."

  show merona t shocked
  "Once I hauled him all the way out the door, a man grumbled and as my head darted to the break in silence, his half-lidded eyes met mine."

  mi "Oh no."

  play music music_movement
  show merona t desperate at RunBounce#; start moving up and down for running
  show duran t neutral S:#; move up to normal height position#; start moving up and down for running
    yalign 1.0
    xalign 0.55
  pause(0.5)
  show duran t neutral S at RunBounce
  "I thrust the door closed and stopped it before it would slam into the frame. After gently shutting it, I pulled Duran up and propelled out of the building with him in tow."

  show duran t angry OM
  dt "Hey!"

  $ renpy.transition(slow_dissolve, layer="master")
  show cg town behind merona
  show cg_sky1 behind cg 
  show clouds behind cg at leftright
  show duran t surprised OM
  "Duran gasped at me as I was running a considerable distance away from there."

  show merona t sad
  show duran t embarrassed
  mi "No way am I stopping until we get out of sight."

  show merona t worried
  show duran t embarrassed OM
  "I kept slamming my feet down onto the road, making dust powder around the two of us. Stores flashed past me. When we reached the turn of the street and crossed to the next one, only then did I slow down into a jog and then a walk. Heat edged into my head. I could feel more dirt than beads of sweat on me, and Duran was panting."

  stop music fadeout 1.0
  show merona t surprised:
    yalign 1.0
    xalign 0.4
  show duran t angryBlush:
    yalign 1.0
    xalign 0.7
  #TODO [Stop the up and down movements of the sprites here please~
  "I let go of him and turned to his sulking form. His breathing became further subdued as we walked at a normal speed now. He focused to what was in front of him."

  play music music_piano
  show merona t worried OM
  mk "Sorry about that. A guy was already appearing to wake up, so my gut feeling told me to bolt. I know, it's not really pleasant to suddenly be taken like that..."

  show merona t worried
  show duran t embarrassed
  dt "..."

  show duran t annoyed OM S
  mk "Yeah."

  show merona t worried OM
  show duran t annoyed
  mk "And I'm sorry about making you go into that room to pick things back up by yourself. If they woke up earlier, you would have taken all the blame there."

  show merona t worried
  show duran t nervous
  dt "..."

  show merona t sadSmile OM
  mk "Also, sorry for literally dragging you out of there... You already told me before that you didn't like being touched by anyone, and there I was pawing at you and everything."

  show merona t sadSmile
  show duran t neutral
  dt "..."

  show duran t sad
  mk "......"

  show merona t determinedGrin
  show duran t sad OM
  mk "Yeah."

  show merona t laugh
  show duran t worried
  "I chortled at his consistent one-liner."

  show merona t happy
  show duran t surprised
  mk "Yeah, I would also say that too."

  show merona t grin
  show duran t worried
  dt "..."

  stop sound
  stop music
  show merona t surprised
  show duran t worried OM
  dt "But..."

  show merona t surprised OM
  show duran t worried
  mk "But?"

  play music music_romance
  show merona t serious
  show duran t embarrassed
  "I stared at the path ahead as well, and Duran crossed one arm over his body."

  show merona t disappointed
  show duran t embarrassed OM
  dt "I don't know. I don't really know what to say."

  show merona t disappointed OM
  show duran t embarrassed
  mk "Well... you did begin with a 'but'."

  show merona t surprised
  show duran t embarrassed OM
  dt "That was just one word. And I didn't know what was going to come after that 'but'."

  show merona t worried
  show duran t embarrassed
  mk "..."

  show merona t sadSmile OM
  mk "You don't have to say anything if you're mad at me."

  show merona t serious
  show duran t embarrassed OM
  dt "But..."

  show duran t embarrassed CE
  "His voice decreased in volume."

  show merona t surprised
  show duran t blushSmile OM
  dt "I'm not really that mad at you."

  show merona t content
  show duran t blushSmile
  "I glimpsed back at him and smiled."

  show merona t content OM
  show duran t surprised
  mk "Is that what you were going to say earlier?"

  show merona t content
  show duran t neutral
  "He returned my glance, however not returning the smile but rather his usual neutral Duran face."

  show duran t neutral OM
  dt "I guess so."

  show merona t content
  show duran t sad OM
  dt "I never actually felt mad... maybe kind of annoyed."

  show merona t grin
  show duran t neutral
  "I chuckled and nodded."

  show merona t content
  show duran t neutral OM
  dt "I don't know."

  show duran t surprised OM
  dt "It's not like it was something to get extremely angry over."

  show merona t surprised
  show duran t tired OM
  dt "This was a little weird and different though. You dragging me and all that... was strange, but anyone can see why you did it. Even if it was not really a great way of doing it."

  show merona t serious
  show duran t annoyed
  "He looked away with a scowling face."

  stop music fadeout 1.0
  show merona t sadSmile
  show duran t annoyed OM
  dt "Seriously though, don't do that ever again."

  show merona t embarrassedSmile
  show duran t annoyed
  "I gave him an embarrassed smile and averted my face."

  show merona t embarrassedSmile OM
  show duran t neutral
  mk "I won't, I won't! Promise."

  show merona t embarrassed
  show duran t sad
  "Duran focused back at me."

  play music music_Ill_be_right_behind_you_Josephine
  show duran t sad OM
  dt "And even stranger, I want to say 'sorry', but also say 'thank you' as well."

  show merona t surprised
  show duran t sad
  "I raised my eyebrows, meeting his eyes."

  show merona t surprised OM
  show duran t neutral
  mk "Why so?"

  show merona t sadSmile
  mi "Okay, now I don't know what he's saying. But it sounds interesting. Let's continue listening."

  show merona t serious
  show duran t sad OM
  dt "Sorry... because I can see that I was sort of pushy when I forced myself into that room. Pushy and yeah, rude."

  show duran t nervous OM
  dt "It's what I'm used to doing. I just want to do what I want and not get 'ran over' all the time."

  show merona t disappointed OM
  show duran t nervous
  mk "Ran over?"

  show merona t serious
  show duran t annoyed EL
  "He rolled his eyes."

  show merona t sadSmile
  show duran t annoyed OM
  dt "Not literally. That was a figure of speech."

  show merona t sadSmile OM
  show duran t neutral
  mk "Right, right, I got that meaning-I was questioning what was behind the figurative meaning."

  show merona t serious
  "He shrugged."

  show duran t annoyed OM
  dt "Nothing really worth noting or that important. I just like doing things the way I like it. Or at least knowing the way I want things. I don't like not thinking and blindly going along with everyone."

  show merona t worried
  show duran t neutral OM
  dt "Doesn't have a nice feeling."

  show merona t worried CE
  show duran t neutral
  "I nodded."

  show merona t worried OM
  mk "Understandable."

  show merona t serious
  dt "Mmhm."

  show merona t surprised
  show duran t neutral OM
  dt "And... thanks for helping me out a little too."

  show merona t serious
  dt "I didn't expect you to do something after I went in there."

  show merona t serious OM
  show duran t neutral
  mk "To be honest, I wasn't going to do anything."

  show merona t sadSmile OM
  show duran t content
  mk "But then I decided that that wouldn't be a good choice."

  show merona t sadSmile
  "Duran scoffed."

  show duran t content OM
  dt "Yeah."

  play music music_meronatheme
  show merona t sadSmile OM
  show duran t neutral
  mk "*laugh* Right. What would you have done if you'd been caught by them?"

  show merona t surprised
  show duran t tired OM
  dt "Eh, nothing. I mean, there's nothing to do after that."

  show merona t surprised OM
  show duran t neutral
  mk "You wouldn't drag me in?"

  show merona t sadSmile
  show duran t neutral OM
  dt "Well, the thought probably would've crossed my mind."

  show merona t serious OM
  show duran t neutral
  mk "Makes sense."

  play music music_Words
  show merona t worried OM
  mk "Duran, do you get in these kind of things a lot? Because you don't seem to panic or react strongly."

  show merona t worried
  show duran t sad
  "His frown deepened."

  show merona t serious
  show duran t sad OM
  dt "Are my reactions even that strong in the first place?"

  show merona t serious OM
  show duran t sad
  mk "Point taken."

  show merona t serious
  show duran t neutral CE
  "He shook his head, and his face went back to neutral."

  show duran t neutral OM
  dt "I'm not involved in these situations a lot. At least, I don't try to. Sometimes I kind of just end up in weird predicaments."

  show merona t content OM
  show duran t neutral
  mk "Well yeah, everyone has those times. Nice job though."

  show merona t serious OM
  show duran t surprised
  mk "You know, I'm still a little confused on why you thanked me."

  show merona t surprised
  show duran t surprised OM
  dt "You don't want the thanks then?"

  show duran t neutral
  "I held out my hands."

  play music music_life
  show merona t surprised OM
  show duran t content
  mk "Give me all the thanks you have."

  show merona t content
  show duran t neutral
  "Duran grabbed the air, placed the nothingness in my palms, and closed my fingers around it."

  show merona t grin
  show duran t evilGrin OM
  dt "Then you won't get a lot."

  show duran t neutral
  dt "..."

  play music music_She_dreams_in_blue
  show merona t surprised
  show duran t neutral OM
  dt "When I said that I happen to somehow get in weird predicaments, I also somehow got out of them myself."

  show merona t serious
  show duran t tired OM
  dt "Sometimes I got into them not because of only myself, but still, I'm used to escaping on my own."

  show merona t content
  show duran t neutral OM
  dt "That's why I said thanks. Because you helped me out. It's natural to thank someone for that, right?"

  show merona t content OM
  show duran t neutral
  mk "Yes, I see. Thanks for the... courtesy of thanking me, I suppose."

  show merona t grin
  show duran t annoyed OM
  dt "Okay, now you don't have to continuously find ways to thank me."

  show merona t worried OM
  show duran t annoyed
  "I nodded and sighed."

  play music music_Travel_Light
  show duran t neutral
  mk "*sigh* How did you think Kreita and Prowen did?"

  show merona t worried
  show duran t worried OM
  dt "I don't imagine any better than us. Who's gonna find something as obscure as a specialized preservationist somewhere like here."

  show merona t content OM
  show duran t neutral
  mk "The other group of Cimaria, Lexan, Boyen, and Rett are probably doing better with the yander search."

  show merona t sadSmile
  mi "I feel like we still have a chance though. We already are at this town, so we got to continue looking around! We may not have any other times to stop."

  show merona t determined
  mi "Okay, let's do this. Get pumped."

  show merona t determined OM
  show duran t surprised
  mk "Let's keep looking."

  show merona t determined
  show duran t tired OM
  dt "Merona, it's still okay if we call it quits and go to the meeting place. We can say that we didn't find anything, and it'll be believable."

  show merona t determinedGrin
  show duran t tired
  "I swatted down his suggestion."

  show merona t determinedGrin OM
  mk "We still have plenty of time before we need to meet up there! Do you really want to just sit there and wait with me, doing nothing?"

  show merona t serious
  show duran t blushSmile
  "Duran looked at the ground."

  play music music_romance
  show merona t surprised
  show duran t blushSmile OM
  dt "It... doesn't sound awful."

  show duran t embarrassed OM
  mk "It could be worse. It's not as boring if you're there too. And there isn't nothing to do. We can... I don't know, look at the view... talk..."

  play music music_potHappy
  show merona t determined OM
  show duran t nervous
  mk "Maybe next time. I still have hopes for finding something in this town. So please, let's keep looking. We've only gone into one place."

  show merona t content
  show duran t nervous OM
  dt "Since you did help me out back there... Fine, let's carry on."

  show merona t grin
  show duran t neutral
  "I stopped and pointed to a storefront with meats on display."

  show merona t happy
  show duran t surprised
  mk "Ah, would you look at that? Good coincidence."

  show merona t content#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide merona
  show duran t neutral
  "I headed up to the man and woman handling some of the raw meat outside the door."

  #TODO [fade Duran out
  $ renpy.transition(slow_dissolve, layer="master")
  hide duran
  mi "The smell of salted dead animal. Not as refreshing as the living and dead plants I'm used to, but refreshing in its own sense, especially in our case."

  mi "Let's test out if they'll help us preserve this 'fish' we have too."

  $ renpy.transition(slow_dissolve, layer="master")
  scene bg black
  pause(0.5)
  return
  #-----------------------------------------------
label lbl_PathA_5_9:
  
  play music music_Nincompoop
  #TODO [fade from black
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg_sky1
  show clouds at leftright
  show cg town
  show cimaria surprised#; center
  show kreita fish happy:#; right from center/ Cimaria#; please use Kreita bodyFish #(switch between this and Kreita bodyFish2 for animation where indicated later on)
    yalign 1.0
    xalign 0.75
  show prowen forcedSmile behind kreita at right#; right from Kreita
  show merona t content at left#; left
  show duran t neutral:#; between Merona and Cimaria #(left from center)
    yalign 1.0
    xalign 0.25
  kh "Guys, guys, look what Prowen and I found!"

  show cimaria neutral
  show kreita fishAnimated grin2#; please animate Kreita bodyFish
  show merona t surprised
  "Kreita's eyes smiled as well when she gushed on about the clump of fish swinging by the tail in her hand. She gestured her fist all around our group, sticking out a puffed chest full of pride."

  show cimaria shocked
  show duran t annoyed
  mi "I suppose this is what the butchers meant by already giving others something before."

  show kreita fish pouty#; stop animating Kreita bodyFish
  show prowen neutral
  show merona t sadSmile
  show duran t annoyed OM
  dt "I... don't see how this is useful."

  show cimaria serious
  show merona t sadSmile OM
  show duran t annoyed
  mk "Well..."

  show kreita fish neutral
  show merona t serious
  mi "Our monster is a fish. Kreita and Prowen brought back normal fish."

  show merona t reflective
  mi "..."

  play music music_Words
  show merona t worried
  mi "I was going to try and find a plausible reason, but nope, I don't have anything to say."

  show cimaria serious OM
  show kreita fish grin2 CE S
  show prowen neutral CE
  show merona t serious
  show duran t tired
  ck "Could you explain to us what the... dead fish... is for, Kreita? We all seem a little confused..."

  show cimaria serious
  show kreita fish sad
  show prowen neutral
  "Kreita deflated a bit at our lack of enthusiasm."

  show cimaria neutral
  show kreita fish sceptical OM
  show prowen forcedSmile
  show merona t surprised
  show duran t nervous
  kh "Oh come on, aren't you guys good at dealing with plants and life and all that other fancy stuff? You should get some kind of idea of what this is for. Apparently, it's a great tip for plants."

  show kreita fish pouty
  show prowen neutral
  show merona t surprised OM
  mk "Plants? Weren't you guys supposed to also be looking for a preservationist like Duran and I? Did I miss something?"

  show merona t surprised
  show duran t neutral
  "Prowen interjected with small raised hand."

  show cimaria worried
  show kreita fish sadSmile
  show prowen neutral OM
  show merona t serious
  pm "Yes we were, but this is the best we found."

  show cimaria neutral
  show kreita fish neutral
  show prowen neutral
  show duran t neutral OM
  dt "You know, we went to the same place, and they just said two people beforehand already asked about preservation. By any chance was it you two at a meat shop?"

  show kreita fishAnimated grin#; please animate Kreita bodyFish
  show merona t serious
  show duran t annoyed
  "Prowen nodded. Kreita pointed the fish at Duran and wagged the shiny heads at him. I couldn't help but keep eye contact with their unblinking jelly-like eyes."

  mi "So many little eyes could make several big eyes on our monster friend here."

  show merona t reflective
  mi "What kind of plant tips could dead fish make again though? I feel like I have an inkling of an idea... It's really been a long time since I've thought about shortcuts to growing things. I'm too used to using my own ability to cut corners."

  play music music_Travel_Light
  show cimaria surprised
  show kreita fishAnimated neutral OM
  show prowen content
  show duran t surprised
  kh "Fertilizer."

  show cimaria neutral
  show kreita fishAnimated neutral
  show merona t surprised
  show duran t neutral
  "My face awakened as the fact entered my head again."

  show kreita fishAnimated content
  show merona t happy
  mk "That's right! Fish is a nice fertilizer."

  show kreita fishAnimated serious
  show prowen neutral
  show merona t disappointed OM
  mk "But wait."

  show cimaria serious
  show kreita fish sad#; stop animating Kreita bodyFish
  show duran t bored
  mk "We're not growing yander."

  show merona t disappointed
  mk "..."

  show kreita fish pouty
  show merona t surprised OM
  show duran t neutral
  mk "Or are we? Did I miss something for real this time?"

  show cimaria serious OM
  show merona t serious
  ck "Not that I know of. Rett and I weren't looking for and didn't find yander to grow."

  #TODO [fade out the sprites
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg_sky1
  show clouds at leftright
  show cg town
  return
  #-----------------------------------------------
  
  
  #-----------------------------------------------
  # CHAPTER 6
  #-----------------------------------------------
label lbl_PathA_6_0_1:
  

  play music music_potHappy
  show cg_sky1
  show clouds at leftright
  show cg town #(from before)
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan content:
    yalign 1.0
    xalign 0.0
  show boyen happy:# right from Lexan
    yalign 1.0
    xalign 0.2
  show rett content:#; left from center
    yalign 1.0
    xalign 0.4
  show duran t neutral:#; right from center
    yalign 1.0
    xalign 0.75
  show merona t content:
    yalign 1.0
    xalign 1.0
  bg "Lexan and I actually found some yander seeds in a store! It was the only yander related item in there, so we bought it."

  $ renpy.transition(slow_dissolve, layer="master")
  show kreita fishAnimated grin:#; center#; animate Kreita bodyFish
    yalign 1.0
    xalign 0.5
  
  show boyen content
  "A smirk danced on Kreita's face as she flung her fish around some more."

  show kreita fishAnimated laugh
  show rett smirk
  show merona t grin
  kh "I knew this was a great choice!"

  show kreita fishAnimated happy
  show rett surprised
  show lexan neutral
  show boyen grin
  show duran t surprised
  show merona t surprised
  kh "We could start a traveling yander garden. Just plant them in pots and have them relax in the wagon, bask in the sunlight, and get occasionally watered."

  show kreita fishAnimated grin2
  show rett surprised OM
  show lexan determined
  show duran t neutral
  show merona t grin
  rt "You know... that actually doesn't sound like bad idea."

  show rett sceptical
  show merona t content
  "Kreita twirled her beloved bunch onto Rett's shoulder."

  show kreita fishAnimated laugh
  show rett neutral
  show lexan content
  show boyen content
  kh "I know, it's making me really excited too! Prowen almost talked me out of it, but thank the earth that I didn't listen to him!"

  show kreita fishAnimated grin
  "Prowen shrugged, making me chuckle. Rett pushed the fish off himself and instead gave a quick side-hug on Kreita's shoulder."

  show kreita fish content#; stop animating
  show rett content OM
  show lexan serious
  show boyen neutral
  show merona t reflective
  rt "Well, whatever happened was good, so nice job little cousin. But is it convenient to plant yander? How long is it going to take to grow?"

  play music music_White
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita neutral#; fade to normal body
  show rett neutral
  show merona t serious
  pm "I think we should move on from this... We've been dragging this out, quite a bit."

  show duran t neutral OM
  dt "Good point. So Merona and I found nothing. Next person."

  show lexan surprised
  show duran t annoyed
  "Duran elbowed Lexan beside him."

  show boyen content
  show lexan neutral OM
  show duran t neutral
  show merona t content
  ln "Uh-the seeds."

  show boyen neutral
  show lexan neutral
  ck "Some unrelated items, but nothing pertaining to yander was found."

  show merona t worried
  mi "Alright, so we ultimately can only plant it. Splendid. All we have to do is figure out how long it'll take and all that other info, but this is a solid start. I just hope that Rett isn't going to die from whatever is in him by then, which isn't looking to be a big issue now, but no jinxing it!"

  show merona t determined
  mi "We're not doing too bad."

  play music music_newBegin
  show kreita content
  show lexan neutral OM
  show merona t content
  ln "So... if the case is that we're going to be planting yander, we should get started on that right away."

  show boyen content
  show lexan content
  show rett smirk
  show merona t content OM
  mk "If it's okay with everyone, could I be the one handling the planting?"

  show boyen grin CE
  show lexan content CE
  show duran t content
  show merona t grin
  "Everyone nodded, and Boyen snorted."

  show kreita grin
  show lexan content
  show boyen happy
  show merona t sadSmile
  bg "You are our only person here who's specialty is working with plant life forms, so trust that you'll be expected to work on it."

  show kreita grin2
  show rett grin
  show duran t annoyed
  show merona t grin
  bg "Unless you want me to. Because I could probably cook up a mean dish with it once done. Maybe sautée some of that monster fish and garnish it with yander."

  show boyen grin
  show lexan surprised
  show rett neutral
  show merona t surprised
  "Duran's stomach rumbled in eager response."

  show kreita grin
  show lexan grin
  show boyen grin CE
  show rett content
  show duran t annoyed OM
  show merona t grin
  dt "I think I was already waiting for you to do that."

  show kreita content
  show lexan content
  show boyen content
  show duran t neutral
  show merona t content
  ck "Haha, yes. Well, I guess it is settled. We got some things accomplished out of this, so I am glad we did this. Oh, and everyone, please do not forget to keep an eye or two on any possible yander along the way. Perhaps we have been negligent with observing."

  show lexan determined OM
  ln "Yes, being more aware of our surroundings is going to be important. Let's all be more attentive in general now for the sake of our safety and well-being."
  return
  #-----------------------------------------------
label lbl_PathA_6_1:
  

  #scene cg town #(from before)
  #TODO [Positions from before
  show kreita neutral behind rett
  show lexan content
  show boyen content
  show rett content OM
  show duran t neutral
  show merona t content
  $ renpy.transition(slow_dissolve, layer="master")
  #TODO [fade in wagon in front of Rett
  show wagon:
    yalign 1.0
    xalign -0.4
  rt "Onward!"

  play music music_Travel_Light
  #TODO [move wagon in front of Kreita
  show rett content OM behind kreita
  show wagon:
    yalign 1.0
    xalign 0.0
  show kreita worried:
    yalign 1.0
    xalign 0.6
  show rett content
  "Rett grabbed hold of the cart handles but halted from moving when Kreita nudged him."

  show kreita worried OM
  show lexan serious
  show boyen worried
  show rett neutral
  show duran t worried
  show merona t worried
  kh "You sure your arms aren't gonna get sore?"

  show kreita serious OM
  show rett surprised
  kh "You should let me help you a bit."

  show kreita serious
  show rett worried OM
  rt "I can walk just fine... Or, I think I can. But eh, it's for the best."

  show kreita weakWink
  show rett worried
  show merona t sadSmile
  "Kreita winked and gave a weak smile."

  show kreita weakWink OM
  show lexan sadSmile
  show boyen content
  show rett sadSmile
  show duran t nervous
  show merona t content
  kh "I've always got your back. Or actually, I've always got your arms-and not in the amputated way."

  show kreita content
  show lexan surprised
  show boyen grin
  show rett smirk
  show duran t nervous OM
  show merona t grin
  dt "Let's not talk about any more cut off limbs, please... I'm a delicate boy who can only handle so much."

  show kreita grin2
  show lexan content
  show duran t nervous
  mi "More like as delicate as that look you always have on your face. Which is pretty solid from being there all the time."

  show rett neutral
  show boyen content
  show duran t neutral
  #TODO [start everyone's walking animation
  
  show kreita grin2 at walkBounce
  show lexan content at walkBounce
  show duran t nervous at walkBounce
  show rett neutral at walkBounce
  show boyen content at walkBounce
  show duran t neutral at walkBounce
  show merona t grin at walkBounce
  
  pause(1.5)
  $ renpy.transition(slow_dissolve, layer="master")
  hide kreita
  hide rett
  hide wagon
  show cg forest24

  play music music_meronatheme
  show duran t neutral:
    yalign 1.0
    xalign 0.6
  show duran t neutral at walkBounce
  show merona t grin:
    linear 0.5 xalign 0.8
  pause(0.5)
  show merona t grin:
    linear 0.5 xalign 0.90
  pause(0.5)
  show merona t grin at walkBounce
  #TODO [Move Merona's sprite towards Duran's #(until they lightly "touch") and back once
  "Kreita and Rett ignored him and started ahead, the rest of us trailing behind like ducklings following the mama duck as usual. I hung around with Duran and lightly \"bodyslammed\" him."

  $ renpy.transition(slow_dissolve, layer="master")
  hide lexan
  hide boyen
  show duran t tired
  show merona t happy
  mk "Hey!"

  show duran t tired OM
  show merona t content
  dt "What?"

  show duran t annoyed
  show merona t grin
  "I shrugged and grinned."

  show merona t happy
  mk "Just saying hi."

  show duran t annoyed OM
  show merona t content
  dt "Okay... Anything else you wanted?"

  show duran t annoyed
  show merona t serious
  mi "Does somebody always have to want something when they seek someone to speak to? I suppose I am wanting conversation though..."

  show merona t serious OM
  mk "Well, uh..."

  show duran t annoyed CE
  show merona t content OM
  mk "Talking."

  show duran t annoyed OM S
  show merona t content
  dt "That's what we're doing right now. Good enough for you?"

  show duran t annoyed
  show merona t happy
  mk "*laugh* I appreciate your concern. And actually, no. Not good enough for me!"

  show merona t content
  "Duran gave me the side eye combined with a tightly closed mouth."

  show duran t annoyed OM
  show merona t grin
  dt "I was hoping you'd feel awkward and stop talking to me."

  play music music_Dark_Red_Wine
  show duran t neutral
  show merona t determinedGrin OM
  mk "Well, I remember you saying that you didn't mind talking to me! Remember? When we were walking around looking for the preservationist?"

  show duran t surprised
  mk "I remember that pretty clearly, and you're going to have to honor your words."

  show duran t nervous
  mk "You're a delicate, well-mannered boy are you not?"

  show merona t determinedGrin
  dt "..."

  show duran t tired OM
  show merona t grin
  "Duran blew out the air inside him and sagged like a droopy flower stem."

  dt "Okay, I give you credit for remembering that."

  show duran t annoyed OM
  show merona t disappointed
  dt "Maybe I should talk even less now."

  show duran t surprised
  show merona t determined CE:#; quickly move her sprite towards Duran's and back once
    linear 0.5 xalign 0.8
  pause(0.3)
  show merona t determined CE:
    linear 0.5 xalign 0.9
  "I bonked my head on his, wincing at the slight impact."

  show duran t angry
  show merona t disappointed OM at walkBounce
  mk "Oh come on, don't stop now that you've started! Keep talking, and I'll keep listening."

  play music music_Pilot_Error
  show merona t disappointed
  "Duran rubbed the spot on his scalp that I clunked and crossed his arms. He shook his head."

  show duran t sad OM
  show merona t serious
  dt "Meh. The crap that comes out of my mouth may not be worth listening to, but whatever keeps you afloat."

  show duran t annoyed OM
  show merona t surprised
  dt "By the way, that was me telling you not to talk to me that much. You didn't get it the first time after all."

  show duran t tired
  show merona t determinedGrin OM
  mk "Oh, but I'm still floating. As buoyant as a boat on a lake. And hey, even if I misunderstand, that'll make me try talking to you even more!"

  return
  #-----------------------------------------------
label lbl_PathA_6_2:
  

  #play music music_Pilot_Error #(from before)
  #scene cg to forest24 #(from before)
  #TODO [Positions from before
  show duran t tired OM
  show merona t determinedGrin
  dt "Well, if that's how it's going to be..."

  stop music fadeout 1.0
  show duran t neutral
  show merona t content
  "He straightened himself up and looked ahead."

  play music music_Radio_Martini
  show duran t neutral OM
  dt "Fine. What do you want to talk about?"

  show duran t neutral
  show merona t surprised OM
  mk "Well..."

  show merona t worried
  mi "I was hoping that you would be the one to bring up a conversation topic since you suggested this chat in the first place, so I don't have any ideas lingering in my head."

  show duran t tired
  show merona t determinedGrin
  mi "You know what? I don't even need a topic. Let's improvise this, Merona. You're a talented girl. I'm sure that you can act just as well as you breath!"

  show merona t content OM
  mk "Uh...How's life so far?"

  show merona t disappointed
  "Duran side eyed me with a dull expression. I mentally shook myself."

  show duran t tired OM
  show merona t serious
  dt "That's a deep question."

  show duran t nervous OM
  dt "Do you want a deep answer or a normal one?"

  play music music_life
  show duran t nervous
  show merona t content
  "I sheepishly smiled to the sky."

  show duran t neutral
  show merona t content OM
  mk "Normal one is good with me. Unless you want to get all deep and philosophical. Then by all means, bring out your inner emotions."

  show merona t content
  dt "..."

  show duran t neutral OM
  show merona t grin
  dt "Normal answer it is."

  show merona t content
  dt "Life has been alright. Decent. Definitely better right now since it's summer break."

  show duran t neutral
  show merona t content OM
  mk "Do you usually stay here or go home during the summer?"

  show merona t content
  "He shrugged and crossed his arms."

  show duran t neutral OM
  dt "It varies. Before, I went home more often, but now I pretty much stay at school all year round unless they kick me out during the holidays. We've got summer work to do anyways, so it's easier to do it in the Academy's facilities."

  show duran t neutral
  show merona t happy
  mk "Good point. I wish I could go home more often, but it's more convenient to stay on campus as much as you can. Especially because of my ability. I can just use the school's plants for practice and work."

  return
  #-----------------------------------------------
label lbl_PathA_6_3:
  

  play music music_Sugar_On_My_Tongue
  #scene cg to forest24 #(from before)
  #TODO [Positions from before
  show duran t neutral OM
  show merona t serious
  dt "Oh yeah, that's how you first got attacked by the monster, right? You were collecting plants and then boom-monster."

  show duran t neutral
  show merona t worried CE
  "I nodded and sighed."

  show merona t sadSmile OM
  mk "That's a good short version description of what happened. Though I wasn't exactly collecting plants first, I was talking to trees."

  show duran t annoyed
  show merona t surprised
  "A scowling Duran rolled his eyes at me as we kept walking forward."

  play music music_Pilot_Error
  show duran t annoyed OM
  show merona t shocked
  dt "Oh how unique for you to do that, you snowflake. What did you do afterwards? Apologetically dance with a daisy you almost stepped on?"

  show duran t annoyed
  show merona t determined OM
  mk "Don't deny the possibility of plants and animals with linguistic capabilities, Duran! If people can communicate the way we do, I have faith that other life forms have their own secret language too."

  show duran t evilGrin OM
  show merona t determined
  dt "So you're saying that you want to crack the mystery and become a tulip whisperer?"

  show duran t annoyed
  show merona t determined OM
  mk "Number one: there are plants other than flowers that exist. Number two: Yes to cracking the mystery. And number three: the official term for me would be a translator."

  show duran t annoyed OM
  show merona t disappointed
  dt "You really go all out with your 'specialness' don't you? If you're going to become a flower translator, then I might as well be a walking bomb."

  show duran t annoyed
  mi "He still doesn't get past the flower part of this, but at least he accepted calling the role a translator..."

  play music music_Soporific
  show merona t determined
  mi "I need a good comeback to throw at him now."

  show duran t neutral
  show merona t determined OM
  mk "A walking bomb..."

  show duran t angry
  show merona t laugh
  mk "...*laugh* Honestly that sounds more plausible than a flora and fauna translator. You could explode from setting yourself on fire, from your poor digestion of Boyen's beans, or even from the build up of the vexing angst in your disgruntled heart."

  show duran t evilGrin OM
  show merona t determined
  dt "If you used that beautiful vocabulary in your class essays, I'm sure that you wouldn't even need this journey. The masters would make you go into a career as a nanny who teaches babies basic language since that's the extent of your words."

  show duran t evilGrin
  "I scoffed. My eye twitched for a moment, and I frowned, feeling less playful."

  show duran t flabber
  show merona t determined OM
  mk "Perhaps if you could actually try to be a good person, maybe you'll befriend some of those tulips I'll whisper to. I mean, it'd be a miracle seeing how you can't get a single human as a buddy."

  show merona t determined
  dt "..."

  show duran t annoyed
  "Duran gave me more side-eye combined with a straight-lined mouth. I held my breath. He kept looking at my face as if he was examining it."

  mi "I'm both excited and apprehensive about what's going to come out of his mouth now. He can take his time thinking of what to say in order to top my words."

  show duran t annoyed OM
  dt "You know..."

  stop music
  show merona t desperate
  dt "You're not pretty enough to be this idiotic."

  show duran t annoyed
  show merona t angry
  "I furrowed my brows and glared at him."

  play music music_Words_Fall_Apart
  show duran t neutral
  show merona t angry OM
  mk "Wow, what a harsh comment."

  show merona t angry
  "I can't help but retort back so quickly. This boy says a lot of rude things, but this one thing is making me more annoyed than usual, and I can't brush it off for some reason..."

  show duran t nervous
  show merona t determined OM
  mk "First off, that's low to imply that pretty people are idiots and that how smart you are is based off of your looks."

  show duran t surprised
  mk "I don't care if you think I'm pretty or not, but there's no need to be all nasty against others who you think are stupid. I mean, you're not exactly ugly, and I wouldn't consider you to be an idiot, though you can be a fool quite often..."

  show merona t determined
  mi "I'm not sure why I'm getting so huffy over specifically this. Duran has been grinding my gears over the past few weeks, but perhaps this push was the one that made the gear come loose."

  show duran t nervous
  mi "After all, it's true that one can only take so much of anything, even medicine, before it becomes a poison. I'm not saying that Duran is my medicine, but I can only take so much of lackluster comments before I want to burn them away."

  show duran t annoyed S
  show merona t nervous
  "Now the scowl transferred to my lips, and Duran only squinted at me with a half-confused and half-irritated face."

  show merona t serious
  mi "Ah. Now that should be what I would call a \"Duran face\"."

  show duran t neutral OM
  dt "I appreciate that you think that I'm decent-looking, but slow down and stop jumping to conclusions for at least two and a half seconds."

  show duran t nervous OM
  show merona t nervous
  dt "I didn't think you'd get so riled up over that. Maybe I should have said something else... But I still feel like you'd jump down my throat over it."

  show duran t nervous
  show merona t nervous OM
  mk "There's a degree of how much you like to rouse up someone? I guess I should be thankful that you have the decency to consider that."

  play music music_Revolution_Now
  show duran t confused
  show merona t surprised
  "Duran's face got rid of its irritation and became a full-on confused one."

  show duran t confused OM
  show merona t serious
  dt "Merona... You're acting strange. Did you accidentally eat some poison berries? Did they change your personality?"

  show duran t smirk
  "But suddenly, his face shifted into a slight smirk."

  show duran t smirk OM
  show merona t disappointed
  dt "Or did the berries tell you to act like this in your conversation?"

  show duran t bored
  show merona t determinedGrin OM
  mk "Don't make me place poison ivy leaves in your sleeping blankets, Duran. And when the itching, bumps, and pus comes, I won't let Cimaria treat you."

  return
  #-----------------------------------------------
label lbl_PathA_6_4:
  

  play music music_Sovereign
  #scene cg to forest24 #(from before)
  #TODO [Positions from before
  show duran t bored OM
  show merona t serious
  dt "So this is your idea of what a good conversation is like? Wow, maybe we should take a little break so that we can save our energy for the next one."

  show duran t bored
  show merona t disappointed
  "I rolled my eyes and sighed. I certainly wasn't going to let it end with that."

  show duran t neutral
  show merona t determined OM
  mk "Look, let's refocus and start another subject. I know you find my ideas ridiculous, and well... a lot of other people would too, but you don't need to get all in my face about it!"

  show merona t serious OM
  mk "Just let me go on with my thoughts without blocking my way, and I'll give you the same treatment."

  show merona t serious
  mi "There. That provides room for closure."

  show duran t tired
  "Duran looked down at the ground and kicked a rock out of his way. My eyes followed it, the stone skipping over to the edge of the path-thankfully not tripping anyone in front of us too."

  show duran t tired OM
  show merona t surprised
  dt "Psh. Whatever works for you, I guess. I don't think it's really wrong to blow off steam."

  show duran t neutral
  show merona t serious OM
  mk "Blowing off steam is fine, but I'm just saying that it'd be better if we were just nicer to each other. Not try insulting each other out of the blue."

  show duran t annoyed
  show merona t serious
  "He shrugged and crossed his arms."

  show duran t annoyed OM
  show merona t worried
  dt "I suppose so, but you were the one who actually ended up imploding a little. Nice job at it too, for someone who doesn't get like that easily."

  stop music fadeout 1.0
  show duran t annoyed
  show merona t determined OM
  mk "Yeah, yeah, yeah, I get it. Let's talk about something else then. I'm not going to suddenly start yelling at you again."

  show duran t neutral
  show merona t determinedGrin
  mi "Or at the very least, I will try not to do that in the near future. No guarantees."

  play music music_Radio_Martini
  show duran t bored OM
  show merona t surprised
  dt "You're kind of boring if you don't get angry. Feel free to rant to me if you want, because I'd rather listen to you do that rather than your plant conversations."

  show duran t bored
  show merona t disappointed
  mi "I'm not that boring, am I? I mean, I would consider talking to plants a fun fact about myself, but then again, this is Duran I'm dealing with."

  show duran t neutral
  show merona t disappointed OM
  mk "Eh, if you insist. I'm not welcoming you to do the same to me though; I've pretty much only seen an annoyed Duran most of the time, so feel free to do something new once in a while."

  show merona t serious
  "He looked at me from the corner of his eyes, a passive expression on his face."

  show duran t tired OM
  show merona t worried
  dt "You're getting the most authentic me right now. But since you did say that you wanted another, I'll give in to you a little, unless you want to cut this chat right now."

  show duran t neutral
  show merona t worried CE
  "I furiously shook my head like a dog wringing water from its fur."

  show merona t determined OM
  mk "We're on a roll here. We don't really talk that much in general, so I want to get to know you a little better. It's already been a few weeks, but there's still not much I know about you or everyone else frankly!"

  show duran t sad OM
  show merona t surprised
  dt "What you're getting right now is basically all there is to me. What's the use of knowing other little facts? Do you really need to know things like my birthday? Or my favorite color?"

  return
  #-----------------------------------------------
label lbl_PathA_6_5:
  

  #play music music_Radio_Martini #(from before)
  #scene cg to forest24 #(from before)
  #TODO [Positions from before
  show duran t sad
  show merona t surprised OM
  mk "I think there's more to Duran than just what I'm getting. No need for fun facts about yourself, but you must have something major that I don't know about you!"

  show duran t annoyed
  show merona t nervous
  "Duran crossed his arms and shook his head. I could almost feel his exasperation pushing me away."

  play music music_piano
  show duran t annoyed OM
  show merona t surprised
  dt "Merona, I don't know how many times I have to tell you-you're getting the whole package. And that should be enough."

  show duran t surprised
  "He raised his eyebrows, boring his eyes into mine."

  show duran t evilGrin OM
  show merona t determined
  dt "If you really considered me a true friend, you should respect my choice not to say anything more. Because we're best friends, right?"

  show duran t evilGrin
  mi "Oh, wipe that smirk off your face, Duran. I don't need your sass."

  show merona t determined OM
  mk "Fine, fine, fine. Since we're obviously best friends for life, I'll stop asking."

  show duran t annoyed
  show merona t determinedGrin OM
  mk "For now."

  show merona t grin
  "I snickered and flashed him an exaggerated grin."

  show duran t annoyed CE
  show merona t happy
  mk "Maybe I'll ask again tomorrow..."

  show merona t grin
  mi "You can never get enough of our conversations!"

  play music music_Travel_Light
  show duran t tired
  "Duran peered at me through half-lidded eyes."

  show duran t tired OM
  show merona t serious
  dt "'Kay. You good now? We're done here?"

  show duran t annoyed
  show merona t determinedGrin OM
  mk "...What do you think?"

  show merona t determinedGrin
  "He rolled his eyes."

  show duran t annoyed OM
  show merona t content
  dt "Okay, what else do you want to talk about?"

  show duran t neutral
  show merona t reflective
  mk "..."

  show duran t annoyed
  dt "..."

  show merona t nervous
  mi "I still would like to talk with him... But now I'm blanking out on what to say."

  show duran t tired CE
  dt "..."

  show duran t neutral OM
  show merona t surprised
  dt "How about I learn a little bit about you then."

  play music music_She_dreams_in_blue
  show duran t neutral
  show merona t sad
  "I squinted at him, wondering if he was playing around or not. His face looked a little more agitated, but it seemed like he wasn't joking."

  show merona t content OM
  mk "What... do you wanna know?"

  show duran t neutral OM
  show merona t content
  dt "Well, tell me what I need to know."

  show duran t neutral
  "I slightly smiled as he looked away from me to the road ahead."

  mi "You're definitely getting \"the most authentic me\"."

  show merona t sadSmile
  mi "But thanks for asking."

  show merona t serious OM
  mk "Well, I'm sixteen and have a plant and animal manipulation ability."

  show duran t bored
  show merona t content OM
  mk "I've been going to the academy for almost three years now."

  show merona t happy
  mk "I'm from the town Rillonine, and my parents own a farm."

  show duran t tired
  mk "And I hope that I ca-"

  show duran t angry OM
  show merona t surprised
  dt "Okay, I already know most of that stuff about you. Isn't there anything else?"

  play music music_life
  show duran t angry
  show merona t determinedGrin behind duran:#; move Merona's sprite next to Duran's #(slightly overlapping)
    xalign 0.8
  show merona t determinedGrin at walkBounce
  "I patted the air above his shoulder."

  show duran t angry CE
  show merona t determinedGrin OM
  mk "Patience, young pupil. I need to lay out the foundation to the story before diving into the extra details."

  show duran t angry
  show merona t determinedGrin
  "He frowned, staring at my hovering hand. I smiled."

  show duran t annoyed
  show merona t laugh
  mk "Isn't this is okay with your terms? No touching. See? I remembered."

  show duran t embarrassed OM
  show merona t grin
  dt "Oh yeah. Uh..."

  show duran t embarrassed
  "He looked down at the ground, and his cheeks reddened."

  show duran t angryBlush OM
  dt "You're fine."

  show duran t angryBlush
  show merona t grin CE
  "I chuckled to myself and straightened my posture even more."

  show duran t neutral
  show merona t content OM:#; move her back to the position before
    xalign 0.9
  show merona t determinedGrin at walkBounce
  mk "Moving on..."

  return
  #-----------------------------------------------
label lbl_PathA_6_6:
  
  play music music_life
  #scene cg to forest24 #(from before)
  #TODO [Positions from before
  show duran t neutral
  show merona t content OM
  mk "I've lived in Rillonine for practically my entire life before moving to the academy in Laneo, and I'm probably going back there once I graduate. Got plans in store for myself."

  play music music_Words
  show duran t neutral OM
  show merona t content
  dt "Does it have to do with the farm you live on? I mean, that's probably all that's going for you over there. Will you become the next landholder or something like that?"

  show duran t neutral
  show merona t reflective
  "Shrugging, I crossed my arms and kicked away a stone."

  show merona t serious OM
  mk "Maybe. My parents and I decided that I should go to the academy so that I could learn a thing or two about my ability for the sake of helping them out. There's no opportunity for a high-quality education in Rillonine like there is in Laneo after all."

  show duran t tired
  show merona t content OM
  mk "You also board at the academy, right? Where do you come from?"

  show duran t annoyed OM
  show merona t content
  dt "Actually, I'm from Laneo. Family lives there too."

  show duran t annoyed
  show merona t surprised OM
  mk "Oh? You don't have to live in the dorms then. You could just commute to your classes from home."

  show duran t annoyed OM
  show merona t serious
  "Duran grimaced and sighed, rolling his eyes at the same time."

  play music music_Ill_be_right_behind_you_Josephine
  show duran t annoyed
  show merona t sadSmile
  mi "Wow. I managed to make him do all three of his favorite things at the same time."

  show duran t annoyed OM
  show merona t serious
  dt "Not the first time I've heard that."

  dt "It's my choice to stay at the academy, okay? Being there all the time is easier to deal with, and it's not like I can't afford to do so either."

  show duran t annoyed
  show merona t serious OM
  mk "Alright, alright, no need to get up in my face about it. Whatever works for you, I suppose."

  show merona t serious
  "I paused, wondering if I should go on asking about his living situation."

  show merona t determined
  mi "Just one more question. And if he becomes even more irked, no more pestering him about it."

  show duran t neutral
  show merona t serious OM
  mk "So... if you do live in the dorms, do you see your family a lot?"

  show duran t neutral OM
  show merona t surprised
  dt "Define 'a lot'."

  show duran t neutral
  show merona t surprised OM
  mk "At least once a week?"

  show duran t neutral CE
  show merona t serious
  "He shook his head, but he didn't seem so sour anymore."

  show duran t neutral OM
  dt "Naw. I usually visit them once every month or so, but that's still more often than any others who come from other towns. It's like a check-in, I guess. My mother and father don't pester me to see them more often, and we're all fine with how that is."

  show duran t neutral
  show merona t reflective
  mi "Interesting. He's not very close to his parents, and they aren't too crazy about him either. Sometimes I wish my parents could be more like that though-their urgings for me to come home more have declined, but dealing with them was quite tiresome when I first came to Laneo."

  show duran t bored
  show merona t content OM
  mk "I see. Do you have any siblings then? Any mini, big, or female versions of Duran?"

  show duran t bored OM
  show merona t content
  dt "There's only one Duran in this world. No variations."

  show duran t neutral
  show merona t grin
  "I stuck my hands on my hips and grinned."

  play music music_White
  show merona t laugh
  mk "Hey, that's something we have in common! There's only one Merona in this world too. Imagine if we had twins of ourselves though. I couldn't handle double the Duran at once."

  show duran t evilGrin
  show merona t happy
  mk "With double the Duran though, there'd be much more chances for me to have nice talks!"

  show duran t evilGrin OM
  show merona t sadSmile
  dt "If there were two of you, I would have most likely made the second one magically 'disappear'."

  show duran t evilGrin
  show merona t angry
  "In exaggerated disappointment, I huffed and scowled."

  show duran t neutral
  show merona t angry OM
  mk "Aw, come on, don't burn my hypothetical twin sister into ashes and hide her remains in the woods! Not cool."

  show duran t nervous
  show merona t serious
  "Duran held up a hand, stopping me from saying anything else."

  show duran t nervous OM
  show merona t sadSmile
  dt "Okay, our conversation has been going on long enough now. You should be happy with all that's been said, right? I don't think I can drag it on any longer."

  show duran t nervous
  show merona t grin
  mi "To be honest, it wasn't a bad chat! I fished out some new information, and he learned a little more about me."

  mi "Sure there's more that I'd like to know, but for now, things are looking good."

  play music music_life
  show duran t neutral
  show merona t happy
  mk "If you say so, Duran. Thanks for a decent talk though! I'm always here if you want to tell me more about yourself!"

  show duran t evilGrin
  show merona t grin
  "He lightly punched my upper arm and scoffed."

  show duran t evilGrin OM
  dt "Yeah, I'll go to you if I feel like it."

  show duran t evilGrin
  show merona t determinedGrin
  mi "Duran! If you hit me, I should be able to hit you. Let's make this fair."

  show duran t nervous CE
  "I smirked as I thumped him on top of his head. He closed his eyes, pursing his lips."
  
  show duran t surprised
  show merona t grin
  mi "That was a light knock on your cranium. Don't even pretend that it hurt you in the slightest. "

  show duran t confused OM CE
  dt "...Thanks."

  play music music_romance
  show duran t confused CE
  show merona t happy
  mk "*laugh* Gotta get you back for that little punch. Am I allowed to have physical contact with you again?"

  show duran t content
  show merona t content
  "With his eyes still closed, he tried stifling a laugh, but he couldn't hide the smile twitching on his lips."

  show duran t content OM
  show merona t grin
  dt "Uh... sure."

  show duran t content
  show merona t blushSmile OM
  mk "Great!"

  $ renpy.transition(slow_dissolve, layer="master")
  scene cg MeronaDuranCuddle
  "I swung my arm around his shoulder and quickly squished my face against his cheek."

  mi "There might not be another opportunity, so I have to take advantage of this for a sneak attack hug! It's not like he's going to be flinging himself at me anytime soon."

  dt "Whoa, whoa, whoa, what are you doing!?"

  mk "Celebratory side-hug. The speedy version."

  play music music_Cool_Steel_Breeze
  #TODO [fade to...
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest24 #(from before)
  #TODO [Positions from before
  show duran t embarrassed:
    yalign 1.0
    xalign 0.75
  show merona t happy:
    yalign 1.0
    xalign 1.0
    
  show duran t embarrassed at walkBounce
  show merona t happy at walkBounce
  mk "*laugh* I figured that it'd be best to do it quickly before you'd realize what was happening, so I went for it. And look! You're still all in one piece."

  show duran t content CE
  show merona t surprised
  "Duran looked at me for a moment, but to my surprise, he started chuckling to himself."

  show duran t content OM
  show merona t content
  "It felt... almost natural. Like this was how he'd usually laugh, if he did usually laugh in front of me."

  show merona t grin CE
  "His chuckles spread to me, and my lips couldn't help turning up too. "

  show duran t content OM CE
  show merona t happy
  "Perhaps I should give more surprise celebratory side-hugs."
  
  scene bg black with fade
  return
  #-----------------------------------------------
label lbl_PathA_6_8_o:
  
  return
  #-----------------------------------------------
label lbl_PathA_6_8:
  

  play music music_Sugar_On_My_Tongue
  show cimaria neutral
  "Duran shrugged."

  show duran t neutral OM
  dt "Doesn't feel like much has changed. I remember how it felt when we first got it, and I just touched it two days ago when I was looking for a pen in Merona's bag."

  show kreita serious
  show merona t serious
  show duran t nervous OM
  show cimaria serious
  dt "Maybe... the body isn't as firm as it originally was? It's more mushy."

  show duran t nervous
  $ renpy.transition(slow_dissolve, layer="master")
  show prowen serious behind rett:#; right from Rett
    yalign 1.0
    xalign 0.98
  show prowen serious at walkBounce
  "Prowen pursed his lips."

  show kreita pouty
  show merona t nervous
  show rett sceptical
  show prowen serious OM
  pm "Not a good sign... it's probably on its way to decomposing then."

  show merona t nervous OM
  show prowen serious
  mk "Yeah, sounds like what's going on. Or I'm just overthinking it."

  show kreita content
  show merona t content
  show duran t surprised
  show cimaria neutral
  show rett content OM
  show prowen sceptical
  rt "There's no pungent stench coming from it, so it's fine."

  show kreita serious
  show merona t disappointed
  show duran t neutral
  show cimaria serious
  show rett neutral
  show prowen sceptical OM
  pm "Fine for now. The stench can come later."

  show kreita grin
  show merona t shocked
  show duran t evilGrin OM
  show rett smirk
  show prowen forcedSmile
  dt "It's convenient that Merona is carrying it in her bag. She'll be the first to know when it starts!"
  return
  #-----------------------------------------------
label lbl_PathA_6_9:
  

  play music music_life
  #scene cg forest25 #(from before)
  #(Positions as in last chapter)
  show kreita grin2
  show wagon
  show merona t disappointed OM
  show duran t evilGrin
  show cimaria serious
  show rett smirk
  show prowen forcedSmile
  mk "Geez, thanks Duran. I'll make sure to let you have some alone time with the monster once the smell kicks in because then you'll be on the same level with it."

  show kreita laugh
  show merona t disappointed
  show duran t content
  show prowen neutral
  kh "Oooh, Merona's getting testy over here! But everything seems to be okay... Hopefully there won't be demons on their way to attack us."

  show kreita grin
  show merona t nervous
  show duran t neutral
  show rett content
  pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")
  hide rett
  hide prowen
  mi "The only demon here is the fish odor. I suppose we will forget about it, but that means we'll smell like musty fish as well..."

  show kreita content
  show merona t surprised
  show duran t sad OM
  show cimaria neutral
  dt "I just wish we could find a resting place soon. I mean, we all don't want to continue walking for the fourth day in a row, right? We could end up dying from exhaustion."

  show merona t grin
  show duran t angry
  "I rolled my eyes and punched his shoulder."

  play music music_Dark_Red_Wine
  show kreita fierce
  show merona t laugh
  show duran t annoyed
  show cimaria worried
  mk "If you can handle an entire night of lighting our path with your fire, then you can definitely walk for a few more days. Besides, it's not like it'll stunt your growth."

  show merona t surprised
  show duran t annoyed OM
  dt "Actually, it does! I'm losing precious sleep. People grow more when they sleep more! If I'm not taller than every single one of you later on, then I'm blaming this trip."

  show kreita content
  show merona t determinedGrin OM
  show duran t surprised
  show cimaria neutral
  mk "Hey, at least in exchange for a few centimeters, you get people to hang out with."

  show kreita grin
  show merona t happy
  show duran t flabber
  show cimaria sadSmile
  mk "People whom you can call 'friends'."

  show merona t grin
  show duran t annoyed CE
  "He shook his head."

  show kreita content
  show merona t sadSmile
  show duran t nervous OM
  dt "Tch. That's so cheesy, but I'm glad you're the one who said it, and not me."

  show duran t nervous
  show cimaria neutral
  mi "Cheese is so delicious though!"

  show merona t laugh
  show cimaria serious
  mi "I'll happily say anything, especially if it has extra cheese on it. Who doesn't love extra cheese?"
  return
  #-----------------------------------------------
  
  
  
  #-----------------------------------------------
  # CHAPTER 7
  #-----------------------------------------------
label lbl_PathA_7_4:

  show merona t worried
  mi "It was alright a few days ago, but it did seem mushier. "

  show merona t serious
  "One way to find out now."

  show kreita neutral
  show duran t neutral
  show cimaria serious
  show rett neutral
  show boyen surprised
  show lexan neutral
  "I swung my bag around and grabbed the monster's pouch. Feeling the cloth from the outside, I cringed at how easily I could press into the flesh."

  show merona t shocked
  mi "Oh boy."

  play music music_SoT
  show merona t serious
  mi "I'm kind of scared now."

  show kreita sceptical
  show duran t nervous
  show cimaria shocked
  show rett sceptical
  show boyen sceptical
  show lexan serious
  "I drew the bag away from me and slowly allowed it to fully open. As the odor escaped its confines, I could almost see it flow out into the air and overtake our noses."

  show kreita pouty
  show merona t sadSmile
  "Everyone crinkled their faces and automatically covered their nose and mouth, snapping their heads towards me."

  show merona t worried
  "I reached in, and after finding the tail, I unsheathed the fish from the pouch. Almost like the decomposing fertilizer fish, chunks of the monster were also missing in some spots, but the still glassy eyes all over its body made it feel as alive as ever."

  show merona t sadSmile
  mi "My bag was really good at hiding this smell."

  play music music_Pilot_Error
  #TODO [Stop walking animations
  show kreita worried:
    yalign 1.0
  show merona t shocked:
    yalign 1.0
  show duran t flabber OM:
    yalign 1.0
  show cimaria worried:
    yalign 1.0
  show rett surprised:
    yalign 1.0
  show boyen surprised:
    yalign 1.0
  show lexan surprised:
    yalign 1.0
  dt "Ahhh!"

  show merona t shocked OM
  show duran t flabber
  show rett confused
  show boyen scared
  show lexan shocked
  "Duran shot his hand out and blasted a stream of flames at the monster. I shrieked and threw the monster out in the air, quickly pulling in my arm. It fell apart and burst upon coming into contact with the ground."

  show kreita sceptical
  show rett worried
  mk "Duran! What was that for?"

  show merona t nervous
  show duran t flabber OM
  show cimaria serious
  show boyen worried
  show lexan serious
  dt "I-I got freaked out by that thing!"

  show merona t serious
  show duran t nervous OM
  show lexan neutral
  dt "I couldn't help it... My hand just..."

  play music music_piano
  show kreita worried
  show duran t sad
  "His face fell, and he looked down at the ground."

  show duran t embarrassed OM
  show cimaria neutral
  show rett neutral
  dt "I... I'm sorry, Merona."

  show merona t surprised
  show duran t embarrassed
  "His eyes flicked up at me again, under his eyelashes."

  show duran t sad OM
  show rett worried
  show lexan worried
  dt "You... you're not hurt, are you?"

  show merona t serious
  show duran t worried OM
  show cimaria serious
  dt "Did I burn you?"

  return
  #(Continued in 7.5)
  #"A7.5"
  #TODO [FINAL


label lbl_PathA_7_5:

  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. A path's storyline is red. B path's storyline is blue. C path's storyline is green. If two paths share the same text, it will be in pink."
  #"-----------------------------------------------------------"
  #(Continuation of 7.4)

  #play music music_piano #(from before)
  #scene cg forest26 b #(from before)
  ##(Positions from before...)
  show kreita worried#; center
  show wagon#; center
  #
  show merona t serious#; left from Kreita
  show duran t worried#; left from Merona
  show cimaria serious#; left from Duran
  #
  show rett worried#; right from Kreita
  show boyen worried#; right from Rett
  show lexan worried#; right from Boyen
  #
  #show rain movie#animation #(from before)
  "I flexed my fingers and pulled off the glove."

  show kreita neutral
  show merona t content OM
  show cimaria neutral CE
  show rett content
  show boyen content
  show lexan content
  mk "I'm fine. Don't worry about me."



  play music music_Soporific
  show kreita sad
  show merona t nervous OM
  show duran t nervous
  show cimaria neutral
  show rett neutral
  show boyen sceptical
  show lexan serious
  mk "The monster however..."

  show merona t nervous
  "I stared down at the charred remnants of our former companion. Only the skeleton remained, with bits of flesh still clinging on for dear life."

  show kreita content
  show merona t sadSmile
  show duran t neutral
  show cimaria sadSmile
  show rett laugh
  show boyen content
  show lexan neutral
  rt "Well, I guess you could say that my assailant has gotten vengeance."

  show kreita neutral
  show merona t serious
  show duran t worried OM
  show cimaria neutral
  show rett worried
  show boyen neutral
  dt "Ugh... I..."

  show duran t worried
  "Duran's eyes stuck to the ground. For once, his face seemed to crumble into actual regret."

  show merona t worried
  show duran t worried CE
  mi "It feels weird to see him emote something other than his usual faces, but I don't like his current expression, nor do I want it to stay."

  show kreita content
  show merona t serious
  show duran t sad OM
  show cimaria gentle
  show rett smirk
  show boyen content
  show lexan sadSmile
  dt "Sorry..."

  play music music_Cool_Steel_Breeze
  show merona t content OM
  show duran t surprised
  show cimaria neutral
  show rett content
  show lexan surprised
  mk "You know what? There's a silver lining to all of this."

  show kreita grin
  show merona t happy
  show duran t nervous
  show cimaria content
  show rett grin
  show boyen grin
  show lexan content
  mk "We can use what's left of the monster as a fertilizer too. Just add it in with the rest of the fish, and there! All better."

  show merona t serious
  "Duran didn't flinch."

  show kreita content
  show merona t content
  show duran t nervous OM
  show boyen content
  dt "All better..."

  show merona t determinedGrin
  show duran t flabber
  show cimaria grin
  show rett content
  "I went over to him and bonked him on the head."

  show merona t content OM
  show duran t neutral
  mk "Yes, all better. Come on, help me pick up the pieces."

  show merona t content
  show duran t embarrassed
  show cimaria content
  "I grabbed his wrist, dragging him to a spot on the ground where a clump of monster parts landed. He stumbled along, but nonetheless didn't resist."

  show duran t embarrassed OM
  show lexan grin
  dt "*sigh* Whatever you say, Mom..."

  return
  #(Continued in 7.6)
  #"A7.6"
  #TODO [FINAL



label lbl_PathA_7_6:
  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. A path's storyline is red. B path's storyline is blue. C path's storyline is green. If two paths share the same text, it will be in pink."
  #"-----------------------------------------------------------"
  #(Continuation of 7.5)
  #play music music_Cool_Steel_Breeze #(from before)
  #scene cg forest26 b #(from before)
  ##(Positions from before...)
  show kreita content#; center
  show wagon#; center
  #
  show merona t content#; left from Kreita
  show duran t neutral#; left from Merona
  show cimaria content#; left from Duran
  #
  show rett neutral#; right from Kreita
  show boyen content#; right from Rett
  show lexan content#; right from Boyen
  #
  #show rain movie #animation #(from before)
  "We crouched down and picked up all that we could, placing the chunks into my pouch. Though the monster was now spread over, we could still collect a sizable amount of it. The random eyes distributed across the path weren't any less intimidating."

  play music music_Dark_Red_Wine
  show kreita surprised
  show merona t surprised
  show duran t surprised
  show cimaria neutral
  show rett confused
  show boyen neutral
  show lexan confused
  "Kreita gasped and flailed her arms."

  show duran t neutral
  show rett neutral
  show boyen surprised
  show lexan surprised
  kh "Ooh, I have an idea!"

  show kreita lol
  show merona t serious
  show duran t annoyed
  show cimaria content
  show rett content
  show boyen content
  show lexan content
  kh "Since the monster isn't preserved anymore, we should use it as a fertilizer!"

  kh "After all, it's also a type of fish, right?"

  show kreita grin
  show merona t sadSmile
  show duran t annoyed EL
  mi "I guess she didn't hear what I said earlier, but at least we're both thinking on the same page!"

  show merona t content
  show duran t neutral
  show cimaria content OM
  show boyen grin
  ck "That sounds like a good idea. There's nothing else we could use it for, after all..."

  show cimaria content
  show lexan content OM
  ln "Yes, I agree. This is a perfect time to place them in the soil as well, since we just added the regular fish too."

  show boyen content
  show lexan content
  "I got up and strolled over to the cart."

  show kreita content
  show merona t content OM
  show cimaria gentle
  mk "I'll plop them right in."

  show merona t content
  mi "At least we were able to repurpose the monster. There's always something you can do, even if it seems like there are no options left."
  return
  #-----------------------------------------------
  
  #-----------------------------------------------
  # CHAPTER 8
  #-----------------------------------------------
label lbl_PathA_8_4:
  
  play music music_piano
  show duran t worried
  "Duran hopped in front of me and held out both of his hands. I squinted at them, slowly registering what those two blobs were."

  show duran t worried OM
  dt "Can you see me?"

  show duran t worried
  mk "Kind of..."

  show duran t evilGrin OM
  dt "Still not sobered up?"

  show duran t content
  mk "Nope."

  show duran t blushSmile
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t serious:#, between Prowen and Duran
    xalign 0.65
    yalign 1.0
  "Sighing, he grabbed my hands and pulled me up."

  show prowen forcedSmile
  show duran t evilGrin OM
  dt "I feel like you'd be the first to pass out from actual drinking."

  show merona t sadSmile OM
  show duran t evilGrin
  mk "Well, hopefully you'll be there to clean up my barf and carry me home when it happens."

  show merona t sadSmile
  show duran t smirk OM
  dt "Tch. Guess I'll have to make sure you never get to that point..."

  show prowen serious
  show duran t worried
  "I bobbed my head up and down, trying to clear my vision. Duran let go of my hands, but I was still reeling a bit. Since Prowen was closest to me, I grabbed hold of his cape."
  
  return
  #-----------------------------------------------
label lbl_PathA_8_8_1:

  #play music music_newBegin #(from before)
  #TODO [positions as before...
  show cg forest29

  show cimaria serious CE
  show merona t sadSmile
  show rett operation
  show rain movie
  mi "The monster may have destroyed our garden, but Cimaria might have some with her!"

  show merona t serious
  "Lunging for her bag, I tore through the pouches, desperately trying to find even a single leaf of yander. No sign of it at all in any of the mini bags."

  "My hopes surged when the glare of a clear jar buried among the pouches caught my attention."

  show merona t nervous
  mi "Please, let it be..."

  show merona t sadSmile
  "Fishing it out, I sighed in relief."

  play music music_White
  mi "Yander."

  show merona t content
  mi "Not in the best shape, but still, it's yander!"
  
  return
  #-----------------------------------------------

  #-----------------------------------------------
  # CHAPTER 9
  #-----------------------------------------------
label lbl_PathA_9_3:
    
  play sound sound_footsteps
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t bored OM:#; right from Merona
    yalign 1.5
    xalign 0.8
  dt "Hey."

  play music music_piano
  show merona t surprised:#; fade back in at 200px lower position from before
    yalign 1.9
    xalign 0.5
  show duran t neutral#; move down by 200px
  "Opening my eyes, I was greeted by Duran's back slumped over his knees. He sat right next to me but facing the opposite direction."

  show merona t surprised OM
  mk "Oh, hi Duran. Need something?"

  show merona t content
  show duran t neutral OM
  dt "Do I need a reason to just be here?"

  show merona t content OM
  show duran t nervous
  mk "Well, usually you wouldn't randomly sit next to me, so I figured you did."

  show merona t serious
  show duran t embarrassed
  "He shrugged, still facing away."

  show merona t surprised
  show duran t embarrassed OM CE
  dt "I just wanted to sit here."

  show merona t content CE
  show duran t embarrassed
  "I smiled to myself and closed my eyes again."

  show merona t content OM CE
  show duran t embarrassed CE
  mk "Just sit? Nothing else?"

  show merona t content CE
  show duran t determined CE
  dt "..."

  play music music_romance
  show merona t serious CE
  show duran t determined OM
  dt "Merona... Can I ask you a question?"

  show merona t serious
  show duran t determined
  "I opened my eyes. Duran slightly turned his head towards me, but I couldn't see his face."

  show merona t surprised
  show duran t sad OM
  dt "What do you think of me?"

  show merona t surprised OM
  show duran t sad
  mk "Huh? Why do you want to know?"

  show merona t surprised
  show duran t worried OM
  dt "Just because."

  show merona t sadSmile
  show duran t confused OM
  dt "Don't answer if you don't want to."

  show merona t serious OM
  show duran t nervous
  mk "Well..."

  show merona t content OM
  show duran t flabber
  mk "I think you're a fun person to be around."

  show merona t happy
  show duran t surprised
  mk "I like being with you. I wish I could talk to you more一not just because we're the only two students here, but also since I want to get to know you better."

  show merona t content
  show duran t confused
  "Duran turned enough so that I could finally see his face, but it was hard to read his expression."

  dt "..."

  play music music_Ill_be_right_behind_you_Josephine
  show merona t surprised
  show duran t confused OM
  dt "You're too nice sometimes."

  show merona t surprised OM
  show duran t neutral
  mk "I'm just being honest."

  show merona t content OM
  show duran t embarrassed
  mk "What do you think about me?"

  show merona t content
  "He paused for a moment and stared into space."

  show merona t surprised
  show duran t embarrassed OM
  dt "Sorry."

  show merona t serious
  show duran t embarrassed
  "Sorry? For what?"

  show duran t sad OM
  dt "I know that I can be pretty rude... There's no good excuse for how I act. It's just the way I am. But I don't want to be like that."

  show merona t content
  show duran t nervous OM
  dt "Especially not to you."

  show merona t grin
  show duran t neutral OM
  dt "I think you're a really caring person, Merona. You're weird too... in a good way. Talking to trees isn't such a terrible thing."

  show merona t laugh
  show duran t blushSmile
  mk "*laugh* Thanks. Don't worry, I don't spend all my spare time talking to trees, so I'm not a complete lunatic."

  show merona t content
  show duran t blushSmile OM
  dt "Doesn't matter if you did. I think you're fine when you do what you want to do."

  show merona t happy
  show duran t neutral
  mk "Take your own advice then, Duran. If you want to be a nicer person, that won't make me run away from you either."
  #"-----------------------------------------------------------"
  #(3/7/17)
  #TODO [FINAL

  show merona t serious
  show duran t sad OM
  dt "I don't know..."

  show merona t content:
    yalign 1.0
    xalign 0.5
  show duran t nervous
  "I smiled and pushed myself up."

  show merona t content OM
  show duran t embarrassed
  mk "Well, we'll always be friends, Duran. Even if you can be a bit much at times, as long as you make an effort to be a better person, I don't mind being with you."

  show merona t content
  dt "..."

  show merona t grin
  show duran t embarrassed OM
  dt "Thanks."

  show merona t happy
  show duran t embarrassed
  mk "Of course!"

  show merona t wink
  show duran t blushSmile
  "I winked at him."

  play music music_Radio_Martini
  show merona t wink OM
  show duran t angryBlush CE
  mk "Saying 'thank you' is also another good step towards becoming nice."

  show merona t wink
  show duran t annoyed EL
  "He rolled his eyes at me."

  show merona t grin
  show duran t annoyed OM
  dt "Yeah, yeah, yeah..."

  show merona t happy
  show duran t grin
  mk "There's the Duran that I know."


  play music music_piano
  show merona t content
  show duran t content
  "Back in Laneo, I heard little snippets about \"Durian\" Trist-standoffish, genius, and pyromaniac."
  
  show merona t sadSmile
  mi "Parts of that may be true, but I'm glad that I got to know what Duran is really like."

  mi "I hope that I can get to know more about him before this journey ends."

  show merona t content#; move back up to normal Y-position please
  show duran t neutral
  "I got up and brushed off the crumbs of dirt sticking onto the backs of my thighs."

  show merona t content OM
  mk "Okay, I think I'll go back to work with Lexan."

  show merona t happy
  show duran t embarrassed:
    yalign 1.0
    xalign 0.8
  mk "Let's talk some more when we hit the road again, Duran."

  show merona t content
  show duran t blushSmile#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide duran
  "He nodded and waved me away. "

  play music music_Summer_Day
  show merona t content#; move next to L and back to center
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan neutral:#; right from M, placed at 200px lower than usually
    yalign 2.0
    xalign 0.9
  "With a small bounce in my step, I ambled over to where Lexan was and tapped his shoulder. He looked up at me from the notebook he was writing in."

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
  ln "As I was taking notes over our situation, I decided to mull over the first monster attack you faced back at the academy."
  
  return

label lbl_PathA_9_6:

  play sound sound_bump
  show merona t surprised
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t neutral:#; right from Merona
    yalign 1.0
    xalign 0.75
  show duran at walkBounce
  "Duran shuffled next to me and poked my arm."

  show merona t content
  show duran t neutral OM
  dt "Hey."

  show merona t happy
  show duran t neutral
  mk "Hey Duran. Need something?"

  show merona t serious
  show duran t sad OM
  dt "Well... I wanted to ask: what are we supposed to do when we're back at the academy?"

  show merona t serious OM
  show duran t neutral
  mk "Go back to normal life? Resume our studies? Report our findings? I don't exactly know... You should ask Lexan to be sure-he's in charge of our academic stuff, after all."

  show merona t serious
  show duran t worried OM
  dt "Yeah... Okay."

  show merona t surprised
  show duran t embarrassed OM
  dt "What about... us?"

  show merona t surprised OM
  show duran t embarrassed
  mk "As in our friendship?"

  play music music_Pride
  show merona t serious
  dt "..."

  show merona t content
  show duran t surprised
  "I smiled and wrapped my arm around his shoulders."

  show merona t content OM
  show duran t neutral
  mk "We'll still be friends, right? We'll say hi to each other in the halls and hang out when we can. Let's introduce our other friends to each other too!"

  show merona t surprised
  show duran t nervous OM
  dt "You... would only be meeting yourself then."

  show merona t serious
  show duran t nervous
  mk "..."

  show merona t worried
  show duran t annoyed CE
  mi "Now that I think about it, Duran did seem like a loner back at school. I didn't know anyone who willingly hung around him, and his standoffishness repelled others more often than not."

  show merona t happy
  show duran t surprised
  mk "Then, I guess that's one set of friends done! You still have to meet my friends, and then we'll all hang out together."

  show merona t grin
  show duran t nervous OM
  dt "You're making it sound too easy..."

  show merona t content OM
  show duran t worried
  mk "Look, you're a fun person to be around, and I'm sure others will think that too once they get to know you. And if they don't, then you can just meet up with me."

  show merona t content
  show duran t embarrassed OM
  dt "...Thanks, Merona. I really appreciate it."

  play sound sound_pat
  show merona t grin
  show duran t embarrassed
  "I patted his head, and we resumed in silence, trekking along the path with Prowen leading the way. "

  show merona t determined
  $ renpy.transition(slow_dissolve, layer="master")
  hide duran
  mi "Misconceptions arise because of a lack of understanding; if more people put in the effort to connect with others, all those misconceptions can finally clear up."
  return
  #-----------------------------------------------