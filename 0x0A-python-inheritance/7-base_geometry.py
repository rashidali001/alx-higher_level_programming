#!/usr/bin/python3
'''Improve Geometry'''


class BaseGeometry:
    '''BaseGeometry class'''

    def area(self):
        '''raises an Exception'''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
         Check whether is an integer
         Check whether integer is <= 0
        '''

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
