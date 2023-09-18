  #-----------------------------------------------
  # CHAPTER 2
  #-----------------------------------------------
label lbl_PathB_2_0:

  #B2.0"
  #(Continuation of 1.9)

  #play music music_recollections #(from before)
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest8
  #TODO [fade in CG forest8
  #TODO [fade in CS wagon#; right from center#; behind the characters
  #TODO [fade in CS lexan content OM#; center
  #TODO [fade in CS rett content#; right
  show wagon:
      xalign 0.75
      yalign 1.0
  show rett content:
      xalign 0.75
      yalign 1.0
  show lexan content OM:
      xalign 0.5 
      yalign 1.0
  "I scanned the area and spotted Lexan leaning against the cart to chat with Rett. They were organizing the supplies, trying to fit everything in the best place possible."

  #TODO [fade in CS merona content#; left from center - animation: move towards Lexan and back to the initial position #(she taps Lexan's shoulder)
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content OM behind lexan
  show merona t content OM at ShoulderTap
  "I dawdled over to the two, but they had their backs turned away from me and kept working. I tapped Lexan's shoulder."

  show lexan surprised OM
  show rett neutral
  show merona t surprised
  ln "Whoa!"

  show lexan surprised
  show rett grin
  show merona t sadSmile
  "He jumped at my hand and almost dropped the box he was holding before he turned around to see me. "

  play music music_Summer_Day
  show lexan laugh
  show merona t content
  ln "Oh, sorry. *laugh* That was so sudden, it gave me a bit of a fright..."

  show lexan content
  show rett content
  show merona t content OM
  mk "Sorry! Just wanted to tell you that I wanted to mainly work with you on my studies over the course of our trip."

  show lexan content OM
  show merona t content
  ln "Sounds good. Did you want to get started now?"

  show lexan content
  show merona t content OM
  mk "Yeah, if you're able to. Do you still need to help out Rett?"

  show rett content CE
  show merona t content
  "We both looked at Rett, and he shook his head."

  show rett content OM
  rt "I'm fine. You should go on ahead and do your job."

  show lexan grin
  show rett grin
  "He broke out in a grin."

  play music music_Incoherent
  show rett laugh
  show merona t grin
  rt "Besides, I always have Kreita who can be my packmule."

  show rett smirk
  "I chuckled to myself, rolling my eyes at him."

  show lexan content
  show merona t laugh
  mk "Hey, she's got her own stuff to do! She could use you as her pack mule whenever she wants too."

  show rett wink
  show merona t grin
  "He winked at me, continuing to lift the crates on and off the cart."

  show lexan grin CE
  show rett wink OM
  show merona t content
  rt "We've been each other's pack mules for a long time. But you two should go on and start 'class' instead of standing around talking to me. Start learning or whatever!"

  play music music_Cool_Steel_Breeze
  show lexan content OM
  show rett content#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide rett
  ln "How about we go under that tree over there?"

  show lexan content
  "He pointed to a flat spot shaded over by the tree's large branches. It had a smooth trunk, perfect for leaning against, and the ground was inviting us to sit on its grassy cushion."

  show lexan content CE
  show merona t happy
  mk "That'd be great! Let's go."

  #TODO [fade in CG forest9
  #TODO [fade in CS lexan content#; right#; y position at 200px lower than normally
  #TODO [fade in CS merona t content#; left#; y position at 200px lower than normally
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest9
  show lexan content:
    xalign 0.75 
    yalign 2.5
  show merona t content:
    xalign 0.25 
    yalign 2.5
  "Lexan grabbed a notebook out of his bag near the cart, and we headed over to the tree. He flipped to the first page and readied his pen as we plopped down."

  show lexan serious OM
  show merona t serious
  ln "I need to create a schedule for you and Duran, but I first need to have a full understanding of where you're at and where you need to be, in terms of your skill level."

  show lexan serious
  show merona t serious OM
  mk "Well, Le-I mean, Master Nerion. I'd say that..."

  show lexan content
  show merona t serious
  "He smiled at me."

  show lexan content OM
  show merona t sadSmile
  ln "If you'd rather call me 'Lexan', I wouldn't mind that. I think you've gotten used to it already."

  show lexan content
  show merona t sadSmile OM
  mk "Are you sure? I don't want to come off disrespectful or anything like that..."

  show lexan laugh
  show merona t content
  ln "It's not like my first name is offensive. Besides, I don't think what you call me should determine if you respect me or not."

  show lexan content
  show merona t content OM
  mk "Well... Alright, if you're okay with me calling you by your first name, then I'm just going to keep doing that."

  play music music_Words
  show merona t determined
  mi "But if I'm going to be using \"Lexan\", he ought to do the same for me."

  show lexan surprised
  show merona t content OM
  mk "You should just call me 'Merona' too, not 'Student Kovene'."

  show lexan content OM
  show merona t grin
  ln "No problem. Glad we got the formalities out of the way."

  show lexan grin
  show merona t surprised OM
  mk "Oh, and make sure you do that for Duran too! It'd be weird if you called him 'Student Trist' all the time."

  show lexan grin OM CE
  show merona t grin
  "He laughed and nodded."

  show lexan grin OM
  ln "Absolutely. I don't think I need to tell Duran to use my first name though."

  show lexan content
  show merona t content OM
  mk "Yeah, you're right about that, haha. Anyways, back to your earlier question!"

  show lexan neutral
  mk "I would say that I..."

  show merona t sadSmile
  "The smile on my face fell a little."

  show merona t sadSmile OM
  mk "...could use some extra help..."

  show lexan serious
  show merona t disappointed OM
  mk "...and I feel like I'm on the verge of repeating my current level next year..."

  play music music_She_dreams_in_blue
  show merona t disappointed
  mi "It feels a bit painful to be saying this out loud. A very pitying pain."

  show lexan serious OM
  show merona t serious
  ln "Oh, well I suppose we'll have to do something about that."

  show lexan neutral OM
  ln "Would you say that you're lacking more in using your ability, or understanding the concepts of your ability type?"

  show lexan neutral
  show merona t worried
  mi "Is it sad that the answer is both?"

  show merona t sadSmile OM
  mk "I guess I could use help for both cases. I feel like I understand the basic concepts and the methods to how to use my ability, but nothing works when I try to do it. It's like I'm missing a connection."

  show lexan determined OM
  show merona t worried
  ln "I think I can help you get a better feel over what you should be doing. You say that you lack a connection, but I'm sure if we try explaining or doing things in different ways, we'll find a way that'll be good for you."

  show lexan determined
  show merona t worried OM CE
  "I sighed, hanging my head down."

  show merona t worried OM
  mk "I sure hope so. I'm tired of getting frustrated over never accomplishing anything."

  show lexan content OM
  show merona t surprised
  ln "Don't worry so much about how you are now. Everybody's going to struggle with something-even an ability-but you're going to move forward. As a teacher, I promise you that."

  show lexan content
  show merona t worried
  "I peeked up at him."

  show lexan surprised
  show merona t worried OM
  mk "And if you don't...?"

  show lexan sceptical
  show merona t worried
  "He rose an eyebrow."

  show lexan sceptical OM
  show merona t disappointed
  ln "Are you suggesting that I can't?"

  play music music_Ill_be_right_behind_you_Josephine
  show lexan worried
  show merona t disappointed OM
  mk "I'm only suggesting that I can't!"

  show lexan content
  show merona t surprised
  "He patted my shoulder."

  show lexan content OM
  ln "I'm going to make sure that you can. Definitely."

  show lexan content
  "Staring at his determined face, I thought about all the past teachers I've had and everything they couldn't do for me."

  show merona t serious
  mi "A lot of them didn't try to find a good way for me to move ahead. A lot of them gave up when I couldn't do what they said after a few times. A lot of them simply told me I had better luck doing something else."

  show merona t content
  mi "But with Lexan, I have hope of growing."

  show lexan determined OM
  show merona t grin
  ln "Okay, let's start with a lesson right now and see what we can do."

  scene bg black with fade

  
  
  return
  
  #-----------------------------------------------
label lbl_PathB_2_1:

  #B2.1"

  play music music_Summer_Day
  scene cg forest11 #(as before)
  #TODO [fade in merona t content#; app. x=70%
  $ renpy.transition(slow_dissolve, layer="master")
  #TODO [fade in lexan neutral#; app. x=25%
  show merona t content:
      xalign 0.70 
      yalign 1.0
  show lexan neutral:
      xalign 0.25 
      yalign 1.0
  "Being right next to Lexan, how about I talk to him a little?"
  show merona t content OM
  show lexan surprised
  mk "So... Lexan, how's your day been?"
  show merona t content
  show lexan content OM
  ln "It's been going quite well, thank you. How has yours been?"
  show merona t happy OM
  show lexan grin
  mk "It's also been pleasant for me. I'm kind of thinking about not tripping into poison ivy or something like that."
  show merona t grin
  show lexan laugh
  ln "Yes, it wouldn't be desirable for that to happen. Have you been recognizing plants that you've learned about from school?"
  show merona t happy OM
  show lexan content
  mk "Actually, I have for some. It's a little weird actually seeing them with my own eyes and not just a picture. It shows that I'm learning something, at least!"
  play music music_newBegin
  show merona t content
  show lexan content OM
  ln "That's good to hear. Being in the forests is the perfect environment for your studies out of the classroom. Since my ability is water manipulation, the best place for me can be anywhere as long as there is a body of water around. Even without a body of water, water exists in clouds and air, so truly anywhere is a perfect place."
  show merona t content OM
  show lexan content
  mk "Sounds useful. There's water in vegetation and all, so the forest is a good spot for you too."
  show merona t content
  show lexan happy OM
  ln "Right. Plant and animal life contain many common elements, so it's lucky that water can be found in most places."
  
  show merona t content OM
  show lexan grin
  mk "You seem to like your ability a lot. Or at least appreciate it."
  show merona t content
  show lexan happy OM
  ln "I do. I both like and appreciate it. I suppose that's one of the factors that motivated me to move along so quickly when I was in school."
  show merona t surprised OM
  show lexan grin CE
  mk "You skipped grade levels?"
  show merona t surprised
  show lexan happy OM
  ln "Yes."
  show merona t surprised OM
  show lexan grin CE
  mk "Wow, that's a big accomplishment! How'd you do it?"
  play music music_piano
  show merona t serious
  show lexan neutral OM
  ln "Well... Most of my time was spent with myself. I wanted to get through school as fast as possible, and it helped that I enjoyed the ability I have. By studying, practicing, and some degrees of luck, I managed to go up."
  show merona t happy OM
  show lexan neutral
  mk "That's really something to be proud of. Why did you want to go through school so fast though?"
  show merona t worried
  show lexan worried OM
  ln "Personal reasons."
  show merona t worried OM
  show lexan worried
  mk "Oh, okay. I see."
  show merona t grin
  show lexan determined OM
  ln "Yes... I became a master mage a few years later, and now here I am."
  show merona t content OM
  show lexan content
  mk "That's pretty intere-."
  
  stop music
  #"-------------------------------------------------------"


  return
  #"-------------------------------------------------------"
  
label lbl_PathB_2_3:
  #B2.3"

  #play music music_Pride #(from before)
  #scene cg forestHouse inside #(from before)
  #show rett worried, center #(from before)
  show cimaria serious#; left from Rett
  #TODO [fade in CS merona t surprised OM, right from Rett
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t surprised OM:
    yalign 1.0
    xalign 0.75

  mk "He should be in here somewhere. It's not that big of a house, and he definitely went in with us. Maybe he had to do something privately."

  #"--------------------------------"



  return
  
  #-----------------------------------------------
  
label lbl_PathB_2_4:

  #B2.4"

  play music music_Summer_Day
  scene cg forest13 #(from before)
  show merona t surprised
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan neutral OM:
    yalign 1.0
    xalign 0.25
  #TODO [fade in CS lexan neutral OM#; left from Merona
  ln "Merona?"

  show lexan content
  mk "Hm?"

  show merona t content
  "I turned around and saw Lexan behind me."

  show lexan surprised OM
  ln "Do you need any help? I figured it'd be better if you had someone else outside with you in case something happened."

  show lexan content
  show merona t content OM
  mk "Oh, sure, help wouldn't hurt. And thanks for going out too. Yeah, it'll be better if the numbers are larger."

  show lexan laugh
  show merona t content
  ln "*laugh* Right. So, how much more wood do you need?"

  show lexan content
  show merona t happy
  mk "Mm, not much. A few more good pieces and we're good."

  show lexan content OM
  show merona t reflective
  ln "Okay. Are you looking for any other things?"

  show lexan content
  show merona t content OM
  mk "Not really. If I come across anything useful, I'll pick it up though."

  show lexan determined OM
  show merona t surprised
  ln "Since there's not much to get anyway, how about a quick impromptu lesson?"

  play music music_Cool_Steel_Breeze
  show lexan grin
  show merona t serious OM
  mk "Impromptu lesson? Uh... sure!"

  show lexan content OM
  show merona t serious
  ln "There are many plants out here to observe and use, so how about practicing speeding the growth of a plant without drinking your enhancer?"

  show lexan content
  show merona t sadSmile OM
  mk "Without it? I don't know, I have enough trouble doing that even when I drink it."

  show lexan content OM
  show merona t surprised
  ln "You're still able to do it though. It's good not to become too reliant on an enhancer, so try your best. Start practicing without it."

  show lexan determined
  show merona t determinedGrin OM
  mk "You're right, I'll give it try!"

  show lexan content
  show merona t content:
    xalign 0.7
    yalign 2.5 #; move her to the right and then move her sprite down by 250px
  "I looked around for a young plant and my eyes caught one a few feet away. I went over to it, and crouched down."

  show merona t content OM
  mk "Is this one okay?"

  show lexan content OM
  show merona t content
  ln "It's fine. Go ahead and try."

  show lexan content
  show merona t serious
  scene bg black with fade
  "I dug my hand into the soil and grasped the roots as usual, while focusing on the life flow."

  stop music fadeout 1.0
  mi "Speed growth... Mature faster..."

  mi "..."

  mi "I don't feel any changes..."


  "The wind kept pulling on my hair, and I was getting a little tired from crouching."

  play music music_romance
  scene cg Lexan handOnMsArm1#; #(has a b version with Lexan's eyes closed)
  #TODO [mouth closed
  #TODO [Merona blushing
  #TODO [Merona's eyes closed
  "I felt Lexan's hand on my arm, but I kept my eyes closed. My face turned a little warm."

  scene cg Lexan handOnMsArm2#; #(has a b version with Lexan's eyes closed) mouth open
  ln "Try and concentrate more on the plant. Ignore the distractions and only focus on the plant."

  scene cg Lexan handOnMsArm3#; mouth closed
  mi "Well Lexan... perhaps you should try giving me a little more personal space to help me. But thanks for the advice."

  scene cg Lexan handOnMsArm4# - Merona normal
  "I took a few more breaths, and I tuned everything out. Everything was in the background, and all I could feel was the ebbing of the plant's flow."

  stop music fadeout 1.0
  #TODO [overlay 30% black
  show bg black:
    alpha 0.3
  mi "..."
  #TODO [overlay 60% black
  show bg black:
    alpha 0.6
  mi "..."

  scene cg Lexan handOnMsArm5#; Merona's eyes open
  "I opened my eyes and the plant didn't grow at all."

  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest13 #(from before)
  #"at the same time fade in..."
  show merona t disappointed:
    xalign 0.7
    yalign 2.5 #; right#; sprite 250px down from normal position
  show lexan sadSmile:
    xalign 0.5
    yalign 2.0 #; center#; sprite 200px down from normal position

  play music music_piano
  mk "*sigh* It didn't work."

  show merona t disappointed
  show lexan sadSmile OM
  ln "Well, that's okay. It'll take more practice, but I know you can do it with more time too. Sorry about interrupting your concentration; you seemed to be struggling, so I had to give you some help."

  show merona t sadSmile OM
  show lexan sadSmile
  mk "I did struggle, so it's fine. Don't worry about it!"

  show merona t content
  show lexan content OM
  ln "I think I'll go back into the house and check up on Duran too. I'll see how everyone else is doing as well."

  show merona t content OM
  show lexan content
  mk "Thanks again for coming out here!"

  show merona t content
  show lexan neutral:
    xalign 0.5
    yalign 1.0 #; move back to normal height position
  "He got up and brushed off his uniform."

  show lexan content OM
  ln "No need to thank me. Stay safe."

  show lexan neutral#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide lexan
  "I stayed crouched and watched him leave."

  show merona t sadSmile
  mi "At least I got some good practice even if it didn't work out too well."

  show merona t serious
  "There were some pieces of firewood I missed seeing earlier, and I picked them up."
  #TODO [move Merona back up to normal height position and then to the center
  show merona:
    xalign 0.5
    yalign 1.0

  #"------------------------------------------------------"



  return
  
  #-----------------------------------------------
  
  
label lbl_PathB_2_8:
  #B2.8"


  #"-----------------------------------------------------------"
  #TODO [fade in CS lexan neutral#; right from Merona
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan neutral OM:
    xalign 0.8
    yalign 1.0
  "Lexan turned his head toward me."

  show merona t grin
  show lexan neutral OM
  ln "Merona?"

  show lexan neutral
  "He was walking at the very front, and I was right behind him. I walked a tad faster to get beside him."

  play music music_recollections
  show merona t surprised OM
  show lexan strict
  mk "Yes?"

  show merona t surprised
  show lexan strict OM
  ln "What do you think of Prowen coming along with us?"

  show merona t content OM
  show lexan strict
  mk "Hm... Prowen seems to need some help and can provide some help for us too maybe, so he's okay."

  show merona t content
  show lexan worried OM
  ln "Valid points. He doesn't appear to be dangerous or show hostile behavior towards us. So far, it's a mutual beneficial relationship we have with him."

  show merona t reflective
  ln "I am curious to know more about him and his whereabouts, but I don't know if it's exactly proper to ask him about his life. He's not offering any information, but perhaps later on, our group can get to know him more."

  show merona t serious OM
  show lexan surprised
  mk "I hope we won't be too bothersome for him either. He doesn't know much about us, how we work, and what we're doing."

  show merona t serious
  show lexan neutral OM
  ln "I don't think that we collectively as a group are very annoying or strange to a degree. It'll also depend on how the environment we come across and the weather we'll encounter affect our traveling."

  show merona t content OM
  show lexan neutral
  mk "We don't have much to worry about with him then."

  play music music_Words
  show merona t content
  show lexan content OM
  ln "Right. By the way, have you been practicing on your own with our current focus?"

  show merona t grin
  show lexan content
  "I nodded and smiled."

  show merona t happy
  mk "Yep. I think it's becoming easier for me to control some aspects of growth in plants. I've been weaning off the enhancer too."

  show merona t grin
  show lexan content OM
  ln "That's good to hear. If you come far enough in your skills, we could try doing some experiments on animals if we find any."

  show merona t happy
  show lexan surprised
  mk "Ooh, that sounds really great! I like working with animals a lot too, living or dead."

  show merona t content
  show lexan neutral OM
  ln "Really? How did you get the experience?"

  show merona t content OM
  show lexan neutral
  mk "Grew up in an agricultural family. I helped out a lot and cared for many animals and crops."

  show merona t content
  show lexan content OM
  ln "You have a fitting ability for that. As much as I like my own ability of water manipulation, I am also quite fascinated with abilities dealing with life, especially environmental life."

  show merona t laugh
  show lexan content
  mk "That's great! I think environmental life is an interesting topic too. Lucky for you get to help a student who has an ability like that."

  show merona t grin
  show lexan laugh
  ln "*laugh* True. I also enjoy working with you too, disregarding the ability. You're very easy to work with and you have a wonderful personality."

  play music music_romance
  show merona t happy
  show lexan content
  mk "Oh, thanks! I could say the same to you as well."

  show merona t content
  show lexan grin CE
  "He closed his eyes and smiled."

  show merona t surprised
  show lexan determined OM
  ln "Thank you as well. I'm not kidding though- people like you are hard to find sometimes, so I'm glad that I have you as a student for this brief time."

  show merona t blushSmile
  show lexan determined
  "I blushed a little and smiled back."

  mi "Thank you, Lexan."

  scene bg black with fade





  return
  
  #-----------------------------------------------
  
  #-----------------------------------------------
  # CHAPTER 3
  #-----------------------------------------------
  
label lbl_PathB_3_3:

  #"-----------------------"
  #TODO [fade out Boyen
  $ renpy.transition(slow_dissolve, layer="master")
  show black at Blinking
  hide boyen
  #TODO [fade in CS lexan shocked and show it "blinking" like Boyen's sprite#; in the center
  show lexan shocked  behind black
  "Lexan stood up and jumped in front of me, steering me away from the fire. I twitched at the quick change in scenery."

  show lexan shocked OM:
    xalign 0.5
    yalign 1.0#; same animation pattern as before
  ln "Look away from there. Look up instead."

  show lexan annoyed#, fade in Lexan's opacity to 100%
  $ renpy.transition(slow_dissolve, layer="master")
  hide black
  #(voice continues to shake)
  mk "U-Up?"

  show lexan strict
  "He kept his hands on my shoulders and squeezed them, stabilizing my stance."

  show lexan annoyed OM
  #TODO [fade bg to CG campingFire but only at 30% opacity
  $ renpy.transition(slow_dissolve, layer="master")
  show cg campingFire:
    alpha 0.3
  ln "Up."

  stop music
  show lexan annoyed
  #TODO [fade bg to full opacity
  $ renpy.transition(slow_dissolve, layer="master")
  show cg campingFire:
    alpha 1.0
  "I swallowed, expecting to see the shadow of the monster over me, and I let my eyes slowly turn up first."

  play sound sound_nighttimeAmbience
  show lexan confused
  mi "The moon."

  show lexan serious
  mi "It's just an almost full moon."

  show lexan sadSmile
  mi "And... the stars."

  play music music_piano
  show lexan sadSmile CE
  mi "There are stars sprinkled next to it."
  #TODO [move Lexan's sprite to the right and fade it out please#; approximately 70%X
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan at right
    
  $ renpy.transition(slow_dissolve, layer="master")
  hide lexan
  
  return
  #"-------------------------------------------------------"
  
  
  
  
  #-----------------------------------------------
  # CHAPTER 4
  #-----------------------------------------------
  
label lbl_PathB_4_4:

  play music music_Radio_Martini
  show cg hillSide2
  show lexan content#; position as in 4.3
  show merona t content OM#; position as in 4.3
  mk "Sure, what do you need me to do?"

  show lexan content OM
  show merona t content
  ln "Organize what is on the cart. Some things are disheveled or prone to falling out, so I would be very grateful if you could rearrange them. I need to get some items a few feet away."

  show lexan grin
  show merona t happy
  mk "No problem!"

  $ renpy.transition(slow_dissolve, layer="master")
  
  #TODO [fade CG to CG hillSide
  show cg hillSide
  #TODO [at the same time fade in CS wagon, center
  show wagon
  #TODO [at the same time fade out Lexan
  hide lexan
  show merona t content
  "I jumped to the cart and hovered over it, taking everything in."

  show merona t surprised
  mi "Okay. Most things in a good position. These bags are still open, and a lot of books and clothes are slipping away, so I should handle that first."

  show merona t sadSmile at QuickCrouch#; move once down and up by 250px
  "I set the monster down, close to my feet."

  show merona t worried:
    yalign 1.0
  mi "Hopefully I won't step on it or else it might... come apart."

  show merona t serious
  "I pushed the items into their rightful bags, drawing them to a close when everything was in the right places. Looking over the wagon again, I moved some boxes of food to the corners, and gave all the things a final push as far as they could."

  show merona t content
  mi "Good. Nothing should fall out now, and we should be able to move this cart easily if the path is smooth enough."

  #TODO [fade in CS lexan content#; same position as before
  show lexan content:
    yalign 1.0
    xalign 0.75
  "Lexan came over and dumped some extra bagged food into the wagon."

  show lexan happy OM
  show merona t grin
  ln "That should be everything we have. Thank you so much for helping me."

  show lexan neutral
  show merona t grin CE
  "I shook my head."

  show lexan surprised
  show merona t happy
  mk "Oh no, it wasn't a big deal. You do a lot for me already anyways."

  show lexan laugh
  show merona t surprised
  ln "*laugh*"

  play music music_romance
  show lexan grin
  show merona t surprised OM
  mk "...What's so funny?"

  show lexan laugh
  show merona t nervous
  ln "Ha ha, it's nothing."

  show lexan grin
  show merona t determinedGrin
  "I crossed my arms and snorted."

  show lexan content
  show merona t determinedGrin OM
  mk "Oh come on, it's never 'nothing'."

  show lexan content OM
  show merona t surprised
  ln "Then instead of 'nothing', it was... amusing."

  show lexan content
  show merona t sadSmile OM
  mk "Amusing?"

  play music music_Summer_Day
  show lexan determined OM
  show merona t surprised
  ln "Amusing how you insist that I deserve more thanks for what I do. You can let me appreciate what you do for me too."

  show lexan determined
  show merona t happy
  mk "*chuckle* Sure. But, let me appreciate your doings too."

  show lexan laugh
  show merona t grin
  ln "Of course, of course."

  show lexan content
  show merona t content
  #TODO [fade in one after another with a short wait time...
  #TODO [fade in CS cimaria neutral#; left from Merona
  pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria neutral:
    yalign 1.0
    xalign 0.17
  #TODO [fade in CS kreita neutral#; center
  pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita neutral:
    yalign 1.0
    xalign 0.5
  #TODO [fade in CS boyen content#; right from Kreita
  pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")
  show boyen content:
    yalign 1.0
    xalign 0.9
  #TODO [fade in CS rett neutral#; left from Kreita
  pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")
  show rett neutral:
    yalign 1.0
    xalign 0.3
  "One by one, everyone came over to the cart once they had gathered all their belongings."

  #TODO [fade in CS duran t annoyed#; right from Lexan
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t annoyed:
    yalign 1.0
    xalign 1.0
  mi "Nothing looks left behind, and Duran woke up too. Seems like everything has been taken care of."
  $ renpy.transition(slow_dissolve, layer="master")
  scene bg black #and from black#; move Merona to center #(show her again after black is gone), erase all other sprites including the wagon
  show merona t content
  pause(1.5)
  #TODO [change CG to hillSide2 with a fade in #(leave Merona visible)
  scene cg hillSide2
  show merona t content
  return
  #-----------------------------------------------
label lbl_PathB_4_5:
  
  
  play music music_Words
  $ renpy.transition(slow_dissolve, layer="master")
  #TODO [fade in CG forest18
  scene cg forest18
  #TODO [fade in CS merona t serious#; center
  show merona t serious:
    yalign 1.0
    xalign 0.35
  show lexan neutral:#; right from Merona
    yalign 1.0
    xalign 0.8
  "As everyone walked forward, small chatter among us began to bob up. I looked around."
  show merona t sadSmile
  mi "At least the weather for today seems fair; it's nice that we're starting off well enough. I'm sure we'll be able to pull through this..."
  show merona t sadSmile OM
  show lexan surprised
  mk "So... Lexan, how do you feel about all this?"
  show merona t sadSmile
  show lexan worried OM
  ln "Regarding Rett?"
  show merona t serious
  show lexan annoyed
  ln "..."
  show merona t worried
  show lexan annoyed OM
  ln "Honestly, I'm rather worried about it. We are not in a good position, and we do not have much specific information about his situation."
  show merona t worried OM
  show lexan annoyed
  mk "Do you think that he'll survive or that we'll find something in time?"

  show merona t worried
  show lexan worried OM
  ln "I can only hope so."
  show merona t sadSmile OM
  show lexan surprised
  mk "I feel like we'll be okay. We'll be able to do something that'll work. Or at least we have the chance to do anything at all for him."
  show merona t content
  show lexan determined OM
  ln "Of course. We still have the possibilities."
  play music music_Cool_Steel_Breeze
  show merona t determinedGrin OM
  show lexan sadSmile
  mk "I'd rather stay optimistic about it."
  show merona t content
  show lexan content OM
  ln "Well, it's good to be positive. Anyways, how have you been feeling about this entire trip in general?"
  show merona t worried OM
  show lexan neutral
  mk "This whole trip..."
  show merona t worried
  mi "How should I put it? I mean, so far things have been swell and all, but then I had a small meltdown after remembering my attack and Rett is possibly dying at the moment, so those two things aren't exactly great highlights."
  show merona t content OM
  show lexan sadSmile
  mk "It's been... alright. Overall, everything has been fine."
  show merona t shocked
  mi "I just hope that it'll continue to be fine."
  show merona t nervous OM
  show lexan neutral
  mk "How about you? Do you feel okay with everything that's happened so far?"

  play music music_Summer_Day
  show merona t serious
  show lexan neutral OM
  ln "I suppose. It hasn't been terrible, but it hasn't been exactly the best of times. Of course, nothing will be perfect though."
  show merona t reflective
  show lexan neutral
  "I shrugged."
  show merona t serious OM
  mk "It can't be helped... By the way, what do you have planned for our next lesson?"
  show merona t sadSmile
  show lexan content OM
  ln "Hm? What has interested you?"
  show merona t sadSmile OM
  show lexan content
  mk "Eh, I've been feeling extra studious lately. I kind of want to do something to get my mind off of everything."
  show merona t content
  show lexan laugh
  ln "*laugh* And you choose to learn more. Good choice, good choice."
  show merona t content OM
  show lexan grin
  mk "Psh, it's not like I exactly have a choice of wanting to study or not. I'm only fulfilling my duty of being a proper student."
  show merona t content
  show lexan grin CE
  "Lexan lightly clapped for a moment, and I rolled my eyes with a small smile."
  show lexan content OM
  ln "Nonetheless, I applaud you for your short-term everlasting passion for learning. To answer your question, I'm thinking of either doing a few joint lessons with you and Duran or skip to another lesson that deals more with our current situation."
  show merona t grin
  ln "I suppose I'll leave it up to you and Duran at the end, so hopefully we won't have to postpone any of our lessons soon on this journey."
  show merona t content OM
  show lexan content
  mk "Oh that sounds fun! Alright, I'm looking forward to this."

  play music music_She_dreams_in_blue
  show merona t serious
  show lexan neutral OM
  ln "Are you handling all your work well? You seem to be improving quickly, so I'm unsure of why you weren't considered to be... a better student."
  show merona t sadSmile OM
  show lexan confused
  mk "Really? Well, you yourself did say that I'm 'improving', and in order to improve, you have to start at the bottom right? Ha ha..."
  show merona t surprised
  show lexan laugh
  ln "*laugh* I guess so. But honestly, you've been doing really well. Once we return, you should be fine and definitely won't need any extra help."
  show merona t blushSmile OM
  show lexan content
  mk "Thanks, that's nice to hear! It was the whole point of this trip after all, so at least we're following that objective..."
  show merona t blushSmile
  show lexan neutral OM
  ln "Well... That's not our entire objective per se."
  show merona t surprised OM
  
  call lbl_PathB_4_5_o from _call_lbl_PathB_4_5_o
  
  play music music_White
  show merona t serious
  show lexan sadSmile OM
  ln "Thank you, Merona. I have to go and speak with the others about a few things, so I hope to chat with you soon."
  show merona t content OM
  show lexan content
  mk "Have a nice time, Lexan."
  show merona t serious
  #TODO [fade out Lexan
  $ renpy.transition(slow_dissolve, layer="master")
  hide lexan
  "He shuffled away, and I was walking on my own."
  show merona t nervous
  mi "My objectives... the reasons why I'm on this journey..."
  show merona t nervous CE
  mi "..."
  show merona t worried OM
  mi "They're only those two points, right?"                                         
  return
  #-----------------------------------------------
label lbl_PathB_4_5_o:
  
  show lexan neutral
  mi "Entire objective? I'm pretty sure the headmaster said that I was only supposed to improve my studies away from the academy area because of my recent attack and become more aware of what's going on Diolacov..."
  play music music_Soporific
  show merona t surprised
  show lexan strict OM
  ln "Oh, um... well, yes that is, uh...what you specifically are supposed to do. We adults have other things we need to worry about."
  show merona t nervous
  show lexan strict
  mi "Sounds sort of... suspicious, but it's probably nothing too important. This is a school trip we're talking about after all-What would there be to hide from me or even Duran?"
  show merona t nervous OM
  show lexan neutral
  mk "Other things concerning the academy or me? I'm sorry if I sound a bit rude, but I'd like to know if there are things concerning me or my well being that I don't know about."
  show merona t surprised
  show lexan worried OM
  ln "No, no, that's not rude at all-you have a right to know of those things. But, what the others and I are dealing with is... not as clear as what you have to do, so I can't offer much of an explanation..."
  show merona t disappointed OM
  show lexan worried
  mk "I see. Well, if you guys are confused about it... you could always speak to Duran and me."
  show merona t surprised OM
  show lexan surprised
  mk "Uh... Actually, I don't know if Duran necessarily would want to do that, but I'd definitely be open to discussing."
  
  $PathB_4_5_o_Flag = True
  
  return
  #-----------------------------------------------
label lbl_PathB_4_7_1:
  
  
  #TODO [As before:
  #play music music_Green_Leaves
  #show cg forestGround
  #show mattress#; center
  #show merona t content#; center, use Merona hair u please
  #show blanket#; center

  #show Clouds dark#; opacity around 30-50%#; "
  #"if possible, use a "multiply" mode for them please#; "
  #"slowly move from right to left please
  mi "I think that if I walk around a bit, it should warm me up. Nothing wrong with a little walk before our long one!"
  #TODO [fade out Merona's sprite while moving the blanket down by 200px
  show blanket:
    yalign 4.5
  $ renpy.transition(slow_dissolve, layer="master")
  hide merona
  "I tossed aside my blankets and scooted out of my makeshift bed."
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest19
  show merona t content#; with Merona hair t again please
  mi "Now, I just have to make sure that I don't get lost or stray away from the group too far. Who knows, I might find something eye-catching and get lost, ha ha. But, I should actually find a good place to relax and stretch a little."
  "I pushed myself up from the ground and tugged at my clothes, straightening them out."
  show merona t grin
  mi "I think I'll walk away from the stream and find another place to go to. We've already been following it for so long, so a change in scenery would be nice! I wonder if I'll find anything strange or useful."
  show merona t content
  "Stepping out of the clearing, I wandered around the pathless area. I came across an assortment of plants, which made me stop."

  show merona t happy
  mk "Oh hey, I can recognize some of them."
  show merona t grin
  mi "Looks like my memorization has been getting better. I can even remember some of the different properties and uses for a few plants..."

  play music music_Summer_Day
  show merona t surprised
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan content OM at right#; right
  ln "Oh, Merona? Is that you?"
  show merona t surprised OM
  show lexan content
  mk "Hm? Lexan?"
  show merona t content
  "I looked around to find where Lexan's voice was coming from, and I finally spotted him through the slits of a group of tree trunks. He was leaning against some of the closer trees with something in his hand and was attempting to catch my attention."
  show merona t content OM
  show lexan grin
  mk "Oh, hello there!"
  show merona t content
  show lexan content
  "I stepped over to his place and gave a tiny wave."
  show merona t content OM
  mk "Hi, how are you? So, what are you doing here so early in the morning?"
  show merona t content
  "He held up the item in his hand."
  show lexan content OM
  ln "Just prepping for one of Duran's lessons today with some reading. I usually go over the lessons for both of you early in the morning."
  show merona t surprised OM
  show lexan surprised
  mk "Oh, sorry to distract you from that then. I can leave if you'd like."

  show merona t surprised
  show lexan neutral
  "He shook his head and swatted his hand down."
  show merona t content
  show lexan content OM
  ln "I've already finished reading everything and was merely skimming over things again, so it's alright if you stay."
  play music music_piano
  show lexan neutral OM
  ln "So, how has everything been so far with you? You're doing okay?"
  show merona t sadSmile OM
  show lexan neutral
  mk "Had a bit of trouble falling asleep last night, so I'm feeling kind of tired right now. *laugh* How about you?"
  show merona t content
  show lexan sadSmile OM
  ln "I actually was able to fall asleep quite easily, so my night was rather pleasant! I'm getting used to-arguably even comfortable with-sleeping on the ground, so I've gotten good rest as of late."
  show merona t content OM
  show lexan content
  mk "That's great! I guess if we were to count some of the positive things happening like your sleeping, one of them would be how I was just able to identify some of the different plants we learned in previous lessons."
  play sound [sound_clap, sound_clap]#, play twice please
  show merona t content
  show lexan content CE
  "Lexan nodded and clapped twice."
  play music music_Words
  show merona t grin
  show lexan content OM
  ln "This goes to show that my teaching is actually effective."
  show merona t happy
  show lexan content
  mk "Very effective, for you've even been able to get me to remember things."
  show merona t grin
  show lexan happy OM
  ln "*laugh* You could say that it was a good choice for Wriane to let you go on a journey and get some tutoring on the way."
  show merona t content
  show lexan content
  "I smiled and looked out at the sky."
  show merona t content OM
  mk "Well, that's exactly why I'm here."
  play music music_Swimming_To_Cambodia
  show merona t worried
  mi "Though it's why I'm here... there is another reason I'm here right? At least, that's what I'm remembering right now the last time I got to speak with Lexan."
  show merona t serious
  show lexan surprised
  mk "..."
  show merona t surprised
  show lexan worried OM
  ln "Is something the matter?"
  show merona t content
  show lexan worried
  "I twitched away from my thoughts and looked at Lexan again."
  show merona t content OM
  mk "Hm? No, why?"
  show merona t sadSmile
  show lexan neutral OM
  ln "You suddenly stopped talking, which was a bit unusual for you."
  show merona t sadSmile OM
  show lexan neutral
  mk "Oh, sorry about that, I didn't mean to silence myself like that. I was thinking about some things. Mainly about what we had talked about last time."
  show merona t serious
  show lexan confused
  "Lexan squinted for a moment."
  show lexan confused OM
  ln "What we talked about? What was it again?"
  show merona t sadSmile OM
  show lexan surprised
  mk "Nothing really. Just about why I'm here."
  show merona t serious
  show lexan surprised OM
  ln "Ah, yes. Now I remember. It was about the..."
  return
  #-----------------------------------------------
  
label lbl_PathB_4_7_o:
  
  ## OPTIONAL ##"
  if PathB_4_5_o_Flag:
    play music music_Soporific
    #(This is all recorded already from the B4.5 script, but if player did not choose that route before this choice, insert this chunk of pink text into the gameplay)
    #----
    #I rechecked this pink text situation. 
    #The instruction says to only include it in 4.7, if the player couldn't read it in 4.5 (different path). However, the last choice before that is in 4.3.. 
    #In other words, it should okay to remove all this.
    #@catharisgaze
    #----
    #call lbl_PathB_4_5_o from _call_lbl_PathB_4_5_o_1
  ## OPTIONAL END ##"
  
  return
  #-----------------------------------------------
  
label lbl_PathB_4_7_2:
  
  
  play music music_eerie
  show merona t content
  show lexan neutral
  mk "..."
  play music music_eerie
  show merona t serious
  show lexan serious OM
  #TODO [B4.7 L12
  ln "If you knew what was entirely in store for you, would it help... quell down your curiosity?"
  show merona t worried OM
  show lexan serious
  mk "If I heard it?"
  show merona t serious OM
  show lexan neutral
  mk "Actually..."
  show merona t serious
  mk "..."
  show merona t determined OM
  show lexan sadSmile
  mk "...Yes. I suppose if you'd like to share it, it'd help. But only if you actually want to do so."
  show merona t determined
  mi "I don't want to force him to say anything that he wouldn't, so I won't make him cough it up, but if he truly does want to tell it himself, then I won't stop him."
  show merona t serious
  show lexan neutral OM
  ln "I'll tell you a little. I think you can figure it out yourself later on, so I won't tell you the whole reason, but maybe a small bit of information can help you."
  show lexan neutral
  "I shrugged."

  show merona t serious OM
  mk "That's perfectly fine. I'll accept that."
  show merona t worried
  show lexan determined OM
  ln "Okay. Something else you have to do relates with... why what happened to you happened to you at the monster attack."
  show merona t worried OM
  show lexan determined
  mk "Why what happened had happened..."
  show merona t worried
  show lexan neutral
  mi "I believe that this was already weighing on my mind before, but now a few more pounds have been added to it if it happens to be related to another objective."
  play music music_piano
  show merona t determined OM
  show lexan sadSmile
  mk "Thanks for telling me, Lexan, but I'll try and not think about this too much. I don't want to let it consume my thoughts."
  show merona t surprised
  show lexan neutral OM
  ln "Do whatever works for you. Don't forget that all the people here are looking out for you, so if you need to speak to someone, any one of us is fine."
  show merona t grin
  show lexan content
  "I grinned and stuck my hands at my hips."
  show merona t happy
  mk "I won't let myself get bogged down."
  show merona t content
  show lexan wink 
  "Lexan winked, tucking his book under his armpit."
  show merona t blushSmile
  show lexan wink OM
  ln "It's one of the things you're superb at."
  show lexan grin
  mk "Psh."
  show merona t content OM
  show lexan content
  "I'm going to go back and organize some of my things. Have fun with lesson plans."
  show merona t content
  "He saluted me."
  show lexan content OM CE
  ln "Will do."
  return
  #-----------------------------------------------
  
  
  #-----------------------------------------------
  # CHAPTER 5
  #-----------------------------------------------
label lbl_PathB_5_2_1:
  
  #play music music_Radio_Martini #(from before)
  show cg forest22 #(from before)
  #(sprite positions as before)
  show cimaria content:#; left from Kreita:
    yalign 1.0
    xalign 0.3
  show kreita content#, center
  show merona t content OM:#, right from Kreita:
    yalign 1.0
    xalign 0.7
  show rett content:#, right from Merona
    yalign 1.0
    xalign 0.9
    
  mk "I'll go to the marketplace!"
  show merona t content
  mi "Might as well put my plant-identifying techniques to use if I can. "
  return
  #-----------------------------------------------
label lbl_PathB_5_2_2:
  
  #TODO [fade in CG town
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg_sky1
  show clouds at leftright
  show cg town
  show cimaria neutral:#; left
    yalign 1.0
    xalign 0.1
  show boyen content:#; left from center
    yalign 1.0
    xalign 0.4
  show merona t content:#; right from center
    yalign 1.0
    xalign 0.75
  show lexan content:#; right
    yalign 1.0
    xalign 1.1
  "Kreita huddled her group together, and the rest of us gathered into a cluster as well. Cimaria clapped her hands."

  show cimaria neutral OM
  show boyen neutral
  ck "The herb you should look for can be found in this area, if the map is accurate. I assume that it may or may not be on display in some shops since it is more of an unique plant used for certain medical reasons, so you can also try asking the owner if they have it."

  ck "Ask for yander. That is the common name it has."

  show cimaria neutral
  "I raised my hand."

  show merona t content OM
  mk "Any recommendations on what type of shop to look in?"

  show cimaria neutral OM
  show merona t content
  ck "Medicinal or herbal shops are the ideal places to look. General-item shops are hit and miss, and food-only shops usually will not have it. Avoid any store that does not sell living things."

  play music music_recollections
  show cimaria surprised
  show boyen worried OM
  show merona t worried
  show lexan worried
  bg "Do you think we'll really be able to find it here?"

  show cimaria serious
  show boyen worried
  "Cimaria sighed and bit her lip."

  show cimaria serious OM
  ck "That is the biggest worry here. The map indicates that there should not be an ample amount of yander in this area, so it may not be sold in this town. This place is not very large or busy as a city, so it is likely that local things are sold here more often than imports or findings elsewhere."

  show cimaria neutral
  show merona t sadSmile
  show lexan determined OM
  ln "We would still have to pass through here anyhow to move on, so we might as well look around, right? I do hope that that map is correct."

  show merona t sadSmile OM
  show lexan neutral
  mk "True. If we can't find anything, then we'll have to move on. There's bound to be something found in the road ahead though... right? We just have to try to find it here, and if not, hope that we can find some as soon as possible before Rett breaks down."

  return
  #-----------------------------------------------
label lbl_PathB_5_3:
  
  play music music_Words
  #scene cg town #(from before)
  #(positions as before)
  show cimaria neutral CE#; left
  show boyen worried#; left from center
  show merona t sadSmile#; right from center
  show lexan neutral#; right
  "Cimaria nodded and rubbed her hands together."
  show cimaria neutral OM
  show boyen neutral
  show merona t content
  ck "Yes to all of that. We should hurry on over then, but first let's split ourselves into smaller units for efficiency's sake."
  show cimaria neutral
  show boyen neutral OM
  bg "Well... two groups of two seem reasonable. How does that sound to everyone else?"
  show boyen neutral
  show lexan content
  "Lexan smiled."
  show lexan content OM
  show merona t grin
  ln "Sounds great! I can go with Merona, if that's alright. If we bump into anything we might need for our lessons, this would be a good opportunity to purchase it."
  show lexan content
  show merona t happy
  mk "I'm fine with that! I also think it'd be convenient."
  show cimaria content OM
  show boyen content
  show merona t content
  ck "Then Boyen and I will be a pair."
  show cimaria surprised
  show boyen grin at SlightLeftBump#; move him towards Cimaria to let him 'touch' her and then back
  "Boyen elbowed Cimaria."

  play music music_Dark_Red_Wine
  show cimaria serious
  show boyen happy
  show lexan surprised
  show merona t surprised
  bg "More like a delicious green pear, am I right?"
  show boyen happy S
  show lexan neutral
  show merona t sadSmile OM
  mk "Ha... ha."
  show cimaria sadderSmile
  show lexan determined
  show merona t sadSmile
  "I was the only one who muttered out a response. The others simply gave their best forced half-smiles."
  show boyen sceptical
  show merona t serious
  mi "Oh, Boyen. Don't make me try to stuff a pear into your mouth."
  "Boyen shook his head."
  show cimaria serious
  show boyen tired OM
  show lexan neutral
  bg "You guys need to laugh a little sometimes."
  show boyen tired
  "I shrugged."
  show boyen neutral
  show merona t serious OM
  mk "It's hard to laugh at things like that, Boyen."
  show cimaria surprised
  show boyen content OM
  show lexan confused
  show merona t surprised
  bg "The more you laugh the more food I'll give you in your portions!"
  show cimaria neutral
  show boyen content
  show lexan sceptical
  show merona t determinedGrin
  "I shook my head, smirking at him."
  show cimaria content
  show merona t determinedGrin OM
  mk "Don't think that you'll be able to tempt me with food! No offense to your cooking though, the stuff you make is pretty nice."
  play music music_Cool_Steel_Breeze
  show lexan content OM
  show merona t content
  ln "*laugh* Alright, alright, I think we can all come up with better puns later. Let's go before we run out of time."
  show cimaria content OM
  show boyen grin
  show lexan content
  ck "See you around, and good luck!"
  show cimaria content#; fade out~
  pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")
  hide cimaria
  hide boyen
  show lexan neutral at WalkBounce
  show merona t content at WalkBounce
  "Cimaria and Boyen waved us off and went towards the west side of town, which made Lexan and I go to the east side. As we walked down, I scanned the area for possible shop suspects."
  mi "Seems like there are plenty of shops that'll have a good chance of containing the yander. I see a lot of greenery scattered around. Hopefully, they aren't merely store décor... I wonder if it'd be too inappropriate if I looked at some plants to put in my room back at the academy, but only after we get what we need."

  show lexan content
  "I looked to Lexan."
  show merona t content OM
  mk "Did you have anything in mind when you said there could other things we to buy here?"
  show merona t content
  show lexan content OM
  ln "Yes, I actually did. I might get some things for demonstrative and experimental purposes for Duran and some special mutated plants that'd help you work on your skill."
  show lexan neutral OM
  ln "By the way, how is your enhancer holding up?"
  show lexan neutral
  "I took the enhancer out of one of my pouches."
  show merona t content OM
  mk "We haven't been using it too much lately, so it looks like I still have around half to three-quarters of the bottle left. That should last long enough, right?"
  play music music_Travel_Light
  show merona t content
  show lexan happy OM
  ln "Yes, it should. Are you interested in any other types of enhancers though? This one that you have already is a general enhancer. There are other varieties that focus on different aspects of your ability."
  show merona t reflective
  show lexan grin
  mi "Different types of enhancers, huh? I wonder what kinds there are. What if I developed an enhancer that help people strengthen their connection to plants more, ultimately letting them to talk to them? "

  show merona t grin
  mi "Yeah, I'm going to have to patent that one."

  show merona t serious
  mi "For now, I'm not feeling too strongly about getting more for myself though."
  show merona t serious OM
  show lexan surprised
  mk "If we bump into some, we could take a look. I don't really care if we get it or not, but it might be better if we save some money by not getting it if it's just something extra."
  show merona t surprised
  show lexan strict
  "Lexan shook his head at me."
  show lexan strict OM
  ln "We have enough money to afford an extra enhancer, so don't worry about our budget. As long as we don't go crazy spending money on personal or additional items, we should be fine."
  play music music_Up_Kilkenny
  show merona t happy
  show lexan grin
  mk "*laugh* Well, if we're ever broke and can't afford anything, we're at least warm as long as there are flammable things in the woods."
  show merona t grin
  show lexan laugh
  ln "If we ever run out of those things, we could always burn up Duran. He'd be great burning material since he's got all that fire-energy inside him."
  show merona t determinedGrin OM
  show lexan determined
  mk "Unfortunately, he is fire-retardant, so we will not be able to use him as fuel. Instead, I guess you could plant me into the soil, continue travelling, come back, and then find a sprouted Merona plant. "

  show merona t content OM
  show lexan grin
  "Light the Merona plant on fire with Duran, and then that's the challenge of the lesson! Learn how to survive with our own elements."
  show merona t content
  show lexan grin CE
  "Lexan held his hand out in a handshake."
  show merona t grin
  show lexan laugh
  ln "Deal. I'll add that to my lesson plans immediately."
  show merona t determinedGrin
  show lexan grin
  "I clasped his hand in agreement, and we shook on it."
  show merona t content OM
  show lexan content
  mk "Excellent. You should add a disclaimer though, that nobody was harmed in this lesson. Just to make sure."
  show merona t content
  show lexan laugh CE
  ln "*laugh* Of course."

  play music music_life
  $ renpy.transition(slow_dissolve, layer="master")
  show cg townShops
  show merona t grin
  show lexan content
  "The line of shops were approaching. I brightened up at the first shop, seeing the assortment of herbs and plants displayed on the table."

  show merona t worried
  mi "So far, things aren't looking bleak. But now I realize that we have a tiny issue#; Cimaria didn't tell us the details of what yander looks like."

  show merona t serious
  mi "I'll have to count on the shopkeepers knowing its appearance or see if they have yander labeled somewhere in their store."
  show merona t surprised
  show lexan content OM
  ln "Now that we've got that lesson 'planned out', I was randomly wondering-how have you been doing lately?"

  show merona t content
  show lexan content
  "We reached the lineup of stores and began browsing. This first one we encountered was a specialty shop for gardening or plant-growing it seems, so it's a good start."
  play music music_piano
  show merona t content OM
  mk "How have I been? Good. Better at least from before, when I was worried about Rett. I'm still pretty anxious about his situation, but now that we're actually doing something that could actively help him, this tones my worry down."
  show merona t surprised OM
  show lexan surprised
  mk "How 'bout you?"
  show merona t content
  show lexan neutral OM
  ln "Similar to how you are feeling, I suppose. Still have a bit of stress weighing me down, but I'm not too shabby."
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan content:
    yalign 1.0
    xalign 0.9
  #TODO [move Merona to a spot left from the center please~
  show merona t content:
    yalign 1.0
    xalign 0.4
  show townHerbs #in front of Merona and Lexan
  "A small table had boxy pots with growing herbs in them. I went over there, peeking at each little tab with the herbs' names written on, and Lexan, not straying too far, observed more potted plants on another table."

  show merona t serious
  mi "No sign of yander yet."

  show merona t content OM
  show lexan neutral
  mk "That's nice to hear. Wouldn't want you to feel terrible after all. You seem to be fine almost all the time though, really calm and collected. What's your secret?"
  show merona t content
  show lexan sceptical
  "Lexan raised an eyebrow."
  show merona t surprised
  show lexan sceptical OM
  ln "My secret?"
  show merona t grin
  show lexan neutral
  "I looked back at him and smiled."

  show merona t content OM
  mk "You either have some sort of trick that makes you permanently not delirious, or you're just really good at looking like you know what you're doing."

  show merona t sadSmile OM
  show lexan content
  mk "I'm going to assume that it's the latter case though."
  show merona t sadSmile
  show lexan sadSmile OM
  ln "Yeah, you're right. I don't think anyone knows of a special something that would make you always so put-together, especially not me. Most people frankly are great at acting like they've got everything settled when in truth nothing is ever settled."
  show merona t sadSmile OM
  show lexan content
  mk "It's a good skill to have though. I would want to have it."
  show merona t surprised
  show lexan determined OM
  ln "It comes over time. I consider myself to not be as calm and collected as you put me up to, so I guess I'm doing it well enough."
  play music music_romance
  show merona t determinedGrin
  show lexan surprised
  "I tsked at Lexan."
  show merona t determinedGrin OM
  show lexan grin
  mk "Ah, but you see I didn't exactly do that! I did say that I assumed you were good at disguising yourself as a capable person, so you and I still need to work on it."
  show merona t content
  show lexan happy OM
  ln "Touché, pal, touché."
  return
  #-----------------------------------------------
label lbl_PathB_5_4:
  
  #play music music_romance#(from before)
  #(Positions as in last chapter)
  show cg townShops
  show merona t grin
  show lexan content
  show townHerbs
  "I smiled at him and quickly refocused back to observing the tables."

  play music music_Cool_Steel_Breeze
  show merona t determined
  show lexan neutral
  mi "Can't get too caught up in talking. Must first get number one objective done!"

  #TODO [fade in CG townHerbShop
  $ renpy.transition(slow_dissolve, layer="master")
  show cg townHerbShop
  hide lexan
  show merona t serious#; position as before #(left side)
  "I stepped through the open doorway into the building and moved to the payment counter, checking out the small goodies laid out and arranged to tempt customers to purchase even more things, but to no avail, there was no sign of yander. The clerk was occupied with another customer, presenting some of the products hanging from the walls."

  show merona t worried
  mi "I doubt that such an unpopular plant would have been placed on full display like that, so I shouldn't be surprised that it isn't there. I just need some kind of indication that this shop does have it though!"

  show merona t serious
  mi "..."

  show merona t surprised
  mi "Wait..."
  show merona t determined
  mi "Since this is an herb shop, it should have some kind of plant directory right? Even if this place doesn't sell what we need in particular, a full plant directory would have an image and description of it. "

  $ renpy.transition(slow_dissolve, layer="master")
  scene cg townShops
  show lexan neutral:
    yalign 1.0
    xalign 0.9
  show townHerbs 
  pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t serious behind townHerbs:
    yalign 1.0
    xalign 0.4
  "I popped my head outside the door to Lexan who was still outside."

  show merona t serious OM
  mk "Any luck with finding yander?"

  show merona t serious
  show lexan neutral CE
  "He shook his head."

  show lexan neutral OM
  ln "None at all."

  show merona t content OM
  show lexan neutral
  mk "Same for me. But, I have another idea."

  show merona t content
  show lexan sceptical OM
  ln "Move on to another store?"

  show merona t content CE
  show lexan neutral
  "This time, I shook my head."

  play music music_potHappy
  show merona t happy
  show lexan surprised
  mk "We'll do that soon, but I have a different idea! If there's a plant directory here, yander will most likely be in it, and we would be able to find out what it looks like and other details about it. Knowing that would help us tremendously."

  show merona t grin
  show lexan happy OM
  ln "Ah, I see! Good idea. Did you realize this method because you've gone shopping for herbs like this?"

  show merona t content OM
  show lexan content
  mk "Actually, no. The academy provides the herbs we need for classes which don't grow from Laneo, so I've never needed to go out and buy those myself. If they are locally available, sometimes we'll be assigned to find them ourselves."

  show merona t content
  show lexan grin
  "He grinned and crossed his arms."

  show lexan happy OM
  ln "Even better that you so immediately thought of this method. Is there a plant directory book in here though?"

  show merona t content OM
  show lexan content
  mk "We'll have to look for it. I actually have my own directory, but it's a pocket version, which doesn't have yander in it. A complete version will have what we need. Try to find a thickish book with illustrations of plants, and that should be it."

  show merona t content
  show lexan determined OM
  ln "Doesn't seem too difficult to find. I'll do my best to find it."

  show merona t happy
  show lexan content
  mk "Let's start looking then! The clerk looks a bit busy right now, so we could ask her about it later if we need to."
  return
  #-----------------------------------------------
label lbl_PathB_5_5:
  
  #play music music_potHappy #(from before)
  #(positions as in end of last chapter:)
  show merona t content
  show lexan content
  "Lexan smiled in return."

  show lexan content OM
  ln "No time to spare, let's look once more."

  #TODO [fade to CG townHerbShop
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg townHerbShop
  show merona t serious:
    yalign 1.0
    xalign 0.4
  show lexan neutral:#; right from center
    yalign 1.0
    xalign 0.9
  "I moved away and gravitated to the table in the center of the shop where some cards were placed. I picked one up."

  show merona t surprised
  mi "A plant info card. Maybe this will suffice instead of a whole directory? That is, depending on if there's a card for yander... And also if the plants on these cards also correspond to the plants in this store."

  show merona t serious
  "Taking the whole deck in my palm, I flipped through each one. This set looked pretty thick, but I was already going through so much of it."

  show merona t worried
  mi "I haven't even seen a card with a word beginning with a \"y\". Then again, how many herbs start with that letter?"

  "Over half of the deck had been gone through."

  show merona t disappointed
  show lexan surprised
  mi "In a nice world, this deck would be alphabetical and would let me find a yander card, but alas, this is only a slightly decent world that doesn't."

  show merona t serious
  show lexan content OM
  ln "Hey Merona, I've found something interesting. Would you like to see it?"

  show lexan content
  "My eyes were stuck to the cards in my hands."

  show merona t serious OM
  show lexan neutral
  mk "Sure, can you come over and bring it with you? I think I may be on the brink of getting close to yander."

  show merona t serious
  show lexan content
  "Lexan joined me at the center table and waved a hand in front of my face, but still I didn't react."

  show merona t serious OM
  show lexan neutral
  mk "Sorry! Hold on for just five seconds, I'm almost there..."

  play music music_Radio_Martini
  show merona t surprised
  show lexan determined OM
  ln "Five seconds you say? One..."

  show merona t disappointed
  ln "Two..."

  show merona t disappointed OM
  show lexan determined
  mk "That was just an exaggeration!"

  show merona t sadSmile
  mi "I feel like going a lot faster now..."

  show merona t determined
  show lexan determined OM
  ln "Three..."

  show merona t determined OM
  show lexan determined
  mk "A pretty commonly used exaggeration where I take maybe around twenty seconds!"

  show merona t determined
  show lexan determined OM
  ln "Four..."

  show merona t determined OM
  show lexan determined
  mk "Almost there!"

  show merona t determined
  show lexan determined OM
  ln "...and a half..."

  show lexan grin
  mk "..."

  show merona t determined OM
  mk "Only about fifteen cards left!"

  show merona t determined
  show lexan grin OM
  ln "...and three quarters..."

  show lexan grin OM CE
  mk "...and three and a half quarters..."

  play sound sound_bump
  show merona t determinedGrin
  show lexan surprised
  "I slapped the finished deck down and grinned in triumph."



  play music music_Dark_Red_Wine
  show merona t determinedGrin OM
  show lexan neutral
  mk "Done."

  show merona t determinedGrin
  show lexan content
  "Lexan's small smile had hints of confusion and amusement in it."

  show merona t surprised
  show lexan sceptical OM
  ln "Why so rushed though? What did you think I was going to do after I got to five seconds?"

  show merona t sadSmile OM
  show lexan neutral
  mk "I can't help but get jittery when someone starts counting! Makes me feel like I'm being timed for something..."

  show merona t content OM
  show lexan grin
  mi "...which what was technically happening..."

  show lexan surprised
  mk "What would you have done once you were done counting?"

  show merona t content
  show lexan grin OM
  ln "Shown you this."

  return
  #-----------------------------------------------
label lbl_PathB_5_6:
  
  play music music_Dark_Red_Wine
  show cg townHerbShop #(as before)
  #TODO [Positions as in end of last chapter please
  show merona t surprised
  show lexan grin
  "He dangled a packet in front of my face. I focused onto the swinging item, trying to read the words on it."

  show merona t surprised OM
  mk "What's this?"

  show merona t serious
  show lexan content
  "I grabbed hold, stabilizing it."

  show merona t serious OM
  mk "Ready-to-mutate seeds?"

  play music music_Summer_Day
  show merona t happy
  show lexan grin CE
  mk "For yander?"

  show merona t grin
  show lexan content
  "I stared at Lexan, wide eyed."

  mi "Ready-to-mutate seeds. The stuff you get for educational use. Didn't expect a general herb store to carry much of these kinds of things, but I won't reject it."

  show merona t happy
  mk "How did you find this?"

  show merona t grin
  show lexan wink
  "He shrugged."

  show merona t content
  show lexan happy OM
  ln "There was a small container tucked away in a corner, so I looked through it to find these types of seeds. Wasn't a very noticeable place, so I almost overlooked it, but it's good that I didn't."

  show merona t laugh
  show lexan surprised
  "I laughed and slapped his arm."

  show lexan content
  mk "Yeah, it's really good that you didn't! Can you let me see it more closely? I want to look for some more information on it."

  show merona t grin
  show lexan content CE
  "He nodded, and I pinched the seeds out of his hand."

  show merona t serious
  show lexan content
  mi "The tag says it's going to take four or five days to be fully grown... Would that be okay for us? At least it doesn't need to be extensively taken care of it seems. And since the seeds are ready-to-mutate, its own elements will be pure and strong by itself. I could attach some other seeds that have around the same growing speed. "

  play music music_Words
  show merona t content OM
  mk "If we're going to get this, we'll have to buy some other things. Containers for it to grow in, suitable soil, some other plants to enhance it, etcetera."
  return
  #-----------------------------------------------
label lbl_PathB_5_7:
  
  #play music music_Words #(from before)
  show cg townHerbShop #(as before)
  #TODO [Positions as in end of last chapter please
  show merona t content
  show lexan content OM
  ln "How much of that do we already have?"

  show merona t happy
  show lexan content
  mk "Mmh, we could get some things technically for free if we take them from the forest. Since this area supposedly has yander native to it, we're able to use its soil. Don't we have some spare pots as well that were for my lessons? Boom, covered on that too."

  show merona t content OM
  mk "Ultimately, we would only need to buy other types of seeds and maybe something to speed its growth."

  show merona t grin
  mi "Not too shabby of a deal, if I do say so myself."

  show merona t content
  show lexan content OM
  ln "Sounds doable. I don't have anything I wish to buy, so if that's all we need from this place, let's just get it and leave."
  show merona t content OM
  show lexan content
  mk "Okay. Do you want to immediately go to our meeting place after we're done?"
  show merona t content
  show lexan content OM
  ln "I think it's fine to do that."
  show lexan content
  "I nodded, looking around the room."
  show merona t content OM
  mk "Where did you get the seeds?"
  show merona t content
  show lexan content OM CE
  ln "I can get them for you. Other than yander, what else do you need?"
  show merona t surprised OM
  show lexan content
  mk "I think..."
  show merona t reflective
  mi "Hm. I don't know the specific properties of yander, but I can at the very least try to get other plants that I know are beneficial in healing or can be easily mutated and grown with it."

  show merona t content OM
  show lexan grin
  mk "I think I'll just get them myself. I have a general idea about what other types of seeds to use."

  show merona t serious
  show lexan happy OM
  ln "Okay. Well, the place I found them are on the stand next to the payment counter, so you might as well pay right at that moment. You also said you wanted an enhancer for growth speed right?"

  play music music_recollections
  show merona t worried
  show lexan content
  mi "Right. I did say that. But..."

  show merona t serious
  mi "Should I get an enhancer that I directly inject into the growing plant or just use my own enhancer that I already have to speed the growth of the plant with my own skills?"

  show merona t reflective
  mi "The perk of using a direct enhancer is that it's easy and basically successful in all cases if used correctly, but it can only speed it up for a set amount of time. "

  show merona t worried
  show lexan neutral
  mi "Not to mention that too much can ultimately poison the plant."

  show merona t reflective
  mi "If I were to use my own ability, I could speed it however fast I want. If done with control over the life flow, it could be ready rather quickly. "

  show merona t disappointed
  mi "The faster I make it though, the more strenuous it is on me, and the more uncontrolled I'm likely to get."

  show merona t serious
  show lexan sceptical
  mi "I don't know for sure if I can speed up growth with my skills even with an enhancer running in me, but I could still try to learn more tips and practice. Unfortunately, that doesn't sound like a solid decision either..."

  show lexan sceptical OM
  ln "Is... something the matter?"

  show merona t worried OM
  show lexan neutral
  mk "Well, uh..."

  show merona t worried
  show lexan worried
  "I scratched my head and bit down on my tongue."

  show merona t worried OM
  show lexan neutral
  mk "I was debating whether I should get a new enhancer or just rely on my own one. Because with the one I already have, I could try speeding the growth with my skills."

  show merona t serious
  show lexan neutral OM
  ln "Oh, I see. In that case, you're weighing both options in."

  play music music_life
  show merona t surprised
  show lexan content OM
  ln "What if you simply buy the new enhancer and also use your current personal one? Having both would not exactly be detrimental."

  show merona t surprised OM
  show lexan content
  "I stared at him, blank faced."

  show lexan surprised
  mi "I..."

  show merona t embarrassed
  show lexan confused
  mi "...am an idiot."

  show merona t embarrassedSmile
  show lexan sadSmile
  "Clenching my teeth into a smile, I nodded."

  show merona t embarrassedSmile OM
  show lexan content
  mk "I'll go with what you said."

  show merona t serious
  mi "Using both really is something without too many repercussions. I can test some plants with each one and other methods."

  show merona t grin
  mi "I'll think more about how to use them later. Let's go and buy the goods right now."

  show merona t content:#; move her sprite to the left please
    yalign 1.0
    xalign 0.4
  show lexan neutral
  "Though he wasn't aware of the location of the enhancers, Lexan pointed out where the seeds were. I headed there first, grabbing five packets of yander and more packs of other types of plants to mix with."

  mi "Even if these won't do, I bet Cimaria has some herbs of her own that could be used too. We'll find a way."

  show merona t serious
  "As I scanned the room, I spotted a row of enhancers representing the mini rack for the packaged version on the payment counter."

  play music music_potHappy
  show merona t determinedGrin
  mi "Target locked on. Nice location too."

  show merona t content
  "I walked over and set the packets down on the table for a moment, allowing me to get my money out in the meantime as my eyes selected the box with the correct label. I detected the one for growth speed and placed it along the packet family."

  show merona t grin
  mi "Now that we have these items, all I have to do is collect the soil nearby and get out those pots from our cart. Sounds like a good plan."

  show merona t content:#; move to the right, a bit left from Lexan
    yalign 1.0
    xalign 0.5
  show lexan content
  "I exchanged the money for the products with the clerk, and skipped to Lexan who was already waiting by the main door."

  show merona t happy
  show lexan grin
  mk "Everything's set!"

  show merona t surprised OM
  show lexan neutral
  mk "What time is it right now by the way? Is the hour up?"

  show merona t content
  show lexan neutral OM
  ln "Perhaps. Since we're already finished with our share, let's go wait at our meeting place nonetheless."

  show merona t content OM
  show lexan sadSmile
  mk "Sure, let's go! Maybe the others have also succeeded in their findings."

  play music music_piano
  show merona t content
  show lexan sadSmile OM
  ln "We can only hope for that... But it seems like things are looking up a little. Becoming a lot smoother."

  scene bg black with fade
  return
  #-----------------------------------------------
label lbl_PathB_5_8:
  
  #play music music_piano #(from before)
  $ renpy.transition(slow_dissolve, layer="master")
  scene bg black
  pause(0.5)
  scene cg_sky1
  show clouds at leftright
  show cg town
  show merona t content:#; left side
    yalign 1.0
    xalign 0.25
  show lexan neutral:#; right side
    yalign 1.0
    xalign 0.75
  "The two of us went off onto the road, and we traversed in the direction of the meeting place. I crossed arms and nodded to myself."

  show merona t happy
  show lexan content
  mk "Wow, I'm really glad that we accomplished something today."

  show merona t grin
  mi "I didn't expect much out of search as to not let my hopes down, but things were alright! I should have more faith."

  show merona t content
  show lexan grin CE
  "Lexan bantered around and nodded as well."

  show lexan content OM
  ln "Accomplishing something is rather noteworthy."


  play music music_Radio_Martini
  show merona t surprised
  show lexan grin OM CE
  ln "Even more so when it's us two."

  show merona t serious
  show lexan grin
  "I crossed my arms."

  show merona t disappointed OM
  show lexan determined
  mk "Was that an indirect insult?"

  show merona t disappointed
  show lexan determined OM
  ln "Actually, it was a pretty direct insult."

  show merona t serious
  show lexan content OM CE
  ln "But I should mention that I was also being sarcastic."

  play music music_Ill_be_right_behind_you_Josephine
  show merona t grin ER
  show lexan grin
  "I rolled my eyes in mock annoyance and smiled to the side."

  show merona t content OM
  show lexan content
  mk "Direct or indirect insult, sarcastic or real, I'm still pleasantly surprised at what we got. It was more out of luck that we found the stuff, but still, we did succeeded at it!"

  show merona t content
  show lexan content OM
  ln "I know what you mean. And with our things, we can apply more of our lessons to this actual real-life situation we're in. So hey, you're getting educated and contributing to the team."

  show merona t grin
  show lexan neutral
  "I snorted."

  show merona t content OM
  show lexan sadSmile
  mk "Good to know that I'm not just one of the kids who aren't capable of doing anything."

  show merona t worried OM
  show lexan worried
  mk "But honestly, I do worry if I can be useful for Rett and everyone else. I don't know... I'm not used to having this kind of position in a group."

  show merona t worried
  show lexan sadSmile OM
  ln "Everyone has to start somewhere, right? This is certainly not the best kind of case for you to be a heavier weight of importance in the team than you usually are as a student, seeing how someone's life is questionable..."

  show merona t serious
  show lexan determined OM
  ln "...But things happen, and you have to deal with it. You can do it though."

  show merona t content OM
  show lexan determined
  mk "Yep. As unfortunate as everything seems... It's still exciting! That kind of excitement should help me for sure."

  play music music_Words
  show merona t content
  show lexan content
  "I looked further over to the side of the road and saw wild flowers in mounds of dirt speckled around the outskirt of the forest jutting right before the buildings."

  show merona t reflective
  mi "Do I have some kind of container on me right now? Because I could just go to that soil and scoop it up. Convenient place."

  show merona t disappointed
  "I stared after the patch as we got closer, for staring was the only thing I could do in my bagless state."

  show merona t grin
  mi "The flowers are pretty... But right now the dirt looks a lot more beautiful!"

  scene bg black with fade
  return
  #-----------------------------------------------
label lbl_PathB_5_9:
  
  stop music
  $ renpy.transition(slow_dissolve, layer="master")
  scene bg black
  pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg_sky1
  show clouds at leftright
  show cg town
  show lexan sceptical:#; right edge of the screen
    yalign 1.0
    xalign 1.0
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t surprised:#; left from Lexan
    yalign 1.0
    xalign 0.7
  mi "Apparently the others found more members of the team instead of yander."

  play music music_Nincompoop
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita fishAnimated happy at LeftToAlmostCenter#; left from Merona #(animation: move her horizontally to the end position a bit#; use Kreita bodyFish +Kreita bodyFish2 please)
  kh "Look what I have!"

  show kreita fishAnimated grin:
    yalign 1.0
    xalign 0.4
  show merona t serious
  show lexan confused
  "As Kreita squealed, she stuck out a clump of rotting fish in her fist as if they were medals she was showing off."

  show merona t nervous
  mi "More dead team members that is."

  $ renpy.transition(slow_dissolve, layer="master")
  show duran t embarrassed:#; left from Kreita
    yalign 1.0
    xalign 0.25
  show kreita fish pouty
  show lexan neutral
  "Duran sighed and looked down."

  show duran t angryBlush OM
  show merona t sadSmile
  dt "Can you put it away now? You don't have to keep it out in the air..."

  show duran t annoyed EL
  show kreita fish fierce OM
  show lexan sceptical
  kh "Take pride in what we've found, my boy!"

  show kreita fish fierce
  show merona t grin ER
  "Kreita shook her finger at all of us, and I stifled back a scoff."

  play music music_Radio_Martini
  show duran t annoyed
  show kreita fish happy
  show merona t content
  show lexan surprised
  kh "This is really nice you know. The people there told us it was good for fertilizing soil. And they just gave it to us too! Win-win situation for everyone."

  show duran t angry CE
  show kreita fish content
  show lexan neutral
  "Duran scowled to himself."

  show duran t annoyed OM
  show kreita fish neutral
  show merona t sadSmile
  dt "More like lose-lose..."

  show duran t sad OM
  show kreita fish pouty
  dt "We got trash and they got nothing from us."

  show duran t flabber
  show kreita fish fierce OM CE
  show merona t grin
  kh "Oh Duran, did you say that you wanted to observe this some more?"

  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria annoyed behind kreita:#; left from Kreita
    yalign 1.0
    xalign 0.3
  show duran t angry:
    yalign 1.0
    xalign 0.2
  #TODO [move Duran's sprite to the left to make room for Cimaria
  show kreita fish grin2
  show lexan serious
  "She jiggled the fish into his face, the tails bouncing dangerously close into his nostrils. He staggered back and swatted at Kreita. Cimaria intervened and separated the two."
  play music music_White
  show duran t tired
  show kreita fish grin2 S
  show merona t content
  show cimaria annoyed OM 
  ck "Okay, okay, stop before someone kills themselves. Let's get reports going on how we all did."

  show kreita fish sad
  show cimaria neutral OM
  ck "I take it that you two got these dead fish. Is that all?"

  show duran t tired OM
  show cimaria neutral
  dt "Nothing else."

  show duran t neutral
  show kreita fish sad OM
  show merona t grin
  show lexan neutral
  kh "Can it be used in some way?"

  show kreita fish neutral
  "I nodded and answered."

  show duran t surprised
  show kreita fish grin
  show merona t happy
  show lexan content
  show cimaria surprised
  mk "Lexan and I found yander seeds in our search, so yeah! It would be great to have for us."

  play music music_Dark_Red_Wine
  show kreita fish happy
  show merona t grin
  show cimaria content
  kh "Hooray!"

  show duran t annoyed
  show kreita fishAnimated grin
  show cimaria serious
  "Kreita flung her fish around like she was ringing a bell."

  show duran t annoyed EL
  show kreita fishAnimated happy
  show lexan grin CE
  kh "We did something useful!"

  show duran t annoyed OM
  show kreita fishAnimated fierce
  show merona t sadSmile
  show lexan neutral
  dt "You didn't get drunk from the fish too, did you?"

  show duran t angry:
    yalign 1.0
    xalign 0.2
  show kreita fish grin2:#; move her to Cimaria's position and Cimaria to Kreita's
    yalign 1.0
    xalign 0.3
  show cimaria serious:
    yalign 1.0
    xalign 0.5
  show merona t content
  "Kreita propped her elbow on Duran's head and rested her chin on her palm."

  show duran t nervous
  show kreita fierce OM
  kh "I can slap you in the face with this fish like it's a bottle of wine too, if you'd like."
  
  play music music_Cool_Steel_Breeze
  $ renpy.transition(slow_dissolve, layer="master")
  show rett neutral behind duran:#; left from Duran
    yalign 1.0
    xalign 0.0
  $ renpy.transition(slow_dissolve, layer="master")
  show prowen neutral:#; left from Rett/ left edge of screen
    yalign 1.0
    xalign -0.15
  show kreita content
  show duran t neutral
  show cimaria neutral OM
  ck "Prowen, Rett, how did you guys do?"

  show prowen neutral OM
  show cimaria neutral
  pm "Only got tips for preservation... nothing else."

  return
  #-----------------------------------------------
  
  
  #-----------------------------------------------
  # CHAPTER 6
  #-----------------------------------------------
label lbl_PathB_6_0_1:
  
  #play music music_Cool_Steel_Breeze #(from before)
  #TODO [Character positions as in end of last chapter
  show lexan sceptical
  show merona t serious
  show kreita sceptical
  show duran t tired
  show cimaria surprised
  show prowen surprised
  show rett confused OM
  rt "Really? Did I miss something when we were talking to the guy?"

  show duran t neutral
  show cimaria serious
  show prowen neutral
  show rett confused
  "Prowen shrugged and looked at Rett."

  play music music_Ill_be_right_behind_you_Josephine
  show merona t worried
  show lexan worried
  show kreita worried
  show prowen worried OM
  show rett worried
  pm "Maybe you zoned out. You've got a lot to think about, right?"

  show cimaria worried
  show prowen worried
  show rett worried OM
  rt "Eh... I guess. Yeah, that's probably what happened. Either that, or this monster venom is giving me bad short term memory."

  show merona t serious
  show rett worried
  mi "That sounds kind of plausible when I think about it. "

  show merona t worried
  show cimaria serious
  "Anything sounds kind of plausible when dealing with this poison though."

  show duran t worried
  show cimaria serious OM
  show lexan neutral
  show rett content
  ck "I... certainly hope that's not actually the case."

  show kreita serious
  show cimaria worried OM
  show prowen neutral
  show rett surprised
  ck "But if you'd like, I could check to see if something strange is going on with your brain."

  show merona t serious
  show duran t neutral
  show cimaria worried
  show prowen neutral OM
  show rett neutral
  pm "Um, anyways, about what we got..."
  return
  #-----------------------------------------------
label lbl_PathB_6_0_o:
  
  #"  ## OPTIONAL  ##"

  play music music_Dark_Red_Wine
  show merona t surprised
  show lexan surprised
  show kreita grin
  show duran t surprised
  show cimaria surprised
  show prowen surprised
  show rett grin at LeftBumpSmall#; move his sprite a bit towards Prowen's and then back to the initial position
  "Rett chuckled and slapped Prowen on the back."

  show merona t sadSmile
  show lexan confused
  show kreita grin2
  show duran t annoyed
  show cimaria neutral
  show prowen forcedSmile
  show rett laugh ER
  rt "*laugh* Now if he forgot about them too, that'd be funny."

  show lexan neutral
  show prowen forcedSmile CE
  show rett grin
  "Prowen shook his head and closed his eyes for a moment."

  play music music_recollections
  show merona t content
  show kreita content
  show prowen neutral OM
  show rett smirk
  pm "Don't worry, I remember."

  show merona t surprised
  show lexan serious
  show duran t neutral
  show prowen sceptical OM
  show rett neutral
  pm "The guy gave a number of methods, but some of them may not work out well for us."

  show merona t serious
  pm "For example, a lot of them involved cutting the meat into slabs."

  show merona t sadSmile
  show lexan annoyed
  show kreita grin
  show duran t annoyed CE
  show cimaria sadSmile
  show prowen appalled
  show rett grin S
  $ renpy.transition(slow_dissolve, layer="master")
  show boyen happy:
    yalign 1.0
    xalign -0.3 
  show boyen happy:#; slide in at left side #(can overlap with Rett, he's not going to stay long...)
    yalign 1.0
    linear 1.0 xalign 0.05 
  #pause(0.5)
  bg "If we were eating the monster, that'd be good. In fact, if it comes down to us needing to eat it, we could-"

  
  
  show lexan serious
  show duran t annoyed
  show prowen appalled OM
  show boyen happy S
  pm "-Um, moving on..."

  show merona t content
  show prowen sceptical
  show kreita content
  show rett neutral
  show boyen worried
  "Boyen held up his palms."


  show merona t grin
  show lexan serious CE
  show duran t annoyed EL
  show cimaria serious
  show prowen annoyed
  show rett grin CE S
  show boyen worried OM:#; move to the left while fading sprite out
    yalign 1.0
    linear 10.0 xalign -1.0 
  pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")  
  hide boyen
  bg "Sorry, I'll stop talking now."

  play music music_Sugar_On_My_Tongue
  show merona t serious
  show lexan serious
  show duran t neutral
  show cimaria neutral
  show prowen sceptical OM
  show rett neutral
  pm "So, all of his advice revolved around preserving meat when it's cut into smaller pieces."

  show kreita neutral
  show prowen sceptical OM
  pm "There's no mention of it being applicable to the animal-or monster in our case-when it's whole."

  show prowen neutral
  pm "..."

  show merona t content
  show lexan determined
  show kreita fierce
  show prowen determined OM
  show rett content
  pm "We could still try it though."

  show kreita content
  show prowen neutral
  "He finished but quickly jumped back in."

  #(slightly more urgent voice)
  show merona t serious
  show lexan surprised
  show kreita neutral
  show cimaria neutral
  show prowen determined OM
  show rett surprised
  pm "I've tried storing meat on my own a long, long time ago. But that was for typical meats, so I didn't think of doing the same thing for this situation."

  show lexan worried
  show prowen determined
  mi "This is probably the most that I've heard Prowen say all at once. He's onto something good... I want to keep poking him for more info, but he would probably get annoyed back into saying very little."

  show merona t content
  show lexan worried OM
  show kreita content
  show duran t surprised
  show cimaria serious
  show prowen content
  show rett content
  ln "*sigh* I mean, it's better than nothing. And if you've already got experience with any kind of preservation of that sort, then we should gladly accept it. Thank you for informing us."

  show lexan neutral
  show duran t annoyed
  show prowen neutral
  "Duran crossed his arms and frowned, turning into an officer waiting for the witness to provide more information."

  show merona t serious
  show duran t annoyed OM
  show rett neutral
  dt "Okay, but... You still haven't told us exactly what to do. Care to share?"

  play music music_life
  show merona t surprised
  show lexan surprised
  show kreita grin
  show duran t surprised
  show cimaria surprised
  show prowen neutral OM
  show rett surprised
  pm "Salt the monster."

  show lexan sceptical
  show duran t surprised
  show cimaria serious OM
  show prowen neutral
  ck "That's all? Just put salt on it?"

  show kreita content
  show duran t surprised
  show cimaria serious
  show rett grin
  "Prowen nodded and looked to the side."

  show merona t grin
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

  show merona t content
  show kreita grin2
  show cimaria sadSmile OM
  show prowen content
  ck "Wow, that's a good tip. In fact, that's probably good enough that we don't need to actively search for another alternative. We should use this technique as soon as possible."

  show lexan surprised
  show kreita content
  show cimaria neutral
  show prowen content OM
  pm "We'll need more salt, so I'll run out and buy more. Should be pretty easy to find."

  show lexan neutral
  show prowen neutral#; fade out his sprite
  $ renpy.transition(slow_dissolve, layer="master") 
  hide prowen
  "Before anyone could reply, he strolled down to the nearby street of shops."

  show merona t reflective
  mi "Would they sell salt by the bulk in this kind of town? I mean, usually you'd expect to find large quantities of spices available for purchase in port cities, so a place like this wouldn't sell a big amount."

  show merona t reflective CE
  mi "Maybe we'll have to buy dozens upon dozens of salt packets."

  #"  ## OPTIONAL END ##"
  return
  #-----------------------------------------------
label lbl_PathB_6_0_2:
  
  play music music_Cool_Steel_Breeze
  show merona t content
  show lexan content OM
  show kreita determined
  show rett smirk
  ln "Great. So far, we have seeds from Merona and I, Kreita and Duran found fish for those seeds, Rett and Prowen know how to preserve the monster..."

  show lexan content
  show cimaria neutral OM
  ck "...And Boyen and I found powdered yander. I was planning to make a serum based off of that and add in a few extras to help increase potency."

  show merona t grin
  show lexan grin
  show duran t neutral OM
  show kreita grin
  show cimaria neutral
  dt "Well, well, well, I'm surprised. Everyone found something somewhat useful."

  show merona t determinedGrin
  show duran t neutral
  mi "If Duran's \"somewhat useful\" means \"very useful\", then I would have to agree!"

  show merona t content
  show lexan neutral
  show cimaria serious CE
  show rett neutral
  "Cimaria tsked and nodded."

  show kreita content
  show cimaria serious OM
  ck "Yes, we all did find items even if we couldn't get actual yander. But what we have still works out. We are on a good track."

  show kreita fishAnimated grin2
  show duran t annoyed
  show cimaria serious
  "Kreita thrashed her fish around again like a happy baby with a rattle."

  show kreita determined OM
  show lexan determined
  show duran t neutral
  show rett worried
  kh "Let's start moving on since we've got the necessary stuff. Or more specifically, let's sow the seeds and then move on. We still need to hurry for Rett's sake."

  show kreita determined
  show lexan neutral
  show rett neutral CE
  "Rett swatted his hand and shook his head."

  show kreita content
  show cimaria worried
  show rett neutral OM
  rt "Take the time you need to properly develop the seeds. I'm fine over here."

  show merona t determined
  show lexan determined
  show cimaria worried OM
  show rett neutral
  ck "No, Kreita is right. We have got the materials, so now it's time to construct our operation. That is, the planting operation, not the actual surgical operation, to be clear."

  show merona t content
  show lexan content
  show cimaria neutral
  show rett neutral OM
  rt "Okay, okay, let's go ahead with that then. We need to start planting right? I can go gather soil if you give me pots."

  show merona t content OM
  show rett content
  mk "We only have two spare pots left, but if you empty a crate or two of our food, you could fill them up. We could plant a few seeds in them too."

  show merona t content
  "I held up the cluster of packets and shook its contents."

  show merona t happy
  mk "They weren't expensive either, so we bought a fair amount. There's room for trial and error."

  return
  #-----------------------------------------------
label lbl_PathB_6_1:
  
  #play music music_Cool_Steel_Breeze #(from before)
  #(Continuation of 6.0)
  #scene cg town #(from before)
  #TODO [Positions as before
  show merona t grin
  show lexan content
  show duran t neutral
  show kreita grin
  show cimaria surprised
  show rett content OM
  rt "I'll run off now and prepare the soil then!"

  play music music_Words
  show merona t sadSmile
  show lexan neutral
  show rett content
  show cimaria serious OM
  ck "Wait, watch out! Be careful walking over..."

  #TODO [fade out Rett~
  $ renpy.transition(slow_dissolve, layer="master") 
  hide rett
  show kreita grin2
  "But before Cimaria could finish, Rett twirled around, fetching the pots before scampering off into the deeper parts of the forest."

  show merona t grin
  show lexan sadSmile
  show kreita content
  show cimaria worried OM
  ck "...Walking over there. *sigh* Nevermind."

  show merona t content OM
  show cimaria worried
  mk "Ha. Funny how Rett and Prowen were the ones who gave us intangible advice, but now they're getting the tangible things needed."

  show merona t surprised
  show lexan neutral
  show duran t annoyed OM
  show cimaria neutral
  dt "Great, now they're contributing something that's actually useful."

  show merona t disappointed
  show duran t annoyed
  mi "Way to be a ray of sunshine, Duran."

  play music music_potHappy
  show merona t content OM
  show lexan content
  show duran t neutral
  show cimaria gentle
  mk "Okay, while Rett is filling the pots, I'll ready a crate or two for him to immediately take back to the forest once he's back."

  show merona t content
  show lexan content OM
  ln "Do you need any help? There are quite a few items in those crates."

  show lexan content
  "I swatted my hand at Lexan."

  show merona t serious OM
  show duran t bored
  show kreita neutral
  mk "Nah, I can handle it. But now that you mention the number of food in them, we need to secure it somewhere else. Do we have a large bag that we can stuff it in?"

  show merona t serious
  show lexan neutral
  show kreita pouty OM
  show cimaria neutral
  kh "I'm pretty sure we don't. I've foraged around that wagon several times, and there isn't any other available storage-well, except for extra space in our personal bags."

  show kreita neutral OM
  kh "There's also the alternative of letting the food roam free in the wagon, but it'd be best to keep those prisoners locked up in a box..."

  show merona t grin
  show lexan content
  show kreita fierce OM
  show cimaria grin
  kh "...with no chance of escape."

  show merona t content OM
  show kreita neutral
  show cimaria neutral
  mk "How much food is left in each crate then? We could shift the contents around so that one is empty while the others are jam-packed."

  show merona t content
  mi "One container is enough and should be able to fit multiple plants. As long as we rearrange the goodies, we'll be good."

  show cimaria gentle OM
  ck "We have already diminished a bit of our food supply, so your suggestion sounds fine. We can all put at least some things in our personal bags as well."

  play music music_Radio_Martini
  show merona t determinedGrin
  show duran t neutral
  show kreita content OM
  $ renpy.transition(slow_dissolve, layer="master")
  show boyen content:#; at Rett's former position
    yalign 1.0
    xalign 0.0
  show cimaria gentle
  kh "Let's quickly do this before Rett comes back."

  show merona t happy
  show kreita content
  show cimaria neutral
  mk "I'll empty one crate."

  show merona t content
  show lexan content OM
  ln "I'll help you with the emptying."

  show lexan content
  show kreita content OM
  kh "I'll ready the possible candidates for extra stuffing."

  show kreita content
  show boyen content OM
  bg "I'll also organize the wagon and holders."

  show boyen content
  show cimaria neutral OM
  ck "Uh... I suppose that I'll check up on Rett and lend a hand with soil collecting. You guys seem to have covered all the bases here."

  show duran t nervous
  show cimaria neutral#; fade out
  $ renpy.transition(slow_dissolve, layer="master") 
  hide cimaria
  dt "..."

  show merona t sadSmile
  show duran t nervous OM
  show kreita grin
  dt "Just tell me if anyone needs anything."

  scene bg white with fade
  kh "Okay, let's start then!"

  "We scrambled into our positions, buzzing around the wagon like bees working in a hive. "

  #TODO [fade in CG town
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg_sky1
  show clouds at leftright
  show cg town
  show wagon#; center
  show merona t content:#; left from center#; still overlapping with the wagon
    yalign 1.0
    xalign 0.1
  
  show lexan content:#; slightly right from center but still overlapping with the wagon
    yalign 1.0
    xalign 0.9
  "I snatched a box of grains out, and Lexan began hauling out the sacks."

  mi "These are medium-sized bags... I hope that they'll fit somewhere."

  #TODO [put these sprites behind the wagon CS please:
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t neutral behind wagon:#; left from center
    yalign 1.0
    xalign 0.3
  show kreita grin behind wagon#; center
  show boyen content behind wagon:#; right from center
    yalign 1.0
    xalign 0.7
  "Kreita, Boyen, and Duran were grabbing and arranging the rest of the containers, placing them on the ground while also taking the grain sacks and shoving them in wherever they could."



  play music music_Up_Kilkenny
  show merona t grin
  show lexan grin
  show kreita fierce OM
  show duran t surprised
  show kreita happy
  kh "Hey, let's make this into a fun game. Whoever stuffs the most crates wins."

  show duran t tired
  show kreita content
  show boyen content OM
  bg "And what do you get if you win?"

  show merona t sadSmile
  show lexan determined
  show duran t annoyed
  show kreita weakWink OM
  show boyen grin CE
  kh "The... glory of knowing you did a good deed."

  show merona t content
  show lexan content CE
  show duran t flabber
  show kreita happy
  show boyen grin2
  kh "Or how about fresh food for dinner?"

  show lexan content
  show duran t flabber OM
  show kreita grin2
  dt "Actually, that's not bad. Let's make it a real thing."

  show duran t evilGrin
  show kreita happy
  show boyen content
  kh "Hooray! Then..."

  show kreita fierce OM
  kh "Start!"

  show lexan surprised
  show kreita fierce at walkBounce
  show boyen neutral at walkBounce
  #TODO [move Kreita's, Duran's and Boyen's sprites up and down/ walking animation
  show duran t neutral at walkBounce
  
  "The three seized away at the little pile of grain bags on the ground, and they dawdled over the wagon and boxes, attempting to find more places to thrust the food in. Little powder clouds bloomed when they did, making me chuckle to myself."

  play music music_Summer_Day
  show merona t sadSmile OM
  show lexan grin
  mk "Hope we don't break any of those... *laugh* And Lexan, you should start double timing on getting those sacks out before they start plucking them away."

  show merona t content
  show lexan grin CE
  "Lexan smiled with one corner of his mouth and shook his head."

  show merona t grin
  show lexan laugh
  ln "Getting attacked by those hungry hands sure is something to be scared of."

  return
  #-----------------------------------------------
label lbl_PathB_6_2:
  
  play music music_Delightful_D
  #(Continuation of 6.1)
  #scene cg town #(from before)
  #TODO [Positions as in former chapter#; K, D and B still moving up and down
  show merona t surprised
  show lexan surprised
  show kreita laugh CE
  show boyen neutral
  show duran t evilGrin
  kh "If you really aren't fast enough, we'll start taking them from you. Not kidding."

  show merona t sadSmile
  show lexan sceptical
  kh "Or I think I'm not kidding."

  show merona t content
  show lexan neutral
  "Duran surged over to the bags, cradling them up in his arms. His eyes were targeted on the laid out pile, like they were analyzing how much he could handle in one shot."

  show merona t grin
  "If you squint, it's almost like he's holding the body of a kid, except he's handling it like... well, like sacks of grain."

  show merona t surprised
  show lexan surprised
  show duran t evilGrin OM
  dt "Lexan and Merona, move faster. The stakes are too high for casual rates."

  show merona t serious
  show lexan neutral
  show duran t evilGrin
  mi "Geez, these people are practically salivating for this unidentified fresh food. Dried vegetables and boiled grains have been pretty decent though, I must say. Not the most luxurious meal we could get, but tasty for what we have."

  show merona t content
  show lexan determined at walkBounce#; move him up and down as well now
  "Lexan picked up his pace, throwing down the sacks now."

  play music music_Ecstasy_X
  show lexan determined OM
  ln "Okay, okay! I'll speed things up a bit."

  show merona t grin
  show lexan grin OM CE
  ln "But winner has to share some of this reward with me too."

  show lexan grin
  show duran t evilGrin OM
  dt "Sure, yeah..."

  show merona t content
  show lexan content
  show duran t evilGrin
  "Duran mumbled out his response. He was only concentrating on finding more places for the grains, and the spaces just kept getting filled up. Boyen, Kreita, and Duran jostled each other, digging around for more available spots, but they had already filled up all the obvious ones."

  show merona t determined at walkBounce #; start moving her up and down as well
  mi "Enter urgent mode. Some creativity will be needed now..."

  play music music_Dark_Red_Wine
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan neutral:#; stop his animation and move his sprite down by 150px
    yalign 2.5
  "I gathered an armful of sacks and unloaded them onto the pile. Lexan crouched down, sorting out the mess."

  show merona t serious OM
  mk "When we're finished, I propose that we start adding a large portion of oatmeal whenever we eat. Because I don't think there's going to be anymore places to stuff all these bags into."

  show merona t serious
  show lexan content OM
  ln "It's either that or throw some food out, and I would prefer your option over the alternative. Perhaps if we adopt an animal-or dare I say even monster-companion along the way, we could start feeding the grain to it as well."

  show merona t happy
  show lexan grin
  mk "Why limit it to one extra member? Why not start a party of animals and monster and create a traveling charity that offers welfare to the creatures who aren't getting their daily meals? It would definitely save those poor saps."

  play music music_Ill_be_right_behind_you_Josephine
  show merona t serious:#; stop her animation
    yalign 1.0
  show lexan neutral OM
  ln "Speaking of saps, are you actually prepared to cultivate the yander? Serious question."

  show lexan worried OM
  ln "Shortly after finding the seeds, it worried me if you could successfully do so since you were a bit shaky in our lessons on enhancing growth speed."

  show merona t sadSmile
  show lexan neutral OM
  ln "It's not that I don't have faith in you. You've made great progress, but I'm-"

  show merona t content
  show lexan neutral
  "I held up my hand to stop him."

  show merona t content OM
  show lexan sadSmile
  mk "No, don't worry, I don't take offense."

  show merona t worried
  mi "Well, maybe not offense, but I do feel the disappointment creeping in me. I need to work on moving that feeling out of my system."

  show merona t sadSmile OM
  mk "I know that in the work I've done with you, the most that has happened was me killing the plant, making the plant slightly stronger, or whatever else that didn't speed up the growth. Overall, not model results."

  show merona t serious OM
  show lexan neutral
  mk "I don't have complete confidence that I can make the growing process significantly better, but I've got solid hope that I can help the yander growth out in one way or another. It may not be speed-it could be stronger attributes of the plant. Maybe I'll do a minor mutation. Maybe I'll plump it up."

  play music music_piano
  show merona t content
  show lexan surprised
  "I nodded to myself and stared down into Lexan's eyes."

  show merona t content OM
  show lexan content
  mk "Whatever I do to it, I'm going to make sure that I can get something right."

  show merona t determined OM
  show lexan neutral
  mk "This isn't just a little lesson that I'm below average in. This is for something that's actually going to matter in real life, not a ridiculous hypothetical scenario, and I'm going to make myself get it right."

  show merona t content
  "I paused and smiled at him."

  play music music_romance
  show merona t content OM
  show lexan surprised
  mk "And... I should also thank you."

  show merona t content
  show lexan grin
  "Lexan furrowed his brow, but looked amused. He stopped his organizing and focused on me."

  show lexan sceptical OM
  ln "You were going on a nice roll there. What's with the sudden 'thank you'?"

  show merona t content OM
  show lexan neutral
  mk "For someone who has a water ability, you can teach plant manipulation quite well. Very well, in fact. I would say the same for Duran and fire ability, but I don't know how he feels."

  stop music #(pause music)
  show merona t content
  show duran t surprised
  "Duran twitched from hearing his name, but summarily went back to work."

  play music music_romance #(continue)
  show merona t content OM
  show lexan content
  show duran t evilGrin
  mk "I'm sure that it's not your thing to teach to students like Duran and me, but I'm really glad that you're the one who came along here."

  show merona t grin
  "I crossed my arms and grinned even wider."

  show merona t happy
  show lexan surprised
  mk "Not the best judge, but I'd say that you know how to be a good master mage."

  show merona t grin
  show lexan grin CE
  "Lexan shook his head, but I didn't miss his own smile growing a little larger at my words."

  show lexan serious OM
  ln "I'm still new at this. You haven't met true masters yet, but I'm flattered that you acknowledge me in this way. I have a lot to learn, and it's going to be a tiring road for me, but if I keep getting students like you and Duran, I'm sure that I'll love doing what I do."

  return
  #-----------------------------------------------
label lbl_PathB_6_3:
  
  play music music_Words
  #(Continuation of 6.2)
  #scene cg town #(from before)
  show wagon#, center
  #TODO [Positions as in former chapter#; K, D and B still moving up and down
  show merona t surprised
  show lexan surprised#; placed 150px lower like before
  show kreita fierce
  show boyen sweaty
  $ renpy.transition(slow_dissolve, layer="master")
  hide duran
  show duran t nervous:#; left from Merona #(in front of wagon)
    yalign 1.0
    xalign 0.0
  "Duran popped over, getting more bags."

  show duran t nervous
  show merona t shocked
  show lexan neutral
  show duran t nervous OM
  dt "Uh, I don't really want Merona lumping me into thinking the same things as her, so lemme just say that I don't feel as strongly as she does over your teaching ability."

  show duran t neutral OM
  show merona t disappointed
  dt "You're not bad, but not inspirational-speech-worthy either. Just another guy with the hat."

  show duran t neutral
  show lexan neutral CE
  "Lexan nodded as Duran cradled another bunch of sacks in his arms."

  show merona t serious
  show lexan content OM
  ln "Never thought that I would be worthy of a motivational speech from you Duran, but I do appreciate your intent."

  play music music_Dark_Red_Wine
  show duran t annoyed
  show merona t determined OM
  show lexan neutral
  mk "Duran, I think I'd give an inspirational speech because of you. Even though you laze around so much, you feel like a necessary addition to the team and bring fresh perspective, which is always gladly welcomed."

  show merona t verySad
  show lexan surprised
  "I started exaggeratedly sniffling and hunching up my shoulders, pulling off my best ugly crying face."

  show duran t angry
  show merona t verySad OM
  mk "*sniff* Aw shucks... *sniff* Look how emotional you got me!"

  show duran t annoyed OM
  show merona t determinedGrin
  show lexan neutral
  dt "I'm leaving."

  show duran t annoyed
  show merona t serious
  "Sometimes I think that Duran and I are like a mouse and cat together, but in reality, it's probably more like a mouse and another mouse."

  play music music_potHappy
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t tired behind wagon:
    yalign 1.0
    xalign 0.3
  show duran t tired at walkBounce#; left from center and behind wagon #(as before)#; start his walking animation again
  show merona t content
  show lexan grin
  "I straightened up and waved Duran off while he scampered away. Lexan gave me an amused expression. Refocusing on the grain, I could only return a quick sheepish look."

  show merona t embarrassed OM
  mk "Was that dramatic?"

  show merona t grin
  show lexan content OM CE
  ln "Nope, it was perfectly natural..."

  show merona t content OM
  show lexan content
  mk "That was a rhetorical question, but thanks for answering."

  show merona t content
  show lexan content OM
  ln "I see."

  play music music_White
  show lexan neutral
  ln "..."

  show merona t surprised
  show lexan serious OM
  ln "Can I ask you a question? A non-rhetorical one, that is."

  show merona t serious
  show lexan serious
  "I kept my visual concentration on organizing the bags, but let my ears tune in to Lexan."

  show merona t serious OM
  mk "Shoot away."

  show merona t serious
  show lexan sadSmile OM
  ln "Why... do you like my teaching?"

  show lexan sadSmile OM
  "I can feel the reluctance and confusion traced in his voice. Weird, since he's supposedly supposed to be this exceptional master mage..."

  show merona t content OM
  show lexan neutral
  mk "Well, I think your teaching is good because it... works for me? I mean, I think the thing was that I needed more specialized attention with more guidance, and my main instructor was not doing a great job at that, so I was not moving ahead in class. He was always busy with other classes..."

  show merona t sadSmile OM
  mk "I can be a little a slow in picking up things because I just don't get how they work. I need to get a feeling for something before fully understanding and carrying the task out."

  show merona t content
  show lexan neutral OM
  ln "Ah... I am a water master mage, so that has a part in it."

  show merona t content OM
  show lexan neutral
  mk "Right, right. Manipulating water does seem like it would need a secure connection to the action and element, just like handling plants and animals."

  show merona t content
  "I rolled my eyes at the grain and kept working."

  show merona t content OM
  show lexan surprised
  mk "It's a fault from both me and my plant master mage I guess. Still gotta give you credit for bumping up my skills."

  play music music_newBegin
  show merona t surprised
  show lexan neutral OM
  ln "I don't know about that, Merona. You're the one with the ability, one that's not even my forte. You should give yourself more credit."

  show merona t surprised OM
  show lexan neutral
  mk "Maybe. I'm just trying to answer your question though. Do you like your way of teaching?"

  show merona t serious
  show lexan serious OM
  ln "I... don't know. I'm not the one teaching myself, and I'm not teaching other people like me, so I wonder what it's like to be on the receiving end."

  show merona t content OM
  show lexan serious
  mk "You're like a master mage prodigy. You're not in their thirties, so that should say something right?"

  show merona t determinedGrin OM
  show lexan sadSmile
  mk "As you said: you should give yourself more credit."

  show merona t surprised
  show lexan sadSmile OM
  ln "Perhaps. But I don't feel like a good teacher for most. The only person I've felt confident in teaching was probably... Duran."

  show merona t serious#; move her sprite down by 150px
  show lexan neutral
  "I squinted at him for a second and got up, stretching my body out. All the sacks finally were out. I plunked back down onto the ground, propped my chin on my hand, and gave Lexan my full attention this time."

  play music music_She_dreams_in_blue
  show merona t serious OM
  mk "Duran... a little more explanation please?"

  show merona t serious
  mi "If I was a teacher, the only person I'd ever not feel confident teaching would be Duran."

  show merona t surprised
  show lexan neutral OM
  ln "It's already funny that he has a fire ability while I have a water ability, but his level of skill reminds me of my own less than ten years ago."

  show merona t surprised OM
  show lexan neutral
  mk "Really? What were you like?"

  show merona t serious
  show lexan serious
  "He stared at the ground, directing his attention to a crawling ant exploring the sacks."

  show lexan serious OM
  ln "It felt like I could never tire from manipulating water. Didn't matter whether I was purifying it, changing it to other forms, or summoning it. There was a strong bond, like water and I were joined together by a thick, uncuttable rope."

  show lexan serious OM CE
  ln "Me being a rather...shy teenager balanced out the force of my ability I guess. I just did well in my classes and skipped around a few levels, allowing me to graduate early and pursue this occupation."

  show merona t worried OM
  show lexan neutral
  mk "You're using past tense talking about how powerful your ability was. Is it still like that?"

  show merona t content
  show lexan neutral OM
  ln "Yes. It may look less to outsiders, but that's only because now I've learnt to truly tame water. It doesn't matter how it looks though, and I'd never go back to that time when it felt more like a tug of war between the water and I, over who was more mighty."

  ln "I only became a master mage so fast because I always was able to have that connection and feel to my ability, and Duran has that same kind of power in his fire."

  show merona t grin
  show lexan neutral
  mi "Ah yes, Duran our human torch. The school candle. So very useful for those nights that we need to travel, and no oil needed!"

  show merona t serious OM
  show lexan serious
  mk "Duran is an advanced fire student who doesn't need any effort to be good... Maybe that's why the Headmaster put you and Duran in. Start collecting and creating a scary super group of students and teachers at the academy."

  show merona t surprised
  show lexan surprised
  "Lexan slightly widened his eyes at me and sighed."

  play music music_eerie
  show lexan surprised OM
  ln "Glad to see that I'm not the only one who can think of that possibility."

  show merona t serious OM
  show lexan serious
  mk "What? Do you really think that's the reason?"

  show merona t serious
  show lexan neutral
  "He shrugged and looked at me."

  show merona t worried
  show lexan neutral OM
  ln "Wriane has been around for a long time as the head of Laneo Academy, and she makes questionable decisions with questionable outcomes from time to time..."

  show merona t sadSmile OM
  show lexan neutral
  mk "Sounds like a lot of people."

  show merona t disappointed
  show lexan determined OM
  ln "The only difference is that her decisions are on a higher, more impacting level."

  show merona t serious
  show lexan determined
  mi "True. Headmaster Wriane doesn't seem like a person with ill intentions though. What kind of person would seek trouble while sitting as a school head?"

  show merona t nervous
  show lexan serious OM
  ln "Take this journey for instance. Why was this whole thing, a large, time-consuming event made and labelled with the purpose for you?"

  show merona t nervous OM
  show lexan serious
  mk "Monsters. It looks like the purpose is for me and my studies, but it really is for the sake of ridding monsters."

  show merona t nervous
  show lexan worried OM
  ln "If it is monsters, then why was Duran dragged in? I don't think Wriane really cares for having another person for the sake of giving you companionship. Duran is a student with a strong ability, and Wriane knows it. Why take him out here and give the two of you a teacher that was me, and not another other novice mage?"

  show lexan serious
  mi "..."

  show merona t worried
  mi "I can't deny the strangeness of this all."

  play music music_Lafayette
  show merona t worried OM
  show lexan worried
  mk "You know... I have been thinking of this stuff briefly before. I do think that there are hidden agendas that none of us may be aware of and that this journey is a little strange in general, but I don't have any answers."

  show merona t sad OM
  show lexan neutral
  mk "I'm only a student. A kid, basically. No one would tell me something too important."

  show merona t sad
  show lexan serious OM
  ln "I'm not asking for answers from you. I know that in your position, you're not treated like an adult, but you're not an ignorant kid. You're capable of thinking. Heavy thinking that gets somewhere important. So don't stop holding back from getting into these matters."

  show merona t worried OM
  show lexan sadSmile
  mk "I am a heavy thinker, but I also think that you're betting just a little too much on me. I'll definitely still try to consider more about the journey as a whole, but you better be doing the same too."

  show merona t worried
  show lexan sadSmile OM
  ln "Of course. However, we're the only ones doing that either-I have a feeling that some of the others are suspicious of this entire thing."

  show merona t sadSmile OM
  show lexan sadSmile
  mk "Geez. *sigh* And I consider making plants grow faster complex."

  play music music_romance
  show merona t sadSmile
  show lexan content OM
  ln "For the record, you are now able to make them grow more. Just hope that it works on yander as well."

  scene cg MeronaLexan_EyeCover
  "I covered my eyes with my palms, but I let Lexan see my grin."

  mk "Don't stress me out. I can do it. I hope."

  scene cg MeronaLexan_EyeCover2
  "He gently peeled both of my hands away from my face and held onto them for a moment on with his own. He matched my smile, looking me in the eyes."

  ln "You got this."

  scene bg white with fade
  "Lexan let go of me, got up, but reached a hand out for me. I grunted as I pushed down on it and rose. A line of ants had marched to where we were, and I made sure not to step on them.  Crossing my arms, I gave him a once-over. "

  play music music_Summer_Day
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg_sky1
  show clouds at leftright
  show cg town
  #TODO [fade in CG town #(from before)
  #TODO [Positions as before#; K, D and B still moving up and down
  show kreita fierce:
    yalign 1.0
    xalign 0.5
  show boyen sweaty:
    yalign 1.0
    xalign 0.7
  show duran t tired:
    yalign 1.0
    xalign 0.3
  show kreita fierce at walkBounce
  show boyen sweaty at walkBounce
  show duran t tired at walkBounce
  show wagon
  show merona t content OM:#; placed 150px lower
    yalign 2.5
    xalign 0.1
  show lexan content:#; placed 150px lower like before
    yalign 2.5
    xalign 0.9
  mk "Sounds like you had an interesting student life. Did you go to Laneo Academy?"

  show merona t content
  show lexan content OM
  ln "I'm an alumnus, yes."

  show merona t content OM
  show lexan neutral
  mk "Can you tell me more about what it was like for you a few years ago then?"

  return
  #-----------------------------------------------
label lbl_PathB_6_4:
  
  #play music music_Summer_Day #(from before)
  #(from before:)[CG town #(from before)
  #TODO [Positions as before#; K, D and B still moving up and down
  show kreita fierce
  show boyen sweaty
  show duran t tired

  #(new:)
  show merona t content#; placed 150px lower
  show lexan content#; placed 150px lower
  "Lexan raised a brow and smiled with one side of his mouth."

  show lexan surprised OM
  ln "Uh... what the academics were like?"

  show merona t content OM
  show lexan surprised
  mk "I guess. But I'm more curious about your student life in general..."

  #TODO [fade in a 40% opaque white area behind Merona and Lexan
  $ renpy.transition(slow_dissolve, layer="master")
  show bg white behind merona:
    alpha 0.6
  show merona t content
  show lexan neutral OM
  ln "Well..."

  show merona t serious
  show lexan neutral
  "He stared into blank space for a moment, traveling back to a time not so far off from the current one."

  mi "I mean, if he was a student just a few years ago, the academy couldn't have been much different from how it is today, right? I'd rather hear more about his personal story..."

  show merona t embarrassed
  mi "But that may be too much to ask for."

  play music music_Sugar_On_My_Tongue
  show merona t content
  mi "He's free to answer as much as he likes though, so I'll take what I can get."

  show lexan neutral OM
  ln "First, let me give you a timeline of my student life."

  ln "I entered the academy when I was twelve or thirteen, and I was sixteen years old when I graduated... six years ago."

  show merona t surprised
  show lexan neutral
  "I squinted at him and opened my mouth only for no sound to come out for a moment."

  show merona t surprised OM
  show lexan surprised
  mk "What?"

  show lexan content
  mk "That's... that's like, six levels in three to four years. And you even started early!"

  show merona t surprised
  "I didn't know what else to say."

  show merona t serious OM
  show lexan grin
  mk "Yeah... Good job..."

  show merona t serious
  show lexan grin CE
  "He chuckled and crossed his arms."

  show merona t content
  show lexan content OM
  ln "Yes, and thank you for the 'good job'. I couldn't skip out any of the master apprenticeship years, so here I am! I intend to continue studying to get to the next stage of my field."

  show merona t determinedGrin OM
  show lexan content
  mk "Okay, I can see that. But enough of your future plans-we're taking a trip to the past right now."

  show merona t embarrassed
  mi "Was that a little too forceful? Eh, it'll all depend on how he responds."

  show merona t content
  show lexan content CE
  "He sheepishly nodded."

  play music music_recollections
  show lexan content OM
  ln "Right, let's get back on track."

  ln "When I first came to Laneo Academy, I never quite realized the extent of my ability. Sure, I was able to summon small amounts of rain and take water from living beings, but I never truly explored how far I could go."

  show merona t grin
  show lexan grin OM
  ln "A school is a great place where you can be challenged. In my first few lessons, I realized that completing the tasks was much easier for me than for my classmates."

  show merona t surprised
  show lexan content OM
  ln "This attracted the attention of other master mages. My teachers began observing me more during class and when I practiced on my own time, so they became interested in all that I could do."

  ln "Soon I began training more advanced skills, and I was allowed to move past some levels."

  return
  #-----------------------------------------------
label lbl_PathB_6_5:
  
  #play music music_recollections #(from before)
  #TODO [scene from before#; white overlay still active
  show merona t serious
  show lexan content
  mi "Okay, so he was basically a prodigy."

  play music music_Words_Fall_Apart
  show merona t surprised
  show lexan sadSmile OM
  ln "I suppose that I drifted through people when I moved up so quickly."

  show merona t serious OM
  show lexan neutral
  mk "Drifted?"

  show merona t serious
  "He nodded once more and met my eyes."

  show merona t worried
  show lexan neutral OM
  ln "I was literally passing them academically, but it also felt as if I was passing my classmates in terms of my relationships with them."

  show merona t surprised
  show lexan serious OM
  ln "There were no issues with anyone. But I didn't have any real connections outside of being acquaintances. I was drifting by them everyday, reaching out to them with a hello in the hall, but then I would ebb back to myself."

  show lexan surprised
  "Lexan raised his brows."

  show merona t serious
  show lexan neutral OM
  ln "I wasn't suffering with loneliness... but if I were to describe my entire academy experience in one word it would be 'drifting'. No great tension or major events ever occurred."

  show lexan sadSmile OM
  ln "My time there just came and went."

  show merona t serious CE
  show lexan neutral
  mi "Huh. \"Drifting\"."

  show merona t worried
  mi "I don't think the word has particularly positive or negative connotations to it. Very neutral. That kind of school life actually sounds better than the usual, stressful kind..."

  show merona t disappointed CE
  mi "...Better than mine."

  show merona t serious
  mi "Maybe it's just a characteristic of a prodigy-nothing pushes you to the limit. Nothing quite fazes you in a good or bad way."

  show merona t serious OM
  mk "If you put it that way..."

  play music music_White
  show lexan surprised
  mk "...Would you say that you liked your time at the academy?"

  return
  #-----------------------------------------------
label lbl_PathB_6_6:
  
  #play music music_White #(from before)
  #TODO [scene from before
  show merona t serious
  show lexan surprised OM
  ln "Sure. It wasn't awful nor was it fantastic, but I would still say that it was simply alright. I'm certain that's how most feel about school though."

  show merona t sadSmile OM
  show lexan content
  mk "*sigh* Definitely. Or at least, it's how I feel."

  show merona t serious
  show lexan laugh
  ln "*laugh* While you're in school, you may feel as if you can't wait to escape, but sometimes I wish I could go back in time. Enjoy what you have right now."

  show merona t worried
  show lexan content
  mi "If he considers that to be a good period of his life, I wonder how bad it must become afterwards. Him being a master mage leads him on a totally different path from mine, so he's bound to have a stressful everyday life."

  show merona t content
  "I rolled my eyes."

  show merona t content OM
  show lexan surprised
  mk "Everything must have been easy for you back when you were a student too, so now you know what it's like to be ordinary!"

  show merona t content
  show lexan content CE
  "He smiled and nodded, closing his eyes."

  show merona t grin
  show lexan content OM CE
  ln "Yeah. The feeling of being frustrated and exhausted so often is the high school experience I missed out on, but it's come to bite me."

  play music music_piano
  show lexan sadSmile OM CE
  ln "It's kind of nice to finally understand how they felt."

  show merona t laugh
  show lexan sadSmile CE
  "I scoffed, lightly whacking his shoulder."

  show merona t content OM
  show lexan grin CE
  mk "Of course, only a former prodigy can say that. I wonder how my life would be if my grades weren't terrible."

  show merona t content
  show lexan content
  "Lexan opened his eyes and raised his brows."

  show merona t surprised
  show lexan content OM
  ln "Ah, but if that were the case, you wouldn't have gone on this journey. Would you still want high grades?"

  show merona t sadSmile OM
  show lexan content
  mk "Psh, probably. Not saying I don't love this trip-aside from the whole Rett situation. Hey, even that is a learning experience! Don't get me wrong, I wouldn't wish monster bites on anyon-"

  show merona t grin
  show lexan content OM
  #TODO [Stop Kreita's animation~
  show kreita:
    yalign 1.0
  ln "-I get it, I get it, no need to justify yourself. You're just looking at the silver lining in this whole case, even if the lining is quite thin."

  play music music_romance
  show merona t content
  show lexan sadSmile OM
  show kreita lol
  ln "It's refreshing that you don't freak out over this kind of thing and can think of solutions too."

  show merona t content CE
  show lexan surprised
  show duran t sad:#, stop animation:
    yalign 1.0
  show boyen sad:#, stop animation:
    yalign 1.0
  "I swatted my hand and shook my head."

  show merona t content OM
  show lexan content
  show kreita happy
  #TODO [move Duran's sprite down by 150px
  #TODO [fade out Boyen
  $ renpy.transition(slow_dissolve, layer="master")
  show duran t sad:
    yalign 2.0
  hide boyen
  mk "I'm just doing what I feel is best. Besides, don't think that normal people my age aren't capable of being rational!"

  show merona t determinedGrin OM
  show lexan grin
  show kreita grin
  mk "We may not be at the top of class, but we know how to handle life."

  show merona t determinedGrin
  mi "I've always got my street-smarts to fall back on!"

  play music music_Aces_High
  #TODO [slowly fade out the white area behind Lexan and Merona
  $ renpy.transition(slow_dissolve, layer="master")
  hide bg
  show merona t surprised
  show lexan surprised
  $ renpy.transition(slow_dissolve, layer="master")
  hide kreita
  show kreita grin#; center
  "Without notice, Kreita ran over and popped up in front of us."

  show merona t content
  show lexan content
  show kreita happy
  kh "You two! We're getting ready to depart. Hand me the rest of the load-I'm the one who's gonna get the fresh food, mwahaha!"

  show kreita content#; fade out
  pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")
  hide kreita
  "She scooped up the sacks into her arms before the two of us could respond. All the remaining little crevices got stuffed, and Lexan and I could only watch her while Duran sulked next to the wagon."

  show merona t grin
  mi "Competitions make everything more efficient. We should start holding clean-up competitions more often so we can always be ready to go as fast as this!"

  play music music_life
  show merona t content
  "I looked up at Lexan."

  show merona t content OM:#; move her sprite back to normal y position
    yalign 1.0
  mk "Shall we go then?"

  show merona t content
  show lexan content OM:#; move his sprite back to normal y position
    yalign 1.0
  ln "Let's."

  show lexan content
  "We strolled down to the cart where everyone else was gathered. Everything seemed packed up and in place."

  $ renpy.transition(slow_dissolve, layer="master")
  show lexan content:#; move his sprite back to normal y position
    yalign 1.0
    xalign 0.7
  show cimaria neutral OM:#; right from Lexan
    yalign 1.0
    xalign 0.75
  ck "Well, we can officially leave."

  show merona t surprised
  show cimaria neutral
  $ renpy.transition(slow_dissolve, layer="master")
  show rett neutral OM:#; right from Cimaria
    yalign 1.0
    xalign 1.1
  rt "I hope we'll get to our destination quickly... We can probably make it there in another two weeks or so."

  play music music_Shes_on_my_Mind
  show lexan surprised
  show cimaria abashed at FarRightBump#; move towards Rett's sprite and back to the former position
  show rett pouty
  "Cimaria poked his upper arm."

  show merona t grin
  show lexan content
  show cimaria neutral OM
  ck "And I hope we can drain this venom out of you and fix you back up. Top priority."

  show cimaria grin
  show rett pouty OM
  rt "Hey, no intentional hurting my arm! I thought you were a professional."

  #TODO [Move Cimaria once more towards Rett's sprite and back
  show rett pouty
  "She smirked and poked the same place even harder."

  show merona t grin CE
  show lexan content CE
  show cimaria laugh
  show rett smirk
  ck "Your bites are on your forearm. I'm just testing how well this part of your arm is withstanding... Think of it like an impromptu medical examination."

  show merona t content
  show lexan content
  show cimaria content
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita content behind wagon#; center behind cart
  show rett content
  "Kreita grasped the handles of the cart, readying it to move forward."

  play music music_Radio_Martini
  show kreita happy
  kh "Let's go!"

  #TODO [fade out the spites, starting with the cart and Kreita~
  "She started up first, and we all followed behind her."
  $ renpy.transition(slow_dissolve, layer="master")
  hide kreita
  hide wagon
  pause(1.0)

  #TODO [fade in CG forest24
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest24
  show merona t content:#; left
    yalign 1.0
    xalign 0.2
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan content:#; right
    yalign 1.0
    xalign 0.8
  mi "Once again, we're back on the road. Hopefully we'll find another decent spot to rest, for the sake of Rett and for the sake of our feet."

  show merona t content OM
  mk "We had a really productive stop. I think we're on a good track now."

  show merona t content
  show lexan content OM
  ln "We'll see how it goes. Seems like we can get everything done."

  show merona t grin
  show lexan grin
  "I elbowed him."

  show merona t happy
  mk "Nothing a prodigy can't handle right?"

  show merona t grin
  show lexan grin CE
  "He chuckled and nodded."

  show lexan content OM
  ln "You don't know."

  play music music_piano
  show merona t blushSmile
  show lexan content
  mi "If I can do it, he can do it."

  show merona t blushSmile CE
  mi "Let's do this."
  scene bg black with fade

  return
  #-----------------------------------------------

label lbl_PathB_6_8:
  
  play music music_potHappy
  show cimaria neutral
  show kreita grin
  show merona t content OM
  show duran t surprised
  show rett content
  mk "Seems to be in good shape! Ever since we salted it, there haven't been any changes."
  show cimaria sadSmile
  show kreita grin2
  show merona t sadSmile OM
  show duran t neutral
  show rett grin
  mk "My bag smells extra salty, but that's better than rotting monster fish. *laugh*"
  show cimaria neutral
  show kreita content
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan content OM behind merona:
    yalign 1.0
    xalign 0.15
  show lexan content OM at walkBounce
  show merona t sadSmile
  show rett content
  ln "As long as the monster doesn't deteriorate, we'll have to tolerate any kind of smell. We can take it out of your bag occasionally though, so the bag can air out the odor."
  show kreita content OM
  show lexan content
  kh "Yeah, having it permanently smell like fish isn't going to exactly attract people..."

  play music music_Greek_Dance
  show cimaria grin
  show kreita surprised
  show lexan confused
  show merona t surprised
  show duran t annoyed
  show rett smirk
  kh "Unless they have a fish fetish. People can like anything."
  show cimaria neutral
  show kreita content
  show lexan neutral
  show merona t serious
  mi "I'm certainly not aiming to attract anyone with a fish fragrance, so taking the monster out of my bag is a fine choice."




  play music music_Cool_Steel_Breeze
  show lexan content OM
  show merona t content
  show duran t neutral
  show rett content
  ln "You could wrap the fish in cloth when it's outside, and I can wash your bag. Letting the bag air-dry will freshen it up."

  show lexan content
  show merona t content OM
  mk "I'd love that! Could I actually set it on top of the wagon crates right now?"
  show kreita content CE
  show merona t content
  "Kreita nodded and jerked her head to the cart."
  show kreita content OM
  kh "Go for it."
  show kreita content
  "I reached into my pouch containing the monster. Grabbing its tail, I covered it with one of my handkerchiefs and gingerly laid it across a crate."
  play music music_piano
  show merona t sadSmile
  mi "It's almost like I'm tucking it in bed..."
  show merona t nervous
  "...When I'm actually covering a corpse with a sheet."
  show lexan neutral
  show cimaria neutral OM
  show merona t content
  ck "Good thing that it isn't extremely hot at the moment, otherwise this monster could have been baking out here."
  play music music_Dark_Red_Wine
  $ renpy.transition(slow_dissolve, layer="master")
  show boyen serious OM behind duran:
    yalign 1.0
    xalign 0.95
  show boyen serious OM at walkBounce
  show lexan sceptical
  show cimaria serious
  show kreita sceptical
  show merona t surprised
  show duran t annoyed
  show rett grin
  bg "Hey, at least it was salted beforehand. Even if you all keep on denying it, it would have had this great, smoky flavor."
  $ renpy.transition(slow_dissolve, layer="master")
  hide boyen
  #TODO [fade out Boyen
  show lexan serious
  show cimaria neutral
  show kreita neutral
  show merona t serious
  show rett surprised
  "Lexan cleared his throat."
  show lexan neutral OM
  show duran t neutral
  show rett neutral
  ln "As appealing as eating monster meat sounds, may I ask how the other aspects of our plan are going? So far, we're doing well on growing yander and preserving the monster."
  show lexan neutral
  show cimaria neutral OM
  show kreita content
  show merona t content
  ck "Well, I've made a serum out of the powdered yander. I haven't been able to test it, but it should be the right consistency for what I need to do."
  show cimaria neutral
  show rett worried
  "Rett pursed his lips for a moment."
  stop music fadeout 1.0
  show lexan worried
  show cimaria surprised
  show kreita worried
  show merona t worried
  show duran t nervous
  show rett worried OM
  rt "If you can-could you describe what exactly you're going to do in my operation?"
  play music music_Ill_be_right_behind_you_Josephine
  show cimaria neutral
  rt "I'd like to know if there's going to be some blood involved..."
  show rett worried
  "Cimaria shrugged, crossing her arms."
  show cimaria neutral OM
  ck "Since we are dealing with venom, I need direct contact with your body fluid. The skin is a barrier in between."
  show cimaria neutral
  show rett surprised
  "Rett's eyebrows jumped up."
  show cimaria worried
  show kreita sad
  show merona t disappointed
  show duran t worried
  show rett surprised OM
  rt "So that's a yes to blood."
  show cimaria worried OM
  show rett pouty
  ck "Perhaps."
  show lexan neutral
  show cimaria neutral OM
  show kreita serious
  show merona t nervous
  show rett worried
  ck "Why? Do you have a phobia towards seeing blood or getting cut?"
  show cimaria sceptical
  show rett worried OM
  rt "N-no, but whenever an operation involves sharp objects cutting me open, it just feels a lot more serious. Or more serious than I thought."
  show cimaria neutral
  show rett confused
  "Cimaria gave him a blank stare."
  show lexan worried
  show cimaria neutral OM
  show kreita neutral
  show merona t serious
  show rett surprised
  ck "'More serious'? This isn't an annual check-up. But now you're prepared for what I'm going to do to you. It's not so major that I must sedate you, so I hope that puts you at ease. If the pain becomes unbearable, I do have anesthesia."
  show cimaria neutral
  show rett neutral
  "Rett's face relaxed a little, and his brows sank back to their normal place."
  show lexan sadSmile
  show cimaria gentle
  show kreita content
  show merona t sadSmile
  show duran t neutral
  show rett neutral OM
  rt "Yeah, that does sound better."
  rt "..."
  show lexan neutral
  show merona t serious
  show rett embarrassedGrin OM
  rt "I... get sort of nervous about surgeries, hospitals, and the like. Probably because I'm usually the one waiting for other people to be operated on."
  show cimaria content
  show rett embarrassedGrin
  "Cimaria smiled, lifting a corner of her mouth."
  show lexan sadSmile
  show cimaria content OM
  show rett neutral
  ck "It's natural to worry like that. There's no need to explain why, and since you're the patient now, you have to relax and let me work my magic."
  play music music_Shes_on_my_Mind
  show cimaria abashed
  "She tilted her head to the side and changed her crooked smile into a teasing one."
  show lexan neutral
  show cimaria abashed OM
  show kreita grin
  show merona t content
  show rett content
  ck "Besides, it's almost like you're saying you don't have faith in my healing skills. Don't you think you'll be alright in my hands?"

  show cimaria abashed
  show rett smirk
  "He nodded, returning a grin."
  show rett laugh
  rt "*laugh* Yes, of course. If it's you, I know that you aren't going to accidentally kill me."

  play music music_recollections
  show lexan grin
  show cimaria grin CE
  show kreita grin2
  show merona t grin
  show duran t annoyed OM
  show rett grin
  dt "Yeah, that doesn't sound really trusting..."
  show lexan content
  show cimaria content
  show kreita content
  show duran t neutral
  show rett content
  mi "It takes baby steps towards getting over your worries."
  show cimaria worried
  show merona t content
  "Cimaria straightened her skirt out and sighed."
  show cimaria worried OM
  show rett smirk
  ck "Anyways, now that we all know the basic plan, how about we take a moment to simply relax a little? Loosen up a bit, until we get to our next stop."
  return
  #-----------------------------------------------
label lbl_PathB_6_9:
  
  #play music music_recollections #(from before)
  #scene cg forest25 #(from before)
  #(Positions as in B6.9)
  show lexan neutral
  show cimaria serious
  show kreita neutral
  show merona t surprised
  show duran t neutral
  show rett neutral
  "She froze, backing up from her previous statement."

  show cimaria serious OM
  show duran t annoyed
  ck "Wait. Actually no, I forgot to ask-how are the enhancers being used? We did get enhancers right? Merona?"

  play music music_Pilot_Error
  show cimaria serious
  show merona t serious
  "Duran scoffed to himself."

  show lexan confused
  show cimaria surprised
  show kreita sceptical
  show merona t nervous
  show duran t annoyed OM
  show rett sceptical
  dt "You know what guys? Why does Merona always get more stuff than me? She gets the enhancers, the extra seeds, the fertilized soil, but what do I get?"

  show cimaria annoyed
  dt "Nothing."

  show duran t sad OM
  dt "I just spend my time like I usually do, burning gas with Lexan."

  show cimaria serious
  show lexan sceptical
  show merona t serious
  show duran t sad
  show rett neutral
  "Lexan raised his eyebrows, shaking his head."

  show lexan sceptical OM
  show duran t angry
  ln "Well Duran, you do not need any extras since your ability and skills are fine enough on their own. It's a good thing."

  play music music_Delightful_D
  show lexan confused
  show kreita pouty
  show merona t surprised
  show duran t angry OM
  show rett sceptical
  dt "But it's more fun if I have other stuff to use... Maybe I should start practicing controlling the form of my fire with an obstacle course."

  show cimaria sceptical
  show duran t smirk OM
  dt "Make the flames go through hoops and the like."

  show cimaria neutral
  show lexan neutral
  show kreita neutral
  show merona t serious OM
  show duran t angry
  show rett neutral
  mk "Uh, to answer Cimaria's question..."

  show cimaria gentle
  show merona t serious
  "Cimaria's face brightened when I started to speak, but Duran put his hand up in my direction."

  show cimaria annoyed
  show lexan annoyed
  show kreita sceptical
  show merona t disappointed
  show duran t angry OM
  show rett sceptical
  dt "Hold on. You get to play with things, so let me do more talking."

  show lexan neutral
  show duran t annoyed
  "A gust of wind blew in from behind, making my hair attack my cheeks. It was almost as if nature was taunting me too."

  show merona t determinedGrin
  mi "I don't think that's how it works. No wonder you don't deserve the fun stuff, Duran."

  show cimaria grin
  show lexan content
  show kreita grin
  show merona t determinedGrin OM
  show rett smirk
  mk "Don't get ahead of yourself, kid. I'm your friend, so you should treat me better than that."

  show lexan determined OM
  show merona t grin
  show duran t angry
  ln "Not to mention that she's your upperclassman."

  play music music_Pilot_Error
  show cimaria neutral
  show lexan content
  show kreita content
  show merona t serious
  "Duran kicked the ground a little harder on his next step. "

  show cimaria serious
  show lexan grin
  show merona t disappointed
  show duran t angry
  show rett neutral
  dt "Oh please, don't forget why we're all on a journey in the first place. Besides, I bet I'm at a higher level than her, so I'm the upperclassman here."
  return
  #-----------------------------------------------
  
  
  #-----------------------------------------------
  # CHAPTER 8
  #-----------------------------------------------
  
label lbl_PathB_8_4:

  play music music_piano
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan serious:#, left from Prowen
    xalign 0.2
    yalign 1.0
  $ renpy.transition(slow_dissolve, layer="master")
  hide duran
  "Lexan stepped forwards and placed my hands into his own."

  show lexan content OM
  ln "Let me help you up."

  show lexan content
  mk "Hm?"

  show lexan sadSmile
  "I could tell it was Lexan from all the blue I was seeing, but I had to pause to take in what was happening."

  show prowen neutral
  show lexan sadSmile OM
  ln "*laugh* I'm going to pull you up, okay?"

  show lexan worried OM
  ln "Just hang onto me, and you'll be fine."

  show lexan worried
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t serious:#, between Prowen and Lexan
    xalign 0.3
    yalign 1.0
  
  "Lexan lifted me all the way up. After pushing aside a few strands of hair stuck to my face, he looked into my eyes. I couldn't make out his expression, but I would like to think that he looked worried."

  show prowen serious
  "On the verge of tottering, I grabbed the closest thing near me-Prowen's cape."
  return
  #-----------------------------------------------
  
label lbl_PathB_8_8_1:
  
  stop music fadeout 1.0
  show merona t serious
  "Near the bottom however was a lone glass jar buried among the bags. I pulled it out and stopped breathing."

  play music music_Ill_be_right_behind_you_Josephine
  show merona t sadSmile
  mi "Now, this is the most beautiful thing I have ever seen."

  "Limp yander leaves lay in the jar as if they were calmly waiting to be discovered."

  show merona t serious
  mi "When did she take some of the yander? Judging from its poor state, she must have kept it in this jar for a few days already."
  return
  #-----------------------------------------------
label lbl_PathB_8_8_2:
  #TODO [black screen from before continues
  mi "Would injecting the yander serum into the leaves help? Would the serum have any traces of a life flow in it?"

  mk "*sigh*"

  mi "Now, I'm just making things up."

  mi "I don't want to give up, but..."
  return
  #-----------------------------------------------
label lbl_PathB_8_9:
  #TODO [black screen from before continues
  mi "Would injecting the yander serum into the leaves help? Would the serum have any traces of a life flow in it?"

  mk "*sigh*"

  mi "Now, I'm just making things up."

  mi "I don't want to give up, but..."
  return
  #-----------------------------------------------

  
label lbl_PathB_9_3:
  #TODO [FINAL
  play music music_meronatheme
  scene cg forest32
  #TODO [character sprite positions as in A9.3
  show merona t determined OM
  show lexan grin:
    yalign 1.0
    xalign 0.9
  mk "I want to give it another shot! I'm so close to getting it..."

  show merona t determined
  show lexan laugh
  ln "*laugh* Alright, if you're still so determined, then go ahead. Don't burn yourself out though-you'd do more harm than good."

  show merona t determinedGrin OM
  show lexan grin
  mk "I know, I know. But it's not like it's going to be easy to burn out. I'd feel more frustrated over not knowing what to do than anything else."

  show merona t determined
  show lexan content OM
  ln "Let's analyze what we have done so far and what we should do next. That's a more efficient way of using our time."

  show merona t serious
  show lexan neutral OM
  ln "Immediate danger seems to trigger an unknown mechanism in your ability. Monsters have disappeared or have seemingly been replaced right before your eyes."

  show merona t worried
  show lexan worried OM
  ln "I can't imagine that you're actually making the monsters vanish. Energy is only transferable, after all..."

  show merona t disappointed OM
  show lexan worried
  mk "*sigh* Only thing we don't know is where it's being transferred to."

  show merona t reflective
  "I stared off into space."

  play music music_recollections
  show merona t worried OM
  show lexan confused
  mk "Lexan... Have you ever dealt with something like this? Do you know how to accomplish something that you're struggling with?"

  show merona t worried
  show lexan serious
  "He paused, pursing his lips for a second."

  show merona t serious
  show lexan serious OM
  ln "There's not a definite solution to that question."

  show merona t surprised
  show lexan sadSmile OM
  ln "Then again, I may not be the best person to give you an answer."

  show merona t surprised OM
  show lexan sadSmile
  mk "How so?"

  show merona t serious
  show lexan neutral
  "He scratched the back of his head and looked down at the ground."

  show lexan neutral OM
  ln "Well..."

  show lexan content OM
  ln "You know that I was able to become a master mage early, right?"

  show merona t surprised
  show lexan sadSmile OM
  ln "I don't know what it means to struggle with my ability or my studies. I was always able to easily catch on to everything, so..."

  show merona t disappointed OM
  show lexan sadSmile
  mk "Lucky..."

  show merona t disappointed
  mi "I guess a few people are born that way. Can I borrow a bit of that luck, Lexan? I'll return it by the time I graduate."

  show merona t surprised
  show lexan strict OM
  ln "It's not always a great thing. Because things have always come so easy, I've never had to work very hard, and I don't know if I'm capable of doing so if needed in the future."

  show merona t surprised OM
  show lexan neutral
  mk "If you've made it to mastery, then I doubt that there's much more that can challenge you."

  show merona t serious
  show lexan sadSmile OM
  ln "But in general, there must be other aspects of life besides education where you must put in great amounts of effort."

  show merona t worried
  show lexan worried OM
  ln "I... I'm worried that when I'm faced with a totally unfamiliar dilemma that I won't know what to do."

  show merona t surprised OM
  show lexan surprised
  mk "But what about this journey? We've faced a lot of new situations, and you seem to handle them just fine."

  show merona t serious
  show lexan surprised OM
  ln "Perhaps it looks that way on the outside... But in reality, I hate the uncertainty that this journey brings to me."

  show lexan worried OM
  ln "Even if I've proven to myself a few times that I can handle these spontaneous occurrences, I absolutely detest this uncertainty I feel."

  play music music_Cool_Steel_Breeze
  show merona t content
  show lexan neutral
  "I smiled at him."

  show merona t happy
  show lexan surprised
  mk "So you are struggling with something after all."

  show merona t content
  show lexan content
  "He smiled back at me."

  show merona t grin
  show lexan content OM
  ln "Now we're more similar than I thought."

  show merona t content OM
  show lexan neutral
  mk "Can I give you some advice?"

  show merona t happy OM
  mk "Uncertainty is probably never going to disappear... You'll always feel threatened by an uncontrollable force that is capable of hurting you."

  show merona t content OM
  show lexan sadSmile
  mk "But then you realize that even if you are hurt, you're still alive. You're still breathing and capable of coming out stronger, so it becomes easier to overcome the uncertainties."

  show merona t content OM CE
  show lexan grin
  mk "I'm scared of failing too, but I know it's not the end if I do."

  show merona t grin
  show lexan grin OM
  ln "You make some good points, Merona."

  show merona t content
  show lexan content
  "I shrugged."

  show merona t content OM
  mk "I know my advice is kind of expected already, but it's good to reiterate these things."

  show merona t content
  show lexan content OM
  ln "Let's try to become braver together and overcome our challenges then."

  show merona t happy OM
  show lexan content
  mk "Of course."

  show merona t laugh
  show lexan grin
  mk "*laugh* I feel like a teacher now. A really under-qualified teacher who preaches more than what she knows."

  show merona t content
  show lexan content OM
  ln "You know, everyone is both a teacher and a student. We're always learning and can share what we already know."

  show merona t surprised
  show lexan grin OM
  ln "I've learned a lot from working with you already, and I'm very grateful for that."

  show merona t surprised OM
  show lexan neutral
  mk "Really? What have you learned?"

  show merona t surprised
  show lexan content
  "He paused for a moment, a smile growing on his face."

  play music music_newBegin
  show merona t surprised
  show lexan grin OM
  ln "Mainly... the power of positivity."

  show merona t blushSmile
  show lexan content OM
  ln "You have radiant energy, Merona, that draws people into you and makes them feel welcome."

  show lexan neutral OM
  ln "Some people may find your cheeriness a bit too much for them..."

  show merona t sadSmile
  show lexan neutral
  mi "Like a certain boy traveling with us..."

  play music music_Summer_Day
  show merona t embarrassedSmile
  show lexan determined OM
  ln "But I think it's what makes you so perseverant and determined to accomplish your goals."

  show merona t embarrassed OM
  show lexan determined
  mk "I guess... I do try to look on the bright side, but is it really as great as you're making it out to be?"

  show merona t serious
  show lexan content
  "He shrugged."

  show merona t confused
  show lexan content OM
  ln "Maybe it's just me."

  show merona t surprisedBlush
  show lexan sadSmile OM
  ln "But even if it is... Know that I really like that about you. And I hope you can see your own virtue yourself."

  show merona t blushSmile
  show lexan sadSmile
  "I felt a growing warmth pulsing within my chest and couldn't help but let a smile take over my lips. Only now did I feel a part of my heart take sprout."

  show merona t embarrassedSmile
  mi "Strange how the littlest of things can make you feel."

  show merona t embarrassedSmile OM
  show lexan grin
  mk "Alright, enough with the flattery. We should get back to work."

  show merona t grin
  show lexan content OM
  ln "Whatever you say. Some new ideas popped up in the back of my head, actually, so let's talk about the first monster you encountered again."
  return
  #-----------------------------------------------


label lbl_PathB_9_6:

  show merona t grin
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan content:#; left from Merona
    yalign 1.0
    xalign 0.07
  show lexan at walkBounce
  "As I glanced at Lexan, he met my gaze and gave a tiny wave."

  show merona t happy
  show lexan surprised
  mk "You must be happy being so close to water."

  show merona t content
  show lexan laugh
  ln "*laugh* It's not like water controls my mood. But regardless of my ability, I do love the ocean."

  show lexan content OM
  ln "I grew up right by the sea, so my childhood was filled with long, relaxing days at the beach."

  show merona t content OM
  show lexan content
  mk "When was the last time you went home?"

  show merona t surprised
  show lexan content OM
  ln "The year I graduated from secondary school. I'll probably return next year-originally, I planned on going back this year, but I decided not to after agreeing to be a part of this trip."

  show merona t sadSmile OM
  show lexan neutral
  mk "Sorry."

  show merona t sadSmile
  show lexan happy OM
  ln "No need to apologize, Merona. Besides, Laneo is my second home. And you know how the saying goes-home is about the people, not the place. Everyone here makes me feel like it's 'home'."

  show merona t reflective
  show lexan grin
  mi "Huh. I never really thought of it like that, but he makes a good point."

  show merona t serious OM
  show lexan neutral
  mk "Well, when we do arrive back at Laneo... What's going to happen next?"

  show merona t nervous
  show lexan neutral OM
  ln "I suppose we'll carry on as we used to. We won't see each other as often unfortunately, but that shouldn't prevent us from meeting up if we wanted."

  play music music_piano
  show merona t worried OM
  show lexan sadSmile
  mk "You won't teach me anymore, right?"

  show merona t disappointed
  "He shook his head, staring ahead."

  show lexan sadSmile OM
  ln "No... There's no need for me to help you when there's other master mages more suited to guide you in your studies. But if you ever delve into irrigation-related matters, plant manipulation and water manipulation types work much closer together."

  show merona t sadSmile OM
  show lexan sadSmile
  mk "Yeah... I'm kind of sad though."

  show merona t nervous OM
  show lexan content
  mk "Is it okay if I still see you if I need something? Like if I want to talk to someone?"

  show merona t sadSmile
  show lexan content OM
  ln "Of course. I may not be your tutor anymore by then, but you can always talk to me about anything."

  play music music_romance
  show merona t embarrassed OM
  show lexan neutral
  mk "Anything?"

  show merona t blushSmile
  show lexan wink OM
  ln "I can't promise that I'll be of much help to anything you ask for, but I'll try my best! We're friends, after all."

  show merona t embarrassed OM
  show lexan content
  mk "Yeah... friends."

  show merona t embarrassed CE
  mi "What kind of relationship will we really have afterwards? "

  show merona t worried
  $ renpy.transition(slow_dissolve, layer="master")
  hide lexan
  "What kind do I really want?"

  return
  #-----------------------------------------------