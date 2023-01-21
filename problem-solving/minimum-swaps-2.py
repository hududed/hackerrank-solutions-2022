#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0

    i = 0
    while i < len(arr): # 1 < 4
        if arr[i] != i + 1: # 3 != 1
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1] # 1,2,3,4
            count += 1                                        # 3
        else:
            i += 1 # 1

    return (count)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
