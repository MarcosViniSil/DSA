#Link to problem: https://leetcode.com/problems/valid-palindrome/description/
#Time complexity:O(n)
#Space complexity: O(n)
                       
class Solution:
    def valid_palindrome(self,s:str) -> bool:
        s_temp = []
        for letter in s:
            if letter.isalnum():
                s_temp.append(letter.lower())

        s = ''.join(s_temp)
        left,right = 0,len(s) - 1

        while left < right:
            
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True

                                        
solution = Solution()
print(solution.valid_palindrome("A man, a plan, a canal: Panama"))
print(solution.valid_palindrome("race a car"))
print(solution.valid_palindrome(" "))
print(solution.valid_palindrome("0P"))
