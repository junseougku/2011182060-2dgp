from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def movePosition(_x,_y,now_x,now_y):
    frame = 0
    moveX_distance = (_x - now_x) / 30
    moveY_distance = (_y - now_y) / 30
    count = 0
    rot = 0
    if(now_x - _x >0) :
        rot = 0
    else :
        rot = 100
    while (True):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, rot, 100, 100, now_x, now_y)
        update_canvas()
        frame = (frame + 1) % 8
        now_x += moveX_distance
        now_y += moveY_distance
        if(count ==30):
            break;
        count += 1
        delay(0.05)
        get_events()

while(True):
    movePosition(203 , 535,712,349)
    movePosition(132 , 243,203,535)
    movePosition(535,470,132,243)
    movePosition(477,203,535,470)
    movePosition(715,136,477,203)
    movePosition(316,225,715,136)
    movePosition(510,92,316,225)
    movePosition(692,518,510,92)
    movePosition(682,336,692,518)
    movePosition(712,349,682,336)



close_canvas()