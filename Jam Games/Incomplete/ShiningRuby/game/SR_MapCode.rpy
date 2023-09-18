init:
  $TimeOfDay = 'Day'
  
label lbl_ReturnToMap:
  "Lets check the map."
  jump lbl_mapStart
  
  return

label lbl_mapStart:
    scene black
    "Lets explore the city. It is currently [TimeOfDay]."
    call screen Map_City
    
    #jump to returned label
    call expression _return from _call_expression

label lbl_Continue:
    menu:
        "Try somewhere else?"
        "Yes, I might've missed something!":
            jump lbl_mapStart
        "We should try again in the Morning":
            $TimeOfDay = 'Day'
            jump lbl_mapStart
        "We should try again at night":
            $TimeOfDay = 'Night'
            jump lbl_mapStart
        "No, I think we are finished here.":
            pass
    jump lbl_ExitMap
    
label lbl_ExitMap:
    "I guess thats the end of that then."
    
    return

init -2:
    transform config_eff(_rotate):
        on idle:
            easein 0.1 rotate _rotate+0
        on selected_idle:
            easein 0.5 rotate _rotate+0
        on hover:
            easein 0.1 rotate _rotate+5
            easein 0.1 rotate _rotate-5
            repeat
        on selected_hover:
            easein 0.3 rotate _rotate+5
            easein 0.3 rotate _rotate-5
            repeat

    $rotate_north = 0
    $rotate_N = 0
    $rotate_NE = 45
    $rotate_E = 90
    $rotate_SE = 135
    $rotate_S = 180
    $rotate_SW = 225
    $rotate_W = 270
    $rotate_NW = 315
    
screen Map_arrow(_leadsTo, _direction, _xpos, _ypos, _size = 75):
  #imagebutton auto im.Scale("images/ui/map/N_%s.png") xpos 0 ypos 0 action Return()
  $idleimg = im.Scale("images/ui/map/arrow/N_idle.png", _size, _size)
  $hoverimg = im.Scale("images/ui/map/arrow/N_hover.png", _size, _size)
  $groundimg = im.Scale("images/ui/map/arrow/N_ground.png", _size, _size)
  imagebutton idle idleimg hover hoverimg insensitive groundimg xpos _xpos ypos _ypos focus_mask True action Return(_leadsTo) at config_eff(_direction)
  #imagebutton auto im.Scale("images/ui/map/N_%s.png", 100, 100) xpos 0 ypos 0 action Return()
  #imagebutton idle idleimg hover hoverimg insensitive groundimg xpos 100 ypos 1000 action None
  
    
screen Map_City:
    tag map_screen
    add im.Scale("images/ui/Map_Background.png", 1366, 768)
    imagebutton auto "images/ui/exitbutton_%s.png"  xpos 0 ypos 0 focus_mask True action Return("lbl_ExitMap")
    #imagebutton auto "images/ui/doorbutton_%s.png"  xpos 200 ypos 200 focus_mask True action Return("lbl_Bathroom")
    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 50 ypos 350 focus_mask True action Return("lbl_Classroom")
    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 100 ypos 200 focus_mask True action Return("lbl_Hallway1")
    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 450 ypos 100 focus_mask True action Return("lbl_House")
    #imagebutton auto "images/ui/doorbutton_%s.png"  xpos 400 ypos 300 focus_mask True action Return("lbl_Arcade")
    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 250 ypos 200 focus_mask True action Return("lbl_Park")
    #imagebutton auto "images/ui/doorbutton_%s.png"  xpos 500 ypos 500 focus_mask True action Return("lbl_Vending")
    
    #use Map_arrow("lbl_Classroom", rotate_N, 200,0)
    #use Map_arrow("lbl_Classroom", rotate_NE, 200,50)
    #use Map_arrow("lbl_Classroom", rotate_E, 200,100)
    #use Map_arrow("lbl_Classroom", rotate_SE, 200,150)
    #use Map_arrow("lbl_Classroom", rotate_S, 200,200)
    #use Map_arrow("lbl_Classroom", rotate_SW, 200,250)
    #use Map_arrow("lbl_Classroom", rotate_W, 200,300)
    #use Map_arrow("lbl_Classroom", rotate_NW, 200,350)
    
screen Map_MapButton:
    imagebutton auto "images/ui/mapbutton_%s.png"  xpos 0 ypos 0 focus_mask True action Return("lbl_ReturnToMap")
    imagebutton auto "images/ui/exitbutton_%s.png"  xpos 60 ypos 0 focus_mask True action Return("lbl_Continue")
 
#School locations
label lbl_Bathroom:
    show bg bathroom 
    "Just in time too. I've been holding it in this whole time."
    
    call screen Map_Bathroom
    #"Guess ill leave then."
    
    call expression _return from _call_expression
    
    return
    
label lbl_Classroom:
    show bg classroom 
    "Time to study"
    call screen Map_Classroom    
    #"Guess ill leave then."
    
    call expression _return from _call_expression
    
    return
    
label lbl_Hallway1:
    show bg hallway1 
    "Theres always this random girl just standing here..."
    call screen Map_Hallway1
    #"Guess ill leave then."
    
    call expression _return from _call_expression
    
    return
    
label lbl_Hallway2:
    show bg hallway2
    "Theres always this random dude just standing here..."
    call screen Map_Hallway2
    #"Guess ill leave then."
    
    call expression _return from _call_expression
    
    return
    
label lbl_Baseball:
    show bg baseball 
    "Im talking bassseeeeballl~"
    call screen Map_Baseball
    #"Guess ill leave then."
    
    call expression _return from _call_expression
    
    return

#House locations
label lbl_House:
    show bg house 
    "Home sweet home."
    call screen Map_House       
    call expression _return from _call_expression
    return
    
label lbl_Kitchen: 
    show bg kitchen 
    "Dinner time."
    call screen Map_Kitchen       
    call expression _return from _call_expression
    return
    
label lbl_Bedroom:
    show bg bedroom 
    "Sleepy tiem."
    call screen Map_Bedroom       
    call expression _return from _call_expression
    return
    
#Town locations    
label lbl_Arcade:  
    show bg arcades 
    "An Arcade. Pew pew!"
    call screen Map_Arcade        
    call expression _return from _call_expression
    return
    
label lbl_Park:
    show bg park 
    "Oh a Park!"
    call screen Map_Park        
    call expression _return from _call_expression
    return
    
label lbl_Street:
    show bg street 
    "Oh a Street!"
    call screen Map_Street       
    call expression _return from _call_expression
    return
    
label lbl_Vending:
    show bg vending 
    "Time for a treat?"  
    call screen Map_Vending        
    call expression _return from _call_expression  
    return    
    
    

#screen Map_Bathroom:
#    tag map_screen
#    #add im.Scale("images/bg/bathroom_%s.jpg"%TimeOfDay, 1366, 768)
#    add im.Scale("images/bg/bathroom.jpg", 1366, 768)
#    #add "images/bg/bathroom.jpg", 1366, 768)
#    use Map_MapButton
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 20 ypos 500 focus_mask True action Return("lbl_Hallway")
#    
#    
# 
#screen Map_Classroom:
#    tag map_screen
#    #add im.Scale("images/bg/Classroom_%s.jpg"%TimeOfDay, 1366, 768)
#    add im.Scale("images/bg/Classroom.jpg", 1366, 768)
#    use Map_MapButton
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 20 ypos 700 focus_mask True action Return("lbl_Hallway")
#    
#    
#screen Map_Hallway:
#    tag map_screen
#    #add im.Scale("images/bg/halyway1_%s.png"%TimeOfDay, 1366, 768)
#    add im.Scale("images/bg/hallway1.jpg", 1366, 768)
#    use Map_MapButton
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 20 ypos 600 focus_mask True action Return("lbl_Bathroom")
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 800 ypos 600 focus_mask True action Return("lbl_Classroom")
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 400 ypos 800 focus_mask True action Return("lbl_Park")
#    
#screen Map_Hallway2:
#    tag map_screen
#    #add im.Scale("images/bg/halyway1_%s.png"%TimeOfDay, 1366, 768)
#    add im.Scale("images/bg/hallway1.jpg", 1366, 768)
#    use Map_MapButton
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 20 ypos 600 focus_mask True action Return("lbl_Bathroom")
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 800 ypos 600 focus_mask True action Return("lbl_Classroom")
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 400 ypos 800 focus_mask True action Return("lbl_Park")
#    
#    
#screen Map_House:
#    tag map_screen
#    add im.Scale("images/bg/house.jpg", 1366, 768)
#    use Map_MapButton
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 800 ypos 600 focus_mask True action Return("lbl_Arcade")
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 400 ypos 800 focus_mask True action Return("lbl_Park")
#    
#    
#screen Map_Arcade:
#    tag map_screen
#    add im.Scale("images/bg/arcades.png", 1366, 768)
#    use Map_MapButton
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 800 ypos 600 focus_mask True action Return("lbl_Park")
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 400 ypos 800 focus_mask True action Return("lbl_House")
#    
#    
#screen Map_Park:
#    tag map_screen
#    add im.Scale("images/bg/park.jpg", 1366, 768)
#    #add im.Scale("images/bg/park background progress_%s.png"%TimeOfDay, 1366, 768)
#    use Map_MapButton
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 800 ypos 600 focus_mask True action Return("lbl_Hallway")
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 400 ypos 800 focus_mask True action Return("lbl_Vending")
#    
#    
#screen Map_Vending:
#    tag map_screen
#    add im.Scale("images/bg/icecream machines.png", 1366, 768)
#    use Map_MapButton
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 800 ypos 600 focus_mask True action Return("lbl_Arcade")
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 400 ypos 800 focus_mask True action Return("lbl_Park")
#    
#    
#screen Map_Baseball:
#    tag map_screen
#    add im.Scale("images/bg/icecream machines.png", 1366, 768)
#    use Map_MapButton
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 800 ypos 600 focus_mask True action Return("lbl_Arcade")
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 400 ypos 800 focus_mask True action Return("lbl_Park")
#    
#screen Map_Bedroom:
#    tag map_screen
#    add im.Scale("images/bg/icecream machines.png", 1366, 768)
#    use Map_MapButton
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 800 ypos 600 focus_mask True action Return("lbl_Arcade")
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 400 ypos 800 focus_mask True action Return("lbl_Park")
#    
#screen Map_Kitchen:
#    tag map_screen
#    add im.Scale("images/bg/icecream machines.png", 1366, 768)
#    use Map_MapButton
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 800 ypos 600 focus_mask True action Return("lbl_Arcade")
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 400 ypos 800 focus_mask True action Return("lbl_Park")
#    
#screen Map_Street:
#    tag map_screen
#    add im.Scale("images/bg/icecream machines.png", 1366, 768)
#    use Map_MapButton
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 800 ypos 600 focus_mask True action Return("lbl_Arcade")
#    imagebutton auto "images/ui/doorbutton_%s.png"  xpos 400 ypos 800 focus_mask True action Return("lbl_Park")
    
    ##############################################################
    
    

screen Map_Bathroom:
    tag map_screen
    add im.Scale("images/bg/bathroom.jpg", 1366, 768)
    use Map_MapButton
    #imagebutton auto "images/ui/map/arrow/E_%s.png"  xpos 20 ypos 500 focus_mask True action Return("lbl_Hallway2") #E
    use Map_arrow("lbl_Hallway2", rotate_E, 20,500)
    
 
screen Map_Classroom:
    tag map_screen
    add im.Scale("images/bg/Classroom.jpg", 1366, 768)
    use Map_MapButton
    #imagebutton auto "images/ui/map/arrow/E_%s.png"  xpos 1100 ypos 400 focus_mask True action Return("lbl_Hallway1") #E 
    use Map_arrow("lbl_Hallway1", rotate_E, 1100,400)  
    
    
screen Map_Hallway1:
    tag map_screen
    add im.Scale("images/bg/hallway1.jpg", 1366, 768)
    use Map_MapButton
    #imagebutton auto "images/ui/map/arrow/SW_%s.png"  xpos 100 ypos 200 focus_mask True action Return("lbl_Hallway2") #SW
    #imagebutton auto "images/ui/map/arrow/N_%s.png"  xpos 1150 ypos 300 focus_mask True action Return("lbl_Classroom") #N
    use Map_arrow("lbl_Hallway2", rotate_SW, 100,200)
    use Map_arrow("lbl_Classroom", rotate_N, 1150,300)
    
    
screen Map_Hallway2:
    tag map_screen
    add im.Scale("images/bg/hallway2.jpg", 1366, 768)
    use Map_MapButton
    #imagebutton auto "images/ui/map/arrow/N_%s.png"  xpos 500 ypos 400 focus_mask True action Return("lbl_Bathroom") #N
    #imagebutton auto "images/ui/map/arrow/W_%s.png"  xpos 300 ypos 400 focus_mask True action Return("lbl_Hallway1") #E / W
    #imagebutton auto "images/ui/map/arrow/S_%s.png"  xpos 800 ypos 600 focus_mask True action Return("lbl_Baseball") #S
    use Map_arrow("lbl_Bathroom", rotate_N, 500,400)
    use Map_arrow("lbl_Hallway1", rotate_W, 300,400)
    use Map_arrow("lbl_Baseball", rotate_S, 800,600)
    
    
screen Map_Baseball:
    tag map_screen
    add im.Scale("images/bg/baseball.jpg", 1366, 768)
    use Map_MapButton
    #imagebutton auto "images/ui/map/arrow/NE_%s.png"  xpos 1150 ypos 250 focus_mask True action Return("lbl_Hallway2") # NE
    #imagebutton auto "images/ui/map/arrow/S_%s.png"  xpos 400 ypos 550 focus_mask True action Return("lbl_Street") #S 
    use Map_arrow("lbl_Hallway2", rotate_NE, 1150,250)
    use Map_arrow("lbl_Street", rotate_S, 400,550)
    
    
screen Map_House:
    tag map_screen
    add im.Scale("images/bg/house.jpg", 1366, 768)
    use Map_MapButton
    #imagebutton auto "images/ui/map/arrow/NE_%s.png"  xpos 100 ypos 300 focus_mask True action Return("lbl_Kitchen") #NE
    #imagebutton auto "images/ui/map/arrow/E_%s.png"  xpos 800 ypos 400 focus_mask True action Return("lbl_Street") #E
    use Map_arrow("lbl_Kitchen", rotate_NE, 100,300)
    use Map_arrow("lbl_Street", rotate_E, 800,400)
    
    
    
screen Map_Bedroom:
    tag map_screen
    add im.Scale("images/bg/bedroom.jpg", 1366, 768)
    use Map_MapButton
    #imagebutton auto "images/ui/map/arrow/SE_%s.png"  xpos 1100 ypos 500 focus_mask True action Return("lbl_Kitchen") #SW
    use Map_arrow("lbl_Kitchen", rotate_E, 1100,500)
    
    
screen Map_Kitchen:
    tag map_screen
    add im.Scale("images/bg/kitchen.jpg", 1366, 768)
    use Map_MapButton
    #imagebutton auto "images/ui/map/arrow/S_%s.png"  xpos 500 ypos 500 focus_mask True action Return("lbl_House") #S
    #imagebutton auto "images/ui/map/arrow/NE_%s.png"  xpos 1200 ypos 300 focus_mask True action Return("lbl_Bedroom") #NE
    use Map_arrow("lbl_House", rotate_S, 500,500)
    use Map_arrow("lbl_Bedroom", rotate_NE, 1200,300)
    
    
screen Map_Street:
    tag map_screen
    add im.Scale("images/bg/street.jpg", 1366, 768)
    use Map_MapButton
    #imagebutton auto "images/ui/map/arrow/S_%s.png"  xpos 600 ypos 500 focus_mask True action Return("lbl_House") #S
    #imagebutton auto "images/ui/map/arrow/NE_%s.png"  xpos 900 ypos 300 focus_mask True action Return("lbl_Park") #NE
    #imagebutton auto "images/ui/map/arrow/SW_%s.png"  xpos 200 ypos 200 focus_mask True action Return("lbl_Baseball") #SW
    use Map_arrow("lbl_House", rotate_S, 600,500)
    use Map_arrow("lbl_Park", rotate_NE, 900,300)
    use Map_arrow("lbl_Baseball", rotate_SW, 200,200)
    
    
screen Map_Park:
    tag map_screen
    add im.Scale("images/bg/park.jpg", 1366, 768)
    use Map_MapButton
    #imagebutton auto "images/ui/map/arrow/SW_%s.png"  xpos 100 ypos 550 focus_mask True action Return("lbl_Street") #SW
    use Map_arrow("lbl_Street", rotate_SW, 100,550)