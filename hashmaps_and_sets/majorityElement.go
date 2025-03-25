package main

/*

link leetcode problem -> https://leetcode.com/problems/majority-element

time complexity  -> O(n)

space complexity -> O(1)

*/

func majorityElement(nums []int) int {
	count := 0
	var actual int

	for _, num := range nums {
		if count == 0 {
			actual = num
		}

		if actual == num {
			count++
		}else{
			count--
		}
	}

	return actual
}

