#!/usr/bin/python3
'''Module that appends text and returns no.s of characters appended'''


def append_write(filename="", text=""):
    ''' Functions that appends and returns no of characters'''
    with open(filename, "a", encoding="UTF8") as myFile:
        characters = myFile.write(text)
    return characters
