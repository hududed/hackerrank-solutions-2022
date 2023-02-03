#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countingSort(arr):
    count = [0] * (max(arr)+1)
    print(len(count))

    for num in arr:
        count[num] += 1
    # print(count)
    sortarr = []
    for i in range(len(count)):
        while count[i] != 0:
            count[i] -= 1
            sortarr.append(i)
            # print(sortarr)
    return sortarr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
