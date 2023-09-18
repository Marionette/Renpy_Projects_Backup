# Rooms #

# Nue ###############################################
label nueroom:
    hide screen walkaround
    show bg nue
    show nue base at chright
    
    if mcramhorns:
        show mc horns at mcleft
    if mctail:
        show mc tail at mctailleft
    if mcwings:
        show mc wings at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc base at mcleft
        
#Chapter1
    if Nuehatesyou:
        "The room is locked from the inside."
        call lbl_mapStart_hallway1 
    if not FirstTimeNue:
        "Oh hello. Haven't seen you around here."
        "Talk to Nue. Everybody in the house has lost something, he says."
        "He doesn't seem bothered though."
        "Ask him about a weapon, and he doesn't have an idea."
        $ FirstTimeNue = True
        $ talkedtonue = True
    else:
        if Nueignoresyou and not Nuehatesyou:
            "..."
        else:
            "Hey there."   
    if Nuesecret and not NuesecretNue:
        "..."
        "You chant the words."
        "Is this gonna make you happy?"
        "That I cut off one of my tails for you?"
        "..."
        "Fine."
        "You're a cruel bastard."
        $ NuesecretNue = True
        $ Nuetailcut = True
        $ Nuehatesyou = True
        call lbl_mapStart_hallway1 
    if MoguhungryNue and not Deislikesbooks and not foodforMogu and not Deishasfood:
        "You should talk to Deis."
        "She always has food."
        call nueroom_hub
    if Deishasfood and not DeishasfoodNue and not Deislikesbooks:
        "She won't give you some?"
        "Hm. You should get on her good side."
        "I heard she likes being read to."
        $ DeishasfoodNue = True
        $ Deislikesbooks = True
        call nueroom_hub 
    if Deislikesbooks and not foodforMoguNue and not foodforMogu:
        "I bet if you read Deis something, she'll like you more."
        call nueroom_hub
    if not MoguhungryNue and Moguhungry and not Deishasfood:
        "Oh you wanna help Mogu out?"
        "I don't have food, sorry!"
        "You should talk to Deis. She's quite a paranoid."
        "She's got a lot of stock."
        $ MoguhungryNue = True
        call nueroom_hub

    if not foodforMoguNue and Moguhungry and foodforMogu and not chap1done:
        "Oh look at that! You managed to get food."
        "Deis is not really bad. She's just really shy."
        $ foodforMoguNue = True
        $ MoguhungryNue = True
        call nueroom_hub
#Chapter2
    if not FirstTimeNuemask and chap1done:
        "Look someone stole my mask."
        "You go to Nue and he is looking for his missing mask."
        "He asks for your help. He will give you what you want."
        "You ask him if he can give you his tail, and he says it is important to him."
        "Then he says that if you find the mask, he'll give it to you."
         
        menu:
            "Take the mask.":
                "Aw that's great!"
                $ helpNuefindmask = True
            "Refuse.":
                "No actually I want your tail."
                "Uhm okay."
                "..."
                $ Nueignoresyou = True
                $ Youwantatail = True
        $ Nuetail = True 
        $ FirstTimeNuemask = True 
        call nueroom_hub
    if helpMaryfindstory and not MarystoryNue:
        "Oh you're helping Mary find her book?"
        "It's probably in a garden or some such, I dun really know."
        $ MarystoryNue = True
        call nueroom_hub
    if findstarjoke and not starjokeNue:
        "You want a joke?"
        "Huh..."
        "Okay, I have one."
        call nuejoke
        "... It isn't very funny."
        "Ahh well.. Sorry! Actually Mary tells the best jokes."
        "She has such deadpan face it fits really well!"
        "You should ask her!"
        $ Nuehasabadjoke = True
        $ starjokeNue = True
        $ Nuehasastarjoke = True
        $ Marygoodwithjokes = True
        call nueroom_hub
    if helpNuefindmask and not brokenmaskNue:
        "Hope you help me out!"
        call nueroom_hub
    if helpMaryfindstory and MarystoryNue and not brokenmask:
        "Did you find my mask yet?"
        call nueroom_hub
    if brokenmask and not brokenmaskNue:
        "Oh..."
        "You found it."
        "It's broken?"
        "I wonder how..."
        "Somehow it makes me sort of sad."
        "Oh well... it can't be helped."
        $ brokenmaskNue = True
        call nueroom_hub
    if Deistransmutingmask and not DeistransmutingmaskNue and not Nuetalkingtoyou:
        "Talks about the house a little bit."
        "Talks about what masks are to him."
        "Talk to him more. like 5x"
        $ Nueisyourfriend = True
        $ DeistransmutingmaskNue = False
        $ Nuetalkingtoyou = True
        call nueroom_hub
    if brokenmask and not Deistransmutingmaskdone and brokenmaskNue:
        "I'm a little sad."
        call nueroom_hub
    if Nueisyourfriend:
        "You wanna talk to my masks?"
        "They're pretty funny."
        call nueroom_hub
    if Nuenewmask and not NuenewmaskNue:
        "Shows new mask."
        "Oh wow..."
        "Is that for me? It's really gorgeous tho"
        "I feel bad keeping it."
        "OKay, thanks! You're great!"
        $ Nueishappy = True
        $ goodpathdone = True
        call nueroom_hub
    hide nue base at chright
    hide mc base at mcright
    hide mc horns
    hide mctail
    call nueroom_hub    
    return

# Deis ###############################################
label deisroom:
    hide screen walkaround
    if mcramhorns:
        show mc horns at mcleft
    if mctail:
        show mc tail at mctailleft
    if mcwings:
        show mc wings at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc base at mcleft
        
    if not FirstTimeDeis:
        "Go away!"
        $ FirstTimeDeis = True
        $ talkedtodeis = True
        call lbl_mapStart_hallway1
    else:
        if Deislikesyou:
            pass
            if not starjokeDeis or Deishasajoke or foundMarystory or not Maryclue:
                call deisfacts_random_set
            if starjokeDeis and not starsareamused and not starsaregoodmood:
                call deisjoke_random_set
                "No no..."
                "Oh hey!"
                "You have to wait a little bit. There's this good one I just can't remember!"
            if MarystoryDeis and not foundMarystory and MarycluefromstarsDeis:
                "Hmm what could it be."   
            if brokenmaskDeis:
                if Deistransmutingmask and not Nueisyourfriend:
                    "It takes a little bit of time to create it."
                    "You should find something else to do."
                else:
                    if not Deistransmutingmask:
                        "Well what do you think?"
                        menu:
                            "Give unicorn horn.":
                                "You slid it under the door."
                                "She does a little magic."
                                "It might take a little bit."
                                $ unicornhorn = False
                                $ Deistransmutingmask = True
                            "No.":
                                call deisroom_hub
                if Deistransmutingmask and Nueisyourfriend and not Deistransmutingmaskdone:
                    "It's finished!"
                    "Here's the new mask!"
                    "Got new mask."
                    $ Nuenewmask = True
                    $ Deistransmutingmaskdone = True 
        else:
            if killedastar:
                "..."
                call lbl_mapStart_hallway1
            else:
                "You again!"
                "I told you to scram!"
                if Deishasfood and not chap1done:
                    "I'm not givng you any food!"
                if chap1done and ramhorn and not YouwantatailDeis:
                    "Stop talking to me."
                if YouwantatailDeis:
                    "You're a horrible person." 
    if Youwantatail and not YouwantatailDeis:
        "My tail?"
        "You're gross. Stop talking to me."
        $ YouwantatailDeis = True
    if not MoguhungryDeis and MoguhungryNue and Moguhungry and not lietoMogu:
        "Do you have food for mogu?"
        "Hah! Like I'll give you anything!"
        $ Deishasfood = True
        $ MoguhungryDeis = True
    
    if bookforDeis and not lookitsabookDeis:
        "Shall I read to you Deis?"
        "Hmm... i dunno."
        "Read story."
        "That was pretty good."
        "Well, okay. You seem like a good guy."
        "I'll give you this in exchange."
        "Got Food."
        $ Deislikesyou = True
        $ lookitsabookDeis = True
        $ foodforMogu = True
        call lbl_mapStart_hallway1
    if not aboutNuetailDeis and Nuetail and not ramhorn:
        "Huh? About Nue's tail?"
        "He's pretty proud of it."
        "Do you have a tail? Can I have it?"
        "No! What a horrible thing to say!"
        $ aboutNuetailDeis = True
        call deisroom_hub
    if not aboutNuemaskDeis and Nuetail and not ramhorn and aboutNuetailDeis:
        "Oh, he's missing a mask?"
        "Hm I dunno where it is."
        $ aboutNuemaskDeis = True
        call deisroom_hub
    if helpMaryfindstory and not MarystoryDeis and aboutNuemaskDeis:
        "Oh I see. Now you're helping Mary find her storybook huh?"
        "Only talks if you talk to her 5x or more."
        "I might have a clue about it. Can you ask Mary for details?"
        $ DeisknowsMarystory = True
        $ MarystoryDeis = True
        $ DeisasksMaryclue = True
        call deisroom_hub
    if Maryclue and not MaryclueDeis:
        "Something fluffy, I see."
        "I'll look around for anything."
        "It's still missing something."
        $ MaryclueDeis = True
        call lbl_mapStart_hallway1
    if findstarjoke and not starjokeDeis and not starsareamused and MaryclueDeis:
        "Ohh, a joke?"
        "I love jokes!"
        "Let me think of a joke!"
        $ starjokeDeis = True
    if starsareamused and not Deishasajoke_seen and not starsarehappy:
        "I got it!"
        "I have this pretty good joke!"
        "Tells joke."
        "It's pretty funny."
        $ Deishasajoke_seen = True
        $ Deishasajoke = True
    if Marycluefromstars and not MarycluefromstarsDeis and MaryclueDeis and Maryclue:
        "Oh! That's it!"
        "I know that book!"
        "Will you wait? I think I have narrowed it down."
        "I just have sort through a pile."
        $ _time = 10      
        $ deis_timer_range = 10
        $ deis_timer_jump = "waitedforDeis"
        show screen countdown   
        $ MarycluefromstarsDeis = True
    if waitedforDeisdone and not lietoMogu and not waitedforDeisseen:
        "Here the book!"
        "I happen to have a copy here!"
        $ foundMarystory = True
        $ Marystorybook = True
        $ waitedforDeisseen = True   
    if brokenmask and not brokenmaskDeis:
        "Oh... the mask is broken."
        "That's really sad."
        if unicornhorn:
            "Hey, you still have that unicorn horn though?"
            "I know how to transmute items you know?"
            "Maybe I'll be able to make a new mask out of it."
            "What do you say?"
            "Give her unicorn horn."
            menu:
                "Give unicorn horn.":
                    "You slid it under the door."
                    "She does a little magic."
                    "It might take a little bit."
                    $ unicornhorn = False
                    $ Deistransmutingmask = True
                    call lbl_mapStart_hallway01
                "No.":
                    call deisroom_hub
                
        $ brokenmaskDeis = True  
        call deisroom_hub
 
    call lbl_mapStart_hallway1  
    hide mc base
    hide mc horns
    hide mc tail
    return

label waitedforDeis:
    $ waitedforDeisdone = True
    call deisroom
    
return


# Morcobashi ###########################################
label morcoroom:
    hide screen walkaround
    show bg clockroom
    show morc base at chright
    if mcramhorns:
        show mc horns at mcleft
    if mctail:
        show mc tail at mctaileft
    if mcwings:
        show mc wings at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc base at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc base at mcleft
    if not FirstTimeMorco:
        "Morcobashi tells you that the clocks in the house has stopped working."
        "He wondered why this is."
        "He also can't remember how to fly."
        "Ask him about a weapon and he says that Mary might know about it."
        "She's at the library."
        $ Maryknowsweapon = True
        $ FirstTimeMorco = True
        $ talkedtomorco = True
    if not puzzlegameforhornMorco and puzzlegameforhorn and talkedtoMary:
        "Oh I know that puzzle."
        "The answer is XYZ."
        $ puzzlegameforhornMorco = True
        $ answertohornpuzzle = True
    if killedMorco:
        show bg clockroom
        "This room is empty."
    else:
        if Nuetailcut:
            "..."
        else:
            "The clock still hasn't moved."
    if not aboutNuetailMorco and Nuetail or (Youwantatail and not YouwantatailMorco) and not Nuetailcut:
        "Tails are very important to beasts."
        "To say you want to take it is like scalping someone."
        "It's really mean."
        $ aboutNuetailMorco = True
        $ YouwantatailMorco = True
    
    if not aboutNuetailMorco and Nuetail and not Nuetailcut:
        "Oh well, I can't give you my tail sorry."
        $ aboutNuetailMorco = False
    if helpMaryfindstory and not MarystoryMorco and not Nuetailcut:
        "I see, so you are helping Mary find her story."
        "People have been forgetting stuff here in the house."
        $ MarystoryMorco = True
    if helpMaryfindstory and not foundMarystory:
        "I wonder if it's connected to the clocks."
    if foundMarystory and not foundMarystoryMorco:
        "That story is good."
        "Somehow it reminds me too, of what this place once was."
        $ foundMarystoryMorco = True
        
    if findstarjoke and not starjokeMorco:
        "A joke?"
        "I don't really know."
        "Why did the chicken cross the road."
        "Why?"
        "..."
        "...."
        "......."
        $ starjokeMorco = True
    if goodpathdone or badpathdone:
        call morco_demo_end
    hide morc base    
    hide mc base at mcleft
    hide mc horns
    hide mc tail
    call morcoroom_hub

    return
    
label morco_demo_end:
    "Hello."
    "This is the end of the demo."
    
return

# Edelia  ###########################################
label edelia:
    hide screen walkaround
    show ede base at chright    
    if mcramhorns:
        show mc horns at mcleft
    if mctail:
        show mc tail at mctaileft
    if mcwings:
        show mc wings at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc base at mcleft
    show bg hallway01
    "..."
    if waitedforEdeliadone and not lietoMogu and not waitedforEdeliaseen:
        show ede base at chright
        show mc base at mcleft
        "Edelia is back!"
        "If you wait for her, she will give you a book."
        "Gives you a book."
        $ book = True
        $ bookforDeis = True
        $ waitedforEdeliaseen = True
        hide ede base
        call lbl_mapStart_hallway1 
    if not FirstTimeEdelia and not ignoreMogu:
        "....."
        "Hello."
        "...."
        "Oh she can't speak."
        "She takes out paper and pencil."
        "I see, you lost your voice"
        $ FirstTimeEdelia = True
    if not DeislikesbooksEdelia and Deislikesbooks and FirstTimeEdelia and not Edelialeft:
        "Edelia seems to be thinking of something."
        "She tell's you to wait."
        hide ede base at chright
        $ DeislikesbooksEdelia = True   
        $ Edelialeft = True
        $ _time = 10      
        $ ede_timer_range = 10
        $ ede_timer_jump = "waitedforEdelia"
        show screen countdown    
        call lbl_mapStart_hallway1   
    hide ede base at chright    
    hide mc base at mcleft
    hide mc horns
    call lbl_mapStart_hallway1 
return    

label waitedforEdelia:
    $ waitedforEdeliadone = True  
    $ Edeliaback = True
    call lbl_mapStart_hallway1
return

# MOGU  ###########################################
label moguroomfirst:
    hide screen walkaround
    show mogu base at chright   
    if mcramhorns:
        show mc horns at mcleft
    if mctail:
        show mc tail at mctaileft
    if mcwings:
        show mc wings at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc base at mcleft
    show bg hallway01
    if helpMogufindfood and not chap1done and not Moguhungry:
        "When you go out of Morcobashi's room, Mogu is blocking the stairs."
        "He's really hungry."
        "You go back to the other character's room."
        "Talk to Mogu."
        "He's hungry and won't let you pass."
        $ Moguhungry = True
    if (Moguhungry)  or (ignoreMogu) and not chap1done:
        "Mogu Hungry..."
        
    if not DeishasfoodMogu and Deishasfood:
        "What? Deis has got some food?"
        "I know she won't give me any. I ate one of her books."
        "*cries*"
        "I wish I could be friends with her again."
        $ DeishasfoodMogu = True
    if Edelialeft and not waitedforEdeliadone and not liedtoMogu:
        "Edelia isn't here yet."
        "I'm soooo hungry."
        menu:
            "Lie to Mogu to move him.":
                "Oh hey. Edelia told me there's food upstairs."
                "Really?"
                "Mogu leaves."
                $ librarypathclear = True
                $ liedtoMogu = True
                $ lietoMogu = True
                call hallway
            "Do nothing":
                "So hungry..."
 
    if not foodforMoguMogu and foodforMogu:
        "Give food to Mogu"
        "Ohhh!! Thats yummy!"
        "I love you!"
        $ Mogulovesyou = True
        "He moves from his place."    
        $ librarypathclear = True 
        $ foodforMoguMogu = True
    hide mogu base
    hide mc base at mcleft
    hide mc horns
    hide mc tail
    call lbl_mapStart_hallway1    
    
label moguroom:
    hide screen walkaround
    show bg starroom
    show mogu base at chright
    if mcramhorns:
        show mc horns at mctaileft
    if mctail:
        show mc tails at mcleft
    if mcwings:
        show mc wings at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc base at mcleft
    if liedtoMogu or Moguhatesyou:
        "..."
    else:
        if not FirstTimeMogu and ignoreMogu:
            if ignoreMogu:
                "I'm really hungry. I'm looking for food."
            if foodforMogu:
                "Thanks for giving me food!"
                "You're really nice."
            $ FirstTimeMogu = True  
        call mogu_random_set1
    if not aboutNuetailMogu and chap1done and Nuetail and not Moguhatesyou:
        "Do you think I can have your tail?"
        "Oh I don't know about that."
        "Big Brother always told me to take care of my tail."
        $ aboutNuetailMogu = True
    if not aboutNuemaskMogu and chap1done and helpNuefindmask and not Moguhatesyou:
        "Nue's mask?"
        "I'm sure I didn't eat it."
        $ aboutNuemaskMogu = True

    if helpMaryfindstory and not MarystoryMogu:
        "Oh Mary's story?"
        "It's pretty nice. I've read a long while ago."
        "I can't remember what it is though."
        $ MarystoryMogu = True

    # Bad Path
    if liedtoMogu and not liedtoMoguseen and not FirstTimeStars:
        "H-Hey. You told me there was food somewhere but there wasn't."
        "You lied to me."
        $ liedtoMoguseen = True
    hide mogu base
    hide mc base at mcleft    
    hide mc horns 
    hide mc tail
    call moguroom_hub
    return
    
label talktostars:
    hide screen walkaround
    show bg starroom
    show mogu base at chright    
    if mcramhorns:
        show mc horns at mctailleft
    if mctail:
        show mc tails at mcleft
    if mcwings:
        show mc wings at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc base at mcleft
    if chap1done and not Moguhatesyou:      
        if not FirstTimestars and not madestarslaugh:
            "The stars are really pretty, but they look a little sad."
            "I wanna make them laugh though."
            "Hmm.."
            "You know, stars know a lot of secrets!"
            $ starsaresmart = True
            $ FirstTimestars = True
        if not madestarslaugh and FirstTimestars and not starsareamused:
            "The stars are really pretty, but they look a little sad."
        if starsarehappy and FirstTimestars:
            "I think they stars are happy!"
        if starsareamused and FirstTimestars:
            "I think the stars are amused."
        if starsaregoodmood and FirstTimestars:
            "I think the stars are in a good mood."
    if Nuehasastarjoke and not NuehasastarjokeMogu:
        "Okay Nue told me a joke."
        "Let the stars hear it."
        "..."
        "It isn't very funny."
        "The stars are politely trying to ignore you."
        "NEvertheless, they are a little amused."
        $ NuehasastarjokeMogu = True
        $ starsareamused = True
        call moguroom_hub
    if Deishasajoke and not starjokeDeisMogu: 
        "Deis told me a joke."
        "Let the stars hear it."
        "The stars giggle."
        "Found Stars happy tears."
        "They start to talk, and the give a clue about Mary's story."
        "Oh you made them happy! That seems to work!"
        "You should find more jokes!"
        $ starjokeDeisMogu = True
        $ happystartears_c = False
        $ happystartears += 1 
        $ happystartears_count += 1
        $ Marycluefromstars = True
        $ starsaregoodmood = True
        $ starsareamused = False
        $ madestarslaugh = True  
        call moguroom_hub
    if Maryhasastarjoke and not starjokeMaryMogu:
        "Mary told me a joke."
        "You whisper it to the stars"
        "The stars laughed!"
        "Found stars happy tears."
        "They start to talk, and give a clue about Nue's mask."
        "What was the joke?"
        "I'm so curious now!"
        $ happystartears += 1 
        $ happystartears_count += 1
        $ Nuecluefromstars = True
        $ starsarehappy = True
        $ starsaregoodmood = False
        "Mogu gives you the keyfor the flower room."
        "Hey you're a really cool guy. Big brother will like you."
        "Here."
        "Gives you key."
        $ keytoflowerroom = True 
        $ starjokeMaryMogu = True
        call moguroom_hub
    if helpNuefindmask or (chap1done and not Moguhatesyou):
        if not starscanhelpyoufindstuff:
            "Maybe they could help you find what you're looking for,"
            "You should make frends with them!"
            if not ramhorn:
                "We should make them laugh. Stars like jokes."
                $ findstarjoke = True
            $ starscanhelpyoufindstuff = True
        if not Maryhasastarjoke and Marygoodwithjokes:
            "You should tell them a pretty good joke so they'll help out."
        if ramhorn and aboutNuetailbook and starsaresmart:
            "..."
            "I don't think they like what you're holding, [mcname]."
            "It's making them uncomfortable. you should put it away."
            menu:
                "Use ramhorn.":
                    "You use the ramhorn to kill one of the stars."
                    "What are you doing!!"
                    "Mogu starts to cry."
                    $ killedastar = True
                    $ Moguhatesyou = True
                    $ Nuesecret = True
                "Don't do anything.":
                    pass
                    call moguroom_hub   
    hide mogu base
    hide mc base at mcleft    
    hide mc horns
    call moguroom_hub
    return   
    
 # Mary  ###########################################
label maryroom:
    hide screen walkaround
    show bg librarymary
    show mr base at maryright   
    if mcramhorns:
        show mc horns at mcleft
    if mctail:
        show mc tail at mctaileft
    if mcwings:
        show mc wings at mcleft
    if not mcramhorns and not mctail and not mcwings:
        show mc base at mcleft
    if not FirstTimeMary:
        "Hey there."
        "Who the heck are you?"
        if lietoMogu or ignoreMogu:
            "I don't like you."
        "Mary will talk to to you. She has misplaced something but she can't 
        remember what it is. It isn't an item or anything, but a story or a memory
        (parallels to stories or memories), and she's looking at books to remind her."
        $ FirstTimeMary = True
        $ talkedtoMary = True
    if Maryknowsweapon and not MaryknowsweaponMary:
        "she doesn't answer your question about a weapon."
        "You look around and you see a portrait of a ram skull."
        "Mary warns you that it's disrespectful to take things that aren't yours."   
        $ MaryknowsweaponMary = True
    if not helpMaryfindstory and not Maryhatesyou:
        "I'm looking for a very particular memory."
    if helpMaryfindstory and not foundMarystory:
        "Thanks for helping me!"
        "I'll look around here too."
    if Maryishappy:
        "I'm happy I found the book."
        "I'm just looking around to"
        "Random babblings about books."
        call lbl_mapStart_library
    if bookforDeis and bookforDeisMary and not chap1done:
        "Hey there. where'd you get that."
        "hmm that's a pretty good story."
        $ bookforDeisMary = True
        call lbl_mapStart_library
    if Maryhatesyou:
        "..."
        "Go away."
        "Stop talking to me."
    if not aboutNuetailMary and chap1done and not ramhorn and Nuetail:
        "I don't have much of a tail sorry."
        "You ask for weird stuff."
        $ aboutNuetailMary = True
        call lbl_mapStart_library
    if not aboutNuemaskMary and chap1done and not ramhorn and helpNuefindmask:
        "Masks?"
        "Erhm Nue's masks are creepy."
        $ aboutNuemaskMary = True
        call lbl_mapStart_library
    if Maryissad and not helpMaryfindstory and helpNuefindmask and not Youwantatail:
        "It's no use..."
        "I can't find it."
        menu:
            "Help Mary find her storybook.":
                "I'll help you find your story."
                "R-Really?"
                $ helpMaryfindstory = True
            "...":
                "..."      
    if starsaresmart and not Maryissad and Marylikesyou:
          "Ugh, I really can't find it."
          "I'm so upset."
          "Why do I even bother."
          $ Maryissad = True
          menu:
              "Help Mary find her storybook.":
                  "I'll help you find your story."
                  "R-Really?"
                  $ helpMaryfindstory = True
              "...":
                  "..."
                  call lbl_mapStart_library
    if DeisasksMaryclue and not DeisasksMaryclueMary:
        "Deis is asking for a clue?"
        "Hm. I dunno."
        "I really can't remember."
        "I just think there's something fluffy like a cloud."
        "And somehow there's a feeling of longing."
        "I don't think it's a lovestory but something more innocent."
        $ DeisasksMaryclueMary = True
        $ Maryclue = True
        call lbl_mapStart_library
    if findstarjoke and starjokeNue and not foundMarystory:
        "A joke?"
        "I'm not really in the mood to tell a joke."
    if foundMarystory and not foundMarystoryMary:
        "Oh..."
        "Oh!"
        "This is it! This is really the story!"
        "Im really happy! Thank you!"
        $ Maryishappy = True
        $ foundMarystoryMary = True
    if findstarjoke and Maryishappy and not starjokeMary:
        "Okay, I know this really funny joke!"
        "..."
        "Tells joke."
        "But I can't say it out loud!"
        "Whispers joke."
        "You start laughing."
        "It's important that the delivery and timing is good, remember!"
        $ Maryhasastarjoke = True
        $ starjokeMary = True
    if Maryhatesyou and Youwantatail and not YouwantatailMary and ramhorn:
        "I'm not interested in what you have to say."
        "You've proven to me that you only take stuff that will benefit you without 
        regard to anyone else."
        "Like I'm going to help you with anything!"
        "Get away from me!"
        $ YouwantatailMary = True
        hide mr base
        hide mc base at mcleft
        call lbl_mapStart_library
    if Maryhatesyou and YouwantatailMary and ramhorn:
        "Blah blah blah."
        "I'm not interested."
    hide mr base    
    hide mc base at mcleft
    hide mc horns
    hide mc tail
    call lbl_mapStart_library
    return   

label readabookinlibrary:
    scene bg black
    hide screen walkaround
    call books_random_set
    if readabook >= 2:
        $ read2books = True
    if read2books and not read2books_seen: 
        "You read a couple of books."
        "There's one about a kitsune will follow you if you find their buried treasure."
        $ aboutNuetailbook = True
        $ read2books_seen = True    
    call lbl_mapStart_library
return
# Flowerroom ########################################

label flowerroom:
    hide screen walkaround
    if not keytoflowerroom:
        jump lbl_hallway2_locked
    else:
        show bg flowerroom
        "There is a flower bud in the middle of the garden."
    if not FirstTimeflowerroom and keytoflowerroom:
        show bg flowerroom
        "You enter a garden."
        "The room is kind of warm."
        "Something is buried here."
        "It's a broken mask."
        $ brokenmask = True
        "There's a little plant blooming underneath the mask."  
        $ FirstTimeflowerroom = True
        call lbl_mapStart_hallway2

    if wateredtheplant >= 2:
        "The flower seems to be radiating heat and happiness."
        "Clock tick off here."
        $ wateredtheplanttwice = True
        
        call flowerroom
    if happystartears_c and not wateredtheplanttwice:
        "You have [happystartears_count] more Happy Star tears."
        "Water the plant?"
        menu:
            "Yes":
                if happystartears <= 0:
                    "You don't have anything to water it with."
                else:
                    "You watered the plant."
                    "The plant looks happy."
                    $ happystartears -= 1
                    $ happystartears_count -= 1
            "No":
                call flowerroom
            "Leave":
                call lbl_mapStart_hallway2
    call lbl_mapStart_hallway2
return

# Ororo Room ##########################################

label ororoom:
    hide screen walkaround
    show bg ororo
    "This is Ororo's room."
    "Go to Ororo's room and he'll tell you a little bit of what's happening."
    "Edelia is also there, and ponchu."
    "The manticore has stopped time and make the dark angry."
    "By helping the characters remember things and giving things they've lost, you've 
    been diluting his spell."
    "The final challenge is to remind Manticore of his name, which everyone in the house 
    has forgotten."
    "Also, Ororo has chains around his ankles. YOu don't know yet why."
    "They suggest that the stars might have the answer."
    
    call thirdhallway
        
 # Dark  ###########################################
label darkroom: 
    hide screen walkaround
    scene bg black
    hide screen FrameScreen
    if unicornhorn and not chap1done:
        "What is this? Are you even taking this seriously?"
        "This is useless and you've already wasted so much time!"
        "But I give you one more chance! Find me a tail faster than wind!"
        $ chap1done = True
        call chap2
    if ramhorn and not chap1done:
        "Excellent."
        "That is a wonderful weapon!"
        "I have a reward for you."
        "Gives you horns."
        $ mcramhorns = True
        $ chap1done = True
        call chap2
    if helpNuefindmask:
        "You're wasting your time."
    if Youwantatail and not Nuetailcut:
        "Faster. Time is ticking."
        "Find me a Kitsune tail."
    if killedastar and not killedastarDark:
        "Quests are always hard."
        "There are times when you really hate it."
        "But you know you're doing the right thing."
        $ killedastarDark = True
    if goodpathdone and Nueishappy:
        "I don't want to go in there anymore."
        call lbl_mapStart_hallway1    
    if Nuetailcut and not NuetailcutDark:
        "Ahh.. what a beautiful tail."
        "You are a very wonderful knight."
        "I have a gift for you."
        "Gives Tail."
        "Just one more item, brave one."
        "Get me the wings of a gryphon."
        "And then we can finally kill the manticore."
        $ NuetailcutDark = True
        $ chap2done = True
        $ badpathdone = True
        $ mchorns = False
        $ mctail = True
    if killedMorco and not killedMorcoDark:
        "Excellent."
        "These beautiful wings."
        "We just have to find where the manticore hides, my dearest."
        $ killedMorcoDark = True
        $ mctail = False
        $ mcwings = True
        call chap3
    if not killedMorco and killedMorcoDark:
        "Your last task is to find me gryphon wings."
        "Hurry. Time is running out."
    show screen FrameScreen
    call lbl_mapStart_hallway1    
    
label lbl_timerwait:
    "..."
    $currenttime = GetTime()
    "The time is: [currenttime]"
    jump darkroom
return

# Throne Room ############################################
label throneroom:
    #hide screen walkaround
    if not throneroomkey:
        jump lbl_hallway2_locked
    call thirdhallway    
