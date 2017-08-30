#!/usr/bin/python3

import sys, getopt, zipfile
from pathlib import Path

def print_help():
    print('Help:')
    print('zip_task.py -z <zip file> -f <zip destination folder>')

def parse_args(argv):
    try:
        opts, args = getopt.getopt(argv, 'hz:f:', ['help', 'zipfile=', 'folder='])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    is_zipfile = False
    is_zipfolder = False

    zip_file = ''
    zip_folder = ''

    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt in ('-z', '--zipfile'):
            is_zipfile = True
            zip_file = arg
        elif opt in ('-f', '--folder'):
            is_zipfolder = True
            zip_folder = arg

    return zip_file, zip_folder, (is_zipfile and is_zipfolder)

def extraction(zip_file, extract_folder):
    file = zip_file
    folder = extract_folder
    z = zipfile.ZipFile(file, 'r')
    for name in z.namelist():
        z.extract(name, folder)
        print('The file named:',file,', has been extracted to:',folder, 'folder')

def dir_check(dir):
    is_dir_already = Path(dir)
    if is_dir_already.exists():
        print('Folder',is_dir_already,'exist!')
        sys.exit(2)
    else:
        return False

def main(argv):
    zip_file, zip_folder, parse_ok = parse_args(argv)
    if parse_ok and not dir_check(zip_folder):
        extraction(zip_file, zip_folder)
    else:
        print_help()
        sys.exit(2)

if __name__ == '__main__':
    main(sys.argv[1:])