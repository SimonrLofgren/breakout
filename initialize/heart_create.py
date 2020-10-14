import pygame

from classes.Heart import Heart
from config import *

image_red = pygame.image.load('sprites/red_life_black_sm.png')
image_gray = pygame.image.load('sprites/gray_life_black_sm.png')

def create_red_hearts():
    red_hearts = []
    x = SCREEN_WIDTH//2 - 50
    y = 5
    for l in range(LIVES):
        red_heart = Heart(x, y, image_red)
        red_hearts.append(red_heart)
        x += 40
    return red_hearts

def create_gray_hearts():
    gray_hearts = []
    x = SCREEN_WIDTH//2 - 50
    y = 5
    for l in range(LIVES):
        red_heart = Heart(x, y, image_gray)
        gray_hearts.append(red_heart)
        x += 40
    return gray_hearts
