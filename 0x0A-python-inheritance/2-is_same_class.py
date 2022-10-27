#!/usr/bin/python3
'''Check whether an object is an instance of a class'''


def is_same_class(obj, a_class):
    '''Returns True is correct otherwise False'''

    return type(obj) is a_class
