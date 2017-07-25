#!/usr/bin/python3

# Subtask 1
#
# Create 2 class
# 1st class will by named Person and during creation you will pass name, surename, age, height i.e. person1 =  Person('Marek', Kowalski, 33,183) . 
# It will have 4 methods to get, name, surename, age, height i.e. GetName() 
#
# 2nd class RandomPerson will contains 2 lists one containing list of some names ie names = {'Marel', 'Agnieszka', 'Tomek'} and list of some surnames.
# It will have 4 methods GetRandomName, GetRandomSurname, GetRandomAge, GetRandomHeight
# GetRandomName will return random name from name list
# GetRandomSurname will return random surname from surename list
# GetRandomAge will return age from range 20 - 70
# GetRandomAge will return height from range 160-210
#
# Subtask 2
#
# Create list of 10 Persons class created using RandomPerson 
#
# Subtask 3
# 
# Create function that will print all persons from list
# Using for loop print all 10 persons
# i.e.
# 1. Marek Kowalski: 38 lat, 183 cm
# 2. Agnieszka Nowak: 20 lat, 200 cm
# ...
#
# Subtask 4
#
# Create function to sort person list by age and print that list using function from subtask 3
# 
# Subtask 5
#
# Create function to sort person list by height and print that list using function from subtask 3
#
class Person:

    def __init__(self, name, surname, age, height):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_age(self):
        return self.age

    def get_height(self):
        return self.height

#    def __str__(self):
#        return 'Person'

def main():
    lukasz = Person('Łukasz', 'Glab', 36, 178)
    print(lukasz.get_height())

if __name__ == "__main__":
    main()