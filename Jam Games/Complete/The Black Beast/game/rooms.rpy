# Rooms #

# Nue ###############################################
label nueroom:
    hide screen walkaround
    if gotNuemask:
        show bg nuemask
    else:
        show bg nue
    if nuesadface:
        show nue sad at chright
    else:
        show nue at chright
    
    if mcramhorns:
        show mc horns at mcleft
    if mctail:
        show mc tail at mctaileft
    if mcwings:
        show mc wings at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc at mcleft
        
#Chapter1
    if not FirstTimeNue:
        nu "Oh, hello! Welcome back."
        mc "..."
        mc "Welcome back? Have I been here before?"
        nu "Haha, maybe not. But I wouldn't be able to tell, anyway."
        nu "I can't remember anything recently. So I just assume I've met everyone!"
        nu "It works out somehow."
        mc "Oh..."
        mc "Why can't you remember?"
        nu "..."
        nu "You know, that is a very good question."
        $renpy.pause(delay=None)
        nu "I haven't the darndest clue!"
        nu "But I think I misplaced something important."
        mc "Do you want it back?"
        nu "Do I want what back?"
        mc "What you've forgotten?"
        nu "Hm..."
        nu "Hmm....."
        nu "Nah."
        $ FirstTimeNue = True
        $ talkedtonue = True
        jump choicesNue
    if Nueignoresyou and not Nuehatesyou:
        "..."

    if brokenmaskNue:
        pass
    else:
        nu "Hey there." 
             
    if Nuesecret and not NuesecretNue:
        show nue sad at chright
        mc "..."
        nu "What do you want?"
        play sound darkmagic
        "I chant the words."
        mc "Give me your tail, Kitsune."
        nu "..."
        nu "Is this going to make you happy?"
        nu "That I cut off one of my tails for you?"
        mc "..."
        nu "..."
        nu "Fine."
        nu "You're a cruel bastard."
        hide nue sad
        show bg nue
        play sound itemtwinkle
        "Got Kitsune Tail"
        $ NuesecretNue = True
        $ Nuetailcut = True
        $ Nuehatesyou = True
        call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_5  
    if MoguhungryNue and not Deislikesbooks and not foodforMogu and not Deishasfood:
        nu "You should talk to Deis."
        nu "Her door has a knocker."
    if Deislikesbooks and not foodforMoguNue and not foodforMogu:
        nu "I bet if you read Deis something, she'll like you more."
        call nueroom_hub from _call_nueroom_hub_4        
    if not foodforMoguNue and foodforMogu and not chap1done:
        nu "Oh look at that! You managed to get food."
        nu "Deis is just not used to new people. But she warms up to them fast."
        $ foodforMoguNue = True
        $ MoguhungryNue = True
        call nueroom_hub from _call_nueroom_hub_6   
    if not FirstTimeNuemask and chap1done:
        nu "I think I figured out what I lost!"
        nu "Do you see my wall?"
        nu "One of my masks is missing."
        nu "I know it looks obvious now, but it's really hard to know you've lost 
        something when you don't even know you've lost it!"
        "{nw}"
        nu "Ah, but I don't even remember what kind of mask it is."
        nu "Will you help me find it?"
        $ FirstTimeNuemask = True   
    if helpNuefindmask and not brokenmask:
        nu "Hope you help me out!"
    if helpMaryfindstory and MarystoryNue and not brokenmask:
        nu "Have you found my mask yet?"
    if brokenmaskNue and not cheerupNue:      
        nu "I'm a little sad."
        if Deistransmutingmask:
            pass
        else:
            jump nueroom_hub
    if cheerupNue and not cheerupNue_seen: 
        show nue at chright  
        nu "Hey..."
        nu "Thanks for going through all that trouble to get my mask."
        nu "..."
        nu "You can keep it... the broken one, I mean."
        nu "It doesn't seem like much but  maybe it will be handy to you one day."
        nu "And if you need help on anything, just ask."
        $ Nueisyourfriend = True
        $ cheerupNue_seen = True
        $ DeistransmutingmaskNue = False        
    if Nueisyourfriend:
        nu "You wanna talk to my masks?"
        nu "They're pretty funny."
        if Deistransmutingmaskdone:
            call choicesNue from _call_choicesNue
        else:
            jump nueroom_hub
    menu choicesNue:
        "Ask about the horn" if not askabouthornsNue and not chap1done:
            mc "Do you know where to find a horn of a dead god?"
            nu "A horn of a what now?"
            nu "Is that a riddle?"
            "..."
            nu "Eh. I don't know anything about that!"
            $ askabouthornsNue = True
            jump choicesNue
        "Ask about Deis" if Deishasfood and not DeishasfoodNue:
            nu "..."
            nu "Oh, I see, so Deis won't give you some, huh?"
            nu "Don't worry about it. She's a nice person."
            nu "It probably won't hurt to get on her good side, though!"
            nu "I heard she likes being read to."
            $ DeishasfoodNue = True
            $ Deislikesbooks = True
            jump choicesNue
        "Ask about food" if not MoguhungryNue and helpMogufindfood:
            nu "Food?"
            nu "Thanks, I'd love some!"
            nu "..."
            mc "..."
            mc "No, it's for Mogu."
            nu "Ohh! I see."
            nu "That can't be that hard. Mogu will eat anything."
            nu "But yeah... I don't have anything to feed him, sorry!"
            nu "..."
            nu "You should talk to Deis. She's one of those paranoid types."
            nu "If there's anyone here who has a stash of food, it would be her."
            nu "I heard she has a whole drawer of band-aids, too."
            nu "...And a hazmat suit."
            $ MoguhungryNue = True
            jump choicesNue
        "Ask about his tail" if FirstTimeNuemask and not askabouttailNue:
            mc "Is there any chance you can give me your tail?"
            show nue sad
            nu "My tail?"
            nu "You want my tail?"
            nu "I can't give it to you! I worked hard to even get three."
            show nue sad
            nu "Besides, you're talking about tail dismemberment here..."
            mc "..."
            "{nw}"                                
            show nue 
            nu "Look, I'll strike you a deal."
            nu "If you help me find my mask, you can keep the mask."
            nu "There might be a reason why it got lost. There's a feeling of sadness that comes with it, I can't explain."
            nu "...But I miss it somehow."
            mc "..."
            mc "Why would you give it to me if you miss it?"
            nu "..."
            show nue sad
            nu "You can miss something and not want it back."
            nu "..."
            show nue
            nu "So, what do you say?"
            menu Nuestailandmask:
                "Help Nue find his mask":
                    if ramhorn:
                        play sound darkmagic
                        "The ram horns are whispering."
                        "Why should I help him?"
                        "It doesn't make any sense."
                        jump Nuestailandmask
                    if didnottakehorn:
                        "Maybe I should follow what the Dark told me to do."
                        jump Nuestailandmask
                    nu "Alright! Thanks!"
                    nu "Where do we even start?"
                    nu "Maybe if we talk to the others, they might have seen it."
                    nu "I'll do some snooping around as well."
                    $ helpNuefindmask = True
                "Refuse, I need his tail.":
                    if unicornhorn:
                        mc "Cutting off a tail seems cruel..."
                        mc "There must be another way."
                        jump Nuestailandmask
                    show nue sad at chright
                    $ nuesadface = True
                    nu "..."
                    nu "Why do you even want it..."
                    nu "You know I can't give it to you."
                    nu "..."
                    $ Nueignoresyou = True
                    $ Youwantatail = True
            $ Nuetail = True 
            $ askabouttailNue = True
            $ FirstTimeNuemask = True
            $ openStardoor = True
            jump choicesNue
        "About Mary's memory" if helpMaryfindstory and not MarystoryNue and not brokenmask:
            nu "Oh you're helping Mary find her memory?"
            nu "Hmm..."
            nu "I don't know anything, sorry!"
            $ MarystoryNue = True
            jump choicesNue
        "Ask for a joke" if findstarjoke and not starjokeNue:
            nu "You want a joke?"
            nu "Huh..."
            nu "....."
            nu "Okay, I have one."
            call nuejoke from _call_nuejoke
            nu "H-Haha... I guess it isn't very funny."
            nu "Actually Mary tells the best jokes!"
            nu "Her deadpan delivery is great!"
            nu "You should ask her!"
            $ Nuehasabadjoke = True
            $ starjokeNue = True
            $ Nuehasastarjoke = True
            $ Marygoodwithjokes = True
            jump choicesNue
       
        "Show Nue the new mask" if Nuenewmask and not gotNuemask:
            nu "..."
            nu "......"
            nu "W-Wow... Where did you you get this mask?"
            nu "It's gorgeous."
            nu "What? It's for me?"
            nu "..."
            nu "No way!"
            $renpy.pause(delay=None)
            nu "..."
            nu "I can't... I can't take it."
            nu "I'd feel bad. You did all the work, after all."
            nu "You earned it."
            $renpy.pause(delay=None)
            nu "You can have the mask. It's yours."
            nu "But you can hang it up here if you want."
            nu "It can make friends with my other masks."
            play sound itemtwinkle
            show bg nuebasemask
            "Got Opaline Mask"
            $ gotNuemask = True
            $ Nueishappy = True
            $ goodpathdone = True
            $ DarkAbandon = True
            jump choicesNue  

        "Show Nue the broken mask" if brokenmask and not brokenmaskNue:
            nu "Oh, hey! You found it!"
            nu "..."
            nu "It's broken?"
            $ nuesadface = True
            show nue sad at chright
            nu "I see..."
            nu "I wonder how..."
            "{nw}"
            nu "Somehow it makes me sad to see it like that."
            nu "Sure, I forgot all about it... But..."
            nu "It's like I lost something I thought I just misplaced..."
            nu "..."
            $ brokenmaskNue = True
            $ brokenmaskEvent = True
            $ deisfacts = False
            jump choicesNue
            
        "Cheer up Nue" if Deistransmutingmask and not Nueisyourfriend:
            call cheerupNue from _call_cheerupNue    
        "That's all":
            jump lbl_mapStart_hallway1
            
      
    hide nue at chright
    hide mc
    hide mc horns
    hide mc tail
    call nueroom_hub from _call_nueroom_hub_17    
    return

label cheerupNue:
    mc "..."
    mc "Hey, do you want to talk?"
    nu "Oh?"
    nu "About what?"
    menu choices_cheerupNue:
        "About the castle" if not FirstTimecastleNue:
            mc "Do you remember anything about this place?"
            nu "..."
            nu "...No."
            nu "But I miss what was."
            mc "..."
            mc "Do you have an idea what this place is exactly?"
            nu "Well, if you ask me--"
            "Nue dropped his voice."
            nu "And I'm sure a lot of people would disagree--"
            nu "--I think we are in somebody's dream."
            mc "What?"
            nu "Somebody is sleeping and they are having a dream."
            mc "Huh?"
            mc "But then--"
            nu "Yeah, yeah, not everyone would like the thought that they are just a figment of someone else's imagination. I don't like it either."
            nu "And even that description is a bit simplistic."
            nu "It's much more complicated than that."
            nu "I believe we are real, but we are also trapped in here, in this place..."
            nu "...In somebody's dream."
            nu "That's my theory, really."
            mc "..."
            $ FirstTimecastleNue = True
            jump choices_cheerupNue
        "About Nue's masks":
            show mc smile
            mc "Tell me about your masks."
            mc "I heard a lot of interesting things about them."
            show nue at chright
            nu "Well, they are a pretty rowdy bunch."
            nu "This one's Lopi. I met him while I was in a mountain training for my first tail."
            nu "That one's Karaga. He just turned up on my doorstep one day, and that one over there is Popo--"
            play sound stargiggle
            $renpy.pause(delay=None)
            show mc
            mc "..!"
            nu "...."
            mc "Was that you?"
            nu "No. It was Jacques. She's quite a prankster."
            mc "..."
            "I narrowed my eyes at Nue. He looked back at me innocently."
            mc "Mary said you make voices with your masks."
            mc "That was you, wasn't it?"
            nu "I swear it wasn't me!"
            mc "..."
            nu "My masks are real!"
            nu "When I put one on, their spirit possesses me, and I become one with my masks."
            mc "..."
            mc "So it {i}is{/i} you."
            nu "No!"
            "Looking at Nue's cheeky smile, I wasn't convinced."
            $ nuesadface = False
            $ cheerupNue = True
            jump nueroom_hub
    jump choicesNue
return

label Nuemasks:
    hide screen walkaround
    if gotNuemask:
        show bg nuemask
    else:
        show bg nue
    if nuesadface:
        show nue sad at chright
    else:
        show nue at chright
    
    if mcramhorns:
        show mc horns at mcleft
    if mctail:
        show mc tail at mctaileft
    if mcwings:
        show mc wings at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc at mcleft
    "I walked up to the wall."
    nu "Don't be shy. They're nice."
    nu "Except for Ido and Gokiboki. They're sorta rude to people they just met."
    show nue angry
    gk "Who are you calling mean, you three-tailed feline?"
    gk "I welcome all manners of lowly creatures to my presence."
    gk "After all, it is the least I could do to uplift their lowly existence!"
    show nue cheeky
    ido "Oh, do shut up, you ugly piece of wood."
    ido "Nobody likes you."
    show nue angryU
    gk "Say that to my face, claymug!"
    show nue cheeky
    ido "You heard me."
    show mc uhm
    mc "..."
    mc "...."
    "Without a doubt, it was just Nue talking with his mouth closed..."
return


# Deis ###############################################
label deisroom:
    hide screen walkaround
    if mcramhorns:
        show mc horns at mcleft
    else:
        show mc at mcleft
        
    if not FirstTimeDeis:
        de "G-Go away!"
        de "Didn't you read the sign?!"
        mc "But I just wanted to {nw}"
        de "There is something wrong going on..."
        de "It's eating this place... devouring us along with it."
        de "I'm not opening this door to anyone!"
        $ FirstTimeDeis = True
        $ talkedtodeis = True

    if not DeisBack and not MaryEvent and MaryclueDeis:
        de "Hmm, what could it be."   
    if killedastar:
        "..."
        call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_7
    if FirstTimeDeis and not Deislikesyou: 
        de "Please stop bothering me."
    if Deishasfood and not chap1done and not bookforDeis:
        de "I don't have anything."
    if YouwantatailDeis:
        de "You're a horrible person." 
        call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_9       

 
    menu choicesDeis:
        "Knowledge?" if Deislikesyou:
            call deisfacts_random_set from _call_deisfacts_random_set
            jump choicesDeis
        "About the castle" if Deislikesyou:
            jump choices_aboutcastleDeis
        "Ask for food" if not MoguhungryDeis and MoguhungryNue and helpMogufindfood:
            mc "..."
            mc "Hey, I know you don't like me but..."
            mc "Do you have anything to eat over there?"
            de "Food?"
            mc "Yes, I'm asking for a friend."
            mc "Do you have some?"
            de "..."
            de "M-Maybe, maybe not."
            de "Depends on who's asking. Are you from around here?"
            mc "My name is [mcname]."
            de "[mcname]?"
            de "I don't recognize you."
            de "You just want to trick me into opening the door, dontcha?"
            de "Well, I'm not going to fall for it!"
            $ Deishasfood = True
            $ MoguhungryDeis = True
            jump choicesDeis
        "Tell a story" if bookforDeis and not lookitsabookDeis:
            mc "Hey..."
            de "W-What? You again?"
            de "Go awa--{nw}"
            mc "I just got this book."
            de "Book?"
            mc "I'd like to read it to you."
            de "..."
            de "...Why?"
            mc "..."
            mc "Stories are only good if shared."
            de "..."
            de "Hmm... I guess..."
            $renpy.pause(delay=None)
            de "Okay..."
            mc "Alright then! I'll start."
            scene bg black with Dissolve(2.0)
            hide screen FrameScreen
            stop music fadeout 3.0
            play music memory fadein 3.0
            nvl clear
            call lucybook from _call_lucybook
            nvl clear
            stop music fadeout 3.0
            show screen FrameScreen with dissolve
            scene bg deisroom
            show mc at mcleft
            $ renpy.music.play("audio/music/hallway.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
            
            $renpy.pause(delay=None)
            de "Hm..."
            mc "..."
            de "That story really resonates with me."
            de "A fear of doing something that will only end to ruin."
            $renpy.pause(delay=None)
            de "O-Oh, sorry... I might be projecting my thoughts on the story."
            de "I'm sure the author meant something else."
            de "..."
            mc "Well that's what stories are for, anyway."
            de "Y-Yeah..."
            $renpy.pause(delay=None)
            de "What do you think about it?"
            menu:
                "I have the same fear":
                    mc "I am afraid of that too..."
                    mc "To know that what I am doing is pointless... or will only hurt me and the people around me."
                    de "..."
                    de "I understand what you mean."
                    $renpy.pause(delay=None)
                "Maybe it means something else":
                    mc "Well, like you said, it might have another interpretation."
                    de "Oh? Like what?"
                    mc "Maybe it was about endings."
                    de "Endings?"
                    mc "The ending was kind of abrupt, wasn't it?"
                    mc "Endings must be tough to write."
                    mc "But any story can end if you give it a bad ending."
                    de "..."
                    "There was a giggle from behind the door."
                    de "Maybe..."
                    de "I didn't think of that."
                    de "You're funny, [mcname]."
                    $renpy.pause(delay=None)
            de "Hey..."
            de "Thanks for reading it to me."
            de "I needed that."
            de "..."
            de "Lately, I've been terrified of something..."
            de "There's this dark shadow looming around the corners and taking things away."
            de "I don't know if anybody else has noticed or if it is all in my head..."
            de "...But then again a lot of things scare me..."
            de "..."
            de "[mcname]..."
            de "You wanted food, right?"
            play sound itemtwinkle
            "Got a cupcake."
            de "Sorry for being rude to you."
            de "My name is Deis."
            de "Come talk to me anytime."
            $ Deislikesyou = True
            $ lookitsabookDeis = True
            $ foodforMogu = True
            call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_11
        "About Deis's tail."  if Youwantatail and not YouwantatailDeis:
            de "M-My tail?"
            de "You want me... to cut off my tail for you...?"
            de "You're gross..."
            $ YouwantatailDeis = True
            jump choicesDeis        
        "About Nue's tail" if not aboutNuetailDeis and Nuetail and not ramhorn:
            de "Huh? About Nue's tail?"
            de "Oh, he's pretty proud of it."
            de "I heard kitsunes only get a tail once they did an amazing feat."
            "{nw}"
            de "I do have a tail... but I don't think it's transferrable."
            $ aboutNuetailDeis = True
            jump choicesDeis        
        "About Nue's mask" if not aboutNuemaskDeis and Nuetail and not ramhorn:
            de "Oh, he's missing a mask?"
            de "That's a shame."
            de "Nue's masks are fun to talk to. You should talk to them when you have the chance."
            $ aboutNuemaskDeis = True
            jump choicesDeis        
        "About Mary's memory" if helpMaryfindstory and not Maryishappy:
            if not MarystoryDeis:
                de "I see. Now you're helping Mary find her memory huh?"
                de "Maybe I can help."
                de "Can you ask Mary for more details?"
                $ DeisknowsMarystory = True
                $ MarystoryDeis = True
                $ DeisasksMaryclue = True
                jump choicesDeis
            if DeisasksMaryclue and not Maryclue:
                de "Have you asked Mary about that clue?"
                jump choicesDeis        
            if Maryclue and not MaryclueDeis:
                de "..."
                de "Buttons... and Flowers..."
                de "A certain smell..."
                de "I'm trying to look around if there's something related to that."
                de "I think I need one more clue."
                $ MaryclueDeis = True
                jump choicesDeis        
            if MaryclueDeis and not Marycluefromstars:
                de "Hm... What could it be?"
                jump choicesDeis        
            if Marycluefromstars and not MarycluefromstarsDeis and MaryclueDeis:
                de "..."
                de "Fairies...?"
                de "Wait..."
                de "That's it!"
                de "Mary talked about this before."
                de "I think I know what will make her remember."
                de "Will you wait? I have to sort through my shelves."
                $ MaryEvent = True
                $ waitingforDeis = True
                $ MarycluefromstarsDeis = True
                $ DeisBack = True
                # $ time = 10
                #$ deis_timer_range = 10
                #$ deis_timer_jump = "lbl_DeisBack"
                #show screen countdown
                jump lbl_mapStart_hallway1   

            if DeisBack and not waitedforDeisseen:
                de "..."
                de "Here it is!"
                de "I finally found it, phew!"
                play sound itemtwinkle
                "Got a bottle of perfume."
                $ foundMarystory = True
                $ Marystorybook = True
                $ waitedforDeisseen = True  
                $ deisfacts = True      
            if foundMarystory and not Maryishappy:
                de "If you give the bottle to Mary, it might remind her of that memory."     
                jump choicesDeis        
        "Ask for a joke" if findstarjoke and not Deishasajoke_seen:
            if not starjokeDeis:
                de "Ohh, a joke?"
                de "I love jokes!"
                de "Let me think of one!"
                $ starjokeDeis = True
                jump choicesDeis        
            if not starsareamused and not starsaregoodmood and not brokenmask:
                call deisjoke_random_set from _call_deisjoke_random_set
                de "No no..."
                de "Oh hey!"
                de "You have to wait a little bit. There's this good one I just can't remember!"
                jump choicesDeis        
            if starsareamused and not Deishasajoke_seen and not starsarehappy and MaryclueDeis:
                de "I got it!"
                de "I have this pretty good joke!"
                de "So a man walks into a seafood store carrying a trout under his arm."
                de "\"Do you make fish cakes?\” he asked."
                de "\“Yes, we do,\” replied the fishmonger."
                de "\"Great!\” said the man. \“It’s his birthday!\”"
                mc "..."
                show mc smile at mcleft
                "I couldn't help but giggle."
                $ Deishasajoke_seen = True
                $ Deishasajoke = True
                jump choicesDeis
        "About Nue's mask" if brokenmask and not gotNuemask:
            if not brokenmaskDeis and not Deistransmutingmask:
                de "..."
                de "The mask is broken?"
                de "That's a shame."
                de "Nue loves his masks."
                if unicornhorn and brokenmaskNue:
                    de "..."
                    de "Hey, do you still have that unicorn horn though?"
                    de "I have an idea."
                    "{nw}"
                    de "You see, I stumbled across a book here, while I was looking for Mary's memory."
                    de "It's called {i}The Beginner's Guide on Transmuting Magical Objects{/i}."
                    de "Most of the pages are still visible."
                    de "If I read through it, maybe I'll be able to create a new mask out of your unicorn horn."
                    de "It'll be my first time trasmuting something, though..."
                    de "What do you say?"
                    menu:
                        "Give unicorn horn."
                        "Yes":
                            "I slid it through the letter slot."
                            de "Thanks! This will do just great."
                            de "Now, wish me luck!"
                            de "I'm going to read up on the book and figure things out."
                            $ unicornhorn = False
                            $ Deistransmutingmask = True
                            $ brokenmaskDeis = True 
                            call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_14
                        "No.": 
                            $ brokenmaskDeis = True 
                            call deisroom_hub from _call_deisroom_hub_4  
                           
                 
            if not Deistransmutingmask and brokenmaskDeis:
                de "Well what do you think?"
                menu:
                    "Give unicorn horn.":      
                        "I slid it through the letter slot."
                        de "Thanks! This will do just great."
                        de "Now, wish me luck!"
                        de "I'm going to read up on the book and figure things out."
                        $ unicornhorn = False
                        $ Deistransmutingmask = True
                        call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_8
                    "No.":
                        call deisroom_hub from _call_deisroom_hub
             
            if Deistransmutingmask and not Morcolikesyou:
                de "It takes a little bit of time to create it."
                de "You should find something else to do."
                jump choicesDeis        
            if Morcolikesyou and FirstTimecastleMary and not Deistransmutingmaskdone:
                de "It's finished!"
                de "Here's the new mask!"
                play sound itemtwinkle
                "Got new mask."
                $ Nuenewmask = True
                $ Deistransmutingmaskdone = True 
                $ deisfacts = True
                jump lbl_mapStart_hallway1  
            if Deistransmutingmaskdone:
                de "I'm sure Nue is going to like it! his new mask"
        "That's all": 
            call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_10
    call deisroom_hub from _call_deisroom_hub_5
    hide mc
    hide mc horns
    hide mc tail
return

label choices_aboutcastleDeis:
    if not FirstTimecastleDeis:
        mc "Hey Deis."
        mc "You told me earlier that something is happening to this place?"
        mc "Can you tell me more?"
        de "..."
        de "Well, it wasn't like this before, I know that much. Even though I have a spotty memory of what it used to be."
        de "I started forgetting things, you see. That was the start. It might not be strange to you, but 
        I have {i}excellent{/i} memory."
        de "Little things like if I had breakfast already, where I put my glasses..."
        de "And then some of the books in my collection started going blank."
        de "The words on the pages faded."
        de "Even now, I have blank books in my shelf, and I can't even remember what they were 
        originally about."
        de "The final straw was when I talked to someone I couldn't remember. I knew I knew them, but 
        couldn't be sure."   
        de "...A reverse of {i}deja vu{/i}, maybe? What's that term..."
        mc "{i}Deja vu{/i} but in reverse?"
        de "Yes... Forgetting something that seems familiar."
        mc "..."
        de "How can I explain..."
        #    de "Every experience felt familiar... but distant, as though I am experiencing something for the very first time, 
        #    but also it felt like I've gone through it already, as if everything was looping."
        de "You know the feeling when you write a word down, and write again, and again, and again?"
        de "At one point, it doesn't look like a word anymore."
        de "It decays into something else..."
        de "A weird combination of symbols and phonemes that used to mean something."
        de "I think that's what's happening to this place."
        mc "..."
        de "You have to help us, [mcname]."
        de "I know you're the only one who can."
        de "You are the first person I talked to that seems different."
        de "Like you can change things."
        mc "Me?"
        de "Yeah..."
        de "I will help you as much as I can."
        de "I think there's still hope, and that's saying a lot for a pessimist like me."
        de "I can still remember some things. I still have a few books intact."
        de "Maybe whatever is happening in this place can still be reversed."
        mc "..."
        mc "But how..."
        mc "What can I do?"
        de "I'll help you with that as well."
        de "I'm an alchemist."
        de "I'll run a few spells and see what comes up. I'm sure whatever's happening is magic related."
        de "The scent of a spell is in the air. It's faint, but I have a good nose."
        mc "..."
        mc "Okay then."
        mc "Thanks a lot."
        de "I should be the one to thank you."
        de "Do your best, [mcname]."
        $ FirstTimecastleDeis = True
        jump deisroom_hub
    if FirstTimecastleDeis:
        de "I'm running some spells right now."
        de "Check back again later!"
        jump deisroom_hub
return
    

label lbl_DeisBack:
    $ DeisBack = True
    call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_16
    
return


# Morcobashi ###########################################
label morcoroom:
    hide screen walkaround
    show bg clockroom
    show morc at chright
    if mcramhorns:
        show mc horns at mcleft
    if mctail:
        show mc tail at mctaileft
    if mcwings:
        show mc wings at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc at mcleft
    if FirstTimeMorco: 
        mor "The clock still hasn't moved."    
    if not FirstTimeMorco:
        mor "..."
        mor "Hello, I didn't notice you there."
        mc "..."
        mor "I'm watching the clock but it hasn't moved at all, as if Time has forgotten this place."
        mor "This world is wasting away."
        mor "With no Time left to lose, we are losing parts of ourselves."
        mor "It is a strange feeling." 
        mor "..."
        mor "Do you have any idea why?"
        mc "Someone told me it was because of a beast."
        mor "A beast?"
        mor "Perhaps... but I can't be sure."
        mor "Then again, I am never sure."
        mor "There are many things I have forgotten recently."
        $renpy.pause(delay=None)
        mor "..."
        mor "That watch you are holding... Can I see it?"
        mc "..."
        mor "It's working."
        mor "But it's moving faster than a normal watch."
        mor "Interesting..."
        mor "All the watches in this place have stopped, you see?"
        mor "Perhaps you have the power to help us."
        mc "Help you? How?"
        mor "By reminding us of the things we have lost."
        $ FirstTimeMorco = True
        $ talkedtomorco = True
    if killedMorco:
        show bg clockroom
        "This room is empty."
    if Nuetailcut:
            "..."   
    if Maryishappy and Nueisyourfriend and not foundMarystoryMorco and not goodpathdone:
        mor "Thanks for helping Mary and Nue find things they've lost."
        mor "It's strange but I am beginning to remember things..."
        mor "Maybe I'll remember how to fly soon."
        $ foundMarystoryMorco = True
        $ Morcolikesyou = True
        
    menu:
        "Ask about the horn" if not Maryknowsweapon and not MorcotellsyouaboutMary:
            mor "A horn of a dead god..."
            mor "I am not good with mythology, I'm afraid."
            mor "Mary is the most knowledgeable about it."
            mor "You can find her at the library upstairs."
            $ Maryknowsweapon = True
            $ MorcotellsyouaboutMary = True
            jump choicesMorco
        "About the puzzle" if not puzzlegameforhornMorco and puzzlegameforhorn and talkedtoMary:
            mor "..."
            mor "Bind thy will to the light?"
            mor "That sounds like a code."
            mor "Usually these puzzles have a key."
            mor "Do you know the key?"
            $renpy.pause(delay=None)
            mor "I see, so the keycode is F E A - - R."
            $renpy.pause(delay=None)
            mor "..."
            mor "......"
            mor "I think I have solved it."
            mor "You see, if you change one letter in the phrase into the letter from the keycode, you get a different 
            message."
            mor "Bind becomes Find. Changing B to F. \"Thy\" becomes \"the\", and so on and so forth."
            mor "Two words are skipped, which are the words \"to\" and \"the\"."
            mor "Putting it all together, you get..."
            mor "\"Find the Wall to the Right.\""
            mor "Is this helpful to you?"
            $ puzzlegameforhornMorco = True
            $ answertohornpuzzle = True
            jump choicesMorco       
        "About tails" if not aboutNuetailMorco and Nuetailcut and not MaryEvent:
            mor "Oh well, I can't give you my tail sorry."
            mor "Tails are very important to beasts."
            mor "To say you want to take it is akin to cutting off a limb."
            $ aboutNuetailMorco = True
            $ YouwantatailMorco = True
            jump choicesMorco
        "About Mary's memory" if helpMaryfindstory and not MarystoryMorco and not foundMarystory:
            mor  "I see, so you are helping Mary find her memory."
            mor "People have been forgetting stuff here in the house."
            $ MarystoryMorco = True
            mor "I wonder if it's connected to the clocks."
            jump choicesMorco
        "Ask for a joke" if findstarjoke and not starjokeMorco and not goodpathdone:
            mor "A joke?"
            mor "I don't know any jokes."
            $ starjokeMorco = True
            jump choicesMorco
        "That's all":
            jump lbl_mapStart_hallway1
            
    if goodpathdone:
        call morco_demo from _call_morco_demo
    if badpathdone:
        call morco_demo_bad from _call_morco_demo_bad
    hide morc 
    hide mc
    hide mc horns
    hide mc tail
    call morcoroom_hub from _call_morcoroom_hub_3

return

# Edelia  ###########################################
label edelia:
    hide screen walkaround
    show ede at chright    
    if mcramhorns:
        show mc horns at mcleft
    if mctail:
        show mc tail at mctaileft
    if mcwings:
        show mc wings at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc at mcleft
    show bg hallway01:
        xpos 0 + (2800/2) - currentLocation
        
    ed "..."
    if waitedforEdeliadone and not lietoMogu and not waitedforEdeliaseen:
        show ede at chright
        show mc at mcleft
        "Edelia is back!"
        "She hands me a book."
        play sound itemtwinkle
        "Got a book."
        $ book = True
        $ bookforDeis = True
        $ waitedforEdeliaseen = True
        call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_17 
    if liedtoMogu:
        mc "..."

    if not FirstTimeEdelia and not ignoreMogu:
        ed "....."
        mc "Hello."
        ed "...."
        mc "Oh, yes. You can't speak."
        "She takes out the wax board."
        ed "..."
        ed "......"
        ed "..."
        "The board reads \"I lost my voice\"."
        mc "I see."
        $ FirstTimeEdelia = True
        
    menu:
        "Ask about the horn" if FirstTimeEdelia and not Edeliahorn:
            mc "Do you know where I can find a horn of a dead god?"
            "The girl shook her head vehemently."
            mc "Is that a no?"
            "She scribbled something on a wax board."
            ed "..."
            ed "....."
            "The wax board read \"Don't\"."
            mc "..."
            mc "Right."
            $ Edeliahorn = True
            jump edelia
        "What book does Deis likes?" if not DeislikesbooksEdelia and Deislikesbooks and FirstTimeEdelia and not Edelialeft:
            "Edelia seems to be thinking of something."
            ed "..."
            "She scribbles on her wax board."
            "The board said \"Wait\"."
            hide ede at chright
            $ DeislikesbooksEdelia = True   
            $ Edelialeft = True
            $ EdeliaPresent = False
            $ time = 10      
            $ ede_timer_range = 10
            $ ede_timer_jump = "waitedforEdelia"
            show screen countdown    
            call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_18   
    hide ede at chright    
    hide mc at mcleft
    hide mc horns
    call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_19 
return    

label waitedforEdelia:
    $ waitedforEdeliadone = True  
    $ Edeliaback = True
    $ EdeliaPresent = True
    hide mogu 
return

# MOGU  ###########################################
label moguroomfirst:
    hide screen walkaround
    show mogu at chright   
    if mcramhorns:
        show mc horns at mcleft
    if mctail:
        show mc tail at mctaileft
    if mcwings:
        show mc wings at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc at mcleft
    show bg hallway01:
        xpos 0 + (2800/2) - currentLocation
        
        
    if (helpMogufindfood or ignoreMogu) and not chap1done:
         mg "Mogu Hungry..."
         mg "My stomach is rumbling..."
    if not DeishasfoodMogu and Deishasfood:
        mg "What? Deis got some food?"
        show mogu blink
        mg "I know she won't give me any, then."
        show mogu
        mg "I ate one of her books one time..."
        mg "It was... I think it was..."
        mg "Ahh! \"The Cats of Armadillo\""
        show mc uhm
        mc "..."
        mc "I'm not sure that's right." 
        show mogu huh
        mg "Tell me about it!"
        show mogu blink
        mg "There wasn't a hint of armadillo at all, {i}or{/i} cats."
        mg "It tasted more like moldy bread and paint--"
        show mogu 
        mg "--With an aftertaste of murder."
        show mogu sad
        mg "*cries*"
        mg "B-But I didn't mean to eat it!"
        mg "I wish I could be friends with her again."
        $ DeishasfoodMogu = True
        
    if Edelialeft and not waitedforEdeliadone and not liedtoMogu:
        mg "Edelia isn't here yet."
        mg "I'm soooo hungry."
        menu:
            "Lie to Mogu to move him.":
                mc "Edelia told me she's waiting for you upstairs."
                mc "She managed to find you some food."
                mg "R-Really?"
                mg "I'll go to her now!"
                $ librarypathclear = True
                $ liedtoMogu = True
                $ lietoMogu = True
                call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_20
            "Do nothing":
                mc "So hungry..."
 
    if not foodforMoguMogu and foodforMogu:
        "I gave Mogu the cupcake."
        show mogu happy
        mg "Ohhh!! This is really yummy!"
        show mogu smile
        mg "I love you!"
        $ Mogulovesyou = True
        mg "I have so much energy now!"
        mg "I'm going to tell the stars all about you, [mcname]!"
        $ librarypathclear = True 
        $ foodforMoguMogu = True
    hide mogu
    hide mc at mcleft
    hide mc horns
    hide mc tail
    call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_21    
return

label moguroom:
    hide screen walkaround
    scene bg starroom
    show mogu at chright
    if mcramhorns:
        show mc horns at mcleft
    if mctail:
        show mc tail at mcleft
    if mcwings:
        show mc wings at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc at mcleft
    if liedtoMogu or Moguhatesyou:
        "..."
    if not FirstTimeMogu and ignoreMogu:
        mg "I'm really hungry. I'm looking for food."
        $ FirstTimeMogu = True  
    if foodforMogu and not FirstTimeMogu:
        show mogu smile at chright
        mg "Thanks for giving me food!"
        mg "You're really nice."
        show mogu at chright
        $renpy.pause(delay=None)
        $ FirstTimeMogu = True  
    if not Moguhatesyou:
        call mogu_random_set1 from _call_mogu_random_set1
    if liedtoMogu and not liedtoMoguseen and not FirstTimestars:
        mg "H-Hey. You told me there was food somewhere but there wasn't."
        mg "You lied to me."
        $ liedtoMoguseen = True
        call moguroom_hub from _call_moguroom_hub_3    
        
    menu choicesMogu:
        "Ask about Mogu's tail" if not aboutNuetailMogu and chap1done and Nuetail and not Moguhatesyou:
            mg "..."
            mg "M-My tail?"
            mg "I don't know about that."
            mg "Big Bro told me a dragon's tail is the pride of a dragon."
            $ aboutNuetailMogu = True
            jump choicesMogu
        "About Nue's mask" if not aboutNuemaskMogu and chap1done and helpNuefindmask and not Moguhatesyou:
            mg "..."
            mg "Nue's mask?"
            mg "I'm pretty sure I didn't eat it."
            mg "I tried to once, but the mask started talking and scolded me."
            mg "It was traumatic."
            $ aboutNuemaskMogu = True
            jump choicesMogu
        "About Mary's memory" if helpMaryfindstory and not MarystoryMogu:
            mg "..."
            mg "Mary's memory?"
            mg "....Hmm..."
            mg "I think she told me about it a long time ago."
            mg "I can't remember what it is about though."
            $ MarystoryMogu = True
            jump choicesMogu
        "Ask about stars" if not FirstTimestars and not starsareamused:
            mg "The stars are really pretty, but they look a little sad."
            mg "I wonder why..."
            mg "I wanna make them laugh though."
            mg "Hmm.."
            mg "You know, stars know a lot of secrets!"
            $ starsaresmart = True
            $ FirstTimestars = True    
        "That's all":
            jump moguroom_hub
    hide mogu
    hide mc at mcleft    
    hide mc horns 
    hide mc tail
    call moguroom_hub from _call_moguroom_hub_4
    return
    
label talktostars:
    hide screen walkaround
    #show bg starroom
    scene bg starroom
    show mogu at chright    
    if mcramhorns:
        show mc horns at mcleft
    if mctail:
        show mc tail at mctaileft
    if mcwings:
        show mc wings at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc at mcleft
    if Moguhatesyou:
        "..."

    if not starsareamused and not starsaregoodmood and not starsarehappy:
        mg "The stars are really pretty, but they look a little sad."
    if starsarehappy:
        show mogu smile at chright
        mg "I think they stars are happy!"
    if starsareamused:
        mg "I think the stars are amused."
    if starsaregoodmood:
        mg "I think the stars are in a good mood."
        
    if Nuehasastarjoke and not NuehasastarjokeMogu:
        mg "..."
        mg "Nue told you a joke?"
        mg "Let's hear it!"
        hide mogu
        hide mc
        "..."
        "....."
        "........"
        show mc at mcleft
        show mogu at chright
        mg "...It isn't very funny."
        "The stars are politely trying to ignore me."
        "Nevertheless, they look amused at my effort."
        $ NuehasastarjokeMogu = True
        $ starsareamused = True
        call moguroom_hub from _call_moguroom_hub_5
    if Deishasajoke and not starjokeDeisMogu: 
        mg "..."
        mg "Deis told you a joke?"
        mg "Let's hear it!"
        hide mogu
        hide mc
        "..."
        "....."
        "........"
        play sound stargiggle
        "The stars giggled."
        play sound itemtwinkle
        "Found stars's happy tears."
        "They whispered a clue about Mary's memory."
        show mc at mcleft
        show mogu at chright
        mg "I think they are saying... \"Fairies\"?"
        mc "I see! Thank you."
        show mogu smile
        mg "Hey [mcname], I think you cheered them up!"
        mg "You should find more jokes!"
        $ starjokeDeisMogu = True
        $ happystartears_c = False
        $ happystartears += 1 
        $ happystartears_count += 1
        $ Marycluefromstars = True
        $ starsaregoodmood = True
        $ starsareamused = False
        $ madestarslaugh = True  
        call moguroom_hub from _call_moguroom_hub_6
    if Maryhasastarjoke and not starjokeMaryMogu:
        mg "..."
        mg "Mary told you a joke?"
        mg "Let's hear it!"
        hide mogu
        hide mc
        "..."
        "....."
        "........"
        "I whisper it to the stars."
        play sound stargiggle
        "The stars laughed!"
        play sound itemtwinkle
        "Found stars's happy tears."
        "They whispered something, a clue about Nue's mask."
        "..."
        show mogu at chright
        show mc at mcleft
        mg "I think they're saying to check the garden."
        show mogu happy
        mg "But what was the joke?"
        mg "I'm so curious now!"
        $ happystartears += 1 
        $ happystartears_count += 1
        $ Nuecluefromstars = True
        $ starsarehappy = True
        $ starsaregoodmood = False
        show mogu smile
        mg "Anyway, here is the key for the garden."
        mg "It's the door beside ours."
        "Mogu gave me the key for the garden."
        play sound itemtwinkle
        "Got Garden Key."
        $renpy.pause(delay=None)
        mg "Hey [mcname], you're really awesome."
        mg "Big bro will like you."
        mg "Come visit me again!"
        $ keytoflowerroom = True 
        $ starjokeMaryMogu = True
        hide mogu
        hide mc
        hide mc horns
        call moguroom_hub from _call_moguroom_hub_7
    if helpNuefindmask or Nuetail:
        if not starscanhelpyoufindstuff:
            mg "Maybe they could help you find what you're looking for,"
            mg "You should make friends with them!"   
            $ starscanhelpyoufindstuff = True
            if not ramhorn:
                if didnottakehorn:
                   pass
                else:             
                    mg "Stars like jokes, you know."
                    mg "If you tell them a couple of good ones, they'll probably help you!"
                    $ findstarjoke = True    
        if not Maryhasastarjoke and Marygoodwithjokes and findstarjoke:
            mg "You should tell them a good joke so they'll help out."
        if (ramhorn or darkunicorn) and aboutNuetailbook and starsaresmart:
            mg "..."
            mg "Uhm... [mcname]"
            mg "I don't think they like what you're holding."
            if ramhorn:
                mg "That... ram horn."
            else:
                mg "That... crystal..."
                mg "What is that?"
            mg "It's making them uncomfortable."
            mg "It makes me feel kinda sick-ish too..."
            mg "You should put it away."
            $renpy.pause(delay=None)
            mc "..."
            mc "So they are afraid of it."
            mc "If I use it and stab one of them--"
            menu:
                "Use weapon":
                    if ramhorn:
                        "I used the ram horn to stab one of the stars."
                    else:
                        "I used the cursed crystal to stab one of the stars."
                    play sound slash
                    show bg starroom with flash
                    show mogu cry at chright
                    "It glimmered and fell to the floor."
                    mg "What are you doing!!"
                    "Mogu started to cry."
                    mg "You killed her!"
                    mc "What's the magic words to Nue's spell?"
                    "The other stars are afraid and hid behind the clouds."
                    play sound darkmagic
                    "I heard one of them whisper the words."
                    "Got Nue's magic words."
                    mg "I hate you! You're horrible!"
                    $ killedastar = True
                    $ Moguhatesyou = True
                    $ Nuesecret = True
                    call lbl_mapStart_hallway2 from _call_lbl_mapStart_hallway2_1
                "Don't do anything.":
                    pass
                    call moguroom_hub from _call_moguroom_hub_8   
    hide mogu
    hide mc
    hide mc horns
    call moguroom_hub from _call_moguroom_hub_9
    return   
    
 # Mary  ###########################################
label maryroom:
    hide screen walkaround
    show bg library:
        xpos 0 + (1808/2) - currentLocation3
    if Maryishappy:
        show mr smile at maryright
    else:
        show mr at maryright   
    if mcramhorns:
        show mc horns at mcleft
    if mctail:
        show mc tail at mctaileft
    if mcwings:
        show mc wings at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc at mcleft
    if not FirstTimeMary:
        mr "Who the heck are you?"
        mc "My name is [mcname]."
        if lietoMogu or ignoreMogu:
            mr "..."
            mr "......"
            mr "I don't like you."
        else:
            mr "...Right."
        $ FirstTimeMary = True
        $ talkedtoMary = True
    if not Maryhatesyou and not chap1done:
        mr "What do you want?"    

    if Maryishappy:
        mr "I remember now..."
    if bookforDeis and not bookforDeisMary and not chap1done:
        $renpy.pause(delay=None)
        mr "Hey, that book you got there."
        mr "I like that book."
        $ bookforDeisMary = True   
    if Maryhatesyou:
        "..."
        mr "Go away."
        mr "Stop talking to me."
    if Maryhatesyou and YouwantatailMary and ramhorn:
        mr "Blah blah blah."
        mr "Just shut up."    
    if Nuetailcut:
        mr "..."
    if didnottakehorn and darkunicorn and not darkunicornMary:
        mr "..."
        mr "W-What did you do..."
        mr "That unicorn horn."
        mr "Y-You..."
        mr "You're terrible!"
        mr "I was wrong about you!"
        mr "Get out!"
        $ Maryhatesyou = True
        $ darkunicornMary = True
        call lbl_mapStart_hallway2 from _call_lbl_mapStart_hallway2_2    
    if Maryhatesyou and Youwantatail and not YouwantatailMary and ramhorn:
        mr "I'm not interested in what you have to say."
        mr "You've proven to me that you only take stuff that will benefit you without regard."
        mr "Like I'm going to help you with anything!"
        mr "So get lost!"
        $ YouwantatailMary = True
        hide mr
        hide mc at mcleft
        call lbl_mapStart_library from _call_lbl_mapStart_library_10    
        
        
    menu choicesMary:
        "About the castle" if Maryishappy:
            jump choices_Maryisyourfriend
        "About Mary's memory" if not Maryishappy :   
            if Maryclue and not foundMarystory:
                mr "It's something fluffy and has a scent..."
                jump choicesMary
            if not helpMaryfindstory and not starjokeNue:
                mr "I'm looking for a very particular memory."    
                jump choicesMary
            if helpMaryfindstory and not Maryishappy:
                mr "Thanks for helping me."
                mr "I'll look around here too."    
                jump choicesMary
            if not askMarylookingfor and not chap1done:
                mc "Are you looking for something?"
                mr "Yeah, it's a memory I have of... {w}something."
                mc "A book in the library?"
                mr "Not exactly."
                mr "Maybe there's a book that will remind me."
                mr "Or not..."
                mr "Maybe if I find the book, I'll remember?"
                mr "Or maybe it's the library itself that reminds me?"
                mr "There's something familiar about it I can't place."
                mc "That's a bit vague."
                mr "..."
                mr "I know..."
                mr "It's like..."
                mr "You know when you think of a word, and you tell yourself \"Oh it sounds like it starts with the letter B!\", but when you finally remember it... It doesn't start with B."
                mr "It starts with F."
                mr "Weird, huh?"
                mc "Not really... Memories are strange like that."
                mr "Yeah."
                $ askMarylookingfor = True
                jump choicesMary
            if helpNuefindmask and chap1done and Maryissad and not helpMaryfindstory:
                mr "It's no use..."
                mr "I can't find it."
                menu:
                    "Help Mary find her memory.":
                        mc "Hey, cheer up."
                        show mc smile
                        mc "If I help you, we might be able to find it."
                        mr "..."
                        mr "R-Really?"
                        mr "You're going to help me?"
                        mc "Sure."
                        mc "I'll look around for it."
                        mr "..."
                        show mr smile
                        mr "Hey [mcname]..."
                        mr "Thanks..."
                        $ helpMaryfindstory = True
                        $ MaryEvent = True
                        $ deisfacts = False
                    "...":
                        "..."           
            if helpNuefindmask and chap1done and not helpMaryfindstory and not ramhorn:      
                mr "Ugh, I really can't find it!"
                mr "I've been looking all day but it's not here!"
                mc "Are you sure you're looking in the right place?"
                mr "I don't know!"
                mr "Maybe it isn't even in the library! Why did I even think it was here?"
                mc "..."
                mr "It's no use..."
                $ Maryissad = True      
                menu:
                    "Help Mary find her memory.":
                        mc "Hey, cheer up."
                        show mc smile
                        mc "If I help you, we might be able to find it."
                        mr "..."
                        mr "R-Really?"
                        mr "You're going to help me?"
                        mc "Sure."
                        mc "I'll look around for it."
                        mr "..."
                        show mr smile
                        mr "Hey [mcname]..."
                        mr "Thanks..."
                        $ helpMaryfindstory = True
                        $ MaryEvent = True
                    "...":
                        "..."
                        jump choicesMary 
                        
                        
        "Ask about the horn." if Maryknowsweapon and not MaryknowsweaponMary:
            "..."
            mc "I was told you know where the horn of a dead god is."
            mr "..."
            mr "....."
            mc "Hey..."
            mc "Are you listening?"
            mr "..."
            mr "I'm busy."
            $ MaryknowsweaponMary = True
            jump choicesMary 
        "Ask about her tail." if Nuetail and not aboutNuetailMary and not ramhorn:
            mr "I don't have much of a tail sorry."
            mr "You ask about weird stuff."
            $ aboutNuetailMary = True
            jump choicesMary 
 
        "Ask about Nue's masks" if helpNuefindmask and not aboutNuemaskMary and not ramhorn:
            mr "Masks?"
            mr "Erhm... Nue's masks are creepy."
            mr "He does this thing where he changes his voices to match the mask."
            mr "And he carries on conversations with them like they're real people."
            mr "Totally bonkers."
            mr "I just stay because I don't want him to feel bad."
            $ aboutNuemaskMary = True
            jump choicesMary 
        "Ask about scroll" if aboutNuetailbook and not NuetailbookMary:
            mr "..."
            mr "Huh?"
            mr "This scroll?"
            mr "I don't know where the other part is."
            if Maryhatesyou:
                mr "And even if I knew, I'm not going to tell you."
            else:
                mr "Why do you need it, anyway?"
                mr "Don't tell me you want to grow a tail!"
            $ NuetailbookMary = True 
            if not Maryhatesyou and NuetailbookMary and not darkunicorn:
                mr "..."
                mr "When I get in a fix, I usually go talk to the stars."
                mr "They know a lot of things."
                mr "Mogu hangs out with them."
            jump choicesMary     
        "Ask for a joke" if findstarjoke and not starjokeMary:
            if starjokeNue and not Maryishappy:
                mr "A joke?"
                mr "I'm not really in the mood to tell a joke."
                jump choicesMary 
            if Maryishappy and not starjokeMary:
                show mr smile
                mr "Hey!"
                mr "Do you still want to hear a joke? Cos I have a pretty good one!"
                mr "..."
                mr "But I can't say it out loud!"
                mr "Come closer and I'll whisper it to you."
                show mc at center
                mr "..."
                mr "....."
                "Mary whispers the joke in my ears."
                show mc smile
                "It's really funny."
                show mc smile at mcleft
                mr "Now, remember!"
                mr "The delivery and the timing is key!"
                show mr
                mr "And try not to laugh at your own joke!"
                mr "It's really tacky."
                $ Maryhasastarjoke = True
                $ starjokeMary = True
                jump lbl_mapStart_library
        "Ask for a clue" if DeisasksMaryclue and not DeisasksMaryclueMary:
            mr "Deis is asking for a clue about my memory?"
            mr "Hm. I dunno."
            mr "It feels fluffy like a dream."
            mr "Something about flowers? Or buttons?"
            mr "There's a certain scent to the memory too."
            mr "I've smelled it in the library so I thought it must be here."
            mc "A smell?"
            mr "...Like somebody's perfume."
            $ DeisasksMaryclueMary = True
            $ Maryclue = True
            jump choicesMary 
        "Show Mary the bottle" if foundMarystory and not foundMarystoryMary:
            "I handed Mary the bottle."
            mr "Oh..."
            mr "This scent..."
            mr "I remember now..."
            scene bg black with Dissolve(2.0)
            hide screen FrameScreen 
            stop music fadeout 3.0
            play music nvlmusic fadein 2.0
            nvl clear
            call marymemory from _call_marymemory
            nvl clear
            stop music fadeout 3.0
            show screen FrameScreen 
            $ renpy.music.play("audio/music/hallway.ogg", loop=True, fadeout=1.0, fadein=2.0, if_changed=True)
            show bg library with dissolve:
                xpos 0 + (1808/2) - currentLocation3
            mr "..."
            $renpy.pause(delay=None)
            show mr smile at maryright
            show mc at mcleft
            mr "Thank you."
            mr "This means a lot to me."
            $ Maryishappy = True
            $ foundMarystoryMary = True
            jump choicesMary 
        "That's all":          
            jump lbl_mapStart_library
        
        
    hide mr
    hide mc at mcleft
    hide mc horns
    hide mc tail
    call lbl_mapStart_library from _call_lbl_mapStart_library_11
    return   

label choices_Maryisyourfriend:
    hide screen walkaround
    show bg library:
        xpos 0 + (1808/2) - currentLocation3
    if Maryishappy:
        show mr smile at maryright
    else:
        show mr at maryright   
    if mcramhorns:
        show mc horns at mcleft
    if mctail:
        show mc tail at mctaileft
    if mcwings:
        show mc wings at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc at mcleft
    if not FirstTimecastleMary:   
        mc "Mary, there's something strange happening in the house."
        show mr
        mr "I know..."
        mr "Time has stopped and everything is broken."
        mr "It's no wonder people are going around forgetting things."
        mc "Do you have any idea why?"
        mr "Hm..."
        mr "I can't remember much about it, but I think it happened yesterday."
        mc "Yesterday?"
        mr "Yeah, but yesterday feels like such a long time ago."
        mr "{i}\"The waning crescent moon ends. The darkness must not return.\"{/i}"
        mr "I remember that from somewhere."
        mr "Somebody is trying to stop the new moon from rising."
        mc "Why?"
        mr "I don't know."
        mc "What do you think we should do?"
        mr "I'm not sure..."
        mr "But when you gave me back my memory, I felt \"free\", like a fog lifted in my mind. I don't know how to describe it."
        mr "I still have a hard time remembering anything from the past."
        mr "The spell is probably still in effect."
        mr "..."
        mr "If I think of anything, I'll let you know."
        $ FirstTimecastleMary = True   
        jump choicesMary
    if FirstTimecastleMary:
        show mr 
        mr "Somebody is trying to stop the new moon from rising."
        jump choicesMary
        
return

label readabookinlibrary:
    scene bg black with dissolve
    hide screen walkaround
    hide screen FrameScreen
    call books_random_set from _call_books_random_set
    if readabook >= 2:
        $ read2books = True
    if read2books and not read2books_seen and Youwantatail: 
        "I read a couple of books."
        "A scroll was tucked into one of them."
        call aboutkitsune from _call_aboutkitsune
        nvl clear
        "The next part of the scroll is torn off."
        "This might be what I'm looking for..."
        "But I need the magic chant."
        $ aboutNuetailbook = True
        $ read2books_seen = True    
    show screen FrameScreen with dissolve
    show bg library:
        xpos 0 + (1808/2) - currentLocation3
    call lbl_mapStart_library from _call_lbl_mapStart_library_12
return
# Flowerroom ########################################

label flowerroom:
    hide screen walkaround
    if FirstTimeflowerroom:
        scene bg flowerroom
        "There is a flower bud in the middle of the garden."
    if not FirstTimeflowerroom:
        scene bg flowerroom_mask
        "I enter a garden."
        "This room is significantly warmer than anywhere I've been."
        "Something is buried here."
        "It's a broken mask."
        play sound itemtwinkle
        scene bg flowerroom
        "Got Broken Mask."
        $ brokenmask = True
        "There's a little plant blooming underneath the mask."  
        $ FirstTimeflowerroom = True
    if wateredtheplant >= 2:
        "The flower seems to be radiating heat and happiness."
        $ wateredtheplanttwice = True
        call lbl_mapStart_hallway2 from _call_lbl_mapStart_hallway2_3
    if happystartears and not wateredtheplanttwice:
        "I have [happystartears_count] more Happy Star tears."
        "Water the plant?"
        menu:
            "Yes":
                if happystartears <= 0:
                    "I don't have anything to water it with."
                else:
                    play sound itemtwinkle
                    "I watered the plant."
                    "The plant looks happy."
                    $ happystartears -= 1
                    $ happystartears_count -= 1
                    $ wateredtheplant += 1
            "No":
                call flowerroom from _call_flowerroom
            "Leave":
                call lbl_mapStart_hallway2 from _call_lbl_mapStart_hallway2_4
    call lbl_mapStart_hallway2 from _call_lbl_mapStart_hallway2_5
return


        
 # Dark  ###########################################
label darkroom: 
    hide screen walkaround
    if mcramhorns:
        scene bg boyhorns
    elif mctail:
        scene bg boytail
    elif mchornstail:
        scene bg boyhornstail
    else:
        scene bg boy
    hide screen FrameScreen
    sh "The clock is ticking, little boy."
    $currenttime = GetTime()
    sh "The time is: [currenttime]"
    if MaryknowsweaponMary and firstmission:
        sh "You are asking me what a dead god's horn is?"
        sh "It is imbibed with powerful magic, the only item that can strike down the beast."
        $renpy.pause(delay=None)
        sh "Are you having doubts now?"
        sh "I told you it's not going to be easy."
        sh "Be brave."
    if unicornhorn and FirstTimecastleDeis and not chap1done:
        sh "What is this?"
        sh "This is not a weapon!"
        sh "This is nothing but a glorified rock!"
        sh "This is useless and you've already wasted so much time!"
        sh "Are you even serious about your quest?"
        mc "..."
        sh "Well?"
        menu:
            "I don't know...":
                mc "I..."
                mc "I don't think it's right..."
                mc "I don't feel good doing this."
                sh "Didn't I tell you that it's not going to be easy?"
                sh "When you have a goal, there will be decisions you have to make for the greater good."
                sh "Those decisions are hard, but will lead you to progress."
                sh "So stop hem and hawing and get on with it."
                mc "..."
                $ doubtedDark = True
            "Yes.":
                mc "Yes..."
                sh "Good! Just so we're clear!"
                $CurrentRoute = 'bad'
        sh "Well... What's done is done."
        sh "Just don't falter from now on."
        $renpy.pause(delay=None) 
        sh "The second item belongs to a rascally creature, the kitsune."
        sh "Its tail grants the weilder the ability to speed and slow down Time itself."
        sh "We need it to lift the spell consuming this place."
        sh "Find me the tail and come back."      
        mc "..."
        scene bg black with dissolve 
        $ chap1done = True
        $ EdeliaPresent = False
        $ firstmission = False
        call chap2 from _call_chap2
    if didnottakehorn and Youwantatail and starscanhelpyoufindstuff and not darkunicorn_done:
        sh "See what happens when you do not follow my commands?"
        sh "Now you're stuck."
        sh "Don't worry, I will help you."
        sh "Give me that unicorn horn."
        "I dropped the unicorn horn."
        "The white stone glittered in the dark."
        "Suddenly, the shadows fused with it."
        play sound darkmagic
        "The unicorn horn changed into a hard, black crystal."
        play sound itemtwinkle
        $ darkunicorn = True
        "Got Cursed Unicorn Horn."
        sh "That will suffice as replacement."
        sh "Now go and fulfill your quest."
        $ darkunicorn_done = True
    if ramhorn and not chap1done:
        sh "Ahh... Excellent."
        sh "Isn't it beautiful?"
        sh "The ridges of the horn are filled with magic and sorrow."
        sh "Every crack follows the story from the day Time was born."
        sh "This is a wonderful weapon!"
        sh "You did a good job, [mcname]!"
        sh "I have a reward for you."
        play sound itemtwinkle
        show bg boyhorns
        "Received Horns"
        sh "We can't celebrate yet, though."
        sh "There is still work to be done."
        $renpy.pause(delay=None)
        sh "The second item belongs to a rascally creature, the kitsune."
        sh "Its tail grants the weilder the ability to speed and slow down Time itself."
        sh "We need it to lift the spell consuming this place."
        sh "Find me the tail and come back."  
        $ CurrentRoute = 'bad'
        $ mcramhorns = True
        $ chap1done = True
        $ firstmission = False
        $ EdeliaPresent = False
        call chap2 from _call_chap2_1
    if helpNuefindmask:
        sh "Are you done with your quest yet?"
        sh "Don't waste time!"
    if Youwantatail and not Nuetailcut:
        sh "Find me a Kitsune tail."
    if killedastar and not killedastarDark:
        sh "When you embark on a quest, there will always be sacrifices."
        sh "There will be damage. There will be broken hearts."
        sh "Even your own..."
        sh "You will question if the path you are in is the right path."
        sh "But who is to say?"
        sh "Maybe the end {i}does{/i} justify the means?"
        $ killedastarDark = True
        call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_24
    if Nuetailcut and not NuetailcutDark:
        sh "Excellent work."
        sh "This kitsune tail is perfect."
        sh "You have done well, little knight."
        sh "I have a gift for you."
        play sound itemtwinkle
        if ramhorn:
            $ mcramhorns = False
            show bg boyhornstail
            $ mchornstail = True
        if darkunicorn:
            $ mchorns = False
            show bg boytail
            $ mctail = True 
        "Received a Tail."
        if beatTimer:
            sh "You have proven that you are a capable and focused warrior."
            sh "I am proud of you."
        $ renpy.pause(delay=None)
        sh "Just one more item, brave one."
        sh "Get me the wings of a gryphon."
        sh "And then we can finally kill the beast."
        $ NuetailcutDark = True
        $ chap2done = True
        $ badpathdone = True

        hide screen pocketwatch
        stop music fadeout 5.0
    call lbl_mapStart_hallway1 from _call_lbl_mapStart_hallway1_25
    
return

