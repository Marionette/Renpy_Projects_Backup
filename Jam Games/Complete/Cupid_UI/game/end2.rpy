label end2:
    $save_name = "end2: dawning"
    if(persistent.Ending2Unlocked == False):
      $persistent.Ending2Unlocked = True
      $ persistent.EndingUnlocked +=1
      
    stop music fadeout 2.0
    scene bg black  
    "Guilleme woke up with the fading dream still in his memory."
    show bg cathroomagape with slowdissolve
    "He was not in his room, but in Catherine's."
    play music "sfx/confront.ogg" 
    show gf angry at right  
    "This did not surprise him."
    "Whoever cast the spell did not do so on a whim."
    "To take him away from his sanctuary was to render him weaker."
    "A pure, white candle flickered on the table, its flame looked as though it was ready to go out."
    u "I couldn't save you."
    u "I tried."
    show rs think at left with Dissolve(2.0, alpha = True)
    "Rosa stepped out of the shadows."

    show gf annoyedtalk at right  
    g "You--!"
    "Guilleme stared at her with irritation."
    show rs norm at left  
    g "What is the meaning of this, Rosa?"
    g "This is your doing?"
    show rs think at left  
    "She looked at him with sadness."
    show rs dep at left  
    show gf angry at right  
    r "I was too weak to save you, Guilleme."
    g "Save me from what?"
    r "From what you are."

    "Guilleme's face crumpled into confused anger."
    show gf pissed at right
    g "I didn't expect such contempt from someone I trusted."
    show rs hmp at left  
    show gf angry at right  
    r "Do you expect me to ask your forgiveness for what I've done, Sire?"
    r "Because I won't."
    r "I will stand by what I did."
    r "I will do it again if I can."
    show rs think at left  
    r "But such a spell requires much preparation."
    
    show gf pissed at right      
    g "You are not to do that again, do you hear me?"
    g "I will not allow myself to be subjected to such an insult."
    
    show rs pissed at left  
    r "I'm not doing something that petty!"
    r "I am trying to save you--"
    
    show gf mad at right  
    g "I do not know what you're talking about!"
    g "If you persist in this foolish behavior then I will be forced to take action."
    
    r "Go ahead."
    r "But I will simply try again."
    g "Stop it!"
    
    show gf grr  :
        xalign 0.35
    "Guilleme grabbed her shoulders, shaking her with irritation."
    "They stared at each other in heavy silence, and Guilleme somewhat regretted his forcefulness."
    
    show gf maddown  
    "But Rosa did not flinch or look away, even at his outburst."
    "There was no fear or fragility in her eye at all."
    "She held her steady gaze until it was Guilleme who looked away."
    
    g "Why--"
    show gf pissed  
    g "Why are you doing this?"
    g "You should know how pointless it is."
    show rs norm at left  
    r "I had to try, Guilleme."
    show rs think at left  
    r "If there is a way to save you, I am inclined to take it."
    show rs hmp at left  
    r "I had hoped Catherine's memory might work on you."
    show gf maddown  
    g "..."

    r "Guilleme, I cast a spell to give you her memory--"
    show rs pissed at left  
    show gf furious  
    r "--So you don't have to resort to feeding."
    show gf furious  :
        xalign 0.5   
    "Guilleme recoiled from her like her skin was scalding to the touch."
    show gf furiousshock  :    
    g "You--"
    g "How did you--"
    
    "Rosa just stared at him, her eye clear and resolute."
    
    r "I know what you are because we are the same."
    r "We are creatures that emanate desire and feed on love."
    show rs frownclose at left  
    r "I have lived with this curse knowing only a semblance of what I am."
    r "Mother taught me how to control it, even in her own twisted way."
    show rs hmp at left  
    r "I was lucky, Guilleme. I wasn't alone."
    show rs dep at left  
    r "..."
    show rs hmp at left  
    r "But you were."
    show rs dep at left  
    "Rosa's eye bloomed with sadness."
    r "I can only imagine... How hard that must've been."
   
    show gf furiousshock  :    
        xalign 0.55
    "Guilleme staggered back in shock."
    show gf furiousdown  
    "So there was another one like him."
    "A desperate hope clutched onto him like talons."
    "Was that why he had taken to her so without wanting to feed on her?"
    
    show rs hmp at left  
    r "That's why I am doing this, Guilleme."
    r "I wanted to give you Catherine's memory, like how Mother's memory keeps me sustained."
    r "Love doesn't have to be taken like this. There are other ways."
    
    "Guilleme frowned indignantly."
    show gf furious  
    g "Hmp. You talk as if you have all the answers."
    g "You're still very young. I can tell."
    g "I have already endured centuries of this curse."
    g "I know all the tricks to survive."
    g "From strangers to the villagers, I know how much I can take."
    g "I am meticulous."
    show gf maddown  
    r "Then why must you insist on {i}this{/i} method--"
    show gf petulantsmile with Dissolve (0.5, alpha=True)

    "With no reason to stand for ceremony, Guilleme's face changed easily."
    show rs pissed at left  
    "Rosa's jaw clenched."

    "She was talking to a stranger now."
    "His face lost the virtue that once belonged to a blameless man."
    "It was replaced by a curious, cheeky grin, a perpetual look of childlike mischief."
    "This man irritated her, and yet, somehow, Rosa felt like she had known him for a lifetime."
    "He had always been there, hadn't he?"
    "Or rather, it had always been him."
    
    g "Why?"
    g "Because it is fun."
    g "And the taste is {i}worlds{/i} better."

    r "..."
    
    g "The experience of drawing out love is unlike any human feeling."
    g "It is transcendent."
    g "It is the only moment I feel alive."
    show gf sneersmile  
    g "The only moment I feel like a god."
    g "Once you've had a taste of it, nothing else compares."
    g "You must try it!"
    g "I bet you can only afford to be self-righteous because you don't know any better."
    show rs angry at left  
    r "You're wrong! I did it to Catherine."
    show gf newtalk  
    r "I tasted her love, but I was able to stop myself in time!"
    r "I knew it would destroy her!"

    show gf sneer  
    g "So that was you, hm?"
    g "It makes sense that Catherine's love for me waned."
    g "That never happened before."
    

    r "Desire can be controlled, Guilleme!"    
    show gf petulant  
    g "I do not wish to control it!"
    g "Why should I?!"
    show gf sneer  
    show rs aww at left  
    g "Admit it, you've longed for that taste since your tongue dipped in its pot."
    show rs dep at left  
    "Rosa did not speak. She shifted nervously on her feet."
    "Guilleme went on."
    show gf newtalk  
    g "We are given this curse to endure, Rosa."
    g "Why must we scutter in a corner and humble ourselves?"
    g "To whom do we abdicate ourselves to?"
    show gf petulanttalk  
    g "To normal people?"
    show gf sneer    
    g "They are beneath us."
    g "For all their achievements and talents, love is the one thing that can drive them mad."
    g "Don't you see?"
    g "Their weakness is the one thing we feed on."
    show gf sneer  
    g "It is the natural order."
    
    show gf newsmile  :
        xalign 0.45
    "Guilleme stepped closer to her and touched her bare arm. He tried to hide his bliss."
    g "I told you before."
    g "If you need power, then be powerful."
    show rs hmp at left  
    g "I will teach you how to wield it. You still have much to learn."
    g "If you will join me, Rosa, just imagine what we can do."
    show gf sneer  
    g "We will be powerful, you and I."    

    
    "Rosa's momentary confusion faded."
    show rs pissed at left  
    "The hard look appeared on her face once again."
    show rs angry at left  
    show gf newtalk  
    r "I will {i}never{/i} join you."
    r "You use people for your gain!"
    show gf newgrr  
    g "So?!"  
    show rs pissed at left  
    "Guilleme's voice couldn't keep from rising."  
    g "What of it?!"
    g "Isn't it the rule of human existence?"
    show gf sneer
    g "It's all a game, Rosa."
    g "A game I play to win!"
    show gf petulantnormal  
    show rs angry at left 
    r "So people's lives are a game to you?"
    show gf petulantsmile
    show rs pissed at left  
    "Guilleme shrugged."
    g "Of course they are."
    show gf petulantnormal
    show rs hmp at left
    r "..."
    g "Humans use and abuse and they throw away on whim."
    g "They destroy for no apparent reason except that they want to."
    g "It took me the longest time to understand why."
    show gf haughty
    g "I realised it is simply their nature."
    g "Humans don't play fair, but I do."
    show gf petulantsmile
    g "And I still get ahead."
    show rs angry at left

    "Rosa's eye narrowed at Guilleme."
    show gf  petulantnormal
    r "How can you throw people away so easily?!"
    r "Don't you see that there are good people, like Catherine?!"
    show rs pissed at left  
    r "You are afraid to remember. You are afraid to give them the worth they deserve!"
    show rs angry at left 
    r "You rejected her memory, content to forget her value!"
    show gf maddown
    g "..."
    "Guilleme was silent for a few moments."
    show gf petulantsmile 
    "Then he gave a low snicker."
    show rs aww at left
    g "Rosa, Rosa, Rosa."
    show rs confused at left
    g "That is... an amusing thesis."
    show gf petulantsmilesmirk    
    "He looked at her dumbfounded face pitifully."
    #"So earnest she was, so passionately she spoke."
    # "But now her mouth hung open, like she was having a hard time processing his response."
    show gf haughty
    "Another chuckle escaped. Guilleme couldn't help it."

    #"She really wanted to change him, didn't she?"
    #"It was so precious in its stupidity."
    show gf petulantsmile
    g "You got me all wrong, Rosa."
    g "I do not undervalue people." 
    show gf petulantsmilesmirk
    g "In fact, I {i}love{/i} them!"
    g "I revere them. I am grateful."
    show gf haughty
    g "They sustain me, after all."
    show rs disturbed at left
    g "That alone deserves all the appreciation and care I can give."
    r "..."
    show gf petulanttalk 
    g "I loved Catherine."
    g "...With every fiber of my being."  
    g "She was a kind soul. She tasted... {i}perfect{/i}."
    show gf petulantnormal
    g "But I think you underestimate how long I've been on this dirty, forsaken rock."
    show rs pissed at left     
    show gf haughty
    g "Good people are not rare and precious treasures."
    g "As such, they are not to be handled any differently from the rest."
    show rs mad at left
    show gf sneer
    r "What...?"
    show gf newtalk
    g "And all this talk about {i}worth{/i}..."
    show rs shock at left
    show gf petulanttalk
    g "Do you mean some people are worth more than others because they are {i}\"kind\"{/i}?"
    show rs confused at left
    g "What if from now on I only consume bad people?"
    show gf haughty
    g "Or how about those in the lowest caste of society? Ruffians. Rapists. Thieves."
    g "It is easy to be kind when you are privileged."
    g "But those poor, unworthy souls... Surely no one would miss them!"
    show gf sneer
    g "Would that make you feel better?"
    "Rosa faltered."
    show rs despair at left
    r "T-That's not what I'm saying!"
    show gf petulanttalk
    g "That is {i}exactly{/i} what you are saying."
    show rs confused at left
    g "You're telling me I shouldn't feed because there are good people out there that deserve better."
    show gf haughty
    g "So if they're bad, it is alright?"
    show rs disturbed at left
    show gf sneer
    g "How terribly judgmental of you."
   
    show rs disturbed at left
    r "...No... I..."
    show gf petulanttalk
    show rs dep at left
    g "Every human being has a capacity for kindness or cruelty."
    g "To judge somebody on such a volatile detail, that is prejudice."
    show gf think
    g "After all, a kind man can mull the death of his fellow man, no sooner than a criminal can turn a new leaf."
    show gf pissed
    g "The truth is, there are no good or bad people."
    g "There are just... people."
    show gf newsmile
    show rs shock at left
    g "...And I'm not picky."
    $ achievement.grant("Guilleme's Soliloquy")
    $achievement.Sync()
    show rs angrycrynothuh at left
    show gf petulantnormal
    r "Stop saying that!"
    show rs despair at left
    r "You don't really believe that, do you?"
    show rs poorcry at left
    r "You hurt like me!"
    r "You want acceptance like me!"
    show rs sadcry at left
    r "I know deep inside you want something more."
    r "More than a feeding or a craving!"
    r "You've written as much in your diary--"
    show rs confused at left
    show gf petulanttalk
    g "You sneaky little minx."
    g "Didn't I tell you you were not supposed to touch that?"
    show rs poorcry at left
    show gf petulantnormal

    r "{i}Stop!{/i}"
    r "P-Please stop this, Guilleme."
    show rs sadcry at left
    r "I implore you!"
    show gf petulant
    "Her pleading face stirred something in Guilleme."
    show gf think
    "But the calluses in his heart had decades to harden."
    "He snorted."
    show rs pissedcry at left
    show gf petulantnormal
    g "Or what?"
    g "What do you plan to do, little girl?"
    show rs confused at left
    r "..."
    g "Is this it? Is this your plan?"
    g "Put on a light show and talk me to death? Surely you didn't think it would be that easy."
    show rs confused at left

    r "..."
    show gf sneer

    g "If you have a different offer, I'm all ears."
    show rs dep at left
    r "..."
    g "Hm. I thought as much."
    #g "Well, good talk."
    #g "Albeit a little pointless, I'm sure you'll agree."
    show rs pissed at left
    show gf newnormal
    r "..."
    r "Is that what you think of Catherine, then?"
    show gf petulantnormal
    r "Nothing but... {i}cattle{/i}?"
    "Guilleme winced despite himself."
    r "I loved Catherine..."
    r "I know you, too, loved her completely, whether you admit it or not."
    r "You can't take love without giving it, can you?"
    g "..."
    show gf maddown
    "Guilleme sighed in annoyance."
    show gf haughty 
    g "Just another spoke in the old, fun wheel."
    show gf petulantnormal
    r "You're lying if you say you are not the least bit troubled by your actions."
    show rs pissedcry at left
    r "That's a start, Guilleme. The first step."
    show rs pissed at left
    r "It means you are not as cold as you want to appear."
    show gf petulant
    g "..."
    r "If you admit your guilt and take responsibility for her death--"
    "Guilleme waved her away with an indifferent scoff."
    show gf petulanttalk
    show rs pissedcry at left
    g "I refuse."
    show gf silentpain
    g "Her death was her own decision. I had no hand in that."
    #g "She reaped what she sowed, and I collected. That is all."
    show rs shock at left
    r "...!"
    show gf haughty
    "With this validation, the assured smile came back to his lips."
    "He shrugged."
    g "Who knows, maybe she could've gotten better over time?"
    g "Most people bounce back from the loss of love."
    g "Or not..."
    g "Who really knows?"
    r "..."
    show gf sneer
    g "Is it my fault she gave me everything? I didn't force her to."
    r "..."
    g "Which was only fair. Like you said, I didn't hold back." 
    g "It was an equal exchange."
    show rs confused at left
    "Rosa's throat went dry."
    show gf haughty
    g "Oh, love."
    g "Love is the strongest force in the world."
    show gf petulantnormal
    g "But it is never pure."
    g "Always tainted, always poisoned."
    r "What are you talking about?"
    show gf sneer
    show rs confused at left
    g "Well, I hate to shatter this vision you have of Catherine, but she wasn't so righteous."
    show gf petulantnormal
    show rs disturbed at left
    g "She was as selfish as everyone else."
    show rs angrycrynothuh at left
    r "What?!"
    g "Think back, Rosa."
    if cathselfish:
        show rs disturbed at left
        g "Did you {i}really{/i} think her sister's death was a complete accident?"
        g "Wasn't it convenient?"
        $ achievement.grant("Emilie's Fate")
        $achievement.Sync()
    else:  
        g "All of our fights started because of her jealousy."
        show rs disturbed at left
        g "She couldn't stand the thought of somebody else getting a slice of her pie."
        g "And why not?"
        $ achievement.grant("Jealous Catherine")
        $achievement.Sync()

    g "Wasn't {i}I{/i} convenient for little Miss Perride?"
    r "..."
    show gf haughty
    g "Yes, of course. Convenient and perfectly adequate."
    g "Sweet, boring, obliging Marquis de Gul."
    g "Wasn't he so easy to love?"
    show gf petulantsmile
    g "He could help her achieve her grand dreams, give her the good life that hovered just beyond her reach."
    g "After all, Guilleme didn't seem to have any plans of his own, did he?"
    g "As if satisfied to exist only for her?"
    g "Honestly, what a catch."
    g "What an impressive... {i}pedestal.{/i}"
    show gf petulantnormal
    g "Even when the core of this love poisoned her, she made no attempts to leave."
    g "I wonder why?"
    show gf sneer
    g "Ah, now there's a question."
    show gf haughty
    g "Why, indeed?"
    show rs angrycrynothuh at left
    show gf newnormal
    r "Because she had hope, Guilleme!"
    r "She stayed hoping her feelings for you would return!"
    r "That was how much she loved you!"
    show rs sadcry at left
    show gf sneer
    "Guilleme scoffed."
    g "Aww. How sweet of you to say."
    g "You really thought Catherine stayed with me just for love?"
    show gf haughty
    g "And not at all because she was... scared? Insecure?"
    g "...Comfortable?"
    show gf sneer
    "Guilleme tapped his chin in mock contemplation."
    g "Or maybe..."
    g "She just wanted so badly to be a Marquis' wife?"
    g "Such a proud girl, she was."
    g "Must she settle for anything less?"
    g "That will show all the people who used to scorn and underestimate her."
    if persistent.adult:
        g "They, who called her sister a whore; the ones who called her and her mother mad."
    else:
        g "They, who gossiped about her family behind her back."
    g "That will show them."    
    show rs disturbed at left
    "Rosa took a shaky step back."
    if cynicalmom:
        "Mother's words forced themselves into her head."
        m "They are all the same."
        m "They are all selfish."
        show rs angrycrynothuh at left
        "Rosa bit her lip."
    r "It is not true!"
    r "I won't believe it!"
    show rs mad at left
    r "Catherine was a kind person!"
    show gf petulantnormal
    g "So what?"
    show rs disturbed at left
    r "..."
    #g "Does it matter?"
    g "Does being kind justify selfishness?"
    g "Does being kind even save anyone?"    
    r "..."
    show rs pissedcry at left
    r "You..."
    r "You are... heartless."
    show gf haughty
    g "Maybe."
    show gf sneer
    g "It has been so long I can't tell."
    g "Always, the love of self is first, Rosa. I don't take it personally."
    show rs angry at left
    show gf newnormal 
    r "Shut up!"
    r "Don't you ever get tired of justifying your hunger?"
    r "So, Catherine wasn't perfect, yet you simply pass the blame."
    r "All just excuses!"
    r "The truth is, you just don't want to stop, do you?"
    show gf petulant
    r "You're no god. No higher being."
    r "You're nothing but a common vampire! A monster!"
    "Guilleme's face twitched."
    r "Feeding on the love of the people who love you?"
    r "You must know how wrong that is--"
    stop music fadeout 2.0
    "Guilleme's fist shook visibly, but he kept his smile. His voice remained pleasant and calm."
    show gf petulantsmile
    show rs pissed at left
    g "So you compare me to storybook monsters now, Rosa?"
    g "How insulting."
    g "But yes. Wouldn't it be easier if I dined on blood or flesh?"
    show gf haughty
    g "Something tangible, perhaps. Something physical."
    g "Things would've been so much simpler."
    g "After all, if I drank blood, I wouldn't have to tangle with their lives."
    show rs confused at left
    show gf furious
    "He turned to Rosa, his eyes burning.  She could feel the heat in his stare."
    g "I wouldn't have to be {i}sane{/i}."
    "Guilleme's voice shook with anger. She flinched."
    show gf furiouser
    g "You {w=0.2} stupid, {w=0.2}arrogant, {w=0.2}self-righteous minstrel {b}{i}dare{/i}{/b} talk to me about guilt!?"
    show rs disturbed at left:
        xalign 0.1
    g "How {i}{b}dare{/b}{/i} you call me a monster!"
    g "You chastise me, singing songs of praise for the greater good."
    g "Have you ever tasted your own betrayal on the lips of the person you love?"
    g "Do you know what it's like to strangle hope with your own hands?"
    r "..."
    g "I look into their eyes and see them die from the inside out."
    g "Am I worth it? Am I worth all their lives?"
    g "{i}Never!{/i}"
    g "But I do it again and again. Again and again. Just for the right to exist."
    g "You read my journal and act like you know me."
    g "You know {i}nothing!{/i}"
    g "I wish I {i}was{/i} a monster--"
    g "Maybe then, I wouldn't have to {i}feel!{/i}"
    r "..."
    "The silence reigned between the two of them."
    show gf furiousdown
    show rs emocry at left:
        xalign 0.1
    "Guilleme's face went blank after his outburst, almost confused at the words that came out of his mouth."
    show gf haughty
    "He forced his lips into a placated grin."

    g "P-Pardon me... I..."
    show gf silentpain
    g "I didn't mean to shout."
    "He took a deep breath and refused to speak again."
    show gf maddown
    "Rosa buried her face in her hands."
    "He was right. She had come here with an overestimation of herself."
    "Her ethics were the cries of a child."
    "How could he listen to someone immersed only in her own tender ideals?"
    "If she wanted to help him, she had to know his pain."
    "But what could she say? Her mind struggled with the words."
    "They all sounded artificial in her head."
    "All she could do was hold out her hand to reach him, couldn't she?"
    show rs sadcry at left
    "She could offer him hope; a little warmth away from the chunk of ice beating inside of him."
    "She approached him, tentatively."
    r "I-I'm sorry..."
    r "I shouldn't have spoken such hateful words--"
    r "But, don't you see? You don't have to endure this pain anymore."
    r "I am offering you a different path, Guilleme."
    r "Let me help you..."
    g "..."

    "He didn't speak, nor move."
    "Rosa held on to the pain she saw in his eyes a moment ago. It was her only hope..."
    "But if there ever was a trace of it in his face, it had flitted away before it took substance."
    play music "sfx/spider.ogg"
    show gf furioussneer
    "His abject face contorted into a grin. He chuckled."
    show gf petulantsmilesmirk
    "Then his laughter filled the room; cold, bitter laughter that chilled her skin into a shiver."
    show rs disturbed at left
    "Rosa drew her hand away in fear."
    show gf furioussneer 
    g "You really don't get it, do you?"
    g "I meant to say that this,"
    g "{i}This{/i} is what makes it worth it."
    g "It is... {i}precious{/i}."
    r "W-What?"
    g "Make no mistake, I endure all this not for something as silly or disposable as blood."
    show gf haughty
    g "{i}Love.{/i}"
    g "Love is worth all the pain."
    show gf petulantsmilesmirk
    g "The best wine tastes like the very dirt from which it was exalted..."
    g "And that is all I want."
    g "Nothing else compares."
    show rs disturbed at left:
        xalign 0.1
    "Rosa's mouth dropped in horror."
    show gf petulantsmile
    "She stepped away from him."
    "A cold shiver passed her spine."
    show rs despair
    "{i}No. No...!{/i}"
    show rs angrycrynothuh
    r "No... Guilleme!"
    show rs despair
    show gf petulantnormal
    #show rs sadcry
    "She stared at him, grasping at the flicker of hope that came as fast as it went."   
    
    scene bg polaroid9dark

    nvl clear
    o "He had built a kingdom from the maze of his own heart."
    nvl clear
    o "Both ruler and prisoner, both exalted and doomed."
    nvl clear
    scene bg polaroid10
    o "She could feel the cracks in his armor, the crumbling of a wall."
    nvl clear
    o "He wanted to get out."
    nvl clear
    o "Rosa thought she saw light in his darkness."
    nvl clear
    o "A hand reaching out to be saved."
    play sound "sfx/glassbreak.ogg"
    scene bg polaroid10break with flash


    nvl clear

    o "...But where was it now?"
    scene bg black with None
    nvl clear
    o "...Where was this hope?"
    nvl clear
    o "...It was..."
    nvl clear
    o "...gone."
    nvl clear
    o "Had it ever been there at all?"
    nvl clear
    
    scene bg cathroomagape
    show gf petulantnormal
    show rs emocry at left
    "...Or did her desire to help him trick her into seeing what she wanted to see?"
    show rs frownclose at left   
    "Rosa bit her lip to steel herself."
    show rs pissed at left
    show gf newsmile
    r "..."
    g "Oh, don't look at me like that."
    g "I had the same morals as you when I was younger."
    show rs frownclose at left
    show gf newsmile
    g "But time smoothes out our rough ideologies."
    r "..."
    show rs angrycry at left
    r "I-I was wrong."
    show gf petulantnormal
    show rs emocry at left
    r "I thought I could still save you--"
    show rs normcry at left
    show gf petulanttalk
    g "You are quite full of yourself if you think you can {i}\"save\"{/i} people."
    show gf newsmile:
        xalign 0.45
    "Guilleme took a step towards her, and Rosa's throat closed up."
    show rs mad at left:
         xalign 0.1
    r "Get away from me."
    show gf newnormal
    g "I'm not going to hurt you, Rosa."
    show gf haughty
    show rs pissedcry at left
    g "If you wish to debate philosophy further, we can do so for a thousand more years."
    show rs confused at left
    show gf newsmile
    g "But aren't we ignoring the single, most potent truth?"
    show gf sneer
    g "We {i}found{/i} each other."
    g "So many souls running around this earth and we actually managed to meet."
    g "Do you realize how momentous this is?"
    g "Centuries, Rosa. I have wandered for, centuries."
    show gf amused
    g "To find someone like you is beyond my wildest imaginations."
    r "..."
    show gf newtalk
    g "I can give you love, Rosa."
    g "Forget Catherine or your Mother. They are remnants of a bitter past."
    show gf newnormal
    g "How long are you going to hang on to their memories, anyway?"
    if openlocket and not rgloves and family:
        show rs angry at left
        r "Love is not something to be thrown away, Guilleme."
        r "It endures."
        show rs frownclose at left
        r "I know this because I've loved Mother this long, despite the pain."
        if badmom:
            r "She was cruel, but now I understand she had my best interests at heart."
            $ achievement.grant("What makes a good parent?")
            $achievement.Sync()
        else:
            r "She was the first person to show me I matter."
        show rs pissed at left
        "From under the folds of her dress Rosa took out a locket."
        "It was the locket he had given her at the cliff."
        "Guilleme stared at it, confused."
        r "Remember the person in the picture, Guilleme?"
        show gf sneer
        g "Oh, you got it open."
        g "Pray tell, who is it? Is it the queen?"
        r "This is my Mother."
        $ achievement.grant("Dysfunctional Family")
        $achievement.Sync()
        show gf newtalk
        g "..."
        g "What?"
        "Guilleme's mind went blank for a moment."
        show rs frownclose at left
        r "I've felt something for you from the very beginning."
        r "My heart felt close to you."
        show rs dep at left
        r "I..."
        show gf pissed 
        r "I want to believe that is because we are family."
        show rs hmp at left
        r "Don't you see?"
        r "That's why I can't give up on your redemption so easily."
        r "I care for you more than you think, Guilleme."
        show gf maddownshock
        "Guilleme furrowed his brow."
        "Indeed, the woman in the picture stirred something in his memory."
        if persistent.origin:
            call motherorigin from _call_motherorigin
        else:
            "And yet, no matter how much he searched his memories he could not remember."
            "Was there such a woman that bore him a child in the past?"
            "A sudden hope dug its nails into his chest once again."
            show gf haughty
            "He answered this hope with contempt."
            "A force of habit."
            show gf sneer
            show rs shock at left
            g "Pardon me. My memory is a bit rusty."
            g "What was her name again?"
        show gf sneer
        show rs shock at left
        "Rosa parted her lips in disappointment."
        show rs mad at left
        r "Is that all you're going to say?!"
        show rs angrycrynothuh at left
        r "You were carrying my Mother's picture all this time!"
        show rs poorcry at left
        show gf petulantnormal
        r "You are my father, Guilleme!"
        show rs angrycrynothuh at left
        r "That is probably why we are the same!"
        show gf silentdep
        show rs sadcry at left
        "Curiously, there was an urge to take back his haughty words."
        "But Guilleme forced it down."
        show gf silentpain
        "This pain made him uncomfortable."
        "Her tears were starting to hurt him."
        if persistent.origin:
            "Whether that woman was behind this all, there was no doubt that Rosa..."
            "Rosa believed {i}he{/i} was her father."
        "He laughed and shrugged, and then promptly clenched his jaw."
        show gf haughty
        show gf petulantnormal
        "He didn't like how she made him aware of his own failings."
        "A sudden irritation at Rosa came over him, an itch to hurt her."
        show gf newsmile
        g "Oh, dear me. Forgive my cynicism, darling."
        "He scratched his chin to hide his distress."
        if persistent.origin:
            g "That woman {i}would{/i} want to believe I had a child with her, wouldn't she?"
            g "But the truth is, I never can."        
            show gf silentdep
            g "I am barren, Rosa."
            show rs poorcry at left
            r "Y-You're lying!"
            g "I'm not."
        else:
            g "That portrait is quite blurry..."
            g "...and I am barren."
        "Rosa staggered."  
        show rs pissedcry at left
        show gf newsmile
        g "How much of your Mother do you really remember?"
        g "I don't remember any being birthing me, do you?"
        r "...!"
        g "You must admit the possibility that this Mother you speak of--"
        g "--Was simply a stranger who took you in as her own, Rosa."
        g "Fueled by the force of our curse, she was deluded, possessive, and hysterical."
        g "I do not deny that I might be the root of her delusion."
        g "She must have searched for me... and found you, by accident, instead."
        "Guilleme shrugged."
        g "An alternate theory, but one that makes more sense."
        g "Now that we've met, that must mean there are others out there like us."
        r "W-What are you saying?"
        show gf haughty
        g "Simple."
        show gf sneer
        show rs disturbed at left
        g "Whoever created a pathetic thing such as me deemed it impossible to scatter my seed."
        g "It was just as well..."
        "There was a tinge of bitterness in his amused voice."
        show gf silentdep
        g "After all, to wish this curse upon somebody else, my child, nonetheless--"
        g "That {i}would{/i} make me a different kind of monster altogether."

        show rs sadcry at left
        "Rosa looked at the locket with shaking hands."
        r "Then why..."
        r "Why did Mother--"
        show rs normcry at left  
        "She remembered wandering, for a long, long time."
        "Alone and in a blur..."
        "And then..."
        "A warm hand reaching out to her..."
        show rs emocry at left
        "A home."
        "{i}Home{/i}."
        "She opened her mouth to say something, but promptly closed it."
        "The fight had vanished from her eye."
        show rs superemocry at left
        "Tears fell as she closed the pendant in her fist."
        "Guilleme fidgeted uncomfortably."
        show rs emocry at left
        show gf newnormal
        g "I-If you want to believe it so much, then I can pretend--"
        show gf silentdep
        show rs sadcry at left
        "Why did he say that?"
        "He admitted that he didn't expect the words to come out."
        "He was only mulling it over in his mind, looking at her dejected face."
        show rs emocry at left
        "It was pity, wasn't it? A favor out of pity for this poor, lonely girl?"
        "Or was it..."
        "{i}Penance?{/i}"
        show gf sneer
        g "...I don't mind."
        show gf silentdep
        "He did his best not to sound distressed."
        "Perhaps a part of him wanted it to be true."
        show gf newnormal
        "Guilleme looked at Rosa and felt the same stirring of affection he had for her through the years."
        show gf silentdep
        "It wouldn't be much of a stretch, would it?"
        "He could protect her and care for her like family."
        "They were the same. They need each other."
        show gf think
        "Hope began to sprout in his heart again."
        "That dastardly thing grew like a weed."
        "It veered dangerously close to breaking through his pride."
        "{i}Wouldn't it be a miracle...{/i}"
        show gf silentdep
        "A child of his own flesh and blood, standing before him, full of love, disappointment, and confusion."
        "Exactly how a child would look up to their parent..."
        show gf silentpain
        "{i}What a nice sentiment.{/i}"
        show gf haughty
        "By this time, Guilleme was already well acquainted with the dying screams of hope."
        "He knew which soft, secret places to push in order to kill it."
        show gf silentdep
        gt "{i}...You do not deserve that.{/i}"
        show gf sneer
        g "Of course, of course."
        "Guilleme laughed, almost a bit too loudly."
        show rs sadcry at left
        "Rosa winced." 

    show rs dep at left
    r "..." 
    show gf newsmile
    if openlocket and not rgloves and family:
        g "Don't look so troubled, my daughter."
    else:
        g "Don't look so troubled, darling."
    if openlocket and not rgloves and family:
        show gf sneer
        g "We're {i}family{/i}, aren't we?"
    g "Enough of such moody, sentimental topics. They bore me."
    g "Instead, why don't we start thinking about possibilities?"
    show rs normcry at left:
        xalign 0.1
    r "Guilleme, please..."
    show gf haughty
    "She was still bent on changing his mind, but Guilleme could tell her resolve had all but fizzled out."
    show rs dep at left:
        xalign 0.1
    g "Oh, again? You still haven't given up?"
    show gf sneer
    g "I'll admit, you have spirit."
    g "It's admirable that you'd go to such lengths for me."
    g "I mean it when I say I'm honored."
    show rs sadcry at left:
        xalign 0.1
    show gf newnormal
    g "But you are so naive."
    show rs emocry at left:
        xalign 0.1
    g "Tragedy is everybody's friend, Rosa."
    g "If you stay with him too long, his smell will linger on your skin."
    show gf newsmile
    g "I don't care much for tragedies myself. I am more interested in opportunities."
    show gf newnormal
    g "And what we have right now is a dawning. A beginning."
    show rs dep at left:
        xalign 0.1
    show gf newnormal:
        xalign 0.40
    "Guilleme stepped closer to Rosa, touching her cheek with his palm."
    scene bg rgtension
    "Rosa was afraid, but she didn't make any attempts to run away this time."
    r "..."
    g "Aren't you glad you found me?"
    r "..."
    g "You're not alone anymore."
    g "You don't have to hide and cower, to subject yourself to the motions of this cruel life."
    g "Enough of this fascination for glorified sacrifice."
    show rs dep at left
    show gf newsmile at nnnearleft
    show bg cathroomagape

    r "..."
    g "Come with me."
    
    "Rosa stared up at him."
    show rs sadcry at left
    r "…What?"
    g "Come with me, Rosa."
    "He repeated his words with a cheerful smile."
    g "Let us leave this place and go far away! Start over."
    show rs sadcry at left
    g "Doesn't that sound grand?"
    r "..."
    g "It's about time you let go of the bad memories and face something new."
    g "Don't you think you owe yourself that much?"
    show rs pissedcry at left
    show gf newnormal at nnnearleft
    r "And what of the victims you will continue to take, Guilleme?"
    r "What about them?"
    show gf petulantnormal at nnnearleft
    show rs sadcry at left
    g "What {i}about{/i} them?"
    show gf think at nnnearleft
    g "I care little for strangers."
    show rs dep at left
    show gf newnormal at nnnearleft
    g "It is {i}you{/i} I want to make happy, Rosa."
    g "Please let me."
    show rs sadcry at left
    g "I need you, as much as you need me."
    show rs emocry at left
    "Rosa bit her lip."
    r "..."
    r "M-Mother...?"
    r "I need you right now."
    r "Please let me hear your voice."
    "She struggled with the pain in her heart."
    "She was freefalling."
    "{i}Mother...{/i}"
    "To hear her Mother's voice..."

    "She had always been the ground she stood on."
    "Both the pain on her bare feet, and a place to stand."
    "Whether she walked or chose to fly, that ground would be there when she landed."
    "Such was the role of family."
    if openlocket:
        "It didn't matter if she was her real mother or not."
        "What mattered was the love she gave her."
        "The memories were real."
        "She was..."
        
    # to get the secret end, the following things should be fulfilled:
    # do not open the locket
    # tell rosa that guilleme will never change
    # believe that rosa is in love with guilleme
        # tell her guilleme's presence bothers her
        # tell her guilleme will never look at her
        # accuse rosa of fancying him
        # tell her that she is in love with him
    # do not take the dagger, or the knife
    # tell rosa maybe killing might not be the answer
    # read all/more of guilleme's journal
    # say "goodbye" to rosa
    # unlock all the other endings
    
    if dagger is True:
        call realend2 from _call_realend2
    if knife is True:
        call realend2 from _call_realend2_1
    if rglove >= 4 and closelocket and nochange and byemom and nokillg and morejournal and persistent.Ending1Unlocked and persistent.Ending2Unlocked and persistent.Ending3Unlocked and persistent.Ending4Unlocked:
        call secretend from _call_secretend
    else:
        call realend2 from _call_realend2_2
        
    if persistent.end2WasReadBefore   is None:
        $persistent.end2WasReadBefore  = True
        $persistent.currentLinesRead +=1

    return

label realend2:
    if goodmom and not silentmom and not byemom:
        m "You've gone this far, darling."
        m "I trust in you."
        m "Whatever you decide, I will always be here."
        m "Like how I have always been..."
    show rs frownclose at left
    "Rosa's jaw clenched."
    show rs pissed at left
    "She tasted the caustic realisation in her mouth."
    show gf newnormal at nnnearleft
    g "…?"
    show gf newtalk at nnnearleft
    g "Rosa?"
    stop music 
    play sound "sfx/knifeslash.ogg"
    scene bg black
    with flashblood
    "And that was when he felt an icy pain shoot through his chest."
    "He looked down."
    scene bg cathroomagape
    "There was a knife sticking out of him."
    if dagger:
        "It was the dagger from his bedside."
        g "...Little thief."
        "He whispered as the wind got knocked out of him."
        $ achievement.grant("Little Thief")
        $achievement.Sync()
    else:
        "The knife Rosa had stolen from the kitchen."
        g "..."
    r "I'm sorry."
    "The blade clattered to the floor. Rosa's lip quivered."
    r "B-But I have to make this right."
    "Guilleme's body lost all strength."
    "He slumped on the floor, blood staining his shirt red."
    "He just laughed in amusement."
    g "Oh, you stupid girl."
    g "So, t-this is your response to my generous offer? Ugh, how trifling."
    g "I expected better from you."
    "Guilleme winced in pain."
    g "Been a while since I was s-stabbed..."
    r "..."
    "She knelt beside him. She didn't speak at once."
    r "That wound will not heal like the others, Guilleme."
    g "..."
    g "Oh?"
    r "I-I... must end it here."
    r "For Catherine. For Mother. For all your victims..."
    r "For you..."
    r "I have to do the right thing."
    "She said this aloud, but she only half-believed it."
    "{i}The right thing... hm?{/i}"
    "Was there such a thing?"
    "Rosa reveled in this confusion."
    "The least she could do was carry the burden of her choice for the rest of her life, instead of forgetting."
    "She had considered simply leaving him, unchanged and a prisoner of his own twisted ideals."
    "She still could."
    "If she reversed the spell now and allowed him to heal, then he would survive."
    "Young, powerful, and healthy, but unchanged and carrying the same shadow in his heart."
    "She had tried, hadn't she? Whatever he did next should be none of her concern."
    "There was a pinch in Rosa's chest."
    "...But to know that she doomed him to make the same mistakes forever."
    "To stop caring about him and degrade him into nothing but a failure."
    "It seemed crueler somehow."
    "It would make her... like him."
    "Guilleme sat up wordlessly, his back pressed on the wall."
    "This pain {i}was{/i} different."
    "The blood hadn't stopped leaking from his chest."
    "He coughed, and liquid flooded his lungs."
    "It was getting harder to breathe."
    "A part of him wanted to ask how she had found a way to kill him."
    "It seemed quite pointless now, a waste of precious breath."
    "He sat there bleeding, willing himself to anger."
    "He thought of threatening her, demanding her to do something."
    "But he didn't."
    "He was surprised to find something else in his heart."
    play music "sfx/bittersweet.ogg"
    "Gratitude, of all things."

    "Rosa held Guilleme's hand as the blood continued to pour out of his wound."
    "Dimly, Guilleme reflected that she really did have spirit."
    "The courage to do what he could not."
    "He used the last of his strength to lift up his hand and wipe away her tears."
    g "Don't cry."
    g "...I'm fine with this."
    "His hand lingered on her face for a while."
    "He searched his heart for anger, for bitterness for this girl."
    "But there was none."
    "How curious it was to feel the steel in his heart and yet no hate for its wielder."
    "How curious it was to know that this was all an act of love."
    "{i}Rosa...{/i}"
    "{i}You are an anomaly.{/i}"
    "{i}You confuse me.{/i}"
    "Maybe if he had listened, would he have--?"
    "Maybe she was right."
    "He could change."
    "..."
    "But it was too late for him, wasn't it?"
    "It had been too late for him decades ago."
    "Long after he had degraded life, including his own, as pointless and petty."
    "That was the only regret."
    g "I wish..."
    g "I wish we had met sooner."
    "He took a deep breath."
    scene bg cathroomagape
    "The pain in his chest throbbed with every breath."
    "Still, it was only a distant buzzing in his mind."
    "The pain was simply white noise."
    "Rosa held his hand tighter."
    r "I-I'm sorry... I--"
    g "Apologizing again?"
    g "I thought I've... m-made myself clear with that."
    "Guilleme coughed and tasted metal in his mouth."
    "He chuckled and wiped it away."
    if persistent.Ending4Unlocked:
        g "Honestly, this could have been much worse."
        r "..."
    g "Rosa..."
    g "I was never strong enough to endure this life..."
    g "...But it looks like you are..."
    g "...That's good..."
    if openlocket and goodmom:
        r "My mother..."
        r "She tried her best..."
        $ achievement.grant("Mother")
        $achievement.Sync()
    else:
        pass
    r "..."
    g "You'll stay with me for a while, won't you?"
    g "P-Please?"
    r "Yes, Guilleme."
    g "..."
    g "T-Take my journal with you. It might help."
    g "I would still... wish for you to start anew."
    g "Board the ship... the papers..."
    g "Take the money in my office."
    g "...Use it to build a new life."
    r "..."
    "Guilleme coughed out red flecks of blood."
    "He swallowed, and his throat felt like it was on fire."
    "He had a lot more to say, a lot more to tell her."
    "He tried to speak as clearly as he could, despite the bulge climbing up his windpipe."
    g "Avoid... small towns. They don't take to strangers kindly."
    g "You'll stick out... like a sore thumb."
    g "Always present yourself... as nobility... or a person of influence."
    g "Give people another reason to think you're desirable."
    g "Otherwise, they will... fear and hate you... confused... by their own urges."
    "His breathing was getting erratic."
    g "Also, remember to--"
    if openlocket and not rgloves and family:
        r "Shh... Please rest now."
        "Rosa smiled sadly."
        r "You are still so generous... even if you are like this."
        "Guilleme smiled."
        g "...Like what?"
        "He chuckled at the memory."
        g "...Generosity is the only saving grace of the dying."
        g "...Or a parent, I suspect."
        r "..."
        r "I'm happy I found you, Father."
        g "Likewise..."
        g "The last... few years I have spent with you were my happiest."
        "Guilleme stared at her, his vision clear now."
        scene bg gdiespeace
        "He pushed a strand of hair away from her face and touched her cheek fondly."
        g "...My daughter."
        "Rosa's eye filled with tears at this."
        g "You are... beautiful."
        g "A-At the end, I... I got to meet you."
        g "To know that... something good... came from my existence..."
        g "It is not... so bad."
        r "..."
        g "...I love you, Rosa."    
        r "As do I, Father."
        r "Please..."
        r "Be free."
        $ achievement.grant("Guilleme's Redemption")
        $achievement.Sync()
        if persistent.locket2WasReadBefore   is None:
            $persistent.locket2WasReadBefore  = True
            $persistent.currentLinesRead +=1
    elif closelocket and rglove >=4:
        scene bg gdiespeace2kiss
        "Rosa leaned over and kissed Guilleme's lips to stop him from speaking."
        "They were cold now, but they were still sweet, laced with the salty taste of blood."
        "She remembered the taste of them in her mouth from the first time she had met him."
        "The way he had filled her with a sweetness so strong that her mouth had watered."
        "The taste had never left her throughout the years that had passed."
        "Perhaps it never would."
        "How could something so corrupt be so sweet?"
        "Rosa touched his face and fresh tears fell from her eye."
        "How could something so beautiful be so ugly?"
        $ achievement.grant("Love is Bittersweet")
        $achievement.Sync()
        scene bg cathroomagape
        r "I-I love you... Guilleme."
        "He was her poison."
        "She would remember him only with regret."
        "Love and pain mixed like water and salt."
        "But she {i}would{/i} remember."
        $ achievement.grant("Poison and Cure")
        $achievement.Sync()
        r "I love you."
        "She whispered."
        "But Guilleme didn't seem to hear."
        "His eyes were closed now and every breath seemed shorter than the last."
        if persistent.poisonWasReadBefore   is None:
            $persistent.poisonWasReadBefore  = True
            $persistent.currentLinesRead +=1
    else:
        r "Shh... Please rest now."
        "Rosa smiled sadly." 
        "Guilleme's eyes fell. Every breath seemed shorter than the last."
    "Death gave the heart a final gift of bliss."
    "He savored this."
    g "...Thank you, Rosa."
    scene bg cathroomagape
    "The two of them crouched in a corner, cherishing each other's warmth for as long as it lasted."
    "The candle's wick expired and the room was plunged into darkness."
    scene bg black with Dissolve (1.0, alpha=True)
    if silentmom or byemom:
        "Rosa got up, looking down at him one last time."
        "Sunlight slipped past the window."
        "It touched her face."
        "Rosa left the room to welcome the dawn."
        $renpy.pause(delay=None)
        scene bg end02 with slowdissolve
        with Pause(2)
        scene bg black with fade
        $renpy.pause(delay=None)
        call endcredits from _call_endcredits_1
    else:  
        m "Darling?"
        r "Yes, Mother."
        m "I know it was hard..."
        "Mother didn't sound spiteful or on edge this time."
        "She was simply… serene."
        "Rosa got up, looking down at him one last time."
        if persistent.Ending1Unlocked:
            r "..."
        else:
            r "Mother, I cannot get rid of the feeling that I should've done things differently."
            r "Should I have done more? S-Should I have sacrificed more?"
            $ achievement.grant("Play It Again")
            $achievement.Sync()
            "Tears once again stung her eye."
            r "I wish I could turn back time and change something--anything..."
            r "I feel so powerless."
            m "..."
            m "I understand."
            m "Loss will always hurt, my darling. It makes us vulnerable."
            m "But you must know that changing things does not guarantee happiness."
            m "Do you understand?"
            r "..."
            r "Y-Yes..."
            m "Oh, my darling, I wish I was there to hold you."
            r "..."
        m "What are you going to do now?"
        r "I don't know."
        m "Whichever direction you head, I will be with you."
        r "I know you will, Mother."
        r "Your presence saved me, as it always does."
        r "You reminded me that nothing lost should be thrown away."
        r "Catherine, Guilleme, and you will always be with me."
        r "I am not alone."
        m "I am proud of you, my beautiful daughter."
        "The first rays of light slipped past the window and touched her face."
        "Rosa left the room to welcome the dawn."
        $ achievement.grant("Closure")
        $achievement.Sync()
        if persistent.closureWasReadBefore   is None:
            $persistent.closureWasReadBefore  = True
            $persistent.currentLinesRead +=1
        $renpy.pause(delay=None)
        scene bg end02 with slowdissolve
        with Pause(2)
        scene bg black with fade
        $renpy.pause(delay=None)
    if persistent.realend2WasReadBefore   is None:
        $persistent.realend2WasReadBefore  = True
        $persistent.currentLinesRead +=1
    call endcredits from _call_endcredits_2
    call summary0 from _call_summary_1
    $ renpy.full_restart()    
    return

label secretend:
    $save_name = "secretend: bliss"
    if(persistent.BonusEndingUnlocked == False):
      $persistent.BonusEndingUnlocked = True
      $ persistent.EndingUnlocked +=1
      
    play music "sfx/confront.ogg"
    scene bg cathroomagape
    show rs emocry at left
    show gf newsmile
    m "..."
    r "..."
    "Rosa wiped her tears."
    "He was right."
    "She was alone now. Mother had left her."
    "Whether for good or ill, she was not sure."
    "This was her choice, wasn't it?"
    "But the thought of being alone out in the world scared her."
    "Where would she go? How would she even begin?"
    "She felt vulnerable."
    show rs hmp at left
    "But here was somebody who would stay with her."
    "{i}A new beginning.{/i}"
    "It was almost too good to be true."
    "She stared at Guilleme's outstretched hand."    
    "Almost at once, she understood what he meant."
    show rs dep at left
    m "{i}Love{/i}"
    m "{i}Have you heard the rumor about Love?{/i}"
    m "{i}It is never pure.{/i}"
    $ achievement.grant("Never Pure")
    $achievement.Sync()
    "He only wanted her for his benefit."
    "That was fine."
    "It was mutual."
    "Who was to say this wasn't love, no matter how twisted?"
    show rs emocry at left
    "Two broken people existing together, edges cutting skin as they drew close."
    "It sounded pathetic. Desperate. Foolish."
    "But was it really?"
    "The world was less lonelier, less empty."
    show rs dep at left
    "That, alone, was worth {i}everything{/i}."
    nvl clear
    o "The sea of despair engulfs unwanted, jettison hearts."
    o "We struggle with the weight of our existence tied to our ankles."
    nvl clear
    o "Without anything to cling on to,"
    o "We drown in its cold embrace, pondering our own solitude."
    nvl clear
    m "{i}Love is the mask of the beast called Need.{/i}"

    scene bg cathroomagape
    "Rosa sighed in submission. She took his hand."

    #show gf think at nearleft
    #show rs emocry at left
    "As she reached out her hand, Guilleme pulled her into a hug, and Rosa let 
    his warmth fill the gaps of her lonely, confused heart."
    #show rs aww at left
    "He terrified her."
    "He was hideous."
    "She shone a light at his true face and saw the monster hiding behind the shadows."
    #show rs emocry at left
    "Yet in her fear, she was also helplessly captivated."
    "His arms were comforting. His heartbeat soothed her own."
    "It thumped in time with hers."
    "..."
    "She could still change him, right?"
    #show gf newnormal at nearleft
    "She stared into his eyes. He would be lost without her."
    "Wasn't she the only one who could help him? Then she had to try more than once..."
    "She had to try for more than a lifetime..."
    #show rs hmp at left
    "A tiny voice screamed its protests."
    "{i}For how long?{/i}"
    "{i}To what ends?{/i}"
    "{i}What is my bargain?{/i}"
    "But then, Guilleme kissed her."
    scene bg rgkiss
    "The doubts stopped, muffled by the bloodrush in her ears as their lips touched."
    "Instantly, a sweet taste exploded in her mouth."
    "{i}Oh.{/i}"
    "So long had she craved that taste."
    "It was... toxic."
    "The sweetest poison."
    "Rosa pulled away in fear."
    scene bg cathroomagape
    show gf newnormal at nearleft
    show rs emocry at left
    r "Guilleme..."
    r "I-I... I don't want to feed."
    r "I will not feed from other people."
    show rs dep at left
    g "Then don't."
    "Guilleme pushed a strand of hair away from her face."
    g "I won't force you."
    show gf newsmile at nearleft
    g "But to survive, you have to feed from me."
    r "..."
    g "One step at a time."
    show rs flinch at left
    r "W-What if I hurt you?"

    show gf sneer at nearleft
    "He grinned."
    show rs aww at left
    g "I have a lot of love to give."
    show rs dep at left
    "Rosa averted her face."
    r "..."
    show gf newnormal at nearleft
    show rs hmp at left
    r "P-Please stop hurting people, Guilleme."
    "It was not an argument anymore, but a request."
    "She expected to be turned down again, but Guilleme appeared to ponder it."
    show gf think at nearleft
    "Rosa looked up at him."
    g "..."
    show gf sneer at nearleft
    g "You managed to make a more appealing offer after all."
    show gf haughty at nearleft
    r "..."
    g "..."
    show gf newsmile at nearleft
    g "Alright."
    g "I shall do it."
    show rs aww at left
    r "R-Really...?"
    show gf haughty at nearleft
    g "As long as you are with me, I will do whatever you wish."
    show gf newnormal at nearleft
    g "I need time to get used to it, however."
    show rs hmp at left
    show gf newnormal at nearleft
    r "..."
    g "Don't worry..."
    show rs huh at left
    g "Now that I have you, I won't have to feed to the point that a person is sucked dry."
    show rs dep at left
    g "I will take only what I need."
    show gf newsmile at nearleft
    g "Does that console you?"
    show rs emocry at left
    "Rosa closed her eye and sighed."
    r "..."
    show rs aww at left
    show gf newnormal at nearleft
    r "Do you promise?"
    r "Do you promise not to take more than what is needed?"
    show gf newsmile at nearleft
    g "Of course!"

    g "Anything for you, Rosa."
    show rs hmp at left
    "He grinned at her easily."
    "A nervous pang of doubt churned in her stomach once again."
    show rs dep at left
    "Rosa hesitated."
    show gf newnormal at nearleft
    "Guilleme held her face in his hands and looked deep into her eye."
    show rs aww at left
    g "Rosa."
    g "You don't know how much I appreciate you."
    show gf think at nearleft
    g "I have been alone for so long..."
    g "But now, I know where I belong."
    show gf bliss at nearleft with Dissolve (1.0, alpha=True)
    g "{cps=20}I belong with you.{/cps}"
    show rs blushdep at left
    "He said this earnestly."
    "His face emanated genuine bliss, like that of an innocent child's."
    show gf bliss2 at nearleft
    "His thumb caressed her cheek."
    "To know that she was the cause of this happiness struck her with ecstasy."
    "The doubts were swept under the covers, along with voiceless things and secrets."
    "At that moment, she knew she would believe anything he said."
    show rs blushhuh at left

    r "...As do I..."
    show rs blushdep at left
    r "..."
    r "Guilleme..."
    show rs blushhuh at left
    r "....I..."
    show gf bliss3 at nearleft
    r "I have always..."
    play sound "sfx/fall.ogg"
    scene bg black
    with Shake((0.2, 1.0, 0.2, 1.0), 1.0, dist=2)
    scene bg rgdeepkiss with slowdissolve

    "Guilleme pushed her against the wall into a deeper kiss, their bodies moving closer."

    "His hand slid down her waist."
    "It made the hairs on her neck stand up."  
    "It was rougher this time, the taste a little stronger."
    "His tongue was vital in her mouth."
    "She felt simultaneously weak and alive."
    "An ebb and a flow."
    "A push and a pull."
    "A waltz."
    "They were feeding on each other."
    "The activity was draining but maddeningly euphoric."
    scene bg cathroomagape
    "Guilleme pulled back, both their breaths laboured and heavy."
    "Blood dashed to his face. His ears were hot. His lower lip trembled."
    "He clutched his chest in surprise to find his heart racing."
    "What a curious sensation."
    "He had never wanted anything so desperately in his life."
    "Guilleme caressed Rosa's face in utter devotion."
    g "You..."
    g "You are... exquisite."
    "His warm breath was on her ear, low and barely audible."
    g "...Thank you..."
    g "...For existing."
    scene bg black
    "The candle lost the last of its light, plunging the room into darkness."
    "Two figures in the shadows entwined and melted into each other like wax." 
    $ achievement.grant("Dark Fairytale")
    $achievement.Sync()
    $renpy.pause(delay=None)
    scene bg end05 with slowdissolve
    with Pause(2)
    scene bg black with fade
    $renpy.pause(delay=None)
    m "You have unlocked the secret end."
    m "Congratulations!"
    $ achievement.grant("Dedication!")
    $achievement.Sync()
    scene bg black with fade
    $renpy.pause(delay=None)
    if persistent.secretWasReadBefore   is None:
        $persistent.secretWasReadBefore  = True
        $persistent.currentLinesRead +=1
    call summary0 from _call_summary0_1
    $ renpy.full_restart()    
    
    return
