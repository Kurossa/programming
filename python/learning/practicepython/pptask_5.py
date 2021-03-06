#!/usr/bin/python3

# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
#
# Extras:
#
#     Randomly generate two lists to test this
#     Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)


import random


def compare_lists(list_a, list_b):

    empty_list = []
    for every_elm in list_a:
        if every_elm in list_b:
            empty_list.append(every_elm)

    list.sort(empty_list)
    return empty_list


def main():


    # list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    # list_to_compare = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    #
    # list_of_same_num = []
    #
    # for every_elm in list_a:
    #     if every_elm in list_to_compare:
    #         list_of_same_num.append(every_elm)

    #print(list_of_same_num)



    random_list_a = random.sample(range(101), random.randrange(20))
    random_list_b = random.sample(range(101), random.randrange(20))

    print(random_list_a)
    print(random_list_b)

    print(compare_lists(random_list_a, random_list_b))






if __name__ == "__main__":
    main()