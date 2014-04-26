/*
 * Problem 4
 * Largest palindrome product
 *
 * A palindromic number reads the same both ways. The largest palindrome
 * made from the product of two 2-digit numbers is 9009 = 91 × 99.
 * 
 * Find the largest palindrome made from the product of two 3-digit numbers.
 *
 */

package main

import (
    "fmt"
    "strconv"
)

func isPalindrome(a string) bool {
    var length int = len(a)
    for i := 0; i < length / 2; i++ {
        if a[i] != a[length - i - 1] {
            return false
        }
    }
    return true
}

func main() {
    var a int = 100
    var b int = 100
    var ab int = 1
    var ab_s string = ""
    var max_palindrome = 1
    
    for a = 999; a >= 100; a-- {
        if a * 999 < max_palindrome {
            break
        }
        for b = 999; b >= 100; b-- {
            ab = a * b
            if ab < max_palindrome {
                break
            }
            ab_s = strconv.FormatInt(int64(ab), 10)
            if isPalindrome(ab_s) {
                if ab > max_palindrome {
                    max_palindrome = ab
                }
            }
        }
    }
    
    fmt.Println(max_palindrome)
}    