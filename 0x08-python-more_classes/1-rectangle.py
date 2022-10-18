#!/usr/bin/python3
'''
    CLass name: Rectangle
    private instance attributes: width & height
    width: getter -> def width(self)
    height: getter -> def height(self)
    inside setters:
    if values are  not int
    raise TypeError exception
    if value < 0
    raise ValueError exception
'''


class Rectangle:
    '''This is a Rectangle class'''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        try:
            if type(value) is not int:
                raise TypeError
            if value < 0:
                raise ValueError

        except TypeError:
            print("width must be an integer")
            self.__width = 0
        except ValueError:
            print("width must be >= 0")
            self.__width = 0
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        try:
            if type(value) is not int:
                raise TypeError
            if value < 0:
                raise ValueError
        except TypeError:
            print("height must be an integer")
            self.__height = 0
        except ValueError:
            print("height must be >= 0")
            self.__height = 0
        else:
            self.__height = value
