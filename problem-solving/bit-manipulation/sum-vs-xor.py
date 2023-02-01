#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

"""
    inp  -  bit  -  count 0s
      4  -  100  -  2^2(0s) = 4
      5  -  101  -  2^1(0s) = 2
      10 -  1010 -  2^2(0s) = 4
"""


def sumXor(n):
    results = 1
    while n:
        b = n & 1
        if b == 0:  # count 0s
            results *= 2
        print(n, b, results)
        n >>= 1
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
