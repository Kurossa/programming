#!/usr/bin/python3

# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
#     If the number is a multiple of 4, print out a different message.
#     Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


def main():
    user_number = input("Please, enter number: ")
    user_number = int(user_number)/2
    if user_number is int:
        print("The number you've passed is even")
    else:
        print("The number you've passed is odd")


if __name__ == "main":
    main()