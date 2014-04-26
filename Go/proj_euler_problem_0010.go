/*
 * Problem 10
 * Summation of primes
 *
 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 * 
 * Find the sum of all the primes below two million.
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
    var a uint64 = 2000000
    var sum uint64 = 0
    var i uint64 = 1
    for i = 2; i <= a; i++ {
        if isPrime(i) {
            sum += i
        }
    }
    fmt.Println(sum)
}    