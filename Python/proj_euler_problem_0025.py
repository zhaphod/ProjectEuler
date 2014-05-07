'''
Problem 25
1000-digit Fibonacci number

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
'''

import math
import sys

def EulerProblem0025():
    a, b = 1, 1
    count = 1
    while True:
        a, b = b, a + b
        count += 1
        if len(str(a)) == 1000:
            print "1000 digit sequence \n", a
            print count
            break
        print len(str(a))
        
if __name__ == "__main__":
    EulerProblem0025()
    
