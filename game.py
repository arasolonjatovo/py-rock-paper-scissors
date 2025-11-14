from utils import check_user_entry


def get_user_entry():
    user_move = input("Enter your move (rock, paper, scissors) : ")
    while not check_user_entry(user_move):
        print("Invalid move. Please try again.")
        user_move = input("Enter your move (rock, paper, scissors) : ")
    print(user_move)
    return user_move


def generate_computer_move():
    import random

    return random.choice(["rock", "paper", "scissors"])


def find_winner(user_move, computer_move):
    if user_move == computer_move:
        return "It's a tie!"
    elif (
        (user_move == "rock" and computer_move == "scissors")
        or (user_move == "paper" and computer_move == "rock")
        or (user_move == "scissors" and computer_move == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"

def start_game():
    user_move = get_user_entry()
    computer_move = generate_computer_move()
    result = find_winner(user_move, computer_move)
    print(f"Computer chose: {computer_move}")
    print(result)