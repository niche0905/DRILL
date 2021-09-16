from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# fill here
import math

x=400
y=90
degree=270

def fill_screen():
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    

while True:
    
    while x<750:
        fill_screen()
        x+=2
        delay(0.01)

    while y<550:
        fill_screen()
        delay(0.01)
        y+=2
        
    while x>50:
        fill_screen()
        delay(0.01)
        x-=2

    while y>90:
        fill_screen()
        delay(0.01)
        y-=2

    while x<400:
        fill_screen()
        x+=2
        delay(0.01)

    while degree<360:
        fill_screen()
        delay(0.01)
        x=math.cos(degree/180*math.pi)*350+400
        y=math.sin(degree/180*math.pi)*230+320
        degree+=2

    degree=0

    while degree<270:
        fill_screen()
        delay(0.01)
        x=math.cos(degree/180*math.pi)*350+400
        y=math.sin(degree/180*math.pi)*230+320
        degree+=1


close_canvas()
