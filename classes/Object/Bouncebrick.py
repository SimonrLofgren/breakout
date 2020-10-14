
from classes.Object import Object
from config.settings_create import SETTINGS_OBJ
from initialize.bouncebrick_create import Bb_sprites


class BounceBrick(Object):
    def __init__(self, x, y, width, height, screen, is_bouncy, is_indestructable, bb_image, type):
        super().__init__(x, y, screen, is_bouncy, is_indestructable)
        self.width = width
        self.height = height
        self.bb_image = bb_image
        self.type_no = type

    @property
    def top(self):
        return self.y

    @property
    def bottom(self):
        return self.y + self.height

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self.width

    @property
    def type(self):
        return self.type_no

    def collide(self, other):
        if self.left >= other.right or other.left >= self.right:
            return False
        if self.top >= other.bottom or other.top >= self.bottom:
            return False
        return True


    def draw(self):
        self.screen.blit(self.bb_image, (self.x, self.y))

    def ai(self, ball_x):
        self.x = ball_x

    @staticmethod
    def create_bouncebrick(screen, x):

        bounce_brick = BounceBrick(100, 550, SETTINGS_OBJ.BRICK_SIZE, 20, screen,
                                   True, True, Bb_sprites().ret_sprite(x), SETTINGS_OBJ.BRICK_TYPE)

        return bounce_brick