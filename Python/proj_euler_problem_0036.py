'''
Problem 36
Double-base palindromes

The decimal number, (585)_10 = (1001001001)_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

import math
import sys
import numpy as np
import pdb
def isPalindrome(num):
    pal = True
    
    length = len(num)
    
    rhs = num[0: length / 2]
    if length % 2 == 0:
        lhs  = num[length / 2:]
    else:
        lhs  = num[length / 2 + 1:]
        
    lhs = lhs[::-1]
        
    if rhs == lhs:
        pal = pal and True
    else:
        pal = pal and False
    return pal
    
def getBinRepr(num):
    bin = ""
    digits = ["0", "1"]
    while True:
        bin += digits[num % 2]
        num /= 2
        if num == 0:
            break
    if len(bin[:-1]) > 0 and int(bin[:-1]) == 0:
        bin = bin[::-1]
    return bin
def EulerProblem0036():
    maxp = 1000000
    sump = 0
    for x in xrange(maxp):
        base10 = str(x)
        base2 = getBinRepr(x)
        
        if isPalindrome(base10) and isPalindrome(base2):
            print x        
            sump += x
    print sump
if __name__ == "__main__":
    EulerProblem0036()
