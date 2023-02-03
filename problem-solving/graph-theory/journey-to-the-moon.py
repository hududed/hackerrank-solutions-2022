#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#
sys.setrecursionlimit(10**8)


def journeyToMoon(n, astronaut):
    # create adjacency list for graph edges
    graph = [[] for _ in range(n)]  # id starts from 0

    for x, y in astronaut:
        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * n

    # calc total pairs
    pairs = n * (n-1) // 2

    # dfs to find n_person in 1 country (subset)
    def dfs(u, graph, visited):
        visited[u] = True
        # vertices is the person
        vertices = 1
        for v in graph[u]:
            if visited[v] == False:
                vertices += dfs(v, graph, visited)
        return vertices

    # main logic
    for v in range(n):
        # print(v, visited, pairs)
        if visited[v] == False:
            n_persons = dfs(v, graph, visited)
            # print(n_persons)
            # remove possible combinations from same country
            pairs -= n_persons * (n_persons - 1) // 2
    return pairs

    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
