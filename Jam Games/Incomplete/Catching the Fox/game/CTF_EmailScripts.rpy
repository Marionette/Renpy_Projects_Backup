init python:
  EmailEnabledFlag = True
  TrinaEmail_Flag_Wedding = False
  TrinaEmail_Flag_Shop = False


label trina_draft(contact, message_title="Listen, Trina..."):
    $MessageIntro = "We seriously need to talk about..."
    menu:
        "We seriously need to talk about...Solomon":
            #$ contact.draft_label = None # must include this line for each option if you want to disable drafts for this contact
            $ draftMessage = MessageIntro + "Solomon. Specifically {i}me{/i} and Solomon. Together. \nRomantically."     
            $SendMessages = []
            $SendMessages.append(draftMessage)
            call screen send_menu('Trina', 'Simone', 'Listen, Trina...', list(SendMessages))
            
            if _return == 'Send':         
              $SendMessages.append(GetRelationshipHintEmail("Solomon", 0, 1))
              $ subject = "RE:Listen, Trina..." 
              $ replylabel = None
              $ add_message(subject, 'Trina', list(SendMessages), replylabel)
              
        "We seriously need to talk about...Milo":
            #$ contact.draft_label = None
            $message = GetRelationshipHintEmail("Milo", 0, 1)
            $ draftMessage = MessageIntro + "Milo. Specifically {i}me{/i} and Milo. Together. \nRomantically."     
            $SendMessages = []
            $SendMessages.append(draftMessage)
            call screen send_menu('Trina', 'Simone', 'Listen, Trina...', list(SendMessages))
            
            if _return == 'Send':         
              $SendMessages.append(GetRelationshipHintEmail("Solomon", 0, 1))
              $ subject = "RE:Listen, Trina..." 
              $ replylabel = None
              $ add_message(subject, 'Trina', list(SendMessages), replylabel)    
        "We seriously need to talk about...Joel":
            #$ contact.draft_label = None
            $message = GetRelationshipHintEmail("Joel", 0, 1)
            $ draftMessage = MessageIntro + "Joel. Specifically {i}me{/i} and Joel. Together. \nRomantically."     
            $SendMessages = []
            $SendMessages.append(draftMessage)
            call screen send_menu('Trina', 'Simone', 'Listen, Trina...', list(SendMessages))
            
            if _return == 'Send':         
              $SendMessages.append(GetRelationshipHintEmail("Joel", 0, 1))
              $ subject = "RE:Listen, Trina..." 
              $ replylabel = None
              $ add_message(subject, 'Trina', list(SendMessages), replylabel)    
        "Nevermind, I should write about something else.":
          menu:
            "Are you ready for the wedding?!" if TrinaEmail_Flag_Wedding == False:
              #$ contact.draft_label = None
              $ draftMessage = "All set for the big day?"     
              $SendMessages = []
              $SendMessages.append(draftMessage)
              call screen send_menu('Trina', 'Simone', 'Are you ready for the wedding?!', list(SendMessages))
              
              if _return == 'Send':          
                $TrinaEmail_Flag_Wedding = True
                $message = "Im freaking out right now. Is this normal?!"
                $SendMessages.append(message)
                $ subject = "NopeNopeNopeNopeNope" 
                $ replylabel = None
                $ add_message(subject, 'Trina', list(SendMessages), replylabel)    
            "Hows things at the shop?" if TrinaEmail_Flag_Shop == False:     
              #$ contact.draft_label = None
              $ draftMessage = "Anthing interesting happening at the shop?"     
              $SendMessages = []
              $SendMessages.append(draftMessage)
              call screen send_menu('Trina', 'Simone', 'Hows things at the shop?', list(SendMessages))
              
              if _return == 'Send':  
                $TrinaEmail_Flag_Shop = True        
                $message = "Its a coffee shop gosh darnit! Why does he keep asking for tea?!"
                $SendMessages.append(message)
                $ subject = "That Tea guy again..." 
                $ replylabel = None
                $ add_message(subject, 'Trina', list(SendMessages), replylabel)      
            "Nevermind.": 
              pass
        "Discard draft.":
            pass
    return
###################### Misc Emails #######################################
init python:
  Sample_Email_1 = ["SubjectHere", "sender@email.com", "EmailContent", "ReplyLabel" ]
  Email_Misc_MilosNumber_replyList = []
  Email_Misc_MeetingNotes_replyList = []
  stat_kindness = 0
  stat_honesty = 0
  stat_intellect = 0
  stat_dependability = 0
  stat_imagination = 0
  stat_laziness = 0
            
##------------------
  #misc functions
  #get points for character
  def GetPoints(_name):
    if _name == 'Solomon':    
      return  stat_imagination + stat_intellect + stat_honesty
    
    if _name == 'Milo':
      return stat_dependability + stat_honesty + stat_kindness
      
    if _name == 'Joel':
      return stat_kindness + stat_intellect + stat_laziness
  
##------------------

##-----------------------------------------------------------------------
label lbl_Email_Misc_MilosNumber_start():
  #From: jhiga@fspub.com
  #To: swest@fspub.com 
  #Subject: Favor
  $Email_Misc_MilosNumber_replyList = []

  $Email_Misc_MilosNumber_replyList.append("Simone, right? Welcome to the office!\nListen, I need your help. Can you send me Milo's office number?\nI need to speak with him, but I left my work phone in my desk before I left for this interview.\nSorry for the inconvenience!")
  
  $ subject = "Favor"
  $ replylabel = "lbl_Email_Misc_MilosNumber_reply"               
  $ add_message(subject, 'jhiga@fspub.com', list(Email_Misc_MilosNumber_replyList), replylabel)
  $ add_now()
  
  return


label lbl_Email_Misc_MilosNumber_reply(current_message):
    menu: 
        "I'll get it for you.": #//+Kindness   
                      
          $ replyMessage = "Thanks for the welcome.\nActually, though, I'm don't have Milo's number (or his email, yet.)\nHere's Joel's email, though!\nHe'll definitely know how to contact Milo.\n\njcabrera@fspub.com\n\nHope your interview goes well.\nSimone West"
        
          $SendMessages = list(Email_Misc_MilosNumber_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('jhiga@fspub.com', 'Simone', 'RE:Favor', SendMessages)
          
          if _return == 'Send':   
            $ stat_kindness +=1
            $Email_Misc_MilosNumber_replyList.append(replyMessage)
            
            $response = "Thanks anyway."            
            $Email_Misc_MilosNumber_replyList.append(response)
            
            $ subject = "RE:RE:Favor" 
            $ replylabel = None
            #$ add_message(subject, 'jhiga@fspub.com', list(Email_Misc_MilosNumber_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
        
        "I don't have it.": #//+Honesty
              
          $ replyMessage = "Oh, thanks for the welcome email.\nUnfortunately, I don't have Milo's number and he's out of the office at the moment.\nI don't have his email either... I could guess, but if it's sensitive information you're after, I don't want to accidentally mail the wrong person.\nSorry about all this! When he gets in, I’ll ask him to contact you.\nSimone West"
        
          $SendMessages = list(Email_Misc_MilosNumber_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('jhiga@fspub.com', 'Simone', 'RE:Favor', SendMessages)
          
          if _return == 'Send':   
            $ stat_honesty +=1
            $Email_Misc_MilosNumber_replyList.append(replyMessage)
            
            $response = "Thanks anyway."            
            $Email_Misc_MilosNumber_replyList.append(response)
            
            $ subject = "RE:RE:Favor" 
            $ replylabel = None
            #$ add_message(subject, 'jhiga@fspub.com', list(Email_Misc_MilosNumber_replyList), replylabel)
            $ current_message.reply_label = None   # must include this line for each option   
        "Don't reply yet.":
          pass 
          
    return
    
##-----------------------------------------------------------------------

label lbl_Email_Misc_JoelCorrections(contact, message_title="Corrections"):
    ##To: jcabrera@fspub.com
    ##From: swest@fspub.com
    ##Subject: Corrections
    
    ##EMAIL CONTENT##
    
    $SendMessages = []
    $ introMessage = "Joel, here's the corrections for Milo.\nMake sure to clear up that misunderstanding, alright?\n\n"
    $SendMessages.append(introMessage)
    show screen send_menuDisplay('Joel', 'Simone', 'Corrections', SendMessages)

    si "Hm..."
    
    "The corrections hadn't as bad as I thought they'd be judging by Milo's dramatics, but he definitely needs to improve if he wants to move up in the company."
    
    "Maybe I'll just add a quick note and send it."

    menu:
        
        "Link him to writing resources to help him improve.": #stat_intellect
            
            $ draftMessage = introMessage + "The quality of the content wasn't bad, but I noticed you make a lot of simple mistakes, which tells that your problem is proofreading. If you plan to become an editor one day, you'll need to pay more attention to detail, alright?\n\nHere's a few websites that helped me.\n\nSimone"
            
            $SendMessages = []
            $SendMessages.append(draftMessage)
            call screen send_menu('Joel', 'Simone', 'Corrections', SendMessages)
            
            if _return == 'Send':   
              $stat_intellect +=1    
              $ contact.draft_label = None        
                
              jump email_complete
                
        "Offer help when he needs it.": #stat_kindness
            
            $ draftMessage = introMessage + "I didn't mind helping you, by the way. It wasn't just that Milo gets on my nerves (which he does, and it's only my first day. I feel like that doesn't bode well for our work relationship.) but I also don't mind helping you out if you need it.\n\nIf you want someone to look over your proposals before you give them to Milo, I'll do it for you, no problem. I can help you out whenever you need me too, because I really understand what you're going through.\n\nI was an intern too, once!\nSimone"
            
            $SendMessages = []
            $SendMessages.append(draftMessage)
            call screen send_menu('Joel', 'Simone', 'Corrections', SendMessages)
            
            if _return == 'Send':   
              $stat_kindness +=1      
              $ contact.draft_label = None                         
              
              jump email_complete
            
        "Give constructive criticism.": #stat_honesty
            
            $ draftMessage = introMessage + "Joel, I don't want to seem like a teacher, but you made a lot of simple mistakes that can easily be corrected if you're a little more careful. For example, the article is called \"The Tux Effect\"-- but you wrote \"The Tux {i}Affect{/i}.\"\n\nIn paragraph six, you accidentally wrote 'tei' instead of 'tie,' so looking for spelling mistakes or running it through a spell check might be best, especially when the editor correcting your work is Milo, of all people.\n\nMake sure you read through very carefully, combing for simple mistakes such has these. And great article!"
            
            
            $SendMessages = []
            $SendMessages.append(draftMessage)
            call screen send_menu('Joel', 'Simone', 'Corrections', SendMessages)
            
            if _return == 'Send':   
              $stat_honesty +=1        
              $ contact.draft_label = None       
              
              jump email_complete
        
        "Remind him to send it on time.": #stat_dependability
            
            $ draftMessage = introMessage + "Don't forget to get this to him by this evening. I don't want him marching to my desk tomorrow because then we might start a fight, and it'll look bad for Solomon. Haha.\n\nGood work, though!"
            
            
            $SendMessages = []
            $SendMessages.append(draftMessage)
            call screen send_menu('Joel', 'Simone', 'Corrections', SendMessages)
            
            if _return == 'Send':   
              $stat_dependability +=1    
              $ contact.draft_label = None           
              
              jump email_complete
        
        "Tell him he owes you lunch.": #stat_imagination
            
            $ draftMessage = introMessage + "You definitely owe me one. I heard you can cook from Solomon.\n\nHow about we work out some kind of edible form of repayment?"
            
            
            $SendMessages = []
            $SendMessages.append(draftMessage)
            call screen send_menu('Joel', 'Simone', 'Corrections', SendMessages)
            
            if _return == 'Send':   
              $stat_imagination +=1 
              $ contact.draft_label = None              
              
              jump email_complete
             
        "Don’t attach anything.": #stat_laziness
            
            si "...On second thought, that's good enough. I'll just send it as is."
            $ draftMessage = introMessage
            
            
            $SendMessages = []
            $SendMessages.append(draftMessage)
            call screen send_menu('Joel', 'Simone', 'Corrections', SendMessages)
            
            if _return == 'Send':   
              $stat_laziness +=1          
              $ contact.draft_label = None     
              
              jump email_complete

    return
            
label email_complete:
  return
##-----------------------------------------------------------------------


label lbl_Email_Misc_MeetingNotes_start():
    ##IMAGINATION/DEPENDABILITY EMAIL
    
        ##From: sfox@fspub.com
        ##Subject: Meeting
        
        ##EMAIL CONTENT
        ##
  $Email_Misc_MeetingNotes_replyList = []

  $Email_Misc_MeetingNotes_replyList.append("Simone, when you have a free moment, could I ask you to forward me the information from this morning's meeting?\n\nAlso, I'm sorry about that outburst from Spade. He's not a bad journalist, but his remarks this morning were reprehensible. I just want to let you know that I've reported him to HR. Hopefully that'll be a lesson.\n\nIn any case, if you have any problems with anyone else, speak with me immediately and I will provide assistance.\n\nS. Fox")
  
  $ subject = "Meeting"
  $ replylabel = "lbl_Email_Misc_MeetingNotes_reply"               
  $ add_message(subject, 'Solomon', list(Email_Misc_MeetingNotes_replyList), replylabel)
  $ add_now()
  
  return
        
label lbl_Email_Misc_MeetingNotes_reply(current_message):
    menu:
      "Mail him your notes.": #//+Dependability
      
          $replyMessage = "Solomon, I'm not sure if the minutes I took from the meeting are satisfactory as far as 'information from the meeting', but I'll include them. They're detailed, so I think they'll be helpful for whatever you need them for!\n\nAlso... thank you. I appreciated the way you and Milo handled it. It was surprising to hear Milo talk like that, though. Kind of unexpected.\n\nThanks for the heads up, I'll let you know.\n\nSimone West"
          
          $SendMessages =  list(Email_Misc_MeetingNotes_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Solomon', 'Simone', 'RE:Meeting', SendMessages)
            
          if _return == 'Send':   
            $stat_imagination +=1    
            $ current_message.reply_label = None   # must include this line for each option   
            
      "Mail him Joel’s slides.": #//+Imagination
      
          $replyMessage = "Joel gave me a copy of these slides afterwards so I’m forwarding them to you.\nIf you need more information, let me know-- I’ll be sure to speak with him.\n\nOf course, I can also send you my notes as a back up, but I didn’t think it’d be necessary/thought this would be easier.\n\nAnd thank you for this morning. I’m glad to know that kind of behavior is taken seriously, so I appreciate it.\n\nHopefully that won’t be necessary, though.\n\nSimone West"
          
          $SendMessages =  list(Email_Misc_MeetingNotes_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('Solomon', 'Simone', 'RE:Meeting', SendMessages)
            
          if _return == 'Send':   
            $stat_imagination +=1    
            $ current_message.reply_label = None   # must include this line for each option   

      "Discard draft.":
          pass
    
    return
    
##-----------------------------------------------------------------------
    

label lbl_Email_Misc_SorryTrina_start():
##From: trinabee@pmail.com
        ##Subject: RE:Sorry, Trina
        
        ##EMAIL CONTENT
    $message = "It's okay, Simone!\n\nSometimes things happen, you know? I mean... it's really sad that we didn't get to hang out but... thanks for letting me know. I called Scott and we went to the dinner instead.\nI know how much you wanted to see it so let's try to do it another time! Maybe I can rent the movie when it comes out in a few months?\n\nAnyway, this is kind of weird but... when I was closing up the shop, guess who I saw? Your co-worker, Miles. Or Milo? (I think you called him 'Milo'. I could look back in an older email but I'm too lazy tbh.) But while we were talking, I realized...\n\nLook, I have some news and you’re not going to like it.\n\nMilo... is our replacement best man. Sorry that I didn’t tell you before, but I only realized that he was the guy Scott told me about when I saw him face-to-face. Turns out they went to school together. Scott told me his name was Milton though! So maybe Milo is a nickname? Sorry. )^:"
    $ subject = "RE:Sorry, Trina"
    $ replylabel = None              
    $ add_message(subject, 'Trina', list([message]), replylabel)
    $ add_now()
    
    return

##-----------------------------------------------------------------------

label lbl_Email_Misc_ZipIt_start():
##From: mmatthew@fspub.com
        ##Subject: Zip it.
        
    $message = "Don’t tell anyone.\n\nMy professional name is Milo Matthews and I don’t need you talking about things that are best kept secrets.\n\nSeriously, I don’t need Joel ruining my day by calling me Milton."
    
    $ subject = "Zip it."
    $ replylabel = None              
    $ add_message(subject, 'Milo', list([message]), replylabel)
    $ add_now()
    
    return

##-----------------------------------------------------------------------

label lbl_Email_Misc_NickThanks_start():
##From: nculs@fspub.com
        ##Subject: Thanks a lot!
        
    $message = "You have no idea how much you helped me, Simone.\n\nThe project somehow managed to get done, so thanks a lot for your help. You saved my life. And probably my job.\n\nOwe you one!\n\nNick C."
    
    $ subject = "Thanks a lot!"
    $ replylabel = None              
    $ add_message(subject, 'nculs@fspub.com', list([message]), replylabel)
    $ add_now()
    
    return

##-----------------------------------------------------------------------

label lbl_Email_Misc_LenaInterview_start():
    ##INTELLECT/LAZINESS EMAIL
    
        ##From: lgarcia@nycagency.com
        ##Subject: My Client
        

  $Email_Misc_LenaInterview_replyList = []

  $Email_Misc_LenaInterview_replyList.append("To Whom This May Concern,\n\nMy name is Lena Garcia, and I’m an agent with NYC Agency. I was contacted recently by a member of my department for an interview.\n\nThank you for the opportunity-- I would like to confirm the date and time if possible.\n\nI am also supposed to be in touch with the art department regarding details of the art direction of the shoot. Please give me more information regarding this.\n\nLena Garcia")
  
  $ subject = "My Client"
  $ replylabel = "lbl_Email_Misc_LenaInterview_reply"               
  $ add_message(subject, 'lgarcia@nycagency.com', list(Email_Misc_LenaInterview_replyList), replylabel)
  $ add_now()
  
  return
        

label lbl_Email_Misc_LenaInterview_reply(current_message):
    menu:
      "Forward it to Solomon.": #//+Imagination
              
          $ replyMessage = "Thank you for contacting us. I am forwarding your information to our editor-in-chief as he would know best the details regarding who is assigned to do the interview as well as date and time.\n\nI will be sure to forward your request for more information to the art department head.\n\nSimone West"
          
          $SendMessages =  list(Email_Misc_LenaInterview_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('lgarcia@nycagency.com', 'Simone', 'RE:My Client', SendMessages)
            
          if _return == 'Send':   
            $stat_imagination +=1    
            $ current_message.reply_label = None   # must include this line for each option   

      "Forward it to Joel.": #//+Laziness

          $ replyMessage = "I am forwarding your information someone capable. We will get back to you in a timely fashion.\n\nSimone West"
          
          $SendMessages =  list(Email_Misc_LenaInterview_replyList)
          $SendMessages.append(replyMessage)
          call screen send_menu('lgarcia@nycagency.com', 'Simone', 'RE:My Client', SendMessages)
            
          if _return == 'Send':   
            $stat_laziness +=1    
            $ current_message.reply_label = None   # must include this line for each option   

      "Discard draft.":
          pass


###################### Trina Emails #######################################

init python:
  Email_Trina_1_replyList = []

#STORY ARC #1) The Sugar Bandit
#Kindness and Honesty Stat Raiser


label lbl_Email_Trina_1_start():
#From: trinabee@pmail.com
#To: swest@fspub.com 
#Subject: Phantom of the Swallows
  $Email_Trina_1_replyList = []

  $Email_Trina_1_replyList.append("I'm telling you, it's the weirdest thing. I was restocking the cream and sugar area and all of the sugar packets were gone. It's the third time this week that it's happened! I don't know where they're going, but I've had to reorder so many that the delivery guy has started giving me weird looks about it.\n\nIt's not like I'm eating the 2000 count boxes! What gives!\n\n-- T")
  
  $ subject = "Phantom of the Swallows"
  $ replylabel = "lbl_Email_Trina_1_reply_1"               
  $ add_message(subject, 'Trina', list(Email_Trina_1_replyList), replylabel)
  $ add_now()
  
  return


label lbl_Email_Trina_1_reply_1(current_message):
  $response = ""
  #OPTIONS FOR THE PLAYER:
  menu:
    "Tell Trina to be careful!":
      #Choice: “Tell Trina to be careful!”
      #+Kindness Reply

      #From: swest@fspub.com
      #To: trinabee@pmail.com
      #Subject: RE:Phantom of the Swallows
      
      $replyMessage = "That's horrible! Not to mention it sounds like a heart attack waiting to happen-- although if the extent of their thievery is sugar packets, I guess it could be worse. But then you never know. First your packets, then your wallet!" + FSP_EmailFooter
      $SendMessages = list(Email_Trina_1_replyList)
      $SendMessages.append(replyMessage)
      call screen send_menu('Trina', 'Simone', 'RE:Phantom of the Swallows', SendMessages)
      
      if _return == 'Send':   
        $ stat_kindness +=1
        $Email_Trina_1_replyList.append(replyMessage)
        #If Kindness, email intro is:
        $response = "That's... quite a jump, Simone, even for you. Still, I can't help laughing at you saying petty thievery! Maybe they're like... the Robin Hood of Sugar. Stealing from the sweet and giving to the bitter.\n\n"
        $response = response + "Anyway, I tried to keep an eye on the area, but no luck so I asked Ms. Marie to help. She's that sweet old lady with the pet poodle, the regular who orders that weird combo of mint tea with low-fat non-dairy whipped topping on the side. She said she'd let me know if she sees anything. I'll keep you posted.\n\n-- T"
        
        $Email_Trina_1_replyList.append(response)
        $ subject = "Robin Hood of the Sugar Kingdom" 
        $ replylabel = "lbl_Email_Trina_1_reply_2" 
        $ add_message(subject, 'Trina', list(Email_Trina_1_replyList), replylabel)
        $ current_message.reply_label = None   # must include this line for each option    

    "It's karma, if you ask me.":
      #+Honesty Reply

      #From: swest@fspub.com
      #To: trinabee@pmail.com
      #Subject: RE:Phantom of the Swallows

      $replyMessage = "This is what you get having the word 'Swallows' in the name of your cafe. You get weird customers who are probably lurking in the corner waiting for you to turn away so they can eat your sugar packets by the hundred.\n\nThat was even weird to type out. But I do want to point out that I veto'ed 'Swallows' from jump. You have no one to blame but yourself." + FSP_EmailFooter
      $SendMessages = list(Email_Trina_1_replyList)
      $SendMessages.append(replyMessage)
      call screen send_menu('Trina', 'Simone', 'RE:Phantom of the Swallows', SendMessages)
      
      if _return == 'Send':
        $ stat_honesty +=1
        $Email_Trina_1_replyList.append(replyMessage)
        #From: trinabee@pmail.com
        #To: swest@fspub.com 
        #Subject: Robin Hood of the Sugar Kingdom

        #If Honesty, email intro is:
        $response = "You know you love Swallows! I've always thought it was cute because... you know the birds and all that... It's a nice pun! If those bird enthusiasts who appealed to the city for me to change the name didn't win, even your biting criticisms won't do the trick.\n\nGinseng Swallows is here to stay!\n\n"
        $response = response + "Anyway, I tried to keep an eye on the area, but no luck so I asked Ms. Marie to help. She's that sweet old lady with the pet poodle, the regular who orders that weird combo of mint tea with low-fat non-dairy whipped topping on the side. She said she'd let me know if she sees anything. I'll keep you posted.\n\n-- T"
        
        $Email_Trina_1_replyList.append(response)
        $ subject = "Robin Hood of the Sugar Kingdom" 
        $ replylabel = "lbl_Email_Trina_1_reply_2" 
        $ add_message(subject, 'Trina', list(Email_Trina_1_replyList), replylabel)
        $ current_message.reply_label = None   # must include this line for each option   
       
    "Don't reply yet.":
      pass 
          
  return

label lbl_Email_Trina_1_reply_2(current_message):
  menu:
    "Mrs. Marie's a little weird but...":
      #+Kindness Reply

      #From: swest@fspub.com
      #To: trinabee@pmail.com
      #Subject: RE:Robin Hood

      $replyMessage = "That Mint and Cream thing sounded weird when she first ordered it, but I told you it didn't taste that bad! You've got to try it yourself sometime. Once you do, you're going to put it on the menu and then you'll owe Ms. Marie royalties and all that.\n\nMint-and-cream tea is the best kept secret on this side of the city." + FSP_EmailFooter
      $SendMessages = list(Email_Trina_1_replyList)
      $SendMessages.append(replyMessage)
      call screen send_menu('Trina', 'Simone', 'RE:Robin Hood', SendMessages)
      
      if _return == 'Send':
        $ stat_kindness +=1
        $Email_Trina_1_replyList.append(replyMessage)

        #If Kindness, email intro is:
        $response = "I still can't believe you order that. It's bad enough that you accidentally drank her order and I had to give her a coupon for me to make more of those abominations, but for you to keep ordering it afterwards... it's disrespectful to both my establishment and the history of tea making!\n\n"
        $response = response + "Anyway, she let me know the sugar packets went missing again today. It seems that she fell asleep while I was doing inventory so we didn't catch the culprit but strangely enough their MO changed. They've migrated from just white sugar to both white and raw sugar. White sugar, okay. Fine. Steal it.\n\nBut raw sugar is expensive! This can't go on!\n\n-- T"
        
        $Email_Trina_1_replyList.append(response)
        $ subject = "Change of M.O." 
        $ replylabel = "lbl_Email_Trina_1_reply_3" 
        $ add_message(subject, 'Trina', list(Email_Trina_1_replyList), replylabel)
        $ current_message.reply_label = None   # must include this line for each option   

    "Good job getting her to watch for you.":
      #+Honesty Reply

      #From: swest@fspub.com
      #To: trinabee@pmail.com
      #Subject: RE:Robin Hood

      $replyMessage = "Ms. Marie said she'd help you? Sweet. Free surveillance labor. You don't even need to get a security camera. It works out perfectly too because old people have eyes like a hawk.\n\nWhile she's looking out for you, tell me if she sees me that necklace I thought I lost in there. I keep telling you, if I don't get it back, I'm not getting you a wedding present. Either that, or I'm adding in a certain section to my maid of honor speech about 'you-know-what'. (((^:" + FSP_EmailFooter
      $SendMessages = list(Email_Trina_1_replyList)
      $SendMessages.append(replyMessage)
      call screen send_menu('Trina', 'Simone', 'RE:Robin Hood', SendMessages)
      
      if _return == 'Send':
        $ stat_honesty +=1
        $Email_Trina_1_replyList.append(replyMessage)

        #From: trinabee@pmail.com
        #To: swest@fspub.com 
        #Subject: Changed MO

        #If Honesty, email intro is:
        $response = "You're terrible. I can't believe you seriously considered going to into hospitality. I'm so glad I talked you out of it. You seem like the type that'd work at a nursing home and let your patients roll down the hallway in their wheelchairs so they can get some air.\n\nOh. You mean the one with the coral beads? I found that a few weeks ago but it matches my peach top so well that I haven't gotten around to giving it back yet. My sister said it matches my skin tone really well, btw. You have great taste! Thanks for the borrow! ;^)\n\nBut with a threat like that... /^: I'll give it back tomorrow.\n\n"         
        $response = response + "Anyway, she let me know the sugar packets went missing again today. It seems that she fell asleep while I was doing inventory so we didn't catch the culprit but strangely enough their MO changed. They've migrated from just white sugar to both white and raw sugar. White sugar, okay. Fine. Steal it.\n\nBut raw sugar is expensive! This can't go on!\n\n-- T"
        
        $Email_Trina_1_replyList.append(response)
        $ subject = "Change of M.O." 
        $ replylabel = "lbl_Email_Trina_1_reply_3" 
        $ add_message(subject, 'Trina', list(Email_Trina_1_replyList), replylabel)
        $ current_message.reply_label = None   # must include this line for each option   
          
    "Don't reply yet.":
      pass 
  return

label lbl_Email_Trina_1_reply_3(current_message):
  menu:
    "Maybe it's an animal?":
      #+Kindness Reply

      #From: swest@fspub.com
      #To: trinabee@pmail.com
      #Subject: RE:Change of M.O.

      $replyMessage = "Not to be gross but have you considered like... mice or something? I mean, if it never happened before, it's probably not your employees, but that doesn't mean that no one is stealing them.\n\nIt's a horrible thing to say but if word got out " + FSP_EmailFooter
      $SendMessages = list(Email_Trina_1_replyList)
      $SendMessages.append(replyMessage)
      call screen send_menu('Trina', 'Simone', 'RE:Change of M.O.', SendMessages)
      
      if _return == 'Send':
        $ stat_kindness +=1
        $Email_Trina_1_replyList.append(replyMessage)


        #If Kindness, email intro is:
        $response = "Don't even say that as a joke! D: I can't imagine having rodents and we clean really well! We always pass inspections so I'd guess no, but even I can't be 100% certain...\n\nGeez, Simone! Now I'm really paranoid... I'll call to schedule an inspection first thing next week if it's definitely not a person. Ugh.\n\n"
              
        $response = response + "Oh, and no help on the Ms. Marie front. I've decided to install a surveillance camera. And before you laugh, please understand-- I checked my business invoice, and I've spent almost four hundred dollars worth of boxes of sugar. Do you know how many sugar packets that is? Well, considering that a 2000 count box costs about thirty bucks, we're talking 26,000 packets of sugar!\n\nThis isn't a sugar bandit, this is a sugar criminal mastermind! I can't order another box of sugar, Simone! I just can't do it.\n\n-- T"
  
        $Email_Trina_1_replyList.append(response)
        $ subject = "Sugar Al Capone" 
        $ replylabel = "lbl_Email_Trina_1_reply_4" 
        $ add_message(subject, 'Trina', list(Email_Trina_1_replyList), replylabel)
        $ current_message.reply_label = None   # must include this line for each option   
          

    "Maybe it's an employee...":
      #+Honesty Reply

      #From: swest@fspub.com
      #To: trinabee@pmail.com
      #Subject: RE:Change of MO

      $replyMessage = "Hm... That sounds pretty suspicious. I don't want to be the cynic in all this, but maybe it's an employee? I know you've never had any issues with them before, so I imagine who it could be, but it's kind of strange that it's happening so recently and so often.\n\nAt the very least, it could be one of your employee's friends and they look the other way while they take them?" + FSP_EmailFooter

      $SendMessages = list(Email_Trina_1_replyList)
      $SendMessages.append(replyMessage)
      call screen send_menu('Trina', 'Simone', 'RE:Change of M.O.', SendMessages)
      
      if _return == 'Send':
        $ stat_honesty +=1
        $Email_Trina_1_replyList.append(replyMessage)

        #From: trinabee@pmail.com
        #To: swest@fspub.com 
        #Subject: Sugar Al Capone

        #If Honesty, email intro is:
        $response = "I don't think so... but I guess I can't be certain. Nothing like this has ever happened before so I'm almost too flabbergasted to know what to do. I mean... of all the things to steal, why sugar? Why not... plastic forks and spoons? Those seems more practical, you know?\n\n\It's just really weird...\n\n"
         
        $response = response + "Oh, and no help on the Ms. Marie front. I've decided to install a surveillance camera. And before you laugh, please understand-- I checked my business invoice, and I've spent almost four hundred dollars worth of boxes of sugar. Do you know how many sugar packets that is? Well, considering that a 2000 count box costs about thirty bucks, we're talking 26,000 packets of sugar!\n\nThis isn't a sugar bandit, this is a sugar criminal mastermind! I can't order another box of sugar, Simone! I just can't do it.\n\n-- T"
        $Email_Trina_1_replyList.append(response)
        $ subject = "Sugar Al Capone" 
        $ replylabel = "lbl_Email_Trina_1_reply_4" 
        $ add_message(subject, 'Trina', list(Email_Trina_1_replyList), replylabel)
        $ current_message.reply_label = None   # must include this line for each option   
          
          
    "Don't reply yet.":
      pass 
            
  return

label lbl_Email_Trina_1_reply_4(current_message):
  menu:
    "Express sympathy about the money.":
      #+Kindness Reply

      #From: swest@fspub.com
      #To: trinabee@pmail.com
      #Subject: RE:Sugar Al Capone

      $replyMessage = "Sorry about your money being wasted... )^:\n\nAlmost $400... that's a lot of money, jeez. When you catch the culprit, you'd better make them pay you back. Sue them in small claims court or something! There's honestly no excuse to steal sugar packets of all things.\n\nI wonder who it is, though?" + FSP_EmailFooter
      $SendMessages = list(Email_Trina_1_replyList)
      $SendMessages.append(replyMessage)
      call screen send_menu('Trina', 'Simone', 'RE:Sugar Al Capone', SendMessages)
      
      if _return == 'Send':
        $ stat_kindness +=1
        $Email_Trina_1_replyList.append(replyMessage)

        #If Kindness, email intro is:
        $response = ""

        $response = response + "YOU WILL NEVER\n\nNEVER\n\nN E V ER in a million years believe who's been stealing the sugar. So I installed the camera and I didn't get a chance to let Ms. Marie know because I was running errands outside the shop and I left Ricardo in charge. Don't you know, I get back to the shop, and what a surprise! Sugar gone. I already knew it was going to be like that.\n\nI go home, I watch the recording-- and I see Ms. Marie chatting with a customer, another old lady. I'm like, 'oh, how cute! Old people friends.” After they chat, old lady #2 walks up and takes a handful of sugar packets! So at first, I'm like AHA! But then I realize the sugar container is full, so while old lady #2 might be a thief, she's probably not The Thief. So I keep watching.\n\nA second old person comes up, grabs a handful of packets and goes. Then it happens a third time, and a fourth!\nSo at first I was confused because it was like... why are all these old people stealing sugar? But then I realized-- right before and after they come up, they go back to talk to Ms. Marie!\n\nThat's right! The sugar criminal mastermind turned out to be Ms. Marie herself! Old people are evil, Simone. Straight up pure evil.\n\nI confronted her this morning, and you know what she told me? She needed them so she could bake cookies at the senior center. Apparently, management's told her to stop baking sweets because sugar things with so many diabetics around is a bad idea. She didn't want to listen, so they locked away the public baking supplies and put up a sign in log for the used supplies so they could monitor the sugar use. She wanted to continue making them so what does she do? She hatches a plan to steal mine!\n\nAnyway, she's banned from the shop. /^:\n\n-- T"
        
        $Email_Trina_1_replyList.append(response)
        $ subject = "WHY" 
        $ replylabel = None # Last email in chain so no replies available
        $ add_message(subject, 'Trina', list(Email_Trina_1_replyList), replylabel)
        $ current_message.reply_label = None   # must include this line for each option   

    "Compliment her on the camera idea.":
      #+Honesty Reply

      #From: swest@fspub.com
      #To: trinabee@pmail.com
      #Subject: RE: Sugar Al Capone

      $replyMessage = "I'm definitely a terrible person because I laughed so loud at you subject heading that Matthews glared at me from across the room. Ugh, it's like he's allergic to joy. I wanted to respond with a pun using 'ice cream cone' in his last name, but it sounds stupid said aloud and sounds even worse written down.\n\nAnyway, keep me posted! I think a camera's a great idea. Catch them white-handed!\n\n...Get it? (Because they're stealing sugar? It's not powdered sugar, I know but.... whatever, you're going to read this joke and you're going to like it! No complaints!)" + FSP_EmailFooter
      
      $SendMessages = list(Email_Trina_1_replyList)
      $SendMessages.append(replyMessage)
      call screen send_menu('Trina', 'Simone', 'RE:Sugar Al Capone', SendMessages)
      
      
      if _return == 'Send':
        $ stat_honesty +=1
        $Email_Trina_1_replyList.append(replyMessage)

        #From: trinabee@pmail.com
        #To: swest@fspub.com 
        #Subject: WHY

        #If Honesty, email intro is:
        $response = "Okay, so before we talk about who it is (I was going to launch right into it, but I have to address this: you might be able to top my jokes sometimes, but you can never improve them. Trina Luong dishes out top quality coffee, catering and commentary. (^:\n\nI would talk about how great I am longer but............ SIMONE.\n\n"

        $response = response + "YOU WILL NEVER\n\nNEVER\n\nN E V ER in a million years believe who's been stealing the sugar. So I installed the camera and I didn't get a chance to let Ms. Marie know because I was running errands outside the shop and I left Ricardo in charge. Don't you know, I get back to the shop, and what a surprise! Sugar gone. I already knew it was going to be like that.\n\nI go home, I watch the recording-- and I see Ms. Marie chatting with a customer, another old lady. I'm like, 'oh, how cute! Old people friends.” After they chat, old lady #2 walks up and takes a handful of sugar packets! So at first, I'm like AHA! But then I realize the sugar container is full, so while old lady #2 might be a thief, she's probably not The Thief. So I keep watching.\n\nA second old person comes up, grabs a handful of packets and goes. Then it happens a third time, and a fourth!\nSo at first I was confused because it was like... why are all these old people stealing sugar? But then I realized-- right before and after they come up, they go back to talk to Ms. Marie!\n\nThat's right! The sugar criminal mastermind turned out to be Ms. Marie herself! Old people are evil, Simone. Straight up pure evil.\n\nI confronted her this morning, and you know what she told me? She needed them so she could bake cookies at the senior center. Apparently, management's told her to stop baking sweets because sugar things with so many diabetics around is a bad idea. She didn't want to listen, so they locked away the public baking supplies and put up a sign in log for the used supplies so they could monitor the sugar use. She wanted to continue making them so what does she do? She hatches a plan to steal mine!\n\nAnyway, she's banned from the shop. /^:\n\n-- T"
        
        $Email_Trina_1_replyList.append(response)
        $ subject = "WHY" 
        $ replylabel = None # Last email in chain so no replies available
        $ add_message(subject, 'Trina', list(Email_Trina_1_replyList), replylabel)
        $ current_message.reply_label = None   # must include this line for each option   
          
    "Don't reply yet.":
      pass 
      
  return
  
  
###################### Thursday Drafts #######################################


init python:
  Email_Joel_Thursday_replyList = []
  Email_Milo_Thursday_replyList = []
  Email_Solomon_Thursday_replyList = []


##-----------------------------------------------------------------------
label lbl_Email_Joel_Thursday_draft(contact, message_title=""):
    menu:
        "Chat about Joel's project.":#//+Laziness

        #From: swest@fspub.com
        #To: jcabrera@fspub.com
        #Subject: Tuesday's Meeting

            $ draftMessage = "Hey, Joel.\n\nAside from the outburst from that journalist- Spade, I think his name was? - your presentation the other day was excellent.\n\nI especially like the idea of articles being released in a interlocked cycle with the site to pull in more readers.\n\nHow's the project going? Everything moving along?"
        
                 
            $SendMessages = []
            $SendMessages.append(draftMessage)
            call screen send_menu('Joel', 'Simone', "Tuesday's Meeting", list(SendMessages))
            
            if _return == 'Send':   
              $ stat_laziness +=1      
              #---------

              #From: jcabrera@fspub.com
              #To: swest@fspub.com
              #Subject: RE:Tuesday's Meeting

              $response = "Simone,\n\nI'm actually at the end of the research stage and I think I should be able to have a draft on Solomon's desk. Maybe by tomorrow? (Probably around lunch-ish or so?)\n\nSorry about that whole thing anyway. You're really cool so I don't know what his problem is... Oh, but overall the project is going well, thanks a lot for checking.\n\nJoel"
              $ contact.draft_label = None 
              
              $Email_Joel_Thursday_replyList = []
              $Email_Joel_Thursday_replyList.append(draftMessage)
              $Email_Joel_Thursday_replyList.append(response)
              $ subject = "RE:Tuesday's Meeting" 
              $ replylabel = None
              $ add_message(subject, 'Joel', list(SendMessages), replylabel)

        #---------

        "Offer Joel help with anything.":# //+Kindness


            #From: swest@fspub.com
            #To: jcabrera@fspub.com
            #Subject: Tuesday's Meeting

            $ draftMessage = "Hey, I hope your project is going well.\n\nYou seem like you've been working really hard on it-- I'm not always busy, though so, I'm just saying-- let me know if you need any help?\n\nIf I can spare a hand I definitely will. Don't be afraid to let me know.\n\nSimone"
                
            $SendMessages = []
            $SendMessages.append(draftMessage)
            call screen send_menu('Joel', 'Simone', "Tuesday's Meeting", list(SendMessages))
            
            if _return == 'Send':    
              $ stat_kindness +=1     
              #---------

              #From: jcabrera@fspub.com
              #To: swest@fspub.com
              #Subject: RE:Tuesday's Meeting

              $response = "Thanks for asking, Simone!\n\nI'm doing okay for right now but... if I could ask you to put a printout of my presentation on my desk? \n\nIt's on my computer but I'm not in the office right now and I don't think I'll have\ntime to get it before the meeting tonight. \n\nJoel"
              $ contact.draft_label = None 
              
              $Email_Joel_Thursday_replyList = []
              $Email_Joel_Thursday_replyList.append(draftMessage)
              $Email_Joel_Thursday_replyList.append(response)
              $ subject = "RE:Tuesday's Meeting" 
              $ replylabel = None
              $ add_message(subject, 'Joel', list(SendMessages), replylabel)
      
        "Discard draft.":
            pass
##-----------------------------------------------------------------------
label lbl_Email_Milo_Thursday_draft(contact, message_title=""):
    menu:


        "Update Milo's schedule.":# //+Dependability


            #From: swest@fspub.com
            #To: mmatthews@fspub.com
            #Subject: Garcia Account

            $ draftMessage = "Matthews,\nI have a possible schedule adjustment for you.\n\nNext Thursday are you open to do an interview on, 10am? The agent, Lena Garcia, is refusing to do it on the 15th as previously agreed.\n\nSimone West"
   
            $SendMessages = []
            $SendMessages.append(draftMessage)
            $subject = "Garcia Account"
            call screen send_menu('Milo', 'Simone', subject, list(SendMessages))
            
            if _return == 'Send':      
              $ stat_dependability +=1   

              #From: mmatthews@fspub.com
              #To: swest@fspub.com
              #Subject: RE:Garcia Account

              $response = "West--\n\nGarcia is refusing what?\n\nI already changed the date twice and what I told her are the only ones I've got left. If she's refusing, ignore her emails.\n\nI'll take care of it.\n\nM.M."

              $ contact.draft_label = None 
              
              $Email_Milo_Thursday_replyList = []
              $Email_Milo_Thursday_replyList.append(draftMessage)
              $Email_Milo_Thursday_replyList.append(response)
              $ subject = "RE:" + subject
              $ replylabel = None
              $ add_message(subject, 'Milo', list(SendMessages), replylabel)
            #---------

        "Ask his opinion on your wedding speech.":#//+Honesty


            #From: swest@fspub.com
            #To: mmatthews@fspub.com
            #Subject: Not Work Related

            $ draftMessage = "Matthews, \n\nI hate to ask you (really, really hate it) but you're an editor by trade so I'm asking in case you have insight that I don't.\n\nIf you want, you can even think of it as a favor for Scott and not for me.\n\nCould you look over my maid of honor speech? \n\nSimone West"
            $SendMessages = []
            $SendMessages.append(draftMessage)
            $subject = "Not Work Related"
            call screen send_menu('Milo', 'Simone', subject, list(SendMessages))
            
            if _return == 'Send':
              $ stat_honesty +=1
              #---------

              #From: mmatthews@fspub.com
              #To: swest@fspub.com
              #Subject: RE:Not Work Related

              $response = "West--\n\nSeriously?\n\nHave it on my desk by tonight.\n\nMaybe if I have time I'll check it. Proofread it for typos. You're a P.A. so I'm sure you can do at least that much.\n\nM.M."
          
              $ contact.draft_label = None 
              
              $Email_Milo_Thursday_replyList = []
              $Email_Milo_Thursday_replyList.append(draftMessage)
              $Email_Milo_Thursday_replyList.append(response)
              $ subject = "RE:" + subject
              $ replylabel = None
              $ add_message(subject, 'Milo', list(SendMessages), replylabel)
            #---------

        "Discard draft.":
            pass

##-----------------------------------------------------------------------

label lbl_Email_Solomon_Thursday_draft(contact, message_title=""):
    menu:
        "Update Solomon's itinerary.":# //+Imagination

            #From: swest@fspub.com
            #To: sfox@fspub.com
            #Subject: Lima

            $ draftMessage = "Mr. Fox,\nI got a call from a certain Atilio Romero, an organizer for the Concept Illusions runway show in Lima-- he's inviting you to stay in his villa until the show itself. Do you want me to book your flight for the 15th of July for time in the city or would you prefer closer to the show?\n\nSimone"
            $SendMessages = []
            $SendMessages.append(draftMessage)
            $subject = "Lima"
            call screen send_menu('Solomon', 'Simone', subject, list(SendMessages))
            
            if _return == 'Send':
              $ stat_imagination +=1

              #---------

              #From: sfox@fspub.com
              #To: swest@fspub.com
              #Subject:RE:Lima

              $response = "Book it closer to the show.\n\nNot to be unprofessional, but Romero tends to be a bit... overwhelming. Also, as my PA, I hope you understand that you will be accompanying me so don't forget your own ticket.\n\nI look forward to attending with you.\n\nS. Fox"
              #$response = 
          
              $ contact.draft_label = None 
              
              $Email_Solomon_Thursday_replyList = []
              $Email_Solomon_Thursday_replyList.append(draftMessage)
              $Email_Solomon_Thursday_replyList.append(response)
              $ subject = "RE:" + subject
              $ replylabel = None
              $ add_message(subject, 'Solomon', list(SendMessages), replylabel)


            #---------

        "Give him an office status report.":#//+Intellect

            #From: swest@fspub.com
            #To: sfox@fspub.com
            #Subject: Status Report

            $ draftMessage = "Mr. Fox,\nHere's this week's status report, just based off of the stack I've gotten off of my desk--\nThere should be three articles coming in this afternoon, though I have no word on Joel's poject.\n\nIs there anything I should be keeping an eye out for?\n\nSimone"
            $SendMessages = []
            $SendMessages.append(draftMessage)
            $subject = "Status Report"
            call screen send_menu('Solomon', 'Simone', subject, list(SendMessages))
            
            if _return == 'Send':
              $ stat_intellect +=1

              #---------

              #From: sfox@fspub.com
              #To: swest@fspub.com
              #Subject:RE:Status Report

              $response = "I'm glad you said so. The art department head is supposed to have a potential concepts file on my desk by... yesterday. If you don't hear from him let me know and we'll have a word.\n\nWell, no.\n\nIt might be best to let you handle it since Pierre and I don't exactly enjoy each other's company. Speaking of company-- there's an office event that's supposed to take place next Tuesday... Can I ask you to do me a favor and come with me?\n\nI find them boring and it would be helpful if I could use you as an excuse to leave early. My treat.\n\nS. Fox"
              #$response = 
          
              $ contact.draft_label = None 
              
              $Email_Solomon_Thursday_replyList = []
              $Email_Solomon_Thursday_replyList.append(draftMessage)
              $Email_Solomon_Thursday_replyList.append(response)
              $ subject = "RE:" + subject
              $ replylabel = None
              $ add_message(subject, 'Solomon', list(SendMessages), replylabel)



        "Discard draft.":
            pass

            
###################### Tutorial Emails #######################################
init python:
  Email_Tutorial_ReplyTest_replyList = []
  Email_Tutorial_HasReplied_Flag = False
  Email_Tutorial_DraftSol_Flag = False
  Email_Tutorial_DraftMilo_Flag = False
  Email_Tutorial_DraftJoel_Flag = False
  Email_Tutorial_HasSentDraft_Flag = False
  
   
  Email_Tutorial_FirstDraft_Flag = True


label lbl_Email_Tutorial_End:
  "And remember that you can use the email button on the textbox to read your emails any time, but you will only be able to reply or write new emails during the allotted times of the day. Can't have you spending all your working day writing emails, now can we?"
  
  "That's the end of the Tutorial, hope it was useful."
  $persistent.TutorialComplete = True
  
label lbl_Email_Tutorial_Skip:
  hide screen screen_desktop
  
  return

label lbl_Email_Tutorial_Start:

    if persistent.TutorialComplete:
      call screen yesno_prompt("Do you wish to see the email tutorial?", Return("Yes"), Return("No"))
      if _return == "No":
        jump lbl_Email_Tutorial_Skip
      
    
    $Email_Tutorial_HasReplied_Flag = False
    $Email_Tutorial_DraftSol_Flag = False
    $Email_Tutorial_DraftMilo_Flag = False
    $Email_Tutorial_DraftJoel_Flag = False
    $Email_Tutorial_HasSentDraft_Flag = False
    $TutorialInProgress = True
    call lbl_Email_Tutorial_ReplyTest_Start from _call_lbl_Email_Tutorial_ReplyTest_Start
    show screen screen_desktop
    
    call screen info_prompt("This is Simone's desktop. When she needs to send emails, click on the email icon here!", Return(""))
    
    #show screen circle_highlight(900,130)
    #
    #call screen info_prompt("Click the highlighted email icon to get started!", Return(""))
    #hide screen circle_highlight
    #show screen email_menu(False)
    #show screen circle_highlight(160,90)
    #call screen info_prompt("Look at that, Simone has an email. Why not try clicking it on it?", Return(""))
    #
    #show screen circle_highlight(490,60)
    #
    #call screen info_prompt("What a nice email! Simone should reply. Click the 'Reply' button.", Return(""))
    
    "Here's a quick guide to replying to an email."
    call screen screen_tutorialShow(0, "On the desktop screen, you can click the pigeon icon to open your emails.")
    call screen screen_tutorialShow(1, "If you click on the email on the left, it will show the contents in the box on the right.")
    call screen screen_tutorialShow(3, "If the option is available, you can select the 'Reply' button to answer an email.")
    call screen screen_tutorialShow(4, "In the reply screen, choose an option to pick the contents of your email, or discard to cancel the email and return to the previous screen.")
    call screen screen_tutorialShow(5, "Once you have chosen your option, you can preview the email and when ready you can click the 'send' button to send the email.")
    call screen screen_tutorialShow('exit', "Lastly if you need to leave the email menu you can use the 'x' at the top right of the window.")
    "Trina's waiting for a reply to her email... Simone should get on that."
    
    "Don't forget to click on the 'x' in the top right of the browser to close the email!"
    
label lbl_Email_Tutorial_ReplyLoop:
    if Email_Tutorial_HasReplied_Flag == True:
        jump lbl_Email_Tutorial_Draft
    else:
        
        "..."
        
        "Well?"
        
        "Have you tried sending that reply yet?"
        jump lbl_Email_Tutorial_ReplyLoop
    
    return

label lbl_Email_Tutorial_Draft:
    $ Contact_Trina = Contact("Trina", "lbl_Email_Tutorial_DraftTest")
    "Oh, great job!"
    
    "But wait! Simone forgot to tell Trina about her day! Now she has to write a new email."
    
    "Normally, Simone can only write Trina once a day--she is at work, after all--but for the purposes of this tutorial, we're going to compose a new email by selecting 'New Draft'."
    "Here's a quick guide to sending a new email."
    call screen screen_tutorialShow(6, "If the option is available, you can select the 'New Draft' button to start drafting a brand new email.")
    call screen screen_tutorialShow(7, "In the compose screen, choose an option to pick who the email is being sent to.")
    call screen screen_tutorialShow(8, "You can also choose an option to pick the contents of your email or discard to cancel the email and return to the previous screen. Normally, the types of replies you select will add a stat. Here, it's just a tutorial, so have fun chatting.")
    call screen screen_tutorialShow(9, "Once you have chosen your option, you can preview the email and when ready you can click the 'send' button to send the email.")
    #draft explanation here
    "Now you try sending a new email to Trina."
    
label lbl_Email_Tutorial_DraftLoop:
    
    if Email_Tutorial_DraftSol_Flag or Email_Tutorial_DraftMilo_Flag or Email_Tutorial_DraftJoel_Flag:
      "Now, usually you can only make one choice, but no doubt Trina wants to know about all the guys, so go ahead and talk about them, too. Include the other options in your email."
    if Email_Tutorial_HasSentDraft_Flag == True:
      jump lbl_Email_Tutorial_End
    else:
      "Have you tried sending that email yet?"
      jump lbl_Email_Tutorial_DraftLoop
    
    return
    
    

label lbl_Email_Tutorial_ReplyTest_Start():

  ##To: swest@fspub.com
  ##From: trinabee@pmail.com
  ##Subject: Have a good day!
  
  ##EMAIL CONTENT##
  $Email_Tutorial_ReplyTest_replyList = []
  $Email_Tutorial_DraftTest_replyList = []

  $Email_Tutorial_ReplyTest_replyList.append("Hey, Simone!\nI just wanted to say I hope you have a great first day. I won't be at the shop as much because... you know, wedding prep and all that, but you can talk to me any time.\n\nI feel like I'm a mom sending my kid to school.\n\nPlay nice with the other kids now. I don't want to have to come to the principal's office to hear about you fighting with little Mikey.\n\nOkay! Stop reading non-work emails at work!\n\n-- T")
  
  $ subject = "Have a good day!"
  $ replylabel = "lbl_Email_Tutorial_ReplyTest_Reply_1"               
  $ add_message(subject, 'Trina', list(Email_Tutorial_ReplyTest_replyList), replylabel)
  $ add_now()
  
  return

label lbl_Email_Tutorial_ReplyTest_Reply_1(current_message):
    menu:
        "Thank Trina for emailing you.":
        
            $replyMessage = "Thanks for the email, Trina. I had a crazy day, but I think I'm going to like it here. I know you're going to be busy, and I miss you already.\n\nTBH you're not just saying that. I already met the schoolyard bully and the shy kid. I feel like the only adult here is my boss, so I guess that makes him the teacher? (More on him later).\n\nThe day's almost over so I was actually pretty good today. Almost emailed you this morning but was interrupted by aforementioned schoolyard bully. :P\n\nOkay, talk to you later.\n\nSimone"
      
            $SendMessages = list(Email_Tutorial_ReplyTest_replyList)
            $SendMessages.append(replyMessage)
            call screen send_menu('Trina', 'Simone', 'Have a good day!', SendMessages)
            
            
            if _return == 'Send':
              $ current_message.reply_label = None   # must include this line for each option   
              $Email_Tutorial_HasReplied_Flag = True
              $Email_Tutorial_ReplyTest_replyList.append(replyMessage)

        "Discard draft.":
            pass
            
    pass
    
return
    
label lbl_Email_Tutorial_DraftTest(contact, message_title="The 411 of 5/7"):

            ##To: trinabee@pmail.com
            ##From: swest@fspub.com
            ##Subject: [Choice]
            ##EMAIL CONTENT##
            
                
        
        ##[Now, usually you can only make one choice, but no doubt Trina wants to know about all the guys, so go ahead and talk about them, too. Include the other options in your email.]
        
        ##When all the options are clicked, Marionette, it should say this.
        
        ##[Now, choose a subject.]
        
            ##Subject choices are:
                ##The 411 of 5/7
                ##Cufflinks? More like Chainlinks.
                ##About the Boss (and Co-workers)
    $intro = "Hey, so.... let's talk about the three guys I met at work today."
    if Email_Tutorial_FirstDraft_Flag == True:
      $Email_Tutorial_DraftTest_replyList.append(intro)
      $Email_Tutorial_FirstDraft_Flag = False
    menu:
        "Tell her about Solomon." if Email_Tutorial_DraftSol_Flag == False:

            $ draftMessage = "My new boss is The British Guy. You know the guy I mean. The print-outs one you mentioned this morning from four years ago!\n\nCan you believe it?!\n\nNot only does he {i}still{/i} work here, but he's got the nerve to look {i}extra{/i} good-- and did I mention, he's my BOSS? When he helped me back then, he was definitely not a department head. Says he's only been in the position for two years.\n\nI don't think he remembers me but he did remember my name. Hopefully that's all he remembers."
            $SendMessages = list(Email_Tutorial_DraftTest_replyList)
            $SendMessages.append(draftMessage)
            $subject = "The 411 of 5/7"
            call screen send_menu('Trina', 'Simone', subject, list(SendMessages))
            
            if _return == 'Send':
              $Email_Tutorial_DraftTest_replyList.append(draftMessage)
              $Email_Tutorial_DraftSol_Flag = True
              
            #---------
        "Tell her about Milo." if Email_Tutorial_DraftMilo_Flag == False:
        
            $ draftMessage = "There's this absolute tool, Milo Matthews. First of all, what kind of fake double-00 lame-o name is 'Milo Matthews'? He's got this fancypants accent. (My boss has one too, but it's not the same!!) And he actually introduced himself like that. \"Matthews. Milo Matthews.\" I'm telling you, I got nauseous."
            $SendMessages = list(Email_Tutorial_DraftTest_replyList)
            $SendMessages.append(draftMessage)
            $subject = "The 411 of 5/7"
            call screen send_menu('Trina', 'Simone', subject, list(SendMessages))
            
            if _return == 'Send':
              $Email_Tutorial_DraftTest_replyList.append(draftMessage)
              $Email_Tutorial_DraftMilo_Flag = True
          
            #---------
        "Tell her about Joel." if Email_Tutorial_DraftJoel_Flag == False:
        
            $ draftMessage = "There's this total sweetheart, Joel. He's like... a puppy. He was telling me he grew up on a farm and he's just... a delicate flower that needs to be protected. I have no idea what he's doing in a fashion journalism job considering how cutthroat it is, but he's pretty likable which is his saving grace. I would ask how he made it this far but I've got the answer. One word, Trina: nepotism.\n\nBut you didn't hear it from me."
            $SendMessages = list(Email_Tutorial_DraftTest_replyList)
            $SendMessages.append(draftMessage)
            $subject = "The 411 of 5/7"
            call screen send_menu('Trina', 'Simone', subject, list(SendMessages))
            
            if _return == 'Send':         
              $Email_Tutorial_DraftTest_replyList.append(draftMessage)
              $Email_Tutorial_DraftJoel_Flag = True

        "Let me just send this already." if Email_Tutorial_DraftSol_Flag and Email_Tutorial_DraftMilo_Flag and Email_Tutorial_DraftJoel_Flag:
            $SendMessages = list(Email_Tutorial_DraftTest_replyList)
            $subject = "The 411 of 5/7"
            call screen send_menu('Trina', 'Simone', subject, list(SendMessages))
            if _return == 'Send':         
              $Email_Tutorial_DraftTest_replyList.append(draftMessage)
          
              $ contact.draft_label = None 
              $Email_Tutorial_HasSentDraft_Flag = True
              
            
              $response = "Phew, what's with these back to back emails? I mean, talk about blowing up my phone.\n\nAnywhooo, I realized: I recognize those names!\n\nScore! Turns out catering for those 5/7 Publishing luncheons was a bonus, and you know how I never forget a name or face.\n\nWow, seems like the universe is on your side today. Since it's apparently raining men on you two weeks before the wedding you should snag one to be your date for the wedding. Kidding!\n\nOh! And before I forget, it's a no go on coming over tomorrow night. )^': I promised Mom I'd help her prepare dinner for the Grannies in our neighborhood. I wanted to turn her down but then she started moaning about how soon, she's going to be one. Cue eyeroll.-- T"
            
              $Email_Tutorial_DraftTest_replyList.append(response)
              $ subject = "RE:" + subject
              $ replylabel = None
              $ add_message(subject, 'Trina', list(Email_Tutorial_DraftTest_replyList), replylabel)
          
        "Discard draft.":
            pass

            