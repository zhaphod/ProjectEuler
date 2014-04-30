/*
 * Problem 15
 * Lattice paths
 * 
 * Starting in the top left corner of a 2×2 grid, and only being able 
 * to move to the right and down, there are exactly 6 routes to the 
 * bottom right corner.
 * 
 * How many such routes are there through a 20×20 grid?
 *
 */

/*
 * Sketch of solution
 *
 * In a NxN grid to reach from one corner to the opposite corners, one
 * has to move N steps in horizontal direction and N steps in vertical
 * direction irrespective of the path chosen.
 *
 * Following is one such example route:
 *      L D L D .... L
 * This path can be treated as a string having 2*N symbols.
 * In order to find all such route we just have to find all the
 * permutations of such a string. Since N such symbols are L and
 * N other symbols are D the final number of routes becomes:
 *  Total routes = (2N)! / (N! * N!)
 *
 */
package main

import (
    "fmt"
)
func main() {
    var num_routes uint64 = 1
    var i uint64 = 0
    var j uint64 = 0
    
    for i = 22; i <= 40; i+=2 {
        num_routes *= i

        j = i / 2
        
        num_routes /= j
        
        fmt.Println(i, j)
    }
    
    for i = 21; i <= 39; i += 2 {
        num_routes *= i
    }
    
    for i = 1; i <=10 ; i++ {
        num_routes /= i
    }
    
    fmt.Println(num_routes)
}    