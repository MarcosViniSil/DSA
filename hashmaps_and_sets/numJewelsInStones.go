package main

/*

link leetcode problem -> https://leetcode.com/problems/jewels-and-stones

time complexity  -> O(n)
where n is the length of stones

space complexity -> O(v)
where v is the length of jewels

*/
func numJewelsInStones(jewels string, stones string) int {
	mymap := make(map[rune]bool)
	result := 0
	for _, jewel := range jewels {
		mymap[jewel] = true
	}

	for _, stone := range stones {
		if _,ok := mymap[stone] ; ok {
			result++
		}
	}
	return result
}

