#!/usr/bin/python3
import random

MAX_TRIES = 10

class GuessANumber:
    def __init__(self, random_num, max_tries):
        self.random = random_num
        self.max_tries = max_tries
        self.try_number = 0

    def guess(self):
        print('Gues a number:')
        number_s = input()
        self.try_number += 1
        if (not number_s.isnumeric()):
            print('Give a nnumber you jerk.')
            return False
        number_s = int(number_s)
        if number_s > self.random:
            print("The number you're looking for is to big.")
            return False
        elif number_s < self.random:
            print("The number you're looking for is to small.")
            return False
        else:
            print("Congratulations! This is the number!")
            return True

    def check_max_tries(self):
        return self.try_number >= self.max_tries;

    def get_try_number(self):
        return self.try_number

    def reset(self, random_num, max_tries):
        self.random = random_num
        self.max_tries = max_tries
        self.try_number = 0


def main():
    guess = GuessANumber(random.randint(0, 20), MAX_TRIES)

    while(not guess.guess() and not guess.check_max_tries()):
        print('Try once again. You did it (' ,guess.get_try_number(), ') times of (' , MAX_TRIES , ')')

    print('Guess again.')
    guess.reset(random.randint(0, 20), MAX_TRIES)
    while(not guess.guess() and not guess.check_max_tries()):
        print('Try once again.')



if __name__ == "__main__":
    main()