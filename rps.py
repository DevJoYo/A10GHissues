# This game was built using GitHub Copilot, but notably the code
# matches this website's version almost identically:
#   https://realpython.com/python-rock-paper-scissors/


import random

loop = 1

while loop == 1:
    user_action = input("Enter throw (rock, paper, scissors): ")
    ai_action = random.choice(["rock", "paper", "scissors"])

    print(f"\nYou chose {user_action}, AI chose {ai_action}.\n")

    if user_action == ai_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if ai_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if ai_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if ai_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    while loop == 1:
        user_choice = input("Play again (Y / N): ")
        user_choice = user_choice.upper()
        if user_choice == 'Y':
            break
        elif user_choice == 'N':
            loop = 0
        else:
            print("incorrect option entered. Please enter Y or N")
  

