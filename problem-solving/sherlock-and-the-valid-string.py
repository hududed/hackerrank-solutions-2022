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
    result = dict(Counter(s))
    list1 = list(result.values())
    high = max(list1)
    print(list1, high)

    if len(dict(Counter(list1))) == 1:
        return "YES"
    elif list1.count(high) == 1 and high - 1 == min(list1):
        return "YES"
    elif list1.count(high) > 1 and list1.count(min(list1)) == 1:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
