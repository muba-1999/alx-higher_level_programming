#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix
    args:
        matrix: matrix to be printed
    Return:
        the matrix
    """
    try:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                print("{:d}".format(matrix[i][j]), end=' ')
            print()
    except IndexError:
        print()
