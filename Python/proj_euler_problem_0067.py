'''
Problem 67
Maximum path sum II

By starting at the top of the triangle below and moving to adjacent 
numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click 
and 'Save Link/Target As...'), a 15K text file containing a triangle 
with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not 
possible to try every route to solve this problem, as there are 299 
altogether! If you could check one trillion (10^12) routes every second 
it would take over twenty billion years to check them all. There is an 
efficient algorithm to solve it. ;O)
'''

import math
import sys

pyramid = [
    [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
    ],
    [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [04, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
    ],
    [
    ]
]    

def EulerProblem0067():
    with open("triangle.txt", "r") as f:
        arr = f.readlines()
    
    for line in arr:
        pyramid[2].append([int(x) for x in line.split()])
        
    tri = pyramid[2]
    path_sum = tri[-1]
    for i in range(len(tri) - 1 - 1, -1, -1):
        row_curr = tri[i]
        row_next = path_sum
        path_sum = []
        for j in range(len(row_curr)):
            path_sum.append(max(row_curr[j] + row_next[j], row_curr[j] + row_next[j + 1]))
    print path_sum
    
if __name__ == "__main__":
    EulerProblem0067()
    
