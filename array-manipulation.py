#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n: int, queries: list[list[int]]) -> int:
    arr = [0]*(n+1)
    max_so_far = 0
    total_sum = 0

    for query in queries:
        l, h, val = query
        print(l, h, val)
        arr[l-1] = arr[l-1] + val
        arr[h] = arr[h]-val
    print(arr)
    for value in arr:
        total_sum = total_sum + value
        max_so_far = max(max_so_far, total_sum)
        print(f"value: {value}, total_sum: {total_sum}, max: {max_so_far}")
    return max_so_far

    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

