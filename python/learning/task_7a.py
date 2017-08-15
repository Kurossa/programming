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
import random

class Person:

    def __init__(self, name, surname, age, height):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height

    def __repr__(self):
        return repr((self.name, self.surname, self.age, self.height))

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_age(self):
        return self.age

    def get_height(self):
        return self.height

class RandomPerson:
    def __init__(self,
                 names_list = ['Andrzej', 'Michał', 'Monika', 'Iza', 'Piotr'],
                 surname_list = ['Kowalik', 'Gad', 'Nowak', 'Rogala', 'Kwiecień'],
                 age_min = 20,
                 age_max = 70,
                 height_min = 160,
                 height_max = 210):
        self.names = names_list
        self.surnames = surname_list
        self.age_min = age_min
        self.age_max = age_max
        self.height_min = height_min
        self.height_max = height_max

    def get_name(self): 
        return random.choice(self.names)

    def get_surname(self): 
        return random.choice(self.surnames)

    def get_age(self):
        age = random.randint(self.age_min, self.age_max)
        return age

    def get_height(self):
        height = random.randint(self.height_min, self.height_max)
        return height

    def get_random_person(self):
        return Person(self.get_name(), self.get_surname(), self.get_age(), self.get_height())


def get_random_persons_list(length, random_person = RandomPerson()):
    persons_list = []
    for i in range(length):
        person = random_person.get_random_person()
        persons_list.append(person)
    return persons_list


def print_persons_list(persons_list):
    for i in range(len(persons_list)):
        print('Person No' + str(i) +
              ': Name: ' + persons_list[i].get_name() +
              ' ' + persons_list[i].get_surname() +
              ', age: ' + str(persons_list[i].get_age()) + 
              'years, height: ' + str(persons_list[i].get_height()) + 'cm')


def sort_and_print(persons_list):
    persons_list_sorted_by_age = sorted(persons_list, key=lambda person: person.get_age())
    persons_list_sorted_by_height = sorted(persons_list, key=lambda person: person.get_height())

    print('Random Persons list:')
    print_persons_list(persons_list)
    print('Sorted by age:')
    print_persons_list(persons_list_sorted_by_age)
    print('Sorted by height:')
    print_persons_list(persons_list_sorted_by_height)


def main():
    persons_list = get_random_persons_list(10)
    sort_and_print(persons_list)

    persons_list = get_random_persons_list(10, RandomPerson(['Ann', 'Marry', 'Helen'] , ['Doe', 'Unknown', 'Prince'] , 30, 50, 150, 180))
    sort_and_print(persons_list)


if __name__ == "__main__":
    main()