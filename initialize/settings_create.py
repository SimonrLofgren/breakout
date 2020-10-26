from config.settings_class import *
import glob
DIFFICULTY = 2
SCORE = 0
LIVES = 3
NO_OF_BALLS = 1
BOUNCEBRICK_SIZE = 100
BRICK_SIZE = 72
BRICK_TYPE = 1
FPS = 110
BRICKS_REMAINING = 0
CURRENT_LVL = 0
SOUND = True
B_BRICK_SPEED = 4

files = glob.glob('Level/Levels/*.txt')
lvl_files = [file for file in files if 'lvl_' in file]
NR_OF_LVL = len(lvl_files)

SETTINGS_OBJ = Settings(DIFFICULTY, SCORE, LIVES, NO_OF_BALLS, BRICK_SIZE, BRICK_TYPE, FPS,
                        BRICKS_REMAINING, CURRENT_LVL, NR_OF_LVL, BOUNCEBRICK_SIZE, SOUND, B_BRICK_SPEED)
