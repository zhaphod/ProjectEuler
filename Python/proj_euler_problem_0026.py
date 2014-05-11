'''
Problem 26
Reciprocal cycles

A unit fraction contains 1 in the numerator. The decimal representation 
of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can 
be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring 
cycle in its decimal fraction part.
'''
'''
Opinions about the solution:

The solution doesn't look elegant. It is analysing a 2000 digit number for 
tokens of size from 1 to 1000. 
Is there a better way to do it?

Initially the loop was for 1000 digit number with token len running upto 500. 
This missed the number 983 which has a period of 982. Was able to figure it 
out based on following:

http://en.wikipedia.org/wiki/Repeating_decimal
http://www.wolframalpha.com/input/?i=1%2F983

Need to come up with better algorithm. Furthermore python can do 2000 digit 
calculations. How to do it in Go?
'''

import math
import sys
import numpy as np
import pdb

def EulerProblem0026():
    maxtklen = 0
    maxtk = ""
    maxn = 0
    longseq = ""
    maxlongseq = 0
    maxlongseqn = 0
    maxmaxlen = 0
    maxmax = {}
    for n in xrange(2, 1000):
        rem = str((10 ** 2000) / n)
        if len(rem) < 2000:
            rem = "0"*(2000 - len(rem)) + rem
            
        # For each token of length from 1 to len(rem) / 2 do
        print rem, "\t", n
        print >> sys.stderr, n
        keys = sorted(maxmax.keys())
        startindex = 981
        if len(keys) > 0:
            startindex = keys[-1]
            
            
        print >> sys.stderr,  startindex, len(rem) / 2
        for tklen in xrange(startindex, len(rem) / 2):
            #print "\t", "n = ", n, " tklen = ", tklen

            tokens = []
            tkset  = {}
            # Generate all tokens of size tklen -> [1, 2, ..., len(rem) / 2]
            for index in xrange(0, len(rem) - tklen):
                substr = rem[index:index + tklen]
                #print substr, tklen
                if len(substr) > 1 and substr.count(substr[0]) == len(substr): continue
                tokens.append(substr)
            
            # obtain unique tokens of len tklen            
            tkset = set(tokens)
            #print tkset, rem
            
            # Need to find which tk of tklen occurs the most number of subsequent times
            maxseqlen = 0
            maxseq = ""
            
            # For each tk of len tklen do
            for tk in tkset:
                tkindex = []
                start = 0
                index = 0
                # Find all locations of the given tk of len tklen
                while True:
                    try:
                        index = rem.index(tk, start)
                    except:
                        break
                    tkindex.append(index)
                    start = index + 1
                    if start >= len(rem):
                        break
                
                # Find the longest increasing subsequence of indices for the given tk of len tklen
                seqlen = 1
                prev = tkindex[0]
                for index in tkindex[1:]:
                    if index == prev + len(tk):
                        seqlen += 1
                    else:
                        if maxseqlen < seqlen:
                            maxseqlen = seqlen
                        seqlen = 1
                    prev = index
                    
                # Remember the tk of length tklen which has the longest increasing subsequence of indices
                if maxseqlen < seqlen:
                    maxseqlen = seqlen
                    maxseq = tk
                    if maxseqlen > 1:
                        #print "$$$ ", maxseqlen, "    ", maxseq, "    ", len(maxseq)
                        if len(maxseq) not in maxmax:
                            maxmax[len(maxseq)] = []
                        maxmax[len(maxseq)].append((maxseq, n))
                    
                #print tk, tkindex, maxseqlen
        
            # Now find out whether this particular tklen is the one which has maximum increasing subsequence of all tklens.
            if maxseqlen > maxtklen:
                maxtklen = maxseqlen
                maxtk = maxseq
                maxn = n
            
#            if len(longseq) * maxlongseq < len(maxtk) * maxtklen:
#                longseq = maxtk
#                maxlongseq = maxtklen
#                maxlongseqn = n
#            
            #if maxtklen > 1:
            if len(longseq) < len(maxtk):
                longseq = maxtk
                maxlongseq = maxtklen
                maxlongseqn = n
                    
            #print "\t", "maxtklen = ", maxtklen, " tk = ", maxtk, " maxn = ", maxn
            #print "\t\t", "longseq = ", longseq, " maxlongseq = ", maxlongseq, " n = ", maxlongseqn
    
    print "=="*10
    print maxtk, maxtklen, maxn
    keys = sorted(maxmax.keys())
    
    for x in keys[::-1]:
        print x, maxmax[x]
        
if __name__ == "__main__":
    EulerProblem0026()
