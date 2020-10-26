from Level.lvls import init_lvl
from Menu import the_loops
from Menu.player_1_menu import player_1_menu
from Menu.start_menu import main_menu
from app.the_game import run_the_game
from engine.reset import reset_game
from initialize import screen
from level_editor.level_editor import editor
from sounds import play_soundtrack

#the_levels = init_lvl(screen)

def run_ed2():
    play_soundtrack()
    while the_loops.main_menu:
        menu_choice = main_menu(screen)
        if menu_choice == 1:
            choice = player_1_menu(screen)
            if choice == 0:
                the_levels = init_lvl(screen)
                reset_game()
                run_the_game(the_levels, screen)
            if choice == 1:
                pass

        elif menu_choice == 2:
            reset_game()
            the_levels = init_lvl(screen)
            editor(the_levels, screen)
            the_loops.set_main_menu(True)

        elif menu_choice == 3:
            pass
        elif menu_choice == 4:
            pass