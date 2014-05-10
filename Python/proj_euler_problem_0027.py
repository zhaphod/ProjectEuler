'''
Problem 27
Quadratic primes

Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive 
values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly 
divisible by 41.

The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 
primes for the consecutive values n = 0 to 79. The product of the 
coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of n, 
starting with n = 0.
'''

import math
import sys
import numpy as np

def prime6(upto):
    primes=np.arange(3,upto+1,2)
    isprime=np.ones((upto-1)/2,dtype=bool)
    for factor in primes[:int(np.sqrt(upto))]:
        if isprime[(factor-2)/2]: isprime[(factor*3-2)/2::factor]=0
    return np.insert(primes[isprime],0,2)

def EulerProblem0027():
    maxprime = 100000
    primes = prime6(maxprime)
    
    #b = [x for x in primes if x <= 1000]
        
    n = np.arange(0, 199, dtype = np.int64)
    sqr_n = n * n
    
    a = np.arange(-999, 1000, dtype = np.int64)
    b = np.arange(-999, 1000, dtype = np.int64)
    maxl = 0
    maxa = 0
    maxb = 0
    F = np.arange(1, dtype = np.int64)
    for x in a:
        for y in b:
            F = sqr_n + n * x + y

            seqlen = 0
            for fx in F:
                if fx in primes:
                    seqlen += 1
                else:
                    break
            #print x, y, seqlen
            if seqlen > maxl:
                maxl = seqlen
                maxa = x
                maxb = y
        if x % 100 == 0:
            print "iteration = ", x
            print maxl, maxa, maxb, maxa * maxb
    print maxl, maxa, maxb, maxa * maxb
if __name__ == "__main__":
    EulerProblem0027()
