class Robot:
    def __init__(self):
        self.pub = "This is public"
        self._protect = "This is protected"
        self.__private = "This is private"

x = Robot()
x.pub  = x.pub + " And can be changed"
x._protect = x._protect + " And can be changed"
print(x.pub)
print(x._protect)
