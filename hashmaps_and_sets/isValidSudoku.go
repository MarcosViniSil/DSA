package main

import "fmt"

/*

link leetcode problem -> https://leetcode.com/problems/valid-sudoku

time complexity  -> O(1)
Because the input is always the same, a board 9x9

space complexity -> O(1)

*/

func isValidSudoku(board [][]byte) bool {
	mapRows := make(map[byte]byte,9)
	mapColumns := make(map[byte]byte,9)

	if !checkEachBox3X3(board, mapRows) {
		return false
	}
	cleanMap(mapRows)

	return verifyRowsAndColumns(board, mapRows,mapColumns)

}

func verifyRowsAndColumns(board [][]byte, mapRows map[byte]byte,mapColumns map[byte]byte) bool {
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			if board[i][j] != 46 {
				if mapRows[board[i][j]] > 0 {
					return false
				}
				mapRows[board[i][j]] += 1
			}
			if board[j][i] != 46 {
				if mapColumns[board[j][i]] > 0 {
					return false
				}
				mapColumns[board[j][i]] += 1
			}
		}
		cleanMap(mapRows)
		cleanMap(mapColumns)
	}

	return true
}

func checkEachBox3X3(board [][]byte, mymap map[byte]byte) bool {
	for row := 0; row < 9; row += 3 {
		for col := 0; col < 9; col += 3 {
			cleanMap(mymap)

			for i := 0; i < 3; i++ {
				for j := 0; j < 3; j++ {
					if board[row+i][col+j] != 46 { 
						if mymap[board[row+i][col+j]] > 0 {
							return false
						}
						mymap[board[row+i][col+j]] += 1
					}
				}
			}
		}
	}
	return true
}



func cleanMap(mymap map[byte]byte) {
	for key := range mymap {
		mymap[key] = 0
	}
}

func main() {
	sudoku := [][]byte{{'.','.','.','.','5','.','.','1','.'},
		{'.','4','.','3','.','.','.','.','.'},
		{'.','.','.','.','.','3','.','.','1'},
		{'8','.','.','.','.','.','.','2','.'},
		{'.','.','2','.','7','.','.','.','.'},
		{'.','1','5','.','.','.','.','.','.'},
		{'.','.','.','.','.','2','.','.','.'},
		{'.','2','.','9','.','.','.','.','.'},
		{'.','.','4','.','.','.','.','.','.'}}

	fmt.Println(isValidSudoku(sudoku))
}
