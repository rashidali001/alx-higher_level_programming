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
        self.width = int(width)
        self.height = int(height)
        self.x = int(x)
        self.y = int(y)

    @property
    def width(self):
        '''getting width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setting value of width'''
        if not isinstance(value, int):
            raise TypeError("width must be a integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = int(value)

    @property
    def height(self):
        '''getting value of height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setting value of height'''
        if not isinstance(value, int):
            raise TypeError("height must be a integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = int(value)

    @property
    def x(self):
        '''getting value of x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''setting value of x'''
        if not isinstance(value, int):
            raise TypeError("x must be a integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = int(value)

    @property
    def y(self):
        '''getting value of y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setting value of y'''
        if not isinstance(value, int):
            raise TypeError("y must be a integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = int(value)

    def area(self):
        '''Getting area of object'''
        return int(self.width) * int(self.height)

    def display(self):
        '''displaying # character in stdout'''
        for y in range(self.y):
            print()

        for height in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for width in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        '''Displaying object information'''
        return "[{}] ({}) {}/{} - {}/{}"\
            .format(self.__class__.__name__,
                    self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        '''Updating object values'''
        count = 0
        for arg in args:
            if count == 0:
                super(Rectangle, self).__init__(args[count])
            if count == 1:
                self.__width = args[count]
            if count == 2:
                self.__height = args[count]
            if count == 3:
                self.__x = args[count]
            if count == 4:
                self.__y = args[count]
            count += 1
