#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def pairs(k, arr):
    # variation of two sum problem
    arr.sort()
    ans = 0
    i, j = 0, 0
    while j < len(arr):
        print(i, j, arr[j], arr[i])
        if arr[j] - arr[i] == k:
            ans += 1
            i += 1
            j += 1
        elif arr[j] - arr[i] < k:
            j += 1
        elif arr[j] - arr[i] > k:
            i += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
