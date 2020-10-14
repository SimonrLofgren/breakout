class Pwup_data:
    def __init__(self, go, no, x, y):
        self.go = go
        self.no = no
        self.x = x
        self.y = y

    def set(self, bool, int, x_pos, y_pos):
        self.go = bool
        self.no = int
        self.x = x_pos
        self.y = y_pos

class Timer:
    def __init__(self, t, limit):
        self.t = t
        self.limit = limit

    def pwup_timer(self):
        if self.t >= self.limit:
            self.t = 0
            return True
        else:
            self.t += 1
            return False
