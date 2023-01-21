#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

"""
n = 5
ori i       1 2 3 4 5
            1 2 3 5 4
            1 2 5 3 4
            2 1 5 3 4

swapped    2 1 5 3 4

1. start from the rear
2. get difference pos to actual value -> if > 2 --> too chaotic
3. for legal bribes diff < 3: find pos in range it moved max(0, diff) to actual val
4. if pos in this inner loop > pos outer --> they bribed

"""
from typing import List


def minimumBribes(q: List[int]) -> None:
    min_bribes = 0

    for i in range(len(q)-1, -1, -1):
        if q[i] - (i+1) > 2:  # cannot bribe more than 2
            print('Too chaotic')
            return
        for j in range(max(0, q[i]-2), i):
            if q[j] > q[i]:
                min_bribes += 1
    print(min_bribes)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
