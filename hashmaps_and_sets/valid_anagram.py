#Link to problem: https://leetcode.com/problems/valid-anagram/description/
#Time complexity: O(n) 
#Space complexity: O(1)
                       
class Solution:
    def valid_anagram(self,s:str,t:str) -> bool:
        if len(s) != len(t):
            return False

        letters_count = [0 for _ in range(27)]
        a_asc_code = ord('a')
        
        for letter in s:
            letters_count[ord(letter) - a_asc_code] += 1

        for letter in t:
            idx = ord(letter) - a_asc_code
            if letters_count[idx] - 1 < 0:
                return False
            
            letters_count[idx] -= 1
        
        return True

                                        
solution = Solution()
print(solution.valid_anagram("anagram","nagaram"))
print(solution.valid_anagram("rat","car"))
