#!/usr/bin/python3

import sys, getopt, zipfile
from pathlib import Path

def print_help():
    print('Help:')
    print('zip_task.py -z <zip file> -f <zip destination folder>')

class ParseArgs:
    def __init__(self):
        self.zip_folder = ''
        self.zip_name = ''

    def parse_args(self, argv):
        try:
            opts, args = getopt.getopt(argv, 'hz:f:', ['help', 'zipfile=', 'folder='])
        except getopt.GetoptError:
            print_help()
            sys.exit(2)

        is_zipfile = False
        is_zipfolder = False

        for opt, arg in opts:
            if opt == '-h':
                print_help()
                sys.exit()
            elif opt in ('-z', '--zipfile'):
                is_zipfile = True
                self.zip_file = arg
            elif opt in ('-f', '--folder'):
                is_zipfolder = True
                self.zip_folder = arg

        return (is_zipfile and is_zipfolder)

    def get_zip_name(self):
        return self.zip_name

    def get_zip_folder(self):
        return self.zip_folder


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
        return False
    else:
        return True

def main(argv):
    parse_args = ParseArgs()
    if parse_args.parse_args(argv) and dir_check(zip_folder):
        extraction(parse_args.get_zip_name(), parse_args.get_zip_folder())
    else:
        print_help()
        sys.exit(2)

if __name__ == '__main__':
    main(sys.argv[1:])