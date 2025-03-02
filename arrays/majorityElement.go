package main

/*

link problem leetcode -> https://leetcode.com/problems/majority-element
time complexity  -> O(n)
space complexity -> O(n)

*/

func majorityElement(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}

	mymap := make(map[int]int)

	for i := 0; i < len(nums); i++ {
		mymap[nums[i]] += 1
	}

	max := 0
	number := 0
	for k := range mymap {
		if mymap[k] > max {
			max = mymap[k]
			number = k
		}
	}

	if max > len(nums)/2 {
		return number
	}
	return 0
}
