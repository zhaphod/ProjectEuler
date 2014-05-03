'''
Problem 17
Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 
20 letters. The use of "and" when writing out numbers is in compliance with 
British usage.
'''
import math
import sys

tens = {
     1 : "one",
     2 : "two",
     3 : "three",
     4 : "four",
     5 : "five",
     6 : "six",
     7 : "seven",
     8 : "eight",
     9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety"
}    



def EulerProblem0017():
    n = 1000
    words = ""
    sep = ""
    for i in range(1, n + 1):
        x = i
        
        y = x % 100
        
        if y >= 10 and y <= 19:
            words += tens[y] + sep        
        else:
            z = (y / 10) * 10
            if z in tens:
                words += tens[z] + sep        
            z = y % 10
            if z != 0:
                words += tens[z] + sep        
            
        if x > 99:
            if x == 1000:
                words += "one" + sep + "thousand"                
            elif x % 100 == 0:
                words += tens[x / 100] + "hundred"
            else:   
                x = x / 100
                
                if x % 10 != 0:
                    words += tens[x % 10] + "hundred" + sep + "and"
        
    print words
    print len(words)
        
if __name__ == "__main__":
    EulerProblem0017()