#!/usr/bin/python3
""" A password generator """
from random import randint
import sys

used = [sys.maxsize]
out = " "


def main():
    """ entry point """
    global used
    global out

    print("Welcome to The Password Generator")

    length = input("Enter the length of the password: ")
    length = validate(length)

    sclen = nolen = used[0]
    if length > 1:
        while sclen > length:
            sclen = input("How many special letters?: ")  # special characters
            sclen = validate(sclen)
    else:
        sclen = 0

    if length - sclen > 1:
        while nolen > length - sclen:
            nolen = input("How many numbers?: ")  # numbers len
            nolen = validate(nolen)
    else:
        nolen = 0

    out = " " * length

    length = (length - sclen) - nolen

    letters = 'abcdefghijklmnopqrxtuvwxyzABCDEFGHIJKLMNOPQRXTUVWXYZ'
    specialc = '~`\\"\'!@#$%^*()_+><,./?;:}{][|-='
    numbers = '0123456789'

    generate(letters, length)
    generate(specialc, sclen)
    generate(numbers, nolen)

    print(f">'{out.replace(' ', '')}'<")


def validate(val):
    """ Validates the ``val`` """
    while True:
        try:
            val = int(val)
            if val < 0:
                raise ValueError()
        except (TypeError, ValueError):
            val = input("Please enter a valid value: ")
        else:
            break
    return val


def generate(cset, length):
    global out
    global used

    outlen = len(out)
    rand = used[0]
    for i in range(length):
        while rand not in used:
            rand = randint(0, outlen - 1)
        out = out[:rand] + cset[randint(0, len(cset) - 1)] + out[rand + 1:]
        used.append(rand)


if __name__ == "__main__":
    main()
