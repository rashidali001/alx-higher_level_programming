#!/usr/bin/python3
import os
'''Task 0'''


def read_file(filename=""):
    ''' Function used for reading files'''

    with open(filename, mode="r", encoding="UTF8") as myFile:
        read_data = myFile.read()
        print(read_data, end="")

    myFile.close()
