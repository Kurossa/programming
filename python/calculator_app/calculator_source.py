#!/usr/bin/python3

import sys, math

def filter_char(input_char):
    allowed_chars = '1234567890.+-*/='
    if(type(input_char) == str):
        if(len(input_char)==1):
            if input_char in allowed_chars:
                return input_char
    return ''

def keyboard_filter(str_list):
    buffer =''
    for char in str_list:
        char = filter_char(char)
        buffer += char
    return buffer

def calculation(number_2, number_1, operation):
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
    else:
        return 'Error operation'

def multi_dot_filter(number_2, char):
    if number_2 == '':
        number_2 += char
    else:
        if '.' in number_2 and char == '.':
            number_2 += ''
        else:
            number_2 += char

    return number_2

class CalculatorEngine:

    def __init__(self):
        self.alow_numbers = '1234567890.'
        self.alow_operations = '+-*/='
        self.operation = ''
        self.number_2 = ''
        self.number_1 = ''
        self.result = ''

    def chars_process(self, str_list):
        for char in str_list:
            if char in self.alow_numbers:
                self.number_2 = multi_dot_filter(self.number_2, char)
            if char in self.alow_operations:
                if self.number_2 == '':
                    self.operation = char
                else:
                    if char == '=':
                        # if self.operation == '=':
                        #     self.number_2 = ''
                        if self.number_1 and self.number_2 != '':# and self.operation != '=':
                            self.result = calculation(self.number_2, self.number_1, self.operation)
                            self.number_1 = self.result
                        else:
                            self.number_2 = ''
                    else:
                        if self.operation == '=':
                            #self.operation = char
                            self.number_2 = ''
                        else:
                            if self.number_1 != '':
                                self.result = calculation(self.number_2, self.number_1, self.operation)
                                self.number_1 = self.result

                            else:
                                self.number_1 = self.number_2
                        self.operation = char

                    #self.operation = char
                    self.number_2 = ''

        return self.result

def main():
    #test_str = "et3e;tg5gerghez43t"

    #output = keyboard_filter(test_str)
    #print(output)

    #test_str2 = 'dw34+sr5nyt.3*gds8bv-yf5k====;+98-8'
    #test_str2 = '123+123='
    #print(keyboard_filter(test_str2))

    # str_1 = '1123..8786.123++234=234===234=234+234='
    # calc = CalculatorEngine()

    str_1 = '54*15-3/*-8=+51==='
    calc = CalculatorEngine()

    output2 = calc.chars_process(keyboard_filter(str_1))
    print(output2)


    #
    # calculation = main_operations(second_number, first_number, op)
    # print(calculation)

if __name__ == "__main__":
    main()