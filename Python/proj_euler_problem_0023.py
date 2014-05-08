'''
Problem 23
Non-abundant sums

A perfect number is a number for which the sum of its proper divisors 
is exactly equal to the number. For example, the sum of the proper 
divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 
is a perfect number.

A number n is called deficient if the sum of its proper divisors is 
less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the 
smallest number that can be written as the sum of two abundant numbers 
is 24. By mathematical analysis, it can be shown that all integers 
greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis 
even though it is known that the greatest number that cannot be expressed 
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the 
sum of two abundant numbers.
'''
'''
NOTE: Running this program will take a long time to complete. 
Julia version is also available.
'''

import math
import sys
import string
import operator

def genPrimes(primes, maxprime):
    primes.append(2)
    
    for i in range (3, maxprime, 2):
        for j in range (2, int(math.ceil(math.sqrt(i))) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)

    #print(primes)
def genPrimeFactors(n, primes, pfactors, multiplicity):  
    for prime in primes:
        temp_n = n
        if prime <= n and n % prime == 0:
            count = 0
            while True:
                if temp_n % prime == 0:
                    count += 1
                    temp_n /= prime
                else:
                    break
            pfactors.append(prime)
            multiplicity.append(count)
        
def genAllFactors(primes, multiplicity, index, factor, allfactors):
    if index == len(primes):
        #print factor
        allfactors.append(factor)
        return
    else:
        for i in range(multiplicity[index] + 1):
            genAllFactors(primes, multiplicity, index + 1, factor, allfactors)
            factor *= primes[index]

def EulerProblem0023():
    number = 28123
    primes = []
    genPrimes(primes, number)
    print "Generated primes"
    
    num = [x for x in xrange(number + 1)]
    abundant = []
    for i in range(1, number + 1):
        if i % 1000 == 0: print "Completed iteration = ", i
        
        x = num[i]
        pfactors = []
        multiplicity = []
        genPrimeFactors(x, primes, pfactors, multiplicity)
 
        allfactors = []
        genAllFactors(pfactors, multiplicity, 0, 1, allfactors)
        
        sumfactors = reduce(operator.add, allfactors) - x
        
        if sumfactors > x:
            #print x, allfactors, sumfactors
            abundant.append(x)

    print "Done calculating abundant elements: len = ", len(abundant)
    weirdnum = []
    for n in num:
        weird = True
        if n % 1000 == 0: print "Weird iteration = ", n
        for x in abundant:
            if x > n: break
            for y in abundant:
                if x + y > n: break
                if x + y == n:
                    weird = False
                    break
            if not weird: break
        if weird: weirdnum.append(n)
    
    print "Sum of weirds = ", sum(weirdnum)
    
if __name__ == "__main__":
    EulerProblem0023()
    