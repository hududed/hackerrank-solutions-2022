#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#


def birthday(s, d, m):
    # s [1, 2, 1, 3, 2] d=3 m=2
    count = 0
    results = [0 for _ in range(len(s))]
    for i in range(len(s)):
        if sum(s[i:i+m]) == d:
            results[i] += 1
    for i in results:
        if i != 0:
            count += 1
    return count

    # SHORTER!
    # return len([1 for i in range(len(s)) if sum(s[i:i+m])==d])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
