#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    while (i < len(matrix)):
        for j in matrix[i]:
            print("{:d}".format(j), end=' ')
        print('')
        i += 1

# matrix is a list of lists (2D list).
# Format each row on its own line.
# Values in a row must be separated by a single space.
