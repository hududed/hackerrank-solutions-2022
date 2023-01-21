#!/bin/python3

import math
import os
import random
import re
import sys
import string
#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s: str, k: int) -> str:
    res=""
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                """len(symbols_up) = len(symbols_low) = 26 if we don't add %26,
                then the integer value of the character resulting from adding k
                to the original integer value of the character, may exceed the
                integer value of the last character which is 'z' in case of
                lowercase and 'Z' in case of uppercase. Therefore, we add %26
                (which equals len(symbols_low) and len(symbols_up)) to apply the
                rotation without exceeding the allowed integer value. 
                """
                res+=chr(ord('A')+(ord(s[i])-ord('A')+k)%26)
            else:
                res+=chr(ord('a')+(ord(s[i])-ord('a')+k)%26)    
        else:
            res+=s[i]
    return res
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

