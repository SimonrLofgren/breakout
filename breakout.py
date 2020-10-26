from Menu.start_menu import main_menu
from app.run import run_ed2
from classes.Object.pwup import Pwup
from classes.pwup_types import pwup_activate, ballspeed_normal
from engine.pwup_control import Timer
from initialize import *
from time import sleep
from Level.lvls import *
from classes.Object.ball_img import Ball_img
from engine.collision_control import *
from config.settings_create import *
import random
from initialize.pwups_create import pwup_data_obj_create


def lvl_prompt(screen, lvl):
    screen.fill(BLACK)
    color = random.choice(colors)
    font = pygame.font.Font('freesansbold.ttf', 132)
    text = font.render("LEVEL "+str(lvl), True, color, BLACK)
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2)
    screen.blit(text, textRect)
    pygame.display.update()
    sleep(3)

def score_prompt(screen):


    font = pygame.font.Font('freesansbold.ttf', 52)
    text = font.render("CURRENT SCORE: " + str(SETTINGS_OBJ.SCORE), True, RED, BLACK)
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2)
    screen.blit(text, textRect)
    pygame.display.update()
    sleep(3)

def final_score_prompt(screen):

    screen.fill(BLACK)
    font = pygame.font.Font('freesansbold.ttf', 52)
    text = font.render("FINAL SCORE: " + str(SETTINGS_OBJ.SCORE), True, RED, BLACK)
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2)
    screen.blit(text, textRect)
    pygame.display.update()
    sleep(3)

def highscore_1(SCORE):
    path = '/Users/simon/PycharmProjects/pythonProject/Breakout/Highscore.txt'
    highscores_list = open(path, 'r+')
    high = highscores_list.read()
    highscores_list.write("\n" + str(SETTINGS_OBJ.SCORE))
    highscores_list.close()

def new_highscore_prompt(screen):
    screen.fill(BLACK)
    color = random.choice(colors)
    font = pygame.font.Font('freesansbold.ttf', 72)
    text1 = font.render("NEW HIGHSCORE!", True, RED, BLACK)
    text2 = font.render(str(SETTINGS_OBJ.SCORE), True, BLUE, BLACK)
    textRect1 = text1.get_rect()
    textRect2 = text2.get_rect()

    textRect1.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2 - 50)
    textRect2.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2 + 50)
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    pygame.display.update()
    sleep(2)

def highscore(screen):

    add_high = True
    with open("Highscore.txt", "r") as high:
        text = high.readlines()
        text_int = []
        for line in text:
            for n in line:
                if n.isdigit():
                    text_int.append(int(line))
        #print(text)
        #print(text_int)
        text_int.sort(reverse=True)
        print(text_int)
        #print(text)
        for line in text_int:
            if int(line) > SETTINGS_OBJ.SCORE:
                print(line)
                add_high = False
    if add_high:
        new_highscore_prompt(screen)
        with open("Highscore.txt", "a") as high:
            high.write("\n"+str(SETTINGS_OBJ.SCORE))
    else:
        final_score_prompt(screen)

def draw_heart(screen, hearts):
    for h in hearts:
        screen.blit(h.the_image, (h.x_pos, h.y_pos))

def keeping_score(screen):

    text = STANDARD_FONT.render("Score: "+str(SETTINGS_OBJ.SCORE), True, WHITE, BLACK)
    textRect = text.get_rect()
    textRect.center = (70, 20)
    screen.blit(text, textRect)

def fps_counter(screen, clock):
    fps = int(clock.get_fps())
    text = STANDARD_FONT.render("fps: "+str(fps), True, WHITE, BLACK)
    textRect = text.get_rect()
    textRect.center = (670, 20)
    screen.blit(text, textRect)

def run(the_levels, screen):



    running = True
    running_2 = True
    current_level = 0



    while running and running_2:
        
        # init start menu
        running_2 = main_menu(screen)
        # temp value
        #running_2 = True

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
        in_level = True   # Main arg

        while in_level and running_2:

            # input control
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    in_level = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                bounce_brick.x -= B_BRICK_SPEED
            if keys[pygame.K_RIGHT]:
                bounce_brick.x += B_BRICK_SPEED

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
                    except:
                        print("pwup went wrong")
                    # improved direction controll. still buggy
                    speed_fix(p, balls)
                    pwups.remove(p)

            ### RESTORE SPEED ###
            if speedtimer.pwup_timer():
                if SETTINGS_OBJ.FPS != 90:
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
                            in_level = False
                            #running = False

            ### Win ###
            if SETTINGS_OBJ.BRICKS_REMAINING <= 0:
                current_level += 1
                if PROMPTS:
                    score_prompt(screen)
                in_level = False

            # next level
            if SETTINGS_OBJ.BRICKS_REMAINING <= 0:
                in_level = False
                SETTINGS_OBJ.change_CURRENT_LVL()

            # game pace
            clock.tick(SETTINGS_OBJ.FPS)

def main():

    the_levels = init_lvl(screen)
    run(the_levels, screen)
    #run_ed2(the_levels, screen)

if __name__ == "__main__":
    main()
