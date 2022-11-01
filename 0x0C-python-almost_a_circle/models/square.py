#!/usr/bin/python3
'''
    Square class
    inherits from Rectangle
'''
Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    '''Class Square definition'''

    def __init__(self, size, x=0, y=0, id=None):
        super(Square, self).__init__(size, size, x, y, id)

    def __str__(self):
        '''Displaying object information'''
        return "[{}] ({}) {}/{} - {}" \
            .format(self.__class__.__name__,
                    self.id, self.x, self.y, self.width)
