class robot:

    population = 0

    def __init__(self, name):
        self.name = name
        print("Initialising {}".format(self.name))
        robot.population += 1

    def sayhi(self):
        print("Hello my name is {}. I am a Robot".format(self.name))

    def die(self):
        print("Killing ({})".format(self.name))
        robot.population -= 1

        if robot.population == 0:
            print("No more Robots Left!")
        else:
            print("{:d} robots remaining".format(robot.population))

    @classmethod
    def hom_many(cls):
        print("{:d} robots available currently".format(cls.population))


robot1 = robot('Rashid-G7623TR')
robot1.sayhi()
robot.hom_many()

robot2 = robot('Omar-G7623TR')
robot2.sayhi()
robot.hom_many()

robot3 = robot('Halima-G7623TR')
robot3.sayhi()
robot.hom_many()

robot2.die()

robot1.die()