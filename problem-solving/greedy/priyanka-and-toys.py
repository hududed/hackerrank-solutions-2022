#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#


def toys(w):
    w.sort()
    print(w)

    container = 1
    temp = []
    for i in range(len(w)):
        temp.append(w[i])
        if w[i] - temp[0] > 4:
            temp = [w[i]]
            container += 1
    return container


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
