import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball
from bird import Bird

name = "MainState"

boy = None
grass = None
balls = []
big_balls = []
b1 = None
b2 = None
b3 = None
b4 = None
b5 = None


def collide(a, b):
    # fill here
    return True




def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    # fill here for balls
    global b1, b2, b3, b4, b5
    b1 = Bird()
    b2 = Bird()
    b3 = Bird()
    b4 = Bird()
    b5 = Bird()



def exit():
    game_world.clear()

    global b1, b2, b3, b4, b5
    del(b1)
    del(b2)
    del(b3)
    del(b4)
    del(b5)

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    b1.update()
    b2.update()
    b3.update()
    b4.update()
    b5.update()
    # fill here for collision check



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    b1.draw()
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    update_canvas()






