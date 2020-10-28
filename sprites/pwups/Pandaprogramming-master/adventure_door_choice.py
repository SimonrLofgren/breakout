import time
from starting_room_normal import starting_room_normal


def door_choice():

    while True:

        user_adventure_choice = input().lower()
        if user_adventure_choice == "yes":
            print("questroom method insert here")
        elif user_adventure_choice == "no":
            print("You back away from the door.\n\n")
            time.sleep(2)
            starting_room_normal()
        elif user_adventure_choice == "exit":
            print("Are you sure you want to exit the game? Type yes/no")
            user_choice_exit2 = input().lower()
            if user_choice_exit2 == "yes":
                exit()
            elif user_choice_exit2 == "no":
                print("Available commands are: 'yes', 'no', 'exit'")
