
from Level.lvl_editor import new_level_bricks
from classes.Level import *
from config.settings_create import SETTINGS_OBJ


def init_lvl(screen):
    the_levels = []

# create object lvl with bricks and "bg"
    for i in range(SETTINGS_OBJ.NR_OF_LVL):

        lvl = Lvl(None, new_level_bricks(screen, i))
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