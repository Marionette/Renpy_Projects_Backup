label childish:
    scene bg black 
    stop music fadeout 2.0
    scene bg festival 
    play music "sfx/festival.ogg"
    "In the once slumbering town, the streets were alive with flowers."
    "Pretty young girls, wrapped in thin white dresses, lined up in their rows, tittering excitedly among themselves. "
    "Each maiden was armed with a basket brimming with flowers."
    "When the clock struck eight, it was the given signal."
    "Girl by girl, the rows progressed down the crowded street, their dresses twirling as they danced."
    "Colour scattered as they unloaded their baskets."
    "Dahlias, tulips, orchids, poppies, sweet peas, they all spiralled across the air and into the hands of the startled citizens."
    "The young men on the street sprang into action."
    "They cheered and hooted and clapped and laughed, and the girls curtsied to them in return."
    "Some intrepid boys even dared blow a kiss, hoping for a reward."
    "And when the girls blew kisses back, they reddened to the tips of their ears and hooted in joy."
    show rk happy
    b "Rose!"
    b "Hey, Rose!"
    show rk huh
    "At first, she didn't know who he was talking to."
    show rk shyblush
    "But then she saw the rose he flourished in front of her, like a gentleman's magic trick."
    b "Well, I'll have to call you something, right? How about Rose?"
    show rk sadblush
    "This particular boy had been at her tail for several days now."
    "The flower festival was a good excuse for romance."
    "It was around this time that the young men of the town went around wooing their prospective lovers."
    "Most would have gone for a taller, more outspoken type of girl, but for some reason, this boy was smitten with her."
    b "Go on, take it."
    show rk shyblush
    "She shook her head. She knew she didn't deserve it."
    show rk sadblush
    b "Again with that stone-cold act? Come on, you're breaking my heart!"
    show rk shyblush
    "He laughed gaily, enjoying the thrill of courtship."

    r "Why…"
    r "Why…do you love me so much?"
    show rk sadblush
    b "Is that what's bothering you?"
    b "I'll tell you one thing, Rose, and you'd better remember this for the rest of your life!"
    b "When someone loves someone else, there's no need for a reason."
    show rk shyblush
    b "I just love you, Rose!"
    b "Won't you at least smile at me?"
    r "You… love me?"
    "He flashed his best youthful grin."
    b "Sure, I love you! To the moon and back!"
    show rk sadblush
    "She knew she shouldn't take the rose. She knew it was wrong."
    "And yet, she also knew, at this instant, that her face was burning hot."
    "Her fingers closed on the rose."
    "Even as she felt the thorns on her skin, she still held onto it."
    "The expression on the boy's face was one of absolute bliss."
    show rk shyblush
    "He hooted and did a little dance."
    show rk sadblush
    b "I do love you Rose! I really do!"
    "He grinned at her."
    show rk happyblush
    "To her surprise, she found herself smiling back."
    #Added#
    "A warm, pleasant feeling gushed inside her."
    "It was like tucking into a hot, home-cooked meal."
    hide rk happyblush
    scene bg black 
    stop music fadeout 2.0
    #transition to scene of Rosa's house
    scene bg rosahouse 
    r "Mother, I'm home!"
    show rk happy
    "Nowadays, she and her mother lived in a quiet cottage, far away from the main streets."
    "The joy and exuberence of the flower festival had long since faded away now, leaving her with the stillness of the lonely house."
    show rk huh
    play music "sfx/bitterness.ogg"
    r "Mother? Are you home?"
    show rk err
    "There was no answer. Not even a sound."
    "Usually, her Mother would have heard the door open by now."
    "She would run up and plaster her with hugs and kisses."
    "Now, however… the unnerving silence meant one of two things."
    "One, Mother was not here. Which wasn't possible, because she was always here."
    "Or, two-- "
    "Mother was angry."
    "The child felt a chill run down her spine as she realised."
    show rk sad
    "Was it possible… that Mother had her suspicions… and had followed her?"
    r "Mother? I'm coming inside now."
    play sound "sfx/doorslam.ogg"
    "The sound of the door closing was like a clash of thunder."
    "Rosa descended deeper into the house."
    "Mother was in the kitchen."
    "She was bent down with her back to the doorway, washing clothes in a wooden basin."
    "She looked just like a normal mother, but the girl knew better."
    show rk scared
    "Because just above Mother hung the cross."
    "It was a heavy, wooden crucifix, and it had been there as long as the child could remember."
    "It was so solid that if it were to drop, it would crush someone's toe."
    show rk sad
    "The girl knew this well. Having felt the cross so many times, she knew exactly how heavy it was."
    "The sharp corners of the cross were especially capable of drawing blood."
    "Mother dipped her hands into the water."
    "{i}Squich, squich.{/i}"
    "She crushed the clothes in a vise grip."
    show rk scared
    mn "Where did you go?"
    "Her sudden question sliced through the air, and the child almost jumped out of her skin."
    show rk sad
    r "..."
    r "J-Just the marketplace, Mother."
    "She tried to press the plump red rose behind her, to stomp on it and make it disappear into the ground."
    "But it was too late."
    show rk scared
    mn "..."
    r "I--"
    show rk dread
    "Mother stood up."
    r "Mother."
    r "It's not what you think, I swear."
    r "I'm not planning to see him again. I just wanted to make him happy, that's all."
    "If she looked at Mother any longer she thought her courage would dry up, so she quickly glanced at her feet."
    r "I-I'll throw away the rose. I'll make sure you never see it again. So--"
    hide rk scared
    stop music
    play sound "sfx/hit.ogg"
    with flashblood

    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    scene bg scaredrosa
    "The blow came so fast she never expected it. Suddenly she was on her knees, her skull throbbing in pain."
    "She looked up just in time to see her Mother raise the cross another time."
    "Although she knew it was no use running, she scrambled away all the same."
    r "Mother, I'm sorry! I won't do it again!"
    with flashblood
    play sound "sfx/hit.ogg"
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    #note: here past Mother is referred to as 'mn' because she isn't a disembodied spirit yet and thus, does not need an nvl mode.
    mn "How much do you think raising a child costs, you little rat?!"
    r "Mother, Mother, please-- "
    with flashblood
    play sound "sfx/hit.ogg"
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    "Undeterred, the cross slammed hard onto the girl's collarbone."
    "She shrieked, rolled over and tried to get back to her feet."
    mn "I clothe you, I house you, and I even feed you!"
    #Added
    mn "I protect you from everything that might harm you!"
    ##
    mn "And yet, I ask nothing in return! Absolutely nothing!"
    
    mn "Didn't I tell you not to go to that festival?!"
    mn "Yet you just can't help shaking your hips at those men, can you?"
    if cynicalmom:
        mn "All of them are the same, didn't I say it?"
    else: 
        mn "You are to avoid them, didn't I say it?"
    with flashblood
    play sound "sfx/hit.ogg"
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    "Up and down came the cross."
    "By now she had resorted to curling up into a ball and covering her eyes."
    "She cried out her pleas, her vows of obedience and love."
    mn "Do you have any idea how much I've sacrificed?"
    mn "What have I wasted my life for?"
    if badmom:
        mn "To be stuck with a filthy monster who betrays me every chance she gets?"
    else:
        mn "To be stuck with a stupid child who doesn't know how to listen?"
    #Added
    mn "I have told you time and again!"
    mn "{i}Do not disobey me!{/i}"
    r "M-Mother!"
    ##
    mn "I should have smothered you when I found you!"
    mn "You are a curse!"
    mn "I do all of this for you, to protect you!"
    mn "And you repay me how?"
    mn "With lies and betrayal?"
    mn "I should have thrown you out the window and watched the crows feed on your remains."
    mn "It's not too late now, don't you think?!"
    mn "Maybe I should teach you a harder lesson."
    mn "Maybe I should leave here right now and never come back-- "
    "Worse than any physical pain, the girl felt a despair so big it made her heart burst."
    "The child clung to her mother's legs."
    r "Please, Mother, please don't leave me!"
    r "I'll atone for this somehow, Mother. So, please, stay with me-- "
    if persistent.adult:
        mn "You are beyond atonement, you degenerate whore!"
    else:
        mn "You are beyond atonement, you dirty child!"
    with flashblood
    play sound "sfx/hit.ogg"
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    "With one final strike Mother sent her spinning to the ground."
    "The Cross had hit her face. The girl tried to open her eyes, and felt something warm trickle down her temple."
    "She lay on the floor, crying."
    "As her tears mixed with blood, she agonized whether Mother really was going to walk out of the house."
    "She could still hear Mother's footsteps, feet thudding near to her head."
    "At first they were hard and fast, then slow and hesitant."
    "At some point in time, the girl realised that the blows had stopped."
    "She dared not raise her head from the floor, so she waited."
    "Something touched her head. It wasn't a cross, but a soft, warm hand."
    play music "sfx/sadness.ogg"
    "A sound of a sob."
    scene bg rosahouse 
    mn "Darling?"
    mn "I-I'm sorry."
    mn "Oh, I'm so sorry. What have I done..."
    "The girl tensed, but she allowed Mother to sit her up."
    "The next thing she knew, Mother had wrapped her arms around her."
    "She was still crying."
    mn "You poor thing."
    mn "I'm so sorry. Mother is so stupid."
    "Her tears were genuine and mournful. The sorrow in her eyes hurt a million times more than any blow."
    mn "I shouldn't have done that... I..."
    "The woman stared at her hands."
    "She dropped the cross as if it was spoiled meat."
    "The girl let her mother hug her."
    "It was her fault, anyway. She had disobeyed Mother. She deserved the punishment."
    "She drowned herself in her arms and felt the familiar surge of love."
    "This was home."
    "{i}Home.{/i}"
    "No matter how broken."
    "Life before Mother was a blur. She was nothing without her."
    "Mother looked into her eyes and touched her face, wiping away her tears."
    if persistent.adult:
        "She locked her lips around hers and delivered a long, deep kiss."
    mn "I love you so much, my darling."
    mn "Please, forgive me..."
    r "I love you too, Mother. Don't cry."
    mn "...Oh, you're bleeding! Wait here."
    "Mother sat her on a chair and returned with a roll of bandages."
    "She began nursing her child's head with delicate care."
    r "I'm sorry, Mother."
    mn "No, no, I'm the one who's sorry."
    mn "Forgive me for what I said."
    mn "You know I would never leave you, right?"
    mn "Even if you have committed the foulest sin, I will never desert you."
    mn "I will always be by your side."
    r "T-Thank you, Mother."
    mn "I get worried, darling, you understand?"
    r "Yes..."
    mn "I am very afraid. Always afraid."
    mn "..." 
    "The woman's voice dropped into a whisper."
    "A sudden split second of lucidity."
    mn "Y-You... scare me."
    r "...?"
    "She shook her head, forgetting the thought."
    #Added
    mn "Just obey me from now on, promise?"
    mn "Mother knows what's best for you!"
    scene bg black
    r "Y-Yes, Mother."
    ##
    scene bg rosahouse
    "Later on, at dinnertime, Mother served her her favourite dish."
    "The vegetable and meat stew with brown gravy that only her Mother would make."
    "The child  tucked in eagerly, all the while feeling the cool bandage pressing lightly against her forehead."
    "The events of the past hour had already faded away into a distant memory."
    "Mother sat across the table, also eating. She seemed to be deep in thought."
    r "Mother?"
    mn "Hm?"
    r "I won't see that boy anymore. If he calls out to me I'll run until he can't catch me."
    mn "I know you will do the right thing, my darling."
    mn "..."
    mn "You didn't ask for all of this, did you, you poor thing?"
    mn "If only your father… was a better man."
    "Here, she pricked up her ears."
    "It was rare to hear Mother talk about Father, and even rarer to see her mention him so calmly."
    "All throughout her life she had wondered about the man whom Mother had fallen in love with."
    "Now it looked like she had the opportunity to glean a few more rare bits of information."
    r "Father..."
    r "Was he… good to you?"
    "Mother puckered up her lips and appeared to ignore this."
    "She decided to risk it and asked another question, tentatively."
    r "Did you... love him a lot?"
    "Mother's eyes were somewhere far away."
    mn "…"
    mn "I don't know."
    "No emotion, neither pain nor fondness, registered on her face."
    mn "...But he certainly loved me, back then."
    mn "...Maybe."
    mn "Now, I'm smarter. I know better than to trust men like him."
    mn "You, too, will understand when you grow up."
    mn "That people who love you will hurt you the most, and you will only have yourself to blame."
    mn "After all, you gave them permission to rearrange the awnings of your soul."
    mn "Do {i}not{/i} give anyone that permission."
    "The child nodded, accepting her mother's teachings."
    if persistent.origin:
        mn "I have laid to rest most of the hate burning in my heart when I found you, my darling."
        mn "You are my dearest daughter..."
        "A flicker of anger sparked in her eyes."
        mn "But one day, one day..."
        if justice:
            mn "His sins will catch up with him."
        else:
            mn "I will get my revenge."
    mn "Promise me, darling."
    stop music fadeout 2.0
    mn "When the time comes, and you meet a demon like your Father..."
    if justice:
        mn "You will do the right thing."
        mn "Deliver the punishment they deserve."
    else:
        mn "You'll take revenge for me."
    scene bg black
    #switch to present
    #bg of castle
    if persistent.childishWasReadBefore   is None:
        $persistent.childishWasReadBefore  = True
        $persistent.currentLinesRead +=1
    jump fleshyroom
    $renpy.pause(delay=None)
    
return    

label motherorigin:
    show gf furiousdown
    "{i}Fire.{/i}"
    "{i}Blood.{/i}"
    show gf maddown
    "{i}The poison of hate surging in his veins.{/i}"
    "Guilleme pushed the images away."
    "Memories had a taste, and this one was particularly bitter."
    "He locked it from his mind and vowed never to open it again."
    scene bg black
    m "Was it admiration? Respect?"
    m "{i}Spite?{/i}"
    m "The locket..."
    m "{i}I kept it to remember you{/i}"
    show bg firecg with dissolve
    m "Ana Sofia"
    m "{i}The woman who came close...{/i}"
    m "{i}To ending my existence...{/i}"
    m "{i}The woman who made me who I am today.{/i}"
    $ achievement.grant("Mother's Past")
    $achievement.Sync()
    g "I see...."
    show bg cathroomagape
    show gf sneer
    show rs shock at left
    show gf sneer
    show rs shock at left
    g "So this is {i}her{/i} doing."
    g "I should've known..."

return
