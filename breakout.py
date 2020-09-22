import pygame
import random
from time import sleep
#import lvls
#from settings import *
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BRIGHT_GREEN = (55, 255, 55)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
colors = [WHITE, BLUE, GREEN, RED, YELLOW, MAGENTA, CYAN]
SCREEN_WIDTH = 800
SCREEN_HIGHT = 600
FPS = 120
MAX_RADIUS = 40
BRICK_SIZE_X = 70
BRICK_SIZE_Y = 20
SCORE = 0
BRICKS_REMAINING = 0
DIFFICULTY = 0

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
    def left(self):
        return self.x - self.radius

    @property
    def right(self):
        return self.x + self.radius

    def Move(self):
        self.x += self.x_step * 1
        self.y += self.y_step * 1

        if not self.radius <= self.x <= SCREEN_WIDTH - self.radius:
            self.x_step *= -1

        if not self.radius <= self.y <= SCREEN_HIGHT - self.radius:
            self.y_step *= -1

    def Draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

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
    def __init__(self, x, y, width, height, color, screen, is_bouncy, is_indestructable):
        super().__init__(x, y, width, height, color, screen, is_bouncy, is_indestructable)

class Lvl:
    def __init__(self, bg_color, bricks):

        self.bg_color = bg_color
        self.bricks = bricks

    def return_bricks(self):
        return self.bricks

    def return_bg_color(self):
        return self.bg_color


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

        mouse = pygame.mouse.get_pos()

        # print(mouse)

        if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(screen, BRIGHT_GREEN, (150, 450, 100, 50))
        else:
            pygame.draw.rect(screen, GREEN, (150, 450, 100, 50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf = smallText
        textRect = "GO!"
        textRect.center = ((150 + (100 / 2)), (450 + (50 / 2)))
        screen.blit(textSurf, textRect)

        pygame.draw.rect(screen, RED, (550, 450, 100, 50))

        pygame.display.update()
        clock.tick(15)

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

def lvl_test(lvl_screen):
    screen = lvl_screen
    y = 0
    lines = 1
    objects = []
    for l in range(lines):
        x = 200
        y += 30
        color = colors[l+1]
        for _ in range(1):
            obst = Rect(x, y, BRICK_SIZE_X, BRICK_SIZE_Y, color, screen, True, False)
            objects.append(obst)
            x += 80
    return objects

def lvl_1(lvl_screen):
    screen = lvl_screen
    y = 10
    lines = 6
    objects = []
    for l in range(lines):
        x = 50
        y += 30
        color = colors[l+1]
        for _ in range(9):
            obst = Rect(x, y, BRICK_SIZE_X, BRICK_SIZE_Y, color, screen, True, False)
            objects.append(obst)
            x += 80
    return objects

def lvl_2(lvl_screen):
    screen = lvl_screen
    y = 10
    lines = 4
    brick_color = [RED, RED, BLUE, BLUE]
    objects = []
    for l in range(lines):
        x = 50
        y += 30
        for _ in range(9):
            obst = Rect(x, y, BRICK_SIZE_X, BRICK_SIZE_Y, brick_color[l], screen, True, False)
            objects.append(obst)
            x += 80
    return objects

def init_lvl(screen):
    list_of_levels = [lvl_test(screen), lvl_1(screen), lvl_2(screen)]
    the_levels = []
    for l in range(len(list_of_levels)):
        lvl = Lvl(None, list_of_levels[l])
        the_levels.append(lvl)
    return the_levels

def create_bouncebrick(screen):
    bounce_brick = BounceBrick(100, 550, 100, 20, WHITE, screen, True, True)
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

def special_if_is_bouncy(ball, BounceBrick, objects):
    if BounceBrick.collide(ball):
        #
        if BounceBrick.left <= ball.right <= BounceBrick.left + DIFFICULTY:
            ball.x_step = -DIFFICULTY
            return hit(BounceBrick, objects)
        if BounceBrick.right >= ball.left >= BounceBrick.right - DIFFICULTY:
            ball.x_step = DIFFICULTY
            return hit(BounceBrick, objects)
        if BounceBrick.top <= ball.bottom <= BounceBrick.top + DIFFICULTY:
            ball.y_step = -DIFFICULTY
            return hit(BounceBrick, objects)
        if BounceBrick.bottom >= ball.top >= BounceBrick.bottom - DIFFICULTY:
            ball.y_step = DIFFICULTY
            return hit(BounceBrick, objects)

def hit(obj, objects):
    if not Object.is_indestructable(obj):
        global SCORE
        global BRICKS_REMAINING
        try:
            objects.remove(obj)
        except:
            print("FEL")
        SCORE += 50
        BRICKS_REMAINING = BRICKS_REMAINING - 1

def keeping_score(screen):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Score: "+str(SCORE), True, WHITE, BLACK)
    textRect = text.get_rect()
    textRect.center = (70, 20)
    screen.blit(text, textRect)


def run(the_levels, screen):
    pygame.init()
    clock = pygame.time.Clock()
    #game_intro(screen, clock)
    running = True
    global DIFFICULTY
    global BRICKS_REMAINING
    current_level = 0
    DIFFICULTY += current_level + 1
    score = 0
    while running:
        objects = Lvl.return_bricks(the_levels[current_level])
        BRICKS_REMAINING = len(objects)

        lvl_prompt(screen, current_level + 1)
        red_ball = Ball(200, 500, -DIFFICULTY, -DIFFICULTY, RED, 10, screen, False, True)
        blue_ball = Ball(400, 500, -DIFFICULTY, -DIFFICULTY, BLUE, 10, screen, False, True)
        balls = [red_ball, blue_ball]
        bounce_brick = create_bouncebrick(screen)
        objects.append(red_ball)
        objects.append(blue_ball)
        #objects.append(bounce_brick)
        in_level = True
        while in_level:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    in_level = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        bounce_brick.x -= 30
                    if event.key == pygame.K_RIGHT:
                        bounce_brick.x += 30
            screen.fill(BLACK)
            red_ball.Draw()
            blue_ball.Draw()
            bounce_brick.draw()
            red_ball.Move()
            blue_ball.Move()
            for obj in objects:
                for ball in balls:
                    if Rect.is_bouncy(obj):
                        obj.draw()
                        if_is_bouncy(ball, obj, objects)
                        special_if_is_bouncy(ball, bounce_brick, objects)
            keeping_score(screen)
            pygame.display.update()
            clock.tick(FPS)
            '''            if Ball.dead(red_ball):
                final_score_prompt(screen)
                in_level = False
                running = False'''
            if BRICKS_REMAINING <= 0:
                current_level += 1
                score_prompt(screen)
                in_level = False

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
    the_levels = init_lvl(screen)
    run(the_levels, screen)


#####
    # blue_rect = Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HIGHT // 2 - 50, 100, 100, BLUE, screen, True)
    # objects.append(blue_rect)
#####
    # run(the_levels, screen)

if __name__ == "__main__":
    main()
'''if bounce_brick.collide(ballen):
    if bounce_brick.left <= ballen.right <= bounce_brick.left + 1:
        ballen.x_step = -1
    if bounce_brick.right >= ballen.left >= bounce_brick.right - 1:
        ballen.x_step = 1
    if bounce_brick.top <= ballen.bottom <= bounce_brick.top + 1:
        ballen.y_step = -1
    if bounce_brick.bottom >= ballen.top >= bounce_brick.bottom - 1:
        ballen.y_step = 1

if blue_rect.collide(ballen):
    if blue_rect.left <= ballen.right <= blue_rect.left + 1:
        ballen.x_step = -1
    if blue_rect.right >= ballen.left >= blue_rect.right - 1:
        ballen.x_step = 1
    if blue_rect.top <= ballen.bottom <= blue_rect.top + 1:
        ballen.y_step = -1
    if blue_rect.bottom >= ballen.top >= blue_rect.bottom - 1:
        ballen.y_step = 1'''