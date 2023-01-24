#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

"""
    2 1 3   ->  1 2 3  all(1+9, 2+8, 3+7 >= 10) = true,
    7 8 9   ->  9 8 7
    
    1 2 2 1 -> 1 1 2 2 all(5,4,5,5 >= 5) = False
    3 3 3 4 -> 4 3 3 3
"""


def twoArrays(k, A, B):
    A_ = sorted(A)
    B_ = sorted(B, reverse=True)
    i, j = 0, 0
    while i < len(A_) and j < len(B_):
        if A_[i]+B_[j] >= k:
            i += 1
            j += 1
        else:
            return "NO"
    return "YES"

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
