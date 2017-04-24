#!/usr/bin/python3
#Create proper python file with main function.
#Create function that will ask you severeal question, of name, age, etc. Put users answer to variables. Put together answer as a one string an than print it in one command.

#Example.
#Ask for dogs name?
dogs_name = 'Foksik'
#Ask for dog age?
dogs_age = 2.0
#
print('Give me your name:')
my_name = input()
my_name = my_name.capitalize()
print(my_name)
#my_name = my_name.split(' ',5)
print('Czesc ' + my_name[0])
# this is only example try to do it, like in example, but also try to use formating it looks like 'Your name is: {0} and age of {1}'.Format(dogs_name,dogs_age) or any other way you like.
reply2 = 'Your dogs name is: {0} and age of {1}'.format(dogs_name, dogs_age)
print(reply2)
reply = 'Your dogs name is: ' + dogs_name + ' and its: ' + str(dogs_age) + ' years old'
print(reply)

int_number = 6
pi = 3.14159
print(' pi = %2.1f, int numbr = %+5d ' % (pi, int_number))

print('{1} {0} {2}'.format(dogs_age,dogs_name,my_name))

print('tu ma być allign')



#Do it for few examples, questions does not matters. You can play with diffrent build-in python functions for strings. Pleas see documentation for strings in Python:
#https://docs.python.org/3/library/string.html


#USE ANY HELP YOU WANT (INTERNET, BOOKS) BUT PLEASE DO NOT COPY CODE, BUT REWRITE IT BY YOUR SELF LETER BY LETER