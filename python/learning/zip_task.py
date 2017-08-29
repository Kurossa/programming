#!/usr/bin/python3

import sys, getopt, zipfile

def print_help():
    print('Help:')
    print('zip_task.py -z <zip file> -f <zip decompression folder>')

def parse_args(argv):
    try:
        opts, args = getopt.getopt(argv, 'hz:f:', ['help', 'zipfile=', 'folder='])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    is_zipfile = False
    is_folder = False

    zip_file = ''
    folder = ''

    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt in ('-z', '--zipfile'):
            is_zipfile = True
            zip_file = arg
        elif opt in ('-f', '--folder'):
            is_folder = True
            folder = arg

        return zip_file, folder, (is_zipfile and is_folder)

def extraction(zip_file, extract_folder):
    file = zip_file
    folder = extract_folder
    z = zipfile.ZipFile(file, 'r')
    for name in z.namelist():
        z.extract(name, folder)
        print('The file named:',file,', has been extracted to:',folder, 'folder')

def main():
    zip_file = "example.zip"
    folder = "example"

    extraction(zip_file, folder)

    # zip_file, folder, parse_ok = parse_args(argv)
    # if parse_ok:
    #     extraction(zip_file, folder)
    # else:
    #     print_help()
    #     sys.exit(2)

    # zf = zipfile.ZipFile
    # zf.open('example.zip', mode = 'r', pwd = None)
    # zf.extractall(path = None, members = None, pwd = None)
    # zf.close()

    # with zipfile.ZipFile('example.zip', 'r') as zf:
    #     data = zf.namelist()
    #     print(data)
    #
    # #file_open = open('example.zip', 'r')
    # z = zipfile.ZipFile('example.zip', 'r')
    # for name in z.namelist():
    #     folder = 'example'
    #     z.extract(name, folder)



if __name__ == '__main__':
    main()