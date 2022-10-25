#!/usr/bin/python3
'''a function that reads a text file (UTF8) and prints it to stdout '''


def read_file(filename=""):
    ''' reads a text file (UTF8) and prints it to stdout '''
    with open(filename, "r", encoding="UTF8") as myFile:
        read_data = myFile.read()
        print(read_data, end="")
    myFile.close()
