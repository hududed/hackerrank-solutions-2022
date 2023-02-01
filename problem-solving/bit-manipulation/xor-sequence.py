#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the xorSequence function below.


def fun(num):
    n = num % 8
    if n == 0 or n == 1:
        return num
    elif n == 2 or n == 3:
        return 2
    elif n == 4 or n == 5:
        return num + 2
    else:
        return 0


def xorSequence(l, r):
    # 0 1 3 0 4 1 7 0
    # 0 1 2 2 6 7 0 0 (0, 0^1, 1^3, 2^0, 2^4, 6^1, 7^7, 0^0)
    return fun(l-1) ^ fun(r)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        lr = input().split()

        l = int(lr[0])

        r = int(lr[1])

        result = xorSequence(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
