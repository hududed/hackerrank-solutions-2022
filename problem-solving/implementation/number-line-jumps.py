#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#


def kangaroo(x1, v1, x2, v2):

    # for i in range(100000):
    #     pos1 = x1 + i * v1
    #     pos2 = x2 + i * v2
    #     # print(i, pos1, pos2)
    #     if pos1 == pos2:
    #         return ("YES")
    # return ("NO")

    # without specifying run size
    if x1 < x2 and v1 < v2:
        return "NO"
    else:
        if v1 != v2 and (x2-x1) % (v2-v1) == 0:
            return "YES"
        else:
            return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
