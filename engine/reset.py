from initialize.settings_create import SETTINGS_OBJ


def reset_game():
    SETTINGS_OBJ.reset_NO_OF_BALLS()
    SETTINGS_OBJ.reset_SCORE()
    SETTINGS_OBJ.reset_LIVES()
