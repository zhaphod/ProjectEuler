'''
 Problem 14
 Longest Collatz sequence
 
 The following iterative sequence is defined for the set of positive
 integers:
 
 n => n/2 (n is even)
 n => 3n + 1 (n is odd)
 
 Using the rule above and starting with 13, we generate the following 
 sequence:
 
 13 => 40 => 20 => 10 => 5 => 16 => 8 => 4 => 2 => 1
 It can be seen that this sequence (starting at 13 and finishing at 1) 
 contains 10 terms. Although it has not been proved yet (Collatz Problem), 
 it is thought that all starting numbers finish at 1.
 
 Which starting number, under one million, produces the longest chain?
 
 NOTE: Once the chain starts the terms are allowed to go above one million.
'''

import math
import sys

steps = [0, 4]
maximum = 4
index = 1
def EulerProblem0014():
	global maximum
	global steps
	global index
	for i in range(2, 1000000 + 1):
		j = i
		steps.append(1)
		while j != 1:
			if j % 2:
				j = 3 * j + 1
			else:
				j = math.floor(j / 2)
			steps[i] += 1
		if maximum < steps[i]:
			maximum = steps[i]
			index = i
			print(index, maximum)
			
if __name__ == "__main__":
	EulerProblem0014()
	
