from time import sleep
import pygame

from Menu import the_loops
from Menu.pause_menu import pause_menu
from prompts.prompts import lvl_prompt, draw_heart, fps_counter, keeping_score, highscore, score_prompt, out_of_levels
from classes.Level import Lvl
from classes.Object.Bouncebrick import BounceBrick
from classes.Object.Brick import Brick
from classes.Object.ball_img import Ball_img
from classes.Object.pwup import Pwup
from classes.pwup_types import pwup_activate, ballspeed_normal
from config import PROMPTS, B_BRICK_SPEED, BLACK, DEATH, SCREEN_WIDTH
from initialize.settings_create import SETTINGS_OBJ
from engine.collision_control import collision_pos, bouncebrick_hit, speed_fix, remove_ball
from engine.pwup_control import Timer
from initialize import bg, gray_hearts, red_hearts, clock
from initialize.pwups_create import pwup_data_obj_create
from sounds import sound_pwup_hit


def run_the_game(the_levels, screen):
    the_loops.set_running(True)
    current_level = 0

    while the_loops.running:

        # from the_levels[(active level)] unpack list from object to new list.
        bricks_on_screen = Lvl.return_bricks(the_levels[SETTINGS_OBJ.CURRENT_LVL])

        # checks if all bricks are gone.
        SETTINGS_OBJ.change_BRICKS_REMAINING(len(bricks_on_screen))

        # prompts on or off in SETTINGS
        if PROMPTS:
            lvl_prompt(screen, current_level + 1)

        # create start ball
        balls = []

        balls.append(Ball_img.create_ball(SETTINGS_OBJ, screen))

        # create bouncebrick
        bounce_brick = BounceBrick.create_bouncebrick(screen, SETTINGS_OBJ.BRICK_TYPE)

        # a False pwup object
        pwup_data_obj = pwup_data_obj_create()

        # a list of active pwups
        pwups = []

        # pwup timer
        speedtimer = Timer(0, 1200)

        ############### in game loop ###############
        the_loops.set_in_level(True)
        while the_loops.in_level:

            # input control
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    the_loops.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p or event.key == pygame.K_PAUSE:
                        pause_menu(screen)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                if not bounce_brick.x <= -10:
                    bounce_brick.x -= SETTINGS_OBJ.B_BRICK_SPEED
            if keys[pygame.K_RIGHT]:
                if not bounce_brick.x >= SCREEN_WIDTH + 10:
                    bounce_brick.x += SETTINGS_OBJ.B_BRICK_SPEED


                #TODO timer

            # clear screen
            screen.fill(BLACK)

            ### Draw and Move phase ###

            # Draw Background
            screen.blit(bg, (0, 0))

            # Bouncebrick
            if SETTINGS_OBJ.BRICK_TYPE != bounce_brick.type:
                bounce_brick = BounceBrick.create_bouncebrick(screen, SETTINGS_OBJ.BRICK_TYPE)
            bounce_brick.draw()

            # hearts
            draw_heart(screen, gray_hearts)
            for h in range(SETTINGS_OBJ.LIVES):
                red_hearts[h].draw(screen)

            # FPS counter on screen
            fps_counter(screen, clock)

            # multiple balls
            SETTINGS_OBJ.change_NO_OF_BALLS()
            if SETTINGS_OBJ.NO_OF_BALLS > len(balls):
                balls.append(Ball_img.create_ball(SETTINGS_OBJ, screen))

            # draw balls
            for b in balls:
                b.Draw()
                b.Move()

            # draw bricks
            for br in bricks_on_screen:
                br.draw()
                # Check if ball collide
                for ball in balls:
                    if Brick.is_bouncy(br):
                        collision_pos(ball, br, bricks_on_screen, pwup_data_obj)

            # check if ball collide withe bouncebrick
            for ball in balls:
                bouncebrick_hit(ball, bounce_brick)


            ### pwups ###
            # if brick has pwup
            if pwup_data_obj.go:
                pwups.append(Pwup.pwup_create(screen, pwup_data_obj))
                pwup_data_obj.set(False, 0, 0, 0)
            # draw pwups
            for p in pwups:
                p.draw_pwup()
                p.move()

                # check if pwup collide with bouncebrick
                if bounce_brick.collide(p):
                    try:
                        pwup_activate(p.pwup_type)
                        if SETTINGS_OBJ.SOUND:
                            sound_pwup_hit()
                    except:
                        print("pwup went wrong")
                    # improved direction controll. still buggy
                    speed_fix(p, balls)
                    pwups.remove(p)

            ### RESTORE SPEED ###
            if speedtimer.pwup_timer():
                if SETTINGS_OBJ.FPS != 110:
                    ballspeed_normal()
                    speed_fix(5, balls)

            # score prompt
            keeping_score(screen)

            pygame.display.update()


            ### Game over ###

            if DEATH:
                for ball in balls:
                    if Ball_img.dead(ball):
                        remove_ball(ball, balls)
                        if SETTINGS_OBJ.NO_OF_BALLS <=0:
                            SETTINGS_OBJ.change_LIVES(-1)
                            SETTINGS_OBJ.change_NO_OF_BALLS(1)
                            sleep(1)


                        if SETTINGS_OBJ.LIVES == 0:
                            highscore(screen)
                            the_loops.set_in_level(False)

                            #running = False

            ### Win ###
            if SETTINGS_OBJ.BRICKS_REMAINING <= 0:
                current_level += 1
                if PROMPTS:
                    score_prompt(screen)
                the_loops.set_in_level(False)

            # next level
            if SETTINGS_OBJ.BRICKS_REMAINING <= 0:
                the_loops.set_in_level(False)
                SETTINGS_OBJ.change_CURRENT_LVL()

            if SETTINGS_OBJ.CURRENT_LVL > SETTINGS_OBJ.NR_OF_LVL - 1:
                out_of_levels(screen)
                the_loops.set_running(False)
                the_loops.set_main_menu(True)
                SETTINGS_OBJ.reset_CURRENT_LVL()

            # game pace
            clock.tick(SETTINGS_OBJ.FPS)