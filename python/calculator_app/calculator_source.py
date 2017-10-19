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

def main_operations(number_2, number_1, operation):
    number_2 = float(number_2)
    number_1 = float(number_1)

    if operation == '+':
        return str(number_1 + number_2)
    elif operation == '-':
        return str(number_1 - number_2)
    elif operation == '*':
        return str(number_1 * number_2)
    elif operation == '/':
        return str(number_1 / number_2)
    elif operation == '=':
        return str(number_1)

def chars_process(str_list):
    alow_numbers = '1234567890.'
    alow_operations = '+-*/='
    operation_1 = ''
    operation_2 = ''
    number_2 = ''
    number_1 = ''

    for char in str_list:
        if char in alow_numbers:
            number_2 += char
        if char in alow_operations:
            operation_1 = char
            if number_1 == '' and operation_2 == '':
                number_1 = number_2
                operation_2 = operation_1
                number_2 = ''
                operation_1 = ''
            else:
                number_2 = main_operations(number_2, number_1, operation_2)
                number_1 = number_2
                operation_2 = operation_1
                number_2 = ''
                operation_1 = ''

    return number_2, number_1,

def main():
    test_str = "et3e;tg5gerghez43t"

    output = keyboard_filter(test_str)
    print(output)

    test_str2 = 'dw34+sr5nyt.3*gds8bv-yf5k=;kh90uo+89+979'
    print(keyboard_filter(test_str2))

    output2 = chars_process(keyboard_filter(test_str2))
    print(output2)
    #
    # calculation = main_operations(second_number, first_number, op)
    # print(calculation)

if __name__ == "__main__":
    main()