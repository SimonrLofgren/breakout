import pygame





class Pwup_sprites:
    def __init__(self):
        self.sprites = self.load_pwup_sprites()


    def ret_sprite(self, x):
        return self.sprites[x]


    def load_pwup_sprites(self):

        pwup_sprites = [PWUP_ADD_LIFE_img, PWUP_BALL_ADD_img]
        return [pygame.image.load(img) for img in pwup_sprites]
