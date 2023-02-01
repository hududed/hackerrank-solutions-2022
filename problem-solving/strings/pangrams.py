#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def pangrams(s):

    # get rid of spaces
    s = s.replace(" ", "").lower()
    total_alphabets = 26
    if len(set(s)) == total_alphabets:
        return ("pangram")
    else:
        return ("not pangram")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
