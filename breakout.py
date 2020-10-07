import pygame
import random
from time import sleep
from initialize import create_red_hearts, create_gray_hearts
from lvl_editor import Brick
from lvls import *
from settings import *
from start_menu import start_menu

class Object:
    def __init__(self, x, y, color, screen, is_bouncy, is_indestructable):
        self.x = x
        self.y = y
        self.color = color
        self.screen = screen
        self.is_indestructable = is_indestructable
        self.is_bouncy = is_bouncy

    def is_bouncy(self):
        if self.is_bouncy == True:
            return True
        else:
            return False
    def is_indestructable(self):
        if self.is_indestructable == True:
            return True
        else:
            return False

class Ball(Object):
    def __init__(self, x, y, x_step, y_step, color, radius, screen, is_bouncy, is_indestructable):
        super().__init__(x, y, color, screen, is_bouncy, is_indestructable)
        self.x_step = x_step
        self.y_step = y_step
        self.radius = radius

        ######Ball hit box######
    @property
    def top(self):
        return self.y - self.radius

    @property
    def bottom(self):
        return self.y + self.radius

    @property
    def side_bottom(self):
        return self.x + self.radius

    @property
    def left(self):
        return self.x - self.radius

    @property
    def right(self):
        return self.x + self.radius
    @property
    def mid(self):
        return self.x + self.radius // 2

    def Move(self):
        self.x += self.x_step * 1
        self.y += self.y_step * 1

        if not self.radius <= self.x <= SCREEN_WIDTH - self.radius:
            self.x_step *= -1

        if not self.radius <= self.y <= SCREEN_HIGHT - self.radius:
            self.y_step *= -1

    def Draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def Reset(self):
        self.x = random.randrange(200, 400)
        self.y = random.randrange(200, 400)

    def show_next_hit(self):
        shadow_x = self.x
        shadow_y = self.y

        no_hit = True
        while no_hit:
            shadow_x += self.x_step
            shadow_y += self.y_step

            if not self.radius <= shadow_x <= SCREEN_WIDTH - self.radius:
                no_hit = False

            if not self.radius <= shadow_y <= SCREEN_HIGHT - self.radius:
                no_hit = False

        pygame.draw.circle(self.screen, WHITE, (shadow_x, shadow_y), self.radius, 2)

    ###prel death

    def dead(self):
        if self.y > SCREEN_HIGHT - self.radius:
            return True

class Ball_img(Object):
    def __init__(self, x, y, x_step, y_step, color, ball_image, radius, screen, is_bouncy, is_indestructable):
        super().__init__(x, y, color, screen, is_bouncy, is_indestructable)
        self.x_step = x_step
        self.y_step = y_step
        self.radius = radius
        self.ball_image = ball_image

        ######Ball hit box######
    @property
    def top(self):
        return self.y - self.radius

    @property
    def bottom(self):
        return self.y + self.radius

    @property
    def side_bottom(self):
        return self.x + self.radius

    @property
    def left(self):
        return self.x - self.radius

    @property
    def right(self):
        return self.x + self.radius
    @property
    def mid(self):
        return self.x + self.radius // 2

    def Move(self):
        self.x += self.x_step * 1
        self.y += self.y_step * 1

        if not self.radius <= self.x <= SCREEN_WIDTH - self.radius:
            self.x_step *= -1

        if not self.radius <= self.y <= SCREEN_HIGHT - self.radius:
            self.y_step *= -1

    def Draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
        self.screen.blit(self.ball_image, (self.x-7, self.y-7))
    def Reset(self):
        self.x = random.randrange(200, 400)
        self.y = random.randrange(200, 400)

    def show_next_hit(self):
        shadow_x = self.x
        shadow_y = self.y

        no_hit = True
        while no_hit:
            shadow_x += self.x_step
            shadow_y += self.y_step

            if not self.radius <= shadow_x <= SCREEN_WIDTH - self.radius:
                no_hit = False

            if not self.radius <= shadow_y <= SCREEN_HIGHT - self.radius:
                no_hit = False

        pygame.draw.circle(self.screen, WHITE, (shadow_x, shadow_y), self.radius, 2)

    ###prel death

    def dead(self):
        if self.y > SCREEN_HIGHT - self.radius:
            return True


class Rect(Object):
    def __init__(self, x, y, width, height, color, screen, is_bouncy, is_indestructable):
        super().__init__(x, y, color, screen, is_bouncy, is_indestructable)
        self.width = width
        self.height = height

    @property
    def top(self):
        return self.y

    @property
    def bottom(self):
        return self.y + self.height

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self.width

    def collide(self, other):
        if self.left >= other.right or other.left >= self.right:
            return False
        if self.top >= other.bottom or other.top >= self.bottom:
            return False
        return True

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

class BounceBrick(Rect):
    def __init__(self, x, y, width, height, color, screen, is_bouncy, is_indestructable, bb_image):
        super().__init__(x, y, width, height, color, screen, is_bouncy, is_indestructable)
        self.bb_image = bb_image

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        self.screen.blit(self.bb_image, (self.x, self.y))

class Lvl:
    def __init__(self, bg_color, bricks):

        self.bg_color = bg_color
        self.bricks = bricks

    def return_bricks(self):
        return self.bricks

    def return_bg_color(self):
        return self.bg_color

def create_bouncebrick(screen):
    bb_img = pygame.image.load("sprites/bouncebrick.png")
    bounce_brick = BounceBrick(100, 550, 100, 20, WHITE, screen, True, True, bb_img)
    return bounce_brick

def create_random_obj(colors, objects, screen):
    for _ in range(10):
        x = random.randrange(10, SCREEN_WIDTH-40)
        y = random.randrange(10, SCREEN_HIGHT-200)
        x_step = random.choice([-3, -2, -1, 1, 2, 3])
        y_step = random.choice([-3, -2, -1, 1, 2, 3])
        color = random.choice(colors)
        radius = random.choice([10, 15, 20])
        screen = screen
        ball = Ball(x, y, x_step, y_step, color, radius, screen, False, True)
        obst = Rect(x, y, 70, 20, color, screen, True, False)
        objects.append(obst)
        #balls.append(ball)
    return objects

def create_level_obj(lvl_screen):
    x = 50
    y = 0
    lines = 5
    objects = []
    for l in range(lines):
        x = 50
        y += 30
        for _ in range(9):
            color = RED
            screen = lvl_screen
            obst = Rect(x, y, 70, 20, color, screen, True, False)
            objects.append(obst)
            x += 80
        #balls.append(ball)
    return objects

def if_is_bouncy(ball, obj, objects):
    if obj.collide(ball):
        if obj.left <= ball.right <= obj.left + DIFFICULTY:
            ball.x_step = -DIFFICULTY
            return hit(obj, objects)
        if obj.right >= ball.left >= obj.right - DIFFICULTY:
            ball.x_step = DIFFICULTY
            return hit(obj, objects)
        if obj.top <= ball.bottom <= obj.top + DIFFICULTY:
            ball.y_step = -DIFFICULTY
            return hit(obj, objects)
        if obj.bottom >= ball.top >= obj.bottom - DIFFICULTY:
            ball.y_step = DIFFICULTY
            return hit(obj, objects)

def determine_angle(angle_1, b):

    if angle_1 <= 2:
        b.x_step = 0
        angle_1 += 1
        return angle_1
    else:
        b.x_step = DIFFICULTY
        angle_1 = 0
        return angle_1

def special_if_is_bouncy(ball, BounceBrick, objects):
    global FPS

    if BounceBrick.collide(ball):

        #left hit
        if BounceBrick.left <= ball.right <= BounceBrick.left + DIFFICULTY:
            ball.x_step = -DIFFICULTY

        #right hit
        if BounceBrick.right >= ball.left >= BounceBrick.right - DIFFICULTY:
            ball.x_step = DIFFICULTY

################################## top hit ######################################

        if BounceBrick.top <= ball.bottom <= BounceBrick.top + DIFFICULTY:
            ball.y_step = -DIFFICULTY
            if BounceBrick.left + (BounceBrick.width // 3) <= ball.mid <= BounceBrick.right - (BounceBrick.width // 3):
                ball.x_step = 0
                FPS = FPS_HIGH_SPEED
            elif BounceBrick.left + BounceBrick.width // 2 < ball.mid:
                ball.x_step = DIFFICULTY
                FPS = FPS_ORG
            else:
                ball.x_step = -DIFFICULTY
                FPS = FPS_ORG
        if BounceBrick.bottom >= ball.top >= BounceBrick.bottom - DIFFICULTY:
            ball.y_step = DIFFICULTY

def hit(obj, objects):
    if not Object.is_indestructable(obj):
        global SCORE
        global BRICKS_REMAINING
        if Brick.hit_count(obj) == 0:
            try:
                objects.remove(obj)

                SCORE += 50
                BRICKS_REMAINING = BRICKS_REMAINING - 1
            except:
                print("FEL")
        else:
            Brick.hit_minus(obj)

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

    screen.fill(BLACK)
    font = pygame.font.Font('freesansbold.ttf', 52)
    text = font.render("CURRENT SCORE: " + str(SCORE), True, RED, BLACK)
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2)
    screen.blit(text, textRect)
    pygame.display.update()
    sleep(3)

def final_score_prompt(screen):

    screen.fill(BLACK)
    font = pygame.font.Font('freesansbold.ttf', 52)
    text = font.render("FINAL SCORE: " + str(SCORE), True, RED, BLACK)
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2)
    screen.blit(text, textRect)
    pygame.display.update()
    sleep(3)

def game_intro(screen, clock):
    intro = True
    text_objects = []
    while intro:
        '''for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()'''

        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf = "A bit Racey"
        TextRect = largeText
        TextRect.center = ((SCREEN_WIDTH / 2), (SCREEN_HIGHT / 2))
        screen.blit(TextSurf, TextRect)



        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf = smallText
        textRect = "GO!"
        textRect.center = ((150 + (100 / 2)), (450 + (50 / 2)))
        screen.blit(textSurf, textRect)
        pygame.draw.rect(screen, RED, (550, 450, 100, 50))

        pygame.display.update()
        clock.tick(15)

def highscore_1(SCORE):
    path = '/Users/simon/PycharmProjects/pythonProject/Breakout/Highscore.txt'
    highscores_list = open(path, 'r+')
    high = highscores_list.read()
    highscores_list.write("\n" + str(SCORE))
    highscores_list.close()

def new_highscore_prompt(screen):
    screen.fill(BLACK)
    color = random.choice(colors)
    font = pygame.font.Font('freesansbold.ttf', 72)
    text1 = font.render("NEW HIGHSCORE!", True, RED, BLACK)
    text2 = font.render(str(SCORE), True, BLUE, BLACK)
    textRect1 = text1.get_rect()
    textRect2 = text2.get_rect()

    textRect1.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2 - 50)
    textRect2.center = (SCREEN_WIDTH//2, SCREEN_HIGHT//2 + 50)
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    pygame.display.update()
    sleep(2)

def highscore(SCORE, screen):

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
            if int(line) > SCORE:
                print(line)
                add_high = False
    if add_high:
        new_highscore_prompt(screen)
        with open("Highscore.txt", "a") as high:
            high.write("\n"+str(SCORE))
    else:
        final_score_prompt(screen)

def draw_heart(screen, hearts):
    for h in hearts:
        screen.blit(h.the_image, (h.x_pos, h.y_pos))

def lose_life(balls):
    for b in balls:
        b.Reset()

def draw_bg(screen, bg):
    screen.blit(bg, (0, 0))

def bg_load():
    bg = pygame.image.load("sprites/spaceBG_w_black.png")
    return bg


def create_ball():
    return pygame.image.load("sprites/balls/metalball_14_ro.png")

def run(the_levels, screen):

    pygame.init()
    clock = pygame.time.Clock()
    #game_intro(screen, clock)
    running = True
    global DIFFICULTY
    global BRICKS_REMAINING
    global SCORE
    global LIVES
    current_level = 0
    DIFFICULTY += current_level + 1
    SCORE = 0
    gtfo = True
    bg = bg_load()
    red_hearts = create_red_hearts()
    gray_hearts = create_gray_hearts()
    ball_image = create_ball()
    color_bg = CYAN
    while running and gtfo:
        gtfo = start_menu(screen)
        objects = Lvl.return_bricks(the_levels[current_level])
        BRICKS_REMAINING = len(objects)
        if PROMPTS:
            lvl_prompt(screen, current_level + 1)
        balls = []

        ########################### Test image ball ##############################
        ball = Ball_img(random.randrange(200, 300), random.randrange(200, 500), -DIFFICULTY, -DIFFICULTY, color_bg, ball_image, BALL_SIZE, screen, False, True)
        balls.append(ball)

        ##########################################################################

        '''for b in range(NO_OF_BALLS):
            ball = Ball(random.randrange(200, 300), random.randrange(200, 500), -DIFFICULTY, -DIFFICULTY, RED, BALL_SIZE, screen, False, True)
            balls.append(ball)
            objects.append(ball)'''

        bounce_brick = create_bouncebrick(screen)
        #angle = 0
        in_level = True
        while in_level and gtfo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    in_level = False

                '''if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        bounce_brick.x -= 40
                    if event.key == pygame.K_RIGHT:
                        bounce_brick.x += 40'''

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                bounce_brick.x -= B_BRICK_SPEED
            if keys[pygame.K_RIGHT]:
                bounce_brick.x += B_BRICK_SPEED

            screen.fill(BLACK)
            draw_bg(screen, bg)
            bounce_brick.draw()
            draw_heart(screen, gray_hearts)
            draw_heart(screen, red_hearts)



            for b in balls:
                b.Draw()
                ############################ MOVE ##############################
                #angle = determine_angle(angle, b)
                b.Move()
            for obj in objects:
                for ball in balls:
                    if Rect.is_bouncy(obj):

                        obj.draw()
                        if_is_bouncy(ball, obj, objects)
                        special_if_is_bouncy(ball, bounce_brick, objects)
            keeping_score(screen)
            pygame.display.update()
            clock.tick(FPS)

            ############################# DEATH #############################
            if DEATH:
                for ball in balls:
                    if Ball.dead(ball):
                        lose_life(balls)
                        red_hearts.pop()
                        LIVES -= 1
                        sleep(1)

                        if LIVES == 0:
                            highscore(SCORE, screen)
                            in_level = False
                            #running = False
            #################################################################
            if BRICKS_REMAINING <= 0:
                current_level += 1
                if PROMPTS:
                    score_prompt(screen)
                in_level = False
            if not gtfo:
                print("new game?")

def keeping_score(screen):

    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Score: "+str(SCORE), True, WHITE, BLACK)
    textRect = text.get_rect()
    textRect.center = (70, 20)
    screen.blit(text, textRect)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
    the_levels = init_lvl(screen)
    run(the_levels, screen,)

if __name__ == "__main__":
    main()
