from initialize.pwups_create import Pwup_sprites


class Pwup:
    def __init__(self, x, y, y_speed, pwup_type, pwup_image, cube, screen):
        self.x = x
        self.y = y
        self.y_speed = y_speed
        self.pwup_type = pwup_type
        self.pwup_image = pwup_image
        self.cube = cube
        self.screen = screen

    @property
    def bottom(self):
        return self.y + self.cube

    @property
    def top(self):
        return self.y

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self.cube

    def collide(self, other):
        if self.left >= other.right or other.left >= self.right:
            return False
        if self.top >= other.bottom or other.top >= self.bottom:
            return False
        return True


    @property
    def pwup_type_return(self):
        return self.pwup_type

    def draw_pwup(self):
        self.screen.blit(self.pwup_image, (self.x, self.y))

    def move(self):
        self.y += self.y_speed

    @staticmethod
    def pwup_create(screen, pwup_data_obj):
        type = pwup_data_obj.no
        y_speed = 1

        pwup = Pwup(pwup_data_obj.x, pwup_data_obj.y, y_speed, type, Pwup_sprites().ret_sprite(type), 30, screen)

        return pwup