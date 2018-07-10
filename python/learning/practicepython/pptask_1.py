#!/usr/bin/python3

# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
# Extras:
#
#     Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#     Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)




def year_count(age):
    age = (int(age))
    year = 2017 - age + 100
    return str(year)

def main():
    print("Tell me your age and I'll show you a year of your 100 birthday: ")
    age = input()
    if age.isnumeric():
        year_summary = "Your 100 birthday will be in: " + year_count(age)
        print(year_summary)
    else:
        #lines = input("How many times I need to tell you this?: ")
        print("You need to put numbers only!")



if __name__ == "__main__":
    main()