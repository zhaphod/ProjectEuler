/*
 * Problem 7
 * 10001st prime
 *
 * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
 * we can see that the 6th prime is 13.
 * 
 * What is the 10001st prime number?
 * 
 */

package main

import (
    "fmt"
    "math"
)

func isPrime(a uint64) bool {
    var a_float float64 = float64(a)
    var b uint64 = uint64(math.Sqrt(a_float))
    var i uint64 = 0
    for i = 2; i <= b; i++ {
        if a % i == 0 {
            return false
        }
    }
    return true
}

func main() {
    var a uint64 = 10001
    var n uint64 = 0
    var num uint64 = 2
    
    for {
        if isPrime(num) {
            n++
            if n == a {
                fmt.Println(num)
                return
            }
        }
        num += 1
    }
}    