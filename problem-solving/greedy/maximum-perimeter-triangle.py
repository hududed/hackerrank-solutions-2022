#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#


def maximumPerimeterTriangle(sticks):
    """
            a + b > c
            a + c > b
            b + c > a
    """

    sticks.sort()
    i = len(sticks) - 3

    while i >= 0 and sticks[i] + sticks[i+1] <= sticks[i+2]:
        # if degenerate, traverse
        i -= 1
    if i >= 0:
        return [sticks[i], sticks[i+1], sticks[i+2]]
    else:
        return [-1]

    # DOESNT WORK!
    # peri = {}

    # for i in range(2, len(sticks)):
    #     if sticks[i-2]+sticks[i-1] <= sticks[i]:
    #         if len(sticks) <= 3:
    #             return [-1]
    #         else:
    #             continue
    #     sides = [sticks[i-2],sticks[i-1],sticks[i]]
    #     peri[sum(sides)] = sides
    # return peri[max(peri)]

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
