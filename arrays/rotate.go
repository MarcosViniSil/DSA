package main

import "fmt"
/*

link problem leetcode -> https://leetcode.com/problems/rotate-image/

time complexity  -> O(k^2)
k = m x n, where m is equal of number of rows and n equal number of columns

space complexity -> O(1)

*/

func rotate(matrix [][]int) {
	transpose(matrix)
	swapElements(matrix)
	
}

func swapElements(matrix [][]int){
	left := 0 
	right := len(matrix[0]) - 1
    temp := 0
	for i := 0; i < len(matrix); i++ {
		for left < right {
			temp = matrix[i][left]
			matrix[i][left] = matrix[i][right]
			matrix[i][right] = temp

			left++
			right--
		}
		left = 0 
		right = len(matrix[0]) - 1 
	}
}

func transpose(matrix [][]int){
	temp := 0
	for i := 0; i < len(matrix); i++ {
		for j := i + 1; j < len(matrix); j++ {
			temp = matrix[i][j]
			matrix[i][j] = matrix[j][i]
			matrix[j][i] = temp
		}
	}
}

func main() {
	nums := [][]int{{5,1,9,11}, {2,4,8,10},{13,3,6,7},{15,14,12,16}}
	rotate(nums)
	fmt.Println(nums)
}