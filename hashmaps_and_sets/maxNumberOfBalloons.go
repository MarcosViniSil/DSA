package main

import (
	"math"
)


/*

link leetcode problem -> https://leetcode.com/problems/maximum-number-of-balloons/

time complexity  -> O(n)
where n is the length of text

space complexity -> O(1)

*/

func maxNumberOfBalloons(text string) int {
	mymap := buildMap()
	BALLOON_WORD_LENGTH := 7.0
	for _, v := range text {
		if _,ok := mymap[v] ; ok {
			mymap[v] += 1
		}
	}
	sum := 0
	for _,v := range mymap {
		sum += v
	}

	numberWordExtimate := int(math.Floor(float64(sum) / BALLOON_WORD_LENGTH ))
	count := 0
	for i:=0 ; i < numberWordExtimate ; i++{
		if mymap['b'] - 1 >= 0 && mymap['a'] - 1 >= 0 && mymap['l'] - 2 >= 0 && mymap['o'] - 2 >= 0 && mymap['n'] - 1 >= 0{
			balloonWordFind(mymap)
			count++
		}
	}

	return count
}


func balloonWordFind(mymap map[rune]int){
	mymap['b'] -= 1
	mymap['a'] -= 1
	mymap['l'] -= 2
	mymap['o'] -= 2
	mymap['n'] -= 1
}

func buildMap() map[rune]int{
	mymap := make(map[rune]int)

	mymap['b'] = 0
	mymap['a'] = 0
	mymap['l'] = 0
	mymap['o'] = 0
	mymap['n'] = 0

	return mymap
}



