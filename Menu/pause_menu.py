import pygame

from Menu import the_loops
from initialize import pause_img, pause_on_img, pause_off_img
from initialize.settings_create import SETTINGS_OBJ

def pause_menu(screen):
    the_loops.set_in_pause(True)
    if SETTINGS_OBJ.SOUND:
        screen.blit(pause_on_img, (275, 100))
    else:
        screen.blit(pause_off_img, (275, 100))
    #pygame.draw.rect(screen, WHITE, [290, 420, 70, 20])
                                    #x, y, width, height

    while the_loops.in_pause:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                the_loops.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p or event.key == pygame.K_PAUSE:
                    the_loops.set_in_pause(False)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        ############################ Sound on/off ############################
        if 335 < mouse_x < 335 + 130 and 200 < mouse_y < 250:
            if click:
                if SETTINGS_OBJ.SOUND:
                    SETTINGS_OBJ.SOUND_OFF()
                    screen.blit(pause_off_img, (275, 100))
                    pygame.mixer.music.set_volume(0.0)
                else:
                    SETTINGS_OBJ.SOUND_ON()
                    screen.blit(pause_on_img, (275, 100))
                    pygame.mixer.music.set_volume(1.0)

        ############################ Main menu ############################
        if 290 < mouse_x < 290 + 150 and 370 < mouse_y < 390:
            if click:
                the_loops.set_running(False)
                the_loops.set_in_level(False)
                the_loops.set_in_pause(False)
                the_loops.set_main_menu(True)

        ############################ Quit ############################
        if 290 < mouse_x < 290 + 150 and 420 < mouse_y < 440:
            if click:
                the_loops.quit()


        pygame.display.update()