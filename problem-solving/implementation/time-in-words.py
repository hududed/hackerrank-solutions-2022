#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#
def int_to_en(num):
    d = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
         19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two',
         23: 'twenty three', 24: 'twenty four', 25: 'twenty five',
         26: 'twenty six', 27: 'twenty seven', 28: 'twenty eight', 29: 'twenty nine'}
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert (0 <= num)

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0:
            return d[num]
        else:
            return d[num // 10 * 10] + '-' + d[num % 10]

    raise AssertionError('num is too large: %s' % str(num))


def timeInWords(h, m):

    d = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
         19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two',
         23: 'twenty three', 24: 'twenty four', 25: 'twenty five',
         26: 'twenty six', 27: 'twenty seven', 28: 'twenty eight', 29: 'twenty nine'}

    if m == 0:
        return (f"{d[h]} o' clock")
    elif m == 30:
        return (f"half past {d[h]}")
    elif m < 30:
        if m == 1:
            return (f"{d[m]} minute past {d[h]}")
        elif m == 15:
            return (f"quarter past {d[h]}")
        else:
            return (f"{d[m]} minutes past {d[h]}")
    else:
        m = 60 - m
        h += 1
        if m == 1:
            return (f"{d[m]} minute to {d[h]}")
        elif m == 15:
            return (f"quarter to {d[h]}")
        else:
            return (f"{d[m]} minutes to {d[h]}")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
