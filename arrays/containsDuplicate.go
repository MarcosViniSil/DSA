package main
/*

link problem leetcode -> https://leetcode.com/problems/contains-duplicate/
time complexity  -> O(n)
space complexity -> O(n)

*/
func containsDuplicate(nums []int) bool {
	if len(nums) == 0 || len(nums) == 1{
		return false
	}
    mymap := make(map[int]int)

	for _, v := range nums {
		if mymap[v] == 1{
			return true
		}
		mymap[v] += 1
	}

	return false
}


