package main

import ("fmt")

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



func main() {
    prices := []int{3,3}
	fmt.Println(containsDuplicate(prices))
}