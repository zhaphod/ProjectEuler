'''
Problem 56
Powerful digit sum

A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is 
the maximum digital sum?
'''
import math
import sys


def EulerProblem0056():
    maxSum = 0

    for i in range (1, 100):
        for j in range(1, 100):
            number = i ** j
            tempSum = 0
            for k in str(number):
                tempSum += int(k) 
            if maxSum < tempSum:
                maxSum = tempSum 
            #print("(", i, j, ")", number, tempSum, maxSum)

    print(maxSum)
            
    
if __name__ == "__main__":
    EulerProblem0056()
    
