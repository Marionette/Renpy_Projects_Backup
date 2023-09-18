##Basic Message System 1.2 provided under CC0 1.0 Universal by saguaro, includes contributions by xavimat
# http://creativecommons.org/publicdomain/zero/1.0/deed.en
# See Lemma Soft Forum for most recent version: http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=19295

init python:
    import renpy.store as store
    
    reply_screen = False
    draft_screen = False

    class Mail(store.object):
        def __init__(self, subject, sender, body, reply_label=False, delay=False, view=True, read=False):
            self.subject = subject
            self.sender = sender
            self.body = body
            self.reply_label = reply_label
            self.delay = delay
            self.view = view
            self.read = read
            if delay:
                self.queued()
            else:            
                self.deliver()  
                
        def delete(self):
            self.view = False
            renpy.restart_interaction()
            
        def deliver(self):
            if self in mail_queue:
                mail_queue.remove(self)
            mail.insert(0, self)
            
        def mark_read(self):
            self.read = True 
            renpy.restart_interaction()         
            
        def queued(self):
            mail_queue.append(self)           
            
        def reply(self):
            global reply_screen
            reply_screen = True
            renpy.call_in_new_context(self.reply_label, current_message=self)                
            reply_screen = False            
            
        def restore(self):
            self.view = True  
            renpy.restart_interaction()            

    class Contact(store.object):
        def __init__(self, name, draft_label):
            self.name = name
            self.draft_label = draft_label  
            self.add_contact()
            
        def add_contact(self):
            contacts.append(self)

        def draft(self):
            global draft_screen
            draft_screen = True
            renpy.call_in_new_context(self.draft_label, contact=self)            
            draft_screen = False
            
        def delete(self):
            contacts.remove(self)

    def add_message(subject, sender, body, reply_label=False, delay=False):
        renpy.sound.play("sounds/chime.wav")
        message = Mail(subject, sender, body, reply_label, delay)
        #renpy.show_screen("mailbox_overlay")
        
    def add_later(subject, sender, body, reply_label=False):
        mail_later.append([subject, sender, body, reply_label])
              
    def add_now():
        for element in mail_later:
            add_message(element[0], element[1], element[2], element[3])
        global mail_later
        mail_later = []
        
    def check(subject):
        for item in mail:
            if item.subject == subject:
                if item.read:
                    return True
                else:
                    return False
                    
    def deliver_all(): 
        mail.extend(mail_queue)
        mail_queue = list()          
        
    def deliver_next():
        if mail_queue:
            mail_queue[0].deliver()

    def mark_all_read():
        unread_messages = [x for x in mail if not x.read]
        for x in unread_messages:
            x.mark_read()                

    def message_count():
        visible_messages = [x for x in mail if x.view]
        return len(visible_messages)
        
    def new_message_count():
        unread_messages = [ x for x in mail if not x.read]
        return len(unread_messages)
            
    def restore_all():
        deleted_messages = [x for x in mail if not x.view]
        for x in deleted_messages:
            x.restore()
        renpy.restart_interaction()

#screen mailbox_overlay:
#    hbox:
#        xalign 1.0 yalign 0.0
#        if new_message_count() > 0:
#            textbutton "Mailbox (%d New)" % (new_message_count()) action [Hide('mailbox_overlay'), Show("email_menu")]
#        else:
#            textbutton "Mailbox" action [Hide('mailbox_overlay'), Show("email_menu")]
#            
#screen mailbox_overlay_exit:
#    hbox:
#        xalign 1.0 yalign 0.0
#        if new_message_count() > 0:
#            textbutton "Mailbox (%d New)" % (new_message_count()) action [Hide("email_menu"), Hide('mailbox_overlay_exit'), Show("mailbox_overlay")]
#        else:
#            textbutton "Mailbox" action [Hide("email_menu"), Hide('mailbox_overlay_exit'), Show("mailbox_overlay")]

#screen mailbox:
#    tag menu
#    modal True
#    
#    use mailbox_overlay_exit
#    default current_message = None
#    $ available_drafts = [i for i in contacts if i.draft_label]   
#
#    
#    add "images/ui/email/email_ground.png" 
#    hbox:
#      xpos 350
#      ypos 65
#      if new_message_count() > 0:
#          text ("{color=#000}Messages: %d (%d unread){/color}") % (message_count(), new_message_count())
#      else:
#          text ("{color=#000}Messages: %d{/color}") % message_count()
#    #frame:
#        #style_group "mailbox"
#    vbox:
#      hbox:
#        vbox:
#          label "{color=#000}{u}{b}Inbox{/b}{/}{/color}" xpos 65 ypos 150
#          side "c r":
#              area (64,154,321,520)
#              viewport id "message_list":
#                  draggable True mousewheel True
#                  vbox:
#                      for i in mail:
#                          if i.view:
#                              if not i.read:
#                                  textbutton ("*NEW* " + i.sender + " - " + i.subject) action [SetScreenVariable("current_message",i), i.mark_read] xfill True
#                              else:
#                                  textbutton (i.sender + " - " + i.subject) action SetScreenVariable("current_message",i) xfill True
#              vbar value YScrollValue("message_list")
#      #hbox:
#        #  null height 20
#    vbox:
#      side "c r":
#        area (430,180,530,520)
#        viewport id "view_message":
#            draggable True mousewheel True
#            vbox:
#                if current_message:
#                    text ("{color=#000}From: " + GetAddressFromSender(current_message.sender) + "{/color}")
#                    text ("{color=#000}To: " + GetAddressFromSender("Simone") + "{/color}")  
#                    text ("{color=#000}Subject: " + current_message.subject + "{/color}")
#                    text ("")
#                    text "{color=#000}" + current_message.body + "{/color}"
#                    if (current_message.intro == ""):
#                      pass
#                    else:
#                      vbox:
#                        frame:
#                          #text ("{color=#000}\n---------------------------------------------\n{/color}")
#                          text ("{color=#000}>" + current_message.intro + "{/color}")
#                        frame:
#                          #text ("{color=#000}\n---------------------------------------------\n{/color}")
#                          text ("{color=#000}>>" + "Older email here" + "{/color}")
#                        frame:
#                          #text ("{color=#000}\n---------------------------------------------\n{/color}")
#                          text ("{color=#000}>>>" + "Oldestest email here" + "{/color}")
#                      #text ("{color=#000}\n---\n{/color}")
#        vbar value YScrollValue("view_message")
#
#    use mailbox_commands
  
#screen mailbox_commands:
#    hbox:
#        xpos 60
#        ypos 120
#        if available_drafts:
#            textbutton "Draft New" action Show("contacts")
#        else:
#            textbutton "Draft New" action None
#        if current_message and current_message.reply_label:
#            textbutton "Reply" action current_message.reply
#        else:
#            textbutton "Reply" action None
#        if current_message:
#            textbutton "Delete" action [current_message.delete, SetScreenVariable("current_message", None)]
#        else:
#            textbutton "Delete" action None
#        if new_message_count() > 0:
#            textbutton "Mark All Read" action mark_all_read
#        else:
#            textbutton "Mark All Read" action None
#        textbutton "Restore All" action restore_all
#        textbutton "Exit" action Hide("mailbox")
        
screen contacts:
    modal True
    add "images/ui/email/email_overlay_ground.png"
    add "images/ui/email/Compose Text.png"
    
    label Simone_email xpos 345 ypos 236
    frame:
      style_group "pref"
      background None
      xsize 200
      xpos 335
      ypos 240
      vbox:
        for name in contacts:
            if name.draft_label:
                textbutton name.name xsize 200 action [name.draft, Hide("contacts")]#, ShowMenu("draft_menu", name.draft)]
            else:
                textbutton name.name xsize 200 action None
        textbutton "Close" xsize 200 action [Hide("contacts")]

init -2 python:
    style.mailbox = Style(style.default)
    style.mailbox_vbox.xalign = 0.5
    style.mailbox_vbox.xfill = True
    style.mailbox_hbox.xalign = 0.5
    style.mailbox_label_text.size = 30
    style.mailbox_label_text.xalign = 0.5
    style.mailbox_label.xfill = True
    #style.mailbox_frame.xalign = 0.5
    #style.mailbox_frame.yalign = 0.5
    #style.mailbox_frame.xpos = 200
    #style.mailbox_frame.ypos = 260
    style.mailbox_frame.background = None
    
# updated choice screen    
screen choice:
    if reply_screen or draft_screen:

          add "images/ui/email/email_overlay_ground.png" 
          if reply_screen:
              add "images/ui/email/Compose Text.png"      
          else:
              add "images/ui/email/Compose Text.png"      
          vbox:
              style_group "file_picker_nav"
              xpos 345 
              ypos 236
              #xpos 150
              #ypos 280
              if reply_screen:
                  text ("{color=#000}" + GetAddressFromSender("Simone") + "{/color}")     
                  text ("{color=#000}" + GetAddressFromSender(current_message.sender) + "{/color}")                
                  text ("{color=#000}Re: " + current_message.subject + "{/color}")             
                  #text ("")             
                  #text ("{color=#000}" + current_message.intro + "{/color}")
              else:
                  text ("{color=#000}" + GetAddressFromSender("Simone") + "{/color}")   
                  text ("{color=#000}" + GetAddressFromSender(contact.name) + "{/color}")
                  text ("{color=#000}" + message_title + "{/color}")           
                  #text ("")                        
                  #text ("{color=#000}" + contact.intro + "{/color}") xpos -50      
              null  height 30

              for caption, action, chosen in items:

                  if action:
                      button:
                          action action
                          xminimum int(config.screen_width * 0.5)
                          xmaximum int(config.screen_width * 0.5)
                          #style "menu_choice_button" 
                          xalign 0.5

                          text caption text_align 0.5

                  else:
                      text caption #style "menu_caption"
                        
    else:
        # this is the default choice menu
        window:
            style "menu_window"
            xalign 0.5
            yalign 0.5

            vbox:
                #style_group "file_picker_nav"
                style "menu"
                spacing 2

                for caption, action, chosen in items:

                    if action:

                        button:
                            action action
                            style "menu_choice_button"

                            text caption style "menu_choice"

                    else:
                        text caption style "menu_caption"    