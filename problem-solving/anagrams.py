#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    """
        aaa bbb
        bbb      3

        mn op
        op       2

        xy yx    0



        1. strings must be equal length -> no odd lengths
        2. if elem in a not in b, count changes
        3. if elem a in b, remove elem a from b
    """

    if len(s) % 2 != 0:
        return -1
    a = [*s[:len(s)//2]]
    b = [*s[len(s)//2:]]
    min_cnt = 0
    for i in a:
        if i not in b:
            min_cnt += 1
        else:
            b.remove(i)
    return min_cnt

    print(s, a, b)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
