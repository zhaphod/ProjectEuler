'''
Problem 37
Truncatable primes

The number 3797 has an interesting property. Being prime itself, 
it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. Similarly 
we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable 
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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
    
def EulerProblem0037():
    maxprime = 1000000
    primes = prime6(maxprime)
    panprime = []
    for prime in primes[4:]:
        strprime = str(prime)
        split = [ int(strprime[0:x + 1]) for x in xrange(len(strprime)) ]
        if prime == 3797:
            print split

        l2r = False
        for every in split:
            if every not in primes:
                break
        else:
            l2r = True
            

        #strprime = str(prime)[::-1]
        split = [ int(strprime[x:]) for x in xrange(len(strprime)) ]
        if prime == 3797:
            print split
        r2l = False
        for every in split:
            if every not in primes:
                break
        else:
            r2l = True
        
        if l2r and r2l:
            panprime.append(prime)
            
    print panprime
    print sum(panprime)
if __name__ == "__main__":
    EulerProblem0037()
