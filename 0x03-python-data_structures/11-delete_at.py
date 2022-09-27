#!/usr/bin/python

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    for i in range(4):
        if i == idx:
            my_list[i] = my_list[i + 1]
        if i > idx:
            my_list[i] = my_list[i + 1]


    return my_list



my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
