import pygame
import random
from settings import *
from time import sleep


#STANDARD_FONT = pygame.font.SysFont('impact.ttf', 50)

class Menu_rect:
    def __init__(self, center_x, center_y, font, text, text_color, button_color):
        self.center_x = center_x
        self.center_y = center_y
        self. font = font
        self.text = text
        self.text_color = text_color
        self.button_color = button_color



    '''def create(self):
        self.font = pygame.font.SysFont(self.font, self.font_size)
        self.text = self.font.render(self.text, True, self.text_color, self.button_color)
        textRect = self.text.get_rect()
        textRect.center = self.x, self.y'''

    def render(self):
        self.render = self.font.render(self.text, True, self.text_color, self.button_color)
        return self.render


    def rect(self):
        self.rect = self.render.get_rect(center=(self.x, self.y))
        return self.rect


    def center(self):
        self.rect.center = (self.center_x, self.center_y)


    def text(self):
        return self.text


    def textRect(self):
        return self.textRect


    def x(self):
        return self.x


    def y(self):
        return self.y


    def font(self):
        return self.font


    def font_size(self):
        return self.font_size


    def text_color(self):
        return self.text_color


    def button_color(self):
        return self.button_color


def start_menu(screen):
    click = False
    global IN_START
    IN_START = True
    while IN_START:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                IN_START = False
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.fill(BLACK)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        p1 = pygame.image.load('sprites/menu/1player.png')
        p2 = pygame.image.load('sprites/menu/2player.png')
        high = pygame.image.load('sprites/menu/highscores.png')
        boing = pygame.image.load('sprites/menu/boing.png')

        screen.blit(p1, (120, 300))
        screen.blit(p2, (430, 301))
        screen.blit(high, (SCREEN_WIDTH//2 -150, SCREEN_HIGHT//2 + 100))
        screen.blit(boing, (40, SCREEN_HIGHT//2 - 300))
        pygame.display.update()

############################ Player 1 ############################
        if 120 < mouse_x < 120 + 250 and 310 < mouse_y < 360:
            print("inside 1")
            if click:
                p1_menu(screen)
############################ Player 2 ############################
        if 425 < mouse_x < 675 and 310 < mouse_y < 360:
            print("inside 2")
            if click:
                print("Click!!!")
                quiter = ""
                return quiter
############################ Highscore ############################
        if 250 < mouse_x < 550 and 410 < mouse_y < 460:
            print("inside high")
            if click:
                print("Click!!!")

############################ Easter BOING ############################
        if 120 < mouse_x < 120 + 250 and 310 < mouse_y < 360:
            print("inside boing")
            if click:
                print("Click!!!")


        click = False
    return True

def p1_menu(screen):
    global IN_START
    click = False
    IN_P1 = True
    while IN_P1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                IN_P1 = False
                IN_START = False
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.fill(BLACK)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        new_game = pygame.image.load('sprites/menu/new_game.png')
        main = pygame.image.load('sprites/menu/main.png')

        new_game_rect = new_game.get_rect()
        main_rect = main.get_rect()

        new_game_rect.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2 - 150)
        main_rect.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2 + 150)

        screen.blit(new_game, new_game_rect)
        screen.blit(main, main_rect)

        pygame.display.update()

############################ new game ############################
        if 200 < mouse_x < 600 and 100 < mouse_y < 200:
            print("inside 1")
            if click:
                IN_P1 = False
                IN_START = False
############################ main menu ############################
        if 180 < mouse_x < 620 and 400 < mouse_y < 500:
            print("inside 2")
            if click:
                IN_P1 = False


        click = False

def start_prompt(screen):
    click = False
    IN_START = True
    while IN_START:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                IN_START = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        text_center_x_2 = SCREEN_WIDTH//2 - 120
        text_center_y_2 = SCREEN_HIGHT//2 + 20

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
        textRect2.center = (text_center_x_2, text_center_y_2)
        textRect3.center = (SCREEN_WIDTH//2 + 120, SCREEN_HIGHT//2 + 20)
        textRect4.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2 + 100)




        #text_menu = Menu_rect(100, 100, 'impact.ttf', 50, "Testing", BLUE, WHITE)

        '''font_test = pygame.font.SysFont('impact.ttf', 50)
        button = Menu_rect(200, 200, font_test, "TEST2", CYAN, WHITE)
        t = button.render()
        r = button.rect()
        screen.blit(t, r)'''



        ''' center_x, center_y, font, font_size,
                 text, text_color, button_color'''
        #button1 = Menu_rect.create(text_menu)


        screen.blit(text1, textRect1)
        screen.blit(text2, textRect2)
        screen.blit(text3, textRect3)
        screen.blit(text4, textRect4)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        # print(mouse_x)
        # print(mouse_y)
        if text_center_x_2 - 75 < mouse_x < text_center_x_2 + 75 and text_center_y_2 - 25 < mouse_y < text_center_y_2 + 25:
            print("inside")
            if click:
                print("Click!!!")
        if text_center_x_2 - 75 < mouse_x < text_center_x_2 + 75 and text_center_y_2 - 25 < mouse_y < text_center_y_2 + 25:
            print("inside")
            if click:
                print("Click!!!")



        '''
                         Head
                   1 player  2player
                       Highscores
        '''
        click = False
        pygame.display.update()

def continues(continues):
    return continues