import time
import random
import sys


def instructions_message():

    guide_main_goal_message = (
        "\n\nYour main goal is to collect enough PandaCash to buy your freedom. Who doesn't like freedom?\n"
        "Down below the instructions of the game are listed:\n"
        "1. Complete various programming tasks flawless to gain PandaCash.\n"
        "2. If you don't succeed the task, your health will go down.\n"
        "3. More health can be purchased with earned PandaCash at the starting room.\n"
        "4. Navigate to each rooms by looking at the map to the left and entering them with textcommands.\n"
        "5. If your health drops below 1, the game will end and you will have to start over.\n"
        "6. You win by gaining 10 PandaCash as that is the price for freedom.\n\n"
        "If you would like to see the instructions again,"
        "TYPE 'instructions' in chat while being in the starting room.\n"
        "If you would like to exit the game, type exit in chat at any time.\n"
        "if not, TYPE 'continue' to start your journey!\n")

    for char in guide_main_goal_message:
        timer_value1 = random.uniform(0.01, 0.02)
        sys.stdout.write(char)
        time.sleep(timer_value1)




