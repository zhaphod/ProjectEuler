'''
Problem 34
Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the 
factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import math
import sys
import numpy as np
import pdb
import scipy as sp
import operator

def EulerProblem0034():
    sumdigitfact = 0
    arr = []
    for x in xrange(3, 10000000):
        nums = [int(m) for m in str(x)]
        fact = [math.factorial(m) for m in nums]
        sumfact = reduce(operator.add, fact)
         
        if sumfact != x: continue
        
        sumdigitfact += x
        arr.append(x)
        print sumdigitfact, x
    print arr
    print sumdigitfact
            
if __name__ == "__main__":
    EulerProblem0034()
