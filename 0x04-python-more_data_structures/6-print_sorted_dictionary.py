#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    result_dictionary = dict()

    for i in sorted(a_dictionary.keys()):
        result_dictionary[i] = a_dictionary[i]

    for i, j in result_dictionary.items():
        print("{}: {}". format(i, j))
