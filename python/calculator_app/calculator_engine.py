#!/usr/bin/python3
import sys
import math

number_1 = 5
number_2 = 5
math_result = ''

def insert_char(char):
    if char == 'd':
        return
    print(str(char))
    if char == '+':
        print('Dzialanie dodawania')
    #math_result += 'Test'
    number_1 = 5

def get_result_str():
    print(str(number_1))
    return math_result




def main():
    test_str = '100.3+10='
    for single_char in test_str:
        insert_char(single_char)

    get_result_str()

# This allows the file to be used as a SCRIPT
if __name__ == "__main__":
    main()

