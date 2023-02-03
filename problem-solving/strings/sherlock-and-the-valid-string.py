#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
from collections import Counter


def isValid(s):
    counted = dict(Counter(s))

    # case 1: same frequency
    if len(set(counted.values())) == 1:
        return "YES"

    # case 2: 3 or more frequencies
    elif len(set(counted.values())) > 2:
        return "NO"
    # case 3: 2 freqs
    else:
        for k in counted:
            counted[k] -= 1
            temp = list(counted.values())
            try:
                temp.remove(0)
            except:
                pass
            if len(set(temp)) == 1:
                return "YES"
            else:
                counted[k] += 1
            # print(counted, len(set(temp)))
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
