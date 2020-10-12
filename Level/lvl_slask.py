import random

from Level.lvl_editor import Brick
from classes.Object.ball import Ball
from config import *


def create_random_obj(colors, objects, screen):
    for _ in range(10):
        x = random.randrange(10, SCREEN_WIDTH-40)
        y = random.randrange(10, SCREEN_HIGHT-200)
        x_step = random.choice([-3, -2, -1, 1, 2, 3])
        y_step = random.choice([-3, -2, -1, 1, 2, 3])
        color = random.choice(colors)
        radius = random.choice([10, 15, 20])
        screen = screen
        ball = Ball(x, y, x_step, y_step, color, radius, screen, False, True)
        obst = Brick(x, y, 70, 20, color, screen, True, False)
        objects.append(obst)
        #balls.append(ball)
    return objects

def create_level_obj(lvl_screen):
    x = 50
    y = 0
    lines = 5
    objects = []
    for l in range(lines):
        x = 50
        y += 30
        for _ in range(9):
            color = RED
            screen = lvl_screen
            obst = Brick(x, y, 70, 20, color, screen, True, False)
            objects.append(obst)
            x += 80
        #balls.append(ball)
    return objects

def lvl_test(lvl_screen):
    screen = lvl_screen
    y = 0
    lines = 1
    objects = []
    for l in range(lines):
        x = 200
        y += 30
        color = colors[l+1]
        for _ in range(1):
            obst = breakout.Rect(x, y, BRICK_SIZE_X, BRICK_SIZE_Y, color, screen, True, False)
            objects.append(obst)
            x += 80
    return objects

def lvl_1(lvl_screen):
    screen = lvl_screen
    y = 10
    lines = 6
    objects = []
    for l in range(lines):
        x = 50
        y += 30
        color = colors[l+1]
        for _ in range(9):
            obst = Rect(x, y, BRICK_SIZE_X, BRICK_SIZE_Y, color, screen, True, False)
            objects.append(obst)
            x += 80
    return objects

def lvl_2(lvl_screen):
    screen = lvl_screen
    y = 10
    lines = 4
    brick_color = [RED, RED, BLUE, BLUE]
    objects = []
    for l in range(lines):
        x = 50
        y += 30
        for _ in range(9):
            obst = Rect(x, y, BRICK_SIZE_X, BRICK_SIZE_Y, brick_color[l], screen, True, False)
            objects.append(obst)
            x += 80
    return objects

def lvl_rand(lvl_screen, list_of_lvls):
    for l in range(NR_OF_LVL):
        screen = lvl_screen
        y = 10
        lines = 6
        colors = [RED, GREEN, BLUE, MAGENTA, CYAN]
        brick_color = []
        objects = []
        for i in range(lines):
            color = breakout.random.choice(colors)
            brick_color.append(color)

        for z in range(lines):
            x = 50
            y += 30
            col_value = 0
            for _ in range(breakout.random.randrange(7, 9)):
                obst = Rect(x, y, BRICK_SIZE_X, BRICK_SIZE_Y, brick_color[col_value], screen, True, False)
                objects.append(obst)
                x += 80
                col_value = breakout.random.randrange(0, 4)
            list_of_lvls.append(objects)
    return list_of_lvls