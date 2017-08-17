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
        return str(self.age)

    def get_height(self):
        return self.height

#    def __str__(self):
#        return 'Person'

class RandomPerson:

    def get_name(self):
        names = ['Andrzej', 'Michał', 'Monika', 'Iza', 'Piotr']
        random_name = random.choice(names)
        return random_name

    def get_surname(self):
        surnames = ['Kowalik', 'Gad', 'Nowak', 'Rogala', 'Kwiecień']
        random_surname = random.choice(surnames)
        return random_surname

    def get_age(self):
        age = random.randint(20, 70)
        return age

    def get_height(self):
        height = random.randint(160, 210)
        return height

def main():
#    rand_person = RandomPerson()
#    person_info = Person()
    persons_quantity = 10
    rand_person = RandomPerson()

    def get_persons_full():
        person = Person(rand_person.get_name(), rand_person.get_surname(), rand_person.get_age(),
                            rand_person.get_height())
        return person

    # def get_person():
    #     rand_person = RandomPerson()
    #     person = Person(rand_person.get_name(), rand_person.get_surname(), rand_person.get_age(), rand_person.get_height())
    #     person_full = person.get_name(), person.get_surname(), person.get_age(), person.get_height()
    #     #person_dic = {'n':person_full[0], 's':person_full[1], 'a':person_full[2], 'h':person_full[3]}
    #     return person_full

    def get_persons_list():
        persons_list = []
        person_full = get_persons_full()
        for i in range(persons_quantity):
            persons_list.append(person_full)
        return persons_list

    persons_true = get_persons_list()
    print(sorted(persons_true, key=lambda person: person.get_age()))
    print(sorted(persons_true, key=lambda person: person.get_height()))

    # for i, n in enumerate(sorted(persons_true, key=lambda person: person.get_age())):
    #         list_numbered = i+1, n
    #         list_numbered = str(list_numbered)
    #         list_numbered = list_numbered.replace('(', '').replace(')', '').replace("'", "").replace(',', '')
    #         print(list_numbered)

    print(list(enumerate(sorted(persons_true, key=lambda person: person.get_age()), start=1)))

if __name__ == "__main__":
    main()