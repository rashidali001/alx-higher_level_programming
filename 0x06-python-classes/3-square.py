#!/usr/bin/python3
'''
Task:

'''


class Square:
    '''Defines a class with private object attributes'''
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            print("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
