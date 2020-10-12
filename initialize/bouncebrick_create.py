import pygame
from classes.Object.Bouncebrick import BounceBrick
from config import *




def create_bouncebrick(screen: pygame.Surface):
    bb_img = pygame.image.load("sprites/bouncebrick.png")
    bounce_brick = BounceBrick(100, 550, 100, 20, WHITE, screen, True, True, bb_img)
    return bounce_brick