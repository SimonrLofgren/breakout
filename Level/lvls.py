
from Level.lvl_editor import new_level_bricks
from classes.Level import *
from initialize.settings_create import SETTINGS_OBJ


def init_lvl(screen):
    """

    :param screen: default screen
    :return: return a list with all levels as objects
    """
    the_levels = []

    # create object lvl with bricks and "bg"
    for i in range(SETTINGS_OBJ.NR_OF_LVL):

        lvl = Lvl(None, new_level_bricks(screen, i))
        the_levels.append(lvl)

    return the_levels