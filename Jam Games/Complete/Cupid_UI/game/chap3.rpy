label chap3:
#CG of candle
    stop music fadeout 2.0
    $save_name = "chap3: portraits, candlelit"
    $persistent.Chapter3Unlocked = True
    
    scene bg chap03 with slowdissolve
    with Pause(2)
    scene bg black with fade
    scene bg pianoroom 
  
    play music "sfx/cathsadsong.ogg"
    "Rosa entered the room with a tray of pastries and a pot of tea."
    "She finished her duties early, and was allowed a bit of free time."
    "She thought of accompanying Catherine for today's piano lesson."
    show rc huh at right
    r "Cath, do you want some tea?"
    show rc sad at right
    "The girl didn't look her way."
    "She continued to churn out the bitter, melancholic sound from her piano."
    show rc dep at right
    "Rosa sighed."
    show rc hmp at right
    "She placed the food on the table."
    show rc normal at nnearright 
    "She sat on the stool beside the piano, twiddling her thumbs while her friend continued to stew in her foul mood."
    show rc huh at nnearright
    r "Is that a new composition?"
    show rc hmp at nnearright
    c "..."
    show rc happy at nnearright 
    r "...It sounds nice..."
    show rc hmp at nnearright
    c "..."
    r "You've been making a new pieces every day, it seems."
    r "It's a shame they're all so sad."
    "Catherine didn't reply to that, but when she spoke again her words were bitter."
    play sound "sfx/pianoslam01.ogg"
    stop music
    play music "sfx/birds.ogg"
    show rc huh at nnearright
    show ct angry
    c "I saw them again, those degenerate louts."
    c "No shame at all."
    show ct annoyed 
    show rc hmp at nnearright
    r "Cath..."
    show ct angry 
    c "At least have the decency to close the door!"
    show ct annoyed 
    r "..."
    c "Sometimes, I think they {i}want{/i} to get caught."
    show ct seethe 
    c "When I walked in on them this morning, eating each others' faces, they had this look on them."
    c "Like they were daring me to say something."
    show ct angry at center 
    c "What? Do they want my applause?"
    show ct angrysmile 
    c "Very nice technique, Sire."
    c "I very much like the way you swap your spit with my sister! Great tongue action!"
    show ct seethe
    c "{i}Très merveilleux!{/i}"

    r "..."
    show ct angry
    c "And he even has the gall to speak to me?!"
    c "{i}'Be a dear and put them on the table, Catherine'{/i}, he even said."
    show ct seethe 
    c "Argh!"
    show ct angry at center 
    c "He wanted me to get annoyed, I just know it."
    if persistent.adult:
        c "Well, I sure as fuck am!"
    else:
        c "Well, I sure as hell am!"

    show ct annoyed 
    "Catherine turned to the tea and pastries, stuffing the buttered bread into her mouth."
    show rc huh at nnearright
    r "Easy there."
    c "These damn things..."
    show ct seethe 
    c "These damn {i}delicious{/i} things!"
    "She said the last part angrily, as if she blamed her troubles on the foods' relish."
    show rc happy at nnearright
    "Rosa giggled in spite of herself."
    show ct angrysmile 
    "Catherine wiped her mouth in mock anger."
    show ct pout 
    c "What are you laughing at, wench?"
    r "It's comical to watch you eat when you're angry, Cath."
    r "You're like the giant monsters that attack defenseless towns in horror books."
    show ct angrysmile 
    c "Oh, yes?"
    show ct pout 
    "Catherine made sad tiny squeals as she picked up another piece of bread."
    c "No, no! Please spare us!"
    "She adjusted her voice and boomed out a roar."
    show ct angry 
    c "{i}The Catherinian monster of the deep doesn't show mercy to anyone!{/i}"
    show ct pout 
    "She dropped it in her mouth and chewed, savagely."
    show ct happy 
    c "Yum! Annihilation is delicious with tea."
    "The two girls giggled."
    show ct sadsmile 
    "Catherine's rare smile turned into a rueful laugh."
    show rc hmp at nnearright
    show ct sad 
    "Soon, Rosa felt her mood turning somber again."
    show rc sad at nnearright
    r "What happened, anyway?"
    show ct pout 
    c "..."
    c "Aren't you annoyed by it too?"
    
    c "Sister has changed ever since she started staying at the château."
    show ct angry 
    c "Now it's all Guilleme this, Guilleme that."
    show ct pout 
    c "As if she wasn't already married. Ugh."
    c "She doesn't even care that people are talking behind her back."
    if persistent.adult:
        show ct angry 
        c "They're calling her a two-timing slut now!"
    c "I'm tired of running around picking fights with gossipers."
    show ct sad 
    c "..."
    c "She hasn't even visited home for a long time."
    c "Father misses her a lot."
    c "He always asks about her."
    show ct seethe 
    c "Father had worked so hard all these years to give us a comfortable life."
    c "Now he is sick, and all she cares about is that dastardly Marquis."
    show ct pout     
    "Rosa shrugged."
    show rc annoyed at nnearright
    r "I am a little bit annoyed."
    r "But I guess I've gotten used to it."
    show rc huh at nnearright
    r "Their lives are their own, Cath. No matter how messy."
    show rc dep at nnearright
    "She didn't dare divulge more than that to Catherine."
    show rc hmp at nnearright
    "But, it was partially true."
    show ct annoyed 
    c "I like Guilleme. He's a good friend."
    c "But I love my sister."
    show ct angry 
    c "If they want to stay together, then why not fix this and have at it?"
    show ct seethe 
    show rc huh at nnearright
    c "But what irritates me to my damn snatch is the way they are with each other!"
    show rc sad at nnearright
    "Catherine recently found the use of expletives endearing in her speech."
    "Rosa hoped it was a phase."
    show ct angry 
    if persistent.adult:
        c "They're fucking {i}miserable{/i}! Any halfwit can see that!"
    else:
        c "They are {i}miserable{/i}! Any halfwit can see that!"
    show rc hmp at nnearright
    r "Yes."
    show ct sad 
    c "I've told Émilie time and again to smarten up."
    c "She's hurting a lot of people, including herself."
    show ct pout 
    c "But as if she would listen to her sixteen-year-old brat of a sister, hm?"
    show rc sad at nnearright
    c "Even Guilleme is depressed, I can tell!"
    show ct sadsmile 
    show rc smile at nnearright
    c "Remember when he used to come here in the piano room to have tea?"
    show ct happy 
    c "Or when we would hold spontaneous picnics in the afternoon?"
    c "We used to run around chasing rabbits in the garden!"
    show rc huh at nnearright
    r "{i}You{/i} ran around."
    show rc happy at nnearright
    r "We just watched you get dirty, actually."
    show ct angrysmile 
    c "That is very true, you chumps!"
    show ct sadsmile 
    show rc normal at nnearright
    c "Back then, it used to be fun visiting the château."
    show ct pout 
    c "Nowadays, we barely even see him."
    c "He just stays in his bureau all day, brooding."
    c "Is it something adults subject themselves to, like a torture ritual?"
    c "I really don't understand why two people who are clearly unhappy keep at it."
    show rc hmp at nnearright
    
    "Rosa did understand."
    show rc dep at nnearright
    "At least some part of her did."
    "She couldn't exactly explain how pain and love worked."
    "All she knew was that it had something to do with an absurd, obsessive amount of hope."
    show rc think at nnearright
    "She felt Mother tugging at her mind."
    "She loved Mother so much."
    
    "Living with the Perrides gave her ample comparison to her former life."
    
    "She had finally accepted that Mother was... cruel."
    show rc dep at nnearright
    "And yet, Mother still gave her love and kept her from wanting."
    "Was that crazy?"   
    "Perhaps it was the only love she needed."
    "Perhaps it was what she deserved..."
    
    "Rosa shook the thoughts off her mind and just shrugged."
    show rc smile at nnearright
    r "I know you are worried about your sister, Cath."
    r "But they will figure it out." 
    show ct huh 
    c "..."
    r "Humans have the ability to learn from their mistakes."
    show rc think at nnearright
    r "As their loved ones, all we can really do is be patient with them and remind them we're still here."
    c "..."
    show ct happy 
    show rc smile at nnearright
    if persistent.adult:
        c "Look at you, all profound and shit! You read any smart books lately?"
    else:
         c "Look at you, all profound and such! You read any smart books lately?"
    show ct smile 
    show rc smile at nnearright
    r "Just the riveting account of the ugly duckling and baa baa black sheep."
    show ct happy 
    c "Ah, the classics."
    show ct pout 
    c "I don't know how you put up with books, though! I get bored easily."
    show ct normal 
    r "In order to write, I have to learn how to read first."
    r "I want to write."
    show ct huh 
    c "Why would you want to do a dastardly thing like writing?"
    show rc huh at nnearright
    r "Why would you want to hit some crazy strings until your fingers bleed?"
    show rc happy at nnearright
    show ct happy     
    "The two friends laughed again."
    show rc think at nnearright
    show ct normal 
    r "I want to remember things."
    r "I want to write them down."
    show ct smile 
    show rc smile at nnearright
    r "But most of all, I want to feel the way you do when you play the piano, Cath."
    show ct huh 
    c "Oh?"
    show rc thinksmile at nnearright
    r "The way you look when you play, you are passion and bliss in musical form."
    show rc smile at nnearright
    r "It feels like love, like magic!"
    show ct smile 
    show rc happy at nnearright
    r "You inspire me to do something fulfilling and grand!"
    show ct happy 
    c "Well, I'm sure you will!"
    show rc smile at nnearright
    show ct huh  
    c "Hey, why not write a play one day?"
    show rc huh at nnearright
    r "Oh!"
    show ct happy 
    c "Let's do it! You write an amazing play--"    
    c "And I shall provide the music!"
    c "We'll travel around the country and perform!"
    c "We'll make lots and lots of money and gain lots of followers."
    c "We shall be known as:"
    show ct angrysmile 
    show rc huh at nnearright
    c "The Perride Parade Caravan of Wonders."
    show rc annoyed at nnearright
    r "Perride... {i}Parade?{/i}"
    show rc hmp at nnearright
    r "Are you sure?"
    show ct happy 
    c "Puns are the best! Trust me!"
    show rc huh at nnearright
    r "That sounds darn batty, Cathy."
    show rc happy at nnearright
    show ct angrysmile 
    c "Ugh!"
    c "From this day forward, nobody is allowed to call me {i}\"Cathy\"{/i} ever again!"
    play sound "sfx/knock.ogg"
    show ct happy 
    "The sound of a knock interrupted their giggles."
    show ct pout  
    show rc huh at nnearright
    a "Catherine, it's me."
    a "I need to discuss something important with you."
    "Catherine pouted at the sound of her sister's voice." 
    hide ct pout 
    show rc sad at nnearright
    play music "sfx/fastsong.ogg"
    "She turned back to her piano and pounded a sarcastically happy tune."
    "Rosa stood up to open the door."

    play sound "sfx/softdoorclose.ogg"
    show rc huh at nearleft

    a "Hello, Rosa."
    show asi base at center
    r "Madame."
    "She had seen little of the older Perride sister recently and it astounded her how old she had began to look."
    "Her once radiant face looked tired and harrowed, almost crone-like. Huge bags hung underneath her eyes."
    "And yet she still looked quite dignified, full of pride and pomp."
    "There was extra rouge on her skin, and her demeanor was elegant." 
    "It was as if pride was her only source of nourishment these days."
    
    show rc normal at nearleft
    a "Do you mind giving Catherine and me a moment of privacy?"
    "Rosa gave a small bow."
    r "Of course not, Madame."
   
    "Rosa gathered her nursery books and squeezed Catherine's shoulder before stepping out of the room."
    hide rc normal
    hide asi base
    $renpy.music.set_volume(0.2, delay=2.0)
    play sound "sfx/softdoorclose.ogg"
    show bg black 
    stop music fadeout 1.0
    
    scene bg library 
    show rc normal at nearleft 
    play music "sfx/library.ogg" fadein 3.0
    "Rosa entered the quiet room of the library."
    "She was about to approach the table when she noticed Guilleme, already occupying a seat."
    show rc huh at nearleft 
    "He was writing something in a book, somewhat immersed in the activity."
    show rc blush at nearleft 
    "Rosa stopped dead in her tracks."
    #########################
    call m04 from _call_m04
    
    "Unfortunately, Guilleme lifted his head and saw her by the door."
    show gc bitchface at right 
    show rc sad at nearleft 
    g "Oh. Hello, Rosa."
    show rc depblush at left 
    "Rosa took a step back. Maybe it was best to walk away as if this were a mistake."
    show rc blush at nearleft 
    "But wouldn't that be rude? He had already seen her, after all."
    show rc depblush at left 
    "But she had never been alone with him. It was just too awkward."
    show rc annoyedblush at nearleft 
    "Well, why not just go in? It was going to be fine! They had conversed normally before."
    show rc depblush at left 
    "But that was because she would hide behind the more assertive Catherine."
    show rc shyblush at left     
    r "{i}Now I look like an idiot!{/i}"
    show gc smirk at right 
    "Guilleme watched her pace in front of the door in amusement."
    show rc annoyedblush at left 
    "Rosa decided to go in. She had already embarrassed herself enough, anyway."
    "There was little left to lose."
    "Besides, there was nowhere else to go in this big house."
    "She had gotten lost in its hallways too many times, much to the annoyance of the {i}Maître d'{/i}."
    "The library was her favourite place."
    "If she stayed quietly in one corner, Rosa was sure they wouldn't bother each other."
    "She took a seat at the farthest corner of the table and opened her book."
    r "..."
    show rc shyblush at left     
    r "{i}Oh no, he's actually standing up and walking over?{/i}"
    show rc annoyedblush at left     
    r "{i}No, no, you horrible man, just sit over there, while I sit over here!{/i}"
    show gc bitchface 
    "But Guilleme was already beside her, peeking at what she was reading."
    show rc shyblush at left 
    "A cold sweat spread on her scalp."
    show gc talk 
    g "Rosa, that book--"
    "Rosa began to chatter nervously."
    show rc embrblush at left     
    r "I know it's a children's book, Sire! I-I-I'm teaching myself to read!"
    show gc bitchface 
    r "I know most commoners don't really bother, but I want to learn!"
    r "So please don't laugh or mock me!"
    "Guilleme pointed to the book."

    show gc boredspeak 
    g "It is upside down."
    show rc shockblush at left 
    "Rosa stared at it."
    show gc smirk 
    "The ducks in the picture had their feet up in the air."
    "Rosa squirmed, feeling the heat on her cheeks."
    show rc embrblush at left  
    r "I-I'm sorry!"
    show gc unamused 
    "Guilleme's face lost its cheer."
    g "What do you need my forgiveness for?"
    show rc huh at left 
    "Rosa looked up at Guilleme."
    "His eyes lacked the gentle glint they usually had."
    "It was such a subtle change, something felt rather than observed."

    show rc dep at left 
    "She thought he would reprimand her further."
    show gc bitchface 
    "Instead, he sat down beside her, drumming his fingers on his cheek as he watched her wordlessly."
    show rc sad at left 
    r "..."
    g "Well?"
    r "...?"
    g "Weren't you going to read?"
    show rc hmp at left 
    r "I--"

    "What was wrong with him today? He didn't seem like himself."
    "Had he eaten something bad?"
    "The aura he exuded was not his usual, friendly warmth."
    show rc normal at left 
    "Yet, it wasn't particularly wicked."
    "The look on his face just read '{i}slightly and eternally miffed'{/i}'."
    "Rosa turned the book upright and read the words out loud."
    show rc huh at left 
    r "O--once yuh---Ah... uhm--"
    show gc boredspeak 
    g "That is the 'u' with the short sound. It is pronounced like this."
    "Guilleme made the sound, his face still in his lazy stare."
    show gc bitchface 
    "Rosa nodded and continued."
    "Her nerves were frazzled, but she was actually at ease in his presence."
    "She felt like a child being taught by a parent."
    show rc think at left 
    "The parent was strict, but still caring."
    "And the child was jumpy, but eager to learn and please."
    show rc smile at left 
    "Most of all, he would not hurt her for her mistakes."
    "Rosa was almost sure."
    show rc huh at left 
    r "There lib-ed."
    show gc boredspeak 
    g "Lived. The past tense of live."
    show gc bitchface 
    r "..."
    show rc normal at left 
    r "Why do we change it?"
    g "It is a rule of grammar that--"
    show rc huh at left 
    r "Grammar?"
    show gc annoyed 
    "Guilleme narrowed his eyes at her."
    show gc bitchface 
    g "Do you even know your alphabet?"
    "Rosa shook her head."
    g "You should start there."
    show rc normal at left 
    hide gc bitchface 
    "Guilleme rose from his chair and disappeared amongst the shelves."
    show rc huh at left 
    "He left behind an old thick book covered in green felt. This was what he had been writing in earlier."
    "It looked tattered and worn."
    "The pages laid thick on its side that the book didn't close properly."
    "Rosa reached out to peek at the cover when--"
    g "You are not to touch that."
    show rc annoyedblush at left 
    #show rc shockblush at left 
    "Rosa's whole body froze at the sound of Guilleme's warning."

    show gc unamused at right 
    "Guilleme's stare followed her as she whispered numerous apologies under her breath."
    show rc embrblush at left  
    r "{i}I'm sorry. I'm sorry. I'm sorry.{/i}"
    show gc think at right 
    "Guilleme just rolled his eyes."
    show gc unamused at right 
    g "Must you always ask forgiveness for everything?"
    g "It is quite irritating."
    #g "Has anyone told you it is quite grating?"

    show rc huh at left 
    r "Ah..."
    r "I-I'm sorr--"
    play sound "sfx/tablehit.ogg"
    scene bg library with None
    show gc angry at nnearleft
    show rc sad at left
                          

    "His hand struck the table in front of Rosa."
    "In the quiet library, the sound rang uncomfortably in her ear."
    show rc shockblush at left 
    "When she looked up, Guilleme's face was looming severely above hers."
    "He moved closer to her, his eyes fixed on her intensely."
    "Rosa's mouth hung open."

    "She struggled to say something, but her wits were like the burning ends of a matchstick."
    "Before she could compose herself, she felt Guilleme's hand lift her chin."
    show rc depblush at left 
    "Rosa's heart thumped loudly inside her chest."
    r "{i}Please, don't... Not you, too!{/i}"
    "She felt his breath on her face, and her heart sank into despair."
    show rc shyblush at left 
    if cynicalmom:
        "Mother's voice resounded in her head."
        m "In the end they are all the same."
        m "He is like everyone else!"
    if badpeople:
        m "{i}There are no more good people left in this world, child!{/i}"
    "She shut her eye and prepared herself for the worst, like she always did when--"
    "Then, she felt her face being turned from side to side."
    show rc shockblush at left 
    "She opened her eye to see Guilleme studying her face like a textbook."
    show gc bitchface at nnearleft 

    g "You are a fairly attractive girl."
    g "Yet you carry yourself as if it is a blight."
    "He lifted the hair that hid her damaged eye."
    "Rosa clenched her teeth."
    show rc blush at left 
    g "Is it because you were hurt before?"
    "He said it so matter-of-factly, like he was stating that the sky was blue."
    "Rosa recoiled from his touch."
    show rc hmp at left 
    r "N-No..."
    show rc dep at left 
    r "I did that to myself."
    g "I wasn't talking about your eye."
    show gc bitchface 
    "He placed a book on the table."
    "It was a thin pamphlet filled with letters."
    "There were lines on the book that instructed the user to trace letters with their quill."
    "Rosa wanted to focus on it, but she could feel the truth in the Marquis' words stinging her."
    g "It was the way you went limp when I touched you."
    show gc bitchface 
    g "Next time, I advise you to fight back."
    show gc angry 
    g "If you don't want to be touched, then you don't have to be."
    g "Do you understand this?"
    show rc hmp at left 
    r "...But..."
    show rc dep at left 
    r "...I am weak."
    show gc unamused 
    g "Says who?"
    show rc sad at left 
    "His eyes were humourless."
    show gc think 
    g "The world cares not for people who think of themselves as victims, Rosa."
    show rc dep at left  
    show gc annoyed 
    g "If you need power, then be powerful."
    g "Push back. Fight back. Struggle."
    show gc unamused 
    show rc huh at left 
    g "If you end up crushing things along the way, so be it."

    show rc dep at left 
    "Rosa flinched under the weight of his stare."

    "She realised that the polite and courteous Guilleme was but a facet."
    show rc normal at left 
    "It was still him, but it was nothing but an oil portrait, an artwork of his devising."
    "Synthetic, aloof, and irrelevant. It couldn't capture his essence in a few human strokes."
    "Suddenly, Rosa realised he {i}was{/i} powerful."
    show rc hmp at left 
    "{i}Who are you?{/i} She caught herself before saying it aloud.{i} You are not Guilleme.{/i}"
    "...And yet."
    "He spoke as if he knew what it was like to hurt and to fear."
    g "If you don't start acting like you own yourself, then people will not hesitate to take everything."
    show rc dep at left 
    "He laid out the rest of the books he had brought out."
    "One was an activity book for children."
    show rc huh at left 
    "It had a picture of a child holding an apple with an arrow stuck in it."
    "Another was a book of limericks."
    "The other two were thicker books that intimidated her."
    "She would come to know them as {i}'Hamlet'{/i} and {i}'Paradise Lost{/i}'."
    "But the one that caught her eye was an ornately designed book."
    "It had a beautiful red jacket, with delicate gold trimmings lining the corners."
    "{i}The Gods and Goddesses of Roman Mythology{/i}"
    "This would be her favourite book, her treasure, and she knew it like love at first sight."
    show gc talk  
    g "These books are yours."
    g "Take them with you."
    g "Read the thin ones first, and then gradually build your vocabulary with the thicker ones."
    g "The big books may look intimidating, but give it time."
    g "Soon, your reading scope will be limitless."
    "Rosa ran her hands over the skin of the red book."
    "She opened the cover gingerly, as if unwrapping a present."
    r "T-Thank you..."
    show gc bitchface 
    g "No thanks needed."
    show rc sad at left 
    r "..."
    show rc huh at left
    r "You are still so generous... even when you are like this.."
    g "Like what?"
    show rc sad at left 
    r "That."
    g "What?"
    show rc annoyed at left 
    r "Uhm, s-somewhat grumpy?"
    "Guilleme didn’t reply, leaving an awkward silence lingering between them."
    show gc smirk 
    "Then, he gave a giant laugh that made Rosa jump out of her skin."
    show rc huh at left 
    g "I do look like a grump, don't I?"
    show rc sad at left 
    r "A-Are you okay?"
    r "Is it because of... Émilie?"
    show gc unamused 
    "Guilleme's eyes drifted away."
    g "No."
    show gc seriouslookdown
    g "I have always been like this."
    show rc huh at left 
    r "T-That's not true."
    r "You're nice and friendly, usually..."
    r "Especially with Catherine and the townsfolk..."
    show gc bitchface
    g "That's nothing."
    g "It's easy for me to adapt to people. Especially, to the ones I like."
    "Rosa furrowed her brow."
    show rc annoyed at left     
    r "Adapt...?"
    r "{i}What a strange word to use...{/i}"
    "Guilleme looked at Rosa as if he had just become aware of her presence."
    show gc huh 
    g "Makes me wonder why I am so stern with you."
    show gc seriouslookdown
    g "..."
    show rc normal at left
    g "You're right... I'm not usually like this."

    g "I'm sorry."
    "Rosa shook her head."

    show gc bitchface
    show rc smile at left 
    r "I... somehow prefer this side of you."
    show gc talk 
    g "..."
    "Guilleme tilted his head to the side with amusement."
    show gc norm 
    "He brought out the green book that Rosa noticed earlier."
    show rc huh at left 
    g "This is called a journal."
    g "When you learn to write, start one."
    r "What is it?"
    g "Something you can use to remember yourself when you've forgotten."
    r "Does it work?"
    show gc bitchface 
    g "It used to. Nowadays, not anymore."
    show rc sad at left
    show gc seriouslookdown
    r "...Oh."

    g "The act itself is the only thing I remember."
    g "..."
    show gc huh 
    g "Now."
    show gc smirk 
    g "Let's start with your vowels--"
    stop music
    scene bg black with None
    play sound "sfx/scream.ogg"
    "A scream pierced the halls of the Château."
    "It was Catherine."
    "Guilleme sprinted to the door with Rosa not far behind."



    play sound "sfx/pianoslam02.ogg"
    $renpy.pause(delay=None)
    play music "sfx/doom.ogg" fadein 3.0
    "Back in the piano room, Catherine took a shaky step towards her sister."

    scene bg pianoroom with None
    show ct shock at nearright with None
    "She wasn't moving at all."
    if persistent.adult:
        "Blood dotted the ivory keys."
    
    c "I didn't--"
    c "It was an accident--"
    c "I--"
    c "Émilie?"
    

    "It was a nasty fall."
    
    c "É-Émilie?"
    
    "Catherine saw the way her sister's head snapped back as it collided with the sharp corner of the piano."
    "She watched it all like a series of photographs in her head."
    "She had to check on her... right?"
    "She had to touch her and shake her awake."
    "Make sure she was okay..."
    "But her feet refused to move."
    show ct shock at right 
    "Instead, she retreated into a corner."
    "She didn't even notice her legs were moving until her forehead touched the wall."
    "She didn't want to turn around."
    if persistent.adult:
        scene bg ameliadead 
    else:
        scene bg ameliadeadsafe 
    "Her sister laid on the floor."
    "Her eyes open, unblinking."
    nvl clear
    o "{i}It was an accident! It was nothing but an accident!{/i}"
    m "...Was it?"
    nvl clear
    o "{i}She pushed first!{/i}"
    nvl clear
    o "{i}She got really scary.{/i}"
    o "{i}She strangled me.{/i}"
    m "What? That's absurd!"
    m "Are you sure?"
    m "Would she do that?"
    nvl clear
    o "{i}I--I don't know..{/i}"
    nvl clear
    o "{i}I think she did.{/i}"
    
    "Catherine touched her throat."
    "It felt fine."
    scene bg black 
    nvl clear
    o "{i}That Perride girl. Émilie, is it?{/i}"
    nvl clear
    o "{i}She really believes just because the Marquis took her in, that he's interested in her?{/i}"
    nvl clear
    o "{i}Well, she's obsessed with the Master.{/i}"
    o "{i}The apple doesn't fall far from the tree.{/i}"
    nvl clear
    o "{i}Wasn't her mother a bit...{/i}"
    nvl clear
    o "{i}You know...{/i}"
    nvl clear
    o "{i}Not right in the head?{/i}"
    m "It probably runs in the family."
    
    "Émilie had looked mad."
    "Her eyes had burned with malice for her as she had closed her fingers around Catherine's neck."
    
    "But she couldn't remember if that had really happened."
    "Sister was always kind to her."
    "She would never ever hurt her, even when they got into fights."
    show bg cathshock     
    m "{i}Sister loved her.{/i}"

    nvl clear
    o "..."
    nvl clear
    o "Am I turning mad?"
    nvl clear
    o "I have the blood of a madwoman."
    nvl clear
    o "Am I going to end up like her?" 
    nvl clear
    o "I--"
    
    nvl clear
    o "I only told her the truth."
    o "Guilleme doesn't care for her."
    o "And she doesn't even care for him that much either."
    nvl clear
    o "It was all just... chaff, their relationship."
    nvl clear
    o "No sense making everyone else miserable, too."
    
    nvl clear
    if persistent.adult:
        o "But she called me jealous and a cunt."
        o "She has never called me a cunt."
    else:
        o "But she called me jealous and a bitch."
        o "She has never called me a bitch."
    nvl clear
    o "I was spoiled, she said..."
    o "Sister had to start work so young, but I got to laze around and play piano all day."
    nvl clear
    o "She said they have decided to send me away."
    nvl clear
    o "My lessons sent home."
    o "The piano replaced."
    nvl clear
    o "It was for my own good, she said."
    o "I don't have to travel here all the time."
    nvl clear
    o "I can concentrate on my other endeavors."
    o "I can make new friends."
    nvl clear
    o "But I know she just doesn't want me near the château or Guilleme."
    o "She hates it when I catch her with him."
    nvl clear
    o "Perhaps this morning was the last straw?"
    nvl clear
    o "She hates it, but she also smirks at me when I see them."
    o "Like she basks in it."
    nvl clear
    o "..."
    nvl clear
    o "I think I might hate her."
    nvl clear
    
    "Catherine's thoughts ran through her head like a storm."
    "They poured out of her aimlessly."
    
    nvl clear
    o "I wonder if the piano is broken."
    nvl clear
    o "Am I going to pay for it?"
    nvl clear
    o "What will become of us without Sister's wages?"
    nvl clear
    o "What of Father's medicine?"
    nvl clear
    o "What of my dreams?"
    nvl clear
    o "Sister can't be dead."

    scene bg black 
    m "{i}Sister can't be dead.{/i}"
    
    "Catherine brought her fingers to her lips and nibbled on her thumb."
    "She didn't notice this. Her mind was preoccupied."
    "She cowered in her corner of the wall, biting her fingers."
    "It was a tiny comfort in a rapidly collapsing world."
    
    scene bg pianoroom
    play sound "sfx/churchdoor.ogg"
    "Guilleme opened the door and found Émilie lying on the floor."
    "An ugly gash broke the skin of her forehead."
    show gc angry 
    "Facing the wall was Catherine, shivering like a leaf and viciously devouring one of her fingernails."
    "He approached her cautiously."
    
    show gc unamused 
    g "Catherine?"
    
    show rc sadsmall at nearleft 
    "Rosa let out a gasp at the grisly scene."
    "Émilie's lifeless eyes stared up at nothing while Catherine pressed herself into a corner."
    "What had happened after she had left?!"
    g "Rosa, will you call for help, please?"
    show rc depsmall at nearleft 
    g "See that someone checks on Émilie."
    hide rc depsmall 
    "Rosa did as she was told, her eyes on the broken, shaking Catherine."
    "She wished she could comfort her friend herself."
    show gc unamusedbig     
    "Guilleme took a small step towards Catherine."
    "He called out her name slowly, coaxingly."
    "Catherine turned her head, her thumb still on her lower lip."
    if persistent.adult:
        "The flesh was torn, and a smudge of scarlet painted her teeth."
    c "I-It was an accident, I-I swear--"
    g "Of course it was, Catherine, of course it was."
    show gc thinkbig 
    c "She pushed me first!"   
    c "She wanted me sent away!"
    c "She wanted me gone!"
    show gc unamusedbig    
    g "You can tell me about it later."
    g "Let me take you away from this room."
    c "W-What have I done?"
    
    "Catherine fell to her knees and wept. Large sobs sucked the air out of her lungs."
    "She felt like drowning, trying to keep herself afloat in between sobs."
    "Every exhale was a squeezing pain in her chest."
    "Guilleme's arms wrapped around her."

    c "What have I done? What have I done?!"
    show gc talkbig 
    g "You didn't do anything, dear."
    show gc unamusedbig    
    g "This is not your fault."
    "There was a bitter bulge building up in her throat, and she felt that no amount of crying could push it back down."
    show gc angrybig 
    c "What am I going to do--"
    show gc thinkbig 
    c "F-Father is--"
    c "Sister--"
    c "I... I'm so scared--"
    show gc unamusedbig    
    "Guilleme's arms wound tighter around her and she clutched onto his arms in this vast sea of fear."
    g "You don't have to be."
    g "I will always be by your side."    
    g "Catherine?"
    g "I will take care of you and your father, alright?"
    g "You don't have to worry about your future."
    "Her tears soaked his shirt through, but the squeezing in her chest felt less painful."
    c "W-Why... Why do you do this? Why do you care so much for me?"
    show gc angrybig 
    "Guilleme's brows furrowed, as if confused that she even asked."
    show gc annoyedbig 
    g "I just do."
    show gc unamusedbig 
    "It was a boldly stated fact, as if painfully obvious, as if Catherine was a fool for not knowing it."
    "It made Catherine's heart expand in her ribs."
    "When she looked back, she would recall this as the moment she fell in love with him."
    "The look in his eyes was reassuring and strong."
    "She wasn't alone. She was going to be alright."
    show gc talkbig 
    g "Let's get you away from here."
    show gc unamused 
    "He supported her arms and stood her up, careful to block the view of her sister from her eyes."
    "He led her to the door."
    scene bg black 
    stop music fadeout 5.0
    "Catherine hated how fast her relief came."
    "She was still drenched in sorrow at her sister's death."
    "Her father would not take well to the news, especially in his health."
    "But she was alright, and she hated it."
    "Rosa was with her."
    "She didn't have to leave her piano."
    "Her dreams."
    "{i}Him.{/i}"
    "Nothing had to change."
    "And most importantly, she hated the voice that came whispering in her head over and over again."
    m "{i}Thank goodness she's dead. Thank goodness.{/i}"

    show bg black 
    stop music fadeout 2.0
    $renpy.pause(delay=None)

    play sound "sfx/matchflare.ogg"
    scene bg candle1 with slowdissolve
    nvl clear
    o "The first candle is lit. This candle is Storge."
    nvl clear
    o "The love for familiars."
    o "The cleanest love."
    "Rosa stared at the blue candle glowing in her hand as she chanted her spell."
    nvl clear
    o "Trust is the veil that conceals and deceives."
    o "Trick his eyes and his heart with the warmth from this candle's flame."
    nvl clear
    o "A bond of blood like kin will be forged."
    o "Weave this trust so his tongue will yield to what is sought."
    scene bg black 
    stop sound fadeout 4.0
    $ renpy.pause(delay=None)

    #back to reality.
    scene bg cemetery with slowdissolve

    play music "sfx/nature.ogg" fadein 3.0
    "Rosa stood by Catherine's tomb, nursing memories of her."
    show rf dep 
    "The soft wind lightly blew her hair."
    "It reminded her of Catherine and her playful ways."
    "Tears sprouted from her eye."
    "{i}Even the wind...{/i}"
    ################################# 
    call m05 from _call_m05
    
    g "Rosa."
    show gn serioussmall at right 
    "Guilleme’s soft voice came from behind. Rosa glanced at him in acknowledgement."

    r "..."
    show gn serious at right 
    "He stood quietly beside her for a few moments but ventured to speak."
    g "Have you thought about my offer?"
    g "My house is always open for you, remember that."
    r "..."
    show rf sad 
    r "I'm sorry for my outburst back then."
    show rf dep 
    show gn talk at right 
    g "It's nothing."
    show gn dep at right 
    "The wind played around their feet, and Rosa pictured Catherine as part of the breeze, playful and free."
    "She was free from the pain and confusion that had plagued her in her last days."
    "They stood beside each other in solemn reverence."

    "Finally, Rosa broke the silence."

    r "She was my family."
    show gn serious at right 
    r "I was in pain before she came along. I didn't know any better."
    r "She gave me hope."
    r "She was... bright, like a flame."
    r "When I close my eyes, I can still see the imprint of her light in the darkness."
    r "I can feel her warmth."
    show gn dep at right     
    g "A star."
    "They didn't speak again for some time."
    "Guilleme cleared his throat."
    g "I--"
    show gn think at right 
    g "I was an orphan too, much like you."
    g "I know what it feels like to lose too much."
    g "I wandered for a long time before I found anything to live for."
    show rf sad 
    r "Were you alone?"
    show gn angrylookdown at right 
    g "Sometimes... {w=0.3}Always."
    show rf dep 
    "Rosa nodded."
    show rf sad 
    r "Did you have family?"
    show gn bitchface at right 
    "Guilleme shifted uncomfortably."
    show gn dep at right 
    g "No, they ah... I never knew them."
    g "Much of my memory of it is blurred."
    g "I was taken in by kind people once before but--"
    show gn think at right 

    "Guilleme sighed, and Rosa observed a certain disquiet in him."
    show gn angrylookdown at right 
    g "...I didn't belong."
    show gn think at right 
    show rf dep
    r "..."
    show rf sad 
    r "But you have no difficulty mingling with people."
    show gn angrylookdown at right 
    g "..."
    g "That's more necessity than preference."
    show gn angrylookdown at right 
    g "...But either way, it can be quite tiresome after a while..." 
    show gn think at right 
    show rf dep 
    #g "Things... don't last."
    show gn angrylookdown at right 
    g "..."
    show gn sad at right 
    g "I don't know why I'm telling you this."
    g "I am making the mood worse."
    g "I'm sorry."
    show rf normal 
    r "I don't mind."
    "Guilleme had never opened up to her about his past before, and it worried Rosa how little she actually knew about him."
    show gn serious at right 
    g "Anyway, would you like to go around town?"
    show rf think 
    g "I'd very much like to take you some place more cheery."
    show rf smile 
    r "How about our favorite spot?"
    show gn smile at right 
    "Guilleme smiled with understanding."
    
    
    scene bg sunset 
    play music "sfx/friends.ogg"
    "The pair travelled up a hill at the edge of town."
    "There, the view overlooked the quaint village."

    "The sunset painted everything in the pink glow of dusk, of endings."
    show rf think 
    show gn serious at right 
    r "It is always so beautiful here."
    "They used to spend time in this grassy knoll, the three of them."
    "It was their own little hideaway."
    "Memories of the past crept up on every corner, the ghost of laughter echoed in the wind."
    "Rosa touched the trunk of the small tree they had carved their names on."
    "So many fond memories."
    show rf normal 
    g "Rosa."

    g "I want you to have this."
    show rf huh 
    "Guilleme took Rosa's hand and placed an item in her palm."
    "It was a simple silver locket."
    "She looked up at him questioningly."
    show gn think at right 
    g "I have had that for as long as I can remember."
    g "One of my remembrances of the past."
    show rf sad 
    show gn serious at right 
    r "I can't take this."
    g "You must."
    g "You need it more than I do."
    r "But--"
    show rf dep 
    g "It's old, and the locket doesn't even open anymore."
    show gn think at right 
    g "I don't know why I've held on to it for so long."
    g "I can't even remember how I came to have it."
    show gn smile at right 
    g "But it comforts me."
    g "Maybe it will have the same effect for you."
    r "..."
    show rf sad 
    r "This is your treasure, Guilleme. It feels wrong to take it."
    show gn dep at right 
    show rf sad 
    g "On the contrary, I believe you must have it."
    show gn sad at right 
    g "I am not good with expressing sorrow, or even giving comfort."
    g "But I want to do something... at least."
    g "For you."
    "He closed his hand over hers, affirming the gift."
    show gn smile at right 
    g "It's yours."
    g "Please take it."
    show rf dep 
    show gn serious at right 
    g "You are wrong if you think I am letting you stay in the manor simply for Catherine's sake."
    g "I do it of my own accord."
    show rf sad 
    g "Let me do this for you, Rosa. We have been friends for quite a while."
    g "If you need to leave, at least stay until you feel ready to go."
    show rf think 
    r "..."
    show rf normal 
    r "Alright."
    r "But I will continue working in your household for my lodging."
    g "You don't have to do that. I can raise your status to a lady."
    g "You can read and write now. And very well."
    g "I'm sure you will be more comfortable in a higher position."
    show rf think 
    r "I have no need for a higher position."
    show rf smile 
    show gn huh at right 
    r "Just free access to your library."
    show gn smile at right 
    g "..."
    g "You have come a long way from the shy girl back then, Rosa."
    g "Watching you grow has been a pleasure."
    g "Yes, the library is yours."
    "They were quiet for a while, only conversing through looks, smiles, and tiny sighs."
    show rf huh 
    "Rosa realised that she had been holding on to Guilleme's hand all that time."
    show rf blush 
    "She broke off from his hold, rather embarrassed."
    show rf think 
    r "We should head back."
    show gn huh at right  
    show rf normal 
    g "You're right. It's getting quite late."
    show gn normal at right 
    hide gn normal 
    "Guilleme walked over to the carriage to get it ready."
    m "Excellent, child."
    m "Being a maid in his household will give you free access to the rooms."
    m "He trusts you completely."
    m "It seems that the candle worked."
    r "I guess so."
    "Rosa looked at the silver necklace in her hand."

    
    ################################## 
    call m06 from _call_m06
    
    m "The spell will start its effect in stages, gradually uncovering his true face."
    m "Fondness first, then Trust."
    m "Familiarity."
    show rf dep 
    "Rosa sighed."
    "But was the spell necessary at all?"
    "Didn't she already have that with Guilleme?"
    "Rosa bit her lip, remembering the warmth of his hand."
    "They had known each other for a long time."
    "It was rather comforting to have someone to mourn with."
    show rf hmp 
    "However, Rosa did find it strange that Guilleme rarely even mentioned Catherine anymore."
    "It was as if he was shedding her off like skin."
    if persistent.adult:
        "Again, the taste of blood in her throat resurfaced."
    else:
        "Again, the pain in her throat resurfaced."
    "The memory of the needles made her stomach lurch."
    "Since her friend had died, the Marquis had begun spending all his hours locked in his office."
    "He barely showed himself socially, rarely even attended meals."
    "..."
    "But they were casting a powerful spell, something that might harm Guilleme."
    show rf dep 
    "What if he was, after all, innocent?"
    "She had years of good memories with him."
    "What was she even expecting to find out?"
    "...Exactly how could she live with the guilt of two dead friends?"
    "Rosa sighed."
    "She cared for him."
    "Despite all the suspicions, she knew that much."
    "But Mother was adamant."
    m "Three candles for three loves."
    m "A fitting curse for a man who frolicks in love's domain."
    m "Storge. The love for familiars."
    m "Philia. The love for friends."
    m "And Eros. The love for lust."
    m "Open his heart with Storge."
    m "Unmask him with Philia."
    m "Strike him down with Eros."
    "Yet Rosa kept a fourth candle."
    "One she had named Agape."
    "{i}Unconditional love.{/i}"
    "She didn't know whether she would ever use it."
    "Mother, of course, would object."
    "But just in case Eros successfully struck Guilleme, she wished to light Agape."
    "{i}At least, give him peace b-before--{/i}"
    "Rosa walked towards Guilleme, a pang of anxiousness biting at her."
    m "Rise, my daughter."
    show rf normal 
    m "The work lays ahead."
    m "To bring him down, we must find his weakness. Then, we attack."
    if revenge:
        m "Revenge will be sweet, my dear daughter."
    if justice:
        m "His due punishment will be swift, my dear daughter."
    scene bg black 
    m "Do it for Mother."
    $renpy.pause(delay=None)    
    if persistent.chap3WasReadBefore   is None:
        $persistent.chap3WasReadBefore  = True
        $persistent.currentLinesRead +=1
    
    call chap4 from _call_chap4

    
    
return    

