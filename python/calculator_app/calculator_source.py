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

def operation_return(char, operation, last_operation):

    if operation != '=':
        operation = last_operation
    else:
        last_operation = operation
        operation = char

    return operation, last_operation


class CalculatorEngine:

    def __init__(self):
        #Calculation variables
        self.allowed_numbers = '1234567890.'
        self.allowed_operations = '+-*/='
        self.operation = ''
        self.last_operation = ''
        self.number_2 = ''
        self.number_1 = ''
        self.result = ''
        self.clear = 'c'
        # Display variables
        self.operation_pressed = True
        self.display = '0'


    def chars_process(self, str_list):
            for char in str_list:
                if char == self.clear:  #clearing process if 'c' pressed
                    #Calculate result
                    self.operation = ''
                    self.last_operation = ''
                    self.number_2 = ''
                    self.number_1 = ''
                    self.result = ''
                    #Prepare display value
                    self.display = '0.0'
                    self.operation_pressed = True
                if char in self.allowed_numbers: #creating a number
                    #Calculate result
                    self.number_2 = multi_dot_filter(self.number_2, char)
                    #Prepare display value
                    if self.operation_pressed:
                        self.display = ''
                        self.operation_pressed = False
                    self.display = multi_dot_filter(self.display, char)
                if char in self.allowed_operations:
                    if self.number_2 == '':
                        self.operation = char
                        self.display = char
                    else:
                        if char == '=': #main calculation
                            #Calculate result
                            if self.number_1 and self.number_2 != '':
                                self.result = calculation(self.number_2, self.number_1, self.operation)
                                self.number_1 = self.result
                                self.display = self.result
                            else:
                                self.number_2 = ''
                            #Prepare to display
                                self.display = char
                        else: #calculation is done even if +-*/ operations are entered
                            #Calculate result
                            if self.number_1 != '':
                                self.result = calculation(self.number_2, self.number_1, self.operation)
                                self.number_1 = self.result
                            else:
                                self.number_1 = self.number_2
                                self.display = self.result
                            #self.operation = char
                            self.operation, self.last_operation = operation_return(char, self.operation, self.last_operation)

                        #Prepare to display
                            self.display = char
                        self.number_2 = ''
                        self.operation_pressed = True
            return self.result

    # def chars_process2(self, kb_input, result):
    #     kb_input = keyboard_filter(kb_input)
    #     for char in kb_input:
    #         if char in self.allowed_numbers:
    #             if self.operation_pressed:
    #                 self.display = ''
    #                 self.operation_pressed = False
    #             self.display = multi_dot_filter(self.display, char)
    #         elif char in self.allowed_operations:
    #             if kb_input == '=':
    #                 # Calculate result
    #                 # sdfsdfdsf
    #
    #                 # Prepare display value
    #                 self.display = result
    #             else:
    #                 # Calculate result
    #                 # sdfsdfdsf
    #
    #                 # Prepare display value
    #                 self.display = char
    #             self.operation_pressed = True
    #         elif char == self.clear:
    #             # Calculate result
    #             # sdfsdfdsf
    #
    #             # Prepare display value
    #             self.display = '0'
    #             self.operation_pressed = True
    #         else:
    #             print('Error')
    #
    #     return self.display

    def get_value_to_display(self):
        return self.display


def main():

    # str_1 = '1123..8786.123++234=234===234=234+234='
    # calc = CalculatorEngine()

    str_1 = '54*15-3/*-8=+51=2+3='
    calc = CalculatorEngine()

    output2 = calc.chars_process(keyboard_filter(str_1))
    print(output2)

if __name__ == "__main__":
    main()