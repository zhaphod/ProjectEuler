'''
Problem 16
Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

import math
import sys


if __name__ == "__main__":
	value = 2 ** 1000
	digitSum = 0
	for k in str(value):
		digitSum += int(k)
	
	print(value)
	print(digitSum)
