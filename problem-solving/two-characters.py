#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def alternate(s):

    letters = list(set(s))
    words = {}

    for i in range(len(letters)):
        for j in range(i+1, len(letters)):
            w = ''
            for l in s:
                print(l, letters[i], letters[j], w)
                if l == letters[i] or l == letters[j]:
                    if w == '' or l != w[-1]:
                        w += l
                    else:
                        w = ''
                        break
            if w != '' and len(w) > 1:
                words[w] = len(w)

    if len(words) == 0:
        return 0
    return max(words.values())

    # unique = list(set(s))
    # # lst = [*s]
    # # print(lst)

    # for i in range(len(unique)):
    #     for j in range(i+1, len(unique)):

    #     temp = s
    #     temp = s.replace(c, '')
    #     for d in reversed(unique):
    #         temp = temp.replace(d,'')

    #     # temp.remove(c)
    #         print(c, d, temp)
    # # print(set(s))
    # # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
