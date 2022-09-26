#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_list = []
    length = len(my_list) - 1
    for i in range(5):
        reversed_list.append(my_list[length])
        length -= 1
    my_list = reversed_list
    for i in my_list:
        print("{:d}".format(i))
