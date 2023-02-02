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
from functools import reduce


def gcd(a, b):
    # greatest common division
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    # lowest common multiplier
    return a*b // gcd(a, b)


def getTotalX(a, b):

    l = reduce(lcm, a)
    g = reduce(gcd, b)

    # print (l, g)
    s = 0
    for i in range(l, g+1, l):
        if g % i == 0:
            s += 1
    return s
    # print(i, g %i)


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
