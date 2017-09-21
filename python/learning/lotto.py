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

class ListSorted:

    def __init__(self, file):
        self.file = file
        self.match_list = []


    def get_list(self):
        lotto_file = self.file
        with open(lotto_file) as file:
            for line in file:
                match = re.search(r'-..-', line)
                match2 = re.search(r'=..=', line)
                data = match.group()[1:3:], match2.group()[1:3:]
                self.match_list.append(data)
            return self.match_list

    def print_sort_numbers(self):
        numbers = self.match_list
        numbers_sorted = sorted(numbers, reverse=True, key=itemgetter(1))
        for i in numbers_sorted:
            print('Number:', i[0], ' Quantity:', i[1])

class UpdateFile:

    def __init__(self, file, value):
        self.file = file
        self.value = value
        self.line = None
        self.new_line = None

    def update_draw(self):
        lotto_file = self.file
        number = self.value
        with open(lotto_file) as file:
            for self.line in file:
                match = re.search('-'+number+'-', self.line)
                if match:
                    main_number = self.line[1:3]
                    old_value = self.line[5:7]
                    new_value = int(old_value)+1
                    new_value = str(new_value)
                    self.new_line = ('-'+main_number+'-'+'='+new_value+'=\n')
                    return self.line, self.new_line

    def write_to_file(self):
        old_line = self.line
        new_line = self.new_line
        with open(self.file, 'r') as file:
            file = file.read()

        new_file_data = file.replace(old_line, new_line)

        with open(self.file, 'w') as file:
            file.write(new_file_data)

def main():

    file_update = UpdateFile('lotto.txt', '15')
    draw_update = file_update.update_draw()
    write_draw_to_file = file_update.write_to_file()
    write_draw_to_file


    sorting_list = ListSorted('lotto.txt')
    getting_list = sorting_list.get_list()
    getting_sorted_list = sorting_list.print_sort_numbers()
    getting_sorted_list



if __name__ == '__main__':
    main()