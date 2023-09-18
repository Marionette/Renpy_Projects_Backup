label start:

  #jump lbl_credits

  #reset variables
  $malice_level = 0
  $heart_item = False
  $heart_show = False
  $intoxication = False

  # Start the game
  jump lbl_001
  
  return

label lbl_001:

  play music music_menu fadein 2.0

  scene cg cg_suits with slow_dissolve

  "Cards control this city."

  "The rule of four retains the balance, without which the booming gambling industry will soon fall into shambles."

  "Each of the four Playing Card Suits operates one of the city's famed casinos — Diyamantes, Bastons, Espadas, and Pusos."

  "Each Suit possesses faint remnants of an ancient witchery."

  "Strong enough to lend a golden glamor to the cityscape, yet subtle enough that the Suits may interact unnoticed with most humans."

  "Humanity resides within them too, mingling with the traces of the dubiously divine."

  "Their roles as Suits, while capable of being passed on to eligible successors, are otherwise vested and immovable."

  "As beings akin to demigods, they can almost never die while they hold their positions, except under rare circumstances."

  "One might even say that they're close to immortal."

  stop music fadeout 1.0

  show bg bg_roulette with slow_dissolve

  "Splayed open against the roulette table."

  "Hearts — minus her hearts — is splayed open, dead, against the roulette table."

  play music music_roulette fadein 2.0

  show spades default #as side image"

  show clubs default at left behind spades with dissolve

  show diamonds default at right behind spades with dissolve

  "The three other Playing Card Suits — Diamonds, Clubs, and Spades — survey the mutilated body of their brethren."

  "Each face displays a different degree of disturbance."

  "Clubs, who arrived at the crime scene first, has had time to grow accustomed to this heartless new reality."

  "There's something of serenity, almost, on their facial features."

  show diamonds anxious at right behind spades with dissolve

  "Diamonds, who typically never misses the opportunity to antagonize everybody around her, is silent for once."

  "There's a wildness in her eyes that's difficult to decipher."

  show spades shock #as side image"

  "And lastly, Spades."

  "After a minute of mute horror, he manages to tear his gaze away from the carnage."

  hide spades

  show clubs shock at left behind spades

  show diamonds shock at right behind spades

  "He bolts toward the closest bin, then throws up breakfast over crumpled receipts and cigarette butts."

  "For a few seconds, Pusos, the casino operated by Hearts, is quiet except for all that horrible retching."

  "Foamy vomit is spilling forth from chapped lips. It emits the stench of acid and regurgitation."

  show spades anxious #as side image"

  show clubs anxious at left behind spades

  show diamonds default at right behind spades

  "Once Spades is done emptying the sparse contents of his abdomen, he straightens up again, his shoulders all ashiver."

  Clubs "Are you feeling okay? I don't know if I've ever seen you in such a state."

  show diamonds smirk at right behind spades

  "But before Spades can get a word out, Diamonds snorts derisively, billowing out smoke as she does."

  Diamonds "Color me even the least bit surprised by your reaction."

  Diamonds "Sources say you've been visiting Pusos regularly these past few weeks."

  show diamonds mad at right behind spades

  Diamonds "Have you been shacking up with Hearts? No wonder your relentless poker face is slipping."

  "Spades' response comes out muffled, as he's rubbing his mouth with the back of his hand."

  Spades "I don't want to talk about that. Any of that."

  show spades default #as side image"

  show clubs default at left behind spades

  show diamonds default at right behind spades

  "To make it doubly clear that this line of inquiry has closed, Spades turns deliberately toward Clubs."

  Spades "So who found the body first? And at what time?"

  "With a nod, Clubs hastens to bring the two other Suits up to speed regarding the situation."

  "It was Hanya, Hearts' second-in-command and sole holder of the casino's duplicate keys, who found the corpse."

  "Hearts wasn't picking up Hanya's calls about which coffee to order. So, at seven in the morning, Hanya let herself into Pusos."

  "On the playing area floor, Hanya spotted a familiar pink-cased phone, buzzing with the persistence of her own calls."

  "The phone's screen was shattered, perhaps from the impact of a fall."

  "Not too far away, against the roulette table, Hearts was lying lifeless. Just as ravaged as the phone."

  "At this point in the story, Spades pipes up with a question for Clubs."

  show spades anxious #as side image"

  Spades "So where's Hanya now?"

  Clubs "She's performing Hearts' usual duties for her charitable endeavors. You know how much Hearts cared about all her causes."

  show diamonds anxious at right behind spades

  Diamonds "Too damn much."

  Diamonds "If she'd only devoted half as much energy to her job, Pusos wouldn't have performed more poorly than even Espadas."

  show spades mad #as side image"

  Spades "Not cool. No insulting my casino. Or Hearts', for that matter."

  show diamonds mad at right behind spades

  Diamonds "Bite me."

  "Detached from the hostilities between the other Suits, Clubs offers a measured response to the discourse about Pusos' limited success."

  show spades default #as side image"

  show diamonds default at right behind spades

  Clubs "You know, the fact that Hearts' gambling profits lagged behind ours always made sense to me."

  Clubs "Even setting aside Hearts' frequent charitable donations, her witchery was the weakest by far among us Suits."

  show clubs anxious at left behind spades

  Clubs "How can it be otherwise when she — bless her soul — had little to no penchant for the malice that fuels our magic?"

  Clubs "And as we all know, the strength of our magic directly affects the success of our respective businesses."

  show clubs default at left behind spades

  Clubs "This is especially true for you, Diamonds, given your gift of good fortune."

  "Spades presents another question to Clubs at this point."

  show spades anxious #as side image"

  Spades "Clubs, there's something else I'm curious about."

  Spades "Hanya didn't contact the cops before calling you up?"

  Clubs "Correct. As of now, aside from Hanya, the three of us are the only ones who know of Heart's fate."

  Clubs "Hanya informed the casino's staff members that they could take the week off, but she didn't explain why."

  show spades default #as side image"

  Spades "I see. That's something."

  show diamonds mad at right behind spades

  "But Diamonds only clucks her tongue impatiently. She's fiddling with her cigarette holder."

  Diamonds "Why are we wasting our time belaboring this point? It's evident why Hanya reached out to us before anyone else."

  Spades "And why's that?"

  show diamonds default at right behind spades

  Diamonds "It seems like Hanya knew all the appropriate protocols, as well as the necessary steps for Hearts' succession."

  Diamonds "If you ask me, Hanya was already being groomed to replace Hearts in her role."

  Diamonds "Why else would those two be closer than sisters? That's got to be it, right?"

  "{i}Wrong,{/i} Spades interjects, but only inside his head."

  "Knowing too much about Hearts' relationship with Hanya can only work to Spades' detriment now that she's dead."

  Diamonds "So tell us, Clubs, what exactly did Hanya tell you over the phone?"

  Clubs "First, she said that Hearts was dead. Second, she revealed that Hearts' two hearts were missing from her corpse."

  show diamonds anxious at right behind spades

  Diamonds "You see? Hanya was obviously razor-focused on that specific detail."

  Diamonds "This suggests that she already knew we would need both hearts to complete the succession ritual."

  show diamonds mad at right behind spades

  Diamonds "As a matter of fact, Hanya is my best guess for the culprit. She's got just the right motive for murder."

  Diamonds "The allure of running Pusos as the new Hearts must've proven irresistible. All that prestige. All those profits."

  show spades mad #as side image"

  Spades "Hold up. We're not out here to figure out who did it. No need to pin the blame on Hanya or anybody else."

  Diamonds "And why shouldn't we? Hearts is dead!"

  Diamonds "She's {i}dead,{/i} Spades! She's gone, and we can never get her back!"

  Diamonds "Do you think she disemboweled and offed herself for fun? We have to hunt down the bastard who did this!"

  Spades "Who knows how long that {i}hunt{/i} could take? Especially with just the three of us doing the hunting?"

  Spades "But I'm telling you now. There's no way it was Hanya who murdered Hearts."

  Spades "If she wanted to succeed as a Suit, why'd she hide the hearts when they're required for the ritual?"

  Spades "Your theory makes no goddamn sense."

  "Diamonds parts her mouth, ready to retort, but Clubs interrupts."

  show clubs anxious at left behind spades

  show spades default #as side image"

  show diamonds default at right behind spades

  Clubs "I'm sorry, Diamonds, but I have to agree with Spades this time. We can't waste our time on extraneous matters like this."

  Clubs "We should prioritize finding the hearts so that we can perform the succession ritual to maintain the balance of the city."

  Clubs "But once the ritual's over, I'll personally retain a private investigator to take on this case. I can promise you that."

  show clubs default at left behind spades

  show diamonds mad at right behind spades

  Diamonds "Do whatever you want."

  Diamonds "Fighting with you two knuckleheads is about as fruitful as bashing my own skull with a baseball bat."

  hide diamonds

  "Diamonds stalks off, forcing Clubs to call after her."

  show clubs anxious at center with dissolve

  Clubs "Remember that we're searching for the hearts! We can finish this task faster if we're all pitching in!"

  Clubs "And none of us should leave until we've accomplished what we came here to do!"

  show clubs default at center

  "Without bothering to slow down or turn around, Diamonds only gives them the finger."

  "Now that he doesn't have the volatility of Diamonds to distract him, Spades notices that his throat has begun to itch."

  Spades "Hey, Clubs."

  Spades "What makes you think that the hearts are still inside the casino? Surely, whoever killed her took them away?"

  Clubs "If you're right and Hanya is telling the truth, it makes the most sense for the hearts to be somewhere around here."

  Clubs "When Hanya arrived, the doors were all locked. All of Hearts' keys were in her pocket, untouched."

  show spades anxious #as side image"

  Spades "So if the hearts are still in the casino, then do you think that the one who did this to Hearts is here too?"

  "They both stare at each other wordlessly, at least until Clubs breaks the silence."

  show clubs anxious at center

  Clubs "Why, Spades? Are you, of all people, afraid?"

  "Spades clutches his throat."

  Spades "I'm not. I think I need to be alone. Just for a moment."

  show clubs default at center

  show spades default #as side image"

  Spades "Don't worry. I'll also be keeping my eyes peeled for the hearts."

  Clubs "Got it. Reach out right away if you need me."

  hide clubs

  stop music fadeout 1.0

  "So Clubs walks off, their stride full of singular purpose."

  "As for Spades, there is but one place that he wants to go."

  play music music_flashback fadein 2.0

  show bg bg_bar with slow_dissolve

  "Alone at the casino's bar, Spades pours himself a drink."

  "He lets the brandy wet his mouth. Revels in its burn, in the buzzing fog that spreads slowly outward."

  "How many times has he been here — done this — before?"

  "These past few weeks, he'd visit after hours, after both Pusos and Espadas had shuttered for the day."

  "In the sober company of Hearts, he'd ransack the bottles behind the counter."

  "He'd drink and spout all sorts of directionless drivel while she'd listen, faultlessly patient."

  "He'd even pop some bubbly, occasionally. And in return, nothing except laughter and empathy would bubble from her warmth."

  "Hearts was that way, always, despite everything."

  "Despite the bottles he broke. Despite the hours he squandered with empty words."

  "She was always by his side. Believing, as no one else did, that there was something more to him than the sum of his parts."

  show spades anxious #as side image"

  "But she's not beside him now."

  "She's back there, resting against the roulette table, her torso filleted open with surgical precision."

  "At the mere remembrance, a tightly-wound knot somewhere within his thoracic cage loosens, then comes entirely undone."

  show spades cry #as side image"

  "Tears spring, unbidden, from the corners of his eyes. They trickle down, betraying him to an invisible spectator."

  Spades "The hell? This feels horrible."

  Spades "I feel like I'm falling apart."

  stop music fadeout 1.0

  "With a shuddering sigh, he sets down his glass."

  "He presses his palms against his streaming eyes."

  hide spades

  play music music_bar fadein 2.0

  show bg bg_darkness with slow_dissolve

  Spades "Don't."

  Spades "Don't you say a damn thing."

  Spades "You've already been pestering me all morning."

  menu:
    "You can't stop me.":
      jump lbl_003
    "I'm still thinking of a sufficient insult.":
      jump lbl_002

label lbl_002:

  $ malice_level += 1

  jump lbl_003

label lbl_003:

  show bg bg_bar with slow_dissolve

  show spades cry #as side image"

  "Spades stops hiding his face behind his hands."

  "All impatience now, he rapidly rubs the tear tracks from his face."

  "He's erasing the evidence of any emotion."

  show spades mad #as side image"

  Spades "Let me be. There's nothing you can say to me that I haven't said to myself already."

  "He picks up his glass again, then swills the liquor around."

  show spades default #as side image"

  "He tips back the glass to guzzle the remainder of his drink."

  "Smacking his lips with a grim sense of satisfaction, he prepares to pour himself another."

  menu:
    "Really? This early in the day?":
      jump lbl_005
    "Hearts is dead, and you're a mess.":
      jump lbl_004

label lbl_004:

  $ malice_level += 1

  jump lbl_005

label lbl_005:

  show spades mad #as side image"

  Spades "What did I just say? I don't want to hear another goddamn word."

  Spades "It's been a hell of a day. A week. A month. A life."

  Spades "Can you blame me if I just want to self-medicate?"

  menu:
    "Yesterday, you self-medicated too much.":
      jump lbl_007
    "Hearts believed in you. Look where she is now.":
      jump lbl_006

label lbl_006:

  $ malice_level += 1

  jump lbl_007

label lbl_007:

  stop music fadeout 1.0

  Spades "Just stop! How many times do I have to tell you —"

  show spades shock #as side image"

  "But before he can finish his sentence, he freezes."

  play music music_nightmare fadein 2.0

  "He's staring down, wide-eyed, at his own hands, which are resting over the counter."

  hide spades

  scene cg cg_hands_creepy with slow_dissolve

  "His hands, they seem to be collapsing into themselves."

  "Knuckles caving in."

  "Muscles flashing wet scarlet."

  "Tendons and nerves progressively exposing themselves."

  "Wildly, Spades shakes his head, as if trying to rid himself of the cursed imagery currently assaulting him."

  scene cg cg_hands with slow_dissolve

  "To his credit, this strategy works."

  "His hands are here once more in their original form."

  "Unwarped."

  stop music fadeout 1.0

  show bg bg_bar with slow_dissolve

  show spades shock #as side image"

  Spades "Did you see that? Did you see what happened?"

  Spades "Please tell me I'm not the only one."

  play music music_bar fadein 2.0

  show spades anxious #as side image"

  Spades "What's going on? Am I losing my mind now?"

  menu:
    "Your body is rebelling.":
      jump lbl_009
    "You did this to yourself. To us.":
      jump lbl_008

label lbl_008:

  $ malice_level += 1

  jump lbl_009

label lbl_009:

  Spades "I can't take this anymore."

  Spades "I'm seeing things, hearing things, feeling things I've never had to deal with before."

  show spades default #as side image"

  Spades "I need another drink. No, I need to finish the whole freaking bottle."

  menu:
    "Do it, then. Binge like you did last night.":
      jump lbl_010
    "Just get up and clear your mind.":
      jump lbl_015

label lbl_010:

  show spades mad #as side image"

  Spades "I don't remember asking for your opinion."

  Spades "You can't tell me what to do."

  show spades default #as side image"

  "He pours himself a second drink."

  "Without further ado, he tosses back all the alcohol at once."

  Spades "Ah, that definitely hit the spot."

  Spades "Another. I need another."

  menu:
    "You sack of dung.":
      jump lbl_011
    "You waste of space.":
      jump lbl_011

label lbl_011:

  show spades mad #as side image"

  Spades "Say whatever you want."

  Spades "The more I drink, the farther away you'll drift from me. That's my theory, at least."

  Spades "All the more incentive to keep drinking, right?"

  show spades default #as side image"

  "He doesn't bother to fill his glass for a third time. He simply tilts back the bottle to pour the brandy directly down his throat."

  menu:
    "Enough.":
      jump lbl_016
    "You're a hopeless case.":
      jump lbl_012

label lbl_012:

  "He pauses only briefly in his chugging."

  Spades "Like I said earlier, you're not telling me anything that I haven't told myself first."

  "With this, he resumes glugging away with a new fervor."

  "Down the brandy goes."

  "A quarter of the way through."

  "Halfway."

  "Then all the way down."

  jump lbl_013

label lbl_013:

  hide spades

  "The empty bottle now clatters on the counter."

  stop music fadeout 1.0

  "Weighted by the fog of firewater, his head falls on his arms, which are folded over the counter."

  show bg bg_darkness with slow_dissolve

  "Before too long, he descends into oblivion."

  play music music_nightmare fadein 2.0

  show spades default #as side image"

  "Spades wanders, for what feels like years, deeper into impenetrable darkness."

  "Blind as a bat, he ambles around a barren landscape stretching infinitely on all sides."

  show spades shock #as side image"

  "At some point, he stumbles, throwing out his palms to break the fall."

  "But shortly after contact — soil to skin — he recoils from what he senses beneath him."

  "The ground is slick to the touch, smearing his palms with a glutinous substance."

  "This surface over which he's walked for an eternity — it's {i}alive.{/i}"

  "It's breathing. Bearing its imperceptible teeth."

  "Anticipating, it seems, the moment when it can finally swallow him whole."

  show spades anxious #as side image"

  "Choking back the bile creeping up his throat, he struggles back to his feet. Or at least he tries."

  "His legs are leaden. Uncooperative, all of a sudden."

  show spades shock #as side image"

  "Ahead of him, an indecipherable {i}something{/i} is approaching."

  "It's emitting just enough light to be barely visible."

  Spades "What is that?"

  menu:
    "What you've been waiting for.":
      jump lbl_014
    "The end of everything.":
      jump lbl_014

label lbl_014:

  hide spades

  scene cg cg_nightmare with slow_dissolve

  "But he can't hear anything anymore. Nothing except the hammer of a stray heartbeat in his chest."

  "She's coming for him."

  "Coming closer."

  "Closer."

  scene cg cg_ending01 with slow_dissolve
  $ persistent.ending_seen_01 = True
  pause
  jump lbl_credits

  return

label lbl_015:

  show spades anxious #as side image"

  Spades "I hate to admit this, but you might be right this time."

  Spades "My mind's already a mess. I'm just making it worse."

  show spades default #as side image"

  Spades "In any case, I'd better go poke around the casino. I told Clubs I would."

  jump lbl_017

label lbl_016:

  $intoxication = True

  "Spades ignores this. He continues chugging away, seemingly out of spite."

  "About halfway through, he coughs, then smacks the bottle down on the counter."

  Spades "That's enough, at least for now."

  Spades "I should poke around the casino. I told Clubs I would."

  jump lbl_017

label lbl_017:

  "Spades screws the cap back on, then stashes the bottle somewhere beneath the counter."

  Spades "Now where should I go?"

  menu:
    "You should visit the slot machines.":
      jump lbl_018
    "Return to the roulette table.":
      jump lbl_031

label lbl_018:

  stop music fadeout 1.0

  Spades "Yeah, I might as well."

  Spades "I have to check the slots, sooner or later."

  play music music_slots fadein 2.0

  show bg bg_slots with slow_dissolve

  "He gazes at the array of slot machines. Wheels of fortune are emblazoned atop darkened screens."

  show diamonds default at center with dissolve

  Diamonds "Oh, joy. My least favorite person in the universe is here."

  show spades anxious #as side image"

  Spades "Hey. Find anything yet?"

  show diamonds mad at center

  Diamonds "Why are you talking to me?"

  Spades "Why not? You heard what Clubs said. We have to work together."

  show spades default #as side image"

  show diamonds smirk at center

  Diamonds "Heh. That's not at all what Clubs said."

  Diamonds "But it's no wonder your memory is failing you, as per usual."

  Diamonds "Past the haze of a morning booze-up, I expected nothing less than to see you blundering about like this."

  show spades anxious #as side image"

  Spades "{i}Booze-up?{/i} I wasn't —"

  show diamonds mad at center

  Diamonds "I saw you, Spades. I saw you drinking at the bar and talking to yourself."

  show spades mad #as side image"

  Spades "Come on! It was barely anything! Just a little something to take the edge off!"

  Diamonds "Yes, it sure seemed that way when you were manhandling an entire bottle of brandy."

  Diamonds "Are you taking {i}any{/i} of this stuff seriously?"

  "She huffs out a cloud of smoke."

  show spades default #as side image"

  show diamonds default at center

  Diamonds "Listen. If you're only going to cock this up, why don't you go back to your solo drinking session instead?"

  Diamonds "Leave the business to Clubs and me. We can wrap things up much faster without you."

  menu:
    "She's right. No one needs you here.":
      jump lbl_019
    "Don't listen to her. Who needs her.":
      jump lbl_021

label lbl_019:

  stop music fadeout 1.0

  show spades anxious #as side image"

  Spades "You don't need me. Of course you don't."


  Spades "I'll get out of your way, then."


  Diamonds "Please do."

  hide diamonds

  play music music_bar fadein 2.0

  show bg bg_bar with slow_dissolve

  show spades default #as side image"

  "So Spades is back. He's here at the bar again."

  "He reunites with all the bottles that, with the exception of Hearts, have served as his only companions."

  menu:
    "You tried to be better, didn't you?":
      jump lbl_020
    "You ended up wrecking everything in your path.":
      jump lbl_020

label lbl_020:

  Spades "I'm begging you. Keep your thoughts to yourself."


  "Without wasting any more time, he retrieves the liquor he's stowed underneath the counter."

  "He tips back the bottle with reckless abandon. He takes swallow after swallow."

  "In no time at all, he polishes off all the brandy."

  jump lbl_013

label lbl_021:

  show spades mad #as side image"

  Spades "You don't own this place. You can't tell me what to do. Or where to go."


  show diamonds smirk at center

  Diamonds "What a way to phrase your comeback."

  Diamonds "Congratulations, Spades. If you were trying to sound like a petulant child, you've succeeded admirably."

  show diamonds mad at center

  Diamonds "Let me guess. This man-child act you're putting on, you used it regularly to garner sympathy points from Hearts."

  Diamonds "She was just soft enough — naive enough — to fall for your lies."

  Spades "My lies? What lies?"

  Diamonds "Don't play ignorant. You know {i}exactly{/i} what I'm talking about."

  menu:
    "Throw the accusation back at her.":
      jump lbl_022
    "Don't take the bait, you wuss.":
      jump lbl_024

label lbl_022:

  $ malice_level += 1

  "If Diamonds is squaring up for a fight, then isn't it only right for Spades to give her what she wants?"

  show spades smirk #as side image"

  Spades "Funny thing — you calling {i}me{/i} out for my lies."

  Spades "But weren't {i}you{/i} the one who was always lying to Hearts?"

  show diamonds default at center

  Diamonds "Spare me the drunken raving. I have no idea what you're talking about."

  Spades "No? Then I was only imagining those intense, heated gazes you were always throwing toward Hearts?"

  show spades default #as side image"

  show diamonds shock at center

  Diamonds "What?"

  show spades mad #as side image"

  Spades "You heard what I said. You thought no one was aware?"

  Spades "Hearts might've been oblivious, but I knew all too well."

  show diamonds anxious at center

  Spades "You were always waiting around for her to notice your true feelings, weren't you?"

  Spades "You can lash out at me for daring to shoot my shot. But you only have yourself to blame for not speaking up."

  Spades "Now it's too late. You blew it. You'll never have her."

  show diamonds mad at center

  Diamonds "You're crossing the line. Who gave you the right to talk to me that way?"

  menu:
    "Double down.":
      jump lbl_023
    "Back away.":
      jump lbl_024

label lbl_023:

  $ malice_level += 1

  "Spades spits out another lie. Who can confirm or deny the truth, after all, now that Hearts is gone?"

  "Besides, is it {i}really{/i} a lie, in the first place?"

  show spades smirk #as side image"

  show diamonds shock at center

  Spades "I {i}had{/i} her, you know. That's right — I got a taste of Hearts."

  Spades "I tasted her, savored her, swallowed her whole."

  Spades "And she was sweeter than you'll ever have the pleasure to know."

  show diamonds mad at center

  Diamonds "Screw you, Spades. {i}Screw you all the way off.{/i}"

  Diamonds "If someone's out here slaughtering the Suits, I swear by the Two of Diamonds — I'll do everything to ensure you're next."

  Diamonds "I'd better go, given that I'm tempted to end you myself."

  hide diamonds

  show spades default #as side image"

  "Emitting enough smoke to put the Taal Volcano to shame, Diamonds stomps off toward a far cluster of slot machines."

  jump lbl_025

label lbl_024:

  show spades anxious #as side image"

  Spades "Look. We're getting nowhere, arguing like this. Let's cool off."

  Spades "I'll go search another area of the slots. You can stay here if you want."

  show spades default #as side image"

  show diamonds default at center

  Diamonds "Ugh. Just stop messing around, got that?"

  Spades "I won't mess around if you promise you won't either."

  Diamonds "Whatever."

  hide diamonds

  "Without further comment, Diamonds exhales a stream of smoke then sidles toward a nearby cluster of slot machines."

  jump lbl_025

label lbl_025:

  "Alone again, Spades relocates to another row."

  "He stops beside his favorite slot machine. Or, as Hearts playfully dubbed it: Spades' Lucky Day."

  menu:
    "Let's play a round.":
      jump lbl_027
    "Not now.":
      jump lbl_026

label lbl_026:

  "He doesn't feel particularly lucky right now. Better not risk it."


  "He should just move on."

  jump lbl_030

label lbl_027:

  "He checks his pocket for any stray Pusos tokens from the last time he was here."


  "There's only one token left. Will this be enough?"

  "He inserts it into the slot, then punches the button."

  "The symbols on the screen start spinning. They spin so quickly that they're a blur."

  if malice_level >= 4:
    jump lbl_028
  if malice_level < 4:
    jump lbl_029

label lbl_028:

  $heart_item = True

  show spades smirk #as side image"

  "Triple sevens!"

  "As expected, the worse his day is, the higher his likelihood of winning the big bucks."

  "A trick compartment below the screen pops open."

  "He reaches into the compartment and wraps his fingers around the object hidden there."

  show spades default #as side image"

  "After tossing glances in all directions to ensure that no one's watching, he stuffs the object into his pocket."

  "He slams the secret compartment door shut, then moves on before anyone can notice what's up."

  "He roams around now, not really going anywhere."

  "His throat has begun to itch again, but the imperceptible weight of a secret in his pocket keeps him from coping with his flask."

  stop music fadeout 1.0

  show spades shock #as side image"

  "His meandering is only interrupted when he hears Clubs hollering his name."

  "Clubs is calling the Suits to a meeting."

  jump lbl_039

label lbl_029:

  "The symbols roll to a stop."

  show spades anxious #as side image"

  "One spade, one club, and one diamond."

  "Figures. Maybe he should try again later."


  "Sighing, he moves on."


  show spades default #as side image"

  jump lbl_030

label lbl_030:

  "He traipses down row after row of slots."

  "As he arrives at the end of a row, his throat has begun to itch again."

  stop music fadeout 1.0

  show spades anxious #as side image"

  "He's just about to extract a flask from an inner pocket of his blazer, when the sound of Diamonds' voice distracts him."

  "She's calling for both Clubs and Spades to come over to where she is."

  jump lbl_038

label lbl_031:

  show spades anxious #as side image"

  Spades "Do I have to? I don't want to hang around {i}that{/i} anymore."

  menu:
    "Do it, you coward.":
      jump lbl_032
    "You gonna bawl like a baby again?":
      jump lbl_032

label lbl_032:

  stop music fadeout 1.0

  show spades anxious #as side image"

  Spades "Ugh, fine. I'll do it if I have to, but I'm not going to like it."

  "He rises to his feet, then heads back to the roulette table."

  play music music_roulette fadein 2.0

  show bg bg_roulette with slow_dissolve

  show spades default #as side image"

  show clubs default at center with dissolve

  "Clubs is here too. Just like Spades, they've been drawn back to the roulette table."

  "Clubs is scrutinizing the corpse, while remaining cautious about not touching it."

  show spades anxious #as side image"

  Spades "Hey, did you find anything? I know I haven't."

  show clubs smile at center

  "Clubs flashes a smile at the sound of his voice."

  Clubs "I checked all the promising locations of the casino, but I saw nothing useful, no."

  show spades default #as side image"

  show clubs default at center

  Clubs "There's one thing I do know, though."

  Spades "What's that?"

  show clubs anxious at center

  Clubs "In all my centuries of existence, I've never seen a crime scene quite like this one. Not with my own eyes, at least."

  Clubs "To mutilate a body this meticulously. I can only surmise that the culprit is a butcher, surgeon, or mortician."

  show spades anxious #as side image"

  show clubs default at center

  Spades "I thought you agreed with me earlier. Finding the one who did this shouldn't be our priority."

  Clubs "No, I know. But while I remain in the dark about where we can find the hearts, I can't help but speculate."

  Clubs "There was a question I wanted to ask you, by the way. It's about something that Diamonds said."

  Spades "You should know better than to listen to what she's saying."

  Spades "When she's in a bad mood, she starts spouting even more nonsense."

  show spades default #as side image"

  Clubs "But at least one thing she mentioned rang true. I've also heard that you've been visiting Pusos regularly after closing time."

  show clubs anxious at center

  Clubs "I may not understand certain impulses — that hunger to be close to another — but I will never condemn those who do."

  Clubs "Were you and Hearts in {i}that{/i} sort of relationship?"

  show spades anxious #as side image"

  show clubs default at center

  "Presented point-blank with such a crucial question, Spades' throat starts to itch in that familiar manner."

  "He wishes he could seek solace from his flask of whiskey, but he knows he should concentrate right now."

  show spades default #as side image"

  "How should he respond to Clubs' question?"

  menu:
    "What's the point of lying now?":
      jump lbl_033
    "Lie anyway.":
      jump lbl_034

label lbl_033:

  "He's going to set the record straight."

  Spades "No, Hearts and I weren't in a romantic or physical relationship. We never were."

  Spades "We were drinking buddies. That's all."

  show clubs anxious at center

  Clubs "Then why didn't you deny Diamonds' accusation earlier?"

  Spades "If I told the truth, would Diamonds have believed me?"

  Spades "She's always ready to believe the worst of everybody, especially me."

  show clubs default at center

  Clubs "You may have a point."

  Spades "There's something else I should probably mention."

  Spades "Hearts and I didn't only meet in Pusos for drinks. We were meeting regularly at other places, for other purposes."

  show clubs shock at center

  Clubs "Really? I haven't heard about that."

  show spades smirk #as side image"

  Spades "Yeah, we guessed that you and Diamonds would freak out if you knew."

  show clubs default at center

  Spades "So whenever Hearts and I went out together, I'd be in disguise."

  Clubs "Where would you go?"

  show spades default #as side image"

  Spades "I accompanied her when she attended charity events. I'd be her date. Platonically, of course."

  show clubs shock at center

  Clubs "Huh. I'm not sure what I was expecting, but it definitely wasn't {i}that.{/i}"

  Spades "Yeah, I think I just wanted to understand. Because the concept has always been a mystery to me."

  Clubs "What concept? Do you mean charity?"

  "Spades nods."

  show spades anxious #as side image"

  show clubs default at center

  Spades "I wanted to see what she was getting out of such initiatives."

  Spades "I wanted to understand why she was giving so much of herself, only to gain nothing in return. It made no sense to me."

  show spades default #as side image"

  Clubs "I'm certain she didn't see it that way. Giving is its own reward — an intangible pleasure that's nonetheless real."

  Spades "That's exactly what I couldn't grasp. This intangible thing you're talking about."

  jump lbl_037

label lbl_034:

  $ malice_level += 1

  show spades anxious #as side image"

  "No harm in uttering a white lie or two, right?"

  "Spades shrugs."

  Spades "Hearts and I were two consenting adults. Did we do anything wrong?"

  show spades default #as side image"

  show clubs anxious at center

  Clubs "No, of course not."

  Clubs "As I've said, I'm not going to judge someone for experiencing a phenomenon that will forever remain a stranger to me."

  Clubs "However, I can't help but worry about you."

  Clubs "You must know that, in the event of a murder, the authorities tend to suspect the victim's former partner."

  show spades anxious #as side image"

  show clubs default at center

  Spades "But I cared about Hearts. {i}Loved{/i} her, even."

  Spades "I could {i}never{/i} hurt the one person on earth who can make me feel all these intense feelings."

  show clubs anxious at center

  Clubs "I believe you. Of course I do."

  Clubs "But the police might not see it the same way."

  show spades default #as side image"

  show clubs default at center

  Spades "Well, the police will have a whole array of suspects to investigate, then."

  Spades "I'm not sure if you know this, but Hearts had lots of lovers of all genders. I wasn't the only one."

  Clubs "I do know that. It was in Hearts' nature to love widely and deeply."

  Clubs "Even so, you appear to be the only one who visited her with any discernible frequency."

  show spades anxious #as side image"

  Spades "Hmm. It might seem that way, but she had at least one other partner who matched that description."

  show clubs anxious at center

  Clubs "Really? Who?"

  menu:
    "You should tell Clubs it was Hanya.":
      jump lbl_035
    "Accuse Diamonds.":
      jump lbl_036

label lbl_035:

  show spades default #as side image"

  show clubs shock at center

  Spades "I'm talking about Hanya, obviously."

  Spades "Given that Hanya is Hearts' second-in-command, those two spent more time alone together than we'll ever know."

  Clubs "But they weren't dating, were they?"

  show spades anxious #as side image"

  show clubs anxious at center

  Spades "They were indeed girlfriends. Of Hearts' many lovers, Hanya was most likely her favorite one."

  Spades "It sucks for me to admit it, but that's the way it was."

  show spades default #as side image"

  Clubs "Oh. Does Diamonds know?"

  show clubs default at center

  Spades "No. And we shouldn't tell her. She has enough beef with Hanya to begin with."

  Clubs "You're right. That would only fuel the flames between them."

  jump lbl_037

label lbl_036:

  $ malice_level += 1

  show spades mad #as side image"

  show clubs shock at center

  Spades "It was Diamonds. She and Hearts were secretly involved."

  Clubs "{i}What?{/i}"

  Spades "Didn't you hear her going on earlier? She was raving mad! Especially at {i}me!{/i}"

  Spades "Why else do you think that was? She and Hearts were together!"

  show spades anxious #as side image"

  show clubs anxious at center

  Spades "Because I was Hearts' close confidant, I learned the truth directly from her."

  Clubs "I don't know what to say. My mind is reeling."

  show spades default #as side image"

  Spades "Just don't let her know that we know."

  Spades "She'll only become more difficult, since she can't stand it when someone — {i}anyone{/i} — knows more than she does."

  show clubs default at center

  Clubs "I understand. My lips are sealed regarding this matter."

  Clubs "Thank you for trusting me enough to let me in on this secret."

  jump lbl_037

label lbl_037:

  show spades shock #as side image"

  show clubs shock at center

  "This conversation between Spades and Clubs is abruptly cut short when they hear Diamonds calling for them both."

  "Her voice is coming from the area where the slot machines are located."

  stop music fadeout 1.0

  show spades anxious #as side image"

  show clubs anxious at center

  Spades "How bothersome. What does she want from us?"

  Clubs "Let's go find out."

  jump lbl_038

label lbl_038:

  play music music_slots fadein 2.0

  show bg bg_slots with slow_dissolve

  show spades default #as side image"

  show clubs default at left behind spades with dissolve

  show diamonds default at right behind spades with dissolve

  "Diamonds is standing by one of the slot machines."

  Clubs "Hey, Diamonds. Have you found anything significant?"

  Diamonds "Oh, you bet."

  show spades shock #as side image"

  show clubs shock at left behind spades

  "She lifts her palm to reveal a pulsating organ."

  "One of Hearts' two hearts, to be exact — deep crimson and swathed with congealed blood."

  show spades anxious #as side image"

  show clubs smile at left behind spades

  Clubs "That's amazing, Diamonds!"

  Clubs "Where'd you find this?"

  show clubs default at left behind spades

  "She gazes at the slot machine beside which she stands. She knocks on it, once, with her fist."

  Diamonds "Strangely enough, I suddenly fancied a game of slots."

  Diamonds "My gift of good fortune was as fickle as always. But after a few tries, I successfully spun a triple seven."

  Diamonds "Some secret compartment in the machine popped open. And lo and behold, the heart was inside it."

  Diamonds "I have no idea how it got there or who put it in there. But at least we've found it now."

  show spades mad #as side image"

  Spades "Wait a minute. You {i}suddenly{/i} got the idea to play this slot machine out of nowhere? But why?"

  show diamonds anxious at right behind spades

  Diamonds "This specific slot machine was {i}calling{/i} to me. Saying my name."

  Diamonds "The machine drew me in and made me play it, repeatedly."

  Diamonds "It may sound implausible. I realize that. But I swear by the Two of Diamonds that it's the truth."

  show spades smirk #as side image"

  Spades "Slot machines that can call your name and make you play. What a story."

  Spades "You'd better start inventing better excuses than that, because I don't believe one word of your current explanation."

  show spades mad #as side image"

  show diamonds mad at right behind spades

  "Diamonds only blows out a spectacular sigh, expelling smoke directly over Spades' incredulous expression."

  Diamonds "Why the hell do I need to explain myself to you, anyway?"

  Diamonds "I managed to accomplish something important while you were aimlessly wandering about."

  Diamonds "You should be on your knees thanking me."

  show clubs anxious at left behind spades

  Clubs "Come on, you two. We're all one the same side here."

  Clubs "Let's not argue and accuse each other over every little thing."

  show clubs sad at left behind spades

  show spades anxious #as side image"

  show diamonds anxious at right behind spades

  Clubs "What would Hearts say if she could see us now? She was always attempting to preserve peace among the Suits."

  Clubs "This is no way to honor her memory."

  show spades default #as side image"

  show clubs default at left behind spades

  show diamonds default at right behind spades

  Diamonds "Fine. But I'll need a drink if I have to deal with this deadbeat any longer."

  Spades "I could use a drink myself. Anything to make this woman's voice grate less against my ears."

  show spades anxious #as side image"

  show clubs smile at left behind spades

  show diamonds anxious at right behind spades

  Clubs "Don't you see? It's all about finding the little things we have in common!"

  Clubs "Now we can all relate with one another!"

  stop music fadeout 1.0

  "The other two don't even flicker in response to Clubs' misplaced enthusiasm."

  "They only walk in stony silence."

  jump lbl_039

label lbl_039:

  show bg bg_bar with slow_dissolve

  play music music_bar fadein 2.0

  show spades default #as side image"

  show clubs default at left behind spades with dissolve

  show diamonds default at right behind spades with dissolve

  "The three Suits thus regroup by the bar."

  "Spades' thoughts gravitate toward his favorite brand of brandy, a bottle of which is hidden beneath the counter."

  "Diamonds, however, reaches for the red wine. She fills a third of a goblet, then does the same to two other goblets."

  show diamonds mad at right behind spades

  "As she hands out the drinks, she glares at Spades."

  Diamonds "If you're serious about pitching in, make this your last glass for the day. I mean it, Spades."

  show spades mad #as side image"

  Spades "Yeah, yeah. Just give me a break."

  show diamonds default at right behind spades with dissolve

  "Spades maintains his icy expression even as his insides rejoice at the flavor of wine on his tongue."

  "That inimitable astringency."

  show spades default #as side image"

  "Clubs is swirling the wine around their goblet. Reveling in its scent."

  Clubs "Okay, let's start. What have we found so far?"

  Clubs "We should go about this in an organized fashion. I can explain my findings first."

  Clubs "So I examined the corpse for clues as to why or how the hearts — and no other organs — were removed."

  Diamonds "And? Have you figured it out?"

  Clubs "My primary theory is that someone in the regular business of slicing up bodies, such as a surgeon, was responsible."

  Spades "Yeah, that makes sense."

  show spades anxious #as side image"

  show diamonds anxious at right behind spades

  Clubs "I have another theory, though. One that may account for the fact that Hearts was defeated in the first place."

  Diamonds "Well? Spit it out."

  show clubs anxious at left behind spades

  show spades shock #as side image"

  show diamonds shock at right behind spades

  Clubs "It was dark magic. Witchery aided the commission of the crime."

  "Ominous silence descends over the Suits. Diamonds is the first to break it."

  show spades anxious #as side image"

  show diamonds anxious at right behind spades

  Diamonds "You think the murderer is one of our kind? But I didn't detect any mystical traces."

  Spades "I have to agree with Diamonds here. If it was witchery all along, wouldn't {i}we{/i} be the first to sense it?"

  Clubs "Look at it this way. As far as crimes go, this was the epitome of perfection."

  Clubs "Impeccable execution. No evidence of the perpetrator's identity. No traces suggesting the manner of entry or escape."

  show clubs default at left behind spades

  Clubs "No traces, in fact, that there was a perpetrator at all."

  Clubs "Now don't get me wrong. I am as fond of ordinary humans as either of you."

  show spades default #as side image"

  show diamonds smirk at right behind spades

  Diamonds "So, in other words, you aren't fond of humans at all."

  show clubs smile at left behind spades

  Clubs "Now, now. Don't go putting words into my mouth that I haven't uttered."

  Clubs "They are amusing, if almost willfully blind to the things that transcend their fundamental human realities."

  show clubs default at left behind spades

  show diamonds anxious at right behind spades

  Clubs "But my point is, no matter how flawless a human's plans, there will always be a certain margin for error."

  Clubs "Error doesn't exist here, which leads me to speculate that something beyond the human realm may be at play."

  show spades anxious #as side image"

  Spades "Is that your only basis, then? The lack of any obvious mistakes?"

  Spades "Kind of a flimsy argument, if you ask me."

  Clubs "This is simply an additional possibility for us to consider, nothing more."

  show spades default #as side image"

  show diamonds default at right behind spades

  "Diamonds blows out contemplative rings of smoke."

  Diamonds "Yes, I suppose two theories are better than just the one."

  Diamonds "Not bad, Clubs. You did a surprisingly solid job today."

  show clubs smile at left behind spades

  Clubs "That's high praise indeed, coming from you. You have my gratitude, Diamonds."

  Clubs "I suppose we can discuss the findings of your investigation now."

  show clubs default at left behind spades

  Diamonds "Right. I'll go next."

  if heart_item == True:
    jump lbl_044
  if heart_item == False:
    jump lbl_040

label lbl_040:

  Diamonds "I've noticed other things around the casino, but everything obviously pales in comparison to this."

  "She holds up the heart that she found in the slot machine."

  show clubs smile at left behind spades

  Clubs "Brilliant. Now we only need to find the second heart to proceed with the succession ritual."

  Clubs "Your discovery of the first heart is a milestone indeed. Exceptional investigation work, Diamonds."

  show clubs default at left behind spades

  show diamonds sad at right behind spades

  Diamonds "Truth be told, this is the only discovery that matters to me."

  Diamonds "Whatever my differences with Hearts, I've always recognized that she had a heart of the most precious gold."

  show spades anxious #as side image"

  show clubs sad at left behind spades

  Diamonds "And when you factor in the reality that she had two such golden hearts, her rareness becomes apparent."

  Diamonds "Not just anyone — and perhaps no one ever — can fulfill her role with such benevolence and grace."

  show clubs default at left behind spades

  show diamonds anxious at right behind spades

  "Lips pursed, Diamonds wraps the heart inside her handkerchief."

  "She stashes the heart away before she speaks again, her voice now dripping with bitterness."

  show diamonds sad at right behind spades

  Diamonds "I mean, don't you two get how preposterous this whole business is?"

  Diamonds "We've gathered now to ensure Hearts' replacement, when I know for a fact that this task is impossible."

  Diamonds "Hearts, as we knew her, can never be replaced."

  show spades default #as side image"

  menu:
    "You should comfort her.":
      jump lbl_041
    "Don't. Worst idea ever.":
      jump lbl_042

label lbl_041:

  $ malice_level += 1

  "Soothing gestures help, right? Or at least they did whenever Hearts applied them on Spades."

  "She'd massage his shoulders whilst he was in a state of agitation. With her warm palms, she'd melt his knots of tension into butter."

  "With this in mind, Spades reaches out to rub Diamonds' back."

  show diamonds mad at right behind spades

  show spades shock #as side image"

  "But she jerks away at once, as if the feel of his fingers have scorched her."

  Diamonds "{i}Don't{/i} touch me!"

  Diamonds "I {i}despise{/i} you! You {i}disgust{/i} me!"

  show spades mad #as side image"

  Spades "Calm down. Quit running your mouth."

  Spades "I was trying to be nice for once! What the hell is your problem?"

  Diamonds "You're my problem! Don't you {i}ever{/i} lay a hand on me again!"

  Diamonds "Don't pretend to be a nice guy out of nowhere. I can read you as easily as I would an open book."

  show spades anxious #as side image"

  Diamonds "Your tricks might have worked on Hearts, as magnanimous as she was."

  Diamonds "But you can't fool me. Never me."

  "Clubs cuts in before Spades can launch into his comeback."

  Clubs "Cool it, you two. How many times have you been at each other's throats today?"

  show spades default #as side image"

  show diamonds anxious at right behind spades

  jump lbl_043

label lbl_042:

  "Spades doesn't try to comfort her. He doesn't make a move, doesn't say anything."

  "Luckily, Clubs speaks up, relieving Spades of this bizarre urge to offer empty words of comfort to Diamonds."

  jump lbl_043

label lbl_043:

  Clubs "Listen, Diamonds. I understand that you cared deeply for Hearts, perhaps more than you ever let on when she was alive."

  Clubs "But it wouldn't do to be so pessimistic about her successor before we've even made our selection."

  show diamonds default at right behind spades

  Clubs "We've all got to contribute our best efforts to training the new Hearts as they transition into the role."

  Spades "We're not letting Hanya succeed, then? Do you, like Diamonds, have your suspicions about her?"

  Clubs "We've got to keep our options open. There may be a more suitable candidate out there for Hearts."

  Clubs "However, given her history with Hearts, we can presume that Hanya is safely on the shortlist, at least pending an investigation."

  Clubs "Speaking of investigations, how did yours go, Spades? Did you find anything while you were looking around the casino?"

  jump lbl_048

label lbl_044:

  Diamonds "Check this out."

  "She holds up her hand, which is seemingly holding nothing."

  show clubs anxious at left behind spades

  "Clubs leans in, squinting."

  Clubs "Is that broken glass?"

  "Now that Clubs has mentioned it, Spades detects just the tiniest glints on Diamonds' palm. Microscopic glimmers. "

  show spades anxious #as side image"

  show clubs default at left behind spades

  Spades "Where'd you get that?"

  show diamonds smirk at right behind spades

  Diamonds "I spotted it by the bar while you were boozing. You didn't even notice I was close by, did you?"

  Diamonds "You were far too preoccupied. Searching the bottom of your brandy glass for clues, I suppose."

  show spades mad #as side image"

  Spades "What makes you think I didn't notice you lurking by the bar?"

  Spades "I was ignoring you. I guessed that you were going to pick a fight like you always do."

  show spades default #as side image"

  show clubs anxious at left behind spades

  show diamonds default at right behind spades

  Clubs "Now, now. Let's not get sidetracked."

  Clubs "Diamonds, where'd these bits of glass come from?"

  show clubs default at left behind spades

  "Rather than answering, she deflects the question toward Spades."

  show spades anxious #as side image"

  show diamonds smirk at right behind spades

  Diamonds "So, Spades, you've just bragged to us about your astute powers of observation."

  Diamonds "Apparently, you noticed me standing close by even as you were rambling drunkenly to a brandy bottle."

  Diamonds "Why not grace us with your observational skills? Where do you think these fragments of glass came from?"

  menu:
    "A broken bottle. Or two. Or three.":
      jump lbl_045
    "A broken phone.":
      jump lbl_046

label lbl_045:

  $ malice_level += 1

  show spades default #as side image"

  show diamonds default at right behind spades

  Spades "These bits of glass, they came from a broken bottle. A brandy bottle, or something of that sort."

  Spades "You found them by the bar, after all. It's common sense."

  show spades anxious #as side image"

  show diamonds mad at right behind spades

  Diamonds "Why don't you do me a favor and {i}stop talking,{/i} Spades."

  Diamonds "I feel like I'm losing brain cells just from listening to your blabbering."

  Diamonds "Is your mind even capable of forming thoughts that aren't alcohol-related?"

  show spades default #as side image"

  show diamonds anxious at right behind spades

  Diamonds "These minuscule fragments of glass came from a phone, not from a brandy bottle."

  Diamonds "From Hearts' phone, to be specific. The one Hanya found broken by the roulette table."

  jump lbl_047

label lbl_046:

  show spades default #as side image"

  show diamonds default at right behind spades

  Spades "These bits of glass, they came from a phone."

  Diamonds "Which phone are you talking about?"

  "After a brief pause, Spades responds."

  Spades "Hearts' phone. The one Hanya found broken by the roulette table."

  show diamonds smirk at right behind spades

  Diamonds "Surprise, surprise."

  Diamonds "He's got space in the brain, however small, for something other than booze and bad decisions."

  jump lbl_047

label lbl_047:

  show spades anxious #as side image"

  show clubs anxious at left behind spades

  show diamonds default at right behind spades

  Clubs "So if the phone broke here at the bar, and not by the roulette table, does that mean Hearts was attacked here first?"

  Clubs "No, that's not right. She wasn't {i}attacked.{/i}"

  Clubs "Her body shows no sign of violence — or resistance — aside from the surgical mutilation of her torso."

  Clubs "However, she might have been caught off guard at the bar, which caused her to drop her phone."

  show spades default #as side image"

  show clubs default at left behind spades

  Diamonds "Yes, that's the same theory as mine. Or at least, mostly the same."

  show diamonds anxious at right behind spades

  Diamonds "I doubt that Hearts dropped her phone. With the way the screen shattered, the phone was more likely thrown."

  Diamonds "Or, in line with your theory, Clubs — it may have fragmented directly or collaterally by the force of dark magic."

  show spades anxious #as side image"

  show clubs anxious at left behind spades

  Clubs "So the incident — whatever might have happened — started here, then culminated by the roulette table?"

  Diamonds "Either that, or the entire incident occurred here."

  Diamonds "Her body and her phone might have been transferred postmortem."

  show spades mad #as side image"

  show clubs default at left behind spades

  show diamonds default at right behind spades

  Spades "And how do any of these theories help us find either of the hearts?"

  Spades "Or is this only speculation for the sake of speculation? An intellectual exercise?"

  show spades default #as side image"

  show diamonds smirk at right behind spades

  Diamonds "Well, now. Spades, has your prowling about the casino yielded better results than my own investigation?"

  Diamonds "If you have better clues than mine, which can offer hints as to the hearts' locations, pray let us hear it."

  Diamonds "Clubs and I are listening closely. So shoot."

  show diamonds default at right behind spades

  jump lbl_048

label lbl_048:

  "Now both Diamonds and Clubs are staring silently at Spades."

  "Clubs looks expectant as they await Spades' investigation report."

  "Diamonds, on the other hand, radiates skepticism from her every pore."

  show spades anxious #as side image"

  "Stuck in the spotlight, Spades feels his mouth drying up rapidly."

  "Instinctively, he reaches for the trusty flask stashed in the inner pocket of his blazer."

  "Just a sip. He only requires a sip of whiskey to steady the nerves."

  show diamonds mad at right behind spades

  show spades shock #as side image"

  "He realizes his mistake, however, as Diamonds' eyes narrow with distaste."

  "His hand abandons its journey to the flask, but it's already too late."

  show spades anxious #as side image"

  "Diamonds has noticed what he was trying to do. Both she and Clubs have."

  show diamonds smirk at right behind spades

  Diamonds "Oh, don't stop on our account, Spades."

  Diamonds "If you're going to suckle on your flask as if it's your mother's teat, why not do it without shame?"

  show spades mad #as side image"

  Spades "I wasn't! There was something else I wanted to get from my pocket!"

  Spades "I uncovered an important clue! It would make your findings laughable compared with mine!"

  show spades anxious #as side image"

  show clubs shock at left behind spades

  show diamonds anxious at right behind spades

  Clubs "Wait, you've located a game-changing clue, Spades?"

  Clubs "If you have, you've got to let us know!"

  show clubs anxious at left behind spades

  if heart_item == True:
    jump lbl_049
  if heart_item == False:
    jump lbl_052

label lbl_049:

  menu:
    "You can't reveal what you found.":
      jump lbl_050
    "Or can you?":
      jump lbl_050

label lbl_050:

  "He can {i}never{/i} let them know about what he found at the slots."

  "Spades' Lucky Day, as Hearts dubbed that slot machine. She practically christened it as his and his alone."

  "She taught him all its tricks."

  show diamonds mad at right behind spades

  Diamonds "Well? Don't keep us waiting, Spades."

  Diamonds "What exactly did you discover that would put my own investigative abilities to shame?"

  Diamonds "Why aren't you telling us? Are you lying through your teeth again, just like you always do?"

  Diamonds "You were always too weak to come right out and tell us the truth. You're pathetic."

  show diamonds anxious at right behind spades

  menu:
    "How dare she call you weak?":
      jump lbl_051
    "And pathetic?":
      jump lbl_051

label lbl_051:

  "Spades is ready to cuss her out for these insults, but Clubs comes to his defense just then."

  show clubs default at left behind spades

  Clubs "Take it down a notch, Diamonds. There's no need for name-calling."

  Clubs "If you antagonize Spades, he'll only become more unwilling to cooperate with us."

  show clubs smile at left behind spades

  show diamonds default at right behind spades

  Clubs "Now, Spades. If there's something you need to tell us, just tell us."

  Clubs "You don't have to be afraid. We're not going to judge. We're all friends here, right?"

  show clubs default at left behind spades

  menu:
    "Time to show them your secret.":
      jump lbl_053
    "Do you have a death wish? Don't.":
      jump lbl_054

label lbl_052:

  "What can Spades even say in response to that?"

  "He's found nothing that he can show to the other Suits. Nothing to impress upon them his commitment to their shared goal."

  show clubs default at left behind spades

  show diamonds smirk at right behind spades

  Diamonds "Allow me to hazard a guess."

  Diamonds "You were just as useless as I thought you'd be, and you don't even have the guts to own up to your incompetence."

  show diamonds anxious at right behind spades

  "Unable to disagree with this harsh assessment, Spades can only nod mutely."

  show clubs anxious at left behind spades

  Clubs "Diamonds, come on. You don't have to phrase it so viciously."

  Clubs "Spades is trying his best here, you know? We all are."

  show diamonds mad at right behind spades

  Diamonds "You're way too soft on him."

  Diamonds "If you don't watch out, he's going to treat {i}you{/i} the way he treated Hearts. You'll be his new emotional punching bag."

  show clubs default at left behind spades

  show diamonds default at right behind spades

  jump lbl_055

label lbl_053:

  $heart_show = True

  "Right. It's high time for a revelation."

  show spades mad #as side image"

  Spades "Friends? Whoever said that we're friends?"

  Spades "Haven't you two been judging me and belittling me since we got here?"

  show clubs anxious at left behind spades

  show diamonds anxious at right behind spades

  Spades "We all know that Diamonds can't stand me."

  Spades "And as for you, Clubs? You only tolerate me, at most."

  Spades "Hearts was the only one who accepted me for who I was. She alone believed in me."

  show spades anxious #as side image"

  show clubs sad at left behind spades

  Clubs "That's not true. You don't think I believe in you too? Because I do."

  show spades anxious #as side image"

  Spades "You believe in me? You have faith in me?"

  Clubs "That's what I'm saying."

  show clubs anxious at left behind spades

  Spades "Then you'll believe me when I say I found {i}this{/i} lying by the slot machines?"

  show spades creepy #as side image"

  "Without further ado, he presents them both with the prize he retrieved upon hitting triple sevens on Spades' Lucky Day."

  show clubs shock at left behind spades

  show diamonds shock at right behind spades

  "On his palm is an organ palpitating, even though it's long been separated from the rest of its body."

  "One of Hearts' two hearts, to be specific — dark crimson and coated with congealed blood."

  show spades default #as side image"

  "The two other Suits stare mutely for a while, dumbfounded."

  show clubs anxious at left behind spades

  show diamonds anxious at right behind spades

  "Then Diamonds breaks the silence, all in a fevered rush."

  Diamonds "Where in the blazes did you find this?"

  show spades anxious #as side image"

  Spades "Didn't I just tell you?"

  "Diamonds takes a step forward, as if about to snatch up the heart and keep it for herself."

  "Before she can do that, however, Spades stashes it away once more."

  Spades "I'm keeping it safe. It's evidence, so we shouldn't have too many fingerprints on it."

  Diamonds "But —"

  "He holds up his palm, flecked with blood, to silence her."

  jump lbl_055

label lbl_054:

  show spades default #as side image"

  "He can't show them {i}that.{/i} No way."

  "How would they even react if they saw that?"

  show spades mad #as side image"

  Spades "Fine, I'll admit it. I was bluffing."

  Spades "But only because Diamonds kept provoking me!"

  Spades "I found absolutely nothing of value. Happy now?"

  show spades default #as side image"

  show clubs anxious at left behind spades

  show diamonds smirk at right behind spades

  Diamonds "As expected. You're nothing if not laughably predictable."

  Clubs "Hey, at least he openly admitted to his momentary indiscretion. That took a lot of guts."

  show clubs default at left behind spades

  show diamonds mad at right behind spades

  Diamonds "You're giving him too much credit. He had nothing to show us."

  Diamonds "What other choice did he have except to own up to his dishonesty?"

  show diamonds default at right behind spades

  jump lbl_055

label lbl_055:

  show spades shock #as side image"

  "Just then, Spades feels a conspicuous shifting inside his body."

  "Something's stirring deep within, as if attempting to clamber up to freedom."

  show spades anxious #as side image"

  "He's got to get away now. He's got to sort himself out."

  stop music fadeout 1.0

  show clubs shock at left behind spades

  show diamonds shock at right behind spades

  Spades "Excuse me. I need some time alone."

  "He dashes off then, before either Diamonds or Clubs can question him or protest."

  hide clubs

  hide diamonds

  play music music_roulette fadein 2.0

  show bg bg_roulette with slow_dissolve

  "Away from the Suits now, he retches, again and again."

  "He's struggling in vain to expel the squirming contents of his abdomen."

  "Portions of his gastrointestinal tract — more particularly, from his esophagus to his stomach — feel as if they're aflame."

  "And is there any better way to quell the fire of pain, than to meet it with a fire of another sort?"

  "Nothing but the welcome scorch of liquor can soothe the bruised-up, battered feeling of his body."

  if intoxication == True:
    jump lbl_056
  if intoxication == False:
    jump lbl_057

label lbl_056:

  "Yes, why not indulge in his thirst, especially if it's his only hope of dulling the disobedience within?"

  "Didn't he down a half-bottle of brandy earlier? Didn't he binge much more than that, only last night?"

  show spades smirk #as side image"

  "Surely, another drink won't kill him!"

  "With this reasoning in mind, he snatches the flask of whiskey from the inner pocket of his blazer."

  "Greedily, he unscrews the cap and guzzles its contents."

  "There's no one who can stop him now."

  show spades anxious #as side image"

  "Before too long, the flask is dry as bone."

  Spades "Already? Nothing good ever stays, huh?"

  "Grunting in annoyance, he returns the emptied flask to his pocket."

  show spades default #as side image"

  "Surprise, surprise. The alcohol is doing nothing to neutralize his aches."

  jump lbl_058

label lbl_057:

  "But as much as he wishes he could drink, he understands that he shouldn't."

  "Too many times in recent memory, he's succumbed to this unquenchable thirst for {i}more.{/i}"

  "There was the brandy he drank at the bar. Then the goblet of wine that Diamonds gave him."

  "But nothing looms as prominently over his head as last night's binge. He regrets that session most of all."

  show spades default #as side image"

  "So he leaves his full flask of whiskey where it is. He can't afford to fog up his mind any further."

  "Deprived of his usual panacea, he simply has to live with this pain."

  jump lbl_058

label lbl_058:

  "This writhing feeling in his gut, it only seems to worsen with time."

  "As he desperately tries to will the agony away, he screws his eyes shut."

  hide spades

  show bg bg_darkness with slow_dissolve

  "Was he a fool to come here all along?"

  "To pretend that nothing, aside from the obvious, is terribly wrong?"

  menu:
    "A fool indeed.":
      jump lbl_060
    "Folly of the highest order.":
      jump lbl_059

label lbl_059:

  $ malice_level += 1

  jump lbl_060

label lbl_060:

  "He briefly opens his eyes."

  show bg bg_roulette_missing with slow_dissolve

  show spades mad #as side image"

  Spades "As I've said many times before, your commentary is unwelcome."

  Spades "If I'm a fool, then let me be a fool in blissful ignorance."

  "With a groan, he once more closes his eyes."

  hide spades

  show bg bg_darkness with slow_dissolve

  menu:
    "Hey, Spades.":
      jump lbl_061
    "Listen up, Spades.":
      jump lbl_061

label lbl_061:

  "He opens his eyes a second time."

  show bg bg_roulette_missing with slow_dissolve

  show spades mad #as side image"

  Spades "What now? What the hell do you want?"

  Spades "Can't you see I'm having the worst day of my life here?"

  Spades "When am I ever going to catch a goddamn break?"

  "He shuts his eyes again."

  hide spades

  show bg bg_darkness with slow_dissolve

  menu:
    "Spades, didn't you notice?":
      jump lbl_062
    "Can't you see that something's missing?":
      jump lbl_062

label lbl_062:

  Spades "Missing?"

  Spades "What's missing?"

  menu:
    "The corpse of Hearts is gone.":
      jump lbl_063
    "What if she's alive?":
      jump lbl_063

label lbl_063:

  Spades "Hearts is missing? She's {i}alive?{/i}"

  Spades "No. That's impossible."

  Spades "She's been lying there, heartless, against the roulette table all morning."

  Spades "Not even a Suit could survive such extensive injuries to the torso. There's no way."

  menu:
    "If you're so sure, why not open your eyes?":
      jump lbl_065
    "See the damage you're powerless to reverse.":
      jump lbl_064

label lbl_064:

  $ malice_level += 1

  jump lbl_065

label lbl_065:

  Spades "I'm shaking all over."

  Spades "I feel like I might shatter into a million pieces at any moment."

  Spades "Is this what fear feels like? Am I actually afraid?"

  Spades "Maybe I should never open my eyes again. Maybe then I'll be safe."

  menu:
    "You can't hide out in darkness forever.":
      jump lbl_067
    "If only you could. You'd be doing the world a favor.":
      jump lbl_066

label lbl_066:

  $ malice_level += 1

  jump lbl_067

label lbl_067:

  Spades "No, I can't accept that this is happening."

  Spades "Please let there be nothing wrong. Please."

  Spades "When I open my eyes, the corpse will be in the same place it's been. Looking the same as it did."

  Spades "Please."

  Spades "Well, I guess I can't delay this forever."

  Spades "Here goes nothing."

  "And so he opens his eyes."

  if malice_level >= 7:
    jump lbl_068
  if malice_level < 7:
    jump lbl_076

label lbl_068:

  show bg bg_roulette with slow_dissolve

  show spades default #as side image"

  Spades "Huh. The corpse isn't missing."

  Spades "Hearts is right here, just as she's been this whole morning."

  show spades mad #as side image"

  Spades "Then you were messing with me, after all?"

  Spades "I've got enough crap to deal with, even without your sadistic games!"

  menu:
    "Why would I lie to the world's biggest liar?":
      jump lbl_069
    "Something sinister is afoot.":
      jump lbl_069

label lbl_069:

  Spades "I don't believe you."

  Spades "I'm not listening to you anymore. So don't even bother trying."

  menu:
    "Suit yourself.":
      jump lbl_070
    "For her, I'll watch you burn in hell.":
      jump lbl_070

label lbl_070:

  show spades anxious #as side image"

  Spades "Enough of this."

  Spades "If I'm ending up in hell anyway, I may as well earn my one-way ticket."

  Spades "I've gone this far already. My stomach seems to have settled, so I should finish what I've started."

  Spades "It's time to take matters in my own hands."

  show spades default #as side image"

  jump lbl_071

label lbl_071:

  "Taking a deep breath, he holds out both of his palms."

  "He waits patiently for the telltale tingling of witchery on his fingertips."

  "Only then does he commence to test his strength."

  "Tentatively, he pinches at the air just above his palms."

  Spades "Oh, malignancy. Don't fail me now."

  if malice_level >= 7:
    jump lbl_072
  if malice_level < 7:
    jump lbl_080

label lbl_072:

  "He succeeds in grasping the otherwise intangible matter by his fingertips."

  "He tugs on the air as if it's fabric, and everything within a certain radius around him shifts subtly in response to this manipulation."

  show spades smirk #as side image"

  Spades "I knew it."

  Spades "I could sense its weight, as dense as it's invisible."

  Spades "Building, building, building."

  Spades "Awaiting the right moment — the right targets — to explode once more."

  Spades "Perhaps this is an aftershock of sorts?"

  Spades "So why don't we show Diamonds and Clubs what we can do together?"

  hide spades

  stop music fadeout 1.0

  show bg bg_darkness with slow_dissolve

  "Here's what he learns from his encounter with the Suits."

  "A beating heart can either be weaponry or a blessing depending on its wielder."

  "The full spectrum of emotions — from horror to sorrow to bliss — can just as easily aid the forces of benevolence as their reverse."

  play music music_bar fadein 2.0

  show bg bg_bar with slow_dissolve

  show spades creepy #as side image"

  "When a spree attains its sweet spot, he tends to get in this particular mood."

  "Waxing poetic about the most artless matters as he sips on his liquor."

  "Engaging in philosophical debate with his most intimate — no, his {i}only{/i} — confidant."

  "But now that she's gone and he's alone again, he can only ramble to an audience of one. Himself."

  stop music fadeout 1.0

  show spades anxious #as side image"

  Spades "No, that's not true, is it?"

  Spades "I've got you. You're still here, aren't you?"

  menu:
    ". . .":
      jump lbl_073

label lbl_073:

  hide spades

  play music music_reveal fadein 2.0

  scene cg cg_hands_bloody with slow_dissolve

  Spades "Hearts is gone."

  Spades "And now Diamonds and Clubs are too."

  Spades "But you? You'll never leave me alone, whether I want you here or not."

  Spades "Since we're stuck together from now on, why don't we learn to get along?"

  menu:
    ". . .":
      jump lbl_074

label lbl_074:

  Spades "What's this? Haven't you been talking my ear off all this time?"

  Spades "{i}Now{/i} you're not going to say anything? Now that it's all over and everyone else has left us behind?"

  menu:
    ". . .":
      jump lbl_075

label lbl_075:

  Spades "Ah, the silent treatment. I understand."

  Spades "After all I've done — and how awful I've been to you — I get why you're upset with me."

  Spades "But guess what? No matter how much you hate me, I can't say the same about you."

  Spades "Quite the contrary, actually."

  Spades "I didn't feel it for Hearts herself, I admit it. But now I feel it for you."

  Spades "I love you."

  Spades "I'm not ashamed to confess that."

  Spades "You weren't mine at first, but perhaps I always sensed that we belonged together."

  Spades "And so I stole you from Hearts' chest to occupy the hole in my own."

  Spades "You're inside me now. You're making me feel things I've never felt before."

  Spades "I finally understand it — why everyone around me took pleasure in such illogical, irrational behavior."

  Spades "What a rush, isn't it, to want someone so badly that you'll swallow them alive and whole."

  Spades "Now here we are. You're a part of me, and I'm the lord that rules you."

  Spades "Today is momentous, to be sure, but it's only the first day of the rest of our entwined lives."

  Spades "Imagine all that we can do together. With our combined forces, we'd be unstoppable."

  Spades "Are you ready for all that?"

  scene cg cg_ending03 with slow_dissolve
  $ persistent.ending_seen_03 = True
  pause
  jump lbl_credits

  return

label lbl_076:

  stop music fadeout 1.0

  show bg bg_roulette_creepy

  show spades shock #as side image"

  "Spades' mouth falls open."

  "He's stunned into silence by the sinister sight before him."

  if heart_item == True:
    jump lbl_077
  if heart_item == False:
    jump lbl_088

label lbl_077:

  play music music_nightmare fadein 2.0

  show spades anxious #as side image"

  "And even when he eventually attempts to speak, he can't utter anything approaching coherence."

  "There's the horrible noise of retching instead, as the monsoon brewing inside him spills over. Finally flooding free."

  "With a torturous heave, he vomits out the thing that's been clawing its way up his throat this entire time."

  "Swift as can be, he catches the cursed object in his fist."

  show spades creepy #as side image"

  "Hearts' second heart."

  "It's smaller than her other one. A runt among hearts."

  "But despite its diminutive size, it's got twice as much energy."

  "It's much louder than an ordinary human conscience has any right to be."

  "Trapped for so long in a body where it doesn't belong, the heart thrashes violently against Spades' grasp."

  "It's trying to get as far away as possible from Spades, for at least two reasons."

  "First and foremost, it yearns to be reunited with its twin."

  "Second, it wishes to escape the poison flowing in Spades' bloodstream, which has been incrementally corrupting its purity."

  show spades mad #as side image"

  "Spades only glares at the pulsing organ. The more it thrashes against his hand, the more he tightens his grip around it."

  Spades "I gave you a new home, and this is how you repay me? Ungrateful brute."

  Spades "You'll learn to love your new cage, sooner or later. Just try harder."

  menu:
    "Let me go!":
      jump lbl_078
    "You monster!":
      jump lbl_078

label lbl_078:

  show spades default #as side image"

  "Ignoring these demands, Spades binds the second heart to submission with some twine."

  "He then hides it in his pocket."

  stop music fadeout 1.0

  "He'll take another stab at swallowing the heart later."

  "For now, though, he's got to pinpoint his attention on more pressing matters."

  play music music_roulette fadein 2.0

  show spades anxious #as side image"

  "Unwillingly, he lets his gaze wander back toward Hearts' corpse."

  "The mere sight of it — desecrated by forces or persons unknown — causes tears to spring from his eyes."

  jump lbl_079

label lbl_079:

  stop music fadeout 1.0

  show spades cry #as side image"

  Spades "Oh, Hearts. Who did this to you?"

  Spades "Who bastardized your memory this badly?"

  play music music_flashback fadein 2.0

  Spades "As for me, I only did what I had to. You know I did."

  Spades "But you know I would never defile you like this. Taint your beauty like this."

  show spades creepy #as side image"

  Spades "Cross my heart, Hearts. I won't let your legacy go to waste."

  Spades "I'm going to finish what I started. I'll make the most of everything you taught me."

  Spades "Everything you gave me, sacrificed for me."

  Spades "I'll create something beautiful and new from the pieces that you left behind. Mark my words."

  show spades default #as side image"

  Spades "But first things first. Whatever it is that I need to do, one thing's for sure."

  stop music fadeout 1.0

  Spades "Everything would go so much more smoothly if my magic would just cooperate with me. I've got to get it under control."

  Spades "Let's give it a shot, shall we?"

  play music music_roulette fadein 2.0

  jump lbl_071

label lbl_080:

  "He continues grasping at thin air, but he only feels as if he's grasping at straws."

  "Nothing is happening."

  "A minute passes, then the prickling sensation on his fingertips fades."

  show spades anxious #as side image"

  Spades "Well, that was a bust."

  Spades "I guess I can't rely on my usual tricks, at least for the time being."

  Spades "But that's the way it is. That's the way it's always been."

  Spades "The witchery of the Suits is as flighty as your average woman."

  show spades default #as side image"

  if heart_item == True:
    jump lbl_081
  if heart_item == False:
    jump lbl_089

label lbl_081:

  Spades "On the plus side, though, I do have the trump cards that the other two Suits sorely desire."

  "From his pocket, Spades unveils the two hearts missing from Hearts' body."

  Spades "But I can't just ingest one of these organs without taking any further steps to retain it."

  Spades "I've already established that, once I swallow a heart, my body will reject the foreign object within hours."

  if heart_show == True:
    jump lbl_085
  if heart_show == False:
    jump lbl_082

label lbl_082:

  "But even as his lips utter this fact aloud, his brain is sprinting ahead."

  show spades shock #as side image"

  "He's formulating a whole new theory, with practically no legs to stand on."

  Spades "Hey! What if I try swallowing {i}both of them{/i} at the same time?"

  show spades smirk #as side image"

  Spades "The two hearts were meant to coexist in harmony within a single body, weren't they?"

  Spades "If separated from its sibling, a heart will rebel against me!"

  Spades "That's it! That's got to be the reason I suffered so much after ingesting one heart!"

  menu:
    "Hate to burst your bubble.":
      jump lbl_083
    "But your theory makes no sense.":
      jump lbl_083

label lbl_083:

  "Spades isn't listening. His eyes are gleaming with child-like excitement."

  "For once, his greed isn't directed toward a bottle of alcohol. He's staring hungrily at the two hearts."

  Spades "I should try it, shouldn't I? For the sake of science."

  menu:
    "Don't you even dare!":
      jump lbl_084
    "I'll kill you if you eat me again!":
      jump lbl_084

label lbl_084:

  stop music fadeout 1.0

  "But it's too late."

  "Without heeding these warnings, Spades stuffs both of the hearts into his mouth — one after the other — and swallows."

  play music music_nightmare fadein 2.0

  show spades creepy #as side image"

  "For a brief moment, at least, it's an immaculate state of being."

  "He feels complete. Or perhaps even more than that — he feels {i}full{/i}."

  "He feels every swing of mood and every flame of passion that a human or a demigod has ever gone through."

  "He's brimming over with wave upon wave of undiluted emotion."

  "More emotion, in fact, than any being — other than the rightful successor of Hearts' mandate — can bear without breaking."

  show spades shock #as side image"

  "And break he does."

  "He falls to his knees just as his body begins to savagely mutate."

  hide spades

  "He's morphing into shapes beyond his control. Approximations of human beings, as drawn by an alien's hand."

  "Repeatedly, he undergoes the agony of successive transformations."

  "His final form is a monster, of course."

  "A beast with teeth as toxic as fairytale fruit and skin as fragile as glass."

  scene cg cg_ending02 with slow_dissolve
  $ persistent.ending_seen_02 = True
  pause
  jump lbl_credits

label lbl_085:

  show spades anxious #as side image"

  Spades "So what should I do now?"

  Spades "The other Suits have found out that I'm holding one of the hearts."

  "Sighing with exasperation, he places both hearts safely inside his pocket again."

  show spades mad #as side image"

  Spades "What in the world was I thinking when I admitted that fact to them?"

  Spades "Why did I confess to something so incriminating?"

  Spades "Am I going senile or something, even though the Suits don't even age?"

  menu:
    "Maybe it was all the liquor you drank?":
      jump lbl_086
    "Booze and bad decisions go hand in hand.":
      jump lbl_086

label lbl_086:

  "Spades parts his mouth, perhaps to protest over these digs against his substance abuse problems."

  show clubs default at left behind spades with dissolve

  show diamonds default at right behind spades with dissolve

  show spades shock #as side image"

  "He is, however, interrupted by the arrivals of Diamonds and Clubs."

  "They come with penetrating stares and tight-lipped expressions."

  show clubs shock at left behind spades

  show diamonds shock at right behind spades

  "But their mouths fall open in unison upon sighting the eerie new appearance of Hearts' corpse."

  Diamonds "What happened to Hearts? What taboo curse did you place upon her body?"

  show spades anxious #as side image"

  show clubs anxious at left behind spades

  show diamonds anxious at right behind spades

  Spades "There's no way I did this! So let me ask you the same question."

  Spades "What are you doing here, anyhow?"

  show diamonds mad at right behind spades

  Diamonds "What do you think we're doing here?"

  Diamonds "You can't just drop a bomb like that and walk away! You'd better explain exactly how you found that heart."

  Diamonds "Depending on your answer, Clubs and I might have a whole slew of follow-up questions for you."

  show spades mad #as side image"

  Spades "I already told you. I found the heart by the slot machines."

  Spades "What more do you want from me, woman? A sworn statement signed in blood?"

  Diamonds "Liar. I don't believe a single stinking word you say."

  show spades anxious #as side image"

  show diamonds anxious at right behind spades

  Diamonds "While you were wasting time drinking at the bar, I investigated the area with the slot machines."

  Diamonds "I scanned every single machine. This strange feeling kept drawing me back to them."

  Diamonds "But I saw nothing there. How could you — bumbling around drunk — find something I missed?"

  show diamonds default at right behind spades

  show clubs sad at left behind spades

  Clubs "Listen, Spades. I'd give anything not to think of you as someone who could do something like {i}that{/i} to Hearts."

  Clubs "But, to be perfectly honest, the situation isn't looking good for you right now."

  Clubs "As much as I'd hate to go against you, I might not have a choice this time."

  show spades mad #as side image"

  Spades "Is that a threat?"

  show clubs default at left behind spades

  Clubs "Spades, I can't permit anyone to disrupt the delicate balance of the Suits. Not even you."

  show spades anxious #as side image"

  Spades "Clubs, don't do this. Didn't you say earlier that you believed in me?"

  Spades "Why would I lie about something so crucial?"

  Spades "Besides, don't you think I could come up with a much better lie than that? Come on."

  Spades "Above all else, don't you know that I cared deeply about Hearts?"

  Spades "You know that I would {i}never{/i} do anything to hurt her, let alone cut up her body like that."

  Spades "You know me. And I know you. I know that, deep down, you want to be on my side."

  show diamonds anxious at right behind spades

  Spades "But Diamonds has been poisoning you against me. She's the one who's feeding you these lies."

  Spades "Don't believe a word she says."

  show diamonds smirk at right behind spades

  Diamonds "Oh, wow. Do you really want to go there?"

  Diamonds "You're really going to try to turn Clubs against me when you're the one who murdered Hearts in cold blood?"

  show spades mad #as side image"

  Spades "You've got no proof. Quit putting the blame on me to cover up for your crime."

  show diamonds mad at right behind spades

  Diamonds "{i}You{/i} should quit putting the blame on {i}me{/i} to cover up for {i}your{/i} crime!"

  Diamonds "I can't believe you would accuse me! Me, of all damn people in the world!"

  Diamonds "As if I would ever lay a hand on Hearts! I would never! Not in this lifetime or the next!"

  Diamonds "I {i}loved{/i} her, for crying out loud! I {i}loved{/i} her with my entire heart!"

  Spades "I loved her too. Even though I was born without a heart."

  Diamonds "But that's {i}exactly{/i} what sets us apart, isn't it?"

  Diamonds "I may not be the most sentimental person in the world, but I understand what it means to love someone."

  Diamonds "Can you ever say the same?"

  show clubs anxious at left behind spades

  "Clubs watches silently as the two continue volleying insults and accusations back and forth."

  "Eventually, the time will come when Clubs has to choose a side, as between the two opposing Suits."

  "And when Clubs does, they'll go with their gut."

  hide spades

  hide clubs

  hide diamonds

  stop music fadeout 1.0

  show bg bg_darkness with slow_dissolve

  "She puts up a valiant fight, to be sure, but falls soon enough."

  "How can she not, when she's up against the combined forces of the other Suits?"

  "How can anyone prevail against the razor-sharp precision of Spades and the anvil-heavy strength of Clubs?"

  play music music_reveal fadein 2.0

  "But the sight of her body on the floor — brutalized and lifeless as her love now — brings Clubs back to reality."

  "This reality, when freed from the distortions of Spades' spiking malice, is harsh indeed."

  "Clubs flees, as if unable to bear staring for even a second more at what they've done to Diamonds."

  show bg bg_bar with slow_dissolve

  show spades creepy #as side image"

  Spades "I wonder where Clubs ran off to?"

  Spades "I'll have to hunt them down, sooner or later. How troublesome."

  Spades "But for now, a drink is in order. I could definitely use one."

  hide spades

  scene cg cg_hands_bloody with slow_dissolve

  Spades "Nothing like a brandy to cap off a long, draining day."

  "He downs on his drink, then smacks his lips with relish."

  menu:
    "I can't believe you killed Diamonds too.":
      jump lbl_087
    "Leave Clubs alone. Please.":
      jump lbl_087

label lbl_087:

  Spades "Oh, please. If you're planning to go all accusatory on me, at least get your facts straight."

  Spades "It was Clubs who dealt the killing blow on Diamonds."

  Spades "It's not as if Clubs is some saint that you need to protect. It's only fair to make them pay for their crime too."

  Spades "Murder is no joke, you know?"

  Spades "But let's not talk about such tiresome things. For now, I just want to drink and unwind."

  "Alone in the casino now, Spades pours himself another glass of brandy."

  "He'd toast to the memories of the recently fallen, but there's no one for him to toast with anymore."

  scene cg cg_ending04 with slow_dissolve
  $ persistent.ending_seen_04 = True
  pause
  jump lbl_credits

label lbl_088:

  play music music_roulette fadein 2.0

  show spades anxious #as side image"

  "His voice is full of agony when he eventually regains his ability to speak."

  "Just the sight of Hearts' dishonored corpse is enough for tears to leak from the corners of his eyes."

  jump lbl_079

label lbl_089:

  Spades "So now what?"

  Spades "I've got to focus on acquiring that heart. That should be my top priority."

  Spades "Given my current state, it's not going to be easy."

  stop music fadeout 1.0

  Spades "But I have to try, right?"

  Spades "Let's go."

  play music music_bar fadein 2.0

  show bg bg_bar with slow_dissolve

  "The bar is deserted."

  Spades "I wonder where Diamonds and Clubs went."

  "He should go and search for them. He knows this."

  "He's sidetracked, however, by this chance to quench his thirst once more."

  "How can he resist those bottles, arranged in such an inviting display behind the counter?"

  show spades anxious #as side image"

  Spades "Perhaps I should stop for a drink."

  Spades "With the additional liquid courage in me, I can take on anything and anyone in the world."

  menu:
    "How about no?":
      jump lbl_090
    "How about we move on?":
      jump lbl_090

label lbl_090:

  show spades mad #as side image"

  Spades "How about you shut up?"

  Spades "I wasn't asking for your input."

  show spades default #as side image"

  if intoxication == True:
    jump lbl_092
  if intoxication == False:
    jump lbl_091

label lbl_091:

  Spades "As it happens, I've already changed my mind. I'm deciding not to drink."

  Spades "Earlier, I was able to stop myself from going overboard with the brandy."

  Spades "I've got to keep up this brand new attitude. I can't afford to get sidetracked."

  Spades "Once the day's done and I've accomplished everything I've set out to do, then I can celebrate as much as I want."

  stop music fadeout 1.0

  Spades "Now where should I go next?"

  Spades "Ah, the area with the slot machines might be a good idea."

  play music music_slots fadein 2.0

  show bg bg_slots with slow_dissolve

  show spades anxious #as side image"

  "As he marches down a row of slot machines, he begins to repeat three words under his breath, again and again and again."

  "He clings to them as if they're a magical incantation."

  Spades "{i}Spades' Lucky Day. Spades' Lucky Day. Spades' Lucky Day.{/i}"

  show spades default #as side image"

  "He can't wait to be blessed with any miracles. Neither can he fall back on the whims of witchery."

  "If he wants today to be his lucky day, he needs to make it happen with his own two hands."

  show spades shock #as side image"

  show clubs shock at center

  "As he reaches the end of the row, he bumps into someone."

  Clubs "Spades! You don't know how glad I am that I ran into you!"

  show clubs anxious at center

  show spades anxious #as side image"

  Spades "What's going on? Where's Diamonds?"

  "Clubs is fidgeting, for some reason."

  Clubs "Uh, you might hate me if I answer that question honestly."

  Spades "Hate you? Of course I won't hate you. I could never."

  Spades "Just tell me what the problem is."

  Clubs "It's about Diamonds."

  Clubs "She's in the casino's back office right now. And, um, she's handcuffed securely."

  show spades shock #as side image"

  Spades "Handcuffed? But why?"

  show clubs sad at center

  Clubs "I suspect that she's been the culprit all along."

  Clubs "The one who both murdered Hearts and hid the two hearts, I mean."

  show clubs default at center

  show spades anxious #as side image"

  Spades "I've had my suspicions about her too, to be perfectly honest with you."

  Spades "I'm curious, though. I wonder whether our reasoning is the same. What made you suspect her?"

  show spades default #as side image"

  Clubs "Well, do you remember what I mentioned about Hearts' potential manner of death?"

  Spades "Yeah. You were theorizing that this crime was committed using dark magic."

  Clubs "Indeed. I stand by that theory."

  Clubs "Diamonds is a powerful witch. Committing a murder of this sort is certainly within her wheelhouse."

  Spades "Oh, definitely. That's a solid point."

  Clubs "And that story of hers — the one about the slot machine calling out her name — was too outlandish for me."

  Clubs "When you pointed out how preposterous she sounded, I secretly agreed with your assessment."

  show clubs anxious at center

  Clubs "If her story was fabricated, then that can only mean that she obtained the heart by some other manner."

  Clubs "So I believe that she was the one who killed Hearts and who hid the two hearts."

  Clubs "And now she's been spitting out lie after lie to cover up her tracks."

  show clubs default at center

  Clubs "This is simply unacceptable."

  Spades "I'm with you on that. Diamonds is definitely the most likely suspect."

  show clubs smile at center

  Clubs "You agree with me, then? You think she killed Hearts too?"

  Spades "Absolutely. Your reasoning is right on the money."

  show clubs default at center

  show spades anxious #as side image"

  Spades "Do you want us to interrogate her now?"

  Spades "She might try to be evasive about certain things, like the location of the second heart."

  Spades "But you don't have to worry about that. I have ways of making people talk."

  show spades default #as side image"

  show clubs smile at center

  Clubs "That's perfect! I knew I could count on you, Spades."

  Clubs "Truth be told, I was worried that I'd been too hasty in accusing Diamonds of such a heinous crime."

  Clubs "But with your vote of confidence, I no longer have any doubts."

  show spades smirk #as side image"

  Spades "Of course. I'm always here for you."

  Spades "The task at hand may seem unsavory on the surface, but that won't matter as long as we adopt the right frame of mind."

  Spades "What's important is that we're doing this together. Let's go, Clubs."

  scene cg cg_ending05 with slow_dissolve
  $ persistent.ending_seen_05 = True
  pause
  jump lbl_credits

label lbl_092:

  Spades "It's not like I have any idea where those two are anyway."

  Spades "Won't it be pointless to wander around without knowing where to go?"

  Spades "I may as well wait here. They'll have to swing by this area sooner or later."

  show spades smirk #as side image"

  Spades "Besides, one glass isn't going to hurt anyone. "

  "Even as he says this, he's already pouring himself a drink."

  menu:
    "You think you're going to stop at one?":
      jump lbl_093
    "I foresee many more glasses in your future.":
      jump lbl_093

label lbl_093:

  show spades default #as side image"

  "Tossing back the liquor with wild abandon, he swallows the lot with one gigantic gulp."

  "He slams down the empty glass on the counter."

  show spades smirk #as side image"

  Spades "Now that was a good dose of liquid courage."

  Spades "But I need a teensy bit more to face the rest of the day. Just a smidge."

  menu:
    "What did I tell you?":
      jump lbl_094
    "I'm psychic.":
      jump lbl_094

label lbl_094:

  "He snorts as he's pouring himself a second glass."

  Spades "I'll drink as many glasses as it takes for you to shut your trap. How about that?"

  show spades default #as side image"

  menu:
    "Let the game begin.":
      jump lbl_095
    "In this game, you always lose.":
      jump lbl_095

label lbl_095:

  stop music fadeout 1.0

  hide spades

  show bg bg_darkness with slow_dissolve

  "His alcohol-induced slumber is dreamless."

  "Whatever monsters lurk in the darkness within his skull, they're kept temporarily at bay by his bone-deep exhaustion."

  play music music_reveal fadein 2.0

  show bg bg_bar with slow_dissolve

  show spades anxious #as side image"

  "He stirs awake with the worst migraine of his life."

  Spades "Ugh."

  Spades "Aspirin."

  Spades "Somebody, anybody. Get me some aspirin."

  "As disoriented as he is, it takes a few seconds for what's happening to sink in."

  show spades shock #as side image"

  "His wrists are bound by silver handcuffs."

  show clubs default at left behind spades with dissolve

  show diamonds default at right behind spades with dissolve

  "To make matters worse, the two Suits are looming over him."

  "They're staring down at his slumped position over the bar counter."

  show spades mad #as side image"

  Spades "What in the hell is going on?"

  Spades "Take off these handcuffs! Now!"

  show clubs anxious at left behind spades

  "Clubs' voice is somber."

  Clubs "We can't let you go, Spades. Not now, not ever."

  Spades "But why? Don't I at least deserve an explanation?"

  show spades anxious #as side image"

  show clubs default at left behind spades

  show diamonds anxious at right behind spades

  Diamonds "You see, Spades, you threw up a very interesting object while you were asleep."

  "Just as she lifts up her palm to show him something, she exhales a plume of smoke which temporarily impairs his sight."

  show spades shock #as side image"

  show diamonds default at right behind spades

  "When the smoke clears and the identity of the object becomes apparent, he gasps."

  Spades "No. I can't believe this. {i}No.{/i}"

  show spades anxious #as side image"

  show diamonds anxious at right behind spades

  Diamonds "That was how we reacted too. But I'm willing to bet you know more about this than we do."

  Diamonds "Better start talking. As Clubs said, we're not planning to let you go."

  scene cg cg_ending06 with slow_dissolve
  $ persistent.ending_seen_06 = True
  pause
  jump lbl_credits

init:
    #image cred = Text("{color=#ffffff}[gui.about!t]\n\nMade with Ren'Py [renpy.version_only]{/color}", text_align=0.5, xmaximum=1200)
    image cred = Text("[gui.about!t]\n\nMade with Ren'Py [renpy.version_only]", text_align=0.5, xmaximum=1200)
    image theend = Text("{size=80}Fin", text_align=0.5)
    image thanks = Text("{size=80}Thanks for playing!", text_align=0.5)

label lbl_credits_from_menu:
    call lbl_credits from _call_lbl_credits
    return
    
label lbl_credits:
        
    if (_in_replay):
        play music music_ending fadein 1.0
    else:
        play music music_ending fadein 1.0

    $ quick_menu = False

    $ credits_speed = 20
    scene bg black
    with dissolve
    show cred at Move((0.5, 1.9), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    
    $ renpy.end_replay()
    
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks with dissolve

    if persistent.extras_unlocked:

        pass

    else:

        centered "You've unlocked the Extras Menu.\nAccess it through the Main Menu."

        $ persistent.extras_unlocked = True
        
    $ quick_menu = True

    return


