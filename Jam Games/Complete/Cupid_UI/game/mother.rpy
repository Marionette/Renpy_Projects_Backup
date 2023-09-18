#MOTHER CHOICES#

############# INTRO
label motherfirst:
    menu:
        "Haven't you learned your lesson, idiot?!":
            show rr dep
            m "You truly are an idiot."
            m "Haven't you learned your lesson?"
            m "You are injured because of your own doing."
            m "And you dare tempt fate again?"
            u "..."
            show rr sad
            u "I'm sorry, Mother..."
            u "I just thought it better to eat and sleep first before I left."
            show rr dep
            u  "Please don't be angry."
            $ badmom = True
            $ meanmom += 1
            $ meanmomcount = 1
            $ cmom += 1
            $ cmomcount = 1
            $ achievement.grant("Angry Start")
            $achievement.Sync()
            menu:
                "Then stop your disobedience!":
                    m "If you do not want me to be angry, then don't give me a reason to be!"
                    m "Haven't I told you, time and again, that the world is full of beasts?"
                    show rr sadclose
                    m "If only you were not like {i}this{/i}."
                    m "You saw the way that priest looked at you, didn't you?"
                    u "..."
                    m "And still, you insist on staying."
                    m "Where is your head?"
                    u "..."
                    show rr dep
                    u "I understand."
                    u "I shall leave at once."
                    $ meanmom += 1
                    $ meanmomcount = 2
                    $ badmom = True
                    $ cmom += 1
                    $ cmomcount = 2
                    return
                "I only want you to be safe, dearest.":
                    show rr dep
                    m "I only want what is best for you, child."
                    m "Do you believe that?"
                    u "Y-Yes..."
                    m "You saw the way that priest looked at you, didn't you?"
                    show rr sadclose
                    u "..."
                    m "And still, you insist on staying."
                    show rr dep
                    m "Where is your head?"
                    u "..."
                    m "So, follow my words, that is final."
                    m "Flee and never look back."
                    show rr sadclose
                    u "..."
                    show rr dep
                    u "Yes, Mother."
                    u "I understand. I shall leave at once."
                    $ mmom += 1
                    $ mmomcount = 2
                    return

        "I fear for your safety":
            m "Child, follow Mother's words and leave."
            m "You saw the look in his eyes, didn't you?"
            show rr sadclose
            u "..."
            m "You cannot stay here."
            m "Even a man of God can stain you with the filthiest colors."
            show rr dep
            u "..."
            m "Be a good girl and follow Mother's words."
            u "But..."
            show rr sad
            u "It is cold outside, Mother."
            u "The rain has not let up."
            u "Can't I stay?"
            $ mmom += 1
            $ mmomcount = 1
            $ achievement.grant("Mother's Intuition")
            $achievement.Sync()
            menu:
                "Alright.":
                    show rr dep
                    m "I suppose you can."
                    m "But you must be wary of everyone in this church, do you understand?"
                    m "You are so weak, my darling."
                    m "You give my heart so much pain."
                    show rr sadclose
                    u "I-I'm sorry, Mother."
                    show rr dep
                    u "I will try my best to stay out of trouble."
                    $ mmom += 1
                    $ mmomcount = 3
                    return
                "No!":
                    m "You leave now and that is final."
                    m "I will not hear another argument."
                    show rr sadclose
                    u "..."
                    show rr dep
                    u "I-I'm sorry."
                    u "Please don't be angry, Mother."
                    u "I understand. I shall leave at once."
                    $ cmom += 1
                    $ cmomcount = 3
                    return
return

        
label mothersecond:
    menu:
        "This is all your fault.":
            m "Why must you be like this?"
            show rr sadclose
            m "You are a blight to my heart."
            show rr dep
            u "I'm sorry."
            u "...It is..."
            u "It's all my fault."
            $ badmom = True
            
            $ cmom += 1
            $ cmomcount = 4
            return
        "My poor child.":
            m "My stupid little girl."
            show rr dep
            m "Always a blight, aren't you?"
            m "Whatever will you do without me?"
            show rr sadclose
            u "I'm sorry, Mother."
            u "Thank you, for always guiding me."
            show rr dep
            u "It is all my fault."
            
            $ mmom += 1
            $ mmomcount = 4
            return
return

##################### CHAPTER 1
label m01:
    menu:
        "Are you hungry, child?":
            jump m01a
        "We must not linger.":
            jump m01b
           
label m01a:
    m "Are you hungry, my dear?"
    ug "...Yes, Mother."
    m "Don't you worry."
    m "Mother will provide."
    show rv sad at right  
    ug "..."
    m "You do not need those high class foods anyway."
    m "They will upset your stomach."
    ug "..."
    m "Now, we've stayed long enough. Let us leave."
return

label m01b:
    m "We must not linger in this place any longer."
    m "I detest it."
    
return
    

label m02:
    menu:
        "He is the same as everyone.":
            jump m02a
        "I do not care for him.":
            jump m02b
            
label m02a:
    

    m "You really are stupid."
    ug "..."
    m "How many times do I have to tell you."
    m "They are all the same."
    m "Greedy."
    m "Insatiable."
    m "Maybe not for you."
    m "But for something else."
    show rv aww at right  
    ug "But he is a kind man, Mother."
    m "Don't let his kindness fool you!"
    m "Sweetest tongue hides sharpest tooth, child."
    show rv shy at right  
    "She bit her lip."
    m "Why do you even bother with him?"
    $ achievement.grant("Cynical Mother")
    $achievement.Sync()
    $ cynicalmom = True
    call goodpeople from _call_goodpeople
return
    
label m02b:
    show rv shy at right
    m "I do not care for him."
    m "I wish you would stop ogling some man like a common whore."
    ug "I just want to see him, Mother."
    m "What for?"
    m "What good does his presence do you?"
    show rv shy at right  
    ug "I-I..."
    label goodpeople:
        ug "..."
        ug "H-He makes me feel that there are still good people in the world, Mother."
        menu:
            "There are no more good people in the world, child.":
                $ achievement.grant("Cynical Mother")
                $achievement.Sync()
                $ badpeople = True
                $ cynicalmom = True
                m "There are no more good people in the world, child."
                m "The world has run out of them."
                m "All that is left are manipulative souls who appear kind on the outside--"
                m "--Because they need other people to survive."
                m "Ultimately, they only care for themselves."
                label goodperson:
                    show rv huh at right  
                    ug "D-Don't you think I'm a good person, Mother?"
                    menu:
                        "Of course I do!":
                            m "Of course, child! You are special!"
                            m "Haven't I raised you as such?"
                            m "I have tried my best, my dearest."
                            show rv close at right  
                            ug "Yes, mother. You keep me right!"
                            show rv smile at right  
                            ug "I love you!"
                            $ goodperson = True
                            return
                        "Of course not!":
                            show rv shy at right  
                            m "Humans are intristically selfish, including you!"
                            m "Why do you think I take great pains to keep you out of trouble?"
                            m "It's because you are like this."
                            m "This... little monster."
                            ug "I-I'm sorry, Mother."
                            ug "If I have ever caused you any pain, please, forgive me."
                            $ badperson = True
                            $ badmom = True
                            $ meanmom += 1
                            $ meanmomcount = 3
                            return
            "It is hard to say.":
                m "It is hard to say, of course, dear."
                m "We do not know the real intentions of people."
                m "One can hope that real charity exists."
                m "But even good people will always put their needs first."
                m "Even your precious Marquis."
                call goodperson from _call_goodperson
                return
    
return
    
label m03:
    menu:
        "Didn't I tell you to leave?":
            m "Didn't I tell you to leave, insolent child?"
            m "Now you call for me."
            m "Try to deal with this situation yourself."
            m "You have put yourself in this position, anyway."
            m "I hope you learn your lesson!"
        "Didn't I tell you people are cruel?":
            $ cynicalmom = True
            m "Haven't I taught you this, time and again?"
            m "People are cruel."
            m "Now, you see it firsthand."
            
return

####################### CHAPTER 2

label cathbad:
    menu:
        "She was nothing but selfish.":
            m "You fought so hard."
            m "You never used to fight with me."
            m "But now, she killed herself."
            m "Your sacrifice lost in her selfish ways."
        "She led you astray.":
            m "Catherine was a curse."
            m "She drove you to a love I warned you about."
return
        

label m017:
    menu:
        "I am glad she is dead.":
            m "It saved me the trouble of delivering you from her clutches."
            m "She was poison."
            m "I am glad she is gone."
            $ badmom = True
            $ meanmom += 1
            $ meanmomcount = 4
            $ cmom += 1
            $ cmomcount = 5
        "I am glad you are back to me.":
            m "I was so worried about you, darling."
            m "She almost led you astray."
            m "...Away from me!"
            m "Trust in Mother, darling."
            m "I am just glad to have you back to myself."
            $ mmom += 1
            $ mmomcount = 5
            
return            

label m019:
    menu:
        "Remember the fear in Catherine's eyes in her last days?":
            m "You have seen it, haven't you?"
            m "She was mostly hostile."
            m "But sometimes, when her sanity returned, she was afraid."
            m "Afraid of this man!"

        "Look at how he is unperturbed by Catherine's death.":
            m "There is an absence of feeling in him, don't you see?"
            m "It goes beyond the usual apathy of loneliness."
            m "Did he even really love Catherine?"
return  



label m020:
    menu:
        "Justice.":
            m "Start with his guilt, child."
            m "...Then deliver punishment fitting for one so vile." 
            m "He cannot get away with this."
            $ punish = True
            $ justice = True
            $ achievement.grant("Justice Fighter")
            $achievement.Sync()
    
        "Retribution.":
            m "Start with his guilt, child."
            m "Uncover his lies. Crush his mask."
            m "He must pay for everything he has done."
            $ revenge = True
            $ achievement.grant("A Grudge")
            $achievement.Sync()

return

label m021:
    menu:
        "I knew it!":
            m "I knew it. I knew it."
            m "That man...."
            if persistent.origin:
                "Mother laughed inside Rosa's head."
                m "How fate favours me after all these years."
                m "She has lead me to him again."
                m "...But I must be sure."
                m "Either way..."
            m "We must find out how to destroy him."
            if persistent.origin:
                m "This time, I will not fail."
        "We must get to the bottom of this.":
            m "Are you quite alright, my darling?"
            m "Now you see it, too. There is a sinister force at work."
            m "Get up. We have a lot of work to do."
            m "We must find out what he is and stop him."
            
return
        
################### CHAPTER 3

label m04:
    menu:
        "Leave now while he is not looking, child.":
            m "What are you doing just standing there?"
            m "He is going to see you."
            m "Leave now, while you still have the chance."
            r "Alright, Mother, maybe you're right--"
        "Just go in and ignore him, child.":
            m "Why are you so nervous, anyway?"
            m "Just ignore him."
            m "He doesn't seem to notice you."
            $ rgloves = True
return
            
label m05:
    menu:
        "Console her.":
            m "I am always here, my love."
            m "Loss will always hurt."
            m "But you love Mother the best, don't you?"
            r "...Yes, Mother."
            m "Then you are going to be fine."
            m "I will never leave you like Catherine did."
            $ mmom += 1
            $ mmomcount = 6
        "Scold her.":
            m "Instead of staring into space, why not do something useful?"
            r "..."
            m "Find out about that Marquis!"
            r "Please... Mother."
            r "...Not right now."
            $ badmom = True
            $ meanmom += 1
            $ meanmomcount = 5
            
            $ cmom += 1
            $ cmomcount = 6
            menu:
                "How dare you talk back to me!":
                    if persistent.adult:
                        m "Well, aren't you an ungrateful little bitch?"
                    else:
                        m "Well, aren't you an ungrateful little worm?"
                    m "How dare you talk back to me like that!"
                    r "..."
                    r "I'm sorry, Mother"
                    r "I-I am just upset."
                    m "Even in her death, this Catherine still manages to offend me!"
                    m "Good riddance!"
                    r "..."
                    $ achievement.grant("Insensitive")
                    $achievement.Sync()
                    $ badmom = True
                    $ meanmom += 1
                    $ meanmomcount = 6
                    return
                "I'm sorry, dear.":
                    m "I'm sorry, dear."
                    m "Mother is just fretful."
                    r "I understand, Mother."
                    r "...Just a little more time, please?"
                    m "Alright, but we must leave soon."
                    return
return
    
label m06:
    menu:
        "Open it.":
            m "Open that locket."
            m "It is his possession."
            m "I want to use whatever means necessary to bring him down."
            "Rosa fiddled with it, trying to open the lock."
            "She fussed with the pendant for a while, but like Guilleme said, it was stuck."
            r "I'll try again later, Mother."
            r "I'm rather curious about it myself."
            $ openlocket = True
        "Ignore it.":
            m "I loathe that thing."
            "Rosa's brow furrowed at Mother's sudden antagonism towards the locket."
            m "I don't want to accept any gift from that man."
            m "I wish you hadn't taken it."
            m "In any case, just leave it alone."
            r "Yes, Mother."
            "Rosa slipped the necklace into her coat's pocket."
            $ closelocket = True
            $ achievement.grant("Nonchalant")
            $achievement.Sync()
return

################### CHAPTER 4


label gorc:
    menu:
        "Does Guilleme's presence upset you?":
            $ rosajealous = True
            $ rgloves = True
            $ rglove += 1
            $ rglovecount = 1
            m "Of course, why focus on Catherine's performance--"
            m "--when Guilleme is just over there?"
            m "Well, go on then, why don't you approach him?"
            show rf dep
            r "..."
            m "Ask him about his travels! His work!"
            m "Tell him all about the books you've read."
            if persistent.adult:
                m "And then listen to him talk about Catherine as if the girl shits gold."
                $ achievement.grant("Catherine's 24k")
                $achievement.Sync()
            else:
                m "And then listen to him talk about Catherine as if the girl's worth more than gold."
            m "...As usual."
            r "..."
            m "That would be nice, wouldn't it?"
        "Are you worried about Catherine now that he's here?":  
            m "That filthy man, again."
            m "I'm sure Catherine will be {i}pleased{/i}."
            m "Whatever will she think now that her lover is back?"
            show rf dep
            m "I bet she would rather spend all her time with him, as usual."
            m "My poor darling."
            m "Always running after her star."
            m "I wonder how long until she is tired of you constantly tagging along?"
            m "You brag to me that you share everything like sisters."
            m "Does that include Guilleme, too?"
            $ rclove += 1
            $ rclovecount = 1
return
label theatre2:
    menu:
        "It is obvious he is never going to look at you.":
            m "Do you like being so miserable?"
            m "It saddens me to see you like this."
            m "He has eyes only for Catherine."
            m "Must you always impose your presence like a little dog?"
            r "..."
            $ rosajealous = True
            $ rglove += 1
            $ rglovecount = 2
            $ rgloves = True
        "It is obvious she will abandon you.":
            m "She will {i}obviously{/i} abandon you when they get together."
            m "They make such a {i}lovely{/i} pair."
            show rf shyblush  
            "Rosa winced at Mother's voice, as if it were nails grating on a wall."
            m "It is only a matter of time, isn't it?"
            m "What will you do then?"
            show rf dep  
            m "Aren't you tired of being the third wheel?"
            $ rclove += 1
            $ rclovecount = 2
            $ rcloves = True

return

label theatre3:
    menu:
        "Friendships do not last.":
            show rf dep  
            m "Listen to Mother."
            m "Friendships do not last."
            m "You always love so much. You give all of yourself."
            m "I just don't want you to get hurt."
            m "They are not worth the love you give them."
            r "..."
            m "My dear, every relationship is centered around need."
            m "They need you now..."
            $ friends = True
        "Family is more important.":
            show rf dep  
            m "I'm the only one who will care for you forever, darling."
            m "A mother's love will endure."
            m "This bond can never be broken by time or absence."
            m "Family lifts you up."
            m "It saves."
            m "Of course you feel this way. You see them often."
            m "But when you lose touch, you're left with nothing but a collection of strangers."
            m "And believe me, my dear, they {i}will{/i} leave."
            m "They always leave."
            m "You amuse them now..."
            $ family = True
return

label cath:
    menu:
        "She is selfish just like everyone else.":
            m "What did you expect? She's selfish, just like everybody else."
            m "She used you as an experiment, and now that her curiosity is sated, she's done with you."
            m "You don't matter to her. You probably never did."
            m "Which is a good thing, darling."
            m "You see her true face."
            $ cathselfish = True
        "She is probably repulsed by you.":
            m "What did you expect?"
            m "After what you did to her, you little monster!"
            m "Of course she will avoid you like the plague."
return
###################### CHAPTER 6 #####################

label fancyg:
    menu:
        "You fancy him, don't you?":
            m "Or, maybe…"
            "The voice pewtered out into an abrupt, chilly silence."
            "Rosa waited, sweat dripping down her brow."
            m "I knew it."
            m "You fancy him, don't you?"
            if persistent. adult:
                m "YOU FILTHY WHORE!"
            else:
                m "YOU BRAINLESS WORM!"
            r "I-It's not like that, Mother!"
            m "Past and present, rinse and repeat! Always, always, a selfish little girl!"
            "Rosa was horrified."
            r "No, no-- I'm not selfish-- "
            m "A selfish little girl that loves a murderer more than her own mother!"
            $ rglove += 1
            $ rglovecount = 3
            $ rgloves = True
        "You hate him, don't you?":
            m "Look deep into your heart and you will find it, child."
            m "As there is deep love, there is burning hate."
            m "A hate so strong it compels to end a life."
            m "Yes, darling, let it burn in you."
            m "This is fire that consumes the same way."
            m "Channel it. Use it."
            r "...No, please..."
            "Rosa's head began to throb, and a vile sickness spread through her stomach."
            m "He took everything away from you, darling."
            if persistent.origin:
                m "The same way he took everything from me."
            m "He took Catherine."
            m "He will not stop."
            r "..."
            m "He needs to be {i}punished!{/i}"
            
return
label bedside:
    menu:
        "Take the dagger first.":
            m "It might come in handy."
            "Rosa closed her fingers around the dagger's hilt."
            "A sudden feeling of repulsion came over her."
            "She didn't want to hold the dagger any more than she wanted to hold a bloody human tooth."
            "Yet, as Mother said, there might be use for it later."
            scene bg guildrawercloseupdagger
            "She extracted the dagger carefully from the drawer, keeping her eyes bouncing between her prize and the sleeping man."
            "Finally, the dagger was in her hand."
            "There was power in it, she could tell."
            "The sleek blade glinted with a sinister wink."
            "Rosa placed it in her pocket--"
            $ dagger = True
            $ achievement.grant("Bull by the Horns")
            $achievement.Sync()
            return
        "Take the key first.":
            m "Take the key and leave that dagger."
            m "..."
            m "I have a bad feeling about that weapon."
            m "Leave it be."
            "Rosa agreed with Mother."
            "The weapon was as sinister as it was beautiful."
            "She didn't want to touch it."
            scene bg guildrawercloseupkey
            "Rosa took the tiny key into her hand, feeling the cool metal against her palm."
            "She pushed the drawer back--"
            $ takekey = True
            return
            
            

return


################### ROSADECIDES

label m015:
    menu:
        "Do it for the greater good!":
            m "He should be stopped!"
            m "It is the right thing to do!"
            $ justice = True
        "Do it for me!":
            m "You must do it for me!"
            m "For my peace!"
            $ revenge = True
            
return

label m07:
    menu:
        "To destroy him, of course!":
            show rs furiousbig  
            m "Are you really this daft, child?"
            show rs madbig  
            m "He devours the minds of those that love him."
            show rs depbig  
            m "I cannot think of a more disgusting creature."
            show rs madbig  
            m "We must destroy him, it needs to be done."
            m "He needs to pay for the victims of his curse."
            $ revenge = True
            return
        "To stop him from hurting more people.":
            m "He must be stopped."
            m "If he will not stop, there will be more victims in the future."
            m "He has grown in pride and greed."
            m "There is no telling what he will do further."
            m "He is nothing but a monster, a rabid dog that must be put down."
            $ justice = True
            return
    
            
label m08:
    menu:
        "He will never change.":
            m "You cannot change him, child!"
            m "This is his nature."
            m "That kind of creature has no redemption!"
            $ nochange = True
            return

        "He will not listen to you.":
            m "What makes you think he will listen to you?"
            m "He has fed for centuries."
            m "His addiction is his own curse. It controls him."
            return

label killhim:
    menu:
        "Yes, it is.":
            show rs madbig 
            m "Of course it is!"
            m "There is no other choice. It's the only way to stop him."
            m "He is a monster."
            m "Besides, it is what he deserves."
        "Maybe not.":
            m "..."
            m "Maybe not."
            m "But must we risk it?"
            m "He has become haughty and powerful."
            m "Soon enough, this power will drive him mad."
            $ nokillg = True
return
        
label m09:
    menu:
        "So you are throwing all our efforts away?":
            m "The spell is in full effect!"
            m "I cannot allow you to throw away all our efforts!"
            r "It won't be for naught."
            return
        "What do you intend to do?":
            m "The spell cannot be reversed now!"
            m "It is dangerous to leave it unfinished."
            return
            

            
label m014:
    menu:
        "No, you are not!":
            show rs angrybig  
            m "You are not a monster!"
            m "I have raised you, guided you, and loved you enough."
            m "All my sacrifices were for you."
            m "To stop you from turning into something like him."
            show rs depbig  
            m "Oh, I was always afraid."
            show rs madbig  
            m "Always. Always."
            show rs crazysmilebig  
            m "But you are my dear daughter."
            m "He may be a monster."
            show rs flinchbig  
            m "But you are not."
            m "Because of me."
            show rs depbig  
            m "Because of a mother's love for her child."
            return
        "Yes, you are.":
            $ rosamonster = True
            show rs crazysmilebig  
            m "Yes, you are, and it is part of my regret to have ever loved you."
            show rs depbig  
            m "But that is why I am here."
            show rs arousedsmilebig  
            m "To keep you from becoming the monster he is."
            $ badmom = True
            $ meanmom += 1
            $ meanmomcount = 7
            return
            
label m010:
    menu:
        "You are to do no such thing!":
            m "Disobedient, insolent child!"
            m "You are not to do such a thing!"
            
            show rs hmpbig  
            r "And why not?"
            menu:
                "Because I say so!":
                    m "Because I am your mother, and I will not be rebuked!"
                    m "Look at you."
                    m "Ready to defy me, for him!"
                    m "I, who loved you and cared for you all this time!"
                    m "You ingrate!"
                    $ revenge
                    return
                "Because you must do the right thing!":
                    m "He will strike and kill again, child!"
                    m "Listen to me! You cannot let this chance escape us!"
                    m "For all the victims that he had used and thrown away--"
                    r "But if there is a way to redeem him, I want to take it."
                    $ justice = True
                    return
            return
        "Will that even work?!":
            m "What if it doesn't work, child?!"
            m "Agape is a blessing, not a curse."
            m "A monster of his calibre will only shrug it off."
            m "And what will become of you then?"
            m "Please don't do this."
            return


label m011:
    menu:
        "Scream at her.":
            $ badmom = True
            $ meanmom += 1
            $ meanmomcount = 8
            m "You disgusting child!"
            m "After everything I have done for you!"
            m "For everything I have sacrificed, you defy my wishes now?"
            if persistent.origin:
                m "I have waited so long to exact revenge!"
                m "Too long I have carried this hate in my heart!"
                m "His death is the only thing that will free me."
                m "You dare disobey me now that we are this close?!"
            else:
                m "For what?"
                m "For a man like him?"
                m "You know what he has done!"
                cn "Are you not going to avenge me?"
            m "You must avenge me!"
            
            show rs hmpbig  
            r "Revenge?"
            r "Is that really what you want?"
            r "Will that give you the peace you seek?"
            menu revenge:
                "Yes!":
                    m "Of course!"
                    cn "I want him to suffer as much as I have suffered."
                    m "All those years of torment--"
                    cn "My pain during my last moments--"
                    m "I want him to pay--"
                    if persistent.origin:
                        m "He took everything from me!"
                    r "..."
                    if persistent.origin:
                        show rs thinkbig
                        r "Mother."
                        m "..."
                        show rs normbig
                        r "Let me be enough to heal your pain."
                        m "..."
                        r "Revenge will not heal you, Mother."
                        r "Do not let hate consume me, like it consumed you many years ago."
                        m "..."
                        m "I... I cannot accept this!"
                        r "Mother."
                        r "Let go of your hate."
                        m "..."
                        m "N-No..."
                        show rs thinkbig
                        r "..."
                    else:
                        r "I do not think that is what you really want."
                        m "What?"
                        show rs thinkbig
                        r "You are a part of me, Mother."
                        r "You do not want vengeance, just as Catherine and I do not."
                        r "You simply crave punishment."
                        r "You crave atonement."
                        m "...How dare you say that!"
                        r "..."
                    return
                "...I don't know":
                    m "..."
                    m "What else--"
                    r "I do not think revenge is what you want."
                    m "..."
                    show rs thinkbig  
                    if persistent.origin:
                        r "Mother."
                        r "Let me be enough to heal your pain."
                        m "..."
                        r "Revenge will not heal you, Mother."
                        r "Do not let hate consume me, like it consumed you many years ago."
                        m "..."
                    else:  
                        r "You are a part of me, Mother."
                        r "You are me."
                        r "You simply crave punishment."
                        r "You crave atonement."
                        m "..."
                    return

        "Plead.":
            m "M-My darling..."
            m "I-I know you are strong now."
            m "But please..."
            m "Are you not going to avenge me?"
            m "Wouldn't you do that for me...?"
            show rs hmpbig  
            r "Revenge?"
            r "Is it really what you want?"
            r "Will that give you the peace you seek?"
            call revenge from _call_revenge
            m "..."
            r "Is it not true?"
            m "..."
            m "Darling..."
            if persistent.origin:
                m "What will become of me now, without a purpose?"
                r "Mother, you will always be somebody to me."
            else:    
                m "What will become of me now, without my role to guide you?"
                m "Can you really make it on your own?"
                r "Of course, Mother."
            show rs smilebig  
            r "I will still listen to you and love you."
            r "But my mind is clear. I am capable."
            return
            
label m012:
    menu:
        "Why...?":
            m "W-Why are you making an effort to save him?"
            m "After all that he has done--"
            r "Because I am all he has left."
            m "But you have seen what he really is!"
            m "You have seen his true, ugly face--"
            show rs thinkbig
            r "We are all ugly."
            r "I want to believe there is something worth saving in him, as well."
            show rs smilebig 
            r "After all, Mother."
            r "Where would I be if you had not seen beauty in me, too?"
            return
        "You love him, don't you?":
            show rs thinkbig  
            r "..."
            $ rglove += 1
            $ rglovecount = 4
            $ rgloves = True
            return
            
label m013:
    menu:
        "How dare you...":
            m "I don't need your forgiveness..."
            m "H-How dare you..."
            show rs thinkbig
            m "..."
            return
        "I understand...":
            m "I cannot stop you from feeling this way, can I?"
            m "..."
            return

label m016:
    menu:
        "Stop!":
            m "Don't you move!!"
            "But Rosa didn't pay attention her mother's voice this time."
            "She took a step forward."
            m "Don't you take another step!"
            "She lifted her foot once more "
            m "Why are you not listening?!"
            m "You've always listened!"
            m "You've always followed me!"
            m "You've always known I want the best for you!"
            r "..."
            m "Please!"
            "Rosa passed through, as if all those words were nothing but wind."
            r "I love you, Mother."
            r "Goodbye."
            $ silentmom = True

        "S-So be it...":
            m "S-So be it."
            m "Just know that he is powerful and full of pride."
            m "He will not take kindly to being bound by magic."
            r "We can only hope, Mother."
            menu:
                "I don't trust him.":
                    $ knife = True
                    m "Won't you at least find something to defend yourself with?"
                    m "He is quite volatile."
                    m "It would put me at ease if you get yourself a weapon."
                    "Rosa thought for a while."
                    r "That is reasonable enough."
                    if dagger:
                        r "The dagger I found in his room might be enough."
                    else:
                        r "I shall find one."
                "Please, take care of yourself.":
                    m "I am always here in your memories, my dear."
                    m "Whatever happens."
                    m "Please take care of yourself."
                    r "Thank you, Mother."
                    m "My beautiful daughter."
                    menu:
                        "I love you.":
                            $ goodmom = True
                            $ achievement.grant("The Promise")
                            $achievement.Sync()
                        "Goodbye.":
                            $ achievement.grant("Freedom")
                            $achievement.Sync()
                            $ byemom = True

return

############ BAD ENDINGS################

label m023:
    menu:
        "Kill him, child!":
            m "You're letting him get away!"
            m "Kill him, now!"
            call gdies from _call_gdies
        "...":
            r "Mother?!"
            r "Mother, please talk to me!"
            r "Please, I want to hear your voice!"
            menu:
                "...":
                    r "No! Please! Please, talk to me!"
                    r "Don't leave me, Mother!"
                    r "Please!"
                    menu:
                        "...":
                            r "Nooo!"
                            call glives from _call_glives
                            
return

label m024:
    menu:
        "Yes.":
            m "Don't let his silver tongue fool you, child."
            m "You have a purpose!"
            m "This is what you're supposed to do!"
            r "W-Why?"
            menu:
                "To get revenge.":
                    m "Have you forgotten all the horrible things he has done, child?"
                    m "He is a monster and he hurt your Mommy."
                    m "He hurt Catherine."
                    m "He should pay for everything he has done."
                    r "But I don't want to kill anyone, Mother!"
                    "Rosa's grip on Guilleme's neck slackened."
                    "Guilleme coughed at the sudden influx of air."
                    "Rosa stared at her hands in confusion. Tears started to run down her face."
                    r "Why do you want me to kill somebody, Mother?"
                    r "Should I really do it?"
                    r "Why should I be the one to kill him?"
                    menu beca:
                        "Because you must!":
                            m "You are my child and you must do what I say!"
                            r "B-But why?!"
                            r "I never wanted to kill him."
                            r "I already lost Catherine, Mother!"
                            r "M-Mother..."
                            r "He is my last friend."
                            r "I'll have nobody left!"
                            menu:
                                "They are not important.":
                                    m "You imbecile child."
                                    m "Listen to me."
                                    m "You love Mother best, don't you?"
                                    m "Then follow Mother's words!"
                                    r "But I don't want to do this anymore!"
                                    r "I just want to sleep and rest!"
                                    menu:
                                        "You fail me!":
                                            m "You are such an idiot."
                                            m "You have a chance and you're wasting it!"
                                            m "You are so close!!"
                                            r "Why do you always call me dumb?"
                                            r "I'm not dumb!"
                                            menu:
                                                "Argue.":
                                                    m "Unless you get your head straight and do as I say, I will treat you like an idiot."
                                                    r "Shut up!"
                                                    r "I hate you!"
                                                    r "{i}Shut up!{/i}"
                                                    jump lovemom
                                                    return
                                                "...":
                                                    r "M-Mother?"
                                                    jump lovemom
                                                    return
                                        "...":
                                            r "M-Mother?" 
                                            return
                                "...":
                                     r "Mother? I didn't hear what you said!"
                            return
                        "Because you are the only one who can!":
                             m "Child, you have seen his face."
                             m "You have an opportunity to end his existence!"
                             r "But why should I be the one to kill him?"
                             r "Can't somebody else do that?"
                             r "M-Mother... I..."
                             r "I don't want to be a murderer..."
                             r "Please don't make me do it."
                             r "I... I am scared..."
                             menu:
                                 "How dare you disobey me!":
                                     m "I already told you that you must!"
                                     m "I will not stand your disobedience, you ingrate!"
                                     r "Why are you doing this?!"
                                     r "I said I don't want to do it!"
                                     r "Stop making me want to do it!"
                                 "...":
                                     "Rosa frowned."
                                     r "Mother?"
                                     r "Please tell me what to do!"
                                     return
                "To stop him.":
                    m "He is a monster, you stupid child!"
                    m "He has to be stopped from feeding again!"
                    m "Haven't we already discussed this?"
                    r "I am not stupid!"
                    r "Stop calling me stupid!"
                    "Rosa's grip on Guilleme's neck slackened."
                    "Guilleme coughed at the sudden influx of air."
                    "Rosa stared at her hands in confusion. Tears started to run down her face."
                    r "Why do you want me to kill somebody, Mother?"
                    r "Should I really do it?"
                    r "Why should I be the one to kill him?"
                    "Rosa yanked hair from her head."
                    r "Why should I do this?"
                    r "If he killed Catherine, should I kill him too?"
                    r "And then if I killed him, I would have his blood on my hands."
                    r "I live a long life, Mother."
                    r "Can it really wash away?"
                    r "Is killing him the only way?"
                    m "Yes!"
                    r "Then why should I be the one to do it?!"
                    
                    jump beca
                    return

        "...":
            m "..."
            r "Mother? Please answer me."
            r "Tell me why I'm here."
            r "Why did you lead me here?"
            r "Am I really doing the right thing?"
            m "..."
            r "Is he right?"
            r "Do you not love me?"
            r "You are forcing me to become a murderer!"
            jump lovemom

            return
return

label lovemom:
    m "..."
    r "Do you even love me, Mother?"
    menu:
        "Yes.":
            m "Of course I do, child!"
            r "Then why do you force me to kill someone?"
            menu:
                "Because he is a bad man.":
                    m "He is a bad man and must be killed, my dear."
                    m "Do you understand this?"
                    m "It is justice!"
                    r "That is not justice. That is just validation!"
                    r "And wouldn't this make me bad too?"
                    r "Killing somebody would make me worse!"
                    menu:
                        "Of course not!":
                            m "Of course not, child."
                            m "You are not bad!"
                            r "Yes, I am! Killing somebody is bad!"
                            r "Don't patronize me!"
                            r "Who deserves to die?"
                            r "Why should I decide?"
                            r "I don't want to!"
                            r "...Tell me the truth, Mother!"
                            r "Why do you want me to kill somebody?"
                            jump truth
                            return
                        "...":
                            r "Answer me, Mother!"
                            r "Do you think it's fun to be like this?"
                            r "Why are you forcing me to kill somebody?!"
                            menu truth:
                                "Tell the truth":
                                    "Mother laughed in Rosa's head."
                                    m "Because I wanted to see a little blood."
                                    m "I find it entertaining."
                                    r "..."
                                    r "Is this funny to you?"
                                    r "To see lives toyed with?"
                                    r "I thought you loved me!"
                                    menu:
                                        "Tell the truth.":
                                            m "You are nothing to me."
                                            "Rosa sobbed with her knees folded."
                                            r "I hate you!"
                                            "She retreated into a corner of the room and cried."
                                            r "I thought you loved me, Mother..."
                                            r "I have followed all your words all this time."
                                            r "I endured all your horrible words."
                                            r "I loved you even when you hurt me."
                                            r "...What even am I to you?"
                                            menu:
                                                "Tell the truth":
                                                    m "You're nothing to me but a plaything."
                                                    m "I don't love you."
                                                    m "All I need for you to do is to follow my orders."
                                                    m "That is all you are good for."
                                                    r "Why are you doing this to me?"
                                                    r "Why have you led me down this path?!"
                                                    jump finalmom
                                                    return
                                                "...":
                                                    "..."
                                                    r "Why aren't you talking to me anymore?"
                                                    r "Tell me! Why have you led me down this path?"
                                                    r "Answer me!"
                                                    jump finalmom
                                                    return
                                        "...":
                                            m "..."
                                            r "I hate you!"
                                            "Rosa sobbed, her knees giving way underneath her."
                                            "She retreated into a corner of the room and cried."
                                            r "I thought you loved me, Mother..."
                                            r "I have followed all your words all this time."
                                            r "Am I even worth anything to you?"
                                            menu:
                                                "Tell the truth":
                                                    m "You're nothing to me but a plaything."
                                                    m "I don't love you."
                                                    m "All I need for you to do is to follow my orders."
                                                    r "Why are you doing this to me?!"
                                                    "Rosa screamed into the empty room."
                                                    r "Why have you led me down this path?!"
                                                    jump finalmom
                                                    return
                                                "...":
                                                    m "..."
                                                    r "Now, you don't speak?!"
                                                    r "Tell me! Why have you led me down this path?"
                                                    r "Answer me!"
                                                    r "Why won't you talk to me?!"
                                                    r "Are you just going to keep silent?"
                                                    if persistent.adult:
                                                        r "I hate you! You abusive bitch!"
                                                    else:
                                                        r "I hate you from the bottom of my heart!"
                                                    jump finalmom
                                                    return
                                                   
                                "...":
                                    r "Tell me why, Mother!"
                                    r "Answer me!"
                                    r "Why won't you talk to me?!"
                                    r "I knew it from the start!"
                                    r "You are just a bitter, scornful woman, full of spite!"
                                    r "I hate you!"
                                    r "You've abandoned me!"
                                    jump finalmom
                                    return
                "...":
                    m "..."
                    r "Is that it?"
                    r "So you are just going to keep silent?"
                    r "I hate you, Mother!"
                    r "I hate you!"
                    r "You were nothing but a cruel, spiteful bitch!"
                    return
        "...":
            m "..."
            r "Mother, don't you love me anymore?"
            r "I have followed all your commands all this time."
            r "I have obeyed you! I did everything for you!"
            r "Do you even care for me?!"
            jump truth
            return
 
            
return

label silence:
    menu:
        "...":
            m  "..."
            r "Mother?"
            m "..."
            r "Don't do this to me again!"
            r "Talk to me!"
            menu:
                "...":
                    m "..."
                    r "Mother? Where are you?"
                    r "I did what I was told."
                    r "Aren't you proud of me?"
                    menu:
                        "...":
                            m "..."
                            "Rosa burst into tears again."
                            r "Why are you doing this to me, Mother?"
                            r "Don't you know I love you so much?"
                            r "I do all that you ask."
                            r "I am nothing without you, Mother."
                            r "Please talk to me."
                            menu:
                                "...":
                                    m "..."
                                    r "Why are you so cruel to me?!"
                                    r "W-What did I do wrong, Mother?!"
                                    r "Whatever it is, I'll do what you want!"
                                    r "J-Just please..."
                                    r "Please don't torture me like this!"
                                    r "I am afraid of being alone!"
                                    menu:
                                        "...":
                                            m "..."
                                            r "You evil bitch!"
                                            r "Now that you got what you wanted from me, you leave me?!"
                                            r "{i}I hate you!{/i}"
                                            r "Are you happy now?!"
                                            r "Are you satisfied?!"
                                            play sound "sfx/fall.ogg"
                                            "Rosa fell to the floor and sobbed."
                                            r "...Come back!"
                                            menu:
                                                "...":
                                                    m "..."
                                                    r "I-I don't want to be alone, Mother!"
                                                    r "Please come back!"
                                                    return
                                       
return
                       
###############################################################  


label momjournal:
    menu:
        "That's enough.":
            m "You have learned enough."
            m "You know what he is and how to kill him."
            m "There is no more need to read further."
            call reveal from _call_reveal
        "Read more.":
            m "Perhaps there might be more."
            call morejournal from _call_morejournal
return
        

label killsomeone:
    menu:
        "Don't worry, I will guide you.":
            m "Don't you fret, my child."
            show rs flinchbig  
            m "I will be there to guide you."
            m "It is simple, my darling."
            m "Focus on the goal ahead."
        "You've done it before.":
            show rs arousedbig  
            m "What is the matter?"
            show rs crazylaughbig  
            m "Haven't you done it before?"
            show rs shockbig  
            r "That was an accident!"
            show rs crazylaughbig  
            m "No. It is {i}necessary{/i}."
            show rs crazylaughbig 
            m "Accident or not, your hands are already dirty."
            m "What's a little more blood to you?"
            show rs furiouscrybig  
            r "T-That's not true! I--"
            show rs superconfusedcry  
            r "..."
   
return
    
label convince:
    menu:
        "Convince":
            show rs hmpcrybig  
            m "My dear child, don't you see this is the right thing to do?"
            show rs flinchbig  
            r "I-Is it?"
            show rs hmpcrybig  
            m "Yes, my darling."
            m "You have read his journal, have you not?"
            show rs depbig  
            m "He is tired."
            m "We are doing him a favor."        
        "Scold":
            show rs madbig  
            m "So you are more willing to face my wrath rather than obey, is that it?"
             
            m "What is it that you do not understand?"
            m "He cannot live."
            m "You have read his journal."
            m "He is a vile, filthy insect."
            m "He has to perish."
            
return
label shout:
    menu:
        "Believe in Mother, child!":
            show rs hmpcrybig  
            m "Mother knows what is best for you, my darling."
            show rs crazysmilebig  
            m "Do you believe that?"
            show rs flinchbig  
            r "Y-Yes, Mother."
            show rs crazysmilebig  
            m "I have protected you and loved you all these years, haven't I?"
            r "Y-Yes, Mother..."
            show rs madbig  
            m "All my sacrifices were for you, you degenerate."
        "Obey!":
            show rs madbig  
            m "You are such a little monster!"
            m "Selfish."
            m "Inconsiderate!"
            m "Ingrate!"
            
return
label obey:
    menu:
        "Don't cry, honey.":
            m "Shh..."
            show rs superconfusedcry  
            m "My darling."
            m "I know it's hard."
            m "But you love Mother, don't you?"
            r "Y-Yes."
            m "Will you keep Mother happy, darling?"
            r "Y-Yes."
        "Stop it.":
            show rs annoyedhuhbig  
            m "Stop your mewling."
            m "You are not amusing me."
            show rs angryarousedbig  
            m "Do you want to keep my presence with you?"
            m "Do you still want my memory to stay?"
            show rs superconfusedcry  
            r "O-Of course, Mother!"
            r "Please don't leave me!"
            show rs madbig  
            m "Do you love me, my daughter?"
            show rs furiouscrybig  
            r "Y-Yes."

return


