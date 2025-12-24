#Link to problem: https://leetcode.com/problems/ransom-note/description/
#Time complexity: O(N + M), where N = len(ransomNote) and M = len(magazine)
#Space complexity: O(K), where K = len(magazine)

from collections import defaultdict          

class Solution:
    def ransom_note(self,ransomNote:str,magazine:str) -> bool:
        magazine_map = defaultdict(int)
        
        for letter in magazine:
            magazine_map[letter] += 1

       
        for note in ransomNote:
            if magazine_map[note] <= 0:
                return False
            
            magazine_map[note] -= 1
        
        return True

                                        
solution = Solution()
print(solution.ransom_note("a","b"))
print(solution.ransom_note("aa","ab"))
print(solution.ransom_note("aa","aab"))
