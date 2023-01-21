#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
"""
    something like digiral root function
    dr(n) = 1 + (n-1 mod 9)
"""


def superDigit(n: str, k: int) -> int:
    return 1 + (k * sum(int(x) for x in n) - 1) % 9

    # for i in range(k):
    #     summed = sum([int(i) for i in n])
    #     print(i, len(n), summed)
    #     n = str(summed)
    # return summed


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
