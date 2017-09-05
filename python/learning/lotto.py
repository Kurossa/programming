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

def sort_numbers():
    pass

def main():
    data = get_list()
    numbers_sorted = sorted(data, reverse=True, key=itemgetter(1))
    print(numbers_sorted)

if __name__ == '__main__':
    main()