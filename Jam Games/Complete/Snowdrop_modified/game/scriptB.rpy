
  #"END OF DEMO"
  #"Post Demo:"

label chapter2_postDemo:
  show archer neutral at right#(ArcherNeutral.png) next to Anjali"
  #"
  "Speaking of Archer..."

  #"
  "He walks in as if on cue with his arms crossed over his chest. Turning to Anjali, he nods appreciatively. "

  #"INSERT: A24.ogg "
  ar "Thank you for your hospitality."

  show anjali smile

  #"
  "Her smile is laced with sincerity. Ugh...the two of them are so cordial to each other. It's like they're at some kind of party that I'm not invited to. "

  an "Of course! Here, I've brought you some hot chocolate with whipped cream. Please do consider sitting with us. Or, you can make yourself at home in one of the back rooms."


  #Play SE: A25.ogg "
  ar "I seemed to have a decent internet connection in the room I was in. I'd like to stream a movie, so I might just stay back there. Thank you for your offer."
  #Stop SE:"

  #"
  "Anjali hands Archer his drink. He takes a large sip of it before thanking Anjali again for the kindness and concern. Not once does he look at me, which is fine I guess. I didn't exactly come out here to impress the likes of him. "

  #"
  "Yet...I feel bad. Wait, why do I feel bad about his rejection? I think I need to clear my head. I don't need his approval, what am I thinking...?"

  li "Actually, I think I'm going to head to bed too if that's alright. It's kind of late."

  #"
  "I stretch my arms over my head and let out a large yawn. Maybe it's the warm atmosphere in this room, but I want to cuddle up under a large blanket and write. "

  #"
  "I say my goodnight to Anjali but only give Archer a slight nod that he doesn't acknowledge. Still feels kinda sucky but....whatever, I guess. That's not something I can fix overnight. "

  #"
  "Tomorrow is another day, and hopefully it's full of rainbows, butterflies, and whatever else is supposed to represent happiness. "

  hide archer
  hide anjali

  scene bg black with fade

  scene bg NightBedroom
  show lilah happy at left
  #"
  "My bed is wonderful. I've cuddled up under a big blanket with my laptop perched comfortably on my lap."

  #"
  "I begin typing. I'm not incredibly inspired, but I've been in the habit of writing daily. It helps me get the word count I'd like, and then I edit all of the jumble when the story is done. "
  show lilah neutral at left
  #"
  "Tonight, I only get a few words in before I put my laptop to the side. My thoughts keep returning to everything that's happened today. "

  #"
  "Archer Lane. "
  show lilah sad at left
  #"
  "I wasn't being unreasonable earlier when I interacted with him, was I? I mean, why else would he be giving me the cold shoulder? I'm not the picture perfect image of hospitality like Anjali is and I understand that. "

  #"
  "It's just harder for me to be so calm, collected, and...cheerful. I can't ignore the burden of the past on my shoulders like Anjali can. I don't mean to wallow, I just..."


  #"
  "I guess I can worry about the whole thing tomorrow..."


  scene bg black with fade
  stop music
  #"Show Image: chapter1for 1.5 seconds"
  play sound sound_phone
  scene bg NightBedroom
  show lilah sad at left
  # "
  "I'm awoken from my peaceful slumber by the sound of the phone ringing. It's not my cellphone, but  the landline that Anjali has set up in the kitchen. "

  #"
  "At first I try to ignore it, but the ringing is incessant. So, I have no choice but to drag myself out of bed. "

  scene bg kitchen
  show lilah neutral at left
  play music music_home
  #"
  "The floor is ice cold. I remember Anjali telling me that Riversone can get absolutely frigid. Right now, I want to curl up in my blanket and close my eyes. But, that won't get the phone to stop ringing, will it?"

  li "Hello?"

  #"
  "I'm sure that I'm slurring my words as I adjust to the real world. "

  an "Good morning! Did you sleep well?"

  #"
  "Anjali sure is chipper this morning. "


  li "Morning. The bed was comfy. I'd actually like to sleep more though."

  an "No can do, Cadet. I need you down here at the barracks."


  show lilah sad at left

  #"
  "At the mention of the word cadet, my chest tightens. Craig and I used to play soldier all the time. He was the energetic sergeant and I, his unwilling pledge. "

  #"
  "He used the title of cadet when referring to me because he saw it in some movie once, and admitted one day when we were both much older, that he thought it'd make me more willing to participate in his training regimens. "

  #"
  "I'm sure Anjali knows this. This reminder of Craig is also a reminder that I'm not the only one hurting. One of us is just better at holding herself together than the other. "



  #"
  "But, I shouldn't let small triggers ruin my day. Craig would not want that. "


  an "Lilah?"


  #"
  "I've been silent for too long. Oops. "


  li "Er, sorry...it might be the connection. You want me there now?"

  an "In a bit. I'm making breakfast in the Inn's kitchen. Will you be joining me?"

  show lilah neutral at left
  li "Oh, I can join you. That'd be really nice."

  an "Ok great. Come on over. After we eat, I'll show you what you have to do today."

  li "Ok, see you soon."

  #"Only if player chooses not to give Archer the contract earlier:"
  if flag_BringAgreement == False:

    an "Wait, before you hang up...I just want you to know that I gave Archer the agreement after you left last night."

    #"
    "Ugh. I had actually forgotten about that."
    show lilah sad at left

    li "Did he say anything stupid?"

    an "Lilah, come on now. Be nice."

    li "So then, he just accepted the document without a single remark? That's hard to believe."

    an "Uh...not exactly. But he was relieved to have your cooperation."

    #"
    "I can imagine why he'd be relieved. Though, now I'm even more on edge. Not that I anticipate breaking his agreement, but the pressure of what could happen if I slip up is immense. "

    #"
    "I don't really want a lawsuit filed against me. That's definitely not what I want to think about on my first day of work. "
    
  #"Common"
  show lilah neutral at left
  #"
  "Anjali and I say our goodbyes before I hang up. It will be nice to eat with her. I haven't had the chance to do that in a long time, and never one on one like this. "

  #"
  "I think we've all been avoiding each other: Anjali, my mother and I. It's just a hunch, but I think Anjali's decision to stay out here on her own has to do with her honoring Craig's wishes for their future."

  #"
  "Riversone is only a few hours away, and Anjali never comes to visit us. We don't leave the city to see her either. What does that say about us? "

  #"
  "We're not bad people. I know deep deep down in my heart that at least she and my mom aren't. Maybe Anjali doesn't want to see my mother the way she is now. Frankly, I don't want to either. "

  #"
  "I promised myself that this wouldn't be a trip about Craig. At the very least, I shouldn't be spending my first day of work full of melancholy. I need to lighten up! "

  #"
  "Today, I feel like wearing something simple. I quickly get changed and head over to the Red Turtleneck Inn. "

  scene bg brown1
  play music music_home
  #"
  "I pass through the empty lobby, and a sudden realization hits me. It really is only me, Anjali, and Archer in this place. I'm not used to the peaceful energy. Everything is so high strung back home in the city. "

  #"
  "I'm careful to be quiet so that my footsteps don't wake the angry beast upstairs. It's too early to deal with his smart mouth. "

  scene bg corner

  #"
  "Anjali has her back to me when I first enter the small room. She looks hard at work. I fight back the thoughts from earlier that are resurfacing. "

  show lilah happy at left

  li "Morning."

  show anjali smile

  #"
  "Anjali looks up at me with a sweet smile, unbothered by my thoughts. Then, I remember that I haven't voiced them, thankfully. "

  an "Just in time. Last night after you left I wasn't tired, so I made some paratha. I just reheated it for our breakfast."

  li "Yes! I love your paratha, Anjali! Thank you!"

  #"
  "Anjali brings the flattened bread over to me. It smells really good! "

  an "My mother taught me how to make this, so you should be thanking her."

  #"
  "She places a piece from the top of the stack onto a plate and slides the porcelain across the table to me. I grab a seat and wait for her to sit down across from me. "

  an "I made this at least twice a week for your brother."

  #"
  "I nod as I take a bite. I can see why Craig liked this dish so much. It's simple yet delicious. The flaky texture and warm temperature makes it easy to scarf one piece down and reach for another. "

  #"
  "Food. Food is a good distraction. "

  li "So GOOD."

  an "I'm glad you're enjoying it."

  show anjali neutral
  #"
  "I munch happily as Anjali begins to explain today's duties. "


  an "First and foremost, Mr. Lane is your top priority because he's a guest at the Inn. The customers are always first. You can check the hallway for any dirty linen."
  an "Then, of course, ask if there's anything you can do for him should you two make contact. He's expressed his desire for his privacy, so keep your distance unless he initiates the meeting."

  show lilah neutral at left

  li "So basically, just go upstairs and see if Archer left anything in the hall, drop off some fresh toiletries, and then avoid him? Can do. What's next?"


  an "When everything's said and done, I need you to do inventory. You'll note how much of each supply the Inn is stocked with, and then together we'll purchase the necessary supplies. After that, if it seems like Archer isn't in need of anything, you're free to take off early and do as you please."


  li "Ok, I can manage that."


  an "There is a festival coming up on Saturday. I'm going to give you the day off. Just make sure you finish everything we set out to do."

  show lilah happy at left

  li "Sweet! What kind of festival is it?"

  show anjali happy
  an "Riversone's own Snow Festival. You can eat delicious food and do all sorts of activities. It's really a good time. You can't miss it."


  li "Are you going to come with me?"

  show anjali neutral

  an "I usually hang around a bit if I can get someone to watch the Inn. Usually, we have guests so we can't just lock it up."

  show lilah neutral at left
  li "I can watch the hotel. You go and have fun."


  an "Absolutely not! I go every year. I can miss it once. Besides, I don't know if I like the prospect of you and Archer alone together. "

  li "Hey, what do you mean by that?"

  an "I'm just not too sure what to expect, is all."

  li "You know he doesn't like me, don't you?"

  #"
  "She hides her smile behind her hand, but then quickly shakes her head and tries to look natural. "

  an "It's only been one day. He hasn't gotten to know the real you. First impressions aren't everything, you know."

  li "It's okay, Anjali. I'm a big girl, I know people don't have to like me. Let's change the subject though."

  an "Fine, I really think you'll enjoy the Snow Festival, so I want you to go."


  #"
  "Anjali seems adamant about this and will not take no for an answer. It must be a really fun time. "

  #"
  "So it's only right that she goes and has fun too!"


  li "We can split the day. I can go at night. How long is the festival?"


  an "It's the entire weekend, so we can worry about it when the time arrives."

  li "For now I should finish the task at hand, right?"


  an "Well, if you've finished your breakfast, it isn't a bad idea."


  #"
  "I stand up. "


  li "Point taken."


  #"
  "Anjali begins cleaning up and gently pushes me away when I try to help. "


  an "Go and get a small bottle of conditioner, shampoo, some toilet paper, and towels from the room across the hall."

  hide anjali

  scene bg black with fade
  stop music
  #"
  "Once I have everything, I make my way upstairs. I'm planning a stealthy drop off and pick up. Archer won't even know I've been up there! "

  scene bg brown2
  #"
  "I quietly make my way up the stairs, which isn't too hard if I take it one step at a time. When I reach the top, it's as simple as placing the stuff gently against the wall. There's nothing outside the door which just tells me that Archer is probably sleeping in. Perfect. "

  #"
  "I turn to leave when..."


  play sound music_interlude

  #"
  "A loud noise jolts me out of the peaceful silence. "

  show lilah blush at left
  #"
  "My phone begins ringing uncontrollably. I fumble to stop Thomas De Luca's gorgeous voice from serenading me."

  #"
  "Oh no, I'm an idiot."

  #"
  "I forgot to turn off my alarm when Anjali called me this morning. I was planning on waking up later. "

  #"
  "I finally get the song to stop playing, but the damage has already been done. "

  play sound sound_opendoor

  show archer mad
  #"
  "A disheveled but fully dressed pop star opens the door and is glaring at me as if I have been sent by Satan himself to smite the singer. "

  #Insert: A26.ogg"
  ar "You disturb me with Thomas De Luca of all things. Really? You are seriously not the person I want to be dealing with this early."
  #stop sound "

  show lilah mad at left
  li "A simple thank you would have done fine."

  #"
  "I point to the toiletries and towels I've brought up for him. Archer rolls his eyes and crosses his arms over his chest. "

  #"
  "Come on! Is a \"thank you\" really that hard? "

  #"
  "He can't be this rude, can he? "

  #"
  "Jerk. "

  #Insert: A27.ogg"
  ar "I can't thank a De Luca fan. Honestly, I'm not even surprised you like him."
  #stop sound "

  li "What is that supposed to mean?"

  #Insert: A28.ogg"
  ar "He's mediocre."
  #stop sound "

  li "Are you implying that I'm mediocre?"

  show archer sad
  #Insert: A29.ogg"
  ar "Did I say that?"
  #stop sound "

  li "You didn't have to."


  #"
  "Let's get this off the table, Thomas De Luca has good music. His album \"TDL\" has some of the best lyrics I have ever heard and his voice is not hidden behind all the production that Archer uses on his tracks. "


  #"
  "Archer doesn't apologize. Instead, he begins berating me again. "

  show archer mad
  #Insert: A30.ogg"
  ar "You were to drop off the necessities without bothering me."
  #stop sound "

  li "I was trying, but then you opened the door and started talking to me about my alarm."

  #Insert: A31.ogg"
  ar "Your alarm? You've got to be kidding me."
  #stop sound "

  show archer neutral
  #"
  "He takes in a large breath. "

  #Insert: A32.ogg"
  ar "I don't understand you."
  #stop sound "

  #"
  "He gently pushes me to the side and walks out into the hallway. "

  play sound sound_doorclose

  #"
  "The door makes a loud click as it shuts. "

  show lilah blush at left
  li "Um...what are you doing?"

  #Insert: A33.ogg"
  ar "Leaving. So don't touch my stuff."
  #stop sound "

  show lilah mad at left
  #"
  "I want to yell at him and say that I'm legally barred from even entering his room. But instead, I'm too dumbfounded by the fact that this guy put his hands on me and literally moved me out of his way. "

  #"
  "Urgh! I stop myself from yelling at him when I picture Anjali's disappointed face. "

  #Insert: A34.ogg"
  #Archer "
  "This is going to be a reoccurring thing with you, isn't it? You just stand there and stare at me?"
  #stop sound "

  #"
  "I ignore his comment."

  show lilah neutral at left
  li "Your toiletries."

  #"
  "That's all I can muster, despite wanting to say so much more. "

  #Insert: A35.ogg"
  ar "They're not going anywhere. I'll be back."
  #stop sound "

  #"
  "He actually waves me off and bounds down the stairs with the energy of someone who has just heard some really good news. "

  hide archer

  #"
  "I have no choice but to follow him. The rest of today's duties are downstairs. "

  scene bg brown1
  show anjali neutral
  play music music_home
  an "Ok Mr. Lane, do enjoy your day!"

  #"
  "I just catch Anjali waving at Archer as he walks out of the Inn. Who knows where he's even going."


  an "Everything went well, Cadet?"

  #"
  "I'm snapped out of my daze. "

  show lilah smile at left
  li "Aye aye ma'am."

  #"
  "My hand flies up to my forehead."

  show anjali smile

  an "That's a pirate, but I'll take it. Next up is stock inventory. It's a little boring, but it'll go by quickly with the two of us."

  scene bg black with fade
  scene bg brown1

  show lilah neutral at left
  show anjali neutral
  #"
  "After a few hours, the inventory is finally done. What a drag. "

  an "Alright. You're free to go do as you please."

  li "I think food is a good idea."

  an "I can't leave the Inn unattended. But, you can check out the town a bit. You haven't seen it all, I'm sure."

  #"
  "She holds her hand up in front of me as if to stop me. "

  an "And before you say anything, no I don't mind. Go ahead and have fun."

  li "I was hoping I could eat here, actually. I want to hang outside of the Inn; It's quite beautiful."

  #"
  "I really just want to hang out with her and catch up. We missed out on a lot of time together, and we both know better than anyone that we have to take advantage of what we have. "

  an "That's a good idea. Let me whip something up for us."


  scene bg black with fade
  scene bg patio

  play music music_warmth
  show lilah neutralout at left 
  show anjali neutral with dissolve


  #"
  "It's so peaceful out here on the back porch of the Inn. There are a few tables and chairs spread about the wood deck. Beyond that is the most amazing view of any backyard I've ever been into."
  "I forget my burdens as I stare into the flowers that are surprisingly in bloom. Riversone is a beautiful place and I'm surprised that more people are not clamoring to be out here, especially during the holiday season. "

  an "It's going to snow soon."

  #"
  "I finish chewing and place my turkey sandwich back onto my plate. Anjali added a bit of fresh mozzarella and tomatoes, and it tastes amazing. She has a knack for cooking that I don't think I ever will be able to compete with."


  li "How can you tell?"

  an "It usually happens around the time of the festival, hence the name."

  li "The Snow Festival."

  an "Yep, exactly."

  #"
  "I feel the cold wind caress my face. I'm consumed by the flawless images of nature I see around me. Life is in every leaf and every blade of grass. With life, comes hope. "

  #"
  "There are things out in the world that I just can't explain. Life is...precious."


  an "Dollar for your thoughts?"

  show lilah smileout at left
  #"
  "Huh? Oh Anjali..."

  #"
  "For a second I forget where I am."

  #"
  "A smile dances on my face. Anjali never says penny. She always tells me that my thoughts are worth so much more than a single cent. The dollar is to entice. Then you charge more. "

  #"
  "She always says that my thoughts are worth an incredible amount. She has an interesting outlook on life."

  #"
  "Anjali wasn't born and raised in America. She's originally from Pakistan where her father owned a small business and her mother took care of the finances. She's one of two children who have left their homeland for better educational opportunities. "

  #"
  "In a cramped classroom with more students than desks, Anjali met my brother. Craig was smiling behind the cover of an overpriced Calculus textbook when he saw her enter the room. Or, at least that's the way he always so fondly told their love's origin story. "


  li "I just love it out here. Being from the city, the most foliage you see in one place is in someone's backyard or a park. The open wilderness is so much different. I feel so relaxed."

  an "Ah, yes. Living in the big city and commuting always felt like such a drag to me. Being out here with nature is what I live for."


  li "I'd like to take Marina around in this huge open space."

  show anjali smile

  an "Aw, how is the little girl?"


  li "Not so little anymore! She's like 35 pounds."

  #"
  "I reach into my jacket pocket for my phone so I can show Anjali a picture of my dog. But when the smartphone is in my hands, I start to think of Archer and his scowl from this morning. "

  show lilah sadout at left
  li "Hey, uh- do you know who Thomas De Luca is?"

  show anjali neutral
  #"
  "She ponders the name for a minute as my heart drops into my stomach. I don't know why I'm feeling this way, it's strange."

  an "My gut is telling me he's a singer."

  show lilah neutralout at left

  li "Your gut would be right. He's fairly new on the scene, but he's really good."


  an "So, what about him?"

  #"
  "I think about telling her what happened earlier with Archer but decide against it. It isn't important, and Anjali might just tell me to be nice or something. I know it's the right thing to do, but sometimes I can't help myself"


  li "I was just wondering. I like his music a lot."

  an "I'm curious to know if you're a fan of Archer's music. Personality aside, is that the kind of music you like? I feel silly asking that. I know that I should know but..."

  li "There's no reason for you to have known. It's been awhile."

  #"
  "A silent remark of forgiveness. I don't want her to feel as if we're two worlds away. "

  li "I'm not his biggest fan. I think his music can be fun to listen to sometimes but there's something missing. I don't know. It's kind of generic. I think he courses through with his looks mostly."

  show anjali smile
  an "He is quite attractive."

  #"
  "Anjali winks at me and I roll my eyes. "

  an "Perfect for a single lady like you."

  li "Ew. No. Just...no."

  #"
  "Anjali laughs lightly but shakes her head. "

  an "If famous, hard-to-deal-with celebrities aren't your thing, what is?"

  #"
  "I pause for a moment to think. It doesn't much matter to me the kind of person I date, as long as they're passionate about something and they treat me right. I just want to be loved like Craig loved Anjali. "

  li "I'm not really looking right now."

  #"
  "Instead of telling her what I'm thinking, I shut the conversation down. Love is something I'm not opposed to. Some time down the line I'm sure I'll be open to it."
  #"
  "But right now, I'm having a hard time imagining myself committed fully to another person. I have too much of my own life that I need to figure out. "
  
  show anjali neutral
  an "And you have no reason to be. I was just curious."

  li "I'd tell you if I had my eye on a handsome gentleman, but I don't. Right now I want to make sure mom is okay. Then I can worry about having another person in my life. Even coming out here was hard. Part of me was afraid to leave her on her own."

  an "This trip will do you both good."

  li "I really hope so."

  hide anjali

  scene bg black with fade
  scene bg park
  show lilah neutralout at left
  play music music_autumn
  #"
  "When we're done eating, Anjali insists I take a walk around Riversone. So, I decide to visit a park where I can sit down and get some writing done. I need a new idea. "

  #"
  "I'm really intrigued with the idea of a character modeled after Archer. But, I know for a fact that violates his terms of staying at the inn. The idea, though, won't leave my head. "

  #"
  "Famous pop star at a small inn in the mountains. All I have to do is give the character some motivations that are deeper than just hiding from paparazzi. Writing this script would be such a great outlet because I feel like I'd be able to insert some of myself in there. "

  #"
  "The famous pop star in my story could be running away from something like I am. They could be using the solitude to try to sort themselves out. "

  #"
  "The more I toss the idea around in my head, the more I like it. Though, I have to throw this one in the trash bin. At least for now. I can't really afford giving my life savings to Archer in some kind of settlement case."

  #"
  "My fingers begin to feel numb. I have been typing for at least twenty minutes, and the cold is finally catching up to me. I'm sitting on a bench in the mostly vacant park. There is someone clearing out the trash bins, but besides that it's just me out here. "


  #"
  "Well, it is a Tuesday afternoon; everyone must still be at work and school. Plus, it is rather chilly out. Maybe people are indoors by the fire. "

  #"
  "Rubbing my hands together generates some warmth. It's not a lot, but probably enough for me to keep brainstorming. I now have an elderly woman character with a fleshed out back story. "

  #"
  "Information broker hiding behind the guise of a widowed and grumpy old woman who preys on young girls for their bad manners. That woman on the train won't sue me...probably. Now, all I need is a conflict. "

  #"
  "Is she lonely? Or maybe it's something different. She has no money left but wants to quit her dangerous job. Oh, or a hitman is after her!"

  show lilah sadout at left
  li "Ugh!"

  #"
  "It's no use. The footsteps approaching aren't loud, but for some reason, I can't focus when I hear them. For a second, I see blonde hair poking out from the bottom of a beige beanie. "

  show lilah blushout at left
  #"
  "Archer! He doesn't seem to recognize me. The man is in his own little world as he walks through the park. "

  #"
  "What do I do? Should I say hello or try to avoid him?"

  menu:
    "Hide":
      jump chapter2_hide
    "Wave": #( + Archer)
      $ archer_score += 5
      jump chapter2_wave

label chapter2_hide:
  #"Hide:
  show lilah neutralout at left
  #"
  "I don't want him to see me. He's definitely not going to come up and talk to me if he does, but I'd like to avoid the awkward eye contact if possible. "

  #"
  "I try Archer's favorite tactic and pull my scarf up over my nose. To cover my eyes, I just look down at my laptop. At least, that way I can pretend I'm working and not have to worry about what to say to Archer. "

  #"
  "I wait a few minutes, and when I finally look up, Archer is gone. Good riddance. Now I can finally concentrate. "
  jump lbl_postHideWave

label chapter2_wave:
  #"Wave:"
  show lilah neutralout at left
  #"
  "It wouldn't hurt to be polite. I know Anjali will appreciate me trying my best. Besides, if I'm a tad bit nicer to Archer, he may be a tad bit nicer to me. That will make my job less painful. "

  #"
  "As Archer passes by me, I wave. I think he notices it because he nods in my direction. No look of annoyance or anything. Is that a score for me?"

  #"
  "I wait for him to pass me by nonchalantly, but he doesn't go on his way. He keeps walking toward me."

  show lilah blushout at left
  stop music
  #"
  " Oh no. What have I done? "

  show archer neutralout #Center screen"
  show lilah neutralout at left

  show animation_heart:
    xalign 0.52
    yalign 0.05
  show animation_heart:
    linear 2 alpha 0.0
  play sound sound_success
  #"Show heart gif for a second"
  #"
  "In a matter of seconds, Archer is standing above me, still no malice on his features. I wave again. "

  #"
  "He doesn't ask me to move over; he just sits down in the empty spot next to me. "

  #Play SE: A36.ogg"
  ar "What are you doing out here? Don't you have a job to do?"
  #Stop SE:"


  li "Not when you're my only client."

  #"
  "I point at my laptop."

  li "I'm writing something."

  #Play SE: A37.ogg"
  ar "Not gonna ask."
  #Stop SE:"

  #"
  "Of course not. "

  li "Why are you talking to me anyway?"

  #"
  "Is this some kind of prank? Archer came up to me to strike up a conversation. "

  #Play SE: A38.ogg"
  ar "You waved me down."
  #Stop SE:"

  li "I was waving to be polite."

  show archer smileout

  #Play SE: A39.ogg"
  ar "So, are you saying that you don't want to talk to me?" #(cocky)
  #Stop SE:"

  show lilah madout at left
  #"
  "His cocky grin makes me sick to my stomach. Who the hell does he think he is? "

  #"
  "Archer Lane. "

  #"
  "That's right. I almost forget for a minute that he's Power Magazine's Most Successful Male Singer of 2018. Archer isn't some regular guy strolling through the park, and he keeps reminding me of that. "

  li "What's the answer that you're looking for?"

  #"
  "No use arguing with him. I've known people like him all my life. Good looking and successful people want recognition of their skills and beauty. I don't really have the energy to goad anyone's ego right now. "


  show archer neutralout

  #Play SE: A40.ogg"
  ar "I'm not looking for an answer."
  #Stop SE:"

  li "Which begs my original question, why are you talking to me?"

  #"
  "I shut my laptop and twist my body to get a better look at him. Archer looks calmer than yesterday, serene almost. "

  #Play SE: A41.ogg"
  ar "Well, I figure that if I'm going to be seeing you everyday, it would behoove me to know a little bit about you,"
  #Stop SE:"

  #"
  "I can't help but question his intentions. Didn't he say that he didn't want me doing anything out of his agreement? Is he just trying to scope me out to see who's working with him? I suppose that makes sense. "

  li "You don't want some stalker going through your stuff, right?"

  #Play SE: A42.ogg"
  ar "Why do you insist upon putting words in my mouth? Did I say any of that?"
  #Stop SE:"

  li "No, but given our past interactions you've done nothing but lead to that claim. So, forgive me if I'm inclined to believe that."

  show archer happyout
  #"
  "I feel that I need to match his formal language. He only laughs though. "

  #Play SE: A43.ogg"
  #Archer #(Amused)
  "One, stop talking like that. It doesn't suit you. Two, you signed the agreement. It's over with. If you go into my stuff, I'll have my attorney deal with it. I'm not concerned about that anymore. I'm really just talking to you."
  #Stop SE:"

  show lilah sadout at left
  #"
  "Maybe my confusion is written on my face because he frowns suddenly. "

  show archer neutralout

  #Play SE: A44.ogg"
  ar "I'm abrasive at times, I'm aware of that. But, am I not reasonable?"
  #Stop SE:"

  #"
  "I simply shrug. I don't have an answer for him. Rather, I don't have one he'll like. It's too early to pass a judgement like that. I barely know the guy."


  li "Maybe I just don't grasp what it's like to be you."

  #Play SE: A45.ogg"
  ar "I don't quite think I understand you either. You're a strange one."
  #Stop SE:"

  li "So I've been told by tons of strangers. You wouldn't be the first."

  #Play SE: A46.ogg"
  ar "It's not necessarily a bad thing."
  #Stop SE:"

  show lilah madout at left
  li "I didn't say that it was."
  #"
  "I kick my feet into the dirt. Our conversation has distracted me from the cold for a few minutes, but now I feel tingling in my toes as they freeze. "

  #Play SE: A47.ogg"
  ar "No matter. We better get inside somewhere. Your teeth are chattering."
  #Stop SE:"

  show lilah neutralout at left
  #"
  "He stands up and offers me his hand, totally uncharacteristic of the man I spoke to this morning. I don't take it. Instead, I place my laptop in its case and stand up on my own."
  " I don't want him thinking that I'm like everyone else. He can't just be nice to me for five seconds, having ignored my presence thus far. "

  #"
  "He needs to know that his actions hurt."


  li "I think I'm going to head back to the Inn."

  show archer sadout

  #"
  "Archer retracts his hand, and for a second I think I see a slight frown. If it was there, it's now masked by his usual unimpressed expression."

  show archer neutralout
  #Play SE: A48.ogg"
  ar "Suit yourself."
  #Stop SE:"

  #"
  "He slightly lowers his head, a gesture to signify goodbye, and walks away from me. "
  hide archer

  #"
  "Some kind of progress has been made between us. Whether it's good or bad, I don't really seem to know. What I do know is that Archer Lane is just a client I'm supposed to tend to. I don't for a second buy his sudden niceness, or rather what he considers to be niceness. "

  jump lbl_postHideWave

label lbl_postHideWave:
  #"COMMON"
  #"
  "Still...I can't stop thinking about Archer. Where does a famous celebrity go for fun? Especially in a small town like this?"

  #"
  "The thought of some kind of second life is exhilarating. Archer is a celebrity posing as a regular person..."

  #"
  "There's more to it than that. There's got to be. He must do this often for no one to even bat an eyelash. There's got to be more than just the big scarf and hat that keeps his identity hidden. "

  #"
  "He's a pro, and there's a story behind that too. If I could just understand his motivations, I could write a compelling character..."

  #"
  "I try to squash that thought. I better leave before it gets too late. No use spending all my time out here thinking about Archer. "

  scene bg bathroom
  show lilah neutral at left
  stop music
  play music music_warmth

  #"
  "I dry my hair off with a towel and throw it up into my usual messy bun. There's not much to do tonight. Anjali has some paperwork to fill out, and I don't think Archer needs my help with anything. A hot shower has warmed me right up, and now I want to do something relaxing. "

  #"
  "When I'm in a creative rut, I watch movies to see how other filmmakers have accomplished their goals. It's inspiring, so I'm always watching movies."
  "Now that I'm away from the city for a bit, I really want to focus on my future, and that includes coming out with some independent films of my own. "

  #"
  "I leave the bathroom in search of my laptop and a comfy pair of sweats. I'll be sitting in the lobby of the Inn, so I don't need an extravagant outfit. "

  #"
  "But, I don't want to wear my pajamas in case Archer is roaming about. That would be totally embarrassing. "


  scene bg librarynight
  show lilah neutral at left
  #"
  "I stretch my legs out across the floor. Anjali has lit the fireplace and brought me a thick comforter and fluffy pillow before returning to what she was doing. She said something about sending out emails. "

  #"
  "I've made myself a comfortable setup. This is what I call relaxation. "

  #"
  "What should I watch? A love story? A drama? A comedy? All three? Oh! Maybe a mystery!"

  #"
  "If I can only get this wifi to connect..."

  show lilah mad at left

  #"
  "After a few minutes of fumbling, I let out a frustrated cry. It's no use, the connection is weak. "


  show archer neutral##Center screen #(the one where he has no scarf or hat on)
  stop music
  #play sound A49.ogg"
  ar "You sound like a dying animal, are you alright?"
  #Stop SE:"

  #"
  "My heart skips a beat. The prince has arrived to ruin my night, and he scared the crap out of me. "

  show lilah neutral at left
  li "I was just trying to stream a movie, but the wifi signal is weak today."

  #"
  "I look up at Archer and see a disheveled man. His wet hair is sticking to his face. His beanie and scarf are lying on the lobby desk behind him, and there are three plastic bags that he's placed on the floor beside him. Yet, he's asking if I'm alright. "


  li "Do you need a towel or something?"

  #"
  "I remember that it's my job to make sure Archer is enjoying his stay. Even if that means getting up out of my comfy seat. "

  #Play: A50.ogg"
  ar "Yeah, please?"
  #Stop SE:"

  #"
  "Urgh okay...."
  
  #"
  "I get up off of the floor and head towards the supply closet where Anjali holds the towels. "

  scene bg black with fade
  scene bg librarynight#(same bg as before)
  show archer neutral with dissolve
  show lilah neutral at left
  play music music_home
  #"
  "When I return, Archer is sitting on one of the chairs looking down at his phone. I toss the towel to him, which he's able to catch effortlessly."

  #Play: A51.ogg"
  ar "Thank you."
  #Stop SE:"

  #"
  "He moves to dry his hair as I awkwardly sit in the chair next to him. What do I do now? "

  #Play: A52.ogg"
  ar "It's snowing out."
  #Stop SE:"

  #"
  "Thankfully Archer breaks the silence because I have no idea what to say."

  li "That would make sense."

  #"
  "I motion to the towel in his hands. It must be a heavy downfall for him to be soaked like that."

  li "Anjali told me that it usually snows around the time of the Snow Festival. Must be holiday magic."

  #"
  "I'm tip toeing with my words around Archer. He hasn't insulted me yet and I don't want to shatter this calmness."

  show archer sad
  #"
  "Archer scoffs."

  #Play: A53.ogg"
  ar "Holiday magic. You don't actually believe in that do you?"
  #Stop SE:"

  #"
  "Despite how bad the holidays can be for my family sometimes, yeah I do. Anything to help me get by."

  li "Why not? You might be in the wrong place. This whole town seems to believe in it. You can't walk a block without seeing a candy cane or something."

  show archer neutral
  #Play SE: A54.ogg"
  ar "I'm not a scrooge, but Holidays have become about spending and making money. There's no magic in that."
  #Stop SE:"

  li "In the big cities maybe, but I don't really get that vibe here. You should go to the Snow Festival this weekend to change your mind."


  #"
  "Actually, that's why I'm going there too. "

  #"
  "I wonder if there's a chance of changing Archer's mind? He has Christmas albums, and I've seen him in Holiday themed commercials on television. It would make sense if that's all a ploy for money. "

  #"
  "In that case, I can see how he would hate the Holidays. Everything he does is probably to sell himself to the public. "

  #"
  "It suddenly occurs to me..."

  li "Is that why you're out here on your own with no publicist or anything?"

  show archer mad
  show lilah sadblush at left

  #"
  "I regret my question the minute I see Archer's face twist in anger. I place my hands up in front of me. "

  li "Forget I asked."

  #Play SE: A55.ogg"
  ar "You didn't read the agreement."
  #Stop SE:"

  show lilah mad at left
  li "I did."

  #Play SE:A56.ogg"
  ar "All of it? Even page 7 section c?"
  #Stop SE:"

  show lilah blush at left
  li "I uh..."

  show archer neutral
  #Play SE: A57.ogg"
  ar "You didn't read it."
  #Stop SE:"

  li "It was really long and non disclosure agreements are self explanatory aren't they?"

  #Play SE: A58.ogg"
  ar "You're insufferable. The agreement concludes with the statement that you will not ask any questions about my personal life."
  #Stop SE:"

  #"
  "Can he even do that? Is that legal?"

  show lilah sad blush at left
  li "Sorry I asked then..."

  #"
  "...And there was the end of an almost golden conversation. "

  #Play SE: A59.ogg"
  ar "Alright, I can't get any wifi either and I don't want to bother your aunt."
  #Stop SE:"

  #"
  "Did he just change the subject like nothing happened?"
  
  show lilah neutral at left
  li "She's my sister-in-law actually."

  #"
  "Archer is a confusing person. I can't tell if he hates me or not. At times, he's tolerable. Others, not so much. "

  #"
  "Archer fishes in one of his bags until he finds what he's looking for. He holds up an old DVD and cracks a small smile. "

  show archer happy
  #Play SE: A60.ogg"
  ar "Got this bad boy for a steal."
  #Stop SE:"

  li "Good Riddance Old King? Dude, that movie is terrible."

  show archer neutral
  #Play SE: A61.ogg"
  #Archer #(in disbelief)
  "What?"
  #Stop SE:"

  li "I don't mind that the movie was filmed in the 70s. I appreciate the camera angles, but the script itself...so cheesy."

  #Play SE: A62.ogg"
  ar "No no. You're not watching it the right way. It's meant to be cheesy. 70s comedy at its best. Put your mind in that time."
  #Stop SE:"

  show archer happy
  #"
  "As Archer talks about the film, I notice the corners of his lips turning up into a vibrant smile. He's a big fan of the movie, and it seems like he's forgotten all about his outburst a minute ago. "

  #"
  "Another side of Archer, this one much more relaxed. How many sides are there? Do I even want to know?"

  #"
  "Here goes nothing. I'm going to ask him if he wants to watch the movie with me since there's nothing else to do. I hope that's acceptable to him. "


  li "Maybe we can watch it?"

  show lilah blush at left
  #"
  "I hold my breath."

  #"
  "Oh, Lilah...why would I ask that? "

  #"
  "I expect Archer to get up angrily, but he doesn't."

  show archer neutral#"
  #Play SE: A63.ogg"
  ar "It's not like there's anything else I planned on doing tonight. Can we use your laptop?"
  #Stop SE:"

  show lilah neutral at left
  #"
  "I nod, completely dumbfounded. The Archer from this morning is gone. In his place is either a really good actor or someone who isn't a complete jerk after all. "

  #"
  "Archer places the disc into the CD tray of my laptop and starts the movie up. The over the top theme music plays, and I can't help but roll my eyes."

  show archer happy
  #Play SE: A64.ogg"
  ar "It's so good!"
  #Stop SE:"

  #"
  "Archer himself is a little over the top, so this doesn't surprise me one bit. He begins humming along to the opening theme and drums his fingers across his thighs. "

  #"
  "I watch him carefully. Suddenly, I don't want to watch this movie anymore. I can't shake the feeling of apprehension. I'm afraid to say anything that might get him angry. "

  #"
  "To me, Archer is the perfect mystery. He's full of intrigue. Yet, I want to not be so interested in his personality shifts. They're more than just his private versus public self being on display. "

  #"
  "Ever since that incident on the train, I've been thinking about his story. I want to tell it. Not Archer Lane's life, but the life of the man sitting next to me right now. The storyline can't get more honest than that."

  #"
  "But then I feel bad. It's a bit like exploitation, isn't it? I don't know if my desire to see into his world is just my cinematic lens talking, if it's because of the novelty of hanging out with a celebrity, or if it's me genuinely wanting to hang out with the guy. "

  #"
  "It dawns on me why he's so guarded, and I hate myself for not seeing it sooner. He's Archer freaking Lane. His public self overtakes his private self. I have the luxury of going home after a long day and being a nameless face among many. "

  #"
  "I don't have to watch what I say or go to the extremes that he does. I can simply sit down and watch a movie like this at home. Seeing how excited he is watching this movie, I wonder if he even gets to really enjoy it in his private sphere. "

  #"
  "I feel even worse now. I'm not justifying his callous attitude, but it makes sense. People want to exploit him, even if they don't quite realize it themselves. "

  #Play SE: A65.ogg"
  ar "Prepare to be dethroned!" #(Exaggerated voice)
  #Stop SE:"

  #"
  "Archer is imitating the man in the movie, obviously forgetting I'm here. He moves his arms in a grandiose fashion, only laughing when he catches my eye. "

  #Play SE: A66.ogg"
  ar "Watch this. It's the best part." #(Amused)
  #Stop SE:"

  #"
  "The man on the screen, Sir William Dansky, stumbles on his lines and fails to deliver his punchline correctly. It isn't 70s comedy, just a low budget movie. The jokes are terrible and the shoddy acting isn't intentional. The actors are simply amateurs."

  show lilah happy at left
  #"
  "The room fills with the sound of Archer's laughter. It's contagious and the laughter leaps out of me. "

  #Play SE: A67.ogg"
  ar "Told you, it's good."
  #Stop SE:"

  li "I wouldn't say that, but okay."

  show archer neutral
  #Play SE: A68.ogg"
  ar "Besides the jokes, what's so bad about it?"
  #Stop SE:"

  show lilah neutral at left
  li "The dialogue isn't as witty as you think it is. Not to mention the acting is just plain bad."

  #"
  "I want to say more, but I stop myself. "

  #Play SE: A69.ogg"
  ar "We're never going to be on the same page, are we?"
  #Stop SE:"

  #"
  "I shake my head.  Archer and I are in two different books completely. He's an anthology and I'm a simple chapter book. "

  show lilah sad at left
  li "I suppose not. We're from two different worlds."

  #"
  "Archer is silent. His gaze is on the screen of my laptop. Even now, with us sitting together, he feels untouchable. "

  #Play SE: A70.ogg"
  ar "We're both from planet Earth. We're both humans."
  #Stop SE:"

  #"
  "Archer's tone is serious. "

  li "That's not what I meant. You made it clear the minute you walked in this lobby that you're a big celebrity, and I am that weird girl from the train who happens to also be a hotel worker."

  show archer smile
  #Play SE: A71.ogg"
  ar "Don't forget about the over zealous girl who followed me in the supermarket."
  #Stop SE:"

  show archer neutral
  li "Point is, we're not on a level playing field."

  #Play SE: A72.ogg"
  ar "Celebrities aren't their own species. We're people too."
  #Stop SE:"

  li "People don't make other people sign non disclosure agreements."

  #Play SE: A73.ogg"
  ar "Should I explain to you again why that agreement is important? I didn't have you sign it to avoid having to see you. It's a safety measure."
  #Stop SE:"

  #"
  "I know that, but still. There's an undeniable distance between Archer and I, regardless of his agreement."

  #"
  "I hold up two fingers. "

  show lilah neutral at left
  li "Two different worlds, buddy. Just accept it."

  #"Archer moves left, Anjali enter to the right- neutral "
  show archer neutral:
    xalign 0.3
    yalign 1.0
  show anjali neutral:
    xalign 0.8
    yalign 1.0
  #"
  "Archer opens his mouth to say something when Anjali enters the room with a smile. She must be done with her work. "

  an "Are you two playing nice?"

  show lilah blush at left
  #"
  "Startled, I nod as quickly as I can. Archer is much more nonchalant."

  #Play SE: A74.ogg"
  ar "For the most part."
  #Stop SE:"

  an "Very good."

  show lilah neutral at left
  #"
  "She peers at the laptop screen and gives us a thumbs up."

  show anjali smile
  an "Is that Good Riddance Old King? What a good movie!"

  #"
  "Archer taps my arm softly. When he has my attention, he motions to Anjali appreciatively. "

  show archer smile
  #Play SE: A75.ogg"
  ar "See? It's a good movie!"
  #Stop SE:"

  an "To our, or at least my, commoner tastes. Lilah is a film connoisseur. She premiered her own movie at a film festival."

  show lilah blush at left
  #"
  "I can feel my face pale. "

  #"
  "Anjali, no! I'm so embarrassed. "

  #"
  "She is telling a man who has appeared in many movies himself that I'm some kind of big shot. All I did was show my work in some small independent movie festival in New York and fail. "

  show archer neutral
  #Play SE: A76.ogg"
  ar "Is that so?"
  #Stop SE:"

  show lilah sad blush at left
  li "Nothing compared to you, oh great one."

  show archer mad
  #"
  "Archer looks angry at what I said. "

  #Play SE:A77.ogg"
  ar "Can't you be serious for one second? A film festival is a big accomplishment. That's your future."
  #Stop SE:"

  show anjali sad
  #"
  "I lower my eyes at Archer. He's right, and it's definitely the validation I need but...I just don't understand this man. Why does he care?"

  #"
  "I shrink away from his attention. My film career is still a sore spot for me. "

  show lilah mad at left

  li "Well you know, it's getting kinda late. I should head to bed."

  #"
  "I stand up and dust off my pants. "

  show lilah neutral at left
  li "You can watch the rest of the movie on your own laptop."

  #"
  "I eject the disc from my computer and hand it back to a disgruntled Archer. I don't mean to sound rude, but it comes out that way. "

  #"
  "What was it Anjali said yesterday? Ah, not everyone understands the hasty nature of a New Yorker. I have to be more patient with Archer, but that's going to take some learning. "

  #"
  "For now, I don't want to talk to Archer about my failure of a creative career. I turn to Anjali. "

  show archer neutral
  li "Need help closing up?"


  an "I've got it."

  #"
  "She's frowning, but I don't want to divulge so much information to a man whom I will never see again. Why does he need to know? "

  #"
  "It is the kind of information I'd discuss with a friend, considering how close to home Snowdrop is to me. Archer and I aren't exactly best friends. "

  #"
  "Not to mention, I don't want to come across as a person looking for doors to be opened for them. Archer more than likely has connections in the film industry. "

  #"
  "He made it abundantly clear yesterday and this morning that I should not cross his boundaries. The last thing I need for him to think is that I'm trying to use him. "

  li "Good night Archer."

  show archer sad
  #Play SE: A78.ogg"
  ar "Night, Lilah."
  #Stop SE:"

  #"
  "The annoyance from mere seconds ago is replaced with a tone of dejection and then a look of realization that spreads across his face. "

  show lilah sad at left
  #"
  "I leave with a heavy heart, but I don't fully understand why. I want to get to know him, but I also know it probably isn't possible. "

  hide archer
  hide anjali
  scene bg transition with fade
  jump chapterThree

label chapterThree:

  show transition_chapter3 with Dissolve(5.0)
  scene bg black with fade

  play sound sound_interlude

  scene bg NightBedroom
  show lilah neutral at left

  #"
  "I wake up to the sound of my own alarm, which startles me because I've grown accustomed to Anjali's early morning wake up calls. "

  #"
  "I check the time, 9:00 am. She let me sleep in?"

  play music music_warmth
  #"
  "Oh, that's right! Today is the Snow Festival, and I get the day off. No having to deal with Archer's superiority complex this morning, which I'm super thrilled about. "

  #"
  "It's like these past few days Archer has forgotten about our movie night. He has gone back to treating me as cold as ice. "

  #"
  "I pay it no mind. It makes more sense to me this way. He is the unruly client, and I the indifferent worker. "

  #"
  "Yet, Archer accepted my offer to watch a movie. Why?"

  #"
  "I keep telling myself that, if I can crack that small code, I'll be so much closer to writing a better script. It's all about life experiences, my film professor used to say. "

  #"
  "Even if it's a fictional story, a good screenwriter always puts what they've experienced in their script. It's why we can relate to even the most absurd movies. "

  #"
  "Is a guy like Archer the conflict I need? And if so, is it worth embracing? Because of his non-disclosure agreement, I have so much at stake. "

  #"
  "What's most important to me?"

  #"
  "I guess it doesn't matter much, considering I'll probably never have the opportunity to show a more appreciative and lucrative audience one of my films. "

  #"
  "It's a stupid idea anyway...throwing myself headfirst into my future career without even fixing the problems I'm facing in the present. Having a good movie isn't going to change anything at all. My world isn't going to magically make sense if I'm successful."

  #"
  "No, I'm looking in the wrong places for my answers. Who cares about Archer's motivations? Who cares about some stupid movie? That's not why I'm here to begin with."

  #"
  "I am dressed by the time I finish my inner monologue. I am more than ready and excited to go to the Snow Festival. I push the negative thoughts out of my mind and gleefully head out into the snowfall. "

  scene bg SnowStreet
  show lilah neutralout at left
  "Possibly a snow overlay? "
  play music sound_peopleambient


  #"
  "Snow pelts my face. I love being out here on the bustling street. It certainly feels like all of Riversone is at the Snow Festival. I see children excitedly tugging on their parent's coats, dogs patiently waiting at their owner's side, and couples both old and young holding hands."


  #"
  "I don't know what to do first. Maybe I can buy Anjali something as a thank you for letting me stay with her at the Red Turtleneck Inn. "

  #"
  "Whether she realizes it or not, she's been more than helpful to me. Anjali offering her place to me in her own time of need and putting herself aside for my well-being shows what kind of person she really is."

  #"
  "Every day, I see why Craig fell for her. Through it all: his deployment, the PTSD, the subsequent sickness...Without her, I don't think my older brother would have held on for as long as he had."

  #"
  "A little gift is nothing compared to what she deserves. It's the least I can do. "

  menu:
    "Check out the Market Stalls":
      $ flag_CheckedMarketStalls = True
      jump chapter3_MarketStalls
    "Check out the food. ":
      jump chapter3_Food

label chapter3_MarketStalls:
  #"Market:"
  scene bg SnowMarket

  #"
  "There are dozens of stands scattered about the big park. I decide to walk down the aisles of shops. Even during flea markets and farmer markets at home, there isn't as much heart."

  #"
  "People are displaying themselves in the art that they're trying to sell. I can appreciate that. I know that it takes a lot of courage and strength to put yourself out there. "


  #"
  "I'm particularly drawn to the small hand carved statuettes that an older gentleman is selling. He sits down behind the table he is using as a display and begins carving a chunk of wood right before my eyes. He looks up with a warm smile. "


  que "I haven't seen you around here before..."

  show lilah neutralout at left
  li "Oh, I'm working in my sister-in-law, Anjali's, Inn. I just got here recently. My name is Lilah."


  que "Ah, Anjali is always a doll. Her paratha is to die for."

  #"
  "He notices my curious gaze and motions for me to come closer and get a better look at the statuette in his hand. It's not complete yet, but it resembles a person."


  que "My name is Willis, and I have lived here for all of my life. In my day, I was a contractor and certified handyman. Now I carve."

  show lilah happyout at left
  #"
  "I see how intricate all of his designs are and know that this is the right gift for Anjali. I just have to find the perfect statue. I can totally see her putting it right on her desk in the lobby of the Inn. "


  li "Your work is beautiful."


  #Willis"
  will "Thank you. Are you interested in any of these little guys?"

  li "Actually, yeah. I want to get one for Anjali."

  #"
  "Willis holds up his index finger. "

  #Willis"
  will "Ah, say no more. I've got the perfect one. And because you're a new customer, I'll give you a discount."

  #"
  "He shows me a small statue of a woman with her hair in a braid to the side. She has her arms outstretched towards the sky. "

  #Willis"
  will "This is the guardian. When I was a child, my mother used to tell me a story about a woman who held Riversone up on her shoulders."

  li "Oh, wow. This is her then?"

  #Willis"
  will "Mhmm, she represents strength and protection. Perfect for Anjali, don't you think? Someone to watch over the Inn."

  #"
  "My brother had a guardian angel pin, and that didn't stop him from being in the line of fire. It didn't stop those bad thoughts from haunting him years later. It didn't stop him from taking his own life. "

  li "Those don't really work, you know."

  #Willis"
  will "Well, they're not magical. They bring a peace of mind to those who own them."

  #"
  "Well, Craig really believed in the little pin my mother got him. It didn't leave his sight. So, whether it works or not, I'm sure Anjali will appreciate the thought. "

  li "I suppose you're right. Anjali will like this very much."
  #"
  "Willis and I talk for a bit before I tell him goodbye. He's a really friendly man and assures me that everyone in Riversone is this way. I'm happy with the statuette he picked out despite the memories it brings up for me. "

  #"
  "Anjali and I are not the same person, and I am positive that it will have her gushing. "

  #"
  "I walk around and enjoy the art on display, stopping only when I hear a voice."
  jump chapter3_MarketContinue

label chapter3_Food:
  #"Food:"
  scene bg SnowMarket

  #"
  "There are dozens of stands scattered about the big park. I decide to walk down the aisle that has the best smelling food. My stomach is rumbling, and I'm itching to taste some of Riversone's local favorites."

  #"
  "My nose takes me to a stall selling waffles. I can see a woman behind the counter mixing the batter. The familiar looking cashier beams brightly at me. "

  cash "Come and try Lady Lacy's homemade waffles fresh!"

  li "Oh, are you guys from Lady Lacy's Sweet Shoppe? My sister-in-law loves your gelato."

  cash "Well, it is the only place you can get homemade ice cream in Riversone."

  li "The only place?"

  cash "Yeah, this place is pretty small. I recognize you from the other day. Are you new here? Just visiting?"

  li "My sister-in-law, Anjali, owns the Red Turtleneck Inn. I'm staying with her for a few months."

  #"
  "The Cashier's smile grows even wider at the mention of Anjali's name. "

  show lilah happyout at left

  #"
  "It's infectious, and I find myself smiling as well."

  cash "Oh, how is she doing? Is she going to stop by the festival?"

  li "She's doing well, but I'm not sure if she's going to stop by because there's not that many people working at the Inn this month."

  #"
  "The cashier holds up her finger as if she has an idea. "

  cash "She's a doll. Please give Anjali this waffle- on the house. I'm giving you two. One for her and one for you. Any newcomer just HAS to try this. You'll be coming back for more."

  li "That's so nice of you. Thank you so much. Anjali will definitely appreciate it."

  cash "Just tell your friends about us!"

  show lilah neutralout at left
  #"
  "The cashier waves, and I head off with the waffles in hand."

  #"
  "I scan the area and find an empty table not too far away. Sitting down on the cold metal is slightly uncomfortable, but I can't wait to taste these homemade waffles. I hastily unwrap the foil and place the waffle on the table."

  li "So good!"

  #"
  "I can't help but exclaim when I taste the dessert. The waffle is topped with brown sugar and laced with cinnamon. The warm center is just perfect in this weather. "

  #"
  "It's not long until I finish the waffle and place Anjali's in my bag. I stand up, ready to see what else the festival will offer. "
  jump chapter3_MarketContinue

label chapter3_MarketContinue:
  #"COMMON"
  stop music
  
  show lilah neutralout at left

  #Play SE: A79.ogg"
  ar "Following me again?"
  #Stop SE:"

  show archer winterneutral  #Center screen"
  #"
  "I turn to see Archer standing behind me, hands on his hips. His face is once again hidden beneath his scarf and hat. "

  li "You're behind me, so you must be the one doing the following."

  #Play SE: A80.ogg"
  #Archer #(sarcastic)
  ar "Wow, cute."
  #Stop SE:"


  li "I thought so."


  #"
  "Archer stares at me for what feels like hours. It's kind of uncomfortable being under his gaze. So, I'm thankful when a loud voice breaks the silence. "


  que "All who wish to participate in the snowman building contest please sign up by the left field! The contest is for pairs so please, teams only!"

  #"
  "Someone is shouting about a snowman building contest. It must be great fun to watch.Though, Archer doesn't seem to share the same sentiment. "

  show archer wintermad
  #Play SE: A81.ogg #(insert later)
  ar "Are we children?"
  #Stop SE:"

  #"
  "Archer's negativity is a damper on the holiday spirit. I don't know...something about his disbelief makes me want to cheer him on and help him get his spirit back. Christmas is a great time if it's not marred by terrible memories. "

  li "I don't see why we can't watch."

  #Play SE: A81.ogg"
  # Archer #(annoyed)
  ar "We?"
  #Stop SE:"

  li "Relax, it's just a phrase. I'm going to watch it. You don't have to come."

  show archer winterneutral
  #"
  "Archer is wearing his infamous scowl, and I can only roll my eyes. "

  li "Remember how we talked about you coming to the festival to get more in the spirit?"

  #Play SE: A83.ogg"
  ar "I recall, which is why I'm here...and pleasantly surprised. The people here seem to be proud of what they do."
  #Stop SE:"

  li "And they should be. This is all so incredible. A lot of people have put themselves on display. It's really a festival of inspiration."

  show archer wintersmile
  #"
  "Archer seems pleased by this statement. "

  #Play SE: A84.ogg"
  ar "Got some ideas for a script?"
  #Stop SE:"

  #"
  "That's right. Anjali mentioned to Archer that I'm interested in making films. "

  li "There are a lot of interesting characters in Riversone. It's hard not to want to pick up a pen and jot a bunch of things down."

  show archer wintersad
  #"
  "Archer frowns, and for a moment I notice something. He's hesitating. Did I strike a nerve?"

  #"
  "No. I must be imagining things. "

  li "Anyway, I'm going to be watching the snowman building contest. I'll see you back at the inn."

  #"
  "I turn to leave when I hear Archer trying to get the last word in. "

  show archer winterneutral
  #Play SE: A85.ogg"
  ar "Have fun with your childish games."
  #Stop SE:"

  li "You know, I bet you're just saying that because you know you'll never win."

  #Play SE: A86.ogg"
  ar "With my creative genius, a simple snowman will be almost mundane."
  #Stop SE:"

  li "Prove it."

  #Play SE: A87.ogg"
  ar "I would, but it'd require me to find a partner."
  #Stop SE:"

  #"
  "I point to myself as if it's obvious. "

  show lilah happyout at left
  li "Hello! Me!"

  #"
  "Archer shakes his head. "

  show lilah neutralout at left

  #Play SE: A88.ogg"
  ar "No, I can't work with a De Luca fan. You have bad taste."
  #Stop SE:"


  li "I bet you my taste wins us the contest."

  #Play SE: A89.ogg #(to be inserted later) "
  ar "Fine, let's make it a bit more interesting then."
  #Stop SE:"

  #"
  "I raise a brow. "

  li "What did you have in mind?"

  ar "If I win, you have to show me one of your movies. It can be a short clip. I don't care."

  #"
  "This has to be a trap somehow. Why does he want to see my work? "


  li "No way."

  #Play SE: A90.ogg"
  ar "I knew it. You don't think you can win."
  #Stop SE:"

  show lilah madout at left
  #"
  "I glare at him intensely. "

  li "Of course I can win! I'll participate in your little bet. But if we win because of me, you let me see your room."

  show archer smileout
  #"
  "He seems more amused by my statement than anything. Er..."

  show lilah blushout at left
  li "Wait! No. I didn't mean that."

  #Play SE: A91.ogg"
  ar "So you didn't just ask to see my bedroom?"
  #Stop SE:"


  li "No, I did but....I just want to get a glimpse of it."



  #"
  "I realize that didn't make it any better. I just want to get a better idea of who Archer is. They say you can figure out who someone is by seeing the place they live in. In this case, the closest I'll get is Archer's room. "

  #"
  "His bedroom is the only thing he doesn't share with the public. I kind of want to see what the real Archer is like..."

  #"
  "He sighs. "

  li "I know! I know! You don't understand me."

  #Play SE: A92.ogg"
  ar "I guess as long as you don't do anything weird, it's fine."
  #Stop SE:"

  show lilah neutralout at left
  li "Or violate the agreement. I got it."

  scene bg black with fade
  scene bg SnowPark
  #"Archer and Lilah should be set to Neutral"
  show lilah neutralout at left
  show archer winterneutral
  stop music
  play music music_foreverfriends

  #
  "Archer and I head over to the park where the contest is being held. He looks around in awe. "

  #Play SE: A93.ogg"
  ar "How does this much snow fall at just the right moment? It doesn't make any sense."
  #Stop SE:"

  li "Holiday magic, buddy."

  #"
  "Archer looks unconvinced. This man is such a killjoy sometimes. "

  li "Maybe it usually snows around this time, so the people of Riversone know when to plan their festival. Or, maybe the name of the festival means something other than the obvious celebration of snow having fallen."
  #"
  "Archer rolls his eyes but doesn't respond. Okay, so maybe there's no reason good enough for him. I don't know why I keep getting surprised."

  #??? "
  que "Last call for sign ups! People of all ages welcome!"

  show archer wintersad
  #Play SE:A94.ogg"
  ar "Is it too late to back out now?"
  #Stop SE:"

  li "No, but we did walk all the way here."

  show archer winterneutral
  #Play SE: A95.ogg"
  ar "Fair enough."
  #Stop SE:"

  #"
  "Archer, er...Irving Prince, and I sign up for the intermediate level snowman building contest. Apparently there are multiple levels. Junior is for children only and advanced is for people who go as far as carving the snow. "

  show lilah madout at left
  li "See! Not for kids!"

  show lilah neutralout at left
  #"
  "Archer rolls his eyes but begins packing snow. The rules have already been explained. All we have to do is build the best snowman using things from the park in only 30 minutes. "

  #Play SE: A96.ogg"
  ar "Hey, if you don't stop talking, we won't even finish making this damn snowman."
  #Stop SE:"

  #"
  "I stick my tongue out at him and drop to my knees to begin packing the base of our snowman as well. "

  #"
  "Archer is very methodical with his actions, focusing on building the snowman up quite literally. He points to the ball of snow in my hand. "

  #Play SE: A97.ogg"
  ar "No moving pieces. Build the whole thing from the base."
  #Stop SE:"

  li "Yeah, but it'd be easier to pack bigger chunks of snow than to do it your way."

  #Play SE: A98.ogg"
  ar "What? No it wouldn't. The snow you packed could break."
  #Stop SE:"

  li "But your way will take too long, and we won't finish in time."

  #"
  "He stops long enough to glare at me. I want to wipe that stupid look off of his face. In fact..."

  #"
  "I look down at the snow in my hands and then back up at Archer. I kinda want to throw some at him. Oh man, should I do it?"

  #"Choice: "
  menu:
    "Throw Snow":# [+ Archer
      $ flag_snowballFight = True
      $ archer_score += 5 
      show animation_heart:
        xalign 0.52
        yalign 0.05
      show animation_heart:
        linear 2 alpha 0.0
      #(should be off of the screen before the sound finishes)
      play sound sound_success
      jump chapter3_ThrowSnow
    "Don't Throw Snow":
      #"Don't Throw Snow:"
      "I drop the snow onto the ground. Maybe it's better if I don't agitate the guy. Archer looks at me, and I just shrug. "
      jump chapter3_AfterSnow

label chapter3_ThrowSnow:
  #"Throw Snow:"
  show lilah happyout at left
  #"
  "Oh, I'm so gonna do it. "
  #"
  "Before I can talk myself out of it, I toss the large chunk of snow at Archer's covered face. "

  #"
  "He looks startled for a moment before standing up. Then, he leans down and grabs a fistful of snow. "

  show lilah blushout at left
  li "Don't do it."
  show archer winterhappy 
  #"
  "I try to warn him, but he steps closer and launches the snow at me. It splatters across my face. The powdery snow is so cold but I am not backing down. "

  show lilah madout at left
  li "It's so on!"

  #"
  "Archer pulls up his scarf as if realizing he's out in public, and shakes his head."

  show archer winterblush
  #Play SE: A99.ogg"
  ar "Uh...wipe your face."
  #Stop SE:"

  show lilah neutralout at left
  #"
  "I use my scarf to dry up the remnants of snow around my face, but it does nothing to warm me up. Being with Archer like this, even I forget that he's a celebrity. Maybe an all out snowball brawl isn't the best idea. I don't want people to recognize him. "

  show archer winterneutral
  #Play SE: A100.ogg"
  ar "At the inn, when we don't have to worry about all this..."
  #Stop SE:"

  #"
  "He motions to his face."

  #Play SE: A101.ogg"
  ar "I will crush you."
  #Stop SE:"

  li "I doubt it, but you can certainly try."

  #Play SE: A102.ogg"
  
  ar "I'll have you know, my hand eye coordination is top level."
  #Stop SE:"

  li "On what scale?"
  jump chapter3_AfterSnow

label chapter3_AfterSnow:
  #"Common"
  #"
  "Just then, as Archer is about to say something, I catch the sight of a judge from the corner of my eye. She walks by our partially formed snowman. Then, placing a hand under her chin, she stares at the two of us."

  judge "You two are falling behind the others, but there's still time to catch up. Lilah Scott and Irving Prince correct?"

  #"
  "After I nod, the woman looks down at the clipboard in her hands and then gives us an exaggerated smile. Like I haven't seen one of those before."


  judge "Newbies always take this competition for granted, but we have some really good prizes. So, try your hardest."

  #"
  "Huh? Did she just say that people take this competition for granted? Maybe I misread how serious snowman building is in Riversone. "

  #"
  "Archer is unamused with her passive aggressive tone, and rightfully so."

  #Play SE: A103.ogg"
  ar "We're not interested in any prizes."
  #Stop SE:"

  judge "Even front row tickets to the tree lighting in the town square? Because, those are a hot commodity. I mean, you're welcome to stop by anyway next weekend but these tickets put you in the best spot."

  show archer wintersmile

  #"
  "Archer smiles, and I know it's because he could get those tickets easily if he exposed who he was. I'm kind of glad that he isn't the kind of person who flaunts his fame around."
  "There's a lot of ways that Archer has proven that he can be a jerk, but it isn't because he throws it in someone's face that he's rich and powerful. "


  #"
  "After all, he's in this small town instead of a more lavish and flashy place. Another curious thing about him that I want to learn  more about."

  show archer winterneutral
  show lilah blushout at left

  #"
  "Archer raises a brow when he looks at me. I look away quickly, as if he could read my thoughts."

  #Play SE: A104.ogg"
  ar "You want those tickets, don't you?"
  #Stop SE:"
  #"
  "Oh! That's what he's getting at. Good."

  #"
  "But now that I think about it, I do want those tickets. Well...I mean, not for me. For Anjali! It's totally not because I never ever get to see the tree lighting in New York City up close. Nope. Not for me. "

  judge "Everyone in Riversone does. On top of that, you get a gingerbread village baked by Lady Lacy herself! So try your best. There's still some time left to fix this mess."

  show lilah madout at left
  #"
  "While our snowman is barely a snowman, really just a foundation, it is by no means a mess. "

  #"
  "Though looking around, I notice that most of the snowmen from the other contestants are already two thirds of the way built. "

  show archer wintermad
  #Play SE: A105.ogg"
  #Archer #(with some disdain)
  ar "I think we'll manage. Thank you."
  #Stop SE:"

  #"
  "When the judge leaves, I can't help but bite my lip and rub my gloved hands together. "

  show lilah neutralout at left
  li "Snowmen competitions are serious business here."

  show archer winterneutral
  #"
  "Archer's expression is serious. His gaze in on the woman's retreating figure, but his words are towards me. "

  #Play SE: A106.ogg #(to insert later)
  ar "I don't like to lose, Lilah."
  #Stop SE:"

  li "I don't imagine you're used to it, either."

  #"
  "Which may be why he hates Thomas De Luca for stepping onto the scene and questioning his spot at the top of the pop artist pyramid. "

  #Play SE: A107.ogg #(to insert later)
  ar "Of course not. I suggest we put aside our differences for the time being and win this competition. We're both creative individuals; we can do it."
  #Stop SE:"

  li "Maybe, but it might be nicer to see you taste some humble pie. You know, seeing you lose might be better than those tickets to the tree lighting."

  #Play SE: A108.ogg #(to be inserted later)
  ar "My pride can take the hit."
  #Stop SE:"

  show lilah happyout at left
  li "Can it?"

  show lilah neutralout at left
  #"
  "Despite my jovial tone, I lean down into the snow and pick up a fistful once again. I toss it in my hands and try to look as serious as I can to Archer."


  li "Okay, let's do it. But if we win, those tickets go to Anjali."

  #Play SE: A109.ogg"
  ar "I'm not against that. The woman is a saint for putting up with you."
  #Stop SE:"

  li "Me? Right, because I'm the one dealing with you."

  #Play SE: A110.ogg"
  ar "And I'm the perfect guest. There's hardly any work you need to do."
  #Stop SE:"

  #"
  "I ignore his remark and instead redirect him to our snowman. "

  li "I know you said no moving pieces but we're better off having someone build the base and the body, and then having the other do the head separately. We'll save some time."

  #Play SE: A111.ogg "
  ar "Fine, go for it. But the face is the money maker so don't make it an ugly snowman."
  #Stop SE:"

  li "We just need to make it distinct! You build your base, and let me worry about the details, okay?"

  #"
  "Archer and I have called off our bet in favor of working together to make the best snowman. Apparently, Archer doesn't like coming in second place, and those tickets might be the best gift I can give Anjali. So, it's a win-win situation for both of us. "

  #"
  "Besides, seeing him so intensely motivated about  something he thought was for children makes me smile. "

  #"
  "Archer builds up the base quite nicely. He pats around the sides, making both the base and the abdomen of the snowman perfectly round. "

  #"
  "I don't know how he manages it, but Archer's style is very meticulous. "

  #"
  "The head I'm holding in my hands is much more rough. It has edges that I can't seem to smooth down."

  #Play SE: A112.ogg"
  ar "Place it on top, and then we can decorate."
  #Stop SE:"

  #"
  "Archer looks so focused, and I'm honestly shocked when he doesn't make a rude remark about how my work is much less perfect than his."

  #"
  "He helps me place the lump of snow firmly on top of our snowman and then gets to work on patting down the sides. I watch him in awe. Archer tackles every single imperfection. "

  #Play SE: A113.ogg"
  ar "Give her some features. A face, a nose, some hair?"
  #Stop SE:"

  li "Oh, she's a her?"

  #Play SE: A114.ogg"
  ar "Mhm. A strong independent snow woman."
  #Stop SE:"
  
  show lilah happyout at left
  show archer winterhappy 
  #"
  "I can't help but laugh, and Archer winks at me. It's so sudden that I just stare at him for a few seconds, trying to convince myself of what I've seen. "
  show archer winterneutral 
  #"
  "He totally didn't just do that...right? No, he couldn't have..."


  #Play SE: A115.ogg"
  ar "Well?"
  #Stop SE:"

  #"
  "His voice pulls me out of my daze. "

  li "So uh...hair, eyes, and a nose. Maybe a scarf and some arms!"

  #"
  "Rules state that anything in nature can be used to construct the snowman. It's easy to find some rocks lying around for her eyes and some sticks for her arms. But there isn't much else besides snow that I can see around us. Still, it doesn't hurt to make a quick sweep of the area. "

  scene bg black with fade
  scene bg SnowPark
  show lilah neutralout at left
  show archer winterneutral 
  #Play SE: A116.ogg"
  ar "Do you think we can use sticks to outline a shirt?"
  #Stop SE:"

  #"
  "I see Archer holding a stick up to the chest of our snow woman when I return. He tilts his head, trying to figure something out. "

  li "Do we have enough time to fill it in with some stones? It could be like a sweater. We just push the stones in the front and the back."

  #Play SE: A117.ogg"
  ar "I don't see why not. I like it better than the stick idea. Do you want me to get the stones?"
  #Stop SE:"

  li "You have a better eye for this kind of thing than I do. Plus, I don't want to mess up the perfect round snow woman we've made. Too much pressure."

  #"
  "I give him what I have, and as he positions the arms onto our snow woman I search for as many stones as I can. There isn't much, but we're able to create a striped pattern on both sides of the snow woman. "

  #"
  "When the bell for time rings, we both step back. I'm actually happy with what we've created. The snow woman has on a nice striped sweater and has some thick hair made from sticks."

  show archer wintersmile
  show lilah happyout at left
  #Play SE: A118.ogg"
  #Archer "
  "I can't believe I'm going to say this, but we made a good team today."
  #Stop SE:"

  li "I did good for a De Luca fan, huh?"

  #Play SE: A119.ogg"
  ar "You should be a Lane fan."
  #Stop SE:"

  li "If we win, I will be."

  #"
  "I've forgotten how much fun it is to actually build a snowman. I haven't built one since I was a child. I remember seeing the snow falling from our apartment window and rushing to Craig's room and him yelling at me for waking him up."

  #"
  "But, he'd get up every single time and bring me outside to build a snowman. I'd pull my snow boots up over my pajama pants, and mom would make sure I had on at least three layers of jackets."

  #"
  "There wasn't ever much room in front of our building, but the superintendent never minded that we used the little bit of sidewalk that we had. "

  #"
  "But, in this moment, I've built a snow woman with Archer freaking Lane. Who would have thought?"

  show archer winterneutral
  show lilah neutralout at left

  #"
  "Archer pulls out his cell phone and snaps a picture of our piece of art. "
  #Play SE: A120.ogg"
  ar "Too bad I can't upload this masterpiece."
  #Stop SE:"

  li "Will everyone really be able to find you if you do? What are you so worried about?"

  #"
  "This time I don't apologize for my question, and Archer doesn't seem so irritated by it. "

  show archer wintersad
  #Play SE: A121.ogg"
  ar "Last year some woman and her friends broke into my home and posted pictures of all my stuff on her social media accounts. People were able to find my address, and I had to move after that."
  #Stop SE:"

  show lilah sadout at left
  li "That's not right. I'm so sorry."

  #Play SE: A122.ogg"
  ar "It is what it is, I guess."
  #Stop SE:"

  li "No, it isn't! People shouldn't be such jerks! You have a right to your privacy, the same as any other person."

  #"
  "We're interrupted once again by the judge who is giving us a fake smile."
  #"
  "Urgh! Right when Archer was opening up! "

  show lilah neutralout at left
  show archer winterneutral

  judge "Gorgeous work, you two. I'm shocked that you're newbies if I'm being honest with you. Definitely top three."

  show lilah blushout at left
  show archer wintersmile
  li "Top three!?"

  #Play SE: A123.ogg"
  ar "Did you doubt me?"
  #Stop SE:"

  show lilah neutralout at left
  #"
  "I roll my eyes at him. "

  li "Maybe."

  judge "Your boyfriend is cocky, but I guess it's within reason. This snow woman is a strong contender. You guys worked well with what you had."

  show archer winterneutral
  #"
  "I wait for Archer to correct the woman on her comment about him being my boyfriend but he doesn't. Though, I do notice his playful smile falter. "

  #"
  "The judge writes some things down on her clipboard before walking away to judge another team. "

  show lilah happyout at left
  li "Thanks for entering the contest with me. Even if we don't win, I had fun."

  show archer wintersmile
  #"Play SE :A124.ogg"
  ar "Me too, surprisingly."
  #Stop SE:"

  show lilah neutralout at left
  show archer neutralout
  #"
  "When the judge calls the teams over to announce the winners, Archer and I are shocked to see that we made second place. Me, because I didn't think we'd score so high, and Archer, because he didn't think he'd score so low. "

  #"
  "We did get a consolation prize, a gift card to Leighton's Grocery, which we both agreed to give to Anjali. "

  #"
  "Archer and I part ways from here. He's highly competitive, but I'm happy to have seen a new side of him. He was actually pleasant to be around today."

  #"
  "I decide to head back to the inn so that Anjali can visit the Snow Festival for a bit. "


  scene bg brown1
  play music music_home
  show lilah neutral at left
  #"
  "When I enter the Inn, Anjali is typing away on the keyboard behind the counter. She looks up at me."

  #
  show anjali neutral
  an "Back so soon?"


  #
  li "Yeah. Long story, but Archer and I entered a snowman building contest together."

  #"
  "I don't tell her about the gift card just yet. It'd mean more to her if Archer and I both gave it to her together. "

  #
  an "How did that happen? Are you two friends now?"

  #
  show anjali smile
  li "We've silently agreed to coexist."

  #"
  "Anjali laughs. "

  #
  an "Silently agreed to coexist, I like that one."

  show anjali sad
  #"
  "She looks down at her computer and then back up at me with a slight frown. "

  #
  an "I feel sort of bad for that boy. He pushes people away. You can see it in his eyes- just when someone gets too close."

  #
  li "Close to scratching the surface you mean."

  #
  an "Maybe that's close to him. He has different standards than regular people."
  show anjali neutral
  show lilah sad at left
  #
  li "I've noticed. Different worlds."

  #
  an "No, no. That's where you're wrong. We're all in the same world. He just has different terms and conditions he has to check off."

  #"
  "I ponder that for a moment. Archer is a person with feelings, struggles, and worries. He just has to pretend they don't exist. He can't rant and complain like Anjali or I can. That makes him distant."


  #"
  "It actually makes some sense..."

  show lilah happy at left
  #
  li "That's it!"

  #"
  "Anjali raises her brow curiously at my outburst."

  #
  an "What's it?"

  #
  show anjali smile
  li "I've got to write this down!"

  #"
  "This character Archer is playing masks his true self, and I might have figured out why. Maybe he's not a jerk. I just have to figure out who he really is. Another challenge accepted. "

  #"
  "I hastily look around for a piece of paper. Anjali lets out a small laugh and slides one over to me with a purple pen. "

  #"
  "I scribble down my thoughts until finally I'm content with my fleshed out breakthrough. "

  #
  an "Next big film?"
  show anjali neutral
  show lilah neutral at left
  #
  li "I really hope so."

  #"
  "Anjali puts the pen back and deposits my folded up piece of paper in a draw behind her. "

  #
  an "Just be careful. You signed that nondisclosure agreement..."


  #
  li "I would never do anything to jeopardize Archer's privacy. I'm not like those other girls."


  #
  an "Those other girls?"


  #
  li "Er, forget it. Just something Archer said to me earlier. Anyway, I came home early so you can go to the Snow Festival. Please go. "


  #
  an "You didn't have to. I already told you that I've attended the festival a million times."


  #
  li "I know but still! There were some people asking about you."


  #
  an "Really?"


  #
  li "Yeah, look. I got you a gift from their booth."
  show anjali smile


  #"
  "I reach into my bag and get the gift that I obtained earlier for Anjali."

  #"If player went to food earlier:"
  if flag_CheckedMarketStalls == False:
    #
    an "Lady Lacy's homemade waffles? I love these so much."

    show lilah happy at left
    #
    li "The cashier wouldn't let me leave until she made one for you."
    show anjali smile


    #
    an "That was probably Lacy's daughter, Lana. They're both extremely kind people. I must thank them."
  else: 
    #"If Market: "

    #
    an "Oh! A little statuette! Is this from Willis' booth?"


    #"
    "She looks ecstatic at the little statue that I purchased from WIllis. I'm happy she likes it. "

    show lilah happy at left
    #
    li "Yep! I thought you'd like to have this beauty watching over you. Willis calls it 'The Guardian'. Do you know the story?"
    show anjali neutral


    #
    an "Of course I do. He tells me it every time I see him, and I'm not exaggerating either. What a sweet man. Thank you. I'll have to thank him as well."

  #"Common"
  show lilah neutral at left
  #
  li "See? The people in this town love you. So, go to the festival. I'm not sure when Archer is going to be back, but I can watch over the Inn until then. I want to call my mom anyway and see how things are going."

  #
  an "Are you sure?"

  #
  li "Yeah. Just tell me what to do. I can hold down the fort."


  #
  an "Just make sure that everything is okay, and do whatever Archer asks of you that's within reason. He's still our guest."


  #
  li "Got it. Anything else?"

  #"
  "Anjali shakes her head. "

  #
  an "No, but I'm proud of you. Craig would be too."

  #"
  "I'm taken aback by her admission. For some reason, the word proud always makes me feel embarrassed. I don't know, maybe it's the attention."

  #"LilahBlush"
  show lilah blush

  #
  li "What...why?"

  #
  an "You've released a movie and put yourself out there. You're working very hard for me here at the Inn, and you're playing nice with Archer. So, thank you."


  #
  li "Anjali..."


  #
  an "No impassioned words needed. I get it."

  #"
  "She gives me a warm pat on my shoulder. "

  #
  an "I'm bringing us home some dinner too so don't eat."
  hide anjali with dissolve


  #"
  show lilah sad at left
  "Anjali leaves, and I can't help but feel a bit lonely in the Inn. I decide that maybe now is a good time to call my mother and check in. I hope she's doing alright without me there. I always feel bad leaving her, especially since she'll be alone with those memories. "


  play sound sound_phone


  #"
  "My mother picks up on the first ring and my heart lurches. She's been waiting for this call and I've been avoiding it. I've sent her texts letting her know that things in general have been alright at the Inn but I have been been dreading hearing her voice."
  stop music

  #
  mom "Oh, Lilah! I've missed you so much!"



  #
  li "Hey mom, how are you doing? Is everything alright at home?"

  #"
  "I feel bad knowing that I've purposely been avoiding her. "


  #
  mom "I'm a little lonely without you here, but everything else is fine."


  #
  li "Mom, just say the word and you know I'll be home in a second."

  #
  mom "Absolutely not. I told you that I'm doing fine. Your sister-in-law needs your help, and you promised her you'd be there until Christmas. You're a Scott, you don't go back on your word."

  #
  li "I don't think Anjali will mind in this case."

  #
  mom "Lilah, I'm fine. Stop worrying about me."

  #"
  "I can just picture her waving her hand at me in an attempt to get me to drop the subject. "

  #
  mom "So, how about you? How's Riversone?"

  #
  li "It's nothing like home. There are no tall buildings or bustling streets. But I'm learning a lot. So, it's definitely an experience."

  #
  mom "I'm glad that you're gaining some knowledge from this. That's always good."

  #"
  "I can't say anything specific, like who my guest is. Though, I'm sure my mom would fall off of the chair she's probably sitting in if she found out I was working one on one with Archer freaking Lane himself. "

  #"
  "Believe it or not, she actually knows who he is. "

  #"
  "I can hear soft music playing in the background. If I strain my ears, I can hear the melody."

  play music music_silentnight
  show lilah mad at left 
  #
  li "Mom! Turn that off right now. You know I hate that song."

  #
  mom "It's Christmas, can't I listen to some music?"


  #
  li "Rudolph the red nosed reindeer, not this crap! Turn it off!"

  #"
  "My hands are shaking. Silent Night. Craig's favorite Christmas song. Why does she do this to herself? Why?"

  #
  mom "I promise you, everything is okay."
  show lilah sad at left 
  #
  li "Stop doing this to yourself, mom. Just please, stop."

  #
  mom "Doing what, Lilah? Listening to music?"

  #
  li "Reliving those memories over and over and over again."

  mom "They're happy memories of your brother. This was his favorite song to listen to during this time of the year."
  stop music
  
  show archer smile at center with dissolve
  play sound sound_opendoor
  #"
  "The front door creaks, and I see Archer walk in with a small white bag in his left hand. He holds it up and winks again. I'm not really in the mood to smile up at him..."

  #"
  "In fact...why is he being so friendly? "
  show archer blush
  #
  ar "Waffles to celebrate our almost win, I guess. If you uh...want?"
  show archer neutral 
  #"
  "I pull my cell phone away from my face."

  #
  li "Oh, thanks."

  #"
  "That's nice of him and also severely out of character... "

  #
  mom "What?"

  #"
  "I hear my mother's voice and pull the phone back up to my ear."


  #
  li "Oh, it's a hotel guest. I'll call you back later after my shift, alright? Turn that music off."


  #
  mom "Listen here, have a good time alright? Stop worrying about me. I am okay, Lilah. I promise you. Now, I'll let you get back to work. I love you."


  #
  li "Love you too, mom. Bye."

  #"
  "I really hope that she's not lying to me. If I'm out here galavanting while she's crying at home, I'll never be able to live with myself. She's acting like she's unaffected by the whole incident, but I just know she's putting a plate out for Craig at dinner."

  #"
  "Oh, mom... "

  #"
  
  "I can feel the tears building up in my eyes. "
  show archer smile
  #"
  "Archer is standing near the front desk by the time I hang up with my mother. He has a mischievous gleam in his eyes..."
  
  show archer sad 
  
  #"
  "...until he sees me."

  
  #"
  "I try to smile up weakly at him, but I'm sure my feelings are evident on my face. I just can't do it."


  #
  li "What? Never talked to your mother before?"

  #"
  "I look away from him quickly and down at the floor. "
  show archer neutral 
  #
  ar "Every night before I go to bed."

  #"
  "He hands me the bag of waffles. He doesn't draw attention to the tears in my eyes, though I know for a fact that he sees them."

  #
  ar "I already ate."

  #
  li "This was a nice gesture. I appreciate it."

  #"
  "I reach up to wipe my eyes. The charade is up anyway, he knows I'm upset about something. "

  show archer blush
  #
  ar "It was uh...nothing. I was passing by anyway...So, yeah." #(nervous)
  # "
  "I'm going to pretend like I don't notice Archer fumbling with his words like he doesn't acknowledge my frown. Maybe he doesn't know how to deal with crying...I don't know."
  
  #"
  "I kind of feel happy seeing him get flustered. "
  
  show lilah sadblush at left
  #"
  "Er...I didn't just think that! What I mean to say is that having Archer worry about me in his own unique way is kind of comforting. He hasn't outright said anything that would be even remotely comforting, but he doesn't have to. "

  #"
  "It's strange, but I think I get it. A nonverbal cue."
  show archer neutral 
  #
  ar "I feel like I should ask if you're okay?"
  show lilah neutral at left
  #
  li "You don't have to. It's kind of embarrassing to talk about anyway, but I just miss my family. I haven't seen my mom in about a week. To you that's probably not a lot of time, but I haven't ever left her side for more than a day or two, tops."

  #
  ar "That's nothing to be embarrassed about. She's your mother. I miss my mom all the time. It doesn't get easier because I'm a celebrity."

  #
  li "Yeah, I guess you're right. If it came out wrong, I didn't mean anything by it."

  #
  ar "No, I get it. Listen, I can't tell you to cheer up and expect it to fix anything but.. you'll see her soon, right?"

  #
  li "I'm going back in a few weeks for Christmas. So, yeah. I'll be fine."

  #
  ar "I know my opinion probably means little to you, because you're so convinced that I'm in another world. I'm a celebrity, so what kind of hardships do I have, right? I've missed out on a lot of stuff, Lilah. So I understand feeling homesick."

  #"
  "He's on the road all of the time. Even on his down time, he's alone. So..."


  #
  li "What works for you?"

  #
  ar "Being in the moment. I enjoy the moments I have now, because I know I'm lucky to have the opportunities that I do. I think of the people I love and how happy they'd be for me and how excited they'd be to hear the stories."

  #
  li "So inadvertently, you're still kinda enjoying life for them?"

  #
  ar "Yeah. Life's precious. If we spend our time sulking, we'll miss out on the opportunities in front of us. Like that snowman building contest. Never in a million years did I think I'd enter that, and I had fun."
  
  show lilah neutral at left
  #"
  "I look down at my hands to make sure that this is really happening."


  #
  li "Yeah. Me too. This is going to sound weird, but it was nice watching you let go a bit. The not so produced version of Archer Lane is kind of cool."
  show archer smile
  #
  ar "It's nice to be that guy, but not many times am I able to. So thanks for that. Maybe you're not that bad after all. I certainly didn't think I'd be meeting someone like you when I decided to come out here."
  show lilah happy 
  #"
  "I want to ask him why he's out here all by himself and not with his family, but I don't. Instead I just smile at Archer, because I'm happy that he's talking to me like this. "

  #
  li "Because I'm a little strange, right?"

  #
  ar "It's part of your charm."

  #
  li "Well, thanks."

  #
  ar "You're welcome."
  show archer neutral
  show lilah neutral 
  
  #"
  "..."
  #"
  "..."
  play music music_home
  #"
  "A silence befalls the two of us until Archer finally speaks up "

  #
  ar "So...Anjali is gone? I saw her walking out of the Inn."

  #
  li "Yep. I'm in charge, so if you need anything let me know."
  show archer blush 
  #
  ar "Thanks. I'm going to be in my room for a bit. If you need anything...ugh, I can't believe I'm offering this, but if you want to talk...uh..."

  #"
  "He looks like he's struggling with his words."

  #
  li "Are you offering what I think you're offering?"

  #
  ar "Yeah yeah. A listening ear. You know where to find me. Now, uhm, enjoy that waffle."

  #
  li "Thanks."
  hide archer with dissolve
  #"
  "I watch Archer walk off and immediately I feel like a weight has been lifted off of my shoulders. Even though I didn't tell Archer the full truth about why I was upset, he still had enough concern to talk to me. Not only that, he offered to listen to anything I wanted to talk about."

  #"
  "I know that's something he doesn't offer lightly. I want to offer my own support to him, but Archer is a private person. "

  #"
  "Anyway, I have some time to myself now. What should I do?"

  menu:
    "Do Some More Writing": #(+Archer)
      $ archer_score += 5 
      play sound sound_success
      jump chapter3_DoWrite
    "Check Social Media":
      jump chapter3_CheckSocialMedia

label chapter3_DoWrite:
  #"Write:"
  #"
  "I can put more work into my script while I've got some time. Writing is a good way to release some steam too. I reach for the paper with notes that I had scribbled before. "

  #"
  "All it boils down to is fear."

  #"
  "I wrote this down originally when Anjali and I were talking about Archer. I thought about what she had said and I realized that I'm not giving Archer the benefit of doubt because of my fear."

  #"
  "I was fearful that I would never be able to be taken seriously by someone as important as Archer. But clearly, I'm wrong because he's told me more than once that we're equals. "

  #"
  "I'm afraid of rehashing old feelings of immeasurable pain. I'm afraid of my mother breaking down and crumbling into nothing but a shell of who she once was. I'm afraid of letting Anjali down. "

  #"
  "I'm afraid of so damn much."

  #"
  "But with Archer and Anjali, it's hard to imagine them being afraid of anything."
  #"
  "I have to separate Archer from his image on television. The Archer I saw today is different. He has his own story to tell and maybe he refrains from telling it because he's scared too. "

  #"
  "On Anjali's computer, I open up her writing software and begin typing the first few sentences that pop into my mind."

  #"
  "If she wasn't afraid, what would she be? If she didn't hide behind herself, could she break down the walls in front of her?"

  #"
  "I don't know what it means for my story but the words flow out of me like I'm hearing them directly from the muses themselves. "

  #"
  "I fold up the paper and place it back in the draw I got it from. "
  jump chapter3_AfterWriteCheckSocialWatchTV


label chapter3_CheckSocialMedia:
  #"Check Social Media"
  #"
  "I think the internet connection is decent enough right now that I can check my email and social media. "

  #"
  "Wait..."

  show lilah blush at left
  #"
  "400 emails!?"
  show lilah neutral at left
  #"
  "I skim through them, but there's nothing important. Just a bunch of coupons and some newsletters for websites I don't remember signing up for. "

  #
  li "Uhm...okay..."

  #"
  "Next, I log onto my social media. Scrolling down the page, I feel like I've been in hibernation for years. "
  
  show lilah happy at left 
  #
  li "Thomas De Luca's album seems to be doing well. Better not tell Archer that..."
  
  show lilah neutral at left
  #"
  "I keep scrolling down. "
  
  #
  li "Wait...she's pregnant now? How? I feel like I just saw her last week!"

  #"
  "Ok, this is a sensory overload. I need to log off before I'm here for the rest of my life scrolling down infinitely. "
  jump chapter3_AfterWriteCheckSocialWatchTV


label chapter3_AfterWriteCheckSocialWatchTV:
  #"Common"
  #"
  "By the time I finish, Anjali is already back at the Inn. "
  show anjali neutral at center with dissolve 
  #
  an "Come to the kitchen. You can call Archer too."

  #
  li "Huh? What for?"

  #
  an "I told you that I would bring home dinner, right?"

  #
  li "Oh, right!"

  #
  an "There's plenty of food to go around, so it's your choice whether you want to invite Archer or not."

  #
  li "Oh um..."

  #"
  "What should I do? Should I invite Archer along? "

  menu:
    "Yes":
      $ archer_score += 5 
      jump chapter3_InviteArcherYes
    "No":
      jump chapter3_InviteArcherNo

label chapter3_InviteArcherNo:
  #"No:"
  #
  li "Well, Archer said that he had eaten already at the festival. Er, I don't really think a guy like him wants to be out of shape, you know?"

  #
  an "Uh-huh, that's why you're not inviting him..."

  #
  li "Wait! Why do you think I'm not inviting him?"

  #
  an "Could be a number of things. For one, you could be too lazy to go up the stairs."

  #
  li "Anjali..."

  #"
  "She winks at me. "

  #
  an "Or maybe it's because you're embarrassed to go up there and ask him."

  #
  li "N-o! It's because I don't want to bother him."

  #"
  "Anjali seems satisfied with my answer and nods."

  #
  an "Okay."

  #
  li "Okay? That's it?"

  #
  an "Yeah. I'm not going to force you to go up there and bother him. I was only teasing."

  #
  an "Anyway, meet me in the dining room. I've got to set up a few things, but trust me. You'll love this."

  #"
  "I nod and give her a thumbs up.  Anjali seems pretty excited for this. I wonder what she has up her sleeve..."

  scene bg kitchen with fade#(fade)
  show lilah neutral at left
  #"
  "All of the food smells delicious. Anjali sets the table in my cabin with a meal fit for a king. There's a platter of cheeses and olives, a pork roast and a salad. On the side there's mashed potatoes and mixed vegetables. To top it all off, there's chocolate cake. "

  #
  li "What's all this for?"

  #
  show anjali neutral
  an "I just wanted to show you how to enjoy a family meal the Riversone way. I had placed this order before you arrived here and had it catered at Lady Lacey's. They specialize in baking but the cooks there can do just about anything. They're amazing."

  #
  li "You really didn't have to..."

  #"
  "My voice trails off. I don't know what to say. This is really nice of Anjali. "

  #
  an "When my mother moved back home, I was lost. You and your brother and your mom made me feel like I belonged somewhere. I know this is a tough time of year for you guys, because it's a tough time of year for me too."

  #
  an "I want you to know that there isn't anything in the world more important to me than family. You're my little sister and you always will be. No matter what."

  #"
  "She kisses my forehead. I can feel the tears biting at the corner of my eyes. "

  #
  li "Anjali...you're making me cry!"

  #
  an "I'm sorry. This time of year always makes me sentimental."

  #"
  "She looks like she wants to say more, but instead lets her hair fall into her face as she shakes her head lightly. "

  #
  an "Anyway... have some food. This is a time to celebrate and be happy. So please..."

  scene bg black with fade
  #"Change bg"
  show lilah neutral at left
  show anjali neutral

  #"
  "We eat our food but there's a tension that looms over the both of us. Even though we're laughing and grinning at each other, there's something I need to get off my chest. "

  #
  li "Anjali..."

  #
  an "Yes Lilah? What is it? Do you want another serving of something? Please, help yourself."

  #"
  "I place down my fork. "


  #
  li "No, it's not that. I've got a lot on my mind right now and I need to tell someone about it. I'm practically bursting at the seems."

  #
  an "Is everything alright?"

  #
  li "I mean...kind of. Maybe? I don't know."

  #
  li "It's about mom. I spoke to her on the phone today."

  #
  an "Oh? How is she doing?"

  #
  li "I don't know. She sounded okay, but Silent Night was playing in the background."

  #"
  "Anjali frowns. "

  #
  an "That was Craig's favorite holiday song. It's quite fitting isn't it? Now that Craig is gone-"

  #
  li "Please don't."

  #"
  "I shake my head furiously. "

  #
  li "I don't want to think about it."

  #
  an "Sweetie, can I ask you something? I don't wish to offend you but I need to know."

  #
  li "Go ahead."

  #
  an "Is it your mom who is holding onto Craig's death, or is it you?"

  #"
  "Her question is blunt and it hits me hard. "

  #
  li "My mom keeps setting the table for Craig when we all know he isn't going to magically walk into the dining room. She blasts that song as if it's his anthem..."

  #"
  "I get choked up even just thinking about it."

  #
  an "That's how your mother copes. If it helps her to play that song, then you should let her. Unless, it bothers you. Does it bother you?"

  #
  li "Of course it does!"

  #"
  "I don't realize I've slammed my fist onto the table until I hear the metal fork I was using hit the ground. "

  #
  li "I don't like that song. Every time I hear it, I think of all the times we played Christmas songs while putting up the Christmas tree."

  #"
  "I sniffle, feeling the tears biting my eyes."

  #
  li "Then I remember he isn't here. He won't ever be here again. For the rest of my life I'll have to wake up knowing I won't ever see my brother again. Anjali, it sucks."

  #
  an "I know. I'm sorry. But instead of pushing his memory away, you should embrace it. Think of all the good times you two had together."

  #
  li "I don't want to talk about it anymore. I came here to get away from everything. Don't do this to me right now."

  #"
  "I wipe my damp cheeks with the back of my hand. "

  #
  li "Can I be excused?"

  #
  an "Yes, of course."

  #
  li "I'm tired, so I'll see you tomorrow bright and early."

  #"
  "It feels like a ton of bricks are weighing on my heart. I can feel the walls closing in around me and all I want to do is curl up into a ball and sleep. Sleep, so I forget. "
  jump chapter3_AfterInviteArcher


label chapter3_InviteArcherYes:
  #"Yes to Dinner with Archer:"
  #
  li "I guess I can invite him."

  #
  an "You guess? Is someone nervous to ask him?"
  show lilah blush at left
  #
  li "N-o!"

  #"
  "I turn my head away from her so she won't notice the blush on my cheeks. "

  #
  an "Uh-huh. Sure. I thought the two of you were getting along."
  
  #
  li "Yeah, getting along is not the same as being friends!"

  show anjali smile
  #
  an "So you say."

  #"
  "She laughs. "

  #
  an "Well? Are you going to invite Mr. Lane or not?"

  #"
  "I take a deep breath and try to swallow my nerves. "

  #"
  "The worst Archer can say is no and that's that. I don't know why I'm letting it bug me this much."

  #"
  "It's just that jerk anyway..."
   
  scene bg hallway with fade
  show lilah neutral at left
  show archer neutral at center with dissolve
  #"
  "I don't have to knock on Archer's door because he's standing outside of his room already. "

  #"
  "In his hands is a large clear garbage bag. "

  #
  ar "Can I help you with something?"

  #"
  "I point to the bag he's holding. "

  #
  li "What are you doing?"

  #
  ar "Throwing out my trash."

  #
  li "No, don't do that. That's my job. Let me get that for you."

  #"
  "I reach for the garbage bag but he holds it above my head. "
  show archer talk 
  #
  ar "Nuh-uh. No can do."

  #
  li "What? Why? Are you hiding your garbage from me now too?"

  #
  ar "No, don't be daft. The bag is clear. You can see right through it."
  #"
  "He holds it up close to my face. I can see...chocolate wrappers!?"

  #
  li "Is that a guilty pleasure of yours or something?"

  #
  ar "What? The chocolate? I love chocolate."

  #
  li "Of course you do. Anyway, I'm here because Anjali had food catered for my visit here. She says it's really too much for both of us to eat and would like to know if you'd join us."

  show animation_heart:
    xalign 0.52
    yalign 0.05
  show animation_heart:
    linear 2 alpha 0.0
  #(should be off of the screen before the sound finishes)
  play sound sound_success
  #
  ar "She'd like to know?"

  #
  li "Yes, that's what I said."
  show archer smile 
  #
  ar "Mhm, that's why you're the one up here asking me. Sure Lilah, I'll join you."
  show lilah blush at left
  #
  li "It would mean a lot to Anjali too, you know. She doesn't get a lot of guests up here. It's pretty lonely and this time of the year is hard on us both so..."
  show lilah sad at left
  #"
  "I turn around before Archer can say anything else about that or see the frown on my face. "

  #
  li "Anyway, just follow me."

  #"
  "I hear no utterance, or grunt from Archer to alert me to his acceptance of my terms. Instead, there are his footsteps against the wooden hallway to assure me of his presence. "


  scene bg kitchen with fade
  show lilah neutral at left
  show anjali neutral with dissolve
  #

  #"
  "All of the food smells delicious. Anjali sets the table in my cabin with a meal fit for a king. There's a platter of cheeses and olives, a pork roast, and a salad. On the side there's mashed potatoes and mixed vegetables. To top it all off, there's chocolate cake. "

  show archer neutral at right with dissolve
  show anjali smile
  #
  an "Oh, Archer! Nice of you to join us. It's a pleasure."
  
  #"
  "She gives him an appraising look before winking at me."
  show lilah blush at left
  #"
  "I can feel my face heating up and I know it's time to come up with some kind of escape plan. "

  #
  ar "Thank you for having me tonight. You didn't have to invite me."

  #
  an "It was Lilah's idea and it was a good one. We have so much food that there's no way we can eat it all by ourselves."
  show lilah neutral at left 
  #
  li "You don't have to lie to him, Anjali. He knows you're the nice one."

  #
  an "Hey, I left the choice up to you and you agreed. So we're partners on this one."
  show archer smile at right
  #
  ar "It doesn't matter who invited me. Thank you both. I haven't had the chance to sit down and eat a quiet meal with others in a long time."
  show lilah happy at left 
  #
  li "Oh boy, if you're looking for quiet you're in for a real treat."

  #
  ar "I know you don't do quiet, Lilah. That's not what I mean. I'm talking about not having to look over my shoulder all the time for paparazzi or fans."

  show lilah sad at left 
  #
  li "I'm sorry, that must be annoying."

  show archer neutral at right
  #
  ar "It truly is. I love my fans, I really do. But sometimes I feel like I live my whole life for them. I lose sense of myself."
  show anjali neutral
  
  #"
  "Anjali shoots me an 'I told you so' look and I can already hear the lecture she's going to give me after dinner about Archer and I both being human. Yada yada..."

  #"
  "I get it. We're human. We both want to enjoy our lives. "
  show lilah neutral at left 
  #"
  "Archer places a hand out, motioning for me to take my choice of seating at the set table. I nod politely, stepping past him to sit at the far right closest to the door. "

  #
  an "Archer, are you by chance allergic to anything? The food was prepared in a kitchen where peanuts are held in storage."
  
  #
  ar "No, no. We're all good here. I can enjoy all of this food."

  #
  an "That's perfect. Then by all means, please dig in."

  #"
  "She doesn't have to tell me twice! Anjali sits beside me and Archer sits across from her. "

  #
  ar "I really do appreciate this."

  #"
  "Archer is hesitant to grab food, meanwhile I'm loading the calories onto my plate by the spoonful. "

  #
  an "Hey, you can make yourself at home. No one is going to judge you here."
  show lilah happy at left 
  #
  li "Nope!"

  #"
  "I don't even finish chewing before I start speaking but I think that kind of informality has relaxed Archer a bit, as he leans over the table and grabs a spoonful of mashed potatoes. "

  #
  ar "I'm going to have to work all of this food off after this trip."
  show lilah neutral at left 
  #
  li "What's a few extra pounds, right?"
  #
  ar "Yeah, tell that to my agent please. She's on my case all the time about what I eat."

  #
  li "She's not here right now."

  #"
  "I don't look up at him when I say this, too afraid to see the look on Archer's face. "

  #
  ar "No, not on my break time. I schedule this time away from everyone. I need it to recharge. I'm going to just take in the sights of Riversone."
  show anjali smile 
  #
  an "My little town is quite impressive, isn't it?"
  show archer smile at right
  #
  ar "Definitely. It's got a lot of charm and character. I kind of feel like I'm in one of those cheesy holiday movies where some rich guy goes to a small town to find the meaning of Christmas or something."

  #
  an "I never really got those movies. The real meaning of Christmas can be found anywhere, not just some mountainside retreat or small town that's isolated from the rest of the world."
  show archer neutral at right 
  #
  ar "I told Lilah that the holiday season is more a capitalistic cash grab now than anything but..."

  #"
  "He looks over at me."

  #
  ar "She believes in Christmas magic."

  #
  li "It's real. I know because after everything I've been through, I don't hate the season. You don't know how easy it would be for me to swear off the holiday for good but I don't. Something keeps drawing me back in."

  #"
  "It's Craig's memory that makes me hold onto the Christmas season. I can't stop celebrating, because I know how much it meant to him. "
  #
  li "Anyway, that was a lot of unnecessary information. Let's talk about something else..."

  #
  an "I'm sure you get a lot of questions on a daily basis, Archer. Do you have any for us? Anything you want to know?"
  show archer talk at right 
  #
  ar "Is this place something you've always wanted to open?"

  #
  an "Oh, no. I was an English Literature major in college. I wanted nothing more than to write the next thrilling academic paper on a Shakespeare play. But, life has a way of throwing things into your lap. I met my late fiance and this was something he decided to open on a whim."

  #
  ar "And you went along with it, just like that?"

  #
  an "Yes, of course. It was a scary endeavor, packing everything up that I knew and moving out here away from the city I was so used to. But, Craig's face lit up when he talked about his dreams for this place. I couldn't say no."

  #
  an "Now, it's a decently successful place. I get the business that I have to in order to stay afloat. I don't ask for more than that."

  #
  ar "Wow, that's incredible."

  #"
  "He really does look awed by Anjali's confession. "

  #
  ar "What about you?"

  #"
  "I shirnk under Archer's gaze." 
  #
  li "Huh? What about me?"

  #
  ar "How'd you find yourself here?"

  #
  li "I just needed a break from the real world. Things are tough back home. So, I just decided to run away from it all so that I could clear my mind. I'm not as inspiring as Anjali. I'm going to leave in a few weeks and go back to my dull life."

  #
  an "Your life isn't dull. You make your movies. You're very creative and you have a lot to say."

  #
  li "I really don't."

  #
  ar "Everyone has a story. It's just a matter of whether or not they want to share."

  #
  li "Well, not every story is exciting."
  show archer neutral at right 
  #
  ar "They don't all have to be. Think about the movies on the market. Imagine having nothing but action films. How boring would that be? What about the people who prefer dramas or comedies?"

  #
  li "Why are you so well versed? It's like I'm reading an advice blog or something. Fine, you make some good points."

  #
  ar "I know I do. You have to be confident in your story, even if you hear that voice in your head telling you to back down. Because you'll fail if you don't believe in what you're putting out there. Confidence goes a long way. I'm more apt to want to invest my time into someone who looks the part."
  show anjali smile 
  #
  an "Ah, there's his big secret tactic. Should we be taking notes?"

  #"
  "Archer, Anjali and I joke around like this for a while. Archer has had some really solid things to say. It's amazing how down to earth he is when he strips away that guard he keeps up all the time. "

  #"
  "I actually think that if the circumstances were different, we could be friends. "


  #
  ar "Wow...that was really good. Thank you for sharing but I am so full right now."

  #"
  "He has his hand on his stomach as if something is about to burst out from it. "

  #
  ar "Did you tell Anjali about our prize from the snowman building competition, Lilah?"
  show lilah smile at left 
  show archer smile at right
  #
  li "Oh! No, I didn't!"

  #"
  "I lean a little into the table and grin at Anjali excitedly. "

  #
  li "We won second place, so we got a gift card to Leighton's Grocery. Archer and I want you to have it."
  show anjali neutral 
  #
  an "Oh, no. I couldn't."

  #
  ar "Please, take it. You've been exceptionally kind to me while I've stayed here. It's really the least I can do."

  #
  li "Yeah, and you've been great to me for my whole life so...this is really nothing."
  show anjali smile 
  #
  an "Aw, you two...thank you both so much. Seeing you two get along is gift enough for me."

  #
  li "But groceries are a nice addition, yeah?"

  #Anjali #(giggles)
  an "Definitely. Thanks again. "


  #
  ar "You're very welcome."
  show archer neutral at right 
  #"
  "Archer suddenly lets out a yawn. "

  #
  ar "Ah, I'm sorry. I really need a nap now."
  show anjali neutral 
  show lilah neutral 
  #
  an "I always say that if the food doesn't make you sleepy, it's not that good."

  #
  li "I'm having that leftover chocolate cake for breakfast...."

  #"
  "I place a hand over my mouth, stifling a yawn. "

  #
  li "Maybe I need a nap too."

  #
  an "You guys go, I'll clean up."

  #
  ar "No, I couldn't. Not after your kindness."

  #
  an "This was my treat. I'm going to clean it up and you two are going to take a nice nap."

  #
  ar "But-"

  #
  li "It's best not to argue with her. You'll just waste ten minutes of your time and she'll still manage to get her way."

  #
  an "She's right, you know. I'm the owner of the inn, let me do my job."

  #
  ar "Thank you again."

  #
  an "Of course."
  hide anjali with dissolve 
  #"
  "Archer and I walk out of the kitchen. "

  if flag_snowballFight == 1:
    #"If snowball fight:"
    #
    ar "I haven't forgotten about our snowball fight."
    show lilah happy at left
    #
    li "Oh, you're on. I'll destroy you."
    show archer smile
    #
    ar "Oh, you wish."
    show archer happy
    show lilah blush at left
    #"
    "He winks at me, causing my heart to flutter. "

    #
    ar "Thanks for today. Have a goodnight, Lilah."

    #
    li "Ye-ah! You too!"

  else:
    #"No snowball fight: "
    #
    ar "Thanks for today. Have a goodnight, Lilah."

    #
    li "No, thank you for joining us. Oh and for the snowman building contest too."

    #
    ar "Don't mention it."

    #"
    "He waves at me. "

    #
    ar "Until the morning."


    #
    li "Until the morning then."


label chapter3_AfterInviteArcher:
  pass
  
label chapter4:
  scene bg transition with fade
  show transition_chapter4 with Dissolve(5.0) 
  
  #Transition to Snowball Fight"
  #"IF Lilah threw snow at Archer at the snowman building competition "
  scene bg lobby
  show lilah neutral at left
  stop music
  
  #"
  "The next morning I wake up feeling refreshed. There's nothing like going to bed with a stomach full of good food. "

  #"
  "I throw my arms above my head and stretch. Today's duties include answering emails from prospective clients. It's not terribly exciting, but Anjali has other things to attend to this morning so she's left me in charge of the inn. "

  #"
  "Her instructions were to answer the remaining emails in her inbox, set the phone's message to say that the inn is closed for the day and not receiving any more messages. Oh, and then take the rest of the day off. She's been giving me a lot of free hours lately, even though I just started."

  #"
  "With only one guest, there really isn't much to do today. "

  #"jump to chapter 5 if lilah does not have snwoball fight with archer"
  if flag_snowballFight == False:
    jump chapter5

label chapter4_snowballFight:
  play sound sound_footsteps

  #"
  "I look up from the computer and see Archer walking towards the door. "
  
  #
  li "Heading out?"
  show archer scarfneutral with dissolve
  #
  ar "Nope. Doing a temperature check. I've gotta see how deep the snow is. You know, for our big snowball fight."
  show lilah happy 
  #"
  "It's kind of cute how excited he is about the whole thing. He's like a little boy. "

  #
  ar "Speaking of...are we still on for that?"


  #
  ar "If you're not scared, I mean."



  #
  li "No, never. I'm ready when you are, superstar. Our bet still stands."

  show archer scarfsmile 
  #
  ar "You're going to lose, I hope you know that."

  #
  li "Really? Because I was just going to say the same thing to you."


  #
  ar "We'll see."


  #
  li "Big words."


  #
  ar "I am quite proud of my vocabulary, yes."


  #"
  "He steps closer to me, a smirk playing on his lips. "

  show lilah neutral 
  #"
  "Intimidation? Oh no, that won't work on me. I step towards the male. He wants to play that game, huh?"

  
  #
  li "All I see is guy who thinks he's tough."


  #"
  "He raises a brow and smirks. He's so close to me I can feel his breath on my face. "


  #
  ar "You've got bad judgement, De Luca girl."


  #
  li "That's not what the judge said when we won second place for our snow woman."

  show archer scarfmad 
  #
  ar "That judge didn't know what she was talking about."

  show lilah mad at left  
  #
  li "Oh no, how could Archer Lane ever get second place for anything?"


  #
  ar "Second place is not winning, Lilah. It's losing. Plain and simple."


  #
  li "So when Thomas De Luca won best male vocalist at last month's music awards, you lost? Even though you were runner up?"


  #Archer #(agitated)
  ar "Yeah, Lilah. That's how losing works."

  
  #"
  "I can see Archer getting visibly upset. Thomas De Luca is a sore spot for him, I realize, because the man is skyrocketing to fame. Does Archer feel intimidated by that?"

  show lilah neutral at left 
  #
  li "But you still have tons of fans and your album must have sold a bunch of copies. You're not really losing anything. Thomas De Luca is just gaining more fans."


  #
  ar "His music isn't even that good. I should have won."


  #
  li "As a De Luca fan, I can speak for his music. Besides the engaging melodies, his lyrics are great. He's very full of heart and you can tell that when you listen to him. He feels what he's singing."


  #
  ar "And I don't? You don't know what I do when I'm behind the scenes writing a song. I put everything into my music. It's all or nothing."


  #
  li "See, that's wrong. You and De Luca can both be good. It doesn't have to be either one or the other. People can like you both."


  #
  ar "Can they?"

  #"
  "He seems unconvinced."


  #
  li "I like TDL's music and I've listened to a lot of your tracks too. So, yeah. It is possible. But for the record, I'm sure De Luca isn't as much of a jerk as you are."


  #
  ar "Alright I've had enough of your smart mouth."
  show archer scarfhappy 
  #"
  "Archer's words have an edge to them, but he's smiling like a little boy who just got a piece of candy."

  #
  ar "Let's take this outside. I'll prove I'm the best."


  #"
  "I place my hands on my hips. "


  #
  li "I don't see how a snowball fight will prove you're better at making music than Thomas De Luca, but okay. I'll champion him."

  #"
  "I lift my arm to make a muscle in an exaggerated fashion. "

  #
  li "I was out on the patio earlier this week and know the perfect open space for a fight."

  #"
  "Behind the Inn there's an open space right next to my cabin. There's plenty of room for Archer and I to run around and toss snow at each other. But before we go, I'm curious about something. "

  #
  li "Hey, I know you don't really want to talk about your personal life but..."

  #"
  "I can't keep from biting my tongue on this one. "
  show archer scarfneutral 
  #
  ar "Don't ask anything stupid."

  #
  li "I just want to know if you've had a snowball fight in a while. That's it."

  #"
  "He's quick to answer, maybe relieved that I didn't cross any of his boundaries. "

  #
  ar "No. Can't say that I have. Why?"

  #
  li "Don't look so suspicious, jeez. You just seem so excited. That's all. I wanted to know if superstars are allowed to have fun since you're so uptight."

  #
  ar "I'm not uptight."
  show lilah happy at left 
  #
  li "No. Of course you're not."

  #"
  "I let out a laugh and begin walking to the front door. "

  #
  li "Head towards the back and when you see my cabin, make a left. That's where we'll throw down."

  #"
  "I don't wait for Archer's reply. I know that he's going to follow me because he is so into the idea of a snowball fight. He probably doesn't have the luxury of running around in the open with his gloves on and snow in his hands. "

  #"
  "What started as a competitive thing has turned into a friendly gathering. Two people having fun for the sake of having fun. The thought brings a smile to my face. "

  #"
  "Archer isn't so bad in moments like this. I wonder if I'm wearing down his walls, or if he's just a little lonely in his bubble. Either way, this is a good sign. "
  
  scene bg fields 
  play music music_foreverfriends
  show lilah smileout at left
  show archer wintersmile with fade

  #"
  "Outside, the air is cold and it hits my face like a refreshing mint. Riveresone is beautiful. I can say that a million times over. I look over at Archer and see the same contented smile on his lips. "

  #"
  "Honestly, when Archer smiles like this and not with that plastered look of hollow happiness he has on television, he looks gorgeous. I don't want to even move a muscle in fear of breaking his tranquility."

  #"
  "Instead, I keep walking in hopes of Archer following me. I walk all the way over to a large plot of land which isn't too far away. The trees covered in snow make for a beautiful backdrop. I hold my hands in front of my face, making a square with my fingers. "

  show lilah neutralout at left
  show archer winterneutral
  #
  li "I'd love to make a movie here. It's gorgeous."

  #
  ar "Why don't you?"

  #"
  "I lower my hands. "

  #
  li "No actors. No script. No money. It's never that easy."

  #
  ar "You know, when I started out I was playing in the subways of NYC for tips. I didn't have a fancy guitar, backup singers, or a stage. It was just me, my voice, and a subway car of about 6 or 7 people."


  #"
  "I stare at him in awe. I had no idea that Archer started so close to the bottom. He carries himself with such confidence that I just always figured he started at the top. "


  #
  li "Really?"


  #
  ar "Yeah. Really. Look it up online, there are videos. Point is, I wasn't born into this position. I had to work for it."


  #
  li "It's hard to imagine you like that."

  show archer wintertalk 
  #
  ar "I keep trying to tell you that I'm a regular person just like you."

  
  #
  li "I mean...You say that, but it's obvious that you're not. Isn't that why you push people away?"
  
  show lilah madout 
  li "I'm not even supposed to ask you personal questions. What kind of regular person makes you sign an agreement like that?"

  show archer wintermad 
  #
  ar "You shouldn't ask anyone personal questions unless they're willing to share. It's common decency."


  #
  li "Yeah but if you don't feel like answering you just tell the person that. You don't threaten to sue them."


  #
  ar "Well excuse me for trying to protect people."
 
  show lilah neutralout 
  #
  li "You're protecting yourself mostly. Which I totally get."

  show archer winterneutral 
  #
  ar "I'm protecting you too.Think about it. If my fans find out I'm here, they'll swarm the place. Paparazzi too. Those piranhas call you my new fling and your life is over. Constant harassment from those people. So, you're welcome."

  show lilah sadblushout 
  #
  li "I didn't realize..."

  #"
  "Archer protecting me? I never even thought about that. Now I feel bad thinking he's only looking out for himself. "
  
  #
  ar "The NDA isn't a punishment."
  show lilah neutralout at left 
  #
  li "Maybe you can loosen up on it. That's all I'm saying. I haven't proven myself unloyal, have I?"


  #
  ar "The threat of losing money does that to a person."


  #
  li "I told you in the beginning that I'm a decent human being. So, we can cut the act. I signed your agreement, I have no intentions of going against it. But can we be friends? Or, at the very least accept each other's existence?"


  #"
  "Archer's gaze is piercing and I can't read what he's thinking. I feel the overwhelming need to fix whatever mess I might have made by speaking my mind. So at least if he disagrees, I can still keep some of my dignity."


  #
  li "I just want to pretend that we're cordial to each other because we sort of like each other. Not because of a piece of paper. I don't know, it rubs me the wrong way that whatever this is..."

  #"
  "I motion to him with my index finger and then to myself. "

  #
  li "...is because of a contract."

  #
  ar "Alright."


  #"
  "My hands are shaking and I don't know what to say anymore. But I do have to say something. "


  #
  li "What?"


  #
  ar "Alright. We can be acquaintances who accept each other's existence. We're not quite friends yet."

  show lilah happyout at left 
  show archer wintermad 
  #"
  "A smile spreads across my face. Archer crinkles his nose up in disgust. "


  #
  ar "Oh, what now?"

  #"
  "I jump up gleefully. "


  #
  li "You said yet! It means there's still a chance. Somewhere down the Lane."
  show archer winter happy
  #
  ar "I can't believe you just made that lame pun."

  #"
  "He acts like he doesn't think it's funny but Archer is totally smiling. "

  #
  ar "Day one, you argued with me in the lobby of the hotel. Now you want to be my friend. Lilah, you're so-"
  show lilah madout at left
  #
  li "Hey!"

  #"
  "I cut him off. "

  #
  li "Call me strange one more time and I'll throw a snowball at you. Don't test me!"

  #"
  "I quickly change the subject because I don't want him to dwell on it. Archer and I may not get along but there's something in his smile that attracts me to him."
  #"
  "I'm not ready to admit it to him yet, but I think we could actually be friends for the duration of his stay. "

  #"
  "Archer steps closer and grins mischievously. "

  #
  ar "Lilah..."

  #"
  "I lean down and pack a snowball in my gloved hands. "

  #
  li "Don't."


  #
  ar "You are a..." #(teasing)


  #
  li "Don't say it!"

  #
  ar "...strange one."


  #"
  "He makes the motion of dropping a mic, takes a step back and makes an explosion sound. I raise a brow. Oh, really? Now, I've got to put my money where my mouth is. Or I mean, I totally don't have to."


  menu:
    "Throw Snowball": #(+Archer) "
      $ archer_score +=5
      jump chapter4_SnowballFightThrow
    "Don't":
      jump chapter4_SnowballFightDontThrow

label chapter4_SnowballFightDontThrow:
  #"Don't:"
  #"
  "I drop the snowball from my grasp. I don't know, I guess I'm just losing my nerve. "

  #
  ar "What, did you chicken out?"

  #
  li "N-o!"

  #"
  "I turn around with a huff. "

  #
  ar "Oh, so you're all talk then, huh? You just wanted to scare me so I wouldn't call you strange."

  #"
  "I cross my arms over my chest, but I'm sure he can't see it. "

  #
  li "So?"

  #"
  "Is it really okay to hit Archer with a snowball? For some reason I'm really scared. What if he gets angry? Urgh, I'm overthinking it because Archer challenged me to a real snowball fight. This was all his idea. "

  #
  ar "We can go back in if you want."

  #
  li "No! I want to have this snowball fight with you. I just felt bad, is all."

  #
  ar "Little Lilah is human after all."

  #
  li "Look who's talking!"

  #"
  "Archer kneels down into the snow and grabs a chunk of snow. "

  #
  ar "So we can't start until someone says go officially?"

  #
  li "Yeah. Let's keep it fair here."

  #
  ar "Ok. Go."

  #"
  "I feel a cold sensation on my cheeks as the snowball makes contact with my face. "

  #"
  "I'm in disbelief. That sneak!"
  #"Jump to label: snowballfight"

  #jump chapter3_SnowballFight

label chapter4_SnowballFightThrow:
  #"Throw: "
  #"
  "The snowball wets my glove as I continue to form it. "

  #
  li "I warned you!"

  #"
  "I shout as I toss the snowball at him, hitting him directly in what he'd call the money maker."
   
  #"  
  show lilah happyout
  
  "I take a step back, tossing my head back with laughter. I just can't help it. Archer's face is totally red! "
  show archer winterblush
  #
  ar "You just hit me with a snowball." #(in disbelief) "

  #Insert: Success.ogg and little heart gif"
  show animation_heart:
    xalign 0.52
    yalign 0.05
  show animation_heart:
    linear 2 alpha 0.0
  #(should be off of the screen before the sound finishes)
  play sound sound_success


  #
  li "I told you I would."
  
  show archer winterhappy
  #"
  "Archer now looks amused as he leans down himself and picks up a snowball. He tosses it between his hands before taking a step towards me. "

  #
  ar "You followed through."

  #"
  "I make a run to the right at full speed. "
  show lilah madout at left 
  #
  li "This is war!"
  show archer wintermad 
  #
  ar "Hey, Lilah!"

  #"
  "I hear him shouting, but I only turn when I have a snowball in my hand. Archer is running after me with two snowballs, one in each hand."
  #"
  "One of the snowballs comes hurling towards me, but I duck just in time to see it fly past my head. Though, when I stand up the other snowball in Archer's hand hits me square in the temple."
  show lilah blushout
  #
  li "Ah!"

  #"
  "I stumble backwards, but catch my footing pretty easily. He isn't going to take me down today. "

  #
  li "Lucky shot."
  
  show archer wintersmile
  #
  ar "Mhmm, sure."

  scene bg black with fade
  scene bg fields 
  show lilah neutralout at left
  show archer winterneutral
  

  #"
  "This prompts an all out war between Archer and I, with both of us flinging snowballs wildly at each other. But only one of us is better, and unfortunately..."

  show archer wintermad 
  #
  ar "Time to be dethroned!"

  #"
  "He screams in the same exaggerated tone he had used when we were watching that cheesy movie. Archer lifts his right arm up as if he's wielding a sword and then lowers it to point towards me. "

  #Archer #(same exaggerated tone)
  "Surrender!"
  
  show lilah madout at left
  #
  li "Absolutely not!"

  #
  ar "Then prepare to be defeated."

  #"
  "He throws the snowball at me, smothering my face in a cold sensation. Archer is ruthless. "

  #
  li "Dude!"
  show archer winterhappy 
  #"
  "He chuckles but places his arms behind his head in a laid back fashion. "
  
  #
  ar "Good match, Lilah. I'm impressed by your resilience but you can't beat the king. So you know what that means, right?"
  show lilah sadout at left
  #"
  "I groan. "
  
  #
  li "I don't want to..."
  show archer winterneutral 
  #
  ar "You've got to show me that movie you made."
  show archer winterblush
  #"
  "Then he lets out a deep sigh and looks away. I swear I see a tinge of red on his cheeks though."

  #
  ar "Unless you really don't want to."
  show lilah neutralout at left 
  #
  li "Oh, you're giving me a choice? Because you know, it really doesn't seem like your style."
  show archer wintertalk
  #
  ar "I told you I'm not a bad person! Stop making me out to be one."


  #
  li "I think we just misunderstood each other in the beginning. But you were the one who kept giving me attitude. Remember that."

  #"
  "He feigns shock."

  #
  ar "Me? You stalked me in the grocery store and then refused to sign my agreement."
  
  #
  li "Okay, so we both made mistakes. Fine."

  #"
  "I cross my arms over my chest and look down at the footsteps in the snow that Archer and I have made. There are a multitude of them."
  
  #"
  "I remember early on not even wanting to be near Archer. Now, I don't know if I want to stay away."


  #"
  "A bet is a bet, and I promised Archer I'd show him my movie. I don't go back on my word. "

  #
  li "When do you want to watch my movie?"
  show archer winterhappy
  #"
  "A vibrant smile grows on Archer's face."

  #
  ar "Yeah? I can see your movie?"

  #"
  "I nod. "

  #
  li "Mhm, that's what I said."

  #
  ar "Thanks. I know that's something personal to you.I mean, it's something you put effort into creating."

  #
  li "Archer, why do you want to see it so badly? Snowdrop really isn't a great movie. It was my first real released film, and it was so bad there wasn't even any reviews at all."

  #"
  "Archer holds his hand out to me. "

  show archer winterneutral
  #
  ar "Ok, enough of that self loathing. Come with me. I want to show you something."


  #"
  "My eyes snap up, but of course Archer's expression is unreadable. I take his gloved hand which is soaked. Still, my hand tingles beneath my own drenched glove. "


  #
  li "What could you possibly want to show me?"

  #"
  "I speak just to calm my nerves. The last time Archer touched me, it was to move me out of his way. Now, he's holding my hand"
  
  #"
  "My mind is screaming why, but I know I'm not going to get an answer. Archer doesn't play by the rules of common social interaction. "

  #
  ar "Well, I was walking around outside of the Inn and how much of it have you seen?"

  #
  li "I've seen my cabin, this area, the patio, you know...and the actual inn."

  #
  ar "Alright, so you haven't seen it yet. Good. Come with me."
  show lilah blushout at left 
  #"
  "He tugs on my hand, a signal that we're going to start walking. All the while, my head is spinning with irrational thoughts of why Archer could possibly be holding my hand. Or rather, why he would want to. Simply to lead me somewhere, right? Why am I even thinking of this to begin with? "
  #
  ar "Are you alright?"

  #
  li "Uh...yeah!"

  #"
  "His voice startles me and I jolt up, removing my hand from his in the process. "

  #
  li "Err..."
  show archer winterhappy
  #"
  "His laugh carries throughout the frigid air. "

  #
  ar "Strong independent woman, I get it. You don't need me to hold your hand."
  show lilah happyout at left 
  #"
  "His smile is contagious and I'm happy that I don't have to explain to him that his presence like this is making me so nervous that I can't even focus."
  scene bg gazebo with fade 
  show archer winterneutral
  show lilah happyout at left
  
  #"
  "We've stopped walking and my eyes fall onto a gorgeous sight. "
  
  #
  li "This is incredible!"

  #"
  "Before us lies a gazebo covered in snow.  The whole scene is picturesque. I can't fight the urge to run right into it and sit on one of the snowy seats. My butt gets soaked, but it's so worth it. "

  #
  li "How'd you find this place?"

  #"
  "Archer steps into the gazebo and leans over the ledge. "

  #
  ar "You didn't think I'd scope this place out as soon as I got here?"

  #"
  "Of course he would. Makes sense. "

  #
  li "Wow. I love it! But what does this have to do with my movie?"

  #
  ar "It's beautiful, right?"

  #"
  "When I nod, he continues speaking. "

  #
  ar "But nobody knows it's here. Not even you."

  #
  li "So?"

  #
  ar "So, I want to see if there's something hidden in your movie. Something beautiful."
  show lilah neutralout at left 
  #
  li "Like what?"

  #
  ar "I don't know. But something. When I first saw you on the train ride up here, I could see that you lived in your own world. I remember having that face myself when I was recording music as a beginning star. You get so enraptured in what you're doing..."

  #"
  "He runs his finger along the edge, picking up snow and then flicking it from his grasp. "

  show archer wintersad 
  #
  ar "I lost that feeling a long time ago. It's partially why I'm here."

  #"
  "I can feel my body tense up. Did he just admit that? When I asked him that same question before when we were watching a movie, he snapped at me. Now he's offering the answer up voluntarily. "

  #
  ar "When you were listening to music on the train, I saw that look. But your sister-in-law said you were a movie buff, so I wanted to see if maybe I'd get a sense of that passion. Ultimately, I'd understand you better. "

  #
  li "But I don't have the passion that you think I have. I'm here because I'm trying to get that passion back."
  show archer winterneutral
  #
  ar "For making movies, maybe. But you clearly have a passion for life. People could learn a thing or two from you. Lilah, you're annoying as hell but your appreciation of the things you're surrounded with, whether you want to admit it or not, is there."

  #"
  "I'm speechless. Archer has been watching me closely all this time and he's saying I represent to him an appreciation of life. I have passionate reactions to things. He wants to get that feeling back himself. "

  #
  li "I don't think there's a better place than Riversone to get some inspiration back."

  #
  ar "You're working on a movie script, right? So you must have some inspiration."

  #"
  "Archer doesn't realize that he's my inspiration."

  #"
  "He straightens himself up. "
  show archer wintersmile 
  #
  ar "You're fun to be around Lilah, even if you're the most annoying person I've ever met."

  show lilah happyout at left 
  #
  li "I'll take any compliment you give me."

  #"
  "Archer extends his hand again as he stands in front of me. "

  #
  ar "It's getting cold. Shall we go inside?"

  #"
  "When I agree with him, he retracts his hand. There's a playful glint in his eyes. "

  #
  ar "Strong independent woman."

  #"
  "I stand up instantly and nudge my elbow to his gut. "

  #
  li "Damn right I am. So, I'll be the one leading us inside."

  #
  ar "After you then."

  #"
  "The two of us head inside. Today was successful. I had a blast with Archer out here in the open pummeling each other with balls of snow. Who knows what else we have in store for us."
  hide archer with dissolve
  stop music 
  
label chapter5:
  scene bg transition with fade
  show transition_chapter5 with Dissolve(5.0) 
  
  scene bg NightBedroom with fade
  show lilah neutral at left
  play music music_home 
  
  "The light shining through the windows alerts me to a new day, but not just any day. Now that the snow festival is over, it's time to start preparing for the tree lighting ceremony!"
  #"
  "In New York City, the tree lighting at Rockefeller Plaza consist of multiple big-name celebrities performing their versions of classic holiday songs. Tens of thousands of people line up to get the best spot, and a tree from a random farm in upstate New York gets illuminated."
  #"
  "I'm pretty sure that doesn't happen in Riversone. I'm just excited to be a part of it and witnessing firsthand the community come together."
  
  
  #"
  "Despite my optimistic thoughts, my footsteps are sluggish and my body is sore."
  
  #"
  "Checking the time, I realize that I'm up an hour before my alarm. The thought of going back to bed is alluring but I know I won't wake up in time for my shift."
  #"
  "So instead, I get dressed and head outside to roam the now covered in snow inn grounds."
  scene bg fields
  show lilah neutralout at left
  play music music_autumn
  #"
  "It's absolutely beautiful out here. I breathe in the cold mountain air, cleansing my stuffy airways."
  #"
  "I reach up and wipe my nose. Well, crap. Am I getting a cold?"
  
  show lilah sadout at left 
  #"
  "This can't be happening now. I rub my hand up and down my arms. I do sort of feel a chill up my spine..."
  #
  show anjali neutral
  an "Good morning beautiful. What are you doing out here so early?"
  
  show lilah neutralout at left  
  #
  li "Huh? Oh, Anjali. Hey. How's it going? I just wanted to clear my head."
  #
  an "It's nice out here today."
  #
  an "I like to go by the gazebo to think about things. Have you seen it yet?"
  #
  li "Oh, Archer showed it to me. It's really nice."
  #
  an "Ah, it's no wonder someone like him was drawn to it."
  #
  li "What does that mean?"
  #
  an "He seems sentimental, no?"
  #
  li "Yeah, he does."
  #"
  "Archer is a guy with so much more depth than I had originally pegged him for. He's a caring guy, even if his actions and words can be a little abrasive at times."
  #
  an "Anyway..."
  #
  li "Hm?"

  #"
  "I look up at her."
  #
  an "This is the part where you deflect because we're talking about Archer."
  show lilah blushout at left
  #
  li "I don't deflect! I just think there are more interesting things to talk about..."
  #"
  "I'm grasping for straws here, hoping she doesn't notice the blush that I feel staining my cheeks."
  show anjali smile 
  
  an "Right, of course. Like what?"
  
  show lilah neutralout
  #
  li "Uh... Did you guys build the gazebo to host weddings and stuff?"
  
  show anjali neutral
  #
  an "That's your big interesting question? No one wants to get married here. The Inn is quaint, but that's about it."
  #
  li "I don't know, it's kind of romantic here. Like a Hallmark movie."
  show anjali smile 
  #
  an "Craig would be happy to know that. You know how he was."
  #"
  "There was an opportunity left open for her to make fun of me, but instead she focuses on something much more meaningful."
  show lilah happyout at left
  #
  li "Yeah, my brother was always a sweet romantic. I know you guys must've held hands out by the gazebo."
  #"
  "I can't help but tease her, and honestly Anjali looks really happy."
  #
  an "Did you know that the gazebo was already on the property when we purchased the inn?"
  show lilah neutralout 
  
  #
  li "Oh, a selling point then."
  
  show anjali sad
  #
  an "Precisely."
  show anjali neutral 
  #"
  "She looks distant for a moment, and then snaps out of it."
  #
  an "Would you like me to fry us up some eggs this morning?"
  #
  li "No, that's okay. Don't worry about me. I just want to sit out here for a bit."
  #
  an "Alright. When you're done let me know. We can discuss today's agenda."
  
  hide anjali with dissolve
  #"
  "Anjali politely excuses herself, leaving me alone with nature."
  
  #"
  "I wish my mom was here to see this. She never really properly visited the place my brother and Anjali invested so much time, money, and effort into. Aside from seeing the business her son built, I think the fresh air will do her good."
  #"
  "I know she'd be against it, but I really want to end my trip early. Being with Anjali and Archer has been a lot of fun, but all good things must come to an end eventually. I'd like to stay in Riversone a little longer, but I don't want to leave my mother alone any longer."
  show lilah sadout at left
  #"
  "Hearing Silent Night playing in the background when we talked still twists my insides. How much torture can one woman take? She doesn't even have dad to lean on anymore."
  #"
  "I tighten the top button on my coat. A chill runs through my body and I can't attribute it to a growing fever or below average temperatures. This is the same feeling I got when my mother first put a plate out for Craig's dinner after he was gone."
  #"
  "It is an absolutely morbid feeling that consumes me for a few brief moments. I try to block out the last images I have of my mother cradling his lifeless body."
  #"
  "Just like that, a simple moment can dredge up the past. There is no running from it."
  
  scene bg black
  "I close my eyes and try to center myself so that I can work efficiently today."
  
  scene bg fields with fade
  show lilah sadout at left 
  #"
  "When I open my eyes, everything has stayed the same. I'm still outside of my cabin freezing. Except now, my mother's voice and that song are much lower – just distant buzzes in the back of my mind."

  #"
  "I decide that nature's healing breeze isn't so healing anymore and I need to head inside before I begin to cry and my tears freeze. "

  scene bg lobby
  show lilah neutral at left
  stop music
  play music music_home

  #"
  "Upon entering the Inn, I hear Archer and Anjali talking about something. I don't bother straining my ears to hear. "

  #
  show anjali neutral
  show archer neutral at right
  an "Ah, the woman of the hour. There she is."

  #"
  "I look up, startled that both sets of eyes are on me. "

  #
  li "Oh, uh hi? How's it going?"

  #"
  "Archer lifts his hand up in a small wave. "

  #
  ar "Good morning, Lilah."

  #"
  "It's so strange hearing him say my name. I want to just crawl under a rock and hide..."

  #
  an "We were just talking about the tree lighting ceremony. I'm going to be giving you the night off for it."

  #
  li "Oh, it's okay. I really don't mind."

  #
  an "Archer says he's going too so I'll just close the Inn and we'll all go together. Well, if Mr. Lane doesn't mind."
  show archer smile at right
  #
  ar "As long as you show me the best spot to see it all go down."
  show anjali smile 
  #
  an "That's Riversone's best kept secret but I can oblige for you two."

  #"
  "She winks. "
  show lilah sad at left
  #
  li "Sorry we didn't win those tickets to sit up front."

  show anjali neutral 
  show archer neutral at right
  show lilah neutral at left 
  #
  an "Oh, trust me. The front is not all it's cut out to be. You have to deal with Riversone's snooty council."
  #"
  "I know she's joking but I still feel a sense of nervousness wash over me. I've never asked how Anjali feels about the council or how she tolerates them. "
  
  #
  ar "I want to be part of the crowd for once, so steering clear of the front is probably best."

  #
  an "Okay good, now that we've got that all sorted out, get to work Lilah. Mr. Lane, enjoy your stay."
  hide anjali with dissolve
  show archer neutral at center

  #"
  "She turns around and leaves, having other things to attend to. Looks like I'm manning the front desk today."
  
  #
  li "So, Archer..."

  #"
  "I begin to speak when I notice Anjali is out of sight. "
 
  #
  ar "Yes, Lilah?"

  #
  li "Are you really okay with coming with us? You really don't have to. If you feel cornered, I can just talk to Anjali."

  #
  ar "No one wants to be alone, Lilah. Especially not during this time of year. I'm very thankful that Anjali invited me. I think it'll be fun."

  #
  li "Oh...good then."

  #
  ar "Is it good then? Do you not want me to come along?"

  show lilah blush at left 
  li "N-o! That's not it at all. I just want to make sure we're not bugging you."
  show archer smile at right
  #
  ar "Well, what can I say? You guys are growing on me."

  #"
  "Did he just....?"
  show lilah happy at left 
  #"
  "I can't help but smile. "

  #
  li "Did the great Archer Lane just say that?"
  show archer neutral 
  #
  ar "I did but don't press your luck. I'm going to deny it every single time."
  show lilah neutral at left 
  #
  li "Your secret is safe with me."

  #
  ar "Thank you, Lilah."

  #"
  "Though I have a feeling he isn't talking about my little joke."

  #
  li "Oh uh...you're welcome."
  show archer smile 
  #
  ar "I'll see you around. Gonna head out and sight-see some more."

  #
  li "Okay, have fun."
  hide archer with dissolve 
  #"
  "I wave at him and he genuinely smiles back in my direction. It feels so awesome knowing that he doesn't hate me."
  scene bg black with fade

  #"
  "The rest of the day goes by very slowly. Responding to emails is not a fun thing, but I power through it. "

label chapter6:
  scene bg transition with fade
  show transition_chapter6 with Dissolve(5.0) 
  "NEXT WEEK"

  #"Lilah's Cabin"
  scene bg NightBedroom
  show lilah sad at left
  #"
  "I can't stop coughing. When I try to pull myself out of bed, the cold hits me a little too hard. Yep, I'm definitely sick and on the day of the tree lighting ceremony too..."

  #
  li "Ughhh...."

  #"
  "I don't even have the energy to pull myself to the phone and call Anjali. Let me just lie here for five more minutes..."


  scene bg black with fade
  scene bg NightBedroom
  show lilah neutral at left 
  play sound sound_doorpound
  #"
  "I wake up to the sound of pounding on my door. Huh...?"
  play music music_autumn
  #"
  "Oh no!!! "

  #"
  "I realize that I've slept through my alarm and Anjali is probably waiting for me..."

  show lilah blush at left
  #
  li "One minute...!"

  #"
  "My voice is hoarse as I call out to my visitor. I jump up from my bed, hugging the blanket tightly around myself. "
  show lilah neutral at left
  #
  li "Hello?"
  show anjali sad
  #"
  "I open the door to reveal a very concerned looking Anjali. "

  #
  show anjali neutral
  an "Is everything okay?"

  #
  li "Uhm...."

  #"
  "As soon as I begin speaking, she realizes that something isn't right. "

  #
  an "You look terrible. Riversone's cold air finally got to you, huh? Go lay down."

  #
  li "I'm fine."

  #
  an "You're not fine! Look at you, you've got a cold."

  #"
  "She doesn't ask for my permission, she simply places the back of her hand on my forehead. "

  #
  an "You're burning up. You need to rest."


  #
  li "No, I'm fine. I can work. I want to go to the tree lighting ceremony later too...."
  show anjali neutral 
  #
  an "If you rest now, you might feel good enough to go tonight."
  show lilah sad 
  #
  li "Anjali, no...what about Archer?"

  #
  an "I can attend to his needs today. That's not a problem. Your health comes first, he'll understand that."

  #"
  "Hah, Archer will probably be happy not to have to deal with me today."

  #
  an "Don't say but. You're going to rest and that's final."

  #"
  "She begins to push me towards my bed. I have no choice but to oblige. Despite wanting to go to work, my body just won't let me. "


  show lilah neutral at left
  show anjali neutral

  #"
  "Anjali tucks me into bed, kissing me on my forehead as a mother would."

  #
  an "Do you want soup?"

  #
  li "No, I'm good. I think I'm just going to sleep some more."

  #
  an "Okay, just call me if you need anything. Some soup, cold medicine, some company...anything."
  show lilah sad at left 
  #
  li "I really want to go to the ceremony, Anjali."

  #"
  "I mumble those words as I curl up into my blanket. "

  #
  an "Rest up, sweetheart and we'll try our best to get you there."

  #"
  "I close my eyes and lull into a slumber. "

  scene bg black with fade
  show lilah sad at left

  #"
  "Ugh....everything is so dark....what's going on??"

  #"
  "I roll over, my back aching as the cold air hits it. I feel like total crap..."
  
  #"
  "It's got to be late afternoon by now."
  
  scene bg NightBedroom
  "It takes a minute or two to orient myself, but I realize that I'm in my cabin, sleeping off my fever. "
  show lilah blush at left
  #
  li "The tree lighting ceremony...!"

  #"
  "Normally I wouldn't care so much about this, but I feel like it's something connecting Archer and I. "

  #"
  "I really want to spend more time with him. I feel like we're getting closer. "

  #"
  "It has nothing to do with my script anymore. I don't care about that. I really think Archer could use a friend, and frankly, I could too. "

  #"
  "I pull my body upwards and drag my body towards the door. I feel like the room is spinning but I can't stop walking. I need to get up and move around. "


  scene bg kitchen
  show lilah neutral at left
  show anjali neutral 
  #"
  "I stumble towards the kitchen where I see Anjali preparing a meal. "

  #
  li "Huh?"

  #"
  "Still being a bit disoriented, I rub my eyes. "

  #"
  "Nope, this is not a hallucination. She's still there with her head poked over a pot of what I can only assume is full of something that she's boiling. "


  #
  show anjali neutral
  an "I see you're awake. How are you feeling? Better?"

  #
  li "Maybe worse."
  show anjali sad 
  #
  an "Worse!? You need to warm up, it's a bit chilly in here."

  #
  li "Did you ever leave?"
  show anjali neutral 
  #
  an "Yep, but Archer doesn't need a lot of maintenance so I decided to come check on you and make some of my famous chicken noodle soup and ginger tea."

  #
  li "Sounds good."

  #
  an "I know you hate tea, stop it."

  #
  li "Anything to make me feel better."

  #
  an "Let this warm you up and then you can take some medicine. Archer should be back by then."

  
  li "Huh?"

  #
  an "Oh! When he heard you were sick, he volunteered to go and pick up some medicine for you."

  #
  li "What? Archer did that?"

  #
  an "I was surprised too. He's taken quite the liking to you, huh?"

  #
  li "Or, he's just being nice."
  show anjali smile 
  #
  an "Mhmm...whatever you say."

  #"
  "A hint of amusement dances behind her eyes."

  #
  an "Make sure you thank him."

  #
  li "I will."
  show anjali neutral
  #"
  "A moment of silence passes between the two of us until I finally find my words. "

  #
  li "Uhm...do you think I can sit in the inn with you? I don't want to be alone."

  #"
  "I would feel more comfortable knowing Anjali is nearby if I feel any worse. Plus there's a TV so I can watch the tree lighting ceremony. I can at least be there in spirit."

  #
  an "Yes. Of course, sweetie."

  #"
  "She slides a piping hot mug towards me. "

  #
  an "Drink up."

  #"
  "I do as she says. The liquid burns my throat but the heat warms me up, and that already makes me feel a lot better."

  #"
  "When I finish up my tea and soup, I put on some shoes and head to the inn with Anajali, my blanket still wrapped tightly around myself. "

  scene bg lobby
  show lilah neutral at left
  show anjali neutral with dissolve
  show archer neutral at right with dissolve
  #"
  "Archer is standing at the front desk with his back turned to us when we enter. He seems to be absently flipping through a magazine that has to be at least a couple years old. The pages are curled up and the cover is nearly torn from the flimsy binding."
  #
  
  an "You're back."
  show archer smile at right 
  #"
  "Archer looks up, a smile placed on his handsome face."
  #
  ar "Yeah, I uh... Didn't know which one to get so I kind of just bought all of the cold medicine..."

  #"
  "He's thrust a white bag brimming to the top with stuff towards Anjali."
  
  #
  ar "Oh and there's some tea bags, a blanket, and orange juice."
  #"
  "He finally seems to notice me and takes a step backwards, bumping into the table behind him."
  show archer blush at right 
  #
  ar "Lilah! Uh...I thought you would be sleeping..."
  show lilah happy at left 
  #"
  "I sniffle and let out a hoarse laugh."
  #
  li "Busted. You do care about what happens to me."
  #
  ar "If you're sick, then there's a high chance that I'll get sick because you're working with me and there's like only three of us here..."
  #
  li "Right, of course. It'll be like the plague and we'll all be infected. Next thing you know, the zombie apocalypse begins."
  #
  ar "So, I'm saving humanity. You're welcome."
  #
  li "Thank you for your kind service."
  #"
  "It really does mean a lot to me that Archer would go out of his way to buy me medicine. He didn't just pick a random thing off the shelf like I was some kind of burden to him. He even thought to get me a blanket and some tea to make me feel better."
  #"
  "Maybe the total jerk Archer Lane, isn't the real Archer Lane at all..."
  #
  ar "Stop smiling at me like that."
  #
  li "It's called gratitude. Get used to it. It's supposed to be something nice."
  #
  an "I appreciate it as well. You're our guest, we're supposed to be caring for you."
  show archer neutral at right 
  #
  ar "You and Lilah have done more than you realize for me. So, a little shopping doesn't bother me at all."
  
  show lilah sad at left 
  #"
  "I decide to address the elephant in the room that's probably only really bothering me. With a heavy heart, I look up at Archer and then Anjali."
  #
  li "I'm probably not going to be able to go to the tree lighting ceremony tonight."
  #
  an "Don't even worry your little head about it. We can watch it on television together. I'll still tell Archer my secret spot for the best viewing."
  show lilah neutral 
  #
  li "Oh, no. You have to go. I don't want to mess with your tradition and Archer hasn't seen it before. So, I want you guys to go. Don't worry about me, I'll probably just sleep through the night."
  #
  ar "If you guys are staying, I'm staying too."
  #
  li "Please, go."
  #
  ar "Things aren't as fun when you're alone. Maybe I can crash on the couch and watch it on television with you guys?"
  #
  an "I don't mind, please don't feel as if you need to do anything. The tree lighting is really a fantastic experience up close."
  #
  ar "Lilah said something to me the other day about Christmas magic. I don't know if it exists, but I doubt a sparkling tree is going to show me that. The movies always say that it's family and friends and giving."
  #"
  "He takes a long look at Anjali and then his gaze settles on me."
  #
  ar "I know that you're excited to go see the tree. I'm not going to rub that in your face by having a good time without you. So, if you have me I'll be more than happy to spend more time with you ladies."
  show anjali smile
  #
  an "If you're trying to say that you enjoy our company, we accept the compliment."
  show lilah happy at left
  #
  li "If it really doesn't bother you, I would love to have you here."
  show archer smile at right
  #
  ar "No, it doesn't bother me. But hey, let me get dinner tonight. We can have some hot chocolate and maybe some of Lady Lacy's famous chocolate cake?"
  #
  an "That would be very nice, thank you."
  hide archer with dissolve 
  hide anjali with dissolve 
  
  scene bg livingroom
  show lilah neutral at left
  show anjali neutral with dissolve
  #"
  "With that, Archer leaves to go buy some food for our little viewing party. I'm curled up on the couch with my blanket wrapped tightly around me. Anjali is standing not too far off."
  #
  an "That was very nice of Archer."
   
  #
  li "He likes me."
  #"
  "My voice is full of disbelief, considering the rocky start he and I had together."
  #
  li "Can it be that he really does want to be my friend?"
  #
  an "You two are very much alike. I can't believe that you don't see it yet."
  show lilah blush at left
  #
  li "What? How are we alike? He's glamorous, sophisticated, not to mention good-looking and funny."
  #"
  "I even surprise myself with that admission."
  #
  li "I know that I'm unlikable. I can be rude, I'm way too absorbed into my own feelings, and I'm too full of pride."
  #
  an "You're both full of pride. It was very hard for Archer to admit that he was concerned about your well-being. Just like it's hard for you to admit that you're starting to get attached to him."
  #
  li "I'm not..."
  #"
  "I let out a heavy sigh."
  #
  li "I'm getting attached to him. I don't know what to do about it."
  #
  an "Embrace it. Some of the best things in life happen when you share moments with other people. For so long it was just you and your mom. Don't you think that it's a good thing for you to be branching out and letting other people in?"
  show lilah sad at left 
  #
  li "I want to. But it's not that easy. With Archer it's even harder because I know that he's going to leave too."
  #
  an "Not necessarily."
  #
  li "He has so many other things going on in his life. Do you think he's going to remember the girl who he spent a few weeks with?"
  #"
  "My heart feels like it's constricting. I don't want to like Archer. I wish we never even met at all. Things would be much easier that way. I don't know how many more times I can say goodbye to someone."
  show anjali sad 
  #
  an "I thought about this same thing when I found out that Craig was gone. I said goodbye to my mom, to my dad, to my siblings... so saying goodbye to the one person who was a constant in my life was the hardest thing I've ever had to endure."
  "I thought for sure that I would never ever let anyone else in again. Not even friends, because I never wanted to feel that low again."
  #
  an "I isolated myself in the mountains but people wouldn't stop trying to get me to let them in. Finally I just had to let my resolve go and it was the best thing I've ever done. Because no matter how small the amount of time spent with me, each and every person I've met has impacted me in some way."
  show anjali neutral 
  #
  
  an "So, even if he says goodbye you can look back on this and be grateful for what he helped you to realize."
  show lilah neutral at left 
  #
  li "Which is what exactly?"
  show anjali smile 
  #
  an "I don't know, you tell me."
  #"
  "She's smiling at me like she has all the secrets of the world stored away in her brain. She obviously sees something that I don't. Still, I can't fathom that Archer staying at the inn is something much more than just that."
  #
  an "You worry too much about things. Everything happens for a reason. Even the bad things in our life make us stronger. You can't dwell on things that you don't even know are going to happen or not."
  #"
  "I know that she's right but it's so much harder than simply following advice. I know that I'm a lot more closed off now than I've ever been. I just don't know what to do about it."
  #"
  "I lay my head flat on a sofa cushion, trying to push the negative thoughts in my brain away. It's supposed to be a fun evening, yet my anxieties never fail to resurface."
  #
  li "I think I'm just going to take a nap until Archer gets back."
  #
  an "Yes, of course. I'll get some work done so that were not swamped this weekend. Feel better, sweetie."
  scene bg black with fade
  #"Background is back"
  scene bg livingroom
  show lilah neutral at left
  show anjali smile 
  show archer neutral at right 
  #"
  "When I wake up, Archer and Anjali are talking as if they've known each other for years. It's a really nice sight."
  #
  
  an "Morning sleepyhead."
  #
  li "Ugh...I'm going back to bed."
  #
  ar "You're going to miss the tree lighting."
  #
  li "...Fine."
  #
  ar "How are you feeling?"
  #"
  "I straighten myself up. Archer is sitting on the floor leaned against the couch I've been sleeping on. Anjali is seated on the loveseat across from us."
  show lilah sad at left
  #
  li "I don't know."
  #"
  "Physically, I still feel pretty bad. Emotionally, I want to be upset but Archer's smiling face brightens my mood. I don't know why he has this effect on me."
  #
  an "You have perfect timing, Lilah. It's just about to start."
  show lilah neutral at left 
  #"
  "She points at the television and I'm relieved that I don't have to answer any more of Archer's questions, as well intentioned as they are."
  #Announcer"
  ann "Welcome to Riversone's 96th annual Tree Lighting Ceremony."
  #"
  "There aren't a million people gathered, but I'm still amazed. In the center of town, there are about a hundred or so people gathered around a Christmas tree. They're all awaiting the lighting anxiously."
  #"
  "If you really think about it, they're all just waiting for some guy to flip a switch. It's really not that exciting and yet...even I've bought into the hype."
  #
  li "That's Christmas magic, Archer. Right there, in the eyes of those people who are so thrilled to be standing in the cold waiting for a flip to be switched."
  #
  
  "Archer is silent for a moment, pensive even."
  #
  ar "You notice things that other people don't."

  #
  li "What do you mean?"
  #
  ar "No one is thinking about how every person in the crowd is feeling. Regular people are focused on the tree."

  #Lilah"
  li "But there would be no tree without those people. Think about all the families who buy Christmas trees and set aside a day or an evening to put on the ornaments."
  li "Some people just decorate the tree as if it was a chore. Other people make it a ritual. They have a specific way that they do things and they share that tradition with others."
  #
  li "If there was no one who wanted to engage in a community tradition, there would be none. Riversone's Christmas spirit was created and is maintained by the people."
  "You and I are from a world where our senses are pelted with bright red and green lights, sparkling silver bows and oversized candy canes in an attempt to lure people in."
  #
  li "The difference is that the people around me, they didn't let me see Christmas as anything but a time meant to be celebrated with family. It's supposed to be a time of love."
  #
  li "It's hard to see it sometimes, and I know that better than anyone. But, we're not the only ones living in the world. If we are only focusing on the objects, we are missing out on some really great characters, motivations, personalities and I'm not even talking about for a script."
  #"
  "The room is silent for a moment and I don't know what to make of it."
  show archer smile 
  #
  ar "That was incredible."
  show lilah blush at left 
  #
  li "Uh..."
  #
  an "Very well put."

  "I'm embarrassed and I look away from the two of them."
  #
  ar "It's cliché to say this but I really do mean it. If more people thought like you, the world would be a better place."
  show lilah neutral at left
  #
  li "I don't want you to hold my ideals in some kind of position to be revered. I'm just saying how I think about things, it doesn't have to be the way that everyone thinks of things."
  show archer sad at right 
  #
  ar "And here you are fighting back on the compliment."
  #
  an "It's called self sabotage."
  #"
  "I ignore Anjali's remark. I'm not pushing back on Archer because of what I said earlier. I just know that the world would be no better with more of me. I have made no impact."
  show archer neutral at right
  show anjali neutral
  show lilah neutral at left 
  stop music
  
  #"
  "The tension grows as the three of us watch the lighting silently. There is some musical buildup, with local singers doing Christmas carols. But other than that, there is nothing flashy about the ceremony. The focus switched, the tree lights up, and people cheer."
  #"
  "I feel a mix of emotions. There is happiness that I'm not alone on this evening, apprehension that Archer could even say something so highly of me, and fear of what's to come next."
  #Announcer"
  ann "Tonight, we will be doing something a little bit differently. In honor of what the holiday is all about, we will be ending the ceremony by singing Silent Night together. Because though it is quiet tonight, great things have come about for our community and for our faith."
  
  play music music_silentnight
  show lilah sad at left
  #
  li "Not now." 
  #"
  "I place my hands over my ears to block out the sound, which I know is useless."
 
  show anjali sad 
  show archer sad at right
  #
  an "Lilah..."
  #
  li "No, I can't right now. There are too many emotions inside of me and if I hear that song..."
  
  #"
  "But the people of Riversone are oblivious to the three of us sitting in the inn's lobby. They continue their song with no remorse. For them, it represents a moment of togetherness."
  "To me, it signifies a moment of loneliness. Except, my loneliness will outlast their excitement. It doesn't come around once a year."
  
  hide anjali with dissolve
  hide archer with dissolve
  scene bg brown1
  stop music 
  show lilah sad at left
  #"
  "I stand up and walk out of the room without another word, not caring that Archer has seen me storm out immaturely."
  #"
  "I need a second to compose myself. I'm not angry at Archer or Anjali. I'm angry at the world for taking away my brother and making me a timid and fearful girl. But more than that, I'm mad at myself for letting it wear me down so much."
  "That strong girl that Anjali and my mother claim I am, is a false front and all it takes is a stupid song to dismantle the security I've built around myself."
  #"
  "I realize that my hands are shaking and my body is trembling. I take in a deep breath and exhale."
  
  if archer_score > archer_comfortScoreNeeded:
    #"If enough points with Archer:"
    show archer sad
    play music music_silentnight
     
    #
    ar "Hey, if I said anything in there to make you upset or to second-guess yourself I'm sorry. I really do think it's amazing the way that you think about people and how you see the world. I wasn't trying to make you feel bad about that."
    #"
    "Of course I'm so focused on myself that I didn't even hear Archer enter the room. Isn't it common sense that when someone is upset you leave them alone?"
    #"
    "Yet there is part of me that is saying not to take out my insecurities on Archer. He has said nothing wrong to me. He's even come to check on me and apologize sincerely."

    #
    li "It's not you. It's that stupid song, Silent Night. I hate it so much."
    #
    ar "Can I ask why? You don't have to tell me."
    
    show lilah mad at left 
    #
    li "Mr. Don't Ask Personal Questions wants to know about my life?"
    #"
    "I don't mean to sound rude, rather I'm just surprised. I still can't get over the fact that Archer cares enough about me to be asking these questions."
    show archer neutral 
    #
    ar "I'm not asking to exploit you. I'm not asking because I'm being nosy. I'm not asking for any personal gain of my own. I'm asking you because I care. You might not really think that I have a heart, and sometimes I don't think I do either, but for you..."
    #
    ar "Let's just say that you have been one of the only people that hasn't treated me like I'm some huge celebrity. You've regarded me as another human being, and I can't help but have concern for the person who has made me feel like the old Archer Lane. The one from before I was a household name."
    show lilah sadblush 
    #"
    "My heartbeat begins to quicken and I can't believe what I'm hearing."
    #
    li "Is that what you meant when you said Anjali and I have done more for you than we realize?"
    #
    ar "Yeah. I mean I told you what those girls did when we were at the snowman building competition. I've always had to be a little bit careful, but you've honestly proven to me that there's no reason not to trust you. You don't care about gaining anything from me."
    #
    show lilah mad
    li "Yes, I do. There's so much that I want to gain from you, but how do you tell someone that? How can I tell you that I want to know more about you when you don't want to talk about yourself?"
    #"
    "I shake my head and hug my arms around myself."
    #
    li "It's true. I don't care about the money or your fame or your accomplishments. I mean at first I wanted to know more about you so that I could write this really cool character for a script. Which I guess are probably mad about..."
    
    
    #
    ar "I'm not. I can't be mad at you for wanting to create art. Everyone takes motivations from everywhere and then we twist that to fit our expression. But, that's not what's bothering you is it? Why does Silent Night bother you so much?"
    
    show lilah sad at left
    #"
    "It's hard to look up at Archer while I say my next few words."
    #
    li "Silent Night was my older brother's favorite Christmas song. He committed suicide a few years ago and nothing has ever been the same."
    show archer sad
    #"
    "There is a moment of silence and then Archer reaches out to place a warm hand on my arm."
    #
    ar "I'm sorry to hear that."
    #
    li "You have nothing to be sorry for. I don't know why people say that. Everyone is always apologizing to me for something that the world did. Craig didn't kill himself because of you."
    #
    ar "No, but that doesn't mean people can't express their condolences. They're apologizing on behalf of the world for what you have to deal with."
    ar "It's not something that will heal the wounds that you have, but I'm just offering up my words of support. I don't think that anyone should have to deal with loss, but it's something that makes us human."
    #
    li "I know that loss is unavoidable. But, you never really think that it's going to be so close to you. I mean, I lost Craig even before he took his life. He was a soldier and after having come back from active duty, things just never really seemed so bright for him anymore."
    #
    li "I could see that moment in his eyes when the lights flickered off. Even Anjali, the woman he loved more than anything, couldn't make him smile. I was seeing someone who I relied on for strength crumble right before my eyes."
    #"
    "There are tears building in those same eyes but I don't even bother trying to fight them."
    #
    li "It was always just my mother, my older brother and I. My dad passed away of a heart attack early on in our lives and Craig kind of took the patriarch role. No one ever told him that he had to, but he just felt like he needed to hold that onto his shoulders. I think that it was his way of coping at the time."
    #
    li "During our family gatherings at Christmas time, he would wear a Santa Suit like my dad used to and my mom would pretend like the reindeers had landed on our roof."
    #"
    "The memory brings a smile to my face."
    #
    li "It was nice to pretend for a little while, but then I grew up and Craig didn't need to pretend he was Santa anymore. He didn't have to walk in my father's footsteps anymore."
    li "He wanted to do something more with his life, but he never really knew what. He just knew that he wanted to change the world somehow."
    #
    li "For some reason enlisting in the military was the way that he thought he was going to do that. Uh..."
    #"
    "The right words are hard to find in this situation, but I scrape for them in my mind and my heart."

    #
    li "Of course my mother and I were against it, but he had made up his mind a long time ago. There wasn't going to be anything that would stop him because Craig was always just so headstrong."
    li "If you told him not to do something, he would try even harder. But he didn't join the military to spite us or anything like that."
    #
    li "He really just wanted to change the world. One fight at a time, I suppose. I can't even imagine the kinds of things that he had seen when he was on active duty, he would never ever tell us. I don't even think he confided in Anjali."
    #
    li "He was really into really upbeat Christmas songs but after the last tour that he did he had found his solace in Silent Night. I never really understood his connection to that song. It just... It made him calm I guess."
    #
    show archer neutral
    ar "Music can be a very powerful thing. The way that we interact if it is unique to ourselves, so a song that meant a lot to him could mean little to you. But that's nothing that you need to feel bad about."
    #
    li "Oh, I know. But the human brain is a funny thing. Every time I heard Silent Night being played, I didn't attribute it to a happy time of year. To me, it just meant that he was having these bad feelings again that he needed to calm down."
    #"
    "It's gross, but I wipe my eyes and runny nose on my sleeve."
    #
    li "Hearing that song makes me feel so helpless because it reminds me what was so obvious. He was crying out for help but I didn't even hear him. I thought he was just listening to a song because he was feeling sad. He was more than sad and I was so oblivious."
    #
    ar "I want to tell you that you can't blame yourself for this, but knowing you you'll fight me on it."
    #
    li "Yeah, because I know in the back of my mind that there was something that I hadn't tried. I wasn't paying attention enough."
    #
    ar "You can't change the way a person feels."
    #
    li "You did. The last few days you made me feel like I've been in a different world. I was able to forget things as long as I was dealing with you annoying me. It was nice."
    #
    ar "But did I change the way you felt or did I mask it?"
    #"
    "I think about that for a moment. I'm not quite sure about that."
    #"
    "I only shrug."

    #
    ar "There are things in life that are deeply personal, things that no one really has the power to change. Sometimes things happen...sometimes life throws a hurdle at you..."

    #
    li "He watched people die on the battlefield, that wasn't a hurdle."

    #
    ar "I'm not articulating myself correctly. I know I don't have to say anything to make you feel better. You're not telling me about your brother's death for my sympathy..."

    #
    li "No, I'm not."
    show archer sad 
    #
    ar "But I still want to offer my comfort. I don't want to see you cry."

    #
    li "But, that's life. Right? You don't get to choose what happens sometimes. You just..."

    #"*screen shake*"
    show bg brown1 with hpunch
    #"
    "In an instant, my voice stops. Archer has pulled me into his chest in a warm embrace."

    show lilah blush at left
    "!!!!"
    show archer blush

    #
    ar "Since I can't find the right words, how's this?"

    #"
    "He strokes my hair with one hand, and my back with the other. "

    #
    li "I'm sick, you moron."

    #"
    "I mumble against his chest. Though, I don't really want him to release me. I'm enjoying the way his arms feel around me. "

    #
    ar "Yeah, I don't really care. Not like I have anything to do in the next few days anyway."

    #"
    "Racing thoughts pound my head. Why is Archer being so nice? Is this some kind of practical joke? Why is his body so warm? Why is my heart racing? Why don't I want him to let me go?"

    #"
    "Eventually Archer pulls away from me and he straightens out his shirt which is wet with my tears. "
    show archer neutral
    show lilah sad at left

    #
    ar "If you tell anyone about this, I'm going to deny it."

    #"
    "My heart sinks. I'm reminded of the distance between the two of us. It's not only physical now."

    #
    ar "No, stop that frowning. I'm only joking. If I hear you say one more time that I'm some untouchable celebrity..."

    #
    li "It's true, isn't it?"

    #
    ar "No, it isn't. It's not true, Lilah. I'm right here talking to you. Aren't I?"

    #
    ar "I don't believe that you really believe that. I think you want me to be some untouchable celebrity. The same way that I want you to be an annoying exploiting fangirl so that I don't have to get too close."

    #
    li "Anjali told me that. She said she could tell when you thought people were getting too close."

    #
    ar "Anjali knows best, doesn't she?"
    show lilah happy

    #"
    "I laugh quietly."

    #
    li "Earlier she said that you and I are alike. I denied it, but maybe."
    show archer talk
    #
    ar "You're too headstrong. I'm nothing like that."
    show lilah mad
    #
    li "Pft! Yeah right!"

    #
    ar "Hey, I'm very accomodating. You're stubborn, loud, aggressive at times..."

    #"
    "I hit his arm and glare at him."

    #
    li "I open up to you and this is how you treat me?"


    show archer smile
    ar "You're still a De Luca fan."

    #
    li "Because he isn't a jerk."

    #"
    "Archer reaches out and wipes an almost dry tear from under my right eye with his thumb. "

    #
    ar "Well just remember that De Luca isn't the one who's comforting you right now."

    #"
    "He winks and walks towards the door. "
    
    #
    ar "When you're ready, there's chocolate cake."

    #"
    "I reach up and wipe the remaining tears that stain my face. "

    #
    li "How can I say no to that?"
    hide archer with dissolve 

  else : #"Comfort with Anjali: "
    stop music
    scene bg brown1
    show lilah sad at left
    show anjali sad
    play music music_silentnight
    
    #
    an "Sweetie...are you okay?"

    #"
    "I look up to see her body leaned against the door frame. There is a familiar sad smile on her face. "

    li "Who sings Silent Night at a tree lighting anyway?"

    #"
    "She approaches me and puts her arm over my shoulders. "

    #
    an "It's a lovely song."

    #
    li "Yeah, well I hate it."

    #
    li "Craig would listen to it nonstop during the holiday season. Especially those last few years..."

    #
    an "Because it calmed him."

    #
    li "Why are you defending that stupid song?"

    #
    an "Lilah, the song didn't kill your brother."

    #
    li "I know that."

    #"
    "There's something about the way she spoke those words...My outburst leaves my lips unbidden. I feel my control slowly slipping. How can Anjali be so blunt?"

    #
    li "Of course I know that. It's just a song."

    #
    an "A song that is clearly bothering you. What does that song mean to you?"

    #"
    "It's something I've never had to confront before. It's something I've always run away from. "

    #"
    "When Craig was in his early twenties, he took the college degree he earned in finances, tossed it out the window #(quite literally) and joined the military. He always said that he wanted to do more with his life. More than counting numbers anyway. "

    #"
    "He assured my mom and I that he wouldn't ever actually have to serve on the ground, but one day he was called in for active duty and he didn't exactly decline. "


    #"
    "Then he began to explain to us that he would be fine. Yet another lie. When Craig came back from fighting in the war, everything changed. "

    #"
    "He was much more serious, like all the time. He never smiled- really smiled, not those half thin lipped smiles he gave when he didn't want us to pester him. Craig had seen things he didn't want to tell anyone about. Not me, not mom and certainly not Anjali. "

    #"
    "So, no one knew how badly he was feeling inside until it was too late. Maybe he had felt this way his whole life and never told anyone, or maybe seeing people die so up close made him feel a turmoil so intense that he felt the need to end his own life. "

    #"
    "Whatever it was, it took Craig from us. "

    #
    li "Silent Night...."

    #"
    "I begin my sentence and let the words hang in the air. I hate them. Every single night feels like a silent night with Craig gone and it is deafening. Nothing is calm and nothing is bright. "
    show lilah mad
    #
    li "He listened to that song all the time like it would save him or something. Like...it had the powers to zap his sadness away! I thought that just because he smiled when he listened to it, that it was enough to keep him happy."

    #
    li "Of course it wasn't. It's just a stupid song! That's all it ever will be. A song."
    show anjali neutral 
    an "It made him happy, Lilah. It did, it really meant so much to him."

    #
    an "So much more than you know. Probably even more than I know."

    #"
    "She begins to walk past me to the front desk where she begins to rummage through stuff. "

    #
    an "You may have only seen Craig listen to that song when he was home from the war. But, that's not the only time he's listened to it."

    #"
    "She holds up a small black flash drive as if it holds the world's most important treasure."

    #
    an "When Craig was first stationed in Iraq, he had called me one day to video chat. I used to record all of our conversations together but a hard drive crash wiped everything clean. I was so angry that I had lost the only memories of Craig that I thought I had."

    #
    an "But one day, while I was going through stuff here at the inn, I found this flash drive. I hadn't ever seen it before but curiosity got the better of me and so when I put it into the computer, this played."

    " #"
    "Anjali plugs in the flash drive and clicks a few things before a man's voice comes out of the speakers."

    play music music_craig1
    show anjali sad
    show lilah sad 
    #"
    "Is that my brother's voice? It sounds so vivid. "
  
    #"
    "I can see Anjali tearing up for the first time, though she quickly turns her head so that I only see a frown. "

    #"
    "I place a hand on my heart, a sob threatening to break out of my chest. I can't hold it in."

    #
    li "He sounded so full of life."

    #
    li "How can he be like that in one instant and the next..."

    #"
    "How can someone who sounded so happy be so unhappy? "

    #
    an "See, why do you do this to yourself? You keep reliving the past over and over again. None of it is your fault."

    #"
    "She says that, but how can I feel any different? He was depressed right in front of my eyes and I didn't even see it."


    #
    li "I..."

    #
    an "There's nothing you could have done. There was nothing any of us could have done. He was sick. Craig thought there was no other way out. He made a conscious decision to do what he thought was right and I can't hate him for that."
    show lilah mad
    #
    li "But...you heard him! He wanted to start a family with you! How can you not be angry that it was all taken away from you?"

    #"
    "Anjali should be the angriest of all. She was planning her future with my brother. She bought an inn with him. They had a house they were going to raise their kids in. She lost the entire life she had thought she was going to have."

    #"
    "Yet, she's the most held together out of all of us. "

    #
    an "Yes, Craig wanted a family of our very own. Kids, a dog, a nice house..."

    #
    an "I really wanted that too."

    #
    an "But, how can I be angry at him? He was unhappy. I would never ask him to live a life that tortured him. Of course, I want more than anything to wake up next to him every morning, but that's selfish, isn't it?"

    #
    an "I've been trying to come to terms with this idea for a long time. I'm still very upset that he's not here. I cry a lot at night and in the mornings, I just push through because I have to. Because this is the life Craig wanted for us."

    #
    an "When you're not around, I listen to Silent Night over and over and over again. To me this song represents the future that Craig wanted us to have. I can't ever think of it negatively. It's a testament of the love he felt for me, the love I feel for him, and the life he was trying to live."

    #
    an "You don't have to see it my way, but I hope you understand."
    show lilah sad 
    #"
    "It occurs to me now that Silent Night meant so much to Craig because of Anjali. Maybe it was the idea of building a future with her that helped him see the light in dark times. "

    #"
    "She reaches out and grabs a hold of my hand. Hers is warm over mine. "

    #
    an "I'm still hurting inside, but Craig wouldn't have wanted me to spend the rest of my life upset. He wouldn't want me, you, or your mother to be sad all the time. All we can do now is remember him in the good times, and to make a difference in the world like he wanted to. I don't know anything else better for us to do than to live."

    #"
    "And live we shall, I suppose. I mean, I'm trying to. I'm trying so hard."
    #
    an "this won't happen overnight. So don't beat yourself up over it. It's okay to be upset, it's okay to cry. It's okay to think about crack every time you hear Silent Night. It just shows how much we love and  care about him."
    #"
    "She envelopes me into a tight hug. One, which I gladly reciprocate."
    #"
    "Life isn't easy. It never has been. But that doesn't mean that it will always be so dark. After talking to  Anjali, I know that there will be a light at the end of this dark tunnel."
    #
    an "Archer went out of his way to get us some hot chocolate. So, if you're feeling up to it why don't we head back into the tv room?"
    #
    li "Yeah, I'd like that."
  scene bg black with fade
  stop music 
 

label chapter7:
  scene bg transition with fade
  show transition_chapter7 with Dissolve(5.0) 
  
  #"======"
  scene bg lilahsroom
  show lilah neutral at left
  play music music_home

  "Rise and Shine! I'm getting used to waking up early now so the sunlight is a welcome addition to my room right now. I'm excited for a new day, and I'm actually feeling much better thanks to that medicine Archer got me. "
  #"
  "I reach for my phone and send Anjali a text before going down to the kitchen to make myself some coffee."

  #"Branches to either Friendship OR Romance endings "

  if archer_score >= archer_romanceEndScoreNeeded:
    jump ending_romance
  else:
    jump ending_friendship

label ending_friendship:
  #"Friend"
  scene bg kitchen
  show lilah neutral at left
  #"
  "It's been only a few days since the tree lighting ceremony and things have been going smoothly. Rather, semi smoothly because it's Archer we're talking about."
  #"
  "I've been thinking a lot about Archer. It's weirding me out, actually."
  #"
  "As always, I bring him his toiletries and then go on with the rest of what Anjali wants me to do. Except, now I don't see Archer as much. Usually I'll run into him serendipitously as we go about our day. He'll make some dumb remark like \"Following me again?\""
  #"
  "But, that's it...nothing more. He's been rather aloof as of late."
  #"
  "Argh, I thought we were getting along. What happened?"
  #"
  "A sinking feeling  forms in the pit of my stomach. Today I'm not going to let it get to me. Nope."
  #"
  "The pack of granola bars on my table isn't the best breakfast for the day but I'm not really in the mood to exert any extra energy. I grab a dark chocolate mocha granola bar and check myself out in the reflection of the old black toaster. Good, no bed head. It's time to go to work."
  scene bg lobby
  show lilah neutral at left
  #"
  "I hate to say goodbye to this place but in a few weeks I'll be gone. The original plan was to stay until early February, but it looks like I'll have to cut the getaway short. My mother won't explicitly state it, but I know that she's missing me like crazy. She texts me \"sleep well\" every night before I go to bed and will send me messages all throughout the day of my baby girl Marina. I miss my dog. I can't just leave her with my mother forever. "

  #"
  "Also, after talking to Anjali I realized a lot about myself. I came here to escape my memories of Craig, but that's not the right thing to do. The holidays are coming up and I usually spend them with my mother. I don't think I really want to spend any more time without her. Just because watching her cope upsets me, doesn't mean that I should just block everything out. "

  #"
  "Just like with Silent Night. I hate it, but it means a lot ot Anjali and my mother. "

  #"
  "I've found what I was looking for. Not a movie script or the purpose of life, but a better understanding of grieving and loss. It's all I could ever ask for this Christmas. I know it'll be hard to re-adjust but I have to try. "

  #"
  "So, I've decided that in a few weeks I'll go home and see what life has to offer me back in the city."
  #
  show anjali neutral
  an "You're looking nostalgic."
  #"
  "Anjali is standing behind the front desk, holding up a piece of paper."
  #
  an "From earlier. You never took it."
  #"
  "I take the piece of paper but don't unfold it. I know what it is. The idea I had about Archer that I wanted to use in my script."
  #
  li "Maybe I should tear this up."
  #
  an "Why's that?"
  #
  li "I don't need it anymore. I've decided to just focus on the Holiday season first and then see where that takes me."
  #"
  "I stick the paper in my back pocket."
  #
  li "Um...I've decided to cut my trip short."
  #
  an "Really? Why?"
  #
  li "I miss my mom. I need to be with her again. I realize there's a lot of unsaid things between us and I've been putting a lot of pressure on her for the things she uses to cope, just because they bother me."

  #
  li "When I return home for Christmas, I don't think I'll be coming back to Riversone."
  #
  an "I'm really happy that you've made such a mature decision but...you realize that Archer is staying here until the end of January, right? I need your help."
  #
  li "Let's get real here. He would probably love having someone else work with him. Besides, it's one guy. You don't need my help. He's really low maintenance."
  #
  an "It's not about how low maintenance he is. It's about how lonely the two of you are.  Archer talks a big game but I think you're growing on him."
  #
  li "Doesn't matter. All things come to an end at some point. I'm sorry, Anjali. I need to do this for me."
  #
  an "Your mother has been texting you a million times, right?"
  #
  li "Yep, she's laying it on thick. It's almost Christmas, and Craig isn't here. You know the drill."
  #
  an "I know. I understand."
  #
  li "Can't you close down the inn for Christmas and come over? Please?"
  #
  an "No, Archer is staying here for the holidays."
  #
  li "You're telling me he isn't visiting his family or something?"
  #
  an "That's none of my business, or yours. Ask him if you need to."

  #
  li "Anyway, if you want to leave I understand. It's up to you."
  #
  li "Yeah...I'm sorry. My hands are tied."
  #"
  "Anjali taps the table with her nails. The sound is drowned out by the thought of Archer alone on the holidays. Even the ice prince himself has to have someplace to be. I want to ask him about it, but I know it's a dumb idea."


  #
  li "I'm going to tell him that I'm leaving...I think I owe him that."

  #
  an "Go right ahead. You know where his room is."

  #"
  "I excuse myself from this conversation and head quietly up to his room. "

  scene bg innhallway
  show lilah neutral at left
  #"
  "I hesitate before knocking on Archer's door. There's so much that I want to say to him, but... Archer still scares the crap out of me."
  #"
  "Just a few weeks ago I was in this very position except I was giving him his toiletries. I wasn't met with the warmest of welcomes, but neither was he. Together, the two of us have had quite the explosive relations. A lot has changed, yet I feel like nothing has changed at all. I don't completely hate Archer anymore, but I wonder if he considers us friends?"
  #"
  "My knock on his door is slow and deliberate, as I calm my nerves. I'm really just saying goodbye, it shouldn't be this hard."
  #"
  "Yet goodbyes, no matter how small, are scary. The consistency have grown accustomed to is going to be shattered. I'm going to have to go back to the life that I used to know and Archer won't be there. Change is one of the most frightening things in the world, isn't it?"
  #"
  "Archer opens the door rather quickly, raising a brow at my disgruntled self."

  #
  ar "good morning, Lilah. Is there something you need?"
  #
  li "Yeah... I just wanted to know if we could talk about something. I have a lot to get off of my chest, I want to apologize about there are things that I have to tell you about other stuff too..."
  #"
  "I'm finding myself at a loss as I trip over my words."
  #
  li "I know not entitled to your time at all, but I just really have to say some things. I'm uh... I might not get a chance to say this again."
  #
  ar "Is everything alright?"
  #
  li "Uh...yeah. I'm happier than I've been in a long time. I mean maybe not in this exact moment but overall, I don't feel like I want to crawl in a hole and never come out."
  #
  ar "that's good, right?"
  #
  li "yeah, it is. I've sorted some stuff out and I made a decision that is good for me at this moment. It's one of the most mature things I've ever had to do so I'm kind of proud of myself."
  #"
  "I crack a smile."
  #
  li "So...will you talk to me? Please?"
  #"
  "Archer looks over his shoulder for a moment and then sighs."
  #
  ar "Yeah, come on in."
  #
  li "Huh? In? Like in your room?"
  #"
  "I'm startled, especially considering Archer is a really private person."
  #
  ar "Yeah, you're not going to do anything weird are you? Because if you are, then I'm going to have to ask you to leave."
  #"
  "He's clearly joking, but I answer seriously."
  #
  li "No, thanks for trusting me. I'll be on my best behavior."
  #
  ar "No sass, huh? This must be really serious then."
  #"
  "He takes a step back and motions for me to enter his room."
  scene bg archerroom
  show lilah neutral at left
  #"
  "I don't know what I'm expecting to see. Archer's room is very minimally affected by his presence at all. Everything is neatly packed away with the exception of a few chocolate bars."
  #
  ar "Take a seat. Tell me what's on your mind."
  #
  li "I was expecting something different. Like millions of fancy clothes scattered about and like really expensive high-tech stuff..."
  #
  ar "That's not really me. I am more of a laid-back kind of person. I don't want to flaunt my wealth to other people and I certainly don't allow those things to rule my life."
  #
  ar "But you still don't see that, do you? You see a rich guy with tons of fans and the power to will people to do whatever he pleases, yeah?"
  #
  li "well, you never tell me anything. You don't allow me into your inner sanctum, how my supposed to feel? Do you want me to just assume that because you say you're a regular person that you're a regular person?"
  #
  ar "There's the attitude I know. Isn't it supposed to be innocent until proven guilty? I'm not even upset that you don't see past my fame. Some people never will. That's why there is an NDA in place."
  #
  ar "Why do you think I let you into my room?"
  #
  li "Because you trust me?"
  #
  ar "Yeah, Lilah. But it's more than that. Do you know how long it's been since I've connected with someone? Like, really connected? What is this, between us? Are we friends?"
  #"
  "Friends..."
  #
  li "I thought that you didn't want to be friends. You were the one who made it very clear that we're not really friends yet. What am I supposed to think?"
  #
  ar "it's very hard for me to say exactly how I feel about things. Everything I'm expected to say is filtered. I didn't want to have to tell you something that could have hurt you in the long run. It's a defense mechanism, but I really do want to know. Do you think of me as more than just the guy you're supposed to serve?"
  #
  li "What kind of defense mechanism? Archer, I don't know what you're trying to protect me from but sometimes when you're so abrasive and mean it hurts me. If you want to be friends, just say it and we can be friends. If you want me to just be the girl who you never see again after this, then you just say that too."
  #
  ar "Woah. Who said that I never wanted to see you again?"
  #
  li "Isn't that how this works? You're the client. You stay at the hotel, I serve and then you leave. Neither of us talk about it ever again."
  #
  ar "That was what was supposed to happen... Things are not like that anymore. You... I don't know how to say this."
  #"
  "He posits for a moment to gather his thoughts before speaking again."
  #
  ar "Every time I do one of these getaways, where I block everyone and everything out, I'm successful. I blend into my surroundings and no one bothers me."
  #
  li "But I bother you."
  #
  ar "Yeah, you do. I've only been here a few weeks and I've seen you more times than I can count. You're completely frustrating. You can't even do your job properly! You wake me up at who knows what hour by making so much noise. You're constantly giving me attitude, and every time I turn around you're magically there."
  #"
  "My hand goes up to my heart. I feel like such a failure. I know Archer and I aren't the most compatible people, but this hurts worse than anything I could have ever imagined. It hurts worse than looking into the crowd of faces at Snowdrop's premier. Because, it's a reminder that I"
  "Can't do anything right. I haven't just failed him, but Anjali too."
  #
  li "I'm sorry. Way to make me feel better."
  #"
  "I want to flee. This suddenly feels like the worst place to be. My gaze falls to the solid wood panels on the floor."
  #
  ar "See, you do that thing too. That thing where you never let me finish my thought without jumping to some kind of irrational conclusion. I don't hate you. You have a lot of shortcomings, sure. But really who does it?"
  #
  ar "If you weren't the most annoying person I've ever met, I would not even be talking to you right now. Your persistence hasn't allowed me to push you away and honestly that's the greatest thing that's happened to me. You reminded me what it's like to interact with another real human being."
  #
  ar "I've been thinking about this since I saw you so absorbed into your phone on the train. You were bopping your head to my song, but there was a look of perplexion on your face. Like, you couldn't believe what you were listening to. I didn't get a good vibe from it."
  #
  ar "I felt so angry at first. I wrote you off instantly. If you can even enjoy my music, clearly you had bad taste and I just assumed that you totally sucked. Which is not true by the way, in case you're trying to skip ahead and fill in my words for me."
  #"
  "I bite my lip, holding back the smile that wants to radiate my face. Archer likes me. He really likes me."
  #
  ar "You're different. Even really care that I'm famous. Everyone I meet tries to get on my good side so that we could be best buddies or something. You're the complete opposite. I told you to keep your distance and you did. You respected my wishes, but there was a level of defiance within you. You respected my wishes but you fought back too."
  #
  ar "You're unlike anyone who has ever had to work for me. You're a freaking mess sure, but you're fun to be around. There I said it."
  #"
  "I don't know what to say or do. Do I thank him? Give him a high five, a firm handshake?"
  #
  ar "I'm feeling like, for the first time, I'm making progress with an actual person. Not some sycophant follower. But I forget that you're a person to and I'm not entitled to anything. Also, that I do a lot of pushing away myself. I'm not the easiest person to get along with."
  #
  li "Thank you, for trying to make progress. You're the way you are for a reason, because you can't trust a lot of people when you're famous."
  #
  ar "No, you can't. I snap my fingers and I get what I want, no hesitations. But you...you can't even restock my room without running your mouth. You don't just let me do whatever I please. I forgot that people like that existed. "
  #"
  "I resist the urge to stick my tongue out at him. So, it hasn't been the smoothest of times together but it's definitely been something."
  #
  ar "I don't know. I'm saying that you're a one of a kind whether that be for better or for worse..."
  #"
  "His voice trails off and he looks over at the curtains that cover the window. I don't know what to make of his words. I should be happy about them, but I'm leaving. That's surely going to shatter this whole thing. It'd be foolish to expect him to fit me into his life."
  #
  li "Archer, I appreciate everything you've just said but I came here to tell you that I'm going home. I thought it'd be easy to say goodbye since you were supposed to hate me, but I guess that's not really the case..."
  #
  ar "You're leaving? What for?"
  #
  li "I came to the inn to get away from my mother's holiday rituals. They remind me too much of my brother Craig, he committed suicide a few years ago. So, every Christmas things are tough. I wanted to run away from that."
  #
  ar "I'm sorry."
  #
  li "You don't have to give me your condolences. Life happens, I guess. But, anyway..."
  #"
  "I take in a deep breath."

  #
  li "I realized that I'm only hurting my mother and myself by running. I need to go home to be with my mother who is really lonely, though she'll never admit it."
  #
  ar "..."
  #
  ar "You have to do what you have to do. Family is important."
  #
  li "It is..."
  #"
  "Neither of us really know what to say next."
  #
  ar "So...what do you want from this, Lilah? Do you want to just leave this as our holiday friendship? A few weeks and then we both go our own ways? Or do you think we could see each other again?"
  #
  ar "I need you to be 100\% honest with me right now, no sugarcoating things for my sake or to be polite."
  #
  li "What I want doesn't matter. What you want doesn't matter either. We're just two fish who happen to be swimming next to each other because of the current. But when it stops pulling us in the same direction, we'll go our separate ways as it's supposed to be. Why waste our breath on the formalities?"
  #"
  "I don't know why I blurt all of this out. I feel like I've known Archer a long time and it's only been a few weeks. Spending every waking minute trying to please him has made me attached to his moody personality, I suppose. He doesn't feel so untouchable all the time."
  #
  ar "The ocean is a big place, and who knows...the current could make us cross paths again. If you let it."
  #
  li "you can't control the current. If I tell you that I don't want to say goodbye forever and you say the same thing that doesn't necessarily mean that our lives will take us back to each other. I know that you're incredibly busy and I'll just get lost in the crowd."
  #
  ar "But we've never tried it. You can't say something is going to happen definitely if you don't have anything to back it up. Who is to say that I won't go out of my way to see you again? To be completely honest with you, you're the only person who feels real. You are the only person that I have met in the last few months that I would actually even want to see again."
  #
  ar "Everyone always wants to know the real Archer Lane. It's always the same thing though. One day..."
  #"
  "He doesn't want to finish that thought."
  #
  ar "one day I want something more than the flashing lights and money. I don't want to be Archer Lane, the celebrity, for ever. I really just wanted to make music to share with the world. A lot of people found that exciting and I love my fans. But sometimes, even I need to slow it down."
  #
  ar "Lilah, I know skirting the issue being very vague so I'm just going to come out and say this once and only once. I would like to be friends with you. I want to try. I'm okay if you don't want to. If you think this whole thing is fake and it's too flashy then fine. I'm just telling you how I feel."
  #
  li "I want to be your friend too. I've wanted it from the beginning, even when I didn't know it. I want to believe that you're not some celebrity who cares more about the weight hair looks than about human interaction. It's just so hard to believe sometimes that someone like you would want to get to know someone like me."
  #
  li "the world has taken so much for me, that a situation like this almost seems like a practical joke. I always ask myself why. Why me? Why do you want to even bother allowing me into your life? I mean I know you said all the things that are great I am but... I guess I don't really believe them."
  #
  ar "It's lonely at the top, Lilah. That's why."
  #"
  "I don't quite know what to make of that. Though I can feel the power behind the words."
  #
  ar "I've seen the people who have tried to use me to get to this spot. I've seen the empty words and the over excitement when I walk into a room. All of that is hollow and it felt like that would be the only thing I would ever hear for a long time. I don't like being here by myself."
  #
  ar "I'm trying to escape the people who don't care about me. I'm not trying to escape social interaction. Just for a few weeks I want to pretend like I'm not this really famous guy. The real Archer Lane, likes the real Lilah Scott. That's all I can really offer you."
  #
  ar "We can give this whole friendship thing shot, can't we? With both of our tenacious natures, why can't we?"
  #"
  "He's lonely. I'm lonely. But we can be lonely together."
  #
  li "I would like that a lot, actually."
  #
  ar "so then, don't say goodbye right now. Just say until next time because if we both try really hard enough there will be a next time."

  #"
  "He looks at me seriously and holds a hand out to me."
  #"
  "I grab hold of it. I don't know where life is going to take either of us. I don't know if he's going to go off on another massive world tour or if I'm going to keep making my movies, but what I do know is in this moment a bond has been formed. A bond, that if the two of us try hard enough, can be something life-changing. But even if life throws something our way, I will have known that in these few weeks in Riversone, I have learned more than I had ever anticipated and that in itself has made me a better person."

  jump lbl_END

label ending_romance:
  #"Romance"

  #"
  "It's been only a few days since the tree lighting ceremony and things have been going smoothly. Rather, semi smoothly because it's Archer we're talking about."
  #"
  "I've been thinking a lot about Archer. When he comforted me, it felt like we had known each other for a long time. The two of us, in that moment, felt unstoppable. "
  #"
  #"
  "A sinking feeling  forms in the pit of my stomach. Things are going so great and Archer is finally opening up to me. I don't want to ruin that but I have to tell him that I'm leaving. "
  #"
  "The pack of granola bars on my table isn't the best breakfast for the day but I'm not really in the mood to exert any extra energy. I grab a dark chocolate mocha granola bar and check myself out in the reflection of the old black toaster."
  "Good, no bed head. It's time to go to work."
  scene bg lobby with fade
  show lilah neutral at left
  #"
  "I hate to say goodbye to this place but in a few days  I'll be gone. The original plan was to stay until early February, but it looks like I'll have to cut the getaway short."
  "My mother won't explicitly state it, but I know that she's missing me like crazy. She texts me \"sleep well\" every night before I go to bed and will send me messages all throughout the day of my baby girl Marina."
  "I miss my dog. I can't just leave her with my mother forever. "

  #"
  "Also, after talking to Archer I realized a lot about myself. I came here to escape my memories of Craig, but that's not the right thing to do. The holidays are coming up and I usually spend them with my mother."
  "I don't think I really want to spend any more time without her. Just because watching her cope upsets me doesn't mean that I should just block everything out. "

  #"
  "I've found what I was looking for. Not a movie script or the purpose of life, but a better understanding of grieving and loss. It's all I could ever ask for this Christmas. I know it'll be hard to re-adjust but I have to try. "

  #"
  "So, I've decided that in a few days I'll go home and see what life has to offer me back in the city."
  #
  show anjali neutral with dissolve
  an "You're looking nostalgic."
  #"
  "Anjali is standing behind the front desk, holding up a piece of paper."
  #
  an "From earlier. You never took it."
  #"
  "I take the piece of paper but don't unfold it. I know what it is. The idea I had about Archer that I wanted to use in my script."
  #
  li "Maybe I should tear this up."
  #
  an "Why's that?"
  #
  li "I don't need it anymore. I've decided to just focus on the Holiday season first and then see where that takes me."
  #"
  "I stick the paper in my back pocket."
  show lilah sad at left 
  #
  li "Um...I've decided to cut my trip short."
  #
  an "Really? Why?"
  #
  li "I miss my mom. I need to be with her again. I realize there's a lot of unsaid things between us and I've been putting a lot of pressure on her for the things she uses to cope, just because they bother me."

  #
  li "When I return home for Christmas, I don't think I'll be coming back to Riversone."
  #
  an "I'm really happy that you've made such a mature decision but...you realize that Archer is staying here until the end of January, right? I need your help."
  show lilah neutral
  #
  li "Let's get real here. He would probably love having someone else work with him. Besides, it's one guy. You don't need my help. He's really low maintenance."
  #
  an "It's not about how low maintenance he is. It's about how lonely the two of you are.  Archer talks a big game but I think you're growing on him. The two of you could really help each other."
  #
  li "Doesn't matter. All things come to an end at some point. I'm sorry, Anjali. I need to do this for me."
  #
  an "Your mother has been texting you a million times, right?"
  #
  li "Yep, she's laying it on thick. It's almost Christmas, and Craig isn't here. You know the drill."
  #
  an "I know. I understand."
  #
  li "Can't you close down the Inn for Christmas and come over? Please?"
  show anjali sad
  #
  an "No, Archer is staying here for the Holidays."
  #
  li "You're telling me he isn't visiting his family or something?"
  show anjali neutral
  #
  an "That's none of my business, or yours. Ask him if you need to."

  #
  an "Anyway, if you want to leave I understand. It's up to you."
  #
  li "Yeah...I'm sorry. My hands are tied."
  #"
  "Anjali taps the table with her nails. The sound is drowned out by the thought of Archer alone on the Holidays. Even the ice prince himself has to have someplace to be."


  #
  li "I'm going to tell him that I'm leaving...I think I owe him that. But, maybe not right now."

  #
  an "Are you afraid?"
  show lilah sad 

  #
  li "I don't want to say goodbye to him. I don't want this trip to end. It feels like a dream."

  #
  an "Then don't say goodbye. That means forever, right? Just say until next time. You'll see him again."

  #
  li "You can't be so sure of that."
  
  #
  an "No, but I have a good feeling."
  hide anjali with dissolve

  scene bg black with fade
  scene bg brown1
  show lilah neutral at left
  #"
  "I try to get through the rest of the day without thinking about Archer. It's proving to be a bit difficult. Every time he walka into the lobby I look the other way so that he doesn't want to approach me. I just can't face him knowing that I have to say goodbye for now."
  #"
  "It sucks because I know that the two of us are finally getting on the same page. I can't help but think what this means for us in the long run. Anjali seems to think that Archer is going to stop his famous lifestyle and make time for me, but this is the real world."
  "That stuff doesn't really happen."
  #"
  "It's already pretty late when Archer returns from whatever adventure he is on for the day."
  
  show archer sad
  #
  ar "Lilah, hey. Is everything all right?"
  #"
  "I look up from the computer screen I'm pretending to be focused on."
  show lilah sadblush
  #
  li "Oh, uh...yeah. Thanks to you I'm feeling much better. My sickness is gone."
  #
  ar "That's good. But you know what I mean. Are things gonna be awkward now that I know about your brother?"
  #
  li "Yeah... I mean, things are going to be awkward but not because of my brother."
  
  #"
  "There's no use lying to him."
  #
  ar "I did something to upset you?"
  show lilah neutral
  #
  li "Oh, you did nothing wrong at all. You've been nothing but a good friend to me."
  #"
  "I feel confident in that assertion."
  #
  li "It's just that I have some news that I need to tell you and I've been avoiding you because I am kind of afraid of what you're going to say or do."
  li "And I guess I'm afraid of what the outcome is going to be. Uhm, I don't really feel like making up some convoluted excuse."
  
  show archer neutral
  ar "I know that we are only just starting to become closer but I want you to know that you don't have to be afraid of telling me something."
  "I want to make it clear that that NDA and me keeping you at a distance was to protect you. But, I trust you now. Everything I said to you the other day is completely true."
  #
  li "I appreciate that. I just get in my head sometimes."
  #
  ar "Do you want to come take a walk with me? I the just went to the town square and saw the tree up close. The TV did not do it justice."

  #
  li "Sorry about that, again."
  #
  ar "Are you kidding? I asked around it turns out that the tree lighting ceremony had no hot chocolate so clearly we had the better set up."
  #
  li "you and your chocolate..."
  #
  ar "Don't pretend like you don't absolutely love it. Anyway, come with me. Let's go see the tree. You can tell me whatever it is you have to tell me there."
  #"
  "I do quite like the idea of having this conversation away from the Inn. It might not feel so suffocating knowing that we're in the open under beautiful Christmas lights. I decide to take him up on his offer, because why not?"
  scene bg treetown
  show lilah neutralout at left
  show archer winterneutral
  #"
  "The Christmas tree looks absolutely stunning. Archer is right, the tree lighting on television did this beauty no favors. It looks so much more incredible in person, especially with the night sky signing down and illuminating the colorful bulbs on the branches."
  #
  li "Wow...this is nothing like Rockefeller Plaza."
  #
  ar "Something about it is even more enchanting though, isn't it? But, I haven't been to New York during this season in a while so..."
  #"
  "His voice trails off."
  show archer wintersad
  #
  ar "Can we skip the pleasantries? I really want to know what's bugging you. You're not the kind of person who doesn't vocalize something that upsets her."
  #
  li "Yeah, there's really no use in us wasting any more time. Uhm... After the conversation about my brother the other day I decided that the best thing that I could possibly do right now is to just abandon everything and go home."
  li "I know I had an obligation to continue working with you but I need to go see my mother. I don't want her to be alone and the holidays and I just realized that I pushed her away because I couldn't face my own emotions."
  #
  li "I haven't completely confronted my own emotions but I don't think that being out here is really going to help me. I need to do some healing with my mother and together we'll see where life takes us from here on out."
  "Don't get me wrong, I really don't want to leave. I just know that I can't leave my mother alone right now. Christmas is coming up and I've not spent one without her."
  show lilah sadout
  #
  li "I guess I'm also upset because Anjali just told me that you're going to be spending the holidays alone. I know that you don't really care for people that much, but it's Christmas. You should not be alone."
  
  show archer winterneutral
  ar "I understand that you have to leave. Family always comes first. I'm actually really happy that you found something that you feel compelled to do. Bettering yourself comes in all different forms."
  #
  ar "As for me spending the holidays alone, don't worry about me. I actually do this quite often."
  #
  li "No, I'm going to worry. Now that we are officially friends, I can't in good faith let you stay here alone. You can come with me to New York if you want. My mom won't mind but... You'll probably stick out like a sore thumb. Someone would definitely notice you."
  #
  ar "Really, I don't mind. Go and spend time with your mom. I'd don't want to interfere in that anyhow because this is something that the two of you are really going to need to strengthen your bond. I will be fine I promise."
  #"
  "For the first time ever Archer and I are having a real conversation that doesn't feel forced. Neither of us are arguing or yelling at each other and it feels really really awesome."
  #
  ar "you are scared about telling me you have to go home? You don't owe me any explanation, Lilah. That's your life."
  show lilah sadblushout
  #
  li "No, it's not that I'm scared about. I'm scared about losing you. I can't believe I just said that out loud..."
  
  show archer wintersmile
  #
  ar "Well, I'm glad you said it. I kinda feel the same way. I know I haven't been nicest to you these past few weeks. I have a tendency to push people away so that neither of us get hurt"
  ar "I have been lied to most of my life by people who want to get to know me in order to benefit somehow. You have been a breath of fresh air. I was just really really afraid that one day this was going to stop and I'd have to go back to being alone."
  show lilah neutralout
  #
  li "You said was."
  show archer winterneutral
  #
  ar "Yeah, was. I'm not really afraid anymore. You're being 100\% honest with me right now and that's something that I've never had before in my entire life. You gain absolutely nothing monetary by telling me about your brother or telling me about how you're really feeling. Yet, you do."
  #
  li "I do because I'm your friend. I mean in the beginning I did see you as Archer Lane, that's not something you can really blame me for the because come on dude... You know how famous you are. But, now you're just Archer."
  #
  li "I know we're not best friends right now, but I really do want to get to know you more. My biggest fear is that I leave and you move on with your life. We both say right now that we're going to keep contact and we're going to do all these great things but then life rears its ugly head and we lose touch."
  li "I don't want that because this has been the hardest I've had to work for friendship. There's so much more I want to know about you. I don't really want you to slip through my fingers."
  
  show archer winterhappy
  #"
  "Archer begins to laugh lightly."
  #
  li "What?"
  #
  ar "You said that Anjali thinks we're very similar. Well, I'm starting to think that she's right too. I'm feeling the exact same way. I have this problem where can't tell you that I like you, even though I do."
  ar "This is going to be the only time you hear me say it but essentially you are one-of-a-kind. You are the most annoying person I've ever met, but I really wouldn't mind being annoyed by you for the rest of my life."
  
  show lilah blushout 
  #
  li "The rest of your life!? That's a really long time. It's a huge commitment."
  show archer winterneutral
  #
  ar "I know, let's take this one step at a time. You opened up to me the other day about yourself. I still want to see that movie one day, but when you're ready to show me. In the meantime, I want to let you in on more of my life. In the future I want to show you the real Archer. If you'll allow me."
  show lilah happyout
  #
  li "Yeah, I would really like that more than anything. Thank you for trusting me enough with your friendship. I'm going to try really hard not to disappoint you."

  #
  ar "All you really have to do is be yourself. That's it. I don't want anything else but the strange girl I met at the Red Turtleneck Inn."
  #"
  "He extends his hand out and I grab hold of it. It is really a small gesture, but it means the entire world to me. Archer is opening himself up to the possibility of us getting to know each other more personally. He isn't pushing me away. I can't help but feel excited for what's to come."
  hide archer with dissolve
  scene bg fields with fade
  show lilah neutralout at left
  play music music_thinkingofyou
  #"
  "This is it. Today is the day I'm going to be going back home to New York City. Archer and I have said our goodbyes already and Anjali gave me a huge monologue about how much she loves me and she's going to miss me."
  #"
  "I assured both of them that this is not goodbye forever. After talking with Archer I feel very confident that the two of us can at least try to make this friendship work."
  "He is a very genuine person and doesn't say anything that he doesn't mean. I value that immensely, because if he thought that I wasn't worth being friends with, he wouldn't sugarcoat it. He would just tell me straight out that we would never see each other again."
  show lilah sadout 
  #"
  "Still... My heart kind of feels empty. I don't want to be leaving Riversone. The beautiful backdrop is still as picturesque as ever and I'm afraid that once I leave it will disappear forever."
  
  show archer wintersmile
  #
  ar "Hey! I'm so glad you didn't leave yet."
  
  show lilah neutralout
  #
  li "Huh? Archer? Oh, I was just looking at this view one last time."
  show archer winterneutral
  #
  ar "Don't make it seem like it's forever. This is your sister-in-law's Inn. You can visit anytime you want."
  #
  li "Hey, listen. If I want to be dramatic on my last day, I'm going to be dramatic. Can't you just play long for like three seconds?"
  #
  ar "No, because I don't want you to get on that train feeling like this is the ending of everything. I'm hoping it's just the beginning."
  #
  li "Beginning of what?"
  #
  ar "Us. You and me."
  
  #
  li "Me and you?"
  #
  ar "Yes, that's what I said. You and me."
  #
  li "Our friendship, yeah?"
  show archer winterblush
  #
  ar "I was thinking a little more than that, actually. Like maybe, we could go on a date the next time I see you?"
  show lilah blushout
  #
  li "...."
  #
  li "Did you just say DATE?"
  #"
  "I can't believe my ears."
  #
  li "I didn't hear you right, did I?"
  
  #
  ar "Yes, Lilah. You did. Stop with the dramatics...I'm asking you out."
  #
  li "I'm just confused. How'd we jump from friend to lovers?"
  #
  ar "I feel a connection when I'm with you. I did a lot of thinking after we left town square the other night and I realized that I don't want to be your friend. There is chemistry between the two of us, whether you want to admit it or not."
  ar "If you are just my friend I would be upset about you leaving, sure. But I would get over it."
  #
  ar "Right now, the thought of you getting on the train back to New York City is literally tearing me up inside. I have never cared enough about a person that I would go out of my way like this for them. "
  "You are special to me, and I know we're not going to be this amazing power couple overnight. I guess I'm just asking for you to keep an open mind."

  #
  li "I mean, I suppose I could think about it..."
  #"
  "I like Archer too. I realized it the moment he hugged me when he was comforting me about my brother. It felt really nice to be in his arms."
  #"
  "Seeing Archer like this is actually really funny. You would think he'd be a total ladies man..."
  #
  li "All right, if you kiss me right now and there are sparks like in all those ridiculous Christmas movies I watch, then when we meet up again it will be for a date and not a hang out session."
  #
  ar "That's it? Of course."
  #
  li "how are you so sure there's going to be sparks?"
  show archer wintersmile
  #
  ar "Because, I'm Archer Lane."
  
  show lilah madout
  #
  li "No, no no! You don't get to use that line on me. I'm a De Luca fan."
  #
  ar "For now... But after I kiss you, you're not going to be saying that."
  #
  li "Prove it then, big shot."

  #
  ar "I will."
  

  scene cg kiss
  
  #"
  "Without warning Archer pulls me in for a very surprising, yet wonderful kiss. I melt into his arms immediately, not wanting this moment to ever end."
  
  #"
  "When we pull away, a smirk dances on his lips."
  #
  ar "You felt those sparks, didn't you?"
  #"
  "I look away with a glare."
  #
  li "Maybe..."
  #
  ar "You owe me a date AND a screening of your movie so...you better pay off your debt soon or I'm going to start charging interest."
  #
  li "I'm pretty sure this violates your NDA agreement..."
  #
  ar "Eh, I won't sue you this time."
  #"
  "I hug Archer tightly, placing my head on his chest."
  #
  li "Well now I really don't want to go."
  #"
  "He strokes my hair."
  #
  ar "Go, be with your mom and I will talk to you in January? New year, new us?"
  #
  li "Yeah, that sounds really nice..."
  #"
  "I groan suddenly."

  #
  ar "What now?"
  #
  li "This was like some corny Christmas movie....!"
  #
  ar "Hey...stop complaining for like 5 seconds. Christmas movies don't get sequels usually and I don't plan on never seeing you again so..."
  #"
  "I can hear Anjali giggling in the background and I know this is what happiness feels like. I didn't make a new movie script, I didn't block out the memory of my brother, I didn't totally push Archer away, but I wasn't really meant to do any of that."
  "I met a wonderful person, I got to see my amazing sister-in-law again and the two of them showed me what life is all about. It isn't living in the past, but always looking to the future because no matter what happens, it will always be bright with the right people by your side."





  jump lbl_END
label lbl_END:
  #"END OF Game"
  return
