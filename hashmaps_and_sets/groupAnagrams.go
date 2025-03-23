package main

import (
	"fmt"
	"math/big"
)

/*

link leetcode problem -> https://leetcode.com/problems/group-anagrams

time complexity  -> O(n * k)

space complexity -> O(n * k)

where n is the length of strs and k length of strs[i]
*/

func groupAnagrams(strs []string) [][]string {
	result := [][]string{}

	primes := map[rune]int64{
		'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19,
		'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53,
		'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89,
		'y': 97, 'z': 101,
	}


	mymap := make(map[string]int)
	positionArray := 0

	for _, word := range strs {
		prod := big.NewInt(1) 

	
		for _, char := range word {
			prod.Mul(prod, big.NewInt(primes[char]))
		}

		prodStr := prod.String()


		if pos, ok := mymap[prodStr]; !ok {
			mymap[prodStr] = positionArray
			result = append(result, []string{word})
			positionArray++
		} else {
			result[pos] = append(result[pos], word)
		}
	}

	return result
}





func main() {
	strs := []string{"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"}
	fmt.Println(groupAnagrams(strs))
}

/*
97 -> a
98 -> b
101 -> e 33
110 -> n
116 -> t

*/
