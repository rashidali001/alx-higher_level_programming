#!/usr/bin/python3
import os
'''Task 0'''


def read_file(filename=""):
    with open(filename, mode="r", encoding="UTF8") as myFile:
        for line in myFile:
            print(line, end="")
