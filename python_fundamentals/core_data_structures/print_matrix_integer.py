#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    while (i < len(matrix)):
        # Only way I see to manage "bounded space print"
        #   is to use index also in subarray
        for j in range(len(matrix[i])):
            if (j > 0):
                print(' ', end='')
            print("{:d}".format(matrix[i][j]), end='')
        print('')
        i += 1

# matrix is a list of lists (2D list).
# Format each row on its own line.
# Values in a row must be separated by a single space.
