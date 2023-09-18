init:
  $Q1Flag = 0
  $Q2Flag = 0
  $KnifeFlag = 0

# The game starts here.
label start:
    scene bg black
    jump lbl_story_start
    
    #testing stuff
    show bg attic
    show fi angry wj       at rightF
    show el angry nj     at leftE
    e "1You've created a new Ren'Py game."

    f "2Once you add a story, pictures, and music, you can release it to the world!"
    show el angry nj     at leftE
    show fi angry wj       at rightF
    e "3You've created a new Ren'Py game."
    show el neutral wj   at leftE
    show fi apologetic nj  at rightF
    menu:
      "What will you do?"
      "4aOption 1":
        e "4a1Once you add a story, pictures, and music, you can release it to the world!"
        f "4a2You've created a new Ren'Py game."
      "4bOption 2":
        f "4b1Once you add a story, pictures, and music, you can release it to the world!"
        e "4b2You've created a new Ren'Py game."


    show el neutral nj   at leftE
    show fi apologetic wj  at rightF
    f "5Once you add a story, pictures, and music, you can release it to the world!"
    show el sad wj       at leftE
    show fi crazy nj       at rightF
    e "6You've created a new Ren'Py game."
    show el sad nj       at leftE
    show fi crazy wj       at rightF

    f "7Once you add a story, pictures, and music, you can release it to the world!"
    show el smiling wj   at leftE
    show fi default nj     at rightF
    e "8You've created a new Ren'Py game."
    show el smiling nj   at leftE
    show fi default wj     at rightF
    menu:
      " "
      "9aOption 1":
        f "9a1Once you add a story, pictures, and music, you can release it to the world!"
        e "9a2You've created a new Ren'Py game."
      "9bOption 2":
        f "9b1Once you add a story, pictures, and music, you can release it to the world!"
        e "9b2You've created a new Ren'Py game."

    show el surprised wj at leftE
    show fi nervous nj     at rightF
    f "10Once you add a story, pictures, and music, you can release it to the world!"
    show el surprised nj at leftE
    show fi nervous wj     at rightF
    e "11You've created a new Ren'Py game."
    show el terrified wj at leftE
    show fi sad nj         at rightF
    f "12You've created a new Ren'Py game."
    show el terrified nj at leftE
    show fi sad wj         at rightF
    e "13You've created a new Ren'Py game."
    show el neutral wj   at leftE
    show fi serious nj     at rightF
    f "14You've created a new Ren'Py game."
    show el neutral nj   at leftE
    show fi serious wj     at rightF
    e "15You've created a new Ren'Py game."
    show el neutral wj   at leftE
    show fi smiling nj     at rightF
    f "16You've created a new Ren'Py game."
    show el neutral nj   at leftE
    show fi smiling wj     at rightF
    e "17You've created a new Ren'Py game."
    show el neutral wj   at leftE
    show fi surprised nj   at rightF
    f "18You've created a new Ren'Py game."
    show el neutral nj   at leftE
    show fi surprised wj   at rightF
    e "19You've created a new Ren'Py game."
    show fi surprised wj anim at rightF

    e "The end!"

    return

label lbl_story_start:
  $Q1Flag = 0
  $Q2Flag = 0
  $KnifeFlag = 0

  "Just keep smiling and sadness will fade..."

  "Just keep smiling and hurt is delayed..."

  "Just keep smiling and begin to believe..."

  "Happiness is not something so hard to achieve..."

  #---
  scene bg sky clouds2 with dissolve
  "Eloise lay dormant within the hazy confines between sleep and consciousness. It was a place where all lines became blurred, where reality and fiction meshed together seamlessly and yet it always managed to be so comforting."

  "It was surreal, but peaceful, devoid of both nightmares and the stress of day-to-day life."

  "At the same time, the space between dreams and reality was bereft by comparison to either. An endless limbo where all Eloise could do was walk forward. She didn't know why she kept on walking but with every step feeling lighter than the last, there was nothing holding her back."

  "As much freedom as the empty space permitted her, Eloise slowly felt the endless journey to be getting rather dulled. Her surroundings lay just as bereft as before, but at least she could stop - so she felt, anyway."

  "In the day-to-day drudgery of life, she often didn't get the chance to stop. To observe the world around her."

  "Pausing brought the revelation to Eloise that she was entirely alone. It didn't seem so bad - there was literally nothing in sight - yet the loneliness still disturbed her."

  e "Maybe it's time to wake up?"

  "Her voice sounded strange to her in the emptiness, alien even. It's really the first thing she'd heard in a while beyond her own rhythmic footsteps."

  "She did get a response though, a sort of echo in the air, a voice in her mind that's just too quiet to understand and yet permeating the void that lay before her."

  e "What is that? Hello?"

  "Eloise continued her endless walk, attempting to catch the elusive voice.  Surprisingly, it seemed to get closer. It was not a voice, but a cry."

  "Then she saw the source, a young child sobbing away. She couldn't tell their gender, but when the child noticed her, the child stopped."

  e "Why?"

  "The child gave Eloise no chance to question the situation. Their face brightened up and the child hastily wiped tear after tear away before running in leaps and bounds towards Eloise, a smile beaming from their features."

  "With that, Eloise lost the rest of her encounter to the depths of her mind, leaving the edge of her own dreamscape and falling back into the void between and then to reality."

  #---
  scene bg sky clouds with dissolve

  "Eloise woke up, strapped in to the front seat of her mother's car. Her mother was handling the wheel in the same fashion she always did."

  "Eloise yawned, and began to stretch. Her body was stiff and her muscles ached. Her neck felt like it'd been snapped with a mallet."

  "Clearly she hadn't slept in a very good position. It took her a few moments, but she remembered she was on the way to school to attend a camping trip with her club members."
  
  show el neutral nj at rightE
  e "Are we almost there?"

  "Her mother spoke up in her usual, cheery nature, yet never removed her eyes from the road."

  m "About five more minutes, honey. Are you excited?"

  "Eloise tried to stretch some more, wincing as she rolled her shoulders and stretched her legs as far as she could in the car. Her response came as decidedly deadpan."

  e "Not in the slightest."

  "It wasn't exactly a lie, though it wasn't entirely true, either. Eloise was not one for outings, much less camping, though she did enjoy the company of friends."

  "All the same it was all too easy for her to complain about what she didn't like rather than focus on what she did. Her sigh was about as depressing as could be."

  e "This is stupid. I can't believe I'm actually going. What am I going to do out in the middle of nowhere?"

  "She really didn't care for the scenery but her friends nagged her endlessly and she figured it would be bearable among amicable company."

  m "Oh honey, it's not that bad."

  "Eloise's mother was a master at holding a smile and making everything sound as though it had been coated in a dozen layers of chocolate and ice cream."

  "The reality was that nothing had been, but somehow her mother managed to convey such a ridiculous notion with an overly optimistic tone of voice."

  m "It should be a great experience, and the fresh air will be a lovely change from what you're used to. Think of all the things you'll be trying for the first time. It will be quite educational."

  "Of course, they were all things Eloise didn't care to try in the first place. She slumped back down into her seat."

  e "I'm going to be stuck in the middle of nowhere surrounded by nerds for days."

  "Even with her mother's lips still smiling, Eloise did take note that her eyes fell to a frown for a brief moment."

  "If Eloise were to be honest, it would also be more correct to say that the other kids weren't exactly nerds - at least, not all of them."

  "In a school that loved its sports programmes, the more bookish types were just a natural rarity. There were only about ten book club members in all."

  m "I'm happy you decided to spend more time outside. It's a nice change of pace and it will work wonders for your complexion."

  "Her mother's features dropped to concern in an instant."

  m "Though I am worried with how messy you are. I hope you'll be alright taking care of everything on your own..."

  e "Mum."

  m "...and your clothes and all your accessories, you're not good at keeping track of your things either. You're losing things all the time. Just last week you lost those new earrings."

  e "Mum."

  m "There was just the other day too where-"

  "Finally Eloise took the initiative to push herself back up in her chair and give her vocal cords a workout."

  e "Mum!"

  "Her mother was unfazed, but she did steer back out of hostile territory."

  m "Oh sorry, deary. It's just so easy to worry knowing that my little girl is all grown up and out on her own for a few days."

  "Eloise remained silent - a notion her mother soon followed - and waited the rest of the car ride out."

  "Before long they were at the school grounds. She'd never once been here so early in the morning. There was little to be seen, just a mere five students gathering in the morning frost while a large, magenta bus stood on standby."
  
  #scene friends?
  
  "Eloise quickly scans over the gathering, feeling more than a little disheartened by their alienation to her. Thankfully, it was short lived, and she soon caught sight of a familiar face. It was her best friend, Tag."

  "Eloise was preparing to leave the car when her mother caught her by the hand."

  m "Be careful with your luggage, remember to check everything is there on a regular basis, okay?"

  "Eloise tried tugging her arm away."

  e "Alright, mum, I get it."

  m "Don't forget to brush your teeth twice a day."

  "Try as she might to escape, Eloise's mother had an iron grip when she wanted to."

  e "Alright, I will."

  m "Remember to-"

  e "Mum!"

  "Her mother finally let go."

  m "Oh sorry, honey. Here, let me open the trunk."

  "Eloise wasted no time hauling her bags out of the trunk once it was open. She was eager to get away from the clinging hands of her mother now, especially knowing she can run straight off to tag to have her mother leave her alone for good."
  
  "All that said, she can't hide the genuine excitement leaping from her face. Her mother gives a simple sigh as she receives but a quick peck on the cheek and watches her daughter jogging away to the other campers."

  e "Bye, mum! See you in a week!"

  m "Ah... bye, honey."

  "Eloise was already off and distracted far too soon to notice the look of sadness in her mother's eyes."

  m "She really is still just a child."

  "For how early it was in the morning, Eloise was positively booming with enthusiasm. It was almost as if she'd entirely forgotten about the whole camping trip but for the sight of her friend."

  e "Tag! Hey!"

  a "Hey, looking well there, sister. Get enough sleep last night?"

  "Eloise struck as triumphant a pose as she could, complete with a smug smile. Really she looked anything but - the bags under her eyes couldn't be more evident."

  e "Sleep is for the weak."

  "Tag simply gave a dirty look."

  a "Says the person who fell asleep in front of the monitor at three in the morning."

  "Eloise's triumphant disposition crumbled like a biscuit in milk."

  e "It's not my fault. The movie was very calming."

  a "You mean dull and tasteless?"

  e "No, I said calming."

  a "That's what I said. Dull and tasteless."

  "Tag was the sort who could really put ants in your pants if she wanted to."

  "Eloise put her foot down with a level of aggression."

  e "Appreciate the indie film, Tag. That movie is a work of art."

  "Tag simply rocked herself back into a more casual position - hands in pockets, leaning posture, the works."

  a "It also comes with the added side effect of drowsiness."

  "Eloise threw her arms up in defeat and took another look around the school grounds."

  e "Hmph. So where are the boys?"

  "The boys in question would make up the other part of Eloise's circle of close friends. There were five of them who'd met and subsequently become friends early in her freshman year."

  a "Well, Ollie refused to come out. Says that nature terrifies him. Kid's probably off to France with his family again. Don't worry, I'll give it to that wimp when I see him next."

  e "Why are you two dating again?"

  "Tag simply grins as she stands confidently."

  a "Hah, there's nothing but open feelings in our relationship."

  e "So the other guys?"

  "Tag presses a hand to her head in thought."

  a "Yeah, well, Kel's probably just sleeping in, that slacker. I should totally do something while he's sleeping, maybe that way he'll remember to use an alarm clock for once."

  e "You know, he probably does use an alarm. The snooze button is a deadly adversary."

  a "Doesn't matter, I'm still raiding his tent while he sleeps."

  k "Oho, is that so?"

  "Tag jumps like a cat in water."

  e "Well look who decided to show up."

  "Kelsey gives us both a frown, with particular emphasis to directing it at Tag."

  k "I'm on time, damnit. Stop acting like I sleep all day. I'm not some lazy bum."

  "Eloise shrugs casually."

  e "Maybe not, but you're damn well close."

  "Kelsey narrows his eyes but says nothing."

  a "Hey, Kel, so you aren't with Finn?"

  "Kelsey shrugs and looks around the school yard."

  k "Nah, he said he's got something he needs to do before heading over. He never said how long he'd be."

  a "This early in the morning? Must suck to be him. Sure is unusual for ol' Finn the Thin to be late."

  "Eloise facepalmed. Kelsey made various gagging motions at Finn's title."

  e "Finn the Thin? Tag, that's just bad. You don't have to give everyone a stupid name, you know. I'll agree it's strange, though."

  "Kelsey scratched his head for a few moments as silence fell upon the group."

  k "Why?"

  a "Why what?"

  k "Why's it strange that he's late?"

  "Tag was not the sort to be serious on a regular basis, but for once she seemed genuinely honest in her assertions."

  a "Finn's never late."

  e "Heck, he's usually waking you up in the morning, Kel."

  "Kelsey threw his arms out."

  k "What, that's it? You guys are acting like it's some foul omen or something and that's all? Let's be real while we're at it, you really think I never get up 'til it's past noon?"

  "Tag gave an overly dramatic shrug alongside a lopsided - and completely smug - smile."

  a "You can't blame us when all you show is your bad side."

  k "Gee, thanks, Tag. Come on, back me up, Lois."

  e "You want it brutal or sugar-coated?"

  "Kelsey raised a brow quizzically."

  k "The latter?"

  e "Dreadfully lazy. You'd already have your masters degree in the art of couch potatoism if it weren't for your basketball practice... Which you skip most of the time."

  "Kelsey quickly established quite the blush."

  k "That's not sugarcoated!"

  "Eloise waved away his accusation"

  e "What can I say? That's as nice as I can get."

  "Without warning, Kelsey leant in and pinched Eloise's cheek."

  e "Ow! Hey, seriously?!"

  "Tag could barely control her chuckling."

  a "There certainly is nothing greater than another's suffering."

  k "You crazy sadist."

  "WIth that, Kelsey grabbed Tag by the nose and gave it a firm squeeze. Her proclamations of protest were anything but threatening with her nose clinched so tight."

  a "Hey, come on! You're going to ruin my perfect, dainty little nose."

  k "It was ruined the moment you were born."

  e "Damn, Tag. Too much."

  "Just as Tag looked about ready to pounce on Kelsey, Finn announced his presence."
  show fi apologetic wj at leftF
  f "Hey guys. Apologies for my late arrival. Family business."

  "Kelsey just about fell to his knees and threw his arms up in salvation."

  k "My trusty pal is here, finally! These two are relentless today. Tell them I'm not a good-for-nothing."

  a "Hey, it's the Finnster."

  "The group sighed simultaneously."

  e "Hey Finn. What has you so late? Nothing bad, I hope."

  "Finn looked about the same as ever, and gave a deadpan delivery that was fairly common to him."

  f "Nothing important. Just some minor miscalculations back at the estate that needed attending to."

  e "Well, it's good that nothing bad's come up. Alright guys, we're all here. Should we get on the bus? It's already five past seven."

  "Tag literally jumped into the conversation. She was fond of the centre stage."
  #scene group
  a "Hey, let's grab some seats near the back."

  e "Yeah, no problem. Let's just get our luggage together."

  "As everyone moved to gather their luggage, Kelsey seemed to be a bit distracted staring at the bus."

  k "Can someone please explain to me... who thought a pink bus was a good idea?"

  a "Dude, it's magenta."

  k "It's tacky."

  a "It's fabulous. Come on, it suits you perfectly."

  "Eloise sighed."

  e "I just hope no-one I know sees me in it... but I guess that's too late, huh?"

  "Picking up her luggage, Eloise certainly noticed something she didn't before. An ache ran through her shoulders as she hauled the bags up. Without the excitement and adrenaline of earlier, it became painfully obvious how over packed her bags were."

  e "Damn is this heavy... Did you pack the whole wardrobe, mum?"

  "She lifted one bag up above her head, inspecting it carefully as though she could determine the contents through that alone. She quickly realised her arms were weakening, and let out a short yelp as the bag collapsed onto her face."

  "If she wasn't muffled by the bag for the following moment, her string of curses would've surely caught the ear of everyone in the area."

  "Finn tapped Kelsey's shoulder and motioned over to Eloise."

  f "Eloise, you think maybe you need a hand?"

  "Kelsey lifted the one bag off her face effortlessly while Finn grabbed hold of her other bag."

  k "...and you guys keep calling me the wimp."

  "Eloise massaged her face firmly as she watched her two friends handle the bags. Even if Kelsey slacked off he was still an athlete, she thought."

  "Kelsey got one bag on board as Finn passed him the other."

  k "There we go. All done."

  "Eloise rubbed one arm awkwardly while she shuffled over towards the bus."

  e "Thanks."

  k "What, no apology for earlier?"

  e "Still a long way to go to earn that one."

  "Kelsey stuck his tongue out."

  k "Meanie."

  scene bg black with fade
  "It didn't take long for everyone to board the bus, or for Eloise to drift off to sleep yet again. True to Tag's word, Eloise opened a movie on her laptop and was out like a light before anyone could even comment."
  
  "She didn't even make the effort to shoo everyone away to hide her fatigue prior, just straight out like a light until they arrived. Occasionally she'd stir to the chatter of the other passengers, or the rumbling of the bus on bumpier roads."

  "As much as the others would rag on her for the nap, they still knew to let her have her sleep. This made it particularly difficult for Tag who can hardly contain her boisterous laughter most of the time."

  "After a long trip, and a good nap and a half for Eloise, the bus arrived at the so-called camp site. Really it was a small mountain resort that had been booked by the club advisor, Mr. Watt."
  
  #scene resort
  "The resort's programme actually holds no relevance to the book club, but it would seem Mr. Watt had managed to pull a few strings to get them there anyway - after all, it was the club's budget, not the school budget on the line."
  
  "Kelsey liked to think that Mr. Watt just persuaded the faculty because he himself liked the mountains rather than any suitability it held for a book club. Regardless, they had a good place to sleep - with actual beds - and transportation."

  "Eloise and Tag had a shared room over in the girl's cottage - really just a small building the resort staff delegated to the girls of the club, while the boys and Mr. Watt shared a selection of rooms in a separate cottage."
  
  "For a resort, the place wasn't too haughty, it was rather humble but quite comfortable - more so than Eloise expected."

  "The first day would have been quite a peaceful endeavour if it weren't for Kelsey either whining about all the teasing or just generally making a fool of himself; or Tag's refusal to get down and dirty, which, as she would put it, meant avoiding anything \"uncouth\"."
  
  "It seemed that despite all her tough talk, she was the most sensitive to getting a little muddy. Mind you, she also included Kelsey in her definition of \"uncouth\". Reasonable enough."

  "Much to Eloise's relief, nobody got eaten by a bear or swarmed by hornets. It didn't stop her from freaking out when Kelsey decided to imitate a bear roar."
  
  "Tag made sure to really nail that one into Eloise for the rest of the day, though she ragged on Kelsey for how lame the roar - and scheme as a whole - was as well."

  #resort rooms
  "By the time everyone got back to their rooms it was very late, at least by most peoples' standards. Mr. Watt had insisted on \"maximising everyone's time\" out and about, though everybody had to stay within the resort's borders by the time night began to fall."

  "Eloise was up later still chatting with Tag. By the time they finally went to bed it was past midnight."

  "Lying down on a bed felt great after the long day, and, much to her surprise, Eloise hadn't regretted any part of the outing yet."

  "Submitted to all the fatigue washing over her, Eloise quickly realised a fatal flaw in her plans to sleep. She'd be neglecting to drink water for practically the entire day, and her parched throat was scratchy and irritated."
  
  "Normally she'd ignore it and sleep, but knowing she had another week of days like this, and knowing how her mother always warned her that she'd collapse, she decided to force herself up and get some water."

  "Of course, the one thing her mother had told her to bring - a water bottle - she'd completely forgotten. It did surprise her that her mother didn't pack one for her like everything else. Thankfully, there was a kitchen on the premises, and the doors had no locks beyond staff rooms."

  "Eloise barely had any time to adjust to the moonlight before she was out and stumbling through the dark hallway. She recalled being told the dining hall - and subsequently the kitchen - was a bit further down the resort, and she could easily make it there by going through the boys' cottage."
  
  "It was a smooth transition from there to the kitchen, and she had soon quenched her thirst with a more-than-welcome serving of tap water."
  
  "She was a little off-put by the different taste the water had - she assumed they must use rain tanks instead of running it through the public water system - but her throat told her to keep drinking."

  "Eloise started wandering back after that, half in a daze and certainly ready to collapse into bed. Much to her surprise, as she trudged through the boys' cottage, she bumped into someone in the dark and was startled half way to a heart attack and back."
  show fi surprised wj at leftF
  f "Woah, careful now. Is that you Eloise?"
  show el surprised nj at rightE
  e "Finn? Yeah, it's me. What are you doing up? Can't sleep?"

  "Eloise had already made assumptions as to why he was up - maybe he was insomniac, or Kelsey was snoring too loud - but she asked all the same."

  f "Yeah, just can't sleep. You too, I take it?"

  e "I'm taking more of a breather. Need a little company?"

  "Eloise could barely make Finn out in all the darkness, but she could tell he was smiling."

  f "It would be appreciated."

  scene bg sky night
  "The two wandered just outside the cottage and had a look out into the woods. The moon gave ample illumination, particularly compared to the dark cottage interiors and the stars littered the sky in all sorts of beautiful arrangements."
  
  "There was a rustling in the trees, though, Eloise knew the offending leaves were on branches far too high for a bear to be lurking."
  show fi default wj at leftF
  f "Hey, hold up, you."

  "Finn removed his jacket and draped it over Eloise. She was in nought but her pyjamas and the chill was certainly starting to get to her. Finn had clearly been more responsible than she had - though naturally she didn't say this. All the same it was a simple gesture that meant a lot."
  
  "Finn looked out for the group, even if they could lay on some hard bites with their relentless insults. Eloise looked up to him as a bit of an older brother sometimes, and notions like this were precisely why."
  show fi default nj 
  f "It would certainly ruin the trip if you went and got a cold."

  "Finn gave Eloise a light pat on the head. It was a nice feeling, but Eloise couldn't help but feel belittled by it."
  show el smiling wj at rightE
  e "I'm strong. I won't get sick."

  "Eloise immediately thought back to how she needed help just getting her luggage on the bus, but decided it'd be best to just leave that part out."
  show fi smiling nj
  f "I know, but let me protect you."

  "It was a statement that sat strangely in Eloise's mind, but, try as she might, she couldn't come up with any counter. She could tell Finn was smiling as he looked out into the woods near the cottage."
  
  "She felt safe, though at the same time, the following silence left her a little on edge. She couldn't help but wonder what was going on in Finn's head."

  f "You remember when we first met?"

  e "Well of course, but, why this all of a sudden?"

  "Finn placed a hand on Eloise's shoulder."

  f "No real reason."

  "Eloise felt a little uncomfortable - not so much because of Finn, but because she had no idea what he was thinking- but she decided to humour him to try and get him to open up."

  e "Well, it was back in the first month of high school."

  "Finn seemed to be pondering, vocalising a questioning \"hmm?\" that held Eloise in her tracks."

  f "Is that so?"

  e "You forgot already? Not cool, Finn."

  "Finn chuckled softly and placed his spare hand on Eloise's other shoulder. He began idly rubbing her shoulders."
  
  "Eloise was pretty sure it was a purely subconscious notion, like chewing on a pen in class to mitigate anxiety, but it was still foreign behaviour to her usual depiction of Finn. If anything, it only made her tenser."

  f "That's not it at all. I was just thinking, like, specifically, how did we meet?"

  "Eloise's eyes scanned around the environment as she thought. Giving her mind something to focus on - and of course the beautiful scenery - gave her time to relax again. It made her quite appreciative of the light - if unintentional - massage."
  
  "It reminded her that, yes, Finn definitely was her friend, and a good one at that."

  e "It was in the book club, I think- wait, no. That was our second meeting. The first time was when I fell on you and strained your ankle. Well, whoops. Sorry about that one."

  "Finn leaned himself in closer to Eloise, as his voice fell a bit softer than before."

  f "It's an old incident, no need to apologise. If anything, I'm glad for that little injury. If it wasn't for that, we wouldn't have met, nor would we be as close as we are now."

  "Eloise's shoulders rose up as she pouted."

  e "That's not true, as long as people give me a chance I'm open to anyone."

  "Finn took his hands away from Eloise and cleared his throat."

  f "Would you still be my friend no matter how much I were to change?"

  "Eloise was unsure how to interpret the question, her mouth fell ever so slightly agape as her brows rose to a questioning gesture."

  e "Well, you're still my friend, right? Even if you were a monster you'd still be my friend in there, right?"

  "Eloise turned around and put a finger to Finn's heart. Both of their eyes never left each other for even a second in that moment."

  e "So long as I know you're right here, it won't matter."

  "Finn held Eloise's hands gently, not daring to look away. If anything he was stunned, though sadness seemed to permeate his features. Upon regaining his bearings, he pulls Eloise into a tight embrace."

  f "Thank you..."

  "Eloise felt the warmth of the embrace, felt his hands glide along her back in smooth motions. It reminded her of just how cold it really was out here, but at least this way they could both be warm."

  f "Eloise?"

  "She didn't want to talk, just to savour the moment, though she knew she couldn't leave him unanswered."

  e "Yes?"

  f "I'm going to move away soon."

  "Eloise pulled herself free of Finn's embrace."

  e "What? What are you talking about?"

  f "Now that I'm an official heir to my family, I need to devote myself to my studies. The best programs are abroad. If I'm to one day lead the company, that's where I'll have to go."

  "Eloise could say nothing, only stand with her mouth agape."

  f "It's a heavy responsibility and a great honour. I can't let my family down. That's why my entire childhood has been keeping me on the edge of this moment."

  "Eloise looked down at the ground, at the two pairs of feet that stood pointing at each other."

  e "It's okay, I understand. If it's really the path you want to follow, I know we'll all support you. We aren't children after all, so we'll manage. I-... just make sure you stay safe. We would all like to see you again."

  "Finn said nothing in response, he only wrapped his arms around Eloise and pulled her tight again. Somehow, the embrace felt a little less warm to her now - it's knowing how long she'll have to wait to feel it again, she told herself."

  f "It's late. I shouldn't keep you out any longer."

  e "Right... You too. Go to sleep or you'll never wake up to enjoy the day."

  f "Good night, Eloise."

  e "Sleep tight."

  "As she turned to leave, Eloise really started to feel the chill in the air. It ran up her spine and spread throughout her body. She folded her arms tight around her chest to stay warm and fend off the shivers."

  e "Maybe I shouldn't have stayed out so long."

  "It struck her that she still had Finn's coat. As much as it'd leave her cold as she made her way back to bed, she knew he'd want it back with how the weather was out here."

  "She made her way back to where she'd seen Finn, undoing the short distance she'd made back to her own room. Finn was nowhere to be found."

  "He must be back in his room, she thought. Seeing no point of knocking on his door when he's probably halfway to sleep by now, she decided to return it the following morning. She makes her way back through the cottage towards her own room."

  "A noise just outside made her stop dead in her tracks. She could only question what it was as she stood shaking in her own skin."

  "There was another noise, this time inside the building. It sounded like movement, but too erratic to be anyone walking around for a late night stroll."

  e "Hello? Anyone there?"

  "There was no response. Eloise felt incredibly uneasy, she recalled how something bad always happens when you hear strange sounds at night, and as much as her curious soul urged her to investigate, her legs were carrying her straight to her room."

  e "It's totally a bear, isn't it. Nopenopenopenope."

  "Eloise gave a big sigh of relief upon reaching the girl's cottage, and from there took a more leisurely pace."

  e "Look at me getting all worked up... It was probably just a squirrel."

  "She was mere meters away from her room when she noticed something behind her. Before she could react she was restrained around the neck, and some sort of soft, wet fabric was held up to her face. It only took a few seconds of panic before the sickly sweet scent of the fabric overwhelmed her."

  "Goodnight."

  #---
  scene bg sky clouds2

  "Eloise looked all around. She was back in that place again. That void where she found the crying child. Maybe she had been dreaming earlier, or maybe she wasn't in a deep enough sleep. She never knew quite what the conditions for the dream were, but she found herself in that place often."

  "Each time she's been within the dream, that child has not been present. As her only lead, Eloise decided to walk until she found the child once more. The place was endless, but she kept walking. She knew that eventually she'd find something."

  "She was right."

  "Exactly like the last time, she heard a voice and followed it without hesitation. She noticed the crying again, only, it seemed to be less of a cry the closer she got."

  "It's time to wake up."

  #---
  scene bg black

  "Everything was dark - completely so. Eloise felt like her eyes were still closed, but she knew they were open. It really was just that dark."
  
  "She didn't remember much, and the darkness gave no tips, all she could do was try to stumble around and feel her way around. Wherever she went, one thing was consistent. A horrible, damp, smell."

  e "Tag? Tag, you there?"

  "Silence. Eloise knew Tag was usually pretty easy to wake up, but she felt compelled to try again, just in case."

  e "Hey! Tag!"

  "There was still no response. Furthermore, Eloise hadn't exactly made a point of feeling around her room at the resort, but she knew this wasn't the same room. She also knew it wasn't her own room."
  
  "There was no comfortable bed and what furniture she could find felt gnarled, damp and broken. She realised the scent she'd been picking up was mould, and it was no subtle smell either. Invasive would be putting it lightly."

  "Moving around so much had quickly brought Eloise's stiff limbs to her attention. She was used to falling asleep in cars and waking up all cramped, but this felt a lot worse than that usually did."
  
  "Every limb felt tense and ached as though she'd been cramped in a small box for a week. She attempted to stretch, but it was fair too painful to stretch her limbs out fully. Instead she stuck to small flexes at a time."

  "Eloise remained defeated in the room, attempting to stretch out her cramped limbs and try and remember what it was that happened. Her memory was hazy, but she recalled heading back to her room, and being restricted and bombarded by an overpowering scent."

  e "Was I... abducted?"

  "The thought was not a pleasant one, and made Eloise's heart race. She had no idea where she was or how she got there, and her final memory leading up to it all was none too pleasant."

  e "I... need to get out of here."

  "Stumbling in circles around the room, Eloise managed to find a door. Of course, it was locked. At the very least, she felt she could listen beyond the door to find something. Unfortunately, there was a not a sound at all, beyond the occasional flutter of wind - or perhaps it was a draft - she had no way to tell."
  
  "An attempt to search the room again had yielded a small drawer with a key inside, but it didn't fit the door. Beyond that there was nothing but old, presumably mouldy furniture."

  "Eloise decided to keep the key, just in case. It gave her some small measure of relief knowing it might be handy later."

  "She paced around the room as she tried to analyse the situation."

  e "Maybe I can break the door down... It seems pretty old."

  "It seemed like a workable plan - at least at first - but Eloise quickly realised that whoever abducted her was probably still around, and that the last thing she'd want to do is make noise."
  
  "Instead, she tries to fiddle with the lock. She had never picked a lock before, but she figured that everything was worth a try."

  "She searched all of her pockets and came across a bobby pin lodged away at the very bottom of one pocket. It had practically become a part of the pocket it was mashed in there so well. Eloise figured the bobby pin had probably been there for weeks if not months."
  
  "She didn't use them often, but she did have a tendency for leaving all sorts of things - cash, accessories, junk - in her pockets and forgetting about them."

  "Eloise remembered one time where Tag had used a bobby pin to break in to one of the school rooms - since a teacher had confiscated her phone for the third time and she didn't want to have to wait for her mother to pick it up, and thus have to admit being caught using it in class, again."
  
  "Eloise didn't really recall why she decided to go too, but it did give her a close look at the process. Why Tag knew it was anyone's guess."

  e "Let's see, I remember something about snapping the pin in half and bending one of them..."

  "Following her memories of Tag as well as she could, Eloise snapped the bobby pin in two and bent the end of the wavy side at a ninety degree angle."
  
  "Whatever Tag had done next had been a bit difficult for Eloise to see, but she tried her best to imitate what she'd seen, wedging the angled bobby pin into the side of the lock and jiggling the other piece around inside it."
  
  "It took only a few seconds before she realised she'd gotten the bulbous end of the bobby pin stuck in the lock. She had fiddled with the lock some more, but didn't want to risk breaking the pin, and decided to stop for a breather."

  "Having taken a step back from the lock, Eloise realised she could hear noises beyond the door. Footsteps - and they were approaching. She could feel her heart ready to jump out of her chest."
  
  "She knew she had to hide, but she couldn't even really see, she knew she'd be found. Maybe she could hide behind the door and rush out when her abductor enters. She could feel the adrenaline run through her body, the tingle run up her spine, but she felt it was her best chance."

  "Eloise waited and listened as the footsteps got closer and closer. Waiting behind the door, her knees were shaking and her breath erratic. She heard the doorknob rattle and turn, and the telltale creaking of the door swinging open - with it a small splash of moonlight."
  
  scene bg attic
  
  f "Eugh, the lights are out here, too?"

  "Eloise had recognised the voice, it was Finn she'd heard"

  e "Finn?"

  "As much as she realised revealing herself so readily could well have been a bad move, Eloise couldn't restrain herself."

  f "Eloise? Is that you?"

  "Eloise leapt out from behind the door to embrace Finn. A moment ago she'd felt as though she were about to break down, and now she had the comfort that she wasn't alone anymore, and that the two of them together could make it out."
  
  "The hallway beyond the door was lined with windows, finally giving Eloise enough light to see. Finn's face wass more than welcome to her deprived eyes."

  "Compared to Eloise's relief, Finn is busy shuffling about with Eloise clinging to him, gradually turning a glowing, beet red. For once he appreciated it still being dark. Finn felt Eloise's shoulders shaking against him, and wrapped his own arms tight around her."

  f "It's all okay now."

  e "Where on earth are we?"

  "Finn's grip loosened up as he thought about the question."

  f "A haunted house?"

  e "Tell me something I don't know."

  f "I really have no clue. I only woke up a short while ago. I just heard some noises and followed them."

  "Did Finn manage to break out on his own or was his room unlocked, thought Eloise."

  e "Was there anyone else around?"

  f "None that I saw."

  "Eloise felt herself starting to relax again, though she knew they were still in potential danger."

  e "Well, that's a bit of a relief. We need to get out of here, we should be safe if we're watching each other's backs."

  "Eloise started to move. Finn held her back."

  f "No. It's still dangerous. Let me check around first."

  "Eloise's features fell."

  e "What? It'd be horrible if we got separated."

  "Finn spoke confidently, with a surprising air of authority."

  f "Trust me. It's best if I check it out first. If we're together, then we can easily both be taken down. Let me check it out first. We'll join each other when it's safe. Stay here and wait for me."

  "Eloise slumped against the wall and pressed her face into her hands."

  e "Do what you want. Don't come back to haunt me when you're dead."

  f "No promises."

  "Finn began to leave, but Eloise held him back."

  e "What if my legs fall asleep?"

  f "You can sit down."

  e "What about the bathroom?"

  f "I don't think it'd be a good idea to go here. Try to hold it in."

  e "Can't you just let me go with you?"

  f "No is no. Look, I'm going to check that it's safe. Stay here."

  "Eloise simply stood and watched Finn leave. She grumbled under her breath, though her body shook, partly from the  chill, partly from fear. She waited for about a minute in that spot, consistently reprimanding herself for doing so."

  e "Like hell I'll stay here. I don't want to die."

  "Compelled by fear, curiosity and plain defiance, Eloise couldn't keep herself still. There were too many unanswered questions. Why was she here? Where was she? What was Finn doing?"
  
  "She couldn't leave him out there alone, as scary as chasing after him on her own felt. There was also the common horror cliché of everyone dying when they split up."

  e "Where could he have gone..."

  "Having followed the way she saw Finn leave in, Eloise quickly stumbled across a staircase. With nothing else of particular interest nearby, she assumed it had to have been the way Finn went."

  "Going down two steps at a time, Eloise is relieved to have the smell of mould leave her nose, though it's quickly replaced with something even more unsettling. Blood, and some other things she can't quite determine."
  
  "Her descent slows as she nears the bottom of the stairs. It's dark, though there's enough light peeking through windows for her to at least see now."

  "Her surroundings seemed less ramshackle than the room she was in earlier. Whoever the tenant - or owner- was, they certainly let the place go. Dust lay on everything, and there seemed to be some stains on both the walls and floor."

  "Eloise had frozen stiff as she heard wood creaking nearby. She slowly turned her head to face the direction of the noise, and saw but a creaky door moving with the slight draft."
  
  "She let out a sigh of relief and approached the door. It was as good a lead as any."
  scene bg living
  
  "The moment she touched her hand to the doorknob, the door crept open on its own. Inside was but a plain, old study. Everything about the room is fine and dandy, but the woman who was within, seated upon a chair in the center of the room, left Eloise with a feeling of dread."
  
  "As much as Eloise felt the woman could be in the same situation as she herself, she knew that nobody would sit alone in the dark like that if they were trying to get away. She had to assume it was one of her captors."

  "Eloise began to back away slowly, pulling the door with her. The door creaked to no end, far more than when it was simply swinging in the draft."

  "Eloise heard the hoarse, broken voice of the woman rise up."

  w "H-honey? Are you there?"

  "Instantaneously, Eloise's first reaction became to swing the door shut. As she positioned her body to slam the door, she heard scuffling about the room. As she slammed the door, it came with a grotesque crunching sound. The door didn't close."
  
  "A hand lay between the door and frame, curling around the side of the door and scrambling about along its surface with an unsettling clacking sound of nails on wood."

  "There was a moment of silent horror as Eloise simply stood, watching the hand shaking and contorting violently, before her senses came back to her and she began pulling at the door, trying to get it shut."
  
  "Her motions were just in time, too, as the woman on the other side began pulling at it with incredible force. Eloise had to press a foot up against the wall just to put up enough resistance to hold the door closed."

  "The woman on the other side began to scream, surely only damaging her broken vocal cords even more."

  w "Honey... Don't you leave! You come back! Come back!"

  "The doorknob is pulled free of Eloise's grasp, now exposing her to the woman. The woman both looks and smells as though she hasn't taken care of herself for weeks, maybe months, maybe longer still."
  
  "Even with her hair up in a bun, it fell messily all over her face, with wild, tangled strands protruding out of every side. Her features were sunken, malnourished, and yet still she possessed incredible strength."
  
  #chase music
  #hallway?
  "Eloise knew that now was the time to leave, and quickly turned heel to put as much distance between herself and the woman as possible. Her legs were still cramped and in pain, but she pushed on, not daring to find out what might happen if she stopped."

  "The woman leapt after her, slipping around corners and using her arms to push herself off walls and furniture as she pursued."

  "By all accounts, Eloise swore the woman looked like a walking corpse. As much as she knew it wasn't true, it was certainly unsettling."

  w "You finally returned to me... after all these years... come back to me!"

  "Eloise couldn't help but think about whether she ever had been here before, but realised that it was both a stupid thought and hardly what she should be focusing on. Whoever this woman was, Eloise certainly knew she had no relation to her whatsoever. All she knew is that she had to get away."

  "All the while, the woman stays hot on her heels, even as much as she stumbles around corners, or into furniture, knocking things all about. In her pursuit she keeps saying but one thing."

  w "My child! My child!"

  e "I'm no child of yours!"

  "Eloise didn't know why she responded. It felt beyond ridiculous too, and yet, it was letting her know she was still alive and breathing. She knew she should reserve her strength and her oxygen, but she couldn't remain silent."

  w "We will never part again... I won't let you leave again..."

  "Eloise quickly realised she's been running in a loop through but a small number of rooms. She risked taking a look to try and find an exit, but couldn't see any ready openings in the darkness. All she caught sight of was a shiny metallic object in the woman's hand."

  e "A knife?! No no no no no."

  "After another loop, Eloise felt her breath starting to leave her for good. She frantically looked for an exit, and was lucky enough to spot a stairway off to the side. She turned and made a beeline straight for it. As she approaches the top of the stairs, she looks down and sees..."

  f "Eloise!"

  e "Run!"

  "Eloise leapt from the top of the stairs, thankfully it was but a small flight, but, as she soon came to realise, she could have been far less lucky than she was."

  "As she hits the bottom of the stairs, she goes crashing straight into Finn, thankfully softening her fall considerably, but knocking them both flat on to the ground in the process."

  "She's certain the landing wasn't so soft for Finn, but his groan was more than enough to let her know he was okay."

  "With haste, Eloise began tugging at Finn's shirt to get him up on his feet."

  e "Get up! We have to run!"

  f "No, look!"

  "Eloise turned around, to see the woman collapsed on the stairs in a grotesquely contorted position. A liquid was cascading down each step one by one - it was blood."
  
  "Eloise could see the glint of the knife embedded into the woman's body. With the unsteady gait that woman had, she must have stumbled on the stairs and lost control of the knife."

  e "Oh god..."

  "It was a sight Eloise could hardly take her eyes away from, even bathed in darkness as it was. She'd never seen a dead person before."

  f "Eloise... Um..."

  "It took Eloise another few moments for her to register how embarrassingly she was positioned atop Finn."

  "For both of them, it was not the time to focus on such trivial matters, though. The body quickly regained its interest and drew Finn's direct attention once they were both up on their feet again."

  "Finn leant over the body, presumably checking that the woman was indeed dead."

  f "How fortunate."

  "The more Eloise looked the body over, the more she realised how contorted the woman now was. The fall had easily dislocated a few bones, nevermind the knife embedded into her gut."

  "Finn takes hold of the knife's handle, and with shocking brute force, tugs it right out in one fell swoop. Whatever veins and arteries the knife was blocking up were now free to spray and gush more blood out of the woman's corpse."

  "Eloise turned away as she felt herself gagging. She knew Finn was an avid horror fan, and lover of all things gory, but this was a bit much."

  "Before she'd even had a chance to turn back around, Finn was in front of her, holding the knife out."

  f "Take this."

  "Eloise's whole body recoiled, she hadn't even had the chance to lower her hand from her face before she felt the need to gag again."

  e "What? It's disgusting."

  "Finn stared directly at Eloise, his voice rising in volume."

  f "It's for your own safety."

  menu: #CHOICE 1
    "How can you say that with a straight face?":
      $Q1Flag = 1
      $KnifeFlag = 0
      jump lbl_straightFace

    "No, you keep it. I don't want to touch that thing.":
      $Q1Flag = 2
      $KnifeFlag = 1
      jump lbl_noTouch

label lbl_straightFace:
  ##A:
  e "I don't get how you can say that with a straight face... That thing... "

  f "What? Don't you watch a lot of movies? You should be used to this sort of thing."

  "Eloise stamped a foot down on the ground."

  e "This isn't a movie, Finn!"

  "Eloise realised she was breathing erratically, and had a cold sweat beading down her forehead. She knew Finn must have just been more acclimatised to such horrid prospects than she was, but it still shocked her."

  "The most she could do to calm herself was to keep telling herself that Finn was just more desensitised,"

  f "Eloise, take it."

  "Finn held the knife out towards Eloise."

  e "I don't even know what I can do with that, Finn!"

  "Finn sighed, withdrawing the knife and gripping it tightly once more."

  f "This time I'll be here to protect you. I know I can't ensure your safety if we part... or rather that I can't trust you to sit still when you're on your own."

  e "I guess I'll have to rely on you, then... I can't say I'm fond of putting so much on you."

  "The blade was still dripping in Finn's hand, blood rolling down over his fingers. \"How could he hold such a thing?\", thought Eloise."

  e "Can we please get out of here now?"

  "Finn gave a firm nod."

  f "Yes, let's."
  jump lbl_AfterChoice1

label lbl_noTouch:
  ##B:
  e "No, you keep it. I don't want to touch that thing."
  
  "Eloise carefully watches the blade, watches the beads of blood roll along to the tip and drip off of it."

  f "If we get caught in a situation like before, there's no knowing what could happen. I need to know you have something to defend yourself with."

  e "I can tell you're not giving me a choice here. I'll take the damn thing."

  f "I'm sure you'll be fine."

  "Finn carefully offered the blade over."

  "Feeling the blood on the handle almost made Eloise drop it on instinct. It was slick and it was disgusting. Despite her disapproval, she did feel the slightest bit safer with it."

  e "What about you?"

  f "I'll be fine. What's important is that you're safe."

  "Finn took Eloise's hand for a moment, thankfully with his own, unsoiled hand, and held it tight. It was a welcome warmth in all the cold and darkness."

  "Eloise felt that she could see a slight blush to Finn's cheeks, but assumed it was probably because he'd been running around and on edge too."

  ##CHOICE END - BACK TO COMMON ROUTE
  jump lbl_AfterChoice1

label lbl_AfterChoice1:
  f "Anyway, I've looked around but all the doors I've come across have been locked. We may find something down here, though."

  e "What about the windows?"

  f "All the ones on the lower levels are barricaded... I don't want to risk dropping from the higher ones in the dark."

  e "Can we get the barricades down?"

  f "If we can find a hammer we can."

  e "Well, I guess we better start searching, then."

  "Together they started searching around the first floor - or as much as they could gain access to. The closest room was the living room, and from there the kitchen could be accessed."

  "Beyond that, there were two closed doors, though Finn said he hadn't tried them yet."

  e "Alright, I say we start with what we know is safe. Let's check the living room out."

  f "Let's see if we can find anything."
  show bg living with fade
  "Together, they entered the living room and began their search. As they enter, Eloise sees the barricades for the first time - large, sturdy, and certainly going to be a nightmare to remove."

  "It reminded her that, even if they were to escape, they don't have a clue what's out there. It could be even more dangerous outside."

  "Eloise inhales deeply."

  e "I'll search this side, you search that side."

  f "Just remember to be careful."

  e "I already learnt that the hard way."

  "Rummaging through whatever she could find, Eloise mostly just encountered dust and junk - and lots of it."

  "She maintained her spirit, and didn't let the meager findings beat her down, moving from one piece of furniture to the next."

  "Everything in the house just screamed abandoned... or haunted."

  f "I can't find anything at all over here."

  e "Same here... we need a torch or something."

  "At that moment, Eloise had felt her hand brush against something considerably more solid than the idle scraps of junk and dust she'd been swathing through."

  e "Hey, I think I've got something."

  "She lifted it up into the light. It looked like a journal of some sort. Old, worn out, leather cover with a button to fasten it shut."

  e "I think it's a journal. Looks as old as everything else in this damn place."

  f "I don't think it'll hurt to take a look. Give it a read. I'll keep looking."

  e "If you're sure."

  "Eloise flipped a few pages into the diary and held it up to the light. It was a strain, but she could read the writing."

  "Jon has been a little... estranged since we moved. He's become quiet, and whenever he does talk he's usually muttering nonsense. I asked him what was wrong, and he told me that 'they are crying'."

  "I tried asking him who he was referring to, but he only said that 'they cry so much'. I couldn't get him to say anything else. I know something is dreadfully wrong, but I can't seem to figure anything out."

  "He won't talk to me, and there are no signs that I can find as to why he's acting this way. Maybe I should seek help from his friends."

  "Eloise skipped ahead a few lines."

  "Recently, Jon's been gawking at our kids like they're some kind of monsters. I don't think he's been sleeping much. He always looks so tired, and his eyes are so bloodshot and weary."

  "I fear that maybe he's been taking drugs. He keeps staring at the children, it's even starting to get to them. It's not affectionate, it's intimidating. He's starting to terrify little Jimmy, every time I leave them alone I come back to find Jimmy crying about it."

  "Daisy's taking it a little better, but I know she's scared too. Jeanna's tried to talk to him, but even she's coming back unsettled."

  e "Weird..."

  "Eloise skipped a few more lines, trying to unravel whatever was in the journal as quickly as possible."

  "His problem is getting worse... I have to get him out of the house, I need to get him to a professional. We just live so far away from town that I don't want to risk leaving the kids alone at home for so long."

  "I'll have to bring everyone along if I do. Sometimes I wish we hadn't bought this house just because of the price. Sometimes during the night, I hear crying from downstairs."

  "Whenever I check on the kids they're always in their rooms, sound asleep. All the stress is making me paranoid. I must be hallucinating in an effort to tell myself that my husband is still in there."

  "The next entry."

  "I don't know where the children are. I left them here with Jon while I went into town for shopping. I'm scared. I've looked everywhere and I can't find them. I tried to ask Jon, but he'll only tell me that 'the crying has stopped'."

  "I don't know what he means, but I fear the worst. I know he's a bit unstable, but I know he still loves our children."

  "As she flipped to the next page, Eloise saw but a single sentence."

  "Where are the children?"

  "Eloise tried the next page, and the next. They were all mirror images of each other from then on."

  "Finn appeared behind Eloise's shoulder."

  f "Did you find anything?"

  e "Only enough to tell me that we're either in a haunted house, or some psychopath's lair."

  f "Or even both. We shouldn't stay here for too long."

  e "You don't need to tell me, that."

  f "Let's go check the kitchen."

  "Eloise quickly grabbed Finn's sleeve."

  e "Wait. From what I understand, there's still someone in here. We need to be careful."

  "Finn nodded in response."

  f "Let me go first."

  "The two crept quietly into the kitchen. There was nobody in sight, but as they entered they were bombarded by a foul smell."

  "Eloise first reaction was to cover her nose. There was a decaying piece of meat on the dining table. It must have been there for weeks."

  "It smelt absolutely dreadful, and Eloise was sure that if she could see it clearly, it would look the part, too. Whoever their host was, they were clearly lacking in hygiene."

  e "Every room has something different in this place."

  "Finn seemed to be considerably less affected. Surely it couldn't be just desensitisation. The smell was absolutely foul."

  f "Indeed. Just try to bear with it for now."

  e "Can we just hurry up? I don't want to stay here."

  "Eloise could constantly feel herself growing more and more nauseous with every passing moment. She held her top's collar up to try and mask the smell, but it did little to weaken it."

  "She made her focus on getting through all the cabinets as quickly as she could. She knew not to be too reckless about it, even the smallest thing could help."

  "It had certainly been a painful process, but Eloise's diligence paid off when she stumbled over a small key. That made two of them she'd found."

  e "Found a key!"

  "Eloise immediately regretted opening her mouth. The smell was plain toxic."

  f "Do you know where it might go?"

  "Eloise stepped just outside of the kitchen to spare herself from the noxious odour. This time she made sure to speak through her top."

  e "If there's a key, there's a lock. We just have to find it."

  "Finn wandered out of the kitchen in pursuit."

  f "Right you are. Well, should we start looking?"

  menu: #CHOICE 2
    "Yeah, let's look around some more.":
      $Q2Flag = 1
      jump lbl_lookMore

    "There's nothing else to find here.":
      $Q2Flag = 0
      jump lbl_nothingLeft

label lbl_lookMore: 
  ##A:
  f "Alright, let's give it another once over. I don't think we should stay in one place for too long, though, we might attract some attention."

  e "We'll keep it quick."

  "Pulling up a chair, Eloise quickly began going through all the old cabinets and cupboards, reaching far into the back of each from her newfound height."

  "With what little she could see, she could tell they were all practically empty, aside from the odd item of canned food or empty jars."

  "The rancid odour only got worse the more she'd lingered. Eloise could feel herself getting closer and closer to vomiting."

  f "Anything?"

    
  menu: #CHOICE 2A
    "I give up. Let's get out of here.":
      $Q2Flag = 0
      jump lbl_giveUp

    "Just a moment more.":
      $Q2Flag = 2
      jump lbl_aMoment

label lbl_giveUp: 
  ##A2:
  f "It's fine, we've already checked just about everything here. I doubt we'll find anything else."

  "Eloise could really feel herself gagging, and it was plain to see that Finn was starting to fall under the same effect."

  e "Come on, let's go already!"

  "As she started jogging out of the room, Finn caught her by the shoulder."

  f "Hold up."

  "Heart thumping in her chest, Eloise turned back to Finn."

  e "What is it?"

  "Finn pointed a finger up towards the ceiling."

  f "Up there."

  "Looking up where he was pointing, Eloise saw what looked like a trap door in the ceiling. It was well hidden, particularly in the darkness, but it was definitely there - betrayed by a handle."

  f "The ceiling's too high, even with a chair."

  e "One more thing to add to the list. They must have a ladder somewhere."

  f "We can get back to it later. Just remember it."
  jump lbl_AfterChoice2

label lbl_aMoment:
  ##B2:
  f "No objection, but be careful."

  e "Of course."

  "Having thought there must be something elsewhere in the room, Eloise quickly scanned the tops of the cupboards, the walls and the ceiling."

  "Her eyes catch something on the ceiling - a break in the simple floral pattern that adorned it - a handle attached to a trap door."

  e "Hey, Finn, look!"

  "Eloise pointed at the trap door, and Finn's eyes quickly followed."

  f "Hmmm."

  e "It has to be connected to the upper floor, but the ceiling in this room is too high."

  f "Well, for you. As much I could hoist you up, we'd still be too low to reach it."

  "Finn almost seemed to snicker as Eloise folder her arms."

  e "Well forgive me for being short."

  f "I'm sure there'll be a ladder somewhere around here."

  e "Well, we're all out of ideas here until we find it. Let's go."

  "Finn offers a hand to Eloise, helping her down off of the chair. She steadies herself quickly upon the landing - thanks to Finn's help - and brushes the dust bunnies off of her clothes."
      
label lbl_nothingLeft:
  ##B:
  f "I have to agree."

  e "Any idea where to go next?"

  "At that moment, Eloise stopped. Standing still gave her the opportunity to listen far more carefully and she felt she could hear something. "

  "It sounded like voices - children, specifically - giggling, and overall sounding quite gleeful, even with how distant and reverberated they were. She looked over to Finn, unable to trust her own senses. Finn doesn't seem to notice."

  f "Everything alright?"

  e "Do you hear anything?"

  "Finn's left brow raises quizzically."

  f "Do you?"

  e "No, nevermind. Let's go."

  jump lbl_AfterChoice2
  ##CHOICE END - BACK TO COMMON ROUTE

label lbl_AfterChoice2:
  f "We may as well find out where that key goes."

  e "Well, we just need to find a door that might work. This one's a small key."

  f "I think the door near the stairs might be a good start. It had a simple, small lock."

  e "What are we waiting for, then?"

  "Hurrying off before Finn had a chance to stop her, Eloise tries the key on the lock. The key fit inside perfectly, but the teeth must have been incorrect - it wouldn't turn at all."

  f "I don't think that's going to work, Eloise..."

  "Without Eloise even having heard Finn approach, he moved right behind her, too close for comfort. He's practically breathing down her neck when he moves her hand back from the lock. Eloise doesn't move, not knowing what to think."

  e "...Finn?"

  "Eloise shuffled around, but Finn was right behind her, practically pinning her in place."

  f "I think the key's for another door."

  e "Yeah... right."

  f "You're acting strange."

  e "Me? I don't think so at all... Surely you're mistaken."

  f "Maybe I am. I am worried about you. This place isn't exactly safe nor fun to be in."

  e "I know that, Finn, but I am alright... for now, anyway. The sooner we're out of here, the better. Sorry for causing you trouble."

  f "It's not a problem at all."

  "Finn smiled as he offered his hand."

  f "Take it if it'll make you feel safer."

  "Eloise hesitated, it was an unusual gesture at the time, at least in her eyes, but the offer of something so simple and debatably mundane in a world gone mad was a comforting one."

  "Finn's skin practically glowed in the dark his skin was so light. If Eloise didn't know better she'd claim he was a ghost. Gingerly she placed her hand in his."

  "Finn's hand wrapped gently around Eloise's, crossing their fingers over each other. He smiled gently, clearly pleased that Eloise responded amicably."

  "Together the two moved hand-in-hand from one door to the next, comparing locks to the key in their possession."

  "Eventually they found a door it opened."

  e "It's dark. Can you see anything in there?"

  f "Not a thing… though I should have a lighter come to think of it."

  "Eloise felt her hands instinctually clench tighter."

  e "You didn't think of that earlier? We've been stumbling around in the dark!"

  "Finn held a finger up to his lips."

  f "Shhh. Not so loud."

  "He gave a heavy sigh."

  f "We haven't exactly had the clearest cognition with everything else going on in this place. Don't think I don't know I should have remembered sooner."

  "Eloise's hands slowly loosened up."

  e "Alright, I understand… but still, every little thing could be the difference between making it out of here or becoming part of the scenery."

  f "I'll try to be more mindful of all our assets from here on."

  e "Well come on, let's go check out this room."

  "Finn quickly held Eloise back from the room."

  f "Allow me."

  e "Want me to go running around the house again? Look, just hand me the lighter, it should be enough."

  "Finn's hands clasped firmly over Eloise's shoulders."

  f "Eloise, it's dangerous."

  e "What makes it any different for you, then?"

  "Eloise could feel Finn's grip tightening, even as his expression softened."

  f "I'm just trying to keep you safe."

  e "We're in this together Finn, we should work together. I can't let you do everything."

  f "But… Eloise-"

  e "But Eloise, I'll be lonely and scared without you."

  "Finn's hands withdrew as he took a step back."

  e "Come on, pixel horror games have little girls as the main character all the time."

  f "And you were trying to tell me this isn't a movie."

  e "Oh come on, Finn. Let me help."

  "Finn's sigh was as heavy as a stormcloud."

  f "Your head's harder than a rock, you know that?"

  "After a few moments of shuffling through his pockets, Finn placed a zippo lighter in Eloise's hands."

  "Eloise could feel an engraving of some kind on the side of the lighter but couldn't make the details out with her touch alone."

  f "Just don't try to hunt me down when you're dead."

  "Eloise couldn't help but smile despite her situation."

  e "Same applies to you."

  "Flipping the top off the lighter, Eloise got it working after a few tries."

  e "Eloise used Finn's lighter."

  f "Oh do be serious. If you're going to make video game references all night I may as well give up now."

  e "Gotta stay sane somehow."

  f "You'll drive me insane in the process."

  e "Ah well. Off I go."

  "The room itself was almost entirely devoid of ambient light, leaving Eloise with just the lighter to make her way around. It was certainly a godsend given the situation but wasn't enough to stop her bumping into things."

  "As Eloise progressed, she began to realise just how spacious the room was. She couldn't even tell if she'd made it halfway through the room yet."

  "There had practically been nothing in sight from her current standing, beyond a few scatterings of broken furniture on the floor."

  "She could hear what sounds like drizzle somewhere close. Disturbingly it didn't seem to be coming from outside, but she couldn't determine precisely where it was coming from all the same."

  "She dismissed it as her mind playing tricks. The floor seems to be getting more and more damp, so perhaps there was simply a hole in the ceiling."

  "Under her feet she feels some sort of liquid with quite the grab to it. Whatever it is it's sticky and clearly more than just water. She felt it in her best interests to keep moving forward and ignore the mystery substance."

  "The deeper she entered the room, the more and more she began to regret the decision. It seemed consistently devoid of anything of use, just broken furniture all around, yet the further she got, the more she came across unnerving sounds and sensations."

  "Now she'd felt she could hear quiet murmuring from her left, and quiet cries from her right. Neither prospect sounded appealing, but going straight was only pushing her deeper and deeper into the mess she was already in."

  "Eloise glanced back over to where Finn had been. Thankfully, he was still there, though she could barely make him out. Despite her anxiety, she didn't want to go crawling back to Finn out of cowardice."

  "It didn't seem right after she'd already forced the lighter out of him."

  "All the same, she didn't have a clue which way she'd opt to go. They were both equally disturbing."

  #(if chose A2 or B in previous choices):
  if (Q2Flag == 0):
    jump lbl_DeadEnd_Silence
  else:
    jump lbl_goLeft
    
label lbl_DeadEnd_Silence:

  "Having decided that one way was probably as treacherous as the other, Eloise opted to try heading to the right."

  "The floor was at least marginally drier, though it meant she had to put up with the creaking of the old floorboards instead. The more weight she'd put down, the more it'd creak."

  "Eloise knew silence would be best, and stepped as lightly as possible. Thankfully, she hadn't seemed to attract any attention."

  "CRUNCH"

  "She'd trodden on something along the way - something that gave off the most sickly sound. It left her wide eyed and ready to rabbit. Looking back for Finn, Eloise was mortified to find nobody at the doorway."

  "Where could he have gone? She tried to formulate a reason as to why he'd be absent but only turned up unpleasant thoughts."

  "She'd wanted to call out, call for Finn, but she knew she had to be quiet - not that she'd have been able to speak through the choking fear anyway."

  "Eloise could hear something, hear something writhing about on the ground. For once, she gave in and looked down. That's when she saw it illuminated by the faint glow of the lighter.."

  "A grotesque creature - practically stretched, sinewy muscles stuck to haggard bones - dragging itself along the ground, eyeing her with its ghoulish eyes."

  "She couldn't even tell where its organs started or its body ended. It was just a mess of pieces. She wanted to scream, but felt her throat tightening, holding back every breath."

  "She did all she could. Try to escape."

  "In the dark, all she really wound up doing was stumbling backwards, scrambling away from the creature as fast as she could. The ground, however, was slick with something sticky, and her efforts led to no progress."

  "She wanted to scream. She wanted to run. She wanted to find something - anything - she could use to escape. There was nothing and her body would do nothing."

  "So this was true terror."

  "Eloise could make out other figures moving in the darkness, undoubtedly more of those abominations. They were pleading and crying, yet none of them would ever hear an answer."

  "She turned and tried to crawl away, slipping constantly on whatever liquid she lay in. Pushing herself up onto her knees then onto her feet, Eloise tried to leap away."

  "Her body simply wouldn't comply - her assailants had grabbed hold of her leg."

  "Before she could react, she was falling down again and lost her grip upon the lighter. It tumbled away, the light extinguishing the second it left her hand."

  "There was no way out."

  "Darkness overwhelmed everything. Eloise tried to reach out, but couldn't even see her own hand."

  "She can feel those creatures begin to clamber over her body. Feel their sinewy, rotting masses clamber over her body until she's pressured on every side."

  "Unable to move. Unable to breath. Unable to think."

  "She quickly loses all of her senses to insanity."

  "'Silence is cruel and bitter' - the final thoughts of a dying girl."
  
  scene bg black with fade
  
  $show_quick_menu = False
  centered "Dead End:\n\nSilence."
  return
  #Silence // Dead Ending #1

  #(if chose B2 in previous choices):
label lbl_goLeft:
  "Reason told her that one way was likely to be as bad as the other, but something in her gut had made Eloise decide to head to the left. She bit her bottom lip as she made her way in the chosen direction."

  "After a few steps, the floorboards gave a horrible whine, sounding like they were ready to snap and break just from her weight alone. She almost jumped back but thankfully caught herself. Any unnecessary pressure could well make that whine go straight to a crack."

  "Her panic instinctually made her look over to Finn. He was barely visible in the doorway and - though it took her a few moments to notice - she realised he looked worried, undoubtedly by the very same creaking that had startled her."

  "Eloise offered a simple thumbs up to put Finn at ease and suggest that the situation was under control."

  "Finn became noticeably more placid - or at least it lessened the edge to his stance - from the simple gesture."

  "Somehow it cheered Eloise up to see him relaxing as a result of her silly attempt to comforting him."

  "Boosted by newfound confidence, Eloise pressed forward. Barely more than a few steps in, she found something that seemed very much unlike the broken furniture that littered the rest of the room."

  e "Oh, a ladder!"

  "Miraculously, Finn had been able to hear her subtle exclamation."

  f "A ladder? How heavy is it? Do you need help?"

  "Eloise gave the ladder a quick hoist to get a feel for its weight. The size would make it awkward, but it was well within her physical limits to carry."

  e "No, all good. I can carry it out. Stay put."

  f "Don't hesitate to call me over if you need me."

  "Readying herself to hoist the ladder up proper, Eloise uttered a simple phrase."

  e "Heave ho."

  "The ladder was easily lifted up and shifted into a more comfortable position."

  e "Piece of cake. On my way, Finn."

  "It was difficult to see the ground afoot and avoid all of the obstacles with the ladder in hand - without a proper grip on the lighter, Eloise also singed her thumb lightly - but it was a straightforward trip back without any major hiccups."

  "As Eloise got back to the doorway, Finn revealed his anxiety with a heavy sigh of relief. He looked both paler than usual - something Eloise didn't even realise was possible give his already palid complexion - and plain nauseous."

  "Eloise opted to make another silly attempt at lightening the mood."

  e "Nothing to fear, Eloise is here!"

  "Finn sighed again, though this time it was filled with more bile than relief."

  f "You're the one causing me heart attacks in the first place."

  e "Oh I am not. Lighten up."

  "Within seconds, Finn's expression fell to a very flat, very lifeless stare."

  f "Remind me who was chased around the building by a knife-wielding psychopath?"

  e "Uh, me."

  "Finn raised one finger. His expression remained the same."

  f "And who disobeyed a simple instruction?"

  e "Me again."

  "Finn raised a second finger and waited a few moments for his lecture to sink in."

  f "Really now, please try to be careful and remember that whenever I suggest something it's for safety's sake."

  "Shrugging it off with a roll off the eyes ad rebellious stance, Eloise laid out her response."

  e "Alright, mother. Jesus, Finn, it's not everyday you get trapped in a haunted house. These aren't exactly normal circumstances."

  f "Uh huh."

  "Finn simply folded his arms and stared Eloise down."

  "Eloise did the same back."

  "It was a silent but lengthy battle but eventually a winner was found."

  e "Alright. I'll behave."

  f "Uh huh."

  "Finn kept up his posture and continued to stare her down to oblivion."

  e "Really now, I'm serious. Look, can we just try that ladder?"

  f "Here, give me that ladder."

  "Raising no objection, Eloise hands the ladder over. It's an effortless exchange. Free of the burden, she's free to more of her own thoughts"

  "She can't help but feel Finn's getting too protective, or at least protective beyond her own understanding of why. He's being way too tense - they need clear heads and rational thinking to make it out - such are her thoughts, anyway."

  "As they make their way back to the kitchen, Finn sighs long and slow. It's certainly not the first Eloise has heard throughout the night."

  "When they get back to the kitchen, Eloise waits patiently for Finn to set the ladder up. Watching him at work, she can't help but feel like he's trying to do everything himself - not that she was inclined to tackle it all on her own either way, but he did seem to completely disregard his own safety over hers."

  "After preparing the ladder, Finn does a quick check of the trap door in the ceiling. It opens without issue, though it's just as creaky as the rest of the house. Once he's back on the ground he proposes his plan."

  f "Looks like it's clear up there. Eloise, you go on up. If there's any trouble at all, just jump down - I'll catch you. If you need my help up there, give me a shout but be sure it's clear first. I want you to have a safe exit."

  "Surprised to hear Finn actually suggesting she go first - even if it were still part of his evident scheme to bubble wrap her - she found herself unwittingly nodding in agreement."

  "It only took Eloise a few moments to climb up the ladder and make safe footing in the room above."

  e "I'm up."

  "Giving the room a quick once over, it quickly became apparent that it was devoid of anything living aside from Eloise herself."

  e "Hey Finn, come on up here. We can search faster together."

  "Finn's own climb up the ladder seemed nearly effortless compared to Eloise, moving several steps at a time he was up before she could even really react."

  e "You know, don't you feel it's a bit rude to go searching through someone's house like this?"

  f "That never crossed your mind over the past few rooms."

  e "Don't remind me. I don't even want to think back to some of those rooms."

  "The room is as dusty and dark as ever. Every step encourages a wave of dust to erupt from the floor, the walls and even the ceiling."

  e "You know, I've got a good feeling about this room. A room like this has to have a key... or a moment... or maybe even booby traps!"

  f "A monument? I think we're more likely to find useless junk like every other room."

  "Eloise pressed a hand to her temple and shook her head gently."

  e "Way to kill a girl's dreams, Finn. Like seriously."

  "Holding his arms out to either side, Finn couldn't help but give her a baffled look."

  f "I'm just being realistic here."

  "Shrugging it off, Finn moved to search the opposite side of the room."

  "Having a spare moment alone - and one not filled with apprehension - Eloise began to wonder about their situation. It's certainly strange, not just where they were but why they were there. Why would anyone want to take them there?"

  e "Hey, Finn? Any idea why we're here? Clues, theories, conspiracies, anything?"

  "Finn doesn't look up from his search, but responds in a suitably clear voice."

  f "If I knew then I'm sure I'd have a lot less to worry about. It's hard to really know anything given the situation. Maybe it's some kind of twisted game. Maybe it's all a dream."

  "Neither party looked back over their shoulder to the other, both continuing to search the room and rummage through any suitable container."

  e "This is all too confusing."

  f "I'm sure you must be scared."

  "Eloise paused momentarily to think about it, and really, she felt more invested in escaping than scared. There was all the thrill of the adventure, even if there was risk to be had."

  e "Well, no. Not really."

  f "Well you're certainly brave... or lying."

  e "It's not a lie! It's just, I know I have someone to watch my back, and we've been making progress since the first few hiccups. Any fear has just faded."

  f "Is that so? Well, I'm glad to hear it."

  "Turning her head around to question Finn directly, Eloise posed the very same question back."

  e "And what about you?"

  "Finn still remained buried in the search, not even giving her a glance."

  f "Fear is a weakness. Fear spreads. To show any in front of you would neither be proper nor beneficial. Is that not correct?"

  e "You act like it's something to be ashamed of. We're just two highschool students, Finn."

  f "Mhm..."

  "Eloise felt that Finn's ambiguous response was nought but dismissive."

  f "Still, I guess I do feel safer alongside you too. Safety in numbers and all that."

  e "It seems like it's the opposite sometimes."

  "Finn shrugged idly while throwing a piece of junk away."

  f "Everyone's entitled to their own opinions."

  "They continued on with nought but their own thoughts for a brief moment until a discovery was made."

  f "Hey, Eloise."

  "Looking over his shoulder to Eloise, Finn waved her over."

  f "Come look at this. Quick."

  "Eloise took a moment to rise to her full height and stride over. She leant over Finn and eyed his find. A locket, simple in decoration but undoubtedly made of proper silver."

  e "Can you open it?"

  "Finn tried to budge it open, making no headway."

  f "I think it's stuck... Give me a moment."

  "After a few moments of wrestling with the locket, he held it up ajar beside the flame of the lighter."

  "Inside was a picture of a girl - neither plain nor fancy, but eerily familiar in appearance."

  e "Who is she?"

  f "Not a clue but don't you think she resembles you a bit?"

  e "Maybe. I don't know. This is strange."

  "Finn casually brushes a finger across the smooth surfaces off the locket, wiping the layers of dust away to reveal a name."

  f "Jeanna."

  e "It's the daughter's name."

  "Looking back to Eloise and eyeing her down, Finn seemed to be trailing a thought. He looked back to the locket and then back to Eloise."

  f "Do you think we were brought here because of the resemblance?"

  e "I'm about ready to believe anything. This was already strange enough without the locket."

  "Flipping the locket closed, Finn gazed off into the distance and made a slow, dramatic motion with his hands as he spoke."

  f "Let's see. Ghosts from a haunted house possessed a couple to find their children. Nice."

  e "You watch too many movies."

  f "Well don't you too? It was just a thought, all the same."

  e "It's creepy enough already, can we just finish looking around?"

  f "Well, go ahead but I know I've hit practically everything of interest on this end and I'm sure it's the same for your end."

  e "Won't know until we've checked for certain."

  "Eloise went back to check the last few items and objects she'd missed."

  e "Empty. Empty. Junk. Empty. Oh, what's this? Looks like another key."

  "Holding the key up to the light didn't reveal much - it was as barren in appearance as the last one and it was impossible to tell which door it matched just by looking at the teeth. They'd have to try it to know for sure."

  f "Well a key is good, but no hammer?"

  e "No hammer. Does this look like a toolshed?"

  f "Hey, who knows? We don't even know what room we pulled that ladder from."

  e "We may as well get to finding the right door."

  "Just as the two had begun walking, Eloise went through all the rooms in her head, trying to think of which might be most befitting to search first. Instead, she recalled that she never had the chance to examine the room her assailant was in."

  e "Hey, I just remembered a room we haven't checked."

  f "Oh? Which one?"

  e "Up the stairs, where I found that lady."

  f "Well, it's certainly free of danger now. Won't hurt to take a look. Just be careful."

  "The two steadily made their way back to the room - a trip made far easier with the faint glow of the lighter."

  "When they arrived, the door was still ajar from Eloise's last visit."

  "Gently pushing the door wide open, Eloise stepped through the doorway and into the room. The room itself looked intricate, with detailed windows and colourful wallpaper, yet the room itself was emptier than her school on holidays."

  "Disheartened, Eloise merely sat down on the floor and remained silent."

  "Finn gave the room a once-over, though whether he made any findings or not, he didn't express them."

  "Within a moment they were out and wandering the halls again, this time having gone back to the floor they'd both woken up on. Now that they actually had a light source to see, the hallway looked so foreign."

  "They checked the first door they came across. It was open."

  "As  they stepped inside, Finn's nose wrinkled."

  f "I think this is the room I woke up in... Judging by the smell."

  e "Guess that saves us the trouble of having to find the key like all the other rooms... Why would anyone need so many locks in their house?"

  f "Dying for privacy, perhaps?"

  "The room appeared to be a study, though the decaying plaster and furniture gave little of the studious air it must have once had. The windows were completely boarded off without so much as a gap. The lighter was the only method they have of scanning the room in any detail."

  f "I'm not sure we'll find anything of use in here... I checked what I could when I woke up."

  e "It won't hurt to try."

  "Finn gave an idle shrug."

  f "No, it won't. Take the lighter, I'll stay on lookout."

  "The second the lighter was in Eloise's hand Finn was off to the doorway - eyeing down the hall like a hawk."

  "Eloise stumbled her way around the room. It was a complete mess, as though someone had taken every piece of furniture up against the wall and given it their all."

  e "The tenants could sure learn a thing or two about redecorating. This place looks my room look tidy."

  "Glancing back from his watch at the door, Finn piped in."

  f "Do you need a hand?"

  e "No I'm fine. Besides, I'm sure we have different definitions for \"useful\"."

  f "Just say the word if you need anything."

  e "You stay on watch for now, mister."

  "Eloise continued her search, but the more she went on, the more and more defeated she felt. They'd been present for hours and while they'd made commendable successes they still had no way out, no ideas, nothing at all beyond room after room to search - each as dark and ruined as the last."

  e "Finn."

  "Looking away from his post, Finn gave a little \"hmm?\" in response."

  e "Do you think we can make it out alive?"

  "Finn's answer was immediate."

  f "There are many possibilities. How things will end I can't say."

  e "You know, I've remembered something I told to someone when they were at the darkest time in their life."

  "There was a moment of silence, punctuated solely by Eloise taking a breath."

  e "Just keep smiling and believe. Everything will be fine. Keep smiling and nothing can go wrong."

  f "When you say it, I have to agree. I'm sure we'll be fine. I'm sure we'll make it out of here together."

  e "Thanks."

  "Giving the room one last check, Eloise finally gave up on finding anything of value within."

  e "Alright, that's it. I don't think there's anything to find here."

  "As she turned to Finn, she sees he's absent from the doorway. In fact, he was right beside her, grabbing her by the arm and hastily pressing her up against the wall by the doorway."

  f "Shhh."

  "As confused as she was, Eloise doesn't dare speak up. She knew Finn's reaction could mean only one thing."

  "Danger."

  "Eloise quickly doused the lighter and tried to hold her breath steady."

  "Finn precariously leaned himself over to see as much of the hallway as possible without risking their position."

  "Trying to lean around him to get a glimpse at what's going on, Eloise made sure to maintain as small a silhouette as Finn had. She could faintly hear what sounded like dragging."

  "She could barely see it, but there was a man wandering through the dark hallway. As her eyes adjusted, she could make out his features in a little more depth, though a lot was left to her imagination."

  "Whatever had happened to the man, his face seemed disfigured, dotted with what she assumed were stitches. His eyes seemed unfocused, darting around this way and that as though he were permanently on edge."

  "What was more disturbing however, was what the man held in his hand. He was dragging someone along the ground by their hair. It looked to be a boy in his teens, noticeably bound in bruises and open cuts and leaving a heavy trail of blood behind as he was pulled along the floor. He put up no resistance, and seemed by all accounts to be dead."

  "At least, that was Eloise's assumption until she saw the boy's head roll to look towards their hiding spot. His pupils seemed to affixate on her specifically. It was an eerie sensation, looking into his dead eyes, only to know that in there he was still alive. It was like looking at a doll - a mere parody of the living."

  "Eloise repeatedly told herself that it was simple coincidence. That he couldn't see them hiding there. All the same, she felt the needed to gasp - a notion that was quickly cut off by Finn covering her mouth and pulling her back from the doorway."

  "Holding a finger to his own lips to suggest silence, Finn made sure they were both out of sight."

  "Together they waited."

  "And waited."

  "They could hear the man walking down the stairs, though it quickly died down to nothing."

  "Together, Finn and Eloise peered around the doorway. The hallway was completely empty as they'd thought."

  "Eloise had the disturbing thought of what might happen if the man discovered the woman who'd met her end on the stairs further down."

  "Her thoughts had little time to process, as if on cue, they heard a horrible shrieking noise from the wood downstairs - as though it ahd been broken through, or suffered a massive strain. Along with it were a collection of crunches and various other more organic sounds."

  "Then there was pure silence save their own panicked breaths."

  "Slowly creeping into a stand, Eloise can't pull her eyes away from the stairs. As she speaks, her voice trembles."

  e "Do you think just believing will be enough?"

  "Finn's own voice was a whole lot more stable, but still noticeably shaky."

  f "I hope so."

  e "And if it's not?"

  f "We'll just have to take that chance."

  e "We should move while he's down there."

  f "Agreed."

  "The two began to move in the opposite direction the estranged man headed."

  "As they progressed, Eloise noticed that she was still wearing Finn's jacket from before the ordeal. She had it off after a little shuffling."

  e "Finn, here. It's your jacket. I've been wearing it the whole time."

  "Finn looked a little puzzled, perhaps he'd even noticed and just not commented."

  f "Won't you be cold?"

  e "I think I'll be alright. All this movement and tension is enough to work up a sweat... and it's a bit big for me. Makes it a little inconvenient to run."

  f "If that's the case..."

  e "I'll be fine. Really. Here."

  "Having taken the jacket gingerly, it took Finn about a minute before he finally decided to put it on."

  "Eloise checked the next door. It was unlocked."

  e "Should we check this room?"

  "Even though she was facing away from him, Eloise could hear Finn sigh. The silence sure makes it easy to catch every little sound and gesture."

  f "I went through that earlier. It's pretty much empty."

  f "Beyond that I think the only other room up here is the one I found you in."

  e "Doesn't seem like we'll find much up here. I can't say I'm eager to head back downstairs, but it might be our only choice if we want to escape."

  f "We just need to be extra careful."

  e "Right."

  "They carefully made their way back down the stairs, being cautious every step of the way."

  "Eloise could feel her heart thump harder and harder, expecting them to turn a corner and see the grotesque man right before them. Encountering another danger only reminded her of how grave their situation really is."

  "Each step had her legs shaking and struggling to balance. Each moment only added more nausea to her already queasy state."

  f "Eloise?"

  "Eloise half jumped at the sound of Finn's voice. Her heart beat furiously."

  e "F-Finn? What is it?"

  f "What's wrong?"

  e "Nothing... I'm just thinking."

  "It was obvious to Finn that she was lying. Her voice was shaking horribly and her body followed suit perfectly."

  f "Are you sure you're fine?"

  "Nodding nervously, Eloise did her best to swallow and regain some composure."

  "Finn reaches a hand out, and squeezes one of hers gently."

  f "Believe. We can do it. I'm here for you."

  "It wasn't a matter of whether she wanted to or not, holding Finn's hand put Eloise at ease and she didn't resist when he took hold of hers."

  "Finn led Eloise down the rest of the stairs and noticed his feet were trailing in something damp. He pulled out his lighter and noticed that there was a rather large helping of bloody footprints paving the hallway floor. They had to have come from the man."

  "Together they follow the trail, despite their better judgement, and find the path of bloody footprints stops in the middle of the room."

  f "You see it, right?"

  e "It's not like he can just fly away... I hope."

  f "There has to be something here."

  "Finn crouches down and analyses the floor carefully, lighter pressed against the ground."

  e "Anything?"

  f "Looks like a door hidden in the wood panelling. There's no locks so just give me a moment to get a good grip on it."

  "Finn cracked open the trapdoor in the floor with a little effort and revealed a lengthy, narrow passage downwards. There was a ladder attached to one wall. He glances back up to Eloise."

  f "It's going to be a tight fit... but if we want answers then the deeper we go the better."

  "Eloise voiced her opinion with a simple nod. As much as she was reliving her earlier terror, she knew the old saying of \"no pain, no gain\" as well as the next person."

  "The ladder proved to be shorter than expected, with Finn able to hop down after only climbing two meters or so underground."

  "Eloise decided to take it easy and climbed her way down the full length of the ladder. From her position at the bottom, she could see they were in a small, damp corridor."

  "It appeared there were only two rooms they could see from here but the hallway made a corner a little further down. Everything seemed a whole lot newer than the rest of the house."

  e "What is this place?"

  f "Some kind of basement? No, it's much more than just that."

  e "I don't think we should be here."

  f "I agree. This could well be the biggest discovery we've had so far though."

  e "Let's see what we can find."

  f "Be careful. He must be down here too."

  "Approaching the closest door, Eloise bit her lip as she began to slowly push it open. Surprisingly, the door was silent as it swerved on its hinges - either this area was far better maintained or was far more recent than its looks gave credit to."

  "The air from within wafted out into the hallway and it was practically caustic. The rotten food was bad, but this was far worse."

  "As the door swings fully ajar, Eloise is exposed to the scene within. She wished it were something she never saw. It was indelible."

  "There were corpses... or what remained of them. They were strung up carelessly from the ceiling, hanging off of meat hooks and anything else that could hold them. It very much resembled a twisted butcher's shop with the prize meat being that of people."

  "Each and every person has been skinned, many others had their organs spilling out of their chests or stomachs. Each and every one of them took whatever mutilated form it could with what scraps of flesh and bone it had left."

  "The worst part of all, is that they were moving. Their eyeballs twisted to stare Eloise down - when they weren't erratically shooting from wall to wall - and their limbs twisted in an impossible effort to let themselves down."

  "Eloise wasted no time shutting the door and getting the hell out of there."

  "She headed straight for the ladder back up, giving Finn no mind at all."

  "Finn was instantly off the moment he saw Eloise running. He checked behind himself to see if Eloise was being chased, but, seeing no-one, realised he'd better stop her before she got too far away."

  "As Eloise began climbing the ladder, Finn wrapped his arms around her waist and cautiously - but forcefully - pulled her away from it. He takes a number of blows as Eloise struggles and tries to escape his grip."

  f "Eloise, calm down!"

  e "No, no... No no no no!"

  f "Eloise!"

  "Her struggle lessened as she buried her face into her hands,. The more she tried to avoid it, the more her mind's eye concocted it again. As panic enveloped her she lost her ability to breath, sucking in air in large, gaping breaths."

  "Eloise collapses onto the ground, head in hands, eyes darting every direction one moment and clenching shut the next. Her breathing is beyond erratic even from what Finn can hear of it over her mumbling. By all accounts she seems to be lost."

  f "I'm sorry..."

  "Finn pulls Eloise in close, into a tight embrace, and presses his lips gently against hers for a soft kiss. To Finn, her lips were as delicate as a flower and sweet as vanilla. It was oddly comforting given the situation."

  "However crazy the idea was, Eloise seemed to be distracted by it, focusing her eyes back on him and regaining some control of her breathing and her movements. Her eyes only widen again as she realises what he's doing."

  "Finn pulls his lips away, giving Eloise's a last, gentle caress as he moves back."

  e "Finn?"

  f "Are you okay?"

  e "...Better... I-... What just happened?"

  e "Am I dreaming? Hallucianting? I have to be..."

  f "It's just..."

  "Finn looked away as he took a breath."

  f "Something I wanted to do before I left."

  "Swallowing back his words, Finn sinks onto the floor opposite Eloise. He turns away, and rubs at his neck idly, though whether distracted by his own thoughts or just plain anxious, Eloise couldn't say."

  f "I figured that it might help you calm down..."

  e "You're a bad liar."

  f "I'm sorry."

  "Eloise sighed as she pressed her forehead to her knee."

  e "Don't be. It's okay. Thank you."

  "As if the atmosphere weren't already heavy enough already, it felt as though everything were made of lead to them now. There were no smiles. There was no laughter. Just the two of them stewing in their own thoughts."

  e "I'll tell you how I feel after we escape."

  f "Huh?"

  e "So... we have to survive this."

  f "I promise you we will."

  "Finn managed a gentle smile. It was easy to see the cheer in his eyes and as much as it could seem forced given their depressing location, it seemed genuine."

  "As he picks himself up, he offers a hand to Eloise."

  f "I promise we'll get out of here."

  e "Yeah, me too."

  "Noticing how much more determined Finn looked now, Eloise couldn't help but feel encouraged and inspired to escape as well."

  "By all means she was still aware of how much danger they were in, even more so after her most recent discovery, but it certainly felt like both of them had some baggage lifted off their shoulders."

  e "Let's keep looking around down here... but Finn, can you please check ahead for me. I can't.. I can't bear to see something so horrid again."

  "Finn gave a firm nod before the two began heading down the hallway. Finn checked the door opposite to the one Eloise did, and gave a shake of his head as he reported it as completely empty."

  "Eloise trailed about a meter behind as they headed for the corner just ahead. Finn made the corner first and froze upon the spot."

  e "Finn? What's there? Why are you-"

  "Eloise catches herself as she realises they must have just come across their assailant. She turned the corner despite the chill running up her spine. While she already knew it was a worst case scenario, she had to see."

  "There was the man, covered in stitches as she'd thought, and a whole lot taller and more muscular than she'd been able to tell earlier. It's hard to ascertain what expression he's trying to portray - anger, amusement, lust even."

  f "Eloise, run."

  "Finn's eyes are locked with the man's, though the way Finn shakes betrays his disposition."

  f "Eloise. Run."

  "Eloise grabbed a firm hold of Finn's sleeve, gritted her teeth hard and gave him a cold stare."

  e "This is no time to play hero. How can we both make it out alive if you die here?"

  "Before Finn had the chance to respond he threw Eloise backwards as the man took a lunge at them both. Finn narrowly managed to duck out of the way as the man slammed a knife against, and into, the floor."

  "Obviously the floors and walls were not quite as up to specification as they looked, but the man clearly held considerable strength as well."

  e "Finn!"

  "Grabbing Finn again and trying to tug him away with her, Eloise is only pushed away again as Finn throws her away from another attack. The knife is plunged firmly into the wall this time, though it was mere centimetres from lodging itself into something else."

  "While their assailant is busy dislodging his knife from the wall after his most recent swing, Finn turns to Eloise and smiles."

  f "Smile and believe."

  e "Damnit, Finn!"

  "Eloise is pushed away from yet another attack while Finn continues to struggle with their attacker."

  e "You better come back!"

  "Not knowing whether it was the right thing to do or not, Eloise took flight and headed back for the ladder. She kept climbing higher and higher within the building, trying to get as far away as possible and winded up finding herself in the very room she woke up in."

  "She slammed the door behind herself with every ounce of strength she still has and moves two pieces of broken furniture to block the doorway. With nothing else left to do, she collapsed against the wall, head in her hands, and tried to rack her brain over what to do."

  "Guilt ate at her as she tried to tell herself she did the right thing."

  e "I traded my friend for a few minutes."

  "Her teeth sinked into her bottom lip so deep it was about to burst into an open wound."

  "She was displaced from her thoughts by a sudden scream from below. It was impossible for her to tell who it belonged to, but her mind instantly raced to all the horrible things that could have happened. Maybe he lost an arm or a leg or worse. She could only hope that Finn was still breathing."

  e "I have to do something!"

  if (KnifeFlag == 1):
    jump lbl_haveKnife
  else:
    jump lbl_noKnife
    
  #(if have the knife)
label lbl_haveKnife:
  "Eloise remembered she still had the knife from earlier. It was all she needed to know that she could save Finn."

  "She gripped it firmly by the handle, quickly adjusting herself to its feel and weight and gave it a quick examination. She could already feel the adrenaline flowing through her body. The idea of ending a life was enough to make her sick, but she told herself it was for the greater good."

  "As she was about ready to charge back downstairs, the ruckus she could hear stopped. She felt as though her own heart stopped with it."

  "There was somebody on their way after her. They'd just made it up the ladder and were moving towards the stairs now. Eloise knew she had no time to lose. She placed herself against the wall beside the doorway, knife held firmly in her hand."

  "The footsteps approached the door. The handle twitched and turned and then shook violently. The door banged against the furniture that held it closed."

  "Feeling a cold sweat run down her brow, Eloise tightened her grip on the knife further, and poised herself to strike at a moment's notice. There was silence. Dead silence."

  "A blade pierced straight through the door from the other side, tearing a hole right through it. The blade is drawn back and thrust through the woodwork again and again."

  "After a few good strikes, the man starts pulling the door apart with his bare hands. It was barely a few seconds before he had torn a hole large enough for Eloise to easily jump through."

  "Eloise saw this as her chance. As the man reached out to tear another chunk of the door away, she swung the knife straight at his hand making a deep cut. It took him barely a moment to pull his hand away after that."

  "Eloise took a look through the gaping hole in the door to see her attacker stumbling backwards, clutching at his hand."

  "With her assailant bewildered, Eloise leapt through the doorway and scrambled her way through the hall and back downstairs. Unfortunately, it didn't take long for the man to recover and he was hot on her tail."

  "She trails through the house, taking the second staircase down further still, back towards some of the first rooms she'd explored with Finn. Her assailant swung his knife back and forth at any opportunity he had as he followed behind her. One slip would surely be fatal."

  "Running low on breath, and losing her ability to rationalise, Eloise began to slow to dangerous levels. To make matters worse, she stumbled into a dead end."

  "She knew the man was overly forceful and lumbering, and knew her best bet was to use speed against him, but there was no time to make any mistakes now. She had to do this quickly."

  "Barging into the room, the man instantly charged towards Eloise and took a swing. Much like she expected, his movements were forceful, but slow, and she stepped aside, causing him to embed his knife in the plaster wall."

  "She knew this was her chance, that she had to attack him now while he recovered."

  "She lifted the knife up and prepared to plunge it down, deep into her attacker's flesh, only, as she was about to swing downwards, he turned around and knocked her aside with his bare hand, knocking her squarely on to the floor a distance back."

  "He'd left his knife lodged in the wall, and was in no way dissuaded by the fact Eloise was armed."

  "Doing her best to recover from the last hit, Eloise found herself locked into a constant pattern of dodging the man's attacks. She was running out of energy, and each weave left her weaker and less agile to the point some swings were clipping her, making instant bruises."

  "Eloise took a wild gambit and swung the knife toward her assailant once more, an attack that she realised was all too well telegraphed too late. The man knocked the blade out of her hand and quickly backed her into a corner all within a second or two."

  "Somehow, the fact she'd been spared - for now - left Eloise all the more horrified than if she were struck by a fatal blow."

  "She tried to back away but could only find solid wall behind her. The man loomed closer and closer, and she knew she was done for. She closed her eyes tight as she awaited whatever cruel fate was hers."

  qq "Not a chance!"

  "The sudden voice caught Eloise's attention, and had her open her eyes just in time to catch the events as they unfolded. A club - formerly a broken table leg - comes slamming into the man's head, sending him stumbling away disorientated."

  "Eloise lunges for her knife, visible even in the dark thanks to its reflective blade and quickly buries it into the man's stomach. The lack of hesitation horrifies her, at least until she tells herself that there was no other way."

  "The man stumbled backwards as fresh blood poured from the wound opened in his stomach. He clutched at the knife, tearing it out gruesomely only to have his entrails follow it."

  "In his efforts to remove the blade he'd only made the wound so much wider. He fell to the ground, twitching and squirming for but a few moments before he stopped and remained completely still."

  "Eloise and Finn surveyed their handiwork, both intrigued and horrified by the man's death until they came back to their senses and turned to each other."

  e "Finn!"

  f "It's over now..."

  "Immediately embracing Finn, Eloise buried her face right into Finn's chest, her arms wrapped tight around him. She was certain that something had happened to him - to see him alive is pure bliss."

  "Her mind wanted to tell her it was all fake, but she could feel him - real and solid - and knew he was really there."

  f "I've got you."

  e "Thank god... Thank god."

  "Without so much as a warning, Eloise began pumelling her hands into Finn's chest and against his shoulders."

  f "Ow. Hey!"

  e "How dare you make me worry like that! How dare you!"

  "Eloise couldn't stop the tears rolling down her cheek. She also couldn't stop hitting Finn."

  f "Hey, look- Ow! Stop! Ouch! Okay, okay, let me explain!"

  e "No! I don't want to hear anything from you, you big liar!"

  f "Eloise, calm down."

  "Finn's voice drops to a whisper."

  f "Please."

  e "...Hmph."

  f "I managed to get away and make it down to this floor. I noticed he stopped tailing me after I was up the ladder, I could only assume he'd gone after you. I figured I had a moment to get a weapon, so I grabbed whatever I could."

  f "Moments later, I heard him chasing you down here. Thank god I was fast enough."

  e "I heard a scream!"

  f "It wasn't mine. I managed to jab him."

  e "With what?"

  "Finn looked away for a moment, rubbing his neck idly."

  f "Pocket knife. It's a family thing... I don't know what happened to it afterwards, though."

  "As much as she'd question Finn taking such a thing with him on a school trip, Eloise knew his family was very strict about their personal protocol, questionable or not."

  e "I'm just so glad you're safe."

  f "I'm still waiting to hear something from you."

  "Eloise pouted."

  e "The deal was that we get out of here first."

  f "Oh right. I think we've rid ourself of the former tenants, so the basement might hold some answers for us now."

  e "Yeah... just please check the rooms first."

  "When they returned to the underground passage, further exploration revealed that it was attached to a sewer."

  "With nought but a lighter to lead them, it was a lengthy and nerve-wracking journey - and the smell was none too pleasant - but after a long trek, they finally come across a ladder to the surface."

  "Wherever they were now, it was a long distance from where they had been before. As certain as she is that they would not be able to see the place of their capture, Eloise decides it as best not to look back. Distancing herself from the bad memories became her primary goal."

  "It was difficult, but she managed to suppress their little 'adventure', instead focusing on her friends, on her promise to Finn. They noticed that the exit they came out of wasn't too far from the camping grounds."

  "They could see the cabins a short distance away, glowing in the rising sun and, despite their weariness, make the trek over, hoping to return with their absence unnoticed."

  "Of course, being a camp, rising early was the norm, and when they return they're scolded for wandering off. Finn covered by referring to is as a simple morning stroll, and they got off without too much ear, but it was still the last thing they wanted after the prior night."

  "Unsurprisingly, Tag and Kelsey weren't worried in the slightest, figuring that they'd woken up early and taken a walk, even if it was unusual for Eloise."

  "If only they knew what had actually transpired, but, aside from how difficult it would be to believe, Finn and Eloise saw no reason to recall the events."

  "Things go back to normal, the camp resumes without issue and it almost feels like it was all just a bad dream. It felt strange how typical everything was after that."

  "Finn was not fond of studying abroad, but knows he has no choice in the matter. He still expressed his desire to stay to his friends, though, with their encouragement and with Eloise's promise to be his girlfriend upon his return, he felt he could stomach it."

  "Eloise truly lived her life, trying to appreciate every single after that. Even so, she still found herself plagued by those same dreams, and found herself wondering what they could mean. Were they merely imagination? Her mind playing tricks? She felt like there was something she'd forgotten."

  "In those dreams, someone kept asking her:"

  "Would you rather live in blissful ignorance, or face the brutal truth?"

  #Innocence // Happy Ending #1
  return
  
  #(if doesn't have the knife)
label lbl_noKnife:
  "Eloise realised she had nothing, no weapons, no tools, nothing to give her any advantage. At most she had a few pieces of broken furniture, all too flimsy to really use bar those she'd blocked the door with."

  "She knows she won't survive unless she does something. If she was unable to help Finn, then maybe it would be best to hide instead."

  "Scanning the room, she spotted a predominantly intact wardrobe. Wasting no time, she headed straight for it and climbed inside, closing herself within. It was dark, it smelt mouldy, it was damp, but she knew she had nowhere else to hide."

  "She sat down, arms wrapped around her legs trying to wait it all out. Let it all pass so she could go and find Finn."

  "Only, it doesn't."

  "There was a horrid scream from the lower levels. She was unable to tell who it was from, but all the same, she knew it was more likely to be Finn than anyone else. Her heart practically froze in place leaving her in nought but silence."

  "Before too long, she heard the sound of heavy footsteps approaching from down the hallway. She knew she was in incredible danger, but didn't know where to go, or what to do."

  "Her whole body shook with fear as someone started beating against the door. By the sounds of it, they began to tear it to pieces, casting away the chunks of wood as though they were nothing and then pushing aside the furniture that barred their path inside."

  "Eloise couldn't stop herself shivering. She couldn't stop herself whimpering. She realised that, while her hiding place may have been the only one in the room, that was also the problem."

  "She couldn't bring herself to move."

  "The footsteps approached the wardrobe, heavy and lumbering as ever. She could hear the heavy breathing of her assailant, knowing that, no matter how hard she tried, she couldn't tell herself that it was Finn coming to save her."

  "The doors were thrust open, and only now was Eloise able to muster the courage to try and flee. She leapt to her feet to scramble away, but found herself struck in the right shoulder by the knife blade."

  "It had gone straight through and was embedding her against the back of the wardrobe. All she could do was scream, for pain, for horror, for what she knew was sure to come."

  "The knife was forcefully removed from its place in her shoulder, though the damage seemed enough that she may never move her right arm properly again - she certainly couldn't right now."

  "Again she tried to run, but the man grabbed her by the shoulder - her right shoulder, causing immense pain - and threw her to the ground."

  "As she looked back up towards her attacker, trying to shield herself with her one good arm, she could see he was already preparing to bring the knife down upon her."

  "In that last moment, she thought she saw someone run up behind her attacker, but what really happened she'd never knew. She could feel the moment the blade pierced through her neck and nothing after that."

  "Nor would she ever again."

  #Angel at the End of The Road // Dead Ending #2
  return