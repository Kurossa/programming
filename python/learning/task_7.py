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

    def get_name(self):
        return str(self.name)

    def get_surname(self):
<<<<<<< HEAD
        return str(self.surname)+':'
=======
        return str(self.surname)+': '
>>>>>>> 65898fcd131511f2369334adeb2a14e4212de4cf

    def get_age(self):
        return str(self.age)+' lat'

    def get_height(self):
        return str(self.height)+' cm'

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
<<<<<<< HEAD
#    rand_person = RandomPerson()
#    person_info = Person()
    persons_quantity = 10


    def get_person():
        rand_person = RandomPerson()
        person = Person(rand_person.get_name(), rand_person.get_surname(), rand_person.get_age(), rand_person.get_height())
        person_full = person.get_name(), person.get_surname(), person.get_age(), person.get_height()
        #person_dic = {'n':person_full[0], 's':person_full[1], 'a':person_full[2], 'h':person_full[3]}
        return person_full

    def get_persons_list():
        persons_list = []
        for i in range(persons_quantity):
            persons_list.append(get_person())
        return persons_list

    for i, n in enumerate (get_persons_list()):
        print(i+1, n)

    #print(get_person())
    #print(get_persons_list())

=======
    lukasz = Person('Łukasz', 'Glab', 36, 178)
    print(lukasz.get_name())

    rand_person = RandomPerson()
    personslist = []
    persons_quantity = 10
    for i in range(persons_quantity):
        person = Person(rand_person.get_name(), rand_person.get_surname(), rand_person.get_age(),
                         rand_person.get_height())
        person_full = i+1, person.get_name(), person.get_surname(), person.get_age(), person.get_height()
#        person_full = str(person_full)
        personslist.append(person_full)
    print(personslist)
>>>>>>> 65898fcd131511f2369334adeb2a14e4212de4cf


if __name__ == "__main__":
    main()