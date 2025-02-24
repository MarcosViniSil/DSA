package main 


import ("fmt")

// link problem leet code -> https://leetcode.com/problems/two-sum/

// time complexity  -> O(n^2)
// space complexity -> O(1)

func twoSum(nums []int, target int) []int {
	var numsR = make([]int, 2)
	if len(nums) == 2 {
		numsR[0] = 0
		numsR[1] = 1
		return numsR
	}

	left := 0
	right := len(nums) - 1

	for i := 0 ; i < len(nums);i++ {
		for j := 0 ; left < right ; j++ {
			if nums[left] + nums[right] == target {
				numsR[0] = left
				numsR[1] = right
				return numsR
			}else{
				left++
			}

		}
		left = 0
		right = right - 1
	} 
	
	return nil
} 

func main(){
	nums := []int{3,2,4}
	fmt.Println(twoSum(nums,6))
}