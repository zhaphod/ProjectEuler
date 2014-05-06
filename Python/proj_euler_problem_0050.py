'''
Problem 50
Consecutive prime sum

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime 
below one-hundred.

The longest sum of consecutive primes below one-thousand that adds 
to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most 
consecutive primes?
'''

'''
NOTE: Running this program for primes < 1000000 will take a very long
time to complete. Instead run the Julia implementation of this problem.
'''

import math
import sys

def genPrimes(primes, maxprime):
    primes.append(2)
    
    for i in range (3, maxprime, 2):
        for j in range (2, int(math.ceil(math.sqrt(i))) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)

    #print(primes)

def EulerProblem0050():
    primes= []
    genPrimes(primes, 1000000)
    print("completed generating primes")

    seq_len = 0
    prime  = 0
    for i in range(len(primes)):
        sum = 0
        if i % 1000 == 0:
            print("iteration = ", i)
            
        for j in range(i, len(primes)):
            sum += primes[j]
            if sum > primes[-1]:
                break
            
            if sum in primes:
                if j - i > seq_len:
                    seq_len = j - i
                    prime = sum
                    
    print(seq_len, prime)
if __name__ == "__main__":
    EulerProblem0050()
    