init:
  # The script of the game goes in this file.

  # Declare characters used by this game. The color argument colorizes the
  # name of the character.
  default mom_name = "One"
  default name = "Two"
  
  default flag_refuse = False
  default flag_understand = False
  default flag_kick = False

  define bat = Character("Quinn")
  define mom = Character("mom_name", dynamic=True)
  define dad = Character("dad_name", dynamic=True)
  define friend = Character("Friend")


# The game starts here.

label start:

#No child of mine.
  $mom_name = "One"
  $dad_name = "Two"
  
  show bat determined
  bat "Ok, today's the day."
  bat "This is where we break the news to mom and dad."
  show bat1 nervous
  mom "I mean does it have to be today?"
  show bat2 nervous
  dad "They've got a point, we have that paper due, and there's that thing after school and..."
  show bat angry
  bat "Ok, stop."
  show bat determined
  bat "We've put this off for long enough"
  mom "Yeah, but"
  bat "No buts. If we put it off any longer it just won't happen."
  bat "There will always be another paper or after-school thing."
  bat "There are always more excuses. Always."
  bat "No amount of waiting for the perfect moment will make it happen."
  bat "So today is the day."

  bat "Today I tell my parents that I want to be a witch,"
  bat "And not a vampire, like they just assumed I would be my whole life."

  show bat conflicted
  bat "I mean at one point I thought the same, you're a bat, be a vampire when you grow up, it just makes sense."
  bat "The assumption that decided the path my entire life would take from the moment I was born."
  bat "But who decided that? My parents? The world?"

  bat "Be a vampire, have little vampires of your own, and continue the legacy."
  bat "Do I even want little vampires? Is legacy even that important anymore?"

  bat "Stick with tradition. Like your parents and their parents. \"If it ain't broken...\""
  bat "What if it is broken? Would I even know if I didn't question it? Would they?"

  show bat excited
  bat "But imagine how it could be."
  bat "Cute gowns, those adorable hats. And learning all those spells and magic."
  show bat neutral
  bat "I mean sure as a vampire you have 'magic' but it's a specific kind of magic."
  bat "It only really makes sense for certain types of people, and that's just not me."
  show bat conflicted
  bat "I don't think it's ever been me."
  bat "But before I didn't think I had a choice. I just had to be the way that worked with the magic."
  bat "After all, you don't just get magic, you work for it, so the struggle was easy to justify."
  bat "That's just how things are, not much to be done about it."

  bat "And for a long time, I think I had just accepted that and tried my best to make it work."
  bat "but all it took was one word from a close friend to shatter the whole idea."
  bat "I talked about how I had to become a vampire and they simply responded."
  bat "Why?"
  
  show bat confused
  bat "Why do you need to fit that particular mold?"
  bat "Why do you have to accept that things are the way they are?"
  bat "Why can you not choose another path for yourself?"

  show bat conflicted
  bat "And I didn't have an answer."
  bat "I mean initially, I had a lot of answers, but every answer just invited more questions until I had nothing left."
  bat "No answer."
  bat "No response."

  bat "I'd never even considered what it meant to question any of it. It was how it was and that was the end of it."

  show bat confused
  bat "But now all I had were questions. Was this life what I really wanted?"
  bat "Did I really have other options? "
  bat "Would people accept me for choosing something else?"
  bat "Would my parents accept me?"
  bat "Would I?"

  show bat neutral
  bat "And so I did as I always did, a retreated into books."
  bat "Stories. Research."
  bat "I tried to find out why things were."
  bat "How things could be different."
  bat "What it meant to choose something else."

  bat "And the only thing I managed to find out was that things really were only the way they were because they were. "
  bat "There didn't seem to be a solid reason, beyond tradition. We do this because it has always been this way."
  bat "And things could be different, I wouldn't be the first bat to walk a different path. Even way back, there have always been a few who broke off from the group."
  bat "And I found out that it might not be easy. Bats who are different aren't always accepted, they tended to get shunned or ostracized in the past. Of course, these days, as this sort of thing becomes more common it's not quite the same. "
  bat "But still. "
  bat "Thinking that it could be a possibility, that something like that could happen to me, just sends me spiraling into an anxious pit."

  bat "And you might be thinking, \"Welp. what kind of hard ass vampire parents does this kid have, to be this worried.\""

  bat "And they're really not. I love my parents, and I have no doubt that they love me."
  bat "They have loved and supported me in everything I've done my whole life, and there's no reason to think that this would be any different."

  bat "Except for that one line."

  bat "\"No child of mine\"."

  bat "Never said directly of course, always in passing. "
  bat "A seemingly innocuous comment while reading the paper."
  bat "Offhand remark while passing a stranger in the street."
  bat "An off-color joke at a dinner party."

  bat "And of course, at the time I thought nothing of it. But now, when there's a very real chance this could affect me, it's hard to ignore. "
  bat "So I poured over my memories of old conversations, is this how they really feel? Were the comments really offhand, or a scathing reflection of their inner selves?"
  bat "Would this be directed at me? "
  bat "Would they directly say it to me? Or just think that way about me behind my back?"

  mom "..."

  dad "...And?"

  bat "And I honestly don't know, I still think my parents will love me no matter what, but that unknown is eating away at me."
  bat "This is why it has to be today. I need to pull off this band-aid and take my chances."

  bat "Though the best time to do it will be just before dinner, it's the one time everyone is together so that makes it the ideal scenario to make the announcement."

  bat "Which gives us an hour or so to run some scenarios."
  mom "I don't remember agreeing to this."
  bat "Well as figments of my imagination you don't get a choice."
  dad "Touche."

  bat "Ok, so number 1 you will be Mom, and number 2 will be Dad. I'll be myself, obviously."  
  $mom_name = "\"Mom\""
  $dad_name = "\"Dad\""
  
  dad "Obviously."

  mom "Ok so which scenario should we run first."

#-----------------------------------------------------------
label lbl_options:
  menu:
    "They refuse to hear you." if not flag_refuse:
      $flag_refuse = True
      jump lbl_refuse
    "They don't understand." if not flag_understand:
      $flag_understand = True
      jump lbl_understand
    "They kick you out." if not flag_kick:
      $flag_kick = True
      jump lbl_kick
      
    #(after other options are chosen)"
    "It all goes well" if flag_refuse and flag_understand and flag_kick:
      jump lbl_good

#-----------------------------------------------------------
#"They refuse to hear you."
label lbl_refuse:
  bat "Hey Mom, dad. Can we talk for a second?"
  mom "Ok, but can you make it quick? I'm about to start making dinner."
  dad "hmm?"

  bat "Well you see, I've been thinking."
  mom "Oh, that reminds me, I got those pamphlets I was talking about for you."
  bat "Mom, can you please listen, this is important."
  mom "No, it's ok dear, keep going, I'm listening. "
  #Rummages about in the bag
  mom "I know they were in here somewhere."
  bat "Like I was saying, I've been thinking about my future."
  mom "Yes yes, that's what I'm talking about. Ah here!"
  mom "Pamphlets for the top Vampire universities."
  mom "Honestly, any of these ones would be fine, they're all top schools."
  bat "Mom, please."
  mom "But of course, if you wanted to pick one closer to home I wouldn't mind at all."
  dad "Mhmm."
  bat "I'm saying I don't."
  mom "Oh look at this one, they even have a pretty good setup for the more sporty types."
  bat "Mom!"
  mom "Of course, you never really were into sports, that's ok, don't worry about it."
  bat "What I'm trying to say is..."
  mom "Oh but look at the library here, it's huge. I know how much you love to read."
  bat "MOM STOP!"
  mom "I'm sorry?!"
  bat "Please put the pamphlets away and listen to me."
  mom "I'm just trying to-"
  dad "Honey."
  mom "..."
  mom "Ok ok ok, you have my undying attention."

  bat "Mom, dad. I don't want to become a vampire."
  dad "!"
  mom "What?!"
  bat "I want to be a witch."
  bat "I want to go to witch school, I want to learn spells, I want to-"
  mom "Oh is that all."
  bat "Is that all?"
  mom "Don't worry about that."
  mom "It's just a phase."

  bat "A Phase?!"

  mom "It's okay, everyone goes through stuff like this. "
  mom "You're at a turning point in your life and you don't know when you're going to be able to explore this side again."

  bat "Mom! It is not a phase. I've thought long and hard about this for a long time. This is definitely what I want."
  mom "Sure thing dear. You just take a year out to go discover yourself or whatever, and I'll keep these for when you are ready to get back to reality."
  bat "Wha-"
  bat "Dad?"
  dad "*shrugs*"
  mom "Anyways I better get to cooking. Good talk kiddo."


  bat "-and cut-"

  mom "So did that help at all?"
  dad "Do you think we managed to encapsulate your parents' personalities?"

  bat "Well I dunno about all that, but I did not like that interaction at all."
  bat "Completely dismissed and treated like a child."

  bat "I'm practically an adult!"
  bat "And I mean taking some time to make sure I know what I want to do is not the worst idea in the world."
  bat "but the way she put it like it was the whims of a silly child, that stung."

  bat "Maybe I'll use the time to decide what kind of witch I want to be!!!"
  bat "I'm not just going to come crawling back once it's 'out of my system'!"

  mom "Ok ok, let's not get too riled up. It was only an imaginary scenario, we don't know that that's what will happen."
  bat "You're right you're right. Give me a moment to calm myself and we can try a different outcome."

  jump lbl_options


#-----------------------------------------------------------
#"They don't understand."
  
label lbl_understand:
  bat "Hey Mom, dad. Can we talk for a second?"
  mom "Sure, what is it dear?"
  dad "Hmm?"

  bat "Well you see, I've been thinking."
  bat "I'm not sure the life of a vampire really suits me. "
  mom "What do you mean?"
  dad "?"
  bat "I want to be a witch instead."
  mom "What does that even mean? "
  bat "Exactly what it sounds like, I don't want to be a vampire."
  mom "How are you supposed to have your own vampire family if you're a witch?"
  bat "Maybe I won't?"
  mom "You won't have a family?"
  bat "Does a family need to be vampires to be a family?"
  mom "You know that we are both vampires right?"
  mom "And our parents were vampires,"
  mom "And their parents?"
  bat "And because everyone before me was the same I should be the same too?"
  mom "That's not what I'm saying."
  bat "Then what are you saying, Mom?"
  mom "I just don't understand, what's wrong with being a vampire."
  bat "There's nothing wrong with being a vampire. It's just not me."
  bat "It's not who I am, it's not who I'm meant to be."

  mom "I have no idea what's going on with you right now."
  bat "I'm trying to explain I-"
  mom "I have things I need to do, and I can't deal with this right now."
  bat "D-Dad?"
  dad "Sorry, kiddo."


  bat "-and cut-"

  bat "Yikes. Do you really think it'll be that hard to get through to them?"
  mom "I dunno, I just go where the improv script takes me."
  dad "If its improv, then there is no script."
  mom "But you get what I'm saying, right?"
  
  bat "Anyways, lets try another one."

  jump lbl_options


#-----------------------------------------------------------
  #"They kick you out."
label lbl_kick:
  
  bat "Hey Mom, dad. Can we talk for a second?"

  mom "Sure, what's up?"
  dad "Hmm?"

  bat "Ok, I'm just going to rip off the band-aid and come out with it!"
  bat "I want to be a witch!"
  dad "!!!"
  mom "I'm sorry, what?"

  bat "I don't want to be a vampire when I grow up."

  mom "And what exactly has brought this on so suddenly?"

  bat "It's not sudden, I've been thinking about it for a long time, and being a vampire just isn't me."
  bat "I want to be something different. I want to be a witch."
  mom "Do you have ANY idea what you are saying?"
  mom "You can't just decide to be a witch, you were born a bat and you should stick to tradition and become a vampire, like your father and I."
  bat "But mom I-"
  mom "Don't 'but mom' me. "
  mom "You are a child, you obviously don't understand how the world works."
  mom "I don't know where you get all these fanciful ideas. I think you need to choose better people to hang around with."
  bat "What have my friends got to do with this?"
  mom "I'm sure one of those guys have put this crazy idea in your head."
  bat "Is it really that crazy an idea?"
  dad "Dear, I'm with your mom on this one. "
  dad "Deciding to become a witch all of a sudden is just too much."
  dad "You still have your whole life ahead of you."
  mom "Exactly, no need to throw that all away on some pipe dream."
  bat "B-But I-"
  mom "I am going to do all a favor and forget this conversation ever happened."
  bat "Wha-"
  mom "Go to your room, and I will call you when dinner is ready."
  bat "I just-"
  mom "Go. To. Your. Room."
  bat "..."
  dad "..."
  bat "..."
  bat "No."
  mom "What was that?"
  bat "I said no."
  mom "If you don't go to your room right now you will be in big trouble."
  bat "I'M NOT DONE TALKING ABOUT THIS!"

  mom "Well, I AM!"
  bat "Dad?!"
  dad "Come on now dear, tensions are a little high so why don't you go to your room and we can revisit this at another time."

  bat "Why won't you talk to me about this?!"
  mom "I won't have this conversation with you."
  mom "It's pretty obvious from the attitude you are giving me right now that all this is just from a lack of discipline."

  bat "Why can't we just have a conversation about this before you jump to conclusions?"

  mom "We won't be talking about this anymore. I don't want to hear another word from you."

  mom "My house, my rules."

  bat "Are you being serious?"

  mom "Ok, let me put this clearly so my stance is clear."

  mom "No child of mine is EVER going to be a Witch."

  bat "W-What are you trying to say?"

  mom "I think it's pretty clear, if you don't like it then you don't have to stay here."
  mom "You can be a witch or a unicorn or whatever you like somewhere else."

  dad "Honey, I don't think-"

  mom "No stop."

  mom "This is your chance to choose what's more important to you."
  mom "Your family, who raised you all these years."
  mom "Or whatever the hell this is?"

  mom "Just know that you won't be welcome here anymore if you decide to follow that path."

  bat "I..."

  bat "-and cut-"

  bat "..."
  bat "Wow, that was devastating."
  bat "Even though I was just imagining that conversation, it cut so much deeper than I expected it to."

  dad "Maybe we should take a few minutes to settle ourselves before continuing."
  mom "I think that would be wise."

  bat "..."


  jump lbl_options

#-----------------------------------------------------------
#"It all goes well" #(after other options are chosen)

label lbl_good:
  bat "Hey Mom, dad. Can we talk for a second?"
  mom "Sure thing dear."

  bat "I want to become a witch!"
  mom "Wow, that's amazing!"
  dad "And I want to become a Vegetarian!"
  bat "Dad?!"
  dad "I'm swapping blood for broccoli!"
  dad "Cartilage for cauliflower!"
  dad "Flesh for er... fruit?"

  bat "Ok, what are you doing?"
  dad "Sorry, I just didn't get many lines."
  mom "Dad doesn't talk much."

  menu:
    "Ok, but seriously.":
      pass

  bat "Hey Mom, dad. Can we talk for a second?"
  mom "Sure thing dear."
  dad "M-hmm?"

  bat "So I've been thinking about it a lot lately and there's something I want to talk to you guys about."
  mom "What is it?"
  bat "I just want you guys to keep an open mind about what I'm going to say."
  dad "What's all this about?"
  mom "Just come out with it already."

  bat "I want to be ...a witch."

  mom "I'm sorry, you want to be a what?"

  bat "It's just that I've never really felt like the vampire life was for me."
  bat "Like I'm a bat sure, but does that really mean I have to become a vampire?"
  bat "Is that really all I have to look forward to?"
  bat "Do I have to, just because that's what everyone else did before?"

  dad "Slow down kiddo."

  mom "Look, do you even know what it takes to be a witch?"
  bat "I've been doing some research..."
  mom "Do you know where you will go to school?"
  bat "I just..."
  mom "Do you know what sorts of magic you want to learn?"
  bat "I..."
  mom "How much it will cost? What you will do after becoming a witch?"
  bat "..."
  bat "{size=20}I don't know{/size}"
  mom "What?"
  bat "I don't..."
  bat "I don't KNOW EVERYTHING YET!"
  bat "I JUST WANT TO BE ABLE TO CHOOSE THAT LIFE IF I THINK IT FITS ME BETTER!"

  dad "..."
  mom "Why are you crying, dear?"

  bat "I just wanted you guys to accept me and this path I want to walk."
  dad "Look dear. What your mother is trying to say is that she's worried about you."
  dad "We're not saying you shouldn't just-"

  mom "I'm sorry, I didn't mean to bombard you with questions. So I just have one important one."
  mom "Have you really thought this through?"
  bat "Yes, I have!"

  mom "Then we will trust you."
  mom "You've always been a smart and independent little bat, so there's no reason to believe that won't continue, no matter what life you decide to follow."

  mom "But most of all. We will always love and support you."
  dad "No matter what."

  bat "Mom!"
  bat "Dad!"

  bat "-and cut-"

  dad "And much hugging ensues!"

  mom "So how are you feeling after that one?"
  bat "I feel a lot better. "

  bat "I'm still nervous about having this conversation if I'm being honest."
  bat "But I think I'm ready to do it now."

  mom "Well, good luck!"
  dad "We're rooting for you!"

#-----------------------------------------------------------

  bat "Hey Mom, dad. Can we talk for a second?"

  #-fade to black-


#-----------------------------------------------------------
#epilogue

  bat "And that's how the warm-up to the conversation with my parents went."

  friend "Wow, you weren't kidding about the overthinking."

  friend "So..."
  bat "So?"
  friend "How did it go?"

  bat "Oh right, well I'm here now, aren't I?"

#-CG showing a photo of the bat and their parents on the first day of 'witch school'

  bat "It went well. "
  bat "Maybe not quite as perfectly as the 'Good' conversation I had in mind, but pretty good all things considered."

  bat "We did have to have a long conversation after that though about off-hand remarks and the effects they have, even on people they aren't directed at."



  "Fin."
  
  return