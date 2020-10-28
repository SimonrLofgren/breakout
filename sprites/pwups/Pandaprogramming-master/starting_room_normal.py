import time
import random
import sys


def starting_room_normal():

    first_reply = ("You are now in the starting room.\n"
                   "Available commands are:\n"
                   "'instructions', 'exit', 'continue'\n")
    for char in first_reply:
        timer_value6 = random.uniform(0.01, 0.02)
        sys.stdout.write(char)
        time.sleep(timer_value6)




