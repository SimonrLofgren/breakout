import pygame
import random
#import lvls
#from settings import *
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
#global colors
colors = [WHITE, BLUE, GREEN, RED, YELLOW, MAGENTA, CYAN]
SCREEN_WIDTH = 800
SCREEN_HIGHT = 600
FPS = 120
MAX_RADIUS = 40
BRICK_SIZE_X = 70
BRICK_SIZE_Y = 20

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

def lvl_1(lvl_screen):
    screen = lvl_screen
    y = 0
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
    y = 0
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
    list_of_levels = [lvl_1(screen), lvl_2(screen)]
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
        if obj.left <= ball.right <= obj.left + 1:
            ball.x_step = -1
            return hit(obj, objects)
        if obj.right >= ball.left >= obj.right - 1:
            ball.x_step = 1
            return hit(obj, objects)
        if obj.top <= ball.bottom <= obj.top + 1:
            ball.y_step = -1
            return hit(obj, objects)
        if obj.bottom >= ball.top >= obj.bottom - 1:
            ball.y_step = 1
            return hit(obj, objects)

def hit(obj, objects):
    if not Object.is_indestructable(obj):
        objects_copy = objects
        objects_copy.remove(obj)
        return objects_copy

def run(bounce_brick, red_ball, objects, screen):
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    bounce_brick.x -= 20
                if event.key == pygame.K_RIGHT:
                    bounce_brick.x += 20
        screen.fill(BLACK)
        red_ball.Draw()
        red_ball.Move()
        obj_copy = objects
        for obj in obj_copy:
            if Rect.is_bouncy(obj):
                obj.draw()
                obj_copy = if_is_bouncy(red_ball, obj, objects)
        pygame.display.update()
        clock.tick(FPS)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
    the_levels = init_lvl(screen)
    
    objects = Lvl.return_bricks(the_levels[0])


    red_ball = Ball(200, 500, -1, -1, RED, 10, screen, False, True)
    bounce_brick = create_bouncebrick(screen)
    objects.append(red_ball)
    objects.append(bounce_brick)

#####
    # blue_rect = Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HIGHT // 2 - 50, 100, 100, BLUE, screen, True)
    # objects.append(blue_rect)
#####
    run(bounce_brick, red_ball, objects, screen)

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