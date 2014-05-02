'''
Problem 3
Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''

import math
import sys
input = 0
primes = [2, 3]
factors = []

def findFactorsJunk():
	global factors

	primeFlag = True
	
	for i in range (3, math.ceil(input / 2)  + 1, 2):
		if i % 3:
			#print("[i][sqrt] = " + str(i) + " " + str(math.ceil(math.sqrt(i))))
			for j in range (2, math.ceil(math.sqrt(i)) + 1):
				temp = (j - 1) / 6
				temp2 = temp - math.floor(temp)
				#print(i, j, temp, temp2)
				if temp2 == 0:
					if i % j == 0:
						primeFlag = False
						break
			if primeFlag:
				print("prime number = " + str(i))
				if input % i == 0:
					factors.append(i)
			else:
				primeFlag = True
			
	
	print(factors)
			
def findPrimes():
	primeFlag = 1
	for i in range (3, math.ceil(input / 2) + 2, 2):				
		for j in range (2, math.ceil(math.sqrt(i)) + 2):
			if i % j == 0:
				primeFlag = 0
				break
		if primeFlag:
			primes.append(i)
		else:
			primeFlag = 1
	for i in primes:
		print(i, end = " ")


def findFactors():
	global factors
	global primes

	primeFlag = 1
	
	for i in range (3, math.ceil(input / 2)  + 1, 2):
		if i % 100000 < 3:
			print("Iteration = " + str(i))

		for k in primes:
			print("one", i, k)
			if i % k == 0:
				primeFlag = 0
				break
				
		if primeFlag:
			for j in range (2, math.ceil(math.sqrt(i)) + 2):
				print("two", i, j)
				if i % j == 0:
					primeFlag = 0
					break
		if primeFlag:
			primes.append(i)
			if input % i == 0:
				factors.append(i)
		else:
			primeFlag = 1
	print(factors)
			
def EulerProblem0003 ():
	global factors
	findPrimes()
	
	
if __name__ == "__main__":
	input = int(sys.argv[1])
	EulerProblem0003 ()
	