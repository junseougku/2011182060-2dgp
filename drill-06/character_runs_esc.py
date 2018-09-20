from pico2d import *


"""

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
"""

"""
def handle_events():
    global running
    global dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -=1
            elif event.key == SDLK_LEFT:
                dir += 1


running = True

x = 800//2
frame = 0
dir = 0



while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dir * 5
    delay(0.05)

close_canvas()
"""

KPU_WIDTH , KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH,KPU_HEIGHT)
grass = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mousePicture = load_image('hand_arrow.png')



running = True
frame = 0
px = KPU_WIDTH//2
py = KPU_HEIGHT//2
x = 0
y = 0
dir = 0
rot = 300

moveX_distance = 0
moveY_distance = 0

dest_X = 0
dest_Y = 0
count = 0
moveRe = False
def handle_events():
    global running
    global x,y
    global px,py
    global moveX_distance
    global moveY_distance
    global moveRe
    global dest_X
    global rot
    global  count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x,y = event.x , KPU_HEIGHT-1-event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            count = 0
            dest_X, dest_Y = event.x , KPU_HEIGHT - 1 - event.y - 150
            moveX_distance = (event.x - px) / 30
            moveY_distance = (KPU_HEIGHT - 1 - event.y - py) / 30
            moveRe = True
            if (px - dest_X > 0):
                rot = 0
            else:
                rot = 100

while running:

    clear_canvas()
    grass.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    character.clip_draw(frame * 100, rot, 100, 100, px, py)
    mousePicture.draw(x, y)
    update_canvas()
    handle_events()
    if(moveRe):
        px += moveX_distance
        py += moveY_distance
        count += 1
    if count== 30:
        moveRe = False
        count = 0
        if rot == 100:
            rot = 300
        elif rot == 0:
            rot = 200
    frame = (frame + 1) % 8
    x += dir * 5
    delay(0.05)

close_canvas()