label chap6:
    $save_name = "chap6: \"good intentions\""
    $persistent.Chapter6Unlocked = True
    scene bg chap06 with slowdissolve
    with Pause(2)
    scene bg black with fade
    stop music fadeout 2.0
    scene bg librarydark
    nvl clear
    play music "sfx/journal.ogg" 
    
    "In the warm, dim light of the library, Rosa opened the journal's cover."
    "She wasn't too surprised to find that a number of entries were written in different tongues."
    "The dates jumped from decade to decade. The writing spanned centuries."
    "Another suspicion validated."
    "Guilleme was... not human."
    "Or at least, he did not have a normal human lifespan."
    "This discovery made Rosa search her mind for her date of birth."
    "It distressed her that she could not remember."
    "She shook her head and turned back to the journal."
    "Despite the multitude of languages, the first entry was translated and rewritten several times."
    "For sentimental reasons, perhaps?"
    "Or maybe a feeble attempt at reminiscing a more innocent time."
    
    #Entry 1  
    show journal
    gd "--\n\n
    I am learning to write.\n\n
    Aelia gave me paper.\n\n
    I like Aelia.\n\n
    She wants me to call her mother.\n\n
    She smells like oranges.\n\n
    She says I am a gift from the goddess. \n\n
    But I don't know any goddesses.\n\n
    Aelia calls me Rai.\n\n
    I guess that is my name now.\n\n
    It is nice to have a name."
    hide journal
    
    play sound "sfx/page.ogg"
    "The other preceding pages were still in a different language."
    "Rosa flipped through the pages until she came upon one she could read."    

    play sound "sfx/page.ogg"
    show journal
    gd "{i} ---- \n\n
    They call me Eros.\n
    A god, a divine.\n
    They don't understand what I am.\n
    They either build me statues, or \n
    spit at my feet.\n\n
    I am a muse. \n
    I am a blight.\n
    A symbol...\n
    But, I am not the answer.\n
    It seems ironic, isn't it, that Love craves\n
    love above all? That which I need, that which\n
    I am, poisons me to the point that I am sick\n
    of its taste. {/i}"
    hide journal
    
    play sound "sfx/page.ogg"
    show journal
    gd "{i}6 May ---- \n\n
    I see it in the way people look at me, the \n
    way they act around me.\n\n
    Some would, of course, think of me as blessed. \n
    I have youth, health, and the gift of being loved.\n
    But I found that these gifts are curses as well.\n
    My youth forces me to always wander. My looks\n
    guarantee that I will always stand out.\n\n
    And love?\n\n
    The very same urge that blesses me quickly turns\n
    rabid. Yet I understand why.\n\n
    Oh, love. We all crave it, don't we? In the end,\n
    we are all drunk on the idea that only love could\n
    heal our brokenness. They all think I am this... cure.\n\n
    ...But I keep hoping there might be something\n
    else besides this twisted sentiment.. There must\n
    be. Mustn't there...?{/i}"
    if persistent.journal1WasReadBefore   is None:
        $persistent.journal1WasReadBefore  = True
        $persistent.currentLinesRead +=1
    hide journal
    
    if GetEndingCount() >=1:
        play sound "sfx/page.ogg"
        show journal
        gd "{i}6 March ---\n\n
        What am I? God, what am I? \n
        I am whole. I can think. I can bleed... \n\n
        But somehow, I am not... normal. Who am I? \n
        What is my purpose on this earth? I drown \n
        myself in delusions of grandeur, that I am \n
        made for something more. It should be, \n
        shouldn't it? These gifts, this life. It should \n
        all mean something. But the days pass and \n
        the slow, trickling horror that I am simply a\n
        mutation, a mistake, is creeping up on me. \n\n
        Day in and day out, a struggle to survive. \n
        Directionless and uncertain. I must be made\n
        for something more than this, but nobody \n
        told me what it is. {/i}"
        if persistent.journal2WasReadBefore   is None:
            $persistent.journal2WasReadBefore  = True
            $persistent.currentLinesRead +=1
        hide journal
    
    "Rosa read the words and found them tugging at her heart."
    "This was the same feeling she had had for years."
    "It almost seemed like the words were her own."
    
    if GetEndingCount() >=1:
        play sound "sfx/page.ogg"
        show journal
        gd "{i}2 December ---\n\n
        It is winter in Liechtenstein and even \n
        the fire can't take the chill off my \n
        weary bones.\n\n
        They named me Isaac. I don't speak\n
        much to anyone, but I like it here. \n
        The convent is a fine place to stay, \n
        until after winter, at least. I have\n
        finally learned English and German.\n\n
        I met a boy named James. He looks to\n
        be about the same age as I. He is an acolyte.\n
        He calls me his brother. I rather like that.\n\n
        He told me to be wary of the Monseigneur. \n
        Not that I don't have any clues otherwise.\n\n
        I always get a sour taste in my mouth,\n
        like acid, like vomit, whenever I am with him.\n\n
        I think I am tasting his shame.{/i}"
        if persistent.journal3WasReadBefore   is None:
            $persistent.journal3WasReadBefore  = True
            $persistent.currentLinesRead +=1
        hide journal
    if GetEndingCount() >=2:        
        play sound "sfx/page.ogg"
        show journal
        gd "{i}19 December --- \n\n
        Today I have learned the meaning of humility.\n
        It is the act of genuflecting. It is kneeling on \n
        the hard marble floor until your knees bleed.\n\n
        It is... Prostrating yourself upon the Lord.\n
        Opening your mouth and accepting \n 
        whatever is put in.\n\n
        They say it is called communion.\n I have
        learned a new word I hate. \n\n
        At least he was behind me so I didn't \n
        have to endure his stupid face during \n
        the whole ordeal.\n\n
        Last time, I couldn't help but laugh at the faces\n
        he made and I received a whipping afterwards.\n\n
        Glory be.{/i}"
        if persistent.journal4WasReadBefore   is None:
            $persistent.journal4WasReadBefore  = True
            $persistent.currentLinesRead +=1
        $ achievement.grant("Filthy Colours")
        $achievement.Sync()
        hide journal
    
    play sound "sfx/page.ogg"
    show journal
    gd "{i}I know I'm not supposed to be writing this.\n\n
    God, forgive me.\n\n
    I do not want to write it down.\n\n
    If I do, it will be the truth.\n\n
    Oh, Lord, please forgive me.\n\n
    I didn't mean to do it.\n\n
    I just wanted to stop hurting.\n\n
    I am hiding now. I slashed my face\n
    and cut my hair so they would not\n
    recognise me. Pain. Pain is good. A penance.\n\n
    ...Oh Lord, please...\n\n
    If there is a god listening, please \n
    strike me down!\n\n{/i}"
    hide journal
    
    "Bad memories began to surface in Rosa's mind."
    "{i}Desperation.{/i}"
    "{i}A cornered animal that fought back.{/i}"
    "It reminded her of her own sins."
    "Her hands were drenched in red."
    "And yet, here she was, planning to kill another man."
    "This had been her goal all along, hadn't it?"
    "That same, familiar guilt began to stir in her mind."
    "She bit her lip."
    
    play sound "sfx/page.ogg"
    "Rosa skipped some entries. Most of them were garbled, almost incomprehensible."
    "They were written in old ink, faded and unloved."
    "Still, though they were melancholic, they painted a picture of a man with sufficient black humor to keep sane."
    
    play sound "sfx/page.ogg"
    show journal
    gd "{i}28 November --\n\n
    The plague has confirmed my \n
    suspicions that I do not die from sickness.\n\n
    I don't know how to feel about that.\n\n
    ...Everyone is dead. \n\n
    But on the bright side, everyone is dead.{/i}"
    if persistent.journal5WasReadBefore   is None:
        $persistent.journal5WasReadBefore  = True
        $persistent.currentLinesRead +=1
    hide journal
    if GetEndingCount() >=1:  
        play sound "sfx/page.ogg"
        show journal
        gd "{i}4th December -- \n\n
        Somebody asked me my\n
        name when I snuggled close to the fire.\n
        I told them my name is John.\n\n
        It is not exactly a lie, is it?\n\n
        I've had so many names I must've been\n
        a {i}'John'{/i} at one point.\n\n
        I found that thought funny.{/i}"
        if persistent.journal6WasReadBefore   is None:
            $persistent.journal6WasReadBefore  = True
            $persistent.currentLinesRead +=1
        hide journal
    if GetEndingCount() >=2:   
        play sound "sfx/page.ogg"
        show journal
        gd "{i}23rd April 1471\n\n
        Thomas got me a job under the court of\n
        the Royal Prince Albert. I tried to object, but \n
        he told me to do it.\n\n
        I admire him greatly. His mind is deep.\n
        His demeanor like that of a king. I will \n
        help him in any way I can. I will support\n
        him. I just wish he'd listen to me \n
        sometimes. I know what he's planning, \n
        but he doesn't like it when I talk back. \n
        His temper is the only thing that distresses me.\n\n
        ...But I can't imagine living with \n
        anybody else. I love him.\n\n
        His love is strong, like ale mixed \n
        with blood and bruises.{/i}"
        $ achievement.grant("Domestic Abuse")
        $achievement.Sync()
        if persistent.journal7WasReadBefore   is None:
            $persistent.journal7WasReadBefore  = True
            $persistent.currentLinesRead +=1
        hide journal
    play sound "sfx/page.ogg"
    show journal
    gd2 "{i}7th June 1489\n\n
    For decades, I have searched for something in this life\n
    and I am always disappointed by transience. What \n
    am I looking for? Meaning? Hope? Love?
    ...Death, maybe? \n\n
    
    I can bleed. Wounds to the heart heal slower than the \n
    rest of my body. I think I may die if wounded enough. \n
    I have tried ...{/i}that{i}. There was a time when seeing\n
    myself bleed was the only reminder that I am not numb.\n\n
    
    Yet my body does not form scars, no matter how many \n
    times I draw my knife. Like any sign of age or ugliness,\n 
    they all fade. A wrinkle today, gone the next. As if my \n
    body isn't even my own to brand.\n\n
    That is a shame.\n\n
    I want to mar my body so badly that anyone who sees\n
    me will flee. But I have tried that too. People are crueler\n 
    when you are ugly. Why is that? Why do they feel the \n
    need to punish you simply because you are detestable?\n
    Perhaps because they can? Or perhaps because it is\n
    easy to be cruel to those which do not belong?\n\n
    
    I don't belong.\n\n
    
    It would be nice to... disappear one day.{/i}"
    hide journal
    
    m "There it is."
    m "There is confirmation that he can be killed."
    m "So he bleeds like everyone else, but heals enough not to die."
    m "A strike to the heart."
    m "If we find a way to leave this wound open, perhaps he can be exterminated."

    "Rosa continued reading."
    "Another feeling was starting to grow in her chest."
    "She began to question her cause the more she read through the journal."
    if persistent.journal8WasReadBefore   is None:
        $persistent.journal8WasReadBefore  = True
        $persistent.currentLinesRead +=1
    if GetEndingCount() >=2:
        play sound "sfx/page.ogg"
        show journal
        gd "{i}----\n\n
        I am staying under the bridge tonight,\n
        at least until the mutiny ends.\n\n
        They will never find her body. It's the \n
        best I can do.\n\n
        She should be thankful I didn't leave\n
        her to the dogs after what she had \n
        done to me. I was nothing to her \n
        but a poor sap to be manipulated.\n
        And yet... that fire in her eyes burned\n
        ever so lovely.\n\n
        Such sentiment... Hmph.{/i}"
        if persistent.journal9WasReadBefore   is None:
            $persistent.journal9WasReadBefore  = True
            $persistent.currentLinesRead +=1
        hide journal
    
    if openlocket and not rgloves and family:
        play sound "sfx/page.ogg"
        show journal
        gd2 "----\n\n
        {i}I have been staying in the old \n
        March farm. They are good people.\n\n
        They invited me to eat with them, \n
        and it was in the warmth of their fire\n
        that I knew then that I must leave.\n
        I will only destroy their happiness.\n\n
        For the briefest of moments, I was able\n
        to experience what it is like to be part of\n
        a family. Not an outsider, but accepted. \n\n
        Little Sissy has taken a liking to me, though.\n\n
        Children are curious creatures. They are\n 
        a constant reminder to humans of their\n
        own impending death, their own \n
        weaknesses and mortality. Yet people\n
        keep making them. One may wonder why,\n
        but it is not difficult to understand. It is\n
        the tantalizing thought, the hope, that no\n
        matter your past mistakes, you were able \n
        to make something pure at one point, watch \n
        it grow, watch it live. Such a poor thing, looking\n
        up to you for love and care. It is both power\n
        and vulnerability, both selfish and selfless.\n
        A curious thing indeed.{/i}"
        hide journal
    else:
        play sound "sfx/page.ogg"
        show journal
        gd "----\n\n
        {i}I have been staying in the old \n
        March farm. They are good people.\n
        They invited me to eat with them, \n
        and it was in the warmth of their fire\n
        that I knew then that I must leave.\n
        I will only destroy their happiness.\n\n
        For the briefest of moments, I was able\n
        to experience what it is like to be part of a\n
        a family. Not an outsider, but accepted.{/i}"
        hide journal
    if GetEndingCount() >= 1:
        play sound "sfx/page.ogg"
        show journal
        gd "{i}4th May 1490\n\n
        As years pass, it is beginning to dawn \n
        on me that humans have holes in their\n
        souls and they are desperate to fill them\n
        with whatever seems to fit. \n\n
        Sex, liquor, money, religion...\n\n
        I, too, have this gaping hole, and it is\n
        in my belly. I am always hungry. Always...\n
        hollow.\n\n
        We are really not that much different.\n\n{/i}"
        if persistent.journal10WasReadBefore   is None:
            $persistent.journal10WasReadBefore  = True
            $persistent.currentLinesRead +=1
        hide journal
    "Rosa shuffled through more pages and saw a different penmanship in one such entry."
    "It caught her eye."
    
    play sound "sfx/page.ogg"
    show journal
    gd "January 1500\n\n
    New century. I like it. \n\n
    I smell change in the air. It is so much \n
    easier to lie when you have the means.\n
    Trading is a good sport. My name \n
    nowadays is Baron Eric Daubeshire.\n
    How could I have forgotten mankind's \n
    paralyzing obsession with titles?\n\n
    
    Names have power. Titles have power. \n
    I simply bought a horse and good robes and \n
    introduced myself as such. Everyone \n
    fawned over it. \n\n
    
    I could get used to this. The taste is... \n
    refreshing. I must plan this better next \n
    time. A background, a story.\n\n
    People love stories. Maybe I shall be an\n
    actor next?"
    if persistent.journal11WasReadBefore   is None:
        $persistent.journal11WasReadBefore  = True
        $persistent.currentLinesRead +=1
    hide journal
    if GetEndingCount() >=1:    
        play sound "sfx/page.ogg"
        show journal
        gd "9th December 1506\n\n
        I am inside the Royal Court now, rather than serving it. \n
        The abundace is staggering. I have never seen\n
        such riches since Constantinople. \n\n
        I can handle myself better now. I have been \n
        catching up with the times. I have been reading\n
        books, conversing, attending social events.\n
        It is time to acquaint myself with the new era, and quit\n
        wallowing in depression and guilt.\n\n
        Frankly, it doesn't suit my new haircut.\n\n"
        if persistent.journal12WasReadBefore   is None:
            $persistent.journal12WasReadBefore  = True
            $persistent.currentLinesRead +=1
        hide journal
    
    play sound "sfx/page.ogg"
    show journal
    gd "27th March 1507\n\n
    Cretins, everywhere. Human nature\n
    stays the same. The powerful will \n
    take advantage of the damned.\n\n
    So, it is all a struggle for control. \n
    Is that all there is?\n\n
    I thought it would be different, \n
    somehow, in a learned class, \n
    in a different era. I was a fool to\n
    expect more.\n\n
    Fortunately, I am already well acquainted."
    if persistent.journal13WasReadBefore   is None:
        $persistent.journal13WasReadBefore  = True
        $persistent.currentLinesRead +=1
    hide journal
    
    if GetEndingCount() >=2:
        play sound "sfx/page.ogg"
        show journal
        if persistent.adult:
            gd "16th September 1508\n\n
            I have invited the shy Lady Isabella to walk with \n
            me tonight. She seemed to wilt at my touch, almost \n
            flinches when I come near her. It is funny because \n
            I know she secretly wants me to grab her neck, \n
            rip her clothes off and take her on the table \n
            in front of everyone.\n\n
            Whatever will her husband say?\n\n
            Everytime I look at her, I see her depraved cravings\n
            painted in her eyes. It makes me giggle out of the blue. \n
            She even wonders what it would be like if I use a \n
            cross in her ass. Maybe she'll find out."
            $ achievement.grant("Sacrilege and Sex")
            $achievement.Sync()
            hide journal
        else:
            gd "16th September 1508\n\n
            I have invited the shy Lady Isabella to \n
            walk with me tonight. She seemed to\n
            wilt at my touch, almost\n
            flinches when I come near her.\n\n
            Oh, I know she wants me... but how \n
            she resists! It makes me want to\n
            play with her even more."
            hide journal
        if persistent.journal14WasReadBefore   is None:
            $persistent.jourmal14WasReadBefore  = True
            $persistent.currentLinesRead +=1
    if GetEndingCount() >=2:
        play sound "sfx/page.ogg"
        show journal
        gd "30th March 1515\n\n
        I am fleeing the country to escape from jail.\n
        I guess some of my dirty books didn't sit well \n
        with the Church and the authorities.\n\n
        It gives me great pleasure to watch them \n
        flail and brandish me as a harlot all the while \n
        wondering what my thigh tastes like.\n\n
        I finally found out what they are.\n\n
        They are my playthings.\n\n
        I can poke them and do things to them, and\n
        they will still love me.\n\n
        I can be the most fiendish little devil, or a saint.\n\n
        I guess I shall play around a bit with \n
        a new name, dance the same old song."
        $ achievement.grant("Marquis de Sade")
        $achievement.Sync()
        hide journal
        
        play sound "sfx/page.ogg"
        show journal
        gd "4th October 1521\n\n
        I was careless before. I bit off more than\n
        I can chew. Perhaps I was too infatuated \n
        with the romp of royalty and the trappings of power. \n
        I should remember that my primary goal is \n
        to survive.\n\n
        Oh, but really. Where is the fun in that?\n\n
        I can be daring, sometimes. I just have to be smarter.\n
        I have the advantage of time on my hands.\n\n
        I have come to understand my real purpose in life. \n\n
        And that is to enjoy it.\n\n
        Otherwise, what else?"
        hide journal
        if persistent.journal15WasReadBefore   is None:
            $persistent.journal15WasReadBefore  = True
            $persistent.currentLinesRead +=1
        
    if GetEndingCount() >=1:   
        play sound "sfx/page.ogg"
        show journal
        gd "21st November 1550\n\n
        I... don't want to live anymore. \n
        My days are nothing but emptiness.\n
        I have told myself before that there\n
        is nothing else needed but to survive. \n\n
        But is that the truth?\n\n
        ...Is this all there is? \n\n
        If so, then Alex, please let me follow you\n
        into the darkness where death dines\n
        on souls.\n\n
        ...Please, forgive me... Forgive me!\n\n
        Why must human lives be so fragile?\n\n
        ...It was an accident. I didn't mean to.\n\n
        I got careless... I shouldn't have \n
        stayed that long."
        if persistent.journal16WasReadBefore   is None:
            $persistent.journal16WasReadBefore  = True
            $persistent.currentLinesRead +=1
        hide journal
        
    "The next entry's penmanship was scratchy and difficult to understand."
    play sound "sfx/page.ogg"
    show journal
    gd "1st December 1550\n\n
    I am tired of this life. It is all an \n
    endless cycle and I can't stand \n
    the taste of this any longer. Love\n
    turns to ash in my mouth.\n\n
    I am trying to stop. \n\n
    I want to stop.\n\n
    It is my seventh day without \n
    consuming anything other than\n
    normal food.\ It barely grazes the\n
    bottom of my stomach.\n\n  
    I want to see if I will die without \n
    eating love.\n\n
    I am sick of this."
    hide journal
    
    r "..."
    m "Now you know what he is, Rosa."
    m "He consumes love."
    if persistent.origin:
        m "All my suspicions were right."
        m "He is the man I have sought."
    else:   
        m "I do not know exactly what he is, but he is a monster."
        m "A demon!"
    m "Didn't I tell you? I felt it in my bones!"
    if persistent.journal17WasReadBefore   is None:
        $persistent.journal17WasReadBefore  = True
        $persistent.currentLinesRead +=1
    call momjournal from _call_momjournal

label morejournal:    
    $ morejournal = True

    play sound "sfx/page.ogg"
    show journal
    gd "4th December 1550\n\n
    This is my tenth day without it and I am still\n
    alive. Barely.\n\n
    I can't... even see where I am writing\n
    anymore. I am so weak. My body is in pain.\n\n
    
    Am I dying? I am afraid.\n\n
    After all my whining, I still want life.\n
    Isn't that funny?\n\n
    
    I am sleeping again. Sleep is the only thing that\n
    sustains me. It is dangerous for me to linger \n
    in sleep's domain, especially when I have \n
    not eaten.\n\n
    I have to keep writing. It's the only way to tell \n
    my mind is still my own.\n\n
    I can't take it anymore."
    hide journal
    
    r "..."
    r "So that was why he fell so easily for the sedatives."
    m "That is not all."
    m "Perhaps we can destroy him this way as well."
    m "He is most vulnerable right now."
    m "If we attack now, he won't be able to put up any defenses."
    
    play sound "sfx/page.ogg"
    show journal
    gd "12 February 1601\n\n
    I have rewritten all of my entries into a new journal.\n
    I have kept some that were close to my heart. \n
    I don't know why I still keep writing. Perhaps this \n
    journal is my will to live.\n\n
    I look back on it and it reminds me of the years I have \n
    endured. Sometimes I have a suspicion that this... \n
    This is my only reason. This perverse obsessive\n
    compulsion to hoard time. Years. Names.\n\n
    It can't end because it's such a shame.\n\n
    
    ...It is almost time to leave again.\n\n"
    hide journal
    
    play sound "sfx/page.ogg"
    show journal
    gd"19 August 1605\n\n
    My ship arrived in France today.\n
    I plan to settle in a smaller town. \n
    I am sick of the taste of instant\n
    gratification.\n\n
    Maybe I will try a different approach \n
    next time. I need to blend in with the\n
    citizens first. My French needs work."
    hide journal
    
    play sound "sfx/page.ogg"
    show journal
    gd "29th June 1784\n\n
    Why do I keep doing this to myself?\n\n
    I shouldn't care so much.\n\n
    It always ends up broken or destroyed.\n\n
    I never learn.\n\n
    I should leave before--"
    hide journal
    
    "The entry was not finished and some fresh pages were torn out of the book."
    "Even if there were no names mentioned, Rosa felt that the last entry was for Catherine."
    if GetEndingCount() == 0:
        "There were more entries that she didn't explore, but she decided to close the book."
        "She had read enough for now."
        $ achievement.grant("Incomplete Journal")
        $achievement.Sync()
    elif GetEndingCount() == 1:
        "There were still quite a few entries that she didn't explore, but she decided to close the book."
        "She had read enough for now."
        $ achievement.grant("Incomplete Journal")
        $ achievement.grant("More entries to unlock")
        $achievement.Sync()
    elif GetEndingCount() == 2:
        "Those were all the entries she could read."
        "She closed the book."
        $ achievement.grant("Incomplete Journal")
        $ achievement.grant("More entries to unlock")
        $ achievement.grant("Unlocked all entries")
        $achievement.Sync()
    elif GetEndingCount() > 2:
        "Those were all the entries she could read."
        "She closed the book."
        $ achievement.grant("Incomplete Journal")
        $ achievement.grant("More entries to unlock")
        $ achievement.grant("Unlocked all entries")
        $ achievement.grant("Unlocked all of Guilleme's entries")
        $achievement.Sync()
    if persistent.morejournalWasReadBefore   is None:
        $persistent.morejournalWasReadBefore  = True
        $persistent.currentLinesRead +=1
label reveal:
    "Rosa's hands were shaking by then."
    "A growing feeling of understanding came over her."
    "His thoughts were too much like her own."
    "They were too similar."
    r "..."
    r "Guilleme consumes love--"
    stop music fadeout 3.0
    "Rosa remembered the taste in her mouth when she had kissed Catherine."
    "There was something else in that kiss."
    "A boundless flavour that coated her mouth and made her realize how {i}hungry{/i} she was."
    play sound "sfx/heartbeat.ogg"
    "The same night that Catherine began to change."
    play sound "sfx/heartbeat.ogg"
    "Rosa's throat throbbed. The thumping felt like it resonated through her whole body."
    "She fell to her knees."
    play sound "sfx/heartbeat.ogg"
    "That same feeling of dread rose up in her throat."
    "The mere mention of the thought seemed to summon the feeling in her chest."
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=3)
    "She gagged."
    r "Did I taste Catherine's love that night?"
    r "Then that means that I am also--"
    "..."
    r "...Mother?"
    r "Am I--"
    r "The same?"
    if openlocket and not rgloves and family:
        "She hastily pulled out the locket that Guilleme had given her previously."
        "It was still as difficult to open as before,"
        "But right now, Rosa was armed with a terrifying conclusion."
        "She struggled with the damn thing until she thought her nails would peel off her fingers."
        "The pendant popped open, revealing a yellowing portrait inside."
        if persistent.locket1WasReadBefore   is None:
            $persistent.locket1WasReadBefore  = True
            $persistent.currentLinesRead +=1
    m "Oh, finally figured it out, have you?"
    m "Do you see it now?"
    if openlocket and not rgloves and family:
        m "Do you see why Mother wants his punishment?"
    if persistent.origin:
        m "All these years..."
        m "I have never learned how to destroy him."
        m "At last, his time has come."
        r "M-Mother..."
    m "My child..."
    m "He is a monster."
    m "The very thing I stopped you from becoming."
    m "Don't you see? I saved you!"
    m "I stopped you from feeding on other people's love."
    m "I didn't want you to be filthy!"
    m "Mother's love is all you need."
    r "..."
    m "You have learnt enough."
    m "Now you know what to do."
    m "Kill him."

label rosadecides:    
    stop music fadeout 2.0
    scene bg rosamono  
    show rs madbig
    m "He is what I have feared the most, Rosa."
    show rs thinkbig with slowdissolve
    r "..."
    show rs madbig  
    m "He must perish."
    play music "sfx/rosadecides.ogg"
    r "..."
    show rs depbig  
    "Rosa's face contorted into worry."
    "The discovery of Guilleme's identity shook her to her core."
    "But it also made her feel the burden of their years together."
    "Perhaps the understanding of his pain as well."
    r "Must we really do this, Mother?"
    show rs madbig  
    m "You still have doubts after everything you have learned?"
    show rs depbig  
    r "No... But--"
    r "This knowledge just makes me want to--"
    show rs madbig  
    m "You stupid child."
    m "Can't you see it is what should be done?"
    
    call m015 from _call_m015
    
    show rs depbig  
    r "..."
    r "Is it really?"
    r "It is easy to say that...."
    r "But..."
    show rs hmpbig      
    r "What do {i}you{/i} really want?"
    
    ##############################
    call m07 from _call_m07
    show rs hmpbig   
    r "But is it really the right thing?"
    r "Is death the only way to change him?"
    call killhim from _call_killhim
    show rs depbig  
    r "Am I not like him, Mother?"
    show rs normbig  
    r "I am also... a monster."
    r "We are the same."
    
    ##############################
    call m014 from _call_m014
    
    show rs flinchbig  
    r "..."
    m "Now that you know his true face, there is only one thing to do!"
    m "Kill him!"
    
    if meanmom >= 5:
        call badrosa from _call_badrosa
    elif rosamonster:
        call badrosa from _call_badrosa_1
    elif badperson:
        call badrosa from _call_badrosa_2
    else:
        pass
    r "..."
    show rs depbig  
    r "..."
    show rs hmpbig  
    r "..."
    show rs normbig  
    r "No."
    m "No?"
    show rs depbig  
    r "I..."
    r "I think he can change."
    r "Perhaps I might still be able to save him."
    
    ################################
    call m08 from _call_m08

    show rs normbig  
    r "Yes, but isn't he a creature of love?"
    r "So am I."
    r "Love, no matter how lonely and depraved, always gives all of itself."
    show rs thinkbig  
    r "Only I can understand."
    r "Only I can save him."
    r "That is why I want to try."
    
    ###############################
    call m09 from _call_m09
    
    r "I will light Agape and make him remember."
    
    ###############################
    call m010 from _call_m010
    r "Trust in me, Mother."
    r "I will do the right thing."
    m "You?"
    m "{i}You?!{/i}"
    show rs thinkbig
    
    m "What could you possibly hope to do, you dumb child?!"
    m "You are ignorant, naive!"
    m "Just a brainless, dangerously idealistic girl with her head up in books and fiction."
    m "There is no happy ending in this life, you worm!"
    m "Oh, you bring me so much pain!"
    m "I should have abandoned you years ago!"
    r "You cannot hurt me any longer, Mother."
    show rs smilebig  
    r "I know that you love me."
    r "You are my memory."
    show rs thinkbig  
    if openlocket:
        r "As such, I want to remember you as the one person who loved me with her whole heart."
    else:
        r "As such, I want to remember you as the one person who cared for me..."
        r "You, who stayed with me despite my burden to your soul."
    r "Not the tainted woman who abused me."
    r "It is my fault you act this way."
    r "Your voice is my own insecurities and my own pain."
    show rs normbig  
    r "Now, not anymore."   
    m "How dare you degrade me into an apparition!"
    m "I am real!"
    m "Listen to me!"

    if goodperson:
        r "You have called me a good person before."
    r "You believe in me, don't you, Mother?"
    r "You have guided me well."
    r "Believe in me."
    show rs normbig  
    r "Believe that I am doing the right thing."
    m "..."
    show rs thinkbig  
    r "I love you so much."
    show rs normbig  
    r "But I cannot follow all your wishes anymore."
    if persistent.origin:
        r "The cycle of hate stops with me."
        r "I will not let the past taint my future."
        r "Mother..."
    r "Let me make my own decisions from now on."
    
    ###############################
    call m011 from _call_m011
    
    show rs normbig  
    "I will save him, whether you allow me to or not."
    
    ##############################
    call m012 from _call_m012
    
    show rs thinkbig  
    r "I'm sorry, Mother..."

    r "I know you hate him from the bottom of your heart."
    r "But I have already forgiven him."
    r "Like how I have already forgiven you."
    
    ##############################
    call m013 from _call_m013
    
    r "I will try to save him from himself because that's what I'm supposed to do."
    r "Perhaps that is the reason why I was sent his way."
    show rs thinkbig  
    r "I got to spend years with him and have memories of him."
    r "He taught me how to be strong."
    if openlocket and not rgloves and family:
        r "He got to watch me grow into this strength."
    else:
        r "I was happy knowing him."
    show rs smilebig  
    r "It is more than I can ask."
    m "You do know that he does not feel the same way for you?"
    m "He does not love you, child."
    show rs thinkbig  
    r "Yes."
    show rs smilebig  
    r "That makes me better than him."

    r "Because I love him without asking for anything in return."
    show rs thinkbig with Dissolve(0.5, alpha=True)
    scene bg black with dissolve
    m "A concept that has never yet crossed his mind."
    
    call m016 from _call_m016
    
    $ achievement.grant("The Talk")
    $achievement.Sync()

    $renpy.pause(delay=None)
    if persistent.chap6WasReadBefore   is None:
        $persistent.chap6WasReadBefore  = True
        $persistent.currentLinesRead +=1
    call chap8 from _call_chap8

return


### BAD ENDINGS ####
label badrosa:
    stop music fadeout 2.0
    show rs depbig  
    "Rosa bit her lip until she could taste blood."
    
    r "But M-Mother, please..."
    r "Don't make me kill anyone again."
    r "I am scared."
    call killsomeone from _call_killsomeone  
    r "This isn't right."
    r "I can't kill another person, Mother!"
    m "Yes, you can."
    m "You must."
    show rs annoyedhuhbig
    m "To fulfill your goal, it is necessary to crush things along the way."
    show rs crazylaughbig
    m "Just remember that they don't matter."
    m "It is just you and I, forever, darling."
    m "Trust no one."
    m "Love no one, but me."
    play music "sfx/doom.ogg" fadein 4.0
    show rs furiouscrybig  
    m "The rest of the world can crumble to dust."   
    m "You have thought about punishing him too, haven't you?"
    show rs superconfusedcry  
    r "..."
    r "W-What--?"
    r "N-No..."
    if rosajealous:
        show rs madbig
        m "How dare he put you on the sidelines?"
        m "Are you not good enough to love?"
        show rs angryarousedbig
        r "{i}Am I not fetching enough?{/i}"
        r "{i}Am I not pretty enough?{/i}"
        r "{i}Why didn't you feed on me instead?{/i}"
        show rs furiouscrybig
        r "No..."
        show rs hmpcrybig
        m "It bothers you, doesn't it?"
        show rs superconfusedcry  
        r "How could you want Catherine and not me?"
        $ achievement.grant("Green-Eyed")
        $achievement.Sync()
        show rs angryarousedbig
        r "{i}I'm better than her! She doesn't understand you the way I do!{/i}"
        r "{i}You are... the only one I've wanted this much.{/i}"
        r "{i}Why won't you... desire me?{/i}"
        r "{i}Everyone does...{/i}"
        r "{i}Why not you?{/i}"
        show rs superconfusedcry
        r "S-Stop!"
        show rs angryarousedbig
        r "{i}And just when my heart turns to Catherine, you take her away?!{/i}"
        r "{i}Bastard!{/i}"
        r "{i}You took my heart! You took Catherine's!{/i}"
        r "{i}You...{/i}"
        show rs angrycrybig
        r "I hate you!"
        r "You shouldn't be allowed to exist!"
        r "..."
        show rs crazysmilebig
        m  "The very thought of him confuses you."
        if persistent.jealous1WasReadBefore   is None:
            $persistent.jealous1WasReadBefore  = True
            $persistent.currentLinesRead +=1
    show rs shockbig  
    m "Catherine and him... They are both the forbidden fruit that you crave so badly."
    show rs arousedsmilebig  
    m "Mother keeps you right, darling."
    show rs crazysmilebig  
    m "Mother keeps you clean."
    m "If you kill the dirty man, then you will stay pure."
    show rs angrycrybig  
    r "N-No..."
    show rs crazylaughbig  
    m "You don't have to be confused."
    show rs furiouscrybig  
    r "B-But--"
    call convince from _call_convince
    show rs furiouscrybig  
    r "B-But it shouldn't be up to me to decide!"
    r "It's not how it's supposed to---"
    call shout from _call_shout
    show rs hmpcrybig  
    "Tears formed in Rosa's eye."
    show rs superconfusedcry  
    "She grabbed her head and scratched viciously."
    show rs furiouscrybig  
    r "No..."
    show rs poorcrybig  
    r "I don't understand anymore!"
    r "I am so confused--"
    r "Please, Mother--"
    call obey from _call_obey
    show rs arousedsmilebig  
    m "Then do as I say, my child."  
    scene bg red  
    play music "sfx/eros.ogg"
    m "Kill him."
    "Rosa began to giggle. Her tongue danced in her mouth."
    show rs crazysmilebig  
    "She licked her lips in delight."
    show rs crazylaughbig  
    r "Ye~s!"
    r "Kill him."
    r "This is what he deserves for being filthy."
    r "I am a little monster, too, aren't I?"
    r "But Mother kept me clean."
    r "She feeds me and loves me and kisses me--"
    r "I'd like to... cut his pretty neck open, Mother."
    r "Watch the pretty blood drain from his dirty mouth."
    r "Is that alright?"
    r "I am a monster."
    $ achievement.grant("Monster")
    $achievement.Sync()
    r "But Mother keeps me right."
    r "Mother, can I please play with him a little bit?"
    r "Pretty please?"
    show rs crazysmilebig  
    r "I want to do naughty things to him."
    show rs crazylaughbig  
    "She laughed."
    r "I want to enjoy his punishment."
    show rs crazysmilebig  
    r "I hate him."
    r "I love him."
    show rs crazylaughbig  
    r "Now I understand why."
    "Rosa tittered again."
    show rs crazysmilebig      
    r "I will kill him, Mother."
    r "For all his sins, he deserves to die."
    show rs flinchbig  
    "For a moment Rosa was shocked by the gravity of her own words…"
    show rs arousedbig  
    "…but Mother's voice came to soothe her."
    m "That's my darling girl."
    m "Make sure you make him suffer for as long as possible."
    m "All the pain in the world wouldn't be enough to punish him for the damage he's caused."
    "There was no doubt about that."
    "Regardless of who Guilleme was, whether he was a saint or devil…"
    "…killing him was the right thing to do."
    show rs crazylaughbig  
    r "Yes, Mommy dear."
    r "I will follow everything you say!"
    show rs crazysmilebig  
    r "But I get to have fun too, right?"
    show rs arousedbig  
    scene bg black  
    "Rosa lit Eros, bathing her face in the scarlet light cast by the candle."
    scene bg red  
    show rs arousedbig  
    "The night went on."
    "The spell buried Guilleme into a deeper slumber."
    if dagger:
        "She brought out the dagger she had stolen from Guilleme's room."
        r "So pretty."
    else:
        "She brought out a gigantic carving knife she'd snuck out of the kitchen."
        "It was almost as long as her forearm."
        "It had been sharpened enough to tear meat from bone."
    show rs tongueoutbig  

    "She played with the shiny thing whilst whistling a lullaby."
    r "Sleep now, my precious Gilly."
    r "Dream of me..."
    r "Dream, and descend into the depths of your personal hell."
    r "I hope you like your gift."
    "Rosa giggled while pricking the tip of her tongue with the sharp knife."
    r "Let me deliver your atonement."
    scene bg black with None
    $renpy.pause(delay=None)
    if persistent.badrosaWasReadBefore   is None:
        $persistent.badrosaWasReadBefore  = True
        $persistent.currentLinesRead +=1
    
    call chap7 from _call_chap7
    
return
