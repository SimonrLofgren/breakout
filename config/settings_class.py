

class Settings:
    def __init__(self, DIFFICULTY, SCORE, LIVES, NO_OF_BALLS, BRICK_SIZE, BRICK_TYPE, FPS, BRICKS_REMAINING):
        self.DIFFICULTY = DIFFICULTY
        self.SCORE = SCORE
        self.LIVES = LIVES
        self.NO_OF_BALLS = NO_OF_BALLS
        self.BRICK_SIZE = BRICK_SIZE
        self.BRICK_TYPE = BRICK_TYPE
        self.FPS = FPS
        self.BRICKS_REMAINING = BRICKS_REMAINING

    def change_SCORE(self, new):
        self.SCORE += new

    def change_DIFFICULTY(self, new):
        self.DIFFICULTY = new

    def change_LIVES(self, new):
        self.LIVES += new

    def change_NO_OF_BALLS(self, new):
        self.NO_OF_BALLS += new

    def change_BRICK_TYPE(self, x):
        self.BRICK_TYPE += x

        if self.BRICK_TYPE < 0:
            self.BRICK_TYPE = 0
        elif self.BRICK_TYPE > 2:
            self.BRICK_TYPE = 2

        if self.BRICK_TYPE == 1:
            self.BRICK_SIZE = 100

        elif self.BRICK_TYPE == 2:
            self.BRICK_SIZE = 140

        else:
            self.BRICK_SIZE = 60
    def change_FPS(self, x):
        self.FPS = x

    def change_BRICKS_REMAINING(self, x):
        self.BRICKS_REMAINING = x