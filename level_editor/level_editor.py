import pygame

from Menu import the_loops
from classes.Level import Lvl
from config import BLACK
from initialize import bg


def editor(the_levels, screen):
    in_editor = True

    active_level = 0
    while in_editor:
        bricks_on_screen = Lvl.return_bricks(the_levels[active_level])
        display_bricks = True
        while display_bricks:

            screen.fill(BLACK)
            screen.blit(bg, (0, 0))

            for br in bricks_on_screen:
                br.draw()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    the_loops.quit()
                    in_editor = False
                    display_bricks = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        active_level = 0
                        display_bricks = False

                    if event.key == pygame.K_1:
                        active_level = 1
                        display_bricks = False

                    if event.key == pygame.K_2:
                        active_level = 2
                        display_bricks = False

                    if event.key == pygame.K_3:
                        active_level = 3
                        display_bricks = False

                    if event.key == pygame.K_4:
                        active_level = 4
                        display_bricks = False

                    if event.key == pygame.K_5:
                        active_level = 5
                        display_bricks = False

                    if event.key == pygame.K_6:
                        active_level = 6
                        display_bricks = False

                    if event.key == pygame.K_l:
                        active_level = int(input("choose lvl: "))
                        display_bricks = False

                    if event.key == pygame.K_BACKSPACE:
                        display_bricks = False
                        in_editor = False