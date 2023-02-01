#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#


def separateNumbers(s):

    if len(s) == 1:
        print("NO")
        return
    else:
        # print(s)
        # generate int strings by 1 increments
        for i in range(1, len(s)//2 + 1):
            genstr = s[:i]  # window size increases by 1
            prev = int(genstr)

            # do ops until length reached
            while len(genstr) < len(s):
                # s[:1] = 1, next is 2,3,.. s[:2] = 12, next is 13, 14, ..
                next = prev + 1
                genstr = genstr + str(next)
                # print(i, prev,next, genstr)
                prev = next
            if genstr == s:
                print("YES", s[:i])
                return
        print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
