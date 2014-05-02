'''
Problem 9
Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, 
a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import math
import sys


if __name__ == "__main__":
	for i in range(1, 1000 + 1, 2):
		for j in range(2, 1000 + 1, 2):
			for k in range(1, 1000 + 1, 2):
				if ((i * i + j * j) == k * k) and (i + j + k == 1000):
					print(i, j, k, i * j * k)
