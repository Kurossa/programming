#!/usr/bin/python3
#Create proper python file with main function.

# Create array (list) of 20 items with random numbers from 0 to 100. Than make function taht will get list and return sorted one. In python for sure there is some list function that will sort it. 
# But to practice more find algorithm how to do it and try to implement it. 

#USE ANY HELP YOU WANT (INTERNET, BOOKS) BUT PLEASE DO NOT COPY CODE, BUT REWRITE IT BY YOUR SELF LETER BY LETER.

import random


class MakeSortList:

    def __init__(self, range_min, range_max,list_lenght):
        self.min = range_min
        self.max = range_max
        self.list_length = list_lenght
        self.numbers_list = []


    def random_list (self):
        for i in range(self.list_length):
            self.numbers_list.append(random.randint(self.min, self.max))
        print(self.numbers_list)


    def sort_list(self):
        numbers_list = self.numbers_list
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
    list = MakeSortList(0, 100, 20)
    list.random_list()
    list.sort_list()


if __name__ == "__main__":
    main()