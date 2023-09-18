#BUILD 11

label intro:
    stop music fadeout 2.0
    $ save_name = "intro: mother"
    $persistent.IntroUnlocked = True
    if persistent.adult == True : 
        $achievement.grant("Playing as an Adult")
        $achievement.Sync()
    scene bg black with dissolve
    play music "sfx/rain.ogg" fadein 2.0
    play sound "sfx/run.ogg"

    $achievement.Sync()
    #sound of running
    m "I love you."
    nvl clear
    #show some bgs as she runs
    m "I love you. I love you."
    nvl clear
    #show more bgs as she runs
    m "I love you."
    m "There's no need to explain. It's only natural."
    m "A mother loves her daughter more than anything in the world."
    #flashes of something suggesting blood
    nvl clear
    m "My poor child."
    nvl clear
    m "How much did they hurt you this time, hm?"
    m "How much did you suffer?"
    m "Did they kick you and wound you when you declined?"
    m "Did they blame you for being {i}\"too friendly?\"{/i}"
    m "Did they laugh at your face when you begged them to stop?"
    m "Ahh..."
    if persistent.adult:
        m "Serves you right for being the brainless slut you are."
    else:
        m "Serves you right for being the dirty girl you are."
    #added
    nvl clear
    m "You deserve that pain."
    m "Savor it."
    m "Rejoice in it."
    m "It is your penance."
    m "Your punishment for not listening to your Mother."
    m "I warned you, didn't I?"
    m "There is no one else who understands you more than me."
    m "No one will protect you, but me."
    m "No one will {i}love{/i} you, but me."
    m "After all, how could anybody love something so monstrous like you?"
    m "…"
    m "Don't cry, my darling."
    m "Shh, it's alright..."
    m "Even if the whole world wishes you dead, I promise you this..."
    nvl clear
    m "Your mother will always be by your side."
    stop sound fadeout 4.0
    stop music fadeout 4.0
    #scene of a church, church doors open
 

    play sound "sfx/churchdoor.ogg"
    play music "sfx/church.ogg" fadein 3.0
    p "My goodness, child, what happened?"
    nvl clear
    show bg rchurch with slowdissolve:
        yalign 1.0
        linear 4.0 yalign 0.1
        time 20.0
    "A girl cowered behind the door of the church, her clothes soaked by the rain."
    "Her legs were covered in dirt and blood."
    "She lifted her head upon hearing the priest's voice and stared at him with blank eyes."
    show bg churchint with dissolve
    show rr sad with dissolve
    "The priest rushed forward to help her up."
    show rr dep
    p "My child, what happened to you?"
    u "..."

    "He ushered her to a pew."    
    p "Easy, now. Lean on my arm."
    "The girl did not speak at all, despite his questions on her welfare."
    "Thankfully, she did not seem to be hurt anywhere else, apart from the deep wound on her leg."
    "But the fear in her glassy eyes were palpable. She flinched every time he touched her."
    show rr sadclose 
    "The priest brought out some clean cloth and antiseptic. He wrapped her shivering shoulders in old robes."
    p "Did somebody hurt you? Were you attacked?"
    show rr dep
    p "You can tell me. We shall call the constable and have them face justice." 
    "The girl didn't say anything."
    
    u "..."
    p "..."
    p "It's fine."
    "The priest looked at the dirty, dishevelled girl."
    "Even with all the mud and grime smeared across her face, he couldn't deny that she was absolutely beautiful."
    "How old was she? Sixteen? Twenty?"
    "Her face was so young, her eyes captivating..."
    #"The priest had long since aged past his desire for the opposite sex, but somehow, something about her enraptured him."
    "When he realised his own thoughts, he steered his mind towards other matters." 
    p "You don't have to say anything if you're uncomfortable."
    p "No matter what happened, know that you are safe here."
    p "Nobody can hurt you anymore."
    u "..."
    show rr dep
    "The shook his head, upset at how this young girl seemed to carry bruises too easily, too conveniently."
    "It was obvious that her physical wounds were the least of the damages she carried."
    "He sighed as he finished treating her wound."
    "What could he say to comfort her?"
    "Would she even believe him?"
    p "You must think..."

    show rr confused 
    p "That the world is a cruel place."
    p "And it is... {w=0.1} It is..."
    show rr dep
    p "One cannot deny the very depths of cruelty we, humans, inflict on each other."
    u "..."
    p "...But please do not lose hope on the goodness of people."
    show rr huh
    u "..."
    u "It is there, I promise you."
    show rr dep
    p "As there are people who harm, there will be people who love."
    u "..."
    "The girl fidgeted."
    "She mumbled to herself, seemed to chew her tongue before she sputtered out the words."
    show rr sad
    u "G-God..."
    u "Will God... {w=0.2}love me even though I am a sinner?"
    "The priest beamed."
    p "O-Of course, my child!"
    "He sat closer to her, his heart beating with hope."
    "The years of spiritual training were for this, was it not?"
    "{i}For her...{/i}"
    "To save the wayward sheep caught in the brambles."
    "To care for a dejected soul in need of guidance, protection and love."
    "{i}Love.{/i}"
    p "What are we but pieces of coal polished to be gems in His grace?"
    p "God's love is unconditional, enduring and pure."
    p "It is all you need."
    p "My darling..."
    show rr confused 
    "He drew closer."
    p "Even if you are hurt, God's love will heal you."
    p "God's love will provide."

    show rr dep 
    u "..."
    show rr sadclose
    u "G-God..."
    u "...cannot protect me."
    p "..."
    p "W-What?"
    "With this utterance, the priest came to his senses."
    "In his frenzy for gospel, he did not notice his hand on the girl's thigh, planted lazily as if it had been there all this time."
    "He snatched it away in shock."
    "When did he--?"
    "The priest stood up. The sudden bloodrush made him feel sick."
    p "I... I must be unwell..."
    p "F-Forgive me..."
    u "..."
    show rr dep
    u "...I'm sorry."
    "Was she apologising to him, or to someone else?"
    "Her hair hid her face innocently, but the shadows on its surface made his insides coil as he stared at her."
    "This feeling..."
    "It was fear."
    show rr sadclose
    u "I'm sorry."
    "She repeated this phrase over and over."
    "After a while, the priest gathered himself. He wiped sweat off his brow."
    show rr dep
    p "Y-You are not to be blamed for this..."
    p "I will..."
    "The priest cleared his throat."
    p "I will have one of the sisters assist you."
    p "In the meantime, please rest."
    "With this, the man left."
    show rr dep
    u "..."
    "The girl remained seated on the pew, her head bent forward."
    stop music fadeout 5.0
    "As the priest's footsteps faded away, the entire church fell into silence."
    $renpy.pause(delay=None)
    #pause to set atmosphere?
    hide rr dep with dissolve
    u ".{w=0.2}.{w=0.2}."
    "She opened her mouth."
    show rr sad with dissolve
    u "No, I know."
    show rr angry with dissolve
    u "If I may say my piece, surely-- "
    show rr dep with dissolve
    u "…"
    show rr sadclose with dissolve
    u "Yes. Yes, Mother."
    show rr dep with dissolve
    u "But he is so very kind-- "
    
    call motherfirst from _call_motherfirst

    nvl clear
    
    m "How am I going to mind you like this?"
    m "You attract so much misfortune everywhere you go."
    u "..."

    call mothersecond from _call_mothersecond    
    u "..."
    "The girl sat in silence."
    "Mother was right, after all. She was always right."
    show rr sadclose
    "Everything was her fault."
    "Her fists shook with a mixture of fear and conviction."
    "She had to do penance."
    u "Mother."
    show rr dep
    u "Give me strength."
    u "...There is something I wish to do."
    "The girl rose from the pew."
    scene bg black with dissolve
    "In front of her was the altar, and on top of the altar was an ornately decorated cross."
    "It was as wide as her head, and the tip of the cross had been crafted such that it was razor sharp."
    "She whispered a prayer, the same one she has taught herself ever since she could speak."
    "A prayer of contrition; Of penance and sorrow."
    nvl clear
    o """{size=20}
    {i}Lord have mercy on me,\n
    A poor unfortunate soul,\n
    Extend Your mercy on my heart,\n
    So I may not sin no more.
    {/i}{/size}
    """
    nvl clear
    "She knelt in front of the giant cross, staring at the deity's face, contorted in torment and agony."
    "{i}Pain...{/i}"
    "Pain was good."
    "Pain washed away your sins and made you pure."
    m "Don't tell me…"
    m "You're quite sure you're doing this?"
    nvl clear
    "The girl's arm trembled ever so slightly."
    u "What other way is there for me to atone?"
    "She picked up the cross."
    m "Oh, my darling daughter."
    m "Mother is proud of you."
    nvl clear
    "Slowly, she brought the sharp end close to her face."
    "So close that it hovered just above her left eye."
    "And with a final gasp of breath she…"
    with flashblood
    play sound "sfx/knifeslash.ogg"

    show bg black
    $renpy.pause(delay=None)
    if persistent.introWasReadBefore   is None:
        $persistent.introWasReadBefore  = True
        $persistent.currentLinesRead +=1
    call chap1 from _call_chap1
return
    
