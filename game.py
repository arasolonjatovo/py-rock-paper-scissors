from utils import check_user_entry

def get_user_entry():
    user_move = input("Enter your move (rock, paper, scissors) : ")
    while not check_user_entry(user_move):
        print("Invalid move. Please try again.")
        user_move = input("Enter your move (rock, paper, scissors) : ")
    print(user_move)
    return user_move
