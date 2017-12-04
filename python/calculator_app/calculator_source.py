#!/usr/bin/python3

import sys, math

def filter_char(input_char):
    allowed_chars = '1234567890.+-*/=c'
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

def multi_dot_filter(number_2, char): #filter preventing from appear more than one decimal point in number (only first decimal point is correct)
    if number_2 == '':
        number_2 += char
    else:
        if '.' in number_2 and char == '.':
            number_2 += ''
        else:
            number_2 += char
    return number_2

def get_value_to_display(number_2):
    return number_2

class CalculatorEngine:

    def __init__(self):
        self.alow_numbers = '1234567890.'
        self.alow_operations = '+-*/='
        self.operation = ''
        self.number_2 = ''
        self.number_1 = ''
        self.result = ''
        self.clear = 'c'

    def chars_process(self, str_list):
        for char in str_list:
            if char == self.clear:  #clearing process if 'c' pressed
                self.operation = ''
                self.number_2 = ''
                self.number_1 = ''
                self.result = ''
            if char in self.alow_numbers: #creating a number
                self.number_2 = multi_dot_filter(self.number_2, char)
            if char in self.alow_operations:
                if self.number_2 == '':
                    self.operation = char
                else:
                    if char == '=': #main calculation
                        if self.number_1 and self.number_2 != '':
                            self.result = calculation(self.number_2, self.number_1, self.operation)
                            self.number_1 = self.result
                        else:
                            self.number_2 = ''
                    else: #calculation is done even if +-*/ operations are entered
                        if self.number_1 != '':
                            self.result = calculation(self.number_2, self.number_1, self.operation)
                            self.number_1 = self.result
                        else:
                            self.number_1 = self.number_2
                        get_value_to_display(self.number_2)
                        self.operation = char
                    self.number_2 = ''
        return self.result

def main():

    # str_1 = '1123..8786.123++234=234===234=234+234='
    # calc = CalculatorEngine()

    str_1 = '54*15-3/*-8=+51=2+3='
    calc = CalculatorEngine()

    print(get_value_to_display(get_value_to_display(keyboard_filter(str_1))))
    output2 = calc.chars_process(keyboard_filter(str_1))
    print(output2)

if __name__ == "__main__":
    main()