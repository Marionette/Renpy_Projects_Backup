init:
    image background_image = "images/forest11.png"
    image midground_image = "images/Tree.png"
    image sprite1 = "images/finalMonster2.png"
    image sprite2 = "images/laneoBoy.png"
    
  


init 800 python:
    class MouseParallax(renpy.Displayable):
        def __init__(self,layer_info):
            super(renpy.Displayable,self).__init__()
            self.xoffset,self.yoffset=0.0,0.0
            self.sort_layer=sorted(layer_info,reverse=True)
            cflayer=[]
            masteryet=False
            for m,n in self.sort_layer:
                if(not masteryet)and(m<41):
                    cflayer.append("master")
                    masteryet=True
                cflayer.append(n)
            if not masteryet:
                cflayer.append("master")
            cflayer.extend(["transient","screens","overlay"])
            config.layers=cflayer
            config.overlay_functions.append(self.overlay)
            return
        def render(self,width,height,st,at):
            return renpy.Render(width,height)
        def parallax(self,m):
            func = renpy.curry(trans)(disp=self, m=m)
            return Transform(function=func)
        def overlay(self):
            ui.add(self)
            for m,n in self.sort_layer:
                renpy.layer_at_list([self.parallax(m)],n)
            return
        def event(self,ev,x,y,st):
            import pygame
            if ev.type==pygame.MOUSEMOTION:
                self.xoffset,self.yoffset=((float)(x)/(config.screen_width))-0.5,((float)(y)/(config.screen_height))-0.5
            return
    MouseParallax([(40,"farback"),(20,"back"),(-20,"front"),(-40,"inyourface")])
            
    def trans(d, st, at, disp=None, m=None):
        d.xoffset, d.yoffset = int(round(m*disp.xoffset)), int(round(m*disp.yoffset))
        return 0
        

        
label lbl_parallax_test:
    show background_image onlayer farback
    show midground_image onlayer back
    show sprite1 onlayer front
    show sprite2 onlayer inyourface
    
    "this is the test."
    "1"
    "2"
    "3"
    "4"
    "5"
    "end."
    hide background_image 
    hide midground_image 
    hide sprite1 
    hide sprite2 
    return