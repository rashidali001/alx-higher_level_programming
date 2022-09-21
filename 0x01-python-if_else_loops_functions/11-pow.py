#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        return 1 / pow(a, -b)
    if b == 0:
        return 1
    i = 1
    product = 1
    while i <= b:
        product = product * a
        i += 1
    return product
