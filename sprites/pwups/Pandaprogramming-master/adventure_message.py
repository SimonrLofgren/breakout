import time
import random
import sys
from adventure_door_choice import door_choice


def adventure_choice():

    adventure_start_message = (
        "\n\nVery well, off we go!\n\n" 
        ". . . . . . . . . . . . . . . . .\n\n" 
        "A door appears in front of you, do you wish to enter? type 'yes'/'no' in chat.\n")

    for char in adventure_start_message:
        timer_value1 = random.uniform(0.01, 0.02)
        sys.stdout.write(char)
        time.sleep(timer_value1)

    door_choice()

