#!/usr/bin/python3


import random
from task_7a import Person
from task_7a import RandomPerson



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