#!/usr/bin/python3
""" The band name generator program """
import time, sys

def main():
    """ The entry point """
    print("Welcome to the Band Name Generator")

    city = input("What's name of the city you grew up in?\n")
    city = validate(city)

    pet = input(f"{city}, cool!\nNow what's your pet's name?\n");
    pet = validate(pet)

    print("mmm, lemme think", end="")
    for i in range(3):
        for t in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(1.0/3)
        sys.stdout.write("\b" * 3 + " " * 3 + "\b" * 3)
        sys.stdout.flush()
    sys.stdout.write("\b" * 17 + " " * 17 + "\b" * 17)
    sys.stdout.flush()

    print(f"Your band name could be {city} {pet}")

def validate(val):
    """ Validates the input """
    while type(val) is not str or len(val) <= 0:
        val = input("Please enter a valid name\n")

    return val

if __name__ == "__main__":
    main()
