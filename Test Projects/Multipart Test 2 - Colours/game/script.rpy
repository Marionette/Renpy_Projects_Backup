init python:
    mp = MultiPersistent("rosaxcath4eva2")

####### coloured name test ##############

image bg black = "#000000"
default pc = "Bob"
define character.b = Character("[pc]", who_color="00F")

define character.e = Character("Eileen", who_color="F00")

$ narrator=Character(None, ctc="ctc_blink", ctc_position="fixed")
#define r = Character('Rosa', color="#ff8787", ctc="ctc_blink", ctc_position="fixed")
#define g = Character('Guilleme', color="#CAA4FF", ctc="ctc_blink", ctc_position="fixed")
#define c = Character('Catherine', color="#cd953b", ctc="ctc_blink", ctc_position="fixed")
#define ug = Character('Rose Girl', color="#ff8787", ctc="ctc_blink", ctc_position="fixed")
#define f = Character('François Perride', color="#c8ffc8", ctc="ctc_blink", ctc_position="fixed")
#define a = Character('Émilie', color="#c8ffc8", ctc="ctc_blink", ctc_position="fixed")
#define m = Character(None,
#    what_color="#fff",
#    window_background="img/ui/mnvlbg.png",
#    window_xalign=0.5,
#    window_yalign=0.5,
#    what_yalign=0.5)
#
##Extras#
#define b = Character('Boy', color="#fff", ctc="ctc_blink", ctc_position="fixed")
#define d = Character('Girl', color="#fff", ctc="ctc_blink", ctc_position="fixed")
#define u = Character('???', color="#fff", ctc="ctc_blink", ctc_position="fixed")
#define la = Character('Rich Lady 1', color="#FFF", ctc="ctc_blink", ctc_position="fixed")
#define la2 = Character('Rich Lady 2', color="#FFF", ctc="ctc_blink", ctc_position="fixed")
#define la3 = Character('Rich Lady 3', color="#FFF", ctc="ctc_blink", ctc_position="fixed")
#define p = Character('Priest', color="#fff", ctc="ctc_blink", ctc_position="fixed")
#define mn = Character('Mother', color="#fff", ctc="ctc_blink", ctc_position="fixed")
##epilogue
#define n = Character(None,
#    what_color="#FFFACD",
#    what_size=25,
#    window_xalign=0.5,
#    window_yalign=0.5,
#    what_yalign=0.5)
#define gr = Character(None, 
#    what_color="#DC143C",
#    what_size=25,
#    window_xalign=0.5,
#    window_yalign=0.5,
#    what_yalign=0.5)
##Effects#
#define o = Character(None, kind = nvl, what_bold=True, what_outlines=[ (2, "#000000") ])
#define o2 = Character(None, kind = nvl)
#define bg = Character(None, ctc="ctc_blink", ctc_position="fixed", window_background="img/ui/redtextbox.png")
#define gt = Character(None, what_color="#fff", what_outlines=[ (1, "#EC4F4F") ], 
#  window_background="img/ui/gnvlbg.png", 
#  window_xalign=0.5, 
#  window_yalign=0.5, 
#  what_yalign=0.5)
#define cn = Character(None, what_color="#cd953b", window_background="img/ui/cnvlbg.png", 
#  window_xalign=0.5, 
#  window_yalign=0.5, 
#  what_yalign=0.5)
#define cm = Character(None, what_color="#3b98cd", window_background="img/ui/cnvlbg.png", 
#  window_xalign=0.5, 
#  window_yalign=0.5, 
#  what_yalign=0.5)
#define n = Character(None, what_color="#FAFAD2")
#define gr = Character(None, what_color="#DC143C")
#define gd = Character(None, what_color="#ffffff", what_font="assets/fonts/arno.otf",
#  #window_xalign=0.5, 
#  window_yalign=0.5, 
#  what_yalign=0.5,
#  what_justify=True,
#  what_center=False)
#define su = Character(None, kind=nvl, what_color="#ffffff")
#define s = Character(None, what_color="#fff")

######

define o = Character(None, kind = nvl)
#define o = Character(None, kind = nvl)
define o2 = Character(None, kind = nvl,  what_xalign=0.5, what_size=11)
define bg = Character(None, ctc="ctc_blink", ctc_position="fixed", window_background="img/ui/redtextbox.png")
define n = Character(None, what_color="#FFFACD", what_layout="subtitle", what_size=20, what_xalign=0.5,)
define gr = Character(None, what_color="#DC143C", what_layout="subtitle", what_size=20, what_xalign=0.5,)
define m = Character(None, what_color="#fff", what_size=20, what_layout="subtitle", what_xalign=0.5, what_text_align=0.5, window_background="img/ui/mnvlbg.png", window_yminimum=0, window_xfill=False,  window_xalign=0.5, window_yalign=0.5)
######

init python:

    char_colours = {}

    for key in character.__dict__:
        char = getattr( character, key )
        if hasattr( char, 'who_args' ):
            colour = char.who_args.get('color', None)
            if colour:
                char_colours[ char.name ] = (
                    "{{color={colour}}}{name}{{/color}}".format(
                        name=char.name, colour='#{0}'.format(colour)))

    def colourize_names( str_to_test ):
        for name in char_colours:
            str_to_test = str_to_test.replace(name, char_colours[name]) 
        return str_to_test

define config.say_menu_text_filter = colourize_names

label start:
    show screen betatest_mode
    scene solid("#ffffff")
    e "My name is Eileen..."
    b "Hi Eileen, my name's [pc]"
    b "Hi Eileen, my name's Bobbing Eileening"
    b "Hi Eileen, my name's [pc]"
    b "Hi Eileen, my name's [pc]"
    
    call nvltest
    
    jump lbl_multipersistant_test
    
    "thats all folks"
    return


label nvltest:
    scene bg black
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
    

label lbl_multipersistant_test:

    if mp.beat_part_1:
         e "I see you've beaten part 1, so welcome back!"
    else:
         e "Hmm, you haven't played part 1, why not try it first?"
    