import pygame
from config import *
from classes.pwup_types import *
from classes.BRICKS_INDEX import *
from classes.Object.Brick import *
from Level import *

def imgtype(b):

    if b == 0:
        return YELLOW_B.convert_alpha()

    if b == 1:
        return RED_B.convert_alpha()

    if b == 2:
        return BLUE_B.convert_alpha()

    if b == 3:
        return GREEN_B.convert_alpha()

    if b == 4:
        return CYAN_B.convert_alpha()

    if b == 5:
        return MAGENTA_B.convert_alpha()

    if b == 6:
        return BRICKBRICK_B.convert_alpha()

    if b == 7:
        return STONE_B.convert_alpha()

    if b == 8:
        return GOLD_B.convert_alpha()

def pwuptype(b):

    if b == 0:
        pass

    if b == 1:
        pass

    if b == 2:
        pass

    if b == 3:
        pass

    if b == 4:
        pass

    if b == 5:
        pass

    if b == 6:
        pass

    if b == 7:
        pass

    if b == 8:
        pass

def new_level_bricks(screen):

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
    brick_pos_y = 20
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
                pwup = b[1]
                if ab > 5 and ab < 9:

                    if ab == 6:
                        hits = 1

                    elif ab == 7:
                        hits = 2

                    elif ab == 8:
                        hits = 3

                else:
                    hits = 0

                brick = Brick(brick_pos_x, brick_pos_y, SETTINGS_OBJ.BRICK_SIZE, BRICK_SIZE_Y, image, screen, True, False, pwup, hits)
                bricks.append(brick)
            brick_pos_x += 80
            b_no += 1

# list of bricks
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