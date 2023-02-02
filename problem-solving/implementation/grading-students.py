#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
# import math

# def round_to_multiple(number, multiple):
#     return multiple * math.ceil(number / multiple)


def gradingStudents(grades):
    results = []
    for g in grades:
        if g >= 38:
            if g % 5 >= 3:  # if remainder 5-n >= 3 or diff < 3
                g += (5-g % 5)
        results.append(g)
    return (results)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
