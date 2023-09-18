
image bg jail = "BG/jail.jpg"
image bg bedroom = "BG/bedroom.jpg"
image bg kitchen = "BG/kitchen.jpg"
image bg school way = "BG/school way.jpg"
image bg classroom = "BG/classroom.jpg"
image bg classroome = "BG/classroom entrance.jpg"
image bg classroomb = "BG/classroom break.jpg"
image bg stairs = "BG/school corridor.jpg"
image bg street = "BG/street.jpg"
image bg hospital en = "BG/hospital corridor.png"
image bg hospital bed = "BG/hospital room.jpg"
image bg magici = "BG/magic institut.jpg"
image bg magici ins = "BG/magic institut inside.jpg"
image bg throneroom = "BG/throneroom.jpg"
image bg palace3 = "BG/palace3.jpg"
image bg palace bed = "BG/palace bedroom.jpg"
image bg dinning room = "BG/dinning room.jpg"
image bg courtyard = "BG/courtyard.jpg"
#image cgs Love Ending = "cgs/Love Ending.png"
#image cgs Sachi shot = "cgs/Sachi shoot.png"
#image cgs Kusanagi stabbed = "cgs/Kusanagi stabbed.png"
image scroll = "BG/scroll.png"
image magic = "BG/magic.png"
image magic dark = "BG/magic dark.png"
image yamakazi h = "Actors/Yamakazi h.png"
image yamakazi hf = "Actors/Yamakazi hf.png"
image yamakazi s = "Actors/suit.png"
image Yamakazi n = "Actors/Yamakazi.png"
image Yamakazi nf = "Actors/Yamakazi flipped.png"
image kai = "Actors/kai.png"
image teacher = "Actors/teacher.png"
image doctor = "Actors/doctor.png"
image doctor f = "Actors/doctor flipped.png"
image sachi = "Actors/sachi.png"
image sachi f = "Actors/sachi flipped.png"
image sachi a = "Actors/sachi angry.png"
image sachi af = "Actors/sachi angry flipped.png"
image sachi c = "Actors/sachi crying.png"
image sachi cf = "Actors/sachi crying flipped.png"
image sachi love = "Actors/sachi love.png"
image yuki = "Actors/yuki.png"
image maiko = "Actors/maiko.png"
image elisven = "Actors/Elisven.png"
image elisven s = "Actors/Elisven scared.png"
image elisven a = "Actors/Elisven afraid.png"
image ikeshia = "Actors/Ikeshia.png"
image ikeshia m = "Actors/Ikeshia mad.png"
image ikeshia s = "Actors/Ikeshia surprised.png"



# Declare characters used by this game.
define x = Character('???', color="#b03510", show_two_window= True, ctc="ctc_tree",ctc_position="fixed")
define k = Character ('Yamakazi', color="#b03510", show_two_window= True, ctc="ctc_tree",ctc_position="fixed")
define s = Character ('Sachi', color="#b03510", show_two_window= True, ctc="ctc_tree",ctc_position="fixed")
define y = Character ('Yuki', color="#b03510", show_two_window= True, ctc="ctc_tree",ctc_position="fixed")
define k2 = Character ('Kai', color="b03510", show_two_window= True, ctc="ctc_tree",ctc_position="fixed")
define t = Character ('Teacher', color="b03510", show_two_window= True, ctc="ctc_tree",ctc_position="fixed")
define d = Character ('Doctor', color="b03510", show_two_window= True, ctc="ctc_tree",ctc_position="fixed")
define m = Character ('Maiko', color="b03510", show_two_window= True, ctc="ctc_tree",ctc_position="fixed")
define so = Character ('Soldier',color="b03510", show_two_window= True, ctc="ctc_tree",ctc_position="fixed")
define ma = Character ('Maid',color="b03510", show_two_window= True, ctc="ctc_tree",ctc_position="fixed")
define i = Character ('Princess Ikeshia',color="b03510", show_two_window= True, ctc="ctc_tree",ctc_position="fixed")
define narator = Character(kind=nvl)
################################# CG GALLERY    

# The game starts here.
label start:
    $ bl_game = False
    scene bg jail
    with fade
    play music "BGM/Reprieve.ogg"
    show kai at left
    $ renpy.music.set_volume(0.3, 0, channel="music")
    voice "Voice/Kai 1"
    x "\"{cps= 15}Hello, human. Are you ready for your execution? \"......{w=0.5}coughs{w=0.5}......
{w=1}\"I mean trial.{/cps}\""
    voice "Voice/Kai 2"
    x "\"{cps= 15}Although, the evidence speaks clearly enough.{/cps}\""
    
    show Yamakazi n at right
    k "\"{cps= 15}.......{/cps}\""
    stop music
    scene bg bedroom
    with dissolve
    "{cps= 15}One week ago.{/cps}"
    play music "BGM/Proximate Hearts.ogg"
    nvl clear
    
    narator "{size= 50}{cps= 15}My name is Yamakazi Kusanagi. I'm what you'd call your average, typical, boring high school student. 
             I'm 14 years old, and I enjoy the simple things in a normal teenager's life. Playing games, reading manga, and trying to keep my perverted fantasies of having my own personal harem in check. 
             Even though most of the time, I fail at that last one.{p}I'd also love to be a NEET and just shut myself in my room and indulge in those simple things in peace and quiet, but sadly... I can't. {/cps}{/size}"
    play sound "SFX/Alarm Clock.ogg"
    "{cps= 15}RING! RING! RING!{/cps}"
    stop sound
    voice "Voice/Sachi 1"
    x "\"{cps= 15}Kusanagi! Wake up!{/cps}\""
    menu:
        
        "Wake up.":
        
            jump Wakeup
        
        "Continue to sleep.":
            jump Sleep
    
    label Wakeup:
    scene bg bedroom
    
    show Yamakazi n at right
    show sachi at left
    
    nvl clear
    voice "Voice/Kusanagi 1"
    k "(yawns) \"{cps= 15}Morning.{/cps}\""
    narator "{size= 50}{cps= 15}And that's because of her. Kogara Sachi.{p}We've known each other forever. 
             We were even born in the same hospital room, just a day apart. She's a day older than me, and she loves to rub it in{p} 
We used to not be that close despite that weird coincidence with our birthdays, but now we're closer than ever before. 
             Nine years ago, I saved her from a pack of \"wolves\", that were actually just some stray dogs... {p}Actually, now that I think about it, 
             it's actually really funny that she thought those were wolves. Scratch that, she still insists that they were. {p}Anyway, since then, she now insists on 'helping' me however she can. 
             She wakes me up and makes sure I've packed my lunch and tries to help me study, whether I like it or not.  {p}
She's always talking about how she owes me for the brave thing I did.{/cps}{/size}"
    
    scene bg kitchen
    show Yamakazi n at right
    voice "Voice/Kusanagi 2"
    k "\"{cps= 15}Mmmm the breakfast is delicious today Sachi{/cps}\""
    voice "Voice/Sachi 2"
    s "\"{cps= 15}Thanks but let's hurry or we'll be late for school.{/cps}\""
    stop music
    scene bg school way
    pause 10
    scene bg classroom
    "{cps= 15}As soon as homeroom starts, I find myself too bored to pay attention.
      After several periods of class, lunch finally arrives. I stretch out, yawning,{/cps}" 
    extend "{cps= 15} but my peaceful awakening is interrupted by a punch to my head.{/cps}" with vpunch
    play music "BGM/casual.ogg"
    show sachi
    voice "Voice/Sachi 3"
    s "\"{cps= 15}You weren't paying attention in class, were you?{/cps}\""
    voice "Voice/Kusanagi 3"
    k "\"{cps= 15}I can't help it if school bores me.{/cps}\""
    voice "Voice/Sachi4"
    s "\"{cps= 15}Idiot!{/cps}" with vpunch
    voice "Voice/Sachi 4"
    extend "{cps= 15} You won't pass your midterms like this. ...Anyway, here's your lunch.{/cps}\""
    voice"Voice/Kusanagi 4"
    k "\"{cps= 15}Oh yeah, I'm starving.{/cps}\""
    voice"Voice/Sachi 5"
    s "\"{cps= 15} Jeez, how can you be starving? You just ate a little while ago{/cps}\""
    voice"Voice/Kusanagi 5"
    k "\"{cps= 15} It's these lessons! They sucked out all my energy{/cps}\""
    voice"Voice/Sachi 6"
    s "\"{cps= 15} Argh, I swear you're hopeless. We're gonna study hard tonight for 
       midterms, so be ready!{/cps}"
    hide sachi
    "{cps= 15}Classes finish and we set out for home.{/cps}"
    stop music
    label Holding:
        $ persistent.Holding = True
    scene bg street
    play music "BGM/Proximate Hearts.ogg"
    show sachi
    voice"Voice/Sachi 7"
    s "\"{cps= 15} Honestly Kusanagi you really should start paying attention in class.
       At least during homeroom.{/cps}\""
    voice"Voice/Kusanagi 6"
    k "\"{cps= 15} I told you-!{/cps}\""
    nvl clear
    stop music
    play music "BGM/The Ground Trembles.ogg"
    narator "{size= 50}{cps= 15} I suddenly feel the earth shaking under my feet. 
             It slowly gets more and more intense, until it feels like the whole world is shaking around me. {/cps}{/size}"
    extend "{size= 50}{cps= 15} I grab Sachi and hold her tightly in my arms. {w=5}And then a few seconds later, it stops. {/cps}{/size}" with Shake((0, 0, 0, 0), 5.0, dist=30)
    narator "{size= 50}{cps= 15}Earthquakes are pretty common here, so I would normally think nothing of it...{p}
But this is the first one in a while to be so intense and to last so long.{p}As I try to calm down and get a grip on what happened, 
             I notice a car going haywire, as if the driver had passed out cold.I hold Sachi tighter and jump to the side, and there's 
             a sudden sickening crack when my head{/cps}{/size}"
    extend "{size= 50}{cps= 15} slams into a wall in my haste.{/cps}{/size}" with vpunch
    show sachi c
extend "{size= 50}{cps= 15}...{p}When I slowly begin to wake up, the first thing I hear is Sachi calling me. As my eyes open, I can blurrily make out her outline, and I dimly realize that she's crying. 
        Damn it, I did it again... I made her cry again...{/cps}{/size}"
"{cps= 15}But she gets me to my feet, and helps me home.{/cps}"

$ renpy.end_replay()

stop music
play music "BGM/Nostalgia.ogg"
label Love_Scene:
    $ persistent.Love_Scene = True
scene bg bedroom
"{cps= 15} She tends to my wounds, and despite the fact that I blacked out, the damage doesn't seem to be too bad. Not bad enough to drag me to the hospital, anyway. 
 We sit down to a meal, just like any other day.{/cps}"
show sachi at left
voice"Voice/Sachi 8"
s "\"{cps= 15}U-um, Kusanagi... I have something I wanna t-tell you.{/cps}\""
"Sachi looks at me, blushing hard and trying her best to keep a stutter out of her voice."
voice"Voice/Sachi 9"
s "\"{cps= 15} It's about what happened today...{w=1} It reminded me... Of what
       you did when we were kids{/cps}\""
show Yamakazi n at right
voice"Voice/Kusanagi 7"
k "\"{cps= 15}Oh, don't worry about that. You know I'll always come to your rescue.{/cps}\""
"{cps= 15} Sachi blushes even more.{/cps}"
stop music
play music "BGM/Sunset.ogg"
voice"Voice/Sachi 10"
hide sachi
show sachi love
s "\"{cps= 15} Kusanagi, I-I-I... I love you. I've loved you ever since... 
   Ever since you saved me, back when we were kids.{/cps}\""
voice"Voice/Sachi 11"
s "\"{cps= 15} Ever since then all I wanted was to be with you. And until today...
       I thought just being by your side was enough. But back there, when you saved me... 
   And you were out cold like that, I thought... I thoght I would lose you. 
   And that I'd never get to tell you how I feel{/cps}\""
"{cps= 15} I can feel my heart hammering in my chest, faster and faster. 
 My throat's dry, and I swallow hard before I can respond.{/cps}"
voice"Voice/Kusanagi 8"
k "\"{cps= 15} I love you too, Sachi.{/cps}\""

hide Yamakazi n
hide sachi love

scene Love Ending
centered "{size= 150}Love Ending{/size}"

$ renpy.end_replay()

return
    
label Sleep:
    scene bg bedroom
    show sachi at left
    play music "BGM/Proximate Hearts.ogg"
    nvl clear
    voice"Voice/Sachi 12"
    s "\"{cps= 15}Hey lazyass, wake up!{/cps}\""
    voice"Voice/Kusanagi 9"
    k "\"{cps= 15}Ughhh. Five more minutes please...{/cps}\""
    voice"Voice/Sachi 13"
    s "\"{cps= 15}Come on sleepyhead, we're going to be late for school!{/cps}\""
    narator "{size= 50}{cps= 15}And that's because of her. Kogara Sachi.{p}We've known each other forever. 
             We were even born in the same hospital room, just a day apart. She's a day older than me, and she loves to rub it in{p} 
We used to not be that close despite that weird coincidence with our birthdays, but now we're closer than ever before. 
             Nine years ago, I saved her from a pack of \"wolves\", that were actually just some stray dogs... {p}Actually, now that I think about it, 
             it's actually really funny that she thought those were wolves. Scratch that, she still insists that they were. {p}Anyway, since then, she now insists on 'helping' me however she can. 
             She wakes me up and makes sure I've packed my lunch and tries to help me study, whether I like it or not.  {p}
She's always talking about how she owes me for the brave thing I did.{/cps}{/size}"
    voice"Voice/Kusanagi 10"
    k "\"Ok, ok, I'm up.\"  yawns  \"{cps= 15}What time is it?{/cps}\""
    voice"Voice/Sachi 14"
    s "\"{cps= 15}It's very late!{/cps}\""
    
    stop music
    scene bg kitchen
    play music "BGM/Nostalgia.ogg"
    show Yamakazi nf at left
    
    voice"Voice/Kusanagi 11"
    k "\"{cps= 15}Sachi, will you cut it out?{/cps}?\""
    show sachi f at right
    voice"Voice/Sachi 15"
    s "\"{cps= 15}Cut what out, Kusanagi?{/cps}\""
    voice"Voice/Kusanagi 12"
    k "\"{cps= 15}This. I appreciate all your help, but you need to stop now. It's been nine years. {/cps}\""
    voice"Voice/Kusanagi 13"
    k "\"{cps= 15}We're both in high school now and I don't need your help anymore.{/cps}\""
    voice"Voice/Kusanagi 14"
    k "\"{cps= 15}You've done more than enough for me, and it's starting to get annoying.{/cps}\""
    show sachi cf at right
    voice"Voice/Sachi16"
    s "\"{cps= 15}...{/cps}\""
    voice"Voice/Kusanagi 15"
    k "\"{cps= 15}Not to mention kinda frustrating. Plus, don't you have midterms to worry about? 
       You tutor me all the time but I doubt you've done any studying for yourself, right? So why not focus on that?{/cps}\""
    "{cps= 15}It's only then that I notice that while I was talking, Sachi's eyes welled up with tears. 
     They spill over onto her cheeks and she reels back her fist, and punches me square in the gut. Then she grabs my arm and throws me into the wall.{/cps}"
    show sachi af at right
    hide Yamakazi n with vpunch
    voice"Voice/Sachi 16"
    s "\"{cps= 15}IDIOT!{/cps}\""
    hide sachi a
    voice"Voice/Kusanagi 16"
    k "\"{cps= 15}Ow... Ugh. I know I was harsh, but did she really have to hit me so hard?
       \" sigh{w=2} \"Well, at least now I know she'll focus on her midterms.{/cps}\""
    voice"Voice/Kusanagi 17"
    k "\"{cps= 15}Oh shit, I'm actually gonna be late.{/cps}\""
    stop music
    scene bg school way
    with fade
    pause 10
    scene bg classroome
    voice"Voice/Kusanagi 18"
    k "\"{cps= 15}Made it, finally.{/cps}\""
    scene bg classroom
    voice"Voice/Kusanagi 19"
    k "\"{cps= 15}And just in time too.{/cps}\""
    "\"{cps= 15}...{/cps}\""
    "\"{cps= 15}After several periods of class, lunch finally arrives.{/cps}\""
    play music "BGM/casual.ogg"
    show yuki
    voice "Voice/Yuki1"
    y "\"{cps= 15}Ummm Yamakazi......{w=2}Is everything ok with Sachi?{w=1} She looked all depressed during class.{/cps}\""
    voice"Voice/Kusanagi 20"
    k "\"{cps= 15}We just had an argument this morning that's all. It's nothing to worry about.{/cps}\""
    voice "Voice/Yuki2"
    y "\"{cps= 15}Well OK, if you say so.{/cps}\""
    "{cps= 15}Yuki steps out of the classroom for a moment, and then returns hastily, looking disturbed{/cps}"
    scene bg classroomb with fade
    stop music
    show yuki at right
    play music "BGM/Emergency.ogg"
    voice "Voice/Yuki3"
    y "\"{cps= 15}Yamakazi!{/cps}\""
    voice"Voice/Kusanagi 21"
    k "\"{cps= 15}What? Why are you yelling?{/cps}\""
    voice "Voice/Yuki4"
    y "\"{cps= 15}Some kids said they saw Sachi heading up towards the roof!{/cps}\""
    voice"Voice/Kusanagi 22"
    k "\"{cps= 15}And?{/cps}\""
    voice "Voice/Yuki5"
    y "\"{cps= 15}The hole in the fence is still there.....Don't you think-?{/cps}\""
    voice"Voice/Kusanagi 23"
    k "\"{cps= 15}Don't be silly, Sachi's not that dumb.{/cps}\""
    voice"Voice/Yuki6"
    y "\"{cps= 15}But... she was so upset earlier...{/cps}\""
    stop music
    "{cps= 15}Sachi's face while leaving my house this morning comes to mind.{p}She wouldn't, would she?{p}
    I get up and decide to go check on her.{/cps}"
    play music "BGM/intense.ogg"
    scene bg stairs
    "{cps= 15}Turning the corridor I suddenly bump into someone.{/cps}"
    show Yamakazi nf at left
    pause 0.5
    voice"Voice/Kusanagi 24"
    show sachi f at right with fade
    k "\"{cps= 15}Who the- Oh, Sachi, I was looking for you.{/cps}\""
    play music "BGM/Proximate Hearts.ogg"
    voice"Voice/Sachi 17"
    s "\"{cps= 15}Kusanagi! I-I... I...{/cps}\""
    voice"Voice/Kusanagi 25"
    k "\"{cps= 15}Pfft! I knew you couldn't be that stupid.{/cps}\""
    hide sachi
    show sachi af at right
    voice"Voice/Sachi 18"
    s "\"{cps= 15}What?!{/cps}\""
    play sound "SFX/school bell.ogg"
    "{cps= 15}DING! DONG!{/cps}"
    voice"Voice/Kusanagi 26"
    k "\"{cps= 15}Oh, nothing never mind. Let's hurry back to the class.{/cps}\""
    stop music
    stop sound
    scene bg classroom
    
    "{cps= 15}Classes finish and we set out for home.{p} Sachi seems to be still upset about 
       this morning and took off before me for the first time in nine years.{/cps}"
    label Earthquake:
        $ persistent.Earthquake = True
    scene bg street with dissolve
    nvl clear
    play music "BGM/reflective.ogg"
    narator "{size= 50}{cps= 15}I watch her back as she hastily walks in front of me, and ponder 
             if it would be a good idea to try and talk to her.{/cps}{/size}"
    play music "Bgm/The Ground Trembles.ogg"
    extend "{size= 50}{cps= 15}Before I can come up with a plan of action, I suddenly feel the earth shaking under my feet. 
            It slowly gets more and more intense, until it feels like the whole world is shaking around me, and the vibrations knock me off my feet.{/cps}{/size}" with Shake((0, 0, 0, 0), 5.0, dist=30) 
    extend "{size= 50}{cps= 15}{w=5}And then a few seconds later, it stops. Earthquakes are pretty common here, so I would normally think nothing of it...
            But this is the first one in a while to be so intense and to last so long.{/cps}{/size}"
    extend "{size= 50}{cps= 15} As I try to get up, I notice a car going haywire, as if the driver had passed out cold. 
            I quickly struggle to my feet to get out of its way, but then I see Sachi still moving towards the car. I scream.{/cps}{/size}"
    voice"Voice/Kusanagi 27"
    k "\"{cps= 15}SACHI, YOU IDIOT! MOVE OUT OF THE WAY!{/cps}\""
    show sachi f at right
    "{cps= 15}As I yell those words I dash towards her.{/cps}"
    voice"Voice/Sachi 19"
    s "\"{cps= 15}Kusanagi? What are you doing?{/cps}\""
    play music "BGM/Demise.ogg"
    "{cps= 15}I blink, and Kusanagi gets hit by the car that was careening towards us. 
     His body flies backwards and slams into the wall of a nearby building. I start to shriek before I even realize it.{/cps}"
    show sachi cf
    voice"Voice/Sachi 20"
    s "\"{cps= 15}KUSANAGI! NO!{/cps}\""
    "{cps= 15}Kusanagi lay there, unconscious. I run up to try and shake him awake, but a voice stops me.{/cps}"
    voice"Voice/T 1"
    x "\"{cps= 15}Don't touch him! {/cps}\""
    show teacher at left
    voice"Voice/T 2"
    t "\"{cps= 15}If you move him now, we might as well bury him here. Go get help, I'll call an ambulance. Go!!{/cps}\""
    $ renpy.end_replay()
    stop music
    
    scene bg hospital en with dissolve
    pause 5
    scene bg hospital bed with blinds
    show sachi c at left
    
    play music "BGM/guilt.ogg"
    voice"Voice/Sachi 21"
    s "\"{cps= 15}It's all my fault....my fault...my fault.....{/cps}\""
    
    show doctor at right
    
    voice"Voice/Doctor 1"
    d "\"{cps= 15}Umm, miss....You should go rest. You do have your exams this week right?{/cps}\""
    voice"Voice/Sachi 22"
    s "\"{cps= 15}How is he? Please, tell me!{/cps}\""
    voice"Voice/Doctor 2"
    d "\"{cps= 15}His condition is stable for now, but we won't know anything until he comes out of the coma.{/cps}\""
    voice"Voice/Doctor 3"
    d "\"{cps= 15}I'm sorry miss, but I must insist you rest and return tomorrow.  It won't help him in any way if you stay here and worry about him.{/cps}\""
    voice"Voice/Sachi 23"
    s "\"{cps= 15}B-but...but...this....this...is all my fault!!!{/cps}\""
    stop music
    
    
    scene bg classroom
    "Five days ago"
    play music "BGM/casual.ogg"
    scene bg classroomb
    show maiko at left
    voice "Voice/Maiko1"
    m "\"{cps= 15}Have you heard? They say that someone found an old scroll that can fully heal a person. Even revive the dead.{/cps}\""
    show yuki
    voice "Voice/Yuki7"
    y "\"{cps= 15}Yes, but it's just a fairy tale. Something scammers make up to steal your money.{/cps}\""
    voice "Voice/Maiko2"
    m "\"{cps= 15}Oh no, they say this one is real ... They say that it even healed a person who'd been in a coma for 4 straight months.{/cps}\""
    show sachi cf at right
    play music "BGM/contemplation.ogg"
    voice"Voice/Sachi 24"
    s "\"{cps= 15}Where is this scroll?! How do I get it?!{/cps}\""
    voice "Voice/Yuki8"
    y "\"{cps= 15}Um... I think they said it's being held at the Tokyo Research Center for Unidentified Items. But they don't let anyone near it, not even reporters.{/cps}\""
    "{cps= 15}This sounds like a chance to help Kusanagi and thank him for saving me...again.{p} It
     seems all I'm doing is getting rescued by him all the time. But then again there is 
     no proof that this is real. Should I really risk it?{/cps}"
    menu:
        
        "Yes! I will do what ever it takes to help him.":
            jump Yes
        
        "No. It's just a hoax anyway most likely":
            jump No
    
    label No:
    
    scene bg classroomb
    "{cps= 15}Modern medicine has come a long way. I'm sure he'll be fine\n{/cps}"
    play sound "SFX/school bell.ogg"
    extend "{cps= 15}DING! DONG!{/cps}"
    "{cps= 15}Classes finish and I head off to the hospital.{/cps}"
    stop music
    stop sound
    scene bg classroome
    pause 3
    scene bg stairs
    pause 3
    scene bg school way
    scene bg hospital en
    pause 5
    label Regret:
         $ persistent.Regret = True
    scene bg hospital bed
    show doctor at left
    pause 5
    show sachi f at right
    voice"Voice/Sachi 25"
    s "\"{cps= 15}Hello doctor. How is he doing?{/cps}\""
    play music "BGM/heartwarming.ogg"
    voice"Voice/Doctor 4"
    d "\"{cps= 15}He's starting to come back, slowly.{/cps}\""
    voice"Voice/Sachi 26"
    s "\"{cps= 15}Thank you, doctor.{/cps}\""
    voice"Voice/Doctor 5"
    d "\"{cps= 15}No worries. Now, if you'll excuse me...{/cps}\""
    hide doctor
    "{cps= 15} The doctor leaves the room, and I sit next to Kusanagi's bed happily and watch his sleeping face.{/cps}"
    voice"Voice/Sachi 27"
    s "\"{cps= 15} I knew I didn't need that hoax to give me false hopes.\n
       After you wake up... I'm going to tell you how I feel. How I've always felt about you since that day...{/cps}\""
    play music "BGM/The Ground Trembles.ogg"
    "{cps= 15}Suddenly, the room starts to shake intensely. 
     I can hear screams go up in adjacent rooms, and rocks begin to crumble down from the roof above.{p}{/cps}"with Shake((0, 0, 0, 0), 5.0, dist=30)
    voice"Voice/Sachi 28"
    s "\"{cps= 15}An earthquake?! Again?!{/cps}\""
    "{cps= 15}I dive over Kusanagi, trying to shield him with my body.{/cps}"
    "{cps= 15}...{/cps}"
    stop music
    hide sachi
    nvl clear
    play music "BGM/Ending Untold.ogg"
    "{cps= 15}After the earthquake settles, the doctor and nurses come to check on you, only to find the both of you dead under the rubble. 
             They try to resuscitate you, but it's in vain. It seems Sachi died trying to protect her beloved Kusanagi.{/cps}"
    centered "{size= 150}ROMEO AND JULIET ENDING{/size}"
    $ renpy.end_replay()
    
    return
    
    label Yes:
    play music "BGM/intense.ogg"
    scene bg classroomb
    "{cps= 15}Not listening, I take off like a shot{/cps}"
    scene bg classroome
    pause 3
    scene bg stairs
    pause 3
    scene bg school way
    voice"Voice/Sachi 29"
    s "\"{cps= 15}Kusanagi, wait for me. I'm going to get that scroll no matter what the cost may be. I swear, I'll save you!{/cps}\""
    play music "BGM/The Ground Trembles.ogg"
    voice"Voice/Sachi 30"
    s "\"{cps= 15}What?! What’s going on?{/cps}\"" with Shake((0, 0, 0, 0), 5.0, dist=30)
    "{cps= 15}Three minutes later{/cps}"
    voice"Voice/Sachi 31"
    s "\"{cps= 15}What on earth just happened?{/cps}\""
    "{cps= 15}Another strong earthquake rocked the pavement beneath my feet, and then stopped suddenly, just like the last one.{/cps}"
    voice"Voice/Sachi 32"
    s "\"{cps= 15}This is insane. Two big earthquakes in such a short period.
       No, this was longer and seemed stronger then the previous one.{/cps}\""
    voice"Voice/Sachi 33"
    s "\"{cps= 15}Oh god... Kusanagi, please be okay. I'll be there soon!{/cps}\""
    stop music
    scene bg magici
    voice"Voice/Sachi 34"
    s "\"{cps= 15}Wow, this place is deserted. No staff members... A few soldiers, but I guess that makes sense after that earthquake.{/cps}.\""
    scene bg magici ins
    play music "BGM/Imminent Danger 2.ogg"
    "{cps= 15}I search desperately for the scroll.{/cps}"
    "{cps= 15}I don't even notice the armed soldier approaching me from behind.{/cps}"
    voice"Voice/So 1"
    so "\"{cps= 15}HEY! What do you think you're doing here?! 
        This is a restricted area! Who are you?!{/cps}\""
    
    menu:
        "Lie about who you are.":
            jump Lie
        "Tell the truth about who and why are you here.":
            jump Truth
    label Truth:
        label Arrested:
            $ persistent.Arrested = True
    play music "BGM/guilt.ogg"
    scene bg magici ins
    show sachi
    voice"Voice/Sachi 35"
    s "\"{cps= 15}M-My name is Kogara Sachi.
I am a student at the Fujiyama Academy! And
I'm looking for the scroll to help my friend!{/cps}\""
    "{cps= 15}He slowly lowers his gun.{/cps}"
    voice"Voice/Sachi 36"
    s "\"{cps= 15}...nearly got killed by my own stupidity.{/cps}\""
    voice"Voice/So 2"
    so "\"{cps= 15}Don't make me laugh kid. There's no magical scroll 
        here, now get lost before I shoot you{/cps}\""
    voice"Voice/Sachi 37"
    s "\"{cps= 15}I know it's here. Everyone in the town knows it's here.{/cps}\""
    voice"Voice/So 3"
    so "\"{cps= 15}Pfft. It's just a publicity stunt. To get people to come here and to attract funding...{/cps}\""
    voice"Voice/Sachi 38"
    s "\"{cps= 15}Oh yeah? Then if that's true, what are you doing here? 
       If you're not guarding anything, then it doesn't matter if I'm here. So leave me alone!{/cps}\""
    "{cps= 15}I start to laugh and go back to my search. Laywer'd.{/cps}"
    voice"Voice/So 4"
    so "\"{cps= 15}Listen kid, you're never gonna find it. You know why? {/cps}"with vpunch
    extend "{cps= 15} Because you're under arrest!{/cps}\""
    hide sachi
    nvl clear
    play music "BGM/Ending Untold.ogg"
    narator "{size= 50}{cps= 15}The soldier suddenly pushes me to the ground with his rifle and tries to cuff me. 
             I try to resist by grabbing a chunk of glass and go for his throat. 
             He sees me, though, and shoots me point blank in the arm, forcing me to drop the glass and immobilizing me with the sudden, sharp pain.
             He cuffs me, and takes me to the police station.After several hours of questioning, he releases me, and I head straight to the hospital to check up on Kusanagi. 
             But his room is empty.I find out that you passed away during the second earthquake.{/cps}{/size}"
    centered "{size= 150}UNTOLD LOVE ENDING{/size}"
    $ renpy.end_replay()
    return
    
    label Lie:
    scene bg magici ins
    show sachi
    
    play music "BGM/Gunpoint2.ogg"
    voice"Voice/Sachi 39"
    s "\"{cps= 15}Uh- um... I'm... looking for a book that my mom needed.{/cps}\""
    voice"Voice/So 5"
    so "\"{cps= 15}What's your mother's name?!{/cps}\""
    voice"Voice/Sachi 40"
    s "\"{cps= 15}Doctor Takagi Narumi.{/cps}\""
    "{cps= 15}The solider begins to talk into his earpiece.{/cps}"
    voice"Voice/So 6"
    so "\"{cps= 15}Captain, can you run a check on a Dr. Takagi Narumi- see if she works here- and a... 
        What's your name, girl?!{/cps}\""
    "{cps= 15}I look up at the soldier, and it vaguely registers in the back of my mind that I 
     only have a matter of seconds before he figures out my lie and has me arrested.{/cps}" 
    voice"Voice/Sachi 41"
    s "\"{cps= 15}Yukari.{/cps}\""
    "{cps= 15}Looking around I see chunks of glass scattered all around the floor from the earthquake. 
     I take a large one in my hand.{/cps}" 
    voice"Voice/So 7"
    so "\"{cps= 15}And a 'Takagi Yukari', captain...\n Sorry about this, but it's just standard procedure. I don't personally know anyone by that name, so...{/cps}\""
    label Yandere:
        $ persistent.Yandere = True
    scene bg magici ins
    play music "BGM/Through.ogg"
    "{cps= 15}The soldier's expression suddenly changes. That must mean he's being informed of my lie. That's my cue. I dash towards him and swing my arm around, slashing his throat with the shard of glass. 
     The soldier manages to fire one bullet, and it sinks into my right arm. I stab the glass shard into his throat and push him away, holding my injured arm. He crumples to the ground.{/cps}."
    "{cps= 15}The pain radiating up my arm is unbearable, but I still turn back to my search, desperate to find the scroll. There's no way no one heard that gunshot- someone's going to come looking soon to see what happened.{/cps}"
    voice"Voice/Sachi 42"
    s "\"{cps= 15}Agh, where is it? Maybe... Maybe it was fake after all?{/cps}\""
    scene Sachi shot
    "{cps= 15}The pain and the bleeding become too much to bear. I lean against a wall to take a short break.I also pull out my handkerchief, and try and use it to stop the bleeding{p}
     Then, I notice something. An old scroll, rolled out as if someone had been studying it. But no one is around.I grab the fire extinguisher mounted on the wall beside me and smash in the glass door that separates me from the scroll, 
     and then go inside the room to see if I can read the scroll.{/cps}"
    $ renpy.end_replay()
    voice"Voice/Sachi 43"
    s"\"{cps= 15}I can't make heads or tails of this. Ugh... But... This is probably it, isn't it? No, it HAS to be it!.{/cps}\""
    scene bg magici
    show sachi c
    "{cps= 15}I grab the scroll and then rush towards the exit, gasping as every moment sends pain shooting through my entire body.I stumble out of the building and trip, falling on my wounded arm.{/cps}"with hpunch
    voice"Voice/Sachi41"
    s "\"{cps= 15}ARGH!!!{/cps}\""
    "{cps= 15}Suddenly a car stops, almost right in front of me.{/cps}"
    voice"Voice/T 3"
    x "\"{cps= 15}Sachi, are you okay?! What happened?{/cps}\""
    "{cps= 15}It's my biology teacher. I look up at him, and then pass out.{/cps}"
    show teacher
    stop music
    scene bg hospital bed
    "{cps= 15}I wake up with a strangled gasp, sitting upright. Pain shoots through me from the sudden movement. I breathe in deeply to try and quell it, and then look around.
     I'm in a hospital room. My arm has been disinfected and bandaged.{/cps}"
    show sachi c
    play music "BGM/reflective.ogg"
    voice"Voice/Sachi 44"
    s "\"{cps= 15}KUSANAGI!{/cps}\""
    "{cps= 15}I leap out of bed, wincing at the aggravation of my arm, but doggedly look for my clothes and the scroll. I get dressed, tuck the scroll under my arm, and then sprint out of the room in search of his.{/cps}"
    hide sachi c
    scene bg hospital en
    extend "{cps= 15}I can't help but notice some rubble on the floor as I careen past.
            Must be from that earthquake earlier.{/cps}"
    "{cps= 15}I can't help picturing worst case scenarios in my head. Rubble crushing Kusanagi in his sleep. Soldiers coming after him in search of the scroll. I try to concentrate and stay calm. I try to tell myself that everything is going to be just fine.{/cps}"
    scene bg hospital bed
    extend "{cps= 15}Finally I reach Kusanagi's room and see two nurses trying to move him on a table.{/cps}"
    voice"Voice/Sachi 45"
    s "\"{cps= 15}Wait! What are you doing? Leave him alone!{/cps}\""
    show sachi a at left
    "{cps= 15}I dash inside, pushing the nurses away. I can feel anger burning in my eyes as I pant, breaths ragged and strained. Just then, the doctor walks in.{/cps}"
    show doctor f at right
    voice"Voice/Doctor 6"
    d "\"{cps= 15}Ah Miss, I'm glad to see you're okay now. You were bleeding pretty badly when your teacher brought you here.{/cps}\""
    voice"Voice/Sachi 46"
    s "\"{cps= 15}I'm just fine. But what're they doing to Kusanagi?!{/cps}\""
    stop music
    "{cps= 15}The doctor glances at the floor, and the room falls silent. I feel a cold sweat break out on my neck.{/cps}" 
    play music "BGM/Demise.ogg"
    voice"Voice/Doctor 7"
    d "\"{cps= 15}Miss... I'm sorry to have to tell you this, but your friend... He passed away during the earthquake.{/cps}\""
    hide sachi a
    show sachi c at left
    "{cps= 15}I feel petrified, unable to move from the shock. 
It feels like time stops. Until the world slowly goes up in flames, and then comes crashing down around me.{/cps}"
    voice"Voice/Sachi 47"
    s "\"{cps= 15}No! It can't be!{/cps}\""
    "{cps= 15}I rush over to Kusanagi and put my ear to his chest, searching for a tiny glimmer of hope in the form of the faintest heartbeat...
     But there's nothing to be heard. A waterfall of tears come to my eyes within seconds.{/cps}"
    voice"Voice/Doctor 8"
    d "\"{cps= 15}I'm sorry miss. We did everything we could.{/cps}\""
    stop music
    play music "BGM/Ending Forgotten.ogg"
    voice"Voice/Sachi 48"
    s "\"{cps= 15}Can... can I have... a few minutes alone with him? Please?{/cps}\""
    "{cps= 15}The tears won't stop, and my throat constricts, making it hard to say that simple request.{/cps}"
    voice"Voice/Doctor 9"
    d "\"{cps= 15}Yes of course.{/cps}\""
    hide doctor
    "{cps= 15}The doctor makes a gesture to the nurses, and they leave me alone with Kusanagi.MMy fists suddenly slam down on the edge of Kusanagi's bed. 
     My quiet tears turn into wailing as I lay my head on his chest.{/cps}"
    label Tarnished_Hope:
        $ persistent.Tarnished_Hope = True
    scene bg hospital bed
    voice"Voice/Sachi 49"
    s "\"{cps= 15}Damn it! Was all this effort for nothing?!{/cps}\"" 
    "{cps= 15}I look at the scroll.{/cps}"
      
    #show magic
    voice"Voice/Sachi 50"
    s "\"{cps= 15}Even if this is real... It can't save him now.{/cps}"
    "{cps= 15}I cry into his chest, soaking his hospital gown through with tears. I cry until I feel like I can't cry anymore, my throat run raw with grief-stricken sobs.{/cps}"
    voice"Voice/Sachi 51"
    s "\"{cps= 15}No... I still have to try.{/cps}\""
    "{cps= 15}I slowly get up, and wipe my face of tears.{/cps}"
    voice"Voice/Sachi 52"
    s "\"{cps= 15}This is my fault! My stupidity got him killed.{/cps}\""
    hide sachi c
    "{cps= 15}I open the scroll, and stare amazed at the runes. I can't understand them at all, but I take a long breath... And then, a miracle happens. The spell jumps to my lips, as if I knew it all along.{p}{/cps}"
    stop music
    nvl clear
    show scroll
    play music "BGM/Rift.ogg"
    voice"Voice/Sachi 53"
    narator "{size= 50}{cps= 15}Om mashiri nei sokawa,\n Anrionta soku, mestsu suko,biriraya  birira suko mestsu,\n
 Ban, kikuru takura ku, \n Anz kikurishu chibikiri nadano, yuu sabara 
shotari dayvaj, \n Shinkashi yan yan yo-on zestsu!{/cps}{/size}"
    hide scroll

    show magic
    init:
        image magic = "magic.png"

        $ flash = Fade(.75, 3, .75, color="#fff")
    
    extend "{cps= 15}{size= 50} \n Suddenly around Kusanagi's bed, a circle of light appears
My jaw drops open, the light making the tear trails on my cheeks shimmer. This is it. The scroll is the real deal! And Kusanagi is...being levitated above the bed.
             A smile slowly spreads across my face.  I reach out to touch{/size}{/cps}"
extend "{cps= 15}{size= 50}Kusanagi, but then the light becomes bright enough to blind me in a sudden flash.{/size}{/cps}" with flash
hide magic
narator "{cps= 15}{size= 50}The doctor and nurses reenter the room, and with simultaneous shocked gasps, they rush in and pull me away from the beam of light.{/size}{/cps}"

voice"Voice/Doctor 10"
d "\"{cps= 15}What on earth is going on here!!!{/cps}\""
"{cps= 15}The beam of light vanishes, and Kusanagi's body is gone. The doctor looks down at my face, the bright smile gone, replaced by shock and disbelief.{/cps}"
$ renpy.end_replay()
stop music

label Alfheim:
    $ persistent.Alfheim = True
scene bg throneroom
play music "BGM/mysterious.ogg"
voice"Voice/Line1"
x "\"{cps= 15}Hello? Can you hear me?{/cps}\""
show yamakazi h at right
voice"Voice/Kusanagi 28"
k "\"{cps= 15}Huh? Where am I? What happened?{/cps}\""
show ikeshia at left
voice"Voice/Line2"
x "\"{cps= 15}I suppose it worked father. Listen boy, you don't have long to live.{/cps}\""
voice"Voice/Kusanagi 29"
k "\"{cps= 15}Huh?! What....what are you talking about? Am I going to die? But... I feel fine...{/cps}\""
voice"Voice/Line3"
x "\"{cps= 15}Well, to be honest, you were already dead to begin with. We just brought you back to life for the moment to ask some questions.{/cps}\""
voice"Voice/Kusanagi 30"
k "\"{cps= 15}I was already dead... WAIT, WHAT!? How can I be alive now if I was already dead? And who are you, anyway!?{/cps}\""
voice"Voice/Line4"
i "\"{cps= 15}I am Princess Ikeshia, and I have resurrected you through my magic power to ask you some questions. It's only a temporary resurrection and time is running out.{/cps}\""
voice"Voice/Kusanagi 31"
k "\"{cps= 15}Princess? Magic? Resurrection? This is all a bad joke, isn't it? Those things don't really exist.{/cps}\""
"I start looking around, and then down at myself. Then I pinch myself- hard- to make sure I'm not dreaming. But nothing happens."
hide ikeshia
show ikeshia m
voice"Voice/Line5"
i "\"{cps= 15}Don't exist?{/cps}\""
"Her expression changes from calm to very, very angry."
voice"Voice/Line6"
i "\"{cps= 15}Airdan show this dog here the proof that he needs.{/cps}\""
"{cps= 15}I look at the princess' face. A scary smile has stretched across her lips. I open my mouth to say something, but before I can, I feel a sudden, piercing pain in my back.
The pain gets more and more intense, almost as if its working its way through my core- and then I see it. {/cps}"
stop music
play music"BGM/Through.ogg"
scene Kusanagi stabbed
play sound "SFX/Slash.ogg"
extend "{cps= 15}The blade of a sword, sticking out of my chest.{/cps}"
"{cps= 15}Blood starts to spray everywhere. I scream in pain, and as the blade is pulled out, I fall to the ground. Blood begins to pool under me on the floor.{/cps}"
voice"Voice/Line7"
i "\"{cps= 15}Oh, stop being so dramatic. This is indeed a fatal wound, and if it wouldn't be for my magic that resurrected you, you would have been dead... But you’re not, are you? 
   Because one that has been temporary resurrected can’t die until the time limit ends.{/cps}\""
"She's right. I can feel the pain and feel the blood flowing out of my body... But I'm still alive."
voice"Voice/Line8"
i "\"{cps= 15}Now before the time runs out tell me, who are you? Where did you come from?{/cps}\""
voice"Voice/Kusanagi 32"
k "\"{cps= 15}Can you... stop my... bleeding, first?{/cps}\""
voice"Voice/Line9"
i "\"{cps= 15}Fine. Taruka metsu sowaka!{/cps}\""
show magic
init:
    image magic = "magic.png"

    $ flash2 = Fade(.75, 1, .75, color="#fff")
hide magic
"There's a blindingly bright flash of light when her chant ends, and all the pain suddenly dissipates from my body."
$ renpy.end_replay()

scene bg throneroom
show yamakazi h at right
show ikeshia m at left
stop music
play music "BGM/mysterious.ogg"
extend "Looking down, I see that my shirt is still torn and stained with blood, but the wound is gone. Amazed, I look back up at her, and her expectant face." with flash2
voice"Voice/Kusanagi 33"
k "\"{cps= 15}I'm Yamazaki Kusanagi. I'm 14 years old... And a high school student at Fujiyama Academy. I live in the Shinjuku district...{/cps}\""
hide ikeshia m
show ikeshia s at left
voice"Voice/Line10"
i "\"{cps= 15}Shinjuku? Where is that?{/cps}\""
"I look at her, stunned. Maybe she's a foreigner?"
voice"Voice/Kusanagi 34"
k "\"{cps= 15}Tokyo?{/cps}\""
"Now I'm just confused. Where in the world could she be from and have never heard of Tokyo?
Suddenly, I feel dizzy. And a few seconds later, I fall to the floor, unconscious."
stop music
hide yamakazi h
hide ikeshia s
scene bg palace bed
play music "BGM/flashback.ogg"
"{cps= 15}I wake up a few hours later. I found myself lying on a luxurious bed, in a bedroom that looked like it belonged to royalty. As I glance around the room, I suddenly notice the feeling of a hand on my forehead, running down the side of my face. 
         I instinctively move my head away, and turn to see a lovely maid who looked just as shocked and scared as I felt.{/cps}"
show yamakazi h at right
voice"Voice/Kusanagi 35"
k "\"{cps= 15}I'm sorry, I didn't mean to scare you like that. Please excuse me.{/cps}\""
"She nods, and  then leaves the room without saying a word."
voice"Voice/Kusanagi 36"
k "\"{cps= 15}Was I rude to her? Was that all... a dream? I couldn't have really been dead, right?{/cps}\""
"All of these questions piled up in my head as I tried to make sense of all the craziness that had occurred. I still had no idea why I was involved... or how I got dragged into this whole mess in the first place."
voice"Voice/Kusanagi 37"
k "\"{cps= 15}Ugh. It’s no use, I can’t make any sense of this! Magic can't possibly exist... but if that's true, then where am I? Last thing I remember was... pushing Sachi out of the way of that car...{/cps}\""
"There's a loud knocking sound. It seems someone's at the door."
voice"Voice/Kusanagi 38"
k "\"{cps= 15}Come in.{/cps}\""
stop music
"The door opens, and the girl from before comes inside. As I look at her closely, my confusion only gets worse. She has big, long elf ears, just like those elf girls you see in fantasy anime. She's cute, though. Graceful, elegant... 
 Plus she has a great rack."
play music "BGM/charactertheme1.ogg"
$ renpy.music.set_volume(0.5, .5, channel="music")
show ikeshia at left
voice"Voice/Line11"
i "\"{cps= 15}Hello again. I'm sorry for the rough treatment earlier, but considering how you just appeared and the situation we’re in, it had to be done like that.{/cps}\""
voice"Voice/Kusanagi 39"
k "\"{cps= 15}Appeared? Situation?{/cps}\""
voice"Voice/Line12"
i "\"{cps= 15}Oh yes, right. You were dead when you appeared on top of me{/cps}\""
"I'm sure I look more confused than ever, but she just keeps explaining how I got here."
voice"Voice/Line13"
i "\"{cps= 15}I do not know who, what, or where you came from. I do not know why you are here either. But what I do know is that last night while I was sleeping, you simply appeared out of nowhere, falling on me with your hands on my breasts. Hm. I guess wherever you came from, even after you die, a pervert remains a pervert.{/cps}\""
"I look at my hands, and then her chest. I can't help but smile. Her expression suddenly turns flustered."
voice"Voice/Line14"
i "\"{cps= 15}Pay attention you pervert! I'm only going to say this once!{/cps}\""
"Her face goes from flustered, to angry, and then suddenly back to normal as she regains her composure."
voice"Voice/Line15"
i "\"{cps= 15}My cousin and head of the guards- that you already met- along with a few of the guards... Dragged you to a cell until this morning.{/cps}\""
"I suddenly feel the memory of a pain in my back when she mentions him."
voice"Voice/Line16"
i "\"{cps= 15}It was him that first noticed that you were dead. It was I that suggested you be brought back to life. Unfortunately, father's head councilor was totally against it, under the pretext that the dead should remain dead. Eventually, due to how little we knew about you... I resurrected you for that short time period just in case you posed a threat to us.{/cps}\""
voice"Voice/Kusanagi 40"
k "\"{cps= 15}So that means... I died again after it went black, right?{/cps}\""
voice"Voice/Line17"
i "\"{cps= 15}Correct! And it was decided shortly after your death that your body would be burned and fed to the dragons. Or vice-versa... depending how the dragons liked your meat.{/cps}\""
"My jaw drops in shock."
voice"Voice/Kusanagi 41"
k "\"{cps= 15}But I'm alive again?{/cps}\""
voice"Voice/Line18"
i "\"{cps= 15}Yes. In the council meeting this afternoon my father went against their decision, and suggested you be resurrected yet again with a longer time frame to find out who, or what you really are, and where you actually came from. And thus you have been resurrected with a time frame of one week.{/cps}\""
"Her expression changes slightly as she finishes talking. A wave of doubt washes through me."
voice"Voice/Line19"
i "\"{cps= 15}So let’s begin by re-introducing ourselves with no rush this time. I am Princess Ikeshia Alvaerele, Princess of Alfheim.{/cps}\""
voice"Voice/Kusanagi 42"
k "\"{cps= 15}Alfheim? Wait... are you a real elf? Are those ears real?{/cps}\""
"Amazed, I reach out and start pinching her ears, yanking and petting them to feel if they were, indeed, real. Her expression goes from mild annoyance to flat out fury, and she punches me square in the face."
voice"Voice/Line20"
i "\"{cps= 15}Of course we're real! I just said I'm princess of Alfheim, where every elf lives. You seem to know about us and our home, yet we don’t know anything about you or yours... So please, do tell.{/cps}\""
voice"Voice/Kusanagi 43"
stop music
play music "BGM/warm.ogg"
k "\"{cps= 15}Well, your highness... I'm in no way royalty such as yourself. I'm just a highschool student, from, uh, Midgard? That's what you'd call the human world, right?{/cps}\"" 
voice"Voice/Kusanagi 44"
k "\"{cps= 15}Anyway, the reason I know about you and your land is that, in my world, there are lots of legends, stories, animes, movies, and games about elves. I'm not really sure how, but there are legends that say elves lived in our world long ago. Others say that elves and Alfheim are only fiction that someone created, but... here you are in front of me{/cps}\""
"Princess Ikeshia looks stunned as I continue to explain what I know."
voice"Voice/Kusanagi 45"
k "\"{cps= 15}Oh... Please excuse my manners, your highness. My name is Ymazaki Kusanagi from the country Japan. I live in the Shinjuku district of Tokyo City.{/cps}\""
voice"Voice/Line21"
i "\"{cps= 15}My, my! What a nice change in attitude. But to be honest... there is a legend here. That two thousand years ago, a group of elves on a sacred journey disappeared from Alfheim... and it’s believed they may have ended up in a different world.{/cps}\""
"My expression becomes puzzled."
voice"Voice/Kusanagi 46"
k "\"{cps= 15}Hm... Two thousand years ago? That's almost since our recorded history began. What is this sacred journey that they were on, anyway?{/cps}\""
voice"Voice/Line22"
i "\"{cps= 15}No one knows....we don’t even know if this story is true or not. Though from what you’re telling me, it may as well be true. Are there anymore elves that live there now?{/cps}\""
voice"Voice/Kusanagi 47"
k "\"{cps= 15}No your highness. As I said, they're believed not to exist at all.{/cps}\""
"She'd had this cute, hopeful smile on her face, but it was dashed by my answer. Now she just looked sad."
voice"Voice/Line23"
i "\"{cps= 15}Oh... I see... We’ll end here for now. Get some rest now, we’ll talk more tomorrow.{/cps}\""
"As I watch her expression and body language, it's clear the news hit a nerve. Maybe I shouldn't have told her that."
voice"Voice/Kusanagi 48"
k "\"{cps= 15}Wait your highness is- Are you alright? I'm very sorry if... I said something wrong?{/cps}\""
voice"Voice/Line24"
i "\"{cps= 15}No, I'm alright. Don't worry{/cps}\""
voice"Voice/Kusanagi 49"
k "\"{cps= 15}You know back where I come from, royalty aren't supposed to be this easy to catch in a lie. It's customary for them to appear totally honest.{/cps}\""
voice"Voice/Line25"
i "\"{cps= 15}Well that’s a good custom. And very true! I've never told a lie in my entire life.{/cps}\""
voice"Voice/Kusanagi 50"
k "\"{cps= 15}Very well, your highness... But when you’re ready, you can come talk about it. It’s not a good thing to hold it in, y'know?{/cps}\""
"After hearing that, she puts on a smile, as if to say that she's really okay, and then leaves the room."
stop music
play music "BGM/flashback.ogg"
"I start thinking about why I said everything I did. And if, maybe, she thinks that the elves were killed by humans? There's no record of that... 
 But then again, there's no record of elves anywhere in our history. Though, taking to account our track record with how we dealt with rumors about witches and vampires, it might actually be true."
"And then, I start to think about how I got here. I think about Sachi... What happened to her? Is she okay? Was she hurt in the accident? And then... I fall asleep."
stop music
play music "BGM/sleep.ogg"
hide yamakazi h
hide ikeshia
"Four days ago."
show elisven
voice"Voice/Elisven01"
x "\"{cps= 15}Sir, breakfast is ready. Please wake up.{/cps}\""
voice"Voice/Kusanagi 51"
k "\"{cps= 15}Ugh... Sachi, I thought I told you to stop doing this. I can get ready for school on my own.{/cps}\""
voice"Voice/Elisven02"
x "\"{cps= 15}Sachi? Sir, it’s time to stop dreaming of girls and wake up.{/cps}\""
voice"Voice/Kusanagi 52"
k "\"{cps= 15}Stop being so jealous, Sachi. Five more minutes...{/cps}\""
"A couple of minutes later, I hear footsteps walking away from my bed. And then... Ice cold water, dumped all over my head and face. I shoot upright in bed, and angrily look around to try and find the person responsible."
stop music
play music "BGM/sliceoflife.ogg"
voice"Voice/Kusanagi 53"
k "\"{cps= 15}Hey, what the hell do you think you’re doing!? Are you trying to kill me!?{/cps}\""
"I realize that I'm shouting at the maid from yesterday. She looks back at me, timidly."
hide elisven
show elisven a
voice"Voice/Elisven03"
ma "\"{cps= 15}I-I-I'm deeply sorry, sir... But you weren't getting up... And it seemed like you were having a perverted dream about a girl named Sachi? U-Unless it was a guy, but... but I mean, it's okay if it's like that, sir. Don't worry, I-I won't tell a soul!{/cps}\""
hide elisven a
show elisven
"She's smiling at me sheepishly."
voice"Voice/Elisven04"
ma "\"{cps= 15}Also, look on the bright side! Now you won't need to wash your face. Though, you should hurry and get dressed...{/cps}\""
"She giggles as she puts the tray and empty glass of water on the counter behind her."
hide elisven
show elisven at right with fade
show yamakazi hf at left
voice"Voice/Kusanagi 54"
k "\"{cps= 15}Oh, yes. I wouldn't want to catch a cold... especially here where there's no medicine for me.{/cps}\""
hide elisven a
show elisven s
voice"Voice/Elisven05"
ma "\"{cps= 15}Catch a cold, sir? Is it custom in Midgard to 'catch a cold'?{/cps}\""
voice"Voice/Kusanagi 55"
k "\"{cps= 15}Well I wouldn't say it’s a custom... But it does happen very often.{/cps}\""
voice"Voice/Elisven06"
ma "\"{cps= 15}Then... can you catch a heat?{/cps}\""
"I can't help but look surprised. Why should I be, though? Of course they don't know what a cold is."
voice"Voice/Kusanagi 56"
k "\"{cps= 15}No, actually, a cold is-{/cps}\""
voice"Voice/Elisven07"
ma "\"{cps= 15}Um... I'm deeply sorry to interrupt you sir, but the princess is waiting for you to have breakfast in the dining room with her.{/cps}\""
hide elisven s
show elisven
voice"Voice/Kusanagi 57"
k "\"{cps= 15}Oh... I see now... So that’s what you meant when you said I had to hurry and change...{/cps}\""
"I get out of bed and start searching for a bathroom to change in, while she starts peeling the wet bed sheets off the bed."
voice"Voice/Kusanagi 58"
k "\"{cps= 15}Uhhh... Where's the bathroom?{/cps}\""
voice"Voice/Elisven08"
ma "\"{cps= 15}Your own personal bathroom is behind that door, sir. If I may, do you still need to wash? If so I would be happy to help you, sir. I have been assigned to be your personal maid, after all!{/cps}\""
"My face flushes red. My mind starts racing, imaging her completely naked, washing me and pressing her chest against my back..."
voice"Voice/Kusanagi 59"
k "\"{cps= 15}Uh, um... No, I just want to get changed.{/cps}\""
voice"Voice/Elisven09"
ma "\"{cps= 15}Yes, sure, right away sir! ...Sir? Are you alright? Your face is all red, and- oh! You're bleeding!{/cps}\""
"I quickly cover my nose and turn around, wiping the blood from my nose."
voice"Voice/Kusanagi 60"
k "\"{cps= 15}I-I'm alright, don’t worry about me!{/cps}\""
"Suddenly I feel something pushing against my back. Two soft hands, moving around my torso to unbutton my shirt. I jump away without realizing, and accidentally elbow her in the face. She stumbles into the edge of the bed."
voice"Voice/Kusanagi 61"
k "\"{cps= 15}W-w-what are you doing?!{/cps}\""
hide elisven
show elisven a
voice"Voice/Elisven10"
ma "\"{cps= 15}I'm sorry, sir! I-I didn't mean to be rude! I only tried to help you change, sir... Should I have come from the front?{/cps}\""
"She looks sad, almost on the verge of tears, and then I notice a bruise forming on her right cheek."
voice"Voice/Kusanagi 62"
k "\"{cps= 15}N-no, don’t worry, you did nothing wrong. I’m sorry, I didn’t meant to hit you. I can get dressed by myself, so, uh, can you please wait for me outside? I don’t really know where the dining room is and, uh, I'd be happy if you'd show me the way.{/cps}\""
voice"Voice/Elisven11"
ma "\"{cps= 15}Oh... Yes, sir. A-and don’t worry, it was my own fault for not asking.{/cps}\""
"She tilts her face down, eyes on her feet as she scurries out of the room, and for a second it looks like she really started to cry." 
hide elisven a
hide yamakazi h
stop music
play music "BGM/majestic.ogg"
scene bg palace3
extend "I quickly change and join her in the hallway, but she seems to be passive and composed again by the time I get out there. 
 She begins to lead me to the dining room, and as we walk, I look around." 
"The building reminds me of a castle or a palace... Similar to human architecture, but not completely the same. Finally, we reach the dining room, where I see Ikeshia waiting at the table."
scene bg dinning room
stop music
play music"BGM/daily.ogg"
show ikeshia m at left
voice"Voice/Line26"
i "\"{cps= 15}You’re late! Very late!{/cps}\""
show yamakazi s at right
voice"Voice/Kusanagi 63"
k "\"{cps= 15}Excuse me your highness. I'm not really a morning person... or easy to wake up.{/cps}\""
voice"Voice/Line27"
i "\"{cps= 15}Enough with the excuses. I'm getting hungry.{/cps}\""
"As I sit down, the maid excuses herself and begins to serve breakfast."
hide ikeshia m
show ikeshia at left
voice"Voice/Line28"
i "\"{cps= 15}Tomorrow, try washing only your face instead of submerging your head in the whole wash-bin.{/cps}\""
"She giggles, motioning at my wet hair."
voice"Voice/Kusanagi 64"
k "\"{cps= 15}Oh, this is just how I wake up when I'm too sleepy, your highness.{/cps}\""
voice"Voice/Line29"
i "\"{cps= 15}I see. By the way, I hope you will be satisfied with her, but in any case, if you don’t feel good or right with her you can always ask to replace her with someone else.{/cps}\""
"I look at the maid, and I swear I see her shudder."
voice"Voice/Kusanagi 65"
k "\"{cps= 15}Thank you for providing her your highness. And I don’t think it will be necessary to replace her.{/cps}\""
"She smiles and moves to stand out the way after she finishes serving breakfast."
voice"Voice/Kusanagi 66"
k "\"{cps= 15}About last night your highness, I’m sorry if I said something I shouldn’t have. Also... you mentioned something about a situation? May I ask what situation were you referring to?{/cps}\""
"As I sip what appears to be a delicious home-blended tea, I can't shake the feeling of wanting to know exactly what's in it, trivial as that is. My thoughts keep shifting around, trying to decipher this amazing world, trying to figure out how to get back home, how to find out if Sachi is safe... 
 And yet my mind is enraptured, for a moment, simply with this tea."
"As much as I'd love to see more of this world, and as tempting as it would be to stay here... I also want to go back home. If only to see Sachi one last time."
voice"Voice/Line30"
i "\"{cps= 15}The situation we are facing at this moment is rather a strange one. During the past couple of days, there have been some mighty shakings of the earth...{/cps}\""
voice"Voice/Kusanagi 67"
k "\"{cps= 15}Shakings of the earth?{/cps}\""
voice"Voice/Line31"
i "\"{cps= 15}Yes... It’s as if the earth under our feet trembles violently. Some of the nobles and elders say it was because father announced me as the heir to his throne.{/cps}\""
"Thinking back... There was a huge earthquake in Tokyo a couple of days ago... Sachi was nearly hit by that driver right after it."
"Could the events be linked?"
voice"Voice/Kusanagi 68"
k "\"{cps= 15}Those are called earthquakes in my world, your highness, and they're pretty frequent where I come from. But it's been a few decades since we had a really huge one. Tell me your highness, how big was this earthquake?{/cps}\""
voice"Voice/Line32"
i "\"{cps= 15}Big enough to not be able to hold your balance at all. Big enough to shake this entire palace.{/cps}\""
voice"Voice/Kusanagi 69"
k "\"{cps= 15}Do you have any leads as to what caused it, aside from the rumors that say it's because of you?{/cps}\""
voice"Voice/Line33"
i "\"{cps= 15}No, none whatsoever.{/cps}\""
"As I finish my delicious breakfast, I start to ponder the earthquakes. They must not happen here if they don't even have a word for them, but then, what would make the earthquakes happen here? I can't help but think that there must be a connection between our two worlds."
voice"Voice/Kusanagi 70"
k "\"{cps= 15}Are there any magic spells or something like that that could cause this, your highness?{/cps}\""
voice"Voice/Line34"
i "\"{cps= 15}Nothing that could shake the entire world this badly.{/cps}\""
"Deep in thought, I don't even notice the maid reaching for my cup of coffee at the same time I go for it."
voice"Voice/Elisven12"
ma "\"{cps= 15}Oh, I'm sorry sir, I thought you were finished.{/cps}\""
voice"Voice/Kusanagi 71"
k "\"{cps= 15}Don’t worry about it.{/cps}\""
"The princess gives me a glare that could kill me... again. I look away and try to change the subject."
voice"Voice/Kusanagi 72"
k "\"{cps= 15}Can I possibly get a tour of the palace?{/cps}\""
"The maid smiles."
voice"Voice/Elisven13"
ma "\"{cps= 15}I-!{/cps}\""
voice"Voice/Line35"
i "\"{cps= 15}Yes, I would be happy to give you a tour of my home! After all, who else knows it better than me?{/cps}\""
"The maid doesn’t even get the slightest chance to reply."
voice"Voice/Kusanagi 73"
k "\"{cps= 15}Ah, yes, thank you your highness.{/cps}\""
voice"Voice/Line36"
i "\"{cps= 15}It doesn’t seem you’re too pleased.{/cps}\""
voice"Voice/Kusanagi 74"
k "\"{cps= 15}No, it’s not like that... I just thought you were busy.{/cps}\""
voice"Voice/Line37"
i "\"{cps= 15}Well I’m not! And besides, I do have to keep you under observation until we check your story. You could be an enemy spy- or assassin- or spy assassin for all we know! ...But, I will let Elisven come with us.{/cps}\""
voice"Voice/Kusanagi 75"
k "\"{cps= 15}Elisven?{/cps}\""
voice"Voice/Line38"
i "\"{cps= 15}Yes, your maid.{/cps}\""
"I stand up, and we set out to see the immense and luxurious palace."
hide yamakazi s
hide ikeshia
stop music
play music "BGM/Majestic.ogg"
scene bg palace3
pause 5
scene bg courtyard
"By the time we finish and arrive in the courtyard garden, it was half-past noon... Or at least, that was my best guess, based on the sun and the way my stomach was growling. Elisven giggled, and I knew she'd heard that. I looked away, embarrassed."
"Fortunately... or perhaps unfortunately, my embarrassment doesn't get to last long."
stop music
play music "BGM/Through.ogg"
"A masked man, armed with a sharp dagger, suddenly appears before us, and charges towards the princess."
"Caught off guard, I hesitate for a moment."

centered "{size= 150}TO BE CONTINUED{/size}"

return
