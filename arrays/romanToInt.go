package main

/*

link problem leetcode -> https://leetcode.com/problems/two-sum/
time complexity  -> O(n)
space complexity -> O(1)

*/
func romanToInt(s string) int {
	subtraction := buildMap()
	values := buildValues()

	if len(s) == 1{
		return values[s]
	}else if len(s) == 2{
		if val, ok := subtraction[string(s[0]) + string(s[1])]; ok {
			return val
		}
		return values[string(s[0])] + values[string(s[1])]
	}

	sum := 0

	actual := len(s) - 1
	next := len(s) - 2 

	for next >= 0 && actual >= 0 {
		if val, ok := subtraction[string(s[next]) + string(s[actual])]; ok {
			sum += val
			next -= 2
			actual -=2 
		}else{
			sum += values[string(s[actual])] 
			next -= 1
			actual -= 1 
		}
	}


	if actual == 0 {
		sum += values[string(s[actual])]
	}

	
	return sum

}

func buildValues() map[string]int{
	mymap := make(map[string]int)
	mymap["I"] = 1
	mymap["V"] = 5
	mymap["X"] = 10
	mymap["L"] = 50
	mymap["C"] = 100
	mymap["D"] = 500
	mymap["M"] = 1000

	return mymap
}

func buildMap() map[string]int {
	mymap := make(map[string]int)
	mymap["IV"] = 4
	mymap["IX"] = 9
	mymap["XL"] = 40
	mymap["XC"] = 90
	mymap["CD"] = 400
	mymap["CM"] = 900

	return mymap
}

