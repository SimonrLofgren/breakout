import random
from time import sleep

import pygame

from config import BLACK, colors, SCREEN_WIDTH, SCREEN_HIGHT, RED, WHITE, BLUE
from initialize.settings_create import SETTINGS_OBJ
from initialize import STANDARD_FONT


def lvl_prompt(screen, lvl):
    screen.fill(BLACK)
    color = random.choice(colors)
    font = pygame.font.Font('freesansbold.ttf', 132)
    text = font.render("LEVEL "+str(lvl), True, color, BLACK)
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2)
    screen.blit(text, textRect)
    pygame.display.update()
    sleep(3)

def score_prompt(screen):


    font = pygame.font.Font('freesansbold.ttf', 52)
    text = font.render("CURRENT SCORE: " + str(SETTINGS_OBJ.SCORE), True, RED, BLACK)
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2)
    screen.blit(text, textRect)
    pygame.display.update()
    sleep(3)

def final_score_prompt(screen):

    screen.fill(BLACK)
    font = pygame.font.Font('freesansbold.ttf', 52)
    text = font.render("FINAL SCORE: " + str(SETTINGS_OBJ.SCORE), True, RED, BLACK)
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2)
    screen.blit(text, textRect)
    pygame.display.update()
    sleep(3)

def highscore_1(SCORE):
    path = '/Users/simon/PycharmProjects/pythonProject/Breakout/Highscore_txt.txt'
    highscores_list = open(path, 'r+')
    high = highscores_list.read()
    highscores_list.write("\n" + str(SETTINGS_OBJ.SCORE))
    highscores_list.close()

def new_highscore_prompt(screen):
    screen.fill(BLACK)
    color = random.choice(colors)
    font = pygame.font.Font('freesansbold.ttf', 72)
    text1 = font.render("NEW HIGHSCORE!", True, RED, BLACK)
    text2 = font.render(str(SETTINGS_OBJ.SCORE), True, BLUE, BLACK)
    textRect1 = text1.get_rect()
    textRect2 = text2.get_rect()

    textRect1.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2 - 50)
    textRect2.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2 + 50)
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    pygame.display.update()
    sleep(2)

def highscore(screen):

    add_high = True
    with open("./app/highscore/Highscore_txt.txt", "r") as high:
        text = high.readlines()
        text_int = []
        for line in text:
            for n in line:
                if n.isdigit():
                    text_int.append(int(line))
        #print(text)
        #print(text_int)
        text_int.sort(reverse=True)
        print(text_int)
        #print(text)
        for line in text_int:
            if int(line) > SETTINGS_OBJ.SCORE:
                print(line)
                add_high = False
    if add_high:
        new_highscore_prompt(screen)
        with open("Highscore_txt.txt", "a") as high:
            high.write("\n"+str(SETTINGS_OBJ.SCORE))
    else:
        final_score_prompt(screen)

def draw_heart(screen, hearts):
    for h in hearts:
        screen.blit(h.the_image, (h.x_pos, h.y_pos))

def keeping_score(screen):

    text = STANDARD_FONT.render("Score: "+str(SETTINGS_OBJ.SCORE), True, WHITE, BLACK)
    textRect = text.get_rect()
    textRect.center = (70, 20)
    screen.blit(text, textRect)

def fps_counter(screen, clock):
    fps = int(clock.get_fps())
    text = STANDARD_FONT.render("fps: "+str(fps), True, WHITE, BLACK)
    textRect = text.get_rect()
    textRect.center = (670, 20)
    screen.blit(text, textRect)

def out_of_levels(screen):
    screen.fill(BLACK)
    font = pygame.font.Font('freesansbold.ttf', 72)
    text = font.render("Out of levels!!!", True, RED, BLACK)
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2)
    screen.blit(text, textRect)
    pygame.display.update()
    sleep(3)