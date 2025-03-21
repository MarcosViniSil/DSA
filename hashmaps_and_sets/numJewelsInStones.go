package main

import "fmt"

/*

link leetcode problem -> https://leetcode.com/problems/jewels-and-stones

time complexity  -> O(n + m)
where n is the length of jewels and m length of stones

space complexity -> O(n)

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

func main() {
	jewels := "z"
	stones := "ZZ"

	fmt.Println(numJewelsInStones(jewels, stones))
}