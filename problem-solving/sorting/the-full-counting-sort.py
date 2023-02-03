#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#


def countSort(arr):
    # create empty lists based on constraint x <= 100
    results = [[] for _ in range(100)]

    # first half
    for i in range(n//2):
        results[int(arr[i][0])].append("-")
    # second half
    for i in range(n//2, n):
        results[int(arr[i][0])].append(arr[i][1])
    for string in results:
        if string:  # edge case, if string is empty we will print an extra space
            print(*string, end=" ")


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
