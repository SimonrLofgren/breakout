import time
import random
import sys


def panda_cash():

    pandacash = 9     #tror denna ska flyttas till gamehandlern
    no_panda_cash_message = "You have no Panda Cash."
    enough_panda_cash_message = "You have enough Panda Cash to buy your freedom! Visit the startingroom!"
    current_panda_cash_message = f"You have {pandacash} Panda Cash. Panda Cash can be traded for extra lives," \
                                 f" or your freedom (10x) at the starting room."

    if pandacash == 0:
        for char in no_panda_cash_message:
            timer_value1 = random.uniform(0.01, 0.02)
            sys.stdout.write(char)
            time.sleep(timer_value1)

    elif pandacash == 10:
        for char in enough_panda_cash_message:
            timer_value1 = random.uniform(0.01, 0.02)
            sys.stdout.write(char)
            time.sleep(timer_value1)

    else:
        for char in current_panda_cash_message:
            timer_value1 = random.uniform(0.01, 0.02)
            sys.stdout.write(char)
            time.sleep(timer_value1)


panda_cash()



