#!/usr/bin/python3
'''
    2.First Rectangle
    - Rectangle class
    - inherits from Base
    - Private instance attributes (2)
'''
Base = __import__('base').Base


class Rectangle(Base):
    '''Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super(Rectangle, self).__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def get_width(self):
        return self.__width

    @get_width.setter
    def set_width(self, value):
        self.__witdh = value

    @property
    def get_height(self):
        return self.__width

    @get_height.setter
    def set_height(self, value):
        self.__height = value

    @property
    def get_x(self):
        return self.__width

    @get_x.setter
    def set_x(self, value):
        self.__height = value

    @property
    def get_y(self):
        return self.__width

    @get_y.setter
    def set_y(self, value):
        self.__height = value
