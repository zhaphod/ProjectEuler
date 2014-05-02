'''
Problem 6
Sum square difference

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the 
first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
'''

import sys
import os
import math

def EulerProblem0006():
    n = 100
    sum_n = (n * (n + 1)) / 2
    sqr_sum_n = sum_n * sum_n
    
    sqr_sum = (n * (n + 1) * (2 * n  + 1)) / 6

    print(sqr_sum_n - sqr_sum)
    
if __name__ == "__main__":
    EulerProblem0006()