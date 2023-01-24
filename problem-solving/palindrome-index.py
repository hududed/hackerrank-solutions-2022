
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def isPalindrome(s): return s == s[::-1]


def palindromeIndex(s):
    """
        aaab        aaa
        |  |
        traverse half
    """
    if isPalindrome(s):
        return -1

    for i in range(len(s)//2):
        last = len(s)-i-1
        if s[i] != s[last]:
            sliced = s[:i]+s[i+1:]
            if isPalindrome(sliced):
                return i
            elif isPalindrome(s[:last]+s[last+1:]):
                return last
            return -1
        # print(i, s[i], s[len(s)-i-1])

    # print(s, s[::-1])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()

#! /bin/python3


def isPalindrome(s): return s == s[::-1]


def palindromeIndex(s):
    if isPalindrome(s):
        return -1
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            if isPalindrome(s[:i]+s[i+1:]):
                return i
            elif isPalindrome(s[:len(s)-1-i]+s[len(s)-i:]):
                return len(s)-1-i
            return -1
