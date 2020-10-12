

class Heart:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    @property
    def x_pos(self):
        return self.x

    @property
    def y_pos(self):
        return self.y

    @property
    def the_image(self):
        return self.image


    def draw(self):
        screen.blit(self.image, (self.x, self.y))
