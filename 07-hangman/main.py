#!/usr/bin/python3
""" The Hangman Game """
from random import randint

logo = """
███████████████████████▀███████████████████████
█─█─██▀▄─██▄─▀█▄─▄█─▄▄▄▄█▄─▀█▀─▄██▀▄─██▄─▀█▄─▄█
█─▄─██─▀─███─█▄▀─██─██▄─██─█▄█─███─▀─███─█▄▀─██
▀▄▀▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀
"""

pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

def main():
    """ The entry point """
    global words
    print(logo)
    input(f"{'Press Enter To Start' : ^48}")

    stages = len(pics)
    word = "cat" #words[randint(0, len(words) - 1)]
    hints = len(word) // 3
    stage = 0
    while stage >= 0 and stage < stages:
        if hints:
            print(f"{hints} hints")
        print(f"{pics[stage]}\n")

        message = "Enter a letter: "
        if hints > 0:
            message = message[:-2] + " or 0 for a hint: "

        uin = input(message)
        if uin and uin in word:
            print("Correct Guess")
            stage += 1
            continue
        elif not uin:
            continue

        if uin == "0":
            if hints > 0:
                print(word[randint(0, len(word) - 1)])
                hints -= 1
                continue
            else:
                print("U have no more hints")
                continue

        stage += 1
        if stage == stages - 1:
            print("You Lose")
        else:
            print("Wrong!")

main()
