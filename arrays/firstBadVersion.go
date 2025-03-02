package main


/*

link problem leetcode -> https://leetcode.com/problems/first-bad-version
time complexity  -> O(log(n))
space complexity -> O(1)

*/
func isBadVersion(version int) bool;

func firstBadVersion(n int) int {
	l,r := 1,n
	middle := 0
	for l < r {
		
		middle = (l + r) / 2
		if isBadVersion(middle){
			r = middle
		}else{
			l = middle + 1
		}
	}  
 
	return l
 }