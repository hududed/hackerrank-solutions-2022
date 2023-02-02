#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
from math import ceil, floor, sqrt


def encryption(s):
    n = len(s)
    r = floor(sqrt(n))
    c = ceil(sqrt(n))
    results = []

    for i in range(c):
        # i = 0, 0, 0, 1, 1, 1, 2, 2, 2
        # j = 0, 4, 8                   since n 12
      # i+j = 0, 4, 8, 1, 5, 9, ...
        #     h, a, e, a, n, d, ...
        temp = []
        j = 0
        while i+j < n:
            temp.append(s[i+j])  # trial and error ...
            j += c
        results.append("".join(temp))
    return " ".join(results)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
