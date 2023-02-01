#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player


def climbingLeaderboard(ranked: List[int], player: List[int]) -> List[int]:
    rankset = list(set(ranked))
    rankset.sort(reverse=True)
    newrank = []
    i = 0
    for score in player[::-1]:
        while i < len(rankset):
            if score >= rankset[i]:
                newrank.append(i+1)
                break
            # print(i, score, rankset[i], newrank)
            i += 1
        if i == len(rankset) and score < rankset[i-1]:
            newrank.append(i + 1)
    newrank = newrank[::-1]
    return newrank


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
