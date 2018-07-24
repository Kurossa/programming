#!/usr/bin/python3


#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)



def main():

    user_input = input("Enter: ")

    print(user_input)
    table_one = user_input[::-1]

    print(table_one)



if __name__ == "__main__":
    main()