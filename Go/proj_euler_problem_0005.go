/*
 * Problem 5
 * Smallest multiple
 *
 * 2520 is the smallest number that can be divided by each of the numbers
 * from 1 to 10 without any remainder.
 * 
 * What is the smallest positive number that is evenly divisible by all
 * of the numbers from 1 to 20?
 *
 */

/*
 * Sketch of Solution
 *
 * To find out LCM of two numbers x and y, express them as product of 
 * unique primes.
 * For each of the primes that are used to represent x and y find the maximum
 * power used for that prime between the two numbers
 * Calculate LCM = p1**power_max1 * p2**power_max2
 *
 * To solve the given problem find the LCM of all numbers from 1 to 20
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
    var a uint64 = 20
    var i uint64 = 1
    primes := make([]uint64, 0)
    
    // We need to find primes that can possibly appear 
    // in the unique factorization of any of the numbers
    // from 1 to 20
    
    for i = 2; i <= a; i++ {
        if isPrime(i) {
            primes = append(primes, i)
        }
    }   

    powers := make([]uint64, len(primes))

    // For each such prime find the maximum power used in any of the
    // numbers from 1 to 20
    
    for i = 1; i <= a; i++ {
        for j := 0; j < len(primes); j++ {
            var index uint64 = 0 //powers[j]
            temp := i
            prime := primes[j]
            
            for temp > 0 {
                if temp % prime == 0 {
                    index++
                    temp /= prime
                } else {
                    break
                }
            }
            if powers[j] < index {
                powers[j] = index
            }
        }
    }
    
    // Calculate LCM by multiplying each of the prime raised to its maximum power 
    // used in unique factorization of each of the number from 1 to 20
    
    var lcm uint64 = 1    
    for i = 0; i < uint64(len(primes)); i++ {
        lcm *= uint64(math.Pow(float64(primes[i]), float64(powers[i])))
    }
    fmt.Println(lcm)
}