#!/usr/bin/python3
""" A quizz game """
import json
from urllib.request import urlopen


class QuizGame():
    """ This is a class for the quizz game """
    questions = ""
    i = 0
    result = 0

    def __init__(self, amount, difficulty):
        qlink = f"https://opentdb.com/api.php?amount={amount}&category=9&difficulty={difficulty}&type=boolean"

        self.get_questions(qlink)

    def get_questions(self, qlink):
        """ gets the question from the api """
        if qlink and type(qlink) is str:
            response = urlopen(qlink)

            self.questions = json.loads(response.read())["results"]
        else:
            raise TypeError("the link most be non-empty string")

    def start(self):
        """ starts the game """
        for self.i in range(len(self.questions)):
            self.print_question()
            uinput = self.get_input()
            self.get_result(uinput)

    def print_question(self):
        """ prints the question """
        question = self.questions[self.i]["question"]
        print(f"Q{self.i}: {question}", end="")

    def get_input(self):
        """ gets the input from the user and validates it """
        uinput = input("True or False:\n")

        while not uinput:
            uinput = input("Please Enter a valid value\n")

        return uinput.lower()

    def get_result(self, uinput):
        """ checks the result and the score and prints them """
        correct = self.questions[self.i]["correct_answer"].lower()
        if correct == uinput or correct[0] == uinput[0]:
            print("Correct!")
            self.result += 1
        else:
            question = self.questions[self.i]["correct_answer"]
            print(f"Incorrect")
        print(f"Your current score is: {self.result}/{len(self.questions)}")
