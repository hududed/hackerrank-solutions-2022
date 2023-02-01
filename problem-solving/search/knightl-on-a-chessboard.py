#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#
from collections import deque

# BFS BFS BFS


def check_pairs(i, j, a, b, n):
    # x[0] x-axis, x[1] y-axis
    possible_pairs = [
        (i+a, j+b), (i-a, j-b),
        (i-a, j+b), (i+a, j-b),
        (i+b, j+a), (i-b, j-a),
        (i-b, j+a), (i+b, j-a)]
    moves = {}
    for pair in possible_pairs:
        if 0 <= pair[0] < n and 0 <= pair[1] < n:
            moves[pair] = 1
    return moves


def bfs(a, b, n):
    q = deque([(0, 0, 0)])
    visited = {(0, 0): 1}
    while q:
        i, j, count = q.popleft()
        possible_pairs = check_pairs(i, j, a, b, n)
        for pair in possible_pairs:
            if pair == (n-1, n-1):
                return count + 1
            if pair not in visited:
                visited[pair] = 1
                q.append((pair[0], pair[1], count+1))
    return -1


def knightlOnAChessboard(n):
    results = []

    for i in range(1, n):  # since 1 <= a,b < n
        temp = []
        for j in range(1, n):
            temp.append(bfs(i, j, n))
        results.append(temp)
    return results

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
