#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrx = matrix.copy()

    for j in range(len(matrix)):
        new_matrx[j] = list(map(lambda x: x**2, matrix[j]))

    return (new_matrx)
