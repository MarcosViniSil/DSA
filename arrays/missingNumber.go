package main

/*

link problem leetcode -> https://leetcode.com/problems/majority-element


Sum of Gauss has the following formula:

sum = n * (n + 1)
	  ----------
	      2

in the end, we have the sum of the n first numbers.

time complexity  -> O(n)
space complexity -> O(1)

*/

func sum(nums []int) int {
	sum:= 0

	for _, value := range nums {
		sum += value
	}

	return sum
}

func missingNumber(nums []int) int {
    n := len(nums)
	expected := (n * (n + 1)) / 2
	actual := sum(nums)

	return expected - actual


}
