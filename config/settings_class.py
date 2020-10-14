

class Settings:
    def __init__(self, DIFFICULTY, SCORE, LIVES):
        self.DIFFICULTY = DIFFICULTY
        self.SCORE = SCORE
        self.LIVES = LIVES

    def change_SCORE(self, new):
        self.SCORE += new

    def change_DIFFICULTY(self, new):
        self.DIFFICULTY = new

    def change_LIVES(self, new):
        self.LIVES += new
