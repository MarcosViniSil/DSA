#Link to problem: https://leetcode.com/problems/longest-common-prefix/description/
#Time complexity: O(n * m), where: n = quantity  of strings and m = length of the smallest string
#Space complexity: O(m), where m = length of smallest string

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        min_length = float("inf")
        for word in strs:
            if len(word) == 0:
                return ""
            if len(word) < min_length:
                min_length = len(word)

        longest_prefix = []
    
        for i in range(min_length):
            last_word = strs[0][i]
            for word in strs:
                if word[i] != last_word:
                    return ''.join(longest_prefix)
            
            longest_prefix.append(last_word)
        
        return ''.join(longest_prefix)    

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["dog","racecar","car"]))
print(solution.longestCommonPrefix(["ab","a"]))