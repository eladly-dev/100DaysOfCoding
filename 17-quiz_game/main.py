#!/usr/bin/python3
""" Test for the QuizzGame Class """
from quiz_game import QuizGame


def main():
    """ entry point """
    amount = input("How many question?: ")
    stages = ["easy", "medium", "hard"]

    while True:
        try:
            amount = int(amount)
            if not amount:
                raise ValueError()
        except ValueError:
            amount = input("Please Enter a valid value: ")
        else:
            break

    difficulty = input("How difficult do u want it to be? [Easy, Medium, Hard]: ").lower()
    while difficulty not in stages and difficulty[0] not in "emh":
        difficulty = input("Please Enter a valid value: ")

    if difficulty[0] == stages[0][0]:
        difficulty = stages[0]
    elif difficulty[0] == stages[2][0]:
        difficulty = stages[2]
    else:
        difficulty = stages[1]

    new_game = QuizGame(amount, difficulty)
    new_game.start()


if __name__ == "__main__":
    main()
