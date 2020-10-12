import breakout
from Level.lvl_editor import new_level_bricks
from config import *
from classes.Level import *


def init_lvl(screen):
    the_levels = []

    # list of bricks for new level
    new_level_1 = new_level_bricks(screen)

    #list_of_levels = [lvl_1(screen), lvl_2(screen)]

# create object lvl with bricks and "bg"
    lvl = Lvl(None, new_level_1)

    the_levels.append(lvl)

    '''for l in range(len(list_of_levels)):
        lvl = breakout.Lvl(None, list_of_levels[l])
        the_levels.append(lvl)
    list_of_lvl = lvl_rand(screen, list_of_levels)
    for l in range(len(list_of_lvl)):
        lvl = breakout.Lvl(None, list_of_lvl[l])
        the_levels.append(lvl)
'''
    # return a list with all levels
    return the_levels