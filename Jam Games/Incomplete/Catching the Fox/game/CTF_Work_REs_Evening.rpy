# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

##EVENING REs

label ek1:
    
    "Hmm... let me just check the office kitchen."
    
    "It might need to be restocked..."
    
    scene black with dissolve
    
    scene o_kitchen with pixellate
            
    si "Oh. Look at that. There's no more napkins or forks in the drawers... but where do they keep the new packages of plasticware?"
    
    show black with dissolve
        
    hide black with dissolve
        
    si "..."
        
    si "Okay, so next objective: actually {i}buy{/i} forks and napkins to restock in here."
    
    si "...With the company card, of course."
    
    scene black with dissolve

    return
    
label ek2:
    
    "Hmm... let me just check the office kitchen."
    
    "It might need to be restocked..."
    
    scene black with dissolve
    
    scene o_kitchen with pixellate
    
    si "Hm..."
    
    si "Forks, spoons and knives all in the drawers, nothing in the dryer rack..."
    
    si "Wow, nothing in the sink either! All the dishes are clean and everything!"
    
    "I guess I was a little prejudiced. I definitely assumed it'd be messier since most of the co-workers I've seen today are male."
    
    "My bad."
    
    "But who could've..."
    
    si "Ah, I wonder if it was Joel."
    
    si "Probably."
    
    scene black with dissolve\
    
    return
        
label ek3:
    
    "Hmm... let me just check the office kitchen."
    
    "It might need to be restocked..."
    
    scene black with dissolve
    
    scene o_kitchen with pixellate
    
    si "Hm..."
    
    si "There's spoons and knives but no forks."
    
    si "There's some dishes in the sink, too."
    
    "Oh, well. I'm in here already so I may as well wash them."
    
    show black with dissolve
    
    hide black with dissolve 
    
    "All right! All done."
    
    scene black with dissolve
    
    return

######################################################

######################################################

label ed1:
    
    si "Let me just look through the caller ID--"
    
    "Oh, wow."
                    
    "I have to call this agency back. I'm kind of surprised this model, of all people, wants to contact us, but they're really popular right now so let me see what's up."

    show black with dissolve
                
    hide black with dissolve
    
    si "I can't believe they wanted to schedule an interview!"
    
    si "I've definitely got to let Solomon know!"
    
    return
    
label ed2:
    
    "Alright, time to see who's called."
    
    "Hm? This agent called the office so many times?"
    
    si "Let me call them back..."
    
    show black with dissolve
                
    hide black with dissolve
    
    si "...I can't believe that agent was so angry. It's not my fault they had to reschedule and lost the contract with Cufflinks..."
    
    "It makes me wish I'd picked up the phone earlier, but my lunch break is my only relaxed time of the day..."
    
    si "Ah, well... maybe that agency will be over it in the Fall."
    
    si "We might {i}not{/i} be blacklisted if we play our cards right..."
    
    return
    
label ed3:
    
    si "Let me check the caller ID."
    
    "Oh! It's fewer numbers than I thought."
    
    si "Hm..."
    
    si "No answer..."
    
    si "I'll just leave a message for now. Maybe they'll call again tomorrow."
    
    return
    
######################################################

######################################################

label eh1:
    
    si "Hm... this one isn't so bad."
    
    si "These credentials almost seem too good to be true."
    
    si "Wow! A recommendation from {i}that{/i} guy? This person must be some kind of fashion journalism prodigy."
    
    si "Let me read the cover letter..."
    
    show black with dissolve
    
    hide black with dissolve
    
    si "What a well-written cover letter. I think I'll forward it to Solomon."
    
    return
    
label eh2:
    
    si "Alright, Miss..."
    
    si "What does this even say? The handwriting is completely illegible. They definitely should've typed this up."
    
    si "And... wait a second, is that--"
    
    si "What's this this sticky stuff on the back?"
    
    "I flip over the sheet."
    
    "{i}And it's brown?{/i}"
    
    si "Ew! No! Disgusting, I'm sorry. There's a margin of cleanliness and I just--"
    
    si "Rejected!"
    
    return
    
label eh3:
    
    si "Oh, this one's not bad, but I don't think we're looking for someone to fill this position anymore..."
    
    si "Too bad, their portfolio is excellent."
    
    "Hm... but... there {i}is{/i} an art department here..."
    
    "I press the intercom."
    
    si "Mr. Fox?"
    
    f "Ms. West?"
    
    si "Do you mind if I forward one of these applications to the art department head?"
    
    f "Not at all. Just put it in the pile and I'll have Joel deliver it over to them."
    
    si "Great, thank you."
    
    return
    
    
######################################################

######################################################

label ein1:
    
    si "I should ask Joel to make coffee..."
            
    si "Where is he anyway?"
    
    si "Hm... let me email him."
    
    show black with dissolve
    
    hide black with dissolve
    
    si "..."
    
    si "No answer."
    
    si "Too bad, I was looking forward to a cup from him."
    
    scene black with dissolve
    
    return
    
label ein2:
    
    "Maybe Joel will make coffee if I ask him."
    
    si "Let me just see if he's in the kitchen."
    
    scene black with dissolve
    
    scene o_kitchen with pixellate
    
    si "Joel?"
    
    "Hm, he's not in here."
    
    si "Oh, but he made it already! Nice."
    
    "Well, may as well have some."
    
    scene black with dissolve
    
    return
    
label ein3:
    
    "Let me just ask Joel if he'll--"
    
    si "Hm? What's this?"
    
    "I have no clue how long this note's been here."
    
    "{i}Simone, there's no more coffee in the office kitchen. I was going to make it but I don't have time to. If you want coffee, the office cafeteria has some.{/i}"
    
    "{i}I'm really, really sorry. From, Joel.{/i}"
    
    "The office cafeteria is on the basement floor... No way am I going all the way down there."
    
    "Guess there's no coffee for Simone today then."
    
    scene black with dissolve
    
    return

######################################################

######################################################

label el1:
    
    si "I wonder what my aunt's doing for dinner tonight..."
    
    si "She usually makes that really good fish fry I like..."
    
    "I shoot out a quick text."
    
    si "Auntie, what're you making tonight...?"
    
    show black with dissolve
    
    hide black with dissolve
    
    #text message sound
    
    "I'm rewarded with a text-- specifically a picture of a golden dinner I won't be eating."
    
    "I'm so hungry..."
    
    "I should grab"
    
    return
    
label el2:
    
    "I wonder if I should go bowling tonight after work."
    
    "I know they sometimes do , and what time they close."
    
    show black with dissolve
    
    hide black with dissolve
    
    "Huh? They're closed for maintenance?"
    
    "Oh, too bad. I thought I finally had time to go."
    
    return
    
label el3:
    
    "Maybe I should just text Trina."
    
    "It's not like she's doing much..."
    
    show black with dissolve
    
    hide black with dissolve
    
    "Hm... I wonder why she's not responding..."
    
    si "Oh, but wait!"
    
    si "I keep forgetting that her phone being broken was the whoole reasm why we're forced to communicate via email anyway."
    
    si "Oh, well."
    
    return
    
######################################################

######################################################

label eim1:
    
    "I wonder if I can find a cuter mousepad..."
    
    "Trina says I have a mousepad addiction, but I only own maybe fifteen or twenty of them."
    
    "That's hardly an addiction."
    
    "I should just look online for one that would compliment my desk really well."
    
    si "Maybe something floral?"
    
    return
    
label eim2:
    
    "Maybe I should think about getting a desk plant."
    
    si "But where would I put it? How would I water it?"
    
    si "Hm..."
    
    si "Winter's coming, too... It might be hard to find a good seasonal one."
    
    si "Maybe I can do it another time."
    
    return
    
label eim3:

    "Hm... it would be nice if I could spruce up my desk with some flowers..."
    
    "But for all I knew, one of my co-workers could have an allergy or something."
    
    "Hm... if it's Milo... Kind of more reason to work here and put them up."
    
    "Inwardly, I can imagine my mother glaring at me. I mutter under my breath."
    
    si "Yeah, yeah, don't be petty. I know."
    
    return