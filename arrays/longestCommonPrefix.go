package main

import (
	"strings"
)

/*

link problem leetcode -> https://leetcode.com/problems/longest-common-prefix
time complexity  -> O(n x m)
Where, n is the lenght of the lower string and m is the lenght of strs
space complexity -> O(1)

*/

func longestCommonPrefix(strs []string) string {


	lowerString := 200

	for _, v := range strs {
		if len(v) == 0 {
			return ""
		}
		if len(v) < lowerString{
			lowerString = len(v)
		}
	}

	var stringResult strings.Builder
	i := 0
	var actualLetter byte 

	for i < lowerString {
		
		actualLetter = strs[0][i]

		for _, word := range strs {
			if word[i] != actualLetter{
				return stringResult.String()
			}
		}
		stringResult.WriteByte(actualLetter)
		i++
	}

	return stringResult.String()
}

