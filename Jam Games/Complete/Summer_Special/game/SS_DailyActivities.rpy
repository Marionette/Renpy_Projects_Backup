# label lbl_dailyComments:
# if CurrentTimeOfDayName == 'morning':
   # "I have a lot of stuff I need to get done this morning."
# elif CurrentTimeOfDayName == 'afternoon':
   # "The days almost halfway over so  I should probably get back to work."
# elif CurrentTimeOfDayName == 'evening':
  # "It's almost time to close for the night but there's a few things left to finish."
# elif CurrentTimeOfDayName == 'night':
   # "..." 
# return

label lbl_dailyActivities:
  $thing = renpy.get_return_stack()
  "[thing]"
  #call lbl_dailyComments    
  if CurrentTimeOfDayName == 'morning':
     "I have a lot of stuff I need to get done this morning."
  elif CurrentTimeOfDayName == 'afternoon':
     "The days almost halfway over so  I should probably get back to work."
  elif CurrentTimeOfDayName == 'evening':
    "It's almost time to close for the night but there's a few things left to finish."
  elif CurrentTimeOfDayName == 'night':
     "..."   
  menu:
    "I should..."
    "Help stock groceries.":
      call lbl_stockShelves from _call_lbl_stockShelves
      "End Help stock groceries. lbl_dailyActivities"
    "Work at the cash register.":
      call lbl_workRegister from _call_lbl_workRegister
    "Do a bit of everything":
      call lbl_doEverything from _call_lbl_doEverything
  $thing = renpy.get_return_stack()
  "[thing]"
  "End lbl_dailyActivities"
  return
      
#DAILY ACTIVITIES
#Daily activities are chosen to do each Morning, Afternoon and Evening by the MC while at work. Certain choices will raise affection for each #guy. There are 3 activities, 3x a day to do for 5 days in game, so at most 15 possibilities for each choice.

#---------------------------------------------------------
init python:
  #StockShelves_LabelsList = ["lbl_Mc_CanT_Lift_Big_Box_Of_Items_And_Needs_Help"]

  StockShelves_LabelsList = ["lbl_Help_Customer_Find_An_Item"]
  
  WorkRegister_LabelsList = ["Checkout_Customer_Who_Pays_For_Everything_With_Change", "Get_N_To_Help_Check_Out_Long_Line_Of_Customers", "Customer_Ask_For_Item_Behind_Counter_That_Too_High_To_Reach_And_N_Helps", "Kids_Come_In_And_Beg_N_For_Cakes", "N_Is_Eating_Fries"]
  
  DoEverything_LabelsList = ["Sweep_Inside_Of_Store", "Clean_Windows", "Dust_Counters", "Sort_Through_The_Stores’_Old_Receipts", "Organize_The_Area_Behind_The_Counter", "Clean_Out_The_Employee_Fridge_In_The_Stockroom", "Chat_With_A_Customer"]

label lbl_stockShelves:
  ##Stock Shelves. (raises JJ points)
  #MC can't lift big box of items and needs help.
  #Help customer find an item
  #Have contest to see who can stock items faster
  #Restock item coworker put in wrong place
  #MC explains weird item store sells
  #Help re-price items for upcoming sell
  #Check Store Inventory
  #MC gets cold while stocking in freezer, JJ lends her his coat
  #MC goes to do stock but JJ isn’t there. He comes back soaking wet;Was having water gun fight with kids while on 15 min break and didn’t realize time got away from him. Apologizes
  #Kids come in asking JJ to play. MC shoos them off because he’s got work to do.
  $relationship_June+=1
  call expression renpy.random.choice(StockShelves_LabelsList) from _call_expression
  "End lbl_stockShelves"
  return


label lbl_Mc_CanT_Lift_Big_Box_Of_Items_And_Needs_Help:
   scene bg storage room
   show cereza angry
   "I wearily glance over at the shipment of goods that were delivered to us yesterday. The store had gotten a little busy around the delivery time, so I put off organizing the boxes for later."
   "It would probably be best to move them out of the way now. The boxes are really big and kind of crowding some of the aisles. I already noticed a few customers blindly bumping into them, and worse, a few others had tripped on the corners."
   show cereza normal
   "The last thing I need is for Granny to get sued by some pretentious customer who wants to blame their klutziness on my mistake of leaving a few measly boxes in the aisles. There are only five or six of boxes; I should be able to move them into our stockroom in no time."
   "I bend down to wrap my arms around one of the boxes. It turns out to be somewhat bigger than I thought, so my arms clumsily hug the sides instead."
   "My fingers can’t seem to get a grip on anything, and they awkwardly slide around. I take a deep breath and brace myself for the lifting. I squeeze my arms around the box as hard as I can and...am unable to pick the box off of the ground."
   show cereza confused
   "I stop and stare at the box incredulously. It didn’t look that heavy at all. I brace myself and try lifting it again. No luck this time either."
   show cereza angry
   "I purse my lips angrily, roll up my sleeves and really give it my all this time. I’m able to lift the box about a foot off of the ground, until I feel myself wobbling and my fingers losing grip of the box."
   "I squeeze my eyes shut, dreading the crash of the box on the ground and having the contents fall out onto the floor."
   show cereza surprise
   "Just as the box is about to slip out of my arms, I feel two warm hands grab my arms for extra support. Surprised at the random touch, I instinctively let go of the box and tumble onto the floor."
   show june disbelief at right
   ju "You okay?"
   show cereza embarrassed
   "I look up and see June holding the box, waiting for me to get back up. I notice an unsure grin on his face trying to cover his concern. I stand up and brush myself off."
   show june normal
   ce "Yeah, I’m okay. I didn’t think the box was going to cause so much trouble."
   show june grin
   ju "Haha, you seem to think that way about everything that comes into this town."
   show cereza sad
   "I glare at him and reach to grab the box again. No way am I going to look weak in front of this dude. The look of concern comes back to June’s face."
   show june surprise
   ju "Woah, wait, you seriously want to try again?!"
   show june confused
   show cereza angry
   ce "Uh, yeah, of course. I’m a strong girl, I can handle this."
   ju "No offense, Captain, but these are really kinda heavy. I can lift them, but even I myself might need help carrying them."
   show cereza unimpressed 
   ce "And your point is?"
   show june embarrassed
   ju "Well...I don’t want you to get hurt. I think they’re too heavy for you."
   ce "So, what? You’re saying you don’t think I can handle this?"
   show june tired
   ju "W-well, no…er, maybe?"
   show cereza angry
   "I angrily grab the box and put all my strength and determination into holding it up on my own. I’ve always been able to handle things by myself. I’m not going to let some box stop me now."
   "I’m able to turn around with the box in my arms and make my way to the stockroom. Just as I start feeling proud of myself, I instead feel the weight of the box against my petite frame. I start teetering and feel the box ready to slide out of my arms."
   show cereza disbelief
   ce "Oh sh--!"
   show june surprise
   ju "Watch out!"
   "I feel June rush up behind me and grab the box. He pushes against my back to keep me from falling. I’m slightly embarrassed because it feels like an awkward hug, but I keep my mouth shut, grateful that he was willing to help me."
   show june hurt
   ju "Cereza, are you okay?"
   show cereza embarrassed
   "He doesn’t even try to hide his concern. I feel bad for being stubborn."
   ce "Yeah, I-I’m fine,"
   "Mumbling those words I shakily duck out from under his arms."
   show june smirk
   ju "Ha, you almost had it that time!"
   show cereza hurt
   ce "Yeah, I'm...sorry."
   ce "I just really thought I could handle it on my own this time."
   show june smile
   "June smiles and grins at me."
   show june tease
   show cereza embarrassed
   ju "You know, it’s okay to ask me for help. I mean, your grandma did hire me to do the heavylifting around here; it’s kind of my job. I got hired because I’ve got the muscles in the description."
   show cereza happy
   "My face breaks into a smile and I roll my eyes at him."
   show june grin
   ce "Well I guess I have to admit, you do a pretty good job." 
   show cereza normal
   "June beams proudly at the compliment. I reach out and hold the opposite side of the box. June arches an eyebrow at me."
   show june tease   
   ju "You still haven’t learned your lesson?"
   show cereza grin
   ce "Haha, I did. The boxes are kinda heavy for me. But the least I can do is at least help you carry them into the stockroom."
   show june happy
   ju "Thank goodness! I really didn’t want to do this on my own. It’s kind of boring, to be honest."
   show cereza tease
   ce "You think any type of work is boring."
   show june smirk
   ju "Can you really blame me?"
   show june grin
   show cereza grin
   "We playfully bicker while we help each other move the boxes out of the aisles and into the stockroom."
   return
  
label lbl_Help_Customer_Find_An_Item:
  $thing = renpy.get_return_stack()
  "[thing]"
  "Help customer find an item"
  return
#   
label lbl_Have_Contest_To_See_Who_Can_Stock_Items_Faster:
  "Have contest to see who can stock items faster"
  return
#   
label lbl_Restock_Item_Coworker_Put_In_Wrong_Place:
  "Restock item coworker put in wrong place"
  return
#   
label lbl_Mc_Explains_Weird_Item_Store_Sells:
  "Cereza explains weird item store sells"
  return
#   
label lbl_Help_RePrice_Items_For_Upcoming_Sell:
  "Help re-price items for upcoming sell"
  return
#   
label lbl_Check_Store_Inventory:
  "Check Store Inventory"
  return
#   
label lbl_Mc_Gets_Cold_While_Stocking_In_Freezer:
  "Cereza gets cold while stocking in freezer, June lends her his coat"
  return
#   
label lbl_Mc_Goes_To_Do_Stock_But_Jj_Isn’T_There:
  "Cereza goes to do stock but June isn’t there. He comes back soaking wet;Was having water gun fight with kids while on 15 min break and didn’t realize time got away from him. Apologizes"
  "End lbl_Mc_Goes_To_Do_Stock_But_Jj_Isn’T_There"
  return
#   
label lbl_Kids_Come_In_Asking_Jj_To_Play:
  if meetKids == False:
      scene bg storeInside
      show june hurt at right2 
      show madison happy
      show rashid normal at left
      un "Awww! Come on June! It's gonna be sooooo fun! Tell em' Rashid."
      show rashid happy
      ra "Uh huh, Madison's right! Terrence even said that whatever team wins the kickball tournament will get a one year pass for free unlimited tokens as Pizza Wally."
      show madison joke
      ma "Not to mention free pizza too. You love pizza June! And the free just makes it all taste even better!"
      show rashid smile
      ra "We just need one more member on our team! Pretty please June!"
      show june tired
      ju "...ugh..."
      ju "...I can't just leave work to play with you guys..."
      show madison sad
      show rashid sad
      ma "Why not? Winning the grand prize is worth way more than missing a day of work. We'll sneak out the back. Your boss won't even know you're gone."
      show june shy
      ju "Cereza really needs me to be here to help. It's not fair to leave her with all the work I'm supposed to do."
      show madison tease
      show rashid normal
      show june embarrassed
      ma "Just tell her you're sick or somethin'. That always works for me when I want to get out of a test at school."
      show cereza angry
      show madison normal at left
      show rashid normal at left2
      show june surprise
      ce "June! Who are these delinquents and why are they trying to get you to bail on work?"
      show june embarrassed
      ju "Ah...this is  Madison and Rashid. Guys this is Cereza, my boss."
      show madison sad
      ma "Sorry to be the bearer of bad news Cereza, but June here is sick and has to leave early. So if you'll exscuse us we'll be on our way~"
      ce "Not so fast short stuff. What is he sick with exactly?"
      show madison tease
      ma "Uhhh...."
      show rashid smile
      show june surprise
      ra "H-hemorrhoids! He has a super bad case of hemorrhoids!"
      show madison sad
      show june disbelief
      ce "Hemorrhoids? Really?"
      show rashid tease
      ra "Uh huh! And t-they're like, really contagious so unless you want them too I think June needs to go home right now immedietly!"
      show june tired
      ju "..."
      show rashid worry
      ce "You guys can cut the act. I overheard your little scheme so I'm afraid June isn't going anywhere today."
      ma "..."
      ra "..."
      show rashid sad
      show june shy
      ju "Sorry guys. Thanks for trying though."
      show madison angry
      ma "Why'd you pick a dumb sickness like hemorrhoids?!"
      show rashid worry
      ra "I don't know! I hear grandpa and his friends talking about them all the time so I thought they were like, adult chicken pox or something..."
      hide madison
      hide rashid
      show cereza smirk
      ce "Some friends you got there."
      show june grin
      ju "They're harmless enough. But I think i'll go to the back now and start sorting through boxes. Never too early to put in a hard days' work!"
      show cereza tease
      show june happy
      ce "Yeah, I think that's for the best. Don't want the customers to catch your hemorrhoids now do we. "
      ju "Heh! "
      $meetKids = True
      return
  else:
      "Kids come in asking June to play. Cereza shoos them off because he’s got work to do."
      return
#   
#---------------------------------------------------------
  
label lbl_workRegister:
  ##Work the Register. (raises K points)
  #Checkout customer who pays for everything with change
  #Get N to help check out long line of customers
  #Customer ask for item behind counter that too high to reach and N helps
  #Kids come in and beg N for cakes. He tells them that if they help him unload a delivery tomorrow morning he’ll let them choose whatever they want  at his bakery afterwards.
  #N is eating fries. MC laughs and says the french word for them, pommes de terre frites. N is surprised she remembers. As a kid they’d pay a game where she would point to things and ask him what the word for it was in French and he’d give her a translation. MC always thought calling them fried apples of the earth was funny.

  $relationship_Kameron+=1
  call expression renpy.random.choice(WorkRegister_LabelsList) from _call_expression_1
  return

  ##Work the Register. 
label Meet_Mona:
  if meetMona == False:
      show bg storeInside_Register
      show cereza normal at center
      show storeRegister  
      show mona normal at left
      "The store is as busy as ever and a long line of customers are in line to be checked out. Groaning at the increase in my workload I quickly ring them up as soon as I can."
      "A familiar face, however causes me to slow down."
      ce "Hi Mona. It's been a while. "
      mo "I had heard you were back in town Cereza but had to come and see it for myself. Sorry to hear about Granny. How's she holding up?"
      show cereza grin
      ce "Same old, same old. If they poke her with another needle she just might make a run for it though. Still run the mechanic shop down the road?"
      show mona smile
      mo "Yup. Just left their actually. Had to stop by real quick before you guys close for the night. Gotta pick up some dinner."
      show cereza tease
      ce "I see....Vienna sausage, beer and ramen. The dinner of champions."
      show mona happy
      show cereza happy
      mo "Don't you know it! It was good seeing you Cereza. And tell Granny I'm coming to visit here as soon as she gets home."
      ce "Sure! Take care."
      hide mona
      $meetMona = True
  else:
      "Mona comes to the store."
  return
  
label Checkout_Customer_Who_Pays_For_Everything_With_Change:
  "Checkout customer who pays for everything with change"
  return
  
label Get_N_To_Help_Check_Out_Long_Line_Of_Customers:
  "Get Kameron to help check out long line of customers"
  return
  
label Customer_Ask_For_Item_Behind_Counter_That_Too_High_To_Reach_And_N_Helps:
  "Customer ask for item behind counter that too high to reach and Kameron helps"
  return
  
label Kids_Come_In_And_Beg_N_For_Cakes:
  "Kids come in and beg Kameron for cakes. He tells them that if they help him unload a delivery tomorrow morning he’ll let them choose whatever they want  at his bakery afterwards."
  return
  
label N_Is_Eating_Fries:
  "Kameron is eating fries. MC laughs and says the french word for them, pommes de terre frites. He is surprised she remembers. As a kid they’d pay a game where she would point to things and ask him what the word for it was in French and he’d give her a translation. Cereza always thought calling them fried apples of the earth was funny."
  return
  
#---------------------------------------------------------
label lbl_doEverything:
  ##Do a bit of everything.  (doesn't raise any affection points. )
  #Sweep inside of store
  #Clean windows
  #Dust counters
  #Sort through the stores’ old receipts to see ho
  #Organize the area behind the counter 
  #Clean out the employee fridge in the stockroom
  #Chat with a customer 
  call expression renpy.random.choice(DoEverything_LabelsList) from _call_expression_2
  return

  
label Sweep_Inside_Of_Store:
  "The floor looks like it could use a good sweeping. Customers can track dirt, dust and sometimes even gum into the store from the outside, so the floor is only as clean as I can make it throughout the day."
  "It’s also beneficial for myself because it means I won’t have to wade around through the grime while I stay inside the shop all day."
  "I grab Granny’s worn-out broom and start sweeping meticulously, taking time not to miss any grains of dirt or random wads of paper. It takes a while, and occasionally I hear June snicker at my laboring pace and detail. A sharp glare from my end usually shuts him up though."
  "After a few solid hours of sweeping, the store floor looks shiny enough to put Cinderella’s cleaning skills to shame. I proudly admire my work for a minute or two before putting the broom away."
  return
  
label Clean_Windows:
   "The store windows look like they could use a good cleaning."
   "Rowdy teens have attempted vandalizing our store from time to time, so sometimes you can find lame graffiti on the windows that need to be cleaned off."
   "Other times I’ll notice messy kids pressing their faces up against the windows while they try to peer into the candy section, leaving behind smudgy face and finger prints after they finish gawking."
   "Granny always does her best to keep a clean store. Even at her old age with all of her health problems, she still insists on going out and cleaning junk off from the windows whenever any appears. As her substitute shopkeeper, it’s only fair that I maintain the store as well as she did."
   "Because as Granny would say, 'What good are windows for a shop if customers can’t even see through ‘em?' "
   "I roll up my sleeves, grab some cleaning supplies and head outside to clean the muck off. It takes a lot of time, patience and elbow grease, but eventually I start to see some progress from my effort."
   "June comes around to make faces from the other side of the glass from time to time, but he usually laughs and goes away when I pretend to throw soap or water at him."
   "After a couple of hours of intense scrubbing, I step back and admire my work. Light shines down on the clear glass, making it sparkle like crystal. It also smells lemony-fresh. Anyone can see clearly in and out of the store now. From the inside of the store, I see June give me a big grin and two thumbs up. I smile and head back inside."  
   return
  
label Dust_Counters:
  "I slide my finger over the tops of one of the counters, and grimace at the layer of dust my finger sweeps up. This can be a health hazard. I should probably dust these counters."
  "I prop the shop door open to let the dust escape as I begin to clean. I throw on some gloves and a hairnet to keep the dust from getting on me. From the way I looked, one might think I was dealing with some kind of radiation or something."
  "June takes a look at my makeshift outfit and doesn’t even try to suppress his guffaw. I’m tempted to order him to throw on the gear and do the cleaning himself, but I notice he’s actually doing a pretty good job of restocking shelves and interacting with customers, so I reluctantly hold my tongue and say nothing."
  "It takes a lot of time rearranging things so I can reach the dust hiding in the nooks and crannies. I also have to wait patiently for customers to leave so I don’t choke them on any dust clouds I create. The store isn’t really dirty or anything, it’s just everyday grime from the air that decides to settle down on our counters."
  "After a couple of steady hours of dusting, I manage to get all of the dust off of our counters and back out into the dirty streets."
  "June slides his palm along the counter surface and looks approvingly at my work. He doesn’t make fun of me when I finally take off my cleaning gear."
  return
  
label Sort_Through_The_Stores’_Old_Receipts:
  "Sort through the stores’ old receipts"
  return
  
label Organize_The_Area_Behind_The_Counter:
  scene bg storeInside_Register
  show storeRegister
  show cereza normal    
  "As I ponder what I should do to help the store, I take a step back from the counter and trip on something."
  "CRASH!"
  show cereza surprise    
  "I fall down onto a pile of empty shipment boxes and assorted canned goods. My body aches a little from the sudden fall, and I notice that I have a few scrapes from some of the cans. Otherwise though, I’m fine."
  "I hear June’s sneakers as he quickly approaches the counter. From my place on the floor, I am able to make out his multicolored hair as he looks down at me."
  show cereza hurt  
  show june confused at right
  ju "Hey Captain, you okay?"
  show cereza angry
  ce "Yeah, I’m alright….how in the world did all of this stuff get piled up back here?"
  show june grin
  "June chuckles nervously as he shifts his gaze away from my angry scowl."
  ju "Uh...I may have left some of that stuff there."
  show cereza pissed   
  ce "Are you kidding me?! This is a safety hazard! Why would you leave a massive pile of stuff lying around like this???"
  show cereza angry
  show june happy
  "June laughs as he scratches the back of his head."
  ju "Well, I don’t know, I just found other stuff to do. It’s not like I wasn’t being productive in the meantime."
  show cereza unimpressed   
  show june normal 
  "I roll my eyes at him and get up from the mess."
  ce "Fine, whatever. I’ll clean this stuff up."
  show june grin
  ju "Hey thanks! I’ll just--"
  show cereza pissed
  show june surprise
  ce "That doesn’t mean you get to slack off! Go do something productive while I clean up this mess. And you better not be leaving behind anymore piles anywhere else in the store!"
  show june embarrassed
  ju "Okay, okay, I get it…"
  hide june
  "Even as he turns away to go find something to do, I can still hear  him muttering."
  show cereza tired
  "With an exasperated sigh I look at the clutter behind the counter. It’s amazing how so much stuff has piled up back here, and admittedly, not all of it was put there by June."
  show cereza normal
  "I remember putting down some of the stuff myself when I was caught in the middle of work by customers who needed help."
  "The delivery people who stop by have also left some of our shipment stuff behind the counter when they were in a rush to leave and couldn’t wait for us to get the packages from them."
  "I start by disassembling some of the empty boxes and taking them to the recycling bin near our store, one that no one seems to remember exists except for Granny and I."
  "That ends up clearing up a lot of the clutter. I spend the rest of the time moving boxes and packages to our storage room and unpacking things that need to be unpacked. I clean up around the counters and throw away useless debris. I also make sure to restock important items, like receipt paper and grocery bags."
  "After a few hours, the back of our counter looks professionally clean. June peers over the counter and smiles sheepishly."
  show cereza angry
  show june normal at right
  ce "No more piles, okay? Make sure it stays looking like this."
  show june smile
  ju "Sure boss, I’ll keep it clean from now on."
  return
  
label Clean_Out_The_Employee_Fridge_In_The_Stockroom:
  scene bg store breakroom
  show cereza normal
  "I head over to the stockroom, which also has a section that doubles up as our breakroom. I remember I left some fruit juice boxes in the refrigerator some time back. A nice, cold drink sounds good right about now."
  "I open the fridge door to reach inside and--"
  show cereza disbelief
  ce "AWW GROSS!!!"
  "The fridge not only smells suspiciously ominous, but it’s packed with all kinds of weird stuff, some that I can see are starting to turn strange colors that food should not be."
  "I don’t normally use the refrigerator because most of my food is non-perishable and can handle being left in my lunchbox, otherwise, I definitely would have noticed this mess before."
  show cereza unimpressed
  "I grab a plastic fork from our utensil area and poke around at the stuff. I see a few of Granny’s snacks going bad; she must have forgotten about them around the time she got sick and had to be taken to the hospital."
  "I also notice an array of browning fruits line one side of the fridge. That was Granny’s attempt to try and remember to eat more fruits that would help her health, like her doctor recommended."
  "But I also notice several containers I don’t recognize filled with half-eaten meals. The containers contain frivolous leftovers, like pizza crust, chicken bones, morsels of vegetables and other junk like that."
  "These can only belong to one other person I know who works in this store…"
  show cereza angry
  "I stomp my way out of the breakroom, when I bump into June at the entrance. Just the person I wanted to see."
  show june happy at right
  ju "Hey boss, you want some--"
  ce "Pizza crust?"
  show june confused
  ju "What??"
  ce "Or chicken bones maybe?"
  show june tease
  ju "You hit your head on a can or something, Captain? What are you even talking about?"
  show cereza pissed
  ce "I’m referring to your 'lunch' that you left decaying in the fridge for who knows how long."
  show june unimpressed
  show cereza angry
  "June looks confused. I lead him over to the refrigerator and open the door for him. He stares with an empty expression."
  ju "Ummm, what am I supposed to be looking at?"
  show cereza pissed
  ce "June! Do you not see this mess? Do you not smell this mess?? Granted, not all of it is yours, but what is all of this stuff???" 
  show cereza angry
  "I point out all of his containers to him."
  show june grin
  ju "Oh! I remember that, that’s my leftover pineapple spinach pizza! Boy, it was good! The crust was kinda dry though. And those were my honey-sriracha wings. They were the bomb with ranch sauce."
  show cereza unimpressed
  show june disbelief
  "June catches my glare and laughs nervously."
  show june hurt 
  ce "You trashed the employee fridge with your leftovers?"
  show june embarrassed
  show cereza hurt
  ju "Well, it wasn’t on purpose..." 
  ju "Sometimes I forget to grab my stuff when I leave to catch the bus at the end of the day. I’m sorry, I didn’t mean to pile it all up like that."
  show cereza tired
  ce "It’s okay, June ." 
  show june normal
  show cereza normal
  ce "Just try and remember to take your stuff from now on. You can go back out, I’ll clean up the fridge. Here, take this with you."
  "I hand him one of my juice boxes I found under his containers. It’s my way of apologizing for coming off so harsh."
  show june happy
  ju "Oh hey, thanks!"
  hide june
  "After he leaves, I grab our giant breakroom trash can and use it to prop open the refrigerator door. I put on some gloves and a disposable face mask so I don’t have to breathe the rotting odors."
  " I carefully pick up Granny’s rotting fruits and throw them away, being careful not to squish or squeeze their now-pulpy bodies. Next I grab June’s containers and empty them out, piling them in the sink to be washed afterwards. I do the same with Granny’s leftover stuff too."
  "After throwing out everything that needed to be thrown away, I quickly tie up the trash bag and hurriedly take it out to the dumpster outside. Once I come back, I wash the containers and set them out to dry."
  "I also grab a box of baking soda from the store shelf and open it up to leave in the fridge to collect any remaining odors."
  "The last thing I do after I finish cleaning everything, is grab a yellow sticky note and a black marker. I write 'DON’T FORGET TO TAKE HOME YOUR STUFF' and stick it on the fridge door so that June will see it each time he comes to the fridge."  
  return
  
label Chat_With_A_Customer:
  "Chat with a customer"
  return
  
  
  