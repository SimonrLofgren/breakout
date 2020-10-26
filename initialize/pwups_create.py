import pygame
from engine.pwup_control import Pwup_data

PWUP_ADD_LIFE_img = "sprites/pwups/lifeplus_pwup.png"
PWUP_BALL_ADD_img = "sprites/pwups/ballplus_pwup.png"
PWUP_BRICK_PLUS =  "sprites/pwups/big_brick_pwup.png"
PWUP_BRICK_MINUS =  "sprites/pwups/small_brick_pwup.png"
PWUP_BALL_FAST =  "sprites/pwups/turbo.png"
PWUP_BALL_SLOW =  "sprites/pwups/slowmo.png"
PWUP_BALL_FLAME =  "sprites/pwups/flame_ball.png"
PWUP_UNDEAD =  "sprites/pwups/undead.png"
PWUP_DEATH =  "sprites/pwups/death.png"

class Pwup_sprites:
    def __init__(self):
        self.sprites = self.load_pwup_sprites()


    def ret_sprite(self, x):
        return self.sprites[x]


    def load_pwup_sprites(self):

        pwup_sprites = [PWUP_ADD_LIFE_img, PWUP_BALL_ADD_img, PWUP_BRICK_PLUS, PWUP_BRICK_MINUS,
                        PWUP_BALL_FAST, PWUP_BALL_SLOW, PWUP_BALL_FLAME, PWUP_UNDEAD, PWUP_DEATH]

        return [pygame.image.load(img) for img in pwup_sprites]



def pwup_data_obj_create():
    """

    :return: Returns a pwup object.
    """
    pwup_data_obj = Pwup_data(False, 0, 0, 0)
    return pwup_data_obj