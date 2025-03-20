package main

/*

link leetcode problem -> https://leetcode.com/problems/product-of-array-except-self
time complexity  -> O(n)
space complexity -> O(1)

*/

func productExceptSelf(nums []int) []int {
	result := make([]int,len(nums))

	left:=1
	for i := 0; i < len(nums); i++ {
		result[i] = left
		left *= nums[i]
	}

	right := 1
	for i := len(nums) -1; i >= 0; i-- {
		result[i] *= right
		right *= nums[i]
	}


	return result
}

