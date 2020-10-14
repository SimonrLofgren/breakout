

class Settings:
    def __init__(self, DIFFICULTY, SCORE, LIVES, NO_OF_BALLS):
        self.DIFFICULTY = DIFFICULTY
        self.SCORE = SCORE
        self.LIVES = LIVES
        self.NO_OF_BALLS = NO_OF_BALLS

    def change_SCORE(self, new):
        self.SCORE += new

    def change_DIFFICULTY(self, new):
        self.DIFFICULTY = new

    def change_LIVES(self, new):
        self.LIVES += new

    def change_NO_OF_BALLS(self, new):
        self.NO_OF_BALLS += new