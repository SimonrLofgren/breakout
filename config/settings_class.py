import time


class Settings:
    def __init__(self, DIFFICULTY, SCORE, LIVES, NO_OF_BALLS, BRICK_SIZE, BRICK_TYPE, FPS, BRICKS_REMAINING,
                 CURRENT_LVL, NR_OF_LVL, BOUNCEBRICK_SIZE, SOUND, B_BRICK_SPEED, TIMER, TIMER_DUR, DEATH, CHEATS):
        self.DIFFICULTY = DIFFICULTY
        self.SCORE = SCORE
        self.LIVES = LIVES
        self.NO_OF_BALLS = NO_OF_BALLS
        self.BRICK_SIZE = BRICK_SIZE
        self.BRICK_TYPE = BRICK_TYPE
        self.FPS = FPS
        self.BRICKS_REMAINING = BRICKS_REMAINING
        self.CURRENT_LVL = CURRENT_LVL
        self.NR_OF_LVL = NR_OF_LVL
        self.BOUNCEBRICK_SIZE = BOUNCEBRICK_SIZE
        self.SOUND = SOUND
        self.B_BRICK_SPEED = B_BRICK_SPEED
        self.TIMER = TIMER
        self.TIMER_DUR = TIMER_DUR
        self.DEATH = DEATH
        self.CHEATS = CHEATS

    def change_SCORE(self, new):
        self.SCORE += new

    def reset_SCORE(self):
        self.SCORE = 0

    def change_DIFFICULTY(self, new):
        self.DIFFICULTY = new

    def change_LIVES(self, new):
        self.LIVES += new

    def reset_LIVES(self):
        self.LIVES = 3

    def change_NO_OF_BALLS(self, new):
        self.NO_OF_BALLS += new

    def reset_NO_OF_BALLS(self):
        self.NO_OF_BALLS = 1

    def change_BRICK_TYPE(self, x):
        self.BRICK_TYPE += x

        if self.BRICK_TYPE < 0:
            self.BRICK_TYPE = 0
        elif self.BRICK_TYPE > 2:
            self.BRICK_TYPE = 2

        if self.BRICK_TYPE == 1:
            self.BOUNCEBRICK_SIZE = 100

        elif self.BRICK_TYPE == 2:
            self.BOUNCEBRICK_SIZE = 140

        else:
            self.BOUNCEBRICK_SIZE = 60
    def change_FPS(self, x):
        self.FPS = x

    def change_BRICKS_REMAINING(self, x):
        self.BRICKS_REMAINING = x

    def change_CURRENT_LVL(self):
        self.CURRENT_LVL += 1

    def reset_CURRENT_LVL(self):
        self.CURRENT_LVL = 0

    def change_NR_OF_LVL(self, x):
        self.NR_OF_LVL = x

    def SOUND_OFF(self):
        self.SOUND = False

    def SOUND_ON(self):
        self.SOUND = True

    def change_B_BRICK_SPEED(self, x):
        self.B_BRICK_SPEED = x

    def set_TIMER(self, t):
        """

        :param t: set duration of timer
        :return: NONE
        """
        self.TIMER = int(time.perf_counter())
        print(self.TIMER)
        self.TIMER_DUR = t

    def get_TIMER(self):

        current_time = int(time.perf_counter())
        print(current_time)
        print(self.TIMER)
        print("_____________________________")
        if current_time == self.TIMER + self.TIMER_DUR:
            return True
        else:
            return False

    def set_DEATH(self, x):
        """

        :param x: Bool
        :return:NONE
        """
        self.DEATH = x

    def set_CHEATS(self, x):
        self.CHEATS = x