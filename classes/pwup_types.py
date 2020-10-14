from config.settings_create import SETTINGS_OBJ


################################ pw ups ################################


def pwup_activate(x):
    if x == 0:
        life_up()

    if x == 1:
        pass

    if x == 2:
        pass

    if x == 3:
        pass

    if x == 4:
        pass

    if x == 5:
        pass

    if x == 6:
        pass







def life_up():

    if SETTINGS_OBJ.LIVES <= 2:
        SETTINGS_OBJ.change_LIVES(1)

def ball_add():
    global NO_OF_BALLS
    NO_OF_BALLS += 1

def bricksize_big():
    pass

def bricksize_small():
    pass

def ballspeed_fast():
    pass

def ballspeed_slow():
    pass

def flameball():
    pass

def undead():
    pass