'''
Problem 38
Pandigital multiples

Take the number 192 and multiply it by each of 1, 2, and 3:

192 * 1 = 192
192 * 2 = 384
192 * 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 
192384576. We will call 192384576 the concatenated product 
of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying 
by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which 
is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can 
be formed as the concatenated product of an integer with 
(1,2, ... , n) where n > 1?
'''

import math
import sys
import numpy as np
import pdb


def EulerProblem0038():
    maxp = 0
    maxdick = None
    digits = "123456789"
    for x in xrange(100000, 1, -1):
        for y in xrange(2, 10):
            dick = [x * m for m in range(1, y + 1)]
            val =  reduce(lambda a, b: str(a)+str(b), dick)
            if len(val) < 10 and int(val) > maxp and "".join(sorted(list(val))) == digits:
                maxp = int(val)
                maxdick = dick
    print maxp
    print maxdick
if __name__ == "__main__":
    EulerProblem0038()
