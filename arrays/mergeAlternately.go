package main

import (
	"strings"
)

/*

link problem leetcode -> https://leetcode.com/problems/merge-strings-alternately/
time complexity  -> O(n)
space complexity -> O(n) 

*/

func mergeAlternately(word1 string, word2 string) string {
	var builder strings.Builder
	i := 0
	for i < len(word1) && i < len(word2) {
		builder.WriteString(string(word1[i]))
		builder.WriteString(string(word2[i]))
		i++
	}

	if i < len(word1) {
		builder.WriteString(string(word1[i:]))
	}

	if i < len(word2) {
		builder.WriteString(string(word2[i:]))
	}

	return builder.String()

}

