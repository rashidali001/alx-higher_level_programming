#!/usr/bin/python3
'''
Task:
    1 - private instance attribute
    2 - pass default value on size if not provided
    3 - size must be an integer else raise TypeError
    4 - if size < 0 raise ValueError
'''


class Square:
    '''Defines a class with private object attributes'''

    def __init__(self, size=0):
        try:
            if isinstance(size, int):
                pass
            else:
                raise TypeError
        except TypeError:
            print("size must be an integer")

        try:
            if size < 0:
                pass
        except (ValueError, TypeError):
            print("size must be >= 0")
        else:
            self.__size = size

    def isinteger(self):
        pass
