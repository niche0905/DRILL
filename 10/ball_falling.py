from pico2d import *
import random

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

class Ball:
    def __init__(self):
        if random.randint(0, 1) == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

        self.x, self.y = random.randint(0,800), 599
        self.velocity = random.randint(3,9)

    def update(self):
        if self.y > 50:
            self.y -= self.velocity
        if self.y < 50:
            self.y = 50

    def draw(self):
        self.image.draw(self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = 0, 90
        self.frame = random.randint(0, 7)
        self.velocity = random.randint(10, 20)

    def update(self):
        self.x += self.velocity
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(100 * self.frame, 0, 100, 100, self.x, self.y)

open_canvas(800, 600)
running = True
grass = Grass()
boys = [Boy() for n in range(11)]
balls = [Ball() for n in range(20)]

while running:
    handle_events()

    for boy in boys:
        boy.update()
    for ball in balls:
        ball.update()

    clear_canvas()
    grass.draw()
    for boy in boys:
        boy.draw()
    for ball in balls:
        ball.draw()

    update_canvas()

    delay(0.05)