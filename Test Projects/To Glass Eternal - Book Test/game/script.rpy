# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define o = Character(None, kind = nvl)
define m = Character("m", kind = nvl)
image bg background = "gui/overlay/game_menu.png"


# The game starts here.

label start:

    jump nvltest

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return


label nvltest:
    scene bg background
    "nvl test"
    nvl clear
    o "He didn't limit himself to royalty, or so the tabloids said."
    nvl clear
    o "His latest fling was with an English poet--"
    o "--who, they say, almost killed him when he was caught with another man--"
    o "Or woman..."
    nvl clear
    o "Ah... at this point, who knew what was real and what was a blatant lie made up by the newspapers?"
    nvl clear
    o "She had looked forward to meeting him."
    o "And here he was, finally."
    nvl clear
    o "...Talking about sampling the new bakery's crème brûlée."
    o "Émilie sighed."
    
    nvl clear
    o "...Talking about sampling the new bakery's crème brûlée."
    o "Émilie sighed."
    o "...Talking about sampling the new bakery's crème brûlée."
    o "Émilie sighed."
    o "...Talking about sampling the new bakery's crème brûlée."
    o "Émilie sighed."
    o "...Talking about sampling the new bakery's crème brûlée."
    o "Émilie sighed."
    o "...Talking about sampling the new bakery's crème brûlée."
    o "Émilie sighed."
    o "...Talking about sampling the new bakery's crème brûlée."
    o "Émilie sighed."
    o "...Talking about sampling the new bakery's crème brûlée."
    o "Émilie sighed."
    o "...Talking about sampling the new bakery's crème brûlée."
    o "Émilie sighed."
    o "...Talking about sampling the new bakery's crème brûlée."
    o "Émilie sighed."
    o "...Talking about sampling the new bakery's crème brûlée."
    o "Émilie sighed."
    o "...Talking about sampling the new bakery's crème brûlée."
    o "Émilie sighed."
    o "...Talking about sampling the new bakery's crème brûlée."
    o "Émilie sighed."
    o "...Talking about sampling the new bakery's crème brûlée."
    o "Émilie sighed."
    o "...Talking about sampling the new bakery's crème brûlée."
    o "Émilie sighed."
    o "...Talking about sampling the new bakery's crème brûlée."
    o "Émilie sighed."
    o "...Talking about sampling the new bakery's crème brûlée."
    o "Émilie sighed."
    o "...Talking about sampling the new bakery's crème brûlée."
    o "Émilie sighed."
    
    
    nvl clear
    o "Émilie sighed."
    o "This is a mistake. Here, we’ll refer to some time-honored typesetting conventions, with an emphasis on readability, and offer guidance on adapting them effectively for devices and screens. We’ll see that the ability to embed fonts with @font-face is not by itself a solution to all of our typographic challenges./n/nBursting with imagery, motion, interaction and distraction though it is, today’s World Wide Web is still primarily a conduit for textual information. In HTML5, the focus on writing and authorship is more pronounced than ever. It’s evident in the very way that new elements such as article and aside are named. HTML5 asks us to treat the HTML document more as… well, a document./nIt’s not just the specifications that are changing, either. Much has been made of permutations to Google’s algorithms, which are beginning to favor better written, more authoritative content (and making work for the growing content strategy industry). Google’s bots are now charged with asking questions like, “Was the article edited well, or does it appear sloppy or hastily produced?” and “Does this article provide a complete or comprehensive description of the topic?,” the sorts of questions one might expect to be posed by an earnest college professor./nThis increased support for quality writing, allied with the book-like convenience and tactility of smartphones and tablets, means there has never been a better time for reading online. The remaining task is to make the writing itself a joy to read./nWhat Is The Perfect Paragraph?/nAs designers, we are frequently and incorrectly reminded that our job is to “make things pretty.” We are indeed designers — not artists — and there is no place for formalism in good design. Web design has a function, and that function is to communicate the message for which the Web page was conceived. The medium is not the message./n/nNever is this principle more pertinent than when dealing with type, the bread and butter of Web-borne communication. A well-set paragraph of text is not supposed to wow the reader; the wowing should be left to the idea or observation for which the paragraph is a vehicle. In fact, the perfect paragraph is unassuming to the point of near invisibility. That is not to say that the appearance of your text should have no appeal at all. On the contrary: well-balanced, comfortably read typography is a thing of beauty; it’s just not the arresting sort of beauty that might distract you from reading./n/nAs a young industry that champions innovation and rates its practitioners based on their ability to apprehend (sorry, “grok”) the continual emergence of new technologies, frameworks, protocols and data models, we are not particularly familiar with tradition. However, the practice of arranging type for optimal pleasure and comfort is a centuries-old discipline. As long ago as 1927, the noted typographer Jan Tschichold spoke of the typesetting “methods and rules upon which it is impossible to improve” — a set of rules it would be foolish to ignore./n/nSo, please put your canvas element and data visualization API to one side just for a short while. We are about to spend a little time brushing up on our typesetting skills. It’s called “hypertext,” after all."
    
    nvl clear
    
    $story = """
    This is a mistake. Here, we'll refer to some time-honored typesetting conventions, with an emphasis on readability, and offer guidance on adapting them effectively for devices and screens. We'll see that the ability to embed fonts with @font-face is not by itself a solution to all of our typographic challenges.
    
    Bursting with imagery, motion, interaction and distraction though it is, today’s World Wide Web is still primarily a conduit for textual information. In HTML5, the focus on writing and authorship is more pronounced than ever. It’s evident in the very way that new elements such as article and aside are named. HTML5 asks us to treat the HTML document more as… well, a document.

    It’s not just the specifications that are changing, either. Much has been made of permutations to Google’s algorithms, which are beginning to favor better written, more authoritative content (and making work for the growing content strategy industry). Google’s bots are now charged with asking questions like, "Was the article edited well, or does it appear sloppy or hastily produced?" and "Does this article provide a complete or comprehensive description of the topic?," the sorts of questions one might expect to be posed by an earnest college professor.

    This increased support for quality writing, allied with the book-like convenience and tactility of smartphones and tablets, means there has never been a better time for reading online. The remaining task is to make the writing itself a joy to read.

    What Is The Perfect Paragraph?
    As designers, we are frequently and incorrectly reminded that our job is to "make things pretty." We are indeed designers — not artists — and there is no place for formalism in good design. Web design has a function, and that function is to communicate the message for which the Web page was conceived. The medium is not the message.

    Never is this principle more pertinent than when dealing with type, the bread and butter of Web-borne communication. A well-set paragraph of text is not supposed to wow the reader; the wowing should be left to the idea or observation for which the paragraph is a vehicle. In fact, the perfect paragraph is unassuming to the point of near invisibility. That is not to say that the appearance of your text should have no appeal at all. On the contrary: well-balanced, comfortably read typography is a thing of beauty; it’s just not the arresting sort of beauty that might distract you from reading.


    As a young industry that champions innovation and rates its practitioners based on their ability to apprehend (sorry, “grok”) the continual emergence of new technologies, frameworks, protocols and data models, we are not particularly familiar with tradition. However, the practice of arranging type for optimal pleasure and comfort is a centuries-old discipline. As long ago as 1927, the noted typographer Jan Tschichold spoke of the typesetting “methods and rules upon which it is impossible to improve” — a set of rules it would be foolish to ignore.

    So, please put your canvas element and data visualization API to one side just for a short while. We are about to spend a little time brushing up on our typesetting skills. It’s called "hypertext," after all.
    
    
    """
    
    o "[story]"
    
    nvl clear
    o "{i}It was an accident! It was nothing but an accident!{/i}"
    m "...Was it?"
    nvl clear
    o "{i}She pushed first!{/i}"
    nvl clear
    o "{i}She got really scary.{/i}"
    o "{i}She strangled me.{/i}"
    m "What? That's absurd!"
    m "Are you sure?"
    m "Would she do that?"
    nvl clear
    o "{i}I--I don't know..{/i}"
    nvl clear
    o "{i}I think she did.{/i}"
    "end nvl test"
    