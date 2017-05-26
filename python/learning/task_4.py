#!/usr/bin/python3
#Create proper python file with main function.

# Create array (list) of 20 items with random numbers from 0 to 100. Than make function taht will get list and return sorted one. In python for sure there is some list function that will sort it. 
# But to practice more find algorithm how to do it and try to implement it. 

#USE ANY HELP YOU WANT (INTERNET, BOOKS) BUT PLEASE DO NOT COPY CODE, BUT REWRITE IT BY YOUR SELF LETER BY LETER.

import random


def sort_list():
    numbers_list = [25, 13, 5, 0, 4, 4, 22]
    sorted_list = []
    while numbers_list:
        minimum = numbers_list[0]
        for i in numbers_list:
            if i <= minimum:
                minimum = i
        sorted_list.append(minimum)
        numbers_list.remove(minimum)
    print(sorted_list)


def main():
    numbers_list = []
    #while len(numbers_list) <= 19:
    for i in range(20):
        numbers_list.append(random.randint(0, 100))
    print(numbers_list)


if __name__ == "__main__":
    main()
    sort_list()