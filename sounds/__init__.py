import pygame

from initialize.settings_create import SETTINGS_OBJ

brick_hit = pygame.mixer.Sound('sounds/bong_001.ogg')
bouncebrick_hit = pygame.mixer.Sound('sounds/glass_006.ogg')
pwup_hit = pygame.mixer.Sound('sounds/select_006.ogg')

'sounds/glass_006.ogg'

def play_soundtrack():
    #pygame.mixer.music.load('sounds/superstitious.mp3')
    pygame.mixer.music.load('sounds/TheFinalCountdown.mp3')
    pygame.mixer.music.play(-1)
    if not SETTINGS_OBJ.SOUND:
        pygame.mixer.music.set_volume(0.0)

def sound_brick_hit():
    brick_hit.play()

def sound_bouncebrick_hit():
    bouncebrick_hit.play()

def sound_pwup_hit():
    pwup_hit.play()