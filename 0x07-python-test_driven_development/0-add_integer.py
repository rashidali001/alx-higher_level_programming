#!/usr/bin/python
'''
Module 0-add_integer
Contains one method that returns an int sum
'''


def add_integer(a, b=98):
    '''Function that adds 2 integers'''

    if a is not int or a is not float:
        raise TypeError("a must be an integer")

    if b is not int or b is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)


