
# The game starts here.

label splashscreen:

  $ renpy.movie_cutscene("legendexgames.ogv")
  return

label start:

label prologue:
  stop music 
  scene bg transition with fade
   
  show transition_prologue with Dissolve(5.0) 
  
  scene bg NYC
  pause(1.0)
  play music music_silentnight
  #scene bg NYC
  #"
  "Tonight is a silent night as I sit in front of my childhood home for the last time."
  "After I return from my trip, the place will have nothing but a Christmas tree and a set table."
  #"
  "Tomorrow morning, I will be saying goodbye to a childhood friend who has watched my family and I grow within its walls."
  "I will be leaving for my sister-in-law's bed and breakfast upstate, while my mother packs all of our good memories into boxes. At least, the ones that fit. "

  #"
  "The house I grew up in isn't really a house, but no one ever asks about the two bedroom walk up I grew up in. "

  #"
  "House is a strange word. I don't really like the way it tastes on my tongue. It feels so much more extravagant than what I live in. Why don't people ever ask about my home?"

  #"
  "A house has enough bedrooms for every person living in the place. It has a comfy living space, a backyard, and a front porch."

  #"
  "What it doesn't have is a bedroom so small that the mattress acts as a couch, desk, and bed all at once. A house doesn't have four flights of stairs between its occupants and a musty smelling lobby."

  #"
  "But most importantly, a house doesn't have the memory of a deceased loved one lingering in all of the things scattered around the cramped space."
  "Not in the always tidy hamper, or the uncluttered top shelf of the wall unit. Not even in the almost empty refrigerator."


  #"
  "My two bedroom walk up certainly isn't a house, but it is a home. A home filled with painful memories that I can no longer stomach. That's why I'm leaving. "


  #"
  "Not for good, that would kill my beautiful mother's taped together smile."
  "But, I'll leave until all of the holiday cheer in the streets of New York City is gone. Until I no longer have to watch my mother wrap a gift and label it \"To Craig, from Santa.\""


  #"
  "We all know that he is going to miss the third Christmas in a row but it will still feel like the very first time we celebrated his favorite holiday without him. "

  #"
  "I'll have to look into my mother's hollow eyes as she tears open the finely wrapped paper and exclaim that Craig would appreciate the gift. "


  #"
  "It's always the same thing too, the sterling silver guardian angel pin that she had given him almost five Christmases ago."
  "The one she and I had spent hours arguing with the postal service on the phone for after they lost the package on route. "


  #"
  "This Christmas, my mother will not have to spend the happiest time of year with three spots at the table unclaimed. She has my word."
  "Until that time comes, I need to leave the overtly \"in your face\" holiday cheer that New York City is famous for. "

  #"
  "Not because I don't appreciate a large Christmas tree in every well known area or ice skating rinks filled with people chattering excitedly."
  "It's because I just don't know how the city is able to keep moving when, to me and my mother, it feels as if it the world has stopped spinning. "

  #"
  "My hand glides over the aluminum mailbox. The same aluminum mailbox that my mother and I would wait anxiously by."
  "Our best memories were when we would finally receive a letter from Craig after months. We'd both smile and count our blessings. "

  #"
  "Tonight, there is a different sentiment as I look at the mailbox. Tonight I feel melancholic. But alas, all good things must come to an end eventually."
  "Goodbye, old friend. "
  stop music

#label prologue:
#  scene bg black with fade
#  show transition_prologue with Dissolve(5.0) 
label chapterOne:
  #"Common:"
  #"Show Image for 2 seconds: chapter1
  scene bg transition with fade
  show transition_chapter1 with Dissolve(5.0) 
  #scene bg black with fade
  #scene P with Dissolve(5.0)
  #scene train1
  #"Show Image for .5 seconds: prologue.jpg #(so that it removes on it's own with no click necessary)
  #"Join Scene: LNeutral.png Bottom Left, near the textbox "
  show lilah neutral at left
  scene bg train_one

  show lilah neutral at left with dissolve
  #Insert: TrainLine1a.ogg"
  ta "Please have your tickets ready for boarding. This train leaves to Riversone, making local stops along the way."

  #"
  play sound sound_train fadein 2.0
  #play sound sound_doorclose
  "I'm already seated on the train. If living in New York City has taught me anything, it's that behind a crowded train is usually an empty one."
  show lilah happy at left
  "Score one for me!"
  
  show lilah neutral at left 
  #"
  "I place my bulky duffel bag on the seat next to me. It's a little tactic I like to call \"uncomfortable silence.\" Most people will see my bag and glare at it silently, but they won't tell me to move it. "


  #"
  "You can't get away with it for the whole ride, but for a few stops it's totally possible. So until some old woman demands I move my stuff, I'm sitting here pretty comfortably. "

  stop sound fadeout 1.0
  play music music_archersong
  show lilah mad at left
  #"
  "Archer Lane's new hit single blasts through the online radio app on my phone. The pop punk take on an old Christmas song is innovative sure, but there's nothing incredibly moving about Archer's song."
  "I don't feel particularly drawn to the beat, the overlayed vocals, or all the extra processing. Christmas songs are most meaningful when they're sung honestly."
  "Besides, why remake this old song? Of all the songs in the world, he chose to remake an old folk song based on a poem he probably knows nothing about!" 


  #"
  "Not really feeling the whole, \"make Christmas cool\" thing Archer's got going on."
  "Nope, no thanks. Not today, buddy. "

  stop music 
  #"
  "I quickly turn off the app and find my saved music folder."
  
  "Ah, yes. Thomas De Luca's music always calms me. I'll play one of his songs."

  play music music_peaceofmind
  show lilah happy at left
  #"
  "Thomas De Luca is my go to artist. His music is gorgeous. The composition, the vocals- all of it!"
  "He doesn't hide behind autotune like Archer Lane does. Thomas De Luca doesn't need to. His talent is unmatched."
  "I read an interview about why Thomas De Luca chose to sing \"O Come O Come Emanuel\" on his Christmas Album instead of a more mainstream song. His answer was simple. He thought this song embodied the spirit of Christmas."
  "His mother used to take him caroling on Christmas Eve and this was one of her favorite songs. You can tell just how much it means to him by listening to the amount of feeling he puts into every word he sings."
  "I can feel his soulful voice in the pit of my stomach with each word he sings and it's amazing. It's almost as if I'm in another world. I shut my eyes and let his vocals take me to a different place. "

  scene bg black
  hide lilah with dissolve
  #"
  "Right now, I'm not on a train to my sister-in-law's inn to work for the winter. I'm on stage and Thomas De Luca is singing to me. He's holding my hand and letting me know that everything will be okay. "

  
  #"
  "Even if I know that nothing is okay."
  "Well for one, I can't even stand to look my mother in the eye as she pours an extra cup of hot cocoa in the morning, or sets the table for three people instead of two."
  "How sad is that? I am running away from my own mother!"

  #"
  "On top of that, I have no money. I'm a 22 year old college graduate with a degree in film and a surmounting pile of debt."
  "All I have to show for my education is one movie and it isn't even that good. I still have no permanent job offers. "

  #"
  "Thomas De Luca's voice can't magically toss money in my lap or bring the smile back to my mother's face. But, he does help me tune out the world for a few minutes so I can pretend like my problems don't exist. "

  #"Screen jolts #(moves right, then back into place quickly)
  scene bg train_one with hpunch#"
  show lilah neutral at left with dissolve
  #"
  "When I open my eyes it's because I can feel that the train has stopped moving. I leave my bag next to me, but I drape an arm over it protectively. "

  #"
  "A person boards the train and walks casually to the other end of the car. My bag's seat is still secured. "


  #"
  "I notice that the scenery around me has changed as the train pulls away farther and farther from the big city. There are so many trees and the sunlight isn't hidden by tall buildings."

  #"
  "Riversone might not be so bad after all. Especially if it looks as peaceful as the scene through the train window."

  #"
  "Riversone is the perfect middle point for travelers heading up north to the textile driven cities or south to the more rural areas. Or so the internet has told me."

  #"
  "I'm sure I'll meet a lot of interesting people there. Or hey, maybe none at all, which I'm totally cool with too. "

  stop music
  play sound sound_train

  #"
  "I switch the music off for a second when I notice we're approaching a new station. This one looks much more packed."
  "I give a forlorn look to my bag, which I know I'll have to move onto my lap. It's fine, just a mild inconvenience."

  #Insert: TrainLine2a.ogg"
  ta "We are now approaching Wistfield station."

  #Play SE: TrainPullingIn.ogg"

  #"
  "The train slows down once again and pulls into a station like the ones before it. I wonder how far we are from Riversone. "
  stop sound fadeout 1.0
  #"
  "Despite having an aisle seat, I can't see much of what's in front of me as people pile into the now crowded train. "


  #"
  "I lean back into my seat and remove my hand from my bag."
  "Play it cool, Lilah. "

  #"
  "My solace has already been lost as I notice the sunlight from the window is being blocked by the people standing in front of my seated figure."
  "I never really realized how much darkness can damper one's mood."

  show archer wintermad  with dissolve  #Center screen." 
  #"
  "I look up to see a man towering above me. He looks annoyed and motions to the seat next to me with his head."
  "Without a single word, I slide the duffel bag into my lap. I'm not trying to cause any trouble."

  #"
  "I expect the man to sit down, but he doesn't."
  
  hide archer with dissolve
  
  #"
  "Instead, he steps back and holds his arm out for an older woman with a cane to slide into the seat next to me."
  

  ow "Kids these days...you ought to be more respectful!"

  show lilah blush at left
  #"
  "She glares at me, but it's nothing that hasn't happened to me on a train before. Kindly I begin to explain that I hadn't seen her, otherwise I would have moved my stuff. "


  #"
  "While I like the seat next to me being empty, I'm not heartless. I'd even stand up for someone if they looked like they needed a seat. "


  #"
  "This isn't a commuter train in the city. The social cues are much different."
  "I only begin to realize that when I lock eyes with the man from earlier. It isn't quite a glare that sits upon his face, but he's definitely judging me. "


  li "Ma'am, I swear I didn't see you."

  ow "The train is crowded, that big bag should go in the overhead above!"

  
  li "When I got onto the train, it was empty. I was just..."

  #"
  "But she continuously cuts me off to tell me I need to learn some respect. Well, sometimes you lose the \"uncomfortable silence\" game..."
  
  show lilah sad at left
  #"
  "I stand up and offer the seat to the man, since this woman looks like she'd much rather sit next to the \"well mannered gentleman\" who helped her get a seat. "

  #"
  "He opens his mouth to protest, but I've already got the hulking duffel bag over my shoulder."
  "I push passed the crowd of people, muttering \"sorry\" before settling into a spot by the door and away from the old woman."
  
  
  hide archer with dissolve
  show lilah neutral at left
  play sound sound_train fadein 2.0
  #"
  "Still, for some reason I feel the need to keep stealing glances at the guy. I've always been infatuated with the idea of people moving around in everyday settings."
  "It's like a photographer friend of mine always said, \"people living their lives is the most fascinating thing\". "

  #"
  "The best way to come up with a character is to just look at the people around you. Trains are the best place to do that, especially in New York. "

  #"
  "I try to figure out who the person might be by what they're wearing or how their posture is. It's a little quirk of mine that helped me through tons of screenwriting classes in college. "


  #"
  "This particular man is strange. As he nestles himself into his corner seat, I take a long look at him. The man looks out of place, and it's no doubt because of the scarf that is pulled all the way up passed his nose. "

  #"
  "He definitely gives off the vibe that he's trying to hide himself. Whether it be him trying to mask his identity or a deeper self esteem issue, I don't know. I'm not a psychologist, just a people watcher."

  #"
  "The man's blond locks peek out from his oversized wool hat. His eyes are closed and the woman next to him is staring at him in awe. How the heck does she gravitate towards the shadiest looking guy in the train car?" 

  #"
  "Ughh...how many more stops until I reach my destination?"

  stop sound fadeout 1.0
  play music music_archersong
  #"
  "I turn on my radio app once again and it brings me back to where I left off in Archer Lane's song. I just leave it on, hoping the beat is enough to cheer me up again. "


  scene bg black with fade
  scene bg train_one with fade
  stop music fadeout (1.0) 
  #"Insert:TrainLine3a.ogg"
  ta "We are now arriving in Riversone. Please exit the train as this is our last stop."

  #"
  "I step out of the train as soon as it stops and the door opens. I have no interest in being trampled on by the twenty or so people trying to exit as well."

  scene bg black with fade

  scene bg trainmorning
  show lilah neutral at left with dissolve
  #"
  "The cold air greets me. Now, I have to call my sister in law. She said that she would be at the station waiting for me, but it's hard to pinpoint anything here."
  "Despite the train letting out a big crowd, there aren't many people mulling around the massive station. "

  
  #"Play Voice: A01.ogg"
  que "Can you move?"
  #Stop SE:"

  #
  "Huh?"
  
  #"
  show archer wintermad  with dissolve #Center screen"
  "I whip around to see the man from earlier."
  
  "I step aside and he quickly brushes passed me with not even a second glance in my direction."
  hide archer with dissolve 
  show lilah mad at left
  "Rude!"

  show anjali smile
  an "Lilah! Hey, you're here! How was the train ride?"

  show lilah blush at left
  #"
  "Startled, I jump slightly. She probably saw all of that, but she's too polite to bring it up."
  "Classic Anjali. "

  show lilah happy at left

  #"
  "I regain my composure and smile brightly at her. She looks as gorgeous as ever."
  "To someone who doesn't know her, I'm sure her brilliant smile masks the bags under her eyes. She's worn down and tired, but she's too proud to admit it."


  an "Well? You never answered my question. How was your train ride?"

     
  menu:
    "Answer Politely":
      show lilah neutral at left
      li "It was nice. The scenery especially was beautiful. So all in all, I'd say it was a relaxing ride."

      #"
      "I'm careful not to mention the old lady who sat next to me or the weird guy who caused the whole commotion earlier. I don't want to worry Anjali with something so trivial. Especially not during this time of the year."

      an "That's great. You're just going to love it in Riversone. I'm so happy to have you here."

      li "I hope so."
      $ anjali_score +=5
      jump chapterOne_common
    
    "Tell the Truth":
      play sound sound_success
      show lilah sad at left
      li "It sucked. There was this old lady and a guy with a big scarf who tag teamed me! The guy basically made me move my bag for this old lady, which is totally fine. But she was yelling at me for not doing it myself."

      show anjali neutral
      an "And why didn't you do it yourself?"

      li "Honestly? I didn't see the lady!"

      an "It's not because of the bag trick your brother taught you, huh?"

      li "I know when to use the bag trick, Anjali! Only when there's not a ton of people and I planned to move it whenever someone asked me to. Until then, how am I supposed to know someone wants to sit there?"

      an "Lilah..."

      li "I swear, I was going to move it! You're looking at me like that guy was. He didn't believe me either."


      an "I believe you, Lilah. I'm only teasing. There are unspoken rules on the trains in NYC, but not here in Riversone. Everything is much more laid back. Don't be as hasty."


      #"
      "You know what they say. You can take the girl out of New York City, but you can't take New York City out of the girl. "

      li "It's not that easy, but I'll try not to be an obnoxious city girl."
      $ archer_score +=5
      jump chapterOne_common
    
label chapterOne_common:

  show anjali neutral
  show lilah neutral at left

  an "Try to see the bright side for once, will you?"

  show lilah happy at left
  li "Yes ma'am!"
  show lilah neutral at left
  show anjali mad

  #"
  "Anjali isn't happy with my feigned obedience."

  show anjali neutral
  an "You know, I actually missed your sass. Believe it or not."

  show lilah sad at left

  #"
  "I frown. It must really be lonely out here for her. I don't know why she chooses to run this hotel in the middle of nowhere by herself. There isn't anything exciting about the area that I know of. "

  

  an "That was supposed to be a compliment."


  li "It's not you. I'm just thinking of something."


  an "I'm okay. Really."

  #"
  "She sees right through me, not surprisingly. Anjali is really good at reading people. She reaches out to me and puts a comforting hand on my back. "

  an "Business is doing better and my sister is thinking about moving out here. So don't pity an old soul."                                                           

  show lilah mad at left

  li "Old? Hardly! You're 32!"  

  show anjali smile
  an "In mountain time that's almost 50."

  #"
  "I scoff."

  li "Your math is off and I don't even think it works like that."

  an "Hey now, don't argue with me."

  show lilah neutral at left

  #"
  "Anjali insists on taking my suitcase from me. She tells me that her car is nearby and begins to talk happily about what my living arrangements will be for the next few weeks. "

  #"
  "It's hard to concentrate on her words when I see the man who caused so much trouble for me on the train earlier. He looks disgruntled, impatiently typing on his phone. Anjali follows my gaze. "

  show anjali neutral
  an "What are you looking at?"

  #""Lilah"
  li "Uhm... everything. Riversone is so different from the big city."   


  an "We have a lot of character here, that's for sure."


  #"
  "I get a better look at the man's outfit as we pass him by.  He's wearing a red plaid shirt under a large jacket. His eyes are hidden under his blonde hair."
  "Yep, he looks just as out of place as I feel. But the few people roaming around pay him no mind. I guess it doesn't really matter. " 


  li "What were you saying before?"


  #"
  "I change the conversation back to Anjali. As she leads me to her car, Anjali begins to talk about how many people have worked at the hotel during the winter."
  "Not including me this year, two others have worked there prior. Not really a big employment pool. "

  scene bg black with fade

  scene bg car
  hide anjali   
  hide lilah

  #"
  "Anjali's car is nothing extravagant, but considering I took a train to get here I'm in no position to judge. Anjali speeds down the empty road with zero reservations. "


  #"
  "She isn't irresponsible, rather, a woman who knows her small town well. I admire her comfort in her own world, something I can't ever seem to achieve."

  #"
  "I look out into the town, seeing Christmas trees in front of almost every single building we pass. It is picturesque."
  "Riversone resembles a postcard, and it makes me wonder if anything has changed at all. I wouldn't be surprised if the Christmas aesthetic was part of Riversone's all year round traditions. "

  #"
  "Anjali switches on the radio with her right hand as her left steers through the bumpy road. I admire her control. Not only of the car, but of herself and probably her hotel too. "

  play music music_archersong

  #"
  "Archer Lane's song plays through the speakers again and I shut my eyes. It's one of his better songs but it's still missing something. Rather, it has too much going on. I wonder what the song would sound like without so much production.  "


  an "This is that guy right? Arrow something?"


  
  #"
  "I let out a laugh. "


  li "Archer Lane, Anjali. But close."


  #"
  "Anjali laughs. "


  an "I told you, I'm an old lady. I've seen things that would prove it."


  #"
  "I don't doubt that she has. She must have, but that's another reason I admire her. "


  #"
  "Anjali and I drive like this for ten more minutes, chatting and laughing. It really is good to see her again in person and not just behind a video chat."


  #"
  "The last time wasn't the happiest of memories, and my heart still aches thinking about her tearful eyes at my older brother's funeral. For the first time ever, I had seen the composed woman crack."
  stop music fadeout (1.0) 
  scene bg treetops with fade
  show lilah neutral at left
  #"
  "Anjali pulls into the parking lot of The Red Turtleneck Inn. I haven't ever seen it in person, but the pictures I've seen online don't do this place justice. The Inn is breathtakingly beautiful."
  "This is the place my brother had always wanted to open with the woman of his dreams. \"The Red Turtleneck is finally a reality,\" he had once exclaimed happily, slamming the lease papers on the kitchen table of the old two bedroom walkup. "


  show anjali sad #Center screen: anjali sad


  #"
  "Anjali tugs at the hem of her shirt. This is the first time I've seen her uncomfortable. Usually, she's a paragon of hope, always looking at the brighter side of things. I feel the need to break the silence that weighs heavily upon us."   


  li "Craig never told me why you guys decided on the name Red Turtleneck all those years ago."

  #"
  "The naming of the Inn is always a thought that passes through my mind. Craig was always so tight lipped about his plans with this place once he acquired it."

  show anjali smile
  #"
  "Anjali gives me a smile, but it isn't as big as the ones we shared in the car. "

  an "The red turtleneck was what I was wearing when Craig and I first met. He was sentimental, that one."

  show lilah sad at left

  #"
  "I can feel my heart tearing apart. My brother truly loved Anjali. She was his heart, his soul, and his better half. I start to realize that the Inn might not be the best place to escape the painful memories of Craig's death. Anjali, despite her normally cool personality, is hurting too. "            

  show anjali neutral

  an "Anyway, why don't we unlock the place?"

  show lilah neutral at left

  #"
  "As she fishes in her purse for the keys, I take in the view. Looking at the property in its entirety, I'd say this place is pretty charming."
  "The Red Turtleneck Inn looks like a cottage, with an eye catching red roof. It resembles a house in size, and I wonder how many rooms are in it. "

  #"
  "Behind the Inn there are two buildings. One of them must be Anjali's home. Or maybe it's a cabin she rents out to guests. "


  #"
  "The mountainous backdrop is like a painting. The lush green mountains stretch up towards the clouds. Tall trees line the base of the mountains trying to reach the summits, but they fall a couple hundred feet short. "

  #"
  "What's most glaring though are the Christmas decorations on the building. There are lights adorning the top of the roof and a plastic snowman by the Inn's sign. "

  #"
  "Anjali has the Christmas spirit despite Craig's death. I hope that, unlike my mother, Anjali isn't living a lie. I hope that she's honoring Craig's memory by celebrating his favorite season, and not just going through the motions of monotony to pretend that everything is okay."

  #"
  "Clearly, she isn't okay. Even if she's putting on a brave front, I can tell that her heart still lurches at the mention of my brother. I suppose this is what an attempt at moving on looks like. "

  show lilah sad at left
  #"
  "A hand flies up to my heart. I have so many conflicting emotions. Love for Anjali and her strength, anger at myself for not being able to move on, and of course sadness for all that is lost."

  #"
  "But dwelling is part of the problem. I promised my mother, myself, and Craig that I wouldn't live in the past. So, I won't dwell on it."
  "I turn back to Anjali. She has to unlock the place. Which means..."

  show lilah neutral at left
  li "Unlock? It hasn't been open this whole time?"


  show anjali neutral
  #"
  "Anjali shakes her head and her black locks fall against her face. "


  an "Normally we would be, but someone booked the whole place."

  show lilah blush at left
  li "What? The entire thing? Who can afford that?"

  show lilah neutral at left
  an "I don't ask questions. My clients are entitled to their privacy. The person prepaid when they booked online and gave me the name Irving Prince. He'll be coming in a little later today, so we'll meet him then."


  li "What about me? Where do I stay?"


  an "We have two cabins in the back. You can stay in the one on the left. It's pretty nice. Plus, you'll only have one guest to deal with."


  li "I hope that means less work."


  #"
  "Anjali just shrugs. She slides the key into the lock and leads us inside of the inn."

  hide anjali
  scene bg ChristmasTreeInn
  stop music


  #"
  "The interior of the place is just as beautiful and serene as the outside. While the outside boasts vintage light fixtures and Adirondack style lawn chairs, the inside has a much different feel. It reminds me of a bed and breakfast, with warm colored wallpaper and quaint furniture. "

  #"
  "There's a large Christmas tree by the front door, which I can't help but gravitate towards as Anjali settles into the Inn."

  scene bg ChristmasTreeInn
  play music music_silentnight
  show lilah sad blush at left
  #"
  "The tree is decorated with colorful lights and plenty of ornaments, but one sticks out to me. I gasp involuntarily as a hand flies to my mouth. "

  #"
  "Anjali is in the midst of sliding off her coat when she hears me. "
  
  show anjali neutral at center with dissolve
  an "What is it?"

  show lilah neutral at left
  li "This ornament..."

  #"
  "I point to the one I'm looking at. It is a group of penguins riding on a sled and each one has a name on it's scarf. Anjali, Craig, Lilah, Marsha. Our family's names, even mom's."

  li "You put out the ornament I gave you all those years ago?"
  show anjali smile

  an "Of course. I've put it out every year since you've given it to me. It's the real star of the tree, topper aside."

  #"
  "Anjali hangs her coat up on a nearby coat rack and walks over to me. She places a comforting hand on my shoulder. "

  an "Are you okay?"
  show lilah sad at left
  li "Yeah. It's just that it's so different from home. Mom is going through the motions of putting out our ornaments, but the sparkle behind her eyes is gone. Your eyes still sparkle when you talk about the sentimental things."
  show anjali sad
  an "Your mother has lost a child. That isn't something anyone but a parent could comprehend. You have to give her time."

  li "Will time ever be enough?"

  an "Maybe. Maybe not. But your mom is strong. She can get through anything, I know it."

  stop music fadeout 2.0#(it fades out)
 
  #"
  "She's right, but it's hard waiting for things to go back to normal. I miss the mother I knew five years ago."
  "Anjali places a kiss on the top of my head before sliding behind the front desk."

  scene bg brown1 with fade
  play music music_home
  show anjali smile #Center screen"

  show lilah neutral at left
  an "Ms. Scott, reservation for 1?"

  #"
  "I roll my eyes. Anjali is trying to make me smile and I applaud her effort."
  "I feign shock. "

  li "I made no such thing."

  show anjali neutral
  #"
  "Anjali rolls her eyes in return but begins starting up the computer. "


  an "Today I'm going to let you explore because you just got here. But tomorrow I want you up bright and early for work."


  #"
  "Bright and early? Ugh. I'm not built for that."


  an "If you see our prolific guest, don't scare them away. I quite like the idea of having only one guest to deal with. Speaking of...that means you'll be the only one on shift."



  li "That's alright. If I'm being honest with you, I think I want the quiet."


  show anjali smile
  #"
  "Anjali is typing furiously on the computer. She flashes me a smile before speaking. "

  an "Why not check out the place while we wait for Irving Prince? Put your stuff away and get comfortable."

  #"
  "It's not a bad idea. I should drop my stuff off in my cabin and settle in. I take the keys that Anjali offers me."

  show anjali neutral
  an "The smaller cabin on the left is yours. Dial 648 on the phone to reach the front desk and 949 to reach my cabin. I'll be here doing a quick maintenance check before our guest arrives."


  li "What about wifi? I need to be connected to the internet."

  show anjali neutral

  an "The signal is weak back there, so you'll have to be in the lobby to connect. But, I doubt you'll be worrying so much when you realize what there is to do around here in the winter."

  show lilah sad at left
  #Lilah:"
  li "But what about at night when I want to stream a movie?"

  #Anjali:"
  an "We have a dvd player. Make use of that, or stream from the lobby."

  #"
  "I groan but Anjali shoos me off so she can finish her work."

  hide anjali
  
  scene bg kitchen with fade
  show lilah neutral at left
  #"
  "The walk to my cabin is short. Inside, it's beautiful. The cabin has a very rustic charm. There is only one floor, but it has everything I'll need including a bedroom, bathroom, living area and kitchen."

  #"
  "I lean my suitcase against the counter in the kitchen and sit at one of the high barstools. This is the perfect place to sit with my coffee and write film scripts. That is, if inspiration strikes again. "

  #"
  "I spent years on my first film, Snowdrop. Yet, no one seemed to even bat an eyelash when it was released. I just wonder if making a new film will have the same result. Maybe being in the mountains a bit will benefit me. Who knows? I could use the creative juices."

  #"
  "I have the day off, at least for a few hours. While I'd love to explore, I need to jot some things down before I forget. My mind wanders to the stranger from the train. "

  #"
  "What's his story? Er...world class super spy who was following the old woman around? She must have been a world class information broker for a secret organization! Well, probably not.  But it'd be fun to write about. "

  #"
  "I pull my notebook out from my bookbag and scrawl \"Identity\" across the top of the first available blank page. A movie about one's self. How we see ourselves versus how others see us. And it all starts with a guy on the train. "

  #"
  "No! Even better. I'll tell his story through the perspective of the girl who watches the events unfold. It'll be a good juxtaposition of the two seemingly different narratives. "

  #"Background Fade to black for .5 second and then changes back to kitchen.png
  scene bg black with fade
  pause(0.5)
  scene bg kitchen with fade

  #"
  "I scribble all of my ideas down before slamming my notebook shut. I should explore Riversone before it gets dark. It wouldn't hurt to know my way around. If I remember my research of the small town correctly, everything closes early. "

  #"
  "I hop off of the tall barstool and head out to tell Anjali of my plans. "

  scene bg brown1 with fade
  show anjali neutral #Center
  show lilah neutral at left
  #"
  "Anjali is still fumbling with the computer when I make my way into the lobby of the Red Turtleneck Inn."
  show anjali smile
  "She looks up with a small smile and waves me over. "

  an "So how do you like your accommodations?"

  li "They're amazing. Honestly, a breath of fresh air. There's something about looking outside of your window and seeing a vast forest that is so calming. Thanks again for letting me stay."

  an "Anything for you. Besides like I said, I could use the help. Now, what are your plans?"

  li "I was hoping to check out the town before it gets dark. Do you have any suggestions of where I should check out?"

  an "Well, it depends. Are you hungry?"

  show lilah smile at left
  #"
  "I grin sheepishly. Is she kidding me? Of course I am."

  li "Always."

  an "There's a small cafe and gelato shop to the west of here. East is a souvenir shop and a grocery store."

    
  menu:
    "Where should I go?"
    
    "Grocery Store":
      play sound sound_success  
      "Grocery Store! That way I can stock my fridge. It won’t hurt to be prepared. I say a quick goodbye to Anjali before leaving the lobby."
      $ archer_score += 5
      jump chapterOne_grocery
    
    "Gelato/Cafe":
      $ fc_score +=5
      jump chapterOne_cafe

label chapterOne_grocery:

  hide anjali with dissolve
  stop music fadeout 1.0
  play music music_sunbathing fadein 1.0
  scene bg street_ordinary with fade    
  show lilah neutral out at left

  #"
  "Luckily, I'm able to find my way around Riversone relatively easily. I take my time walking around, letting the cold brisk air caress my cheeks."

  #"
  "The scenery of Riversone is truly breathtaking. The tall trees are lush and green, the buildings are composed of a dulled red brick and the storefronts are all decorated with snowmen, reindeer, penguins and the like. "

  #"
  "Riversone is a winter town just like in one of those cheesy romantic Christmas movies."

  scene bg grocery with fade 
  stop music fadeout 1.0
  play music music_passingtime fadein 1.0
  show lilah neutral at left
  #"
  "Leighton's Milk and Grocery Store is stocked to the top with local delicacies. Their selection of homemade pies is impressive, but what I'm here for is something much more savory. Maybe fresh cold cuts and chips? Or, how about a roast beef? I'm sure the oven in my cabin works well. "

  #"
  "I turn down into the meat aisle, only to stop in surprise. The man from the train is standing there. "

  show archer winterneutral with dissolve #Center screen"

  #"
  "He's fiddling with his scarf in one hand while the other holds up a pack of organic chicken. I instinctively take a step back and turn on my heels to run. But then I realize that I need some food in this aisle if I want to eat."

  #"
  "Ok Lilah. Play it cool. You can do this. Cool as a cucumber."

  #"
  "I pick up a package of chopped meat and flip it over to read the nutritional facts. Really, I'm looking at the man from the corner of my eye."
  "His stature, lazily hunched over a package of cured beef, tells me that he's young. That and the expensive name brand headphones that are peaking out of his winter hat. "

  #"
  "For a moment we meet eyes. He looks up at me, dropping the package into his shopping cart casually. I look away quickly."
  "Does he recognize me?"

  show lilah sad blush out at left
  #"
  "I expect him to look away too, but he doesn't. I feel his steady gaze on my back. It's a little unsettling. That must be how he feels with me staring at him."

  #"
  "Fine. Point taken."
  "I drop the packaged chopped meat back into the fridge where I got it from and head into the next aisle."

  #"
  "I almost forget why I'm here to begin with. I'm hungry! But I would rather get something else to eat than deal with this guy staring at me, even if I was staring at him first."
  "My bad."

  hide archer with dissolve
  show lilah neutral out at left
  #"
  "I'm in the cereal aisle. Whatever. That'll do."
  "I grab the fruitiest thing I can off the shelf and try to find the milk. I purposely traverse the aisles slowly so I can steal glances at the stranger to assure he doesn't approach me."

  #"
  "He doesn't. Thank goodness. I don't think I can deal with another old lady yelling at me today."

  stop music fadeout (1.0)
  jump chapterTwo
    
label chapterOne_cafe:
  "Gelato sounds delicious right about now. I turn to tell Anjali a quick goodbye. "
  show anjali neutral
  show lilah neutral at left

  an "Lilah! Wait! On your way back can you pick up some white bread for me? I can't have jam and toast in the morning without it."

  #"
  "She hands me some money."

  an "For the gelato too."

  li "I can't take this. I have money."


  an "I can't spoil my sister? Nonsense."
  show lilah smile at left
  #"
  "Anjali refers to me as a sister rather than her sister-in-law. That means a lot to me. "

  li "Thank you."
  show anjali smile
  an "Have fun!"

  #"
  "I thank Anjali one more time before leaving the lobby. "

  hide anjali with dissolve

  stop music fadeout 1.0
  play music music_sunbathing fadein 1.0
  scene bg street_ordinary with fade
  show lilah neutral out at left
  #"
  "The streets are quiet, and there is barely anyone traversing them. I follow Anjali's directions and arrive at Lady Lacy's Sweet Shoppe."
  
  scene bg cafe with fade
  stop music
  show lilah neutral at left
  play music music_gentlepiano fadein 1.0 
  
  
  #"
  "This place is small but I can imagine myself spending a lot of time here.I wait on line patiently, taking in the sights of the town through the window."
  "This is nothing like New York City, where tons of people fill the seats of every coffeehouse with their laptops and expensive drinks."
  "The older woman behind the cash register smiles at me and asks what I'd like to have. A gelato sounds good."
  
  #"
  "I wait a few moments for the sugary goodness and grab a seat when the cashier hands the chocolate gelato to me."
  "No one is here right now but I know that when there are a few more people mulling about, I want to be sitting in a booth and watching them."
  "Anjali is right. This gelato is amazing, unlike anything I've ever had before. I contemplate getting anaother one, but I remember that I have to go and pick up some bread for Anjali."
  "I stand up and smile at the cashier before ducking out of the ice cream shop."

  scene bg grocery with fade
  stop music fadeout 1.0
  play music music_passingtime fadein 1.0
  show lilah neutral at left
  
  #"
  "Leighton's Milk and Grocery store is stocked to the top with local delicacies. Their selection of homemade pies is impressive, but what I'm here for is something much more savory. "

  #"
  "Maybe fresh cold cuts and chips? Or, how about a roast beef? I'm sure the oven in my cabin works well. Oh, and I need to pick up some bread for Anjali. "

  #"
  "I turn down into the bread aisle, only to stop in surprise. The man from earlier is there. "

  show archer winterneutral with dissolve #Center screen"

  #"
  "He's fiddling with his scarf in one hand and the other holds up a loaf of wheat bread. I instinctively take a step back and turn on my heels when I realize that being in this aisle is unavoidable."

  #"
  "Anjali wants bread. Ok, fine. I can do this."


  #"
  "I pick up a loaf of white bread and flip it over to read its contents. But really, I'm looking at the man from the corner of my eye."
  "His stature, lazily hunched over a package of plain bagels, tells me that he's young. That and the expensive name brand headphones that are peaking out of his winter hat. "

  #"
  "For a moment we meet eyes. He looks up at me, dropping the package into his shopping cart with purpose. I look away quickly. Does he recognize me?"

  show lilah sad blush out at left
  #"
  "I expect him to look away too, but he doesn't. I feel his steady gaze on my back. It's a little unsettling. That must be how he feels with me staring at him."
  #"
  "Fine. Point taken."
  "I drop the white bread into my shopping cart and head into the next aisle. All but forgetting why I'm here in the first place. I'm hungry!"

  hide archer with dissolve
  show lilah neutral out at left
  #"
  "I'm in the cereal aisle. Whatever. That'll do. I grab the fruitiest thing I can off the shelf and try to find the milk. I purposely traverse the aisles slowly so I can steal glances at the stranger to assure that he doesn't approach me. "

  #"
  "He doesn't. Thank goodness. I don't think I can deal with another old lady yelling at me today."
  stop music fadeout (1.0)
  jump chapterTwo

label chapterTwo:
  #"Common:"
  #"Show Image for 2 seconds: chapter1
  
  scene bg transition with fade
  show transition_chapter2 with Dissolve(5.0) 
  scene bg street_ordinary
  play music music_sunbathing fadein 1.0
  #"
  "I open the box of cereal and eat it as I'm walking. The cell service isn't the best here, and I'm struggling to maintain an internet connection long enough to check my social media. "

  #"
  "It's no use. "

  #"
  "The walk back to the Inn is uneventful. But, Riversone seems like a pretty uneventful place in itself. It's why I chose to come here. "

  stop music fadeout 1.0
  scene bg brown1 with fade
  show lilah happy out at left
  play music music_home
  li "I'm back!"

  #"
  "I chime in happily as I take off my earmuffs and scarf. Even though there's no snow on the ground, it's still pretty cold out."


  show anjali neutral with dissolve #Center screen"

  #"
  "Anjali looks frazzled. She sighs when she notices me. "


  #show ArcherNeutralScarf.png. Anjali moves to the left. "
  show anjali neutral behind lilah:
    xalign 0.3
    yalign 1.0
  show archer scarfnormal with dissolve:
    xalign 0.8
    yalign 1.0

  #"
  "Standing in front of her is the man from both the train and the grocery store, but this time the stranger has managed to take off his hat and has pulled the scarf down from covering his mouth. "
  show lilah blush at left
  #"
  "Involuntarily, I gasp. I know this man. Not from the train, or from the grocery store. I know him from somewhere else entirely."

  show lilah blush at left

  #"
  "Archer Lane. "

  #"
  "At least, his doppleganger. I rub my eyes to get a better look at him. I'm finding it hard to believe the man I've been avoiding looks exactly like pop sensation, Archer Lane. I mean, why haven't I noticed this until now?"

  #"
  "Anjali stretches an arm out to me to grab my attention. I realize that my eyes are trained on the disgruntled man for a little too long, and seeing Anjali snap her fingers jolts me out of my thoughts. "

  #"
  "She carries on the conversation as if I hadn't just been gawking at the celebrity look-alike. I bite my lip and look away from both of them. "
  stop music fadeout 1.0
  an "Good. You're here."

  show anjali smile
  #"
  "Anjali turns to the man with her warming smile adorned proudly on her face. "


  an "This is Lilah. She'll be the only one in and out of your room to clean it and-"

  show anjali neutral
  #"
  "The man cuts her off mid sentence. "

  show lilah neutral at left
  show archer scarfmad with dissolve:
    xalign 0.8
    yalign 1.0
  #Play SE: A02.ogg"
  que "I don't need any cleaning done. I'll leave my dirty bed sheets and towels in the hallway. I can take care of everything else."
  #Stop SE:"


  an "And toiletries? Will you need someone to restock your room?"


  show archer scarfmad 
  #"
  "The man looks annoyed at Anjali's perfectly reasonable question."
  show lilah mad at left
  "Rude." 
  "There is no way that this guy can be the celebrity that people gush over. But his look is definitely convincing."

  #"
  "Anjali looks unperturbed, a seasoned veteran at dealing with insulting behavior. If not for her, I'd be telling that guy to watch his tone. No need to be so snippy about everything when Anjali is being perfectly hospitable"
  
  show archer scarfnormal
  #Play SE: A03.ogg"
  que "Lilah, was it? She can bring those to me when she supplies me with clean sheets. Also, access to your kitchen facilities will be helpful."
  #Stop SE:"

  show lilah mad at left
  #"
  "This is a lot to take in and kind of strange frankly. If the man notices me from earlier, he doesn't mention it."
  "Am I supposed to? Is that socially acceptable? What now? "

  an "I assume this is all in your paperwork, Mr. Lane? A nondisclosure agreement and your rules for staying here that we must comply with?"

  #"
  "Irving Prince is actually Archer Lane? I pull on my ear lobe. Did I just hear Anjali right?"
  show lilah blush at left
  li "Mr.Lane? You mean he isn't just some look alike?"

  #"
  "Of course he isn't. A look alike wouldn't carry himself with so much authority. It baffles me how I didn't notice this sooner. The mystery man who caused a scene on the train for me is a celebrity. A rude one, at that. "

  #"
  "The man lets out an aggravated sigh. "

  #Play SE: A04.ogg"
  ar "Yes, I'm Archer Lane. Stop gawking. My nondisclosure agreement is in the paperwork packet I handed to your boss. It details my conditions for staying here, the gist being not to enter my room without permission, not taking any pictures or videos of me, and not leaking my whereabouts or personal information to the public. I will not stay otherwise."
  #Stop SE:"


  an "I've signed it. Lilah, you'll need to sign it as well."
  show lilah neutral at left

  #"
  "Anjali hands me the packet in question. My hands are shaking as I flip through the documents and I don't know why. "

  #"
  "The rules are what I'd imagine are standard for a nondisclosure agreement, but also for a decent human being. For example, things like not going into Archer's room without permission or not taking something from him. "

  #"
  "I know I shouldn't be, but I'm offended that Archer assumes I'm like that. Even if it is standard procedure, I respect people's privacy. I'm a decent human being." 

  li "Uhm..."

  #"
  "I struggle to find the words to say right now. "

  an "Lilah? Are you hesitant to sign the agreement?"

  li "I'm sorry, it's just very hard to believe all of this. I mean, just a few hours ago Archer was on the train with me and he had drawn everyone's attention to me as if I was some bad guy."

  show archer scarfneutral 
  #Play SE: A05.ogg"
  ar "Were you not ogling me in the grocery store?"
  #Stop SE:"

  #"
  "He poses the question as if to say, \"we're even,\" but clearly those are two different scales. Besides, ogling isn't the word I would use!"

  show lilah blush at left
  li "T-hat was different! I was just trying to buy some lunch. You were in the aisle where my food was..."

  #"
  "Anjali puts her hand up, saving me from my embarrassing rambling. "


  an "Mr.Lane has a right to his privacy. We won't go against his wishes. Correct?"

  show lilah sad at left
  #"
  "I shrink back, not wanting to disappoint her. "

  li "I guess..."


  an "Mr. Lane, I assure you that Lilah won't be a problem. She'll aid you to the best of her abilities. You just need to ask."
  #Play SE: A06.ogg"
  ar "I don't need a teenage girl in control of my stay."
  #Stop SE:"

  show lilah mad at left
  li "I'm not a teenager. I'm twenty two. Dude, I've got a college degree."

  #"
  "Because, Archer seems like the kind of guy that needs my qualifications to assert that I can do a decent job."

  #Play SE: A07.ogg"
  show archer scarfhappy 
  #"
  "Archer begins to laugh and then swipes at his eyes as if drying tears. "
  #Stop SE:"

  li "Hey! What's so funny about that?"

  #Play SE: A08.ogg"
  ar "You were listening to my album on the train."
  #Stop SE:"

  show lilah blush at left
  #"
  "I can feel my face heat up. Did he see me listening to his song? I wasn't even near him! "

  li "He-y! How did you know that?"

  #"
  "Archer smirks but doesn't answer me. He definitely saw me on his way out of the train. That has to be it..."

  #"
  "Anjali steps in front of us, her arms crossed over her chest. She looks more concerned than angry."

  an "How many times have you two run into each other exactly?"

  show lilah neutral at left
  li "Twice. He was that guy on the train I was telling you about earlier. Except, I didn't know he was Archer Lane because there was a scarf covering his face."

  show archer scarfneutral 
  #Play SE: A09.ogg"
  ar "That's the point. I'm in hiding. I want a few weeks to myself without any paparazzi bugging me. If that's going to be a problem, I'll check in somewhere else."
  #Stop SE:"
  show anjali mad
  an "Will it be, Lilah?"
  
  #"
  "Her stare is fierce and I look down at my boots. "

  show lilah sad blush at left

  li "No, I'll be good."
  show anjali neutral
  #"
  "Archer waves the paper in the air. So much for some respect. "

  #Play SE: A10.ogg"
  ar "I'll basically be invisible. You don't have to worry about me. But, I need written proof of your intentions."
  #Stop SE:"

  show lilah neutral at left
  li "How do I know that I'm not signing my life away?"
  

  #"
  "This whole thing is surreal. Archer Lane is standing right in front of me, but it doesn't feel like I'm looking at a mega star. He just seems like a regular smug dude, minus the non-disclosure agreement he's waving in my face."

  #Play SE: A11.ogg"
  ar "You're not if you follow some simple rules."
  #Stop SE:"

  li "I'm giving you my word. Is that not enough?"

  #"
  "He cuts me off abruptly, as he seems to have a habit of doing. "

  #Play SE: A12.ogg"
  ar "It's not."
  #Stop SE:"

  show lilah mad at left
  #"
  "He looks at Anjali who softens her gaze. "

  an "I apologize, Mr. Lane. I promise that Lilah and I both have your best interest in mind as our guest. Please bring your stuff upstairs. Anyone who doesn't sign your agreement will not have access to you or your room."

  #Play SE: A13.ogg"
  ar "Thank you. That's all I ask."
  #Stop SE:"

  #"
  "I swear I see a glare shot in my direction. Whatever Archer, I'm not a fan of yours either. "

  hide archer with dissolve
  show anjali sad:
      
      linear 0.5 xpos 0.45
  #"
  "Archer grabs his bags and begins carrying them up the stairs with little fuss. "

  


  stop music fadeout 1.0
  play music music_home
   
  #"
  "When she's sure he's out of view, Anjali looks at me with a frown."
  show lilah smile at left
  "I grin sheepishly at her, but she's having none of it. Anjali lets out a huff. "

  an "Don't give Archer a hard time."

  show lilah neutral at left
  li "I'm really not trying to. I'm sorry if it came across that way."

  show anjali neutral
  an "I understand that this may be a shock to you. Honestly, I'm shocked too. Archer Lane is staying at my Inn! I've never had a prolific guest here before."

  
  #"
  "She steps closer to me and pushes my bangs out of my face gently."
  show lilah happy at left
  "I smile weakly at her."

  an "I also know that it's a tough time of year with Craig gone. But, Archer doesn't know that. So don't take out your frustrations out on him in the future if you feel upset."

  show lilah sad at left
  #"
  "I keep forgetting that the world doesn't stop spinning even if it feels like my world has ceased motion sometimes."

  li "So you're saying to sign his agreement, then. It wasn't my intention not to. I just...I don't know."

  an "Honey, I get it. But you have to give Archer a chance. You didn't say it, but I saw by the look on your face that he might not be the ideal guest you were hoping for. This is business, we ignore our feelings of dread."

  li "It's just that I'm confused, overwhelmed, and a little bit disappointed with the idea of having to work with someone who is so arrogant. But that's on me I guess, not him."


  an "He's protecting himself and what he's built. I don't blame him. But the fact of the matter is, Archer is our guest. He will not stay without that agreement being signed. All we have to do is make sure his stay is pleasant."  

  #"
  "I groan. She's right. It's way too late now for Anjali to get any more customers if we let Archer walk out. Something tells me that even though Riversone is gorgeous, it isn't bustling with people looking for a place to stay."
  "I'll sign that agreement. "


  li "He's going to be so annoying to deal with, Anjali..."
 
  show anjali smile
  an "That's my girl. If you just keep being the person that I know you are, you won't have a problem dealing with Archer. I know you mean well. "

  show lilah neutral at left
  li "I didn't yell at him. I should get points for that."

  
  #"
  "She lets out a small laugh. "

  an "This is that game where the points don't matter, Lilah."

  #"
  "She winks and hands me the thick packet of paper."


  #"
  "I pick up a pen from the front desk and sign my name as neatly as I can. I don't want Archer Lane to think I have bad penmanship."
  "I slide the document back to Anjali when it has my name scrawled across it in thin blue ink. "

  show anjali neutral
  an "Thank you. Now, why don't you bring this agreement up to Mr.Lane? He's staying in the first room by the top of the steps."

  #"
  "I don't know if I want to. Archer seemed to be annoyed by my presence and if I bring him the document I'll have to face him again. But if I don't bring him the agreement, what will that show about who I am as a person? "

  #"
  "I don't know what I should do. "
  
  menu:
    "Yes":
      $flag_BringAgreement = True
      $ archer_score +=5
      jump chapter2_Agreement_Yes
    "No":
      jump chapter2_Agreement_No

label chapter2_Agreement_Yes:
  li "Fine, but only because I love you."

  #"
  "It's also because I know this is something I owe Archer. A peace offering, if I may. "


  an "Thank you, dear. When you come down, we can hang out and catch up on things. I want to hear all about this movie premiere your mom told me about."


  #"
  "I drag my feet to the stairs. "


  li "Trust me, it's not that exciting."


  an "I'm sure it is. Your mother seemed very proud of you when she told me about it over the phone."


  li "As moms do, Anjali."

  #"
  "I give Anjali a slight nod to let her know that we'll continue this conversation if I've survived my time in the dragon's den. "

  hide anjali
  scene bg brown2 with fade
  show lilah neutral at left

  #"
  "I take a minute to admire the decor of the inn. Anjali has done a nice job making it feel homey."

  #"
  "I'm surprised Archer hasn't complained about his room being right next to the staircase. Easy access to his belongings or something like that. I roll my eyes just thinking about it. "

  #"
  "All of a sudden I'm nervous. I know I need to be a big girl, but anxiety creeps in. "

  stop music
  play sound sound_opendoor
  
  show lilah blush at left
  #"
  "The door opens and I jump back, startled."
  
  show archer neutral with dissolve
  
  #"
  "Archer looks unimpressed as he leans lazily against the door frame. "

  #"Show Image/Gif: heart.gif #(see reference pic I sent for placement) for 2-3 seconds 
  show animation_heart:
    xalign 0.52
    yalign 0.05
  show animation_heart:
    linear 2 alpha 0.0
  #(should be off of the screen before the sound finishes)
  play sound sound_success

  show lilah blush at left
  #Play SE: A14.ogg"
  ar "Don't look at me like that. I heard you walking up the stairs."
  #Stop SE:"

  #"
  "Ah, so that's why he wanted a room near the staircase. "

  #Play SE: A15.ogg"
  ar "What is it you want? I told you my terms. Until you sign that document, we have nothing to discuss."
  #Stop SE:"

  show lilah sad blush at left

  #"
  "I hold the packet out to him. "

  li "Here it is, your highness. I'm at your service, or whatever."

  show archer smile
  #"
  "Archer has a satisfied smirk on his face. Ugh, I want to punch him so bad but Anjali might demote me from sister status if I do. "

  #Play SE: A16.ogg"
  ar "You read it carefully?"
  #Stop SE:"

  #"
  "I thumbed through it. Does that count? Eh, Archer doesn't need to know that. I think he made himself pretty clear with what he expects from me. "

  show lilah neutral at left
  li "Yeah. I won't even look at you after this conversation. You leave your dirty sheets or whatever in the hall and I'll bring the replacement toiletries to your room. Should we have a drop off service? I just leave them in the hall and knock 3 times?"

  #"
  "He rolls his eyes."

  show archer neutral
  #Play SE: A17.ogg"
  ar "Smart ass."
  #Stop SE:"

  #"
  "Archer flips through the packet to make sure I actually gave my signature. His lack of trust is disheartening, but I guess that's the kind of precautions that celebrities have to take."

  li "Wow. You're being rude again, shocking. Is there anything else I can do for you? Bring you a bell?"

  #Play SE: A18.ogg"
  ar "Actually, yeah. You can help me. I need the wifi."
  #Stop SE:"

  show lilah happy at left

  #"
  "I have some bad news..."


  li "There is barely any service out here, buddy. If you want wifi you'll need to hang out in the lobby."

  #Play SE: A19.ogg"
  ar "Are you done? I have to unpack."
  #Stop SE:"
  show lilah neutral at left
  #"
  "Rude."
  "Fine. I don't want to be up here anyway."

  show lilah neutral at left

  li "Of course I am, Lane."

  #Play SE: A20.ogg"
  ar "Didn't your boss ever teach you to be courteous to your guests? It's Mr.Lane or Sir, to you."
  #Stop SE:"

  li "Right. Oh and Anjali is my sister-in-law."

  #"
  "I don't know why I added that extra information in, as Archer doesn't seem to care one bit. "

  #Play SE: A21.ogg"
  ar "That poor woman. She seems like such a nice lady too."
  #Stop SE:"

  play sound sound_doorclose
  hide archer with dissolve
  #"
  "Archer doesn't say anything more as he closes the door in my face. "

  

  li "Thanks for the vote of confidence!"

  #"
  "I shout at the door and hear a grunt in return."


  #"
  "I can do this. It's just a few weeks."

  scene bg librarynight

  show anjali neutral #Center screen"
  play music music_home fadein 1.0
  show lilah neutral at left
  #"
  "Downstairs Anjali is sitting in one of the living chairs near the fireplace. There's a bookshelf behind her packed so tightly that I wonder how hard it will be to dislodge one of the books."

  li "You read any of these?"

  an "I've read a few every here and there. It's relaxing to have a good book in your hand. How'd it go upstairs?"

  li "Fantastic. We are really getting along. You know, I might have been wrong about this Archer guy. He seems great!"

  an "That bad, huh? I thought he'd appreciate you bringing the packet to him as a truce. Guess people like him are set in their ways. I wouldn't dwell on it. So, tell me about this movie you made. I'm dying to know."
  $ archer_score += 5
  jump chapter2_postAgreement

label chapter2_Agreement_No:
  li "You can do it."

  show anjali sad

  #"
  "Anjali frowns. "

  an "Lilah."

  show lilah sad at left

  li "I'm just not in the mood today."

  show anjali neutral

  an "Welcome to adulthood. Sometimes we have to swallow our pride. I can call him down if that makes you feel better."

  li "It doesn't."

  an "I'm not going to force you to do anything you don't want to. I can hand it to him in the morning when he comes down for breakfast."

  #"
  "She places the contract in a drawer behind the front desk and then saunters over to the seating area of the lobby. "

  scene bg black with fade

  scene bg librarynight with fade
  show lilah neutral at left
  #"
  "She motions for me to follow before taking a seat in a comfortable looking chair."

  show anjali neutral with dissolve
  an "I'm dying to know about this movie premier your mother told me about over the phone. I could feel her pride. It must have been really exciting."
  jump chapter2_postAgreement
    
label chapter2_postAgreement:
  "I sit down in the chair opposite her. It makes me feel ten times worse knowing how excited Anjali is to see me succeed. Looking at Archer, a man who is so popular that he has to have nondisclosure agreements drawn up, reminds me that I'm a nobody. "
  show lilah sad 
  li "It premiered to a total of 11 people, and the majority of them were friends or family members."

  show anjali happy
  an "That's a huge accomplishment! It was at an independent filmmakers festival, correct? Who can say they've done that?"

  li "All 23 other independent filmmakers. I'm telling you, it wasn't a big deal at all. My movie isn't even that good."

  show anjali neutral
  an "I'll be the judge of that. What's it about?"

  #"
  "I'm hesitant to answer, but Anjali has never meant ill will towards me."
  show lilah neutral at left

  li "Well...it's called Snowdrop. It's about this girl who feels trapped where she is. All she wants to do in life is make a difference in the world but she doesn't know how."
  li "Her resources are limited and the people around her don't seem to care about her dreams. Because of this, she is at her lowest point until she meets someone who inspires her and picks her up off the ground."

  show anjali smile

  an "It sounds like an intriguing plot. Reminds me an awful lot of someone I know. A recent college graduate who doesn't think her parents understand her career in the fine arts."

  #"
  "I feel her gaze on me deep within my soul. Now, I'm a bit embarrassed."
  show lilah sadblush at left
  li "I didn't know how else to channel my frustrations. I think after watching it, mom finally understands how passionate I am about making films."

  #"
  "I have always fought with my mother on pursuing film in college. She doesn't understand why I would take out student loans to study something that will probably make me little to no money."

  #"
  " Anjali and Craig have always supported my dreams, but they weren't the people I was living with and had to face everyday. My mother means well, she just wants to make sure that I'll have enough money to support myself. "

  #"
  "I'm starting to see her fears become a reality. My first movie didn't make nearly as many waves as I thought it would. To me, it feels like I'm proving her right. On top of everything else in my life, I'm stressing out. "


  an "Your mother is proud of you, that's for sure. I could hear the exuberance in her voice. You are her everything, Lilah."

  show lilah sad at left
  stop music fadeout 1.0
  #"
  "Because Craig is gone."

  #"
  "I want to say it but my better judgement kicks in. I know uttering these words will hurt Anjali, so I keep them to myself. But when Anjali leans in closer to me, I know I don't have to say a word. She's aware of what I'm thinking."

  #"
  "The tension in the room is thick. I can't deny that things have changed because of my brother's passing. People treat me differently, my mother especially. "

  show anjali sad
  an "You can't tell me that your mother didn't hold you on a pedestal when Craig was alive. Even if your mother is clinging to you so that she doesn't lose you, it doesn't invalidate her love for you. I'm telling you Lilah, she adores you. She is proud of who you've become. It has nothing to do with your brother."

  play sound sound_footsteps
  show anjali neutral
  show lilah neutral at left
  #"
  "We hear footsteps and instantly Anjali is standing up. Always the perfect host."
  "Archer comes downstairs with his laptop in his hands. I'm relieved to not have to talk about my mother with Anjali. "
  stop sound 
  #show ArcherNeutral.png#, Anjali moves left or right"
  show anjali neutral behind lilah:
    xalign 0.3
    yalign 1.0
  show archer normal with dissolve:
    xalign 0.8
    yalign 1.0
  #Play SE: A22.ogg"
  ar "I feel like I'm interrupting a moment. I don't mean to. I just have to send an email before I disappear off the face of the earth for a few weeks."
  #Stop SE:"

  #"
  "When he's talking to Anjali, Archer seems so much more polite. "

  an "There's a room right behind you that has a desk and some chairs in it, and also a communal kitchen across from it. Either of those rooms gets a strong wifi signal."

  #Play SE: A23.ogg"
  ar "Thanks."
  #Stop SE:"

  #"
  "He offers only a single word before turning to leave us. "

  hide archer with dissolve
  play music music_home fadein 1.0
  show anjali neutral:
    linear 0.5 xpos 0.45
  an "Should we offer him some coffee?"

  show lilah neutral at left
  li "I guess that's the polite thing to do."

  #"
  "My arms feel heavy. I want to curl up in a ball and disappear. Archer didn't dissipate the tension, only pulled my attention away from it for a second."

  an "Yeah, it is. Always offer your guest a drink."

  #"
  "Anjali begins walking towards the kitchen. "

  an "Do you want anything to drink, Lilah?"

  li "I'm good. Thanks though."

  hide anjali with dissolve

  #"
  "I walk over to the bookshelf and look at the titles idly. Anjali has a lot of detective fiction and romance novels on the shelf, a weird combination. "

  #"
  "As I wait for her, I pull a book off of the shelf. \"Love in Arms\" by some author I've never heard of. The woman looks like an independent author, as the copy of the book has a signature and a thank you note scrawled across the front page."

  #"
  "I flip through the book aimlessly until I see the words \"For you, always.\" They catch my eyes because they're highlighted in a fluorescent yellow and underlined in red. Anjali has definitely read this book before."

  #"
  "Those words must mean something to her. "

  show anjali neutral with dissolve

  an "That was a good book."

  #"
  "I jump when I hear her voice."
  show lilah blush
  li "You scared the crap out of me."

  #"
  "Anjali is standing beside me with two mugs overflowing with whipped cream. "
  show lilah neutral
  li "I take it Archer wanted a drink?"

  an "Yeah, and he thanked me three times before I left. I think he regrets his first impression, L."

  #"
  "I'm astounded. I could barely get the guy to talk to me civilly for five seconds and here Anjali has coaxed him out of his lair with the promise of a hot beverage. "

  an "I told him he could sit down here with us for a bit. It's getting dark out, so I don't imagine either you or him wanting to head outside."

  li "Is he actually going to?"

  an "You can ask him yourself when he's finished sending his email."

  #"
  "I pull my knees up to my chest and bury my face into them." 
  "Well, this is going to be an interesting few weeks. "
  jump chapter2_postDemo
  
label lbl_demoEnd:
  scene bg black with fade
  #"
  "That concludes the demo of Snowdrop. Thank you for playing! For more information on the official release, please follow us on {a=https://twitter.com/legendexg}twitter: LegendExG{/a} and {a=http://legendexgames.tumblr.com/}tumblr: LegendExGames{/a}."
  
  
  "Be sure to check the credits doc included in the zip file to see who made this game possible!"
  
  #"END OF DEMO"
  return
