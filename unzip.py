#!/usr/bin/python3

import magic
import os
from zipfile import ZipFile

def createDestroy(directory):
    file = directory
    directory = directory.split(".")[0]
    if os.path.exists(directory):
        pass
    else:
        try:
            os.mkdir(directory)
            with ZipFile(file) as myzip:
                myzip.extractall(directory)
                os.remove(file)
        except:
            pass

def isFileZip(file):
    if os.path.isdir(file) == True:
        pass
    else:
        if magic.from_file(file).split(" ")[0] != 'Zip':
            pass
        else:
            createDestroy(file)

def main():
        for i in os.listdir():
                isFileZip(i)

if __name__ == "__main__":
    main()
