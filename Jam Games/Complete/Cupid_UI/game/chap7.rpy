label chap7:  
    $save_name = "chap7: the taste of honey"
    $persistent.Chapter7Unlocked = True
    
    scene bg chap07 with slowdissolve
    with Pause(2)
    play music "sfx/eros.ogg"
    scene bg black with fade
    nvl clear
    o "{i}What in me is dark.{/i}"    
    nvl clear
    play sound "sfx/heartbeat.ogg"
    show bg polaroid1 with fade
    show bg black  
    nvl clear
    o "{i}No light, but rather darkness visible.{/i}"
    nvl clear
    play sound "sfx/heartbeat.ogg"
    show bg polaroid1 with fade
    show bg black  

    "But that is not me."
    show bg polaroid2 with zoomin
    show bg polaroid3 with zoomin
    show bg polaroid4 with zoomin
    show bg black with zoomin
    play sound "sfx/heartbeat.ogg"
    "What is in me, is not me."
    "I have fought with it, lived with it, and survived."
    play sound "sfx/heartbeat.ogg"
    "Yet we become what we subdue."
    "If that is true, then I was never myself."
    show bg polaroid5 with zoomin
    show bg polaroid10 with zoomin
    show bg polaroid7 with zoomin
    show bg black with zoomin
    play sound "sfx/heartbeat.ogg"
    "I am not a monster."
    scene bg rosadark with Dissolve (3.0, alpha=True)
    m "Then what are you?"
    "..."
    "...tired."
    
    r "{i}Uhm, somewhat irritable.{/i}"
    "That too."    
    r "{i}I... somehow prefer this side of you.{/i}"
    "{i}Makes me wonder why I am so stern with you.{/i}"
    "Why I care so much for your well-being."
    "Why did I even offer you to stay with me?"
    "I do not know."
    r "{i}You are still so generous... even when you are like this{/i}"
    "I give because I can take."
    r "Once upon a time, there lives a man."
    "{i}Lived.{/i}"
    r "Who lost his heart."
    r "So he ate others'."
    show bg polaroid9 with zoomin
    show bg polaroid6 with zoomin
    show bg polaroid8 with zoomin
    show bg polaroid11 with zoomin
    show bg black with None
    show text "{i}He who makes a beast of himself gets rid of the pain of being a man.{/i}"
    with Dissolve (2.0, alpha=True)
    with Pause (2)
    scene bg rosadark with None
    "I never lost it. I have always been cursed without it."

    r "Then take mine."
    "Yours?"
    scene bg rosadark2 
    r "Do you love me? I think you do."
    scene bg rosadark 
    "..."
    scene bg rosadark2 
    r "Do you know how long I have travelled to find you?"
    r "How far I've searched?"
    r "And now you're here."
    r "Finally."
    r "My heart yearns for you, Guilleme."
    scene bg black with None
    show text "{=iloveu}I love you{/iloveu}"
    with Dissolve (2.0, alpha=True)
    with Pause (3)
    "S-Stop."
    hide text
    "Nectar flows from the spring of the rose."
    show text "{i}In eminence and obstacle find none\nOf membrane, joint or limb, exclusive bars{/i}"
    with Dissolve (2.0, alpha=True)
    with Pause (3)
    hide text
    r "Touch me, Guilleme."
    r "My body wants you."
    scene bg rosawalks with Dissolve (0.3, alpha=True)
    scene bg black with Dissolve (1.0, alpha=True)
    "My eyes fly open from the groggy mist of confusion."
    scene bg cupidbound2 with Dissolve (0.3, alpha=True)
    scene bg black with Dissolve (1.0, alpha=True)
    "My body is bound in a force that imprisoned my limbs."
    scene bg cupidbound with Dissolve (0.3, alpha=True)
    scene bg black with Dissolve (1.0, alpha=True)
    "{i}Chains.{/i}"
    if persistent.adult:
        "The smell of your juices saturates my nose."
    else:
        "The smell of your skin saturates my nose."
    "{i}Sweat.{/i}"
    if persistent.adult:
        "I am hard."
    else:
        "My whole body is tense."
    "{i}Flesh.{/i}"
    scene bg rosawalks2 with Dissolve (0.3, alpha=True)
    "You walk up to me."
    if persistent.adult:
        "Your naked body makes my throat swallow."
    "You put a finger on my lips and trace it down my neck."
    "Goose bumps break on my skin."
    "You are beautiful. I have noticed before."
    "I knew you were, before you even did."
    "But... You were pure."
    "{i}Pure.{/i}"
    "The taste of your love was unripe fruit."
    
    "Instead, I've thought of you as something I'd like to protect."
    "Why is that?"
    "Your hair flows out like a river as it brushes against my skin."
    "You reach your hand to me and my stomach curls."
    
    "There is a tainted power radiating from you that makes me gag."
    
    "Like sugar dissolved in water."
    "Like a full belly on the brink of sick."
 
    "I thought I had forgotten this feeling."
    "I am afraid."
    "You move closer to me, and I startle back."
    "Everything in dreams is slower."
    "You claim my mouth with yours, it tastes just like honey."
    scene bg cupidbound3 with Dissolve (0.3, alpha=True)
    scene bg black with Dissolve (1.0, alpha=True)
    show chains
    "Spit ropes between our lips and I feel weaker the more I linger in this dream."
    "A trap."
    "Rosa."
    "What are you doing?"
    "Stop this."
    "You giggle."
    r "No."
    if persistent.adult:
        "Your fingers grope my stiffness and stroke it hungrily."
        "My eyes roll back."
        "My energy drains from me."
        $ achievement.grant("Spectral Handjob")
        $achievement.Sync()
    else:
        "You open your mouth and kiss me again."
        "My energy drains from me."
        "I pull my face away."
    "S-Stop!"
    "I don't want this."
    
    r "And yet you want me."  
    r "Your body agrees."
    "No."
    r "You want me too, don't you?"
    "Stop it, Rosa!"
    "You don't know what you're doing!"
    
    r "See, you do love me!"
    r "You want to protect me."
    r "You treat me differently."
    
    "..."
    "{i}I have always kept my distance from you.{/i}"
    "{i}You were always hovering at the edge of my vision.{/i}"
    if persistent.adult:
        "Pressure mounts as your hand moves faster."
        "I will myself to move, but my mind is torn to pieces at this assault."
        "You bow low at my groin, and your mouth opens to swallow my mound."
        "Your tongue slides along my hardness. The sound is slick in my ear."
        "I hit the back of your warm throat."
        "My eyes flutter."
        "S-Shit..."
        $ achievement.grant("Oral Sex from Hell")
        $achievement.Sync()
    else:
        "The air is heavy with magic."
        "I will myself to move, but my mind is torn to pieces at the spell."
        "Imaginary hands touch my body and pinch at my flesh."
        "They pull me down and hold me in place."
    scene bg cupidchains
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    scene bg black with Dissolve (0.3, alpha=True)  
    "I-I must escape!"
    scene bg chains with None
    "I can't move from this dastardly prison!"
    
    r "What does it feel like to be helpless?"
    r "Have you forgotten what it feels like to be a victim?"
    r "To be weak?"
    play sound "sfx/monster.ogg"
    play music "sfx/nightterror.ogg"
    scene bg rosamonster with Dissolve (3.0, alpha=True)    
    "Your face begins to change."
    "You are Rosa."
    "You are Catherine."
    "You are Marcus."
    "You are Diomedes."
    "You are Psyche."
    "Your head begins to snap and distort."
    "The skin bubbles and the flesh tears to reveal the pulsing hide of the monster inside."
    "Your glistening heart pumps in your chest."
    "Another face grins as its eyes focus on me."
    "Yet I'm not afraid of this thing and its many mouths."
    "This was nothing but a reflection, a mirror held up to what I really am."
    scene bg black
    if persistent.adult:
        "You sit on top of me, slipping me inside you."
    scene bg sinisterchains 
    "I gasp and struggle, but your hands clamp around my neck."
    "One of your tongues licks at the side of my belly, as if sampling the food before the course."
    
    gt "You are nothing but a parasite, you see?"
    "The other face contorts into a grin."
    gt "How did you ever think you were powerful?"
    gt "Look at you squirm."
    gt "You are an insect."
    gt "Itis time for me to swat you."
    gt "To make you pay for all you have done."
    
    "W-Who are you, really, Rosa--"
    if persistent.origin:
        r "Oh, you have forgotten me?"
        r "{i}...Florian?{/i}"
        "Guilleme staggered back from the sound of an old name."
        r "Do remember the heat of fire that licked my flesh?"
        r "The fire that burned {i}Hacienda de Puzo{/i} to the ground?"
        r "You have taken everything from me, Florian."
        r "It is time for payment."
        "My mind unearths memories buried by decades."
        "They hover just beyond my reach and the the taste is bitter."
    if persistent.adult:
        "But you're moving now, grinding deeper into me."
        "Your hips slap on my thigh."
        "The poison of disgust and arousal saturates my senses."
        $ achievement.grant("Nightmare Fuel")
        $achievement.Sync()
    "You smile at my helplessness."
    "The smile breaks your cheek and splits your face in two."
    "Your mouth reveals a gaping hole."
    "R-Rosa--"
    if persistent.origin:
        r "I am not Rosa!"
        r "I am every victim you devoured, every life you laid to waste!"
        r "Didn't I promise you that I will find you?"
        r "I may have forgotten your face, but never the taste of your blood."
        r "Fate favors her child, Florian."
        r "I have destroyed you once."
        r "I can do it again."
    else:
        "W-Why are you doing this--"  
        r "Why?!"
        r "Because you are filthy!"
        r "You eat and you eat!"
        if rosajealous:
            r "I hate you."
            r "You won't even look at me."
            r "Do I have your attention now?"
            if persistent.adult:
                r "Do I taste good?"
                $ achievement.grant("Jealousy")
                $achievement.Sync()
            r "Well, it's too late."
            r "You had your chance."
            r "Now, it is my turn to feed on {i}you{/i}."
            if justice:
                r "Like Mother said, this is a fitting end for your crimes."
            else:
                r "Like Mother said, this is a fitting payment for your crimes."
        else:  
            r "You took all her love, left me with nothing!"
            r "I've always been at your scraps."
            r "I just wanted a bite, that's all, but you had to consume every last bit!"
    "My eyes widen at your words as the realization strikes my senses."
    "What did you say?!"
    "Y-You are--"
    if persistent.origin:
        r "How you have hurt Mother, Guilleme."
        r "You deserve all the pain and punishment in the world."
        r "But oh, I forgive you, even if she can't."
    else:  
        r "But oh, I forgive you, even if Mother can't."
    r "I love you that much."
    "Shut up!"
    r "I do! Don't you believe me?"
    if persistent.adult:
        "Your hips pound faster into me, and a moan escapes through my gritted teeth."
        "Every eternity that passes saps my strength, yet I try desperately to shake my bounds."
        r "Look at you, fighting me so hard."
        r "Doesn't it feel good?"
        r "Aren't you supposed to like this?"
        "..."
        "What does that even mean?"
        "How am I supposed to like it?"
        "How is being degraded into a rag supposed to be enjoyable?"
    else:
        "I struggle with the chains in my mind."
        r "Look at you, fighting me so hard."
        r "If you just relax, it will all be over soon."
        "My teeth grit with anger."
    "Too many times I have heard the same revolting words."
    "All convincing me to accept my fate lying down, eyes closed."
    "{i}It will be over soon.{/i}"
    "Anger rips apart my chest."
    if persistent.adult:
        "{i}Open your mouth.{/i}"
        "{i}Take them off.{/i}"
        "{i}Swallow.{/i}"
    else:
        "{i}Open your mouth.{/i}"
        "{i}Twirl around.{/i}"
        "{i}Shut up.{/i}"
    "And after all of that, they have the gall to tell me what I am supposed to feel."
    "{i}Little boys aren't supposed to cry.{/i}"
    "{i}Why do you refuse a lady?{/i}"
    "{i}Just relax and enjoy it.{/i}"
    "{i}...It will be over soon.{/i}"
    "..."
    "Men and women, they are all rabid for desire."
    "They are disgusting."
    "I will not be anyone's toy, ever again."
    "I will not be a piece of meat."

    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
    "{i}How dare you humiliate me, you wretched little witch!{/i}"
    "I rattle the bounds of my cage, and it makes you flinch."
    "You don't notice a part of it splinter."
    "I bare my teeth at you."
    "I will {i}never{/i} forgive you!"

    r "Why are you so cross with me?"
    r "Don't you see I am doing this for you?"
    "S-Shut your mouth!"
    "The creature doesn't stop."
    if persistent.adult:
        "It continues to feed on my mind, its body grinding at me with increased fervor."
        "The muscles of my thighs begin to shiver."
        "The creature on top of me screams out my oldest names out of its many mouths."
    else:
        "It continues to feed on my life."
    "It drools over me with ecstacy."
    "It is never, ever gentle."
    "It grasps my neck and suffocates me as it nears its peak."
        
    gt "Y..Yes.."
    gt "Mine!"
    gt "You are mine!"
    
    "I struggle out of the creature's grip."
    "I can feel my body weaken and tense at the same time."
    if persistent.adult:
        "My groin throbs and calls out for more flesh."
        "Even at its peril, my body doesn't listen to me at all."
        "Desire is its own ruler."
    "I concentrate on breaking the spell that holds me in place."
    if persistent.adult:
        "The creature on my groin is nothing but another mouth."
        "Its tongue slips and slides at me with every push."
        "But it is hard to escape."
        "---the pressure in my bladder--"
        "It distracts me from my goal."
        "My consciousness is frail and almost out of my grip. My lungs are crying out for air."
    else:
        "But it is hard to escape."
        "My consciousness is frail and almost out of my grip. My lungs are crying out for air."
    "Terror mounts inside me as I feel my life drain away."
    
    "P-Perhaps..."
    "I should stop struggling."
    
    gt "Perhaps."
    "Let the monster take me."
    "I am... so tired."
    "{i}...So tired of fighting...{/i}"
    gt "You poor thing."
    
    "The momentary lapse on the creature's hold lets loose a part of my mind."
    "I gather all my remaining strength and push back at the crack I made a while ago."
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
    play sound "sfx/glassbreak.ogg"
    show bg black with pixellate
    "The spell shatters, and I break free."
    "I do not give the creature a chance to think."
    play sound "sfx/stab.ogg"
    with flashblood
    
    if persistent.adult:
        play sound "sfx/stabslash.ogg"
        with flashblood
        "I jab my hand into its chest and rip its heart out."
        "I slice through its skin until flesh erupts on my fingers."
        play sound "sfx/blood.ogg"
        with flashblood
        "It sprays out thick, dark blood onto my face."
        play sound "sfx/stab.ogg"
        show bg gattacks
        with flashblood
        $ achievement.grant("Bloody Cupid")
        $achievement.Sync()
    else:
        "I jab my hand into its chest."
        "Momentarily winded and stunned, I hit it again."
        play sound "sfx/stab.ogg"
        with flashblood
        "It falls to its knees."
    "The spell on me weakens. I feel power returning to my body."
    "And yet, the creature laughs, the sound resonating from around me."

    bg "I am not going to die here."
    bg "I have sacrificed far too much to perish."
    "The creature's laughter jeers at me."
    gt "For what?"
    
    if persistent.adult:
        play sound "sfx/goreblood.ogg"
        with flashblood
        "I grasp one of its limbs and pull. The flesh tears away like a flower's petals."
        
        "The creature drowns in its own blood."
        "I break its wings and it howls in pain."
        "I push it off of me, striking its malformed body."
        "Every blow breaks bones and snaps sinews."
    else:
        play sound "sfx/grip.ogg"
        with flashblood
        "I grasp its neck and watch it choke, relishing the control back in my veins."
    "Yet the creature still laughs."
    
    bg "I am not to be mocked, you filthy thing."
    bg "I am powerful and I will endure."
    bg "I have played this game for centuries and I will not be beaten at my own device."
    if persistent.adult:
        "The creature crawls at my feet."
        "Suspended blood forms scarlet jewels around us."
        "In dreams, time is slow."
        "It caresses my leg with its girlish hand."
    else:
        "The creature caresses my hand choking its throat."
    scene bg black    
    gt "This... you enjoyed it too, r..right..?"
    gt "I did it all for you..."
    
    if persistent.adult:
        "I bring my foot up."
        "Its head titters as I crush its skull under my heel."
        play sound "sfx/gore.ogg"
        with flashblood
        gt "I love you...!"
    else:
        "My anger increases the power in my hands."
        "Its mouth titters as I snap its neck."
        
        play sound "sfx/crack.ogg"
        gt "I love you--!"
    $ achievement.grant("Wet Dream Gone Bad")
    $achievement.Sync()
    stop music fadeout 2.0    
    scene bg guilroomdark with slowdissolve

    #show gf maddown with Dissolve (0.3, alpha=True)
    if persistent.adult:
        
        "Guilleme woke up from the dream with bloody hands."
        "His trousers were wet."
        "His groin still felt sore and pulsing inside his pants."
    else:
        "Guilleme woke up from the dream, weak and shaking."
    "He stood up from the bed and his vision floundered."
    "He fell onto the floor, losing balance from the sudden frailty of his legs."
    play sound "sfx/slump.ogg"
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    if persistent.adult:
        "The churning in his stomach wouldn't go away."
        play sound "sfx/blood.ogg"
        "Bile rose up in his throat and he vomited."
    else:
        "The churning in his stomach wouldn't go away."
    "Every breath was shallow and tasted like sick."
    "He closed his eyes."
    "He laid on the floor for a little while, dragging air into his lungs until the urge to vomit passed."
    "How could darkness still spin without ground?"
    "Guilleme's fist balled up in anger."
    "To be degraded into this pathetic state was unforgivable."
    "He felt the fury burning hot in his heart, consuming every thought in his head."
    "He tried to reign it in."
    "It was an unnecessary expulsion of energy at this point."
    "He didn't know how long he laid there in the dark."
    if persistent.adult:
        "Helpless and weak, beside his own vomit and blood."
    "But soon, his strength came back to him."
    "Pushing himself from the floor, Guilleme staggered around his room."
    "He cleaned himself and put on fresh clothes."
    "He could still feel the tugs of odious power within his stomach."
    "He walked to his bedside drawer and looked inside."
    if dagger:
        show gf furiousdown
        "It was empty."
        show gf furiousdown2
        "Another bite of vile hatred churned his chest."
        if persistent.adult:
            "He grabbed his face, running his nails over the flesh of his cheek."
            "Blood promptly traced a light trail on his skin, but the scratch disappeared as soon as his finger lifted."
            $ achievement.grant("Does not Form Scars")
            $achievement.Sync()
        else:
            "He grabbed his face in frustration."
        if persistent.dagger2WasReadBefore   is None:
            $persistent.dagger2WasReadBefore  = True
            $persistent.currentLinesRead +=1    
    else:
        show gf petulantnormal
        "The old dagger glinted at him with malice."
        "It reminded him of his anger, forged and sharpened over the years."
        "His hatred was distilled in this blade."
        "He gripped the dagger's hilt until red welts formed on his palms."
        "He felt bound by purpose and rage."
    show gf furiousshock  
    play music "sfx/whisper.ogg" fadein 2.0
    "He could hear her calling out to him."
    "A whisper."
    "A taunt."

    m "{i}Guilleme...{/i}"
    m "{i}Play with me again...{/i}"
    m "{i}Pleeeease...?{/i}"
    m "{i}You know where to find me!{/i}"
    
    show gf petulant  
    "He shivered as his teeth grinded in his mouth."
    g "You will pay for this."
     
    scene bg black with dissolve
    
    if persistent.chap7WasReadBefore   is None:
        $persistent.chap7WasReadBefore  = True
        $persistent.currentLinesRead +=1
    call badend from _call_badend

return
    
    
    

    
