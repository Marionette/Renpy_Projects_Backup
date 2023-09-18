label bonus:
    scene bg black
    menu:
        "Production Jokes"
        "Bonus 1: Alternate End..?":
            jump bonus1
        "Bonus 2: How-to game goals":
            jump bonus2
        "Bonus 3: Guilleme's Face":
            jump bonus3
        "Back to Bonus Screen":
            #$ renpy.call_screen("extra_bonus")
            return
        
return
label bonus2:
    scene bg black
    m "I was discussing the story with one of the writers."
    m "She commented on the content of the story and asked what the eff I was really doing here."
    m "So I outlined my goals for her."
    m "Just so, you know..."
    m "There are no misconceptions."
    nvl clear
    o "Goal #1:{w} Sexually confuse straight female players."
    o "Goal #2: {w}Mommy issues."
    o "Goal #3: {w}Daddy issues."
    nvl clear
    m "The end!"
    $renpy.pause(delay=None)
    jump bonus
     
return

label bonus1:
    scene bg black
    m "After reading through one of the draft builds, somebody said,"
    nvl clear
    o "\"You know, if Catherine, Rosa, and Guilleme just had a threesome--\""
    o "\"All their problems would've been solved.\""
    nvl clear
    m "So if there ever was an alternate end, it would probably be like:"
    o "{i}And they had a threesome and lived happily ever after.{/i}"
    m "It brings tears to my eyes."
    nvl clear
    $renpy.pause(delay=None)
    jump bonus
    
return

label bonus3:
    scene bg black
    
    m "This came about when I was making expressions for the sprites."
    m "I accidentally duplicated Guilleme's facial expression to another project, which had a teapot."
    show gface 01 with dissolve

    "Look at that f***ing thing."
    "It landed right plop in the middle."
    "*agonizing laughter*"
    scene bg black with dissolve
    m "I set off to prove the theory:"
    m "{i}Does Guilleme's face fit on everything?{/i}"
    show gface 02 with dissolve
    with Pause(1)
    #show bg black with dissolve
    #with Pause(1)
    show gface 03 with dissolve
    with Pause(1)
    #show bg black with dissolve
    #with Pause(1)
    show gface 04 with dissolve
    show bg black with dissolve
    nvl clear
    o "Clearly."
    nvl clear
    $renpy.pause(delay=None)
    jump bonus
   
return

label origin:
    scene bg black
    $ persistent.origin = True
    m "You unlocked the \"Origins\" bonus."
    m "There will be hints of Mother's backstory peppered throughout the game now."
    m "Enjoy!"
    $renpy.pause(delay=None)
    $ renpy.call_screen("extra_bonus")
    
return
