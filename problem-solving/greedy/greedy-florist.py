#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):

    cost = 0
    n = len(c)
    m = 1  # (0+1)

    c.sort(reverse=True)

    for i in range(n):
        cost += c[i]*m
        print(i, c[i], m, cost)
        if (i+1) % k == 0:  # increase multiplier after every k person
            m += 1
    return cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
