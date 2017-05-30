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


    def random_list (self):
        numbers_list = []
        for i in range(self.list_length):
            numbers_list.append(random.randint(self.min, self.max))
        #print(self.numbers_list)
        return numbers_list


    def sort_list(self, list_to_sort):
        numbers_list = list_to_sort
        sorted_list = []
        while numbers_list:
            minimum = numbers_list[0]
            for i in numbers_list:
                if i <= minimum:
                    minimum = i
            sorted_list.append(minimum)
            numbers_list.remove(minimum)
        return sorted_list


def main():
    sort_list_obj = MakeSortList(0, 100, 20)
    my_numbers = sort_list_obj.random_list()
    print(my_numbers)
    my_numbers = sort_list_obj.sort_list(my_numbers)
    print(my_numbers)


if __name__ == "__main__":
    main()