#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr: list[int]) -> None:

    neg_count, pos_count, zero_count = 0, 0, 0

    for i in arr:
        if i < 0:
            neg_count += 1
        elif i > 0:
            pos_count += 1
        else:
            zero_count += 1

    print(pos_count/len(arr))
    print(neg_count/len(arr))
    print(zero_count/len(arr))
    # Write your code here


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
