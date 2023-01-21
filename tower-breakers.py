#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
from typing import List

def towerBreakers(n: int, m: int) -> None:
    """
    n m               .
    2 2       W.      .
    1 4    .  .       .
                      .
    """
    print(1%2)
    i=0
    while i < n:
        if m == 1:
            return 2 #P1 cant move, P2 wins
        else:
            if n%2 == 1: # if odd number of towers, P1 wins
                return 1
            else: 
                return 2
        i += 1
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

