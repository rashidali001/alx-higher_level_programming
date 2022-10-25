#!/usr/bin/python3
''' module that writes to a textfile,returns the no of characters written'''


def write_file(filename="", text=""):
    ''' Function returns number of characters written on a file'''
    with open(filename, "w", encoding="UTF8") as myFile:
        characters = myFile.write(text)
    return characters
