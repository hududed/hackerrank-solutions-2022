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


def runningTime(l):
    count = 0
    for i in range(1, len(l)):
        inner_count = 0
        key = l[i]
        j = i
        while (j > 0) and (l[j-1] > key):
            l[j] = l[j-1]
            inner_count += 1
            j -= 1
        count += inner_count
        l[j] = key
    return (count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
