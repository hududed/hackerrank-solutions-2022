#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#


def minimumNumber(n, password):

    count = 0
    if not re.search('\d', password):
        count += 1
    if not re.search('[a-z]', password):
        count += 1
    if not re.search('[A-Z]', password):
        count += 1
    if not re.search('[!@#$%^&*()\-+]', password):
        count += 1
    print(count)
    if (n+count) < 6:
        z = 6-(n+count)
        count = count+z
    return count

    # Return the minimum number of characters to make the password strong


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
