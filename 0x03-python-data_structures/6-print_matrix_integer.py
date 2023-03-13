#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == []:
        print("")
    else:
        for row in matrix:
            for col in row:
                print("{:d}".format(col), end=" ")
            print()
