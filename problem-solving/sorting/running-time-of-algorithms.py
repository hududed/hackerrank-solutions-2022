#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def runningTime(arr):
    shift = 0
    for j in range(1, len(arr)):
        key = arr[j]  # to be sorted
        i = j
        while i > 0 and arr[i-1] > key:
            arr[i] = arr[i-1]
            shift += 1
            i -= 1
        arr[i] = key
        # print(j, i, arr, shift)
    return shift
    # print(j, arr[j])
    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
