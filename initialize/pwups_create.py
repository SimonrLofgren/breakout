import pygame
from classes.Object.pwup import Pwup
from engine.pwup_control import Pwup_data



PWUP_ADD_LIFE_img = pygame.image.load("sprites/pwups/lifeplus_pwup.png")

def pwup_create(screen, pwup_data_obj):
    type = pwup_data_obj.no
    y_speed = 1
    ######################## Add life ########################
    if type == 0:
        pwup = Pwup(pwup_data_obj.x, pwup_data_obj.y, y_speed, 0, PWUP_ADD_LIFE_img, 30, screen)



    return pwup



def pwup_data_obj_create():
    pwup_data_obj = Pwup_data(False, 0, 0, 0)
    return pwup_data_obj