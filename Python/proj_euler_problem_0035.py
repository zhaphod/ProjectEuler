'''
Problem 35
Circular primes

The number, 197, is called a circular prime because all rotations of 
the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

import math
import sys
import numpy as np
import pdb

def prime6(upto):
    primes=np.arange(3,upto+1,2)
    isprime=np.ones((upto-1)/2,dtype=bool)
    for factor in primes[:int(np.sqrt(upto))]:
        if isprime[(factor-2)/2]: isprime[(factor*3-2)/2::factor]=0
    return np.insert(primes[isprime],0,2)

def isRotation(num):
    strnum = str(num)
    dick = [int(strnum[x:] + strnum[:x]) for x in xrange(len(strnum))] 
    return dick
def EulerProblem0035():
    maxp = 1000000
    primes = prime6(maxp)
    dick = []
    for x in primes:
        rotation =  isRotation(x)
        for rot in rotation:
            if rot not in primes:
                break
        else:
            dick.append(x)
    
    print len(dick), dick
if __name__ == "__main__":
    EulerProblem0035()
