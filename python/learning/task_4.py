#!/usr/bin/python3
#Create proper python file with main function.

# Create array (list) of 20 items with random numbers from 0 to 100. Than make function taht will get list and return sorted one. In python for sure there is some list function that will sort it. 
# But to practice more find algorithm how to do it and try to implement it. 

#USE ANY HELP YOU WANT (INTERNET, BOOKS) BUT PLEASE DO NOT COPY CODE, BUT REWRITE IT BY YOUR SELF LETER BY LETER.

import random


def main():
    numbers_list = []
    random_number = random.randint(0, 100)

    while len(numbers_list) == 19:
    numbers_list.append(random_number)
    print(numbers_list)


if __name__ == "__main__":
    main()