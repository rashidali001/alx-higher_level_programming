#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for j in matrix[i]:
            print("{}".format(j), end=" ")
        print()
