#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_sum = []

    if len(tuple_a) == 0 and len(tuple_b) == 2:
        return tuple_b
    if len(tuple_b) == 0 and len(tuple_a) == 2:
        return tuple_a

    if len(tuple_a) == 0 or len(tuple_b) == 0:
        if len(tuple_a) == 0:
            if len(tuple_b) < 2:
                tuple_b += tuple((0, ))
                return tuple_b
        else:
            if len(tuple_a) < 2:
                tuple_a += tuple((0, ))
                return tuple_a

    if len(tuple_a) > 2 or len(tuple_b) > 2:
        if len(tuple_a) > 2:
            tuple_a = tuple((tuple_a[0], tuple_a[1]))

        if len(tuple_b) > 2:
            tuple_b = tuple((tuple_b[0], tuple_b[1]))

    if len(tuple_b) < 2:
        tuple_b += tuple((0,))
    if len(tuple_a) < 2:
        tuple_a += tuple((0,))

    for i in range(len(tuple_a)):
        tuple_sum.append(tuple_a[i] + tuple_b[i])

    return tuple(tuple_sum)
