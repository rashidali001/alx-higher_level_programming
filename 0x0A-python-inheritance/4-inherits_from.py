#!/usr/bin/python3
'''Check whether an object is a subclass'''


def inherits_from(obj, a_class):
    '''Returns True is correct otherwise False'''

    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False
