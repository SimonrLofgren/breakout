from classes.Object import Object


class BounceBrick(Object):
    def __init__(self, x, y, width, height, color, screen, is_bouncy, is_indestructable, bb_image):
        super().__init__(x, y, color, screen, is_bouncy, is_indestructable)
        self.width = width
        self.height = height
        self.bb_image = bb_image

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
        # pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        self.screen.blit(self.bb_image, (self.x, self.y))

    def ai(self, ball_x):
        self.x = ball_x
