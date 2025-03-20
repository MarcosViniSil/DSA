package main


/*

link problem leetcode -> https://leetcode.com/problems/spiral-matrix/

time complexity  -> O(k)
space complexity -> O(k)

k = m x n, where m number of rows and n number os columns

*/

const SEEN = -101
func spiralOrder(matrix [][]int) []int {

	if len(matrix) == 1{
		return matrix[0]
	} 

	arrayLeft := 0
	arrayRight := len(matrix) - 1 

	result := []int{}

	
	for arrayLeft <= arrayRight {
		logicLeftToRight(matrix,&result,arrayLeft)
		arrayLeft ++
		logicRightToLeft(matrix,&result,arrayRight)
		arrayRight --
	}
	return result
}

func logicLeftToRight(matrix [][]int ,result *[]int,arrayLeft int){
	for i, value := range matrix[arrayLeft] {
		if value != SEEN{
			*result = append(*result, value)
			matrix[arrayLeft][i] = SEEN

		}
	}

	positionFirstValue := 0
	for i := len(matrix[arrayLeft + 1]) - 1; i >= 0; i-- {
		if matrix[arrayLeft + 1][i] != SEEN {
			positionFirstValue = i
			break
		}
	}

	for i := 0; i < len(matrix); i++ {
		if matrix[i][positionFirstValue] != SEEN{
			*result = append(*result, matrix[i][positionFirstValue])
			matrix[i][positionFirstValue] = SEEN
		}
	}	
}

func logicRightToLeft(matrix [][]int ,result *[]int,arrayRight int){
	for i := len(matrix[arrayRight]) - 1; i >= 0; i-- {
		if matrix[arrayRight][i] != SEEN{
			*result = append(*result, matrix[arrayRight][i])
			matrix[arrayRight][i] = SEEN

		}
	}

	positionFirstValue := 0
	for i := 0; i < len(matrix[arrayRight - 1]); i++ {
		if matrix[arrayRight - 1][i] != SEEN {
			positionFirstValue = i
			break
		}
	}
	for i := len(matrix) - 1 ;i >= 0; i-- {
		if matrix[i][positionFirstValue] != SEEN{
			*result = append(*result, matrix[i][positionFirstValue])
			matrix[i][positionFirstValue] = SEEN
		}
	}	
}


