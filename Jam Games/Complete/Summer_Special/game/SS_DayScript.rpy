label lbl_day_1:
  #"Day 1"
  #"Morning"
  $CurrentTimeOfDayName = 'morning'
  $CurrentDayName = 'monday' 
  #stop music fadeout 2.5
  #play music everyday  
  scene bg storeInside
  show cereza normal  
  "The soft chime of the bells greets me as I push open the worn door and enter the shop. For a split second, I can see Granny standing there, right behind the register, fanning herself rapidly while she chats with the customers."
  "But when I blink, she's gone, like a Fata Morgana. Must be the sticky summer heat getting to my head."
  "Regardless, the memory of her leaves a smile on my face. But if Granny was here, she wouldn't have send me that letter, and I wouldn't be here in the first place."

  show black with fade
  $show_quick_menu = False
  centered "Dear Cereza,   \n\nI'm sorry to ask you this, but I'll be staying in the hospital for a bit longer and I have nobody else I can trust with the shop while I'm ill. When you were young, you loved to pretend to own the store, and you were quite good at it, too! I know time has passed and you have changed, but would you do this old lady one last favor and take care of the store for a week? My part-timer June will tell you everything you need to know. Thank you for the last minute favor sweetheart.\n\nLove, Granny"
  
  scene bg storeInside with fade
  $show_quick_menu = True
  show cereza sad
  "How could I ever ignore such a request from one of the few people who has never given up on me? I visited her yesterday, and despite her cheery attitude, I could tell that she's in a lot of pain."
  "But Granny will never admit that of course, she's stubborn as a bull. I suppose I didn't get it from a stranger."
  "Granny's note mentioned a certain June, but she's not here yet. Sure, it's a little bit before seven in the morning, but we open at eight and by the look of this place, there is still a lot to do before then."
  scene bg storeInside_Register
  show storeRegister   
  show cereza normal
  "Walking up the the register I can see that the place hasn't really changed too much, with the same old posters peeling from the wall."
  "That buy one get one for free sale on bread has been going on for at least twenty years, by the look of it. Even the music is still the same as it was when I entered this shop for the very first time, the dull tunes of classical music filling the air."
  ce "Well, Granny won't mind it if I change that for a week. And if she does mind, then she isn't here."
  
    
  #play music funny  
  show cg juneIntro1
  "Lost in thought, the touch of a warm hand of my shoulder startles me out of my reverie and I quickly turn to see an equally shocked face looking back at me."
  ce "Who are you, and what are you doing in my shop!"
  show cg juneIntro2 
  un "Your shop? When did Angeline sell it?"
  scene bg storeInside_Register
  show storeRegister  
  show cereza pissed
  show june confused at right
  ce "She didn't. She's in the hospital, so I'm filling in for her. However, that doesn't answer my question. Who are you and what are you doing in my shop?"
  show june smile
  "The man smiles sheepishly as he walks around the front of the counter. Lowering the box he was carrying he then proceeds to lean forward against it giving me his full attention."
  show june grin
  un "Note taken! Well, I'll call you boss then! I work here too."
  show cereza tired
  ce "In that case, you can  help me. I'm supposed to be meeting June here. Do you know when she'll be in?"
  show cereza unimpressed
  show june happy
  "He looks at me strangely for a second, but that bubbly smile on his face never wavers."
  ju "You're looking at him! What can I do for you?"
  show cereza surprise
  ce "Ah....I...was expecting a woman."
  show june grin
  ju " Sorry, guess it's a bit confusing. My name's Jun Jie but when I started working here my boss had a bit of trouble pronouncing my name so I told her she could call me June. Now everyone else does too."
  show cereza confused
  ce "It would have been nice of her to tell me that before I got here..."
  show june normal
  ju "Oh! You must be Angeline's granddaughter then? She did mention something about you coming Monday...but aren't you a few days early?"
  show cereza unimpressed
  ce "Today's Monday."
  show june confused
  "June looks at the weathered calendar behind him as he scratches his chin thoughtfully."
  ju "Hmmm...Guess I should switch that out then..."
  show cereza smirk
  ce "That would probably be a good idea, especially since it's from 1985."
  show june happy
  ju "Wow. Yeah, that definitely has to go!"
  #stop music fadeout 2.5
  #play music everyday
  show cereza normal
  "I shrug lightly at his comment. Granny was always a bit of a packrat. Not surprised some of her quirks have trickled down to her business as well."
  show june confused
  ju "Guess we'd better get to it since we'll be working together this week...ah..."
  ce "Cereza."
  show june grin
  ju "Right, right! Let me give you a quick tour of the store then, not that you need it. I'm sure you know this place way better than I ever could."
  ce "It's been a while so a refresher couldn't hurt."
  show bg storeInside
  hide storeRegister
  show june happy
  "June happily jumps up as he walks to the middle of the shop and gestures around grandly."
  show june smirk
  ju "Here's the front of the store. Not that it's much to see or anything like that. "
  "That's the understatement of the year. Granny's shop isn't much more than a small convenience store located smack dab in the middle of a proverbial ghetto."
  "On the way to the alone shop I heard three gunshots and was questioned by the police about an armed robbery, not to mention the fourteen year old that casually offered me a discount on his drugs if I bought the package deal."
  "Granny insists that it always wasn't like this but I suppose the steady influx of drugs, guns and apathy slowly eroded everything to its current state. But despite its notorious reputation, she loves this town and has no plans of ever leaving it behind."
  show june normal
  ju "Granny usually works up front, but I guess you'll be covering that now?"
  ce "Pretty much. I've got enough customer service experience to last a lifetime so I know my way around a register. But I don't mind helping out wherever else I'm needed."
  ju "That's cool. There's always lots of other little tasks around the store that could use some attention every now and then."
  hide storeRegister
  show bg storage room
  show june normal at right
  show cereza normal
  "Beconing me to follow June leads me to a door next to the register labeled 'Employees Only'. "
  ju "And here's where all the magic happens, the back storage room. I'm usually here restocking since Granny has a hard time moving boxes and stuff now that's she's getting older."
  show bg store breakroom
  ju " There's also an area right over here that you can use for breaks or whatever."
  ce "..."
  show june tease
  ju "Guess that concludes the tour. Unless you want to see the dumpster out back..."
  show cereza tired
  ce "I think I'm good on that. Thanks though."
  show june grin
  ju "No problem!"
  scene bg storeInside_Register
  show storeRegister
  show june happy at right
  show cereza normal 
  ju "Oh yeah. Can't forget to give this to you."
  "June digs through his pockets until he unearths a large key ring littered with various charms, keys and store loyalty cards. Grinning, he unceremoniously drops its ungainly weight in my upturned palm."
  ju "Here's the keys to the store as well as Granny's apartment upstairs. I've been taking care of her plants and cats but now that you're here might I as well pass it along since you're the boss now."
  show cereza unimpressed
  "Great. Another grim reminder of my new responsibilities."
  show june normal
  show cereza normal
  ju "I have a bit of stocking left to do, but you're more than welcome to help me out if you want. I doubt any customers will be coming in this early so you probably don't have to be on register just yet."
  ce "Is there anything else that needs to be done? Like cleaning up this place?"
  ju "She likes it this way. Says it makes everything feel nice and cozy."
  ce "Heh. She would."
  menu: 
      ju "Well, other than that, the bakery will probably deliver the bread and pasteries sometime around noon. You could always wait for them."
      "Help June stock groceries.":
          $relationship_June+=1
          ce "I'll help you do stock if that's alright."
          ju "Great! More hands always makes the work go faster."
          scene bg storeInside
          show june grin at right
          show cereza normal 
          "June hands me a small box as we head back to the front of the store to begin working."
          "After a few minutes of stocking and making idle chit chat the jarring sound of the front door of the store violently opening catches our attention. "
          show rafael normal at left
          un "Where's Angie?"
          ju "Hey manl! You're really early for your shift today."
          show rafael disbelief
          un "You really think I'd be here early for fun? I just came to pick up my paycheck."
          ju "Hmmm, well I'm not really sure where Granny would have left it. And I can't exactly ask her where it is..."
          show rafael unimpressed 
          un "Just go check inside the register. Sometimes she leaves it there for me."
          show june grin
          ju "Granny hasn't quite gotten around to teaching me the register so I don't know how to use it yet. Sorry!"
          show rafael confused
          un "Unbelieveable..."
          show cereza unimpressed
          ce "And you are...?"
          show rafael sad
          show cereza angry 
          un "Don't think that's any of your business."
          ce "!?!"
          show june tease
          show rafael tired
          ju "Don't mind Rafael! He works the night shift here so his grumpy mood is more than likely due from lack of sleep."
          show june normal
          show rafael disbelief
          show cereza normal 
          ju "This is Cereza, Grannys' granddaughter. She's going to be managing the store until she comes back from the hosptial so try to be nice to her, okay?" 
          rf "Heh, whatever. So how am I gonna get paid then? There's stuff I need to do before I come back in to this dump."
          show cereza angry
          show rafael normal
          "Fed up with is attitude I stomp back to the area behind the counter and start rummaging through the register. Sure enough I find an envelope addressed to Rafael that contains his missing check."
          ce "Is this what you're looking for?"
          show cereza disbelief
          "Before I can even hand him the envelope properly he sntaches it out of my hands, scrutinizing the the check inside to make sure the amount is correct. "
          show rafael smirk
          rf "Took you long enough. "
          show cereza pissed
          ce "You know, saying 'thank you' wouldn't kill you."
          show cereza angry
          show rafael tease
          rf "Yeah, but why thank you for doing something you're suposed to do anyway Miss Manager?"
          show cereza unimpressed
          show rafael normal
          ce "..."
          rf "Later June."
          hide rafael
          show cereza normal
          ce "Is he always that rude and unfriendly?"
          ju "Not always, no. He's a prettty cool guy once you get to know him! "
          show cereza unimpressed
          ce "I have a hard time believing that..."
          ju "Well...he sorta grows on you over time."
          show cereza smirk
          ce "Much like mold or fungus, I'm sure."
          show june happy
          ju "But the good kind of mold! Like, what you find on fancy cheese."
          show cereza happy
          ce "I'll take your word for it then June."
          scene black with fade
      
      "Work at the cash register.":
          ce "It's probably a good idea for me to work at the register for the time being. Never know when a customer might show up."
          ju "That's good thinking. I'll be in the back so just call if you need me."
          hide june
          hide storeRegister
          show cereza normal
          show storeRegister
          "June smiles happily as he heads back to the storage room to begin working."
          "After a few minutes of standing idly at the register waiting for customers to show up  the jarring sound of the front door of the store violently opening catches my attention."          
          show rafael normal at left
          un "Where's Angie?"
          show cereza unimpressed
          ce "And you are...?"
          show rafael sad
          show cereza angry 
          un "Don't think that's any of your business."
          show rafael disbelief
          ce"I'm Cereza, her granddaughter and for the time being I'm in charge of managing the store until she comes back from the hosptial." 
          show cereza normal 
          ce "So yeah, whatever you want with her is my business now and the sooner you tell me your name and what you want the faster I can help you."
          show rafael tired
          rf "I'm Rafael and I work the night shift here.  I just came to pick up my paycheck. There's stuff I need to do before I come back in to this dump."
          show cereza angry
          show rafael normal
          "Fed up with is attitude I open the register and start rummaging through it. Sure enough I find an envelope addressed to Rafael that contains his missing check."
          ce "Is this what you're looking for?"
          show cereza disbelief
          "Before I can even hand him the envelope properly he snatches it out of my hands, scrutinizing the the check inside to make sure the amount is correct. "
          show rafael smirk
          rf "Took you long enough. "
          show cereza pissed
          ce "You know, saying 'thank you' wouldn't kill you."
          show cereza angry
          show rafael tease
          rf "Yeah, but why thank you for doing something you're suposed to do anyway Miss Manager?"
          show cereza unimpressed
          hide rafael
          ce "..."
          scene black with fade
       
      #call lbl_workRegister from _call_lbl_workRegister  
  #TODO >Help JJ stock"
  #TODO >Work at the register"
  #TODO need to change this so kameron isnt shown before hes introduced. lol
  #call lbl_dailyComments    
  #call lbl_dailyActivities from _call_lbl_dailyActivities
  
label lbl_day_1_afternoon:  
  $CurrentTimeOfDayName = 'afternoon'
  scene bg storeInside_Register
  show storeRegister
  show cereza normal
  show june normal at right
  "Like June said, a quarter before twelve, the doorbell chimed loudly."

  show  cg kamIntro1
  un "June! Delivery!"
  ju "About time, Kameron!"
  show cg kamIntro2
  ka "Whatever joker, I'm exactly on time. Unlike some people..."
  hide cg kamIntro2
  show kameron normal at left
  show cereza normal at center
  show june disbelief at right
  ju "Hey! That was only once!"
  show kameron tease
  show june shy
  ka "Really now? Then how about that time that I waited an hour in front of the cinema because somebody decided that alarm clocks were overrated."
  ka "Or when you promised to bring my mom some flour from the shop in 'just a few seconds' and instead made her wait another three hours?"
  show kameron grin
  show june happy
  ju "Yeah, yeah, I get it, golden boy. Anyway, may I introduce you to my new and improved overlord, miss Cezera! She's filling in for Granny."
  ka "Cezera? Is it really you?"
  ce "Long time no see, Kameron."
  show june surprise
  ju "Wait, you two know each other?"
  show kameron happy
  show june normal
  ka "We used to play together all the time! Wow, Cezera, you've really become a woman! You look a lot like your mother. How are you doing?"
  ce "Well... you sure have gotten very... tall."
  show kameron embarrassed
  ka "Yeah, second growth spurts and all that. Looks like the days where you were taller than me are in the past!"
  show cereza happy
  ce "No kidding."
  show kameron grin
  show cereza normal
  ka "I didn't know you were back in town, or I would have visited earlier."
  ce "I'm just here for the week, taking care of the shop till Granny is out of the hospital."
  show kameron confused
  ka "What happened to her? Is she alright?"
  show cereza tired
  ce "She'll be fine. She's just doing too much at her advanced age. Her cholesterol is through the roof, but she'll be fine after she recovers from her surgery."
  show kameron hurt
  ka " Please send her my well wishes. If there is anything I can do for her..."
  show cereza smirk
  ce "Don't worry too much. She's well enought to cause a stink in the hospital so i'd say she'll be back on her feet in no time.'"
  show kameron tired
  ka "If you say so... I can't help but be concerned."
  show cereza tease
  ce "So, what have you been up to, besides growing like a weed."
  show kameron normal
  show cereza normal
  ka "During the day I help my parents out in the bakery. And I'm taking classes at night."
  show june tease
  ju "Golden Boy here wants to become a nurse."
  show kameron grin
  ka "You can laugh all you want, I think it's a good way to help people out, even if it doesn't pay too much."
  show cereza smirk
  show june normal
  ce "Not surprised you'd want to do that to be honest. Helping people doesn't pay the bills, though."
  ka "Perhaps, but as long as my work is a benefit to others I'll make ends meet until it does."
  show kameron normal
  show cereza normal
  ka "But enough about me, how have you been doing Cezera?"
  show cereza tired
  ce "As well as anyone can in this hell hole of a city."
  ka "It's not that bad."
  show cereza smirk
  ce "We'll agree to disagree then."
  ka "It's a deal. Here, take a rum cake. It's my mom's specialty. Here, take one too June!"
  ju "Thanks man! Your mom is great!"
  show cereza embarrassed
  ce "These... aren't half bad."
  show kameron happy
  ka "I'll be sure to tell her."
  show cereza normal
  ce "It's been great seeing you again Kameron, but June and I have to get back to work."
  show june tired
  ju "Aw! Come on! We can take a break for a minute or five!"
  show cereza tired
  ce "There are five more crates that need to be restocked before the afternoon rush, and they won't move themselves."
  show kameron embarrassed
  show cereza normal
  ka "If you want, I could lend you two a hand. I have a few spare hours today. And starting tomorrow I can come in every afternoon after I do the delivery."
  show june tease
  ju "You? Free time? Somebody call the police, I think we have an imposter here."
  
  menu:
    ka " I'm being serious. If you guys need me I'm here."
    "Accept his offer to help.":
      $relationship_Kameron+=1
      ce "Actually, that would be great. Could you perhaps watch the register while I go through our finances? I want to get a better idea of what I'm dealing with here."
      ka "No problem! I've helped Angie out now and then, so I know my way around the shop."
      show june happy
      ju "Does that mean I can finally have my lunch break?"
      ce "Sure, go ahead. We'll manage for a bit with just the two of us."
      hide june
      "Together with Kameron, I was able to make quick work of the remaining duties in the shop. My neck might hurt every time I have to look up to him, but having someone of his height around sure comes in handy when you need to reach high places."
      hide kameron
    "Decline his offer.":
      $relationship_June+=1
      ce "Thanks, but no thanks. I've got June here to help."
      ka "Right. Well, whenever you change your mind, I'm next door at  bakery."
      ce "We might slip by during our break to say hi, but no promises."
      ka "I'll be looking forward to that, then!"
      hide kameron
      "June and I worked hard the rest of the afternoon, but we didn't have time to visit the bakery. A shame, because as much as I hate to take charity, those rum cakes were amazing."

label lbl_day_1_evening:      
  $CurrentTimeOfDayName = 'evening'
  show june normal at right
  show cereza normal
  "Time passed quicker than I had expected, and before I knew it rush hour was over and June was finishing up the last of his duties."
  ju "Would you mind if I left fifteen minutes before the end of my shift?"
  show cereza angry
  ce "Why? Do you also take evening classes?"
  show june grin
  ju "My bus home only goes twice an hour, and if I leave a bit earlier, I can just catch the early one."
  show cereza unimpressed
  ce "You're a bit of a slacker, you know that?"
  show june happy
  ju "Hey! I worked hard today!"
  ce "And you get paid for it."
  show june tease
  ju "Pretty pretty please, oh great overlord?"
  if persistent.GameFinished == True:
    #> If the player has finished the game once:"
    show cereza tired
    ce "Ugh...Sure, go ahead. I'll manage without you."
    show june happy
    ju "Yay! You're the best Cezera! Okay, I'll grab my stuff and I'm out of here!"
    ce "Hey, you said fifteen minutes! You still have another half an hour left on your shift!"
    show june grin
    ju "Fifteen minutes, thirty minutes, what's the difference? See you tomorrow morning!"
    hide june 
    ce "What a child..."
    #TODO <Introduction of Rafael>"
    rf "You're one to talk."
    ce "...you again..."
    rf "Well, it is time for my shift to start.  I'm surprised you're still here though. Thought a princess like yourself would be tucked away in her ivory tower by now."
    ce "I dont even know you, but I suggest you take that crappy attitude elsewhere next time you want to say anything to me."
    rf "Heh. Looks like Miss Manager has a bit of an attitude herself."
    ce "Only when I have to deal with obnoxious coworkers."
    menu:
        rf "Good thing you're on the day shift then. We don't have to cross paths any more than necessary."
        "I think I'll work the night shift from now on.":
            rf "You can't be serious..."
            ce "Oh, but I am. June is more than capable of handing the store by himself and Kameron offered to help so why not just leave them to it."
            ce "And from what I know you work nights alone so it's better for the store if there's two of us on duty. Less chance of any trouble going down that way."
            rf "..."
            ce "What's wrong Rafael? Not looking forward to working with me all this week?"
            rf "Like I care what you do. Working nights isn't a cakewalk so don't look my way when you figure out it's too much for you to handle."
            ce "Don't worry about me. I'm more than capable of handling anything this store can dish out."
            rf "Guess we'll see about that then, huh?"
        " I'd rather work during the day shift anyway.":  
            ce "Seems like being around you would be more trouble than it's worth."
            rf "Believe me, the feeling is mutual."
    $HasMetRafael = True
  else:
    show cereza tired
    show june sad
    ce "Out of the question. There is still a lot of work to be done, and I need someone to watch the shop while I go and make some dinner for myself."
    show june surprise
    ju "You cook?"
    show cereza angry
    ce "Does that surprise you?"
    show june happy
    ju "Actually, it doesn't. You look pretty capable."
    show cereza sad
    ce "Thanks...I guess."
    show june tease
    ju "Go ahead and start cooking then, I'll watch over the ship, captain!"
    show cereza confused
    ce "Five seconds ago I was your overlord. Make up your mind."
    show june grin
    ju "Overlord, captain, boss. It's all the same, really."
    show cereza tired
    ce "Right... Anything special?"
    show june confused
    ju "Huh?"
    ce "For dinner. Do you have any allergies or things you dislike? I don't want to make something for you only to have you puke it over our newly cleaned floor five minutes later."
    show cereza normal
    show june shy
    ju "Wait... You're offering to make me dinner? Seriously?"
    ce "If you work from seven to five here, we are obligated by law to provide you with a dinner. Doesn't Granny do that?"
    show june smile
    ju "She orders pizza for me sometimes if I work overtime, but I've never eaten her home cooked food."
    ce "That's a shame then, she makes a mean stew. Anyway, your answer please?"
    show june happy
    ju "I'll eat anything you make me!"
    show cereza smirk
    ce "One 'anything' coming up then."
    ju "You're the best, Captain!"
    show cereza tease
    ce "Nice words won't get you out of cleaning duty."
    hide cereza
    hide june
    show cg chibiJune Eat
    "Since it was getting late and he did say anything I made sandwiches, but that didn't seem to matter to June."
    "I've never seen anyone enjoy my food as much as he did, even if we had to eat it on the counter of the shop while assisting customers."
    hide cg chibiJune Eat
    scene black with fade
    "Afterwards he tried to cheat his way out of taking out the trash, but ended up losing the thumb wrestling competition over it and was stuck with it  anyway."
    "Regardless of his protests, he was smiling and chatting the entire time. When he left two hours later than he was supposed to, the shop felt empty and silent without him."
  scene black with fade
  
label lbl_day_2_night1:  
  $CurrentTimeOfDayName = 'night'
  #play music thinking
  show bg grandmaHouse 
  #show cereza tired
  "I closed the shop at nine, immediately went upstairs and plopped down on Granny's sofa."
  "Working from seven to nine every day is no joke, and I'm exhausted to the bone. Perhaps I shouldn't have been wearing heels while working, but I didn't think it would be this tough."
  "It's really no wonder that Granny got ill. Anyone would after working those hours for a lifetime."
  "I don't remember falling asleep that night, but I do remember unpacking my weekend bag full of clothing, sustaining my every move with the thought that after this week was over, I would finally have enough money to buy that car, and get the hell out of this city and never look back."
  "And if one week of putting up with the store, June and Kameron, then that is a small price to pay for my freedom."
  "With that thought in mind, I drifted off to a calm, dreamless sleep."
  scene black with fade
  #stop music fadeout 2.5
  #"End of Day 1"
  jump lbl_day_2


label lbl_day_2:
  #"Day 2"
  #"Morning"
  $CurrentTimeOfDayName = 'morning'
  $CurrentDayName = 'tuesday'
  #play music everyday
  scene bg storeInside_Register
  show storeRegister
  show cereza unimpressed  
  show june tease at right
  ju "Good Morning, Captain Sunshine~!"
  show cereza tired    
  ce "Don't talk to me before I've had my morning coffee."
  show june happy
  ju "Ah, come on! The sun is up! The birds are singing! It's a wonderful day!"
  show cereza unimpressed   
  ce "Your lips are still moving and yet there's no cup of coffee in your hands."
  show june disbelief
  ju "Geez, you're a grump in the morning, you know that?"
  show cereza angry
  ce "Duly noted. Now hurry up and make a batch of coffe so I can try and deal with your sunny disposition."
  ju "Well as much as I'd like to do that the coffe machine for the store broke a few months back and Granny hasn't got around to replacing it yet."
  ce "...are you serious?"
  ju "As serious as a heart attack."
  ce "Ugh..."
  ju "I can run down to the Burger Queen and grab you a cup of coffee if you want me to. Can't say it'll be the best quality but-"
  ce "Yes. Please. Go."
  show june grin
  ju "Your word is my command, oh great overlord of Angie's Mart! I'll be back in a bit!"
  hide june 
  show cereza tired  
  "Finally, peace and quiet. Well, that is until the first customers arrive."
  show kameron normal at left
  show cereza sad
  ka "Still haven't beaten that morning mood, huh?"
  show cereza embarrassed
  ce "....You're early."
  ka "I told you yesterday, that if I would have known you were back in town that I would drop by before I start my shift. And you know I never go back on a promise."
  ce "You shouldn't have bothered."
  ka "Let's see how you feel about that after you've tasted the Golden Waves patented sorrel ginger morning special smoothie. It's not coffee, but I swear it's the next best thing, and better for your health on top of that!"
  "Kameron proudly hands me a cup of a cheery red, sweet smelling liquid and I tentively take a sip. A spicy kick of ginger followed by a soothing floral flavor quickly fill my mouth and I grudgingly smile in appreciation."
  ce "Okay, so perhaps I will reconsider my opinion. Come back tomorrow and find out."
  ka "Haha! That I will! I even brought some for June. Could you please give it to him  when he finally shows up?"
  ce "June actually beat me to work today but I send him out to get me coffee not long ago."
  ka "No way! So he's already here? Your managing skills must be supernatural, if you got him whipped into shape within a single day."
  ka "Angie always complains that he's late, but she hasn't got the heart to reprimand him or anything."
  show cereza smirk
  ce "June's not so bad once you rein him in."
  ka "We all have our shortcomings, and he's a good guy on the inside. Anyway. I have to go help my mother with the ovens. I'll come back this afternoon with your delivery but after that I'm all yours."
  ce "Kameron...You don't have to work here pro bono. You have enough on your plate as is without me imposing."
  ka "Don't worry about it! I'm not needed at the bakery in the afternoon and your Grandmother paid a part of my tuition when my mother couldn't afford it, so I'm not really working here for free."
  ka "This is just my way of giving back to Mrs.Angie after all she's done for me and my family."
  show kameron embarrassed
  ka "Besides, I like seeing your face again after such a long time. See you in a few hours, Cereza!"
  show cereza embarrassed
  ce "Yeah you too, Kameron."
  hide kameron
  #[Choose Morning activity] "
  #call lbl_dailyActivities from _call_lbl_dailyActivities_1 
  "Start lbl_dailyActivities choice call"
  call lbl_dailyActivities from _call_lbl_dailyActivities
  "End lbl_dailyActivities choice call"
  jump lbl_day_2_afternoon
  
label lbl_day_2_afternoon:
  $CurrentTimeOfDayName = 'afternoon'
  show june happy at right
  show cereza normal
  ju "Time for a break?"
  ce "You can go first, if you want to. I'll watch the shop."
  ju "How about I get you some snacks to celebrate a job well done? I'm sure Kameron can give some discount to his favorite customers."
  show kameron grin at left
  ka "Kameron knew you would say that, and came prepared."
  ju "Aww man! You're an angel, you know that?"
  ka "And one for the lady."
  ce "You shouldn't have.... Okay no I take that back, this is delicious!"
  ka "Thank you! I remember how much you always liked the mango tarts my dad made when we were kids so I asked him for the recipe and made these just for you."
  ka "Consider them a welcome home present."
  ju "Hey, dude! I'm right here, you know!"
  ce "Guys shut up, or I'll put you both back to work while I eat both of your cakes in front of you."
  ka "Technically you're not my boss-"
  ce "Do you really want to see me try?"
  ju "Yes captain!"
  ka "Yes ma'am. I assume you need my help today, then?"
  ce "I could use an extra pair of hands, that's for sure."
  ju "By which we mean, the extra meter attached to the pair of hands."
  "I watched them go at it for a bit, and suddenly working in the worn down shop wasn't all that bad, though that was perhaps the heat talking. Granny should get that air conditioner fixed."
  ce "Anyway, June, go take your lunch break. You've deserved it."
  ka "Why don't you go with him Cereza? I can watch the store for a bit while you two sit down since I have to restock the pastry case with todays' delivery anyway."
  
  menu:
    ju "I can wait for another half an hour, don't worry about me. Why don't you go first today, Cereza?"
    "Take a break with Kameron.":
      $relationship_Kameron+=1
      ce "Thank you June. I kind of want to sit down and enjoy the sun for a bit. I'm not quite used to working from dawn till dusk just yet."
      ka "Allow me to treat you then."
      ce "No, I'll pay this time. See you in a bit, June!"
      ju "Yeah, see you soon..."
      #TODO (N and MC go outside)
      show bg storeFront
      hide storeRegister
      ka "I was serious about treating you, you know. Our bakery is just next door and my family has been dying to see you ever since they heard you're back in town."
      ce "You're going to make me gain so much weight if you keep that up, so let me to treat you with something healthy this time. Let's head to that café."
      ka "If you insist."
      ce "Wait a second, I'm getting a call."
      hide kameron 
      hide cereza  
      show cg chibiKam Phone5
      ce "Hello?"
      gr "Hey darling-"
      show cg chibiKam Phone1
      ce "Grandma! Is something wrong? Do you need me to come to you?"
      show cg chibiKam Phone2
      gr "I'm fine honey, don't worry about me! I was just curious about the shop. Is everything going alright?"
      show cg chibiKam Phone4
      ce "I'm handling everything perfectly fine. We've had no trouble at all."
      show cg chibiKam Phone3
      ka "She's doing great, Mrs.Angie. The store has never been cleaner."
      gr "Kameron, is that you? Are you trying to win my granddaughter over with sweets?"
      ka "No, Mrs.Angie, I'm merely making sure she eats well."
      show cg chibiKam Phone4
      ce "I can take care of myself."
      gr "Of course you can, dear. But I'm happy that you're not in that store alone all the time. It can be dangerous at night, so make sure you lock up after you close for the night."
      show cg chibiKam Phone6
      ce "Naturally."
      gr "And don't throw away my posters. Or my teddy bears. Or that little dragon I got from June at New Years! I know it's broken, but it's the thought that counts!"
      show cg chibiKam Phone5
      ce "I'll try to restrain myself, Granny."
      gr "And take care of yourself, dear. You're a bit too much like your old grandma after all, always tackling things all by yourself."
      show cg chibiKam Phone6
      ce "I'll be fine. You worry about yourself first, I'm not the one in the hospital!"
      show cg chibiKam Phone5
      gr "You got me there, dear. Now, the nurse is looking like she'll kill me if I don't hang up any second now, so I'm afraid I'll have to cut it short. Love you, baby!"
      show cg chibiKam Phone7
      ce "Love you too, Granny."
      ka "Get well soon, Mrs.Angie!"
      hide cg chibiKam Phone7
      show kameron happy at left
      show cereza normal at center      
      ce "Still as stubborn as always."
      ka "I'm curious how they managed to keep her in the hospital for as long as they have already, she hates them."
      ce "I didn't think it was that bad?"
      ka "The year before she broke her finger and refused to go to the doctor for nearly a month. I set it myself with the tools I have at home, but it still won't bend the way it used to. I'm not a doctor after all."
      ce "I'm happy she has you and June to look after her."
      ka "And now, she has you as well."
      ce "I'm not staying for long."
      ka "What? But you only just got back!"
      ce "I've got my reasons. Anyway, we should head back before June breaks down the store."
      ka "He wouldn't... Mrs. Angie would skin him alive."
      ce "That's exactly why I'm worried."
      scene black with fade
    "Take a break with June.":
      $relationship_June+=1
      ce "Thank you Kameron. We could both use a break after that annoying customer we had."
      ka "Of course! Don't worry about anything, I'll man the fort."
      ju "You're a star, Golden Boy!"
      #(June and Cereza go outside)
      show bg storeFront
      hide storeRegister
      ju "He has really taken a shine to you, you know that? He's never that open towards strangers."
      ce "We go way back. When I was young and we still lived nearby, we used to play tag while our parents were working."
      ju "That sounds like fun! We should try that out some time here as well!"
      ce "Considering the rampage we used to cause, I don't think so."
      ce "Wait a second, I'm getting a call."
      hide june
      hide cereza
      show cg chibiJune Phone5  
      ce "Hello?"
      gr "Hey darling-"
      show cg chibiJune Phone1
      ce "Grandma! Is something wrong? Do you need me to come to you??"
      show cg chibiJune Phone2
      gr "I'm fine honey, don't worry about me! I was just curious about the shop. Is everything going alright?"
      show cg chibiJune Phone4
      ce "I'm handling everything perfectly fine. We've had no trouble at all."
      show cg chibiJune Phone3
      ju "Don't worry Granny! She's got me at her side, nothing could possibly go wrong!"
      gr "June, is that you? Aren't you supposed to be working?"
      ju "Kameron took over for a second so we could take a break! He even brought us some lunch. It's a rum cake, your favorite!"
      gr "How about you sneak one of those fine cakes past these nurses? I swear, the food they're serving me here is terrible! If I hadn't been sick already, I would be now!"
      show cg chibiJune Phone6  
      ce "It's not that bad."
      gr "You haven't tasted it, so you can't judge."
      show cg chibiJune Phone5  
      ce "I might save one for you when I visit you, but only if you promise to get better soon."
      gr "You're an angel. I'll try to get better soon, but only if you'll also take care of yourself, dear. You're a bit too much like your old grandma after all, always tackling things all by yourself."
      show cg chibiJune Phone6
      ce "I'll be fine. You worry about yourself first, I'm not the one in the hospital!"
      show cg chibiJune Phone5 
      gr "You got me there, dear. Now, the nurse is looking like she'll kill me if I don't hang up any second now, so I'm afraid I'll have to cut it short. Love you, baby!"
      show cg chibiJune Phone7
      ce "Love you too, grandma."
      ju "Get well soon Granny! Once you get home, I'll make you some samgyetang and I'll swear you'll be back on your feet in no time!"
      gr "I'm looking forward to that, dears. Now, Bye!"
      ce "Bye!"
      hide cg chibiJune Phone7
      show june happy at right
      show cereza normal
      ju "She sure is one cool old lady."
      ce "She sure is."
      show june grin
      ju "Must be a family trait, then."
      show cereza tired
      ce "What do you mean by that?"
      ju "Well, not everyone would  just drop everything to manage their grandmother's store the second they heard she was sick. That's pretty cool, in my opinion."
      show cereza embarrassed
      ce "It's nothing."
      show june tease
      ju "Sure, sure. You're bad with compliments, I get it. Anyway, she is pretty lucky to have you."
      ce "It's only for a week."
      show june confused
      ju "Why? I thought you were going to take over the ship from the old lady?"
      show cereza unimpressed
      ce "Like she would let me. No... this is just temporary. After this week, I'm out of this rotten town."
      ju "But.... Why?"
      show cereza pissed
      ce "Look around, June! There is nothing left here!"
      ju " This is your home...Won't you miss it? How can you just...you know, leave?"
      ce "....I'm sure the drug dealers and prostitutes will get along well enough without me around."
      ce "Anyway, we should get back to work before a conartist with a fake sob story comes in and Kameron ends up giving half the store away. "
      ju "He wouldn't do that... right?"
      ce "Well, there was this one time when we were young...."
      scene black with fade
    "Take a break alone":
      if HasMetRafael:
        #(MC takes a walk in the park/? And meets Raphael.)
        $relationship_Rafael += 0
        "Meet Raf."
        scene black with fade
      else:
        #(Player takes a solitary walk, enjoys the sun and notes the bad shape of the neighborhood. When she returns she notes that there is an uneasy tension between N and JJ)
        "Solo Walk"
        scene black with fade
  
  #TODO [Afternoon Activity Choice]"
  #call lbl_dailyComments   
  #call lbl_dailyActivities from _call_lbl_dailyActivities_1
  show bg storeInside
  show cereza normal
  call lbl_dailyActivities from _call_lbl_dailyActivities_1
  jump lbl_day_2_evening
  
label lbl_day_2_evening:  
  $CurrentTimeOfDayName = 'evening'
  show bg storeInside_Register
  show cereza normal at center
  show storeRegister  
  show mona normal at left
  "The store is as busy as ever and a long line of customers are in line to be checked out. Groaning at the increase in customers just as we're on the verge of closing I quickly ring them up as soon as I can."
  "A familiar face, however causes me to slow down."
  ce "Hi Mona. It's been a while. "
  mo "I had heard you were back in town Cereza but had to come and see it for myself. Sorry to hear about Granny. How's she holding up?"
  show cereza grin
  ce "Same old, same old. If they poke her with another needle she just might make a run for it though. Still run the mechanic shop down the road?"
  show mona smile
  mo "Yup. Just left their actually. Had to stop by real quick before you guys close for the night. Gotta pick up some dinner."
  show cereza tease
  ce "I see....Vienna sausage, beer and ramen. The dinner of champions."
  show mona happy
  show cereza happy
  mo "Don't you know it! It was good seeing you Cereza. And tell Granny I'm coming to visit here as soon as she gets home."
  ce "Sure! Take care."
  hide mona
  #call lbl_dailyActivities from _call_lbl_dailyActivities_3
  call lbl_dailyActivities from _call_lbl_dailyActivities_2
  jump lbl_day_2_night
  
  
label lbl_day_2_night2:
  scene black with fade
  $CurrentTimeOfDayName = 'night'  
  show bg storeInside
  show june normal at right
  show cereza normal  
  show kameron normal at left
  "With the last few customers exiting the store I happily lock the door and flip the store sign from 'Open' to 'Closed'. Taking a much needed sigh of relief I work along side June and Kameron to tidy up the store."
  show bg storeOutside back2
  "Before long everything is clean and properly in it's place. Flipping the lights off we all make our way out the back employee entrance and into the humid night air."
  show june tired
  ju "So tired! I think my aches and pains have aches and pains!"
  show cereza unimpressed
  ce "Are you seriously complaining? I could have sworn you talked more than actually worked today."
  ju "No way Boss! I did tons of work. Like, literally tons."
  show kameron grin
  ka "To be fair, I did see him lift some really heavy boxes today..."
  show june grin
  ju "Told ya!"
  show kameron tease
  show cereza happy
  show june unimpressed
  ka "...Too bad they were all filled with toilet paper though."
  ju "Wow. And here a thought you were on my side. I'll have you know toilet paper can be pretty heavy when it's packaged in bulk Golden Boy."
  show cereza tease
  ce "I'm sure it was. Anyways, thanks for your guys hard work today. See you tomorrow?"
  show kameron happy
  show june happy
  ka "Of course."
  ju "Later Captain!"
  hide kameron
  hide june
  if relationship_June > (relationship_Kameron):
      show cereza normal
      "As I turn to finishing locking the back door a familiar figure lingering nearby catches my attention."
      show june normal at right
      show cereza sad
      ce "Did you forget something in the store June?"
      show june smile
      ju "Not really. I was just wondering if I'd be okay if I walked you home?"
      show cereza normal
      ce "I'm literally going right upstairs. I think I can manage that far on my own."
      show june grin
      ju "Yeah...but I'd make me feel better knowing your inside safe and sound before I leave to catch my bus."
      show june normal
      ju "Can't be too careful this time of night, you know?"
      show cereza smirk
      ce "Suit yourself. But don't blame me if you miss your ride home."
      show june grin
      ju "Heh, Course not!"
      show cereza normal
      "With that said June walks me the few feet to the entrance of Grannys' upstairs apartment."
      show june normal
      ce "Looks like this is where we part ways. Thanks for walking with me June."
      ju "Oh yeah, no problem!"
      ce "You'd better hurry and get a move on before the bus comes."
      show june embarrassed
      ju "I'm going. But first...I just wanted to say thanks Cereza."
      show cereza confused
      ce "Hmmm? For what?"
      show june shy
      ju "For coming here and helping Granny. I'm sure she really appreciates the help...and it's nice having you around."
      show cereza tease
      ce "Well, enjoy it while it last. I'm sure Granny will be back and running things in no time."
      ju "Heh, yeah."
      ce "See you bright and early tomorrow morning June."
      show june happy
      ju "I'll be there with bells on!"
      show june grin
      ju "Ah, not literally though. It's just a figure of speech. But I will be there, and on time too!"
      show cereza happy
      ce "I'm going to hold you to it. Now hurry up and go!"
      show june happy
      scene black with fade
      "With one last laugh and wave goodbye June dashes off to the nearest bus stop. Walking upstairs I can't help but chuckle at his antics."
      "It's been a while since I've been able to enjoy a smile with people I work with."
  elif relationship_Kameron > (relationship_June):
      "As I turn to finishing locking the back door a familiar figure lingering nearby catches my attention."
      show kameron normal at left
      ce "Did you forget something in the store Kameron?"
      show kameron shy
      ka "No. I was just wondering if I'd be okay if I walked you home?"
      ce "I'm literally going right upstairs. I think I can manage that far on my own."
      show kameron grin
      ka "I know. I just want to make sure you're getting in okay."
      show kameron normal
      ka "Can't be too careful this time of night. "
      show cereza smirk
      ce "Suit yourself. But don't blame me if you're late for school."
      show kameron grin
      ka "Class doesn't start til nine thirty so I have plenty of time to see you home and make it there."
      show cereza normal
      show kameron normal
      "With that said Kameron walks me the few feet to the entrance of Grannys' upstairs apartment."
      ce "Looks like this is where we part ways. Thanks for walking with me Kameron."
      ka "My pleasure."
      ce "You'd better hurry and get a move on before you're late."
      show kameron embarrassed
      ka "I'm going. But first...I just wanted to say thanks Cereza."
      show cereza confused
      ce "Hmmm? For what?"
      show kameron shy
      ka "For coming here and helping Granny. I'm sure she really appreciates the help...and it's being able to spend time with you again  like we did when we were younger."
      show cereza tease
      ce "Well, enjoy it while it last. I'm sure Granny will be back and running things in no time."
      show kameron happy
      ka "I'm sure she's already itching to come home by now."
      show cereza happy
      ce "Oh, most definitely! See you tomorrow Kameron."
      show kameron normal
      ka "You too Cereza."
      scene black with fade
      "With one last  wave goodbye Kameron hurries off to school. Walking upstairs I can't help but chuckle at his behavior."
      "It's been a while since I've been able to enjoy a smile with people I work with."  
  else:
      scene black with fade
      "With one last laugh and wave goodbye I hurry up the few feet to Grannys' apartment and unlock the door. Walking upstairs I can't help but chuckle at both their antics."
      "If anything working at Grannys' store and being around those two everyday is sure to keep me entertained."   
  jump lbl_day_3
    
label lbl_day_3:
  #"Day 3"
  #"Morning"
  $CurrentTimeOfDayName = 'morning'
  $CurrentDayName = 'wednesday'
  if meetKids == False:
      scene bg storeInside_Register
      show storeRegister
      show june hurt at right2 
      show madison happy
      show rashid normal at left
      un "Awww! Come on June! It's gonna be sooooo fun! Tell em' Rashid."
      show rashid happy
      ra "Uh huh, Madison's right! Terrence even said that whatever team wins the kickball tournament will get a one year pass for free unlimited tokens as Pizza Wally."
      show madison joke
      ma "Not to mention free pizza too. You love pizza June! And the free just makes it all taste even better!"
      show rashid smile
      ra "We just need one more member on our team! Pretty please June!"
      show june tired
      ju "...ugh..."
      ju "...I can't just leave work to play with you guys..."
      show madison sad
      show rashid sad
      ma "Why not? Winning the grand prize is worth way more than missing a day of work. We'll sneak out the back. Your boss won't even know you're gone."
      show june shy
      ju "Cereza really needs me to be here to help. It's not fair to leave her with all the work I'm supposed to do."
      show madison tease
      show rashid normal
      show june embarrassed
      ma "Just tell her you're sick or somethin'. That always works for me when I want to get out of a test at school."
      show cereza angry
      show madison normal at left
      show rashid normal at left2
      show june surprise
      ce "June! Who are these delinquents and why are they trying to get you to bail on work?"
      show june embarrassed
      ju "Ah...this is  Madison and Rashid. Guys this is Cereza, my boss."
      show madison sad
      ma "Sorry to be the bearer of bad news Cereza, but June here is sick and has to leave early. So if you'll exscuse us we'll be on our way~"
      ce "Not so fast short stuff. What is he sick with exactly?"
      show madison tease
      ma "Uhhh...."
      show rashid smile
      show june surprise
      ra "H-hemorrhoids! He has a super bad case of hemorrhoids!"
      show madison sad
      show june disbelief
      ce "Hemorrhoids? Really?"
      show rashid tease
      ra "Uh huh! And t-they're like, really contagious so unless you want them too I think June needs to go home right now immedietly!"
      show june tired
      ju "..."
      show rashid worry
      ce "You guys can cut the act. I overheard your little scheme so I'm afraid June isn't going anywhere today."
      ma "..."
      ra "..."
      show rashid sad
      show june shy
      ju "Sorry guys. Thanks for trying though."
      show madison angry
      ma "Why'd you pick a dumb sickness like hemorrhoids?!"
      show rashid worry
      ra "I don't know! I hear grandpa and his friends talking about them all the time so I thought they were like, adult chicken pox or something..."
      hide madison
      hide rashid
      show cereza smirk
      ce "Some friends you got there."
      show june grin
      ju "They're harmless enough. But I think i'll go to the back now and start sorting through boxes. Never too early to put in a hard days' work!"
      show cereza tease
      show june happy
      ce "Yeah, I think that's for the best. Don't want the customers to catch your hemorrhoids now do we. "
      ju "Heh! "
      $meetKids = True
  else:
      scene bg storeInside
      show june normal at right2 
      show madison normal at left
      show rashid normal at left2
      show cereza unimpressed at center
      ce "Don't tell me your little fan club is here to help you bail on work again June."
      show june hurt
      ju "I'm not trying to skip work, honest Captain!"
      show madison happy
      show june normal
      ma"We're not here for you June. We came to talk to Cereza about a businees propostion."
      show cereza smirk
      ce "You don't say. What could you kids possibily want with me?"
      ra "Madison and I are want to start a lemonade stand and we were wondering if you'd like to be our business partner."
      show cereza unimpressed
      ce "Uh huh."
      ma "And since we're just kids and all, we're hoping you'd be a kind and generous benifactor to help us  get started."
      show cereza disbelief
      ce "Ah... I see....So you guys just want me to give you money but what do I get out of the deal?"
      ma "The joy of helping children, obviously!"
      show cereza tired
      ce "Not interested."
      show june tired
      ju "Boss..."
      show cereza normal
      ce "What?"
      show june shy
      ju "A lemonade stand doesn't sound like a bad idea. I mean, it'll give them something to do and teaches them about money."
      ra "And we won't be around to bug June so it's like you benefit that way too!"
      show madison joke
      ma "There's a lot worse thing we could be doing during Summer vacation!"    
      show cereza tired
      ce "...all  you guys are a bunch of moochers, you know that?"
      show madison happy
      show june grin
      show rashid happy
      ce "But whatever. If it'll get you off my back i'll help you guys out. But this is going to be a business transaction and not a partnership so you're going to have to sign a contract."
      ce "I'll front you guys some cash until you sell enough lemonade to pay me back but after that you're on your own. You can take whatever supplies you need from the store and June will start a tab so i'll know what ya'll owe me. "
      "I grab my purse and hand Madison a $50 bill."
      show cereza normal
      ce "And don't even think of spending my money at the arcade. I'm going to be watching you both like a hawk until you pay me back."
      ra "Whooo! Thanks Cereza! You're the bestest!"      
      show madison tease
      ma "Don't worry Cereza. We'll name a special lemonade after you. Should go along with great your sour personality! Bye!"
      ra "Later!"
      hide madison
      hide rashid
      show cereza pissed
      show june happy
      ce "Get back here you ungreateful brats!!!"
      "Madison and Rashid scamper happily out the door, waving the money I gave them proudly. June on the other hand, can't keep himslef from nearly doubling over with laughter."
      show cereza angry
      ce "What are you laughing at? It's not that funny..."
      show june grin
      ju "It's just that they remind me alot of you Captain. "
      show cereza unimpressed
      ce "If I'm ever that overbearing, annoying and hard headed you have my permission to knock some sense into me."
      show june tease
      ju "Well in that case~"
      "June casually leans close to me and lightly flicks my forehead."
      show cereza pissed
      ce "June!"
      show june happy
      show cereza angry
      ju "What? You told me I could do it Captain. Just be glad I don't make it a point to hit girls."
      ce "Try that again and you'll be missing a few fingers, got it?"
      show june happy
      ju "I don't doubt you for a second boss!"
     #ma "We take checks, cash or cards."      
  #[Choose Morning activity] "
  call lbl_dailyActivities from _call_lbl_dailyActivities_3
  "End lbl_day_3_morning"
  jump lbl_day_3_afternoon
  
  
label lbl_day_3_afternoon:  
  $CurrentTimeOfDayName = 'afternoon'
  scene bg storeInside
  show cereza unimpressed at left2 
  show june tease 
  show cody worry at right  
  ju "You're looking particularly angry. What's got your goat Captain?"
  ce "Do you know that kid?"
  ju "Hmmm...I've seen him around a few times but I don't think he hangs out with any of the kids I know. Why do you ask?"
  ce "...Something's up with him..."
  ju "Oh? I don't know what you're talking about. He looks pretty normal to me."
  "I continue to watch on as the kid in question wanders into another aisle, nervously glancing over his shoulder. After a few moments of fidgeting he bends down and quickly stuffs some items into a well worn bookbag."
  ce "Did you see that?! The little rat is stealing!"
  "Noticing that he's making his way towards the exit I quickly come up behind him, grabbing him by the collar and lifting him a few feet off the ground."
  show cody shock at center
  show cereza pissed at left
  show june surprise at right
  ce "Where do you think you going?!"
  un "!!!"
  un "P-please d-don't--"
  ce "What? Call the police? Don't you know what happens to little boys who steal?"
  show cody cry
  show june confused
  "Ripping the backpack out of his hands I quickly dump it's contents onto the store floor. Containers of baby formula, diapers, a loaf of bread, hot dogs and multiple cans of pork and beans quickly litter the surrounding area."
  "Dumbfounded I can only stare on in confusion as the child lets out heavy sobs as he continues to dangle from my frozen fingertips."
  show cereza angry at left2
  show kameron sad
  show june sad at right2
  show cody cry  at right
  "A steady hand squeezes my shoulder lightly and I turn to see a concerned Kameron standing behind me. I slowly lower the crying child to the ground and he slumps down to the floor dispondently."
  "June quickly approaches and leans down on the floor next to the now uncontrollably blubbering would be thief."
  show cody cry big
  show kameron normal 
  un "I'm s-s-s-sorry!"
  ju "It's okay. What's you're name kid?"
  show cody cry
  co "C-Cody. Cody Townsend."
  show kameron normal 
  ka "Okay Cody. Everything's going to be just fine.  We just want to talk to you for a bit."
  show cody sad
  show kameron hurt 
  "Cody continues to sniffle as my coworkers hover around him offering the occasional reassuring touch or a fresh tissue for his overflowing tears."
  ka "Why did you come here and take those things Cody?"
  co "I didn't want to b-but I didn't have a choice! Mommy is sick in bed, m-my sisters were hungry and the baby doesn't have any diapers..."
  ka "So you came here to get stuff for them, right?"
  co "..."
  ka "It's okay to tell us. No one here is going to hurt you."
  co "I know it's wrong to take anything that doesn't belong to me, b-but I didn't know what else to do! I'm their big brother and Mommy left me in charge. I had to do s-something..."
  ju "What about your dad?"
  "Cody looks down at the floor and shrugs sadly. Growing up in this neighborhood it's not surprising many kids don't have a father figure in their lives."
  "Lost in thought, everyone startles when June suddenly jumps up from his place on the floor and quickly picks up the nearly stolen goods. He  places them into a plastic grocery bag, along with a few other toiletries and food stuffs, and hands the now heavy bundle to Cody."
  ju "Take this home. I know it's hard being the one to take care of your family but just know you can come here for help when things get tough."
  ju "We're going to make sure you and your family are alright."
  ka "That's right. And if you ever want to earn a bit of money working, you can come next door to the bakery. There's always little tasks like picking up litter or washing windows that we could use help with. "
  ka "You don't have to take anything you need. Just ask and we'll do our best to help."
  co "T-thank you!"
  ka "Why don't you come with me to the bakery now? Smells like my mother just pulled a fresh batch of pineapple cakes out of the oven and I'm sure she's like another taste tester on board. Sound good?"
  "Cody nods happily as Kameron takes his hand and leads him out of the store. With them  gone June whistles happily as he goes back to the stockroom, leaving me alone."
  hide kameron
  hide cody
  hide june
  show cereza normal at center
  menu: 
      "Everything seems to be resolved, but a nagging feeling keeps brushing across my mind as I think about what happened."
      "Follow Kameron out the store and talk to him":
          $relationship_Kameron+=1  
          show bg storeFront 
          show cereza pissed 
          show kameron normal at right2
          show cody normal at right
          "I hurry out the store, intent on finding Kameron and having a talk with him. Looking around outside I see the pair nearby."
          ce "Hey! Wait a second!"
          ka "Sure Cereza. Why don't you go on inside Cody? I'll be there in a second."
          "The bosy nod enthusiastically before going into the bakery, leaving Kameron and I standing outside the shop."
          hide cody
          show kameron normal at right
          ka "If you wanted to talk about the items June gave Cody don't worry about it, I'll reimburse you for the cost of everything once I get him settled in."
          ce "I'm not worried about that. I planned to doct the cost from Junes' pay regardless."
          menu:
              ka "Is there anythingthing else you wanted to talk to me about then?"
              "Why did you help that kid?":
                  ka "What do you mean?"
                  ce "He was stealing Kameron! There's enough crime going on without us condoning someone taking from what little profit the store makes."
                  ce "As someone who's grown up around here I know you're well aware of the effect shop lifters and burglars can have on a business."
                  ka "He's just a kid Cereza. I seriously doubt he would have done what he did if he felt like he had no other choice."
                  ce "There's always a choice and he just so happened to choose wrong this time! And you coddling him will only encourage him to keep up that bad behavior."
                  ka "...I had no idea you feel that strongly about it. But now I understand where you're coming from and I'm sorry for overstepping my boundaries."
                  ka "You're in charge of Angie's Mart and have the final say as to what happends to anyone who breaks the law there. I had no business interferring. Next time I'll check with you first before doing anything."
                  ce "I'd appreciate that. And it's okay, I know it's not in you to stand back without trying to help at least a little."                  
                  ka "Thanks for being so understanding Cereza."
              "I just wanted to say thanks for helping.":
                  ce "I got a little...overwhelmed back there so I just wanted to thank you for stepping in to lend a hand."
                  ce "The store is struggling enough as it is so when I saw him stealing..."
                  ka "Don't worry about it, I really do understand where you're coming from. With things so tight money wise around here it's hard not to get a little upset when someone shop lifts."
                  ka "I've had to chase down my own fair share of dine and dashers over the years."
                  ce "Don't tell me that's how you managed to get in shape? Maybe I should give chasing after thieves a try. I'm sure my legs would look amazing afterwards."
                  ka "Not the workout regimen I'd personally recommend but if anything I'd be great cardio!"
                  ce "Oh, I'm sure!"
                  #ka "I just couldn't stand by and let a child suffer when I have the ability to step in and help."
                  #ka "My pleasure."
          ce "I just don't know why you decided to help him in the first place since it wasn't your problem to begin with."        
          ka "It might sound strange to you but I sympathize with Codys' predicament. "
          if relationship_Kameron >= 3:  
              ka "I was three when my parents first left for the United States. Unfortunately they didn't have enough money to bring me over when they came so I had to stay with my grandmother in Martinique."
              ka "For five long years I stayed behind, struggling everyday to work on grandmothers' sugar cane fields and hurting over the loss of my parents."
              ka "Eventually they saved enough and brought me to live with them but things weren't the same anymore. Unbeknownst to me, my parents had had my sisters while living abroad."
              ka "Having been born here my sisters never had to learn our native French while I had little knowledge of English, making it hard to connect to them, let alone any other kids. And because they were younger they took up the majority of my familys' attention."
              ka "I felt like my parents had forgotten and replaced me all in the same moment. That I was left all alone to fend for myself in a foreign world."
              ka "It was a dark and difficult time but Mrs. Angie and you help to make my first few months here better than I thought they could be."
              ce "Huh, me?"
              ka "You were probably too young to remember much, but your grandmother would often ask me to help her with reading books to you, which in turn helped me to learn English faster."
              ka "Mrs.Angie gave me purpose and a sense of belonging. He kindness planted the seeds of the man I am today."
              ka "And given all of that, I'd say you had a larger part in me wanting to help other than you may have originally thought."
          ka "A child shouldn't have to handle such a burden alone and I just couldn't stand by and let him suffer when I have the ability to step in and be of assistance. "
          ka "Cody is doing his best to make a life for himself out of the hand fate has delt him. But I think with the right guidance he'll turn out to be a outstanding young man."       
          ka "Regardless of all that, we're still a community and it's important for everyone to help and look out for each other." 
          ce "If only everyone thought like that this place wouldn't be such a dump..."
          ka "I won't deny that life can be rough around here or that things couldn't use some fixing up. But what we lack in outer appearance the neighborhood more than makes up for with in heart."
          ce "Heh. Spoken like a true boy scout. Don't you think you're being a bit naïve though? I doubt things will get better around here, regardless of what anyone does..."
          ka "Maybe I am a bit optimistic but I'm just not ready to give up on this place, and everyone in it,  just yet."
          ce "You sound just like Granny."
          ka "I'll take that as a compliment then. Mrs. Angie is an amazing woman and one day I hope to aspire to have even half her greatness. " 
      "Stay here and talk to June.":
          hide kameron
          hide cody
          $relationship_June+=1  
          "Since Kameron and the kid are gone now is a good a time as any to have a chat with June so I follow him to the storeroom."
          show bg storage room
          show cereza normal
          show june normal at right
          ce "June, do you have a second to talk?"
          show june happy
          ju "Oh hey, perfect timing! You're just the lady I wanted to see!"
          ju "Sorry about giving Cody all the stuff without asking first. I got a little caught up in the moment but I'll reimburse you for everything as soon as I can."
          show june disbelief
          ce "That's the least of my worries. I planned to doct the cost of the items from your pay regardless. I'm running a business here, not a charity."
          ju "A-ah okay, that's fine! Guess the landlord won't mind if I'm a tad short on rent..."
          menu:
              ju "Was there anything else you wanted to talk to me about Captain?"
              "Why did you help that kid?":
                  #play music sad
                  show june confused
                  ju "Uh...What do you mean?"
                  ce "He was stealing June! There's enough crime going on without us condoning someone taking from what little profit the store makes."
                  ce "Maybe since you're not from around here you don't know the particulars but shop lifters and burgalars can have a huge effect on a business, especially one as small as Angie's Mart."
                  ce "Enough of them taking from our stock could even lead to the store shutting down. What's Granny going to do then?"
                  show june tired
                  ju "Ah...I didn't think of all that...."
                  show june embarrassed 
                  ce "Exactly! And you not thinking ended up costing us in revenue today, not to mention the fact you helped a thief reinforce their horrible behavior."
                  show june angry
                  ju "But he's just a kid boss! I don't think he felt like he had another choice in the matter."
                  show june sad
                  ce "There's always a choice and he just so happened to choose wrong this time! And you coddling him will only encourage him to steal again."
                  ju "..."
                  ju "I'm sorry...I didn't mean to hurt you or the store when I stepped in with Cody today."
                  show june shy
                  ce "*sigh* It's okay June. I know you were just trying to help but next time let me handle things, alright?"
                  ju "Sure. Thanks for being so understanding Cereza."
              "I just wanted to say thanks for helping.":
                  show cereza sad
                  ce "I got a little...overwhelmed back there so I just wanted to thank you for stepping in to lend a hand."
                  ce "The store is struggling enough as it is so when I saw him stealing..."
                  ju "No need to explain, I totally get it. Granny likes to keep a tight lip about finances but even I can tell she's been struggling to keep things going recently."
                  
          ce "So why bother sticking your neck out for a kid you don't even know?"
          show june normal
          if relationship_June >= 3:  
              show june sad
              ju "When I first moved to this town I didn't know anyone and ran out of the little bit of money I brought along faster than expected."
              ju "Eventually I was down to my last few bucks and practically starving when I saw a Help Wanted sign in the window here. I had no experience and totally bombed the interview, but Granny hired me on to work for her anyway." 
              show june shy
              ju "She saw the potential in me when I couldn't. She even helped me find a room to rent and talked the landlord down to a resonable rate for me."
              show june embarrassed 
              ju "I may just stock boxes for a living, but without this job I'm sure that I'd be out on the streets or worse by now."
              ju "If Granny hadn't went out on a limb and given me a chance I could have easily ended up like Cody, doing whatever necessary to get by because I felt like I had no one in my corner."
          ju "Everyone has been so nice to me since I've moved here. I just really want to show my thanks to and try to be a productive member of the neighborhood."
          show june happy
          ju "That's why we should all work together to make this the best place it can be!"          
          show june grin
          ce "Heh. Spoken like a true boy scout. Don't you think you're being a bit naïve though? I doubt things will get better around here, regardless of what anyone does..."
          show june shy
          ju "Maybe, but it's worth a try in any case."
          ce "You sound just like Granny."
          show june tease 
          ju "What can I say? I had a great teacher!"          
      "Get back to work.":
          "There'll be plenty of time to socialize later but right now I have responsibilities to take care of. Sighing heavily, I brush aside those feeling and pick up where I left off with work."
  #TODO [Afternoon Activity Choice]"
  #play music everyday
  #call lbl_dailyComments   
  #call lbl_dailyActivities from _call_lbl_dailyActivities_2
  call lbl_dailyActivities from _call_lbl_dailyActivities_4
  "End lbl_day_3_afternoon"
  jump  lbl_day_3_evening
    
label lbl_day_3_evening:  
  $CurrentTimeOfDayName = 'evening'
  scene bg storeInside
  show cereza normal  
# 
  #TODO [Evening Activity Choice]"
  call lbl_dailyComments from _call_lbl_dailyComments   
  call lbl_dailyActivities from _call_lbl_dailyActivities_5
  "End lbl_day_3_evening"
  jump lbl_day_3_night
#  
label lbl_day_3_night:
  $CurrentTimeOfDayName = 'night'  
  show bg storeInside
  show june normal at right
  show cereza normal  
  show kameron normal at left
  "That's the end of the Demo! Please be sure to come back and play the final version once it's released!"
  "End Game!"

