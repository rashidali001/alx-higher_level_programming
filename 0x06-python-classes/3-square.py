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
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def area(self):
        return self.__size * self.__size
