package main

/*

link leetcode problem -> https://leetcode.com/problems/ransom-note

time complexity  -> O(n)
where n is the length of ransomNote 

space complexity -> O(v)
where v is the length of magazine

*/

func canConstruct(ransomNote string, magazine string) bool {
	mymap := make(map[rune]int)

	for _, letter := range magazine {
		mymap[letter] += 1
	}

	for _, value := range ransomNote {
		if mymap[value] > 0 {
			mymap[value] -= 1
		}else{
			return false
		}
	}

	return true
}

