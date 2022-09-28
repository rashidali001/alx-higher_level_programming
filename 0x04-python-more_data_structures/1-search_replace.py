#!/usr/bin/python3

def search_replace(my_list, search, replace):
    list_a = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            list_a.append(replace)
        else:
            list_a.append(my_list[i])
    return list_a

