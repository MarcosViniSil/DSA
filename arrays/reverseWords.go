package main

/*

link problem leetcode -> https://leetcode.com/problems/reverse-words-in-a-string-iii
time complexity  -> O(n)
space complexity -> O(n)

*/
func reverseWords(s string) string {
	newString := []rune(s)
	left := 0
	right := 0
	for i := 0; i <= len(newString); i++ {
		if i == len(newString) || newString[i] == 32 {
			right = i - 1
			invertString(newString, left, right)
			left = i + 1
		}
	}
	return string(newString)
}

func invertString(v []rune, left, right int) {
	for left < right {
		v[left], v[right] = v[right], v[left]
		left++
		right--
	}
}
