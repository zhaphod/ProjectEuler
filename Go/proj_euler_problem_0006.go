/*
 * Problem 6
 * Sum square difference
 *
 * The sum of the squares of the first ten natural numbers is,
 * 
 * 1^2 + 2^2 + ... + 10^2 = 385
 *
 * The square of the sum of the first ten natural numbers is,
 * 
 * (1 + 2 + ... + 10)^2 = 55^2 = 3025
 *
 * Hence the difference between the sum of the squares of the 
 * first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
 * 
 * Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
 *
 */

package main

import (
    "fmt"
)


func main() {
    var a uint64 = 100
    var sum_n uint64 = a * (a + 1) / 2
    var sqr_sum_n uint64 = sum_n * sum_n
    var sum_sqr uint64 = a * (a + 1) * (2 * a + 1) / 6
    
    fmt.Println(sqr_sum_n - sum_sqr)
}    