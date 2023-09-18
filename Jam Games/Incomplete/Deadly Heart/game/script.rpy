# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image Aiyora happy = "Aiyora1.png"
image Ison happy = "Ison1.png"
image Sorben happy = "Sorben1.png"
image Maika happy = "Maika1.png"
image bgBlack = "#000F"

# Declare characters used by this game.
define Aiyora = Character('Aiyora', color="#c8ffc8")
define a = Character('Aiyora', color="#c8ffc8")
define Ison = Character('Ison', color="#c8ffc8")
define i = Character('Ison', color="#c8ffc8")
define Sorben = Character('Sorben', color="#c8ffc8")
define s = Character('Sorben', color="#c8ffc8")
define Maika = Character('Maika', color="#c8ffc8")
define m = Character('Maika', color="#c8ffc8")

screen CharacterSelect_imagemap:
    imagemap:
        auto "1CharacterSelectImageMap_%s.png"
        hotspot (000,0,320,600)  action Return("Aiyora")
        hotspot (320,0,500,600) action Return("Ison")
        hotspot (500,0,620,600)  action Return("Sorben")
        hotspot (620,0,800,600)  action Return("Maika")


# The game starts here.
label start:
    scene bgBlack

    "Who should take the first step on this journey?"
    # Show an imagemap.
    window hide None
    call screen CharacterSelect_imagemap
    window show None

    
    if _return == "Aiyora":
        jump lbl_chooseAiyora
    elif _return == "Ison":
        jump lbl_chooseIson
    elif _return == "Sorben":
        jump lbl_chooseSorben
    elif _return == "Maika":
        jump lbl_chooseMaika


label lbl_chooseAiyora:
    show Aiyora happy at right
    Aiyora "Thank you for picking me."
    jump lbl_AiyoraPathStart
    
label lbl_chooseIson:
    show Ison happy at right
    Ison "What are your orders?"
    jump lbl_END

label lbl_chooseSorben:
    show Sorben happy at right
    Sorben "Picking me? You're smarter than you look."
    jump lbl_END

label lbl_chooseMaika:
    show Maika happy at right
    Maika "You picked me, now lets play!"
    jump lbl_END

        
label lbl_GOOD_END:
    return
label lbl_END:
    jump start
    return
