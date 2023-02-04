#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
# 4 6 4 5 6 5 2
# 1 2 1 2 1 1 1

# 1 2 1 2 3 2 1


def candies(n, arr):
    dist = [1] * n
    # check left to right
    for i in range(1, n):
        if arr[i-1] < arr[i]:
            dist[i] = dist[i-1] + 1
    # check right to left
    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1] and dist[i] <= dist[i+1]:
            dist[i] = dist[i+1] + 1

    # print(dist)
    return sum(dist)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
