#!/usr/bin/python3

import sys, math

def keyboard_filter(str_list):
    allowed_chars = '1234567890.+-*/='
    buffer =''

    for char in str_list:
        for allowed_char in allowed_chars:
            if char == allowed_char:
                buffer += char

    return buffer

def chars_process(str_list):
    alow_numbers = '1234567890.'
    alow_operations = '+-*/='
    operation = ''
    number_2 =''
    number_1 = ''


    for char in str_list:
        if char in alow_numbers:
            number_2 += char
        if char in alow_operations:
            number_1 = number_2
            number_2 = ''
            operation = char
            #break

    return number_1, number_2, operation

def main_operations(number_2, number_1, operation):
    number_2 = float(number_2)
    number_1 = float(number_1)

    if operation == '+':
        number_2 + number_1
    elif operation == '-':
        number_2 - number_1
    elif operation == '*':
        number_2 * number_1
    elif operation == '/':
        number_2 / number_1

def main():
    test_str = "et3e;tg5gerghez43t"

    output = keyboard_filter(test_str)
    print(output)

    test_str2 = 'dw3.4+sr5nyt3*gds8bv'
    print(keyboard_filter(test_str2))

    output2 = chars_process(keyboard_filter(test_str2))
    print(output2)

if __name__ == "__main__":
    main()