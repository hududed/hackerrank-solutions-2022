#! /bin/python3

def isPalindrome(s):return s==s[::-1]

def palindromeIndex(s):
    if isPalindrome(s):return -1
    for i in range(len(s)//2):
        if s[i]!=s[len(s)-1-i]:
            if isPalindrome(s[:i]+s[i+1:]):
                return i
            elif isPalindrome(s[:len(s)-1-i]+s[len(s)-i:]):
                return len(s)-1-i
            return -1
