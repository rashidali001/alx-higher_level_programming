

class p:
    def __init__(self, x):
        self.set_x(x)
    def set_x(self, x):
        if x > 1000:
            self.__x = 1000
        elif x < 0:
            self.__x = 0
        else:
            self.__x = x

    def get_x(self):
        return self.__x

p1  = p(-87)
print(p1.get_x())