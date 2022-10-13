#!/usr/bin/python3
'''Task: create a class with private object attribute size'''


class Square:
    '''
    creating a class called square

    Has private object attribute called size
    '''
    def __init__(self, size):
        self.__size = size
