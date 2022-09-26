#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    for i in element:
        if i == idx:
            new_list.append(element)
            continue
        new_list.append(my_list[i])

    return new_list
