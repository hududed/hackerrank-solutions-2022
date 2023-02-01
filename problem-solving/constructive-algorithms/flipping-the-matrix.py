#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
"""                        |
112 42 | 83 119       -  A B B A      arr[i][j] ->     0,0 ->112
56 125 | 56 49           C D D C      arr[i][n-j-1] -> 0,3 ->119
-------                  C D D C      arr[n-i-1][j] -> 3,0 -> 62
15 78    101 43          A B B A      arr[n-i-1][n-j-1]3,3 -> 108
62 98    114 108

1. loop through just half of rows and half of cols
2. 
"""


def flippingMatrix(matrix):

    n = len(matrix)
    total = 0
    for i in range(n//2):
        for j in range(n//2):
            total += (max(matrix[i][j],
                          matrix[i][n-j-1],
                          matrix[n-i-1][j],
                          matrix[n-i-1][n-j-1]))
    return total


    # print(matrix[i][j]) # top right
    # print(matrix[i][n-j-1]) # top right
    # print(matrix[n-i-1][j]) # bottom left
    # print(matrix[n-i-1][n-j-1]) # bottom right4
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
