
    
label lbl_introduction:
    #Introduction
    #[FINAL]
    #[Any line without a character name/letter abbreviation ([M], [L], [V], etc) is a thought by Merona, so please voice those thoughts as well. Every space is a new textbox.]
    #------------------------------------
    scene cg intro1 with fade
    #show sunrays movie
    play music music_newBegin
    #TODO: something with leaves? 
    show leaf1 at leafspin
    show leaf2 at leafspin2
    show leaf1_small at leafspin3
    show leaf2_small at leafspin4
    "It's no secret that the forest is brimming with life."
    "Of course, everybody knows that; plants and animals inhabit these areas and will eventually die."
    #voice sustain
    "But death isn't what makes something living. It's the constant internal motion of that something that will keep running until it is destroyed or broken down. "
    #voice sustain
    "Life is mysterious to me though. I can't guarantee an adequate answer of what it is."
    scene cg intro2 with fade
    "What I can guarantee though, is that everything living needs certain things to continue surviving. Whether it be the providing of absolute necessities, other tangible things, or even emotions, different life has different needs. "
    #voice sustain
    "Some of these needs are right in front of them; some of these needs are far away from them. If there is such a thing as a living thing without needs, is it truly living?"
    "Until that something inside me breaks down, gets destroyed, or when I'll stop needing things, I will never truly know what really qualifies as \"living\". And I'm okay with that... "
    "...for now."
    scene cg intro3 with fade
    
    "What really qualifies as death though?"
    "Death is usually seen as a tragic event. It's the loss of something from life. But can't it also be seen as a happy event? It's the start of something new, but how would we humans know whether it'd truly be something negative? "
    "When life dies, that life is released into a separate world; that is something guaranteed. It can start afresh and throw away a past of mistakes and misery. "
    "But sometimes life wants to cling on. Life wants to fight, for it's not finished with it's adventure yet. And life has a right to fight for that. "
    scene cg intro4 with fade
    "I believe there's life in death, and that there's death in life."
    scene bg black with fade
    $show_quick_menu = False
    centered "..."
    centered "What really does make something alive or dead?"    
    
    show logo with Fade(0.5, 0.0, 2.5)
    #------------------------------------
    
label lbl_introForest:
    play music music_Cool_Steel_Breeze fadeout 1.0    
    play sound sound_birds
    scene cg forest1 with Fade(3.5, 0.0, 0.5)
    $show_quick_menu = True
    show tree:
        xalign 0.3
    show merona content behind tree:
        xalign .6
        yalign 1.0
    
    mi "The leaves twitched. "
    mi "A very slight twitch. But still, a twitch is a twitch."
    mi "Interesting."
    show merona grin 
    "The side of my mouth slowly crept up into a crooked grin."
    show merona happy
    mk "Was that the wind or did you just move on your own?"
    show merona content
    mi "I can't deny that I may have felt a slight breeze. But I'm putting the emphasis on may."
    show merona worried
    mi "Will my words reach it?"
    "I waited for some kind of response."
    show merona worried OM
    mk "Please let it be that you moved your own leaves."
    scene cg talkwithtree1 with fade
    "I leaned against the tree, and I pressed my face into the rough bark as if this would encourage it to continue moving. I closed my eyes and smiled. My mind was bubbling."
    mi "Hopefully, this isn't a false alarm and is the real deal. My theories would come true! "
    mi "Talking trees of course sounds completely impossible, but what am I to know? "
    mi "Anything can be possible with a logical reason, so I'm on the search for my logical reasons."
    mi "I'm fairly sure that this tree just moved by itself."
    mi "Unless it was someone else moving the leaves; that's possible, but who'd be interested in tricking a person like me?"
    "I mentally rolled my eyes."
    mi "I suppose a lot of people could get a kick out of fooling me, but that's not the point."
    mi "No, no, we have a very special different point here."
    play music music_Dark_Red_Wine fadeout 1.0    
    "I made my voice sound syrupy and tried to put on an appealing tone."
    scene cg talkwithtree2
    mk "You know..."
    mk "You should really move a little."
    mi "First step: look at it from their point of view."
    mk "I understand that you may feel uncomfortable moving in the presence of others."
    mi "Identify the consequences of their standpoint."
    mk "It's good not to be so still all the time and let others move you around."
    mi "Make a pleasing offer that beckons them."
    mk "If you move though, you'll be able to connect with more humans!"
    mi "And reassure that there will be no consequences."
    mk "I know you're a tree, but... things work out one way or another in the end."
    mi "Finish the deal with a conclusion."
    mk "So, just move and I'm positive that we can have a good time with each other..."
    mk "Maybe have a cup of tea... or two..."
    mi "Not the best time I've tried negotiating, but who can push aside an offer of..."
    mi "...a cup of tea... or two..."
    scene cg talkwithtree3
    "I pulled out some short laughs, the noise sounding more pathetic than amusing. My eyes darted around, and then eventually settled on the tufts of grass by my feet. "
    scene cg talkwithtree4
    mi "I don't know what it is about plants, but they sure know how to bring out that awkward side of me. "
    mi "But, I'm glad that I got this chance to review my negotiating techniques! Now I can probably talk my way through the teachers and sound sort of classy at the same time. "
    mi "Now, that is a nice combination."
    scene cg talkwithtree5
    mi "All I've got to see is this tree accept my offer."
    stop music fadeout 1.0   
    play sound sound_cricket
    mi "..."
    mi "......"
    mi "..."
    scene cg talkwithtree6
    mi "I'm waiting."
    play sound sound_cukoo
    mi "..."
    mi "......"
    "I sighed and shook my head. Peeling myself off the tree, I dusted some of the bark still holding on to my uniform. "
    
    scene cg forest1 with fade
    show tree:
        xalign 0.3
    show merona disappointed OM behind tree:
        xalign .6
        yalign 1.0
    play music music_SoT
    mk "Sorry little guys. Looks like your mother doesn't want you to hang out with me since she herself doesn't want to."
    show merona disappointed
    mi "I see how it is."
    mi "Not a very friendly tree then, are you?"
    mi "That's alright, there are other trees in the forest."
    show merona content
    mi "Maybe I'll catch one moving."
    
    play music music_meronatheme fadeout 1.0
    play sound sound_ambiance
    
    scene cg_sky1
    show cg forest1_5
    show clouds behind cg at leftright
    show merona behind1 at bottomtop
    
    "I half-pumped my fist into the air."
    mi "Onwards is the direction I must go!"
    mi "But, I shouldn't forget the objective I have..."
    mi "...but I shouldn't forget about my theories too..."
    show merona behind2
    "I scowled and smacked my face a few times."
    mi "No, no! I have to remember why I came out here in the first place."
    "I shuddered and wrinkled my nose."
    mi "I don't want to have to stay up all night again like last time..."
    show merona behind3
    mi "And the time before that..."
    mi "Blargh!"
    mi "I don't understand how I keep doing this."
    show merona behind1
    "I lolled my head back then let it fall onto my left shoulder."
    mi "Now, where are the greens I need!?"
    scene cg forest2
    show merona worried
    "I walked for a few more seconds as my eyes scanned the surroundings around me. "
    mi "Hm."
    mi "Well, I can't skip out on this homework unless I want to fail this assignment and possibly repeat a level seeing my current standpoint."
    mi "I don't want to know what would happen if that happened..."
    "I recollected myself and barked out a laugh."    
    show merona laugh
    mi "But it won't happen!"
    mi "Yeah, I'm going to find them!"
    mi "..."
    show merona worried
    mi "Where are the herbs? Don't tell me that they've been taken already. That's impossible."
    mi "But, I did drag this work out a little and procrastinated, ha..."
    mi "..."
    mi "......"
    mi ".........."
    "My face lit up when I saw what I was looking for."
    show merona happy
    mk "I've finally found you!"
    mk "See now? I told you, Merona, that it was impossible for it to be gone."
    mi "I'm pretty certain that that's the one I'm looking for. I'll just stick it in my bag. Now I'm almost done! I've just got to find a few more and then I can go back to my room."
    show merona content
    "I continued meandering through the worn path."
    mi "Would I have the time to catch another plant in self-motion?"
    mi "I'll probably spend another hour finishing this assignment, so I could have time to do my personal observations."
    mi "It's currently edging to the afternoon, so I have some time. But what if I go at night? Maybe they'll be active at then since so many animals are asleep. "
    show merona grin
    mi "Maybe the animals have seen them move! I could maybe talk to an animal if I developed my skills enough, and it sounds easier to communicate with them than with a tree. "
    show merona eyesRight
    mi "It'd be interesting to see if humans can befriend trees. But then again, how would that happen if they don't have a nature-related ability?"
    show merona sad
    mi "That tree though. The one that rejected me. "
    show merona content
    mi "Maybe we'll communicate one day....?"
    scene cg handOnBranch1
    "I came to a cover of thin branches on a short tree and pushed them out to get through."
    mi "Go to a restaurant and share a cup of tea or tw-"
    
    
    stop sound
    stop music
    "I froze at the sight in front of me."
    scene cg handOnBranch2
    mk "..."
    mi "This can't be an illusion right? That monster..."
    scene cg handOnBranch3
    mk "..."
    scene bg black
    "I abruptly let go of the branches."
    play sound sound_snarl
    scene cg monsterRoar with hpunch
    mo "ROOOOAAAAARRR!"
    mk "AHHHHHHH!"
    play music music_movement
    scene cg forest3
    show rabbitMonster:
        yalign 1.0
        xalign 0.3
    show merona scared:
        yalign 1.0
        xalign 0.7
    show merona scared at RunBounce
    show rabbitMonster at RunBounce
    "I pivoted away and started slamming my feet onto the ground in a possibly hopeless attempt to run away."
    mi "Forget the tea, let's just pay the bill and leave!"
    show merona veryScared
    mi "Am I going to die now!? I feel like this is the wrong time for me to die!"
    mi "When did monsters appear in this forest!? I thought the academy protected this one! "
    "I continued fleeing, hoping that there would be nothing upcoming in the path to trip me or slow me down."
    show rabbitMonster with hpunch
    mo "ROOOOOAAAAARRRR!"
    scene cg M_onGround1
    "The dark colored creature pounced on me and I came crashing down on the dirt, landing on my arm. I coughed and closed my eyes, trying to shield them from the small dust storm that raged from my fall. "
    scene cg M_onGround2
    "The monster backed away, almost as if it was being cautious."
    scene cg forest4
    show rabbitMonster
    mi "It's like the forest's other life has stopped singing; but that's impossible because the forest is always full of sound. "
    mi "The only sound that I can hear though, is the rough panting of the monster a few meters away."
    scene cg M_onGround3
    mi "I'm going to die now, am I not?"
    stop music fadeout 1.0   
    mi "..."
    mi "..."
    play music music_newBegin fadein 1.0   
    scene cg M_onGround4
    mi "...but I'm not dead yet..."
    scene cg M_onGround5
    mi "I have to get up."
    scene cg forest5
    show merona determined
    show rabbitMonster shadow
    "My head was lighter. I partially opened my eyes to see what was before me."
    "The monster growled and its ears quivered as I slowly rose and slumped back onto my knees. I stabled myself by keeping my weight on my hitched up feet."
    mi "I don't know what I see in that monster's eyes; but I almost feel that something is residing inside there."
    mk "Uh-"
    $renpy.music.set_volume(0.8)
    scene cg M_zoomShadow1
    "The monster howled and I saw it's body surge forward. I brought up my arms in a futile attempt to defend myself. I took a final quick glance away from the creature to the clumps of trees, and squeezed my eyes shut. "
    $renpy.music.set_volume(0.5)
    scene cg M_zoomShadow2 with Pause(0.5)
    scene cg M_zoomShadow3
    mi "I'm probably about to embrace death anyways, so I'd rather die seeing the trees as my last image of life."
    stop music fadeout 1.0   
    scene bg black
    mi "..."
    mi "......."
    mi "..."
    mi "......."
    mi "...?"
    mi ".....!?"
    mi "...nothing has happened yet."
    mi "Does that mean I died a quick and painless death?"
    mi "Is death supposed to feel the same as life? Also known as approximately two seconds ago?"
    "Not wanting to bear the darkness anymore, I snapped my eyes open only to see nothing directly above or in front of me."
    play music music_piano
    $renpy.music.set_volume(1.0)
    
    
    scene cg forest4 with fade
    mk "Huh."
    mi "I suppose I'm okay now."
    mi "But... where did that monster go?"
    mi "It was just here and about to attack, so did someone kill it?"
    scene cg rabbit
    "Looking down at my knees,  I was matched in my gaze by a small black rabbit. "
    mi "Um..."
    mi "...?"
    mi "..."
    mi "Did that rabbit just save me!?"
    mi "Is this more evidence on how the inhabitants of the forest are much more complex than how humans think they are!?"
    mi "I think I just got saved by a rabbit!"
    mk "Uh..."
    mk "So..."
    mi "My voice feels kind of weak. Maybe I shouldn't speak so much, or at least speak quieter."
    #(the question mark represents Lexan speaking)"
    qq "Student!"
    mi "Hm? Is someone here? Did that someone release this rabbit to save me, because I'm pretty sure that this rabbit just saved me."
    qq "Student, if you are alright, please say something to me!"
    scene cg forest4
    "I sat up a little. I should answer that person."
    show merona surprised OM
    mk "I think I'm okay..."
    show merona worried
    mi "That was more of a mutter than an audible sound. But I feel strange. I think something might be wrong with my right shoulder. It feels different from the rest of my body and that was the place the monster's claws sunk into when it pounced on me. "
    show merona worried CE
    mi "My head's becoming lighter... I hear a dull ringing..."
    qq "Student, I'm coming over!"
    scene bg black with fade
    mi "Coming over? Oh alright, that would be best... but I might be down when you come over, since there's nothing nearby I can grab on to keep myself up..."
    stop music fadeout 1.0   
    "As the voice called again, I surrendered to the dizzying thing that took over me. "
    
    ###########################################
    ############## END OF DEMO ################
    
    #"This is the end of the demo. You're done playing, right? Right?"
    #menu:
    #    "Quit?"
    #    "Yes!":
    #        return
    #    "No?":
    #        pass
    
    
    ###########################################

    play music music_Lafayette
    play sound sound_birds
    mi "I can finally hear the sounds of the forest again."
    mi "The leaves, the birds, the whistles..."
    mi "What a pleasant tune."
    mi "Am I lying down right now?"
    mi "I should get up from this position I'm in and open my eyes..."
    "I tried moving my upper half, but a sturdy hand pressed me back down."
    #"(this question mark is Cimaria)"
    qq "You shouldn't move the upper half of your body very much, but feel free to move your legs."
    
    scene cg sunsetScape1 with fade
    "I opened my eyes and saw the fading sky of a day about to end. I was lying down on a mat outside."
    mk "...?"
    "The woman's voice spoke again."
    qq "You've been here for only a couple of hours. Do not fret, you did not suffer any fatal damage to your body."   
    #stop 
    scene cg sunsetScape2
    "I blinked twice and turned to her sound. She was kneeling at my right side. Her smile looked gentle but also like she had an embarrassing fact about me that she was hiding. "
    stop music fadeout 1.0   
    stop sound fadeout 1.0   
    mk "..."
    qq "..."
    mk "I lost consciousness right?"
    
    scene cg sunsetScape3
    qq "Yes. From a monster attack."
    scene cg sunsetScape2
    mk "Right, a monster attack. Are you the one who released the rabbit?"
    scene cg sunsetScape4
    qq "I do not understand what you mean by releasing a rabbit, for I am not the one who discovered you. I merely tended to your wound."
    play music music_potHappy
    scene cg sunsetScape2
    mk "Oh. Thank you for caring for me. You must be a healer then. Who did discover me? Did they release a rabbit?"
    scene cg sunsetScape5
    qq "I am a healer, yes. One of the academy's master mages found you after he heard some commotion. If I have the correct information, you are the one who brought the black rabbit."
    scene cg sunsetScape2
    "I frowned."
    mk "I am the one? How can that be? I didn't do anything. The rabbit just appeared right in front of me, and the monster was gone."
    scene cg sunsetScape3
    qq "It is still a mystery to what happened. But the master mage was certain that you were the one who brought forth the rabbit."
    scene cg sunsetScape2
    mk "Well, uh, um... you..."
    play sound sound_bell
    scene cg sunsetScape6
    ck "Healer Kinoten. My name is Healer Kinoten. I do not mind if you may call me by my given name, Cimaria."
    scene cg sunsetScape2
    mk "Thank you. Where is the master mage?"
    scene cg sunsetScape5
    ck "He's speaking with other academy authorities over the current situation that has risen."
    scene cg sunsetScape2
    mk "Will I be able to talk with him later about what happened?"
    scene cg sunsetScape5
    ck "I am certain that you will be able to speak with him later, but I cannot be too sure. He could even possibly come over here and speak to you."
    scene cg sunsetScape2
    mk "Alright."
    stop music fadeout 1.0   
    ck "..."
    mk "Cimaria, why am I outside and being treated? Shouldn't I be inside?"
    play music music_River_Meditation
    scene cg sunsetScape3
    ck "You were just wounded by a monster. No one knows what the wound could be, if it's infectious, and if you should be quarantined. Not many have survived monster attacks, so there is minimal knowledge of this subject."
    scene cg sunsetScape2
    mk "I see..."
    "I wonder if my bag is still on myself. Hm. It probably isn't."
    mk "Uh... do you know where my bag is? The one filled with herbs?"
    scene cg sunsetScape6
    ck "Yes, it's right at your feet. I'm sorry, but you had some herbs that helped speed your recovery, and I used some in my healing."
    scene cg sunsetScape2
    mk "What? Oh, but if they were used to help me, then I don't mind."
    scene cg sunsetScape6
    ck "Many things tie together with healing. It is a complex process to others, but only the people who have the right ability to become one will understand."
    scene cg sunsetScape2
    mk "I see. It sounds interesting."
    scene cg sunsetScape7
    "Cimaria perked up a little, and turned around. She turned back to me, faintly smiling."
    stop music fadeout 1.0
    scene cg sunsetScape6
    ck "I will have to stop our conversation. The master mage is coming."
    scene cg sunsetScape2
    play sound sound_footsteps
    "The sounds of the mage's footsteps gradually grew louder, and I could hear his rubbing fabric as he got closer. He stopped behind Cimaria. She looked up to him."
    play music music_Summer_Day
    scene cg sunsetScape8
    ck "Good evening, Master Lexan."
    "The mage acknowledged her back."
    ln "Good evening. Thank you for being willing to take care of this student."
    scene cg sunsetScape8
    ck "It was of no trouble, and I benefited from the experience. I shall take my leave now. Go ahead and talk to her about the situation."
    scene cg sunsetScape10 with fade
    "The master nodded."
    ln "I'll see you in the future."
    scene cg C_leaving1
    "Cimaria got up and slightly waved at me as she walked away. I mouthed my goodbye to her, but then I remembered something."
    mk "Cimaria!"
    scene cg C_leaving2
    "She stopped, looking confused."
    mk "Can I move my upper body now?"
    scene cg C_leaving3
    "She laughed, her face becoming a little pink."
    ck "Sure. Just have the master help you up. Make sure you don't move it too much. I healed it enough so that the shoulder should function normally by tomorrow, but be wary of it when you're sleeping."
    "She was about to walk away, but she stopped herself again."
    scene cg C_leaving4
    ck "I'm sorry for not telling you the other information about your injury; I've only been an official healer for a short time. Do not forget to return the mat too."
    "So she recently received her job occupation. "
    "It makes sense, seeing how young she looks. It's actually kind of impressive. Most who study to become a healer usually manage to become one when they're in their thirties."
    scene cg sunsetScape10
    ln "So then student, I'll help you get up."
    stop music fadeout 1.0
    
    "I finally took notice of the mage."    
    play music music_piano
    scene cg_sky2
    show lexan content    
    mk "Thank you, Master."
    play sound sound_bell
    show lexan content OM
    ln "It's alright if you call me Master Lexan. I don't mind having my name added."
    ln "What's your name?"
    show lexan content    
    mk "Student Kovene. My given name is Merona."
    show lexan content OM   
    ln "Okay. Student Kovene. I'll help you up now."
    scene cg L_holdingM1
    show cg_composite L_holding_M1 behind cg # Show here to enable gallery
    show cg_composite L_holding_M2 behind cg # Show here to enable gallery
    show cg_composite L_holding_M3 behind cg # Show here to enable gallery
    hide cg_composite
    
    "He lifted my head so he could place a hand on my back and his other on the mat, and he carefully pushed my upper body up."
    scene cg L_holdingM2
    mk "Thanks, Lexan. Or, er, Master Lexan. Sorry for not using your title."
    scene cg L_holdingM3
    ln "It's fine, it's fine, but you'll probably get in some kind of trouble by others if you forget to call me Master, so just remember to do that."
    scene cg L_holdingM4
    "I really should call him with a Master title, but he just seems too young to be a master mage. I don't feel like he is like one of the other masters in this way. "
    "I'll just call him Lexan in my mind. It feels more fitting to think of him by that rather than 'Master Lexan'. There are no authorities who'd tell me off except myself."
    play music music_Sugar_On_My_Tongue
    scene cg L_holdingM5
    ln "Anyway, I wanted to immediately discuss with you about what had happened earlier today."
    scene cg L_holdingM6
    mk "Sure, but, I myself don't really know what happened."
    scene cg L_holdingM5
    ln "I figured you would not be certain. I have deduced a possible explanation over what had happened, and if I may, I'd like to share it with you."
    scene cg L_holdingM6
    mk "Go ahead."
    "He blew out some air, looking straight ahead. "
    scene cg L_holdingM5
    ln "You saw a monster and I assume that you attempted to run away from it, correct?"
    scene cg L_holdingM7
    "I nodded."
    scene cg L_holdingM5
    ln "You ran a short distance but it managed to attack you and injure your shoulder, which caused you to stop and collapse."
    ln "The monster was about to strike when you... when you did something. Can you tell me what exactly did you do?"
    scene cg L_holdingM8
    mk "I really did nothing to protect myself, unless you'll consider my holding up my arms as my try at defense."
    mk "I had done absolutely nothing but that. I swear on all of the dead monster victims."
    scene cg L_holdingM9
    ln "Then this is where the guessing starts."
    stop music fadeout 1.0
    ln "You are student with a magical ability of life manipulation, correct?"
    scene cg L_holdingM10
    mk "My ability does involve life forms, but only the ones like plants and animals, disregarding humans."
    mk "Even so, I'm not a highly progressing student considering my age."
    scene cg L_holdingM11
    ln "Really? My assumption may be incorrect then."
    play music music_title
    ln "I had thought that you had used your magical ability to transform that monster into a simple animal."
    scene cg L_holdingM12
    "I raised my eyebrow at this statement."
    scene cg L_holdingM13
    mk "That sounds impossible."
    mk " I didn't consciously order anything to happen, and I don't believe that my ability covers a subject like this."
    mk "But..."
    scene cg L_holdingM12
    "I paused to think."
    scene cg L_holdingM13
    mk "...I've never been in this kind of situation, so I wouldn't really know."
    mk "Maybe? This might be true."
    mk "I'm still a novice at my ability, and maybe this event just triggered this extra function of my magic."
    scene cg L_holdingM14
    "Lexan's face practically glowed with the setting sun."
    ln "Precisely! That was what I had concluded."
    ln "You may have another part of your ability that can be used to transform things into plant or animal life forms!"
    ln "Do you know what this means?"
    scene cg L_holdingM15
    mk "I... can use this part of my magical ability to do something?"
    scene cg L_holdingM14
    ln "Um, yes, I suppose. But more specifically, you can do something special."
    scene cg L_holdingM16
    mk "...?"
    scene cg L_holdingM15
    mk "What exactly is this 'special thing' in store for me? Is it something that you had discussed with the other masters?"
    scene cg L_holdingM14
    ln "I did discuss this with others, but I didn't speak of it to the other masters. I talked to Headmaster Wriane."
    scene cg L_holdingM15
    mk "...Am I being assigned something to do?"
    scene cg L_holdingM16
    "If Lexan had to speak with the academy headmaster, then I must be doing something important in the future. "
    "What, am I going to change monsters into animals or plants? Am I going to become the savior to our nation for its monster problem?"
    scene cg L_holdingM14
    ln "You are going to see Headmaster Wriane because she would like you to help our nation."
    scene cg L_holdingM17
    "I widened my eyes."
    mk "Excuse me?"
    scene cg L_holdingM18
    ln "We know you're young, inexperienced, and lacking of skills. But you are a shred of hope that the kingdom needs."
    ln "Student Kovene, it is requested that you assist our kingdom by helping to eradicate the monster population of Diolacov."
    stop music fadeout 1.0
    scene cg L_holdingM19
    mk "..."
    "I looked at Lexan. I probably have a dumb look plastered onto my face."
    "It looks like in the future I'm basically going to be killing the monster population of this country."
    
    scene bg black with fade

    jump lbl_chapter1

    
label lbl_END:
    #"End"
    #Show the credits roll
    call lbl_Credits from _call_lbl_Credits
    return