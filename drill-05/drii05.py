from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while True:
    make_rectangle()
    make_circle()

close_canvas()