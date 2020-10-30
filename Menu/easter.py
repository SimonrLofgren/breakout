import pygame

from Menu import the_loops
from initialize import easter_on, easter_off
from initialize.settings_create import SETTINGS_OBJ

def easter(screen):
    the_loops.set_in_easter(True)
    if SETTINGS_OBJ.CHEATS:
        screen.blit(easter_on, (0, 0))
    else:
        screen.blit(easter_off, (0, 0))
    #pygame.draw.rect(screen, WHITE, [290, 420, 70, 20])
                                    #x, y, width, height

    while the_loops.in_easter:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                the_loops.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mouse_x, mouse_y = pygame.mouse.get_pos()

        ############################ Sound on/off ############################
        if 260 < mouse_x < 260 + 250 and 380 < mouse_y < 440:
            print("cheats")
            if click:
                if SETTINGS_OBJ.DEATH:
                    SETTINGS_OBJ.set_DEATH(False)
                    SETTINGS_OBJ.set_CHEATS(True)
                    screen.blit(easter_on, (0, 0))

                else:
                    SETTINGS_OBJ.set_DEATH(True)
                    SETTINGS_OBJ.set_CHEATS(False)
                    screen.blit(easter_off, (0, 0))

        if 0 < mouse_x < 0 + 130 and 550 < mouse_y < 600:
            print("in main")
            if click:
                the_loops.set_main_menu(True)
                the_loops.set_in_easter(False)

        pygame.display.update()