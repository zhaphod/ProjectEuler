'''
Problem 19
Counting Sundays

You are given the following information, but you may prefer to do some 
research for yourself.

1 Jan 1900 was a Monday.

Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century 
unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
'''

import math
import sys

months = [ ("jan", 31), 
           ("feb", 28), 
           ("mar", 31), 
           ("apr", 30), 
           ("may", 31), 
           ("jun", 30), 
           ("jul", 31), 
           ("aug", 31), 
           ("sep", 30), 
           ("oct", 31), 
           ("nov", 30), 
           ("dec", 31) ]

days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
           
def EulerProblem0019():
    start = 1
    # Generate start day for 1901
    for m, n in months:
        # print m, n
        week = ""
        for x in range(1, n + 1):
            week += str((days[start], x))
            start = (start + 1) % 7
            if start == 0:
                # print week
                week = ""
        else:
            # print week
            pass
    
    cnt_sun_1st = 0
    
    # print start
    
    # Now calculate number of sundays falling on 1st of a month
    for year in range(1901, 2000 + 1):
        for m, n in months:
            # print m, n
            if m == "feb":
                if year % 4 == 0:
                    n = 29
                    if year % 100 == 0 and year % 400 != 0:
                        n = 28
                    
            week = ""
            for x in range(1, n + 1):
                if start == 0 and x == 1:
                    cnt_sun_1st += 1
                week += str((days[start], x))
                start = (start + 1) % 7
                if start == 0:
                    # print week
                    week = ""
            else:
                # print week
                pass
    print "cnt_sun_1st = ", cnt_sun_1st
    
if __name__ == "__main__":
    EulerProblem0019()