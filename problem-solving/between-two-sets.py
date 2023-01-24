#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
"""
    2 4
    16 32 96
    
    1. get all possible even divisions between 1 and min of b
    2. get all elements in b not dividable by all elem in a,  b % a != 0
    3. get difference between the two
"""


def getTotalX(a, b):
    even_divs = []
    to_remove = []
    for num in range(1, min(b)+1):
        if min(b) % num == 0:
            even_divs.append(num)
            # print(min(b), num)
    for div in even_divs:
        for num_b in b:
            if num_b % div != 0 and div not in to_remove:
                to_remove.append(div)
            # print(num_b, div, to_remove)
        for num_a in a:
            if div % num_a != 0 and div not in to_remove:
                to_remove.append(div)
            # print(num_a, div, to_remove)
    return len(even_divs)-len(to_remove)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
