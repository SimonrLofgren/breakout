import pygame
from config import *
from breakout import bg_load, create_ball
from initialize.heart_create import create_red_hearts, create_gray_hearts
from config.settings_class import Settings


EMPTY = (0, 0, 0, 0)
pygame.init()
screen_bg = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
screen_brick = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT),  flags=pygame.SRCALPHA)
STANDARD_FONT = pygame.font.Font('freesansbold.ttf', 20)

bg = bg_load()
red_hearts = create_red_hearts()
gray_hearts = create_gray_hearts()
ball_image = create_ball()
PWUP_ADD_LIFE = pygame.image.load("sprites/pwups/lifeplus_pwup.png")
