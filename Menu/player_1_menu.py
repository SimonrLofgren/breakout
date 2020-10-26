import pygame

from Menu import the_loops
from config import BLACK, SCREEN_WIDTH, SCREEN_HIGHT


def player_1_menu(screen):
    click = False
    the_loops.set_p1_menu(True)
    while the_loops.p1_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                the_loops.quit()
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
                return 0
############################ main menu ############################
        if 180 < mouse_x < 620 and 400 < mouse_y < 500:
            print("inside 2")
            if click:
                return 1


        click = False