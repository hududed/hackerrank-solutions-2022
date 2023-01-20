#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr: list[int], r: int) -> int:
    """
    r = 2
    1 2 2 4
    |
    
    num = {4: 1, 2: 2}
    pairs = {2: 2}
    count = 0
    1*2 = 2, since there are two pairs (2,4) already, we can count 2 triplets (1,2,4)
    
    1. track the number in array
    2. track the pair of geometrical progression
    3. count pairs and return
    """
    numbers, pairs = {}, {}
    counter = 0
    if len(arr) <= 2: # triples must have length 3
        return 0

    for i in reversed(arr):
        if r*i in pairs:
            counter += pairs[r*i]
        if r*i in numbers:
            pairs[i] = pairs.get(i, 0) + numbers[r*i]
        numbers[i] = numbers.get(i, 0 ) + 1
    
    return counter
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

