#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

"""
    [10, 20, 30, 100, 200, 300, 1000] k = 3
    
    max(10,20,30) - min(10,20,30) = 30-10 = 20

"""


def maxMin(k, arr):
    arr = sorted(arr)
    res = []
    for i in range(len(arr)+1-k):
        res.append(arr[i+k-1]-arr[i])
        return min(res)
    # SHORTER!
    # return min([arr[i+k-1]-arr[i] for i in range(len(arr)+1-k)])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
