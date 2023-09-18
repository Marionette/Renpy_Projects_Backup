label lbl_chapter4:
  #"A4.0"
  #TODO [FINAL













  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. The path's storyline is in blue."
  #"-----------------------------------------------------------"

  #(Continuation of 3.9)

  #play music music_Travel_Light #(from before)
  scene cg hillSide
  # [CS positions as in 3.9 please!
  show merona t surprised
  show prowen neutral:
    yalign 1.0
    xalign 0.80
  show hill #- keep in front of Merona and Prowen please
  # [the following CSs in front of CS hill please
  show cimaria neutral:
    yalign 1.0
    xalign 0.25
  show kreita happy:
    yalign 1.0
    xalign 0.35
  show lexan content:
    yalign 1.0
    xalign 0.1
  show boyen neutral:
    yalign 1.0
    xalign -0.5
  show duran t neutral:
    yalign 1.0
    xalign 0.9
  kh "Well would you look at that! I think he actually might have caught something..."

  show merona t nervous OM
  show kreita grin
  mk "He's still not getting up, but then again, that could be a sign that he doesn't want what's under his body to escape."

  show merona t nervous
  show kreita neutral OM
  kh "True, true. I think he's twitching a little right now though."

  show kreita neutral
  mi "Yep."

  show merona t worried
  mi "His twitching movements are becoming larger. Perhaps he's trying to get up?"

  scene cg riverSide
  #TODO [CG: Falling Leave loop from the intro as before
  show leaf1 at leafspin
  show leaf2 at leafspin2
  show leaf1_small at leafspin3
  show leaf2_small at leafspin4
  "Rett indeed was attempting to start pushing himself up. He scooched his knees up to slide his body over to the tree near him, but he still kept his upper body down with his arms crossed."

  mi "I wonder if the ground is rough or on the smooth side. Rett is sliding around, but there only looks to be soil and rocks down there... mainly rocks near the water. But hey, if this was a technique to try and help tire out the animal by dragging it on rough ground, I've got to give him some credit for thinking like that."

  "As Rett reached the tree's base, he dragged his knees up more to support his body. He rose up and leaned against its trunk."

  rt "Oi!"

  play music music_River_Meditation
  scene cg hillSide
  # [CS positions as in 3.9 please!
  show merona t worried
  show prowen sceptical:
    yalign 1.0
    xalign 0.80
  show hill #- keep in front of Merona and Prowen please
  # [the following CSs in front of CS hill please
  show cimaria worried:
    yalign 2.0
    xalign 0.25#; position as before but also move down by 100 pixels please #(as she steps down the hill)
  show kreita neutral behind cimaria:
    yalign 1.0
    xalign 0.35
  show lexan serious behind cimaria:
    yalign 1.0
    xalign 0.1
  show boyen worried behind cimaria:
    yalign 1.0
    xalign -0.5
  show duran t worried behind cimaria:
    yalign 1.0
    xalign 0.9
  "He kept face on the tree's body. Cimaria skipped over and grabbed a branch of the tree near where Kreita and I were, steadying herself with it while leaning in Rett's direction."

  show cimaria worried OM
  ck "Rett, are you alright? Are you hurt? Do you need something?"

  show cimaria surprised
  rt "Uh... I don't know?"

  show cimaria annoyed OM
  show lexan strict
  ck "Great answer."

  show cimaria annoyed
  show kreita surprised
  show merona t surprised
  show boyen neutral
  show duran t annoyed
  show prowen forcedSmile
  "Kreita and I shot a look at each other."

  show kreita neutral
  mi "Cimaria being sarcastic? That's a first."

  show merona t serious
  show kreita grin
  "Kreita grinned."

  play music music_She_dreams_in_blue
  show cimaria surprised
  show kreita happy
  show merona t sadSmile
  kh "What happened to you, Cimaria? I didn't know you had it in you. Wow, today has been full of surprises! I find out that Merona was practically a savage in the past and Cimaria is a sassy beast."

  show cimaria content
  show kreita grin
  show merona t content
  show lexan serious
  "Cimaria chuckled and rolled her eyes."

  show cimaria neutral OM
  show kreita neutral
  show merona t nervous
  show prowen sceptical
  show lexan worried
  show boyen worried
  show duran t worried
  ck "Never mind that. I think your cousin may need some help from you. He has been whining for you for some time now."

  show cimaria neutral
  show kreita worried OM
  kh "What? Wait, nobody say anything."

  show kreita worried
  #(Rett repeatedly calling "Kreita" at a low volume plays through the ellipses)
  
  play sound sound_rettCallingKreitaQuietly loop
  show cimaria worried
  mk "..."

  show merona t shocked
  mk "..."

  show cimaria serious
  show kreita aggressive
  ck "..."
  
  stop sound
  show kreita aggressive OM
  kh "Okay Rett, I'm coming!"

  show kreita aggressive#; fade out please~
  $ renpy.transition(slow_dissolve, layer="master")
  hide kreita
  "Kreita hobbled down the hill and jumped to Rett. She started chatting with him, but he kept his face pressed against the trunk."

  #TODO [fade to CG hillSide2, only show Merona's and Cimaria's sprites at the new positions
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg hillSide2
  #TODO [fade in CS cimaria neutral#; center
  show cimaria neutral
  #TODO [fade in CS merona t shocked OM#; right from Cimaria
  show merona t shocked OM:
    yalign 1.0
    xalign 0.75
  mk "Oh yeah. He is definitely injured."

  show cimaria serious
  show merona t shocked
  "Cimaria spun around and faced me, turning her back to Kreita and Rett."

  show cimaria serious OM
  show merona t sadSmile
  ck "I do not think that him worming through the ground helped either."

  show cimaria neutral
  show merona t sadSmile OM
  mk "Kreita was sort of right. You do have some sass."

  play music music_Ill_be_right_behind_you_Josephine
  show cimaria neutral OM
  show merona t serious
  ck "Sass? I suppose you could say that. But what matters now isn't my assumed 'sass'. I think I might need to do some healing on Rett."


  show cimaria serious
  "I looked over to where Kreita and Rett were. I couldn't see too clearly, but Rett had started coming up the hill and his arms clutched to his chest were looking a little..."

  show merona t scared
  mi "That's blood on his arms isn't it?"

  show merona t veryScared
  mk "Oh my..."

  play music music_eerie
  show cimaria serious OM
  ck "Was that an animal that caused it? Is he still holding an animal?"

  show cimaria serious
  show merona t scared
  mk "I can't tell from here..."

  show merona t worried
  mk "..."

  show cimaria surprised
  show merona t worried OM
  mk "I wonder why we didn't think too much about him getting hurt. I know we weren't expecting much, but we were taking this too lightly almost."

  show cimaria serious OM
  show merona t worried
  ck "Merona, we cannot change what has happened. There is no use to ponder what we could have done. All that we can do now is deal with the situation here before us. Please do not worry so much about it."

  show cimaria serious
  show merona t sadSmile OM
  mk "I know. I can't do anything about it. I guess I can't help but try and think of... what I could have done. But I really shouldn't think of it so much anymore, like you said. "

  show cimaria neutral
  show merona t serious
  mk "..."

  show merona t serious OM
  mk "So how long will it take for you to heal his wounds?"

  show cimaria neutral OM
  show merona t serious
  ck "How long? Well, that may partially depend on how much the patient wants for it to heal."

  show cimaria neutral
  show merona t nervous OM
  mk "But can't you heal it completely? Wouldn't it be easier for the patient to have it healed all the way?"

  show cimaria serious OM
  show merona t nervous
  ck "You would be surprised how much energy it can take for a healer to fully heal moderate to large injuries. Sometimes if I need to or expect to assist more than one person I must reserve some energy, but if there's only one person I may use more than usual."

  show cimaria serious
  show merona t serious OM
  mk "I'm going to bet that we'll have to stay here for a little because of Rett, so since he's the only hurt one and the rest of us most likely won't get hurt, would you use all your energy?"

  play music music_White
  show cimaria surprised
  show merona t serious
  rt "Well, I don't think that you'll have to use all your energy. It's not as bad as you guys think."

  play sound sound_bump
  show cimaria serious CE
  show merona t surprised
  "Cimaria slightly turned around, and her head was knocked by Rett's forehead."

  #(Continued in 4.1)
  #"A4.1"
  #TODO [FINAL












  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. The path's storyline is in blue."
  #"-----------------------------------------------------------"

  #(Continuation of 4.0)

  #play music music_White #(from before)
  #scene cg hillSide2 #(as before)
  show cimaria surprised#; center
  show merona t grin#; right from Cimaria
  #(from here on please use rett body injured)
  #TODO [fade in CS rett smirk#; left from Cimaria
  $ renpy.transition(slow_dissolve, layer="master")
  show rett injured2 smirk:
    yalign 1.0
    xalign 0.25
  ck "Oh. Hello."

  show cimaria neutral
  show merona t serious
  show rett injured2 neutral
  "She moved back and took a sweeping glance up and down at Rett."

  show cimaria neutral OM
  ck "Most notably, your arms are injured. You are slightly slouched over and from listening to you come up, you were shuffling. Describe to me your overall pain."

  show cimaria neutral
  show rett injured2 neutral OM
  rt "Um... well the only thing that actually hurts are my arms. It's got, uh, bite marks."

  show rett injured2 neutral
  show merona t worried
  "I tilted my head to get a better look at Rett's arms."

  show merona t worried OM
  mk "What happened? Do you still have it?"

  show rett injured2 worried OM
  show merona t worried
  rt "I think I still do... I'm starting to not feel anything in that area though. I'll try moving them."

  play music music_Shes_on_my_Mind
  show rett injured2 worried
  show merona t scared
  show cimaria serious:#; move closer to Rett's sprite please #(so that they slightly overlap)
    yalign 1.0
    xalign 0.45
  "Cimaria frowned and put her hand down on his arms, stopping him."

  show merona t worried
  show cimaria serious OM
  ck "Before you try moving it, sit down and let me treat you at least for a bit of time. You need to take it slow before you do anything too rash."

  #(Continued in 4.2)
  #"A4.2"
  #TODO [FINAL







  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. The path's storyline is in blue."
  #"-----------------------------------------------------------"
  #(Continuation of 4.1)
  #play music music_Shes_on_my_Mind #(from before)
  #scene cg hillSide2 #(as before)
  show merona t worried#; right from Cimaria as in 4.1
  show cimaria serious#; center but moved closer to Rett's sprite as before in 4.1
  show rett injured2 content OM#; left from Cimaria as in 4.1
  rt "Fine, fine, fine. But they're only bites, and they'll heal on their own."
  show cimaria serious OM
  ck "*sigh* You never know if it will be more than mere bites."
  scene cg RettAtTree#; Rett's face always needs to be the lowest layer #(Cimaria later kneels right before him)#; he also has the eyes separated from the rest of the face, so they can be animated
  show cg_composite RettAtTree_full1 behind cg # Show here to enable gallery
  show cg_composite RettAtTree_full2 behind cg # Show here to enable gallery
  show cg_composite RettAtTree_full3 behind cg # Show here to enable gallery
  hide cg_composite
  
  show RettAtTree face1
  show KreitaAtTree pose1
  show CimariaAtTree pose1
  "He shrugged and plopped over to sit against the closest tree. "
  show RettAtTree face2
  rt "Then now we'll know!"

  play music music_Swimming_To_Cambodia
  show RettAtTree face1
  "The others had stopped what they were doing, glancing over at what was going on. They looked at each other, not moving."

  dt "Do... do you guys need some help or anything?"

  show RettAtTree face3
  kh "Rett, are you actually alright? I mean, this could be serious. You don't know what kind of venom or whatever is in the animal you picked up."

  ln "She's right. You might not feel anything now, but there is the possibility of you having a major injury."

  show RettAtTree face1
  show CimariaAtTree pose2
  "Everyone started to approach where Kreita, Cimaria, Rett, and I were, but Cimaria held up a hand gesturing them to stop."

  ck "It is best if you all go back to what you were doing. Making him nervous or uncomfortable will only result negatively, so for now, let me do what I can."

  show CimariaAtTree pose1
  dt "Meh. You guys were kind of overreacting. Come on, it's not like we can do anything, so we don't have to worry about it. Ugh, I'm so tired. Nobody bother me; I'm taking a rest."

  "Duran went ahead to go to the closest patch of grass he could find and flopped down, sighing. Kreita snorted and patted Rett's shoulder."

  show KreitaAtTree pose2
  kh "I'm going to help them out then. I'll trust you guys to find out what's going on. Bye!"

  #TODO [fade out Kreita's sprite
  $ renpy.transition(slow_dissolve, layer="master")
  hide KreitaAtTree
  "Kreita trotted off, and I bit my lip."

  mk "I can't really do much for you Cimaria, so... I guess I'll go and join the others too."

  play music music_recollections
  show RettAtTree face2
  rt "Well actually, I think having you here would be fine. You can hold the animal's corpse if that's okay with you. I'd rather not leave it on the ground."
  show RettAtTree face1
  mk "Oh... so you're still holding whatever you were holding then? Then, I guess..."
  mi "Do I want to take a possibly dead animal?"
  mi "..."
  mi "Eh, why not?"
  "I reached out for the animal and waited."
  show RettAtTree face2
  rt "Um... can someone help me release my arms?"
  show RettAtTree face1
  mk "Weren't you somewhat moving your arms before you sat down?"
  show CimariaAtTree pose2
  ck "You were holding your arms in so tightly before, so I assume that it is difficult to change their position now."

  show RettAtTree face2
  rt "Exactly."
  show RettAtTree face1
  show CimariaAtTree pose1
  play music music_romance #>=3"
  ck "*sigh* Alright. I will help you."
  show RettAtTree face4
  "Rett smirked."
  show RettAtTree face5
  rt "Aren't you supposed to be more patient? And here I thought you were a calm and kind person."
  show RettAtTree face4
  ck "And aren't you supposed to be more grateful? Here I thought that you would appreciate someone helping you even after I witnessed you doing so many foolish things before."
  mk "..."
  show RettAtTree face1
  show CimariaAtTree pose3
  "Cimaria started pulling out Rett's arms little by little, until there was barely enough space between his chest and arms for me to see what he was holding. I leaned forward to get a closer peek."
  play music music_eerie
  mk "It's... what?"
  mi "I can't recognize this animal-or at the least, I can't recognize it immediately. It's strange... I've never quite seen something like it before, and it's almost abnormally small. Perhaps a hybrid of some kind?"
  mi "Is it truly dead though? I can't be too hasty with it in case it actually isn't. It's not moving, I don't see it breathing, and its eyes are open and unblinking. But what if that's some kind of defense tactic or something else?"
  show RettAtTree face3
  ck "Rett, what exactly did you catch?"
  show RettAtTree face2
  rt "I don't even know myself! I just saw it and went for it."
  show RettAtTree face1
  mk "You know... there is the slight-no, big-possibility that this is..."
  "Cimaria widened her eyes and stared at the creature."
  ck "You are suggesting that it's..."
  mk "Yeah..."
  show RettAtTree face2
  rt "What? Are you suggesting that this is..."
  rt "...a monster?"
  "I didn't say anything."
  show RettAtTree face1
  mi "Even if it's small and hasn't been like any other monster we've seen, I have a feeling that this too is one of them. Not all monsters, like any other living thing I suppose, will be very similar. I wouldn't be surprised to find small or weaker monsters lurking around."
  "I gulped down some air before speaking."
  mk "Well, what kind of animal would it be otherwise? None of us know what it is, and I don't think that this is exactly a common forest animal."

  show RettAtTree face2
  rt "You..."
  show RettAtTree face1
  mk "..."
  show RettAtTree face2
  rt "...You're probably right."
  show RettAtTree face1
  ck "Even if it is a monster... it's a dead monster now."
  stop music fadeout 1.0
  mk "If we called the others over to observe it, I am sure it would help us come to a definite answer."
  play music music_Lafayette
  "I nodded and inhaled. I scanned around to see everyone working on their individual duties as they said."

  mi "Well, except for Duran. But he's going to have to get up nonetheless."
  #(raised voice)
  mk "Can everyone come over here for something?"
  ck "While they are coming over, I will take care of your arm, Rett."
  #(Continued in next script)
  #" A4.3"
  #TODO [FINAL







  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. Path A's choice is in red, Path B's choice is in blue, and Path C's storyline is in pink."
  #"-----------------------------------------------------------"
  #(Continuation of 4.2)
  #play music music_Lafayette#; continuation from before
  show cg RettAtTree
  show RettAtTree face1
  show CimariaAtTree pose3
  "I leaned over and extended my arms for the creature, not taking it yet."

  mi "Where should I grab it? It's in a bit of an awkward position, and I don't want to just strangle it or something in case it's not fully dead."

  "I scrutinized for a few more seconds."

  mi "I guess it'll be best if I try and cup its back and head into my arms. Any other position wouldn't be better for me nor the creature..."

  stop music fadeout 1.0
  scene cg fishMonster:#; at 50% image size #(will be double the normal size)
    zoom 1.0
    xalign 0.5
    yalign 0.5
  "I scooped up the little possible monster and cradled it in the nook of my elbow."

  #(awkward laugh)
  "Ha ha... "

  play music music_piano
  mi "It's like... a baby."

  "Everyone gathered around us and huddled in, some looking at Rett and some looking at what was in my arms."

  kh "What happened? Did you guys actually find something traumatizing?"

  mk "Heh, sort of."

  mk "So... right now, Cimaria is still dealing with Rett's arms as you can see. We don't know if Rett is necessarily okay yet, but hopefully he is. It'll probably be fine though. That's not our main issue at hand. Why I called you guys over was because we wanted your opinion on this."

  #TODO [slowly zoom closer to the monster #(to 100%)
  show cg fishMonster at ZoomOut
  "I jerked my head down to the unknown being."

  mk "What do you think this is?"

  bg "By that, do you mean what kind of animal it is?"

  mk "Yes. When Cimaria, Rett, and I observed it more carefully, we couldn't exactly tell what it was."

  ln "It definitely doesn't look like a common forest animal. However... I feel like I might have seen it before."

  bg "I don't really know what it is either. It even seems almost unnatural."

  kh "I don't think I've ever encountered something like that before. I've seen a lot of things, but this isn't one of them..."

  pm "I can't say that I've ever seen this before either."

  mk "Yeah. The three of us didn't know what it was too."

  stop music fadeout 1.0
  mk "I'm speculating that it's..."

  scene cg hillSide2
  show prowen appalled OM
  play music music_Under_the_Stairs
  pm "...a monster?"

  show prowen appalled
  "Everyone fixated their eyes on Prowen, and my mouth slightly opened."

  mk "Yes... a monster."

  #TODO [fade back to the zoomed in CG fishMonster
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg fishMonster:
    zoom 1.0
    xalign 0.5
    yalign 0.5
  "I looked away, back down at what was in my arms."

  mk "I know that it seems strange for a monster to look like this and to be coincidentally found by Rett, but what other reasoning is there? We're not in a totally unknown area and we have people who know of what's to be expected to be found. This isn't exactly your everyday forest animal."

  "I let out some of the air I was holding in."

  mk "..."

  #TODO [fade to...
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg hillSide2
  show prowen sceptical OM
  pm "I have to agree. It's the most likely outcome."

  show prowen sceptical
  #TODO [fade in CS lexan sceptical OM#; right from Prowen
  $ renpy.transition(slow_dissolve, layer="master")
  show lexan sceptical OM:
    yalign 1.0
    xalign 0.8
  ln "Prowen, have you seen monsters like that before?"

  show prowen forcedSmile
  show lexan worried
  pm "..."

  show prowen neutral OM
  show lexan confused
  mk "No."

  play music music_Swimming_To_Cambodia
  show prowen neutral
  show lexan neutral
  #TODO [fade in CS kreita sceptical#; left from Prowen
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita sceptical:
    yalign 1.0
    xalign 0.18
  "Kreita clicked her tongue."

  show prowen surprised
  show lexan neutral
  show kreita sceptical OM
  kh "You know if it's actually a monster, this could be kind of useful for us."

  show prowen sceptical
  show lexan sceptical OM
  show kreita neutral
  ln "Useful how?"

  play music music_newBegin
  show lexan surprised
  show kreita neutral OM
  kh "It may be dead, but come on, a dead monster is better than no monster at all. We could use it to help us find out more about what exactly a monster is."

  show lexan determined
  show kreita content
  #TODO [fade in CS merona t surprised OM#; left from Kreita
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t surprised OM:
    yalign 1.0
    xalign -0.08
  mk "You're..."

  show prowen neutral
  show kreita grin2
  show merona t happy
  "You're right... this could actually help in our reports too."

  show lexan determined OM
  show merona t content
  ln "We could even use this to help Merona determine if what happened at her attack was directly correlated with monsters!"

  show lexan determined
  show kreita grin
  "Kreita grinned and crossed her arms."

  show prowen forcedSmile
  show kreita fierce OM
  show merona t sadSmile
  #TODO [fade in CS boyen tired#; right from Lexan
  $ renpy.transition(slow_dissolve, layer="master")
  show boyen tired:
    yalign 1.0
    xalign 0.97
  kh "I have to say, this was way better than getting fresh meat."

  show lexan sadSmile
  show kreita grin2 S
  show boyen tired OM
  bg "Ugh, I hope you're not saying that I should cook monster meat for all of you to eat."

  show prowen neutral
  show lexan neutral
  show merona t surprised
  show boyen neutral
  "Rett stretched his head up from where he was to look at us."

  show lexan content
  show kreita grin2
  show merona t sadSmile
  show boyen grin
  rt "NO! Please."

  play music music_SoT
  show lexan neutral
  show kreita neutral
  show merona t serious OM
  show boyen content
  mk "How long are we going to keep it then? Before it decomposes and all that."

  show kreita neutral OM
  show merona t serious
  kh "A decomposing monster is not better than no monster at all."

  show prowen sceptical
  show kreita neutral
  rt "Kreita, you know how long you can keep dead animals. It should probably apply to monsters too."

  show lexan surprised
  show kreita neutral OM
  show boyen neutral
  kh "How about if we try and preserve it somehow? Maybe we can take it into a nearby town and talk to a preservationist if there is one? Maybe even a butcher if it comes to that?"

  play music music_eerie
  show lexan strict OM
  show kreita worried
  show merona t worried
  show boyen sceptical
  ln "The issue is that this is most likely a monster; I don't know how others will react to that."

  show prowen neutral
  show lexan surprised
  show kreita grin
  rt "We don't have to tell them that it's a monster?"

  show lexan worried
  show merona t worried OM
  show boyen neutral
  mk "They still wouldn't know what it is though. We would have to make up some elaborate lie over what kind of animal this would be or something like that."

  show lexan determined
  show kreita happy
  show merona t worried
  kh "That seems doable."

  show prowen neutral OM
  show kreita grin
  show merona t surprised
  pm "It could work."

  show prowen neutral
  pm "..."

  show prowen neutral OM
  show lexan neutral
  show kreita neutral
  pm "I can help with that."

  show prowen neutral
  show merona t serious
  mi "Prowen offering to be the one to do it? I'm kind of surprised, but more curious as to why he'd want to so suddenly. He hasn't exactly communicated that much about himself or with us."

  rt "Oh, have you done something like this before?"

  show prowen neutral OM
  show lexan serious
  show kreita sceptical
  show boyen sceptical
  pm "More or less."

  pm "I can help talk to people and do some convincing."

  show prowen neutral
  show lexan neutral OM
  show kreita neutral
  show boyen tired
  ln "Ah... okay."

  ln "Okay. I guess we'll be... doing something of that sort."

  stop music
  show lexan neutral
  show kreita content
  show merona t content
  show boyen neutral
  ck "Finished."

  "Cimaria got up and stretched her neck on both sides. Rett seemed to be able to move his bandaged arms more, and he kept them at has sides."

  play music music_Roll_away_the_Stone
  show lexan neutral
  ck "What is good is that there is nothing critical with his bites and body at the moment."

  show lexan strict
  show merona t serious
  show kreita neutral
  show boyen worried
  mk "..."

  show lexan annoyed
  show merona t worried
  show kreita worried
  show boyen scared
  mk "What is bad is that there is venom inside him as a result of the bites, and I most likely need to make a specific medicine which we do not have."

  show prowen appalled OM
  pm "It's a monster then."

  show prowen appalled
  show merona t scared
  mi "Monster venom. So if we don't have that medicine..."

  show prowen neutral
  show lexan annoyed OM
  show kreita worried CE
  show merona t disappointed
  show boyen sceptical
  ln "Are you suggesting that Rett's health may be in possible danger?!"

  play music music_Sovereign
  show lexan annoyed
  show kreita worried
  show merona t sad
  mi "...at the worst, Rett could die?"

  show merona t sad CE
  show boyen worried
  rt "Wait, what does this all mean? What's going to happen to me?!"

  show lexan surprised
  show merona t worried
  show boyen tired
  ck "Calm down. Stressing over this situation will not help us, so please try your best to not become too anxious. I can obtain this medicine by purchasing the needed ingredients in most herb shops. We need to go into a town and possibly stay at an inn for a fast recovery."

  show prowen neutral OM
  show lexan worried
  pm "We now have two reasons for going to a town."

  show prowen neutral
  show boyen surprised
  bg "I'm worried if we have enough money for all of that. How much would it cost and how long can the venom stay in his body?"

  show lexan neutral
  show merona t serious
  show boyen sceptical
  ck "Depending on where we go to, it could cost a great deal or almost none at all. We would have to see once we arrive at one."

  show lexan serious
  ck "As for the venom, I cannot predict an accurate amount of time. I'm unfamiliar with monster venom and I am not sure how different monster venoms function once inside the body. I can only experiment with what remedies I find suitable and do what I can to the best of my ability."

  show prowen forcedSmile
  show merona t determined
  show boyen worried
  ck "We must hurry to a town. Is everyone set to leave right now?"

  show lexan strict
  show kreita worried OM
  kh "Right now sounds like a fine time."

  stop music fadeout 1.0
  show prowen neutral#; fade out
  show kreita worried#; fade out
  show boyen tired#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide prowen
  hide kreita
  hide boyen
  show merona t serious
  "Everyone dispersed, gathering everything we set up and collected. I looked around and spotted Duran still lying down."

  show lexan neutral
  show merona t sad
  mi "That's right. He didn't come, so he must be sleeping right now. We have to hurry and go..."

  play music music_recollections
  show lexan neutral OM
  show merona t surprised
  ln "Merona! Can you help me pick up some things?"

  #"-----------------------------------------------"
  show lexan neutral

  menu:
    "I have to get Duran first before we forget him! He needs to get up now!":
      $currentPath = "A"
      $AChoiceCount += 1
    "Duran will probably get woken up by someone else. I need to help Lexan load the cart fast!":
      $currentPath = "B"
      $BChoiceCount += 1
    "This monster in my arms needs to go somewhere safer! That has to be taken care of first!":
      $currentPath = "C"
      $CChoiceCount += 1

  #(Continued in 4.4)

  #"A4.4"
  #TODO [FINAL







  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"

  if (currentPath == "A"):
    call lbl_PathA_4_4 from _call_lbl_PathA_4_4_1 
  if (currentPath == "B"):
    call lbl_PathB_4_4 from _call_lbl_PathB_4_4_1 
  if (currentPath == "C"):
    call lbl_PathC_4_4 from _call_lbl_PathC_4_4_1   

  #"-----------------------------------------------------------"

  play music music_White
  show merona t worried
  mi "I hope we know where we're going. We haven't passed a town as of late. Otherwise..."

  show merona t sad
  mi "..."

  show merona t nervous
  mi "I just hope that we can do this without too many consequences."

  show merona t surprised
  ck "Is everyone ready? Nothing is left behind? Nobody is left behind?"

  #TODO [fade in CS cimaria serious#; right from Merona
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria serious:
    yalign 1.0
    xalign 0.75
  show merona t serious
  "Cimaria looked at each of us for a second and nodded."

  show cimaria serious OM
  show merona t worried
  ck "Good. We're all here. Now, someone please hand me the map. I need to see where is the closest large town for me to buy what is needed."

  show cimaria serious
  "Lexan dug into the bag of our records and threw the folded map to Cimaria."

  show cimaria neutral OM
  show merona t nervous
  ck "Thank you. Where are we approximately at now?"

  #TODO [fade in CS rett neutral OM#; right from Cimaria#; change body base to rett body injured2
  show rett injured2 neutral OM:
    yalign 1.0
    xalign 1.0
  show cimaria neutral
  rt "We should be nearing the longer river of the Northeastern Lake fork. I'm sure that there'll be some towns in that area. Even though our destination is not part of that direct path, it is in that direction, so it wouldn't exactly stop us from progressing there."

  show rett injured2 neutral
  show cimaria neutral OM
  ck "Yes... there are some towns near that area that have what we want. Which direction do we need to go now?"

  #TODO [move CS merona t serious to the right to make just enough space for Kreita #(a few hundred px probably?)
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t serious
  #TODO [fade in CS kreita serious OM
  show kreita serious OM:
    yalign 1.0
    xalign 0.2
  show cimaria neutral
  kh "If this creek is a tributary of Northeastern Lake's main river, we could follow it. It'd just lead us right there. I'm pretty sure it should be a part of that direction, looking farther down where the creek winds. Anyone else have any ideas?"

  stop music fadeout 1.0
  show kreita serious
  kh "..."

  #TODO [fade in Sound #(only once): Nature Ambiance
  play sound sound_ambiance
  show kreita serious CE
  show cimaria serious
  kh "..."

  show kreita worried OM
  kh "I assume 'no'."

  play music music_Ill_be_right_behind_you_Josephine
  show kreita worried
  show cimaria serious OM
  ck "*sigh* What other choice do we have? This is the best available option to make sure that Rett is safe. We may spend a large amount of our money on this and get off schedule with our arrival."

  show cimaria worried
  "Cimaria pursed her lips and paused for a moment."

  show cimaria worried OM
  ck "Is everyone alright with this decision?"

  scene cg hillSide
  show lexan strict OM#; center
  show prowen neutral:
    yalign 1.0
    xalign 0.1 #, left from Lexan"
  show boyen worried:
    yalign 1.0
    xalign 0.75 #, right from Lexan
  show duran t worried:
    yalign 1.0
    xalign 0.98 #; right from Boyen
  ln "We have to do this. We can't sacrifice the life of Rett for the convenience of staying on our current path."

  show prowen neutral OM
  show lexan strict
  pm "Whatever we do is fine with me."

  show boyen worried OM
  show prowen neutral
  bg "This is more than just arriving at where we're supposed to be. It's about being here for each other, so no doubt is doing this not only the best choice but the only choice."

  show boyen worried
  show duran t worried OM
  dt "How could we just not help Rett? Even I want to go out of the way to solve this."

  scene cg hillSide2
  #(positions as before the intermission with Lexan, Prowen, etc)
  show merona t sad OM
  show kreita worried:
    yalign 1.0
    xalign 0.2
  show cimaria serious:
    yalign 1.0
    xalign 0.75
  show rett injured2 worried:
    yalign 1.0
    xalign 1.0
 
  mk "Everyone really cares about him. We should definitely go and try to get this medicine, as soon as possible."

  show merona t sad
  mi "I don't even think it's necessary for her to ask that question. Of course we have to help Rett. No one here would think otherwise."

  show cimaria neutral
  "Cimaria stared at all of us for a short while and nodded."

  show cimaria gentle OM
  show merona t sadSmile
  ck "Thank you for understanding the situation..."

  show cimaria worried
  show rett injured2 wink OM
  show kreita neutral
  show merona t surprised
  rt "Guys, you're making a really big deal out of everything. Don't get so worked up over me. I promise you all that I'll be fine."

  play music music_A_Moments_Reflection
  show rett injured2 smirk
  show kreita shocked
  show merona t shocked
  show cimaria worried OM
  ck "I'm sorry Rett, but you can't guarantee that you'll be fine."

  show merona t desperate
  show rett injured2 worried
  show cimaria serious
  rt "..."

  show merona t sad
  show cimaria serious OM
  ck "Oh well... it really would be best if everyone tries to stay composed. Becoming too flustered will only slow us down."

  show kreita sad
  show cimaria neutral OM#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  hide cimaria
  ck "If everyone is ready to leave now, let us do so."

  show rett injured2 neutral#; fade out
  $ renpy.transition(slow_dissolve, layer="master")
  #TODO [fade Kreita out
  hide kreita
  show merona t sad CE
  "Cimaria marched forward, and Kreita hurried over to grab the cart and follow her."

  #TODO [fade to cg_sky1
  scene cg_sky1
  show clouds at LeftRight#; move from left to right
  "I guess it's time."

  "No one said anything else, and we all moved on."

  #TODO [After this chapter change Rett's body base back to the normal one

  #(Continued in 4.5)
  #"A4.5"
  #TODO [FINAL







  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"

  if (currentPath == "A"):
    call lbl_PathA_4_5 from _call_lbl_PathA_4_5_1 
  if (currentPath == "B"):
    call lbl_PathB_4_5 from _call_lbl_PathB_4_5_1 
  if (currentPath == "C"):
    call lbl_PathC_4_5 from _call_lbl_PathC_4_5_1   
  #(Continuation of 4.4)

  #"-----------------------------------------------------------"

  #TODO [fade out music
  stop music fadeout 1.0
  play sound sound_water#/ River #(same as in 3.8)
  show merona t worried
  "I looked away and stared at the stream instead. The water was becoming rougher, and further ahead, it was churning faster and faster."

  show merona t serious
  mi "I wonder if we'll be able to find some actual animals by the river."

  scene bg black with fade

  #"A4.6"
  #TODO [FINAL






  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"
  play music music_piano
  #TODO [fade from black
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg_sky3
  show cg forest1_5
  show black:
    alpha 0.3#; if possible please overlay something like 30% black on the forest to make the light look more like in morning hours
  mi "Hm..."

  "I stared back at the black ash in front of where I was on my stomach. The fire was only flicking up a few centimeters when I turned away and dozed off later. I rested my cheek on the back of my hands."

  mi "It was a nice gradual cooldown. Now if only, it had helped me get to sleep faster..."

  scene bg black with fade
  "I closed my eyes."

  mi "Now, just don't shut your eyes too tightly. Relax. Loosen up. Think boring thoughts. You can do it, Merona."

  mi "..."

  mi "......"

  mi "..."

  play music music_Lafayette
  #TODO [fade in...
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg_sky3
  show cg forest1_5 #; overlay something like 30% black
  show black:
    alpha 0.3
  mk "*soft groan*"


  mi "I wonder what time it is. It feels like I've only slept for an hour or two since the sky was getting lighter when I started to fall asleep. Not good. If I don't sleep a little more now, I won't be able to have much energy for all the walking we're going to do when everyone else wakes up. It's already light enough to wake some people up."

  mi "Why couldn't I fall asleep very easily? It almost felt like how long it took for me to fall asleep at the beginning of this journey... Maybe it's unconscious stress from myself. It's already been two days of searching, so the worry could be starting to creep into my mind."

  #TODO [fade to...
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forestGround
  show mattress#; center
  show merona t sleepy noHat#; center, use Merona hair u please
  show blanket#; center

  show clouds dark at LeftRight:
    alpha 0.3#; already in Drive here: https://drive.google.com/file/d/0By2EUlNeLO3Mb0VjQkNsQ2ZrMlU/view?usp=sharing #; "
  #"opacity around 30-50%#; "
  #"if possible, use a "multiply" mode for them please#; "
  #"slowly move from right to left please
  "I flipped over to my back and snuggled deeper into my covers, pulling them over my nose. I looked up at the sky."

  show merona t surprised noHat
  mi "Streaky clouds in the sky today... what will that mean for the weather later on?"

  show merona t reflective noHat
  mk "Hm..."

  show merona t serious noHat
  mi "I wonder where we exactly are right now or at least our general location. I think I should start observing the map more often rather than always asking; also, what if the others aren't that aware either? We only went in this semi-reliable route by following this stream. At least the stream is getting wider into the main river. That gives some kind of sign that we're on the right path since the towns are there."

  play music music_Green_Leaves
  show merona t sad noHat
  mi "All I have to do is stay positive over everything and do whatever I can to help. Like Cimaria said, worrying about things too much isn't beneficial, so I'll try working on that too. I hope the others are feeling okay right now."

  show merona t content CE noHat
  show merona t content CE noHat:
    yalign 1.5#; move sprite down by 100px please
  "I scrunched up into a ball and buried all of myself into the warmth of my blanket. The familiar cloth tickled my face the same way the blanket of my dorm bed did. I thought of my dorm room with all my plants and twitched."

  show merona t surprised noHat
  mi "You know... I never really told anyone to look after those plants."

  show merona t disappointed noHat
  mi "..."

  #TODO [move her sprite down by 100px
  show merona t disappointed CE noHat:
    yalign 1.7
  "I moaned and scrunched in even further."

  show merona t serious CE noHat
  mi "Well, maybe there's a kind soul that thought of them and is taking care of them without me even asking. That'd be the dream."

  show merona t sadSmile CE noHat
  mi "Those plants should be able to properly decompose at least."

  show merona t determined noHat:
    yalign 1.0#; move back to normal position
  #TODO [a bit later: move the blankets down by 200px
  pause(0.1)
  show blanket:
    yalign 2.5
  "I shot up and slapped my covers down."

  mi "I'm not really feeling like I'll get some more sleep right now. I think it might be better to get up and get myself up and energized. Yes, getting warmed up for another long day of trekking sounds just fine. But where to go?"

  if (currentPath == "B"):
    mi "I'm going to just wander near here and stretch a little. Loosen my muscles a bit."
  if (currentPath == "A"):
    mi "I want to go and sit down by the stream. Splashing a little water on me should help wake me up."
  if (currentPath == "C"):
    mi "I feel like climbing a tree. It's been a while since I've done it, and the rough bark may make me more alert."
  
  #"A4.7"
  #TODO [FINAL
  
  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"

  if (currentPath == "A"):
    call lbl_PathA_4_7 from _call_lbl_PathA_4_7_1 
  if (currentPath == "B"):
    call lbl_PathB_4_7_1 from _call_lbl_PathB_4_7_1_1 
    call lbl_PathB_4_7_o from _call_lbl_PathB_4_7_o_1 
    call lbl_PathB_4_7_2 from _call_lbl_PathB_4_7_2_1 
    $ renpy.transition(slow_dissolve, layer="master")
    hide lexan
  if (currentPath == "C"):
    call lbl_PathC_4_7 from _call_lbl_PathC_4_7_1  
  #(Continuation of 4.6)
  #"--------------------------------"

  show merona t serious
  "I trotted through the forest, meandering my way through the path I thought I took. As I kept walking, I saw that I was only moving slightly away from the clearing."

  #TODO [fade in CS merona t worried OM
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t worried OM
  mk "These paths are either a maze, or I just forgot the right direction. I could also be confusing myself too and be on the right path though..."

  #TODO [fCS merona t content
  show merona t content
  "I went down a little further and saw the familiar plants and land from where I came from."

  show merona t grin
  "Good, I'm going the right way. All I have to do now is-"

  show merona t surprised
  "I turned my head and saw someone sitting on a large fallen tree."

  show merona t content
  mi "That's..."

  play music music_She_dreams_in_blue
  show merona t happy
  mk "Cimaria."

  show merona t grin
  "At the mention of her name, she flinched and turned to the sound of my voice."

  show merona t content
  ck "Oh... Merona?"

  #TODO [fade Merona out
  $ renpy.transition(slow_dissolve, layer="master")
  hide merona
  "I started making my way over to her."

  #(Continued in 4.8)

  #"A4.8"
  #TODO [FINAL





  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"
  #(Continuation of 4.7)
  #play music music_She_dreams_in_blue #(from before)
  scene cg forest20
  show cimaria surprised:
    yalign 2.5
    xalign 0.75#; right#; positioned 250px lower than normal height
  #show sunShine#; this will become a simple animation with probably 1920 x 1080px size
  show sunrays movie
  ck "What are you doing over here?"
  #TODO [fade in CS merona t content#; left#; positioned 230px lower than normal height
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t content:
    yalign 2.3
    xalign 0.25
  show cimaria neutral
  "I stumbled over some thick roots and made it to a fallen tree opposite of Cimaria's spot. Plopping down on the long trunk, I straightened my clothes out."
  show merona t content OM
  mk "I wanted to get up and do something, so I'm just walking around here. What about you?"
  show merona t content
  show cimaria neutral CE
  "She shrugged and leaned back on her hands."
  show merona t worried
  show cimaria neutral OM
  ck "Something similar to what you are doing, I suppose. Doing some thinking."
  show merona t worried OM
  show cimaria serious
  mk "How have you been lately? Everything has been a bit more jumbled than what we're used to, so are you doing fine?"
  stop music fadeout 1.0
  show merona t worried
  show cimaria serious OM
  ck "I'm... only okay."
  show merona t sad
  show cimaria worried OM
  ck "Or you could say that... I'm trying to be okay."

  play music music_newBegin
  show merona t worried OM
  show cimaria worried
  mk "Yeah. I get the feeling."
  show merona t worried
  mk "..."
  show merona t determined OM
  show cimaria surprised
  mk "Do you want to let someone listen to you talk about it?"
  show merona t determined
  show cimaria gentle#; fade to cimaria gentle CE
  $ renpy.transition(slow_dissolve, layer="master")
  pause(0.1)
  show cimaria gentle CE
  "Cimaria stared at me with a faint smile and eventually closed her eyes."
  show merona t surprised
  show cimaria gentle OM CE
  ck "Are you sure you want to hear an old person like me talk about my problems?"
  show merona t grin CE
  show cimaria gentle
  "I snorted and nodded."
  show merona t content OM
  show cimaria grin
  mk "Yes. Even though you're not old-you're not even a decade older than I am."
  show merona t content
  show cimaria gentle OM
  ck "*laugh* Still, I'm old compared to you. I think when I was about your age-sixteen years old, yes?-I thought that being the age I am right now was unimaginable."

  show merona t happy
  show cimaria grin
  mk "Sounds like you were a dramatic teenager."
  show merona t grin
  show cimaria wink
  "Cimaria winked and sheepishly grinned."
  show cimaria neutral OM
  ck "You could say that. But enough about how my adolescent years were. You asked to listen to what I'm thinking of right now."
  show merona t serious
  show cimaria neutral
  mi "Right now, I sort of get the feeling that Cimaria seems a bit different from usual. I don't know, she just seems to be not as... Cimaria-ish."
  show merona t reflective
  "But, maybe who I thought she was isn't who she actually is. I can't exactly say that I've closely interacted with her in different situations, so I wouldn't know. This can be another side of her that I've never encountered yet."
  show merona t surprised
  show cimaria worried
  "Cimaria looked down at her short shadow, focusing on the silhouette of the strands of her hair getting pushed up by the gentle breeze. She clamped her lips shut first, but opened them again soon after."
  stop music fadeout 1.0
  show merona t serious
  show cimaria worried OM
  ck "I feel as if..."
  play music music_Roll_away_the_Stone
  show merona t worried
  show cimaria serious OM
  ck "I'm not doing my job properly."
  show merona t worried OM
  show cimaria serious
  mk "What do you mean? You're doing everything you can."

  show merona t worried
  show cimaria serious OM
  ck "I know that this is all that I can do-however, there is so much more that needs to be done on my part that I should be able to do, and I'm unable to do it."
  show merona t disappointed
  show cimaria serious OM CE
  ck "I should be able to at least do something that will help treat wounds or injuries. But I couldn't with Rett. I couldn't give him anything. Even if it is monster venom, any kind of venom should be able to be treated by something that'll at least numb some pain, but I couldn't even think of that when I was dealing with his bites when they were still fresh."
  show merona t worried
  show cimaria serious OM
  ck "Despite every bit of training and work that I've gotten, I couldn't even think to take some of the pain away."
  show cimaria worried OM
  ck "I can't even provide some of the needed common herbs for these types of things. I wasn't able to even to diagnose if he was going to die soon or not! These are some of the basic requirements to being a healer, and I couldn't fulfill them for Rett."
  show merona t nervous
  show cimaria worried
  mk "..."
  show cimaria worried CE
  "Cimaria closed her eyes."
  show merona t serious
  show cimaria worried OM CE
  ck "I can't let him die, Merona."
  ck "It's not even about letting someone die break my integrity o-or reputation as a healer, b-but..."
  show merona t surprised
  show cimaria serious OM
  ck "...it's just something else. I don't really know if I can say it, or if I want to say it but, it's something else."
  show merona t worried
  show cimaria serious
  ck "..."
  play music music_River_Meditation
  show cimaria serious OM
  ck "I'm not going to let it happen."
  show merona t serious
  show cimaria serious
  mk "..."
  "I didn't want to say anything back to her. Not even something encouraging or helpful."
  show merona t serious CE
  "This is not the time to say anything, but rather it is the time to sit back and stay silent."
  show merona t serious
  show cimaria neutral
  "Like... a moment to simply watch, but not capture."
  show cimaria sadSmile
  "Cimaria flashed me a bittersweet smile."
  ck "..."
  play music music_Sugar_On_My_Tongue
  show merona t surprised
  show cimaria sadSmile OM
  ck "With you, I was lucky that your venom was able to be somewhat treated with what I had at the time."
  show merona t worried
  show cimaria sadderSmile OM
  ck "I had really thought that I was capable of doing this journey because of that. But look at what's happened now. I can only pretend that I know what I'm doing and try to make everyone believe that things will go smoothly. Pathetic."
  ck "I'm just deeply sorry that I had to be the one here for Rett."
  show cimaria sadderSmile
  "Cimaria let out a breath and looked to the side at the rest of the forest."
  show merona t surprised
  show cimaria sadSmile OM
  ck "...That must have been a lot of rambling."
  show merona t sadSmile
  show cimaria worried OM
  ck "I do apologize if it was a bit much, Merona. I should have held back a little."
  show merona t sadSmile OM
  show cimaria worried
  mk "No, no-it was fine. Don't worry about it at all. How long has it been since you've just talked about everything like that with someone?"
  show merona t serious
  show cimaria neutral OM
  ck "How long has it been? Hm..."
  show cimaria sadSmile
  "She lifted up a corner of her mouth."
  show merona t reflective
  show cimaria sadSmile OM
  ck "It has been a while. You can say that the last person who listened is off somewhere in her own world up there now. But I will admit, talking like this helped."
  show merona t content OM
  show cimaria content
  mk "That's good to hear."
  show merona t serious
  show cimaria neutral
  "I paused for a moment, wondering if I should ask, but I decided to go for it."
  play music music_romance
  show merona t serious OM
  show cimaria surprised
  mk "How familiar with Rett are you?"
  show merona t serious
  show cimaria abashed
  "Cimaria raised an eyebrow and smirked."
  show merona t sadSmile
  show cimaria abashed OM
  ck "I see you decide to ask that question after what I've said about him."
  show merona t happy
  show cimaria abashed
  mk "Psh, it's just... a simple question that I'd like to know the answer to!"
  show merona t content
  show cimaria neutral OM
  ck "A simple question will get a simple answer then. I usually help Rett keep watch at night for a few hours. That's how familiar I am with him."
  show merona t grin ER
  show cimaria neutral
  mi "Keeping watch, you say? Oh, really?"
  show merona t grin CE
  show cimaria surprised
  "I held both hands up and sighed."
  play music music_potHappy
  show merona t content OM
  show cimaria gentle
  mk "Alright, alright, that's good enough. Sort of."
  show merona t content
  show cimaria laugh
  "She laughed and hung her head down."
  show cimaria content OM
  ck "You don't need to know anything else. I've already told you enough about what has been going on in my mind."
  
  #(Continued in 4.9)
  #"4.9"
  #TODO [FINAL


  #The dashed line separates where the main storyline and path separate. The main storyline will be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"

  #(Continuation of 4.8)
  #play music music_potHappy #(from before)
  show cg forest20 #(as before)
  show merona t content OM
  show cimaria neutral
  show sunrays movie #(as before#; always over characters)
  mk "Well, there's always next time for more."
  show merona t surprised
  show cimaria abashed
  "Cimaria scoffed and swatted her hand at me."
  show merona t sadSmile
  show cimaria abashed OM
  ck "More like there's always never in the future for more."
  play music music_Lafayette
  show merona t surprised
  show cimaria sadSmile OM
  ck "While we're at it, do you have anything you feel like sputtering out? I've already dumped all of my thoughts onto you, so having new ones wouldn't hurt."
  show merona t happy
  show cimaria content
  mk "Ha ha, I don't exactly have that much on my mind, but if-no, probably when-I do, I'll make sure to vomit out as much as I can."
  show merona t serious
  show cimaria neutral OM
  ck "I hope you won't get to the point where you have to do so, though it is better to let those sorts of things out rather than manifesting them inside you. However, I'm not sure if it will be inevitable for it to come to that..."
  show merona t worried
  show cimaria neutral
  "I bit my bottom lip and squinted my eyes."
  show merona t content OM
  show cimaria gentle
  mk "I don't think there'd be much for me to worry about...probably. I don't know. But I'll try to take care of myself."
  show merona t content
  show cimaria gentle CE
  "Cimaria hummed a note of satisfaction."
  show cimaria gentle OM
  ck "Good. I won't let you crumble down either-I will not let anyone here fall over from anything anymore."
  show merona t worried OM
  show cimaria worried
  mk "But sometimes we can't help but topple from unexpected things... We won't be able to help ourselves with that."
  show merona t serious
  show cimaria worried OM
  ck "It's a shame... but I suppose what we should always be able to do to rise up each time... from the smallest stumble to the dive off into an endless abyss."
  show merona t content OM
  show cimaria gentle
  mk "To be able to rise after any kind of fall... Yes, that's the best thing that can be accomplished by us if we're strong enough."
  show merona t reflective
  show cimaria neutral OM
  ck "I cannot say that I myself have this ability. I have never been exposed to all kinds of falls, but this is only a beginning to a long spiraling cycle of mountains and valleys-it'll only come to us when we're rich in experience."

  show merona t surprised
  show cimaria serious
  "Cimara paused, and her face hardened."
  show cimaria serious OM
  ck "Don't forget about this, Merona."
  show merona t determined
  show cimaria neutral OM
  ck "These problems may seem like small problems in the future, but nonetheless, they are still problems being faced today, so they must be dealt with accordingly...with confidence and persistence as well."
  show merona t serious
  show cimaria neutral
  "I stared at Cimaria. She was sitting taller and held herself up more, looking more put together and like how she appeared to me before."
  play music music_Ill_be_right_behind_you_Josephine
  show merona t content
  mi "Even healers need a bit of healing for themselves too."
  show merona t grin
  show cimaria serious
  mi "Cimaria is looking and sounding a lot better now... It goes to show that talking can help out our emotional or mental health as well."
  show cimaria surprised
  "A small chuckle wanted to bubble out of me, but I suppressed it before it leaked into the air. Cimaria lifted only one side of her mouth up, making a crooked smile."
  show merona t sadSmile
  show cimaria neutral OM
  ck "Care to share what you find so amusing, Merona?"
  show merona t sadSmile OM
  show cimaria worried
  mk "Uh, it's nothing, really. I was just thinking to myself of how talking is helpful. Sometimes I either get wrapped up in my head by thinking or talking aloud too much, so now I at least have good reason to be incredibly chatty around others."



  show merona t content OM
  show cimaria neutral
  mk "Usually it's when I'm with friends that I feel that I might talk too much, but we all sort of do talk a lot. You could say we're all being therapeutic."
  show merona t content
  show cimaria gentle OM
  ck "*laugh* I'm glad to hear that you get along so well with your friends. Just make sure not to get in any kind of trouble with them, alright? You're probably fine already though."
  show cimaria gentle
  "I shrugged and smiled."
  show merona t content OM
  mk "Well... sort of."
  show merona t content
  show cimaria gentle OM
  ck "*laugh* Okay."
  play music music_recollections
  show cimaria content OM
  ck "I think I'm going to go over to get some papers by our cart and come back here. We most likely will leave in around half an hour or so-if the others aren't up yet, I will wake them up. You may do something else if you wish. I don't want to force you to stay with me."
  show merona t happy
  show cimaria content
  mk "Oh, alright then. Can I go back to the cart with you then? I'll probably grab some things from my other bag or write in my journal in my bed since I won't risk falling asleep again."
  show merona t content
  show cimaria content OM
  ck "Of course, of course. Shall we leave now?"
  show merona t happy
  show cimaria content
  mk "Sure!"
  #TODO [move both sprites to normal height position
  show cimaria:
    yalign 1.0
    xalign 0.75
  show merona t content:
    yalign 1.0
    xalign 0.25
  "The two of us got up from our seats and made our way out of the jumble of roots, going into the groups of trees leading back to our camp. Right as we began walking, Cimaria cleared her throat."
  show merona t surprised
  show cimaria neutral OM
  ck "*cough* As much as I'll complain or whine over being incapable of doing things whether aloud or in my head..."
  show merona t content
  show cimaria serious OM
  ck "...know that I'll never give up or truly think that I'm unable to do anything-if that ever happens, that will be the end for me."

  show cimaria neutral OM
  ck "And if you ever reach a stage like that, please try to get yourself out of it. Know that you shouldn't ever actually think you aren't able to do anything, because there will always be at least one thing you can do."
  show merona t grin
  show cimaria gentle OM
  ck "Don't rob yourself of even your choices, and always keep some inner-faith festered inside you. This is what I want to you to know."
  show merona t surprised
  show cimaria neutral
  mk "..."
  stop music fadeout 1.0
  show cimaria sadSmile OM
  ck "And..."
  show cimaria sadSmile
  "Cimaria sighed, shaking her head with a wry smile."
  play music music_title
  show merona t sadSmile
  show cimaria sadderSmile OM
  ck "...I'm also trying to get a bit of my self-dignity back by giving you some advice, so I hope that you can follow it."
  show merona t grin CE
  show cimaria abashed
  "I snorted and lightly punched her arm."
  show merona t happy
  show cimaria content
  mk "Yeah. I can do that for you. Even if it wasn't for helping you restore your self-dignity."
  show merona t grin
  "She patted my shoulder in return, and we continued walking back to our clearing without any other leaked words."
  show merona t content
  mi "Cimaria, I hope that you can actively handle teenagers for longer periods of time because you may be getting more appearances by a certain gabby one here in your vicinity."

  scene bg black with fade
  #"A4.95"
  #TODO [FINAL








  #The dashed line separates where the main storyline and path separate. The main storyline will "be the same text in scripts A, B, and C. This path's storyline is in blue."
  #"-----------------------------------------------------------"

  #TODO [Setting notes: Evening, around 8-9 PM. Sky isn't completely dark yet, but the sun has pretty much set. In an area without much space to completely settle. Everyone is seated close to each other, finishing dinner.

  play music music_Radio_Martini
  play sound sound_nighttimeAmbience
  scene bg black
  pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest20_5
  #TODO [fade from black
  #TODO [fade in CG forest20 5

  #TODO [all sprites placed 200px lower than usual...
  #TODO [fade in CS merona t serious#; center
  show merona t serious:
    yalign 2.0
    xalign 0.55
  #TODO [fade in CS kreita content#; right from Merona
  show kreita content:
    yalign 2.0
    xalign 0.7
  #TODO [fade in CS rett content#; right from Kreita
  show rett content:
    yalign 2.3
    xalign 0.9
  #TODO [fade in CS prowen neutral#; right from Rett
  show prowen neutral:
    yalign 2.2
    xalign 1.1
  #TODO [fade in CS cimaria neutral#; left from Merona
  show cimaria neutral:
    yalign 2.3
    xalign 0.4
  #TODO [fade in CS lexan neutral#; left from Cimaria
  show lexan neutral:
    yalign 2.3
    xalign 0.25
  #TODO [fade in CS boyen neutral#; left from Lexan
  show boyen neutral:
    yalign 2.0
    xalign 0.05
  show duran t neutral:#; left from Boyen
    yalign 1.5
    xalign -0.05
  "I pushed around the remnants of beans on my plate."

  show merona t nervous
  mi "Being the first to finish a meal is always awkward... Waiting for everyone else makes me feel like I'm silently pushing them to finish up."

  show merona t content
  mi "At least I have these morsels to entertain myself with."

  play music music_Summer_Day
  show merona t surprised
  show lexan serious OM
  ln "Hey, Merona. Do you have some time right now?"

  show lexan serious
  "I bobbed my head up, and Lexan was also done with dinner."

  show merona t surprised OM
  show lexan neutral
  mk "Uh, yeah. What do you need?"

  show merona t serious
  show lexan neutral OM
  ln "Well, it's something you need more than me. Do you want to test your ability with the monster?"

  show lexan neutral
  "I blinked."

  show merona t nervous OM
  mk "The monster? Right now?"

  show merona t nervous
  show lexan worried OM
  ln "If we don't do it sooner or later, this monster could be unusable. Now is a good time to take advantage of it."

  show lexan determined
  "Lexan looked to everyone else."

  show merona t serious
  show lexan determined OM
  ln "We do have a little time, right? I know we're not going to stay here overnight, but do we have an hour or so before we depart again?"

  show lexan content
  show cimaria gentle OM
  ck "I believe so. We've got a little time."

  show merona t sadSmile
  show cimaria content
  show kreita content OM
  kh "Yeah, you guys go and do whatever you need while we're here. It's going to be a long, weary night of walking though, so don't break your legs. Or anything else."

  show merona t serious
  show lexan content CE
  show kreita content
  "Lexan nodded."

  play music music_Cool_Steel_Breeze
  show lexan content OM
  ln "Okay. Ready, Merona?"

  show merona t determinedGrin
  show lexan determined
  mi "It's monster time!"

  #TODO [move Merona to normal sprite height position, then fade out
  show merona:
    yalign 1.0
    xalign 0.55
  pause(0.3)
  $ renpy.transition(slow_dissolve, layer="master")
  hide merona
  "I got up and set my plate back on the stack sitting in the cart."

  #TODO [fade in CS merona t serious OM#; center
  $ renpy.transition(slow_dissolve, layer="master")
  show merona t serious OM
  show lexan content:#; move up to normal height position
    yalign 1.0
    xalign 0.25
  mk "So, where are we gonna go?"

  show merona t content
  show lexan content OM
  ln "Let's see if can find a place where there's a little more room to work. It's a bit claustrophobic here with everyone."

  show lexan content
  "Grabbing the monster's pouch out of my bag, I nodded."

  show cimaria gentle OM
  ck "Be safe, you two. Call us over if you need help."

  show merona t content OM
  #TODO [fade both out
  $ renpy.transition(slow_dissolve, layer="master")
  hide lexan
  hide merona
  show cimaria gentle
  mk "Aye, aye!"

  $ renpy.transition(slow_dissolve, layer="master")
  #TODO [fade in CG forest20 75
  scene cg forest20_75
  #TODO [fade in CS merona t serious#; left side of screen
  show merona t serious:
    yalign 1.0
    xalign 0.1
  #TODO [fade in CS lexan neutral#; right from Merona
  show lexan neutral:
    yalign 1.0
    xalign 0.5
  "Lexan and I walked deeper into the forest, scanning through the gaps of the trees for an open spot."

  show merona t nervous
  mi "How big should the space be? This monster is only fish-sized after all, so I can't imagine that it's going to suddenly grow into a gargantuan beast."

  show merona t surprised
  mi "But who knows?"

  show lexan content OM:#; move to a spot right from the center
    yalign 1.0
    xalign 0.75
  show merona t content
  ln "Ah, here's a good place!"

  #TODO [move Merona to the center
  show merona t content:
    yalign 1.0
    xalign 0.35
  show lexan content
  "I followed his lead. We snaked between two trees and stepped over a fallen trunk."

  show merona t serious
  show lexan neutral OM
  ln "Alright. Before we do anything with the monster, let's go over what happened that day in the school gardens."

  stop music
  show lexan neutral
  "He froze."

  play music music_Ill_be_right_behind_you_Josephine
  show lexan shocked OM
  ln "Wait-I'm sorry, you probably don't want to think about that."

  show lexan shocked
  "I paused for a moment."

  show lexan worried
  mi "I remember what happened to me the first time when the memory came back at the campfire..."

  show merona t nervous
  "But it didn't happen because I was trying to think of it, right?"

  $ renpy.transition(slow_dissolve, layer="master")
  hide cg forest20_75
  show bg black behind merona
  #TODO [fade background to black screen
  "It just suddenly attacked my mind again. "

  $ renpy.transition(slow_dissolve, layer="master")
  show meronaflashback scared at right behind merona
  show rabbitMonster at left behind merona
  show cg danger behind merona:
      alpha 0.45
  #TODO [fade background to CG danger
  hide lexan
  #TODO [fade out Lexan
  #TODO [fade in CS merona scared#; right#; 60% opacity
  #show meronaflashback scared at right 
  #TODO [fade in CS rabbitM#; left, 60% opacity
  #show rabbitMonster at left behind merona
  show bg black behind merona
    
  "A spark provoked the memory out of where I buried it in my mind, and the unexpected return just hit me out of nowhere, as if I was in danger once more."

  show merona t determined CE
  "..."

  #TODO [fade out rabbitM and merona scared
  #TODO [fade background back to forest20 75
  #TODO [fade in CS lexan serious#; at former positon
  $ renpy.transition(slow_dissolve, layer="master")
  hide meronaflashback
  hide rabbitMonster
  show cg forest20_75
  show lexan serious:
    yalign 1.0
    xalign 0.75
  show merona t determined OM
  mk "I think... I'll be fine."

  show merona t serious
  show lexan serious OM
  ln "You don't have to force yourself to imagine it if you don't want to. It's okay if-"

  show merona t content CE
  show lexan serious
  "I shook my head."

  show merona t serious OM
  show lexan neutral
  mk "It's not about me feeling obligated to do this. I'm capable of simply describing what went down, and... "

  show merona t content OM
  mk "...I'm pretty safe here, so I know I'll be okay."

  show merona t content
  show lexan worried OM
  ln "If you don't want to talk about it, then stop whenever. We can head back sooner if needed."

  show lexan worried
  mi "I'm going to be fine. I'm going to be just fine."

  show merona t reflective OM
  show lexan neutral
  "I took a deep breath."

  show merona t serious OM
  mk "As soon as I saw the monster, I started running away. Probably the fastest I've ever ran."

  show merona t serious
  "I clutched my shoulder."

  show merona t serious OM CE
  show lexan worried
  mk "Then... I either tripped first or the monster swung at me first and caused me to trip."

  show merona t nervous
  mi "All that dust that clouded around me really burnt my eyes. Not to mention the nasty pain on the side of my body from sliding across the ground."

  show merona t determined OM
  mk "I squeezed my eyes shut, and then I..."

  show merona t nervous OM
  mk "I..."

  show merona t serious OM
  mk "Just concentrated hard. Trying to tell myself that if I concentrated hard enough, I could will myself to survive."

  show merona t disappointed
  mi "Ugh. I never want to experience those emotions again."

  show merona t worried OM
  show lexan neutral
  mk "Next thing I knew, nothing happened, and a bunny was sitting in front of me."

  show merona t worried
  "Lexan stared at me, taking in my words."

  show merona t serious
  show lexan neutral OM
  ln "Quite interesting, no matter how many times I hear it..."

  play music music_newBegin
  show lexan determined OM
  ln "I do think it's unlikely that the monster suddenly ran off and was replaced by a rabbit though. There must have been some kind of transformation involved."

  show merona t serious OM
  show lexan determined
  mk "A transformation..."

  show merona t nervous OM
  show lexan content
  mk "So you want me to try and transform this monster fish into another creature?"

  show merona t serious
  show lexan content OM
  ln "It's worth a try."

  show lexan content
  mi "I wonder..."

  show merona t reflective
  mi "What will happen if I actually do manage to transform it?"

  show merona t nervous
  mi "Is it going to become another animal? Another monster?"

  "..."

  play sound [sound_punch, sound_punch, sound_punch]#, three times
  show lexan surprised
  "I opened my pouch and pulled out the creature. Seeing myself reflected back in those eyes always gave me a jolt. I shook my head and slapped my cheek a few times."

  #TODO [fade in CG FishmonsterEyes
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg FishmonsterEyes
  mi "Let's hold this little guy, close my eyes, think hard, and see what happens."

  scene bg black with fade 
  "I tried to focus on something-any thought that I could grasp onto with all my might-but there was nothing I could find to put my strength in."

  "All the energy left the monster, and merely trying to concentrate on the its body wasn't going to work."

  mi "No connection. No flow. Nothing."

  "Squeezing my eyes shut even more didn't help either. The monster wasn't completely void though... It felt more like I was void of something. Something I couldn't really understand enough to be able to use it."

  "Whatever it was, I couldn't do this until I found it."

  stop music fadeout 1.0
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest20_75
  show merona t disappointed:
    yalign 1.0
    xalign 0.35
  show lexan worried:
    yalign 1.0
    xalign 0.75
  #TODO [fade in CG forest20 75
  #TODO [fade in CS merona t disappointed
  #TODO [fade in CS lexan worried
  "I sighed and opened my eyes."

  show merona t disappointed OM
  show lexan serious
  mk "This won't work."

  show merona t nervous
  show lexan serious OM
  ln "Hm... What exactly is the problem?"

  show merona t nervous OM
  show lexan serious
  mk "I... I'm missing something. I don't know. I haven't found what I need to do."

  play music music_recollections
  show merona t serious OM
  show lexan neutral
  mk "It's not the monster's fault. It's my own inability. I don't think it'll be useful if I keep trying to transform it in this way... I need more time to process what I can do."

  show merona t serious
  show lexan sadSmile OM
  ln "That's completely understandable. If there's a way in which I can assist you, please let me know, and I'll do my best."

  show merona t content
  show lexan sadSmile
  "I smiled at him, nodding."

  show merona t content OM
  show lexan neutral
  mk "Yeah. Let's go back now. We'll need to get going soon."

  show merona t content
  show lexan neutral OM
  ln "Sure. It's a shame it couldn't be transformed ."

  show merona t surprised
  show lexan neutral
  "I shrugged as we headed back to the group."

  show merona t laugh
  show lexan content
  mk "*laugh* Only because I couldn't turn it into a roast chicken!"

  show merona t sadSmile
  mi "I suppose I'm also a little relieved that nothing happened at the moment. With what's going on with Rett and everything else, I can push it to the back of my head."

  show merona t serious
  mi "For now, at least."

  play music music_Travel_Light
  
  $ renpy.transition(slow_dissolve, layer="master")
  scene cg forest20_5
  #TODO [fade in CG forest20 5
  #TODO [fade in CS merona t content#; right
  show merona t content:
    yalign 1.0
    xalign 1.1
  show lexan content:
    yalign 1.0
    xalign 0.9
  #TODO [fade in CS lexan content#; left from Merona
  "By the time we got back, the others were prepared to set off."

  #TODO [fade in CS kreita content, center
  #TODO [fade in CS rett content OM#; right from Kreita
  #TODO [fade in CS wagon#; behind character sprites#; center
  $ renpy.transition(slow_dissolve, layer="master")
  show kreita content:
    yalign 1.0
    xalign 0.6
  show rett content OM:
    yalign 1.0
    xalign 0.35
  show wagon behind merona
  show lexan sadSmile
  rt "That was fast. Any progress from you guys?"

  show rett neutral
  show merona t sadSmile
  "I shook my head."

  show merona t sadSmile OM
  mk "Still working on it."

  show rett smirk
  show merona t surprised
  "Rett patted my hat."

  show rett content OM
  show merona t content
  show lexan content
  rt "You can do it. You're a smart kid."

  show rett content
  show lexan content OM
  ln "I'm glad we didn't make you guys wait too long for us. Shall we depart?"

  #TODO [fade in CS cimaria neutral OM#; left from Rett
  $ renpy.transition(slow_dissolve, layer="master")
  show cimaria neutral OM:
    yalign 1.0
    xalign 0.15
  show lexan content
  ck "We're all ready. Prowen, are you good to go?"

  #TODO [fade in CS prowen neutral, left from Cimaria
  $ renpy.transition(slow_dissolve, layer="master")
  show prowen neutral:
    yalign 1.0
    xalign -0.13
  show cimaria neutral
  show merona t surprised
  show rett neutral
  "He nodded and rose from the ground. As he got up, two rolled up pieces of paper fell from his bag and landed by Cimaria's feet. A gust pushed a third one to tumble to Kreita."

  show prowen shocked
  "All I saw was a flash of an image and a high number. A very high number."

  show merona t nervous
  "Those are... posters?"

  play music music_Under_the_Stairs
  show merona t serious
  show lexan neutral
  show kreita neutral
  show cimaria surprised
  show prowen appalled
  "Prowen lunged over to Cimaria and snatched them away, stuffing them back into his bag. Kreita had already unfurled one, but Prowen hesitated to grab hers as well."

  show cimaria serious OM
  show prowen surprised
  ck "Uh... Sorry, was that something private, Prowen?"

  show merona t surprised
  show cimaria serious
  show prowen serious OM
  pm "*cough* No. I apologize for coming at you so suddenly... I was just..."

  show cimaria worried
  show prowen forcedSmile OM
  pm "...Worried that they'd get ruined by the ground."

  show kreita content
  show merona t serious
  show cimaria neutral
  pm "It's just spare paper."

  show lexan surprised
  pm "For writing. Or drawing."

  show prowen neutral OM
  pm "Or whatever."

  show lexan neutral
  show rett content
  show prowen serious
  "Rett leaned against the wagon."

  show merona t content
  show lexan content
  show rett content OM
  show kreita grin
  show cimaria content
  show prowen forcedSmile
  rt "Oh, we could give you paper if you want. These guys have several notebooks, so I'm sure they'd be willing to spare a piece."

  show rett smirk
  show kreita laugh
  show prowen neutral
  kh "Yeah, you don't have to use the backs of old posters! That Nony Soum guy on there is up on a ton of posters across the area, so he won't be missed."

  show rett content
  show kreita content
  show merona t serious
  "Prowen kept a blank look on his face as Kreita handed the sheet back to him."

  show prowen neutral OM
  pm "Uh, okay. Thanks."

  play music music_Cool_Steel_Breeze
  show cimaria content OM
  show prowen neutral
  ck "If you're all situated now, then let's leave."

  show cimaria neutral
  #TODO [start walking animations
  show kreita content at walkBounce
  show merona t content at walkBounce
  show lexan content at walkBounce
  show rett content OM at walkBounce
  show cimaria neutral at walkBounce
  show prowen neutral at walkBounce
  #TODO [fade out Kreita, Rett, Lexan and Cimaria
  pause(0.5)
  $ renpy.transition(slow_dissolve, layer="master")
  hide kreita
  hide rett
  hide lexan
  hide cimaria
  "We all started up the path again, with Kreita and Rett leading the way with the cart. I glanced over at Prowen."

  show merona t worried
  #TODO [fade out Prowen
  $ renpy.transition(slow_dissolve, layer="master")
  hide prowen  
  mi "He keeps staring at Cimaria, Kreita, and Rett. Is he just sensitive over being called out?"

  show merona t serious
  mi "..."

  show merona t content#; fade out  
  $ renpy.transition(slow_dissolve, layer="master")
  hide merona
  mi "I guess everyone, even Prowen, gets embarrassed every now and then."

  scene bg black with fade

  jump lbl_chapter5
