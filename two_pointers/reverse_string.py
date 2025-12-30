#Link to problem: https://leetcode.com/problems/reverse-string/description/
#Time complexity:O(n)
#Space complexity:O(1) 
                       
class Solution:
    def reverse_string(self,s:list[str]) -> None:
        left, right = 0, len(s) - 1

        while left <= right:
            s[left],s[right] = s[right],s[left]

            left += 1
            right -= 1 

                                        
solution = Solution()
s = ["h","e","l","l","o"]
solution.reverse_string(s)
print(s)

s = ["H","a","n","n","a","h"]
solution.reverse_string(s)
print(s)