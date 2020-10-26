import pygame

from Menu import the_loops
from config import *

'''class Menu_rect:
    def __init__(self, center_x, center_y, font, text, text_color, button_color):
        self.center_x = center_x
        self.center_y = center_y
        self. font = font
        self.text = text
        self.text_color = text_color
        self.button_color = button_color

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
'''

def main_menu(screen):
    click = False
    menu_choice = 0

    while the_loops.main_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                the_loops.quit()
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
                menu_choice = 1
                the_loops.set_main_menu(False)

############################ Player 2 ############################
        if 425 < mouse_x < 675 and 310 < mouse_y < 360:
            print("inside 2")
            if click:
                menu_choice = 2
                the_loops.set_main_menu(False)

############################ Highscore ############################
        if 250 < mouse_x < 550 and 410 < mouse_y < 460:
            print("inside high")
            if click:
                print("Click!!!")
                menu_choice = 3
                the_loops.set_main_menu(False)

############################ Easter BOING ############################
        """if 120 < mouse_x < 120 + 250 and 310 < mouse_y < 360:
            print("inside boing")
            if click:
                print("Click!!!")
                menu_choice = 4
                IN_START = False"""

        click = False
    return menu_choice