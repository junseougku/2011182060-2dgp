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
character = load_image('run_animation.png')

running = True
frame = 0
x = 800//2
dir = 0
def handle_events():
    global running
    global x,y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x,y = event.x , KPU_HEIGHT-1-event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



while running:

    clear_canvas()
    grass.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dir * 5
    delay(0.05)

close_canvas()