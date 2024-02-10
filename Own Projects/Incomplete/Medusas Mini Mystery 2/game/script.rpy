
init python:
    
    pos_x = 0
    pos_y = 0
    
    class TrackCursor(renpy.Displayable):

        def __init__(self, child):
            global pos_x
            global pos_y

            super(TrackCursor, self).__init__()

            self.child = renpy.displayable(child)

            self.x = pos_x #None
            self.y = pos_y #None

        def render(self, width, height, st, at):

            rv = renpy.Render(width, height)

            if self.x is not None:
                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (self.x - cw / 2, self.y - ch / 2))

            return rv

        def event(self, ev, x, y, st):
            global pos_x
            global pos_y

            if (x != self.x) or (y != self.y):
                self.x = x
                self.y = y
                pos_x = x
                pos_y = y
                renpy.redraw(self, 0)
                

#init python:
#    config.overlay_screens.append("torch")
screen dialog_torch():
    use torch(-1)
    
screen torch(_zorder=100):
    zorder _zorder
    add TrackCursor("images/torch98.png")
screen medusa:
  add im.Crop("images/Medusa3.png",(550,0,820, 1080)) at charaPos
  
screen dark_panorama():
  use panorama
  #use torch
  use pan_controls
  
init:
  
  $old_xpan = 0
  $old_ypan = 0
  $current_xpan = 0#45*3
  $current_ypan = 0#15*5
  $current_zoom = 1.0
  $current_xpanWrapped = False
  $zoom_offset_x = 0
  $zoom_offset_y = 0
  $zoom_offset_y_limit = 0
  $xpanWrappedl = False
  $xpanWrappedr = False
  $current_view = "room"
  
screen pan_controls:
  $xstepsize = 25#45
  $ystepsize = 15#15
  
  #$zoom_offset_x = 0
  #$zoom_offset_y = 0
  #$zoom_offset_y_limit = 0
  
  if current_zoom == 1.0:
    $zoom_offset_x = 0
    $zoom_offset_y = 0
    $zoom_offset_y_limit = 0
    $xstepsize = 25
  if current_zoom == 2.0:
    $zoom_offset_x = 24
    $zoom_offset_y = 47
    $zoom_offset_y_limit = 115
    $xstepsize = 10
  if current_zoom == 3.0:
    $zoom_offset_x = 32
    $zoom_offset_y = 65
    $zoom_offset_y_limit = 150
    $xstepsize = 7
  if current_zoom == 4.0:
    $zoom_offset_x = 36
    $zoom_offset_y = 72
    $zoom_offset_y_limit = 170
    $xstepsize = 5
  
  
  $xpanWrappedl = False
  $xpanWrappedr = False
  $left_pan = current_xpan - xstepsize
  #if left_pan < 0:
  #  $left_pan = 360 - left_pan
  #  $xpanWrappedl = True
  $right_pan = current_xpan + xstepsize
  #if right_pan >= 360:
  #  $right_pan = right_pan - 360
  #  $xpanWrappedr = True
    
  $up_pan = current_ypan - ystepsize
  if up_pan <= 0:
    $up_pan = 0
  $down_pan = current_ypan + ystepsize
  if down_pan >= 135 + zoom_offset_y_limit:
    $down_pan = 135 + zoom_offset_y_limit
  
  
  $out_zoom = current_zoom - 1.0
  if out_zoom <= 1.0:
    $out_zoom = 1.0
  $in_zoom = current_zoom + 1.0
  if in_zoom >= 4.0:
    $in_zoom = 4.0
  
  add "gui/overlay/room_navi.png"
  
  hbox:
    xoffset 10
    yoffset 10
    spacing 64
    imagebutton idle "gui/icons8-plus-64.png" hover "gui/icons8-plus-64.png"  action [SetVariable("current_zoom", in_zoom), SetVariable("current_xpan", int(current_xpan * (in_zoom/1.666))), SetVariable("current_ypan",  int(current_xpan * (in_zoom/1.666)))]
    imagebutton idle "gui/icons8-minus-64.png" hover "gui/icons8-minus-64.png"  action [SetVariable("current_zoom", out_zoom), SetVariable("current_xpan", old_xpan), SetVariable("current_ypan", old_ypan), SetVariable("current_view", "room")]
    
  imagebutton idle "gui/icons8-arrow-64.png" hover "gui/icons8-arrow-64.png" xpos 0 ypos 120 action [SetVariable("current_xpanWrapped", xpanWrappedl), SetVariable("current_xpan", left_pan)] at rotateButton(0)  
  imagebutton idle "gui/icons8-arrow-64.png" hover "gui/icons8-arrow-64.png" xpos 60 ypos 60 action SetVariable("current_ypan", up_pan) at rotateButton(90)
  imagebutton idle "gui/icons8-arrow-64.png" hover "gui/icons8-arrow-64.png" xpos 60 ypos 180  action SetVariable("current_ypan", down_pan) at rotateButton(-90)    
  imagebutton idle "gui/icons8-arrow-64.png" hover "gui/icons8-arrow-64.png" xpos 120 ypos 120  action  [SetVariable("current_xpanWrapped", xpanWrappedr), SetVariable("current_xpan", right_pan)] at rotateButton(180)
    
            
  vbox:
    yoffset 300
    text "x=[current_xpan] y=[current_ypan] z=[current_zoom]" xalign 0.5
    text "x=[zoom_offset_x] y=[zoom_offset_y] z=[zoom_offset_y_limit]" xalign 0.5
    text "[current_xpanWrapped], [current_view]" xalign 0.5
  
  key "K_UP" action SetVariable("current_ypan", up_pan)
  key "repeat_K_UP" action SetVariable("current_ypan", up_pan)
  key "K_DOWN" action SetVariable("current_ypan", down_pan)
  key "repeat_K_DOWN" action SetVariable("current_ypan", down_pan)
  key "K_LEFT" action SetVariable("current_xpan", left_pan)
  key "repeat_K_LEFT" action SetVariable("current_xpan", left_pan)
  key "K_RIGHT" action SetVariable("current_xpan", right_pan)
  key "repeat_K_RIGHT" action SetVariable("current_xpan", right_pan)
  
  #add TrackCursor("images/torch90.png")
  
screen panorama(_useTorch=False):
  #if _useTorch:                                  
    #add TrackCursor("images/torch90.png")
    #use torch
  #if current_xpanWrapped:
  #  text "WRAPPED" size 100
  #  add "images/Panoramabg_test6.png":
  #      zoom current_zoom
  #      xpan current_xpan
  #      ypan current_ypan
  #else:
  #add "images/Panoramabg_test6.png" at PositionBg(current_zoom, current_xpan, current_ypan, 0.2)
      #yalign 0.5      
  if current_view == "room":
    imagemap at PositionBg(current_zoom, current_xpan, current_ypan, 0.2):  
        idle "images/Panoramabg_shaded.png" 
        hover "images/Panoramabg_shaded_highlight_debug.png" 
        #Door
        hotspot (320, 88, 700, 345) action [SetVariable("old_xpan", current_xpan), SetVariable("old_ypan", current_ypan), SetVariable("current_zoom", 2), SetVariable("current_xpan", 8), SetVariable("current_ypan",  0), SetVariable("current_view", "door")]
        
        #Plants
        hotspot (30,530,230,640) action [SetVariable("current_xpan", -40), SetVariable("current_ypan",  30), SetVariable("current_zoom", 1),SetVariable("selected_item", "plant_left"), SetVariable("current_view", "room")]
        hotspot (1190,500,230,640) action [SetVariable("current_xpan", 15), SetVariable("current_ypan",  30), SetVariable("current_zoom", 1),SetVariable("selected_item", "plant_right"), SetVariable("current_view", "room")]
        
        #Stairs
        hotspot (110,110,300,200)   action [SetVariable("current_xpan", 0), SetVariable("current_ypan",  45), SetVariable("current_zoom", 1),SetVariable("selected_item", "stairs"), SetVariable("current_view", "room")]
        hotspot (260,260,300,200)   action [SetVariable("current_xpan", 0), SetVariable("current_ypan",  45), SetVariable("current_zoom", 1),SetVariable("selected_item", "stairs"), SetVariable("current_view", "room")]
        hotspot (410,410,300,200)   action [SetVariable("current_xpan", 0), SetVariable("current_ypan",  45), SetVariable("current_zoom", 1),SetVariable("selected_item", "stairs"), SetVariable("current_view", "room")]
        hotspot (560,560,300,200)   action [SetVariable("current_xpan", 0), SetVariable("current_ypan",  45), SetVariable("current_zoom", 1),SetVariable("selected_item", "stairs"), SetVariable("current_view", "room")]
        hotspot (710,710,300,200)   action [SetVariable("current_xpan", 0), SetVariable("current_ypan",  45), SetVariable("current_zoom", 1),SetVariable("selected_item", "stairs"), SetVariable("current_view", "room")]
        hotspot (860,860,300,200)   action [SetVariable("current_xpan", 0), SetVariable("current_ypan",  45), SetVariable("current_zoom", 1),SetVariable("selected_item", "stairs"), SetVariable("current_view", "room")]
        hotspot (1010,1010,300,200) action [SetVariable("current_xpan", 0), SetVariable("current_ypan",  45), SetVariable("current_zoom", 1),SetVariable("selected_item", "stairs"), SetVariable("current_view", "room")]
        hotspot (1160,1160,300,200) action [SetVariable("current_xpan", 0), SetVariable("current_ypan",  45), SetVariable("current_zoom", 1),SetVariable("selected_item", "stairs"), SetVariable("current_view", "room")]
        hotspot (1310,1310,300,200) action [SetVariable("current_xpan", 0), SetVariable("current_ypan",  45), SetVariable("current_zoom", 1),SetVariable("selected_item", "stairs"), SetVariable("current_view", "room")]
        
        
        #Table_small
        hotspot (140,950,620,800) action [SetVariable("old_xpan", current_xpan), SetVariable("old_ypan", current_ypan), SetVariable("current_zoom", 1), SetVariable("current_xpan", -20), SetVariable("current_ypan",  130), SetVariable("selected_item", "table_small"), SetVariable("current_view", "table_small")]
        #Crystal Ball
        #hotspot (440,900,260,260) action [SetVariable("selected_item", "crystal_ball"), SetVariable("current_view", "room")]
        
        #Floor notes - left
        hotspot (280,1420,265,130) action [SetVariable("selected_item", "recipe_l2g_torn_right"), SetVariable("current_view", "room")] #under table
        hotspot (820,1245,380,280) action [SetVariable("selected_item", "hint_papers_1"), SetVariable("current_view", "room")] #under stairs
        
        #Wall Notes
        hotspot (1600, 410, 575, 370) action [SetVariable("old_xpan", current_xpan), SetVariable("old_ypan", current_ypan), SetVariable("current_zoom", 2), SetVariable("current_xpan", 70), SetVariable("current_ypan",  75)]
        #Harp
        hotspot (2400, 730, 330, 740) action [SetVariable("old_xpan", current_xpan), SetVariable("old_ypan", current_ypan), SetVariable("current_zoom", 2), SetVariable("current_xpan", 105), SetVariable("current_ypan",  135), SetVariable("current_view", "harp")]
        #Cabinet
        
        #Fireplace
        #Cauldren 
        #Shelves
        hotspot (4640, 300, 1000, 1060) action [SetVariable("old_xpan", current_xpan), SetVariable("old_ypan", current_ypan), SetVariable("current_zoom", 1), SetVariable("current_xpan", 210), SetVariable("current_ypan",  65), SetVariable("current_view", "shelves")]
        #Floor notes - right
        hotspot (4875,1270,200,140) action [SetVariable("selected_item", "floor_notes_3"), SetVariable("current_view", "room")] #notes under shelves
        
        #Table_large
        #Tome
        #Lockbox
        #maze
        
  if current_view == "door":
    imagemap at PositionBg(current_zoom, current_xpan, current_ypan, 0.2):  
        idle "images/Panoramabg_shaded.png" 
        hover "images/Panoramabg_shaded_highlight_debug.png" 
        hotspot (700, 160, 120, 120) action SetVariable("selected_item", "door_symbol")
        hotspot (630, 150, 50, 50) action SetVariable("selected_item", "door_lock_1")
        hotspot (820, 150, 60, 50) action SetVariable("selected_item", "door_lock_2")
        hotspot (820, 270, 50, 50) action SetVariable("selected_item", "door_lock_3")
        hotspot (650, 260, 50, 50) action SetVariable("selected_item", "door_lock_4")
        
  if current_view == "harp":
    imagemap at PositionBg(current_zoom, current_xpan, current_ypan, 0.2):  
        idle "images/Panoramabg_shaded.png" 
        hover "images/Panoramabg_shaded_highlight_debug.png" 
        hotspot (2420, 914, 300, 530) action SetVariable("selected_item", "lyre_pedestal")
        hotspot (2450, 730, 280, 260) action SetVariable("selected_item", "lyre")
        hotspot (2505, 770, 30, 160) action SetVariable("selected_item", "lyre_string_1")
        if string_2_found:
            hotspot (2535, 770, 30, 160) action SetVariable("selected_item", "lyre_string_2")
        if string_3_found:
            hotspot (2566, 770, 30, 160) action SetVariable("selected_item", "lyre_string_3")
        if string_4_found:
            hotspot (2597, 770, 30, 160) action SetVariable("selected_item", "lyre_string_4")
        hotspot (2625, 770, 30, 160) action SetVariable("selected_item", "lyre_string_5")
        hotspot (2520, 1010, 90, 60) action SetVariable("selected_item", "lyre_pedestal_drawer")
        
  if current_view == "shelves":
    imagemap at PositionBg(current_zoom, current_xpan, current_ypan, 0.2):  
        idle "images/Panoramabg_shaded.png" 
        hover "images/Panoramabg_shaded_highlight_debug.png" 
        hotspot (4640, 380, 1000, 200) action [SetVariable("old_xpan", current_xpan), SetVariable("old_ypan", current_ypan), SetVariable("current_zoom", 2), SetVariable("current_xpan", 230), SetVariable("current_ypan",  65), SetVariable("current_view", "shelves")]
        hotspot (4640, 570, 1000, 200) action [SetVariable("old_xpan", current_xpan), SetVariable("old_ypan", current_ypan), SetVariable("current_zoom", 2), SetVariable("current_xpan", 230), SetVariable("current_ypan",  80), SetVariable("current_view", "shelves")]
        hotspot (4640, 750, 1000, 200) action [SetVariable("old_xpan", current_xpan), SetVariable("old_ypan", current_ypan), SetVariable("current_zoom", 2), SetVariable("current_xpan", 230), SetVariable("current_ypan",  115), SetVariable("current_view", "shelves")]
        hotspot (4640, 910, 1000, 200) action [SetVariable("old_xpan", current_xpan), SetVariable("old_ypan", current_ypan), SetVariable("current_zoom", 2), SetVariable("current_xpan", 230), SetVariable("current_ypan",  140), SetVariable("current_view", "shelves")]
        hotspot (4640, 1060, 1000, 300) action [SetVariable("old_xpan", current_xpan), SetVariable("old_ypan", current_ypan), SetVariable("current_zoom", 2), SetVariable("current_xpan", 230), SetVariable("current_ypan",  180), SetVariable("current_view", "shelves")]
      
  if current_view == "table_small":
    imagemap at PositionBg(current_zoom, current_xpan, current_ypan, 0.2):  
        idle "images/Panoramabg_shaded.png" 
        hover "images/Panoramabg_shaded_highlight_debug.png" 
        #table
        hotspot (140,950,620,400) action [SetVariable("old_xpan", current_xpan), SetVariable("old_ypan", current_ypan), SetVariable("current_zoom", 2), SetVariable("current_xpan", 0), SetVariable("current_ypan",  175), SetVariable("current_view", "table_small"), SetVariable("selected_item", "table_small")]
        #crystal ball
        hotspot (440,900,260,260) action [SetVariable("old_xpan", current_xpan), SetVariable("old_ypan", current_ypan), SetVariable("current_zoom", 2), SetVariable("current_xpan", 5), SetVariable("current_ypan",  145), SetVariable("current_view", "table_small"), SetVariable("selected_item", "crystal_ball")]
        #drawer
        hotspot (160, 1280, 590, 195) action [SetVariable("old_xpan", current_xpan), SetVariable("old_ypan", current_ypan), SetVariable("current_zoom", 2), SetVariable("current_xpan", -5), SetVariable("current_ypan",  215), SetVariable("current_view", "table_small_drawer"), SetVariable("selected_item", "table_small")]
        #hotspot (140,950,620,800) action [SetVariable("selected_item", "table_small"), SetVariable("current_view", "table_small")]
        #Crystal Ball
        #hotspot (440,900,260,260) action [SetVariable("selected_item", "crystal_ball"), SetVariable("current_view", "table_small")]
  #add "images/bg room.png"
  #use pan_controls
  add "gui/centerMarker.png"  
            
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")
image bg room = "images/bg room.png"
image black = Solid("#000000")
image bg black = Solid("#000000")
image bg white = Solid("#FFFFFF")
image bg panorama = "images/Panoramabg_shaded.png"
image medusa neutral = "images/Medusa3.png"

# The game starts here.

label start:
    #jump lbl_test_random_character_speaks
    #jump lbl_torch_test
    #start game
    jump lbl_intro # 420 words
    
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg panorama:
    #  yalign 0.5
    #  xalign 0.5
    #
    ## This shows a character sprite. A placeholder is used, but you can
    ## replace it by adding a file named "eileen happy.png" to the images
    ## directory.
    #
    #show medusa neutral
    #
    ## These display lines of dialogue.
    #
    #show medusa at show_snake1
    #
    #a "Pssst everyone wake up."
    #show medusa at show_snake2
    #b "Huh? What is it?"
    #show medusa at show_snake3
    #c "Huh? What is it?"
    #show medusa at show_snake4
    #d "Huh? What is it?"
    #show medusa at show_snake5
    #e "Huh? What is it?"
    #show medusa at show_snake6
    #f "Huh? What is it?"
    #show medusa at show_medusa
    #m "Huh? What is it?"
    #
    #menu:
    #  "Choose?"
    #  "Panorama test":
    #    jump lbl_panorama_test
    #  "Torch test":
    #    jump lbl_torch_test
    #  "Skip":
    #    pass
    ## This ends the game.
    #
    #return
  
label lbl_torch_test:
  scene bg black
  #show screen torch
  #call screen panorama(True)
  #show screen medusa  
  #jump lbl_panorama_test
  call screen dark_panorama
  "testing panorama" 
  
label lbl_panorama_test:
  show screen panorama(False)
  
  #show screen pan_controls
  
  #show medusa
  scene bg panorama:
      yalign 0.5
      zoom 1.0
      xpan current_xpan
      #xpan 0
      #linear 0.1 xpan 60
      #pause 2.0
      #linear 0.1 xpan 120
      #pause 2.0
      #linear 0.1 xpan 180
      #pause 2.0
      #linear 0.1 xpan 240
      #pause 2.0
      #linear 0.1 xpan 300
      #pause 2.0
      #linear 0.1 xpan 360
      #pause 2.0
      #xpan 100
      #zoom 1.0
      #linear 10.1 xpan 160
      #xpan 100
      #zoom 2.0
      #linear 10.1 xpan 160
      #xpan 100
      #linear 0.1 zoom 3.0
      #linear 10.1 xpan 160
      #xpan 100
      #linear 0.1 zoom 4.0
      #linear 10.1 xpan 160
      #xpan 100
      #linear 0.1 zoom 5.0
      #linear 10.1 xpan 160
      #block:
      #  xpan 350
      #  zoom 1.0
      #  pause 2.0
      #  zoom 2.0
      #  pause 2.0
      #  zoom 3.0
      #  pause 2.0
      #  #linear 36.0 xpan 360
      #  zoom 4.0
      #  pause 2.0
      #  repeat
  
  #"testing panorama" 
  return
  
#### Helper labels ####

label show_background(_xpan=0, _ypan=0, zoom=0):
  $current_zoom = zoom
  $current_xpan = _xpan
  $current_ypan = _ypan
  show bg panorama at PositionBgInstant(_xpan, _ypan, zoom)
  return
  
label show_background_current():
  show bg panorama at PositionBgInstant(current_zoom, current_xpan, current_ypan)
  return

#######################
  
  
##----- Intro -----##
label lbl_intro:
  scene bg black
  
  "Melissa slowly stepped through the door in the floor and carefully walked down the wooden stairs into the dark basement."
  "The were a few loud clicks as the locks snapped shut behind them."
  "Wah!"
  "The last of the light had disappeared with the closing of the door so they were now in complete darkness."
  
  "Where did i put the torch? Melissa fumbles about in her pockets for a small torch."
  "Ah, her-"
  "I-I'LL H-HOLD IT! Casssie snapped the torch out of her hand and after some fiddling managed to get it turned on."
  call show_background(20, 90, 1.0)
  show screen dialog_torch
  show medusa shock
  
  #"Maybe we should read the letter we received before we do anything else?"
  #"Oh good idea."
  #"Lemme see, here. Melissa holds up the letter to the torchlight and begins to read."
  #
  #"Welcome, weary travelers, as you have no doubt surmised this quaint little cottage in the middle of the forest was actually home to an evil witch!"
  #"A forest? Did we pass a forest?"
  #"Its all part of the theme, just go along with it."
  #
  #"Melissa continued. The basement you have been lead into is not the sleeping area you were expecting but instead a holding area for the witch to keep prisoners for her experiments."
  #"Oooh spooky~"
  #
  #"The witch has locked you up and went off to retrieve a magic item, if you are still trapped within these walls when she returns in 1 hour, you will be forced to remain here forever!"
  #"Oh a time limit!"
  #"Find the 4 magic keys to unlock the basement door and make your escape!"
  
  #"Oh theres a note on the back."
  #"Your safety is a priority here at Minotaur labyrinths and Escape rooms so remember the following rules:"
  #"- No running - It is a dark room after all"
  #"- Do not try to move any large furniture items, these will not be required as part of the escape"
  #"- Do not consume any items unless explicitly instructed to do so."
  #"- If you need to leave early you may return to the entrance and say \"Open sesame\" to be released early (no refunds)"
  #"- And most importantly, Have fun! )"
  
  $ready_to_start = "Ok, i guess we are ready to start puzzling!"
  "[ready_to_start]"
  call lbl_team_name
  "[ready_to_start]"
  jump lbl_game_room_start
  return
  
label lbl_team_name:
#  "Wait, we forgot one important step."
#  "Yeah?"
#  "The team name!"
#  "Oh right! But the clock is ticking so lets decide quickly."
#  "Since theres 7 of us maybe 7 Deadly Sins >:D"
#  "I-Im terrified get me out of here....You know has a joke. haha"
#  "How about Daisy and the do-littles. :3"
#  "Daisy thinking very highly of herself today."
#  
#  $you_think = "What do you think Melissa?"
#  "[you_think]"
#  
#  $choice_happy = "Excellent choice!"
#  menu:
#    "[you_think]"
#    "7 Deadly Sins":
#      $team_name = "7 Deadly Sins"
#      f "[choice_happy]"
#    "I-Im terrified get me out of here":
#      $team_name = "I'm terrified get me out of here!"
#      c "[choice_happy]"
#    "Daisy and the do-littles":
#      $team_name = "Daisy and the do-littles"
#      d "[choice_happy]"
#    "I have a better idea.":
#      $team_name = renpy.input("Team name?", length=32)
#      $team_name = povname.strip()
#      a "[choice_happy]"  
#  
  return
  
  
##----- Ending -----##
label lbl_feedback:
  minotaur "Could you give us some feedback on the escape room before you go?"
  "Melissa and the Minotaur spend some time talking about how they found the room and any suggestions or improvements mentioned were noted."
  return

#label lbl_ending_out_early:
#  scene bg black with flash
#  "The doors swung open quickly with the utterance of the safety phrase."
#  minotaur "Is everything ok?"
#  m "We just needed to get out."
#  minotaur "Thats totally understandable, dark rooms arent for everyone and we always have our customers interests at heard. The minotaur spoke proudly."
#  
#  call lbl_ending_no_finish
#  return
#  
#label lbl_ending_times_up:
#  "A small buzzer sounds as the allotted time passes."
#  scene bg black with flash
#  "The doors open up and Melissa left the room."
#  
#  minotaur "I thought the local detective would have no trouble with a room like this."
#  
#  call lbl_ending_no_finish
#  return
#  
#
#label lbl_ending_no_finish:
#  minotaur "Its a pity you didn't end up finishing the room, but-"
#  call lbl_feedback
#  return


label lbl_ending:
  
  scene bg black with flash
  "There is a flash as the last key clicks into place. The door swings open with a loud creak and Melissa steps into the hallway."
  
  minotaur "Congratulations! You have escaped the witches basement and are free!"
  "The Minotaur who had previously been at the reception desk popped off a streamer and excitedly danced around with them."
  
  minotaur "I'm excited to know what you guys think since you're the first ones to complete the new room."
  
  minotaur "Im really glad you were able to take on this job, hopefully its not keeping you from anything too important."
  "Its ok, its been a slow week."
  
  call lbl_feedback
  
  minotaur "One last thing before you go, let me put you guys on the leaderbaord, whats your team name?"
  $team_name = renpy.input("Team name?", length=32)
  $team_name = povname.strip()
  all "[team_name]"
  
  
  return
  
  
##----- Game room -----##
label lbl_game_room_start:
  "Finally they get a good look at the room. It is themed like a witches basement with various things on each of the 4 sides of the room."
  a "We better go find those keys!"
  jump lbl_room_explore
  
  
label lbl_room_explore:
  call screen dark_panorama()
  
  $ret = _return
  call expression _return
  
  jump lbl_room_explore
  
  
label lbl_game_room_door:
  if keys_count < 4:
    "Looks like we need 4 keys to get this open again."
  else:
    "Now that we have all the keys we can get out of here"
    jump lbl_ending
    
  return
  

#----- Crystal Ball -----
label lbl_crystal_ball:
  "It is a crystal ball with a faint glow."
  "Theres a drawer here but it wont budge, is this part of the puzzle?"
  
  cb "I am the spirit of the crystal ball and keeper of a sacred key! The ball springs to life as a voice calls out from it."
  cb "Answer me the following riddles and it's yours!"
  $answer_list = [["spellbook", "magicbook", "spell book", "magic book", "spell tome", "magic tome", "tome"],
                  ["potion", "potions"],
                  ["crystalball", "crystal ball"],
                  ["siren", "mermaid"]]
  $riddle_max = 3
  $riddle_current = 0
  
  menu:
    "Answer":
      jump lbl_crystal_ball_riddles
    "Go back":
      return
  
label lbl_crystal_ball_riddles:
  if riddle_current == 0:
    cb "With symbols and glyphs, my pages adorned"
    cb "A sorcerer's ally, where spells are born."
    #cb "Wizards seek me to learn their craft,"
    #cb "Within my bindings, their knowledge raft."
    jump lbl_answer
  if riddle_current == 1:
    cb "Born of magic, brewed with care,"
    cb "A concoction beyond compare."
    #cb "Healing woes, or curses deep,"
    #cb "In the cauldron's embrace, our secrets sleep."
    jump lbl_answer
  if riddle_current == 2:
    cb "A sphere of glass, an enigmatic show,"
    cb "Glimpses of what's to come, I bestow."
    #cb "Peer deep within, the answers you'll find,"
    #cb "In this realm of magic, destinies entwined."
    jump lbl_answer
  #if riddle_current == 3:
  #  cb "With flowing hair and eyes that gleam,"
  #  cb "I tempt sailors into my dream."
  #  cb "Beware the seas where I reside,"
  #  cb "My haunting call, a treacherous guide."
  #  jump lbl_answer
    
  return

label lbl_answer:
  
  cb "What am i?"
  $riddle_answer = renpy.input("Team name?", length=32)
  $riddle_answer = povname.strip()
  
  if riddle_answer.lower() in answer_list[riddle_current]:
    cb "Correct!"
    if riddle_current == riddle_max -1:
      jump lbl_crystal_ball_success
    else:
      $riddle_current = lbl_crystal_ball_riddles +1
      jump lbl_crystal_ball_riddles
  
  
label lbl_crystal_ball_success:
  cb "I bow to your wisdom."
  "The crystal ball flicker for a second and then with a click the previously locked drawer popped open revealing one of the magic keys"
  call lbl_key_get
  return

label lbl_crystal_ball_failure:
  cb "That is incorrect, please think about your answers and try again later."
  return

#----- Harp Puzzle -----

label lbl_harp_start:
  "Whats this, like a harp or something?"
  "A Lyre"
  "What did you call me?"
  "Ugh nevermind"
  
  "Theres a little drawer on the pedestal but it wont open."
  "I bet thats where the key is!"
  "Since it an instrument maybe we need to play some music to unlock it?"
  "Its missing some strings so i dunno how much we are going to be able to play."
  
  "Maybe we should look for some extra strings?"
  "Or some hints on what to play."
  
  "Try playing?"  
  menu:
    "Yes":
      $song_notes = ""
      jump lbl_harp_play
    "No":
      pass
  
  return
  
  
  
label lbl_harp_play:
  $pluck = "Pluck the string marked"
  menu:    
      "[pluck] F":
        $song_notes = song_notes+"F"
      "[pluck] D" if string_4_found:
        $song_notes = song_notes+"D"
      "[pluck] B" if string_3_found:
        $song_notes = song_notes+"B"
      "[pluck] G" if string_2_found:
        $song_notes = song_notes+"G"
      "[pluck] E":
        $song_notes = song_notes+"E"
      "Stop":
        jump lbl_harp_song

label lbl_harp_song:
  if song_notes == "EGBBD":
    "As the song finishes the harp starts to glow and adds on a little musical flourish of its own before the drawer in the pedestal clicks open."
    jump lbl_key_get
  if song_notes == "EGF":
    "There's a loud click to the right as something unlocked."
    $music_drawer_unlocked = True
  else:
    "It was a nice little tune but it doesn't look like anything else happened."
    
  return
  
label music_drawer:
  "It's a small wooden set of drawers."
  menu:
    "Check the first drawer":
      "It opens easily and you find a string inside."
      $string_4_found = True
    "Check the second drawer":
      if not music_drawer_unlocked:
        "It doesn't seem to open, but there are some musical notes carved in the front."
        "Maybe we have to unlock it somehow?"
      else:
        "It opens easily and you find a string inside."
        $string_3_found = True
        
    "Check the third drawer":
      "Looks like theres a combination needed to open this one."
      $music_drawer_combo = renpy.input("???", length=3)
      if music_drawer_combo == "230":
        "The drawer clicks as the last digit is entered."
        "It opens easily and you find a string inside."
        $string_2_found = True
      else:
        "That wasn't it, maybe theres a clue somewhere about what numbers to use."
        return
    

#----- Cauldron Puzzle -----

label lbl_cauldron_start:
  "A large cauldron sits in the fireplace. It is empty so you can see a black key at the bottom."
  "Oh that was an easy one."
  "Hnnnnng- "
  "The key however refuses to budge."
  "Is theres some trick to it?"
  "Oh it looks like theres a note in here too."
  "The key LEADen with weight from the past must be transformed to receive the GOLDen light of freedom."
  "Wierd flavour text, but i guess the highlighted parts are important"
  jump lbl_cauldron_mix
  
label lbl_cauldron_mix:
  "Maybe we can use it to mix something?"
  $ingredient_list = []
  $potion_philstone = False
  
  call lbl_cauldron_ingredients
  
  #jump lbl_cauldron_mix_check
  return
  
label lbl_cauldron_mix_check:
  call show_background(180, 135, 1.0)

  $key_potion = [False, False, False, False]
  $fire_potion = [False, False, False, False]
  
  if len(ingredient_list) == 3:
    if "ingredient_dragon_fang" in ingredient_list:
      $key_potion[0] = True
      $fire_potion[0] = True
      
    if "ingredient_harpy_feather" in ingredient_list:
      $key_potion[1] = True
      
    if "ingredient_quicksilver" in ingredient_list:
      $key_potion[2] = True
      
    if "ingredient_allspice" in ingredient_list:
      $fire_potion[1] = True
      
    if "ingredient_campfire_ash" in ingredient_list:
      $fire_potion[2] = True
      
    if potion_philstone:
      $key_potion[3] = True
      $fire_potion[3] = True
      
    #"[fire_potion]"
      
    if key_potion[0] and key_potion[1] and key_potion[2] and key_potion[3]:
      "It looks like the mix was a success, and it glows a bright white before evaporating in the cauldron leaving behind a shining gold key."
      jump lbl_key_get
    if fire_potion[0] and fire_potion[1] and fire_potion[2] and not fire_potion[3]:
      "It looks like the mix was a success, and it glows a bright red. You put some in a little bottle and the remaining liquid evaporates."
      $fire_potion_get = True
      return
    
  "The mix doesn't seem to have worked as expected as it lets off a foul oder before evaporating leaving nothing behind but the black key."
  return
  
  
screen ingredient_picker_items:
    #style_prefix "game_menu"
    
    use pan_controls
    imagemap at PositionBg(current_zoom, current_xpan, current_ypan, 0.2):  
        idle "images/Panoramabg_shaded.png" 
        hover "images/Panoramabg_shaded_highlight.png" 
        hotspot (4730, 380, 50, 200) action SetVariable("selected_item", "ingredient_salt")
        hotspot (4780, 440, 45, 100) action SetVariable("selected_item", "ingredient_allspice")
        hotspot (4830, 420, 30, 150) action SetVariable("selected_item", "ingredient_cumin")
        hotspot (4860, 420, 50, 120) action SetVariable("selected_item", "ingredient_coriander")
        hotspot (4920, 420, 50, 120) action SetVariable("selected_item", "ingredient_garlic")
        hotspot (4960, 480, 50, 80) action SetVariable("selected_item", "ingredient_dust")
        hotspot (5000, 480, 50, 100) action SetVariable("selected_item", "ingredient_tears")
        
        hotspot (5360, 480, 200, 100) action SetVariable("selected_item", "ingredient_dragon_fang")  
        
        hotspot (4720, 540, 100, 200) action SetVariable("selected_item", "ingredient_harpy_feather")
        hotspot (4810, 620, 150, 100) action SetVariable("selected_item", "ingredient_slime_red")
        hotspot (4990, 560, 100, 180) action SetVariable("selected_item", "ingredient_onion")
        
        hotspot (5220, 660, 70, 100) action SetVariable("selected_item", "ingredient_candle_wax")
        hotspot (5280, 650, 110, 100) action SetVariable("selected_item", "ingredient_quicksilver")
        hotspot (5430, 620, 110, 100) action SetVariable("selected_item", "ingredient_poison")      
        
        hotspot (4780, 810, 160, 100) action SetVariable("selected_item", "ingredient_slime_blue")
        hotspot (4950, 760, 180, 150) action SetVariable("selected_item", "ingredient_book_worms")
        
        hotspot (5180, 800, 110, 100) action SetVariable("selected_item", "ingredient_candle_wicks")
        hotspot (5300, 800, 100, 100) action SetVariable("selected_item", "ingredient_dragon_orbs")
        hotspot (5400, 800, 100, 100) action SetVariable("selected_item", "ingredient_harpy_talon") 
        
        hotspot (4780, 960, 150, 100) action SetVariable("selected_item", "ingredient_campfire_ash")
        hotspot (4940, 960, 150, 100) action SetVariable("selected_item", "ingredient_cheese_holes")
        
        hotspot (5200, 950, 150, 100) action SetVariable("selected_item", "ingredient_dragon_scale")
        hotspot (5330, 950, 150, 100) action SetVariable("selected_item", "ingredient_emerald_ice")
        hotspot (5440, 910, 90, 200) action SetVariable("selected_item", "ingredient_cyclops_eye")
    
    use torch
    
screen ingredient_picker:
    use ingredient_picker_items
    add im.FactorScale("gui/overlay/potion_overlay.png", 1.5) xoffset -150
    frame:
        style_prefix "ingredient_check"
        vbox:
            spacing 50
            yoffset -200
            vbox at vbox_rotate:
                for item in ingredient_list:
                    $item_details = GetItemDetails(item)
                    label "- [item_details[1]]" #text_size 24 text_font gui.interface_font
                    
        vbox at vbox_rotate(0):
                xalign 0.5
                yalign 1.0
                yoffset 80
                #if potion_philstone_found:
                if potion_philstone:
                    vbox at vbox_rotate(-5):
                        yoffset 180
                        textbutton _("Use Philosophers Stone") action SetVariable("potion_philstone", False)
                else:
                    vbox at vbox_rotate(-5):
                        yoffset 180
                        textbutton _("{s}Use Philosophers Stone{/s}") action SetVariable("potion_philstone", True)
                if len(ingredient_list) < 4:
                    if (selected_item and not selected_item == ""): 
                        $item = GetItemDetails(selected_item)
                        label "Selected Item: [item[1]]" xalign 0.5
                        textbutton "Add to potion!" xalign 0.5 action Return(selected_item)
                    else:
                        label " " xalign 0.5
                        label " " xalign 0.5
                else:
                    label " " xalign 0.5
                    label " " xalign 0.5
                #    label "Nothing Selected" xalign 0.5
                #    textbutton "Add to potion!" xalign 0.5 action NullAction()
                
                if len(ingredient_list) > 0:
                    textbutton "Brew!" xalign 0.5 action Return("brew")
                else:
                    textbutton "Cancel!" xalign 0.5 action Return("cancel")
  
style ingredient_check_label is pref_label
style ingredient_check_label_text is pref_label_text
style ingredient_chect_text is pref_label_text
style ingredient_check_button is gui_button
style ingredient_check_button_text is gui_button_text
style ingredient_check_vbox is pref_vbox

style ingredient_check_frame:    
    xoffset 100
    yoffset 250
    xsize 500
    ysize 450
    background None
    

style ingredient_check_vbox:
#    spacing gui.pref_button_spacing
    xsize 500

style ingredient_check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style ingredient_check_button_text:
    properties gui.button_text_properties("check_button")
    size 24 
    idle_color "#555353"
    
style ingredient_check_label_text:  
    size 24 
    color "#000000"
    
transform vbox_rotate(_rot=-5):
    rotate _rot
  
label lbl_cauldron_ingredients:
    call show_background(200, 51, 1.0)
    call screen ingredient_picker
 #menu:
 #  "Pick an ingredient":
 #    
 #  "Use Philosopher Stone" if potion_philstone_found:
 #    $potion_philstone = True
 #  "Done":
 #    return
      
    if _return == "brew":
        jump lbl_cauldron_mix_check
    if _return == "cancel":
        return
    if not _return == None:
        $ingredient_list.append(_return)
        jump lbl_cauldron_ingredients

label lbl_cauldron_cupboards:
  menu:
    "Check left cupboard":
      "It opens easily but there doesn't seem to be anything important in it."
    "Check right cupboard":
      if not cauldron_cupboard_unlocked:
        "You try to open the cupboard but it seemed to be sealed shut by some material."
        "Its cold to the touch."
        if not fire_potion_get:
          "Ice?"
          "Maybe theres a way to melt it."
        else:
          "Oh wait, we have that potion we made."
          menu:
            "Pour the potion on the material.":
              "You pour a little of the potion on the material but there is no reaction."
              "Maybe thats not the way to use it."
            "Drink the potion":
              "Well here goes nothing."
              "Melissa takes a large swig of the potion and waits for the effect."
              "She doesn't have to wake long as a warm feeling starts to quickly build up in her mouth"
              "AHHHHHH~"
              "Ah Melissa and the snakes open their mouths to cool down a lick of flames shoots out from them and blasts the icy material."
              "As it starts to melt the burning in their mouths is quickly replaced with a cool soothing sensation."
              "LETS DO THAT AGAIN!"
              "NO!"
              "Aww..."
              $cauldron_cupboard_unlocked = True
              return
            "Do nothing":
              return
              
      else:
        if not potion_philstone_found:
          "Inside you find a glowing red stone with a tag that says \"Philosophers Stone: Use with caution.\""
          $potion_philstone_found = True
        else:
          "There doesn't seem to be anything else here."
          return
          
  return

#----- Spell book puzzle -----
label lbl_spellbook_start:
  "Looks like a spell book and some pages are strewn about the table."
  "Theres also a box with a lock symbol surrounded by magic symbols."
  "There doesn't seem to be any obvious opening so maybe we need some magic to open it?"
  
  jump lbl_spellbook_spell
  
label lbl_spellbook_spell:
  
  $box_spell = renpy.input("Team name?", length=32)
  $box_spell = povname.strip()
  
  if box_spell.lower() == "liberate hold":
    "As you utter the magic words the top of the box slides open to reveal the key."
    jump lbl_key_get
  else:
    "There was no noticeable effect."
  
  return  
  

#----- Misc / reusable labels -----

label lbl_key_get:
  $keys_count = keys_count + 1
  $keys_left = 4 - keys_count
  $keys_a = "a"
  if keys_count > 0:   
    $keys_a = "another"
    
  "Awesome we got [keys_a] key!"
  
  if keys_count < 4:
    "Looks like theres only [keys_left] left!"
  else:
    "That was the last key we needed!"
  return 
  
  
#----- Item speeches -----
label lbl_test_random_character_speaks:
    show side_medusa at show_side_medusa_instant:
        xalign 0.0
        yalign 1.0
        
    call Item_interact("d","poster_maze")
    call Item_interact("","")
    call Item_interact("","ingredient_cumin")
        
    show side_medusa at show_side_full
    m " Whats this?"
    call SaySomething("a", "NANI?!")
    call SaySomething("b", "NANI?!")
    call SaySomething("c", "NANI?!")
    call SaySomething("d", "NANI?!")
    call SaySomething("e", "NANI?!")
    call SaySomething("f", "NANI?!")
    show side_medusa at show_side_full
    m "Hmmm..."
    call SaySomething("", "NANI?!")
    call SaySomething("", "NANI?!")
    call SaySomething("", "NANI?!")
    call SaySomething("", "NANI?!")
    return
    
label SaySomething(_who="",_what=""):
    if _who == "":
        $_who = renpy.random.choice(['a', 'b', 'c', 'd', 'e', 'f'])
    
    if _who == "a":
        #"agness"
        show side_medusa at show_side_snake1
        a "[_what]"
    if _who == "b":
        show side_medusa at show_side_snake2
        b "[_what]"
    if _who == "c":
        show side_medusa at show_side_snake3
        c "[_what]"
    if _who == "d":
        show side_medusa at show_side_snake4
        d "[_what]"
    if _who == "e":
        show side_medusa at show_side_snake5
        e "[_what]"
    if _who == "f":
        show side_medusa at show_side_snake6
        f "[_what]"
        
    return
    
    
label Item_interact(_who="", _item_id=""):
    $item = GetItemDetails(_item_id)
    
    show side_medusa at show_side_full
    m "Looks like [item[1]]."
    call SaySomething(_who, item[3])
    
    return
    