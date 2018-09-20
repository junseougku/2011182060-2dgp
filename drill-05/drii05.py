from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

character.draw_now(203,535)
def move_position(_x,_y):
     px =203
     py = 535
    while(True):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now( px, py)
        px -=1
        py -=1
        delay(0.01)
        if(_x == px and _y == py):
            break;


while True:
    move_position(132,243);

close_canvas()