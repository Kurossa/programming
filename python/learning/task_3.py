#!/usr/bin/python3
#Create proper python file with main function.

#Create main function that will ask for two numbers, and it will say which is bigger. Create function for checkin those vairables. If it will be not too hard. Put one variable as global and put any value you want.
#Program can ask in loop all time "Gess number, enter your guese:" till user will find out what is number you put.

#USE ANY HELP YOU WANT (INTERNET, BOOKS) BUT PLEASE DO NOT COPY CODE, BUT REWRITE IT BY YOUR SELF LETER BY LETER.
import random


def searching_number(random_n):
    print('Gues a number:')
    number_s = input()
    if (not number_s.isnumeric()):
        print('Give a nnumber you jerk.')
        return True
    number_s = int(number_s)
    if number_s > random_n:
        print("The number you're looking for is to big.")
        return True
    elif number_s < random_n:
        print("The number you're looking for is to small.")
        return True
    else:
        print("Congratulations! This is the number!")
        return False


def multiply_numbers(num_1, num_2):
    error = 'No Error'
    if( not num_1.isnumeric()):
        print('You gave not a number as 1st parameter')
        return 'Error: 1st param is not a number'
    if ( not num_2.isnumeric()):
        print('You gave not a number as 2nd parameter')
        return 'Error: 2nd param is not a number'
    return num_1*num_2

#HIGHLIGHT LINES AND USE CTRL+/ TO QUICKLY COMMENT/UNCOMMENT IN PYCHARM

# main using "while" for number of tries
# def main():
#     random_number = random.randint(0,9)
#     tries = 3
#     print('You have ',tries,' tries')
#     while tries > 0:
#         if searching_number(random_number) == False:
#             break
#         tries -= 1
#         if tries == 0:
#             print('Game over. You failed to guess a number. Searched number was:',random_number)
#         else:
#             print ('Try again. You have ',tries,' tries left')



#main using "for" for number of tries
def main():
    random_number = random.randint(0, 9)
    tries = 3
    for i in reversed(range(tries)):
        print('You have ',i+1,'tries left')
        if searching_number(random_number) == False:
            break
        if i == 0:
            print('Game over. You failed to guess a number. Searched number was:',random_number)



    print('End of transmission...')


if __name__ == "__main__":
    main()

    ret_value = multiply_numbers('123','123kk')
    if(ret_value.isnumeric()):
        print(ret_value)
    else:
        print('You did something wrong, error comment %s' % ret_value)