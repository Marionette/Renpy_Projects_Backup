# The script of the game goes in this file.


# The game starts here.

label start:

    jump lbl_story_part_1

    #call minigame_start() from minigametime
    #"Done with minigames"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label lbl_story_part_1:

  play music BACKGROUND fadein 2.0

  show  bg bedroom
  with slow_dissolve

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  "Sprawled out on the floor of your sister's bedroom, you doodle in your sketchbook. "

  "Maybe, just maybe, you should do tomorrow's homework. "

  "Or maybe you should tidy up your own bedroom, which looks like it's been hit by Super Typhoon Yolanda. "

  "But those are problems for tomorrow's Cris. "

  "Today's Cris just wants to draw. "

  "In your sketchbook, you draw anything that crosses your mind. "

  hide CRIS

  hide  bg bedroom

  show  cg doodle1
  with slow_dissolve

  "You draw your friends, faces sweaty from dodgeball in the school gym. "

  hide  cg doodle1

  show  cg doodle2
  with slow_dissolve

  "You draw Mom, telephone cord wrapped around her wrist as she chats long-distance with Dad. "

  hide  cg doodle2

  show  cg doodle3
  with slow_dissolve

  "You draw the fancy chocolate cake in the fridge. Sixteen pink candles. "

  "For your after-school snack, you ate a big fat slice. "

  hide  cg doodle3

  show  bg bedroom
  with slow_dissolve

  show CRIS ANGRY: #as side image
    xalign 0.05
    yalign 1.0

  "You don't get it. Why do people call it devil's food cake? "

  "Is there anything in the world closer to heaven than chocolate cake? "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  "Now here you are, lying tummy-down on the floor of your sister's bedroom. "

  "Your belly feels bloated. Too much cake, maybe? "

  "As you're wriggling to a comfier position, you hear an outburst coming from the living room. "

  stop music fadeout 1.0

  ate "He did what?! Mom, why didn't you stop him?! "

  "It's your sister's voice. Sounds like she's come home from volleyball practice. "

  "Mom responds, but her voice isn't shouty like Ate Yasmin's, so you can't hear what she's saying. "

  "Then Ate Yasmin's talking again, voice louder and angrier than ever. "

  ate "But that was {i}my{/i} cake! I saved {i}my{/i} allowance! I bought it for Annika's birthday party! "

  play music TENSION fadein 2.0

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  "Oh no! "

  "Your tummy, already bloated, knots up as the truth about the cake sinks in. "

  ate "I told Cris about that cake, I'm sure I did! "

  ate "Now he's ruined everything! I'm gonna kill that little brat! "

  "You hear stomping noises. Getting closer and closer. "

  "Ate Yasmin's heading to this room! "

  "Clutching your sketchbook to your chest, you dart inside her closet, just in time. "

  hide CRIS

  hide  bg bedroom

  show  bg black
  with slow_dissolve

  "You're hiding inside your sister's closet. "

  "You hear the bedroom door swing open. "

  ate "Not here? He's always here. "

  ate "He's always invading my personal space, wasting my time. What a brat! "

  "You then hear Mom's voice. Mom must have followed her in. "

  mom "Now, Yasmin, no need to call him names. Cris is only twelve. "

  mom "He's just a kid. Of course he acts before he thinks. "

  mom "But you? You're sixteen. "

  mom "You're his big sister. You need to be the better person here. "

  mom "If you need me to buy another cake, just say it. I can buy one before Annika's party. "

  ate "God, Mom. That's not the point. You don't understand. "

  mom "So help me understand. "

  mom "Remember when you were a sweet little girl? What happened to that sweet Yasmin? "

  mom "Your Dad and I were so proud of her! "

  "Ate Yasmin doesn't say anything to this. "

  "Instead, there are more stomping sounds. A flurry of footsteps leaving the room. "

  "Then a screen door slamming shut, farther away. "

  stop music fadeout 1.0

  "Sounds like Ate Yasmin has left the house again. "

  "Who knows where she's going? Maybe to Annika's? "

  "At Annika's, she can rant about you to the one person who actually listens. "

  play music HORROR fadein 2.0

  "Suddenly dead tired, your knees buckle. "

  "You sink to the floor of the closet. Your drop is muffled by your sister's clothes. "

  "You know she keeps a flashlight in the pocket of her yellow slicker, back from her {i}Harriet the Spy{/i} phase. "

  "It takes some fumbling to find it, but you do. "

  hide  bg black

  show  cg closet
  with slow_dissolve

  "Maybe you'll just stay here, surrounded by clothes. "

  "It's snug. It feels safe. "

  "The piles of clothing pressing on your skin feel like many tiny hugs. "

  "Wait, that's it! That's what you should do! "

  "You can't take it when Ate Yasmin's mad at you like this. You have to make up with her somehow. "

  "See, when she comes home, she'll change into pajamas first thing. "

  "That will be your chance! "

  "When she opens the closet door, you'll jump out and surprise her! "

  "You'll hug her before she can start calling you a brat again. "

  "It's kinda like a prank. But really, it's your way of saying sorry. "

  "But what if she ignores you? Gives you the silent treatment? "

  "What if she pushes you away when you hug her? "

  "Just imagining this makes you want to cry. "

  stop music fadeout 1.0

  "Quick, better distract yourself from these thoughts! "

  "You don't want Ate Yasmin coming home to your crying face, do you? "

  play music BACKGROUND fadein 2.0

  "With the flashlight, you take a look at the clothes all around you. "

  "Boy, Ate Yasmin sure is a hoarder when it comes to clothes! "

  "Some of this stuff she hasn't used in forever! "

  "Here are her old Halloween costumes, from before she decided she was too old to go trick-or-treating with you. "

  "You dragged her along anyway. You can't be a pirate without your loyal crewmate. "

  "Here are her Christmas sweaters, from before she realized it would never be cold enough in the Philippines. "

  "No sweater weather for her! "

  "See, your sister's tall for sixteen. Tall enough to be a model, even. "

  "But she wastes her height on such baggy clothes! "

  "She says she's too awkward to be a model, but she does use her height for sports. "

  "Here's her spare volleyball varsity uniform. "

  "And there's her basketball varsity uniform. She didn't last long in that team, but she kept the jersey. "

  "Ate Yasmin actually likes basketball way more than volleyball. Even so, she quit the basketball team. "

  "She told you why. Here in her bedroom, in her pajamas with the stripes on them, she told you her secret. "

  "She never told your parents, but she told you. It made you feel special. "

  "Back then, she trusted you with her biggest secret. Why does she hate you so much now? "

  "Just because of a birthday cake? "

  "You're trying to remember if she really told you about the cake. "

  "The birthday party you knew about. She talked about it all the time. "

  "She picked out an outfit a whole month before the party. "

  "In front of the mirror, she twirled around in this blue summer dress. "

  "She asked you, would Annika like this dress? "

  "You could only shrug. Annika was her best friend, not yours. "

  "How would you know what Annika wanted? Wouldn't Ate Yasmin know that better than anyone? "

  "Back then, you were doodling in your sketchbook, as usual. Ignoring the next day's homework, as usual. "

  "You were kinda listening as she babbled to you, but also kinda not. "

  "Maybe she told you then? About her plan to save up for a cake? "

  "You strain your brain, trying to remember. "

  "Great, you're giving yourself a headache as well as a stomachache. "

  "You're so tired. Everything hurts. This day is the worst. "

  "Ate Yasmin could come home any moment now, but you really want a nap. "

  "Maybe if you close your eyes, just for a minute, everything will disappear. "

  "None of this will be real. Ate Yasmin won't hate you. "

  "You'll be her favorite person again, the one she trusts with her secrets. "

  "You close your eyes. "

  stop music fadeout 1.0

  hide  cg closet

  show  bg black
  with slow_dissolve

  "A knocking on the closet door jerks you awake. "

  "Wow, you really fell asleep? You were {i}that{/i} tired? "

  "Wait, why is Ate Yasmin even knocking on her closet? "

  "Never mind. "

  "It's time to make up with her! Time to say sorry with a surprise hug! "

  "Maybe you've lost the element of surprise. But you'll give it a shot anyway. "

  "You throw open the closet door. "

  cris "BOO!!! "

  play music HORROR

  hide  bg black

  show  cg limbokin
  with slow_dissolve

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  "It's not your sister. "

  "It's a bunch of creepy strangers, straight from a horror movie! "

  "They stare down at you with sunken eyes. "

  "You stare back up at them. "

  "You're so scared you can't move a muscle. "

  "Just lost for words. "

  hide CRIS

  hide  cg limbokin

  show  bg purgatory
  with slow_dissolve

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  "Where are you? What is this place? "

  "Where's Ate Yasmin? Her closet is here, so where's her bedroom? "

  "Did someone kidnap you while you were sleeping?! "

  "A girl around your age steps up. "

  show RAFA ANGRY at center

  "She moves to stand beside you. Facing the rest of the strangers, she folds her arms across her chest. "

  "There's this fiery spark in her eyes. "

  girl "Hey! Stop staring at the kid! "

  girl "You're obviously scaring him. Poor thing. "

  girl "Death is traumatizing enough for the newbies without the rest of you making it worse. "

  "Death?! What is she talking about? "

  show RAFA POKERFACE at center

  girl "Look, I'll take care of the new kid. I'll orient him. "

  girl "Just go. Get out of here. Get on with your business. "

  "Upon hearing these words, most of the creepy strangers shamble away. "

  "They remind you of zombies! "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  "A few of the creepy strangers lag behind though. "

  "They're staring. Not at you, but at the closet behind you. "

  hide RAFA

  hide CRIS

  hide  bg purgatory

  show  cg limbokin
  with slow_dissolve

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  stranger "Hey, kid, are those clothes? Why do you have clothes in your coffin? "

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  "Coffin?! You don't understand any of this! "

  "The stragglers are whispering among themselves. "

  "They're all excited about the clothes in your \"coffin.\""

  hide CRIS

  hide  cg limbokin

  show  bg purgatory
  with slow_dissolve

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  show RAFA ANGRY at center

  girl "So what if they're clothes? What's it to you? "

  girl "Even if the kid had a mountain of clothes, the fact remains that they're his clothes, not yours. "

  "With this, the girl finally manages to drive away the last of the creepy strangers. "

  stop music fadeout 1.0

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  "You're alone with her now. "

  show RAFA SMILE at center

  "She turns toward you, a bright smile on her face. "

  "It's a big change from her fiery expression earlier. "

  play music BACKGROUND fadein 2.0

  girl "Hey, new kid! My name's Rafa. What's yours? "

  cris "Cris. Short for Crisanto. "

  rafa "That's a pretty name. "

  cris "Mom said I was named after the chrysanthemum. It's a golden flower. "

  "Wait, why are you even talking about this? "

  "More importantly, what is happening here? What is this place? Who were those people?! "

  "Your mind swirls with questions. "

  show RAFA POKERFACE at center

  rafa "I know you're dying to ask me a million things. The new ones always are. "

  rafa "I know it's difficult to make sense of this, but how about one question to start? "

  cris "Okay, what in the world is going on? "

  rafa "What do you think is going on? "

  "You shrug. You have no clue. "

  rafa "Walk me through the chain of events that led you here. I'm genuinely curious. "

  "So you explain. "

  "You talk about the birthday cake, your after-school snack, your sister's anger. "

  "You talk about hiding in your sister's closet. About sitting alone in the dark, planning your apology. "

  "You talk about how your head and your tummy were killing you. About how you were dying for a nap. "

  show RAFA SAD at center

  rafa "Ah, I see now. "

  cris "See what? "

  rafa "I need to tell you something, and I need you to listen. "

  cris "Is it bad? "

  rafa "It's bad. "

  show CRIS SAD: #as side image
    xalign 0.05
    yalign 1.0

  cris "Am I . . . dead? "

  rafa "In a nutshell, yes. We're in the afterlife now. "

  rafa "You probably died in your sleep. It's been known to happen. "

  cris "This is too much. "

  rafa "It's a lot to take in, I know. "

  "There's a silence as she lets you absorb this. "

  "You're dead. "

  "Not so long ago, you were alive and kicking. Then you took a nap. "

  "And now you're dead. "

  cris "How do I get back home? Can I? "

  "Rafa sighs. "

  rafa "You can't. "

  rafa "I'm sorry, Cris, but you're stuck here with the rest of us. "

  show RAFA POKERFACE at center

  rafa "If it makes you feel any better, everyone here is dead too. "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  cris "You mean those creepy strangers? "

  rafa "Yes. They all died with major regrets, which is why they were sent here in the first place. "

  rafa "In your case, it was most likely the conflict with your sister that sent you here. "

  cris "Do you mean to say that this place is, um, he-- "

  rafa "No, this isn't heaven or hell. We're in purgatory. "

  rafa "Do you know about purgatory? "

  cris "I remember a little bit from Sunday school. "

  rafa "Those people you called \"creepy strangers\"? They're actually called the Limbokin. "

  rafa "You're one of the Limbokin now, meaning you're a resident of purgatory. "

  cris "And you? You're also one of the Limbokin? "

  rafa "Sure, I live here too. "

  "For a small moment, Rafa stares into space. She seems to be thinking. "

  "Then her eyes snap back to yours. "

  show RAFA SAD at center

  rafa "I live here, but the truth is I can't remember how I got here. "

  rafa "I mean, I obviously belong in purgatory. Why else would I have been sent here? "

  rafa "I just can't remember how I died, even though everyone else has a general idea. "

  cris "You have no clue at all? "

  rafa "Well, I don't know how I got them, but. . . . "

  rafa "I have these scars. Big scars. "

  cris "Really? Where? "

  "Rafa looks uncomfortable. She quickly changes the subject. "

  show RAFA POKERFACE at center

  rafa "So anyway, this closet of yours, it's really interesting, huh? "

  cris "Yeah, it's my sister's. "

  "You both look over at the closet. "

  "You're so used to seeing it in Ate Yasmin's room. It looks out of place here. "

  cris "Hey, Rafa, why were those Limbokin hung up on my sister's clothes? "

  rafa "Who wouldn't be? Clothes are a scarcity here in purgatory, you know? "

  rafa "What do you remember about the Limbokin you've met? What were their clothes like? "

  cris "I wasn't looking at their clothes. I was too busy freaking out! "

  rafa "Okay, fair point. "

  rafa "The Limbokin are wearing the outfits they were buried in. "

  rafa "And they've been wearing the same clothes ever since. "

  rafa "You see, here in purgatory, all you have with you are the things close to you the moment you were buried. "

  rafa "So maybe your coffin, maybe some flowers, maybe some soil. Things like that. "

  rafa "The ones whose bodies were never found -- the ones who were never officially buried -- they have it worst. "

  rafa "They get absolutely nothing. "

  rafa "In your case, your sister's closet must have been mistaken for a coffin. "

  rafa "Some sort of glitch in the system, I suppose. "

  show RAFA SMILE at center

  rafa "Lucky mistake! You have a supply of one of the hottest commodities in purgatory. Clothes! "

  rafa "Hey, do you mind if I take a peek? "

  "You shake your head. You step aside so she can open the closet. "

  "She starts looking through Ate Yasmin's clothes, going {i}ooh{/i} and {i}aah{/i} over certain pieces. "

  "Her favorite is the blue summer dress. The same one Ate Yasmin wanted to wear to Annika's party. "

  "With sparkling eyes, Rafa runs her palms over the cotton fabric. "

  show RAFA POKERFACE at center

  "Then something else catches her eye. "

  rafa "What's this? "

  "You look at where she's pointing. "

  "It's your sketchbook, in the closet where you left it. "

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  cris "Oh, I like to draw. I was doodling just before I -- before I hid in the closet. "

  show RAFA SMILE at center

  "Rafa flips through your drawings. "

  "She smiles as she traces your lines with her finger. "

  show RAFA SAD at center

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  "She whispers something, so softly you probably aren't meant to hear it. "

  rafa "So young. What a waste. What a tragedy. "

  show RAFA SMILE at center

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  "Out of nowhere, she snaps your sketchbook shut! "

  "You jerk back in surprise. "

  "Her eyes are shining, all of a sudden. "

  show RAFA LAUGH at center

  rafa "Come on! No time to waste! Let's go! "

  cris "Go where? "

  show RAFA SMILE at center

  rafa "You wanted to make up with your sister, right? That's why you hid in her closet. "

  show CRIS SAD: #as side image
    xalign 0.05
    yalign 1.0

  cris "Yeah, but it's too late now. "

  rafa "We'll see about that. "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  "She gets behind the closet, then starts pushing it. "

  "You just stare. "

  rafa "Come on, Cris. Help me push. "

  rafa "If we leave this behind, the Limbokin will raid it in no time. "

  cris "But where are we going? You didn't answer me. "

  rafa "To the river. There's someone I want you to meet. "

  cris "Who? "

  rafa "He might not have the magic to bring you back to life. No one does. "

  rafa "But I think he has just enough magic to give you what you want. "

  cris "To talk to my sister? "

  rafa "To achieve closure, yes. "

  hide RAFA

  hide CRIS

  hide  bg purgatory

  show  bg riverstyx
  with slow_dissolve

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  show RAFA POKERFACE at center

  "Dragging Ate Yasmin's closet between you both, you and Rafa head toward the river. "

  "The water gives off a faint glow. You're not too far away now. "

  "As you're walking, Rafa tells you about this friend of hers. "

  "She says this man can maybe help you reach out to your sister. "

  "The way Rafa tells it, this man is her savior. "

  rafa "So when I first got to purgatory, I was just as disoriented as you were, right? "

  rafa "Just bursting with questions, and frustrated by the utter lack of answers. "

  rafa "But he guided me through all that chaos. "

  rafa "He went out of his way to help me acclimate to this strange new place. "

  rafa "He took me under his wing. Literally. "

  cris "Literally? "

  rafa "He also helped me assimilate with the Limbokin. Now I'm even closer to them than he is."

  rafa "Well, it's no wonder he has no time to socialize. He's always so busy. "

  hide RAFA

  "You're close to the river now. "

  "There's a man standing right by the edge of the water. "

  show RAFA LAUGH: #at left
    xalign 0.2
    yalign 1.0

  show SAMI POKERFACE: #at right
    xalign 0.8
    yalign 1.0

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  rafa "Hey, Sami! "

  "The man called Sami turns. "

  show RAFA SMILE: #at left
    xalign 0.2
    yalign 1.0

  rafa "Sami, meet my new friend, Cris. "

  rafa "Cris, meet Sami, my oldest friend in purgatory. "

  "Sami looks curiously at you, then at the closet between you and Rafa. "

  sami "Now that's a coffin design I haven't had the pleasure of seeing before. "

  sami "The aesthetic sensibilities of those blasted Earthlings has gone severely downhill, I'm afraid. "

  "But you're barely listening to these words. "

  "Sami has wings! Huge feathery wings, the kind you've only seen on TV! "

  "Sami notices that you're staring, starry-eyed, at his wings. "

  show SAMI SMILE: #at right
    xalign 0.8
    yalign 1.0

  sami "These wings are really something, aren't they? "

  cris "Super cool! Can I get wings too? Where can I get them? "

  sami "Apologies, but these are special wings. Only for special inhabitants of purgatory who perform special roles. "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  show SAMI POKERFACE: #at right
    xalign 0.8
    yalign 1.0

  cris "Why, what's your role? "

  sami "I guard the two boundaries. "

  sami "The line separating purgatory from hell, and the line separating purgatory from the living realm. "

  rafa "Sami alternates between boundaries, flying periodically from one to the other. "

  rafa "Because he only pays attention to one at a time, boundary-crossing shenanigans often happen. "

  rafa "Then he has to scramble to clean up his mess. I've seen it many times. "

  show SAMI SHOCK: #at right
    xalign 0.8
    yalign 1.0

  sami "Rafa! Don't embarrass me when I'm trying to impress my new friend! "

  show RAFA LAUGH: #at left
    xalign 0.2
    yalign 1.0

  "Rafa giggles. "

  rafa "You goof. Anyway, we came to ask a favor. "

  show RAFA SMILE: #at left
    xalign 0.2
    yalign 1.0

  show SAMI SMILE: #at right
    xalign 0.8
    yalign 1.0

  sami "Ah. Yes, of course. "

  sami "Silly me, thinking my precious daughter only wanted to pay her dearest papa a visit. "

  show RAFA POKERFACE: #at left
    xalign 0.2
    yalign 1.0

  rafa "Stop trying to make me laugh. We're being dead serious here, okay? "

  "Sami opens his mouth, but Rafa swiftly interrupts. "

  rafa "No jokes about how we're already dead. I mean it, Sami. "

  show SAMI POKERFACE: #at right
    xalign 0.8
    yalign 1.0

  "Sami groans. "

  sami "Why maintain this surly act if it's a favor you desire? "

  sami "Papa is disappointed in you, dear Rafa. Have I taught you nothing about the subtle art of persuasion? "

  sami "But suit yourself. What do you want from me? "

  rafa "You can set up conversations between Limbokin and Earthlings, right? "

  rafa "Using the magical properties of the river? "

  rafa "I've seen you do it, when you're deporting boundary-crossers to their proper realms. "

  rafa "That's what we need. Just one tiny little conversation, that's all. "

  "Sami directs his next words to you. "

  sami "And what exactly do you intend to accomplish with this conversation? "

  sami "Are you an aspiring young rebel hero, scheming to incite a war between realms? "

  sami "If so, this simply won't do! "

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  cris "No! I just want -- "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  "But Rafa cuts in. "

  rafa "Never mind what we're trying to accomplish. Can you do it? "

  sami "Do you know how many Limbokin would kill to converse with the living if they had the opportunity? "

  sami "All of them, that's how many. At least all the ones whose loved ones are still alive. "

  sami "Does that mean I should go around indiscriminately granting everyone's wishes? That doesn't make sense. "

  show RAFA SAD: #at left
    xalign 0.2
    yalign 1.0

  rafa "Please, Sami? For me? "

  "Rafa turns up the full force of her expressive eyes. "

  "Sami blows out a sigh. "

  sami "Yes, yes, I can do it. However, you'll have to pay a hefty price. "

  show RAFA LAUGH: #at left
    xalign 0.2
    yalign 1.0

  rafa "Anything that exists in purgatory, we can get you. No problem! "

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  show RAFA SMILE: #at left
    xalign 0.2
    yalign 1.0

  "You wouldn't be so sure. But Rafa's confidence is starting to rub off on you. "

  show CRIS LAUGH: #as side image
    xalign 0.05
    yalign 1.0

  cris "That's right! We can get you whatever you want, no matter what! "

  show SAMI SMILE: #at right
    xalign 0.8
    yalign 1.0

  sami "Seven teeth. That's my price. Take it or leave it. "

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  show RAFA SHOCK: #at left
    xalign 0.2
    yalign 1.0

  cris "Teeth? Like . . . animal teeth? False teeth? "

  show RAFA POKERFACE: #at left
    xalign 0.2
    yalign 1.0

  rafa "No, Sami means human teeth. "

  "Sami plucks a necklace from under the collar of his shirt. "

  "There are three teeth, strung on a bit of cord. "

  "Yep. Those are human teeth, all right. "

  "Is that . . . dried blood? Yikes! "

  sami "It's so hard to distinguish oneself from the hordes of dead people nowadays. "

  sami "That's why I'm making myself some jewellery, just to spice up this tedious life. "

  sami "Isn't this a pretty necklace? "

  "{i}Pretty{/i} isn't exactly how you would describe it. "

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  "Even so, you force a smile. You need this guy's help, after all. "

  cris "Very pretty! "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  show RAFA ANGRY: #at left
    xalign 0.2
    yalign 1.0

  rafa "God, Sami. Can't you ask for anything a little less morbid? "

  sami "Oh, my dear girl. Don't you know that beggars can't be choosers? "

  sami "Besides, do the Limbokin even need their teeth at this point? It's not like they need to eat. "

  show SAMI POKERFACE: #at right
    xalign 0.8
    yalign 1.0

  show RAFA POKERFACE: #at left
    xalign 0.2
    yalign 1.0

  sami "By the way, I don't want teeth from either of you. "

  sami "Miniscule baby teeth, warped by excessive sugar intake? No thank you. I prefer mature adult teeth. "

  show CRIS ANGRY: #as side image
    xalign 0.05
    yalign 1.0

  cris "Hey, I already have my permanent teeth! I'm not a baby! "

  "But Sami just ignores this. "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  rafa "Any chance we can still change your mind about this? "

  sami "None whatsoever. "

  sami "You'd better make up your minds. I need to be off soon, to perform my dreary duties at the other boundary. "

  "Rafa looks at you. "

  "You just shrug. What are you supposed to say? "

  "She turns to Sami. "

  rafa "Okay, we'll do it. We'll get you your seven teeth. "

  rafa "If we give you seven teeth, do you promise to arrange one conversation between Limbokin and Earthling? "

  sami "Sure, sure. That's what I said. "

  rafa "No, you need to say it clearly. You need to promise. "

  "Sami sighs, then says his next words with an extremely bored expression. "

  sami "If you give me seven teeth, I promise to arrange one conversation between Limbokin and Earthling. "

  sami "Happy? "

  show RAFA SMILE: #at left
    xalign 0.2
    yalign 1.0

  "Rafa beams at him. "

  rafa "Quite. Run along now. "

  "With a final mocking bow in your direction, Sami takes off running. "

  hide SAMI

  hide RAFA

  "When he gets off the ground, his wings fumble a little, but he manages to steady himself midair. "

  "He flies off beyond the river. "

  "The moment he's gone, you start whining to Rafa. "

  show RAFA POKERFACE at center

  show CRIS SAD: #as side image
    xalign 0.05
    yalign 1.0

  cris "Can we really do this? Teeth, of all possible things! "

  "But Rafa isn't listening. She's staring into the distance, where Sami has just disappeared. "

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  cris "Flying is cool, huh? I bet Sami can get everywhere with those wings. "

  "Rafa starts, seeming to just now remember that she's not alone. "

  rafa "No, not everywhere. Sami can't fly long distances. "

  rafa "He also can't fly too high. He says his wings are too frail. Too weak. "

  rafa "He's been around for millions of years, after all. Or so he says. "

  cris "Wow. "

  rafa "I wonder how old I am. "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  cris "Aren't you, like, twelve? Around my age? "

  show RAFA SAD at center

  rafa "You stop aging in purgatory. "

  rafa "But I can't remember my life before I got here. So I have no idea about my real age. "

  cris "Really, you can't remember your life? "

  rafa "Sometimes, fragments of memories hit me. Maybe a face. Or maybe a voice. "

  rafa "But that's it. I have no idea how any of these fragments connect. "

  show CRIS SAD: #as side image
    xalign 0.05
    yalign 1.0

  "She looks miserable. "

  "Your heart hurts for her. "

  "This afterlife thing may be new to you, but for Rafa, it's ancient history. "

  "Even so, it obviously hasn't gotten any better for her. "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  "You want to do something. Cheer her up. Something. "

  "You open your sister's closet and start rummaging through the clothes. "

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  cris "Here you go, Rafa! "

  "You hold out the blue summer dress toward her. The one both she and your sister loved. "

  show RAFA SHOCK at center

  rafa "What's this for? "

  cris "It's a gift. To cheer you up! "

  rafa "I can't accept this, Cris. It's too much. "

  cris "It's also to thank you for going out of your way to help me. You didn't have to, but you did. "

  "You shove the dress into her arms. "

  "She opens her mouth as if to protest, but she can't help admiring the dress all over again. "

  show RAFA SMILE at center

  rafa "It's beautiful. I'm obsessed with this nostalgic shade of blue. "

  rafa "This is the best thing anyone's ever given me. Thank you. "

  "She's running her palms over the cotton again. "

  "Then a light comes on in her eyes. "

  "Even though you've just met, you already feel like you've known this expression forever. "

  "You can kinda guess what she's going to say next. "

  show RAFA LAUGH at center

  rafa "I have the best idea ever! We have to do it! Let's go! "

  show CRIS LAUGH: #as side image
    xalign 0.05
    yalign 1.0

  cris "Okay, okay. One step at a time. What's this grand idea? "

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  show RAFA SMILE at center

  rafa "I know what to do. I know how you can talk to your sister. "

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  cris "How? Tell me! "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  rafa "Okay, so we can't just ask people for their teeth out of nowhere, right? "

  rafa "Instead, we should give them what they want, in exchange for their teeth. "

  rafa "And what do the Limbokin want more than anything? Clothes! "

  "Beaming, Rafa gestures toward Ate Yasmin's closet. "

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  cris "Wait a minute. Trade my sister's clothes for some crummy old teeth? "

  cris "Are you kidding? I might as well trade my own teeth! "

  show RAFA POKERFACE at center

  rafa "Do you {i}want{/i} to trade your own teeth? "

  cris "No way! "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  rafa "See what I mean? It would take a lot for the Limbokin to give up their beloved chompers. "

  rafa "They value their precious few possessions too much. "

  rafa "One can imagine they'd be even more protective about actual body parts. "

  rafa "However! They're absolutely obsessed with clothes! "

  rafa "I've been stuck with them for God knows how long. Trust me. I know. "

  show CRIS ANGRY: #as side image
    xalign 0.05
    yalign 1.0

  cris "You know that the Limbokin are all a bunch of wannabe fashionistas? Get out of here! "

  rafa "Look, they've been wearing the same outfits for years or decades now. Centuries, even! "

  rafa "Lord knows they want a change. "

  "You're silent for a while, fuming. "

  "Why are you so against this idea? "

  "Back when you were alive, you always teased Ate Yasmin for her fashion sense, didn't you? "

  show CRIS SAD: #as side image
    xalign 0.05
    yalign 1.0

  "But these clothes, they're the only things you have left that connect you to her, and to Earth. "

  rafa "Look, do you want to talk to your sister or not? "

  cris "But what if I fail? Then I gave up her stuff for nothing! "

  rafa "You know this isn't really her stuff, right? All her real clothes are back on Earth. "

  rafa "Think of this stuff as an echo. A shadow. You're just trading shadows. "

  "You're still unsure about this. "

  show RAFA SMILE at center

  rafa "Okay, tell you what. Let's set a limit. "

  rafa "Five items from her closet. That's it. "

  rafa "As long as you're smart about it, that's all you need to give up for those seven teeth. "

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  cris "Just five? Really? "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  rafa "I promise. Once you've traded five items of clothing, I'll end the trading myself. "

  rafa "And that's not all. I guarantee you'll have the power. "

  rafa "You decide which items to trade. You decide if you want to push through or back out. "

  rafa "I won't let them screw you over. "

  show CRIS SAD: #as side image
    xalign 0.05
    yalign 1.0

  "Now you can't help feeling ashamed. "

  "She's just thinking about you. She's doing all she can to help you. "

  "And here you are, being such a wuss about giving away some clothes. "

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  cris "Okay. Let's do it. "

  cris "You're right. What matters is I get to talk to my sister. "

  "Smiling, Rafa bumps your shoulder with her fist. "

  show RAFA LAUGH at center

  rafa "Good! That's the spirit! "

  show RAFA SMILE at center

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  cris "Rafa, why are you so nice to me? "

  rafa "Nice? I'm not nice. Haven't you seen how bossy I can be? "

  rafa "The Limbokin tolerate me, but that's it. I'm no one's favorite person. "

  rafa "But we're friends now, aren't we? And friends look out for each other. "

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  "You grin at her. "

  cris "Yeah. Friends. "

  show RAFA POKERFACE at center

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  rafa "Okay. As your friend, I have to ask you something. "

  rafa "You say you want to make up with your sister. But do you even get what you're apologizing for? "

  cris "I told you. I ate a slice of the cake reserved for her best friend's birthday party. "

  rafa "And your sister was angry? "

  cris "Angrier than I've ever known her to be. "

  rafa "Oh, Cris. No one gets that angry over a cake. There must have been an underlying reason. "

  rafa "Now I need to go prepare some things before we can begin our grand trading scheme, so just sit tight. "

  rafa "Use this time to think about it, okay? Think about what you'll say to your sister. "

  rafa "Before apologizing, you need to understand why you're apologizing in the first place. "

  hide RAFA

  "Once Rafa leaves you, you take out your sketchbook. You start to doodle. "

  "Drawing helps you figure things out. "

  "What did Rafa mean? Isn't it obvious why you want to apologize to your sister? "

  "Ate Yasmin bought a cake. You ate that cake. "

  "It was her cake, not yours. You shouldn't have touched it. End of story. "

  "You're still doodling, but you stop when you see what you've drawn. "

  stop music fadeout 1.0

  hide CRIS

  hide  bg riverstyx

  show  cg doodle4
  with slow_dissolve

  "A girl in stripy pajamas. "

  "That takes you back. The striped pajamas. Ate Yasmin's bedroom. "

  "That day, maybe a year ago now, she told you a secret. "

  hide  cg doodle4

  play music THEMESONG fadein 2.0

  show  bg bedroom
  with slow_dissolve

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  show ATE YASMIN POKERFACE at center

  ate "Don't tell Mom yet, but I had to quit the basketball team. "

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  cris "Huh? Why? Didn't you tell me you wanted to be like Jaworski? "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  ate "It sucks, I know. I love the game, but my teammates were pissing me off. "

  cris "Why, what did they do? "

  ate "See, there's this girl named Annika on the team. We're both new. "

  ate "For some reason, the team liked me right away, but totally ignored Annika. "

  ate "I mean, they never pass her the ball or anything, even though she's not a bad player. "

  show ATE YASMIN ANGRY at center

  ate "I always thought that was weird, but when I found out the real reason, my blood really boiled. "

  cris "What was the reason? "

  ate "They told me, \"Annika's a lesbo and has this big pervy crush on you!\" They told me I should stay away. "

  ate "So of course I told them they were bullies and they should stay away from me. "

  show ATE YASMIN POKERFACE at center

  ate "Things got sour after that. It was hard to stay. "

  cris "Wow. That does suck. "

  ate "But you know what really, really sucks? "

  ate "The name they were calling Annika, as some big insult? I kinda feel like -- "

  ate "Cris, can you keep a secret? "

  cris "Yeah, I can. "

  ate "I mean, I'll probably talk to Mom and Dad about this at some point. But for now. . . . "

  cris "I won't tell them. I promise. "

  ate "You know the word \"lesbian\"? I kinda feel like it applies to me. "

  ate "So when they were picking on Annika, it felt like they were picking on me too. "

  show ATE YASMIN ANGRY at center

  ate "And I just couldn't stand it. "

  ate "Yeah, I think girls are pretty. Sometimes I want to hold a pretty girl's hand. "

  ate "Is that so wrong? Should I be ashamed of it? "

  show ATE YASMIN POKERFACE at center

  cris "It's not wrong. No way. "

  ate "You won't hate me if I, like, got a girlfriend? "

  cris "Why would I hate you? "

  cris "That's like if you hated me for hating math or something! It's just a preference! "

  show ATE YASMIN SMILE at center

  ate "Is this your way of telling me to finish your math homework for you? "

  show CRIS LAUGH: #as side image
    xalign 0.05
    yalign 1.0

  cris "I never said that. But now that you've brought it up. . . . "

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  "Ate Yasmin shakes her head, but she's smiling. "

  ate "You don't have to love math, but you have to do your own homework, you know. "

  cris "Who cares about homework? Does this mean you'll make that Annika girl your girlfriend? "

  show ATE YASMIN POKERFACE at center

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  ate "That's not how it works. "

  ate "I mean, I don't even know if Annika's a lesbian. Or if she really likes me. "

  ate "That could be a rumor they cooked up just to be mean. I wouldn't put it past them. "

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  cris "But maybe you can ask Annika about it? Won't it be nice to have a friend like you? "

  show ATE YASMIN SMILE at center

  ate "Yeah, that would be nice. "

  hide ATE

  hide CRIS

  hide  bg bedroom

  show  bg riverstyx
  with slow_dissolve

  show CRIS SAD: #as side image
    xalign 0.05
    yalign 1.0

  "How is Ate Yasmin doing now? "

  "You already miss her, even though it hasn't been long since you last saw her. "

  "You picture her opening her closet. Surely, she's the first to find your body there. "

  "Maybe she tries to shake you awake. "

  "Maybe she's still angry and yells at you to get out of her room. "

  "Either way, she'll notice that your body's limp. And you're not breathing. "

  "Maybe she screams. "

  "Maybe she's shocked into silence. "

  "Maybe you've scarred her forever by dying inside her closet, of all possible places to die. "

  "Is this what you need to say sorry for? It's not like you chose to die there. "

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  "With a pang, you suddenly realize something. "

  "Because of the timing of your death, this means Ate Yasmin can't go to Annika's birthday party. "

  "And given how close the two of them are, will Annika push through with the party at all? "

  show CRIS SAD: #as side image
    xalign 0.05
    yalign 1.0

  "Maybe it's just a birthday party, but to Ate Yasmin it's more than that. "

  "It was a big deal to her. She wanted everything about that party to be perfect. "

  stop music fadeout 1.0

  "And now you've ruined it. Maybe you didn't mean to, but you ruined it anyway. "

  "First, by eating the birthday cake. "

  "Second, by dying. "

  hide CRIS

  hide  bg riverstyx

  play music BACKGROUND fadein 2.0

  show  bg purgatory
  with slow_dissolve

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  show RAFA SMILE at center

  "Rafa has now wrapped up preparations. "

  "She's picked out a quieter side of purgatory for the trading. "

  "Seven Limbokin are standing in front of you both. "

  "Rafa has decided to limit the trading to just these seven, so that it won't get too messy. "

  rafa "Hello, everyone! Congrats on winning our fun little lottery! "

  rafa "Thanks to your luck in drawing those lots, you may walk away with some brand spanking new clothes! "

  "The Limbokin clap and cheer. "

  "One of the Limbokin raises his hand. "

  limbokin "I've got a question. Who gets first dibs? Because I'd happily die again for a -- "

  show RAFA POKERFACE at center

  "Rafa interrupts him. "

  rafa "Who picked Lot No. 1? "

  "Someone else raises her hand. "

  rafa "We shall proceed in an orderly fashion, from Lot No. 1 to Lot No. 7. "

  "The Limbokin who just spoke looks stricken. Clearly, he picked Lot No. 7. "

  show RAFA SMILE at center

  rafa "So here's how this works. First, you talk a little bit to my friend Cris over here. "

  rafa "Cris is new to purgatory, so be nice. "

  rafa "He'll ask you a question, and based on your answer, he'll figure out what you're all about. "

  rafa "He'll think about what type of clothes you might like. Then he'll choose an item to offer you. "

  limbokin "What?! You mean we can't even choose? "

  show RAFA ANGRY at center

  rafa "No point arguing with me about this. It's a done deal. Take it or leave it. "

  show RAFA POKERFACE at center

  rafa "It's not like you have no choice. You decide how many teeth you want to trade for the item Cris offers you. "

  rafa "If you don't want to trade at all, then don't. Just walk away. "

  "The Limbokin begin talking among themselves. "

  show RAFA SMILE at center

  "Ignoring the dirty expressions some of them are shooting her way, Rafa grins at you. "

  rafa "You okay, Cris? "

  cris "Yeah, just a little nervous, I guess. "

  rafa "Remember, you just need seven teeth. This will be a piece of cake! "

  show CRIS SAD: #as side image
    xalign 0.05
    yalign 1.0

  "You wince at her word choice. "

  show RAFA SHOCK at center

  rafa "Sorry! I meant to say, this will be easy. "

  show RAFA SMILE at center

  rafa "Also remember what I told you earlier. "

  rafa "You only have to trade five items of clothing at most. I'll make sure of that. "

  rafa "So don't worry. No big deal, right? "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  cris "I guess. "

  show RAFA POKERFACE at center

  "Rafa glances at the sketchbook in your arms. "

  "You like to hold it close to your chest when something is stressing you out. "

  rafa "Hey, why don't you record the proceedings by drawing them? "

  rafa "Time moves differently in purgatory. Down here, your memories go so fast. "

  rafa "If you draw what happens, then you won't forget. "

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  cris "Okay, I'll draw. "

  "You open your sketchbook and position a marker over it. "

  show RAFA SMILE at center

  rafa "Ready to start? "

  "Ready or not, you have to do this. "

  cris "I'm ready. "

  hide RAFA

  hide CRIS

  hide  bg purgatory
  
  jump lbl_minigame_start

######### MINIGAME #############
label lbl_minigame_start:
    #menu:
    #    "Ready to start the minigame?"
    #    "Yes!":
    #       pass
    call minigame_start() from minigametime
    
    #"[END MINIGAME
    jump lbl_story_part_36

######### MINIGAME #############


                               

label lbl_story_part_36:


  hide  cg limbokin

  stop music fadeout 1.0

  show  bg purgatory
  with slow_dissolve

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  show RAFA SMILE at center

  rafa "Okay, that's enough trading. We're done here, everyone. "

  rafa "Thanks for coming! Nice doing business with you all! "

  "One of the Limbokin tries to protest, but Rafa isn't having it. "

  show RAFA ANGRY at center

  rafa "I said it's over! End of discussion! "

  rafa "Go on! Scram! "

  play music BACKGROUND fadein 2.0

  "With this, the Limbokin lumber away, talking to each other about clothes. "

  show RAFA POKERFACE at center

  "Once you're alone, Rafa turns to you. "

  rafa "I was busy keeping the Limbokin in line. You know, to make sure they wouldn't start a riot or something. "

  rafa "So I couldn't really pay attention to the trading itself. How did it go? "

  "You spread your palm open. "
  
  if minigame_teeth == 0:
    cris "I didn't get any teeth. "
  else:
    $teethcount = NumberStringList[minigame_teeth]
    cris "I got [teethcount] teeth."

  #TODO {IF X=0} CRIS: I didn't get any teeth. "
  #TODO {IF X=1} CRIS: I got one tooth. "
  #TODO {IF X=2} CRIS: I got two teeth. "
  #TODO {IF X=3} CRIS: I got three teeth. "
  #TODO {IF X=4} CRIS: I got four teeth. "
  #TODO {IF X=5} CRIS: I got five teeth. "
  #TODO {IF X=6} CRIS: I got six teeth. "
  #TODO {IF X=7} CRIS: I got seven teeth. "
  #TODO {IF X=8} CRIS: I got eight teeth. "
  #TODO {IF X=9} CRIS: I got nine teeth. "
  #TODO {IF X=10} CRIS: I got ten teeth. "

  #TODO {IF X<7: GO TO PART 37} "

  #TODO {IF X=7: GO TO PART 38} "

  #TODO {IF X>7: GO TO PART 38} "

  if minigame_teeth < 7:
    jump lbl_story_part_37
  else:
    jump lbl_story_part_38

                               

label lbl_story_part_37:

  show RAFA SHOCK at center

  rafa "What? That's not enough! You need at least seven teeth. "

  show CRIS SAD: #as side image
    xalign 0.05
    yalign 1.0

  cris "Yeah. Guess I just suck at trading. "

  show RAFA SAD at center

  rafa "Sorry, I was too caught up in the logistics of it. "

  rafa "I should have paid more attention to the trading itself. I could have helped. "

  cris "It's not your fault. I made bad choices. "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  show RAFA POKERFACE at center

  rafa "Understandable. You're a kid, not some veteran merchant. "

  cris "Should we arrange another trading session? "

  rafa "I don't think so. I know how much those clothes mean to you. "

  rafa "Maybe it's just not meant to be. "

  rafa "Maybe this proves how important your sister is to you, which is why you can't give up her clothes. "

  show CRIS SAD: #as side image
    xalign 0.05
    yalign 1.0

  cris "She {i}is{/i} important. My favorite person on Earth. Now I won't even get to talk to her. "

  rafa "That's just life. Things don't work out sometimes. "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  cris "Life, huh? "

  rafa "Life. Death. You know what I mean. "

  show CRIS SAD: #as side image
    xalign 0.05
    yalign 1.0

  cris "So what do I do now? Just move on? "

  cris "I never got to say sorry. She'll probably hate me forever and ever. "

  rafa "You don't know that. "

  cris "And I never will. This sucks. "

  rafa "I know it does. But you just learn to live with it, I suppose. "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  cris "Live with it? "

  rafa "Yeah, I confuse life and death a lot. For me, they're not all that different. "

  rafa "In a way, purgatory is just another shot at life, you know? "

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  cris "When you put it that way, this place doesn't sound so bad. "

  show RAFA SMILE at center

  rafa "It really isn't. "

  rafa "And you know one good thing about purgatory? "

  cris "What? "

  rafa "All the Limbokin have been through the exact same thing you're going through right now. "

  rafa "They've all grappled with these same questions. At the very least, you're not alone. "

  cris "Yeah, I won't be alone. That's something. "

  rafa "You're not alone right now. I'm here, aren't I? "

  cris "That's true. You're here. "

  cris "Yeah, I'm feeling a little better now. "

  cris "Maybe moving on is the best thing I can do. For myself. And for my sister. "

  show RAFA LAUGH at center

  rafa "That's the spirit! "

  show RAFA SMILE at center

  rafa "Ready to see what this new world has to offer? "

  cris "Ready. "

  hide RAFA

  hide CRIS

  hide  bg purgatory

  show  cg ending1
  with slow_dissolve

  return

                               

label lbl_story_part_38:

  show RAFA LAUGH at center

  rafa "Great! You did it! "

  show CRIS LAUGH: #as side image
    xalign 0.05
    yalign 1.0

  cris "We did it! "

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  show RAFA SMILE at center

  rafa "Let's go see Sami. "

  rafa "He has to keep his end of the deal. He promised, after all. "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  "But will it really be that easy? Nothing's ever that easy, is it? "

  hide RAFA

  hide CRIS

  hide  bg purgatory

  show  bg riverstyx
  with slow_dissolve

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  show RAFA POKERFACE: #at left
    xalign 0.2
    yalign 1.0

  show SAMI SMILE: #at right
    xalign 0.8
    yalign 1.0

  sami "I said I'd help you, and I fully intend to. "

  sami "I'd be honored to grant you this small favor. "

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  "What?! It's that easy? "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  show SAMI POKERFACE: #at right
    xalign 0.8
    yalign 1.0

  "Sami crouches by the river. "

  "Rafa moves to stand beside him. You follow her. "

  "Mumbling in a strange language, Sami stirs the surface of the water with his hand. "

  "The water, already faintly gleaming, begins to glow even brighter. "

  "You turn to Rafa. "

  hide SAMI

  cris "This is all happening so fast. "

  rafa "This is what you want, right? "

  cris "Yes, but -- "

  rafa "So what's the problem? "

  rafa "This is a big favor. Huge. "

  rafa "There's not a single Limbokin who wouldn't love to be in your place right now, you know? "

  cris "Including you? "

  show RAFA SAD: #at left
    xalign 0.2
    yalign 1.0

  "Rafa pauses, an odd look passing over her eyes. "

  rafa "You know I can't remember anything about my life. "

  show RAFA POKERFACE: #at left
    xalign 0.2
    yalign 1.0

  cris "But you remember some faces and some voices, right? That's what you told me. "

  cris "What if you got to talk to someone you knew when you were alive? Wouldn't that be cool? "

  "Rafa just fidgets, saying nothing. "

  "You don't know why you haven't thought of this before. "

  "You were so busy trying to get what you wanted, you never bothered to ask Rafa what she wanted. "

  "It's all thanks to Rafa that you even got this far. "

  "She linked you up with Sami. "

  "She got the idea to trade Ate Yasmin's clothes for teeth. "

  "She arranged the trading with the Limbokin. "

  "Doesn't she deserve this favor way more than you do? "

  "On the other hand, this is your last chance to speak with your sister. Should you really give this up? "

  menu:
      "Use the favor, or offer the favor? "
      "Use the favor to talk to your sister.":
        jump lbl_story_part_39
      "Offer the favor to Rafa.":
        jump lbl_story_part_40

                               

label lbl_story_part_39:

  "Rafa helped you through this whole thing. She never asked for anything in return. "

  "She's obviously invested in this reunion between you and your sister. "

  "It makes sense to use the favor, as originally planned. "

  "Don't let it go to waste. Rafa would hate that. "

  "The glowy lights in the water are brighter than ever. "

  show SAMI POKERFACE: #at right
    xalign 0.8
    yalign 1.0

  "Still crouching by the river, Sami turns to look at you. "

  sami "Are you ready, Cris? "

  "You nod then step forward. "

  cris "What do I need to do? "

  sami "Kneel. Close your eyes. Picture the Earthling you want to visit. "

  "You kneel, but you keep your eyes open. "

  cris "Will I be transported to Earth? "

  sami "You'll feel like it. And the person you're visiting, they'll think you're there too. "

  sami "But it's simply an illusion. "

  sami "Just a trick of the magical properties of the water. And a bit of my own magic too. "

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  cris "Is this where ghost stories come from? "

  show SAMI SMILE: #at right
    xalign 0.8
    yalign 1.0

  sami "I could tell you, but then I'd have to kill you. "

  "That creepy smile. You shiver. "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  show SAMI POKERFACE: #at right
    xalign 0.8
    yalign 1.0

  "Rafa sighs impatiently. "

  rafa "He's already dead, so what are you going to do about it? "

  rafa "Let's just get on with this, for God's sake. "

  rafa "Cris, close your eyes. "

  "You hesitate, but decide to do as Rafa says. "

  "You close your eyes. "

  hide SAMI

  hide RAFA

  hide CRIS

  hide  bg riverstyx

  stop music fadeout 1.0

  show  bg black
  with slow_dissolve

  "At least Rafa's here. You feel better with her being here. "

  "Slowly, you allow your body to relax. "

  play music TENSION fadein 2.0

  "Suddenly, a hand grabs your hair and dunks your head underwater! "

  "You thrash, but you can't escape. The iron grip holds you down. "

  "No! This is bad! You're going to -- "

  "Then you hear Rafa's voice. She sounds so far away. "

  rafa "Remember, Cris. You don't need to breathe. You're not going to die. "

  "Then you hear Sami's voice. He sounds far away too. "

  sami "You can open your eyes now. "

  "You open your eyes. "

  hide  bg black

  stop music fadeout 1.0

  show  bg bedroom
  with slow_dissolve

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  "You're in your sister's bedroom. "

  "A peaceful late afternoon. "

  "The room is so quiet you can hear the soft ticking of the clock. "

  "You look around the room. "

  "You thought you were alone, so it startles you to see someone there. "

  show ATE YASMIN SHOCK at center

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  "There's Ate Yasmin, backed against the wall! "

  "She's so shocked she's not making a sound. Not breathing. "

  "You hurry toward her. "

  cris "Ate Yasmin? Are you okay? "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  play music THEMESONG fadein 2.0

  "She looks like she can't believe what her eyes are seeing. "

  "She chokes out her words. "

  ate "Cris?! Is it you? Is it really you? "

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  "She reaches out to touch you, but her hand passes through your face! "

  "You're like a ghost! "

  "With a gasp, she yanks back her hand. "

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  cris "It's me, Ate! "

  cris "I'm still dead. But I really wanted to talk to you. "

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  "Looking like she's about to faint, she tips over backward. "

  "She falls on her bed. "

  "You rush forward to help, but of course you can't touch her. You just hover uselessly over her. "

  show CRIS SAD: #as side image
    xalign 0.05
    yalign 1.0

  show ATE YASMIN SAD at center

  "She looks like she's about to burst into tears any moment now. "

  ate "Oh, Cris! I'm so sorry! I can't tell you how sorry I am! "

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  cris "Why are you sorry? I'm the one who's sorry! "

  show CRIS SAD: #as side image
    xalign 0.05
    yalign 1.0

  ate "I said such mean things about you. "

  ate "I knew you were hiding somewhere in my room. You left a mess on the floor. "

  ate "I talked loud enough for you to hear all the cruel things I was saying. "

  ate "I was so angry, so horrible, the worst sister in the world! "

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  cris "Of course you were angry! I ate your cake! "

  show CRIS SAD: #as side image
    xalign 0.05
    yalign 1.0

  cris "The cake had candles and everything. I even counted them. Sixteen. "

  cris "Part of me knew the cake was reserved for a birthday, but the bigger part of me didn't care. "

  cris "I was greedy. Insensitive. I wasn't thinking. "

  ate "Who cares about that cake! "

  cris "I should have known you got that cake for Annika, should have remembered it was her birthday. "

  ate "Who cares about Annika! "

  show CRIS ANGRY: #as side image
    xalign 0.05
    yalign 1.0

  cris "Don't say that! You love Annika, don't you? "

  show CRIS SAD: #as side image
    xalign 0.05
    yalign 1.0

  "Now she really looks like she's going to cry. "

  ate "Oh, Cris. I miss you. I miss you so much. "

  cris "Even though I was a brat? "

  ate "You're not a brat. You weren't perfect, but you were my brother. {i}Are{/i} my brother. "

  ate "I wish you were here. I need you. You're the only one who understands. "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  show ATE YASMIN POKERFACE at center

  cris "About Annika? About how you feel about her? "

  ate "I was going to ask her, you know. At the birthday party. "

  ate "Ask her if she loves me too. And if she wants to be my girlfriend. "

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  cris "You can still ask her those things. "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  ate "You mean now? I've been crying all week. "

  "A week has passed? How long have you been gone? Time does move differently in purgatory. "

  ate "I literally can't do anything else. I'm a wreck. "

  ate "You know the only reason I'm not crying right now? It's because I'm all cried out. "

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  cris "Listen, Ate. I'm sure Annika will understand. "

  cris "I can tell she loves you too, just by the way she looks at you. "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  show ATE YASMIN SHOCK at center

  "Ate Yasmin suddenly leans forward. Her eyes widen. "

  ate "Cris. I -- I think you're fading. "

  show CRIS SAD: #as side image
    xalign 0.05
    yalign 1.0

  cris "Maybe it's time for me to go. I can't stay. "

  ate "But -- "

  cris "I just wanted to say sorry. And goodbye. "

  ate "Cris, please -- "

  cris "Take care of Mom and Dad, okay? And Annika, take care of her too. "

  "You can feel it now. A force is pulling you away from her. "

  show ATE YASMIN SAD at center

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  cris "I love you, Ate. Okay? Your bratty little brother loves you. Don't forget. "

  ate "I won't -- "

  hide ATE

  hide CRIS

  hide  bg bedroom

  stop music fadeout 1.0

  show  bg riverstyx
  with slow_dissolve

  show CRIS SAD: #as side image
    xalign 0.05
    yalign 1.0

  show RAFA POKERFACE: #at left
    xalign 0.2
    yalign 1.0

  show SAMI POKERFACE: #at right
    xalign 0.8
    yalign 1.0

  "Sami has yanked your head up from the water. "

  "You're back by the river, dripping wet to your shoulders. "

  "You're thankful for this. It hides your tears. "

  play music BACKGROUND fadein 2.0

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  "You force a smile. You give Rafa and Sami a thumbs-up. "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  show RAFA SAD: #at left
    xalign 0.2
    yalign 1.0

  "This doesn't fool Rafa though. "

  "Without a word, she crouches beside you. She rubs your back as if to soothe you. "

  show SAMI SMILE: #at right
    xalign 0.8
    yalign 1.0

  sami "Well, that certainly seemed like an intense conversation. "

  sami "You were blowing so many bubbles to the surface, I thought for a moment you'd magically revived from the dead. "

  sami "Who were you talking to? Your childhood sweetheart? "

  sami "Oh, puppy love! So pure, so sacred, so beautiful! "

  show RAFA ANGRY: #at left
    xalign 0.2
    yalign 1.0

  rafa "What happened is none of our business, Sami. We shouldn't pry. "

  show SAMI POKERFACE: #at right
    xalign 0.8
    yalign 1.0

  sami "I am beyond devastated that I will never get to know. "

  "He doesn't look like it, though. He just looks bored. "

  rafa "Isn't it just about time for you to head to the other boundary? "

  show SAMI SMILE: #at right
    xalign 0.8
    yalign 1.0

  sami "Indeed it is. "

  sami "Thank you, dear daughter, for giving me an out. "

  sami "Now I must make myself scarce before this extremely emotional scene suffocates me. "

  hide SAMI

  rafa "Stop calling me your daughter!!! "

  "Rafa shouts these words, but it's too late. "

  "Sami has already flown away. "

  show RAFA POKERFACE: #at left
    xalign 0.2
    yalign 1.0

  "You turn to her. "

  stop music fadeout 1.0

  cris "I know you said that what happened with my sister is none of your business. "

  cris "But it can be your business. I mean, if you want. "

  play music THEMESONG fadein 2.0

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  cris "This never would have happened without your help, after all. "

  cris "Thank you, Rafa. "

  show RAFA SMILE: #at left
    xalign 0.2
    yalign 1.0

  rafa "Hey, as long as you feel like talking about it, then I'd love to hear about it. Absolutely. "

  hide RAFA

  show RAFA SMILE at center

  "So the two of you sit on the riverbank. "

  "You sprawl tummy-down, like you always did in your sister's bedroom. "

  "Rafa sits upright a short distance away, like your sister always did. "

  "Stirring the surface of the river with your finger, you start talking. "

  "You talk and talk. About what you said to your sister, about what your sister said to you. "

  "After you're done talking about that, you just keep talking. "

  "Not just about your sister, but about the rest of your family. School. Your friends. "

  "Now it hits you, just how much you'll miss all of them. "

  "Maybe you didn't appreciate what you had when you had it. It's a bittersweet feeling. "

  "Rafa just sits beside you. She listens. "

  hide RAFA

  hide CRIS

  hide  bg riverstyx

  show  cg ending2
  with slow_dissolve
  
  return

                               

label lbl_story_part_40:

  "The glowy lights in the water are brighter than ever. "

  show SAMI POKERFACE: #at right
    xalign 0.8
    yalign 1.0

  "Still crouching by the river, Sami turns to look at you. "

  sami "Are you ready, Cris? "

  cris "No. Hang on. "

  hide SAMI

  "You turn to Rafa. "

  cris "Rafa, I think you should do it. "

  rafa "Do what? I have no magic. Only Sami has magic. "

  cris "That's not what I mean. I think you should have the favor. "

  cris "You deserve it more than I do. It's all thanks to you I got this far. "

  show RAFA SHOCK: #at left
    xalign 0.2
    yalign 1.0

  rafa "That doesn't make sense. I helped you because I wanted you to have this. "

  show RAFA POKERFACE: #at left
    xalign 0.2
    yalign 1.0

  cris "Think about why I wanted this favor in the first place. I wanted to say sorry to my sister. "

  cris "I was greedy. I was a brat. "

  cris "If I'm the same greedy brat now, what's the point of talking to her? I won't deserve her forgiveness. "

  cris "If I sacrifice this favor, I'm closer to becoming the brother my sister deserved. "

  rafa "You're being too hard on yourself. "

  cris "Maybe. But what's done is done, you know? "

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  cris "But for you, this could be a rare chance! "

  cris "Just focus on a face or a voice you remember, and maybe the magic will work! "

  cris "Maybe you'll get to talk to someone you knew when you were alive! "

  cris "And maybe they can tell you about your life on Earth! "

  rafa "That's a lot of maybes. "

  cris "If there's even a small chance, I think we should take it. "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  "Rafa starts fidgeting again, so you turn to Sami. "

  hide RAFA

  show SAMI POKERFACE: #at right
    xalign 0.8
    yalign 1.0

  cris "Sami, we're switching. Rafa will make use of the favor instead. "

  "Sami stops with whatever weird magical ritual he's doing with the water. "

  "He stands up from where he's been crouching. He looms over you. "

  sami "That wasn't the deal. You can't just switch. "

  cris "I know what the deal was. I made sure to remember each word. "

  cris "\"If you give me seven teeth, I promise to arrange one conversation between Limbokin and Earthling.\""

  cris "That's what you said. That's what you promised. "

  sami "Technicalities aside, this is ridiculous. "

  sami "Who would Rafa even want to talk to? There's not a single person on Earth. "

  stop music fadeout 1.0

  show CRIS ANGRY: #as side image
    xalign 0.05
    yalign 1.0

  cris "How do you know that? "

  sami "I know Rafa. You don't. She lost her memories, you know? "

  cris "Not completely. Rafa said she remembers little things from her life. Faces. Voices. "

  play music HORROR fadein 2.0

  show SAMI ANGRY: #at right
    xalign 0.8
    yalign 1.0

  "Sami begins to look angry for the first time. "

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  "He starts beating his wings, as if trying to intimidate you. "

  "You {i}are{/i} a bit scared, but you stand your ground. "

  show CRIS ANGRY: #as side image
    xalign 0.05
    yalign 1.0

  "You turn to Rafa. "

  show RAFA SHOCK: #at left
    xalign 0.2
    yalign 1.0

  cris "Rafa, don't listen to him. We can do this -- "

  "But Rafa's freaking out, for some reason. "

  "She rapidly walks off. "

  hide RAFA

  cris "Rafa! Wait! Where are you going? "

  sami "Look what you've done. You've upset her. "

  hide SAMI

  "Ignoring Sami, you chase after Rafa. "

  "You call her name, again and again. "

  "But she can't seem to hear you. "

  hide CRIS

  hide  bg riverstyx

  stop music fadeout 1.0

  show  bg purgatory
  with slow_dissolve

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  "Rafa is huddled in a corner somewhere. Not talking. Not moving. "

  "You've tried talking to her. You've tried snapping your fingers in front of her face. "

  "No response. "

  play music BACKGROUND fadein 2.0

  "She just stared blankly, as if lost in thought. "

  "The only time she reacted was when you touched her back, as you were trying to get her to talk to you. "

  "She shrieked and jerked away from your hand. "

  "You tried saying sorry, but again, she didn't respond. "

  "So you've decided to leave her alone for now. "

  "Sitting a short distance away from her, you doodle on your sketchbook instead. "

  "You're sketching home. The windows, the doors, the different rooms. "

  "If one day you forget about home, you can look at these sketches to remember. "

  show RAFA POKERFACE at center

  rafa "Cris? Can we talk? "

  "Rafa is suddenly beside you. You didn't even notice her approaching you. "

  "You close your sketchbook. "

  cris "Sure, we can talk. "

  cris "Listen, I'm sorry for putting you on the spot like that. It was a big decision -- "

  rafa "You were right. How did he know? "

  "You just stare. What is she talking about? "

  rafa "Sami always acts like that, like he alone knows what's best for me. "

  rafa "He always tells me he's the only one who really knows me. "

  rafa "And I trust Sami. Of course I do. "

  rafa "When I was lost and confused and needed someone, he was there. I will always owe him for that. "

  rafa "But sometimes -- I don't know -- I get the feeling he's not telling me the whole truth. "

  rafa "And that feeling gets even stronger when I look at his wings. "

  cris "His wings? Why? "

  rafa "Can you keep a secret? "

  "Ate Yasmin once asked you the same question. You answer Rafa the same way you answered your sister. "

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  cris "Yeah, I can. "

  rafa "It's weird. I've seen Sami taking off his wings a few times. Almost like they're clothes. "

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  cris "Taking them off? How does that even work? "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  rafa "I don't know, but it's like this whole covert operation. He's very secretive about it. "

  rafa "There's this spot by the river that's well-hidden, so I've watched him do it a couple of times. "

  rafa "He doesn't know that I know. "

  rafa "It's the same every time. He sheds the wings, then goes to wash himself in the river. "

  rafa "I don't know how wings are supposed to work. I mean, he's the only person I've met who has them. "

  rafa "He says there are others, but he's the only one in purgatory who has wings. "

  rafa "For all I know, everyone who has wings does this. Removes their wings like they're clothes. "

  rafa "But isn't it strange? Something about it doesn't feel right to me. "

  cris "Huh. "

  "You're not sure what to make of this story. "

  rafa "The reason I'm telling you this is because there's something I want to try. Just this wild idea of mine. "

  rafa "I have a plan. It might be risky. Maybe even dangerous. "

  rafa "But will you help me? "

  show CRIS SMILE: #as side image
    xalign 0.05
    yalign 1.0

  cris "Hey, you helped me with the trading. Of course I'll help you. "

  rafa "You don't even know what the plan is yet. "

  cris "Does it matter? We're friends now, right? Friends look out for each other. "

  show RAFA SMILE at center

  "The two of you smile at each other. "

  hide RAFA

  hide CRIS

  hide  bg purgatory

  show  bg riverstyx
  with slow_dissolve

  show CRIS LAUGH: #as side image
    xalign 0.05
    yalign 1.0

  "You're playing in the river. Splashing around like a kid. "

  "You {i}are{/i} a kid, but ever since you arrived in purgatory, you've felt less and less like one. "

  "Sure, the river glows creepily. Even so, playing in the water reminds you of summer vacation. "

  stop music fadeout 1.0

  "Beach trips. "

  "Collecting seashells and coral with Ate Yasmin. "

  "Orbs on your shoulders in the photos taken at night. "

  "Then an angry voice interrupts your dreamy thoughts. "

  play music TENSION fadein 2.0

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  show SAMI ANGRY at center

  sami "Hey! What the hell are you doing?! "

  sami "Get out of the river! Now! "

  "Sami lunges at you, as if planning to haul you away! "

  "You dodge and run off toward the riverbank. "

  "Sami's chasing after you! "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  "Once he's close enough, you turn around to splash mud on his outfit. "

  show SAMI SHOCK at center

  "His jaw drops. "

  sami "My . . . my perfect clothes. . . . "

  show SAMI ANGRY at center

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  "His wings start beating. He looks like he wants to attack you! "

  "You bolt before he can try anything! "

  hide SAMI

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  "As Rafa predicted, Sami doesn't chase you very far. "

  "He returns to the riverbank, more concerned with his muddy clothes than with revenge. "

  "As soon as Sami loses interest in chasing you, you join Rafa at her hiding place. "

  show RAFA SMILE at center

  "Rafa gives you a thumbs-up. "

  "Completely hidden, you both silently turn to watch what Sami's going to do. "

  hide RAFA

  show SAMI POKERFACE at center

  "Sami's looking around, checking to see if he's alone. "

  "Thinking that he is, he peels off his wings. "

  hide SAMI

  show WINGLESSSAMI POKERFACE at center

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  "It's very weird to watch. "

  "Rafa was right. Something about it just feels wrong. "

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  "Sami leaves the wings by the riverbank. "

  "He wades into the river and tries to wash the mud from his clothes. "

  hide WINGLESSSAMI

  show RAFA POKERFACE at center

  "Without a second to waste, you and Rafa rush to the riverbank. "

  "You both grab one wing each, then take off running in opposite directions. "

  hide RAFA

  sami "WHAT THE HELL DO YOU THINK YOU'RE DOING?! "

  "You spare one look backward. "

  "Sami has chosen to chase Rafa, not you! "

  "But Rafa's fast. Fast enough to get away, you hope. "

  "Right now, you have your own problems. "

  "You and Rafa knew you would split up, so you set a meeting place beforehand. "

  "But how can you even get there? "

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  "The wing you're carrying obviously doesn't want to! "

  "The wing thrashes wildly in your arms! "

  "It's so strong! Maybe it's trying to drag you back to its owner? "

  "The wing gives one mighty jolt, and -- "

  hide CRIS

  hide  bg riverstyx

  show  bg sky
  with slow_dissolve

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  "The wing shoots to the sky, dragging you along for the ride! "

  "You're soaring upward! "

  cris "AHHHHHHHHHH!!! "

  "You clutch the wing tightly in your arms. You're holding on for dear life. "

  "Okay, even if you let go, you probably won't die again. "

  "But from this height, it will surely be a nasty fall. "

  "You don't know what a fall like this will do to your body, and you don't want to find out. "

  "At the very least, there will be pain. "

  "The wing keeps zooming up, up, up. "

  "Where is it taking you? What's up there? "

  "Will you ever get back down? "

  hide CRIS

  hide  bg sky

  stop music fadeout 1.0

  show  bg riverstyx
  with slow_dissolve

  show RAFA ANGRY: #at left
    xalign 0.2
    yalign 1.0

  show WINGLESSSAMI ANGRY: #at right
    xalign 0.8
    yalign 1.0

  "Sami has Rafa backed against a wall. "

  "He towers over her. "

  play music HORROR fadein 2.0

  sami "Just hand it over, Rafa. That's all you need to do. "

  show WINGLESSSAMI POKERFACE: #at right
    xalign 0.8
    yalign 1.0

  sami "If you do that, I'll forgive you. I'll forget all about it. I won't hold it against you. "

  sami "I won't hurt you or Cris. I promise. "

  "Rafa hugs the wing to her chest. It thrashes in her arms. She can barely contain it. "

  "She's out of breath when she speaks. "

  rafa "I know you have a secret. I don't know how I know, but I do. "

  rafa "Tell me everything. Or else. "

  "Sami snorts. "

  sami "Or else what? "

  "Rafa pulls a makeshift weapon from her pocket. "

  "A metal rod borrowed from one of the Limbokin, which she then spiked with teeth. "

  "She presses the weapon against the wing. "

  rafa "Go on. Start talking. "

  show WINGLESSSAMI SHOCK: #at right
    xalign 0.8
    yalign 1.0

  "Sami's eyes widen. "

  sami "You're bluffing. "

  "Rafa pricks the wing with the Limbokin teeth. "

  "A golden substance -- half liquid, half gas -- seeps from the puncture wound. "

  "Sami gasps. "

  show WINGLESSSAMI ANGRY: #at right
    xalign 0.8
    yalign 1.0

  sami "What are you doing?! Don't you realize how foolish you're being? "

  rafa "Foolish, huh? Enlighten me, then! "

  "More golden wisps appear as she presses down even harder on the wing. "

  sami "Okay, okay! I'll tell you whatever you want! "

  sami "Just stop injuring that wing. Holy hell. "

  show WINGLESSSAMI POKERFACE: #at right
    xalign 0.8
    yalign 1.0

  "Sami heaves out a sigh. "

  sami "Okay, do you remember that fable I told you about? "

  sami "When we were roleplaying one of our father-and-daughter scenarios? "

  rafa "I {i}never{/i} want to roleplay. "

  rafa "I just shut up and let you play your games so that they end sooner. "

  show WINGLESSSAMI ANGRY: #at right
    xalign 0.8
    yalign 1.0

  sami "Will you just let me finish? Do you or do you not want to know this secret you keep harping about? "

  "Rafa just glares at him. "

  sami "{i}Thank you.{/i}"

  show WINGLESSSAMI POKERFACE: #at right
    xalign 0.8
    yalign 1.0

  sami "As I was saying before you rudely interrupted me, think back to that fable. "

  rafa "What about it? "

  sami "That's it. That fable is the answer to everything you want to know. "

  hide WINGLESSSAMI

  hide RAFA

  hide  bg riverstyx

  show  NVLMODE
  with slow_dissolve

  #"[START NVL MODE

  nvl clear
  nvlnarrator "Once upon a time, there was this flock of birds. "

  nvlnarrator "The flock was ruled by a peacock king. The king could not fly as far and as high as the other birds. "

  nvlnarrator "Even so, his loyal subjects supported his frail wings from beneath to make him believe he could. "

  nvlnarrator "The flock was a peaceful one. Or rather, if any bird dared to disrupt the peace, the king would take action. "

  nvlnarrator "The king would order his subjects to clip the dissident's wings. The dissident would then plunge to the ground, never to fly again. "

  nvlnarrator "As the numbers in the sky dwindled, the king wondered more and more about life below. "

  nvlnarrator "The king himself would never deign to touch the ground, but he thought he might send an envoy who could relay the living conditions to him. "

  nvlnarrator "A budgerigar volunteered to go on the mission. She was the only one who dared. "

  nvlnarrator "Younger than most other birds, the budgie didn't know enough to fear the ground, as older, more experienced birds did. "

  nvlnarrator "So the peacock king sent the budgerigar on her way. "

  nvlnarrator "Not the best at flying in her flock, the budgie crashed horribly during her landing. The place she had fallen was a little off course. "

  nvlnarrator "The only one who witnessed her crash was a hummingbird who watched the boundary between air and earth. "

  nvlnarrator "The hummingbird's wings had been clipped long ago, for his defiance against the peacock king. "

  nvlnarrator "As the budgie lay unconscious, the hummingbird saw his chance and took it. "

  nvlnarrator "He tore off the budgie's wings and wore them as his own. "

  nvlnarrator "Because the wings were merely stolen, the hummingbird could neither fly high nor fly long, but fly he could. "

  nvlnarrator "He intended to tell all birds and beasts that the peacock king had blessed him with new wings, for all the good work he had done on the ground. "

  nvlnarrator  "The hummingbird considered silencing the budgie forever, so that she could not contradict his story. "

  nvlnarrator "But when the budgie awoke, she had lost all her memories. "

  nvlnarrator "She no longer remembered her mission. She had forgotten that she had once belonged to a flock. "

  nvlnarrator "Some birds from the flock came by to look for the budgie, who had never returned from her mission. "

  nvlnarrator "But the hummingbird, with his silver tongue, found it easy to mislead them. "

  nvlnarrator "He hid the budgie from their sight until they departed. "

  nvlnarrator "From then on, the hummingbird took the budgie under his stolen wings, guiding her as she navigated her new home. "

  nvlnarrator "He took good care of her and kept her happy, so that she would not go looking for answers. "

  nvlnarrator "And they lived happily ever -- "

  #"[END NVL MODE

  hide  NVLMODE

  show  bg riverstyx
  with slow_dissolve

  show RAFA ANGRY: #at left
    xalign 0.2
    yalign 1.0

  show WINGLESSSAMI POKERFACE: #at right
    xalign 0.8
    yalign 1.0

  rafa "Don't you dare finish that sentence. "

  rafa "I always thought that fable of yours was the worst. It doesn't even have a moral. "

  show WINGLESSSAMI SMILE: #at right
    xalign 0.8
    yalign 1.0

  "Sami smiles bitterly. "

  sami "I suppose the moral of the story is you never should have trusted me. "

  show WINGLESSSAMI POKERFACE: #at right
    xalign 0.8
    yalign 1.0

  sami "So what now? Are you going to cry? Or perhaps attack me? "

  sami "I might have taken one thing from you, but haven't I given you so many other things since then? "

  rafa "Oh? {i}So many other things?{/i} Name one thing. "

  sami "I gave you a home. "

  show RAFA POKERFACE: #at left
    xalign 0.2
    yalign 1.0

  stop music fadeout 1.0

  "Rafa is silent for a while, then -- "

  rafa "Hey, Sami, what's going to happen if I let go of this wing? "

  "As if it can hear her talking about it, the wing trembles even more violently in her arms. "

  rafa "The wings were just lying there, docile, on the riverbank, weren't they? "

  rafa "But do you see how the wings reacted when I touched one of them? "

  rafa "Do you think maybe they're excited to return to their true owner? "

  hide WINGLESSSAMI

  hide RAFA

  hide  bg riverstyx

  play music TENSION fadein 2.0

  show  bg sky
  with slow_dissolve

  show CRIS POKERFACE: #as side image
    xalign 0.05
    yalign 1.0

  "Your arms are numb from holding on to the wing. It shows no sign of wanting to return to the ground. "

  "Where's Rafa now? Is she safe? "

  "You try to picture her reaction when you show up in the meeting place after falling miles down. "

  "Bones broken. Guts spilling out. "

  "Yikes. "

  show CRIS SHOCK: #as side image
    xalign 0.05
    yalign 1.0

  "Just then, the wing gives a particularly strong jolt. "

  "You're thrown off! "

  "Looks like the scenario you just pictured will now be a reality! "

  "As you plummet, you close your eyes. "

  hide CRIS

  hide  bg sky

  stop music fadeout 1.0

  show  bg black
  with slow_dissolve

  "You brace for the impact of the ground. The pain. "

  "But there's no impact. No pain. "

  "Instead, you feel hands snatching you up. "

  "Have you been saved? "

  "You open your eyes. "

  hide  bg black

  play music THEMESONG

  show  cg flight
  with slow_dissolve

  cris "Rafa?! "

  "Rafa has saved you! "

  "She seems to be glowing! And more importantly, she has wings! "

  "Rafa's flying!!! "

  cris "What -- "

  rafa "Look, Cris! I have wings! "

  cris "I can see that! "

  rafa "They were my wings, all this time! Not Sami's! He stole them from me! "

  cris "What?! So where's Sami now? "

  rafa "Down where he belongs! He can't touch us here! "

  rafa "I'll tell you the whole story later, when we get there! "

  cris "Where are we going? "

  rafa "Where do you think? Up there! "

  cris "Heaven?! "

  rafa "It's where I belong! Where I lived before Sami stole my wings! "

  cris "So you're -- "

  rafa "Yeah, I'm an angel! "

  cris "That's super cool! "

  rafa "I know! "

  cris "Wait, Rafa. Maybe you belong up there, but I don't. "

  cris "Will they let me pass the pearly gates? "

  cris "Wasn't I sent to purgatory for a reason? "

  rafa "Don't worry, Cris! You're a good person! "

  rafa "I've seen it first-hand, and I'll tell them. I'll tell all of them where you really belong. "

  rafa "I'll fight them if I have to! "

  rafa "You're getting in, Cris. Trust me. I won't accept any other outcome. "

  "Maybe this isn't going to work, but has Rafa ever steered you the wrong way? "

  "Maybe she's right again this time. Maybe you can trust her on this. "

  "Maybe you can allow yourself to have a little hope. "

  hide  cg flight

  show  cg ending3
  with slow_dissolve

  return

