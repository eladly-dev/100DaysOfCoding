#!/usr/bin/python3
""" Rock-paper-scissor Game """
from random import randint
from time import sleep
import sys

welcome = """
 _____         _        _____                      _____     _                 
| __  |___ ___| |_     |  _  |___ ___ ___ ___     |   __|___|_|___ ___ ___ ___ 
|    -| . |  _| '_|_   |   __| .'| . | -_|  _|_   |__   |  _| |_ -|_ -| . |  _|
|__|__|___|___|_,_| |  |__|  |__,|  _|___|_| | |  |_____|___|_|___|___|___|_|  
                  |_|            |_|         |_|                               
"""

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


def main():
    """ entry point """
    global rock, paper, scissor

    choices = [rock, paper, scissor]

    print(welcome)
    print(f"{'Ready to LOSE?' : ^70}")
    input(f"{'press enter to start': ^70}")

    while True:
        u = input("choose 0 for rock, 1 for paper or 2 for scissor: ")
        while True:
            try:
                u = int(u)
                if u > 3 or u < 0:
                    raise ValueError()
            except (TypeError, ValueError):
                u = input("Enter a valid choice \n0 for rock, 1 for paper, 2 for scissor or 3 to exit: ")
            else:
                break

        if u == 3:
            break

        r = randint(0, len(choices) - 1)

        print(f"\nUr choice:\n{choices[u]}\n{'-' * 20}")
        print(f"Mine:\n{choices[r]}")

        if u == 0 and r == 2 or u == 1 and r == 0 or u == 2 and r == 1:
            print("U won, just by luck :D\nShow me again if u confident")
        elif u == r:
            print("Huh, Draw\nLet's try again")
        else:
            print("True, I Win\nTold ya 'u gonna lose' ;D")


if __name__ == "__main__":
    main()
