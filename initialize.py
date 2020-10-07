import pygame
from settings import LIVES, SCREEN_WIDTH

class Heart:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    @property
    def x_pos(self):
        return self.x

    @property
    def y_pos(self):
        return self.y

    @property
    def the_image(self):
        return self.image

def create_red_hearts():
    red_hearts = []
    image = pygame.image.load('sprites/red_life_black_sm.png')
    x = SCREEN_WIDTH//2 - 50
    y = 5
    for l in range(LIVES):
        red_heart = Heart(x, y, image)
        red_hearts.append(red_heart)
        x += 40
    return red_hearts

def create_gray_hearts():
    gray_hearts = []
    image = pygame.image.load('sprites/gray_life_black_sm.png')
    x = SCREEN_WIDTH//2 - 50
    y = 5
    for l in range(LIVES):
        red_heart = Heart(x, y, image)
        gray_hearts.append(red_heart)
        x += 40
    return gray_hearts
