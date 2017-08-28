#!/usr/bin/python3

import sys, getopt, zipfile

def print_help():
    print('Help:')
    print_help('zip_task.py -z <zip file> -f <zip decompression folder>')

def parse_args(argv):
    try:
        opts, args = getopt.getopt(argv, 'hz:f:', ['help', 'zipfile=', 'folder='])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    is_zipfile = False
    is_folder = False

    zipfile = ''
    folder = ''

    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt in ('-z', '--zipfile'):
            is_zipfile = True
            zipfile = arg
        elif opt in ('-f', '--folder'):
            is_folder = True
            folder = arg

        return zipfile, folder, (is_zipfile and is_folder)

def main():
    #zipfile, folder, parse_ok = parse_args(argv)

    # zf = zipfile.ZipFile
    # zf.open('example.zip', mode = 'r', pwd = None)
    # zf.extractall(path = None, members = None, pwd = None)
    # zf.close()

    with zipfile.ZipFile('example.zip', 'r') as zf:
        data = zf.namelist()
        print(data)




if __name__ == '__main__':
    main()