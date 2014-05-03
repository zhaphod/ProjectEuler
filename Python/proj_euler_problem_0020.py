'''
Problem 20
Factorial digit sum

n! means n * (n - 1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
import math
import sys

def EulerProblem0020():
    number = 100
    factorial = 1    
    for i in range(1, number + 1):
        factorial *= i
    
    print(factorial)
    sum = 0
    for i in str(factorial):
        sum += int(i)
    print(sum)

    
if __name__ == "__main__":
    EulerProblem0020()