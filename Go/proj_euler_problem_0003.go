/*
 * Problem 3
 * Largest prime factor
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * 
 * What is the largest prime factor of the number 600851475143 ?
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
    var a uint64 = 600851475143
    var b uint64 = uint64(math.Sqrt(float64(a)))
    var max_multiple uint64 = 1
    var i uint64 = 0
    
    for i = 2; i < b; i++ {
        if a % i == 0 {
            if isPrime(i) {
                fmt.Println("prime multiple", i)
                if i > max_multiple {
                    max_multiple = i
                }
            }
        }
    }
    fmt.Println(max_multiple)
}    