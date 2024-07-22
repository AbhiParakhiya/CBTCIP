import random

def generate_number(digits):
    """Generate a random multi-digit number"""
    return str(random.randint(10**(digits-1), 10**digits - 1))

def get_hint(guess, number):
    """Get a hint for the guess"""
    hint = ""
    for i in range(len(guess)):
        if guess[i] == number[i]:
            hint += "X"  # correct digit in correct position
        elif guess[i] in number:
            hint += "O"  # correct digit in incorrect position
        else:
            hint += "-"  # incorrect digit
    return hint

def play_mastermind():
    """Play a game of Mastermind"""
    digits = 4  # number of digits in the number
    player1_number = generate_number(digits)
    player2_guesses = 0

    print("Player 1 has set a {}-digit number.".format(digits))
    while True:
        player2_guess = input("Player 2, enter your guess: ")
        if len(player2_guess) != digits:
            print("Invalid guess. Please enter a {}-digit number.".format(digits))
            continue
        player2_guesses += 1
        if player2_guess == player1_number:
            print("Congratulations, Player 2! You guessed the number in {} tries.".format(player2_guesses))
            break
        else:
            hint = get_hint(player2_guess, player1_number)
            print("Hint: {}".format(hint))

    # Now it's Player 2's turn to set the number
    player2_number = input("Player 2, set a {}-digit number: ".format(digits))
    player1_guesses = 0

    while True:
        player1_guess = input("Player 1, enter your guess: ")
        if len(player1_guess) != digits:
            print("Invalid guess. Please enter a {}-digit number.".format(digits))
            continue
        player1_guesses += 1
        if player1_guess == player2_number:
            if player1_guesses < player2_guesses:
                print("Congratulations, Player 1! You guessed the number in {} tries, which is less than Player 2's {} tries.".format(player1_guesses, player2_guesses))
                print("Player 1 is the Mastermind!")
            else:
                print("Congratulations, Player 1! You guessed the number in {} tries.".format(player1_guesses))
                print("Player 2 is the Mastermind!")
            break
        else:
            hint = get_hint(player1_guess, player2_number)
            print("Hint: {}".format(hint))

play_mastermind()