package main

/*

link problem leetcode -> https://leetcode.com/problems/two-sum/
time complexity  -> O(n)
space complexity -> O(n)

*/
func twoSum(nums []int, target int) []int {
	mymap := make(map[int]int)

	for i, v := range nums {
		mymap[v] = i
	}

	
	for i, v := range nums {
		diff := target - v
		if va, ok := mymap[diff]; ok && va != i {
			return []int{va,i}
		}
	}

	

	return nil
} 

