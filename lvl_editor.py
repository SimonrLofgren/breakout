import pygame

from settings import *
from BRICKS_INDEX import *

YELLOW_B = pygame.image.load("bricks/YELLOW.png")
RED_B = pygame.image.load("bricks/RED.PNG")
BLUE_B = pygame.image.load("bricks/BLUE.png")
GREEN_B = pygame.image.load("bricks/GREEN.png")
CYAN_B = pygame.image.load("bricks/CYAN.png")
MAGENTA_B = pygame.image.load("bricks/MAGENTA.png")
BRICKBRICK_B = pygame.image.load("bricks/BRICKBRICK.png")
STONE_B = pygame.image.load("bricks/STONE.png")
GOLD_B = pygame.image.load("bricks/GOLD.png")

class Brick:
    def __init__(self, x, y, width, height, image, screen, is_bouncy, is_indestructable, pwup, hits):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.screen = screen
        self.is_indestructable = is_indestructable
        self.is_bouncy = is_bouncy
        self.pwup = pwup
        self.hits = hits

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

    def collide(self, other):
        if self.left >= other.right or other.left >= self.right:
            return False
        if self.top >= other.bottom or other.top >= self.bottom:
            return False
        return True

    def is_bouncy(self):
        if self.is_bouncy == True:
            return True
        else:
            return False

    def is_indestructable(self):
        if self.is_indestructable == True:
            return True
        else:
            return False

    def collide(self, other):
        if self.left >= other.right or other.left >= self.right:
            return False
        if self.top >= other.bottom or other.top >= self.bottom:
            return False
        return True

    def draw(self):
        screen = self.screen
        screen.blit(self.image, (self.x, self.y))

    def hit_count(self):
        return self.hits

    def hit_minus(self):
        self.hits -= 1
def imgtype(b):

    if b == 0:
        return YELLOW_B

    if b == 1:
        return RED_B

    if b == 2:
        return BLUE_B

    if b == 3:
        return GREEN_B

    if b == 4:
        return CYAN_B

    if b == 5:
        return MAGENTA_B

    if b == 6:
        return BRICKBRICK_B

    if b == 7:
        return STONE_B

    if b == 8:
        return GOLD_B


def pwuptype(b):
    pass


def new_level(screen):

    grid = [1, 1, 1, 0, 0, 0, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1,
            0, 0, 0, 1, 1, 1, 0, 0, 0,
            0, 0, 0, 1, 1, 1, 0, 0, 0,
            1, 1, 1, 0, 0, 0, 1, 1, 1,
            1, 1, 1, 0, 0, 0, 1, 1, 1]

    grid_t_f = [B0, B1, B2, B3, B4, B5, B6, B7, B8,
                B9, B10, B11, B12, B13, B14, B15, B16, B17,
                B18, B19, B20, B21, B22, B23, B24, B25, B26,
                B27, B28, B29, B30, B31, B32, B33, B34, B35,
                B36, B37, B38, B39, B40, B41, B42, B43, B44,
                B45, B46, B47, B48, B49, B50, B51, B52, B53]



    bricks = []
    pwups = []
    image = 0
    pwup = 0
    lines = 6
    brick_pos_y = 10
    b_no = 0
    hits = 0
    for l in range(lines):
        brick_pos_x = 50
        brick_pos_y += 30
        for line_no in range(9):
            b = grid_t_f[b_no]

            if b != None:
                image = imgtype(b[0])
                ab = b[0]
                if ab > 5 and ab < 9:

                    if ab == 6:
                        hits = 1

                    elif ab == 7:
                        hits = 2

                    elif ab == 8:
                        hits = 3

                else:
                    hits = 0
                if b[1] != 0:
                    pwup = pwuptype(b[1])


            brick = Brick(brick_pos_x, brick_pos_y, BRICK_SIZE_X, BRICK_SIZE_Y, image, screen, True, False, pwup, hits)
            bricks.append(brick)
            brick_pos_x += 80
            b_no += 1

    return bricks



    '''
    screen = lvl_screen
    y = 10
    lines = 6
    objects = []
    for l in range(lines):
        x = 50
        y += 30
        color = colors[l+1]
        for _ in range(9):
            obst = breakout.Rect(x, y, BRICK_SIZE_X, BRICK_SIZE_Y, color, screen, True, False)
            objects.append(obst)
            x += 80
    return objects'''