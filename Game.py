import random

def get_user1_choice():
    """Get the user's choice"""
    while True:
        user1_choice = input("Enter your choice (rock, paper, or scissor): ")
        if user1_choice.lower() in ["rock", "paper", "scissor"]:
            return user1_choice.lower()
        else:
            print("Invalid choice. Please enter rock, paper, or scissor.")

def get_user2_choice():
    user2_choice = input("Enter your choice (rock, paper, or scissor): ")
    if user2_choice.lower() in ["rock", "paper", "scissor"]:
        return user2_choice.lower()
    else:
        print("Invalid choice. Please enter rock, paper, or scissor.")


def determine_winner(user1_choice, user2_choice):
    """Determine the winner"""
    if user1_choice == user2_choice:
        return "It's a tie!"
    elif (user1_choice == "rock" and user2_choice == "scissor") or \
         (user1_choice == "paper" and user2_choice == "rock") or \
         (user1_choice == "scissor" and user2_choice == "paper"):
        return "You win!"
    else:
        return "user2 wins!"

def play_game():
    """Play a game of Rock Paper Scissors"""
    user1_choice = get_user1_choice()
    user2_choice = get_user2_choice()
    print("User's choice: {}".format(user2_choice))
    print(determine_winner(user1_choice, user2_choice))

play_game()