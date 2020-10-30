from config import STANDARD_TIMER_DUR
from initialize.settings_create import SETTINGS_OBJ


################################ pw ups ################################


def pwup_activate(x):
    if x == 0 or x == 6:
        pass

    if x == 1:
        ball_add()

    if x == 2:
        bricksize_big()

    if x == 3:
        bricksize_small()

    if x == 4:
        SETTINGS_OBJ.set_TIMER(STANDARD_TIMER_DUR)
        ballspeed_fast()

    if x == 5:
        SETTINGS_OBJ.set_TIMER(STANDARD_TIMER_DUR)
        ballspeed_slow()

    if x == 7:
        flameball()
        SETTINGS_OBJ.set_TIMER(10)

    if x == 8:
        undead()
        SETTINGS_OBJ.set_TIMER(20)

    if x == 9:
        dead()

    if x == 10:
        life_up()






def life_up():

    if SETTINGS_OBJ.LIVES <= 2:
        SETTINGS_OBJ.change_LIVES(1)

def ball_add():

    SETTINGS_OBJ.change_NO_OF_BALLS(1)

def bricksize_big():
    SETTINGS_OBJ.change_BRICK_TYPE(1)

def bricksize_small():
    SETTINGS_OBJ.change_BRICK_TYPE(-1)

def ballspeed_fast():
    SETTINGS_OBJ.change_DIFFICULTY(3)
    SETTINGS_OBJ.change_FPS(120)

def ballspeed_slow():
    SETTINGS_OBJ.change_DIFFICULTY(2)
    SETTINGS_OBJ.change_FPS(90)

def ballspeed_normal():
    SETTINGS_OBJ.change_DIFFICULTY(2)
    SETTINGS_OBJ.change_FPS(110)

def flameball():
    pass

def undead():
    SETTINGS_OBJ.set_DEATH(False)
def dead():
    SETTINGS_OBJ.change_LIVES(-1)

def bricksize_normal():
    SETTINGS_OBJ.change_BRICK_TYPE(0)

