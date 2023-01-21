#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

"""         diag_neg    diag_pos
11 2   4    arr[0][0]   arr[0][2] n-1-i
 4 5   6    arr[1][1]   arr[1][1] n-1-i
10 8 -12    arr[i][i]   arr[2][0] n-1-i

"""


def diagonalDifference(arr: list[list[int]]) -> int:

    n = len(arr[0])

    diag_negative = 0
    diag_positive = 0

    for i in range(0, n):
        diag_negative += arr[i][i]
        diag_positive += arr[i][n - i - 1]

    return abs(diag_negative - diag_positive)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
