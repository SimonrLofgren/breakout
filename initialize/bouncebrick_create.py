import pygame
bb_img = "sprites/bouncebricks/bouncebrick.png"
bb_img_small = "sprites/bouncebricks/bouncebrick_SMALL.png"
bb_img_big = "sprites/bouncebricks/bouncebrick_BIG.png"


class Bb_sprites:
    def __init__(self):
        self.sprites = self.load_pwup_sprites()

    def ret_sprite(self, x):
        return self.sprites[x]

    def load_pwup_sprites(self):

        bb_sprites = [bb_img_small, bb_img, bb_img_big]

        return [pygame.image.load(img) for img in bb_sprites]


