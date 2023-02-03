#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#
from collections import deque

# sys.setrecursionlimit(10**8)


def bfs(n, m, edges, s):
    graph = [[] for _ in range(n+1)]  # starts with 1
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * (n+1)
    distances = [-1] * (n+1)

    q = deque([(s, 0)])
    distances[s] = 0
    visited[s] = True

    # main
    while q:
        u, w = q.popleft()

        for v in graph[u]:
            # print(q, v, distances, visited)
            if visited[v] == False:
                distances[v] = w + 6
                visited[v] = True
                q.append((v, w+6))

    distances.remove(0)
    return distances[1:]

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
