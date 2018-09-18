from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def movePosition(_x,_y,x,y):
    frame = 0
    moveX = (_x - x) / 30
    moveY = (_y - y) / 30
    count = 0
    while (True):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += moveX
        y += moveY
        if(count ==30):
            break;
        count += 1
        delay(0.05)
        get_events()

while(True):
    movePosition(203 , 535,800//2,600//2)
    movePosition(132 , 243,203,535)


close_canvas()