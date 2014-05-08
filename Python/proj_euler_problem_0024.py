'''
Problem 24
Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is 
one possible permutation of the digits 1, 2, 3 and 4. If all of the 
permutations are listed numerically or alphabetically, we call it 
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

import math
import sys

def genPermutation(numbers, partperm, perms):
    if numbers == []:
        perms.append(partperm)
        return
    else:        
        for x in numbers:
            temp = numbers[:]
            temp.remove(x)
            genPermutation(temp, partperm + str(x), perms)
            
def EulerProblem0024():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    perms = []
    genPermutation(numbers, "", perms)
    #print perms
    print len(perms)
    perms.sort()
    print perms[1000000 - 1]

if __name__ == "__main__":
    EulerProblem0024()
    
