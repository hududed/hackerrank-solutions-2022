#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def quickSort(arr):
    # l = []
    # r = []
    pivot = arr[0]

    # for i in range(1, len(arr)):
    #     if arr[i] < pivot:
    #         l.append(arr[i])
    #     elif arr[i] > pivot:
    #         r.append(arr[i])
    # return l + [pivot] + r

    l, r = 0, len(arr) - 1

    while l < r:
        while l < r and arr[l] <= pivot:
            l += 1
        while arr[r] > pivot:
            r -= 1
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    arr[0], arr[r] = arr[r], arr[0]
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
