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
    def width(self):
        '''getting width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setting width'''
        self.__width = value

    @property
    def height(self):
        '''getting height'''
        return self.__width

    @height.setter
    def height(self, value):
        '''setting height'''
        self.__height = value

    @property
    def x(self):
        '''getting x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setting x'''
        self.__x = value

    @property
    def y(self):
        '''getting y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setting y'''
        self.__y = value
