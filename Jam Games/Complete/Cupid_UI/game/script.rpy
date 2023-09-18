#BUILD 12
define r = Character('Rosa', color="#ff8787", ctc="ctc_blink", ctc_position="fixed")
define g = Character('Guilleme', color="#CAA4FF", ctc="ctc_blink", ctc_position="fixed")
define c = Character('Catherine', color="#cd953b", ctc="ctc_blink", ctc_position="fixed")
define ug = Character('Rose Girl', color="#ff8787", ctc="ctc_blink", ctc_position="fixed")
define f = Character('François Perride', color="#c8ffc8", ctc="ctc_blink", ctc_position="fixed")
define a = Character('Émilie', color="#c8ffc8", ctc="ctc_blink", ctc_position="fixed")
define m = Character(None,
    what_color="#fff",
    window_background="gui/mnvlbg.png",
    window_xalign=0.5,
    window_yalign=0.5,
    what_yalign=0.5)

#Extras#
define b = Character('Boy', color="#fff", ctc="ctc_blink", ctc_position="fixed")
define d = Character('Girl', color="#fff", ctc="ctc_blink", ctc_position="fixed")
define u = Character('???', color="#fff", ctc="ctc_blink", ctc_position="fixed")
define la = Character('Rich Lady 1', color="#FFF", ctc="ctc_blink", ctc_position="fixed")
define la2 = Character('Rich Lady 2', color="#FFF", ctc="ctc_blink", ctc_position="fixed")
define la3 = Character('Rich Lady 3', color="#FFF", ctc="ctc_blink", ctc_position="fixed")
define p = Character('Priest', color="#fff", ctc="ctc_blink", ctc_position="fixed")
define mn = Character('Mother', color="#fff", ctc="ctc_blink", ctc_position="fixed")
#Effects#
define o = Character(None, kind = nvl, 
    what_bold=True, 
    what_outlines=[ (2, "#000000") ])
define o2 = Character(None, kind = nvl)
define o3 = Character(None, kind = nvl, 
    what_bold=True, 
    what_size=50, 
    what_font="gui/iloveu.ttf",
    what_kerning=20)
    #what_outlines=[ (2, "#000000") ])
#Guilleme Inner Thoughts
define bg = Character(None, ctc="ctc_blink", 
    what_line_spacing=-20, 
    what_size=50, 
    what_font="gui/cupid.ttf", 
    ctc_position="fixed", 
    window_background="gui/redtextbox.png")
define gt = Character(None, what_size=30, what_font="gui/friday.ttf", what_color="#fff", what_outlines=[ (1, "#EC4F4F") ], 
  window_background="gui/gnvlbg.png", 
  window_xalign=0.5, 
  window_yalign=0.5, 
  what_yalign=0.5)
define gi = Character(None, what_color="#fff", what_outlines=[ (1, "#EC4F4F") ], 
  window_background="gui/gnvlbg.png", 
  window_xalign=0.5, 
  window_yalign=0.5, 
  what_yalign=0.5)
define cn = Character(None, what_color="#cd953b", window_background="gui/cnvlbg.png", 
  window_xalign=0.5, 
  window_yalign=0.5, 
  what_yalign=0.5)
define cm = Character(None, what_color="#3b98cd", window_background="gui/cnvlbg.png", 
  window_xalign=0.5, 
  window_yalign=0.5, 
  what_yalign=0.5)
define ra = Character(None,
    what_color="#fff",
    what_size=40,
    what_font="gui/iloveu.ttf",
    window_background="gui/mnvlbg.png",
    window_xalign=0.5,
    window_yalign=0.5,
    what_yalign=0.5)


#Journal
define gd = Character(None, what_color="#ffffff", what_font="gui/arno.otf",
  what_text_align=0,
  what_italic = True,
  #window_xalign=0.5, 
  window_yalign=0.5, 
  what_yalign=0.5,
  window_background=None)
define su = Character(None, kind=nvl, what_color="#ffffff")
define s = Character(None, what_color="#fff")

define gd2 = Character(None, what_color="#ffffff", what_font="gui/arno.otf",
  what_text_align=0,
  what_size=20,
  what_italic = True,
  window_yalign=0.5, 
  what_yalign=0.5,
  window_background=None)
#Epilogue
define n = Character(None, what_color="#FAFAD2",
  window_xalign=0.5, 
  window_yalign=0.5, 
  what_yalign=0.5)
define gr = Character(None, what_color="#DC143C",
  window_xalign=0.5, 
  window_yalign=0.5, 
  what_yalign=0.5)


init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    $ goodperson = False
    $ badpeople = False
    $ badperson = False
    $ openlocket = False
    $ closelocket = False
    $ rosamonster = False
    $ revenge = False
    $ punish = False
    $ justice = False
    $ knife = False
    $ book = False
    $ dagger = False
    $ takekey = False
    $ nochange = False
    $ rgloves = False
    $ nokillg = False
    $ cathselfish = False
    $ morejournal = False
    $ silentmom = False
    $ rosajealous = False
    $ family = False
    $ friends = False
    $ goodmom = False
    $ badmom = False
    $ cynicalmom = False
    $ origin = False
    $ byemom = False
    $ rcloves = False
   
    $ cmom = 0
    $ cmomcount = 0

    $ mmom = 0
    $ mmomcount = 0

    $ rglove = 0
    $ rglovecount = 0
    
    $ rclove = 0
    $ rclovecount = 0

    $ meanmom = 0
    $ meanmomcount = 0
    
    $ nvl_darkbg = False
    
    
    #default only sets the value once if it doesn't exist, otherwise leaves it alone so it wont be reset
    default persistent.EndingUnlocked = 0
    default persistent.totalLines = 52
    default persistent.currentLinesRead = 0
    default persistent.origin = False 
    
init python:
    achievement.register("ACH_UNLOCK_ALL_ENDS", steam="Unlocked All Endings", stat_max=6) # the total endings goes in the stat_max field

label start:
    #call lbl_achievementTest from _call_lbl_achievementTest
    python:
        if persistent.adult is None:
            persistent.adult = False
            achievement.grant("Playing as an Adult")
    call intro from _call_intro

return

label unlock_everything:
  scene bg black
  menu:
    "Unlock all chapters":  
      $persistent.IntroUnlocked = True
      $persistent.Chapter1Unlocked = True
      $persistent.Chapter2Unlocked = True
      $persistent.Chapter3Unlocked = True
      $persistent.Chapter4Unlocked = True
      $persistent.Chapter5Unlocked = True
      $persistent.Chapter6Unlocked = True
      $persistent.Chapter7Unlocked = True
      $persistent.Chapter8Unlocked = True
      show bg black
      "Chapters all unlocked."
      
    "Unlock all endings":
      $persistent.Ending1Unlocked = True
      $persistent.Ending2Unlocked = True
      $persistent.Ending3Unlocked = True
      $persistent.Ending4Unlocked = True
      $persistent.BonusEndingUnlocked = True
      show bg black
      "Endings all unlocked."
      
    "Unlock all event CGs":
      show bg rchurch
      show bg cfirstpiano
      show bg ckidg
      show bg rawe
      show bg csuicide3
      #chap2
      show bg grhug  
      show bg rpow
      show bg rosachoke
      show bg rosachokesafe
      show bg needles
      show bg needlessafe
      #piano
      show bg gchappy
      #sweet
      show bg rcbed
      show bg rcsweet3
      show bg cgbed
      #darktimes
      show bg gcsexay
      show bg gcsexay2
      show bg gcneckiss
      show bg gscary
      show bg cupidsexay
      #cathdown
      show bg cathcrazy
      show bg cathscratch
      show bg cathscratchsafe
      #chap6
      show bg scaredrosa
      show bg rgdread
      #chap7
      show bg gattacks
      #chap8
      show bg angrycupid3
      #end01
      show bg gclutch2
      #badend
      show bg rgtension
      show bg rgseduce
      show bg rosacray
      #end 04
      show bg gdiesdagger
      show bg gdiesdaggersafe
      show bg gdiesknife
      show bg gdiesknifesafe
      show bg rgchoke
      show bg guilchoke
      #end02
      show bg gdiespeace
      show bg gdiespeace2kiss
      #end03
      show bg rgcarry
      #secret end
      show bg rgkiss
      show bg rgdeepkiss
      show drunkpic
      
      scene bg black
      "Event CGs all unlocked."
      
    "Unlock all Music Tracks":    
      #list the Music Box songss here 
      play music "sfx/intro2.ogg"
      play music "sfx/churchraw.ogg"
      play music "sfx/partyraw.ogg"
      play music "sfx/catsfirstperf.ogg"
      play music "sfx/waltz.ogg"
      play music "sfx/garden.ogg"
      play music "sfx/quietsadness.ogg"
      play music "sfx/sorrow.ogg"
      play music "sfx/cathsadsong.ogg"
      play music "sfx/fastsong.ogg"
      play music "sfx/library.ogg"
      play music "sfx/nature.ogg"
      play music "sfx/friends.ogg"
      #demo
      play music "sfx/catsaria.ogg"
      play music "sfx/sweetune2.ogg"
      play music "sfx/loverstango.ogg"
      play music "sfx/mellow.ogg"
      play music "sfx/spooks.ogg"
      play music "sfx/journal0.ogg"
      play music "sfx/night2.ogg"
      play music "sfx/darksexy.ogg"
      play music "sfx/cathsfinal.ogg"
      play music "sfx/bitterness.ogg"
      play music "sfx/sadness.ogg"
      play music "sfx/gbeat.ogg"
      play music "sfx/journal.ogg"
      play music "sfx/rosadecides.ogg"
      play music "sfx/nightterror.ogg"
      play music "sfx/intro.ogg"
      play music "sfx/confront.ogg"
      play music "sfx/spider.ogg"
      play music "sfx/badend.ogg"
      play music "sfx/bittersweet.ogg" 
      stop music
      show bg black
      "Music Tracks all unlocked."
    "Unlock all Steam Achievements":    
      $ achievement.grant("Playing as an Adult")
      $ achievement.grant("Angry Start")
      $ achievement.grant("Mother's Intuition")
      $ achievement.grant("Cynical Mother")
      $ achievement.grant("Justice Fighter")
      $ achievement.grant("A Grudge")
      $ achievement.grant("Insensitive")
      $ achievement.grant("Nonchalant")
      $ achievement.grant("Catherine's 24k")
      $ achievement.grant("Bull by the Horns")
      $ achievement.grant("The Promise")
      $ achievement.grant("Freedom")
      $ achievement.grant("The Talk")
      $ achievement.grant("The Creature")
      $ achievement.grant("Filthy Colours")
      $ achievement.grant("Domestic Abuse")
      $ achievement.grant("Sacrilege and Sex")
      $ achievement.grant("Marquis de Sade")
      $ achievement.grant("Incomplete Journal")
      $ achievement.grant("More Entries to unlock")
      $ achievement.grant("Unlocked all entries")
      $ achievement.grant("Green-Eyed")
      $ achievement.grant("Monster")
      $ achievement.grant("Spectral Handjob")
      $ achievement.grant("Oral Sex from Hell")
      $ achievement.grant("Nightmare Fuel")
      $ achievement.grant("Jealousy")
      $ achievement.grant("Bloody Cupid")
      $ achievement.grant("Wet Dream Gone Bad")
      $ achievement.grant("Does not Form Scars")
      $ achievement.grant("Victim Mentality")
      $ achievement.grant("Father and Child")
      $ achievement.grant("Love is my Drug")
      $ achievement.grant("Sound Advice")
      $ achievement.grant("New Beginnings")
      $ achievement.grant("Agape's Blessing")
      $ achievement.grant("Emilie's Fate")
      $ achievement.grant("Jealous Catherine")
      $ achievement.grant("Guilleme's Soliloquy")
      $ achievement.grant("What makes a good parent?")
      $ achievement.grant("Dysfunctional Family")
      $ achievement.grant("Mother's Past")
      $ achievement.grant("Mother")
      $ achievement.grant("Little Thief")
      $ achievement.grant("Closure")
      $ achievement.grant("Love is Bittersweet")
      $ achievement.grant("Guilleme's Redemption")
      $ achievement.grant("Poison and Cure")
      $ achievement.grant("Play it Again")
      $ achievement.grant("Never Pure")
      $ achievement.grant("Dedication!")
      $ achievement.grant("Dark Fairytale")
      $ achievement.grant("Pat the Bunny")
      $ achievement.grant("Drawing Blood")
      $ achievement.grant("Punisher")
      $ achievement.grant("Angel of Vengeance")
      $ achievement.grant("Squick")
      $ achievement.grant("Fan Disservice")
      $ achievement.grant("Fourth Wall")
      $ achievement.grant("Emptiness")
      $ achievement.grant("Hostage")
      $ achievement.grant("Implied Incest")
      $ achievement.grant("This should have been a comedy")
      $ achievement.grant("Modern Day Cupid")
      $ achievement.grant("Unlocked All Endings")
      $ achievement.grant("Unlocked all of Guilleme's entries")
      $ achievement.grant("You don't mean..?")
      $achievement.Sync()
      show bg black
      "Steam Achievements all unlocked."
    "Reset Unlocks":
      "Warning, this will reset all game data including already seen dialog."
      "This will not reset Gallery or Music Box."
      "Are you sure?"
      menu:
        "Reset game data.":
          $ persistent._clear()
          $ renpy.save_persistent()
          "Game Data all reset. You may need to restart game to see all effects."
        "Reset Steam Achievements": 
          $achievement.clear_all()
          $achievement.Sync()  
          "Steam Achievements all reset. You may need to restart game to see all effects."
        "No, I want to keep things as they are":
          pass   
    "All done":      
      $ renpy.end_replay()
      return
      
  jump unlock_everything   
    
return
#label lbl_achievementTest:
#
#  "Testing achievements"
#  
#  menu:
#    "reset all achievements":
#      $achievement.clear_all()
#      $achievement.Sync()  
#      "Clear all achievements"
#      #"[achievement]"
#    "reset adult achievement":
#      $achievement.clear("Playing as an Adult")
#      $achievement.Sync()  
#      "Achievement cleared"
#    "Give adult achievement":    
#      if not achievement.has("Playing as an Adult"):
#          $ achievement.grant("Playing as an Adult")
#          init:
#              $ achievement.register("Playing as an Adult")
#              $ achievement.sync()
#          $ achievement.sync()
#          "Achievement granted"
#      else:
#        "You already have this achievement"
#    "Give freedom achievement":    
#      if not achievement.has("Freedom"):
#          $ achievement.grant("Freedom")
#          init:
#              $ achievement.register("Freedom")
#              $ achievement.sync()
#          $ achievement.sync()
#          $ achievement.Sync()  
#          "Achievement granted"
#      else:
#        "You already have this achievement"
#    "Dont reset":
#      $ achievement.sync()
#      $ achievement.Sync()
#      pass
#    "continue game":
#      return
#  
#  jump lbl_achievementTest