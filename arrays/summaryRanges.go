package main

import (
	"fmt"
	"strings"
)
/*

link leetcode problem -> https://leetcode.com/problems/summary-ranges/

time complexity  -> O(n)
space complexity -> O(n)

*/
func summaryRanges(nums []int) []string {
	if len(nums) == 0 {
		return []string{}
	}
	var stringResult []string
	var sequence strings.Builder
	startSequence := nums[0]
	endSequence := nums[0]

	i:= 0
	j:= 1

	for j < len(nums) {
		if nums[i] == nums[j] - 1{
			endSequence = nums[j]
		}else{
			sequence.WriteString(fmt.Sprintf("%d->%d", startSequence, endSequence))
			
			if startSequence == endSequence{
				sequence.Reset()
				sequence.WriteString(fmt.Sprintf("%d",endSequence))
				
			} 
			stringResult = append(stringResult,sequence.String())
			sequence.Reset()
			startSequence = nums[j]
			endSequence = nums[j]
		}
		i++
		j++
	}

	sequence.WriteString(fmt.Sprintf("%d->%d", startSequence, endSequence))
	if startSequence == endSequence{
		sequence.Reset()
		sequence.WriteString(fmt.Sprintf("%d",endSequence))
		
	} 
	stringResult = append(stringResult,sequence.String())
	sequence.Reset()

	return stringResult

}

