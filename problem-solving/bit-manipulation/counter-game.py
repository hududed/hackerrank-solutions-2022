#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#


def counterGame(n):
    if n == 1:
        return "Richard"
    s = bin(n)
    k = s.count('1')

    # The number of steps to complete the game is one less than
    # the number of 1s in the binary expansion of n plus the
    # number of 0s at the end.
    # E.g. the binary expansion of 132 = 128 + 4 = 2^7+2^2 (10000100).
    # There are two 1s in total and two 0s at the end, so the game finishes
    # 2(1s) + 2(0s at the end) - 1= 4-1 = 3 steps.

    for c in s[:1:-1]:  # in reverse order, NOT `sorted` or `reversed`
        if c == '0':
            k += 1
        else:
            break
    return 'Louise' if k % 2 == 0 else 'Richard'

    # << shifts bits left (multiply), >> divides
    # count = 0
    # while n != 1:
    #     n = n - (1<<len(bin(n))-3) if bin(n).count('1')!=1 else n//2
    #     count += 1
    # return "Louise" if count%2 != 0 else "Richard"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
