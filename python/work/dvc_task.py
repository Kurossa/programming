#!/usr/bin/python3

import zipfile


def extracting(zip_file, extract_folder):
    z = zip_file.ZipFile(zip_file, 'r')
    for name in z.namelist():
        z.extract(name, extract_folder)
        print('The file named:', zip_file, ', has been extracted to:', extract_folder, 'folder')



if __name__ == "__main__":
    main()