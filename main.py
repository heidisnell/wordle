import random


class Wordle:
    def __init__(self):
        self.Wordle.new_game()

    def new_game(self):
        print("new game")

        with open("possible_words.txt") as possible_words:
            lines = possible_words.readlines()

        print(lines)


def play():
    wordle = Wordle()
    solved = False

    print("Enter your guess: ")


if __name__ == "__main__":
    play()
