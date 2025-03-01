package main

import "fmt"

func abs(x int) int {
	if x < 0 {
		return -x
	} else {
		return x
	}
}
/*

link problem leetcode -> https://leetcode.com/problems/contains-duplicate-ii
time complexity  -> O(n)
space complexity -> O(n)

*/

func containsNearbyDuplicate(nums []int, k int) bool {
	if k == 0 && len(nums) == 1 {
		return true
	}

	mymap := make(map[int]int)

	for i, v := range nums {
		if value, exists := mymap[v]; exists {
			if abs(value-i) <= k {
				return true
			}else{
				mymap[v] = i
			}
		} else {
			mymap[v] = i
		}
	}

	return false
}

func main() {
	v := []int{1,2,3,1,2,3}
	fmt.Println(containsNearbyDuplicate(v, 2))
}
