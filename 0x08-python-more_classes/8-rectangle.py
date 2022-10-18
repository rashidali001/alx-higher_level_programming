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

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
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

    def area(self):
        return int(self.height) * int(self.width)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (int(self.height) * 2) + (int(self.width) * 2)

    def __str__(self):
        result = ""
        if self.width == 0 or self.height == 0:
            return result

        for i in range(self.height):
            for i in range(self.width):
                result += self.print_symbol
            result += '\n'

        return result

    def __repr__(self):
        return ("Rectangle({:d}, {:d})". format(self.width, self.height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not (isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not (isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_2.area() > rect_1.area():
            return rect_2
        if rect_1.area() == rect_2.area():
            rect_1
