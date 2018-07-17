#!/usr/bin/python3



# Take a list, say for example this one:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
#     Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#     Write this in one line of Python.
#     Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


def main():
    list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list_to_add = []
    number = input("Enter a number. It will show only elements below that number: ")
    for i in list:
        if i < int(number):
            list_to_add.append(i)

    print(list_to_add)


if __name__ == "__main__":
    main()