'''
Problem 4
Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import math
import sys

palindromes = []
def isPalindrome(number):
	n = number
	reverse = 0
	while(n > 0):
		reverse = reverse * 10 + n % 10
		n = math.floor(n / 10)
	return number == reverse

def EulerProblem0004():
	for i in range(100, 1000, 1):
		for j in range(100, 1000, 1):
			if isPalindrome(i * j):
				palindromes.append(i * j)

	maxPalindrome = max(palindromes)

	print(maxPalindrome)
if __name__ == "__main__":
	EulerProblem0004()
	
