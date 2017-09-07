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

def get_list():
    match_list = []
    with open('lotto.txt') as file:
        for line in file:
            match = re.search(r'-..-', line)
            match2 = re.search(r'=..=', line)
            data = match.group()[1:3:], match2.group()[1:3:]
            match_list.append(data)
        return match_list

def update_draw(value):
    number = value
    with open('lotto.txt') as file:
        for line in file:
            match = re.search('-'+number+'-', line)
            if match:
                main_number = line[1:3]
                new_value = int(line[5:7])+1
                new_value = str(new_value)
                return main_number, new_value

# def update_number():
#     updated_number = find_number(value)[0]
#     updated_value = find_number(value)[1]
#     print(updated_number, updated_value)




def print_sort_numbers():
    numbers = get_list()
    numbers_sorted = sorted(numbers, reverse=True, key=itemgetter(1))
    for i in numbers_sorted:
        print('Number:', i[0], ' Quantity:', i[1])

def main():
    get_value = update_draw('17')
    print(get_value)

if __name__ == '__main__':
    main()