#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries: list[tuple[int]]) -> list[int]:
    """
    3 4 
    2 1003 
    1 16
    3 1
    
    op 3 -> return 1 if some number is counted 4 times, else 0 -> return 0
    op 2 -> remove 1003 from array
    op 1 -> add 16 to array
    op 3 -> return 1 if some number is counted 1 time -> 16 occurs 1 time -> return 1
    
    """

    count = dict()
    result = list()

    for q in queries:
        if q[0] == 1:
            try:
                count[q[1]] += 1
            except:
                count[q[1]] = 1
        elif q[0] == 2:
            try:
                count[q[1]] -= 1
                if count[q[1]] == 0:
                    del count[q[1]]
            except:
                continue
        else:
            if q[1] in set(count.values()):
                result.append('1')
            else:
                result.append('0')
    return result
            
            
    # print(op, data, dict(hmap).values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

