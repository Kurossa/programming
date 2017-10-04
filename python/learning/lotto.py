#!/usr/bin/python3

#Main task of this excercise is to practice opening, reading and writing files
#It's based on "Super pensja" Lotto game. The 'lotto.txt' file includes two columns of numbers: a number (marked with -,
#for example '-01-') and in the same row, information how many times that number was drawn (marked with =,for example
#'=24=').
#
#While executing lotto.py file with -s argument, it will display all 35 numbers sorted by the most drawn one.
#
#But while executing lotto.py with -x argument and giving 5 numbers (separated by space) it will add +1 to the
#=drawn number= to each number we gave after -x argument. This operation will update lotto.txt with the lates draw.

import re
from operator import itemgetter
import random

class LottoDraw:
    def __init__(self, file):
        self.file = file
        self.line = None
        self.new_line = None

    def update_draw(self, value):
        lotto_file = self.file
        number = value
        with open(lotto_file) as file:
            for self.line in file:
                match = re.search('-' +  number + '-', self.line)
                if match:
                    main_number = self.line[1:3]
                    main_number_count = self.line[5:7]
                    main_number_count = int(main_number_count)+1
                    main_number_count = str(main_number_count)
                    self.new_line = ('-' + main_number + '-' + '=' + main_number_count + '=\n')
                    self.write_to_file()
                    #return self.line, self.new_line

    def write_to_file(self):
        old_line = self.line
        new_line = self.new_line
        with open(self.file, 'r') as file:
            file = file.read()

        new_file_data = file.replace(old_line, new_line)

        with open(self.file, 'w') as file:
            file.write(new_file_data)


    def get_list(self):
        lotto_file = self.file
        match_list = []
        with open(lotto_file) as file:
            for line in file:
                match = re.search(r'-..-', line)
                match2 = re.search(r'=..=', line)
                data = match.group()[1:3:], match2.group()[1:3:]
                match_list.append(data)
        return match_list


    def print_sort_numbers(self):
        numbers = self.get_list()
        numbers_sorted = sorted(numbers, reverse=True, key=itemgetter(1))
        for i in numbers_sorted:
            print('Number:', i[0], ' Quantity:', i[1])


def main():

    lotto_draw = LottoDraw('lotto.txt')
    for i in range(100):
        lotto_draw.update_draw(str(random.randrange(1,35)))
    lotto_draw.print_sort_numbers()


if __name__ == '__main__':
    main()