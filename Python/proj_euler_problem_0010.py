'''
Problem 10
Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import math
import sys


def findPrimes():
    input = 2000000
    primes = [2]
    
    primeFlag = 1
    for i in range (3, input + 1, 2):                
        for j in range (2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                primeFlag = 0
                break
        if primeFlag:
            primes.append(i)
        else:
            primeFlag = 1
    sum = 0
    for i in primes:
        sum += i
    
    print(sum)

            
def EulerProblem0010():
    findPrimes()
        
if __name__ == "__main__":
    EulerProblem0010()
    