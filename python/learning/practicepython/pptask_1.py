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
    #print("Tell me your age and I'll show you a year of your 100 birthday: ")
    age = input("Tell me your age and I'll show you a year of your 100 birthday: ")
    while not age.isnumeric():
        print("Age needs to be a number!")
        age = input("Tell me your age and I'll show you a year of your 100 birthday: ")
    else:
        display_count = input("How many times I need to tell you that?: ")
        year_count(age)
        for i in range(int(display_count)):
            print("You'll be 100 year old in: ", year_count(age))


if __name__ == "__main__":
    main()