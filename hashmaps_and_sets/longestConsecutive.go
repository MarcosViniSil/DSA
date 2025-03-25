package main

import (
	"fmt"
	
)
/*

link leetcode problem -> https://leetcode.com/problems/longest-consecutive-sequence

time complexity  -> O(n)

space complexity -> O(n)

*/

func max(a,b int) int {
	if a > b {
		return a
	}

	return b
}

func longestConsecutive(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	mymap := make(map[int]bool)
	result := 0
	for _, num := range nums {
		mymap[num] = true
	}
	for key := range mymap {
		
		if !mymap[key - 1] {
			resultActual := 0
			actual := key 

			for mymap[actual] {
				resultActual ++
				actual += 1
			}

			result = max(result,resultActual)

		}
	}

	return result
}

func main() {
	nums := []int{1,0,1,2}
	fmt.Println(longestConsecutive(nums))
}