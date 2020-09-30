import pygame
import random
from settings import *
from time import sleep


def start_prompt(screen):
    IN_START = True
    while IN_START:
        screen.fill(BLACK)
        font1 = pygame.font.SysFont('impact.ttf', 100)
        font2 = pygame.font.SysFont('impact.ttf', 60)
        font3 = pygame.font.SysFont('impact.ttf', 50)

        text1 = font1.render("BALL GOES BOING", True, GREEN_DARK, BLACK)
        text2 = font2.render("1 Player ", True, BLUE_MELLOW, BLACK)
        text3 = font2.render("2 Player ", True, RED_MELLOW, BLACK)
        text4 = font3.render("Highscores ", True, BLACK, GOLD)

        textRect1 = text1.get_rect()
        textRect2 = text2.get_rect()
        textRect3 = text3.get_rect()
        textRect4 = text4.get_rect()

        textRect1.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2 - 100)
        textRect2.center = (SCREEN_WIDTH//2 - 120, SCREEN_HIGHT//2 + 20)
        textRect3.center = (SCREEN_WIDTH//2 + 120, SCREEN_HIGHT//2 + 20)
        textRect4.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2 + 100)

        screen.blit(text1, textRect1)
        screen.blit(text2, textRect2)
        screen.blit(text3, textRect3)
        screen.blit(text4, textRect4)

        '''
                         Head
                   1 player  2player
                       Highscores
        '''
        pygame.display.update()