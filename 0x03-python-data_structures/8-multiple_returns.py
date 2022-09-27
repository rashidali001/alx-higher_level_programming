#!/usr/bin/python3

def multiple_returns(sentence):
    answer = []
    first_character = ""
    length = len(sentence)
    if len(sentence) == 0:
        first_character = None
    else:
        first_character = sentence[0]
    answer.append(length)
    answer.append(first_character)
    return tuple(answer)
