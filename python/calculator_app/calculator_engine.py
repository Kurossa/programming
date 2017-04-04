#!/usr/bin/python3
import sys
import math

buffer = ''
operation = ''
number_1 = 0.0
number_2 = 0.0
math_result = 0.0
# Allowed characters for numbers
# 0123456789.
# Allowed functions
# +-*/=

def filter_char(char):
    global number_1
    return char
    # if char == 1234567890.-+*/=
    #   return char
    # else
    #   return ''


def proccess_char(char):
    global buffer
    global number_1
    global number_2
    global operation
    global math_result

    allowed_chars_for_number = '1234567890.'
    is_char_allowed_for_number = False

    for allowed_char in allowed_chars_for_number:
        if allowed_char == char:
            is_char_allowed_for_number = True
            break

    if is_char_allowed_for_number:
        buffer += char      # 43575
    else:                   #only for other signs +-*/=
        if operation == '':
            number_1 = float(buffer)
            buffer = ''
            operation = char
        else:
            number_2 = float(buffer)
            #print(number_1)
            #print(number_2)
            math_result = claculate(number_1, number_2, operation)
            #print(math_result)
            operation = char
            buffer = ''
            number_1 = math_result


def claculate(num_1, num_2, op):
    # can be +-*/=
    #print('Result of ' + op + ' :')
    if op == '+':
        return num_1 + num_2
    elif op == '-':
        return num_1 - num_2
    elif op == '*':
        return num_1 * num_2
    elif op == '/':
        return num_1 / num_2





def get_result_str():
    print(str(math_result))
    return math_result


def main():
    test_str2 = '2343sdfg+4dfg3575-sdfg22+123sdfg*2/sdfg1sdfg2'
    test_str3 = ''
    for single_char in test_str2:
        test_str3 += filter_char(single_char)

    print(test_str2)
    print(test_str3)


    test_str = '2343+43575-22+123*2/12'
    print('Is same as?')
    print(test_str)

    for single_char in test_str:
        proccess_char(single_char)

    get_result_str()


# This allows the file to be used as a SCRIPT
if __name__ == "__main__":
    main()