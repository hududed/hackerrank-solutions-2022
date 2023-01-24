#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#


def flip(bits):
    inverse = ''
    for i in bits:
        if i == '0':
            inverse += '1'
        else:
            inverse += '0'
    return inverse


def flippingBits(n):
    bits = "{0:032b}".format(n)
    flipped = flip(bits)
    return int(flipped, 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
