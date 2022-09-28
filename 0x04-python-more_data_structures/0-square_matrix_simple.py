#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for i in matrix:
        list_a = []
        for j in range(len(i)):
            list_a.append(i[j] * i[j])
        square.append(list_a)
    return square
