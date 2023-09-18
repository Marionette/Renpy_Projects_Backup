
transform testbubble:
    xalign .8
    yanchor .5
    ypos (bubble_ybase+400)
    alpha 0.0
    on show:
        ypos (bubble_ybase+400)
    on hide:
        pause bubble_delay
        parallel:
            linear 1.0 alpha 1.0
            pause 1.0
            linear 1.0 alpha 0.0 
        parallel:
            linear 3.0 ypos (bubble_ybase-10)
            
init python:
    bubble_ybase = 0
    bubblenum = 0
    
    def bubble_ybase_tick():
        global bubble_ybase
        bubble_ybase -= 50
        
    def bubble(s,bg,delay=0.001):
        if persistent.hide_feedback:
            return
        global bubblenum
        bubbles = 'bubble'+str(bubblenum)
        w = ui.window(background=Frame(bg,16,16),xminimum=200,yminimum=33,xfill=False,xmaximum=900,left_padding=20,right_padding=20)
        w.add(ui.text(s,xmaximum=800,color='#000',xalign=.5))
        ui.remove(w)
        global bubble_delay
        bubble_delay = delay
        renpy.show(bubbles,what=w,at_list=[testbubble,])
        renpy.hide(bubbles)
        bubblenum += 1
        
    def show_test(caption, val, invert=False, delay=0.001, partial=None):
        s = 'Test: '+caption+u' ? '
        if invert ^ val:
            res_s = 'Success'
        elif partial:
            res_s = 'Partial Success'
        else:
            res_s = 'Failed'
        s = _(u'Test: %(caption)s -> %(result)s')%dict(caption=_(caption),result=_(res_s))
        
        bg = ((invert ^ val) and 'ui/indicators/bubble-success.png') or 'ui/indicators/bubble-fail.png'
        bubble(s,bg,delay=delay)
        return val