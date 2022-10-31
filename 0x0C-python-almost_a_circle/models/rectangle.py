#!/usr/bin/python3
'''
    2.First Rectangle
    - Rectangle class
    - inherits from Base
    - Private instance attributes (2)
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


class Rectangle(Base):
    '''Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializing'''

        if not isinstance(width, int):
            raise TypeError("width must be a integer")
        if not isinstance(height, int):
            raise TypeError("height must be a integer")
        if not isinstance(x, int):
            raise TypeError("x must be a integer")
        if not isinstance(y, int):
            raise TypeError("y must be a integer")

        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")

        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("width must be a integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''getting height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setting height'''
        if not isinstance(value, int):
            raise TypeError("height must be a integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''getting x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setting x'''
        if not isinstance(value, int):
            raise TypeError("x must be a integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        '''getting y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setting y'''
        if not isinstance(value, int):
            raise TypeError("y must be a integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Getting area'''
        return int(self.width) * int(self.height)
