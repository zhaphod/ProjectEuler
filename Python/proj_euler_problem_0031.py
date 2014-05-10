'''
Problem 31
Coin sums

In England the currency is made up of pound, Pounds_, and pence, p, 
and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, Pounds_1 (100p) and Pounds_2 (200p).
It is possible to make Pounds_2 in the following way:

1*Pounds_1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
How many different ways can Pounds_2 be made using any number of coins?
'''

import math
import sys

denom = [1, 2, 5, 10, 20, 50, 100, 200]

def genSequence3(left, change, index, seq):
    if left == 0:
        #print seq
        return 1
    elif left < 0:
        return 0
    else:
        totalsum = 0
        rem = ()
        for i in xrange(index, len(change)):
            d, c = change[i]
            currleft = left
            for x in xrange(c):
                currleft -= d
                #tempsum = genSequence3(currleft, change, i + 1, seq + (str(d) + "_") * (x+1))
                tempsum = genSequence3(currleft, change, i + 1, "")
                totalsum += tempsum
        return totalsum

def EulerProblem0031():
    total = 200
    change = [(d, total / d) for d in denom]
    totalsum = genSequence3(total, change, 0, "")
    print totalsum
    
if __name__ == "__main__":
    EulerProblem0031()
