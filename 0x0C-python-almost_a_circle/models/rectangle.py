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
        '''Initializing'''

        super(Rectangle, self).__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def get_width(self):
        '''getting width'''
        return self.__width

    @get_width.setter
    def set_width(self, value):
        '''setting width'''
        self.__witdh = value

    @property
    def get_height(self):
        '''getting height'''
        return self.__width

    @get_height.setter
    def set_height(self, value):
        '''setting height'''
        self.__height = value

    @property
    def get_x(self):
        '''getting x'''
        return self.__width

    @get_x.setter
    def set_x(self, value):
        '''setting x'''
        self.__height = value

    @property
    def get_y(self):
        '''getting y'''
        return self.__width

    @get_y.setter
    def set_y(self, value):
        '''setting y'''
        self.__height = value
