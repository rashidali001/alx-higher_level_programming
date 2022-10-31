#!/usr/bin/python3
'''
    1. Base class
    - private class attribute
    - class constructor:
'''


class Base:
    '''Base class'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''__init__ method'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
