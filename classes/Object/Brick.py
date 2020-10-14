

class Brick:
    def __init__(self, x, y, width, height, image, screen, is_bouncy, is_indestructable, pwup, hits):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.screen = screen
        self.is_indestructable = is_indestructable
        self.is_bouncy = is_bouncy
        self.pwup = pwup
        self.hits = hits

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


    def draw(self):
        screen = self.screen
        screen.blit(self.image, (self.x, self.y))

    def hit_count(self):
        return self.hits

    def hit_minus(self):
        self.hits -= 1

    def is_bouncy_return(self):
        return self.is_bouncy

    def pwup_return(self):
        return self.pwup