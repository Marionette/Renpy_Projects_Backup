
  
label lbl_character_gen:
  call lbl_pickName from _call_lbl_pickName
  call lbl_pickGender from _call_lbl_pickGender
  
  
  jump lbl_chapter1_start
  
  return
  
label lbl_pickName:
  python:
    player_name = renpy.input("What is your name?")
    player_name = player_name.strip()

    if not player_name:
      player_name = "MC"
       
    
  "So your name is [player_name]?"
  menu:
      "Yes":
        pass
      "No":
        jump lbl_pickName
        
        
  return
  
label lbl_pickGender:
  python:
    player_gender = renpy.input("Are you Male or Female? ( M or F )")
    player_gender = player_gender.strip()

    if not player_gender:
      player_gender = "M"
  
  if player_gender == "M" or player_gender == "m":
    "So you're Male?"
  elif player_gender == "F" or player_gender == "f":
    "So you're Female?"
  else:
    "You have you pick M or F."
    jump lbl_pickGender
   
    
  menu:
      "Yes":
        if player_gender == "M":
          $player_childStatus = "son"
          $player_siblingStatus = "brother"
          $player_identifierHECaps = "He"
          $player_identifierHE = "he"
          $player_identifierHIM = "him"
          $player_identifierHIS = "his"
        elif player_gender == "F":
          $player_childStatus = "daughter"
          $player_siblingStatus = "sister"
          $player_identifierHECaps = "She"
          $player_identifierHE = "she"
          $player_identifierHIM = "her"
          $player_identifierHIS = "her"
      "No":
        jump lbl_pickGender
        
        
  return
  
label lbl_chapter1_start:
  scene sacred_grove with fade
  "One-hundred and twenty-one years ago, on this day, I was born. [player_name]: [player_childStatus] to Alarad and Laurin, and [player_siblingStatus] to Olin."

  "As with the majority of Lyris, on the day of my birth a tree was planted, one which would grow alongside me as the years, decades and centuries passed."

  "The tree was more than a symbolic gesture, its life was inherently bound to mine – on the day I died, so would the tree."

  "But death was the last thing on my mind as I sat in the sacred grove where my birth tree stood, for both it and I were young and strong and in the prime of our lives."

  "My eyes were closed as I meditated before my birth tree, my sight not needed to smell its familiar scent or hear the gentle rustling of its leaves as the breeze caressed its branches."

  "I felt the warmth of the sun on my face. I listened to the steady susurration of the grass around me and the pleasant singing of nearby birds."

  "I took in a deep breath of crisp morning air and then exhaled slowly. I’d visited this spot regularly since I was a child and it never failed in making me feel content and at peace."

  "But today was bittersweet. Because today, one-hundred and twenty-one years after the day I was born, was the day I came of age."

  "And the coming-of-age tradition upheld by many Lyris families encouraged me to leave home and strike out on my own so that I might find my own path and experience what the world outside had to offer, both good and ill."

  "Although I had of course ventured out into other parts of Lyriathis, I’d never done so alone for any real length of time, and there were still countless places and things I had yet to see."

  "But I was torn, as although the thought of striding out into the big, wide world was a thrilling one, I was simultaneously reluctant to leave the comfort of my home and the family I loved."

  "Part of me wanted today to last forever, for me to remain here in the place where I had grown up, while another part was keen to get out there and see what life might have in store for me."

  "The sound of a fallen twig snapping somewhere behind me brought an abrupt end to my thoughts. My eyes quickly opened and I instinctively rose to my feet and turned in the direction of the sound."

  show MC happy at left
  show Olin happy at right

  "The sight of my older brother brought a smile to my face. The last time I’d seen him, Olin had promised to return home for today. I was glad to see he kept that promise."

  MC "Military life at Fort Sol-Nahr still hasn’t improved your stealth, I see."

  Olin "I’m a captain now, I don’t need to be stealthy – it’s all about shouting orders at the Lyris under my command."

  show Olin wink at right

  Olin "And it’s not as if I can order you around after today, is it, little [player_siblingStatus]."

  show Olin normal  at right

  "Olin and I embraced briefly. Then we each took a step back and he regarded me with a wistful smile."

  Olin "I can’t believe it’s your coming-of-age already. I don’t know where the years have gone."

  MC "That’s because you’re losing your wits, old man."

  show Olin happy at right

  "Olin gave me a playful punch on one shoulder, both of us smiling."

  show Olin normal at right

  Olin "I’m not that much older than you, smart-arse, and I’m still more than capable of kicking your backside all over this grove, so watch it."

  MC "Thanks for making it. I know the fort keeps you busy."

  Olin "No problem. I wouldn’t have missed your big day."

  show MC normal at left

  MC "Have you seen mum and dad?"

  Olin "Yes, the house was my first stop, they told me you were out here. Are you ready to head back?"

  "I took in another deep breath of the invigorating air and glanced back in the direction of my birth tree. Whatever was to come, I wished it continued strength and vitality."

  "I turned back to Olin. Smiling, I nodded."

  MC "I’m ready."

  Olin "Then let’s get back before dad eats all of the pie."

  scene black with slowfade 
  scene house with fade

  "My mother had piled up the dining table with an assortment of foods by the time Olin and I returned to the house, and the whole family sat down together to celebrate my coming-of-age and Olin’s visit."

  "As we ate and drank, Olin filled us in on recent events at the fort and his life in general. I knew our parents still worried about the dangers inherent in his career of choice..."

  "...but he’d been a soldier – and by all accounts, a good one – for long enough now that they trusted him to look after himself."

  "In return, our mother told Olin about her latest alchemical experiments and findings, and our father did the same regarding his healing, both of them still as interested in their respective passions as they always had been."

  "Eventually we all sat back in our chairs, Olin and I stuffed to bursting and protesting our mother’s insistence that we could manage a few more mouthfuls."

  "As I expected it to at some point, conversation began to focus on the subject of my coming-of-age. My parents shared a few choice memories of my childhood, some amusing, some embarrassing, some both."

  show father smile at right with dissolve

  "Then my father reached beneath the dining table and brought up two wooden boxes that I didn’t realise he’d had down there. He placed the boxes before him and looked at me, smiling."

  Alarad "If you can summon the willpower to move your arms after stuffing all that food, your mother and I have some gifts we’d like to give you."
  show MC happy at left with dissolve

  MC "Thank you. Should I open them now?"

  show Olin wink at right#_c

  Olin "If you don’t, I will."

  show Olin normal at right#_c
  show MC normal at left with dissolve

  "I opened the first box and carefully removed the item within after unfolding the small sheet of cloth in which it was wrapped."

  "It was a bottle, its glass finely crafted but sturdy. Contained within was some kind of liquid. Assuming this was one of my mother’s concoctions, I looked at her."

  MC "What is it?"

  hide father smile
  show mother smile at right with dissolve

  Laurin "A healing potion. It’s very potent. The recipe is one I’ve studied and tinkered with over the years, and as today got closer, I finally decided to commit to my own take on the formula and cook it up."

  Laurin "It’s the only one I’m likely to make for a long time, if not ever – I’ve only ever owned one vial of dragon blood and I used it in that potion."

  show Olin laugh with dissolve

  "Of course I believed my mother but even so, I couldn’t help but raise my eyebrows in surprise. Olin chuckled."

  show MC blush with dissolve

  Olin "Mum, dragons have been extinct for... well, forever. How would you have some of their blood just lying around?"

  show Olin smile with dissolve
  show MC normal with dissolve
  show mother normal with dissolve

  Laurin "Blood can last a very long time if it’s properly preserved. It was passed down to me by my mother. She never told me where she got it from."

  Olin "So why didn’t you make this one-of-a-kind healing potion for me when I came of age?"

  Laurin "I wasn’t as experienced then as I am now. I didn’t trust my skills enough to use the dragon blood in a worthy manner and I certainly wasn’t going to waste it. So I waited. And now I’m good enough."

  show MC happy with dissolve

  MC "If you ask me nicely, Olin, maybe I’ll let you have a drop next time you stub your toe."

  show MC normal with dissolve
  show Olin wink with dissolve

  Olin "You’re the one who’s going to need it when I stub my boot on your thick head."

  show Olin normal with dissolve
  show MC happy with dissolve

  MC "Thanks, mum. This is amazing."

  show mother smile with dissolve

  Laurin "You’re welcome. Open your other present."

  show mother normal with dissolve
  show MC normal with dissolve

  "I placed the healing potion back inside its box before taking hold of the second box. I opened it and removed the item it contained: a cloth map."

  "The map was detailed, its lines drawn cleanly and carefully. It covered not only all of Lyriathis but also the neighbouring lands of Dahraith and Grana as well."

  "My eyes roamed over the map for a few seconds before they focused on something I suddenly noticed: a very small and faint dot of light emanating from a particular spot on the map."

  "In fact, the location marked by the dot seemed to be where our house stood in reality. I looked at my father."

  hide mother
  show father normal at right with dissolve
  show MC happy with dissolve

  MC "An enchanted map."

  Alarad "I drew it, but I had to ask for help from a mage I know to actually enchant it."

  MC "It looks great. I assume the light marks the house?"

  show MC normal with dissolve

  Alarad "Not quite. It’s you."

  Alarad "The enchantment is tied to your physical presence, so wherever you go in the lands covered by that map, the light will follow you and mark your current location. That way, the map will always show you where you are – you’ll never be lost."

  show Olin wink with dissolve
  Olin "So did you get a second copy made for you and mum, so you can always keep track of [player_name]?"
  show Olin normal with dissolve
  show MC angry with dissolve
  show father smile with dissolve
  Alarad "I’d be lying if I said the thought didn’t cross my mind, but no. [player_identifierHECaps]’s of age now, we shouldn’t be watching over [player_identifierHIM] all of the time."

  show MC normal with dissolve
  show father normal with dissolve
  MC "Thanks, dad. I really appreciate this."

  Alarad "If you do go travelling, it can help remind you where home is, and that mum and I are always here."

  MC "I’d never forget that."

  hide father
  show mother smile with dissolve
  Laurin "Olin, are you going to give your [player_siblingStatus] your gift?"

  Olin "Well, I can’t compete with dragon blood or a magic map, but anyway..."

  Olin "...here you go."

  "Olin reached beneath the table and brought up an item which he placed before me. I couldn’t tell what it was as it was wrapped in cloth."

  show mother normal with dissolve

  "I picked up the bundle and unwrapped it to reveal what was inside: a dagger."
  "The blade was sharp, and polished to the degree that I could see my face reflected back at me in the flat of the blade. The handle was metal and covered in an elegant and elaborate pattern."

  "Whoever had made the dagger had clearly put a lot of care and effort into it. It was a good weight and felt comfortable in my hand. I looked at my brother."

  show MC happy with dissolve
  MC "Thank you. I’m no expert but it looks like a fine piece of work."

  show Olin wink with dissolve
  Olin "I’ve seen a lot of daggers and believe me, it is."
  show Olin normal with dissolve
  show mother sad with dissolve
  "Out of the corner of my eye I saw my mother shift in her seat, and although she was still smiling, it seemed a little strained now. I assumed she wasn’t overly keen on the idea of me receiving a weapon as a gift."
  "Olin noticed her reaction as well – his eyes flicked briefly in her direction before focusing on me again."
  show Olin sad with dissolve
  Olin "I received that dagger years ago, during one of my earliest missions at Fort Sol-Nahr. A group of eight soldiers, including myself, rescued some travellers from a gang of bandits who’d been operating in the woods."

  Olin "One of the travellers was an old Lyrian – an old soldier. During our fight with the bandits, I saved his daughter’s life. He gave me that dagger in return."

  Olin "Apparently he’d had it for centuries. He said he was once a member of an elite group of rangers and that each member received an identical dagger upon joining, as a symbol of their status. That dagger was the one given to him."

  Olin "The group disbanded centuries ago and the old Lyrian was convinced he wasn’t long for this world, so he thought it would be fitting to pass down the dagger to a fellow soldier."

  Olin "With what I’d done for his daughter, he decided that I was that soldier. He wouldn’t take \"no\" for an answer."

  show Olin normal with dissolve
  Olin "Anyway, it’s mine to pass down now, and while you may not be a soldier, [player_name], you’re worthy of it and I know you’ll take good care of it."

  Olin "The old Lyrian’s daughter also rewarded me with a kiss but I think I’ll hang onto that. She was quite the pretty thing."
  show Olin smile with dissolve
  show mother normal with dissolve
  Olin "Olin grinned while our father chuckled and our mother rolled her eyes."

  show MC happy with dissolve
  MC "Thanks, Olin. I will take care of it."

  "I rewrapped the dagger and placed it next to my other two gifts. Then Olin asked the question I’d been waiting to hear from someone."

  show Olin normal with dissolve
  Olin "So, have you decided what you’re going to do now that you’ve come of age? Are you going to venture out on your own and explore the world or stay here and annoy mum and dad?"
  show MC normal with dissolve
  "I’d already given a lot of thought to my future, but before I could give Olin any kind of answer, our mother spoke."

  Laurin "Olin, give your [player_siblingStatus] a chance, [player_identifierHIS] coming-of-age day isn’t even halfway-over yet. There’s plenty of time for all that."

  Laurin "Now, who wants pudding?"

  hide mother 
  show father smile at right with dissolve

  "My father both frowned and smiled as he placed one hand on his stomach."

  Alarad "Not for me, sweetheart, or I’ll never be able to get up from this chair. Why don’t you fatten up your children some more while they’re both here?"

  show Olin laugh with dissolve
  Olin "At this rate you’ll have to cart me back to the fort in a wheelbarrow. But since I’ll be back on military food soon enough, I suppose I should make the most of it while I’m here."
  show Olin smile with dissolve
  hide father
  show mother smile at right with dissolve

  Laurin "That’s my boy. What about you, [player_name]?"
  show MC happy with dissolve
  MC "Sounds good. Like you said, there’s no rush."

  "While that was true to a degree, I was old enough now to understand that delaying the future was impossible – it was coming for me in some form, whether I was ready or not."

  "But first, pudding."
