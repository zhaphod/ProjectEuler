'''
Problem 39
Integer right triangles

If p is the perimeter of a right angle triangle with integral length 
sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
'''

import math
import sys
import numpy as np


def EulerProblem0039():
    size = 1000
    maxp = 1000
    
    c = np.arange(1, size, dtype=int)
    cc = c * c
    
    a = np.arange(1, size, dtype=int)
    aa = a * a
        
    dick = {}
    
    for i in xrange(len(aa)):
        fx = aa[i] + aa
        
        for j in xrange(len(fx)):
            if fx[j] in cc:
                sqrtfx = int(np.sqrt(fx[j]))
                peri = a[i] + a[j] + sqrtfx 
                if (peri <= maxp):
                    #print a[i], a[j], sqrtfx
                    tup = None
                    if a[i] > a[j]:
                        tup = (a[j], a[i], sqrtfx)
                    else:
                        tup = (a[i], a[j], sqrtfx)
                    if peri not in dick:
                        dick[peri] = []
                    if tup not in dick[peri]:
                        dick[peri].append(tup)
                        
    maxp = 0
    maxc = []
    for k, v in dick.items():
        if len(v) > len(maxc):
            maxc = v
            maxp = k
            
    print maxp
    print len(maxc)
    print maxc
if __name__ == "__main__":
    EulerProblem0039()
