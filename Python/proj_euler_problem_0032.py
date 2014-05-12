'''
Problem 32
Pandigital products

We shall say that an n-digit number is pandigital if it makes use of 
all the digits 1 to n exactly once; for example, the 5-digit number, 
15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product 
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to 
only include it once in your sum.
'''

import math
import sys
import numpy as np
import pdb

def EulerProblem0032_2():
    numberstr = "123456789"
    sumpandigital = 0
    size = 10000
    dick = []
    xy = np.ones(size, dtype=int)
    y  = np.arange(size, dtype=int)
    for x in xrange(1, size):
        if x % 100 == 0: print x
        xy = y * x
        for i in xrange(0, size):
            #xy = x * y
            #if xy[i] == 5796: pdb.set_trace()
            xystr = str(x) + str(y[i]) + str(xy[i])
            if len(xystr) != 9: continue

            truth = [0 for m in xrange(9)]
            truth.insert(0, 1)
            xystr = [int(m) for m in xystr]
            
            for m in xystr:
                truth[m] = 1
            if all(truth):
                sumpandigital += xy[i]
                print truth, xy[i], sumpandigital
                    
    print sumpandigital

def EulerProblem0032():
    numberstr = "123456789"
    dick = []
    for x in xrange(0, 10000):
        if x % 100 == 0: print x
        for y in xrange(0, 1000000):
            xy = x * y
            
            xystr = str(x) + str(y) + str(xy)
            xystr = list(xystr)
            xystr = sorted(xystr)
            xystr = "".join(xystr)
            if len(set(list(xystr))) > 9: break
            
            if xystr == numberstr:
                #if xystr not in dick:
                #dick.append((x,y,x*y))
                dick.append(xy)
    print dick
    
    
    #sumpandigital = 0
    #for (x,y,z) in dick:
    #    sumpandigital += z
    dick = set(dick)
    print dick
    sumpandigital = sum(dick)
    print sumpandigital
            
if __name__ == "__main__":
    EulerProblem0032()
