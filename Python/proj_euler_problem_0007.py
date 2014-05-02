'''
Problem 7
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10001st prime number?
'''
import math
import sys
input = 0
primes = [2, 3]
factors = []

def findPrimes():
	primeFlag = 1
	found = 0
	number = 5
	
	for i in range (2, input):
		while found == 0:
			for j in range (2, math.ceil(math.sqrt(number)) + 1):
				if number % j == 0:
					primeFlag = 0
					break
			if primeFlag:
				found = 1
				primes.append(number)
			else:
				primeFlag = 1
			
			number += 2
		
		found = 0
	print(primes[-1])

#	print(primes)
			
def EulerProblem0003 ():
	global factors
	findPrimes()
	
	
if __name__ == "__main__":
	input = int(sys.argv[1])
	EulerProblem0003 ()
	