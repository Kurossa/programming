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

def main():
    with open('lotto.txt') as file:
        #read_data = file.read(8)
        read_line = file.readline(1)
        #print(read_data)
        print(read_line)

if __name__ == '__main__':
    main()