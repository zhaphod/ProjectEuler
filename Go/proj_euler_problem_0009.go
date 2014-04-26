/*
 * Problem 9
 * Special Pythagorean triplet
 *
 * A Pythagorean triplet is a set of three natural numbers, 
 * a < b < c, for which,
 * 
 * a^2 + b^2 = c^2
 * For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
 * 
 * There exists exactly one Pythagorean triplet for which a + b + c = 1000.
 * Find the product abc.
 *
 */

package main

import (
    "fmt"
    "math"
)


func main() {
    var i uint64 = 1
    var j uint64 = 1
    for i = 1; i < 1000; i++ {
        for j = 1; j < 1000; j++ {
            rhs := i*i + j*j
            c := uint64(math.Sqrt(float64(i*i + j*j)))
            if rhs != c*c {
                continue
            }
            if (i + j + c == 1000) {
                fmt.Println(i, j, c, i * j * c)
                return
            }
        }
    }
}    