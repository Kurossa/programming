#!/usr/bin/python3
import sys



def print_function(args_num=0):

    print('Hello World! with',args_num,'arg(s).')
    for i in range(args_num):
        print (sys.argv[i],'\n')



# This allows the file to be used as a SCRIPT
if __name__ == "__main__":





    print_function(len(sys.argv))
