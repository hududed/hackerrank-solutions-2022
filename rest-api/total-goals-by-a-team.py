#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#
import requests


def getTotalGoals(team: str, year: int) -> int:

    c = 0
    r = requests.get(
        f'https://jsonmock.hackerrank.com/api/football_matches?year={str(year)}&team1={str(team)}').json()
    total_pages_1 = r['total_pages']
    per_page_2 = r['per_page']
    for page in range(1, total_pages_1 + 1):
        r = requests.get(
            f'https://jsonmock.hackerrank.com/api/football_matches?year={str(year)}&team1={str(team)}&page={str(page)}').json()
        try:
            for i in range(0, per_page_2):
                team1 = r['data'][i]['team1goals']
                c += int(team1)
        except:
            pass

    r_1 = requests.get(
        f'https://jsonmock.hackerrank.com/api/football_matches?year={str(year)}&team2={str(team)}').json()
    total_pages_2 = r_1['total_pages']
    per_page_2 = r['per_page']
    for page in range(1, total_pages_2+1):
        r_1 = requests.get(
            f'https://jsonmock.hackerrank.com/api/football_matches?year={str(year)}&team2={str(team)}&page={str(page)}').json()
        try:
            for i in range(0, per_page_2):
                team2 = r_1['data'][i]['team2goals']
                c += int(team2)
        except:
            pass

    return c


if __name__ == '__main__':
    result = getTotalGoals('APOEL Nikosia', 2011)
    print(result)
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # team = input()

    # year = int(input().strip())

    # result = getTotalGoals(team, year)

    # fptr.write(str(result) + '\n')

    # fptr.close()
