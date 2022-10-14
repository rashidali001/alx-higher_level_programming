#!/usr/bin/python3
''' Task 4'''


import sys
var = sys.stdout


class Square:
    '''Square class definition'''
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.size * self.size

    def my_print(self):
        if self.size == 0:
            var.write(" " + '\n')

        for i in range(self.size):

            for i in range(self.size):

                var.write("#")

            var.write('\n')
