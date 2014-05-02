'''
Problem 5
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?

'''

'''
Sketch of Solution

To find out LCM of two numbers x and y, express them as product of 
unique primes.
For each of the primes that are used to represent x and y find the maximum
power used for that prime between the two numbers
Calculate LCM = p1**power_max1p2**power_max2

To solve the given problem find the LCM of all numbers from 1 to 20

'''
import sys
import os
import math

def isPrime(a):
    b = math.sqrt(a)
    
    for i in range(2, int(b) + 1):
        if a % i == 0:
            return False
    else:
        return True

def EulerProblem0005():
    a = 20
    primes = []
    
    # We need to find primes that can possibly appear 
    # in the unique factorization of any of the numbers
    # from 1 to 20
    for i in range(2, a + 1):
        if isPrime(i):
            primes.append(i)

    powers = [0 for i in primes]

    # For each such prime find the maximum power used in any of the
    # numbers from 1 to 20
    for i in range(2, a + 1):
        for j in range(len(primes)):
            index = 0
            temp = i
            prime = primes[j]
            
            while temp > 0:
                if temp % prime == 0:
                    index += 1
                    temp /= prime
                else:
                    break
                    
            if powers[j] < index:
                powers[j] = index
    
    # Calculate LCM by multiplying each of the prime raised to its maximum power 
    # used in unique factorization of each of the number from 1 to 20
    
    lcm = 1    
    for i in range(len(primes)):
        lcm *= primes[i] ** powers[i]

    print(lcm)

    
if __name__ == "__main__":
    EulerProblem0005()