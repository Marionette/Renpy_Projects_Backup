label prodnotes:      
    scene bg black
    m "Hello there! This is Ame speaking!"
    m "I hope you're enjoying the game!"
    if GetEndingCount() <= 3:
        jump pnlocked  
    if GetEndingCount() >= 4:
        jump pnunlocked       
return


label pnlocked:
    m "This content is locked at the moment."
    m "Check back again after you've unlocked all the endings!"
    m "Good luck!"
    menu:
        "Back to Bonus Screen":
            #$ renpy.call_screen("extra_bonus")
            return
        "More":
            jump more
    return

label pnunlocked:
    m "Good job unlocking all the endings!"
    if GetEndingCount() >= 5:
        if persistent.congrats:
            m "Congratulations on getting the secret end, by the way!"
            m "That is amazing!"
            m "I hope you enjoyed it!"
            scene bg black
            $ persistent.congrats = False
    call notes from _call_notes 

return
        

label notes:
    
    menu:
        "{size=-3}Is there anything in particular you'd like to know?{/size}"
        "Ideas and Mythology":
            jump idea
        "Characters":
            jump char
        "Trivia":
            jump trivia
        "More":
            jump more
        "Back to Bonus Screen":
            jump prodnotes
return

label idea:
    m "This story was brought about by the question:"
    m "{i}What if Cupid is the bad guy?{/i}"
    m "In case you haven't gotten it from the context, Guilleme is {i}*SPOILER!*{/i} the titular character Cupid."
    scene bg cupidsketches
    "It was back in 2007 when I started drafting ideas on Cupid being a monster."
    "Someone or something who eats \"hearts\" or love."
    scene bg cupidsketches2
    "He was supposed to be a dark being, since I've always been suspicious of that cheery, winged brat."
    "Why is he always portrayed as angelic and innocent, anyway?"
    "{i}\"Being shot by Cupid hurts\"{/i}, said my emo teenage brain. {i}\"He must be a hunter!\"{/i}"
    "{i}\"What if he's just bringing hearts together so he can eat them?!\"{/i}"
    "{size=-3}(What a weird kid.){/size}"
    scene bg black
    m "The story was first designed to be an Adventure RPG, looking for items and solving puzzles."
    m "Unfortunately, I wasn't a skilled enough programmer back then (or even now lol)."
    m "The story, at that time, was quite a mess so I didn't pursue it further."

    m "Thank goodness for NanoReno 2015, a month-long VN Jam during the month of March."
    m "I decided to tackle something I was familiar with, so I dusted off ye big ol' treasure chest of unused story ideas--"
    m "And here we are!"
    $renpy.pause(delay=None)
    m "Yes, I took inspiration from the Roman myth of Cupid, the god of love."
    m "But Guilleme in this story is not Cupid, the god. He's {i}a{/i} Cupid."
    m "A broken, supernatural creature that takes love as sustenance, and (un-)fortunately, emits it, as well."
    #m "So goes the description."
    m "There were talks of incubi, nephilims and fallen angels in the writer's forum while we were drafting."
    m "Somebody also mentioned {i}'Energy Vampires'{/i}."
    m "I was adamant not to stick to any established lore, however."
    $renpy.pause(delay=None)
    m "So, wait, are there more cupids out there?"
    m "Probably not."
    m "In my mind, there is only Rosa and Guilleme."
    m "Sort of an inversion of Cupid and Venus."
    m "Whenever I read the myths I have always wondered why Venus was always portrayed as sort of resentful and scheming."
    m "While Cupid is just this chill, nekkid kid."
    m "They are both creatures of love, aren't they?"
    m "It interests me that {i}love{/i} seems to have two faces."
    m "One is innocent, while the other is manipulative."
    m "In my research, I also found that Cupid and Venus used to be portrayed as lovers in the earliest myths. "
    m "I tried to emulate it in the game, where the relationship between Guilleme and Rosa is ambiguous, filled with unknown tension."
    $renpy.pause(delay=None)
    m "There are also hints of Psyche in both Rosa and Catherine. Psyche, a woman who descends to the darkest depths of the underworld after seeing her lover's real face."
    m "Psyche was told she married a monster. Upon her sisters' prodding, she found that she married Cupid, the beautiful god of love."
    m "In this story, it's inverted, as Rosa/Catherine both thought of Guilleme as a good man, but later found he is a dark being."
    m "I will discuss more themes and in-depth thoughts in the Cupid Artbook."
    m "If you're interested, you can access it {a=https://fervent.itch.io/cupid-artbook}here{/a}."
    $renpy.pause(delay=None)
    if persistent.ideaWasReadBefore   is None:
        $persistent.ideaWasReadBefore = True
        $persistent.currentLinesRead +=1
    jump notes
label trivia:
    nvl clear
    m "Did you know?"
    m "In the 2007 draft, Rosa's original name was Madeleine."
    m "Catherine's name was Emilia."
    m "And Guilleme's name was Lenard."
    m "I'm pretty happy with their current names, however."
    nvl clear
    m "A lot of people pointed out that Guilleme is supposed to be spelled {i}'Guillaume'{/i}."
    m "A French beta-tester commented that it is somewhat uncanny for a French person to have a non-Christian name back in the old days."
    m "Even to the point that people will refuse to do business with you if you have a weird name."
    nvl clear
    m "That is quite an interesting bit of information!"
    m "I was contemplating whether or not I should change it."
    nvl clear
    m "In the end, I decided to keep it, for nostalgia's sake, and also for a certain effect."
    m "Guilleme was masquerading as something else."
    m "His name is the first hint that he did not belong."
    nvl clear
    m "I liked how the name worked as his introduction with the court ladies."
    m "He is weird, he stands out, and might possibly be sinister, but people can't help but be drawn to him."
    nvl clear
    m "And I imagine Guilleme choosing such a name just to be cheeky."
    m "(In his diary, he did confess to problems with authority and the Church.)"
    nvl clear
    $renpy.pause(2.0)
    m "There was a draft of a fourth character, a prince, trapped in a portrait."
    m "He was supposed to be Guilleme's remaining innocence and a possible love interest for Rosa."
    m "Sort of a reverse Dorian Gray."
    m "He was too shallowly entwined in the overall plot, though, so he got lynched."
    nvl clear
    $renpy.pause(2.0)
    m "Originally, the story was supposed to center around Guilleme and Rosa's relationship, with Catherine only getting mentioned in passing."
    m "But while drafting the story, Rosa's journey didn't make much sense if we didn't know who she was doing it for."
    $renpy.pause(delay=None)
    if persistent.triviaWasReadBefore   is None:
        $persistent.triviaWasReadBefore  = True
        $persistent.currentLinesRead +=1
    jump notes
    
return
    

label char:
    menu:
        "{size=-3}About the characters{/size}"
        "Rosa":
            nvl clear
            m "Rosa's development is something I'm quite proud of."
            m "Right off the bat, there was a danger of her being a one-dimensional stock character:"
            m "{i}Introvert with voices in her head.{/i}"
            m "No purpose but to move the plot along."
            nvl clear
            m "I floundered a bit on what she was all about."
            m "How will she grow? What did she learn?"
            m "Thankfully, she answered it for us."
            nvl clear
            m "She started as a masochist with low self-esteem and a very twisted view of love."
            m "But she grew up, learned from people along the way."
            m "She became a strong, kind-hearted gal who wants to believe in people, despite her abuse."
            m "(In the good endings, at least.)"
            m "I think that's the mark of a really strong person."
            m "One who doesn't give excuses to be kind, despite the pain they carry."
            nvl clear
            $renpy.pause(2.0)
            m "I wonder what she would be doing after the events of the game?"
            m "Maybe she would retire to a quiet life? Or would she go on an adventure?"
            m "She has social anxiety and is an introvert at heart."
            m "But I'd really love to see her going around the world and exploring!"
            nvl clear
            $renpy.pause(delay=None)
            jump char
            return
        "Guilleme":
            nvl clear
            m "Guilleme's public persona is a sweet and kind-hearted man; a little naive and very generous."
            m "The real Guilleme is a self-destructive, jaded cynic who treats love like a fix to cover up his despair and guilt."
            m "Nevertheless, he is a being born of love. I'd like to think he is innately good."
            m "After all, love is known to be a beautiful and uplifting thing."
            m "...But it can quickly turn dark and selfish."
            m "In short, Guilleme has the capacity for good, but simply gives himself excuses not to be."
            nvl clear
            m "He's not {i}exactly{/i} evil, just a brat. His true character is more like a kid:"
            m "{i}(a reference to Cupid being depicted as a child-like cherub){/i}"
            m "Stubborn, immature, self-centered and lonely."
            m "He likes to play and doesn't take things too seriously."
            nvl clear
            m "He has severe self-esteem issues, and in many ways, very similar to Rosa."
            m "They both get attached easily and have a tendency to give everything they have."
            m "He tries his hardest not to let anyone see through him, though."
            nvl clear
            $renpy.pause(2.0)
            m "He is also a junkie."
            m "He has no self-control, since nobody taught him how."
            m "Like most kids, his self-gratification is his top priority."
            m "So even though he falls in love, he will {i}always{/i} put his needs first."
            nvl clear
            $renpy.pause(2.0)
            m "In one of the good ends, he was portrayed as somebody with the possibility to grow or change."
            m "Whether or not he chooses to, is up to the mind of the viewer."
            m "Even in the epilogue, he is still a bit flimsy with his ideals. He still struggles with self-control."
            nvl clear
            m "{i}\"At least, I don't harm anyone anymore!!\"{/i} I can hear him say."
            nvl clear
            m "A step in the right direction, but he still has a long way to go."
            nvl clear
            $renpy.pause(delay=None)
            jump char
            return
        "Catherine":
            nvl clear
            m "I wanted to portray Catherine as a funny, energetic dreamer."
            m "She's a hothead with terrible mood swings. She is fiercely loyal to her friends, and also very ambitious."
            m "Ultimately, she wants to do the right thing."
            m "She's a compassionate person, kind and always ready to help."
            nvl clear
            m "I didn't want her to be a 'stuffed in the fridge' dead girlfriend character."
            m "I wanted her to make a difference in Rosa and Guilleme's lives,"
            m "Even if they are these powerful love beings and crap."
            nvl clear
            m "One of my major concerns was whether I portrayed Catherine right."
            m "Was her kindness enough to change Rosa and Guilleme?"
            nvl clear
            m "Maybe it was..."
            m "Since Rosa changed for the better."
            m "She became more confident, had begun to accept herself, started to have dreams like Catherine--"
            m "And Guilleme actually contemplated saving her. He, who was so selfish."
            nvl clear
            m "It's all a bit between the lines, though."
            m "I was tempted to show more of the interactions the three had while growing up."
            m "But...!"
            m "That's what fanfics are for, right? *wink* *wink*"
            nvl clear
            m "Through Catherine, I wanted to show that kindness can really change another person."
            m "And death doesn't mean your effect on people has ceased."
            nvl clear
            $renpy.pause(delay=None)
            jump char
            return
        "Mother":
            nvl clear
            m "Mother deserves a worthy mention, because I think she's quite an interesting character."
            m "During the draft stages, the group had very different takes on her."
            m "Somebody wanted to portray her as straight-up sadistic, while another writer wanted her to be snide and sarcastic."
            m "Another draft had her sound like a funny cartoon villain (which was fun actually, but it didn't quite fit)."
            nvl clear
            m "It was another pitfall, since she was starting to sound like a shoulder devil."
            m "Just a weird, annoying voice that taunted Rosa when she feels like it."
            m "A bit useless in the whole plot."
            nvl clear
            m "I changed it midway, making Mother's purpose into Rosa's redemption."
            m "She's cruel, but she wants to save Rosa from becoming an addict like Guilleme."
            m "Sure, she's usually scornful and verbally abusive."
            m "But her core is still love."
            m "Whether or not that kind of love is valid and/or {i} \"good\"{/i} is a subjective question."
            nvl clear
            $renpy.pause(delay=None)
            m "The idea for Mother as a character you control came about while talking with tinytim12 from Lemmasoft Forums."
            m "Hi there, Tim!"
            nvl clear
            m "I was looking for people to bounce ideas with me and I stumbled upon his work:"
            nvl clear
            m "\"I Think My Head is Darkness\" (Check it out!)"
            nvl clear
            m "In it, the main character was talking to you, the player, asking you to decide what she should do."
            m "It was very interesting, the thought that you 'affect' the characters rather than 'control' them."
            nvl clear
            m "When the Cupid demo was released, a number of people reacted to this feature positively."
            m "The usual VN choice system suddenly had emotional weight."
            m "They were caring for some other character, knowing that whatever they 'tell' her will affect her and not them."
            m "Overall, it was a nice feature and adds another layer of immersion to the story."
            nvl clear
            $renpy.pause(delay=None)
            jump char
            
        "Return":
            jump notes
    if persistent.charWasReadBefore   is None:
        $persistent.charWasReadBefore  = True
        $persistent.currentLinesRead +=1
   
return
    
    
label more:
    menu:
        "{size=-3}Links and Plugs, etc.{/size}"
        "Artbook":
            m "Do you want more about the Cupid world?"
            m "Then please consider buying Cupid's {a=https://fervent.itch.io/cupid-artbook}Official Artbook{/a}!"
            m "The document contains insider info, psychology on the characters, drafts, sketches, tutorials and much more!"
            m "If you have enjoyed this story, the Artbook is a wonderful supplement to the game."
            m "Download it {a=https://fervent.itch.io/cupid-artbook}here{/a}!"
            m "Enjoy!"
            jump more       
        "Other projects":
            m "Currently I have a demo for a fairytale puzzle game that I worked on for a while, {a=https://fervent.itch.io/theblackbeastvn} \"The Black Beast.\"{/a}"
            m "It is {i}totally{/i} different from Cupid. Very sweet, child-like and innocent."
            m "I-It's not all gore, sex  and darkness in my brain hhuhu."
            m "M-Maybe..."
            m "But I do hope you {a=https://fervent.itch.io/theblackbeastvn}check it out{/a}!"
            $renpy.pause(2.0)
            m "I have another finished game called {a=https://fervent.itch.io/whoismike}\"Who is Mike?\"{/a}"
            m "It's a free mystery/thriller about doppelgangers and mistaken identities."
            m "It's a little bit more light-hearted than Cupid, and very short at a run-time of two hours."
            m "I hope you enjoy it!"
            m "Download it {a=https://fervent.itch.io/whoismike}here{/a}!"
            jump more
        "Updates":
            m "If you want more updates, please follow me on {a=https://twitter.com/ameliori}Twitter{/a}."
            m "You can watch me spazz on art, writing and storytelling."
            m "See you there!"
            jump more
        "Patreon":
            m "I also run a small {a=https://www.patreon.com/ameliori}Patreon{/a} where I dump my art and ideas."
            m "Be part of my little circle {a=https://www.patreon.com/ameliori}there{/a}."
            jump more
        "Back":
            jump prodnotes
    if persistent.moreWasReadBefore   is None:
        $persistent.moreWasReadBefore  = True
        $persistent.currentLinesRead +=1
    $renpy.pause(delay=None)
    jump prodnotes
   
return
          
