class Robot:
    def __init__(self, name = None, build_year = 2000):
        self.__name = name
        self.__build_year = build_year

    def  setname(self, name):
        self.__name = name
    def setyear(self, year):
        self.__build_year = year
    def getname(self):
        return self.__name
    def getyear(self):
        return self.__build_year