#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s: str) -> int:
    n = len(s)
    sub_strings = {}
    anagrams = 0

    for i in range(n):
        for j in range(i+1, n+1):
            sub = "".join(sorted(s[i:j]))
            
            if sub in sub_strings:
                sub_strings[sub] += 1
            else:
                sub_strings[sub] = 1
                
    print(sub_strings)

    for i in sub_strings:
        n = sub_strings[i] - 1
        anagrams += int((n * (n+1)) / 2) # if n = 0 -> anagram = 0, else
        print(n, anagrams)

    return anagrams

    # for i in range(1, len(s)):
    #     for j in range(len(s) - i + 1):
    #         substrings[''.join(sorted(s[j:j+i]))] += 1

    # ans = 0
    # for key, value in substrings.items():
    #     ans += value*(value-1) // 2

    # print(ans)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
