
#Screen with all the buttons
screen betatest_mode():
    frame:
        vbox:
            text "Signal an error:"
            textbutton "Grammar/typo" action SetVariable("typo_error", _last_say_what), Show("typo_error") #action Function(betatest, "Grammar/typo error"), Show("registered")
            textbutton "Sprite" action Function(betatest, "Sprite error"), Show("registered")
            textbutton "Other" action Show("other_error")

#Feedback so the betatester knows everything is well send.
screen registered():
    frame:
        text "This has been registered"
    timer 1.5 action Hide("registered")

#Free error screen
default error_name = ""
screen other_error():
    modal True
    frame:
        vbox:
            text "Describe the error"
            input:
                 value VariableInputValue("error_name")
            textbutton "Submit":
                 keysym "K_RETURN"
                 action Function(betatest, error_name), Show("registered"), Hide("other_error")

#Retrieve text to correct it more easily.
default typo_error = ""
screen typo_error():
    zorder 100
    modal True
    predict False
    frame:
        vbox:
            text "Correct the error:"
            input:
                value VariableInputValue("typo_error")
            textbutton "Submit":
                 keysym "K_RETURN"
                 action Function(betatest, "grammar/typo error", typo_error), Show("registered"), Hide("typo_error")
            textbutton "Cancel":
                action Hide("typo_error")


#Send the text to the betatest.txt
init -1 python:
    def betatest(type, correct = None):
        file = open( os.path.join( renpy.config.gamedir, "betatest.txt" ), 'a' )

        nb_line = renpy.get_filename_line()
        line = _last_say_what #renpy.reshow_say()
        if correct != None:
            file.write(" - Error line : \"{}\" at {} \n > Correction to make : {} : {} \n \n".format(line, nb_line, type, correct))
        else:
            file.write(" - Error line : \"{}\" at {} \n > Correction to make : {} \n \n".format(line, nb_line, type))
        file.close()
