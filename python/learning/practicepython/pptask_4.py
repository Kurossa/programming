#!/usr/bin/python3

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


def main():
    num = int(input("Enter a number: "))
    # work_num = number
    # div_list = []
    # while work_num.is_integer():
    #     #print(number)
    #     div_list.append(work_num)
    #     work_num = float(work_num/2)
    #
    # print("List of divisors of number",number, div_list[1:])

    list_range = list(range(1, num + 1))

    divisor_list = []

    for number in list_range:
        if num % number == 0:
            divisor_list.append(number)

    print(divisor_list)


if __name__ == "__main__":
    main()