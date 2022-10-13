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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            print("size must be >= 0")
        self.__size = size
