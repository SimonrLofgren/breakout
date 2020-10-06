import breakout
from lvl_editor import new_level
from settings import *

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
            obst = breakout.Rect(x, y, BRICK_SIZE_X, BRICK_SIZE_Y, color, screen, True, False)
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
            obst = breakout.Rect(x, y, BRICK_SIZE_X, BRICK_SIZE_Y, brick_color[l], screen, True, False)
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
                obst = breakout.Rect(x, y, BRICK_SIZE_X, BRICK_SIZE_Y, brick_color[col_value], screen, True, False)
                objects.append(obst)
                x += 80
                col_value = breakout.random.randrange(0, 4)
            list_of_lvls.append(objects)
    return list_of_lvls

def init_lvl(screen):
    new_level_1 = new_level(screen)
    list_of_levels = [lvl_1(screen), lvl_2(screen)]
    the_levels = []

    lvl = breakout.Lvl(None, new_level_1)
    the_levels.append(lvl)

    '''for l in range(len(list_of_levels)):
        lvl = breakout.Lvl(None, list_of_levels[l])
        the_levels.append(lvl)
    list_of_lvl = lvl_rand(screen, list_of_levels)
    for l in range(len(list_of_lvl)):
        lvl = breakout.Lvl(None, list_of_lvl[l])
        the_levels.append(lvl)'''

    return the_levels