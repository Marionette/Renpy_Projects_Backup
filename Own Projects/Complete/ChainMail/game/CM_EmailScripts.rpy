init python:
  EmailEnabledFlag = True
  TrinaEmail_Flag_Wedding = False
  TrinaEmail_Flag_Shop = False

###################### Misc Emails #######################################
init python:
  Sample_Email_1 = ["SubjectHere", "sender@email.com", "EmailContent", "ReplyLabel" ]

##-----------------------------------------------------------------------

#TODO: Figure out how to set these to send TO 'Everyone' instead of Robert
#TODO: Add timestamps

##IT Emails
#DONT PANIC!
#RE:DONT PANIC!
#Scheduled Maintenance

##Teacher Emails
#Re:Scheduled Maintenance (Bannister)
#RE:Scheduled Maintenance (Marshall)

label lbl_Email_IT_Maintenance_start():
  call lbl_Email_IT_Maintenance_DontPanic1 from _call_lbl_Email_IT_Maintenance_DontPanic1
  call lbl_Email_IT_Maintenance_DontPanic2 from _call_lbl_Email_IT_Maintenance_DontPanic2
  call lbl_Email_IT_Maintenance_ScheduledMaintenance1 from _call_lbl_Email_IT_Maintenance_ScheduledMaintenance1
  call lbl_Email_IT_Maintenance_ScheduledMaintenance2 from _call_lbl_Email_IT_Maintenance_ScheduledMaintenance2
  call lbl_Email_IT_Maintenance_ScheduledMaintenance3 from _call_lbl_Email_IT_Maintenance_ScheduledMaintenance3
  
  return
  
label lbl_Email_IT_Maintenance_DontPanic1():
  $Email_IT_Maintenance_DontPanic_replyList = []

  $Email_IT_Maintenance_DontPanic_replyList.append("Your emails are safe!\nWe are changing over the email server so the email system will be down for the weekend. Some email functionality is currently disabled untill the work is complete. This includes visibility of old emails, but even though you can't see them they are still there, and will be available again once the transfer is complete.\n\n Erin")
  
  $ subject = "DONT PANIC!"
  $ replylabel =  None        
  $ forwardlabel =  None    
  $ add_message(subject, 'Erin', list(Email_IT_Maintenance_DontPanic_replyList), replylabel, forwardlabel)
  #$ add_now()
  
  return
  
label lbl_Email_IT_Maintenance_DontPanic2():
  $Email_IT_Maintenance_DontPanic_replyList = []

  $Email_IT_Maintenance_DontPanic_replyList.append("Ignore my last email as I have been informed the format made it seem 'unprofessional'.\n (Also Derek, you can stop emailing me about your party, like I've said 10 times now nobody will be able to see those emails so just send them again.) \n\nThanks,\nErin")
  
  $ subject = "RE:DONT PANIC!"
  $ replylabel =  None        
  $ forwardlabel =  None    
  $ add_message(subject, 'Erin', list(Email_IT_Maintenance_DontPanic_replyList), replylabel, forwardlabel)
  #$ add_now()
  
  return
  
label lbl_Email_IT_Maintenance_ScheduledMaintenance1():
  $Email_IT_Maintenance_ScheduledMaintenance_replyList = []

  $Email_IT_Maintenance_ScheduledMaintenance_replyList.append("This is an automated message to inform you of ongoing [EMAIL MAINTENCE] due to start on [00:00 FRIDAY 28th OCTOBER] at and end on [11:59 SUNDAY 30th OCTOBER]. During this time [EMAIL] functionality will be limited however no data is expected to be lost and full access will return upon completion.\n\nApologies for any inconvenience caused.\n\nIT Department")
  
  $ subject = "Scheduled Maintenance"
  $ replylabel =  None        
  $ forwardlabel =  None    
  $ add_message(subject, 'IT', list(Email_IT_Maintenance_ScheduledMaintenance_replyList), replylabel, forwardlabel)
  #$ add_now()
  
  return
  
label lbl_Email_IT_Maintenance_ScheduledMaintenance2():
  $Email_IT_Maintenance_ScheduledMaintenance_replyList = []

  $Email_IT_Maintenance_ScheduledMaintenance_replyList.append("Hi Guys,\nWith regards to the email maintenance thats going on atm, im extending the Monday deadline to Wednesday. I hope the extra time helps you guys out if you were still working on your assignments.\n\nEnjoy your weekend and Happy Halloween!\n\nDr. Anisa Marshall")
  
  $ subject = "Re:Scheduled Maintenance"
  $ replylabel =  None        
  $ forwardlabel =  None    
  $ add_message(subject, 'Marshall', list(Email_IT_Maintenance_ScheduledMaintenance_replyList), replylabel, forwardlabel)
  #$ add_now()
  
  return
  
label lbl_Email_IT_Maintenance_ScheduledMaintenance3():
  $Email_IT_Maintenance_ScheduledMaintenance_replyList = []

  $Email_IT_Maintenance_ScheduledMaintenance_replyList.append("Attention All,\nAs i keep receiving extension requests from individuals due to the scheduled email maintenance let me clarify my stance on extensions. \nNo extensions will be given and I will expect any outstanding work to be delivered to me on Monday morning.\n\nPoor planning on your part does not constitute an emergency on mine.\n\nRegards,\nDr. Laith Bannister")
  
  $ subject = "Scheduled Maintenance"
  $ replylabel =  None        
  $ forwardlabel =  None    
  $ add_message(subject, 'Bannister', list(Email_IT_Maintenance_ScheduledMaintenance_replyList), replylabel, forwardlabel)
  #$ add_now()
  
  return

##-----------------------------------------------------------------------

#party


label lbl_Email_Derek_Party_start():
  call lbl_Email_Derek_Party() from _call_lbl_Email_Derek_Party
  call lbl_Email_Derek_Party1() from _call_lbl_Email_Derek_Party1
  call lbl_Email_Derek_Party2() from _call_lbl_Email_Derek_Party2
  call lbl_Email_Derek_Party3() from _call_lbl_Email_Derek_Party3
  return
  
label lbl_Email_Derek_Party():
  $Email_Derek_Party_replyList = []

  $Email_Derek_Party_replyList.append("Are you gonna spend halloween weekend trick or treating with the kids. Or are you planning on having some real fun? If so")
  
  $ subject = "Attention Guys and Ghouls!"
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Derek', list(Email_Derek_Party_replyList), replylabel, forwardlabel)
  #$ add_now()
  
  return
  
label lbl_Email_Derek_Party1():
  $Email_Derek_Party_replyList = []

  $Email_Derek_Party_replyList.append("Sorry my cat hit the go button before i was ready. Lets start again. \nAre you gonna spend halloween weekend trick or treating with the kids. Or are you planning on having some real fun? If so then you are invited to a Spooktacular extravaganza. Costumes are NOT optional. \nIf you're still down to par")
  
  $ subject = "RE:Attention Guys and Ghouls!"
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Derek', list(Email_Derek_Party_replyList), replylabel, forwardlabel)
  #$ add_now()
  
  return
  
label lbl_Email_Derek_Party2():
  $Email_Derek_Party_replyList = []

  $Email_Derek_Party_replyList.append("(Sorry cat again)\n\nAre you gonna spend halloween weekend trick or treating with the kids. Or are you planning on having some real fun? Interested in our Haunting Spirits and Wicked Brews? If so then you are invited to a Spooktacular extravaganza. Costumes are NOT optional. \nIf you're still down to party then come on down to my house on Saturda")
  
  $ subject = "RE:RE:Attention Guys and Ghouls!"
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Derek', list(Email_Derek_Party_replyList), replylabel, forwardlabel)
  #$ add_now()
  
  return

  
label lbl_Email_Derek_Party3():
  $Email_Derek_Party_replyList = []

  $Email_Derek_Party_replyList.append("Oh ffs. \nMy house 6pm Saturday. Its a party, wear a costume. Food and drink supplied.")
  
  $ subject = "RE:RE:RE:Attention Guys and Ghouls!"
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Derek', list(Email_Derek_Party_replyList), replylabel, forwardlabel)
  #$ add_now()
  
  return

##-----------------------------------------------------------------------

##Curse email
init python:
  Email_ChainLetter_replyList = []
  Email_ChainLetter_Forwarded_Flag = False
  
  
label lbl_Email_ChainLetter_start():
  #From: jhiga@fspub.com
  #To: swest@fspub.com 
  #Subject: Favor
  $Email_ChainLetter_replyList = []

  $Email_ChainLetter_replyList.append("DON'T STOP READING! Now that you have started reading this you are under the curse of Olivia-Rose Murphy.\n\nOlivia-Rose Murphy grew up a happy child in the countryside. She was always friendly with the local animals and the animals loved her. As she turned 15 her family moved to the countryside and unfortunately for her the other children at her new school didn't appreciate the crow that had followed her from the countryside and was always around her. They started to spread rumors around the school about her, and it wasn't long before the bullying started. \nAfter months of being tormented by the other kids Olivia-Rose got mad at the crow and tried to chase it away, when it wouldn't leave she threw a stone at the bird, hitting it in the eye blinding it in that eye and it flew off. Olivia-Rose felt bad about hitting the bird but at least it was finally gone. \nIt wasn't long before her luck seemed to turn around, Olivia-Rose made some friends at school and the rumors about her faded and within the next few weeks the bullying had all but stopped. \n\nOlivia-Rose never saw the bird again until a year later when she returned to the countryside to visit her Grandparents. She saw the bird again as she arrived in town and it seemed to be following her around. It never got close to her but it always seemed to be watching whenever she looked outside. Each day it seemed like there were more and more birds gathering outside her Grandparents house until by the day before they were set to return to the city there were a dozen birds perched on the power lines outside the house. \n\nRemembering the rock she had thrown she went outside to try and make amends with the bird, but each time she got close the bird would fly a little further away. She tried to speak softly and move slowly to show she wasn't a threat but seemingly still frightened of her it slowly moved deeper into the forest next to the house. After 20 minutes she realized that she was pretty deep in the forest and decided to give up, unfortunately that was when the other birds swooped down and started pecking at her.\n\nIn a panic she ran deeper into the woods before tripping and falling into a small ravine. She survived, however her left leg and right arm were broken and she was unable to climb out. After an hour of crying she realized the crow she had been following had gotten closer, she tried to call it over, after all crows are supposed to be very smart, maybe it could get help. Eventually she coaxed it over and it hopped onto her chest as she lay there. From this close she could see the scar on its eye were the rock had struck it, and she apologized profusely. But it was too late. Suddenly without warning the bird pecked at her right eye. She screamed and tried to fight it off, but in her exhaustion she was unable to fight it off for very long as the bird plucked out her eye, the very same eye she had blinded a year before.\n\nIt wasn't until a week later that her body was found in that ravine, broken and bloody. The authorities ruled the death accidental and although they found it curious that she had been attacked by birds only one of her eyes had been taken.\n\nThat however was not the end of the story for Olivia-Rose Murphy. A year later another girl was found in a similar state back in the city Olivia-Rose lived in. It was the girl who had started the rumors in the first place. And a few weeks after that a boy was found. One of her bullies. And then another, each time the victim ending up with the same broken arm and leg and missing their right eye with marks indicating that they had been attacked by birds. It was clear that Olivia-Rose and her crow were hunting people from beyond the grave. After all her bullies were dead however her curse didn't stop. Olivia-Rose still wanted a new eye to replace the one she had lost, and was willing to take it from anyone she could. So each year the curse starts again, and this letter marks the recipient as cursed by Olivia-Rose.\n\nThe only way to break the curse is to pass it onto another. So forward this Letter in the next hour, or a grizzly fate will befall you at midnight tonight.")
  
  $ subject = "FW:FW:FW:Olivia-Rose Murphy"
  $ replylabel =  "lbl_Email_ChainLetter_reply"         
  $ forwardlabel =  "lbl_Email_ChainLetter_forward"       
  $ add_message(subject, 'Belle', list(Email_ChainLetter_replyList), replylabel, forwardlabel)
  #$ add_now()
  
  return
  
label lbl_Email_ChainLetter_reply(current_message):
    menu: 
        "What is this?":  
                      
          $ replyMessage = "What is this? Some prank or something?"
        
          $SendMessages = list(Email_ChainLetter_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Belle', 'Bob', 'RE:Favor', SendMessages)
          
          if _return == 'Send':   
            $Email_ChainLetter_replyList.append(replyMessage)
            
            $response = "...I'm Sorry.\nB."            
            $Email_ChainLetter_replyList.append(response)
            
            $ subject = "RE:RE:FW:FW:FW:Olivia-Rose Murphy" 
            $ replylabel = None
            $ add_message(subject, 'Belle', list(Email_ChainLetter_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            #$ add_now()
        
        "I didn't realize you were into this sort of thing.": 
              
          $ replyMessage = "Hi Belle, \nI don't think we ever got to talk much, but i hadn't pegged you as the type to follow instructions on chain letters. lol\n\nRegards,\nBob"
        
          $SendMessages = list(Email_ChainLetter_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Belle', 'Bob', 'RE:Favor', SendMessages)
          
          if _return == 'Send':  
            $Email_ChainLetter_replyList.append(replyMessage)
            
            $response = "There are so many things in the world that we do not understand, you'd do well to be wary at times.\nB."            
            $Email_ChainLetter_replyList.append(response)
            
            $ subject = "RE:RE:FW:FW:FW:Olivia-Rose Murphy" 
            $ replylabel = None
            $ add_message(subject, 'Belle', list(Email_ChainLetter_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            #$ add_now()  
        "Don't reply yet.":
          pass 
          
    return
    
label lbl_Email_ChainLetter_forward(current_message):
  $ contacts = []   
  if not forward_Curse_Dave:
    $ Contact_Dave = Contact("Dave", "lbl_Email_ChainLetter_forward_dave")
  if not forward_Curse_Anne:
    $ Contact_Anne = Contact("Anne", "lbl_Email_ChainLetter_forward_anne")
  call screen contacts(current_message, True)
  $result = _return
  #"test = [result]"
  #$current_message.updateReplyLabel(_return)
  $forwarding_email_flag = True
  $current_message.callForward(_return);
  
  $forwarding_email_flag = False
  #"forwarding over"
  #call expression result pass (current_message)
  #$current_message.forward_screen = False          
  return

label lbl_Email_ChainLetter_forward_anne(current_message):
    menu: 
        "Hey, Check this out.":  
                      
          $ replyMessage = "Have you seen this one before?\n\nBob"
        
          $SendMessages = list(Email_ChainLetter_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Anne', 'Bob', 'FW:Olivia-Rose Murphy', SendMessages)
          
          if _return == 'Send': 
            $forward_Curse_Anne = True
            $Email_ChainLetter_replyList.append(replyMessage)
            
            $response = "Delivery to the following recipient has failed:\n\n  annabanana99@gmail.com\n\nWe tried to deliver your message but the following error was returned from the receiving server:\nError 550-5.1.1 The email account has been TEMPORARILY LOCKED. "            
            $Email_ChainLetter_replyList.append(response)
            
            $ subject = "RE:FW:Olivia-Rose Murphy" 
            $ replylabel = None #"lbl_Email_ChainLetter_forward_dave_1a"
            $ add_message(subject, 'Anne', list(Email_ChainLetter_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            #$ add_now()
        "Don't reply yet.":
          pass 
          
    return
label lbl_Email_ChainLetter_forward_dave(current_message):
    menu: 
        "Hey, Check this out.":  
                      
          $ replyMessage = "Have you seen this one before?\n\nBob"
        
          $SendMessages = list(Email_ChainLetter_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'FW:Olivia-Rose Murphy', SendMessages)
          
          if _return == 'Send':   
            $forward_Curse_Dave = True
            $Email_ChainLetter_replyList.append(replyMessage)
            
            $response = "I mean I'm hardly the expert on the occult, but it looks like some angsty teens creative writing attempt.\n\nDave"            
            $Email_ChainLetter_replyList.append(response)
            
            $ subject = "RE:FW:Olivia-Rose Murphy" 
            $ replylabel = None #"lbl_Email_ChainLetter_forward_dave_1a"
            $ add_message(subject, 'Dave', list(Email_ChainLetter_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            #$ add_now()
        
        "BeWarE oF tHe CuRSe~": 
              
          $ replyMessage = "So sorry but I'm not taking any chances this close to Halloween, this curse is yours my friend.\n\nBest of Luck,\nBob"
        
          $SendMessages = list(Email_ChainLetter_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'BeWarE oF tHe CuRSe~', SendMessages)
          
          if _return == 'Send':  
            $forward_Curse_Dave = True
            $Email_ChainLetter_replyList.append(replyMessage)
            
            $response = "Wow thats cold af man. If I die I need you to delete my browser history.\nLast thing i need is people finding out just how mundane my fetishes are. Gotta have some mystery, you know?\n\nDave"            
            $Email_ChainLetter_replyList.append(response)
            
            $ subject = "RE:BeWarE oF tHe CuRSe~" 
            $ replylabel = "lbl_Email_ChainLetter_forward_dave_1b"
            $ add_message(subject, 'Dave', list(Email_ChainLetter_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            #$ add_now()  
        "Don't reply yet.":
          pass 
          
    return
    

  
label lbl_Email_ChainLetter_forward_dave_1b(current_message):
    menu: 
        "TMI":  
                      
          $ replyMessage = "TMI dude."
        
          $SendMessages = list(Email_ChainLetter_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Belle', 'Bob', 'RE:RE:BeWarE oF tHe CuRSe~', SendMessages)
          
          if _return == 'Send':   
            $Email_ChainLetter_replyList.append(replyMessage)
            
            $response = ";)"            
            $Email_ChainLetter_replyList.append(response)
            
            $ subject = "RE:RE:RE:BeWarE oF tHe CuRSe~" 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_ChainLetter_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            #$ add_now() 
            
        "And here I thought you were freaky.":  
                      
          $ replyMessage = "And here I thought you were the freaky one who was into all the weird stuff."
        
          $SendMessages = list(Email_ChainLetter_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:BeWarE oF tHe CuRSe~', SendMessages)
          
          if _return == 'Send':   
            $Email_ChainLetter_replyList.append(replyMessage)
            
            $response = "Not yet, but who knows what the future holds?"            
            $Email_ChainLetter_replyList.append(response)
            
            $ subject = "RE:RE:RE:BeWarE oF tHe CuRSe~" 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_ChainLetter_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            #$ add_now() 
        "Don't reply yet.":
          pass 
          
    return
##-----------------------------------------------------------------------


##Dave Emails##

#Dude answer your phone!
  
##-----------------------------
label lbl_Email_Dave_Phone_start():
  call lbl_Email_Dave_Phone() from _call_lbl_Email_Dave_Phone
  return
  
label lbl_Email_Dave_Phone():
  $Email_Dave_Phone_replyList = []

  $Email_Dave_Phone_replyList.append("Stop ignoring my texts.\nDave")
  
  $ subject = "Dude answer your phone!"
  $ replylabel =  "lbl_Email_Dave_Phone_reply_1"        
  $ forwardlabel =  None    
  $ add_later(subject, 'Dave', list(Email_Dave_Phone_replyList), replylabel, forwardlabel)
  #$ add_now()
  
  return

label lbl_Email_Dave_Phone_reply_1(current_message):
    menu: 
        "Its broken.":  
                      
          $ replyMessage = "I already told you that it was broken. I can't use it until the screen is fixed. Thats why i told you to email me if you needed anything.\nBob"
        
          $SendMessages = list(Email_Dave_Phone_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Belle', 'Bob', 'RE:Dude answer your phone!', SendMessages)
          
          if _return == 'Send':  
            $email_response_dave1 = True
            $Email_Dave_Phone_replyList.append(replyMessage)
            
            $response = "Oh right. Can't you just buy a new one?"            
            $Email_Dave_Phone_replyList.append(response)
            
            $ subject = "RE:RE:Dude answer your phone!" 
            $ replylabel = "lbl_Email_Dave_Phone_reply_1a"
            $ add_later(subject, 'Dave', list(Email_Dave_Phone_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            #$ add_now() 
            
        "Dude! You were there when I dropped it.":  
                      
          $ replyMessage = "Don't you remember? I dropped it off the balcony and the screen smashed. You were there with me!\nBob"
        
          $SendMessages = list(Email_Dave_Phone_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:Dude answer your phone!', SendMessages)
          
          if _return == 'Send':   
            $email_response_dave1 = True
            $Email_Dave_Phone_replyList.append(replyMessage)
            
            $response = "HAHAHA YES! You were trying to impress Ryley with your phone flipping skills and you flung it off the balcony.\nDid you get a Phone number?\nDave"            
            $Email_Dave_Phone_replyList.append(response)
            
            $ subject = "RE:RE:Dude answer your phone!" 
            $ replylabel = "lbl_Email_Dave_Phone_reply_1b"
            $ add_later(subject, 'Dave', list(Email_Dave_Phone_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            #$ add_now() 
        "Don't reply yet.":
          pass 
          
    return
    
label lbl_Email_Dave_Phone_reply_1a(current_message):
    menu: 
        "Its too expensive":  
                      
          $ replyMessage = "With what money? Anyways its just the screen, the person at the shop said it was easy to replace it's just gonna take a few days. Much cheaper than getting a new phone.\nBob"
        
          $SendMessages = list(Email_Dave_Phone_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Belle', 'Bob', 'RE:RE:Dude answer your phone!', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Phone_replyList.append(replyMessage)
            
            $response = "With what money? I mean eating is optional right? :D"            
            $Email_Dave_Phone_replyList.append(response)
            
            $ subject = "RE:RE:RE:Dude answer your phone!" 
            $ replylabel = None
            $ add_later(subject, 'Dave', list(Email_Dave_Phone_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "I like my old phone though.":  
                      
          $ replyMessage = "I like my old phone though. And getting a phone set up just the way i like it is a lot of work so I'd rather get it fixed if possible. Anyways the person at the shop said it was easy to replace it's just gonna take a few days. Much cheaper than getting a new phone.\nBob"
        
          $SendMessages = list(Email_Dave_Phone_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:Dude answer your phone!', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Phone_replyList.append(replyMessage)
            
            $response = "I guess i can relate to that. If i lost the high scores on my games I'd be devastated."            
            $Email_Dave_Phone_replyList.append(response)
            
            $ subject = "RE:RE:RE:Dude answer your phone!" 
            $ replylabel = None
            $ add_later(subject, 'Dave', list(Email_Dave_Phone_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return
    
label lbl_Email_Dave_Phone_reply_1b(current_message):
    menu: 
        "ON WHAT PHONE?!":  
                      
          $ replyMessage = "ON WHAT PHONE?! Not to mention I was so embarrassed I could barely keep the conversation going never mind working up the courage to ask for it.\nBob"
        
          $SendMessages = list(Email_Dave_Phone_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Belle', 'Bob', 'RE:RE:Dude answer your phone!', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Phone_replyList.append(replyMessage)
            
            $response = "Pssh! I guarantee that nobody remembers it anymore. Either way don't give up yet. I'm pretty sure i saw some sparks there that night.\nDave"            
            $Email_Dave_Phone_replyList.append(response)
            
            $ subject = "RE:RE:RE:Dude answer your phone!" 
            $ replylabel = "lbl_Email_Dave_Phone_reply_1c"
            $ add_later(subject, 'Dave', list(Email_Dave_Phone_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return
    
label lbl_Email_Dave_Phone_reply_1c(current_message):
    menu: 
        "Really?":  
                      
          $ replyMessage = "Really? I'm surprised you remember anything, you were pretty wasted that night.\nBob"
        
          $SendMessages = list(Email_Dave_Phone_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Belle', 'Bob', 'RE:RE:RE:Dude answer your phone!', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Phone_replyList.append(replyMessage)
            
            $response = "For sure. Don't worry ill get you the number. I mean whats a wingman for?\n\nAlso I can hold my alcohol. Better than you can hold your phone at least. ;D\nDave"            
            $Email_Dave_Phone_replyList.append(response)
            
            $ subject = "RE:RE:RE:RE:Dude answer your phone!" 
            $ replylabel = "lbl_Email_Dave_Phone_reply_1d"
            $ add_later(subject, 'Dave', list(Email_Dave_Phone_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return
    
label lbl_Email_Dave_Phone_reply_1d(current_message):
    menu: 
        "Go to hell.":  
                      
          $ replyMessage = "Go to hell asshole. lol.\nBob"
        
          $SendMessages = list(Email_Dave_Phone_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Belle', 'Bob', 'RE:RE:RE:RE:Dude answer your phone!', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Phone_replyList.append(replyMessage)
            
            $response = "They'd only send me back.\nDave"            
            $Email_Dave_Phone_replyList.append(response)
            
            $ subject = "RE:RE:RE:RE:RE:Dude answer your phone!" 
            $ replylabel = None
            $ add_later(subject, 'Dave', list(Email_Dave_Phone_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return
##-----------------------------
#one of those days lol

label lbl_Email_Dave_Days_start():
  call lbl_Email_Dave_Days() from _call_lbl_Email_Dave_Days
  return
  
label lbl_Email_Dave_Days():
  $Email_Dave_Days_replyList = []

  $Email_Dave_Days_replyList.append("Went to take a drink of my coffee and the handle snapped off in my hand. Coffee everywhere. Total disaster.\nDave")
  
  $ subject = "One of those days lol"
  $ replylabel =  "lbl_Email_Dave_Days_reply_1"        
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Days_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return

label lbl_Email_Dave_Days_reply_1(current_message):
    menu: 
        "You Ok?":  
                      
          $ replyMessage = "You Ok? Last time I spilled coffee on myself it stung for days. :(\nBob"
        
          $SendMessages = list(Email_Dave_Days_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Belle', 'Bob', 'RE:One of those days lol', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Days_replyList.append(replyMessage)
            
            $response = "Oh no, it had been sitting for like an hour so it wasn't hot. Just a pain to clean up since it went everywhere. It was practically a full mug since I forgot I had made it.\nDave"            
            $Email_Dave_Days_replyList.append(response)
            
            $ subject = "RE:RE:One of those days lol" 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Days_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "Wow. Thats unlucky.":  
                      
          $ replyMessage = "Wow. Thats unlucky. Hope you didn't spill it on anything expensive. lol\nBob"
        
          $SendMessages = list(Email_Dave_Days_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:One of those days lol', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Days_replyList.append(replyMessage)
            
            $response = "Just my own priceless self. :("            
            $Email_Dave_Days_replyList.append(response)
            
            $ subject = "RE:RE:One of those days lol" 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Days_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return
##-----------------------------
#Going to the party?

label lbl_Email_Dave_Party_start():
  call lbl_Email_Dave_Party() from _call_lbl_Email_Dave_Party
  return
  
label lbl_Email_Dave_Party():
  $Email_Dave_Party_replyList = []

  $Email_Dave_Party_replyList.append("You going to the party? Derek is kind of weird but he knows how to throw a Party. \nDave")
  
  $ subject = "You Going?"
  $ replylabel =  "lbl_Email_Dave_Party_reply_1"        
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Party_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return

label lbl_Email_Dave_Party_reply_1(current_message):
    menu: 
        "Ehhh, dunno if i could be bothered.":  
                      
          $ replyMessage = "Ehhh, dunno if i could be bothered.\nBob"
        
          $SendMessages = list(Email_Dave_Party_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:You Going?', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Party_replyList.append(replyMessage)
            
            $response = "Come on man. You know who will be there for sure.\nDave"            
            $Email_Dave_Party_replyList.append(response)
            
            $ subject = "RE:RE:You Going?" 
            $ replylabel = "lbl_Email_Dave_Party_reply_1a"
            $ add_message(subject, 'Dave', list(Email_Dave_Party_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "I've nothing better to do i suppose.":  
                      
          $ replyMessage = "Sweet! Do you already have a costume, or are you gonna throw something together last second like last year?\nBob"
        
          $SendMessages = list(Email_Dave_Party_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:You Going?', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Party_replyList.append(replyMessage)
            
            $response = "Just my own priceless self. :("            
            $Email_Dave_Party_replyList.append(response)
            
            $ subject = "RE:RE:You Going?" 
            $ replylabel = "lbl_Email_Dave_Party_reply_1b"
            $ add_message(subject, 'Dave', list(Email_Dave_Party_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

label lbl_Email_Dave_Party_reply_1a(current_message):
    menu: 
        "Even less reason to go.":  
                      
          $ replyMessage = "Even less reason to go. After last time, how am I supposed to face them?\nBob"
        
          $SendMessages = list(Email_Dave_Party_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:You Going?', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Party_replyList.append(replyMessage)
            
            $response = "Don't be so hard on yourself. This will be your chance to make up for your goof last time.\nDave"            
            $Email_Dave_Party_replyList.append(response)
            
            $ subject = "RE:RE:RE:You Going?" 
            $ replylabel = "lbl_Email_Dave_Party_reply_1c"
            $ add_message(subject, 'Dave', list(Email_Dave_Party_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "Wait, who?":  
                      
          $ replyMessage = "Dude, really? Ryley obviously. This will be your chance to make up for your goof last time.\nBob"
        
          $SendMessages = list(Email_Dave_Party_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:You Going?', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Party_replyList.append(replyMessage)
            
            $response = "Just my own priceless self. :("            
            $Email_Dave_Party_replyList.append(response)
            
            $ subject = "RE:RE:RE:You Going?" 
            $ replylabel = "lbl_Email_Dave_Party_reply_1c"
            $ add_message(subject, 'Dave', list(Email_Dave_Party_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

label lbl_Email_Dave_Party_reply_1b(current_message):
    menu: 
        "Why mess with tradition?":  
                      
          $ replyMessage = "Why mess with tradition? People loved my rendition of \'Homeless Bob\' last year. \nBob"
        
          $SendMessages = list(Email_Dave_Party_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:You Going?', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Party_replyList.append(replyMessage)
            
            $response = "Don't forget \'Student Bob\' from the year before.\nSeriously though, would it kill you to put a little effort into it?\nDave"            
            $Email_Dave_Party_replyList.append(response)
            
            $ subject = "RE:RE:RE:You Going?" 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Party_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "I have an idea...":  
                      
          $ replyMessage = "Actually i do have an idea this time. But i won't tell you what it is in case it doesn't work out.\nBob"
        
          $SendMessages = list(Email_Dave_Party_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:You Going?', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Party_replyList.append(replyMessage)
            
            $response = "I swear if you come to another party as \'Homeless Bob\', I'm going to pretend i don't know you.\nDave"            
            $Email_Dave_Party_replyList.append(response)
            
            $ subject = "RE:RE:RE:You Going?" 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Party_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return
label lbl_Email_Dave_Party_reply_1c(current_message):
    menu: 
        "Well i can't make it any worse.":  
                      
          $ replyMessage = "Well i can't make it any worse.\nBob"
        
          $SendMessages = list(Email_Dave_Party_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:RE:You Going?', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Party_replyList.append(replyMessage)
            
            $response = "Famous last words.\n\nSorry sorry, i couldn't help it. It'll be fine, don't worry.\nDave"            
            $Email_Dave_Party_replyList.append(response)
            
            $ subject = "RE:RE:RE:RE:You Going?" 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Party_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "Yeah, this might be my chance.":  
                      
          $ replyMessage = "Yeah, this might be my chance!\nBob"
        
          $SendMessages = list(Email_Dave_Party_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:RE:You Going?', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Party_replyList.append(replyMessage)
            
            $response = "Thats the spirit. Cool and confident. Ryley wont know what hit 'em.\nDave"            
            $Email_Dave_Party_replyList.append(response)
            
            $ subject = "RE:RE:RE:RE:You Going?" 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Party_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return
    
##-----------------------------
#Bannister is being a real dick.

label lbl_Email_Dave_Bannister_start():
  call lbl_Email_Dave_Bannister() from _call_lbl_Email_Dave_Bannister
  return
  
label lbl_Email_Dave_Bannister():
  $Email_Dave_Bannister_replyList = []

  $Email_Dave_Bannister_replyList.append("Asked for an extension since the emails were down and i had my work saved to my drafts. Basically told me to take a hike. Now i have to do it over from scratch in order to be done in time to hand it on on Monday. \nDave")
  
  $ subject = "Bannister is being a real dick."
  $ replylabel =  "lbl_Email_Dave_Bannister_reply_1"        
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Bannister_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return

label lbl_Email_Dave_Bannister_reply_1(current_message):
    menu: 
        "He's always been a hard ass.":  
                      
          $ replyMessage = "He's always been a hard ass. I always try to have my stuff in early for him so i don't have to deal with him.\nBob"
        
          $SendMessages = list(Email_Dave_Bannister_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:Bannister is being a real dick.', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Bannister_replyList.append(replyMessage)
            
            $response = "Its like he thinks hes Gods gift to teaching or something. Like you couldn't find someone on the internet teaching the same thing twice as well for free.\nUniversity is such a scam.\nDave"         
            
            $Email_Dave_Bannister_replyList.append(response)
            
            $ subject = "RE:RE:Bannister is being a real dick." 
            $ replylabel = "lbl_Email_Dave_Bannister_reply_1a"
            $ add_message(subject, 'Dave', list(Email_Dave_Bannister_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "There's two types of teachers.":  
                      
          $ replyMessage = "Yeah i saw the email he sent out to everyone. Compared to the one that Dr. Marshall sent out its like night a day. There's two types of teachers I guess.\nBob"
        
          $SendMessages = list(Email_Dave_Bannister_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:Bannister is being a real dick.', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Bannister_replyList.append(replyMessage)
            
            $response = "Oh I love Marshalls class, she gets so excited about teaching it that its hard not to to get secondary excitement from it. lol\nDave"            
            $Email_Dave_Bannister_replyList.append(response)
            
            $ subject = "RE:RE:Bannister is being a real dick." 
            $ replylabel = "lbl_Email_Dave_Bannister_reply_1b"
            $ add_message(subject, 'Dave', list(Email_Dave_Bannister_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

label lbl_Email_Dave_Bannister_reply_1a(current_message):
    menu: 
        "But you gotta have it":  
                      
          $ replyMessage = "Preaching to the choir on that one, but since its the first check box on most job applications these days we don't really have much choice. \nBob"
        
          $SendMessages = list(Email_Dave_Bannister_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:Bannister is being a real dick.', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Bannister_replyList.append(replyMessage)
            
            $response = "Jumping through hoops like seals. Practice for corporate life i suppose.\nDave"         
            
            $Email_Dave_Bannister_replyList.append(response)
            
            $ subject = "RE:RE:RE:Bannister is being a real dick." 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Bannister_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "Think of it as expensive networking.":  
                      
          $ replyMessage = "Yeah its less about the teaching as it is about the Networking. Between making contacts with people you got to school with and the industry links the University has.\nBob"
        
          $SendMessages = list(Email_Dave_Bannister_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:Bannister is being a real dick.', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Bannister_replyList.append(replyMessage)
            
            $response = "Yeah, after all where would you be if you hadn't met me?\nDave"            
            $Email_Dave_Bannister_replyList.append(response)
            
            $ subject = "RE:RE:RE:Bannister is being a real dick." 
            $ replylabel = "lbl_Email_Dave_Bannister_reply_1c"
            $ add_message(subject, 'Dave', list(Email_Dave_Bannister_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

label lbl_Email_Dave_Bannister_reply_1b(current_message):
    menu: 
        "Yeah i love that class too!":  
                      
          $ replyMessage = "Its also nice that asking questions doesn't get you Bannisters signature look of scorn.\nBob"
        
          $SendMessages = list(Email_Dave_Bannister_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:Bannister is being a real dick.', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Bannister_replyList.append(replyMessage)
            
            $response = "I KNOW. Dr. Ball-Breaker more like. \nDave"         
            
            $Email_Dave_Bannister_replyList.append(response)
            
            $ subject = "RE:RE:RE:Bannister is being a real dick." 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Bannister_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "Maybe we could have her teach Bannister.":  
                      
          $ replyMessage = "Maybe we could have her teach Bannister. See if he catches some enthusiasm. lol\nBob"
        
          $SendMessages = list(Email_Dave_Bannister_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:Bannister is being a real dick.', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Bannister_replyList.append(replyMessage)
            
            $response = "Lets not risk it. He'd probably suck all the enthusiasm out, like some kind of fun vampire, and leave none left for the rest of us.\nDave"            
            $Email_Dave_Bannister_replyList.append(response)
            
            $ subject = "RE:RE:RE:Bannister is being a real dick." 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Bannister_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

label lbl_Email_Dave_Bannister_reply_1c(current_message):
    menu: 
        "Probably ruling the world.":  
                      
          $ replyMessage = "Probably ruling the world. Really you've been holding me back all this time.\nBob"
        
          $SendMessages = list(Email_Dave_Bannister_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:RE:Bannister is being a real dick.', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Bannister_replyList.append(replyMessage)
            
            $response = "Well then i hope the world thanks me. They don't want a Tyrant like you running the show anyways.\nDave"         
            
            $Email_Dave_Bannister_replyList.append(response)
            
            $ subject = "RE:RE:RE:RE:Bannister is being a real dick." 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Bannister_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "In the same place.":  
                      
          $ replyMessage = "No change, I'd be right here in the same place. \n\nOf course it wouldn't be nearly as interesting if I was by myself. \nBob"
        
          $SendMessages = list(Email_Dave_Bannister_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:RE:Bannister is being a real dick.', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Bannister_replyList.append(replyMessage)
            
            $response = "You had me in the first half. Not gonna lie. \nDave"            
            $Email_Dave_Bannister_replyList.append(response)
            
            $ subject = "RE:RE:RE:Bannister is being a real dick." 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Bannister_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

##-----------------------------
#You know that feeling when someone is watching you?

label lbl_Email_Dave_Feeling_start():
  call lbl_Email_Dave_Feeling() from _call_lbl_Email_Dave_Feeling
  return
  
label lbl_Email_Dave_Feeling():
  $Email_Dave_Feeling_replyList = []

  $Email_Dave_Feeling_replyList.append("You know that feeling when someone is watching you? \nWell not exactly that but like when you're working and theres someone standing over your shoulder, and after a while you're not sure if they're still there or not, and it kinda freaks you out? \nDave")
  
  $ subject = "You know that feeling when someone is watching you?"
  $ replylabel =  "lbl_Email_Dave_Feeling_reply_1"        
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Feeling_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return

label lbl_Email_Dave_Feeling_reply_1(current_message):
    menu: 
        "What about it?":  
                      
          $ replyMessage = "Yeah i think i know what you mean. What about it?\nBob"
        
          $SendMessages = list(Email_Dave_Feeling_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:You know that feeling when someone is watching you?', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Feeling_replyList.append(replyMessage)
            
            $response = "Its super weird. But I'm here alone and I'm getting that feeling every so often. lol \nDave"            
            $Email_Dave_Feeling_replyList.append(response)
            
            $ subject = "RE:RE:You know that feeling when someone is watching you?" 
            $ replylabel = "lbl_Email_Dave_Feeling_reply_1a"
            $ add_message(subject, 'Dave', list(Email_Dave_Feeling_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "Oh God, I Hate that.":  
                      
          $ replyMessage = "Oh God, I Hate that. I'm getting goosebumps just thinking about it. lol\nBob"
        
          $SendMessages = list(Email_Dave_Feeling_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:You know that feeling when someone is watching you?', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Feeling_replyList.append(replyMessage)
            
            $response = "Yeah lol. I keep wanting to turn around and look behind me even though I know im here alone. lol"            
            $Email_Dave_Feeling_replyList.append(response)
            
            $ subject = "RE:RE:You know that feeling when someone is watching you?" 
            $ replylabel = "lbl_Email_Dave_Feeling_reply_1a"
            $ add_message(subject, 'Dave', list(Email_Dave_Feeling_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

label lbl_Email_Dave_Feeling_reply_1a(current_message):
    menu: 
        "You're alone?":  
                      
          $ replyMessage = "You're alone? I thought you were staying with your parents?\nBob"
        
          $SendMessages = list(Email_Dave_Feeling_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:You know that feeling when someone is watching you?', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Feeling_replyList.append(replyMessage)
            
            $response = "Oh yeah I was, But i got roped into house-sitting for my cousin while they're away for the weekend.  \nDave"            
            $Email_Dave_Feeling_replyList.append(response)
            
            $ subject = "RE:RE:RE:You know that feeling when someone is watching you?" 
            $ replylabel = "lbl_Email_Dave_Feeling_reply_1b"
            $ add_message(subject, 'Dave', list(Email_Dave_Feeling_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

label lbl_Email_Dave_Feeling_reply_1b(current_message):
    menu: 
        "Wait, is that the one that lives near here?":  
                      
          $ replyMessage = "Wait, is that the one that lives near here?\nBob"
        
          $SendMessages = list(Email_Dave_Feeling_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:RE:You know that feeling when someone is watching you?', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Feeling_replyList.append(replyMessage)
            
            $response = "Yeah. You should call over sometime. They're got a bunch of game systems here. \nDave"            
            $Email_Dave_Feeling_replyList.append(response)
            
            $ subject = "RE:RE:RE:RE:You know that feeling when someone is watching you?" 
            $ replylabel = "lbl_Email_Dave_Feeling_reply_1d"
            $ add_message(subject, 'Dave', list(Email_Dave_Feeling_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Hope you're being paid!":  
                      
          $ replyMessage = "So much for a peaceful weekend. Hope you're at least getting paid for it. lol\nBob"
        
          $SendMessages = list(Email_Dave_Feeling_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:RE:You know that feeling when someone is watching you?', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Feeling_replyList.append(replyMessage)
            
            $response = "\"Do it for the family blah blah blah.\" So yeah, doing this one pro bono. :( Maybe you can come hang out for a bit? Ease the boredom a little.\nDave"            
            $Email_Dave_Feeling_replyList.append(response)
            
            $ subject = "RE:RE:RE:RE:You know that feeling when someone is watching you?" 
            $ replylabel = "lbl_Email_Dave_Feeling_reply_1d"
            $ add_message(subject, 'Dave', list(Email_Dave_Feeling_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

label lbl_Email_Dave_Feeling_reply_1d(current_message):
    menu: 
        "I'd have to walk though. :(":  
                      
          $ replyMessage = "Spending a day playing games does sound enticing. I'd have to walk though. :(\nBob"
        
          $SendMessages = list(Email_Dave_Feeling_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:RE:RE:You know that feeling when someone is watching you?', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Feeling_replyList.append(replyMessage)
            
            $response = "It'll do you good. Better get to using those legs before you forget how they work. :D \nDave"            
            $Email_Dave_Feeling_replyList.append(response)
            
            $ subject = "RE:RE:RE:RE:RE:You know that feeling when someone is watching you?" 
            $ replylabel = "lbl_Email_Dave_Feeling_reply_1e"
            $ add_message(subject, 'Dave', list(Email_Dave_Feeling_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Maybe after I'm done studying.":  
                      
          $ replyMessage = "Maybe I'll head over after I'm done studying.\nBob"
        
          $SendMessages = list(Email_Dave_Feeling_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:RE:RE:You know that feeling when someone is watching you?', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Feeling_replyList.append(replyMessage)
            
            $response = "Fffffffffff- I should be working on the stupid assignment for Bannister. Rain check on the visit then.\nDave"            
            $Email_Dave_Feeling_replyList.append(response)
            
            $ subject = "RE:RE:RE:RE:RE:You know that feeling when someone is watching you?" 
            $ replylabel = "lbl_Email_Dave_Feeling_reply_1f"
            $ add_message(subject, 'Dave', list(Email_Dave_Feeling_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

label lbl_Email_Dave_Feeling_reply_1e(current_message):
    menu: 
        "Maybe after I'm done studying.":  
                      
          $ replyMessage = "Maybe I'll head over after I'm done studying then.\nBob"
        
          $SendMessages = list(Email_Dave_Feeling_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:RE:RE:You know that feeling when someone is watching you?', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Feeling_replyList.append(replyMessage)
            
            $response = "Fffffffffff- I should be working on the stupid assignment for Bannister. Rain check on the visit then.\nDave"            
            $Email_Dave_Feeling_replyList.append(response)
            
            $ subject = "RE:RE:RE:RE:RE:You know that feeling when someone is watching you?" 
            $ replylabel = "lbl_Email_Dave_Feeling_reply_1f"
            $ add_message(subject, 'Dave', list(Email_Dave_Feeling_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

label lbl_Email_Dave_Feeling_reply_1f(current_message):
    menu: 
        "Sunday then?":  
                      
          $ replyMessage = "Sunday then? Assuming you get your assignment finished in time. lol\nBob"
        
          $SendMessages = list(Email_Dave_Feeling_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:RE:RE:You know that feeling when someone is watching you?', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Feeling_replyList.append(replyMessage)
            
            $response = "Its a date. ;) \nDave"            
            $Email_Dave_Feeling_replyList.append(response)
            
            $ subject = "RE:RE:RE:RE:RE:You know that feeling when someone is watching you?" 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Feeling_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Good Luck with the assignment":  
                      
          $ replyMessage = "Good Luck with the assignment. Last thing you need is to be on Bannisters shit list.\nBob"
        
          $SendMessages = list(Email_Dave_Feeling_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:RE:RE:RE:You know that feeling when someone is watching you?', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Feeling_replyList.append(replyMessage)
            
            $response = "Don't i know it. :(\nDave"            
            $Email_Dave_Feeling_replyList.append(response)
            
            $ subject = "RE:RE:RE:RE:RE:You know that feeling when someone is watching you?" 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Feeling_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return
##-----------------------------
#These birds are creeping me out.

label lbl_Email_Dave_Birds_start():
  call lbl_Email_Dave_Birds() from _call_lbl_Email_Dave_Birds
  return
  
label lbl_Email_Dave_Birds():
  $Email_Dave_Birds_replyList = []

  $Email_Dave_Birds_replyList.append("These Birds man. I mean theres always been birds around here, but i never looked outside and felt like they were staring at me. \nDave")
  
  $ subject = "These birds are creeping me out."
  $ replylabel =  "lbl_Email_Dave_Birds_reply_1"        
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Birds_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return

label lbl_Email_Dave_Birds_reply_1(current_message):
    menu: 
        "Have you been sleeping alright recently?":  
                      
          $ replyMessage = "That sounds pretty crazy. lol \nHave you been sleeping alright recently?\nBob"
        
          $SendMessages = list(Email_Dave_Birds_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:These birds are creeping me out.', SendMessages)
          
          if _return == 'Send':   
            $email_response_dave2 = True
            $Email_Dave_Birds_replyList.append(replyMessage)
            
            $response = "I mean i was up to 2am binge watching the last few episodes of that new show. But thats nothing unusual. lol\nDave"            
            $Email_Dave_Birds_replyList.append(response)
            
            $ subject = "RE:RE:These birds are creeping me out." 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Birds_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "Birds are surprisingly smart.":  
                      
          $ replyMessage = "Birds are surprisingly smart. Maybe they know you have food or something. lol\nBob"
        
          $SendMessages = list(Email_Dave_Birds_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:These birds are creeping me out.', SendMessages)
          
          if _return == 'Send':  
            $email_response_dave2 = True 
            $Email_Dave_Birds_replyList.append(replyMessage)
            
            $response = "Well they know more than me. Seems my cousin cleared the place out before he left. \nI'm watching the place for free least he could do is feed me.\nDave"            
            $Email_Dave_Birds_replyList.append(response)
            
            $ subject = "RE:RE:These birds are creeping me out." 
            $ replylabel = "lbl_Email_Dave_Birds_reply_1a"
            $ add_message(subject, 'Dave', list(Email_Dave_Birds_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

label lbl_Email_Dave_Birds_reply_1a(current_message):
    menu: 
        "You should get takeout.":  
                      
          $ replyMessage = "Well if theres no food, you should get takeout. That new Chinese place is pretty good.\nBob"
        
          $SendMessages = list(Email_Dave_Birds_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:These birds are creeping me out.', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Birds_replyList.append(replyMessage)
            
            $response = "Now theres an idea. I'll see if i can find the menu online. Any recommendations? \nDave"            
            $Email_Dave_Birds_replyList.append(response)
            
            $ subject = "RE:RE:These birds are creeping me out." 
            $ replylabel = "lbl_Email_Dave_Birds_reply_1b"
            $ add_message(subject, 'Dave', list(Email_Dave_Birds_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "The nerve of some people":  
                      
          $ replyMessage = "Rude. They probably knew there was no food when they asked you to look after the place.\nBob"
        
          $SendMessages = list(Email_Dave_Birds_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:These birds are creeping me out.', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Birds_replyList.append(replyMessage)
            
            $response = "Yeah, a heads up would've been nice. Guess ill order takeout. \nDave"            
            $Email_Dave_Birds_replyList.append(response)
            
            $ subject = "RE:RE:These birds are creeping me out." 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Birds_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

label lbl_Email_Dave_Birds_reply_1b(current_message):
    menu: 
        "How about Honey Chilly chicken?":  
                      
          $ replyMessage = "How about Honey Chilly chicken? It's probably not the best I've had but as far as places around here go its pretty good. \nBob"
        
          $SendMessages = list(Email_Dave_Birds_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:These birds are creeping me out.', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Birds_replyList.append(replyMessage)
            
            $response = "Hmm, Sounds good. And let me guess \"The place back home\" has the best Chinese food? \nDave"            
            $Email_Dave_Birds_replyList.append(response)
            
            $ subject = "RE:RE:These birds are creeping me out." 
            $ replylabel = "lbl_Email_Dave_Birds_reply_1c"
            $ add_message(subject, 'Dave', list(Email_Dave_Birds_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "The Chow mein is pretty good":  
                      
          $ replyMessage = "The Chow mein there is pretty good. \nBob"
        
          $SendMessages = list(Email_Dave_Birds_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:These birds are creeping me out.', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Birds_replyList.append(replyMessage)
            
            $response = "Ugh. I can't eat Chow mein anymore. The last time i ate it i was sick as a dog, and now even thinking about eating it turns my stomach. I'll probably just go for some sweet and sour pork like usual. \nDave"            
            $Email_Dave_Birds_replyList.append(response)
            
            $ subject = "RE:RE:These birds are creeping me out." 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Birds_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "You can't go wrong with a curry half and half":  
                      
          $ replyMessage = "You can't go wrong with a curry half and half. And they do a special with chicken balls. \nBob"
        
          $SendMessages = list(Email_Dave_Birds_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:These birds are creeping me out.', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Birds_replyList.append(replyMessage)
            
            $response = "Aw yeah. Now you're talking. The only thing better than chicken balls, is left over chicken balls the next morning. \nDave"            
            $Email_Dave_Birds_replyList.append(response)
            
            $ subject = "RE:RE:These birds are creeping me out." 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Birds_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

label lbl_Email_Dave_Birds_reply_1c(current_message):
    menu: 
        "You better believe it.":  
                      
          $ replyMessage = "You better believe it. I'm sure it beats the hell out of wherever you normally eat from. \nBob"
        
          $SendMessages = list(Email_Dave_Birds_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:These birds are creeping me out.', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Birds_replyList.append(replyMessage)
            
            $response = "Oh them's fighting words. I'm gonna take you there some day and make you eat those words, along with some delicious Chinese food. \nDave"            
            $Email_Dave_Birds_replyList.append(response)
            
            $ subject = "RE:RE:These birds are creeping me out." 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Birds_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "Almost as if we've talked about this before.":  
                      
          $ replyMessage = "Almost as if we've had this argument many times before. lol\nBob"
        
          $SendMessages = list(Email_Dave_Birds_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:These birds are creeping me out.', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Birds_replyList.append(replyMessage)
            
            $response = "Everyone always thinks the food in their home town is best. And unless they are from my town they are wrong. 8D\nDave"            
            $Email_Dave_Birds_replyList.append(response)
            
            $ subject = "RE:RE:These birds are creeping me out." 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Birds_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

##-----------------------------
#I really need some sleep ( prepherial vision )

label lbl_Email_Dave_Need_Sleep_start():
  call lbl_Email_Dave_Need_Sleep() from _call_lbl_Email_Dave_Need_Sleep
  return
  
label lbl_Email_Dave_Need_Sleep():
  $Email_Dave_Need_Sleep_replyList = []

  $Email_Dave_Need_Sleep_replyList.append("I think I'm going crazy. lol\nI keep thinking i see something off to the side, but when i look over nothing is there. Its the weirdest feeling. \nDave")
  
  $ subject = "I really need some sleep"
  $ replylabel =  "lbl_Email_Dave_Need_Sleep_reply_1"        
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Need_Sleep_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return

label lbl_Email_Dave_Need_Sleep_reply_1(current_message):
    menu: 
        "Did you take something?":  
                      
          $ replyMessage = "Are you on drugs or something? I'd have thought it would take more than a little sleep deprivation to start hallucinations. lol \nBob"
        
          $SendMessages = list(Email_Dave_Need_Sleep_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:I really need some sleep', SendMessages)
          
          if _return == 'Send':   
            $email_response_dave3 = True 
            $Email_Dave_Need_Sleep_replyList.append(replyMessage)
            
            $response = "Haha, of course not. And if it feels like that I'm not sure i want to start. \nDave"            
            $Email_Dave_Need_Sleep_replyList.append(response)
            
            $ subject = "RE:RE:I really need some sleep" 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Need_Sleep_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "You're staring to scare me.":  
                      
          $ replyMessage = "Dude. That doesn't sound good at all. Do you need to go see a doctor or something?\nBob"
        
          $SendMessages = list(Email_Dave_Need_Sleep_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:I really need some sleep', SendMessages)
          
          if _return == 'Send':  
            $email_response_dave3 = True  
            $Email_Dave_Need_Sleep_replyList.append(replyMessage)
            
            $response = "Lol, I'm fine. A little sleep and ill be right as rain.\nDave"            
            $Email_Dave_Need_Sleep_replyList.append(response)
            
            $ subject = "RE:RE:I really need some sleep" 
            $ replylabel = "lbl_Email_Dave_Need_Sleep_reply_1a"
            $ add_message(subject, 'Dave', list(Email_Dave_Need_Sleep_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "You really do!":  
                      
          $ replyMessage = "Its obviously driving you mad. lol\nBob"
        
          $SendMessages = list(Email_Dave_Need_Sleep_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:I really need some sleep', SendMessages)
          
          if _return == 'Send':  
            $email_response_dave3 = True   
            $Email_Dave_Need_Sleep_replyList.append(replyMessage)
            
            $response = "Yeah no doubt. Want to try and get this stupid assignment out of the way firs though.\nDave"            
            $Email_Dave_Need_Sleep_replyList.append(response)
            
            $ subject = "RE:RE:I really need some sleep" 
            $ replylabel = "lbl_Email_Dave_Need_Sleep_reply_1b"
            $ add_message(subject, 'Dave', list(Email_Dave_Need_Sleep_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

label lbl_Email_Dave_Need_Sleep_reply_1a(current_message):
    menu: 
        "You need to look after yourself better.":  
                      
          $ replyMessage = "You need to look after yourself better.  \nBob"
        
          $SendMessages = list(Email_Dave_Need_Sleep_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:I really need some sleep', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Need_Sleep_replyList.append(replyMessage)
            
            $response = "OK MOM. \nDave"            
            $Email_Dave_Need_Sleep_replyList.append(response)
            
            $ subject = "RE:RE:I really need some sleep" 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Need_Sleep_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "Well go to sleep then!":  
                      
          $ replyMessage = "Well go to sleep then!\nBob"
        
          $SendMessages = list(Email_Dave_Need_Sleep_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:I really need some sleep', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Need_Sleep_replyList.append(replyMessage)
            
            $response = "I will. I Will. Want to try and get this stupid assignment out of the way firs though.\nDave"            
            $Email_Dave_Need_Sleep_replyList.append(response)
            
            $ subject = "RE:RE:I really need some sleep" 
            $ replylabel = "lbl_Email_Dave_Need_Sleep_reply_1b"
            $ add_message(subject, 'Dave', list(Email_Dave_Need_Sleep_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

label lbl_Email_Dave_Need_Sleep_reply_1b(current_message):
    menu: 
        "Well good luck then!":  
                      
          $ replyMessage = "Well good luck with it then. Finish up and get some sleep man. \nBob"
        
          $SendMessages = list(Email_Dave_Need_Sleep_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:I really need some sleep', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Need_Sleep_replyList.append(replyMessage)
            
            $response = "Thats the plan chief. \nDave"            
            $Email_Dave_Need_Sleep_replyList.append(response)
            
            $ subject = "RE:RE:I really need some sleep" 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Need_Sleep_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "Can't it wait?":  
                      
          $ replyMessage = "Can't it wait? Seems like the lack of sleep is doing a number on you, are you even able to concentrate on what you're doing? \nBob"
        
          $SendMessages = list(Email_Dave_Need_Sleep_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:I really need some sleep', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Need_Sleep_replyList.append(replyMessage)
            
            $response = "Maybe i would be done already if someone stopped emailing me?!\nDave"            
            $Email_Dave_Need_Sleep_replyList.append(response)
            
            $ subject = "RE:RE:I really need some sleep" 
            $ replylabel = "lbl_Email_Dave_Need_Sleep_reply_1c"
            $ add_message(subject, 'Dave', list(Email_Dave_Need_Sleep_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

label lbl_Email_Dave_Need_Sleep_reply_1c(current_message):
    menu: 
        "Well excuuuuuuse me":  
                      
          $ replyMessage = "Well excuuuuuuse me princess. \nBob"
        
          $SendMessages = list(Email_Dave_Need_Sleep_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:I really need some sleep', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Need_Sleep_replyList.append(replyMessage)
            
            $response = "Yep, and now that we know you are to blame you can finish the assignment for me. \nDave"            
            $Email_Dave_Need_Sleep_replyList.append(response)
            
            $ subject = "RE:RE:I really need some sleep" 
            $ replylabel = "lbl_Email_Dave_Need_Sleep_reply_1d"
            $ add_message(subject, 'Dave', list(Email_Dave_Need_Sleep_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "YOU EMAILED ME!":  
                      
          $ replyMessage = "YOU EMAILED ME FIRST YOU PUNK! \nBob"
        
          $SendMessages = list(Email_Dave_Need_Sleep_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:I really need some sleep', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Need_Sleep_replyList.append(replyMessage)
            
            $response = "Me? Never. I've been framed. \nDave"            
            $Email_Dave_Need_Sleep_replyList.append(response)
            
            $ subject = "RE:RE:I really need some sleep" 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Need_Sleep_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

label lbl_Email_Dave_Need_Sleep_reply_1d(current_message):
    menu: 
        "No way":  
                      
          $ replyMessage = "No way. I already finished mine, and theres no way I'm doing it again. \nBob"
        
          $SendMessages = list(Email_Dave_Need_Sleep_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:I really need some sleep', SendMessages)
          
          if _return == 'Send':   
            $Email_Dave_Need_Sleep_replyList.append(replyMessage)
            
            $response = "Wow. So uncool. \nI guess i better get stuck into it then. :(\nDave"            
            $Email_Dave_Need_Sleep_replyList.append(response)
            
            $ subject = "RE:RE:I really need some sleep" 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Need_Sleep_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

##-----------------------------
#Ok Im going to bed.

label lbl_Email_Dave_Bed_start():
  call lbl_Email_Dave_Bed() from _call_lbl_Email_Dave_Bed
  return
  
label lbl_Email_Dave_Bed():
  $Email_Dave_Bed_replyList = []

  $Email_Dave_Bed_replyList.append("I can't focus on this work at all. Talk to you tomorrow. \nDave")
  
  $ subject = "Ok Im going to bed."
  $ replylabel =  "lbl_Email_Dave_Bed_reply_1"        
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Bed_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return

label lbl_Email_Dave_Bed_reply_1(current_message):
    menu: 
        "Heres to a good Lie-in":  
                      
          $ replyMessage = "Remember to turn your alarm off and sleep in till the afternoon. lol\nBob"
        
          $SendMessages = list(Email_Dave_Bed_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:Ok Im going to bed.', SendMessages)
          
          if _return == 'Send':   
            $email_response_dave4 = True  
            $Email_Dave_Bed_replyList.append(replyMessage)
            
            $response = "Now theres an idea.\nDave"            
            $Email_Dave_Bed_replyList.append(response)
            
            $ subject = "RE:RE:Ok Im going to bed." 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Bed_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
            
        "Yeah, get some rest.":  
                      
          $ replyMessage = "Yeah, get some rest. Sounds like you really need it.\nBob"
        
          $SendMessages = list(Email_Dave_Bed_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Dave', 'Bob', 'RE:Ok Im going to bed.', SendMessages)
          
          if _return == 'Send':   
            $email_response_dave4 = True  
            $Email_Dave_Bed_replyList.append(replyMessage)
            
            $response = "Thanks, ill talk to you Tomorrow.\nDave"            
            $Email_Dave_Bed_replyList.append(response)
            
            $ subject = "RE:RE:Ok Im going to bed." 
            $ replylabel = None
            $ add_message(subject, 'Dave', list(Email_Dave_Bed_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
            $ add_now() 
        "Don't reply yet.":
          pass 
          
    return

##-----------------------------
#Dude i cant sleep

label lbl_Email_Dave_cant_sleep_start():
  call lbl_Email_Dave_cant_sleep() from _call_lbl_Email_Dave_cant_sleep
  return
  
label lbl_Email_Dave_cant_sleep():
  $Email_Dave_cant_sleep_replyList = []

  $Email_Dave_cant_sleep_replyList.append("I can feel the birds watching me. lol \nThats crazy right?\nDave")
  
  $ subject = "Dude i cant sleep"
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_cant_sleep_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return
##-----------------------------
#Im kinda freaking out

label lbl_Email_Dave_Freaking_Out_start():
  call lbl_Email_Dave_Freaking_Out() from _call_lbl_Email_Dave_Freaking_Out
  return
  
label lbl_Email_Dave_Freaking_Out():
  $Email_Dave_Freaking_Out_replyList = []

  $Email_Dave_Freaking_Out_replyList.append("It's like all the hair on my body is standing on end. I don't like this at all.")
  
  $ subject = "I'm kinda freaking out"
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Freaking_Out_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return
##-----------------------------
#Are you awake?

label lbl_Email_Dave_You_Awake_start():
  call lbl_Email_Dave_You_Awake() from _call_lbl_Email_Dave_You_Awake
  return
  
label lbl_Email_Dave_You_Awake():
  $Email_Dave_You_Awake_replyList = []

  $Email_Dave_You_Awake_replyList.append("Are you?")
  
  $ subject = "Are you awake?"
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_You_Awake_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return
##-----------------------------
#Dude?

label lbl_Email_Dave_Dude_start():
  call lbl_Email_Dave_Dude() from _call_lbl_Email_Dave_Dude
  return
  
label lbl_Email_Dave_Dude():
  $Email_Dave_Dude_replyList = []

  $Email_Dave_Dude_replyList.append("Please respond.")
  
  $ subject = "Dude?"
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Dude_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return
##-----------------------------
#No seriously.

label lbl_Email_Dave_Seriously_start():
  call lbl_Email_Dave_Seriously() from _call_lbl_Email_Dave_Seriously
  return
  
label lbl_Email_Dave_Seriously():
  $Email_Dave_Seriously_replyList = []

  $Email_Dave_Seriously_replyList.append("Please.")
  
  $ subject = "No seriously."
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Seriously_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return
##-----------------------------
#Please respond.

label lbl_Email_Dave_Respond_start():
  call lbl_Email_Dave_Respond() from _call_lbl_Email_Dave_Respond
  return
  
label lbl_Email_Dave_Respond():
  $Email_Dave_Respond_replyList = []

  $Email_Dave_Respond_replyList.append("I can feel the birds watching me. \nDave")
  
  $ subject = "Please respond."
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Respond_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return
##-----------------------------
#I Sent it on

label lbl_Email_Dave_Sent_On_start():
  call lbl_Email_Dave_Sent_On() from _call_lbl_Email_Dave_Sent_On
  return
  
label lbl_Email_Dave_Sent_On():
  $Email_Dave_Sent_On_replyList = []

  $Email_Dave_Sent_On_replyList.append("Its that stupid email. It's freaking me out. Now its someone elses problem.")
  
  $ subject = "I Sent it on"
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Sent_On_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return
##-----------------------------
#It didn't work. I can tell.

label lbl_Email_Dave_Didnt_Work_start():
  call lbl_Email_Dave_Didnt_Work() from _call_lbl_Email_Dave_Didnt_Work
  return
  
label lbl_Email_Dave_Didnt_Work():
  $Email_Dave_Didnt_Work_replyList = []

  $Email_Dave_Didnt_Work_replyList.append("I can still feel it. I don't even know how to describe it. Its like in the air. This fucking feeling.")
  
  $ subject = "It didn't work. I can tell."
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Didnt_Work_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return
##-----------------------------
#Fuck. 

label lbl_Email_Dave_Fuck_1_start():
  call lbl_Email_Dave_Fuck_1() from _call_lbl_Email_Dave_Fuck_1
  return
  
label lbl_Email_Dave_Fuck_1():
  $Email_Dave_Fuck_1_replyList = []

  $Email_Dave_Fuck_1_replyList.append("I don't want to feel like this anymore.")
  
  $ subject = "Fuck. "
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Fuck_1_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return
##-----------------------------
#Fuck

label lbl_Email_Dave_Fuck_2_start():
  call lbl_Email_Dave_Fuck_2() from _call_lbl_Email_Dave_Fuck_2
  return
  
label lbl_Email_Dave_Fuck_2():
  $Email_Dave_Fuck_2_replyList = []

  $Email_Dave_Fuck_2_replyList.append("I tried to leave. The birds saw me. I went back inside. I had no choice.")
  
  $ subject = "Fuck. "
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Fuck_2_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return
##-----------------------------
#Fuck

label lbl_Email_Dave_Fuck_3_start():
  call lbl_Email_Dave_Fuck_3() from _call_lbl_Email_Dave_Fuck_3
  return
  
label lbl_Email_Dave_Fuck_3():
  $Email_Dave_Fuck_3_replyList = []

  $Email_Dave_Fuck_3_replyList.append("I moved the furniture to block the windows and doors. I'll feel better.")
  
  $ subject = "Fuck. "
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Fuck_3_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return
##-----------------------------
#Fuck

label lbl_Email_Dave_Fuck_4_start():
  call lbl_Email_Dave_Fuck_4() from _call_lbl_Email_Dave_Fuck_4
  return
  
label lbl_Email_Dave_Fuck_4():
  $Email_Dave_Fuck_4_replyList = []

  $Email_Dave_Fuck_4_replyList.append("I don't feel better. It wont work. I don't know how but i can feel it.")
  
  $ subject = "Fuck. "
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Fuck_4_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return
##-----------------------------
#Fuckfuckfuckfcukfcufkcukfcukfuckfuckfuckfuckfc

label lbl_Email_Dave_Fuck_5_start():
  call lbl_Email_Dave_Fuck_5() from _call_lbl_Email_Dave_Fuck_5
  return
  
label lbl_Email_Dave_Fuck_5():
  $Email_Dave_Fuck_5_replyList = []

  $Email_Dave_Fuck_5_replyList.append("STOP IGNORING ME!")
  
  $ subject = "Fuckfuckfuckfcukfcufkcukfcukfuckfuckfuckfuckfc"
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Fuck_5_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return
##-----------------------------
#fuckufckufckufkcuf

label lbl_Email_Dave_Fuck_6_start():
  call lbl_Email_Dave_Fuck_6() from _call_lbl_Email_Dave_Fuck_6
  return
  
label lbl_Email_Dave_Fuck_6():
  $Email_Dave_Fuck_6_replyList = []

  $Email_Dave_Fuck_6_replyList.append("YOU DID THIS!")
  
  $ subject = "fuckufckufckufkcuf "
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Fuck_6_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return
##-----------------------------
#kcufkucf

label lbl_Email_Dave_Fuck_7_start():
  call lbl_Email_Dave_Fuck_7() from _call_lbl_Email_Dave_Fuck_7
  return
  
label lbl_Email_Dave_Fuck_7():
  $Email_Dave_Fuck_7_replyList = []

  $Email_Dave_Fuck_7_replyList.append("I'm sorry. Please respond. I need to talk to someone.")
  
  $ subject = "kcufkucf "
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Fuck_7_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return
##-----------------------------
#kcufkucufuc

label lbl_Email_Dave_Fuck_8_start():
  call lbl_Email_Dave_Fuck_8() from _call_lbl_Email_Dave_Fuck_8
  return
  
label lbl_Email_Dave_Fuck_8():
  $Email_Dave_Fuck_8_replyList = []

  $Email_Dave_Fuck_8_replyList.append("Why won't anyone answer me. Please please please please.")
  
  $ subject = "kcufkucufuc"
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Fuck_8_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return
##-----------------------------
#I think shes here.

label lbl_Email_Dave_Here_start():
  call lbl_Email_Dave_Here() from _call_lbl_Email_Dave_Here
  return
  
label lbl_Email_Dave_Here():
  $Email_Dave_Here_replyList = []

  $Email_Dave_Here_replyList.append("")
  
  $ subject = "I think she's here."
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Here_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return
##-----------------------------



# Dave?
#Thank you.

label lbl_Email_Dave_Thanks_start():
  call lbl_Email_Thanks_Here() from _call_lbl_Email_Thanks_Here
  return
  
label lbl_Email_Thanks_Here():
  $Email_Dave_Thanks_replyList = []

  $Email_Dave_Thanks_replyList.append("I can see properly again. It is wonderful.\nThank you for your help.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\nBest Wishes,\nOlivia-Rose Murphy")
  
  $ subject = "Thank you."
  $ replylabel =  None       
  $ forwardlabel =  None    
  $ add_message(subject, 'Dave', list(Email_Dave_Thanks_replyList), replylabel, forwardlabel)
  $ add_now()
  
  return
##-----------------------------
