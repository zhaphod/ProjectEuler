'''
Problem 21
Amicable numbers

Let d(n) be defined as the sum of proper divisors 
of n (numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a != b, then a and b 
are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 
284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import math
import sys

def EulerProblem0021():
    divisors = []
    divisors.append([]) #index 0

    sumOfDivisors = []
    sumOfDivisors.append(0)
    
    number = 10000

    for i in range(1, number + 1):
        divisors.append([])
        for j in range(1, int(i / 2) + 1):
            if i % j == 0:
                divisors[i].append(j)

    for i in range(1, number + 1):
        sumOfDivisors.append(0)
        sumOfDivisors[i] = 0
        for j in range(0, len(divisors[i])):
            sumOfDivisors[i] += divisors[i][j]

    amicable = []
    for i in range(2, number + 1):
        if i == sumOfDivisors[i]:
            continue
        a = i       
        b = sumOfDivisors[a]
        if b > number:
            continue
        if a == sumOfDivisors[b]:
            if a not in amicable:
                amicable.append(a)
            if b not in amicable:
                amicable.append(b)
            print(a, b)
            
    print sum(amicable)
if __name__ == "__main__":
    EulerProblem0021()