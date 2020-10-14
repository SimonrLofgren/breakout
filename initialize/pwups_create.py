import pygame
from engine.pwup_control import Pwup_data

PWUP_ADD_LIFE_img = "sprites/pwups/lifeplus_pwup.png"
PWUP_BALL_ADD_img = "sprites/pwups/ballplus_pwup.png"


class Pwup_sprites:
    def __init__(self):
        self.sprites = self.load_pwup_sprites()


    def ret_sprite(self, x):
        return self.sprites[x]


    def load_pwup_sprites(self):

        pwup_sprites = [PWUP_ADD_LIFE_img, PWUP_BALL_ADD_img]
        return [pygame.image.load(img) for img in pwup_sprites]



def pwup_data_obj_create():
    pwup_data_obj = Pwup_data(False, 0, 0, 0)
    return pwup_data_obj