
class Robot:
    def __init__(self, name=None):
        self.name = name
    def say_hi(self):
        if self.name:
            print("Hi I am {}".format(self.name))
        else:
            print("Hi. I am a Robot without a name")

    def  setname(self, name):
        self.name = name
    def setyear(self, year):
        self.year = year
    def getname(self):
        return self.name
    def getyear(self):
        return self.year


