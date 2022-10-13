class student:
    def __init__(self, name = None, age = None):
        self.__name = name
        self.__age = age

    def setname(self, name):
        self.__name = name
    def setage(self, age):
        self.__age = age
    def getname(self):
        return self.__name
    def getage(self):
        return self.__age

    def sayhi(self):
        print(f"Hi my name is {self.__name}")
        print(f"I am {self.__age} years old!")


student1 = student()
student1.setname("Marvin")
student1.setage(24)

student2 = student()
student2.setname("Nash")
student2.setage(22)

for x in [student1, student2]:
    x.sayhi()
    if x.getname() == "Marvin":
        x.setage(26)
    if x.getname() == "Nash":
        x.setage(24)
    x.sayhi()

