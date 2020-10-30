import pygame
from config import *
from initialize.heart_create import create_red_hearts, create_gray_hearts


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT),  flags=pygame.SRCALPHA)
STANDARD_FONT = pygame.font.Font('freesansbold.ttf', 20)

bg = pygame.image.load("sprites/spaceBG_w_black.png").convert_alpha()
red_hearts = create_red_hearts()
gray_hearts = create_gray_hearts()
ball_image = pygame.image.load("sprites/balls/metalball_14_ro.png").convert_alpha()
pause_img = pygame.image.load("sprites/menu/pause1.png").convert_alpha()
pause_off_img = pygame.image.load("sprites/menu/pause_sound_off.png").convert_alpha()
pause_on_img = pygame.image.load("sprites/menu/pause_sound_on.png").convert_alpha()
easter_on = pygame.image.load("sprites/easter_on.png").convert_alpha()
easter_off = pygame.image.load("sprites/easter_off.png").convert_alpha()
clock = pygame.time.Clock()

