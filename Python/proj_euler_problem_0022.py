'''
Problem 22
Names scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text 
file containing over five-thousand first names, begin by sorting it into 
alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a 
name score.

For example, when the list is sorted into alphabetical order, COLIN, which 
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, 
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
'''

import math
import sys
import string


def EulerProblem0022():
    namestr = ""
    with open("names.txt", "r") as f:
        namestr = f.readline()
    
    names = [x[1:-1] for x in namestr.split(",")]
    names.sort()
    # adjust array so that data starts from index 1
    names.insert(0, "")

    # Pick capital letters and adjust so that letter index begins from 1
    letters = "0" + string.letters[26:]
    
    sum = 0
    for i in range(1, len(names)):
        let_sum = 0
        for ch in names[i]:
            let_sum += letters.index(ch)
        sum += i * let_sum
    
    print sum
    
if __name__ == "__main__":
    EulerProblem0022()
    