from classes.Object import *
from config import SCREEN_HIGHT, SCREEN_WIDTH
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
        self.screen.blit(self.ball_image, (self.x-7, self.y-7))

    def Reset(self):
        self.x = random.randrange(200, 400)
        self.y = random.randrange(200, 400)

    ###prel death

    def dead(self):
        if self.y > SCREEN_HIGHT - self.radius:
            return True

    def heading(self):
        return self.x_step, self.y_step