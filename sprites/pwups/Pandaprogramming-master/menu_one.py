from instructions_message import instructions_message
from adventure_message import adventure_choice


def menu_one():

    while True:

        user_starting_room_choice = input().lower()
        if user_starting_room_choice == "instructions":
            instructions_message()
            menu_one()
        elif user_starting_room_choice == "continue":
            adventure_choice()
        elif user_starting_room_choice == "exit":
            print("Are you sure you want to exit the game? Type yes/no")
            user_choice_exit1 = input().lower()
            if user_choice_exit1 == "yes":
                exit()
            elif user_choice_exit1 == "no":
                print("Available commands are: 'instructions', 'continue', 'exit'")
