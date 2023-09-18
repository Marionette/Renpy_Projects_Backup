#BUILD 12
label summary0:
    stop music fadeout 2.0
    scene bg choices 
    if (GetEndingCount() >= 5):   
      $ achievement.grant("Unlocked All Endings")
      $achievement.Sync()
    show screen endingbit
    ""    
    $ renpy.full_restart()   
    return
    
screen endingbit():
    style_prefix "summary"
    vbox:
        if revenge:
            text "{size=-4}Your main purpose was revenge.\n{/size}"
        elif justice:
            text "{size=-4}Your main purpose was justice.\n{/size}"
      
        if cmom >= 6:
            text "{size=-4}You chose to control Rosa by being demanding and controlling.{/size}"
        if mmom >= 6:
            text "{size=-4}You chose to control Rosa by being emotionally manipulative.{/size}"
        if meanmom >= 8:
            text "{size=-4}You were verbally abusive to Rosa.{/size}"
        if goodmom:
            text "{size=-4}You loved Rosa despite your misgivings.{/size}"
        elif byemom:
            text "{size=-4}You gave Rosa her freedom by saying goodbye.{/size}"
 
        if rosamonster:
            text "{size=-4}You called Rosa a monster.{/size}"
        if openlocket:
            text "{size=-4}You opened Guilleme's locket.{/size}"
        elif closelocket:
            text "{size=-4}You left Guilleme's locket closed.{/size}"
        if rglove >= 4:
            text "{size=-4}You believed Rosa is in love with Guilleme.{/size}"
        if rcloves and not rgloves:
            text "{size=-4}You believed Rosa is in love with Catherine.{/size}"
        if family:
            text "{size=-4}You told Rosa that family is the most important thing.{/size}"
        if cathselfish:
            text "{size=-4}You convinced Rosa that Catherine was selfish.{/size}"       
        if morejournal:
            text "{size=-4}You wanted to read more of Guilleme's journal.{/size}"     
        if dagger:
            text "{size=-4}You made Rosa steal Guilleme's dagger.{/size}"
        elif takekey:
            text "{size=-4}You took Guilleme's key.{/size}"
        if nochange:
            text "{size=-4}You didn't believe Guilleme could change.{/size}"

        if nokillg:
            text "{size=-4}You admitted that killing Guilleme might not be the only answer.{/size}"
        if knife:
            text "{size=-4}You advised Rosa to take the knife from the kitchen.{/size}"
        $completion = GetCompletionPercentage()
        text "{size=-4}\n[completion]% complete.{/size}"
          
return

style summary_vbox:
    xalign 0.5
    yalign 0.5
    spacing gui.choice_spacing

style summary_text:
    xalign 0.5