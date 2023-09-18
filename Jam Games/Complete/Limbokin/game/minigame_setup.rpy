######################################
# Some Assumptions about image names #
######################################
# The minigame code makes the assumption that the images are named "minigame_buyer<#> <figure>" and "minigame_buyer<#> clothes<#>"
# For example, minigame_buyer0 pokerfigure, minigame_buyer1 heartfigure, minigame_buyer2 clothes0, etc
# (This also means you can use layeredimage to change expression if you'd like)
# If you want to change image names, you'll have to update code in minigame_run.rpy that shows things, as well as the screen with drag and drop

# All the images in /images/minigame/ are so named and the naming conventions should be followed for the final game

# All of the other images in /images/ can be ignored (see "Image aliases" below)

############################################################
# Things to update when this is plugged into the real game #
############################################################

# Image aliases to the temporary files; update to the real file names
image minigame_limbokin_bg = "limbokinbg"

# The dict of buyer number to object (question responses and correct answer)
# TODO: Update me with actual text responses and the correct article of clothing
# The format is (name, greeting, response to "How did you die", response to "Life in purgatory", response to "one more day",
#                post-question dialogue, list of clothing preferences from most preferred to least preferred, closing dialogue)
define minigame_buyer_map = {
    0 : MinigameBuyer("Limbokin No. 1",
        "lbl_minigame_1_Intro",
        "lbl_minigame_1_Die",
        "lbl_minigame_1_Purgatory",
        "lbl_minigame_1_Earth",
        "So you got a clothing item for me or what?",
        [2, 1, 0],
        "I can give you one tooth for that.",
        "I can give you two teeth for that."),
    1 : MinigameBuyer("Limbokin No. 2",
        "lbl_minigame_2_Intro",
        "lbl_minigame_2_Die",
        "lbl_minigame_2_Purgatory",
        "lbl_minigame_2_Earth",
        "Anyway, what do you have for me, bro?",
        [0, 1, 2],
        "I can give you one tooth for that.",
        "I can give you two teeth for that."),
    2 : MinigameBuyer("Limbokin No. 3",
        "lbl_minigame_3_Intro",
        "lbl_minigame_3_Die",
        "lbl_minigame_3_Purgatory",
        "lbl_minigame_3_Earth",
        "So what clothing item are you offering me, child?",
        [1, 0, 2],
        "I can give you one tooth for that.",
        "I can give you two teeth for that."),
    3 : MinigameBuyer("Limbokin No. 4",
        "lbl_minigame_4_Intro",
        "lbl_minigame_4_Die",
        "lbl_minigame_4_Purgatory",
        "lbl_minigame_4_Earth",
        "Oh. You have something t-to t-trade me?",
        [2, 0, 1],
        "I c-can g-give you one t-tooth for t-that.",
        "I c-can g-give you t-two t-teeth for t-that."),
    4 : MinigameBuyer("Limbokin No. 5",
        "lbl_minigame_5_Intro",
        "lbl_minigame_5_Die",
        "lbl_minigame_5_Purgatory",
        "lbl_minigame_5_Earth",
        "Hee-hee. So what clothing item am I getting?",
        [1, 2, 0],
        "I can give you one tooth for that.",
        "I can give you two teeth for that."),
    5 : MinigameBuyer("Limbokin No. 6",
        "lbl_minigame_6_Intro",
        "lbl_minigame_6_Die",
        "lbl_minigame_6_Purgatory",
        "lbl_minigame_6_Earth",
        ". . . Trade?",
        [0, 2, 1],
        ". . . Can give you one tooth.",
        "",
        "lbl_minigame_6_two_teeth"),
    6 : MinigameBuyer("Limbokin No. 7",
        "lbl_minigame_7_Intro",
        "lbl_minigame_7_Die",
        "lbl_minigame_7_Purgatory",
        "lbl_minigame_7_Earth",
        "Let's cut to the chase. What do you have for me?",
        [1, 0],
        "I can give you one tooth for that.",
        "I can give you two teeth for that."),
}

# The character used to respond to questions you ask the current buyer; customize as desired
define minigame_buyer = Character("{size=-15}[minigame_buyer_name]{/size}")

# The player character; alias to the existing one or remove it or change how the player speaks
define minigame_player = Character("Cris")

# These buyer numbers only have two clothing choices
define minigame_fewer_options = [6]


####################################################
# You should not need to touch anything under here #
####################################################
default minigame_buyer_name = ""
default minigame_teeth = 0
default minigame_trades = 0
default minigame_current_buyer = 0
default minigame_selected_clothing = ""
default minigame_buyer_offer = 0

image minigame_white_bg = "#ffffff"
#image minigame_white_bg = "#b7b5b6"

init -1 python:
    class MinigameBuyer:
        def __init__(self, name, greeting, die_response, life_response, earth_response, trade_dialogue, clothing_order, trade1_response, trade2_response, trade2_label=None):
            self.name = name
            self.greeting = greeting
            self.die_response = die_response
            self.life_response = life_response
            self.earth_response = earth_response
            self.trade_dialogue = trade_dialogue
            self.clothing_order = clothing_order
            self.trade1_response = trade1_response
            self.trade2_response = trade2_response
            self.trade2_label = trade2_label