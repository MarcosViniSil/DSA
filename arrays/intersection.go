package main


/*

link problem leetcode -> https://leetcode.com/problems/intersection-of-two-arrays

time complexity  -> O(k + v)
where k is the length of nums1 and v nums2

space complexity -> O(k)
k is the length of nums1, because the map, in the worst case has the same lenght that nums1

*/

func intersection(nums1 []int, nums2 []int) []int {
	mymap := make(map[int]bool)

	for _, value := range nums1 {
		mymap[value] = true
	}
	vetResult := []int{}
	for _, value := range nums2 {
		if va, _ := mymap[value]; va {
			vetResult = append(vetResult, value)
			mymap[value] = false
		}
	}

	return vetResult
}


