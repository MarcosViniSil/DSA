package main

import (
	"sort"
)

/*

link problem leetcode -> https://leetcode.com/problems/merge-intervals/
time complexity  -> O(n.log(n))
space complexity -> O(n)

*/

func merge(intervals [][]int) [][]int {
	sortInterval(intervals)
	result := [][]int{}

	for _, cell := range intervals {
		if len(result) == 0 || cell[0] > result[len(result)-1][1] {
			result = append(result, cell)
		} else {
			result[len(result)-1][1] = max(cell[1], result[len(result)-1][1])
		}

	}

	return result
}

func sortInterval(intervals [][]int) {
	sort.SliceStable(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
}

func max(a, b int) int {
	if a < b {
		return b
	} else {
		return a
	}
}


