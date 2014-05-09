'''
Problem 30
Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum 
of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth 
powers of their digits.
'''
import math
import sys
import operator

fifth_power = [ x ** 5 for x in range(0, 10) ]
digit_power = []

def EulerProblem0030():
    for x in xrange(2, 1000000):
        digits = [fifth_power[int(y)] for y in str(x)]
        digit_sum = sum(digits)
        if digit_sum == x:
            digit_power.append(x)
    print digit_power, sum(digit_power)
    
if __name__ == "__main__":
    EulerProblem0030()
