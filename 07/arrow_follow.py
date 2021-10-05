from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    global mx, my

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
mx, my = random.randint(0, KPU_WIDTH - 1), random.randint(0, KPU_HEIGHT - 1)
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    x = x + (mx - x) / 10
    y = y + (my - y) / 10
    if abs(mx - x) < 20:
        x = mx
    if abs(my - y) < 20:
        y = my

    if mx > x:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    arrow.draw(mx, my)
    update_canvas()
    frame = (frame + 1) % 8
    if mx == x and my == y:
        mx, my = random.randint(0, KPU_WIDTH - 1), random.randint(0, KPU_HEIGHT - 1)

    handle_events()
    delay(0.01)

close_canvas()


