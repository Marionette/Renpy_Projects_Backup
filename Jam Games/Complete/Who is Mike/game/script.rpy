# Main Character
define y = Character ('You', show_two_window=True)
define s = Character ('Sarah', who_color="#FFFF66", what_color="#FFFF66", show_two_window=True, who_text_align=0.5,)
define m = Character('Mike', what_color="CC33FF", who_color="CC33FF", show_two_window=True, who_text_align=0.5,)
define u = Character ('???', what_color="CC33FF", who_color="CC33FF", show_two_window=True, who_text_align=0.5,)
define d = Character ('Fake Mike', what_color="CC0000", who_color="CC0000", show_two_window=True, who_text_align=0.5,)
define b = Character ('Mike & You', show_two_window=True, who_text_align=0.5,)
define ds = Character ('Fake Sarah', what_color="CC0000", who_color="CC0000", show_two_window=True, who_text_align=0.5,)

init:
    $ cr = Character(None,
                            what_color="#fff",
                            what_size=20,
                            what_layout="subtitle",
                            what_xalign=0.5,
                            what_text_align=0.5,
                            window_background=None,
                            window_yminimum=0,
                            window_xminimum=0,
                            window_xfill=False,
                            window_xalign=0.5,
                            window_yalign=0.5)
init:
    $ left = Position(xpos=0.11, xanchor='left')
    $ rightblur = Position(xpos=0.930, xanchor='right')
    $ center = Position(xpos=0.5, xanchor='center')
    $ right = Position(xpos=0.9, xanchor='right')

    $ top = Position(xpos=0.5, xanchor='center', ypos=0.0,
                   yanchor='top')
init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    
    $ timer_range = 0
    $ timer_jump = 0
    
label start:
  $ truth = 0
  $ lie = 0
  $ agree = 0
  $ disagree = 0
  $ truthcount = 0
  $ liecount = 0
  $ agreecount = 0
  $ disagreecount = 0

  ############# STORY STARTS HERE ###########
  stop music fadeout 2.0
  scene bg black with flash
  play sound "sfx/thump2.ogg"

  scene bg blur
  with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
  y "Ugh! My head!"
  "My nape throbbed with a sudden, persistent pain."
  "Dizziness came and went like a slow trickle of sweat."
  "What--?"
  play music "sfx/room.ogg"
  "It was evening." 
  "The curtains were closed and the sound of blood thumping in my ears made the silence malignant."
  "I was in my house, yes."
  "But I was disoriented. Something felt amiss."
  "There was a certain creepiness that made the hairs on my arms prickle."
  "I blinked at my surroundings."
  "{i}My glasses...{/i}"
  "{i}Where are they?{/i}"
  "D-Did I bump into something? Or--"
  with flash
  show mike blurredangry at rightblur
  u "S-Stay back, whatever you are!"
  show mike blurredscared at rightblur
  "Even before I heard his voice, I had felt the presence of someone else in the room."
  "It justified the awful feeling in my gut."
  show mike blurredangry at rightblur
  u "J-Just... Don't move!!"
  show mike blurredscared at rightblur
  "Oh my God."
  "There was..."
  "A stranger in my house!"
  "He held a bat with his outstretched arms, maintaining the distance between us."
  show mike blurredangry at rightblur
  u "G-Get back!"
  show mike blurredscared at rightblur
  "I didn't know what to do."
  "I opened my mouth in several attempts to say something."
  "{i}'Dont hurt me'?{/i}"
  "{i}'Please leave'?{/i}"
  "{i}'What do you want?'{/i}"
  "In the end, I just stood there in dumb silence, stewing in my own nervous sweat."
  "{i}What is he even doing here?{/i}"
  "If he was a robber, he picked the wrong house."
  "{w=0.2}.{w=0.2}.{w=0.2}."
  "{i}Do I.{w=0.2}.{w=0.2}.{w=0.2}. know him from somewhere?{/i}"
  "I squinted at his blurred shape, trying to replace the man's fuzzy edges with something more tangible."
  "{i}He looks--{/i}"
  "I stepped closer." 
  "The man waved the bat in alarm."
  show mike blurredangry at rightblur
  u "I-I told you not to move!"
  u "Ugh!"
  show mike blurredscared at rightblur
  "{w}Did he just shiver?"
  "..."
  "He was acting way more upset than me, {w}considering {i}he's{/i} the intruder in my house."
  "It might be a foolish thing to say, but he didn't seem dangerous at all."
  show mike blurredangry at rightblur
  u "Just go away, please...{w}{i} Please...{/i}"
  show mike blurredscared at rightblur
  "He continued mumbling to himself, gasping big gulps of panicked breaths."
  "Uh-oh. "
  y "Hey, uh. I think you're having a panic attack."
  y "Try breathing through your nose and out your mouth."
  show mike blurredshy at rightblur
  "..."
  "Damn..."
  "Did I actually just give breathing exercises to a tresspasser?"
  "I guess Sarah was right. {w}My kindness will be the death of me one day."
  "In any case, the stranger relaxed a good deal."
  "I gave him a small, unsure smile."
  y "You alright?"
  u "..."
  u "What{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2} What are you?"
  y "Um.. Sorry?"
  y "My name is Mike Jansen and you're in my house."
  y "Who are {i}you?{/i}"
  u "{w=0.2}.{w=0.2}.{w=0.2}."
  y "Nevermind."
  y "I think I lost my glasses somewhere."
  y "If you let me find them, I'm sure we can sort this out. You don't seem like a bad guy."
  "The man dropped the bat to his side and let out a long, forlorn sigh."
  u "Under the coffee table, probably."
  y "Thanks."
  "I fumbled around the floor, praying for dear life the stranger wouldn't attack me while I was vulnerable."
  "But he just stood there, shuffling his feet and mumbling to himself."
  "He wasn't very threatening, really. I'm sure the poor guy's just confused."
  "Also, there was something familiar about him. Something I couldn't quite put my finger on."
  "It might be his posture or even that red sweater he was wearing."
  "I could swear it looks {i}exactly{/i} like mine."
  u "Sorry for threatening you with a bat."
  y "Uh{w=0.2}.{w=0.2}.{w=0.2}. S'alright."
  u "If it makes any difference, I wasn't really going to hit you."
  "The shape of my glasses finally registed in my hand and I fished them out."
  u "I{w=0.2}.{w=0.2}.{w=0.2}. don't really think I can hurt anyone,{w} even in this situation."
  u "Sarah has always said---"
  "The world gained clarity as I put the pair of glasses over my eyes."
  scene bg room
  show mike sad at right 
  u "Someday kindness is going to kill me."
  y "...!"
  m "So, uh{w=0.2}.{w=0.2}.{w=0.2}."
  m "You can see me now."
  show mike unsure at right
  m "{i}{w=0.2}.{w=0.2}.{w=0.2}.Hi.{/i}"
  "The man waved lamely."
  show mike unsure2 at right
  "I stood there with my jaw agape, staring at him."
  "He{w=0.2}.{w=0.2}.{w=0.2}.  {w}was me."
  "...Existing as a separate being."
  "He had my face, hair, my posture--"
  "My... {i}sweater.{/i}"
  "No wonder that sweater looked liked mine, it {i}was{/i} mine!"
  show mike unsure3 at right 
  y "This is--"
  "{i}Just a dream. It's just a dream. That's it.{/i}"
  "{i}Calm down, don't lose your head. Relax.{/i}"
  "No matter how many times I said it though, the gravity of the situation refused to stick."
  "The room felt simultaneously constricting and vast, like being squeezed and let go again and again."
  "I felt like I was child again, lost in a crowd, blindly reaching for my mother's hand."
  "Only to realize in horror that the hand belonged to a stranger."
  "{w=0.5}.{w=0.5}.{w=0.5}."
  y "Aghk!"                           
  show mike worried2 at right
  m "O-Okay!"
  m "Now it's your turn not to panic, right?"
  show mike nervous at right
  m "Deep breaths!"
  "Was he some kind of clone? An apparition of my future? What?"
  "{i}What?!{/i}"
  "What exactly was he?"
  "I reached out to touch him, wanting to make sure he was real and not some figment of imagination."
  show mike annoyed at right
  "The other 'Mike' recoiled from my touch and pushed my arm away."
  m "Hey, this is weird for both of us."
  m "Don't make it worse by being grabby!"
  show mike sideunimpressed at right
  "He looked solid, so he couldn't be a ghost."
  "He could form separate thoughts from my own."
  "And he seemed aware that we were the same person."
  y "W-What are you?"
  y "Why do you have my face?"
  show mike annoyed at right
  m "Excuse me?"
  m "{i}Your{/i} face?"
  m "For your information, I was having a normal night in {i}my{/i} house when you came barging in here!"
  m "So why don't {i}you{/i} tell me what you're doing in {i}my{/i} living room?"
  "I opened my mouth to argue, but once I did, I realized I couldn't remember anything."
  "My last bits of memory consisted of a bowl of chips and late night T.V. shows."
  "Also, a pain at the back of my head..."
  y "I{w=0.2}.{w=0.2}.{w=0.2}."
  y "I can't remember--"
  show mike victory at right
  m "AHA!"
  m "See? That's what all fakes say! Case closed."
  y "{i}Fake?!{/i} Excuse me?"
  show mike annoyed at right
  m "You're some sort of anomaly. It's the only explanation."
  show mike sideunimpressed at right
  m "I don't remember doing anything special recently."
  m "If you have my memories, I'm sure you'll agree."
  show mike smirk at right
  m "You, on the other hand, lost a chunk of time from yours."
  m "So you are either the cause of everything or simply an effect."
  m "Ergo, an anomaly."
  y "Right."
  y "Then, if we're going there, I might as well say {i}you're{/i} lying about the state of your memories."
  y "Normality was disrupted with your presence, {w}hence I lost that track of time."
  y "The probability that {i}you{/i} are the cause {i}and{/i} effect of my sudden amnesia is very high."
  y "Therefore, you're the fake."
  show mike annoyed at right
  m "You can't prove that."
  y "Neither can you disprove it since we will have the same arguments--"
  show mike sad at right
  m "--And go around in circles. I see what you're getting at."
  show mike unsure3 at right
  y "..."
  m "..."
  show mike unsure at right
  m "It {i}is{/i} quite interesting, though."
  m "Isn't it?"
  call q1 from _call_q1
  show mike annoyed at right
  m "You make it sound like {i}I'm{/i} the copy here."
  y "Well, aren't you?"
  m "Don't start that thing again!"
  y "..."
  m "..."
  y "This is such a pain in the ass."
  show mike sad at right
  m "Don't I know it."
  "..."
  "What could have caused this?"
  "What kind of freak of nature would've sprouted another {i}me{/i}?"
  "Sure, I should be flattered or something, but I am hardly {i}clonable specimen{/i} material."
  "{i}*Sigh*{/i}"
  "At the very least, he didn't seem... {w}dangerous."
  "There was no animosity or aggression coming from him."
  "I didn't feel any ill will towards him either."
  "But it {i}was{/i} strange how we had the same small scar on the chin."
  "And even the same pock marks from teenage acne."
  "I touched my own face on a sudden impulse."
  "{i}I'm still me{w=0.2}.{w=0.2}.{w=0.2}.{/i}"
  "...Right?"
  play sound "sfx/door.ogg"
  stop music fadeout 2.0
  "Just then, we heard a door softly opening from upstairs."
  show mike scared at right
  show mike worried at right
  m "Oh no! Sarah!"
  y "Sarah!"
  show mike worried2 at right
  play music "sfx/earlyend.ogg"
  m "I knew Sarah heard that noise a while ago!"
  m "Quick, find somewhere to hide!"
  m "I'll try to distract Sarah while you crawl out the front door!"
  y "WHAT?"
  y "Wait a minute."
  y "You're getting rid of me!"
  show mike annoyed at right
  m "No, I'm not, okay?!"
  m "We just can't risk having two Mikes in the house. You know that."
  y "Then why don't {i}you{/i} leave?"
  show mike regret at right
  m "Are you kidding?"
  m "You look like a trainwreck!"
  "He was right. I was filthy."
  "How did that happen?"
  m "Look."
  m "We'll get it all sorted out tomorrow."
  m "Who knows, maybe your missing memories might even come back."
  y "But you're throwing me out of my house!"
  show mike sad at right
  m "I'm not throwing you out!"
  m "This is just a temporary arrangement."
  m "Let me deal with Sarah tonight, and tomorrow, we'll sort out this mess."
  m "Just leave for now, okay?"
  call earlyend from _call_earlyend
  return

  label cont:
  scene bg room
  show mike sad at right
  "I stand there with a heavy feeling in my stomach."
  "His suggestion made sense, but my feet refused to move."
  "Why should {i}I{/i} hide?"
  "Why should I scurry away from {i}my{/i} girlfriend in {i}my{/i} house?"
  "It wasn't right."
  "Faint trickles of anger scratched at my chest."
  y "No. {w=0.2}Way."
  show mike worried at right
  m "What?"
  y "I'm not leaving."
  show mike annoyed at right
  m "Come on, man! Don't be difficult!"
  show mike worried2 at right
  m "If Sarah sees this... {w}{i}this{/i}..."
  show mike freaked at right
  m "It will not end well for either of us!"
  y "But if there's anyone out there who can help us it's--"
  play sound "sfx/stairs.ogg"
  stop music

  show mike worried2 at right
  m "SHH!"
  show mike sideworried2 at right

  ####################SARAH ARRIVES################################

  s "Mikey. It's getting late. Aren't you coming up?"
  "Her voice called from the stairs."
  "The living room was dark, and she probably couldn't see {i}'us'{/i} in the dim light."
  "We held our breaths tight in our throats."
  m "Uhh{w=0.2}.{w=0.2}.{w=0.2}."
  m "I--I got distracted."
  show sarah normal at left with dissolve
  "Sarah walked towards us, a nonchalant look on her face."
  show sarah confused at left
  s "Is someone there? It's pretty late for visitors."
  m "Uh{w=0.2}.{w=0.2}.{w=0.2}."
  show sarah suspicious at left
  s "Is that your broth--"
  show sarah shock at left
  play music "sfx/sarah.ogg"
  "Mike stole a glance at me."
  show sarah comicshock at left
  m "Listen...{w} Sarah."
  show sarah wtf at left
  y "Please don't panic."
  #Sarah stares in shock
  s "...!"
  s "Oh."
  show sarah ohshit at left
  s "My."
  show mike cringe at right
  show sarah holyshit at left
  with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
  s "{i}GOD!{/i}" 
  show sarah ohshit at left
  show mike sideworried at right
  m "Sarah, calm down."
  #Sarah stares at main character then Mike then back at character again."
  s "THIS IS-"
  show sarah holyshit at left
  show mike cringe at right
  with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
  s "WHAT THE FUCK?!"
  show sarah ohshit at left
  show mike shy at right
  y "Okay{w=0.2}.{w=0.2}.{w=0.2}."
  y "I-I know this looks {i}sorta{/i} bad but--"
  show sarah holyshit at left
  s "SORTA BAD?"
  show sarah ohshit at left
  s "Mike, I'm staring at two of you!"
  show sarah fuckthat at left
  s "I think we've crossed the threshold of {i}'sorta bad'{/i} a {i}long{/i} time ago!"
  show mike sidesad at right
  show sarah ohplease at left
  m "..."
  show sarah ohplease2 at left
  s "This is a trick, isn't it?{w} With some mirrors and shit?"
  show mike cringe at right
  y "It's not a prank, Sarah."
  show mike shy at right
  show sarah ohshit2 at left
  m "This is really happening."
  show sarah ohshit at left
  show sarah ohshit2 at left
  show sarah ohshit at left
  y "And we don't really know what to do."
  show sarah ugh at left
  s "Stop!"
  show mike cringe at right
  show sarah pain at left
  s "Stop talking!"
  show sarah pain2 at left
  s "Watching both of you talk at the same time is giving me vertigo!"
  show mike unsure4 at right
  show sarah goofypain at left
  m "Uhm. Deep breaths?"
  s "I{w=0.2}.{w=0.2}.{w=0.2}."
  show sarah pain2 at left
  s "I think I need to lie down."
  show sarah goofypain at left
  show mike unsure2 at right
  "{w=0.2}.{w=0.2}.{w=0.2}."
  s "Excuse me for a bit."
  hide sarah goofypain with dissolve
  ####################################SARAH LEAVES######################
  y "Well!"
  y "That went better than expected!"
  show mike annoyed2 at right
  m "If by that you mean 'my girlfriend is ready to pop a stress baby' then, yeah, sure."
  show mike annoyed at right
  m "I told you this was a bad idea!"
  call q2 from _call_q2
  show mike sad at right
  m "{i}*sigh*{/i} Guess we better just deal with it."
  ###################################Sarah comes back#########################
  show mike unsure2 at right
  scene black
  scene bg room
  show mike unsure2 at right
  show sarah suspicious at left
  "Mike and I stood in silence, waiting for Sarah to come back."
  "She joined us a couple of minutes later, her face grim, but composed."
  "It gave me a feeling of normalcy during this bizzare situation."
  s "Alright, boys. I'm a lot calmer now."
  s "Now, first order of business."
  show mike shy at right
  show sarah dubious at left
  s "What the flying fuck?"
  "{w=0.2}.{w=0.2}.{w=0.2}."
  show sarah sidedubious at left
  m "I have no idea."
  show sarah sidedubious2 at left
  s "Start at the beginning, then."
  show mike unsure2 at right
  show sarah sidenormalcross at left
  m "Well{w=0.2}.{w=0.2}.{w=0.2}."
  m "I heard a noise and I checked it out."
  m "I found somebody stumbling around in the living room."
  m "I panicked and took the bat. B-But I just wanted to scare off the guy."
  show mike unsure3 at right
  m "And then,{w} I saw {i}him{/i}."
  m "With my face on."
  show sarah dubious at left
  show mike freaked at right
  m "I thought I was losing it!"
  show mike shy at right
  show sarah sidenormalcross at left
  m "But he was making his way upstairs, so I had to confront him somehow."
  m "To be honest, I thought of grabbing a crucifix or something."
  show sarah sidedubious at left
  s "Cute."
  show mike unsure3 at right
  show sarah normalcross at left
  y "I don't remember any of that."
  y "I just woke up here with an aching head."
  show mike unsure2 at right
  s "What's the last thing you do remember?"
  #########################QUESTIONNAIRE########################
  ############### Q3 ###
  call q3 from _call_q3
  show mike unsure3 at right
  show sarah normalcross at left
  y "Next thing I know, I'm in the living room and this guy was waving a bat at my face."
  show mike smirk at right
  show sarah sidenormalcross at left
  m "No way!"
  m "He came in here dragging himself like a drunk."
  m "...And then he tripped on that stupid carpet."
  ################# Q4 ###
  call q4 from _call_q4
  show mike normalsad at right
  show sarah dubious2 at left
  s "So{w=0.2}.{w=0.2}.{w=0.2}."
  s "I have a feeling there's another issue here though."
  m "..."
  s "Are you guys trying to out-real each other or what?"
  show mike unsure2 at right
  show sarah sidedubious at left
  y "Well{w=0.2}.{w=0.2}.{w=0.2}."
  m "There {i}can't{/i} be two Mike Jansens, can there?"
  show mike shy at right
  show sarah normalcross at left
  y "Maybe you could help us figure it out."
  show sarah dubious2 at left
  s "Huh?"
  s "Decide which one of you is real?"
  y "Yeah."
  s "Like how, exactly?"
  show mike normalsad at right
  show sarah normalcross at left
  y "Oh, {w}I don't know. {w}Ask us some personal questions or whatever."
  show mike unsure2 at right
  m "Hey. Yeah! Why not?"
  show mike unsure3 at right
  m "Maybe one of us will slip up."
  show mike unsure2 at right
  show sarah thinking at left
  s "Right."
  s "Because you want to treat this like a fucking trivia game."
  show mike shy at right
  show sarah angrythinking at left
  "{w=0.2}.{w=0.2}.{w=0.2}."
  show sarah dubious at left
  show mike unsure2 at right
  show sarah determined at left
  s "Look, guys.{w} I don't think that's gonna work."
  show mike regret2 at right
  show sarah suspicious at left
  s "You can't just decide the {i}'realness'{/i} of somebody in one night of 20 questions."
  show sarah angrythinking at left
  s "We have to find another way."
  show mike sad at right
  y "Like what?"
  show sarah ohplease at left
  s "Blood sampling? {w}DNA Test?"
  s "{i}An exorcism?{/i}"
  show mike shy at right
  show sarah pain2 at left
  s "I don't fucking know!"
  show sarah ohplease2 at left
  s "Just, please!"
  show sarah pain at left
  s "Don't make me choose between the two of you!"
  show mike regret at right
  show sarah goofypain at left
  y "Sarah, I'm--{w}we're aware this is unfair."
  show sarah ohplease at left
  y "But if there is {i}one{/i} person who can help us, it's you."
  show mike unsure2 at right
  show sarah dubious2 at left
  s "Mikey, you do know I love you, right? We've been together a long time."
  show sarah suspicious at left
  s "I know your bowel patterns and your unhealthy fanboy obssession with Jason Statham."
  show mike shy at right
  m "Err{w=0.2}.{w=0.2}.{w=0.2}."
  show mike unsure2 at right
  show sarah pain at left
  s "But I don't think literally {i}anyone{/i} is cut out for this shit."
  show sarah concerned at left
  show mike shy at right
  show sarah angrythinking at left
  "{w=0.2}.{w=0.2}.{w=0.2}."
  show sarah sidedubious2 at left
  s "Why don't we just call your mother?"
  show sarah smug2 at left
  show mike sideworried2 at right
  show mike worried2 at right
  with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)             
  b "{i}NO!{/i}"
  show sarah amused at left
  s "Oho! Even your reactions are the same."
  show mike worried at right
  show sarah smug2 at left
  s "Impressive."
  show mike shy at right
  show sarah comicshock at left
  y "Baby Bunny, please?"
  show sarah blush at left
  y "{i}Pleeeaase,{/i} help Papa Bunny out?"
  show sarah bigblush at left
  s "S-stop!"
  s "D-Didn't I tell you that nickname is only {i}between the two of us{/i}?!"
  show mike unsure4 at right
  show sarah bigblush2 at left
  m "Err... technically, it's still just me so..."
  show sarah freaked at left
  s "Oh my god."
  s "That is so fucking creepy."
  show mike shy at right
  show sarah concerned at left
  s "One thing's for sure. We do have to fix this."
  show sarah goofypain at left
  s "It's just too damn weird."
  show mike normalsad at right
  show sarah suspicious at left
  y "So will you help us?"
  show sarah goofypain at left
  "Sarah sighed and shook her head."
  s "I don't think I get a say either way."
  m "It's at least worth a shot."
  show sarah angrythinking at left
  s "Wait."
  show sarah determined at left

  s "After this is over, {w}what are we going to do with the supposed imposter?"
  show sarah sidedubious2 at left
  show mike sidesad at right
  s "Have you guys thought about that little gem?"
  show mike shy at right
  show sarah sidedubious at left
  m "I-I'm sure we'll figure something out afterwards."
  ##########################  Q5 ###
  call q5 from _call_q5
  show mike normal at right
  show sarah exasperated at left

  s "*sighs* Okay. Whatever. Personal questions it is."

  show sarah angrythinking at left
  m "..."
  y "..."
  show sarah sidedubious2 at left
  show mike sidenormal at right
  s "Anniversary?"
  show sarah sidedubious at left
  m "February 26, 2009."
  ########################### Q6 ###
  call q6 from _call_q6
  show mike normal at right
  show sarah smug3 at left
  s "Too easy!"
  show sarah sidenormalcross at left
  show mike sidenormal at right
  s "Brother's name?"
  show mike happy at right
  m "Myles Jordan Jansen."
  m "He hates it!"
  ############################ Q7 ###
  call q7 from _call_q7
  show sarah pain2 at left
  show mike happy at right
  s "You guys are being {i}very{/i} mature."
  show mike normal at right
  show sarah angrythinking at left
  s "Anyway{w=0.2}.{w=0.2}.{w=0.2}."
  show sarah sidedubious at left
  s "Favorite animal?"
  show sarah pain2 at left
  s "I'm starting to sound like the worst dating website in history."
  show mike happy at right
  show sarah sidenormalcross at left
  m "Dogs!"
  ############################# Q8 ###
  call q8 from _call_q8
  show mike normal at right
  show sarah determined at left
  s "Okay. That's it."
  show sarah pain2 at left
  s "I don't think this is working."
  show mike annoyed at right
  show sarah sidenormalcross at left
  m "Hey, wait!" 
  show sarah sidedubious2 at left
  m "Let's take turns! What if he's just leeching off my answers?"
  show sarah normalcross at left
  y "I resent that!"
  show mike normal at right
  show sarah angrythinking at left
  s "Alright, alright."
  show sarah smug3 at left
  s "Here we go."
  show sarah amused at left
  s "Tell me a secret you {i}haven't{/i} told me before."
  show sarah smug2 at left
  show mike unsure4 at right
  ################################## Q9 ###
  call q9 from _call_q9
  show sarah sideamused at left
  s "Same question?"
  show mike nervous2 at right
  m "Uhh.."
  m "Sarah, {w}I love you but--"
  show mike freaked at right
  m "Thatlasttunacasseroleyoucookedsuckedlikeballs"
  ################################## Q10 ####
  call q10 from _call_q10
  show sarah amused2 at left
  s "Ah!"
  menu:
    "stop here":
      pass
  show mike cringe at right
  with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
  show sarah verypissed at left
  s "{i}So it takes a clone of you to pop up before you admit to it, huh?{/i}"
  show mike worried2 at right
  b "{w=0.2}.{w=0.2}.{w=0.2}.but."
  show mike freaked at right
  with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
  s "{i}Next question!{/i}"
  show sarah pissed at left
  s "Now we're getting somewhere."
  s "At least one of you has to be telling the truth."
  b "{i}*whine*{/i}"
  s "So, Mike. What's wrong with the casserole?"
  show mike cringe at right
  ################################## Q11 ####
  call q11 from _call_q11
  show sarah pissed at left
  s "Anything else? You were on a roll there."
  show mike nervous at right
  show sarah pissed2 at left
  m "Uh{w=0.2}.{w=0.2}.{w=0.2}. {w}That's all."
  #show mike apologetic
  m "O-On the other hand! {w}You make great pizzalets!"
  ################################## Q12 ####
  call q12 from _call_q12
  s "In short..."
  show mike nervous2 at right
  show sarah verypissed at left
  s "You like {i}none{/i} of my cooking, you lying ass."
  m "..."
  show mike nervous at right
  m "That's not--"
  show mike worried at right
  y "Nice going, {i}Mike{/i}!"
  y "At this point, she'll throw both of us out!"
  show sarah pissed at left
  s "Alright then! {w}More questions!"
  show sarah pissed2 at left
  s "Do you have a crush on our neighbor?"
  show mike scared at right
  y "What? {w}Who?"
  show sarah pissed at left
  s "Paris Beaufort, the model who sunbathes naked on Sundays."
  show sarah pissed2 at left
  y "What?{w} That's--"
  show mike nervous2 at right
  m "S-sarah?? {w}What even are these questions??"
  s "I'm just making full use of this situation, Mikey.{w} Wouldn't you?"
  s "Besides!"
  show sarah scary at left
  s "I'm having fun."
  show mike freaked at right
  show sarah scary2 at left
  m "..."
  ################################## Q13 ####
  call q13 from _call_q13
  show mike nervous at right
  show sarah pissed2 at left
  m "Err{w=0.2}.{w=0.2}.{w=0.2}. {w}She's..."
  m "She's pretty, okay?"
  m "You both are."
  show mike unsure4 at right
  show sarah hmp at left
  m "But you're my soulmate."
  s "Hmp."
  ################################## Q14 ####
  call q14 from _call_q14
  show sarah smug at left
  show mike shy at right
  s "Well, this has been {i}very{/i} educational."
  show sarah annoyed at left
  s "Anything else you want to tell me?"
  ################################## Q15 ####
  call q15 from _call_q15
  show mike regret at right
  show sarah sidenormalcross at left
  m "Anyway."
  m "Going back to the dilemma at hand."
  show mike regret2 at right
  show sarah pain at left
  s "We didn't really make any progress, if you ask me."
  show sarah goofypain at left
  s "I still don't know which one of you is which."
  show sarah pain2 at left
  s "Why don't we just flip a damn coin?"
  show sarah pain2 at left
  ################################## Q16 ####
  call q16 from _call_q16
  show mike sad at right
  show sarah sideconcerned at left
  m "I hardly think that's a good idea though."
  s "Of course not."
  s "But at this point, I'm really at a loss."
  show mike regret2 at right
  show sarah concerned at left
  "{w=0.5}.{w=0.5}.{w=0.5}."
  show mike normalsad at right
  show sarah exasperated at left
  m "We still have to decide, though."
  s "{i}*Sigh*{/i}"
  show sarah sidedubious2 at left
  s "Fine."
  show sarah sidedubious at left
  s "If you are the real Mike, what do you suggest we do with the imposter?"
  show mike shy at right
  m "That's difficult."
  show mike unsure2 at right
  m "Uhm,{w} if I'm the real Mike, then I should stay Mike, right?"
  m "The other one has to leave.{w} Go out in the world and find their own identity. {w}The world is big anyway."
  ################################## Q17 ####
  call q17 from _call_q17
  show sarah normalcross at left
  s "{i}Are{/i} you the real Mike?"
  show mike unsure3 at right
  show sarah dubious at left
  y "Of course I am!"
  show mike shy at right
  show sarah sidedubious at left
  m "Is this still one of your weird question thingies?"
  s "Just answer."
  ################################## Q18 ####
  call q18 from _call_q18
  show sarah sidedubious at left
  s "How about you? Are you the real Mike?"
  show mike unsure2 at right
  m "I am."
  show sarah sidedubious2 at left
  s "Prove it then. {w}Convince me."
  show mike shy at right
  show sarah sidedubious at left
  m "Uhm... Okay... {w}Bit awkward..."
  show mike unsure2 at right
  show sarah sidenormalcross at left
  m "But I {i}am{/i} Mike. Heart and mind."
  m "It's the only thing I know, really. I wouldn't know what else to say."
  s "{w=0.2}.{w=0.2}.{w=0.2}."
  show mike unsure3 at right
  show sarah normalcross at left
  ################################## Q19 ####
  call q19 from _call_q19
  show sarah dubious2 at left
  s "What are you going to do if I ever say you're the fake?"
  ################################## Q20 ####
  call q20 from _call_q20
  s "{w=0.2}.{w=0.2}.{w=0.2}."
  show sarah angrythinking at left
  s "Alright. I think I just need to ask one last question."
  show sarah normalcross at left
      
  label endings:
      if truth >=6 and agree >=6:
          call deadend from _call_deadend
      elif truth >=6 and disagree >=6:
          call truend from _call_truend
      elif lie >=6 and agree >=6:
          call badend from _call_badend
      elif lie >=6 and disagree >=6:
          call bonusend from _call_bonusend
      else:
          call deadend from _call_deadend_1     
  return
  jump start


      
