#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#


def icecreamParlor(m, arr):

    n = len(arr)
    s = 0
    results = []
    print(m, arr)
    for i in range(n-1, 0, -1):
        if arr[i] < m:
            for j in range(i):
                temp = arr[i]+arr[j]
                if temp == m:
                    results = [j+1, i+1]
    # print(i,j, arr[i],arr[j], temp)
    """
        4 [1, 4, 5, 3, 2]
        1 2 4 5 8
        4 [2, 2, 4, 3]
        1 0 2 2 4
    """  # 1 2 4 5 8
    return results
    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
