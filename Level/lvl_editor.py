import pygame

from Level.lvl_1 import lvl_1_grid
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

def new_level_bricks(screen, i):

    grid = [1, 1, 1, 0, 0, 0, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1,
            0, 0, 0, 1, 1, 1, 0, 0, 0,
            0, 0, 0, 1, 1, 1, 0, 0, 0,
            1, 1, 1, 0, 0, 0, 1, 1, 1,
            1, 1, 1, 0, 0, 0, 1, 1, 1]



    lvl_list = [lvl_0_grid, lvl_1_grid]

    bricks = []
    pwups = []
    image = 0
    pwup = 0
    lines = 6
    brick_pos_y = 20
    b_no = 0
    hits = 0
    SETTINGS_OBJ.change_NR_OF_LVL(len(lvl_list))
    active_lvl = lvl_list[i]
    for l in range(lines):
        brick_pos_x = 50
        brick_pos_y += 30
        for line_no in range(9):
            b = active_lvl[b_no]

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