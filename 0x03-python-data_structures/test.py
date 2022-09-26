#!/usr/bin/python3
import random

navlist = []

for i in range(5):
    navlist.append(random.randrange(1,10))

for i in navlist:
    print("{}".format(i))
