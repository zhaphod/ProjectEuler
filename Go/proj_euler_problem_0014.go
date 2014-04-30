/*
 * Problem 14
 * Longest Collatz sequence
 * 
 * The following iterative sequence is defined for the set of positive
 * integers:
 * 
 * n → n/2 (n is even)
 * n → 3n + 1 (n is odd)
 * 
 * Using the rule above and starting with 13, we generate the following 
 * sequence:
 * 
 * 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
 * It can be seen that this sequence (starting at 13 and finishing at 1) 
 * contains 10 terms. Although it has not been proved yet (Collatz Problem), 
 * it is thought that all starting numbers finish at 1.
 * 
 * Which starting number, under one million, produces the longest chain?
 * 
 * NOTE: Once the chain starts the terms are allowed to go above one million.
 *
 */

package main

import (
    "fmt"
)
func main() {
    var max_chain = 0
    var max_num = 0
    var curr_chain = 0
    
    for j := 2; j < 1000000; j++ {
        curr_chain = 1
        i := j
        for {
            if i == 1 {
                break
            }
            
            if i % 2 == 0 {
                i = i / 2
            } else {
                i = i * 3 + 1
            }
            curr_chain += 1
        }
        if curr_chain > max_chain {
            max_chain = curr_chain
            max_num = j
        }
        //fmt.Println(j, max_chain, max_num)
    }
    fmt.Println(max_num, max_chain)
}    