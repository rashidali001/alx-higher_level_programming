#!/usr/bin/python3
def islower(c):
    numerical_value = ord(c)
    if (numerical_value >= 97) and (numerical_value <= 123):
        return True
    else:
        return False
