#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
"""                      .
    n m     P1 lose      .
    2 2       .          . 
    1 4     . .          . P2 lose
    
    1. if m = 1, then P2 auto win
    2. if n % 2 = 1, P1 wins
"""


def towerBreakers(n, m):

    i = 0
    while i < n:
        if m == 1:
            return 2
        else:
            if n % 2 == 1:
                return 1
            else:
                return 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
