from game import start_game
from utils import play_again


def main():
    while True:
        start_game()
        if not play_again():
            print("You fought well! Bye!")
            break


if __name__ == "__main__":
    main()
