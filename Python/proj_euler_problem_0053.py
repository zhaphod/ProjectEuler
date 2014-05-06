'''
Problem 53
Combinatoric selections

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr = n! / (r! * (n - r)!)

where r <= n, n! = n*(n - 1)*...*3*2*1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, 
are greater than one-million?
'''
import math
import sys

def printPascalsTriangle():
    input = 100
    triangle = []
    countExceed10e6 = 0
    for i in range(0, input + 1):
        lenRowI = i + 1
        row = [0 for k in range(0, lenRowI)]
        triangle.append(row)
        triangle[i][0] = 1
        triangle[i][-1] = 1
        for j in range(0, i - 1):
            triangle[i][j + 1] = triangle[i - 1][j] + triangle[i - 1][j + 1]
            if triangle[i][j + 1] > 1000000:
                countExceed10e6 += 1
        print(i, triangle[i])

    print(countExceed10e6)
def EulerProblem0053():
    printPascalsTriangle()
            
if __name__ == "__main__":
    EulerProblem0053()
    
