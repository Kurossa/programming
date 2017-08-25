#!/usr/bin/python3

from task_7a import RandomPerson
import sys, getopt


def print_help():
    print('Help:')
    print('task_7_main.py -a <array size (must be a number!)>')

def parse_args(argv):
    try:
        opts, args = getopt.getopt(argv, 'ha:', ['help', 'array size='])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    is_input_value = False
    input_value = ''

    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt in ('-a', '--array size'):
            is_input_value = True
            input_value = argv

        return input_value, is_input_value

def arg_check(parse_args):
    arg = parse_args[0]
    array_size = arg[1]
    if array_size.isdigit():
        return int(array_size)
    else:
        print_help()
        sys.exit(2)

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

def main(argv):
    list_size, parse_ok = parse_args(argv)
    array_size = arg_check(parse_args(argv))
    if parse_ok:
        persons_list = get_random_persons_list(array_size)
        sort_and_print(persons_list)
    else:
        print_help()

    # persons_list = get_random_persons_list(array_size, RandomPerson(['Ann', 'Marry', 'Helen'] , ['Doe', 'Unknown', 'Prince'] , 30, 50, 150, 180))
    # sort_and_print(persons_list)


if __name__ == "__main__":
    main(sys.argv[1:])