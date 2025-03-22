package main

/*

link leetcode problem -> https://leetcode.com/problems/valid-anagram/description/

time complexity  -> O(n)
where n is the length of s 

space complexity -> O(v)
where v is the length of t

*/
func isAnagram(s string, t string) bool {
	if len(s) != len(t){
		return false
	}
    mymap := make(map[rune]int)

	for _, value := range t {
		mymap[value] += 1
	}

	for _, value := range s {
		if mymap[value] > 0 {
			mymap[value] -= 1
		}else{
			return false
		}
	}

	return true
}

