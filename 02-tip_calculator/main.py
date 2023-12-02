#!/usr/bin/python3
""" A tip calculator program """
import math


def main():
    """ entry point """
    print("Welcome to the tip calculator.")

    total = input("What was the total bill? $")
    total = validate(total)

    noppl = input("How many people to split the bill? ")  # number of people
    noppl = validate(noppl)

    per = input("What percentage tip would you like to give? (0 to 100):\n")
    per = validate(per)

    res = round((total/noppl) + ((total*per/100) / noppl), 2)
    print(f"Each person should pay: {res}")


def validate(val):
    """ validates the ``val`` """
    while True:
        try:
            val = float(val)
            if val < 0:
                raise ValueError()
        except (TypeError, ValueError):
            val = input("Please enter a valid number:\n")
        else:
            break

    return val


if __name__ == "__main__":
    main()
