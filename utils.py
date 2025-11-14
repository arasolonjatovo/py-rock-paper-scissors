def check_user_entry(user_move):
    valid_moves = ["rock", "paper", "scissors"]
    return user_move in valid_moves


def play_again():
    user_input = input("Do you want to play again? (y/n):").lower()
    return user_input == "y"
