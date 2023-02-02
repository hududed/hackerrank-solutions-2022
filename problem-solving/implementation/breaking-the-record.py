#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    # n = len(scores)

    # min_score = max_score = scores[0]
    # min_count = max_count = 0
    # for i in range(n):
    #     prev_min, prev_max = min_score, max_score

    #     min_score = min(scores[i], min_score)
    #     max_score = max(scores[i], max_score)

    #     if min_score != prev_min:
    #         min_count += 1
    #     if max_score != prev_max:
    #         max_count += 1

    # return (max_count, min_count)

    min_score = max_score = scores[0]
    min_count = max_count = 0

    for i in range(1, len(scores)):
        if min_score < scores[i]:
            min_score = scores[i]
            min_count += 1
        elif max_score > scores[i]:
            max_score = scores[i]
            max_count += 1
    return min_count, max_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
