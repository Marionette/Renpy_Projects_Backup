label chap2:
    stop music
    $save_name = "chap2: la piqûre"
    play music "sfx/pant.ogg" volume 1.0
    $persistent.Chapter2Unlocked = True
    
    scene bg chap02 with slowdissolve
    with Pause(2)
    scene bg black with fade

    m "It's funny, is it not?"
    r "..."
    m "They always leave you."
    m "Such is the way of the world."
    m "The more you love, the more you lose."
    m "Oh, it seems like they'll stay forever, but they never do."
    m "I'm the only one who stays, my lovely rose."
    m "My love is the only love you need."

    
    m "You were always so weak."
    m "Always so loving to people who did not deserve it."
    
    m "I told you to get rid of her, didn't I?"
    m "I told you to be wary."
    
    m "I knew it from the start, my rose."
    
    call cathbad from _call_cathbad
    m "I knew she would just cause you pain."
    
    call m017 from _call_m017
    
    r "..."
    
    m "Your silence bothers me, child."

    r "She was important to me, Mother."
    r "I..."
    r "I... loved her..."

    "Mother only laughed as Rosa screamed out her pain."
    "..."
    stop music fadeout 2.0
    "Rosa felt strong arms shake her awake."
    scene bg rosaroomnorm with Dissolve  (3.0, alpha=True)

    g "Rosa..."
    "She opened her eyes and was hit by a strange sadness that crushed her."
    "She was dazed for a moment."
    "Why was she so sad?"
    "And then she remembered..."
    scene bg rosaroomnorm
    play music "sfx/quietsadness.ogg"
    "Her best friend was gone."
    "...She was gone."
    show gn serious  
    g "Rosa...?"
    g "How are you feeling?"
    "Guilleme sat by her bed, a hand in hers. Rosa didn't realise she had been holding on to it tightly in her fitful sleep."
    "She broke from his grasp and clutched her knees."
    show gn dep  
    g "Rosa?"
    "She remained silent."
    show gn pout  
    g "I came to check on you."
    g "You went into shock and lost consciousness."
    g "...I can only imagine..."
    show gn angrylookdown  
    g "How hard it must have been for you to see her--"
    g "Like that..."
    "His words echoed in her brain, yet she did not register much of their meaning."
    "Rosa still refused to speak, and Guilleme fidgeted with his glove."
    show gn dep  
    g "The wake will take place as soon as possible, Rosa."
    show gn think  
    g "I just wanted to let you know that she is being taken care of."
    show gn angrylookdown  
    m "He's hiding something."
    "There was a slight triumph in Mother's voice."
    r "..."
    m "He wants to get rid of her body as soon as possible."
    m "Don't you see it, child?"
    m "Tell me you're not falling for this."
    "Rosa was tired." 
    if cynicalmom:
        "Mother, always the cynic, would say such things."
    else:
        "It was unsurprising to hear Mother say such things."
    "She hated anyone who came close to Rosa's heart."
    "Rosa didn't want to hear it."
    "She didn't want to deal with anything right now."
    "All she wanted to do was wallow in her loneliness."
    "...To curl up inside the hole Catherine had left behind and sleep."
    m "My child, tell me you see it."
    
    call m019 from _call_m019
    m "How well do you even know him, child?"
    r "I-I've known him for as long as I knew Catherine, Mother."
    r "He is a close friend..."
    m "I didn't ask how {i}long{/i} you've known him, but how well!"
    m "Beyond the mask that he displays in public view. Do you even know his past?"
    m "Do you even know any of his ambitions or secrets?"
    r "He was always a private man, Mother."
    m "Think back, child!"
    m "Isn't it curious how all his past relationships have ended in disaster?"
    show gn think  
    m "Everything he touches crumbles."
    r "..."
    r "...That is not enough to accuse him of anything..."
    show gn angrylookdown  
    m "You idiot!"
    m "He is different!"
    m "He does not belong!"
    m "You have felt it too, haven't you?"
    
    "Rosa looked at Guilleme with new eyes now."
    show gn serious  
    "A hint of doubt slithered out beneath her sadness."
    "Rosa wanted something to blame, a cask for all her regrets."
    "Guilleme seemed like the perfect candidate, didn't he?"
    m "Yes, you're finally seeing it."
    m "Open your eyes, child."
    "It made sense."
    "Guilleme and Catherine's relationship began to pewter off into coldness right before she died."
    "Her mental instability only served to compound the fracture in their relationship."
    "Perhaps Guilleme was tired of her and had her killed off for convenience?"
    "...Or perhaps Catherine, in her psychotic state, killed herself to spite him?"
    show gn huh
    g "Rosa? Are you okay? You've been mumbling."
    "Rosa stared at the man beside her."
    r "..."
    show gn angry  
    m "He is not to be trusted, child."
    m "He is a demon."
    
    "Guilleme returned Rosa's angry stare with a resolute look."
    show gn annoyedtalk  
    g "I know you must hate me, Rosa."
    g "I am aware that I only aggravated Catherine's condition with my presence."
    show gn angrylookdown  
    g "I know the feeling when I am not wanted."
    
    "He stood up, a hard yet kind look on his face."
    show gn angry  
    g "Just remember that I will always be here for you."
    show gn think  
    g "As much as I was there for Catherine, even though she spat me out."
    
    show gn angry  
    "Rosa bit her lip."
    "When Catherine had refused to eat, it had been Guilleme who fed her and attended to her."
    "Despite Catherine hurling abuse at him, he had tried to care for the sick woman himself."
    
    m "Lies! All lies!"
    m "Keeping up appearances!"

    r "Then what is it that he has done, Mother?"
    r "Catherine committed suicide."
    r "It was not by his hand that she died."
    
    m "Are you just going to leave it at that?"
    m "Look at his face and tell me you trust him whole-heartedly!"
    
    "Rosa tried to search for the answer in Guilleme's eyes."
    "But, as always, his face betrayed only few emotions."
    stop music fadeout 3.0        
    r "I... don't know."
 
    "Mother was screaming now."
    m "He killed her!"
    m "I am sure he did!"
    m "And you're letting him get away with it!"

    r "Please, my head hurts."
    m "And you say you loved her."
    m "You never loved her, you selfish child."
    m "I've always known you were this selfish."
    if badmom:
        m "You're a monster!"
  
    r "S-Stop!"
    
    m "You throw people away!"
    m "Didn't you throw me away when I inconvenienced you?"
    m "Admit it."
    cn "You were secretly relieved I died."
    
    r "{i}No! Stop it!!{/i}"
    show gn annoyedtalk  
    "She screamed back at that last voice."
    "Her mouth quivered."
    "Guilleme stared at Rosa in shock."
    "The outburst had accidentally come out aloud."
    show gn dep  
    "It pulled a plug that kept the tears from pouring out."
    "Now her vision clouded, and she blinked them away again and again."
    "She was not sobbing. She did not even realise her face was wet."
    show gn pout  
    "Guilleme and Rosa stared at each other, both kindred in their sorrow."
    
    "He knelt down by Rosa's bed and wiped her tears with his hand."
    "He did not say anything while doing this, and Rosa stared blankly ahead."
    "It almost stunned her how many tears a person's eyes could carry."
    show gn angrylookdown  
    g "I loved her too, Rosa."
    "He said it after a while."
    
    show gn pout  
    g "I know what you're feeling."
    "She didn't know if it was her own, or if Mother's anger influenced her, but her chest heaved."
    "She balled up her fist so tightly that her fingernails hurt."

    r "Shut up."
    show gn annoyedtalk  
    "She spat, and the man recoiled at the uncharacteristic bitterness of her words."
    show gn angrylookdown  
    r "Catherine was afraid of you in her last days!"
    show gn think  
    r "You did something to her!"
    r "I know it!"

    "She could feel Mother inside her head, building up her anger."
    m "He has to be punished!"
    show gn angry  
    r "You are to blame!"
    m "He has to atone!"
    r "I know you are guilty!"
    m "He must pay!"

    "Guilleme stared at her, dumbfounded for a few seconds."
    "But the man didn't try to appease her."
    show gn seriousbig  
    "He only stepped closer to Rosa, wrapping his arms around the hysterical girl."
    scene bg grhug  
    play music "sfx/sorrow.ogg"
    r "Let go of me!"
    r "I hate you! Let me go!"
    
    "But Guilleme didn't."
    
    g "If you need something to hate, then I'll accept your hate."
    g "But you must accept my comfort, too."
    g "I need you too, right now, Rosa."
    g "You are the only one who loved her as much as I did."

    "Guilleme's words brought back Catherine in Rosa's mind."
    "Almost at once, the anger was replaced with a sadness so heavy she couldn't breathe."
    "Why was she so angry again?"
    "She was focusing on anger instead of pain."
    "It was easier."
    "The real tears came, all for the loss of the girl they both loved."
    "Tomorrow was not going to come."
    "There was only right now, the loss, and two friends mourning a loved one."
    "Rosa cried until she thought she wouldn't be able to stop, and Guilleme quietly held her."
    "Slowly, her weeping began to subside into sobs, and only then did he speak again."
    g "Stay in the château, Rosa."
    g "I know you are thinking of leaving now that Catherine is gone."
    g "But I can't let you wander the streets again."
    g "I will take care of you."
    g "...It's what Catherine would have wanted."

    "Like a spell being broken, these words brought back her anger."
    r "How could you possibly know what Catherine wants?"
    scene bg rosaroomnorm  
    show gn angry
    "She pushed his arms away from her."
    show gn annoyedtalk  
    r "She's dead."

    show gn pout  
    "Guilleme's mouth pursed, and he stepped away." 
    r "I want you to go."
    show gn angrylookdown  
    r "Please leave me."
    show gn think  
    "Guilleme sighed and closed his eyes."
    g "...I understand."
    show gn angry  
    hide gn angry  
    play sound "sfx/softdoorclose.ogg"
    "He turned on his heels and left without another word."
    $renpy.pause(delay=0.2)
    
    scene bg rosaroomdark with Dissolve (3.0, alpha=True)
    
    "Hours seemed like minutes to her."
    "She would fall asleep and awaken in unfit intervals so often that she had lost the exact time."
    "Awake, she would stare at a part of the wall with no coherent thoughts forming in her mind."
    "One would think mourning was an activity spent in depressive frenzy."
    "All the reasons to grieve are yours, after all."
    "She could wail now, if she wanted. She could pull on her hair, curse the skies."
    "She could reminisce the past, admire the frailty of human lives..."
    "..."
    "Unfortunately, it was something less poetic."
    "Pain was simple. It was clean."
    "It was a well-sharpened knife that sliced through the heart in one stroke."
    "No blood, no mess."
    "{w=0.3}Empty."
    "When tears were spent, when you have exhausted your grief,"
    "In place of pain, there would be..."
    "{i}Nothing...{/i}"
    "The pain might call out."
    "Grating, nagging, constantly picking at fresh wounds."
    "But as time pass, the hole would get bigger..."
    "Darker..."
    "Deeper..."
    "Soon, there would be nothing left."
    "Soon, it would be hard to find where the hollowness ended and where you began."
    "{w}"
    "Rosa slept all day."
    stop music fadeout 2.0   
    "The sun had gone down twice before she shifted from her bed."
    "She stood up slowly, deliberately, with a purpose."

    m "My child, you know I hurt when you're hurt."   
    scene bg black  
    "Already a surge of power flowed within her, fueled by her grief."
    "The power filled her up, and there was so much emptiness inside that the energy saturated her whole body."
    "Purpose was always a balm for grief."
    
    r "Mother."
    r "Tell me what to do."

    
    call m020 from _call_m020
    play music "sfx/uncomfy.ogg"     
    scene bg rpow  
    "Rosa didn't speak, but she started to form the words in her mind, feeling them in her bones, giving life to every thought."
    "She took a small knife and carved a symbol on her floor."
    "It didn't need much, a guilt spell."
    "It didn't aim to punish. It only aimed to inform."
    "She needed to know how much guilt the man carried, and the source of such guilt."
    "If the guilt was concrete and came from a direct action, then she would know Guilleme did something to Catherine."

    "It had been a while since she had used magic."
    "It used to be the only way she could protect herself from the world."
    "Mother had taught her, and now, Mother guided her as she cast her spell."
    
    "She needed a possession of the man."
    "Rosa opted for his voice, still fresh from memory."
    "She focused on the last conversation they shared."
    
    g "{i}If you need something to hate--{/i}"
    g "{i}I will take care of you--{/i}"
    r "..."
    g "{i}I need you.{/i}"
    
    "His words made Rosa feel distress and confusion."
    "Always, it was this way with him."
    "The feeling wasn't foreign. It had been there for years."
    
    g "{i}I will always be here for you.{/i}"
    play sound "sfx/dripcrack.ogg"
    with flashblood      
    "Rosa felt a violent force upturn her stomach. It was that horrid lurch just before vomiting."
    m "You failed!"
    "The spell collapsed in her brain."
    m "Focus, idiot child, or you'll lose your chance."
    
    "Rosa tried again."
    "This time, she focused on Guilleme's eyes."
    "Cold."
    "Like flints of steel."  
    "Dark and fathomless."
    "No grief except, perhaps, for the situation."
    "No Catherine."
    "No pain of loss."
    
    "This didn't matter to her. Their relationship was dying anyway."
    "Where was his guilt?"
    
    "Rosa dug deeper. She increased the chanting on her lips."
    "No torment."
    "No uncertainty."
    "{i}...No guilt.{/i}"
    "Did the spell fail again?"
    "She searched once more and found nothing."
    "There was no guilt in Guilleme's eyes."
    "She could stop the spell now, knowing that he was innocent."
    "If the spell had worked, then Guilleme was blameless."
    "But..."
    "This absence was most distressing."
    
    "Rosa desperately pushed her mind further, almost wishing there were traces hiding beyond her reach."
    
    "{i}Guilt should be present in any loss, no matter how little!{/i}"
    "{i}Don't we blame ourselves for our own loss?{/i}"
    "{i}Don't we hate ourselves and punish ourselves, even if it wasn't our fault?{/i}"
    "{i}It didn't have to be real, but we need guilt to feel pain.{/i}"
    
    "...But Guilleme didn't have a sliver of guilt."
    scene bg black
    play sound "sfx/dripcrack.ogg"
    with flashblood        
    "The vicious pain took hold of her again, squeezing her stomach with murderous intent."

    "The pain was so great Rosa wasn't sure if the spell had failed or succeeded."
    m "Something is wrong."
    play sound "sfx/dripcrack.ogg"
    with flashblood      
    "Before Rosa could agree with Mother, she felt a sharp pain in her throat."
    "Rosa clutched her neck, a sharp jagged lump blocked her breathing."
    "It crawled up her windpipe, tearing the soft walls as it moved about."
    with flashblood  
    if persistent.adult:
        scene bg rosachoke  
    else:
        scene bg rosachokesafe  
    "Rosa fell to her knees and gagged."
    with flashblood  
    if persistent.adult:
        "Huge drips of blood-spotted spit ran down her chin."
    "Mother remained calm, unaffected by Rosa's distress."
    "Finally, she opened her mouth and forced the vile thing out."
    scene bg black  
    play sound "sfx/stab.ogg"
    with flashblood
    "She kept her eyes shut, afraid to look at whatever had come out of her."
    play sound "sfx/blood.ogg"
    with flashblood
    "But the choking feeling gripped her, and she puked again."
    scene bg rosaroomdark   
    if persistent.adult:
        "The liquid dripping down her mouth thickened and congealed. It wasn't spit anymore, but blood."
    else:
        "She spat after she vomited. Her spit felt thick in her mouth."
    "Rosa panted. The gruesome effect had finally stopped."
    
    "Something on the floor reflected light."
    "She reached out with her hand, and the prick of something sharp made her recoil."
    "Rosa picked them up with shaking hands."
    if persistent.adult:
        scene bg needles  
    else:
        scene bg needlessafe  
    #"Horror mixed with the pain moving around in her throat."
    "{i}Needles.{/i}"
    "In her palms were a handful of long, metal needles."
    if persistent.adult:
        "She had regurgitated them along with blood and jagged pieces of flesh."
    "Rosa examined them with a horrified kind of curiosity."
    if persistent.adult:
        "She stuck one in her thumb and it drew more blood."
    else:
        "She stuck one in her thumb and it drew blood."
    "They were real."
    "They had materialized in her throat while casting the spell on Guilleme."
    
    "Rosa wiped her mouth."
    "There was something... {i}{w}wrong{/i} with him."
    "Something... potent and dark."
    
    "...Or could it be that she had botched the spell horribly?"
    "She had pushed her limits this time. She had gone too far."
    "But still, a tugging concern was forming. It was as real as the metal needles in her hand."
    "Rosa tried to stand up on her feet, but she was exhausted."
    "Her knees failed her, and she crumpled on the floor like a rag."
    
    call m021 from _call_m021
    
    "Rosa stared at the needles in her hand."

    "\"Who are you really, Guilleme?\""
    scene bg black     
    
    $renpy.pause(delay=None)
    if persistent.chap2WasReadBefore   is None:
        $persistent.chap2WasReadBefore  = True
        $persistent.currentLinesRead +=1
    call chap3 from _call_chap3
return    
