#!/usr/bin/python3

#Main task of this excercise is to practice opening, reading and writing files
#It's based on "Super pensja" Lotto game. The 'lotto.txt' file includes two columns of numbers: a number (marked with -,
#for example '-01-') and in the same row, information how many times that number was drawn (marked with =,for example
#'=24=').
#
#While executing lotto.py file with -s argument, it will display all 35 numbers sorted by the most drawn one.
#
#But while executing lotto.py with -x argument and giving 5 numbers (separated by space) it will add +1 to the
#=drawn number= to each number we gave after -x argument. This operation will update lotto.txt with the lates draw.

import re, random, sys, getopt
from operator import itemgetter

def print_help():
    print('Help:')
    print('lotto.py -l (prints sorted list)')
    print('lotto.py -d <numbers separated by space> (adds the latest draw)')

class LottoDraw:
    def __init__(self, file):
        self.file = file


    def update_draw(self, value):
        lotto_file = self.file
        number = value
        # line = None
        # new_line = None
        with open(lotto_file) as file:
            for line in file:
                match = re.search('-' + number + '-', line)
                if match:
                    main_number = line[1:3]
                    main_number_count = line[5:7]
                    main_number_count = int(main_number_count)+1
                    main_number_count = str(main_number_count)
                    new_line = ('-' + main_number + '-' + '=' + main_number_count + '=\n')
                    self.write_to_file(line, new_line)
                    #return self.line, self.new_line

    def write_to_file(self, line, new_line):
        old_line = line
        new_line = new_line
        with open(self.file, 'r') as file:
            file = file.read()

        new_file_data = file.replace(old_line, new_line)

        with open(self.file, 'w') as file:
            file.write(new_file_data)


    def get_list(self):
        lotto_file = self.file
        match_list = []
        with open(lotto_file) as file:
            for line in file:
                match = re.search(r'-..-', line)
                match2 = re.search(r'=..=', line)
                data = match.group()[1:3:], match2.group()[1:3:]
                match_list.append(data)
        return match_list


    def print_sort_numbers(self):
        numbers = self.get_list()
        numbers_sorted = sorted(numbers, reverse=True, key=itemgetter(1))
        for i in numbers_sorted:
            print('Number:', i[0], ' Quantity:', i[1])


class ParseArgs:

    def __init__(self):
        self.is_input_value = False
        self.is_input_is_a_list = False
        self.draw_value = ''



    def parse_args(self, lotto_draw, argv):
        try:
            opts, args = getopt.getopt(argv, 'hld:', ['help', 'list_sorted', 'draw_value'])
        except getopt.GetoptError:
            print_help()
            sys.exit(2)

        print (opts)
        print (args)
        print(argv)

        for opt, arg in opts:
            print(opt)
            print(arg)
            if opt == '-h':
                print_help()
                sys.exit()
            elif opt == '-l':
                #self.is_input_is_a_list = True
                lotto_draw.print_sort_numbers()
            elif opt in ('-d', '--draw'):
                self.is_input_value = True
                self.draw_value = arg
                lotto_draw.update_draw(arg)
            else:
                print_help()
                sys.exit(2)

        #return self.draw_value, self.is_input_value, self.is_input_is_a_list

def main(argv):

    # lotto_draw = LottoDraw('lotto.txt')
    # for i in range(100):
    #     lotto_draw.update_draw(str(random.randrange(1,35)))
    # lotto_draw.print_sort_numbers()

    parse_task = ParseArgs()
    lotto_draw = LottoDraw('lotto.txt')
    parse_task.parse_args(lotto_draw, argv)
    # if list_print:
    #     lotto_draw.print_sort_numbers()
    # elif draw_numbers and parse_ok:
    #     lotto_draw.update_draw(draw_numbers)
    # else:
    #     print_help()
    #     sys.exit(2)

if __name__ == '__main__':
    main(sys.argv[1:])