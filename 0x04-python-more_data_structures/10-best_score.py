#!/usr/bin/pyton3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    score = 0
    for i in a_dictionary:
        if score < a_dictionary[i]:
            score = a_dictionary[i]
    for i in a_dictionary:
        if a_dictionary[i] == score:
            return i
