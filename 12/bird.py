import random
from pico2d import *
import game_world
import game_framework
import boy

# 큰 새 평균 35~70 인치
# 50인치는 약 1.27m
# 새 속도 다양하게 분포
# 대략적인 평균 125 km/h 로 가정

BIRD_PIXEL_SIZE = 1.27 * boy.PIXEL_PER_METER
BIRD_SPEED_KMPH = 125
BIRD_SPEED_MPH = BIRD_SPEED_KMPH * 1000
BIRD_SPEED_MPM = BIRD_SPEED_MPH / 60
BIRD_SPEED_MPS = BIRD_SPEED_MPM / 60
BIRD_SPEED_PPS = BIRD_SPEED_MPS * boy.PIXEL_PER_METER

# 벌새 날개짓 횟수 초당 90회
BIRD_ACTION_PER_SEC = 90.0 / 1

LEFT = 0
RIGHT = 1

class Bird:
    image = None
    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.x, self.y = random.randint(0, 800), random.randint(300, 600)
        self.frame = random.randint(0, 14)
        self.dir = random.randint(0, 2)

    def update(self):
        if self.dir == LEFT:
            self.x -= BIRD_SPEED_PPS * game_framework.frame_time
            if self.x < 10:
                self.dir = RIGHT
                self.x = 10
        else:
            self.x += BIRD_SPEED_PPS * game_framework.frame_time
            if self.x > 1600 - 10:
                self.dir = LEFT
                self.x = 1600 - 10

        self.frame = (self.frame + 14 * BIRD_ACTION_PER_SEC * game_framework.frame_time) % 14

    def draw(self):
        if self.dir == LEFT:
            Bird.image.clip_composite_draw(int(self.frame * 100), 0, 100, 100, 0, 'h', self.x, self.y, BIRD_PIXEL_SIZE, BIRD_PIXEL_SIZE)
        else:
            Bird.image.clip_draw(int(self.frame * 100), 0, 100, 100, self.x, self.y, BIRD_PIXEL_SIZE, BIRD_PIXEL_SIZE)