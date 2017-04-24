#!/usr/bin/python3
# first task for python practising purposes

#Create proper python file with main function.

#Creat function that will create variables of all known types with any value you want. i.e. int, float etc. Print those values and print those variables types using python functions.

#USE ANY HELP YOU WANT (INTERNET, BOOKS) BUT PLEASE DO NOT COPY CODE, BUT REWRITE IT BY YOUR SELF LETER BY LETER.

def main():
    var_string = 'hello world'
    var_int = 97
    var_float = 3.14
    var_bool = True
    one = '-'

    var_print_summmary = "Value is: " + var_string.capitalize() + " And when you shout it look like: " \
                         + var_string.upper() + " You can spell it like: " + var_string.zfill(15) + " type of: " \
                         + str(type(var_string)) + "  " + str(var_int) + "  " + str(ord('a')) +chr(var_int) + str(var_int).zfill(5)


    print(var_print_summmary)
    print(var_string,type(var_string))

    print(var_int, type(var_int))
    # 123.1239729835743948573984573894
    # 123.12
    # 000123.123
    var_print_summmary = "Value is: " + str(var_float) + " type of: ", type(var_float)
    print(var_print_summmary)
    print(var_float, type(var_float))
    print(var_bool, type(var_bool))
    char = 3
    print(char)
    print(type(char))


if __name__ == "__main__":
    main()
