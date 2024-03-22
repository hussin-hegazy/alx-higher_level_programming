#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = []
    for x in matrix:
        n_list = []
        for y in x:
            n_list.append(y**2)
        n_matrix.append(n_list)
    return n_matrix
