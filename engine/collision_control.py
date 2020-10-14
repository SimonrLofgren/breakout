from classes.Object.Brick import *
from classes.Object.Bouncebrick import *
from config.settings_create import SETTINGS_OBJ
from config import *


'''
def pwup_tracker(pwup,bb):

########### check x axis ###########
    if bb.collide(pwup):
        if bb.top <= pwup.bottom <= bb.top + DIFFICULTY:
            print("pwup hit")
'''


def collision_pos(ball, br, bricks_on_screen, pwup_t_or_f_obj):
    if br.collide(ball):
        if br.left <= ball.right <= br.left + SETTINGS_OBJ.DIFFICULTY:
            ball.x_step = -SETTINGS_OBJ.DIFFICULTY
            hit(br, bricks_on_screen, pwup_t_or_f_obj)

        if br.right >= ball.left >= br.right - SETTINGS_OBJ.DIFFICULTY:
            ball.x_step = SETTINGS_OBJ.DIFFICULTY
            hit(br, bricks_on_screen, pwup_t_or_f_obj)

        if br.top <= ball.bottom <= br.top + SETTINGS_OBJ.DIFFICULTY:
            ball.y_step = -SETTINGS_OBJ.DIFFICULTY
            hit(br, bricks_on_screen, pwup_t_or_f_obj)

        if br.bottom >= ball.top >= br.bottom - SETTINGS_OBJ.DIFFICULTY:
            ball.y_step = SETTINGS_OBJ.DIFFICULTY
            hit(br, bricks_on_screen, pwup_t_or_f_obj)

def speed_fix(p, balls):
    try:
        value = p.pwup_type
    except:
        value = 5
    if 4 <= value <= 6:
        for b in balls:
            if b.x_step != SETTINGS_OBJ.DIFFICULTY or b.x_step != -SETTINGS_OBJ.DIFFICULTY:
                if b.x_step < 0:
                    b.x_step = -SETTINGS_OBJ.DIFFICULTY
                else:
                    b.x_step = SETTINGS_OBJ.DIFFICULTY

            if b.y_step != SETTINGS_OBJ.DIFFICULTY or b.y_step != -SETTINGS_OBJ.DIFFICULTY:
                if b.y_step < 0:
                    b.y_step = -SETTINGS_OBJ.DIFFICULTY
                else:
                    b.y_step = SETTINGS_OBJ.DIFFICULTY


def bouncebrick_hit(ball, BounceBrick):
    global FPS

    if BounceBrick.collide(ball):

        #left hit
        if BounceBrick.left <= ball.right <= BounceBrick.left + SETTINGS_OBJ.DIFFICULTY:
            ball.x_step = -SETTINGS_OBJ.DIFFICULTY

        #right hit
        if BounceBrick.right >= ball.left >= BounceBrick.right - SETTINGS_OBJ.DIFFICULTY:
            ball.x_step = SETTINGS_OBJ.DIFFICULTY

################################## top hit ######################################

        if BounceBrick.top <= ball.bottom <= BounceBrick.top + SETTINGS_OBJ.DIFFICULTY:
            ball.y_step = -SETTINGS_OBJ.DIFFICULTY
            if BounceBrick.left + (BounceBrick.width // 3) <= ball.mid <= BounceBrick.right - (BounceBrick.width // 3):
                ball.x_step = 0
                #FPS = FPS_HIGH_SPEED
            elif BounceBrick.left + BounceBrick.width // 2 < ball.mid:
                ball.x_step = SETTINGS_OBJ.DIFFICULTY
                #FPS = FPS_ORG
            else:
                ball.x_step = -SETTINGS_OBJ.DIFFICULTY
                #FPS = FPS_ORG
        if BounceBrick.bottom >= ball.top >= BounceBrick.bottom - SETTINGS_OBJ.DIFFICULTY:
            ball.y_step = SETTINGS_OBJ.DIFFICULTY

def hit(obj, objects, pwup_t_or_f_obj):
    if not Object.is_indestructable(obj):
        global BRICKS_REMAINING

        if Brick.hit_count(obj) == 0:
            try:
                pwup_t_or_f_obj.set(True, Brick.pwup_return(obj), obj.x, obj.y)
                objects.remove(obj)
                SETTINGS_OBJ.change_SCORE(50)
                SETTINGS_OBJ.change_BRICKS_REMAINING(SETTINGS_OBJ.BRICKS_REMAINING - 1)
            except:
                print("FEL")
        else:
            Brick.hit_minus(obj)
            print("-hit")

def remove_ball(ball, balls):

    balls.remove(ball)
    SETTINGS_OBJ.change_NO_OF_BALLS(-1)
