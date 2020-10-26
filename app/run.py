import pygame
from Menu.start_menu import main_menu, p1_menu
from config.Looper import Looper


def run_ed2(the_levels, screen):
    the_loops = Looper(True, True, True, True,)
    while the_loops.main_menu:
        menu_choice = main_menu(screen)
        if menu_choice == 1:
            choice = p1_menu(screen)
            if choice == 0:
                the_loops.set_main_menu(False)
            if choice == 1:
                break

        elif menu_choice == 2:
            pass
        elif menu_choice == 3:
            pass
        elif menu_choice == 4:
            pass
    print("Success")