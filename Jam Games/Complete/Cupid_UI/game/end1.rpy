label end1:
    stop music fadeout 2.0
    $save_name = "end1: temperance"
    if(persistent.Ending1Unlocked == False):
      $persistent.Ending1Unlocked = True
      $ persistent.EndingUnlocked +=1
      
    scene bg black  
    "Guilleme woke up with the fading dream still in his memory."
    show bg cathroomagape with slowdissolve
    "He was not in his room, but in Catherine's."
    play music "sfx/confront.ogg" 
    #"How did he get here? Did he sleepwalk?"
    show gf angry at right  
    "This did not surprise him."
    "Whoever cast the spell did not do so on a whim."
    "A pure, white candle flickered on the table, and its flame looked as though it was ready to go out."
    u "I couldn't save you."
    u "I tried."
    show rs think at left with Dissolve(2.0, alpha = True)
    "Rosa stepped out of the shadows."

    show gf annoyedtalk at right  
    g "You--!"
    "Guilleme's anger mixed with a tinge of relief."
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
    g "I do not take kindly to people who dabble with my brain, Rosa."
    g "Especially when they have such audacity to do so when I am most vulnerable."
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
    "Rosa had grown stronger through the years, but she was still fragile, wasn't she?"
    show gf mad  
    "...Maybe to him."
    "Why was that?"
    
    show gf maddown  
    "But Rosa's eye did not flinch or look away, even at his outburst."
    "There was no fear or fragility in her eye at all."
    "She held her gaze steady until it was Guilleme who looked away."
    
    g "Why--"
    show gf pissed  
    g "Why are you doing this?"
    g " Fine... you loved Catherine. I understand you want her memory to live on but--"
    show rs norm at left  
    r "No. It's not because of that."
    show rs think at left  
    r "Catherine's memory is already present in me."
    r "I already have her."
    show rs hmp at left  
    r "But you don't."
    show gf maddown  
    r "I wanted to... give her to you--"
    show rs pissed at left  
    show gf furious  
    r "--so you don't have to resort to feeding."
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
    r "Mother guided me. She protected me."
    r "She taught me how to control it, even in her own twisted way."
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
    "Rosa wiped tears from her face."    
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
    show gf sneer with Dissolve (1.5, alpha=True)
    "With no reason to stand for ceremony, Guilleme's face changed easily."
    "Rosa's jaw clenched."

    "She was talking to a stranger now."
    "His face lost the virtue that once belonged to a blameless man."
    "It was replaced by a curious, cheeky grin, a perpetual look of childlike mischief."
    "He was different, and yet somehow, Rosa felt like she had known him for a lifetime."
    "He had always been there, hadn't he?"
    "Or rather, it had always been him."
    
    g "Why?"
    g "Because it is fun."
    g "And the taste is {i}worlds{/i} better."
    show rs pissed at left  
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
    "The hard look dawned on her face once again."
    show rs angry at left  
    show gf newtalk  
    r "I will never join you."
    r "You use people for your gain."
    show gf newgrr  
    g "And so?!"  
    show rs pissed at left  
    "Guilleme's voice couldn't keep from rising."  
    g "What of it?!"
    g "Isn't it the rule of human existence?"
    show gf sneer
    g "It's all a game."
    g "And it's a game I play to win!"

    show gf petulantnormal
    show rs angry at left
    r "So people's lives are a game to you?"
    show gf petulantsmile
    show rs pissed at left  
    "Guilleme shrugged."
    g "Of course they are."
    show gf petulanttalk
    g "The alternative is much worse."
    show gf petulantnormal
    r "..."
    g "Humans don't play fair."
    show gf silentpain
    g "They use and abuse and they throw away on whim."
    g "They destroy for no apparent reason except that they want to."
    show gf furioussneer  
    g "I just get ahead."
    show gf furious          
    g "I can give them love, I can give them affection."
    show gf petulant
    g "But I will {i}never{/i} give them pity."
    
    "Rosa's eye narrowed at Guilleme."
    
    show gf furious  
    r "Didn't you once tell me not to think of myself as a victim, Guilleme?"
    r "So why is that all you ever think of yourself as?"
    $ achievement.grant("Victim Mentality")
    $achievement.Sync()
    show gf furiousshock  :
        xalign 0.47
    
    "Guilleme's lips quivered. He tried to speak but no words came out."
    "Rosa stared at him, her eye seemed to search for his answer beyond his silence."
    "{i}Naive!{/i} He shouted in his head. {i}You do not know what you're talking about!{/i}"
    "But his throat dried up."
    show gf maddown
    "Suddenly, he felt inadequate in her gaze."
    
    r "Is that the reason you tell yourself  it's alright to throw people away?"
    r "But you don't believe that, do you?"
   
    r "Mother was tainted. But she still loved me and protected me the best she could."
    r "Even in her cruelty, she gave herself wholly."
    r "Papa Francois was tainted, but he looked at me like a daughter and never touched me."
    show rs dep at left  
    r "Catherine..."
    show rs angrycry at left  
    "Rosa's tears made her voice quiver and break."
    r "She was tainted."
    r "Caught between me and you, I wonder what that was like?"
    r "And yet, for all her faults, she still gave herself to you whole-heartedly."
    r "She loved you, Guilleme."
    r "When you took her love, you left a lifetime of memories."
    r "You left her hope."
    r "The lack of love isn't what broke her, but this hope."
    r "She never stopped loving you."
    r "Love is not lust, attraction or an exchange of favors."
    $ renpy.pause (delay=None)
    r "It is a choice."
    show gf furiousdown  
    g "..."
    r "You know it as much as I do."
    r "Don't you?"
    g "..."
    show rs pissed at left  
    "Rosa wiped her tears."
    r "I am tainted by you."
    r "I could hate you and curse you like any of your victims."
    show gf furiousshock  
    r "...But I choose not to."
    stop music fadeout 2.0
    show rs frownclose at left  
    r "Because of Catherine..."
    r "Because of Mother..."
    r "...I learned that love can be a blessing."
    r "Something we can give rather than take."
    show rs pissed at left      
    r "Love isn't your curse, Guilleme."
    r "This curse you wallow in was brought on by yourself."
    r "Your own choices."
    show gf furiousshock  :
        xalign 0.50
    "Guilleme took a hasty step back."
    show gf maddownshock      
    g "..."

    "Catherine's memory once again flooded his mind."
    scene bg cath13 with zoomin
    scene bg cathkidmemory with zoomin
    scene bg cath14 with zoomin
    scene bg cath03 with slowdissolve
    "{i}The girl who gave him everything.{/i}"
    "In his greed, he forgot to ask why."
    "Why {i}did{/i} she give everything?"
    "He might say that it was only fair."
    "...But that had always been a lie, hadn't it?"
    "{i}The girl who always chose to be loving, instead of just loved.{/i}"
    "He had always..."
    "...kept a few pieces to himself..."
    "...This concept of totality utterly foreign and terrifying to someone like him."
    "{i}The girl who was whole.{/i}"
    scene bg cath03 with None
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    play music "sfx/intro.ogg"
    "Guilleme clutched his chest."
    scene bg cath03  
    g "...But it's..."
    g "{cps=10}{i}...painful...{/i}{/cps}"
    g "I don't want to..."
    "He said this petulantly, like a child."
    g "I don't want to..."
    scene bg gclutch with Dissolve(0.4, alpha = True)
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
    g "{i}I don't want to!{/i}"
    r "It {i}is{/i} painful, isn't it?"
    r "But that is the real taste of love."
  
    r "Have you ever asked yourself why you stayed that long with her?"
    scene bg gclutch2 with Dissolve(1.0, alpha = True)  
    r "Why you have delayed your feeding for so long?"
    r "Why you cared for her until she died, even when you had no use for her anymore?"
    r "Maybe you had started to love her beyond your needs, Guilleme."
    
    scene bg white with Dissolve(0.4, alpha = True)
    scene bg cath03  
    c "{i}You can't fake sacrifice, mon chou{/i}."
    scene bg white with Dissolve(0.4, alpha = True)
    scene bg cath06  
    c "{i}You are a good man.{/i}"
    scene bg white with Dissolve(0.4, alpha = True)
    scene bg cath07  
    c "{i}Maybe you liked keeping this face?{/i}"
    scene bg tear    
    "A different taste spread on Guilleme's tongue."
    "It was salty with just the hint of sweetness."
    "Pure. Like seawater."

    "Guilleme realized he tasted his own sadness."
    "But it faded quickly from his numb mouth."
    scene bg white with Dissolve(4.0, alpha = True)
    "He was so accustomed to pleasure that he scrambled to get her face back."
    scene bg cath03 with Dissolve(4.0, alpha = True)
    "It took all of his efforts to remember, to form the memories like a jigsaw puzzle in his mind."
    "The stars."
    "Ribbons."
    "The smell of burnt sugar."
    "Magpies."
    "{i}\"You're like a prince in the fairy tales, Gilly!\"{/i}"
    "Her hair."
    "The wind."
    "A touch of her fingers on his cheek."
    "Every memory squeezed his heart which he thought was long dead."
    "It was the harder way."
    scene bg white with Dissolve(4.0, alpha = True)
    "But a glimmer of understanding appeared."
    "It was not enough to change him, but there was hope."
    "The sickening taste he had been devouring was not love."
    "Only desire."
    "He had put it in his mouth over and over again, convincing himself it was all there was."
    "Perhaps to wash away the taste of what he really wanted."
    "Was it... too late for him?"
    "The cravings controlled him. He could feel them slither under his tongue."
    "He was sick of them, but also reliant on them."
    "...They were most loyal."
    "Guilleme looked up at Rosa."
    show rs hmp with Dissolve(2.0, alpha = True)
    "He was never strong, he knew that now."
    "Rosa was."
    "{i}You...{/i}"
    "{i}You are the one I seek.{/i}"
    "{i}The one to save me from this wretchedness.{/i}"
    
    "{i}And didn't you say you are tainted by me?{/i}"
    "{i}Do you love me, Rosa?{/i}"
    "{i}Please say you do.{/i}"
    "{i}Please walk beside me.{/i}"
    show rs hmpbig with Dissolve(2.0, alpha = True)
    "Guilleme stepped closer to her."
    g "I don't... understand much."
    g "...But I will try."
    g "Stay with me..."
    g "You don't know how grateful I am to know I am not alone in enduring this."
    show rs pissedbig  
    "He reached out his hand to touch her, almost like a newborn reaching for the warmth of a mother."
    show rs angrybig  
    "But Rosa shoved away his hand."
    "There was a bitterness in her voice that stabbed through his heart."
    r "Why are you surprised to know I exist?"
    r "Am I that easy to forget?"

    "Guilleme frowned."
    g "What are you talking about?"
    
    r "You don't remember me at all, do you?"
    r "You locked my memory away."
    r "You were content to forget!"
    show rs angrybig  
    r "What you did to my Mother was already unforgivable."
    r "But to erase her existence from your mind!"
    show rs madbig     
    r "{i}I could hate you, Father!{/i}"
    
    "Guilleme's chest tightened."
    show rs pissedbig  
    g "W-What?"
    
    "{i}But... that's impossible...{/i}"
    "{i}I was never able to...{/i}"
    
    "Rosa took out the locket that he had given her."
    "The lock was open now, and a picture of a woman was inside."
    "Guilleme couldn't remember her, but the woman's face stirred something buried deeply in his mind."
    "{i}Fire.{/i}"
    "{i}Moonlight.{/i}"
    "He searched his memory for such a woman but his mind came up blank."
    "His head ached."
    
    g "I--"
    g "I don't remember."
    
    show rs angrybig  
    r "Of course you don't."
    r "Isn't that how insignificant we were to you?"
    g "..."
    show rs angrycrybig   
    r "She... she loved you."
    r "But to you, she was just another faceless woman, easy to throw away and forget."
    r "Even when you left, she kept {i}me{/i}."
    r "{i}Me...{/i} who was a constant reminder of her pain."
    g "..."
    r "Tell me now how meaningless this love is?" 
    r "Why did you leave her, Father?"
    show rs furious   
    r "{i}Is it hard to keep something you broke?{/i}"
    show rs angrycrybig      
    "Guilleme's hand shook."
    "He was barren... Wasn't he?"
    "...And yet here she was. His child."
    "He didn't know how this could have happened, but he clung to the belief desperately."
    "He welcomed the regret. He savored this pain."
    "How could he have forgotten the only child he sired?"
    
    show rs pissedcrybig  
    g "Rosa... I---"
    show rs furiouscrybig  
    r "My name is not Rosa!"
    show rs angrycrybig  
    r "I lost my name a long time ago."
    
    r "Much like you have lost me in your memory."
    
    "Tears fell from her eye."
    show rs furiouscrybig  
    r "How could you drop me so easily?"
    r "Am I not good enough?"
    r "You didn't even look for me, never even thought about me."
    "She was sobbing now."
    "A mere a child forcing herself to understand the mysterious ways of her parents."
    show rs hmpcrybig      
    "Guilleme's arms moved stiffly on their own."
    "He held her as she cried, stroking her head to soothe her."
    $ achievement.grant("Father and Child")
    $achievement.Sync()
    g "I-I'm sorry."
    
    "He still couldn't remember this woman he loved."
    "Unlike his other victims, he must have stayed."
    "Hoping, probably, that things would improve."
    "Hoping that the hundreds of shallow lovers he had had before were somehow payment for one true love."
    "If he stayed long enough, if he paced his feeding, if he---"

    "He might not remember her, but he already knew what happened."
    "Greed is the core of desire."
    "{i}I am not a monster.{/i}"
    "{i}But why am I always hungry?{/i}"
    
    g "I..."
    g "I'm sorry..."
    g "But... Y-You're here now, Rosa."
    g "Let me... make it up to you."
    
    "He held Rosa tightly in his arms."
    g "Maybe..."
    g "This is the love I need."
    g "The love of family."
    g "Rosa."
    g "You are my family."
    g "If we stay together, I don't need to use other people, you see?"
    g "I will try my best to learn from you."
    g "I-I will... {w=0.2}try to sate my addiction."
    $ achievement.grant("Love is my Drug")
    $achievement.Sync()
    "This was the first time Guilleme used that word."
    "He winced at the grossness of it. His mouth salivated with disgust at its weight."
    "But he swallowed it like a hard pill."
    "He could change."
    "He could!"
    "For her."
    "Everything would be alright."
    "Rosa was here now. Rosa was--"

    show rs pissedcrybig  
    r "I don't think you understand, Guilleme."
    r "We cannot stay together."
    
    g "--Why not?!"
    "Guilleme spat with the anger of a man with shattered hopes."
    "Deep inside he knew why, but his loneliness pushed it away."
    "{i}\"Maybe this time it wouldn't turn out like the others\"{/i}, he tried to convince himself."
    "She was his daughter."
    "It might be different! It would be!"
    "He wished to change it with the force of will alone."

    show rs madcrybig
    r "Our curse will taint even this kind of love."
    r "I can feel it surge in me even now."
    r "It is... slower than normal, but more potent and dangerous."
    r "...And then what?"
    r "Time will pass, and you will degrade me into another lover's memory."
    r "You will be doomed to repeat the same thing."
    r "You know this too, don't you?"
    
    g "..."
    g "No."
    "He held on to her stubbornly."
    g "No, please."
    g "I'm sure we'll find a way!"
    g "I'll do whatever it takes!"
    show rs angrycry  
    "Rosa broke away from his embrace."
    r "You can't make me stay like an object to satisfy you, Father."
    $ achievement.grant("Sound Advice")
    $achievement.Sync()
    show rs sadcry  

    r "I... I am doing this for you."
    r "If you do not want Catherine's memory, then I will leave you mine."
    r "My dearest Guilleme"
    r "I love you."
    r "I love you how a child innocently loves their parent."
    r "Without any conditions, or any hope of return."
    r "You were given the chance to raise me, and I was able to make memories of you I will treasure."
    r "I want you to be happy. I want you to be free."
    show rs normcry  
    r "You don't know how much it hurts me to do this..."
    r "But you cannot depend on me for change."
    r "You must do it on your own."
    show rs emocry  
    r "Please remember me like this."
    r "I hope you will change, knowing that it can be done."
    g "Rosa..."
    g "Please--"
    g "P-Please stay."
    g "I beg you."
    show rs superemocry  
    r "Goodbye, Father."

    r "May we meet again in better times."
    "Rosa turned her back on him, and Guilleme fell to his knees in despair."
    "He stretched out his hand to reach for her, but she seemed too far away."
    show rs final  
    g "{i}...Don't leave me!{/i}"
    scene bg black with Dissolve (2.0, alpha=True)
    "A final exhale of breath. The candle fizzled out."
    $renpy.pause(delay=None)
    $ achievement.grant("New Beginnings")
    $achievement.Sync()
    "The first few rays of dawn touched his face."
    "He opened his eyes."
    $ achievement.grant("Agape's Blessing")
    $achievement.Sync()
    $renpy.pause(delay=None)
    scene bg end01 with slowdissolve
    with Pause(2)
    scene bg black with fade
    $renpy.pause(delay=None)
    if persistent.end1WasReadBefore   is None:
        $persistent.end1WasReadBefore  = True
        $persistent.currentLinesRead +=1
    call endcredits from _call_endcredits

return
    
    
    
    
    
    
    
    
