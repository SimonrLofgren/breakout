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
                print(SETTINGS_OBJ.SCORE)
                SETTINGS_OBJ.change_SCORE(50)
                BRICKS_REMAINING = BRICKS_REMAINING - 1
            except:
                print("FEL")
        else:
            Brick.hit_minus(obj)
            print("-hit")
