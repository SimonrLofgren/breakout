import time
import random
import sys


def welcome_message():

    starting_message = "Hello, and welcome to Panda programming!"
    for char in starting_message:
        timer_value1 = random.uniform(0.01, 0.02)
        sys.stdout.write(char)
        time.sleep(timer_value1)

    time.sleep(2)

    ask_user_name = "\nBefore we start,\n"
    for char in ask_user_name:
        timer_value2 = random.uniform(0.01, 0.02)
        sys.stdout.write(char)
        time.sleep(timer_value2)

    time.sleep(1)

    while True:
        error_message_1 = "Please enter your name in the textbox below, with only alphabetic characters.\n"
        for char in error_message_1:
            timer_value4 = random.uniform(0.01, 0.02)
            sys.stdout.write(char)
            time.sleep(timer_value4)
        user_name = input()

        if user_name.isalpha():
            hello_message = f"\nHello, {user_name}, it is nice to have you here!"
            for char in hello_message:
                timer_value3 = random.uniform(0.01, 0.02)
                sys.stdout.write(char)
                time.sleep(timer_value3)
            break

    time.sleep(1)


