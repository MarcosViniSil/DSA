package main

/*

link leetcode problem -> https://leetcode.com/problems/remove-duplicates-from-sorted-array
time complexity  -> O(n)
space complexity -> O(1)

*/

func RemoveDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	j := 1

	for i := 1; i < len(nums); i++ {
		if nums[i] != nums[i-1] {
			nums[j] = nums[i]
			j++
		}
	}

	return j
}
