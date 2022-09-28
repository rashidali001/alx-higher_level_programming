#!/usr/bin/python3

def uniq_add(my_list=[]):
    list_sum = set(my_list)
    list_sum = list(list_sum)
    result = 0
    for i in list_sum:
        result += i
    return result
